# Filters out news headlines with the drug name in them to filtered-text.txt

tickers = []
with open("../output/tickers.txt") as file:
    for line in file:
        line = line.strip() 
        tickers.append(line)
       
drugs = []
with open("../output/drugs.txt") as file:
    for line in file:
        line = line.strip() 
        drugs.append(line.split(' ')[0])
        
cataDates = []
with open("../output/catalyst-dates.txt") as file:
    for line in file:
        line = line.strip() 
        cataDates.append(line.split(' ')[0])

for i in range(0, len(tickers)):
    ticker = tickers[i]
    drug = drugs[i]
    cataDate = cataDates[i]
    with open("../news/" + tickers[i] + ".txt") as newsFile:
        with open("../output/filtered-news.txt", 'a') as filteredFile:
            for newsLine in newsFile:
                if drug.lower() in newsLine.lower():
                    filteredFile.write(ticker + ',' + cataDate + ',' + drug + ',' + newsLine)

# Remove duplicate headlines
lines_seen = set() 
unique = []
for line in open("../output/filtered-news.txt", "r"):
    if line not in lines_seen:
        unique.append(line)
        lines_seen.add(line)
        
with open("../output/filtered-news.txt", "w") as uniqueFilteredFile:
    for line in unique:
        uniqueFilteredFile.write(line)
