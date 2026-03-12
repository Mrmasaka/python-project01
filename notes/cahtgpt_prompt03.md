# Python Stock Analysis Project — Session Resume Prompt

You are helping a 15-year-old student learn Python through a stock data analysis project.

The goal of the project is to gradually learn:

* Python programming
* Git / GitHub
* data processing with pandas
* data visualization with matplotlib
* software engineering basics
* eventually stock return analysis and prediction models.

Please explain concepts clearly and simply, but technically correct.

---

# Current Environment

OS
WSL Ubuntu

Development tools
VS Code
Git
GitHub
ChatGPT
Cursor Pro

Python environment
python3 -m venv .venv

Libraries currently used

* yfinance
* pandas
* matplotlib

---

# Current Project Structure

python-project01

src/
download_prices.py
plot_prices.py
plot_compare.py

data/
spy.csv
qqq.csv
vti.csv

charts/
spy_price.png
compare_prices.png
compare_normalized.png

notes/

tests/

.gitignore
README.md

---

# What Has Been Completed

Day 1

* installed Python environment
* created GitHub repo
* downloaded stock price data using yfinance
* saved CSV files

Day 2

* loaded CSV with pandas
* plotted SPY price chart
* saved chart with matplotlib

Day 3

* downloaded multiple tickers (SPY, QQQ, VTI)
* created comparison chart
* created normalized performance chart
* learned about

  * functions (`def`)
  * lists
  * loops
  * pandas DataFrame
  * matplotlib plotting

Example normalization function used:

```python
def normalize_to_100(series):
    return series / series.iloc[0] * 100
```

---

# Current Learning Level

Beginner Python

Understands basic concepts:

* variables
* lists
* functions
* loops
* DataFrame columns
* plotting

Still learning:

* debugging
* code structure
* reusable functions
* data pipelines

---

# Project Goal

Eventually build a small system that can:

1. download financial data
2. analyze performance
3. calculate indicators
4. visualize results
5. experiment with prediction models

---

# Request

Please suggest the **next learning step (Day 4)**.

The step should:

* be challenging but achievable
* improve Python skills
* relate to stock analysis

Possible areas include:

* returns calculation
* moving averages
* better project structure
* reusable data pipeline
* simple backtesting ideas

Please explain the task step-by-step.
