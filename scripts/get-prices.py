# Retrieves daily prices for the past year from Google Finance for each stock
# Writes the data to historical-stock-data/(ticker).txt

import urllib
import re
import datetime

tickers = []
with open("../output/tickers.txt") as file:
    for line in file:
        line = line.strip() 
        tickers.append(line)

for ticker in tickers:
    f = urllib.urlopen("https://www.google.com/finance/getprices?i=86400&p=1Y&f=d,o,h,l,c,v&q=" + ticker) # i - 86400/day
    myF = f.read()
    dataFile = open("../historical-stock-data/" + ticker + ".txt", "w")
    dataString = myF.split("\n",6)[6]
    dataString = re.sub(r"TIMEZONE_OFFSET=[^\n]*\n", "", dataString)
    
    output = ""
    humanTime = ""
    for line in dataString.splitlines():
        lineSplit = line.split(',')
        if line[0] == 'a': # unix timestamp
            uTime = lineSplit[0]
            uTime = uTime[1:]
            humanTime = datetime.datetime.fromtimestamp(int(uTime))
            lineSplit[0] = humanTime.strftime('%m-%d-%Y')
            output += ','.join(lineSplit) + "\n"
        else: # delta
            delta = datetime.timedelta(days=int(lineSplit[0])) # interval
            newTime = humanTime + delta
            lineSplit[0] = newTime.strftime('%m-%d-%Y')
            output += ','.join(lineSplit) + "\n"
            
    dataFile.write(output)
    dataFile.close()
