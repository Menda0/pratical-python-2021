# https://api.spaceflightnewsapi.net/v3/articles

# 1. Use reuqest to get space news
# 2. Write all the news inside a csv file
# 3. id, title, imageUrl, summary, url

import csv
import requests

response = requests.get("https://api.spaceflightnewsapi.net/v3/articles")
articles = response.json()

print(articles)