import requests

joke_url = "https://api.jokes.one/jod"

def get_joke(url):
    """Defintion that sends a request to an API"""
    # use an api to get the data we need

    # joke_url = "https://dad-jokes.p.rapidapi.com/random/joke"
    r = requests.get(url)
    data = r.json() # to turn the request into a dictionary
    return data["contents"]["jokes"][0]["joke"]["text"]


joke = get_joke(url=joke_url)
print(joke)
