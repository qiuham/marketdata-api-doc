---
exchange: gateio
source_url: https://www.gate.com/docs/developers/crossex/en
api_type: Trading
updated_at: 2026-11-13 20:58:21.531688
---

# Gate CrossEx API v1.0.8

* Python 
  * Shell 

v1.0.8 · Stable


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

CrossEx is a cross-exchange trading platform that allows users to trade across multiple exchanges (Binance, OKX, Gate, Bybit, Kraken, Hyperliquid, Deribit, Lighter, Aster) through a unified account. The CrossEx API provides complete account management, asset transfers, order placement, and position management functions across exchanges.

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

**v1.0.8**

2026-11-09

  * Clarify the `coin` restriction for `POST /crossex/transfers`. When either `from` or `to` is `CROSSEX_DERIBIT`, only `USDC` is supported.

**v1.0.7**

2026-11-02

  * Add `GET /crossex/rule/open_capacity` (`listCrossexRuleOpenCapacity`) with required response fields `symbol`, `position_side` (`LONG`/`SHORT`), and `available_to_open_notional`. Only trading pairs and position sides below the remaining opening capacity threshold are returned; `0` means no position can currently be opened for that pair and side.

**v1.0.6**

2026-10-12

  * Add stock and ETF trading for US, Hong Kong, South Korean, and Japanese markets to CrossEx. Symbols use `{market}_{STOCK_or_ETF}_{security_code}_USDT`.
  * Add `GET /crossex/security_positions` to query security positions, and document stock and ETF order restrictions, native market pricing currencies, and related fields.

**v1.0.5**

2026-09-15

  * Add `LIGHTER` exchange support to CrossEx: futures order symbols use `LIGHTER_FUTURE_{Base}_{Counter}`; `POST /crossex/transfers` supports USDC transfers between `CROSSEX_LIGHTER` and `SPOT`; `POST /crossex/convert/quote` supports swaps between `LIGHTER_USDC` and `CROSSEX_USDT` in cross-exchange mode.

**v1.0.4**

2026-08-24

  * Add optional `margin_mode` (`CROSS`/`ISOLATED`) to `GET /crossex/history_positions` response items
  * Add optional `position_side` (`NONE`/`LONG`/`SHORT`) to the `POST /crossex/positions/margin` response

**v1.0.3**

2026-08-10

  * Add Hyperliquid isolated margin support to CrossEx, including margin mode updates and queries, and isolated margin increases and decreases
  * Add Hyperliquid USDC Flash Swap support to CrossEx, including liability repayment
  * Clarify isolated margin and liquidation price fields, and update margin mode and isolated margin error labels

**v1.0.2**

2026-07-02

  * Add DERIBIT exchange support for CrossEx

2026-06-09

  * Add HYPERLIQUID exchange support for CrossEx

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

  * Unified account management across multiple exchanges (Binance, OKX, Gate, Bybit, Kraken, Hyperliquid, Deribit, Lighter, Aster)
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

When APIv4 rejects a request synchronously, the server returns a non-2xx HTTP status code and a JSON response body that describes the error. An asynchronously accepted order can still enter `FAIL` or `REJECT` later; handle those outcomes as described in the next section.

The error response body usually has the following format:
    
    
    {
      "label": "COMMON_PARAM_BIND_ERROR",
      "message": "Invalid parameter, please refer to API documentation"
    }
    

  * `label` is a stable `string` identifier selected from a predefined list. Use it to identify an error and implement programmatic error handling.
  * `message` (or `detail`) provides human-readable diagnostic information about the failure. Do not depend on this field for programmatic error handling.

The following Python [requests ](https://requests.readthedocs.io/en/latest/) example demonstrates the basic error-handling flow:

> This example only handles business errors returned by the API. Handle network failures, timeouts, and other transport-level errors separately.
    
    
    import requests
    
    r = requests.get("https://api.gateio.ws/api/v4/crossex/accounts")
    try:
        r.raise_for_status()
    except requests.HTTPError:
        # Catch non-2xx responses, parse the response body, and handle specific labels as needed.
        if r.json()['label'] == 'xxx':
            print(r.json())
    

##  Order rejection `reason`

To reduce response latency, CrossEx accepts order requests asynchronously. After accepting a request, the API returns an acknowledgement containing `order_id` and `text`, similar to placing a spot order with `action_mode=ACK`.

> An acknowledgement only confirms that CrossEx has accepted the request. It does not mean that the order has been successfully submitted to the target exchange or filled. Use the order query endpoints or order push notifications to obtain the final result.

After accepting an order, CrossEx performs the following steps:

  1. Revalidates the account's trading restrictions, available balance or margin, and risk status.
  2. If validation succeeds, submits the order to the target exchange.

An order may be rejected during CrossEx validation or by the target exchange. These cases use different order states and `reason` formats.

###  Rejected by CrossEx: `state = FAIL`

If an order violates CrossEx trading rules, balance or margin requirements, or risk controls, its state is `FAIL`.

In this case, `reason` is a JSON-encoded string containing a programmatically identifiable `label` and a human-readable `message`. Parse the `reason` string as JSON and use `label` for programmatic error handling.
    
    
    {
      "user_id": "123",
      "order_id": "xxx",
      "state": "FAIL",
      "reason": "{\"label\":\"TRADE_INSUFFICIENT_AVAILABLE_MARGIN_ERROR\",\"message\":\"Insufficient availableMargin\"}"
    }
    

###  Rejected by the target exchange: `state = REJECT`

If an order passes CrossEx validation but is rejected by the target exchange, its state is `REJECT`. In this case, `reason` preserves the raw error returned by the exchange. It is usually plain text, is not guaranteed to be valid JSON, and does not have a standardized `label`. Display or log it as a human-readable diagnostic message; do not depend on a fixed format for programmatic error handling.
    
    
    {
      "user_id": "123",
      "order_id": "xxx",
      "state": "REJECT",
      "reason": "Due to the order could not be executed as maker, the Post Only order will be rejected. The order will not be recorded in the order history"
    }
    

The following tables list common exchange rejection messages and suggested actions for troubleshooting. Error messages and trading rules vary by exchange; always consult the target exchange's official documentation for authoritative details.

###  Limit order rejections

Placeholders such as `${price}` represent dynamic values returned by the exchange. The actual `reason` contains the corresponding value or name.

Limit order rejections`reason` | `tips`  
---|---  
`Due to the order could not be executed ... The order will not be recorded in the order history` | The order cannot be executed under the requested time-in-force constraint. For POC/Post Only orders, adjust the limit price so the order does not immediately match the opposite side of the book. For FOK orders, reduce the order size, improve the limit price, or use another supported `time_in_force`.  
`EC_PostOnlyWillTakeLiquidity` | The Post Only order would immediately take liquidity. Lower the buy price or raise the sell price, or use a time-in-force mode that allows immediate execution.  
`Post only order would have immediately matched, bbo was ...` | The Post Only price has reached the best price on the opposite side of the book. Adjust the price using the returned best bid and offer (BBO) so the order rests on the order book instead of matching immediately.  
`label: ORDER_POC_IMMEDIATE, message: order price ... while counter price ...` | The POC order would immediately match the opposite side. A buy price must be below the best ask, and a sell price must be above the best bid.  
`label: ORDER_FOK, message: order can not be filled` | Available market depth is insufficient to fill the FOK order immediately and in full. Reduce the order size, improve the price, or use IOC/GTC.  
`iocWouldNotExecute` | No quantity can execute immediately at the specified IOC price. Adjust the price or retry when executable liquidity is available.  
`Order price is not within the price limit (max buy price: ${price}, min sell price: ${price})` | The order price is outside the exchange's permitted range. A buy price must not exceed `max buy price`, and a sell price must not be below `min sell price`. Adjust the price using the returned boundaries.  
`Limit price can't be higher than {price}` | The limit price exceeds the exchange maximum. Reduce it to the returned maximum price or below.  
`The lowest price limit for sell orders is ${price}` | The sell price is below the exchange minimum. Raise it to the returned minimum price or above.  
`The highest price limit for buy orders is ${price}` | The buy price exceeds the exchange maximum. Reduce it to the returned maximum price or below.  
`The counterparty's best price does not meet the PERCENT_PRICE filter limit.` | The best price on the opposite side is outside the exchange's price-protection range. Wait for the market to return to the permitted range or submit a limit order that satisfies the price filter.  
`label: PRICE_TOO_DEVIATED, message: order price ... while mark price ... and deviation-rate limit ...` | The order price deviates from the mark price by more than the permitted rate. Recalculate the order price using the returned mark price and deviation limit.  
`Price too far from oracle asset=${asset}` | The order price deviates too far from the oracle price. Refresh market data, adjust the price, and verify the price precision and order side.  
`label: RISK_LIMIT_EXCEEDED, message: position value (include pending orders) would reach to ... while risk limit is ...` | The combined value of the current position and open orders would exceed the risk limit. Reduce the order size, cancel open orders, or reduce the position first.  
`Order failed. ... the maximum position amount under current leverage ...` | The combined quantity of the current position, pending orders, and this order exceeds the position limit for the current leverage. Reduce the order size, cancel same-side orders, reduce the position, or adjust leverage.  
`Order must have minimum value of $10. asset=${asset}` | The order value is below the exchange minimum. Increase the size or price so the order value is at least 10 USD while still satisfying quantity precision requirements.  
`label: INVALID_PARAM_VALUE, message: Invalid request parameter tif value: rpi` | This exchange or endpoint does not accept `tif=rpi`. Confirm that the account and symbol are enabled for RPI; otherwise, use a supported standard `time_in_force`.  
`label: INVALID_PARAM_VALUE, message: TimeInForce rpi is not support` | The exchange, business type, or symbol does not support RPI orders. Route the order through an RPI-capable venue or use a supported mode such as GTC or IOC.  
`Only post-only orders allowed immediately after network upgrade` | The exchange temporarily accepts only Post Only orders following a network upgrade. Use Post Only or wait until the exchange restores other order types.  
`marketIsPostOnly` | The market is in a protective Post Only mode. Submit a Post Only order or wait until normal trading resumes.  
  
###  Exchange maintenance errors

CrossEx cannot place orders while the target exchange is under maintenance. Monitor the exchange's service announcements and retry after trading services recover.

Exchange maintenance errors`reason`  
---  
`Order processing error temporarily, please try again later`  
`Systems are busy. Please try again later.`  
`Service is stopping`  
`{"jsonrpc":"2.0","error":{"message":"system_maintenance","code":11051}}`  
`502 bad gateway`  
  
##  Error `label` list

The following errors are grouped by common business scenario. `message` is the raw error message returned by the API, and `tips` describes an action that can be taken to resolve the issue.

###  General, routing, and permission errors

General, routing, and permission errors`label` | `message` | `tips`  
---|---|---  
`COMMON_PARAM_BIND_ERROR` | Invalid Parameter, please check api doc | Verify field names, field types, and JSON syntax against the API documentation, then correct the request.  
`COMMON_MISSING_PARAM_ERROR` | Missing Parameter, please check api doc | Supply all required fields. Check the request body, path parameters, and query parameters for omissions.  
`TRADE_UNSUPPORTED_OPERATION` | This operation is not currently supported | The exchange, business type, or endpoint combination does not support this operation. Verify that all three are compatible.  
`NOT_BEST_ACCOUNT_ROUTER` | Your order was not executed. All trading channels are currently busy. Consider reducing the order amount, selecting a different exchange symbol, or trying again later. | Trading channels are busy. Reduce the order size, select a symbol on another exchange, or retry later.  
`TRADE_ASSET_NOT_EXISTS_ERROR` | Asset is not exists | The asset is not available in the account. Initialize the asset or transfer it into the account first.  
  
###  Account and account-mode errors

Account and account-mode errors`label` | `message` | `tips`  
---|---|---  
`USER_NOT_EXIST` | user does not exist | Retry later.  
`USER_DEACTIVATED` | User has been deactivated | The user is deactivated. Restore the user to an active state or contact support.  
`QUERY_INVALID_EXCHANGE_TYPE` | The exchange_type is invalid. When the account_mode is ISOLATED_EXCHANGE, it should be GATE, BINANCE, BYBIT, OKX, KRAKEN, HYPERLIQUID, DERIBIT or LIGHTER | In `ISOLATED_EXCHANGE` mode, use GATE, BINANCE, BYBIT, OKX, KRAKEN, HYPERLIQUID, DERIBIT, or LIGHTER.  
`TRADE_CHANGE_PZ_MODE_SAME_ERROR` | No need to repeatedly change your position mode | The account is already in the requested position mode; no update is required.  
`TRADE_PZ_MODE_HAVE_ORDER_ERROR` | Change failed. Please cancel any open order and close positions first. | Cancel all open futures orders before changing the position mode.  
`TRADE_PZ_MODE_HAVE_POSITION_ERROR` | Change failed. Please cancel any open order and close positions first. | Close all futures positions before changing the position mode.  
`UPDATE_ACCOUNT_PARAMETERS_ALL_EMPTY_ERROR` | The request parameters cannot all be empty. | Provide at least one account field to update.  
`UPDATE_ACCOUNT_PARAMETERS_ERROR` | Cannot set both positionMode and accountMode at the same time. | Update either `position_mode` or `account_mode` in a single request, not both.  
`UPDATE_ACCOUNT_EXCHANGE_TYPE_PARAMETERS_ERROR` | exchangeType must be provided with positionMode. | When providing `exchange_type`, also provide `position_mode`. Do not provide `exchange_type` by itself if the position mode is not being changed.  
`UPDATE_ACCOUNT_ACCOUNT_MODE_ERROR` | Invalid accountMode , please check api doc | Use an `account_mode` value supported by the endpoint.  
`UPDATE_ACCOUNT_EXCHANGE_TYPE_ERROR` | Invalid exchangeType , please check api doc | Use an `exchange_type` value supported by the endpoint.  
`UPDATE_ACCOUNT_PZ_ISOLATED_MODE_NOT_EXCHANGE_TYPE_ERROR` | When updating the position mode in isolated mode, the exchange type parameter is required. | Provide `exchange_type` when changing the position mode in isolated-exchange mode.  
`UPDATE_ACCOUNT_MODE_OPEN_ORDERS_EXIST_ERROR` | The account must not have any open orders to update the account mode. | Cancel all open orders before changing the account mode.  
`UPDATE_ACCOUNT_MODE_POSITION_NOT_EMPTY_ERROR` | The account must not have any open positions to update the account mode. | Close all futures and margin positions before changing the account mode.  
`UPDATE_ACCOUNT_MODE_INITIAL_MARGIN_NOT_ZERO_ERROR` | The account must have zero initial margin to update the account mode. | Cancel open orders and close positions, then confirm that initial margin is zero before changing the account mode.  
`UPDATE_ACCOUNT_MODE_MAINTENANCE_MARGIN_NOT_ZERO_ERROR` | The account must have zero maintenance margin to update the account mode. | Close all positions and confirm that maintenance margin is zero before changing the account mode.  
`UPDATE_ACCOUNT_MODE_ACCOUNT_STATUS_NOT_NORMAL_ERROR` | The account status must be NORMAL to update the account mode. | Wait until the account status returns to `NORMAL` before changing the account mode.  
`UPDATE_ACCOUNT_CROSSEX_MODE_EXCHANGE_TYPE_NOT_CROSSEX_ERROR` | In cross-exchange mode, the exchange type must be CROSSEX. | Set `exchange_type` to `CROSSEX` in cross-exchange mode.  
`UPDATE_ACCOUNT_ISOLATED_MODE_EXCHANGE_TYPE_NOT_CROSSEX_ERROR` | In isolated mode, the exchange type must not be CROSSEX. | Specify a target exchange in isolated-exchange mode; do not use `CROSSEX`.  
`TRADE_INVALID_PZ_MODE_ERROR` | Invalid positionMode | Use a `position_mode` supported by the endpoint.  
  
###  Convert errors

Convert errors`label` | `message` | `tips`  
---|---|---  
`CONVERT_TRADE_QUOTE_UNKNOWN_ERROR` | Convert trade request error, please try again later | The quote request failed temporarily. Request a new quote later; contact support if the error persists.  
`CONVERT_TRADE_QUOTE_EXCHANGE_INVALID_ERROR` | Invalid exchangeType , please check api doc | Use an `exchange_type` supported by the Convert endpoints.  
`CONVERT_TRADE_QUOTE_FROM_COIN_INVALID_ERROR` | Invalid fromCoin , please check api doc | Verify the spelling of `from_coin` and confirm that the asset is supported for conversion.  
`CONVERT_TRADE_QUOTE_TO_COIN_INVALID_ERROR` | Invalid toCoin, please check api doc | Verify `to_coin`, confirm that the conversion direction is supported, and ensure that the source and destination assets differ.  
`CONVERT_TRADE_QUOTE_FROM_AMOUNT_INVALID_ERROR` | Invalid fromAmount , please check api doc | `from_amount` must be a valid number with no more than 16 decimal places.  
`CONVERT_TRADE_QUOTE_FROM_AMOUNT_LIMIT_ERROR` | Invalid fromAmount, fromAmount can't be less than zero | `from_amount` must be greater than zero.  
`CONVERT_TRADE_QUOTE_FROM_AMOUNT_MAX_ERROR` | Invalid fromAmount, fromAmount value can't be greater than %s USDT | Keep `from_amount` at or below %s USDT.  
`CONVERT_TRADE_QUOTE_EXCHANGE_REJECT_ERROR` | Convert quote request reject by Exchange, reason : %s | Adjust the request according to the exchange-specific reason in `message`, then request a new quote.  
`TRADE_CONVERT_QUOTE_ERROR` | Quote does not exist or has expired | The quote does not exist, has expired, or has already been used. Request a new quote before placing the Convert order.  
  
###  Close-all-position errors

Close-all-position errors`label` | `message` | `tips`  
---|---|---  
`CAN_NOT_DELETE_POSITION` | With a position size of 0, it is impossible to completely close out the position. | The position size is already zero; no close-all operation is required.  
`CAN_NOT_DELETE_LARGE_POSITION` | The position size is too large to close at market price. Close the position by placing an order first. | The position is too large for the close-all operation. Reduce or close it using regular orders first.  
`OPEN_ORDERS_CAN_NOT_DELETE_POSITION` | Open orders exist, positions cannot be deleted. | Cancel all open orders for the symbol before using the close-all operation.  
  
###  Order parameters and symbols

Order parameters and symbols`label` | `message` | `tips`  
---|---|---  
`TRADE_CLIENT_ORDER_ID_LENGTH_ERROR` | The order_id must less than 64 | Shorten the client order ID to fewer than 64 characters.  
`TRADE_CLIENT_ORDER_ID_MATCH_ERROR` | Text only support letters and numbers | Use only letters, numbers, hyphens (`-`), and underscores (`_`) in the client order ID.  
`TRADE_INVALID_SIDE` | Invalid side | Use a side supported by the endpoint.  
`TRADE_INVALID_ORDER_TYPE` | Invalid order_type | Use an order type supported by the selected exchange and business type.  
`TRADE_INVALID_TIME_IN_FORCE` | Invalid time_in_force | Use a `time_in_force` compatible with the order type; for example, do not use POC for a market order.  
`TRADE_INVALID_POC` | Market order timeInForce can't be POC | A market order cannot use POC. Select a supported `time_in_force`.  
`TRADE_INVALID_ORDER_QTY` | Invalid qty | `qty` must be a valid number greater than zero and must satisfy the symbol's quantity precision.  
`TRADE_INVALID_QUOTE_ORDER_QTY` | Invalid quote_qty | `quote_qty` must be a valid number greater than zero.  
`TRADE_INVALID_LIMIT_PRICE` | Invalid limitPrice | Verify the price format and sign, and ensure that the price satisfies exchange constraints.  
`TRADE_INVALID_REDUCE_ONLY` | Invalid reduceOnly | `reduce_only` must be the string `"true"` or `"false"`.  
`TRADE_SYM_NOT_SUPPORT` | The symbol is not supported | Confirm that the symbol is listed, and verify the exchange, business type, and symbol spelling.  
`TRADE_NOT_SUPPORT_SYMBOLS_ERROR` | These symbols are not supported: [%s] | Remove the symbols listed in `message`, or replace them with listed symbols supported by the endpoint's business type.  
`TRADE_MARGIN_INVALID_PZ_SIDE_ERROR` | Invalid position_side, margin order position_side must be LONG or SHORT | A margin order must specify `LONG` or `SHORT` as `position_side`.  
`TRADE_INVALID_POSITION_SIDE` | Invalid position_side | Use a `position_side` compatible with the account's current position mode.  
`TRADE_INVALID_PZ_SIDE_ERROR` | Invalid position_side, your position_mode is dual, so position_side must be LONG or SHORT | In dual position mode, set `position_side` to `LONG` or `SHORT`.  
`TRADE_INVALID_EXCHANGE_TYPE` | Invalid exchange_type | Verify that the symbol prefix matches `exchange_type`, and use an exchange supported by the selected business type.  
`TRADE_INVALID_MARGIN_MODE_ERROR` | Invalid margin_mode | Set `margin_mode` to `CROSS` or `ISOLATED`.  
`TRADE_INVALID_SYM_BUSINESSTYPE_ERROR` | The symbol should be FUTURE businessType | This operation requires a `FUTURE` symbol; do not use a `SPOT` or `MARGIN` symbol.  
`TRADE_INVALID_MARGIN_SYM_BUSINESSTYPE_ERROR` | The symbol should be MARGIN businessType | This operation requires a `MARGIN` symbol; do not use a `SPOT` or `FUTURE` symbol.  
  
###  Order limits, queries, and amendments

Order limits, queries, and amendments`label` | `message` | `tips`  
---|---|---  
`TRADE_ORDER_DUPLICATE_ERROR` | Text duplicate | Use a unique client order ID; do not submit the same `text` more than once.  
`TRADE_ONE_OF_ORDER_ID_ERROR` | One of the order_id or text must be send | Provide at least one of `order_id` or `text`. If both are provided, `order_id` takes precedence.  
`TRADE_ORDER_ID_ERROR` | Invalid orderId | `order_id` must be a positive integer. Verify that `text` or another field was not supplied by mistake.  
`TRADE_ORDER_ID_LENGTH` | OrderId length must be 16 digits | Use the complete 16-digit `order_id` returned by the API; do not truncate or construct it.  
`TRADE_ORDER_NOT_FOUND_ERROR` | The order was not found | Verify the order ID, account ownership, and order state. A completed order may no longer be queryable by `text`.  
`TRADE_NOT_ALLOW_REPLACE` | Market order not allowed replace | Market orders cannot be amended. Cancel the order and place a new one.  
`TRADE_ORDER_REPLACE_QTY_PRICE_ERROR` | Replace price or qty invalid | Verify that the amended price and quantity are valid.  
`TRADE_ORDER_REPLACE_QTY_PRICE_SAME_ERROR` | The qty and price have not changed | Change at least one of price or quantity.  
`TRADE_ORDER_REPLACE_ALLOW_ERROR` | Order state or type not allow replace | Only limit orders in an amendable state can be amended.  
`TRADE_ORDER_LOT_SIZE_ERROR` | Order quantity is not multiple of lotSize | Adjust the order quantity to a multiple of `lot_size`.  
`TRADE_ORDER_QUANTITY_MAX_ERROR` | Order quantity should be less than the max quantity | Reduce the quantity so it does not exceed the symbol's maximum.  
`TRADE_ORDER_QUANTITY_MIN_ERROR` | Order quantity should be greater than the min quantity | Increase the quantity so it meets the symbol's minimum.  
`TRADE_ORDER_TICK_SIZE_ERROR` | Order price is not multiple of tickSize | Adjust the order price to a multiple of `tick_size`.  
`TRADE_ORDER_AMOUNT_MIN_ERROR` | Order amount should be greater than the min notional | Increase the quantity or price so the order value meets `min_notional`.  
`TRADE_MAX_ORDERS_ERROR` | The open order num exceeds the limit | Cancel open orders until the number of active orders falls below the limit.  
`TRADE_ORDER_REPLACE_INSUFFICIENT_AVAILABLE_ERROR` | Replace order failed. Insufficient available | The amended order requires more available balance. Reduce the new quantity or amount, or add funds.  
  
###  Positions, margin, and reduce-only orders

Positions, margin, and reduce-only orders`label` | `message` | `tips`  
---|---|---  
`MARGIN_ORDER_NOT_SUPPORT` | ISOLATED_EXCHANGE account mode does not currently support MARGIN order. | Margin trading is not supported in isolated-exchange account mode. Switch to cross-exchange mode or use a supported business type.  
`TRADE_APPEND_BALANCE_ERROR` | Insufficient margin. Leverage cannot be adjusted | Available margin is insufficient. Add margin or reduce the position before adjusting leverage.  
`TRADE_BOTH_REDUCE_ERROR` | This order is close order, but your positionQty is 0 | The position quantity is zero. Refresh the position state instead of submitting another closing order.  
`TRADE_CHANGE_MARGIN_MODE_SAME_ERROR` | No need to repeatedly change margin mode | The position already uses the requested margin mode; no update is required.  
`TRADE_EXCEED_MAX_NOTIONAL` | Place order failed. Your open position value exceeds the max notional, you should reduce your open value or lower your leverage | Reduce the order or position size. If it remains above the limit, lower leverage.  
`TRADE_INSUFFICIENT_AVAILABLE_ERROR` | Insufficient available balance | Transfer funds into the account or reduce the order size.  
`TRADE_INSUFFICIENT_AVAILABLE_MARGIN_ERROR` | Insufficient availableMargin | Add available margin or reduce the position and open-order exposure.  
`TRADE_INVALID_ISOLATED_MARGIN_ERROR` | Invalid margin | `margin` must be a valid non-zero number. Use a positive value to add margin and a negative value to remove margin.  
`TRADE_ISOLATED_MARGIN_TOO_SMALL_ERROR` | The absolute margin amount must be at least 0.01 | Set the absolute margin adjustment amount to at least `0.01`.  
`TRADE_ISOLATED_MARGIN_NOT_SUPPORT` | Only isolated positions support margin adjustment | Margin adjustment is supported only for Hyperliquid isolated futures positions.  
`TRADE_MARGIN_MODE_NOT_SUPPORT` | This symbol does not support changing margin mode | Use a symbol that supports margin mode changes.  
`TRADE_POSITION_EXCEED_MAX_NOTIONAL_LIMIT` | Position value exceeds the max risk limit value | Reduce the current position or new order size until the position value is within the risk limit.  
`TRADE_POSITION_NOT_FOUND_ERROR` | The position was not found | Verify `symbol` and `position_side`. No position operation is required when the position size is zero.  
`TRADE_REDUCE_ISOLATED_MARGIN_ERROR` | The remaining isolated margin does not meet the transfer margin requirement | Reduce the amount of margin being removed so the remaining isolated margin still satisfies requirements.  
`TRADE_REDUCE_ONLY_CANNOT_PLACE_IN_THIS_PRICE` | Can not place reduce order | Adjust the reduce-only price or quantity. If necessary, cancel conflicting reduce-only orders and retry.  
`TRADE_REDUCE_ONLY_ORDER_CANCELLED_ERROR` | Due to an order with a better price, %s reduce only order to %s %s %s at %s was cancelled | The system cancelled this reduce-only order because a better-priced reduce-only order exists. Place a new order at the updated price if necessary.  
`TRADE_REDUCE_ONLY_POSITION_QTY_ERROR` | Can not place ReduceOnly order when position quantity is zero | A reduce-only order cannot be submitted when the position quantity is zero.  
`TRADE_REDUCE_ONLY_SIDE_ERROR` | ReduceOnly orders must be in the opposite direction of the position | A reduce-only order must be on the opposite side of the current position.  
`TRADE_REDUCE_TOO_SMALL_ERROR` | The positionQty occupied by this order is too small to be processed | Increase the effective reduction quantity, or cancel other orders that reserve the position quantity.  
  
###  Leverage settings

Leverage settings`label` | `message` | `tips`  
---|---|---  
`TRADE_SET_LEVERAGE_ERROR` | Invalid leverage | `leverage` must be a positive integer supported by the endpoint.  
`TRADE_SET_LEVERAGE_EXCEED_LIMIT_ERROR` | The leverage you have set exceeds the maximum leverage limit | Reduce leverage to the maximum permitted for the symbol or current position.  
`TRADE_LEVERAGE_MARGIN_OPEN_ERROR` | The maximum leverage of the exchange has been adjusted. Please reduce your positionQty or reset your leverage. | The exchange has changed its leverage limit. Reduce the position or reset leverage to the current maximum.  
`TRADE_LEVERAGE_MARGIN_REVERSE_OPEN_ERROR` | The maximum leverage of the exchange has been adjusted. Only can reduce your current positionQty, reverse open is not allowed. | Only position reduction is currently allowed. Reset leverage before attempting to open a position in the opposite direction.  
  
###  Liquidation, delisting, and risk-control errors

Liquidation, delisting, and risk-control errors`label` | `message` | `tips`  
---|---|---  
`RISK_CHECK_MARKET_FORBIDDEN` | Risk management requirements prohibit operations. | Risk controls currently block the operation. Wait for the restriction to be lifted; contact support if it persists.  
`TRADE_DELIST_OPEN_PROHIBITED_ERROR` | Symbol delisted. Opening positions is prohibited. | The symbol is delisted. Only position-reducing or closing orders are allowed.  
  
###  RPI order errors

RPI order errors`label` | `message` | `tips`  
---|---|---  
`TRADE_RPI_EXCHANGE_NOT_SUPPORT` | The exchange or business type does not support RPI orders | Use an exchange and business type that support RPI orders.  
`TRADE_RPI_LIMIT_ORDER_REQUIRED` | RPI orders must be limit orders | RPI orders must use the limit order type.  
`TRADE_RPI_REPLACE_NOT_SUPPORT` | Binance RPI order replace is not supported | Binance RPI orders cannot be amended. Cancel the order and place a new one.  
`TRADE_RPI_SYMBOL_NOT_SUPPORT` | The symbol does not support RPI orders | Use a symbol that supports RPI orders.  
`TRADE_RPI_USER_NOT_SUPPORT` | The user is not allowed to place RPI orders | This account is not enabled for RPI orders. Request access or use a standard limit order.  
  
###  Exchange-specific restrictions

Exchange-specific restrictions`label` | `message` | `tips`  
---|---|---  
`TRADE_OKX_LIMIT_BUY_ORDER_PRICE_ERROR` | Due to OKX's trading rule, the limit price for a buy order cannot be less than 1/3 of the last price or mark price. | Raise the OKX limit buy price so it is not below one-third of the last price or mark price.  
`TRADE_HYPERLIQUID_ORDER_LIMIT_ERROR` | Too many order sent for Hyperliquid. Place taker orders to free up 1 request per USDC traded. | Reduce the Hyperliquid order rate and wait for capacity to recover. Under Hyperliquid's rules, taker volume may also restore request capacity.  
`TRADE_LIGHTER_ORDER_LIMIT_ERROR` | Too many orders sent for Lighter. Place taker orders to free up 1 request per 2 USDC traded. | Reduce the Lighter order rate and wait for capacity to recover; every 2 USDC of taker volume restores capacity for 1 request.  
`TRADE_HYPERLIQUID_ORDER_REPLACE_EXECUTED_ERROR` | Hyperliquid orders with executed quantity do not support replace | A partially filled Hyperliquid order cannot be amended. Cancel the remaining quantity and place a new order.  
`TRADE_HYPERLIQUID_PRICE_SIGNIFICANT_FIGURES_ERROR` | Order price exceeds Hyperliquid exchange limit: at most 5 significant figures | Use no more than five significant figures in the Hyperliquid order price.  
  
#  CrossEx

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

Name | Type | Description  
---|---|---  
_None_ | array | none  
» symbol | string | Unique trading pair identifier in the format ExchangeType_BusinessType_Base_Counter.  
Stocks and ETFs use the market as ExchangeType (US/HK/KR/JP) and STOCK or ETF as the business type, for example US_STOCK_AAPL_USDT, HK_STOCK_00700_USDT, or US_ETF_SPY_USDT.  
» exchange_type | string | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
» business_type | string | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / STOCK: stocks / ETF: exchange-traded funds)  
» state | string | Status (`live` running / `suspend` paused).  
» min_size | string | Minimum order quantity  
» min_notional | string | Minimum Order Value  
» lot_size | string | Quantity Step  
» tick_size | string | Price Step  
» max_num_orders | string | maximumopen orderamount  
» max_market_size | string | Maximum Market Order Quantity  
» max_limit_size | string | Maximum order quantity for limit orders.  
» contract_size | string | Contract multiplier (deprecated; quantity is used uniformly)  
» liquidation_fee | string | Liquidation Fee Rate  
» delist_time | string | Millisecond timestamp; `0` means not delisted.  
» support_rpi | string | Whether RPI order placement is supported (true if supported; false otherwise)  
» support_cross | string | Whether cross-margin order placement is supported (true if supported; false otherwise)  
» tag | string | Tag information. Hyperliquid returns DEX information, stocks and ETFs return the security description, and other businesses return an empty string  
  
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

Name | Type | Description  
---|---|---  
» CrossexOpenCapacity | object | none  
»» symbol | string | Futures trading pair  
»» position_side | string | Position side (LONG for long positions / SHORT for short positions)  
»» available_to_open_notional | number(decimal) | Current maximum remaining opening notional value for the position side; 0 means no position can currently be opened  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
position_side | LONG  
position_side | SHORT  
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

Name | Type | Description  
---|---|---  
» CrossexTransferCoin | object | none  
»» coin | string | Currency  
»» min_trans_amount | number | Minimum transfer amount (estimated fee included)  
»» est_fee | number | Estimated Fee  
»» precision | integer | Precision  
»» is_disabled | integer | If it is disabled. 0 means NOT being disabled  
  
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
    

##  Fund Transfer🔒 Authenticated

POST`/crossex/transfers`

POST `/crossex/transfers`

_Fund Transfer_

Rate limit: 10 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexTransferRequest | Optional | none  
» coin | body | string | Required | Currency  
» amount | body | string | Required | Transfer amount  
» from | body | string | Required | `from` debit account (funds withdrawn from): `CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`  
» to | body | string | Required | `to` receiving account (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`).  
» text | body | string | Optional | User-defined ID  
  
### Responses

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

Name | Type | Description  
---|---|---  
» CrossexTransferRecord | object | none  
»» id | string | Order ID  
»» text | string | Client Custom ID  
»» from_account_type | string | Source account for this operation (`from`) (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`).  
»» to_account_type | string | Destination account for this operation (`to`) (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`).  
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
    

##  Create order🔒 Authenticated

POST`/crossex/orders`

POST `/crossex/orders`

_Create order_

Rate limit: 100 requests per 10 seconds; each user may have up to 1,000 open orders. Stocks and ETFs have an additional per-user limit of one request per second and support only cross-exchange account mode and GTC. Stock and ETF orders must use qty; quote_qty is not supported. Stock and ETF order prices use the listing market currency: USD for US markets, HKD for Hong Kong, KRW for South Korea, and JPY for Japan.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexOrderRequest | Optional | none  
» text | body | string | Optional | Client-defined Order ID, supports letters (a-z), numbers (0-9), symbols (-, _) only  
» symbol | body | string | Required | Unique identifier Exchange_Business_Base_Counter  
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
» side | body | string | Required | BUY, SELL  
» type | body | string | Optional | Order type (default: `LIMIT`; supported types: `LIMIT`, `MARKET`)  
» time_in_force | body | string | Optional | Defaults to GTC. Supported values: `GTC`, `IOC`, `FOK`, `POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
Stocks and ETFs support only `GTC`  
» qty | body | string | Optional | Order quantity (required except for spot and margin market buys; qty is required for stocks and ETFs)  
» price | body | string | Optional | Limit order price (required for limit orders). Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
» quote_qty | body | string | Optional | Order quote quantity, required for spot and margin market buys. Stock and ETF orders do not support quote_qty  
» reduce_only | body | string | Optional | Reduce-only: `true` or `false`  
» position_side | body | string | Optional | Position side: `NONE`, `LONG`, `SHORT`  
Defaults to `NONE` (single position mode) if not specified  
  
####  Detailed descriptions

**» symbol** : Unique identifier Exchange_Business_Base_Counter  
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

**» time_in_force** : Defaults to GTC. Supported values: `GTC`, `IOC`, `FOK`, `POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
Stocks and ETFs support only `GTC`

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
» time_in_force | RPI  
» reduce_only | true  
» reduce_only | false  
» position_side | LONG  
» position_side | SHORT  
» position_side | NONE  
  
### Responses

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
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Batch order cancellation request results | [CrossexBatchCancelOrderResponse]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Batch order cancellation request results]  
» CrossexBatchCancelOrderResponse | CrossexBatchCancelOrderResponse | Batch order cancellation request results  
»» order_id | string | Order ID  
»» text | string | Custom ID specified by the user when creating the order  
»» accepted | string | Whether the request was accepted, as the string true or false  
»» label | string | Error label when the request is not accepted; empty on success  
»» message | string | Error message when the request is not accepted; empty on success  
  
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
» qty | body | string | Optional | modify amount  
» price | body | string | Optional | modify price  
  
### Responses

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

_CrossexOrder_

Name | Type | Description  
---|---|---  
» user_id | string | User ID  
» order_id | string | Order ID  
» text | string | Client-defined order ID.  
» state | string | Order status:  
`NEW`: validated locally, pending submission to the exchange  
`OPEN`: resting on the exchange order book  
`PARTIALLY_FILLED`: partially filled  
`FILLED`: fully filled  
`FAIL`: CrossEx validation failed; see `reason`  
`REJECT`: rejected by the exchange; see `reason`  
`CANCELLED`: cancelled  
» symbol | string | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
» side | string | Side (`BUY` buy / `SELL` sell).  
» type | string | Order type (`LIMIT` limit / `MARKET` market).  
» attribute | string | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
» exchange_type | string | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
» business_type | string | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)  
» qty | string | Order quantity in the base currency.  
» quote_qty | string | Order quantity in the quote currency.  
» price | string | Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
» time_in_force | string | Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)  
» executed_qty | string | Filled base amount.  
» executed_amount | string | Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
» executed_avg_price | string | Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
» fee_coin | string | Fee currency  
» fee | string | Fee amount.  
» reduce_only | string | Reduce-only order (`"true"` or `"false"`).  
» leverage | string | Order leverage multiplier.  
» reason | string | Failure reason description.  
» last_executed_qty | string | Base quantity of the latest fill.  
» last_executed_price | string | Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
» last_executed_amount | string | Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
» position_side | string | Position side (`NONE` one-way position / `LONG` long / `SHORT` short)  
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
    

##  Flash Swap Inquiry🔒 Authenticated

POST`/crossex/convert/quote`

POST `/crossex/convert/quote`

_Flash Swap Inquiry_

Rate limit: 100 requests per day For HYPERLIQUID, swaps between `HYPERLIQUID_USDC` and `CROSSEX_USDT` are supported. Flash Swap in isolated exchange mode is not currently supported for HYPERLIQUID. For LIGHTER, swaps between `LIGHTER_USDC` and `CROSSEX_USDT` are supported. Flash Swap in isolated exchange mode is not currently supported for LIGHTER. For KRAKEN, only conversion from `KRAKEN_USD` to `CROSSEX_USDT` is supported. Flash Swap in isolated exchange mode is not currently supported for KRAKEN.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexConvertQuoteRequest | Optional | none  
» exchange_type | body | string | Required | Exchange type  
Currently supports only BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, and LIGHTER  
» from_coin | body | string | Required | Asset Sold  
» to_coin | body | string | Required | Asset to receive  
OKX and GATE only support conversion to BTC, ETH, or USDT  
BYBIT and BINANCE only support conversion to USDT  
HYPERLIQUID only supports conversion to USDT or USDC  
KRAKEN only supports conversion to USDT  
LIGHTER only supports swaps between USDT and USDC  
» from_amount | body | string | Required | Amount to sell  
  
####  Detailed descriptions

**» exchange_type** : Exchange type  
Currently supports only BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, and LIGHTER

**» to_coin** : Asset to receive  
OKX and GATE only support conversion to BTC, ETH, or USDT  
BYBIT and BINANCE only support conversion to USDT  
HYPERLIQUID only supports conversion to USDT or USDC  
KRAKEN only supports conversion to USDT  
LIGHTER only supports swaps between USDT and USDC

### Responses

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
» price | string | Quoted price  
  
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
» quote_id | body | string | Required | Inquiry ID  
  
### Responses

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
    

##  Modify Account Contract Position Mode and Account Mode🔒 Authenticated

PUT`/crossex/accounts`

PUT `/crossex/accounts`

_Modify Account Contract Position Mode and Account Mode_

Rate Limit: 100 requests per 60 seconds. position_mode+exchange_type modifies contract position mode (exchange_type is required when the user's account mode is split exchange); account_mode modifies the user's account mode.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexAccountUpdateRequest | Optional | none  
» position_mode | body | string | Optional | Futures position mode (SINGLE/DUAL)  
» account_mode | body | string | Optional | Account mode (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE)  
» exchange_type | body | string | Optional | Exchange (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to adjust futures position mode.  
  
### Responses

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
» exchange_type | string | Exchange targeted by the requested change (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to change futures position mode.  
  
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
»»» equity | string | Net margin equity for the currency  
»»» futures_initial_margin | string | Currency-specific futures initial margin. This value is populated for futures settlement currencies (USDT/USDC/USD)  
»»» futures_maintenance_margin | string | Currency-specific futures maintenance margin. This value is populated for futures settlement currencies (USDT/USDC/USD)  
»»» borrowing_initial_margin | string | Currency-specific margin trading initial margin. This value is populated for margin or futures settlement currencies (USDT/USDC/USD)  
»»» borrowing_maintenance_margin | string | Currency-specific margin trading maintenance margin. This value is populated for margin or futures settlement currencies (USDT/USDC/USD)  
»»» available_balance | string | Available Balance  
»»» liability | string | Liability for the currency. This value is populated only for USDT, USDC, or USD  
  
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
    

##  Modify Contract Trading Pair Leverage Multiplier🔒 Authenticated

POST`/crossex/positions/leverage`

POST `/crossex/positions/leverage`

_Modify Contract Trading Pair Leverage Multiplier_

Rate Limit: 100 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexLeverageRequest | Optional | none  
» symbol | body | string | Required | Currency pair  
» leverage | body | string | Required | Leverage  
  
### Responses

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
    

##  Modify Leveraged Trading Pair Leverage Multiplier🔒 Authenticated

POST`/crossex/margin_positions/leverage`

POST `/crossex/margin_positions/leverage`

_Modify Leveraged Trading Pair Leverage Multiplier_

Rate Limit: 100 requests per 10 seconds

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexLeverageRequest | Optional | none  
» symbol | body | string | Required | Currency pair  
» leverage | body | string | Required | Leverage  
  
### Responses

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
» symbol | body | string | Required | Trading Pair  
1\. Supports leveraged trading pairs, e.g., BINANCE_MARGIN_SOL_USDT  
2\. Supports contract trading pairs, e.g., OKX_FUTURE_ETH_USDT  
» position_side | body | string | Optional | Position Direction  
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
    

##  Update futures position margin mode🔒 Authenticated

POST`/crossex/positions/margin_mode`

POST `/crossex/positions/margin_mode`

_Update futures position margin mode_

Rate limit: 100 requests per 10 seconds. Only Hyperliquid futures trading pairs are supported. The margin mode cannot be changed while open orders or positions exist

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexMarginModeRequest | Optional | none  
» symbol | body | string | Required | Hyperliquid futures trading pair  
» margin_mode | body | string | Required | Margin mode (CROSS/ISOLATED)  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» margin_mode | CROSS  
» margin_mode | ISOLATED  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexMarginModeResponse  
  
### Response Schema

Status Code **202**

_CrossexMarginModeResponse_

Name | Type | Description  
---|---|---  
» symbol | string | Futures trading pair  
» margin_mode | string | Margin mode (CROSS/ISOLATED)  
  
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

_CrossexMarginModeResponse_

Name | Type | Description  
---|---|---  
» symbol | string | Futures trading pair  
» margin_mode | string | Margin mode (CROSS/ISOLATED)  
  
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
    

##  Increase or decrease isolated margin🔒 Authenticated

POST`/crossex/positions/margin`

POST `/crossex/positions/margin`

_Increase or decrease isolated margin_

Rate limit: 100 requests per 10 seconds. Only Hyperliquid isolated futures positions are supported. Positive values increase margin, while negative values decrease margin

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CrossexIsolatedMarginRequest | Optional | none  
» symbol | body | string | Required | Hyperliquid futures trading pair  
» margin | body | string | Required | Margin adjustment amount. Positive values increase margin, while negative values decrease margin. Values with more than two decimal places are truncated to two decimal places  
» position_side | body | string | Optional | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» position_side | NONE  
» position_side | LONG  
» position_side | SHORT  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexIsolatedMarginResponse  
  
### Response Schema

Status Code **202**

_CrossexIsolatedMarginResponse_

Name | Type | Description  
---|---|---  
» symbol | string | Futures trading pair  
» margin | string | Amount of isolated margin increased or decreased in this request  
» position_side | string | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted  
  
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

_CrossexFee_

Name | Type | Description  
---|---|---  
CrossexFee | array | none  
» exchange_type | string | Exchange  
» spot_maker_fee | string | spotMakerfee rate  
» spot_taker_fee | string | spotTakerfee rate  
» spot_rpi_maker_fee | string | Spot RPI order maker fee rate  
» future_maker_fee | string | contractMakerfee rate  
» future_taker_fee | string | contractTakerfee rate  
» future_rpi_maker_fee | string | Futures RPI order maker fee rate  
» special_fee_list | array | none  
»» CrossexSpecialFee | object | none  
»»» symbol | string | Currency pair  
»»» taker_fee_rate | string | Taker fee rate  
»»» maker_fee_rate | string | Maker fee rate  
»»» rpi_fee_rate | string | RPI order maker fee rate  
  
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

Name | Type | Description  
---|---|---  
» CrossexPosition | object | none  
»» user_id | string | User ID  
»» position_id | string | Position ID  
»» symbol | string | Currency pair  
»» position_side | string | Position Direction  
»» initial_margin | string | Initial Margin  
»» isolated_margin | string | Isolated margin. It is 0 in cross margin mode and applies only to isolated margin positions  
»» margin_mode | string | Margin mode (CROSS/ISOLATED)  
»» maintenance_margin | string | Maintenance margin  
»» position_qty | string | Position Quantity  
»» position_value | string | Position Value  
»» upnl | string | Unrealized P&L  
»» upnl_rate | string | Unrealized P&L Ratio  
»» entry_price | string | Position Average Entry Price  
»» liq_price | string | Liquidation price. It is 0 in cross margin mode and applies only to isolated margin positions; 0 in isolated margin mode means the position will not be liquidated  
»» mark_price | string | Mark price  
»» leverage | string | Position Leverage  
»» max_leverage | string | Maximum leverage  
»» risk_limit | string | Position risk limit  
»» fee | string | Position Fee  
»» funding_fee | string | Accumulated position funding fee. A positive value indicates a gain, while a negative value indicates a loss.  
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

Name | Type | Description  
---|---|---  
» CrossexSecurityPosition | object | none  
»» user_id | string | User ID  
»» symbol | string | Stock or ETF trading pair  
»» price | string | Latest price in the listing market currency  
»» entry_price | string | Position cost price in the listing market currency  
»» diluted_cost_price | string | Diluted cost price in the listing market currency  
»» upnl | string | Unrealized profit and loss in the listing market currency  
»» position_qty | string | Position size  
»» position_value | string | Position value in the listing market currency  
  
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

_CrossexAdlRank_

Name | Type | Description  
---|---|---  
» user_id | string | User ID  
» symbol | string | Currency pair  
» crossex_adl_rank | string | CrossEx ADL priority, with values from 1 to 5  
Priority from highest to lowest: 5, 4, 3, 2, 1  
» exchange_adl_rank | string | Raw exchange ADL rank. Priority order from highest to lowest by exchange:  
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

Name | Type | Description  
---|---|---  
_None_ | array | none  
» CrossexOrder | CrossexOrder | none  
»» user_id | string | User ID  
»» order_id | string | Order ID  
»» text | string | Client-defined order ID.  
»» state | string | Order status:  
`NEW`: validated locally, pending submission to the exchange  
`OPEN`: resting on the exchange order book  
`PARTIALLY_FILLED`: partially filled  
`FILLED`: fully filled  
`FAIL`: CrossEx validation failed; see `reason`  
`REJECT`: rejected by the exchange; see `reason`  
`CANCELLED`: cancelled  
»» symbol | string | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
»» side | string | Side (`BUY` buy / `SELL` sell).  
»» type | string | Order type (`LIMIT` limit / `MARKET` market).  
»» attribute | string | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
»» exchange_type | string | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
»» business_type | string | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)  
»» qty | string | Order quantity in the base currency.  
»» quote_qty | string | Order quantity in the quote currency.  
»» price | string | Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» time_in_force | string | Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)  
»» executed_qty | string | Filled base amount.  
»» executed_amount | string | Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» executed_avg_price | string | Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» fee_coin | string | Fee currency  
»» fee | string | Fee amount.  
»» reduce_only | string | Reduce-only order (`"true"` or `"false"`).  
»» leverage | string | Order leverage multiplier.  
»» reason | string | Failure reason description.  
»» last_executed_qty | string | Base quantity of the latest fill.  
»» last_executed_price | string | Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» last_executed_amount | string | Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» position_side | string | Position side (`NONE` one-way position / `LONG` long / `SHORT` short)  
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

Name | Type | Description  
---|---|---  
_None_ | array | none  
» CrossexOrder | CrossexOrder | none  
»» user_id | string | User ID  
»» order_id | string | Order ID  
»» text | string | Client-defined order ID.  
»» state | string | Order status:  
`NEW`: validated locally, pending submission to the exchange  
`OPEN`: resting on the exchange order book  
`PARTIALLY_FILLED`: partially filled  
`FILLED`: fully filled  
`FAIL`: CrossEx validation failed; see `reason`  
`REJECT`: rejected by the exchange; see `reason`  
`CANCELLED`: cancelled  
»» symbol | string | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
»» side | string | Side (`BUY` buy / `SELL` sell).  
»» type | string | Order type (`LIMIT` limit / `MARKET` market).  
»» attribute | string | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
»» exchange_type | string | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
»» business_type | string | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)  
»» qty | string | Order quantity in the base currency.  
»» quote_qty | string | Order quantity in the quote currency.  
»» price | string | Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» time_in_force | string | Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)  
»» executed_qty | string | Filled base amount.  
»» executed_amount | string | Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» executed_avg_price | string | Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» fee_coin | string | Fee currency  
»» fee | string | Fee amount.  
»» reduce_only | string | Reduce-only order (`"true"` or `"false"`).  
»» leverage | string | Order leverage multiplier.  
»» reason | string | Failure reason description.  
»» last_executed_qty | string | Base quantity of the latest fill.  
»» last_executed_price | string | Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» last_executed_amount | string | Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
»» position_side | string | Position side (`NONE` one-way position / `LONG` long / `SHORT` short)  
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
»» margin_mode | string | Margin mode (CROSS/ISOLATED)  
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
»» interest | string | Accumulated position interest  
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

Name | Type | Description  
---|---|---  
» CrossexMarginInterestRecord | object | none  
»» user_id | string | User ID  
»» symbol | string | Trading Pair  
»» interest_id | string | Interest Deduction ID  
»» liability_id | string | Debt Source ID, can be Order ID or Position ID  
»» liability | string | Debt Quantity  
»» liability_coin | string | Debt Currency  
»» interest | string | Interest  
»» interest_rate | string | interest rate  
»» interest_type | string | Interest deduction type  
`PERIODIC_POSITION`: hourly interest charged on positions  
`PERIODIC_OPEN_ORDER`: hourly interest charged on open orders  
`IMMEDIATE_OPEN_ORDER`: interest charged when an order is placed  
`PERIODIC_ISOLATED`: hourly interest charged on liabilities  
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
»» price | string | Fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
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

Name | Type | Description  
---|---|---  
» CrossexAccountBookRecord | object | none  
»» id | string | Account Change Record ID  
»» user_id | string | User ID  
»» business_id | string | Business ID. Its meaning varies by `statement_type`.  
TRANSACTION: order ID  
TRADING_FEE: order ID  
LIQUIDATION_FEE: liquidation order ID  
FUNDING_FEE: position ID and funding fee settlement time  
For other types, it is a system-generated processing ID with no business meaning  
»» statement_type | string | Account book transaction type  
`TRANSACTION`: Trade  
`TRADING_FEE`: Trading fee  
`FUNDING_FEE`: Futures funding fee  
`LIQUIDATION_FEE`: Liquidation fee  
`TRANSFER_IN`: Incoming transfer  
`TRANSFER_OUT`: Outgoing transfer  
`BANKRUPT_COMPENSATION`: Bankruptcy compensation  
`AUTO_REPAY`: Automatic margin liability repayment  
`INTEREST_ISOLATED`: Interest transaction  
`ACCOUNT_MODE_CHANGE`: Funds movement on account mode change  
`KRAKEN_CONVERSION`: Conversion of other collateral currencies to cover a negative KRAKEN_USD balance  
`SECURITY_DIVIDEND`: Stock or ETF dividend payout  
`SECURITY_CORPORATE_ACTION`: Stock or ETF split or reverse split  
`OTHER`: Other  
»» exchange_type | string | Exchange  
»» coin | string | Currency  
»» symbol | string | Trading Pair  
»» change | string | Change amount (positive values indicate an increase; negative values indicate a decrease)  
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

Name | Type | Description  
---|---|---  
» symbol | string | Trading Pair  
» last_price | string | Last price  
» open_24h | string | 24-hour opening price  
» low_24h | string | 24h Low  
» high_24h | string | 24h High  
» volume_24h_base | string | 24-hour trading volume in base currency  
» volume_24h_quote | string | 24-hour trading volume in quote currency  
» mark_price | string | Mark price  
» index_price | string | Index price  
» open_interest | string | Open interest  
» open_interest_quote | string | Open interest (in quote currency)  
» timestamp | string | Update timestamp  
  
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

Name | Type | Description  
---|---|---  
» symbol | string | Currency  
» funding_rate | string | Funding rate  
» funding_interval | string | Funding interval (in seconds)  
» funding_time | string | Next funding time (Unix timestamp in milliseconds)  
  
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

##  Symbol

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Unique trading pair identifier in the format ExchangeType_BusinessType_Base_Counter.  
Stocks and ETFs use the market as ExchangeType (US/HK/KR/JP) and STOCK or ETF as the business type, for example US_STOCK_AAPL_USDT, HK_STOCK_00700_USDT, or US_ETF_SPY_USDT.  
exchange_type | string | Required | none | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
business_type | string | Required | none | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / STOCK: stocks / ETF: exchange-traded funds)  
state | string | Required | none | Status (`live` running / `suspend` paused).  
min_size | string | Required | none | Minimum order quantity  
min_notional | string | Required | none | Minimum Order Value  
lot_size | string | Required | none | Quantity Step  
tick_size | string | Required | none | Price Step  
max_num_orders | string | Required | none | maximumopen orderamount  
max_market_size | string | Required | none | Maximum Market Order Quantity  
max_limit_size | string | Required | none | Maximum order quantity for limit orders.  
contract_size | string | Required | none | Contract multiplier (deprecated; quantity is used uniformly)  
liquidation_fee | string | Required | none | Liquidation Fee Rate  
delist_time | string | Required | none | Millisecond timestamp; `0` means not delisted.  
support_rpi | string | Optional | none | Whether RPI order placement is supported (true if supported; false otherwise)  
support_cross | string | Optional | none | Whether cross-margin order placement is supported (true if supported; false otherwise)  
tag | string | Required | none | Tag information. Hyperliquid returns DEX information, stocks and ETFs return the security description, and other businesses return an empty string  
      
    
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
    
    

##  CrossexOrder

_CrossexOrder_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_id | string | Required | none | User ID  
order_id | string | Required | none | Order ID  
text | string | Required | none | Client-defined order ID.  
state | string | Required | none | Order status:  
`NEW`: validated locally, pending submission to the exchange  
`OPEN`: resting on the exchange order book  
`PARTIALLY_FILLED`: partially filled  
`FILLED`: fully filled  
`FAIL`: CrossEx validation failed; see `reason`  
`REJECT`: rejected by the exchange; see `reason`  
`CANCELLED`: cancelled  
symbol | string | Required | none | Unique trading pair identifiers, e.g.  
`BINANCE_SPOT_BTC_USDT`, `BINANCE_FUTURE_BTC_USDT`.  
side | string | Required | none | Side (`BUY` buy / `SELL` sell).  
type | string | Required | none | Order type (`LIMIT` limit / `MARKET` market).  
attribute | string | Required | none | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement).  
exchange_type | string | Required | none | Exchange type (BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER). Stocks and ETFs return the listing market (US / HK / KR / JP)  
business_type | string | Required | none | Business type (SPOT: spot / FUTURE: futures / MARGIN: margin / CONVERT: flash swap / STOCK: stocks / ETF: exchange-traded funds)  
qty | string | Required | none | Order quantity in the base currency.  
quote_qty | string | Required | none | Order quantity in the quote currency.  
price | string | Required | none | Order price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
time_in_force | string | Required | none | Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI)  
executed_qty | string | Required | none | Filled base amount.  
executed_amount | string | Required | none | Filled amount in the quote currency. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
executed_avg_price | string | Required | none | Average fill price. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
fee_coin | string | Required | none | Fee currency  
fee | string | Required | none | Fee amount.  
reduce_only | string | Required | none | Reduce-only order (`"true"` or `"false"`).  
leverage | string | Required | none | Order leverage multiplier.  
reason | string | Required | none | Failure reason description.  
last_executed_qty | string | Required | none | Base quantity of the latest fill.  
last_executed_price | string | Required | none | Price of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
last_executed_amount | string | Required | none | Amount of the latest fill. Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
position_side | string | Required | none | Position side (`NONE` one-way position / `LONG` long / `SHORT` short)  
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
    
    

##  CrossexBatchCancelOrderRequest

_CrossexBatchCancelOrderRequest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Optional | none | Order ID; either this field or text is required  
text | string | Optional | none | Custom ID specified by the user when creating the order; either this field or order_id is required  
  
_anyOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
  
_or_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
      
    
    {}
    
    

##  CrossexBatchCancelOrderResponse

_CrossexBatchCancelOrderResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Required | none | Order ID  
text | string | Required | none | Custom ID specified by the user when creating the order  
accepted | string | Required | none | Whether the request was accepted, as the string true or false  
label | string | Required | none | Error label when the request is not accepted; empty on success  
message | string | Required | none | Error message when the request is not accepted; empty on success  
      
    
    {
      "order_id": "string",
      "text": "string",
      "accepted": "string",
      "label": "string",
      "message": "string"
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
    
    

##  CrossexMarginModeResponse

_CrossexMarginModeResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Futures trading pair  
margin_mode | string | Required | none | Margin mode (CROSS/ISOLATED)  
      
    
    {
      "symbol": "string",
      "margin_mode": "string"
    }
    
    

##  CrossexIsolatedMarginResponse

_CrossexIsolatedMarginResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Futures trading pair  
margin | string | Required | none | Amount of isolated margin increased or decreased in this request  
position_side | string | Optional | none | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted  
      
    
    {
      "symbol": "string",
      "margin": "string",
      "position_side": "string"
    }
    
    

##  CrossexTransferRequest

_Fund Transfer Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
coin | string | Required | none | Currency  
amount | string | Required | none | Transfer amount  
from | string | Required | none | `from` debit account (funds withdrawn from): `CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`  
to | string | Required | none | `to` receiving account (`CROSSEX_BINANCE`, `CROSSEX_OKX`, `CROSSEX_GATE`, `CROSSEX_BYBIT`, `CROSSEX_KRAKEN`, `CROSSEX_HYPERLIQUID`, `CROSSEX_DERIBIT`, `CROSSEX_LIGHTER`, `CROSSEX`, `SPOT`).  
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
symbol | string | Required | none | Unique identifier Exchange_Business_Base_Counter  
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
side | string | Required | none | BUY, SELL  
type | string | Optional | none | Order type (default: `LIMIT`; supported types: `LIMIT`, `MARKET`)  
time_in_force | string | Optional | none | Defaults to GTC. Supported values: `GTC`, `IOC`, `FOK`, `POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
Stocks and ETFs support only `GTC`  
qty | string | Optional | none | Order quantity (required except for spot and margin market buys; qty is required for stocks and ETFs)  
price | string | Optional | none | Limit order price (required for limit orders). Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY)  
quote_qty | string | Optional | none | Order quote quantity, required for spot and margin market buys. Stock and ETF orders do not support quote_qty  
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
time_in_force | RPI  
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
exchange_type | string | Required | none | Exchange type  
Currently supports only BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, and LIGHTER  
from_coin | string | Required | none | Asset Sold  
to_coin | string | Required | none | Asset to receive  
OKX and GATE only support conversion to BTC, ETH, or USDT  
BYBIT and BINANCE only support conversion to USDT  
HYPERLIQUID only supports conversion to USDT or USDC  
KRAKEN only supports conversion to USDT  
LIGHTER only supports swaps between USDT and USDC  
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
exchange_type | string | Optional | none | Exchange (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to adjust futures position mode.  
      
    
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
leverage | string | Required | none | Leverage  
      
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    
    

##  CrossexMarginModeRequest

_Request body for updating the futures position margin mode_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Hyperliquid futures trading pair  
margin_mode | string | Required | none | Margin mode (CROSS/ISOLATED)  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
margin_mode | CROSS  
margin_mode | ISOLATED  
      
    
    {
      "symbol": "string",
      "margin_mode": "CROSS"
    }
    
    

##  CrossexIsolatedMarginRequest

_Request body for increasing or decreasing isolated margin_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
symbol | string | Required | none | Hyperliquid futures trading pair  
margin | string | Required | none | Margin adjustment amount. Positive values increase margin, while negative values decrease margin. Values with more than two decimal places are truncated to two decimal places  
position_side | string | Optional | none | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
position_side | NONE  
position_side | LONG  
position_side | SHORT  
      
    
    {
      "symbol": "string",
      "margin": "string",
      "position_side": "NONE"
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
price | string | Required | none | Quoted price  
      
    
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
» CrossexAccountAsset | object | Optional | none | none  
»» user_id | string | Optional | none | User ID  
»» coin | string | Optional | none | Currency  
»» exchange_type | string | Optional | none | Exchange  
»» balance | string | Optional | none | Balance  
»» upnl | string | Optional | none | Unrealized P&L  
»» equity | string | Optional | none | Net margin equity for the currency  
»» futures_initial_margin | string | Optional | none | Currency-specific futures initial margin. This value is populated for futures settlement currencies (USDT/USDC/USD)  
»» futures_maintenance_margin | string | Optional | none | Currency-specific futures maintenance margin. This value is populated for futures settlement currencies (USDT/USDC/USD)  
»» borrowing_initial_margin | string | Required | none | Currency-specific margin trading initial margin. This value is populated for margin or futures settlement currencies (USDT/USDC/USD)  
»» borrowing_maintenance_margin | string | Required | none | Currency-specific margin trading maintenance margin. This value is populated for margin or futures settlement currencies (USDT/USDC/USD)  
»» available_balance | string | Optional | none | Available Balance  
»» liability | string | Optional | none | Liability for the currency. This value is populated only for USDT, USDC, or USD  
      
    
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
exchange_type | string | Optional | none | Exchange targeted by the requested change (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT` / `LIGHTER` / `CROSSEX`). When account mode is `ISOLATED_EXCHANGE`, the exchange must be specified to change futures position mode.  
      
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    
    

Last Updated: 10/13/2026, 1:22:04 AM