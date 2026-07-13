# bzan545-python-first-scripts

Small follow-along repo for the first Python scripts + Positron tour.

## Setup

```bash
uv sync
uv run python orders_plot.py
```

## Positron tour

- Open this folder in Positron.
- Find the file browser, editor, terminal, console, and plots/output area.
- Check that Positron is using the project `.venv`.
- Run `orders_plot.py` from the terminal with `uv run python orders_plot.py`.
- Run `orders_plot.py` with the editor play/run button.
- Run a few Python lines one at a time with Cmd/Ctrl+Enter.
- Open `orders_plot.R` and notice the same idea in R.
- Open `orders_plot.ipynb` and notice the same idea in notebook form.
- Create a new `.py` file in Positron and run something tiny.

## Python basics path

Day 06 starts here:

- `python_basics/01_variables_math_types.py`
- `python_basics/02_strings_lists_dicts.py`

Day 07 likely continues here:

- `python_basics/03_conditionals.py`
- `python_basics/04_iteration.py`
- `python_basics/05_functions.py`
- `python_basics/06_csv_pipeline_start.py`

## Optional data generation

`data/orders.csv` is already created for you.

If you want to see how it was created:

```bash
uv run python data/create_orders_csv.py
```
