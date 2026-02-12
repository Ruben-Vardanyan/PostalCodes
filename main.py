import requests

params = {
    "apikey": "....",
    "city": "Vagharshapat",
    "country": "AM"
}

response = requests.get('https://app.zipcodebase.com/api/v1/code/city', params=params)

print(response.text)
