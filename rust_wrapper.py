from ctypes import cdll, c_int

# Load the Rust lib.
lib = cdll.LoadLibrary("./rust_library/target/release/librust_library.dylib")

# Configure function arguments
lib.add_numbers.argtypes = (c_int, c_int)
lib.add_numbers.restype = c_int


def add_rust(value_1: int, value_2: int) -> int:
    result = lib.add_numbers(value_1, value_2)
    return result
