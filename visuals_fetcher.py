import requests

PEXELS_API_KEY = "ENTER_YOUR_SECRET_KEY"

def fetch_images(topic, count=5):
    url = f"https://api.pexels.com/v1/search?query={topic}&per_page={count}"
    headers = {"Authorization": PEXELS_API_KEY}
    response = requests.get(url, headers=headers).json()

    image_urls = [photo["src"]["large"] for photo in response["photos"]]
    return image_urls

