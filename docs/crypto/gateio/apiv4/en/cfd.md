---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/cfd
api_type: REST
updated_at: 2026-11-19 19:00:36.388670
---

# CFD

CFD is a contracts-for-difference trading business that provides MT5-based forex and CFD trading services. The CFD API provides complete user management, asset query, order management, position management, and market data query capabilities.

  * REST API BaseURL for live trading: `https://api.gateio.ws/api/v4/`
  * [Help Center ](https://www.gate.com/help/tradfi/functional)
  * [CFD Trading ](https://www.gate.com/tradfi)
  * Before using this business API, make sure the user has enabled CFD business. You can call the create CFD user endpoint or log in to the app to enable it
  * For lead trading via APIv4, add the request header `x-gate-trader-copy-type: cfd_copy`. This does not apply to CFD user activation or fund transfer endpoints.

##  Query MT5 account information🔒 Authenticated

GET`/tradfi/users/mt5-account`

GET `/tradfi/users/mt5-account`

_Query MT5 account information_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | Mt5Account  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
Mt5Account |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Optional |  | Business Status Code; Non-zero Indicates Business Exception, Please Check Message  
message | string | Optional |  | Response message  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
leverage | integer | Optional |  | Leverage multiplier  
stop_out_level | string | Optional |  | Liquidation margin ratio  
status | integer | Optional |  | Account status (1=not opened, 2=pending review, 3=active)  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/users/mt5-account'
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
    url="/tradfi/users/mt5-account"
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
      "data": {
        "leverage": 0,
        "stop_out_level": "",
        "status": 1
      },
      "timestamp": 1769426795464
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query trading symbol categories

GET`/tradfi/symbols/categories`

GET `/tradfi/symbols/categories`

_Query trading symbol categories_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | Categories  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
Categories |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Data  
  
**data**

Data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  |   
  
**data / list**

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Category information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
category_id | integer | Optional |  | Category ID  
is_favorite | boolean | Optional |  | Whether it is a custom category, generally no need to pay attention  
category_name | string | Optional |  | Category name  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/tradfi/symbols/categories'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/tradfi/symbols/categories \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "list": [
          {
            "category_id": 1,
            "is_favorite": false,
            "category_name": "金属"
          },
          {
            "category_id": 2,
            "is_favorite": false,
            "category_name": "Stocks"
          },
          {
            "category_id": 4,
            "is_favorite": false,
            "category_name": "指数"
          },
          {
            "category_id": 5,
            "is_favorite": false,
            "category_name": "外汇"
          },
          {
            "category_id": 6,
            "is_favorite": false,
            "category_name": "大宗商品"
          }
        ]
      },
      "timestamp": 1769398039786
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query symbol commission rates🔒 Authenticated

GET`/tradfi/symbols/commissions`

GET `/tradfi/symbols/commissions`

_Query symbol commission rates_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Optional | Comma-separated instrument symbols. Provide at least one of symbols and category_code.  
category_code | query | string | Optional | List of category codes (multiple codes separated by commas). When provided together with symbols, filters symbols by category. At least one of symbol and category_code is required  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | SymbolCommissions  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
SymbolCommissions |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | List of symbol commission rates  
  
**data / list**

List of symbol commission rates

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Symbol commission rate

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
category_code | string | Optional |  | Category code  
symbol | string | Optional |  | Trading symbol code  
fee_per_lot | string | Optional |  | Commission rate per lot  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/symbols/commissions'
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
    url="/tradfi/symbols/commissions"
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
      "data": {
        "list": [
          {
            "category_code": "forex",
            "symbol": "AUDUSD",
            "fee_per_lot": "6"
          },
          {
            "category_code": "metal",
            "symbol": "XAUUSD",
            "fee_per_lot": "6"
          }
        ]
      },
      "timestamp": 1769426795464
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query trading symbol list

GET`/tradfi/symbols`

GET `/tradfi/symbols`

_Query trading symbol list_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | Symbols  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
Symbols |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Trading symbol list  
  
**data / list**

Trading symbol list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Trading symbol information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Trading symbol code  
symbol_desc | string | Optional |  | Trading symbol description  
category_id | integer | Optional |  | Category ID  
status | string | Optional |  | Trading status (open=tradable, closed=non-tradable)  
trade_mode | string | Optional |  | Trading mode code (0=disabled, 1=long only, 2=short only, 3=close only, 4=full trading access)  
icon_link | string | Optional |  | Symbol icon URL  
close_time | integer(int64) | Optional |  | Close time (Unix timestamp in seconds)  
open_time | integer(int64) | Optional |  | Open time (Unix timestamp in seconds)  
next_open_time | integer(int64) | Optional |  | Next open time (Unix timestamp in seconds, 0 means none)  
settlement_currency | string | Optional |  | Settlement currency  
settlement_currency_symbol | string | Optional |  | Settlement currency symbol  
price_precision | integer | Optional |  | Price precision (decimal places)  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/tradfi/symbols'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/tradfi/symbols \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "list": [
          {
            "symbol": "EURUSD",
            "symbol_desc": "Euro vs United States Dollar",
            "category_id": 6,
            "status": "open",
            "trade_mode": "4",
            "icon_link": "https://gimg.staticimgs.com/image/eurusd_20260123_120701_3982593a8387f849b5eb60a05bbadd3c.png",
            "close_time": 1769464800,
            "open_time": 1769378400,
            "next_open_time": 0,
            "settlement_currency": "USD",
            "settlement_currency_symbol": "$",
            "price_precision": 8
          },
          {
            "symbol": "XAGUSD",
            "symbol_desc": "Silver vs US Dollar / Spot",
            "category_id": 1,
            "status": "open",
            "trade_mode": "4",
            "icon_link": "https://gimg.staticimgs.com/image/xagusd_20260115_162831_6d2429db5ad657da37d139eb33e4a324.png",
            "close_time": 1769464800,
            "open_time": 1769378400,
            "next_open_time": 0,
            "settlement_currency": "USD",
            "settlement_currency_symbol": "$",
            "price_precision": 3
          }
        ]
      },
      "timestamp": 1769426795464
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query trading symbol details🔒 Authenticated

GET`/tradfi/symbols/detail`

GET `/tradfi/symbols/detail`

_Query trading symbol details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Required | Trading symbol code list (comma-separated, max 10 symbols)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | ContractDetail  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
ContractDetail |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Contract Details List  
  
**data / list**

Contract Details List

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Futures contract details

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Trading symbol code  
symbol_desc | string | Optional |  | Trading symbol description  
category_name | string | Optional |  | Category name  
contract_volume | string | Optional |  | Contract Volume  
settlement_currency | string | Optional |  | Settle currency  
max_order_volume | string | Optional |  | Maximum Order Volume  
min_order_volume | string | Optional |  | Minimum Order Volume  
leverage | string | Optional |  | Leverage multiplier  
price_precision | integer | Optional |  | Price precision (decimal places)  
price_sl_level | string | Optional |  | Stop Loss Price Level  
swap_cost_type | string | Optional |  | Swap Cost Type  
buy_swap_cost_rate | string | Optional |  | Buy Swap Cost Rate  
sell_swap_cost_rate | string | Optional |  | Sell Swap Cost Rate  
swap_cost_3day | string | Optional |  | 3-Day Swap Cost  
trade_timezone | string | Optional |  | Trading Timezone  
trade_mode | string | Optional |  | Trading mode code (0=disabled, 1=long only, 2=short only, 3=close only, 4=full trading access)  
icon_link | string | Optional |  | Symbol icon URL  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/symbols/detail'
    query_param = 'symbols=EURUSD,XAGUSD'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/tradfi/symbols/detail"
    query_param="symbols=EURUSD,XAGUSD"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "list": [
          {
            "symbol": "PLNJPY",
            "symbol_desc": "掉期费-货币-预0",
            "category_name": "Forex",
            "contract_volume": "100000",
            "settlement_currency": "JPY",
            "max_order_volume": "100",
            "min_order_volume": "10",
            "leverage": "25",
            "price_precision": 4,
            "price_sl_level": "100.00",
            "swap_cost_type": "1",
            "buy_swap_cost_rate": "7.937347",
            "sell_swap_cost_rate": "-172.856426",
            "swap_cost_3day": "3",
            "trade_timezone": "GMT+2",
            "trade_mode": "4",
            "icon_link": ""
          }
        ]
      },
      "timestamp": 1769426795464
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query trading symbol klines

GET`/tradfi/symbols/{symbol}/klines`

GET `/tradfi/symbols/{symbol}/klines`

_Query trading symbol klines_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | path | string | Required | Trading symbol code  
kline_type | query | string | Required | Kline type (time period)  
begin_time | query | integer(int64) | Optional | Start time (Unix timestamp in seconds)  
end_time | query | integer(int64) | Optional | End time (Unix timestamp in seconds)  
limit | query | integer | Optional | Kline limit (max 500, error if exceeded)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
kline_type | 1m  
kline_type | 15m  
kline_type | 1h  
kline_type | 4h  
kline_type | 1d  
kline_type | 7d  
kline_type | 30d  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | Klines  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
Klines |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Kline data list  
  
**data / list**

Kline data list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Single kline data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
o | string | Optional |  | Open price  
c | string | Optional |  | Close price  
h | string | Optional |  | High price  
l | string | Optional |  | Low price  
t | integer(int64) | Optional |  | Timestamp (Unix seconds)  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/tradfi/symbols/EURUSD/klines'
    query_param = 'kline_type=1m'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/tradfi/symbols/EURUSD/klines?kline_type=1m \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1769398039786,
      "data": {
        "list": [
          {
            "o": "1.17198",
            "c": "1.17213",
            "h": "1.17268",
            "l": "1.1718",
            "t": 1755896400
          },
          {
            "o": "1.17208",
            "c": "1.16092",
            "h": "1.17263",
            "l": "1.16023",
            "t": 1756069200
          }
        ]
      }
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query trading symbol ticker

GET`/tradfi/symbols/{symbol}/tickers`

GET `/tradfi/symbols/{symbol}/tickers`

_Query trading symbol ticker_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | path | string | Required | Trading symbol code  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradFiTicker  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

TradFiTicker

Ticker summary information

Type | Constraints  
---|---  
TradFiTicker |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
highest_price | string | Optional |  | High price  
lowest_price | string | Optional |  | Low price  
price_change | string | Optional |  | Price change percentage (multiplied by 100)  
price_change_amount | string | Optional |  | Price change amount  
today_open_price | string | Optional |  | Today's open price  
last_today_close_price | string | Optional |  | Previous close price  
last_price | string | Optional |  | Last trading price  
bid_price | string | Optional |  | Bid price  
ask_price | string | Optional |  | Ask price  
favorite | boolean | Optional |  | Is favorited  
status | string | Optional |  | Trading status (open=tradable, closed=non-tradable)  
close_time | integer(int64) | Optional |  | Close time (Unix timestamp in seconds)  
open_time | integer(int64) | Optional |  | Open time (Unix timestamp in seconds)  
next_open_time | integer(int64) | Optional |  | Next open time (0 means none)  
trade_mode | string | Optional |  | Trading mode code  
category_name | string | Optional |  | Category name  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/tradfi/symbols/EURUSD/tickers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/tradfi/symbols/EURUSD/tickers \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "highest_price": "5093.04",
        "lowest_price": "5003.61",
        "price_change": "1.32",
        "price_change_amount": "66.13",
        "today_open_price": "5008.06",
        "last_today_close_price": "4989.92",
        "last_price": "5074.19",
        "bid_price": "5073.83",
        "ask_price": "5074.06",
        "favorite": false,
        "status": "open",
        "close_time": 1769464800,
        "open_time": 1769378400,
        "next_open_time": 0,
        "trade_mode": "4",
        "category_name": "Metals"
      },
      "timestamp": 1769426795464
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Create CFD user🔒 Authenticated

POST`/tradfi/users`

POST `/tradfi/users`

_Create CFD user_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Account opened successfully | CreateUserResp  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
CreateUserResp |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
status | integer | Optional |  | Status (1=not opened, 2=pending review, 3=opened)  
leverage | integer | Optional |  | Leverage  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/users'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/tradfi/users"
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
      "data": {
        "leverage": 1,
        "status": 3
      },
      "timestamp": 1769398039786
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query account assets🔒 Authenticated

GET`/tradfi/users/assets`

GET `/tradfi/users/assets`

_Query account assets_

Query account assets

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | UserAssetResp  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
UserAssetResp |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
equity | string | Optional |  | Account equity  
margin_level | string | Optional |  | Margin level (percentage)  
balance | string | Optional |  | Account Balance  
margin | string | Optional |  | Used margin  
margin_free | string | Optional |  | Available Margin  
unrealized_pnl | string | Optional |  | Unrealized PNL  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/users/assets'
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
    url="/tradfi/users/assets"
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
      "timestamp": 1769426795464,
      "data": {
        "equity": "0.00",
        "margin_level": "0.00",
        "balance": "0.00",
        "margin": "0.00",
        "margin_free": "0.00",
        "unrealized_pnl": "0.00"
      }
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query Fund Transfer In/Out Records🔒 Authenticated

GET`/tradfi/transactions`

GET `/tradfi/transactions`

_Query Fund Transfer In/Out Records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
begin_time | query | integer(int64) | Optional | Start Time (Second-level Timestamp)  
end_time | query | integer(int64) | Optional | End Time (Second-level Timestamp)  
type | query | string | Optional | Transaction Type (deposit - transfer in, withdraw - transfer out, dividend - dividend payment, fill_negative - cover negative balance)  
page | query | integer | Optional | page number  
page_size | query | integer | Optional | Number per page, default 10, maximum 50  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | deposit  
type | withdraw  
type | dividend  
type | fill_negative  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TransactionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
TransactionList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer | Optional |  | Total Records  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  | Record List  
  
**data / list**

Record List

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Optional |  | Asset Type  
type | string | Optional | enum: ["deposit-转入","withdraw-转出","dividend-分红结息","fill_negative-填平负余额"] | Trading Type  
type_desc | string | Optional |  | Transaction Type Description  
change | string | Optional |  | Change amount  
balance | string | Optional |  | Current Balance  
time | integer(int64) | Optional |  | Occurrence Time (Second-level Timestamp)  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/transactions'
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
    url="/tradfi/transactions"
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
      "data": {
        "total": 2,
        "total_page": 1,
        "list": [
          {
            "asset": "USDT",
            "type": "dividend",
            "type_desc": "Dividend Adjustment",
            "change": "1",
            "balance": "1",
            "time": 1769329389
          },
          {
            "asset": "USDT",
            "type": "fill_negative",
            "type_desc": "填補損失",
            "change": "0.5",
            "balance": "0.5",
            "time": 1769238545
          }
        ]
      },
      "timestamp": 1769332996590
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Fund transfer🔒 Authenticated

POST`/tradfi/transactions`

POST `/tradfi/transactions`

_Fund transfer_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiTransactionRequest | Required | none  
asset | body | string | Required | Asset type, e.g., USDT, currently only USDT is supported  
change | body | string | Required | Change Quantity, supports up to two decimal places  
type | body | string | Required | Transaction Type (deposit - transfer in, withdraw - transfer out)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | deposit  
type | withdraw  
  
####  Request Body Schema

Fund Transfer Request Body

Request Body SchemaType | Constraints  
---|---  
TradFiTransactionRequest | required: ["asset","change","type"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Asset type, e.g., USDT, currently only USDT is supported  
change | string | Required |  | Change Quantity, supports up to two decimal places  
type | string | Required | enum: ["deposit","withdraw"] | Transaction Type (deposit - transfer in, withdraw - transfer out)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | CreateTransaction  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
CreateTransaction |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  |   
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/transactions'
    query_param = ''
    body='{"asset":"USDT","change":"10","type":"withdraw"}'
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
    url="/tradfi/transactions"
    query_param=""
    body_param='{"asset":"USDT","change":"10","type":"withdraw"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "asset": "USDT",
      "change": "10",
      "type": "withdraw"
    }
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "total": 2,
        "total_page": 1,
        "list": [
          {
            "asset": "USDT",
            "type": "dividend",
            "type_desc": "Dividend Adjustment",
            "change": "1",
            "balance": "1",
            "time": 1769329389
          },
          {
            "asset": "USDT",
            "type": "fill_negative",
            "type_desc": "填補損失",
            "change": "0.5",
            "balance": "0.5",
            "time": 1769238545
          }
        ]
      },
      "timestamp": 1769332996590
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query active order list🔒 Authenticated

GET`/tradfi/orders`

GET `/tradfi/orders`

_Query active order list_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | OrderList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
OrderList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Order list  
  
**data / list**

Order list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Order detail

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
symbol | string | Optional |  | Currency pair  
symbol_desc | string | Optional |  | Symbol description  
price_type | string | Optional | enum: ["market","trigger"] | Trade type (market=market price, trigger=trigger price)  
state | integer | Optional |  | Order status code  
state_desc | string | Optional |  | Order status description  
finished | integer | Optional | enum: [0,1] | Is completed (0=shown in active order list, 1=not shown in active list)  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
volume | string | Optional |  | Order quantity  
price | string | Optional |  | Trigger price  
price_tp | string | Optional |  | Take profit price  
price_sl | string | Optional |  | Stop loss price  
time_setup | integer(int64) | Optional |  | Order time (Unix timestamp in seconds)  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/orders'
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
    url="/tradfi/orders"
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
      "data": {
        "list": [
          {
            "order_id": 2630591,
            "symbol": "USDCHF",
            "symbol_desc": "US Dollar vs Swiss Franc",
            "price_type": "trigger",
            "state": 1,
            "state_desc": "",
            "finished": 0,
            "side": 2,
            "volume": "1.6",
            "price": "5.000000",
            "price_tp": "5.200000",
            "price_sl": "4.800000",
            "time_setup": 1768741530
          },
          {
            "order_id": 2630590,
            "symbol": "USDCHF",
            "symbol_desc": "US Dollar vs Swiss Franc",
            "price_type": "trigger",
            "state": 1,
            "state_desc": "",
            "finished": 0,
            "side": 2,
            "volume": "1.6",
            "price": "5.000000",
            "price_tp": "5.100000",
            "price_sl": "4.900000",
            "time_setup": 1768741526
          }
        ],
        "timestamp": 1769426795464
      }
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Create order🔒 Authenticated

POST`/tradfi/orders`

POST `/tradfi/orders`

_Create order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiOrderRequest | Required | none  
price | body | string | Required | Order price  
price_type | body | string | Required | Price type (trigger=trigger price, market=market price)  
side | body | integer | Required | Side (1=sell, 2=buy)  
symbol | body | string | Required | Base trading symbol code  
volume | body | string | Required | Order quantity  
price_tp | body | string | Optional | Take profit price (optional)  
price_sl | body | string | Optional | Stop loss price (optional)  
leverage | body | integer | Optional | Leverage multiplier (must be one of the leverage multipliers allowed for the symbol in the trading symbol details response)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
price_type | trigger  
price_type | market  
side | 1  
side | 2  
  
####  Request Body Schema

Place order request parameters

Request Body SchemaType | Constraints  
---|---  
TradFiOrderRequest | required: ["price","price_type","side","symbol","volume"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Order price  
price_type | string | Required | enum: ["trigger","market"] | Price type (trigger=trigger price, market=market price)  
side | integer | Required | enum: [1,2] | Side (1=sell, 2=buy)  
symbol | string | Required |  | Base trading symbol code  
volume | string | Required |  | Order quantity  
price_tp | string | Optional |  | Take profit price (optional)  
price_sl | string | Optional |  | Stop loss price (optional)  
leverage | integer | Optional |  | Leverage multiplier (must be one of the leverage multipliers allowed for the symbol in the trading symbol details response)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order placed successfully | CreateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
CreateOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Order result  
  
**data**

Order result

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Queue Task ID (not order ID)  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/orders'
    query_param = ''
    body='{"price":"0.9","price_type":"trigger","side":2,"symbol":"EURUSD","volume":"10","price_tp":"1.5","price_sl":"0.8","leverage":500}'
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
    url="/tradfi/orders"
    query_param=""
    body_param='{"price":"0.9","price_type":"trigger","side":2,"symbol":"EURUSD","volume":"10","price_tp":"1.5","price_sl":"0.8","leverage":500}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "price": "0.9",
      "price_type": "trigger",
      "side": 2,
      "symbol": "EURUSD",
      "volume": "10",
      "price_tp": "1.5",
      "price_sl": "0.8",
      "leverage": 500
    }
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "id": "117"
      },
      "timestamp": 1769426795464
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Modify order🔒 Authenticated

PUT`/tradfi/orders/{order_id}`

PUT `/tradfi/orders/{order_id}`

_Modify order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiOrderUpdateRequest | Required | none  
price | body | string | Required | Price  
Description:  
\- Required  
price_tp | body | string|null | Optional | Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface  
price_sl | body | string|null | Optional | Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface  
order_id | path | integer(int64) | Required | Order ID  
  
####  Detailed descriptions

** price**: Price  
Description:  
\- Required

** price_tp**: Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface

** price_sl**: Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface

####  Request Body Schema

Modify order price and take profit/stop loss parameters

Request Body SchemaType | Constraints  
---|---  
TradFiOrderUpdateRequest | required: ["price"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Price  
Description:  
\- Required  
price_tp | string|null | Optional | nullable: true | Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface  
price_sl | string|null | Optional | nullable: true | Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | UpdateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Order modification result

Type | Constraints  
---|---  
UpdateOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional | required: ["order_id","symbol","state","volume","price","price_tp","price_sl"] | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object | required: ["order_id","symbol","state","volume","price","price_tp","price_sl"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Required |  | Order ID  
symbol | string | Required |  | Currency pair  
state | string | Required |  | Order status code  
volume | string | Required |  | Order quantity  
price | string | Required |  | Current price  
price_tp | string | Required |  | Current take profit price  
price_sl | string | Required |  | Current stop loss price  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/orders/1223'
    query_param = ''
    body='{"price":"2","price_tp":"1.5","price_sl":"0.8"}'
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
    url="/tradfi/orders/1223"
    query_param=""
    body_param='{"price":"2","price_tp":"1.5","price_sl":"0.8"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "price": "2",
      "price_tp": "1.5",
      "price_sl": "0.8"
    }
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "order_id": 2651172,
        "symbol": "AUDUSD",
        "state": "1",
        "volume": "1",
        "price": "2.00000",
        "price_tp": "1.50000",
        "price_sl": "0.80000"
      },
      "timestamp": 1769956396273
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Cancel order🔒 Authenticated

DELETE`/tradfi/orders/{order_id}`

DELETE `/tradfi/orders/{order_id}`

_Cancel order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | integer(int64) | Required | Order ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Deleted successfully | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Returns empty object on success

Type | Constraints  
---|---  
object | additionalProperties: false  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/orders/1223'
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
    url="/tradfi/orders/1223"
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
    
    
    {}
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query historical order list🔒 Authenticated

GET`/tradfi/orders/history`

GET `/tradfi/orders/history`

_Query historical order list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
begin_time | query | integer(int64) | Optional | Start time (Unix timestamp in seconds), earliest query is one month ago  
end_time | query | integer(int64) | Optional | End time (Unix timestamp in seconds)  
symbol | query | string | Optional | Currency pair  
side | query | integer | Optional | Side (1=sell, 2=buy)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | 1  
side | 2  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | OrderHistoryList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
OrderHistoryList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Historical order list  
  
**data / list**

Historical order list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Order detail

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
symbol | string | Optional |  | Currency pair  
symbol_desc | string | Optional |  | Symbol description  
price_type | string | Optional | enum: ["market","trigger"] | Trade type (market=market price, trigger=trigger price)  
order_opt_type | integer | Optional | enum: [1,2,3,4,5,6] | Order operation type (1=sell, 2=buy, 3=close long, 4=close short, 5=force close long, 6=force close short)  
state | integer | Optional |  | Order status code  
state_desc | string | Optional |  | Order status description  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
volume | string | Optional |  | Order quantity  
fill_volume | string | Optional |  | Trading size  
close_pnl | string | Optional |  | Close Position P&L  
price | string | Optional |  | Average fill price  
trigger_price | string | Optional |  | Trigger price  
price_tp | string | Optional |  | Take profit price  
price_sl | string | Optional |  | Stop loss price  
time_setup | integer(int64) | Optional |  | Order time (Unix timestamp in seconds)  
time_done | integer(int64) | Optional |  | End time (Unix timestamp in seconds)  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/orders/history'
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
    url="/tradfi/orders/history"
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
      "data": {
        "list": [
          {
            "order_id": 2648991,
            "symbol": "USDCAD",
            "symbol_desc": "USD VS CAD;",
            "price_type": "market",
            "order_opt_type": 4,
            "state": 4,
            "state_desc": "Filled",
            "side": 2,
            "volume": "0.05",
            "fill_volume": "0.05",
            "close_pnl": "-1.49755",
            "price": "1.3689",
            "trigger_price": "1.3689",
            "price_tp": "0",
            "price_sl": "0",
            "time_setup": 1769397512,
            "time_done": 1769397512
          }
        ]
      }
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Get order details by log ID🔒 Authenticated

GET`/tradfi/orders/log/{log_id}`

GET `/tradfi/orders/log/{log_id}`

_Get order details by log ID_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
log_id | path | integer(int64) | Required | log_id returned from the order placement API  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | OrderLog  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
OrderLog |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
log_id | integer(int64) | Optional |  | logID  
symbol | string | Optional |  | Trading pair of the order  
price_type | string | Optional | enum: ["market","trigger"] | Trade type (market=market price, trigger=trigger price)  
state | integer | Optional |  | Order status code (1=placed, 2=canceled, 3=partially filled, 4=filled, 5=rejected)  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
volume | string | Optional |  | Order quantity  
price | string | Optional |  | Average fill price  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/orders/log/1223'
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
    url="/tradfi/orders/log/1223"
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
      "timestamp": 1715769600000,
      "data": {
        "order_id": 13950884,
        "log_id": 1214290,
        "symbol": "AUDUSD",
        "price_type": "market",
        "state": 4,
        "side": 2,
        "volume": "0.01",
        "price": "0.72221"
      }
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query active position list🔒 Authenticated

GET`/tradfi/positions`

GET `/tradfi/positions`

_Query active position list_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | PositionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
PositionList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Position information  
  
**data / list**

Position information

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Position information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
position_id | integer(int64) | Optional |  | Position ID  
symbol | string | Optional |  | Trading market code  
symbol_desc | string | Optional |  | Market description  
margin | string | Optional |  | Used margin  
unrealized_pnl | string | Optional |  | Unrealized PNL  
unrealized_pnl_rate | string | Optional |  | Unrealized return rate  
volume | string | Optional |  | Position size  
price_open | string | Optional |  | Average Opening Price  
position_dir | string | Optional |  | Position direction (Long=long position, Short=short position)  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/positions'
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
    url="/tradfi/positions"
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
      "data": {
        "list": [
          {
            "position_id": 2648925,
            "margin": "2.354440320000000142",
            "symbol": "EURUSD",
            "symbol_desc": "Euro vs United States Dollar",
            "unrealized_pnl": "8.06969999999992903440215741284191608428955078125",
            "unrealized_pnl_rate": "0.0068548775107622",
            "volume": "0.01",
            "price_open": "1.177220",
            "position_dir": "Long",
            "price_tp": "0.000000",
            "price_sl": "0.000000",
            "counterparty_price": "1.1851598599999999539278405791264958679676055908203125",
            "time_create": 1769319320
          }
        ],
        "timestamp": 1769426795464
      }
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Modify position🔒 Authenticated

PUT`/tradfi/positions/{position_id}`

PUT `/tradfi/positions/{position_id}`

_Modify position_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
position_id | path | integer(int64) | Required | Position ID  
body | body | TradFiPositionUpdateRequest | Required | none  
price_tp | body | string|null | Optional | Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface  
price_sl | body | string|null | Optional | Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface  
  
####  Detailed descriptions

** price_tp**: Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface

** price_sl**: Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface

####  Request Body Schema

Modify position take profit/stop loss parameters

Request Body SchemaType | Constraints  
---|---  
TradFiPositionUpdateRequest |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
price_tp | string|null | Optional | nullable: true | Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface  
price_sl | string|null | Optional | nullable: true | Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | UpdatePosition  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
UpdatePosition |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  |   
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/positions/1223'
    query_param = ''
    body='{"price_tp":"1","price_sl":"1"}'
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
    url="/tradfi/positions/1223"
    query_param=""
    body_param='{"price_tp":"1","price_sl":"1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "price_tp": "1",
      "price_sl": "1"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 0,
      "data": {}
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Close position🔒 Authenticated

POST`/tradfi/positions/{position_id}/close`

POST `/tradfi/positions/{position_id}/close`

_Close position_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
position_id | path | integer(int64) | Required | Position ID  
body | body | TradFiClosePositionRequest | Required | none  
close_type | body | integer | Required | Close Type  
Description:  
\- 1: Partial Close (close_volume is required)  
\- 2: Full Close (close_volume is not required)  
close_volume | body | string|null | Optional | Close Volume  
Description:  
\- Required when close_type = 1  
\- Ignored when close_type = 2  
  
####  Detailed descriptions

** close_type**: Close Type  
Description:  
\- 1: Partial Close (close_volume is required)  
\- 2: Full Close (close_volume is not required)

** close_volume**: Close Volume  
Description:  
\- Required when close_type = 1  
\- Ignored when close_type = 2

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
close_type | 1  
close_type | 2  
  
####  Request Body Schema

Close position request parameters

Request Body SchemaType | Constraints  
---|---  
TradFiClosePositionRequest | required: ["close_type"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
close_type | integer | Required | enum: [1,2] | Close Type  
Description:  
\- 1: Partial Close (close_volume is required)  
\- 2: Full Close (close_volume is not required)  
close_volume | string|null | Optional | nullable: true | Close Volume  
Description:  
\- Required when close_type = 1  
\- Ignored when close_type = 2  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | DeletePosition  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
DeletePosition |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  |   
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/positions/1223/close'
    query_param = ''
    body='{"close_type":1,"close_volume":"1"}'
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
    url="/tradfi/positions/1223/close"
    query_param=""
    body_param='{"close_type":1,"close_volume":"1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "close_type": 1,
      "close_volume": "1"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 0,
      "data": {}
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  Query historical position list🔒 Authenticated

GET`/tradfi/positions/history`

GET `/tradfi/positions/history`

_Query historical position list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page | query | integer(int64) | Optional | Page number; defaults to 1 if omitted.  
page_size | query | integer(int64) | Optional | Page size; defaults to 10 if omitted. Maximum 100.  
begin_time | query | integer(int64) | Optional | Start time as a Unix timestamp in seconds. The earliest supported start time is one month ago.  
end_time | query | integer(int64) | Optional | End time (timestamp in seconds)  
symbol | query | string | Optional | Trading symbol (e.g., EURUSD)  
position_dir | query | string | Optional | Position direction (Long=long position, Short=short position)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
position_dir | Long  
position_dir | Short  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | PositionHistoryList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
PositionHistoryList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer | Optional |  | Total amount  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  | Query historical position list  
  
**data / list**

Query historical position list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Position close history

Type | Constraints  
---|---  
object | required: ["position_id","symbol","realized_pnl","volume","volume_closed","price_open","position_dir","close_price","time_create","time_close","position_status","realized_pnl_detail"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
position_id | integer(int64) | Required |  | Position ID  
symbol | string | Required |  | Market / Trading symbol  
realized_pnl | string | Required |  | Realized PnL  
realized_pnl_rate | string | Optional |  | Realized return rate  
volume | string | Required |  | Position size / Maximum position size  
volume_closed | string | Required |  | Close volume  
price_open | string | Required |  | Average Opening Price  
position_dir | string | Required | enum: ["Long","Short"] | Position Direction  
\- Long: Long Position  
\- Short: Short Position  
price_tp | string | Optional |  | Take profit price  
price_sl | string | Optional |  | Stop loss price  
counterparty_price | string | Optional |  | Counterparty price  
close_price | string | Required |  | Close price  
time_create | string | Required |  | Open time (timestamp in seconds)  
time_close | string | Required |  | Close time (timestamp in seconds)  
position_status | string | Required |  | Position Status  
\- 1: Fully Closed  
\- 2: Forced Liquidation  
close_detail | object|null | Optional | nullable: true | Liquidation details (null for normal close)  
realized_pnl_detail | object | Required |  | Realized P&L details  
  
**data / list / items / close_detail**

Liquidation details (null for normal close)

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
margin_level | string | Optional |  | Margin ratio (multiplied by 100)  
margin | string | Optional |  | Margin  
equity | string | Optional |  | Net equity  
stop_out_level | string | Optional |  | Liquidation ratio (multiplied by 100)  
  
**data / list / items / realized_pnl_detail**

Realized P&L details

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
closed_pnl | string | Optional |  | Close Position P&L  
swap | string | Optional |  | Swap fee  
fee | string | Optional |  | fee  
  
Status Code **400**

TradFiError

Type | Constraints  
---|---  
TradFiError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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
    
    url = '/tradfi/positions/history'
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
    url="/tradfi/positions/history"
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
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "position_id": 2648854,
            "symbol": "EURUSD",
            "realized_pnl": "-2.4",
            "realized_pnl_rate": "-0.0339783598282142",
            "volume": "0.3",
            "volume_closed": "0.3",
            "price_open": "1.17722016",
            "position_dir": "Long",
            "price_tp": "0",
            "price_sl": "0",
            "counterparty_price": "",
            "close_price": "1.1772198600000001",
            "time_close": "1769223573",
            "time_create": "1769223566",
            "position_status": "1",
            "realized_pnl_detail": {
              "closed_pnl": "0",
              "swap": "0",
              "fee": "-2.4"
            },
            "close_detail": null
          },
          {
            "position_id": 2648850,
            "symbol": "EURUSD",
            "realized_pnl": "-1.6",
            "realized_pnl_rate": "-0.0339783598282142",
            "volume": "0.2",
            "volume_closed": "0.2",
            "price_open": "1.17722016",
            "position_dir": "Long",
            "price_tp": "0",
            "price_sl": "0",
            "counterparty_price": "",
            "close_price": "1.1772198600000001",
            "time_close": "1769223391",
            "time_create": "1769223287",
            "position_status": "1",
            "realized_pnl_detail": {
              "closed_pnl": "0",
              "swap": "0",
              "fee": "-1.6"
            },
            "close_detail": null
          }
        ]
      }
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

#  Schemas

##  UserAssetResp

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
equity | string | Optional |  | Account equity  
margin_level | string | Optional |  | Margin level (percentage)  
balance | string | Optional |  | Account Balance  
margin | string | Optional |  | Used margin  
margin_free | string | Optional |  | Available Margin  
unrealized_pnl | string | Optional |  | Unrealized PNL  
      
    
    {
      "timestamp": 0,
      "data": {
        "equity": "0.00",
        "margin_level": "0.00",
        "balance": "0.00",
        "margin": "0.00",
        "margin_free": "0.00",
        "unrealized_pnl": "0.00"
      }
    }
    
    

##  CreateUserResp

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
status | integer | Optional |  | Status (1=not opened, 2=pending review, 3=opened)  
leverage | integer | Optional |  | Leverage  
      
    
    {
      "timestamp": 0,
      "data": {
        "status": 0,
        "leverage": 0
      }
    }
    
    

##  OrderLog

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
log_id | integer(int64) | Optional |  | logID  
symbol | string | Optional |  | Trading pair of the order  
price_type | string | Optional | enum: ["market","trigger"] | Trade type (market=market price, trigger=trigger price)  
state | integer | Optional |  | Order status code (1=placed, 2=canceled, 3=partially filled, 4=filled, 5=rejected)  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
volume | string | Optional |  | Order quantity  
price | string | Optional |  | Average fill price  
      
    
    {
      "timestamp": 0,
      "data": {
        "order_id": 2648991,
        "log_id": 87699,
        "symbol": "USDCAD",
        "price_type": "market",
        "state": 4,
        "side": 2,
        "volume": "0.05",
        "price": "1.3689"
      }
    }
    
    

##  TradFiPositionUpdateRequest

Modify position take profit/stop loss parameters

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price_tp | string|null | Optional | nullable: true | Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface  
price_sl | string|null | Optional | nullable: true | Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface  
      
    
    {
      "price_tp": "1",
      "price_sl": "1"
    }
    
    

##  CreateTransaction

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  |   
      
    
    {
      "timestamp": 0,
      "data": {}
    }
    
    

##  TradFiTicker

TradFiTicker

Ticker summary information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
highest_price | string | Optional |  | High price  
lowest_price | string | Optional |  | Low price  
price_change | string | Optional |  | Price change percentage (multiplied by 100)  
price_change_amount | string | Optional |  | Price change amount  
today_open_price | string | Optional |  | Today's open price  
last_today_close_price | string | Optional |  | Previous close price  
last_price | string | Optional |  | Last trading price  
bid_price | string | Optional |  | Bid price  
ask_price | string | Optional |  | Ask price  
favorite | boolean | Optional |  | Is favorited  
status | string | Optional |  | Trading status (open=tradable, closed=non-tradable)  
close_time | integer(int64) | Optional |  | Close time (Unix timestamp in seconds)  
open_time | integer(int64) | Optional |  | Open time (Unix timestamp in seconds)  
next_open_time | integer(int64) | Optional |  | Next open time (0 means none)  
trade_mode | string | Optional |  | Trading mode code  
category_name | string | Optional |  | Category name  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "timestamp": 0,
      "data": {
        "highest_price": "5093.04",
        "lowest_price": "5003.61",
        "price_change": "1.32",
        "price_change_amount": "66.13",
        "today_open_price": "5008.06",
        "last_today_close_price": "4989.92",
        "last_price": "5074.19",
        "bid_price": "5073.83",
        "ask_price": "5074.06",
        "favorite": false,
        "status": "open",
        "close_time": 1769464800,
        "open_time": 1769378400,
        "next_open_time": 0,
        "trade_mode": "4",
        "category_name": "Metals"
      }
    }
    
    

##  Symbols

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Trading symbol list  
  
**data / list**

Trading symbol list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Trading symbol information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Trading symbol code  
symbol_desc | string | Optional |  | Trading symbol description  
category_id | integer | Optional |  | Category ID  
status | string | Optional |  | Trading status (open=tradable, closed=non-tradable)  
trade_mode | string | Optional |  | Trading mode code (0=disabled, 1=long only, 2=short only, 3=close only, 4=full trading access)  
icon_link | string | Optional |  | Symbol icon URL  
close_time | integer(int64) | Optional |  | Close time (Unix timestamp in seconds)  
open_time | integer(int64) | Optional |  | Open time (Unix timestamp in seconds)  
next_open_time | integer(int64) | Optional |  | Next open time (Unix timestamp in seconds, 0 means none)  
settlement_currency | string | Optional |  | Settlement currency  
settlement_currency_symbol | string | Optional |  | Settlement currency symbol  
price_precision | integer | Optional |  | Price precision (decimal places)  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  Mt5Account

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Optional |  | Business Status Code; Non-zero Indicates Business Exception, Please Check Message  
message | string | Optional |  | Response message  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
leverage | integer | Optional |  | Leverage multiplier  
stop_out_level | string | Optional |  | Liquidation margin ratio  
status | integer | Optional |  | Account status (1=not opened, 2=pending review, 3=active)  
      
    
    {
      "code": 0,
      "message": "ok",
      "timestamp": 0,
      "data": {
        "leverage": 100,
        "stop_out_level": "50%",
        "status": 1
      }
    }
    
    

##  PositionHistoryList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer | Optional |  | Total amount  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  | Query historical position list  
  
**data / list**

Query historical position list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Position close history

Type | Constraints  
---|---  
object | required: ["position_id","symbol","realized_pnl","volume","volume_closed","price_open","position_dir","close_price","time_create","time_close","position_status","realized_pnl_detail"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
position_id | integer(int64) | Required |  | Position ID  
symbol | string | Required |  | Market / Trading symbol  
realized_pnl | string | Required |  | Realized PnL  
realized_pnl_rate | string | Optional |  | Realized return rate  
volume | string | Required |  | Position size / Maximum position size  
volume_closed | string | Required |  | Close volume  
price_open | string | Required |  | Average Opening Price  
position_dir | string | Required | enum: ["Long","Short"] | Position Direction  
\- Long: Long Position  
\- Short: Short Position  
price_tp | string | Optional |  | Take profit price  
price_sl | string | Optional |  | Stop loss price  
counterparty_price | string | Optional |  | Counterparty price  
close_price | string | Required |  | Close price  
time_create | string | Required |  | Open time (timestamp in seconds)  
time_close | string | Required |  | Close time (timestamp in seconds)  
position_status | string | Required |  | Position Status  
\- 1: Fully Closed  
\- 2: Forced Liquidation  
close_detail | object|null | Optional | nullable: true | Liquidation details (null for normal close)  
realized_pnl_detail | object | Required |  | Realized P&L details  
  
**data / list / items / close_detail**

Liquidation details (null for normal close)

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
margin_level | string | Optional |  | Margin ratio (multiplied by 100)  
margin | string | Optional |  | Margin  
equity | string | Optional |  | Net equity  
stop_out_level | string | Optional |  | Liquidation ratio (multiplied by 100)  
  
**data / list / items / realized_pnl_detail**

Realized P&L details

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
closed_pnl | string | Optional |  | Close Position P&L  
swap | string | Optional |  | Swap fee  
fee | string | Optional |  | fee  
      
    
    {
      "timestamp": 0,
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      }
    }
    
    

##  TradFiClosePositionRequest

Close position request parameters

Type | Constraints  
---|---  
object | required: ["close_type"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
close_type | integer | Required | enum: [1,2] | Close Type  
Description:  
\- 1: Partial Close (close_volume is required)  
\- 2: Full Close (close_volume is not required)  
close_volume | string|null | Optional | nullable: true | Close Volume  
Description:  
\- Required when close_type = 1  
\- Ignored when close_type = 2  
      
    
    {
      "close_type": 1,
      "close_volume": "1"
    }
    
    

##  TradFiTransactionRequest

Fund Transfer Request Body

Type | Constraints  
---|---  
object | required: ["asset","change","type"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Asset type, e.g., USDT, currently only USDT is supported  
change | string | Required |  | Change Quantity, supports up to two decimal places  
type | string | Required | enum: ["deposit","withdraw"] | Transaction Type (deposit - transfer in, withdraw - transfer out)  
      
    
    {
      "asset": "USDT",
      "change": "10",
      "type": "withdraw"
    }
    
    

##  TransactionList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer | Optional |  | Total Records  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  | Record List  
  
**data / list**

Record List

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Optional |  | Asset Type  
type | string | Optional | enum: ["deposit-转入","withdraw-转出","dividend-分红结息","fill_negative-填平负余额"] | Trading Type  
type_desc | string | Optional |  | Transaction Type Description  
change | string | Optional |  | Change amount  
balance | string | Optional |  | Current Balance  
time | integer(int64) | Optional |  | Occurrence Time (Second-level Timestamp)  
      
    
    {
      "data": {
        "total": 2,
        "total_page": 1,
        "list": [
          {}
        ]
      },
      "timestamp": 1769332996590
    }
    
    

##  CreateOrder

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Order result  
  
**data**

Order result

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Queue Task ID (not order ID)  
      
    
    {
      "timestamp": 0,
      "data": {
        "id": "117"
      }
    }
    
    

##  UpdatePosition

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  |   
      
    
    {
      "timestamp": 0,
      "data": {}
    }
    
    

##  TradFiError

TradFiError

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "timestamp": 0
    }
    
    

##  UpdateOrder

Order modification result

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional | required: ["order_id","symbol","state","volume","price","price_tp","price_sl"] | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object | required: ["order_id","symbol","state","volume","price","price_tp","price_sl"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Required |  | Order ID  
symbol | string | Required |  | Currency pair  
state | string | Required |  | Order status code  
volume | string | Required |  | Order quantity  
price | string | Required |  | Current price  
price_tp | string | Required |  | Current take profit price  
price_sl | string | Required |  | Current stop loss price  
      
    
    {
      "timestamp": 0,
      "data": {
        "order_id": 2630591,
        "symbol": "USDCHF",
        "state": 1,
        "volume": "1.6",
        "price": "5.000000",
        "price_tp": "5.200000",
        "price_sl": "4.800000"
      }
    }
    
    

##  PositionList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional |  | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Position information  
  
**data / list**

Position information

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Position information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
position_id | integer(int64) | Optional |  | Position ID  
symbol | string | Optional |  | Trading market code  
symbol_desc | string | Optional |  | Market description  
margin | string | Optional |  | Used margin  
unrealized_pnl | string | Optional |  | Unrealized PNL  
unrealized_pnl_rate | string | Optional |  | Unrealized return rate  
volume | string | Optional |  | Position size  
price_open | string | Optional |  | Average Opening Price  
position_dir | string | Optional |  | Position direction (Long=long position, Short=short position)  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  DeletePosition

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  |   
      
    
    {
      "timestamp": 0,
      "data": {}
    }
    
    

##  Categories

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Data  
  
**data**

Data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  |   
  
**data / list**

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Category information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
category_id | integer | Optional |  | Category ID  
is_favorite | boolean | Optional |  | Whether it is a custom category, generally no need to pay attention  
category_name | string | Optional |  | Category name  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  Klines

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Kline data list  
  
**data / list**

Kline data list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Single kline data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
o | string | Optional |  | Open price  
c | string | Optional |  | Close price  
h | string | Optional |  | High price  
l | string | Optional |  | Low price  
t | integer(int64) | Optional |  | Timestamp (Unix seconds)  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  TradFiOrderRequest

Place order request parameters

Type | Constraints  
---|---  
object | required: ["price","price_type","side","symbol","volume"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Order price  
price_type | string | Required | enum: ["trigger","market"] | Price type (trigger=trigger price, market=market price)  
side | integer | Required | enum: [1,2] | Side (1=sell, 2=buy)  
symbol | string | Required |  | Base trading symbol code  
volume | string | Required |  | Order quantity  
price_tp | string | Optional |  | Take profit price (optional)  
price_sl | string | Optional |  | Stop loss price (optional)  
leverage | integer | Optional |  | Leverage multiplier (must be one of the leverage multipliers allowed for the symbol in the trading symbol details response)  
      
    
    {
      "price": "0.9",
      "price_type": "trigger",
      "side": 2,
      "symbol": "EURUSD",
      "volume": "10",
      "price_tp": "1.5",
      "price_sl": "0.8",
      "leverage": 500
    }
    
    

##  SymbolCommissions

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | List of symbol commission rates  
  
**data / list**

List of symbol commission rates

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Symbol commission rate

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
category_code | string | Optional |  | Category code  
symbol | string | Optional |  | Trading symbol code  
fee_per_lot | string | Optional |  | Commission rate per lot  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  TradFiOrderUpdateRequest

Modify order price and take profit/stop loss parameters

Type | Constraints  
---|---  
object | required: ["price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Price  
Description:  
\- Required  
price_tp | string|null | Optional | nullable: true | Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface  
price_sl | string|null | Optional | nullable: true | Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface  
      
    
    {
      "price": "2",
      "price_tp": "1.5",
      "price_sl": "0.8"
    }
    
    

##  ContractDetail

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Contract Details List  
  
**data / list**

Contract Details List

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Futures contract details

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Trading symbol code  
symbol_desc | string | Optional |  | Trading symbol description  
category_name | string | Optional |  | Category name  
contract_volume | string | Optional |  | Contract Volume  
settlement_currency | string | Optional |  | Settle currency  
max_order_volume | string | Optional |  | Maximum Order Volume  
min_order_volume | string | Optional |  | Minimum Order Volume  
leverage | string | Optional |  | Leverage multiplier  
price_precision | integer | Optional |  | Price precision (decimal places)  
price_sl_level | string | Optional |  | Stop Loss Price Level  
swap_cost_type | string | Optional |  | Swap Cost Type  
buy_swap_cost_rate | string | Optional |  | Buy Swap Cost Rate  
sell_swap_cost_rate | string | Optional |  | Sell Swap Cost Rate  
swap_cost_3day | string | Optional |  | 3-Day Swap Cost  
trade_timezone | string | Optional |  | Trading Timezone  
trade_mode | string | Optional |  | Trading mode code (0=disabled, 1=long only, 2=short only, 3=close only, 4=full trading access)  
icon_link | string | Optional |  | Symbol icon URL  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  OrderHistoryList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Historical order list  
  
**data / list**

Historical order list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Order detail

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
symbol | string | Optional |  | Currency pair  
symbol_desc | string | Optional |  | Symbol description  
price_type | string | Optional | enum: ["market","trigger"] | Trade type (market=market price, trigger=trigger price)  
order_opt_type | integer | Optional | enum: [1,2,3,4,5,6] | Order operation type (1=sell, 2=buy, 3=close long, 4=close short, 5=force close long, 6=force close short)  
state | integer | Optional |  | Order status code  
state_desc | string | Optional |  | Order status description  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
volume | string | Optional |  | Order quantity  
fill_volume | string | Optional |  | Trading size  
close_pnl | string | Optional |  | Close Position P&L  
price | string | Optional |  | Average fill price  
trigger_price | string | Optional |  | Trigger price  
price_tp | string | Optional |  | Take profit price  
price_sl | string | Optional |  | Stop loss price  
time_setup | integer(int64) | Optional |  | Order time (Unix timestamp in seconds)  
time_done | integer(int64) | Optional |  | End time (Unix timestamp in seconds)  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  OrderList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
data | object | Optional |  | Response data  
  
**data**

Response data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Order list  
  
**data / list**

Order list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Order detail

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
symbol | string | Optional |  | Currency pair  
symbol_desc | string | Optional |  | Symbol description  
price_type | string | Optional | enum: ["market","trigger"] | Trade type (market=market price, trigger=trigger price)  
state | integer | Optional |  | Order status code  
state_desc | string | Optional |  | Order status description  
finished | integer | Optional | enum: [0,1] | Is completed (0=shown in active order list, 1=not shown in active list)  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
volume | string | Optional |  | Order quantity  
price | string | Optional |  | Trigger price  
price_tp | string | Optional |  | Take profit price  
price_sl | string | Optional |  | Stop loss price  
time_setup | integer(int64) | Optional |  | Order time (Unix timestamp in seconds)  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }