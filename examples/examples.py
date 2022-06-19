import json
from eodapi import EODAPI

# Use your API token
api = EODAPI('OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX')

# Get API rate information
status, data = api.getUserData()
print(status)
print(json.dumps(data, indent="\t"))

status, data = api.getExchangeList()
print(status)
print(json.dumps(data, indent="\t"))

status, data = api.getTickers("XETRA")
print(status)
print(json.dumps(data, indent="\t"))

status, data = api.getTickers("US")
print(status)
print(len(data))
status, data = api.getTickers("US", onlyDelisted=True)
print(status)
print(len(data))
status, data = api.getTickers("US", onlyDelisted=False)
print(status)
print(len(data))

status, data = api.getOptions("AAPL", "US")
print(status)
print(json.dumps(data, indent="\t"))

status, data = api.getFundamentals("AAPL", "US")
print(status)
print(json.dumps(data, indent="\t"))

status, data = api.getSplitAdjustedQuotes("AAPL", "US")
print(status)
print(json.dumps(data, indent="\t"))

status, data = api.getAllDividends("AAPL", "US")
print(status)
print(json.dumps(data, indent="\t"))
status, data = api.getAllSplits("AAPL", "US")
print(status)
print(json.dumps(data, indent="\t"))

status, data = api.getHistoricalData("AAPL", "US")
#status, data = api.getHistoricalData("AAPL", "US", start="2021-08-01")
#status, data = api.getHistoricalData("AAPL", "US", start="2021-07-01", end="2021-07-31")
print(status)
print(json.dumps(data, indent="\t"))

# Get only quotes as default
status, data = api.getBulk("F")
# Or also splits and dividends
#status, data = api.getBulk("F", quotes=True, splits=True, dividends=True)
# For a specific date
#status, data = api.getBulk("US", quotes=False, splits=True, dividends=True, date="2021-08-10")
print(status)
print(json.dumps(data, indent="\t"))

status, data = api.getExchangeDetails("XETRA")
#status, data = api.getExchangeDetails("XETRA", start="2021-04-01", end="2021-05-01")
print(status)
print(json.dumps(data, indent="\t"))

# Single ticker
status, data = api.getRealTimeData("VOW3.F")
print(status)
print(json.dumps(data, indent="\t"))
# List of symbols
status, data = api.getRealTimeData(["VOW3.F", "AAPL.US"])
print(status)
print(json.dumps(data, indent="\t"))

# IPOs
status, data = api.getUpcomingIPOs()
#print(json.dumps(ipos, indent="\t"))
print(status)
print(json.dumps(data, indent="\t"))

# Insiders
status, data = api.getInsiderTransactions(start="2020-01-01", end="2020-12-31", code="AAPL.US")
print(status)
print(json.dumps(data, indent="\t"))