# Combines all news headlines into one file for viewing

import os

filenames = os.listdir('../news/')
with open('../news/ALLNEWS.txt', 'w') as outfile:
    for fname in filenames:
        with open('../news/' + fname) as infile:
            outfile.write(infile.read())
