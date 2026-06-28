---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/spot
api_type: Trading
updated_at: 2026-05-27 20:16:00.541862
---

# Spot

Spot trading

##  Query all currency information

GET`/spot/currencies`

GET `/spot/currencies`

_Query all currency information_

When a currency corresponds to multiple chains, you can query the information of multiple chains through the `chains` field, such as the charging and recharge status, identification, etc. of the chain

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Currency]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» currency | string | Currency symbol  
» name | string | Currency name  
» delisted | boolean | Whether currency is de-listed  
» withdraw_disabled | boolean | Whether currency's withdrawal is disabled (deprecated)  
» withdraw_delayed | boolean | Whether currency's withdrawal is delayed (deprecated)  
» deposit_disabled | boolean | Whether currency's deposit is disabled (deprecated)  
» trade_disabled | boolean | Whether currency's trading is disabled  
» fixed_rate | string | Fixed fee rate. Only for fixed rate currencies, not valid for normal currencies  
» chain | string | The main chain corresponding to the coin  
» chains | array | All links corresponding to coins  
»» SpotCurrencyChain | object | none  
»»» name | string | Blockchain name  
»»» addr | string | token address  
»»» withdraw_disabled | boolean | Whether currency's withdrawal is disabled  
»»» withdraw_delayed | boolean | Whether currency's withdrawal is delayed  
»»» deposit_disabled | boolean | Whether currency's deposit is disabled  
»» total_supply | string | Total supply  
»» market_cap | string | Market cap  
»» category | array | Currency categories  
\- stocks: Stocks  
\- metals: Metals  
\- indices: Indices  
\- forex: Forex  
\- commodities: Commodities  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Currency  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» currency | string | Currency symbol  
» name | string | Currency name  
» delisted | boolean | Whether currency is de-listed  
» withdraw_disabled | boolean | Whether currency's withdrawal is disabled (deprecated)  
» withdraw_delayed | boolean | Whether currency's withdrawal is delayed (deprecated)  
» deposit_disabled | boolean | Whether currency's deposit is disabled (deprecated)  
» trade_disabled | boolean | Whether currency's trading is disabled  
» fixed_rate | string | Fixed fee rate. Only for fixed rate currencies, not valid for normal currencies  
» chain | string | The main chain corresponding to the coin  
» chains | array | All links corresponding to coins  
»» SpotCurrencyChain | object | none  
»»» name | string | Blockchain name  
»»» addr | string | token address  
»»» withdraw_disabled | boolean | Whether currency's withdrawal is disabled  
»»» withdraw_delayed | boolean | Whether currency's withdrawal is delayed  
»»» deposit_disabled | boolean | Whether currency's deposit is disabled  
»» total_supply | string | Total supply  
»» market_cap | string | Market cap  
»» category | array | Currency categories  
\- stocks: Stocks  
\- metals: Metals  
\- indices: Indices  
\- forex: Forex  
\- commodities: Commodities  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)All currency pairs retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | All currency pairs retrieved | [CurrencyPair]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Spot currency pair]  
» _None_ | CurrencyPair | Spot currency pair  
»» id | string | Currency pair  
»» base | string | Base currency  
»» base_name | string | Base currency name  
»» quote | string | Quote currency  
»» quote_name | string | Quote currency name  
»» fee | string | Trading fee rate(deprecated)  
»» min_base_amount | string | Minimum amount of base currency to trade, `null` means no limit  
»» min_quote_amount | string | Minimum amount of quote currency to trade, `null` means no limit  
»» max_base_amount | string | Maximum amount of base currency to trade, `null` means no limit  
»» max_quote_amount | string | Maximum amount of quote currency to trade, `null` means no limit  
»» amount_precision | integer | Amount scale  
»» precision | integer | Price scale  
»» trade_status | string | Trading status  
  
\- untradable: cannot be traded  
\- buyable: can be bought  
\- sellable: can be sold  
\- tradable: can be bought and sold  
»» sell_start | integer(int64) | Sell start unix timestamp in seconds  
»» buy_start | integer(int64) | Buy start unix timestamp in seconds  
»» delisting_time | integer(int64) | Expected time to remove the shelves, Unix timestamp in seconds  
»» type | string | Trading pair type, normal: normal, premarket: pre-market  
»» trade_url | string | Transaction link  
»» st_tag | boolean | Whether the trading pair is in ST risk assessment, false - No, true - Yes  
»» up_rate | string | Maximum Quote Rise Percentage  
»» down_rate | string | Maximum Quote Decline Percentage  
»» slippage | string | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
»» market_order_max_stock | string | Maximum Market Order Quantity  
»» market_order_max_money | string | Maximum Market Order Amount  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
trade_status | untradable  
trade_status | buyable  
trade_status | sellable  
trade_status | tradable  
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
        "trade_url": "https://www.gate.io/trade/ETH_USDT",
        "st_tag": false,
        "up_rate": "0.05",
        "down_rate": "0.02",
        "slippage": "0.05",
        "max_market_order_stock": "100000",
        "max_market_order_money": "1000000"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | CurrencyPair  
  
### Response Schema

Status Code **200**

_Spot currency pair_

Name | Type | Description  
---|---|---  
» id | string | Currency pair  
» base | string | Base currency  
» base_name | string | Base currency name  
» quote | string | Quote currency  
» quote_name | string | Quote currency name  
» fee | string | Trading fee rate(deprecated)  
» min_base_amount | string | Minimum amount of base currency to trade, `null` means no limit  
» min_quote_amount | string | Minimum amount of quote currency to trade, `null` means no limit  
» max_base_amount | string | Maximum amount of base currency to trade, `null` means no limit  
» max_quote_amount | string | Maximum amount of quote currency to trade, `null` means no limit  
» amount_precision | integer | Amount scale  
» precision | integer | Price scale  
» trade_status | string | Trading status  
  
\- untradable: cannot be traded  
\- buyable: can be bought  
\- sellable: can be sold  
\- tradable: can be bought and sold  
» sell_start | integer(int64) | Sell start unix timestamp in seconds  
» buy_start | integer(int64) | Buy start unix timestamp in seconds  
» delisting_time | integer(int64) | Expected time to remove the shelves, Unix timestamp in seconds  
» type | string | Trading pair type, normal: normal, premarket: pre-market  
» trade_url | string | Transaction link  
» st_tag | boolean | Whether the trading pair is in ST risk assessment, false - No, true - Yes  
» up_rate | string | Maximum Quote Rise Percentage  
» down_rate | string | Maximum Quote Decline Percentage  
» slippage | string | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
» market_order_max_stock | string | Maximum Market Order Quantity  
» market_order_max_money | string | Maximum Market Order Amount  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
trade_status | untradable  
trade_status | buyable  
trade_status | sellable  
trade_status | tradable  
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
      "trade_url": "https://www.gate.io/trade/ETH_USDT",
      "st_tag": false,
      "up_rate": "0.05",
      "down_rate": "0.02",
      "slippage": "0.05",
      "max_market_order_stock": "100000",
      "max_market_order_money": "1000000"
    }
    

##  Get currency pair ticker information

GET`/spot/tickers`

GET `/spot/tickers`

Get `currency pair ticker information`

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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [Ticker]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» currency_pair | string | Currency pair  
» last | string | Last trading price  
» lowest_ask | string | Recent lowest ask  
» lowest_size | string | Latest seller's lowest price quantity; not available for batch queries; available for single queries, empty if no data  
» highest_bid | string | Recent highest bid  
» highest_size | string | Latest buyer's highest price quantity; not available for batch queries; available for single queries, empty if no data  
» change_percentage | string | 24h price change percentage (negative for decrease, e.g., -7.45)  
» change_utc0 | string | UTC+0 timezone, 24h price change percentage, negative for decline (e.g., -7.45)  
» change_utc8 | string | UTC+8 timezone, 24h price change percentage, negative for decline (e.g., -7.45)  
» base_volume | string | Base currency trading volume in the last 24h  
» quote_volume | string | Quote currency trading volume in the last 24h  
» high_24h | string | 24h High  
» low_24h | string | 24h Low  
» etf_net_value | string | ETF net value  
» etf_pre_net_value | string|null | ETF net value at previous rebalancing point  
» etf_pre_timestamp | integer(int64)|null | ETF previous rebalancing time  
» etf_leverage | string|null | ETF current leverage  
  
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

Get `market depth information`

Market depth buy orders are sorted by price from high to low, sell orders are reversed

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Required | Currency pair  
interval | query | string | Optional | Price precision for merged depth. 0 means no merging. If not specified, defaults to 0  
limit | query | integer | Optional | Number of depth levels  
with_id | query | boolean | Optional | Return order book update ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OrderBook  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» id | integer(int64) | Order book ID, which is updated whenever the order book is changed. Valid only when `with_id` is set to `true`  
» current | integer(int64) | The timestamp of the response data being generated (in milliseconds)  
» update | integer(int64) | The timestamp of when the orderbook last changed (in milliseconds)  
» asks | array | Ask Depth  
»» _None_ | array | Price and Quantity Pair  
» bids | array | Bid Depth  
»» _None_ | array | Price and Quantity Pair  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Trade]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | string | Fill ID  
» create_time | string | Fill Time  
» create_time_ms | string | Trading time, with millisecond precision  
» currency_pair | string | Currency pair  
» side | string | Buy or sell order  
» role | string | Trade role, not returned in public endpoints  
» amount | string | Trade amount  
» price | string | Order price  
» order_id | string | Related order ID, not returned in public endpoints  
» fee | string | Fee deducted, not returned in public endpoints  
» fee_currency | string | Fee currency unit, not returned in public endpoints  
» point_fee | string | Points used to deduct fee, not returned in public endpoints  
» gt_fee | string | GT used to deduct fee, not returned in public endpoints  
» amend_text | string | The custom data that the user remarked when amending the order  
» sequence_id | string | Consecutive trade ID within a single market.  
Used to track and identify trades in the specific market  
» text | string | Order's Custom Information. This field is not returned by public interfaces.  
The scenarios pm_liquidate, comb_margin_liquidate, and scm_liquidate represent full-account forced liquidation orders.  
liquidate represents isolated-account forced liquidation orders.  
» deal | string | Total Executed Value  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
side | buy  
side | sell  
role | taker  
role | maker  
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
        "deal": "0.0045"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [[string]]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» _None_ | array | Candlestick data for each time granularity, from left to right:  
  
\- Unix timestamp with second precision  
\- Trading volume in quote currency  
\- Closing price  
\- Highest price  
\- Lowest price  
\- Opening price  
\- Trading volume in base currency  
\- Whether window is closed; true means this candlestick data segment is complete, false means not yet complete  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | SpotFee  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» user_id | integer(int64) | User ID  
» taker_fee | string | taker fee rate  
» maker_fee | string | maker fee rate  
» rpi_maker_fee | string | RPI MM maker fee rate  
» gt_discount | boolean | Whether GT deduction discount is enabled  
» gt_taker_fee | string | Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  
» gt_maker_fee | string | Maker fee rate with GT deduction. Returns 0 if GT deduction is disabled  
» loan_fee | string | Loan fee rate of margin lending  
» point_type | string | Point card type: 0 - Original version, 1 - New version since 202009  
» currency_pair | string | Currency pair  
» debit_fee | integer | Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  
» rpi_mm | integer | RPI MM Level  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Inline  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» **additionalProperties** | SpotFee | none  
»» user_id | integer(int64) | User ID  
»» taker_fee | string | taker fee rate  
»» maker_fee | string | maker fee rate  
»» rpi_maker_fee | string | RPI MM maker fee rate  
»» gt_discount | boolean | Whether GT deduction discount is enabled  
»» gt_taker_fee | string | Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  
»» gt_maker_fee | string | Maker fee rate with GT deduction. Returns 0 if GT deduction is disabled  
»» loan_fee | string | Loan fee rate of margin lending  
»» point_type | string | Point card type: 0 - Original version, 1 - New version since 202009  
»» currency_pair | string | Currency pair  
»» debit_fee | integer | Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  
»» rpi_mm | integer | RPI MM Level  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SpotAccount]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» currency | string | Currency detail  
» available | string | Available amount  
» locked | string | Locked amount, used in trading  
» update_id | integer(int64) | Version number  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SpotAccountBook]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | string | Balance change record ID  
» time | integer(int64) | The timestamp of the change (in milliseconds)  
» currency | string | Currency changed  
» change | string | Amount changed. Positive value means transferring in, while negative out  
» balance | string | Balance after change  
» type | string | Account change type; deprecated (see `code` for account change type encoding)  
» code | string | Account change code, see [Asset Record Code] (Asset Record Code)  
» text | string | Additional information  
  
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
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request execution completed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request execution completed | [BatchOrder]  
  
### Response Schema

Status Code **200**

_Contains multiple order objects; for the specific structure of the order object, refer to the structure of the /spot/orders order placement interface_

Name | Type | Description  
---|---|---  
_None_ | array | Contains multiple order objects; for the specific structure of the order object, refer to the structure of the /spot/orders order placement interface  
» _None_ | BatchOrder | Batch order details  
»» order_id | string | Order ID  
»» amend_text | string | The custom data that the user remarked when amending the order  
»» text | string | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
»» succeeded | boolean | Request execution result  
»» label | string | Error label, if any, otherwise an empty string  
»» message | string | Detailed error message, if any, otherwise an empty string  
»» id | string | Order ID  
»» create_time | string | Creation time of order  
»» update_time | string | Last modification time of order  
»» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
»» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
»» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
»» currency_pair | string | Currency pair  
»» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
»» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
»» side | string | Buy or sell order  
»» amount | string | Trade amount  
»» price | string | Order price  
»» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
»» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
»» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
»» left | string | Amount left to fill  
»» filled_amount | string | Amount filled  
»» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
»» filled_total | string | Total filled in quote currency  
»» avg_deal_price | string | Average fill price  
»» fee | string | Fee deducted  
»» fee_currency | string | Fee currency unit  
»» point_fee | string | Points used to deduct fee  
»» gt_fee | string | GT used to deduct fee  
»» gt_discount | boolean | Whether GT fee deduction is enabled  
»» rebated_fee | string | Rebated fee  
»» rebated_fee_currency | string | Rebated fee currency unit  
»» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
»» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  
  
1\. After users join the `STP Group`, he can pass `stp_act` to limit the user's self-trade prevetion strategy. If `stp_act` is not passed, the default is `cn` strategy。  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter。  
3\. If the user did not use 'stp_act' when placing the order, 'stp_act' will return '-'  
  
\- cn: Cancel newest, Cancel new orders and keep old ones  
\- co: Cancel oldest, new ones  
\- cb: Cancel both, Both old and new orders will be cancelled  
»» finish_as | string | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
»» stop_profit | object | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
»»» trigger_price | string | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
»»» order_price | string | Take profit order price  
»» stop_loss | object | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
»»» trigger_price | string | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
»»» order_price | string | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
account | spot  
account | margin  
account | cross_margin  
account | unified  
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
    body='[{"text":"t-abc123","currency_pair":"BTC_USDT","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}]'
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
    body_param='[{"text":"t-abc123","currency_pair":"BTC_USDT","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}]'
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [OpenOrders]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» currency_pair | string | Currency pair  
» total | integer | Total number of open orders for this trading pair on the current page  
» orders | array | none  
»» _None_ | object | Spot order details  
»»» id | string | Order ID  
»»» text | string | User defined information. If not empty, must follow the rules below:  
  
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
»»» amend_text | string | The custom data that the user remarked when amending the order  
»»» create_time | string | Creation time of order  
»»» update_time | string | Last modification time of order  
»»» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
»»» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
»»» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
»»» currency_pair | string | Currency pair  
»»» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
»»» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
»»» side | string | Buy or sell order  
»»» amount | string | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
»»» price | string | Trading price, required when `type`=`limit`  
»»» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
»»» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
»»» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
»»» left | string | Amount left to fill  
»»» filled_amount | string | Amount filled  
»»» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
»»» filled_total | string | Total filled in quote currency  
»»» avg_deal_price | string | Average fill price  
»»» fee | string | Fee deducted  
»»» fee_currency | string | Fee currency unit  
»»» point_fee | string | Points used to deduct fee  
»»» gt_fee | string | GT used to deduct fee  
»»» gt_maker_fee | string | GT amount used to deduct maker fee  
»»» gt_taker_fee | string | GT amount used to deduct taker fee  
»»» gt_discount | boolean | Whether GT fee deduction is enabled  
»»» rebated_fee | string | Rebated fee  
»»» rebated_fee_currency | string | Rebated fee currency unit  
»»» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
»»» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
»»» finish_as | string | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
»»» stop_profit | object | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
»»»» trigger_price | string | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
»»»» order_price | string | Take profit order price  
»»» stop_loss | object | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
»»»» trigger_price | string | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
»»»» order_price | string | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
↳ text | body | string | Optional | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
↳ currency_pair | body | string | Required | Currency pair  
↳ amount | body | string | Required | Trade amount  
↳ price | body | string | Required | Order price  
↳ action_mode | body | string | Optional | Processing mode:  
  
Different fields are returned when placing an order based on action_mode. This field is only valid during the request and is not included in the response  
`ACK`: Asynchronous mode, only returns key order fields  
`RESULT`: No liquidation information  
`FULL`: Full mode (default)  
  
####  Detailed descriptions

**» text** : Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)

**» action_mode** : Processing mode:  
  
Different fields are returned when placing an order based on action_mode. This field is only valid during the request and is not included in the response  
`ACK`: Asynchronous mode, only returns key order fields  
`RESULT`: No liquidation information  
`FULL`: Full mode (default)

### Responses

  * 201[Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2)Order created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order created successfully | Order  
  
### Response Schema

Status Code **201**

_Spot order details_

Name | Type | Description  
---|---|---  
» id | string | Order ID  
» text | string | User defined information. If not empty, must follow the rules below:  
  
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
» amend_text | string | The custom data that the user remarked when amending the order  
» create_time | string | Creation time of order  
» update_time | string | Last modification time of order  
» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
» currency_pair | string | Currency pair  
» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
» side | string | Buy or sell order  
» amount | string | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
» price | string | Trading price, required when `type`=`limit`  
» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
» left | string | Amount left to fill  
» filled_amount | string | Amount filled  
» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
» filled_total | string | Total filled in quote currency  
» avg_deal_price | string | Average fill price  
» fee | string | Fee deducted  
» fee_currency | string | Fee currency unit  
» point_fee | string | Points used to deduct fee  
» gt_fee | string | GT used to deduct fee  
» gt_maker_fee | string | GT amount used to deduct maker fee  
» gt_taker_fee | string | GT amount used to deduct taker fee  
» gt_discount | boolean | Whether GT fee deduction is enabled  
» rebated_fee | string | Rebated fee  
» rebated_fee_currency | string | Rebated fee currency unit  
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
» finish_as | string | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
» stop_profit | object | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
»» trigger_price | string | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
»» order_price | string | Take profit order price  
» stop_loss | object | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
»» trigger_price | string | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
»» order_price | string | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
      }
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Order]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Spot order details]  
» _None_ | Order | Spot order details  
»» id | string | Order ID  
»» text | string | User defined information. If not empty, must follow the rules below:  
  
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
»» amend_text | string | The custom data that the user remarked when amending the order  
»» create_time | string | Creation time of order  
»» update_time | string | Last modification time of order  
»» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
»» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
»» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
»» currency_pair | string | Currency pair  
»» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
»» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
»» side | string | Buy or sell order  
»» amount | string | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
»» price | string | Trading price, required when `type`=`limit`  
»» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
»» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
»» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
»» left | string | Amount left to fill  
»» filled_amount | string | Amount filled  
»» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
»» filled_total | string | Total filled in quote currency  
»» avg_deal_price | string | Average fill price  
»» fee | string | Fee deducted  
»» fee_currency | string | Fee currency unit  
»» point_fee | string | Points used to deduct fee  
»» gt_fee | string | GT used to deduct fee  
»» gt_maker_fee | string | GT amount used to deduct maker fee  
»» gt_taker_fee | string | GT amount used to deduct taker fee  
»» gt_discount | boolean | Whether GT fee deduction is enabled  
»» rebated_fee | string | Rebated fee  
»» rebated_fee_currency | string | Rebated fee currency unit  
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
»» finish_as | string | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
»» stop_profit | object | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
»»» trigger_price | string | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
»»» order_price | string | Take profit order price  
»» stop_loss | object | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
»»» trigger_price | string | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
»»» order_price | string | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
        }
      }
    ]
    

##  Create an order🔒 Authenticated

POST`/spot/orders`

POST `/spot/orders`

_Create an order_

Supports spot, margin, leverage, and cross-margin leverage orders. Use different accounts through the `account` field. Default is `spot`, which means using the spot account to place orders. If the user has a `unified` account, the default is to place orders with the unified account.

When using leveraged account trading (i.e., when `account` is set to `margin`), you can set `auto_borrow` to `true`. In case of insufficient account balance, the system will automatically execute `POST /margin/uni/loans` to borrow the insufficient amount. Whether assets obtained after leveraged order execution are automatically used to repay borrowing orders of the isolated margin account depends on the automatic repayment settings of the user's isolated margin account. Account automatic repayment settings can be queried and set through `/margin/auto_repay`.

When using unified account trading (i.e., when `account` is set to `unified`), `auto_borrow` can also be enabled to realize automatic borrowing of insufficient amounts. However, unlike the isolated margin account, whether unified account orders are automatically repaid depends on the `auto_repay` setting when placing the order. This setting only applies to the current order, meaning only assets obtained after order execution will be used to repay borrowing orders of the cross-margin account. Unified account ordering currently supports enabling both `auto_borrow` and `auto_repay` simultaneously.

Auto repayment will be triggered when the order ends, i.e., when `status` is `cancelled` or `closed`.

**Order Status**

The order status in pending orders is `open`, which remains `open` until all quantity is filled. If fully filled, the order ends and status becomes `closed`. If the order is cancelled before all transactions are completed, regardless of partial fills, the status will become `cancelled`.

**Iceberg Orders**

`iceberg` is used to set the displayed quantity of iceberg orders and does not support complete hiding. Note that hidden portions are charged according to the taker's fee rate.

**Self-Trade Prevention**

Set `stp_act` to determine the self-trade prevention strategy to use

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | Order | Required | none  
↳ text | body | string | Optional | User defined information. If not empty, must follow the rules below:  
  
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
↳ currency_pair | body | string | Required | Currency pair  
↳ type | body | string | Optional | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
↳ account | body | string | Optional | Account type, spot - spot account, margin - leveraged account, unified - unified account  
↳ side | body | string | Required | Buy or sell order  
↳ amount | body | string | Required | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
↳ price | body | string | Optional | Trading price, required when `type`=`limit`  
↳ time_in_force | body | string | Optional | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
↳ iceberg | body | string | Optional | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
↳ auto_borrow | body | boolean | Optional | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
↳ auto_repay | body | boolean | Optional | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
↳ stp_act | body | string | Optional | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
↳ action_mode | body | string | Optional | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
↳ slippage | body | string | Optional | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
↳ stop_profit | body | object | Optional | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
↳ trigger_price | body | string | Optional | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
↳ order_price | body | string | Optional | Take profit order price  
↳ stop_loss | body | object | Optional | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
↳ trigger_price | body | string | Optional | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
↳ order_price | body | string | Optional | Stop-loss order price  
  
####  Detailed descriptions

**» text** : User defined information. If not empty, must follow the rules below:  
  
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

**» type** : Order Type   
  
\- limit : Limit Order  
\- market : Market Order

**» amount** : Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`

**» time_in_force** : Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`

**» auto_repay** : Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order

**» stp_act** : Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled

**» action_mode** : Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)

**»» trigger_price** : Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`

**»» trigger_price** : Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» type | limit  
» type | market  
» side | buy  
» side | sell  
» time_in_force | gtc  
» time_in_force | ioc  
» time_in_force | poc  
» time_in_force | fok  
» stp_act | cn  
» stp_act | co  
» stp_act | cb  
» stp_act | -  
  
### Responses

  * 201[Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2)Order created

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Order created | Order  
  
### Response Schema

Status Code **201**

_Spot order details_

Name | Type | Description  
---|---|---  
» id | string | Order ID  
» text | string | User defined information. If not empty, must follow the rules below:  
  
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
» amend_text | string | The custom data that the user remarked when amending the order  
» create_time | string | Creation time of order  
» update_time | string | Last modification time of order  
» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
» currency_pair | string | Currency pair  
» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
» side | string | Buy or sell order  
» amount | string | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
» price | string | Trading price, required when `type`=`limit`  
» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
» auto_borrow | boolean | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
» left | string | Amount left to fill  
» filled_amount | string | Amount filled  
» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
» filled_total | string | Total filled in quote currency  
» avg_deal_price | string | Average fill price  
» fee | string | Fee deducted  
» fee_currency | string | Fee currency unit  
» point_fee | string | Points used to deduct fee  
» gt_fee | string | GT used to deduct fee  
» gt_maker_fee | string | GT amount used to deduct maker fee  
» gt_taker_fee | string | GT amount used to deduct taker fee  
» gt_discount | boolean | Whether GT fee deduction is enabled  
» rebated_fee | string | Rebated fee  
» rebated_fee_currency | string | Rebated fee currency unit  
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
» finish_as | string | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
» action_mode | string | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
» slippage | string | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
» stop_profit | object | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
»» trigger_price | string | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
»» order_price | string | Take profit order price  
» stop_loss | object | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
»» trigger_price | string | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
»» order_price | string | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
    body='{"text":"t-abc123","currency_pair":"BTC_USDT","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}'
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
    body_param='{"text":"t-abc123","currency_pair":"BTC_USDT","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}'
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
      }
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
      }
    }
    

##  Cancel all `open` orders in specified currency pair🔒 Authenticated

DELETE`/spot/orders`

DELETE `/spot/orders`

_Cancel all`open` orders in specified currency pair_

When the `account` parameter is not specified, all pending orders including spot, unified account, and isolated margin will be cancelled. When `currency_pair` is not specified, all trading pair pending orders will be cancelled. You can specify a particular account to cancel all pending orders under that account

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Currency pair  
side | query | string | Optional | Specify all bids or all asks, both included if not specified  
account | query | string | Optional | Specify account type  
  
Classic account: All are included if not specified  
Unified account: Specify `unified`  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Batch cancel request is received and processed. Success is determined based on the order list

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancel request is received and processed. Success is determined based on the order list | [OrderCancel]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Spot order details]  
» _None_ | OrderCancel | Spot order details  
»» id | string | Order ID  
»» text | string | User defined information. If not empty, must follow the rules below:  
  
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
»» amend_text | string | The custom data that the user remarked when amending the order  
»» succeeded | boolean | Request execution result  
»» label | string | Error label, if any, otherwise an empty string  
»» message | string | Detailed error message, if any, otherwise an empty string  
»» create_time | string | Creation time of order  
»» update_time | string | Last modification time of order  
»» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
»» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
»» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
»» currency_pair | string | Currency pair  
»» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
»» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
»» side | string | Buy or sell order  
»» amount | string | Trading quantity  
When `type` is `limit`, it refers to the base currency (the currency being traded), such as `BTC` in `BTC_USDT`  
When `type` is `market`, it refers to different currencies based on the side:  
\- `side`: `buy` refers to quote currency, `BTC_USDT` means `USDT`  
\- `side`: `sell` refers to base currency, `BTC_USDT` means `BTC`  
»» price | string | Trading price, required when `type`=`limit`  
»» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
»» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
»» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
»» left | string | Amount left to fill  
»» filled_amount | string | Amount filled  
»» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
»» filled_total | string | Total filled in quote currency  
»» avg_deal_price | string | Average fill price  
»» fee | string | Fee deducted  
»» fee_currency | string | Fee currency unit  
»» point_fee | string | Points used to deduct fee  
»» gt_fee | string | GT used to deduct fee  
»» gt_maker_fee | string | GT amount used to deduct maker fee  
»» gt_taker_fee | string | GT amount used to deduct taker fee  
»» gt_discount | boolean | Whether GT fee deduction is enabled  
»» rebated_fee | string | Rebated fee  
»» rebated_fee_currency | string | Rebated fee currency unit  
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
»» finish_as | string | How the order was finished.  
  
\- open: processing  
\- filled: filled totally  
\- cancelled: manually cancelled  
\- ioc: time in force is `IOC`, finish immediately  
\- stp: cancelled because self trade prevention  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
finish_as | ioc  
finish_as | stp  
  
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
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Batch cancellation completed

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancellation completed | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CancelOrderResult | object | Order cancellation result  
»» currency_pair | string | Order currency pair  
»» id | string | Order ID  
»» text | string | Custom order information  
»» succeeded | boolean | Whether cancellation succeeded  
»» label | string | Error label when failed to cancel the order; emtpy if succeeded  
»» message | string | Error description when cancellation fails, empty if successful  
»» account | string | Default is empty (deprecated)  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Detail retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Detail retrieved | Order  
  
### Response Schema

Status Code **200**

_Spot order details_

Name | Type | Description  
---|---|---  
» id | string | Order ID  
» text | string | User defined information. If not empty, must follow the rules below:  
  
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
» amend_text | string | The custom data that the user remarked when amending the order  
» create_time | string | Creation time of order  
» update_time | string | Last modification time of order  
» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
» currency_pair | string | Currency pair  
» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
» side | string | Buy or sell order  
» amount | string | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
» price | string | Trading price, required when `type`=`limit`  
» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
» left | string | Amount left to fill  
» filled_amount | string | Amount filled  
» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
» filled_total | string | Total filled in quote currency  
» avg_deal_price | string | Average fill price  
» fee | string | Fee deducted  
» fee_currency | string | Fee currency unit  
» point_fee | string | Points used to deduct fee  
» gt_fee | string | GT used to deduct fee  
» gt_maker_fee | string | GT amount used to deduct maker fee  
» gt_taker_fee | string | GT amount used to deduct taker fee  
» gt_discount | boolean | Whether GT fee deduction is enabled  
» rebated_fee | string | Rebated fee  
» rebated_fee_currency | string | Rebated fee currency unit  
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
» finish_as | string | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
» stop_profit | object | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
»» trigger_price | string | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
»» order_price | string | Take profit order price  
» stop_loss | object | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
»» trigger_price | string | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
»» order_price | string | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
      }
    }
    

##  Amend single order🔒 Authenticated

PATCH`/spot/orders/{order_id}`

PATCH `/spot/orders/{order_id}`

_Amend single order_

Modify orders in spot, unified account and isolated margin account by default.

Currently both request body and query support currency_pair and account parameters, but request body has higher priority.

currency_pair must be filled in one of the request body or query parameters.

About rate limit: Order modification and order creation share the same rate limit rules.

About matching priority: Only reducing the quantity does not affect the matching priority. Modifying the price or increasing the quantity will adjust the priority to the end of the new price level.

Note: Modifying the quantity to be less than the filled quantity will trigger a cancellation and isolated margin account by default.

Currently both request body and query support currency_pair and account parameters, but request body has higher priority.

currency_pair must be filled in one of the request body or query parameters.

About rate limit: Order modification and order creation share the same rate limit rules.

About matching priority: Only reducing the quantity does not affect the matching priority. Modifying the price or increasing the quantity will adjust the priority to the end of the new price level.

Note: Modifying the quantity to be less than the filled quantity will trigger a cancellation operation.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field).  
Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)  
currency_pair | query | string | Optional | Currency pair  
account | query | string | Optional | Specify query account  
x-gate-exptime | header | string | Optional | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected  
body | body | OrderPatch | Required | none  
↳ currency_pair | body | string | Optional | Currency pair  
↳ account | body | string | Optional | Specify query account  
↳ amount | body | string | Optional | Trading quantity. Either `amount` or `price` must be specified  
↳ price | body | string | Optional | Trading price. Either `amount` or `price` must be specified  
↳ amend_text | body | string | Optional | Custom info during order amendment  
↳ action_mode | body | string | Optional | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
↳ stop_profit | body | object | Optional | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
↳ trigger_price | body | string | Optional | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
↳ order_price | body | string | Optional | Take profit order price  
↳ stop_loss | body | object | Optional | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
↳ trigger_price | body | string | Optional | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
↳ order_price | body | string | Optional | Stop-loss order price  
  
####  Detailed descriptions

**order_id** : The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field).  
Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)

**» action_mode** : Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)

**»» trigger_price** : Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`

**»» trigger_price** : Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Updated successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Updated successfully | Order  
  
### Response Schema

Status Code **200**

_Spot order details_

Name | Type | Description  
---|---|---  
» id | string | Order ID  
» text | string | User defined information. If not empty, must follow the rules below:  
  
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
» amend_text | string | The custom data that the user remarked when amending the order  
» create_time | string | Creation time of order  
» update_time | string | Last modification time of order  
» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
» currency_pair | string | Currency pair  
» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
» side | string | Buy or sell order  
» amount | string | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
» price | string | Trading price, required when `type`=`limit`  
» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
» left | string | Amount left to fill  
» filled_amount | string | Amount filled  
» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
» filled_total | string | Total filled in quote currency  
» avg_deal_price | string | Average fill price  
» fee | string | Fee deducted  
» fee_currency | string | Fee currency unit  
» point_fee | string | Points used to deduct fee  
» gt_fee | string | GT used to deduct fee  
» gt_maker_fee | string | GT amount used to deduct maker fee  
» gt_taker_fee | string | GT amount used to deduct taker fee  
» gt_discount | boolean | Whether GT fee deduction is enabled  
» rebated_fee | string | Rebated fee  
» rebated_fee_currency | string | Rebated fee currency unit  
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
» finish_as | string | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
» stop_profit | object | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
»» trigger_price | string | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
»» order_price | string | Take profit order price  
» stop_loss | object | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
»» trigger_price | string | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
»» order_price | string | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
      }
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order cancelled

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order cancelled | Order  
  
### Response Schema

Status Code **200**

_Spot order details_

Name | Type | Description  
---|---|---  
» id | string | Order ID  
» text | string | User defined information. If not empty, must follow the rules below:  
  
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
» amend_text | string | The custom data that the user remarked when amending the order  
» create_time | string | Creation time of order  
» update_time | string | Last modification time of order  
» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
» currency_pair | string | Currency pair  
» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
» side | string | Buy or sell order  
» amount | string | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
» price | string | Trading price, required when `type`=`limit`  
» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
» left | string | Amount left to fill  
» filled_amount | string | Amount filled  
» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
» filled_total | string | Total filled in quote currency  
» avg_deal_price | string | Average fill price  
» fee | string | Fee deducted  
» fee_currency | string | Fee currency unit  
» point_fee | string | Points used to deduct fee  
» gt_fee | string | GT used to deduct fee  
» gt_maker_fee | string | GT amount used to deduct maker fee  
» gt_taker_fee | string | GT amount used to deduct taker fee  
» gt_discount | boolean | Whether GT fee deduction is enabled  
» rebated_fee | string | Rebated fee  
» rebated_fee_currency | string | Rebated fee currency unit  
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
» finish_as | string | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
» stop_profit | object | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
»» trigger_price | string | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
»» order_price | string | Take profit order price  
» stop_loss | object | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
»» trigger_price | string | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
»» order_price | string | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
      }
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [Trade]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | string | Fill ID  
» create_time | string | Fill Time  
» create_time_ms | string | Trading time, with millisecond precision  
» currency_pair | string | Currency pair  
» side | string | Buy or sell order  
» role | string | Trade role, not returned in public endpoints  
» amount | string | Trade amount  
» price | string | Order price  
» order_id | string | Related order ID, not returned in public endpoints  
» fee | string | Fee deducted, not returned in public endpoints  
» fee_currency | string | Fee currency unit, not returned in public endpoints  
» point_fee | string | Points used to deduct fee, not returned in public endpoints  
» gt_fee | string | GT used to deduct fee, not returned in public endpoints  
» amend_text | string | The custom data that the user remarked when amending the order  
» sequence_id | string | Consecutive trade ID within a single market.  
Used to track and identify trades in the specific market  
» text | string | Order's Custom Information. This field is not returned by public interfaces.  
The scenarios pm_liquidate, comb_margin_liquidate, and scm_liquidate represent full-account forced liquidation orders.  
liquidate represents isolated-account forced liquidation orders.  
» deal | string | Total Executed Value  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
side | buy  
side | sell  
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
        "deal": "0.0045"
      }
    ]
    

##  Get server current time

GET`/spot/time`

GET `/spot/time`

Get `server current time`

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | SystemTime  
  
### Response Schema

Status Code **200**

_SystemTime_

Name | Type | Description  
---|---|---  
» server_time | integer(int64) | Server current time(ms)  
  
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

Spot order heartbeat detection. If there is no "cancel existing countdown" or "set new countdown" when the user-set `timeout` time is reached, the related `spot pending orders` will be automatically cancelled. This interface can be called repeatedly to set a new countdown or cancel the countdown. Usage example: Repeat this interface at 30s intervals, setting the countdown `timeout` to `30 (seconds)` each time. If this interface is not called again within 30 seconds, all pending orders on the `market` you specified will be automatically cancelled. If no `market` is specified, all market cancelled. If the `timeout` is set to 0 within 30 seconds, the countdown timer will be terminated and the automatic order cancellation function will be cancelled.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CountdownCancelAllSpotTask | Required | none  
↳ timeout | body | integer(int32) | Required | Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown  
↳ currency_pair | body | string | Optional | Currency pair  
  
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
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order modification executed successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order modification executed successfully | [BatchOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Batch order details]  
» _None_ | BatchOrder | Batch order details  
»» order_id | string | Order ID  
»» amend_text | string | The custom data that the user remarked when amending the order  
»» text | string | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
»» succeeded | boolean | Request execution result  
»» label | string | Error label, if any, otherwise an empty string  
»» message | string | Detailed error message, if any, otherwise an empty string  
»» id | string | Order ID  
»» create_time | string | Creation time of order  
»» update_time | string | Last modification time of order  
»» create_time_ms | integer(int64) | Creation time of order (in milliseconds)  
»» update_time_ms | integer(int64) | Last modification time of order (in milliseconds)  
»» status | string | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
»» currency_pair | string | Currency pair  
»» type | string | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
»» account | string | Account type, spot - spot account, margin - leveraged account, unified - unified account  
»» side | string | Buy or sell order  
»» amount | string | Trade amount  
»» price | string | Order price  
»» time_in_force | string | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
»» iceberg | string | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
»» auto_repay | boolean | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
»» left | string | Amount left to fill  
»» filled_amount | string | Amount filled  
»» fill_price | string | Total filled in quote currency. Deprecated in favor of `filled_total`  
»» filled_total | string | Total filled in quote currency  
»» avg_deal_price | string | Average fill price  
»» fee | string | Fee deducted  
»» fee_currency | string | Fee currency unit  
»» point_fee | string | Points used to deduct fee  
»» gt_fee | string | GT used to deduct fee  
»» gt_discount | boolean | Whether GT fee deduction is enabled  
»» rebated_fee | string | Rebated fee  
»» rebated_fee_currency | string | Rebated fee currency unit  
»» stp_id | integer | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
»» stp_act | string | Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  
  
1\. After users join the `STP Group`, he can pass `stp_act` to limit the user's self-trade prevetion strategy. If `stp_act` is not passed, the default is `cn` strategy。  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter。  
3\. If the user did not use 'stp_act' when placing the order, 'stp_act' will return '-'  
  
\- cn: Cancel newest, Cancel new orders and keep old ones  
\- co: Cancel oldest, new ones  
\- cb: Cancel both, Both old and new orders will be cancelled  
»» finish_as | string | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
»» stop_profit | object | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
»»» trigger_price | string | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
»»» order_price | string | Take profit order price  
»» stop_loss | object | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
»»» trigger_price | string | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
»»» order_price | string | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
account | spot  
account | margin  
account | cross_margin  
account | unified  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [SpotInsuranceHistory]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» currency | string | Currency  
» balance | string | Balance  
» time | integer(int64) | Creation time, timestamp, milliseconds  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SpotPriceTriggeredOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Spot price order details]  
» _None_ | SpotPriceTriggeredOrder | Spot price order details  
»» trigger | SpotPriceTrigger | none  
»»» price | string | Trigger price  
»»» rule | string | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
»»» expiration | integer | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
»» put | SpotPricePutOrder | none  
»»» type | string | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
»»» side | string | Order side  
  
\- buy: buy side  
\- sell: sell side  
»»» price | string | Order price  
»»» amount | string | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
»»» account | string | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
»»» time_in_force | string | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
»»» auto_borrow | boolean | Whether to borrow coins automatically  
»»» auto_repay | boolean | Whether to repay the loan automatically  
»»» text | string | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
»» id | integer(int64) | Auto order ID  
»» user | integer | User ID  
»» market | string | Market  
»» ctime | integer(int64) | Created time  
»» ftime | integer(int64) | End time  
»» fired_order_id | integer(int64) | ID of the order created after trigger  
»» status | string | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
»» reason | string | Additional description of how the order was completed  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
rule | >=  
rule | <=  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
  
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
↳ trigger | body | SpotPriceTrigger | Required | none  
↳ price | body | string | Required | Trigger price  
↳ rule | body | string | Required | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
↳ expiration | body | integer | Optional | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
↳ put | body | SpotPricePutOrder | Required | none  
↳ type | body | string | Optional | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
↳ side | body | string | Required | Order side  
  
\- buy: buy side  
\- sell: sell side  
↳ price | body | string | Required | Order price  
↳ amount | body | string | Required | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
↳ account | body | string | Required | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
↳ time_in_force | body | string | Required | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
↳ auto_borrow | body | boolean | Optional | Whether to borrow coins automatically  
↳ auto_repay | body | boolean | Optional | Whether to repay the loan automatically  
↳ text | body | string | Optional | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
↳ market | body | string | Required | Market  
  
####  Detailed descriptions

**»» rule** : Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`

**»» type** : Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order

**»» side** : Order side  
  
\- buy: buy side  
\- sell: sell side

**»» account** : Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account

**»» time_in_force** : time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only

**»» text** : The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
»» rule | >=  
»» rule | <=  
»» type | limit  
»» type | market  
»» side | buy  
»» side | sell  
»» account | normal  
»» account | margin  
»» account | unified  
»» time_in_force | gtc  
»» time_in_force | ioc  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Batch cancel request is received and processed. Success is determined based on the order list

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch cancel request is received and processed. Success is determined based on the order list | [SpotPriceTriggeredOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Spot price order details]  
» _None_ | SpotPriceTriggeredOrder | Spot price order details  
»» trigger | SpotPriceTrigger | none  
»»» price | string | Trigger price  
»»» rule | string | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
»»» expiration | integer | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
»» put | SpotPricePutOrder | none  
»»» type | string | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
»»» side | string | Order side  
  
\- buy: buy side  
\- sell: sell side  
»»» price | string | Order price  
»»» amount | string | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
»»» account | string | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
»»» time_in_force | string | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
»»» auto_borrow | boolean | Whether to borrow coins automatically  
»»» auto_repay | boolean | Whether to repay the loan automatically  
»»» text | string | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
»» id | integer(int64) | Auto order ID  
»» user | integer | User ID  
»» market | string | Market  
»» ctime | integer(int64) | Created time  
»» ftime | integer(int64) | End time  
»» fired_order_id | integer(int64) | ID of the order created after trigger  
»» status | string | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
»» reason | string | Additional description of how the order was completed  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
rule | >=  
rule | <=  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Auto order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Auto order details | SpotPriceTriggeredOrder  
  
### Response Schema

Status Code **200**

_Spot price order details_

Name | Type | Description  
---|---|---  
» trigger | SpotPriceTrigger | none  
»» price | string | Trigger price  
»» rule | string | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
»» expiration | integer | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
» put | SpotPricePutOrder | none  
»» type | string | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
»» side | string | Order side  
  
\- buy: buy side  
\- sell: sell side  
»» price | string | Order price  
»» amount | string | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
»» account | string | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
»» time_in_force | string | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
»» auto_borrow | boolean | Whether to borrow coins automatically  
»» auto_repay | boolean | Whether to repay the loan automatically  
»» text | string | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
» id | integer(int64) | Auto order ID  
» user | integer | User ID  
» market | string | Market  
» ctime | integer(int64) | Created time  
» ftime | integer(int64) | End time  
» fired_order_id | integer(int64) | ID of the order created after trigger  
» status | string | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
» reason | string | Additional description of how the order was completed  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
rule | >=  
rule | <=  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Auto order details

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Auto order details | SpotPriceTriggeredOrder  
  
### Response Schema

Status Code **200**

_Spot price order details_

Name | Type | Description  
---|---|---  
» trigger | SpotPriceTrigger | none  
»» price | string | Trigger price  
»» rule | string | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
»» expiration | integer | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
» put | SpotPricePutOrder | none  
»» type | string | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
»» side | string | Order side  
  
\- buy: buy side  
\- sell: sell side  
»» price | string | Order price  
»» amount | string | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
»» account | string | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
»» time_in_force | string | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
»» auto_borrow | boolean | Whether to borrow coins automatically  
»» auto_repay | boolean | Whether to repay the loan automatically  
»» text | string | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
» id | integer(int64) | Auto order ID  
» user | integer | User ID  
» market | string | Market  
» ctime | integer(int64) | Created time  
» ftime | integer(int64) | End time  
» fired_order_id | integer(int64) | ID of the order created after trigger  
» status | string | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
» reason | string | Additional description of how the order was completed  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
rule | >=  
rule | <=  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
  
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
    
    

##  SpotPriceTriggeredOrder

_Spot price order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
trigger | SpotPriceTrigger | Required | none | none  
put | SpotPricePutOrder | Required | none | none  
id | integer(int64) | Optional | read-only | Auto order ID  
user | integer | Optional | read-only | User ID  
market | string | Required | none | Market  
ctime | integer(int64) | Optional | read-only | Created time  
ftime | integer(int64) | Optional | read-only | End time  
fired_order_id | integer(int64) | Optional | read-only | ID of the order created after trigger  
status | string | Optional | read-only | Status  
  
\- open: Running  
\- cancelled: Manually cancelled  
\- finish: Successfully completed  
\- failed: Failed to execute  
\- expired: Expired  
reason | string | Optional | read-only | Additional description of how the order was completed  
      
    
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
    
    

##  OrderBook

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Order book ID, which is updated whenever the order book is changed. Valid only when `with_id` is set to `true`  
current | integer(int64) | Optional | none | The timestamp of the response data being generated (in milliseconds)  
update | integer(int64) | Optional | none | The timestamp of when the orderbook last changed (in milliseconds)  
asks | array | Required | none | Ask Depth  
↳ None | array | Optional | none | Price and Quantity Pair  
bids | array | Required | none | Bid Depth  
↳ None | array | Optional | none | Price and Quantity Pair  
      
    
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
    
    

##  CountdownCancelAllSpotTask

_CountdownCancelAllSpotTask_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timeout | integer(int32) | Required | none | Countdown time in seconds  
At least 5 seconds, 0 means cancel countdown  
currency_pair | string | Optional | none | Currency pair  
      
    
    {
      "timeout": 0,
      "currency_pair": "string"
    }
    
    

##  SpotAccount

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency detail  
available | string | Optional | none | Available amount  
locked | string | Optional | none | Locked amount, used in trading  
update_id | integer(int64) | Optional | none | Version number  
      
    
    {
      "currency": "string",
      "available": "string",
      "locked": "string",
      "update_id": 0
    }
    
    

##  CurrencyPair

_Spot currency pair_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | none | Currency pair  
base | string | Optional | none | Base currency  
base_name | string | Optional | none | Base currency name  
quote | string | Optional | none | Quote currency  
quote_name | string | Optional | none | Quote currency name  
fee | string | Optional | none | Trading fee rate(deprecated)  
min_base_amount | string | Optional | none | Minimum amount of base currency to trade, `null` means no limit  
min_quote_amount | string | Optional | none | Minimum amount of quote currency to trade, `null` means no limit  
max_base_amount | string | Optional | none | Maximum amount of base currency to trade, `null` means no limit  
max_quote_amount | string | Optional | none | Maximum amount of quote currency to trade, `null` means no limit  
amount_precision | integer | Optional | none | Amount scale  
precision | integer | Optional | none | Price scale  
trade_status | string | Optional | none | Trading status  
  
\- untradable: cannot be traded  
\- buyable: can be bought  
\- sellable: can be sold  
\- tradable: can be bought and sold  
sell_start | integer(int64) | Optional | none | Sell start unix timestamp in seconds  
buy_start | integer(int64) | Optional | none | Buy start unix timestamp in seconds  
delisting_time | integer(int64) | Optional | none | Expected time to remove the shelves, Unix timestamp in seconds  
type | string | Optional | none | Trading pair type, normal: normal, premarket: pre-market  
trade_url | string | Optional | none | Transaction link  
st_tag | boolean | Optional | none | Whether the trading pair is in ST risk assessment, false - No, true - Yes  
up_rate | string | Optional | none | Maximum Quote Rise Percentage  
down_rate | string | Optional | none | Maximum Quote Decline Percentage  
slippage | string | Optional | none | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
market_order_max_stock | string | Optional | none | Maximum Market Order Quantity  
market_order_max_money | string | Optional | none | Maximum Market Order Amount  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
trade_status | untradable  
trade_status | buyable  
trade_status | sellable  
trade_status | tradable  
      
    
    {
      "id": "string",
      "base": "string",
      "base_name": "string",
      "quote": "string",
      "quote_name": "string",
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
    
    

##  LiquidateOrder

_Spot liquidation order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
text | string | Optional | none | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
currency_pair | string | Required | none | Currency pair  
amount | string | Required | none | Trade amount  
price | string | Required | none | Order price  
action_mode | string | Optional | none | Processing mode:  
  
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
    
    

##  SpotFee

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional | none | User ID  
taker_fee | string | Optional | none | taker fee rate  
maker_fee | string | Optional | none | maker fee rate  
rpi_maker_fee | string | Optional | none | RPI MM maker fee rate  
gt_discount | boolean | Optional | none | Whether GT deduction discount is enabled  
gt_taker_fee | string | Optional | none | Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  
gt_maker_fee | string | Optional | none | Maker fee rate with GT deduction. Returns 0 if GT deduction is disabled  
loan_fee | string | Optional | none | Loan fee rate of margin lending  
point_type | string | Optional | none | Point card type: 0 - Original version, 1 - New version since 202009  
currency_pair | string | Optional | none | Currency pair  
debit_fee | integer | Optional | none | Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  
rpi_mm | integer | Optional | none | RPI MM Level  
      
    
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

_Spot order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency_pair | string | Optional | none | Currency pair  
account | string | Optional | none | Specify query account  
amount | string | Optional | none | Trading quantity. Either `amount` or `price` must be specified  
price | string | Optional | none | Trading price. Either `amount` or `price` must be specified  
amend_text | string | Optional | none | Custom info during order amendment  
action_mode | string | Optional | none | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
stop_profit | object | Optional | none | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
↳ trigger_price | string | Optional | none | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
↳ order_price | string | Optional | none | Take profit order price  
stop_loss | object | Optional | none | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
↳ trigger_price | string | Optional | none | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
↳ order_price | string | Optional | none | Stop-loss order price  
      
    
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
    
    

##  BatchAmendItem

_Order information that needs to be modified_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Required | none | The order ID returned upon successful creation or the custom ID specified by the user during creation (i.e., the 'text' field)  
currency_pair | string | Required | none | Currency pair  
account | string | Optional | none | Default spot, unified account and warehouse-by-store leverage account  
amount | string | Optional | none | Trading Quantity. Only one of `amount` or `price` can be specified  
price | string | Optional | none | Trading Price. Only one of `amount` or `price` can be specified  
amend_text | string | Optional | none | Custom info during order amendment  
action_mode | string | Optional | none | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
stop_profit | object | Optional | none | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
↳ trigger_price | string | Optional | none | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
↳ order_price | string | Optional | none | Take profit order price  
stop_loss | object | Optional | none | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
↳ trigger_price | string | Optional | none | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
↳ order_price | string | Optional | none | Stop-loss order price  
      
    
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
    
    

##  Order

_Spot order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | read-only | Order ID  
text | string | Optional | none | User defined information. If not empty, must follow the rules below:  
  
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
amend_text | string | Optional | read-only | The custom data that the user remarked when amending the order  
create_time | string | Optional | read-only | Creation time of order  
update_time | string | Optional | read-only | Last modification time of order  
create_time_ms | integer(int64) | Optional | read-only | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | read-only | Last modification time of order (in milliseconds)  
status | string | Optional | read-only | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
currency_pair | string | Required | none | Currency pair  
type | string | Optional | none | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | none | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | none | Buy or sell order  
amount | string | Required | none | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
price | string | Optional | none | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | none | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
iceberg | string | Optional | none | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
auto_borrow | boolean | Optional | write-only | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional | none | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | read-only | Amount left to fill  
filled_amount | string | Optional | read-only | Amount filled  
fill_price | string | Optional | read-only | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | read-only | Total filled in quote currency  
avg_deal_price | string | Optional | read-only | Average fill price  
fee | string | Optional | read-only | Fee deducted  
fee_currency | string | Optional | read-only | Fee currency unit  
point_fee | string | Optional | read-only | Points used to deduct fee  
gt_fee | string | Optional | read-only | GT used to deduct fee  
gt_maker_fee | string | Optional | read-only | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | read-only | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | read-only | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | read-only | Rebated fee  
rebated_fee_currency | string | Optional | read-only | Rebated fee currency unit  
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
finish_as | string | Optional | read-only | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
action_mode | string | Optional | write-only | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
slippage | string | Optional | write-only | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object | Optional | none | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
↳ trigger_price | string | Optional | none | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
↳ order_price | string | Optional | none | Take profit order price  
stop_loss | object | Optional | none | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
↳ trigger_price | string | Optional | none | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
↳ order_price | string | Optional | none | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
      }
    }
    
    

##  Ticker

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency_pair | string | Optional | none | Currency pair  
last | string | Optional | none | Last trading price  
lowest_ask | string | Optional | none | Recent lowest ask  
lowest_size | string | Optional | none | Latest seller's lowest price quantity; not available for batch queries; available for single queries, empty if no data  
highest_bid | string | Optional | none | Recent highest bid  
highest_size | string | Optional | none | Latest buyer's highest price quantity; not available for batch queries; available for single queries, empty if no data  
change_percentage | string | Optional | none | 24h price change percentage (negative for decrease, e.g., -7.45)  
change_utc0 | string | Optional | none | UTC+0 timezone, 24h price change percentage, negative for decline (e.g., -7.45)  
change_utc8 | string | Optional | none | UTC+8 timezone, 24h price change percentage, negative for decline (e.g., -7.45)  
base_volume | string | Optional | none | Base currency trading volume in the last 24h  
quote_volume | string | Optional | none | Quote currency trading volume in the last 24h  
high_24h | string | Optional | none | 24h High  
low_24h | string | Optional | none | 24h Low  
etf_net_value | string | Optional | none | ETF net value  
etf_pre_net_value | string|null | Optional | none | ETF net value at previous rebalancing point  
etf_pre_timestamp | integer(int64)|null | Optional | none | ETF previous rebalancing time  
etf_leverage | string|null | Optional | none | ETF current leverage  
      
    
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

_Spot order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | read-only | Order ID  
text | string | Optional | none | User defined information. If not empty, must follow the rules below:  
  
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
amend_text | string | Optional | read-only | The custom data that the user remarked when amending the order  
succeeded | boolean | Optional | none | Request execution result  
label | string | Optional | none | Error label, if any, otherwise an empty string  
message | string | Optional | none | Detailed error message, if any, otherwise an empty string  
create_time | string | Optional | read-only | Creation time of order  
update_time | string | Optional | read-only | Last modification time of order  
create_time_ms | integer(int64) | Optional | read-only | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | read-only | Last modification time of order (in milliseconds)  
status | string | Optional | read-only | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
currency_pair | string | Required | none | Currency pair  
type | string | Optional | none | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | none | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Required | none | Buy or sell order  
amount | string | Required | none | Trading quantity  
When `type` is `limit`, it refers to the base currency (the currency being traded), such as `BTC` in `BTC_USDT`  
When `type` is `market`, it refers to different currencies based on the side:  
\- `side`: `buy` refers to quote currency, `BTC_USDT` means `USDT`  
\- `side`: `sell` refers to base currency, `BTC_USDT` means `BTC`  
price | string | Optional | none | Trading price, required when `type`=`limit`  
time_in_force | string | Optional | none | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
iceberg | string | Optional | none | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
auto_borrow | boolean | Optional | write-only | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional | none | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | read-only | Amount left to fill  
filled_amount | string | Optional | read-only | Amount filled  
fill_price | string | Optional | read-only | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | read-only | Total filled in quote currency  
avg_deal_price | string | Optional | read-only | Average fill price  
fee | string | Optional | read-only | Fee deducted  
fee_currency | string | Optional | read-only | Fee currency unit  
point_fee | string | Optional | read-only | Points used to deduct fee  
gt_fee | string | Optional | read-only | GT used to deduct fee  
gt_maker_fee | string | Optional | read-only | GT amount used to deduct maker fee  
gt_taker_fee | string | Optional | read-only | GT amount used to deduct taker fee  
gt_discount | boolean | Optional | read-only | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | read-only | Rebated fee  
rebated_fee_currency | string | Optional | read-only | Rebated fee currency unit  
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
finish_as | string | Optional | read-only | How the order was finished.  
  
\- open: processing  
\- filled: filled totally  
\- cancelled: manually cancelled  
\- ioc: time in force is `IOC`, finish immediately  
\- stp: cancelled because self trade prevention  
action_mode | string | Optional | write-only | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
finish_as | ioc  
finish_as | stp  
      
    
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
    
    

##  SystemTime

_SystemTime_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
server_time | integer(int64) | Optional | none | Server current time(ms)  
      
    
    {
      "server_time": 0
    }
    
    

##  CancelBatchOrder

_Info of order to be cancelled_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency_pair | string | Required | none | Order currency pair  
id | string | Required | none | Order ID or user custom ID.  
Custom ID are accepted only within 30 minutes after order creation  
account | string | Optional | none | If the canceled order is a unified account apikey, this field must be specified and set to `unified`  
action_mode | string | Optional | none | Processing Mode:  
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
    
    

##  SpotPriceTrigger

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
price | string | Required | none | Trigger price  
rule | string | Required | none | Price trigger condition  
  
\- `>=`: triggered when market price is greater than or equal to `price`  
\- `<=`: triggered when market price is less than or equal to `price`  
expiration | integer | Optional | none | Maximum wait time for trigger condition (in seconds). Order will be cancelled if timeout  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
rule | >=  
rule | <=  
      
    
    {
      "price": "string",
      "rule": ">=",
      "expiration": 0
    }
    
    

##  Trade

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | none | Fill ID  
create_time | string | Optional | none | Fill Time  
create_time_ms | string | Optional | none | Trading time, with millisecond precision  
currency_pair | string | Optional | none | Currency pair  
side | string | Optional | none | Buy or sell order  
role | string | Optional | none | Trade role, not returned in public endpoints  
amount | string | Optional | none | Trade amount  
price | string | Optional | none | Order price  
order_id | string | Optional | none | Related order ID, not returned in public endpoints  
fee | string | Optional | none | Fee deducted, not returned in public endpoints  
fee_currency | string | Optional | none | Fee currency unit, not returned in public endpoints  
point_fee | string | Optional | none | Points used to deduct fee, not returned in public endpoints  
gt_fee | string | Optional | none | GT used to deduct fee, not returned in public endpoints  
amend_text | string | Optional | none | The custom data that the user remarked when amending the order  
sequence_id | string | Optional | none | Consecutive trade ID within a single market.  
Used to track and identify trades in the specific market  
text | string | Optional | none | Order's Custom Information. This field is not returned by public interfaces.  
The scenarios pm_liquidate, comb_margin_liquidate, and scm_liquidate represent full-account forced liquidation orders.  
liquidate represents isolated-account forced liquidation orders.  
deal | string | Optional | none | Total Executed Value  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
side | buy  
side | sell  
role | taker  
role | maker  
      
    
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
      "deal": "string"
    }
    
    

##  SpotInsuranceHistory

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency  
balance | string | Optional | none | Balance  
time | integer(int64) | Optional | none | Creation time, timestamp, milliseconds  
      
    
    {
      "currency": "string",
      "balance": "string",
      "time": 0
    }
    
    

##  OpenOrders

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency_pair | string | Optional | none | Currency pair  
total | integer | Optional | none | Total number of open orders for this trading pair on the current page  
orders | array | Optional | none | none  
↳ None | object | Optional | none | Spot order details  
↳ id | string | Optional | read-only | Order ID  
↳ text | string | Optional | none | User defined information. If not empty, must follow the rules below:  
  
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
↳ amend_text | string | Optional | read-only | The custom data that the user remarked when amending the order  
↳ create_time | string | Optional | read-only | Creation time of order  
↳ update_time | string | Optional | read-only | Last modification time of order  
↳ create_time_ms | integer(int64) | Optional | read-only | Creation time of order (in milliseconds)  
↳ update_time_ms | integer(int64) | Optional | read-only | Last modification time of order (in milliseconds)  
↳ status | string | Optional | read-only | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
↳ currency_pair | string | Required | none | Currency pair  
↳ type | string | Optional | none | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
↳ account | string | Optional | none | Account type, spot - spot account, margin - leveraged account, unified - unified account  
↳ side | string | Required | none | Buy or sell order  
↳ amount | string | Required | none | Trade amount  
When `type` is `limit`, this is the base currency to trade (the currency being bought or sold), e.g. `BTC` in `BTC_USDT`.  
When `type` is `market`, the meaning depends on the side:  
\- `side`: `buy` refers to the quote currency, e.g. `USDT` in `BTC_USDT`  
\- `side`: `sell` refers to the base currency, e.g. `BTC` in `BTC_USDT`  
↳ price | string | Optional | none | Trading price, required when `type`=`limit`  
↳ time_in_force | string | Optional | none | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
Only `ioc` and `fok` are supported when `type`=`market`  
↳ iceberg | string | Optional | none | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
↳ auto_borrow | boolean | Optional | write-only | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
↳ auto_repay | boolean | Optional | none | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
↳ left | string | Optional | read-only | Amount left to fill  
↳ filled_amount | string | Optional | read-only | Amount filled  
↳ fill_price | string | Optional | read-only | Total filled in quote currency. Deprecated in favor of `filled_total`  
↳ filled_total | string | Optional | read-only | Total filled in quote currency  
↳ avg_deal_price | string | Optional | read-only | Average fill price  
↳ fee | string | Optional | read-only | Fee deducted  
↳ fee_currency | string | Optional | read-only | Fee currency unit  
↳ point_fee | string | Optional | read-only | Points used to deduct fee  
↳ gt_fee | string | Optional | read-only | GT used to deduct fee  
↳ gt_maker_fee | string | Optional | read-only | GT amount used to deduct maker fee  
↳ gt_taker_fee | string | Optional | read-only | GT amount used to deduct taker fee  
↳ gt_discount | boolean | Optional | read-only | Whether GT fee deduction is enabled  
↳ rebated_fee | string | Optional | read-only | Rebated fee  
↳ rebated_fee_currency | string | Optional | read-only | Rebated fee currency unit  
↳ stp_id | integer | Optional | read-only | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
↳ stp_act | string | Optional | none | Self-Trading Prevention Action. Users can use this field to set self-trade prevention strategies  
  
1\. After users join the `STP Group`, they can pass `stp_act` to limit the user's self-trade prevention strategy. If `stp_act` is not passed, the default is `cn` strategy.  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter.  
3\. If the user did not use `stp_act` when placing the order, `stp_act` will return '-'  
  
\- cn: Cancel newest, cancel new orders and keep old ones  
\- co: Cancel oldest, cancel old orders and keep new ones  
\- cb: Cancel both, both old and new orders will be cancelled  
↳ finish_as | string | Optional | read-only | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
↳ action_mode | string | Optional | write-only | Processing Mode:  
When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result  
ACK: Asynchronous mode, only returns key order fields  
RESULT: No clearing information  
FULL: Full mode (default)  
↳ slippage | string | Optional | write-only | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
↳ stop_profit | object | Optional | none | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
↳ trigger_price | string | Optional | none | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
↳ order_price | string | Optional | none | Take profit order price  
↳ stop_loss | object | Optional | none | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
↳ trigger_price | string | Optional | none | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
↳ order_price | string | Optional | none | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
          "stop_loss": {}
        }
      ]
    }
    
    

##  Currency

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency symbol  
name | string | Optional | none | Currency name  
delisted | boolean | Optional | none | Whether currency is de-listed  
withdraw_disabled | boolean | Optional | none | Whether currency's withdrawal is disabled (deprecated)  
withdraw_delayed | boolean | Optional | none | Whether currency's withdrawal is delayed (deprecated)  
deposit_disabled | boolean | Optional | none | Whether currency's deposit is disabled (deprecated)  
trade_disabled | boolean | Optional | none | Whether currency's trading is disabled  
fixed_rate | string | Optional | none | Fixed fee rate. Only for fixed rate currencies, not valid for normal currencies  
chain | string | Optional | none | The main chain corresponding to the coin  
chains | array | Optional | none | All links corresponding to coins  
↳ SpotCurrencyChain | object | Optional | none | none  
↳ name | string | Optional | none | Blockchain name  
↳ addr | string | Optional | none | token address  
↳ withdraw_disabled | boolean | Optional | none | Whether currency's withdrawal is disabled  
↳ withdraw_delayed | boolean | Optional | none | Whether currency's withdrawal is delayed  
↳ deposit_disabled | boolean | Optional | none | Whether currency's deposit is disabled  
↳ total_supply | string | Optional | none | Total supply  
↳ market_cap | string | Optional | none | Market cap  
↳ category | array | Optional | none | Currency categories  
\- stocks: Stocks  
\- metals: Metals  
\- indices: Indices  
\- forex: Forex  
\- commodities: Commodities  
      
    
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
    
    

##  BatchOrder

_Batch order details_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Optional | none | Order ID  
amend_text | string | Optional | none | The custom data that the user remarked when amending the order  
text | string | Optional | none | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
succeeded | boolean | Optional | none | Request execution result  
label | string | Optional | none | Error label, if any, otherwise an empty string  
message | string | Optional | none | Detailed error message, if any, otherwise an empty string  
id | string | Optional | read-only | Order ID  
create_time | string | Optional | read-only | Creation time of order  
update_time | string | Optional | read-only | Last modification time of order  
create_time_ms | integer(int64) | Optional | read-only | Creation time of order (in milliseconds)  
update_time_ms | integer(int64) | Optional | read-only | Last modification time of order (in milliseconds)  
status | string | Optional | read-only | Order status  
  
\- `open`: to be filled  
\- `closed`: closed order  
\- `cancelled`: cancelled  
currency_pair | string | Optional | none | Currency pair  
type | string | Optional | none | Order Type   
  
\- limit : Limit Order  
\- market : Market Order  
account | string | Optional | none | Account type, spot - spot account, margin - leveraged account, unified - unified account  
side | string | Optional | none | Buy or sell order  
amount | string | Optional | none | Trade amount  
price | string | Optional | none | Order price  
time_in_force | string | Optional | none | Time in force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
\- poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee  
\- fok: FillOrKill, fill either completely or none  
iceberg | string | Optional | none | Amount to display for the iceberg order. Null or 0 for normal orders. Hiding all amount is not supported  
auto_borrow | boolean | Optional | write-only | Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough  
auto_repay | boolean | Optional | none | Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  
  
1\. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders.  
2\. `auto_borrow` and `auto_repay` can be both set to true in one order  
left | string | Optional | read-only | Amount left to fill  
filled_amount | string | Optional | read-only | Amount filled  
fill_price | string | Optional | read-only | Total filled in quote currency. Deprecated in favor of `filled_total`  
filled_total | string | Optional | read-only | Total filled in quote currency  
avg_deal_price | string | Optional | read-only | Average fill price  
fee | string | Optional | read-only | Fee deducted  
fee_currency | string | Optional | read-only | Fee currency unit  
point_fee | string | Optional | read-only | Points used to deduct fee  
gt_fee | string | Optional | read-only | GT used to deduct fee  
gt_discount | boolean | Optional | read-only | Whether GT fee deduction is enabled  
rebated_fee | string | Optional | read-only | Rebated fee  
rebated_fee_currency | string | Optional | read-only | Rebated fee currency unit  
stp_id | integer | Optional | read-only | Orders between users in the same `stp_id` group are not allowed to be self-traded  
  
1\. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker.  
2\. `stp_id` returns `0` by default for orders that have not been set for `STP group`  
stp_act | string | Optional | none | Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  
  
1\. After users join the `STP Group`, he can pass `stp_act` to limit the user's self-trade prevetion strategy. If `stp_act` is not passed, the default is `cn` strategy。  
2\. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter。  
3\. If the user did not use 'stp_act' when placing the order, 'stp_act' will return '-'  
  
\- cn: Cancel newest, Cancel new orders and keep old ones  
\- co: Cancel oldest, new ones  
\- cb: Cancel both, Both old and new orders will be cancelled  
finish_as | string | Optional | read-only | How the order finished:  
  
\- open: Pending processing  
\- filled: Fully filled  
\- cancelled: Cancelled by user  
\- liquidate_cancelled: Cancelled by liquidation  
\- small: Order size too small  
\- depth_not_enough: Cancelled due to insufficient order book depth  
\- trader_not_enough: Cancelled due to insufficient counterparty liquidity  
\- ioc: Not filled immediately because time-in-force is IOC  
\- poc: Post-only / maker requirement not met (e.g. related TIF such as poc/rvt/rat/rpi would take liquidity as taker)  
\- fok: Not fully filled immediately because time-in-force is FOK  
\- stp: Cancelled due to self-trade prevention  
\- price_protect_cancelled: Cancelled due to price protection  
\- unknown: Unknown  
slippage | string | Optional | write-only | Maximum supported slippage ratio for Spot Market Order Placement, calculated based on the latest market price at the time of order placement as the benchmark (Example: 0.03 means 3%)  
stop_profit | object | Optional | none | Take profit for limit orders. Pass {} to cancel take profit; pass null to leave take profit unchanged.  
↳ trigger_price | string | Optional | none | Take profit trigger price  
When `side == "buy"`, `trigger_price` must be greater than `price`  
When `side == "sell"`, `trigger_price` must be less than `price`  
↳ order_price | string | Optional | none | Take profit order price  
stop_loss | object | Optional | none | Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.  
↳ trigger_price | string | Optional | none | Stop loss trigger price  
When `side == "buy"`, `trigger_price` must be less than `price`  
When `side == "sell"`, `trigger_price` must be greater than `price`  
↳ order_price | string | Optional | none | Stop-loss order price  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
account | spot  
account | margin  
account | cross_margin  
account | unified  
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
    
    

##  SpotAccountBook

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | none | Balance change record ID  
time | integer(int64) | Optional | none | The timestamp of the change (in milliseconds)  
currency | string | Optional | none | Currency changed  
change | string | Optional | none | Amount changed. Positive value means transferring in, while negative out  
balance | string | Optional | none | Balance after change  
type | string | Optional | none | Account change type; deprecated (see `code` for account change type encoding)  
code | string | Optional | none | Account change code, see [Asset Record Code] (Asset Record Code)  
text | string | Optional | none | Additional information  
      
    
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
    
    

##  SpotPricePutOrder

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
type | string | Optional | none | Order type，default to `limit`  
  
\- limit : Limit Order  
\- market : Market Order  
side | string | Required | none | Order side  
  
\- buy: buy side  
\- sell: sell side  
price | string | Required | none | Order price  
amount | string | Required | none | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT.  
account | string | Required | none | Trading account type. Unified account must be set to `unified`  
  
\- normal: spot trading  
\- margin: margin trading  
\- unified: unified account  
time_in_force | string | Required | none | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled, taker only  
auto_borrow | boolean | Optional | none | Whether to borrow coins automatically  
auto_repay | boolean | Optional | none | Whether to repay the loan automatically  
text | string | Optional | none | The source of the order, including:  
\- web: Web  
\- api: API call  
\- app: Mobile app  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
      
    
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