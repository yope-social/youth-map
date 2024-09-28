"""locations"""

import json
from pathlib import Path

import reflex as rx
from loguru import logger
from pydantic.v1.error_wrappers import ValidationError

BOOMER_ZONE = 1
SUPPORT_ZONE = 2
NERD_ZONE = 3
KOMPROMISS_ZONE = 4
FREIRAUM_ZONE = 5


class Location(rx.Base):
    """The location class"""

    name: str
    lat: float
    long: float
    zone: int
    area: str
    description: str | None
    accessibility: str | None
    risk: str | None
    link: str | None

    def get_icon(self) -> str:
        """Get the icon for the location (based on the zone ID)."""
        if self.zone == BOOMER_ZONE:
            return "/marker-boomer.png"
        if self.zone == SUPPORT_ZONE:
            return "/marker-support.png"
        if self.zone == NERD_ZONE:
            return "/marker-nerd.png"
        if self.zone == KOMPROMISS_ZONE:
            return "/marker-kompromiss.png"
        if self.zone == FREIRAUM_ZONE:
            return "/marker-freiraum.png"
        return "/marker-unknown.png"

    def get_zone(self) -> str:
        """Get the zone for the location (based on the zone ID)."""
        if self.zone == BOOMER_ZONE:
            return "boomer"
        if self.zone == SUPPORT_ZONE:
            return "support"
        if self.zone == NERD_ZONE:
            return "nerd"
        if self.zone == KOMPROMISS_ZONE:
            return "kompromiss"
        if self.zone == FREIRAUM_ZONE:
            return "freiraum"
        return "unknown"


file_path = Path(__file__).parent / "locations.json"
with file_path.open("r") as file:
    parsed_json = json.load(file)

locations = []
for location in parsed_json:
    try:
        locations.append(Location(**location))
    except ValidationError as error:
        all_errors = error.errors()
        other_errors = []
        missing_fields: list[str] = []
        for _ in error.errors():
            if _["msg"] == "field required":
                missing_fields.extend([str(field) for field in _["loc"]])
            else:
                other_errors.append(_)
        logger.warning(
            f"Could not parse location: {location}. "
            f"Missing Fields: {', '.join(missing_fields)}; "
            f"Other Errors: {other_errors}"
        )
