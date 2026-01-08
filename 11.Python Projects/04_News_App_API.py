import requests
query = input("What type of news are you interested in today?")
api = "bce46097182f4af5a6be8b60725fd7bf"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-09-04&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
