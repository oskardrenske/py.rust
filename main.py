from ctypes import cdll, c_int, ArgumentError
import pytest

# Load the Rust lib.
lib = cdll.LoadLibrary("./rust_library/target/release/librust_library.dylib")

# Configure function arguments
lib.add_numbers.argtypes = (c_int, c_int)
lib.add_numbers.restype = c_int


result = lib.add_numbers(35, 7)
print(f"the Answer to the Ultimate Question of Life, the Universe, and Everything is: {result}")


def main():
    assert lib.add_numbers(38, 4) == 42
    """
    The Rust function expects int,  
    an Argumenterror is expected when strings are sent as args
    """
    with pytest.raises(ArgumentError):
        lib.add_numbers("5", "7")


if __name__ == "__main__":
    main()
