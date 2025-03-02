"""Hello Component

as described in https://reflex.dev/docs/wrapping-react/guide/
"""

import reflex as rx


class Marker(rx.NoSSRComponent):
    """Leaflet Marker with custom icons"""

    # Use an absolute path starting with /public
    library = "/public/marker"

    # Define everything else as normal.
    tag = "Marker"

    position: rx.Var[list[float]]
    data: rx.Var[dict[str, str | float | None]]


marker = Marker.create
