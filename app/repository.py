from __future__ import annotations

from typing import List, Optional

from .models import RentalListing


class ListingRepository:
    def __init__(self) -> None:
        self._next_id = 100
        self._listings: List[RentalListing] = [
            RentalListing(
                id=1,
                title="1 BHK near Hinjewadi Phase 1",
                area="Hinjewadi",
                rent=14500,
                deposit=30000,
                bhk="1 BHK",
                furnishing="Semi-furnished",
                available_from="Available now",
                description="Good for IT professionals. Gated society, lift, backup power and bike parking.",
                owner_name="Amit Kulkarni",
                phone="98765432",
                posted_label="Posted today",
            ),
            RentalListing(
                id=2,
                title="2 BHK family flat in Kothrud",
                area="Kothrud",
                rent=24000,
                deposit=60000,
                bhk="2 BHK",
                furnishing="Fully furnished",
                available_from="Available in 1 week",
                description="Near metro and schools. Includes wardrobes, sofa, geyser and covered parking.",
                owner_name="Neha Deshpande",
                phone="98230111",
                posted_label="Posted 2 days ago",
            ),
            RentalListing(
                id=3,
                title="Studio for students in Viman Nagar",
                area="Viman Nagar",
                rent=12000,
                deposit=25000,
                bhk="Studio",
                furnishing="Furnished",
                available_from="Available now",
                description="Close to colleges and Phoenix Mall. Best for students or working bachelors.",
                owner_name="Sana Shaikh",
                phone="97644588",
                posted_label="Posted today",
            ),
            RentalListing(
                id=4,
                title="2 BHK near Magarpatta City",
                area="Hadapsar",
                rent=22000,
                deposit=50000,
                bhk="2 BHK",
                furnishing="Semi-furnished",
                available_from="Available next month",
                description="Spacious flat with balcony, security and children's play area.",
                owner_name="Rohit Jagtap",
                phone="98900123",
                posted_label="Posted 3 days ago",
            ),
            RentalListing(
                id=5,
                title="1 RK budget room in Baner",
                area="Baner",
                rent=9000,
                deposit=18000,
                bhk="1 RK",
                furnishing="Unfurnished",
                available_from="Available now",
                description="Budget-friendly option with separate bathroom and easy commute to Aundh and Balewadi.",
                owner_name="Priya Patil",
                phone="99224477",
                posted_label="Posted yesterday",
            ),
        ]

    def areas(self) -> List[str]:
        base = ["All"]
        unique_areas = sorted({listing.area for listing in self._listings})
        return base + unique_areas

    def all(self, area: str = "All", query: str = "") -> List[RentalListing]:
        normalized_query = query.strip().lower()
        results = []
        for listing in self._listings:
            area_matches = area == "All" or listing.area == area
            query_matches = (
                not normalized_query
                or normalized_query in listing.title.lower()
                or normalized_query in listing.area.lower()
                or normalized_query in listing.bhk.lower()
            )
            if area_matches and query_matches:
                results.append(listing)
        return results

    def get(self, listing_id: int) -> Optional[RentalListing]:
        for listing in self._listings:
            if listing.id == listing_id:
                return listing
        return None

    def create(
        self,
        *,
        title: str,
        area: str,
        rent: int,
        deposit: int,
        bhk: str,
        furnishing: str,
        available_from: str,
        description: str,
        owner_name: str,
        phone: str,
    ) -> RentalListing:
        listing = RentalListing(
            id=self._next_id,
            title=title,
            area=area,
            rent=rent,
            deposit=deposit,
            bhk=bhk,
            furnishing=furnishing,
            available_from=available_from,
            description=description,
            owner_name=owner_name,
            phone=phone,
            posted_label="Posted today",
        )
        self._next_id += 1
        self._listings.insert(0, listing)
        return listing


repository = ListingRepository()
