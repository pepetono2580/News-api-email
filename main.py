import requests
from send_email import send_email

api_key = "4bbb10d45f86466485e4eeb669ce2a0e"
url = ("https://newsapi.org/v2/everything?q=apple&from=2024-04-18&to=2024-04-18&sortBy=popularity&apiKey=4bbb10d45f86466485e4eeb669ce2a0e")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message = ""
# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        message = message + article["title"] + "\n" + article["description"] + 2*"\n"
        # print("Title: ", article["title"])
        # print("Description: ", article["description"])

message = message.encode("UTF-8")
send_email(message)

