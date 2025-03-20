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
    base_url = "https://jobicy.com/api/v2"
    endpoint = "/remote-jobs"
    params = {
        "count": count,
        "geo": "usa",
        "industry": "marketing",
        "tag": "seo"
    }

    response = requests.get(url=base_url+endpoint, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request to {response.request.url} failed")


def filter_jobs_by_keyword(api_response, keyword):
    """
    Filters jobs listings based on a given keyword.

    Args:
        api_response (dict): The response data containing job listings.
        keyword (str): The keyword to filter job titles.

    Returns:
        list: A list of job titles that contain the keyword.
    """
    filtered_jobs = []
    
    
    for job in api_response["jobs"]:
        if keyword.lower() in job["jobTitle"].lower():
            filtered_jobs.append(job["jobTitle"])
    
    return filtered_jobs
    

# Example
u = fetch_remote_marketing_jobs()
v = filter_jobs_by_keyword(u, "senior")
w = filter_jobs_by_keyword(u, "manager")

print(v)
print("**********")
print(w)