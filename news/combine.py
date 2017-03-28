import os

filenames = os.listdir('.')
with open('ALLNEWS.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
