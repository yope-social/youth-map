"""Application State"""

import reflex as rx


class State(rx.State):
    """The app state."""

    counter: int = 0
