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

The workflow (`.github/workflows/run-pytest.yml`) runs pytest on GitHub:

- on pull requests into `main`, once they are ready for review (draft pull requests are skipped)
- on pushes to `main`
- manually, using the **Run workflow** button in the Actions tab

It only runs when files in `src/`, `tests/` or the workflow file change.
If a newer run starts on the same branch, the older run is cancelled.