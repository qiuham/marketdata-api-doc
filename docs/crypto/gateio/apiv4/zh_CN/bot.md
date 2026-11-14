---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/bot
api_type: REST
updated_at: 2026-11-13 20:57:41.462777
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
exclude_recommendation_id | 请求参数 | string | 否 | 仅用于刷新，传入上次返回的标识：type  
  
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

_获取策略推荐成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubDiscoverData | 策略推荐结果数据。  
»» scene | DiscoverScene | 策略推荐接口支持的场景枚举。  
»» recommendations | array | [单条策略推荐信息。]  
»»» _None_ | AIHubRecommendation | 单条策略推荐信息。  
»»»» recommendation_id | string |   
»»»» market | string |   
»»»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»»»» strategy_name | string |   
»»»» backtest_apr | string |   
»»»» max_drawdown | string |   
»»»» summary | string |   
»»»» strategy_params_preview | string | 推荐参数预览的 JSON 文本（字符串形态传输，便于客户端统一反序列化）。 内容为按策略类型变化的 JSON 对象序列化结果；调用方或上层模型需自行解析。  
»»» unsupported_filters | array | 本期不支持的筛选条件  
»» trace_id | string |   
»» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
» strategy_type | body | string | 是 |   
» market | body | string | 是 |   
» create_params | body | SpotGridCreateParams | 是 | 现货网格策略的创建参数。  
»» money | body | string | 是 | 投入金额  
»» low_price | body | string | 是 | 区间下限  
»» high_price | body | string | 是 | 区间上限  
»» grid_num | body | integer(int32) | 是 | 网格数量  
»» price_type | body | integer(int32) | 是 |   
»» trigger_price | body | string | 否 |   
»» stop_profit | body | string | 否 |   
»» stop_loss | body | string | 否 |   
»» profit_sharing_ratio | body | string | 否 |   
»» is_use_base | body | boolean | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» strategy_type | spot_grid  
»» price_type | 0  
»» price_type | 1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

_创建策略成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubCreateData | 策略创建成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
»» jump_url | string |   
»» operation_status | string | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
»» recovery_required | boolean |   
» trace_id | string |   
» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
» strategy_type | body | string | 是 |   
» market | body | string | 是 |   
» create_params | body | MarginGridCreateParams | 是 | 杠杆网格策略的创建参数。  
»» money | body | string | 是 |   
»» low_price | body | string | 是 |   
»» high_price | body | string | 是 |   
»» grid_num | body | integer(int32) | 是 |   
»» price_type | body | integer(int32) | 是 |   
»» leverage | body | string | 是 |   
»» direction | body | FuturesDirection | 否 | 合约类策略支持的方向枚举。  
»» trigger_price | body | string | 否 |   
»» stop_profit | body | string | 否 |   
»» stop_loss | body | string | 否 |   
»» profit_sharing_ratio | body | string | 否 |   
»» is_use_base | body | boolean | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» strategy_type | margin_grid  
»» price_type | 0  
»» price_type | 1  
»» direction | long  
»» direction | short  
»» direction | neutral  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

_创建策略成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubCreateData | 策略创建成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
»» jump_url | string |   
»» operation_status | string | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
»» recovery_required | boolean |   
» trace_id | string |   
» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
» strategy_type | body | string | 是 |   
» market | body | string | 是 |   
» create_params | body | InfiniteGridCreateParams | 是 | 无限网格策略的创建参数。  
  
与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填；  
`grid_num`、`price_type` 可选（不传时由服务端按默认处理）。  
»» money | body | string | 是 |   
»» price_floor | body | string | 是 | 价格地板  
»» profit_per_grid | body | string | 是 | 每格利润  
»» grid_num | body | integer(int32) | 否 | 可选；与 App 一致可省略。  
»» price_type | body | integer(int32) | 否 | 可选。`0` 等差，`1` 等比；不传时按服务端默认。  
»» trigger_price | body | string | 否 |   
»» stop_profit | body | string | 否 |   
»» stop_loss | body | string | 否 |   
»» profit_sharing_ratio | body | string | 否 |   
»» is_use_base | body | boolean | 否 |   
  
####  详细描述

**» create_params** : 无限网格策略的创建参数。  
  
与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填；  
`grid_num`、`price_type` 可选（不传时由服务端按默认处理）。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» strategy_type | infinite_grid  
»» price_type | 0  
»» price_type | 1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

_创建策略成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubCreateData | 策略创建成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
»» jump_url | string |   
»» operation_status | string | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
»» recovery_required | boolean |   
» trace_id | string |   
» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
» strategy_type | body | string | 是 |   
» market | body | string | 是 |   
» create_params | body | FuturesGridCreateParams | 是 | 合约网格策略的创建参数。  
»» money | body | string | 是 |   
»» low_price | body | string | 是 |   
»» high_price | body | string | 是 |   
»» grid_num | body | integer(int32) | 是 |   
»» price_type | body | integer(int32) | 是 |   
»» leverage | body | string | 是 |   
»» direction | body | FuturesDirection | 否 | 合约类策略支持的方向枚举。  
»» trigger_price | body | string | 否 |   
»» stop_profit | body | string | 否 |   
»» stop_loss | body | string | 否 |   
»» profit_sharing_ratio | body | string | 否 |   
»» is_use_base | body | boolean | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» strategy_type | futures_grid  
»» price_type | 0  
»» price_type | 1  
»» direction | long  
»» direction | short  
»» direction | neutral  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

_创建策略成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubCreateData | 策略创建成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
»» jump_url | string |   
»» operation_status | string | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
»» recovery_required | boolean |   
» trace_id | string |   
» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
» strategy_type | body | string | 是 |   
» market | body | string | 是 |   
» create_params | body | SpotMartingaleCreateParams | 是 | 现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。  
  
\- **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。  
\- 可选 **`trigger_price`** ：触发价。  
\- `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。  
»» invest_amount | body | string | 是 |   
»» price_deviation | body | string | 是 | 加仓偏离比例，小数字符串（例如跌幅 2% 为 `0.02`）。  
»» max_orders | body | integer(int32) | 是 |   
»» take_profit_ratio | body | string | 是 | 每轮止盈比例，小数字符串。  
»» stop_loss_per_cycle | body | string | 否 | 每轮止损比例，小数字符串；可选，与 App `stop_loss_per_cycle` 一致。  
»» trigger_price | body | string | 否 | 触发价；可选。  
»» profit_sharing_ratio | body | string | 否 |   
  
####  详细描述

**» create_params** : 现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。  
  
\- **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。  
\- 可选 **`trigger_price`** ：触发价。  
\- `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» strategy_type | spot_martingale  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

_创建策略成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubCreateData | 策略创建成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
»» jump_url | string |   
»» operation_status | string | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
»» recovery_required | boolean |   
» trace_id | string |   
» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
» strategy_type | body | string | 是 |   
» market | body | string | 是 |   
» create_params | body | ContractMartingaleCreateParams | 是 | 合约马丁策略的创建参数。  
»» invest_amount | body | string | 是 | 策略总预算，不是首单保证金。服务端结合现有完整阶梯公式、用户费率及实时合约信息计算，向下量化数量，并在分配前重新检查；低于可行最低预算时拒绝。  
»» price_deviation | body | string | 是 |   
»» max_orders | body | integer(int32) | 是 | 最大追加建仓次数，不含首单；保留原有语义。  
»» take_profit_ratio | body | string | 是 |   
»» direction | body | ContractMartingaleDirection | 是 | 合约马丁策略支持的方向枚举，和 App 原始接口保持一致。  
»» leverage | body | string | 是 |   
»» stop_loss_price | body | string | 否 | 正数固定止损价；必须显式提供 stop_loss_price_type。两者均不传时，保留原有不设置固定止损的请求行为。  
»» profit_sharing_ratio | body | string | 否 |   
»» stop_loss_price_type | body | string | 否 |   
»» _None_ | body | any | 否 |   
»»» _None_ | body | any | 否 |   
»»»» _None_ | body | object | 否 |   
»»»» _None_ | body | object | 否 |   
»»» _None_ | body | object | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» strategy_type | contract_martingale  
»» direction | buy  
»» direction | sell  
»» stop_loss_price_type | last  
»» stop_loss_price_type | index  
»» stop_loss_price_type | mark  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

_创建策略成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubCreateData | 策略创建成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
»» jump_url | string |   
»» operation_status | string | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
»» recovery_required | boolean |   
» trace_id | string |   
» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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

_查询运行中策略列表成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubPortfolioRunningData | 运行中策略列表数据。  
»» items | array | [运行中策略列表的一条记录。]  
»»» _None_ | AIHubPortfolioRunningItem | 运行中策略列表的一条记录。  
»»»» strategy_id | string |   
»»»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»»»» strategy_name | string |   
»»»» market | string | 单个市场；组合策略可为空字符串，此时使用 assets/markets。  
»»»» status | string |   
»»»» pnl | string |   
»»»» pnl_rate | string |   
»»»» invest_amount | string |   
»»»» created_at | string | 创建时间  
»»»» assets | array |   
»»»» markets | array |   
»»» page | integer(int32) |   
»»» page_size | integer(int32) |   
»»» total | integer(int32) |   
»» trace_id | string |   
»» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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

_查询策略详情成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubPortfolioDetailData | 策略详情数据。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string | 单个市场；组合策略可为空字符串，此时使用 assets/markets。  
»» status | string |   
»» base_info | AIHubPortfolioBaseInfo | 策略详情基础信息。  
»»» strategy_name | string |   
»»» created_at | string | 创建时间  
»»» running_duration | integer(int64) | 运行时长，单位秒  
»»» invest_amount | string |   
»»» total_profit | string |   
»»» profit_rate | string |   
»» metrics | AIHubPortfolioMetrics | 策略详情指标信息，按策略类型返回对应字段。  
»»» grid_profit | string |   
»»» floating_pnl | string |   
»»» arbitrage_count | integer(int64) |   
»»» price_range | string |   
»»» grid_count | integer(int64) |   
»»» estimated_liquidation_price | string |   
»»» price_floor | string |   
»»» grid_profit_rate | string |   
»»» realized_pnl | string |   
»»» finished_rounds | integer(int64) |   
»»» avg_cost | string |   
»»» take_profit_price | string |   
»»» maintenance_margin_ratio | string |   
»» position | AIHubPortfolioPosition|null | 策略详情仓位信息，按策略类型返回对应字段。  
»»» amount | string |   
»»» entry_price | string |   
»»» quote_amount | string |   
»»» position_value | string |   
»»» margin | string |   
»»» side | string |   
»» stop_supported | boolean |   
»» assets | array |   
»» markets | array |   
»» positions | array | [组合策略中单个资产或市场的仓位信息。]  
»»» _None_ | AIHubPortfolioAssetPosition | 组合策略中单个资产或市场的仓位信息。  
»»»» asset | string |   
»»»» market | string |   
»»»» side | string |   
»»»» amount | string |   
»»»» amount_unit | string |   
»»»» entry_price | string |   
»»»» position_value | string |   
»»»» position_value_unit | string |   
»»»» target_weight | string |   
»»»» leverage | string |   
»»» positions_status | string |   
»»» configuration | object | 按产品保存的配置。spot_martingale 返回 AIHubSpotMartingaleConfiguration；缺失时表示未核实。不包含运行时恢复内部信息。  
»»» stop_progress | AIHubStopProgress | 持久化事实的只读投影。字段缺失表示未核实。最终退款不包含普通减本金划转。不能根据已停止状态或空账户推断账户已释放。  
»»»» trading_finished | boolean |   
»»»» funds_returned | boolean |   
»»»» refund_amount | string |   
»»»» refund_currency | string |   
»»»» account_released | boolean |   
»»» trace_id | string |   
»»» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
» strategy_id | body | string | 是 |   
» strategy_type | body | StrategyType | 是 | AIHub 支持的完整策略类型枚举。  
» stop_mode | body | string | 否 | 仅 smart_position 必填。其他策略类型拒绝自定义退出选项。  
» stop_options | body | AIHubRebalanceStopOptions | 否 | 智能调仓限价停止模式使用的参数。  
»» price | body | string | 是 | 产品支持的单个价格表达式，不是为每个成员分别指定表达式。  
»» expiration | body | integer(int64) | 是 | 有效时长，单位秒。到期后撤销委托并返还资产，不切换为市价。  
»» slip | body | string | 否 | 可选比例，范围为 0.001–0.05，最多六位小数。  
» _None_ | body | object | 否 |   
»» strategy_type | body | any | 否 |   
»»» _None_ | body | string | 否 |   
»» _None_ | body | any | 否 |   
»»» _None_ | body | object | 否 |   
»»» _None_ | body | object | 否 |   
»» _None_ | body | object | 否 |   
»»» strategy_type | body | string | 否 |   
»»» stop_mode | body | any | 是 |   
»»» _None_ | body | object | 否 |   
»» _None_ | body | object | 否 |   
»»» strategy_type | body | string | 否 |   
»»» stop_mode | body | string | 是 |   
  
####  枚举值列表

枚举值列表参数 | 值  
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
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubPortfolioStopSuccessResponse  
  
### 返回格式

状态码 **200**

_终止策略成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubPortfolioStopData | 终止策略成功后返回的结果信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» status | string | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
»» result_message | string |   
»» operation_status | string | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
»» recovery_required | boolean |   
» trace_id | string |   
» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
» strategy_type | body | string | 是 |   
» create_params | body | AIHubRebalanceCreateParams | 是 | 智能调仓策略的创建参数。  
»» begin_money_amount | body | string | 是 |   
»» begin_money_currency | body | string | 是 |   
»» asset_info | body | array | 是 | [智能调仓策略中的单个资产及目标比例。]  
»»» _None_ | body | AIHubRebalanceAsset | 否 | 智能调仓策略中的单个资产及目标比例。  
»»»» asset | body | string | 是 |   
»»»» rate | body | string | 是 | 保留两位小数，最小值 0.01；资产不得重复，比例之和必须恰好为 1。  
»»» period | body | string | 否 | 产品调仓周期，范围为 1m 至 28d。  
»»» threshold | body | string | 否 | 大于 0 且小于 1 的比例，最多四位小数。  
»»» close_flag | body | integer | 否 |   
»»» is_use_base | body | boolean | 否 |   
»»» stop_profit | body | string | 否 |   
»»» stop_loss | body | string | 否 |   
»»» _None_ | body | object | 否 |   
»»»» _None_ | body | object | 否 |   
»»» _None_ | body | object | 否 |   
»»»» _None_ | body | object | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» strategy_type | smart_position  
»» begin_money_currency | USDT  
»»» close_flag | 0  
»»» close_flag | 1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

_创建策略成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubCreateData | 策略创建成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
»» jump_url | string |   
»» operation_status | string | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
»» recovery_required | boolean |   
» trace_id | string |   
» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
» strategy_type | body | string | 是 |   
» create_params | body | AIHubFuturesComboCreateParams | 是 | 合约拼盘策略的创建参数。  
»» begin_money_amount | body | string | 是 |   
»» begin_money_currency | body | string | 是 |   
»» asset_info | body | array | 是 | [合约拼盘的单个合约成员。]  
»»» _None_ | body | AIHubFuturesComboAsset | 否 | 合约拼盘的单个合约成员。  
»»»» market | body | string | 是 |   
»»»» side | body | string | 是 |   
»»»» rate | body | string | 是 | 比例范围为 0.01–1，步长 0.01；所有成员权重之和为 1。  
»»» leverage | body | integer | 是 |   
»»» period | body | string | 否 |   
»»» threshold | body | string | 否 | 比例范围为 0.01–0.50；与 period 互斥。  
»»» stop_profit | body | string|null | 否 |   
»»» stop_loss | body | string|null | 否 |   
»»» _None_ | body | object | 否 |   
»»»» _None_ | body | object | 否 |   
»»» _None_ | body | object | 否 |   
»»»» _None_ | body | object | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
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
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 统一业务响应 | AIHubCreateSuccessResponse  
  
### 返回格式

状态码 **200**

_创建策略成功时的响应体。_

名称 | 类型 | 描述  
---|---|---  
» code | integer(int32) |   
» message | string |   
» data | AIHubCreateData | 策略创建成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
»» jump_url | string |   
»» operation_status | string | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
»» recovery_required | boolean |   
» trace_id | string |   
» label | string | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
  
####  枚举值列表

枚举值列表属性 | 值  
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

_创建合约拼盘策略的请求体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_type | string | true | none | none  
create_params | AIHubFuturesComboCreateParams | true | none | 合约拼盘策略的创建参数。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | futures_combo  
      
    
    {
      "strategy_type": "futures_combo",
      "create_params": {}
    }
    
    

##  AIHubDiscoverSuccessResponse

_获取策略推荐成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubDiscoverData | false | none | 策略推荐结果数据。  
trace_id | string | false | none | none  
label | string | false | none | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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

_创建现货马丁策略的请求体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_type | string | true | none | none  
market | string | true | none | none  
create_params | SpotMartingaleCreateParams | true | none | 现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。  
  
\- **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。  
\- 可选 **`trigger_price`** ：触发价。  
\- `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  AIHubDiscoverData

_策略推荐结果数据。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
scene | DiscoverScene | true | none | 策略推荐接口支持的场景枚举。  
recommendations | [AIHubRecommendation] | true | none | [单条策略推荐信息。]  
unsupported_filters | array | true | none | 本期不支持的筛选条件  
      
    
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
    
    

##  DiscoverScene

_策略推荐接口支持的场景枚举。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | string | false | none | 策略推荐接口支持的场景枚举。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
_None_ | top1  
_None_ | bundle  
_None_ | filter  
_None_ | refresh  
      
    
    "top1"
    
    

##  InfiniteGridCreateRequest

_创建无限网格策略的请求体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_type | string | true | none | none  
market | string | true | none | none  
create_params | InfiniteGridCreateParams | true | none | 无限网格策略的创建参数。  
  
与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填；  
`grid_num`、`price_type` 可选（不传时由服务端按默认处理）。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  FuturesGridCreateRequest

_创建合约网格策略的请求体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_type | string | true | none | none  
market | string | true | none | none  
create_params | FuturesGridCreateParams | true | none | 合约网格策略的创建参数。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  SpotGridCreateRequest

_创建现货网格策略的请求体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_type | string | true | none | none  
market | string | true | none | none  
create_params | SpotGridCreateParams | true | none | 现货网格策略的创建参数。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  MarginGridCreateRequest

_创建杠杆网格策略的请求体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_type | string | true | none | none  
market | string | true | none | none  
create_params | MarginGridCreateParams | true | none | 杠杆网格策略的创建参数。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  ContractMartingaleCreateRequest

_创建合约马丁策略的请求体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_type | string | true | none | none  
market | string | true | none | none  
create_params | ContractMartingaleCreateParams | true | none | 合约马丁策略的创建参数。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  AIHubRebalanceCreateRequest

_创建智能调仓策略的请求体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_type | string | true | none | none  
create_params | AIHubRebalanceCreateParams | true | none | 智能调仓策略的创建参数。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | smart_position  
      
    
    {
      "strategy_type": "smart_position",
      "create_params": {}
    }
    
    

##  AIHubCreateSuccessResponse

_创建策略成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubCreateData | false | none | 策略创建成功后返回的策略信息。  
trace_id | string | false | none | none  
label | string | false | none | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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
    
    

##  SpotGridCreateParams

_现货网格策略的创建参数。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
money | string | true | none | 投入金额  
low_price | string | true | none | 区间下限  
high_price | string | true | none | 区间上限  
grid_num | integer(int32) | true | none | 网格数量  
price_type | integer(int32) | true | none | none  
trigger_price | string | false | none | none  
stop_profit | string | false | none | none  
stop_loss | string | false | none | none  
profit_sharing_ratio | string | false | none | none  
is_use_base | boolean | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  AIHubPortfolioStopRequest

_终止当前用户拥有的单个策略。原有六类策略的 ID/类型请求保留默认退出行为。smart_position 必须显式指定模式，limit 模式必须提供选项；futures_combo 使用固定的整组平仓及结算流程。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | true | none | none  
strategy_type | StrategyType | true | none | AIHub 支持的完整策略类型枚举。  
stop_mode | string | false | none | 仅 smart_position 必填。其他策略类型拒绝自定义退出选项。  
stop_options | AIHubRebalanceStopOptions | false | none | 智能调仓限价停止模式使用的参数。  
  
_oneOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
» strategy_type | any | false | none | none  
  
_not_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
»» _None_ | string | false | none | none  
  
_not_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
» _None_ | any | false | none | none  
  
_anyOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
»» _None_ | object | false | none | none  
  
_or_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
»» _None_ | object | false | none | none  
  
_xor_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
» _None_ | object | false | none | none  
»» strategy_type | string | false | none | none  
»» stop_mode | any | true | none | none  
  
_not_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
»» _None_ | object | false | none | none  
  
_xor_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
» _None_ | object | false | none | none  
»» strategy_type | string | false | none | none  
»» stop_mode | string | true | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  AIHubFuturesComboCreateParams

_合约拼盘策略的创建参数。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
begin_money_amount | string | true | none | none  
begin_money_currency | string | true | none | none  
asset_info | [AIHubFuturesComboAsset] | true | none | [合约拼盘的单个合约成员。]  
leverage | integer | true | none | none  
period | string | false | none | none  
threshold | string | false | none | 比例范围为 0.01–0.50；与 period 互斥。  
stop_profit | string|null | false | none | none  
stop_loss | string|null | false | none | none  
  
_oneOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
  
_not_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
» _None_ | object | false | none | none  
  
_xor_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
  
_not_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
» _None_ | object | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  SpotMartingaleCreateParams

*现货马丁策略的创建参数（对应 `MartingaleBot` 序列化字段）。

  * **止损** ：使用 `stop_loss_per_cycle`（每轮止损比例），与 App 一致；**不使用** `stop_loss_price`。
  * 可选 **`trigger_price`** ：触发价。
  * `stop_loss_per_cycle` 若传入且大于 0，服务端校验区间约为 `0.001`～`0.9999`（与 `check_martingale` 一致）。*

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
invest_amount | string | true | none | none  
price_deviation | string | true | none | 加仓偏离比例，小数字符串（例如跌幅 2% 为 `0.02`）。  
max_orders | integer(int32) | true | none | none  
take_profit_ratio | string | true | none | 每轮止盈比例，小数字符串。  
stop_loss_per_cycle | string | false | none | 每轮止损比例，小数字符串；可选，与 App `stop_loss_per_cycle` 一致。  
trigger_price | string | false | none | 触发价；可选。  
profit_sharing_ratio | string | false | none | none  
      
    
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

_合约马丁策略的创建参数。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
invest_amount | string | true | none | 策略总预算，不是首单保证金。服务端结合现有完整阶梯公式、用户费率及实时合约信息计算，向下量化数量，并在分配前重新检查；低于可行最低预算时拒绝。  
price_deviation | string | true | none | none  
max_orders | integer(int32) | true | none | 最大追加建仓次数，不含首单；保留原有语义。  
take_profit_ratio | string | true | none | none  
direction | ContractMartingaleDirection | true | none | 合约马丁策略支持的方向枚举，和 App 原始接口保持一致。  
leverage | string | true | none | none  
stop_loss_price | string | false | none | 正数固定止损价；必须显式提供 stop_loss_price_type。两者均不传时，保留原有不设置固定止损的请求行为。  
profit_sharing_ratio | string | false | none | none  
stop_loss_price_type | string | false | none | none  
  
_oneOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | any | false | none | none  
  
_not_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
» _None_ | any | false | none | none  
  
_anyOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
»» _None_ | object | false | none | none  
  
_or_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
»» _None_ | object | false | none | none  
  
_xor_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
» _None_ | object | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  InfiniteGridCreateParams

*无限网格策略的创建参数。

与 App 口径对齐：**仅** `money`、`price_floor`、`profit_per_grid` 为必填； `grid_num`、`price_type` 可选（不传时由服务端按默认处理）。*

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
money | string | true | none | none  
price_floor | string | true | none | 价格地板  
profit_per_grid | string | true | none | 每格利润  
grid_num | integer(int32) | false | none | 可选；与 App 一致可省略。  
price_type | integer(int32) | false | none | 可选。`0` 等差，`1` 等比；不传时按服务端默认。  
trigger_price | string | false | none | none  
stop_profit | string | false | none | none  
stop_loss | string | false | none | none  
profit_sharing_ratio | string | false | none | none  
is_use_base | boolean | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  StrategyType

_AIHub 支持的完整策略类型枚举。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | string | false | none | AIHub 支持的完整策略类型枚举。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  AIHubPortfolioDetailSuccessResponse

_查询策略详情成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubPortfolioDetailData | false | none | 策略详情数据。  
trace_id | string | false | none | none  
label | string | false | none | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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
    
    

##  AIHubPortfolioStopSuccessResponse

_终止策略成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubPortfolioStopData | false | none | 终止策略成功后返回的结果信息。  
trace_id | string | false | none | none  
label | string | false | none | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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
    
    

##  FuturesGridCreateParams

_合约网格策略的创建参数。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
money | string | true | none | none  
low_price | string | true | none | none  
high_price | string | true | none | none  
grid_num | integer(int32) | true | none | none  
price_type | integer(int32) | true | none | none  
leverage | string | true | none | none  
direction | FuturesDirection | false | none | 合约类策略支持的方向枚举。  
trigger_price | string | false | none | none  
stop_profit | string | false | none | none  
stop_loss | string | false | none | none  
profit_sharing_ratio | string | false | none | none  
is_use_base | boolean | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  AIHubPortfolioRunningSuccessResponse

_查询运行中策略列表成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubPortfolioRunningData | false | none | 运行中策略列表数据。  
trace_id | string | false | none | none  
label | string | false | none | 存在时表示稳定的业务错误标签。HTTP 200 也可能包含非 200 的业务码；失败时 data 中仍可能保留真实标识。  
      
    
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
    
    

##  AIHubCreateData

_策略创建成功后返回的策略信息。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | false | none | none  
strategy_type | StrategyType | false | none | AIHub 支持的完整策略类型枚举。  
market | string | false | none | none  
status | string | false | none | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
jump_url | string | false | none | none  
operation_status | string | false | none | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | false | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "market": "string",
      "status": "string",
      "jump_url": "string",
      "operation_status": "string",
      "recovery_required": true
    }
    
    

##  AIHubPortfolioDetailData

_策略详情数据。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | true | none | none  
strategy_type | StrategyType | true | none | AIHub 支持的完整策略类型枚举。  
market | string | true | none | 单个市场；组合策略可为空字符串，此时使用 assets/markets。  
status | string | true | none | none  
base_info | AIHubPortfolioBaseInfo | true | none | 策略详情基础信息。  
metrics | AIHubPortfolioMetrics | true | none | 策略详情指标信息，按策略类型返回对应字段。  
position | AIHubPortfolioPosition | false | none | 策略详情仓位信息，按策略类型返回对应字段。  
stop_supported | boolean | true | none | none  
assets | array | false | none | none  
markets | array | false | none | none  
positions | [AIHubPortfolioAssetPosition] | false | none | [组合策略中单个资产或市场的仓位信息。]  
positions_status | string | false | none | none  
configuration | object | false | none | 按产品保存的配置。spot_martingale 返回 AIHubSpotMartingaleConfiguration；缺失时表示未核实。不包含运行时恢复内部信息。  
stop_progress | AIHubStopProgress | false | none | 持久化事实的只读投影。字段缺失表示未核实。最终退款不包含普通减本金划转。不能根据已停止状态或空账户推断账户已释放。  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  AIHubRecommendation

_单条策略推荐信息。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
recommendation_id | string | true | none | none  
market | string | true | none | none  
strategy_type | StrategyType | true | none | AIHub 支持的完整策略类型枚举。  
strategy_name | string | true | none | none  
backtest_apr | string | false | none | none  
max_drawdown | string | false | none | none  
summary | string | true | none | none  
strategy_params_preview | string | false | none | 推荐参数预览的 JSON 文本（字符串形态传输，便于客户端统一反序列化）。 内容为按策略类型变化的 JSON 对象序列化结果；调用方或上层模型需自行解析。  
      
    
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
    
    

##  AIHubSpotMartingaleConfiguration

_AIHub 支持的已保存配置，不能替代全部高级原生配置。上游参数缺失时表示未核实。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
invest_amount | string | false | none | none  
investment_currency | string | false | none | none  
price_deviation | string | false | none | none  
take_profit_ratio | string | false | none | none  
stop_loss_per_cycle | string | false | none | 已保存的每轮比例，原样返回。历史值为 0 或负数时，不构成有效保护。  
trigger_price | string | false | none | none  
max_orders | integer(int32) | false | none | 已保存的最大追加建仓次数，不含首单，并非总订单数。  
      
    
    {
      "invest_amount": "string",
      "investment_currency": "string",
      "price_deviation": "string",
      "take_profit_ratio": "string",
      "stop_loss_per_cycle": "string",
      "trigger_price": "string",
      "max_orders": 0
    }
    
    

##  ContractMartingaleDirection

_合约马丁策略支持的方向枚举，和 App 原始接口保持一致。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | string | false | none | 合约马丁策略支持的方向枚举，和 App 原始接口保持一致。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
_None_ | buy  
_None_ | sell  
      
    
    "buy"
    
    

##  FuturesDirection

_合约类策略支持的方向枚举。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | string | false | none | 合约类策略支持的方向枚举。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
_None_ | long  
_None_ | short  
_None_ | neutral  
      
    
    "long"
    
    

##  AIHubStopProgress

_持久化事实的只读投影。字段缺失表示未核实。最终退款不包含普通减本金划转。不能根据已停止状态或空账户推断账户已释放。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
trading_finished | boolean | false | none | none  
funds_returned | boolean | false | none | none  
refund_amount | string | false | none | none  
refund_currency | string | false | none | none  
account_released | boolean | false | none | none  
      
    
    {
      "trading_finished": true,
      "funds_returned": true,
      "refund_amount": "string",
      "refund_currency": "string",
      "account_released": true
    }
    
    

##  AIHubFuturesComboAsset

_合约拼盘的单个合约成员。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
market | string | true | none | none  
side | string | true | none | none  
rate | string | true | none | 比例范围为 0.01–1，步长 0.01；所有成员权重之和为 1。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
side | buy  
side | sell  
      
    
    {
      "market": "string",
      "side": "buy",
      "rate": "string"
    }
    
    

##  AIHubPortfolioBaseInfo

_策略详情基础信息。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_name | string | true | none | none  
created_at | string | true | none | 创建时间  
running_duration | integer(int64) | true | none | 运行时长，单位秒  
invest_amount | string | true | none | none  
total_profit | string | true | none | none  
profit_rate | string | true | none | none  
      
    
    {
      "strategy_name": "string",
      "created_at": "string",
      "running_duration": 0,
      "invest_amount": "string",
      "total_profit": "string",
      "profit_rate": "string"
    }
    
    

##  MarginGridCreateParams

_杠杆网格策略的创建参数。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
money | string | true | none | none  
low_price | string | true | none | none  
high_price | string | true | none | none  
grid_num | integer(int32) | true | none | none  
price_type | integer(int32) | true | none | none  
leverage | string | true | none | none  
direction | FuturesDirection | false | none | 合约类策略支持的方向枚举。  
trigger_price | string | false | none | none  
stop_profit | string | false | none | none  
stop_loss | string | false | none | none  
profit_sharing_ratio | string | false | none | none  
is_use_base | boolean | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
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
    
    

##  AIHubRebalanceCreateParams

_智能调仓策略的创建参数。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
begin_money_amount | string | true | none | none  
begin_money_currency | string | true | none | none  
asset_info | [AIHubRebalanceAsset] | true | none | [智能调仓策略中的单个资产及目标比例。]  
period | string | false | none | 产品调仓周期，范围为 1m 至 28d。  
threshold | string | false | none | 大于 0 且小于 1 的比例，最多四位小数。  
close_flag | integer | false | none | none  
is_use_base | boolean | false | none | none  
stop_profit | string | false | none | none  
stop_loss | string | false | none | none  
  
_oneOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
  
_not_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
» _None_ | object | false | none | none  
  
_xor_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
  
_not_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
» _None_ | object | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
begin_money_currency | USDT  
close_flag | 0  
close_flag | 1  
      
    
    {}
    
    

##  AIHubPortfolioMetrics

_策略详情指标信息，按策略类型返回对应字段。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
grid_profit | string | false | none | none  
floating_pnl | string | false | none | none  
arbitrage_count | integer(int64) | false | none | none  
price_range | string | false | none | none  
grid_count | integer(int64) | false | none | none  
estimated_liquidation_price | string | false | none | none  
price_floor | string | false | none | none  
grid_profit_rate | string | false | none | none  
realized_pnl | string | false | none | none  
finished_rounds | integer(int64) | false | none | none  
avg_cost | string | false | none | none  
take_profit_price | string | false | none | none  
maintenance_margin_ratio | string | false | none | none  
      
    
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
    
    

##  AIHubRebalanceStopOptions

_智能调仓限价停止模式使用的参数。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
price | string | true | none | 产品支持的单个价格表达式，不是为每个成员分别指定表达式。  
expiration | integer(int64) | true | none | 有效时长，单位秒。到期后撤销委托并返还资产，不切换为市价。  
slip | string | false | none | 可选比例，范围为 0.001–0.05，最多六位小数。  
      
    
    {
      "price": "string",
      "expiration": 1,
      "slip": "string"
    }
    
    

##  AIHubContractMartingaleConfiguration

_AIHub 支持的已保存合约配置，不是完整的高级原生配置。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
invest_amount | string | false | none | none  
investment_currency | string | false | none | none  
price_deviation | string | false | none | none  
take_profit_ratio | string | false | none | none  
direction | string | false | none | none  
first_order_size | string | false | none | 产品快照中的精确十进制合约数量；空值表示未核实，不根据总预算推算。  
max_orders | integer(int64) | false | none | 最大追加建仓次数，不含首单。  
leverage | integer(int32) | false | none | none  
stop_loss_price_rule | AIHubMartingalePriceRule | false | none | 仅表示已保存的价格规则，不能证明订单已经执行。价格依据未知或价格非正数时，不构成有效保护。  
      
    
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
    
    

##  AIHubPortfolioRunningData

_运行中策略列表数据。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
items | [AIHubPortfolioRunningItem] | true | none | [运行中策略列表的一条记录。]  
page | integer(int32) | true | none | none  
page_size | integer(int32) | true | none | none  
total | integer(int32) | true | none | none  
      
    
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
    
    

##  AIHubPortfolioAssetPosition

_组合策略中单个资产或市场的仓位信息。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
asset | string | false | none | none  
market | string | false | none | none  
side | string | false | none | none  
amount | string | false | none | none  
amount_unit | string | false | none | none  
entry_price | string | false | none | none  
position_value | string | false | none | none  
position_value_unit | string | false | none | none  
target_weight | string | false | none | none  
leverage | string | false | none | none  
      
    
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
    
    

##  AIHubRebalanceAsset

_智能调仓策略中的单个资产及目标比例。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
asset | string | true | none | none  
rate | string | true | none | 保留两位小数，最小值 0.01；资产不得重复，比例之和必须恰好为 1。  
      
    
    {
      "asset": "string",
      "rate": "string"
    }
    
    

##  AIHubPortfolioPosition

_策略详情仓位信息，按策略类型返回对应字段。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
amount | string | false | none | none  
entry_price | string | false | none | none  
quote_amount | string | false | none | none  
position_value | string | false | none | none  
margin | string | false | none | none  
side | string | false | none | none  
      
    
    {
      "amount": "string",
      "entry_price": "string",
      "quote_amount": "string",
      "position_value": "string",
      "margin": "string",
      "side": "string"
    }
    
    

##  AIHubPortfolioStopData

_终止策略成功后返回的结果信息。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | false | none | none  
strategy_type | StrategyType | false | none | AIHub 支持的完整策略类型枚举。  
status | string | false | none | 观测到的产品生命周期状态，或 unknown。创建已受理或 starting 不等于 running；仅 stopping/finished 不能证明资金已结算。  
result_message | string | false | none | none  
operation_status | string | false | none | 写入结果需要核实时为 pending；已确认在产生副作用前拒绝时为 rejected。  
recovery_required | boolean | false | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "status": "string",
      "result_message": "string",
      "operation_status": "string",
      "recovery_required": true
    }
    
    

##  AIHubMartingalePriceRule

_仅表示已保存的价格规则，不能证明订单已经执行。价格依据未知或价格非正数时，不构成有效保护。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
price | string | false | none | none  
price_type | string | false | none | 原始枚举名称（last/index/mark/unknown）；未来出现未知枚举时返回其数字字符串。  
is_gte | boolean | false | none | none  
      
    
    {
      "price": "string",
      "price_type": "string",
      "is_gte": true
    }
    
    

##  AIHubPortfolioRunningItem

_运行中策略列表的一条记录。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | true | none | none  
strategy_type | StrategyType | true | none | AIHub 支持的完整策略类型枚举。  
strategy_name | string | true | none | none  
market | string | true | none | 单个市场；组合策略可为空字符串，此时使用 assets/markets。  
status | string | true | none | none  
pnl | string | false | none | none  
pnl_rate | string | false | none | none  
invest_amount | string | false | none | none  
created_at | string | false | none | 创建时间  
assets | array | false | none | none  
markets | array | false | none | none  
      
    
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