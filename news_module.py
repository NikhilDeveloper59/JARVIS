import requests
from config import NEWS_API_KEY

''' NEWS_API responsed with josn formate data like this

{"status": "ok","totalResults": 34,"articles": [{"title": "Some breaking news...","description": "...","url": "https://...",  ...}]}

'''

# request → JSON → status check → limit articles → titles extract → return

def get_top_headlines(country="in", limit=5): # limit set only 5 headlines 
    try:

        # This is NewsAPI endpoint. '/v2/top-headlines'
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)  # sends request to browser and wants for the data
        data = response.json()        # NewsAPI response with the JSON format

        if data["status"] != "ok":
            return ["Sorry, unable to fetch news right now."]

        articles = data["articles"][0:limit] # slice function used to slice only limited headlines extract
        headlines = [f"{i+1}. {a['title']}" for i, a in enumerate(articles)] # enumerate function used for data and its correct index 

        return headlines

    except:
        return ["Sorry, news service is not responding."]

def search_news(query, limit=5):
    try:
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}&language=en"
        response = requests.get(url)
        data = response.json()

        if data["status"] != "ok":
            return ["Sorry, unable to fetch news about that."]

        articles = data["articles"][0:limit]
        headlines = [f"{i+1}. {a['title']}" for i, a in enumerate(articles)]  # Extract only Titles (a['title']--> titlr of each article)
        return headlines
    except:
        return ["Sorry, news service is not responding."]
