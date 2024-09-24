"""dummy test"""

from youth_map.state import State


def test_state() -> None:
    """Test state"""
    state = State()
    assert state.counter == 0
