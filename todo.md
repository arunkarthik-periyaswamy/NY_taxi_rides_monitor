# Steps to Reproduce

## Setup

**Purpose**: Setup an isolated Python environment for working on this project.

- [ ] Install Python via Anaconda Python or Microsoft App Store
- [ ] Install Poetry
- [ ] Start a new project
- [ ] Activate the poetry-managed environment
- [ ] Install `notebook` package using Poetry
- [ ] Create directories in the project folder based on the suggested directory structure.

## 01 Fetch Data

**Purpose**: Write a Python function in Jupyter Notebook to fetch Taxi demand data.

- [ ] Install the `requests` package using Poetry
- [ ] Create a new notebook called `01_fetch_data.ipynb`
- [ ] Write a function that takes year and month and fetches a parquet file and stores it in `data/raw`
- [ ] Run the function and verify that you can download different years and months

## 02 Validate and Save Data

- [ ] Create a new notebook called `02_validate_and_save.ipynb`
- [ ] Install packages
- [ ] Remove outliers in total amount
- [ ] Remove outliers in duration.
- [ ] Remove dates out of range.
- [ ] Remove pickup locations outside of NYC.
- [ ] Save the data in `data/processed`.

## 03
