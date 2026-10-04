#!/usr/bin/env python3

from pydantic import (BaseModel, Field, PastDatetime,
                      ValidationError, model_validator)
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: PastDatetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_rules(self) -> "AlienContact":
        if (self.contact_id[:2] != "AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError('Physical contact reports must be verified')
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                'Telepathic contact requires at least 3 witnesses'
                )
        if (self.signal_strength > 7
                and self.message_received is None):
            raise ValueError('Strong signals should include received messages')
        return self


def print_contact(contact: AlienContact) -> None:
    print(
        f"ID: {contact.contact_id}\n"
        f"Type: {contact.contact_type.value}\n"
        f"Location: {contact.location}\n"
        f"Signal: {contact.signal_strength}/10\n"
        f"Duration: {contact.duration_minutes} minutes\n"
        f"Witnesses: {contact.witness_count}\n"
        f"Message: '{contact.message_received}'\n"
    )


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    print("Valid contact report:")
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 7, 4, 22, 30),
            location="Area 52, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print_contact(valid_contact)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].removeprefix("Value error, "))

    print("======================================")

    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 7, 4, 22, 30),
            location="Area 52, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received=None,
        )
        print_contact(invalid_contact)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
