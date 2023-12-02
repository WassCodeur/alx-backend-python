import requests

try:
    res = requests.get("http://example.com")

    # Check if the request was successful (status code 200)
    res.raise_for_status()

    # Check if the content is not empty
    if res.text:
        # Try to parse the response content as JSON
        json_data = res.json()
        print(json_data)
    else:
        print("Response content is empty.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")

except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")

except requests.exceptions.JSONDecodeError as json_err:
    print(f"JSON decoding error occurred: {json_err}")
    # Handle the case where the response is not valid JSON

except Exception as e:
    print(f"An unexpected error occurred: {e}")

