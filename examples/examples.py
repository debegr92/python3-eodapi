import json
from eodapi import EODAPI

# Use your API token
api = EODAPI('OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX')

#f = api.getExchangeList()

#f = api.getTickers("XETRA")

#f = api.getOptions("AAPL", "US")

f = api.getFundamentals("AAPL", "US")

#f = api.getAllDividends("AAPL", "US")
#f = api.getAllSplits("AAPL", "US")

#f = api.getHistoricalData("AAPL", "US")
#f = api.getHistoricalData("AAPL", "US", start="2021-08-01")
#f = api.getHistoricalData("AAPL", "US", start="2021-07-01", end="2021-07-31")

# Get only quotes as default
#f = api.getBulk("F")
# Or also splits and dividends
#f = api.getBulk("F", quotes=True, splits=True, dividends=True)
# For a specific date
#f = api.getBulk("US", quotes=False, splits=True, dividends=True, date="2021-08-10")

#f = api.getExchangeDetails("XETRA")
#f = api.getExchangeDetails("XETRA", start="2021-04-01", end="2021-05-01")

# Single ticker
#f = api.getRealTimeData("VOW3.F")
# List of symbols
#f = api.getRealTimeData(["VOW3.F", "AAPL.US"])

print(json.dumps(f, indent="\t"))

# Get API rate information
d = api.getUserData()
print(json.dumps(d, indent="\t"))