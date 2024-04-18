import requests

api_key = "4bbb10d45f86466485e4eeb669ce2a0e"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-03-18&sortBy=publishedAt&apiKey="
       "4bbb10d45f86466485e4eeb669ce2a0e")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

