.ONESHELL:  # Everything in one shell to make it easier to use venv 
.DEFAULT_GOAL := help  # Om du bara skriver make
PYTEST := pytest -s -v
# kör även om det inte finns en fil med samma namn som kommandot
.PHONY: all

# Indentering görs med tab i makefile, inte spaces
# topp-nivån är make-kommandon
# indenterad kod körs i ett shell



# Create new venv and install dependencies
# Run tests so you know that they pass before you start working

install: setup_venv pre-commit install rust pytest
	@echo "** Installation complete **"

install-clean: clean rust-clean install


activate_venv:
	. .venv/bin/activate  # dot instead of source is make-specific

pre-commit-install: activate_venv
	pre-commit install # konfigurera git hooks och installera 

setup_venv:
	uv venv  # skapa venv
	. .venv/bin/activate # aktivera venv
	uv sync  # Installera dependencies från uv.lock
	

clean: rust-clean
	rm -rf .venv/
	rm -rf __pycache__/
	rm -rf .pytest_cache
	

# Kör Python-tester med coverage (cov-report i terminalen)
pytest:  activate_venv
	${PYTEST} --cov . tests

test: pytest rust-test


# kör ruff check
lint: activate_venv
	ruff check

# Formattera koden (Python & Rust)
format: activate_venv rust-fmt
	ruff format
	

# Allt du vill göra innan en commit
commit: activate_venv lint format rust test
	

help:
	@echo "Kolla i Makefile vilka kommandon som finns"



# Rust things
RUST_PATH := --manifest-path ./rust_library/Cargo.toml

rust: build pytest-rust
	@echo "Rust section complete"

rust-test:
	cargo test ${RUST_PATH}
	pytest -s -v 

rust-fmt:
	cargo fmt ${RUST_PATH}

build: rust-fmt rust-test	
	cargo build --release ${RUST_PATH}

pytest-rust: activate_venv
	pytest -v -s -m rust tests
	
rust-clean:
	cargo clean ${RUST_PATH}

