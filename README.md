# Exempelprojekt för att köra Rust ifrån Python 


## UV krävs
https://github.com/astral-sh/uv  
Installera Python 3.12 om du inte har det redan.


## Installation
Installera UV och Python 3.12 (om du inte har det)

## Installera Rust
https://www.rust-lang.org/tools/install



Har du inte `make`så installera det.

Viktigaste make-kommandot:
`make setup`
- skapar ett venv
- installerar Python-dependencies
- Konfigurerar pre-commit (tar lite längre tid första gången)
- formatterar, testar och bygger Rust-koden
- Kör alla Pytest-tester

Kolla i `Makefile`för övriga.



Exemplet är i stort sett härifrån: https://pythonislove.com/supercharge-your-python-apps-with-rust

##  PyO3
>"Rust bindings for Python, including tools for creating native Python extension modules. Running and interacting with Python code from a Rust binary is also supported."  

 https://pyo3.rs/v0.18.1/python_from_rust.html

På gott och ont flyttar det en del kod (såsom typ-definitioner) från Python- till Rust delen av projektet. Men deras enklaste exempel (som skapats av deras init) kompilerar inte. 

## Lär dig Rust
https://www.rust-lang.org/learn  
https://doc.rust-lang.org/rust-by-example/index.html

