from app.domain.entities import Address, Coordinates


class MockPaymentService:
    def __init__(self, should_succeed: bool = True):
        self.should_succeed = should_succeed
        self.calls: list[tuple[str, float, str]] = []

    def process_payment(
        self, credit_card_number: str, amount: float, description: str
    ) -> bool:
        self.calls.append((credit_card_number, amount, description))
        return self.should_succeed


class MockGeocodingService:
    def __init__(self, default_coordinates: Coordinates | None = None):
        self.default_coordinates = default_coordinates or Coordinates(
            latitude=0.0, longitude=0.0
        )
        self.calls: list[Address] = []
        self._responses: dict[Address, Coordinates] = {}

    def set_response(self, address: Address, coordinates: Coordinates) -> None:
        self._responses[address] = coordinates

    def geocode(self, address: Address) -> Coordinates:
        self.calls.append(address)
        return self._responses.get(address, self.default_coordinates)


class MockWarehouseRepository:
    def __init__(self, warehouses: list):
        self.warehouses = warehouses
        self.calls: list[tuple] = []

    def get_all(self) -> list:
        self.calls.append(())
        return self.warehouses
