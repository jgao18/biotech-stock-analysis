# biotech-stock-analysis

1. [get-stocks.sh](scripts/get-stocks.sh) - Retrieves the [tickers](output/tickers.txt), [drugs](output/drugs.txt), [phases](output/phases.txt), and [catalyst dates](output/catalyst-dates.txt) from the [August 2016 FDA calendar](fda-calendar-aug-2016.html)
	1. The compiled data is written to [calendar-data](output/calendar-data.txt)
2. [get-prices.py](scripts/get-prices.py) - Retrieves each ticker's daily prices from the past year from Google Finance and writes them to [its own file](historical-stock-data/)
3. [get-news.sh](scripts/get-news.sh) - Retrieves each ticker's headlines from [The Street](https://www.thestreet.com/) and writes them to [its own file](news/)
	1. [filter-news.py](scripts/filter-news.py) - Retrieves only the headlines containing each ticker's drug name and writes them to [filtered-news.txt](output/filtered-news.txt)
4. [chart.py](scripts/chart.py) - Retrieves headlines of tickers from the filtered news containing certain key words ("positive", "efficacy", "designation", etc.) and plots the ticker's price data before and after the news date to [charts](charts/)