# 04_cinema_tickets

Unit tests for the Cinema Ticket System (C339 Software Testing and Analytics, CA1).

## Project structure

- `src/` – the code being tested (`cinema_price.py` and `cinema_entry.py`)
- `tests/` – the pytest unit tests
- `.github/workflows/run-pytest.yml` – the GitHub Actions workflow that runs the tests

## How to run the tests

Install pytest:

    pip install pytest

Run the tests from this folder:

    python -m pytest -v

## GitHub Actions

The workflow runs pytest automatically when code in `src/`, `tests/` or the workflow file is pushed.
Changes to other files, such as this README, do not start a test run.