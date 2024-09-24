"""Index page."""

import reflex as rx

from youth_map.components.leaflet import map_container, marker, popup, tile_layer
from youth_map.data.locations import Location, locations


def get_popup(location: Location) -> rx.Component:
    """Get popup for a location"""
    description = rx.text(location.description) if location.description else rx.text("")
    link = (
        rx.link(rx.badge("Link", variant="solid"), href=location.link, target="new")
        if location.link
        else rx.text("")
    )
    return popup(
        rx.vstack(
            rx.box(
                rx.heading(location.name),
                rx.container(description),
                rx.container(link),
            )
        )
    )


def get_marker(location: Location) -> rx.Component:
    """Get marker for a location"""
    return marker(
        get_popup(location),
        position=[location.lat, location.long]
    )


def get_markers(area: str | None = None) -> list[rx.Component]:
    """Get the map marker"""
    if area is None:
        return [
            get_marker(location=_)
            for _ in locations
        ]
    return [
        get_marker(location=_)
        for _ in locations
        if _.area == area
    ]


def get_map(area: str | None = None) -> rx.Component:
    """Get the map container"""
    attribution = (
        "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors"
    )

    center = [51.2727962, 12.8190212]
    zoom = 11
    if area == "colditz":
        zoom = 13
        center = [51.13302, 12.8071]
    if area == "lossatal":
        zoom = 11
        center = [51.3957047, 12.8310184]

    return rx.center(
        map_container(
            tile_layer(
                attribution=attribution,
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            ),
            *get_markers(area=area),
            center=center,
            zoom=zoom,
            scroll_wheel_zoom=True,
            height="100vh",
            width="100%",
        ),
    )


def map_page(area: str | None = None) -> rx.Component:
    """Provide the index page"""
    return get_map(area=area)
