"""Test page."""

import reflex as rx
from loguru import logger

from youth_map.components.leaflet import map_container, tile_layer
from youth_map.components.marker import marker
from youth_map.data.locations import Location, locations


def get_marker(location: Location) -> rx.Component:
    """Get marker for a location"""
    data = location.dict()
    data["icon"] = location.get_icon()
    data["zone"] = location.get_zone()
    return marker(position=[location.lat, location.long], data=data)


def get_markers(area: str | None = None) -> list[rx.Component]:
    """Get the map marker"""
    markers = []
    if area is None:
        markers = [get_marker(location=_) for _ in locations]
    else:
        markers = [get_marker(location=_) for _ in locations if _.area == area]
    logger.info(f"Have {len(markers)} markers for area: {area}")
    return markers


def map_page(area: str | None = None) -> rx.Component:
    """Provide the data page"""
    center = [51.2727962, 12.8190212]
    zoom = 11
    if area == "colditz":
        zoom = 13
        center = [51.13302, 12.8071]
    if area == "lossatal":
        zoom = 11
        center = [51.3957047, 12.8310184]

    return map_container(
        tile_layer(
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        ),
        *get_markers(area=area),
        center=center,
        zoom=zoom,
        scroll_wheel_zoom=True,
        height="100vh",
        width="100%",
    )
