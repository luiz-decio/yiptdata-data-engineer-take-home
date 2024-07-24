import pandas as pd
import requests
import json
import os
import datetime
from tqdm import tqdm
from utils import process_budget, parse_running_time





import re
# Function to convert the movies budgets to USD
def process_budget(budget):
    
    # Clean up budget data
    if pd.isna(budget):
        return 0, 0
    
    # Extract budget value and convert to integer
    budget_value = re.search(r'(\d+(?:\.\d+)?)', budget.replace(',', ''))
    if budget_value:
        budget_value = float(budget_value.group(0)) * (1e6 if 'million' in budget else 1)
        if 'US$' in budget or 'USD' in budget:
            return budget_value, budget_value
        else:
            # Convert to USD using an assumed conversion rate
            conversion_rate = 1.1  # Hypothetical conversion rate; adjust as needed
            return budget_value, budget_value * conversion_rate
    return 0, 0

# Function to transform the tim
def parse_running_time(running_time):
    if not running_time:
        return None
    # Extract the running time in minutes
    match = re.search(r'(\d+) minutes', running_time)
    return int(match.group(1)) if match else None




# Define the date to save the files
date_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def fetch_movie_data(url: str) -> dict:

    response = requests.get(url)

    if response.status_code == 200:
        movie_data =  response.json()
        return movie_data

    else:
        raise Exception(f"Failed to fetch data from {url}")
    
def save_raw_file(raw_data: dict, save_path = 'data/raw', date_stamp = date_stamp):

        # Define the file path for saving the JSON data
        file_path = os.path.join(save_path, f'{date_stamp}_raw_movies_data.json')

        # Save the movie data to a JSON file
        with open(file_path, 'w') as json_file:
            json.dump(raw_data, json_file, indent= 4)

def extract_movie_details(movie_data):

    # Create an empty list to store movie details
    movies = []

    for year_entry in tqdm(movie_data["results"], desc="Processing years"):
        year = year_entry.get('year')

        try:
            
            for film in year_entry['films']:
                film_name = film.get('Film')
                wikipedia_url = film.get('Wiki URL')
                oscar_winner = film.get('Winner')
                detail_url = film.get('Detail URL')
                
                # Fetch additional details from detail URL
                detail_data = fetch_movie_data(detail_url)
                original_budget, budget_converted_to_usd = process_budget(detail_data.get('Budget'))

                # Extract other details
                release_date = detail_data.get(' Release dates ')
                running_time = detail_data.get(' Running time ')
                production_company = detail_data.get(' Production company ')
                country = detail_data.get('Country')

                movies.append({
                    'film': film_name,
                    'year': year,
                    'wikipedia_url': wikipedia_url,
                    'oscar_winner': oscar_winner,
                    'original_budget': original_budget,
                    'budget_converted_to_usd': budget_converted_to_usd,
                    'release_date': release_date.strip() if release_date else None,
                    'running_time': parse_running_time(running_time),
                    'production_company': production_company.strip() if production_company else None,
                    'country': country
                })

        except Exception as e:
            print(f'The movie {film_name} could not be extracted.')
            print(f'Error: {e}')
            continue
    
    return movies

def clean_data(movies: list) -> pd.DataFrame:

    # Convert the data to Dataframe
    df = pd.DataFrame(movies)

    # Transofrms year and budget columns
    df['year'] = df['year'].apply(lambda x: int(x.split('/')[0]) if x.split('/')[0].isnumeric() else None)
    df.fillna({'original_budget': 0, 'budget_converted_to_usd': 0}, inplace=True)
    
    return df

def export_to_csv(df, date_stamp = date_stamp):
    file_name = f'data/cleaned/{date_stamp}_cleaned_movie_data.csv'
    print(file_name)
    df.to_csv(file_name, index=False)


url = "http://oscars.yipitdata.com/"
raw_movie_data = fetch_movie_data(url)
save_raw_file(raw_movie_data)
movies = extract_movie_details(raw_movie_data)
print(movies)
cleaned_data = clean_data(movies)
export_to_csv(cleaned_data)

def main() -> None:
    url = "http://oscars.yipitdata.com/"
    raw_movie_data = fetch_movie_data(url)
    save_raw_file(raw_movie_data)
    movies = extract_movie_details(raw_movie_data)
    cleaned_data = clean_data(movies)
    export_to_csv(cleaned_data, f'trusted/{date_stamp}_cleaned_movie_data.csv')


if __name__ == "__main__":
    main()