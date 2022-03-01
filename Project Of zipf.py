# Import libraries
import requests

# Load The Webpage
requests = requests.get('https://en.wikipedia.org/wiki/Zipf%27s_law')

from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.content, 'html.parser')
wiki = " "
count = 0
while count < 32:
    wiki += soup.select('p')[count].text
    count += 1

for words in wiki:
    data = wiki.split(" ")

number = 0
dict_of_words = dict()
while number < len(data):
    word = data[number]
    dict_of_words[word] = data.count(word)
    number += 1

sorted_dict = dict(sorted(dict_of_words.items(), reverse=True, key=lambda x: x[1]))

top_20 = dict(list(sorted_dict.items())[:20])

zipf = list()
for wrd in range(1, 21):
    math = 105 * (1 / wrd)
    zipf.append(math)

import matplotlib.pyplot as plt

plt.plot(top_20.keys(), top_20.values(), '-*', color='black', label="Top 20 words")
plt.plot(top_20.keys(), zipf,  '-*', color='red', label='Zipf Line')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.legend()
plt.show()
