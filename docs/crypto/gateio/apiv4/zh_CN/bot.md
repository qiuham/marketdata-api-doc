---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/bot
api_type: REST
updated_at: 2026-11-22 18:56:24.514936
---

# Bot

Bot AIHub 策略推荐、创建、查询与终止接口

##  获取 AIHub 策略推荐🔒 需要认证

GET`/bot/strategy/recommend`

GET `/bot/strategy/recommend`

_获取 AIHub 策略推荐_

支持六类真实官方推荐源。智能调仓在排序前按资产集合精确筛选。contract_martingale 和 futures_combo 仅支持手动创建。兼容原有年化收益率、回撤筛选及普通两段式刷新。排除条件在排序前绑定上一条逻辑候选；没有替代结果时返回空列表，不放宽约束。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
market | 请求参数 | string | 否 | 交易对，例如 `BTC_USDT`  
strategy_type | 请求参数 | string | 否 | 推荐目标策略类型；不支持 `contract_martingale`  
direction | 请求参数 | string | 否 | 行情方向  
invest_amount | 请求参数 | string | 否 | 仅提供上下文，不按预算筛选资格；未使用该条件时将其报告为不支持。  
scene | 请求参数 | string | 否 | 推荐场景；为空时，bot-service 可按实现逻辑自动推断。  
refresh_recommendation_id | 请求参数 | string | 否 | 推荐刷新上下文。用于 `scene=refresh`；当 `scene` 为空但提供此字段时，bot-service 也会自动按 `refresh` 处理。  
官方最简格式为 `strategy_type|market`；直接传入上一条推荐的 `recommendation_id` 时，会忽略第三段 `backtest_id`。  
limit | 请求参数 | integer(int32) | 否 | 实际返回条数上限，范围为 1–10，默认 10。  
max_drawdown_lte | 请求参数 | string | 否 | 最大回撤上限  
backtest_apr_gte | 请求参数 | string | 否 | 回测年化收益率下限  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
exclude_recommendation_id | 请求参数 | string | 否 | 仅用于刷新，传入上次返回的标识：type|market|backtest_id。当源 ID 冲突时，可附加稳定的参数区分标识。拒绝有歧义的旧标识；仅指标变化不视为新方案。  
  
####  详细描述

**refresh_recommendation_id** : 推荐刷新上下文。用于 `scene=refresh`；当 `scene` 为空但提供此字段时，bot-service 也会自动按 `refresh` 处理。  
官方最简格式为 `strategy_type|market`；直接传入上一条推荐的 `recommendation_id` 时，会忽略第三段 `backtest_id`。

####  枚举值列表

枚举值列表参数 | 值  
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
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubDiscoverSuccessResponse  
  
### 返回格式

状态码 **200**

获取策略推荐成功时的响应体。

类型 | 约束  
---|---  
AIHubDiscoverSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubDiscoverData | Optional | required: ["scene","recommendations","unsupported_filters"] | 策略推荐结果数据。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略推荐结果数据。

类型 | 约束  
---|---  
AIHubDiscoverData | required: ["scene","recommendations","unsupported_filters"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
scene | DiscoverScene | Required | enum: ["top1","bundle","filter","refresh"] | 策略推荐接口支持的场景枚举。  
recommendations | array | Required |  |   
unsupported_filters | array | Required |  | 本期不支持的筛选条件  
  
**data / recommendations**

类型 | 约束  
---|---  
array |   
  
**data / recommendations / items**

单条策略推荐信息。

类型 | 约束  
---|---  
AIHubRecommendation | required: ["recommendation_id","market","strategy_type","strategy_name","summary"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
recommendation_id | string | Required |  |   
market | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
strategy_name | string | Required |  |   
backtest_apr | string | Optional |  |   
max_drawdown | string | Optional |  |   
summary | string | Required |  |   
strategy_params_preview | string | Optional |  | 推荐参数预览的 JSON 文本（字符串形态传输，便于客户端统一反序列化）。 内容为按策略类型变化的 JSON 对象序列化结果；调用方或上层模型需自行解析。  
  
**data / unsupported_filters**

本期不支持的筛选条件

类型 | 约束  
---|---  
array |   
  
**data / unsupported_filters / items**

类型 | 约束  
---|---  
string |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 返回示例

> 200 返回
    
    
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
    

##  创建现货网格🔒 需要认证

POST`/bot/spot-grid/create`

POST `/bot/spot-grid/create`

_创建现货网格_

根据传入参数创建现货网格策略。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
body | body | SpotGridCreateRequest | 是 |   
strategy_type | body | string | 是 |   
market | body | string | 是 |   
create_params | body | SpotGridCreateParams | 是 | 现货网格策略的创建参数。  
» money | body | string | 是 | 投入金额  
» low_price | body | string | 是 | 区间下限  
» high_price | body | string | 是 | 区间上限  
» grid_num | body | integer(int32) | 是 | 网格数量  
» price_type | body | integer(int32) | 是 |   
» trigger_price | body | string | 否 |   
» stop_profit | body | string | 否 |   
» stop_loss | body | string | 否 |   
» profit_sharing_ratio | body | string | 否 |   
» is_use_base | body | boolean | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | spot_grid  
» price_type | 0  
» price_type | 1  
  
####  请求体结构

创建现货网格策略的请求体。

请求体结构类型 | 约束  
---|---  
SpotGridCreateRequest | required: ["strategy_type","market","create_params"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["spot_grid"] |   
market | string | Required |  |   
create_params | SpotGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type"] | 现货网格策略的创建参数。  
  
**create_params**

现货网格策略的创建参数。

请求体结构类型 | 约束  
---|---  
SpotGridCreateParams | required: ["money","low_price","high_price","grid_num","price_type"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
money | string | Required |  | 投入金额  
low_price | string | Required |  | 区间下限  
high_price | string | Required |  | 区间上限  
grid_num | integer(int32) | Required | minimum: 1 | 网格数量  
price_type | integer(int32) | Required | enum: [0,1] |   
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

创建策略成功时的响应体。

类型 | 约束  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | 策略创建成功后返回的策略信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略创建成功后返回的策略信息。

类型 | 约束  
---|---  
AIHubCreateData |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Optional |  |   
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 请求体示例
    
    
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
    

> 返回示例

> 200 返回
    
    
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
    

##  创建杠杆网格🔒 需要认证

POST`/bot/margin-grid/create`

POST `/bot/margin-grid/create`

_创建杠杆网格_

根据传入参数创建杠杆网格策略。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
body | body | MarginGridCreateRequest | 是 |   
strategy_type | body | string | 是 |   
market | body | string | 是 |   
create_params | body | MarginGridCreateParams | 是 | 杠杆网格策略的创建参数。  
» money | body | string | 是 |   
» low_price | body | string | 是 |   
» high_price | body | string | 是 |   
» grid_num | body | integer(int32) | 是 |   
» price_type | body | integer(int32) | 是 |   
» leverage | body | string | 是 |   
» direction | body | FuturesDirection | 否 | 合约类策略支持的方向枚举。  
» trigger_price | body | string | 否 |   
» stop_profit | body | string | 否 |   
» stop_loss | body | string | 否 |   
» profit_sharing_ratio | body | string | 否 |   
» is_use_base | body | boolean | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | margin_grid  
» price_type | 0  
» price_type | 1  
  
####  请求体结构

创建杠杆网格策略的请求体。

请求体结构类型 | 约束  
---|---  
MarginGridCreateRequest | required: ["strategy_type","market","create_params"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["margin_grid"] |   
market | string | Required |  |   
create_params | MarginGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type","leverage"] | 杠杆网格策略的创建参数。  
  
**create_params**

杠杆网格策略的创建参数。

请求体结构类型 | 约束  
---|---  
MarginGridCreateParams | required: ["money","low_price","high_price","grid_num","price_type","leverage"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
money | string | Required |  |   
low_price | string | Required |  |   
high_price | string | Required |  |   
grid_num | integer(int32) | Required | minimum: 1 |   
price_type | integer(int32) | Required | enum: [0,1] |   
leverage | string | Required |  |   
direction | FuturesDirection | Optional | enum: ["long","short","neutral"] | 合约类策略支持的方向枚举。  
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

创建策略成功时的响应体。

类型 | 约束  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | 策略创建成功后返回的策略信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略创建成功后返回的策略信息。

类型 | 约束  
---|---  
AIHubCreateData |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Optional |  |   
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 请求体示例
    
    
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
    

> 返回示例

> 200 返回
    
    
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
    

##  创建无限网格🔒 需要认证

POST`/bot/infinite-grid/create`

POST `/bot/infinite-grid/create`

_创建无限网格_

根据传入参数创建无限网格策略。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
body | body | InfiniteGridCreateRequest | 是 |   
strategy_type | body | string | 是 |   
market | body | string | 是 |   
create_params | body | InfiniteGridCreateParams | 是 | 无限网格策略的创建参数。  
  
与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填；  
`grid_num`、`price_type` 可选（不传时由服务端按默认处理）。  
  
» money | body | string | 是 |   
» price_floor | body | string | 是 | 价格地板  
» profit_per_grid | body | string | 是 | 每格利润  
» grid_num | body | integer(int32) | 否 | 可选；与 App 一致可省略。  
» price_type | body | integer(int32) | 否 | 可选。`0` 等差，`1` 等比；不传时按服务端默认。  
» trigger_price | body | string | 否 |   
» stop_profit | body | string | 否 |   
» stop_loss | body | string | 否 |   
» profit_sharing_ratio | body | string | 否 |   
» is_use_base | body | boolean | 否 |   
  
####  详细描述

** create_params**: 无限网格策略的创建参数。  
  
与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填；  
`grid_num`、`price_type` 可选（不传时由服务端按默认处理）。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | infinite_grid  
» price_type | 0  
» price_type | 1  
  
####  请求体结构

创建无限网格策略的请求体。

请求体结构类型 | 约束  
---|---  
InfiniteGridCreateRequest | required: ["strategy_type","market","create_params"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["infinite_grid"] |   
market | string | Required |  |   
create_params | InfiniteGridCreateParams | Required | required: ["money","price_floor","profit_per_grid"] | 无限网格策略的创建参数。  
  
与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填；  
`grid_num`、`price_type` 可选（不传时由服务端按默认处理）。  
  
**create_params**

无限网格策略的创建参数。

与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填； `grid_num`、`price_type` 可选（不传时由服务端按默认处理）。

请求体结构类型 | 约束  
---|---  
InfiniteGridCreateParams | required: ["money","price_floor","profit_per_grid"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
money | string | Required |  |   
price_floor | string | Required |  | 价格地板  
profit_per_grid | string | Required |  | 每格利润  
grid_num | integer(int32) | Optional | minimum: 1 | 可选；与 App 一致可省略。  
price_type | integer(int32) | Optional | enum: [0,1] | 可选。`0` 等差，`1` 等比；不传时按服务端默认。  
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

创建策略成功时的响应体。

类型 | 约束  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | 策略创建成功后返回的策略信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略创建成功后返回的策略信息。

类型 | 约束  
---|---  
AIHubCreateData |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Optional |  |   
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 请求体示例
    
    
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
    

> 返回示例

> 200 返回
    
    
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
    

##  创建合约网格🔒 需要认证

POST`/bot/futures-grid/create`

POST `/bot/futures-grid/create`

_创建合约网格_

根据传入参数创建合约网格策略。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
body | body | FuturesGridCreateRequest | 是 |   
strategy_type | body | string | 是 |   
market | body | string | 是 |   
create_params | body | FuturesGridCreateParams | 是 | 合约网格策略的创建参数。  
» money | body | string | 是 |   
» low_price | body | string | 是 |   
» high_price | body | string | 是 |   
» grid_num | body | integer(int32) | 是 |   
» price_type | body | integer(int32) | 是 |   
» leverage | body | string | 是 |   
» direction | body | FuturesDirection | 否 | 合约类策略支持的方向枚举。  
» trigger_price | body | string | 否 |   
» stop_profit | body | string | 否 |   
» stop_loss | body | string | 否 |   
» profit_sharing_ratio | body | string | 否 |   
» is_use_base | body | boolean | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | futures_grid  
» price_type | 0  
» price_type | 1  
  
####  请求体结构

创建合约网格策略的请求体。

请求体结构类型 | 约束  
---|---  
FuturesGridCreateRequest | required: ["strategy_type","market","create_params"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["futures_grid"] |   
market | string | Required |  |   
create_params | FuturesGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type","leverage"] | 合约网格策略的创建参数。  
  
**create_params**

合约网格策略的创建参数。

请求体结构类型 | 约束  
---|---  
FuturesGridCreateParams | required: ["money","low_price","high_price","grid_num","price_type","leverage"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
money | string | Required |  |   
low_price | string | Required |  |   
high_price | string | Required |  |   
grid_num | integer(int32) | Required | minimum: 1 |   
price_type | integer(int32) | Required | enum: [0,1] |   
leverage | string | Required |  |   
direction | FuturesDirection | Optional | enum: ["long","short","neutral"] | 合约类策略支持的方向枚举。  
trigger_price | string | Optional |  |   
stop_profit | string | Optional |  |   
stop_loss | string | Optional |  |   
profit_sharing_ratio | string | Optional |  |   
is_use_base | boolean | Optional |  |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

创建策略成功时的响应体。

类型 | 约束  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | 策略创建成功后返回的策略信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略创建成功后返回的策略信息。

类型 | 约束  
---|---  
AIHubCreateData |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Optional |  |   
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 请求体示例
    
    
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
    

> 返回示例

> 200 返回
    
    
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
    

##  创建现货马丁🔒 需要认证

POST`/bot/spot-martingale/create`

POST `/bot/spot-martingale/create`

_创建现货马丁_

根据传入参数创建现货马丁策略。

止损口径与 App / `MartingaleBot` 一致：

  * 使用 **`create_params.stop_loss_per_cycle`** （每轮止损比例，小数字符串），**不要** 使用 `stop_loss_price` 表达创建侧止损。
  * 详情页展示的「止损价」由引擎按轮次计算；创建侧可选 **`create_params.trigger_price`** （触发价）。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
body | body | SpotMartingaleCreateRequest | 是 |   
strategy_type | body | string | 是 |   
market | body | string | 是 |   
create_params | body | SpotMartingaleCreateParams | 是 | 现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。  
  
\- **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。  
\- 可选 **`trigger_price`** ：触发价。  
\- `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。  
  
» invest_amount | body | string | 是 |   
» price_deviation | body | string | 是 | 加仓偏离比例，小数字符串（例如跌幅 2% 为 `0.02`）。  
» max_orders | body | integer(int32) | 是 |   
» take_profit_ratio | body | string | 是 | 每轮止盈比例，小数字符串。  
» stop_loss_per_cycle | body | string | 否 | 每轮止损比例，小数字符串；可选，与 App `stop_loss_per_cycle` 一致。  
» trigger_price | body | string | 否 | 触发价；可选。  
» profit_sharing_ratio | body | string | 否 |   
  
####  详细描述

** create_params**: 现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。  
  
\- **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。  
\- 可选 **`trigger_price`** ：触发价。  
\- `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | spot_martingale  
  
####  请求体结构

创建现货马丁策略的请求体。

请求体结构类型 | 约束  
---|---  
SpotMartingaleCreateRequest | required: ["strategy_type","market","create_params"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["spot_martingale"] |   
market | string | Required |  |   
create_params | SpotMartingaleCreateParams | Required | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio"] | 现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。  
  
\- **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。  
\- 可选 **`trigger_price`** ：触发价。  
\- `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。  
  
**create_params**

现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。

  * **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。
  * 可选 **`trigger_price`** ：触发价。
  * `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。

请求体结构类型 | 约束  
---|---  
SpotMartingaleCreateParams | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
invest_amount | string | Required |  |   
price_deviation | string | Required |  | 加仓偏离比例，小数字符串（例如跌幅 2% 为 `0.02`）。  
max_orders | integer(int32) | Required | minimum: 1 |   
take_profit_ratio | string | Required |  | 每轮止盈比例，小数字符串。  
stop_loss_per_cycle | string | Optional |  | 每轮止损比例，小数字符串；可选，与 App `stop_loss_per_cycle` 一致。  
trigger_price | string | Optional |  | 触发价；可选。  
profit_sharing_ratio | string | Optional |  |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

创建策略成功时的响应体。

类型 | 约束  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | 策略创建成功后返回的策略信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略创建成功后返回的策略信息。

类型 | 约束  
---|---  
AIHubCreateData |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Optional |  |   
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 请求体示例
    
    
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
    

> 返回示例

> 200 返回
    
    
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
    

##  创建合约马丁🔒 需要认证

POST`/bot/contract-martingale/create`

POST `/bot/contract-martingale/create`

_创建合约马丁_

根据传入参数创建合约马丁策略。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
body | body | ContractMartingaleCreateRequest | 是 |   
strategy_type | body | string | 是 |   
market | body | string | 是 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | contract_martingale  
  
####  请求体结构

创建合约马丁策略的请求体。

请求体结构类型 | 约束  
---|---  
ContractMartingaleCreateRequest | required: ["strategy_type","market","create_params"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["contract_martingale"] |   
market | string | Required |  |   
create_params | ContractMartingaleCreateParams | Required | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio","direction","leverage"] | 合约马丁策略的创建参数。  
  
**create_params**

合约马丁策略的创建参数。

请求体结构类型 | 约束  
---|---  
ContractMartingaleCreateParams | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio","direction","leverage"]  
  
**属性**

请求体结构名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
invest_amount | string | 是 |  | 策略总预算，不是首单保证金。服务端结合现有完整阶梯公式、用户费率及实时合约信息计算，向下量化数量，并在分配前重新检查；低于可行最低预算时拒绝。  
price_deviation | string | 是 |  |   
max_orders | integer(int32) | 是 | minimum: 1 | 最大追加建仓次数，不含首单；保留原有语义。  
take_profit_ratio | string | 是 |  |   
direction | ContractMartingaleDirection | 是 | enum: ["buy","sell"] | 合约马丁策略支持的方向枚举，和 App 原始接口保持一致。  
leverage | string | 是 |  |   
stop_loss_price | string | 否 |  | 正数固定止损价；必须显式提供 stop_loss_price_type。两者均不传时，保留原有不设置固定止损的请求行为。  
profit_sharing_ratio | string | 否 |  |   
stop_loss_price_type | string | 否 | enum: ["last","index","mark"] |   
  
**create_params / allOf[0]**

请求体结构类型 | 约束  
---|---  
oneOf |   
  
**create_params / allOf[0] / oneOf[0]**

请求体结构类型 | 约束  
---|---  
not |   
  
**create_params / allOf[0] / oneOf[0] / not**

请求体结构类型 | 约束  
---|---  
anyOf |   
  
**create_params / allOf[0] / oneOf[0] / not / anyOf[0]**

请求体结构类型 | 约束  
---|---  
any | required: ["stop_loss_price"]  
  
**create_params / allOf[0] / oneOf[0] / not / anyOf[1]**

请求体结构类型 | 约束  
---|---  
any | required: ["stop_loss_price_type"]  
  
**create_params / allOf[0] / oneOf[1]**

请求体结构类型 | 约束  
---|---  
any | required: ["stop_loss_price","stop_loss_price_type"]  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

创建策略成功时的响应体。

类型 | 约束  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | 策略创建成功后返回的策略信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略创建成功后返回的策略信息。

类型 | 约束  
---|---  
AIHubCreateData |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Optional |  |   
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 请求体示例
    
    
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
    

> 返回示例

> 200 返回
    
    
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
    

##  查询运行中的策略列表。🔒 需要认证

GET`/bot/portfolio/running`

GET `/bot/portfolio/running`

_查询运行中的策略列表。_

查询用户当前运行中的 AIHub 策略列表，支持按策略类型、交易对和分页条件筛选。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
strategy_type | 请求参数 | string | 否 | 按策略类型筛选  
market | 请求参数 | string | 否 | 按交易对筛选  
page | 请求参数 | integer(int32) | 否 | 页码，默认 1  
page_size | 请求参数 | integer(int32) | 否 | 每页条数，默认 20，最大 50  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubPortfolioRunningSuccessResponse  
  
### 返回格式

状态码 **200**

查询运行中策略列表成功时的响应体。

类型 | 约束  
---|---  
AIHubPortfolioRunningSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioRunningData | Optional | required: ["items","page","page_size","total"] | 运行中策略列表数据。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

运行中策略列表数据。

类型 | 约束  
---|---  
AIHubPortfolioRunningData | required: ["items","page","page_size","total"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
items | array | Required |  |   
page | integer(int32) | Required |  |   
page_size | integer(int32) | Required |  |   
total | integer(int32) | Required |  |   
  
**data / items**

类型 | 约束  
---|---  
array |   
  
**data / items / items**

运行中策略列表的一条记录。

类型 | 约束  
---|---  
AIHubPortfolioRunningItem | required: ["strategy_id","strategy_type","strategy_name","market","status"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
strategy_name | string | Required |  |   
market | string | Required |  | 单个市场；组合策略可为空字符串，此时使用 assets/markets。  
status | string | Required |  |   
pnl | string | Optional |  |   
pnl_rate | string | Optional |  |   
invest_amount | string | Optional |  |   
created_at | string | Optional |  | 创建时间  
assets | array | Optional |  |   
markets | array | Optional |  |   
  
**data / items / items / assets**

类型 | 约束  
---|---  
array |   
  
**data / items / items / assets / items**

类型 | 约束  
---|---  
string |   
  
**data / items / items / markets**

类型 | 约束  
---|---  
array |   
  
**data / items / items / markets / items**

类型 | 约束  
---|---  
string |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 返回示例

> 200 返回
    
    
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
    

##  查询单个策略详情🔒 需要认证

GET`/bot/portfolio/detail`

GET `/bot/portfolio/detail`

_查询单个策略详情_

请求必须同时传入 `strategy_id` 和 `strategy_type`；`strategy_type` 用于按策略类型分派到底层详情实现。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
strategy_id | 请求参数 | string | 是 | 策略 ID  
strategy_type | 请求参数 | string | 是 | 策略类型；用于底层详情分派  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
strategy_type | smart_position  
strategy_type | futures_combo  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubPortfolioDetailSuccessResponse  
  
### 返回格式

状态码 **200**

查询策略详情成功时的响应体。

类型 | 约束  
---|---  
AIHubPortfolioDetailSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioDetailData | Optional | required: ["strategy_id","strategy_type","market","status","base_info","metrics","stop_supported"] | 策略详情数据。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略详情数据。

类型 | 约束  
---|---  
AIHubPortfolioDetailData | required: ["strategy_id","strategy_type","market","status","base_info","metrics","stop_supported"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Required |  | 单个市场；组合策略可为空字符串，此时使用 assets/markets。  
status | string | Required |  |   
base_info | AIHubPortfolioBaseInfo | Required | required: ["strategy_name","created_at","running_duration","invest_amount","total_profit","profit_rate"] | 策略详情基础信息。  
metrics | AIHubPortfolioMetrics | Required |  | 策略详情指标信息，按策略类型返回对应字段。  
position | AIHubPortfolioPosition|null | Optional | nullable: true | 策略详情仓位信息，按策略类型返回对应字段。  
stop_supported | boolean | Required |  |   
assets | array | Optional |  |   
markets | array | Optional |  |   
positions | array | Optional |  |   
positions_status | string | Optional | enum: ["verified","partial","unverified","historical"] |   
configuration | object | Optional |  | 按产品保存的配置。spot_martingale 返回 AIHubSpotMartingaleConfiguration；缺失时表示未核实。不包含运行时恢复内部信息。  
stop_progress | AIHubStopProgress | Optional |  | 持久化事实的只读投影。字段缺失表示未核实。最终退款不包含普通减本金划转。不能根据已停止状态或空账户推断账户已释放。  
  
**data / base_info**

策略详情基础信息。

类型 | 约束  
---|---  
AIHubPortfolioBaseInfo | required: ["strategy_name","created_at","running_duration","invest_amount","total_profit","profit_rate"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_name | string | Required |  |   
created_at | string | Required |  | 创建时间  
running_duration | integer(int64) | Required |  | 运行时长，单位秒  
invest_amount | string | Required |  |   
total_profit | string | Required |  |   
profit_rate | string | Required |  |   
  
**data / metrics**

策略详情指标信息，按策略类型返回对应字段。

类型 | 约束  
---|---  
AIHubPortfolioMetrics |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
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

策略详情仓位信息，按策略类型返回对应字段。

类型 | 约束  
---|---  
AIHubPortfolioPosition|null | nullable: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
amount | string | Optional |  |   
entry_price | string | Optional |  |   
quote_amount | string | Optional |  |   
position_value | string | Optional |  |   
margin | string | Optional |  |   
side | string | Optional |  |   
  
**data / assets**

类型 | 约束  
---|---  
array |   
  
**data / assets / items**

类型 | 约束  
---|---  
string |   
  
**data / markets**

类型 | 约束  
---|---  
array |   
  
**data / markets / items**

类型 | 约束  
---|---  
string |   
  
**data / positions**

类型 | 约束  
---|---  
array |   
  
**data / positions / items**

组合策略中单个资产或市场的仓位信息。

类型 | 约束  
---|---  
AIHubPortfolioAssetPosition |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
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

持久化事实的只读投影。字段缺失表示未核实。最终退款不包含普通减本金划转。不能根据已停止状态或空账户推断账户已释放。

类型 | 约束  
---|---  
AIHubStopProgress |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
trading_finished | boolean | Optional |  |   
funds_returned | boolean | Optional |  |   
refund_amount | string | Optional |  |   
refund_currency | string | Optional |  |   
account_released | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 返回示例

> 200 返回
    
    
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
    

##  终止单个运行中策略🔒 需要认证

POST`/bot/portfolio/stop`

POST `/bot/portfolio/stop`

_终止单个运行中策略_

单次请求只允许终止一个策略。 风险提示与二次确认由 OpenClaw 上层承担；本接口只负责执行 stop。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
body | body | AIHubPortfolioStopRequest | 是 |   
  
####  请求体结构

终止当前用户拥有的单个策略。原有六类策略的 ID/类型请求保留默认退出行为。smart_position 必须显式指定模式，limit 模式必须提供选项；futures_combo 使用固定的整组平仓及结算流程。

请求体结构类型 | 约束  
---|---  
AIHubPortfolioStopRequest | required: ["strategy_id","strategy_type"]  
  
**属性**

请求体结构名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | 是 |  |   
strategy_type | StrategyType | 是 | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
stop_mode | string | 否 | enum: ["market","limit","no_close"] | 仅 smart_position 必填。其他策略类型拒绝自定义退出选项。  
stop_options | AIHubRebalanceStopOptions | 否 | required: ["price","expiration"]  
additionalProperties: false | 智能调仓限价停止模式使用的参数。  
  
**stop_options**

智能调仓限价停止模式使用的参数。

请求体结构类型 | 约束  
---|---  
AIHubRebalanceStopOptions | required: ["price","expiration"]  
additionalProperties: false  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price | string | Required |  | 产品支持的单个价格表达式，不是为每个成员分别指定表达式。  
expiration | integer(int64) | Required | minimum: 1 | 有效时长，单位秒。到期后撤销委托并返还资产，不切换为市价。  
slip | string | Optional |  | 可选比例，范围为 0.001–0.05，最多六位小数。  
  
**allOf[0]**

请求体结构类型 | 约束  
---|---  
oneOf |   
  
**allOf[0] / oneOf[0]**

请求体结构类型 | 约束  
---|---  
object |   
  
**属性**

请求体结构名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | not | 是 |  |   
  
**allOf[0] / oneOf[0] / strategy_type**

请求体结构类型 | 约束  
---|---  
not |   
  
**allOf[0] / oneOf[0] / strategy_type / not**

请求体结构类型 | 约束  
---|---  
string |   
  
**枚举值列表**

请求体结构值  
---  
"smart_position"  
  
**allOf[0] / oneOf[0] / not**

请求体结构类型 | 约束  
---|---  
anyOf |   
  
**allOf[0] / oneOf[0] / not / anyOf[0]**

请求体结构类型 | 约束  
---|---  
any | required: ["stop_mode"]  
  
**allOf[0] / oneOf[0] / not / anyOf[1]**

请求体结构类型 | 约束  
---|---  
any | required: ["stop_options"]  
  
**allOf[0] / oneOf[1]**

请求体结构类型 | 约束  
---|---  
object | required: ["stop_mode"]  
  
**属性**

请求体结构名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | 是 | enum: ["smart_position"] |   
stop_mode | string | 是 | enum: ["market","no_close"] |   
  
**allOf[0] / oneOf[1] / not**

请求体结构类型 | 约束  
---|---  
any | required: ["stop_options"]  
  
**allOf[0] / oneOf[2]**

请求体结构类型 | 约束  
---|---  
object | required: ["stop_mode","stop_options"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["smart_position"] |   
stop_mode | string | Required | enum: ["limit"] |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubPortfolioStopSuccessResponse  
  
### 返回格式

状态码 **200**

终止策略成功时的响应体。

类型 | 约束  
---|---  
AIHubPortfolioStopSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioStopData | Optional |  | 终止策略成功后返回的结果信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

终止策略成功后返回的结果信息。

类型 | 约束  
---|---  
AIHubPortfolioStopData |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
result_message | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 请求体示例
    
    
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
    

> 返回示例

> 200 返回
    
    
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
    

##  创建智能调仓策略🔒 需要认证

POST`/bot/smart-position/create`

POST `/bot/smart-position/create`

_创建智能调仓策略_

AIHub 强类型适配接口；认证用户身份仅来自可信网关上下文。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
body | body | AIHubRebalanceCreateRequest | 是 |   
strategy_type | body | string | 是 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | smart_position  
  
####  请求体结构

创建智能调仓策略的请求体。

请求体结构类型 | 约束  
---|---  
AIHubRebalanceCreateRequest | required: ["strategy_type","create_params"]  
additionalProperties: false  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["smart_position"] |   
create_params | AIHubRebalanceCreateParams | Required | required: ["begin_money_amount","begin_money_currency","asset_info"]  
additionalProperties: false | 智能调仓策略的创建参数。  
  
**create_params**

智能调仓策略的创建参数。

请求体结构类型 | 约束  
---|---  
AIHubRebalanceCreateParams | required: ["begin_money_amount","begin_money_currency","asset_info"]  
additionalProperties: false  
  
**属性**

请求体结构名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
begin_money_amount | string | 是 |  |   
begin_money_currency | string | 是 | enum: ["USDT"] |   
asset_info | array | 是 | minItems: 2  
maxItems: 10 |   
period | string | 否 |  | 产品调仓周期，范围为 1m 至 28d。  
threshold | string | 否 |  | 大于 0 且小于 1 的比例，最多四位小数。  
close_flag | integer | 否 | enum: [0,1]  
default: 1 |   
is_use_base | boolean | 否 |  |   
stop_profit | string | 否 |  |   
stop_loss | string | 否 |  |   
  
**create_params / asset_info**

请求体结构类型 | 约束  
---|---  
array | minItems: 2  
maxItems: 10  
  
**create_params / asset_info / items**

智能调仓策略中的单个资产及目标比例。

请求体结构类型 | 约束  
---|---  
AIHubRebalanceAsset | required: ["asset","rate"]  
additionalProperties: false  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
asset | string | Required |  |   
rate | string | Required |  | 保留两位小数，最小值 0.01；资产不得重复，比例之和必须恰好为 1。  
  
**create_params / oneOf[0]**

请求体结构类型 | 约束  
---|---  
not | required: ["period"]  
  
**create_params / oneOf[0] / not**

请求体结构类型 | 约束  
---|---  
any | required: ["threshold"]  
  
**create_params / oneOf[1]**

请求体结构类型 | 约束  
---|---  
not | required: ["threshold"]  
  
**create_params / oneOf[1] / not**

请求体结构类型 | 约束  
---|---  
any | required: ["period"]  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

创建策略成功时的响应体。

类型 | 约束  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | 策略创建成功后返回的策略信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略创建成功后返回的策略信息。

类型 | 约束  
---|---  
AIHubCreateData |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Optional |  |   
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 请求体示例
    
    
    {
      "strategy_type": "smart_position",
      "create_params": {}
    }
    

> 返回示例

> 200 返回
    
    
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
    

##  创建合约拼盘策略🔒 需要认证

POST`/bot/futures-combo/create`

POST `/bot/futures-combo/create`

_创建合约拼盘策略_

AIHub 强类型适配接口；认证用户身份仅来自可信网关上下文。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
body | body | AIHubFuturesComboCreateRequest | 是 |   
strategy_type | body | string | 是 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
strategy_type | futures_combo  
  
####  请求体结构

创建合约拼盘策略的请求体。

请求体结构类型 | 约束  
---|---  
AIHubFuturesComboCreateRequest | required: ["strategy_type","create_params"]  
additionalProperties: false  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["futures_combo"] |   
create_params | AIHubFuturesComboCreateParams | Required | required: ["begin_money_amount","begin_money_currency","asset_info","leverage"]  
additionalProperties: false | 合约拼盘策略的创建参数。  
  
**create_params**

合约拼盘策略的创建参数。

请求体结构类型 | 约束  
---|---  
AIHubFuturesComboCreateParams | required: ["begin_money_amount","begin_money_currency","asset_info","leverage"]  
additionalProperties: false  
  
**属性**

请求体结构名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
begin_money_amount | string | 是 |  |   
begin_money_currency | string | 是 | enum: ["USDT"] |   
asset_info | array | 是 | minItems: 2  
maxItems: 10 |   
leverage | integer | 是 | minimum: 1  
maximum: 100 |   
period | string | 否 | enum: ["30m","1h","4h","8h","12h","1d","3d","7d","14d","28d"] |   
threshold | string | 否 |  | 比例范围为 0.01–0.50；与 period 互斥。  
stop_profit | string|null | 否 | nullable: true |   
stop_loss | string|null | 否 | nullable: true |   
  
**create_params / asset_info**

请求体结构类型 | 约束  
---|---  
array | minItems: 2  
maxItems: 10  
  
**create_params / asset_info / items**

合约拼盘的单个合约成员。

请求体结构类型 | 约束  
---|---  
AIHubFuturesComboAsset | required: ["market","side","rate"]  
additionalProperties: false  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
market | string | Required |  |   
side | string | Required | enum: ["buy","sell"] |   
rate | string | Required |  | 比例范围为 0.01–1，步长 0.01；所有成员权重之和为 1。  
  
**create_params / oneOf[0]**

请求体结构类型 | 约束  
---|---  
not | required: ["period"]  
  
**create_params / oneOf[0] / not**

请求体结构类型 | 约束  
---|---  
any | required: ["threshold"]  
  
**create_params / oneOf[1]**

请求体结构类型 | 约束  
---|---  
not | required: ["threshold"]  
  
**create_params / oneOf[1] / not**

请求体结构类型 | 约束  
---|---  
any | required: ["period"]  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

创建策略成功时的响应体。

类型 | 约束  
---|---  
AIHubCreateSuccessResponse | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | 策略创建成功后返回的策略信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
**data**

策略创建成功后返回的策略信息。

类型 | 约束  
---|---  
AIHubCreateData |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Optional |  |   
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
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
    # `gen_sign` 的实现参考认证一章
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
    
    

> 请求体示例
    
    
    {
      "strategy_type": "futures_combo",
      "create_params": {}
    }
    

> 返回示例

> 200 返回
    
    
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
    

#  模型

##  AIHubFuturesComboCreateRequest

创建合约拼盘策略的请求体。

类型 | 约束  
---|---  
object | required: ["strategy_type","create_params"]  
additionalProperties: false  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["futures_combo"] |   
create_params | AIHubFuturesComboCreateParams | Required | required: ["begin_money_amount","begin_money_currency","asset_info","leverage"]  
additionalProperties: false | 合约拼盘策略的创建参数。  
      
    
    {
      "strategy_type": "futures_combo",
      "create_params": {}
    }
    
    

##  MarginGridCreateRequest

创建杠杆网格策略的请求体。

类型 | 约束  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["margin_grid"] |   
market | string | Required |  |   
create_params | MarginGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type","leverage"] | 杠杆网格策略的创建参数。  
      
    
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
    
    

##  SpotGridCreateRequest

创建现货网格策略的请求体。

类型 | 约束  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["spot_grid"] |   
market | string | Required |  |   
create_params | SpotGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type"] | 现货网格策略的创建参数。  
      
    
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
    
    

##  AIHubCreateSuccessResponse

创建策略成功时的响应体。

类型 | 约束  
---|---  
object | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubCreateData | Optional |  | 策略创建成功后返回的策略信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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
    
    

##  AIHubFuturesComboCreateParams

合约拼盘策略的创建参数。

类型 | 约束  
---|---  
object | required: ["begin_money_amount","begin_money_currency","asset_info","leverage"]  
additionalProperties: false  
  
**属性**

名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
begin_money_amount | string | 是 |  |   
begin_money_currency | string | 是 | enum: ["USDT"] |   
asset_info | array | 是 | minItems: 2  
maxItems: 10 |   
leverage | integer | 是 | minimum: 1  
maximum: 100 |   
period | string | 否 | enum: ["30m","1h","4h","8h","12h","1d","3d","7d","14d","28d"] |   
threshold | string | 否 |  | 比例范围为 0.01–0.50；与 period 互斥。  
stop_profit | string|null | 否 | nullable: true |   
stop_loss | string|null | 否 | nullable: true |   
  
**asset_info**

类型 | 约束  
---|---  
array | minItems: 2  
maxItems: 10  
  
**asset_info / items**

合约拼盘的单个合约成员。

类型 | 约束  
---|---  
AIHubFuturesComboAsset | required: ["market","side","rate"]  
additionalProperties: false  
  
**oneOf[0]**

类型 | 约束  
---|---  
not | required: ["period"]  
  
**oneOf[0] / not**

类型 | 约束  
---|---  
any | required: ["threshold"]  
  
**oneOf[1]**

类型 | 约束  
---|---  
not | required: ["threshold"]  
  
**oneOf[1] / not**

类型 | 约束  
---|---  
any | required: ["period"]  
      
    
    {}
    
    

##  AIHubDiscoverSuccessResponse

获取策略推荐成功时的响应体。

类型 | 约束  
---|---  
object | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubDiscoverData | Optional | required: ["scene","recommendations","unsupported_filters"] | 策略推荐结果数据。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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

创建现货马丁策略的请求体。

类型 | 约束  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["spot_martingale"] |   
market | string | Required |  |   
create_params | SpotMartingaleCreateParams | Required | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio"] | 现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。  
  
\- **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。  
\- 可选 **`trigger_price`** ：触发价。  
\- `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。  
      
    
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

创建合约马丁策略的请求体。

类型 | 约束  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["contract_martingale"] |   
market | string | Required |  |   
create_params | ContractMartingaleCreateParams | Required | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio","direction","leverage"] | 合约马丁策略的创建参数。  
      
    
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
    
    

##  ContractMartingaleCreateParams

合约马丁策略的创建参数。

类型 | 约束  
---|---  
object | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio","direction","leverage"]  
  
**属性**

名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
invest_amount | string | 是 |  | 策略总预算，不是首单保证金。服务端结合现有完整阶梯公式、用户费率及实时合约信息计算，向下量化数量，并在分配前重新检查；低于可行最低预算时拒绝。  
price_deviation | string | 是 |  |   
max_orders | integer(int32) | 是 | minimum: 1 | 最大追加建仓次数，不含首单；保留原有语义。  
take_profit_ratio | string | 是 |  |   
direction | ContractMartingaleDirection | 是 | enum: ["buy","sell"] | 合约马丁策略支持的方向枚举，和 App 原始接口保持一致。  
leverage | string | 是 |  |   
stop_loss_price | string | 否 |  | 正数固定止损价；必须显式提供 stop_loss_price_type。两者均不传时，保留原有不设置固定止损的请求行为。  
profit_sharing_ratio | string | 否 |  |   
stop_loss_price_type | string | 否 | enum: ["last","index","mark"] |   
  
**allOf[0]**

类型 | 约束  
---|---  
oneOf |   
  
**allOf[0] / oneOf[0]**

类型 | 约束  
---|---  
not |   
  
**allOf[0] / oneOf[0] / not**

类型 | 约束  
---|---  
anyOf |   
  
**allOf[0] / oneOf[0] / not / anyOf[0]**

类型 | 约束  
---|---  
any | required: ["stop_loss_price"]  
  
**allOf[0] / oneOf[0] / not / anyOf[1]**

类型 | 约束  
---|---  
any | required: ["stop_loss_price_type"]  
  
**allOf[0] / oneOf[1]**

类型 | 约束  
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
    
    

##  AIHubDiscoverData

策略推荐结果数据。

类型 | 约束  
---|---  
object | required: ["scene","recommendations","unsupported_filters"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
scene | DiscoverScene | Required | enum: ["top1","bundle","filter","refresh"] | 策略推荐接口支持的场景枚举。  
recommendations | array | Required |  |   
unsupported_filters | array | Required |  | 本期不支持的筛选条件  
  
**recommendations**

类型 | 约束  
---|---  
array |   
  
**recommendations / items**

单条策略推荐信息。

类型 | 约束  
---|---  
AIHubRecommendation | required: ["recommendation_id","market","strategy_type","strategy_name","summary"]  
  
**unsupported_filters**

本期不支持的筛选条件

类型 | 约束  
---|---  
array |   
  
**unsupported_filters / items**

类型 | 约束  
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
    
    

##  AIHubRecommendation

单条策略推荐信息。

类型 | 约束  
---|---  
object | required: ["recommendation_id","market","strategy_type","strategy_name","summary"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
recommendation_id | string | Required |  |   
market | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
strategy_name | string | Required |  |   
backtest_apr | string | Optional |  |   
max_drawdown | string | Optional |  |   
summary | string | Required |  |   
strategy_params_preview | string | Optional |  | 推荐参数预览的 JSON 文本（字符串形态传输，便于客户端统一反序列化）。 内容为按策略类型变化的 JSON 对象序列化结果；调用方或上层模型需自行解析。  
      
    
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
    
    

##  DiscoverScene

策略推荐接口支持的场景枚举。

类型 | 约束  
---|---  
string |   
  
**枚举值列表**

值  
---  
"top1"  
"bundle"  
"filter"  
"refresh"  
      
    
    "top1"
    
    

##  SpotGridCreateParams

现货网格策略的创建参数。

类型 | 约束  
---|---  
object | required: ["money","low_price","high_price","grid_num","price_type"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
money | string | Required |  | 投入金额  
low_price | string | Required |  | 区间下限  
high_price | string | Required |  | 区间上限  
grid_num | integer(int32) | Required | minimum: 1 | 网格数量  
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
    
    

##  AIHubRebalanceCreateRequest

创建智能调仓策略的请求体。

类型 | 约束  
---|---  
object | required: ["strategy_type","create_params"]  
additionalProperties: false  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["smart_position"] |   
create_params | AIHubRebalanceCreateParams | Required | required: ["begin_money_amount","begin_money_currency","asset_info"]  
additionalProperties: false | 智能调仓策略的创建参数。  
      
    
    {
      "strategy_type": "smart_position",
      "create_params": {}
    }
    
    

##  AIHubPortfolioRunningSuccessResponse

查询运行中策略列表成功时的响应体。

类型 | 约束  
---|---  
object | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioRunningData | Optional | required: ["items","page","page_size","total"] | 运行中策略列表数据。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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
    
    

##  InfiniteGridCreateRequest

创建无限网格策略的请求体。

类型 | 约束  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["infinite_grid"] |   
market | string | Required |  |   
create_params | InfiniteGridCreateParams | Required | required: ["money","price_floor","profit_per_grid"] | 无限网格策略的创建参数。  
  
与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填；  
`grid_num`、`price_type` 可选（不传时由服务端按默认处理）。  
      
    
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
    
    

##  AIHubPortfolioDetailSuccessResponse

查询策略详情成功时的响应体。

类型 | 约束  
---|---  
object | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioDetailData | Optional | required: ["strategy_id","strategy_type","market","status","base_info","metrics","stop_supported"] | 策略详情数据。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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
    
    

##  SpotMartingaleCreateParams

现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。

  * **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。
  * 可选 **`trigger_price`** ：触发价。
  * `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。

类型 | 约束  
---|---  
object | required: ["invest_amount","price_deviation","max_orders","take_profit_ratio"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
invest_amount | string | Required |  |   
price_deviation | string | Required |  | 加仓偏离比例，小数字符串（例如跌幅 2% 为 `0.02`）。  
max_orders | integer(int32) | Required | minimum: 1 |   
take_profit_ratio | string | Required |  | 每轮止盈比例，小数字符串。  
stop_loss_per_cycle | string | Optional |  | 每轮止损比例，小数字符串；可选，与 App `stop_loss_per_cycle` 一致。  
trigger_price | string | Optional |  | 触发价；可选。  
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
    
    

##  AIHubPortfolioStopRequest

终止当前用户拥有的单个策略。原有六类策略的 ID/类型请求保留默认退出行为。smart_position 必须显式指定模式，limit 模式必须提供选项；futures_combo 使用固定的整组平仓及结算流程。

类型 | 约束  
---|---  
object | required: ["strategy_id","strategy_type"]  
  
**属性**

名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | 是 |  |   
strategy_type | StrategyType | 是 | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
stop_mode | string | 否 | enum: ["market","limit","no_close"] | 仅 smart_position 必填。其他策略类型拒绝自定义退出选项。  
stop_options | AIHubRebalanceStopOptions | 否 | required: ["price","expiration"]  
additionalProperties: false | 智能调仓限价停止模式使用的参数。  
  
**allOf[0]**

类型 | 约束  
---|---  
oneOf |   
  
**allOf[0] / oneOf[0]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | not | 是 |  |   
  
**allOf[0] / oneOf[0] / strategy_type**

类型 | 约束  
---|---  
not |   
  
**allOf[0] / oneOf[0] / strategy_type / not**

类型 | 约束  
---|---  
string |   
  
**枚举值列表**

值  
---  
"smart_position"  
  
**allOf[0] / oneOf[0] / not**

类型 | 约束  
---|---  
anyOf |   
  
**allOf[0] / oneOf[0] / not / anyOf[0]**

类型 | 约束  
---|---  
any | required: ["stop_mode"]  
  
**allOf[0] / oneOf[0] / not / anyOf[1]**

类型 | 约束  
---|---  
any | required: ["stop_options"]  
  
**allOf[0] / oneOf[1]**

类型 | 约束  
---|---  
object | required: ["stop_mode"]  
  
**属性**

名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | 是 | enum: ["smart_position"] |   
stop_mode | string | 是 | enum: ["market","no_close"] |   
  
**allOf[0] / oneOf[1] / not**

类型 | 约束  
---|---  
any | required: ["stop_options"]  
  
**allOf[0] / oneOf[2]**

类型 | 约束  
---|---  
object | required: ["stop_mode","stop_options"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
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
    
    

##  AIHubFuturesComboAsset

合约拼盘的单个合约成员。

类型 | 约束  
---|---  
object | required: ["market","side","rate"]  
additionalProperties: false  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
market | string | Required |  |   
side | string | Required | enum: ["buy","sell"] |   
rate | string | Required |  | 比例范围为 0.01–1，步长 0.01；所有成员权重之和为 1。  
      
    
    {
      "market": "string",
      "side": "buy",
      "rate": "string"
    }
    
    

##  MarginGridCreateParams

杠杆网格策略的创建参数。

类型 | 约束  
---|---  
object | required: ["money","low_price","high_price","grid_num","price_type","leverage"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
money | string | Required |  |   
low_price | string | Required |  |   
high_price | string | Required |  |   
grid_num | integer(int32) | Required | minimum: 1 |   
price_type | integer(int32) | Required | enum: [0,1] |   
leverage | string | Required |  |   
direction | FuturesDirection | Optional | enum: ["long","short","neutral"] | 合约类策略支持的方向枚举。  
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
    
    

##  FuturesGridCreateRequest

创建合约网格策略的请求体。

类型 | 约束  
---|---  
object | required: ["strategy_type","market","create_params"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | string | Required | enum: ["futures_grid"] |   
market | string | Required |  |   
create_params | FuturesGridCreateParams | Required | required: ["money","low_price","high_price","grid_num","price_type","leverage"] | 合约网格策略的创建参数。  
      
    
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
    
    

##  StrategyType

AIHub 支持的完整策略类型枚举。

类型 | 约束  
---|---  
string |   
  
**枚举值列表**

值  
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
    
    

##  AIHubCreateData

策略创建成功后返回的策略信息。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Optional |  |   
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
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
    
    

##  AIHubPortfolioStopSuccessResponse

终止策略成功时的响应体。

类型 | 约束  
---|---  
object | required: ["code","message"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Required |  |   
message | string | Required |  |   
data | AIHubPortfolioStopData | Optional |  | 终止策略成功后返回的结果信息。  
trace_id | string | Optional |  |   
label | string | Optional |  | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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
    
    

##  AIHubRebalanceStopOptions

智能调仓限价停止模式使用的参数。

类型 | 约束  
---|---  
object | required: ["price","expiration"]  
additionalProperties: false  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price | string | Required |  | 产品支持的单个价格表达式，不是为每个成员分别指定表达式。  
expiration | integer(int64) | Required | minimum: 1 | 有效时长，单位秒。到期后撤销委托并返还资产，不切换为市价。  
slip | string | Optional |  | 可选比例，范围为 0.001–0.05，最多六位小数。  
      
    
    {
      "price": "string",
      "expiration": 1,
      "slip": "string"
    }
    
    

##  ContractMartingaleDirection

合约马丁策略支持的方向枚举，和 App 原始接口保持一致。

类型 | 约束  
---|---  
string |   
  
**枚举值列表**

值  
---  
"buy"  
"sell"  
      
    
    "buy"
    
    

##  AIHubPortfolioRunningData

运行中策略列表数据。

类型 | 约束  
---|---  
object | required: ["items","page","page_size","total"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
items | array | Required |  |   
page | integer(int32) | Required |  |   
page_size | integer(int32) | Required |  |   
total | integer(int32) | Required |  |   
  
**items**

类型 | 约束  
---|---  
array |   
  
**items / items**

运行中策略列表的一条记录。

类型 | 约束  
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
    
    

##  AIHubRebalanceCreateParams

智能调仓策略的创建参数。

类型 | 约束  
---|---  
object | required: ["begin_money_amount","begin_money_currency","asset_info"]  
additionalProperties: false  
  
**属性**

名称 | 类型 | 当前对象内必填 | 约束 | 描述  
---|---|---|---|---  
begin_money_amount | string | 是 |  |   
begin_money_currency | string | 是 | enum: ["USDT"] |   
asset_info | array | 是 | minItems: 2  
maxItems: 10 |   
period | string | 否 |  | 产品调仓周期，范围为 1m 至 28d。  
threshold | string | 否 |  | 大于 0 且小于 1 的比例，最多四位小数。  
close_flag | integer | 否 | enum: [0,1]  
default: 1 |   
is_use_base | boolean | 否 |  |   
stop_profit | string | 否 |  |   
stop_loss | string | 否 |  |   
  
**asset_info**

类型 | 约束  
---|---  
array | minItems: 2  
maxItems: 10  
  
**asset_info / items**

智能调仓策略中的单个资产及目标比例。

类型 | 约束  
---|---  
AIHubRebalanceAsset | required: ["asset","rate"]  
additionalProperties: false  
  
**oneOf[0]**

类型 | 约束  
---|---  
not | required: ["period"]  
  
**oneOf[0] / not**

类型 | 约束  
---|---  
any | required: ["threshold"]  
  
**oneOf[1]**

类型 | 约束  
---|---  
not | required: ["threshold"]  
  
**oneOf[1] / not**

类型 | 约束  
---|---  
any | required: ["period"]  
      
    
    {}
    
    

##  FuturesGridCreateParams

合约网格策略的创建参数。

类型 | 约束  
---|---  
object | required: ["money","low_price","high_price","grid_num","price_type","leverage"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
money | string | Required |  |   
low_price | string | Required |  |   
high_price | string | Required |  |   
grid_num | integer(int32) | Required | minimum: 1 |   
price_type | integer(int32) | Required | enum: [0,1] |   
leverage | string | Required |  |   
direction | FuturesDirection | Optional | enum: ["long","short","neutral"] | 合约类策略支持的方向枚举。  
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
    
    

##  AIHubPortfolioDetailData

策略详情数据。

类型 | 约束  
---|---  
object | required: ["strategy_id","strategy_type","market","status","base_info","metrics","stop_supported"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
market | string | Required |  | 单个市场；组合策略可为空字符串，此时使用 assets/markets。  
status | string | Required |  |   
base_info | AIHubPortfolioBaseInfo | Required | required: ["strategy_name","created_at","running_duration","invest_amount","total_profit","profit_rate"] | 策略详情基础信息。  
metrics | AIHubPortfolioMetrics | Required |  | 策略详情指标信息，按策略类型返回对应字段。  
position | AIHubPortfolioPosition|null | Optional | nullable: true | 策略详情仓位信息，按策略类型返回对应字段。  
stop_supported | boolean | Required |  |   
assets | array | Optional |  |   
markets | array | Optional |  |   
positions | array | Optional |  |   
positions_status | string | Optional | enum: ["verified","partial","unverified","historical"] |   
configuration | object | Optional |  | 按产品保存的配置。spot_martingale 返回 AIHubSpotMartingaleConfiguration；缺失时表示未核实。不包含运行时恢复内部信息。  
stop_progress | AIHubStopProgress | Optional |  | 持久化事实的只读投影。字段缺失表示未核实。最终退款不包含普通减本金划转。不能根据已停止状态或空账户推断账户已释放。  
  
**assets**

类型 | 约束  
---|---  
array |   
  
**assets / items**

类型 | 约束  
---|---  
string |   
  
**markets**

类型 | 约束  
---|---  
array |   
  
**markets / items**

类型 | 约束  
---|---  
string |   
  
**positions**

类型 | 约束  
---|---  
array |   
  
**positions / items**

组合策略中单个资产或市场的仓位信息。

类型 | 约束  
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
    
    

##  FuturesDirection

合约类策略支持的方向枚举。

类型 | 约束  
---|---  
string |   
  
**枚举值列表**

值  
---  
"long"  
"short"  
"neutral"  
      
    
    "long"
    
    

##  AIHubPortfolioStopData

终止策略成功后返回的结果信息。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Optional |  |   
strategy_type | StrategyType | Optional | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
status | string | Optional |  | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
result_message | string | Optional |  |   
operation_status | string | Optional |  | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | Optional |  |   
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "status": "string",
      "result_message": "string",
      "operation_status": "string",
      "recovery_required": true
    }
    
    

##  AIHubPortfolioRunningItem

运行中策略列表的一条记录。

类型 | 约束  
---|---  
object | required: ["strategy_id","strategy_type","strategy_name","market","status"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_id | string | Required |  |   
strategy_type | StrategyType | Required | enum: ["spot_grid","margin_grid","infinite_grid","futures_grid","spot_martingale","contract_martingale","smart_position","futures_combo"] | AIHub 支持的完整策略类型枚举。  
strategy_name | string | Required |  |   
market | string | Required |  | 单个市场；组合策略可为空字符串，此时使用 assets/markets。  
status | string | Required |  |   
pnl | string | Optional |  |   
pnl_rate | string | Optional |  |   
invest_amount | string | Optional |  |   
created_at | string | Optional |  | 创建时间  
assets | array | Optional |  |   
markets | array | Optional |  |   
  
**assets**

类型 | 约束  
---|---  
array |   
  
**assets / items**

类型 | 约束  
---|---  
string |   
  
**markets**

类型 | 约束  
---|---  
array |   
  
**markets / items**

类型 | 约束  
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
    
    

##  InfiniteGridCreateParams

无限网格策略的创建参数。

与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填； `grid_num`、`price_type` 可选（不传时由服务端按默认处理）。

类型 | 约束  
---|---  
object | required: ["money","price_floor","profit_per_grid"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
money | string | Required |  |   
price_floor | string | Required |  | 价格地板  
profit_per_grid | string | Required |  | 每格利润  
grid_num | integer(int32) | Optional | minimum: 1 | 可选；与 App 一致可省略。  
price_type | integer(int32) | Optional | enum: [0,1] | 可选。`0` 等差，`1` 等比；不传时按服务端默认。  
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
    
    

##  AIHubPortfolioPosition

策略详情仓位信息，按策略类型返回对应字段。

类型 | 约束  
---|---  
object|null | nullable: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
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

AIHub 支持的已保存配置，不能替代全部高级原生配置。上游参数缺失时表示未核实。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
invest_amount | string | Optional |  |   
investment_currency | string | Optional |  |   
price_deviation | string | Optional |  |   
take_profit_ratio | string | Optional |  |   
stop_loss_per_cycle | string | Optional |  | 已保存的每轮比例，原样返回。历史值为 0 或负数时，不构成有效保护。  
trigger_price | string | Optional |  |   
max_orders | integer(int32) | Optional |  | 已保存的最大追加建仓次数，不含首单，并非总订单数。  
      
    
    {
      "invest_amount": "string",
      "investment_currency": "string",
      "price_deviation": "string",
      "take_profit_ratio": "string",
      "stop_loss_per_cycle": "string",
      "trigger_price": "string",
      "max_orders": 0
    }
    
    

##  AIHubPortfolioMetrics

策略详情指标信息，按策略类型返回对应字段。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
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
    
    

##  AIHubStopProgress

持久化事实的只读投影。字段缺失表示未核实。最终退款不包含普通减本金划转。不能根据已停止状态或空账户推断账户已释放。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
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
    
    

##  AIHubContractMartingaleConfiguration

AIHub 支持的已保存合约配置，不是完整的高级原生配置。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
invest_amount | string | Optional |  |   
investment_currency | string | Optional |  |   
price_deviation | string | Optional |  |   
take_profit_ratio | string | Optional |  |   
direction | string | Optional |  |   
first_order_size | string | Optional |  | 产品快照中的精确十进制合约数量；空值表示未核实，不根据总预算推算。  
max_orders | integer(int64) | Optional |  | 最大追加建仓次数，不含首单。  
leverage | integer(int32) | Optional |  |   
stop_loss_price_rule | AIHubMartingalePriceRule | Optional |  | 仅表示已保存的价格规则，不能证明订单已经执行。价格依据未知或价格非正数时，不构成有效保护。  
      
    
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
    
    

##  AIHubPortfolioBaseInfo

策略详情基础信息。

类型 | 约束  
---|---  
object | required: ["strategy_name","created_at","running_duration","invest_amount","total_profit","profit_rate"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_name | string | Required |  |   
created_at | string | Required |  | 创建时间  
running_duration | integer(int64) | Required |  | 运行时长，单位秒  
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
    
    

##  AIHubMartingalePriceRule

仅表示已保存的价格规则，不能证明订单已经执行。价格依据未知或价格非正数时，不构成有效保护。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price | string | Optional |  |   
price_type | string | Optional |  | 原始枚举名称（last/index/mark/unknown）；未来出现未知枚举时返回其数字字符串。  
is_gte | boolean | Optional |  |   
      
    
    {
      "price": "string",
      "price_type": "string",
      "is_gte": true
    }
    
    

##  AIHubRebalanceAsset

智能调仓策略中的单个资产及目标比例。

类型 | 约束  
---|---  
object | required: ["asset","rate"]  
additionalProperties: false  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
asset | string | Required |  |   
rate | string | Required |  | 保留两位小数，最小值 0.01；资产不得重复，比例之和必须恰好为 1。  
      
    
    {
      "asset": "string",
      "rate": "string"
    }
    
    

##  AIHubPortfolioAssetPosition

组合策略中单个资产或市场的仓位信息。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
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