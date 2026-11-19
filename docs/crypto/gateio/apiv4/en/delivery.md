---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/delivery
api_type: Trading
updated_at: 2026-11-19 19:00:40.499719
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryContract]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Futures contract details

Type | Constraints  
---|---  
DeliveryContract |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Optional |  | Futures contract  
underlying | string | Optional |  | Underlying  
cycle | string | Optional | enum: ["WEEKLY","BI-WEEKLY","QUARTERLY","BI-QUARTERLY"] | Cycle type, e.g. WEEKLY, QUARTERLY  
type | string | Optional | enum: ["inverse","direct"] | Contract type: inverse - inverse contract, direct - direct contract  
quanto_multiplier | string | Optional |  | The contract multiplier indicates how many units of the underlying asset the face value of one contract represents.  
leverage_min | string | Optional |  | Minimum leverage  
leverage_max | string | Optional |  | Maximum leverage  
maintenance_rate | string | Optional |  | The maintenance margin rate of the first tier of risk limit sheet  
mark_type | string | Optional | enum: ["internal","index"] | Deprecated  
mark_price | string | Optional |  | Current mark price  
index_price | string | Optional |  | Current index price  
last_price | string | Optional |  | Last trading price  
maker_fee_rate | string | Optional |  | Maker fee rate, negative values indicate rebates  
taker_fee_rate | string | Optional |  | Taker fee rate  
order_price_round | string | Optional |  | Minimum order price increment  
mark_price_round | string | Optional |  | Minimum mark price increment  
basis_rate | string | Optional |  | Fair basis rate  
basis_value | string | Optional |  | Fair basis value  
basis_impact_value | string | Optional |  | Funding used for calculating impact bid, ask price  
settle_price | string | Optional |  | Settle price  
settle_price_interval | integer | Optional |  | Settle price update interval  
settle_price_duration | integer | Optional |  | Settle price update duration in seconds  
expire_time | integer(int64) | Optional |  | Contract expiry timestamp  
risk_limit_base | string | Optional |  | Risk limit base  
risk_limit_step | string | Optional |  | Step of adjusting risk limit  
risk_limit_max | string | Optional |  | Maximum risk limit the contract allowed  
order_size_min | integer(int64) | Optional |  | Minimum order quantity  
order_size_max | integer(int64) | Optional |  | Maximum order quantity  
order_price_deviate | string | Optional |  | Maximum allowed deviation between order price and current mark price. The order price `order_price` must satisfy the following condition:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | Optional |  | Trading fee discount for referred users  
ref_rebate_rate | string | Optional |  | Commission rate for referrers  
orderbook_id | integer(int64) | Optional |  | Orderbook update ID  
trade_id | integer(int64) | Optional |  | Current trade ID  
trade_size | integer(int64) | Optional |  | Historical cumulative trading volume  
position_size | integer(int64) | Optional |  | Current total long position size  
config_change_time | number(double) | Optional |  | Last configuration update time  
in_delisting | boolean | Optional |  | Contract is delisting  
orders_limit | integer | Optional |  | Maximum number of pending orders  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Contract information | DeliveryContract  
  
### Response Schema

Status Code **200**

Futures contract details

Type | Constraints  
---|---  
DeliveryContract |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Optional |  | Futures contract  
underlying | string | Optional |  | Underlying  
cycle | string | Optional | enum: ["WEEKLY","BI-WEEKLY","QUARTERLY","BI-QUARTERLY"] | Cycle type, e.g. WEEKLY, QUARTERLY  
type | string | Optional | enum: ["inverse","direct"] | Contract type: inverse - inverse contract, direct - direct contract  
quanto_multiplier | string | Optional |  | The contract multiplier indicates how many units of the underlying asset the face value of one contract represents.  
leverage_min | string | Optional |  | Minimum leverage  
leverage_max | string | Optional |  | Maximum leverage  
maintenance_rate | string | Optional |  | The maintenance margin rate of the first tier of risk limit sheet  
mark_type | string | Optional | enum: ["internal","index"] | Deprecated  
mark_price | string | Optional |  | Current mark price  
index_price | string | Optional |  | Current index price  
last_price | string | Optional |  | Last trading price  
maker_fee_rate | string | Optional |  | Maker fee rate, negative values indicate rebates  
taker_fee_rate | string | Optional |  | Taker fee rate  
order_price_round | string | Optional |  | Minimum order price increment  
mark_price_round | string | Optional |  | Minimum mark price increment  
basis_rate | string | Optional |  | Fair basis rate  
basis_value | string | Optional |  | Fair basis value  
basis_impact_value | string | Optional |  | Funding used for calculating impact bid, ask price  
settle_price | string | Optional |  | Settle price  
settle_price_interval | integer | Optional |  | Settle price update interval  
settle_price_duration | integer | Optional |  | Settle price update duration in seconds  
expire_time | integer(int64) | Optional |  | Contract expiry timestamp  
risk_limit_base | string | Optional |  | Risk limit base  
risk_limit_step | string | Optional |  | Step of adjusting risk limit  
risk_limit_max | string | Optional |  | Maximum risk limit the contract allowed  
order_size_min | integer(int64) | Optional |  | Minimum order quantity  
order_size_max | integer(int64) | Optional |  | Maximum order quantity  
order_price_deviate | string | Optional |  | Maximum allowed deviation between order price and current mark price. The order price `order_price` must satisfy the following condition:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | Optional |  | Trading fee discount for referred users  
ref_rebate_rate | string | Optional |  | Commission rate for referrers  
orderbook_id | integer(int64) | Optional |  | Orderbook update ID  
trade_id | integer(int64) | Optional |  | Current trade ID  
trade_size | integer(int64) | Optional |  | Historical cumulative trading volume  
position_size | integer(int64) | Optional |  | Current total long position size  
config_change_time | number(double) | Optional |  | Last configuration update time  
in_delisting | boolean | Optional |  | Contract is delisting  
orders_limit | integer | Optional |  | Maximum number of pending orders  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Depth query successful | DeliveryOrderBook  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
DeliveryOrderBook | required: ["asks","bids"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order Book ID. Increases by 1 on every order book change. Set `with_id=true` to include this field in response  
current | number(double) | Optional |  | Response data generation timestamp  
update | number(double) | Optional |  | Order book changed timestamp  
asks | array | Required |  | Ask Depth  
bids | array | Required |  | Bid Depth  
  
**asks**

Ask Depth

Type | Constraints  
---|---  
array |   
  
**asks / items**

DeliveryOrderBookItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
p | string | Optional |  | Price (quote currency)  
s | integer(int64) | Optional |  | Size  
  
**bids**

Bid Depth

Type | Constraints  
---|---  
array |   
  
**bids / items**

DeliveryOrderBookItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
p | string | Optional |  | Price (quote currency)  
s | integer(int64) | Optional |  | Size  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryTrade]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DeliveryTrade |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Fill ID  
create_time | number(double) | Optional |  | Fill Time  
create_time_ms | number(double) | Optional |  | Trade time, with millisecond precision to 3 decimal places  
contract | string | Optional |  | Futures contract  
size | integer(int64) | Optional |  | Trading size  
price | string | Optional |  | Trade price (quote currency)  
is_internal | boolean | Optional |  | Deprecated  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [DeliveryCandlestick]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

data point in every timestamp

Type | Constraints  
---|---  
DeliveryCandlestick |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
t | number(double) | Optional |  | Unix timestamp in seconds  
v | integer(int64) | Optional |  | size volume (contract size). Only returned if `contract` is not prefixed  
c | string | Optional |  | Close price (quote currency)  
h | string | Optional |  | Highest price (quote currency)  
l | string | Optional |  | Lowest price (quote currency)  
o | string | Optional |  | Open price (quote currency)  
  
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

_Get all futures trading statistics_

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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [DeliveryTicker]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DeliveryTicker |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
contract | string | Optional |  | Futures contract  
last | string | Optional |  | Last trading price  
change_percentage | string | Optional |  | Price change percentage. Negative values indicate price decrease, e.g. -7.45  
total_size | string | Optional |  | Contract total size  
low_24h | string | Optional |  | 24-hour lowest price  
high_24h | string | Optional |  | 24-hour highest price  
volume_24h | string | Optional |  | 24-hour trading volume  
volume_24h_btc | string | Optional |  | 24-hour trading volume in BTC (deprecated, use `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle` instead)  
volume_24h_usd | string | Optional |  | 24-hour trading volume in USD (deprecated, use `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle` instead)  
volume_24h_base | string | Optional |  | 24-hour trading volume in base currency  
volume_24h_quote | string | Optional |  | 24-hour trading volume in quote currency  
volume_24h_settle | string | Optional |  | 24-hour trading volume in settle currency  
mark_price | string | Optional |  | Recent mark price  
funding_rate | string | Optional |  | Funding rate  
funding_rate_indicative | string | Optional |  | Indicative Funding rate in next period. (deprecated. use `funding_rate`)  
index_price | string | Optional |  | Index price  
quanto_base_rate | string | Optional |  | Deprecated  
basis_rate | string | Optional |  | Basis rate  
basis_value | string | Optional |  | Basis value  
lowest_ask | string | Optional |  | Recent lowest ask  
lowest_size | string | Optional |  | The latest seller's lowest price order quantity  
highest_bid | string | Optional |  | Recent highest bid  
highest_size | string | Optional |  | The latest buyer's highest price order volume  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [InsuranceRecord]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
InsuranceRecord |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
t | integer(int64) | Optional |  | Unix timestamp in seconds  
b | string | Optional |  | Insurance balance  
  
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

_Get futures account_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | DeliveryAccount  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
DeliveryAccount |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | string | Optional |  | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional |  | Unrealized PNL  
position_margin | string | Optional |  | Deprecated  
order_margin | string | Optional |  | initial margin of all open orders  
available | string | Optional |  | Available amount for transfer or trading, which includes credit limits under the unified account (includes experience funds; experience funds cannot be transferred, so when transferring, the transfer amount must deduct experience funds)  
point | string | Optional |  | Point card amount  
currency | string | Optional |  | Settlement currency  
in_dual_mode | boolean | Optional |  | Whether Hedge Mode is enabled  
enable_credit | boolean | Optional |  | Whether portfolio margin account mode is enabled  
position_initial_margin | string | Optional |  | Initial margin occupied by positions, applicable to unified account mode  
maintenance_margin | string | Optional |  | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode  
bonus | string | Optional |  | Bonus  
enable_evolved_classic | boolean | Optional |  | Deprecated  
cross_order_margin | string | Optional |  | Cross margin order margin, applicable to new classic account margin mode  
cross_initial_margin | string | Optional |  | Cross margin initial margin, applicable to new classic account margin mode  
cross_maintenance_margin | string | Optional |  | Cross margin maintenance margin, applicable to new classic account margin mode  
cross_unrealised_pnl | string | Optional |  | Cross margin unrealized P&L, applicable to new classic account margin mode  
cross_available | string | Optional |  | Cross margin available balance, applicable to new classic account margin mode  
cross_margin_balance | string | Optional |  | Cross margin balance, applicable to new classic account margin mode  
cross_mmr | string | Optional |  | Cross margin maintenance margin rate, applicable to new classic account margin mode  
cross_imr | string | Optional |  | Cross margin initial margin rate, applicable to new classic account margin mode  
isolated_position_margin | string | Optional |  | Isolated position margin, applicable to new classic account margin mode  
enable_new_dual_mode | boolean | Optional |  | Deprecated  
margin_mode | integer | Optional |  | Margin mode of the account  
0: classic future account or Classic Spot Margin Mode of unified account;  
1: Multi-Currency Margin Mode;  
2: Portoforlio Margin Mode;  
3: Single-Currency Margin Mode  
enable_tiered_mm | boolean | Optional |  | Whether to enable tiered maintenance margin calculation  
history | object | Optional |  | Statistical data  
  
**history**

Statistical data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
dnw | string | Optional |  | total amount of deposit and withdraw  
pnl | string | Optional |  | total amount of trading profit and loss  
fee | string | Optional |  | total amount of fee  
refr | string | Optional |  | total amount of referrer rebates  
fund | string | Optional |  | total amount of funding costs  
point_dnw | string | Optional |  | total amount of point deposit and withdraw  
point_fee | string | Optional |  | total amount of point fee  
point_refr | string | Optional |  | total amount of referrer rebates of point fee  
bonus_dnw | string | Optional |  | total amount of perpetual contract bonus transfer  
bonus_offset | string | Optional |  | total amount of perpetual contract bonus deduction  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryAccountBook]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DeliveryAccountBook |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | number(double) | Optional |  | Change time  
change | string | Optional |  | Change amount  
balance | string | Optional |  | Balance after change  
type | string | Optional | enum: ["dnw","pnl","fee","refr","fund","point_dnw","point_fee","point_refr","bonus_offset"] | Change types:  
  
\- dnw: Deposit and withdrawal  
\- pnl: Profit and loss from position reduction  
\- fee: Trading fees  
\- refr: Referrer rebates  
\- fund: Funding fees  
\- point_dnw: Point card deposit and withdrawal  
\- point_fee: Point card trading fees  
\- point_refr: Point card referrer rebates  
\- bonus_offset: Trial fund deduction  
text | string | Optional |  | Comment  
contract | string | Optional |  | Futures contract, the field is only available for data after 2023-10-30  
trade_id | string | Optional |  | trade id  
id | string | Optional |  | Account change record ID  
  
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

_Get user position list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
settle | path | string | Required | Settle currency  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | usdt  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryPosition]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Futures position details

Type | Constraints  
---|---  
DeliveryPosition |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | User ID  
contract | string | Optional | readOnly: true | Futures contract  
size | integer(int64) | Optional | readOnly: true | Position size  
leverage | string | Optional |  | Position leverage. 0 means cross margin; positive number means isolated margin  
risk_limit | string | Optional |  | Position risk limit  
leverage_max | string | Optional | readOnly: true | Maximum leverage under current risk limit  
maintenance_rate | string | Optional | readOnly: true | The maintenance margin rate of the first tier of risk limit sheet  
value | string | Optional | readOnly: true | Position value calculated in settlement currency  
margin | string | Optional |  | Margin  
entry_price | string | Optional | readOnly: true | Entry price  
liq_price | string | Optional | readOnly: true | Liquidation price  
mark_price | string | Optional | readOnly: true | Current mark price  
initial_margin | string | Optional | readOnly: true | The initial margin occupied by the position, applicable to the portfolio margin account  
maintenance_margin | string | Optional | readOnly: true | Maintenance margin required for the position, applicable to portfolio margin account  
unrealised_pnl | string | Optional | readOnly: true | Unrealized PNL  
realised_pnl | string | Optional | readOnly: true | Realized PnL  
pnl_pnl | string | Optional | readOnly: true | Realized PNL - Position P/L  
pnl_fund | string | Optional | readOnly: true | Realized PNL - Funding Fees  
pnl_fee | string | Optional | readOnly: true | Realized PNL - Transaction Fees  
history_pnl | string | Optional | readOnly: true | Total realized PnL from closed positions  
last_close_pnl | string | Optional | readOnly: true | PNL of last position close  
realised_point | string | Optional | readOnly: true | Realized POINT PNL  
history_point | string | Optional | readOnly: true | History realized POINT PNL  
adl_ranking | integer | Optional | readOnly: true | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
pending_orders | integer | Optional | readOnly: true | Current pending order quantity  
close_order | object|null | Optional | nullable: true  
readOnly: true | Current close order information, or `null` if no close order  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
cross_leverage_limit | string | Optional |  | Cross margin leverage (valid only when `leverage` is 0)  
update_time | integer(int64) | Optional | readOnly: true | Last update time  
update_id | integer(int64) | Optional | readOnly: true | Update ID. The value increments by 1 each time the position is updated  
open_time | integer(int64) | Optional |  | First Open Time  
risk_limit_table | string | Optional | readOnly: true | Risk limit table ID  
average_maintenance_rate | string | Optional | readOnly: true | Average maintenance margin rate  
  
**items / close_order**

Current close order information, or `null` if no close order

Type | Constraints  
---|---  
object|null | nullable: true  
readOnly: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order ID  
price | string | Optional |  | Order price  
is_liq | boolean | Optional |  | Whether the close order is from liquidation  
  
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

_Get single position information_

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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | DeliveryPosition  
  
### Response Schema

Status Code **200**

Futures position details

Type | Constraints  
---|---  
DeliveryPosition |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | User ID  
contract | string | Optional | readOnly: true | Futures contract  
size | integer(int64) | Optional | readOnly: true | Position size  
leverage | string | Optional |  | Position leverage. 0 means cross margin; positive number means isolated margin  
risk_limit | string | Optional |  | Position risk limit  
leverage_max | string | Optional | readOnly: true | Maximum leverage under current risk limit  
maintenance_rate | string | Optional | readOnly: true | The maintenance margin rate of the first tier of risk limit sheet  
value | string | Optional | readOnly: true | Position value calculated in settlement currency  
margin | string | Optional |  | Margin  
entry_price | string | Optional | readOnly: true | Entry price  
liq_price | string | Optional | readOnly: true | Liquidation price  
mark_price | string | Optional | readOnly: true | Current mark price  
initial_margin | string | Optional | readOnly: true | The initial margin occupied by the position, applicable to the portfolio margin account  
maintenance_margin | string | Optional | readOnly: true | Maintenance margin required for the position, applicable to portfolio margin account  
unrealised_pnl | string | Optional | readOnly: true | Unrealized PNL  
realised_pnl | string | Optional | readOnly: true | Realized PnL  
pnl_pnl | string | Optional | readOnly: true | Realized PNL - Position P/L  
pnl_fund | string | Optional | readOnly: true | Realized PNL - Funding Fees  
pnl_fee | string | Optional | readOnly: true | Realized PNL - Transaction Fees  
history_pnl | string | Optional | readOnly: true | Total realized PnL from closed positions  
last_close_pnl | string | Optional | readOnly: true | PNL of last position close  
realised_point | string | Optional | readOnly: true | Realized POINT PNL  
history_point | string | Optional | readOnly: true | History realized POINT PNL  
adl_ranking | integer | Optional | readOnly: true | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
pending_orders | integer | Optional | readOnly: true | Current pending order quantity  
close_order | object|null | Optional | nullable: true  
readOnly: true | Current close order information, or `null` if no close order  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
cross_leverage_limit | string | Optional |  | Cross margin leverage (valid only when `leverage` is 0)  
update_time | integer(int64) | Optional | readOnly: true | Last update time  
update_id | integer(int64) | Optional | readOnly: true | Update ID. The value increments by 1 each time the position is updated  
open_time | integer(int64) | Optional |  | First Open Time  
risk_limit_table | string | Optional | readOnly: true | Risk limit table ID  
average_maintenance_rate | string | Optional | readOnly: true | Average maintenance margin rate  
  
**close_order**

Current close order information, or `null` if no close order

Type | Constraints  
---|---  
object|null | nullable: true  
readOnly: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order ID  
price | string | Optional |  | Order price  
is_liq | boolean | Optional |  | Whether the close order is from liquidation  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | DeliveryPosition  
  
### Response Schema

Status Code **200**

Futures position details

Type | Constraints  
---|---  
DeliveryPosition |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | User ID  
contract | string | Optional | readOnly: true | Futures contract  
size | integer(int64) | Optional | readOnly: true | Position size  
leverage | string | Optional |  | Position leverage. 0 means cross margin; positive number means isolated margin  
risk_limit | string | Optional |  | Position risk limit  
leverage_max | string | Optional | readOnly: true | Maximum leverage under current risk limit  
maintenance_rate | string | Optional | readOnly: true | The maintenance margin rate of the first tier of risk limit sheet  
value | string | Optional | readOnly: true | Position value calculated in settlement currency  
margin | string | Optional |  | Margin  
entry_price | string | Optional | readOnly: true | Entry price  
liq_price | string | Optional | readOnly: true | Liquidation price  
mark_price | string | Optional | readOnly: true | Current mark price  
initial_margin | string | Optional | readOnly: true | The initial margin occupied by the position, applicable to the portfolio margin account  
maintenance_margin | string | Optional | readOnly: true | Maintenance margin required for the position, applicable to portfolio margin account  
unrealised_pnl | string | Optional | readOnly: true | Unrealized PNL  
realised_pnl | string | Optional | readOnly: true | Realized PnL  
pnl_pnl | string | Optional | readOnly: true | Realized PNL - Position P/L  
pnl_fund | string | Optional | readOnly: true | Realized PNL - Funding Fees  
pnl_fee | string | Optional | readOnly: true | Realized PNL - Transaction Fees  
history_pnl | string | Optional | readOnly: true | Total realized PnL from closed positions  
last_close_pnl | string | Optional | readOnly: true | PNL of last position close  
realised_point | string | Optional | readOnly: true | Realized POINT PNL  
history_point | string | Optional | readOnly: true | History realized POINT PNL  
adl_ranking | integer | Optional | readOnly: true | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
pending_orders | integer | Optional | readOnly: true | Current pending order quantity  
close_order | object|null | Optional | nullable: true  
readOnly: true | Current close order information, or `null` if no close order  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
cross_leverage_limit | string | Optional |  | Cross margin leverage (valid only when `leverage` is 0)  
update_time | integer(int64) | Optional | readOnly: true | Last update time  
update_id | integer(int64) | Optional | readOnly: true | Update ID. The value increments by 1 each time the position is updated  
open_time | integer(int64) | Optional |  | First Open Time  
risk_limit_table | string | Optional | readOnly: true | Risk limit table ID  
average_maintenance_rate | string | Optional | readOnly: true | Average maintenance margin rate  
  
**close_order**

Current close order information, or `null` if no close order

Type | Constraints  
---|---  
object|null | nullable: true  
readOnly: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order ID  
price | string | Optional |  | Order price  
is_liq | boolean | Optional |  | Whether the close order is from liquidation  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | DeliveryPosition  
  
### Response Schema

Status Code **200**

Futures position details

Type | Constraints  
---|---  
DeliveryPosition |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | User ID  
contract | string | Optional | readOnly: true | Futures contract  
size | integer(int64) | Optional | readOnly: true | Position size  
leverage | string | Optional |  | Position leverage. 0 means cross margin; positive number means isolated margin  
risk_limit | string | Optional |  | Position risk limit  
leverage_max | string | Optional | readOnly: true | Maximum leverage under current risk limit  
maintenance_rate | string | Optional | readOnly: true | The maintenance margin rate of the first tier of risk limit sheet  
value | string | Optional | readOnly: true | Position value calculated in settlement currency  
margin | string | Optional |  | Margin  
entry_price | string | Optional | readOnly: true | Entry price  
liq_price | string | Optional | readOnly: true | Liquidation price  
mark_price | string | Optional | readOnly: true | Current mark price  
initial_margin | string | Optional | readOnly: true | The initial margin occupied by the position, applicable to the portfolio margin account  
maintenance_margin | string | Optional | readOnly: true | Maintenance margin required for the position, applicable to portfolio margin account  
unrealised_pnl | string | Optional | readOnly: true | Unrealized PNL  
realised_pnl | string | Optional | readOnly: true | Realized PnL  
pnl_pnl | string | Optional | readOnly: true | Realized PNL - Position P/L  
pnl_fund | string | Optional | readOnly: true | Realized PNL - Funding Fees  
pnl_fee | string | Optional | readOnly: true | Realized PNL - Transaction Fees  
history_pnl | string | Optional | readOnly: true | Total realized PnL from closed positions  
last_close_pnl | string | Optional | readOnly: true | PNL of last position close  
realised_point | string | Optional | readOnly: true | Realized POINT PNL  
history_point | string | Optional | readOnly: true | History realized POINT PNL  
adl_ranking | integer | Optional | readOnly: true | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
pending_orders | integer | Optional | readOnly: true | Current pending order quantity  
close_order | object|null | Optional | nullable: true  
readOnly: true | Current close order information, or `null` if no close order  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
cross_leverage_limit | string | Optional |  | Cross margin leverage (valid only when `leverage` is 0)  
update_time | integer(int64) | Optional | readOnly: true | Last update time  
update_id | integer(int64) | Optional | readOnly: true | Update ID. The value increments by 1 each time the position is updated  
open_time | integer(int64) | Optional |  | First Open Time  
risk_limit_table | string | Optional | readOnly: true | Risk limit table ID  
average_maintenance_rate | string | Optional | readOnly: true | Average maintenance margin rate  
  
**close_order**

Current close order information, or `null` if no close order

Type | Constraints  
---|---  
object|null | nullable: true  
readOnly: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order ID  
price | string | Optional |  | Order price  
is_liq | boolean | Optional |  | Whether the close order is from liquidation  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Position information | DeliveryPosition  
  
### Response Schema

Status Code **200**

Futures position details

Type | Constraints  
---|---  
DeliveryPosition |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | User ID  
contract | string | Optional | readOnly: true | Futures contract  
size | integer(int64) | Optional | readOnly: true | Position size  
leverage | string | Optional |  | Position leverage. 0 means cross margin; positive number means isolated margin  
risk_limit | string | Optional |  | Position risk limit  
leverage_max | string | Optional | readOnly: true | Maximum leverage under current risk limit  
maintenance_rate | string | Optional | readOnly: true | The maintenance margin rate of the first tier of risk limit sheet  
value | string | Optional | readOnly: true | Position value calculated in settlement currency  
margin | string | Optional |  | Margin  
entry_price | string | Optional | readOnly: true | Entry price  
liq_price | string | Optional | readOnly: true | Liquidation price  
mark_price | string | Optional | readOnly: true | Current mark price  
initial_margin | string | Optional | readOnly: true | The initial margin occupied by the position, applicable to the portfolio margin account  
maintenance_margin | string | Optional | readOnly: true | Maintenance margin required for the position, applicable to portfolio margin account  
unrealised_pnl | string | Optional | readOnly: true | Unrealized PNL  
realised_pnl | string | Optional | readOnly: true | Realized PnL  
pnl_pnl | string | Optional | readOnly: true | Realized PNL - Position P/L  
pnl_fund | string | Optional | readOnly: true | Realized PNL - Funding Fees  
pnl_fee | string | Optional | readOnly: true | Realized PNL - Transaction Fees  
history_pnl | string | Optional | readOnly: true | Total realized PnL from closed positions  
last_close_pnl | string | Optional | readOnly: true | PNL of last position close  
realised_point | string | Optional | readOnly: true | Realized POINT PNL  
history_point | string | Optional | readOnly: true | History realized POINT PNL  
adl_ranking | integer | Optional | readOnly: true | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
pending_orders | integer | Optional | readOnly: true | Current pending order quantity  
close_order | object|null | Optional | nullable: true  
readOnly: true | Current close order information, or `null` if no close order  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
cross_leverage_limit | string | Optional |  | Cross margin leverage (valid only when `leverage` is 0)  
update_time | integer(int64) | Optional | readOnly: true | Last update time  
update_id | integer(int64) | Optional | readOnly: true | Update ID. The value increments by 1 each time the position is updated  
open_time | integer(int64) | Optional |  | First Open Time  
risk_limit_table | string | Optional | readOnly: true | Risk limit table ID  
average_maintenance_rate | string | Optional | readOnly: true | Average maintenance margin rate  
  
**close_order**

Current close order information, or `null` if no close order

Type | Constraints  
---|---  
object|null | nullable: true  
readOnly: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order ID  
price | string | Optional |  | Order price  
is_liq | boolean | Optional |  | Whether the close order is from liquidation  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Futures order details

Type | Constraints  
---|---  
DeliveryOrder | required: ["contract","size"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Futures order ID  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Creation time of order  
finish_time | number(double) | Optional | readOnly: true | Order finished time. Not returned if order is open  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required |  | Futures contract  
size | integer(int64) | Required |  | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | integer(int64) | Optional |  | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Optional |  | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
close | boolean | Optional | default: false  
writeOnly: true | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
reduce_only | boolean | Optional | default: false  
writeOnly: true | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_liq | boolean | Optional | readOnly: true | Is the order for liquidation  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | integer(int64) | Optional | readOnly: true | Unfilled quantity  
fill_price | string | Optional | readOnly: true | Fill price  
text | string | Optional |  | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
tkfr | string | Optional | readOnly: true | Taker fee  
mkfr | string | Optional | readOnly: true | Maker fee  
refu | integer | Optional | readOnly: true | Referrer user ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
  
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
id | body | integer(int64) | Optional | Futures order ID  
user | body | integer | Optional | User ID  
create_time | body | number(double) | Optional | Creation time of order  
finish_time | body | number(double) | Optional | Order finished time. Not returned if order is open  
finish_as | body | string | Optional | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | body | string | Optional | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | body | string | Required | Futures contract  
size | body | integer(int64) | Required | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | body | integer(int64) | Optional | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | body | string | Optional | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
close | body | boolean | Optional | Set as `true` to close the position, with `size` set to 0  
is_close | body | boolean | Optional | Is the order to close position  
reduce_only | body | boolean | Optional | Set as `true` to be reduce-only order  
is_reduce_only | body | boolean | Optional | Is the order reduce-only  
is_liq | body | boolean | Optional | Is the order for liquidation  
tif | body | string | Optional | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | body | integer(int64) | Optional | Unfilled quantity  
fill_price | body | string | Optional | Fill price  
text | body | string | Optional | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
tkfr | body | string | Optional | Taker fee  
mkfr | body | string | Optional | Maker fee  
refu | body | integer | Optional | Referrer user ID  
auto_size | body | string | Optional | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | body | integer | Optional | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | body | string | Optional | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | body | string | Optional | The custom data that the user remarked when amending the order  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

** finish_as**: How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention

** status**: Order status  
  
\- `open`: Pending  
\- `finished`: Completed

** tif**: Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none

** text**: Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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

** stp_id**: Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`

** stp_act**: Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled

####  Enumerated Values

Enumerated ValuesParameter | Value  
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
settle | usdt  
  
####  Request Body Schema

Futures order details

Request Body SchemaType | Constraints  
---|---  
DeliveryOrder | required: ["contract","size"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Futures order ID  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Creation time of order  
finish_time | number(double) | Optional | readOnly: true | Order finished time. Not returned if order is open  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required |  | Futures contract  
size | integer(int64) | Required |  | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | integer(int64) | Optional |  | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Optional |  | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
close | boolean | Optional | default: false  
writeOnly: true | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
reduce_only | boolean | Optional | default: false  
writeOnly: true | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_liq | boolean | Optional | readOnly: true | Is the order for liquidation  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | integer(int64) | Optional | readOnly: true | Unfilled quantity  
fill_price | string | Optional | readOnly: true | Fill price  
text | string | Optional |  | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
tkfr | string | Optional | readOnly: true | Taker fee  
mkfr | string | Optional | readOnly: true | Maker fee  
refu | integer | Optional | readOnly: true | Referrer user ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order details | DeliveryOrder  
  
### Response Schema

Status Code **201**

Futures order details

Type | Constraints  
---|---  
DeliveryOrder | required: ["contract","size"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Futures order ID  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Creation time of order  
finish_time | number(double) | Optional | readOnly: true | Order finished time. Not returned if order is open  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required |  | Futures contract  
size | integer(int64) | Required |  | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | integer(int64) | Optional |  | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Optional |  | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
close | boolean | Optional | default: false  
writeOnly: true | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
reduce_only | boolean | Optional | default: false  
writeOnly: true | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_liq | boolean | Optional | readOnly: true | Is the order for liquidation  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | integer(int64) | Optional | readOnly: true | Unfilled quantity  
fill_price | string | Optional | readOnly: true | Fill price  
text | string | Optional |  | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
tkfr | string | Optional | readOnly: true | Taker fee  
mkfr | string | Optional | readOnly: true | Maker fee  
refu | integer | Optional | readOnly: true | Referrer user ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancellation successful | [DeliveryOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Futures order details

Type | Constraints  
---|---  
DeliveryOrder | required: ["contract","size"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Futures order ID  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Creation time of order  
finish_time | number(double) | Optional | readOnly: true | Order finished time. Not returned if order is open  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required |  | Futures contract  
size | integer(int64) | Required |  | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | integer(int64) | Optional |  | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Optional |  | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
close | boolean | Optional | default: false  
writeOnly: true | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
reduce_only | boolean | Optional | default: false  
writeOnly: true | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_liq | boolean | Optional | readOnly: true | Is the order for liquidation  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | integer(int64) | Optional | readOnly: true | Unfilled quantity  
fill_price | string | Optional | readOnly: true | Fill price  
text | string | Optional |  | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
tkfr | string | Optional | readOnly: true | Taker fee  
mkfr | string | Optional | readOnly: true | Maker fee  
refu | integer | Optional | readOnly: true | Referrer user ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order details | DeliveryOrder  
  
### Response Schema

Status Code **200**

Futures order details

Type | Constraints  
---|---  
DeliveryOrder | required: ["contract","size"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Futures order ID  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Creation time of order  
finish_time | number(double) | Optional | readOnly: true | Order finished time. Not returned if order is open  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required |  | Futures contract  
size | integer(int64) | Required |  | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | integer(int64) | Optional |  | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Optional |  | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
close | boolean | Optional | default: false  
writeOnly: true | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
reduce_only | boolean | Optional | default: false  
writeOnly: true | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_liq | boolean | Optional | readOnly: true | Is the order for liquidation  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | integer(int64) | Optional | readOnly: true | Unfilled quantity  
fill_price | string | Optional | readOnly: true | Fill price  
text | string | Optional |  | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
tkfr | string | Optional | readOnly: true | Taker fee  
mkfr | string | Optional | readOnly: true | Maker fee  
refu | integer | Optional | readOnly: true | Referrer user ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order details | DeliveryOrder  
  
### Response Schema

Status Code **200**

Futures order details

Type | Constraints  
---|---  
DeliveryOrder | required: ["contract","size"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Futures order ID  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Creation time of order  
finish_time | number(double) | Optional | readOnly: true | Order finished time. Not returned if order is open  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required |  | Futures contract  
size | integer(int64) | Required |  | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | integer(int64) | Optional |  | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Optional |  | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
close | boolean | Optional | default: false  
writeOnly: true | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
reduce_only | boolean | Optional | default: false  
writeOnly: true | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_liq | boolean | Optional | readOnly: true | Is the order for liquidation  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | integer(int64) | Optional | readOnly: true | Unfilled quantity  
fill_price | string | Optional | readOnly: true | Fill price  
text | string | Optional |  | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
tkfr | string | Optional | readOnly: true | Taker fee  
mkfr | string | Optional | readOnly: true | Maker fee  
refu | integer | Optional | readOnly: true | Referrer user ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryMyTrade]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DeliveryMyTrade |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Fill ID  
create_time | number(double) | Optional |  | Fill Time  
contract | string | Optional |  | Futures contract  
order_id | string | Optional |  | Related order ID  
size | integer(int64) | Optional |  | Trading size  
close_size | integer(int64) | Optional |  | Number of closed positions:  
  
close_size=0 && size＞0 Open long position  
close_size=0 && size＜0 Open short position  
close_size>0 && size>0 && size <= close_size Close short position  
close_size>0 && size>0 && size > close_size Close short position and open long position  
close_size<0 && size<0 && size >= close_size Close long position  
close_size<0 && size<0 && size < close_size Close long position and open short position  
price | string | Optional |  | Fill Price  
role | string | Optional | enum: ["taker","maker"] | Trade role. taker - taker, maker - maker  
text | string | Optional |  | Order custom information  
fee | string | Optional |  | Trade fee  
point_fee | string | Optional |  | Points used to deduct trade fee  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryPositionClose]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DeliveryPositionClose |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | number(double) | Optional | readOnly: true | Position close time  
contract | string | Optional | readOnly: true | Futures contract  
side | string | Optional | enum: ["long","short"]  
readOnly: true | Position side  
  
\- `long`: Long position  
\- `short`: Short position  
pnl | string | Optional | readOnly: true | PnL  
pnl_pnl | string | Optional | readOnly: true | PNL - Position P/L  
pnl_fund | string | Optional | readOnly: true | PNL - Funding Fees  
pnl_fee | string | Optional | readOnly: true | PNL - Transaction Fees  
text | string | Optional | readOnly: true | Source of close order. See `order.text` field for specific values  
max_size | integer(int64) | Optional | readOnly: true | Max Trade Size  
accum_size | integer(int64) | Optional | readOnly: true | Cumulative closed position volume  
first_open_time | integer(int64) | Optional | readOnly: true | First Open Time  
long_price | string | Optional | readOnly: true | When side is 'long', it indicates the opening average price; when side is 'short', it indicates the closing average price  
short_price | string | Optional | readOnly: true | When side is 'long', it indicates the closing average price; when side is 'short', it indicates the opening average price  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliveryLiquidate]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DeliveryLiquidate |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | Liquidation time  
contract | string | Optional | readOnly: true | Futures contract  
leverage | string | Optional | readOnly: true | Position leverage. Not returned in public endpoints  
size | integer(int64) | Optional | readOnly: true | Position size  
margin | string | Optional | readOnly: true | Position margin. Not returned in public endpoints  
entry_price | string | Optional | readOnly: true | Average entry price. Not returned in public endpoints  
liq_price | string | Optional | readOnly: true | Liquidation price. Not returned in public endpoints  
mark_price | string | Optional | readOnly: true | Mark price. Not returned in public endpoints  
order_id | integer(int64) | Optional | readOnly: true | Liquidation order ID. Not returned in public endpoints  
order_price | string | Optional | readOnly: true | Liquidation order price  
fill_price | string | Optional | readOnly: true | Liquidation order average taker price  
left | integer(int64) | Optional | readOnly: true | Liquidation order maker size  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DeliverySettlement]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DeliverySettlement |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | Liquidation time  
contract | string | Optional | readOnly: true | Futures contract  
leverage | string | Optional | readOnly: true | Leverage multiplier  
size | integer(int64) | Optional | readOnly: true | Position size  
margin | string | Optional | readOnly: true | Margin  
entry_price | string | Optional | readOnly: true | Average entry price  
settle_price | string | Optional | readOnly: true | Settled price  
profit | string | Optional | readOnly: true | Profit  
fee | string | Optional | readOnly: true | Fee deducted  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [DeliveryLimitRiskTiers]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Retrieve risk limit configurations for different tiers under a specified contract

Type | Constraints  
---|---  
DeliveryLimitRiskTiers |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
tier | integer(int) | Optional |  | Tier  
risk_limit | string | Optional |  | Position risk limit  
initial_rate | string | Optional |  | Initial margin rate  
maintenance_rate | string | Optional |  | The maintenance margin rate of the first tier of risk limit sheet  
leverage_max | string | Optional |  | Maximum leverage  
contract | string | Optional |  | Market, only visible when market pagination is requested  
deduction | string | Optional |  | Maintenance margin quick calculation deduction amount  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FuturesPriceTriggeredOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Futures price-triggered order details

Type | Constraints  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
id_string | string | Optional | readOnly: true | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Created time  
finish_time | number(double) | Optional | readOnly: true | End time  
trade_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
order_type | string | Optional |  | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
me_order_id | integer(int64) | Optional | readOnly: true | Corresponding order ID for order take-profit/stop-loss orders  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
**items / initial**

Type | Constraints  
---|---  
object | required: ["contract","price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
contract | string | Required |  | Futures contract  
size | integer(int64) | Optional |  | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
amount | string | Optional |  | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
price | string | Required |  | Order price. Set to 0 to use market price  
close | boolean | Optional | default: false  
writeOnly: true | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
reduce_only | boolean | Optional | default: false | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
auto_size | string | Optional | writeOnly: true | One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
  
**items / trigger**

Type | Constraints  
---|---  
object | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
price_type | integer(int32) | Optional | enum: [0,1,2] | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
price | string | Required |  | Price value for price trigger, or spread value for spread trigger  
rule | integer(int32) | Required | enum: [1,2] | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
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
initial | body | object | Required | none  
» contract | body | string | Required | Futures contract  
» size | body | integer(int64) | Optional | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
» amount | body | string | Optional | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
» price | body | string | Required | Order price. Set to 0 to use market price  
» close | body | boolean | Optional | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
» tif | body | string | Optional | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
» text | body | string | Optional | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
» reduce_only | body | boolean | Optional | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
» auto_size | body | string | Optional | One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required  
» is_reduce_only | body | boolean | Optional | Is the order reduce-only  
» is_close | body | boolean | Optional | Is the order to close position  
trigger | body | object | Required | none  
» strategy_type | body | integer(int32) | Optional | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
» price_type | body | integer(int32) | Optional | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
» price | body | string | Required | Price value for price trigger, or spread value for spread trigger  
» rule | body | integer(int32) | Required | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
» expiration | body | integer | Optional | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
id | body | integer(int64) | Optional | Auto order ID  
id_string | body | string | Optional | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
user | body | integer | Optional | User ID  
create_time | body | number(double) | Optional | Created time  
finish_time | body | number(double) | Optional | End time  
trade_id | body | integer(int64) | Optional | ID of the order created after trigger  
status | body | string | Optional | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
finish_as | body | string | Optional | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
reason | body | string | Optional | Additional description of how the order was completed  
order_type | body | string | Optional | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
me_order_id | body | integer(int64) | Optional | Corresponding order ID for order take-profit/stop-loss orders  
pos_margin_mode | body | string | Optional | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
settle | path | string | Required | Settle currency  
  
####  Detailed descriptions

**» size** : Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0

**» close** : When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.

**» tif** : Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled

**» text** : The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app

**» auto_size** : One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required

**» strategy_type** : Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)

**» rule** : Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price

** id_string**: String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.

** status**: Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss

** order_type**: Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests

** pos_margin_mode**: Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» tif | gtc  
» tif | ioc  
» strategy_type | 0  
» strategy_type | 1  
» price_type | 0  
» price_type | 1  
» price_type | 2  
» rule | 1  
» rule | 2  
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
settle | usdt  
  
####  Request Body Schema

Futures price-triggered order details

Request Body SchemaType | Constraints  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
id_string | string | Optional | readOnly: true | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Created time  
finish_time | number(double) | Optional | readOnly: true | End time  
trade_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
order_type | string | Optional |  | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
me_order_id | integer(int64) | Optional | readOnly: true | Corresponding order ID for order take-profit/stop-loss orders  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
**initial**

Request Body SchemaType | Constraints  
---|---  
object | required: ["contract","price"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
contract | string | Required |  | Futures contract  
size | integer(int64) | Optional |  | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
amount | string | Optional |  | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
price | string | Required |  | Order price. Set to 0 to use market price  
close | boolean | Optional | default: false  
writeOnly: true | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
reduce_only | boolean | Optional | default: false | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
auto_size | string | Optional | writeOnly: true | One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
  
**trigger**

Request Body SchemaType | Constraints  
---|---  
object | required: ["price","rule"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
price_type | integer(int32) | Optional | enum: [0,1,2] | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
price | string | Required |  | Price value for price trigger, or spread value for spread trigger  
rule | integer(int32) | Required | enum: [1,2] | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order created successfully | TriggerOrderResponse  
  
### Response Schema

Status Code **201**

TriggerOrderResponse

Type | Constraints  
---|---  
TriggerOrderResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Auto order ID  
id_string | string | Optional | readOnly: true | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancel request is received and processed. Success is determined based on the order list | [FuturesPriceTriggeredOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Futures price-triggered order details

Type | Constraints  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
id_string | string | Optional | readOnly: true | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Created time  
finish_time | number(double) | Optional | readOnly: true | End time  
trade_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
order_type | string | Optional |  | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
me_order_id | integer(int64) | Optional | readOnly: true | Corresponding order ID for order take-profit/stop-loss orders  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
**items / initial**

Type | Constraints  
---|---  
object | required: ["contract","price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
contract | string | Required |  | Futures contract  
size | integer(int64) | Optional |  | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
amount | string | Optional |  | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
price | string | Required |  | Order price. Set to 0 to use market price  
close | boolean | Optional | default: false  
writeOnly: true | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
reduce_only | boolean | Optional | default: false | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
auto_size | string | Optional | writeOnly: true | One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
  
**items / trigger**

Type | Constraints  
---|---  
object | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
price_type | integer(int32) | Optional | enum: [0,1,2] | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
price | string | Required |  | Price value for price trigger, or spread value for spread trigger  
rule | integer(int32) | Required | enum: [1,2] | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Auto order details | FuturesPriceTriggeredOrder  
  
### Response Schema

Status Code **200**

Futures price-triggered order details

Type | Constraints  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
id_string | string | Optional | readOnly: true | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Created time  
finish_time | number(double) | Optional | readOnly: true | End time  
trade_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
order_type | string | Optional |  | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
me_order_id | integer(int64) | Optional | readOnly: true | Corresponding order ID for order take-profit/stop-loss orders  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
**initial**

Type | Constraints  
---|---  
object | required: ["contract","price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
contract | string | Required |  | Futures contract  
size | integer(int64) | Optional |  | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
amount | string | Optional |  | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
price | string | Required |  | Order price. Set to 0 to use market price  
close | boolean | Optional | default: false  
writeOnly: true | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
reduce_only | boolean | Optional | default: false | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
auto_size | string | Optional | writeOnly: true | One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
  
**trigger**

Type | Constraints  
---|---  
object | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
price_type | integer(int32) | Optional | enum: [0,1,2] | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
price | string | Required |  | Price value for price trigger, or spread value for spread trigger  
rule | integer(int32) | Required | enum: [1,2] | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Auto order details | FuturesPriceTriggeredOrder  
  
### Response Schema

Status Code **200**

Futures price-triggered order details

Type | Constraints  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
id_string | string | Optional | readOnly: true | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Created time  
finish_time | number(double) | Optional | readOnly: true | End time  
trade_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
order_type | string | Optional |  | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
me_order_id | integer(int64) | Optional | readOnly: true | Corresponding order ID for order take-profit/stop-loss orders  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
**initial**

Type | Constraints  
---|---  
object | required: ["contract","price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
contract | string | Required |  | Futures contract  
size | integer(int64) | Optional |  | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
amount | string | Optional |  | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
price | string | Required |  | Order price. Set to 0 to use market price  
close | boolean | Optional | default: false  
writeOnly: true | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
reduce_only | boolean | Optional | default: false | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
auto_size | string | Optional | writeOnly: true | One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
  
**trigger**

Type | Constraints  
---|---  
object | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
price_type | integer(int32) | Optional | enum: [0,1,2] | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
price | string | Required |  | Price value for price trigger, or spread value for spread trigger  
rule | integer(int32) | Required | enum: [1,2] | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
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

##  DeliveryPositionClose

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | number(double) | Optional | readOnly: true | Position close time  
contract | string | Optional | readOnly: true | Futures contract  
side | string | Optional | enum: ["long","short"]  
readOnly: true | Position side  
  
\- `long`: Long position  
\- `short`: Short position  
pnl | string | Optional | readOnly: true | PnL  
pnl_pnl | string | Optional | readOnly: true | PNL - Position P/L  
pnl_fund | string | Optional | readOnly: true | PNL - Funding Fees  
pnl_fee | string | Optional | readOnly: true | PNL - Transaction Fees  
text | string | Optional | readOnly: true | Source of close order. See `order.text` field for specific values  
max_size | integer(int64) | Optional | readOnly: true | Max Trade Size  
accum_size | integer(int64) | Optional | readOnly: true | Cumulative closed position volume  
first_open_time | integer(int64) | Optional | readOnly: true | First Open Time  
long_price | string | Optional | readOnly: true | When side is 'long', it indicates the opening average price; when side is 'short', it indicates the closing average price  
short_price | string | Optional | readOnly: true | When side is 'long', it indicates the closing average price; when side is 'short', it indicates the opening average price  
      
    
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
    
    

##  DeliveryTrade

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Fill ID  
create_time | number(double) | Optional |  | Fill Time  
create_time_ms | number(double) | Optional |  | Trade time, with millisecond precision to 3 decimal places  
contract | string | Optional |  | Futures contract  
size | integer(int64) | Optional |  | Trading size  
price | string | Optional |  | Trade price (quote currency)  
is_internal | boolean | Optional |  | Deprecated  
      
    
    {
      "id": 0,
      "create_time": 0,
      "create_time_ms": 0,
      "contract": "string",
      "size": 0,
      "price": "string",
      "is_internal": true
    }
    
    

##  DeliveryMyTrade

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Fill ID  
create_time | number(double) | Optional |  | Fill Time  
contract | string | Optional |  | Futures contract  
order_id | string | Optional |  | Related order ID  
size | integer(int64) | Optional |  | Trading size  
close_size | integer(int64) | Optional |  | Number of closed positions:  
  
close_size=0 && size＞0 Open long position  
close_size=0 && size＜0 Open short position  
close_size>0 && size>0 && size <= close_size Close short position  
close_size>0 && size>0 && size > close_size Close short position and open long position  
close_size<0 && size<0 && size >= close_size Close long position  
close_size<0 && size<0 && size < close_size Close long position and open short position  
price | string | Optional |  | Fill Price  
role | string | Optional | enum: ["taker","maker"] | Trade role. taker - taker, maker - maker  
text | string | Optional |  | Order custom information  
fee | string | Optional |  | Trade fee  
point_fee | string | Optional |  | Points used to deduct trade fee  
      
    
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
    
    

##  DeliverySettlement

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | Liquidation time  
contract | string | Optional | readOnly: true | Futures contract  
leverage | string | Optional | readOnly: true | Leverage multiplier  
size | integer(int64) | Optional | readOnly: true | Position size  
margin | string | Optional | readOnly: true | Margin  
entry_price | string | Optional | readOnly: true | Average entry price  
settle_price | string | Optional | readOnly: true | Settled price  
profit | string | Optional | readOnly: true | Profit  
fee | string | Optional | readOnly: true | Fee deducted  
      
    
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
    
    

##  InsuranceRecord

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
t | integer(int64) | Optional |  | Unix timestamp in seconds  
b | string | Optional |  | Insurance balance  
      
    
    {
      "t": 0,
      "b": "string"
    }
    
    

##  FuturesPriceTriggeredOrder

Futures price-triggered order details

Type | Constraints  
---|---  
object | required: ["initial","trigger"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
id_string | string | Optional | readOnly: true | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Created time  
finish_time | number(double) | Optional | readOnly: true | End time  
trade_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | Order status  
  
\- `open`: Active  
\- `finished`: Finished  
\- `inactive`: Inactive, only applies to order take-profit/stop-loss  
\- `invalid`: Invalid, only applies to order take-profit/stop-loss  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
order_type | string | Optional |  | Types of take-profit and stop-loss orders, including:  
  
\- `close-long-order`: Order take-profit/stop-loss, close long position  
\- `close-short-order`: Order take-profit/stop-loss, close short position  
\- `close-long-position`: Position take-profit/stop-loss, used to close all long positions  
\- `close-short-position`: Position take-profit/stop-loss, used to close all short positions  
\- `plan-close-long-position`: Position plan take-profit/stop-loss, used to close all or partial long positions  
\- `plan-close-short-position`: Position plan take-profit/stop-loss, used to close all or partial short positions  
  
The two types of order take-profit/stop-loss are read-only and cannot be passed in requests  
me_order_id | integer(int64) | Optional | readOnly: true | Corresponding order ID for order take-profit/stop-loss orders  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | Position margin mode: `isolated` (isolated margin) or `cross` (cross margin).  
Returned by the server in simple split-position mode; when writing, use only the values below.  
  
**initial**

Type | Constraints  
---|---  
object | required: ["contract","price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
contract | string | Required |  | Futures contract  
size | integer(int64) | Optional |  | Represents the number of contracts that need to be closed, full closing: size=0  
Partial closing: plan-close-short-position size>0   
Partial closing: plan-close-long-position size<0  
amount | string | Optional |  | Same as `size`; used for decimal contract size. When both `size` and `amount` are provided, `amount` takes precedence.  
price | string | Required |  | Order price. Set to 0 to use market price  
close | boolean | Optional | default: false  
writeOnly: true | When fully closing a position in single-position mode, close must be set to true to execute the close operation.  
When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false.  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force strategy, default is gtc, market orders currently only support ioc mode  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
reduce_only | boolean | Optional | default: false | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions  
auto_size | string | Optional | writeOnly: true | One-way Mode: auto_size is not required  
Hedge Mode full closing (size=0): auto_size must be set, close_long for closing long positions, close_short for closing short positions  
Hedge Mode partial closing (size≠0): auto_size is not required  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
  
**trigger**

Type | Constraints  
---|---  
object | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | Trigger Strategy  
  
\- 0: Price trigger, triggered when price meets conditions  
\- 1: Price spread trigger, i.e. the difference between the latest price specified in `price_type` and the second-last price  
Currently only supports 0 (latest transaction price)  
price_type | integer(int32) | Optional | enum: [0,1,2] | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price  
price | string | Required |  | Price value for price trigger, or spread value for spread trigger  
rule | integer(int32) | Required | enum: [1,2] | Price Condition Type  
  
\- 1: Trigger when the price calculated based on `strategy_type` and `price_type` is greater than or equal to `Trigger.Price`, while Trigger.Price must > last_price  
\- 2: Trigger when the price calculated based on `strategy_type` and `price_type` is less than or equal to `Trigger.Price`, and Trigger.Price must < last_price  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
      
    
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
    
    

##  DeliveryLimitRiskTiers

Retrieve risk limit configurations for different tiers under a specified contract

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
tier | integer(int) | Optional |  | Tier  
risk_limit | string | Optional |  | Position risk limit  
initial_rate | string | Optional |  | Initial margin rate  
maintenance_rate | string | Optional |  | The maintenance margin rate of the first tier of risk limit sheet  
leverage_max | string | Optional |  | Maximum leverage  
contract | string | Optional |  | Market, only visible when market pagination is requested  
deduction | string | Optional |  | Maintenance margin quick calculation deduction amount  
      
    
    {
      "tier": 0,
      "risk_limit": "string",
      "initial_rate": "string",
      "maintenance_rate": "string",
      "leverage_max": "string",
      "contract": "string",
      "deduction": "string"
    }
    
    

##  DeliveryOrderBook

Type | Constraints  
---|---  
object | required: ["asks","bids"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order Book ID. Increases by 1 on every order book change. Set `with_id=true` to include this field in response  
current | number(double) | Optional |  | Response data generation timestamp  
update | number(double) | Optional |  | Order book changed timestamp  
asks | array | Required |  | Ask Depth  
bids | array | Required |  | Bid Depth  
  
**asks**

Ask Depth

Type | Constraints  
---|---  
array |   
  
**asks / items**

DeliveryOrderBookItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
p | string | Optional |  | Price (quote currency)  
s | integer(int64) | Optional |  | Size  
  
**bids**

Bid Depth

Type | Constraints  
---|---  
array |   
  
**bids / items**

DeliveryOrderBookItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
p | string | Optional |  | Price (quote currency)  
s | integer(int64) | Optional |  | Size  
      
    
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
    
    

##  DeliveryAccount

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | string | Optional |  | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional |  | Unrealized PNL  
position_margin | string | Optional |  | Deprecated  
order_margin | string | Optional |  | initial margin of all open orders  
available | string | Optional |  | Available amount for transfer or trading, which includes credit limits under the unified account (includes experience funds; experience funds cannot be transferred, so when transferring, the transfer amount must deduct experience funds)  
point | string | Optional |  | Point card amount  
currency | string | Optional |  | Settlement currency  
in_dual_mode | boolean | Optional |  | Whether Hedge Mode is enabled  
enable_credit | boolean | Optional |  | Whether portfolio margin account mode is enabled  
position_initial_margin | string | Optional |  | Initial margin occupied by positions, applicable to unified account mode  
maintenance_margin | string | Optional |  | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode  
bonus | string | Optional |  | Bonus  
enable_evolved_classic | boolean | Optional |  | Deprecated  
cross_order_margin | string | Optional |  | Cross margin order margin, applicable to new classic account margin mode  
cross_initial_margin | string | Optional |  | Cross margin initial margin, applicable to new classic account margin mode  
cross_maintenance_margin | string | Optional |  | Cross margin maintenance margin, applicable to new classic account margin mode  
cross_unrealised_pnl | string | Optional |  | Cross margin unrealized P&L, applicable to new classic account margin mode  
cross_available | string | Optional |  | Cross margin available balance, applicable to new classic account margin mode  
cross_margin_balance | string | Optional |  | Cross margin balance, applicable to new classic account margin mode  
cross_mmr | string | Optional |  | Cross margin maintenance margin rate, applicable to new classic account margin mode  
cross_imr | string | Optional |  | Cross margin initial margin rate, applicable to new classic account margin mode  
isolated_position_margin | string | Optional |  | Isolated position margin, applicable to new classic account margin mode  
enable_new_dual_mode | boolean | Optional |  | Deprecated  
margin_mode | integer | Optional |  | Margin mode of the account  
0: classic future account or Classic Spot Margin Mode of unified account;  
1: Multi-Currency Margin Mode;  
2: Portoforlio Margin Mode;  
3: Single-Currency Margin Mode  
enable_tiered_mm | boolean | Optional |  | Whether to enable tiered maintenance margin calculation  
history | object | Optional |  | Statistical data  
  
**history**

Statistical data

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
dnw | string | Optional |  | total amount of deposit and withdraw  
pnl | string | Optional |  | total amount of trading profit and loss  
fee | string | Optional |  | total amount of fee  
refr | string | Optional |  | total amount of referrer rebates  
fund | string | Optional |  | total amount of funding costs  
point_dnw | string | Optional |  | total amount of point deposit and withdraw  
point_fee | string | Optional |  | total amount of point fee  
point_refr | string | Optional |  | total amount of referrer rebates of point fee  
bonus_dnw | string | Optional |  | total amount of perpetual contract bonus transfer  
bonus_offset | string | Optional |  | total amount of perpetual contract bonus deduction  
      
    
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
    
    

##  DeliveryLiquidate

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | Liquidation time  
contract | string | Optional | readOnly: true | Futures contract  
leverage | string | Optional | readOnly: true | Position leverage. Not returned in public endpoints  
size | integer(int64) | Optional | readOnly: true | Position size  
margin | string | Optional | readOnly: true | Position margin. Not returned in public endpoints  
entry_price | string | Optional | readOnly: true | Average entry price. Not returned in public endpoints  
liq_price | string | Optional | readOnly: true | Liquidation price. Not returned in public endpoints  
mark_price | string | Optional | readOnly: true | Mark price. Not returned in public endpoints  
order_id | integer(int64) | Optional | readOnly: true | Liquidation order ID. Not returned in public endpoints  
order_price | string | Optional | readOnly: true | Liquidation order price  
fill_price | string | Optional | readOnly: true | Liquidation order average taker price  
left | integer(int64) | Optional | readOnly: true | Liquidation order maker size  
      
    
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
    
    

##  TriggerOrderResponse

TriggerOrderResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Auto order ID  
id_string | string | Optional | readOnly: true | String form of the auto order ID; the same order as numeric `id`, as the decimal string of `id` to avoid int64 precision loss in JavaScript and similar environments.  
Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with `id`. Same meaning as the field of the same name in futures price-trigger REST APIs and in `futures.orders` / `futures.autoorders` WebSocket pushes.  
      
    
    {
      "id": 0,
      "id_string": "string"
    }
    
    

##  DeliveryPosition

Futures position details

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | User ID  
contract | string | Optional | readOnly: true | Futures contract  
size | integer(int64) | Optional | readOnly: true | Position size  
leverage | string | Optional |  | Position leverage. 0 means cross margin; positive number means isolated margin  
risk_limit | string | Optional |  | Position risk limit  
leverage_max | string | Optional | readOnly: true | Maximum leverage under current risk limit  
maintenance_rate | string | Optional | readOnly: true | The maintenance margin rate of the first tier of risk limit sheet  
value | string | Optional | readOnly: true | Position value calculated in settlement currency  
margin | string | Optional |  | Margin  
entry_price | string | Optional | readOnly: true | Entry price  
liq_price | string | Optional | readOnly: true | Liquidation price  
mark_price | string | Optional | readOnly: true | Current mark price  
initial_margin | string | Optional | readOnly: true | The initial margin occupied by the position, applicable to the portfolio margin account  
maintenance_margin | string | Optional | readOnly: true | Maintenance margin required for the position, applicable to portfolio margin account  
unrealised_pnl | string | Optional | readOnly: true | Unrealized PNL  
realised_pnl | string | Optional | readOnly: true | Realized PnL  
pnl_pnl | string | Optional | readOnly: true | Realized PNL - Position P/L  
pnl_fund | string | Optional | readOnly: true | Realized PNL - Funding Fees  
pnl_fee | string | Optional | readOnly: true | Realized PNL - Transaction Fees  
history_pnl | string | Optional | readOnly: true | Total realized PnL from closed positions  
last_close_pnl | string | Optional | readOnly: true | PNL of last position close  
realised_point | string | Optional | readOnly: true | Realized POINT PNL  
history_point | string | Optional | readOnly: true | History realized POINT PNL  
adl_ranking | integer | Optional | readOnly: true | Ranking of auto deleveraging, a total of 1-5 grades, `1` is the highest, `5` is the lowest, and `6` is the special case when there is no position held or in liquidation  
pending_orders | integer | Optional | readOnly: true | Current pending order quantity  
close_order | object|null | Optional | nullable: true  
readOnly: true | Current close order information, or `null` if no close order  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | Position mode, including:  
  
\- `single`: One-way Mode  
\- `dual_long`: Long position in Hedge Mode  
\- `dual_short`: Short position in Hedge Mode  
cross_leverage_limit | string | Optional |  | Cross margin leverage (valid only when `leverage` is 0)  
update_time | integer(int64) | Optional | readOnly: true | Last update time  
update_id | integer(int64) | Optional | readOnly: true | Update ID. The value increments by 1 each time the position is updated  
open_time | integer(int64) | Optional |  | First Open Time  
risk_limit_table | string | Optional | readOnly: true | Risk limit table ID  
average_maintenance_rate | string | Optional | readOnly: true | Average maintenance margin rate  
  
**close_order**

Current close order information, or `null` if no close order

Type | Constraints  
---|---  
object|null | nullable: true  
readOnly: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order ID  
price | string | Optional |  | Order price  
is_liq | boolean | Optional |  | Whether the close order is from liquidation  
      
    
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
    
    

##  DeliveryContract

Futures contract details

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Optional |  | Futures contract  
underlying | string | Optional |  | Underlying  
cycle | string | Optional | enum: ["WEEKLY","BI-WEEKLY","QUARTERLY","BI-QUARTERLY"] | Cycle type, e.g. WEEKLY, QUARTERLY  
type | string | Optional | enum: ["inverse","direct"] | Contract type: inverse - inverse contract, direct - direct contract  
quanto_multiplier | string | Optional |  | The contract multiplier indicates how many units of the underlying asset the face value of one contract represents.  
leverage_min | string | Optional |  | Minimum leverage  
leverage_max | string | Optional |  | Maximum leverage  
maintenance_rate | string | Optional |  | The maintenance margin rate of the first tier of risk limit sheet  
mark_type | string | Optional | enum: ["internal","index"] | Deprecated  
mark_price | string | Optional |  | Current mark price  
index_price | string | Optional |  | Current index price  
last_price | string | Optional |  | Last trading price  
maker_fee_rate | string | Optional |  | Maker fee rate, negative values indicate rebates  
taker_fee_rate | string | Optional |  | Taker fee rate  
order_price_round | string | Optional |  | Minimum order price increment  
mark_price_round | string | Optional |  | Minimum mark price increment  
basis_rate | string | Optional |  | Fair basis rate  
basis_value | string | Optional |  | Fair basis value  
basis_impact_value | string | Optional |  | Funding used for calculating impact bid, ask price  
settle_price | string | Optional |  | Settle price  
settle_price_interval | integer | Optional |  | Settle price update interval  
settle_price_duration | integer | Optional |  | Settle price update duration in seconds  
expire_time | integer(int64) | Optional |  | Contract expiry timestamp  
risk_limit_base | string | Optional |  | Risk limit base  
risk_limit_step | string | Optional |  | Step of adjusting risk limit  
risk_limit_max | string | Optional |  | Maximum risk limit the contract allowed  
order_size_min | integer(int64) | Optional |  | Minimum order quantity  
order_size_max | integer(int64) | Optional |  | Maximum order quantity  
order_price_deviate | string | Optional |  | Maximum allowed deviation between order price and current mark price. The order price `order_price` must satisfy the following condition:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | Optional |  | Trading fee discount for referred users  
ref_rebate_rate | string | Optional |  | Commission rate for referrers  
orderbook_id | integer(int64) | Optional |  | Orderbook update ID  
trade_id | integer(int64) | Optional |  | Current trade ID  
trade_size | integer(int64) | Optional |  | Historical cumulative trading volume  
position_size | integer(int64) | Optional |  | Current total long position size  
config_change_time | number(double) | Optional |  | Last configuration update time  
in_delisting | boolean | Optional |  | Contract is delisting  
orders_limit | integer | Optional |  | Maximum number of pending orders  
      
    
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
    
    

##  DeliveryTicker

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
contract | string | Optional |  | Futures contract  
last | string | Optional |  | Last trading price  
change_percentage | string | Optional |  | Price change percentage. Negative values indicate price decrease, e.g. -7.45  
total_size | string | Optional |  | Contract total size  
low_24h | string | Optional |  | 24-hour lowest price  
high_24h | string | Optional |  | 24-hour highest price  
volume_24h | string | Optional |  | 24-hour trading volume  
volume_24h_btc | string | Optional |  | 24-hour trading volume in BTC (deprecated, use `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle` instead)  
volume_24h_usd | string | Optional |  | 24-hour trading volume in USD (deprecated, use `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle` instead)  
volume_24h_base | string | Optional |  | 24-hour trading volume in base currency  
volume_24h_quote | string | Optional |  | 24-hour trading volume in quote currency  
volume_24h_settle | string | Optional |  | 24-hour trading volume in settle currency  
mark_price | string | Optional |  | Recent mark price  
funding_rate | string | Optional |  | Funding rate  
funding_rate_indicative | string | Optional |  | Indicative Funding rate in next period. (deprecated. use `funding_rate`)  
index_price | string | Optional |  | Index price  
quanto_base_rate | string | Optional |  | Deprecated  
basis_rate | string | Optional |  | Basis rate  
basis_value | string | Optional |  | Basis value  
lowest_ask | string | Optional |  | Recent lowest ask  
lowest_size | string | Optional |  | The latest seller's lowest price order quantity  
highest_bid | string | Optional |  | Recent highest bid  
highest_size | string | Optional |  | The latest buyer's highest price order volume  
      
    
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
    
    

##  DeliveryCandlestick

data point in every timestamp

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
t | number(double) | Optional |  | Unix timestamp in seconds  
v | integer(int64) | Optional |  | size volume (contract size). Only returned if `contract` is not prefixed  
c | string | Optional |  | Close price (quote currency)  
h | string | Optional |  | Highest price (quote currency)  
l | string | Optional |  | Lowest price (quote currency)  
o | string | Optional |  | Open price (quote currency)  
      
    
    {
      "t": 0,
      "v": 0,
      "c": "string",
      "h": "string",
      "l": "string",
      "o": "string"
    }
    
    

##  DeliveryAccountBook

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | number(double) | Optional |  | Change time  
change | string | Optional |  | Change amount  
balance | string | Optional |  | Balance after change  
type | string | Optional | enum: ["dnw","pnl","fee","refr","fund","point_dnw","point_fee","point_refr","bonus_offset"] | Change types:  
  
\- dnw: Deposit and withdrawal  
\- pnl: Profit and loss from position reduction  
\- fee: Trading fees  
\- refr: Referrer rebates  
\- fund: Funding fees  
\- point_dnw: Point card deposit and withdrawal  
\- point_fee: Point card trading fees  
\- point_refr: Point card referrer rebates  
\- bonus_offset: Trial fund deduction  
text | string | Optional |  | Comment  
contract | string | Optional |  | Futures contract, the field is only available for data after 2023-10-30  
trade_id | string | Optional |  | trade id  
id | string | Optional |  | Account change record ID  
      
    
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
    
    

##  DeliveryOrder

Futures order details

Type | Constraints  
---|---  
object | required: ["contract","size"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Futures order ID  
user | integer | Optional | readOnly: true | User ID  
create_time | number(double) | Optional | readOnly: true | Creation time of order  
finish_time | number(double) | Optional | readOnly: true | Order finished time. Not returned if order is open  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | How the order was finished:  
  
\- filled: all filled  
\- cancelled: manually cancelled  
\- liquidated: cancelled because of liquidation  
\- ioc: time in force is `IOC`, finish immediately  
\- auto_deleveraged: finished by ADL  
\- reduce_only: cancelled because of increasing position while `reduce-only` set  
\- position_closed: cancelled because the position was closed  
\- reduce_out: only reduce positions by excluding hard-to-fill orders  
\- stp: cancelled because self trade prevention  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | Order status  
  
\- `open`: Pending  
\- `finished`: Completed  
contract | string | Required |  | Futures contract  
size | integer(int64) | Required |  | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders.  
iceberg | integer(int64) | Optional |  | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees.  
price | string | Optional |  | Order price. Price of 0 with `tif` set to `ioc` represents a market order.  
close | boolean | Optional | default: false  
writeOnly: true | Set as `true` to close the position, with `size` set to 0  
is_close | boolean | Optional | readOnly: true | Is the order to close position  
reduce_only | boolean | Optional | default: false  
writeOnly: true | Set as `true` to be reduce-only order  
is_reduce_only | boolean | Optional | readOnly: true | Is the order reduce-only  
is_liq | boolean | Optional | readOnly: true | Is the order for liquidation  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
left | integer(int64) | Optional | readOnly: true | Unfilled quantity  
fill_price | string | Optional | readOnly: true | Fill price  
text | string | Optional |  | Order Custom Information: Users can set custom IDs via this field. Custom fields must meet the following conditions:  
  
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
tkfr | string | Optional | readOnly: true | Taker fee  
mkfr | string | Optional | readOnly: true | Maker fee  
refu | integer | Optional | readOnly: true | Referrer user ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
      
    
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