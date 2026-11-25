---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/stockoptions
api_type: REST
updated_at: 2026-11-25 18:57:31.507034
---

# Stock options

Options trading provides underlying, contract, market data, position and order management.

  * Documentation route prefix: `/stock_options`
  * Authentication, signing and the common error structure follow APIv4.

##  Get option trading fee rates

GET`/stock_options/fee-rate`

GET `/stock_options/fee-rate`

_Get option trading fee rates_

Query the fee configuration for options trading before placing an order. Returns the rates and applicable minimum and maximum fees for SEC, TAF, OCC, ORF and CAT charges.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Option trading fee configuration | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionConfigResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
sec | string | Optional |  | SEC fee rate.  
min_sec | string | Optional |  | Minimum SEC fee.  
max_sec | string | Optional |  | Maximum SEC fee; empty means no limit.  
taf | string | Optional |  | TAF fee rate.  
min_taf | string | Optional |  | Minimum TAF fee.  
max_taf | string | Optional |  | Maximum TAF fee.  
occ | string | Optional |  | OCC fee.  
orf | string | Optional |  | ORF fee.  
cat | string | Optional |  | CAT fee.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/fee-rate'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/fee-rate \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "sec": "0.0000206",
        "min_sec": "0.01",
        "max_sec": "",
        "taf": "0.00279",
        "min_taf": "0.01",
        "max_taf": "9.79",
        "occ": "0.025",
        "orf": "0.012",
        "cat": "0.0003"
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  List option underlyings

GET`/stock_options/underlyings`

GET `/stock_options/underlyings`

_List option underlyings_

Query available option underlyings before looking up contracts, expiration dates and option chains. Returns underlying symbols, names, multilingual descriptions, icons, price precision and order quantity limits. `underlyings` accepts multiple comma-separated symbols; omit it to query all available underlyings.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlyings | query | string | Optional | Comma-separated option underlying symbols, for example AAPL,TSLA. Omit to query all available underlyings.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Option underlying list | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionSymbolListResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
underlying | string | Optional |  | Option underlying symbol.  
description | string | Optional |  | Underlying description.  
descs | array | Optional |  | Underlying descriptions in multiple languages.  
icon_link | string | Optional |  | Underlying icon URL.  
price_precision | integer | Optional |  | Number of decimal places for prices.  
min_order_volume | string | Optional |  | Minimum order quantity.  
max_order_volume | string | Optional |  | Maximum order quantity.  
step_order_volume | string | Optional |  | Order quantity increment.  
  
**allOf[1] / data / list / items / descs**

Underlying descriptions in multiple languages.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items / descs / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
lang | string | Optional |  | Language code.  
value | string | Optional |  | Underlying description in this language.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/underlyings'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/underlyings \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "list": [
          {
            "underlying": "AAPL",
            "description": "Apple Inc.",
            "descs": [
              {
                "lang": "en",
                "value": "Apple Inc."
              }
            ],
            "icon_link": "https://example.com/aapl.png",
            "price_precision": 2,
            "min_order_volume": "1",
            "max_order_volume": "1000",
            "step_order_volume": "1"
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  List option contracts

GET`/stock_options/contracts`

GET `/stock_options/contracts`

_List option contracts_

Query option contracts for an underlying, including contract symbols, strike prices, expiration dates and trading rules. `underlying` is required. Filter by expiration date and call or put type; only US market (`us`) contracts are currently available. Results are paginated in ascending contract symbol order, with total records, total pages and the current page. The default and maximum `page_size` are both 1000. Use price precision and minimum and maximum order quantities to check an order before submission.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Option underlying symbol, for example AAPL. This is one underlying symbol, not an option contract symbol.  
exchange | query | string | Optional | Trading market filter. Only US market (us) contracts are currently available. Omitted or empty values use us.  
\- us: US market.  
expiration_date | query | string(date) | Optional | Option expiration date in YYYY-MM-DD format. Omit to disable expiration date filtering.  
option_type | query | StockOptionOptionType | Optional | Option type filter for the contract list. Omit for both types.  
\- call: Call option.  
\- put: Put option.  
page | query | integer | Optional | Page number, starting from 1. Defaults to 1 when omitted.  
page_size | query | integer | Optional | Contracts per page. Defaults to 1000 when omitted; values above 1000 are capped at 1000.  
  
####  Detailed descriptions

**exchange** : Trading market filter. Only US market (us) contracts are currently available. Omitted or empty values use us.  
\- us: US market.

**option_type** : Option type filter for the contract list. Omit for both types.  
\- call: Call option.  
\- put: Put option.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
exchange | us  
option_type | call  
option_type | put  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Option contract list | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionContractListResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total number of matching records.  
total_page | integer | Optional |  | Total number of pages.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
exchange | string | Optional |  | Trading market.  
expiration_date | string(date) | Optional |  | Option expiration date in YYYY-MM-DD format.  
settlement_date | string(date) | Optional |  | Option settlement date in YYYY-MM-DD format.  
strike_price | string | Optional |  | Strike price.  
option_type | string | Optional | enum: ["call","put"] | Option type.  
\- call: Call option.  
\- put: Put option.  
multiplier | string | Optional |  | Contract multiplier.  
open_interest | string | Optional |  | Open interest.  
quote_currency | string | Optional |  | Quote currency.  
settlement_type | string | Optional |  | Settlement type.  
trade_status | string | Optional | enum: ["open","closed"] | Current contract trading status.  
\- open: Within trading hours, with both the contract and underlying tradable.  
\- closed: Not tradable, including outside trading hours, an inactive contract or a disabled underlying.  
trade_mode | integer | Optional | enum: [0,4] | Current trading mode.  
\- 0: Trading disabled.  
\- 4: Buying and selling allowed; regular accounts still require sufficient available long positions to sell.  
price_precision | integer | Optional |  | Number of decimal places for prices.  
min_order_volume | string | Optional |  | Minimum order quantity.  
max_order_volume | string | Optional |  | Maximum order quantity.  
step_order_volume | string | Optional |  | Order quantity increment.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/contracts'
    query_param = 'underlying=AAPL'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/contracts?underlying=AAPL \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "symbol": "AAPL260814P00130000",
            "symbol_display": "AAPL-260814-130-P",
            "underlying": "AAPL",
            "exchange": "us",
            "expiration_date": "2026-08-14",
            "settlement_date": "2026-08-15",
            "strike_price": "130",
            "option_type": "put",
            "multiplier": "100",
            "open_interest": "100",
            "quote_currency": "USD",
            "settlement_type": "physical",
            "trade_status": "open",
            "trade_mode": 4,
            "price_precision": 2,
            "min_order_volume": "1",
            "max_order_volume": "1000",
            "step_order_volume": "1"
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  List option expiration dates

GET`/stock_options/market/expirations`

GET `/stock_options/market/expirations`

_List option expiration dates_

Query expiration dates for an option underlying before selecting a contract expiration. `underlying` is required. Returns dates and their Unix timestamps; use the selected date to query the option chain.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Option underlying symbol, for example AAPL. This is one underlying symbol, not an option contract symbol.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Option expiration date list | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionExpirationListResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
underlying | string | Optional |  | Option underlying symbol.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
expiration_date | string(date) | Optional |  | Option expiration date in YYYY-MM-DD format.  
expiration_date_ts | integer(int64) | Optional |  | Unix timestamp of the expiration date.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/market/expirations'
    query_param = 'underlying=AAPL'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/market/expirations?underlying=AAPL \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "underlying": "AAPL",
        "list": [
          {
            "expiration_date": "2026-08-14",
            "expiration_date_ts": 1786665600
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  Get the option chain

GET`/stock_options/market/chain`

GET `/stock_options/market/chain`

_Get the option chain_

Query option quotes at different strike prices for the same underlying and expiration date to compare call and put contracts. `underlying` and `expiration_date` are required. Set `option_type` to `call` or `put` to filter; omit it or use `all` for both types. Returns contract symbols, strike prices, bid and ask quotes, last prices, mark prices, implied volatility and Greeks.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Option underlying symbol, for example AAPL. This is one underlying symbol, not an option contract symbol.  
expiration_date | query | string(date) | Required | Required option expiration date in YYYY-MM-DD format, obtained from the expiration date list.  
option_type | query | string | Optional | Option type filter for the option chain.  
\- call: Call options only.  
\- put: Put options only.  
\- all: Both types, equivalent to omitting this parameter.  
  
####  Detailed descriptions

**option_type** : Option type filter for the option chain.  
\- call: Call options only.  
\- put: Put options only.  
\- all: Both types, equivalent to omitting this parameter.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
option_type | call  
option_type | put  
option_type | all  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Option chain | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionOptionChainResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
underlying | string | Optional |  | Option underlying symbol.  
expiration_date | string(date) | Optional |  | Option expiration date in YYYY-MM-DD format.  
expiration_date_ts | integer(int64) | Optional |  | Unix timestamp of the expiration date.  
index_price | string | Optional |  | Underlying index price; empty when no valid value is available.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
strike_price | string | Optional |  | Strike price.  
option_type | string | Optional | enum: ["call","put"] | Option type.  
\- call: Call option.  
\- put: Put option.  
bid | string | Optional |  | Best bid price.  
ask | string | Optional |  | Best ask price.  
mark_price | string | Optional |  | Mark price.  
mark_iv | string | Optional |  | Mark implied volatility.  
last | string | Optional |  | Last traded price.  
display_price | string | Optional |  | Display price.  
breakeven_price | string | Optional |  | Breakeven price.  
to_breakeven_pct | string | Optional |  | Percentage distance to the breakeven price.  
today_change_pct | string | Optional |  | Price change percentage today.  
open_interest | string | Optional |  | Open interest.  
position | string | Optional |  | Position quantity.  
delta | string | Optional |  | Option delta.  
gamma | string | Optional |  | Option gamma.  
theta | string | Optional |  | Option theta.  
vega | string | Optional |  | Option vega.  
rho | string | Optional |  | Option rho.  
trade_status | string | Optional | enum: ["open","closed"] | Current contract trading status.  
\- open: Within trading hours, with both the contract and underlying tradable.  
\- closed: Not tradable, including outside trading hours, an inactive contract or a disabled underlying.  
trade_mode | integer | Optional | enum: [0,4] | Current trading mode.  
\- 0: Trading disabled.  
\- 4: Buying and selling allowed; regular accounts still require sufficient available long positions to sell.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/market/chain'
    query_param = 'underlying=AAPL&expiration_date=2026-08-14'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/market/chain?underlying=AAPL&expiration_date=2026-08-14 \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "underlying": "AAPL",
        "expiration_date": "2026-08-14",
        "expiration_date_ts": 1786665600,
        "index_price": "130.25",
        "list": [
          {
            "symbol": "AAPL260814P00130000",
            "symbol_display": "AAPL-260814-130-P",
            "strike_price": "130",
            "option_type": "put",
            "bid": "1.10",
            "ask": "1.20",
            "mark_price": "1.15",
            "mark_iv": "0.25",
            "last": "1.18",
            "display_price": "1.15",
            "breakeven_price": "128.85",
            "to_breakeven_pct": "-0.0108",
            "today_change_pct": "0.05",
            "open_interest": "100",
            "position": "0",
            "delta": "-0.45",
            "gamma": "0.03",
            "theta": "-0.02",
            "vega": "0.10",
            "rho": "-0.01",
            "trade_status": "open",
            "trade_mode": 4
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  Get the option order book

GET`/stock_options/market/{symbol}/orderbook`

GET `/stock_options/market/{symbol}/orderbook`

_Get the option order book_

Query the best bid and ask for an option contract. `symbol` is the option contract symbol. Each of `bids` and `asks` contains at most one price level, without order quantities. A side without an available quote is an empty array. Both sides are empty arrays when the contract is not found.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | path | string | Required | Option contract symbol  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Option order book | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionOrderBookResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
bids | array | Optional |  | Bid prices; at most one level, or an empty array when no quote is available.  
asks | array | Optional |  | Ask prices; at most one level, or an empty array when no quote is available.  
  
**allOf[1] / data / bids**

Bid prices; at most one level, or an empty array when no quote is available.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / bids / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Optional |  | Quoted price.  
  
**allOf[1] / data / asks**

Ask prices; at most one level, or an empty array when no quote is available.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / asks / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Optional |  | Quoted price.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/market/AAPL260814P00130000/orderbook'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/market/AAPL260814P00130000/orderbook \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "symbol": "AAPL260814P00130000",
        "symbol_display": "AAPL-260814-130-P",
        "bids": [
          {
            "price": "1.10"
          }
        ],
        "asks": [
          {
            "price": "1.20"
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  List current option positions🔒 Authenticated

GET`/stock_options/positions`

GET `/stock_options/positions`

_List current option positions_

Query the current user's option positions, market values and profit and loss. Filter by `underlying` or `symbol`. A specified `symbol` must identify an existing option contract; no position returns an empty list. `price_type` selects the price for market value, unrealized PnL and today's PnL: `latest` (default) uses the last traded price; `mark` uses the mark price. Aggregate `today_pnl` includes current positions and contracts fully closed today. Results are sorted by `open_time` descending, then `symbol` ascending.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Optional | Option underlying symbol, for example AAPL. Omit to disable underlying filtering. Current orders support only one underlying.  
symbol | query | string | Optional | Full option contract symbol, for example AAPL260814P00130000. Omit to disable contract filtering.  
price_type | query | StockOptionPositionPnlPriceType | Optional | Valuation price type for position market value, unrealized PnL, and daily PnL.  
Options: `latest` (last traded price) or `mark` (mark price). Defaults to `latest` when omitted or empty.  
  
####  Detailed descriptions

**price_type** : Valuation price type for position market value, unrealized PnL, and daily PnL.  
Options: `latest` (last traded price) or `mark` (mark price). Defaults to `latest` when omitted or empty.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
price_type | latest  
price_type | mark  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Current option position list | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionPositionListResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
today_pnl | string | Optional |  | Total daily option PnL = sum of today_pnl for current positions + daily PnL for contracts fully closed today.  
The valuation price for current positions is selected by the request parameter `price_type`.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
side | string | Optional | enum: ["long","short"] | Position side.  
\- long: Long position.  
\- short: Short position.  
open_time | integer(int64) | Optional |  | Position opening time as a Unix timestamp in seconds; 0 when unavailable.  
quantity | string | Optional |  | Position quantity.  
available | string | Optional |  | Available quantity; currently equal to quantity.  
frozen | string | Optional |  | Frozen quantity; may be empty when not calculated separately.  
avg_entry_price | string | Optional |  | Average entry price.  
last_price | string | Optional |  | Last traded price; 0 when no valid value is available.  
mark_price | string | Optional |  | Mark price; 0 when no valid value is available.  
previous_close | string | Optional |  | Previous closing price.  
If no valid positive value exists, this field may be empty and daily PnL calculation is skipped.  
market_value | string | Optional |  | Market value = valuation price × signed position quantity × contract multiplier.  
The valuation price is selected by `price_type` (`latest` uses last_price; `mark` uses mark_price).  
unrealized_pnl | string | Optional |  | Unrealized PnL = (valuation price - average entry price) × signed position quantity × contract multiplier.  
Returns 0 if the average entry price or quantity is invalid. The valuation price follows the same rules as market_value.  
today_pnl | string | Optional |  | Daily PnL for this contract. Requires a valid previous_close; 0 if unavailable.  
The valuation price follows the same rules as market_value.  
today_buy_qty | string | Optional |  | Quantity bought today (user's daily trading totals).  
today_sell_qty | string | Optional |  | Quantity sold today (user's daily trading totals).  
today_buy_value | string | Optional |  | Amount bought today (user's daily trading totals).  
today_sell_value | string | Optional |  | Amount sold today (user's daily trading totals).  
trade_status | string | Optional | enum: ["open","closed"] | Current contract trading status.  
\- open: Within trading hours, with both the contract and underlying tradable.  
\- closed: Not tradable, including outside trading hours, an inactive contract or a disabled underlying.  
trade_mode | integer | Optional | enum: [0,4] | Current trading mode.  
\- 0: Trading disabled.  
\- 4: Buying and selling allowed; regular accounts still require sufficient available long positions to sell.  
multiplier | string | Optional |  | Contract multiplier.  
price_precision | integer | Optional |  | Number of decimal places for prices.  
min_order_volume | string | Optional |  | Minimum order quantity.  
max_order_volume | string | Optional |  | Maximum order quantity.  
step_order_volume | string | Optional |  | Order quantity increment.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/positions'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/stock_options/positions"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "today_pnl": "68.50",
        "list": [
          {
            "symbol": "AAPL260821C00210000",
            "symbol_display": "AAPL-260821-210-C",
            "underlying": "AAPL",
            "side": "long",
            "open_time": 1785919118,
            "quantity": "2",
            "available": "2",
            "frozen": "0",
            "avg_entry_price": "10.95",
            "last_price": "12.18",
            "mark_price": "12.05",
            "previous_close": "11.20",
            "market_value": "2436.00",
            "unrealized_pnl": "246.00",
            "today_pnl": "54.00",
            "today_buy_qty": "1",
            "today_sell_qty": "0",
            "today_buy_value": "100.00",
            "today_sell_value": "0",
            "trade_status": "open",
            "trade_mode": 4,
            "multiplier": "100",
            "price_precision": 2,
            "min_order_volume": "1",
            "max_order_volume": "1000",
            "step_order_volume": "1"
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  Close an option position🔒 Authenticated

POST`/stock_options/positions/close`

POST `/stock_options/positions/close`

_Close an option position_

Submit a closing order for part or all of an option position. `symbol` and `quantity` are required. The positive quantity must not exceed the available position and must satisfy the contract's minimum, maximum and quantity increment rules. Omit `order_type` or pass an empty value for a `market` order. A `limit` order requires a positive `price`; a market order ignores `price`. The closing side is derived from the position and time in force is fixed to `day`. The response returns the closing `order_id`; query the order for its subsequent status.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | StockOptionClosePositionRequest | Required | none  
symbol | body | string | Required | Option contract symbol to close, with an available position.  
quantity | body | string | Required | Quantity to close as a positive decimal string. Must not exceed the available position and must satisfy the contract's minimum, maximum and quantity increment rules.  
order_type | body | string | Optional | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
price | body | string | Optional | Positive limit closing price as a plain decimal string, up to 64 characters, without scientific notation. Ignored for market closing orders.  
client_order_id | body | string | Optional | Custom closing order identifier. Generated automatically when omitted or whitespace-only.  
  
####  Detailed descriptions

** order_type**: Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
order_type | market  
order_type | limit  
  
####  Request Body Schema

`order_type` is optional. Omitted or empty values close at market; only `market` and `limit` are supported.

Request Body SchemaType | Constraints  
---|---  
StockOptionClosePositionRequest | required: ["symbol","quantity"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Option contract symbol to close, with an available position.  
quantity | string | Required |  | Quantity to close as a positive decimal string. Must not exceed the available position and must satisfy the contract's minimum, maximum and quantity increment rules.  
order_type | string | Optional | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
price | string | Optional |  | Positive limit closing price as a plain decimal string, up to 64 characters, without scientific notation. Ignored for market closing orders.  
client_order_id | string | Optional |  | Custom closing order identifier. Generated automatically when omitted or whitespace-only.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position closing response | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionClosePositionResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/positions/close'
    query_param = ''
    body='{"symbol":"string","quantity":"string","order_type":"market","price":"1.00","client_order_id":"string"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/stock_options/positions/close"
    query_param=""
    body_param='{"symbol":"string","quantity":"string","order_type":"market","price":"1.00","client_order_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "symbol": "string",
      "quantity": "string",
      "order_type": "market",
      "price": "1.00",
      "client_order_id": "string"
    }
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "order_id": "8000000001"
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  List current option orders🔒 Authenticated

GET`/stock_options/orders`

GET `/stock_options/orders`

_List current option orders_

Query the current user's unfinished option orders, including open and partially filled orders. Filter by `underlying`, `symbol` or `side`. `underlying` accepts only one symbol, not a comma-separated list. `status` includes only 1 (new) and 2 (partially filled). Query order history for terminal orders. Matching orders are sorted by creation time `time_setup` descending. This endpoint has no pagination parameters.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Optional | Option underlying symbol, for example AAPL. Omit to disable underlying filtering. Current orders support only one underlying.  
symbol | query | string | Optional | Full option contract symbol, for example AAPL260814P00130000. Omit to disable contract filtering.  
side | query | StockOptionOrderListSide | Optional | Order side filter.  
Omit to query both sides.  
\- 1: Sell orders only.  
\- 2: Buy orders only.  
  
####  Detailed descriptions

**side** : Order side filter.  
Omit to query both sides.  
\- 1: Sell orders only.  
\- 2: Buy orders only.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | 1  
side | 2  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Current option order list | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionOrderListResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Current unfinished orders, excluding filled, cancelled and rejected terminal orders.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID.  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
side | integer | Optional | enum: [1,2] | Order side.  
\- 1: Sell.  
\- 2: Buy.  
order_type | string | Optional | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
status | integer | Optional | enum: [1,2] | Current order status:  
\- 1: New, validated and awaiting processing.  
\- 2: Partially filled, with a remaining unfilled quantity.  
status_desc | string | Optional |  | Human-readable order status description in the requested language.  
time_in_force | string | Optional | enum: ["day","gtc"] | Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.  
quantity | string | Optional |  | Order quantity.  
filled_quantity | string | Optional |  | Filled quantity.  
price | string | Optional |  | Order price.  
time_setup | integer(int64) | Optional |  | Order creation time.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/orders'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/stock_options/orders"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "list": [
          {
            "order_id": "8000000001",
            "symbol": "AAPL260814P00130000",
            "symbol_display": "AAPL-260814-130-P",
            "underlying": "AAPL",
            "side": 2,
            "order_type": "limit",
            "status": 1,
            "status_desc": "new",
            "time_in_force": "day",
            "quantity": "1",
            "filled_quantity": "0",
            "price": "1.20",
            "time_setup": 1785919118
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  Create an option order🔒 Authenticated

POST`/stock_options/orders`

POST `/stock_options/orders`

_Create an option order_

Submit a buy or sell order for an option contract and return the order ID on success. `symbol`, `side`, `order_type`, `time_in_force` and `quantity` are required. `side` is 1 (sell) or 2 (buy). Limit orders require a positive `price` and support `day` or `gtc`. Market orders ignore `price` and support only `day`. Quantity is a positive decimal string within the contract's minimum and maximum order quantities. Sell orders require sufficient available long positions. `client_order_id` is optional and is generated automatically when omitted or whitespace-only. Query current orders or order details to track the returned order ID.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | StockOptionPutOrderRequest | Required | none  
symbol | body | string | Required | Full option contract symbol to trade, obtained from the contract list or option chain.  
side | body | integer | Required | Order side.  
\- 1: Sell.  
\- 2: Buy.  
order_type | body | string | Required | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
time_in_force | body | string | Required | Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.  
price | body | string | Optional | Limit order price as a positive plain decimal string, up to 64 characters, without scientific notation. Required for limit orders and ignored for market orders.  
quantity | body | string | Required | Order quantity as a positive decimal string within the contract's minimum and maximum order quantities.  
client_order_id | body | string | Optional | Optional custom order identifier, up to 30 UTF-8 bytes. Generated automatically when omitted or whitespace-only.  
  
####  Detailed descriptions

** side**: Order side.  
\- 1: Sell.  
\- 2: Buy.

** order_type**: Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.

** time_in_force**: Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | 1  
side | 2  
time_in_force | day  
time_in_force | gtc  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
StockOptionPutOrderRequest | required: ["symbol","side","order_type","time_in_force","quantity"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Full option contract symbol to trade, obtained from the contract list or option chain.  
side | integer | Required | enum: [1,2] | Order side.  
\- 1: Sell.  
\- 2: Buy.  
order_type | string | Required | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
time_in_force | string | Required | enum: ["day","gtc"] | Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.  
price | string | Optional |  | Limit order price as a positive plain decimal string, up to 64 characters, without scientific notation. Required for limit orders and ignored for market orders.  
quantity | string | Required |  | Order quantity as a positive decimal string within the contract's minimum and maximum order quantities.  
client_order_id | string | Optional | maxLength: 30 | Optional custom order identifier, up to 30 UTF-8 bytes. Generated automatically when omitted or whitespace-only.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order creation response | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionPutOrderResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/orders'
    query_param = ''
    body='{"symbol":"AAPL260814P00130000","side":1,"order_type":"market","time_in_force":"day","price":"1.00","quantity":"1","client_order_id":"string"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/stock_options/orders"
    query_param=""
    body_param='{"symbol":"AAPL260814P00130000","side":1,"order_type":"market","time_in_force":"day","price":"1.00","quantity":"1","client_order_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "symbol": "AAPL260814P00130000",
      "side": 1,
      "order_type": "market",
      "time_in_force": "day",
      "price": "1.00",
      "quantity": "1",
      "client_order_id": "string"
    }
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "id": "8000000001"
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  Cancel all option limit orders🔒 Authenticated

DELETE`/stock_options/orders`

DELETE `/stock_options/orders`

_Cancel all option limit orders_

Cancel all or a filtered set of the current user's option limit orders. The request body may be omitted or an empty object. Without filters, all limit orders are cancelled. Filter by `underlying`, `symbol` or `side`. `side` supports 1 (sell) and 2 (buy); omit it to include both sides. The response reports the cancellation request result. Query the orders to confirm their subsequent status.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | StockOptionCancelAllOrdersRequest | Optional | none  
underlying | body | string | Optional | Option underlying symbol. Empty or omitted values disable underlying filtering.  
symbol | body | string | Optional | Option contract symbol. Empty or omitted values disable contract filtering.  
side | body | integer | Optional | Order side filter.  
Omit to query both sides.  
\- 1: Sell orders only.  
\- 2: Buy orders only.  
  
####  Detailed descriptions

** side**: Order side filter.  
Omit to query both sides.  
\- 1: Sell orders only.  
\- 2: Buy orders only.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | 1  
side | 2  
  
####  Request Body Schema

Filters for cancelling limit orders in bulk. side is 1 (sell) or 2 (buy); omit it to include both sides.

Request Body SchemaType | Constraints  
---|---  
StockOptionCancelAllOrdersRequest |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
underlying | string | Optional |  | Option underlying symbol. Empty or omitted values disable underlying filtering.  
symbol | string | Optional |  | Option contract symbol. Empty or omitted values disable contract filtering.  
side | integer | Optional | enum: [1,2] | Order side filter.  
Omit to query both sides.  
\- 1: Sell orders only.  
\- 2: Buy orders only.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Bulk order cancellation response | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionCancelAllOrdersResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
success | boolean | Optional |  | Whether the cancellation request succeeded.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/orders'
    query_param = ''
    body='{"underlying":"AAPL","symbol":"string","side":1}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('DELETE', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/stock_options/orders"
    query_param=""
    body_param='{"underlying":"AAPL","symbol":"string","side":1}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "underlying": "AAPL",
      "symbol": "string",
      "side": 1
    }
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "success": true
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  Get option order details🔒 Authenticated

GET`/stock_options/orders/{order_id}`

GET `/stock_options/orders/{order_id}`

_Get option order details_

Query one of the current user's orders by ID to track its status, filled quantity and average fill price. `order_id` is required and must be a positive integer represented as a string. Both current and finished orders can be queried, without filtering by terminal status. Returns price, quantity, filled quantity, status description, average fill price, fees and timestamps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | Option order ID as a positive integer string, obtained from order submission or query results.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Option order details | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionOrderDetailResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  | Order details for a current or finished order.  
  
**allOf[1] / data**

Order details for a current or finished order.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID.  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
side | integer | Optional | enum: [1,2] | Order side.  
\- 1: Sell.  
\- 2: Buy.  
order_type | string | Optional | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
status | integer | Optional |  | Order status in order details. The details endpoint does not filter by status.  
\- 1: New, validated and awaiting processing.  
\- 2: Partially filled, with a remaining unfilled quantity.  
\- 3: Filled, terminal.  
\- 4: Cancelled, terminal; the order may have been partially filled.  
\- 5: Rejected, terminal.  
Current orders include only 1 and 2; order history includes only 3, 4 and 5.  
status_desc | string | Optional |  | Human-readable order status description in the requested language.  
time_in_force | string | Optional | enum: ["day","gtc"] | Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.  
quantity | string | Optional |  | Order quantity.  
filled_quantity | string | Optional |  | Filled quantity.  
price | string | Optional |  | Order price.  
time_setup | integer(int64) | Optional |  | Order creation time.  
avg_fill_price | string | Optional |  | Average fill price.  
fee | string | Optional |  | Trading fee.  
time_done | integer(int64) | Optional |  | Order completion time.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/orders/8000000001'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/stock_options/orders/8000000001"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "order_id": "8000000001",
        "symbol": "AAPL260814P00130000",
        "symbol_display": "AAPL-260814-130-P",
        "underlying": "AAPL",
        "side": 2,
        "order_type": "limit",
        "status": 3,
        "status_desc": "filled",
        "time_in_force": "day",
        "quantity": "1",
        "filled_quantity": "1",
        "price": "1.20",
        "avg_fill_price": "1.20",
        "fee": "0.025",
        "time_setup": 1785919118,
        "time_done": 1785919120
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  Amend an option limit order🔒 Authenticated

PUT`/stock_options/orders/{order_id}`

PUT `/stock_options/orders/{order_id}`

_Amend an option limit order_

Update the price and total quantity of one of the current user's option limit orders. The path `order_id` and body `price` and `quantity` are required. Market orders cannot be amended. `quantity` is the new total order quantity, not the remaining unfilled quantity, and must be at least `filled_quantity`. Amending a sell order also requires sufficient available positions for the new unfilled quantity. Returns the order ID; query the order for its subsequent status.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | Option order ID as a positive integer string, obtained from order submission or query results.  
body | body | StockOptionUpdateOrderRequest | Required | none  
price | body | string | Required | New limit price, required, as a positive plain decimal string up to 64 characters, without scientific notation.  
quantity | body | string | Required | New total order quantity as a positive decimal string, not the remaining unfilled quantity. Must be at least filled_quantity.  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
StockOptionUpdateOrderRequest | required: ["price","quantity"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | New limit price, required, as a positive plain decimal string up to 64 characters, without scientific notation.  
quantity | string | Required |  | New total order quantity as a positive decimal string, not the remaining unfilled quantity. Must be at least filled_quantity.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order amendment response | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionUpdateOrderResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/orders/72057594037983901'
    query_param = ''
    body='{"price":"1.25","quantity":"2"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('PUT', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('PUT', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="PUT"
    url="/stock_options/orders/72057594037983901"
    query_param=""
    body_param='{"price":"1.25","quantity":"2"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "price": "1.25",
      "quantity": "2"
    }
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "id": "8000000001"
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  Cancel an option limit order🔒 Authenticated

DELETE`/stock_options/orders/{order_id}`

DELETE `/stock_options/orders/{order_id}`

_Cancel an option limit order_

Cancel one of the current user's option limit orders by ID. `order_id` is required. Only limit orders can be cancelled; already filled quantities are unaffected. Returns the order ID. Query order details or order history for the final status.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | Option order ID as a positive integer string, obtained from order submission or query results.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order cancellation response | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionCancelOrderResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/orders/72057594037983901'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/stock_options/orders/72057594037983901"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "id": "8000000001"
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  List historical option orders🔒 Authenticated

GET`/stock_options/orders/history`

GET `/stock_options/orders/history`

_List historical option orders_

Query the current user's finished option orders with pagination to check orders, fills and fees. `status` includes only 3 (filled), 4 (cancelled) and 5 (rejected). Filter by underlying, contract, side or order creation time. `begin_time` and `end_time` are Unix timestamps in seconds; when both are provided, the start must not be later than the end. Returns total records, total pages and the current page. The default and maximum `page_size` are both 100.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Optional | Option underlying symbol, for example AAPL. Omit to disable underlying filtering. Current orders support only one underlying.  
symbol | query | string | Optional | Full option contract symbol, for example AAPL260814P00130000. Omit to disable contract filtering.  
begin_time | query | integer(int64) | Optional | Order creation time filter start, as a Unix timestamp in seconds. Omit for no lower bound; must not exceed end_time when both are provided.  
end_time | query | integer(int64) | Optional | Order creation time filter end, as a Unix timestamp in seconds. Omit for no upper bound; must not precede begin_time when both are provided.  
side | query | StockOptionOrderListSide | Optional | Order side filter.  
Omit to query both sides.  
\- 1: Sell orders only.  
\- 2: Buy orders only.  
page | query | integer | Optional | Page number, starting from 1. Defaults to 1 when omitted.  
page_size | query | integer | Optional | Number of items per page, up to 100. Defaults to 100 when omitted; values above 100 are capped at 100.  
  
####  Detailed descriptions

**side** : Order side filter.  
Omit to query both sides.  
\- 1: Sell orders only.  
\- 2: Buy orders only.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | 1  
side | 2  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Historical option order list | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | StockOptionApiResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
StockOptionOrderHistoryResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total number of matching records.  
total_page | integer | Optional |  | Total number of pages.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Finished orders, including only filled, cancelled and rejected terminal orders.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID.  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
side | integer | Optional | enum: [1,2] | Order side.  
\- 1: Sell.  
\- 2: Buy.  
order_type | string | Optional | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
status | integer | Optional | enum: [3,4,5] | Historical order status:  
\- 3: Filled.  
\- 4: Cancelled; the order may have been partially filled.  
\- 5: Rejected.  
status_desc | string | Optional |  | Human-readable order status description in the requested language.  
time_in_force | string | Optional | enum: ["day","gtc"] | Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.  
quantity | string | Optional |  | Order quantity.  
filled_quantity | string | Optional |  | Filled quantity.  
price | string | Optional |  | Order price.  
time_setup | integer(int64) | Optional |  | Order creation time.  
avg_fill_price | string | Optional |  | Average fill price.  
fee | string | Optional |  | Trading fee.  
time_done | integer(int64) | Optional |  | Order completion time.  
  
Status Code **400**

Type | Constraints  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/orders/history'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/stock_options/orders/history"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "label": "",
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "order_id": "8000000001",
            "symbol": "AAPL260814P00130000",
            "symbol_display": "AAPL-260814-130-P",
            "underlying": "AAPL",
            "side": 2,
            "order_type": "limit",
            "status": 3,
            "status_desc": "filled",
            "time_in_force": "day",
            "quantity": "1",
            "filled_quantity": "1",
            "price": "1.20",
            "avg_fill_price": "1.20",
            "fee": "0.025",
            "time_setup": 1785919118,
            "time_done": 1785919120
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

#  Schemas

##  StockOptionOrderHistoryResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total number of matching records.  
total_page | integer | Optional |  | Total number of pages.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Finished orders, including only filled, cancelled and rejected terminal orders.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID.  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
side | integer | Optional | enum: [1,2] | Order side.  
\- 1: Sell.  
\- 2: Buy.  
order_type | string | Optional | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
status | integer | Optional | enum: [3,4,5] | Historical order status:  
\- 3: Filled.  
\- 4: Cancelled; the order may have been partially filled.  
\- 5: Rejected.  
status_desc | string | Optional |  | Human-readable order status description in the requested language.  
time_in_force | string | Optional | enum: ["day","gtc"] | Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.  
quantity | string | Optional |  | Order quantity.  
filled_quantity | string | Optional |  | Filled quantity.  
price | string | Optional |  | Order price.  
time_setup | integer(int64) | Optional |  | Order creation time.  
avg_fill_price | string | Optional |  | Average fill price.  
fee | string | Optional |  | Trading fee.  
time_done | integer(int64) | Optional |  | Order completion time.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionPositionPnlPriceType

Price type for position PnL.

  * latest: Last traded price; used when omitted or empty.
  * mark: Mark price.

Type | Constraints  
---|---  
string | default: "latest"  
  
**Enumerated Values**

Value  
---  
"latest"  
"mark"  
      
    
    "latest"
    
    

##  StockOptionOptionType

Option type.

  * call: Call option.
  * put: Put option.

Type | Constraints  
---|---  
string |   
  
**Enumerated Values**

Value  
---  
"call"  
"put"  
      
    
    "call"
    
    

##  StockOptionOrderBookResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
bids | array | Optional |  | Bid prices; at most one level, or an empty array when no quote is available.  
asks | array | Optional |  | Ask prices; at most one level, or an empty array when no quote is available.  
  
**allOf[1] / data / bids**

Bid prices; at most one level, or an empty array when no quote is available.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / bids / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Optional |  | Quoted price.  
  
**allOf[1] / data / asks**

Ask prices; at most one level, or an empty array when no quote is available.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / asks / items**

Type | Constraints  
---|---  
object |   
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "symbol": "string",
        "symbol_display": "string",
        "bids": [
          {}
        ],
        "asks": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionCancelAllOrdersRequest

Filters for cancelling limit orders in bulk. side is 1 (sell) or 2 (buy); omit it to include both sides.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
underlying | string | Optional |  | Option underlying symbol. Empty or omitted values disable underlying filtering.  
symbol | string | Optional |  | Option contract symbol. Empty or omitted values disable contract filtering.  
side | integer | Optional | enum: [1,2] | Order side filter.  
Omit to query both sides.  
\- 1: Sell orders only.  
\- 2: Buy orders only.  
      
    
    {
      "underlying": "AAPL",
      "symbol": "string",
      "side": 1
    }
    
    

##  StockOptionOptionChainResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
underlying | string | Optional |  | Option underlying symbol.  
expiration_date | string(date) | Optional |  | Option expiration date in YYYY-MM-DD format.  
expiration_date_ts | integer(int64) | Optional |  | Unix timestamp of the expiration date.  
index_price | string | Optional |  | Underlying index price; empty when no valid value is available.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
strike_price | string | Optional |  | Strike price.  
option_type | string | Optional | enum: ["call","put"] | Option type.  
\- call: Call option.  
\- put: Put option.  
bid | string | Optional |  | Best bid price.  
ask | string | Optional |  | Best ask price.  
mark_price | string | Optional |  | Mark price.  
mark_iv | string | Optional |  | Mark implied volatility.  
last | string | Optional |  | Last traded price.  
display_price | string | Optional |  | Display price.  
breakeven_price | string | Optional |  | Breakeven price.  
to_breakeven_pct | string | Optional |  | Percentage distance to the breakeven price.  
today_change_pct | string | Optional |  | Price change percentage today.  
open_interest | string | Optional |  | Open interest.  
position | string | Optional |  | Position quantity.  
delta | string | Optional |  | Option delta.  
gamma | string | Optional |  | Option gamma.  
theta | string | Optional |  | Option theta.  
vega | string | Optional |  | Option vega.  
rho | string | Optional |  | Option rho.  
trade_status | string | Optional | enum: ["open","closed"] | Current contract trading status.  
\- open: Within trading hours, with both the contract and underlying tradable.  
\- closed: Not tradable, including outside trading hours, an inactive contract or a disabled underlying.  
trade_mode | integer | Optional | enum: [0,4] | Current trading mode.  
\- 0: Trading disabled.  
\- 4: Buying and selling allowed; regular accounts still require sufficient available long positions to sell.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "underlying": "string",
        "expiration_date": "2026-11-20",
        "expiration_date_ts": 0,
        "index_price": "string",
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionOrderListResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Current unfinished orders, excluding filled, cancelled and rejected terminal orders.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID.  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
side | integer | Optional | enum: [1,2] | Order side.  
\- 1: Sell.  
\- 2: Buy.  
order_type | string | Optional | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
status | integer | Optional | enum: [1,2] | Current order status:  
\- 1: New, validated and awaiting processing.  
\- 2: Partially filled, with a remaining unfilled quantity.  
status_desc | string | Optional |  | Human-readable order status description in the requested language.  
time_in_force | string | Optional | enum: ["day","gtc"] | Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.  
quantity | string | Optional |  | Order quantity.  
filled_quantity | string | Optional |  | Filled quantity.  
price | string | Optional |  | Order price.  
time_setup | integer(int64) | Optional |  | Order creation time.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionApiResponse

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Required |  | Business error label. Empty on successful requests.  
message | string | Optional |  | Error message. Omitted on successful requests.  
data | any|null | Required | nullable: true | Business response data.  
timestamp | integer(int64) | Required |  | Server timestamp in milliseconds.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1785919118845
    }
    
    

##  StockOptionClosePositionResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "order_id": "string"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionSymbolListResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
underlying | string | Optional |  | Option underlying symbol.  
description | string | Optional |  | Underlying description.  
descs | array | Optional |  | Underlying descriptions in multiple languages.  
icon_link | string | Optional |  | Underlying icon URL.  
price_precision | integer | Optional |  | Number of decimal places for prices.  
min_order_volume | string | Optional |  | Minimum order quantity.  
max_order_volume | string | Optional |  | Maximum order quantity.  
step_order_volume | string | Optional |  | Order quantity increment.  
  
**allOf[1] / data / list / items / descs**

Underlying descriptions in multiple languages.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items / descs / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
lang | string | Optional |  | Language code.  
value | string | Optional |  | Underlying description in this language.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionConfigResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
sec | string | Optional |  | SEC fee rate.  
min_sec | string | Optional |  | Minimum SEC fee.  
max_sec | string | Optional |  | Maximum SEC fee; empty means no limit.  
taf | string | Optional |  | TAF fee rate.  
min_taf | string | Optional |  | Minimum TAF fee.  
max_taf | string | Optional |  | Maximum TAF fee.  
occ | string | Optional |  | OCC fee.  
orf | string | Optional |  | ORF fee.  
cat | string | Optional |  | CAT fee.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "sec": "0.0000206",
        "min_sec": "0.01",
        "max_sec": "",
        "taf": "0.00279",
        "min_taf": "0.01",
        "max_taf": "9.79",
        "occ": "0.025",
        "orf": "0.012",
        "cat": "0.0003"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionPositionListResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
today_pnl | string | Optional |  | Total daily option PnL = sum of today_pnl for current positions + daily PnL for contracts fully closed today.  
The valuation price for current positions is selected by the request parameter `price_type`.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
side | string | Optional | enum: ["long","short"] | Position side.  
\- long: Long position.  
\- short: Short position.  
open_time | integer(int64) | Optional |  | Position opening time as a Unix timestamp in seconds; 0 when unavailable.  
quantity | string | Optional |  | Position quantity.  
available | string | Optional |  | Available quantity; currently equal to quantity.  
frozen | string | Optional |  | Frozen quantity; may be empty when not calculated separately.  
avg_entry_price | string | Optional |  | Average entry price.  
last_price | string | Optional |  | Last traded price; 0 when no valid value is available.  
mark_price | string | Optional |  | Mark price; 0 when no valid value is available.  
previous_close | string | Optional |  | Previous closing price.  
If no valid positive value exists, this field may be empty and daily PnL calculation is skipped.  
market_value | string | Optional |  | Market value = valuation price × signed position quantity × contract multiplier.  
The valuation price is selected by `price_type` (`latest` uses last_price; `mark` uses mark_price).  
unrealized_pnl | string | Optional |  | Unrealized PnL = (valuation price - average entry price) × signed position quantity × contract multiplier.  
Returns 0 if the average entry price or quantity is invalid. The valuation price follows the same rules as market_value.  
today_pnl | string | Optional |  | Daily PnL for this contract. Requires a valid previous_close; 0 if unavailable.  
The valuation price follows the same rules as market_value.  
today_buy_qty | string | Optional |  | Quantity bought today (user's daily trading totals).  
today_sell_qty | string | Optional |  | Quantity sold today (user's daily trading totals).  
today_buy_value | string | Optional |  | Amount bought today (user's daily trading totals).  
today_sell_value | string | Optional |  | Amount sold today (user's daily trading totals).  
trade_status | string | Optional | enum: ["open","closed"] | Current contract trading status.  
\- open: Within trading hours, with both the contract and underlying tradable.  
\- closed: Not tradable, including outside trading hours, an inactive contract or a disabled underlying.  
trade_mode | integer | Optional | enum: [0,4] | Current trading mode.  
\- 0: Trading disabled.  
\- 4: Buying and selling allowed; regular accounts still require sufficient available long positions to sell.  
multiplier | string | Optional |  | Contract multiplier.  
price_precision | integer | Optional |  | Number of decimal places for prices.  
min_order_volume | string | Optional |  | Minimum order quantity.  
max_order_volume | string | Optional |  | Maximum order quantity.  
step_order_volume | string | Optional |  | Order quantity increment.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "today_pnl": "68.50",
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionContractListResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total number of matching records.  
total_page | integer | Optional |  | Total number of pages.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
exchange | string | Optional |  | Trading market.  
expiration_date | string(date) | Optional |  | Option expiration date in YYYY-MM-DD format.  
settlement_date | string(date) | Optional |  | Option settlement date in YYYY-MM-DD format.  
strike_price | string | Optional |  | Strike price.  
option_type | string | Optional | enum: ["call","put"] | Option type.  
\- call: Call option.  
\- put: Put option.  
multiplier | string | Optional |  | Contract multiplier.  
open_interest | string | Optional |  | Open interest.  
quote_currency | string | Optional |  | Quote currency.  
settlement_type | string | Optional |  | Settlement type.  
trade_status | string | Optional | enum: ["open","closed"] | Current contract trading status.  
\- open: Within trading hours, with both the contract and underlying tradable.  
\- closed: Not tradable, including outside trading hours, an inactive contract or a disabled underlying.  
trade_mode | integer | Optional | enum: [0,4] | Current trading mode.  
\- 0: Trading disabled.  
\- 4: Buying and selling allowed; regular accounts still require sufficient available long positions to sell.  
price_precision | integer | Optional |  | Number of decimal places for prices.  
min_order_volume | string | Optional |  | Minimum order quantity.  
max_order_volume | string | Optional |  | Maximum order quantity.  
step_order_volume | string | Optional |  | Order quantity increment.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionCancelAllOrdersResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
success | boolean | Optional |  | Whether the cancellation request succeeded.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "success": true
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionClosePositionRequest

`order_type` is optional. Omitted or empty values close at market; only `market` and `limit` are supported.

Type | Constraints  
---|---  
object | required: ["symbol","quantity"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Option contract symbol to close, with an available position.  
quantity | string | Required |  | Quantity to close as a positive decimal string. Must not exceed the available position and must satisfy the contract's minimum, maximum and quantity increment rules.  
order_type | string | Optional | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
price | string | Optional |  | Positive limit closing price as a plain decimal string, up to 64 characters, without scientific notation. Ignored for market closing orders.  
client_order_id | string | Optional |  | Custom closing order identifier. Generated automatically when omitted or whitespace-only.  
      
    
    {
      "symbol": "string",
      "quantity": "string",
      "order_type": "market",
      "price": "1.00",
      "client_order_id": "string"
    }
    
    

##  StockOptionOrderDetailResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  | Order details for a current or finished order.  
  
**allOf[1] / data**

Order details for a current or finished order.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID.  
symbol | string | Optional |  | Full option contract symbol.  
symbol_display | string | Optional |  | Option contract name for display.  
underlying | string | Optional |  | Option underlying symbol.  
side | integer | Optional | enum: [1,2] | Order side.  
\- 1: Sell.  
\- 2: Buy.  
order_type | string | Optional | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
status | integer | Optional |  | Order status in order details. The details endpoint does not filter by status.  
\- 1: New, validated and awaiting processing.  
\- 2: Partially filled, with a remaining unfilled quantity.  
\- 3: Filled, terminal.  
\- 4: Cancelled, terminal; the order may have been partially filled.  
\- 5: Rejected, terminal.  
Current orders include only 1 and 2; order history includes only 3, 4 and 5.  
status_desc | string | Optional |  | Human-readable order status description in the requested language.  
time_in_force | string | Optional | enum: ["day","gtc"] | Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.  
quantity | string | Optional |  | Order quantity.  
filled_quantity | string | Optional |  | Filled quantity.  
price | string | Optional |  | Order price.  
time_setup | integer(int64) | Optional |  | Order creation time.  
avg_fill_price | string | Optional |  | Average fill price.  
fee | string | Optional |  | Trading fee.  
time_done | integer(int64) | Optional |  | Order completion time.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "order_id": "string",
        "symbol": "string",
        "symbol_display": "string",
        "underlying": "string",
        "side": 1,
        "order_type": "market",
        "status": 0,
        "status_desc": "string",
        "time_in_force": "day",
        "quantity": "string",
        "filled_quantity": "string",
        "price": "string",
        "time_setup": 0,
        "avg_fill_price": "string",
        "fee": "string",
        "time_done": 0
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionCancelOrderResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "id": "string"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionOrderListSide

Order side filter. Omit to query both sides.

  * 1: Sell orders only.
  * 2: Buy orders only.

Type | Constraints  
---|---  
integer |   
  
**Enumerated Values**

Value  
---  
1  
2  
      
    
    1
    
    

##  StockOptionPutOrderResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "id": "string"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionUpdateOrderResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "id": "string"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionUpdateOrderRequest

Type | Constraints  
---|---  
object | required: ["price","quantity"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | New limit price, required, as a positive plain decimal string up to 64 characters, without scientific notation.  
quantity | string | Required |  | New total order quantity as a positive decimal string, not the remaining unfilled quantity. Must be at least filled_quantity.  
      
    
    {
      "price": "1.25",
      "quantity": "2"
    }
    
    

##  StockOptionPutOrderRequest

Type | Constraints  
---|---  
object | required: ["symbol","side","order_type","time_in_force","quantity"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Full option contract symbol to trade, obtained from the contract list or option chain.  
side | integer | Required | enum: [1,2] | Order side.  
\- 1: Sell.  
\- 2: Buy.  
order_type | string | Required | enum: ["market","limit"] | Order type.  
\- market: Market order, executed at available market prices.  
\- limit: Limit order, requiring price.  
time_in_force | string | Required | enum: ["day","gtc"] | Time in force. Limit orders support day and gtc; market orders support only day.  
\- day: Valid for the day; the unfilled portion is cancelled when that day's validity period ends.  
\- gtc: Good until cancelled.  
Closing orders always use day.  
price | string | Optional |  | Limit order price as a positive plain decimal string, up to 64 characters, without scientific notation. Required for limit orders and ignored for market orders.  
quantity | string | Required |  | Order quantity as a positive decimal string within the contract's minimum and maximum order quantities.  
client_order_id | string | Optional | maxLength: 30 | Optional custom order identifier, up to 30 UTF-8 bytes. Generated automatically when omitted or whitespace-only.  
      
    
    {
      "symbol": "AAPL260814P00130000",
      "side": 1,
      "order_type": "market",
      "time_in_force": "day",
      "price": "1.00",
      "quantity": "1",
      "client_order_id": "string"
    }
    
    

##  StockOptionExpirationListResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
underlying | string | Optional |  | Option underlying symbol.  
list | array | Optional |  | List of query results.  
  
**allOf[1] / data / list**

List of query results.

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
expiration_date | string(date) | Optional |  | Option expiration date in YYYY-MM-DD format.  
expiration_date_ts | integer(int64) | Optional |  | Unix timestamp of the expiration date.  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "underlying": "string",
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }