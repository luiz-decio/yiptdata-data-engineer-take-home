import pandas as pd
import requests
from tqdm import tqdm
from utils import process_budget, parse_running_time

def fetch_movie_data(url: str) -> dict:
    '''
    Get the movie data from the site
    '''

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {url}")
    
def extract_movie_details(movie_data):

    # Create an empty list to store movie details
    movies = []

    for year_entry in tqdm(movie_data["results"], desc="Processing years"):
        year = year_entry.get("year")

        try:
            for film in year_entry["films"]:
            
                film_name = film.get("Film")
                wikipedia_url = film.get("Wiki URL")
                oscar_winner = film.get("Winner")
                detail_url = film.get("Detail URL")

                # Fetch additional details from detail URL
                detail_data = fetch_movie_data(detail_url)
                original_budget, budget_converted_to_usd = process_budget(detail_data.get('Budget'))

                # Extract other details
                release_date = detail_data.get(' Release dates ')
                running_time = detail_data.get(' Running time ')
                production_company = detail_data.get(' Production company ')
                country = detail_data.get('Country')

                # Adds the data to the movies list
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

def main() -> None:
    url = "http://oscars.yipitdata.com/"
    movie_data = fetch_movie_data(url)
    movies = extract_movie_details(movie_data)

    # Save the data extracted

if __name__ == "__main__":
    main()