# EXPLAIN.md

## Overview

This script performs an ETL (Extract, Transform, Load) process to fetch, process, clean, and save movie data from a specified URL. The code is structured to fetch movie data, save the raw data, extract relevant details, clean the data, and export the cleaned data to a CSV file. Logging is used throughout the script to track the progress and catch any errors.

## Components

### Imports

- **Standard Library Imports**:
  - `datetime`: For handling date and time-related operations.
  - `json`: For parsing and saving JSON data.
  - `logging`: For logging informational and error messages.
  - `os`: For file and directory operations.
  - `requests`: For making HTTP requests to fetch data.
  - `pandas`: For data manipulation and analysis.
  
- **Third-Party Imports**:
  - `tqdm`: For displaying progress bars in loops.

- **Custom Imports**:
  - `process_budget`, `parse_running_time`: Custom utility functions from the `utils` module.

### Logging Configuration

- **Logging Setup**:
  - Logs are saved to a file in a "logs" directory.
  - The log file name includes a timestamp to ensure uniqueness.
  - Logging level is set to `INFO` to capture informational messages and errors.

### Functions

1. **`fetch_movie_data(url: str) -> dict`**:
   - **Purpose**: Fetch movie data from the provided URL.
   - **Rationale**: Uses the `requests` library to perform a GET request. Logs success or failure based on the HTTP response status code.
   - **Error Handling**: Raises an HTTP error if the request fails.

2. **`save_raw_file(raw_data: dict, save_path: str = "data/raw", date_stamp: str = date_stamp) -> None`**:
   - **Purpose**: Save the raw movie data to a JSON file.
   - **Rationale**: Defines a file path using the current timestamp to avoid filename conflicts. Uses `json.dump` to write data to a file with indentation for readability.
   - **Error Handling**: Catches exceptions and logs errors if the file operation fails.

3. **`extract_movie_details(movie_data: dict) -> list`**:
   - **Purpose**: Extract relevant movie details from the fetched data.
   - **Rationale**: Iterates over the data, processes each entry, and fetches additional details using URLs. Utilizes helper functions to process budgets and parse running times.
   - **Error Handling**: Logs warnings and prints error messages if details for a movie cannot be extracted.

4. **`clean_data(movies: list) -> pd.DataFrame`**:
   - **Purpose**: Clean and prepare the movie data for export.
   - **Rationale**: Converts the list of movie dictionaries to a Pandas DataFrame. Transforms columns as needed and fills missing values.
   - **Error Handling**: Assumes no specific errors but logs completion of the cleaning process.

5. **`export_to_csv(df: pd.DataFrame, date_stamp: str = date_stamp) -> None`**:
   - **Purpose**: Export the cleaned data to a CSV file.
   - **Rationale**: Saves the DataFrame as a CSV file in a "cleaned" directory with a timestamped filename to prevent overwriting previous files.
   - **Error Handling**: Catches exceptions and logs errors if the file export fails.

### ETL Function

- **Purpose**: Orchestrates the ETL process.
- **Rationale**:
  - Calls each function in sequence: fetches data, saves raw data, extracts details, cleans data, and exports to CSV.
  - Provides feedback to the user via print statements.
  - Catches and logs any exceptions that occur during the process.

## File Structure

- **Data Directories**:
  - `data/raw/`: Stores raw JSON files of movie data.
  - `data/cleaned/`: Stores cleaned CSV files of movie data.
  - `logs/`: Stores log files for tracking the ETL process.

- **Log Files**:
  - Each log file is timestamped to uniquely identify logs for different runs of the script.

## Conclusion

This script demonstrates a straightforward approach to processing movie data with robust error handling and clear logging. The ETL process is modular, making it easy to extend or modify individual components as needed. The use of logging and structured error handling ensures that issues can be diagnosed and addressed effectively.