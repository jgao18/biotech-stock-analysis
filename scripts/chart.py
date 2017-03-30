# Retrives news headlines containing keywords
# Retrieves price data 60 days before and after the event
# Plots the price data to charts/(ticker).png

from dateutil import parser
import numpy as np
import os
import sys
import textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import string
printable = set(string.printable)

keywords = ["POSITIVE", "INITIATES", "ENROLLMENT", "DESIGNATION", "COMPLETES", "GRANTED", "INITIATION", "EFFICACY", "FAST", "ACCEPTED", "CHECKPOINT", "APPROVES"]

for keyword in keywords:
    if not os.path.exists('../charts/' + keyword):
        os.mkdir('../charts/' + keyword)

with open("../output/filtered-news.txt") as newsFile:
    for line in newsFile:
        ticker = line.split(',')[0]
        cataDate = line.split(',')[1]
        drug = line.split(',')[2]
        newsDateOrig = line.split(',')[3]
        newsDate = parser.parse(newsDateOrig)
        headline = line.split(',')[4]
        for keyword in keywords:
            if (keyword in line.upper()) and (newsDate > parser.parse("3-28-2016")) and (newsDate < parser.parse(cataDate)):
                dataLines = []
                with open("../historical-stock-data/" + ticker + ".txt") as dataFile:
                    for dataLine in dataFile:
                        dataLine = dataLine.strip() 
                        dataLines.append(dataLine)
                prices = []
                dayCounter = 0
                newsDay = 0
                for data in dataLines:
                    dataSplit = data.split(',')
                    dataDate = parser.parse(dataSplit[0])
                    dataPrice = dataSplit[1]
        
                    if abs((dataDate - newsDate).days) == 0: # mark news date
                        newsDay = dayCounter
                        prices.append(dataPrice)
                    if abs((dataDate - newsDate).days) < 60:
                        dayCounter+=1
                        prices.append(dataPrice)
                    
                fig = plt.figure(figsize=(25,10))
                plt.plot(prices,marker='o')
                plt.axvline(x=newsDay, color='r', linestyle='--')
                fig.suptitle("\n".join(textwrap.wrap(filter(lambda x: x in printable, headline), 80)) + '\nCatalyst Date: ' + cataDate, fontsize=12)
                plt.xticks(np.arange(0, len(prices), 5))
                plt.xlabel('News Day: ' + str(newsDay) + ' (' + newsDate.strftime("%m/%d/%Y") + ')' , fontsize=18)
                plt.ylabel('Price of ' + ticker + ' (' + drug + ')', fontsize=18)
                i = 0
                while os.path.exists('../charts/' + keyword + '/' + ticker + '-' + str(i) + '.png'):
                    i += 1
                plt.savefig('../charts/' + keyword + '/' + ticker + '-' + str(i))
                plt.close(fig)
                break
                                                                    
                    
            

        
