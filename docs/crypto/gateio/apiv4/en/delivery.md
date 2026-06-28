---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/delivery
api_type: Trading
updated_at: 2026-05-27 20:14:56.257900
---

# Delivery

Delivery contract

##  Query all futures contracts

GET`/delivery/{settle}/contracts`

GET `/delivery/{settle}/contracts`

_Query all futures contracts_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryContract]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures contract details]  
» _None_ | DeliveryContract | Futures contract details  
»» name | string | Futures contract  
»» underlying | string | Underlying  
»» cycle | string | Cycle type, e.g. WEEKLY, QUARTERLY  
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
»» basis_rate | string | Fair basis rate  
»» basis_value | string | Fair basis value  
»» basis_impact_value | string | Funding used for calculating impact bid, ask price  
»» settle_price | string | Settle price  
»» settle_price_interval | integer | Settle price update interval  
»» settle_price_duration | integer | Settle price update duration in seconds  
»» expire_time | integer(int64) | Contract expiry timestamp  
»» risk_limit_base | string | Risk limit base  
»» risk_limit_step | string | Step of adjusting risk limit  
»» risk_limit_max | string | Maximum risk limit the contract allowed  
»» order_size_min | integer(int64) | Minimum order size allowed by the contract  
»» order_size_max | integer(int64) | Maximum order size allowed by the contract  
»» order_price_deviate | string | Maximum allowed deviation between order price and current mark price. The order price `order_price` must satisfy the following condition:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
»» ref_discount_rate | string | Trading fee discount for referred users  
»» ref_rebate_rate | string | Commission rate for referrers  
»» orderbook_id | integer(int64) | Orderbook update ID  
»» trade_id | integer(int64) | Current trade ID  
»» trade_size | integer(int64) | Historical cumulative trading volume  
»» position_size | integer(int64) | Current total long position size  
»» config_change_time | number(double) | Last configuration update time  
»» in_delisting | boolean | Contract is delisting  
»» orders_limit | integer | Maximum number of pending orders  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
cycle | WEEKLY  
cycle | BI-WEEKLY  
cycle | QUARTERLY  
cycle | BI-QUARTERLY  
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
    
    url = '/delivery/usdt/contracts'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/contracts \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "name": "BTC_USDT_20200814",
        "underlying": "BTC_USDT",
        "cycle": "WEEKLY",
        "type": "direct",
        "quanto_multiplier": "0.0001",
        "mark_type": "index",
        "last_price": "9017",
        "mark_price": "9019",
        "index_price": "9005.3",
        "basis_rate": "0.185095",
        "basis_value": "13.7",
        "basis_impact_value": "100000",
        "settle_price": "0",
        "settle_price_interval": 60,
        "settle_price_duration": 1800,
        "settle_fee_rate": "0.0015",
        "expire_time": 1593763200,
        "order_price_round": "0.1",
        "mark_price_round": "0.1",
        "leverage_min": "1",
        "leverage_max": "100",
        "maintenance_rate": "1000000",
        "risk_limit_base": "140.726652109199",
        "risk_limit_step": "1000000",
        "risk_limit_max": "8000000",
        "maker_fee_rate": "-0.00025",
        "taker_fee_rate": "0.00075",
        "ref_discount_rate": "0",
        "ref_rebate_rate": "0.2",
        "order_price_deviate": "0.5",
        "order_size_min": 1,
        "order_size_max": 1000000,
        "orders_limit": 50,
        "orderbook_id": 63,
        "trade_id": 26,
        "trade_size": 435,
        "position_size": 130,
        "config_change_time": 1593158867,
        "in_delisting": false
      }
    ]
    

##  Query single contract information

GET`/delivery/{settle}/contracts/{contract}`

GET `/delivery/{settle}/contracts/{contract}`

_Query single contract information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Contract information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Contract information | DeliveryContract  
  
### Response Schema

Status Code **200**

_Futures contract details_

Name | Type | Description  
---|---|---  
» name | string | Futures contract  
» underlying | string | Underlying  
» cycle | string | Cycle type, e.g. WEEKLY, QUARTERLY  
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
» basis_rate | string | Fair basis rate  
» basis_value | string | Fair basis value  
» basis_impact_value | string | Funding used for calculating impact bid, ask price  
» settle_price | string | Settle price  
» settle_price_interval | integer | Settle price update interval  
» settle_price_duration | integer | Settle price update duration in seconds  
» expire_time | integer(int64) | Contract expiry timestamp  
» risk_limit_base | string | Risk limit base  
» risk_limit_step | string | Step of adjusting risk limit  
» risk_limit_max | string | Maximum risk limit the contract allowed  
» order_size_min | integer(int64) | Minimum order size allowed by the contract  
» order_size_max | integer(int64) | Maximum order size allowed by the contract  
» order_price_deviate | string | Maximum allowed deviation between order price and current mark price. The order price `order_price` must satisfy the following condition:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
» ref_discount_rate | string | Trading fee discount for referred users  
» ref_rebate_rate | string | Commission rate for referrers  
» orderbook_id | integer(int64) | Orderbook update ID  
» trade_id | integer(int64) | Current trade ID  
» trade_size | integer(int64) | Historical cumulative trading volume  
» position_size | integer(int64) | Current total long position size  
» config_change_time | number(double) | Last configuration update time  
» in_delisting | boolean | Contract is delisting  
» orders_limit | integer | Maximum number of pending orders  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
cycle | WEEKLY  
cycle | BI-WEEKLY  
cycle | QUARTERLY  
cycle | BI-QUARTERLY  
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
    
    url = '/delivery/usdt/contracts/BTC_USDT_20200814'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/contracts/BTC_USDT_20200814 \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "name": "BTC_USDT_20200814",
      "underlying": "BTC_USDT",
      "cycle": "WEEKLY",
      "type": "direct",
      "quanto_multiplier": "0.0001",
      "mark_type": "index",
      "last_price": "9017",
      "mark_price": "9019",
      "index_price": "9005.3",
      "basis_rate": "0.185095",
      "basis_value": "13.7",
      "basis_impact_value": "100000",
      "settle_price": "0",
      "settle_price_interval": 60,
      "settle_price_duration": 1800,
      "settle_fee_rate": "0.0015",
      "expire_time": 1593763200,
      "order_price_round": "0.1",
      "mark_price_round": "0.1",
      "leverage_min": "1",
      "leverage_max": "100",
      "maintenance_rate": "1000000",
      "risk_limit_base": "140.726652109199",
      "risk_limit_step": "1000000",
      "risk_limit_max": "8000000",
      "maker_fee_rate": "-0.00025",
      "taker_fee_rate": "0.00075",
      "ref_discount_rate": "0",
      "ref_rebate_rate": "0.2",
      "order_price_deviate": "0.5",
      "order_size_min": 1,
      "order_size_max": 1000000,
      "orders_limit": 50,
      "orderbook_id": 63,
      "trade_id": 26,
      "trade_size": 435,
      "position_size": 130,
      "config_change_time": 1593158867,
      "in_delisting": false
    }
    

##  Query futures market depth information

GET`/delivery/{settle}/order_book`

GET `/delivery/{settle}/order_book`

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
settle | usdt  
interval | 0  
interval | 0.1  
interval | 0.01  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Depth query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Depth query successful | DeliveryOrderBook  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» id | integer(int64) | Order Book ID. Increases by 1 on every order book change. Set `with_id=true` to include this field in response  
» current | number(double) | Response data generation timestamp  
» update | number(double) | Order book changed timestamp  
» asks | array | Ask Depth  
»» DeliveryOrderBookItem | object | none  
»»» p | string | Price (quote currency)  
»»» s | integer(int64) | Size  
»» bids | array | Bid Depth  
»»» DeliveryOrderBookItem | object | none  
»»»» p | string | Price (quote currency)  
»»»» s | integer(int64) | Size  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/order_book'
    query_param = 'contract=BTC_USDT_20200814'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/order_book?contract=BTC_USDT_20200814 \
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
    

##  Futures market transaction records

GET`/delivery/{settle}/trades`

GET `/delivery/{settle}/trades`

_Futures market transaction records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Required | Futures contract  
limit | query | integer | Optional | Maximum number of records returned in a single list  
last_id | query | string | Optional | Use the ID of the last record in the previous list as the starting point for the next list.This field is no longer supported. For new requests, please use the fromand tofields to specify the time rang  
from | query | integer(int64) | Optional | Specify starting time in Unix seconds. If not specified, `to` and `limit` will be used to limit response items.  
If items between `from` and `to` are more than `limit`, only `limit` number will be returned.  
  
to | query | integer(int64) | Optional | Specify end time in Unix seconds, default to current time.  
  
####  Detailed descriptions

**from** : Specify starting time in Unix seconds. If not specified, `to` and `limit` will be used to limit response items.  
If items between `from` and `to` are more than `limit`, only `limit` number will be returned.  

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryTrade]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int64) | Fill ID  
» create_time | number(double) | Fill Time  
» create_time_ms | number(double) | Trade time, with millisecond precision to 3 decimal places  
» contract | string | Futures contract  
» size | integer(int64) | Trading size  
» price | string | Trade price (quote currency)  
» is_internal | boolean | Deprecated  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/trades'
    query_param = 'contract=BTC_USDT_20200814'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/trades?contract=BTC_USDT_20200814 \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": 121234231,
        "create_time": 1514764800,
        "contract": "BTC_USDT",
        "size": -100,
        "price": "100.123"
      }
    ]
    

##  Futures market K-line chart

GET`/delivery/{settle}/candlesticks`

GET `/delivery/{settle}/candlesticks`

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
interval | query | string | Optional | Time interval between data points, note that 1w represents a natural week, 7d time is aligned with Unix initial time  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
interval | 10s  
interval | 30s  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
interval | 2h  
interval | 4h  
interval | 6h  
interval | 8h  
interval | 12h  
interval | 1d  
interval | 7d  
interval | 1w  
interval | 30d  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [DeliveryCandlestick]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [data point in every timestamp]  
» _None_ | DeliveryCandlestick | data point in every timestamp  
»» t | number(double) | Unix timestamp in seconds  
»» v | integer(int64) | size volume (contract size). Only returned if `contract` is not prefixed  
»» c | string | Close price (quote currency)  
»» h | string | Highest price (quote currency)  
»» l | string | Lowest price (quote currency)  
»» o | string | Open price (quote currency)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/candlesticks'
    query_param = 'contract=BTC_USDT_20200814'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/candlesticks?contract=BTC_USDT_20200814 \
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
    

##  Get all futures trading statistics

GET`/delivery/{settle}/tickers`

GET `/delivery/{settle}/tickers`

Get `all futures trading statistics`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [DeliveryTicker]  
  
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
» basis_rate | string | Basis rate  
» basis_value | string | Basis value  
» lowest_ask | string | Recent lowest ask  
» lowest_size | string | The latest seller's lowest price order quantity  
» highest_bid | string | Recent highest bid  
» highest_size | string | The latest buyer's highest price order volume  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/tickers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/tickers \
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
    

##  Futures market insurance fund history

GET`/delivery/{settle}/insurance`

GET `/delivery/{settle}/insurance`

_Futures market insurance fund history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
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
    
    url = '/delivery/usdt/insurance'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/insurance \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "t": 1543968000,
        "b": "83.0031"
      }
    ]
    

##  Get futures account🔒 Authenticated

GET`/delivery/{settle}/accounts`

GET `/delivery/{settle}/accounts`

Get `futures account`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | DeliveryAccount  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» total | string | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
» unrealised_pnl | string | Unrealized PNL  
» position_margin | string | Deprecated  
» order_margin | string | initial margin of all open orders  
» available | string | Available amount for transfer or trading, which includes credit limits under the unified account (includes experience funds; experience funds cannot be transferred, so when transferring, the transfer amount must deduct experience funds)  
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
    
    url = '/delivery/usdt/accounts'
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
    url="/delivery/usdt/accounts"
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
      "enable_tiered_mm": true
    }
    

##  Query futures account change history🔒 Authenticated

GET`/delivery/{settle}/account_book`

GET `/delivery/{settle}/account_book`

_Query futures account change history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
limit | query | integer | Optional | Maximum number of records returned in a single list  
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

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
type | dnw  
type | pnl  
type | fee  
type | refr  
type | fund  
type | point_dnw  
type | point_fee  
type | point_refr  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryAccountBook]  
  
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
    
    url = '/delivery/usdt/account_book'
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
    url="/delivery/usdt/account_book"
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

GET`/delivery/{settle}/positions`

GET `/delivery/{settle}/positions`

Get `user position list`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryPosition]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures position details]  
» _None_ | DeliveryPosition | Futures position details  
»» user | integer(int64) | User ID  
»» contract | string | Futures contract  
»» size | integer(int64) | Position size  
»» leverage | string | Position leverage. 0 means cross margin; positive number means isolated margin  
»» risk_limit | string | Position risk limit  
»» leverage_max | string | Maximum leverage under current risk limit  
»» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
»» value | string | Position value calculated in settlement currency  
»» margin | string | Position margin  
»» entry_price | string | Entry price  
»» liq_price | string | Liquidation price  
»» mark_price | string | Current mark price  
»» initial_margin | string | The initial margin occupied by the position, applicable to the portfolio margin account  
»» maintenance_margin | string | Maintenance margin required for the position, applicable to portfolio margin account  
»» unrealised_pnl | string | Unrealized PNL  
»» realised_pnl | string | Realized PnL  
»» pnl_pnl | string | Realized PNL - Position P/L  
»» pnl_fund | string | Realized PNL - Funding Fees  
»» pnl_fee | string | Realized PNL - Transaction Fees  
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
»» cross_leverage_limit | string | Cross margin leverage (valid only when `leverage` is 0)  
»» update_time | integer(int64) | Last update time  
»» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
»» open_time | integer(int64) | First Open Time  
»» risk_limit_table | string | Risk limit table ID  
»» average_maintenance_rate | string | Average maintenance margin rate  
  
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
    
    url = '/delivery/usdt/positions'
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
    url="/delivery/usdt/positions"
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
        "size": -9440,
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
        "average_maintenance_rate": "0.005"
      }
    ]
    

##  Get single position information🔒 Authenticated

GET`/delivery/{settle}/positions/{contract}`

GET `/delivery/{settle}/positions/{contract}`

Get `single position information`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | DeliveryPosition  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | integer(int64) | Position size  
» leverage | string | Position leverage. 0 means cross margin; positive number means isolated margin  
» risk_limit | string | Position risk limit  
» leverage_max | string | Maximum leverage under current risk limit  
» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Liquidation price  
» mark_price | string | Current mark price  
» initial_margin | string | The initial margin occupied by the position, applicable to the portfolio margin account  
» maintenance_margin | string | Maintenance margin required for the position, applicable to portfolio margin account  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realized PnL  
» pnl_pnl | string | Realized PNL - Position P/L  
» pnl_fund | string | Realized PNL - Funding Fees  
» pnl_fee | string | Realized PNL - Transaction Fees  
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
» cross_leverage_limit | string | Cross margin leverage (valid only when `leverage` is 0)  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
  
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
    
    url = '/delivery/usdt/positions/BTC_USDT_20200814'
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
    url="/delivery/usdt/positions/BTC_USDT_20200814"
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
      "size": -9440,
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
      "average_maintenance_rate": "0.005"
    }
    

##  Update position margin🔒 Authenticated

POST`/delivery/{settle}/positions/{contract}/margin`

POST `/delivery/{settle}/positions/{contract}/margin`

_Update position margin_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
change | query | string | Required | Margin change amount, positive number increases, negative number decreases  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | DeliveryPosition  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | integer(int64) | Position size  
» leverage | string | Position leverage. 0 means cross margin; positive number means isolated margin  
» risk_limit | string | Position risk limit  
» leverage_max | string | Maximum leverage under current risk limit  
» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Liquidation price  
» mark_price | string | Current mark price  
» initial_margin | string | The initial margin occupied by the position, applicable to the portfolio margin account  
» maintenance_margin | string | Maintenance margin required for the position, applicable to portfolio margin account  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realized PnL  
» pnl_pnl | string | Realized PNL - Position P/L  
» pnl_fund | string | Realized PNL - Funding Fees  
» pnl_fee | string | Realized PNL - Transaction Fees  
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
» cross_leverage_limit | string | Cross margin leverage (valid only when `leverage` is 0)  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
  
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
    
    url = '/delivery/usdt/positions/BTC_USDT_20200814/margin'
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
    url="/delivery/usdt/positions/BTC_USDT_20200814/margin"
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
      "size": -9440,
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
      "average_maintenance_rate": "0.005"
    }
    

##  Update position leverage🔒 Authenticated

POST`/delivery/{settle}/positions/{contract}/leverage`

POST `/delivery/{settle}/positions/{contract}/leverage`

_Update position leverage_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
leverage | query | string | Required | New position leverage  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | DeliveryPosition  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | integer(int64) | Position size  
» leverage | string | Position leverage. 0 means cross margin; positive number means isolated margin  
» risk_limit | string | Position risk limit  
» leverage_max | string | Maximum leverage under current risk limit  
» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Liquidation price  
» mark_price | string | Current mark price  
» initial_margin | string | The initial margin occupied by the position, applicable to the portfolio margin account  
» maintenance_margin | string | Maintenance margin required for the position, applicable to portfolio margin account  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realized PnL  
» pnl_pnl | string | Realized PNL - Position P/L  
» pnl_fund | string | Realized PNL - Funding Fees  
» pnl_fee | string | Realized PNL - Transaction Fees  
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
» cross_leverage_limit | string | Cross margin leverage (valid only when `leverage` is 0)  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
  
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
    
    url = '/delivery/usdt/positions/BTC_USDT_20200814/leverage'
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
    url="/delivery/usdt/positions/BTC_USDT_20200814/leverage"
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
      "size": -9440,
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
      "average_maintenance_rate": "0.005"
    }
    

##  Update position risk limit🔒 Authenticated

POST`/delivery/{settle}/positions/{contract}/risk_limit`

POST `/delivery/{settle}/positions/{contract}/risk_limit`

_Update position risk limit_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | path | string | Required | Futures contract  
risk_limit | query | string | Required | New position risk limit  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Position information

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | DeliveryPosition  
  
### Response Schema

Status Code **200**

_Futures position details_

Name | Type | Description  
---|---|---  
» user | integer(int64) | User ID  
» contract | string | Futures contract  
» size | integer(int64) | Position size  
» leverage | string | Position leverage. 0 means cross margin; positive number means isolated margin  
» risk_limit | string | Position risk limit  
» leverage_max | string | Maximum leverage under current risk limit  
» maintenance_rate | string | The maintenance margin rate of the first tier of risk limit sheet  
» value | string | Position value calculated in settlement currency  
» margin | string | Position margin  
» entry_price | string | Entry price  
» liq_price | string | Liquidation price  
» mark_price | string | Current mark price  
» initial_margin | string | The initial margin occupied by the position, applicable to the portfolio margin account  
» maintenance_margin | string | Maintenance margin required for the position, applicable to portfolio margin account  
» unrealised_pnl | string | Unrealized PNL  
» realised_pnl | string | Realized PnL  
» pnl_pnl | string | Realized PNL - Position P/L  
» pnl_fund | string | Realized PNL - Funding Fees  
» pnl_fee | string | Realized PNL - Transaction Fees  
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
» cross_leverage_limit | string | Cross margin leverage (valid only when `leverage` is 0)  
» update_time | integer(int64) | Last update time  
» update_id | integer(int64) | Update ID. The value increments by 1 each time the position is updated  
» open_time | integer(int64) | First Open Time  
» risk_limit_table | string | Risk limit table ID  
» average_maintenance_rate | string | Average maintenance margin rate  
  
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
    
    url = '/delivery/usdt/positions/BTC_USDT_20200814/risk_limit'
    query_param = 'risk_limit=10'
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
    url="/delivery/usdt/positions/BTC_USDT_20200814/risk_limit"
    query_param="risk_limit=10"
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
      "size": -9440,
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
      "average_maintenance_rate": "0.005"
    }
    

##  Query futures order list🔒 Authenticated

GET`/delivery/{settle}/orders`

GET `/delivery/{settle}/orders`

_Query futures order list_

Zero-fill orders cannot be retrieved 10 minutes after order cancellation

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Optional | Futures contract  
status | query | string | Required | Query order list based on status  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
last_id | query | string | Optional | Use the ID of the last record in the previous list as the starting point for the next list  
  
Operations based on custom IDs can only be checked when orders are pending. After orders are completed (filled/cancelled), they can be checked within 1 hour after completion. After expiration, only order IDs can be used  
count_total | query | integer | Optional | Whether to return total number matched, defaults to 0 (no return)  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**last_id** : Use the ID of the last record in the previous list as the starting point for the next list  
  
Operations based on custom IDs can only be checked when orders are pending. After orders are completed (filled/cancelled), they can be checked within 1 hour after completion. After expiration, only order IDs can be used

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
status | open  
status | finished  
count_total | 0  
count_total | 1  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures order details]  
» _None_ | DeliveryOrder | Futures order details  
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
»» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
»» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
»» price | string | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
»» is_close | boolean | Is the order to close position  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_liq | boolean | Is the order for liquidation  
»» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
»» left | integer(int64) | Unfilled quantity  
»» fill_price | string | Fill price  
»» text | string | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
200 | X-Pagination-Total | integer |  | Total number matched, only returned if `count_total` is set to 1  
  
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
    
    url = '/delivery/usdt/orders'
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
    url="/delivery/usdt/orders"
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
        "size": 6024,
        "iceberg": 0,
        "left": 6024,
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
        "amend_text": "-"
      }
    ]
    

##  Place futures order🔒 Authenticated

POST`/delivery/{settle}/orders`

POST `/delivery/{settle}/orders`

_Place futures order_

Zero-fill orders cannot be retrieved 10 minutes after order cancellation

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | DeliveryOrder | Required | none  
↳ contract | body | string | Required | Futures contract  
↳ size | body | integer(int64) | Required | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
↳ iceberg | body | integer(int64) | Optional | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
↳ price | body | string | Optional | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
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
settle | usdt  
  
### Responses

  * 201[Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2)Order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order details | DeliveryOrder  
  
### Response Schema

Status Code **201**

_Futures order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Futures order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
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
» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
» left | integer(int64) | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
    
    url = '/delivery/usdt/orders'
    query_param = ''
    body='{"contract":"BTC_USDT","size":6024,"iceberg":0,"price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-"}'
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
    url="/delivery/usdt/orders"
    query_param=""
    body_param='{"contract":"BTC_USDT","size":6024,"iceberg":0,"price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-"}'
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
      "size": 6024,
      "iceberg": 0,
      "price": "3765",
      "tif": "gtc",
      "text": "t-my-custom-id",
      "stp_act": "-"
    }
    

> Example responses

> 201 Response
    
    
    {
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968,
      "size": 6024,
      "iceberg": 0,
      "left": 6024,
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
      "amend_text": "-"
    }
    

##  Cancel all orders with 'open' status🔒 Authenticated

DELETE`/delivery/{settle}/orders`

DELETE `/delivery/{settle}/orders`

_Cancel all orders with 'open' status_

Zero-fill orders cannot be retrieved 10 minutes after order cancellation

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Required | Futures contract  
side | query | string | Optional | Specify all bids or all asks, both included if not specified  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | ask  
side | bid  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Batch cancellation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancellation successful | [DeliveryOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Futures order details]  
» _None_ | DeliveryOrder | Futures order details  
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
»» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
»» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
»» price | string | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
»» is_close | boolean | Is the order to close position  
»» is_reduce_only | boolean | Is the order reduce-only  
»» is_liq | boolean | Is the order for liquidation  
»» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
»» left | integer(int64) | Unfilled quantity  
»» fill_price | string | Fill price  
»» text | string | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
    
    url = '/delivery/usdt/orders'
    query_param = 'contract=BTC_USDT_20200814'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/delivery/usdt/orders"
    query_param="contract=BTC_USDT_20200814"
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
        "size": 6024,
        "iceberg": 0,
        "left": 6024,
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
        "amend_text": "-"
      }
    ]
    

##  Query single order details🔒 Authenticated

GET`/delivery/{settle}/orders/{order_id}`

GET `/delivery/{settle}/orders/{order_id}`

_Query single order details_

Zero-fill orders cannot be retrieved 10 minutes after order cancellation

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
order_id | path | string | Required | ID returned when order is successfully created  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order details | DeliveryOrder  
  
### Response Schema

Status Code **200**

_Futures order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Futures order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
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
» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
» left | integer(int64) | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
    
    url = '/delivery/usdt/orders/12345'
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
    url="/delivery/usdt/orders/12345"
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
      "size": 6024,
      "iceberg": 0,
      "left": 6024,
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
      "amend_text": "-"
    }
    

##  Cancel single order🔒 Authenticated

DELETE`/delivery/{settle}/orders/{order_id}`

DELETE `/delivery/{settle}/orders/{order_id}`

_Cancel single order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
order_id | path | string | Required | ID returned when order is successfully created  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order details | DeliveryOrder  
  
### Response Schema

Status Code **200**

_Futures order details_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Futures order ID  
» user | integer | User ID  
» create_time | number(double) | Creation time of order  
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
» size | integer(int64) | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
» iceberg | integer(int64) | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
» price | string | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
» is_close | boolean | Is the order to close position  
» is_reduce_only | boolean | Is the order reduce-only  
» is_liq | boolean | Is the order for liquidation  
» tif | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
» left | integer(int64) | Unfilled quantity  
» fill_price | string | Fill price  
» text | string | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
    
    url = '/delivery/usdt/orders/12345'
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
    url="/delivery/usdt/orders/12345"
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
      "size": 6024,
      "iceberg": 0,
      "left": 6024,
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
      "amend_text": "-"
    }
    

##  Query personal trading records🔒 Authenticated

GET`/delivery/{settle}/my_trades`

GET `/delivery/{settle}/my_trades`

_Query personal trading records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract  
order | query | integer(int64) | Optional | Futures order ID, return related data only if specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
last_id | query | string | Optional | Use the ID of the last record in the previous list as the starting point for the next list  
  
Operations based on custom IDs can only be checked when orders are pending. After orders are completed (filled/cancelled), they can be checked within 1 hour after completion. After expiration, only order IDs can be used  
count_total | query | integer | Optional | Whether to return total number matched, defaults to 0 (no return)  
  
####  Detailed descriptions

**last_id** : Use the ID of the last record in the previous list as the starting point for the next list  
  
Operations based on custom IDs can only be checked when orders are pending. After orders are completed (filled/cancelled), they can be checked within 1 hour after completion. After expiration, only order IDs can be used

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
count_total | 0  
count_total | 1  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryMyTrade]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int64) | Fill ID  
» create_time | number(double) | Fill Time  
» contract | string | Futures contract  
» order_id | string | Related order ID  
» size | integer(int64) | Trading size  
» close_size | integer(int64) | Number of closed positions:  
  
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
200 | X-Pagination-Total | integer |  | Total number matched, only returned if `count_total` is set to 1  
  
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
    
    url = '/delivery/usdt/my_trades'
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
    url="/delivery/usdt/my_trades"
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
        "size": 100,
        "price": "100.123",
        "text": "t-123456",
        "fee": "0.01",
        "point_fee": "0",
        "role": "taker",
        "close_size": 0
      }
    ]
    

##  Query position close history🔒 Authenticated

GET`/delivery/{settle}/position_close`

GET `/delivery/{settle}/position_close`

_Query position close history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryPositionClose]  
  
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
» max_size | integer(int64) | Max Trade Size  
» accum_size | integer(int64) | Cumulative closed position volume  
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
    
    url = '/delivery/usdt/position_close'
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
    url="/delivery/usdt/position_close"
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

GET`/delivery/{settle}/liquidates`

GET `/delivery/{settle}/liquidates`

_Query liquidation history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract  
limit | query | integer | Optional | Maximum number of records returned in a single list  
at | query | integer | Optional | Specify liquidation timestamp  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryLiquidate]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | integer(int64) | Liquidation time  
» contract | string | Futures contract  
» leverage | string | Position leverage. Not returned in public endpoints  
» size | integer(int64) | Position size  
» margin | string | Position margin. Not returned in public endpoints  
» entry_price | string | Average entry price. Not returned in public endpoints  
» liq_price | string | Liquidation price. Not returned in public endpoints  
» mark_price | string | Mark price. Not returned in public endpoints  
» order_id | integer(int64) | Liquidation order ID. Not returned in public endpoints  
» order_price | string | Liquidation order price  
» fill_price | string | Liquidation order average taker price  
» left | integer(int64) | Liquidation order maker size  
  
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
    
    url = '/delivery/usdt/liquidates'
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
    url="/delivery/usdt/liquidates"
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
        "size": 600,
        "leverage": "25",
        "margin": "0.006705256878",
        "entry_price": "3536.123",
        "liq_price": "3421.54",
        "mark_price": "3420.27",
        "order_id": 317393847,
        "order_price": "3405",
        "fill_price": "3424",
        "left": 0
      }
    ]
    

##  Query settlement records🔒 Authenticated

GET`/delivery/{settle}/settlements`

GET `/delivery/{settle}/settlements`

_Query settlement records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract  
limit | query | integer | Optional | Maximum number of records returned in a single list  
at | query | integer | Optional | Specify settlement timestamp  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliverySettlement]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» time | integer(int64) | Liquidation time  
» contract | string | Futures contract  
» leverage | string | Position leverage  
» size | integer(int64) | Position size  
» margin | string | Position margin  
» entry_price | string | Average entry price  
» settle_price | string | Settled price  
» profit | string | Profit  
» fee | string | Fee deducted  
  
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
    
    url = '/delivery/usdt/settlements'
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
    url="/delivery/usdt/settlements"
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
        "size": 600,
        "leverage": "25",
        "margin": "0.006705256878",
        "entry_price": "3536.123",
        "settle_price": "3421.54",
        "profit": "-6.87498",
        "fee": "0.03079386"
      }
    ]
    

##  Query risk limit tiers

GET`/delivery/{settle}/risk_limit_tiers`

GET `/delivery/{settle}/risk_limit_tiers`

_Query risk limit tiers_

When the 'contract' parameter is not passed, the default is to query the risk limits for the top 100 markets. 'Limit' and 'offset' correspond to pagination queries at the market level, not to the length of the returned array. This only takes effect when the contract parameter is empty.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
contract | query | string | Optional | Futures contract  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [DeliveryLimitRiskTiers]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Retrieve risk limit configurations for different tiers under a specified contract]  
» _None_ | DeliveryLimitRiskTiers | Retrieve risk limit configurations for different tiers under a specified contract  
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
    
    url = '/delivery/usdt/risk_limit_tiers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/risk_limit_tiers \
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
    

##  Query auto order list🔒 Authenticated

GET`/delivery/{settle}/price_orders`

GET `/delivery/{settle}/price_orders`

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
    
    url = '/delivery/usdt/price_orders'
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
    url="/delivery/usdt/price_orders"
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

POST`/delivery/{settle}/price_orders`

POST `/delivery/{settle}/price_orders`

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
    
    url = '/delivery/usdt/price_orders'
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
    url="/delivery/usdt/price_orders"
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
      "id": 1432329
    }
    

##  Cancel all auto orders🔒 Authenticated

DELETE`/delivery/{settle}/price_orders`

DELETE `/delivery/{settle}/price_orders`

_Cancel all auto orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
contract | query | string | Required | Futures contract  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
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
    
    url = '/delivery/usdt/price_orders'
    query_param = 'contract=BTC_USDT'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/delivery/usdt/price_orders"
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

GET`/delivery/{settle}/price_orders/{order_id}`

GET `/delivery/{settle}/price_orders/{order_id}`

_Query single auto order details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
order_id | path | string | Required | ID returned when order is successfully created  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
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
    
    url = '/delivery/usdt/price_orders/string'
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
    url="/delivery/usdt/price_orders/string"
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

DELETE`/delivery/{settle}/price_orders/{order_id}`

DELETE `/delivery/{settle}/price_orders/{order_id}`

_Cancel single auto order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
order_id | path | string | Required | ID returned when order is successfully created  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
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
    
    url = '/delivery/usdt/price_orders/string'
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
    url="/delivery/usdt/price_orders/string"
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
    

#  Schemas

##  DeliveryOrder

_Futures order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
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
contract | string | Required | none | Futures contract  
size | integer(int64) | Required | none | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | integer(int64) | Optional | none | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
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
      "amend_text": "string"
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
    
    

##  DeliveryTrade

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Fill ID  
create_time | number(double) | Optional | none | Fill Time  
create_time_ms | number(double) | Optional | none | Trade time, with millisecond precision to 3 decimal places  
contract | string | Optional | none | Futures contract  
size | integer(int64) | Optional | none | Trading size  
price | string | Optional | none | Trade price (quote currency)  
is_internal | boolean | Optional | none | Deprecated  
      
    
    {
      "id": 0,
      "create_time": 0,
      "create_time_ms": 0,
      "contract": "string",
      "size": 0,
      "price": "string",
      "is_internal": true
    }
    
    

##  DeliveryContract

_Futures contract details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
name | string | Optional | none | Futures contract  
underlying | string | Optional | none | Underlying  
cycle | string | Optional | none | Cycle type, e.g. WEEKLY, QUARTERLY  
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
basis_rate | string | Optional | none | Fair basis rate  
basis_value | string | Optional | none | Fair basis value  
basis_impact_value | string | Optional | none | Funding used for calculating impact bid, ask price  
settle_price | string | Optional | none | Settle price  
settle_price_interval | integer | Optional | none | Settle price update interval  
settle_price_duration | integer | Optional | none | Settle price update duration in seconds  
expire_time | integer(int64) | Optional | none | Contract expiry timestamp  
risk_limit_base | string | Optional | none | Risk limit base  
risk_limit_step | string | Optional | none | Step of adjusting risk limit  
risk_limit_max | string | Optional | none | Maximum risk limit the contract allowed  
order_size_min | integer(int64) | Optional | none | Minimum order size allowed by the contract  
order_size_max | integer(int64) | Optional | none | Maximum order size allowed by the contract  
order_price_deviate | string | Optional | none | Maximum allowed deviation between order price and current mark price. The order price `order_price` must satisfy the following condition:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | Optional | none | Trading fee discount for referred users  
ref_rebate_rate | string | Optional | none | Commission rate for referrers  
orderbook_id | integer(int64) | Optional | none | Orderbook update ID  
trade_id | integer(int64) | Optional | none | Current trade ID  
trade_size | integer(int64) | Optional | none | Historical cumulative trading volume  
position_size | integer(int64) | Optional | none | Current total long position size  
config_change_time | number(double) | Optional | none | Last configuration update time  
in_delisting | boolean | Optional | none | Contract is delisting  
orders_limit | integer | Optional | none | Maximum number of pending orders  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
cycle | WEEKLY  
cycle | BI-WEEKLY  
cycle | QUARTERLY  
cycle | BI-QUARTERLY  
type | inverse  
type | direct  
mark_type | internal  
mark_type | index  
      
    
    {
      "name": "string",
      "underlying": "string",
      "cycle": "WEEKLY",
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
      "basis_rate": "string",
      "basis_value": "string",
      "basis_impact_value": "string",
      "settle_price": "string",
      "settle_price_interval": 0,
      "settle_price_duration": 0,
      "expire_time": 0,
      "risk_limit_base": "string",
      "risk_limit_step": "string",
      "risk_limit_max": "string",
      "order_size_min": 0,
      "order_size_max": 0,
      "order_price_deviate": "string",
      "ref_discount_rate": "string",
      "ref_rebate_rate": "string",
      "orderbook_id": 0,
      "trade_id": 0,
      "trade_size": 0,
      "position_size": 0,
      "config_change_time": 0,
      "in_delisting": true,
      "orders_limit": 0
    }
    
    

##  DeliveryPositionClose

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
max_size | integer(int64) | Optional | read-only | Max Trade Size  
accum_size | integer(int64) | Optional | read-only | Cumulative closed position volume  
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
      "max_size": 0,
      "accum_size": 0,
      "first_open_time": 0,
      "long_price": "string",
      "short_price": "string"
    }
    
    

##  DeliverySettlement

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | integer(int64) | Optional | read-only | Liquidation time  
contract | string | Optional | read-only | Futures contract  
leverage | string | Optional | read-only | Position leverage  
size | integer(int64) | Optional | read-only | Position size  
margin | string | Optional | read-only | Position margin  
entry_price | string | Optional | read-only | Average entry price  
settle_price | string | Optional | read-only | Settled price  
profit | string | Optional | read-only | Profit  
fee | string | Optional | read-only | Fee deducted  
      
    
    {
      "time": 0,
      "contract": "string",
      "leverage": "string",
      "size": 0,
      "margin": "string",
      "entry_price": "string",
      "settle_price": "string",
      "profit": "string",
      "fee": "string"
    }
    
    

##  DeliveryMyTrade

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Fill ID  
create_time | number(double) | Optional | none | Fill Time  
contract | string | Optional | none | Futures contract  
order_id | string | Optional | none | Related order ID  
size | integer(int64) | Optional | none | Trading size  
close_size | integer(int64) | Optional | none | Number of closed positions:  
  
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
      "id": 0,
      "create_time": 0,
      "contract": "string",
      "order_id": "string",
      "size": 0,
      "close_size": 0,
      "price": "string",
      "role": "taker",
      "text": "string",
      "fee": "string",
      "point_fee": "string"
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
    
    

##  DeliveryOrderBook

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Order Book ID. Increases by 1 on every order book change. Set `with_id=true` to include this field in response  
current | number(double) | Optional | none | Response data generation timestamp  
update | number(double) | Optional | none | Order book changed timestamp  
asks | array | Required | none | Ask Depth  
↳ DeliveryOrderBookItem | object | Optional | none | none  
↳ p | string | Optional | none | Price (quote currency)  
↳ s | integer(int64) | Optional | none | Size  
↳ bids | array | Required | none | Bid Depth  
↳ DeliveryOrderBookItem | object | Optional | none | none  
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
    
    

##  DeliveryLiquidate

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
time | integer(int64) | Optional | read-only | Liquidation time  
contract | string | Optional | read-only | Futures contract  
leverage | string | Optional | read-only | Position leverage. Not returned in public endpoints  
size | integer(int64) | Optional | read-only | Position size  
margin | string | Optional | read-only | Position margin. Not returned in public endpoints  
entry_price | string | Optional | read-only | Average entry price. Not returned in public endpoints  
liq_price | string | Optional | read-only | Liquidation price. Not returned in public endpoints  
mark_price | string | Optional | read-only | Mark price. Not returned in public endpoints  
order_id | integer(int64) | Optional | read-only | Liquidation order ID. Not returned in public endpoints  
order_price | string | Optional | read-only | Liquidation order price  
fill_price | string | Optional | read-only | Liquidation order average taker price  
left | integer(int64) | Optional | read-only | Liquidation order maker size  
      
    
    {
      "time": 0,
      "contract": "string",
      "leverage": "string",
      "size": 0,
      "margin": "string",
      "entry_price": "string",
      "liq_price": "string",
      "mark_price": "string",
      "order_id": 0,
      "order_price": "string",
      "fill_price": "string",
      "left": 0
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
    
    

##  DeliveryAccountBook

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
    
    

##  DeliveryPosition

_Futures position details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user | integer(int64) | Optional | read-only | User ID  
contract | string | Optional | read-only | Futures contract  
size | integer(int64) | Optional | read-only | Position size  
leverage | string | Optional | none | Position leverage. 0 means cross margin; positive number means isolated margin  
risk_limit | string | Optional | none | Position risk limit  
leverage_max | string | Optional | read-only | Maximum leverage under current risk limit  
maintenance_rate | string | Optional | read-only | The maintenance margin rate of the first tier of risk limit sheet  
value | string | Optional | read-only | Position value calculated in settlement currency  
margin | string | Optional | none | Position margin  
entry_price | string | Optional | read-only | Entry price  
liq_price | string | Optional | read-only | Liquidation price  
mark_price | string | Optional | read-only | Current mark price  
initial_margin | string | Optional | read-only | The initial margin occupied by the position, applicable to the portfolio margin account  
maintenance_margin | string | Optional | read-only | Maintenance margin required for the position, applicable to portfolio margin account  
unrealised_pnl | string | Optional | read-only | Unrealized PNL  
realised_pnl | string | Optional | read-only | Realized PnL  
pnl_pnl | string | Optional | read-only | Realized PNL - Position P/L  
pnl_fund | string | Optional | read-only | Realized PNL - Funding Fees  
pnl_fee | string | Optional | read-only | Realized PNL - Transaction Fees  
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
cross_leverage_limit | string | Optional | none | Cross margin leverage (valid only when `leverage` is 0)  
update_time | integer(int64) | Optional | read-only | Last update time  
update_id | integer(int64) | Optional | read-only | Update ID. The value increments by 1 each time the position is updated  
open_time | integer(int64) | Optional | none | First Open Time  
risk_limit_table | string | Optional | read-only | Risk limit table ID  
average_maintenance_rate | string | Optional | read-only | Average maintenance margin rate  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
      
    
    {
      "user": 0,
      "contract": "string",
      "size": 0,
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
      "average_maintenance_rate": "string"
    }
    
    

##  DeliveryTicker

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
basis_rate | string | Optional | none | Basis rate  
basis_value | string | Optional | none | Basis value  
lowest_ask | string | Optional | none | Recent lowest ask  
lowest_size | string | Optional | none | The latest seller's lowest price order quantity  
highest_bid | string | Optional | none | Recent highest bid  
highest_size | string | Optional | none | The latest buyer's highest price order volume  
      
    
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
      "basis_rate": "string",
      "basis_value": "string",
      "lowest_ask": "string",
      "lowest_size": "string",
      "highest_bid": "string",
      "highest_size": "string"
    }
    
    

##  DeliveryLimitRiskTiers

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
    
    

##  DeliveryCandlestick

_data point in every timestamp_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
t | number(double) | Optional | none | Unix timestamp in seconds  
v | integer(int64) | Optional | none | size volume (contract size). Only returned if `contract` is not prefixed  
c | string | Optional | none | Close price (quote currency)  
h | string | Optional | none | Highest price (quote currency)  
l | string | Optional | none | Lowest price (quote currency)  
o | string | Optional | none | Open price (quote currency)  
      
    
    {
      "t": 0,
      "v": 0,
      "c": "string",
      "h": "string",
      "l": "string",
      "o": "string"
    }
    
    

##  DeliveryAccount

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
total | string | Optional | none | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional | none | Unrealized PNL  
position_margin | string | Optional | none | Deprecated  
order_margin | string | Optional | none | initial margin of all open orders  
available | string | Optional | none | Available amount for transfer or trading, which includes credit limits under the unified account (includes experience funds; experience funds cannot be transferred, so when transferring, the transfer amount must deduct experience funds)  
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
        "bonus_offset": "string"
      }
    }