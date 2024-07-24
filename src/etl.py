import pandas as pd
import requests

def fetch_movie_data(url: str) -> dict:
    '''
    Get the movie data from the site
    '''

    response = requests.get(url)

    if response.status_code == 200:
        print("Data fetched successfully.")
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {url}")
    
def extract_movie_details(movie_data):

    # Create an empty list to store movie details
    movies = []

    for year_entry in movie_data["results"]:
        year = year_entry.get("year")

        for film in year_entry["films"]:
        
            film_name = film.get("Film")
            wikipedia_url = film.get("Wiki URL")
            oscar_winner = film.get("Winner")
            detail_url = film.get("Detail URL")

            #Fetch additional details from detail URL
            detail_data = fetch_movie_data(detail_data)
            original_budget, budget_converted_to_usd = process_budget(detail_data.get('Budget', ''))

if __name__ == "__main__":
    url = "http://oscars.yipitdata.com/"
    movie_data = fetch_movie_data(url)
