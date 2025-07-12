import requests
# GET Request to Public API
response = requests.get("https://api.github.com/users/octocat")

print(response.status_code) # Check status
print(response.json()) # Convert to dict


# Handling Response
if response.status_code == 200:
    data = response.json()
    print("Username:", data['login'])
    print("Followers:", data['followers'])
else:
    print("Error:", response.status_code)