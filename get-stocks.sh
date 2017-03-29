# Retrives the tickers, drug names, phase, and catalyst dates for each stock on the FDA calendar
# Writes the data to together.txt

tickers=$(cat fda-calendar-aug-2016.html | egrep 'class="ticker">' | egrep -o '>[^<]+' | sed 's/>//' | head -n -156)
drugs=$(cat fda-calendar-aug-2016.html | egrep 'class="drug">' | egrep -o '>[^<]+' | sed 's/>//' | head -n -156)
phases=$(cat fda-calendar-aug-2016.html | egrep 'class="stage"' | egrep -o 'data-value="[^"]*' | sed 's/data-value="//' | head -n -156)
cataDates=$(cat fda-calendar-aug-2016.html | egrep 'class="catalyst-date"' | egrep -o '>[^<]+' | sed 's/>//' | head -n -156)
paste -d ',' <(echo "$tickers") <(echo "$drugs") <(echo "$phases") <(echo "$cataDates") > together.txt
