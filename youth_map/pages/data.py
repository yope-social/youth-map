"""Index page."""

import reflex as rx

from youth_map.data.locations import parsed_json

table = rx.data_table(
    data=parsed_json,
    columns=["name", "lat", "long", "zone"],
    pagination=True,
    search=True,
    sort=True,
)


def data_page() -> rx.Component:
    """Provide the data page"""
    return table
