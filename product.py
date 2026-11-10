from Pyro5.api import expose

@expose
class Product:
    """A product whose methods can be called remotely through Pyro5 client."""

    def__init__(self, name: str, description: str, price: float) -> None:
        