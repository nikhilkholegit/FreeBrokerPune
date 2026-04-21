from dataclasses import dataclass


@dataclass
class RentalListing:
    id: int
    title: str
    area: str
    rent: int
    deposit: int
    bhk: str
    furnishing: str
    available_from: str
    description: str
    owner_name: str
    phone: str
    posted_label: str
