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
        print(f"ERROR: Unable to fetch data (Status Code: {response.status_code})")
        raise Exception(f"API to {response.request.url} request failed")


def extract_user_profiles(api_response: dict) -> list:
    """
    Extracts the list of user profiles from the API response

    Args:
        api_response (dict): The raw API response from the api

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
    Extracts the date of birth from user profiles.

    Args:
        user_profiles (list): List of user profiles.

    Returns:
        list: A list containing the date of birth of all profiles.
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
        user_profiles (list): List of user profiles.

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


def run_pipeline():
    """
    Fetches user data and extracts relevant details

    Returns:
        tuple: This tuple contains
            - List of male profiles
            - List of female profiles
            - List of dates of birth
            - List of full names
    """
    api_response = fetch_random_users()
    user_profiles = extract_user_profiles(api_response)

    male_profiles = filter_profiles_by_gender(user_profiles, "male")
    female_profiles = filter_profiles_by_gender(user_profiles, "female")
    dates_of_birth = extract_dates_of_birth(user_profiles)
    full_names = extract_full_names(user_profiles)

    return male_profiles, female_profiles, dates_of_birth, full_names

# Example
male_users, female_users, birth_dates, full_names = run_pipeline()
# print(male_users)
# print(female_users)
print(birth_dates)
print(full_names)
