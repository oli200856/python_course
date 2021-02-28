# import requests

# url = "https://www.icanhazdadjoke.com"
# response = requests.get(url, headers={"Accept": "application/json"})

# data = response.json()

# print(data["joke"])

import requests

url = "https://www.icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat"}
    )

data = response.json()

print(data["results"])