from app.infrastructure.mocks import (
    MockGeocodingService,
    MockPaymentService,
    MockWarehouseRepository,
)
from app.services.order_service import OrderService
from app.domain.entities import Address, Coordinates, ProductId, Warehouse, WarehouseId

payment_mock = MockPaymentService(should_succeed=True)
geocoding_mock = MockGeocodingService()
warehouse_mock = MockWarehouseRepository(
    warehouses=[
        Warehouse(
            id=WarehouseId("wh-nyc"),
            name="Warehouse NYC",
            address=Address("11 W 34th St", "New York", "NY", "10001"),
            coordinates=Coordinates(latitude=40.7484, longitude=-73.9857),
            items_in_stock={ProductId("prod-1"): 20, ProductId("prod-2"): 10},
        ),
        Warehouse(
            id=WarehouseId("wh-jersey"),
            name="Warehouse Jersey",
            address=Address("30 Hudson St", "Jersey City", "NJ", "07302"),
            coordinates=Coordinates(latitude=40.7216, longitude=-74.0470),
            items_in_stock={ProductId("prod-1"): 200, ProductId("prod-2"): 200},
        ),
        Warehouse(
            id=WarehouseId("wh-buffalo-limited"),
            name="Warehouse Buffalo Limited",
            address=Address("1 Main St", "Buffalo", "NY", "14201"),
            coordinates=Coordinates(latitude=42.8864, longitude=-78.8784),
            items_in_stock={ProductId("prod-1"): 1000, ProductId("prod-2"): 0},
        ),
    ]
)

order_service_instance = OrderService(
    payment_service=payment_mock,
    geocoding_service=geocoding_mock,
    warehouse_repository=warehouse_mock,
)

geocoding_mock.set_response(
    Address("123 Tech Ave", "New York", "NY", "10001"),
    Coordinates(latitude=40.7506, longitude=-73.9972),
)
geocoding_mock.set_response(
    Address("Main St", "Buffalo", "NY", "14201"),
    Coordinates(latitude=42.8864, longitude=-78.8784),
)


def get_order_service() -> OrderService:
    return order_service_instance
