---
exchange: gateio
source_url: https://www.gate.com/docs/developers/crossex/en
api_type: Trading
updated_at: 2026-05-27 20:18:18.483886
---

# Gate CrossEx API v1.0.1

* Python 
  * Shell 

v1.0.1 · Stable


The API fully supports core capabilities of cross-exchange accounts, covering full-process operations such as fund transfers, queries, trading, account information modifications, subscriptions, and push notifications.

Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

##  Access URL

**REST API BaseURL:**

  * Live trading: `https://api.gateio.ws/api/v4`

##  SDK

Available SDK:

[PyPython](https://github.com/gate/gateapi-python)[JavaJava](https://github.com/gate/gateapi-java)[PHPPHP](https://github.com/gate/gateapi-php)[GoGo](https://github.com/gate/gateapi-go)[C#C#](https://github.com/gate/gateapi-csharp)[NodeNodeJS](https://github.com/gate/gateapi-nodejs)[JSJavascript](https://github.com/gate/gateapi-js)

  * [Python ](https://github.com/gate/gateapi-python)
  * [Java ](https://github.com/gate/gateapi-java)
  * [PHP ](https://github.com/gate/gateapi-php)
  * [Go ](https://github.com/gate/gateapi-go)
  * [C# ](https://github.com/gate/gateapi-csharp)
  * [NodeJS ](https://github.com/gate/gateapi-nodejs)
  * [Javascript ](https://github.com/gate/gateapi-js)

Besides API examples, some SDK provides an additional demo application. The demo application is a relatively complete example demonstrating how to use the SDK. It can be built and run separately. Refer to corresponding repository for details.

  * [Python ](https://github.com/gate/gateapi-python/tree/master/example)
  * [Java ](https://github.com/gate/gateapi-java/tree/master/example)
  * [C# ](https://github.com/gate/gateapi-csharp/tree/master/example)
  * [Go ](https://github.com/gate/gateapi-go/tree/master/_example)

##  About CrossEx

CrossEx is a cross-exchange trading platform that allows users to trade across multiple exchanges (Binance, OKX, Gate.io, Bybit) through a unified account. The CrossEx API provides complete account management, asset transfers, order placement, and position management functions across exchanges.

  * [Help Center ](https://www.gate.com/help/crossex/functional)
  * [CrossEx Trading ](https://www.gate.com/crossex)

##  Technical Support

If you have any questions or suggestions during the use, you can contact us in any of the following ways:

  * Submit Work Order Feedback
  * Online Work Order Feedback
  * Send your contact information and questions to [mm@gate.com](mailto:mm@gate.com) We will assign technical specialists to serve you.

If you encounter API errors, it is recommended that you sort out the following content, so that we can quickly analyze the problem for you:

  1. Problem Description
  2. Gate UID
  3. Request URI and parameters
  4. Error Code
  5. Responses

DANGER

Even if you submit a problem, you should not submit the API key information to customer service or others, otherwise there will be serious asset risk. If it has been accidentally leaked, please delete the existing API and rebuild it.

#  Changelog

**v1.0.2**

2026-05-19

  * Add KRAKEN exchange support for CrossEx

2026-03-19

  * Support isolated exchange rates, the fee rate query structure has been changed to an array

**v1.0.1**

2026-03-12

  * Add BYBIT exchange support for CrossEx

**v1.0.0**

2026-01-20

  * Initial release of CrossEx API
  * Provide unified account management across multiple exchanges
  * Support cross-exchange asset transfers
  * Provide order placement and management across exchanges
  * Support position management for futures and margin trading
  * Provide market data query (trading pairs, risk limits, etc.)
  * Support account settings (position mode, account mode, leverage)

#  General

API delivers full support for CrossEx account operations, including fund transfers, queries, trading, account updates, subscriptions, and real‑time push notifications.

  * [Help Center ](https://www.gate.com/help/crossex/functional)
  * [CrossEx Trading ](https://www.gate.com/crossex)

##  Data Center

Gate data center is located in AWS Japan's ap-northeast-1 region.

##  API Overview

API OverviewAPI Classification | Category Links | Overview  
---|---|---  
host + `/api/v4/crossex/*` | CrossEx API | Cross-exchange trading API for unified account management and trading across multiple exchanges  
  
##  CrossEx Features

CrossEx is a cross-exchange trading platform that provides the following features:

  * Unified account management across multiple exchanges (Binance, OKX, Gate.io, Bybit)
  * Cross-exchange asset transfers
  * Unified order management and trading
  * Real-time position and asset monitoring
  * Support for spot, futures, and margin trading across exchanges

##  Usage Instructions

Before using the CrossEx API, please ensure:

  1. You have opened a CrossEx account
  2. You have obtained the corresponding API permissions
  3. You understand the trading rules and restrictions of CrossEx
  4. You have configured your exchange accounts properly

##  API Categories

CrossEx API mainly includes the following functional modules:

  * **Account Management** : Query and manage unified account assets
  * **Asset Transfers** : Transfer assets between exchanges and spot accounts
  * **Order Management** : Place, query, and manage orders across exchanges
  * **Position Management** : Query and manage positions for futures and margin trading
  * **Market Data** : Query trading pairs, risk limits, and market information
  * **Account Settings** : Configure position modes, account modes, and leverage

#  Authentication

##  Generate API key

Before calling the private API interface, the API key of the account needs to be generated to verify the identity. You can log in on the website and generate it in [account management] - > [APIv4 keys], or click [ here](/myaccount/apiv4keys) to generate API keys.

Each account can create 20 API keys, and the permission configuration of each key is independent of each other. It is recommended to set a note name for each key to indicate its purpose.

**`Key`** Access Key **`Secret Key`** The key used for signature authentication encryption

Besides, you can attach an IP whitelist, which requires the server only accept requests from specified IPs. Each key can have at most 20 IPs formatted in IPv4(not supporting IP range though). If IP whitelist is not set, the server will skip client IP validation.

Each user can create at most 5 keys with separate permissions. It is recommended to set a name for key denoting how the key will be used.

TIP

Note: If the key is named with `spot` or `futures`, then it could be the default name after APIv4 migration. For details refer to _About APIv4 key improvement_ section

Created key can also be updated or deleted, but any modification(s) can take up to 5 minutes to take effect.

Please note that futures TestNet trading is a separate environment from futures real trading. Real trading API keys cannot be used in TestNet. If you want to test futures API with TestNet, you need to log into the console to generate TestNet API keys(in _"Futures TestNet APIKeys"_ tab on _" APIv4Keys"_ page). Making futures requests are identical between real and TestNet trading, with the only exceptions are different base URLs and different API keys.

##  APIv4 Permissions

When creating a Key, you can configure whether to enable spot, margin, contract, wallet, or withdrawal permissions for the Key, and whether to enable read-write or read-only permissions.

APIv4 PermissionsProducts | Permissions  
---|---  
`spot/margin` | `Read-only` query orders `Read-write` query orders & place orders  
`perpetual contract` | `Read-only` query orders `Read-write` query orders & place orders  
`delivery contract` | `Read-only` query orders `Read-write` query orders & place orders  
`wallet` | `Read-only` Query for withdrawal transfer records `Read-write` Query for account records & fund transfers  
`withdrawal` | `Read-only` Query cash withdrawal records `Read-write` Query cash withdrawal records & withdrawals  
  
All `GET` operations are read requests, while others are write requests. Each permission group can be set to disabled, read-only or read-write.

Please note that even though withdrawal API has only one operation(i.e. `POST /withdrawals`), for general concern, it is still separated from wallet API into a standalone permission group, while withdrawal history retrieving API stays inside wallet operations( i.e., `GET /wallet/withdrawals`).

##  APIv4 signed request requirements

  1. Generate APIv4 Key pairs in web console, and make sure it has the right permissions.
  2. Set request header `KEY` to the key.
  3. Set request header `Timestamp` to current time formatted in Unix time in seconds. Pay attention that the gap between its value and current time cannot exceed 60 seconds.
  4. Set request header `SIGN` to encrypted request signature. Refer to next section for how signature string is generated. Signature generation method is `HexEncode(HMAC_SHA512(secret, signature_string))`, i.e., the hexadecimal digest output of HMAC-SHA512 with APIv4 secret as secret and signature string as message,
  5. Make sure request client's IP is in your APIv4 Key's IP whitelist.

##  API Signature string generation

In APIv4, signature string is concatenated as the following way:

`Request Method + "\n" + Request URL + "\n" + Query String + "\n" + HexEncode(SHA512(Request Payload)) + "\n" + Timestamp`

###  Request Method

Request method in UPPERCASE, e.g. `POST`, `GET`

###  Request URL

Request url. Protocol, host and port are not included, e.g. `/api/v4/futures/orders`

###  Query String

Request query string without URL encode. query parameters order should be the same as how they are concatenated in the request URL, e.g. `status=finished&limit=50`. Use empty string("") if no query parameters.

###  HexEncode(SHA512(Request Payload))

Hash the request body with SHA512 and output its Hex encoded form. If no request body, use empty string's hashed result, i.e. `cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e`

###  Timestamp

`Timestamp` request header value.

Examples

Note: all example signature string are broken into multiple lines for displaying purpose only. Only the `\n` character in signature string is reserved in reality.

Suppose the key we used is `key`, while the secret is `secret`.

  1. List all orders

    
    
    	GET /api/v4/futures/orders?contract=BTC_USD&status=finished&limit=50 HTTP/1.1
    

Signature string：
    
    
    	GET\n
    	/api/v4/futures/orders\n
    	contract=BTC_USD&status=finished&limit=50\n
    	cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e\n
    	1541993715
    

Explanation：

  * `/api/v4/futures/orders`: request url
  * `contract=BTC_USD&status=finished&limit=50`: keep the query string as it is in the request url
  * request body use empty string's hashed result
  * `1541993715`: Unix timestamp in seconds

Signature generated

`55f84ea195d6fe57ce62464daaa7c3c02fa9d1dde954e4c898289c9a2407a3d6fb3faf24deff16790d726b66ac9f74526668b13bd01029199cc4fcc522418b8a`

  2. Create an order

    
    
    	POST /api/v4/futures/orders HTTP/1.1
    
    	{"contract":"BTC_USD","type":"limit","size":100,"price":6800,"time_in_force":"gtc"}
    

Signature string：
    
    
    	POST\n
    	/api/v4/futures/orders\n
    	\n
    	ad3c169203dc3026558f01b4df307641fa1fa361f086b2306658886d5708767b1854797c68d9e62fef2f991645aa82673622ebf417e091d0bd22bafe5d956cca\n
    	1541993715
    

Explanation：

  * request query string is empty, use plain empty string
  * use the hashed result of the json-string-formatted request body

Signature generated

`eae42da914a590ddf727473aff25fc87d50b64783941061f47a3fdb92742541fc4c2c14017581b4199a1418d54471c269c03a38d788d802e2c306c37636389f0`
    
    
    # example authentication implementation in Python
    
    """
    Python SDK is recommended as it has already implemented the authentication process for every API:
    """
    
    import time
    import hashlib
    import hmac
    import requests
    import json
    
    def gen_sign(method, url, query_string=None, payload_string=None):
        key = ''        # api_key
        secret = ''     # api_secret
    
        t = time.time()
        m = hashlib.sha512()
        m.update((payload_string or "").encode('utf-8'))
        hashed_payload = m.hexdigest()
        s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
        sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}
    
    if __name__ == "__main__":
        host = "https://api.gateio.ws"
        prefix = "/api/v4"
        common_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
        url = '/futures/orders'
        body = {"contract": "BTC_USD", "size": 100, "price": "30", "tif": "gtc"}
        request_content = json.dumps(body)
        sign_headers = gen_sign('POST', prefix + url, "", request_content)
        sign_headers.update(common_headers)
        print('signature headers: %s' % sign_headers)
        res = requests.post(host + prefix + url, headers=sign_headers, data=request_content)
        print(res.status_code)
        print(res.content)
    

##  Error Handling

For all abnormal requests, APIv4 will return non-2xx status code, with a response body in JSON format to explain the error.

The error response body follows a format like:
    
    
    {
      "label": "COMMON_PARAM_BIND_ERROR",
      "message": "Invalid parameter, please refer to API documentation"
    }
    

  * `label`: denotes error type in `string` format. Its value are chosen from a certain list(see below). Programs can use `label` to identify and catch a specific error.
  * `message`(or `detail`): detailed error message. A longer explanation showing why the error is generated or how to avoid it. Its purpose is helping to better understand the API. Error handling mechanism with this field is highly **NOT** recommended.

Take Python [requests ](https://requests.readthedocs.io/en/latest/) for example, error handling can be written like:

> Following examples only deal with business-related errors. Network timeout or other common errors need to be handled separately:
    
    
    import requests
    
    r = requests.get("https://api.gateio.ws/api/v4/crossex/accounts")
    try:
        r.raise_for_status()
    except requests.HTTPError:
        # catch 2xx errors, parse error message in body, and do something based on `label`
        if r.json()['label'] == 'xxx':
            print(r.json())
    

##  `label` list

  * Common errors

label list`label` | Meaning  
---|---  
COMMON_PARAM_BIND_ERROR | Invalid parameter, please refer to API documentation  
TRADE_UNSUPPORTED_OPERATION | Current operation is not allowed  
  
  * Account related

label list`label` | Meaning  
---|---  
USER_NOT_EXIST | User does not exist  
USER_DEACTIVATED | User has been deactivated  
QUERY_INVALID_EXCHANGE_TYPE | Invalid exchange type, in isolated mode exchange type must be BINANCE, OKX, GATE, BYBIT or KRAKEN  
TRADE_CHANGE_PZ_MODE_SAME_ERROR | No need to set position mode repeatedly  
TRADE_PZ_MODE_HAVE_ORDER_ERROR | Cannot set position mode with open orders  
TRADE_PZ_MODE_HAVE_POSITION_ERROR | Cannot set position mode with open positions  
UPDATE_ACCOUNT_PARAMETERS_ALL_EMPTY_ERROR | Parameters cannot all be empty  
UPDATE_ACCOUNT_PARAMETERS_ERROR | Cannot set account mode and position mode simultaneously  
UPDATE_ACCOUNT_EXCHANGE_TYPE_PARAMETERS_ERROR | If exchange parameter is provided, position mode must be provided  
UPDATE_ACCOUNT_ACCOUNT_MODE_ERROR | Invalid account mode, please refer to API documentation  
UPDATE_ACCOUNT_EXCHANGE_TYPE_ERROR | Invalid exchange type, please refer to API documentation  
UPDATE_ACCOUNT_PZ_ISOLATED_MODE_NOT_EXCHANGE_TYPE_ERROR | Exchange must be provided when modifying position mode in isolated mode  
UPDATE_ACCOUNT_MODE_OPEN_ORDERS_EXIST_ERROR | Cannot modify account mode with open orders  
UPDATE_ACCOUNT_MODE_POSITION_NOT_EMPTY_ERROR | Cannot modify account mode with open positions  
UPDATE_ACCOUNT_MODE_INITIAL_MARGIN_NOT_ZERO_ERROR | Cannot modify account mode with initial margin  
UPDATE_ACCOUNT_MODE_MAINTENANCE_MARGIN_NOT_ZERO_ERROR | Cannot modify account mode with maintenance margin  
UPDATE_ACCOUNT_MODE_ACCOUNT_STATUS_NOT_NORMAL_ERROR | Cannot modify account mode when account status is not NORMAL  
UPDATE_ACCOUNT_CROSSEX_MODE_EXCHANGE_TYPE_NOT_CROSSEX_ERROR | In cross-exchange mode, exchange type can only be CROSSEX  
UPDATE_ACCOUNT_ISOLATED_MODE_EXCHANGE_TYPE_NOT_CROSSEX_ERROR | In isolated mode, exchange type cannot be CROSSEX  
  
  * Order related

label list`label` | Meaning  
---|---  
TRADE_CLIENT_ORDER_ID_LENGTH_ERROR | Client order ID is too long  
TRADE_CLIENT_ORDER_ID_MATCH_ERROR | Client order ID only supports letters (a-z), numbers (0-9), and symbols (-, _)  
TRADE_INVALID_SIDE | Invalid order side  
TRADE_INVALID_ORDER_TYPE | Invalid order type  
TRADE_INVALID_TIME_IN_FORCE | Invalid timeInForce  
TRADE_INVALID_POC | Market order timeInForce cannot be POC  
TRADE_INVALID_ORDER_QTY | Invalid order quantity  
TRADE_INVALID_QUOTE_ORDER_QTY | Invalid quote order quantity  
TRADE_INVALID_LIMIT_PRICE | Invalid limit price  
TRADE_INVALID_REDUCE_ONLY | Invalid reduceOnly  
TRADE_ORDER_DUPLICATE_ERROR | Duplicate client order ID  
TRADE_SYM_NOT_SUPPORT | Current symbol is not supported  
MARGIN_ORDER_NOT_SUPPORT | Isolated mode does not support spot margin trading  
TRADE_MARGIN_INVALID_PZ_SIDE_ERROR | Margin only supports dual mode, LONG/SHORT must be provided  
TRADE_DELIST_OPEN_PROHIBITED_ERROR | Symbol is delisted, only close orders are allowed  
TRADE_INVALID_POSITION_SIDE | Invalid positionSide  
TRADE_REDUCE_ONLY_SIDE_ERROR | ReduceOnly order cannot have the same direction as position  
TRADE_REDUCE_ONLY_POSITION_QTY_ERROR | Cannot use reduceOnly when position quantity is 0  
TRADE_ONE_OF_ORDER_ID_ERROR | Either orderId or text must be provided for cancellation  
TRADE_ORDER_NOT_FOUND_ERROR | Order does not exist or is in terminal state  
TRADE_NOT_ALLOW_REPLACE | Market orders are not allowed to be replaced  
TRADE_ORDER_REPLACE_QTY_PRICE_ERROR | Invalid quantity or price for order replacement  
TRADE_ORDER_REPLACE_QTY_PRICE_SAME_ERROR | Replacement quantity and price are the same as existing order  
TRADE_ORDER_REPLACE_ALLOW_ERROR | Order status does not allow replacement  
TRADE_ORDER_LOT_SIZE_ERROR | Order quantity must be a multiple of lotSize  
TRADE_ORDER_QUANTITY_MAX_ERROR | Order quantity exceeds maximum limit  
TRADE_ORDER_QUANTITY_MIN_ERROR | Order quantity is below minimum limit  
TRADE_ORDER_TICK_SIZE_ERROR | Order price must be a multiple of tickSize  
TRADE_ORDER_AMOUNT_MIN_ERROR | Order value is below minimum value limit  
TRADE_OKX_LIMIT_BUY_ORDER_PRICE_ERROR | OKX limit price deviates too much from market  
TRADE_MAX_ORDERS_ERROR | Number of open orders exceeds limit  
TRADE_INVALID_PZ_MODE_ERROR | Invalid position mode  
  
  * Leverage adjustment related

label list`label` | Meaning  
---|---  
TRADE_SET_LEVERAGE_ERROR | Invalid leverage  
TRADE_INVALID_SYM_BUSINESSTYPE_ERROR | Leverage adjustment must be for contract symbol  
TRADE_SET_LEVERAGE_EXCEED_LIMIT_ERROR | Leverage exceeds maximum limit  
TRADE_INVALID_MARGIN_SYM_BUSINESSTYPE_ERROR | Leverage adjustment must be for margin symbol  
  
  * Convert trade related

label list`label` | Meaning  
---|---  
CONVERT_TRADE_QUOTE_UNKNOWN_ERROR | Convert trade request error, please try again later  
CONVERT_TRADE_QUOTE_EXCHANGE_INVALID_ERROR | Invalid exchange type, please refer to API documentation  
CONVERT_TRADE_QUOTE_FROM_COIN_INVALID_ERROR | Invalid fromCoin, please refer to API documentation  
CONVERT_TRADE_QUOTE_TO_COIN_INVALID_ERROR | Invalid toCoin, please refer to API documentation  
CONVERT_TRADE_QUOTE_FROM_AMOUNT_INVALID_ERROR | Invalid fromAmount, please refer to API documentation  
CONVERT_TRADE_QUOTE_FROM_AMOUNT_LIMIT_ERROR | Invalid fromAmount, cannot be 0  
CONVERT_TRADE_QUOTE_FROM_AMOUNT_MAX_ERROR | Invalid fromAmount, amount cannot exceed 10U  
CONVERT_TRADE_QUOTE_EXCHANGE_REJECT_ERROR | Convert trade request rejected by exchange, please check reason  
  
  * Close all positions related

label list`label` | Meaning  
---|---  
CAN_NOT_DELETE_POSITION | Position quantity is 0, cannot close all positions  
CAN_NOT_DELETE_LARGE_POSITION | Position quantity is too large, please close via orders first  
OPEN_ORDERS_CAN_NOT_DELETE_POSITION | Cannot close all positions with open orders  
  
#  CrossEx

CrossEx is a unified multi-venue exchange surface: Binance, OKX, Gate, Bybit, and Kraken tie into one account shell for transfers, market data subscriptions, fills, positions, and account maintenance.

  * REST production base URL: `https://api.gateio.ws/api/v4`
  * [CrossEx help desk ](https://www.gate.com/help/crossex/functional)
  * [Unified trading cockpit ](https://www.gate.com/crossex)

##  Query symbol information

GET`/crossex/rule/symbols`

GET `/crossex/rule/symbols`

_Query symbol information_

Query Trading Pair Information

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
symbols | query | string | Optional | List of trading pairs, comma-separated.  
Example:  
BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT  
  
####  Detailed descriptions

**symbols** : List of trading pairs, comma-separated.  
Example:  
BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Symbol]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» symbol | string | Unique trading pair identifier in the form ExchangeType_BusinessType_Base_Counter.  
» exchange_type | string | Venue bucket (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN`).  
» business_type | string | Business type (`SPOT` Spot / `FUTURE` Futures / `MARGIN` Margin).  
» state | string | Status (`live` running / `suspend` paused).  
» min_size | string | Minimum order size allowed by the contract  
» min_notional | string | Minimum Order Value  
» lot_size | string | Quantity Step  
» tick_size | string | Price Step  
» max_num_orders | string | maximumopen orderamount  
» max_market_size | string | Maximum Market Order Quantity  
» max_limit_size | string | Maximum order quantity for limit orders.  
» contract_size | string | Contract Multiplier  
» liquidation_fee | string | Liquidation Fee Rate  
» delist_time | string | Millisecond timestamp; `0` means not delisted.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "//"
    prefix = "//"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/rule/symbols'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET /crossex/rule/symbols \
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
        "delist_time": "0"
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
        "delist_time": "1762163297615"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexRiskLimit | object | none  
»» symbol | string | none  
»» tiers | array | none  
»»» CrossexRiskLimitTier | object | none  
»»»» min_risk_limit_value | string | Minimum risk limit value  
»»»» max_risk_limit_value | string | Maximum risk limit value  
»»»» quick_cal_amount | string | Quick-calculation amount  
»»»» leverage_max | string | Maximum leverage  
»»»» maintenance_rate | string | Maintenance margin rate  
»»»» tier | string | Tier  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "//"
    prefix = "//"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/rule/risk_limits'
    query_param = 'symbols=BINANCE_FUTURE_AAVE_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET /crossex/rule/risk_limits?symbols=BINANCE_FUTURE_AAVE_USDT \
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

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
coin | query | string | Optional | Query by specified currency name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexTransferCoin | object | none  
»» coin | string | Currency  
»» min_trans_amount | number | Minimum Transfer Quantity (including estimated fees)  
»» est_fee | number | Estimated Fee  
»» precision | integer | Precision  
»» is_disabled | integer | If it is disabled. 0 means NOT being disabled  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "//"
    prefix = "//"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/transfers/coin'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET /crossex/transfers/coin \
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
    

##  Fund Transfer🔒 Authenticated

POST`/crossex/transfers`

POST `/crossex/transfers`

_Fund Transfer_

Rate limit: 10 requests per 10 seconds

  * In cross-exchange mode, when transferring USDT, either `from` or `to` must be `SPOT`, and the other side must be `CROSSEX`. If `CROSSEX_${exchange_type}` (e.g. `CROSSEX_GATE`) is provided, it will be automatically treated as `CROSSEX`.
  * In isolated exchange mode, when transferring USDT, either `from` or `to` must be `CROSSEX_${exchange_type}`, and the other side must be `SPOT` or `CROSSEX_${exchange_type}`. If `CROSSEX` is provided, it will be automatically treated as `CROSSEX_GATE`.
  * When transferring non-USDT assets to or from CrossEx, neither `from` nor `to` can be `CROSSEX`; `CROSSEX_${exchange_type}` must be explicitly specified.
  * When transferring non-USDT assets, transfers between `CROSSEX_{exchange_type}` accounts are supported, for example: from = `CROSSEX_BINANCE`, to = `CROSSEX_GATE`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexTransferRequest | Optional | none  
↳ coin | body | string | Required | Currency  
↳ amount | body | string | Required | Transfer amount  
↳ from | body | string | Required | `from` receiving account (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX`, `SPOT`).  
↳ to | body | string | Required | `to` debit account (funds withdrawn from): `CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX`, `SPOT`  
↳ text | body | string | Optional | User-defined ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexTransferResponse  
  
### Response Schema

Status Code **200**

_CrossexTransferResponse_

Name | Type | Description  
---|---|---  
» tx_id | string | Order ID  
» text | string | User-defined Order ID  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexTransferRecord | object | none  
»» id | string | Order ID  
»» text | string | Client Custom ID  
»» from_account_type | string | `from` credit account touched by this operation (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX`, `SPOT`).  
»» to_account_type | string | `to` debit account handled by this operation (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX`, `SPOT`).  
»» coin | string | Currency  
»» amount | string | Transfer amount, the amount requested for the transfer  
»» actual_receive | string | Actual credited amount (has a value when status = SUCCESS; empty for other statuses)  
»» status | string | Transfer Status  
\- `FAIL`: Failed  
\- `SUCCESS`: Successful  
\- `PENDING`: Transfer in Progress  
»» fail_reason | string | Failure reason (has a value when status = FAIL; empty for other statuses)  
»» create_time | integer | Creation time of order  
»» update_time | integer | OrderUpdateTime  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
    

##  Create an order🔒 Authenticated

POST`/crossex/orders`

POST `/crossex/orders`

_Create an order_

Rate Limit: 100 requests per 10 seconds, maximum 1,000 open orders per user

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexOrderRequest | Optional | none  
↳ text | body | string | Optional | Client-defined Order ID, supports letters (a-z), numbers (0-9), symbols (-, _) only  
↳ symbol | body | string | Required | Unique identifier `{Exchange}_{Business}_{Base}_{Counter}`  
Examples:  
To send a Binance spot order on `ADA/USDT`, use `BINANCE_SPOT_ADA_USDT`;  
For an ADA/USDT-margined USDT perpetual futures order on OKX, use `OKX_FUTURE_ADA_USDT`;  
For ADA/USDT margin trading on Gate, use `GATE_MARGIN_ADA_USDT`;  
For ADA/USDT spot trading on Bybit, use `BYBIT_SPOT_ADA_USDT`;  
For ADA/USDT-linked futures routing on Kraken, use `KRAKEN_FUTURE_ADA_USD`;  
Supports spot trades, USDT-margined perpetual futures, and spot margin templates. BYBIT omits spot margin for now; Kraken omits dedicated spot/margin legs inside CrossEx.  
↳ side | body | string | Required | BUY, SELL  
↳ type | body | string | Optional | Order type (default: `LIMIT`; supported types: `LIMIT`, `MARKET`)  
↳ time_in_force | body | string | Optional | Default GTC, supports enumerated types: GTC, IOC, FOK, POC  
GTC: GoodTillCancelled  
IOC: ImmediateOrCancelled  
FOK: FillOrKill  
POC: PendingOrCancelled or PostOnly  
↳ qty | body | string | Optional | Order quantity (required unless spot market buy)  
↳ price | body | string | Optional | Limit Order Price (Required for Limit Orders)  
↳ quote_qty | body | string | Optional | Order quote quantity; required for spot and margin market buy orders  
↳ reduce_only | body | string | Optional | Reduce-only: `true` or `false`  
↳ position_side | body | string | Optional | Position side: `NONE`, `LONG`, `SHORT`  
Defaults to `NONE` (single position mode) if not specified  
  
####  Detailed descriptions

**» symbol** : Unique identifier `{Exchange}_{Business}_{Base}_{Counter}`  
Examples:  
To send a Binance spot order on `ADA/USDT`, use `BINANCE_SPOT_ADA_USDT`;  
For an ADA/USDT-margined USDT perpetual futures order on OKX, use `OKX_FUTURE_ADA_USDT`;  
For ADA/USDT margin trading on Gate, use `GATE_MARGIN_ADA_USDT`;  
For ADA/USDT spot trading on Bybit, use `BYBIT_SPOT_ADA_USDT`;  
For ADA/USDT-linked futures routing on Kraken, use `KRAKEN_FUTURE_ADA_USD`;  
Supports spot trades, USDT-margined perpetual futures, and spot margin templates. BYBIT omits spot margin for now; Kraken omits dedicated spot/margin legs inside CrossEx.

**» time_in_force** : Default GTC, supports enumerated types: GTC, IOC, FOK, POC  
GTC: GoodTillCancelled  
IOC: ImmediateOrCancelled  
FOK: FillOrKill  
POC: PendingOrCancelled or PostOnly

**» position_side** : Position side: `NONE`, `LONG`, `SHORT`  
Defaults to `NONE` (single position mode) if not specified

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» side | BUY  
» side | SELL  
» type | LIMIT  
» type | MARKET  
» time_in_force | GTC  
» time_in_force | IOC  
» time_in_force | FOK  
» time_in_force | POC  
» reduce_only | true  
» reduce_only | false  
» position_side | LONG  
» position_side | SHORT  
» position_side | NONE  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrderActionResponse  
  
### Response Schema

Status Code **200**

_CrossexOrderActionResponse_

Name | Type | Description  
---|---|---  
» order_id | string | Order ID  
» text | string | User-defined Order ID  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrderActionResponse  
  
### Response Schema

Status Code **200**

_CrossexOrderActionResponse_

Name | Type | Description  
---|---|---  
» order_id | string | Order ID  
» text | string | User-defined Order ID  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
↳ qty | body | string | Optional | modify amount  
↳ price | body | string | Optional | modify price  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrderActionResponse  
  
### Response Schema

Status Code **200**

_CrossexOrderActionResponse_

Name | Type | Description  
---|---|---  
» order_id | string | Order ID  
» text | string | User-defined Order ID  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
      "text": "crossx-test-1"
    }
    

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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrder  
  
### Response Schema

Status Code **200**

_CrossexOrder_

Name | Type | Description  
---|---|---  
» user_id | string | User ID  
» order_id | string | Order ID  
» text | string | Client-defined order ID.  
» state | string | Order status:  
  
NEW: Validated and queued to be sent to the exchange.  
  
OPEN: Resting on the exchange order book.  
  
PARTIALLY_FILLED: Partially filled.  
  
FILLED: Fully filled.  
  
FAIL: CrossEx internal validation failed; see the `reason` field for details.  
  
REJECT: Rejected by the exchange; see the `reason` field for details.  
» symbol | string | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
» side | string | Side (`BUY` buy / `SELL` sell).  
» type | string | Order type (`LIMIT` limit / `MARKET` market).  
» attribute | string | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
» exchange_type | string | Venue bucket (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN`).  
» business_type | string | Business type (`SPOT` Spot / `FUTURE` Futures / `MARGIN` Margin).  
» qty | string | Order quantity in the base currency.  
» quote_qty | string | Order quantity in the quote currency.  
» price | string | Order price.  
» time_in_force | string | Time in force (default `GTC`; enum: `GTC` / `IOC` / `FOK` / `POC`).  
» executed_qty | string | Filled base amount.  
» executed_amount | string | Filled quote amount.  
» executed_avg_price | string | Average Filled Price  
» fee_coin | string | Fee currency  
» fee | string | Fee amount.  
» reduce_only | string | Reduce-only order (`"true"` or `"false"`).  
» leverage | string | Order leverage multiplier.  
» reason | string | Failure reason description.  
» last_executed_qty | string | Base quantity of the latest fill.  
» last_executed_price | string | Price of the latest fill.  
» last_executed_amount | string | Quote amount of the latest fill.  
» position_side | string | Position side (`NONE` flat / `LONG` long / `SHORT` short).  
» create_time | string | Created time  
» update_time | string | Update time  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
    

##  Flash Swap Inquiry🔒 Authenticated

POST`/crossex/convert/quote`

POST `/crossex/convert/quote`

_Flash Swap Inquiry_

Rate Limit: 100 requests per day

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexConvertQuoteRequest | Optional | none  
↳ exchange_type | body | string | Required | Exchange Type  
↳ from_coin | body | string | Required | Asset Sold  
↳ to_coin | body | string | Required | Asset name to buy (OKX and GATE only allow BTC, ETH, USDT; BN only allows USDT)  
↳ from_amount | body | string | Required | Amount to sell  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexConvertQuoteResponse  
  
### Response Schema

Status Code **200**

_CrossexConvertQuoteResponse_

Name | Type | Description  
---|---|---  
» quote_id | string | Quote ID  
» valid_ms | string | Valid time (milliseconds timestamp)  
» from_coin | string | Asset Sold  
» to_coin | string | Asset Bought  
» from_amount | string | Amount to sell  
» to_amount | string | Amount to buy  
» price | string | Price  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
↳ quote_id | body | string | Required | Inquiry ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexConvertOrderResponse  
  
### Response Schema

Status Code **200**

_CrossexConvertOrderResponse_

Name | Type | Description  
---|---|---  
» order_id | string | Order ID  
» text | string | Order ID (cannot be customized)  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
    

##  Modify Account Contract Position Mode and Account Mode🔒 Authenticated

PUT`/crossex/accounts`

PUT `/crossex/accounts`

_Modify Account Contract Position Mode and Account Mode_

Rate Limit: 100 requests per 60 seconds. position_mode+exchange_type modifies contract position mode (exchange_type is required when the user's account mode is split exchange); account_mode modifies the user's account mode.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexAccountUpdateRequest | Optional | none  
↳ position_mode | body | string | Optional | Futures position mode (SINGLE/DUAL)  
↳ account_mode | body | string | Optional | Account mode (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
↳ exchange_type | body | string | Optional | Exchange (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to adjust futures position mode.  
  
### Responses

  * 202[Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexAccountUpdateResponse  
  
### Response Schema

Status Code **202**

_CrossexAccountUpdateResponse_

Name | Type | Description  
---|---|---  
» position_mode | string | Requested futures position mode to modify (SINGLE/DUAL)  
» account_mode | string | Requested account mode to modify (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
» exchange_type | string | Exchange targeted by the requested change (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to change futures position mode.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/accounts'
    query_param = ''
    body='{"position_mode":"string","account_mode":"string","exchange_type":"string"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('PUT', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('PUT', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="//"
    prefix="//"
    method="PUT"
    url="/crossex/accounts"
    query_param=""
    body_param='{"position_mode":"string","account_mode":"string","exchange_type":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    

> Example responses

> 202 Response
    
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    

##  Query Account Assets🔒 Authenticated

GET`/crossex/accounts`

GET `/crossex/accounts`

_Query Account Assets_

Rate Limit: 200 requests per 10 seconds If 100% ≤ initial_margin_rate < 110%, transferring out the margin currency is prohibited. If initial_margin_rate < 100%, the system will automatically cancel orders; only closing positions is allowed, not opening new ones. If maintenance_margin_rate ≤ 100%, the system will force liquidation.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
exchange_type | query | string | Optional | Trading venue identifier. Omit in cross-exchange mode; required in isolated-per-venue mode (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN`).  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexAccount  
  
### Response Schema

Status Code **200**

_CrossexAccount_

Name | Type | Description  
---|---|---  
» user_id | string | User ID  
» available_margin | string | Available Margin  
» margin_balance | string | marginbalance  
» initial_margin | string | Initial Margin  
» maintenance_margin | string | Maintenance margin  
» initial_margin_rate | string | Initial margin rate  
» maintenance_margin_rate | string | Maintenance margin rate  
» position_mode | string | Contract Position Mode  
» account_limit | string | Account limit  
» create_time | string | Created time  
» update_time | string | Update time  
» account_mode | string | Account Mode. CROSS_EXCHANGE: Cross-Exchange Mode; ISOLATED_EXCHANGE: Split-Exchange Mode  
» exchange_type | string | Exchange Type. When account_mode is CROSS_EXCHANGE, it must be CROSSEX; otherwise, it is another exchange.  
» assets | array | Asset list: grouped by exchange and currency, returning per-account balances, margin, and PnL details  
»» CrossexAccountAsset | object | none  
»»» user_id | string | User ID  
»»» coin | string | Currency  
»»» exchange_type | string | Exchange  
»»» balance | string | Balance  
»»» upnl | string | Unrealized P&L  
»»» equity | string | Equity (only USDT has a value; other assets are 0)  
»»» futures_initial_margin | string | Futures initial margin (only USDT has a value; other assets are 0)  
»»» futures_maintenance_margin | string | Futures maintenance margin (only USDT has a value; other assets are 0)  
»»» borrowing_initial_margin | string | Margin trading initial margin (only USDT has a value; other assets are 0)  
»»» borrowing_maintenance_margin | string | Margin trading maintenance margin (only USDT has a value; other assets are 0)  
»»» available_balance | string | Available Balance  
»»» liability | string | Liabilities (only meaningful in isolated exchange mode; always 0 in cross-exchange mode)  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
    

##  Modify Contract Trading Pair Leverage Multiplier🔒 Authenticated

POST`/crossex/positions/leverage`

POST `/crossex/positions/leverage`

_Modify Contract Trading Pair Leverage Multiplier_

Rate Limit: 100 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexLeverageRequest | Optional | none  
↳ symbol | body | string | Required | Currency pair  
↳ leverage | body | string | Required | leverage  
  
### Responses

  * 202[Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexLeverageResponse  
  
### Response Schema

Status Code **202**

_CrossexLeverageResponse_

Name | Type | Description  
---|---|---  
» symbol | string | Currency pair  
» leverage | string | Requested Modified Leverage  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
      "symbol": "string",
      "leverage": "string"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline  
  
### Response Schema

Status Code **200**

_Mapping from trading pair to leverage multiplier._

Name | Type | Description  
---|---|---  
» **additionalProperties** | string | Leverage multiplier for the corresponding trading pair  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
    

##  Modify Leveraged Trading Pair Leverage Multiplier🔒 Authenticated

POST`/crossex/margin_positions/leverage`

POST `/crossex/margin_positions/leverage`

_Modify Leveraged Trading Pair Leverage Multiplier_

Rate Limit: 100 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexLeverageRequest | Optional | none  
↳ symbol | body | string | Required | Currency pair  
↳ leverage | body | string | Required | leverage  
  
### Responses

  * 202[Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexLeverageResponse  
  
### Response Schema

Status Code **202**

_CrossexLeverageResponse_

Name | Type | Description  
---|---|---  
» symbol | string | Currency pair  
» leverage | string | Requested Modified Leverage  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline  
  
### Response Schema

Status Code **200**

_Mapping from trading pair to leverage multiplier._

Name | Type | Description  
---|---|---  
» **additionalProperties** | string | Leverage multiplier for the corresponding trading pair  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
    

##  Full Close Position🔒 Authenticated

POST`/crossex/position`

POST `/crossex/position`

_Full Close Position_

Rate Limit: 100 requests per day. Automatic close-out rules. Supports closing FUTURE or MARGIN positions.

Prerequisites before using this interface:

  * No pending orders for the symbol exist in the current account.
  * When the system detects the position meets any of the following limits while prerequisites are met:
  * Less than or equal to the minimum notional amount (minNotional)
  * Less than or equal to the minimum order quantity (minSize)

After meeting the conditions, the system will automatically generate a close-out order and immediately fully close the position. This interface is used to avoid issues where orders are too small to be placed on the exchange, ensuring small positions can be closed smoothly when reaching the threshold.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexClosePositionRequest | Optional | none  
↳ symbol | body | string | Required | Trading Pair  
1\. Supports leveraged trading pairs, e.g., BINANCE_MARGIN_SOL_USDT  
2\. Supports contract trading pairs, e.g., OKX_FUTURE_ETH_USDT  
↳ position_side | body | string | Optional | Position Direction  
1\. For leveraged positions, this parameter must be passed  
2\. For contract positions, pass selectively based on your contract holding method  
  
####  Detailed descriptions

**» symbol** : Trading Pair  
1\. Supports leveraged trading pairs, e.g., BINANCE_MARGIN_SOL_USDT  
2\. Supports contract trading pairs, e.g., OKX_FUTURE_ETH_USDT

**» position_side** : Position Direction  
1\. For leveraged positions, this parameter must be passed  
2\. For contract positions, pass selectively based on your contract holding method

### Responses

  * 202[Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexOrderActionResponse  
  
### Response Schema

Status Code **202**

_CrossexOrderActionResponse_

Name | Type | Description  
---|---|---  
» order_id | string | Order ID  
» text | string | User-defined Order ID  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexInterestRate | object | none  
»» coin | string | Currency  
»» exchange_type | string | Exchange  
»» hour_interest_rate | string | Hourly Interest Rate  
»» time | string | Millisecond Timestamp  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

_CrossexFee_

Name | Type | Description  
---|---|---  
CrossexFee | array | none  
» exchange_type | string | Exchange  
» spot_maker_fee | string | spotMakerfee rate  
» spot_taker_fee | string | spotTakerfee rate  
» future_maker_fee | string | contractMakerfee rate  
» future_taker_fee | string | contractTakerfee rate  
» special_fee_list | array | none  
»» CrossexSpecialFee | object | none  
»»» symbol | string | Currency pair  
»»» taker_fee_rate | string | Taker fee rate  
»»» maker_fee_rate | string | Maker fee rate  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "special_fee_list": []
      },
      {
        "exchange_type": "OKX",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
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
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "special_fee_list": []
      },
      {
        "exchange_type": "BYBIT",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
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
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexPosition | object | none  
»» user_id | string | User ID  
»» position_id | string | Position ID  
»» symbol | string | Currency pair  
»» position_side | string | Position Direction  
»» initial_margin | string | Initial Margin  
»» maintenance_margin | string | Maintenance margin  
»» position_qty | string | Position Quantity  
»» position_value | string | Position Value  
»» upnl | string | Unrealized P&L  
»» upnl_rate | string | Unrealized P&L Ratio  
»» entry_price | string | Position Average Entry Price  
»» mark_price | string | Mark price  
»» leverage | string | Position Leverage  
»» max_leverage | string | Maximum leverage  
»» risk_limit | string | Position risk limit  
»» fee | string | Position Fee  
»» funding_fee | string | Position Funding Fee  
»» funding_time | string | Position funding fee collection time (0 indicates it has not been collected yet)  
»» create_time | string | Position Creation Time  
»» update_time | string | Position Update Time  
»» closed_pnl | string | Realized PnL  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
        "maintenance_margin": "0.06229625",
        "position_qty": "10",
        "position_value": "5.795",
        "upnl": "0.369",
        "upnl_rate": "0.068005897530409141",
        "entry_price": "0.5426",
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexMarginPosition | object | none  
»» user_id | string | User ID  
»» position_id | string | Leveraged Position ID  
»» symbol | string | Trading Pair  
»» position_side | string | Position Direction  
»» initial_margin | string | Initial position margin  
»» maintenance_margin | string | Position maintenance margin  
»» asset_qty | string | Position Asset Quantity  
»» asset_coin | string | Position Asset Currency  
»» position_value | string | Position Value  
»» liability | string | Debt Quantity  
»» liability_coin | string | Debt Currency  
»» interest | string | Deducted Interest  
»» max_position_qty | string | Max Trade Size  
»» entry_price | string | Position Cost Price (Average Opening Price)  
»» index_price | string | Index price  
»» upnl | string | Unrealized P&L  
»» upnl_rate | string | Unrealized P&L Ratio  
»» leverage | string | Opening Leverage  
»» max_leverage | string | Maximum leverage  
»» create_time | string | Created time  
»» update_time | string | Update time  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexAdlRank | object | none  
»» user_id | string | User ID  
»» symbol | string | Currency pair  
»» crossex_adl_rank | string | CROSSEX position-reduction indicator ranking (1–5, higher value ranks higher)  
»» exchange_adl_rank | string | Original exchange information (BINANCE: 0–4, higher value ranks higher; OKX: 0–5, higher value ranks higher; GATE: 1–5, lower value ranks higher; BYBIT: 0–5, higher value ranks higher)  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [CrossexOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» CrossexOrder | CrossexOrder | none  
»» user_id | string | User ID  
»» order_id | string | Order ID  
»» text | string | Client-defined order ID.  
»» state | string | Order status:  
  
NEW: Validated and queued to be sent to the exchange.  
  
OPEN: Resting on the exchange order book.  
  
PARTIALLY_FILLED: Partially filled.  
  
FILLED: Fully filled.  
  
FAIL: CrossEx internal validation failed; see the `reason` field for details.  
  
REJECT: Rejected by the exchange; see the `reason` field for details.  
»» symbol | string | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
»» side | string | Side (`BUY` buy / `SELL` sell).  
»» type | string | Order type (`LIMIT` limit / `MARKET` market).  
»» attribute | string | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
»» exchange_type | string | Venue bucket (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN`).  
»» business_type | string | Business type (`SPOT` Spot / `FUTURE` Futures / `MARGIN` Margin).  
»» qty | string | Order quantity in the base currency.  
»» quote_qty | string | Order quantity in the quote currency.  
»» price | string | Order price.  
»» time_in_force | string | Time in force (default `GTC`; enum: `GTC` / `IOC` / `FOK` / `POC`).  
»» executed_qty | string | Filled base amount.  
»» executed_amount | string | Filled quote amount.  
»» executed_avg_price | string | Average Filled Price  
»» fee_coin | string | Fee currency  
»» fee | string | Fee amount.  
»» reduce_only | string | Reduce-only order (`"true"` or `"false"`).  
»» leverage | string | Order leverage multiplier.  
»» reason | string | Failure reason description.  
»» last_executed_qty | string | Base quantity of the latest fill.  
»» last_executed_price | string | Price of the latest fill.  
»» last_executed_amount | string | Quote amount of the latest fill.  
»» position_side | string | Position side (`NONE` flat / `LONG` long / `SHORT` short).  
»» create_time | string | Created time  
»» update_time | string | Update time  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
    

##  queryorderhistory🔒 Authenticated

GET`/crossex/history_orders`

GET `/crossex/history_orders`

_queryorderhistory_

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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [CrossexOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» CrossexOrder | CrossexOrder | none  
»» user_id | string | User ID  
»» order_id | string | Order ID  
»» text | string | Client-defined order ID.  
»» state | string | Order status:  
  
NEW: Validated and queued to be sent to the exchange.  
  
OPEN: Resting on the exchange order book.  
  
PARTIALLY_FILLED: Partially filled.  
  
FILLED: Fully filled.  
  
FAIL: CrossEx internal validation failed; see the `reason` field for details.  
  
REJECT: Rejected by the exchange; see the `reason` field for details.  
»» symbol | string | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
»» side | string | Side (`BUY` buy / `SELL` sell).  
»» type | string | Order type (`LIMIT` limit / `MARKET` market).  
»» attribute | string | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
»» exchange_type | string | Venue bucket (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN`).  
»» business_type | string | Business type (`SPOT` Spot / `FUTURE` Futures / `MARGIN` Margin).  
»» qty | string | Order quantity in the base currency.  
»» quote_qty | string | Order quantity in the quote currency.  
»» price | string | Order price.  
»» time_in_force | string | Time in force (default `GTC`; enum: `GTC` / `IOC` / `FOK` / `POC`).  
»» executed_qty | string | Filled base amount.  
»» executed_amount | string | Filled quote amount.  
»» executed_avg_price | string | Average Filled Price  
»» fee_coin | string | Fee currency  
»» fee | string | Fee amount.  
»» reduce_only | string | Reduce-only order (`"true"` or `"false"`).  
»» leverage | string | Order leverage multiplier.  
»» reason | string | Failure reason description.  
»» last_executed_qty | string | Base quantity of the latest fill.  
»» last_executed_price | string | Price of the latest fill.  
»» last_executed_amount | string | Quote amount of the latest fill.  
»» position_side | string | Position side (`NONE` flat / `LONG` long / `SHORT` short).  
»» create_time | string | Created time  
»» update_time | string | Update time  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexHistoricalPosition | object | none  
»» position_id | string | Position ID  
»» user_id | string | User ID  
»» symbol | string | Currency pair  
»» closed_type | string | Position close type (PARTIAL_CLOSED: partially closed; COMPLETE_CLOSED: fully closed)  
»» closed_pnl | string | Close Position P&L  
»» closed_pnl_rate | string | Close Position P&L Ratio  
»» open_avg_price | string | Average Opening Price  
»» closed_avg_price | string | Average Close Price  
»» max_position_qty | string | Max Trade Size  
»» closed_qty | string | Close Position Quantity  
»» closed_value | string | Close Position Value  
»» fee | string | Position Accumulated Fees  
»» liq_fee | string | Liquidation Fee  
»» funding_fee | string | Funding Fee  
»» position_side | string | Position Direction Before Close  
»» position_mode | string | Position Mode at Close  
»» leverage | string | Leverage at Close  
»» business_type | string | Business Type  
»» create_time | string | Created time  
»» update_time | string | Update time  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
        "update_time": "1750941402661"
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexHistoricalMarginPosition | object | none  
»» position_id | string | Position ID  
»» user_id | string | User ID  
»» symbol | string | Currency pair  
»» closed_type | string | Position close type (PARTIAL_CLOSED: partially closed; COMPLETE_CLOSED: fully closed)  
»» closed_pnl | string | Close Position P&L  
»» closed_pnl_rate | string | Close Position P&L Ratio  
»» open_avg_price | string | Average Opening Price  
»» closed_avg_price | string | Average Close Price  
»» max_position_qty | string | Max Trade Size  
»» closed_qty | string | Close Position Quantity  
»» closed_value | string | Close Position Value  
»» liq_fee | string | Liquidation Fee  
»» position_side | string | Position Direction Before Close  
»» leverage | string | Leverage at Close  
»» interest | string | Total Deducted Interest  
»» business_type | string | Position Business Type  
»» create_time | string | Created time  
»» update_time | string | Update time  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
from | query | integer | Optional | none  
to | query | integer | Optional | none  
page | query | integer | Optional | none  
limit | query | integer | Optional | none  
exchange_type | query | string | Optional | none  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexMarginInterestRecord | object | none  
»» userId | string | User ID  
»» symbol | string | Trading Pair  
»» interest_id | string | Interest Deduction ID  
»» liability_id | string | Debt Source ID, can be Order ID or Position ID  
»» liability | string | Debt Quantity  
»» liability_coin | string | Debt Currency  
»» interest | string | Interest  
»» interest_rate | string | interest rate  
»» interest_type | string | Interest deduction type (`PERIODIC_POSITION` hourly interest on position, `PERIODIC_OPEN_ORDER` hourly interest on open orders, `IMMEDIATE_OPEN_ORDER` interest charged on order placement, `PERIODIC_ISOLATED` hourly interest on debt)  
»» create_time | string | Created time  
»» exchange_type | string | Exchange  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
        "exchange_type": ""
      }
    ]
    

##  queryfilledhistory🔒 Authenticated

GET`/crossex/history_trades`

GET `/crossex/history_trades`

_queryfilledhistory_

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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexTrade | object | none  
»» user_id | string | User ID  
»» transaction_id | string | filledrecordsID  
»» order_id | string | Order ID  
»» text | string | User Order ID  
»» symbol | string | Currency pair  
»» exchange_type | string | Exchange  
»» business_type | string | Business Type  
»» side | string | Buy/Sell Direction  
»» qty | string | Trading size  
»» price | string | Fill Price  
»» fee | string | fee  
»» fee_coin | string | Fee currency  
»» fee_rate | string | Fee Rate  
»» match_role | string | Filled Role  
»» rpnl | string | Realized P&L  
»» position_mode | string | Position Mode  
»» position_side | string | Position Direction  
»» create_time | string | Created time  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
        "position_mode": "BOTH",
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
statement_type | query | string | Optional | Bill entry type.  
from | query | integer | Optional | Start Millisecond Timestamp  
to | query | integer | Optional | End Millisecond Timestamp  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexAccountBookRecord | object | none  
»» id | string | Account Change Record ID  
»» user_id | string | User ID  
»» business_id | string | Business ID  
»» statement_type | string | Bill entry type  
»» exchange_type | string | Exchange  
»» coin | string | Currency  
»» change | string | Change amount (positive indicates transfer in; negative indicates transfer out)  
»» balance | string | Balance after change  
»» create_time | string | Created time  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
        "statement_type": "TRADING_FEE",
        "exchange_type": "BINANCE",
        "coin": "USDT",
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
exchange_type | query | string | Optional | OKX/GATE/BINANCE/BYBIT/KRAKEN  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» CrossexCoinDiscountRate | object | none  
»» coin | string | Currency  
»» exchange_type | string | Exchange  
»» tier | string | Tier  
»» min_value | string | Minimum value  
»» max_value | string | Maximum value  
»» discount_rate | string | Discount rate  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "//"
    prefix = "//"
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
    host="//"
    prefix="//"
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
    

#  Schemas

##  Symbol

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Unique trading pair identifier in the form ExchangeType_BusinessType_Base_Counter.  
exchange_type | string | Required | none | Venue bucket (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN`).  
business_type | string | Required | none | Business type (`SPOT` Spot / `FUTURE` Futures / `MARGIN` Margin).  
state | string | Required | none | Status (`live` running / `suspend` paused).  
min_size | string | Required | none | Minimum order size allowed by the contract  
min_notional | string | Required | none | Minimum Order Value  
lot_size | string | Required | none | Quantity Step  
tick_size | string | Required | none | Price Step  
max_num_orders | string | Required | none | maximumopen orderamount  
max_market_size | string | Required | none | Maximum Market Order Quantity  
max_limit_size | string | Required | none | Maximum order quantity for limit orders.  
contract_size | string | Required | none | Contract Multiplier  
liquidation_fee | string | Required | none | Liquidation Fee Rate  
delist_time | string | Required | none | Millisecond timestamp; `0` means not delisted.  
      
    
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
      "delist_time": "string"
    }
    
    

##  CrossexOrder

_CrossexOrder_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_id | string | Required | none | User ID  
order_id | string | Required | none | Order ID  
text | string | Required | none | Client-defined order ID.  
state | string | Required | none | Order status:  
  
NEW: Validated and queued to be sent to the exchange.  
  
OPEN: Resting on the exchange order book.  
  
PARTIALLY_FILLED: Partially filled.  
  
FILLED: Fully filled.  
  
FAIL: CrossEx internal validation failed; see the `reason` field for details.  
  
REJECT: Rejected by the exchange; see the `reason` field for details.  
symbol | string | Required | none | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
side | string | Required | none | Side (`BUY` buy / `SELL` sell).  
type | string | Required | none | Order type (`LIMIT` limit / `MARKET` market).  
attribute | string | Required | none | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
exchange_type | string | Required | none | Venue bucket (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN`).  
business_type | string | Required | none | Business type (`SPOT` Spot / `FUTURE` Futures / `MARGIN` Margin).  
qty | string | Required | none | Order quantity in the base currency.  
quote_qty | string | Required | none | Order quantity in the quote currency.  
price | string | Required | none | Order price.  
time_in_force | string | Required | none | Time in force (default `GTC`; enum: `GTC` / `IOC` / `FOK` / `POC`).  
executed_qty | string | Required | none | Filled base amount.  
executed_amount | string | Required | none | Filled quote amount.  
executed_avg_price | string | Required | none | Average Filled Price  
fee_coin | string | Required | none | Fee currency  
fee | string | Required | none | Fee amount.  
reduce_only | string | Required | none | Reduce-only order (`"true"` or `"false"`).  
leverage | string | Required | none | Order leverage multiplier.  
reason | string | Required | none | Failure reason description.  
last_executed_qty | string | Required | none | Base quantity of the latest fill.  
last_executed_price | string | Required | none | Price of the latest fill.  
last_executed_amount | string | Required | none | Quote amount of the latest fill.  
position_side | string | Required | none | Position side (`NONE` flat / `LONG` long / `SHORT` short).  
create_time | string | Required | none | Created time  
update_time | string | Required | none | Update time  
      
    
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
    
    

##  CrossexOrderActionResponse

_CrossexOrderActionResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Required | none | Order ID  
text | string | Required | none | User-defined Order ID  
      
    
    {
      "order_id": "string",
      "text": "string"
    }
    
    

##  CrossexLeverageResponse

_CrossexLeverageResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Currency pair  
leverage | string | Required | none | Requested Modified Leverage  
      
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    
    

##  CrossexTransferRequest

_Fund Transfer Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
coin | string | Required | none | Currency  
amount | string | Required | none | Transfer amount  
from | string | Required | none | `from` receiving account (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX`, `SPOT`).  
to | string | Required | none | `to` debit account (funds withdrawn from): `CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX`, `SPOT`  
text | string | Optional | none | User-defined ID  
      
    
    {
      "coin": "string",
      "amount": "string",
      "from": "string",
      "to": "string",
      "text": "string"
    }
    
    

##  CrossexOrderRequest

_Place Order Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
text | string | Optional | none | Client-defined Order ID, supports letters (a-z), numbers (0-9), symbols (-, _) only  
symbol | string | Required | none | Unique identifier `{Exchange}_{Business}_{Base}_{Counter}`  
Examples:  
To send a Binance spot order on `ADA/USDT`, use `BINANCE_SPOT_ADA_USDT`;  
For an ADA/USDT-margined USDT perpetual futures order on OKX, use `OKX_FUTURE_ADA_USDT`;  
For ADA/USDT margin trading on Gate, use `GATE_MARGIN_ADA_USDT`;  
For ADA/USDT spot trading on Bybit, use `BYBIT_SPOT_ADA_USDT`;  
For ADA/USDT-linked futures routing on Kraken, use `KRAKEN_FUTURE_ADA_USD`;  
Supports spot trades, USDT-margined perpetual futures, and spot margin templates. BYBIT omits spot margin for now; Kraken omits dedicated spot/margin legs inside CrossEx.  
side | string | Required | none | BUY, SELL  
type | string | Optional | none | Order type (default: `LIMIT`; supported types: `LIMIT`, `MARKET`)  
time_in_force | string | Optional | none | Default GTC, supports enumerated types: GTC, IOC, FOK, POC  
GTC: GoodTillCancelled  
IOC: ImmediateOrCancelled  
FOK: FillOrKill  
POC: PendingOrCancelled or PostOnly  
qty | string | Optional | none | Order quantity (required unless spot market buy)  
price | string | Optional | none | Limit Order Price (Required for Limit Orders)  
quote_qty | string | Optional | none | Order quote quantity; required for spot and margin market buy orders  
reduce_only | string | Optional | none | Reduce-only: `true` or `false`  
position_side | string | Optional | none | Position side: `NONE`, `LONG`, `SHORT`  
Defaults to `NONE` (single position mode) if not specified  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
side | BUY  
side | SELL  
type | LIMIT  
type | MARKET  
time_in_force | GTC  
time_in_force | IOC  
time_in_force | FOK  
time_in_force | POC  
reduce_only | true  
reduce_only | false  
position_side | LONG  
position_side | SHORT  
position_side | NONE  
      
    
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
    
    

##  CrossexOrderUpdateRequest

_Order Modification Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
qty | string | Optional | none | modify amount  
price | string | Optional | none | modify price  
      
    
    {
      "qty": "string",
      "price": "string"
    }
    
    

##  CrossexConvertQuoteRequest

_Flash Swap Quote Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
exchange_type | string | Required | none | Exchange Type  
from_coin | string | Required | none | Asset Sold  
to_coin | string | Required | none | Asset name to buy (OKX and GATE only allow BTC, ETH, USDT; BN only allows USDT)  
from_amount | string | Required | none | Amount to sell  
      
    
    {
      "exchange_type": "string",
      "from_coin": "string",
      "to_coin": "string",
      "from_amount": "string"
    }
    
    

##  CrossexConvertOrderRequest

_Flash Swap Transaction Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
quote_id | string | Required | none | Inquiry ID  
      
    
    {
      "quote_id": "string"
    }
    
    

##  CrossexAccountUpdateRequest

_Change Account Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
position_mode | string | Optional | none | Futures position mode (SINGLE/DUAL)  
account_mode | string | Optional | none | Account mode (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
exchange_type | string | Optional | none | Exchange (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to adjust futures position mode.  
      
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    
    

##  CrossexLeverageRequest

_Change Leverage Request Body (for futures/margin)_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Currency pair  
leverage | string | Required | none | leverage  
      
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    
    

##  CrossexClosePositionRequest

_Full Close Position Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Trading Pair  
1\. Supports leveraged trading pairs, e.g., BINANCE_MARGIN_SOL_USDT  
2\. Supports contract trading pairs, e.g., OKX_FUTURE_ETH_USDT  
position_side | string | Optional | none | Position Direction  
1\. For leveraged positions, this parameter must be passed  
2\. For contract positions, pass selectively based on your contract holding method  
      
    
    {
      "symbol": "string",
      "position_side": "string"
    }
    
    

##  CrossexTransferResponse

_CrossexTransferResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
tx_id | string | Required | none | Order ID  
text | string | Required | none | User-defined Order ID  
      
    
    {
      "tx_id": "string",
      "text": "string"
    }
    
    

##  CrossexConvertQuoteResponse

_CrossexConvertQuoteResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
quote_id | string | Required | none | Quote ID  
valid_ms | string | Required | none | Valid time (milliseconds timestamp)  
from_coin | string | Required | none | Asset Sold  
to_coin | string | Required | none | Asset Bought  
from_amount | string | Required | none | Amount to sell  
to_amount | string | Required | none | Amount to buy  
price | string | Required | none | Price  
      
    
    {
      "quote_id": "string",
      "valid_ms": "string",
      "from_coin": "string",
      "to_coin": "string",
      "from_amount": "string",
      "to_amount": "string",
      "price": "string"
    }
    
    

##  CrossexConvertOrderResponse

_CrossexConvertOrderResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Required | none | Order ID  
text | string | Required | none | Order ID (cannot be customized)  
      
    
    {
      "order_id": "string",
      "text": "string"
    }
    
    

##  CrossexAccount

_CrossexAccount_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_id | string | Required | none | User ID  
available_margin | string | Required | none | Available Margin  
margin_balance | string | Required | none | marginbalance  
initial_margin | string | Required | none | Initial Margin  
maintenance_margin | string | Required | none | Maintenance margin  
initial_margin_rate | string | Required | none | Initial margin rate  
maintenance_margin_rate | string | Required | none | Maintenance margin rate  
position_mode | string | Required | none | Contract Position Mode  
account_limit | string | Optional | none | Account limit  
create_time | string | Required | none | Created time  
update_time | string | Required | none | Update time  
account_mode | string | Optional | none | Account Mode. CROSS_EXCHANGE: Cross-Exchange Mode; ISOLATED_EXCHANGE: Split-Exchange Mode  
exchange_type | string | Optional | none | Exchange Type. When account_mode is CROSS_EXCHANGE, it must be CROSSEX; otherwise, it is another exchange.  
assets | array | Required | none | Asset list: grouped by exchange and currency, returning per-account balances, margin, and PnL details  
↳ CrossexAccountAsset | object | Optional | none | none  
↳ user_id | string | Optional | none | User ID  
↳ coin | string | Optional | none | Currency  
↳ exchange_type | string | Optional | none | Exchange  
↳ balance | string | Optional | none | Balance  
↳ upnl | string | Optional | none | Unrealized P&L  
↳ equity | string | Optional | none | Equity (only USDT has a value; other assets are 0)  
↳ futures_initial_margin | string | Optional | none | Futures initial margin (only USDT has a value; other assets are 0)  
↳ futures_maintenance_margin | string | Optional | none | Futures maintenance margin (only USDT has a value; other assets are 0)  
↳ borrowing_initial_margin | string | Required | none | Margin trading initial margin (only USDT has a value; other assets are 0)  
↳ borrowing_maintenance_margin | string | Required | none | Margin trading maintenance margin (only USDT has a value; other assets are 0)  
↳ available_balance | string | Optional | none | Available Balance  
↳ liability | string | Optional | none | Liabilities (only meaningful in isolated exchange mode; always 0 in cross-exchange mode)  
      
    
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
    
    

##  CrossexAccountUpdateResponse

_CrossexAccountUpdateResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
position_mode | string | Optional | none | Requested futures position mode to modify (SINGLE/DUAL)  
account_mode | string | Optional | none | Requested account mode to modify (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
exchange_type | string | Optional | none | Exchange targeted by the requested change (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to change futures position mode.  
      
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    
    

Last Updated: 1/20/2026, 7:36:57 AM