"""React-leaflet component in Reflex

https://github.com/reflex-dev/reflex/issues/1291
"""

from typing import Any

import reflex as rx
from reflex.components.tags import Tag
from reflex.style import Style


class LeafletLib(rx.Component):
    """Leaflet component"""

    def _get_imports(self) -> dict:
        """Get imports"""
        return {}

    @classmethod
    def create(cls, *children, **props) -> rx.Component:  # noqa: ANN002, ANN003
        """Create the component"""
        custom_style = props.pop("style", {})

        # Transfer style props to the custom style prop.
        for key, value in props.items():
            if key not in cls.get_fields():
                custom_style[key] = value

        # Create the component.
        return super().create(
            *children,
            **props,
            custom_style=Style(custom_style),
        )

    def _render(self, props: dict[str, Any] | None = None) -> Tag:  # noqa: ARG002
        """Define how to render the component in React."""
        out = super()._render()
        return out.add_props(style=self.custom_style).remove_props("custom_style")


class MapContainer(LeafletLib):
    """Map container"""

    library = "react-leaflet"
    tag = "MapContainer"

    center: rx.Var[list[float]]
    zoom: rx.Var[int]
    scroll_wheel_zoom: rx.Var[bool]

    def _get_custom_code(self) -> str:
        return """import "leaflet/dist/leaflet.css";
import dynamic from 'next/dynamic'
const greenIcon =  import('leaflet').then(
(mod) =>
    L.icon({
        iconUrl: 'marker-nerd.png',
        shadowUrl: 'marker-shadow.png',
    })
)
const MapContainer = dynamic(() => import('react-leaflet').then(
    (mod) => mod.MapContainer), { ssr: false }
);
"""


class TileLayer(LeafletLib):
    """Tile Layer"""

    library = "react-leaflet"
    tag = "TileLayer"

    def _get_custom_code(self) -> str:
        return """const TileLayer = dynamic(() => import('react-leaflet').then(
    (mod) => mod.TileLayer), { ssr: false }
);"""

    attribution: rx.Var[str]
    url: rx.Var[str]


class UseMap(LeafletLib):
    """Use Map"""

    library = "react-leaflet"
    tag = "useMap"


class Marker(LeafletLib):
    """Marker"""

    library = "react-leaflet"
    tag = "Marker"

    def _get_custom_code(self) -> str:
        return """
const markerFuture = () => import('react-leaflet').then(
    (mod) => mod.Marker
)
const Marker = dynamic(markerFuture, { ssr: false });
"""

    position: rx.Var[list[float]]
    icon: rx.Var[dict]
    opacity: rx.Var[float] = 1.0


class Popup(LeafletLib):
    """Popup"""

    library = "react-leaflet"
    tag = "Popup"

    def _get_custom_code(self) -> str:
        return """const Popup = dynamic(() => import('react-leaflet').then(
    (mod) => mod.Popup), { ssr: false }
);"""


map_container = MapContainer.create
tile_layer = TileLayer.create
use_map = UseMap.create
marker = Marker.create
popup = Popup.create
