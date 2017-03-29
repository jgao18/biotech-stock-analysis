# Retrieves the first 180 headlines from TheStreet for each stock
# Writes the headlines to news/(ticker).txt

cat tickers.txt | while read ticker
do
   for i in {0..150..30}
	do
		url="https://www.thestreet.com/quote/$ticker""/details/news?start=$i"
		headlines=$(curl $url | egrep "news-list-compact__headline" | egrep -o '>[^<]+' | sed 's/>//' | sed '$d')
		dates=$(curl $url | egrep "<time datetime=" | sed '1d' | egrep -o 'datetime="[^T]+' | sed 's/datetime="//')
		paste -d ',' <(echo "$dates") <(echo "$headlines") >> news/$ticker.txt
	done

done