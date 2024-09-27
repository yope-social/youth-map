"""locations"""

import json
from pathlib import Path

import reflex as rx
from loguru import logger
from pydantic.v1.error_wrappers import ValidationError


class Location(rx.Base):
    """The location class"""

    name: str
    lat: float
    long: float
    zone: int
    area: str
    description: str | None
    link: str | None


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
