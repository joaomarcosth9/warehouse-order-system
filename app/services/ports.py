from typing import Protocol

from app.domain.entities import Address, Coordinates, Warehouse


class PaymentService(Protocol):
    def process_payment(
        self, credit_card_number: str, amount: float, description: str
    ) -> bool:
        pass


class GeocodingService(Protocol):
    def geocode(self, address: Address) -> Coordinates:
        pass


class WarehouseRepository(Protocol):
    def get_all(self) -> list[Warehouse]:
        pass
