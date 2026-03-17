from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt


@dataclass(frozen=True)
class CustomerId:
    value: str

    def __post_init__(self):
        if not self.value.strip():
            raise ValueError("CustomerId cannot be empty")


@dataclass(frozen=True)
class ProductId:
    value: str

    def __post_init__(self):
        if not self.value.strip():
            raise ValueError("ProductId cannot be empty")


@dataclass(frozen=True)
class OrderId:
    value: str

    def __post_init__(self):
        if not self.value.strip():
            raise ValueError("OrderId cannot be empty")


@dataclass(frozen=True)
class WarehouseId:
    value: str

    def __post_init__(self):
        if not self.value.strip():
            raise ValueError("WarehouseId cannot be empty")


@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    zip_code: str


@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float

    def distance_to(self, other: "Coordinates") -> float:
        earth_radius_km = 6371.0

        lat1 = radians(self.latitude)
        lon1 = radians(self.longitude)
        lat2 = radians(other.latitude)
        lon2 = radians(other.longitude)

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        haversine = (
            sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
        )
        return 2 * earth_radius_km * asin(sqrt(haversine))


@dataclass(frozen=True)
class OrderItemIntent:
    product_id: ProductId
    quantity: int


@dataclass(frozen=True)
class OrderItem:
    product_id: ProductId
    quantity: int
    price: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.price


@dataclass(frozen=True)
class Order:
    id: OrderId
    customer_id: CustomerId
    shipping_address: Address
    items: list[OrderItem]
    status: str

    @property
    def total_amount(self) -> float:
        return sum(item.subtotal for item in self.items)


@dataclass(frozen=True)
class Warehouse:
    id: WarehouseId
    name: str
    address: Address
    coordinates: Coordinates
    items_in_stock: dict[ProductId, int]

    def can_fulfill(self, items: list[OrderItemIntent]) -> bool:
        return all(
            self.items_in_stock.get(item.product_id, 0) >= item.quantity
            for item in items
        )
