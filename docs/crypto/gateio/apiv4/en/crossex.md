---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/crossex
api_type: Trading
updated_at: 2026-11-19 19:00:38.093138
---

# CrossEx

CrossEx is a cross-exchange trading platform that allows users to trade on multiple exchanges (Binance, OKX, Gate, Bybit, Kraken, Hyperliquid, Deribit, and Lighter) through a unified account, with access to stocks in US, Hong Kong, South Korean, and Japanese markets. The CrossEx API provides account management, asset transfers, order placement, and position management across exchanges.

  * Stocks and ETFs support only cross-exchange account mode. Stock markets use US, HK, KR, and JP as exchange_type, and STOCK or ETF as business_type
  * REST API BaseURL for live trading: `https://api.gateio.ws/api/v4`
  * [Help Center ](https://www.gate.com/help/crossex/functional)
  * [Cross-exchange Trading ](https://www.gate.com/crossex)

##  Query symbol information

GET`/crossex/rule/symbols`

GET `/crossex/rule/symbols`

_Query symbol information_

List trading pair information. Stock and ETF symbols use `{market}_{business_type}_{security_code}_USDT`, for example `US_STOCK_AAPL_USDT`, `HK_STOCK_00700_USDT`, or `US_ETF_SPY_USDT`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Optional | Comma-separated list of trading pairs  
Example:  
BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT,US_STOCK_AAPL_USDT  
  
####  Detailed descriptions

**symbols** : Comma-separated list of trading pairs  
Example:  
BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT,US_STOCK_AAPL_USDT

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Symbol]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
Symbol | required: ["symbol","exchange_type","business_type","state","min_size","min_notional","lot_size","tick_size","max_num_orders","max_market_size","max_limit_size","contract_size","liquidation_fee","delist_time","tag"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Unique trading pair identifier in the format ExchangeType_BusinessType_Base_Counter.  
Stocks and ETFs use the market as ExchangeType (US/HK/KR/JP) and STOCK or ETF as the business type, for example US_STOCK_AAPL_USDT, HK_STOCK_00700_USDT, or US_ETF_SPY_USDT.  
exchange_type | string | Required |  | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
business_type | string | Required |  | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / STOCK: stocks / ETF: exchange-traded funds)  
state | string | Required |  | Status (`live` running / `suspend` paused).  
min_size | string | Required |  | Minimum order quantity  
min_notional | string | Required |  | Minimum Order Value  
lot_size | string | Required |  | Quantity Step  
tick_size | string | Required |  | Price Step  
max_num_orders | string | Required |  | maximumopen orderamount  
max_market_size | string | Required |  | Maximum Market Order Quantity  
max_limit_size | string | Required |  | Maximum order quantity for limit orders.  
contract_size | string | Required |  | Contract multiplier (deprecated; quantity is used uniformly)  
liquidation_fee | string | Required |  | Liquidation Fee Rate  
delist_time | string | Required |  | Millisecond timestamp; `0` means not delisted.  
support_rpi | string | Optional |  | Whether RPI order placement is supported (true if supported; false otherwise)  
support_cross | string | Optional |  | Whether cross-margin order placement is supported (true if supported; false otherwise)  
tag | string | Required |  | Tag information. Hyperliquid returns DEX information, stocks and ETFs return the security description, and other businesses return an empty string  
  
**items / symbol**

Currency pair

Unique trading pair identifier in the format ExchangeType_BusinessType_Base_Counter. Stocks and ETFs use the market as ExchangeType (US/HK/KR/JP) and STOCK or ETF as the business type, for example US_STOCK_AAPL_USDT, HK_STOCK_00700_USDT, or US_ETF_SPY_USDT.

Type | Constraints  
---|---  
string |   
  
**items / exchange_type**

Exchange

Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)

Type | Constraints  
---|---  
string |   
  
**items / business_type**

Business Type

Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / STOCK: stocks / ETF: exchange-traded funds)

Type | Constraints  
---|---  
string |   
  
**items / state**

availablestatus

Status (`live` running / `suspend` paused).

Type | Constraints  
---|---  
string |   
  
**items / min_size**

Minimum order quantity

Minimum order quantity

Type | Constraints  
---|---  
string |   
  
**items / min_notional**

Minimum Order Value

Minimum Order Value

Type | Constraints  
---|---  
string |   
  
**items / lot_size**

Quantity Step

Quantity Step

Type | Constraints  
---|---  
string |   
  
**items / tick_size**

Price Step

Price Step

Type | Constraints  
---|---  
string |   
  
**items / max_num_orders**

maximumopen orderamount

maximumopen orderamount

Type | Constraints  
---|---  
string |   
  
**items / max_market_size**

Maximum Market Order Quantity

Maximum Market Order Quantity

Type | Constraints  
---|---  
string |   
  
**items / max_limit_size**

Maximum Limit Order Quantity

Maximum order quantity for limit orders.

Type | Constraints  
---|---  
string |   
  
**items / contract_size**

Contract Size

Contract multiplier (deprecated; quantity is used uniformly)

Type | Constraints  
---|---  
string |   
  
**items / liquidation_fee**

Liquidation Fee Rate

Liquidation Fee Rate

Type | Constraints  
---|---  
string |   
  
**items / delist_time**

Delisting Time

Millisecond timestamp; `0` means not delisted.

Type | Constraints  
---|---  
string |   
  
**items / support_rpi**

Whether RPI order placement is supported

Whether RPI order placement is supported (true if supported; false otherwise)

Type | Constraints  
---|---  
string |   
  
**items / support_cross**

Whether cross-margin order placement is supported

Whether cross-margin order placement is supported (true if supported; false otherwise)

Type | Constraints  
---|---  
string |   
  
**items / tag**

Tag

Tag information. Hyperliquid returns DEX information, stocks and ETFs return the security description, and other businesses return an empty string

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
    
    url = '/crossex/rule/symbols'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/crossex/rule/symbols \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "exchange_type": "BINANCE",
        "business_type": "FUTURE",
        "state": "live",
        "min_size": "1",
        "min_notional": "5",
        "lot_size": "1",
        "tick_size": "0.00010",
        "max_num_orders": "200",
        "max_market_size": "300000",
        "max_limit_size": "2000000",
        "contract_size": "1",
        "liquidation_fee": "0.012500",
        "support_rpi": "false",
        "support_cross": "true",
        "delist_time": "0",
        "tag": ""
      },
      {
        "symbol": "OKX_FUTURE_ADA_USDT",
        "exchange_type": "OKX",
        "business_type": "FUTURE",
        "state": "suspend",
        "min_size": "10",
        "min_notional": "0",
        "lot_size": "10",
        "tick_size": "0.0001",
        "max_num_orders": "10",
        "max_market_size": "1000000",
        "max_limit_size": "10000000000",
        "contract_size": "100",
        "liquidation_fee": "0",
        "delist_time": "1762163297615",
        "support_rpi": "false",
        "support_cross": "true",
        "tag": ""
      },
      {
        "symbol": "US_STOCK_AAPL_USDT",
        "exchange_type": "US",
        "business_type": "STOCK",
        "state": "live",
        "min_size": "0.01",
        "min_notional": "0",
        "lot_size": "0.01",
        "tick_size": "0.01",
        "max_num_orders": "0",
        "max_market_size": "0",
        "max_limit_size": "0",
        "contract_size": "0",
        "liquidation_fee": "0",
        "delist_time": "0",
        "support_rpi": "false",
        "support_cross": "true",
        "tag": "Apple Inc."
      }
    ]
    

##  Query remaining platform opening capacity

GET`/crossex/rule/open_capacity`

GET `/crossex/rule/open_capacity`

_Query remaining platform opening capacity_

Query the current maximum remaining opening notional value for each futures trading pair in the LONG and SHORT directions. Only trading pairs and position sides with remaining opening capacity below the threshold are returned; omission means the remaining capacity is at least the threshold. When `available_to_open_notional` is `0`, no position can currently be opened for that trading pair and position side. Closing positions is not affected by this rule.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexOpenCapacity

Type | Constraints  
---|---  
object | required: ["symbol","position_side","available_to_open_notional"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Futures trading pair  
position_side | string | Required | enum: ["LONG","SHORT"] | Position side (LONG for long positions / SHORT for short positions)  
available_to_open_notional | number(decimal) | Required |  | Current maximum remaining opening notional value for the position side; 0 means no position can currently be opened  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/rule/open_capacity'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/crossex/rule/open_capacity \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "symbol": "GATE_FUTURE_HIVE_USDT",
        "position_side": "LONG",
        "available_to_open_notional": 390.625
      },
      {
        "symbol": "GATE_FUTURE_HIVE_USDT",
        "position_side": "SHORT",
        "available_to_open_notional": 390.625
      }
    ]
    

##  Query risk limit information

GET`/crossex/rule/risk_limits`

GET `/crossex/rule/risk_limits`

_Query risk limit information_

Query risk limit information for futures/margin trading pairs

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Required | Trading Pair List, multiple separated by commas  
Example values:  
BINANCE_FUTURE_ADA_USDT,GATE_MARGIN_ADA_USDT  
  
####  Detailed descriptions

**symbols** : Trading Pair List, multiple separated by commas  
Example values:  
BINANCE_FUTURE_ADA_USDT,GATE_MARGIN_ADA_USDT

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexRiskLimit

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Optional |  |   
tiers | array | Optional |  |   
  
**items / tiers**

Type | Constraints  
---|---  
array |   
  
**items / tiers / items**

CrossexRiskLimitTier

Type | Constraints  
---|---  
object | required: ["min_risk_limit_value","max_risk_limit_value","quick_cal_amount","leverage_max","maintenance_rate","tier"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
min_risk_limit_value | string | Required |  | Minimum risk limit value  
max_risk_limit_value | string | Required |  | Maximum risk limit value  
quick_cal_amount | string | Required |  | Quick-calculation amount  
leverage_max | string | Required |  | Maximum leverage  
maintenance_rate | string | Required |  | Maintenance margin rate  
tier | string | Required |  | Tier  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/rule/risk_limits'
    query_param = 'symbols=BINANCE_FUTURE_AAVE_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/crossex/rule/risk_limits?symbols=BINANCE_FUTURE_AAVE_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "symbol": "BINANCE_FUTURE_BTC_USDT",
        "tiers": [
          {
            "min_risk_limit_value": "0",
            "max_risk_limit_value": "50000",
            "quick_cal_amount": "0",
            "leverage_max": "20",
            "maintenance_rate": "0.004",
            "tier": "1"
          },
          {
            "min_risk_limit_value": "50000",
            "max_risk_limit_value": "100000",
            "quick_cal_amount": "50",
            "leverage_max": "18",
            "maintenance_rate": "0.005",
            "tier": "2"
          }
        ]
      }
    ]
    

##  Query supported transfer currencies

GET`/crossex/transfers/coin`

GET `/crossex/transfers/coin`

_Query supported transfer currencies_

`est_fee`: Estimated fee. When a fund transfer involves an on-chain withdrawal, the exchange charges this fee. This value is for reference only; the actual fee charged by the exchange applies

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
coin | query | string | Optional | Query by specified currency name  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexTransferCoin

Type | Constraints  
---|---  
object | required: ["coin","is_disabled","precision","est_fee","min_trans_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  | Currency  
min_trans_amount | number | Required |  | Minimum transfer amount (estimated fee included)  
est_fee | number | Required |  | Estimated Fee  
precision | integer | Required |  | Precision  
is_disabled | integer | Required |  | If it is disabled. 0 means NOT being disabled  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/transfers/coin'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/crossex/transfers/coin \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "coin": "string",
        "min_trans_amount": 0,
        "est_fee": 0,
        "precision": 0,
        "is_disabled": 0
      }
    ]
    

##  Query Fund Transfer History🔒 Authenticated

GET`/crossex/transfers`

GET `/crossex/transfers`

_Query Fund Transfer History_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
coin | query | string | Optional | Query by specified currency name  
order_id | query | string | Optional | Supports querying by the order ID returned when creating an order (tx_id), as well as a user-defined custom ID specified at creation (text)  
from | query | integer | Optional | Start timestamp for the query  
to | query | integer | Optional | End timestamp for the query, defaults to current time if not specified  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number returned by list, max 1000  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexTransferRecord

Type | Constraints  
---|---  
object | required: ["id","text","create_time","update_time","status","from_account_type","to_account_type","amount","coin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required |  | Order ID  
text | string | Required |  | Client Custom ID  
from_account_type | string | Required |  | Source account for this operation (`from`) (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`).  
to_account_type | string | Required |  | Destination account for this operation (`to`) (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`).  
coin | string | Required |  | Currency  
amount | string | Required |  | Transfer amount, the amount requested for the transfer  
actual_receive | string | Optional |  | Actual credited amount (has a value when status = SUCCESS; empty for other statuses)  
status | string | Required |  | Transfer Status  
\- `FAIL`: Failed  
\- `SUCCESS`: Successful  
\- `PENDING`: Transfer in Progress  
fail_reason | string | Optional |  | Failure reason (has a value when status = FAIL; empty for other statuses)  
create_time | integer | Required |  | Creation time of order  
update_time | integer | Required |  | OrderUpdateTime  
  
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
    
    url = '/crossex/transfers'
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
    url="/crossex/transfers"
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
        "id": "33829017692939266",
        "text": "33829017692939266",
        "from_account_type": "CROSSEX_BINANCE",
        "to_account_type": "CROSSEX_OKX",
        "coin": "BTC",
        "amount": "1.1234567",
        "actual_receive": "1.123",
        "status": "SUCCESS",
        "fail_reason": null,
        "create_time": 1750681141933,
        "update_time": 1750681141933
      },
      {
        "id": "38083797492939266",
        "text": "38083797492939266",
        "from_account_type": "CROSSEX",
        "to_account_type": "SPOT",
        "coin": "USDT",
        "amount": "100",
        "actual_receive": null,
        "status": "FAIL",
        "fail_reason": "Insufficient transferAvailable",
        "create_time": 1750681141933,
        "update_time": 1750681141933
      }
    ]
    

##  Fund Transfer🔒 Authenticated

POST`/crossex/transfers`

POST `/crossex/transfers`

_Fund Transfer_

Rate limit: 10 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexTransferRequest | Optional | none  
coin | body | string | Required | Currency  
amount | body | string | Required | Transfer amount  
from | body | string | Required | `from` debit account (funds withdrawn from): `CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`  
to | body | string | Required | `to` receiving account (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`).  
text | body | string | Optional | User-defined ID  
  
####  Request Body Schema

Fund Transfer Request Body

Request Body SchemaType | Constraints  
---|---  
CrossexTransferRequest | required: ["amount","from","coin","to"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  | Currency  
amount | string | Required |  | Transfer amount  
from | string | Required |  | `from` debit account (funds withdrawn from): `CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`  
to | string | Required |  | `to` receiving account (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`).  
text | string | Optional |  | User-defined ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexTransferResponse  
  
### Response Schema

Status Code **200**

CrossexTransferResponse

Type | Constraints  
---|---  
CrossexTransferResponse | required: ["tx_id","text"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
tx_id | string | Required |  | Order ID  
text | string | Required |  | User-defined Order ID  
  
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
    
    url = '/crossex/transfers'
    query_param = ''
    body='{"coin":"USDT","amount":"242.45","from":"SPOT","to":"CROSSEX"}'
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
    url="/crossex/transfers"
    query_param=""
    body_param='{"coin":"USDT","amount":"242.45","from":"SPOT","to":"CROSSEX"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "coin": "USDT",
      "amount": "242.45",
      "from": "SPOT",
      "to": "CROSSEX"
    }
    

> Example responses

> 200 Response
    
    
    {
      "tx_id": "23453",
      "text": "23453"
    }
    

##  Create order🔒 Authenticated

POST`/crossex/orders`

POST `/crossex/orders`

_Create order_

Rate limit: 100 requests per 10 seconds; each user may have up to 1,000 open orders. Stocks and ETFs have an additional per-user limit of one request per second and support only cross-exchange account mode and GTC. Stock and ETF orders must use qty; quote_qty is not supported. Stock and ETF order prices use the listing market currency: USD for US markets, HKD for Hong Kong, KRW for South Korea, and JPY for Japan.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexOrderRequest | Optional | none  
text | body | string | Optional | Client-defined Order ID, supports letters (a-z), numbers (0-9), symbols (-, _) only  
symbol | body | string | Required | Unique identifier Exchange_Business_Base_Counter  
Examples:  
To place a spot order for ADA/USDT on BINANCE, use `BINANCE_SPOT_ADA_USDT`;  
To place a USDT-margined perpetual futures order for ADA/USDT on OKX, use `OKX_FUTURE_ADA_USDT`;  
To place a spot margin order for ADA/USDT on GATE, use `GATE_MARGIN_ADA_USDT`;  
To place a spot order for ADA/USDT on BYBIT, use `BYBIT_SPOT_ADA_USDT`;  
To place a futures order for ADA/USD on KRAKEN, use `KRAKEN_FUTURE_ADA_USD`;  
To place a futures order for ADA/USDC on HYPERLIQUID, use `HYPERLIQUID_FUTURE_ADA_USDC`;  
To place a futures order for ADA/USDC on DERIBIT, use `DERIBIT_FUTURE_ADA_USDC`;  
To place a futures order for ADA/USDC on LIGHTER, use `LIGHTER_FUTURE_ADA_USDC`;  
To trade US stock AAPL, use `US_STOCK_AAPL_USDT`;  
To trade Hong Kong stock 00700, use `HK_STOCK_00700_USDT`;  
To trade US ETF SPY, use `US_ETF_SPY_USDT`;  
Spot, USDT-margined perpetual futures, spot margin, stock, and ETF orders are supported. BYBIT/DERIBIT do not currently support spot margin orders. KRAKEN, HYPERLIQUID, and LIGHTER do not currently support spot or margin orders. Stocks and ETFs support only cross-exchange account mode  
side | body | string | Required | BUY, SELL  
type | body | string | Optional | Order type (default: `LIMIT`; supported types: `LIMIT`, `MARKET`)  
time_in_force | body | string | Optional | Defaults to GTC. Supported values: `GTC`, `IOC`, `FOK`, `POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
Stocks and ETFs support only `GTC`  
qty | body | string | Optional | Order quantity (required except for spot and margin market buys; qty is required for stocks and ETFs)  
price | body | string | Optional | Limit order price (required for limit orders). Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
quote_qty | body | string | Optional | Order quote quantity, required for spot and margin market buys. Stock and ETF orders do not support quote_qty  
reduce_only | body | string | Optional | Reduce-only: `true` or `false`  
position_side | body | string | Optional | Position side: `NONE`, `LONG`, `SHORT`  
Defaults to `NONE` (single position mode) if not specified  
  
####  Detailed descriptions

** symbol**: Unique identifier Exchange_Business_Base_Counter  
Examples:  
To place a spot order for ADA/USDT on BINANCE, use `BINANCE_SPOT_ADA_USDT`;  
To place a USDT-margined perpetual futures order for ADA/USDT on OKX, use `OKX_FUTURE_ADA_USDT`;  
To place a spot margin order for ADA/USDT on GATE, use `GATE_MARGIN_ADA_USDT`;  
To place a spot order for ADA/USDT on BYBIT, use `BYBIT_SPOT_ADA_USDT`;  
To place a futures order for ADA/USD on KRAKEN, use `KRAKEN_FUTURE_ADA_USD`;  
To place a futures order for ADA/USDC on HYPERLIQUID, use `HYPERLIQUID_FUTURE_ADA_USDC`;  
To place a futures order for ADA/USDC on DERIBIT, use `DERIBIT_FUTURE_ADA_USDC`;  
To place a futures order for ADA/USDC on LIGHTER, use `LIGHTER_FUTURE_ADA_USDC`;  
To trade US stock AAPL, use `US_STOCK_AAPL_USDT`;  
To trade Hong Kong stock 00700, use `HK_STOCK_00700_USDT`;  
To trade US ETF SPY, use `US_ETF_SPY_USDT`;  
Spot, USDT-margined perpetual futures, spot margin, stock, and ETF orders are supported. BYBIT/DERIBIT do not currently support spot margin orders. KRAKEN, HYPERLIQUID, and LIGHTER do not currently support spot or margin orders. Stocks and ETFs support only cross-exchange account mode

** time_in_force**: Defaults to GTC. Supported values: `GTC`, `IOC`, `FOK`, `POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
Stocks and ETFs support only `GTC`

** position_side**: Position side: `NONE`, `LONG`, `SHORT`  
Defaults to `NONE` (single position mode) if not specified

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | BUY  
side | SELL  
type | LIMIT  
type | MARKET  
time_in_force | GTC  
time_in_force | IOC  
time_in_force | FOK  
time_in_force | POC  
time_in_force | RPI  
reduce_only | true  
reduce_only | false  
position_side | LONG  
position_side | SHORT  
position_side | NONE  
  
####  Request Body Schema

Place Order Request Body

Request Body SchemaType | Constraints  
---|---  
CrossexOrderRequest | required: ["symbol","side"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
text | string | Optional |  | Client-defined Order ID, supports letters (a-z), numbers (0-9), symbols (-, _) only  
symbol | string | Required |  | Unique identifier Exchange_Business_Base_Counter  
Examples:  
To place a spot order for ADA/USDT on BINANCE, use `BINANCE_SPOT_ADA_USDT`;  
To place a USDT-margined perpetual futures order for ADA/USDT on OKX, use `OKX_FUTURE_ADA_USDT`;  
To place a spot margin order for ADA/USDT on GATE, use `GATE_MARGIN_ADA_USDT`;  
To place a spot order for ADA/USDT on BYBIT, use `BYBIT_SPOT_ADA_USDT`;  
To place a futures order for ADA/USD on KRAKEN, use `KRAKEN_FUTURE_ADA_USD`;  
To place a futures order for ADA/USDC on HYPERLIQUID, use `HYPERLIQUID_FUTURE_ADA_USDC`;  
To place a futures order for ADA/USDC on DERIBIT, use `DERIBIT_FUTURE_ADA_USDC`;  
To place a futures order for ADA/USDC on LIGHTER, use `LIGHTER_FUTURE_ADA_USDC`;  
To trade US stock AAPL, use `US_STOCK_AAPL_USDT`;  
To trade Hong Kong stock 00700, use `HK_STOCK_00700_USDT`;  
To trade US ETF SPY, use `US_ETF_SPY_USDT`;  
Spot, USDT-margined perpetual futures, spot margin, stock, and ETF orders are supported. BYBIT/DERIBIT do not currently support spot margin orders. KRAKEN, HYPERLIQUID, and LIGHTER do not currently support spot or margin orders. Stocks and ETFs support only cross-exchange account mode  
side | string | Required | enum: ["BUY","SELL"] | BUY, SELL  
type | string | Optional | enum: ["LIMIT","MARKET"]  
default: "LIMIT" | Order type (default: `LIMIT`; supported types: `LIMIT`, `MARKET`)  
time_in_force | string | Optional | enum: ["GTC","IOC","FOK","POC","RPI"]  
default: "GTC" | Defaults to GTC. Supported values: `GTC`, `IOC`, `FOK`, `POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
Stocks and ETFs support only `GTC`  
qty | string | Optional |  | Order quantity (required except for spot and margin market buys; qty is required for stocks and ETFs)  
price | string | Optional |  | Limit order price (required for limit orders). Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
quote_qty | string | Optional |  | Order quote quantity, required for spot and margin market buys. Stock and ETF orders do not support quote_qty  
reduce_only | string | Optional | enum: ["true","false"] | Reduce-only: `true` or `false`  
position_side | string | Optional | enum: ["LONG","SHORT","NONE"] | Position side: `NONE`, `LONG`, `SHORT`  
Defaults to `NONE` (single position mode) if not specified  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrderActionResponse  
  
### Response Schema

Status Code **200**

CrossexOrderActionResponse

Type | Constraints  
---|---  
CrossexOrderActionResponse | required: ["order_id","text"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
text | string | Required |  | User-defined Order ID  
  
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
    
    url = '/crossex/orders'
    query_param = ''
    body='{"symbol":"BINANCE_SPOT_ADA_USDT","side":"BUY","type":"MARKET","quote_qty":"10"}'
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
    url="/crossex/orders"
    query_param=""
    body_param='{"symbol":"BINANCE_SPOT_ADA_USDT","side":"BUY","type":"MARKET","quote_qty":"10"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "symbol": "BINANCE_SPOT_ADA_USDT",
      "side": "BUY",
      "type": "MARKET",
      "quote_qty": "10"
    }
    

> Example responses

> 200 Response
    
    
    {
      "order_id": "123456",
      "text": "cross-test-1"
    }
    

##  Batch cancel orders🔒 Authenticated

POST`/crossex/batch_cancel_orders`

POST `/crossex/batch_cancel_orders`

_Batch cancel orders_

Cancel multiple specified orders. Either order_id or text is required; if both are provided, order_id takes precedence. Rate limit: 100 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | array[CrossexBatchCancelOrderRequest] | Required | none  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
array |   
  
**items**

CrossexBatchCancelOrderRequest

Batch cancel orders

Request Body SchemaType | Constraints  
---|---  
CrossexBatchCancelOrderRequest |   
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
order_id | string | false |  | Order ID; either this field or text is required  
text | string | false |  | Custom ID specified by the user when creating the order; either this field or order_id is required  
  
**items / anyOf[0]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["order_id"]  
  
**items / anyOf[1]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["text"]  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch order cancellation request results | [CrossexBatchCancelOrderResponse]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexBatchCancelOrderResponse

Batch order cancellation request results

Type | Constraints  
---|---  
CrossexBatchCancelOrderResponse | required: ["order_id","text","accepted","label","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
text | string | Required |  | Custom ID specified by the user when creating the order  
accepted | string | Required |  | Whether the request was accepted, as the string true or false  
label | string | Required |  | Error label when the request is not accepted; empty on success  
message | string | Required |  | Error message when the request is not accepted; empty on success  
  
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
    
    url = '/crossex/batch_cancel_orders'
    query_param = ''
    body='[{"order_id":"123456"},{"text":"crossex-test-1"}]'
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
    url="/crossex/batch_cancel_orders"
    query_param=""
    body_param='[{"order_id":"123456"},{"text":"crossex-test-1"}]'
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
        "order_id": "123456"
      },
      {
        "text": "crossex-test-1"
      }
    ]
    

> Example responses

> 200 Response
    
    
    [
      {
        "order_id": "123456",
        "text": "",
        "accepted": "true",
        "label": "",
        "message": ""
      },
      {
        "order_id": "",
        "text": "crossex-test-1",
        "accepted": "false",
        "label": "TRADE_ORDER_NOT_FOUND_ERROR",
        "message": "The order was not found"
      }
    ]
    

##  Query order details🔒 Authenticated

GET`/crossex/orders/{order_id}`

GET `/crossex/orders/{order_id}`

_Query order details_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | 1\. Supports querying order IDs returned when creating orders  
2\. Supports custom IDs specified by users when creating orders (i.e., the text field)  
  
####  Detailed descriptions

**order_id** : 1. Supports querying order IDs returned when creating orders  
2\. Supports custom IDs specified by users when creating orders (i.e., the text field)

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrder  
  
### Response Schema

Status Code **200**

CrossexOrder

Type | Constraints  
---|---  
CrossexOrder | required: ["user_id","order_id","text","state","symbol","side","type","exchange_type","attribute","executed_avg_price","executed_amount","executed_qty","time_in_force","price","quote_qty","qty","business_type","fee","fee_coin","reduce_only","leverage","last_executed_price","last_executed_qty","reason","position_side","last_executed_amount","update_time","create_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
order_id | string | Required |  | Order ID  
text | string | Required |  | Client-defined order ID.  
state | string | Required |  | Order status:  
`NEW`: validated locally, pending submission to the exchange  
`OPEN`: resting on the exchange order book  
`PARTIALLY_FILLED`: partially filled  
`FILLED`: fully filled  
`FAIL`: CrossEx validation failed; see `reason`  
`REJECT`: rejected by the exchange; see `reason`  
`CANCELLED`: cancelled  
symbol | string | Required |  | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
side | string | Required |  | Side (`BUY` buy / `SELL` sell).  
type | string | Required |  | Order type (`LIMIT` limit / `MARKET` market).  
attribute | string | Required |  | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
exchange_type | string | Required |  | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
business_type | string | Required |  | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)  
qty | string | Required |  | Order quantity in the base currency.  
quote_qty | string | Required |  | Order quantity in the quote currency.  
price | string | Required |  | Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
time_in_force | string | Required |  | Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)  
executed_qty | string | Required |  | Filled base amount.  
executed_amount | string | Required |  | Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
executed_avg_price | string | Required |  | Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
fee_coin | string | Required |  | Fee currency  
fee | string | Required |  | Fee amount.  
reduce_only | string | Required |  | Reduce-only order (`"true"` or `"false"`).  
leverage | string | Required |  | Order leverage multiplier.  
reason | string | Required |  | Failure reason description.  
last_executed_qty | string | Required |  | Base quantity of the latest fill.  
last_executed_price | string | Required |  | Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
last_executed_amount | string | Required |  | Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
position_side | string | Required |  | Position side (`NONE` one-way position / `LONG` long / `SHORT` short)  
create_time | string | Required |  | Created time  
update_time | string | Required |  | Update time  
  
**user_id**

User ID

User ID

Type | Constraints  
---|---  
string |   
  
**order_id**

Order ID

Order ID

Type | Constraints  
---|---  
string |   
  
**text**

Client Order ID

Client-defined order ID.

Type | Constraints  
---|---  
string |   
  
**state**

Order status

Order status: `NEW`: validated locally, pending submission to the exchange `OPEN`: resting on the exchange order book `PARTIALLY_FILLED`: partially filled `FILLED`: fully filled `FAIL`: CrossEx validation failed; see `reason` `REJECT`: rejected by the exchange; see `reason` `CANCELLED`: cancelled

Type | Constraints  
---|---  
string |   
  
**symbol**

Currency pair

Unique trading pair identifiers, e.g. `BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.

Type | Constraints  
---|---  
string |   
  
**side**

direction

Side (`BUY` buy / `SELL` sell).

Type | Constraints  
---|---  
string |   
  
**type**

Type

Order type (`LIMIT` limit / `MARKET` market).

Type | Constraints  
---|---  
string |   
  
**attribute**

Attribute COMMON: Normal Order, LIQ: Liquidation Takeover Order, REDUCE: Liquidation Reduce Order, ADL: Auto-Reduce

Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).

Type | Constraints  
---|---  
string |   
  
**exchange_type**

Exchange

Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)

Type | Constraints  
---|---  
string |   
  
**business_type**

Business Type

Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)

Type | Constraints  
---|---  
string |   
  
**qty**

Base Currency Quantity

Order quantity in the base currency.

Type | Constraints  
---|---  
string |   
  
**quote_qty**

Quote Currency Quantity

Order quantity in the quote currency.

Type | Constraints  
---|---  
string |   
  
**price**

Price

Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**time_in_force**

Time in Force Strategy

Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)

Type | Constraints  
---|---  
string |   
  
**executed_qty**

Filled quantity

Filled base amount.

Type | Constraints  
---|---  
string |   
  
**executed_amount**

Filled Amount

Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**executed_avg_price**

Average Filled Price

Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**fee_coin**

Fee currency

Fee currency

Type | Constraints  
---|---  
string |   
  
**fee**

fee

Fee amount.

Type | Constraints  
---|---  
string |   
  
**reduce_only**

Reduce Position Only

Reduce-only order (`"true"` or `"false"`).

Type | Constraints  
---|---  
string |   
  
**leverage**

Leverage

Order leverage multiplier.

Type | Constraints  
---|---  
string |   
  
**reason**

Reason

Failure reason description.

Type | Constraints  
---|---  
string |   
  
**last_executed_qty**

Latest Filled Quantity

Base quantity of the latest fill.

Type | Constraints  
---|---  
string |   
  
**last_executed_price**

Latest Filled Price

Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**last_executed_amount**

Latest Filled Amount

Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**position_side**

Position Direction

Position side (`NONE` one-way position / `LONG` long / `SHORT` short)

Type | Constraints  
---|---  
string |   
  
**create_time**

Created time

Created time

Type | Constraints  
---|---  
string |   
  
**update_time**

Update time

Update time

Type | Constraints  
---|---  
string |   
  
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
    
    url = '/crossex/orders/2048522992198912'
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
    url="/crossex/orders/2048522992198912"
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
      "user_id": "10001004",
      "order_id": "2048522992198912",
      "text": "2048522992198912",
      "state": "FILLED",
      "symbol": "BINANCE_SPOT_ADA_USDT",
      "side": "BUY",
      "type": "MARKET",
      "attribute": "COMMON",
      "exchange_type": "BINANCE",
      "business_type": "SPOT",
      "qty": "0",
      "quote_qty": "7",
      "price": "0",
      "time_in_force": "GTC",
      "executed_qty": "12.9",
      "executed_amount": "6.96471",
      "executed_avg_price": "0.5399",
      "fee_coin": "ADA",
      "fee": "0.0129",
      "reduce_only": "false",
      "leverage": "1",
      "reason": "",
      "last_executed_qty": "12.9",
      "last_executed_price": "0.5399",
      "last_executed_amount": "6.96471",
      "position_side": "NONE",
      "create_time": "1750681141933",
      "update_time": "1750681142379"
    }
    

##  Modify Order🔒 Authenticated

PUT`/crossex/orders/{order_id}`

PUT `/crossex/orders/{order_id}`

_Modify Order_

Rate Limit: 100 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | Support Order ID or Text for Modify Order  
body | body | CrossexOrderUpdateRequest | Optional | none  
qty | body | string | Optional | modify amount  
price | body | string | Optional | modify price  
  
####  Request Body Schema

Order Modification Request Body

Request Body SchemaType | Constraints  
---|---  
CrossexOrderUpdateRequest |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
qty | string | Optional |  | modify amount  
price | string | Optional |  | modify price  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrderActionResponse  
  
### Response Schema

Status Code **200**

CrossexOrderActionResponse

Type | Constraints  
---|---  
CrossexOrderActionResponse | required: ["order_id","text"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
text | string | Required |  | User-defined Order ID  
  
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
    
    url = '/crossex/orders/string'
    query_param = ''
    body='{"qty":"20","price":"0.65"}'
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
    url="/crossex/orders/string"
    query_param=""
    body_param='{"qty":"20","price":"0.65"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "qty": "20",
      "price": "0.65"
    }
    

> Example responses

> 200 Response
    
    
    {
      "order_id": "123",
      "text": "crossex-test-1"
    }
    

##  Cancel Order🔒 Authenticated

DELETE`/crossex/orders/{order_id}`

DELETE `/crossex/orders/{order_id}`

_Cancel Order_

Rate Limit: 100 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | Support Order ID or Text for Cancel Order  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrderActionResponse  
  
### Response Schema

Status Code **200**

CrossexOrderActionResponse

Type | Constraints  
---|---  
CrossexOrderActionResponse | required: ["order_id","text"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
text | string | Required |  | User-defined Order ID  
  
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
    
    url = '/crossex/orders/string'
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
    url="/crossex/orders/string"
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
      "order_id": "123456",
      "text": "crossex-test-1"
    }
    

##  Flash Swap Inquiry🔒 Authenticated

POST`/crossex/convert/quote`

POST `/crossex/convert/quote`

_Flash Swap Inquiry_

Rate limit: 100 requests per day For HYPERLIQUID, swaps between `HYPERLIQUID_USDC` and `CROSSEX_USDT` are supported. Flash Swap in isolated exchange mode is not currently supported for HYPERLIQUID. For LIGHTER, swaps between `LIGHTER_USDC` and `CROSSEX_USDT` are supported. Flash Swap in isolated exchange mode is not currently supported for LIGHTER. For KRAKEN, only conversion from `KRAKEN_USD` to `CROSSEX_USDT` is supported. Flash Swap in isolated exchange mode is not currently supported for KRAKEN.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexConvertQuoteRequest | Optional | none  
exchange_type | body | string | Required | Exchange type  
Currently supports only BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, and LIGHTER  
from_coin | body | string | Required | Asset Sold  
to_coin | body | string | Required | Asset to receive  
OKX and GATE only support conversion to BTC, ETH, or USDT  
BYBIT and BINANCE only support conversion to USDT  
HYPERLIQUID only supports conversion to USDT or USDC  
KRAKEN only supports conversion to USDT  
LIGHTER only supports swaps between USDT and USDC  
from_amount | body | string | Required | Amount to sell  
  
####  Detailed descriptions

** exchange_type**: Exchange type  
Currently supports only BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, and LIGHTER

** to_coin**: Asset to receive  
OKX and GATE only support conversion to BTC, ETH, or USDT  
BYBIT and BINANCE only support conversion to USDT  
HYPERLIQUID only supports conversion to USDT or USDC  
KRAKEN only supports conversion to USDT  
LIGHTER only supports swaps between USDT and USDC

####  Request Body Schema

Flash Swap Quote Request Body

Request Body SchemaType | Constraints  
---|---  
CrossexConvertQuoteRequest | required: ["exchange_type","from_coin","to_coin","from_amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
exchange_type | string | Required |  | Exchange type  
Currently supports only BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, and LIGHTER  
from_coin | string | Required |  | Asset Sold  
to_coin | string | Required |  | Asset to receive  
OKX and GATE only support conversion to BTC, ETH, or USDT  
BYBIT and BINANCE only support conversion to USDT  
HYPERLIQUID only supports conversion to USDT or USDC  
KRAKEN only supports conversion to USDT  
LIGHTER only supports swaps between USDT and USDC  
from_amount | string | Required |  | Amount to sell  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexConvertQuoteResponse  
  
### Response Schema

Status Code **200**

CrossexConvertQuoteResponse

Type | Constraints  
---|---  
CrossexConvertQuoteResponse | required: ["quote_id","valid_ms","from_coin","to_coin","from_amount","to_amount","price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
quote_id | string | Required |  | Quote ID  
valid_ms | string | Required |  | Valid time (milliseconds timestamp)  
from_coin | string | Required |  | Asset Sold  
to_coin | string | Required |  | Asset Bought  
from_amount | string | Required |  | Amount to sell  
to_amount | string | Required |  | Amount to buy  
price | string | Required |  | Quoted price  
  
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
    
    url = '/crossex/convert/quote'
    query_param = ''
    body='{"exchange_type":"GATE","from_coin":"BTC","to_coin":"USDT","from_amount":"0.00008"}'
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
    url="/crossex/convert/quote"
    query_param=""
    body_param='{"exchange_type":"GATE","from_coin":"BTC","to_coin":"USDT","from_amount":"0.00008"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "exchange_type": "GATE",
      "from_coin": "BTC",
      "to_coin": "USDT",
      "from_amount": "0.00008"
    }
    

> Example responses

> 200 Response
    
    
    {
      "quote_id": "2074460878500352",
      "valid_ms": "5000",
      "from_coin": "USDT",
      "to_coin": "BTC",
      "from_amount": "3",
      "to_amount": "0.000027",
      "price": "0.000009"
    }
    

##  Flash Swap Transaction🔒 Authenticated

POST`/crossex/convert/orders`

POST `/crossex/convert/orders`

_Flash Swap Transaction_

Rate limit: 10 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexConvertOrderRequest | Optional | none  
quote_id | body | string | Required | Inquiry ID  
  
####  Request Body Schema

Flash Swap Transaction Request Body

Request Body SchemaType | Constraints  
---|---  
CrossexConvertOrderRequest | required: ["quote_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
quote_id | string | Required |  | Inquiry ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexConvertOrderResponse  
  
### Response Schema

Status Code **200**

CrossexConvertOrderResponse

Type | Constraints  
---|---  
CrossexConvertOrderResponse | required: ["order_id","text"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
text | string | Required |  | Order ID (cannot be customized)  
  
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
    
    url = '/crossex/convert/orders'
    query_param = ''
    body='{"quote_id":"232321331"}'
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
    url="/crossex/convert/orders"
    query_param=""
    body_param='{"quote_id":"232321331"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "quote_id": "232321331"
    }
    

> Example responses

> 200 Response
    
    
    {
      "order_id": "123456",
      "text": "123456"
    }
    

##  Query Account Assets🔒 Authenticated

GET`/crossex/accounts`

GET `/crossex/accounts`

_Query Account Assets_

Rate limit: 200 requests per 10 seconds If 100% <= initial_margin_rate < 110%, transferring out the margin currency is prohibited. If initial_margin_rate < 100%, the system automatically cancels orders; only closing positions is allowed, not opening new ones. If maintenance_margin_rate <= 100%, the system forces liquidation.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
exchange_type | query | string | Optional | Trading venue identifier. Omit in cross-exchange mode; required in isolated-per-venue mode (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER`).  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexAccount  
  
### Response Schema

Status Code **200**

CrossexAccount

Type | Constraints  
---|---  
CrossexAccount | required: ["user_id","available_margin","margin_balance","initial_margin","maintenance_margin","initial_margin_rate","maintenance_margin_rate","position_mode","create_time","update_time","assets"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
available_margin | string | Required |  | Available Margin  
margin_balance | string | Required |  | marginbalance  
initial_margin | string | Required |  | Initial Margin  
maintenance_margin | string | Required |  | Maintenance margin  
initial_margin_rate | string | Required |  | Initial margin rate  
maintenance_margin_rate | string | Required |  | Maintenance margin rate  
position_mode | string | Required |  | Contract Position Mode  
account_limit | string | Optional |  | Account limit  
create_time | string | Required |  | Created time  
update_time | string | Required |  | Update time  
account_mode | string | Optional |  | Account Mode. CROSS_EXCHANGE: Cross-Exchange Mode; ISOLATED_EXCHANGE: Split-Exchange Mode  
exchange_type | string | Optional |  | Exchange Type. When account_mode is CROSS_EXCHANGE, it must be CROSSEX; otherwise, it is another exchange.  
assets | array | Required |  | Asset list: grouped by exchange and currency, returning per-account balances, margin, and PnL details  
  
**assets**

Asset list: grouped by exchange and currency, returning per-account balances, margin, and PnL details

Type | Constraints  
---|---  
array |   
  
**assets / items**

CrossexAccountAsset

Type | Constraints  
---|---  
object | required: ["borrowing_initial_margin","borrowing_maintenance_margin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Optional |  | User ID  
coin | string | Optional |  | Currency  
exchange_type | string | Optional |  | Exchange  
balance | string | Optional |  | Balance  
upnl | string | Optional |  | Unrealized P&L  
equity | string | Optional |  | Net margin equity for the currency  
futures_initial_margin | string | Optional |  | Currency-specific futures initial margin. This value is populated for futures settlement currencies (USDT/USDC/USD)  
futures_maintenance_margin | string | Optional |  | Currency-specific futures maintenance margin. This value is populated for futures settlement currencies (USDT/USDC/USD)  
borrowing_initial_margin | string | Required |  | Currency-specific margin trading initial margin. This value is populated for margin or futures settlement currencies (USDT/USDC/USD)  
borrowing_maintenance_margin | string | Required |  | Currency-specific margin trading maintenance margin. This value is populated for margin or futures settlement currencies (USDT/USDC/USD)  
available_balance | string | Optional |  | Available Balance  
liability | string | Optional |  | Liability for the currency. This value is populated only for USDT, USDC, or USD  
  
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
    
    url = '/crossex/accounts'
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
    url="/crossex/accounts"
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
      "user_id": "123456789",
      "available_margin": "1200",
      "margin_balance": "1200",
      "initial_margin": "500",
      "maintenance_margin": "250",
      "initial_margin_rate": "2.4",
      "maintenance_margin_rate": "4.8",
      "position_mode": "SINGLE",
      "account_limit": "5000",
      "create_time": "1687573845000",
      "update_time": "1687588938000",
      "account_mode": "CROSS_EXCHANGE",
      "exchange_type": "CROSSEX",
      "assets": [
        {
          "user_id": "123456789",
          "coin": "USDT",
          "exchange_type": "BINANCE",
          "balance": "1000",
          "upnl": "200",
          "equity": "1200",
          "futures_initial_margin": "400",
          "futures_maintenance_margin": "130",
          "borrowing_initial_margin": "100",
          "borrowing_maintenance_margin": "120",
          "available_balance": "1000.0",
          "liability": "0"
        }
      ]
    }
    

##  Modify Account Contract Position Mode and Account Mode🔒 Authenticated

PUT`/crossex/accounts`

PUT `/crossex/accounts`

_Modify Account Contract Position Mode and Account Mode_

Rate Limit: 100 requests per 60 seconds. position_mode+exchange_type modifies contract position mode (exchange_type is required when the user's account mode is split exchange); account_mode modifies the user's account mode.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexAccountUpdateRequest | Optional | none  
position_mode | body | string | Optional | Futures position mode (SINGLE/DUAL)  
account_mode | body | string | Optional | Account mode (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
exchange_type | body | string | Optional | Exchange (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to adjust futures position mode.  
  
####  Request Body Schema

Change Account Request Body

Request Body SchemaType | Constraints  
---|---  
CrossexAccountUpdateRequest |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
position_mode | string | Optional |  | Futures position mode (SINGLE/DUAL)  
account_mode | string | Optional |  | Account mode (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
exchange_type | string | Optional |  | Exchange (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to adjust futures position mode.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexAccountUpdateResponse  
  
### Response Schema

Status Code **202**

CrossexAccountUpdateResponse

Type | Constraints  
---|---  
CrossexAccountUpdateResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
position_mode | string | Optional |  | Requested futures position mode to modify (SINGLE/DUAL)  
account_mode | string | Optional |  | Requested account mode to modify (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
exchange_type | string | Optional |  | Exchange targeted by the requested change (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to change futures position mode.  
  
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
    
    url = '/crossex/accounts'
    query_param = ''
    body='{"position_mode":"SINGLE"}'
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
    url="/crossex/accounts"
    query_param=""
    body_param='{"position_mode":"SINGLE"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "position_mode": "SINGLE"
    }
    

> Example responses

> 202 Response
    
    
    {
      "position_mode": "SINGLE"
    }
    

##  Query Contract Trading Pair Leverage Multiplier🔒 Authenticated

GET`/crossex/positions/leverage`

GET `/crossex/positions/leverage`

_Query Contract Trading Pair Leverage Multiplier_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Optional | Trading Pair List, multiple separated by commas  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline  
  
### Response Schema

Status Code **200**

Mapping from trading pair to leverage multiplier.

Type | Constraints  
---|---  
object |   
  
**additionalProperties**

Leverage multiplier for the corresponding trading pair

Type | Constraints  
---|---  
string |   
  
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
    
    url = '/crossex/positions/leverage'
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
    url="/crossex/positions/leverage"
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
      "BINANCE_FUTURE_BTC_USDT": "3",
      "OKX_FUTURE_BTC_USDT": "3",
      "GATE_FUTURE_BTC_USDT": "3"
    }
    

##  Modify Contract Trading Pair Leverage Multiplier🔒 Authenticated

POST`/crossex/positions/leverage`

POST `/crossex/positions/leverage`

_Modify Contract Trading Pair Leverage Multiplier_

Rate Limit: 100 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexLeverageRequest | Optional | none  
symbol | body | string | Required | Currency pair  
leverage | body | string | Required | Leverage  
  
####  Request Body Schema

Change Leverage Request Body (for futures/margin)

Request Body SchemaType | Constraints  
---|---  
CrossexLeverageRequest | required: ["symbol","leverage"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Currency pair  
leverage | string | Required |  | Leverage  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexLeverageResponse  
  
### Response Schema

Status Code **202**

CrossexLeverageResponse

Type | Constraints  
---|---  
CrossexLeverageResponse | required: ["symbol","leverage"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Currency pair  
leverage | string | Required |  | Requested Modified Leverage  
  
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
    
    url = '/crossex/positions/leverage'
    query_param = ''
    body='{"symbol":"OKX_FUTURE_ADA_USDT","leverage":"1"}'
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
    url="/crossex/positions/leverage"
    query_param=""
    body_param='{"symbol":"OKX_FUTURE_ADA_USDT","leverage":"1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "symbol": "OKX_FUTURE_ADA_USDT",
      "leverage": "1"
    }
    

> Example responses

> 202 Response
    
    
    {
      "symbol": "OKX_FUTURE_ADA_USDT",
      "leverage": "1"
    }
    

##  Query Leveraged Trading Pair Leverage Multiplier🔒 Authenticated

GET`/crossex/margin_positions/leverage`

GET `/crossex/margin_positions/leverage`

_Query Leveraged Trading Pair Leverage Multiplier_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Optional | Trading Pair List, multiple separated by commas  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline  
  
### Response Schema

Status Code **200**

Mapping from trading pair to leverage multiplier.

Type | Constraints  
---|---  
object |   
  
**additionalProperties**

Leverage multiplier for the corresponding trading pair

Type | Constraints  
---|---  
string |   
  
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
    
    url = '/crossex/margin_positions/leverage'
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
    url="/crossex/margin_positions/leverage"
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
      "BINANCE_MARGIN_BTC_USDT": "3",
      "OKX_MARGIN_BTC_USDT": "3",
      "GATE_MARGIN_BTC_USDT": "3"
    }
    

##  Modify Leveraged Trading Pair Leverage Multiplier🔒 Authenticated

POST`/crossex/margin_positions/leverage`

POST `/crossex/margin_positions/leverage`

_Modify Leveraged Trading Pair Leverage Multiplier_

Rate Limit: 100 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexLeverageRequest | Optional | none  
symbol | body | string | Required | Currency pair  
leverage | body | string | Required | Leverage  
  
####  Request Body Schema

Change Leverage Request Body (for futures/margin)

Request Body SchemaType | Constraints  
---|---  
CrossexLeverageRequest | required: ["symbol","leverage"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Currency pair  
leverage | string | Required |  | Leverage  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexLeverageResponse  
  
### Response Schema

Status Code **202**

CrossexLeverageResponse

Type | Constraints  
---|---  
CrossexLeverageResponse | required: ["symbol","leverage"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Currency pair  
leverage | string | Required |  | Requested Modified Leverage  
  
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
    
    url = '/crossex/margin_positions/leverage'
    query_param = ''
    body='{"symbol":"OKX_MARGIN_ADA_USDT","leverage":"1"}'
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
    url="/crossex/margin_positions/leverage"
    query_param=""
    body_param='{"symbol":"OKX_MARGIN_ADA_USDT","leverage":"1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "symbol": "OKX_MARGIN_ADA_USDT",
      "leverage": "1"
    }
    

> Example responses

> 202 Response
    
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    

##  Close a position in full.🔒 Authenticated

POST`/crossex/position`

POST `/crossex/position`

_Close a position in full._

Rate limit: 100 requests per day. Automatic position-closing rules. FUTURE and MARGIN positions are supported.

Before using this endpoint, ensure that the following prerequisite is met:

  * There are no open orders for the symbol in the current account.
  * Once the prerequisite is met, the system checks whether the position meets either of the following conditions:
  * Less than the minimum notional amount (minNotional)
  * Less than the minimum order size (minSize)

When either condition is met, the system automatically creates a closing order and immediately closes the entire position. This endpoint prevents positions that are too small to be submitted to an exchange from becoming stranded and ensures that small positions can be closed when they fall below the threshold.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexClosePositionRequest | Optional | none  
symbol | body | string | Required | Trading Pair  
1\. Supports leveraged trading pairs, e.g., BINANCE_MARGIN_SOL_USDT  
2\. Supports contract trading pairs, e.g., OKX_FUTURE_ETH_USDT  
position_side | body | string | Optional | Position Direction  
1\. For leveraged positions, this parameter must be passed  
2\. For contract positions, pass selectively based on your contract holding method  
  
####  Detailed descriptions

** symbol**: Trading Pair  
1\. Supports leveraged trading pairs, e.g., BINANCE_MARGIN_SOL_USDT  
2\. Supports contract trading pairs, e.g., OKX_FUTURE_ETH_USDT

** position_side**: Position Direction  
1\. For leveraged positions, this parameter must be passed  
2\. For contract positions, pass selectively based on your contract holding method

####  Request Body Schema

Full Close Position Request Body

Request Body SchemaType | Constraints  
---|---  
CrossexClosePositionRequest | required: ["symbol"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Trading Pair  
1\. Supports leveraged trading pairs, e.g., BINANCE_MARGIN_SOL_USDT  
2\. Supports contract trading pairs, e.g., OKX_FUTURE_ETH_USDT  
position_side | string | Optional |  | Position Direction  
1\. For leveraged positions, this parameter must be passed  
2\. For contract positions, pass selectively based on your contract holding method  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexOrderActionResponse  
  
### Response Schema

Status Code **202**

CrossexOrderActionResponse

Type | Constraints  
---|---  
CrossexOrderActionResponse | required: ["order_id","text"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
text | string | Required |  | User-defined Order ID  
  
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
    
    url = '/crossex/position'
    query_param = ''
    body='{"symbol":"BINANCE_FUTURE_SOL_USDT","position_side":"LONG"}'
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
    url="/crossex/position"
    query_param=""
    body_param='{"symbol":"BINANCE_FUTURE_SOL_USDT","position_side":"LONG"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "symbol": "BINANCE_FUTURE_SOL_USDT",
      "position_side": "LONG"
    }
    

> Example responses

> 202 Response
    
    
    {
      "order_id": "123456",
      "text": "123456"
    }
    

##  Get futures position margin mode🔒 Authenticated

GET`/crossex/positions/margin_mode`

GET `/crossex/positions/margin_mode`

_Get futures position margin mode_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | query | string | Required | Futures trading pair  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexMarginModeResponse  
  
### Response Schema

Status Code **200**

CrossexMarginModeResponse

Type | Constraints  
---|---  
CrossexMarginModeResponse | required: ["symbol","margin_mode"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Futures trading pair  
margin_mode | string | Required |  | Margin mode (CROSS/ISOLATED)  
  
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
    
    url = '/crossex/positions/margin_mode'
    query_param = 'symbol=HYPERLIQUID_FUTURE_CXMT_USDC'
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
    url="/crossex/positions/margin_mode"
    query_param="symbol=HYPERLIQUID_FUTURE_CXMT_USDC"
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
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin_mode": "ISOLATED"
    }
    

##  Update futures position margin mode🔒 Authenticated

POST`/crossex/positions/margin_mode`

POST `/crossex/positions/margin_mode`

_Update futures position margin mode_

Rate limit: 100 requests per 10 seconds. Only Hyperliquid futures trading pairs are supported. The margin mode cannot be changed while open orders or positions exist

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexMarginModeRequest | Optional | none  
symbol | body | string | Required | Hyperliquid futures trading pair  
margin_mode | body | string | Required | Margin mode (CROSS/ISOLATED)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
margin_mode | CROSS  
margin_mode | ISOLATED  
  
####  Request Body Schema

Request body for updating the futures position margin mode

Request Body SchemaType | Constraints  
---|---  
CrossexMarginModeRequest | required: ["symbol","margin_mode"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Hyperliquid futures trading pair  
margin_mode | string | Required | enum: ["CROSS","ISOLATED"] | Margin mode (CROSS/ISOLATED)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexMarginModeResponse  
  
### Response Schema

Status Code **202**

CrossexMarginModeResponse

Type | Constraints  
---|---  
CrossexMarginModeResponse | required: ["symbol","margin_mode"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Futures trading pair  
margin_mode | string | Required |  | Margin mode (CROSS/ISOLATED)  
  
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
    
    url = '/crossex/positions/margin_mode'
    query_param = ''
    body='{"symbol":"HYPERLIQUID_FUTURE_CXMT_USDC","margin_mode":"ISOLATED"}'
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
    url="/crossex/positions/margin_mode"
    query_param=""
    body_param='{"symbol":"HYPERLIQUID_FUTURE_CXMT_USDC","margin_mode":"ISOLATED"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin_mode": "ISOLATED"
    }
    

> Example responses

> 202 Response
    
    
    {
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin_mode": "ISOLATED"
    }
    

##  Increase or decrease isolated margin🔒 Authenticated

POST`/crossex/positions/margin`

POST `/crossex/positions/margin`

_Increase or decrease isolated margin_

Rate limit: 100 requests per 10 seconds. Only Hyperliquid isolated futures positions are supported. Positive values increase margin, while negative values decrease margin

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexIsolatedMarginRequest | Optional | none  
symbol | body | string | Required | Hyperliquid futures trading pair  
margin | body | string | Required | Margin adjustment amount. Positive values increase margin, while negative values decrease margin. Values with more than two decimal places are truncated to two decimal places  
position_side | body | string | Optional | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
position_side | NONE  
position_side | LONG  
position_side | SHORT  
  
####  Request Body Schema

Request body for increasing or decreasing isolated margin

Request Body SchemaType | Constraints  
---|---  
CrossexIsolatedMarginRequest | required: ["symbol","margin"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Hyperliquid futures trading pair  
margin | string | Required |  | Margin adjustment amount. Positive values increase margin, while negative values decrease margin. Values with more than two decimal places are truncated to two decimal places  
position_side | string | Optional | enum: ["NONE","LONG","SHORT"] | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexIsolatedMarginResponse  
  
### Response Schema

Status Code **202**

CrossexIsolatedMarginResponse

Type | Constraints  
---|---  
CrossexIsolatedMarginResponse | required: ["symbol","margin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Futures trading pair  
margin | string | Required |  | Amount of isolated margin increased or decreased in this request  
position_side | string | Optional |  | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted  
  
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
    
    url = '/crossex/positions/margin'
    query_param = ''
    body='{"symbol":"HYPERLIQUID_FUTURE_CXMT_USDC","margin":"-30","position_side":"NONE"}'
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
    url="/crossex/positions/margin"
    query_param=""
    body_param='{"symbol":"HYPERLIQUID_FUTURE_CXMT_USDC","margin":"-30","position_side":"NONE"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin": "-30",
      "position_side": "NONE"
    }
    

> Example responses

> 202 Response
    
    
    {
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin": "-30",
      "position_side": "NONE"
    }
    

##  Query margin asset interest rates🔒 Authenticated

GET`/crossex/interest_rate`

GET `/crossex/interest_rate`

_Query margin asset interest rates_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
coin | query | string | Optional | Query by specified currency name  
exchange_type | query | string | Optional | Exchange  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexInterestRate

Type | Constraints  
---|---  
object | required: ["coin","exchange_type","hour_interest_rate","time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  | Currency  
exchange_type | string | Required |  | Exchange  
hour_interest_rate | string | Required |  | Hourly Interest Rate  
time | string | Required |  | Millisecond Timestamp  
  
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
    
    url = '/crossex/interest_rate'
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
    url="/crossex/interest_rate"
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
        "coin": "BCH",
        "exchange_type": "GATE",
        "hour_interest_rate": "0.00000485",
        "time": "1763971200000"
      },
      {
        "coin": "ADA",
        "exchange_type": "BINANCE",
        "hour_interest_rate": "0.0000036558334",
        "time": "1763971200000"
      },
      {
        "coin": "BCH",
        "exchange_type": "OKX",
        "hour_interest_rate": "0.00000115",
        "time": "1763971200000"
      }
    ]
    

##  Query User Fee Rates🔒 Authenticated

GET`/crossex/fee`

GET `/crossex/fee`

_Query User Fee Rates_

Rate Limit: 200 requests per 10 seconds

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

CrossexFee

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
object | required: ["spot_maker_fee","spot_taker_fee","future_maker_fee","future_taker_fee","special_fee_list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
exchange_type | string | Optional |  | Exchange  
spot_maker_fee | string | Required |  | spotMakerfee rate  
spot_taker_fee | string | Required |  | spotTakerfee rate  
spot_rpi_maker_fee | string | Optional |  | Spot RPI order maker fee rate  
future_maker_fee | string | Required |  | contractMakerfee rate  
future_taker_fee | string | Required |  | contractTakerfee rate  
future_rpi_maker_fee | string | Optional |  | Futures RPI order maker fee rate  
special_fee_list | array | Required |  |   
  
**items / special_fee_list**

Type | Constraints  
---|---  
array |   
  
**items / special_fee_list / items**

CrossexSpecialFee

Type | Constraints  
---|---  
object | required: ["symbol","taker_fee_rate","maker_fee_rate"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Currency pair  
taker_fee_rate | string | Required |  | Taker fee rate  
maker_fee_rate | string | Required |  | Maker fee rate  
rpi_fee_rate | string | Optional |  | RPI order maker fee rate  
  
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
    
    url = '/crossex/fee'
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
    url="/crossex/fee"
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
        "exchange_type": "BINANCE",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": "",
        "special_fee_list": []
      },
      {
        "exchange_type": "OKX",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": "",
        "special_fee_list": [
          {
            "symbol": "OKX_SPOT_FLOW_USDT",
            "taker_fee_rate": "0.0004",
            "maker_fee_rate": "0.0001"
          }
        ]
      },
      {
        "exchange_type": "GATE",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": "",
        "special_fee_list": []
      },
      {
        "exchange_type": "BYBIT",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": "",
        "special_fee_list": [
          {
            "symbol": "BYBIT_FUTURE_BLAST_USDT",
            "taker_fee_rate": "0.00029",
            "maker_fee_rate": "0.00006"
          }
        ]
      },
      {
        "exchange_type": "KRAKEN",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": ""
      },
      {
        "exchange_type": "HYPERLIQUID",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": ""
      },
      {
        "exchange_type": "DERIBIT",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": ""
      },
      {
        "exchange_type": "LIGHTER",
        "spot_maker_fee": "0.0005",
        "spot_taker_fee": "0.0005",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00005",
        "future_taker_fee": "0.00005",
        "future_rpi_maker_fee": ""
      }
    ]
    

##  Query Contract Positions🔒 Authenticated

GET`/crossex/positions`

GET `/crossex/positions`

_Query Contract Positions_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | query | string | Optional | Trading Pair  
exchange_type | query | string | Optional | Exchange  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexPosition

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Optional |  | User ID  
position_id | string | Optional |  | Position ID  
symbol | string | Optional |  | Currency pair  
position_side | string | Optional |  | Position Direction  
initial_margin | string | Optional |  | Initial Margin  
isolated_margin | string | Optional |  | Isolated margin. It is 0 in cross margin mode and applies only to isolated margin positions  
margin_mode | string | Optional |  | Margin mode (CROSS/ISOLATED)  
maintenance_margin | string | Optional |  | Maintenance margin  
position_qty | string | Optional |  | Position Quantity  
position_value | string | Optional |  | Position Value  
upnl | string | Optional |  | Unrealized P&L  
upnl_rate | string | Optional |  | Unrealized P&L Ratio  
entry_price | string | Optional |  | Position Average Entry Price  
liq_price | string | Optional |  | Liquidation price. It is 0 in cross margin mode and applies only to isolated margin positions; 0 in isolated margin mode means the position will not be liquidated  
mark_price | string | Optional |  | Mark price  
leverage | string | Optional |  | Position Leverage  
max_leverage | string | Optional |  | Maximum leverage  
risk_limit | string | Optional |  | Position risk limit  
fee | string | Optional |  | Position Fee  
funding_fee | string | Optional |  | Accumulated position funding fee. A positive value indicates a gain, while a negative value indicates a loss.  
funding_time | string | Optional |  | Position funding fee collection time (0 indicates it has not been collected yet)  
create_time | string | Optional |  | Position Creation Time  
update_time | string | Optional |  | Position Update Time  
closed_pnl | string | Optional |  | Realized PnL  
  
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
    
    url = '/crossex/positions'
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
    url="/crossex/positions"
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
        "user_id": "10001004",
        "position_id": "20062926505289216",
        "symbol": "OKX_FUTURE_ADA_USDT",
        "position_side": "LONG",
        "initial_margin": "5.79934625",
        "isolated_margin": "0",
        "margin_mode": "CROSS",
        "maintenance_margin": "0.06229625",
        "position_qty": "10",
        "position_value": "5.795",
        "upnl": "0.369",
        "upnl_rate": "0.068005897530409141",
        "entry_price": "0.5426",
        "liq_price": "0",
        "mark_price": "0.5795",
        "leverage": "1",
        "max_leverage": "18",
        "risk_limit": "1",
        "fee": "0.002713",
        "funding_fee": "0",
        "funding_time": "0",
        "create_time": "1750682334273",
        "update_time": "1750730699867",
        "closed_pnl": "12"
      }
    ]
    

##  List security positions🔒 Authenticated

GET`/crossex/security_positions`

GET `/crossex/security_positions`

_List security positions_

List stock and ETF positions. Rate limit: 200 requests per 10 seconds. Prices, position values, and unrealized profit and loss use the listing market currency: USD for US markets, HKD for Hong Kong, KRW for South Korea, and JPY for Japan.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | query | string | Optional | Stock or ETF trading pair  
exchange_type | query | string | Optional | Stock market (US/HK/KR/JP)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexSecurityPosition

Type | Constraints  
---|---  
object | required: ["user_id","symbol","price","entry_price","diluted_cost_price","upnl","position_qty","position_value"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
symbol | string | Required |  | Stock or ETF trading pair  
price | string | Required |  | Latest price in the listing market currency  
entry_price | string | Required |  | Position cost price in the listing market currency  
diluted_cost_price | string | Required |  | Diluted cost price in the listing market currency  
upnl | string | Required |  | Unrealized profit and loss in the listing market currency  
position_qty | string | Required |  | Position size  
position_value | string | Required |  | Position value in the listing market currency  
  
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
    
    url = '/crossex/security_positions'
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
    url="/crossex/security_positions"
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
        "user_id": "59138103",
        "symbol": "HK_STOCK_00700_USDT",
        "price": "424.8",
        "entry_price": "428",
        "diluted_cost_price": "428",
        "upnl": "-0.032",
        "position_qty": "0.01",
        "position_value": "4.248"
      }
    ]
    

##  Query Leveraged Positions🔒 Authenticated

GET`/crossex/margin_positions`

GET `/crossex/margin_positions`

_Query Leveraged Positions_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | query | string | Optional | Currency pair  
exchange_type | query | string | Optional | Exchange  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexMarginPosition

Type | Constraints  
---|---  
object | required: ["user_id","position_id","symbol","position_side","initial_margin","maintenance_margin","asset_qty","asset_coin","position_value","liability","liability_coin","interest","max_position_qty","entry_price","index_price","upnl","upnl_rate","leverage","max_leverage","create_time","update_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
position_id | string | Required |  | Leveraged Position ID  
symbol | string | Required |  | Trading Pair  
position_side | string | Required |  | Position Direction  
initial_margin | string | Required |  | Initial position margin  
maintenance_margin | string | Required |  | Position maintenance margin  
asset_qty | string | Required |  | Position Asset Quantity  
asset_coin | string | Required |  | Position Asset Currency  
position_value | string | Required |  | Position Value  
liability | string | Required |  | Debt Quantity  
liability_coin | string | Required |  | Debt Currency  
interest | string | Required |  | Deducted Interest  
max_position_qty | string | Required |  | Max Trade Size  
entry_price | string | Required |  | Position Cost Price (Average Opening Price)  
index_price | string | Required |  | Index price  
upnl | string | Required |  | Unrealized P&L  
upnl_rate | string | Required |  | Unrealized P&L Ratio  
leverage | string | Required |  | Opening Leverage  
max_leverage | string | Required |  | Maximum leverage  
create_time | string | Required |  | Created time  
update_time | string | Required |  | Update time  
  
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
    
    url = '/crossex/margin_positions'
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
    url="/crossex/margin_positions"
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
        "user_id": "12345",
        "position_id": "20126312530221056",
        "symbol": "BINANCE_MARGIN_ADA_USDT",
        "position_side": "LONG",
        "initial_margin": "0",
        "maintenance_margin": "0",
        "asset_qty": "0",
        "asset_coin": "ADA",
        "position_value": "0",
        "liability": "0.0001708920658",
        "liability_coin": "USDT",
        "interest": "0.0001708920658",
        "max_position_qty": "0",
        "entry_price": "0",
        "index_price": "0.35466844",
        "upnl": "-0.0001708920658",
        "upnl_rate": "-3",
        "leverage": "3",
        "max_leverage": "5",
        "create_time": "1765794740152",
        "update_time": "1766716075010"
      }
    ]
    

##  Query ADL Position Reduction Ranking🔒 Authenticated

GET`/crossex/adl_rank`

GET `/crossex/adl_rank`

_Query ADL Position Reduction Ranking_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | query | string | Required | Trading Pair  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline  
  
### Response Schema

Status Code **200**

CrossexAdlRank

Type | Constraints  
---|---  
object | required: ["user_id","symbol","crossex_adl_rank","exchange_adl_rank"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
symbol | string | Required |  | Currency pair  
crossex_adl_rank | string | Required |  | CrossEx ADL priority, with values from 1 to 5  
Priority from highest to lowest: 5, 4, 3, 2, 1  
exchange_adl_rank | string | Required |  | Raw exchange ADL rank. Priority order from highest to lowest by exchange:  
\- BINANCE: 4, 3, 2, 1, 0  
\- OKX: 5, 4, 3, 2, 1, 0  
\- GATE: 1, 2, 3, 4, 5  
\- Kraken: 20, 40, 60, 80, 100  
\- BYBIT: 5, 4, 3, 2, 1, 0  
  
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
    
    url = '/crossex/adl_rank'
    query_param = 'symbol=BINANCE_FUTURE_ADA_USDT'
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
    url="/crossex/adl_rank"
    query_param="symbol=BINANCE_FUTURE_ADA_USDT"
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
        "user_id": "111",
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "crossex_adl_rank": "1",
        "exchange_adl_rank": "1"
      }
    ]
    

##  Query All Current Open Orders🔒 Authenticated

GET`/crossex/open_orders`

GET `/crossex/open_orders`

_Query All Current Open Orders_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | query | string | Optional | Trading Pair  
exchange_type | query | string | Optional | Exchange  
business_type | query | string | Optional | Business Type  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [CrossexOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexOrder

Type | Constraints  
---|---  
CrossexOrder | required: ["user_id","order_id","text","state","symbol","side","type","exchange_type","attribute","executed_avg_price","executed_amount","executed_qty","time_in_force","price","quote_qty","qty","business_type","fee","fee_coin","reduce_only","leverage","last_executed_price","last_executed_qty","reason","position_side","last_executed_amount","update_time","create_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
order_id | string | Required |  | Order ID  
text | string | Required |  | Client-defined order ID.  
state | string | Required |  | Order status:  
`NEW`: validated locally, pending submission to the exchange  
`OPEN`: resting on the exchange order book  
`PARTIALLY_FILLED`: partially filled  
`FILLED`: fully filled  
`FAIL`: CrossEx validation failed; see `reason`  
`REJECT`: rejected by the exchange; see `reason`  
`CANCELLED`: cancelled  
symbol | string | Required |  | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
side | string | Required |  | Side (`BUY` buy / `SELL` sell).  
type | string | Required |  | Order type (`LIMIT` limit / `MARKET` market).  
attribute | string | Required |  | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
exchange_type | string | Required |  | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
business_type | string | Required |  | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)  
qty | string | Required |  | Order quantity in the base currency.  
quote_qty | string | Required |  | Order quantity in the quote currency.  
price | string | Required |  | Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
time_in_force | string | Required |  | Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)  
executed_qty | string | Required |  | Filled base amount.  
executed_amount | string | Required |  | Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
executed_avg_price | string | Required |  | Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
fee_coin | string | Required |  | Fee currency  
fee | string | Required |  | Fee amount.  
reduce_only | string | Required |  | Reduce-only order (`"true"` or `"false"`).  
leverage | string | Required |  | Order leverage multiplier.  
reason | string | Required |  | Failure reason description.  
last_executed_qty | string | Required |  | Base quantity of the latest fill.  
last_executed_price | string | Required |  | Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
last_executed_amount | string | Required |  | Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
position_side | string | Required |  | Position side (`NONE` one-way position / `LONG` long / `SHORT` short)  
create_time | string | Required |  | Created time  
update_time | string | Required |  | Update time  
  
**items / user_id**

User ID

User ID

Type | Constraints  
---|---  
string |   
  
**items / order_id**

Order ID

Order ID

Type | Constraints  
---|---  
string |   
  
**items / text**

Client Order ID

Client-defined order ID.

Type | Constraints  
---|---  
string |   
  
**items / state**

Order status

Order status: `NEW`: validated locally, pending submission to the exchange `OPEN`: resting on the exchange order book `PARTIALLY_FILLED`: partially filled `FILLED`: fully filled `FAIL`: CrossEx validation failed; see `reason` `REJECT`: rejected by the exchange; see `reason` `CANCELLED`: cancelled

Type | Constraints  
---|---  
string |   
  
**items / symbol**

Currency pair

Unique trading pair identifiers, e.g. `BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.

Type | Constraints  
---|---  
string |   
  
**items / side**

direction

Side (`BUY` buy / `SELL` sell).

Type | Constraints  
---|---  
string |   
  
**items / type**

Type

Order type (`LIMIT` limit / `MARKET` market).

Type | Constraints  
---|---  
string |   
  
**items / attribute**

Attribute COMMON: Normal Order, LIQ: Liquidation Takeover Order, REDUCE: Liquidation Reduce Order, ADL: Auto-Reduce

Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).

Type | Constraints  
---|---  
string |   
  
**items / exchange_type**

Exchange

Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)

Type | Constraints  
---|---  
string |   
  
**items / business_type**

Business Type

Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)

Type | Constraints  
---|---  
string |   
  
**items / qty**

Base Currency Quantity

Order quantity in the base currency.

Type | Constraints  
---|---  
string |   
  
**items / quote_qty**

Quote Currency Quantity

Order quantity in the quote currency.

Type | Constraints  
---|---  
string |   
  
**items / price**

Price

Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / time_in_force**

Time in Force Strategy

Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)

Type | Constraints  
---|---  
string |   
  
**items / executed_qty**

Filled quantity

Filled base amount.

Type | Constraints  
---|---  
string |   
  
**items / executed_amount**

Filled Amount

Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / executed_avg_price**

Average Filled Price

Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / fee_coin**

Fee currency

Fee currency

Type | Constraints  
---|---  
string |   
  
**items / fee**

fee

Fee amount.

Type | Constraints  
---|---  
string |   
  
**items / reduce_only**

Reduce Position Only

Reduce-only order (`"true"` or `"false"`).

Type | Constraints  
---|---  
string |   
  
**items / leverage**

Leverage

Order leverage multiplier.

Type | Constraints  
---|---  
string |   
  
**items / reason**

Reason

Failure reason description.

Type | Constraints  
---|---  
string |   
  
**items / last_executed_qty**

Latest Filled Quantity

Base quantity of the latest fill.

Type | Constraints  
---|---  
string |   
  
**items / last_executed_price**

Latest Filled Price

Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / last_executed_amount**

Latest Filled Amount

Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / position_side**

Position Direction

Position side (`NONE` one-way position / `LONG` long / `SHORT` short)

Type | Constraints  
---|---  
string |   
  
**items / create_time**

Created time

Created time

Type | Constraints  
---|---  
string |   
  
**items / update_time**

Update time

Update time

Type | Constraints  
---|---  
string |   
  
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
    
    url = '/crossex/open_orders'
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
    url="/crossex/open_orders"
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
        "user_id": "10001004",
        "order_id": "2048529119934720",
        "client_order_id": "2048529119934720",
        "state": "PARTIALLY_FILLED",
        "symbol": "OKX_SPOT_ADA_USDT",
        "side": "BUY",
        "type": "MARKET",
        "attribute": "COMMON",
        "exchange_type": "OKX",
        "business_type": "SPOT",
        "qty": "6",
        "quote_qty": "6",
        "price": "0",
        "time_in_force": "GTC",
        "executed_qty": "11.0354",
        "executed_amount": "5.99994698",
        "executed_avg_price": "0.5437",
        "fee_coin": "ADA",
        "fee": "0.0110354",
        "reduce_only": "false",
        "leverage": "1",
        "reason": "",
        "last_executed_qty": "11.0354",
        "last_executed_price": "0.5437",
        "last_executed_amount": "5.99994698",
        "position_side": "NONE",
        "create_time": "1750682602377",
        "update_time": "1750682602413"
      }
    ]
    

##  Query order history🔒 Authenticated

GET`/crossex/history_orders`

GET `/crossex/history_orders`

_Query order history_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
symbol | query | string | Optional | Currency pair  
from | query | integer | Optional | Start Millisecond Timestamp  
to | query | integer | Optional | End Millisecond Timestamp  
attributes | query | string | Optional | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement). Multiple values, comma-separated.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [CrossexOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexOrder

Type | Constraints  
---|---  
CrossexOrder | required: ["user_id","order_id","text","state","symbol","side","type","exchange_type","attribute","executed_avg_price","executed_amount","executed_qty","time_in_force","price","quote_qty","qty","business_type","fee","fee_coin","reduce_only","leverage","last_executed_price","last_executed_qty","reason","position_side","last_executed_amount","update_time","create_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
order_id | string | Required |  | Order ID  
text | string | Required |  | Client-defined order ID.  
state | string | Required |  | Order status:  
`NEW`: validated locally, pending submission to the exchange  
`OPEN`: resting on the exchange order book  
`PARTIALLY_FILLED`: partially filled  
`FILLED`: fully filled  
`FAIL`: CrossEx validation failed; see `reason`  
`REJECT`: rejected by the exchange; see `reason`  
`CANCELLED`: cancelled  
symbol | string | Required |  | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
side | string | Required |  | Side (`BUY` buy / `SELL` sell).  
type | string | Required |  | Order type (`LIMIT` limit / `MARKET` market).  
attribute | string | Required |  | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
exchange_type | string | Required |  | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
business_type | string | Required |  | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)  
qty | string | Required |  | Order quantity in the base currency.  
quote_qty | string | Required |  | Order quantity in the quote currency.  
price | string | Required |  | Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
time_in_force | string | Required |  | Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)  
executed_qty | string | Required |  | Filled base amount.  
executed_amount | string | Required |  | Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
executed_avg_price | string | Required |  | Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
fee_coin | string | Required |  | Fee currency  
fee | string | Required |  | Fee amount.  
reduce_only | string | Required |  | Reduce-only order (`"true"` or `"false"`).  
leverage | string | Required |  | Order leverage multiplier.  
reason | string | Required |  | Failure reason description.  
last_executed_qty | string | Required |  | Base quantity of the latest fill.  
last_executed_price | string | Required |  | Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
last_executed_amount | string | Required |  | Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
position_side | string | Required |  | Position side (`NONE` one-way position / `LONG` long / `SHORT` short)  
create_time | string | Required |  | Created time  
update_time | string | Required |  | Update time  
  
**items / user_id**

User ID

User ID

Type | Constraints  
---|---  
string |   
  
**items / order_id**

Order ID

Order ID

Type | Constraints  
---|---  
string |   
  
**items / text**

Client Order ID

Client-defined order ID.

Type | Constraints  
---|---  
string |   
  
**items / state**

Order status

Order status: `NEW`: validated locally, pending submission to the exchange `OPEN`: resting on the exchange order book `PARTIALLY_FILLED`: partially filled `FILLED`: fully filled `FAIL`: CrossEx validation failed; see `reason` `REJECT`: rejected by the exchange; see `reason` `CANCELLED`: cancelled

Type | Constraints  
---|---  
string |   
  
**items / symbol**

Currency pair

Unique trading pair identifiers, e.g. `BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.

Type | Constraints  
---|---  
string |   
  
**items / side**

direction

Side (`BUY` buy / `SELL` sell).

Type | Constraints  
---|---  
string |   
  
**items / type**

Type

Order type (`LIMIT` limit / `MARKET` market).

Type | Constraints  
---|---  
string |   
  
**items / attribute**

Attribute COMMON: Normal Order, LIQ: Liquidation Takeover Order, REDUCE: Liquidation Reduce Order, ADL: Auto-Reduce

Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).

Type | Constraints  
---|---  
string |   
  
**items / exchange_type**

Exchange

Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)

Type | Constraints  
---|---  
string |   
  
**items / business_type**

Business Type

Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)

Type | Constraints  
---|---  
string |   
  
**items / qty**

Base Currency Quantity

Order quantity in the base currency.

Type | Constraints  
---|---  
string |   
  
**items / quote_qty**

Quote Currency Quantity

Order quantity in the quote currency.

Type | Constraints  
---|---  
string |   
  
**items / price**

Price

Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / time_in_force**

Time in Force Strategy

Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)

Type | Constraints  
---|---  
string |   
  
**items / executed_qty**

Filled quantity

Filled base amount.

Type | Constraints  
---|---  
string |   
  
**items / executed_amount**

Filled Amount

Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / executed_avg_price**

Average Filled Price

Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / fee_coin**

Fee currency

Fee currency

Type | Constraints  
---|---  
string |   
  
**items / fee**

fee

Fee amount.

Type | Constraints  
---|---  
string |   
  
**items / reduce_only**

Reduce Position Only

Reduce-only order (`"true"` or `"false"`).

Type | Constraints  
---|---  
string |   
  
**items / leverage**

Leverage

Order leverage multiplier.

Type | Constraints  
---|---  
string |   
  
**items / reason**

Reason

Failure reason description.

Type | Constraints  
---|---  
string |   
  
**items / last_executed_qty**

Latest Filled Quantity

Base quantity of the latest fill.

Type | Constraints  
---|---  
string |   
  
**items / last_executed_price**

Latest Filled Price

Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / last_executed_amount**

Latest Filled Amount

Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**items / position_side**

Position Direction

Position side (`NONE` one-way position / `LONG` long / `SHORT` short)

Type | Constraints  
---|---  
string |   
  
**items / create_time**

Created time

Created time

Type | Constraints  
---|---  
string |   
  
**items / update_time**

Update time

Update time

Type | Constraints  
---|---  
string |   
  
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
    
    url = '/crossex/history_orders'
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
    url="/crossex/history_orders"
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
        "user_id": "10001004",
        "order_id": "2048522992198912",
        "text": "2048522992198912",
        "state": "FILLED",
        "symbol": "BINANCE_SPOT_ADA_USDT",
        "side": "BUY",
        "type": "MARKET",
        "attribute": "COMMON",
        "exchange_type": "BINANCE",
        "business_type": "SPOT",
        "qty": "0",
        "quote_qty": "7",
        "price": "0",
        "time_in_force": "GTC",
        "executed_qty": "12.9",
        "executed_amount": "6.96471",
        "executed_avg_price": "0.5399",
        "fee_coin": "ADA",
        "fee": "0.0129",
        "reduce_only": "false",
        "leverage": "1",
        "reason": "",
        "last_executed_qty": "12.9",
        "last_executed_price": "0.5399",
        "last_executed_amount": "6.96471",
        "position_side": "NONE",
        "create_time": "1750681141933",
        "update_time": "1750681142379"
      }
    ]
    

##  Query Contract Position History🔒 Authenticated

GET`/crossex/history_positions`

GET `/crossex/history_positions`

_Query Contract Position History_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number returned by list, max 1000  
symbol | query | string | Optional | Currency pair  
from | query | integer | Optional | Start Millisecond Timestamp  
to | query | integer | Optional | End Millisecond Timestamp  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexHistoricalPosition

Type | Constraints  
---|---  
object | required: ["business_type"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
position_id | string | Optional |  | Position ID  
user_id | string | Optional |  | User ID  
symbol | string | Optional |  | Currency pair  
closed_type | string | Optional |  | Position close type (PARTIAL_CLOSED: partially closed; COMPLETE_CLOSED: fully closed)  
closed_pnl | string | Optional |  | Close Position P&L  
closed_pnl_rate | string | Optional |  | Close Position P&L Ratio  
open_avg_price | string | Optional |  | Average Opening Price  
closed_avg_price | string | Optional |  | Average Close Price  
max_position_qty | string | Optional |  | Max Trade Size  
closed_qty | string | Optional |  | Close Position Quantity  
closed_value | string | Optional |  | Close Position Value  
fee | string | Optional |  | Position Accumulated Fees  
liq_fee | string | Optional |  | Liquidation Fee  
funding_fee | string | Optional |  | Funding Fee  
position_side | string | Optional |  | Position Direction Before Close  
position_mode | string | Optional |  | Position Mode at Close  
leverage | string | Optional |  | Leverage at Close  
margin_mode | string | Optional |  | Margin mode (CROSS/ISOLATED)  
business_type | string | Required |  | Business Type  
create_time | string | Optional |  | Created time  
update_time | string | Optional |  | Update time  
  
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
    
    url = '/crossex/history_positions'
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
    url="/crossex/history_positions"
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
        "position_id": "20064013106942976",
        "user_id": "12345678",
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "closed_type": "COMPLETE_CLOSED",
        "closed_pnl": "-0.001",
        "closed_pnl_rate": "-0.001",
        "open_avg_price": "0.5598",
        "closed_avg_price": "0.5597",
        "max_position_qty": "10",
        "closed_qty": "10",
        "closed_value": "5.597",
        "fee": "0.0055975",
        "liq_fee": "0",
        "funding_fee": "0",
        "position_side": "LONG",
        "position_mode": "DUAL",
        "leverage": "1",
        "create_time": "1750941400632",
        "update_time": "1750941402661",
        "margin_mode": "CROSS"
      }
    ]
    

##  Query Leveraged Position History🔒 Authenticated

GET`/crossex/history_margin_positions`

GET `/crossex/history_margin_positions`

_Query Leveraged Position History_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number returned by list, max 1000  
symbol | query | string | Optional | Currency pair  
from | query | integer | Optional | Start Millisecond Timestamp  
to | query | integer | Optional | End Millisecond Timestamp  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexHistoricalMarginPosition

Type | Constraints  
---|---  
object | required: ["business_type","interest"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
position_id | string | Optional |  | Position ID  
user_id | string | Optional |  | User ID  
symbol | string | Optional |  | Currency pair  
closed_type | string | Optional |  | Position close type (PARTIAL_CLOSED: partially closed; COMPLETE_CLOSED: fully closed)  
closed_pnl | string | Optional |  | Close Position P&L  
closed_pnl_rate | string | Optional |  | Close Position P&L Ratio  
open_avg_price | string | Optional |  | Average Opening Price  
closed_avg_price | string | Optional |  | Average Close Price  
max_position_qty | string | Optional |  | Max Trade Size  
closed_qty | string | Optional |  | Close Position Quantity  
closed_value | string | Optional |  | Close Position Value  
liq_fee | string | Optional |  | Liquidation Fee  
position_side | string | Optional |  | Position Direction Before Close  
leverage | string | Optional |  | Leverage at Close  
interest | string | Required |  | Accumulated position interest  
business_type | string | Required |  | Position Business Type  
create_time | string | Optional |  | Created time  
update_time | string | Optional |  | Update time  
  
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
    
    url = '/crossex/history_margin_positions'
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
    url="/crossex/history_margin_positions"
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
        "position_id": "20064013106942976",
        "user_id": "12345678",
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "closed_type": "COMPLETE_CLOSED",
        "closed_pnl": "-0.001",
        "closed_pnl_rate": "-0.001",
        "open_avg_price": "0.5598",
        "closed_avg_price": "0.5597",
        "max_position_qty": "10",
        "closed_qty": "10",
        "closed_value": "5.597",
        "liq_fee": "0",
        "position_side": "LONG",
        "leverage": "1",
        "interest": "0.2",
        "business_type": "MARGIN",
        "create_time": "1750941400632",
        "update_time": "1750941402661"
      }
    ]
    

##  Query Leveraged Interest Deduction History🔒 Authenticated

GET`/crossex/history_margin_interests`

GET `/crossex/history_margin_interests`

_Query Leveraged Interest Deduction History_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbol | query | string | Optional | Currency pair  
from | query | integer | Optional | Start Millisecond Timestamp  
to | query | integer | Optional | End Millisecond Timestamp  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number returned by list, max 1000  
exchange_type | query | string | Optional | Exchange  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexMarginInterestRecord

Type | Constraints  
---|---  
object | required: ["user_id","symbol","interest_id","liability_id","liability","liability_coin","interest","interest_rate","interest_type","create_time","exchange_type"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
symbol | string | Required |  | Trading Pair  
interest_id | string | Required |  | Interest Deduction ID  
liability_id | string | Required |  | Debt Source ID, can be Order ID or Position ID  
liability | string | Required |  | Debt Quantity  
liability_coin | string | Required |  | Debt Currency  
interest | string | Required |  | Interest  
interest_rate | string | Required |  | interest rate  
interest_type | string | Required |  | Interest deduction type  
`PERIODIC_POSITION`: hourly interest charged on positions  
`PERIODIC_OPEN_ORDER`: hourly interest charged on open orders  
`IMMEDIATE_OPEN_ORDER`: interest charged when an order is placed  
`PERIODIC_ISOLATED`: hourly interest charged on liabilities  
create_time | string | Required |  | Created time  
exchange_type | string | Required |  | Exchange  
  
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
    
    url = '/crossex/history_margin_interests'
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
    url="/crossex/history_margin_interests"
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
        "user_id": "2124575357",
        "symbol": "OKX_MARGIN_WLD_USDT",
        "interest_id": "2115944013038336",
        "liability_id": "2115944013038080",
        "liability": "2",
        "liability_coin": "USDT",
        "interest": "0.00000732",
        "interest_rate": "0.00000366",
        "interest_type": "IMMEDIATE_OPEN_ORDER",
        "create_time": "1766755565807",
        "exchange_type": "OKX"
      },
      {
        "user_id": "2124575357",
        "symbol": "OKX_MARGIN_WLD_USDT",
        "interest_id": "2114666587422976",
        "liability_id": "2114666587422720",
        "liability": "2",
        "liability_coin": "USDT",
        "interest": "0.00000732",
        "interest_rate": "0.00000366",
        "interest_type": "IMMEDIATE_OPEN_ORDER",
        "create_time": "1766451003780",
        "exchange_type": "OKX"
      }
    ]
    

##  Query filled history🔒 Authenticated

GET`/crossex/history_trades`

GET `/crossex/history_trades`

_Query filled history_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number returned by list, max 1000  
symbol | query | string | Optional | Currency pair  
from | query | integer | Optional | Start Millisecond Timestamp  
to | query | integer | Optional | End Millisecond Timestamp  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexTrade

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Optional |  | User ID  
transaction_id | string | Optional |  | filledrecordsID  
order_id | string | Optional |  | Order ID  
text | string | Optional |  | User Order ID  
symbol | string | Optional |  | Currency pair  
exchange_type | string | Optional |  | Exchange  
business_type | string | Optional |  | Business Type  
side | string | Optional |  | Buy/Sell Direction  
qty | string | Optional |  | Trading size  
price | string | Optional |  | Fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
fee | string | Optional |  | fee  
fee_coin | string | Optional |  | Fee currency  
fee_rate | string | Optional |  | Fee Rate  
match_role | string | Optional |  | Filled Role  
rpnl | string | Optional |  | Realized P&L  
position_mode | string | Optional |  | Position Mode  
position_side | string | Optional |  | Position Direction  
create_time | string | Optional |  | Created time  
  
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
    
    url = '/crossex/history_trades'
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
    url="/crossex/history_trades"
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
        "user_id": "3511316454450547",
        "transaction_id": "2049614605858560",
        "order_id": "2049614605857536",
        "text": "2049614605857536",
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "exchange_type": "BINANCE",
        "business_type": "FUTURE",
        "side": "SELL",
        "qty": "10",
        "price": "0.5597",
        "fee": "0.002798500000000000",
        "fee_coin": "USDT",
        "fee_rate": "0.0005",
        "match_role": "MAKER",
        "rpnl": "-0.001",
        "position_mode": "DUAL",
        "position_side": "LONG",
        "create_time": "1750941402661"
      }
    ]
    

##  Query Account Asset Change History🔒 Authenticated

GET`/crossex/account_book`

GET `/crossex/account_book`

_Query Account Asset Change History_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number returned by list, max 1000  
coin | query | string | Optional | Query by specified currency name  
statement_type | query | string | Optional | Bill entry type. The filter accepts the same values returned in the response.  
from | query | integer | Optional | Start Millisecond Timestamp  
to | query | integer | Optional | End Millisecond Timestamp  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexAccountBookRecord

Type | Constraints  
---|---  
object | required: ["user_id","business_id","statement_type","exchange_type","change","balance","create_time","id","coin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required |  | Account Change Record ID  
user_id | string | Required |  | User ID  
business_id | string | Required |  | Business ID. Its meaning varies by `statement_type`.  
TRANSACTION: order ID  
TRADING_FEE: order ID  
LIQUIDATION_FEE: liquidation order ID  
FUNDING_FEE: position ID and funding fee settlement time  
For other types, it is a system-generated processing ID with no business meaning  
statement_type | string | Required |  | Bill entry type.  
exchange_type | string | Required |  | Exchange  
coin | string | Required |  | Currency  
symbol | string | Optional |  | Trading Pair  
change | string | Required |  | Change amount (positive values indicate an increase; negative values indicate a decrease)  
balance | string | Required |  | Balance after change  
create_time | string | Required |  | Created time  
  
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
    
    url = '/crossex/account_book'
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
    url="/crossex/account_book"
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
        "id": "121",
        "user_id": "12345678",
        "business_id": "20818182821",
        "statement_type": "FUNDING_FEE",
        "exchange_type": "BINANCE",
        "coin": "USDT",
        "symbol": "BINANCE_FUTURE_BTC_USDT",
        "change": "-0.002",
        "balance": "81",
        "create_time": "1750941402661"
      }
    ]
    

##  Query Currency Discount Rate🔒 Authenticated

GET`/crossex/coin_discount_rate`

GET `/crossex/coin_discount_rate`

_Query Currency Discount Rate_

Rate Limit: 200 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
coin | query | string | Optional | Query by specified currency name  
exchange_type | query | string | Optional | OKX/GATE/BINANCE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT/LIGHTER  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

CrossexCoinDiscountRate

Type | Constraints  
---|---  
object | required: ["coin","exchange_type","tier","min_value","max_value","discount_rate"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  | Currency  
exchange_type | string | Required |  | Exchange  
tier | string | Required |  | Tier  
min_value | string | Required |  | Minimum value  
max_value | string | Required |  | Maximum value  
discount_rate | string | Required |  | Discount rate  
  
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
    
    url = '/crossex/coin_discount_rate'
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
    url="/crossex/coin_discount_rate"
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
        "coin": "SOL",
        "exchange_type": "GATE",
        "tier": "1",
        "min_value": "0",
        "max_value": "10000",
        "discount_rate": "0.95"
      },
      {
        "coin": "SOL",
        "exchange_type": "GATE",
        "tier": "2",
        "min_value": "10000",
        "max_value": "20000",
        "discount_rate": "0.93"
      },
      {
        "coin": "SOL",
        "exchange_type": "GATE",
        "tier": "3",
        "min_value": "20000",
        "max_value": "30000",
        "discount_rate": "0.2"
      }
    ]
    

##  Get exchange tickers🔒 Authenticated

GET`/crossex/market/tickers`

GET `/crossex/market/tickers`

_Get exchange tickers_

Rate limit: 1 request per second

  * Margin trading pairs cannot be passed directly as parameters. For example, `GATE_MARGIN_BTC_USDT` is invalid.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Optional | Trading Pair List, multiple separated by commas  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
object | required: ["symbol","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Trading Pair  
last_price | string | Optional |  | Last price  
open_24h | string | Optional |  | 24-hour opening price  
low_24h | string | Optional |  | 24h Low  
high_24h | string | Optional |  | 24h High  
volume_24h_base | string | Optional |  | 24-hour trading volume in base currency  
volume_24h_quote | string | Optional |  | 24-hour trading volume in quote currency  
mark_price | string | Optional |  | Mark price  
index_price | string | Optional |  | Index price  
open_interest | string | Optional |  | Open interest  
open_interest_quote | string | Optional |  | Open interest (in quote currency)  
timestamp | string | Required |  | Update timestamp  
  
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
    
    url = '/crossex/market/tickers'
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
    url="/crossex/market/tickers"
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
        "symbol": "GATE_FUTURE_BTC_USDT",
        "last_price": "64052.4",
        "open_24h": "65144.7",
        "low_24h": "64375",
        "high_24h": "65734.8",
        "volume_24h_base": "31705",
        "volume_24h_quote": "2063128626",
        "mark_price": "65148.9",
        "index_price": "65174.38",
        "open_interest": "65568.2144",
        "open_interest_quote": "4271697043.12416",
        "timestamp": "1785168000000"
      },
      {
        "symbol": "GATE_SPOT_BTC_USDT",
        "last_price": "65179.4",
        "open_24h": "",
        "low_24h": "65744",
        "high_24h": "64410.9",
        "volume_24h_base": "3480.769758",
        "volume_24h_quote": "226794942.82361",
        "mark_price": "",
        "index_price": "",
        "open_interest": "",
        "open_interest_quote": "",
        "timestamp": "1785168000000"
      }
    ]
    

##  Get exchange futures funding rate information🔒 Authenticated

GET`/crossex/market/funding_info`

GET `/crossex/market/funding_info`

_Get exchange futures funding rate information_

Rate limit: 1 request per second

  * For `Deribit`, `funding_rate` is the current real-time rate calculated over an 8-hour period.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Optional | Trading Pair List, multiple separated by commas  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
object | required: ["symbol","funding_rate","funding_interval","funding_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Currency  
funding_rate | string | Required |  | Funding rate  
funding_interval | string | Required |  | Funding interval (in seconds)  
funding_time | string | Required |  | Next funding time (Unix timestamp in milliseconds)  
  
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
    
    url = '/crossex/market/funding_info'
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
    url="/crossex/market/funding_info"
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
        "symbol": "BINANCE_FUTURE_BTC_USDT",
        "funding_rate": "0.00006537",
        "funding_time": "1785168000000",
        "funding_interval": "28800"
      },
      {
        "symbol": "OKX_FUTURE_BTC_USDT",
        "funding_rate": "0.0000543885374247",
        "funding_time": "1785168000000",
        "funding_interval": "28800"
      },
      {
        "symbol": "KRAKEN_FUTURE_BTC_USD",
        "funding_rate": "0.000011898754310345",
        "funding_time": "1785139200000",
        "funding_interval": "3600"
      },
      {
        "symbol": "GATE_FUTURE_BTC_USDT",
        "funding_rate": "0.0001",
        "funding_time": "1785168000000",
        "funding_interval": "28800"
      },
      {
        "symbol": "BYBIT_FUTURE_BTC_USDT",
        "funding_rate": "0.00008708",
        "funding_time": "1785168000000",
        "funding_interval": "28800"
      }
    ]
    

#  Schemas

##  CrossexAccountUpdateResponse

CrossexAccountUpdateResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
position_mode | string | Optional |  | Requested futures position mode to modify (SINGLE/DUAL)  
account_mode | string | Optional |  | Requested account mode to modify (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
exchange_type | string | Optional |  | Exchange targeted by the requested change (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to change futures position mode.  
      
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    
    

##  Symbol

Type | Constraints  
---|---  
object | required: ["symbol","exchange_type","business_type","state","min_size","min_notional","lot_size","tick_size","max_num_orders","max_market_size","max_limit_size","contract_size","liquidation_fee","delist_time","tag"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Unique trading pair identifier in the format ExchangeType_BusinessType_Base_Counter.  
Stocks and ETFs use the market as ExchangeType (US/HK/KR/JP) and STOCK or ETF as the business type, for example US_STOCK_AAPL_USDT, HK_STOCK_00700_USDT, or US_ETF_SPY_USDT.  
exchange_type | string | Required |  | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
business_type | string | Required |  | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / STOCK: stocks / ETF: exchange-traded funds)  
state | string | Required |  | Status (`live` running / `suspend` paused).  
min_size | string | Required |  | Minimum order quantity  
min_notional | string | Required |  | Minimum Order Value  
lot_size | string | Required |  | Quantity Step  
tick_size | string | Required |  | Price Step  
max_num_orders | string | Required |  | maximumopen orderamount  
max_market_size | string | Required |  | Maximum Market Order Quantity  
max_limit_size | string | Required |  | Maximum order quantity for limit orders.  
contract_size | string | Required |  | Contract multiplier (deprecated; quantity is used uniformly)  
liquidation_fee | string | Required |  | Liquidation Fee Rate  
delist_time | string | Required |  | Millisecond timestamp; `0` means not delisted.  
support_rpi | string | Optional |  | Whether RPI order placement is supported (true if supported; false otherwise)  
support_cross | string | Optional |  | Whether cross-margin order placement is supported (true if supported; false otherwise)  
tag | string | Required |  | Tag information. Hyperliquid returns DEX information, stocks and ETFs return the security description, and other businesses return an empty string  
  
**symbol**

Currency pair

Unique trading pair identifier in the format ExchangeType_BusinessType_Base_Counter. Stocks and ETFs use the market as ExchangeType (US/HK/KR/JP) and STOCK or ETF as the business type, for example US_STOCK_AAPL_USDT, HK_STOCK_00700_USDT, or US_ETF_SPY_USDT.

Type | Constraints  
---|---  
string |   
  
**exchange_type**

Exchange

Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)

Type | Constraints  
---|---  
string |   
  
**business_type**

Business Type

Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / STOCK: stocks / ETF: exchange-traded funds)

Type | Constraints  
---|---  
string |   
  
**state**

availablestatus

Status (`live` running / `suspend` paused).

Type | Constraints  
---|---  
string |   
  
**min_size**

Minimum order quantity

Minimum order quantity

Type | Constraints  
---|---  
string |   
  
**min_notional**

Minimum Order Value

Minimum Order Value

Type | Constraints  
---|---  
string |   
  
**lot_size**

Quantity Step

Quantity Step

Type | Constraints  
---|---  
string |   
  
**tick_size**

Price Step

Price Step

Type | Constraints  
---|---  
string |   
  
**max_num_orders**

maximumopen orderamount

maximumopen orderamount

Type | Constraints  
---|---  
string |   
  
**max_market_size**

Maximum Market Order Quantity

Maximum Market Order Quantity

Type | Constraints  
---|---  
string |   
  
**max_limit_size**

Maximum Limit Order Quantity

Maximum order quantity for limit orders.

Type | Constraints  
---|---  
string |   
  
**contract_size**

Contract Size

Contract multiplier (deprecated; quantity is used uniformly)

Type | Constraints  
---|---  
string |   
  
**liquidation_fee**

Liquidation Fee Rate

Liquidation Fee Rate

Type | Constraints  
---|---  
string |   
  
**delist_time**

Delisting Time

Millisecond timestamp; `0` means not delisted.

Type | Constraints  
---|---  
string |   
  
**support_rpi**

Whether RPI order placement is supported

Whether RPI order placement is supported (true if supported; false otherwise)

Type | Constraints  
---|---  
string |   
  
**support_cross**

Whether cross-margin order placement is supported

Whether cross-margin order placement is supported (true if supported; false otherwise)

Type | Constraints  
---|---  
string |   
  
**tag**

Tag

Tag information. Hyperliquid returns DEX information, stocks and ETFs return the security description, and other businesses return an empty string

Type | Constraints  
---|---  
string |   
      
    
    {
      "symbol": "string",
      "exchange_type": "string",
      "business_type": "string",
      "state": "string",
      "min_size": "string",
      "min_notional": "string",
      "lot_size": "string",
      "tick_size": "string",
      "max_num_orders": "string",
      "max_market_size": "string",
      "max_limit_size": "string",
      "contract_size": "string",
      "liquidation_fee": "string",
      "delist_time": "string",
      "support_rpi": "string",
      "support_cross": "string",
      "tag": "string"
    }
    
    

##  CrossexIsolatedMarginResponse

CrossexIsolatedMarginResponse

Type | Constraints  
---|---  
object | required: ["symbol","margin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Futures trading pair  
margin | string | Required |  | Amount of isolated margin increased or decreased in this request  
position_side | string | Optional |  | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted  
      
    
    {
      "symbol": "string",
      "margin": "string",
      "position_side": "string"
    }
    
    

##  CrossexAccountUpdateRequest

Change Account Request Body

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
position_mode | string | Optional |  | Futures position mode (SINGLE/DUAL)  
account_mode | string | Optional |  | Account mode (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
exchange_type | string | Optional |  | Exchange (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to adjust futures position mode.  
      
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    
    

##  CrossexTransferResponse

CrossexTransferResponse

Type | Constraints  
---|---  
object | required: ["tx_id","text"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
tx_id | string | Required |  | Order ID  
text | string | Required |  | User-defined Order ID  
      
    
    {
      "tx_id": "string",
      "text": "string"
    }
    
    

##  CrossexOrderActionResponse

CrossexOrderActionResponse

Type | Constraints  
---|---  
object | required: ["order_id","text"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
text | string | Required |  | User-defined Order ID  
      
    
    {
      "order_id": "string",
      "text": "string"
    }
    
    

##  CrossexOrderRequest

Place Order Request Body

Type | Constraints  
---|---  
object | required: ["symbol","side"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
text | string | Optional |  | Client-defined Order ID, supports letters (a-z), numbers (0-9), symbols (-, _) only  
symbol | string | Required |  | Unique identifier Exchange_Business_Base_Counter  
Examples:  
To place a spot order for ADA/USDT on BINANCE, use `BINANCE_SPOT_ADA_USDT`;  
To place a USDT-margined perpetual futures order for ADA/USDT on OKX, use `OKX_FUTURE_ADA_USDT`;  
To place a spot margin order for ADA/USDT on GATE, use `GATE_MARGIN_ADA_USDT`;  
To place a spot order for ADA/USDT on BYBIT, use `BYBIT_SPOT_ADA_USDT`;  
To place a futures order for ADA/USD on KRAKEN, use `KRAKEN_FUTURE_ADA_USD`;  
To place a futures order for ADA/USDC on HYPERLIQUID, use `HYPERLIQUID_FUTURE_ADA_USDC`;  
To place a futures order for ADA/USDC on DERIBIT, use `DERIBIT_FUTURE_ADA_USDC`;  
To place a futures order for ADA/USDC on LIGHTER, use `LIGHTER_FUTURE_ADA_USDC`;  
To trade US stock AAPL, use `US_STOCK_AAPL_USDT`;  
To trade Hong Kong stock 00700, use `HK_STOCK_00700_USDT`;  
To trade US ETF SPY, use `US_ETF_SPY_USDT`;  
Spot, USDT-margined perpetual futures, spot margin, stock, and ETF orders are supported. BYBIT/DERIBIT do not currently support spot margin orders. KRAKEN, HYPERLIQUID, and LIGHTER do not currently support spot or margin orders. Stocks and ETFs support only cross-exchange account mode  
side | string | Required | enum: ["BUY","SELL"] | BUY, SELL  
type | string | Optional | enum: ["LIMIT","MARKET"]  
default: "LIMIT" | Order type (default: `LIMIT`; supported types: `LIMIT`, `MARKET`)  
time_in_force | string | Optional | enum: ["GTC","IOC","FOK","POC","RPI"]  
default: "GTC" | Defaults to GTC. Supported values: `GTC`, `IOC`, `FOK`, `POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
Stocks and ETFs support only `GTC`  
qty | string | Optional |  | Order quantity (required except for spot and margin market buys; qty is required for stocks and ETFs)  
price | string | Optional |  | Limit order price (required for limit orders). Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
quote_qty | string | Optional |  | Order quote quantity, required for spot and margin market buys. Stock and ETF orders do not support quote_qty  
reduce_only | string | Optional | enum: ["true","false"] | Reduce-only: `true` or `false`  
position_side | string | Optional | enum: ["LONG","SHORT","NONE"] | Position side: `NONE`, `LONG`, `SHORT`  
Defaults to `NONE` (single position mode) if not specified  
      
    
    {
      "text": "string",
      "symbol": "string",
      "side": "BUY",
      "type": "LIMIT",
      "time_in_force": "GTC",
      "qty": "string",
      "price": "string",
      "quote_qty": "string",
      "reduce_only": "true",
      "position_side": "LONG"
    }
    
    

##  CrossexConvertOrderRequest

Flash Swap Transaction Request Body

Type | Constraints  
---|---  
object | required: ["quote_id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
quote_id | string | Required |  | Inquiry ID  
      
    
    {
      "quote_id": "string"
    }
    
    

##  CrossexConvertOrderResponse

CrossexConvertOrderResponse

Type | Constraints  
---|---  
object | required: ["order_id","text"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
text | string | Required |  | Order ID (cannot be customized)  
      
    
    {
      "order_id": "string",
      "text": "string"
    }
    
    

##  CrossexLeverageResponse

CrossexLeverageResponse

Type | Constraints  
---|---  
object | required: ["symbol","leverage"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Currency pair  
leverage | string | Required |  | Requested Modified Leverage  
      
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    
    

##  CrossexMarginModeRequest

Request body for updating the futures position margin mode

Type | Constraints  
---|---  
object | required: ["symbol","margin_mode"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Hyperliquid futures trading pair  
margin_mode | string | Required | enum: ["CROSS","ISOLATED"] | Margin mode (CROSS/ISOLATED)  
      
    
    {
      "symbol": "string",
      "margin_mode": "CROSS"
    }
    
    

##  CrossexAccount

CrossexAccount

Type | Constraints  
---|---  
object | required: ["user_id","available_margin","margin_balance","initial_margin","maintenance_margin","initial_margin_rate","maintenance_margin_rate","position_mode","create_time","update_time","assets"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
available_margin | string | Required |  | Available Margin  
margin_balance | string | Required |  | marginbalance  
initial_margin | string | Required |  | Initial Margin  
maintenance_margin | string | Required |  | Maintenance margin  
initial_margin_rate | string | Required |  | Initial margin rate  
maintenance_margin_rate | string | Required |  | Maintenance margin rate  
position_mode | string | Required |  | Contract Position Mode  
account_limit | string | Optional |  | Account limit  
create_time | string | Required |  | Created time  
update_time | string | Required |  | Update time  
account_mode | string | Optional |  | Account Mode. CROSS_EXCHANGE: Cross-Exchange Mode; ISOLATED_EXCHANGE: Split-Exchange Mode  
exchange_type | string | Optional |  | Exchange Type. When account_mode is CROSS_EXCHANGE, it must be CROSSEX; otherwise, it is another exchange.  
assets | array | Required |  | Asset list: grouped by exchange and currency, returning per-account balances, margin, and PnL details  
  
**assets**

Asset list: grouped by exchange and currency, returning per-account balances, margin, and PnL details

Type | Constraints  
---|---  
array |   
  
**assets / items**

CrossexAccountAsset

Type | Constraints  
---|---  
object | required: ["borrowing_initial_margin","borrowing_maintenance_margin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Optional |  | User ID  
coin | string | Optional |  | Currency  
exchange_type | string | Optional |  | Exchange  
balance | string | Optional |  | Balance  
upnl | string | Optional |  | Unrealized P&L  
equity | string | Optional |  | Net margin equity for the currency  
futures_initial_margin | string | Optional |  | Currency-specific futures initial margin. This value is populated for futures settlement currencies (USDT/USDC/USD)  
futures_maintenance_margin | string | Optional |  | Currency-specific futures maintenance margin. This value is populated for futures settlement currencies (USDT/USDC/USD)  
borrowing_initial_margin | string | Required |  | Currency-specific margin trading initial margin. This value is populated for margin or futures settlement currencies (USDT/USDC/USD)  
borrowing_maintenance_margin | string | Required |  | Currency-specific margin trading maintenance margin. This value is populated for margin or futures settlement currencies (USDT/USDC/USD)  
available_balance | string | Optional |  | Available Balance  
liability | string | Optional |  | Liability for the currency. This value is populated only for USDT, USDC, or USD  
      
    
    {
      "user_id": "string",
      "available_margin": "string",
      "margin_balance": "string",
      "initial_margin": "string",
      "maintenance_margin": "string",
      "initial_margin_rate": "string",
      "maintenance_margin_rate": "string",
      "position_mode": "string",
      "account_limit": "string",
      "create_time": "string",
      "update_time": "string",
      "account_mode": "string",
      "exchange_type": "string",
      "assets": [
        {
          "user_id": "string",
          "coin": "string",
          "exchange_type": "string",
          "balance": "string",
          "upnl": "string",
          "equity": "string",
          "futures_initial_margin": "string",
          "futures_maintenance_margin": "string",
          "borrowing_initial_margin": "string",
          "borrowing_maintenance_margin": "string",
          "available_balance": "string",
          "liability": "string"
        }
      ]
    }
    
    

##  CrossexOrderUpdateRequest

Order Modification Request Body

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
qty | string | Optional |  | modify amount  
price | string | Optional |  | modify price  
      
    
    {
      "qty": "string",
      "price": "string"
    }
    
    

##  CrossexConvertQuoteResponse

CrossexConvertQuoteResponse

Type | Constraints  
---|---  
object | required: ["quote_id","valid_ms","from_coin","to_coin","from_amount","to_amount","price"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
quote_id | string | Required |  | Quote ID  
valid_ms | string | Required |  | Valid time (milliseconds timestamp)  
from_coin | string | Required |  | Asset Sold  
to_coin | string | Required |  | Asset Bought  
from_amount | string | Required |  | Amount to sell  
to_amount | string | Required |  | Amount to buy  
price | string | Required |  | Quoted price  
      
    
    {
      "quote_id": "string",
      "valid_ms": "string",
      "from_coin": "string",
      "to_coin": "string",
      "from_amount": "string",
      "to_amount": "string",
      "price": "string"
    }
    
    

##  CrossexIsolatedMarginRequest

Request body for increasing or decreasing isolated margin

Type | Constraints  
---|---  
object | required: ["symbol","margin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Hyperliquid futures trading pair  
margin | string | Required |  | Margin adjustment amount. Positive values increase margin, while negative values decrease margin. Values with more than two decimal places are truncated to two decimal places  
position_side | string | Optional | enum: ["NONE","LONG","SHORT"] | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted  
      
    
    {
      "symbol": "string",
      "margin": "string",
      "position_side": "NONE"
    }
    
    

##  CrossexBatchCancelOrderRequest

CrossexBatchCancelOrderRequest

Batch cancel orders

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
order_id | string | false |  | Order ID; either this field or text is required  
text | string | false |  | Custom ID specified by the user when creating the order; either this field or order_id is required  
  
**anyOf[0]**

Type | Constraints  
---|---  
any | required: ["order_id"]  
  
**anyOf[1]**

Type | Constraints  
---|---  
any | required: ["text"]  
      
    
    {}
    
    

##  CrossexBatchCancelOrderResponse

CrossexBatchCancelOrderResponse

Batch order cancellation request results

Type | Constraints  
---|---  
object | required: ["order_id","text","accepted","label","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
text | string | Required |  | Custom ID specified by the user when creating the order  
accepted | string | Required |  | Whether the request was accepted, as the string true or false  
label | string | Required |  | Error label when the request is not accepted; empty on success  
message | string | Required |  | Error message when the request is not accepted; empty on success  
      
    
    {
      "order_id": "string",
      "text": "string",
      "accepted": "string",
      "label": "string",
      "message": "string"
    }
    
    

##  CrossexOrder

CrossexOrder

Type | Constraints  
---|---  
object | required: ["user_id","order_id","text","state","symbol","side","type","exchange_type","attribute","executed_avg_price","executed_amount","executed_qty","time_in_force","price","quote_qty","qty","business_type","fee","fee_coin","reduce_only","leverage","last_executed_price","last_executed_qty","reason","position_side","last_executed_amount","update_time","create_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | string | Required |  | User ID  
order_id | string | Required |  | Order ID  
text | string | Required |  | Client-defined order ID.  
state | string | Required |  | Order status:  
`NEW`: validated locally, pending submission to the exchange  
`OPEN`: resting on the exchange order book  
`PARTIALLY_FILLED`: partially filled  
`FILLED`: fully filled  
`FAIL`: CrossEx validation failed; see `reason`  
`REJECT`: rejected by the exchange; see `reason`  
`CANCELLED`: cancelled  
symbol | string | Required |  | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
side | string | Required |  | Side (`BUY` buy / `SELL` sell).  
type | string | Required |  | Order type (`LIMIT` limit / `MARKET` market).  
attribute | string | Required |  | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
exchange_type | string | Required |  | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
business_type | string | Required |  | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)  
qty | string | Required |  | Order quantity in the base currency.  
quote_qty | string | Required |  | Order quantity in the quote currency.  
price | string | Required |  | Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
time_in_force | string | Required |  | Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)  
executed_qty | string | Required |  | Filled base amount.  
executed_amount | string | Required |  | Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
executed_avg_price | string | Required |  | Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
fee_coin | string | Required |  | Fee currency  
fee | string | Required |  | Fee amount.  
reduce_only | string | Required |  | Reduce-only order (`"true"` or `"false"`).  
leverage | string | Required |  | Order leverage multiplier.  
reason | string | Required |  | Failure reason description.  
last_executed_qty | string | Required |  | Base quantity of the latest fill.  
last_executed_price | string | Required |  | Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
last_executed_amount | string | Required |  | Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
position_side | string | Required |  | Position side (`NONE` one-way position / `LONG` long / `SHORT` short)  
create_time | string | Required |  | Created time  
update_time | string | Required |  | Update time  
  
**user_id**

User ID

User ID

Type | Constraints  
---|---  
string |   
  
**order_id**

Order ID

Order ID

Type | Constraints  
---|---  
string |   
  
**text**

Client Order ID

Client-defined order ID.

Type | Constraints  
---|---  
string |   
  
**state**

Order status

Order status: `NEW`: validated locally, pending submission to the exchange `OPEN`: resting on the exchange order book `PARTIALLY_FILLED`: partially filled `FILLED`: fully filled `FAIL`: CrossEx validation failed; see `reason` `REJECT`: rejected by the exchange; see `reason` `CANCELLED`: cancelled

Type | Constraints  
---|---  
string |   
  
**symbol**

Currency pair

Unique trading pair identifiers, e.g. `BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.

Type | Constraints  
---|---  
string |   
  
**side**

direction

Side (`BUY` buy / `SELL` sell).

Type | Constraints  
---|---  
string |   
  
**type**

Type

Order type (`LIMIT` limit / `MARKET` market).

Type | Constraints  
---|---  
string |   
  
**attribute**

Attribute COMMON: Normal Order, LIQ: Liquidation Takeover Order, REDUCE: Liquidation Reduce Order, ADL: Auto-Reduce

Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).

Type | Constraints  
---|---  
string |   
  
**exchange_type**

Exchange

Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)

Type | Constraints  
---|---  
string |   
  
**business_type**

Business Type

Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)

Type | Constraints  
---|---  
string |   
  
**qty**

Base Currency Quantity

Order quantity in the base currency.

Type | Constraints  
---|---  
string |   
  
**quote_qty**

Quote Currency Quantity

Order quantity in the quote currency.

Type | Constraints  
---|---  
string |   
  
**price**

Price

Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**time_in_force**

Time in Force Strategy

Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)

Type | Constraints  
---|---  
string |   
  
**executed_qty**

Filled quantity

Filled base amount.

Type | Constraints  
---|---  
string |   
  
**executed_amount**

Filled Amount

Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**executed_avg_price**

Average Filled Price

Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**fee_coin**

Fee currency

Fee currency

Type | Constraints  
---|---  
string |   
  
**fee**

fee

Fee amount.

Type | Constraints  
---|---  
string |   
  
**reduce_only**

Reduce Position Only

Reduce-only order (`"true"` or `"false"`).

Type | Constraints  
---|---  
string |   
  
**leverage**

Leverage

Order leverage multiplier.

Type | Constraints  
---|---  
string |   
  
**reason**

Reason

Failure reason description.

Type | Constraints  
---|---  
string |   
  
**last_executed_qty**

Latest Filled Quantity

Base quantity of the latest fill.

Type | Constraints  
---|---  
string |   
  
**last_executed_price**

Latest Filled Price

Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**last_executed_amount**

Latest Filled Amount

Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)

Type | Constraints  
---|---  
string |   
  
**position_side**

Position Direction

Position side (`NONE` one-way position / `LONG` long / `SHORT` short)

Type | Constraints  
---|---  
string |   
  
**create_time**

Created time

Created time

Type | Constraints  
---|---  
string |   
  
**update_time**

Update time

Update time

Type | Constraints  
---|---  
string |   
      
    
    {
      "user_id": "string",
      "order_id": "string",
      "text": "string",
      "state": "string",
      "symbol": "string",
      "side": "string",
      "type": "string",
      "attribute": "string",
      "exchange_type": "string",
      "business_type": "string",
      "qty": "string",
      "quote_qty": "string",
      "price": "string",
      "time_in_force": "string",
      "executed_qty": "string",
      "executed_amount": "string",
      "executed_avg_price": "string",
      "fee_coin": "string",
      "fee": "string",
      "reduce_only": "string",
      "leverage": "string",
      "reason": "string",
      "last_executed_qty": "string",
      "last_executed_price": "string",
      "last_executed_amount": "string",
      "position_side": "string",
      "create_time": "string",
      "update_time": "string"
    }
    
    

##  CrossexMarginModeResponse

CrossexMarginModeResponse

Type | Constraints  
---|---  
object | required: ["symbol","margin_mode"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Futures trading pair  
margin_mode | string | Required |  | Margin mode (CROSS/ISOLATED)  
      
    
    {
      "symbol": "string",
      "margin_mode": "string"
    }
    
    

##  CrossexConvertQuoteRequest

Flash Swap Quote Request Body

Type | Constraints  
---|---  
object | required: ["exchange_type","from_coin","to_coin","from_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
exchange_type | string | Required |  | Exchange type  
Currently supports only BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, and LIGHTER  
from_coin | string | Required |  | Asset Sold  
to_coin | string | Required |  | Asset to receive  
OKX and GATE only support conversion to BTC, ETH, or USDT  
BYBIT and BINANCE only support conversion to USDT  
HYPERLIQUID only supports conversion to USDT or USDC  
KRAKEN only supports conversion to USDT  
LIGHTER only supports swaps between USDT and USDC  
from_amount | string | Required |  | Amount to sell  
      
    
    {
      "exchange_type": "string",
      "from_coin": "string",
      "to_coin": "string",
      "from_amount": "string"
    }
    
    

##  CrossexLeverageRequest

Change Leverage Request Body (for futures/margin)

Type | Constraints  
---|---  
object | required: ["symbol","leverage"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Currency pair  
leverage | string | Required |  | Leverage  
      
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    
    

##  CrossexClosePositionRequest

Full Close Position Request Body

Type | Constraints  
---|---  
object | required: ["symbol"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
symbol | string | Required |  | Trading Pair  
1\. Supports leveraged trading pairs, e.g., BINANCE_MARGIN_SOL_USDT  
2\. Supports contract trading pairs, e.g., OKX_FUTURE_ETH_USDT  
position_side | string | Optional |  | Position Direction  
1\. For leveraged positions, this parameter must be passed  
2\. For contract positions, pass selectively based on your contract holding method  
      
    
    {
      "symbol": "string",
      "position_side": "string"
    }
    
    

##  CrossexTransferRequest

Fund Transfer Request Body

Type | Constraints  
---|---  
object | required: ["amount","from","coin","to"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  | Currency  
amount | string | Required |  | Transfer amount  
from | string | Required |  | `from` debit account (funds withdrawn from): `CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`  
to | string | Required |  | `to` receiving account (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`).  
text | string | Optional |  | User-defined ID  
      
    
    {
      "coin": "string",
      "amount": "string",
      "from": "string",
      "to": "string",
      "text": "string"
    }