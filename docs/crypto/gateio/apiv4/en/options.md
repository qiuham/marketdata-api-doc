---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/options
api_type: Trading
updated_at: 2026-05-27 20:15:32.390877
---

# Options

Options API

##  List all underlying assets

GET`/options/underlyings`

GET `/options/underlyings`

_List all underlying assets_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsUnderlying]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» name | string | Underlying name  
» index_price | string | Spot index price (quote currency)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/underlyings'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/underlyings \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "name": "BTC_USDT",
        "index_price": "70000"
      }
    ]
    

##  List all expiration dates

GET`/options/expirations`

GET `/options/expirations`

_List all expiration dates_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Underlying (Obtained by listing underlying endpoint)  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List expiration dates for specified underlying

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List expiration dates for specified underlying | [integer]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» _None_ | integer(int64) | Unix timestamp of expiration date  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/expirations'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/expirations?underlying=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      1637913600
    ]
    

##  List all contracts for specified underlying and expiration date

GET`/options/contracts`

GET `/options/contracts`

_List all contracts for specified underlying and expiration date_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Underlying (Obtained by listing underlying endpoint)  
expiration | query | integer(int64) | Optional | Unix timestamp of expiration date  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsContract]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Options contract details]  
» _None_ | OptionsContract | Options contract details  
»» name | string | Options contract name  
»» tag | string | Expiry periods include day, week, and month.  
»» create_time | number(double) | Created time  
»» expiration_time | number(double) | Expiration time  
»» is_call | boolean | `true` means call options, `false` means put options  
»» multiplier | string | The option contract multiplier indicates how many units of the underlying asset the face value of one contract represents.  
»» underlying | string | Underlying  
»» underlying_price | string | The forward futures price corresponding to the delivery date  
»» last_price | string | Last trading price  
»» mark_price | string | Current mark price (quote currency)  
»» index_price | string | Current index price (quote currency)  
»» maker_fee_rate | string | Maker fee rate, negative values indicate rebates  
»» taker_fee_rate | string | Taker fee rate  
»» order_price_round | string | Minimum order price increment  
»» mark_price_round | string | Minimum mark price increment  
»» order_size_min | integer(int64) | Minimum order size allowed by the contract  
»» order_size_max | integer(int64) | Maximum order size allowed by the contract  
»» order_price_deviate | string | Deprecated  
»» ref_discount_rate | string | Trading fee discount for referred users  
»» ref_rebate_rate | string | Commission rate for referrers  
»» orderbook_id | integer(int64) | Orderbook update ID  
»» trade_id | integer(int64) | Deprecated  
»» trade_size | integer(int64) | Historical cumulative trading volume  
»» position_size | integer(int64) | Current total long position size  
»» orders_limit | integer | The maximum number of open orders each user can place in this order book.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/contracts'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/contracts?underlying=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "name": "BTC_USDT-20211130-65000-C",
        "tag": "WEEK",
        "create_time": 1636702700,
        "expiration_time": 1637913600,
        "is_call": true,
        "strike_price": "65000",
        "last_price": "13000",
        "mark_price": "14010",
        "orderbook_id": 9,
        "trade_id": 1,
        "trade_size": 10,
        "position_size": 10,
        "underlying": "BTC_USDT",
        "underlying_price": "70000",
        "multiplier": "0.0001",
        "order_price_round": "0.1",
        "mark_price_round": "0.1",
        "maker_fee_rate": "0.0004",
        "taker_fee_rate": "0.0004",
        "price_limit_fee_rate": "0.1",
        "ref_discount_rate": "0",
        "ref_rebate_rate": "0",
        "order_price_deviate": "0.5",
        "order_size_min": 1,
        "order_size_max": 100000,
        "orders_limit": 50
      }
    ]
    

##  Query specified contract details

GET`/options/contracts/{contract}`

GET `/options/contracts/{contract}`

_Query specified contract details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | path | string | Required | none  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OptionsContract  
  
### Response Schema

Status Code **200**

_Options contract details_

Name | Type | Description  
---|---|---  
» name | string | Options contract name  
» tag | string | Expiry periods include day, week, and month.  
» create_time | number(double) | Created time  
» expiration_time | number(double) | Expiration time  
» is_call | boolean | `true` means call options, `false` means put options  
» multiplier | string | The option contract multiplier indicates how many units of the underlying asset the face value of one contract represents.  
» underlying | string | Underlying  
» underlying_price | string | The forward futures price corresponding to the delivery date  
» last_price | string | Last trading price  
» mark_price | string | Current mark price (quote currency)  
» index_price | string | Current index price (quote currency)  
» maker_fee_rate | string | Maker fee rate, negative values indicate rebates  
» taker_fee_rate | string | Taker fee rate  
» order_price_round | string | Minimum order price increment  
» mark_price_round | string | Minimum mark price increment  
» order_size_min | integer(int64) | Minimum order size allowed by the contract  
» order_size_max | integer(int64) | Maximum order size allowed by the contract  
» order_price_deviate | string | Deprecated  
» ref_discount_rate | string | Trading fee discount for referred users  
» ref_rebate_rate | string | Commission rate for referrers  
» orderbook_id | integer(int64) | Orderbook update ID  
» trade_id | integer(int64) | Deprecated  
» trade_size | integer(int64) | Historical cumulative trading volume  
» position_size | integer(int64) | Current total long position size  
» orders_limit | integer | The maximum number of open orders each user can place in this order book.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/contracts/BTC_USDT-20211130-65000-C'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/contracts/BTC_USDT-20211130-65000-C \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "name": "BTC_USDT-20211130-65000-C",
      "tag": "WEEK",
      "create_time": 1636702700,
      "expiration_time": 1637913600,
      "is_call": true,
      "strike_price": "65000",
      "last_price": "13000",
      "mark_price": "14010",
      "orderbook_id": 9,
      "trade_id": 1,
      "trade_size": 10,
      "position_size": 10,
      "underlying": "BTC_USDT",
      "underlying_price": "70000",
      "multiplier": "0.0001",
      "order_price_round": "0.1",
      "mark_price_round": "0.1",
      "maker_fee_rate": "0.0004",
      "taker_fee_rate": "0.0004",
      "price_limit_fee_rate": "0.1",
      "ref_discount_rate": "0",
      "ref_rebate_rate": "0",
      "order_price_deviate": "0.5",
      "order_size_min": 1,
      "order_size_max": 100000,
      "orders_limit": 50
    }
    

##  List settlement history

GET`/options/settlements`

GET `/options/settlements`

_List settlement history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Underlying (Obtained by listing underlying endpoint)  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsSettlement]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | number(double) | Last configuration update time  
» contract | string | Options contract name  
» profit | string | Settlement profit per contract (quote currency)  
» fee | string | Settlement fee per contract (quote currency)  
» strike_price | string | Strike price (quote currency)  
» settle_price | string | Settlement price (quote currency)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/settlements'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/settlements?underlying=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "time": 1598839200,
        "profit": "312.35",
        "fee": "0.3284",
        "settle_price": "11687.65",
        "contract": "BTC-WEEKLY-200824-11000-P",
        "strike_price": "12000"
      }
    ]
    

##  Get specified contract settlement information

GET`/options/settlements/{contract}`

GET `/options/settlements/{contract}`

Get `specified contract settlement information`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | path | string | Required | none  
underlying | query | string | Required | Underlying (Obtained by listing underlying endpoint)  
at | query | integer(int64) | Required | none  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OptionsSettlement  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» time | number(double) | Last configuration update time  
» contract | string | Options contract name  
» profit | string | Settlement profit per contract (quote currency)  
» fee | string | Settlement fee per contract (quote currency)  
» strike_price | string | Strike price (quote currency)  
» settle_price | string | Settlement price (quote currency)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/settlements/BTC_USDT-20211130-65000-C'
    query_param = 'underlying=BTC_USDT&at=0'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/settlements/BTC_USDT-20211130-65000-C?underlying=BTC_USDT&at=0 \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "time": 1598839200,
      "profit": "312.35",
      "fee": "0.3284",
      "settle_price": "11687.65",
      "contract": "BTC-WEEKLY-200824-11000-P",
      "strike_price": "12000"
    }
    

##  Query personal settlement records🔒 Authenticated

GET`/options/my_settlements`

GET `/options/my_settlements`

_Query personal settlement records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Underlying (Obtained by listing underlying endpoint)  
contract | query | string | Optional | Options contract name  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsMySettlements]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | number(double) | Settlement time  
» underlying | string | Underlying  
» contract | string | Options contract name  
» strike_price | string | Strike price (quote currency)  
» settle_price | string | Settlement price (quote currency)  
» size | integer(int64) | Settlement size  
» settle_profit | string | Settlement profit (quote currency)  
» fee | string | Settlement fee (quote currency)  
» realised_pnl | string | Accumulated profit and loss from opening positions, including premium, fees, settlement profit, etc. (quote currency)  
  
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
    
    url = '/options/my_settlements'
    query_param = 'underlying=BTC_USDT'
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
    url="/options/my_settlements"
    query_param="underlying=BTC_USDT"
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
    
    
    [
      {
        "size": -1,
        "settle_profit": "0",
        "contract": "BTC_USDT-20220624-26000-C",
        "strike_price": "26000",
        "time": 1656057600,
        "settle_price": "20917.461281337048",
        "underlying": "BTC_USDT",
        "realised_pnl": "-0.00116042",
        "fee": "0"
      }
    ]
    

##  Query options contract order book

GET`/options/order_book`

GET `/options/order_book`

_Query options contract order book_

Bids will be sorted by price from high to low, while asks sorted reversely

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Required | Options contract name  
interval | query | string | Optional | Price precision for merged depth. 0 means no merging. If not specified, defaults to 0  
limit | query | integer | Optional | Number of depth levels  
with_id | query | boolean | Optional | Whether to return depth update ID. This ID increments by 1 each time the depth changes  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
interval | 0  
interval | 0.1  
interval | 0.01  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Depth query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Depth query successful | OptionsOrderBook  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» id | integer(int64) | Order Book ID. Increases by 1 on every order book change. Set `with_id=true` to include this field in response  
» current | number(double) | Response data generation timestamp  
» update | number(double) | Order book changed timestamp  
» asks | array | Ask Depth  
»» options_order_book_item | object | none  
»»» p | string | Price (quote currency)  
»»» s | integer(int64) | Size  
»» bids | array | Bid Depth  
»»» options_order_book_item | object | none  
»»»» p | string | Price (quote currency)  
»»»» s | integer(int64) | Size  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/order_book'
    query_param = 'contract=BTC_USDT-20210916-5000-C'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/order_book?contract=BTC_USDT-20210916-5000-C \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "id": 123456,
      "current": 1623898993.123,
      "update": 1623898993.121,
      "asks": [
        {
          "p": "1.52",
          "s": 100
        },
        {
          "p": "1.53",
          "s": 40
        }
      ],
      "bids": [
        {
          "p": "1.17",
          "s": 150
        },
        {
          "p": "1.16",
          "s": 203
        }
      ]
    }
    

##  Query options market ticker information

GET`/options/tickers`

GET `/options/tickers`

_Query options market ticker information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Underlying (Obtained by listing underlying endpoint)  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [OptionsTicker]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Options contract details]  
» _None_ | OptionsTicker | Options contract details  
»» name | string | Options contract name  
»» last_price | string | Last trade price (quote currency)  
»» mark_price | string | Current mark price (quote currency)  
»» index_price | string | Current index price (quote currency)  
»» ask1_size | integer(int64) | Best ask size  
»» ask1_price | string | Best ask price  
»» bid1_size | integer(int64) | Best bid size  
»» bid1_price | string | Best bid price  
»» position_size | integer(int64) | Current total long position size  
»» mark_iv | string | Implied volatility  
»» bid_iv | string | Bid side implied volatility  
»» ask_iv | string | Ask side implied volatility  
»» leverage | string | Leverage = underlying_price / (mark_price * delta). This value is for reference only.  
»» delta | string | Greek letter delta  
»» gamma | string | Greek letter gamma  
»» vega | string | Greek letter vega  
»» theta | string | Greek letter theta  
»» rho | string | Rho  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/tickers'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/tickers?underlying=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "name": "BTC_USDT-20211130-65000-C",
        "last_price": "13000",
        "mark_price": "14010",
        "position_size": 10,
        "ask1_size": 0,
        "ask1_price": "0",
        "bid1_size": 1,
        "bid1_price": "11",
        "vega": "41.41202",
        "theta": "-120.1506",
        "rho": "6.52485",
        "gamma": "0.00004",
        "delta": "0.33505",
        "mark_iv": "0.123",
        "bid_iv": "0.023",
        "ask_iv": "0.342",
        "leverage": "13"
      }
    ]
    

##  Query underlying ticker information

GET`/options/underlying/tickers/{underlying}`

GET `/options/underlying/tickers/{underlying}`

_Query underlying ticker information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | path | string | Required | Underlying  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OptionsUnderlyingTicker  
  
### Response Schema

Status Code **200**

_Options underlying detail_

Name | Type | Description  
---|---|---  
» trade_put | integer(int64) | Total put options trades amount in last 24h  
» trade_call | integer(int64) | Total call options trades amount in last 24h  
» index_price | string | Index price (quote currency)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/underlying/tickers/BTC_USDT'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/underlying/tickers/BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "trade_put": 33505,
      "trade_call": 123,
      "index_price": "76543.3"
    }
    

##  Options contract market candlestick chart

GET`/options/candlesticks`

GET `/options/candlesticks`

_Options contract market candlestick chart_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Required | Options contract name  
limit | query | integer | Optional | Maximum number of records returned in a single list  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
interval | query | string | Optional | Time interval between data points  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [OptionsCandlestick]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [data point in every timestamp]  
» _None_ | OptionsCandlestick | data point in every timestamp  
»» t | number(double) | Unix timestamp in seconds  
»» v | integer(int64) | size volume (contract size). Only returned if `contract` is not prefixed  
»» c | string | Close price (quote currency, unit: underlying corresponding option price)  
»» h | string | Highest price (quote currency, unit: underlying corresponding option price)  
»» l | string | Lowest price (quote currency, unit: underlying corresponding option price)  
»» o | string | Open price (quote currency, unit: underlying corresponding option price)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/candlesticks'
    query_param = 'contract=BTC_USDT-20210916-5000-C'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/candlesticks?contract=BTC_USDT-20210916-5000-C \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "t": 1539852480,
        "v": 97151,
        "c": "1.032",
        "h": "1.032",
        "l": "1.032",
        "o": "1.032"
      }
    ]
    

##  Underlying index price candlestick chart

GET`/options/underlying/candlesticks`

GET `/options/underlying/candlesticks`

_Underlying index price candlestick chart_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Underlying (Obtained by listing underlying endpoint)  
limit | query | integer | Optional | Maximum number of records returned in a single list  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
interval | query | string | Optional | Time interval between data points  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [OptionsCandlestick]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [data point in every timestamp]  
» _None_ | OptionsCandlestick | data point in every timestamp  
»» t | number(double) | Unix timestamp in seconds  
»» v | integer(int64) | size volume (contract size). Only returned if `contract` is not prefixed  
»» c | string | Close price (quote currency, unit: underlying corresponding option price)  
»» h | string | Highest price (quote currency, unit: underlying corresponding option price)  
»» l | string | Lowest price (quote currency, unit: underlying corresponding option price)  
»» o | string | Open price (quote currency, unit: underlying corresponding option price)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/underlying/candlesticks'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/underlying/candlesticks?underlying=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "t": 1539852480,
        "v": 97151,
        "c": "1.032",
        "h": "1.032",
        "l": "1.032",
        "o": "1.032"
      }
    ]
    

##  Market trade records

GET`/options/trades`

GET `/options/trades`

_Market trade records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Optional | Options contract name  
type | query | string(P) | Optional | `C` for call, `P` for put  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsTrade]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int64) | Fill ID  
» create_time | integer(int64) | Fill Time  
» contract | string | Options contract name  
» size | integer(int64) | Trading size  
» price | string | Transaction Price (Quoted Currency, Unit: Underlying Option Price)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/trades'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/trades \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": 121234231,
        "create_time": 1514764800,
        "contract": "BTC_USDT-20211130-65000-C",
        "size": 100,
        "price": "1.032"
      }
    ]
    

##  Query account information🔒 Authenticated

GET`/options/accounts`

GET `/options/accounts`

_Query account information_

Query account information for classic option account and unified account

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OptionsAccount  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» total | string | Account balance, invalid for unified account  
» position_value | string | Position value, long position value is positive, short position value is negative  
» equity | string | Account equity = balance + option position value, invalid for unified account  
» short_enabled | boolean | If the account is allowed to short  
» mmp_enabled | boolean | Whether to enable MMP  
» liq_triggered | boolean | Whether the account is in a liquidation state  
» margin_mode | integer(int32) | This field indicates the margin mode used by the unified account:  
  
\- 0: Classic Spot Margin Mode  
\- 1: Cross-Currency Margin Mode  
\- 2: Portfolio Margin Mode  
\- 3: Single-Currency Margin Mode  
» unrealised_pnl | string | Unrealised PnL = (mark price - entry price) * position size. For long postion, size is positive; for short positon, size is negative.This value is for reference only.  
» init_margin | string | Initial position margin  
» maint_margin | string | Position maintenance margin  
» order_margin | string | Order margin of unfinished orders  
» ask_order_margin | string | Margin for outstanding sell orders  
» bid_order_margin | string | Margin for outstanding buy orders  
» available | string | Available balance to transfer out or trade  
» point | string | Point card amount  
» currency | string | Settlement currency  
» orders_limit | integer(int32) | Maximum number of outstanding orders  
» position_notional_limit | integer(int64) | Notional value upper limit, including the nominal value of positions and outstanding orders  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
  
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
    
    url = '/options/accounts'
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
    url="/options/accounts"
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
      "user": 666,
      "currency": "USDT",
      "short_enabled": true,
      "mmp_enabled": false,
      "liq_triggered": false,
      "margin_mode": 0,
      "total": "1650.443022",
      "position_value": "-40.1136",
      "equity": "1610.329422",
      "unrealised_pnl": "-0.7811",
      "init_margin": "0",
      "maint_margin": "135.541485",
      "order_margin": "139.74496",
      "ask_order_margin": "139.74496",
      "bid_order_margin": "0",
      "available": "1514.901537",
      "point": "0",
      "orders_limit": 10,
      "position_notional_limit": 1000000
    }
    

##  Query account change history🔒 Authenticated

GET`/options/account_book`

GET `/options/account_book`

_Query account change history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
type | query | string | Optional | Change types:  
\- dnw: Deposit & Withdrawal  
\- prem: Trading premium  
\- fee: Trading fee  
\- refr: Referrer rebate  
\- set: Settlement P&L  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

**type** : Change types:  
\- dnw: Deposit & Withdrawal  
\- prem: Trading premium  
\- fee: Trading fee  
\- refr: Referrer rebate  
\- set: Settlement P&L

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | dnw  
type | prem  
type | fee  
type | refr  
type | set  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsAccountBook]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | number(double) | Change time  
» change | string | Amount changed (USDT)  
» balance | string | Account total balance after change (USDT)  
» type | string | Changing Type:  
\- dnw: Deposit & Withdraw  
\- prem: Trading premium  
\- fee: Trading fee  
\- refr: Referrer rebate  
\- point_dnw: point_fee: POINT Trading fee  
\- point_refr: POINT Referrer rebate  
» text | string | Remark  
  
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
    
    url = '/options/account_book'
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
    url="/options/account_book"
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
    
    
    [
      {
        "time": 1636426005,
        "change": "-0.16",
        "balance": "7378.189",
        "text": "BTC_USDT-20211216-5000-P:25",
        "type": "fee"
      }
    ]
    

##  List user's positions of specified underlying🔒 Authenticated

GET`/options/positions`

GET `/options/positions`

_List user's positions of specified underlying_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Optional | Underlying  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsPosition]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Options contract position details]  
» _None_ | OptionsPosition | Options contract position details  
»» user | integer | User ID  
»» underlying | string | Underlying  
»» underlying_price | string | The forward futures price corresponding to the delivery date  
»» contract | string | Options contract name  
»» size | integer(int64) | Position size (contract quantity)  
»» entry_price | string | Entry size (quote currency)  
»» mark_price | string | Current mark price (quote currency)  
»» mark_iv | string | Implied volatility  
»» realised_pnl | string | Realized PnL  
»» unrealised_pnl | string | Unrealised PnL = (mark price - entry price) * position size. For long postion, size is positive; for short positon, size is negative.This value is for reference only.  
»» pending_orders | integer | Current pending order quantity  
»» close_order | object|null | Current close order information, or `null` if no close order  
»»» id | integer(int64) | Order ID  
»»» price | string | Order price (quote currency)  
»»» is_liq | boolean | Whether the close order is from liquidation  
»» delta | string | Greek letter delta  
»» gamma | string | Greek letter gamma  
»» vega | string | Greek letter vega  
»» theta | string | Greek letter theta  
  
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
    
    url = '/options/positions'
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
    url="/options/positions"
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
    
    
    [
      {
        "user": 11027586,
        "underlying": "BTC_USDT",
        "underlying_price": "70000",
        "contract": "BTC_USDT-20211216-5000-P",
        "size": 10,
        "entry_price": "1234",
        "realised_pnl": "120",
        "mark_price": "6000",
        "mark_iv": "0.9638",
        "unrealised_pnl": "-320",
        "pending_orders": 1,
        "close_order": {
          "id": 232323,
          "price": "5779",
          "is_liq": false
        },
        "delta": "-0.0046",
        "gamma": "0",
        "vega": "2.87656",
        "theta": "-1.00247"
      }
    ]
    

##  Get specified contract position🔒 Authenticated

GET`/options/positions/{contract}`

GET `/options/positions/{contract}`

Get `specified contract position`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | path | string | Required | none  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OptionsPosition  
  
### Response Schema

Status Code **200**

_Options contract position details_

Name | Type | Description  
---|---|---  
» user | integer | User ID  
» underlying | string | Underlying  
» underlying_price | string | The forward futures price corresponding to the delivery date  
» contract | string | Options contract name  
» size | integer(int64) | Position size (contract quantity)  
» entry_price | string | Entry size (quote currency)  
» mark_price | string | Current mark price (quote currency)  
» mark_iv | string | Implied volatility  
» realised_pnl | string | Realized PnL  
» unrealised_pnl | string | Unrealised PnL = (mark price - entry price) * position size. For long postion, size is positive; for short positon, size is negative.This value is for reference only.  
» pending_orders | integer | Current pending order quantity  
» close_order | object|null | Current close order information, or `null` if no close order  
»» id | integer(int64) | Order ID  
»» price | string | Order price (quote currency)  
»» is_liq | boolean | Whether the close order is from liquidation  
» delta | string | Greek letter delta  
» gamma | string | Greek letter gamma  
» vega | string | Greek letter vega  
» theta | string | Greek letter theta  
  
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
    
    url = '/options/positions/BTC_USDT-20211130-65000-C'
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
    url="/options/positions/BTC_USDT-20211130-65000-C"
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
      "user": 11027586,
      "underlying": "BTC_USDT",
      "underlying_price": "70000",
      "contract": "BTC_USDT-20211216-5000-P",
      "size": 10,
      "entry_price": "1234",
      "realised_pnl": "120",
      "mark_price": "6000",
      "mark_iv": "0.9638",
      "unrealised_pnl": "-320",
      "pending_orders": 1,
      "close_order": {
        "id": 232323,
        "price": "5779",
        "is_liq": false
      },
      "delta": "-0.0046",
      "gamma": "0",
      "vega": "2.87656",
      "theta": "-1.00247"
    }
    

##  List user's liquidation history of specified underlying🔒 Authenticated

GET`/options/position_close`

GET `/options/position_close`

_List user's liquidation history of specified underlying_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Underlying (Obtained by listing underlying endpoint)  
contract | query | string | Optional | Options contract name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsPositionClose]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | number(double) | Position close time  
» contract | string | Options contract name  
» side | string | Position side  
  
\- `long`: Long position  
\- `short`: Short position  
» pnl | string | PnL  
» text | string | Source of close order. See `order.text` field for specific values  
» settle_size | string | Settlement size  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
side | long  
side | short  
  
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
    
    url = '/options/position_close'
    query_param = 'underlying=BTC_USDT'
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
    url="/options/position_close"
    query_param="underlying=BTC_USDT"
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
    
    
    [
      {
        "time": 1631764800,
        "pnl": "-42914.291",
        "settle_size": "-10001",
        "side": "short",
        "contract": "BTC_USDT-20210916-5000-C",
        "text": "settled"
      }
    ]
    

##  List options orders🔒 Authenticated

GET`/options/orders`

GET `/options/orders`

_List options orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Optional | Options contract name  
underlying | query | string | Optional | Underlying  
status | query | string | Required | Query order list based on status  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
status | open  
status | finished  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Options order details]  
» _None_ | OptionsOrder | Options order details  
»» id | integer(int64) | Options order ID  
»» user | integer | User ID  
»» create_time | number(double) | Creation time of order  
»» finish_time | number(double) | Order finished time. Not returned if order is open  
»» finish_as | string | Order finish reason:  
  
\- filled: Fully filled  
\- cancelled: User cancelled  
\- liquidated: Cancelled due to liquidation  
\- ioc: Not immediately fully filled due to IOC time-in-force setting  
\- auto_deleveraged: Cancelled due to auto-deleveraging  
\- reduce_only: Cancelled due to position increase while reduce-only is set  
\- position_closed: Cancelled because the position was closed  
\- reduce_out: Only reduce positions by excluding hard-to-fill orders  
\- mmp_cancelled: Cancelled by MMP  
»» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
»» contract | string | Options identifier  
»» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
»» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
»» price | string | Order price. Price of 0 with `tif` set as `ioc` represents market order (quote currency)  
»» is_close | boolean | Is the order to close position  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_liq | boolean | Is the order for liquidation  
»» is_mmp | boolean | Whether it is an MMP order. Corresponds to `mmp` in the request  
»» tif | string | Time in force strategy. Market orders currently only support IOC mode  
  
\- gtc: Good Till Cancelled  
\- ioc: Immediate Or Cancelled, execute immediately or cancel, taker only  
\- poc: Pending Or Cancelled, passive order, maker only  
»» left | integer(int64) | Unfilled quantity  
»» fill_price | string | Fill price  
»» text | string | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- web: from web  
\- api: from API  
\- app: from mobile phones  
\- auto_deleveraging: from ADL  
\- liquidation: from liquidation  
\- insurance: from insurance  
»» tkfr | string | Taker fee  
»» mkfr | string | Maker fee  
»» refu | integer | Referrer user ID  
»» refr | string | Referrer rebate  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders'
    query_param = 'status=open'
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
    url="/options/orders"
    query_param="status=open"
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
    
    
    [
      {
        "status": "finished",
        "size": -1,
        "id": 2,
        "iceberg": 0,
        "is_liq": false,
        "is_close": false,
        "is_mmp": false,
        "contract": "BTC_USDT-20210916-5000-C",
        "text": "-",
        "fill_price": "100",
        "finish_as": "filled",
        "left": 0,
        "tif": "gtc",
        "is_reduce_only": false,
        "create_time": 1631763361,
        "finish_time": 1631763397,
        "price": "100"
      }
    ]
    

##  Create an options order🔒 Authenticated

POST`/options/orders`

POST `/options/orders`

_Create an options order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OptionsOrder | Required | none  
↳ contract | body | string | Required | Options identifier  
↳ size | body | integer(int64) | Required | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
↳ iceberg | body | integer(int64) | Optional | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
↳ price | body | string | Optional | Order price. Price of 0 with `tif` set as `ioc` represents market order (quote currency)  
↳ close | body | boolean | Optional | Set as `true` to close the position, with `size` set to 0  
↳ reduce_only | body | boolean | Optional | Set as `true` to be reduce-only order  
↳ mmp | body | boolean | Optional | When set to true, it is an MMP order  
↳ tif | body | string | Optional | Time in force strategy. Market orders currently only support IOC mode  
  
\- gtc: Good Till Cancelled  
\- ioc: Immediate Or Cancelled, execute immediately or cancel, taker only  
\- poc: Pending Or Cancelled, passive order, maker only  
↳ text | body | string | Optional | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- web: from web  
\- api: from API  
\- app: from mobile phones  
\- auto_deleveraging: from ADL  
\- liquidation: from liquidation  
\- insurance: from insurance  
  
####  Detailed descriptions

**» tif** : Time in force strategy. Market orders currently only support IOC mode  
  
\- gtc: Good Till Cancelled  
\- ioc: Immediate Or Cancelled, execute immediately or cancel, taker only  
\- poc: Pending Or Cancelled, passive order, maker only

**» text** : User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- web: from web  
\- api: from API  
\- app: from mobile phones  
\- auto_deleveraging: from ADL  
\- liquidation: from liquidation  
\- insurance: from insurance

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» tif | gtc  
» tif | ioc  
» tif | poc  
  
### Responses

  * 201[Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2)Order detail

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order detail | OptionsOrder  
  
### Response Schema

Status Code **201**

_Options order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Options order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
» finish_time | number(double) | Order finished time. Not returned if order is open  
» finish_as | string | Order finish reason:  
  
\- filled: Fully filled  
\- cancelled: User cancelled  
\- liquidated: Cancelled due to liquidation  
\- ioc: Not immediately fully filled due to IOC time-in-force setting  
\- auto_deleveraged: Cancelled due to auto-deleveraging  
\- reduce_only: Cancelled due to position increase while reduce-only is set  
\- position_closed: Cancelled because the position was closed  
\- reduce_out: Only reduce positions by excluding hard-to-fill orders  
\- mmp_cancelled: Cancelled by MMP  
» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
» contract | string | Options identifier  
» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Order price. Price of 0 with `tif` set as `ioc` represents market order (quote currency)  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» is_mmp | boolean | Whether it is an MMP order. Corresponds to `mmp` in the request  
» tif | string | Time in force strategy. Market orders currently only support IOC mode  
  
\- gtc: Good Till Cancelled  
\- ioc: Immediate Or Cancelled, execute immediately or cancel, taker only  
\- poc: Pending Or Cancelled, passive order, maker only  
» left | integer(int64) | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- web: from web  
\- api: from API  
\- app: from mobile phones  
\- auto_deleveraging: from ADL  
\- liquidation: from liquidation  
\- insurance: from insurance  
» tkfr | string | Taker fee  
» mkfr | string | Maker fee  
» refu | integer | Referrer user ID  
» refr | string | Referrer rebate  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders'
    query_param = ''
    body='{"size":-1,"iceberg":0,"contract":"BTC_USDT-20210916-5000-C","text":"-","tif":"gtc","price":"100"}'
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
    url="/options/orders"
    query_param=""
    body_param='{"size":-1,"iceberg":0,"contract":"BTC_USDT-20210916-5000-C","text":"-","tif":"gtc","price":"100"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "size": -1,
      "iceberg": 0,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "tif": "gtc",
      "price": "100"
    }
    

> Example responses

> 201 Response
    
    
    {
      "status": "finished",
      "size": -1,
      "id": 2,
      "iceberg": 0,
      "is_liq": false,
      "is_close": false,
      "is_mmp": false,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "fill_price": "100",
      "finish_as": "filled",
      "left": 0,
      "tif": "gtc",
      "is_reduce_only": false,
      "create_time": 1631763361,
      "finish_time": 1631763397,
      "price": "100"
    }
    

##  Cancel all orders with 'open' status🔒 Authenticated

DELETE`/options/orders`

DELETE `/options/orders`

_Cancel all orders with 'open' status_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Optional | Options contract name  
underlying | query | string | Optional | Underlying  
side | query | string | Optional | Specify all bids or all asks, both included if not specified  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | ask  
side | bid  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Batch cancellation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancellation successful | [OptionsOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Options order details]  
» _None_ | OptionsOrder | Options order details  
»» id | integer(int64) | Options order ID  
»» user | integer | User ID  
»» create_time | number(double) | Creation time of order  
»» finish_time | number(double) | Order finished time. Not returned if order is open  
»» finish_as | string | Order finish reason:  
  
\- filled: Fully filled  
\- cancelled: User cancelled  
\- liquidated: Cancelled due to liquidation  
\- ioc: Not immediately fully filled due to IOC time-in-force setting  
\- auto_deleveraged: Cancelled due to auto-deleveraging  
\- reduce_only: Cancelled due to position increase while reduce-only is set  
\- position_closed: Cancelled because the position was closed  
\- reduce_out: Only reduce positions by excluding hard-to-fill orders  
\- mmp_cancelled: Cancelled by MMP  
»» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
»» contract | string | Options identifier  
»» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
»» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
»» price | string | Order price. Price of 0 with `tif` set as `ioc` represents market order (quote currency)  
»» is_close | boolean | Is the order to close position  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_liq | boolean | Is the order for liquidation  
»» is_mmp | boolean | Whether it is an MMP order. Corresponds to `mmp` in the request  
»» tif | string | Time in force strategy. Market orders currently only support IOC mode  
  
\- gtc: Good Till Cancelled  
\- ioc: Immediate Or Cancelled, execute immediately or cancel, taker only  
\- poc: Pending Or Cancelled, passive order, maker only  
»» left | integer(int64) | Unfilled quantity  
»» fill_price | string | Fill price  
»» text | string | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- web: from web  
\- api: from API  
\- app: from mobile phones  
\- auto_deleveraging: from ADL  
\- liquidation: from liquidation  
\- insurance: from insurance  
»» tkfr | string | Taker fee  
»» mkfr | string | Maker fee  
»» refu | integer | Referrer user ID  
»» refr | string | Referrer rebate  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders'
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
    url="/options/orders"
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
    
    
    [
      {
        "status": "finished",
        "size": -1,
        "id": 2,
        "iceberg": 0,
        "is_liq": false,
        "is_close": false,
        "is_mmp": false,
        "contract": "BTC_USDT-20210916-5000-C",
        "text": "-",
        "fill_price": "100",
        "finish_as": "filled",
        "left": 0,
        "tif": "gtc",
        "is_reduce_only": false,
        "create_time": 1631763361,
        "finish_time": 1631763397,
        "price": "100"
      }
    ]
    

##  Query single order details🔒 Authenticated

GET`/options/orders/{order_id}`

GET `/options/orders/{order_id}`

_Query single order details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | integer(int64) | Required | Order ID returned when order is successfully created  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order detail

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order detail | OptionsOrder  
  
### Response Schema

Status Code **200**

_Options order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Options order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
» finish_time | number(double) | Order finished time. Not returned if order is open  
» finish_as | string | Order finish reason:  
  
\- filled: Fully filled  
\- cancelled: User cancelled  
\- liquidated: Cancelled due to liquidation  
\- ioc: Not immediately fully filled due to IOC time-in-force setting  
\- auto_deleveraged: Cancelled due to auto-deleveraging  
\- reduce_only: Cancelled due to position increase while reduce-only is set  
\- position_closed: Cancelled because the position was closed  
\- reduce_out: Only reduce positions by excluding hard-to-fill orders  
\- mmp_cancelled: Cancelled by MMP  
» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
» contract | string | Options identifier  
» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Order price. Price of 0 with `tif` set as `ioc` represents market order (quote currency)  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» is_mmp | boolean | Whether it is an MMP order. Corresponds to `mmp` in the request  
» tif | string | Time in force strategy. Market orders currently only support IOC mode  
  
\- gtc: Good Till Cancelled  
\- ioc: Immediate Or Cancelled, execute immediately or cancel, taker only  
\- poc: Pending Or Cancelled, passive order, maker only  
» left | integer(int64) | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- web: from web  
\- api: from API  
\- app: from mobile phones  
\- auto_deleveraging: from ADL  
\- liquidation: from liquidation  
\- insurance: from insurance  
» tkfr | string | Taker fee  
» mkfr | string | Maker fee  
» refu | integer | Referrer user ID  
» refr | string | Referrer rebate  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders/12345'
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
    url="/options/orders/12345"
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
      "status": "finished",
      "size": -1,
      "id": 2,
      "iceberg": 0,
      "is_liq": false,
      "is_close": false,
      "is_mmp": false,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "fill_price": "100",
      "finish_as": "filled",
      "left": 0,
      "tif": "gtc",
      "is_reduce_only": false,
      "create_time": 1631763361,
      "finish_time": 1631763397,
      "price": "100"
    }
    

##  Option Order Modification🔒 Authenticated

PUT`/options/orders/{order_id}`

PUT `/options/orders/{order_id}`

_Option Order Modification_

Modify the order price and/or quantity of a specified order; only orders with status 'open' are supported

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AmendOptionsOrderRequest | Required | none  
↳ contract | body | string | Required | Options contract name  
↳ price | body | string | Required | Order Price  
↳ size | body | integer(int64) | Required | Trade amount  
order_id | path | integer(int64) | Required | Order ID returned when order is successfully created  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order detail

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order detail | OptionsOrder  
  
### Response Schema

Status Code **200**

_Options order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Options order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
» finish_time | number(double) | Order finished time. Not returned if order is open  
» finish_as | string | Order finish reason:  
  
\- filled: Fully filled  
\- cancelled: User cancelled  
\- liquidated: Cancelled due to liquidation  
\- ioc: Not immediately fully filled due to IOC time-in-force setting  
\- auto_deleveraged: Cancelled due to auto-deleveraging  
\- reduce_only: Cancelled due to position increase while reduce-only is set  
\- position_closed: Cancelled because the position was closed  
\- reduce_out: Only reduce positions by excluding hard-to-fill orders  
\- mmp_cancelled: Cancelled by MMP  
» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
» contract | string | Options identifier  
» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Order price. Price of 0 with `tif` set as `ioc` represents market order (quote currency)  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» is_mmp | boolean | Whether it is an MMP order. Corresponds to `mmp` in the request  
» tif | string | Time in force strategy. Market orders currently only support IOC mode  
  
\- gtc: Good Till Cancelled  
\- ioc: Immediate Or Cancelled, execute immediately or cancel, taker only  
\- poc: Pending Or Cancelled, passive order, maker only  
» left | integer(int64) | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- web: from web  
\- api: from API  
\- app: from mobile phones  
\- auto_deleveraging: from ADL  
\- liquidation: from liquidation  
\- insurance: from insurance  
» tkfr | string | Taker fee  
» mkfr | string | Maker fee  
» refu | integer | Referrer user ID  
» refr | string | Referrer rebate  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders/12345'
    query_param = ''
    body='{"contract":"BTC_USDT-20260320-75000-C","price":"1661","size":10}'
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
    url="/options/orders/12345"
    query_param=""
    body_param='{"contract":"BTC_USDT-20260320-75000-C","price":"1661","size":10}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "contract": "BTC_USDT-20260320-75000-C",
      "price": "1661",
      "size": 10
    }
    

> Example responses

> 200 Response
    
    
    {
      "status": "finished",
      "size": -1,
      "id": 2,
      "iceberg": 0,
      "is_liq": false,
      "is_close": false,
      "is_mmp": false,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "fill_price": "100",
      "finish_as": "filled",
      "left": 0,
      "tif": "gtc",
      "is_reduce_only": false,
      "create_time": 1631763361,
      "finish_time": 1631763397,
      "price": "100"
    }
    

##  Cancel single order🔒 Authenticated

DELETE`/options/orders/{order_id}`

DELETE `/options/orders/{order_id}`

_Cancel single order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | integer(int64) | Required | Order ID returned when order is successfully created  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order detail

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order detail | OptionsOrder  
  
### Response Schema

Status Code **200**

_Options order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Options order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
» finish_time | number(double) | Order finished time. Not returned if order is open  
» finish_as | string | Order finish reason:  
  
\- filled: Fully filled  
\- cancelled: User cancelled  
\- liquidated: Cancelled due to liquidation  
\- ioc: Not immediately fully filled due to IOC time-in-force setting  
\- auto_deleveraged: Cancelled due to auto-deleveraging  
\- reduce_only: Cancelled due to position increase while reduce-only is set  
\- position_closed: Cancelled because the position was closed  
\- reduce_out: Only reduce positions by excluding hard-to-fill orders  
\- mmp_cancelled: Cancelled by MMP  
» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
» contract | string | Options identifier  
» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Order price. Price of 0 with `tif` set as `ioc` represents market order (quote currency)  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» is_mmp | boolean | Whether it is an MMP order. Corresponds to `mmp` in the request  
» tif | string | Time in force strategy. Market orders currently only support IOC mode  
  
\- gtc: Good Till Cancelled  
\- ioc: Immediate Or Cancelled, execute immediately or cancel, taker only  
\- poc: Pending Or Cancelled, passive order, maker only  
» left | integer(int64) | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- web: from web  
\- api: from API  
\- app: from mobile phones  
\- auto_deleveraging: from ADL  
\- liquidation: from liquidation  
\- insurance: from insurance  
» tkfr | string | Taker fee  
» mkfr | string | Maker fee  
» refu | integer | Referrer user ID  
» refr | string | Referrer rebate  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders/12345'
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
    url="/options/orders/12345"
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
      "status": "finished",
      "size": -1,
      "id": 2,
      "iceberg": 0,
      "is_liq": false,
      "is_close": false,
      "is_mmp": false,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "fill_price": "100",
      "finish_as": "filled",
      "left": 0,
      "tif": "gtc",
      "is_reduce_only": false,
      "create_time": 1631763361,
      "finish_time": 1631763397,
      "price": "100"
    }
    

##  Countdown cancel orders🔒 Authenticated

POST`/options/countdown_cancel_all`

POST `/options/countdown_cancel_all`

_Countdown cancel orders_

Option order heartbeat detection, when the `timeout` time set by the user is reached, if the existing countdown is not canceled or a new countdown is set, the related `option pending order` will be automatically canceled. This interface can be called repeatedly to set a new countdown or cancel the countdown. Usage example: Repeat this interface at intervals of 30 seconds, with each countdown `timeout` set to 30 (seconds). If this interface is not called again within 30 seconds, all pending orders on the `underlying` `contract` you specified will be automatically cancelled. If `underlying` `contract` is not specified, user will be automatically cancelled If `timeout` is set to 0 within 30 seconds, the countdown timer will expire and the automatic order cancellation function will be cancelled.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CountdownCancelAllOptionsTask | Required | none  
↳ timeout | body | integer(int32) | Required | Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown  
↳ contract | body | string | Optional | Options contract name  
↳ underlying | body | string | Optional | Underlying  
  
####  Detailed descriptions

**» timeout** : Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Countdown set successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Countdown set successfully | TriggerTime  
  
### Response Schema

Status Code **200**

_triggerTime_

Name | Type | Description  
---|---|---  
» triggerTime | integer(int64) | Timestamp when countdown ends, in milliseconds  
  
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
    
    url = '/options/countdown_cancel_all'
    query_param = ''
    body='{"timeout":30,"contract":"BTC_USDT-20241001-46000-C","underlying":"BTC_USDT"}'
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
    url="/options/countdown_cancel_all"
    query_param=""
    body_param='{"timeout":30,"contract":"BTC_USDT-20241001-46000-C","underlying":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "timeout": 30,
      "contract": "BTC_USDT-20241001-46000-C",
      "underlying": "BTC_USDT"
    }
    

> Example responses

> 200 Response
    
    
    {
      "triggerTime": "1660039145000"
    }
    

##  Query personal trading records🔒 Authenticated

GET`/options/my_trades`

GET `/options/my_trades`

_Query personal trading records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Required | Underlying (Obtained by listing underlying endpoint)  
contract | query | string | Optional | Options contract name  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OptionsMyTrade]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int64) | Fill ID  
» create_time | number(double) | Fill Time  
» contract | string | Options contract name  
» order_id | integer | Related order ID  
» size | integer(int64) | Trading size  
» price | string | Trade price (quote currency)  
» underlying_price | string | The forward futures price corresponding to the delivery date  
» role | string | Trade role. taker - taker, maker - maker  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
role | taker  
role | maker  
  
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
    
    url = '/options/my_trades'
    query_param = 'underlying=BTC_USDT'
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
    url="/options/my_trades"
    query_param="underlying=BTC_USDT"
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
    
    
    [
      {
        "underlying_price": "48000",
        "size": 1,
        "contract": "BTC_USDT-20210916-5000-C",
        "id": 1,
        "role": "taker",
        "create_time": 1631763397,
        "order_id": 4,
        "price": "100"
      }
    ]
    

##  MMP Query.🔒 Authenticated

GET`/options/mmp`

GET `/options/mmp`

_MMP Query._

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
underlying | query | string | Optional | Underlying  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [OptionsMMP]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [MMP Settings]  
» _None_ | OptionsMMP | MMP Settings  
»» underlying | string | Underlying  
»» window | integer(int32) | Time window (milliseconds), between 1-5000, 0 means disable MMP  
»» frozen_period | integer(int32) | Freeze duration (milliseconds), 0 means always frozen, need to call reset API to unfreeze  
»» qty_limit | string | Trading volume upper limit (positive number, up to 2 decimal places)  
»» delta_limit | string | Upper limit of net delta value (positive number, up to 2 decimal places)  
»» trigger_time_ms | integer(int64) | Trigger freeze time (milliseconds), 0 means no freeze is triggered  
»» frozen_until_ms | integer(int64) | Unfreeze time (milliseconds). If the freeze duration is not configured, there will be no unfreeze time after the freeze is triggered  
  
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
    
    url = '/options/mmp'
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
    url="/options/mmp"
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
    
    
    [
      {
        "underlying": "BTC_USDT",
        "window": 5000,
        "frozen_period": 200,
        "qty_limit": "10",
        "delta_limit": "10",
        "trigger_time_ms": 0,
        "frozen_until_ms": 0
      }
    ]
    

##  MMP Settings🔒 Authenticated

POST`/options/mmp`

POST `/options/mmp`

_MMP Settings_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OptionsMMP | Required | none  
↳ underlying | body | string | Required | Underlying  
↳ window | body | integer(int32) | Required | Time window (milliseconds), between 1-5000, 0 means disable MMP  
↳ frozen_period | body | integer(int32) | Required | Freeze duration (milliseconds), 0 means always frozen, need to call reset API to unfreeze  
↳ qty_limit | body | string | Required | Trading volume upper limit (positive number, up to 2 decimal places)  
↳ delta_limit | body | string | Required | Upper limit of net delta value (positive number, up to 2 decimal places)  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)MMP Information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | MMP Information | OptionsMMP  
  
### Response Schema

Status Code **200**

_MMP Settings_

Name | Type | Description  
---|---|---  
» underlying | string | Underlying  
» window | integer(int32) | Time window (milliseconds), between 1-5000, 0 means disable MMP  
» frozen_period | integer(int32) | Freeze duration (milliseconds), 0 means always frozen, need to call reset API to unfreeze  
» qty_limit | string | Trading volume upper limit (positive number, up to 2 decimal places)  
» delta_limit | string | Upper limit of net delta value (positive number, up to 2 decimal places)  
» trigger_time_ms | integer(int64) | Trigger freeze time (milliseconds), 0 means no freeze is triggered  
» frozen_until_ms | integer(int64) | Unfreeze time (milliseconds). If the freeze duration is not configured, there will be no unfreeze time after the freeze is triggered  
  
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
    
    url = '/options/mmp'
    query_param = ''
    body='{"underlying":"BTC_USDT","window":5000,"frozen_period":200,"qty_limit":"10","delta_limit":"10"}'
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
    url="/options/mmp"
    query_param=""
    body_param='{"underlying":"BTC_USDT","window":5000,"frozen_period":200,"qty_limit":"10","delta_limit":"10"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "underlying": "BTC_USDT",
      "window": 5000,
      "frozen_period": 200,
      "qty_limit": "10",
      "delta_limit": "10"
    }
    

> Example responses

> 200 Response
    
    
    {
      "underlying": "BTC_USDT",
      "window": 5000,
      "frozen_period": 200,
      "qty_limit": "10",
      "delta_limit": "10",
      "trigger_time_ms": 0,
      "frozen_until_ms": 0
    }
    

##  MMP Reset🔒 Authenticated

POST`/options/mmp/reset`

POST `/options/mmp/reset`

_MMP Reset_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OptionsMMPReset | Required | none  
↳ underlying | body | string | Required | Underlying  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)MMP Information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | MMP Information | OptionsMMP  
  
### Response Schema

Status Code **200**

_MMP Settings_

Name | Type | Description  
---|---|---  
» underlying | string | Underlying  
» window | integer(int32) | Time window (milliseconds), between 1-5000, 0 means disable MMP  
» frozen_period | integer(int32) | Freeze duration (milliseconds), 0 means always frozen, need to call reset API to unfreeze  
» qty_limit | string | Trading volume upper limit (positive number, up to 2 decimal places)  
» delta_limit | string | Upper limit of net delta value (positive number, up to 2 decimal places)  
» trigger_time_ms | integer(int64) | Trigger freeze time (milliseconds), 0 means no freeze is triggered  
» frozen_until_ms | integer(int64) | Unfreeze time (milliseconds). If the freeze duration is not configured, there will be no unfreeze time after the freeze is triggered  
  
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
    
    url = '/options/mmp/reset'
    query_param = ''
    body='{"underlying":"BTC_USDT"}'
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
    url="/options/mmp/reset"
    query_param=""
    body_param='{"underlying":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "underlying": "BTC_USDT"
    }
    

> Example responses

> 200 Response
    
    
    {
      "underlying": "BTC_USDT",
      "window": 5000,
      "frozen_period": 200,
      "qty_limit": "10",
      "delta_limit": "10",
      "trigger_time_ms": 0,
      "frozen_until_ms": 0
    }
    

#  Schemas

##  TriggerTime

_triggerTime_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
triggerTime | integer(int64) | Optional | none | Timestamp when countdown ends, in milliseconds  
      
    
    {
      "triggerTime": "1660039145000"
    }
    
    

##  OptionsOrder

_Options order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | read-only | Options order ID  
user | integer | Optional | read-only | User ID  
create_time | number(double) | Optional | read-only | Creation time of order  
finish_time | number(double) | Optional | read-only | Order finished time. Not returned if order is open  
finish_as | string | Optional | read-only | Order finish reason:  
  
\- filled: Fully filled  
\- cancelled: User cancelled  
\- liquidated: Cancelled due to liquidation  
\- ioc: Not immediately fully filled due to IOC time-in-force setting  
\- auto_deleveraged: Cancelled due to auto-deleveraging  
\- reduce_only: Cancelled due to position increase while reduce-only is set  
\- position_closed: Cancelled because the position was closed  
\- reduce_out: Only reduce positions by excluding hard-to-fill orders  
\- mmp_cancelled: Cancelled by MMP  
status | string | Optional | read-only | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required | none | Options identifier  
size | integer(int64) | Required | none | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | integer(int64) | Optional | none | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Optional | none | Order price. Price of 0 with `tif` set as `ioc` represents market order (quote currency)  
close | boolean | Optional | write-only | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | read-only | Is the order to close position  
reduce_only | boolean | Optional | write-only | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | read-only | Is the order reduce-only  
is_liq | boolean | Optional | read-only | Is the order for liquidation  
mmp | boolean | Optional | write-only | When set to true, it is an MMP order  
is_mmp | boolean | Optional | read-only | Whether it is an MMP order. Corresponds to `mmp` in the request  
tif | string | Optional | none | Time in force strategy. Market orders currently only support IOC mode  
  
\- gtc: Good Till Cancelled  
\- ioc: Immediate Or Cancelled, execute immediately or cancel, taker only  
\- poc: Pending Or Cancelled, passive order, maker only  
left | integer(int64) | Optional | read-only | Unfilled quantity  
fill_price | string | Optional | read-only | Fill price  
text | string | Optional | none | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- web: from web  
\- api: from API  
\- app: from mobile phones  
\- auto_deleveraging: from ADL  
\- liquidation: from liquidation  
\- insurance: from insurance  
tkfr | string | Optional | read-only | Taker fee  
mkfr | string | Optional | read-only | Maker fee  
refu | integer | Optional | read-only | Referrer user ID  
refr | string | Optional | read-only | Referrer rebate  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
      
    
    {
      "id": 0,
      "user": 0,
      "create_time": 0,
      "finish_time": 0,
      "finish_as": "filled",
      "status": "open",
      "contract": "string",
      "size": 0,
      "iceberg": 0,
      "price": "string",
      "close": false,
      "is_close": true,
      "reduce_only": false,
      "is_reduce_only": true,
      "is_liq": true,
      "mmp": false,
      "is_mmp": true,
      "tif": "gtc",
      "left": 0,
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "refr": "string"
    }
    
    

##  AmendOptionsOrderRequest

_AmendOptionsOrderRequest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contract | string | Required | none | Options contract name  
price | string | Required | none | Order Price  
size | integer(int64) | Required | none | Trade amount  
      
    
    {
      "contract": "string",
      "price": "string",
      "size": 0
    }
    
    

##  OptionsSettlement

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | number(double) | Optional | none | Last configuration update time  
contract | string | Optional | none | Options contract name  
profit | string | Optional | none | Settlement profit per contract (quote currency)  
fee | string | Optional | none | Settlement fee per contract (quote currency)  
strike_price | string | Optional | none | Strike price (quote currency)  
settle_price | string | Optional | none | Settlement price (quote currency)  
      
    
    {
      "time": 0,
      "contract": "string",
      "profit": "string",
      "fee": "string",
      "strike_price": "string",
      "settle_price": "string"
    }
    
    

##  OptionsTrade

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Fill ID  
create_time | integer(int64) | Optional | none | Fill Time  
contract | string | Optional | none | Options contract name  
size | integer(int64) | Optional | none | Trading size  
price | string | Optional | none | Transaction Price (Quoted Currency, Unit: Underlying Option Price)  
      
    
    {
      "id": 0,
      "create_time": 0,
      "contract": "string",
      "size": 0,
      "price": "string"
    }
    
    

##  OptionsMySettlements

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | number(double) | Optional | none | Settlement time  
underlying | string | Optional | none | Underlying  
contract | string | Optional | none | Options contract name  
strike_price | string | Optional | none | Strike price (quote currency)  
settle_price | string | Optional | none | Settlement price (quote currency)  
size | integer(int64) | Optional | none | Settlement size  
settle_profit | string | Optional | none | Settlement profit (quote currency)  
fee | string | Optional | none | Settlement fee (quote currency)  
realised_pnl | string | Optional | none | Accumulated profit and loss from opening positions, including premium, fees, settlement profit, etc. (quote currency)  
      
    
    {
      "time": 0,
      "underlying": "string",
      "contract": "string",
      "strike_price": "string",
      "settle_price": "string",
      "size": 0,
      "settle_profit": "string",
      "fee": "string",
      "realised_pnl": "string"
    }
    
    

##  OptionsUnderlying

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
name | string | Optional | none | Underlying name  
index_price | string | Optional | none | Spot index price (quote currency)  
      
    
    {
      "name": "string",
      "index_price": "string"
    }
    
    

##  OptionsOrderBook

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Order Book ID. Increases by 1 on every order book change. Set `with_id=true` to include this field in response  
current | number(double) | Optional | none | Response data generation timestamp  
update | number(double) | Optional | none | Order book changed timestamp  
asks | array | Required | none | Ask Depth  
↳ options_order_book_item | object | Optional | none | none  
↳ p | string | Optional | none | Price (quote currency)  
↳ s | integer(int64) | Optional | none | Size  
↳ bids | array | Required | none | Bid Depth  
↳ options_order_book_item | object | Optional | none | none  
↳ p | string | Optional | none | Price (quote currency)  
↳ s | integer(int64) | Optional | none | Size  
      
    
    {
      "id": 0,
      "current": 0,
      "update": 0,
      "asks": [
        {
          "p": "string",
          "s": 0
        }
      ],
      "bids": [
        {
          "p": "string",
          "s": 0
        }
      ]
    }
    
    

##  OptionsCandlestick

_data point in every timestamp_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
t | number(double) | Optional | none | Unix timestamp in seconds  
v | integer(int64) | Optional | none | size volume (contract size). Only returned if `contract` is not prefixed  
c | string | Optional | none | Close price (quote currency, unit: underlying corresponding option price)  
h | string | Optional | none | Highest price (quote currency, unit: underlying corresponding option price)  
l | string | Optional | none | Lowest price (quote currency, unit: underlying corresponding option price)  
o | string | Optional | none | Open price (quote currency, unit: underlying corresponding option price)  
      
    
    {
      "t": 0,
      "v": 0,
      "c": "string",
      "h": "string",
      "l": "string",
      "o": "string"
    }
    
    

##  OptionsTicker

_Options contract details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
name | string | Optional | none | Options contract name  
last_price | string | Optional | none | Last trade price (quote currency)  
mark_price | string | Optional | none | Current mark price (quote currency)  
index_price | string | Optional | none | Current index price (quote currency)  
ask1_size | integer(int64) | Optional | none | Best ask size  
ask1_price | string | Optional | none | Best ask price  
bid1_size | integer(int64) | Optional | none | Best bid size  
bid1_price | string | Optional | none | Best bid price  
position_size | integer(int64) | Optional | none | Current total long position size  
mark_iv | string | Optional | none | Implied volatility  
bid_iv | string | Optional | none | Bid side implied volatility  
ask_iv | string | Optional | none | Ask side implied volatility  
leverage | string | Optional | none | Leverage = underlying_price / (mark_price * delta). This value is for reference only.  
delta | string | Optional | none | Greek letter delta  
gamma | string | Optional | none | Greek letter gamma  
vega | string | Optional | none | Greek letter vega  
theta | string | Optional | none | Greek letter theta  
rho | string | Optional | none | Rho  
      
    
    {
      "name": "string",
      "last_price": "string",
      "mark_price": "string",
      "index_price": "string",
      "ask1_size": 0,
      "ask1_price": "string",
      "bid1_size": 0,
      "bid1_price": "string",
      "position_size": 0,
      "mark_iv": "string",
      "bid_iv": "string",
      "ask_iv": "string",
      "leverage": "string",
      "delta": "string",
      "gamma": "string",
      "vega": "string",
      "theta": "string",
      "rho": "string"
    }
    
    

##  OptionsPositionClose

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | number(double) | Optional | read-only | Position close time  
contract | string | Optional | read-only | Options contract name  
side | string | Optional | read-only | Position side  
  
\- `long`: Long position  
\- `short`: Short position  
pnl | string | Optional | read-only | PnL  
text | string | Optional | read-only | Source of close order. See `order.text` field for specific values  
settle_size | string | Optional | read-only | Settlement size  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
side | long  
side | short  
      
    
    {
      "time": 0,
      "contract": "string",
      "side": "long",
      "pnl": "string",
      "text": "string",
      "settle_size": "string"
    }
    
    

##  OptionsContract

_Options contract details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
name | string | Optional | none | Options contract name  
tag | string | Optional | none | Expiry periods include day, week, and month.  
create_time | number(double) | Optional | none | Created time  
expiration_time | number(double) | Optional | none | Expiration time  
is_call | boolean | Optional | none | `true` means call options, `false` means put options  
multiplier | string | Optional | none | The option contract multiplier indicates how many units of the underlying asset the face value of one contract represents.  
underlying | string | Optional | none | Underlying  
underlying_price | string | Optional | none | The forward futures price corresponding to the delivery date  
last_price | string | Optional | none | Last trading price  
mark_price | string | Optional | none | Current mark price (quote currency)  
index_price | string | Optional | none | Current index price (quote currency)  
maker_fee_rate | string | Optional | none | Maker fee rate, negative values indicate rebates  
taker_fee_rate | string | Optional | none | Taker fee rate  
order_price_round | string | Optional | none | Minimum order price increment  
mark_price_round | string | Optional | none | Minimum mark price increment  
order_size_min | integer(int64) | Optional | none | Minimum order size allowed by the contract  
order_size_max | integer(int64) | Optional | none | Maximum order size allowed by the contract  
order_price_deviate | string | Optional | none | Deprecated  
ref_discount_rate | string | Optional | none | Trading fee discount for referred users  
ref_rebate_rate | string | Optional | none | Commission rate for referrers  
orderbook_id | integer(int64) | Optional | none | Orderbook update ID  
trade_id | integer(int64) | Optional | none | Deprecated  
trade_size | integer(int64) | Optional | none | Historical cumulative trading volume  
position_size | integer(int64) | Optional | none | Current total long position size  
orders_limit | integer | Optional | none | The maximum number of open orders each user can place in this order book.  
      
    
    {
      "name": "string",
      "tag": "string",
      "create_time": 0,
      "expiration_time": 0,
      "is_call": true,
      "multiplier": "string",
      "underlying": "string",
      "underlying_price": "string",
      "last_price": "string",
      "mark_price": "string",
      "index_price": "string",
      "maker_fee_rate": "string",
      "taker_fee_rate": "string",
      "order_price_round": "string",
      "mark_price_round": "string",
      "order_size_min": 0,
      "order_size_max": 0,
      "order_price_deviate": "string",
      "ref_discount_rate": "string",
      "ref_rebate_rate": "string",
      "orderbook_id": 0,
      "trade_id": 0,
      "trade_size": 0,
      "position_size": 0,
      "orders_limit": 0
    }
    
    

##  OptionsMMP

_MMP Settings_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
underlying | string | Required | none | Underlying  
window | integer(int32) | Required | none | Time window (milliseconds), between 1-5000, 0 means disable MMP  
frozen_period | integer(int32) | Required | none | Freeze duration (milliseconds), 0 means always frozen, need to call reset API to unfreeze  
qty_limit | string | Required | none | Trading volume upper limit (positive number, up to 2 decimal places)  
delta_limit | string | Required | none | Upper limit of net delta value (positive number, up to 2 decimal places)  
trigger_time_ms | integer(int64) | Optional | read-only | Trigger freeze time (milliseconds), 0 means no freeze is triggered  
frozen_until_ms | integer(int64) | Optional | read-only | Unfreeze time (milliseconds). If the freeze duration is not configured, there will be no unfreeze time after the freeze is triggered  
      
    
    {
      "underlying": "string",
      "window": 0,
      "frozen_period": 0,
      "qty_limit": "string",
      "delta_limit": "string",
      "trigger_time_ms": 0,
      "frozen_until_ms": 0
    }
    
    

##  OptionsPosition

_Options contract position details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user | integer | Optional | read-only | User ID  
underlying | string | Optional | read-only | Underlying  
underlying_price | string | Optional | read-only | The forward futures price corresponding to the delivery date  
contract | string | Optional | read-only | Options contract name  
size | integer(int64) | Optional | read-only | Position size (contract quantity)  
entry_price | string | Optional | read-only | Entry size (quote currency)  
mark_price | string | Optional | read-only | Current mark price (quote currency)  
mark_iv | string | Optional | read-only | Implied volatility  
realised_pnl | string | Optional | read-only | Realized PnL  
unrealised_pnl | string | Optional | read-only | Unrealised PnL = (mark price - entry price) * position size. For long postion, size is positive; for short positon, size is negative.This value is for reference only.  
pending_orders | integer | Optional | read-only | Current pending order quantity  
close_order | object|null | Optional | read-only | Current close order information, or `null` if no close order  
↳ id | integer(int64) | Optional | none | Order ID  
↳ price | string | Optional | none | Order price (quote currency)  
↳ is_liq | boolean | Optional | none | Whether the close order is from liquidation  
delta | string | Optional | read-only | Greek letter delta  
gamma | string | Optional | read-only | Greek letter gamma  
vega | string | Optional | read-only | Greek letter vega  
theta | string | Optional | read-only | Greek letter theta  
      
    
    {
      "user": 0,
      "underlying": "string",
      "underlying_price": "string",
      "contract": "string",
      "size": 0,
      "entry_price": "string",
      "mark_price": "string",
      "mark_iv": "string",
      "realised_pnl": "string",
      "unrealised_pnl": "string",
      "pending_orders": 0,
      "close_order": {
        "id": 0,
        "price": "string",
        "is_liq": true
      },
      "delta": "string",
      "gamma": "string",
      "vega": "string",
      "theta": "string"
    }
    
    

##  OptionsAccountBook

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | number(double) | Optional | none | Change time  
change | string | Optional | none | Amount changed (USDT)  
balance | string | Optional | none | Account total balance after change (USDT)  
type | string | Optional | none | Changing Type:  
\- dnw: Deposit & Withdraw  
\- prem: Trading premium  
\- fee: Trading fee  
\- refr: Referrer rebate  
\- point_dnw: point_fee: POINT Trading fee  
\- point_refr: POINT Referrer rebate  
text | string | Optional | none | Remark  
      
    
    {
      "time": 0,
      "change": "string",
      "balance": "string",
      "type": "string",
      "text": "string"
    }
    
    

##  OptionsMMPReset

_MMP Reset_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
underlying | string | Required | none | Underlying  
window | integer(int32) | Optional | read-only | Time window (milliseconds), between 1-5000, 0 means disable MMP  
frozen_period | integer(int32) | Optional | read-only | Freeze duration (milliseconds), 0 means always frozen, need to call reset API to unfreeze  
qty_limit | string | Optional | read-only | Trading volume upper limit (positive number, up to 2 decimal places)  
delta_limit | string | Optional | read-only | Upper limit of net delta value (positive number, up to 2 decimal places)  
trigger_time_ms | integer(int64) | Optional | read-only | Trigger freeze time (milliseconds), 0 means no freeze is triggered  
frozen_until_ms | integer(int64) | Optional | read-only | Unfreeze time (milliseconds). If the freeze duration is not configured, there will be no unfreeze time after the freeze is triggered  
      
    
    {
      "underlying": "string",
      "window": 0,
      "frozen_period": 0,
      "qty_limit": "string",
      "delta_limit": "string",
      "trigger_time_ms": 0,
      "frozen_until_ms": 0
    }
    
    

##  CountdownCancelAllOptionsTask

_CountdownCancelAllOptionsTask_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timeout | integer(int32) | Required | none | Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown  
contract | string | Optional | none | Options contract name  
underlying | string | Optional | none | Underlying  
      
    
    {
      "timeout": 0,
      "contract": "string",
      "underlying": "string"
    }
    
    

##  OptionsUnderlyingTicker

_Options underlying detail_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
trade_put | integer(int64) | Optional | none | Total put options trades amount in last 24h  
trade_call | integer(int64) | Optional | none | Total call options trades amount in last 24h  
index_price | string | Optional | none | Index price (quote currency)  
      
    
    {
      "trade_put": 0,
      "trade_call": 0,
      "index_price": "string"
    }
    
    

##  OptionsAccount

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user | integer(int64) | Optional | none | User ID  
total | string | Optional | none | Account balance, invalid for unified account  
position_value | string | Optional | none | Position value, long position value is positive, short position value is negative  
equity | string | Optional | none | Account equity = balance + option position value, invalid for unified account  
short_enabled | boolean | Optional | none | If the account is allowed to short  
mmp_enabled | boolean | Optional | none | Whether to enable MMP  
liq_triggered | boolean | Optional | none | Whether the account is in a liquidation state  
margin_mode | integer(int32) | Optional | none | This field indicates the margin mode used by the unified account:  
  
\- 0: Classic Spot Margin Mode  
\- 1: Cross-Currency Margin Mode  
\- 2: Portfolio Margin Mode  
\- 3: Single-Currency Margin Mode  
unrealised_pnl | string | Optional | none | Unrealised PnL = (mark price - entry price) * position size. For long postion, size is positive; for short positon, size is negative.This value is for reference only.  
init_margin | string | Optional | none | Initial position margin  
maint_margin | string | Optional | none | Position maintenance margin  
order_margin | string | Optional | none | Order margin of unfinished orders  
ask_order_margin | string | Optional | none | Margin for outstanding sell orders  
bid_order_margin | string | Optional | none | Margin for outstanding buy orders  
available | string | Optional | none | Available balance to transfer out or trade  
point | string | Optional | none | Point card amount  
currency | string | Optional | none | Settlement currency  
orders_limit | integer(int32) | Optional | none | Maximum number of outstanding orders  
position_notional_limit | integer(int64) | Optional | none | Notional value upper limit, including the nominal value of positions and outstanding orders  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
      
    
    {
      "user": 0,
      "total": "string",
      "position_value": "string",
      "equity": "string",
      "short_enabled": true,
      "mmp_enabled": true,
      "liq_triggered": true,
      "margin_mode": 0,
      "unrealised_pnl": "string",
      "init_margin": "string",
      "maint_margin": "string",
      "order_margin": "string",
      "ask_order_margin": "string",
      "bid_order_margin": "string",
      "available": "string",
      "point": "string",
      "currency": "string",
      "orders_limit": 0,
      "position_notional_limit": 0
    }
    
    

##  OptionsMyTrade

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Fill ID  
create_time | number(double) | Optional | none | Fill Time  
contract | string | Optional | none | Options contract name  
order_id | integer | Optional | none | Related order ID  
size | integer(int64) | Optional | none | Trading size  
price | string | Optional | none | Trade price (quote currency)  
underlying_price | string | Optional | none | The forward futures price corresponding to the delivery date  
role | string | Optional | none | Trade role. taker - taker, maker - maker  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
role | taker  
role | maker  
      
    
    {
      "id": 0,
      "create_time": 0,
      "contract": "string",
      "order_id": 0,
      "size": 0,
      "price": "string",
      "underlying_price": "string",
      "role": "taker"
    }