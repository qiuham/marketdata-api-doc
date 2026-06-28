---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/bot
api_type: REST
updated_at: 2026-05-27 20:16:50.343082
---

# Bot

* Python 
  * Shell 


Bot AIHub 策略推荐、创建、查询与终止接口

##  获取 AIHub 策略推荐🔒 需要认证

GET`/bot/strategy/recommend`

GET `/bot/strategy/recommend`

_获取 AIHub 策略推荐_

discover 域唯一正式接口。

支持场景：

  * `top1`
  * `bundle`
  * `filter`
  * `refresh`

约束：

  * 主动推荐池仅包含 `spot_grid`、`futures_grid`、`spot_martingale`
  * 可返回但不主动推荐 `infinite_grid`、`margin_grid`
  * 不得返回 `contract_martingale`、`smart-position`、`spot-future-arbitrage`
  * `scene=filter` 时只允许按 `market`、`backtest_apr_gte`、`max_drawdown_lte` 过滤
  * `scene=refresh` 通过 `refresh_recommendation_id` 承接刷新上下文；正式最小格式只要求 `strategy_type|market`
  * 若上游直接透传上一条推荐的 `recommendation_id`，其中第三段 `backtest_id` 当前会被忽略

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
market | 请求参数 | string | 否 | 交易对，例如 `BTC_USDT`  
strategy_type | 请求参数 | string | 否 | 推荐目标策略类型；`contract_martingale` 不允许  
direction | 请求参数 | string | 否 | 行情方向  
invest_amount | 请求参数 | string | 否 | 投入金额，字符串透传  
scene | 请求参数 | string | 否 | 推荐场景；为空时 bot-service 可按实现逻辑自动推断  
refresh_recommendation_id | 请求参数 | string | 否 | 推荐刷新上下文。`scene=refresh` 时使用；当 `scene` 为空但该字段存在时，bot-service 也会自动判定为 `refresh`。  
正式最小格式为 `strategy_type|market`；若直接透传上一条推荐的 `recommendation_id`，第三段 `backtest_id` 会被忽略。  
limit | 请求参数 | integer(int32) | 否 | 返回数量；`scene=filter` 时实际结果最多 10 条  
max_drawdown_lte | 请求参数 | string | 否 | 最大回撤上限  
backtest_apr_gte | 请求参数 | string | 否 | 回测年化下限  
X-Gate-Service-Id | 请求头部 | string | 否 | 调用来源标识；如有需要由 APIv4 注入  
X-Gate-AppLang | 请求头部 | string | 否 | 语言上下文，例如 `zh-CN` / `en-US`  
X-Request-Id | 请求头部 | string | 否 | 请求链路 ID；调用方可透传  
X-Trace-Id | 请求头部 | string | 否 | trace header；可由 APIv4 统一生成  
  
####  详细描述

**refresh_recommendation_id** : 推荐刷新上下文。`scene=refresh` 时使用；当 `scene` 为空但该字段存在时，bot-service 也会自动判定为 `refresh`。  
正式最小格式为 `strategy_type|market`；若直接透传上一条推荐的 `recommendation_id`，第三段 `backtest_id` 会被忽略。

####  枚举值列表

枚举值列表参数 | 值  
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
      "trace_id": "string"
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
» data | AIHubCreateData | 创建策略成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 创建成功后的初始状态，通常为 `running`  
»» jump_url | string |   
» trace_id | string |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
        "jump_url": "string"
      },
      "trace_id": "string"
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
» data | AIHubCreateData | 创建策略成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 创建成功后的初始状态，通常为 `running`  
»» jump_url | string |   
» trace_id | string |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
        "jump_url": "string"
      },
      "trace_id": "string"
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
» data | AIHubCreateData | 创建策略成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 创建成功后的初始状态，通常为 `running`  
»» jump_url | string |   
» trace_id | string |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
        "jump_url": "string"
      },
      "trace_id": "string"
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
» data | AIHubCreateData | 创建策略成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 创建成功后的初始状态，通常为 `running`  
»» jump_url | string |   
» trace_id | string |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
        "jump_url": "string"
      },
      "trace_id": "string"
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
» data | AIHubCreateData | 创建策略成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 创建成功后的初始状态，通常为 `running`  
»» jump_url | string |   
» trace_id | string |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
        "jump_url": "string"
      },
      "trace_id": "string"
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
»» invest_amount | body | string | 是 | 投入保证金金额；服务端会按实时合约价格、合约乘数和最小下单单位自动换算首单张数。  
»» price_deviation | body | string | 是 |   
»» max_orders | body | integer(int32) | 是 |   
»» take_profit_ratio | body | string | 是 |   
»» direction | body | ContractMartingaleDirection | 是 | 合约马丁策略支持的方向枚举，和 App 原始接口保持一致。  
»» leverage | body | string | 是 |   
»» stop_loss_price | body | string | 否 | 历史字段名。当前 AIHub `contract_martingale` 创建路径未映射该字段；  
合约止损规则以合约马丁底层接口为准。MCP 工具请以 bot-service 实现为准。  
»» profit_sharing_ratio | body | string | 否 |   
  
####  详细描述

**»» stop_loss_price** : 历史字段名。当前 AIHub `contract_martingale` 创建路径未映射该字段；  
合约止损规则以合约马丁底层接口为准。MCP 工具请以 bot-service 实现为准。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» strategy_type | contract_martingale  
»» direction | buy  
»» direction | sell  
  
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
» data | AIHubCreateData | 创建策略成功后返回的策略信息。  
»» strategy_id | string |   
»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»» market | string |   
»» status | string | 创建成功后的初始状态，通常为 `running`  
»» jump_url | string |   
» trace_id | string |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    body='{"strategy_type":"contract_martingale","market":"string","create_params":{"invest_amount":"string","price_deviation":"string","max_orders":1,"take_profit_ratio":"string","direction":"buy","leverage":"string","stop_loss_price":"string","profit_sharing_ratio":"string"}}'
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
    body_param='{"strategy_type":"contract_martingale","market":"string","create_params":{"invest_amount":"string","price_deviation":"string","max_orders":1,"take_profit_ratio":"string","direction":"buy","leverage":"string","stop_loss_price":"string","profit_sharing_ratio":"string"}}'
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
        "jump_url": "string"
      },
      "trace_id": "string"
    }
    

##  查询运行中策略列表🔒 需要认证

GET`/bot/portfolio/running`

GET `/bot/portfolio/running`

_查询运行中策略列表_

查询当前用户运行中的 AIHub 策略列表，支持按策略类型、交易对和分页条件过滤。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
strategy_type | 请求参数 | string | 否 | 按策略类型过滤  
market | 请求参数 | string | 否 | 按交易对过滤  
page | 请求参数 | integer(int32) | 否 | 页码，默认 1  
page_size | 请求参数 | integer(int32) | 否 | 分页大小，默认 20，最大 50  
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
»» items | array | [运行中策略列表中的单条记录。]  
»»» _None_ | AIHubPortfolioRunningItem | 运行中策略列表中的单条记录。  
»»»» strategy_id | string |   
»»»» strategy_type | StrategyType | AIHub 支持的完整策略类型枚举。  
»»»» strategy_name | string |   
»»»» market | string |   
»»»» status | string |   
»»»» pnl | string |   
»»»» pnl_rate | string |   
»»»» invest_amount | string |   
»»»» created_at | string | 创建时间  
»»» page | integer(int32) |   
»»» page_size | integer(int32) |   
»»» total | integer(int32) |   
»» trace_id | string |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
      "trace_id": "string"
    }
    

##  查询单策略详情🔒 需要认证

GET`/bot/portfolio/detail`

GET `/bot/portfolio/detail`

_查询单策略详情_

请求中必须同时传 `strategy_id` 与 `strategy_type`，其中 `strategy_type` 用于按策略类型分发到底层详情实现。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
strategy_id | 请求参数 | string | 是 | 策略 ID  
strategy_type | 请求参数 | string | 是 | 策略类型；用于底层详情分发  
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
»» market | string |   
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
» trace_id | string |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
        "stop_supported": true
      },
      "trace_id": "string"
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
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» strategy_type | spot_grid  
» strategy_type | margin_grid  
» strategy_type | infinite_grid  
» strategy_type | futures_grid  
» strategy_type | spot_martingale  
» strategy_type | contract_martingale  
  
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
»» status | string | 当前实现返回 `stopping`  
»» result_message | string |   
» trace_id | string |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
strategy_type | spot_grid  
strategy_type | margin_grid  
strategy_type | infinite_grid  
strategy_type | futures_grid  
strategy_type | spot_martingale  
strategy_type | contract_martingale  
  
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
    body='{"strategy_id":"string","strategy_type":"spot_grid"}'
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
    body_param='{"strategy_id":"string","strategy_type":"spot_grid"}'
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
      "strategy_type": "spot_grid"
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
        "result_message": "string"
      },
      "trace_id": "string"
    }
    

#  模型

##  AIHubCreateSuccessResponse

_创建策略成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubCreateData | true | none | 创建策略成功后返回的策略信息。  
trace_id | string | true | none | none  
      
    
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
    
    

##  AIHubPortfolioDetailSuccessResponse

_查询策略详情成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubPortfolioDetailData | true | none | 策略详情数据。  
trace_id | string | true | none | none  
      
    
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
    
    

##  AIHubPortfolioRunningSuccessResponse

_查询运行中策略列表成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubPortfolioRunningData | true | none | 运行中策略列表数据。  
trace_id | string | true | none | none  
      
    
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
    
    

##  AIHubPortfolioStopSuccessResponse

_终止策略成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubPortfolioStopData | true | none | 终止策略成功后返回的结果信息。  
trace_id | string | true | none | none  
      
    
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
    
    

##  AIHubPortfolioStopData

_终止策略成功后返回的结果信息。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | true | none | none  
strategy_type | StrategyType | true | none | AIHub 支持的完整策略类型枚举。  
status | string | true | none | 当前实现返回 `stopping`  
result_message | string | true | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "status": "string",
      "result_message": "string"
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
    
    

##  AIHubPortfolioStopRequest

_终止运行中策略的请求体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | true | none | none  
strategy_type | StrategyType | true | none | AIHub 支持的完整策略类型枚举。  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid"
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
    
    

##  AIHubDiscoverSuccessResponse

_获取策略推荐成功时的响应体。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer(int32) | true | none | none  
message | string | true | none | none  
data | AIHubDiscoverData | true | none | 策略推荐结果数据。  
trace_id | string | true | none | none  
      
    
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
    
    

##  AIHubPortfolioDetailData

_策略详情数据。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | true | none | none  
strategy_type | StrategyType | true | none | AIHub 支持的完整策略类型枚举。  
market | string | true | none | none  
status | string | true | none | none  
base_info | AIHubPortfolioBaseInfo | true | none | 策略详情基础信息。  
metrics | AIHubPortfolioMetrics | true | none | 策略详情指标信息，按策略类型返回对应字段。  
position | AIHubPortfolioPosition | false | none | 策略详情仓位信息，按策略类型返回对应字段。  
stop_supported | boolean | true | none | none  
      
    
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
      
    
    "spot_grid"
    
    

##  AIHubCreateData

_创建策略成功后返回的策略信息。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | true | none | none  
strategy_type | StrategyType | true | none | AIHub 支持的完整策略类型枚举。  
market | string | true | none | none  
status | string | true | none | 创建成功后的初始状态，通常为 `running`  
jump_url | string | false | none | none  
      
    
    {
      "strategy_id": "string",
      "strategy_type": "spot_grid",
      "market": "string",
      "status": "string",
      "jump_url": "string"
    }
    
    

##  AIHubPortfolioRunningData

_运行中策略列表数据。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
items | [AIHubPortfolioRunningItem] | true | none | [运行中策略列表中的单条记录。]  
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
          "created_at": "string"
        }
      ],
      "page": 0,
      "page_size": 0,
      "total": 0
    }
    
    

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
    
    

##  AIHubPortfolioRunningItem

_运行中策略列表中的单条记录。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
strategy_id | string | true | none | none  
strategy_type | StrategyType | true | none | AIHub 支持的完整策略类型枚举。  
strategy_name | string | true | none | none  
market | string | true | none | none  
status | string | true | none | none  
pnl | string | false | none | none  
pnl_rate | string | false | none | none  
invest_amount | string | false | none | none  
created_at | string | false | none | 创建时间  
      
    
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
        "profit_sharing_ratio": "string"
      }
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
    
    

##  ContractMartingaleCreateParams

_合约马丁策略的创建参数。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
invest_amount | string | true | none | 投入保证金金额；服务端会按实时合约价格、合约乘数和最小下单单位自动换算首单张数。  
price_deviation | string | true | none | none  
max_orders | integer(int32) | true | none | none  
take_profit_ratio | string | true | none | none  
direction | ContractMartingaleDirection | true | none | 合约马丁策略支持的方向枚举，和 App 原始接口保持一致。  
leverage | string | true | none | none  
stop_loss_price | string | false | none | 历史字段名。当前 AIHub `contract_martingale` 创建路径未映射该字段；  
合约止损规则以合约马丁底层接口为准。MCP 工具请以 bot-service 实现为准。  
profit_sharing_ratio | string | false | none | none  
      
    
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