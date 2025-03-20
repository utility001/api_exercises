import requests

def fetch_competitions(url):
    """Fetches competition data from the API URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"ERROR::: Unable to fetch data (Status Code::: {response.status_code})")
        return None

def extract_competition_names(data):
    """Gets the competition names out fo the api response"""
    competition_names = []

    # check that the "competitions" key is part of the response
    if "competitions" in data.keys():
        for competition in data["competitions"]:
            competition_names.append(competition["name"])
    return competition_names


def football_pipeline():
    """
    Fetch the data from "http://api.football-data.org/v4/competitions/" 
    and extract the competition name
    """
    URL = "http://api.football-data.org/v4/competitions/"
    output = fetch_competitions(URL)
    return extract_competition_names(output)


# u = football_pipeline()
# print(u)