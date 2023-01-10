"""""
import yfinance as yf

entercompany= str(input("Enter company ticker symbol: "))
stock = yf.download(entercompany, start="2022-12-20", end="2022-12-30", group_by="ticker")
ticker = entercompany
ticker.info


# show sustainability
#print(cg.sustainability)

"""

import yfinance as yf
# get last stock price
entercompany= str(input("Enter company ticker symbol: "))
entercompany.upper()
tickers = [entercompany]


for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    company_name = ticker_yahoo.info['longName']
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    last_quote = round(last_quote,2)
    print("Latest Price: "+ company_name ,"is " + str(last_quote))
    quote = str(last_quote)

with open('Data.txt', 'a') as file:
    file.writelines("% s\n" % data for data in company_name)
    file.writelines("% s" % data for data in quote)

