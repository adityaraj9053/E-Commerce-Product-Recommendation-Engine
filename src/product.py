from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    name: str
    category: str
    brand: str
    price: int
    rating: float