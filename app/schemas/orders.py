from pydantic import BaseModel, Field
from app.domain.entities import Address, OrderItemIntent, ProductId


class AddressSchema(BaseModel):
    street: str = Field(min_length=1)
    city: str = Field(min_length=1)
    state: str = Field(min_length=1)
    zip_code: str = Field(min_length=1)

    def to_domain(self) -> Address:
        return Address(**self.model_dump())


class OrderItemSchema(BaseModel):
    product_id: str = Field(min_length=1)
    quantity: int = Field(gt=0)

    def to_domain(self) -> OrderItemIntent:
        return OrderItemIntent(
            product_id=ProductId(self.product_id), quantity=self.quantity
        )


class CreateOrderRequest(BaseModel):
    customer_id: str = Field(min_length=1)
    shipping_address: AddressSchema
    items: list[OrderItemSchema] = Field(min_length=1)


class CreateOrderResponse(BaseModel):
    order_id: str
    status: str
