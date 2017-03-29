# Provides a word count of the filtered news to filtered-news-wc.txt
''' Common key words are:
RESULTS,708
POSITIVE,525
PRESENT,396
PRESENTS,312
INITIATES,297
ENROLLMENT,248
DESIGNATION,189
COMPLETES,120
PRESENTATIONS,117
GRANTED,100
INITIATION,93
EFFICACY,68
FAST,64
ACCEPTED,25
NEGATIVE,25
STRONG,24
CHECKPOINT,21
INITIATE,16
APPROVES,6'''

import re
from collections import Counter

text = ""
with open("filtered-news.txt") as f:
    text = f.read()

words = re.findall(r'\w+', text)
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)

with open("filtered-news-wc.txt", 'w') as f:
    for wcTuple in word_counts.most_common():
        word = wcTuple[0]
        count = wcTuple[1]
        f.write(word + "," + str(count) + "\n")


