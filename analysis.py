from dateutil import parser

marker = "*"
with open("together.txt") as togetherFile:
    for line in togetherFile:
        lineSplit = line.split(',')
        ticker = lineSplit[0]
        catalystDate = lineSplit[-1]
        catalystDate = parser.parse(catalystDate)
        dataLines = []
        with open("historical-stock-data/" + ticker + ".txt") as dataFile:
            for dataLine in dataFile:
                dataLine = dataLine.strip() 
                dataLines.append(dataLine)
        output = ticker + " "
        lastPrice = 0
        postCatalyst = False
        for data in dataLines:
            dataSplit = data.split(',')
            dataDate = parser.parse(dataSplit[0])
            dataPrice = dataSplit[1]
            if dataDate > catalystDate and postCatalyst is False:
                output += "!!! "
                postCatalyst = True
                
            if lastPrice == 0:
                lastPrice = dataPrice
                output += lastPrice + " "
            else:
                if dataPrice < lastPrice:
                    output += "v "
                elif dataPrice == lastPrice:
                    output += "- "
                else:
                    output += "^ "
                lastPrice = dataPrice
        print output
            
                
            

        
