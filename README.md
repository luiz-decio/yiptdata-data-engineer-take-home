# SpendHound Data Integration Engineer Take-Home Exercise

## Overview

This project is designed to scrape data from an API containing information about Oscar-nominated movies from 1927 to 2014. The script extracts relevant details, including movie budgets, release dates, running times, and production companies, cleans the data, and exports it as a CSV file. The code is written in Python and utilizes the `requests` and `pandas` libraries for web scraping and data manipulation.

## Project Structure

- `etl.py`: The main script that runs the data extraction, cleaning, and export process.
- `requirements.txt`: Lists all Python dependencies required to run the script.
- `README.md`: This file contains an overview of the project and instructions for setting it up.
- `EXPLAIN.md`: A file explaining the approach and assumptions made during development.

## Features

1. **Data Scraping**: Fetches movie data from `http://oscars.yipitdata.com/` and detailed movie data from individual URLs.
2. **Data Cleaning**: Cleans the budget data, converts currencies to USD, and fills missing values.
3. **CSV Export**: Exports the cleaned data to a CSV file named `cleaned_oscar_movies.csv`.

## Requirements

- Python 3.6 or higher
- Internet connection to fetch data from the API

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/luiz-decio/yiptdata-data-engineer-take-home.git
   cd yiptdata-data-engineer-take-home

2. **Install the libraries and run the project**
   ```bash
   pip install requirements.txt
   python src/etl.py
   ```
3. **Check the final result in CSV generated in the [cleaned data folder](data/cleaned/)!**
4. **Feel free to play around with the [Analysis notebook](analysis/movie_data_exploration.ipynb)!**
