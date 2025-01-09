from pydantic import BaseModel


class TravelEntry(BaseModel):
    destination: str
    departure: str
    arrival: str
