---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/bot
api_type: REST
updated_at: 2026-05-27 20:14:47.724156
---

# Bot

* Python 
  * Shell 


Bot AIHub policy recommendation, creation, query and termination interface

##  Get AIHub strategy recommendations🔒 Authenticated

GET`/bot/strategy/recommend`

GET `/bot/strategy/recommend`

Get `AIHub strategy recommendations`

The only formal interface for the discover domain. Support scenarios:

  * `top1`
  * `bundle`
  * `filter`
  * `refresh` Constraints:
  * The active recommendation pool only contains `spot_grid`, `futures_grid`, `spot_martingale`
  * Can return but do not actively recommend `infinite_grid`, `margin_grid`
  * `contract_martingale`, `smart-position`, `spot-future-arbitrage` must not be returned
  * When `scene=filter` is used, only filtering by `market`, `backtest_apr_gte`, `max_drawdown_lte` is allowed
  * `scene=refresh` inherits the refresh context through `refresh_recommendation_id`; the official minimum format only requires `strategy_type|market`
  * If the upstream directly transmits the previous recommendation `recommendation_id`, the third paragraph `backtest_id` will currently be ignored.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
market | query | string | Optional | Trading pair, such as `BTC_USDT`  
strategy_type | query | string | Optional | Recommended target policy type; `contract_martingale` not allowed  
direction | query | string | Optional | Market direction  
invest_amount | query | string | Optional | Investment amount, string transparent transmission  
scene | query | string | Optional | Recommended scenario; when empty, bot-service can automatically infer according to the implementation logic.  
refresh_recommendation_id | query | string | Optional | It is recommended to refresh the context. Used when `scene=refresh` is used; when `scene` is empty but the field exists, bot-service will also automatically determine as `refresh`.  
The official minimum format is `strategy_type|market`; if the `recommendation_id` of the previous recommendation is directly passed through, the third paragraph `backtest_id` will be ignored.  
limit | query | integer(int32) | Optional | Return quantity; when `scene=filter` is used, the actual results are up to 10  
max_drawdown_lte | query | string | Optional | Maximum drawdown limit  
backtest_apr_gte | query | string | Optional | Backtest annualized lower limit  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
  
####  Detailed descriptions

**refresh_recommendation_id** : It is recommended to refresh the context. Used when `scene=refresh` is used; when `scene` is empty but the field exists, bot-service will also automatically determine as `refresh`.  
The official minimum format is `strategy_type|market`; if the `recommendation_id` of the previous recommendation is directly passed through, the third paragraph `backtest_id` will be ignored.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
direction | buy  
direction | sell  
direction | neutral  
scene | top1  
scene | bundle  
scene | filter  
scene | refresh  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubDiscoverSuccessResponse  
  
### Response Schema

Status Code **200**

Get `the response body when the strategy recommendation is successful.`

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubDiscoverData | Strategy recommendation result data.  
»» scene | DiscoverScene | Enumeration of scenarios supported by the policy recommendation interface.  
»» recommendations | array | [A single piece of strategy recommendation information.]  
»»» _None_ | AIHubRecommendation | A single piece of strategy recommendation information.  
»»»» recommendation_id | string | none  
»»»» market | string | none  
»»»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»»»» strategy_name | string | none  
»»»» backtest_apr | string | none  
»»»» max_drawdown | string | none  
»»»» summary | string | none  
»»»» strategy_params_preview | string | Recommended-parameter preview as JSON text (string-encoded so clients deserialize it consistently). The value is a serialized JSON object whose structure varies by strategy type; callers or upper-layer models must parse it.  
»»» unsupported_filters | array | Filter conditions not supported in this issue  
»» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
scene | top1  
scene | bundle  
scene | filter  
scene | refresh  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/strategy/recommend'
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
    url="/bot/strategy/recommend"
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
      "code": 200,
      "message": "success",
      "data": {
        "scene": "top1",
        "recommendations": [
          {}
        ],
        "unsupported_filters": [
          "string"
        ]
      },
      "trace_id": "string"
    }
    

##  Create spot grid🔒 Authenticated

POST`/bot/spot-grid/create`

POST `/bot/spot-grid/create`

_Create spot grid_

Create a spot grid strategy based on the incoming parameters.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | SpotGridCreateRequest | Required | none  
↳ strategy_type | body | string | Required | none  
↳ market | body | string | Required | none  
↳ create_params | body | SpotGridCreateParams | Required | Creation parameters for the spot grid strategy.  
↳ money | body | string | Required | Amount of investment  
↳ low_price | body | string | Required | Range lower limit  
↳ high_price | body | string | Required | Range upper limit  
↳ grid_num | body | integer(int32) | Required | Number of grids  
↳ price_type | body | integer(int32) | Required | none  
↳ trigger_price | body | string | Optional | none  
↳ stop_profit | body | string | Optional | none  
↳ stop_loss | body | string | Optional | none  
↳ profit_sharing_ratio | body | string | Optional | none  
↳ is_use_base | body | boolean | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | spot_grid  
»» price_type | 0  
»» price_type | 1  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

_The response body when the creation strategy is successful._

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubCreateData | Policy information returned after the policy is successfully created.  
»» strategy_id | string | none  
»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»» market | string | none  
»» status | string | The initial state after successful creation, usually `running`  
»» jump_url | string | none  
» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/spot-grid/create'
    query_param = ''
    body='{"strategy_type":"spot_grid","market":"string","create_params":{"money":"string","low_price":"string","high_price":"string","grid_num":1,"price_type":0,"trigger_price":"string","stop_profit":"string","stop_loss":"string","profit_sharing_ratio":"string","is_use_base":true}}'
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
    url="/bot/spot-grid/create"
    query_param=""
    body_param='{"strategy_type":"spot_grid","market":"string","create_params":{"money":"string","low_price":"string","high_price":"string","grid_num":1,"price_type":0,"trigger_price":"string","stop_profit":"string","stop_loss":"string","profit_sharing_ratio":"string","is_use_base":true}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "strategy_type": "spot_grid",
      "market": "string",
      "create_params": {
        "money": "string",
        "low_price": "string",
        "high_price": "string",
        "grid_num": 1,
        "price_type": 0,
        "trigger_price": "string",
        "stop_profit": "string",
        "stop_loss": "string",
        "profit_sharing_ratio": "string",
        "is_use_base": true
      }
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "jump_url": "string"
      },
      "trace_id": "string"
    }
    

##  Create a lever grid🔒 Authenticated

POST`/bot/margin-grid/create`

POST `/bot/margin-grid/create`

_Create a lever grid_

Create a leverage grid strategy based on the passed parameters.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | MarginGridCreateRequest | Required | none  
↳ strategy_type | body | string | Required | none  
↳ market | body | string | Required | none  
↳ create_params | body | MarginGridCreateParams | Required | Creation parameters for the Leverage Grid strategy.  
↳ money | body | string | Required | none  
↳ low_price | body | string | Required | none  
↳ high_price | body | string | Required | none  
↳ grid_num | body | integer(int32) | Required | none  
↳ price_type | body | integer(int32) | Required | none  
↳ leverage | body | string | Required | none  
↳ direction | body | FuturesDirection | Optional | Direction enumeration supported by contract-based strategies.  
↳ trigger_price | body | string | Optional | none  
↳ stop_profit | body | string | Optional | none  
↳ stop_loss | body | string | Optional | none  
↳ profit_sharing_ratio | body | string | Optional | none  
↳ is_use_base | body | boolean | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | margin_grid  
»» price_type | 0  
»» price_type | 1  
»» direction | long  
»» direction | short  
»» direction | neutral  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

_The response body when the creation strategy is successful._

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubCreateData | Policy information returned after the policy is successfully created.  
»» strategy_id | string | none  
»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»» market | string | none  
»» status | string | The initial state after successful creation, usually `running`  
»» jump_url | string | none  
» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/margin-grid/create'
    query_param = ''
    body='{"strategy_type":"margin_grid","market":"string","create_params":{"money":"string","low_price":"string","high_price":"string","grid_num":1,"price_type":0,"leverage":"string","direction":"long","trigger_price":"string","stop_profit":"string","stop_loss":"string","profit_sharing_ratio":"string","is_use_base":true}}'
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
    url="/bot/margin-grid/create"
    query_param=""
    body_param='{"strategy_type":"margin_grid","market":"string","create_params":{"money":"string","low_price":"string","high_price":"string","grid_num":1,"price_type":0,"leverage":"string","direction":"long","trigger_price":"string","stop_profit":"string","stop_loss":"string","profit_sharing_ratio":"string","is_use_base":true}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "strategy_type": "margin_grid",
      "market": "string",
      "create_params": {
        "money": "string",
        "low_price": "string",
        "high_price": "string",
        "grid_num": 1,
        "price_type": 0,
        "leverage": "string",
        "direction": "long",
        "trigger_price": "string",
        "stop_profit": "string",
        "stop_loss": "string",
        "profit_sharing_ratio": "string",
        "is_use_base": true
      }
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "jump_url": "string"
      },
      "trace_id": "string"
    }
    

##  Create infinite grid🔒 Authenticated

POST`/bot/infinite-grid/create`

POST `/bot/infinite-grid/create`

_Create infinite grid_

Create an infinite grid strategy based on passed parameters.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | InfiniteGridCreateRequest | Required | none  
↳ strategy_type | body | string | Required | none  
↳ market | body | string | Required | none  
↳ create_params | body | InfiniteGridCreateParams | Required | Creation parameters for infinite grid strategies.  
↳ money | body | string | Required | none  
↳ price_floor | body | string | Required | price floor  
↳ profit_per_grid | body | string | Required | Profit per square  
↳ grid_num | body | integer(int32) | Optional | Optional; may be omitted like in the app.  
↳ price_type | body | integer(int32) | Optional | Optional. `0` arithmetic grid; `1` geometric; omit for server defaults.  
↳ trigger_price | body | string | Optional | none  
↳ stop_profit | body | string | Optional | none  
↳ stop_loss | body | string | Optional | none  
↳ profit_sharing_ratio | body | string | Optional | none  
↳ is_use_base | body | boolean | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | infinite_grid  
»» price_type | 0  
»» price_type | 1  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

_The response body when the creation strategy is successful._

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubCreateData | Policy information returned after the policy is successfully created.  
»» strategy_id | string | none  
»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»» market | string | none  
»» status | string | The initial state after successful creation, usually `running`  
»» jump_url | string | none  
» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/infinite-grid/create'
    query_param = ''
    body='{"strategy_type":"infinite_grid","market":"string","create_params":{"money":"string","price_floor":"string","profit_per_grid":"string","grid_num":1,"price_type":0,"trigger_price":"string","stop_profit":"string","stop_loss":"string","profit_sharing_ratio":"string","is_use_base":true}}'
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
    url="/bot/infinite-grid/create"
    query_param=""
    body_param='{"strategy_type":"infinite_grid","market":"string","create_params":{"money":"string","price_floor":"string","profit_per_grid":"string","grid_num":1,"price_type":0,"trigger_price":"string","stop_profit":"string","stop_loss":"string","profit_sharing_ratio":"string","is_use_base":true}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "strategy_type": "infinite_grid",
      "market": "string",
      "create_params": {
        "money": "string",
        "price_floor": "string",
        "profit_per_grid": "string",
        "grid_num": 1,
        "price_type": 0,
        "trigger_price": "string",
        "stop_profit": "string",
        "stop_loss": "string",
        "profit_sharing_ratio": "string",
        "is_use_base": true
      }
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "jump_url": "string"
      },
      "trace_id": "string"
    }
    

##  Create a contract grid🔒 Authenticated

POST`/bot/futures-grid/create`

POST `/bot/futures-grid/create`

_Create a contract grid_

Create a contract grid strategy based on the incoming parameters.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | FuturesGridCreateRequest | Required | none  
↳ strategy_type | body | string | Required | none  
↳ market | body | string | Required | none  
↳ create_params | body | FuturesGridCreateParams | Required | Creation parameters for the contract grid strategy.  
↳ money | body | string | Required | none  
↳ low_price | body | string | Required | none  
↳ high_price | body | string | Required | none  
↳ grid_num | body | integer(int32) | Required | none  
↳ price_type | body | integer(int32) | Required | none  
↳ leverage | body | string | Required | none  
↳ direction | body | FuturesDirection | Optional | Direction enumeration supported by contract-based strategies.  
↳ trigger_price | body | string | Optional | none  
↳ stop_profit | body | string | Optional | none  
↳ stop_loss | body | string | Optional | none  
↳ profit_sharing_ratio | body | string | Optional | none  
↳ is_use_base | body | boolean | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | futures_grid  
»» price_type | 0  
»» price_type | 1  
»» direction | long  
»» direction | short  
»» direction | neutral  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

_The response body when the creation strategy is successful._

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubCreateData | Policy information returned after the policy is successfully created.  
»» strategy_id | string | none  
»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»» market | string | none  
»» status | string | The initial state after successful creation, usually `running`  
»» jump_url | string | none  
» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/futures-grid/create'
    query_param = ''
    body='{"strategy_type":"futures_grid","market":"string","create_params":{"money":"string","low_price":"string","high_price":"string","grid_num":1,"price_type":0,"leverage":"string","direction":"long","trigger_price":"string","stop_profit":"string","stop_loss":"string","profit_sharing_ratio":"string","is_use_base":true}}'
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
    url="/bot/futures-grid/create"
    query_param=""
    body_param='{"strategy_type":"futures_grid","market":"string","create_params":{"money":"string","low_price":"string","high_price":"string","grid_num":1,"price_type":0,"leverage":"string","direction":"long","trigger_price":"string","stop_profit":"string","stop_loss":"string","profit_sharing_ratio":"string","is_use_base":true}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "strategy_type": "futures_grid",
      "market": "string",
      "create_params": {
        "money": "string",
        "low_price": "string",
        "high_price": "string",
        "grid_num": 1,
        "price_type": 0,
        "leverage": "string",
        "direction": "long",
        "trigger_price": "string",
        "stop_profit": "string",
        "stop_loss": "string",
        "profit_sharing_ratio": "string",
        "is_use_base": true
      }
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "jump_url": "string"
      },
      "trace_id": "string"
    }
    

##  Create Spot Martin🔒 Authenticated

POST`/bot/spot-martingale/create`

POST `/bot/spot-martingale/create`

_Create Spot Martin_

Create a spot Martin strategy based on the passed parameters.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | SpotMartingaleCreateRequest | Required | none  
↳ strategy_type | body | string | Required | none  
↳ market | body | string | Required | none  
↳ create_params | body | SpotMartingaleCreateParams | Required | Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).  
\- **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.  
\- Optional **`trigger_price`** : trigger price.  
\- If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).  
↳ invest_amount | body | string | Required | none  
↳ price_deviation | body | string | Required | Add-position deviation ratio as a decimal string (e.g. a 2% drop is `0.02`).  
↳ max_orders | body | integer(int32) | Required | none  
↳ take_profit_ratio | body | string | Required | Take-profit ratio per round as a decimal string.  
↳ stop_loss_per_cycle | body | string | Optional | Stop-loss ratio per round as a decimal string; optional; aligned with app `stop_loss_per_cycle`.  
↳ trigger_price | body | string | Optional | Trigger price; optional.  
↳ profit_sharing_ratio | body | string | Optional | none  
  
####  Detailed descriptions

**» create_params** : Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).  
\- **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.  
\- Optional **`trigger_price`** : trigger price.  
\- If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | spot_martingale  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

_The response body when the creation strategy is successful._

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubCreateData | Policy information returned after the policy is successfully created.  
»» strategy_id | string | none  
»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»» market | string | none  
»» status | string | The initial state after successful creation, usually `running`  
»» jump_url | string | none  
» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/spot-martingale/create'
    query_param = ''
    body='{"strategy_type":"spot_martingale","market":"string","create_params":{"invest_amount":"string","price_deviation":"string","max_orders":1,"take_profit_ratio":"string","stop_loss_per_cycle":"string","trigger_price":"string","profit_sharing_ratio":"string"}}'
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
    url="/bot/spot-martingale/create"
    query_param=""
    body_param='{"strategy_type":"spot_martingale","market":"string","create_params":{"invest_amount":"string","price_deviation":"string","max_orders":1,"take_profit_ratio":"string","stop_loss_per_cycle":"string","trigger_price":"string","profit_sharing_ratio":"string"}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "strategy_type": "spot_martingale",
      "market": "string",
      "create_params": {
        "invest_amount": "string",
        "price_deviation": "string",
        "max_orders": 1,
        "take_profit_ratio": "string",
        "stop_loss_per_cycle": "string",
        "trigger_price": "string",
        "profit_sharing_ratio": "string"
      }
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "jump_url": "string"
      },
      "trace_id": "string"
    }
    

##  Create contract martin🔒 Authenticated

POST`/bot/contract-martingale/create`

POST `/bot/contract-martingale/create`

_Create contract martin_

Create a contract Martin strategy based on the input parameters.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | ContractMartingaleCreateRequest | Required | none  
↳ strategy_type | body | string | Required | none  
↳ market | body | string | Required | none  
↳ create_params | body | ContractMartingaleCreateParams | Required | The creation parameters of the contract Martin strategy.  
↳ invest_amount | body | string | Required | Margin allocated; the server converts it to initial contract size using live contract price, contract multiplier, and minimum lot size.  
↳ price_deviation | body | string | Required | none  
↳ max_orders | body | integer(int32) | Required | none  
↳ take_profit_ratio | body | string | Required | none  
↳ direction | body | ContractMartingaleDirection | Required | The direction enumeration supported by the contract Martin strategy is consistent with the original interface of the App.  
↳ leverage | body | string | Required | none  
↳ stop_loss_price | body | string | Optional | Legacy field name. The AIHub `contract_martingale` creation path does not map this field today;  
follow contract martingale rules from the underlying API. MCP tooling must match bot-service behavior.  
↳ profit_sharing_ratio | body | string | Optional | none  
  
####  Detailed descriptions

**»» stop_loss_price** : Legacy field name. The AIHub `contract_martingale` creation path does not map this field today;  
follow contract martingale rules from the underlying API. MCP tooling must match bot-service behavior.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | contract_martingale  
»» direction | buy  
»» direction | sell  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

_The response body when the creation strategy is successful._

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubCreateData | Policy information returned after the policy is successfully created.  
»» strategy_id | string | none  
»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»» market | string | none  
»» status | string | The initial state after successful creation, usually `running`  
»» jump_url | string | none  
» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/contract-martingale/create'
    query_param = ''
    body='{"strategy_type":"contract_martingale","market":"string","create_params":{"invest_amount":"string","price_deviation":"string","max_orders":1,"take_profit_ratio":"string","direction":"buy","leverage":"string","stop_loss_price":"string","profit_sharing_ratio":"string"}}'
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
    url="/bot/contract-martingale/create"
    query_param=""
    body_param='{"strategy_type":"contract_martingale","market":"string","create_params":{"invest_amount":"string","price_deviation":"string","max_orders":1,"take_profit_ratio":"string","direction":"buy","leverage":"string","stop_loss_price":"string","profit_sharing_ratio":"string"}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "strategy_type": "contract_martingale",
      "market": "string",
      "create_params": {
        "invest_amount": "string",
        "price_deviation": "string",
        "max_orders": 1,
        "take_profit_ratio": "string",
        "direction": "buy",
        "leverage": "string",
        "stop_loss_price": "string",
        "profit_sharing_ratio": "string"
      }
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "jump_url": "string"
      },
      "trace_id": "string"
    }
    

##  Query the list of running policies🔒 Authenticated

GET`/bot/portfolio/running`

GET `/bot/portfolio/running`

_Query the list of running policies_

Query the list of AIHub strategies currently running by the user, and support filtering by strategy type, trading pair and paging conditions.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
strategy_type | query | string | Optional | Filter by policy type  
market | query | string | Optional | Filter by trading pair  
page | query | integer(int32) | Optional | Page number, default 1  
page_size | query | integer(int32) | Optional | Paging size, default 20, maximum 50  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubPortfolioRunningSuccessResponse  
  
### Response Schema

Status Code **200**

_The response body when querying the running policy list is successful._

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubPortfolioRunningData | Running policy list data.  
»» items | array | [A single record in the list of running policies.]  
»»» _None_ | AIHubPortfolioRunningItem | A single record in the list of running policies.  
»»»» strategy_id | string | none  
»»»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»»»» strategy_name | string | none  
»»»» market | string | none  
»»»» status | string | none  
»»»» pnl | string | none  
»»»» pnl_rate | string | none  
»»»» invest_amount | string | none  
»»»» created_at | string | Created time  
»»» page | integer(int32) | none  
»»» page_size | integer(int32) | none  
»»» total | integer(int32) | none  
»» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/portfolio/running'
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
    url="/bot/portfolio/running"
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
      "code": 200,
      "message": "success",
      "data": {
        "items": [
          {}
        ],
        "page": 0,
        "page_size": 0,
        "total": 0
      },
      "trace_id": "string"
    }
    

##  Query order policy details🔒 Authenticated

GET`/bot/portfolio/detail`

GET `/bot/portfolio/detail`

_Query order policy details_

Both `strategy_id` and `strategy_type` must be passed in the request, where `strategy_type` is used to distribute to the underlying detailed implementation by strategy type.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
strategy_id | query | string | Required | Policy ID  
strategy_type | query | string | Required | Policy type; used for underlying detail distribution  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubPortfolioDetailSuccessResponse  
  
### Response Schema

Status Code **200**

_The response body when querying policy details is successful._

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubPortfolioDetailData | Policy details data.  
»» strategy_id | string | none  
»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»» market | string | none  
»» status | string | none  
»» base_info | AIHubPortfolioBaseInfo | Strategy detail base info.  
»»» strategy_name | string | none  
»»» created_at | string | Created time  
»»» running_duration | integer(int64) | Runtime duration in seconds.  
»»» invest_amount | string | none  
»»» total_profit | string | none  
»»» profit_rate | string | none  
»» metrics | AIHubPortfolioMetrics | Strategy detail metrics; fields returned depend on strategy type.  
»»» grid_profit | string | none  
»»» floating_pnl | string | none  
»»» arbitrage_count | integer(int64) | none  
»»» price_range | string | none  
»»» grid_count | integer(int64) | none  
»»» estimated_liquidation_price | string | none  
»»» price_floor | string | none  
»»» grid_profit_rate | string | none  
»»» realized_pnl | string | none  
»»» finished_rounds | integer(int64) | none  
»»» avg_cost | string | none  
»»» take_profit_price | string | none  
»»» maintenance_margin_ratio | string | none  
»» position | AIHubPortfolioPosition|null | Strategy detail position info; fields returned depend on strategy type.  
»»» amount | string | none  
»»» entry_price | string | none  
»»» quote_amount | string | none  
»»» position_value | string | none  
»»» margin | string | none  
»»» side | string | none  
»» stop_supported | boolean | none  
» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/portfolio/detail'
    query_param = 'strategy_id=string&strategy_type=spot_grid'
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
    url="/bot/portfolio/detail"
    query_param="strategy_id=string&strategy_type=spot_grid"
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
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "base_info": {
          "strategy_name": "string",
          "created_at": "string",
          "running_duration": 0,
          "invest_amount": "string",
          "total_profit": "string",
          "profit_rate": "string"
        },
        "metrics": {
          "grid_profit": "string",
          "floating_pnl": "string",
          "arbitrage_count": 0,
          "price_range": "string",
          "grid_count": 0,
          "estimated_liquidation_price": "string",
          "price_floor": "string",
          "grid_profit_rate": "string",
          "realized_pnl": "string",
          "finished_rounds": 0,
          "avg_cost": "string",
          "take_profit_price": "string",
          "maintenance_margin_ratio": "string"
        },
        "position": {
          "amount": "string",
          "entry_price": "string",
          "quote_amount": "string",
          "position_value": "string",
          "margin": "string",
          "side": "string"
        },
        "stop_supported": true
      },
      "trace_id": "string"
    }
    

##  Terminate a single running policy🔒 Authenticated

POST`/bot/portfolio/stop`

POST `/bot/portfolio/stop`

_Terminate a single running policy_

Only one policy is allowed to be terminated per request. Risk warning and secondary confirmation are borne by the upper layer of OpenClaw; this interface is only responsible for executing stop.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | AIHubPortfolioStopRequest | Required | none  
↳ strategy_id | body | string | Required | none  
↳ strategy_type | body | StrategyType | Required | The complete enumeration of policy types supported by AIHub.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | spot_grid  
» strategy_type | margin_grid  
» strategy_type | infinite_grid  
» strategy_type | futures_grid  
» strategy_type | spot_martingale  
» strategy_type | contract_martingale  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Unified business response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubPortfolioStopSuccessResponse  
  
### Response Schema

Status Code **200**

_The response body when the termination strategy is successful._

Name | Type | Description  
---|---|---  
» code | integer(int32) | none  
» message | string | none  
» data | AIHubPortfolioStopData | The result information returned after the termination strategy is successful.  
»» strategy_id | string | none  
»» strategy_type | StrategyType | The complete enumeration of policy types supported by AIHub.  
»» status | string | The current implementation returns `stopping`  
»» result_message | string | none  
» trace_id | string | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    
    url = '/bot/portfolio/stop'
    query_param = ''
    body='{"strategy_id":"string","strategy_type":"spot_grid"}'
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
    url="/bot/portfolio/stop"
    query_param=""
    body_param='{"strategy_id":"string","strategy_type":"spot_grid"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "status": "string",
        "result_message": "string"
      },
      "trace_id": "string"
    }
    

#  Schemas

##  AIHubDiscoverSuccessResponse

Get`the response body when the strategy recommendation is successful.`

Get `the response body when the strategy recommendation is successful.`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubDiscoverData | Required | none | Strategy recommendation result data.  
trace_id | string | Required | none | none  
      
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "scene": "top1",
        "recommendations": [
          {}
        ],
        "unsupported_filters": [
          "string"
        ]
      },
      "trace_id": "string"
    }
    
    

##  AIHubPortfolioStopSuccessResponse

_The response body when the termination strategy is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubPortfolioStopData | Required | none | The result information returned after the termination strategy is successful.  
trace_id | string | Required | none | none  
      
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "status": "string",
        "result_message": "string"
      },
      "trace_id": "string"
    }
    
    

##  AIHubPortfolioStopRequest

_The request body to terminate a running policy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Required | none | none  
strategy_type | StrategyType | Required | none | The complete enumeration of policy types supported by AIHub.  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid"
    }
    
    

##  InfiniteGridCreateRequest

_Create the request body for the infinite grid policy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_type | string | Required | none | none  
market | string | Required | none | none  
create_params | InfiniteGridCreateParams | Required | none | Creation parameters for infinite grid strategies.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | infinite_grid  
      
    
    {
      "strategy_type": "infinite_grid",
      "market": "string",
      "create_params": {
        "money": "string",
        "price_floor": "string",
        "profit_per_grid": "string",
        "grid_num": 1,
        "price_type": 0,
        "trigger_price": "string",
        "stop_profit": "string",
        "stop_loss": "string",
        "profit_sharing_ratio": "string",
        "is_use_base": true
      }
    }
    
    

##  StrategyType

_The complete enumeration of policy types supported by AIHub._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | string | Optional | none | The complete enumeration of policy types supported by AIHub.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
_None_ | spot_grid  
_None_ | margin_grid  
_None_ | infinite_grid  
_None_ | futures_grid  
_None_ | spot_martingale  
_None_ | contract_martingale  
      
    
    "spot_grid"
    
    

##  AIHubPortfolioRunningSuccessResponse

_The response body when querying the running policy list is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubPortfolioRunningData | Required | none | Running policy list data.  
trace_id | string | Required | none | none  
      
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "items": [
          {}
        ],
        "page": 0,
        "page_size": 0,
        "total": 0
      },
      "trace_id": "string"
    }
    
    

##  SpotGridCreateRequest

_Create the request body for the spot grid policy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_type | string | Required | none | none  
market | string | Required | none | none  
create_params | SpotGridCreateParams | Required | none | Creation parameters for the spot grid strategy.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
      
    
    {
      "strategy_type": "spot_grid",
      "market": "string",
      "create_params": {
        "money": "string",
        "low_price": "string",
        "high_price": "string",
        "grid_num": 1,
        "price_type": 0,
        "trigger_price": "string",
        "stop_profit": "string",
        "stop_loss": "string",
        "profit_sharing_ratio": "string",
        "is_use_base": true
      }
    }
    
    

##  AIHubDiscoverData

_Strategy recommendation result data._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
scene | DiscoverScene | Required | none | Enumeration of scenarios supported by the policy recommendation interface.  
recommendations | [AIHubRecommendation] | Required | none | [A single piece of strategy recommendation information.]  
unsupported_filters | array | Required | none | Filter conditions not supported in this issue  
      
    
    {
      "scene": "top1",
      "recommendations": [
        {
          "recommendation_id": "string",
          "market": "string",
          "strategy_type": "spot_grid",
          "strategy_name": "string",
          "backtest_apr": "string",
          "max_drawdown": "string",
          "summary": "string",
          "strategy_params_preview": "string"
        }
      ],
      "unsupported_filters": [
        "string"
      ]
    }
    
    

##  InfiniteGridCreateParams

_Creation parameters for infinite grid strategies._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
money | string | Required | none | none  
price_floor | string | Required | none | price floor  
profit_per_grid | string | Required | none | Profit per square  
grid_num | integer(int32) | Optional | none | Optional; may be omitted like in the app.  
price_type | integer(int32) | Optional | none | Optional. `0` arithmetic grid; `1` geometric; omit for server defaults.  
trigger_price | string | Optional | none | none  
stop_profit | string | Optional | none | none  
stop_loss | string | Optional | none | none  
profit_sharing_ratio | string | Optional | none | none  
is_use_base | boolean | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
      
    
    {
      "money": "string",
      "price_floor": "string",
      "profit_per_grid": "string",
      "grid_num": 1,
      "price_type": 0,
      "trigger_price": "string",
      "stop_profit": "string",
      "stop_loss": "string",
      "profit_sharing_ratio": "string",
      "is_use_base": true
    }
    
    

##  FuturesGridCreateRequest

_Create the request body of the contract grid strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_type | string | Required | none | none  
market | string | Required | none | none  
create_params | FuturesGridCreateParams | Required | none | Creation parameters for the contract grid strategy.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | futures_grid  
      
    
    {
      "strategy_type": "futures_grid",
      "market": "string",
      "create_params": {
        "money": "string",
        "low_price": "string",
        "high_price": "string",
        "grid_num": 1,
        "price_type": 0,
        "leverage": "string",
        "direction": "long",
        "trigger_price": "string",
        "stop_profit": "string",
        "stop_loss": "string",
        "profit_sharing_ratio": "string",
        "is_use_base": true
      }
    }
    
    

##  AIHubRecommendation

_A single piece of strategy recommendation information._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
recommendation_id | string | Required | none | none  
market | string | Required | none | none  
strategy_type | StrategyType | Required | none | The complete enumeration of policy types supported by AIHub.  
strategy_name | string | Required | none | none  
backtest_apr | string | Optional | none | none  
max_drawdown | string | Optional | none | none  
summary | string | Required | none | none  
strategy_params_preview | string | Optional | none | Recommended-parameter preview as JSON text (string-encoded so clients deserialize it consistently). The value is a serialized JSON object whose structure varies by strategy type; callers or upper-layer models must parse it.  
      
    
    {
      "recommendation_id": "string",
      "market": "string",
      "strategy_type": "spot_grid",
      "strategy_name": "string",
      "backtest_apr": "string",
      "max_drawdown": "string",
      "summary": "string",
      "strategy_params_preview": "string"
    }
    
    

##  MarginGridCreateRequest

_Create the request body for the Leverage Grid strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_type | string | Required | none | none  
market | string | Required | none | none  
create_params | MarginGridCreateParams | Required | none | Creation parameters for the Leverage Grid strategy.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | margin_grid  
      
    
    {
      "strategy_type": "margin_grid",
      "market": "string",
      "create_params": {
        "money": "string",
        "low_price": "string",
        "high_price": "string",
        "grid_num": 1,
        "price_type": 0,
        "leverage": "string",
        "direction": "long",
        "trigger_price": "string",
        "stop_profit": "string",
        "stop_loss": "string",
        "profit_sharing_ratio": "string",
        "is_use_base": true
      }
    }
    
    

##  FuturesGridCreateParams

_Creation parameters for the contract grid strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
money | string | Required | none | none  
low_price | string | Required | none | none  
high_price | string | Required | none | none  
grid_num | integer(int32) | Required | none | none  
price_type | integer(int32) | Required | none | none  
leverage | string | Required | none | none  
direction | FuturesDirection | Optional | none | Direction enumeration supported by contract-based strategies.  
trigger_price | string | Optional | none | none  
stop_profit | string | Optional | none | none  
stop_loss | string | Optional | none | none  
profit_sharing_ratio | string | Optional | none | none  
is_use_base | boolean | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
      
    
    {
      "money": "string",
      "low_price": "string",
      "high_price": "string",
      "grid_num": 1,
      "price_type": 0,
      "leverage": "string",
      "direction": "long",
      "trigger_price": "string",
      "stop_profit": "string",
      "stop_loss": "string",
      "profit_sharing_ratio": "string",
      "is_use_base": true
    }
    
    

##  AIHubPortfolioDetailSuccessResponse

_The response body when querying policy details is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubPortfolioDetailData | Required | none | Policy details data.  
trace_id | string | Required | none | none  
      
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "base_info": {
          "strategy_name": "string",
          "created_at": "string",
          "running_duration": 0,
          "invest_amount": "string",
          "total_profit": "string",
          "profit_rate": "string"
        },
        "metrics": {
          "grid_profit": "string",
          "floating_pnl": "string",
          "arbitrage_count": 0,
          "price_range": "string",
          "grid_count": 0,
          "estimated_liquidation_price": "string",
          "price_floor": "string",
          "grid_profit_rate": "string",
          "realized_pnl": "string",
          "finished_rounds": 0,
          "avg_cost": "string",
          "take_profit_price": "string",
          "maintenance_margin_ratio": "string"
        },
        "position": {
          "amount": "string",
          "entry_price": "string",
          "quote_amount": "string",
          "position_value": "string",
          "margin": "string",
          "side": "string"
        },
        "stop_supported": true
      },
      "trace_id": "string"
    }
    
    

##  AIHubCreateSuccessResponse

_The response body when the creation strategy is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubCreateData | Required | none | Policy information returned after the policy is successfully created.  
trace_id | string | Required | none | none  
      
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "jump_url": "string"
      },
      "trace_id": "string"
    }
    
    

##  SpotMartingaleCreateRequest

_Create the request body of the Spot Martin strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_type | string | Required | none | none  
market | string | Required | none | none  
create_params | SpotMartingaleCreateParams | Required | none | Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).  
\- **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.  
\- Optional **`trigger_price`** : trigger price.  
\- If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_martingale  
      
    
    {
      "strategy_type": "spot_martingale",
      "market": "string",
      "create_params": {
        "invest_amount": "string",
        "price_deviation": "string",
        "max_orders": 1,
        "take_profit_ratio": "string",
        "stop_loss_per_cycle": "string",
        "trigger_price": "string",
        "profit_sharing_ratio": "string"
      }
    }
    
    

##  ContractMartingaleCreateRequest

_Create the request body of the contract Martin strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_type | string | Required | none | none  
market | string | Required | none | none  
create_params | ContractMartingaleCreateParams | Required | none | The creation parameters of the contract Martin strategy.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | contract_martingale  
      
    
    {
      "strategy_type": "contract_martingale",
      "market": "string",
      "create_params": {
        "invest_amount": "string",
        "price_deviation": "string",
        "max_orders": 1,
        "take_profit_ratio": "string",
        "direction": "buy",
        "leverage": "string",
        "stop_loss_price": "string",
        "profit_sharing_ratio": "string"
      }
    }
    
    

##  SpotGridCreateParams

_Creation parameters for the spot grid strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
money | string | Required | none | Amount of investment  
low_price | string | Required | none | Range lower limit  
high_price | string | Required | none | Range upper limit  
grid_num | integer(int32) | Required | none | Number of grids  
price_type | integer(int32) | Required | none | none  
trigger_price | string | Optional | none | none  
stop_profit | string | Optional | none | none  
stop_loss | string | Optional | none | none  
profit_sharing_ratio | string | Optional | none | none  
is_use_base | boolean | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
      
    
    {
      "money": "string",
      "low_price": "string",
      "high_price": "string",
      "grid_num": 1,
      "price_type": 0,
      "trigger_price": "string",
      "stop_profit": "string",
      "stop_loss": "string",
      "profit_sharing_ratio": "string",
      "is_use_base": true
    }
    
    

##  DiscoverScene

_Enumeration of scenarios supported by the policy recommendation interface._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | string | Optional | none | Enumeration of scenarios supported by the policy recommendation interface.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
_None_ | top1  
_None_ | bundle  
_None_ | filter  
_None_ | refresh  
      
    
    "top1"
    
    

##  MarginGridCreateParams

_Creation parameters for the Leverage Grid strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
money | string | Required | none | none  
low_price | string | Required | none | none  
high_price | string | Required | none | none  
grid_num | integer(int32) | Required | none | none  
price_type | integer(int32) | Required | none | none  
leverage | string | Required | none | none  
direction | FuturesDirection | Optional | none | Direction enumeration supported by contract-based strategies.  
trigger_price | string | Optional | none | none  
stop_profit | string | Optional | none | none  
stop_loss | string | Optional | none | none  
profit_sharing_ratio | string | Optional | none | none  
is_use_base | boolean | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
price_type | 0  
price_type | 1  
      
    
    {
      "money": "string",
      "low_price": "string",
      "high_price": "string",
      "grid_num": 1,
      "price_type": 0,
      "leverage": "string",
      "direction": "long",
      "trigger_price": "string",
      "stop_profit": "string",
      "stop_loss": "string",
      "profit_sharing_ratio": "string",
      "is_use_base": true
    }
    
    

##  AIHubPortfolioDetailData

_Policy details data._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Required | none | none  
strategy_type | StrategyType | Required | none | The complete enumeration of policy types supported by AIHub.  
market | string | Required | none | none  
status | string | Required | none | none  
base_info | AIHubPortfolioBaseInfo | Required | none | Strategy detail base info.  
metrics | AIHubPortfolioMetrics | Required | none | Strategy detail metrics; fields returned depend on strategy type.  
position | AIHubPortfolioPosition | Optional | none | Strategy detail position info; fields returned depend on strategy type.  
stop_supported | boolean | Required | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "market": "string",
      "status": "string",
      "base_info": {
        "strategy_name": "string",
        "created_at": "string",
        "running_duration": 0,
        "invest_amount": "string",
        "total_profit": "string",
        "profit_rate": "string"
      },
      "metrics": {
        "grid_profit": "string",
        "floating_pnl": "string",
        "arbitrage_count": 0,
        "price_range": "string",
        "grid_count": 0,
        "estimated_liquidation_price": "string",
        "price_floor": "string",
        "grid_profit_rate": "string",
        "realized_pnl": "string",
        "finished_rounds": 0,
        "avg_cost": "string",
        "take_profit_price": "string",
        "maintenance_margin_ratio": "string"
      },
      "position": {
        "amount": "string",
        "entry_price": "string",
        "quote_amount": "string",
        "position_value": "string",
        "margin": "string",
        "side": "string"
      },
      "stop_supported": true
    }
    
    

##  AIHubPortfolioStopData

_The result information returned after the termination strategy is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Required | none | none  
strategy_type | StrategyType | Required | none | The complete enumeration of policy types supported by AIHub.  
status | string | Required | none | The current implementation returns `stopping`  
result_message | string | Required | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "status": "string",
      "result_message": "string"
    }
    
    

##  AIHubCreateData

_Policy information returned after the policy is successfully created._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Required | none | none  
strategy_type | StrategyType | Required | none | The complete enumeration of policy types supported by AIHub.  
market | string | Required | none | none  
status | string | Required | none | The initial state after successful creation, usually `running`  
jump_url | string | Optional | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "market": "string",
      "status": "string",
      "jump_url": "string"
    }
    
    

##  AIHubPortfolioRunningData

_Running policy list data._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
items | [AIHubPortfolioRunningItem] | Required | none | [A single record in the list of running policies.]  
page | integer(int32) | Required | none | none  
page_size | integer(int32) | Required | none | none  
total | integer(int32) | Required | none | none  
      
    
    {
      "items": [
        {
          "strategy_id": "string",
          "strategy_type": "spot_grid",
          "strategy_name": "string",
          "market": "string",
          "status": "string",
          "pnl": "string",
          "pnl_rate": "string",
          "invest_amount": "string",
          "created_at": "string"
        }
      ],
      "page": 0,
      "page_size": 0,
      "total": 0
    }
    
    

##  FuturesDirection

_Direction enumeration supported by contract-based strategies._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | string | Optional | none | Direction enumeration supported by contract-based strategies.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
_None_ | long  
_None_ | short  
_None_ | neutral  
      
    
    "long"
    
    

##  SpotMartingaleCreateParams

*Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).

  * **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.
  * Optional **`trigger_price`** : trigger price.
  * If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).*

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
invest_amount | string | Required | none | none  
price_deviation | string | Required | none | Add-position deviation ratio as a decimal string (e.g. a 2% drop is `0.02`).  
max_orders | integer(int32) | Required | none | none  
take_profit_ratio | string | Required | none | Take-profit ratio per round as a decimal string.  
stop_loss_per_cycle | string | Optional | none | Stop-loss ratio per round as a decimal string; optional; aligned with app `stop_loss_per_cycle`.  
trigger_price | string | Optional | none | Trigger price; optional.  
profit_sharing_ratio | string | Optional | none | none  
      
    
    {
      "invest_amount": "string",
      "price_deviation": "string",
      "max_orders": 1,
      "take_profit_ratio": "string",
      "stop_loss_per_cycle": "string",
      "trigger_price": "string",
      "profit_sharing_ratio": "string"
    }
    
    

##  ContractMartingaleCreateParams

_The creation parameters of the contract Martin strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
invest_amount | string | Required | none | Margin allocated; the server converts it to initial contract size using live contract price, contract multiplier, and minimum lot size.  
price_deviation | string | Required | none | none  
max_orders | integer(int32) | Required | none | none  
take_profit_ratio | string | Required | none | none  
direction | ContractMartingaleDirection | Required | none | The direction enumeration supported by the contract Martin strategy is consistent with the original interface of the App.  
leverage | string | Required | none | none  
stop_loss_price | string | Optional | none | Legacy field name. The AIHub `contract_martingale` creation path does not map this field today;  
follow contract martingale rules from the underlying API. MCP tooling must match bot-service behavior.  
profit_sharing_ratio | string | Optional | none | none  
      
    
    {
      "invest_amount": "string",
      "price_deviation": "string",
      "max_orders": 1,
      "take_profit_ratio": "string",
      "direction": "buy",
      "leverage": "string",
      "stop_loss_price": "string",
      "profit_sharing_ratio": "string"
    }
    
    

##  AIHubPortfolioRunningItem

_A single record in the list of running policies._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Required | none | none  
strategy_type | StrategyType | Required | none | The complete enumeration of policy types supported by AIHub.  
strategy_name | string | Required | none | none  
market | string | Required | none | none  
status | string | Required | none | none  
pnl | string | Optional | none | none  
pnl_rate | string | Optional | none | none  
invest_amount | string | Optional | none | none  
created_at | string | Optional | none | Created time  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "strategy_name": "string",
      "market": "string",
      "status": "string",
      "pnl": "string",
      "pnl_rate": "string",
      "invest_amount": "string",
      "created_at": "string"
    }
    
    

##  AIHubPortfolioMetrics

_Strategy detail metrics; fields returned depend on strategy type._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
grid_profit | string | Optional | none | none  
floating_pnl | string | Optional | none | none  
arbitrage_count | integer(int64) | Optional | none | none  
price_range | string | Optional | none | none  
grid_count | integer(int64) | Optional | none | none  
estimated_liquidation_price | string | Optional | none | none  
price_floor | string | Optional | none | none  
grid_profit_rate | string | Optional | none | none  
realized_pnl | string | Optional | none | none  
finished_rounds | integer(int64) | Optional | none | none  
avg_cost | string | Optional | none | none  
take_profit_price | string | Optional | none | none  
maintenance_margin_ratio | string | Optional | none | none  
      
    
    {
      "grid_profit": "string",
      "floating_pnl": "string",
      "arbitrage_count": 0,
      "price_range": "string",
      "grid_count": 0,
      "estimated_liquidation_price": "string",
      "price_floor": "string",
      "grid_profit_rate": "string",
      "realized_pnl": "string",
      "finished_rounds": 0,
      "avg_cost": "string",
      "take_profit_price": "string",
      "maintenance_margin_ratio": "string"
    }
    
    

##  AIHubPortfolioBaseInfo

_Strategy detail base info._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_name | string | Required | none | none  
created_at | string | Required | none | Created time  
running_duration | integer(int64) | Required | none | Runtime duration in seconds.  
invest_amount | string | Required | none | none  
total_profit | string | Required | none | none  
profit_rate | string | Required | none | none  
      
    
    {
      "strategy_name": "string",
      "created_at": "string",
      "running_duration": 0,
      "invest_amount": "string",
      "total_profit": "string",
      "profit_rate": "string"
    }
    
    

##  AIHubPortfolioPosition

_Strategy detail position info; fields returned depend on strategy type._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
amount | string | Optional | none | none  
entry_price | string | Optional | none | none  
quote_amount | string | Optional | none | none  
position_value | string | Optional | none | none  
margin | string | Optional | none | none  
side | string | Optional | none | none  
      
    
    {
      "amount": "string",
      "entry_price": "string",
      "quote_amount": "string",
      "position_value": "string",
      "margin": "string",
      "side": "string"
    }
    
    

##  ContractMartingaleDirection

_The direction enumeration supported by the contract Martin strategy is consistent with the original interface of the App._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | string | Optional | none | The direction enumeration supported by the contract Martin strategy is consistent with the original interface of the App.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
_None_ | buy  
_None_ | sell  
      
    
    "buy"