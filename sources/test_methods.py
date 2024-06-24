import requests
#------------------------method to get a query from an endpoint---------------------------------------------------------------

def get_query(base_url, endpoint, *elements):
    url = base_url + endpoint
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Request to {url} failed with status code {response.status_code}")
        return None
    json_response = response.json()
    if isinstance(json_response, list):
        return [[item[element] for element in elements] for item in json_response]
    else:
        return [json_response[element] for element in elements]

#------------------------method to get a query from an endpoint---------------------------------------------------------------

def get_query_negative(base_url, endpoint, *elements):
    url = base_url + endpoint
    response = requests.get(url)
    return response

#------------------------method to post a query to an endpoint---------------------------------------------------------------


def post_query(base_url, endpoint, data):
    url = base_url + endpoint
    response = requests.post(url, json=data)
    if response.status_code != 500:
        print(f"POST request to {url} finished with status code. {response.status_code}")
        return response.json()
    else:
        return response

#------------------------method to delete a query to an endpoint---------------------------------------------------------------

def delete_query(base_url, endpoint):
    url = base_url + endpoint
    response = requests.delete(url)
    if response.status_code != 200:
        print(f"DELETE request to {url} failed with status code {response.status_code}")
        return response
    return response
#------------------------method to update a query to an endpoint---------------------------------------------------------------
def update_query(base_url, endpoint, data):
    url = base_url + endpoint
    response = requests.put(url, data)
    if response.status_code != 200:
        print(f"PUT request to {url} failed with status code {response.status_code}")
        return response.status_code
    return response