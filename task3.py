import requests

def make_request_randomuserme(results=500):
    """
    This function makes request to the randomuser.meapi
    """
    URL = "https://randomuser.me/api/"
    PARAMS = {"results" : results}

    response = requests.get(url=URL, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"ERROR::: Unable to fetch data (Status Code::: {response.status_code})")
        raise

def get_profile(api_resp, gender: str):
    """
    Extracts profile based on gender

    api_resp
    gender: str
        The gender you want
        We only accept "male" or "female"
    """
    if gender not in ["male", "female"]:
        raise ValueError("We only accept 'male' or 'female' keyword as gender. Please check it")
    
    output = []

    all_profiles = api_resp["results"]
    for profile in all_profiles:
        if profile["gender"] == gender:
            output.append(profile)

    return output

def get_dob(api_resp):
    """
    Gets Date of births from the API
    """
    output = []

    all_profiles = api_resp["results"]
    for profile in all_profiles:
        date_of_birth = profile["dob"]["date"]
        output.append(date_of_birth)
    return output

def get_name(api_resp):
    """
    Gets names from the API
    """
    output = []

    all_profiles = api_resp["results"]
    for profile in all_profiles:
        first_name = profile["name"]["first"]
        last_name = profile["name"]["last"]
        full_name = first_name + " " + last_name
        output.append(full_name)
    return output