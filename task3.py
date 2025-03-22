import requests

def fetch_random_users(result_count: int = 500):
    """
    Gets random user data from the randomuser.me API

    Args:
        result_count (int): The number of user profiles to fetch 
        Default is 500
    Returns:
        dict: The JSON response returned by the API
    Raises:
        Exception If the request fails
    """
    url = "https://randomuser.me/api/"
    params = {"results": result_count}

    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request to {response.request.url} request failed")


def extract_user_profiles(api_response: dict) -> list:
    """
    Extracts the list of user profiles returned from the API call

    Args:
        api_response (dict): The raw json response from the API
    Returns:
        list: A list of user profiles
    """
    return api_response["results"]


def filter_profiles_by_gender(user_profiles: list, gender: str) -> list:
    """
    Filters user profiles based on gender

    Args:
        user_profiles (list): List of user profiles
        gender (str): The gender to filter by. Accepted values::: "male" or "female"
    Returns:
        list: A list of profiles matching the specified gender
    Raises:
        ValueError: If an invalid gender is provided
    """
    # First check that the user has inputed the correct gender
    if gender not in ["male", "female"]:
        raise ValueError("Gender must be either 'male' or 'female'.")

    # Initialize a list to store the filtered user profiles
    output = []

    for profile in user_profiles:
        if profile["gender"] == gender:
            output.append(profile)

    return output


def extract_dates_of_birth(user_profiles: list) -> list:
    """
    Extracts the date of birth from user profiles

    Args:
        user_profiles (list): List of user profiles
    Returns:
        list: A list containing the date of birth of all profiles
    """
    output = []

    for profile in user_profiles:
        date_of_birth = profile["dob"]["date"]
        output.append(date_of_birth)

    return output

    

def extract_full_names(user_profiles: list) -> list:
    """
    Extracts full names from user profiles

    Args:
        user_profiles (list): List of user profiles
    Returns:
        list: A list of full names
    """
    output = []

    for profile in user_profiles:
        first_name = profile["name"]["first"]
        last_name = profile["name"]["last"]
        full_name = first_name + " " + last_name
        output.append(full_name)
    return output



## USAGE
api_response = fetch_random_users()
user_profiles = extract_user_profiles(api_response)

male_profiles = filter_profiles_by_gender(user_profiles, "male")
female_profiles = filter_profiles_by_gender(user_profiles, "female")
birth_dates = extract_dates_of_birth(user_profiles)
full_names = extract_full_names(user_profiles)

print(male_profiles)
print(female_profiles)
print(birth_dates)
print(full_names)