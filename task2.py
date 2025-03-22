import requests

def fetch_competitions():
    """
    Fetches competition data from Football Data API.

    Returns:
        dict: The JSON response returned by the API.
    
    Raises:
        Exception If the request fails
    """
    url = "http://api.football-data.org/v4/competitions/"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Request to {response.request.url} request failed")
    

def extract_competition_names(api_response: dict) -> list[str]:
    """
    Extracts competition names out fo the api response

    Args:
        api_resp (dict): The response data containing the competitions
    Returns:
        A list containing all competition names
    """
    competition_names = []

    for competition in api_response["competitions"]:
        competition_names.append(competition["name"])

    return competition_names


# Get all competitions
resp = fetch_competitions()
comp_names = extract_competition_names(resp)

print(len(comp_names))
print(comp_names)