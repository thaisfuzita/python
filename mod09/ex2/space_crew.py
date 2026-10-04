#!/usr/bin/env python3

from pydantic import (BaseModel, Field, ValidationError, model_validator)
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def safety_requirements(self) -> "SpaceMission":
        if self.mission_id[:1] != "M":
            raise ValueError('Mission ID must start with "M"')
        if not (any(member.rank == "captain" or member.rank == "commander"
                for member in self.crew)):
            raise ValueError(
                'Mission must have at least one Commander or Captain'
                )
        experienced_members = sum(1 for member in self.crew
                                  if member.years_experience >= 5)
        if (self.duration_days > 365
                and experienced_members / len(self.crew) * 100 < 50):
            raise ValueError(
                'Long missions need 50% experienced crew'
                )
        if not (all(member.is_active for member in self.crew)):
            raise ValueError(
                'All crew members must be active'
                )
        return self


def print_mission(mission: SpaceMission) -> None:
    print(
        f"Mission: {mission.mission_name}\n"
        f"ID: {mission.mission_id}\n"
        f"Destination: {mission.destination}\n"
        f"Duration: {mission.duration_days} days\n"
        f"Budget: ${mission.budget_millions}M\n"
        f"Crew size: {len(mission.crew)}\n"
        "Crew members:"
    )
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
        )
    print()


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    valid_crew = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=45,
            specialization="Mission Command",
            years_experience=20,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=34,
            specialization="Navigation",
            years_experience=10,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=4,
        ),
    ]

    print("Valid mission created:")
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15, 9),
            duration_days=900,
            crew=valid_crew,
            budget_millions=2500.0,
        )
        print_mission(valid_mission)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].removeprefix("Value error, "))

    print("=========================================")

    print("Expected validation error:")
    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15, 9),
            duration_days=900,
            crew=valid_crew[1:],
            budget_millions=2500.0,
        )
        print_mission(invalid_mission)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
