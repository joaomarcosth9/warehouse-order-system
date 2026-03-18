from uuid import uuid4

from app.domain.entities import (
    Address,
    CustomerId,
    Order,
    OrderId,
    OrderItem,
    OrderItemIntent,
)
from app.services.ports import PaymentService, GeocodingService, WarehouseRepository


class OrderService:
    def __init__(
        self,
        payment_service: PaymentService,
        geocoding_service: GeocodingService,
        warehouse_repository: WarehouseRepository,
    ):
        self.payment_service = payment_service
        self.geocoding_service = geocoding_service
        self.warehouse_repository = warehouse_repository

    def create_order(
        self,
        customer_id: CustomerId,
        shipping_address: Address,
        items: list[OrderItemIntent],
    ) -> Order:
        destination = self.geocoding_service.geocode(shipping_address)
        warehouses = self.warehouse_repository.get_all()

        candidate_warehouses = [
            warehouse for warehouse in warehouses if warehouse.can_fulfill(items)
        ]
        if not candidate_warehouses:
            raise ValueError("No warehouse can fulfill all requested items")

        selected_warehouse = min(
            candidate_warehouses,
            key=lambda warehouse: warehouse.coordinates.distance_to(destination),
        )

        # In a real implementation, prices would be fetched from a product catalog or similar service
        order_items = [
            OrderItem(product_id=item.product_id, quantity=item.quantity, price=10.0)
            for item in items
        ]

        order = Order(
            id=OrderId(str(uuid4())),
            customer_id=customer_id,
            shipping_address=shipping_address,
            items=order_items,
            status="created",
        )

        payment_description = f"Order for customer {customer_id.value} from warehouse {selected_warehouse.id.value}"

        # In a real implementation, credit card details would be securely handled and not hardcoded
        payment_success = self.payment_service.process_payment(
            credit_card_number="4111111111111111",
            amount=order.total_amount,
            description=payment_description,
        )

        if not payment_success:
            raise ValueError("Payment failed")

        return order
