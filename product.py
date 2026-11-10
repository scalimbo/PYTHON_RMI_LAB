from Pyro5.api import expose

@expose
class Product:
    """A product whose methods can be called remotely through Pyro5 client."""

    def__init__(self, name: str, description: str, price: float) -> None:
        self._name = name
        self._description = description
        self._price = price

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_price(self) -> float:
        return self._price