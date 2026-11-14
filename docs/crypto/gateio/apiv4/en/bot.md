---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/bot
api_type: REST
updated_at: 2026-11-13 20:56:55.702149
---

# Bot

Bot AIHub policy recommendation, creation, query and termination interface

##  Get AIHub strategy recommendations🔒 Authenticated

GET`/bot/strategy/recommend`

GET `/bot/strategy/recommend`

_Get AIHub strategy recommendations_

Six real official source types. Exact rebalance asset membership is filtered before ranking. contract_martingale and futures_combo are manual-only. Legacy APR/drawdown and ordinary two-segment refresh remain compatible. Exclusion binds one prior logical candidate before ranking; no alternative returns an empty list without relaxing constraints.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
market | query | string | Optional | Trading pair, such as `BTC_USDT`  
strategy_type | query | string | Optional | Recommended target policy type; `contract_martingale` not allowed  
direction | query | string | Optional | Market direction  
invest_amount | query | string | Optional | Context only. No budget eligibility filter; reported unsupported when not consumed.  
scene | query | string | Optional | Recommended scenario; when empty, bot-service can automatically infer according to the implementation logic.  
refresh_recommendation_id | query | string | Optional | It is recommended to refresh the context. Used when `scene=refresh` is used; when `scene` is empty but the field exists, bot-service will also automatically determine as `refresh`.  
The official minimum format is `strategy_type|market`; if the `recommendation_id` of the previous recommendation is directly passed through, the third paragraph `backtest_id` will be ignored.  
limit | query | integer(int32) | Optional | Actual maximum result count, 1–10; defaults to 10.  
max_drawdown_lte | query | string | Optional | Maximum drawdown limit  
backtest_apr_gte | query | string | Optional | Backtest annualized lower limit  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
exclude_recommendation_id | query | string | Optional | Refresh-only previous returned identity: type  
  
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
strategy_type | smart_position  
direction | buy  
direction | sell  
direction | neutral  
scene | top1  
scene | bundle  
scene | filter  
scene | refresh  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubDiscoverSuccessResponse  
  
### Response Schema

Status Code **200**

_Get the response body when the strategy recommendation is successful._

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
»» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
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
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
      "trace_id": "string",
      "label": "string"
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
» strategy_type | body | string | Required | none  
» market | body | string | Required | none  
» create_params | body | SpotGridCreateParams | Required | Creation parameters for the spot grid strategy.  
»» money | body | string | Required | Amount of investment  
»» low_price | body | string | Required | Range lower limit  
»» high_price | body | string | Required | Range upper limit  
»» grid_num | body | integer(int32) | Required | Number of grids  
»» price_type | body | integer(int32) | Required | none  
»» trigger_price | body | string | Optional | none  
»» stop_profit | body | string | Optional | none  
»» stop_loss | body | string | Optional | none  
»» profit_sharing_ratio | body | string | Optional | none  
»» is_use_base | body | boolean | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | spot_grid  
»» price_type | 0  
»» price_type | 1  
  
### Responses

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
»» status | string | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
»» jump_url | string | none  
»» operation_status | string | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
»» recovery_required | boolean | none  
» trace_id | string | none  
» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
        "jump_url": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
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
» strategy_type | body | string | Required | none  
» market | body | string | Required | none  
» create_params | body | MarginGridCreateParams | Required | Creation parameters for the Leverage Grid strategy.  
»» money | body | string | Required | none  
»» low_price | body | string | Required | none  
»» high_price | body | string | Required | none  
»» grid_num | body | integer(int32) | Required | none  
»» price_type | body | integer(int32) | Required | none  
»» leverage | body | string | Required | none  
»» direction | body | FuturesDirection | Optional | Direction enumeration supported by contract-based strategies.  
»» trigger_price | body | string | Optional | none  
»» stop_profit | body | string | Optional | none  
»» stop_loss | body | string | Optional | none  
»» profit_sharing_ratio | body | string | Optional | none  
»» is_use_base | body | boolean | Optional | none  
  
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
»» status | string | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
»» jump_url | string | none  
»» operation_status | string | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
»» recovery_required | boolean | none  
» trace_id | string | none  
» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
        "jump_url": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
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
» strategy_type | body | string | Required | none  
» market | body | string | Required | none  
» create_params | body | InfiniteGridCreateParams | Required | Infinite grid creation parameters.  
Aligned with the app: **`money`** , **`price_floor`** , and **`profit_per_grid`** are required;  
`grid_num` and `price_type` are optional (defaults applied server-side when omitted).  
»» money | body | string | Required | none  
»» price_floor | body | string | Required | price floor  
»» profit_per_grid | body | string | Required | Profit per square  
»» grid_num | body | integer(int32) | Optional | Optional; may be omitted like in the app.  
»» price_type | body | integer(int32) | Optional | Optional. `0` arithmetic grid; `1` geometric; omit for server defaults.  
»» trigger_price | body | string | Optional | none  
»» stop_profit | body | string | Optional | none  
»» stop_loss | body | string | Optional | none  
»» profit_sharing_ratio | body | string | Optional | none  
»» is_use_base | body | boolean | Optional | none  
  
####  Detailed descriptions

**» create_params** : Infinite grid creation parameters.  
Aligned with the app: **`money`** , **`price_floor`** , and **`profit_per_grid`** are required;  
`grid_num` and `price_type` are optional (defaults applied server-side when omitted).

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | infinite_grid  
»» price_type | 0  
»» price_type | 1  
  
### Responses

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
»» status | string | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
»» jump_url | string | none  
»» operation_status | string | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
»» recovery_required | boolean | none  
» trace_id | string | none  
» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
        "jump_url": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
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
» strategy_type | body | string | Required | none  
» market | body | string | Required | none  
» create_params | body | FuturesGridCreateParams | Required | Creation parameters for the contract grid strategy.  
»» money | body | string | Required | none  
»» low_price | body | string | Required | none  
»» high_price | body | string | Required | none  
»» grid_num | body | integer(int32) | Required | none  
»» price_type | body | integer(int32) | Required | none  
»» leverage | body | string | Required | none  
»» direction | body | FuturesDirection | Optional | Direction enumeration supported by contract-based strategies.  
»» trigger_price | body | string | Optional | none  
»» stop_profit | body | string | Optional | none  
»» stop_loss | body | string | Optional | none  
»» profit_sharing_ratio | body | string | Optional | none  
»» is_use_base | body | boolean | Optional | none  
  
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
»» status | string | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
»» jump_url | string | none  
»» operation_status | string | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
»» recovery_required | boolean | none  
» trace_id | string | none  
» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
        "jump_url": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
    }
    

##  Create Spot Martin🔒 Authenticated

POST`/bot/spot-martingale/create`

POST `/bot/spot-martingale/create`

_Create Spot Martin_

Create a spot martingale strategy from the given parameters. Stop-loss semantics match the app / `MartingaleBot`:

  * Use **`create_params.stop_loss_per_cycle`** (ratio per round as a decimal string) for creation-side stop-loss; **do not** use `stop_loss_price` for creation logic.
  * Stop-loss prices shown on detail pages are computed per round by the engine; creation accepts optional **`create_params.trigger_price`** (trigger price).

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | SpotMartingaleCreateRequest | Required | none  
» strategy_type | body | string | Required | none  
» market | body | string | Required | none  
» create_params | body | SpotMartingaleCreateParams | Required | Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).  
\- **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.  
\- Optional **`trigger_price`** : trigger price.  
\- If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).  
»» invest_amount | body | string | Required | none  
»» price_deviation | body | string | Required | Add-position deviation ratio as a decimal string (e.g. a 2% drop is `0.02`).  
»» max_orders | body | integer(int32) | Required | none  
»» take_profit_ratio | body | string | Required | Take-profit ratio per round as a decimal string.  
»» stop_loss_per_cycle | body | string | Optional | Stop-loss ratio per round as a decimal string; optional; aligned with app `stop_loss_per_cycle`.  
»» trigger_price | body | string | Optional | Trigger price; optional.  
»» profit_sharing_ratio | body | string | Optional | none  
  
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
»» status | string | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
»» jump_url | string | none  
»» operation_status | string | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
»» recovery_required | boolean | none  
» trace_id | string | none  
» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
        "jump_url": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
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
» strategy_type | body | string | Required | none  
» market | body | string | Required | none  
» create_params | body | ContractMartingaleCreateParams | Required | The creation parameters of the contract Martin strategy.  
»» invest_amount | body | string | Required | Total strategy budget, not first-order margin. The server uses the complete existing ladder formula, owner fee and live contract facts, quantizes quantity down and rechecks before allocation. Minimum infeasible budget is rejected.  
»» price_deviation | body | string | Required | none  
»» max_orders | body | integer(int32) | Required | Maximum additional entries, excluding the first; preserve this legacy meaning.  
»» take_profit_ratio | body | string | Required | none  
»» direction | body | ContractMartingaleDirection | Required | The direction enumeration supported by the contract Martin strategy is consistent with the original interface of the App.  
»» leverage | body | string | Required | none  
»» stop_loss_price | body | string | Optional | Positive fixed stop price; requires explicit stop_loss_price_type. Missing both leaves the old no-fixed-stop request unchanged.  
»» profit_sharing_ratio | body | string | Optional | none  
»» stop_loss_price_type | body | string | Optional | none  
»» _None_ | body | any | Optional | none  
»»» _None_ | body | any | Optional | none  
»»»» _None_ | body | object | Optional | none  
»»»» _None_ | body | object | Optional | none  
»»» _None_ | body | object | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | contract_martingale  
»» direction | buy  
»» direction | sell  
»» stop_loss_price_type | last  
»» stop_loss_price_type | index  
»» stop_loss_price_type | mark  
  
### Responses

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
»» status | string | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
»» jump_url | string | none  
»» operation_status | string | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
»» recovery_required | boolean | none  
» trace_id | string | none  
» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
    body='{"strategy_type":"contract_martingale","market":"string","create_params":{"invest_amount":"string","price_deviation":"string","max_orders":1,"take_profit_ratio":"string","direction":"buy","leverage":"string","stop_loss_price":"string","profit_sharing_ratio":"string","stop_loss_price_type":"last"}}'
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
    body_param='{"strategy_type":"contract_martingale","market":"string","create_params":{"invest_amount":"string","price_deviation":"string","max_orders":1,"take_profit_ratio":"string","direction":"buy","leverage":"string","stop_loss_price":"string","profit_sharing_ratio":"string","stop_loss_price_type":"last"}}'
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
        "profit_sharing_ratio": "string",
        "stop_loss_price_type": "last"
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
        "jump_url": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
    }
    

##  List running strategies.🔒 Authenticated

GET`/bot/portfolio/running`

GET `/bot/portfolio/running`

_List running strategies._

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
strategy_type | smart_position  
strategy_type | futures_combo  
  
### Responses

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
»»»» market | string | Single market, or empty string for a portfolio; use assets/markets for the latter.  
»»»» status | string | none  
»»»» pnl | string | none  
»»»» pnl_rate | string | none  
»»»» invest_amount | string | none  
»»»» created_at | string | Created time  
»»»» assets | array | none  
»»»» markets | array | none  
»»» page | integer(int32) | none  
»»» page_size | integer(int32) | none  
»»» total | integer(int32) | none  
»» trace_id | string | none  
»» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
      "trace_id": "string",
      "label": "string"
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
strategy_type | smart_position  
strategy_type | futures_combo  
  
### Responses

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
»» market | string | Single market, or empty string for a portfolio; use assets/markets for the latter.  
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
»» assets | array | none  
»» markets | array | none  
»» positions | array | [Position information for one asset or market in a portfolio strategy.]  
»»» _None_ | AIHubPortfolioAssetPosition | Position information for one asset or market in a portfolio strategy.  
»»»» asset | string | none  
»»»» market | string | none  
»»»» side | string | none  
»»»» amount | string | none  
»»»» amount_unit | string | none  
»»»» entry_price | string | none  
»»»» position_value | string | none  
»»»» position_value_unit | string | none  
»»»» target_weight | string | none  
»»»» leverage | string | none  
»»» positions_status | string | none  
»»» configuration | object | Product-specific saved configuration. spot_martingale exposes AIHubSpotMartingaleConfiguration; absence is unverified. Runtime recovery internals are excluded.  
»»» stop_progress | AIHubStopProgress | Read-only projection of durable facts. Absent values are unverified. Final refund excludes ordinary decrease-principal transfers. Account release is never inferred from stopped status or an empty account.  
»»»» trading_finished | boolean | none  
»»»» funds_returned | boolean | none  
»»»» refund_amount | string | none  
»»»» refund_currency | string | none  
»»»» account_released | boolean | none  
»»» trace_id | string | none  
»»» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
positions_status | verified  
positions_status | partial  
positions_status | unverified  
positions_status | historical  
  
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
        "stop_supported": true,
        "assets": [
          "string"
        ],
        "markets": [
          "string"
        ],
        "positions": [
          {}
        ],
        "positions_status": "verified",
        "configuration": {},
        "stop_progress": {
          "trading_finished": true,
          "funds_returned": true,
          "refund_amount": "string",
          "refund_currency": "string",
          "account_released": true
        }
      },
      "trace_id": "string",
      "label": "string"
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
» strategy_id | body | string | Required | none  
» strategy_type | body | StrategyType | Required | The complete enumeration of policy types supported by AIHub.  
» stop_mode | body | string | Optional | Required only for smart_position. Other types reject custom exit options.  
» stop_options | body | AIHubRebalanceStopOptions | Optional | Options for the limit stop mode of a smart-position strategy.  
»» price | body | string | Required | One product-supported price expression; not one expression per member.  
»» expiration | body | integer(int64) | Required | Seconds of validity. Expiry cancels and returns assets; never switches to market.  
»» slip | body | string | Optional | Optional ratio 0.001–0.05, precision at most six.  
» _None_ | body | object | Optional | none  
»» strategy_type | body | any | Optional | none  
»»» _None_ | body | string | Optional | none  
»» _None_ | body | any | Optional | none  
»»» _None_ | body | object | Optional | none  
»»» _None_ | body | object | Optional | none  
»» _None_ | body | object | Optional | none  
»»» strategy_type | body | string | Optional | none  
»»» stop_mode | body | any | Required | none  
»»» _None_ | body | object | Optional | none  
»» _None_ | body | object | Optional | none  
»»» strategy_type | body | string | Optional | none  
»»» stop_mode | body | string | Required | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | spot_grid  
» strategy_type | margin_grid  
» strategy_type | infinite_grid  
» strategy_type | futures_grid  
» strategy_type | spot_martingale  
» strategy_type | contract_martingale  
» strategy_type | smart_position  
» strategy_type | futures_combo  
» stop_mode | market  
» stop_mode | limit  
» stop_mode | no_close  
»»» _None_ | smart_position  
»»» strategy_type | smart_position  
»»» stop_mode | market  
»»» stop_mode | no_close  
»»» strategy_type | smart_position  
»»» stop_mode | limit  
  
### Responses

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
»» status | string | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
»» result_message | string | none  
»» operation_status | string | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
»» recovery_required | boolean | none  
» trace_id | string | none  
» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
    body='{"strategy_id":"string","strategy_type":null,"stop_mode":"market","stop_options":{"price":"string","expiration":1,"slip":"string"}}'
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
    body_param='{"strategy_id":"string","strategy_type":null,"stop_mode":"market","stop_options":{"price":"string","expiration":1,"slip":"string"}}'
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
      "strategy_type": null,
      "stop_mode": "market",
      "stop_options": {
        "price": "string",
        "expiration": 1,
        "slip": "string"
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
        "status": "string",
        "result_message": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
    }
    

##  Create rebalance bot🔒 Authenticated

POST`/bot/smart-position/create`

POST `/bot/smart-position/create`

_Create rebalance bot_

Typed AIHub adapter; authenticated owner comes only from trusted gateway context.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | AIHubRebalanceCreateRequest | Required | none  
» strategy_type | body | string | Required | none  
» create_params | body | AIHubRebalanceCreateParams | Required | Creation parameters for a smart-position strategy.  
»» begin_money_amount | body | string | Required | none  
»» begin_money_currency | body | string | Required | none  
»» asset_info | body | array | Required | [One asset and its target weight in a smart-position strategy.]  
»»» _None_ | body | AIHubRebalanceAsset | Optional | One asset and its target weight in a smart-position strategy.  
»»»» asset | body | string | Required | none  
»»»» rate | body | string | Required | Two decimal places, minimum 0.01; unique assets and sum exactly 1.  
»»» period | body | string | Optional | Product interval between 1m and 28d.  
»»» threshold | body | string | Optional | Positive ratio below 1, at most four decimal places.  
»»» close_flag | body | integer | Optional | none  
»»» is_use_base | body | boolean | Optional | none  
»»» stop_profit | body | string | Optional | none  
»»» stop_loss | body | string | Optional | none  
»»» _None_ | body | object | Optional | none  
»»»» _None_ | body | object | Optional | none  
»»» _None_ | body | object | Optional | none  
»»»» _None_ | body | object | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | smart_position  
»» begin_money_currency | USDT  
»»» close_flag | 0  
»»» close_flag | 1  
  
### Responses

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
»» status | string | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
»» jump_url | string | none  
»» operation_status | string | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
»» recovery_required | boolean | none  
» trace_id | string | none  
» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
    
    url = '/bot/smart-position/create'
    query_param = ''
    body='{"strategy_type":"smart_position","create_params":{}}'
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
    url="/bot/smart-position/create"
    query_param=""
    body_param='{"strategy_type":"smart_position","create_params":{}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "strategy_type": "smart_position",
      "create_params": {}
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
        "jump_url": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
    }
    

##  Create futures-combo bot🔒 Authenticated

POST`/bot/futures-combo/create`

POST `/bot/futures-combo/create`

_Create futures-combo bot_

Typed AIHub adapter; authenticated owner comes only from trusted gateway context.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
X-Gate-Service-Id | header | string | Optional | Call source identifier; injected by APIv4 if necessary  
X-Gate-AppLang | header | string | Optional | Language context, such as `zh-CN` / `en-US`  
X-Request-Id | header | string | Optional | Request link ID; caller can transmit transparently  
X-Trace-Id | header | string | Optional | trace header; can be generated uniformly by APIv4  
body | body | AIHubFuturesComboCreateRequest | Required | none  
» strategy_type | body | string | Required | none  
» create_params | body | AIHubFuturesComboCreateParams | Required | Creation parameters for a futures-combo strategy.  
»» begin_money_amount | body | string | Required | none  
»» begin_money_currency | body | string | Required | none  
»» asset_info | body | array | Required | [One contract member of a futures-combo strategy.]  
»»» _None_ | body | AIHubFuturesComboAsset | Optional | One contract member of a futures-combo strategy.  
»»»» market | body | string | Required | none  
»»»» side | body | string | Required | none  
»»»» rate | body | string | Required | Ratio 0.01–1 in increments of 0.01; all member weights sum to 1.  
»»» leverage | body | integer | Required | none  
»»» period | body | string | Optional | none  
»»» threshold | body | string | Optional | Ratio 0.01–0.50; exclusive with period.  
»»» stop_profit | body | string|null | Optional | none  
»»» stop_loss | body | string|null | Optional | none  
»»» _None_ | body | object | Optional | none  
»»»» _None_ | body | object | Optional | none  
»»» _None_ | body | object | Optional | none  
»»»» _None_ | body | object | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» strategy_type | futures_combo  
»» begin_money_currency | USDT  
»»»» side | buy  
»»»» side | sell  
»»» period | 30m  
»»» period | 1h  
»»» period | 4h  
»»» period | 8h  
»»» period | 12h  
»»» period | 1d  
»»» period | 3d  
»»» period | 7d  
»»» period | 14d  
»»» period | 28d  
  
### Responses

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
»» status | string | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
»» jump_url | string | none  
»» operation_status | string | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
»» recovery_required | boolean | none  
» trace_id | string | none  
» label | string | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
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
    
    url = '/bot/futures-combo/create'
    query_param = ''
    body='{"strategy_type":"futures_combo","create_params":{}}'
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
    url="/bot/futures-combo/create"
    query_param=""
    body_param='{"strategy_type":"futures_combo","create_params":{}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "strategy_type": "futures_combo",
      "create_params": {}
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
        "jump_url": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
    }
    

#  Schemas

##  AIHubFuturesComboCreateRequest

_Request body for creating a futures-combo strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_type | string | Required | none | none  
create_params | AIHubFuturesComboCreateParams | Required | none | Creation parameters for a futures-combo strategy.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | futures_combo  
      
    
    {
      "strategy_type": "futures_combo",
      "create_params": {}
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
    
    

##  InfiniteGridCreateRequest

_Create the request body for the infinite grid policy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_type | string | Required | none | none  
market | string | Required | none | none  
create_params | InfiniteGridCreateParams | Required | none | Infinite grid creation parameters.  
Aligned with the app: **`money`** , **`price_floor`** , and **`profit_per_grid`** are required;  
`grid_num` and `price_type` are optional (defaults applied server-side when omitted).  
  
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
    
    

##  AIHubPortfolioRunningSuccessResponse

_The response body when querying the running policy list is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubPortfolioRunningData | Optional | none | Running policy list data.  
trace_id | string | Optional | none | none  
label | string | Optional | none | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
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
      "trace_id": "string",
      "label": "string"
    }
    
    

##  AIHubDiscoverSuccessResponse

_Get the response body when the strategy recommendation is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubDiscoverData | Optional | none | Strategy recommendation result data.  
trace_id | string | Optional | none | none  
label | string | Optional | none | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
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
      "trace_id": "string",
      "label": "string"
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
    
    

##  AIHubCreateSuccessResponse

_The response body when the creation strategy is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubCreateData | Optional | none | Policy information returned after the policy is successfully created.  
trace_id | string | Optional | none | none  
label | string | Optional | none | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "market": "string",
        "status": "string",
        "jump_url": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
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
        "profit_sharing_ratio": "string",
        "stop_loss_price_type": "last"
      }
    }
    
    

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
    
    

##  AIHubPortfolioDetailSuccessResponse

_The response body when querying policy details is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubPortfolioDetailData | Optional | none | Policy details data.  
trace_id | string | Optional | none | none  
label | string | Optional | none | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
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
        "stop_supported": true,
        "assets": [
          "string"
        ],
        "markets": [
          "string"
        ],
        "positions": [
          {}
        ],
        "positions_status": "verified",
        "configuration": {},
        "stop_progress": {
          "trading_finished": true,
          "funds_returned": true,
          "refund_amount": "string",
          "refund_currency": "string",
          "account_released": true
        }
      },
      "trace_id": "string",
      "label": "string"
    }
    
    

##  InfiniteGridCreateParams

_Infinite grid creation parameters. Aligned with the app:**`money`** , **`price_floor`** , and **`profit_per_grid`** are required; `grid_num` and `price_type` are optional (defaults applied server-side when omitted)._

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
    
    

##  AIHubFuturesComboCreateParams

_Creation parameters for a futures-combo strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
begin_money_amount | string | Required | none | none  
begin_money_currency | string | Required | none | none  
asset_info | [AIHubFuturesComboAsset] | Required | none | [One contract member of a futures-combo strategy.]  
leverage | integer | Required | none | none  
period | string | Optional | none | none  
threshold | string | Optional | none | Ratio 0.01–0.50; exclusive with period.  
stop_profit | string|null | Optional | none | none  
stop_loss | string|null | Optional | none | none  
  
_oneOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
  
_not_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
» _None_ | object | Optional | none | none  
  
_xor_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
  
_not_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
» _None_ | object | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
begin_money_currency | USDT  
period | 30m  
period | 1h  
period | 4h  
period | 8h  
period | 12h  
period | 1d  
period | 3d  
period | 7d  
period | 14d  
period | 28d  
      
    
    {}
    
    

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
    
    

##  ContractMartingaleCreateParams

_The creation parameters of the contract Martin strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
invest_amount | string | Required | none | Total strategy budget, not first-order margin. The server uses the complete existing ladder formula, owner fee and live contract facts, quantizes quantity down and rechecks before allocation. Minimum infeasible budget is rejected.  
price_deviation | string | Required | none | none  
max_orders | integer(int32) | Required | none | Maximum additional entries, excluding the first; preserve this legacy meaning.  
take_profit_ratio | string | Required | none | none  
direction | ContractMartingaleDirection | Required | none | The direction enumeration supported by the contract Martin strategy is consistent with the original interface of the App.  
leverage | string | Required | none | none  
stop_loss_price | string | Optional | none | Positive fixed stop price; requires explicit stop_loss_price_type. Missing both leaves the old no-fixed-stop request unchanged.  
profit_sharing_ratio | string | Optional | none | none  
stop_loss_price_type | string | Optional | none | none  
  
_oneOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | any | Optional | none | none  
  
_not_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
» _None_ | any | Optional | none | none  
  
_anyOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
»» _None_ | object | Optional | none | none  
  
_or_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
»» _None_ | object | Optional | none | none  
  
_xor_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
» _None_ | object | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
stop_loss_price_type | last  
stop_loss_price_type | index  
stop_loss_price_type | mark  
      
    
    {
      "invest_amount": "string",
      "price_deviation": "string",
      "max_orders": 1,
      "take_profit_ratio": "string",
      "direction": "buy",
      "leverage": "string",
      "stop_loss_price": "string",
      "profit_sharing_ratio": "string",
      "stop_loss_price_type": "last"
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
          "created_at": "string",
          "assets": [],
          "markets": []
        }
      ],
      "page": 0,
      "page_size": 0,
      "total": 0
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
    
    

##  AIHubPortfolioDetailData

_Policy details data._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Required | none | none  
strategy_type | StrategyType | Required | none | The complete enumeration of policy types supported by AIHub.  
market | string | Required | none | Single market, or empty string for a portfolio; use assets/markets for the latter.  
status | string | Required | none | none  
base_info | AIHubPortfolioBaseInfo | Required | none | Strategy detail base info.  
metrics | AIHubPortfolioMetrics | Required | none | Strategy detail metrics; fields returned depend on strategy type.  
position | AIHubPortfolioPosition | Optional | none | Strategy detail position info; fields returned depend on strategy type.  
stop_supported | boolean | Required | none | none  
assets | array | Optional | none | none  
markets | array | Optional | none | none  
positions | [AIHubPortfolioAssetPosition] | Optional | none | [Position information for one asset or market in a portfolio strategy.]  
positions_status | string | Optional | none | none  
configuration | object | Optional | none | Product-specific saved configuration. spot_martingale exposes AIHubSpotMartingaleConfiguration; absence is unverified. Runtime recovery internals are excluded.  
stop_progress | AIHubStopProgress | Optional | none | Read-only projection of durable facts. Absent values are unverified. Final refund excludes ordinary decrease-principal transfers. Account release is never inferred from stopped status or an empty account.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
positions_status | verified  
positions_status | partial  
positions_status | unverified  
positions_status | historical  
      
    
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
      "stop_supported": true,
      "assets": [
        "string"
      ],
      "markets": [
        "string"
      ],
      "positions": [
        {
          "asset": "string",
          "market": "string",
          "side": "string",
          "amount": "string",
          "amount_unit": "string",
          "entry_price": "string",
          "position_value": "string",
          "position_value_unit": "string",
          "target_weight": "string",
          "leverage": "string"
        }
      ],
      "positions_status": "verified",
      "configuration": {},
      "stop_progress": {
        "trading_finished": true,
        "funds_returned": true,
        "refund_amount": "string",
        "refund_currency": "string",
        "account_released": true
      }
    }
    
    

##  AIHubPortfolioStopRequest

_Single owner-scoped stop. Existing six-type ID/type requests retain default exits. smart_position requires explicit mode, limit requires options; futures_combo uses fixed whole-portfolio close/settlement._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Required | none | none  
strategy_type | StrategyType | Required | none | The complete enumeration of policy types supported by AIHub.  
stop_mode | string | Optional | none | Required only for smart_position. Other types reject custom exit options.  
stop_options | AIHubRebalanceStopOptions | Optional | none | Options for the limit stop mode of a smart-position strategy.  
  
_oneOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
» strategy_type | any | Optional | none | none  
  
_not_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
»» _None_ | string | Optional | none | none  
  
_not_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
» _None_ | any | Optional | none | none  
  
_anyOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
»» _None_ | object | Optional | none | none  
  
_or_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
»» _None_ | object | Optional | none | none  
  
_xor_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
» _None_ | object | Optional | none | none  
»» strategy_type | string | Optional | none | none  
»» stop_mode | any | Required | none | none  
  
_not_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
»» _None_ | object | Optional | none | none  
  
_xor_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
» _None_ | object | Optional | none | none  
»» strategy_type | string | Optional | none | none  
»» stop_mode | string | Required | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
stop_mode | market  
stop_mode | limit  
stop_mode | no_close  
_None_ | smart_position  
strategy_type | smart_position  
stop_mode | market  
stop_mode | no_close  
strategy_type | smart_position  
stop_mode | limit  
      
    
    {
      "strategy_id": "string",
      "strategy_type": null,
      "stop_mode": "market",
      "stop_options": {
        "price": "string",
        "expiration": 1,
        "slip": "string"
      }
    }
    
    

##  AIHubPortfolioStopSuccessResponse

_The response body when the termination strategy is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer(int32) | Required | none | none  
message | string | Required | none | none  
data | AIHubPortfolioStopData | Optional | none | The result information returned after the termination strategy is successful.  
trace_id | string | Optional | none | none  
label | string | Optional | none | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
    {
      "code": 200,
      "message": "success",
      "data": {
        "strategy_id": "string",
        "strategy_type": "spot_grid",
        "status": "string",
        "result_message": "string",
        "operation_status": "string",
        "recovery_required": true
      },
      "trace_id": "string",
      "label": "string"
    }
    
    

##  AIHubRebalanceCreateRequest

_Request body for creating a smart-position strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_type | string | Required | none | none  
create_params | AIHubRebalanceCreateParams | Required | none | Creation parameters for a smart-position strategy.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
strategy_type | smart_position  
      
    
    {
      "strategy_type": "smart_position",
      "create_params": {}
    }
    
    

##  AIHubContractMartingaleConfiguration

_AIHub-supported persisted contract settings. This is not a complete advanced native configuration._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
invest_amount | string | Optional | none | none  
investment_currency | string | Optional | none | none  
price_deviation | string | Optional | none | none  
take_profit_ratio | string | Optional | none | none  
direction | string | Optional | none | none  
first_order_size | string | Optional | none | Exact decimal contract quantity from the product snapshot; empty remains unverified, never inferred from the total budget.  
max_orders | integer(int64) | Optional | none | Maximum additional entries excluding the first.  
leverage | integer(int32) | Optional | none | none  
stop_loss_price_rule | AIHubMartingalePriceRule | Optional | none | Persisted price rule only, not proof that an order executed. Unknown price basis or non-positive price is not effective protection.  
      
    
    {
      "invest_amount": "string",
      "investment_currency": "string",
      "price_deviation": "string",
      "take_profit_ratio": "string",
      "direction": "string",
      "first_order_size": "string",
      "max_orders": 0,
      "leverage": 0,
      "stop_loss_price_rule": {
        "price": "string",
        "price_type": "string",
        "is_gte": true
      }
    }
    
    

##  AIHubStopProgress

_Read-only projection of durable facts. Absent values are unverified. Final refund excludes ordinary decrease-principal transfers. Account release is never inferred from stopped status or an empty account._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
trading_finished | boolean | Optional | none | none  
funds_returned | boolean | Optional | none | none  
refund_amount | string | Optional | none | none  
refund_currency | string | Optional | none | none  
account_released | boolean | Optional | none | none  
      
    
    {
      "trading_finished": true,
      "funds_returned": true,
      "refund_amount": "string",
      "refund_currency": "string",
      "account_released": true
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
    
    

##  AIHubFuturesComboAsset

_One contract member of a futures-combo strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
market | string | Required | none | none  
side | string | Required | none | none  
rate | string | Required | none | Ratio 0.01–1 in increments of 0.01; all member weights sum to 1.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
side | buy  
side | sell  
      
    
    {
      "market": "string",
      "side": "buy",
      "rate": "string"
    }
    
    

##  AIHubPortfolioRunningItem

_A single record in the list of running policies._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Required | none | none  
strategy_type | StrategyType | Required | none | The complete enumeration of policy types supported by AIHub.  
strategy_name | string | Required | none | none  
market | string | Required | none | Single market, or empty string for a portfolio; use assets/markets for the latter.  
status | string | Required | none | none  
pnl | string | Optional | none | none  
pnl_rate | string | Optional | none | none  
invest_amount | string | Optional | none | none  
created_at | string | Optional | none | Created time  
assets | array | Optional | none | none  
markets | array | Optional | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "strategy_name": "string",
      "market": "string",
      "status": "string",
      "pnl": "string",
      "pnl_rate": "string",
      "invest_amount": "string",
      "created_at": "string",
      "assets": [
        "string"
      ],
      "markets": [
        "string"
      ]
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
    
    

##  AIHubCreateData

_Policy information returned after the policy is successfully created._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Optional | none | none  
strategy_type | StrategyType | Optional | none | The complete enumeration of policy types supported by AIHub.  
market | string | Optional | none | none  
status | string | Optional | none | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional | none | none  
operation_status | string | Optional | none | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "market": "string",
      "status": "string",
      "jump_url": "string",
      "operation_status": "string",
      "recovery_required": true
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
    
    

##  AIHubPortfolioStopData

_The result information returned after the termination strategy is successful._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
strategy_id | string | Optional | none | none  
strategy_type | StrategyType | Optional | none | The complete enumeration of policy types supported by AIHub.  
status | string | Optional | none | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
result_message | string | Optional | none | none  
operation_status | string | Optional | none | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "status": "string",
      "result_message": "string",
      "operation_status": "string",
      "recovery_required": true
    }
    
    

##  AIHubRebalanceCreateParams

_Creation parameters for a smart-position strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
begin_money_amount | string | Required | none | none  
begin_money_currency | string | Required | none | none  
asset_info | [AIHubRebalanceAsset] | Required | none | [One asset and its target weight in a smart-position strategy.]  
period | string | Optional | none | Product interval between 1m and 28d.  
threshold | string | Optional | none | Positive ratio below 1, at most four decimal places.  
close_flag | integer | Optional | none | none  
is_use_base | boolean | Optional | none | none  
stop_profit | string | Optional | none | none  
stop_loss | string | Optional | none | none  
  
_oneOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
  
_not_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
» _None_ | object | Optional | none | none  
  
_xor_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
  
_not_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
» _None_ | object | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
begin_money_currency | USDT  
close_flag | 0  
close_flag | 1  
      
    
    {}
    
    

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
_None_ | smart_position  
_None_ | futures_combo  
      
    
    "spot_grid"
    
    

##  AIHubMartingalePriceRule

_Persisted price rule only, not proof that an order executed. Unknown price basis or non-positive price is not effective protection._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
price | string | Optional | none | none  
price_type | string | Optional | none | Original enum name (last/index/mark/unknown), or its numeric string for an unknown future enum.  
is_gte | boolean | Optional | none | none  
      
    
    {
      "price": "string",
      "price_type": "string",
      "is_gte": true
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
    
    

##  AIHubSpotMartingaleConfiguration

_Saved settings supported by AIHub, not a substitute for all advanced native configuration. Absent upstream params are unverified._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
invest_amount | string | Optional | none | none  
investment_currency | string | Optional | none | none  
price_deviation | string | Optional | none | none  
take_profit_ratio | string | Optional | none | none  
stop_loss_per_cycle | string | Optional | none | Saved per-cycle ratio, returned unchanged. Zero or negative legacy values do not constitute effective protection.  
trigger_price | string | Optional | none | none  
max_orders | integer(int32) | Optional | none | Saved maximum additional entries excluding the first; not total orders.  
      
    
    {
      "invest_amount": "string",
      "investment_currency": "string",
      "price_deviation": "string",
      "take_profit_ratio": "string",
      "stop_loss_per_cycle": "string",
      "trigger_price": "string",
      "max_orders": 0
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
    
    

##  AIHubRebalanceStopOptions

_Options for the limit stop mode of a smart-position strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
price | string | Required | none | One product-supported price expression; not one expression per member.  
expiration | integer(int64) | Required | none | Seconds of validity. Expiry cancels and returns assets; never switches to market.  
slip | string | Optional | none | Optional ratio 0.001–0.05, precision at most six.  
      
    
    {
      "price": "string",
      "expiration": 1,
      "slip": "string"
    }
    
    

##  AIHubPortfolioAssetPosition

_Position information for one asset or market in a portfolio strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
asset | string | Optional | none | none  
market | string | Optional | none | none  
side | string | Optional | none | none  
amount | string | Optional | none | none  
amount_unit | string | Optional | none | none  
entry_price | string | Optional | none | none  
position_value | string | Optional | none | none  
position_value_unit | string | Optional | none | none  
target_weight | string | Optional | none | none  
leverage | string | Optional | none | none  
      
    
    {
      "asset": "string",
      "market": "string",
      "side": "string",
      "amount": "string",
      "amount_unit": "string",
      "entry_price": "string",
      "position_value": "string",
      "position_value_unit": "string",
      "target_weight": "string",
      "leverage": "string"
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
    
    

##  AIHubRebalanceAsset

_One asset and its target weight in a smart-position strategy._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
asset | string | Required | none | none  
rate | string | Required | none | Two decimal places, minimum 0.01; unique assets and sum exactly 1.  
      
    
    {
      "asset": "string",
      "rate": "string"
    }