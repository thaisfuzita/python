#!/usr/bin/env python3

from pydantic import BaseModel, Field, PastDatetime, ValidationError, model_validator
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

    @model_validator(mode="after")
    def check_rules(self) -> "AlienContact":
        if self.contact_id[:2] != "AC":
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError('Telepathic contact requires at least 3 witnesses')
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError('Strong signals should include received messages')
        return self


def main() -> None:
    # depois eu faço
    pass