---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/stock
api_type: REST
updated_at: 2026-11-28 18:55:38.176466
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

Type | Constraints  
---|---  
TradfiSpotUserAssetResp |   
  
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
equity | string | Optional |  | Account equity  
balance | string | Optional |  | Account Balance  
available | string | Optional |  | Available Balance  
loan_amount | string | Optional |  | Loan amount. Non-negative: the absolute value of the original available balance when it is negative, otherwise 0.  
buy_power | string | Optional |  | Buying power  
leverage | string | Optional |  | Leverage  
leave_liquidity | string | Optional |  | Excess liquidity  
leave_liquidity_rate | string | Optional |  | Excess liquidity ratio  
aee | string | Optional |  | Available Excess Equity (AEE)  
options_margin | string | Optional |  | Options margin  
position_market_value | string | Optional |  | Position market value  
position_pnl | string | Optional |  | Position P&L  
today_pnl | string | Optional |  | Today's P&L  
option_position_market_value | string | Optional |  | Option position market value  
option_position_pnl | string | Optional |  | Option position PnL  
option_today_pnl | string | Optional |  | Option today's PnL  
user_exists | boolean | Optional |  | Whether the user has activated the service  
margin_enabled | boolean | Optional |  | Whether margin financing is enabled  
long_borrowing_rate | string | Optional |  | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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
margin_feature | body | boolean | Required | Whether to enable margin financing. true enables it; false disables it.  
  
####  Request Body Schema

Request parameters for enabling or disabling margin financing

Request Body SchemaType | Constraints  
---|---  
TradFiSpotSetMarginFeatureRequest | required: ["margin_feature"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
margin_feature | boolean | Required |  | Whether to enable margin financing. true enables it; false disables it.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | SetMarginFeature  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
SetMarginFeature |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional | additionalProperties: false | Returns empty object on success  
timestamp | integer(int64) | Optional |  |   
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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

Type | Constraints  
---|---  
TradfiSpotSymbols |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  | Symbol list  
  
**data / list**

Symbol list

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
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
exchange_desc | string | Optional |  | Exchange description  
quote_currency | string | Optional |  | Quote currency  
quote_currency_precision | integer | Optional |  | Quote currency precision  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
symbol_desc | string | Optional |  | Symbol description  
category | string | Optional | enum: ["CS","ETF","ADRC","ADR","ETV","PFD","ETS","ETN","FUND"] | Symbol category.  
\- CS: Common stock.  
\- ETF: Exchange-traded funds.  
\- ADRC, ADR: Depositary receipts for foreign companies listed in the U.S.  
\- ETV: Exchange-traded products.  
\- PFD: Preferred stock.  
\- ETS: Exchange-traded securities.  
\- ETN: Exchange-traded notes.  
\- FUND: Funds.  
asset_type | string | Optional | enum: ["STOCK","ETF"] | Asset type.  
\- STOCK: Stock.  
\- ETF: Exchange-traded fund.  
trade_status | string | Optional | enum: ["pre_market","open","post_market"] | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
trade_mode | integer | Optional | enum: [0,1,2,4,5] | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
order_fill_timing | integer | Optional | enum: [1,2,3] | Order fill timing (1=immediate, 2=after pre-market opens, 3=after regular session opens)  
icon_link | string | Optional |  | Icon URL  
quote_currency_symbol | string | Optional |  | Quote currency symbol  
price_precision | integer | Optional |  | Price precision  
volume_precision | integer | Optional |  | Quantity precision  
is_ipo | boolean | Optional |  | Whether it is an IPO symbol  
ipo_price | string | Optional |  | IPO price  
sell_price_protection | string | Optional |  | Sell price protection rate  
buy_price_protection | string | Optional |  | Buy price protection rate  
symbol_descs | array | Optional |  | Multilingual symbol description  
margin_mode | integer | Optional | enum: [0,1,2,3] | Margin trading mode.  
\- 0: Neither margin financing nor securities borrowing is supported.  
\- 1: Margin financing is supported.  
\- 2: Securities borrowing is supported.  
\- 3: Both margin financing and securities borrowing are supported.  
long_im | string | Optional |  | Initial margin ratio for long positions  
long_mm | string | Optional |  | Maintenance margin ratio for long positions  
short_im | string | Optional |  | Initial margin ratio for short positions  
short_mm | string | Optional |  | Maintenance margin ratio for short positions  
long_borrowing_rate | string | Optional |  | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
short_borrowing_rate | string | Optional |  | Annual securities borrowing interest rate. An empty string indicates that no valid rate is currently available.  
  
**data / list / items / symbol_descs**

Multilingual symbol description

Type | Constraints  
---|---  
array |   
  
**data / list / items / symbol_descs / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
lang | string | Optional |  | Language  
value | string | Optional |  | Localized description  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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

Type | Constraints  
---|---  
SymbolDetail |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  |   
  
**data / list**

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
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
exchange_desc | string | Optional |  | Exchange description  
quote_currency | string | Optional |  | Quote currency  
quote_currency_precision | integer | Optional |  | Quote currency precision  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
symbol_desc | string | Optional |  | Symbol description  
category | string | Optional | enum: ["CS","ETF","ADRC","ADR","ETV","PFD","ETS","ETN","FUND"] | Symbol category.  
\- CS: Common stock.  
\- ETF: Exchange-traded funds.  
\- ADRC, ADR: Depositary receipts for foreign companies listed in the U.S.  
\- ETV: Exchange-traded products.  
\- PFD: Preferred stock.  
\- ETS: Exchange-traded securities.  
\- ETN: Exchange-traded notes.  
\- FUND: Funds.  
asset_type | string | Optional | enum: ["STOCK","ETF"] | Asset type.  
\- STOCK: Stock.  
\- ETF: Exchange-traded fund.  
settlement_currency | string | Optional |  | Settlement currency  
max_order_volume | string | Optional |  | Maximum order quantity  
step_order_volume | string | Optional |  | Order step size  
min_order_volume | string | Optional |  | Minimum order quantity  
price_precision | integer | Optional |  | Price precision  
volume_precision | integer | Optional |  | Quantity precision  
is_ipo | boolean | Optional |  | Whether it is an IPO symbol  
ipo_price | string | Optional |  | IPO price  
price_protection | string | Optional |  | Price protection range  
sell_price_protection | string | Optional |  | Sell price protection rate  
buy_price_protection | string | Optional |  | Buy price protection rate  
slippage_rate | string | Optional |  | Slippage  
commission_rate | string | Optional |  | Fee Rate  
trade_status | string | Optional | enum: ["pre_market","open","post_market"] | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
trade_mode | integer | Optional | enum: [0,1,2,4,5] | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
order_fill_timing | integer | Optional | enum: [1,2,3] | Order fill timing (1=immediate, 2=after pre-market opens, 3=after regular session opens)  
symbol_descs | array | Optional |  | Multilingual symbol description  
icon_link | string | Optional |  | Icon URL  
margin_mode | integer | Optional | enum: [0,1,2,3] | Margin trading mode.  
\- 0: Neither margin financing nor securities borrowing is supported.  
\- 1: Margin financing is supported.  
\- 2: Securities borrowing is supported.  
\- 3: Both margin financing and securities borrowing are supported.  
long_im | string | Optional |  | Initial margin ratio for long positions  
long_mm | string | Optional |  | Maintenance margin ratio for long positions  
short_im | string | Optional |  | Initial margin ratio for short positions  
short_mm | string | Optional |  | Maintenance margin ratio for short positions  
long_borrowing_rate | string | Optional |  | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
short_borrowing_rate | string | Optional |  | Annual securities borrowing interest rate. An empty string indicates that no valid rate is currently available.  
  
**data / list / items / symbol_descs**

Multilingual symbol description

Type | Constraints  
---|---  
array |   
  
**data / list / items / symbol_descs / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
lang | string | Optional |  | Language  
value | string | Optional |  | Localized description  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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

Type | Constraints  
---|---  
TradfiSpotOrderBook |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Symbol  
bids | array | Optional |  | Bid orders  
asks | array | Optional |  | Ask orders  
  
**data / bids**

Bid orders

Type | Constraints  
---|---  
array |   
  
**data / bids / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
p | string | Optional |  | Price  
user_order | boolean | Optional |  | Whether it is the user's own order  
  
**data / asks**

Ask orders

Type | Constraints  
---|---  
array |   
  
**data / asks / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
p | string | Optional |  | Price  
user_order | boolean | Optional |  | Whether it is the user's own order  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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

Type | Constraints  
---|---  
TradfiSpotOrderList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Query active order list  
  
**data / list**

Query active order list

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
order_id | string | Optional |  | Order ID  
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
quote_currency | string | Optional |  | Quote currency  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
symbol_desc | string | Optional |  | Symbol description  
trade_status | string | Optional | enum: ["pre_market","open","post_market"] | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
trade_mode | integer | Optional | enum: [0,1,2,4,5] | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
price_type | string | Optional | enum: ["market","limit"] | Price type (market = market order, limit = limit order)  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
status | integer | Optional | enum: [0,1,2,3,4,5,6,7,8] | Order status.  
\- 0: Unknown.  
\- 1: New order; the order has been validated and is waiting to be processed.  
\- 2: Partially filled.  
\- 3: Filled.  
\- 4: Canceled.  
\- 5: Order rejected.  
\- 6: Cancellation rejected.  
\- 7: Order update succeeded.  
\- 8: Order update rejected.  
volume | string | Optional |  | Order quantity  
fill_volume | string | Optional |  | Trading size  
price | string | Optional |  | Order price  
time_setup | integer(int64) | Optional |  | Order creation time (Unix timestamp, seconds)  
time_update | integer(int64) | Optional |  | Order update time (Unix timestamp, seconds)  
max_order_volume | string | Optional |  | Maximum order quantity  
step_order_volume | string | Optional |  | Order step size  
min_order_volume | string | Optional |  | Minimum order quantity  
price_precision | integer | Optional |  | Price precision  
price_protection | string | Optional |  | Price protection range  
sell_price_protection | string | Optional |  | Sell price protection rate  
buy_price_protection | string | Optional |  | Buy price protection rate  
commission_rate | string | Optional |  | Fee Rate  
slippage_rate | string | Optional |  | Slippage  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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
volume | body | string | Required | Order quantity  
symbol | body | string | Required | Symbol  
side | body | integer | Required | Side (1=sell, 2=buy)  
price_type | body | string | Required | Price type (market = market order, limit = limit order)  
trading_session | body | string | Required | Trading session.  
Limit orders support only all, while market orders support only regular.  
time_in_force | body | string | Required | Time in force.  
\- day: Day order.  
price | body | string | Optional | Order price, used for limit orders  
client_order_id | body | string | Optional | Client-defined order ID  
  
####  Detailed descriptions

** trading_session**: Trading session.  
Limit orders support only all, while market orders support only regular.

** time_in_force**: Time in force.  
\- day: Day order.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | 1  
side | 2  
price_type | market  
price_type | limit  
trading_session | regular  
trading_session | all  
time_in_force | day  
  
####  Request Body Schema

Place order request parameters

Request Body SchemaType | Constraints  
---|---  
TradFiSpotOrderRequest | required: ["volume","symbol","side","price_type","trading_session","time_in_force"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
volume | string | Required |  | Order quantity  
symbol | string | Required |  | Symbol  
side | integer | Required | enum: [1,2] | Side (1=sell, 2=buy)  
price_type | string | Required | enum: ["market","limit"] | Price type (market = market order, limit = limit order)  
trading_session | string | Required | enum: ["regular","all"] | Trading session.  
Limit orders support only all, while market orders support only regular.  
time_in_force | string | Required | enum: ["day"] | Time in force.  
\- day: Day order.  
price | string | Optional |  | Order price, used for limit orders  
client_order_id | string | Optional |  | Client-defined order ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order placed successfully | TradfiSpotCreateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
TradfiSpotCreateOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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

Type | Constraints  
---|---  
DeleteOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional | additionalProperties: false | Returns empty object on success  
timestamp | integer(int64) | Optional |  |   
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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

Type | Constraints  
---|---  
TradfiSpotOrderHistoryList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  | Query historical order list  
  
**data / list**

Query historical order list

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
order_id | string | Optional |  | Order ID  
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
quote_currency | string | Optional |  | Quote currency  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
symbol_desc | string | Optional |  | Symbol description  
price_type | string | Optional | enum: ["market","limit"] | Price type (market = market order, limit = limit order)  
status | integer | Optional | enum: [0,1,2,3,4,5,6,7,8] | Order status.  
\- 0: Unknown.  
\- 1: New order; the order has been validated and is waiting to be processed.  
\- 2: Partially filled.  
\- 3: Filled.  
\- 4: Canceled.  
\- 5: Order rejected.  
\- 6: Cancellation rejected.  
\- 7: Order update succeeded.  
\- 8: Order update rejected.  
status_desc | string | Optional |  | Order status description  
status_detail | object|null | Optional | nullable: true | Order status details  
finish_as | integer | Optional | enum: [0,1,2,3,4,5,6,7,8,9,13] | Order completion reason.  
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
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
time_in_force | string | Optional | enum: ["day"] | Time in force.  
\- day: Day order.  
volume | string | Optional |  | Order quantity  
fill_volume | string | Optional |  | Trading size  
price | string | Optional |  | Order price  
avg_fill_price | string|null | Optional | nullable: true | Average fill price  
commission | string | Optional |  | fee  
time_setup | integer(int64) | Optional |  | Order creation time (Unix timestamp, seconds)  
time_done | integer(int64) | Optional |  | Order completion time (Unix timestamp in seconds)  
  
**data / list / items / status_detail**

Order status details

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
title | string | Optional |  | Status title  
message | string | Optional |  | Status message  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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

Type | Constraints  
---|---  
OrderDealList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer(int64) | Optional |  | Total pages  
list | array | Optional |  | Trade records  
  
**data / list**

Trade records

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
id | integer(int64) | Optional |  | Trade record primary key ID  
deal_id | integer(int64) | Optional |  | Trade ID  
order_id | integer(int64) | Optional |  | Order ID  
client_order_id | string | Optional |  | Client-defined order ID  
user_id | integer | Optional |  | User ID  
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
role | string | Optional | enum: ["maker","taker"] | Liquidity role.  
\- maker: Maker.  
\- taker: Taker.  
price | string | Optional |  | Trade price in the instrument trading currency  
quantity | string | Optional |  | Trading size  
position_qty | string | Optional |  | Position quantity after the trade  
avg_entry_price | string | Optional |  | Average entry price  
value | string | Optional |  | Trade value in the instrument trading currency  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
fee | string | Optional |  | Fee in the instrument trading currency  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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
volume | body | string | Required | Modified order quantity  
price | body | string | Required | Modified order price  
order_id | path | integer(int64) | Required | Order ID  
  
####  Request Body Schema

Modify order request parameters

Request Body SchemaType | Constraints  
---|---  
TradFiSpotOrderUpdateRequest | required: ["volume","price"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
volume | string | Required |  | Modified order quantity  
price | string | Required |  | Modified order price  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotUpdateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
TradfiSpotUpdateOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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

Type | Constraints  
---|---  
DeleteOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional | additionalProperties: false | Returns empty object on success  
timestamp | integer(int64) | Optional |  |   
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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

Type | Constraints  
---|---  
TradfiSpotPositionList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Query active position list  
  
**data / list**

Query active position list

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
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
quote_currency | string | Optional |  | Quote currency  
quote_currency_precision | integer | Optional |  | Quote currency precision  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
trade_status | string | Optional | enum: ["pre_market","open","post_market"] | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
symbol_desc | string | Optional |  | Symbol description  
position_pnl | string | Optional |  | Position P&L  
today_pnl | string | Optional |  | Today's P&L  
pnl_rate | string | Optional |  | Yield  
today_sell_amount | string | Optional |  | Today's sales amount  
today_buy_amount | string | Optional |  | Today's purchase amount  
today_sell_volume | string | Optional |  | Today's sell volume  
today_buy_volume | string | Optional |  | Today's buy volume  
yesterday_volume | string | Optional |  | Previous close position quantity  
volume | string | Optional |  | Position quantity  
available | string | Optional |  | Available position quantity  
transfer_out_pending_qty | string | Optional |  | Stock transfer in progress quantity  
avg_cost_price | string | Optional |  | Cost price  
diluted_cost_price | string | Optional |  | Diluted cost price  
last_price | string | Optional |  | Latest price  
extended_last_price | string|null | Optional | nullable: true | Extended hours latest price  
max_order_volume | string | Optional |  | Maximum order quantity  
step_order_volume | string | Optional |  | Order step size  
min_order_volume | string | Optional |  | Minimum order quantity  
price_precision | integer | Optional |  | Price precision  
price_protection | string | Optional |  | Price protection range  
sell_price_protection | string | Optional |  | Sell price protection rate  
buy_price_protection | string | Optional |  | Buy price protection rate  
commission_rate | string | Optional |  | Fee Rate  
slippage_rate | string | Optional |  | Slippage  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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
symbol | body | string | Required | Symbol  
close_volume | body | string | Optional | Close quantity; required for partial close  
close_type | body | integer | Required | Close type (1=partial close, 2=close all)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
close_type | 1  
close_type | 2  
  
####  Request Body Schema

Close position request parameters

Request Body SchemaType | Constraints  
---|---  
TradFiSpotClosePositionRequest | required: ["symbol","close_type"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Symbol  
close_volume | string | Optional |  | Close quantity; required for partial close  
close_type | integer | Required | enum: [1,2] | Close type (1=partial close, 2=close all)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | ClosePosition  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
ClosePosition |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Close order ID  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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

Type | Constraints  
---|---  
TradfiSpotTransactionList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  |   
total_page | integer(int64) | Optional |  |   
list | array | Optional |  | Transaction record list  
  
**data / list**

Transaction record list

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
asset | string | Optional |  | Asset  
symbol | string | Optional |  | Symbol  
symbol_display | string | Optional |  | Symbol display name  
type | string | Optional | enum: ["deposit","withdraw","fee","dividend","sell","buy","award","stock_transfer_in","stock_transfer_out"] | Transaction type.  
\- deposit: Funds transfer in.  
\- withdraw: Funds transfer out.  
\- fee: Trading fee.  
\- dividend: Dividend payout.  
\- sell: Stock sale credit.  
\- buy: Stock purchase debit.  
\- award: Airdrop reward.  
\- stock_transfer_in: Stock transfer in.  
\- stock_transfer_out: Stock transfer out.  
type_desc | string | Optional |  | Transaction type description  
change | string | Optional |  | Change amount. A positive value means a credit, and a negative value means a debit.  
balance | string | Optional |  | Balance after change  
ref_id | string | Optional |  | Business idempotent ID  
time | integer(int64) | Optional |  | Unix timestamp (seconds)  
unit_text | string | Optional |  | Unit display text  
detail | object | Optional | additionalProperties: true | Business details  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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
asset | body | string | Required | Asset, USDT only  
change | body | string | Required | Change amount, must be greater than 0  
type | body | string | Required | Transaction type. deposit transfers funds from the spot account to the stock account; withdraw transfers funds from the stock account to the spot account.  
ref_id | body | string | Required | Business idempotent ID  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
asset | USDT  
type | deposit  
type | withdraw  
  
####  Request Body Schema

Fund transfer request parameters. Transfer in means moving funds from the spot account to the stock account; transfer out means moving funds from the stock account to the spot account.

Request Body SchemaType | Constraints  
---|---  
TradFiSpotTransactionRequest | required: ["asset","change","type","ref_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required | enum: ["USDT"] | Asset, USDT only  
change | string | Required |  | Change amount, must be greater than 0  
type | string | Required | enum: ["deposit","withdraw"] | Transaction type. deposit transfers funds from the spot account to the stock account; withdraw transfers funds from the stock account to the spot account.  
ref_id | string | Required |  | Business idempotent ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request success | TradfiSpotCreateTransaction  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Request failed | TradFiSpotError  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
TradfiSpotCreateTransaction |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional | additionalProperties: false | Returns empty object on success  
timestamp | integer(int64) | Optional |  |   
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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

Type | Constraints  
---|---  
BalanceRecordList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer(int64) | Optional |  | Total pages  
list | array | Optional |  | Balance record details  
  
**data / list**

Balance record details

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
id | integer(int64) | Optional |  | Balance record primary key ID  
user_id | integer | Optional |  | User ID  
change | string | Optional |  | Cash amount change. Positive values are credits; negative values are debits.  
balance | string | Optional |  | Cash balance snapshot after the change  
stock_change | string | Optional |  | Stock quantity change, parsed from detail.amount for stock quantity records; may be an empty string for other records  
type | string | Optional |  | Raw record type. Common values include:  
\- deposit: Funds transferred in.  
\- withdraw: Funds transferred out.  
\- fee: Trading fee.  
\- dividend: Dividend payment.  
\- sell: Proceeds from selling stocks.  
\- buy: Payment for buying stocks.  
\- award: Airdrop reward.  
\- stock_transfer_in: Stocks transferred in.  
\- stock_transfer_out: Stocks transferred out.  
business | string | Optional |  | Business identifier  
business_id | integer(int64) | Optional |  | Related business ID  
symbol | string | Optional |  | Symbol  
detail | string | Optional |  | Raw business details as a JSON string; returned only when include_detail=true is requested  
version | integer | Optional |  | Record version  
time_create | integer(int64) | Optional |  | Business event time (Unix timestamp in seconds)  
create_time | integer(int64) | Optional |  | Record creation time (Unix timestamp in seconds)  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
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

Type | Constraints  
---|---  
Exchanges |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

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

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Trading market.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
exchange_desc | string | Optional |  | Market display name  
icon_link | string | Optional |  | Market icon  
support_transfer | boolean | Optional |  | Whether stock transfer is supported  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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

Type | Constraints  
---|---  
FeeRate |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

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

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
vip_level | integer | Optional |  | VIP level  
maker_fee | string | Optional |  | Maker fee rate for Japanese and Korean stocks  
taker_fee | string | Optional |  | Taker fee rate for Japanese and Korean stocks  
  
Status Code **400**

TradFiSpotError

Type | Constraints  
---|---  
TradFiSpotError |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
  
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

##  BalanceRecordList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer(int64) | Optional |  | Total pages  
list | array | Optional |  | Balance record details  
  
**data / list**

Balance record details

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
id | integer(int64) | Optional |  | Balance record primary key ID  
user_id | integer | Optional |  | User ID  
change | string | Optional |  | Cash amount change. Positive values are credits; negative values are debits.  
balance | string | Optional |  | Cash balance snapshot after the change  
stock_change | string | Optional |  | Stock quantity change, parsed from detail.amount for stock quantity records; may be an empty string for other records  
type | string | Optional |  | Raw record type. Common values include:  
\- deposit: Funds transferred in.  
\- withdraw: Funds transferred out.  
\- fee: Trading fee.  
\- dividend: Dividend payment.  
\- sell: Proceeds from selling stocks.  
\- buy: Payment for buying stocks.  
\- award: Airdrop reward.  
\- stock_transfer_in: Stocks transferred in.  
\- stock_transfer_out: Stocks transferred out.  
business | string | Optional |  | Business identifier  
business_id | integer(int64) | Optional |  | Related business ID  
symbol | string | Optional |  | Symbol  
detail | string | Optional |  | Raw business details as a JSON string; returned only when include_detail=true is requested  
version | integer | Optional |  | Record version  
time_create | integer(int64) | Optional |  | Business event time (Unix timestamp in seconds)  
create_time | integer(int64) | Optional |  | Record creation time (Unix timestamp in seconds)  
      
    
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
    
    

##  TradfiSpotUpdateOrder

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
      
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotOrderHistoryList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  | Query historical order list  
  
**data / list**

Query historical order list

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
order_id | string | Optional |  | Order ID  
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
quote_currency | string | Optional |  | Quote currency  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
symbol_desc | string | Optional |  | Symbol description  
price_type | string | Optional | enum: ["market","limit"] | Price type (market = market order, limit = limit order)  
status | integer | Optional | enum: [0,1,2,3,4,5,6,7,8] | Order status.  
\- 0: Unknown.  
\- 1: New order; the order has been validated and is waiting to be processed.  
\- 2: Partially filled.  
\- 3: Filled.  
\- 4: Canceled.  
\- 5: Order rejected.  
\- 6: Cancellation rejected.  
\- 7: Order update succeeded.  
\- 8: Order update rejected.  
status_desc | string | Optional |  | Order status description  
status_detail | object|null | Optional | nullable: true | Order status details  
finish_as | integer | Optional | enum: [0,1,2,3,4,5,6,7,8,9,13] | Order completion reason.  
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
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
time_in_force | string | Optional | enum: ["day"] | Time in force.  
\- day: Day order.  
volume | string | Optional |  | Order quantity  
fill_volume | string | Optional |  | Trading size  
price | string | Optional |  | Order price  
avg_fill_price | string|null | Optional | nullable: true | Average fill price  
commission | string | Optional |  | fee  
time_setup | integer(int64) | Optional |  | Order creation time (Unix timestamp, seconds)  
time_done | integer(int64) | Optional |  | Order completion time (Unix timestamp in seconds)  
  
**data / list / items / status_detail**

Order status details

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
title | string | Optional |  | Status title  
message | string | Optional |  | Status message  
      
    
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

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  |   
  
**data / list**

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
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
exchange_desc | string | Optional |  | Exchange description  
quote_currency | string | Optional |  | Quote currency  
quote_currency_precision | integer | Optional |  | Quote currency precision  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
symbol_desc | string | Optional |  | Symbol description  
category | string | Optional | enum: ["CS","ETF","ADRC","ADR","ETV","PFD","ETS","ETN","FUND"] | Symbol category.  
\- CS: Common stock.  
\- ETF: Exchange-traded funds.  
\- ADRC, ADR: Depositary receipts for foreign companies listed in the U.S.  
\- ETV: Exchange-traded products.  
\- PFD: Preferred stock.  
\- ETS: Exchange-traded securities.  
\- ETN: Exchange-traded notes.  
\- FUND: Funds.  
asset_type | string | Optional | enum: ["STOCK","ETF"] | Asset type.  
\- STOCK: Stock.  
\- ETF: Exchange-traded fund.  
settlement_currency | string | Optional |  | Settlement currency  
max_order_volume | string | Optional |  | Maximum order quantity  
step_order_volume | string | Optional |  | Order step size  
min_order_volume | string | Optional |  | Minimum order quantity  
price_precision | integer | Optional |  | Price precision  
volume_precision | integer | Optional |  | Quantity precision  
is_ipo | boolean | Optional |  | Whether it is an IPO symbol  
ipo_price | string | Optional |  | IPO price  
price_protection | string | Optional |  | Price protection range  
sell_price_protection | string | Optional |  | Sell price protection rate  
buy_price_protection | string | Optional |  | Buy price protection rate  
slippage_rate | string | Optional |  | Slippage  
commission_rate | string | Optional |  | Fee Rate  
trade_status | string | Optional | enum: ["pre_market","open","post_market"] | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
trade_mode | integer | Optional | enum: [0,1,2,4,5] | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
order_fill_timing | integer | Optional | enum: [1,2,3] | Order fill timing (1=immediate, 2=after pre-market opens, 3=after regular session opens)  
symbol_descs | array | Optional |  | Multilingual symbol description  
icon_link | string | Optional |  | Icon URL  
margin_mode | integer | Optional | enum: [0,1,2,3] | Margin trading mode.  
\- 0: Neither margin financing nor securities borrowing is supported.  
\- 1: Margin financing is supported.  
\- 2: Securities borrowing is supported.  
\- 3: Both margin financing and securities borrowing are supported.  
long_im | string | Optional |  | Initial margin ratio for long positions  
long_mm | string | Optional |  | Maintenance margin ratio for long positions  
short_im | string | Optional |  | Initial margin ratio for short positions  
short_mm | string | Optional |  | Maintenance margin ratio for short positions  
long_borrowing_rate | string | Optional |  | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
short_borrowing_rate | string | Optional |  | Annual securities borrowing interest rate. An empty string indicates that no valid rate is currently available.  
  
**data / list / items / symbol_descs**

Multilingual symbol description

Type | Constraints  
---|---  
array |   
  
**data / list / items / symbol_descs / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
lang | string | Optional |  | Language  
value | string | Optional |  | Localized description  
      
    
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
    
    

##  SetMarginFeature

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional | additionalProperties: false | Returns empty object on success  
timestamp | integer(int64) | Optional |  |   
      
    
    {
      "data": {},
      "timestamp": 0
    }
    
    

##  FeeRate

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

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

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
vip_level | integer | Optional |  | VIP level  
maker_fee | string | Optional |  | Maker fee rate for Japanese and Korean stocks  
taker_fee | string | Optional |  | Taker fee rate for Japanese and Korean stocks  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotOrderUpdateRequest

Modify order request parameters

Type | Constraints  
---|---  
object | required: ["volume","price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
volume | string | Required |  | Modified order quantity  
price | string | Required |  | Modified order price  
      
    
    {
      "volume": "8",
      "price": "201.23"
    }
    
    

##  TradfiSpotPositionList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Query active position list  
  
**data / list**

Query active position list

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
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
quote_currency | string | Optional |  | Quote currency  
quote_currency_precision | integer | Optional |  | Quote currency precision  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
trade_status | string | Optional | enum: ["pre_market","open","post_market"] | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
symbol_desc | string | Optional |  | Symbol description  
position_pnl | string | Optional |  | Position P&L  
today_pnl | string | Optional |  | Today's P&L  
pnl_rate | string | Optional |  | Yield  
today_sell_amount | string | Optional |  | Today's sales amount  
today_buy_amount | string | Optional |  | Today's purchase amount  
today_sell_volume | string | Optional |  | Today's sell volume  
today_buy_volume | string | Optional |  | Today's buy volume  
yesterday_volume | string | Optional |  | Previous close position quantity  
volume | string | Optional |  | Position quantity  
available | string | Optional |  | Available position quantity  
transfer_out_pending_qty | string | Optional |  | Stock transfer in progress quantity  
avg_cost_price | string | Optional |  | Cost price  
diluted_cost_price | string | Optional |  | Diluted cost price  
last_price | string | Optional |  | Latest price  
extended_last_price | string|null | Optional | nullable: true | Extended hours latest price  
max_order_volume | string | Optional |  | Maximum order quantity  
step_order_volume | string | Optional |  | Order step size  
min_order_volume | string | Optional |  | Minimum order quantity  
price_precision | integer | Optional |  | Price precision  
price_protection | string | Optional |  | Price protection range  
sell_price_protection | string | Optional |  | Sell price protection rate  
buy_price_protection | string | Optional |  | Buy price protection rate  
commission_rate | string | Optional |  | Fee Rate  
slippage_rate | string | Optional |  | Slippage  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotOrderRequest

Place order request parameters

Type | Constraints  
---|---  
object | required: ["volume","symbol","side","price_type","trading_session","time_in_force"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
volume | string | Required |  | Order quantity  
symbol | string | Required |  | Symbol  
side | integer | Required | enum: [1,2] | Side (1=sell, 2=buy)  
price_type | string | Required | enum: ["market","limit"] | Price type (market = market order, limit = limit order)  
trading_session | string | Required | enum: ["regular","all"] | Trading session.  
Limit orders support only all, while market orders support only regular.  
time_in_force | string | Required | enum: ["day"] | Time in force.  
\- day: Day order.  
price | string | Optional |  | Order price, used for limit orders  
client_order_id | string | Optional |  | Client-defined order ID  
      
    
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
    
    

##  TradfiSpotOrderList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Query active order list  
  
**data / list**

Query active order list

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
order_id | string | Optional |  | Order ID  
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
quote_currency | string | Optional |  | Quote currency  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
symbol_desc | string | Optional |  | Symbol description  
trade_status | string | Optional | enum: ["pre_market","open","post_market"] | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
trade_mode | integer | Optional | enum: [0,1,2,4,5] | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
price_type | string | Optional | enum: ["market","limit"] | Price type (market = market order, limit = limit order)  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
status | integer | Optional | enum: [0,1,2,3,4,5,6,7,8] | Order status.  
\- 0: Unknown.  
\- 1: New order; the order has been validated and is waiting to be processed.  
\- 2: Partially filled.  
\- 3: Filled.  
\- 4: Canceled.  
\- 5: Order rejected.  
\- 6: Cancellation rejected.  
\- 7: Order update succeeded.  
\- 8: Order update rejected.  
volume | string | Optional |  | Order quantity  
fill_volume | string | Optional |  | Trading size  
price | string | Optional |  | Order price  
time_setup | integer(int64) | Optional |  | Order creation time (Unix timestamp, seconds)  
time_update | integer(int64) | Optional |  | Order update time (Unix timestamp, seconds)  
max_order_volume | string | Optional |  | Maximum order quantity  
step_order_volume | string | Optional |  | Order step size  
min_order_volume | string | Optional |  | Minimum order quantity  
price_precision | integer | Optional |  | Price precision  
price_protection | string | Optional |  | Price protection range  
sell_price_protection | string | Optional |  | Sell price protection rate  
buy_price_protection | string | Optional |  | Buy price protection rate  
commission_rate | string | Optional |  | Fee Rate  
slippage_rate | string | Optional |  | Slippage  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  OrderDealList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer(int64) | Optional |  | Total pages  
list | array | Optional |  | Trade records  
  
**data / list**

Trade records

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
id | integer(int64) | Optional |  | Trade record primary key ID  
deal_id | integer(int64) | Optional |  | Trade ID  
order_id | integer(int64) | Optional |  | Order ID  
client_order_id | string | Optional |  | Client-defined order ID  
user_id | integer | Optional |  | User ID  
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
side | integer | Optional | enum: [1,2] | Side (1=sell, 2=buy)  
role | string | Optional | enum: ["maker","taker"] | Liquidity role.  
\- maker: Maker.  
\- taker: Taker.  
price | string | Optional |  | Trade price in the instrument trading currency  
quantity | string | Optional |  | Trading size  
position_qty | string | Optional |  | Position quantity after the trade  
avg_entry_price | string | Optional |  | Average entry price  
value | string | Optional |  | Trade value in the instrument trading currency  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
fee | string | Optional |  | Fee in the instrument trading currency  
      
    
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

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Close order ID  
      
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotError

TradFiSpotError

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
label | string | Optional |  | Business error label  
message | string | Optional |  | Error message  
data | object|null | Optional | nullable: true | Error additional data  
timestamp | integer(int64) | Optional |  | Server timestamp (milliseconds)  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": {},
      "timestamp": 1783411200000
    }
    
    

##  TradFiSpotClosePositionRequest

Close position request parameters

Type | Constraints  
---|---  
object | required: ["symbol","close_type"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Symbol  
close_volume | string | Optional |  | Close quantity; required for partial close  
close_type | integer | Required | enum: [1,2] | Close type (1=partial close, 2=close all)  
      
    
    {
      "symbol": "AAPL",
      "close_volume": "2",
      "close_type": 1
    }
    
    

##  TradFiSpotTransactionRequest

Fund transfer request parameters. Transfer in means moving funds from the spot account to the stock account; transfer out means moving funds from the stock account to the spot account.

Type | Constraints  
---|---  
object | required: ["asset","change","type","ref_id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required | enum: ["USDT"] | Asset, USDT only  
change | string | Required |  | Change amount, must be greater than 0  
type | string | Required | enum: ["deposit","withdraw"] | Transaction type. deposit transfers funds from the spot account to the stock account; withdraw transfers funds from the stock account to the spot account.  
ref_id | string | Required |  | Business idempotent ID  
      
    
    {
      "asset": "USDT",
      "change": "100",
      "type": "deposit",
      "ref_id": "transfer-202607070001"
    }
    
    

##  Exchanges

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

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

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Trading market.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
exchange_desc | string | Optional |  | Market display name  
icon_link | string | Optional |  | Market icon  
support_transfer | boolean | Optional |  | Whether stock transfer is supported  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotSymbols

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total quantity  
total_page | integer | Optional |  | Total pages  
list | array | Optional |  | Symbol list  
  
**data / list**

Symbol list

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
symbol | string | Optional |  | Symbol  
exchange | string | Optional | enum: ["us","hk","kr","jp"] | Exchange.  
\- us: US stocks.  
\- hk: Hong Kong stocks.  
\- kr: Korean stocks.  
\- jp: Japanese stocks.  
exchange_desc | string | Optional |  | Exchange description  
quote_currency | string | Optional |  | Quote currency  
quote_currency_precision | integer | Optional |  | Quote currency precision  
fx_rate | string | Optional |  | Quote currency to USD exchange rate  
symbol_desc | string | Optional |  | Symbol description  
category | string | Optional | enum: ["CS","ETF","ADRC","ADR","ETV","PFD","ETS","ETN","FUND"] | Symbol category.  
\- CS: Common stock.  
\- ETF: Exchange-traded funds.  
\- ADRC, ADR: Depositary receipts for foreign companies listed in the U.S.  
\- ETV: Exchange-traded products.  
\- PFD: Preferred stock.  
\- ETS: Exchange-traded securities.  
\- ETN: Exchange-traded notes.  
\- FUND: Funds.  
asset_type | string | Optional | enum: ["STOCK","ETF"] | Asset type.  
\- STOCK: Stock.  
\- ETF: Exchange-traded fund.  
trade_status | string | Optional | enum: ["pre_market","open","post_market"] | Trading status.  
\- pre_market: Pre-market.  
\- open: Regular trading session.  
\- post_market: Post-market.  
trade_mode | integer | Optional | enum: [0,1,2,4,5] | Current session trading mode.  
\- 0: Trading disabled.  
\- 1: Buy only.  
\- 2: Sell only.  
\- 4: Buy and sell supported.  
\- 5: Trading suspended.  
order_fill_timing | integer | Optional | enum: [1,2,3] | Order fill timing (1=immediate, 2=after pre-market opens, 3=after regular session opens)  
icon_link | string | Optional |  | Icon URL  
quote_currency_symbol | string | Optional |  | Quote currency symbol  
price_precision | integer | Optional |  | Price precision  
volume_precision | integer | Optional |  | Quantity precision  
is_ipo | boolean | Optional |  | Whether it is an IPO symbol  
ipo_price | string | Optional |  | IPO price  
sell_price_protection | string | Optional |  | Sell price protection rate  
buy_price_protection | string | Optional |  | Buy price protection rate  
symbol_descs | array | Optional |  | Multilingual symbol description  
margin_mode | integer | Optional | enum: [0,1,2,3] | Margin trading mode.  
\- 0: Neither margin financing nor securities borrowing is supported.  
\- 1: Margin financing is supported.  
\- 2: Securities borrowing is supported.  
\- 3: Both margin financing and securities borrowing are supported.  
long_im | string | Optional |  | Initial margin ratio for long positions  
long_mm | string | Optional |  | Maintenance margin ratio for long positions  
short_im | string | Optional |  | Initial margin ratio for short positions  
short_mm | string | Optional |  | Maintenance margin ratio for short positions  
long_borrowing_rate | string | Optional |  | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
short_borrowing_rate | string | Optional |  | Annual securities borrowing interest rate. An empty string indicates that no valid rate is currently available.  
  
**data / list / items / symbol_descs**

Multilingual symbol description

Type | Constraints  
---|---  
array |   
  
**data / list / items / symbol_descs / items**

Type | Constraints  
---|---  
object |   
      
    
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

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  | Symbol  
bids | array | Optional |  | Bid orders  
asks | array | Optional |  | Ask orders  
  
**data / bids**

Bid orders

Type | Constraints  
---|---  
array |   
  
**data / bids / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
p | string | Optional |  | Price  
user_order | boolean | Optional |  | Whether it is the user's own order  
  
**data / asks**

Ask orders

Type | Constraints  
---|---  
array |   
  
**data / asks / items**

Type | Constraints  
---|---  
object |   
      
    
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
    
    

##  TradfiSpotTransactionList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  |   
total_page | integer(int64) | Optional |  |   
list | array | Optional |  | Transaction record list  
  
**data / list**

Transaction record list

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
asset | string | Optional |  | Asset  
symbol | string | Optional |  | Symbol  
symbol_display | string | Optional |  | Symbol display name  
type | string | Optional | enum: ["deposit","withdraw","fee","dividend","sell","buy","award","stock_transfer_in","stock_transfer_out"] | Transaction type.  
\- deposit: Funds transfer in.  
\- withdraw: Funds transfer out.  
\- fee: Trading fee.  
\- dividend: Dividend payout.  
\- sell: Stock sale credit.  
\- buy: Stock purchase debit.  
\- award: Airdrop reward.  
\- stock_transfer_in: Stock transfer in.  
\- stock_transfer_out: Stock transfer out.  
type_desc | string | Optional |  | Transaction type description  
change | string | Optional |  | Change amount. A positive value means a credit, and a negative value means a debit.  
balance | string | Optional |  | Balance after change  
ref_id | string | Optional |  | Business idempotent ID  
time | integer(int64) | Optional |  | Unix timestamp (seconds)  
unit_text | string | Optional |  | Unit display text  
detail | object | Optional | additionalProperties: true | Business details  
      
    
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
    
    

##  TradfiSpotCreateOrder

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID  
      
    
    {
      "data": {
        "id": "123456"
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotSetMarginFeatureRequest

Request parameters for enabling or disabling margin financing

Type | Constraints  
---|---  
object | required: ["margin_feature"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
margin_feature | boolean | Required |  | Whether to enable margin financing. true enables it; false disables it.  
      
    
    {
      "margin_feature": true
    }
    
    

##  DeleteOrder

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional | additionalProperties: false | Returns empty object on success  
timestamp | integer(int64) | Optional |  |   
      
    
    {
      "data": {},
      "timestamp": 0
    }
    
    

##  TradfiSpotCreateTransaction

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Optional | additionalProperties: false | Returns empty object on success  
timestamp | integer(int64) | Optional |  |   
      
    
    {
      "data": {},
      "timestamp": 0
    }
    
    

##  TradfiSpotUserAssetResp

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
equity | string | Optional |  | Account equity  
balance | string | Optional |  | Account Balance  
available | string | Optional |  | Available Balance  
loan_amount | string | Optional |  | Loan amount. Non-negative: the absolute value of the original available balance when it is negative, otherwise 0.  
buy_power | string | Optional |  | Buying power  
leverage | string | Optional |  | Leverage  
leave_liquidity | string | Optional |  | Excess liquidity  
leave_liquidity_rate | string | Optional |  | Excess liquidity ratio  
aee | string | Optional |  | Available Excess Equity (AEE)  
options_margin | string | Optional |  | Options margin  
position_market_value | string | Optional |  | Position market value  
position_pnl | string | Optional |  | Position P&L  
today_pnl | string | Optional |  | Today's P&L  
option_position_market_value | string | Optional |  | Option position market value  
option_position_pnl | string | Optional |  | Option position PnL  
option_today_pnl | string | Optional |  | Option today's PnL  
user_exists | boolean | Optional |  | Whether the user has activated the service  
margin_enabled | boolean | Optional |  | Whether margin financing is enabled  
long_borrowing_rate | string | Optional |  | Annual margin financing interest rate. An empty string indicates that no valid rate is currently available.  
      
    
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