import requests
import random

word_site = "https://raw.githubusercontent.com/RoxanaKovaci/Azure-pipelines/master/names.txt"

response = requests.get(word_site)
WORDS = response.content.splitlines()

print(random.choice(WORDS).decode("utf-8"))
