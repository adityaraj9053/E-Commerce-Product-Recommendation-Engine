from dataclasses import dataclass, field

@dataclass
class User:

    user_id: int

    age: int

    city: str

    gender: str

    searches: list = field(default_factory=list)

    cart: list = field(default_factory=list)

    purchases: list = field(default_factory=list)

    ratings: dict = field(default_factory=dict)