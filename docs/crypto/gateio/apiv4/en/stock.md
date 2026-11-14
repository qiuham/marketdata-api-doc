---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/stock
api_type: REST
updated_at: 2026-11-13 20:57:23.936279
---

# Stock

The Stock API provides traditional financial stock spot trading. Responses are compatible with APIv4: successful responses contain `data` and `timestamp`; error responses contain `label`, `message`, `data`, and `timestamp`.

  * REST API production BaseURL: `https://api.gateio.ws/api/v4/`
  * Documentation route prefix: `/stock`
  * For lead trading via APIv4, add the request header `x-gate-trader-copy-type: stock_copy` (fund transfers and transaction history endpoints are excluded from lead trading).

##  Query user assets🔒 Authenticated

GET`/stock/users/assets`

GET `/stock/users/assets`

_Query user assets_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
pnl_calc_type | query | integer | Optional | PnL calculation cost type. Defaults to average cost price when omitted (1 = average cost price, 2 = diluted cost price)  
pnl_calc_price | query | integer | Optional | PnL calculation price type. Defaults to intraday price when omitted (1 = intraday price, 2 = latest extended-hours price)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
pnl_calc_type | 1  
pnl_calc_type | 2  
pnl_calc_price | 1  
pnl_calc_price | 2  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotUserAssetResp  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» equity | string | Account equity  
»» balance | string | Account Balance  
»» available | string | Available Balance  
»» loan_amount | string | Loan amount. Non-negative: the absolute value of the original available balance when it is negative, otherwise 0.  
»» buy_power | string | Buying power  
»» leverage | string | Leverage  
»» leave_liquidity | string | Excess liquidity  
»» leave_liquidity_rate | string | Excess liquidity ratio  
»» aee | string | Available Excess Equity (AEE)  
»» options_margin | string | Options margin  
»» position_market_value | string | Position market value  
»» position_pnl | string | Position P&L  
»» today_pnl | string | Today's P&L  
»» option_position_market_value | string | Option position market value  
»» option_position_pnl | string | Option position PnL  
»» option_today_pnl | string | Option today's PnL  
»» user_exists | boolean | Whether the user has activated the service  
»» margin_enabled | boolean | Whether margin financing is enabled  
»» long_borrowing_rate | string | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/users/assets'
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
    url="/stock/users/assets"
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
        "equity": "10000.12",
        "balance": "8000",
        "available": "6500.5",
        "loan_amount": "0",
        "buy_power": "13000",
        "leverage": "2",
        "leave_liquidity": "5000",
        "leave_liquidity_rate": "0.5",
        "aee": "4800",
        "options_margin": "0",
        "position_market_value": "1500.25",
        "position_pnl": "12.5",
        "today_pnl": "3.2",
        "option_position_market_value": "0",
        "option_position_pnl": "0",
        "option_today_pnl": "0",
        "user_exists": true,
        "margin_enabled": true,
        "long_borrowing_rate": "0.03"
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Set margin financing availability🔒 Authenticated

PUT`/stock/users/margin-feature`

PUT `/stock/users/margin-feature`

_Set margin financing availability_

Rate limit: 5 requests per second. Enable or disable margin financing for the user.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiSpotSetMarginFeatureRequest | Required | none  
» margin_feature | body | boolean | Required | Whether to enable margin financing. true enables it; false disables it.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | SetMarginFeature  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | Returns empty object on success  
» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/users/margin-feature'
    query_param = ''
    body='{"margin_feature":true}'
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
    url="/stock/users/margin-feature"
    query_param=""
    body_param='{"margin_feature":true}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "margin_feature": true
    }
    

> Example responses

> 200 Response
    
    
    {
      "data": {},
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query symbol list

GET`/stock/symbols`

GET `/stock/symbols`

_Query symbol list_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Optional | Symbol list, multiple separated by commas  
exchange | query | string | Optional | Trading market code.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: South Korean stocks.  
\- jp: Japanese stocks.  
with_desc_i18n | query | boolean | Optional | Whether to return multilingual symbol description  
page | query | integer | Optional | Page number, defaults to 1  
page_size | query | integer | Optional | Page size, defaults to 10, max 500; server caps at 500  
  
####  Detailed descriptions

**exchange** : Trading market code.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: South Korean stocks.  
\- jp: Japanese stocks.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotSymbols  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» total | integer(int64) | Total quantity  
»» total_page | integer | Total pages  
»» list | array | Symbol list  
»»» symbol | string | Symbol  
»»» exchange | string | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»»» exchange_desc | string | Exchange description  
»»» quote_currency | string | Quote currency  
»»» quote_currency_precision | integer | Quote currency precision  
»»» fx_rate | string | Quote currency to USD exchange rate  
»»» symbol_desc | string | Symbol description  
»»» category | string | Symbol category.  
\- CS: Common stock.  
\- ETF: Exchange-traded funds.  
\- ADRC, ADR: Depositary receipts for foreign companies listed in the U.S.  
\- ETV: Exchange-traded products.  
\- PFD: Preferred stock.  
\- ETS: Exchange-traded securities.  
\- ETN: Exchange-traded notes.  
\- FUND: Funds.  
»»» asset_type | string | Asset type.  
\- STOCK: Stock.  
\- ETF: Exchange-traded fund.  
»»» trade_status | string | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
»»» trade_mode | integer | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
\- 6: Trading suspended.  
\- 7: Trading suspended.  
\- 8: Trading suspended.  
»»» order_fill_timing | integer | Order fill timing (1=immediate, 2=after pre-market opens, 3=after regular session opens)  
»»» icon_link | string | Icon URL  
»»» quote_currency_symbol | string | Quote currency symbol  
»»» price_precision | integer | Price precision  
»»» volume_precision | integer | Quantity precision  
»»» is_ipo | boolean | Whether it is an IPO symbol  
»»» ipo_price | string | IPO price  
»»» sell_price_protection | string | Sell price protection rate  
»»» buy_price_protection | string | Buy price protection rate  
»»» symbol_descs | array | Multilingual symbol description  
»»»» lang | string | Language  
»»»» value | string | Localized description  
»»» margin_mode | integer | Margin trading mode.  
\- 0: Neither margin financing nor securities borrowing is supported.  
\- 1: Margin financing is supported.  
\- 2: Securities borrowing is supported.  
\- 3: Both margin financing and securities borrowing are supported.  
»»» long_im | string | Initial margin ratio for long positions  
»»» long_mm | string | Maintenance margin ratio for long positions  
»»» short_im | string | Initial margin ratio for short positions  
»»» short_mm | string | Maintenance margin ratio for short positions  
»»» long_borrowing_rate | string | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
»»» short_borrowing_rate | string | Annual securities borrowing interest rate. An empty string indicates that no valid rate is currently available.  
»» timestamp | integer(int64) | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
category | CS  
category | ETF  
category | ADRC  
category | ADR  
category | ETV  
category | PFD  
category | ETS  
category | ETN  
category | FUND  
asset_type | STOCK  
asset_type | ETF  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
order_fill_timing | 1  
order_fill_timing | 2  
order_fill_timing | 3  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/symbols'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/symbols \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "symbol": "AAPL",
            "exchange": "us",
            "exchange_desc": "United States",
            "quote_currency": "USD",
            "quote_currency_precision": 2,
            "fx_rate": "1",
            "symbol_desc": "Apple Inc.",
            "category": "CS",
            "asset_type": "STOCK",
            "trade_status": "open",
            "trade_mode": 4,
            "order_fill_timing": 1,
            "icon_link": "https://static.gate.com/aapl.png",
            "quote_currency_symbol": "$",
            "price_precision": 2,
            "volume_precision": 4,
            "is_ipo": false,
            "sell_price_protection": "0.1",
            "buy_price_protection": "0.1",
            "symbol_descs": [
              {
                "lang": "en",
                "value": "Apple Inc."
              }
            ],
            "margin_mode": 1,
            "long_im": "0.25",
            "long_mm": "0.45",
            "short_im": "0.3",
            "short_mm": "0.5",
            "long_borrowing_rate": "0.03",
            "short_borrowing_rate": ""
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query symbol details

GET`/stock/symbols/detail`

GET `/stock/symbols/detail`

_Query symbol details_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Optional | Symbol list, multiple separated by commas  
exchange | query | string | Optional | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
page | query | integer | Optional | Page number, defaults to 1  
page_size | query | integer | Optional | Page size, defaults to 10, max 500; server caps at 500  
  
####  Detailed descriptions

**exchange** : Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | SymbolDetail  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» total | integer(int64) | Total quantity  
»» total_page | integer | Total pages  
»» list | array | none  
»»» symbol | string | Symbol  
»»» exchange | string | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»»» exchange_desc | string | Exchange description  
»»» quote_currency | string | Quote currency  
»»» quote_currency_precision | integer | Quote currency precision  
»»» fx_rate | string | Quote currency to USD exchange rate  
»»» symbol_desc | string | Symbol description  
»»» category | string | Symbol category.  
\- CS: Common stock.  
\- ETF: Exchange-traded funds.  
\- ADRC, ADR: Depositary receipts for foreign companies listed in the U.S.  
\- ETV: Exchange-traded products.  
\- PFD: Preferred stock.  
\- ETS: Exchange-traded securities.  
\- ETN: Exchange-traded notes.  
\- FUND: Funds.  
»»» asset_type | string | Asset type.  
\- STOCK: Stock.  
\- ETF: Exchange-traded fund.  
»»» settlement_currency | string | Settlement currency  
»»» max_order_volume | string | Maximum order quantity  
»»» step_order_volume | string | Order step size  
»»» min_order_volume | string | Minimum order quantity  
»»» price_precision | integer | Price precision  
»»» volume_precision | integer | Quantity precision  
»»» is_ipo | boolean | Whether it is an IPO symbol  
»»» ipo_price | string | IPO price  
»»» price_protection | string | Price protection range  
»»» sell_price_protection | string | Sell price protection rate  
»»» buy_price_protection | string | Buy price protection rate  
»»» slippage_rate | string | Slippage  
»»» commission_rate | string | Fee Rate  
»»» trade_status | string | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
»»» trade_mode | integer | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
\- 6: Trading suspended.  
\- 7: Trading suspended.  
\- 8: Trading suspended.  
»»» order_fill_timing | integer | Order fill timing (1=immediate, 2=after pre-market opens, 3=after regular session opens)  
»»» symbol_descs | array | Multilingual symbol description  
»»»» lang | string | Language  
»»»» value | string | Localized description  
»»» icon_link | string | Icon URL  
»»» margin_mode | integer | Margin trading mode.  
\- 0: Neither margin financing nor securities borrowing is supported.  
\- 1: Margin financing is supported.  
\- 2: Securities borrowing is supported.  
\- 3: Both margin financing and securities borrowing are supported.  
»»» long_im | string | Initial margin ratio for long positions  
»»» long_mm | string | Maintenance margin ratio for long positions  
»»» short_im | string | Initial margin ratio for short positions  
»»» short_mm | string | Maintenance margin ratio for short positions  
»»» long_borrowing_rate | string | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
»»» short_borrowing_rate | string | Annual securities borrowing interest rate. An empty string indicates that no valid rate is currently available.  
»» timestamp | integer(int64) | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
category | CS  
category | ETF  
category | ADRC  
category | ADR  
category | ETV  
category | PFD  
category | ETS  
category | ETN  
category | FUND  
asset_type | STOCK  
asset_type | ETF  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
order_fill_timing | 1  
order_fill_timing | 2  
order_fill_timing | 3  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/symbols/detail'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/symbols/detail \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "symbol": "AAPL",
            "exchange": "us",
            "exchange_desc": "United States",
            "quote_currency": "USD",
            "quote_currency_precision": 2,
            "fx_rate": "1",
            "symbol_desc": "Apple Inc.",
            "category": "CS",
            "asset_type": "STOCK",
            "settlement_currency": "USD",
            "max_order_volume": "10000",
            "step_order_volume": "1",
            "min_order_volume": "1",
            "price_precision": 2,
            "volume_precision": 4,
            "is_ipo": false,
            "ipo_price": "15",
            "price_protection": "0.1",
            "sell_price_protection": "0.1",
            "buy_price_protection": "0.1",
            "slippage_rate": "0.001",
            "commission_rate": "0.001",
            "trade_status": "open",
            "trade_mode": 4,
            "order_fill_timing": 1,
            "symbol_descs": [
              {
                "lang": "en",
                "value": "Apple Inc."
              }
            ],
            "icon_link": "https://static.gate.com/aapl.png",
            "margin_mode": 1,
            "long_im": "0.25",
            "long_mm": "0.45",
            "short_im": "0.3",
            "short_mm": "0.5",
            "long_borrowing_rate": "0.03",
            "short_borrowing_rate": ""
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query market order book

GET`/stock/market/{symbol}/orderbook`

GET `/stock/market/{symbol}/orderbook`

_Query market order book_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | path | string | Required | Symbol  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotOrderBook  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» symbol | string | Symbol  
»» bids | array | Bid orders  
»»» p | string | Price  
»»» user_order | boolean | Whether it is the user's own order  
»» asks | array | Ask orders  
»»» p | string | Price  
»»» user_order | boolean | Whether it is the user's own order  
»» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/market/AAPL/orderbook'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/market/AAPL/orderbook \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "symbol": "AAPL",
        "bids": [
          {
            "p": "200.11",
            "user_order": false
          }
        ],
        "asks": [
          {
            "p": "200.12",
            "user_order": false
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query open order list🔒 Authenticated

GET`/stock/orders`

GET `/stock/orders`

_Query open order list_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | query | string | Optional | Symbol  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotOrderList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» list | array | Query active order list  
»»» order_id | string | Order ID  
»»» symbol | string | Symbol  
»»» exchange | string | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»»» quote_currency | string | Quote currency  
»»» fx_rate | string | Quote currency to USD exchange rate  
»»» symbol_desc | string | Symbol description  
»»» trade_status | string | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
»»» trade_mode | integer | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
\- 6: Trading suspended.  
\- 7: Trading suspended.  
\- 8: Trading suspended.  
»»» price_type | string | Price type (market = market order, limit = limit order)  
»»» side | integer | Side (1=sell, 2=buy)  
»»» status | integer | Order status.  
\- 0: Unknown.  
\- 1: New order; the order has been validated and is waiting to be processed.  
\- 2: Partially filled.  
\- 3: Filled.  
\- 4: Canceled.  
\- 5: Order rejected.  
\- 6: Cancellation rejected.  
\- 7: Order update succeeded.  
\- 8: Order update rejected.  
»»» volume | string | Order quantity  
»»» fill_volume | string | Trading size  
»»» price | string | Order price  
»»» time_setup | integer(int64) | Order creation time (Unix timestamp, seconds)  
»»» time_update | integer(int64) | Order update time (Unix timestamp, seconds)  
»»» max_order_volume | string | Maximum order quantity  
»»» step_order_volume | string | Order step size  
»»» min_order_volume | string | Minimum order quantity  
»»» price_precision | integer | Price precision  
»»» price_protection | string | Price protection range  
»»» sell_price_protection | string | Sell price protection rate  
»»» buy_price_protection | string | Buy price protection rate  
»»» commission_rate | string | Fee Rate  
»»» slippage_rate | string | Slippage  
»» timestamp | integer(int64) | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
price_type | market  
price_type | limit  
side | 1  
side | 2  
status | 0  
status | 1  
status | 2  
status | 3  
status | 4  
status | 5  
status | 6  
status | 7  
status | 8  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/orders'
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
    url="/stock/orders"
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
            "order_id": "123456",
            "symbol": "AAPL",
            "exchange": "us",
            "quote_currency": "USD",
            "fx_rate": "1",
            "symbol_desc": "Apple Inc.",
            "trade_status": "open",
            "trade_mode": 3,
            "price_type": "limit",
            "side": 2,
            "status": 1,
            "volume": "10",
            "fill_volume": "2",
            "price": "200.12",
            "time_setup": 1769378400,
            "time_update": 1769378500,
            "max_order_volume": "10000",
            "step_order_volume": "1",
            "min_order_volume": "1",
            "price_precision": 2,
            "price_protection": "0.1",
            "sell_price_protection": "0.1",
            "buy_price_protection": "0.1",
            "commission_rate": "0.001",
            "slippage_rate": "0.001"
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Create order🔒 Authenticated

POST`/stock/orders`

POST `/stock/orders`

_Create order_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiSpotOrderRequest | Required | none  
» volume | body | string | Required | Order quantity  
» symbol | body | string | Required | Symbol  
» side | body | integer | Required | Side (1=sell, 2=buy)  
» price_type | body | string | Required | Price type (market = market order, limit = limit order)  
» trading_session | body | string | Required | Trading session.  
Limit orders support only all, while market orders support only regular.  
» time_in_force | body | string | Required | Time in force.  
\- day: Day order.  
» price | body | string | Optional | Order price, used for limit orders  
» client_order_id | body | string | Optional | Client-defined order ID  
  
####  Detailed descriptions

**» trading_session** : Trading session.  
Limit orders support only all, while market orders support only regular.

**» time_in_force** : Time in force.  
\- day: Day order.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» side | 1  
» side | 2  
» price_type | market  
» price_type | limit  
» trading_session | regular  
» trading_session | all  
» time_in_force | day  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order placed successfully | TradfiSpotCreateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» id | string | Order ID  
» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/orders'
    query_param = ''
    body='{"volume":"10","symbol":"AAPL","side":2,"price_type":"limit","trading_session":"all","time_in_force":"day","price":"200.12","client_order_id":"client-202607070001"}'
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
    url="/stock/orders"
    query_param=""
    body_param='{"volume":"10","symbol":"AAPL","side":2,"price_type":"limit","trading_session":"all","time_in_force":"day","price":"200.12","client_order_id":"client-202607070001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "volume": "10",
      "symbol": "AAPL",
      "side": 2,
      "price_type": "limit",
      "trading_session": "all",
      "time_in_force": "day",
      "price": "200.12",
      "client_order_id": "client-202607070001"
    }
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "id": "123456"
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Cancel all open orders🔒 Authenticated

DELETE`/stock/orders`

DELETE `/stock/orders`

_Cancel all open orders_

Rate limit: 5 qps.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | DeleteOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | Returns empty object on success  
» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/orders'
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
    url="/stock/orders"
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
      "data": {},
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query historical order list🔒 Authenticated

GET`/stock/orders/history`

GET `/stock/orders/history`

_Query historical order list_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | query | string | Optional | Symbol  
order_ids | query | string | Optional | Order ID list, multiple separated by commas; max 20, each must be a positive integer  
begin_time | query | integer(int32) | Optional | Start time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be >= begin_time, query range must not exceed 3 months.  
end_time | query | integer(int32) | Optional | End time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be >= begin_time, query range must not exceed 3 months.  
side | query | integer | Optional | Side (1=sell, 2=buy)  
page | query | integer | Optional | Page number, defaults to 1  
page_size | query | integer | Optional | Page size, defaults to 10, max 500; server caps at 500  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | 1  
side | 2  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotOrderHistoryList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» total | integer(int64) | Total quantity  
»» total_page | integer | Total pages  
»» list | array | Query historical order list  
»»» order_id | string | Order ID  
»»» symbol | string | Symbol  
»»» exchange | string | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»»» quote_currency | string | Quote currency  
»»» fx_rate | string | Quote currency to USD exchange rate  
»»» symbol_desc | string | Symbol description  
»»» price_type | string | Price type (market = market order, limit = limit order)  
»»» status | integer | Order status.  
\- 0: Unknown.  
\- 1: New order; the order has been validated and is waiting to be processed.  
\- 2: Partially filled.  
\- 3: Filled.  
\- 4: Canceled.  
\- 5: Order rejected.  
\- 6: Cancellation rejected.  
\- 7: Order update succeeded.  
\- 8: Order update rejected.  
»»» status_desc | string | Order status description  
»»» status_detail | object|null | Order status details  
»»»» title | string | Status title  
»»»» message | string | Status message  
»»» finish_as | integer | Order completion reason.  
\- 0: Unknown.  
\- 1: No quote found.  
\- 2: No match found.  
\- 3: Trigger price exceeded.  
\- 4: Order value exceeds the limit.  
\- 5: Unknown rejection.  
\- 6: Unknown cancellation.  
\- 7: Canceled by user.  
\- 8: Canceled after the order time in force expired.  
\- 9: Trading is not supported in the current session.  
\- 13: Canceled due to corporate action.  
»»» side | integer | Side (1=sell, 2=buy)  
»»» time_in_force | string | Time in force.  
\- day: Day order.  
»»» volume | string | Order quantity  
»»» fill_volume | string | Trading size  
»»» price | string | Order price  
»»» avg_fill_price | string|null | Average fill price  
»»» commission | string | fee  
»»» time_setup | integer(int64) | Order creation time (Unix timestamp, seconds)  
»»» time_done | integer(int64) | Order completion time (Unix timestamp in seconds)  
»» timestamp | integer(int64) | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
price_type | market  
price_type | limit  
status | 0  
status | 1  
status | 2  
status | 3  
status | 4  
status | 5  
status | 6  
status | 7  
status | 8  
finish_as | 0  
finish_as | 1  
finish_as | 2  
finish_as | 3  
finish_as | 4  
finish_as | 5  
finish_as | 6  
finish_as | 7  
finish_as | 8  
finish_as | 9  
finish_as | 13  
side | 1  
side | 2  
time_in_force | day  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/orders/history'
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
    url="/stock/orders/history"
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
            "order_id": "123456",
            "symbol": "AAPL",
            "exchange": "us",
            "quote_currency": "USD",
            "fx_rate": "1",
            "symbol_desc": "Apple Inc.",
            "price_type": "limit",
            "status": 3,
            "status_desc": "filled",
            "status_detail": {
              "title": "Filled",
              "message": "Order filled"
            },
            "finish_as": 0,
            "side": 2,
            "time_in_force": "day",
            "volume": "10",
            "fill_volume": "10",
            "price": "200.12",
            "avg_fill_price": "200.10",
            "commission": "2.001",
            "time_setup": 1769378400,
            "time_done": 1769378500
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query order trade records🔒 Authenticated

GET`/stock/orders/deals`

GET `/stock/orders/deals`

_Query order trade records_

Rate limit: 5 requests per second. Query the current user's trade records by order ID. `price`, `value`, and `fee` are denominated in the instrument trading currency (for example, USD for US stocks, HKD for Hong Kong stocks, JPY for Japanese stocks, and KRW for Korean stocks). `role` returns `maker` or `taker`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | query | integer(int64) | Required | Order ID  
page | query | integer | Optional | Page number, defaults to 1  
page_size | query | integer | Optional | Records per page. Defaults to 10, maximum 100. The server caps values greater than 100 at 100.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | OrderDealList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» total | integer(int64) | Total quantity  
»» total_page | integer(int64) | Total pages  
»» list | array | Trade records  
»»» id | integer(int64) | Trade record primary key ID  
»»» deal_id | integer(int64) | Trade ID  
»»» order_id | integer(int64) | Order ID  
»»» client_order_id | string | Client-defined order ID  
»»» user_id | integer | User ID  
»»» symbol | string | Symbol  
»»» exchange | string | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»»» side | integer | Side (1=sell, 2=buy)  
»»» role | string | Liquidity role.  
\- maker: Maker.  
\- taker: Taker.  
»»» price | string | Trade price in the instrument trading currency  
»»» quantity | string | Trading size  
»»» position_qty | string | Position quantity after the trade  
»»» avg_entry_price | string | Average entry price  
»»» value | string | Trade value in the instrument trading currency  
»»» fx_rate | string | Quote currency to USD exchange rate  
»»» fee | string | Fee in the instrument trading currency  
»» timestamp | integer(int64) | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
side | 1  
side | 2  
role | maker  
role | taker  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/orders/deals'
    query_param = 'order_id=123456'
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
    url="/stock/orders/deals"
    query_param="order_id=123456"
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
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "id": 10001,
            "deal_id": 90001,
            "order_id": 123456,
            "client_order_id": "client-202607070001",
            "user_id": 100001,
            "symbol": "AAPL",
            "exchange": "us",
            "side": 2,
            "role": "taker",
            "price": "200.10",
            "quantity": "5",
            "position_qty": "15",
            "avg_entry_price": "198.50",
            "value": "1000.50",
            "fx_rate": "1",
            "fee": "1.001"
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Modify order🔒 Authenticated

PUT`/stock/orders/{order_id}`

PUT `/stock/orders/{order_id}`

_Modify order_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiSpotOrderUpdateRequest | Required | none  
» volume | body | string | Required | Modified order quantity  
» price | body | string | Required | Modified order price  
order_id | path | integer(int64) | Required | Order ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotUpdateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» order_id | integer(int64) | Order ID  
» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/orders/123456'
    query_param = ''
    body='{"volume":"8","price":"201.23"}'
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
    url="/stock/orders/123456"
    query_param=""
    body_param='{"volume":"8","price":"201.23"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "volume": "8",
      "price": "201.23"
    }
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Cancel order🔒 Authenticated

DELETE`/stock/orders/{order_id}`

DELETE `/stock/orders/{order_id}`

_Cancel order_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | integer(int64) | Required | Order ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | DeleteOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | Returns empty object on success  
» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/orders/123456'
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
    url="/stock/orders/123456"
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
      "data": {},
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query current position list🔒 Authenticated

GET`/stock/positions`

GET `/stock/positions`

_Query current position list_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
pnl_calc_type | query | integer | Optional | PnL calculation cost type. Defaults to average cost price when omitted (1 = average cost price, 2 = diluted cost price)  
pnl_calc_price | query | integer | Optional | PnL calculation price type. Defaults to intraday price when omitted (1 = intraday price, 2 = latest extended-hours price)  
symbol | query | string | Optional | Symbol  
exchange | query | string | Optional | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
  
####  Detailed descriptions

**exchange** : Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
pnl_calc_type | 1  
pnl_calc_type | 2  
pnl_calc_price | 1  
pnl_calc_price | 2  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotPositionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» list | array | Query active position list  
»»» symbol | string | Symbol  
»»» exchange | string | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»»» quote_currency | string | Quote currency  
»»» quote_currency_precision | integer | Quote currency precision  
»»» fx_rate | string | Quote currency to USD exchange rate  
»»» trade_status | string | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
»»» symbol_desc | string | Symbol description  
»»» position_pnl | string | Position P&L  
»»» today_pnl | string | Today's P&L  
»»» pnl_rate | string | Yield  
»»» today_sell_amount | string | Today's sales amount  
»»» today_buy_amount | string | Today's purchase amount  
»»» today_sell_volume | string | Today's sell volume  
»»» today_buy_volume | string | Today's buy volume  
»»» yesterday_volume | string | Previous close position quantity  
»»» volume | string | Position quantity  
»»» available | string | Available position quantity  
»»» transfer_out_pending_qty | string | Stock transfer in progress quantity  
»»» avg_cost_price | string | Cost price  
»»» diluted_cost_price | string | Diluted cost price  
»»» last_price | string | Latest price  
»»» extended_last_price | string|null | Extended hours latest price  
»»» max_order_volume | string | Maximum order quantity  
»»» step_order_volume | string | Order step size  
»»» min_order_volume | string | Minimum order quantity  
»»» price_precision | integer | Price precision  
»»» price_protection | string | Price protection range  
»»» sell_price_protection | string | Sell price protection rate  
»»» buy_price_protection | string | Buy price protection rate  
»»» commission_rate | string | Fee Rate  
»»» slippage_rate | string | Slippage  
»» timestamp | integer(int64) | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/positions'
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
    url="/stock/positions"
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
            "symbol": "AAPL",
            "exchange": "us",
            "quote_currency": "USD",
            "quote_currency_precision": 2,
            "fx_rate": "1",
            "trade_status": "open",
            "symbol_desc": "Apple Inc.",
            "position_pnl": "12.5",
            "today_pnl": "3.2",
            "pnl_rate": "0.012",
            "today_sell_amount": "0",
            "today_buy_amount": "2001.2",
            "today_sell_volume": "0",
            "today_buy_volume": "10",
            "yesterday_volume": "8",
            "volume": "10",
            "available": "8",
            "transfer_out_pending_qty": "0",
            "avg_cost_price": "198.11",
            "diluted_cost_price": "198.11",
            "last_price": "200.12",
            "extended_last_price": "200.2",
            "max_order_volume": "10000",
            "step_order_volume": "1",
            "min_order_volume": "1",
            "price_precision": 2,
            "price_protection": "0.1",
            "sell_price_protection": "0.1",
            "buy_price_protection": "0.1",
            "commission_rate": "0.001",
            "slippage_rate": "0.001"
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Close position🔒 Authenticated

POST`/stock/positions/close`

POST `/stock/positions/close`

_Close position_

Rate limit: 5 qps.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiSpotClosePositionRequest | Required | none  
» symbol | body | string | Required | Symbol  
» close_volume | body | string | Optional | Close quantity; required for partial close  
» close_type | body | integer | Required | Close type (1=partial close, 2=close all)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» close_type | 1  
» close_type | 2  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | ClosePosition  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» order_id | integer(int64) | Close order ID  
» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/positions/close'
    query_param = ''
    body='{"symbol":"AAPL","close_volume":"2","close_type":1}'
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
    url="/stock/positions/close"
    query_param=""
    body_param='{"symbol":"AAPL","close_volume":"2","close_type":1}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "symbol": "AAPL",
      "close_volume": "2",
      "close_type": 1
    }
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query transaction records🔒 Authenticated

GET`/stock/transactions`

GET `/stock/transactions`

_Query transaction records_

Rate limit: 5 qps. Query stock account transaction records, including fund transfers, trades, fees, dividends, rewards, and stock transfers.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
begin_time | query | integer(int64) | Optional | Start time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be >= begin_time, query range must not exceed 3 months.  
end_time | query | integer(int64) | Optional | End time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be >= begin_time, query range must not exceed 3 months.  
ref_id | query | string | Optional | Business idempotent ID. When ref_id is provided, the server queries by ref_id, ignoring other parameters such as begin_time, end_time, type, page, page_size  
type | query | string | Optional | Transaction type.  
page | query | integer | Optional | Page number, defaults to 1  
page_size | query | integer | Optional | Page size, defaults to 10, max 500; server caps at 500  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | deposit  
type | withdraw  
type | fee  
type | dividend  
type | sell  
type | buy  
type | award  
type | stock_transfer_in  
type | stock_transfer_out  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotTransactionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» total | integer(int64) | none  
»» total_page | integer(int64) | none  
»» list | array | Transaction record list  
»»» asset | string | Asset  
»»» symbol | string | Symbol  
»»» symbol_display | string | Symbol display name  
»»» type | string | Transaction type.  
\- deposit: Funds transfer in.  
\- withdraw: Funds transfer out.  
\- fee: Trading fee.  
\- dividend: Dividend payout.  
\- sell: Stock sale credit.  
\- buy: Stock purchase debit.  
\- award: Airdrop reward.  
\- stock_transfer_in: Stock transfer in.  
\- stock_transfer_out: Stock transfer out.  
»»» type_desc | string | Transaction type description  
»»» change | string | Change amount. A positive value means a credit, and a negative value means a debit.  
»»» balance | string | Balance after change  
»»» ref_id | string | Business idempotent ID  
»»» time | integer(int64) | Unix timestamp (seconds)  
»»» unit_text | string | Unit display text  
»»» detail | object | Business details  
»» timestamp | integer(int64) | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | deposit  
type | withdraw  
type | fee  
type | dividend  
type | sell  
type | buy  
type | award  
type | stock_transfer_in  
type | stock_transfer_out  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/transactions'
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
    url="/stock/transactions"
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
            "asset": "USDT",
            "symbol": "AAPL",
            "symbol_display": "Apple Inc.",
            "type": "deposit",
            "type_desc": "Deposit",
            "change": "100",
            "balance": "1000",
            "ref_id": "transfer-202607070001",
            "time": 1769378400,
            "unit_text": "USDT",
            "detail": {
              "source": "api"
            }
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Fund transfer🔒 Authenticated

POST`/stock/transactions`

POST `/stock/transactions`

_Fund transfer_

Rate limit: 5 qps. Fund transfer moves USDT between the spot account and the stock account.

  * deposit: transfer from the spot account to the stock account.
  * withdraw: transfer from the stock account to the spot account.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | TradFiSpotTransactionRequest | Required | none  
» asset | body | string | Required | Asset, USDT only  
» change | body | string | Required | Change amount, must be greater than 0  
» type | body | string | Required | Transaction type. deposit transfers funds from the spot account to the stock account; withdraw transfers funds from the stock account to the spot account.  
» ref_id | body | string | Required | Business idempotent ID  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» asset | USDT  
» type | deposit  
» type | withdraw  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotCreateTransaction  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | Returns empty object on success  
» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/transactions'
    query_param = ''
    body='{"asset":"USDT","change":"100","type":"deposit","ref_id":"transfer-202607070001"}'
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
    url="/stock/transactions"
    query_param=""
    body_param='{"asset":"USDT","change":"100","type":"deposit","ref_id":"transfer-202607070001"}'
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
      "change": "100",
      "type": "deposit",
      "ref_id": "transfer-202607070001"
    }
    

> Example responses

> 200 Response
    
    
    {
      "data": {},
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query user balance records🔒 Authenticated

GET`/stock/users/balance-records`

GET `/stock/users/balance-records`

_Query user balance records_

Rate limit: 5 requests per second. Query the current user's raw balance records. User scope is derived from the request headers; a query parameter `user_id` is not supported.

  * `type` and `business` support multiple comma-separated values.
  * `begin_time` and `end_time` filter record creation time in seconds. When both are provided, `end_time` must be greater than `begin_time`.
  * Results are always sorted by primary key `id`; `sort_direction` accepts `asc` or `desc`. The default is `id desc`. With `start_id` and no `sort_direction`, the order is `id asc`, and only records with `id > start_id` are returned for incremental retrieval.
  * `detail` is omitted by default and returned only when `include_detail=true`.
  * `stock_change` is parsed from `detail.amount` for stock quantity records; `balance` is a cash balance snapshot, not a stock position balance.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
type | query | string | Optional | Record types, separated by commas  
business | query | string | Optional | Business identifiers, separated by commas  
symbol | query | string | Optional | Symbol  
begin_time | query | integer(int64) | Optional | Start time (Unix timestamp in seconds). When both begin_time and end_time are provided, end_time must be greater than begin_time.  
end_time | query | integer(int64) | Optional | End time (Unix timestamp in seconds). When both begin_time and end_time are provided, end_time must be greater than begin_time.  
start_id | query | integer(int64) | Optional | Starting primary key ID for incremental queries. Only records with a greater id are returned.  
sort_direction | query | string | Optional | Sort direction by primary key id.  
\- asc: Ascending.  
\- desc: Descending.  
When omitted, defaults to desc without start_id, or asc with start_id.  
include_detail | query | boolean | Optional | Whether to return the raw detail field; defaults to false when omitted  
page | query | integer | Optional | Page number, defaults to 1  
page_size | query | integer | Optional | Records per page. Defaults to 10, maximum 100. The server caps values greater than 100 at 100.  
  
####  Detailed descriptions

**sort_direction** : Sort direction by primary key id.  
\- asc: Ascending.  
\- desc: Descending.  
When omitted, defaults to desc without start_id, or asc with start_id.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
sort_direction | asc  
sort_direction | desc  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | BalanceRecordList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» total | integer(int64) | Total quantity  
»» total_page | integer(int64) | Total pages  
»» list | array | Balance record details  
»»» id | integer(int64) | Balance record primary key ID  
»»» user_id | integer | User ID  
»»» change | string | Cash amount change. Positive values are credits; negative values are debits.  
»»» balance | string | Cash balance snapshot after the change  
»»» stock_change | string | Stock quantity change, parsed from detail.amount for stock quantity records; may be an empty string for other records  
»»» type | string | Raw record type. Common values include:  
\- deposit: Funds transferred in.  
\- withdraw: Funds transferred out.  
\- fee: Trading fee.  
\- dividend: Dividend payment.  
\- sell: Proceeds from selling stocks.  
\- buy: Payment for buying stocks.  
\- award: Airdrop reward.  
\- stock_transfer_in: Stocks transferred in.  
\- stock_transfer_out: Stocks transferred out.  
»»» business | string | Business identifier  
»»» business_id | integer(int64) | Related business ID  
»»» symbol | string | Symbol  
»»» detail | string | Raw business details as a JSON string; returned only when include_detail=true is requested  
»»» version | integer | Record version  
»»» time_create | integer(int64) | Business event time (Unix timestamp in seconds)  
»»» create_time | integer(int64) | Record creation time (Unix timestamp in seconds)  
»» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
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
    
    url = '/stock/users/balance-records'
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
    url="/stock/users/balance-records"
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
            "id": 1001,
            "user_id": 100001,
            "change": "100",
            "balance": "1000",
            "stock_change": "10",
            "type": "deposit",
            "business": "transfer",
            "business_id": 2001,
            "symbol": "AAPL",
            "detail": "{\"amount\":\"10\",\"source\":\"api\"}",
            "version": 1,
            "time_create": 1769378400,
            "create_time": 1769378400
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query supported exchanges

GET`/stock/exchanges`

GET `/stock/exchanges`

_Query supported exchanges_

Query stock spot supported exchanges and whether stock transfers are supported. Rate limit: 5 qps.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | Exchanges  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» list | array | none  
»»» exchange | string | Trading market.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»»» exchange_desc | string | Market display name  
»»» icon_link | string | Market icon  
»»» support_transfer | boolean | Whether stock transfer is supported  
»» timestamp | integer(int64) | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/exchanges'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/exchanges \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "list": [
          {
            "exchange": "us",
            "exchange_desc": "United States",
            "icon_link": "https://static.gate.com/us.png",
            "support_transfer": true
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  Query fee rates for Japanese and Korean stocks

GET`/stock/fee-rate`

GET `/stock/fee-rate`

_Query fee rates for Japanese and Korean stocks_

Query fee rates for Japanese and Korean stocks. Rate limit: 5 qps.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | FeeRate  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» data | object | none  
»» list | array | none  
»»» vip_level | integer | VIP level  
»»» maker_fee | string | Maker fee rate for Japanese and Korean stocks  
»»» taker_fee | string | Taker fee rate for Japanese and Korean stocks  
»» timestamp | integer(int64) | none  
  
Status Code **400**

_TradFiSpotError_

Name | Type | Description  
---|---|---  
» label | string | Business error label  
» message | string | Error message  
» data | object|null | Error additional data  
» timestamp | integer(int64) | Server timestamp (milliseconds)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/fee-rate'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/fee-rate \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "data": {
        "list": [
          {
            "vip_level": 0,
            "maker_fee": "0.001",
            "taker_fee": "0.001"
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

#  Schemas

##  TradFiSpotError

_TradFiSpotError_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
label | string | Optional | none | Business error label  
message | string | Optional | none | Error message  
data | object|null | Optional | none | Error additional data  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": {},
      "timestamp": 1783411200000
    }
    
    

##  TradfiSpotUpdateOrder

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» order_id | integer(int64) | Optional | none | Order ID  
timestamp | integer(int64) | Optional | none | none  
      
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotOrderRequest

_Place order request parameters_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
volume | string | Required | none | Order quantity  
symbol | string | Required | none | Symbol  
side | integer | Required | none | Side (1=sell, 2=buy)  
price_type | string | Required | none | Price type (market = market order, limit = limit order)  
trading_session | string | Required | none | Trading session.  
Limit orders support only all, while market orders support only regular.  
time_in_force | string | Required | none | Time in force.  
\- day: Day order.  
price | string | Optional | none | Order price, used for limit orders  
client_order_id | string | Optional | none | Client-defined order ID  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
side | 1  
side | 2  
price_type | market  
price_type | limit  
trading_session | regular  
trading_session | all  
time_in_force | day  
      
    
    {
      "volume": "10",
      "symbol": "AAPL",
      "side": 2,
      "price_type": "limit",
      "trading_session": "all",
      "time_in_force": "day",
      "price": "200.12",
      "client_order_id": "client-202607070001"
    }
    
    

##  DeleteOrder

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | Returns empty object on success  
timestamp | integer(int64) | Optional | none | none  
      
    
    {
      "data": {},
      "timestamp": 0
    }
    
    

##  SetMarginFeature

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | Returns empty object on success  
timestamp | integer(int64) | Optional | none | none  
      
    
    {
      "data": {},
      "timestamp": 0
    }
    
    

##  Exchanges

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» list | array | Optional | none | none  
»» exchange | string | Optional | none | Trading market.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»» exchange_desc | string | Optional | none | Market display name  
»» icon_link | string | Optional | none | Market icon  
»» support_transfer | boolean | Optional | none | Whether stock transfer is supported  
» timestamp | integer(int64) | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotSetMarginFeatureRequest

_Request parameters for enabling or disabling margin financing_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
margin_feature | boolean | Required | none | Whether to enable margin financing. true enables it; false disables it.  
      
    
    {
      "margin_feature": true
    }
    
    

##  FeeRate

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» list | array | Optional | none | none  
»» vip_level | integer | Optional | none | VIP level  
»» maker_fee | string | Optional | none | Maker fee rate for Japanese and Korean stocks  
»» taker_fee | string | Optional | none | Taker fee rate for Japanese and Korean stocks  
» timestamp | integer(int64) | Optional | none | none  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotSymbols

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» total | integer(int64) | Optional | none | Total quantity  
» total_page | integer | Optional | none | Total pages  
» list | array | Optional | none | Symbol list  
»» symbol | string | Optional | none | Symbol  
»» exchange | string | Optional | none | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»» exchange_desc | string | Optional | none | Exchange description  
»» quote_currency | string | Optional | none | Quote currency  
»» quote_currency_precision | integer | Optional | none | Quote currency precision  
»» fx_rate | string | Optional | none | Quote currency to USD exchange rate  
»» symbol_desc | string | Optional | none | Symbol description  
»» category | string | Optional | none | Symbol category.  
\- CS: Common stock.  
\- ETF: Exchange-traded funds.  
\- ADRC, ADR: Depositary receipts for foreign companies listed in the U.S.  
\- ETV: Exchange-traded products.  
\- PFD: Preferred stock.  
\- ETS: Exchange-traded securities.  
\- ETN: Exchange-traded notes.  
\- FUND: Funds.  
»» asset_type | string | Optional | none | Asset type.  
\- STOCK: Stock.  
\- ETF: Exchange-traded fund.  
»» trade_status | string | Optional | none | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
»» trade_mode | integer | Optional | none | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
\- 6: Trading suspended.  
\- 7: Trading suspended.  
\- 8: Trading suspended.  
»» order_fill_timing | integer | Optional | none | Order fill timing (1=immediate, 2=after pre-market opens, 3=after regular session opens)  
»» icon_link | string | Optional | none | Icon URL  
»» quote_currency_symbol | string | Optional | none | Quote currency symbol  
»» price_precision | integer | Optional | none | Price precision  
»» volume_precision | integer | Optional | none | Quantity precision  
»» is_ipo | boolean | Optional | none | Whether it is an IPO symbol  
»» ipo_price | string | Optional | none | IPO price  
»» sell_price_protection | string | Optional | none | Sell price protection rate  
»» buy_price_protection | string | Optional | none | Buy price protection rate  
»» symbol_descs | [TradfiSpotSymbols/definitions/SymbolListItem/properties/symbol_descs/items] | Optional | none | Multilingual symbol description  
»» margin_mode | integer | Optional | none | Margin trading mode.  
\- 0: Neither margin financing nor securities borrowing is supported.  
\- 1: Margin financing is supported.  
\- 2: Securities borrowing is supported.  
\- 3: Both margin financing and securities borrowing are supported.  
»» long_im | string | Optional | none | Initial margin ratio for long positions  
»» long_mm | string | Optional | none | Maintenance margin ratio for long positions  
»» short_im | string | Optional | none | Initial margin ratio for short positions  
»» short_mm | string | Optional | none | Maintenance margin ratio for short positions  
»» long_borrowing_rate | string | Optional | none | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
»» short_borrowing_rate | string | Optional | none | Annual securities borrowing interest rate. An empty string indicates that no valid rate is currently available.  
» timestamp | integer(int64) | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
category | CS  
category | ETF  
category | ADRC  
category | ADR  
category | ETV  
category | PFD  
category | ETS  
category | ETN  
category | FUND  
asset_type | STOCK  
asset_type | ETF  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
order_fill_timing | 1  
order_fill_timing | 2  
order_fill_timing | 3  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotUserAssetResp

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» equity | string | Optional | none | Account equity  
» balance | string | Optional | none | Account Balance  
» available | string | Optional | none | Available Balance  
» loan_amount | string | Optional | none | Loan amount. Non-negative: the absolute value of the original available balance when it is negative, otherwise 0.  
» buy_power | string | Optional | none | Buying power  
» leverage | string | Optional | none | Leverage  
» leave_liquidity | string | Optional | none | Excess liquidity  
» leave_liquidity_rate | string | Optional | none | Excess liquidity ratio  
» aee | string | Optional | none | Available Excess Equity (AEE)  
» options_margin | string | Optional | none | Options margin  
» position_market_value | string | Optional | none | Position market value  
» position_pnl | string | Optional | none | Position P&L  
» today_pnl | string | Optional | none | Today's P&L  
» option_position_market_value | string | Optional | none | Option position market value  
» option_position_pnl | string | Optional | none | Option position PnL  
» option_today_pnl | string | Optional | none | Option today's PnL  
» user_exists | boolean | Optional | none | Whether the user has activated the service  
» margin_enabled | boolean | Optional | none | Whether margin financing is enabled  
» long_borrowing_rate | string | Optional | none | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
timestamp | integer(int64) | Optional | none | Server timestamp (milliseconds)  
      
    
    {
      "data": {
        "equity": "10000.12",
        "balance": "8000",
        "available": "6500.5",
        "loan_amount": "0",
        "buy_power": "13000",
        "leverage": "2",
        "leave_liquidity": "5000",
        "leave_liquidity_rate": "0.5",
        "aee": "4800",
        "options_margin": "0",
        "position_market_value": "1500.25",
        "position_pnl": "12.5",
        "today_pnl": "3.2",
        "option_position_market_value": "0",
        "option_position_pnl": "0",
        "option_today_pnl": "0",
        "user_exists": true,
        "margin_enabled": true,
        "long_borrowing_rate": "0.03"
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotCreateOrder

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» id | string | Optional | none | Order ID  
timestamp | integer(int64) | Optional | none | none  
      
    
    {
      "data": {
        "id": "123456"
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotOrderList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» list | array | Optional | none | Query active order list  
»» order_id | string | Optional | none | Order ID  
»» symbol | string | Optional | none | Symbol  
»» exchange | string | Optional | none | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»» quote_currency | string | Optional | none | Quote currency  
»» fx_rate | string | Optional | none | Quote currency to USD exchange rate  
»» symbol_desc | string | Optional | none | Symbol description  
»» trade_status | string | Optional | none | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
»» trade_mode | integer | Optional | none | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
\- 6: Trading suspended.  
\- 7: Trading suspended.  
\- 8: Trading suspended.  
»» price_type | string | Optional | none | Price type (market = market order, limit = limit order)  
»» side | integer | Optional | none | Side (1=sell, 2=buy)  
»» status | integer | Optional | none | Order status.  
\- 0: Unknown.  
\- 1: New order; the order has been validated and is waiting to be processed.  
\- 2: Partially filled.  
\- 3: Filled.  
\- 4: Canceled.  
\- 5: Order rejected.  
\- 6: Cancellation rejected.  
\- 7: Order update succeeded.  
\- 8: Order update rejected.  
»» volume | string | Optional | none | Order quantity  
»» fill_volume | string | Optional | none | Trading size  
»» price | string | Optional | none | Order price  
»» time_setup | integer(int64) | Optional | none | Order creation time (Unix timestamp, seconds)  
»» time_update | integer(int64) | Optional | none | Order update time (Unix timestamp, seconds)  
»» max_order_volume | string | Optional | none | Maximum order quantity  
»» step_order_volume | string | Optional | none | Order step size  
»» min_order_volume | string | Optional | none | Minimum order quantity  
»» price_precision | integer | Optional | none | Price precision  
»» price_protection | string | Optional | none | Price protection range  
»» sell_price_protection | string | Optional | none | Sell price protection rate  
»» buy_price_protection | string | Optional | none | Buy price protection rate  
»» commission_rate | string | Optional | none | Fee Rate  
»» slippage_rate | string | Optional | none | Slippage  
» timestamp | integer(int64) | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
price_type | market  
price_type | limit  
side | 1  
side | 2  
status | 0  
status | 1  
status | 2  
status | 3  
status | 4  
status | 5  
status | 6  
status | 7  
status | 8  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotOrderUpdateRequest

_Modify order request parameters_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
volume | string | Required | none | Modified order quantity  
price | string | Required | none | Modified order price  
      
    
    {
      "volume": "8",
      "price": "201.23"
    }
    
    

##  TradfiSpotPositionList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» list | array | Optional | none | Query active position list  
»» symbol | string | Optional | none | Symbol  
»» exchange | string | Optional | none | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»» quote_currency | string | Optional | none | Quote currency  
»» quote_currency_precision | integer | Optional | none | Quote currency precision  
»» fx_rate | string | Optional | none | Quote currency to USD exchange rate  
»» trade_status | string | Optional | none | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
»» symbol_desc | string | Optional | none | Symbol description  
»» position_pnl | string | Optional | none | Position P&L  
»» today_pnl | string | Optional | none | Today's P&L  
»» pnl_rate | string | Optional | none | Yield  
»» today_sell_amount | string | Optional | none | Today's sales amount  
»» today_buy_amount | string | Optional | none | Today's purchase amount  
»» today_sell_volume | string | Optional | none | Today's sell volume  
»» today_buy_volume | string | Optional | none | Today's buy volume  
»» yesterday_volume | string | Optional | none | Previous close position quantity  
»» volume | string | Optional | none | Position quantity  
»» available | string | Optional | none | Available position quantity  
»» transfer_out_pending_qty | string | Optional | none | Stock transfer in progress quantity  
»» avg_cost_price | string | Optional | none | Cost price  
»» diluted_cost_price | string | Optional | none | Diluted cost price  
»» last_price | string | Optional | none | Latest price  
»» extended_last_price | string|null | Optional | none | Extended hours latest price  
»» max_order_volume | string | Optional | none | Maximum order quantity  
»» step_order_volume | string | Optional | none | Order step size  
»» min_order_volume | string | Optional | none | Minimum order quantity  
»» price_precision | integer | Optional | none | Price precision  
»» price_protection | string | Optional | none | Price protection range  
»» sell_price_protection | string | Optional | none | Sell price protection rate  
»» buy_price_protection | string | Optional | none | Buy price protection rate  
»» commission_rate | string | Optional | none | Fee Rate  
»» slippage_rate | string | Optional | none | Slippage  
» timestamp | integer(int64) | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotTransactionList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» total | integer(int64) | Optional | none | none  
» total_page | integer(int64) | Optional | none | none  
» list | array | Optional | none | Transaction record list  
»» asset | string | Optional | none | Asset  
»» symbol | string | Optional | none | Symbol  
»» symbol_display | string | Optional | none | Symbol display name  
»» type | string | Optional | none | Transaction type.  
\- deposit: Funds transfer in.  
\- withdraw: Funds transfer out.  
\- fee: Trading fee.  
\- dividend: Dividend payout.  
\- sell: Stock sale credit.  
\- buy: Stock purchase debit.  
\- award: Airdrop reward.  
\- stock_transfer_in: Stock transfer in.  
\- stock_transfer_out: Stock transfer out.  
»» type_desc | string | Optional | none | Transaction type description  
»» change | string | Optional | none | Change amount. A positive value means a credit, and a negative value means a debit.  
»» balance | string | Optional | none | Balance after change  
»» ref_id | string | Optional | none | Business idempotent ID  
»» time | integer(int64) | Optional | none | Unix timestamp (seconds)  
»» unit_text | string | Optional | none | Unit display text  
»» detail | object | Optional | none | Business details  
» timestamp | integer(int64) | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | deposit  
type | withdraw  
type | fee  
type | dividend  
type | sell  
type | buy  
type | award  
type | stock_transfer_in  
type | stock_transfer_out  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  SymbolDetail

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» total | integer(int64) | Optional | none | Total quantity  
» total_page | integer | Optional | none | Total pages  
» list | array | Optional | none | none  
»» symbol | string | Optional | none | Symbol  
»» exchange | string | Optional | none | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»» exchange_desc | string | Optional | none | Exchange description  
»» quote_currency | string | Optional | none | Quote currency  
»» quote_currency_precision | integer | Optional | none | Quote currency precision  
»» fx_rate | string | Optional | none | Quote currency to USD exchange rate  
»» symbol_desc | string | Optional | none | Symbol description  
»» category | string | Optional | none | Symbol category.  
\- CS: Common stock.  
\- ETF: Exchange-traded funds.  
\- ADRC, ADR: Depositary receipts for foreign companies listed in the U.S.  
\- ETV: Exchange-traded products.  
\- PFD: Preferred stock.  
\- ETS: Exchange-traded securities.  
\- ETN: Exchange-traded notes.  
\- FUND: Funds.  
»» asset_type | string | Optional | none | Asset type.  
\- STOCK: Stock.  
\- ETF: Exchange-traded fund.  
»» settlement_currency | string | Optional | none | Settlement currency  
»» max_order_volume | string | Optional | none | Maximum order quantity  
»» step_order_volume | string | Optional | none | Order step size  
»» min_order_volume | string | Optional | none | Minimum order quantity  
»» price_precision | integer | Optional | none | Price precision  
»» volume_precision | integer | Optional | none | Quantity precision  
»» is_ipo | boolean | Optional | none | Whether it is an IPO symbol  
»» ipo_price | string | Optional | none | IPO price  
»» price_protection | string | Optional | none | Price protection range  
»» sell_price_protection | string | Optional | none | Sell price protection rate  
»» buy_price_protection | string | Optional | none | Buy price protection rate  
»» slippage_rate | string | Optional | none | Slippage  
»» commission_rate | string | Optional | none | Fee Rate  
»» trade_status | string | Optional | none | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
»» trade_mode | integer | Optional | none | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
\- 6: Trading suspended.  
\- 7: Trading suspended.  
\- 8: Trading suspended.  
»» order_fill_timing | integer | Optional | none | Order fill timing (1=immediate, 2=after pre-market opens, 3=after regular session opens)  
»» symbol_descs | array | Optional | none | Multilingual symbol description  
»»» lang | string | Optional | none | Language  
»»» value | string | Optional | none | Localized description  
»» icon_link | string | Optional | none | Icon URL  
»» margin_mode | integer | Optional | none | Margin trading mode.  
\- 0: Neither margin financing nor securities borrowing is supported.  
\- 1: Margin financing is supported.  
\- 2: Securities borrowing is supported.  
\- 3: Both margin financing and securities borrowing are supported.  
»» long_im | string | Optional | none | Initial margin ratio for long positions  
»» long_mm | string | Optional | none | Maintenance margin ratio for long positions  
»» short_im | string | Optional | none | Initial margin ratio for short positions  
»» short_mm | string | Optional | none | Maintenance margin ratio for short positions  
»» long_borrowing_rate | string | Optional | none | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
»» short_borrowing_rate | string | Optional | none | Annual securities borrowing interest rate. An empty string indicates that no valid rate is currently available.  
» timestamp | integer(int64) | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
category | CS  
category | ETF  
category | ADRC  
category | ADR  
category | ETV  
category | PFD  
category | ETS  
category | ETN  
category | FUND  
asset_type | STOCK  
asset_type | ETF  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
order_fill_timing | 1  
order_fill_timing | 2  
order_fill_timing | 3  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  ClosePosition

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» order_id | integer(int64) | Optional | none | Close order ID  
timestamp | integer(int64) | Optional | none | none  
      
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotCreateTransaction

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | Returns empty object on success  
timestamp | integer(int64) | Optional | none | none  
      
    
    {
      "data": {},
      "timestamp": 0
    }
    
    

##  OrderDealList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» total | integer(int64) | Optional | none | Total quantity  
» total_page | integer(int64) | Optional | none | Total pages  
» list | array | Optional | none | Trade records  
»» id | integer(int64) | Optional | none | Trade record primary key ID  
»» deal_id | integer(int64) | Optional | none | Trade ID  
»» order_id | integer(int64) | Optional | none | Order ID  
»» client_order_id | string | Optional | none | Client-defined order ID  
»» user_id | integer | Optional | none | User ID  
»» symbol | string | Optional | none | Symbol  
»» exchange | string | Optional | none | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»» side | integer | Optional | none | Side (1=sell, 2=buy)  
»» role | string | Optional | none | Liquidity role.  
\- maker: Maker.  
\- taker: Taker.  
»» price | string | Optional | none | Trade price in the instrument trading currency  
»» quantity | string | Optional | none | Trading size  
»» position_qty | string | Optional | none | Position quantity after the trade  
»» avg_entry_price | string | Optional | none | Average entry price  
»» value | string | Optional | none | Trade value in the instrument trading currency  
»» fx_rate | string | Optional | none | Quote currency to USD exchange rate  
»» fee | string | Optional | none | Fee in the instrument trading currency  
» timestamp | integer(int64) | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
side | 1  
side | 2  
role | maker  
role | taker  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotClosePositionRequest

_Close position request parameters_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Symbol  
close_volume | string | Optional | none | Close quantity; required for partial close  
close_type | integer | Required | none | Close type (1=partial close, 2=close all)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
close_type | 1  
close_type | 2  
      
    
    {
      "symbol": "AAPL",
      "close_volume": "2",
      "close_type": 1
    }
    
    

##  BalanceRecordList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» total | integer(int64) | Optional | none | Total quantity  
» total_page | integer(int64) | Optional | none | Total pages  
» list | array | Optional | none | Balance record details  
»» id | integer(int64) | Optional | none | Balance record primary key ID  
»» user_id | integer | Optional | none | User ID  
»» change | string | Optional | none | Cash amount change. Positive values are credits; negative values are debits.  
»» balance | string | Optional | none | Cash balance snapshot after the change  
»» stock_change | string | Optional | none | Stock quantity change, parsed from detail.amount for stock quantity records; may be an empty string for other records  
»» type | string | Optional | none | Raw record type. Common values include:  
\- deposit: Funds transferred in.  
\- withdraw: Funds transferred out.  
\- fee: Trading fee.  
\- dividend: Dividend payment.  
\- sell: Proceeds from selling stocks.  
\- buy: Payment for buying stocks.  
\- award: Airdrop reward.  
\- stock_transfer_in: Stocks transferred in.  
\- stock_transfer_out: Stocks transferred out.  
»» business | string | Optional | none | Business identifier  
»» business_id | integer(int64) | Optional | none | Related business ID  
»» symbol | string | Optional | none | Symbol  
»» detail | string | Optional | none | Raw business details as a JSON string; returned only when include_detail=true is requested  
»» version | integer | Optional | none | Record version  
»» time_create | integer(int64) | Optional | none | Business event time (Unix timestamp in seconds)  
»» create_time | integer(int64) | Optional | none | Record creation time (Unix timestamp in seconds)  
» timestamp | integer(int64) | Optional | none | none  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotOrderBook

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» symbol | string | Optional | none | Symbol  
» bids | array | Optional | none | Bid orders  
»» p | string | Optional | none | Price  
»» user_order | boolean | Optional | none | Whether it is the user's own order  
» asks | [TradfiSpotOrderBook/properties/data/properties/bids/items] | Optional | none | Ask orders  
timestamp | integer(int64) | Optional | none | none  
      
    
    {
      "data": {
        "symbol": "AAPL",
        "bids": [
          {}
        ],
        "asks": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotTransactionRequest

_Fund transfer request parameters. Transfer in means moving funds from the spot account to the stock account; transfer out means moving funds from the stock account to the spot account._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
asset | string | Required | none | Asset, USDT only  
change | string | Required | none | Change amount, must be greater than 0  
type | string | Required | none | Transaction type. deposit transfers funds from the spot account to the stock account; withdraw transfers funds from the stock account to the spot account.  
ref_id | string | Required | none | Business idempotent ID  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
asset | USDT  
type | deposit  
type | withdraw  
      
    
    {
      "asset": "USDT",
      "change": "100",
      "type": "deposit",
      "ref_id": "transfer-202607070001"
    }
    
    

##  TradfiSpotOrderHistoryList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
data | object | Optional | none | none  
» total | integer(int64) | Optional | none | Total quantity  
» total_page | integer | Optional | none | Total pages  
» list | array | Optional | none | Query historical order list  
»» order_id | string | Optional | none | Order ID  
»» symbol | string | Optional | none | Symbol  
»» exchange | string | Optional | none | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
»» quote_currency | string | Optional | none | Quote currency  
»» fx_rate | string | Optional | none | Quote currency to USD exchange rate  
»» symbol_desc | string | Optional | none | Symbol description  
»» price_type | string | Optional | none | Price type (market = market order, limit = limit order)  
»» status | integer | Optional | none | Order status.  
\- 0: Unknown.  
\- 1: New order; the order has been validated and is waiting to be processed.  
\- 2: Partially filled.  
\- 3: Filled.  
\- 4: Canceled.  
\- 5: Order rejected.  
\- 6: Cancellation rejected.  
\- 7: Order update succeeded.  
\- 8: Order update rejected.  
»» status_desc | string | Optional | none | Order status description  
»» status_detail | object|null | Optional | none | Order status details  
»»» title | string | Optional | none | Status title  
»»» message | string | Optional | none | Status message  
»» finish_as | integer | Optional | none | Order completion reason.  
\- 0: Unknown.  
\- 1: No quote found.  
\- 2: No match found.  
\- 3: Trigger price exceeded.  
\- 4: Order value exceeds the limit.  
\- 5: Unknown rejection.  
\- 6: Unknown cancellation.  
\- 7: Canceled by user.  
\- 8: Canceled after the order time in force expired.  
\- 9: Trading is not supported in the current session.  
\- 13: Canceled due to corporate action.  
»» side | integer | Optional | none | Side (1=sell, 2=buy)  
»» time_in_force | string | Optional | none | Time in force.  
\- day: Day order.  
»» volume | string | Optional | none | Order quantity  
»» fill_volume | string | Optional | none | Trading size  
»» price | string | Optional | none | Order price  
»» avg_fill_price | string|null | Optional | none | Average fill price  
»» commission | string | Optional | none | fee  
»» time_setup | integer(int64) | Optional | none | Order creation time (Unix timestamp, seconds)  
»» time_done | integer(int64) | Optional | none | Order completion time (Unix timestamp in seconds)  
» timestamp | integer(int64) | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
price_type | market  
price_type | limit  
status | 0  
status | 1  
status | 2  
status | 3  
status | 4  
status | 5  
status | 6  
status | 7  
status | 8  
finish_as | 0  
finish_as | 1  
finish_as | 2  
finish_as | 3  
finish_as | 4  
finish_as | 5  
finish_as | 6  
finish_as | 7  
finish_as | 8  
finish_as | 9  
finish_as | 13  
side | 1  
side | 2  
time_in_force | day  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }