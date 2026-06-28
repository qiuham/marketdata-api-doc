---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/tradfi
api_type: Trading
updated_at: 2026-05-27 20:16:10.890456
---

# TradFi

TradFi is a traditional financial trading platform providing forex and CFD trading services based on MT5. The TradFi API offers complete functionality for user management, asset queries, order management, position management, and market data queries.

  * REST API Base URL for Live Trading: `https://api.gateio.ws/api/v4/`
  * [Help Center ](https://www.gate.com/help/tradfi/functional)
  * [TradFi Trading ](https://www.gate.com/tradfi)
  * Note: Before using the APIs of this service, ensure the user has activated the TradFi service. Activation can be done by calling the Activate TradFi User Interface or logging into the app to activate.

##  Query MT5 account information🔒 Authenticated

GET`/tradfi/users/mt5-account`

GET `/tradfi/users/mt5-account`

_Query MT5 account information_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | Mt5Account  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» code | integer | Business Status Code; Non-zero Indicates Business Exception, Please Check Message  
» message | string | Response message  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» mt5_uid | integer | MT5 userID  
»» leverage | integer | Position leverage  
»» stop_out_level | string | Liquidation margin ratio  
»» status | integer | Account status (1=not opened, 2=pending review, 3=active)  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
        "mt5_uid": 0,
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | Categories  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Data  
»» list | array | none  
»»» _None_ | object | Category information  
»»»» category_id | integer | Category ID  
»»»» is_favorite | boolean | Whether it is a custom category, generally no need to pay attention  
»»»» category_name | string | Category name  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
    

##  Query trading symbol list

GET`/tradfi/symbols`

GET `/tradfi/symbols`

_Query trading symbol list_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | Symbols  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» list | array | Trading symbol list  
»»» _None_ | object | Trading symbol information  
»»»» symbol | string | Trading symbol code  
»»»» symbol_desc | string | Trading symbol description  
»»»» category_id | integer | Category ID  
»»»» status | string | Trading status (open=tradable, closed=non-tradable)  
»»»» trade_mode | string | Trading mode code (0=disabled, 1=long only, 2=short only, 3=close only, 4=full trading access)  
»»»» icon_link | string | Symbol icon URL  
»»»» close_time | integer(int64) | Close time (Unix timestamp in seconds)  
»»»» open_time | integer(int64) | Open time (Unix timestamp in seconds)  
»»»» next_open_time | integer(int64) | Next open time (Unix timestamp in seconds, 0 means none)  
»»»» settlement_currency | string | Settlement currency  
»»»» settlement_currency_symbol | string | Settlement currency symbol  
»»»» price_precision | integer | Price precision (decimal places)  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | ContractDetail  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» list | array | Contract Details List  
»»» _None_ | object | Futures contract details  
»»»» symbol | string | Trading symbol code  
»»»» symbol_desc | string | Trading symbol description  
»»»» category_name | string | Category name  
»»»» contract_volume | string | Contract Volume  
»»»» settlement_currency | string | Settle currency  
»»»» max_order_volume | string | Maximum Order Volume  
»»»» min_order_volume | string | Minimum Order Volume  
»»»» leverage | string | Position leverage  
»»»» price_precision | integer | Price precision (decimal places)  
»»»» price_sl_level | string | Stop Loss Price Level  
»»»» swap_cost_type | string | Swap Cost Type  
»»»» buy_swap_cost_rate | string | Buy Swap Cost Rate  
»»»» sell_swap_cost_rate | string | Sell Swap Cost Rate  
»»»» swap_cost_3day | string | 3-Day Swap Cost  
»»»» trade_timezone | string | Trading Timezone  
»»»» trade_mode | string | Trading mode code (0=disabled, 1=long only, 2=short only, 3=close only, 4=full trading access)  
»»»» icon_link | string | Symbol icon URL  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | Klines  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» list | array | Kline data list  
»»» _None_ | object | Single kline data  
»»»» o | string | Open price  
»»»» c | string | Close price  
»»»» h | string | High price  
»»»» l | string | Low price  
»»»» t | integer(int64) | Timestamp (Unix seconds)  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradFiTicker  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

_TradFiTicker_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» highest_price | string | Highest price  
»» lowest_price | string | Lowest price  
»» price_change | string | Price change percentage (multiplied by 100)  
»» price_change_amount | string | Price change amount  
»» today_open_price | string | Today's open price  
»» last_today_close_price | string | Previous close price  
»» last_price | string | Last trading price  
»» bid_price | string | Bid price  
»» ask_price | string | Ask price  
»» favorite | boolean | Is favorited  
»» status | string | Trading status (open=tradable, closed=non-tradable)  
»» close_time | integer(int64) | Close time (Unix timestamp in seconds)  
»» open_time | integer(int64) | Open time (Unix timestamp in seconds)  
»» next_open_time | integer(int64) | Next open time (0 means none)  
»» trade_mode | string | Trading mode code  
»» category_name | string | Category name  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
    

##  Create TradFi user🔒 Authenticated

POST`/tradfi/users`

POST `/tradfi/users`

_Create TradFi user_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Account opened successfully
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Account opened successfully | CreateUserResp  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | none  
»» status | integer | Status (1=not opened, 2=pending review, 3=opened)  
»» leverage | integer | leverage  
»» mt5_uid | string | mt5uid  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
        "status": 3,
        "mt5_uid": "1"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | UserAssetResp  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» equity | string | Account equity  
»» margin_level | string | Margin level (percentage)  
»» balance | string | Account Balance  
»» margin | string | Used margin  
»» margin_free | string | Available Margin  
»» unrealized_pnl | string | Unrealized PNL  
»» mt5_uid | string | MT5 userID  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
        "unrealized_pnl": "0.00",
        "mt5_uid": "10122"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TransactionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» total | integer | Total Records  
»» total_page | integer | Total pages  
»» list | array | Record List  
»»» asset | string | Asset Type  
»»» type | string | Trading Type  
»»» type_desc | string | Transaction Type Description  
»»» change | string | Change Quantity  
»»» balance | string | Current Balance  
»»» time | integer(int64) | Occurrence Time (Second-level Timestamp)  
»» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | deposit-转入  
type | withdraw-转出  
type | dividend-分红结息  
type | fill_negative-填平负余额  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
    

##  Fund Deposit and Withdrawal🔒 Authenticated

POST`/tradfi/transactions`

POST `/tradfi/transactions`

_Fund Deposit and Withdrawal_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiTransactionRequest | Required | none  
↳ asset | body | string | Required | Asset type, e.g., USDT, currently only USDT is supported  
↳ change | body | string | Required | Change Quantity, supports up to two decimal places  
↳ type | body | string | Required | Transaction Type (deposit - transfer in, withdraw - transfer out)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» type | deposit  
» type | withdraw  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | CreateTransaction  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | none  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | OrderList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» list | array | Order list  
»»» _None_ | object | Order detail  
»»»» order_id | integer | Order ID  
»»»» symbol | string | Currency pair  
»»»» symbol_desc | string | Trading symbol description  
»»»» price_type | string | Trade type (market=market price, trigger=trigger price)  
»»»» state | integer | Order status code  
»»»» state_desc | string | Order status description  
»»»» finished | integer | Is completed (0=shown in active order list, 1=not shown in active list)  
»»»» side | integer | Order side (1=sell, 2=buy)  
»»»» volume | string | Order volume  
»»»» price | string | Trigger price  
»»»» price_tp | string | Take profit price  
»»»» price_sl | string | Stop loss price  
»»»» time_setup | integer(int64) | Order time (Unix timestamp in seconds)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | market  
price_type | trigger  
finished | 0  
finished | 1  
side | 1  
side | 2  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
    

##  Create an order🔒 Authenticated

POST`/tradfi/orders`

POST `/tradfi/orders`

_Create an order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiOrderRequest | Required | none  
↳ price | body | string | Required | Order price  
↳ price_type | body | string | Required | Price type (trigger=trigger price, market=market price)  
↳ side | body | integer | Required | Order side (1=sell, 2=buy)  
↳ symbol | body | string | Required | Trading symbol code  
↳ volume | body | string | Required | Order volume  
↳ price_tp | body | string | Optional | Take profit price (optional)  
↳ price_sl | body | string | Optional | Stop loss price (optional)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» price_type | trigger  
» price_type | market  
» side | 1  
» side | 2  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order placed successfully
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order placed successfully | CreateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Order result  
»» id | string | Queue Task ID (not task ID)  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
    body='{"price":"0.9","price_type":"trigger","side":2,"symbol":"EURUSD","volume":"10","price_tp":"1.5","price_sl":"0.8"}'
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
    body_param='{"price":"0.9","price_type":"trigger","side":2,"symbol":"EURUSD","volume":"10","price_tp":"1.5","price_sl":"0.8"}'
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
      "price_sl": "0.8"
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
↳ price | body | string | Required | Price  
Description:  
\- Required  
↳ price_tp | body | string|null | Optional | Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface  
↳ price_sl | body | string|null | Optional | Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface  
order_id | path | integer | Required | Order ID  
  
####  Detailed descriptions

**» price** : Price  
Description:  
\- Required

**» price_tp** : Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface

**» price_sl** : Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | UpdateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

_Order modification result_

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» order_id | integer | Order ID  
»» symbol | string | Currency pair  
»» state | string | Order status code  
»» volume | string | Order volume  
»» price | string | Current price  
»» price_tp | string | Current take profit price  
»» price_sl | string | Current stop loss price  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
order_id | path | integer | Required | Order ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Deleted successfully
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Deleted successfully | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

_Returns empty object on success_

Name | Type | Description  
---|---|---  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
side | query | integer | Optional | Order side (1=sell, 2=buy)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | 1  
side | 2  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | OrderHistoryList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» list | array | Historical order list  
»»» _None_ | object | Order detail  
»»»» order_id | integer | Order ID  
»»»» symbol | string | Currency pair  
»»»» symbol_desc | string | Trading symbol description  
»»»» price_type | string | Trade type (market=market price, trigger=trigger price)  
»»»» order_opt_type | integer | Order operation type (1=sell, 2=buy, 3=close long, 4=close short, 5=force close long, 6=force close short)  
»»»» state | integer | Order status code  
»»»» state_desc | string | Order status description  
»»»» side | integer | Order side (1=sell, 2=buy)  
»»»» volume | string | Order volume  
»»»» fill_volume | string | Trading size  
»»»» close_pnl | string | Close Position P&L  
»»»» price | string | Average fill price  
»»»» trigger_price | string | Trigger price  
»»»» price_tp | string | Take profit price  
»»»» price_sl | string | Stop loss price  
»»»» time_setup | integer(int64) | Order time (Unix timestamp in seconds)  
»»»» time_done | integer(int64) | End time (Unix timestamp in seconds)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | market  
price_type | trigger  
order_opt_type | 1  
order_opt_type | 2  
order_opt_type | 3  
order_opt_type | 4  
order_opt_type | 5  
order_opt_type | 6  
side | 1  
side | 2  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
    

##  Query active position list🔒 Authenticated

GET`/tradfi/positions`

GET `/tradfi/positions`

_Query active position list_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | PositionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» list | array | Position information  
»»» _None_ | object | Position information  
»»»» position_id | integer | Position ID  
»»»» symbol | string | Trading market code  
»»»» symbol_desc | string | Market description  
»»»» margin | string | Used margin  
»»»» unrealized_pnl | string | Unrealized PNL  
»»»» unrealized_pnl_rate | string | Unrealized return rate  
»»»» volume | string | Position size  
»»»» price_open | string | Average Opening Price  
»»»» position_dir | string | Position direction (Long=long position, Short=short position)  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
position_id | path | integer | Required | Position ID  
body | body | TradFiPositionUpdateRequest | Required | none  
↳ price_tp | body | string|null | Optional | Take profit price  
↳ price_sl | body | string|null | Optional | Stop loss price  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | UpdatePosition  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | none  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
position_id | path | integer | Required | Position ID  
body | body | TradFiClosePositionRequest | Required | none  
↳ close_type | body | integer | Required | Close Position Type  
↳ close_volume | body | string|null | Optional | Close volume  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» close_type | 1  
» close_type | 2  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | DeletePosition  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | none  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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
begin_time | query | integer(int64) | Optional | Start Time (Unix Timestamp, seconds). The earliest queryable time is one month ago  
end_time | query | integer(int64) | Optional | End time (timestamp in seconds)  
symbol | query | string | Optional | Trading symbol (e.g., EURUSD)  
position_dir | query | string | Optional | Position direction (Long=long position, Short=short position)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
position_dir | Long  
position_dir | Short  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request success
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Request failed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | PositionHistoryList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
» data | object | Response data  
»» total | integer | Total amount  
»» total_page | integer | Total pages  
»» list | array | Query historical position list  
»»» _None_ | object | Position close history  
»»»» position_id | integer(int64) | Position ID  
»»»» symbol | string | Market / Trading symbol  
»»»» realized_pnl | string | Realized PnL  
»»»» realized_pnl_rate | string | Realized return rate  
»»»» volume | string | Position size / Maximum position size  
»»»» volume_closed | string | Close volume  
»»»» price_open | string | Average Opening Price  
»»»» position_dir | string | Position Direction  
\- Long: Long Position  
\- Short: Short Position  
»»»» price_tp | string | Take profit price  
»»»» price_sl | string | Stop loss price  
»»»» counterparty_price | string | Counterparty price  
»»»» close_price | string | Close price  
»»»» time_create | string | Open time (timestamp in seconds)  
»»»» time_close | string | Close time (timestamp in seconds)  
»»»» position_status | string | Position Status  
\- 1: Fully Closed  
\- 2: Forced Liquidation  
»»»» close_detail | object|null | Liquidation details (null for normal close)  
»»»»» margin_level | string | Margin ratio (multiplied by 100)  
»»»»» margin | string | Position margin  
»»»»» equity | string | Net equity  
»»»»» stop_out_level | string | Liquidation ratio (multiplied by 100)  
»»»» realized_pnl_detail | object | Realized P&L details  
»»»»» closed_pnl | string | Close Position P&L  
»»»»» swap | string | Swap fee  
»»»»» fee | string | fee  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
position_dir | Long  
position_dir | Short  
  
Status Code **400**

_TradFiError_

Name | Type | Description  
---|---|---  
» label | string | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
» message | string | Return message, returned when request error occurs  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
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

##  OrderList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ list | array | Optional | none | Order list  
↳ None | object | Optional | none | Order detail  
↳ order_id | integer | Optional | none | Order ID  
↳ symbol | string | Optional | none | Currency pair  
↳ symbol_desc | string | Optional | none | Trading symbol description  
↳ price_type | string | Optional | none | Trade type (market=market price, trigger=trigger price)  
↳ state | integer | Optional | none | Order status code  
↳ state_desc | string | Optional | none | Order status description  
↳ finished | integer | Optional | none | Is completed (0=shown in active order list, 1=not shown in active list)  
↳ side | integer | Optional | none | Order side (1=sell, 2=buy)  
↳ volume | string | Optional | none | Order volume  
↳ price | string | Optional | none | Trigger price  
↳ price_tp | string | Optional | none | Take profit price  
↳ price_sl | string | Optional | none | Stop loss price  
↳ time_setup | integer(int64) | Optional | none | Order time (Unix timestamp in seconds)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | market  
price_type | trigger  
finished | 0  
finished | 1  
side | 1  
side | 2  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  Klines

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ list | array | Optional | none | Kline data list  
↳ None | object | Optional | none | Single kline data  
↳ o | string | Optional | none | Open price  
↳ c | string | Optional | none | Close price  
↳ h | string | Optional | none | High price  
↳ l | string | Optional | none | Low price  
↳ t | integer(int64) | Optional | none | Timestamp (Unix seconds)  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  PositionHistoryList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ total | integer | Optional | none | Total amount  
↳ total_page | integer | Optional | none | Total pages  
↳ list | array | Optional | none | Query historical position list  
↳ None | object | Optional | none | Position close history  
↳ position_id | integer(int64) | Required | none | Position ID  
↳ symbol | string | Required | none | Market / Trading symbol  
↳ realized_pnl | string | Required | none | Realized PnL  
↳ realized_pnl_rate | string | Optional | none | Realized return rate  
↳ volume | string | Required | none | Position size / Maximum position size  
↳ volume_closed | string | Required | none | Close volume  
↳ price_open | string | Required | none | Average Opening Price  
↳ position_dir | string | Required | none | Position Direction  
\- Long: Long Position  
\- Short: Short Position  
↳ price_tp | string | Optional | none | Take profit price  
↳ price_sl | string | Optional | none | Stop loss price  
↳ counterparty_price | string | Optional | none | Counterparty price  
↳ close_price | string | Required | none | Close price  
↳ time_create | string | Required | none | Open time (timestamp in seconds)  
↳ time_close | string | Required | none | Close time (timestamp in seconds)  
↳ position_status | string | Required | none | Position Status  
\- 1: Fully Closed  
\- 2: Forced Liquidation  
↳ close_detail | object|null | Optional | none | Liquidation details (null for normal close)  
↳ margin_level | string | Optional | none | Margin ratio (multiplied by 100)  
↳ margin | string | Optional | none | Position margin  
↳ equity | string | Optional | none | Net equity  
↳ stop_out_level | string | Optional | none | Liquidation ratio (multiplied by 100)  
↳ realized_pnl_detail | object | Required | none | Realized P&L details  
↳ closed_pnl | string | Optional | none | Close Position P&L  
↳ swap | string | Optional | none | Swap fee  
↳ fee | string | Optional | none | fee  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
position_dir | Long  
position_dir | Short  
      
    
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
    
    

##  Categories

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Data  
↳ list | array | Optional | none | none  
↳ None | object | Optional | none | Category information  
↳ category_id | integer | Optional | none | Category ID  
↳ is_favorite | boolean | Optional | none | Whether it is a custom category, generally no need to pay attention  
↳ category_name | string | Optional | none | Category name  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  UpdateOrder

_Order modification result_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ order_id | integer | Optional | none | Order ID  
↳ symbol | string | Optional | none | Currency pair  
↳ state | string | Optional | none | Order status code  
↳ volume | string | Optional | none | Order volume  
↳ price | string | Optional | none | Current price  
↳ price_tp | string | Optional | none | Current take profit price  
↳ price_sl | string | Optional | none | Current stop loss price  
      
    
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
    
    

##  ContractDetail

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ list | array | Optional | none | Contract Details List  
↳ None | object | Optional | none | Futures contract details  
↳ symbol | string | Optional | none | Trading symbol code  
↳ symbol_desc | string | Optional | none | Trading symbol description  
↳ category_name | string | Optional | none | Category name  
↳ contract_volume | string | Optional | none | Contract Volume  
↳ settlement_currency | string | Optional | none | Settle currency  
↳ max_order_volume | string | Optional | none | Maximum Order Volume  
↳ min_order_volume | string | Optional | none | Minimum Order Volume  
↳ leverage | string | Optional | none | Position leverage  
↳ price_precision | integer | Optional | none | Price precision (decimal places)  
↳ price_sl_level | string | Optional | none | Stop Loss Price Level  
↳ swap_cost_type | string | Optional | none | Swap Cost Type  
↳ buy_swap_cost_rate | string | Optional | none | Buy Swap Cost Rate  
↳ sell_swap_cost_rate | string | Optional | none | Sell Swap Cost Rate  
↳ swap_cost_3day | string | Optional | none | 3-Day Swap Cost  
↳ trade_timezone | string | Optional | none | Trading Timezone  
↳ trade_mode | string | Optional | none | Trading mode code (0=disabled, 1=long only, 2=short only, 3=close only, 4=full trading access)  
↳ icon_link | string | Optional | none | Symbol icon URL  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  TradFiTransactionRequest

_Fund Transfer Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
asset | string | Required | none | Asset type, e.g., USDT, currently only USDT is supported  
change | string | Required | none | Change Quantity, supports up to two decimal places  
type | string | Required | none | Transaction Type (deposit - transfer in, withdraw - transfer out)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | deposit  
type | withdraw  
      
    
    {
      "asset": "USDT",
      "change": "10",
      "type": "withdraw"
    }
    
    

##  Symbols

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ list | array | Optional | none | Trading symbol list  
↳ None | object | Optional | none | Trading symbol information  
↳ symbol | string | Optional | none | Trading symbol code  
↳ symbol_desc | string | Optional | none | Trading symbol description  
↳ category_id | integer | Optional | none | Category ID  
↳ status | string | Optional | none | Trading status (open=tradable, closed=non-tradable)  
↳ trade_mode | string | Optional | none | Trading mode code (0=disabled, 1=long only, 2=short only, 3=close only, 4=full trading access)  
↳ icon_link | string | Optional | none | Symbol icon URL  
↳ close_time | integer(int64) | Optional | none | Close time (Unix timestamp in seconds)  
↳ open_time | integer(int64) | Optional | none | Open time (Unix timestamp in seconds)  
↳ next_open_time | integer(int64) | Optional | none | Next open time (Unix timestamp in seconds, 0 means none)  
↳ settlement_currency | string | Optional | none | Settlement currency  
↳ settlement_currency_symbol | string | Optional | none | Settlement currency symbol  
↳ price_precision | integer | Optional | none | Price precision (decimal places)  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  CreateUserResp

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | none  
↳ status | integer | Optional | none | Status (1=not opened, 2=pending review, 3=opened)  
↳ leverage | integer | Optional | none | leverage  
↳ mt5_uid | string | Optional | none | mt5uid  
      
    
    {
      "timestamp": 0,
      "data": {
        "status": 0,
        "leverage": 0,
        "mt5_uid": "string"
      }
    }
    
    

##  TradFiOrderUpdateRequest

_Modify order price and take profit/stop loss parameters_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
price | string | Required | none | Price  
Description:  
\- Required  
price_tp | string|null | Optional | none | Take Profit Price  
Description:  
\- If not provided or set to "0": The original take profit price will be cleared  
\- If you do not want to clear it, pass the original take profit price returned by the interface  
price_sl | string|null | Optional | none | Stop Loss Price  
Description:  
\- If not provided or set to "0": The original stop loss price will be cleared  
\- If you do not want to clear it, pass the original stop loss price returned by the interface  
      
    
    {
      "price": "2",
      "price_tp": "1.5",
      "price_sl": "0.8"
    }
    
    

##  UpdatePosition

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | none  
      
    
    {
      "timestamp": 0,
      "data": {}
    }
    
    

##  TransactionList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
↳ total | integer | Optional | none | Total Records  
↳ total_page | integer | Optional | none | Total pages  
↳ list | array | Optional | none | Record List  
↳ asset | string | Optional | none | Asset Type  
↳ type | string | Optional | none | Trading Type  
↳ type_desc | string | Optional | none | Transaction Type Description  
↳ change | string | Optional | none | Change Quantity  
↳ balance | string | Optional | none | Current Balance  
↳ time | integer(int64) | Optional | none | Occurrence Time (Second-level Timestamp)  
↳ timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | deposit-转入  
type | withdraw-转出  
type | dividend-分红结息  
type | fill_negative-填平负余额  
      
    
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
    
    

##  TradFiPositionUpdateRequest

_Modify position take profit/stop loss parameters_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
price_tp | string|null | Optional | none | Take profit price  
price_sl | string|null | Optional | none | Stop loss price  
      
    
    {
      "price_tp": "1",
      "price_sl": "1"
    }
    
    

##  DeletePosition

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | none  
      
    
    {
      "timestamp": 0,
      "data": {}
    }
    
    

##  Mt5Account

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Optional | none | Business Status Code; Non-zero Indicates Business Exception, Please Check Message  
message | string | Optional | none | Response message  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ mt5_uid | integer | Optional | none | MT5 userID  
↳ leverage | integer | Optional | none | Position leverage  
↳ stop_out_level | string | Optional | none | Liquidation margin ratio  
↳ status | integer | Optional | none | Account status (1=not opened, 2=pending review, 3=active)  
      
    
    {
      "code": 0,
      "message": "ok",
      "timestamp": 0,
      "data": {
        "mt5_uid": 0,
        "leverage": 100,
        "stop_out_level": "50%",
        "status": 1
      }
    }
    
    

##  PositionList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
label | string | Optional | none | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional | none | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ list | array | Optional | none | Position information  
↳ None | object | Optional | none | Position information  
↳ position_id | integer | Optional | none | Position ID  
↳ symbol | string | Optional | none | Trading market code  
↳ symbol_desc | string | Optional | none | Market description  
↳ margin | string | Optional | none | Used margin  
↳ unrealized_pnl | string | Optional | none | Unrealized PNL  
↳ unrealized_pnl_rate | string | Optional | none | Unrealized return rate  
↳ volume | string | Optional | none | Position size  
↳ price_open | string | Optional | none | Average Opening Price  
↳ position_dir | string | Optional | none | Position direction (Long=long position, Short=short position)  
      
    
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
    
    

##  CreateTransaction

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | none  
      
    
    {
      "timestamp": 0,
      "data": {}
    }
    
    

##  TradFiOrderRequest

_Place order request parameters_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
price | string | Required | none | Order price  
price_type | string | Required | none | Price type (trigger=trigger price, market=market price)  
side | integer | Required | none | Order side (1=sell, 2=buy)  
symbol | string | Required | none | Trading symbol code  
volume | string | Required | none | Order volume  
price_tp | string | Optional | none | Take profit price (optional)  
price_sl | string | Optional | none | Stop loss price (optional)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | trigger  
price_type | market  
side | 1  
side | 2  
      
    
    {
      "price": "0.9",
      "price_type": "trigger",
      "side": 2,
      "symbol": "EURUSD",
      "volume": "10",
      "price_tp": "1.5",
      "price_sl": "0.8"
    }
    
    

##  TradFiClosePositionRequest

_Close position request parameters_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
close_type | integer | Required | none | Close Position Type  
close_volume | string|null | Optional | none | Close volume  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
close_type | 1  
close_type | 2  
      
    
    {
      "close_type": 1,
      "close_volume": "1"
    }
    
    

##  OrderHistoryList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ list | array | Optional | none | Historical order list  
↳ None | object | Optional | none | Order detail  
↳ order_id | integer | Optional | none | Order ID  
↳ symbol | string | Optional | none | Currency pair  
↳ symbol_desc | string | Optional | none | Trading symbol description  
↳ price_type | string | Optional | none | Trade type (market=market price, trigger=trigger price)  
↳ order_opt_type | integer | Optional | none | Order operation type (1=sell, 2=buy, 3=close long, 4=close short, 5=force close long, 6=force close short)  
↳ state | integer | Optional | none | Order status code  
↳ state_desc | string | Optional | none | Order status description  
↳ side | integer | Optional | none | Order side (1=sell, 2=buy)  
↳ volume | string | Optional | none | Order volume  
↳ fill_volume | string | Optional | none | Trading size  
↳ close_pnl | string | Optional | none | Close Position P&L  
↳ price | string | Optional | none | Average fill price  
↳ trigger_price | string | Optional | none | Trigger price  
↳ price_tp | string | Optional | none | Take profit price  
↳ price_sl | string | Optional | none | Stop loss price  
↳ time_setup | integer(int64) | Optional | none | Order time (Unix timestamp in seconds)  
↳ time_done | integer(int64) | Optional | none | End time (Unix timestamp in seconds)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | market  
price_type | trigger  
order_opt_type | 1  
order_opt_type | 2  
order_opt_type | 3  
order_opt_type | 4  
order_opt_type | 5  
order_opt_type | 6  
side | 1  
side | 2  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  UserAssetResp

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ equity | string | Optional | none | Account equity  
↳ margin_level | string | Optional | none | Margin level (percentage)  
↳ balance | string | Optional | none | Account Balance  
↳ margin | string | Optional | none | Used margin  
↳ margin_free | string | Optional | none | Available Margin  
↳ unrealized_pnl | string | Optional | none | Unrealized PNL  
↳ mt5_uid | string | Optional | none | MT5 userID  
      
    
    {
      "timestamp": 0,
      "data": {
        "equity": "0.00",
        "margin_level": "0.00",
        "balance": "0.00",
        "margin": "0.00",
        "margin_free": "0.00",
        "unrealized_pnl": "0.00",
        "mt5_uid": "10122"
      }
    }
    
    

##  TradFiError

_TradFiError_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
label | string | Optional | none | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional | none | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "timestamp": 0
    }
    
    

##  TradFiTicker

_TradFiTicker_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
label | string | Optional | none | Business status code, non-empty indicates request exception, please refer to TradFi error enumeration in documentation  
message | string | Optional | none | Return message, returned when request error occurs  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Response data  
↳ highest_price | string | Optional | none | Highest price  
↳ lowest_price | string | Optional | none | Lowest price  
↳ price_change | string | Optional | none | Price change percentage (multiplied by 100)  
↳ price_change_amount | string | Optional | none | Price change amount  
↳ today_open_price | string | Optional | none | Today's open price  
↳ last_today_close_price | string | Optional | none | Previous close price  
↳ last_price | string | Optional | none | Last trading price  
↳ bid_price | string | Optional | none | Bid price  
↳ ask_price | string | Optional | none | Ask price  
↳ favorite | boolean | Optional | none | Is favorited  
↳ status | string | Optional | none | Trading status (open=tradable, closed=non-tradable)  
↳ close_time | integer(int64) | Optional | none | Close time (Unix timestamp in seconds)  
↳ open_time | integer(int64) | Optional | none | Open time (Unix timestamp in seconds)  
↳ next_open_time | integer(int64) | Optional | none | Next open time (0 means none)  
↳ trade_mode | string | Optional | none | Trading mode code  
↳ category_name | string | Optional | none | Category name  
      
    
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
    
    

##  CreateOrder

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
data | object | Optional | none | Order result  
↳ id | string | Optional | none | Queue Task ID (not task ID)  
      
    
    {
      "timestamp": 0,
      "data": {
        "id": "117"
      }
    }