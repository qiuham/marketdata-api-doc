---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/spot
api_type: Trading
updated_at: 2026-11-21 18:58:08.682942
---

# Spot

Spot trading

##  Query all currency information

GET`/spot/currencies`

GET `/spot/currencies`

_Query all currency information_

When a currency is associated with multiple blockchains, use `chains` to view information about each chain, such as deposit and withdrawal status and chain identifiers.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Currency]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
Currency |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency | string | Optional |  | Currency symbol  
name | string | Optional |  | Currency name  
delisted | boolean | Optional |  | Whether currency is de-listed  
withdraw_disabled | boolean | Optional |  | Whether currency's withdrawal is disabled (deprecated)  
withdraw_delayed | boolean | Optional |  | Whether currency's withdrawal is delayed (deprecated)  
deposit_disabled | boolean | Optional |  | Whether currency's deposit is disabled (deprecated)  
trade_disabled | boolean | Optional |  | Whether currency's trading is disabled  
fixed_rate | string | Optional |  | Fixed fee rate. Only for fixed rate currencies, not valid for normal currencies  
chain | string | Optional |  | The main chain corresponding to the coin  
chains | array | Optional |  | All blockchains associated with this currency.  
total_supply | string | Optional |  | Total supply  
market_cap | string | Optional |  | Market cap  
category | array | Optional |  | Currency categories  
\- stocks: Stocks  
\- metals: Metals  
\- indices: Indices  
\- forex: Forex  
\- commodities: Commodities  
  
**items / chains**

All blockchains associated with this currency.

Type | Constraints  
---|---  
array |   
  
**items / chains / items**

SpotCurrencyChain

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Optional |  | Blockchain name  
addr | string | Optional |  | token address  
withdraw_disabled | boolean | Optional |  | Whether currency's withdrawal is disabled  
withdraw_delayed | boolean | Optional |  | Whether currency's withdrawal is delayed  
deposit_disabled | boolean | Optional |  | Whether currency's deposit is disabled  
  
**items / category**

Currency categories

  * stocks: Stocks
  * metals: Metals
  * indices: Indices
  * forex: Forex
  * commodities: Commodities

Type | Constraints  
---|---  
array |   
  
**items / category / items**

Type | Constraints  
---|---  
string |   
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/currencies'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/currencies \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency": "GT",
        "name": "GateToken",
        "delisted": false,
        "withdraw_disabled": false,
        "withdraw_delayed": false,
        "deposit_disabled": false,
        "trade_disabled": false,
        "chain": "GT",
        "chains": [
          {
            "name": "GT",
            "addr": "",
            "withdraw_disabled": false,
            "withdraw_delayed": false,
            "deposit_disabled": false
          },
          {
            "name": "ETH",
            "withdraw_disabled": false,
            "withdraw_delayed": false,
            "deposit_disabled": false,
            "addr": "0xE66747a101bFF2dBA3697199DCcE5b743b454759"
          },
          {
            "name": "GTEVM",
            "withdraw_disabled": false,
            "withdraw_delayed": false,
            "deposit_disabled": false,
            "addr": ""
          }
        ],
        "total_supply": "2100000",
        "market_cap": "18880000",
        "category": []
      }
    ]
    

##  Query single currency information

GET`/spot/currencies/{currency}`

GET `/spot/currencies/{currency}`

_Query single currency information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | path | any | Required | Currency name  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Currency  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
Currency |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency | string | Optional |  | Currency symbol  
name | string | Optional |  | Currency name  
delisted | boolean | Optional |  | Whether currency is de-listed  
withdraw_disabled | boolean | Optional |  | Whether currency's withdrawal is disabled (deprecated)  
withdraw_delayed | boolean | Optional |  | Whether currency's withdrawal is delayed (deprecated)  
deposit_disabled | boolean | Optional |  | Whether currency's deposit is disabled (deprecated)  
trade_disabled | boolean | Optional |  | Whether currency's trading is disabled  
fixed_rate | string | Optional |  | Fixed fee rate. Only for fixed rate currencies, not valid for normal currencies  
chain | string | Optional |  | The main chain corresponding to the coin  
chains | array | Optional |  | All blockchains associated with this currency.  
total_supply | string | Optional |  | Total supply  
market_cap | string | Optional |  | Market cap  
category | array | Optional |  | Currency categories  
\- stocks: Stocks  
\- metals: Metals  
\- indices: Indices  
\- forex: Forex  
\- commodities: Commodities  
  
**chains**

All blockchains associated with this currency.

Type | Constraints  
---|---  
array |   
  
**chains / items**

SpotCurrencyChain

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Optional |  | Blockchain name  
addr | string | Optional |  | token address  
withdraw_disabled | boolean | Optional |  | Whether currency's withdrawal is disabled  
withdraw_delayed | boolean | Optional |  | Whether currency's withdrawal is delayed  
deposit_disabled | boolean | Optional |  | Whether currency's deposit is disabled  
  
**category**

Currency categories

  * stocks: Stocks
  * metals: Metals
  * indices: Indices
  * forex: Forex
  * commodities: Commodities

Type | Constraints  
---|---  
array |   
  
**category / items**

Type | Constraints  
---|---  
string |   
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/currencies/GT'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/currencies/GT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "currency": "GT",
      "name": "GateToken",
      "delisted": false,
      "withdraw_disabled": false,
      "withdraw_delayed": false,
      "deposit_disabled": false,
      "trade_disabled": false,
      "chain": "GT",
      "chains": [
        {
          "name": "GT",
          "addr": "",
          "withdraw_disabled": false,
          "withdraw_delayed": false,
          "deposit_disabled": false
        },
        {
          "name": "ETH",
          "withdraw_disabled": false,
          "withdraw_delayed": false,
          "deposit_disabled": false,
          "addr": "0xE66747a101bFF2dBA3697199DCcE5b743b454759"
        },
        {
          "name": "GTEVM",
          "withdraw_disabled": false,
          "withdraw_delayed": false,
          "deposit_disabled": false,
          "addr": ""
        }
      ],
      "total_supply": "2100000",
      "market_cap": "18880000",
      "category": []
    }
    

##  Query all supported currency pairs

GET`/spot/currency_pairs`

GET `/spot/currency_pairs`

_Query all supported currency pairs_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | All currency pairs retrieved | [CurrencyPair]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Spot currency pair

Type | Constraints  
---|---  
CurrencyPair |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Currency pair  
base | string | Optional |  | Base currency  
base_name | string | Optional |  | Base currency name  
quote | string | Optional |  | Quote currency  
quote_name | string | Optional |  | Quote currency name  
trade_quotes | array|null | Optional | nullable: true | Quote currencies supported by the unified market; null means that the market does not support unified quote currencies  
fee | string | Optional |  | Trading fee rate(deprecated)  
min_base_amount | string | Optional |  | Minimum amount of base currency to trade, `null` means no limit  
min_quote_amount | string | Optional |  | Minimum amount of quote currency to trade, `null` means no limit  
max_base_amount | string | Optional |  | Maximum amount of base currency to trade, `null` means no limit  
max_quote_amount | string | Optional |  | Maximum amount of quote currency to trade, `null` means no limit  
amount_precision | integer | Optional |  | Quantity precision  
precision | integer | Optional |  | Price precision  
trade_status | string | Optional | enum: ["untradable","buyable","sellable","tradable"] | Trading status  
  
\- untradable: cannot be traded  
\- buyable: can be bought  
\- sellable: can be sold  
\- tradable: can be bought and sold  
sell_start | integer(int64) | Optional |  | Sell start unix timestamp in seconds  
buy_start | integer(int64) | Optional |  | Buy start unix timestamp in seconds  
delisting_time | integer(int64) | Optional |  | Expected delisting time as a Unix timestamp in seconds.  
type | string | Optional |  | Trading pair type, normal: normal, premarket: pre-market  
trade_url | string | Optional |  | Transaction link  
st_tag | boolean | Optional |  | Whether the trading pair is in ST risk assessment, false - No, true - Yes  
up_rate | string | Optional |  | Maximum Quote Rise Percentage  
down_rate | string | Optional |  | Maximum Quote Decline Percentage  
slippage | string | Optional |  | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
market_order_max_stock | string | Optional |  | Maximum market order quantity. `null` or `0` means no limit  
market_order_max_money | string | Optional |  | Maximum market order amount. `null` or `0` means no limit  
  
**items / trade_quotes**

Quote currencies supported by the unified market; null means that the market does not support unified quote currencies

Type | Constraints  
---|---  
array|null | nullable: true  
  
**items / trade_quotes / items**

Type | Constraints  
---|---  
string |   
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/currency_pairs'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/currency_pairs \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": "ETH_USDT",
        "base": "ETH",
        "base_name": "Ethereum",
        "quote": "USDT",
        "quote_name": "Tether",
        "trade_quotes": [
          "USDC",
          "RLUSD"
        ],
        "fee": "0.2",
        "min_base_amount": "0.001",
        "min_quote_amount": "1.0",
        "max_base_amount": "10000",
        "max_quote_amount": "10000000",
        "amount_precision": 3,
        "precision": 6,
        "trade_status": "tradable",
        "sell_start": 1516378650,
        "buy_start": 1516378650,
        "delisting_time": 0,
        "type": "normal",
        "trade_url": "https://www.gate.io/trade/ETH_USDT",
        "st_tag": false,
        "up_rate": "0.05",
        "down_rate": "0.02",
        "slippage": "0.05",
        "market_order_max_stock": "100000",
        "market_order_max_money": "1000000"
      }
    ]
    

##  Query single currency pair details

GET`/spot/currency_pairs/{currency_pair}`

GET `/spot/currency_pairs/{currency_pair}`

_Query single currency pair details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | path | string | Required | Currency pair  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | CurrencyPair  
  
### Response Schema

Status Code **200**

Spot currency pair

Type | Constraints  
---|---  
CurrencyPair |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Currency pair  
base | string | Optional |  | Base currency  
base_name | string | Optional |  | Base currency name  
quote | string | Optional |  | Quote currency  
quote_name | string | Optional |  | Quote currency name  
trade_quotes | array|null | Optional | nullable: true | Quote currencies supported by the unified market; null means that the market does not support unified quote currencies  
fee | string | Optional |  | Trading fee rate(deprecated)  
min_base_amount | string | Optional |  | Minimum amount of base currency to trade, `null` means no limit  
min_quote_amount | string | Optional |  | Minimum amount of quote currency to trade, `null` means no limit  
max_base_amount | string | Optional |  | Maximum amount of base currency to trade, `null` means no limit  
max_quote_amount | string | Optional |  | Maximum amount of quote currency to trade, `null` means no limit  
amount_precision | integer | Optional |  | Quantity precision  
precision | integer | Optional |  | Price precision  
trade_status | string | Optional | enum: ["untradable","buyable","sellable","tradable"] | Trading status  
  
\- untradable: cannot be traded  
\- buyable: can be bought  
\- sellable: can be sold  
\- tradable: can be bought and sold  
sell_start | integer(int64) | Optional |  | Sell start unix timestamp in seconds  
buy_start | integer(int64) | Optional |  | Buy start unix timestamp in seconds  
delisting_time | integer(int64) | Optional |  | Expected delisting time as a Unix timestamp in seconds.  
type | string | Optional |  | Trading pair type, normal: normal, premarket: pre-market  
trade_url | string | Optional |  | Transaction link  
st_tag | boolean | Optional |  | Whether the trading pair is in ST risk assessment, false - No, true - Yes  
up_rate | string | Optional |  | Maximum Quote Rise Percentage  
down_rate | string | Optional |  | Maximum Quote Decline Percentage  
slippage | string | Optional |  | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
market_order_max_stock | string | Optional |  | Maximum market order quantity. `null` or `0` means no limit  
market_order_max_money | string | Optional |  | Maximum market order amount. `null` or `0` means no limit  
  
**trade_quotes**

Quote currencies supported by the unified market; null means that the market does not support unified quote currencies

Type | Constraints  
---|---  
array|null | nullable: true  
  
**trade_quotes / items**

Type | Constraints  
---|---  
string |   
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/currency_pairs/ETH_BTC'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/currency_pairs/ETH_BTC \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "id": "ETH_USDT",
      "base": "ETH",
      "base_name": "Ethereum",
      "quote": "USDT",
      "quote_name": "Tether",
      "trade_quotes": [
        "USDC",
        "RLUSD"
      ],
      "fee": "0.2",
      "min_base_amount": "0.001",
      "min_quote_amount": "1.0",
      "max_base_amount": "10000",
      "max_quote_amount": "10000000",
      "amount_precision": 3,
      "precision": 6,
      "trade_status": "tradable",
      "sell_start": 1516378650,
      "buy_start": 1516378650,
      "delisting_time": 0,
      "type": "normal",
      "trade_url": "https://www.gate.io/trade/ETH_USDT",
      "st_tag": false,
      "up_rate": "0.05",
      "down_rate": "0.02",
      "slippage": "0.05",
      "market_order_max_stock": "100000",
      "market_order_max_money": "1000000"
    }
    

##  Get currency pair ticker information

GET`/spot/tickers`

GET `/spot/tickers`

_Get currency pair ticker information_

If `currency_pair` is specified, only query that currency pair; otherwise return all information

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Currency pair  
timezone | query | string | Optional | Timezone  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
timezone | utc0  
timezone | utc8  
timezone | all  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [Ticker]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
Ticker |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
last | string | Optional |  | Last trading price  
lowest_ask | string | Optional |  | Recent lowest ask  
lowest_size | string | Optional |  | Latest seller's lowest price quantity; not available for batch queries; available for single queries, empty if no data  
highest_bid | string | Optional |  | Recent highest bid  
highest_size | string | Optional |  | Latest buyer's highest price quantity; not available for batch queries; available for single queries, empty if no data  
change_percentage | string | Optional |  | 24h price change percentage (negative for decrease, e.g., -7.45)  
change_utc0 | string | Optional |  | UTC+0 timezone, 24h price change percentage, negative for decline (e.g., -7.45)  
change_utc8 | string | Optional |  | UTC+8 timezone, 24h price change percentage, negative for decline (e.g., -7.45)  
base_volume | string | Optional |  | Base currency trading volume in the last 24h  
quote_volume | string | Optional |  | Quote currency trading volume in the last 24h  
high_24h | string | Optional |  | 24h High  
low_24h | string | Optional |  | 24h Low  
etf_net_value | string | Optional |  | ETF net value  
etf_pre_net_value | string|null | Optional | nullable: true | ETF net value at previous rebalancing point  
etf_pre_timestamp | integer(int64)|null | Optional | nullable: true | ETF previous rebalancing time  
etf_leverage | string|null | Optional | nullable: true | ETF current leverage  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/tickers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/tickers \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency_pair": "BTC3L_USDT",
        "last": "2.46140352",
        "lowest_ask": "2.477",
        "highest_bid": "2.4606821",
        "change_percentage": "-8.91",
        "change_utc0": "-8.91",
        "change_utc8": "-8.91",
        "base_volume": "656614.0845820589",
        "quote_volume": "1602221.66468375534639404191",
        "high_24h": "2.7431",
        "low_24h": "1.9863",
        "etf_net_value": "2.46316141",
        "etf_pre_net_value": "2.43201848",
        "etf_pre_timestamp": 1611244800,
        "etf_leverage": "2.2803019447281203"
      }
    ]
    

##  Get market depth information

GET`/spot/order_book`

GET `/spot/order_book`

_Get market depth information_

Market depth buy orders are sorted by price from high to low, sell orders are reversed

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Required | Currency pair  
interval | query | string | Optional | Price precision for merged depth. 0 means no merging. If not specified, defaults to 0  
limit | query | integer | Optional | Number of depth levels  
with_id | query | boolean | Optional | Return order book update ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OrderBook  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
OrderBook | required: ["asks","bids"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order book ID, which is updated whenever the order book is changed. Valid only when `with_id` is set to `true`  
current | integer(int64) | Optional |  | The timestamp of the response data being generated (in milliseconds)  
update | integer(int64) | Optional |  | The timestamp of when the orderbook last changed (in milliseconds)  
asks | array | Required |  | Ask Depth  
bids | array | Required |  | Bid Depth  
  
**asks**

Ask Depth

Type | Constraints  
---|---  
array |   
  
**asks / items**

Price and Quantity Pair

Type | Constraints  
---|---  
array | minItems: 2  
maxItems: 2  
  
**asks / items / items**

Type | Constraints  
---|---  
string |   
  
**bids**

Bid Depth

Type | Constraints  
---|---  
array |   
  
**bids / items**

Price and Quantity Pair

Type | Constraints  
---|---  
array | minItems: 2  
maxItems: 2  
  
**bids / items / items**

Type | Constraints  
---|---  
string |   
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/order_book'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/order_book?currency_pair=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "id": 123456,
      "current": 1623898993123,
      "update": 1623898993121,
      "asks": [
        [
          "1.52",
          "1.151"
        ],
        [
          "1.53",
          "1.218"
        ]
      ],
      "bids": [
        [
          "1.17",
          "201.863"
        ],
        [
          "1.16",
          "725.464"
        ]
      ]
    }
    

##  Get the RPI order book

GET`/spot/rpi_order_book`

GET `/spot/rpi_order_book`

_Get the RPI order book_

Get the RPI order book, with bids sorted by descending price and asks by ascending price.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Required | Currency pair  
interval | query | string | Optional | Price precision for merged depth. 0 means no merging. If not specified, defaults to 0  
limit | query | integer | Optional | Number of depth levels  
with_id | query | boolean | Optional | Return order book update ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OrderBook  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
OrderBook | required: ["asks","bids"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order book ID, which is updated whenever the order book is changed. Valid only when `with_id` is set to `true`  
current | integer(int64) | Optional |  | The timestamp of the response data being generated (in milliseconds)  
update | integer(int64) | Optional |  | The timestamp of when the orderbook last changed (in milliseconds)  
asks | array | Required |  | Ask Depth  
bids | array | Required |  | Bid Depth  
  
**asks**

Ask Depth

Type | Constraints  
---|---  
array |   
  
**asks / items**

Price and Quantity Pair

Type | Constraints  
---|---  
array | minItems: 2  
maxItems: 2  
  
**asks / items / items**

Type | Constraints  
---|---  
string |   
  
**bids**

Bid Depth

Type | Constraints  
---|---  
array |   
  
**bids / items**

Price and Quantity Pair

Type | Constraints  
---|---  
array | minItems: 2  
maxItems: 2  
  
**bids / items / items**

Type | Constraints  
---|---  
string |   
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/rpi_order_book'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/rpi_order_book?currency_pair=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "id": 123456,
      "current": 1623898993123,
      "update": 1623898993121,
      "asks": [
        [
          "1.52",
          "1.151"
        ],
        [
          "1.53",
          "1.218"
        ]
      ],
      "bids": [
        [
          "1.17",
          "201.863"
        ],
        [
          "1.16",
          "725.464"
        ]
      ]
    }
    

##  Query market transaction records

GET`/spot/trades`

GET `/spot/trades`

_Query market transaction records_

Supports querying by time range using `from` and `to` parameters or pagination based on `last_id`. By default, queries the last 30 days.

Pagination based on `last_id` is no longer recommended. If `last_id` is specified, the time range query parameters will be ignored.

When using limit&page pagination to retrieve data, the maximum number of pages is 100,000, that is, limit * (page - 1) <= 100,000.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Required | Currency pair  
limit | query | integer(int32) | Optional | Maximum number of items returned in list. Default: 100, minimum: 1, maximum: 1000  
last_id | query | string | Optional | Use the ID of the last record in the previous list as the starting point for the next list  
  
Operations based on custom IDs can only be checked when orders are pending. After orders are completed (filled/cancelled), they can be checked within 1 hour after completion. After expiration, only order IDs can be used  
reverse | query | boolean | Optional | Whether to retrieve data less than `last_id`. Default returns records greater than `last_id`.  
  
Set to `true` to trace back market trade records, `false` to get latest trades.  
  
No effect when `last_id` is not set.  
from | query | integer(int64) | Optional | Start timestamp for the query  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
page | query | integer(int32) | Optional | Page number  
  
####  Detailed descriptions

**last_id** : Use the ID of the last record in the previous list as the starting point for the next list  
  
Operations based on custom IDs can only be checked when orders are pending. After orders are completed (filled/cancelled), they can be checked within 1 hour after completion. After expiration, only order IDs can be used

**reverse** : Whether to retrieve data less than `last_id`. Default returns records greater than `last_id`.  
  
Set to `true` to trace back market trade records, `false` to get latest trades.  
  
No effect when `last_id` is not set.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Trade]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
Trade |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Fill ID  
create_time | string | Optional |  | Fill Time  
create_time_ms | string | Optional |  | Trading time, with millisecond precision  
currency_pair | string | Optional |  | Currency pair  
side | string | Optional | enum: ["buy","sell"] | Buy or sell order  
role | string | Optional | enum: ["taker","maker"] | Trade role, not returned in public endpoints  
amount | string | Optional |  | Trade amount  
price | string | Optional |  | Trade price.  
order_id | string | Optional |  | Related order ID, not returned in public endpoints  
fee | string | Optional |  | Fee deducted, not returned in public endpoints  
fee_currency | string | Optional |  | Fee currency unit, not returned in public endpoints  
point_fee | string | Optional |  | Points used to deduct fee, not returned in public endpoints  
gt_fee | string | Optional |  | GT used to deduct fee, not returned in public endpoints  
amend_text | string | Optional |  | The custom data that the user remarked when amending the order  
sequence_id | string | Optional |  | Consecutive trade ID within a single market.  
Used to track and identify trades in the specific market  
text | string | Optional |  | Order's Custom Information. This field is not returned by public interfaces.  
The scenarios pm_liquidate, comb_margin_liquidate, and scm_liquidate represent full-account forced liquidation orders.  
liquidate represents isolated-account forced liquidation orders.  
deal | string | Optional |  | Total Executed Value  
trade_quote | string | Optional |  | Actual quote currency used for the trade  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/trades'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/trades?currency_pair=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": "1232893232",
        "create_time": "1548000000",
        "create_time_ms": "1548000000123.456",
        "currency_pair": "BTC_USDT",
        "order_id": "4128442423",
        "side": "buy",
        "role": "maker",
        "amount": "0.15",
        "price": "0.03",
        "fee": "0.0005",
        "fee_currency": "ETH",
        "point_fee": "0",
        "gt_fee": "0",
        "sequence_id": "588018",
        "text": "t-test",
        "deal": "0.0045",
        "trade_quote": "USDC"
      }
    ]
    

##  Market K-line chart

GET`/spot/candlesticks`

GET `/spot/candlesticks`

_Market K-line chart_

K-line chart data returns a maximum of 1000 points per request. When specifying from, to, and interval, ensure the number of points is not excessive

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Required | Currency pair  
limit | query | integer | Optional | Maximum number of recent data points to return. `limit` conflicts with `from` and `to`. If either `from` or `to` is specified, request will be rejected.  
from | query | integer(int64) | Optional | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified  
to | query | integer(int64) | Optional | Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision  
interval | query | string | Optional | Time interval between data points. Note that `30d` represents a calendar month, not aligned to 30 days  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
interval | 1s  
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
interval | 30d  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [[string]]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Candlestick data for each time granularity, from left to right:

  * Unix timestamp with second precision
  * Trading volume in quote currency
  * Closing price
  * Highest price
  * Lowest price
  * Opening price
  * Trading volume in base currency
  * Whether window is closed; true means this candlestick data segment is complete, false means not yet complete

Type | Constraints  
---|---  
array | minItems: 6  
  
**items / items**

Type | Constraints  
---|---  
string |   
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/candlesticks'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      [
        "1539852480",
        "971519.677",
        "0.0021724",
        "0.0021922",
        "0.0021724",
        "0.0021737",
        "true"
      ]
    ]
    

##  Query account fee rates🔒 Authenticated

GET`/spot/fee`

GET `/spot/fee`

_Query account fee rates_

This API is deprecated. The new fee query API is `/wallet/fee`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Specify currency pair to get more accurate fee settings.  
  
This field is optional. Usually fee settings are the same for all currency pairs.  
  
####  Detailed descriptions

**currency_pair** : Specify currency pair to get more accurate fee settings.  
  
This field is optional. Usually fee settings are the same for all currency pairs.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | SpotFee  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
SpotFee |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | User ID  
taker_fee | string | Optional |  | taker fee rate  
maker_fee | string | Optional |  | maker fee rate  
rpi_maker_fee | string | Optional |  | RPI MM maker fee rate  
gt_discount | boolean | Optional |  | Whether GT deduction discount is enabled  
gt_taker_fee | string | Optional |  | Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  
gt_maker_fee | string | Optional |  | Maker fee rate with GT deduction. Returns 0 if GT deduction is disabled  
loan_fee | string | Optional |  | Loan fee rate of margin lending  
point_type | string | Optional |  | Point card type: 0 - Original version, 1 - New version since 202009  
currency_pair | string | Optional |  | Currency pair  
debit_fee | integer | Optional |  | Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  
rpi_mm | integer | Optional |  | RPI MM Level  
  
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
    
    url = '/spot/fee'
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
    url="/spot/fee"
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
      "user_id": 10001,
      "taker_fee": "0.002",
      "maker_fee": "0.002",
      "gt_discount": false,
      "gt_taker_fee": "0",
      "gt_maker_fee": "0",
      "loan_fee": "0.18",
      "point_type": "1",
      "currency_pair": "BTC_USDT",
      "debit_fee": 3
    }
    

##  Batch query account fee rates🔒 Authenticated

GET`/spot/batch_fee`

GET `/spot/batch_fee`

_Batch query account fee rates_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pairs | query | string | Required | Maximum 50 currency pairs per request  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Inline  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
object |   
  
**additionalProperties**

Type | Constraints  
---|---  
SpotFee |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | User ID  
taker_fee | string | Optional |  | taker fee rate  
maker_fee | string | Optional |  | maker fee rate  
rpi_maker_fee | string | Optional |  | RPI MM maker fee rate  
gt_discount | boolean | Optional |  | Whether GT deduction discount is enabled  
gt_taker_fee | string | Optional |  | Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  
gt_maker_fee | string | Optional |  | Maker fee rate with GT deduction. Returns 0 if GT deduction is disabled  
loan_fee | string | Optional |  | Loan fee rate of margin lending  
point_type | string | Optional |  | Point card type: 0 - Original version, 1 - New version since 202009  
currency_pair | string | Optional |  | Currency pair  
debit_fee | integer | Optional |  | Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  
rpi_mm | integer | Optional |  | RPI MM Level  
  
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
    
    url = '/spot/batch_fee'
    query_param = 'currency_pairs=BTC_USDT,ETH_USDT'
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
    url="/spot/batch_fee"
    query_param="currency_pairs=BTC_USDT,ETH_USDT"
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
      "BTC_USDT": {
        "user_id": 10001,
        "taker_fee": "0.002",
        "maker_fee": "0.002",
        "rpi_maker_fee": "-0.00175",
        "gt_discount": false,
        "gt_taker_fee": "0",
        "gt_maker_fee": "0",
        "loan_fee": "0.18",
        "point_type": "1",
        "currency_pair": "BTC_USDT",
        "debit_fee": 3,
        "rpi_mm": 2
      },
      "GT_USDT": {
        "user_id": 10001,
        "taker_fee": "0.002",
        "maker_fee": "0.002",
        "rpi_maker_fee": "-0.00175",
        "gt_discount": false,
        "gt_taker_fee": "0",
        "gt_maker_fee": "0",
        "loan_fee": "0.18",
        "point_type": "1",
        "currency_pair": "GT_USDT",
        "debit_fee": 3,
        "rpi_mm": 2
      },
      "ETH_USDT": {
        "user_id": 10001,
        "taker_fee": "0.002",
        "maker_fee": "0.002",
        "rpi_maker_fee": "-0.00175",
        "gt_discount": false,
        "gt_taker_fee": "0",
        "gt_maker_fee": "0",
        "loan_fee": "0.18",
        "point_type": "1",
        "currency_pair": "ETH_USDT",
        "debit_fee": 3,
        "rpi_mm": 2
      }
    }
    

##  List spot trading accounts🔒 Authenticated

GET`/spot/accounts`

GET `/spot/accounts`

_List spot trading accounts_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SpotAccount]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
SpotAccount |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency | string | Optional |  | Currency detail  
available | string | Optional |  | Available amount  
locked | string | Optional |  | Locked amount, used in trading  
update_id | integer(int64) | Optional |  | Version number  
  
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
    
    url = '/spot/accounts'
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
    url="/spot/accounts"
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
        "currency": "ETH",
        "available": "968.8",
        "locked": "0",
        "update_id": 98
      }
    ]
    

##  Query spot account transaction history🔒 Authenticated

GET`/spot/account_book`

GET `/spot/account_book`

_Query spot account transaction history_

Record query time range cannot exceed 30 days.

When using limit&page pagination to retrieve data, the maximum number of pages is 100,000, that is, limit * (page - 1) <= 100,000.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
from | query | integer(int64) | Optional | Start timestamp for the query  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
page | query | integer(int32) | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
type | query | string | Optional | Query by specified account change type. If not specified, all change types will be included.  
code | query | string | Optional | Specify account change code for query. If not specified, all change types are included. This parameter has higher priority than `type`  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SpotAccountBook]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
SpotAccountBook |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Balance change record ID  
time | integer(int64) | Optional |  | The timestamp of the change (in milliseconds)  
currency | string | Optional |  | Currency changed  
change | string | Optional |  | Amount changed. Positive value means transferring in, while negative out  
balance | string | Optional |  | Balance after change  
type | string | Optional |  | Account change type; deprecated (see `code` for account change type encoding)  
code | string | Optional |  | Account change code, see [Asset Record Code] (Asset Record Code)  
text | string | Optional |  | Additional information  
  
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
    
    url = '/spot/account_book'
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
    url="/spot/account_book"
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
        "id": "123456",
        "time": 1547633726123,
        "currency": "BTC",
        "change": "1.03",
        "balance": "4.59316525194",
        "type": "margin_in",
        "text": "3815099"
      }
    ]
    

##  Batch place orders🔒 Authenticated

POST`/spot/batch_orders`

POST `/spot/batch_orders`

_Batch place orders_

Batch order requirements:

  1. Custom order field `text` must be specified
  2. Up to 4 currency pairs per request, with up to 10 orders per currency pair
  3. Spot orders and margin orders cannot be mixed; all `account` fields in the same request must be identical

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | array[Order] | Required | none  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
array |   
  
**items**

Spot order details

Request Body SchemaType | Constraints  
---|---  
Order | required: ["currency_pair","side","amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**items / stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Request Body SchemaType | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**items / stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Request Body SchemaType | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request execution completed | [BatchOrder]  
  
### Response Schema

Status Code **200**

Contains multiple order objects; for the specific structure of the order object, refer to the structure of the /spot/orders order placement interface

Type | Constraints  
---|---  
array |   
  
**items**

Batch order details

Type | Constraints  
---|---  
BatchOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID  
amend_text | string | Optional |  | The custom data that the user remarked when amending the order  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
succeeded | boolean | Optional |  | Request execution result  
label | string | Optional |  | Error label, if any, otherwise an empty string  
message | string | Optional |  | Detailed error message, if any, otherwise an empty string  
id | string | Optional | readOnly: true | Order ID  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
currency_pair | string | Optional |  | Currency pair  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | enum: ["spot","margin","cross_margin","unified"]  
default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Optional | enum: ["buy","sell"] | Buy or sell order  
amount | string | Optional |  | Trade amount  
price | string | Optional |  | Order price  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
iceberg | string | Optional |  | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  
  
1\. After users join the `STP Group`, he can pass `stp_act` to limit the user's self-trade prevetion strategy. If `stp_act` is not passed, the default is `cn` strategy。  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter。  
3\. If the user did not use 'stp_act' when placing the order, 'stp_act' will return '-'  
  
\- cn: Cancel newest, Cancel new orders and keep old ones  
\- co: Cancel oldest, new ones  
\- cb: Cancel both, Both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object | Optional |  | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object | Optional |  | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
  
**items / stop_profit**

PatchSpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**items / stop_loss**

PatchSpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
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
    
    url = '/spot/batch_orders'
    query_param = ''
    body='[{"text":"t-abc123","currency_pair":"BTC_USDT","trade_quote":"USDC","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"},"use_earn":false}]'
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
    url="/spot/batch_orders"
    query_param=""
    body_param='[{"text":"t-abc123","currency_pair":"BTC_USDT","trade_quote":"USDC","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"},"use_earn":false}]'
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
        "text": "t-abc123",
        "currency_pair": "BTC_USDT",
        "trade_quote": "USDC",
        "type": "limit",
        "account": "unified",
        "side": "buy",
        "amount": "0.001",
        "price": "65000",
        "time_in_force": "gtc",
        "iceberg": "0",
        "slippage": "0.05",
        "stop_profit": {
          "trigger_price": "67000",
          "order_price": "67000"
        },
        "stop_loss": {
          "trigger_price": "63000",
          "order_price": "63000"
        },
        "use_earn": false
      }
    ]
    

> Example responses

> 200 Response
    
    
    [
      {
        "order_id": "12332324",
        "amend_text": "t-123456",
        "text": "t-123456",
        "succeeded": true,
        "label": "",
        "message": "",
        "id": "12332324",
        "create_time": "1548000000",
        "update_time": "1548000100",
        "create_time_ms": 1548000000123,
        "update_time_ms": 1548000100123,
        "currency_pair": "ETC_BTC",
        "status": "cancelled",
        "type": "limit",
        "account": "spot",
        "side": "buy",
        "amount": "1",
        "price": "5.00032",
        "time_in_force": "gtc",
        "iceberg": "0",
        "left": "0.5",
        "filled_amount": "1.242",
        "filled_total": "2.50016",
        "avg_deal_price": "5.00032",
        "fee": "0.005",
        "fee_currency": "ETH",
        "point_fee": "0",
        "gt_fee": "0",
        "gt_discount": false,
        "rebated_fee": "0",
        "rebated_fee_currency": "BTC",
        "stp_act": "cn",
        "finish_as": "stp",
        "stp_id": 10240
      }
    ]
    

##  List all open orders🔒 Authenticated

GET`/spot/open_orders`

GET `/spot/open_orders`

_List all open orders_

Query the current order list of all trading pairs. Please note that the paging parameter controls the number of pending orders in each trading pair. There is no paging control trading pairs. All trading pairs with pending orders will be returned.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page | query | integer(int32) | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in one page in each currency pair  
account | query | string | Optional | Specify query account  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OpenOrders]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
OpenOrders |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
total | integer | Optional |  | Total number of open orders for this trading pair on the current page  
orders | array | Optional |  |   
  
**items / orders**

Type | Constraints  
---|---  
array |   
  
**items / orders / items**

Spot order details

Type | Constraints  
---|---  
object | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**items / orders / items / stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**items / orders / items / stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
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
    
    url = '/spot/open_orders'
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
    url="/spot/open_orders"
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
        "currency_pair": "ETH_BTC",
        "total": 1,
        "orders": [
          {
            "id": "12332324",
            "text": "t-123456",
            "create_time": "1548000000",
            "update_time": "1548000100",
            "currency_pair": "ETH_BTC",
            "status": "open",
            "type": "limit",
            "account": "spot",
            "side": "buy",
            "amount": "1",
            "price": "5.00032",
            "time_in_force": "gtc",
            "left": "0.5",
            "filled_total": "2.50016",
            "fee": "0.005",
            "fee_currency": "ETH",
            "point_fee": "0",
            "gt_fee": "0",
            "gt_discount": false,
            "rebated_fee": "0",
            "rebated_fee_currency": "BTC"
          }
        ]
      }
    ]
    

##  Close position when cross-currency is disabled🔒 Authenticated

POST`/spot/cross_liquidate_orders`

POST `/spot/cross_liquidate_orders`

_Close position when cross-currency is disabled_

Currently, only cross-margin accounts are supported to place buy orders for disabled currencies. Maximum buy quantity = (unpaid principal and interest - currency balance - the amount of the currency in pending orders) / 0.998

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | LiquidateOrder | Required | none  
text | body | string | Optional | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
currency_pair | body | string | Required | Currency pair  
amount | body | string | Required | Trade amount  
price | body | string | Required | Order price  
action_mode | body | string | Optional | Processing mode:  
  
Different fields are returned when placing an order based on action_mode. This field is only valid during the request and is not included in the response  
`ACK`: Asynchronous mode, only returns key order fields  
`RESULT`: No liquidation information  
`FULL`: Full mode (default)  
  
####  Detailed descriptions

** text**: Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  

** action_mode**: Processing mode:  
  
Different fields are returned when placing an order based on action_mode. This field is only valid during the request and is not included in the response  
`ACK`: Asynchronous mode, only returns key order fields  
`RESULT`: No liquidation information  
`FULL`: Full mode (default)

####  Request Body Schema

Spot liquidation order details

Request Body SchemaType | Constraints  
---|---  
LiquidateOrder | required: ["currency_pair","amount","price"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
currency_pair | string | Required |  | Currency pair  
amount | string | Required |  | Trade amount  
price | string | Required |  | Order price  
action_mode | string | Optional |  | Processing mode:  
  
Different fields are returned when placing an order based on action_mode. This field is only valid during the request and is not included in the response  
`ACK`: Asynchronous mode, only returns key order fields  
`RESULT`: No liquidation information  
`FULL`: Full mode (default)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order created successfully | Order  
  
### Response Schema

Status Code **201**

Spot order details

Type | Constraints  
---|---  
Order | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
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
    
    url = '/spot/cross_liquidate_orders'
    query_param = ''
    body='{"currency_pair":"GT_USDT","amount":"12","price":"10.15","text":"t-34535"}'
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
    url="/spot/cross_liquidate_orders"
    query_param=""
    body_param='{"currency_pair":"GT_USDT","amount":"12","price":"10.15","text":"t-34535"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "currency_pair": "GT_USDT",
      "amount": "12",
      "price": "10.15",
      "text": "t-34535"
    }
    

> Example responses

> 201 Response
    
    
    {
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "trade_quote": "USDC",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      },
      "use_earn": false
    }
    

##  List orders🔒 Authenticated

GET`/spot/orders`

GET `/spot/orders`

_List orders_

Note that query results default to spot order lists for spot, unified account, and isolated margin accounts.

When `status` is set to `open` (i.e., when querying pending order lists), only `page` and `limit` pagination controls are supported. `limit` can only be set to a maximum of 100. The `side` parameter and time range query parameters `from` and `to` are not supported.

When `status` is set to `finished` (i.e., when querying historical orders), in addition to pagination queries, `from` and `to` time range queries are also supported. Additionally, the `side` parameter can be set to filter one-sided history.

Time range filter parameters are processed according to the order end time.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Required | Query by specified currency pair. Required for open orders, optional for filled orders  
status | query | string | Required | List orders based on status  
  
`open` \- order is waiting to be filled  
`finished` \- order has been filled or cancelled  
  
page | query | integer(int32) | Optional | Page number  
limit | query | integer | Optional | Maximum number of records to be returned. If `status` is `open`, maximum of `limit` is 100  
account | query | string | Optional | Specify query account  
from | query | integer(int64) | Optional | Start timestamp for the query  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
side | query | string | Optional | Specify all bids or all asks, both included if not specified  
  
####  Detailed descriptions

**status** : List orders based on status  
  
`open` \- order is waiting to be filled  
`finished` \- order has been filled or cancelled  

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Order]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Spot order details

Type | Constraints  
---|---  
Order | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**items / stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**items / stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
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
    
    url = '/spot/orders'
    query_param = 'currency_pair=BTC_USDT&status=open'
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
    url="/spot/orders"
    query_param="currency_pair=BTC_USDT&status=open"
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
        "id": "1852454420",
        "text": "t-abc123",
        "amend_text": "-",
        "create_time": "1710488334",
        "update_time": "1710488334",
        "create_time_ms": 1710488334073,
        "update_time_ms": 1710488334074,
        "status": "closed",
        "currency_pair": "BTC_USDT",
        "trade_quote": "USDC",
        "type": "limit",
        "account": "unified",
        "side": "buy",
        "amount": "0.001",
        "price": "65000",
        "time_in_force": "gtc",
        "iceberg": "0",
        "left": "0",
        "filled_amount": "0.001",
        "fill_price": "63.4693",
        "filled_total": "63.4693",
        "avg_deal_price": "63469.3",
        "fee": "0.00000022",
        "fee_currency": "BTC",
        "point_fee": "0",
        "gt_fee": "0",
        "gt_maker_fee": "0",
        "gt_taker_fee": "0",
        "gt_discount": false,
        "rebated_fee": "0",
        "rebated_fee_currency": "USDT",
        "finish_as": "filled",
        "stop_profit": {
          "trigger_price": "67000",
          "order_price": "67000"
        },
        "stop_loss": {
          "trigger_price": "63000",
          "order_price": "63000"
        },
        "use_earn": false
      }
    ]
    

##  Create order🔒 Authenticated

POST`/spot/orders`

POST `/spot/orders`

_Create order_

Supports placing orders from spot, margin, leveraged, and cross-margin accounts. Use the `account` field to select the account type. The default is `spot`, which places an order from the spot account. For a `unified` account, orders use the unified account by default.

When trading with a margin account by setting `account` to `margin`, you can set `auto_borrow` to `true`. If the account balance is insufficient, the system automatically calls `POST /margin/uni/loans` to borrow the shortfall. Whether assets received from a filled margin order are automatically used to repay an isolated-margin loan depends on the automatic repayment setting of the user's isolated-margin **account**. Use `/margin/auto_repay` to query or update this account-level automatic repayment setting.

When trading with a unified account by setting `account` to `unified`, `auto_borrow` can likewise be enabled to borrow any shortfall. Unlike an isolated-margin account, whether a unified-account order repays automatically depends on the order's `auto_repay` setting. This setting applies only to the current order, so only assets received when that order is filled are used to repay the cross-margin loan. Unified-account orders currently support enabling both `auto_borrow` and `auto_repay`.

Automatic repayment is triggered when the order finishes, that is, when `status` becomes `cancelled` or `closed`.

**Order status**

A resting order remains `open` until its entire quantity is filled. Once fully filled, the order finishes and its status becomes `closed`. If the order is cancelled before being fully filled, its status becomes `cancelled` regardless of whether it was partially filled.

**Iceberg orders**

Use `iceberg` to set the displayed quantity of an iceberg order. Fully hidden orders are not supported. Note that fills against the hidden portion are charged at the taker fee rate.

**Self-trade prevention**

Set `stp_act` to select the self-trade prevention action.

**Unified market**

A unified market supports matching orders that use different quote currencies. Specify the actual quote currency through `trade_quote`. For example, the BTC_USD market can match orders quoted in USDC, RLUSD, and other supported quote currencies. Query `GET /spot/currency_pairs` for the quote currencies supported by each unified market.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | Order | Required | none  
id | body | string | Optional | Order ID  
text | body | string | Optional | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | body | string | Optional | The custom data that the user remarked when amending the order  
create_time | body | string | Optional | Creation time of order  
update_time | body | string | Optional | Last modification time of order  
create_time_ms | body | integer(int64) | Optional | Creation time of order (in milliseconds)  
update_time_ms | body | integer(int64) | Optional | Last modification time of order (in milliseconds)  
status | body | string | Optional | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | body | string | Required | Currency pair  
trade_quote | body | string | Optional | Actual quote currency used for the trade; can be specified only in a unified market  
type | body | string | Optional | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | body | string | Optional | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | body | string | Required | Buy or sell order  
amount | body | string | Required | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | body | string | Optional | Trading price, required when `type`=`limit`  
time_in_force | body | string | Optional | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | body | string | Optional | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | body | boolean | Optional | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | body | boolean | Optional | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | body | string | Optional | Amount left to fill  
filled_amount | body | string | Optional | Amount filled  
fill_price | body | string | Optional | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | body | string | Optional | Total filled in quote currency  
avg_deal_price | body | string | Optional | Average fill price  
fee | body | string | Optional | Fee deducted  
fee_currency | body | string | Optional | Fee currency unit  
point_fee | body | string | Optional | Points used to deduct fee  
gt_fee | body | string | Optional | GT used to deduct fee  
gt_maker_fee | body | string | Optional | GT amount used to deduct maker fee  
gt_taker_fee | body | string | Optional | GT amount used to deduct taker fee  
gt_discount | body | boolean | Optional | Whether GT fee deduction is enabled  
rebated_fee | body | string | Optional | Rebated fee  
rebated_fee_currency | body | string | Optional | Rebated fee currency unit  
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
finish_as | body | string | Optional | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | body | string | Optional | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | body | string | Optional | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | body | object|null | Optional | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
» trigger_price | body | string | Optional | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
» order_price | body | string | Optional | Take profit order price  
stop_loss | body | object|null | Optional | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
» trigger_price | body | string | Optional | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
» order_price | body | string | Optional | Stop-loss order price  
use_earn | body | boolean|null | Optional | Redeem Simple Earn funds when placing an order  
  
####  Detailed descriptions

** text**: User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders

** status**: Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled

** type**: Order Type   
  
\- limit : Limit Order  
\- market : Market Order

** amount**: Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.

** time_in_force**: Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.

** auto_repay**: Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order

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

** finish_as**: How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown

** action_mode**: Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)

**» trigger_price** : Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`

**» trigger_price** : Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
####  Request Body Schema

Spot order details

Request Body SchemaType | Constraints  
---|---  
Order | required: ["currency_pair","side","amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Request Body SchemaType | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Request Body SchemaType | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order created. The execution result depends on the time-in-force policy specified when placing the order. | Order  
  
### Response Schema

Status Code **201**

Spot order details

Type | Constraints  
---|---  
Order | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
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
    
    url = '/spot/orders'
    query_param = ''
    body='{"text":"t-abc123","currency_pair":"BTC_USDT","trade_quote":"USDC","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"},"use_earn":false}'
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
    url="/spot/orders"
    query_param=""
    body_param='{"text":"t-abc123","currency_pair":"BTC_USDT","trade_quote":"USDC","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"},"use_earn":false}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "text": "t-abc123",
      "currency_pair": "BTC_USDT",
      "trade_quote": "USDC",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "slippage": "0.05",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      },
      "use_earn": false
    }
    

> Example responses

> ACK response body example
    
    
    {
      "id": "12332324",
      "text": "t-123456",
      "amend_text": "test2"
    }
    

> RESULT response body example
    
    
    {
      "id": "12332324",
      "text": "t-123456",
      "create_time": "1548000000",
      "update_time": "1548000100",
      "create_time_ms": 1548000000123,
      "update_time_ms": 1548000100123,
      "currency_pair": "ETH_BTC",
      "status": "cancelled",
      "type": "limit",
      "account": "spot",
      "side": "buy",
      "iceberg": "0",
      "amount": "1",
      "price": "5.00032",
      "time_in_force": "gtc",
      "auto_borrow": false,
      "left": "0.5",
      "filled_total": "2.50016",
      "avg_deal_price": "5.00032",
      "stp_act": "cn",
      "finish_as": "stp",
      "stp_id": 10240
    }
    

> FULL response body example
    
    
    {
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "trade_quote": "USDC",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "slippage": "0.05",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      },
      "use_earn": false
    }
    

##  Cancel `open` orders in bulk, optionally filtered by currency pair🔒 Authenticated

DELETE`/spot/orders`

DELETE `/spot/orders`

_Cancel`open` orders in bulk, optionally filtered by currency pair_

When the `account` parameter is not specified, all pending orders including spot, unified account, and isolated margin will be cancelled. When `currency_pair` is not specified, all trading pair pending orders will be cancelled. You can specify a particular account to cancel all pending orders under that account

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Currency pair  
side | query | string | Optional | Specify all bids or all asks, both included if not specified  
account | query | string | Optional | Specify account type  
  
Classic account: All are included if not specified  
Unified account: Specify `unified`  
trade_quote | query | string | Optional | In a **unified market** only, specifies the actual quote currency for cancellation; when omitted, all orders matching the other criteria are cancelled  
action_mode | query | string | Optional | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
  
####  Detailed descriptions

**account** : Specify account type  
  
Classic account: All are included if not specified  
Unified account: Specify `unified`

**action_mode** : Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancel request is received and processed. Success is determined based on the order list | [OrderCancel]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Spot order details

Type | Constraints  
---|---  
OrderCancel | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
succeeded | boolean | Optional |  | Request execution result  
label | string | Optional |  | Error label, if any, otherwise an empty string  
message | string | Optional |  | Detailed error message, if any, otherwise an empty string  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Trading quantity  
When `type` is `limit`, it refers to the base currency (the currency being traded), such as `BTC` in `BTC_USDT`  
When `type` is `market`, it refers to different currencies based on the side:  
\- `side`: `buy` refers to quote currency, `BTC_USDT` means `USDT`  
\- `side`: `sell` refers to base currency, `BTC_USDT` means `BTC`  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
iceberg | string | Optional |  | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","ioc","stp"]  
readOnly: true | How the order was finished.  
  
\- open: processing  
\- filled: filled totally  
\- cancelled: manually cancelled  
\- ioc: time in force is `IOC`, finish immediately  
\- stp: cancelled because self trade prevention  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
  
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
    
    url = '/spot/orders'
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
    url="/spot/orders"
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
        "id": "1852454420",
        "text": "t-abc123",
        "amend_text": "-",
        "succeeded": true,
        "create_time": "1710488334",
        "update_time": "1710488334",
        "create_time_ms": 1710488334073,
        "update_time_ms": 1710488334074,
        "status": "closed",
        "currency_pair": "BTC_USDT",
        "type": "limit",
        "account": "unified",
        "side": "buy",
        "amount": "0.001",
        "price": "65000",
        "time_in_force": "gtc",
        "iceberg": "0",
        "left": "0",
        "filled_amount": "0.001",
        "fill_price": "63.4693",
        "filled_total": "63.4693",
        "avg_deal_price": "63469.3",
        "fee": "0.00000022",
        "fee_currency": "BTC",
        "point_fee": "0",
        "gt_fee": "0",
        "gt_maker_fee": "0",
        "gt_taker_fee": "0",
        "gt_discount": false,
        "rebated_fee": "0",
        "rebated_fee_currency": "USDT",
        "finish_as": "filled"
      }
    ]
    

##  Cancel batch orders by specified ID list🔒 Authenticated

POST`/spot/cancel_batch_orders`

POST `/spot/cancel_batch_orders`

_Cancel batch orders by specified ID list_

Multiple currency pairs can be specified, but maximum 20 orders are allowed per request

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | array[CancelBatchOrder] | Required | none  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
array |   
  
**items**

Info of order to be cancelled

Request Body SchemaType | Constraints  
---|---  
CancelBatchOrder | required: ["currency_pair","id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Required |  | Order currency pair  
id | string | Required |  | Order ID or user custom ID.  
Custom ID are accepted only within 30 minutes after order creation  
account | string | Optional |  | If the canceled order is a unified account apikey, this field must be specified and set to `unified`  
action_mode | string | Optional |  | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancellation completed | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CancelOrderResult

Order cancellation result

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Order currency pair  
id | string | Optional |  | Order ID  
text | string | Optional |  | Custom order information  
succeeded | boolean | Optional |  | Whether cancellation succeeded  
label | string | Optional |  | Error label when failed to cancel the order; emtpy if succeeded  
message | string | Optional |  | Error description when cancellation fails, empty if successful  
account | string | Optional |  | Default is empty (deprecated)  
  
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
    
    url = '/spot/cancel_batch_orders'
    query_param = ''
    body='[{"currency_pair":"BTC_USDT","id":"123456"}]'
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
    url="/spot/cancel_batch_orders"
    query_param=""
    body_param='[{"currency_pair":"BTC_USDT","id":"123456"}]'
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
        "currency_pair": "BTC_USDT",
        "id": "123456"
      }
    ]
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency_pair": "BTC_USDT",
        "id": "123456",
        "text": "123456",
        "succeeded": true,
        "label": null,
        "message": null
      }
    ]
    

##  Query single order details🔒 Authenticated

GET`/spot/orders/{order_id}`

GET `/spot/orders/{order_id}`

_Query single order details_

By default, queries orders for spot, unified account, and isolated margin accounts.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field).  
Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)  
currency_pair | query | string | Required | Specify the trading pair to query. This field is required when querying pending order records. This field can be omitted when querying filled order records.  
account | query | string | Optional | Specify query account  
  
####  Detailed descriptions

**order_id** : The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field).  
Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Detail retrieved | Order  
  
### Response Schema

Status Code **200**

Spot order details

Type | Constraints  
---|---  
Order | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
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
    
    url = '/spot/orders/12345'
    query_param = 'currency_pair=BTC_USDT'
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
    url="/spot/orders/12345"
    query_param="currency_pair=BTC_USDT"
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
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "trade_quote": "USDC",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      },
      "use_earn": false
    }
    

##  Amend single order🔒 Authenticated

PATCH`/spot/orders/{order_id}`

PATCH `/spot/orders/{order_id}`

_Amend single order_

By default, amend orders for spot, unified, and isolated-margin accounts.

Both the request body and query parameters support `currency_pair` and `account`; the request body has higher precedence.

Provide `currency_pair` in either the request body or the query parameters, choosing one location.

Amendments and order creation share rate limits.

Reducing quantity alone preserves matching priority. Changing the price or increasing the quantity places the order at the end of the new price level.

A new quantity below the filled quantity triggers cancellation.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field).  
Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)  
currency_pair | query | string | Optional | Currency pair  
account | query | string | Optional | Specify query account  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | OrderPatch | Required | none  
currency_pair | body | string | Optional | Currency pair  
account | body | string | Optional | Specify query account  
amount | body | string | Optional | Trading quantity. Either `amount` or `price` must be specified  
price | body | string | Optional | Trading price. Either `amount` or `price` must be specified  
amend_text | body | string | Optional | Custom info during order amendment  
action_mode | body | string | Optional | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
stop_profit | body | object|null | Optional | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
» trigger_price | body | string | Optional | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
» order_price | body | string | Optional | Take profit order price  
stop_loss | body | object|null | Optional | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
» trigger_price | body | string | Optional | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
» order_price | body | string | Optional | Stop-loss order price  
  
####  Detailed descriptions

**order_id** : The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field).  
Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)

** action_mode**: Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)

**» trigger_price** : Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`

**» trigger_price** : Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`

####  Request Body Schema

Spot order details

Request Body SchemaType | Constraints  
---|---  
OrderPatch |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
account | string | Optional |  | Specify query account  
amount | string | Optional |  | Trading quantity. Either `amount` or `price` must be specified  
price | string | Optional |  | Trading price. Either `amount` or `price` must be specified  
amend_text | string | Optional | maxLength: 31 | Custom info during order amendment  
action_mode | string | Optional |  | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
  
**stop_profit**

PatchSpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Request Body SchemaType | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

PatchSpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Request Body SchemaType | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Updated successfully | Order  
  
### Response Schema

Status Code **200**

Spot order details

Type | Constraints  
---|---  
Order | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
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
    
    url = '/spot/orders/12345'
    query_param = ''
    body='{"currency_pair":"BTC_USDT","account":"spot","amount":"1","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('PATCH', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('PATCH', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="PATCH"
    url="/spot/orders/12345"
    query_param=""
    body_param='{"currency_pair":"BTC_USDT","account":"spot","amount":"1","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "currency_pair": "BTC_USDT",
      "account": "spot",
      "amount": "1",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      }
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "trade_quote": "USDC",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      },
      "use_earn": false
    }
    

##  Cancel single order🔒 Authenticated

DELETE`/spot/orders/{order_id}`

DELETE `/spot/orders/{order_id}`

_Cancel single order_

By default, orders for spot, unified accounts and leveraged accounts are revoked.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field).  
Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)  
currency_pair | query | string | Required | Currency pair  
account | query | string | Optional | Specify query account  
action_mode | query | string | Optional | Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
  
####  Detailed descriptions

**order_id** : The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field).  
Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)

**action_mode** : Processing Mode  
  
When placing an order, different fields are returned based on the action_mode  
  
\- `ACK`: Asynchronous mode, returns only key order fields  
\- `RESULT`: No clearing information  
\- `FULL`: Full mode (default)

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order cancelled | Order  
  
### Response Schema

Status Code **200**

Spot order details

Type | Constraints  
---|---  
Order | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
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
    
    url = '/spot/orders/12345'
    query_param = 'currency_pair=BTC_USDT'
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
    url="/spot/orders/12345"
    query_param="currency_pair=BTC_USDT"
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
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "trade_quote": "USDC",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      },
      "use_earn": false
    }
    

##  Query personal trading records🔒 Authenticated

GET`/spot/my_trades`

GET `/spot/my_trades`

_Query personal trading records_

By default query of transaction records for spot, unified account and warehouse-by-site leverage accounts.

The history within a specified time range can be queried by specifying `from` or (and) `to`.

  * If no time parameters are specified, only data for the last 7 days can be obtained.
  * If only any parameter of `from` or `to` is specified, only 7-day data from the start (or end) of the specified time is returned.
  * The range not allowed to exceed 30 days.

The parameters of the time range filter are processed according to the order end time.

The maximum number of pages when searching data using limit&page paging function is 100,000, that is, limit * (page - 1) <= 100,000.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Retrieve results with specified currency pair  
limit | query | integer | Optional | Maximum number of items returned in list. Default: 100, minimum: 1, maximum: 1000  
page | query | integer(int32) | Optional | Page number  
order_id | query | string | Optional | Filter trades with specified order ID. `currency_pair` is also required if this field is present  
account | query | string | Optional | The accountparameter has been deprecated. The interface supports querying all transaction records of the account.  
from | query | integer(int64) | Optional | Start timestamp for the query  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Trade]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
Trade |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Fill ID  
create_time | string | Optional |  | Fill Time  
create_time_ms | string | Optional |  | Trading time, with millisecond precision  
currency_pair | string | Optional |  | Currency pair  
side | string | Optional | enum: ["buy","sell"] | Buy or sell order  
role | string | Optional | enum: ["taker","maker"] | Trade role, not returned in public endpoints  
amount | string | Optional |  | Trade amount  
price | string | Optional |  | Trade price.  
order_id | string | Optional |  | Related order ID, not returned in public endpoints  
fee | string | Optional |  | Fee deducted, not returned in public endpoints  
fee_currency | string | Optional |  | Fee currency unit, not returned in public endpoints  
point_fee | string | Optional |  | Points used to deduct fee, not returned in public endpoints  
gt_fee | string | Optional |  | GT used to deduct fee, not returned in public endpoints  
amend_text | string | Optional |  | The custom data that the user remarked when amending the order  
sequence_id | string | Optional |  | Consecutive trade ID within a single market.  
Used to track and identify trades in the specific market  
text | string | Optional |  | Order's Custom Information. This field is not returned by public interfaces.  
The scenarios pm_liquidate, comb_margin_liquidate, and scm_liquidate represent full-account forced liquidation orders.  
liquidate represents isolated-account forced liquidation orders.  
deal | string | Optional |  | Total Executed Value  
trade_quote | string | Optional |  | Actual quote currency used for the trade  
  
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
    
    url = '/spot/my_trades'
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
    url="/spot/my_trades"
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
        "id": "1232893232",
        "create_time": "1548000000",
        "create_time_ms": "1548000000123.456",
        "currency_pair": "BTC_USDT",
        "order_id": "4128442423",
        "side": "buy",
        "role": "maker",
        "amount": "0.15",
        "price": "0.03",
        "fee": "0.0005",
        "fee_currency": "ETH",
        "point_fee": "0",
        "gt_fee": "0",
        "sequence_id": "588018",
        "text": "t-test",
        "deal": "0.0045",
        "trade_quote": "USDC"
      }
    ]
    

##  Get server current time

GET`/spot/time`

GET `/spot/time`

_Get server current time_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | SystemTime  
  
### Response Schema

Status Code **200**

SystemTime

Type | Constraints  
---|---  
SystemTime |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
server_time | integer(int64) | Optional |  | Server current time(ms)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/time'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/time \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "server_time": 1597026383085
    }
    

##  Countdown cancel orders🔒 Authenticated

POST`/spot/countdown_cancel_all`

POST `/spot/countdown_cancel_all`

_Countdown cancel orders_

Spot order heartbeat detection. If there is no "cancel existing countdown" or "set new countdown" when the user-set `timeout` time is reached, the related `spot pending orders` will be automatically cancelled. This interface can be called repeatedly to set a new countdown or cancel the countdown. Usage example: Repeat this interface at 30s intervals, setting the countdown `timeout` to `30 (seconds)` each time. If this interface is not called again within 30 seconds, all open orders for the `currency_pair` you specified will be automatically cancelled. If no `currency_pair` is specified, open orders for all currency pairs are cancelled automatically. If the `timeout` is set to 0 within 30 seconds, the countdown timer will be terminated and the automatic order cancellation function will be cancelled.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CountdownCancelAllSpotTask | Required | none  
timeout | body | integer(int32) | Required | Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown  
currency_pair | body | string | Optional | Currency pair  
  
####  Detailed descriptions

** timeout**: Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown

####  Request Body Schema

CountdownCancelAllSpotTask

Countdown cancel task details

Request Body SchemaType | Constraints  
---|---  
CountdownCancelAllSpotTask | required: ["timeout"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
timeout | integer(int32) | Required |  | Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown  
currency_pair | string | Optional |  | Currency pair  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Countdown set successfully | TriggerTime  
  
### Response Schema

Status Code **200**

triggerTime

Type | Constraints  
---|---  
TriggerTime |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
triggerTime | integer(int64) | Optional |  | Timestamp when countdown ends, in milliseconds  
  
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
    
    url = '/spot/countdown_cancel_all'
    query_param = ''
    body='{"timeout":30,"currency_pair":"BTC_USDT"}'
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
    url="/spot/countdown_cancel_all"
    query_param=""
    body_param='{"timeout":30,"currency_pair":"BTC_USDT"}'
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
      "currency_pair": "BTC_USDT"
    }
    

> Example responses

> 200 Response
    
    
    {
      "triggerTime": "1660039145000"
    }
    

##  Batch modification of orders🔒 Authenticated

POST`/spot/amend_batch_orders`

POST `/spot/amend_batch_orders`

_Batch modification of orders_

Modify orders in spot, unified account and isolated margin account by default. Modify uncompleted orders, up to 5 orders can be modified at a time. Request parameters should be passed in array format. If there are order modification failures during the batch modification process, the modification of the next order will continue to be executed, and the execution will return with the corresponding order failure information. The call order of batch modification orders is consistent with the order list order. The return content order of batch modification orders is consistent with the order list order.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | array[BatchAmendItem] | Required | none  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
array |   
  
**items**

Order information that needs to be modified

Request Body SchemaType | Constraints  
---|---  
BatchAmendItem | required: ["order_id","currency_pair"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | The order ID returned upon successful creation or the custom ID specified by the user during creation (i.e., the 'text' field)  
currency_pair | string | Required |  | Currency pair  
account | string | Optional |  | Default spot, unified account and warehouse-by-store leverage account  
amount | string | Optional |  | Trading Quantity. Only one of `amount` or `price` can be specified  
price | string | Optional |  | Trading Price. Only one of `amount` or `price` can be specified  
amend_text | string | Optional | maxLength: 31 | Custom info during order amendment  
action_mode | string | Optional |  | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
  
**items / stop_profit**

PatchSpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Request Body SchemaType | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**items / stop_loss**

PatchSpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Request Body SchemaType | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order modification executed successfully | [BatchOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Batch order details

Type | Constraints  
---|---  
BatchOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID  
amend_text | string | Optional |  | The custom data that the user remarked when amending the order  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
succeeded | boolean | Optional |  | Request execution result  
label | string | Optional |  | Error label, if any, otherwise an empty string  
message | string | Optional |  | Detailed error message, if any, otherwise an empty string  
id | string | Optional | readOnly: true | Order ID  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
currency_pair | string | Optional |  | Currency pair  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | enum: ["spot","margin","cross_margin","unified"]  
default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Optional | enum: ["buy","sell"] | Buy or sell order  
amount | string | Optional |  | Trade amount  
price | string | Optional |  | Order price  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
iceberg | string | Optional |  | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  
  
1\. After users join the `STP Group`, he can pass `stp_act` to limit the user's self-trade prevetion strategy. If `stp_act` is not passed, the default is `cn` strategy。  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter。  
3\. If the user did not use 'stp_act' when placing the order, 'stp_act' will return '-'  
  
\- cn: Cancel newest, Cancel new orders and keep old ones  
\- co: Cancel oldest, new ones  
\- cb: Cancel both, Both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object | Optional |  | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object | Optional |  | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
  
**items / stop_profit**

PatchSpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**items / stop_loss**

PatchSpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
  
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
    
    url = '/spot/amend_batch_orders'
    query_param = ''
    body='[{"order_id":"121212","currency_pair":"BTC_USDT","account":"spot","amount":"1","amend_text":"test","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}]'
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
    url="/spot/amend_batch_orders"
    query_param=""
    body_param='[{"order_id":"121212","currency_pair":"BTC_USDT","account":"spot","amount":"1","amend_text":"test","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}]'
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
        "order_id": "121212",
        "currency_pair": "BTC_USDT",
        "account": "spot",
        "amount": "1",
        "amend_text": "test",
        "stop_profit": {
          "trigger_price": "67000",
          "order_price": "67000"
        },
        "stop_loss": {
          "trigger_price": "63000",
          "order_price": "63000"
        }
      }
    ]
    

> Example responses

> 200 Response
    
    
    [
      {
        "order_id": "12332324",
        "amend_text": "t-123456",
        "text": "t-123456",
        "succeeded": true,
        "label": "",
        "message": "",
        "id": "12332324",
        "create_time": "1548000000",
        "update_time": "1548000100",
        "create_time_ms": 1548000000123,
        "update_time_ms": 1548000100123,
        "currency_pair": "ETC_BTC",
        "status": "cancelled",
        "type": "limit",
        "account": "spot",
        "side": "buy",
        "amount": "1",
        "price": "5.00032",
        "time_in_force": "gtc",
        "iceberg": "0",
        "left": "0.5",
        "filled_amount": "1.242",
        "filled_total": "2.50016",
        "avg_deal_price": "5.00032",
        "fee": "0.005",
        "fee_currency": "ETH",
        "point_fee": "0",
        "gt_fee": "0",
        "gt_discount": false,
        "rebated_fee": "0",
        "rebated_fee_currency": "BTC",
        "stp_act": "cn",
        "finish_as": "stp",
        "stp_id": 10240
      }
    ]
    

##  Query spot insurance fund historical data

GET`/spot/insurance_history`

GET `/spot/insurance_history`

_Query spot insurance fund historical data_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
business | query | string | Required | Leverage business, margin - position by position; unified - unified account  
currency | query | string | Required | Currency  
page | query | integer(int32) | Optional | Page number  
limit | query | integer | Optional | The maximum number of items returned in the list, the default value is 30  
from | query | integer(int64) | Required | Start timestamp in seconds  
to | query | integer(int64) | Required | End timestamp in seconds  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [SpotInsuranceHistory]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
SpotInsuranceHistory |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency | string | Optional |  | Currency  
balance | string | Optional |  | Balance  
time | integer(int64) | Optional |  | Creation time, timestamp, milliseconds  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/insurance_history'
    query_param = 'business=margin&currency=BTC&from=1547706332&to=1547706332'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/insurance_history?business=margin&currency=BTC&from=1547706332&to=1547706332 \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency": "BTC",
        "balance": "1021.21",
        "time": 1727054547
      }
    ]
    

##  Query running auto order list🔒 Authenticated

GET`/spot/price_orders`

GET `/spot/price_orders`

_Query running auto order list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
status | query | string | Required | Query order list based on status  
market | query | string | Optional | Trading market  
account | query | string | Optional | Trading account type. Unified account must be set to `unified`  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
status | open  
status | finished  
account | normal  
account | margin  
account | unified  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SpotPriceTriggeredOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Spot price order details

Type | Constraints  
---|---  
SpotPriceTriggeredOrder | required: ["trigger","put","market"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger | SpotPriceTrigger | Required | required: ["price","rule"] |   
put | SpotPricePutOrder | Required | required: ["side","price","amount","account","time_in_force"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
user | integer | Optional | readOnly: true | User ID  
market | string | Required |  | Market  
ctime | integer(int64) | Optional | readOnly: true | Created time  
ftime | integer(int64) | Optional | readOnly: true | End time  
fired_order_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | readOnly: true | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
  
**items / trigger**

Type | Constraints  
---|---  
SpotPriceTrigger | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Trigger price  
rule | string | Required | enum: [">=","<="] | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
**items / put**

Type | Constraints  
---|---  
SpotPricePutOrder | required: ["side","price","amount","account","time_in_force"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
side | string | Required | enum: ["buy","sell"] | Order side  
  
\- buy: buy side  
\- sell: sell side  
price | string | Required |  | Order price  
amount | string | Required |  | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
account | string | Required | enum: ["normal","margin","unified"]  
default: "normal" | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
time_in_force | string | Required | enum: ["gtc","ioc"]  
default: "gtc" | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
auto_borrow | boolean | Optional | default: false | Whether to borrow coins automatically  
auto_repay | boolean | Optional | default: false | Whether to repay the loan automatically  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
  
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
    
    url = '/spot/price_orders'
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
    url="/spot/price_orders"
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
        "trigger": {
          "price": "100",
          "rule": ">=",
          "expiration": 3600
        },
        "put": {
          "type": "limit",
          "side": "buy",
          "price": "2.15",
          "amount": "2.00000000",
          "account": "normal",
          "time_in_force": "gtc",
          "text": "api"
        },
        "id": 1283293,
        "user": 1234,
        "market": "GT_USDT",
        "ctime": 1616397800,
        "ftime": 1616397801,
        "fired_order_id": 0,
        "status": "",
        "reason": ""
      }
    ]
    

##  Create price-triggered order🔒 Authenticated

POST`/spot/price_orders`

POST `/spot/price_orders`

_Create price-triggered order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | SpotPriceTriggeredOrder | Required | none  
trigger | body | SpotPriceTrigger | Required | none  
» price | body | string | Required | Trigger price  
» rule | body | string | Required | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
  
» expiration | body | integer | Optional | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
put | body | SpotPricePutOrder | Required | none  
» type | body | string | Optional | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
» side | body | string | Required | Order side  
  
\- buy: buy side  
\- sell: sell side  
» price | body | string | Required | Order price  
» amount | body | string | Required | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
» account | body | string | Required | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
  
» time_in_force | body | string | Required | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
  
» auto_borrow | body | boolean | Optional | Whether to borrow coins automatically  
» auto_repay | body | boolean | Optional | Whether to repay the loan automatically  
» text | body | string | Optional | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
id | body | integer(int64) | Optional | Auto order ID  
user | body | integer | Optional | User ID  
market | body | string | Required | Market  
ctime | body | integer(int64) | Optional | Created time  
ftime | body | integer(int64) | Optional | End time  
fired_order_id | body | integer(int64) | Optional | ID of the order created after trigger  
status | body | string | Optional | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
reason | body | string | Optional | Additional description of how the order was completed  
  
####  Detailed descriptions

**» rule** : Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  

**» type** : Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order

**» side** : Order side  
  
\- buy: buy side  
\- sell: sell side

**» account** : Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  

**» time_in_force** : time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  

**» text** : The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app

** status**: Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» rule | >=  
» rule | <=  
» type | limit  
» type | market  
» side | buy  
» side | sell  
» account | normal  
» account | margin  
» account | unified  
» time_in_force | gtc  
» time_in_force | ioc  
  
####  Request Body Schema

Spot price order details

Request Body SchemaType | Constraints  
---|---  
SpotPriceTriggeredOrder | required: ["trigger","put","market"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger | SpotPriceTrigger | Required | required: ["price","rule"] |   
put | SpotPricePutOrder | Required | required: ["side","price","amount","account","time_in_force"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
user | integer | Optional | readOnly: true | User ID  
market | string | Required |  | Market  
ctime | integer(int64) | Optional | readOnly: true | Created time  
ftime | integer(int64) | Optional | readOnly: true | End time  
fired_order_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | readOnly: true | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
  
**trigger**

Request Body SchemaType | Constraints  
---|---  
SpotPriceTrigger | required: ["price","rule"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Trigger price  
rule | string | Required | enum: [">=","<="] | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
**put**

Request Body SchemaType | Constraints  
---|---  
SpotPricePutOrder | required: ["side","price","amount","account","time_in_force"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
side | string | Required | enum: ["buy","sell"] | Order side  
  
\- buy: buy side  
\- sell: sell side  
price | string | Required |  | Order price  
amount | string | Required |  | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
account | string | Required | enum: ["normal","margin","unified"]  
default: "normal" | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
time_in_force | string | Required | enum: ["gtc","ioc"]  
default: "gtc" | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
auto_borrow | boolean | Optional | default: false | Whether to borrow coins automatically  
auto_repay | boolean | Optional | default: false | Whether to repay the loan automatically  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
  
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
    
    url = '/spot/price_orders'
    query_param = ''
    body='{"trigger":{"price":"100","rule":">=","expiration":3600},"put":{"type":"limit","side":"buy","price":"2.15","amount":"2.00000000","account":"normal","time_in_force":"gtc","text":"api"},"market":"GT_USDT"}'
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
    url="/spot/price_orders"
    query_param=""
    body_param='{"trigger":{"price":"100","rule":">=","expiration":3600},"put":{"type":"limit","side":"buy","price":"2.15","amount":"2.00000000","account":"normal","time_in_force":"gtc","text":"api"},"market":"GT_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "trigger": {
        "price": "100",
        "rule": ">=",
        "expiration": 3600
      },
      "put": {
        "type": "limit",
        "side": "buy",
        "price": "2.15",
        "amount": "2.00000000",
        "account": "normal",
        "time_in_force": "gtc",
        "text": "api"
      },
      "market": "GT_USDT"
    }
    

> Example responses

> 201 Response
    
    
    {
      "id": 1432329
    }
    

##  Cancel all auto orders🔒 Authenticated

DELETE`/spot/price_orders`

DELETE `/spot/price_orders`

_Cancel all auto orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
market | query | string | Optional | Trading market  
account | query | string | Optional | Trading account type. Unified account must be set to `unified`  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
account | normal  
account | margin  
account | unified  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancel request is received and processed. Success is determined based on the order list | [SpotPriceTriggeredOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Spot price order details

Type | Constraints  
---|---  
SpotPriceTriggeredOrder | required: ["trigger","put","market"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger | SpotPriceTrigger | Required | required: ["price","rule"] |   
put | SpotPricePutOrder | Required | required: ["side","price","amount","account","time_in_force"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
user | integer | Optional | readOnly: true | User ID  
market | string | Required |  | Market  
ctime | integer(int64) | Optional | readOnly: true | Created time  
ftime | integer(int64) | Optional | readOnly: true | End time  
fired_order_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | readOnly: true | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
  
**items / trigger**

Type | Constraints  
---|---  
SpotPriceTrigger | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Trigger price  
rule | string | Required | enum: [">=","<="] | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
**items / put**

Type | Constraints  
---|---  
SpotPricePutOrder | required: ["side","price","amount","account","time_in_force"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
side | string | Required | enum: ["buy","sell"] | Order side  
  
\- buy: buy side  
\- sell: sell side  
price | string | Required |  | Order price  
amount | string | Required |  | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
account | string | Required | enum: ["normal","margin","unified"]  
default: "normal" | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
time_in_force | string | Required | enum: ["gtc","ioc"]  
default: "gtc" | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
auto_borrow | boolean | Optional | default: false | Whether to borrow coins automatically  
auto_repay | boolean | Optional | default: false | Whether to repay the loan automatically  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
  
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
    
    url = '/spot/price_orders'
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
    url="/spot/price_orders"
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
        "trigger": {
          "price": "100",
          "rule": ">=",
          "expiration": 3600
        },
        "put": {
          "type": "limit",
          "side": "buy",
          "price": "2.15",
          "amount": "2.00000000",
          "account": "normal",
          "time_in_force": "gtc",
          "text": "api"
        },
        "id": 1283293,
        "user": 1234,
        "market": "GT_USDT",
        "ctime": 1616397800,
        "ftime": 1616397801,
        "fired_order_id": 0,
        "status": "",
        "reason": ""
      }
    ]
    

##  Query single auto order details🔒 Authenticated

GET`/spot/price_orders/{order_id}`

GET `/spot/price_orders/{order_id}`

_Query single auto order details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | ID returned when order is successfully created  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Auto order details | SpotPriceTriggeredOrder  
  
### Response Schema

Status Code **200**

Spot price order details

Type | Constraints  
---|---  
SpotPriceTriggeredOrder | required: ["trigger","put","market"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger | SpotPriceTrigger | Required | required: ["price","rule"] |   
put | SpotPricePutOrder | Required | required: ["side","price","amount","account","time_in_force"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
user | integer | Optional | readOnly: true | User ID  
market | string | Required |  | Market  
ctime | integer(int64) | Optional | readOnly: true | Created time  
ftime | integer(int64) | Optional | readOnly: true | End time  
fired_order_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | readOnly: true | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
  
**trigger**

Type | Constraints  
---|---  
SpotPriceTrigger | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Trigger price  
rule | string | Required | enum: [">=","<="] | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
**put**

Type | Constraints  
---|---  
SpotPricePutOrder | required: ["side","price","amount","account","time_in_force"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
side | string | Required | enum: ["buy","sell"] | Order side  
  
\- buy: buy side  
\- sell: sell side  
price | string | Required |  | Order price  
amount | string | Required |  | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
account | string | Required | enum: ["normal","margin","unified"]  
default: "normal" | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
time_in_force | string | Required | enum: ["gtc","ioc"]  
default: "gtc" | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
auto_borrow | boolean | Optional | default: false | Whether to borrow coins automatically  
auto_repay | boolean | Optional | default: false | Whether to repay the loan automatically  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
  
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
    
    url = '/spot/price_orders/string'
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
    url="/spot/price_orders/string"
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
      "trigger": {
        "price": "100",
        "rule": ">=",
        "expiration": 3600
      },
      "put": {
        "type": "limit",
        "side": "buy",
        "price": "2.15",
        "amount": "2.00000000",
        "account": "normal",
        "time_in_force": "gtc",
        "text": "api"
      },
      "id": 1283293,
      "user": 1234,
      "market": "GT_USDT",
      "ctime": 1616397800,
      "ftime": 1616397801,
      "fired_order_id": 0,
      "status": "",
      "reason": ""
    }
    

##  Cancel single auto order🔒 Authenticated

DELETE`/spot/price_orders/{order_id}`

DELETE `/spot/price_orders/{order_id}`

_Cancel single auto order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | ID returned when order is successfully created  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Auto order details | SpotPriceTriggeredOrder  
  
### Response Schema

Status Code **200**

Spot price order details

Type | Constraints  
---|---  
SpotPriceTriggeredOrder | required: ["trigger","put","market"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger | SpotPriceTrigger | Required | required: ["price","rule"] |   
put | SpotPricePutOrder | Required | required: ["side","price","amount","account","time_in_force"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
user | integer | Optional | readOnly: true | User ID  
market | string | Required |  | Market  
ctime | integer(int64) | Optional | readOnly: true | Created time  
ftime | integer(int64) | Optional | readOnly: true | End time  
fired_order_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | readOnly: true | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
  
**trigger**

Type | Constraints  
---|---  
SpotPriceTrigger | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Trigger price  
rule | string | Required | enum: [">=","<="] | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
**put**

Type | Constraints  
---|---  
SpotPricePutOrder | required: ["side","price","amount","account","time_in_force"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
side | string | Required | enum: ["buy","sell"] | Order side  
  
\- buy: buy side  
\- sell: sell side  
price | string | Required |  | Order price  
amount | string | Required |  | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
account | string | Required | enum: ["normal","margin","unified"]  
default: "normal" | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
time_in_force | string | Required | enum: ["gtc","ioc"]  
default: "gtc" | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
auto_borrow | boolean | Optional | default: false | Whether to borrow coins automatically  
auto_repay | boolean | Optional | default: false | Whether to repay the loan automatically  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
  
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
    
    url = '/spot/price_orders/string'
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
    url="/spot/price_orders/string"
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
      "trigger": {
        "price": "100",
        "rule": ">=",
        "expiration": 3600
      },
      "put": {
        "type": "limit",
        "side": "buy",
        "price": "2.15",
        "amount": "2.00000000",
        "account": "normal",
        "time_in_force": "gtc",
        "text": "api"
      },
      "id": 1283293,
      "user": 1234,
      "market": "GT_USDT",
      "ctime": 1616397800,
      "ftime": 1616397801,
      "fired_order_id": 0,
      "status": "",
      "reason": ""
    }
    

##  List Spot POV orders🔒 Authenticated

GET`/spot/pov_orders`

GET `/spot/pov_orders`

_List Spot POV orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Currency pair  
status | query | string | Required | Order status. Defaults to open  
  
\- open: Active orders  
\- finished: Finished orders  
side | query | string | Optional | Specify all bids or all asks, both included if not specified  
page | query | integer(int32) | Optional | Page number, up to 100  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
####  Detailed descriptions

**status** : Order status. Defaults to open  
  
\- open: Active orders  
\- finished: Finished orders

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [SpotPovOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Spot POV order details

Type | Constraints  
---|---  
SpotPovOrder | required: ["id","currency_pair","side","amount","participation_rate","ttl","status","create_time_ms"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required | readOnly: true | Order ID  
currency_pair | string | Required | readOnly: true | Currency pair  
side | string | Required | readOnly: true | Buy or sell order  
amount | string | Required | readOnly: true | Trade amount  
participation_rate | integer | Required | readOnly: true | Target participation rate as a percentage. Allowed values: 5, 10, 20, and 40  
ttl | string | Required | readOnly: true | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d  
limit_price | string | Optional | readOnly: true | Limit price. If omitted, the market price is used  
trigger_price | string | Optional | readOnly: true | Trigger price. If omitted, the order is triggered immediately  
status | string | Required | readOnly: true | Order status  
  
\- CREATED: Created  
\- CANCELING: Canceling  
\- RUNNING: Running  
\- COMPLETED: Completed  
\- EXPIRED: Expired  
\- TERMINATED: Terminated  
terminated_as | string | Optional | readOnly: true | Order termination reason code  
start_time_ms | integer(int64) | Optional | readOnly: true | Order execution start time in milliseconds  
end_time_ms | integer(int64) | Optional | readOnly: true | Order execution end time in milliseconds  
expire_time_ms | integer(int64) | Optional | readOnly: true | Order expiration time in milliseconds  
create_time_ms | integer(int64) | Required | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
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
    
    url = '/spot/pov_orders'
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
    url="/spot/pov_orders"
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
        "id": "1216",
        "currency_pair": "BTC_USDT",
        "side": "buy",
        "amount": "0.010000",
        "participation_rate": 10,
        "ttl": "1h",
        "limit_price": "63000",
        "trigger_price": "63000",
        "status": "CREATED",
        "terminated_as": "",
        "start_time_ms": 0,
        "end_time_ms": 0,
        "expire_time_ms": 1784365405074,
        "create_time_ms": 1784279005258,
        "update_time_ms": 1784279005258
      }
    ]
    

##  Create a spot percentage-of-volume (POV) strategy order🔒 Authenticated

POST`/spot/pov_orders`

POST `/spot/pov_orders`

_Create a spot percentage-of-volume (POV) strategy order_

participation_rate specifies the target participation rate, and ttl specifies the validity period. The response contains the order id, which can be used with GET /spot/pov_orders/{order_id} to query details.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | SpotPovOrderCreator | Required | none  
currency_pair | body | string | Required | Currency pair  
side | body | string | Required | Buy or sell order  
amount | body | string | Required | Trade amount  
participation_rate | body | integer | Required | Target participation rate as a percentage. Valid values: 5, 10, 20, and 40  
ttl | body | string | Required | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d  
limit_price | body | string | Optional | Limit price. If omitted, the market price is used  
trigger_price | body | string | Optional | Trigger price. If omitted, the order is triggered immediately  
text | body | string | Optional | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
  
####  Detailed descriptions

** text**: Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | buy  
side | sell  
  
####  Request Body Schema

Spot POV order creation request

Request Body SchemaType | Constraints  
---|---  
SpotPovOrderCreator | required: ["currency_pair","side","amount","participation_rate","ttl"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Required |  | Currency pair  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Trade amount  
participation_rate | integer | Required |  | Target participation rate as a percentage. Valid values: 5, 10, 20, and 40  
ttl | string | Required |  | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d  
limit_price | string | Optional |  | Limit price. If omitted, the market price is used  
trigger_price | string | Optional |  | Trigger price. If omitted, the order is triggered immediately  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order created successfully | SpotPovOrder  
  
### Response Schema

Status Code **201**

Spot POV order details

Type | Constraints  
---|---  
SpotPovOrder | required: ["id","currency_pair","side","amount","participation_rate","ttl","status","create_time_ms"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required | readOnly: true | Order ID  
currency_pair | string | Required | readOnly: true | Currency pair  
side | string | Required | readOnly: true | Buy or sell order  
amount | string | Required | readOnly: true | Trade amount  
participation_rate | integer | Required | readOnly: true | Target participation rate as a percentage. Allowed values: 5, 10, 20, and 40  
ttl | string | Required | readOnly: true | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d  
limit_price | string | Optional | readOnly: true | Limit price. If omitted, the market price is used  
trigger_price | string | Optional | readOnly: true | Trigger price. If omitted, the order is triggered immediately  
status | string | Required | readOnly: true | Order status  
  
\- CREATED: Created  
\- CANCELING: Canceling  
\- RUNNING: Running  
\- COMPLETED: Completed  
\- EXPIRED: Expired  
\- TERMINATED: Terminated  
terminated_as | string | Optional | readOnly: true | Order termination reason code  
start_time_ms | integer(int64) | Optional | readOnly: true | Order execution start time in milliseconds  
end_time_ms | integer(int64) | Optional | readOnly: true | Order execution end time in milliseconds  
expire_time_ms | integer(int64) | Optional | readOnly: true | Order expiration time in milliseconds  
create_time_ms | integer(int64) | Required | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
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
    
    url = '/spot/pov_orders'
    query_param = ''
    body='{"currency_pair":"BTC_USDT","side":"buy","amount":"1","participation_rate":5,"ttl":"1h","limit_price":"63000","trigger_price":"63000"}'
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
    url="/spot/pov_orders"
    query_param=""
    body_param='{"currency_pair":"BTC_USDT","side":"buy","amount":"1","participation_rate":5,"ttl":"1h","limit_price":"63000","trigger_price":"63000"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "currency_pair": "BTC_USDT",
      "side": "buy",
      "amount": "1",
      "participation_rate": 5,
      "ttl": "1h",
      "limit_price": "63000",
      "trigger_price": "63000"
    }
    

> Example responses

> 201 Response
    
    
    {
      "id": "1216",
      "currency_pair": "BTC_USDT",
      "side": "buy",
      "amount": "0.010000",
      "participation_rate": 10,
      "ttl": "1h",
      "limit_price": "63000",
      "trigger_price": "63000",
      "status": "CREATED",
      "terminated_as": "",
      "start_time_ms": 0,
      "end_time_ms": 0,
      "expire_time_ms": 1784365405074,
      "create_time_ms": 1784279005258,
      "update_time_ms": 1784279005258
    }
    

##  Cancel Spot POV orders🔒 Authenticated

DELETE`/spot/pov_orders`

DELETE `/spot/pov_orders`

_Cancel Spot POV orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Currency pair  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancel request is received and processed. Success is determined based on the order list | [SpotPovOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Spot POV order details

Type | Constraints  
---|---  
SpotPovOrder | required: ["id","currency_pair","side","amount","participation_rate","ttl","status","create_time_ms"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required | readOnly: true | Order ID  
currency_pair | string | Required | readOnly: true | Currency pair  
side | string | Required | readOnly: true | Buy or sell order  
amount | string | Required | readOnly: true | Trade amount  
participation_rate | integer | Required | readOnly: true | Target participation rate as a percentage. Allowed values: 5, 10, 20, and 40  
ttl | string | Required | readOnly: true | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d  
limit_price | string | Optional | readOnly: true | Limit price. If omitted, the market price is used  
trigger_price | string | Optional | readOnly: true | Trigger price. If omitted, the order is triggered immediately  
status | string | Required | readOnly: true | Order status  
  
\- CREATED: Created  
\- CANCELING: Canceling  
\- RUNNING: Running  
\- COMPLETED: Completed  
\- EXPIRED: Expired  
\- TERMINATED: Terminated  
terminated_as | string | Optional | readOnly: true | Order termination reason code  
start_time_ms | integer(int64) | Optional | readOnly: true | Order execution start time in milliseconds  
end_time_ms | integer(int64) | Optional | readOnly: true | Order execution end time in milliseconds  
expire_time_ms | integer(int64) | Optional | readOnly: true | Order expiration time in milliseconds  
create_time_ms | integer(int64) | Required | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
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
    
    url = '/spot/pov_orders'
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
    url="/spot/pov_orders"
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
        "id": "1216",
        "currency_pair": "BTC_USDT",
        "side": "buy",
        "amount": "0.010000",
        "participation_rate": 10,
        "ttl": "1h",
        "limit_price": "63000",
        "trigger_price": "63000",
        "status": "CREATED",
        "terminated_as": "",
        "start_time_ms": 0,
        "end_time_ms": 0,
        "expire_time_ms": 1784365405074,
        "create_time_ms": 1784279005258,
        "update_time_ms": 1784279005258
      }
    ]
    

##  Query Spot POV order details🔒 Authenticated

GET`/spot/pov_orders/{order_id}`

GET `/spot/pov_orders/{order_id}`

_Query Spot POV order details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | The order ID returned after successful creation, or the custom ID specified by the user in the `text` field.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Detail retrieved | SpotPovOrder  
  
### Response Schema

Status Code **200**

Spot POV order details

Type | Constraints  
---|---  
SpotPovOrder | required: ["id","currency_pair","side","amount","participation_rate","ttl","status","create_time_ms"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required | readOnly: true | Order ID  
currency_pair | string | Required | readOnly: true | Currency pair  
side | string | Required | readOnly: true | Buy or sell order  
amount | string | Required | readOnly: true | Trade amount  
participation_rate | integer | Required | readOnly: true | Target participation rate as a percentage. Allowed values: 5, 10, 20, and 40  
ttl | string | Required | readOnly: true | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d  
limit_price | string | Optional | readOnly: true | Limit price. If omitted, the market price is used  
trigger_price | string | Optional | readOnly: true | Trigger price. If omitted, the order is triggered immediately  
status | string | Required | readOnly: true | Order status  
  
\- CREATED: Created  
\- CANCELING: Canceling  
\- RUNNING: Running  
\- COMPLETED: Completed  
\- EXPIRED: Expired  
\- TERMINATED: Terminated  
terminated_as | string | Optional | readOnly: true | Order termination reason code  
start_time_ms | integer(int64) | Optional | readOnly: true | Order execution start time in milliseconds  
end_time_ms | integer(int64) | Optional | readOnly: true | Order execution end time in milliseconds  
expire_time_ms | integer(int64) | Optional | readOnly: true | Order expiration time in milliseconds  
create_time_ms | integer(int64) | Required | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
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
    
    url = '/spot/pov_orders/12345'
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
    url="/spot/pov_orders/12345"
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
      "id": "1216",
      "currency_pair": "BTC_USDT",
      "side": "buy",
      "amount": "0.010000",
      "participation_rate": 10,
      "ttl": "1h",
      "limit_price": "63000",
      "trigger_price": "63000",
      "status": "CREATED",
      "terminated_as": "",
      "start_time_ms": 0,
      "end_time_ms": 0,
      "expire_time_ms": 1784365405074,
      "create_time_ms": 1784279005258,
      "update_time_ms": 1784279005258
    }
    

##  Cancel a Spot POV order🔒 Authenticated

DELETE`/spot/pov_orders/{order_id}`

DELETE `/spot/pov_orders/{order_id}`

_Cancel a Spot POV order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | The order ID returned after successful creation, or the custom ID specified by the user in the `text` field.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order cancelled | SpotPovOrder  
  
### Response Schema

Status Code **200**

Spot POV order details

Type | Constraints  
---|---  
SpotPovOrder | required: ["id","currency_pair","side","amount","participation_rate","ttl","status","create_time_ms"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required | readOnly: true | Order ID  
currency_pair | string | Required | readOnly: true | Currency pair  
side | string | Required | readOnly: true | Buy or sell order  
amount | string | Required | readOnly: true | Trade amount  
participation_rate | integer | Required | readOnly: true | Target participation rate as a percentage. Allowed values: 5, 10, 20, and 40  
ttl | string | Required | readOnly: true | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d  
limit_price | string | Optional | readOnly: true | Limit price. If omitted, the market price is used  
trigger_price | string | Optional | readOnly: true | Trigger price. If omitted, the order is triggered immediately  
status | string | Required | readOnly: true | Order status  
  
\- CREATED: Created  
\- CANCELING: Canceling  
\- RUNNING: Running  
\- COMPLETED: Completed  
\- EXPIRED: Expired  
\- TERMINATED: Terminated  
terminated_as | string | Optional | readOnly: true | Order termination reason code  
start_time_ms | integer(int64) | Optional | readOnly: true | Order execution start time in milliseconds  
end_time_ms | integer(int64) | Optional | readOnly: true | Order execution end time in milliseconds  
expire_time_ms | integer(int64) | Optional | readOnly: true | Order expiration time in milliseconds  
create_time_ms | integer(int64) | Required | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
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
    
    url = '/spot/pov_orders/12345'
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
    url="/spot/pov_orders/12345"
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
      "id": "1216",
      "currency_pair": "BTC_USDT",
      "side": "buy",
      "amount": "0.010000",
      "participation_rate": 10,
      "ttl": "1h",
      "limit_price": "63000",
      "trigger_price": "63000",
      "status": "CREATED",
      "terminated_as": "",
      "start_time_ms": 0,
      "end_time_ms": 0,
      "expire_time_ms": 1784365405074,
      "create_time_ms": 1784279005258,
      "update_time_ms": 1784279005258
    }
    

#  Schemas

##  OpenOrders

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
total | integer | Optional |  | Total number of open orders for this trading pair on the current page  
orders | array | Optional |  |   
  
**orders**

Type | Constraints  
---|---  
array |   
  
**orders / items**

Spot order details

Type | Constraints  
---|---  
object | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**orders / items / stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**orders / items / stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
      
    
    {
      "currency_pair": "string",
      "total": 0,
      "orders": [
        {
          "id": "string",
          "text": "string",
          "amend_text": "string",
          "create_time": "string",
          "update_time": "string",
          "create_time_ms": 0,
          "update_time_ms": 0,
          "status": "open",
          "currency_pair": "string",
          "trade_quote": "string",
          "type": "limit",
          "account": "spot",
          "side": "buy",
          "amount": "string",
          "price": "string",
          "time_in_force": "gtc",
          "iceberg": "string",
          "auto_borrow": true,
          "auto_repay": true,
          "left": "string",
          "filled_amount": "string",
          "fill_price": "string",
          "filled_total": "string",
          "avg_deal_price": "string",
          "fee": "string",
          "fee_currency": "string",
          "point_fee": "string",
          "gt_fee": "string",
          "gt_maker_fee": "string",
          "gt_taker_fee": "string",
          "gt_discount": true,
          "rebated_fee": "string",
          "rebated_fee_currency": "string",
          "stp_id": 0,
          "stp_act": "cn",
          "finish_as": "open",
          "action_mode": "string",
          "slippage": "string",
          "stop_profit": {},
          "stop_loss": {},
          "use_earn": true
        }
      ]
    }
    
    

##  SpotPriceTriggeredOrder

Spot price order details

Type | Constraints  
---|---  
object | required: ["trigger","put","market"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger | SpotPriceTrigger | Required | required: ["price","rule"] |   
put | SpotPricePutOrder | Required | required: ["side","price","amount","account","time_in_force"] |   
id | integer(int64) | Optional | readOnly: true | Auto order ID  
user | integer | Optional | readOnly: true | User ID  
market | string | Required |  | Market  
ctime | integer(int64) | Optional | readOnly: true | Created time  
ftime | integer(int64) | Optional | readOnly: true | End time  
fired_order_id | integer(int64) | Optional | readOnly: true | ID of the order created after trigger  
status | string | Optional | readOnly: true | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
reason | string | Optional | readOnly: true | Additional description of how the order was completed  
      
    
    {
      "trigger": {
        "price": "string",
        "rule": ">=",
        "expiration": 0
      },
      "put": {
        "type": "limit",
        "side": "buy",
        "price": "string",
        "amount": "string",
        "account": "normal",
        "time_in_force": "gtc",
        "auto_borrow": false,
        "auto_repay": false,
        "text": "string"
      },
      "id": 0,
      "user": 0,
      "market": "string",
      "ctime": 0,
      "ftime": 0,
      "fired_order_id": 0,
      "status": "string",
      "reason": "string"
    }
    
    

##  BatchAmendItem

Order information that needs to be modified

Type | Constraints  
---|---  
object | required: ["order_id","currency_pair"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | The order ID returned upon successful creation or the custom ID specified by the user during creation (i.e., the 'text' field)  
currency_pair | string | Required |  | Currency pair  
account | string | Optional |  | Default spot, unified account and warehouse-by-store leverage account  
amount | string | Optional |  | Trading Quantity. Only one of `amount` or `price` can be specified  
price | string | Optional |  | Trading Price. Only one of `amount` or `price` can be specified  
amend_text | string | Optional | maxLength: 31 | Custom info during order amendment  
action_mode | string | Optional |  | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
  
**stop_profit**

PatchSpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

PatchSpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
      
    
    {
      "order_id": "string",
      "currency_pair": "string",
      "account": "string",
      "amount": "string",
      "price": "string",
      "amend_text": "string",
      "action_mode": "string",
      "stop_profit": {
        "trigger_price": "string",
        "order_price": "string"
      },
      "stop_loss": {
        "trigger_price": "string",
        "order_price": "string"
      }
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
    
    

##  LiquidateOrder

Spot liquidation order details

Type | Constraints  
---|---  
object | required: ["currency_pair","amount","price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
currency_pair | string | Required |  | Currency pair  
amount | string | Required |  | Trade amount  
price | string | Required |  | Order price  
action_mode | string | Optional |  | Processing mode:  
  
Different fields are returned when placing an order based on action_mode. This field is only valid during the request and is not included in the response  
`ACK`: Asynchronous mode, only returns key order fields  
`RESULT`: No liquidation information  
`FULL`: Full mode (default)  
      
    
    {
      "text": "string",
      "currency_pair": "string",
      "amount": "string",
      "price": "string",
      "action_mode": "string"
    }
    
    

##  SpotAccountBook

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Balance change record ID  
time | integer(int64) | Optional |  | The timestamp of the change (in milliseconds)  
currency | string | Optional |  | Currency changed  
change | string | Optional |  | Amount changed. Positive value means transferring in, while negative out  
balance | string | Optional |  | Balance after change  
type | string | Optional |  | Account change type; deprecated (see `code` for account change type encoding)  
code | string | Optional |  | Account change code, see [Asset Record Code] (Asset Record Code)  
text | string | Optional |  | Additional information  
      
    
    {
      "id": "string",
      "time": 0,
      "currency": "string",
      "change": "string",
      "balance": "string",
      "type": "string",
      "code": "string",
      "text": "string"
    }
    
    

##  SpotAccount

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency | string | Optional |  | Currency detail  
available | string | Optional |  | Available amount  
locked | string | Optional |  | Locked amount, used in trading  
update_id | integer(int64) | Optional |  | Version number  
      
    
    {
      "currency": "string",
      "available": "string",
      "locked": "string",
      "update_id": 0
    }
    
    

##  SpotPovOrder

Spot POV order details

Type | Constraints  
---|---  
object | required: ["id","currency_pair","side","amount","participation_rate","ttl","status","create_time_ms"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required | readOnly: true | Order ID  
currency_pair | string | Required | readOnly: true | Currency pair  
side | string | Required | readOnly: true | Buy or sell order  
amount | string | Required | readOnly: true | Trade amount  
participation_rate | integer | Required | readOnly: true | Target participation rate as a percentage. Allowed values: 5, 10, 20, and 40  
ttl | string | Required | readOnly: true | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d  
limit_price | string | Optional | readOnly: true | Limit price. If omitted, the market price is used  
trigger_price | string | Optional | readOnly: true | Trigger price. If omitted, the order is triggered immediately  
status | string | Required | readOnly: true | Order status  
  
\- CREATED: Created  
\- CANCELING: Canceling  
\- RUNNING: Running  
\- COMPLETED: Completed  
\- EXPIRED: Expired  
\- TERMINATED: Terminated  
terminated_as | string | Optional | readOnly: true | Order termination reason code  
start_time_ms | integer(int64) | Optional | readOnly: true | Order execution start time in milliseconds  
end_time_ms | integer(int64) | Optional | readOnly: true | Order execution end time in milliseconds  
expire_time_ms | integer(int64) | Optional | readOnly: true | Order expiration time in milliseconds  
create_time_ms | integer(int64) | Required | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
      
    
    {
      "id": "string",
      "currency_pair": "string",
      "side": "string",
      "amount": "string",
      "participation_rate": 0,
      "ttl": "string",
      "limit_price": "string",
      "trigger_price": "string",
      "status": "string",
      "terminated_as": "string",
      "start_time_ms": 0,
      "end_time_ms": 0,
      "expire_time_ms": 0,
      "create_time_ms": 0,
      "update_time_ms": 0,
      "text": "string"
    }
    
    

##  OrderBook

Type | Constraints  
---|---  
object | required: ["asks","bids"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Order book ID, which is updated whenever the order book is changed. Valid only when `with_id` is set to `true`  
current | integer(int64) | Optional |  | The timestamp of the response data being generated (in milliseconds)  
update | integer(int64) | Optional |  | The timestamp of when the orderbook last changed (in milliseconds)  
asks | array | Required |  | Ask Depth  
bids | array | Required |  | Bid Depth  
  
**asks**

Ask Depth

Type | Constraints  
---|---  
array |   
  
**asks / items**

Price and Quantity Pair

Type | Constraints  
---|---  
array | minItems: 2  
maxItems: 2  
  
**asks / items / items**

Type | Constraints  
---|---  
string |   
  
**bids**

Bid Depth

Type | Constraints  
---|---  
array |   
  
**bids / items**

Price and Quantity Pair

Type | Constraints  
---|---  
array | minItems: 2  
maxItems: 2  
  
**bids / items / items**

Type | Constraints  
---|---  
string |   
      
    
    {
      "id": 0,
      "current": 0,
      "update": 0,
      "asks": [
        [
          "string",
          "string"
        ]
      ],
      "bids": [
        [
          "string",
          "string"
        ]
      ]
    }
    
    

##  BatchOrder

Batch order details

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Optional |  | Order ID  
amend_text | string | Optional |  | The custom data that the user remarked when amending the order  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
succeeded | boolean | Optional |  | Request execution result  
label | string | Optional |  | Error label, if any, otherwise an empty string  
message | string | Optional |  | Detailed error message, if any, otherwise an empty string  
id | string | Optional | readOnly: true | Order ID  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
currency_pair | string | Optional |  | Currency pair  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | enum: ["spot","margin","cross_margin","unified"]  
default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Optional | enum: ["buy","sell"] | Buy or sell order  
amount | string | Optional |  | Trade amount  
price | string | Optional |  | Order price  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
iceberg | string | Optional |  | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  
  
1\. After users join the `STP Group`, he can pass `stp_act` to limit the user's self-trade prevetion strategy. If `stp_act` is not passed, the default is `cn` strategy。  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter。  
3\. If the user did not use 'stp_act' when placing the order, 'stp_act' will return '-'  
  
\- cn: Cancel newest, Cancel new orders and keep old ones  
\- co: Cancel oldest, new ones  
\- cb: Cancel both, Both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object | Optional |  | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object | Optional |  | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
  
**stop_profit**

PatchSpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

PatchSpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
      
    
    {
      "order_id": "string",
      "amend_text": "string",
      "text": "string",
      "succeeded": true,
      "label": "string",
      "message": "string",
      "id": "string",
      "create_time": "string",
      "update_time": "string",
      "create_time_ms": 0,
      "update_time_ms": 0,
      "status": "open",
      "currency_pair": "string",
      "type": "limit",
      "account": "spot",
      "side": "buy",
      "amount": "string",
      "price": "string",
      "time_in_force": "gtc",
      "iceberg": "string",
      "auto_borrow": true,
      "auto_repay": true,
      "left": "string",
      "filled_amount": "string",
      "fill_price": "string",
      "filled_total": "string",
      "avg_deal_price": "string",
      "fee": "string",
      "fee_currency": "string",
      "point_fee": "string",
      "gt_fee": "string",
      "gt_discount": true,
      "rebated_fee": "string",
      "rebated_fee_currency": "string",
      "stp_id": 0,
      "stp_act": "cn",
      "finish_as": "open",
      "slippage": "string",
      "stop_profit": {
        "trigger_price": "string",
        "order_price": "string"
      },
      "stop_loss": {
        "trigger_price": "string",
        "order_price": "string"
      }
    }
    
    

##  SpotPovOrderCreator

Spot POV order creation request

Type | Constraints  
---|---  
object | required: ["currency_pair","side","amount","participation_rate","ttl"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Required |  | Currency pair  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Trade amount  
participation_rate | integer | Required |  | Target participation rate as a percentage. Valid values: 5, 10, 20, and 40  
ttl | string | Required |  | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d  
limit_price | string | Optional |  | Limit price. If omitted, the market price is used  
trigger_price | string | Optional |  | Trigger price. If omitted, the order is triggered immediately  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
      
    
    {
      "currency_pair": "string",
      "side": "buy",
      "amount": "string",
      "participation_rate": 0,
      "ttl": "string",
      "limit_price": "string",
      "trigger_price": "string",
      "text": "string"
    }
    
    

##  SystemTime

SystemTime

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
server_time | integer(int64) | Optional |  | Server current time(ms)  
      
    
    {
      "server_time": 0
    }
    
    

##  CurrencyPair

Spot currency pair

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Currency pair  
base | string | Optional |  | Base currency  
base_name | string | Optional |  | Base currency name  
quote | string | Optional |  | Quote currency  
quote_name | string | Optional |  | Quote currency name  
trade_quotes | array|null | Optional | nullable: true | Quote currencies supported by the unified market; null means that the market does not support unified quote currencies  
fee | string | Optional |  | Trading fee rate(deprecated)  
min_base_amount | string | Optional |  | Minimum amount of base currency to trade, `null` means no limit  
min_quote_amount | string | Optional |  | Minimum amount of quote currency to trade, `null` means no limit  
max_base_amount | string | Optional |  | Maximum amount of base currency to trade, `null` means no limit  
max_quote_amount | string | Optional |  | Maximum amount of quote currency to trade, `null` means no limit  
amount_precision | integer | Optional |  | Quantity precision  
precision | integer | Optional |  | Price precision  
trade_status | string | Optional | enum: ["untradable","buyable","sellable","tradable"] | Trading status  
  
\- untradable: cannot be traded  
\- buyable: can be bought  
\- sellable: can be sold  
\- tradable: can be bought and sold  
sell_start | integer(int64) | Optional |  | Sell start unix timestamp in seconds  
buy_start | integer(int64) | Optional |  | Buy start unix timestamp in seconds  
delisting_time | integer(int64) | Optional |  | Expected delisting time as a Unix timestamp in seconds.  
type | string | Optional |  | Trading pair type, normal: normal, premarket: pre-market  
trade_url | string | Optional |  | Transaction link  
st_tag | boolean | Optional |  | Whether the trading pair is in ST risk assessment, false - No, true - Yes  
up_rate | string | Optional |  | Maximum Quote Rise Percentage  
down_rate | string | Optional |  | Maximum Quote Decline Percentage  
slippage | string | Optional |  | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
market_order_max_stock | string | Optional |  | Maximum market order quantity. `null` or `0` means no limit  
market_order_max_money | string | Optional |  | Maximum market order amount. `null` or `0` means no limit  
  
**trade_quotes**

Quote currencies supported by the unified market; null means that the market does not support unified quote currencies

Type | Constraints  
---|---  
array|null | nullable: true  
  
**trade_quotes / items**

Type | Constraints  
---|---  
string |   
      
    
    {
      "id": "string",
      "base": "string",
      "base_name": "string",
      "quote": "string",
      "quote_name": "string",
      "trade_quotes": [
        "string"
      ],
      "fee": "string",
      "min_base_amount": "string",
      "min_quote_amount": "string",
      "max_base_amount": "string",
      "max_quote_amount": "string",
      "amount_precision": 0,
      "precision": 0,
      "trade_status": "untradable",
      "sell_start": 0,
      "buy_start": 0,
      "delisting_time": 0,
      "type": "string",
      "trade_url": "string",
      "st_tag": true,
      "up_rate": "string",
      "down_rate": "string",
      "slippage": "string",
      "market_order_max_stock": "string",
      "market_order_max_money": "string"
    }
    
    

##  CountdownCancelAllSpotTask

CountdownCancelAllSpotTask

Countdown cancel task details

Type | Constraints  
---|---  
object | required: ["timeout"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timeout | integer(int32) | Required |  | Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown  
currency_pair | string | Optional |  | Currency pair  
      
    
    {
      "timeout": 0,
      "currency_pair": "string"
    }
    
    

##  SpotInsuranceHistory

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency | string | Optional |  | Currency  
balance | string | Optional |  | Balance  
time | integer(int64) | Optional |  | Creation time, timestamp, milliseconds  
      
    
    {
      "currency": "string",
      "balance": "string",
      "time": 0
    }
    
    

##  TriggerTime

triggerTime

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
triggerTime | integer(int64) | Optional |  | Timestamp when countdown ends, in milliseconds  
      
    
    {
      "triggerTime": "1660039145000"
    }
    
    

##  SpotPricePutOrder

Type | Constraints  
---|---  
object | required: ["side","price","amount","account","time_in_force"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
side | string | Required | enum: ["buy","sell"] | Order side  
  
\- buy: buy side  
\- sell: sell side  
price | string | Required |  | Order price  
amount | string | Required |  | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
account | string | Required | enum: ["normal","margin","unified"]  
default: "normal" | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
time_in_force | string | Required | enum: ["gtc","ioc"]  
default: "gtc" | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
auto_borrow | boolean | Optional | default: false | Whether to borrow coins automatically  
auto_repay | boolean | Optional | default: false | Whether to repay the loan automatically  
text | string | Optional |  | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
      
    
    {
      "type": "limit",
      "side": "buy",
      "price": "string",
      "amount": "string",
      "account": "normal",
      "time_in_force": "gtc",
      "auto_borrow": false,
      "auto_repay": false,
      "text": "string"
    }
    
    

##  SpotFee

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | User ID  
taker_fee | string | Optional |  | taker fee rate  
maker_fee | string | Optional |  | maker fee rate  
rpi_maker_fee | string | Optional |  | RPI MM maker fee rate  
gt_discount | boolean | Optional |  | Whether GT deduction discount is enabled  
gt_taker_fee | string | Optional |  | Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  
gt_maker_fee | string | Optional |  | Maker fee rate with GT deduction. Returns 0 if GT deduction is disabled  
loan_fee | string | Optional |  | Loan fee rate of margin lending  
point_type | string | Optional |  | Point card type: 0 - Original version, 1 - New version since 202009  
currency_pair | string | Optional |  | Currency pair  
debit_fee | integer | Optional |  | Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  
rpi_mm | integer | Optional |  | RPI MM Level  
      
    
    {
      "user_id": 0,
      "taker_fee": "string",
      "maker_fee": "string",
      "rpi_maker_fee": "string",
      "gt_discount": true,
      "gt_taker_fee": "string",
      "gt_maker_fee": "string",
      "loan_fee": "string",
      "point_type": "string",
      "currency_pair": "string",
      "debit_fee": 0,
      "rpi_mm": 0
    }
    
    

##  OrderPatch

Spot order details

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
account | string | Optional |  | Specify query account  
amount | string | Optional |  | Trading quantity. Either `amount` or `price` must be specified  
price | string | Optional |  | Trading price. Either `amount` or `price` must be specified  
amend_text | string | Optional | maxLength: 31 | Custom info during order amendment  
action_mode | string | Optional |  | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
  
**stop_profit**

PatchSpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

PatchSpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
      
    
    {
      "currency_pair": "string",
      "account": "string",
      "amount": "string",
      "price": "string",
      "amend_text": "string",
      "action_mode": "string",
      "stop_profit": {
        "trigger_price": "string",
        "order_price": "string"
      },
      "stop_loss": {
        "trigger_price": "string",
        "order_price": "string"
      }
    }
    
    

##  CancelBatchOrder

Info of order to be cancelled

Type | Constraints  
---|---  
object | required: ["currency_pair","id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Required |  | Order currency pair  
id | string | Required |  | Order ID or user custom ID.  
Custom ID are accepted only within 30 minutes after order creation  
account | string | Optional |  | If the canceled order is a unified account apikey, this field must be specified and set to `unified`  
action_mode | string | Optional |  | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
      
    
    {
      "currency_pair": "string",
      "id": "string",
      "account": "string",
      "action_mode": "string"
    }
    
    

##  Ticker

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
last | string | Optional |  | Last trading price  
lowest_ask | string | Optional |  | Recent lowest ask  
lowest_size | string | Optional |  | Latest seller's lowest price quantity; not available for batch queries; available for single queries, empty if no data  
highest_bid | string | Optional |  | Recent highest bid  
highest_size | string | Optional |  | Latest buyer's highest price quantity; not available for batch queries; available for single queries, empty if no data  
change_percentage | string | Optional |  | 24h price change percentage (negative for decrease, e.g., -7.45)  
change_utc0 | string | Optional |  | UTC+0 timezone, 24h price change percentage, negative for decline (e.g., -7.45)  
change_utc8 | string | Optional |  | UTC+8 timezone, 24h price change percentage, negative for decline (e.g., -7.45)  
base_volume | string | Optional |  | Base currency trading volume in the last 24h  
quote_volume | string | Optional |  | Quote currency trading volume in the last 24h  
high_24h | string | Optional |  | 24h High  
low_24h | string | Optional |  | 24h Low  
etf_net_value | string | Optional |  | ETF net value  
etf_pre_net_value | string|null | Optional | nullable: true | ETF net value at previous rebalancing point  
etf_pre_timestamp | integer(int64)|null | Optional | nullable: true | ETF previous rebalancing time  
etf_leverage | string|null | Optional | nullable: true | ETF current leverage  
      
    
    {
      "currency_pair": "string",
      "last": "string",
      "lowest_ask": "string",
      "lowest_size": "string",
      "highest_bid": "string",
      "highest_size": "string",
      "change_percentage": "string",
      "change_utc0": "string",
      "change_utc8": "string",
      "base_volume": "string",
      "quote_volume": "string",
      "high_24h": "string",
      "low_24h": "string",
      "etf_net_value": "string",
      "etf_pre_net_value": "string",
      "etf_pre_timestamp": 0,
      "etf_leverage": "string"
    }
    
    

##  OrderCancel

Spot order details

Type | Constraints  
---|---  
object | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
succeeded | boolean | Optional |  | Request execution result  
label | string | Optional |  | Error label, if any, otherwise an empty string  
message | string | Optional |  | Detailed error message, if any, otherwise an empty string  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Trading quantity  
When `type` is `limit`, it refers to the base currency (the currency being traded), such as `BTC` in `BTC_USDT`  
When `type` is `market`, it refers to different currencies based on the side:  
\- `side`: `buy` refers to quote currency, `BTC_USDT` means `USDT`  
\- `side`: `sell` refers to base currency, `BTC_USDT` means `BTC`  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
iceberg | string | Optional |  | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","ioc","stp"]  
readOnly: true | How the order was finished.  
  
\- open: processing  
\- filled: filled totally  
\- cancelled: manually cancelled  
\- ioc: time in force is `IOC`, finish immediately  
\- stp: cancelled because self trade prevention  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
      
    
    {
      "id": "string",
      "text": "string",
      "amend_text": "string",
      "succeeded": true,
      "label": "string",
      "message": "string",
      "create_time": "string",
      "update_time": "string",
      "create_time_ms": 0,
      "update_time_ms": 0,
      "status": "open",
      "currency_pair": "string",
      "type": "limit",
      "account": "spot",
      "side": "buy",
      "amount": "string",
      "price": "string",
      "time_in_force": "gtc",
      "iceberg": "string",
      "auto_borrow": true,
      "auto_repay": true,
      "left": "string",
      "filled_amount": "string",
      "fill_price": "string",
      "filled_total": "string",
      "avg_deal_price": "string",
      "fee": "string",
      "fee_currency": "string",
      "point_fee": "string",
      "gt_fee": "string",
      "gt_maker_fee": "string",
      "gt_taker_fee": "string",
      "gt_discount": true,
      "rebated_fee": "string",
      "rebated_fee_currency": "string",
      "stp_id": 0,
      "stp_act": "cn",
      "finish_as": "open",
      "action_mode": "string"
    }
    
    

##  Order

Spot order details

Type | Constraints  
---|---  
object | required: ["currency_pair","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Order ID  
text | string | Optional |  | User defined information. If not empty, must follow the rules below:  
  
1\. prefixed with `t-`  
2\. no longer than 28 bytes without `t-` prefix  
3\. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
  
Besides user defined information, reserved contents are listed below, denoting how the order is created:  
  
\- 101: from android  
\- 102: from IOS  
\- 103: from IPAD  
\- 104: from webapp  
\- 3: from web  
\- 2: from apiv2  
\- apiv4: from apiv4  
pm_liquidate, comb_margin_liquidate, and scm_liquidate represent cross-margin liquidation orders  
liquidate represents isolated-margin liquidation orders  
amend_text | string | Optional | readOnly: true | The custom data that the user remarked when amending the order  
create_time | string | Optional | readOnly: true | Creation time of order  
update_time | string | Optional | readOnly: true | Last modification time of order  
create_time_ms | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | readOnly: true | Last modification time of order (in milliseconds)  
status | string | Optional | enum: ["open","closed","cancelled"]  
readOnly: true | Order status:  
  
\- `open`: pending  
\- `closed`: ended  
\- `cancelled`: cancelled  
currency_pair | string | Required |  | Currency pair  
trade_quote | string | Optional |  | Actual quote currency used for the trade; can be specified only in a unified market  
type | string | Optional | enum: ["limit","market"]  
default: "limit" | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | default: "spot" | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | enum: ["buy","sell"] | Buy or sell order  
amount | string | Required |  | Order amount.  
  
\- `type=limit`: measured in the base currency.  
\- `type=market`: `side=buy` uses the quote currency; `side=sell` uses the base currency.  
  
For `BTC_USDT`, the base currency is `BTC` and the quote currency is `USDT`.  
price | string | Optional |  | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force:  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, immediate execution or cancellation, taker-only  
\- poc: PendingOrCancelled, post-only, maker-only  
\- fok: FillOrKill, fill in full or cancel in full  
  
For `type=market`, only `ioc` and `fok` are supported.  
iceberg | string | Optional |  | Displayed amount of an iceberg order. Omit this field or pass "0" for a regular order. Fully hidden orders are not supported.  
auto_borrow | boolean | Optional | writeOnly: true | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional |  | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | readOnly: true | Amount left to fill  
filled_amount | string | Optional | readOnly: true | Amount filled  
fill_price | string | Optional | readOnly: true | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | readOnly: true | Total filled in quote currency  
avg_deal_price | string | Optional | readOnly: true | Average fill price  
fee | string | Optional | readOnly: true | Fee deducted  
fee_currency | string | Optional | readOnly: true | Fee currency unit  
point_fee | string | Optional | readOnly: true | Points used to deduct fee  
gt_fee | string | Optional | readOnly: true | GT used to deduct fee  
gt_maker_fee | string | Optional | readOnly: true | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | readOnly: true | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | readOnly: true | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | readOnly: true | Rebated fee  
rebated_fee_currency | string | Optional | readOnly: true | Rebated fee currency unit  
stp_id | integer | Optional | readOnly: true | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | enum: ["cn","co","cb","-"] | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
finish_as | string | Optional | enum: ["open","filled","cancelled","liquidate_cancelled","depth_not_enough","trader_not_enough","small","ioc","poc","fok","stp","price_protect_cancelled","unknown"]  
readOnly: true | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only requirement not met because time-in-force is set to poc (maker-only); rejected after being detected as taker  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | writeOnly: true | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | writeOnly: true | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object|null | Optional | nullable: true | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
stop_loss | object|null | Optional | nullable: true | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
use_earn | boolean|null | Optional | nullable: true | Redeem Simple Earn funds when placing an order  
  
**stop_profit**

SpotOrderStopProfit

Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
order_price | string | Optional |  | Take profit order price  
  
**stop_loss**

SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trigger_price | string | Optional |  | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
order_price | string | Optional |  | Stop-loss order price  
      
    
    {
      "id": "string",
      "text": "string",
      "amend_text": "string",
      "create_time": "string",
      "update_time": "string",
      "create_time_ms": 0,
      "update_time_ms": 0,
      "status": "open",
      "currency_pair": "string",
      "trade_quote": "string",
      "type": "limit",
      "account": "spot",
      "side": "buy",
      "amount": "string",
      "price": "string",
      "time_in_force": "gtc",
      "iceberg": "string",
      "auto_borrow": true,
      "auto_repay": true,
      "left": "string",
      "filled_amount": "string",
      "fill_price": "string",
      "filled_total": "string",
      "avg_deal_price": "string",
      "fee": "string",
      "fee_currency": "string",
      "point_fee": "string",
      "gt_fee": "string",
      "gt_maker_fee": "string",
      "gt_taker_fee": "string",
      "gt_discount": true,
      "rebated_fee": "string",
      "rebated_fee_currency": "string",
      "stp_id": 0,
      "stp_act": "cn",
      "finish_as": "open",
      "action_mode": "string",
      "slippage": "string",
      "stop_profit": {
        "trigger_price": "string",
        "order_price": "string"
      },
      "stop_loss": {
        "trigger_price": "string",
        "order_price": "string"
      },
      "use_earn": true
    }
    
    

##  Currency

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency | string | Optional |  | Currency symbol  
name | string | Optional |  | Currency name  
delisted | boolean | Optional |  | Whether currency is de-listed  
withdraw_disabled | boolean | Optional |  | Whether currency's withdrawal is disabled (deprecated)  
withdraw_delayed | boolean | Optional |  | Whether currency's withdrawal is delayed (deprecated)  
deposit_disabled | boolean | Optional |  | Whether currency's deposit is disabled (deprecated)  
trade_disabled | boolean | Optional |  | Whether currency's trading is disabled  
fixed_rate | string | Optional |  | Fixed fee rate. Only for fixed rate currencies, not valid for normal currencies  
chain | string | Optional |  | The main chain corresponding to the coin  
chains | array | Optional |  | All blockchains associated with this currency.  
total_supply | string | Optional |  | Total supply  
market_cap | string | Optional |  | Market cap  
category | array | Optional |  | Currency categories  
\- stocks: Stocks  
\- metals: Metals  
\- indices: Indices  
\- forex: Forex  
\- commodities: Commodities  
  
**chains**

All blockchains associated with this currency.

Type | Constraints  
---|---  
array |   
  
**chains / items**

SpotCurrencyChain

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Optional |  | Blockchain name  
addr | string | Optional |  | token address  
withdraw_disabled | boolean | Optional |  | Whether currency's withdrawal is disabled  
withdraw_delayed | boolean | Optional |  | Whether currency's withdrawal is delayed  
deposit_disabled | boolean | Optional |  | Whether currency's deposit is disabled  
  
**category**

Currency categories

  * stocks: Stocks
  * metals: Metals
  * indices: Indices
  * forex: Forex
  * commodities: Commodities

Type | Constraints  
---|---  
array |   
  
**category / items**

Type | Constraints  
---|---  
string |   
      
    
    {
      "currency": "string",
      "name": "string",
      "delisted": true,
      "withdraw_disabled": true,
      "withdraw_delayed": true,
      "deposit_disabled": true,
      "trade_disabled": true,
      "fixed_rate": "string",
      "chain": "string",
      "chains": [
        {
          "name": "string",
          "addr": "string",
          "withdraw_disabled": true,
          "withdraw_delayed": true,
          "deposit_disabled": true
        }
      ],
      "total_supply": "string",
      "market_cap": "string",
      "category": [
        "string"
      ]
    }
    
    

##  SpotPriceTrigger

Type | Constraints  
---|---  
object | required: ["price","rule"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | Trigger price  
rule | string | Required | enum: [">=","<="] | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
expiration | integer | Optional |  | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
      
    
    {
      "price": "string",
      "rule": ">=",
      "expiration": 0
    }
    
    

##  Trade

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Fill ID  
create_time | string | Optional |  | Fill Time  
create_time_ms | string | Optional |  | Trading time, with millisecond precision  
currency_pair | string | Optional |  | Currency pair  
side | string | Optional | enum: ["buy","sell"] | Buy or sell order  
role | string | Optional | enum: ["taker","maker"] | Trade role, not returned in public endpoints  
amount | string | Optional |  | Trade amount  
price | string | Optional |  | Trade price.  
order_id | string | Optional |  | Related order ID, not returned in public endpoints  
fee | string | Optional |  | Fee deducted, not returned in public endpoints  
fee_currency | string | Optional |  | Fee currency unit, not returned in public endpoints  
point_fee | string | Optional |  | Points used to deduct fee, not returned in public endpoints  
gt_fee | string | Optional |  | GT used to deduct fee, not returned in public endpoints  
amend_text | string | Optional |  | The custom data that the user remarked when amending the order  
sequence_id | string | Optional |  | Consecutive trade ID within a single market.  
Used to track and identify trades in the specific market  
text | string | Optional |  | Order's Custom Information. This field is not returned by public interfaces.  
The scenarios pm_liquidate, comb_margin_liquidate, and scm_liquidate represent full-account forced liquidation orders.  
liquidate represents isolated-account forced liquidation orders.  
deal | string | Optional |  | Total Executed Value  
trade_quote | string | Optional |  | Actual quote currency used for the trade  
      
    
    {
      "id": "string",
      "create_time": "string",
      "create_time_ms": "string",
      "currency_pair": "string",
      "side": "buy",
      "role": "taker",
      "amount": "string",
      "price": "string",
      "order_id": "string",
      "fee": "string",
      "fee_currency": "string",
      "point_fee": "string",
      "gt_fee": "string",
      "amend_text": "string",
      "sequence_id": "string",
      "text": "string",
      "deal": "string",
      "trade_quote": "string"
    }