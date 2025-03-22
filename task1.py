import requests

def fetch_remote_marketing_jobs(count: int = 20):
    """
    Fetches remote marketing job listings in the USA from the Jobicy API

    Args:
        count (int): The number of jobs to retrieve from the API
        Note that the API may return less jobs if there aren't enough listings available.
    Returns:
        dict: A dictionary containing job listings.
    Raises:
        Exception: If the request to the API fails.
    """
    endpoint = "https://jobicy.com/api/v2/remote-jobs"
    params = {
        "count": count,
        "geo": "usa",
        "industry": "marketing",
        "tag": "seo"
    }

    response = requests.get(url=endpoint, params=params)
    print(f"Sending request to::: {response.request.url}")

    if response.status_code == 200:
        print("Request Sucessful")
        return response.json()
    else:
        raise Exception(f"API request to {response.request.url} failed")


def filter_jobs_by_keyword(api_response, keyword):
    """
    Filters jobs listings based on a given keyword

    Args:
        api_response (dict): The api response data containing job listings
        keyword (str): The keyword to filter job titles
    Returns:
        list: A list of job titles that contain the input keyword
    """
    filtered_jobs = []
    
    for job in api_response["jobs"]:
        if keyword.lower() in job["jobTitle"].lower():
            filtered_jobs.append(job["jobTitle"])
    
    return filtered_jobs
    

# Fetch Seinor and Manager roles from the API
resp = fetch_remote_marketing_jobs()
senior_roles = filter_jobs_by_keyword(resp, "senior")
manager_roles = filter_jobs_by_keyword(resp, "manager")

print(senior_roles)
print("**********")
print(manager_roles)