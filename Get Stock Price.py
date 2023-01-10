import yfinance as yf

company= str(input("Enter company ticker symbol: "))
stock = yf.download(company, start="2022-12-20", end="2022-12-30", group_by="ticker")


company_name = yf.Ticker(company)

#print company name

msft = yf.Ticker(company)

company_name = msft.info['longName']

#print(company_name)
print("Here is the stock data for " + company_name)

print(stock)


#df = yf.download("AMZN MSFT", start="2022-12-20", end="2022-12-30",group_by="ticker")
#print(df)
#print(df.AMZN)

""""
This code will write it to a file
"""

with open('Stock Data.txt', 'a') as file:
    #company_name = input("Which Company is this?: ")
    #name = [company_name]
    file.writelines("% s\n" % data for data in company_name)
    #file.writelines("% s\n" % data for data in msft)
