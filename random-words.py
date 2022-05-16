import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

print(random.choice(WORDS).decode("utf-8"))
