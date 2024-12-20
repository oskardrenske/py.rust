# Exempelprojekt för att köra Rust ifrån Python 


## UV krävs
https://github.com/astral-sh/uv  
Installera Python 3.12 om du inte har det redan.


## Installation
Installera UV.

Kör sedan dessa kommandon i repo-rooten (på Windows aktiveras venv på annat sätt)

```
uv venv
source .venv/bin/activate
uv sync
pre-commit install
```


## Installera Rust
https://www.rust-lang.org/tools/install

i rust_library-katalogen:
- test: `cargo test`
- build: `cargo build --release`


Exemplet är i stort sett härifrån: https://pythonislove.com/supercharge-your-python-apps-with-rust

##  PyO3
>"Rust bindings for Python, including tools for creating native Python extension modules. Running and interacting with Python code from a Rust binary is also supported."  

 https://pyo3.rs/v0.18.1/python_from_rust.html

Det kanske underlättar för mer avancerade program

## Lär dig Rust
https://www.rust-lang.org/learn  
https://doc.rust-lang.org/rust-by-example/index.html

