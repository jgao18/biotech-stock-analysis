import re
from collections import Counter

text = ""
with open("filtered-news.txt") as f:
    text = f.read()

words = re.findall(r'\w+', text)
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)
with open("test.txt", 'w') as t:
    t.write(str(word_counts))
