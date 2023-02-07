import yfinance as yf
from datetime   import date
# get last stock price
entercompany= str(input("Enter company ticker symbol: "))
entercompany.upper()
tickers = [entercompany]
today =date.today()
today=today.strftime("%B %d, %Y")

for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    company_name = ticker_yahoo.info['longName']
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    last_quote = round(last_quote,2)
    print("Latest Price: "+ company_name ,"is " + str(last_quote)+ " as of", today)
    quote = str(last_quote)

symbol = yf.Ticker("msft").info
pe = symbol["trailingPE"]
fowardPe=symbol["forwardPE"]
print("Current P/E: ",round(pe,2))
print("Forward P/E: ",round(fowardPe,2))

#Calculation

target_price = ((pe/fowardPe)*last_quote)
target_price =round(target_price,2)

print("The target price is: ", target_price)