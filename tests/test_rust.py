from ctypes import ArgumentError
import pytest
from rust_wrapper import add_rust

# all tests in this file can be called using the pytest.mark rust
# Useful for running only these tests after buidling the Rust code
pytestmark = pytest.mark.rust


def test_simple():
    val_1 = 23
    val_2 = 632
    result = add_rust(val_1, val_2)
    assert result == val_1 + val_2, f"Result was {result}"


def test_return_type():
    result = add_rust(1, 2)
    assert isinstance(result, int)


@pytest.mark.parametrize(
    "test_data",
    [
        ("string", "doesn't work"),
        ({"dict": True}, {"result": "it doesn't work"}),
        (0.2, 1.6),  # float
    ],
)
def test_error(test_data):
    """
    An ArgumentError is expected when non-int types are sent as arguments to the Rust function)
    if no ArgumentError is raised, the test will fail
    """
    with pytest.raises(ArgumentError):
        add_rust(test_data[0], test_data[1])
