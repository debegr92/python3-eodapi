# EOD API
Wrapper for EOD Historical stock data.

API documentation: https://eodhistoricaldata.com/financial-apis/

# Install

## Clone Repository
```
cd CLONED_REPO_FOLDER
pip3 install --user .
```

# Example
Only a few lines of code needed to request data in a simple way:
```python
from eodapi import EODAPI

api = EODAPI('OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX')

stock = api.getFundamentals("AAPL", "US")

print(stock["Description"])
```