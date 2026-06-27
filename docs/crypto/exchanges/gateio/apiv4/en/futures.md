---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/futures
api_type: Trading
updated_at: 2026-05-27 20:15:15.283860
---

# Futures

Perpetual futures

##  Query all futures contracts

GET`/futures/{settle}/contracts`

GET `/futures/{settle}/contracts`

_Query all futures contracts_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Contract]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures contract details]  
» _None_ | Contract | Futures contract details  
»» name | string | Futures contract  
»» type | string | Contract type: inverse - inverse contract, direct - direct contract  
»» quanto_multiplier | string | The contract multiplier indicates how many units of the underlying asset the face value of one contract represents.  
»» leverage_min | string | Minimum leverage  
»» leverage_max | string | Maximum leverage  
»» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
»» mark_type | string | Deprecated  
»» mark_price | string | Current mark price  
»» index_price | string | Current index price  
»» last_price | string | Last trading price  
»» maker_fee_rate | string | Maker fee rate, negative values indicate rebates  
»» taker_fee_rate | string | Taker fee rate  
»» order_price_round | string | Minimum order price increment  
»» mark_price_round | string | Minimum mark price increment  
»» funding_rate | string | Current funding rate  
»» funding_interval | integer | Funding application interval, unit in seconds  
»» funding_next_apply | number(double) | Next funding time  
»» risk_limit_base | string | Base risk limit (deprecated)  
»» interest_rate | string | Interest rate parameter used in funding rate and premium-related calculations for perpetual contracts. Returned as a string decimal ratio (e.g. `0.0003`), same convention as `funding_rate` (ratio, not percent).  
»» risk_limit_step | string | Risk limit adjustment step (deprecated)  
»» risk_limit_max | string | Maximum risk limit allowed by the contract (deprecated). It is recommended to use /futures/{settle}/risk_limit_tiers to query risk limits  
»» order_size_min | string | Minimum order size allowed by the contract  
»» enable_decimal | boolean | Whether decimal string type is supported for contract lot size. When this field is set to `true`, it indicates that the contract supports decimal lot sizes (i.e., the `size` field can use a decimal string type); when set to `false`, it indicates that the contract does not support decimal lot sizes (i.e., the `size` field can only use an integer type).  
»» order_size_max | string | Maximum order size allowed by the contract  
»» order_price_deviate | string | Maximum allowed deviation between order price and current mark price. The order price `order_price` must satisfy the following condition:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
»» ref_discount_rate | string | Trading fee discount for referred users  
»» ref_rebate_rate | string | Commission rate for referrers  
»» orderbook_id | integer(int64) | Orderbook update ID  
»» trade_id | integer(int64) | Current trade ID  
»» trade_size | string | Historical cumulative trading volume  
»» position_size | string | Current total long position size  
»» config_change_time | number(double) | Last configuration update time  
»» in_delisting | boolean | `in_delisting=true` and position_size>0 indicates the contract is in delisting transition period  
`in_delisting=true` and position_size=0 indicates the contract is delisted  
»» orders_limit | integer | Maximum number of pending orders  
»» enable_bonus | boolean | Whether bonus is enabled  
»» enable_credit | boolean | Whether portfolio margin account is enabled  
»» create_time | number(double) | Created time of the contract  
»» funding_cap_ratio | string | Deprecated  
»» status | string | Contract status types include: prelaunch (pre-launch), trading (active), delisting (delisting), delisted (delisted), circuit_breaker (circuit breaker)  
»» launch_time | integer(int64) | Contract expiry timestamp  
»» delisting_time | integer(int64) | Timestamp when contract enters reduce-only state  
»» delisted_time | integer(int64) | Contract delisting time  
»» market_order_slip_ratio | string | The maximum slippage allowed for market orders, with the slippage rate calculated based on the latest market price  
»» market_order_size_max | string | The maximum number of contracts supported for market orders, with a default value of 0. When the default value is used, the maximum number of contracts is limited by the `order_size_max` field  
»» funding_rate_limit | string | Upper and lower limits of funding rate  
»» contract_type | string | Contract classification type, e.g. stocks, metals, indices, forex, commodities, etc.  
»» funding_impact_value | string | Funding rate depth impact value  
»» enable_circuit_breaker | boolean | Whether the newly launched contract activates mark price circuit breaker (If the platform intends to activate this mechanism for a newly launched contract market to prevent significant price fluctuations and excessive liquidations after launch, an advance announcement will be made).  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | inverse  
type | direct  
mark_type | internal  
mark_type | index  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/contracts'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/contracts \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "name": "BTC_USDT",
        "type": "direct",
        "quanto_multiplier": "0.0001",
        "ref_discount_rate": "0",
        "order_price_deviate": "0.5",
        "maintenance_rate": "0.005",
        "mark_type": "index",
        "last_price": "38026",
        "mark_price": "37985.6",
        "index_price": "37954.92",
        "funding_rate_indicative": "0.000219",
        "mark_price_round": "0.01",
        "funding_offset": 0,
        "in_delisting": false,
        "risk_limit_base": "1000000",
        "interest_rate": "0.0003",
        "order_price_round": "0.1",
        "order_size_min": "1",
        "enable_decimal": false,
        "ref_rebate_rate": "0.2",
        "funding_interval": 28800,
        "risk_limit_step": "1000000",
        "leverage_min": "1",
        "leverage_max": "100",
        "risk_limit_max": "8000000",
        "maker_fee_rate": "-0.00025",
        "taker_fee_rate": "0.00075",
        "funding_rate": "0.002053",
        "order_size_max": "1000000",
        "funding_next_apply": 1610035200,
        "short_users": 977,
        "config_change_time": 1609899548,
        "trade_size": "28530850594",
        "position_size": "5223816",
        "long_users": 455,
        "funding_impact_value": "60000",
        "orders_limit": 50,
        "trade_id": 10851092,
        "orderbook_id": 2129638396,
        "enable_bonus": true,
        "enable_credit": true,
        "create_time": 1669688556,
        "funding_cap_ratio": "0.75",
        "status": "trading",
        "launch_time": 1609899548,
        "delisting_time": 1609899548,
        "delisted_time": 1609899548,
        "market_order_slip_ratio": "0.05",
        "market_order_size_max": "0",
        "funding_rate_limit": "0.003",
        "contract_type": "indices",
        "enable_circuit_breaker": false
      }
    ]
    

##  Query single contract information

GET`/futures/{settle}/contracts/{contract}`

GET `/futures/{settle}/contracts/{contract}`

_Query single contract information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Contract information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Contract information | Contract  
  
### Response Schema

Status Code **200**

_Futures contract details_

Name | Type | Description  
---|---|---  
» name | string | Futures contract  
» type | string | Contract type: inverse - inverse contract, direct - direct contract  
» quanto_multiplier | string | The contract multiplier indicates how many units of the underlying asset the face value of one contract represents.  
» leverage_min | string | Minimum leverage  
» leverage_max | string | Maximum leverage  
» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
» mark_type | string | Deprecated  
» mark_price | string | Current mark price  
» index_price | string | Current index price  
» last_price | string | Last trading price  
» maker_fee_rate | string | Maker fee rate, negative values indicate rebates  
» taker_fee_rate | string | Taker fee rate  
» order_price_round | string | Minimum order price increment  
» mark_price_round | string | Minimum mark price increment  
» funding_rate | string | Current funding rate  
» funding_interval | integer | Funding application interval, unit in seconds  
» funding_next_apply | number(double) | Next funding time  
» risk_limit_base | string | Base risk limit (deprecated)  
» interest_rate | string | Interest rate parameter used in funding rate and premium-related calculations for perpetual contracts. Returned as a string decimal ratio (e.g. `0.0003`), same convention as `funding_rate` (ratio, not percent).  
» risk_limit_step | string | Risk limit adjustment step (deprecated)  
» risk_limit_max | string | Maximum risk limit allowed by the contract (deprecated). It is recommended to use /futures/{settle}/risk_limit_tiers to query risk limits  
» order_size_min | string | Minimum order size allowed by the contract  
» enable_decimal | boolean | Whether decimal string type is supported for contract lot size. When this field is set to `true`, it indicates that the contract supports decimal lot sizes (i.e., the `size` field can use a decimal string type); when set to `false`, it indicates that the contract does not support decimal lot sizes (i.e., the `size` field can only use an integer type).  
» order_size_max | string | Maximum order size allowed by the contract  
» order_price_deviate | string | Maximum allowed deviation between order price and current mark price. The order price `order_price` must satisfy the following condition:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
» ref_discount_rate | string | Trading fee discount for referred users  
» ref_rebate_rate | string | Commission rate for referrers  
» orderbook_id | integer(int64) | Orderbook update ID  
» trade_id | integer(int64) | Current trade ID  
» trade_size | string | Historical cumulative trading volume  
» position_size | string | Current total long position size  
» config_change_time | number(double) | Last configuration update time  
» in_delisting | boolean | `in_delisting=true` and position_size>0 indicates the contract is in delisting transition period  
`in_delisting=true` and position_size=0 indicates the contract is delisted  
» orders_limit | integer | Maximum number of pending orders  
» enable_bonus | boolean | Whether bonus is enabled  
» enable_credit | boolean | Whether portfolio margin account is enabled  
» create_time | number(double) | Created time of the contract  
» funding_cap_ratio | string | Deprecated  
» status | string | Contract status types include: prelaunch (pre-launch), trading (active), delisting (delisting), delisted (delisted), circuit_breaker (circuit breaker)  
» launch_time | integer(int64) | Contract expiry timestamp  
» delisting_time | integer(int64) | Timestamp when contract enters reduce-only state  
» delisted_time | integer(int64) | Contract delisting time  
» market_order_slip_ratio | string | The maximum slippage allowed for market orders, with the slippage rate calculated based on the latest market price  
» market_order_size_max | string | The maximum number of contracts supported for market orders, with a default value of 0. When the default value is used, the maximum number of contracts is limited by the `order_size_max` field  
» funding_rate_limit | string | Upper and lower limits of funding rate  
» contract_type | string | Contract classification type, e.g. stocks, metals, indices, forex, commodities, etc.  
» funding_impact_value | string | Funding rate depth impact value  
» enable_circuit_breaker | boolean | Whether the newly launched contract activates mark price circuit breaker (If the platform intends to activate this mechanism for a newly launched contract market to prevent significant price fluctuations and excessive liquidations after launch, an advance announcement will be made).  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | inverse  
type | direct  
mark_type | internal  
mark_type | index  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/contracts/BTC_USDT'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/contracts/BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "name": "BTC_USDT",
      "type": "direct",
      "quanto_multiplier": "0.0001",
      "ref_discount_rate": "0",
      "order_price_deviate": "0.5",
      "maintenance_rate": "0.005",
      "mark_type": "index",
      "last_price": "38026",
      "mark_price": "37985.6",
      "index_price": "37954.92",
      "funding_rate_indicative": "0.000219",
      "mark_price_round": "0.01",
      "funding_offset": 0,
      "in_delisting": false,
      "risk_limit_base": "1000000",
      "interest_rate": "0.0003",
      "order_price_round": "0.1",
      "order_size_min": "1",
      "enable_decimal": false,
      "ref_rebate_rate": "0.2",
      "funding_interval": 28800,
      "risk_limit_step": "1000000",
      "leverage_min": "1",
      "leverage_max": "100",
      "risk_limit_max": "8000000",
      "maker_fee_rate": "-0.00025",
      "taker_fee_rate": "0.00075",
      "funding_rate": "0.002053",
      "order_size_max": "1000000",
      "funding_next_apply": 1610035200,
      "short_users": 977,
      "config_change_time": 1609899548,
      "trade_size": "28530850594",
      "position_size": "5223816",
      "long_users": 455,
      "funding_impact_value": "60000",
      "orders_limit": 50,
      "trade_id": 10851092,
      "orderbook_id": 2129638396,
      "enable_bonus": true,
      "enable_credit": true,
      "create_time": 1669688556,
      "funding_cap_ratio": "0.75",
      "status": "trading",
      "launch_time": 1609899548,
      "delisting_time": 1609899548,
      "delisted_time": 1609899548,
      "market_order_slip_ratio": "0.05",
      "market_order_size_max": "0",
      "funding_rate_limit": "0.003",
      "contract_type": "indices",
      "enable_circuit_breaker": false
    }
    

##  Query futures market depth information

GET`/futures/{settle}/order_book`

GET `/futures/{settle}/order_book`

_Query futures market depth information_

Bids will be sorted by price from high to low, while asks sorted reversely

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Required | Futures contract  
interval | query | string | Optional | Price precision for merged depth. 0 means no merging. If not specified, defaults to 0  
limit | query | integer | Optional | Number of depth levels  
with_id | query | boolean | Optional | Whether to return depth update ID. This ID increments by 1 each time the depth changes  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Depth query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Depth query successful | FuturesOrderBook  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» id | integer(int64) | Order Book ID. Increases by 1 on every order book change. Set `with_id=true` to include this field in response  
» current | number(double) | Response data generation timestamp  
» update | number(double) | Order book changed timestamp  
» asks | array | Ask Depth  
»» FuturesOrderBookItem | object | none  
»»» p | string | Price (quote currency)  
»»» s | string | Size  
»» bids | array | Bid Depth  
»»» FuturesOrderBookItem | object | none  
»»»» p | string | Price (quote currency)  
»»»» s | string | Size  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/order_book'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/order_book?contract=BTC_USDT \
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
          "s": "100"
        },
        {
          "p": "1.53",
          "s": "40"
        }
      ],
      "bids": [
        {
          "p": "1.17",
          "s": "150"
        },
        {
          "p": "1.16",
          "s": "203"
        }
      ]
    }
    

##  Futures market transaction records

GET`/futures/{settle}/trades`

GET `/futures/{settle}/trades`

_Futures market transaction records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Required | Futures contract  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
last_id | query | string | Optional | Specify the starting point for this list based on a previously retrieved id  
  
This parameter is deprecated. Use `from` and `to` instead to limit time range  
from | query | integer(int64) | Optional | Specify starting time in Unix seconds. If not specified, `to` and `limit` will be used to limit response items.  
If items between `from` and `to` are more than `limit`, only `limit` number will be returned.  
  
to | query | integer(int64) | Optional | Specify end time in Unix seconds, default to current time.  
  
####  Detailed descriptions

**last_id** : Specify the starting point for this list based on a previously retrieved id  
  
This parameter is deprecated. Use `from` and `to` instead to limit time range

**from** : Specify starting time in Unix seconds. If not specified, `to` and `limit` will be used to limit response items.  
If items between `from` and `to` are more than `limit`, only `limit` number will be returned.  

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FuturesTrade]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int64) | Fill ID  
» create_time | number(double) | Fill Time  
» create_time_ms | number(double) | Trade time, with millisecond precision to 3 decimal places  
» contract | string | Futures contract  
» size | string | Trading size  
» price | string | Trade price (quote currency)  
» is_internal | boolean | Deprecated  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/trades'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/trades?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": 121234231,
        "create_time": 1514764800,
        "contract": "BTC_USDT",
        "size": "-100",
        "price": "100.123"
      }
    ]
    

##  Futures market K-line chart

GET`/futures/{settle}/candlesticks`

GET `/futures/{settle}/candlesticks`

_Futures market K-line chart_

Return specified contract candlesticks. If prefix `contract` with `mark_`, the contract's mark price candlesticks are returned; if prefix with `index_`, index price candlesticks will be returned.

Maximum of 2000 points are returned in one query. Be sure not to exceed the limit when specifying `from`, `to` and `interval`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Required | Futures contract  
from | query | integer(int64) | Optional | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified  
to | query | integer(int64) | Optional | Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision  
limit | query | integer | Optional | Maximum number of recent data points to return. `limit` conflicts with `from` and `to`. If either `from` or `to` is specified, request will be rejected.  
interval | query | string | Optional | Time interval for data points. Note: 1w represents a natural week, 7d is aligned with Unix epoch time, 30d represents a natural month  
timezone | query | string | Optional | Time zone: all/utc0/utc8, default utc0  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
interval | 10s  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
interval | 4h  
interval | 8h  
interval | 1d  
interval | 7d  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [FuturesCandlestick]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [data point in every timestamp]  
» _None_ | FuturesCandlestick | data point in every timestamp  
»» t | number(double) | Unix timestamp in seconds  
»» v | string | size volume (contract size). Only returned if `contract` is not prefixed  
»» c | string | Close price (quote currency)  
»» h | string | Highest price (quote currency)  
»» l | string | Lowest price (quote currency)  
»» o | string | Open price (quote currency)  
»» sum | string | Trading volume (unit: Quote currency)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/candlesticks'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/candlesticks?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "t": 1539852480,
        "v": "97151",
        "c": "1.032",
        "h": "1.032",
        "l": "1.032",
        "o": "1.032",
        "sum": "3580"
      }
    ]
    

##  Premium Index K-line chart

GET`/futures/{settle}/premium_index`

GET `/futures/{settle}/premium_index`

_Premium Index K-line chart_

K-line chart data returns a maximum of 1000 points per request. When specifying from, to, and interval, ensure the number of points is not excessive

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Required | Futures contract  
from | query | integer(int64) | Optional | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified  
to | query | integer(int64) | Optional | Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision  
limit | query | integer | Optional | Maximum number of recent data points to return. `limit` conflicts with `from` and `to`. If either `from` or `to` is specified, request will be rejected.  
interval | query | string | Optional | Time interval between data points  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
interval | 4h  
interval | 8h  
interval | 1d  
interval | 7d  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [FuturesPremiumIndex]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [data point in every timestamp]  
» _None_ | FuturesPremiumIndex | data point in every timestamp  
»» t | number(double) | Unix timestamp in seconds  
»» c | string | Close price  
»» h | string | Highest price  
»» l | string | Lowest price  
»» o | string | Open price  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/premium_index'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/premium_index?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "t": 1539852480,
        "c": "0",
        "h": "0.00023",
        "l": "0",
        "o": "0"
      }
    ]
    

##  Get all futures trading statistics

GET`/futures/{settle}/tickers`

GET `/futures/{settle}/tickers`

Get `all futures trading statistics`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [FuturesTicker]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» contract | string | Futures contract  
» last | string | Last trading price  
» change_percentage | string | Price change percentage. Negative values indicate price decrease, e.g. -7.45  
» total_size | string | Contract total size  
» low_24h | string | 24-hour lowest price  
» high_24h | string | 24-hour highest price  
» volume_24h | string | 24-hour trading volume  
» volume_24h_btc | string | 24-hour trading volume in BTC (deprecated, use `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle` instead)  
» volume_24h_usd | string | 24-hour trading volume in USD (deprecated, use `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle` instead)  
» volume_24h_base | string | 24-hour trading volume in base currency  
» volume_24h_quote | string | 24-hour trading volume in quote currency  
» volume_24h_settle | string | 24-hour trading volume in settle currency  
» mark_price | string | Recent mark price  
» funding_rate | string | Funding rate  
» funding_rate_indicative | string | Indicative Funding rate in next period. (deprecated. use `funding_rate`)  
» index_price | string | Index price  
» quanto_base_rate | string | Deprecated  
» lowest_ask | string | Recent lowest ask  
» lowest_size | string | The latest seller's lowest price order quantity  
» highest_bid | string | Recent highest bid  
» highest_size | string | The latest buyer's highest price order volume  
» change_utc0 | string | Percentage change at utc0. Negative values indicate a drop, e.g., -7.45%  
» change_utc8 | string | Percentage change at utc8. Negative values indicate a drop, e.g., -7.45%  
» change_price | string | 24h change amount. Negative values indicate a drop, e.g., -7.45  
» change_utc0_price | string | Change amount at utc0. Negative values indicate a drop, e.g., -7.45  
» change_utc8_price | string | Change amount at utc8. Negative values indicate a drop, e.g., -7.45  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/tickers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/tickers \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "contract": "BTC_USDT",
        "last": "6432",
        "low_24h": "6278",
        "high_24h": "6790",
        "change_percentage": "4.43",
        "total_size": "32323904",
        "volume_24h": "184040233284",
        "volume_24h_btc": "28613220",
        "volume_24h_usd": "184040233284",
        "volume_24h_base": "28613220",
        "volume_24h_quote": "184040233284",
        "volume_24h_settle": "28613220",
        "mark_price": "6534",
        "funding_rate": "0.0001",
        "funding_rate_indicative": "0.0001",
        "index_price": "6531",
        "highest_bid": "34089.7",
        "highest_size": "100",
        "lowest_ask": "34217.9",
        "lowest_size": "1000"
      }
    ]
    

##  Futures market historical funding rate

GET`/futures/{settle}/funding_rate`

GET `/futures/{settle}/funding_rate`

_Futures market historical funding rate_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Required | Futures contract  
limit | query | integer | Optional | Maximum number of records returned in a single list  
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
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)History query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | History query successful | [FundingRateRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» t | integer(int64) | Unix timestamp in seconds  
» r | string | Funding rate  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/funding_rate'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/funding_rate?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "t": 1543968000,
        "r": "0.000157"
      }
    ]
    

##  Batch Query Historical Funding Rate Data for Perpetual Contracts

POST`/futures/{settle}/funding_rates`

POST `/futures/{settle}/funding_rates`

_Batch Query Historical Funding Rate Data for Perpetual Contracts_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
body | body | BatchFundingRatesRequest | Required | none  
↳ contracts | body | array | Required | Array of Contract Names  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Batch Query Successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch Query Successful | [BatchFundingRatesResponse]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» contract | string | Contract name  
» data | array | Array of Funding Rates  
»» t | integer(int64) | Unix timestamp in seconds  
»» r | string | Funding rate  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/funding_rates'
    query_param = ''
    body='{"contracts":["BTC_USDT","ETH_USDT"]}'
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    curl -X POST https://api.gateio.ws/api/v4/futures/usdt/funding_rates \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    
    

> Body parameter
    
    
    {
      "contracts": [
        "BTC_USDT",
        "ETH_USDT"
      ]
    }
    

> Example responses

> 200 Response
    
    
    [
      [
        {
          "contract": "BTC_USDT",
          "data": [
            {
              "t": 1543968000,
              "r": "0.000157"
            },
            {
              "t": 1544054400,
              "r": "0.000145"
            }
          ]
        }
      ]
    ]
    

##  Futures market insurance fund history

GET`/futures/{settle}/insurance`

GET `/futures/{settle}/insurance`

_Futures market insurance fund history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [InsuranceRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» t | integer(int64) | Unix timestamp in seconds  
» b | string | Insurance balance  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/insurance'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/insurance \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "t": 1543968000,
        "b": "83.0031"
      }
    ]
    

##  Futures statistics

GET`/futures/{settle}/contract_stats`

GET `/futures/{settle}/contract_stats`

_Futures statistics_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Required | Futures contract  
from | query | integer(int64) | Optional | Start timestamp  
interval | query | string | Optional | none  
limit | query | integer | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [ContractStat]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | integer(int64) | Stat timestamp  
» lsr_taker | number(double) | Long/short taker ratio  
» lsr_account | number(double) | Long/short position user ratio  
» long_liq_size | string | Long liquidation size (contracts)  
» long_liq_amount | number(double) | Long liquidation amount (base currency)  
» long_liq_usd | number(double) | Long liquidation volume (quote currency)  
» long_liq_usd_new | number(double) | Long liquidations in quote currency; USDT settlement: long_liq_size × multiplier × mark price  
» short_liq_size | string | Short liquidation size (contracts)  
» short_liq_amount | number(double) | Short liquidation amount (base currency)  
» short_liq_usd | number(double) | Short liquidation volume (quote currency)  
» short_liq_usd_new | number(double) | Short liquidations in quote currency; USDT settlement: short_liq_size × multiplier × mark price  
» open_interest | string | Total open interest size (contracts)  
» open_interest_usd | number(double) | Total open interest volume (quote currency)  
» top_lsr_account | number(double) | Top trader long/short account ratio  
» top_lsr_size | string | Top trader long/short position ratio  
» mark_price | number(double) | Mark price  
» top_long_size | string | Top long open interest (contracts)  
» top_short_size | string | Top short open interest (contracts)  
» long_taker_size | string | Long taker trade volume (contracts)  
» short_taker_size | string | Short taker trade volume (contracts)  
» top_long_account | string | Number of top long accounts (large holders)  
» top_short_account | string | Number of top short accounts (large holders)  
» long_users | string | Number of users holding long positions  
» short_users | string | Number of users holding short positions  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/contract_stats'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/contract_stats?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "time": 1603865400,
        "lsr_taker": 100,
        "lsr_account": 0.5,
        "long_liq_size": "0",
        "short_liq_size": "0",
        "open_interest": "124724",
        "short_liq_usd": 0,
        "mark_price": "8865",
        "top_lsr_size": "1.02",
        "short_liq_amount": 0,
        "long_liq_amount": 0,
        "open_interest_usd": 1511,
        "top_lsr_account": 1.5,
        "long_liq_usd": 0
      }
    ]
    

##  Query index constituents

GET`/futures/{settle}/index_constituents/{index}`

GET `/futures/{settle}/index_constituents/{index}`

_Query index constituents_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
index | path | string | Required | Index name  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | FuturesIndexConstituents  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» index | string | Index name  
» constituents | array | Constituents  
»» IndexConstituent | object | none  
»»» exchange | string | Exchange  
»»» symbols | array | Symbol list  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/index_constituents/BTC_USDT'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/index_constituents/BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "index": "BTC_USDT",
      "constituents": [
        {
          "exchange": "Binance",
          "symbols": [
            "BTC_USDT"
          ]
        },
        {
          "exchange": "Gate.com",
          "symbols": [
            "BTC_USDT"
          ]
        },
        {
          "exchange": "Huobi",
          "symbols": [
            "BTC_USDT"
          ]
        }
      ]
    }
    

##  Query liquidation order history

GET`/futures/{settle}/liq_orders`

GET `/futures/{settle}/liq_orders`

_Query liquidation order history_

The time interval between from and to is maximum 3600. Some private fields are not returned by public interfaces, refer to field descriptions for details

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FuturesLiqOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | integer(int64) | Liquidation time  
» contract | string | Futures contract  
» size | string | User position size  
» order_size | string | Number of forced liquidation orders  
» order_price | string | Liquidation order price  
» fill_price | string | Liquidation order average taker price  
» left | string | System liquidation order maker size  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/liq_orders'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/liq_orders \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "time": 1548654951,
        "contract": "BTC_USDT",
        "size": "600",
        "order_size": "-600",
        "order_price": "3405",
        "fill_price": "3424",
        "left": "0"
      }
    ]
    

##  Query risk limit tiers

GET`/futures/{settle}/risk_limit_tiers`

GET `/futures/{settle}/risk_limit_tiers`

_Query risk limit tiers_

When the 'contract' parameter is not passed, the default is to query the risk limits for the top 100 markets. 'Limit' and 'offset' correspond to pagination queries at the market level, not to the length of the returned array. This only takes effect when the contract parameter is empty.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [FuturesLimitRiskTiers]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Retrieve risk limit configurations for different tiers under a specified contract]  
» _None_ | FuturesLimitRiskTiers | Retrieve risk limit configurations for different tiers under a specified contract  
»» tier | integer(int) | Tier  
»» risk_limit | string | Position risk limit  
»» initial_rate | string | Initial margin rate  
»» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
»» leverage_max | string | Maximum leverage  
»» contract | string | Market, only visible when market pagination is requested  
»» deduction | string | Maintenance margin quick calculation deduction amount  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/risk_limit_tiers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/risk_limit_tiers \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "maintenance_rate": "0.01",
        "tier": 1,
        "initial_rate": "0.02",
        "leverage_max": "50",
        "risk_limit": "20000",
        "contract": "ZTX_USDT",
        "deduction": "0"
      },
      {
        "maintenance_rate": "0.013",
        "tier": 2,
        "initial_rate": "0.025",
        "leverage_max": "40",
        "risk_limit": "30000",
        "contract": "ZTX_USDT",
        "deduction": "60"
      },
      {
        "maintenance_rate": "0.015",
        "tier": 3,
        "initial_rate": "0.02857",
        "leverage_max": "35",
        "risk_limit": "50000",
        "contract": "ZTX_USDT",
        "deduction": "120"
      },
      {
        "maintenance_rate": "0.02",
        "tier": 4,
        "initial_rate": "0.03333",
        "leverage_max": "30",
        "risk_limit": "70000",
        "contract": "ZTX_USDT",
        "deduction": "370"
      },
      {
        "maintenance_rate": "0.025",
        "tier": 5,
        "initial_rate": "0.04",
        "leverage_max": "25",
        "risk_limit": "100000",
        "contract": "ZTX_USDT",
        "deduction": "720"
      }
    ]
    

##  Get futures account🔒 Authenticated

GET`/futures/{settle}/accounts`

GET `/futures/{settle}/accounts`

Get `futures account`

Query account information for classic future account and unified account

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | FuturesAccount  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» total | string | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
» unrealised_pnl | string | Unrealized PNL  
» position_margin | string | Deprecated  
» order_margin | string | initial margin of all open orders  
» available | string | Refers to the available withdrawal or trading amount in per-position, specifically the per-position available balance under the unified account that includes the credit line (which incorporates trial funds; since trial funds cannot be withdrawn, the actual withdrawal amount needs to deduct the trial fund portion when processing withdrawals)  
» point | string | Point card amount  
» currency | string | Settlement currency  
» in_dual_mode | boolean | Whether Hedge Mode is enabled  
» enable_credit | boolean | Whether portfolio margin account mode is enabled  
» position_initial_margin | string | Initial margin occupied by positions, applicable to unified account mode  
» maintenance_margin | string | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode  
» bonus | string | Bonus  
» enable_evolved_classic | boolean | Deprecated  
» cross_order_margin | string | Cross margin order margin, applicable to new classic account margin mode  
» cross_initial_margin | string | Cross margin initial margin, applicable to new classic account margin mode  
» cross_maintenance_margin | string | Cross margin maintenance margin, applicable to new classic account margin mode  
» cross_unrealised_pnl | string | Cross margin unrealized P&L, applicable to new classic account margin mode  
» cross_available | string | Cross margin available balance, applicable to new classic account margin mode  
» cross_margin_balance | string | Cross margin balance, applicable to new classic account margin mode  
» cross_mmr | string | Cross margin maintenance margin rate, applicable to new classic account margin mode  
» cross_imr | string | Cross margin initial margin rate, applicable to new classic account margin mode  
» isolated_position_margin | string | Isolated position margin, applicable to new classic account margin mode  
» enable_new_dual_mode | boolean | Deprecated  
» margin_mode | integer | Margin mode of the account  
0: classic future account or Classic Spot Margin Mode of unified account;  
1: Multi-Currency Margin Mode;  
2: Portoforlio Margin Mode;  
3: Single-Currency Margin Mode  
» enable_tiered_mm | boolean | Whether to enable tiered maintenance margin calculation  
» enable_dual_plus | boolean | Whether to Support Split Position Mode  
» position_mode | string | Position Holding Mode single - Single Direction Position, dual - Dual Direction Position, dual_plus - Split Position  
» history | object | Statistical data  
»» dnw | string | total amount of deposit and withdraw  
»» pnl | string | total amount of trading profit and loss  
»» fee | string | total amount of fee  
»» refr | string | total amount of referrer rebates  
»» fund | string | total amount of funding costs  
»» point_dnw | string | total amount of point deposit and withdraw  
»» point_fee | string | total amount of point fee  
»» point_refr | string | total amount of referrer rebates of point fee  
»» bonus_dnw | string | total amount of perpetual contract bonus transfer  
»» bonus_offset | string | total amount of perpetual contract bonus deduction  
»» cross_settle | string | Represents the value of profit settlement from the futures account to the spot account under Unified Account Mode. Negative values indicate settlement from futures to spot, while positive values indicate settlement from spot to futures. This value is cumulative.  
  
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
    
    url = '/futures/usdt/accounts'
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
    url="/futures/usdt/accounts"
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
      "user": 1666,
      "currency": "USDT",
      "total": "9707.803567115145",
      "unrealised_pnl": "3371.248828",
      "position_margin": "38.712189181",
      "order_margin": "0",
      "available": "9669.091377934145",
      "point": "0",
      "bonus": "0",
      "in_dual_mode": false,
      "enable_evolved_classic": false,
      "cross_initial_margin": "61855.56788525",
      "cross_maintenance_margin": "682.04678105",
      "cross_order_margin": "0",
      "cross_unrealised_pnl": "1501.178222634128",
      "cross_available": "27549.406108813951",
      "cross_margin_balance": "10371.77306201952",
      "cross_mmr": "797.2134",
      "cross_imr": "116.6097",
      "isolated_position_margin": "0",
      "history": {
        "dnw": "10000",
        "pnl": "68.3685",
        "fee": "-1.645812875",
        "refr": "0",
        "fund": "-358.919120009855",
        "point_dnw": "0",
        "point_fee": "0",
        "point_refr": "0",
        "bonus_dnw": "0",
        "bonus_offset": "0"
      },
      "enable_tiered_mm": true,
      "position_mode": "dual_plus",
      "enable_dual_plus": true
    }
    

##  Query futures account change history🔒 Authenticated

GET`/futures/{settle}/account_book`

GET `/futures/{settle}/account_book`

_Query futures account change history_

If the contract field is passed, only records containing this field after 2023-10-30 can be filtered。

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
type | query | string | Optional | Change types:  
  
\- dnw: Deposit and withdrawal  
\- pnl: Profit and loss from position reduction  
\- fee: Trading fees  
\- refr: Referrer rebates  
\- fund: Funding fees  
\- point_dnw: Point card deposit and withdrawal  
\- point_fee: Point card trading fees  
\- point_refr: Point card referrer rebates  
\- bonus_offset: Trial fund deduction  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

**type** : Change types:  
  
\- dnw: Deposit and withdrawal  
\- pnl: Profit and loss from position reduction  
\- fee: Trading fees  
\- refr: Referrer rebates  
\- fund: Funding fees  
\- point_dnw: Point card deposit and withdrawal  
\- point_fee: Point card trading fees  
\- point_refr: Point card referrer rebates  
\- bonus_offset: Trial fund deduction

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FuturesAccountBook]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | number(double) | Change time  
» change | string | Change amount  
» balance | string | Balance after change  
» type | string | Change types:  
  
\- dnw: Deposit and withdrawal  
\- pnl: Profit and loss from position reduction  
\- fee: Trading fees  
\- refr: Referrer rebates  
\- fund: Funding fees  
\- point_dnw: Point card deposit and withdrawal  
\- point_fee: Point card trading fees  
\- point_refr: Point card referrer rebates  
\- bonus_offset: Trial fund deduction  
» text | string | Comment  
» contract | string | Futures contract, the field is only available for data after 2023-10-30  
» trade_id | string | trade id  
» id | string | Account change record ID  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | dnw  
type | pnl  
type | fee  
type | refr  
type | fund  
type | point_dnw  
type | point_fee  
type | point_refr  
type | bonus_offset  
  
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
    
    url = '/futures/usdt/account_book'
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
    url="/futures/usdt/account_book"
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
        "time": 1682294400.123456,
        "change": "0.000010152188",
        "balance": "4.59316525194",
        "text": "ETH_USD:6086261",
        "type": "fee",
        "contract": "ETH_USD",
        "trade_id": "1",
        "id": "1"
      }
    ]
    

##  Get user position list🔒 Authenticated

GET`/futures/{settle}/positions`

GET `/futures/{settle}/positions`

Get `user position list`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
holding | query | boolean | Optional | Return only real positions - true, return all - false  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Position]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures position details]  
» _None_ | Position | Futures position details  
»» user | integer(int64) | User ID  
»» contract | string | Futures contract  
»» size | string | Position size  
»» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
»» risk_limit | string | Position risk limit  
»» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
»» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
»» value | string | Position value calculated in settlement currency  
»» margin | string | Position margin  
»» entry_price | string | Entry price  
»» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
»» mark_price | string | Current mark price  
»» initial_margin | string | Initial margin of postions  
»» maintenance_margin | string | Maintencance margin of postions  
»» unrealised_pnl | string | Unrealized PNL  
»» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
»» pnl_pnl | string | settled pnl when closing postion  
»» pnl_fund | string | funding fees  
»» pnl_fee | string | trading fees  
»» history_pnl | string | Total realized PnL from closed positions  
»» last_close_pnl | string | PNL of last position close  
»» realised_point | string | Realized POINT PNL  
»» history_point | string | History realized POINT PNL  
»» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
»» pending_orders | integer | Current pending order quantity  
»» close_order | object|null | Current close order information, or `null` if no close order  
»»» id | integer(int64) | Order ID  
»»» price | string | Order price  
»»» is_liq | boolean | Whether the close order is from liquidation  
»» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
»» cross_leverage_limit | string | leverage for cross margin  
»» update_time | integer(int64) | Last update time  
»» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
»» open_time | integer(int64) | First Open Time  
»» risk_limit_table | string | Risk limit table ID  
»» average_maintenance_rate | string | Average maintenance margin rate  
»» pid | integer(int64) | Sub-account position ID  
»» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
»» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/positions'
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
    url="/futures/usdt/positions"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "leverage": "0",
        "risk_limit": "100",
        "leverage_max": "100",
        "maintenance_rate": "0.005",
        "value": "3568.62",
        "margin": "4.431548146258",
        "entry_price": "3779.55",
        "liq_price": "99999999",
        "mark_price": "3780.32",
        "unrealised_pnl": "-0.000507486844",
        "realised_pnl": "0.045543982432",
        "pnl_pnl": "0.045543982432",
        "pnl_fund": "0",
        "pnl_fee": "0",
        "history_pnl": "0",
        "last_close_pnl": "0",
        "realised_point": "0",
        "history_point": "0",
        "adl_ranking": 5,
        "pending_orders": 16,
        "close_order": {
          "id": 232323,
          "price": "3779",
          "is_liq": false
        },
        "mode": "single",
        "update_time": 1684994406,
        "update_id": 1,
        "cross_leverage_limit": "0",
        "risk_limit_table": "BIG_HOT_COIN_50X_V2",
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  Get user's historical position information list by time🔒 Authenticated

GET`/futures/{settle}/positions_timerange`

GET `/futures/{settle}/positions_timerange`

Get `user's historical position information list by time`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Required | Futures contract  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [PositionTimerange]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Contract position details (historical data)]  
» _None_ | PositionTimerange | Contract position details (historical data)  
»» contract | string | Futures contract  
»» size | string | Position size  
»» leverage | string | Position leverage. 0 means cross margin; positive number means isolated margin  
»» risk_limit | string | Position risk limit  
»» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
»» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
»» margin | string | Position margin  
»» liq_price | string | Liquidation price  
»» realised_pnl | string | Realized PnL  
»» history_pnl | string | Total realized PnL from closed positions  
»» last_close_pnl | string | PNL of last position close  
»» realised_point | string | Realized POINT PNL  
»» history_point | string | History realized POINT PNL  
»» mode | string | Position mode, including:  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
»» cross_leverage_limit | string | Cross margin leverage (valid only when `leverage` is 0)  
»» entry_price | string | Entry price  
»» time | integer(int64) | Timestamp  
  
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
    
    url = '/futures/usdt/positions_timerange'
    query_param = 'contract=BTC_USDT'
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
    url="/futures/usdt/positions_timerange"
    query_param="contract=BTC_USDT"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "leverage": "0",
        "risk_limit": "100",
        "leverage_max": "100",
        "maintenance_rate": "0.005",
        "value": "3568.62",
        "margin": "4.431548146258",
        "entry_price": "3779.55",
        "liq_price": "99999999",
        "mark_price": "3780.32",
        "unrealised_pnl": "-0.000507486844",
        "realised_pnl": "0.045543982432",
        "pnl_pnl": "0.045543982432",
        "pnl_fund": "0",
        "pnl_fee": "0",
        "history_pnl": "0",
        "last_close_pnl": "0",
        "realised_point": "0",
        "history_point": "0",
        "adl_ranking": 5,
        "pending_orders": 16,
        "close_order": {
          "id": 232323,
          "price": "3779",
          "is_liq": false
        },
        "mode": "single",
        "update_time": 1684994406,
        "update_id": 1,
        "cross_leverage_limit": "0",
        "risk_limit_table": "BIG_HOT_COIN_50X_V2",
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  Get single position information🔒 Authenticated

GET`/futures/{settle}/positions/{contract}`

GET `/futures/{settle}/positions/{contract}`

Get `single position information`

Get `single position information from a contract. If you hold two postions in one contract market, please use this API: /futures/{settle}/dual_comp/positions/{contract}`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | Position  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | string | Position size  
» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
» risk_limit | string | Position risk limit  
» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
» mark_price | string | Current mark price  
» initial_margin | string | Initial margin of postions  
» maintenance_margin | string | Maintencance margin of postions  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
» pnl_pnl | string | settled pnl when closing postion  
» pnl_fund | string | funding fees  
» pnl_fee | string | trading fees  
» history_pnl | string | Total realized PnL from closed positions  
» last_close_pnl | string | PNL of last position close  
» realised_point | string | Realized POINT PNL  
» history_point | string | History realized POINT PNL  
» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
» pending_orders | integer | Current pending order quantity  
» close_order | object|null | Current close order information, or `null` if no close order  
»» id | integer(int64) | Order ID  
»» price | string | Order price  
»» is_liq | boolean | Whether the close order is from liquidation  
» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
» cross_leverage_limit | string | leverage for cross margin  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
» pid | integer(int64) | Sub-account position ID  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT'
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
    url="/futures/usdt/positions/BTC_USDT"
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
      "user": 10000,
      "contract": "BTC_USDT",
      "size": "-9440",
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  Get Leverage Information for Specified Mode🔒 Authenticated

GET`/futures/{settle}/get_leverage/{contract}`

GET `/futures/{settle}/get_leverage/{contract}`

Get `Leverage Information for Specified Mode`

Get `Leverage Information for Specified Mode`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
pos_margin_mode | query | string | Required | Position Margin Mode, required for split position mode, values: isolated/cross.  
dual_side | query | string | Required | dual_long - Long, dual_short - Short  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)query leverage success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | query leverage success | FuturesLeverage  
  
### Response Schema

Status Code **200**

_Return result includes Lever field_

Name | Type | Description  
---|---|---  
» Lever | string | leverage  
  
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
    
    url = '/futures/usdt/get_leverage/BTC_USDT'
    query_param = 'pos_margin_mode=isolated&dual_side=dual_long'
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
    url="/futures/usdt/get_leverage/BTC_USDT"
    query_param="pos_margin_mode=isolated&dual_side=dual_long"
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
      "Lever": "10"
    }
    

##  Update position margin🔒 Authenticated

POST`/futures/{settle}/positions/{contract}/margin`

POST `/futures/{settle}/positions/{contract}/margin`

_Update position margin_

Under the new risk limit rules(https://www.gate.com/en/help/futures/futures-logic/22162), the position limit is related to the leverage you set; a lower leverage will result in a higher position limit. Please use the leverage adjustment api to adjust the position limit.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
change | query | string | Required | Margin change amount, positive number increases, negative number decreases  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | Position  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | string | Position size  
» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
» risk_limit | string | Position risk limit  
» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
» mark_price | string | Current mark price  
» initial_margin | string | Initial margin of postions  
» maintenance_margin | string | Maintencance margin of postions  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
» pnl_pnl | string | settled pnl when closing postion  
» pnl_fund | string | funding fees  
» pnl_fee | string | trading fees  
» history_pnl | string | Total realized PnL from closed positions  
» last_close_pnl | string | PNL of last position close  
» realised_point | string | Realized POINT PNL  
» history_point | string | History realized POINT PNL  
» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
» pending_orders | integer | Current pending order quantity  
» close_order | object|null | Current close order information, or `null` if no close order  
»» id | integer(int64) | Order ID  
»» price | string | Order price  
»» is_liq | boolean | Whether the close order is from liquidation  
» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
» cross_leverage_limit | string | leverage for cross margin  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
» pid | integer(int64) | Sub-account position ID  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT/margin'
    query_param = 'change=0.01'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/futures/usdt/positions/BTC_USDT/margin"
    query_param="change=0.01"
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
      "user": 10000,
      "contract": "BTC_USDT",
      "size": "-9440",
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  Update position leverage🔒 Authenticated

POST`/futures/{settle}/positions/{contract}/leverage`

POST `/futures/{settle}/positions/{contract}/leverage`

_Update position leverage_

⚠️ Position Mode Switching Rules:

  * leverage ≠ 0: Isolated Margin Mode (Regardless of whether cross_leverage_limit is filled, this parameter will be ignored)
  * leverage = 0: Cross Margin Mode (Use cross_leverage_limit to set the leverage multiple)

Examples:

  * Set isolated margin with 10x leverage: leverage=10
  * Set cross margin with 10x leverage: leverage=0&cross_leverage_limit=10
  * leverage=5&cross_leverage_limit=10 → Result: Isolated margin with 5x leverage (cross_leverage_limit is ignored)

⚠️ Warning: Incorrect settings may cause unexpected position mode switching, affecting risk management.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
leverage | query | string | Required | Set the leverage for isolated margin. When setting isolated margin leverage, the `cross_leverage_limit` must be empty.  
cross_leverage_limit | query | string | Optional | Set the leverage for cross margin. When setting cross margin leverage, the `leverage` must be set to 0.  
pid | query | integer(int32) | Optional | Product ID  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | Position  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | string | Position size  
» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
» risk_limit | string | Position risk limit  
» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
» mark_price | string | Current mark price  
» initial_margin | string | Initial margin of postions  
» maintenance_margin | string | Maintencance margin of postions  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
» pnl_pnl | string | settled pnl when closing postion  
» pnl_fund | string | funding fees  
» pnl_fee | string | trading fees  
» history_pnl | string | Total realized PnL from closed positions  
» last_close_pnl | string | PNL of last position close  
» realised_point | string | Realized POINT PNL  
» history_point | string | History realized POINT PNL  
» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
» pending_orders | integer | Current pending order quantity  
» close_order | object|null | Current close order information, or `null` if no close order  
»» id | integer(int64) | Order ID  
»» price | string | Order price  
»» is_liq | boolean | Whether the close order is from liquidation  
» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
» cross_leverage_limit | string | leverage for cross margin  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
» pid | integer(int64) | Sub-account position ID  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT/leverage'
    query_param = 'leverage=10'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/futures/usdt/positions/BTC_USDT/leverage"
    query_param="leverage=10"
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
      "user": 10000,
      "contract": "BTC_USDT",
      "size": "-9440",
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  Update Leverage for Specified Mode🔒 Authenticated

POST`/futures/{settle}/positions/{contract}/set_leverage`

POST `/futures/{settle}/positions/{contract}/set_leverage`

_Update Leverage for Specified Mode_

To simplify the complex logic of the leverage interface, added a new interface for modifying leverage

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
leverage | query | string | Required | Position Leverage Multiple  
margin_mode | query | string | Required | Margin Mode isolated/cross  
dual_side | query | string | Optional | dual_long - Long, dual_short - Short  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | Position  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | string | Position size  
» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
» risk_limit | string | Position risk limit  
» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
» mark_price | string | Current mark price  
» initial_margin | string | Initial margin of postions  
» maintenance_margin | string | Maintencance margin of postions  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
» pnl_pnl | string | settled pnl when closing postion  
» pnl_fund | string | funding fees  
» pnl_fee | string | trading fees  
» history_pnl | string | Total realized PnL from closed positions  
» last_close_pnl | string | PNL of last position close  
» realised_point | string | Realized POINT PNL  
» history_point | string | History realized POINT PNL  
» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
» pending_orders | integer | Current pending order quantity  
» close_order | object|null | Current close order information, or `null` if no close order  
»» id | integer(int64) | Order ID  
»» price | string | Order price  
»» is_liq | boolean | Whether the close order is from liquidation  
» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
» cross_leverage_limit | string | leverage for cross margin  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
» pid | integer(int64) | Sub-account position ID  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT/set_leverage'
    query_param = 'leverage=10&margin_mode=cross'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/futures/usdt/positions/BTC_USDT/set_leverage"
    query_param="leverage=10&margin_mode=cross"
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
      "user": 10000,
      "contract": "BTC_USDT",
      "size": "-9440",
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  Switch Position Margin Mode🔒 Authenticated

POST`/futures/{settle}/positions/cross_mode`

POST `/futures/{settle}/positions/cross_mode`

_Switch Position Margin Mode_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
body | body | FuturesPositionCrossMode | Required | none  
↳ mode | body | string | Required | Cross/isolated margin mode. ISOLATED - isolated margin, CROSS - cross margin  
↳ contract | body | string | Required | Futures market  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | Position  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | string | Position size  
» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
» risk_limit | string | Position risk limit  
» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
» mark_price | string | Current mark price  
» initial_margin | string | Initial margin of postions  
» maintenance_margin | string | Maintencance margin of postions  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
» pnl_pnl | string | settled pnl when closing postion  
» pnl_fund | string | funding fees  
» pnl_fee | string | trading fees  
» history_pnl | string | Total realized PnL from closed positions  
» last_close_pnl | string | PNL of last position close  
» realised_point | string | Realized POINT PNL  
» history_point | string | History realized POINT PNL  
» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
» pending_orders | integer | Current pending order quantity  
» close_order | object|null | Current close order information, or `null` if no close order  
»» id | integer(int64) | Order ID  
»» price | string | Order price  
»» is_liq | boolean | Whether the close order is from liquidation  
» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
» cross_leverage_limit | string | leverage for cross margin  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
» pid | integer(int64) | Sub-account position ID  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/positions/cross_mode'
    query_param = ''
    body='{"mode":"ISOLATED","contract":"BTC_USDT"}'
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
    url="/futures/usdt/positions/cross_mode"
    query_param=""
    body_param='{"mode":"ISOLATED","contract":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "mode": "ISOLATED",
      "contract": "BTC_USDT"
    }
    

> Example responses

> 200 Response
    
    
    {
      "user": 10000,
      "contract": "BTC_USDT",
      "size": "-9440",
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  Switch Between Cross and Isolated Margin Modes Under Hedge Mode🔒 Authenticated

POST`/futures/{settle}/dual_comp/positions/cross_mode`

POST `/futures/{settle}/dual_comp/positions/cross_mode`

_Switch Between Cross and Isolated Margin Modes Under Hedge Mode_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
body | body | UpdateDualCompPositionCrossModeRequest | Required | none  
↳ mode | body | string | Required | Cross/isolated margin mode. ISOLATED - isolated margin, CROSS - cross margin  
↳ contract | body | string | Required | Futures market  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [Position]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures position details]  
» _None_ | Position | Futures position details  
»» user | integer(int64) | User ID  
»» contract | string | Futures contract  
»» size | string | Position size  
»» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
»» risk_limit | string | Position risk limit  
»» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
»» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
»» value | string | Position value calculated in settlement currency  
»» margin | string | Position margin  
»» entry_price | string | Entry price  
»» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
»» mark_price | string | Current mark price  
»» initial_margin | string | Initial margin of postions  
»» maintenance_margin | string | Maintencance margin of postions  
»» unrealised_pnl | string | Unrealized PNL  
»» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
»» pnl_pnl | string | settled pnl when closing postion  
»» pnl_fund | string | funding fees  
»» pnl_fee | string | trading fees  
»» history_pnl | string | Total realized PnL from closed positions  
»» last_close_pnl | string | PNL of last position close  
»» realised_point | string | Realized POINT PNL  
»» history_point | string | History realized POINT PNL  
»» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
»» pending_orders | integer | Current pending order quantity  
»» close_order | object|null | Current close order information, or `null` if no close order  
»»» id | integer(int64) | Order ID  
»»» price | string | Order price  
»»» is_liq | boolean | Whether the close order is from liquidation  
»» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
»» cross_leverage_limit | string | leverage for cross margin  
»» update_time | integer(int64) | Last update time  
»» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
»» open_time | integer(int64) | First Open Time  
»» risk_limit_table | string | Risk limit table ID  
»» average_maintenance_rate | string | Average maintenance margin rate  
»» pid | integer(int64) | Sub-account position ID  
»» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
»» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/dual_comp/positions/cross_mode'
    query_param = ''
    body='{"mode":"ISOLATED","contract":"BTC_USDT"}'
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
    url="/futures/usdt/dual_comp/positions/cross_mode"
    query_param=""
    body_param='{"mode":"ISOLATED","contract":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "mode": "ISOLATED",
      "contract": "BTC_USDT"
    }
    

> Example responses

> 200 Response
    
    
    [
      {
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "leverage": "0",
        "risk_limit": "100",
        "leverage_max": "100",
        "maintenance_rate": "0.005",
        "value": "3568.62",
        "margin": "4.431548146258",
        "entry_price": "3779.55",
        "liq_price": "99999999",
        "mark_price": "3780.32",
        "unrealised_pnl": "-0.000507486844",
        "realised_pnl": "0.045543982432",
        "pnl_pnl": "0.045543982432",
        "pnl_fund": "0",
        "pnl_fee": "0",
        "history_pnl": "0",
        "last_close_pnl": "0",
        "realised_point": "0",
        "history_point": "0",
        "adl_ranking": 5,
        "pending_orders": 16,
        "close_order": {
          "id": 232323,
          "price": "3779",
          "is_liq": false
        },
        "mode": "single",
        "update_time": 1684994406,
        "update_id": 1,
        "cross_leverage_limit": "0",
        "risk_limit_table": "BIG_HOT_COIN_50X_V2",
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  Update position risk limit🔒 Authenticated

POST`/futures/{settle}/positions/{contract}/risk_limit`

POST `/futures/{settle}/positions/{contract}/risk_limit`

_Update position risk limit_

Under the new risk limit rules(https://www.gate.com/en/help/futures/futures-logic/22162), the position limit is related to the leverage you set; a lower leverage will result in a higher position limit. Please use the leverage adjustment api to adjust the position limit.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
risk_limit | query | string | Required | New risk limit value  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | Position  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | string | Position size  
» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
» risk_limit | string | Position risk limit  
» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
» mark_price | string | Current mark price  
» initial_margin | string | Initial margin of postions  
» maintenance_margin | string | Maintencance margin of postions  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
» pnl_pnl | string | settled pnl when closing postion  
» pnl_fund | string | funding fees  
» pnl_fee | string | trading fees  
» history_pnl | string | Total realized PnL from closed positions  
» last_close_pnl | string | PNL of last position close  
» realised_point | string | Realized POINT PNL  
» history_point | string | History realized POINT PNL  
» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
» pending_orders | integer | Current pending order quantity  
» close_order | object|null | Current close order information, or `null` if no close order  
»» id | integer(int64) | Order ID  
»» price | string | Order price  
»» is_liq | boolean | Whether the close order is from liquidation  
» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
» cross_leverage_limit | string | leverage for cross margin  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
» pid | integer(int64) | Sub-account position ID  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT/risk_limit'
    query_param = 'risk_limit=1000000'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/futures/usdt/positions/BTC_USDT/risk_limit"
    query_param="risk_limit=1000000"
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
      "user": 10000,
      "contract": "BTC_USDT",
      "size": "-9440",
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  Set position mode🔒 Authenticated

POST`/futures/{settle}/dual_mode`

POST `/futures/{settle}/dual_mode`

_Set position mode_

The prerequisite for changing mode is that all positions have no holdings and no pending orders

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
dual_mode | query | boolean | Required | Whether to enable Hedge Mode  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Updated successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Updated successfully | FuturesAccount  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» total | string | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
» unrealised_pnl | string | Unrealized PNL  
» position_margin | string | Deprecated  
» order_margin | string | initial margin of all open orders  
» available | string | Refers to the available withdrawal or trading amount in per-position, specifically the per-position available balance under the unified account that includes the credit line (which incorporates trial funds; since trial funds cannot be withdrawn, the actual withdrawal amount needs to deduct the trial fund portion when processing withdrawals)  
» point | string | Point card amount  
» currency | string | Settlement currency  
» in_dual_mode | boolean | Whether Hedge Mode is enabled  
» enable_credit | boolean | Whether portfolio margin account mode is enabled  
» position_initial_margin | string | Initial margin occupied by positions, applicable to unified account mode  
» maintenance_margin | string | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode  
» bonus | string | Bonus  
» enable_evolved_classic | boolean | Deprecated  
» cross_order_margin | string | Cross margin order margin, applicable to new classic account margin mode  
» cross_initial_margin | string | Cross margin initial margin, applicable to new classic account margin mode  
» cross_maintenance_margin | string | Cross margin maintenance margin, applicable to new classic account margin mode  
» cross_unrealised_pnl | string | Cross margin unrealized P&L, applicable to new classic account margin mode  
» cross_available | string | Cross margin available balance, applicable to new classic account margin mode  
» cross_margin_balance | string | Cross margin balance, applicable to new classic account margin mode  
» cross_mmr | string | Cross margin maintenance margin rate, applicable to new classic account margin mode  
» cross_imr | string | Cross margin initial margin rate, applicable to new classic account margin mode  
» isolated_position_margin | string | Isolated position margin, applicable to new classic account margin mode  
» enable_new_dual_mode | boolean | Deprecated  
» margin_mode | integer | Margin mode of the account  
0: classic future account or Classic Spot Margin Mode of unified account;  
1: Multi-Currency Margin Mode;  
2: Portoforlio Margin Mode;  
3: Single-Currency Margin Mode  
» enable_tiered_mm | boolean | Whether to enable tiered maintenance margin calculation  
» enable_dual_plus | boolean | Whether to Support Split Position Mode  
» position_mode | string | Position Holding Mode single - Single Direction Position, dual - Dual Direction Position, dual_plus - Split Position  
» history | object | Statistical data  
»» dnw | string | total amount of deposit and withdraw  
»» pnl | string | total amount of trading profit and loss  
»» fee | string | total amount of fee  
»» refr | string | total amount of referrer rebates  
»» fund | string | total amount of funding costs  
»» point_dnw | string | total amount of point deposit and withdraw  
»» point_fee | string | total amount of point fee  
»» point_refr | string | total amount of referrer rebates of point fee  
»» bonus_dnw | string | total amount of perpetual contract bonus transfer  
»» bonus_offset | string | total amount of perpetual contract bonus deduction  
»» cross_settle | string | Represents the value of profit settlement from the futures account to the spot account under Unified Account Mode. Negative values indicate settlement from futures to spot, while positive values indicate settlement from spot to futures. This value is cumulative.  
  
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
    
    url = '/futures/usdt/dual_mode'
    query_param = 'dual_mode=true'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/futures/usdt/dual_mode"
    query_param="dual_mode=true"
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
      "user": 1666,
      "currency": "USDT",
      "total": "9707.803567115145",
      "unrealised_pnl": "3371.248828",
      "position_margin": "38.712189181",
      "order_margin": "0",
      "available": "9669.091377934145",
      "point": "0",
      "bonus": "0",
      "in_dual_mode": false,
      "enable_evolved_classic": false,
      "cross_initial_margin": "61855.56788525",
      "cross_maintenance_margin": "682.04678105",
      "cross_order_margin": "0",
      "cross_unrealised_pnl": "1501.178222634128",
      "cross_available": "27549.406108813951",
      "cross_margin_balance": "10371.77306201952",
      "cross_mmr": "797.2134",
      "cross_imr": "116.6097",
      "isolated_position_margin": "0",
      "history": {
        "dnw": "10000",
        "pnl": "68.3685",
        "fee": "-1.645812875",
        "refr": "0",
        "fund": "-358.919120009855",
        "point_dnw": "0",
        "point_fee": "0",
        "point_refr": "0",
        "bonus_dnw": "0",
        "bonus_offset": "0"
      },
      "enable_tiered_mm": true,
      "position_mode": "dual_plus",
      "enable_dual_plus": true
    }
    

##  Set Position Holding Mode, replacing the dual_mode interface🔒 Authenticated

POST`/futures/{settle}/set_position_mode`

POST `/futures/{settle}/set_position_mode`

_Set Position Holding Mode, replacing the dual_mode interface_

The prerequisite for changing mode is that all positions have no holdings and no pending orders

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
position_mode | query | string | Required | Optional Values: single, dual, dual_plus, representing Single Direction, Dual Direction, Split Position respectively  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Updated successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Updated successfully | FuturesAccount  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» total | string | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
» unrealised_pnl | string | Unrealized PNL  
» position_margin | string | Deprecated  
» order_margin | string | initial margin of all open orders  
» available | string | Refers to the available withdrawal or trading amount in per-position, specifically the per-position available balance under the unified account that includes the credit line (which incorporates trial funds; since trial funds cannot be withdrawn, the actual withdrawal amount needs to deduct the trial fund portion when processing withdrawals)  
» point | string | Point card amount  
» currency | string | Settlement currency  
» in_dual_mode | boolean | Whether Hedge Mode is enabled  
» enable_credit | boolean | Whether portfolio margin account mode is enabled  
» position_initial_margin | string | Initial margin occupied by positions, applicable to unified account mode  
» maintenance_margin | string | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode  
» bonus | string | Bonus  
» enable_evolved_classic | boolean | Deprecated  
» cross_order_margin | string | Cross margin order margin, applicable to new classic account margin mode  
» cross_initial_margin | string | Cross margin initial margin, applicable to new classic account margin mode  
» cross_maintenance_margin | string | Cross margin maintenance margin, applicable to new classic account margin mode  
» cross_unrealised_pnl | string | Cross margin unrealized P&L, applicable to new classic account margin mode  
» cross_available | string | Cross margin available balance, applicable to new classic account margin mode  
» cross_margin_balance | string | Cross margin balance, applicable to new classic account margin mode  
» cross_mmr | string | Cross margin maintenance margin rate, applicable to new classic account margin mode  
» cross_imr | string | Cross margin initial margin rate, applicable to new classic account margin mode  
» isolated_position_margin | string | Isolated position margin, applicable to new classic account margin mode  
» enable_new_dual_mode | boolean | Deprecated  
» margin_mode | integer | Margin mode of the account  
0: classic future account or Classic Spot Margin Mode of unified account;  
1: Multi-Currency Margin Mode;  
2: Portoforlio Margin Mode;  
3: Single-Currency Margin Mode  
» enable_tiered_mm | boolean | Whether to enable tiered maintenance margin calculation  
» enable_dual_plus | boolean | Whether to Support Split Position Mode  
» position_mode | string | Position Holding Mode single - Single Direction Position, dual - Dual Direction Position, dual_plus - Split Position  
» history | object | Statistical data  
»» dnw | string | total amount of deposit and withdraw  
»» pnl | string | total amount of trading profit and loss  
»» fee | string | total amount of fee  
»» refr | string | total amount of referrer rebates  
»» fund | string | total amount of funding costs  
»» point_dnw | string | total amount of point deposit and withdraw  
»» point_fee | string | total amount of point fee  
»» point_refr | string | total amount of referrer rebates of point fee  
»» bonus_dnw | string | total amount of perpetual contract bonus transfer  
»» bonus_offset | string | total amount of perpetual contract bonus deduction  
»» cross_settle | string | Represents the value of profit settlement from the futures account to the spot account under Unified Account Mode. Negative values indicate settlement from futures to spot, while positive values indicate settlement from spot to futures. This value is cumulative.  
  
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
    
    url = '/futures/usdt/set_position_mode'
    query_param = 'position_mode=dual_plus'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/futures/usdt/set_position_mode"
    query_param="position_mode=dual_plus"
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
      "user": 1666,
      "currency": "USDT",
      "total": "9707.803567115145",
      "unrealised_pnl": "3371.248828",
      "position_margin": "38.712189181",
      "order_margin": "0",
      "available": "9669.091377934145",
      "point": "0",
      "bonus": "0",
      "in_dual_mode": false,
      "enable_evolved_classic": false,
      "cross_initial_margin": "61855.56788525",
      "cross_maintenance_margin": "682.04678105",
      "cross_order_margin": "0",
      "cross_unrealised_pnl": "1501.178222634128",
      "cross_available": "27549.406108813951",
      "cross_margin_balance": "10371.77306201952",
      "cross_mmr": "797.2134",
      "cross_imr": "116.6097",
      "isolated_position_margin": "0",
      "history": {
        "dnw": "10000",
        "pnl": "68.3685",
        "fee": "-1.645812875",
        "refr": "0",
        "fund": "-358.919120009855",
        "point_dnw": "0",
        "point_fee": "0",
        "point_refr": "0",
        "bonus_dnw": "0",
        "bonus_offset": "0"
      },
      "enable_tiered_mm": true,
      "position_mode": "dual_plus",
      "enable_dual_plus": true
    }
    

##  Get position information in Hedge Mode🔒 Authenticated

GET`/futures/{settle}/dual_comp/positions/{contract}`

GET `/futures/{settle}/dual_comp/positions/{contract}`

Get `position information in Hedge Mode`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [Position]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures position details]  
» _None_ | Position | Futures position details  
»» user | integer(int64) | User ID  
»» contract | string | Futures contract  
»» size | string | Position size  
»» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
»» risk_limit | string | Position risk limit  
»» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
»» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
»» value | string | Position value calculated in settlement currency  
»» margin | string | Position margin  
»» entry_price | string | Entry price  
»» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
»» mark_price | string | Current mark price  
»» initial_margin | string | Initial margin of postions  
»» maintenance_margin | string | Maintencance margin of postions  
»» unrealised_pnl | string | Unrealized PNL  
»» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
»» pnl_pnl | string | settled pnl when closing postion  
»» pnl_fund | string | funding fees  
»» pnl_fee | string | trading fees  
»» history_pnl | string | Total realized PnL from closed positions  
»» last_close_pnl | string | PNL of last position close  
»» realised_point | string | Realized POINT PNL  
»» history_point | string | History realized POINT PNL  
»» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
»» pending_orders | integer | Current pending order quantity  
»» close_order | object|null | Current close order information, or `null` if no close order  
»»» id | integer(int64) | Order ID  
»»» price | string | Order price  
»»» is_liq | boolean | Whether the close order is from liquidation  
»» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
»» cross_leverage_limit | string | leverage for cross margin  
»» update_time | integer(int64) | Last update time  
»» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
»» open_time | integer(int64) | First Open Time  
»» risk_limit_table | string | Risk limit table ID  
»» average_maintenance_rate | string | Average maintenance margin rate  
»» pid | integer(int64) | Sub-account position ID  
»» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
»» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/dual_comp/positions/BTC_USDT'
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
    url="/futures/usdt/dual_comp/positions/BTC_USDT"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "leverage": "0",
        "risk_limit": "100",
        "leverage_max": "100",
        "maintenance_rate": "0.005",
        "value": "3568.62",
        "margin": "4.431548146258",
        "entry_price": "3779.55",
        "liq_price": "99999999",
        "mark_price": "3780.32",
        "unrealised_pnl": "-0.000507486844",
        "realised_pnl": "0.045543982432",
        "pnl_pnl": "0.045543982432",
        "pnl_fund": "0",
        "pnl_fee": "0",
        "history_pnl": "0",
        "last_close_pnl": "0",
        "realised_point": "0",
        "history_point": "0",
        "adl_ranking": 5,
        "pending_orders": 16,
        "close_order": {
          "id": 232323,
          "price": "3779",
          "is_liq": false
        },
        "mode": "single",
        "update_time": 1684994406,
        "update_id": 1,
        "cross_leverage_limit": "0",
        "risk_limit_table": "BIG_HOT_COIN_50X_V2",
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  Update position margin in Hedge Mode🔒 Authenticated

POST`/futures/{settle}/dual_comp/positions/{contract}/margin`

POST `/futures/{settle}/dual_comp/positions/{contract}/margin`

_Update position margin in Hedge Mode_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
change | query | string | Required | Margin change amount, positive number increases, negative number decreases  
dual_side | query | string | Required | Long or short position  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [Position]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures position details]  
» _None_ | Position | Futures position details  
»» user | integer(int64) | User ID  
»» contract | string | Futures contract  
»» size | string | Position size  
»» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
»» risk_limit | string | Position risk limit  
»» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
»» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
»» value | string | Position value calculated in settlement currency  
»» margin | string | Position margin  
»» entry_price | string | Entry price  
»» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
»» mark_price | string | Current mark price  
»» initial_margin | string | Initial margin of postions  
»» maintenance_margin | string | Maintencance margin of postions  
»» unrealised_pnl | string | Unrealized PNL  
»» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
»» pnl_pnl | string | settled pnl when closing postion  
»» pnl_fund | string | funding fees  
»» pnl_fee | string | trading fees  
»» history_pnl | string | Total realized PnL from closed positions  
»» last_close_pnl | string | PNL of last position close  
»» realised_point | string | Realized POINT PNL  
»» history_point | string | History realized POINT PNL  
»» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
»» pending_orders | integer | Current pending order quantity  
»» close_order | object|null | Current close order information, or `null` if no close order  
»»» id | integer(int64) | Order ID  
»»» price | string | Order price  
»»» is_liq | boolean | Whether the close order is from liquidation  
»» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
»» cross_leverage_limit | string | leverage for cross margin  
»» update_time | integer(int64) | Last update time  
»» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
»» open_time | integer(int64) | First Open Time  
»» risk_limit_table | string | Risk limit table ID  
»» average_maintenance_rate | string | Average maintenance margin rate  
»» pid | integer(int64) | Sub-account position ID  
»» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
»» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/dual_comp/positions/BTC_USDT/margin'
    query_param = 'change=0.01&dual_side=dual_long'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/futures/usdt/dual_comp/positions/BTC_USDT/margin"
    query_param="change=0.01&dual_side=dual_long"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "leverage": "0",
        "risk_limit": "100",
        "leverage_max": "100",
        "maintenance_rate": "0.005",
        "value": "3568.62",
        "margin": "4.431548146258",
        "entry_price": "3779.55",
        "liq_price": "99999999",
        "mark_price": "3780.32",
        "unrealised_pnl": "-0.000507486844",
        "realised_pnl": "0.045543982432",
        "pnl_pnl": "0.045543982432",
        "pnl_fund": "0",
        "pnl_fee": "0",
        "history_pnl": "0",
        "last_close_pnl": "0",
        "realised_point": "0",
        "history_point": "0",
        "adl_ranking": 5,
        "pending_orders": 16,
        "close_order": {
          "id": 232323,
          "price": "3779",
          "is_liq": false
        },
        "mode": "single",
        "update_time": 1684994406,
        "update_id": 1,
        "cross_leverage_limit": "0",
        "risk_limit_table": "BIG_HOT_COIN_50X_V2",
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  Update position leverage in Hedge Mode🔒 Authenticated

POST`/futures/{settle}/dual_comp/positions/{contract}/leverage`

POST `/futures/{settle}/dual_comp/positions/{contract}/leverage`

_Update position leverage in Hedge Mode_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
leverage | query | string | Required | New position leverage  
cross_leverage_limit | query | string | Optional | Cross margin leverage (valid only when `leverage` is 0)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [Position]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures position details]  
» _None_ | Position | Futures position details  
»» user | integer(int64) | User ID  
»» contract | string | Futures contract  
»» size | string | Position size  
»» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
»» risk_limit | string | Position risk limit  
»» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
»» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
»» value | string | Position value calculated in settlement currency  
»» margin | string | Position margin  
»» entry_price | string | Entry price  
»» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
»» mark_price | string | Current mark price  
»» initial_margin | string | Initial margin of postions  
»» maintenance_margin | string | Maintencance margin of postions  
»» unrealised_pnl | string | Unrealized PNL  
»» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
»» pnl_pnl | string | settled pnl when closing postion  
»» pnl_fund | string | funding fees  
»» pnl_fee | string | trading fees  
»» history_pnl | string | Total realized PnL from closed positions  
»» last_close_pnl | string | PNL of last position close  
»» realised_point | string | Realized POINT PNL  
»» history_point | string | History realized POINT PNL  
»» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
»» pending_orders | integer | Current pending order quantity  
»» close_order | object|null | Current close order information, or `null` if no close order  
»»» id | integer(int64) | Order ID  
»»» price | string | Order price  
»»» is_liq | boolean | Whether the close order is from liquidation  
»» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
»» cross_leverage_limit | string | leverage for cross margin  
»» update_time | integer(int64) | Last update time  
»» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
»» open_time | integer(int64) | First Open Time  
»» risk_limit_table | string | Risk limit table ID  
»» average_maintenance_rate | string | Average maintenance margin rate  
»» pid | integer(int64) | Sub-account position ID  
»» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
»» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/dual_comp/positions/BTC_USDT/leverage'
    query_param = 'leverage=10'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/futures/usdt/dual_comp/positions/BTC_USDT/leverage"
    query_param="leverage=10"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "leverage": "0",
        "risk_limit": "100",
        "leverage_max": "100",
        "maintenance_rate": "0.005",
        "value": "3568.62",
        "margin": "4.431548146258",
        "entry_price": "3779.55",
        "liq_price": "99999999",
        "mark_price": "3780.32",
        "unrealised_pnl": "-0.000507486844",
        "realised_pnl": "0.045543982432",
        "pnl_pnl": "0.045543982432",
        "pnl_fund": "0",
        "pnl_fee": "0",
        "history_pnl": "0",
        "last_close_pnl": "0",
        "realised_point": "0",
        "history_point": "0",
        "adl_ranking": 5,
        "pending_orders": 16,
        "close_order": {
          "id": 232323,
          "price": "3779",
          "is_liq": false
        },
        "mode": "single",
        "update_time": 1684994406,
        "update_id": 1,
        "cross_leverage_limit": "0",
        "risk_limit_table": "BIG_HOT_COIN_50X_V2",
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  Update position risk limit in Hedge Mode🔒 Authenticated

POST`/futures/{settle}/dual_comp/positions/{contract}/risk_limit`

POST `/futures/{settle}/dual_comp/positions/{contract}/risk_limit`

_Update position risk limit in Hedge Mode_

Under the new risk limit rules(https://www.gate.com/en/help/futures/futures-logic/22162), the position limit is related to the leverage you set; a lower leverage will result in a higher position limit. Please use the leverage adjustment api to adjust the position limit.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
risk_limit | query | string | Required | New risk limit value  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [Position]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures position details]  
» _None_ | Position | Futures position details  
»» user | integer(int64) | User ID  
»» contract | string | Futures contract  
»» size | string | Position size  
»» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
»» risk_limit | string | Position risk limit  
»» leverage_max | string | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
»» maintenance_rate | string | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
»» value | string | Position value calculated in settlement currency  
»» margin | string | Position margin  
»» entry_price | string | Entry price  
»» liq_price | string | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
»» mark_price | string | Current mark price  
»» initial_margin | string | Initial margin of postions  
»» maintenance_margin | string | Maintencance margin of postions  
»» unrealised_pnl | string | Unrealized PNL  
»» realised_pnl | string | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
»» pnl_pnl | string | settled pnl when closing postion  
»» pnl_fund | string | funding fees  
»» pnl_fee | string | trading fees  
»» history_pnl | string | Total realized PnL from closed positions  
»» last_close_pnl | string | PNL of last position close  
»» realised_point | string | Realized POINT PNL  
»» history_point | string | History realized POINT PNL  
»» adl_ranking | integer | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
»» pending_orders | integer | Current pending order quantity  
»» close_order | object|null | Current close order information, or `null` if no close order  
»»» id | integer(int64) | Order ID  
»»» price | string | Order price  
»»» is_liq | boolean | Whether the close order is from liquidation  
»» mode | string | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
»» cross_leverage_limit | string | leverage for cross margin  
»» update_time | integer(int64) | Last update time  
»» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
»» open_time | integer(int64) | First Open Time  
»» risk_limit_table | string | Risk limit table ID  
»» average_maintenance_rate | string | Average maintenance margin rate  
»» pid | integer(int64) | Sub-account position ID  
»» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
»» lever | string | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/futures/usdt/dual_comp/positions/BTC_USDT/risk_limit'
    query_param = 'risk_limit=1000000'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/futures/usdt/dual_comp/positions/BTC_USDT/risk_limit"
    query_param="risk_limit=1000000"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "leverage": "0",
        "risk_limit": "100",
        "leverage_max": "100",
        "maintenance_rate": "0.005",
        "value": "3568.62",
        "margin": "4.431548146258",
        "entry_price": "3779.55",
        "liq_price": "99999999",
        "mark_price": "3780.32",
        "unrealised_pnl": "-0.000507486844",
        "realised_pnl": "0.045543982432",
        "pnl_pnl": "0.045543982432",
        "pnl_fund": "0",
        "pnl_fee": "0",
        "history_pnl": "0",
        "last_close_pnl": "0",
        "realised_point": "0",
        "history_point": "0",
        "adl_ranking": 5,
        "pending_orders": 16,
        "close_order": {
          "id": 232323,
          "price": "3779",
          "is_liq": false
        },
        "mode": "single",
        "update_time": 1684994406,
        "update_id": 1,
        "cross_leverage_limit": "0",
        "risk_limit_table": "BIG_HOT_COIN_50X_V2",
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  Query futures order list🔒 Authenticated

GET`/futures/{settle}/orders`

GET `/futures/{settle}/orders`

_Query futures order list_

  * Zero-fill order cannot be retrieved for 10 minutes after cancellation
  * Historical orders, by default, only data within the past 6 months is supported. If you need to query data for a longer period, please use `GET /futures/{settle}/orders_timerange`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Optional | Futures contract, return related data only if specified  
status | query | string | Required | Query order list based on status  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
last_id | query | string | Optional | Use the ID of the last record in the previous list as the starting point for the next list  
  
Operations based on custom IDs can only be checked when orders are pending. After orders are completed (filled/cancelled), they can be checked within 1 hour after completion. After expiration, only order IDs can be used  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**last_id** : Use the ID of the last record in the previous list as the starting point for the next list  
  
Operations based on custom IDs can only be checked when orders are pending. After orders are completed (filled/cancelled), they can be checked within 1 hour after completion. After expiration, only order IDs can be used

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FuturesOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures order details]  
» _None_ | FuturesOrder | Futures order details  
»» id | integer(int64) | Futures order ID  
»» user | integer | User ID  
»» create_time | number(double) | Creation time of order  
»» update_time | number(double) | OrderUpdateTime  
»» finish_time | number(double) | Order finished time. Not returned if order is open  
»» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
»» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
»» contract | string | Futures contract  
»» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
»» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
»» price | string | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
»» is_close | boolean | Is the order to close position  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_liq | boolean | Is the order for liquidation  
»» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
»» left | string | Unfilled quantity  
»» fill_price | string | Fill price  
»» text | string | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
»» tkfr | string | Taker fee  
»» mkfr | string | Maker fee  
»» refu | integer | Referrer user ID  
»» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
»» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
»» amend_text | string | The custom data that the user remarked when amending the order  
»» market_order_slip_ratio | string | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
»» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
»» action_mode | string | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
»» tpsl_tp_trigger_price | string | Take profit price  
»» tpsl_sl_trigger_price | string | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
###  Response Headers

Response HeadersStatus | Header | Type | Format | Description  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | Limit specified for pagination  
200 | X-Pagination-Offset | integer |  | Offset specified for pagination  
  
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
    
    url = '/futures/usdt/orders'
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
    url="/futures/usdt/orders"
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
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968,
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
        "price": "3765",
        "fill_price": "0",
        "mkfr": "-0.00025",
        "tkfr": "0.00075",
        "tif": "gtc",
        "refu": 0,
        "is_reduce_only": false,
        "is_close": false,
        "is_liq": false,
        "text": "t-my-custom-id",
        "status": "finished",
        "finish_time": 1514764900,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "order_value": "64112.2099000000005",
        "trade_value": "64112.2099000000005",
        "market_order_slip_ratio": "0.03",
        "pos_margin_mode": "isolated",
        "tpsl_tp_trigger_price": "3800",
        "tpsl_sl_trigger_price": "3700"
      }
    ]
    

##  Place futures order🔒 Authenticated

POST`/futures/{settle}/orders`

POST `/futures/{settle}/orders`

_Place futures order_

  * When placing an order, the number of contracts is specified `size`, not the number of coins. The number of coins corresponding to each contract is returned in the contract details interface `quanto_multiplier`
  * 0 The order that was completed cannot be obtained after 10 minutes of withdrawal, and the order will be mentioned that the order does not exist
  * Setting `reduce_only` to `true` can prevent the position from being penetrated when reducing the position
  * In single-position mode, if you need to close the position, you need to set `size` to 0 and `close` to `true`
  * In dual warehouse mode,
  * Reduce position: reduce_only=true, size is a positive number that indicates short position, negative number that indicates long position
  * Add number that indicates adding long positions, and negative numbers indicate adding short positions
  * Close position: size=0, set the direction of closing position according to auto_size, and set `reduce_only` to true at the same time - reduce_only: Make sure to only perform position reduction operations to prevent increased positions
  * Set `stp_act` to determine the use of a strategy that restricts user transactions. For detailed usage, refer to the body parameter `stp_act`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | FuturesOrder | Required | none  
↳ contract | body | string | Required | Futures contract  
↳ size | body | string | Required | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
↳ iceberg | body | string | Optional | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
↳ price | body | string | Required | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
↳ close | body | boolean | Optional | Set as `true` to close the position, with `size` set to 0  
↳ reduce_only | body | boolean | Optional | Set as `true` to be reduce-only order  
↳ tif | body | string | Optional | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
↳ text | body | string | Optional | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
↳ auto_size | body | string | Optional | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
↳ stp_act | body | string | Optional | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
↳ pid | body | integer(int64) | Optional | Position ID  
↳ market_order_slip_ratio | body | string | Optional | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
↳ pos_margin_mode | body | string | Optional | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
↳ action_mode | body | string | Optional | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
↳ tpsl_tp_trigger_price | body | string | Optional | Take profit price  
↳ tpsl_sl_trigger_price | body | string | Optional | Stop loss price  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**» tif** : Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none

**» text** : Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal

**» stp_act** : Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled

**» action_mode** : Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» tif | gtc  
» tif | ioc  
» tif | poc  
» tif | fok  
» auto_size | close_long  
» auto_size | close_short  
» stp_act | co  
» stp_act | cn  
» stp_act | cb  
» stp_act | -  
settle | btc  
settle | usdt  
  
### Responses

  * 201[Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2)Order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order details | FuturesOrder  
  
### Response Schema

Status Code **201**

_Futures order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Futures order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
» update_time | number(double) | OrderUpdateTime  
» finish_time | number(double) | Order finished time. Not returned if order is open  
» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
» contract | string | Futures contract  
» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
» left | string | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
» tkfr | string | Taker fee  
» mkfr | string | Maker fee  
» refu | integer | Referrer user ID  
» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
» amend_text | string | The custom data that the user remarked when amending the order  
» market_order_slip_ratio | string | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
» action_mode | string | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
» tpsl_tp_trigger_price | string | Take profit price  
» tpsl_sl_trigger_price | string | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/futures/usdt/orders'
    query_param = ''
    body='{"contract":"BTC_USDT","size":"6024","iceberg":"0","price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-","order_value":"64112.2099000000005","trade_value":"64112.2099000000005","market_order_slip_ratio":"0.03","pos_margin_mode":"isolated","tpsl_tp_trigger_price":"3800","tpsl_sl_trigger_price":"3700"}'
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
    url="/futures/usdt/orders"
    query_param=""
    body_param='{"contract":"BTC_USDT","size":"6024","iceberg":"0","price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-","order_value":"64112.2099000000005","trade_value":"64112.2099000000005","market_order_slip_ratio":"0.03","pos_margin_mode":"isolated","tpsl_tp_trigger_price":"3800","tpsl_sl_trigger_price":"3700"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "contract": "BTC_USDT",
      "size": "6024",
      "iceberg": "0",
      "price": "3765",
      "tif": "gtc",
      "text": "t-my-custom-id",
      "stp_act": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

> Example responses

> 201 Response
    
    
    {
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
      "price": "3765",
      "fill_price": "0",
      "mkfr": "-0.00025",
      "tkfr": "0.00075",
      "tif": "gtc",
      "refu": 0,
      "is_reduce_only": false,
      "is_close": false,
      "is_liq": false,
      "text": "t-my-custom-id",
      "status": "finished",
      "finish_time": 1514764900,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  Cancel all orders with 'open' status🔒 Authenticated

DELETE`/futures/{settle}/orders`

DELETE `/futures/{settle}/orders`

_Cancel all orders with 'open' status_

Zero-fill orders cannot be retrieved 10 minutes after order cancellation

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
contract | query | string | Optional | Contract Identifier; if specified, only cancel pending orders related to this contract  
action_mode | query | string | Optional | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
side | query | string | Optional | Specify all buy orders or all sell orders, both are included if not specified. Set to bid to cancel all buy orders, set to ask to cancel all sell orders  
exclude_reduce_only | query | boolean | Optional | Whether to exclude reduce-only orders  
text | query | string | Optional | Remark for order cancellation  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**action_mode** : Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Batch cancellation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancellation successful | [FuturesOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures order details]  
» _None_ | FuturesOrder | Futures order details  
»» id | integer(int64) | Futures order ID  
»» user | integer | User ID  
»» create_time | number(double) | Creation time of order  
»» update_time | number(double) | OrderUpdateTime  
»» finish_time | number(double) | Order finished time. Not returned if order is open  
»» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
»» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
»» contract | string | Futures contract  
»» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
»» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
»» price | string | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
»» is_close | boolean | Is the order to close position  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_liq | boolean | Is the order for liquidation  
»» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
»» left | string | Unfilled quantity  
»» fill_price | string | Fill price  
»» text | string | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
»» tkfr | string | Taker fee  
»» mkfr | string | Maker fee  
»» refu | integer | Referrer user ID  
»» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
»» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
»» amend_text | string | The custom data that the user remarked when amending the order  
»» market_order_slip_ratio | string | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
»» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
»» action_mode | string | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
»» tpsl_tp_trigger_price | string | Take profit price  
»» tpsl_sl_trigger_price | string | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/futures/usdt/orders'
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
    url="/futures/usdt/orders"
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
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968,
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
        "price": "3765",
        "fill_price": "0",
        "mkfr": "-0.00025",
        "tkfr": "0.00075",
        "tif": "gtc",
        "refu": 0,
        "is_reduce_only": false,
        "is_close": false,
        "is_liq": false,
        "text": "t-my-custom-id",
        "status": "finished",
        "finish_time": 1514764900,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "order_value": "64112.2099000000005",
        "trade_value": "64112.2099000000005",
        "market_order_slip_ratio": "0.03",
        "pos_margin_mode": "isolated",
        "tpsl_tp_trigger_price": "3800",
        "tpsl_sl_trigger_price": "3700"
      }
    ]
    

##  Query futures order list by time range🔒 Authenticated

GET`/futures/{settle}/orders_timerange`

GET `/futures/{settle}/orders_timerange`

_Query futures order list by time range_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FuturesOrderTimerange]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures order details]  
» _None_ | FuturesOrderTimerange | Futures order details  
»» id | integer(int64) | Futures order ID  
»» user | integer | User ID  
»» create_time | number(double) | Creation time of order  
»» update_time | string | OrderUpdateTime  
»» finish_time | string | Order finished time. Not returned if order is open  
»» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
»» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
»» contract | string | Futures contract  
»» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
»» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
»» price | string | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
»» is_close | boolean | Is the order to close position  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_liq | boolean | Is the order for liquidation  
»» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
»» left | string | Unfilled quantity  
»» fill_price | string | Fill price  
»» text | string | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
»» tkfr | string | Taker fee  
»» mkfr | string | Maker fee  
»» refu | integer | Referrer user ID  
»» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
»» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
»» amend_text | string | The custom data that the user remarked when amending the order  
»» market_order_slip_ratio | string | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
»» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
»» tpsl_tp_trigger_price | string | Take profit price  
»» tpsl_sl_trigger_price | string | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
###  Response Headers

Response HeadersStatus | Header | Type | Format | Description  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | Limit specified for pagination  
200 | X-Pagination-Offset | integer |  | Offset specified for pagination  
  
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
    
    url = '/futures/usdt/orders_timerange'
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
    url="/futures/usdt/orders_timerange"
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
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968,
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
        "price": "3765",
        "fill_price": "0",
        "mkfr": "-0.00025",
        "tkfr": "0.00075",
        "tif": "gtc",
        "refu": 0,
        "is_reduce_only": false,
        "is_close": false,
        "is_liq": false,
        "text": "t-my-custom-id",
        "status": "finished",
        "finish_time": 1514764900,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "order_value": "64112.2099000000005",
        "trade_value": "64112.2099000000005",
        "market_order_slip_ratio": "0.03",
        "pos_margin_mode": "isolated",
        "tpsl_tp_trigger_price": "3800",
        "tpsl_sl_trigger_price": "3700"
      }
    ]
    

##  Place batch futures orders🔒 Authenticated

POST`/futures/{settle}/batch_orders`

POST `/futures/{settle}/batch_orders`

_Place batch futures orders_

  * Up to 10 orders per request
  * If any of the order's parameters are missing or in the wrong format, all of them will not be executed, and a http status 400 error will be returned directly
  * If the parameters are checked and passed, all are executed. Even if there is a business logic error in the middle (such as insufficient funds), it will not affect other execution orders
  * The returned result is in array format, and the order corresponds to the orders in the request body
  * In the returned result, the `succeeded` field of type bool indicates whether the execution was successful or not
  * If the execution is successful, the normal order content is included; if the execution fails, the `label` field is included to indicate the cause of the error
  * In the rate limiting, each order is counted individually

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | array[FuturesOrder] | Required | none  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request execution completed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request execution completed | [BatchFuturesOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures order details]  
» _None_ | BatchFuturesOrder | Futures order details  
»» succeeded | boolean | Request execution result  
»» label | string | Error label, only exists if execution fails  
»» detail | string | Error detail, only present if execution failed and details need to be given  
»» id | integer(int64) | Futures order ID  
»» user | integer | User ID  
»» create_time | number(double) | Creation time of order  
»» finish_time | number(double) | Order finished time. Not returned if order is open  
»» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
»» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
»» contract | string | Futures contract  
»» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
»» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
»» price | string | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
»» is_close | boolean | Is the order to close position  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_liq | boolean | Is the order for liquidation  
»» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
»» left | string | Unfilled quantity  
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
»» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
»» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
»» market_order_slip_ratio | string | The maximum slippage ratio  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/futures/usdt/batch_orders'
    query_param = ''
    body='[{"contract":"BTC_USDT","size":"6024","iceberg":"0","price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-","order_value":"64112.2099000000005","trade_value":"64112.2099000000005","market_order_slip_ratio":"0.03","pos_margin_mode":"isolated","tpsl_tp_trigger_price":"3800","tpsl_sl_trigger_price":"3700"}]'
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
    url="/futures/usdt/batch_orders"
    query_param=""
    body_param='[{"contract":"BTC_USDT","size":"6024","iceberg":"0","price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-","order_value":"64112.2099000000005","trade_value":"64112.2099000000005","market_order_slip_ratio":"0.03","pos_margin_mode":"isolated","tpsl_tp_trigger_price":"3800","tpsl_sl_trigger_price":"3700"}]'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    [
      {
        "contract": "BTC_USDT",
        "size": "6024",
        "iceberg": "0",
        "price": "3765",
        "tif": "gtc",
        "text": "t-my-custom-id",
        "stp_act": "-",
        "order_value": "64112.2099000000005",
        "trade_value": "64112.2099000000005",
        "market_order_slip_ratio": "0.03",
        "pos_margin_mode": "isolated",
        "tpsl_tp_trigger_price": "3800",
        "tpsl_sl_trigger_price": "3700"
      }
    ]
    

> Example responses

> 200 Response
    
    
    [
      {
        "succeeded": true,
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968,
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
        "price": "3765",
        "fill_price": "0",
        "mkfr": "-0.00025",
        "tkfr": "0.00075",
        "tif": "gtc",
        "refu": 0,
        "is_reduce_only": false,
        "is_close": false,
        "is_liq": false,
        "text": "t-my-custom-id",
        "status": "finished",
        "finish_time": 1514764900,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "market_order_slip_ratio": "0.03"
      }
    ]
    

##  Query single order details🔒 Authenticated

GET`/futures/{settle}/orders/{order_id}`

GET `/futures/{settle}/orders/{order_id}`

_Query single order details_

  * Zero-fill order cannot be retrieved for 10 minutes after cancellation
  * Historical orders, by default, only data within the past 6 months is supported.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
order_id | path | string | Required | The order ID returned when the order is created successfully, or the custom ID specified by the user when creating the order (i.e. the `text` field). When using the custom `text` field:  
1\. If the order was not filled and has been cancelled, after 60 seconds you cannot query the order by `text`; continuing to use `text` returns error ORDER_NOT_FOUND.  
2\. If the order was fully or partially filled, you can query the order by `text` indefinitely.  
  
####  Detailed descriptions

**order_id** : The order ID returned when the order is created successfully, or the custom ID specified by the user when creating the order (i.e. the `text` field). When using the custom `text` field:  
1\. If the order was not filled and has been cancelled, after 60 seconds you cannot query the order by `text`; continuing to use `text` returns error ORDER_NOT_FOUND.  
2\. If the order was fully or partially filled, you can query the order by `text` indefinitely.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order details | FuturesOrder  
  
### Response Schema

Status Code **200**

_Futures order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Futures order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
» update_time | number(double) | OrderUpdateTime  
» finish_time | number(double) | Order finished time. Not returned if order is open  
» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
» contract | string | Futures contract  
» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
» left | string | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
» tkfr | string | Taker fee  
» mkfr | string | Maker fee  
» refu | integer | Referrer user ID  
» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
» amend_text | string | The custom data that the user remarked when amending the order  
» market_order_slip_ratio | string | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
» action_mode | string | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
» tpsl_tp_trigger_price | string | Take profit price  
» tpsl_sl_trigger_price | string | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/futures/usdt/orders/12345'
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
    url="/futures/usdt/orders/12345"
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
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
      "price": "3765",
      "fill_price": "0",
      "mkfr": "-0.00025",
      "tkfr": "0.00075",
      "tif": "gtc",
      "refu": 0,
      "is_reduce_only": false,
      "is_close": false,
      "is_liq": false,
      "text": "t-my-custom-id",
      "status": "finished",
      "finish_time": 1514764900,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  Amend single order🔒 Authenticated

PUT`/futures/{settle}/orders/{order_id}`

PUT `/futures/{settle}/orders/{order_id}`

_Amend single order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | FuturesOrderAmendment | Required | none  
↳ size | body | string | Optional | New order size, including filled part.  
  
\- If new size is less than or equal to filled size, the order will be cancelled.  
\- Order side must be identical to the original one.  
\- Close order size cannot be changed.  
\- For reduce only orders, increasing size may leads to other reduce only orders being cancelled.  
\- If price is not changed, decreasing size will not change its precedence in order book, while increasing will move it to the last at current price.  
↳ price | body | string | Optional | New order price  
↳ amend_text | body | string | Optional | Custom info during order amendment  
↳ text | body | string | Optional | Internal users can modify information in the text field.  
↳ action_mode | body | string | Optional | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
settle | path | string | Required | Settle currency  
order_id | path | string | Required | The order ID returned when the order is created successfully, or the custom ID specified by the user when creating the order (i.e. the `text` field). When using the custom `text` field:  
1\. If the order was not filled and has been cancelled, after 60 seconds you cannot query the order by `text`; continuing to use `text` returns error ORDER_NOT_FOUND.  
2\. If the order was fully or partially filled, you can query the order by `text` indefinitely.  
  
####  Detailed descriptions

**» size** : New order size, including filled part.  
  
\- If new size is less than or equal to filled size, the order will be cancelled.  
\- Order side must be identical to the original one.  
\- Close order size cannot be changed.  
\- For reduce only orders, increasing size may leads to other reduce only orders being cancelled.  
\- If price is not changed, decreasing size will not change its precedence in order book, while increasing will move it to the last at current price.

**» action_mode** : Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)

**order_id** : The order ID returned when the order is created successfully, or the custom ID specified by the user when creating the order (i.e. the `text` field). When using the custom `text` field:  
1\. If the order was not filled and has been cancelled, after 60 seconds you cannot query the order by `text`; continuing to use `text` returns error ORDER_NOT_FOUND.  
2\. If the order was fully or partially filled, you can query the order by `text` indefinitely.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order details | FuturesOrder  
  
### Response Schema

Status Code **200**

_Futures order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Futures order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
» update_time | number(double) | OrderUpdateTime  
» finish_time | number(double) | Order finished time. Not returned if order is open  
» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
» contract | string | Futures contract  
» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
» left | string | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
» tkfr | string | Taker fee  
» mkfr | string | Maker fee  
» refu | integer | Referrer user ID  
» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
» amend_text | string | The custom data that the user remarked when amending the order  
» market_order_slip_ratio | string | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
» action_mode | string | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
» tpsl_tp_trigger_price | string | Take profit price  
» tpsl_sl_trigger_price | string | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/futures/usdt/orders/12345'
    query_param = ''
    body='{"size":"100","price":"54321","contract":"BTC_USDT"}'
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
    url="/futures/usdt/orders/12345"
    query_param=""
    body_param='{"size":"100","price":"54321","contract":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "size": "100",
      "price": "54321",
      "contract": "BTC_USDT"
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
      "price": "3765",
      "fill_price": "0",
      "mkfr": "-0.00025",
      "tkfr": "0.00075",
      "tif": "gtc",
      "refu": 0,
      "is_reduce_only": false,
      "is_close": false,
      "is_liq": false,
      "text": "t-my-custom-id",
      "status": "finished",
      "finish_time": 1514764900,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  Cancel single order🔒 Authenticated

DELETE`/futures/{settle}/orders/{order_id}`

DELETE `/futures/{settle}/orders/{order_id}`

_Cancel single order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
action_mode | query | string | Optional | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
settle | path | string | Required | Settle currency  
order_id | path | string | Required | The order ID returned when the order is created successfully, or the custom ID specified by the user when creating the order (i.e. the `text` field). When using the custom `text` field:  
1\. If the order was not filled and has been cancelled, after 60 seconds you cannot query the order by `text`; continuing to use `text` returns error ORDER_NOT_FOUND.  
2\. If the order was fully or partially filled, you can query the order by `text` indefinitely.  
  
####  Detailed descriptions

**action_mode** : Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)

**order_id** : The order ID returned when the order is created successfully, or the custom ID specified by the user when creating the order (i.e. the `text` field). When using the custom `text` field:  
1\. If the order was not filled and has been cancelled, after 60 seconds you cannot query the order by `text`; continuing to use `text` returns error ORDER_NOT_FOUND.  
2\. If the order was fully or partially filled, you can query the order by `text` indefinitely.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order details | FuturesOrder  
  
### Response Schema

Status Code **200**

_Futures order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Futures order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
» update_time | number(double) | OrderUpdateTime  
» finish_time | number(double) | Order finished time. Not returned if order is open  
» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
» contract | string | Futures contract  
» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
» left | string | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
» tkfr | string | Taker fee  
» mkfr | string | Maker fee  
» refu | integer | Referrer user ID  
» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
» amend_text | string | The custom data that the user remarked when amending the order  
» market_order_slip_ratio | string | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
» action_mode | string | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
» tpsl_tp_trigger_price | string | Take profit price  
» tpsl_sl_trigger_price | string | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/futures/usdt/orders/12345'
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
    url="/futures/usdt/orders/12345"
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
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
      "price": "3765",
      "fill_price": "0",
      "mkfr": "-0.00025",
      "tkfr": "0.00075",
      "tif": "gtc",
      "refu": 0,
      "is_reduce_only": false,
      "is_close": false,
      "is_liq": false,
      "text": "t-my-custom-id",
      "status": "finished",
      "finish_time": 1514764900,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  Query personal trading records🔒 Authenticated

GET`/futures/{settle}/my_trades`

GET `/futures/{settle}/my_trades`

_Query personal trading records_

By default, only supports querying data within 6 months. For older data, use `GET /futures/{settle}/my_trades_timerange`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
order | query | integer(int64) | Optional | Futures order ID, return related data only if specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
last_id | query | string | Optional | Specify the starting point for this list based on a previously retrieved id  
  
This parameter is deprecated. If you need to iterate through and retrieve more records, we recommend using 'GET /futures/{settle}/my_trades_timerange'.  
  
####  Detailed descriptions

**last_id** : Specify the starting point for this list based on a previously retrieved id  
  
This parameter is deprecated. If you need to iterate through and retrieve more records, we recommend using 'GET /futures/{settle}/my_trades_timerange'.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [MyFuturesTrade]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int64) | Fill ID  
» create_time | number(double) | Fill Time  
» contract | string | Futures contract  
» order_id | string | Related order ID  
» size | string | Trading size  
» close_size | string | Number of closed positions:  
  
close_size=0 && size＞0 Open long position  
close_size=0 && size＜0 Open short position  
close_size>0 && size>0 && size <= close_size Close short position  
close_size>0 && size>0 && size > close_size Close short position and open long position  
close_size<0 && size<0 && size >= close_size Close long position  
close_size<0 && size<0 && size < close_size Close long position and open short position  
» price | string | Fill Price  
» role | string | Trade role. taker - taker, maker - maker  
» text | string | Order custom information  
» fee | string | Trade fee  
» point_fee | string | Points used to deduct trade fee  
» trade_value | string | trade value  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
role | taker  
role | maker  
  
###  Response Headers

Response HeadersStatus | Header | Type | Format | Description  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | Limit specified for pagination  
200 | X-Pagination-Offset | integer |  | Offset specified for pagination  
  
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
    
    url = '/futures/usdt/my_trades'
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
    url="/futures/usdt/my_trades"
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
        "id": 121234231,
        "create_time": 1514764800.123,
        "contract": "BTC_USDT",
        "order_id": "21893289839",
        "size": "100",
        "price": "100.123",
        "text": "t-123456",
        "fee": "0.01",
        "point_fee": "0",
        "role": "taker",
        "close_size": "0",
        "trade_value": "28601.83"
      }
    ]
    

##  Query personal trading records by time range🔒 Authenticated

GET`/futures/{settle}/my_trades_timerange`

GET `/futures/{settle}/my_trades_timerange`

_Query personal trading records by time range_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
role | query | string | Optional | Query role, maker or taker  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [MyFuturesTradeTimeRange]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» trade_id | string | Fill ID  
» create_time | number(double) | Fill Time  
» contract | string | Futures contract  
» order_id | string | Related order ID  
» size | string | Trading size  
» close_size | string | Number of closed positions:  
  
close_size=0 && size＞0 Open long position  
close_size=0 && size＜0 Open short position  
close_size>0 && size>0 && size <= close_size Close short position  
close_size>0 && size>0 && size > close_size Close short position and open long position  
close_size<0 && size<0 && size >= close_size Close long position  
close_size<0 && size<0 && size < close_size Close long position and open short position  
» price | string | Fill Price  
» role | string | Trade role. taker - taker, maker - maker  
» text | string | Order custom information  
» fee | string | Trade fee  
» point_fee | string | Points used to deduct trade fee  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
role | taker  
role | maker  
  
###  Response Headers

Response HeadersStatus | Header | Type | Format | Description  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | Limit specified for pagination  
200 | X-Pagination-Offset | integer |  | Offset specified for pagination  
  
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
    
    url = '/futures/usdt/my_trades_timerange'
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
    url="/futures/usdt/my_trades_timerange"
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
        "trade_id": "121234231",
        "create_time": 1514764800.123,
        "contract": "BTC_USDT",
        "order_id": "21893289839",
        "size": "100",
        "price": "100.123",
        "text": "t-123456",
        "fee": "0.01",
        "point_fee": "0",
        "role": "taker",
        "close_size": "0"
      }
    ]
    

##  Query position close history🔒 Authenticated

GET`/futures/{settle}/position_close`

GET `/futures/{settle}/position_close`

_Query position close history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
side | query | string | Optional | Query side. long or shot  
pnl | query | string | Optional | Query profit or loss  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [PositionClose]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | number(double) | Position close time  
» contract | string | Futures contract  
» side | string | Position side  
  
\- `long`: Long position  
\- `short`: Short position  
» pnl | string | PnL  
» pnl_pnl | string | PNL - Position P/L  
» pnl_fund | string | PNL - Funding Fees  
» pnl_fee | string | PNL - Transaction Fees  
» text | string | Source of close order. See `order.text` field for specific values  
» max_size | string | Max Trade Size  
» accum_size | string | Cumulative closed position volume  
» first_open_time | integer(int64) | First Open Time  
» long_price | string | When side is 'long', it indicates the opening average price; when side is 'short', it indicates the closing average price  
» short_price | string | When side is 'long', it indicates the closing average price; when side is 'short', it indicates the opening average price  
  
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
    
    url = '/futures/usdt/position_close'
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
    url="/futures/usdt/position_close"
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
        "time": 1546487347,
        "pnl": "0.00013",
        "pnl_pnl": "0.00011",
        "pnl_fund": "0.00001",
        "pnl_fee": "0.00001",
        "side": "long",
        "contract": "BTC_USDT",
        "text": "web",
        "max_size": "100",
        "accum_size": "100",
        "first_open_time": 1546487347,
        "long_price": "2026.87",
        "short_price": "2544.4"
      }
    ]
    

##  Query liquidation history🔒 Authenticated

GET`/futures/{settle}/liquidates`

GET `/futures/{settle}/liquidates`

_Query liquidation history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
at | query | integer | Optional | Specify liquidation timestamp  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FuturesLiquidate]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | integer(int64) | Liquidation time  
» contract | string | Futures contract  
» leverage | string | Position leverage. Not returned in public endpoints  
» size | string | Position size  
» margin | string | Position margin. Not returned in public endpoints  
» entry_price | string | Average entry price. Not returned in public endpoints  
» liq_price | string | Liquidation price. Not returned in public endpoints  
» mark_price | string | Mark price. Not returned in public endpoints  
» order_id | integer(int64) | Liquidation order ID. Not returned in public endpoints  
» order_price | string | Liquidation order price  
» fill_price | string | Liquidation order average taker price  
» left | string | Liquidation order maker size  
  
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
    
    url = '/futures/usdt/liquidates'
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
    url="/futures/usdt/liquidates"
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
        "time": 1548654951,
        "contract": "BTC_USDT",
        "size": "600",
        "leverage": "25",
        "margin": "0.006705256878",
        "entry_price": "3536.123",
        "liq_price": "3421.54",
        "mark_price": "3420.27",
        "order_id": 317393847,
        "order_price": "3405",
        "fill_price": "3424",
        "left": "0"
      }
    ]
    

##  Query ADL auto-deleveraging order information🔒 Authenticated

GET`/futures/{settle}/auto_deleverages`

GET `/futures/{settle}/auto_deleverages`

_Query ADL auto-deleveraging order information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
at | query | integer | Optional | Specify auto-deleveraging timestamp  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FuturesAutoDeleverage]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | integer(int64) | Automatic deleveraging time  
» user | integer(int64) | User ID  
» order_id | integer(int64) | Order ID. Order IDs before 2023-02-20 are null  
» contract | string | Futures contract  
» leverage | string | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
» cross_leverage_limit | string | leverage for cross margin  
» entry_price | string | Average entry price  
» fill_price | string | Average fill price  
» trade_size | string | Trading size  
» position_size | string | Positions after auto-deleveraging  
  
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
    
    url = '/futures/usdt/auto_deleverages'
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
    url="/futures/usdt/auto_deleverages"
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
        "time": 1675841679,
        "contract": "ACH_USDT",
        "order_id": 73873128,
        "user": 1666,
        "cross_leverage_limit": "0",
        "leverage": "0",
        "entry_price": "2649.648633636364",
        "fill_price": "2790.8082",
        "position_size": "1",
        "trade_size": "-10"
      }
    ]
    

##  Countdown cancel orders🔒 Authenticated

POST`/futures/{settle}/countdown_cancel_all`

POST `/futures/{settle}/countdown_cancel_all`

_Countdown cancel orders_

Heartbeat detection for contract orders: When the user-set `timeout` time is reached, if neither the existing countdown is canceled nor a new countdown is set, the relevant contract orders will be automatically canceled. This API can be called repeatedly to or cancel the countdown. Usage example: Repeatedly call this API at 30-second intervals, setting the `timeout` to 30 (seconds) each time. If this API is not called again within 30 seconds, all open orders on your specified `market` will be automatically canceled. If the `timeout` is set to 0 within 30 seconds, the countdown timer will terminate, and the automatic order cancellation function will be disabled.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CountdownCancelAllFuturesTask | Required | none  
↳ timeout | body | integer(int32) | Required | Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown  
↳ contract | body | string | Optional | Futures contract  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**» timeout** : Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
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
    
    url = '/futures/usdt/countdown_cancel_all'
    query_param = ''
    body='{"timeout":30,"contract":"BTC_USDT"}'
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
    url="/futures/usdt/countdown_cancel_all"
    query_param=""
    body_param='{"timeout":30,"contract":"BTC_USDT"}'
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
      "contract": "BTC_USDT"
    }
    

> Example responses

> 200 Response
    
    
    {
      "triggerTime": "1660039145000"
    }
    

##  Query futures market trading fee rates🔒 Authenticated

GET`/futures/{settle}/fee`

GET `/futures/{settle}/fee`

_Query futures market trading fee rates_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract, return related data only if specified  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Inline  
  
### Response Schema

Status Code **200**

_FuturesFee_

Name | Type | Description  
---|---|---  
» **additionalProperties** | FuturesFee | The returned result is a map type, where the key represents the market and taker and maker fee rates  
»» taker_fee | string | Taker fee  
»» maker_fee | string | maker fee  
  
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
    
    url = '/futures/usdt/fee'
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
    url="/futures/usdt/fee"
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
      "1INCH_USDT": {
        "taker_fee": "0.00025",
        "maker_fee": "-0.00010"
      },
      "AAVE_USDT": {
        "taker_fee": "0.00025",
        "maker_fee": "-0.00010"
      }
    }
    

##  Cancel batch orders by specified ID list🔒 Authenticated

POST`/futures/{settle}/batch_cancel_orders`

POST `/futures/{settle}/batch_cancel_orders`

_Cancel batch orders by specified ID list_

Multiple different order IDs can be specified. A maximum of 20 records can be cancelled in one request

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | CancelBatchFutureOrdersRequest | Required | none  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order cancellation operation completed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order cancellation operation completed | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» FutureCancelOrderResult | object | Order cancellation result  
»» id | string | Order ID  
»» user_id | integer(int64) | User ID  
»» succeeded | boolean | Whether cancellation succeeded  
»» message | string | Error description when cancellation fails, empty if successful  
  
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
    
    url = '/futures/usdt/batch_cancel_orders'
    query_param = ''
    body='["1","2","3"]'
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
    url="/futures/usdt/batch_cancel_orders"
    query_param=""
    body_param='["1","2","3"]'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    [
      "1",
      "2",
      "3"
    ]
    

> Example responses

> 200 Response
    
    
    [
      {
        "user_id": 111,
        "id": "123456",
        "succeeded": true,
        "message": ""
      }
    ]
    

##  Batch modify orders by specified IDs🔒 Authenticated

POST`/futures/{settle}/batch_amend_orders`

POST `/futures/{settle}/batch_amend_orders`

_Batch modify orders by specified IDs_

Multiple different order IDs can be specified. A maximum of 10 orders can be modified in one request

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | array[BatchAmendOrderReq] | Required | none  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request execution completed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request execution completed | [BatchFuturesOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures order details]  
» _None_ | BatchFuturesOrder | Futures order details  
»» succeeded | boolean | Request execution result  
»» label | string | Error label, only exists if execution fails  
»» detail | string | Error detail, only present if execution failed and details need to be given  
»» id | integer(int64) | Futures order ID  
»» user | integer | User ID  
»» create_time | number(double) | Creation time of order  
»» finish_time | number(double) | Order finished time. Not returned if order is open  
»» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
»» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
»» contract | string | Futures contract  
»» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
»» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
»» price | string | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
»» is_close | boolean | Is the order to close position  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_liq | boolean | Is the order for liquidation  
»» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
»» left | string | Unfilled quantity  
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
»» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
»» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
»» market_order_slip_ratio | string | The maximum slippage ratio  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/futures/usdt/batch_amend_orders'
    query_param = ''
    body='[{"order_id":121212,"amend_text":"batch amend text","size":"100","price":"54321"}]'
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
    url="/futures/usdt/batch_amend_orders"
    query_param=""
    body_param='[{"order_id":121212,"amend_text":"batch amend text","size":"100","price":"54321"}]'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    [
      {
        "order_id": 121212,
        "amend_text": "batch amend text",
        "size": "100",
        "price": "54321"
      }
    ]
    

> Example responses

> 200 Response
    
    
    [
      {
        "succeeded": true,
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968,
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
        "price": "3765",
        "fill_price": "0",
        "mkfr": "-0.00025",
        "tkfr": "0.00075",
        "tif": "gtc",
        "refu": 0,
        "is_reduce_only": false,
        "is_close": false,
        "is_liq": false,
        "text": "t-my-custom-id",
        "status": "finished",
        "finish_time": 1514764900,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "market_order_slip_ratio": "0.03"
      }
    ]
    

##  Query risk limit table by table_id

GET`/futures/{settle}/risk_limit_table`

GET `/futures/{settle}/risk_limit_table`

_Query risk limit table by table_id_

Just pass table_id

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
table_id | query | string | Required | Risk limit table ID  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [FuturesRiskLimitTier]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Information for each tier of the gradient risk limit table]  
» _None_ | FuturesRiskLimitTier | Information for each tier of the gradient risk limit table  
»» tier | integer(int) | Tier  
»» risk_limit | string | Position risk limit  
»» initial_rate | string | Initial margin rate  
»» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
»» leverage_max | string | Maximum leverage  
»» deduction | string | Maintenance margin quick calculation deduction amount  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/risk_limit_table'
    query_param = 'table_id=CYBER_USDT_20241122'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/risk_limit_table?table_id=CYBER_USDT_20241122 \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "tier": 1,
        "risk_limit": "10000",
        "initial_rate": "0.025",
        "maintenance_rate": "0.015",
        "leverage_max": "40",
        "deduction": "0"
      },
      {
        "tier": 2,
        "risk_limit": "30000",
        "initial_rate": "0.03333",
        "maintenance_rate": "0.02",
        "leverage_max": "30",
        "deduction": "50"
      },
      {
        "tier": 3,
        "risk_limit": "50000",
        "initial_rate": "0.04545",
        "maintenance_rate": "0.03",
        "leverage_max": "22",
        "deduction": "350"
      },
      {
        "tier": 4,
        "risk_limit": "70000",
        "initial_rate": "0.05555",
        "maintenance_rate": "0.04",
        "leverage_max": "18",
        "deduction": "850"
      },
      {
        "tier": 5,
        "risk_limit": "100000",
        "initial_rate": "0.1",
        "maintenance_rate": "0.085",
        "leverage_max": "10",
        "deduction": "4000"
      },
      {
        "tier": 6,
        "risk_limit": "150000",
        "initial_rate": "0.333",
        "maintenance_rate": "0.3",
        "leverage_max": "3",
        "deduction": "25500"
      },
      {
        "tier": 7,
        "risk_limit": "200000",
        "initial_rate": "0.5",
        "maintenance_rate": "0.45",
        "leverage_max": "2",
        "deduction": "48000"
      },
      {
        "tier": 8,
        "risk_limit": "300000",
        "initial_rate": "1",
        "maintenance_rate": "0.95",
        "leverage_max": "1",
        "deduction": "148000"
      }
    ]
    

##  Level-based BBO Contract Order Placement🔒 Authenticated

POST`/futures/{settle}/bbo_orders`

POST `/futures/{settle}/bbo_orders`

_Level-based BBO Contract Order Placement_

Compared to the futures trading order placement interface (futures/{settle}/orders), it adds the `level` and `direction` parameters.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | FuturesBBOOrder | Required | none  
↳ contract | body | string | Required | Futures contract  
↳ size | body | integer(int64) | Required | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
↳ direction | body | string | Required | Direction: 'sell' fetches the bid side, 'buy' fetches the ask side.  
↳ iceberg | body | integer(int64) | Optional | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
↳ level | body | integer(int64) | Required | Level: maximum 20 levels  
↳ close | body | boolean | Optional | Set as `true` to close the position, with `size` set to 0  
↳ reduce_only | body | boolean | Optional | Set as `true` to be reduce-only order  
↳ tif | body | string | Optional | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
↳ text | body | string | Optional | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Content can only contain numbers, letters, underscores (_), hyphens (-), or dots (.)  
  
In addition to user custom information, the following are internal reserved fields identifying order sources:  
  
\- web: Web  
\- api: API Call  
\- app: Mobile App  
\- auto_deleveraging: Auto-Deleveraging  
\- liquidation: Forced Liquidation of Legacy Classic Mode Positions  
\- liq-xxx: a. Forced liquidation of New Classic Mode positions, including isolated margin, single-direction cross margin, and non-hedged dual-direction cross margin positions. b. Forced liquidation of isolated margin positions in Unified Account Single-Currency Margin Mode  
\- hedge-liq-xxx: Forced liquidation of hedged portions in New Classic Mode dual-direction cross margin (simultaneous closing of long and short positions)  
\- pm_liquidate: Forced liquidation in Unified Account Cross-Currency Margin Mode  
\- comb_margin_liquidate: Forced liquidation in Unified Account Portfolio Margin Mode  
\- scm_liquidate: Forced liquidation of positions in Unified Account Single-Currency Margin Mode  
\- insurance: Insurance  
↳ auto_size | body | string | Optional | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
↳ stp_act | body | string | Optional | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
↳ pid | body | integer(int64) | Optional | Position ID  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**» tif** : Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none

**» text** : Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Content can only contain numbers, letters, underscores (_), hyphens (-), or dots (.)  
  
In addition to user custom information, the following are internal reserved fields identifying order sources:  
  
\- web: Web  
\- api: API Call  
\- app: Mobile App  
\- auto_deleveraging: Auto-Deleveraging  
\- liquidation: Forced Liquidation of Legacy Classic Mode Positions  
\- liq-xxx: a. Forced liquidation of New Classic Mode positions, including isolated margin, single-direction cross margin, and non-hedged dual-direction cross margin positions. b. Forced liquidation of isolated margin positions in Unified Account Single-Currency Margin Mode  
\- hedge-liq-xxx: Forced liquidation of hedged portions in New Classic Mode dual-direction cross margin (simultaneous closing of long and short positions)  
\- pm_liquidate: Forced liquidation in Unified Account Cross-Currency Margin Mode  
\- comb_margin_liquidate: Forced liquidation in Unified Account Portfolio Margin Mode  
\- scm_liquidate: Forced liquidation of positions in Unified Account Single-Currency Margin Mode  
\- insurance: Insurance

**» stp_act** : Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» tif | gtc  
» tif | ioc  
» tif | poc  
» tif | fok  
» auto_size | close_long  
» auto_size | close_short  
» stp_act | co  
» stp_act | cn  
» stp_act | cb  
» stp_act | -  
settle | btc  
settle | usdt  
  
### Responses

  * 201[Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2)Order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order details | FuturesOrder  
  
### Response Schema

Status Code **201**

_Futures order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Futures order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
» update_time | number(double) | OrderUpdateTime  
» finish_time | number(double) | Order finished time. Not returned if order is open  
» finish_as | string | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
» status | string | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
» contract | string | Futures contract  
» size | string | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | string | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
» left | string | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
» tkfr | string | Taker fee  
» mkfr | string | Maker fee  
» refu | integer | Referrer user ID  
» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
» amend_text | string | The custom data that the user remarked when amending the order  
» market_order_slip_ratio | string | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
» pos_margin_mode | string | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
» action_mode | string | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
» tpsl_tp_trigger_price | string | Take profit price  
» tpsl_sl_trigger_price | string | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/futures/usdt/bbo_orders'
    query_param = ''
    body='{"contract":"PI_USDT","level":8,"direction":"sell","size":1}'
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
    url="/futures/usdt/bbo_orders"
    query_param=""
    body_param='{"contract":"PI_USDT","level":8,"direction":"sell","size":1}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "contract": "PI_USDT",
      "level": 8,
      "direction": "sell",
      "size": 1
    }
    

> Example responses

> 201 Response
    
    
    {
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
      "price": "3765",
      "fill_price": "0",
      "mkfr": "-0.00025",
      "tkfr": "0.00075",
      "tif": "gtc",
      "refu": 0,
      "is_reduce_only": false,
      "is_close": false,
      "is_liq": false,
      "text": "t-my-custom-id",
      "status": "finished",
      "finish_time": 1514764900,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  Create trail order🔒 Authenticated

POST`/futures/{settle}/autoorder/v1/trail/create`

POST `/futures/{settle}/autoorder/v1/trail/create`

_Create trail order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CreateTrailOrder | Required | none  
↳ contract | body | string | Required | Contract name  
↳ amount | body | string | Required | Trading quantity in contracts, positive for buy, negative for sell  
↳ activation_price | body | string | Optional | Activation price, 0 means trigger immediately  
↳ is_gte | body | boolean | Optional | true: activate when market price >= activation price, false: <= activation price  
↳ price_type | body | integer(int32) | Optional | Activation price type: 1-latest price, 2-index price, 3-mark price  
↳ price_offset | body | string | Optional | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
↳ reduce_only | body | boolean | Optional | Whether reduce only  
↳ position_related | body | boolean | Optional | Whether bound to a position (if position_related = true (position-related), then reduce_only must also be true)  
↳ text | body | string | Optional | Order custom information, optional field. Used to identify the order source or set a user-defined ID.  
  
If non-empty, it must meet one of the following rules:  
  
1\. Internal Reserved Fields (identifying order source):  
\- `apiv4`: API call  
2\. User-defined Fields (setting custom ID):  
\- Must start with `t-`  
\- The content after `t-` must not exceed 28 bytes in length  
\- Can only contain: numbers, letters, underscores (_), hyphens (-), or dots (.)  
\- Examples: `t-my-order-001`, `t-trail_2024.01`  
  
Note: User-defined fields must not conflict with internal reserved fields.  
↳ pos_margin_mode | body | string | Optional | Position margin mode: isolated/cross  
↳ position_mode | body | string | Optional | Position mode: single, dual, and dual_plus  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**» text** : Order custom information, optional field. Used to identify the order source or set a user-defined ID.  
  
If non-empty, it must meet one of the following rules:  
  
1\. Internal Reserved Fields (identifying order source):  
\- `apiv4`: API call  
2\. User-defined Fields (setting custom ID):  
\- Must start with `t-`  
\- The content after `t-` must not exceed 28 bytes in length  
\- Can only contain: numbers, letters, underscores (_), hyphens (-), or dots (.)  
\- Examples: `t-my-order-001`, `t-trail_2024.01`  
  
Note: User-defined fields must not conflict with internal reserved fields.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» price_type | 1  
» price_type | 2  
» price_type | 3  
settle | btc  
settle | usdt  
  
### Responses

  * 201[Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2)Created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Created successfully | CreateTrailOrderResponse  
  
### Response Schema

Status Code **201**

_CreateTrailOrderResponse_

Name | Type | Description  
---|---|---  
» code | integer(int32) | Status code, 0 means success  
» message | string | Response message  
» data | object | none  
»» id | string | Order ID  
» timestamp | integer(int64) | Response timestamp (milliseconds)  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/create'
    query_param = ''
    body='{"contract":"BTC_USDT","amount":"10","activation_price":"50000","is_gte":true,"price_type":1,"price_offset":"0.1%","reduce_only":false,"text":"apiv4"}'
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
    url="/futures/usdt/autoorder/v1/trail/create"
    query_param=""
    body_param='{"contract":"BTC_USDT","amount":"10","activation_price":"50000","is_gte":true,"price_type":1,"price_offset":"0.1%","reduce_only":false,"text":"apiv4"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "contract": "BTC_USDT",
      "amount": "10",
      "activation_price": "50000",
      "is_gte": true,
      "price_type": 1,
      "price_offset": "0.1%",
      "reduce_only": false,
      "text": "apiv4"
    }
    

> Example responses

> 201 Response
    
    
    {
      "code": 0,
      "message": "ok",
      "data": {
        "id": "63648"
      },
      "timestamp": 1769583885680
    }
    

##  Terminate trail order🔒 Authenticated

POST`/futures/{settle}/autoorder/v1/trail/stop`

POST `/futures/{settle}/autoorder/v1/trail/stop`

_Terminate trail order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | StopTrailOrder | Required | none  
↳ id | body | integer(int64) | Optional | Order ID, if ID is specified, text is not needed  
↳ text | body | string | Optional | Custom text, if ID is not specified, terminate based on user_id and text  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Termination successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Termination successful | Inline  
  
### Response Schema

Status Code **200**

_TrailOrderResponse_

Name | Type | Description  
---|---|---  
» order | object | Trail order details  
»» id | integer(int64) | Order ID  
»» user_id | integer(int64) | User ID  
»» user | integer(int64) | User ID  
»» contract | string | Contract name  
»» settle | string | Settle currency  
»» amount | string | Trading quantity in contracts, positive for buy, negative for sell  
»» is_gte | boolean | true: activate when market price >= activation price, false: <= activation price  
»» activation_price | string | Activation price, 0 means trigger immediately  
»» price_type | integer(int32) | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price  
»» price_offset | string | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
»» text | string | Custom field  
»» reduce_only | boolean | Reduce Position Only  
»» position_related | boolean | Whether bound to position  
»» created_at | integer(int64) | Created time  
»» activated_at | integer(int64) | Activation time  
»» finished_at | integer(int64) | End time  
»» create_time | integer(int64) | Created time  
»» active_time | integer(int64) | Activation time  
»» finish_time | integer(int64) | End time  
»» reason | string | End reason  
»» suborder_text | string | Sub-order text field  
»» is_dual_mode | boolean | Whether dual position mode when creating order  
»» trigger_price | string | Trigger price  
»» suborder_id | integer(int64) | Sub-order ID  
»» side_label | string | Order direction label: long/short/open long/open short/close long/close short  
»» original_status | integer(int32) | Order status  
»» status | string | Simplified order status: open/finished  
»» position_side_output | string | Same as side_label, client requires consistency with other order types  
»» updated_at | integer(int64) | Update time  
»» extremum_price | string | Extremum price  
»» status_code | string | Status code value  
»» created_at_precise | string | Creation time (high precision, seconds.microseconds format)  
»» finished_at_precise | string | End time (high precision, seconds.microseconds format)  
»» activated_at_precise | string | Activation time (high precision, seconds.microseconds format)  
»» status_label | string | Status internationalization label (translated status text)  
»» pos_margin_mode | string | Position margin mode: isolated/cross  
»» position_mode | string | Position mode: single, dual, and dual_plus  
»» error_label | string | Error label  
»» leverage | string | leverage  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
status | open  
status | finished  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/stop'
    query_param = ''
    body='{"id":123456789}'
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
    url="/futures/usdt/autoorder/v1/trail/stop"
    query_param=""
    body_param='{"id":123456789}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "id": 123456789
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": "63585",
      "user_id": "2124438083",
      "contract": "BTC_USDT",
      "settle": "usdt",
      "amount": "10",
      "is_gte": false,
      "activation_price": "0",
      "price_type": 1,
      "price_offset": "5%",
      "text": "apiv4",
      "reduce_only": false,
      "position_related": false,
      "created_at": "1769569837",
      "activated_at": "1769569837",
      "finished_at": "1769578529",
      "reason": "",
      "suborder_text": "apiv4-auto-trail-o-1d29",
      "is_dual_mode": false,
      "trigger_price": "91047.4",
      "suborder_id": "94294117233225616",
      "side_label": "买入",
      "original_status": 4,
      "status": "finished",
      "user": "2124438083",
      "create_time": "1769569837",
      "active_time": "1769569837",
      "finish_time": "1769578529",
      "position_side_output": "买入",
      "updated_at": "1769578529",
      "extremum_price": "86711.9",
      "status_code": "success",
      "created_at_precise": "1769569837778000",
      "finished_at_precise": "1769578529853294",
      "activated_at_precise": "1769569837976010",
      "status_label": "已完成",
      "pos_margin_mode": "",
      "position_mode": "single",
      "error_label": "",
      "leverage": ""
    }
    

##  Batch terminate trail orders🔒 Authenticated

POST`/futures/{settle}/autoorder/v1/trail/stop_all`

POST `/futures/{settle}/autoorder/v1/trail/stop_all`

_Batch terminate trail orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | StopAllTrailOrders | Required | none  
↳ contract | body | string | Optional | Contract name  
↳ related_position | body | integer(int32) | Optional | Associated position, if provided, only cancel orders associated with this position, 1-long, 2-short  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» related_position | 1  
» related_position | 2  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Termination successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Termination successful | Inline  
  
### Response Schema

Status Code **200**

_TrailOrderListResponse_

Name | Type | Description  
---|---|---  
» orders | array | none  
»» TrailOrder | object | Trail order details  
»»» id | integer(int64) | Order ID  
»»» user_id | integer(int64) | User ID  
»»» user | integer(int64) | User ID  
»»» contract | string | Contract name  
»»» settle | string | Settle currency  
»»» amount | string | Trading quantity in contracts, positive for buy, negative for sell  
»»» is_gte | boolean | true: activate when market price >= activation price, false: <= activation price  
»»» activation_price | string | Activation price, 0 means trigger immediately  
»»» price_type | integer(int32) | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price  
»»» price_offset | string | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
»»» text | string | Custom field  
»»» reduce_only | boolean | Reduce Position Only  
»»» position_related | boolean | Whether bound to position  
»»» created_at | integer(int64) | Created time  
»»» activated_at | integer(int64) | Activation time  
»»» finished_at | integer(int64) | End time  
»»» create_time | integer(int64) | Created time  
»»» active_time | integer(int64) | Activation time  
»»» finish_time | integer(int64) | End time  
»»» reason | string | End reason  
»»» suborder_text | string | Sub-order text field  
»»» is_dual_mode | boolean | Whether dual position mode when creating order  
»»» trigger_price | string | Trigger price  
»»» suborder_id | integer(int64) | Sub-order ID  
»»» side_label | string | Order direction label: long/short/open long/open short/close long/close short  
»»» original_status | integer(int32) | Order status  
»»» status | string | Simplified order status: open/finished  
»»» position_side_output | string | Same as side_label, client requires consistency with other order types  
»»» updated_at | integer(int64) | Update time  
»»» extremum_price | string | Extremum price  
»»» status_code | string | Status code value  
»»» created_at_precise | string | Creation time (high precision, seconds.microseconds format)  
»»» finished_at_precise | string | End time (high precision, seconds.microseconds format)  
»»» activated_at_precise | string | Activation time (high precision, seconds.microseconds format)  
»»» status_label | string | Status internationalization label (translated status text)  
»»» pos_margin_mode | string | Position margin mode: isolated/cross  
»»» position_mode | string | Position mode: single, dual, and dual_plus  
»»» error_label | string | Error label  
»»» leverage | string | leverage  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
status | open  
status | finished  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/stop_all'
    query_param = ''
    body='{"contract":"BTC_USDT"}'
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
    url="/futures/usdt/autoorder/v1/trail/stop_all"
    query_param=""
    body_param='{"contract":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "contract": "BTC_USDT"
    }
    

> Example responses

> 200 Response
    
    
    {
      "orders": [
        {
          "id": "123456789",
          "user_id": "100000",
          "user": "100000",
          "contract": "BTC_USDT",
          "settle": "usdt",
          "amount": "10",
          "is_gte": true,
          "activation_price": "50000",
          "price_type": 1,
          "price_offset": "0.1%",
          "text": "t-my-trail-order-1",
          "reduce_only": false,
          "position_related": false,
          "created_at": "1546569968",
          "create_time": "1546569968",
          "activated_at": "1546570000",
          "active_time": "1546570000",
          "finished_at": "0",
          "finish_time": "0",
          "reason": "",
          "suborder_text": "",
          "is_dual_mode": false,
          "trigger_price": "50000",
          "suborder_id": "0",
          "side_label": "开多",
          "position_side_output": "开多",
          "original_status": 1,
          "status": "open",
          "updated_at": "1546569968",
          "extremum_price": "50100",
          "status_code": "pending",
          "created_at_precise": "1546569968.123456",
          "finished_at_precise": "",
          "activated_at_precise": "",
          "status_label": "待激活",
          "pos_margin_mode": "isolated",
          "position_mode": "single",
          "error_label": "",
          "leverage": "10"
        },
        {
          "id": "123456790",
          "user_id": "100000",
          "user": "100000",
          "contract": "ETH_USDT",
          "settle": "usdt",
          "amount": "-5",
          "is_gte": false,
          "activation_price": "3000",
          "price_type": 2,
          "price_offset": "0.2%",
          "text": "t-my-trail-order-2",
          "reduce_only": true,
          "position_related": true,
          "created_at": "1546569970",
          "create_time": "1546569970",
          "activated_at": "1546570100",
          "active_time": "1546570100",
          "finished_at": "1546571000",
          "finish_time": "1546571000",
          "reason": "success",
          "suborder_text": "t-suborder-1",
          "is_dual_mode": true,
          "trigger_price": "3000",
          "suborder_id": "987654321",
          "side_label": "平空",
          "position_side_output": "平空",
          "original_status": 4,
          "status": "finished",
          "updated_at": "1546571000",
          "extremum_price": "2990",
          "status_code": "success",
          "created_at_precise": "1546569970.654321",
          "finished_at_precise": "1546571000.123456",
          "activated_at_precise": "1546570100.789012",
          "status_label": "完成全部委托量",
          "pos_margin_mode": "cross",
          "position_mode": "dual",
          "error_label": "",
          "leverage": "20"
        }
      ]
    }
    

##  Get trail order list🔒 Authenticated

GET`/futures/{settle}/autoorder/v1/trail/list`

GET `/futures/{settle}/autoorder/v1/trail/list`

Get `trail order list`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Contract name  
is_finished | query | boolean | Optional | Whether historical order  
start_at | query | integer(int64) | Optional | Start time of time range  
end_at | query | integer(int64) | Optional | End time of time range  
page_num | query | integer(int32) | Optional | Page number, starting from 1  
page_size | query | integer(int32) | Optional | Number of items per page  
sort_by | query | integer(int32) | Optional | Common sort field, 1-creation time, 2-end time  
hide_cancel | query | boolean | Optional | Hide cancelled orders  
related_position | query | integer(int32) | Optional | Associated position, if provided, only return orders associated with this position, 1-long, 2-short  
sort_by_trigger | query | boolean | Optional | Sort by trigger price and activation price, easy to trigger or activate first, only for current orders associated with positions  
reduce_only | query | integer(int32) | Optional | Whether reduce only, 1-yes, 2-no  
side | query | integer(int32) | Optional | Direction, 1-long position, 2-short position  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
sort_by | 1  
sort_by | 2  
related_position | 1  
related_position | 2  
reduce_only | 1  
reduce_only | 2  
side | 1  
side | 2  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Inline  
  
### Response Schema

Status Code **200**

_TrailOrderListResponse_

Name | Type | Description  
---|---|---  
» orders | array | none  
»» TrailOrder | object | Trail order details  
»»» id | integer(int64) | Order ID  
»»» user_id | integer(int64) | User ID  
»»» user | integer(int64) | User ID  
»»» contract | string | Contract name  
»»» settle | string | Settle currency  
»»» amount | string | Trading quantity in contracts, positive for buy, negative for sell  
»»» is_gte | boolean | true: activate when market price >= activation price, false: <= activation price  
»»» activation_price | string | Activation price, 0 means trigger immediately  
»»» price_type | integer(int32) | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price  
»»» price_offset | string | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
»»» text | string | Custom field  
»»» reduce_only | boolean | Reduce Position Only  
»»» position_related | boolean | Whether bound to position  
»»» created_at | integer(int64) | Created time  
»»» activated_at | integer(int64) | Activation time  
»»» finished_at | integer(int64) | End time  
»»» create_time | integer(int64) | Created time  
»»» active_time | integer(int64) | Activation time  
»»» finish_time | integer(int64) | End time  
»»» reason | string | End reason  
»»» suborder_text | string | Sub-order text field  
»»» is_dual_mode | boolean | Whether dual position mode when creating order  
»»» trigger_price | string | Trigger price  
»»» suborder_id | integer(int64) | Sub-order ID  
»»» side_label | string | Order direction label: long/short/open long/open short/close long/close short  
»»» original_status | integer(int32) | Order status  
»»» status | string | Simplified order status: open/finished  
»»» position_side_output | string | Same as side_label, client requires consistency with other order types  
»»» updated_at | integer(int64) | Update time  
»»» extremum_price | string | Extremum price  
»»» status_code | string | Status code value  
»»» created_at_precise | string | Creation time (high precision, seconds.microseconds format)  
»»» finished_at_precise | string | End time (high precision, seconds.microseconds format)  
»»» activated_at_precise | string | Activation time (high precision, seconds.microseconds format)  
»»» status_label | string | Status internationalization label (translated status text)  
»»» pos_margin_mode | string | Position margin mode: isolated/cross  
»»» position_mode | string | Position mode: single, dual, and dual_plus  
»»» error_label | string | Error label  
»»» leverage | string | leverage  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
status | open  
status | finished  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/list'
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
    url="/futures/usdt/autoorder/v1/trail/list"
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
      "orders": [
        {
          "id": "123456789",
          "user_id": "100000",
          "user": "100000",
          "contract": "BTC_USDT",
          "settle": "usdt",
          "amount": "10",
          "is_gte": true,
          "activation_price": "50000",
          "price_type": 1,
          "price_offset": "0.1%",
          "text": "t-my-trail-order-1",
          "reduce_only": false,
          "position_related": false,
          "created_at": "1546569968",
          "create_time": "1546569968",
          "activated_at": "1546570000",
          "active_time": "1546570000",
          "finished_at": "0",
          "finish_time": "0",
          "reason": "",
          "suborder_text": "",
          "is_dual_mode": false,
          "trigger_price": "50000",
          "suborder_id": "0",
          "side_label": "开多",
          "position_side_output": "开多",
          "original_status": 1,
          "status": "open",
          "updated_at": "1546569968",
          "extremum_price": "50100",
          "status_code": "pending",
          "created_at_precise": "1546569968.123456",
          "finished_at_precise": "",
          "activated_at_precise": "",
          "status_label": "待激活",
          "pos_margin_mode": "isolated",
          "position_mode": "single",
          "error_label": "",
          "leverage": "10"
        },
        {
          "id": "123456790",
          "user_id": "100000",
          "user": "100000",
          "contract": "ETH_USDT",
          "settle": "usdt",
          "amount": "-5",
          "is_gte": false,
          "activation_price": "3000",
          "price_type": 2,
          "price_offset": "0.2%",
          "text": "t-my-trail-order-2",
          "reduce_only": true,
          "position_related": true,
          "created_at": "1546569970",
          "create_time": "1546569970",
          "activated_at": "1546570100",
          "active_time": "1546570100",
          "finished_at": "1546571000",
          "finish_time": "1546571000",
          "reason": "success",
          "suborder_text": "t-suborder-1",
          "is_dual_mode": true,
          "trigger_price": "3000",
          "suborder_id": "987654321",
          "side_label": "平空",
          "position_side_output": "平空",
          "original_status": 4,
          "status": "finished",
          "updated_at": "1546571000",
          "extremum_price": "2990",
          "status_code": "success",
          "created_at_precise": "1546569970.654321",
          "finished_at_precise": "1546571000.123456",
          "activated_at_precise": "1546570100.789012",
          "status_label": "完成全部委托量",
          "pos_margin_mode": "cross",
          "position_mode": "dual",
          "error_label": "",
          "leverage": "20"
        }
      ]
    }
    

##  Get trail order details🔒 Authenticated

GET`/futures/{settle}/autoorder/v1/trail/detail`

GET `/futures/{settle}/autoorder/v1/trail/detail`

Get `trail order details`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
id | query | integer(int64) | Required | Order ID  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | TrailOrderDetailResponse  
  
### Response Schema

Status Code **200**

_TrailOrderDetailResponse_

Name | Type | Description  
---|---|---  
» code | integer(int32) | Status code, 0 means success  
» message | string | Response message  
» data | object | none  
»» order | object | Trail order details  
»»» id | integer(int64) | Order ID  
»»» user_id | integer(int64) | User ID  
»»» user | integer(int64) | User ID  
»»» contract | string | Contract name  
»»» settle | string | Settle currency  
»»» amount | string | Trading quantity in contracts, positive for buy, negative for sell  
»»» is_gte | boolean | true: activate when market price >= activation price, false: <= activation price  
»»» activation_price | string | Activation price, 0 means trigger immediately  
»»» price_type | integer(int32) | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price  
»»» price_offset | string | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
»»» text | string | Custom field  
»»» reduce_only | boolean | Reduce Position Only  
»»» position_related | boolean | Whether bound to position  
»»» created_at | integer(int64) | Created time  
»»» activated_at | integer(int64) | Activation time  
»»» finished_at | integer(int64) | End time  
»»» create_time | integer(int64) | Created time  
»»» active_time | integer(int64) | Activation time  
»»» finish_time | integer(int64) | End time  
»»» reason | string | End reason  
»»» suborder_text | string | Sub-order text field  
»»» is_dual_mode | boolean | Whether dual position mode when creating order  
»»» trigger_price | string | Trigger price  
»»» suborder_id | integer(int64) | Sub-order ID  
»»» side_label | string | Order direction label: long/short/open long/open short/close long/close short  
»»» original_status | integer(int32) | Order status  
»»» status | string | Simplified order status: open/finished  
»»» position_side_output | string | Same as side_label, client requires consistency with other order types  
»»» updated_at | integer(int64) | Update time  
»»» extremum_price | string | Extremum price  
»»» status_code | string | Status code value  
»»» created_at_precise | string | Creation time (high precision, seconds.microseconds format)  
»»» finished_at_precise | string | End time (high precision, seconds.microseconds format)  
»»» activated_at_precise | string | Activation time (high precision, seconds.microseconds format)  
»»» status_label | string | Status internationalization label (translated status text)  
»»» pos_margin_mode | string | Position margin mode: isolated/cross  
»»» position_mode | string | Position mode: single, dual, and dual_plus  
»»» error_label | string | Error label  
»»» leverage | string | leverage  
»» timestamp | integer(int64) | Response timestamp (milliseconds)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
status | open  
status | finished  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/detail'
    query_param = 'id=0'
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
    url="/futures/usdt/autoorder/v1/trail/detail"
    query_param="id=0"
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
      "code": 0,
      "message": "ok",
      "data": {
        "order": {
          "id": "63585",
          "user_id": "2124438083",
          "contract": "BTC_USDT",
          "settle": "usdt",
          "amount": "10",
          "is_gte": false,
          "activation_price": "0",
          "price_type": 1,
          "price_offset": "5%",
          "text": "apiv4",
          "reduce_only": false,
          "position_related": false,
          "created_at": "1769569837",
          "activated_at": "1769569837",
          "finished_at": "1769578529",
          "reason": "",
          "suborder_text": "apiv4-auto-trail-o-1d29",
          "is_dual_mode": false,
          "trigger_price": "91047.4",
          "suborder_id": "94294117233225616",
          "side_label": "买入",
          "original_status": 4,
          "status": "finished",
          "user": "2124438083",
          "create_time": "1769569837",
          "active_time": "1769569837",
          "finish_time": "1769578529",
          "position_side_output": "买入",
          "updated_at": "1769578529",
          "extremum_price": "86711.9",
          "status_code": "success",
          "created_at_precise": "1769569837778000",
          "finished_at_precise": "1769578529853294",
          "activated_at_precise": "1769569837976010",
          "status_label": "已完成",
          "pos_margin_mode": "",
          "position_mode": "single",
          "error_label": "",
          "leverage": ""
        }
      },
      "timestamp": 1769584936814
    }
    

##  Update trail order🔒 Authenticated

POST`/futures/{settle}/autoorder/v1/trail/update`

POST `/futures/{settle}/autoorder/v1/trail/update`

_Update trail order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | UpdateTrailOrder | Required | none  
↳ id | body | integer(int64) | Required | Order ID  
↳ amount | body | string | Optional | Total trading quantity in contracts, positive for buy, negative for sell, 0 means no modification  
↳ activation_price | body | string | Optional | Activation price, 0 means trigger immediately, empty means no modification  
↳ is_gte_str | body | string | Optional | true: activate when market price >= activation price, false: <= activation price, empty means no modification  
↳ price_type | body | integer(int32) | Optional | Activation price type, not provided or 0 means no modification, 1-latest price, 2-index price, 3-mark price  
↳ price_offset | body | string | Optional | Callback ratio or price distance, e.g., `0.1` or `0.1%`; empty means no modification  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» price_type | 0  
» price_type | 1  
» price_type | 2  
» price_type | 3  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Updated successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Updated successfully | Inline  
  
### Response Schema

Status Code **200**

_TrailOrderResponse_

Name | Type | Description  
---|---|---  
» order | object | Trail order details  
»» id | integer(int64) | Order ID  
»» user_id | integer(int64) | User ID  
»» user | integer(int64) | User ID  
»» contract | string | Contract name  
»» settle | string | Settle currency  
»» amount | string | Trading quantity in contracts, positive for buy, negative for sell  
»» is_gte | boolean | true: activate when market price >= activation price, false: <= activation price  
»» activation_price | string | Activation price, 0 means trigger immediately  
»» price_type | integer(int32) | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price  
»» price_offset | string | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
»» text | string | Custom field  
»» reduce_only | boolean | Reduce Position Only  
»» position_related | boolean | Whether bound to position  
»» created_at | integer(int64) | Created time  
»» activated_at | integer(int64) | Activation time  
»» finished_at | integer(int64) | End time  
»» create_time | integer(int64) | Created time  
»» active_time | integer(int64) | Activation time  
»» finish_time | integer(int64) | End time  
»» reason | string | End reason  
»» suborder_text | string | Sub-order text field  
»» is_dual_mode | boolean | Whether dual position mode when creating order  
»» trigger_price | string | Trigger price  
»» suborder_id | integer(int64) | Sub-order ID  
»» side_label | string | Order direction label: long/short/open long/open short/close long/close short  
»» original_status | integer(int32) | Order status  
»» status | string | Simplified order status: open/finished  
»» position_side_output | string | Same as side_label, client requires consistency with other order types  
»» updated_at | integer(int64) | Update time  
»» extremum_price | string | Extremum price  
»» status_code | string | Status code value  
»» created_at_precise | string | Creation time (high precision, seconds.microseconds format)  
»» finished_at_precise | string | End time (high precision, seconds.microseconds format)  
»» activated_at_precise | string | Activation time (high precision, seconds.microseconds format)  
»» status_label | string | Status internationalization label (translated status text)  
»» pos_margin_mode | string | Position margin mode: isolated/cross  
»» position_mode | string | Position mode: single, dual, and dual_plus  
»» error_label | string | Error label  
»» leverage | string | leverage  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
status | open  
status | finished  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/update'
    query_param = ''
    body='{"id":123456789,"amount":"20","activation_price":"51000","price_offset":"0.2%"}'
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
    url="/futures/usdt/autoorder/v1/trail/update"
    query_param=""
    body_param='{"id":123456789,"amount":"20","activation_price":"51000","price_offset":"0.2%"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "id": 123456789,
      "amount": "20",
      "activation_price": "51000",
      "price_offset": "0.2%"
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": "63585",
      "user_id": "2124438083",
      "contract": "BTC_USDT",
      "settle": "usdt",
      "amount": "10",
      "is_gte": false,
      "activation_price": "0",
      "price_type": 1,
      "price_offset": "5%",
      "text": "apiv4",
      "reduce_only": false,
      "position_related": false,
      "created_at": "1769569837",
      "activated_at": "1769569837",
      "finished_at": "1769578529",
      "reason": "",
      "suborder_text": "apiv4-auto-trail-o-1d29",
      "is_dual_mode": false,
      "trigger_price": "91047.4",
      "suborder_id": "94294117233225616",
      "side_label": "买入",
      "original_status": 4,
      "status": "finished",
      "user": "2124438083",
      "create_time": "1769569837",
      "active_time": "1769569837",
      "finish_time": "1769578529",
      "position_side_output": "买入",
      "updated_at": "1769578529",
      "extremum_price": "86711.9",
      "status_code": "success",
      "created_at_precise": "1769569837778000",
      "finished_at_precise": "1769578529853294",
      "activated_at_precise": "1769569837976010",
      "status_label": "已完成",
      "pos_margin_mode": "",
      "position_mode": "single",
      "error_label": "",
      "leverage": ""
    }
    

##  Get trail order user modification records🔒 Authenticated

GET`/futures/{settle}/autoorder/v1/trail/change_log`

GET `/futures/{settle}/autoorder/v1/trail/change_log`

Get `trail order user modification records`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
id | query | integer(int64) | Required | Order ID  
page_num | query | integer(int32) | Optional | Page number, starting from 1  
page_size | query | integer(int32) | Optional | Number of items per page  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | TrailOrderChangeLogResponse  
  
### Response Schema

Status Code **200**

_TrailOrderChangeLogResponse_

Name | Type | Description  
---|---|---  
» change_log | array | [Trail order modification records]  
»» _None_ | TrailChangeLog | Trail order modification records  
»»» updated_at | integer(int64) | Update time  
»»» amount | string | Trading quantity in contracts, positive for buy, negative for sell  
»»» is_gte | boolean | true: activate when market price >= activation price, false: <= activation price  
»»» activation_price | string | Activation price, 0 means trigger immediately  
»»» price_type | integer(int32) | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price  
»»» price_offset | string | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
»»» is_create | boolean | true - order creation, false - order modification  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/change_log'
    query_param = 'id=0'
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
    url="/futures/usdt/autoorder/v1/trail/change_log"
    query_param="id=0"
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
      "change_log": [
        {
          "updated_at": 1546569968,
          "amount": "10",
          "is_gte": true,
          "activation_price": "50000",
          "price_type": 1,
          "price_offset": "0.1%",
          "is_create": true
        },
        {
          "updated_at": 1546570000,
          "amount": "20",
          "is_gte": true,
          "activation_price": "51000",
          "price_type": 1,
          "price_offset": "0.2%",
          "is_create": false
        },
        {
          "updated_at": 1546570100,
          "amount": "20",
          "is_gte": true,
          "activation_price": "51000",
          "price_type": 2,
          "price_offset": "0.2%",
          "is_create": false
        }
      ]
    }
    

##  Create a chase order🔒 Authenticated

POST`/futures/{settle}/autoorder/v1/chase/create`

POST `/futures/{settle}/autoorder/v1/chase/create`

_Create a chase order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
body | body | CreateChaseOrderReq | Required | none  
↳ contract | body | string | Required | Contract name; server-side converted to uppercase  
↳ settle | body | string | Optional | Settle currency, overridden by the path parameter and converted to lowercase  
↳ amount | body | string | Required | Total order size in contracts, decimal string. Positive for buy, negative for sell. Cannot be 0  
↳ price_limit | body | string | Required | Maximum chase price as a valid decimal string. Pass "0" when no price limit is set  
↳ offset_limit | body | string | Optional | Maximum chasing distance from the best price, mutually exclusive with price_limit  
↳ reduce_only | body | boolean | Optional | Whether reduce only  
↳ text | body | string | Optional | Optional custom tag  
↳ is_dual_mode | body | boolean | Optional | Whether dual-position mode is enabled  
↳ price_type | body | integer(int64) | Optional | Price type: 1 best bid/ask, 2 distance from best bid/ask  
↳ price_gap_type | body | integer(int64) | Optional | Used when price_type == 2: 1 absolute price gap, 2 percentage  
↳ price_gap_value | body | string | Optional | Price gap value paired with price_gap_type  
↳ pos_margin_mode | body | string | Optional | Position margin mode, e.g. isolated or cross  
↳ position_mode | body | string | Optional | Position mode (e.g. single, dual, dual_plus)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | CreateChaseOrderResp  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» id | string | ID of the newly created order  
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/create'
    query_param = ''
    body='{"contract":"string","settle":"string","amount":"string","price_limit":"string","offset_limit":"string","reduce_only":true,"text":"string","is_dual_mode":true,"price_type":0,"price_gap_type":0,"price_gap_value":"string","pos_margin_mode":"string","position_mode":"string"}'
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
    url="/futures/usdt/autoorder/v1/chase/create"
    query_param=""
    body_param='{"contract":"string","settle":"string","amount":"string","price_limit":"string","offset_limit":"string","reduce_only":true,"text":"string","is_dual_mode":true,"price_type":0,"price_gap_type":0,"price_gap_value":"string","pos_margin_mode":"string","position_mode":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "contract": "string",
      "settle": "string",
      "amount": "string",
      "price_limit": "string",
      "offset_limit": "string",
      "reduce_only": true,
      "text": "string",
      "is_dual_mode": true,
      "price_type": 0,
      "price_gap_type": 0,
      "price_gap_value": "string",
      "pos_margin_mode": "string",
      "position_mode": "string"
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": "string"
    }
    

##  Stop a chase order🔒 Authenticated

POST`/futures/{settle}/autoorder/v1/chase/stop`

POST `/futures/{settle}/autoorder/v1/chase/stop`

_Stop a chase order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
body | body | StopChaseOrderReq | Required | none  
↳ id | body | string | Optional | Order ID. Either id or text must be provided  
↳ text | body | string | Optional | Custom text. Required only when id is 0 or omitted  
↳ settle | body | string | Optional | Overridden by the path parameter  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | StopChaseOrderResp  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» order | ChaseOrder | Chase order detail or list item  
»» id | string | none  
»» user | string | none  
»» contract | string | none  
»» settle | string | none  
»» amount | string | Total size in contracts; positive for buy, negative for sell  
»» price_limit | string | none  
»» reduce_only | boolean | none  
»» text | string | none  
»» create_time | integer(int64) | none  
»» finish_time | integer(int64) | none  
»» original_status | integer | Raw status enum  
»» status | string | Simplified status, e.g. open / finished  
»» reason | string | none  
»» fill_amount | string | none  
»» average_fill_price | string | none  
»» suborder_id | string | none  
»» is_dual_mode | boolean | none  
»» side_label | string | none  
»» position_side_output | string | none  
»» chase_price | string | none  
»» interval_sec | integer(uint32) | none  
»» updated_at | integer(int64) | none  
»» suborder_price | string | none  
»» suborder_ongoing | boolean | none  
»» suborder_finish_as | string | none  
»» price_type | integer | PriceType enum: 1 latest, 2 index, 3 mark  
»» price_gap_type | string | none  
»» price_gap_value | string | none  
»» status_code | string | none  
»» create_time_precise | string | Creation time (seconds.microseconds)  
»» finish_time_precise | string | none  
»» pos_margin_mode | string | none  
»» position_mode | string | none  
»» leverage | string | none  
»» error_label | string | none  
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/stop'
    query_param = ''
    body='{"id":"string","text":"string","settle":"string"}'
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
    url="/futures/usdt/autoorder/v1/chase/stop"
    query_param=""
    body_param='{"id":"string","text":"string","settle":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "id": "string",
      "text": "string",
      "settle": "string"
    }
    

> Example responses

> 200 Response
    
    
    {
      "order": {
        "id": "string",
        "user": "string",
        "contract": "string",
        "settle": "string",
        "amount": "string",
        "price_limit": "string",
        "reduce_only": true,
        "text": "string",
        "create_time": 0,
        "finish_time": 0,
        "original_status": 0,
        "status": "string",
        "reason": "string",
        "fill_amount": "string",
        "average_fill_price": "string",
        "suborder_id": "string",
        "is_dual_mode": true,
        "side_label": "string",
        "position_side_output": "string",
        "chase_price": "string",
        "interval_sec": 0,
        "updated_at": 0,
        "suborder_price": "string",
        "suborder_ongoing": true,
        "suborder_finish_as": "string",
        "price_type": 0,
        "price_gap_type": "string",
        "price_gap_value": "string",
        "status_code": "string",
        "create_time_precise": "string",
        "finish_time_precise": "string",
        "pos_margin_mode": "string",
        "position_mode": "string",
        "leverage": "string",
        "error_label": "string"
      }
    }
    

##  Stop chase orders in batch🔒 Authenticated

POST`/futures/{settle}/autoorder/v1/chase/stop_all`

POST `/futures/{settle}/autoorder/v1/chase/stop_all`

_Stop chase orders in batch_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
body | body | StopAllChaseOrdersReq | Required | none  
↳ contract | body | string | Optional | Optional contract name  
↳ settle | body | string | Optional | Overridden by the path parameter  
↳ pos_margin_mode | body | string | Optional | Optional margin mode  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | StopAllChaseOrdersResp  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» orders | array | [Chase order detail or list item]  
»» _None_ | ChaseOrder | Chase order detail or list item  
»»» id | string | none  
»»» user | string | none  
»»» contract | string | none  
»»» settle | string | none  
»»» amount | string | Total size in contracts; positive for buy, negative for sell  
»»» price_limit | string | none  
»»» reduce_only | boolean | none  
»»» text | string | none  
»»» create_time | integer(int64) | none  
»»» finish_time | integer(int64) | none  
»»» original_status | integer | Raw status enum  
»»» status | string | Simplified status, e.g. open / finished  
»»» reason | string | none  
»»» fill_amount | string | none  
»»» average_fill_price | string | none  
»»» suborder_id | string | none  
»»» is_dual_mode | boolean | none  
»»» side_label | string | none  
»»» position_side_output | string | none  
»»» chase_price | string | none  
»»» interval_sec | integer(uint32) | none  
»»» updated_at | integer(int64) | none  
»»» suborder_price | string | none  
»»» suborder_ongoing | boolean | none  
»»» suborder_finish_as | string | none  
»»» price_type | integer | PriceType enum: 1 latest, 2 index, 3 mark  
»»» price_gap_type | string | none  
»»» price_gap_value | string | none  
»»» status_code | string | none  
»»» create_time_precise | string | Creation time (seconds.microseconds)  
»»» finish_time_precise | string | none  
»»» pos_margin_mode | string | none  
»»» position_mode | string | none  
»»» leverage | string | none  
»»» error_label | string | none  
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/stop_all'
    query_param = ''
    body='{"contract":"string","settle":"string","pos_margin_mode":"string"}'
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
    url="/futures/usdt/autoorder/v1/chase/stop_all"
    query_param=""
    body_param='{"contract":"string","settle":"string","pos_margin_mode":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "contract": "string",
      "settle": "string",
      "pos_margin_mode": "string"
    }
    

> Example responses

> 200 Response
    
    
    {
      "orders": [
        {
          "id": "string",
          "user": "string",
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "price_limit": "string",
          "reduce_only": true,
          "text": "string",
          "create_time": 0,
          "finish_time": 0,
          "original_status": 0,
          "status": "string",
          "reason": "string",
          "fill_amount": "string",
          "average_fill_price": "string",
          "suborder_id": "string",
          "is_dual_mode": true,
          "side_label": "string",
          "position_side_output": "string",
          "chase_price": "string",
          "interval_sec": 0,
          "updated_at": 0,
          "suborder_price": "string",
          "suborder_ongoing": true,
          "suborder_finish_as": "string",
          "price_type": 0,
          "price_gap_type": "string",
          "price_gap_value": "string",
          "status_code": "string",
          "create_time_precise": "string",
          "finish_time_precise": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "leverage": "string",
          "error_label": "string"
        }
      ]
    }
    

##  List chase orders🔒 Authenticated

GET`/futures/{settle}/autoorder/v1/chase/list`

GET `/futures/{settle}/autoorder/v1/chase/list`

_List chase orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Optional. When non-empty, must be a valid contract (validated against the market cache for the path settle); server-side converted to uppercase  
is_finished | query | boolean | Optional | true to query finished orders, false to query in-progress orders  
start_at | query | integer(int64) | Optional | Lower time bound for the history list, paired with end_at. Required when is_finished is true  
end_at | query | integer(int64) | Optional | Upper time bound for the history list, paired with start_at. Required when is_finished is true  
page_num | query | integer(uint32) | Optional | Page number, starting from 1  
page_size | query | integer(uint32) | Optional | Page size; must be between 1 and 100  
sort_by | query | integer | Required | Sort field: 1 ORDER_SORT_CREATED_AT, 2 ORDER_SORT_FINISHED_AT; cannot be 0  
hide_cancel | query | boolean | Optional | When true, cancelled orders are hidden in the list  
reduce_only | query | integer | Optional | OptionalBool: 0 unknown, 1 true, 2 false; used to filter by reduce-only flag  
side | query | integer | Optional | Filter by long/short side: 1 long, 2 short  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
sort_by | 1  
sort_by | 2  
reduce_only | 0  
reduce_only | 1  
reduce_only | 2  
side | 0  
side | 1  
side | 2  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | GetChaseOrdersResp  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» orders | array | [Chase order detail or list item]  
»» _None_ | ChaseOrder | Chase order detail or list item  
»»» id | string | none  
»»» user | string | none  
»»» contract | string | none  
»»» settle | string | none  
»»» amount | string | Total size in contracts; positive for buy, negative for sell  
»»» price_limit | string | none  
»»» reduce_only | boolean | none  
»»» text | string | none  
»»» create_time | integer(int64) | none  
»»» finish_time | integer(int64) | none  
»»» original_status | integer | Raw status enum  
»»» status | string | Simplified status, e.g. open / finished  
»»» reason | string | none  
»»» fill_amount | string | none  
»»» average_fill_price | string | none  
»»» suborder_id | string | none  
»»» is_dual_mode | boolean | none  
»»» side_label | string | none  
»»» position_side_output | string | none  
»»» chase_price | string | none  
»»» interval_sec | integer(uint32) | none  
»»» updated_at | integer(int64) | none  
»»» suborder_price | string | none  
»»» suborder_ongoing | boolean | none  
»»» suborder_finish_as | string | none  
»»» price_type | integer | PriceType enum: 1 latest, 2 index, 3 mark  
»»» price_gap_type | string | none  
»»» price_gap_value | string | none  
»»» status_code | string | none  
»»» create_time_precise | string | Creation time (seconds.microseconds)  
»»» finish_time_precise | string | none  
»»» pos_margin_mode | string | none  
»»» position_mode | string | none  
»»» leverage | string | none  
»»» error_label | string | none  
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/list'
    query_param = 'sort_by=1'
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
    url="/futures/usdt/autoorder/v1/chase/list"
    query_param="sort_by=1"
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
      "orders": [
        {
          "id": "string",
          "user": "string",
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "price_limit": "string",
          "reduce_only": true,
          "text": "string",
          "create_time": 0,
          "finish_time": 0,
          "original_status": 0,
          "status": "string",
          "reason": "string",
          "fill_amount": "string",
          "average_fill_price": "string",
          "suborder_id": "string",
          "is_dual_mode": true,
          "side_label": "string",
          "position_side_output": "string",
          "chase_price": "string",
          "interval_sec": 0,
          "updated_at": 0,
          "suborder_price": "string",
          "suborder_ongoing": true,
          "suborder_finish_as": "string",
          "price_type": 0,
          "price_gap_type": "string",
          "price_gap_value": "string",
          "status_code": "string",
          "create_time_precise": "string",
          "finish_time_precise": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "leverage": "string",
          "error_label": "string"
        }
      ]
    }
    

##  Get chase order detail🔒 Authenticated

GET`/futures/{settle}/autoorder/v1/chase/detail`

GET `/futures/{settle}/autoorder/v1/chase/detail`

Get `chase order detail`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
id | query | string | Required | Order ID, must be a non-zero positive integer  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | GetChaseOrderDetailResp  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» order | ChaseOrder | Chase order detail or list item  
»» id | string | none  
»» user | string | none  
»» contract | string | none  
»» settle | string | none  
»» amount | string | Total size in contracts; positive for buy, negative for sell  
»» price_limit | string | none  
»» reduce_only | boolean | none  
»» text | string | none  
»» create_time | integer(int64) | none  
»» finish_time | integer(int64) | none  
»» original_status | integer | Raw status enum  
»» status | string | Simplified status, e.g. open / finished  
»» reason | string | none  
»» fill_amount | string | none  
»» average_fill_price | string | none  
»» suborder_id | string | none  
»» is_dual_mode | boolean | none  
»» side_label | string | none  
»» position_side_output | string | none  
»» chase_price | string | none  
»» interval_sec | integer(uint32) | none  
»» updated_at | integer(int64) | none  
»» suborder_price | string | none  
»» suborder_ongoing | boolean | none  
»» suborder_finish_as | string | none  
»» price_type | integer | PriceType enum: 1 latest, 2 index, 3 mark  
»» price_gap_type | string | none  
»» price_gap_value | string | none  
»» status_code | string | none  
»» create_time_precise | string | Creation time (seconds.microseconds)  
»» finish_time_precise | string | none  
»» pos_margin_mode | string | none  
»» position_mode | string | none  
»» leverage | string | none  
»» error_label | string | none  
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/detail'
    query_param = 'id=string'
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
    url="/futures/usdt/autoorder/v1/chase/detail"
    query_param="id=string"
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
      "order": {
        "id": "string",
        "user": "string",
        "contract": "string",
        "settle": "string",
        "amount": "string",
        "price_limit": "string",
        "reduce_only": true,
        "text": "string",
        "create_time": 0,
        "finish_time": 0,
        "original_status": 0,
        "status": "string",
        "reason": "string",
        "fill_amount": "string",
        "average_fill_price": "string",
        "suborder_id": "string",
        "is_dual_mode": true,
        "side_label": "string",
        "position_side_output": "string",
        "chase_price": "string",
        "interval_sec": 0,
        "updated_at": 0,
        "suborder_price": "string",
        "suborder_ongoing": true,
        "suborder_finish_as": "string",
        "price_type": 0,
        "price_gap_type": "string",
        "price_gap_value": "string",
        "status_code": "string",
        "create_time_precise": "string",
        "finish_time_precise": "string",
        "pos_margin_mode": "string",
        "position_mode": "string",
        "leverage": "string",
        "error_label": "string"
      }
    }
    

##  Query auto order list🔒 Authenticated

GET`/futures/{settle}/price_orders`

GET `/futures/{settle}/price_orders`

_Query auto order list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
status | query | string | Required | Query order list based on status  
contract | query | string | Optional | Futures contract, return related data only if specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
status | open  
status | finished  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FuturesPriceTriggeredOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures price-triggered order details]  
» _None_ | FuturesPriceTriggeredOrder | Futures price-triggered order details  
»» initial | object | none  
»»» contract | string | Futures contract  
»»» size | integer(int64) | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
»»» amount | string | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
»»» price | string | Order price. Set to 0 to use market price  
»»» tif | string | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
»»» text | string | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
»»» reduce_only | boolean | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
»»» is_reduce_only | boolean | Is the order reduce-only  
»»» is_close | boolean | Is the order to close position  
»» trigger | object | none  
»»» strategy_type | integer(int32) | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
»»» price_type | integer(int32) | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
»»» price | string | Price value for price trigger, or spread value for spread trigger  
»»» rule | integer(int32) | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
»»» expiration | integer | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
»» id | integer(int64) | Auto order ID  
»» id_string | string | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
»» user | integer | User ID  
»» create_time | number(double) | Created time  
»» finish_time | number(double) | End time  
»» trade_id | integer(int64) | ID of the order created after trigger  
»» status | string | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
»» finish_as | string | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
»» reason | string | Additional description of how the order was completed  
»» order_type | string | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
»» me_order_id | integer(int64) | Corresponding order ID for order take-profit/stop-loss orders  
»» pos_margin_mode | string | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
  
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
    
    url = '/futures/usdt/price_orders'
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
    url="/futures/usdt/price_orders"
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
        "initial": {
          "contract": "BTC_USDT",
          "size": 100,
          "price": "5.03"
        },
        "trigger": {
          "strategy_type": 0,
          "price_type": 0,
          "price": "3000",
          "rule": 1,
          "expiration": 86400
        },
        "id": 1283293,
        "id_string": "1283293",
        "user": 1234,
        "create_time": 1514764800,
        "finish_time": 1514764900,
        "trade_id": 13566,
        "status": "finished",
        "finish_as": "cancelled",
        "reason": "",
        "order_type": "close-long-order",
        "pos_margin_mode": "isolated"
      }
    ]
    

##  Create price-triggered order🔒 Authenticated

POST`/futures/{settle}/price_orders`

POST `/futures/{settle}/price_orders`

_Create price-triggered order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | FuturesPriceTriggeredOrder | Required | none  
↳ initial | body | object | Required | none  
↳ contract | body | string | Required | Futures contract  
↳ size | body | integer(int64) | Optional | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
↳ amount | body | string | Optional | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
↳ price | body | string | Required | Order price. Set to 0 to use market price  
↳ close | body | boolean | Optional | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
↳ tif | body | string | Optional | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
↳ text | body | string | Optional | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
↳ reduce_only | body | boolean | Optional | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
↳ auto_size | body | string | Optional | One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required  
↳ trigger | body | object | Required | none  
↳ strategy_type | body | integer(int32) | Optional | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
↳ price_type | body | integer(int32) | Optional | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
↳ price | body | string | Required | Price value for price trigger, or spread value for spread trigger  
↳ rule | body | integer(int32) | Required | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
↳ expiration | body | integer | Optional | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
↳ order_type | body | string | Optional | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
↳ pos_margin_mode | body | string | Optional | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**»» size** : Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0

**»» close** : When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.

**»» tif** : Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled

**»» text** : The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app

**»» auto_size** : One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required

**»» strategy_type** : Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)

**»» rule** : Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price

**» order_type** : Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests

**» pos_margin_mode** : Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
»» tif | gtc  
»» tif | ioc  
»» strategy_type | 0  
»» strategy_type | 1  
»» price_type | 0  
»» price_type | 1  
»» price_type | 2  
»» rule | 1  
»» rule | 2  
» pos_margin_mode | isolated  
» pos_margin_mode | cross  
settle | btc  
settle | usdt  
  
### Responses

  * 201[Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2)Order created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order created successfully | TriggerOrderResponse  
  
### Response Schema

Status Code **201**

_TriggerOrderResponse_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Auto order ID  
» id_string | string | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
  
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
    
    url = '/futures/usdt/price_orders'
    query_param = ''
    body='{"initial":{"contract":"BTC_USDT","size":100,"price":"5.03"},"trigger":{"strategy_type":0,"price_type":0,"price":"3000","rule":1,"expiration":86400},"order_type":"close-long-order","pos_margin_mode":"isolated"}'
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
    url="/futures/usdt/price_orders"
    query_param=""
    body_param='{"initial":{"contract":"BTC_USDT","size":100,"price":"5.03"},"trigger":{"strategy_type":0,"price_type":0,"price":"3000","rule":1,"expiration":86400},"order_type":"close-long-order","pos_margin_mode":"isolated"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "initial": {
        "contract": "BTC_USDT",
        "size": 100,
        "price": "5.03"
      },
      "trigger": {
        "strategy_type": 0,
        "price_type": 0,
        "price": "3000",
        "rule": 1,
        "expiration": 86400
      },
      "order_type": "close-long-order",
      "pos_margin_mode": "isolated"
    }
    

> Example responses

> 201 Response
    
    
    {
      "id": 1432329,
      "id_string": "1432329"
    }
    

##  Cancel all auto orders🔒 Authenticated

DELETE`/futures/{settle}/price_orders`

DELETE `/futures/{settle}/price_orders`

_Cancel all auto orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Optional | Futures contract, return related data only if specified  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Batch cancel request is received and processed. Success is determined based on the order list

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancel request is received and processed. Success is determined based on the order list | [FuturesPriceTriggeredOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures price-triggered order details]  
» _None_ | FuturesPriceTriggeredOrder | Futures price-triggered order details  
»» initial | object | none  
»»» contract | string | Futures contract  
»»» size | integer(int64) | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
»»» amount | string | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
»»» price | string | Order price. Set to 0 to use market price  
»»» tif | string | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
»»» text | string | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
»»» reduce_only | boolean | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
»»» is_reduce_only | boolean | Is the order reduce-only  
»»» is_close | boolean | Is the order to close position  
»» trigger | object | none  
»»» strategy_type | integer(int32) | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
»»» price_type | integer(int32) | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
»»» price | string | Price value for price trigger, or spread value for spread trigger  
»»» rule | integer(int32) | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
»»» expiration | integer | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
»» id | integer(int64) | Auto order ID  
»» id_string | string | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
»» user | integer | User ID  
»» create_time | number(double) | Created time  
»» finish_time | number(double) | End time  
»» trade_id | integer(int64) | ID of the order created after trigger  
»» status | string | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
»» finish_as | string | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
»» reason | string | Additional description of how the order was completed  
»» order_type | string | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
»» me_order_id | integer(int64) | Corresponding order ID for order take-profit/stop-loss orders  
»» pos_margin_mode | string | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
  
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
    
    url = '/futures/usdt/price_orders'
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
    url="/futures/usdt/price_orders"
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
        "initial": {
          "contract": "BTC_USDT",
          "size": 100,
          "price": "5.03"
        },
        "trigger": {
          "strategy_type": 0,
          "price_type": 0,
          "price": "3000",
          "rule": 1,
          "expiration": 86400
        },
        "id": 1283293,
        "id_string": "1283293",
        "user": 1234,
        "create_time": 1514764800,
        "finish_time": 1514764900,
        "trade_id": 13566,
        "status": "finished",
        "finish_as": "cancelled",
        "reason": "",
        "order_type": "close-long-order",
        "pos_margin_mode": "isolated"
      }
    ]
    

##  Query single auto order details🔒 Authenticated

GET`/futures/{settle}/price_orders/{order_id}`

GET `/futures/{settle}/price_orders/{order_id}`

_Query single auto order details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
order_id | path | integer(int64) | Required | ID returned when order is successfully created  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Auto order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Auto order details | FuturesPriceTriggeredOrder  
  
### Response Schema

Status Code **200**

_Futures price-triggered order details_

Name | Type | Description  
---|---|---  
» initial | object | none  
»» contract | string | Futures contract  
»» size | integer(int64) | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
»» amount | string | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
»» price | string | Order price. Set to 0 to use market price  
»» tif | string | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
»» text | string | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
»» reduce_only | boolean | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_close | boolean | Is the order to close position  
» trigger | object | none  
»» strategy_type | integer(int32) | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
»» price_type | integer(int32) | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
»» price | string | Price value for price trigger, or spread value for spread trigger  
»» rule | integer(int32) | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
»» expiration | integer | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
» id | integer(int64) | Auto order ID  
» id_string | string | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
» user | integer | User ID  
» create_time | number(double) | Created time  
» finish_time | number(double) | End time  
» trade_id | integer(int64) | ID of the order created after trigger  
» status | string | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
» finish_as | string | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
» reason | string | Additional description of how the order was completed  
» order_type | string | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
» me_order_id | integer(int64) | Corresponding order ID for order take-profit/stop-loss orders  
» pos_margin_mode | string | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
  
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
    
    url = '/futures/usdt/price_orders/0'
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
    url="/futures/usdt/price_orders/0"
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
      "initial": {
        "contract": "BTC_USDT",
        "size": 100,
        "price": "5.03"
      },
      "trigger": {
        "strategy_type": 0,
        "price_type": 0,
        "price": "3000",
        "rule": 1,
        "expiration": 86400
      },
      "id": 1283293,
      "id_string": "1283293",
      "user": 1234,
      "create_time": 1514764800,
      "finish_time": 1514764900,
      "trade_id": 13566,
      "status": "finished",
      "finish_as": "cancelled",
      "reason": "",
      "order_type": "close-long-order",
      "pos_margin_mode": "isolated"
    }
    

##  Cancel single auto order🔒 Authenticated

DELETE`/futures/{settle}/price_orders/{order_id}`

DELETE `/futures/{settle}/price_orders/{order_id}`

_Cancel single auto order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
order_id | path | integer(int64) | Required | ID returned when order is successfully created  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Auto order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Auto order details | FuturesPriceTriggeredOrder  
  
### Response Schema

Status Code **200**

_Futures price-triggered order details_

Name | Type | Description  
---|---|---  
» initial | object | none  
»» contract | string | Futures contract  
»» size | integer(int64) | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
»» amount | string | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
»» price | string | Order price. Set to 0 to use market price  
»» tif | string | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
»» text | string | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
»» reduce_only | boolean | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_close | boolean | Is the order to close position  
» trigger | object | none  
»» strategy_type | integer(int32) | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
»» price_type | integer(int32) | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
»» price | string | Price value for price trigger, or spread value for spread trigger  
»» rule | integer(int32) | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
»» expiration | integer | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
» id | integer(int64) | Auto order ID  
» id_string | string | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
» user | integer | User ID  
» create_time | number(double) | Created time  
» finish_time | number(double) | End time  
» trade_id | integer(int64) | ID of the order created after trigger  
» status | string | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
» finish_as | string | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
» reason | string | Additional description of how the order was completed  
» order_type | string | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
» me_order_id | integer(int64) | Corresponding order ID for order take-profit/stop-loss orders  
» pos_margin_mode | string | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
  
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
    
    url = '/futures/usdt/price_orders/0'
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
    url="/futures/usdt/price_orders/0"
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
      "initial": {
        "contract": "BTC_USDT",
        "size": 100,
        "price": "5.03"
      },
      "trigger": {
        "strategy_type": 0,
        "price_type": 0,
        "price": "3000",
        "rule": 1,
        "expiration": 86400
      },
      "id": 1283293,
      "id_string": "1283293",
      "user": 1234,
      "create_time": 1514764800,
      "finish_time": 1514764900,
      "trade_id": 13566,
      "status": "finished",
      "finish_as": "cancelled",
      "reason": "",
      "order_type": "close-long-order",
      "pos_margin_mode": "isolated"
    }
    

##  Modify a Single Auto Order🔒 Authenticated

PUT`/futures/{settle}/price_orders/amend`

PUT `/futures/{settle}/price_orders/amend`

_Modify a Single Auto Order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | FuturesUpdatePriceTriggeredOrder | Required | none  
↳ settle | body | string | Optional | Settlement Currency (e.g., USDT, BTC)  
↳ order_id | body | integer(int64) | Required | ID of the Pending Take-Profit/Stop-Loss Trigger Order  
↳ size | body | integer(int64) | Optional | Modified Contract Quantity. Full Close: 0; Partial Close: Positive/Negative values indicate direction (consistent with the creation interface logic).  
↳ amount | body | string | Optional | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
↳ price | body | string | Optional | Represents the modified trading price. A value of 0 indicates a market order.  
↳ trigger_price | body | string | Optional | Modified Trigger Price  
↳ price_type | body | integer(int32) | Optional | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
↳ auto_size | body | string | Optional | One-way Mode: auto_size is not required  
Hedge Mode partial closing (size≠0): auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
↳ close | body | boolean | Optional | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**» auto_size** : One-way Mode: auto_size is not required  
Hedge Mode partial closing (size≠0): auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions

**» close** : When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» price_type | 0  
» price_type | 1  
» price_type | 2  
settle | btc  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order created successfully | TriggerOrderResponse  
  
### Response Schema

Status Code **200**

_TriggerOrderResponse_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Auto order ID  
» id_string | string | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
  
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
    
    url = '/futures/usdt/price_orders/amend'
    query_param = ''
    body='{"order_id":123456789,"size":0,"price":"0","trigger_price":"988888","price_type":0,"auto_size":"close_long"}'
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
    url="/futures/usdt/price_orders/amend"
    query_param=""
    body_param='{"order_id":123456789,"size":0,"price":"0","trigger_price":"988888","price_type":0,"auto_size":"close_long"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": 123456789,
      "size": 0,
      "price": "0",
      "trigger_price": "988888",
      "price_type": 0,
      "auto_size": "close_long"
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": 1432329,
      "id_string": "1432329"
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
    
    

##  ContractStat

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | integer(int64) | Optional | none | Stat timestamp  
lsr_taker | number(double) | Optional | none | Long/short taker ratio  
lsr_account | number(double) | Optional | none | Long/short position user ratio  
long_liq_size | string | Optional | none | Long liquidation size (contracts)  
long_liq_amount | number(double) | Optional | none | Long liquidation amount (base currency)  
long_liq_usd | number(double) | Optional | none | Long liquidation volume (quote currency)  
long_liq_usd_new | number(double) | Optional | none | Long liquidations in quote currency; USDT settlement: long_liq_size × multiplier × mark price  
short_liq_size | string | Optional | none | Short liquidation size (contracts)  
short_liq_amount | number(double) | Optional | none | Short liquidation amount (base currency)  
short_liq_usd | number(double) | Optional | none | Short liquidation volume (quote currency)  
short_liq_usd_new | number(double) | Optional | none | Short liquidations in quote currency; USDT settlement: short_liq_size × multiplier × mark price  
open_interest | string | Optional | none | Total open interest size (contracts)  
open_interest_usd | number(double) | Optional | none | Total open interest volume (quote currency)  
top_lsr_account | number(double) | Optional | none | Top trader long/short account ratio  
top_lsr_size | string | Optional | none | Top trader long/short position ratio  
mark_price | number(double) | Optional | none | Mark price  
top_long_size | string | Optional | none | Top long open interest (contracts)  
top_short_size | string | Optional | none | Top short open interest (contracts)  
long_taker_size | string | Optional | none | Long taker trade volume (contracts)  
short_taker_size | string | Optional | none | Short taker trade volume (contracts)  
top_long_account | string | Optional | none | Number of top long accounts (large holders)  
top_short_account | string | Optional | none | Number of top short accounts (large holders)  
long_users | string | Optional | none | Number of users holding long positions  
short_users | string | Optional | none | Number of users holding short positions  
      
    
    {
      "time": 0,
      "lsr_taker": 0,
      "lsr_account": 0,
      "long_liq_size": "string",
      "long_liq_amount": 0,
      "long_liq_usd": 0,
      "long_liq_usd_new": 0,
      "short_liq_size": "string",
      "short_liq_amount": 0,
      "short_liq_usd": 0,
      "short_liq_usd_new": 0,
      "open_interest": "string",
      "open_interest_usd": 0,
      "top_lsr_account": 0,
      "top_lsr_size": "string",
      "mark_price": 0,
      "top_long_size": "string",
      "top_short_size": "string",
      "long_taker_size": "string",
      "short_taker_size": "string",
      "top_long_account": "string",
      "top_short_account": "string",
      "long_users": "string",
      "short_users": "string"
    }
    
    

##  FuturesAutoDeleverage

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | integer(int64) | Optional | read-only | Automatic deleveraging time  
user | integer(int64) | Optional | read-only | User ID  
order_id | integer(int64) | Optional | read-only | Order ID. Order IDs before 2023-02-20 are null  
contract | string | Optional | read-only | Futures contract  
leverage | string | Optional | read-only | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
cross_leverage_limit | string | Optional | read-only | leverage for cross margin  
entry_price | string | Optional | read-only | Average entry price  
fill_price | string | Optional | read-only | Average fill price  
trade_size | string | Optional | read-only | Trading size  
position_size | string | Optional | read-only | Positions after auto-deleveraging  
      
    
    {
      "time": 0,
      "user": 0,
      "order_id": 0,
      "contract": "string",
      "leverage": "string",
      "cross_leverage_limit": "string",
      "entry_price": "string",
      "fill_price": "string",
      "trade_size": "string",
      "position_size": "string"
    }
    
    

##  StopAllChaseOrdersReq

_Request body for stopping chase orders in batch_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contract | string | Optional | none | Optional contract name  
settle | string | Optional | none | Overridden by the path parameter  
pos_margin_mode | string | Optional | none | Optional margin mode  
      
    
    {
      "contract": "string",
      "settle": "string",
      "pos_margin_mode": "string"
    }
    
    

##  TriggerOrderResponse

_TriggerOrderResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Auto order ID  
id_string | string | Optional | read-only | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
      
    
    {
      "id": 0,
      "id_string": "string"
    }
    
    

##  FuturesUpdatePriceTriggeredOrder

_Modify Price Order Details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
settle | string | Optional | none | Settlement Currency (e.g., USDT, BTC)  
order_id | integer(int64) | Required | none | ID of the Pending Take-Profit/Stop-Loss Trigger Order  
size | integer(int64) | Optional | none | Modified Contract Quantity. Full Close: 0; Partial Close: Positive/Negative values indicate direction (consistent with the creation interface logic).  
amount | string | Optional | none | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
price | string | Optional | none | Represents the modified trading price. A value of 0 indicates a market order.  
trigger_price | string | Optional | none | Modified Trigger Price  
price_type | integer(int32) | Optional | none | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
auto_size | string | Optional | none | One-way Mode: auto_size is not required  
Hedge Mode partial closing (size≠0): auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
close | boolean | Optional | none | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
      
    
    {
      "settle": "string",
      "order_id": 0,
      "size": 0,
      "amount": "string",
      "price": "string",
      "trigger_price": "string",
      "price_type": 0,
      "auto_size": "string",
      "close": true
    }
    
    

##  BatchFundingRatesRequest

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contracts | array | Required | none | Array of Contract Names  
      
    
    {
      "contracts": [
        "BTC_USDT",
        "ETH_USDT"
      ]
    }
    
    

##  CancelBatchFutureOrdersRequest

_Order ID array_

###  Properties

_None_
    
    
    [
      "string"
    ]
    
    

##  UpdateTrailOrder

_UpdateTrailOrder_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Required | none | Order ID  
amount | string | Optional | none | Total trading quantity in contracts, positive for buy, negative for sell, 0 means no modification  
activation_price | string | Optional | none | Activation price, 0 means trigger immediately, empty means no modification  
is_gte_str | string | Optional | none | true: activate when market price >= activation price, false: <= activation price, empty means no modification  
price_type | integer(int32) | Optional | none | Activation price type, not provided or 0 means no modification, 1-latest price, 2-index price, 3-mark price  
price_offset | string | Optional | none | Callback ratio or price distance, e.g., `0.1` or `0.1%`; empty means no modification  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
      
    
    {
      "id": 0,
      "amount": "string",
      "activation_price": "string",
      "is_gte_str": "string",
      "price_type": 0,
      "price_offset": "string"
    }
    
    

##  FuturesRiskLimitTier

_Information for each tier of the gradient risk limit table_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
tier | integer(int) | Optional | none | Tier  
risk_limit | string | Optional | none | Position risk limit  
initial_rate | string | Optional | none | Initial margin rate  
maintenance_rate | string | Optional | none | The maintenance margin rate of the first tier of risk limit sheet  
leverage_max | string | Optional | none | Maximum leverage  
deduction | string | Optional | none | Maintenance margin quick calculation deduction amount  
      
    
    {
      "tier": 0,
      "risk_limit": "string",
      "initial_rate": "string",
      "maintenance_rate": "string",
      "leverage_max": "string",
      "deduction": "string"
    }
    
    

##  FuturesLiquidate

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | integer(int64) | Optional | read-only | Liquidation time  
contract | string | Optional | read-only | Futures contract  
leverage | string | Optional | read-only | Position leverage. Not returned in public endpoints  
size | string | Optional | read-only | Position size  
margin | string | Optional | read-only | Position margin. Not returned in public endpoints  
entry_price | string | Optional | read-only | Average entry price. Not returned in public endpoints  
liq_price | string | Optional | read-only | Liquidation price. Not returned in public endpoints  
mark_price | string | Optional | read-only | Mark price. Not returned in public endpoints  
order_id | integer(int64) | Optional | read-only | Liquidation order ID. Not returned in public endpoints  
order_price | string | Optional | read-only | Liquidation order price  
fill_price | string | Optional | read-only | Liquidation order average taker price  
left | string | Optional | read-only | Liquidation order maker size  
      
    
    {
      "time": 0,
      "contract": "string",
      "leverage": "string",
      "size": "string",
      "margin": "string",
      "entry_price": "string",
      "liq_price": "string",
      "mark_price": "string",
      "order_id": 0,
      "order_price": "string",
      "fill_price": "string",
      "left": "string"
    }
    
    

##  CreateChaseOrderReq

_Request body for creating a chase order_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contract | string | Required | none | Contract name; server-side converted to uppercase  
settle | string | Optional | none | Settle currency, overridden by the path parameter and converted to lowercase  
amount | string | Required | none | Total order size in contracts, decimal string. Positive for buy, negative for sell. Cannot be 0  
price_limit | string | Required | none | Maximum chase price as a valid decimal string. Pass "0" when no price limit is set  
offset_limit | string | Optional | none | Maximum chasing distance from the best price, mutually exclusive with price_limit  
reduce_only | boolean | Optional | none | Whether reduce only  
text | string | Optional | none | Optional custom tag  
is_dual_mode | boolean | Optional | none | Whether dual-position mode is enabled  
price_type | integer(int64) | Optional | none | Price type: 1 best bid/ask, 2 distance from best bid/ask  
price_gap_type | integer(int64) | Optional | none | Used when price_type == 2: 1 absolute price gap, 2 percentage  
price_gap_value | string | Optional | none | Price gap value paired with price_gap_type  
pos_margin_mode | string | Optional | none | Position margin mode, e.g. isolated or cross  
position_mode | string | Optional | none | Position mode (e.g. single, dual, dual_plus)  
      
    
    {
      "contract": "string",
      "settle": "string",
      "amount": "string",
      "price_limit": "string",
      "offset_limit": "string",
      "reduce_only": true,
      "text": "string",
      "is_dual_mode": true,
      "price_type": 0,
      "price_gap_type": 0,
      "price_gap_value": "string",
      "pos_margin_mode": "string",
      "position_mode": "string"
    }
    
    

##  PositionTimerange

_Contract position details (historical data)_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contract | string | Optional | read-only | Futures contract  
size | string | Optional | read-only | Position size  
leverage | string | Optional | none | Position leverage. 0 means cross margin; positive number means isolated margin  
risk_limit | string | Optional | none | Position risk limit  
leverage_max | string | Optional | read-only | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
maintenance_rate | string | Optional | read-only | The maintenance margin rate of the first tier of risk limit sheet  
margin | string | Optional | none | Position margin  
liq_price | string | Optional | read-only | Liquidation price  
realised_pnl | string | Optional | read-only | Realized PnL  
history_pnl | string | Optional | read-only | Total realized PnL from closed positions  
last_close_pnl | string | Optional | read-only | PNL of last position close  
realised_point | string | Optional | read-only | Realized POINT PNL  
history_point | string | Optional | read-only | History realized POINT PNL  
mode | string | Optional | none | Position mode, including:  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
cross_leverage_limit | string | Optional | none | Cross margin leverage (valid only when `leverage` is 0)  
entry_price | string | Optional | read-only | Entry price  
time | integer(int64) | Optional | none | Timestamp  
      
    
    {
      "contract": "string",
      "size": "string",
      "leverage": "string",
      "risk_limit": "string",
      "leverage_max": "string",
      "maintenance_rate": "string",
      "margin": "string",
      "liq_price": "string",
      "realised_pnl": "string",
      "history_pnl": "string",
      "last_close_pnl": "string",
      "realised_point": "string",
      "history_point": "string",
      "mode": "string",
      "cross_leverage_limit": "string",
      "entry_price": "string",
      "time": 0
    }
    
    

##  FuturesLimitRiskTiers

_Retrieve risk limit configurations for different tiers under a specified contract_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
tier | integer(int) | Optional | none | Tier  
risk_limit | string | Optional | none | Position risk limit  
initial_rate | string | Optional | none | Initial margin rate  
maintenance_rate | string | Optional | none | The maintenance margin rate of the first tier of risk limit sheet  
leverage_max | string | Optional | none | Maximum leverage  
contract | string | Optional | none | Market, only visible when market pagination is requested  
deduction | string | Optional | none | Maintenance margin quick calculation deduction amount  
      
    
    {
      "tier": 0,
      "risk_limit": "string",
      "initial_rate": "string",
      "maintenance_rate": "string",
      "leverage_max": "string",
      "contract": "string",
      "deduction": "string"
    }
    
    

##  BatchAmendOrderReq

_Modify contract order parameters_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional | none | Order id, order_id and text must contain at least one  
text | string | Optional | none | User-defined order text, at least one of order_id and text must be passed  
size | string | Optional | none | New order size, including filled size.  
\- If less than or equal to the filled quantity, the order will be cancelled.  
\- The new order side must be identical to the original one.  
\- Close order size cannot be modified.  
\- For reduce-only orders, increasing the size may cancel other reduce-only orders.  
\- If the price is not modified, decreasing the size will not affect the depth queue, while increasing the size will place it at the end of the current price level.  
price | string | Optional | none | New order price  
amend_text | string | Optional | none | Custom info during order amendment  
action_mode | string | Optional | none | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
      
    
    {
      "order_id": 0,
      "text": "string",
      "size": "string",
      "price": "string",
      "amend_text": "string",
      "action_mode": "string"
    }
    
    

##  StopAllChaseOrdersResp

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
orders | [ChaseOrder] | Optional | none | [Chase order detail or list item]  
      
    
    {
      "orders": [
        {
          "id": "string",
          "user": "string",
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "price_limit": "string",
          "reduce_only": true,
          "text": "string",
          "create_time": 0,
          "finish_time": 0,
          "original_status": 0,
          "status": "string",
          "reason": "string",
          "fill_amount": "string",
          "average_fill_price": "string",
          "suborder_id": "string",
          "is_dual_mode": true,
          "side_label": "string",
          "position_side_output": "string",
          "chase_price": "string",
          "interval_sec": 0,
          "updated_at": 0,
          "suborder_price": "string",
          "suborder_ongoing": true,
          "suborder_finish_as": "string",
          "price_type": 0,
          "price_gap_type": "string",
          "price_gap_value": "string",
          "status_code": "string",
          "create_time_precise": "string",
          "finish_time_precise": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "leverage": "string",
          "error_label": "string"
        }
      ]
    }
    
    

##  FuturesOrderBook

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Order Book ID. Increases by 1 on every order book change. Set `with_id=true` to include this field in response  
current | number(double) | Optional | none | Response data generation timestamp  
update | number(double) | Optional | none | Order book changed timestamp  
asks | array | Required | none | Ask Depth  
↳ FuturesOrderBookItem | object | Optional | none | none  
↳ p | string | Optional | none | Price (quote currency)  
↳ s | string | Optional | none | Size  
↳ bids | array | Required | none | Bid Depth  
↳ FuturesOrderBookItem | object | Optional | none | none  
↳ p | string | Optional | none | Price (quote currency)  
↳ s | string | Optional | none | Size  
      
    
    {
      "id": 0,
      "current": 0,
      "update": 0,
      "asks": [
        {
          "p": "string",
          "s": "string"
        }
      ],
      "bids": [
        {
          "p": "string",
          "s": "string"
        }
      ]
    }
    
    

##  FuturesIndexConstituents

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
index | string | Optional | read-only | Index name  
constituents | array | Optional | read-only | Constituents  
↳ IndexConstituent | object | Optional | none | none  
↳ exchange | string | Optional | none | Exchange  
↳ symbols | array | Optional | none | Symbol list  
      
    
    {
      "index": "string",
      "constituents": [
        {
          "exchange": "string",
          "symbols": []
        }
      ]
    }
    
    

##  FuturesPositionCrossMode

_FuturesPositionCrossMode_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
mode | string | Required | none | Cross/isolated margin mode. ISOLATED - isolated margin, CROSS - cross margin  
contract | string | Required | none | Futures market  
      
    
    {
      "mode": "string",
      "contract": "BTC_USDT"
    }
    
    

##  PositionClose

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | number(double) | Optional | read-only | Position close time  
contract | string | Optional | read-only | Futures contract  
side | string | Optional | read-only | Position side  
  
\- `long`: Long position  
\- `short`: Short position  
pnl | string | Optional | read-only | PnL  
pnl_pnl | string | Optional | read-only | PNL - Position P/L  
pnl_fund | string | Optional | read-only | PNL - Funding Fees  
pnl_fee | string | Optional | read-only | PNL - Transaction Fees  
text | string | Optional | read-only | Source of close order. See `order.text` field for specific values  
max_size | string | Optional | read-only | Max Trade Size  
accum_size | string | Optional | read-only | Cumulative closed position volume  
first_open_time | integer(int64) | Optional | read-only | First Open Time  
long_price | string | Optional | read-only | When side is 'long', it indicates the opening average price; when side is 'short', it indicates the closing average price  
short_price | string | Optional | read-only | When side is 'long', it indicates the closing average price; when side is 'short', it indicates the opening average price  
  
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
      "pnl_pnl": "string",
      "pnl_fund": "string",
      "pnl_fee": "string",
      "text": "string",
      "max_size": "string",
      "accum_size": "string",
      "first_open_time": 0,
      "long_price": "string",
      "short_price": "string"
    }
    
    

##  FuturesTrade

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Fill ID  
create_time | number(double) | Optional | none | Fill Time  
create_time_ms | number(double) | Optional | none | Trade time, with millisecond precision to 3 decimal places  
contract | string | Optional | none | Futures contract  
size | string | Optional | none | Trading size  
price | string | Optional | none | Trade price (quote currency)  
is_internal | boolean | Optional | none | Deprecated  
      
    
    {
      "id": 0,
      "create_time": 0,
      "create_time_ms": 0,
      "contract": "string",
      "size": "string",
      "price": "string",
      "is_internal": true
    }
    
    

##  FuturesBBOOrder

_contractBBOorderdetails_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contract | string | Required | none | Futures contract  
size | integer(int64) | Required | none | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
direction | string | Required | none | Direction: 'sell' fetches the bid side, 'buy' fetches the ask side.  
iceberg | integer(int64) | Optional | none | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
level | integer(int64) | Required | write-only | Level: maximum 20 levels  
close | boolean | Optional | write-only | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | read-only | Is the order to close position  
reduce_only | boolean | Optional | write-only | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | read-only | Is the order reduce-only  
is_liq | boolean | Optional | read-only | Is the order for liquidation  
tif | string | Optional | none | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | integer(int64) | Optional | read-only | Unfilled quantity  
fill_price | string | Optional | read-only | Fill price  
text | string | Optional | none | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Content can only contain numbers, letters, underscores (_), hyphens (-), or dots (.)  
  
In addition to user custom information, the following are internal reserved fields identifying order sources:  
  
\- web: Web  
\- api: API Call  
\- app: Mobile App  
\- auto_deleveraging: Auto-Deleveraging  
\- liquidation: Forced Liquidation of Legacy Classic Mode Positions  
\- liq-xxx: a. Forced liquidation of New Classic Mode positions, including isolated margin, single-direction cross margin, and non-hedged dual-direction cross margin positions. b. Forced liquidation of isolated margin positions in Unified Account Single-Currency Margin Mode  
\- hedge-liq-xxx: Forced liquidation of hedged portions in New Classic Mode dual-direction cross margin (simultaneous closing of long and short positions)  
\- pm_liquidate: Forced liquidation in Unified Account Cross-Currency Margin Mode  
\- comb_margin_liquidate: Forced liquidation in Unified Account Portfolio Margin Mode  
\- scm_liquidate: Forced liquidation of positions in Unified Account Single-Currency Margin Mode  
\- insurance: Insurance  
tkfr | string | Optional | read-only | Taker fee  
mkfr | string | Optional | read-only | Maker fee  
refu | integer | Optional | read-only | Referrer user ID  
auto_size | string | Optional | write-only | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | read-only | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | none | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | read-only | The custom data that the user remarked when amending the order  
pid | integer(int64) | Optional | write-only | Position ID  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
auto_size | close_long  
auto_size | close_short  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
      
    
    {
      "contract": "string",
      "size": 0,
      "direction": "string",
      "iceberg": 0,
      "level": 0,
      "close": false,
      "is_close": true,
      "reduce_only": false,
      "is_reduce_only": true,
      "is_liq": true,
      "tif": "gtc",
      "left": 0,
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "auto_size": "close_long",
      "stp_id": 0,
      "stp_act": "co",
      "amend_text": "string",
      "pid": 0
    }
    
    

##  TrailOrderDetailResponse

_TrailOrderDetailResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Optional | none | Status code, 0 means success  
message | string | Optional | none | Response message  
data | object | Optional | none | none  
↳ order | object | Optional | none | Trail order details  
↳ id | integer(int64) | Optional | read-only | Order ID  
↳ user_id | integer(int64) | Optional | read-only | User ID  
↳ user | integer(int64) | Optional | read-only | User ID  
↳ contract | string | Optional | none | Contract name  
↳ settle | string | Optional | none | Settle currency  
↳ amount | string | Optional | none | Trading quantity in contracts, positive for buy, negative for sell  
↳ is_gte | boolean | Optional | none | true: activate when market price >= activation price, false: <= activation price  
↳ activation_price | string | Optional | none | Activation price, 0 means trigger immediately  
↳ price_type | integer(int32) | Optional | none | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price  
↳ price_offset | string | Optional | none | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
↳ text | string | Optional | none | Custom field  
↳ reduce_only | boolean | Optional | none | Reduce Position Only  
↳ position_related | boolean | Optional | none | Whether bound to position  
↳ created_at | integer(int64) | Optional | read-only | Created time  
↳ activated_at | integer(int64) | Optional | read-only | Activation time  
↳ finished_at | integer(int64) | Optional | read-only | End time  
↳ create_time | integer(int64) | Optional | read-only | Created time  
↳ active_time | integer(int64) | Optional | read-only | Activation time  
↳ finish_time | integer(int64) | Optional | read-only | End time  
↳ reason | string | Optional | read-only | End reason  
↳ suborder_text | string | Optional | read-only | Sub-order text field  
↳ is_dual_mode | boolean | Optional | read-only | Whether dual position mode when creating order  
↳ trigger_price | string | Optional | read-only | Trigger price  
↳ suborder_id | integer(int64) | Optional | read-only | Sub-order ID  
↳ side_label | string | Optional | read-only | Order direction label: long/short/open long/open short/close long/close short  
↳ original_status | integer(int32) | Optional | read-only | Order status  
↳ status | string | Optional | read-only | Simplified order status: open/finished  
↳ position_side_output | string | Optional | read-only | Same as side_label, client requires consistency with other order types  
↳ updated_at | integer(int64) | Optional | read-only | Update time  
↳ extremum_price | string | Optional | read-only | Extremum price  
↳ status_code | string | Optional | read-only | Status code value  
↳ created_at_precise | string | Optional | read-only | Creation time (high precision, seconds.microseconds format)  
↳ finished_at_precise | string | Optional | read-only | End time (high precision, seconds.microseconds format)  
↳ activated_at_precise | string | Optional | read-only | Activation time (high precision, seconds.microseconds format)  
↳ status_label | string | Optional | read-only | Status internationalization label (translated status text)  
↳ pos_margin_mode | string | Optional | read-only | Position margin mode: isolated/cross  
↳ position_mode | string | Optional | read-only | Position mode: single, dual, and dual_plus  
↳ error_label | string | Optional | read-only | Error label  
↳ leverage | string | Optional | read-only | leverage  
↳ timestamp | integer(int64) | Optional | none | Response timestamp (milliseconds)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
status | open  
status | finished  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "order": {
          "id": 0,
          "user_id": 0,
          "user": 0,
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "is_gte": true,
          "activation_price": "string",
          "price_type": 0,
          "price_offset": "string",
          "text": "string",
          "reduce_only": true,
          "position_related": true,
          "created_at": 0,
          "activated_at": 0,
          "finished_at": 0,
          "create_time": 0,
          "active_time": 0,
          "finish_time": 0,
          "reason": "string",
          "suborder_text": "string",
          "is_dual_mode": true,
          "trigger_price": "string",
          "suborder_id": 0,
          "side_label": "string",
          "original_status": 0,
          "status": "open",
          "position_side_output": "string",
          "updated_at": 0,
          "extremum_price": "string",
          "status_code": "string",
          "created_at_precise": "string",
          "finished_at_precise": "string",
          "activated_at_precise": "string",
          "status_label": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "error_label": "string",
          "leverage": "string"
        }
      },
      "timestamp": 0
    }
    
    

##  FuturesCandlestick

_data point in every timestamp_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
t | number(double) | Optional | none | Unix timestamp in seconds  
v | string | Optional | none | size volume (contract size). Only returned if `contract` is not prefixed  
c | string | Optional | none | Close price (quote currency)  
h | string | Optional | none | Highest price (quote currency)  
l | string | Optional | none | Lowest price (quote currency)  
o | string | Optional | none | Open price (quote currency)  
sum | string | Optional | none | Trading volume (unit: Quote currency)  
      
    
    {
      "t": 0,
      "v": "string",
      "c": "string",
      "h": "string",
      "l": "string",
      "o": "string",
      "sum": "string"
    }
    
    

##  BatchFuturesOrder

_Futures order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
succeeded | boolean | Optional | none | Request execution result  
label | string | Optional | none | Error label, only exists if execution fails  
detail | string | Optional | none | Error detail, only present if execution failed and details need to be given  
id | integer(int64) | Optional | read-only | Futures order ID  
user | integer | Optional | read-only | User ID  
create_time | number(double) | Optional | read-only | Creation time of order  
finish_time | number(double) | Optional | read-only | Order finished time. Not returned if order is open  
finish_as | string | Optional | read-only | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | read-only | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Optional | none | Futures contract  
size | string | Optional | none | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | string | Optional | none | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Optional | none | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
close | boolean | Optional | write-only | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | read-only | Is the order to close position  
reduce_only | boolean | Optional | write-only | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | read-only | Is the order reduce-only  
is_liq | boolean | Optional | read-only | Is the order for liquidation  
tif | string | Optional | none | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | string | Optional | read-only | Unfilled quantity  
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
auto_size | string | Optional | write-only | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_act | string | Optional | none | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
stp_id | integer | Optional | read-only | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
market_order_slip_ratio | string | Optional | none | The maximum slippage ratio  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
auto_size | close_long  
auto_size | close_short  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
      
    
    {
      "succeeded": true,
      "label": "string",
      "detail": "string",
      "id": 0,
      "user": 0,
      "create_time": 0,
      "finish_time": 0,
      "finish_as": "filled",
      "status": "open",
      "contract": "string",
      "size": "string",
      "iceberg": "string",
      "price": "string",
      "close": false,
      "is_close": true,
      "reduce_only": false,
      "is_reduce_only": true,
      "is_liq": true,
      "tif": "gtc",
      "left": "string",
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "auto_size": "close_long",
      "stp_act": "co",
      "stp_id": 0,
      "market_order_slip_ratio": "string"
    }
    
    

##  StopTrailOrder

_StopTrailOrder_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Order ID, if ID is specified, text is not needed  
text | string | Optional | none | Custom text, if ID is not specified, terminate based on user_id and text  
      
    
    {
      "id": 0,
      "text": "string"
    }
    
    

##  GetChaseOrdersResp

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
orders | [ChaseOrder] | Optional | none | [Chase order detail or list item]  
      
    
    {
      "orders": [
        {
          "id": "string",
          "user": "string",
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "price_limit": "string",
          "reduce_only": true,
          "text": "string",
          "create_time": 0,
          "finish_time": 0,
          "original_status": 0,
          "status": "string",
          "reason": "string",
          "fill_amount": "string",
          "average_fill_price": "string",
          "suborder_id": "string",
          "is_dual_mode": true,
          "side_label": "string",
          "position_side_output": "string",
          "chase_price": "string",
          "interval_sec": 0,
          "updated_at": 0,
          "suborder_price": "string",
          "suborder_ongoing": true,
          "suborder_finish_as": "string",
          "price_type": 0,
          "price_gap_type": "string",
          "price_gap_value": "string",
          "status_code": "string",
          "create_time_precise": "string",
          "finish_time_precise": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "leverage": "string",
          "error_label": "string"
        }
      ]
    }
    
    

##  FuturesTicker

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contract | string | Optional | none | Futures contract  
last | string | Optional | none | Last trading price  
change_percentage | string | Optional | none | Price change percentage. Negative values indicate price decrease, e.g. -7.45  
total_size | string | Optional | none | Contract total size  
low_24h | string | Optional | none | 24-hour lowest price  
high_24h | string | Optional | none | 24-hour highest price  
volume_24h | string | Optional | none | 24-hour trading volume  
volume_24h_btc | string | Optional | none | 24-hour trading volume in BTC (deprecated, use `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle` instead)  
volume_24h_usd | string | Optional | none | 24-hour trading volume in USD (deprecated, use `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle` instead)  
volume_24h_base | string | Optional | none | 24-hour trading volume in base currency  
volume_24h_quote | string | Optional | none | 24-hour trading volume in quote currency  
volume_24h_settle | string | Optional | none | 24-hour trading volume in settle currency  
mark_price | string | Optional | none | Recent mark price  
funding_rate | string | Optional | none | Funding rate  
funding_rate_indicative | string | Optional | none | Indicative Funding rate in next period. (deprecated. use `funding_rate`)  
index_price | string | Optional | none | Index price  
quanto_base_rate | string | Optional | none | Deprecated  
lowest_ask | string | Optional | none | Recent lowest ask  
lowest_size | string | Optional | none | The latest seller's lowest price order quantity  
highest_bid | string | Optional | none | Recent highest bid  
highest_size | string | Optional | none | The latest buyer's highest price order volume  
change_utc0 | string | Optional | none | Percentage change at utc0. Negative values indicate a drop, e.g., -7.45%  
change_utc8 | string | Optional | none | Percentage change at utc8. Negative values indicate a drop, e.g., -7.45%  
change_price | string | Optional | none | 24h change amount. Negative values indicate a drop, e.g., -7.45  
change_utc0_price | string | Optional | none | Change amount at utc0. Negative values indicate a drop, e.g., -7.45  
change_utc8_price | string | Optional | none | Change amount at utc8. Negative values indicate a drop, e.g., -7.45  
      
    
    {
      "contract": "string",
      "last": "string",
      "change_percentage": "string",
      "total_size": "string",
      "low_24h": "string",
      "high_24h": "string",
      "volume_24h": "string",
      "volume_24h_btc": "string",
      "volume_24h_usd": "string",
      "volume_24h_base": "string",
      "volume_24h_quote": "string",
      "volume_24h_settle": "string",
      "mark_price": "string",
      "funding_rate": "string",
      "funding_rate_indicative": "string",
      "index_price": "string",
      "quanto_base_rate": "string",
      "lowest_ask": "string",
      "lowest_size": "string",
      "highest_bid": "string",
      "highest_size": "string",
      "change_utc0": "string",
      "change_utc8": "string",
      "change_price": "string",
      "change_utc0_price": "string",
      "change_utc8_price": "string"
    }
    
    

##  GetChaseOrderDetailResp

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order | ChaseOrder | Optional | none | Chase order detail or list item  
      
    
    {
      "order": {
        "id": "string",
        "user": "string",
        "contract": "string",
        "settle": "string",
        "amount": "string",
        "price_limit": "string",
        "reduce_only": true,
        "text": "string",
        "create_time": 0,
        "finish_time": 0,
        "original_status": 0,
        "status": "string",
        "reason": "string",
        "fill_amount": "string",
        "average_fill_price": "string",
        "suborder_id": "string",
        "is_dual_mode": true,
        "side_label": "string",
        "position_side_output": "string",
        "chase_price": "string",
        "interval_sec": 0,
        "updated_at": 0,
        "suborder_price": "string",
        "suborder_ongoing": true,
        "suborder_finish_as": "string",
        "price_type": 0,
        "price_gap_type": "string",
        "price_gap_value": "string",
        "status_code": "string",
        "create_time_precise": "string",
        "finish_time_precise": "string",
        "pos_margin_mode": "string",
        "position_mode": "string",
        "leverage": "string",
        "error_label": "string"
      }
    }
    
    

##  UpdateDualCompPositionCrossModeRequest

_UpdateDualCompPositionCrossModeRequest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
mode | string | Required | none | Cross/isolated margin mode. ISOLATED - isolated margin, CROSS - cross margin  
contract | string | Required | none | Futures market  
      
    
    {
      "mode": "string",
      "contract": "BTC_USDT"
    }
    
    

##  FundingRateRecord

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
t | integer(int64) | Optional | none | Unix timestamp in seconds  
r | string | Optional | none | Funding rate  
      
    
    {
      "t": 0,
      "r": "string"
    }
    
    

##  FuturesPremiumIndex

_data point in every timestamp_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
t | number(double) | Optional | none | Unix timestamp in seconds  
c | string | Optional | none | Close price  
h | string | Optional | none | Highest price  
l | string | Optional | none | Lowest price  
o | string | Optional | none | Open price  
      
    
    {
      "t": 0,
      "c": "string",
      "h": "string",
      "l": "string",
      "o": "string"
    }
    
    

##  BatchFundingRatesResponse

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contract | string | Optional | none | Contract name  
data | array | Optional | none | Array of Funding Rates  
↳ t | integer(int64) | Optional | none | Unix timestamp in seconds  
↳ r | string | Optional | none | Funding rate  
      
    
    {
      "contract": "string",
      "data": [
        {
          "t": 0,
          "r": "string"
        }
      ]
    }
    
    

##  StopChaseOrderResp

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order | ChaseOrder | Optional | none | Chase order detail or list item  
      
    
    {
      "order": {
        "id": "string",
        "user": "string",
        "contract": "string",
        "settle": "string",
        "amount": "string",
        "price_limit": "string",
        "reduce_only": true,
        "text": "string",
        "create_time": 0,
        "finish_time": 0,
        "original_status": 0,
        "status": "string",
        "reason": "string",
        "fill_amount": "string",
        "average_fill_price": "string",
        "suborder_id": "string",
        "is_dual_mode": true,
        "side_label": "string",
        "position_side_output": "string",
        "chase_price": "string",
        "interval_sec": 0,
        "updated_at": 0,
        "suborder_price": "string",
        "suborder_ongoing": true,
        "suborder_finish_as": "string",
        "price_type": 0,
        "price_gap_type": "string",
        "price_gap_value": "string",
        "status_code": "string",
        "create_time_precise": "string",
        "finish_time_precise": "string",
        "pos_margin_mode": "string",
        "position_mode": "string",
        "leverage": "string",
        "error_label": "string"
      }
    }
    
    

##  FuturesOrderTimerange

_Futures order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | read-only | Futures order ID  
user | integer | Optional | read-only | User ID  
create_time | number(double) | Optional | read-only | Creation time of order  
update_time | string | Optional | read-only | OrderUpdateTime  
finish_time | string | Optional | read-only | Order finished time. Not returned if order is open  
finish_as | string | Optional | read-only | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | read-only | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required | none | Futures contract  
size | string | Required | none | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | string | Optional | none | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Required | none | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
close | boolean | Optional | write-only | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | read-only | Is the order to close position  
reduce_only | boolean | Optional | write-only | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | read-only | Is the order reduce-only  
is_liq | boolean | Optional | read-only | Is the order for liquidation  
tif | string | Optional | none | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | string | Optional | read-only | Unfilled quantity  
fill_price | string | Optional | read-only | Fill price  
text | string | Optional | none | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
tkfr | string | Optional | read-only | Taker fee  
mkfr | string | Optional | read-only | Maker fee  
refu | integer | Optional | read-only | Referrer user ID  
auto_size | string | Optional | write-only | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | read-only | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | none | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | read-only | The custom data that the user remarked when amending the order  
pid | integer(int64) | Optional | write-only | Position ID  
market_order_slip_ratio | string | Optional | none | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
pos_margin_mode | string | Optional | none | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
tpsl_tp_trigger_price | string | Optional | none | Take profit price  
tpsl_sl_trigger_price | string | Optional | none | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
auto_size | close_long  
auto_size | close_short  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
      
    
    {
      "id": 0,
      "user": 0,
      "create_time": 0,
      "update_time": "string",
      "finish_time": "string",
      "finish_as": "filled",
      "status": "open",
      "contract": "string",
      "size": "string",
      "iceberg": "string",
      "price": "string",
      "close": false,
      "is_close": true,
      "reduce_only": false,
      "is_reduce_only": true,
      "is_liq": true,
      "tif": "gtc",
      "left": "string",
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "auto_size": "close_long",
      "stp_id": 0,
      "stp_act": "co",
      "amend_text": "string",
      "pid": 0,
      "market_order_slip_ratio": "string",
      "pos_margin_mode": "string",
      "tpsl_tp_trigger_price": "string",
      "tpsl_sl_trigger_price": "string"
    }
    
    

##  FuturesAccount

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
total | string | Optional | none | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional | none | Unrealized PNL  
position_margin | string | Optional | none | Deprecated  
order_margin | string | Optional | none | initial margin of all open orders  
available | string | Optional | none | Refers to the available withdrawal or trading amount in per-position, specifically the per-position available balance under the unified account that includes the credit line (which incorporates trial funds; since trial funds cannot be withdrawn, the actual withdrawal amount needs to deduct the trial fund portion when processing withdrawals)  
point | string | Optional | none | Point card amount  
currency | string | Optional | none | Settlement currency  
in_dual_mode | boolean | Optional | none | Whether Hedge Mode is enabled  
enable_credit | boolean | Optional | none | Whether portfolio margin account mode is enabled  
position_initial_margin | string | Optional | none | Initial margin occupied by positions, applicable to unified account mode  
maintenance_margin | string | Optional | none | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode  
bonus | string | Optional | none | Bonus  
enable_evolved_classic | boolean | Optional | none | Deprecated  
cross_order_margin | string | Optional | none | Cross margin order margin, applicable to new classic account margin mode  
cross_initial_margin | string | Optional | none | Cross margin initial margin, applicable to new classic account margin mode  
cross_maintenance_margin | string | Optional | none | Cross margin maintenance margin, applicable to new classic account margin mode  
cross_unrealised_pnl | string | Optional | none | Cross margin unrealized P&L, applicable to new classic account margin mode  
cross_available | string | Optional | none | Cross margin available balance, applicable to new classic account margin mode  
cross_margin_balance | string | Optional | none | Cross margin balance, applicable to new classic account margin mode  
cross_mmr | string | Optional | none | Cross margin maintenance margin rate, applicable to new classic account margin mode  
cross_imr | string | Optional | none | Cross margin initial margin rate, applicable to new classic account margin mode  
isolated_position_margin | string | Optional | none | Isolated position margin, applicable to new classic account margin mode  
enable_new_dual_mode | boolean | Optional | none | Deprecated  
margin_mode | integer | Optional | none | Margin mode of the account  
0: classic future account or Classic Spot Margin Mode of unified account;  
1: Multi-Currency Margin Mode;  
2: Portoforlio Margin Mode;  
3: Single-Currency Margin Mode  
enable_tiered_mm | boolean | Optional | none | Whether to enable tiered maintenance margin calculation  
enable_dual_plus | boolean | Optional | none | Whether to Support Split Position Mode  
position_mode | string | Optional | none | Position Holding Mode single - Single Direction Position, dual - Dual Direction Position, dual_plus - Split Position  
history | object | Optional | none | Statistical data  
↳ dnw | string | Optional | none | total amount of deposit and withdraw  
↳ pnl | string | Optional | none | total amount of trading profit and loss  
↳ fee | string | Optional | none | total amount of fee  
↳ refr | string | Optional | none | total amount of referrer rebates  
↳ fund | string | Optional | none | total amount of funding costs  
↳ point_dnw | string | Optional | none | total amount of point deposit and withdraw  
↳ point_fee | string | Optional | none | total amount of point fee  
↳ point_refr | string | Optional | none | total amount of referrer rebates of point fee  
↳ bonus_dnw | string | Optional | none | total amount of perpetual contract bonus transfer  
↳ bonus_offset | string | Optional | none | total amount of perpetual contract bonus deduction  
↳ cross_settle | string | Optional | none | Represents the value of profit settlement from the futures account to the spot account under Unified Account Mode. Negative values indicate settlement from futures to spot, while positive values indicate settlement from spot to futures. This value is cumulative.  
      
    
    {
      "total": "string",
      "unrealised_pnl": "string",
      "position_margin": "string",
      "order_margin": "string",
      "available": "string",
      "point": "string",
      "currency": "string",
      "in_dual_mode": true,
      "enable_credit": true,
      "position_initial_margin": "string",
      "maintenance_margin": "string",
      "bonus": "string",
      "enable_evolved_classic": true,
      "cross_order_margin": "string",
      "cross_initial_margin": "string",
      "cross_maintenance_margin": "string",
      "cross_unrealised_pnl": "string",
      "cross_available": "string",
      "cross_margin_balance": "string",
      "cross_mmr": "string",
      "cross_imr": "string",
      "isolated_position_margin": "string",
      "enable_new_dual_mode": true,
      "margin_mode": 0,
      "enable_tiered_mm": true,
      "enable_dual_plus": true,
      "position_mode": "string",
      "history": {
        "dnw": "string",
        "pnl": "string",
        "fee": "string",
        "refr": "string",
        "fund": "string",
        "point_dnw": "string",
        "point_fee": "string",
        "point_refr": "string",
        "bonus_dnw": "string",
        "bonus_offset": "string",
        "cross_settle": "string"
      }
    }
    
    

##  Contract

_Futures contract details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
name | string | Optional | none | Futures contract  
type | string | Optional | none | Contract type: inverse - inverse contract, direct - direct contract  
quanto_multiplier | string | Optional | none | The contract multiplier indicates how many units of the underlying asset the face value of one contract represents.  
leverage_min | string | Optional | none | Minimum leverage  
leverage_max | string | Optional | none | Maximum leverage  
maintenance_rate | string | Optional | none | The maintenance margin rate of the first tier of risk limit sheet  
mark_type | string | Optional | none | Deprecated  
mark_price | string | Optional | none | Current mark price  
index_price | string | Optional | none | Current index price  
last_price | string | Optional | none | Last trading price  
maker_fee_rate | string | Optional | none | Maker fee rate, negative values indicate rebates  
taker_fee_rate | string | Optional | none | Taker fee rate  
order_price_round | string | Optional | none | Minimum order price increment  
mark_price_round | string | Optional | none | Minimum mark price increment  
funding_rate | string | Optional | none | Current funding rate  
funding_interval | integer | Optional | none | Funding application interval, unit in seconds  
funding_next_apply | number(double) | Optional | none | Next funding time  
risk_limit_base | string | Optional | none | Base risk limit (deprecated)  
interest_rate | string | Optional | none | Interest rate parameter used in funding rate and premium-related calculations for perpetual contracts. Returned as a string decimal ratio (e.g. `0.0003`), same convention as `funding_rate` (ratio, not percent).  
risk_limit_step | string | Optional | none | Risk limit adjustment step (deprecated)  
risk_limit_max | string | Optional | none | Maximum risk limit allowed by the contract (deprecated). It is recommended to use /futures/{settle}/risk_limit_tiers to query risk limits  
order_size_min | string | Optional | none | Minimum order size allowed by the contract  
enable_decimal | boolean | Optional | none | Whether decimal string type is supported for contract lot size. When this field is set to `true`, it indicates that the contract supports decimal lot sizes (i.e., the `size` field can use a decimal string type); when set to `false`, it indicates that the contract does not support decimal lot sizes (i.e., the `size` field can only use an integer type).  
order_size_max | string | Optional | none | Maximum order size allowed by the contract  
order_price_deviate | string | Optional | none | Maximum allowed deviation between order price and current mark price. The order price `order_price` must satisfy the following condition:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | Optional | none | Trading fee discount for referred users  
ref_rebate_rate | string | Optional | none | Commission rate for referrers  
orderbook_id | integer(int64) | Optional | none | Orderbook update ID  
trade_id | integer(int64) | Optional | none | Current trade ID  
trade_size | string | Optional | none | Historical cumulative trading volume  
position_size | string | Optional | none | Current total long position size  
config_change_time | number(double) | Optional | none | Last configuration update time  
in_delisting | boolean | Optional | none | `in_delisting=true` and position_size>0 indicates the contract is in delisting transition period  
`in_delisting=true` and position_size=0 indicates the contract is delisted  
orders_limit | integer | Optional | none | Maximum number of pending orders  
enable_bonus | boolean | Optional | none | Whether bonus is enabled  
enable_credit | boolean | Optional | none | Whether portfolio margin account is enabled  
create_time | number(double) | Optional | none | Created time of the contract  
funding_cap_ratio | string | Optional | none | Deprecated  
status | string | Optional | none | Contract status types include: prelaunch (pre-launch), trading (active), delisting (delisting), delisted (delisted), circuit_breaker (circuit breaker)  
launch_time | integer(int64) | Optional | none | Contract expiry timestamp  
delisting_time | integer(int64) | Optional | none | Timestamp when contract enters reduce-only state  
delisted_time | integer(int64) | Optional | none | Contract delisting time  
market_order_slip_ratio | string | Optional | none | The maximum slippage allowed for market orders, with the slippage rate calculated based on the latest market price  
market_order_size_max | string | Optional | none | The maximum number of contracts supported for market orders, with a default value of 0. When the default value is used, the maximum number of contracts is limited by the `order_size_max` field  
funding_rate_limit | string | Optional | none | Upper and lower limits of funding rate  
contract_type | string | Optional | none | Contract classification type, e.g. stocks, metals, indices, forex, commodities, etc.  
funding_impact_value | string | Optional | none | Funding rate depth impact value  
enable_circuit_breaker | boolean | Optional | none | Whether the newly launched contract activates mark price circuit breaker (If the platform intends to activate this mechanism for a newly launched contract market to prevent significant price fluctuations and excessive liquidations after launch, an advance announcement will be made).  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | inverse  
type | direct  
mark_type | internal  
mark_type | index  
      
    
    {
      "name": "string",
      "type": "inverse",
      "quanto_multiplier": "string",
      "leverage_min": "string",
      "leverage_max": "string",
      "maintenance_rate": "string",
      "mark_type": "internal",
      "mark_price": "string",
      "index_price": "string",
      "last_price": "string",
      "maker_fee_rate": "string",
      "taker_fee_rate": "string",
      "order_price_round": "string",
      "mark_price_round": "string",
      "funding_rate": "string",
      "funding_interval": 0,
      "funding_next_apply": 0,
      "risk_limit_base": "string",
      "interest_rate": "string",
      "risk_limit_step": "string",
      "risk_limit_max": "string",
      "order_size_min": "string",
      "enable_decimal": true,
      "order_size_max": "string",
      "order_price_deviate": "string",
      "ref_discount_rate": "string",
      "ref_rebate_rate": "string",
      "orderbook_id": 0,
      "trade_id": 0,
      "trade_size": "string",
      "position_size": "string",
      "config_change_time": 0,
      "in_delisting": true,
      "orders_limit": 0,
      "enable_bonus": true,
      "enable_credit": true,
      "create_time": 0,
      "funding_cap_ratio": "string",
      "status": "string",
      "launch_time": 0,
      "delisting_time": 0,
      "delisted_time": 0,
      "market_order_slip_ratio": "string",
      "market_order_size_max": "string",
      "funding_rate_limit": "string",
      "contract_type": "string",
      "funding_impact_value": "string",
      "enable_circuit_breaker": true
    }
    
    

##  FuturesLeverage

_Return result includes Lever field_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
Lever | string | Optional | none | leverage  
      
    
    {
      "Lever": "string"
    }
    
    

##  FuturesOrderAmendment

_FuturesOrderAmendment_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
size | string | Optional | none | New order size, including filled part.  
  
\- If new size is less than or equal to filled size, the order will be cancelled.  
\- Order side must be identical to the original one.  
\- Close order size cannot be changed.  
\- For reduce only orders, increasing size may leads to other reduce only orders being cancelled.  
\- If price is not changed, decreasing size will not change its precedence in order book, while increasing will move it to the last at current price.  
price | string | Optional | none | New order price  
amend_text | string | Optional | none | Custom info during order amendment  
text | string | Optional | none | Internal users can modify information in the text field.  
action_mode | string | Optional | none | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
      
    
    {
      "size": "string",
      "price": "string",
      "amend_text": "string",
      "text": "string",
      "action_mode": "string"
    }
    
    

##  FuturesAccountBook

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | number(double) | Optional | none | Change time  
change | string | Optional | none | Change amount  
balance | string | Optional | none | Balance after change  
type | string | Optional | none | Change types:  
  
\- dnw: Deposit and withdrawal  
\- pnl: Profit and loss from position reduction  
\- fee: Trading fees  
\- refr: Referrer rebates  
\- fund: Funding fees  
\- point_dnw: Point card deposit and withdrawal  
\- point_fee: Point card trading fees  
\- point_refr: Point card referrer rebates  
\- bonus_offset: Trial fund deduction  
text | string | Optional | none | Comment  
contract | string | Optional | none | Futures contract, the field is only available for data after 2023-10-30  
trade_id | string | Optional | none | trade id  
id | string | Optional | none | Account change record ID  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | dnw  
type | pnl  
type | fee  
type | refr  
type | fund  
type | point_dnw  
type | point_fee  
type | point_refr  
type | bonus_offset  
      
    
    {
      "time": 0,
      "change": "string",
      "balance": "string",
      "type": "dnw",
      "text": "string",
      "contract": "string",
      "trade_id": "string",
      "id": "string"
    }
    
    

##  FuturesOrder

_Futures order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | read-only | Futures order ID  
user | integer | Optional | read-only | User ID  
create_time | number(double) | Optional | read-only | Creation time of order  
update_time | number(double) | Optional | read-only | OrderUpdateTime  
finish_time | number(double) | Optional | read-only | Order finished time. Not returned if order is open  
finish_as | string | Optional | read-only | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | read-only | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required | none | Futures contract  
size | string | Required | none | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | string | Optional | none | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Required | none | Required. Order Price; a price of 0 with `tif` as `ioc` represents a market order.  
close | boolean | Optional | write-only | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | read-only | Is the order to close position  
reduce_only | boolean | Optional | write-only | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | read-only | Is the order reduce-only  
is_liq | boolean | Optional | read-only | Is the order for liquidation  
tif | string | Optional | none | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | string | Optional | read-only | Unfilled quantity  
fill_price | string | Optional | read-only | Fill price  
text | string | Optional | none | Custom order information. If not empty, must follow the rules below:  
  
1\. Prefixed with `t-`  
2\. No longer than 28 bytes without `t-` prefix  
3\. Can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
In addition to user-defined information, the following are internal reserved fields that identify the order source:  
  
\- web: Web  
\- api: API call  
\- app: Mobile app  
\- auto_deleveraging: Automatic deleveraging  
\- liquidation: Forced liquidation of positions under the old classic mode  
\- liq-xxx: a. Forced liquidation of positions under the new classic mode, including isolated margin, one-way cross margin, and non-hedged positions under two-way cross margin. b. Forced liquidation of isolated positions under the unified account single-currency margin mode  
\- hedge-liq-xxx: Forced liquidation of hedged positions under the new classic mode two-way cross margin, i.e., simultaneously closing long and short positions  
\- pm_liquidate: Forced liquidation under unified account multi-currency margin mode  
\- comb_margin_liquidate: Forced liquidation under unified account portfolio margin mode  
\- scm_liquidate: Forced liquidation of positions under unified account single-currency margin mode  
\- insurance: Insurance  
\- clear: Contract delisting withdrawal  
tkfr | string | Optional | read-only | Taker fee  
mkfr | string | Optional | read-only | Maker fee  
refu | integer | Optional | read-only | Referrer user ID  
auto_size | string | Optional | write-only | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | read-only | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | none | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | read-only | The custom data that the user remarked when amending the order  
pid | integer(int64) | Optional | write-only | Position ID  
market_order_slip_ratio | string | Optional | none | Custom maximum slippage rate for market orders. If not provided, the default contract settings will be used  
pos_margin_mode | string | Optional | none | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin, only passed in simple split position mode  
action_mode | string | Optional | none | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
tpsl_tp_trigger_price | string | Optional | none | Take profit price  
tpsl_sl_trigger_price | string | Optional | none | Stop loss price  
  
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
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
auto_size | close_long  
auto_size | close_short  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
      
    
    {
      "id": 0,
      "user": 0,
      "create_time": 0,
      "update_time": 0,
      "finish_time": 0,
      "finish_as": "filled",
      "status": "open",
      "contract": "string",
      "size": "string",
      "iceberg": "string",
      "price": "string",
      "close": false,
      "is_close": true,
      "reduce_only": false,
      "is_reduce_only": true,
      "is_liq": true,
      "tif": "gtc",
      "left": "string",
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "auto_size": "close_long",
      "stp_id": 0,
      "stp_act": "co",
      "amend_text": "string",
      "pid": 0,
      "market_order_slip_ratio": "string",
      "pos_margin_mode": "string",
      "action_mode": "string",
      "tpsl_tp_trigger_price": "string",
      "tpsl_sl_trigger_price": "string"
    }
    
    

##  CountdownCancelAllFuturesTask

_CountdownCancelAllFuturesTask_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timeout | integer(int32) | Required | none | Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown  
contract | string | Optional | none | Futures contract  
      
    
    {
      "timeout": 0,
      "contract": "string"
    }
    
    

##  MyFuturesTradeTimeRange

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
trade_id | string | Optional | none | Fill ID  
create_time | number(double) | Optional | none | Fill Time  
contract | string | Optional | none | Futures contract  
order_id | string | Optional | none | Related order ID  
size | string | Optional | none | Trading size  
close_size | string | Optional | none | Number of closed positions:  
  
close_size=0 && size＞0 Open long position  
close_size=0 && size＜0 Open short position  
close_size>0 && size>0 && size <= close_size Close short position  
close_size>0 && size>0 && size > close_size Close short position and open long position  
close_size<0 && size<0 && size >= close_size Close long position  
close_size<0 && size<0 && size < close_size Close long position and open short position  
price | string | Optional | none | Fill Price  
role | string | Optional | none | Trade role. taker - taker, maker - maker  
text | string | Optional | none | Order custom information  
fee | string | Optional | none | Trade fee  
point_fee | string | Optional | none | Points used to deduct trade fee  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
role | taker  
role | maker  
      
    
    {
      "trade_id": "string",
      "create_time": 0,
      "contract": "string",
      "order_id": "string",
      "size": "string",
      "close_size": "string",
      "price": "string",
      "role": "taker",
      "text": "string",
      "fee": "string",
      "point_fee": "string"
    }
    
    

##  CreateTrailOrderResponse

_CreateTrailOrderResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Optional | none | Status code, 0 means success  
message | string | Optional | none | Response message  
data | object | Optional | none | none  
↳ id | string | Optional | none | Order ID  
timestamp | integer(int64) | Optional | none | Response timestamp (milliseconds)  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "id": "string"
      },
      "timestamp": 0
    }
    
    

##  FuturesFee

_The returned result is a map type, where the key represents the market and taker and maker fee rates_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
taker_fee | string | Optional | read-only | Taker fee  
maker_fee | string | Optional | read-only | maker fee  
      
    
    {
      "taker_fee": "string",
      "maker_fee": "string"
    }
    
    

##  CreateTrailOrder

_CreateTrailOrder_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contract | string | Required | none | Contract name  
amount | string | Required | none | Trading quantity in contracts, positive for buy, negative for sell  
activation_price | string | Optional | none | Activation price, 0 means trigger immediately  
is_gte | boolean | Optional | none | true: activate when market price >= activation price, false: <= activation price  
price_type | integer(int32) | Optional | none | Activation price type: 1-latest price, 2-index price, 3-mark price  
price_offset | string | Optional | none | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
reduce_only | boolean | Optional | none | Whether reduce only  
position_related | boolean | Optional | none | Whether bound to a position (if position_related = true (position-related), then reduce_only must also be true)  
text | string | Optional | none | Order custom information, optional field. Used to identify the order source or set a user-defined ID.  
  
If non-empty, it must meet one of the following rules:  
  
1\. Internal Reserved Fields (identifying order source):  
\- `apiv4`: API call  
2\. User-defined Fields (setting custom ID):  
\- Must start with `t-`  
\- The content after `t-` must not exceed 28 bytes in length  
\- Can only contain: numbers, letters, underscores (_), hyphens (-), or dots (.)  
\- Examples: `t-my-order-001`, `t-trail_2024.01`  
  
Note: User-defined fields must not conflict with internal reserved fields.  
pos_margin_mode | string | Optional | none | Position margin mode: isolated/cross  
position_mode | string | Optional | none | Position mode: single, dual, and dual_plus  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 1  
price_type | 2  
price_type | 3  
      
    
    {
      "contract": "string",
      "amount": "string",
      "activation_price": "0",
      "is_gte": true,
      "price_type": 1,
      "price_offset": "string",
      "reduce_only": false,
      "position_related": false,
      "text": "apiv4",
      "pos_margin_mode": "string",
      "position_mode": "string"
    }
    
    

##  StopChaseOrderReq

_Request body for stopping a chase order_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | none | Order ID. Either id or text must be provided  
text | string | Optional | none | Custom text. Required only when id is 0 or omitted  
settle | string | Optional | none | Overridden by the path parameter  
      
    
    {
      "id": "string",
      "text": "string",
      "settle": "string"
    }
    
    

##  FuturesLiqOrder

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | integer(int64) | Optional | read-only | Liquidation time  
contract | string | Optional | read-only | Futures contract  
size | string | Optional | read-only | User position size  
order_size | string | Optional | read-only | Number of forced liquidation orders  
order_price | string | Optional | read-only | Liquidation order price  
fill_price | string | Optional | read-only | Liquidation order average taker price  
left | string | Optional | read-only | System liquidation order maker size  
      
    
    {
      "time": 0,
      "contract": "string",
      "size": "string",
      "order_size": "string",
      "order_price": "string",
      "fill_price": "string",
      "left": "string"
    }
    
    

##  ChaseOrder

_Chase order detail or list item_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | none | none  
user | string | Optional | none | none  
contract | string | Optional | none | none  
settle | string | Optional | none | none  
amount | string | Optional | none | Total size in contracts; positive for buy, negative for sell  
price_limit | string | Optional | none | none  
reduce_only | boolean | Optional | none | none  
text | string | Optional | none | none  
create_time | integer(int64) | Optional | none | none  
finish_time | integer(int64) | Optional | none | none  
original_status | integer | Optional | none | Raw status enum  
status | string | Optional | none | Simplified status, e.g. open / finished  
reason | string | Optional | none | none  
fill_amount | string | Optional | none | none  
average_fill_price | string | Optional | none | none  
suborder_id | string | Optional | none | none  
is_dual_mode | boolean | Optional | none | none  
side_label | string | Optional | none | none  
position_side_output | string | Optional | none | none  
chase_price | string | Optional | none | none  
interval_sec | integer(uint32) | Optional | none | none  
updated_at | integer(int64) | Optional | none | none  
suborder_price | string | Optional | none | none  
suborder_ongoing | boolean | Optional | none | none  
suborder_finish_as | string | Optional | none | none  
price_type | integer | Optional | none | PriceType enum: 1 latest, 2 index, 3 mark  
price_gap_type | string | Optional | none | none  
price_gap_value | string | Optional | none | none  
status_code | string | Optional | none | none  
create_time_precise | string | Optional | none | Creation time (seconds.microseconds)  
finish_time_precise | string | Optional | none | none  
pos_margin_mode | string | Optional | none | none  
position_mode | string | Optional | none | none  
leverage | string | Optional | none | none  
error_label | string | Optional | none | none  
      
    
    {
      "id": "string",
      "user": "string",
      "contract": "string",
      "settle": "string",
      "amount": "string",
      "price_limit": "string",
      "reduce_only": true,
      "text": "string",
      "create_time": 0,
      "finish_time": 0,
      "original_status": 0,
      "status": "string",
      "reason": "string",
      "fill_amount": "string",
      "average_fill_price": "string",
      "suborder_id": "string",
      "is_dual_mode": true,
      "side_label": "string",
      "position_side_output": "string",
      "chase_price": "string",
      "interval_sec": 0,
      "updated_at": 0,
      "suborder_price": "string",
      "suborder_ongoing": true,
      "suborder_finish_as": "string",
      "price_type": 0,
      "price_gap_type": "string",
      "price_gap_value": "string",
      "status_code": "string",
      "create_time_precise": "string",
      "finish_time_precise": "string",
      "pos_margin_mode": "string",
      "position_mode": "string",
      "leverage": "string",
      "error_label": "string"
    }
    
    

##  CreateChaseOrderResp

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | none | ID of the newly created order  
      
    
    {
      "id": "string"
    }
    
    

##  InsuranceRecord

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
t | integer(int64) | Optional | none | Unix timestamp in seconds  
b | string | Optional | none | Insurance balance  
      
    
    {
      "t": 0,
      "b": "string"
    }
    
    

##  Position

_Futures position details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user | integer(int64) | Optional | read-only | User ID  
contract | string | Optional | read-only | Futures contract  
size | string | Optional | read-only | Position size  
leverage | string | Optional | none | leverage for isolated margin. 0 means cross margin. For leverage of cross margin, please refer to `cross_leverage_limit`.  
risk_limit | string | Optional | none | Position risk limit  
leverage_max | string | Optional | read-only | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage  
maintenance_rate | string | Optional | read-only | The maintenance margin requirement for the risk limit at which the current position size is located.Since the maintenance margin for the position has been calculated using a tiered system, the actual maintenance margin rate required for this position is based on `average_maintenance_rate`.  
value | string | Optional | read-only | Position value calculated in settlement currency  
margin | string | Optional | none | Position margin  
entry_price | string | Optional | read-only | Entry price  
liq_price | string | Optional | read-only | Estimated liquidation price, for reference only. The actual liquidation trigger is based on the position mmr or the account maintenance margin level.  
mark_price | string | Optional | read-only | Current mark price  
initial_margin | string | Optional | read-only | Initial margin of postions  
maintenance_margin | string | Optional | read-only | Maintencance margin of postions  
unrealised_pnl | string | Optional | read-only | Unrealized PNL  
realised_pnl | string | Optional | read-only | Realised PnL, the sum of all cash flows generated by this position, including settlement of closing positions, settlement of funding fees, and transaction fee expenses.  
pnl_pnl | string | Optional | read-only | settled pnl when closing postion  
pnl_fund | string | Optional | read-only | funding fees  
pnl_fee | string | Optional | read-only | trading fees  
history_pnl | string | Optional | read-only | Total realized PnL from closed positions  
last_close_pnl | string | Optional | read-only | PNL of last position close  
realised_point | string | Optional | read-only | Realized POINT PNL  
history_point | string | Optional | read-only | History realized POINT PNL  
adl_ranking | integer | Optional | read-only | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
pending_orders | integer | Optional | read-only | Current pending order quantity  
close_order | object|null | Optional | read-only | Current close order information, or `null` if no close order  
↳ id | integer(int64) | Optional | none | Order ID  
↳ price | string | Optional | none | Order price  
↳ is_liq | boolean | Optional | none | Whether the close order is from liquidation  
mode | string | Optional | none | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
cross_leverage_limit | string | Optional | none | leverage for cross margin  
update_time | integer(int64) | Optional | read-only | Last update time  
update_id | integer(int64) | Optional | read-only | Update ID. The value increments by 1 each time the position is updated  
open_time | integer(int64) | Optional | none | First Open Time  
risk_limit_table | string | Optional | read-only | Risk limit table ID  
average_maintenance_rate | string | Optional | read-only | Average maintenance margin rate  
pid | integer(int64) | Optional | read-only | Sub-account position ID  
pos_margin_mode | string | Optional | none | Position Margin Mode isolated - Isolated Margin, cross - Cross Margin  
lever | string | Optional | none | Indicates the current leverage of the position, applicable to both isolated and cross margin, gradually replacing the current leverage and cross_leverage_limit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
      
    
    {
      "user": 0,
      "contract": "string",
      "size": "string",
      "leverage": "string",
      "risk_limit": "string",
      "leverage_max": "string",
      "maintenance_rate": "string",
      "value": "string",
      "margin": "string",
      "entry_price": "string",
      "liq_price": "string",
      "mark_price": "string",
      "initial_margin": "string",
      "maintenance_margin": "string",
      "unrealised_pnl": "string",
      "realised_pnl": "string",
      "pnl_pnl": "string",
      "pnl_fund": "string",
      "pnl_fee": "string",
      "history_pnl": "string",
      "last_close_pnl": "string",
      "realised_point": "string",
      "history_point": "string",
      "adl_ranking": 0,
      "pending_orders": 0,
      "close_order": {
        "id": 0,
        "price": "string",
        "is_liq": true
      },
      "mode": "single",
      "cross_leverage_limit": "string",
      "update_time": 0,
      "update_id": 0,
      "open_time": 0,
      "risk_limit_table": "string",
      "average_maintenance_rate": "string",
      "pid": 0,
      "pos_margin_mode": "string",
      "lever": "string"
    }
    
    

##  StopAllTrailOrders

_StopAllTrailOrders_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
contract | string | Optional | none | Contract name  
related_position | integer(int32) | Optional | none | Associated position, if provided, only cancel orders associated with this position, 1-long, 2-short  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
related_position | 1  
related_position | 2  
      
    
    {
      "contract": "string",
      "related_position": 1
    }
    
    

##  TrailOrderChangeLogResponse

_TrailOrderChangeLogResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
change_log | [TrailChangeLog] | Optional | none | [Trail order modification records]  
      
    
    {
      "change_log": [
        {
          "updated_at": 0,
          "amount": "string",
          "is_gte": true,
          "activation_price": "string",
          "price_type": 0,
          "price_offset": "string",
          "is_create": true
        }
      ]
    }
    
    

##  FuturesPriceTriggeredOrder

_Futures price-triggered order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
initial | object | Required | none | none  
↳ contract | string | Required | none | Futures contract  
↳ size | integer(int64) | Optional | none | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
↳ amount | string | Optional | none | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
↳ price | string | Required | none | Order price. Set to 0 to use market price  
↳ close | boolean | Optional | write-only | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
↳ tif | string | Optional | none | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
↳ text | string | Optional | none | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
↳ reduce_only | boolean | Optional | none | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
↳ auto_size | string | Optional | write-only | One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required  
↳ is_reduce_only | boolean | Optional | read-only | Is the order reduce-only  
↳ is_close | boolean | Optional | read-only | Is the order to close position  
trigger | object | Required | none | none  
↳ strategy_type | integer(int32) | Optional | none | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
↳ price_type | integer(int32) | Optional | none | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
↳ price | string | Required | none | Price value for price trigger, or spread value for spread trigger  
↳ rule | integer(int32) | Required | none | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
↳ expiration | integer | Optional | none | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
id | integer(int64) | Optional | read-only | Auto order ID  
id_string | string | Optional | read-only | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
user | integer | Optional | read-only | User ID  
create_time | number(double) | Optional | read-only | Created time  
finish_time | number(double) | Optional | read-only | End time  
trade_id | integer(int64) | Optional | read-only | ID of the order created after trigger  
status | string | Optional | read-only | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
finish_as | string | Optional | read-only | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
reason | string | Optional | read-only | Additional description of how the order was completed  
order_type | string | Optional | none | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
me_order_id | integer(int64) | Optional | read-only | Corresponding order ID for order take-profit/stop-loss orders  
pos_margin_mode | string | Optional | none | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
      
    
    {
      "initial": {
        "contract": "string",
        "size": 0,
        "amount": "string",
        "price": "string",
        "close": false,
        "tif": "gtc",
        "text": "string",
        "reduce_only": false,
        "auto_size": "string",
        "is_reduce_only": true,
        "is_close": true
      },
      "trigger": {
        "strategy_type": 0,
        "price_type": 0,
        "price": "string",
        "rule": 1,
        "expiration": 0
      },
      "id": 0,
      "id_string": "string",
      "user": 0,
      "create_time": 0,
      "finish_time": 0,
      "trade_id": 0,
      "status": "open",
      "finish_as": "cancelled",
      "reason": "string",
      "order_type": "string",
      "me_order_id": 0,
      "pos_margin_mode": "isolated"
    }
    
    

##  MyFuturesTrade

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Fill ID  
create_time | number(double) | Optional | none | Fill Time  
contract | string | Optional | none | Futures contract  
order_id | string | Optional | none | Related order ID  
size | string | Optional | none | Trading size  
close_size | string | Optional | none | Number of closed positions:  
  
close_size=0 && size＞0 Open long position  
close_size=0 && size＜0 Open short position  
close_size>0 && size>0 && size <= close_size Close short position  
close_size>0 && size>0 && size > close_size Close short position and open long position  
close_size<0 && size<0 && size >= close_size Close long position  
close_size<0 && size<0 && size < close_size Close long position and open short position  
price | string | Optional | none | Fill Price  
role | string | Optional | none | Trade role. taker - taker, maker - maker  
text | string | Optional | none | Order custom information  
fee | string | Optional | none | Trade fee  
point_fee | string | Optional | none | Points used to deduct trade fee  
trade_value | string | Optional | none | trade value  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
role | taker  
role | maker  
      
    
    {
      "id": 0,
      "create_time": 0,
      "contract": "string",
      "order_id": "string",
      "size": "string",
      "close_size": "string",
      "price": "string",
      "role": "taker",
      "text": "string",
      "fee": "string",
      "point_fee": "string",
      "trade_value": "string"
    }
    
    

##  TrailChangeLog

_Trail order modification records_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
updated_at | integer(int64) | Optional | read-only | Update time  
amount | string | Optional | read-only | Trading quantity in contracts, positive for buy, negative for sell  
is_gte | boolean | Optional | read-only | true: activate when market price >= activation price, false: <= activation price  
activation_price | string | Optional | read-only | Activation price, 0 means trigger immediately  
price_type | integer(int32) | Optional | read-only | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price  
price_offset | string | Optional | read-only | Callback ratio or price distance, e.g., `0.1` or `0.1%`  
is_create | boolean | Optional | read-only | true - order creation, false - order modification  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
      
    
    {
      "updated_at": 0,
      "amount": "string",
      "is_gte": true,
      "activation_price": "string",
      "price_type": 0,
      "price_offset": "string",
      "is_create": true
    }