import requests

# API_KEY="141710af2113bab9f55ef73e1bcd33d5" Ardit Instructor

API_KEY = "ce8207f61f82de03b1c890ee0a91d4ad"


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo", 3))
