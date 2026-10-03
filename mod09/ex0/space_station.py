#!/usr/bin/env python3

from pydantic import BaseModel, Field, PastDatetime, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: PastDatetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def print_station(station: SpaceStation) -> None:
    print(
        f"ID: {station.station_id}\n"
        f"Name: {station.name}\n"
        f"Crew: {station.crew_size} people\n"
        f"Power: {station.power_level}%\n"
        f"Oxygen: {station.oxygen_level}%\n"
        "Status: "
        f"{'Operational' if station.is_operational else 'Non-operational'}\n"
    )


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    print("Valid station created:")
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 10, 2, 23)
        )
        print_station(valid_station)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print("========================================")

    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="Invalid Station Test",
            crew_size=42,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 10, 2, 23)
        )
        print_station(invalid_station)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
