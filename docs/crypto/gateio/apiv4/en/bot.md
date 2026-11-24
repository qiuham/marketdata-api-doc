---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/bot
api_type: REST
updated_at: 2026-11-24 18:56:11.011421
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
exclude_recommendation_id | query | string | Optional | Refresh-only previous returned identity: type|market|backtest_id, with an optional stable parameter discriminator for colliding source IDs. Ambiguous old identities are rejected; metric-only changes do not produce a new plan.  
  
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

Get the response body when the strategy recommendation is successful.

Type | Constraints  
---|---  
AIHubDiscoverSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubDiscoverData | Optional | required: ["scene","recommendations","unsupported_filters"] | Strategy recommendation result data.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Strategy recommendation result data.

Type | Constraints  
---|---  
AIHubDiscoverData | required: ["scene","recommendations","unsupported_filters"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
scene | DiscoverScene | Required | enum: ["top1","bundle","filter","refresh"] | Enumeration of scenarios supported by the policy recommendation interface.  
recommendations | array | Required |  |   
unsupported_filters | array | Required |  | Filter conditions not supported in this issue  
  
**data / recommendations**

Type | Constraints  
---|---  
array |   
  
**data / recommendations / items**

A single piece of strategy recommendation information.

Type | Constraints  
---|---  
AIHubRecommendation | required: ["recommendation_id","market","strategy_type","strategy_name","summary"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
recommendation_id | string | Required |  |   
market | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
strategy_name | string | Required |  |   
backtest_apr | string | Optional |  |   
max_drawdown | string | Optional |  |   
summary | string | Required |  |   
strategy_params_preview | string | Optional |  | Recommended-parameter preview as JSON text (string-encoded so clients deserialize it consistently). The value is a serialized JSON object whose structure varies by strategy type; callers or upper-layer models must parse it.  
  
**data / unsupported_filters**

Filter conditions not supported in this issue

Type | Constraints  
---|---  
array |   
  
**data / unsupported_filters / items**

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
strategy_type | body | string | Required | none  
market | body | string | Required | none  
create_params | body | SpotGridCreateParams | Required | Creation parameters for the spot grid strategy.  
» money | body | string | Required | Amount of investment  
» low_price | body | string | Required | Range lower limit  
» high_price | body | string | Required | Range upper limit  
» grid_num | body | integer(int32) | Required | Number of grids  
» price_type | body | integer(int32) | Required | none  
» trigger_price | body | string | Optional | none  
» stop_profit | body | string | Optional | none  
» stop_loss | body | string | Optional | none  
» profit_sharing_ratio | body | string | Optional | none  
» is_use_base | body | boolean | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | spot_grid  
» price_type | 0  
» price_type | 1  
  
####  Request Body Schema

Create the request body for the spot grid policy.

Request Body SchemaType | Constraints  
---|---  
SpotGridCreateRequest | required: ["strategy_type","market","create_params"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["spot_grid"] |   
market | string | Required |  |   
create_params | SpotGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type"] | Creation parameters for the spot grid strategy.  
  
**create_params**

Creation parameters for the spot grid strategy.

Request Body SchemaType | Constraints  
---|---  
SpotGridCreateParams | required: ["money","low_price","high_price","grid_num","price_type"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  | Amount of investment  
low_price | string | Required |  | Range lower limit  
high_price | string | Required |  | Range upper limit  
grid_num | integer(int32) | Required | minimum: 1 | Number of grids  
price_type | integer(int32) | Required | enum: [0,1] |   
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

The response body when the creation strategy is successful.

Type | Constraints  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | Policy information returned after the policy is successfully created.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Policy information returned after the policy is successfully created.

Type | Constraints  
---|---  
AIHubCreateData |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Optional |  |   
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
  
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
strategy_type | body | string | Required | none  
market | body | string | Required | none  
create_params | body | MarginGridCreateParams | Required | Creation parameters for the Leverage Grid strategy.  
» money | body | string | Required | none  
» low_price | body | string | Required | none  
» high_price | body | string | Required | none  
» grid_num | body | integer(int32) | Required | none  
» price_type | body | integer(int32) | Required | none  
» leverage | body | string | Required | none  
» direction | body | FuturesDirection | Optional | Direction enumeration supported by contract-based strategies.  
» trigger_price | body | string | Optional | none  
» stop_profit | body | string | Optional | none  
» stop_loss | body | string | Optional | none  
» profit_sharing_ratio | body | string | Optional | none  
» is_use_base | body | boolean | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | margin_grid  
» price_type | 0  
» price_type | 1  
  
####  Request Body Schema

Create the request body for the Leverage Grid strategy.

Request Body SchemaType | Constraints  
---|---  
MarginGridCreateRequest | required: ["strategy_type","market","create_params"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["margin_grid"] |   
market | string | Required |  |   
create_params | MarginGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type","leverage"] | Creation parameters for the Leverage Grid strategy.  
  
**create_params**

Creation parameters for the Leverage Grid strategy.

Request Body SchemaType | Constraints  
---|---  
MarginGridCreateParams | required: ["money","low_price","high_price","grid_num","price_type","leverage"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  |   
low_price | string | Required |  |   
high_price | string | Required |  |   
grid_num | integer(int32) | Required | minimum: 1 |   
price_type | integer(int32) | Required | enum: [0,1] |   
leverage | string | Required |  |   
direction | FuturesDirection | Optional | enum: ["long","short","neutral"] | Direction enumeration supported by contract-based strategies.  
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

The response body when the creation strategy is successful.

Type | Constraints  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | Policy information returned after the policy is successfully created.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Policy information returned after the policy is successfully created.

Type | Constraints  
---|---  
AIHubCreateData |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Optional |  |   
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
  
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
strategy_type | body | string | Required | none  
market | body | string | Required | none  
create_params | body | InfiniteGridCreateParams | Required | Infinite grid creation parameters.  
Aligned with the app: **`money`** , **`price_floor`** , and **`profit_per_grid`** are required;  
`grid_num` and `price_type` are optional (defaults applied server-side when omitted).  
» money | body | string | Required | none  
» price_floor | body | string | Required | price floor  
» profit_per_grid | body | string | Required | Profit per square  
» grid_num | body | integer(int32) | Optional | Optional; may be omitted like in the app.  
» price_type | body | integer(int32) | Optional | Optional. `0` arithmetic grid; `1` geometric; omit for server defaults.  
» trigger_price | body | string | Optional | none  
» stop_profit | body | string | Optional | none  
» stop_loss | body | string | Optional | none  
» profit_sharing_ratio | body | string | Optional | none  
» is_use_base | body | boolean | Optional | none  
  
####  Detailed descriptions

** create_params**: Infinite grid creation parameters.  
Aligned with the app: **`money`** , **`price_floor`** , and **`profit_per_grid`** are required;  
`grid_num` and `price_type` are optional (defaults applied server-side when omitted).

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | infinite_grid  
» price_type | 0  
» price_type | 1  
  
####  Request Body Schema

Create the request body for the infinite grid policy.

Request Body SchemaType | Constraints  
---|---  
InfiniteGridCreateRequest | required: ["strategy_type","market","create_params"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["infinite_grid"] |   
market | string | Required |  |   
create_params | InfiniteGridCreateParams | Required | required: ["money","price_floor","profit_per_grid"] | Infinite grid creation parameters.  
Aligned with the app: **`money`** , **`price_floor`** , and **`profit_per_grid`** are required;  
`grid_num` and `price_type` are optional (defaults applied server-side when omitted).  
  
**create_params**

Infinite grid creation parameters. Aligned with the app: **`money`** , **`price_floor`** , and **`profit_per_grid`** are required; `grid_num` and `price_type` are optional (defaults applied server-side when omitted).

Request Body SchemaType | Constraints  
---|---  
InfiniteGridCreateParams | required: ["money","price_floor","profit_per_grid"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  |   
price_floor | string | Required |  | price floor  
profit_per_grid | string | Required |  | Profit per square  
grid_num | integer(int32) | Optional | minimum: 1 | Optional; may be omitted like in the app.  
price_type | integer(int32) | Optional | enum: [0,1] | Optional. `0` arithmetic grid; `1` geometric; omit for server defaults.  
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

The response body when the creation strategy is successful.

Type | Constraints  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | Policy information returned after the policy is successfully created.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Policy information returned after the policy is successfully created.

Type | Constraints  
---|---  
AIHubCreateData |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Optional |  |   
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
  
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
strategy_type | body | string | Required | none  
market | body | string | Required | none  
create_params | body | FuturesGridCreateParams | Required | Creation parameters for the contract grid strategy.  
» money | body | string | Required | none  
» low_price | body | string | Required | none  
» high_price | body | string | Required | none  
» grid_num | body | integer(int32) | Required | none  
» price_type | body | integer(int32) | Required | none  
» leverage | body | string | Required | none  
» direction | body | FuturesDirection | Optional | Direction enumeration supported by contract-based strategies.  
» trigger_price | body | string | Optional | none  
» stop_profit | body | string | Optional | none  
» stop_loss | body | string | Optional | none  
» profit_sharing_ratio | body | string | Optional | none  
» is_use_base | body | boolean | Optional | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | futures_grid  
» price_type | 0  
» price_type | 1  
  
####  Request Body Schema

Create the request body of the contract grid strategy.

Request Body SchemaType | Constraints  
---|---  
FuturesGridCreateRequest | required: ["strategy_type","market","create_params"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["futures_grid"] |   
market | string | Required |  |   
create_params | FuturesGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type","leverage"] | Creation parameters for the contract grid strategy.  
  
**create_params**

Creation parameters for the contract grid strategy.

Request Body SchemaType | Constraints  
---|---  
FuturesGridCreateParams | required: ["money","low_price","high_price","grid_num","price_type","leverage"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  |   
low_price | string | Required |  |   
high_price | string | Required |  |   
grid_num | integer(int32) | Required | minimum: 1 |   
price_type | integer(int32) | Required | enum: [0,1] |   
leverage | string | Required |  |   
direction | FuturesDirection | Optional | enum: ["long","short","neutral"] | Direction enumeration supported by contract-based strategies.  
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

The response body when the creation strategy is successful.

Type | Constraints  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | Policy information returned after the policy is successfully created.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Policy information returned after the policy is successfully created.

Type | Constraints  
---|---  
AIHubCreateData |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Optional |  |   
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
  
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
strategy_type | body | string | Required | none  
market | body | string | Required | none  
create_params | body | SpotMartingaleCreateParams | Required | Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).  
\- **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.  
\- Optional **`trigger_price`** : trigger price.  
\- If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).  
» invest_amount | body | string | Required | none  
» price_deviation | body | string | Required | Add-position deviation ratio as a decimal string (e.g. a 2% drop is `0.02`).  
» max_orders | body | integer(int32) | Required | none  
» take_profit_ratio | body | string | Required | Take-profit ratio per round as a decimal string.  
» stop_loss_per_cycle | body | string | Optional | Stop-loss ratio per round as a decimal string; optional; aligned with app `stop_loss_per_cycle`.  
» trigger_price | body | string | Optional | Trigger price; optional.  
» profit_sharing_ratio | body | string | Optional | none  
  
####  Detailed descriptions

** create_params**: Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).  
\- **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.  
\- Optional **`trigger_price`** : trigger price.  
\- If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | spot_martingale  
  
####  Request Body Schema

Create the request body of the Spot Martin strategy.

Request Body SchemaType | Constraints  
---|---  
SpotMartingaleCreateRequest | required: ["strategy_type","market","create_params"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["spot_martingale"] |   
market | string | Required |  |   
create_params | SpotMartingaleCreateParams | Required | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio"] | Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).  
\- **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.  
\- Optional **`trigger_price`** : trigger price.  
\- If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).  
  
**create_params**

Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).

  * **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.
  * Optional **`trigger_price`** : trigger price.
  * If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).

Request Body SchemaType | Constraints  
---|---  
SpotMartingaleCreateParams | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
invest_amount | string | Required |  |   
price_deviation | string | Required |  | Add-position deviation ratio as a decimal string (e.g. a 2% drop is `0.02`).  
max_orders | integer(int32) | Required | minimum: 1 |   
take_profit_ratio | string | Required |  | Take-profit ratio per round as a decimal string.  
stop_loss_per_cycle | string | Optional |  | Stop-loss ratio per round as a decimal string; optional; aligned with app `stop_loss_per_cycle`.  
trigger_price | string | Optional |  | Trigger price; optional.  
profit_sharing_ratio | string | Optional |  |   
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

The response body when the creation strategy is successful.

Type | Constraints  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | Policy information returned after the policy is successfully created.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Policy information returned after the policy is successfully created.

Type | Constraints  
---|---  
AIHubCreateData |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Optional |  |   
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
  
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
strategy_type | body | string | Required | none  
market | body | string | Required | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | contract_martingale  
  
####  Request Body Schema

Create the request body of the contract Martin strategy.

Request Body SchemaType | Constraints  
---|---  
ContractMartingaleCreateRequest | required: ["strategy_type","market","create_params"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["contract_martingale"] |   
market | string | Required |  |   
create_params | ContractMartingaleCreateParams | Required | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio","direction","leverage"] | The creation parameters of the contract Martin strategy.  
  
**create_params**

The creation parameters of the contract Martin strategy.

Request Body SchemaType | Constraints  
---|---  
ContractMartingaleCreateParams | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio","direction","leverage"]  
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
invest_amount | string | true |  | Total strategy budget, not first-order margin. The server uses the complete existing ladder formula, owner fee and live contract facts, quantizes quantity down and rechecks before allocation. Minimum infeasible budget is rejected.  
price_deviation | string | true |  |   
max_orders | integer(int32) | true | minimum: 1 | Maximum additional entries, excluding the first; preserve this legacy meaning.  
take_profit_ratio | string | true |  |   
direction | ContractMartingaleDirection | true | enum: ["buy","sell"] | The direction enumeration supported by the contract Martin strategy is consistent with the original interface of the App.  
leverage | string | true |  |   
stop_loss_price | string | false |  | Positive fixed stop price; requires explicit stop_loss_price_type. Missing both leaves the old no-fixed-stop request unchanged.  
profit_sharing_ratio | string | false |  |   
stop_loss_price_type | string | false | enum: ["last","index","mark"] |   
  
**create_params / allOf[0]**

Request Body SchemaType | Constraints  
---|---  
oneOf |   
  
**create_params / allOf[0] / oneOf[0]**

Request Body SchemaType | Constraints  
---|---  
not |   
  
**create_params / allOf[0] / oneOf[0] / not**

Request Body SchemaType | Constraints  
---|---  
anyOf |   
  
**create_params / allOf[0] / oneOf[0] / not / anyOf[0]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["stop_loss_price"]  
  
**create_params / allOf[0] / oneOf[0] / not / anyOf[1]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["stop_loss_price_type"]  
  
**create_params / allOf[0] / oneOf[1]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["stop_loss_price","stop_loss_price_type"]  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

The response body when the creation strategy is successful.

Type | Constraints  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | Policy information returned after the policy is successfully created.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Policy information returned after the policy is successfully created.

Type | Constraints  
---|---  
AIHubCreateData |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Optional |  |   
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
  
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

The response body when querying the running policy list is successful.

Type | Constraints  
---|---  
AIHubPortfolioRunningSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioRunningData | Optional | required: ["items","page","page_size","total"] | Running policy list data.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Running policy list data.

Type | Constraints  
---|---  
AIHubPortfolioRunningData | required: ["items","page","page_size","total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
items | array | Required |  |   
page | integer(int32) | Required |  |   
page_size | integer(int32) | Required |  |   
total | integer(int32) | Required |  |   
  
**data / items**

Type | Constraints  
---|---  
array |   
  
**data / items / items**

A single record in the list of running policies.

Type | Constraints  
---|---  
AIHubPortfolioRunningItem | required: ["strategy_id","strategy_type","strategy_name","market","status"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
strategy_name | string | Required |  |   
market | string | Required |  | Single market, or empty string for a portfolio; use assets/markets for the latter.  
status | string | Required |  |   
pnl | string | Optional |  |   
pnl_rate | string | Optional |  |   
invest_amount | string | Optional |  |   
created_at | string | Optional |  | Created time  
assets | array | Optional |  |   
markets | array | Optional |  |   
  
**data / items / items / assets**

Type | Constraints  
---|---  
array |   
  
**data / items / items / assets / items**

Type | Constraints  
---|---  
string |   
  
**data / items / items / markets**

Type | Constraints  
---|---  
array |   
  
**data / items / items / markets / items**

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

The response body when querying policy details is successful.

Type | Constraints  
---|---  
AIHubPortfolioDetailSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioDetailData | Optional | required: ["strategy_id","strategy_type","market","status","base_info","metrics","stop_supported"] | Policy details data.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Policy details data.

Type | Constraints  
---|---  
AIHubPortfolioDetailData | required: ["strategy_id","strategy_type","market","status","base_info","metrics","stop_supported"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Required |  | Single market, or empty string for a portfolio; use assets/markets for the latter.  
status | string | Required |  |   
base_info | AIHubPortfolioBaseInfo | Required | required: ["strategy_name","created_at","running_duration","invest_amount","total_profit","profit_rate"] | Strategy detail base info.  
metrics | AIHubPortfolioMetrics | Required |  | Strategy detail metrics; fields returned depend on strategy type.  
position | AIHubPortfolioPosition|null | Optional | nullable: true | Strategy detail position info; fields returned depend on strategy type.  
stop_supported | boolean | Required |  |   
assets | array | Optional |  |   
markets | array | Optional |  |   
positions | array | Optional |  |   
positions_status | string | Optional | enum: ["verified","partial","unverified","historical"] |   
configuration | object | Optional |  | Product-specific saved configuration. spot_martingale exposes AIHubSpotMartingaleConfiguration; absence is unverified. Runtime recovery internals are excluded.  
stop_progress | AIHubStopProgress | Optional |  | Read-only projection of durable facts. Absent values are unverified. Final refund excludes ordinary decrease-principal transfers. Account release is never inferred from stopped status or an empty account.  
  
**data / base_info**

Strategy detail base info.

Type | Constraints  
---|---  
AIHubPortfolioBaseInfo | required: ["strategy_name","created_at","running_duration","invest_amount","total_profit","profit_rate"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_name | string | Required |  |   
created_at | string | Required |  | Created time  
running_duration | integer(int64) | Required |  | Runtime duration in seconds.  
invest_amount | string | Required |  |   
total_profit | string | Required |  |   
profit_rate | string | Required |  |   
  
**data / metrics**

Strategy detail metrics; fields returned depend on strategy type.

Type | Constraints  
---|---  
AIHubPortfolioMetrics |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
grid_profit | string | Optional |  |   
floating_pnl | string | Optional |  |   
arbitrage_count | integer(int64) | Optional |  |   
price_range | string | Optional |  |   
grid_count | integer(int64) | Optional |  |   
estimated_liquidation_price | string | Optional |  |   
price_floor | string | Optional |  |   
grid_profit_rate | string | Optional |  |   
realized_pnl | string | Optional |  |   
finished_rounds | integer(int64) | Optional |  |   
avg_cost | string | Optional |  |   
take_profit_price | string | Optional |  |   
maintenance_margin_ratio | string | Optional |  |   
  
**data / position**

Strategy detail position info; fields returned depend on strategy type.

Type | Constraints  
---|---  
AIHubPortfolioPosition|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
amount | string | Optional |  |   
entry_price | string | Optional |  |   
quote_amount | string | Optional |  |   
position_value | string | Optional |  |   
margin | string | Optional |  |   
side | string | Optional |  |   
  
**data / assets**

Type | Constraints  
---|---  
array |   
  
**data / assets / items**

Type | Constraints  
---|---  
string |   
  
**data / markets**

Type | Constraints  
---|---  
array |   
  
**data / markets / items**

Type | Constraints  
---|---  
string |   
  
**data / positions**

Type | Constraints  
---|---  
array |   
  
**data / positions / items**

Position information for one asset or market in a portfolio strategy.

Type | Constraints  
---|---  
AIHubPortfolioAssetPosition |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Optional |  |   
market | string | Optional |  |   
side | string | Optional |  |   
amount | string | Optional |  |   
amount_unit | string | Optional |  |   
entry_price | string | Optional |  |   
position_value | string | Optional |  |   
position_value_unit | string | Optional |  |   
target_weight | string | Optional |  |   
leverage | string | Optional |  |   
  
**data / stop_progress**

Read-only projection of durable facts. Absent values are unverified. Final refund excludes ordinary decrease-principal transfers. Account release is never inferred from stopped status or an empty account.

Type | Constraints  
---|---  
AIHubStopProgress |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trading_finished | boolean | Optional |  |   
funds_returned | boolean | Optional |  |   
refund_amount | string | Optional |  |   
refund_currency | string | Optional |  |   
account_released | boolean | Optional |  |   
  
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
  
####  Request Body Schema

Single owner-scoped stop. Existing six-type ID/type requests retain default exits. smart_position requires explicit mode, limit requires options; futures_combo uses fixed whole-portfolio close/settlement.

Request Body SchemaType | Constraints  
---|---  
AIHubPortfolioStopRequest | required: ["strategy_id","strategy_type"]  
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
strategy_id | string | true |  |   
strategy_type | StrategyType | true | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
stop_mode | string | false | enum: ["market","limit","no_close"] | Required only for smart_position. Other types reject custom exit options.  
stop_options | AIHubRebalanceStopOptions | false | required: ["price","expiration"]  
additionalProperties: false | Options for the limit stop mode of a smart-position strategy.  
  
**stop_options**

Options for the limit stop mode of a smart-position strategy.

Request Body SchemaType | Constraints  
---|---  
AIHubRebalanceStopOptions | required: ["price","expiration"]  
additionalProperties: false  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | One product-supported price expression; not one expression per member.  
expiration | integer(int64) | Required | minimum: 1 | Seconds of validity. Expiry cancels and returns assets; never switches to market.  
slip | string | Optional |  | Optional ratio 0.001–0.05, precision at most six.  
  
**allOf[0]**

Request Body SchemaType | Constraints  
---|---  
oneOf |   
  
**allOf[0] / oneOf[0]**

Request Body SchemaType | Constraints  
---|---  
object |   
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
strategy_type | not | true |  |   
  
**allOf[0] / oneOf[0] / strategy_type**

Request Body SchemaType | Constraints  
---|---  
not |   
  
**allOf[0] / oneOf[0] / strategy_type / not**

Request Body SchemaType | Constraints  
---|---  
string |   
  
**Enumerated Values**

Request Body SchemaValue  
---  
"smart_position"  
  
**allOf[0] / oneOf[0] / not**

Request Body SchemaType | Constraints  
---|---  
anyOf |   
  
**allOf[0] / oneOf[0] / not / anyOf[0]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["stop_mode"]  
  
**allOf[0] / oneOf[0] / not / anyOf[1]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["stop_options"]  
  
**allOf[0] / oneOf[1]**

Request Body SchemaType | Constraints  
---|---  
object | required: ["stop_mode"]  
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
strategy_type | string | true | enum: ["smart_position"] |   
stop_mode | string | true | enum: ["market","no_close"] |   
  
**allOf[0] / oneOf[1] / not**

Request Body SchemaType | Constraints  
---|---  
any | required: ["stop_options"]  
  
**allOf[0] / oneOf[2]**

Request Body SchemaType | Constraints  
---|---  
object | required: ["stop_mode","stop_options"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["smart_position"] |   
stop_mode | string | Required | enum: ["limit"] |   
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubPortfolioStopSuccessResponse  
  
### Response Schema

Status Code **200**

The response body when the termination strategy is successful.

Type | Constraints  
---|---  
AIHubPortfolioStopSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioStopData | Optional |  | The result information returned after the termination strategy is successful.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

The result information returned after the termination strategy is successful.

Type | Constraints  
---|---  
AIHubPortfolioStopData |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
result_message | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
  
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
strategy_type | body | string | Required | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | smart_position  
  
####  Request Body Schema

Request body for creating a smart-position strategy.

Request Body SchemaType | Constraints  
---|---  
AIHubRebalanceCreateRequest | required: ["strategy_type","create_params"]  
additionalProperties: false  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["smart_position"] |   
create_params | AIHubRebalanceCreateParams | Required | required: ["begin_money_amount","begin_money_currency","asset_info"]  
additionalProperties: false | Creation parameters for a smart-position strategy.  
  
**create_params**

Creation parameters for a smart-position strategy.

Request Body SchemaType | Constraints  
---|---  
AIHubRebalanceCreateParams | required: ["begin_money_amount","begin_money_currency","asset_info"]  
additionalProperties: false  
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
begin_money_amount | string | true |  |   
begin_money_currency | string | true | enum: ["USDT"] |   
asset_info | array | true | minItems: 2  
maxItems: 10 |   
period | string | false |  | Product interval between 1m and 28d.  
threshold | string | false |  | Positive ratio below 1, at most four decimal places.  
close_flag | integer | false | enum: [0,1]  
default: 1 |   
is_use_base | boolean | false |  |   
stop_profit | string | false |  |   
stop_loss | string | false |  |   
  
**create_params / asset_info**

Request Body SchemaType | Constraints  
---|---  
array | minItems: 2  
maxItems: 10  
  
**create_params / asset_info / items**

One asset and its target weight in a smart-position strategy.

Request Body SchemaType | Constraints  
---|---  
AIHubRebalanceAsset | required: ["asset","rate"]  
additionalProperties: false  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  |   
rate | string | Required |  | Two decimal places, minimum 0.01; unique assets and sum exactly 1.  
  
**create_params / oneOf[0]**

Request Body SchemaType | Constraints  
---|---  
not | required: ["period"]  
  
**create_params / oneOf[0] / not**

Request Body SchemaType | Constraints  
---|---  
any | required: ["threshold"]  
  
**create_params / oneOf[1]**

Request Body SchemaType | Constraints  
---|---  
not | required: ["threshold"]  
  
**create_params / oneOf[1] / not**

Request Body SchemaType | Constraints  
---|---  
any | required: ["period"]  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

The response body when the creation strategy is successful.

Type | Constraints  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | Policy information returned after the policy is successfully created.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Policy information returned after the policy is successfully created.

Type | Constraints  
---|---  
AIHubCreateData |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Optional |  |   
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
  
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
strategy_type | body | string | Required | none  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
strategy_type | futures_combo  
  
####  Request Body Schema

Request body for creating a futures-combo strategy.

Request Body SchemaType | Constraints  
---|---  
AIHubFuturesComboCreateRequest | required: ["strategy_type","create_params"]  
additionalProperties: false  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["futures_combo"] |   
create_params | AIHubFuturesComboCreateParams | Required | required: ["begin_money_amount","begin_money_currency","asset_info","leverage"]  
additionalProperties: false | Creation parameters for a futures-combo strategy.  
  
**create_params**

Creation parameters for a futures-combo strategy.

Request Body SchemaType | Constraints  
---|---  
AIHubFuturesComboCreateParams | required: ["begin_money_amount","begin_money_currency","asset_info","leverage"]  
additionalProperties: false  
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
begin_money_amount | string | true |  |   
begin_money_currency | string | true | enum: ["USDT"] |   
asset_info | array | true | minItems: 2  
maxItems: 10 |   
leverage | integer | true | minimum: 1  
maximum: 100 |   
period | string | false | enum: ["30m","1h","4h","8h","12h","1d","3d","7d","14d","28d"] |   
threshold | string | false |  | Ratio 0.01–0.50; exclusive with period.  
stop_profit | string|null | false | nullable: true |   
stop_loss | string|null | false | nullable: true |   
  
**create_params / asset_info**

Request Body SchemaType | Constraints  
---|---  
array | minItems: 2  
maxItems: 10  
  
**create_params / asset_info / items**

One contract member of a futures-combo strategy.

Request Body SchemaType | Constraints  
---|---  
AIHubFuturesComboAsset | required: ["market","side","rate"]  
additionalProperties: false  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
market | string | Required |  |   
side | string | Required | enum: ["buy","sell"] |   
rate | string | Required |  | Ratio 0.01–1 in increments of 0.01; all member weights sum to 1.  
  
**create_params / oneOf[0]**

Request Body SchemaType | Constraints  
---|---  
not | required: ["period"]  
  
**create_params / oneOf[0] / not**

Request Body SchemaType | Constraints  
---|---  
any | required: ["threshold"]  
  
**create_params / oneOf[1]**

Request Body SchemaType | Constraints  
---|---  
not | required: ["threshold"]  
  
**create_params / oneOf[1] / not**

Request Body SchemaType | Constraints  
---|---  
any | required: ["period"]  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Unified business response | AIHubCreateSuccessResponse  
  
### Response Schema

Status Code **200**

The response body when the creation strategy is successful.

Type | Constraints  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | Policy information returned after the policy is successfully created.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
  
**data**

Policy information returned after the policy is successfully created.

Type | Constraints  
---|---  
AIHubCreateData |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Optional |  |   
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
  
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

##  AIHubDiscoverSuccessResponse

Get the response body when the strategy recommendation is successful.

Type | Constraints  
---|---  
object | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubDiscoverData | Optional | required: ["scene","recommendations","unsupported_filters"] | Strategy recommendation result data.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
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
    
    

##  AIHubPortfolioStopSuccessResponse

The response body when the termination strategy is successful.

Type | Constraints  
---|---  
object | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioStopData | Optional |  | The result information returned after the termination strategy is successful.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
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
    
    

##  InfiniteGridCreateRequest

Create the request body for the infinite grid policy.

Type | Constraints  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["infinite_grid"] |   
market | string | Required |  |   
create_params | InfiniteGridCreateParams | Required | required: ["money","price_floor","profit_per_grid"] | Infinite grid creation parameters.  
Aligned with the app: **`money`** , **`price_floor`** , and **`profit_per_grid`** are required;  
`grid_num` and `price_type` are optional (defaults applied server-side when omitted).  
      
    
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
    
    

##  MarginGridCreateRequest

Create the request body for the Leverage Grid strategy.

Type | Constraints  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["margin_grid"] |   
market | string | Required |  |   
create_params | MarginGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type","leverage"] | Creation parameters for the Leverage Grid strategy.  
      
    
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
    
    

##  AIHubPortfolioRunningSuccessResponse

The response body when querying the running policy list is successful.

Type | Constraints  
---|---  
object | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioRunningData | Optional | required: ["items","page","page_size","total"] | Running policy list data.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
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
    
    

##  ContractMartingaleCreateRequest

Create the request body of the contract Martin strategy.

Type | Constraints  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["contract_martingale"] |   
market | string | Required |  |   
create_params | ContractMartingaleCreateParams | Required | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio","direction","leverage"] | The creation parameters of the contract Martin strategy.  
      
    
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
    
    

##  AIHubFuturesComboCreateRequest

Request body for creating a futures-combo strategy.

Type | Constraints  
---|---  
object | required: ["strategy_type","create_params"]  
additionalProperties: false  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["futures_combo"] |   
create_params | AIHubFuturesComboCreateParams | Required | required: ["begin_money_amount","begin_money_currency","asset_info","leverage"]  
additionalProperties: false | Creation parameters for a futures-combo strategy.  
      
    
    {
      "strategy_type": "futures_combo",
      "create_params": {}
    }
    
    

##  MarginGridCreateParams

Creation parameters for the Leverage Grid strategy.

Type | Constraints  
---|---  
object | required: ["money","low_price","high_price","grid_num","price_type","leverage"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  |   
low_price | string | Required |  |   
high_price | string | Required |  |   
grid_num | integer(int32) | Required | minimum: 1 |   
price_type | integer(int32) | Required | enum: [0,1] |   
leverage | string | Required |  |   
direction | FuturesDirection | Optional | enum: ["long","short","neutral"] | Direction enumeration supported by contract-based strategies.  
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
      
    
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
    
    

##  AIHubCreateSuccessResponse

The response body when the creation strategy is successful.

Type | Constraints  
---|---  
object | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | Policy information returned after the policy is successfully created.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
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
    
    

##  ContractMartingaleCreateParams

The creation parameters of the contract Martin strategy.

Type | Constraints  
---|---  
object | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio","direction","leverage"]  
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
invest_amount | string | true |  | Total strategy budget, not first-order margin. The server uses the complete existing ladder formula, owner fee and live contract facts, quantizes quantity down and rechecks before allocation. Minimum infeasible budget is rejected.  
price_deviation | string | true |  |   
max_orders | integer(int32) | true | minimum: 1 | Maximum additional entries, excluding the first; preserve this legacy meaning.  
take_profit_ratio | string | true |  |   
direction | ContractMartingaleDirection | true | enum: ["buy","sell"] | The direction enumeration supported by the contract Martin strategy is consistent with the original interface of the App.  
leverage | string | true |  |   
stop_loss_price | string | false |  | Positive fixed stop price; requires explicit stop_loss_price_type. Missing both leaves the old no-fixed-stop request unchanged.  
profit_sharing_ratio | string | false |  |   
stop_loss_price_type | string | false | enum: ["last","index","mark"] |   
  
**allOf[0]**

Type | Constraints  
---|---  
oneOf |   
  
**allOf[0] / oneOf[0]**

Type | Constraints  
---|---  
not |   
  
**allOf[0] / oneOf[0] / not**

Type | Constraints  
---|---  
anyOf |   
  
**allOf[0] / oneOf[0] / not / anyOf[0]**

Type | Constraints  
---|---  
any | required: ["stop_loss_price"]  
  
**allOf[0] / oneOf[0] / not / anyOf[1]**

Type | Constraints  
---|---  
any | required: ["stop_loss_price_type"]  
  
**allOf[0] / oneOf[1]**

Type | Constraints  
---|---  
any | required: ["stop_loss_price","stop_loss_price_type"]  
      
    
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
    
    

##  SpotMartingaleCreateRequest

Create the request body of the Spot Martin strategy.

Type | Constraints  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["spot_martingale"] |   
market | string | Required |  |   
create_params | SpotMartingaleCreateParams | Required | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio"] | Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).  
\- **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.  
\- Optional **`trigger_price`** : trigger price.  
\- If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).  
      
    
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
    
    

##  AIHubPortfolioStopData

The result information returned after the termination strategy is successful.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
result_message | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "status": "string",
      "result_message": "string",
      "operation_status": "string",
      "recovery_required": true
    }
    
    

##  SpotGridCreateRequest

Create the request body for the spot grid policy.

Type | Constraints  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["spot_grid"] |   
market | string | Required |  |   
create_params | SpotGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type"] | Creation parameters for the spot grid strategy.  
      
    
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
    
    

##  FuturesGridCreateRequest

Create the request body of the contract grid strategy.

Type | Constraints  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["futures_grid"] |   
market | string | Required |  |   
create_params | FuturesGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type","leverage"] | Creation parameters for the contract grid strategy.  
      
    
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
    
    

##  SpotGridCreateParams

Creation parameters for the spot grid strategy.

Type | Constraints  
---|---  
object | required: ["money","low_price","high_price","grid_num","price_type"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  | Amount of investment  
low_price | string | Required |  | Range lower limit  
high_price | string | Required |  | Range upper limit  
grid_num | integer(int32) | Required | minimum: 1 | Number of grids  
price_type | integer(int32) | Required | enum: [0,1] |   
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
      
    
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
    
    

##  FuturesDirection

Direction enumeration supported by contract-based strategies.

Type | Constraints  
---|---  
string |   
  
**Enumerated Values**

Value  
---  
"long"  
"short"  
"neutral"  
      
    
    "long"
    
    

##  ContractMartingaleDirection

The direction enumeration supported by the contract Martin strategy is consistent with the original interface of the App.

Type | Constraints  
---|---  
string |   
  
**Enumerated Values**

Value  
---  
"buy"  
"sell"  
      
    
    "buy"
    
    

##  AIHubPortfolioDetailSuccessResponse

The response body when querying policy details is successful.

Type | Constraints  
---|---  
object | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioDetailData | Optional | required: ["strategy_id","strategy_type","market","status","base_info","metrics","stop_supported"] | Policy details data.  
trace_id | string | Optional |  |   
label | string | Optional |  | Stable business error label when present. HTTP 200 can contain a non-200 business code; data may retain a real identity on failure.  
      
    
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

Infinite grid creation parameters. Aligned with the app: **`money`** , **`price_floor`** , and **`profit_per_grid`** are required; `grid_num` and `price_type` are optional (defaults applied server-side when omitted).

Type | Constraints  
---|---  
object | required: ["money","price_floor","profit_per_grid"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  |   
price_floor | string | Required |  | price floor  
profit_per_grid | string | Required |  | Profit per square  
grid_num | integer(int32) | Optional | minimum: 1 | Optional; may be omitted like in the app.  
price_type | integer(int32) | Optional | enum: [0,1] | Optional. `0` arithmetic grid; `1` geometric; omit for server defaults.  
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
      
    
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
    
    

##  AIHubRebalanceCreateRequest

Request body for creating a smart-position strategy.

Type | Constraints  
---|---  
object | required: ["strategy_type","create_params"]  
additionalProperties: false  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["smart_position"] |   
create_params | AIHubRebalanceCreateParams | Required | required: ["begin_money_amount","begin_money_currency","asset_info"]  
additionalProperties: false | Creation parameters for a smart-position strategy.  
      
    
    {
      "strategy_type": "smart_position",
      "create_params": {}
    }
    
    

##  AIHubCreateData

Policy information returned after the policy is successfully created.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Optional |  |   
status | string | Optional |  | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled.  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | pending when the write result requires verification; rejected for a proven pre-effect refusal.  
recovery_required | boolean | Optional |  |   
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "market": "string",
      "status": "string",
      "jump_url": "string",
      "operation_status": "string",
      "recovery_required": true
    }
    
    

##  StrategyType

The complete enumeration of policy types supported by AIHub.

Type | Constraints  
---|---  
string |   
  
**Enumerated Values**

Value  
---  
"spot_grid"  
"margin_grid"  
"infinite_grid"  
"futures_grid"  
"spot_martingale"  
"contract_martingale"  
"smart_position"  
"futures_combo"  
      
    
    "spot_grid"
    
    

##  AIHubPortfolioStopRequest

Single owner-scoped stop. Existing six-type ID/type requests retain default exits. smart_position requires explicit mode, limit requires options; futures_combo uses fixed whole-portfolio close/settlement.

Type | Constraints  
---|---  
object | required: ["strategy_id","strategy_type"]  
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
strategy_id | string | true |  |   
strategy_type | StrategyType | true | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
stop_mode | string | false | enum: ["market","limit","no_close"] | Required only for smart_position. Other types reject custom exit options.  
stop_options | AIHubRebalanceStopOptions | false | required: ["price","expiration"]  
additionalProperties: false | Options for the limit stop mode of a smart-position strategy.  
  
**allOf[0]**

Type | Constraints  
---|---  
oneOf |   
  
**allOf[0] / oneOf[0]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
strategy_type | not | true |  |   
  
**allOf[0] / oneOf[0] / strategy_type**

Type | Constraints  
---|---  
not |   
  
**allOf[0] / oneOf[0] / strategy_type / not**

Type | Constraints  
---|---  
string |   
  
**Enumerated Values**

Value  
---  
"smart_position"  
  
**allOf[0] / oneOf[0] / not**

Type | Constraints  
---|---  
anyOf |   
  
**allOf[0] / oneOf[0] / not / anyOf[0]**

Type | Constraints  
---|---  
any | required: ["stop_mode"]  
  
**allOf[0] / oneOf[0] / not / anyOf[1]**

Type | Constraints  
---|---  
any | required: ["stop_options"]  
  
**allOf[0] / oneOf[1]**

Type | Constraints  
---|---  
object | required: ["stop_mode"]  
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
strategy_type | string | true | enum: ["smart_position"] |   
stop_mode | string | true | enum: ["market","no_close"] |   
  
**allOf[0] / oneOf[1] / not**

Type | Constraints  
---|---  
any | required: ["stop_options"]  
  
**allOf[0] / oneOf[2]**

Type | Constraints  
---|---  
object | required: ["stop_mode","stop_options"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_type | string | Required | enum: ["smart_position"] |   
stop_mode | string | Required | enum: ["limit"] |   
      
    
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
    
    

##  AIHubPortfolioRunningData

Running policy list data.

Type | Constraints  
---|---  
object | required: ["items","page","page_size","total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
items | array | Required |  |   
page | integer(int32) | Required |  |   
page_size | integer(int32) | Required |  |   
total | integer(int32) | Required |  |   
  
**items**

Type | Constraints  
---|---  
array |   
  
**items / items**

A single record in the list of running policies.

Type | Constraints  
---|---  
AIHubPortfolioRunningItem | required: ["strategy_id","strategy_type","strategy_name","market","status"]  
      
    
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

Strategy recommendation result data.

Type | Constraints  
---|---  
object | required: ["scene","recommendations","unsupported_filters"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
scene | DiscoverScene | Required | enum: ["top1","bundle","filter","refresh"] | Enumeration of scenarios supported by the policy recommendation interface.  
recommendations | array | Required |  |   
unsupported_filters | array | Required |  | Filter conditions not supported in this issue  
  
**recommendations**

Type | Constraints  
---|---  
array |   
  
**recommendations / items**

A single piece of strategy recommendation information.

Type | Constraints  
---|---  
AIHubRecommendation | required: ["recommendation_id","market","strategy_type","strategy_name","summary"]  
  
**unsupported_filters**

Filter conditions not supported in this issue

Type | Constraints  
---|---  
array |   
  
**unsupported_filters / items**

Type | Constraints  
---|---  
string |   
      
    
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
    
    

##  SpotMartingaleCreateParams

Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`).

  * **Stop-loss** : use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`.
  * Optional **`trigger_price`** : trigger price.
  * If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).

Type | Constraints  
---|---  
object | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
invest_amount | string | Required |  |   
price_deviation | string | Required |  | Add-position deviation ratio as a decimal string (e.g. a 2% drop is `0.02`).  
max_orders | integer(int32) | Required | minimum: 1 |   
take_profit_ratio | string | Required |  | Take-profit ratio per round as a decimal string.  
stop_loss_per_cycle | string | Optional |  | Stop-loss ratio per round as a decimal string; optional; aligned with app `stop_loss_per_cycle`.  
trigger_price | string | Optional |  | Trigger price; optional.  
profit_sharing_ratio | string | Optional |  |   
      
    
    {
      "invest_amount": "string",
      "price_deviation": "string",
      "max_orders": 1,
      "take_profit_ratio": "string",
      "stop_loss_per_cycle": "string",
      "trigger_price": "string",
      "profit_sharing_ratio": "string"
    }
    
    

##  AIHubFuturesComboCreateParams

Creation parameters for a futures-combo strategy.

Type | Constraints  
---|---  
object | required: ["begin_money_amount","begin_money_currency","asset_info","leverage"]  
additionalProperties: false  
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
begin_money_amount | string | true |  |   
begin_money_currency | string | true | enum: ["USDT"] |   
asset_info | array | true | minItems: 2  
maxItems: 10 |   
leverage | integer | true | minimum: 1  
maximum: 100 |   
period | string | false | enum: ["30m","1h","4h","8h","12h","1d","3d","7d","14d","28d"] |   
threshold | string | false |  | Ratio 0.01–0.50; exclusive with period.  
stop_profit | string|null | false | nullable: true |   
stop_loss | string|null | false | nullable: true |   
  
**asset_info**

Type | Constraints  
---|---  
array | minItems: 2  
maxItems: 10  
  
**asset_info / items**

One contract member of a futures-combo strategy.

Type | Constraints  
---|---  
AIHubFuturesComboAsset | required: ["market","side","rate"]  
additionalProperties: false  
  
**oneOf[0]**

Type | Constraints  
---|---  
not | required: ["period"]  
  
**oneOf[0] / not**

Type | Constraints  
---|---  
any | required: ["threshold"]  
  
**oneOf[1]**

Type | Constraints  
---|---  
not | required: ["threshold"]  
  
**oneOf[1] / not**

Type | Constraints  
---|---  
any | required: ["period"]  
      
    
    {}
    
    

##  FuturesGridCreateParams

Creation parameters for the contract grid strategy.

Type | Constraints  
---|---  
object | required: ["money","low_price","high_price","grid_num","price_type","leverage"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  |   
low_price | string | Required |  |   
high_price | string | Required |  |   
grid_num | integer(int32) | Required | minimum: 1 |   
price_type | integer(int32) | Required | enum: [0,1] |   
leverage | string | Required |  |   
direction | FuturesDirection | Optional | enum: ["long","short","neutral"] | Direction enumeration supported by contract-based strategies.  
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
      
    
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
    
    

##  AIHubRecommendation

A single piece of strategy recommendation information.

Type | Constraints  
---|---  
object | required: ["recommendation_id","market","strategy_type","strategy_name","summary"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
recommendation_id | string | Required |  |   
market | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
strategy_name | string | Required |  |   
backtest_apr | string | Optional |  |   
max_drawdown | string | Optional |  |   
summary | string | Required |  |   
strategy_params_preview | string | Optional |  | Recommended-parameter preview as JSON text (string-encoded so clients deserialize it consistently). The value is a serialized JSON object whose structure varies by strategy type; callers or upper-layer models must parse it.  
      
    
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
    
    

##  AIHubFuturesComboAsset

One contract member of a futures-combo strategy.

Type | Constraints  
---|---  
object | required: ["market","side","rate"]  
additionalProperties: false  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
market | string | Required |  |   
side | string | Required | enum: ["buy","sell"] |   
rate | string | Required |  | Ratio 0.01–1 in increments of 0.01; all member weights sum to 1.  
      
    
    {
      "market": "string",
      "side": "buy",
      "rate": "string"
    }
    
    

##  DiscoverScene

Enumeration of scenarios supported by the policy recommendation interface.

Type | Constraints  
---|---  
string |   
  
**Enumerated Values**

Value  
---  
"top1"  
"bundle"  
"filter"  
"refresh"  
      
    
    "top1"
    
    

##  AIHubRebalanceCreateParams

Creation parameters for a smart-position strategy.

Type | Constraints  
---|---  
object | required: ["begin_money_amount","begin_money_currency","asset_info"]  
additionalProperties: false  
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
begin_money_amount | string | true |  |   
begin_money_currency | string | true | enum: ["USDT"] |   
asset_info | array | true | minItems: 2  
maxItems: 10 |   
period | string | false |  | Product interval between 1m and 28d.  
threshold | string | false |  | Positive ratio below 1, at most four decimal places.  
close_flag | integer | false | enum: [0,1]  
default: 1 |   
is_use_base | boolean | false |  |   
stop_profit | string | false |  |   
stop_loss | string | false |  |   
  
**asset_info**

Type | Constraints  
---|---  
array | minItems: 2  
maxItems: 10  
  
**asset_info / items**

One asset and its target weight in a smart-position strategy.

Type | Constraints  
---|---  
AIHubRebalanceAsset | required: ["asset","rate"]  
additionalProperties: false  
  
**oneOf[0]**

Type | Constraints  
---|---  
not | required: ["period"]  
  
**oneOf[0] / not**

Type | Constraints  
---|---  
any | required: ["threshold"]  
  
**oneOf[1]**

Type | Constraints  
---|---  
not | required: ["threshold"]  
  
**oneOf[1] / not**

Type | Constraints  
---|---  
any | required: ["period"]  
      
    
    {}
    
    

##  AIHubPortfolioDetailData

Policy details data.

Type | Constraints  
---|---  
object | required: ["strategy_id","strategy_type","market","status","base_info","metrics","stop_supported"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
market | string | Required |  | Single market, or empty string for a portfolio; use assets/markets for the latter.  
status | string | Required |  |   
base_info | AIHubPortfolioBaseInfo | Required | required: ["strategy_name","created_at","running_duration","invest_amount","total_profit","profit_rate"] | Strategy detail base info.  
metrics | AIHubPortfolioMetrics | Required |  | Strategy detail metrics; fields returned depend on strategy type.  
position | AIHubPortfolioPosition|null | Optional | nullable: true | Strategy detail position info; fields returned depend on strategy type.  
stop_supported | boolean | Required |  |   
assets | array | Optional |  |   
markets | array | Optional |  |   
positions | array | Optional |  |   
positions_status | string | Optional | enum: ["verified","partial","unverified","historical"] |   
configuration | object | Optional |  | Product-specific saved configuration. spot_martingale exposes AIHubSpotMartingaleConfiguration; absence is unverified. Runtime recovery internals are excluded.  
stop_progress | AIHubStopProgress | Optional |  | Read-only projection of durable facts. Absent values are unverified. Final refund excludes ordinary decrease-principal transfers. Account release is never inferred from stopped status or an empty account.  
  
**assets**

Type | Constraints  
---|---  
array |   
  
**assets / items**

Type | Constraints  
---|---  
string |   
  
**markets**

Type | Constraints  
---|---  
array |   
  
**markets / items**

Type | Constraints  
---|---  
string |   
  
**positions**

Type | Constraints  
---|---  
array |   
  
**positions / items**

Position information for one asset or market in a portfolio strategy.

Type | Constraints  
---|---  
AIHubPortfolioAssetPosition |   
      
    
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
    
    

##  AIHubStopProgress

Read-only projection of durable facts. Absent values are unverified. Final refund excludes ordinary decrease-principal transfers. Account release is never inferred from stopped status or an empty account.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
trading_finished | boolean | Optional |  |   
funds_returned | boolean | Optional |  |   
refund_amount | string | Optional |  |   
refund_currency | string | Optional |  |   
account_released | boolean | Optional |  |   
      
    
    {
      "trading_finished": true,
      "funds_returned": true,
      "refund_amount": "string",
      "refund_currency": "string",
      "account_released": true
    }
    
    

##  AIHubRebalanceAsset

One asset and its target weight in a smart-position strategy.

Type | Constraints  
---|---  
object | required: ["asset","rate"]  
additionalProperties: false  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  |   
rate | string | Required |  | Two decimal places, minimum 0.01; unique assets and sum exactly 1.  
      
    
    {
      "asset": "string",
      "rate": "string"
    }
    
    

##  AIHubRebalanceStopOptions

Options for the limit stop mode of a smart-position strategy.

Type | Constraints  
---|---  
object | required: ["price","expiration"]  
additionalProperties: false  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Required |  | One product-supported price expression; not one expression per member.  
expiration | integer(int64) | Required | minimum: 1 | Seconds of validity. Expiry cancels and returns assets; never switches to market.  
slip | string | Optional |  | Optional ratio 0.001–0.05, precision at most six.  
      
    
    {
      "price": "string",
      "expiration": 1,
      "slip": "string"
    }
    
    

##  AIHubPortfolioRunningItem

A single record in the list of running policies.

Type | Constraints  
---|---  
object | required: ["strategy_id","strategy_type","strategy_name","market","status"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_id | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | The complete enumeration of policy types supported by AIHub.  
strategy_name | string | Required |  |   
market | string | Required |  | Single market, or empty string for a portfolio; use assets/markets for the latter.  
status | string | Required |  |   
pnl | string | Optional |  |   
pnl_rate | string | Optional |  |   
invest_amount | string | Optional |  |   
created_at | string | Optional |  | Created time  
assets | array | Optional |  |   
markets | array | Optional |  |   
  
**assets**

Type | Constraints  
---|---  
array |   
  
**assets / items**

Type | Constraints  
---|---  
string |   
  
**markets**

Type | Constraints  
---|---  
array |   
  
**markets / items**

Type | Constraints  
---|---  
string |   
      
    
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
    
    

##  AIHubContractMartingaleConfiguration

AIHub-supported persisted contract settings. This is not a complete advanced native configuration.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
invest_amount | string | Optional |  |   
investment_currency | string | Optional |  |   
price_deviation | string | Optional |  |   
take_profit_ratio | string | Optional |  |   
direction | string | Optional |  |   
first_order_size | string | Optional |  | Exact decimal contract quantity from the product snapshot; empty remains unverified, never inferred from the total budget.  
max_orders | integer(int64) | Optional |  | Maximum additional entries excluding the first.  
leverage | integer(int32) | Optional |  |   
stop_loss_price_rule | AIHubMartingalePriceRule | Optional |  | Persisted price rule only, not proof that an order executed. Unknown price basis or non-positive price is not effective protection.  
      
    
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
    
    

##  AIHubPortfolioAssetPosition

Position information for one asset or market in a portfolio strategy.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Optional |  |   
market | string | Optional |  |   
side | string | Optional |  |   
amount | string | Optional |  |   
amount_unit | string | Optional |  |   
entry_price | string | Optional |  |   
position_value | string | Optional |  |   
position_value_unit | string | Optional |  |   
target_weight | string | Optional |  |   
leverage | string | Optional |  |   
      
    
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
    
    

##  AIHubPortfolioMetrics

Strategy detail metrics; fields returned depend on strategy type.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
grid_profit | string | Optional |  |   
floating_pnl | string | Optional |  |   
arbitrage_count | integer(int64) | Optional |  |   
price_range | string | Optional |  |   
grid_count | integer(int64) | Optional |  |   
estimated_liquidation_price | string | Optional |  |   
price_floor | string | Optional |  |   
grid_profit_rate | string | Optional |  |   
realized_pnl | string | Optional |  |   
finished_rounds | integer(int64) | Optional |  |   
avg_cost | string | Optional |  |   
take_profit_price | string | Optional |  |   
maintenance_margin_ratio | string | Optional |  |   
      
    
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
    
    

##  AIHubMartingalePriceRule

Persisted price rule only, not proof that an order executed. Unknown price basis or non-positive price is not effective protection.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
price | string | Optional |  |   
price_type | string | Optional |  | Original enum name (last/index/mark/unknown), or its numeric string for an unknown future enum.  
is_gte | boolean | Optional |  |   
      
    
    {
      "price": "string",
      "price_type": "string",
      "is_gte": true
    }
    
    

##  AIHubPortfolioBaseInfo

Strategy detail base info.

Type | Constraints  
---|---  
object | required: ["strategy_name","created_at","running_duration","invest_amount","total_profit","profit_rate"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
strategy_name | string | Required |  |   
created_at | string | Required |  | Created time  
running_duration | integer(int64) | Required |  | Runtime duration in seconds.  
invest_amount | string | Required |  |   
total_profit | string | Required |  |   
profit_rate | string | Required |  |   
      
    
    {
      "strategy_name": "string",
      "created_at": "string",
      "running_duration": 0,
      "invest_amount": "string",
      "total_profit": "string",
      "profit_rate": "string"
    }
    
    

##  AIHubPortfolioPosition

Strategy detail position info; fields returned depend on strategy type.

Type | Constraints  
---|---  
object|null | nullable: true  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
amount | string | Optional |  |   
entry_price | string | Optional |  |   
quote_amount | string | Optional |  |   
position_value | string | Optional |  |   
margin | string | Optional |  |   
side | string | Optional |  |   
      
    
    {
      "amount": "string",
      "entry_price": "string",
      "quote_amount": "string",
      "position_value": "string",
      "margin": "string",
      "side": "string"
    }
    
    

##  AIHubSpotMartingaleConfiguration

Saved settings supported by AIHub, not a substitute for all advanced native configuration. Absent upstream params are unverified.

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
invest_amount | string | Optional |  |   
investment_currency | string | Optional |  |   
price_deviation | string | Optional |  |   
take_profit_ratio | string | Optional |  |   
stop_loss_per_cycle | string | Optional |  | Saved per-cycle ratio, returned unchanged. Zero or negative legacy values do not constitute effective protection.  
trigger_price | string | Optional |  |   
max_orders | integer(int32) | Optional |  | Saved maximum additional entries excluding the first; not total orders.  
      
    
    {
      "invest_amount": "string",
      "investment_currency": "string",
      "price_deviation": "string",
      "take_profit_ratio": "string",
      "stop_loss_per_cycle": "string",
      "trigger_price": "string",
      "max_orders": 0
    }