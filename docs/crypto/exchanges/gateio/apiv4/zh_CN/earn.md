---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/earn
api_type: Earn
updated_at: 2026-05-27 20:17:04.566663
---

# Earn

理财服务

##  双币理财产品列表

GET`/earn/dual/investment_plan`

GET `/earn/dual/investment_plan`

_双币理财产品列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
plan_id | 请求参数 | integer(int64) | 否 | 理财项目id  
coin | 请求参数 | string | 否 | 投资币种  
type | 请求参数 | string | 否 | 类型枚举：put 低买，call 高卖  
quote_currency | 请求参数 | string | 否 | 结算币种枚举：默认USDT，可选GUSD  
sort | 请求参数 | string | 否 | 排序字段枚举：  
apy-收益从高到低  
short-period-周期由短到长  
multiple-溢价由高到低  
page | 请求参数 | integer | 否 | 页码  
page_size | 请求参数 | integer | 否 | 每页条数  
  
####  详细描述

**sort** : 排序字段枚举：  
apy-收益从高到低  
short-period-周期由短到长  
multiple-溢价由高到低

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | [DualGetPlans]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | integer(int32) | 项目ID  
» instrument_name | string | 项目名称  
» invest_currency | string | 投资币种  
» exercise_currency | string | 行权币种  
» exercise_price | number(double) | 行权价格  
» delivery_time | integer(int32) | 结算时间  
» apy_display | string | 年化收益率  
» min_amount | string | 最小投资金额  
» start_time | integer(int32) | 开始时间  
» end_time | integer(int32) | 结束时间  
» status | string | 状态:  
  
`NOTSTARTED`-未开始  
`ONGOING`-进行中  
`ENDED`-已结束  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/dual/investment_plan'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/dual/investment_plan \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": 272,
        "instrument_name": "DOGE-17NOV23-0.067-P",
        "type": "put",
        "invest_currency": "USDT",
        "exercise_currency": "DOGE",
        "exercise_price": 0.067,
        "delivery_time": 1700208000,
        "start_time": 1697685172,
        "end_time": 1697685172,
        "status": "ONGOING",
        "apy_display": "0.0114000000",
        "min_amount": "1"
      }
    ]
    

##  双币理财订单列表🔒 需要认证

GET`/earn/dual/orders`

GET `/earn/dual/orders`

_双币理财订单列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
from | 请求参数 | integer(int64) | 否 | 开始结算时间  
to | 请求参数 | integer(int64) | 否 | 结束结算时间  
type | 请求参数 | string | 否 | 类型枚举：put 低买，call 高卖  
status | 请求参数 | string | 否 | 订单状态枚举：  
HOLD-持仓  
REPAY-历史持仓  
PROCESSING-持仓中  
SETTLEMENT_PROCESSING-结算中  
ALL-全部  
coin | 请求参数 | string | 否 | 投资币种  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
  
####  详细描述

**status** : 订单状态枚举：  
HOLD-持仓  
REPAY-历史持仓  
PROCESSING-持仓中  
SETTLEMENT_PROCESSING-结算中  
ALL-全部

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | [DualGetOrders]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | integer(int32) | 订单ID  
» plan_id | integer(int32) | 项目ID  
» invest_amount | string | 投资数量  
» settlement_amount | string | 结算数量  
» create_time | integer(int32) | 创建时间  
» complete_time | integer(int32) | 完成时间  
» status | string | 状态:  
  
`INIT`-创建  
`SETTLEMENT_SUCCESS`-结算成功  
`SETTLEMENT_PROCESSING`-结算中  
`CANCELED`-取消  
`FAILED`-失败  
» invest_currency | string | 投资币种  
» exercise_currency | string | 行权币种  
» exercise_price | string | 行权价格  
» settlement_price | string | 结算价格  
» settlement_currency | string | 结算币种  
» apy_display | string | 年化收益率  
» apy_settlement | string | 结算年化收益率  
» delivery_time | integer(int32) | 结算时间  
» text | string | 订单自定义信息  
  
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
    
    url = '/earn/dual/orders'
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
    url="/earn/dual/orders"
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
    
    
    [
      {
        "id": 373,
        "plan_id": 176,
        "invest_amount": "0.0000000000",
        "settlement_amount": "0.0000000000",
        "create_time": 1697685172,
        "complete_time": 1697685172,
        "status": "CANCELED",
        "invest_currency": "USDT",
        "exercise_currency": "BTC",
        "settlement_currency": "",
        "exercise_price": "24500.0000000000",
        "settlement_price": "0.0000000000",
        "delivery_time": 1697685172,
        "apy_display": "0.6800000000",
        "apy_settlement": "0.0000000000",
        "text": "t-custom-text"
      }
    ]
    

##  双币理财下单🔒 需要认证

POST`/earn/dual/orders`

POST `/earn/dual/orders`

_双币理财下单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | PlaceDualInvestmentOrderParams | 是 |   
» plan_id | body | string | 是 | 项目ID  
» amount | body | string | 是 | 申购金额  
» text | body | string | 否 | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
####  详细描述

**» text** : 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 下单成功 | PlaceDualInvestmentOrder  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» id | integer(int32) | 订单ID  
» plan_id | integer(int32) | 项目ID  
» invest_amount | string | 投资数量  
» settlement_amount | string | 结算数量  
» create_time | integer(int32) | 创建时间  
» complete_time | integer(int32) | 完成时间  
» status | string | 状态:  
  
`INIT`-创建  
`SETTLEMENT_SUCCESS`-结算成功  
`SETTLEMENT_PROCESSING`-结算中  
`CANCELED`-取消  
`FAILED`-失败  
» invest_currency | string | 投资币种  
» exercise_currency | string | 行权币种  
» exercise_price | string | 行权价格  
» settlement_price | string | 结算价格  
» settlement_currency | string | 结算币种  
» apy_display | string | 年化收益率  
» apy_settlement | string | 结算年化收益率  
» delivery_time | integer(int32) | 结算时间  
» text | string | 订单自定义信息  
  
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
    
    url = '/earn/dual/orders'
    query_param = ''
    body='{"plan_id":"176","amount":"1","text":"t-custom-text"}'
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
    url="/earn/dual/orders"
    query_param=""
    body_param='{"plan_id":"176","amount":"1","text":"t-custom-text"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "plan_id": "176",
      "amount": "1",
      "text": "t-custom-text"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": 373,
      "plan_id": 176,
      "invest_amount": "0.0000000000",
      "settlement_amount": "0.0000000000",
      "create_time": 1697685172,
      "complete_time": 1697685172,
      "status": "CANCELED",
      "invest_currency": "USDT",
      "exercise_currency": "BTC",
      "settlement_currency": "",
      "exercise_price": "24500.0000000000",
      "settlement_price": "0.0000000000",
      "delivery_time": 1697685172,
      "apy_display": "0.6800000000",
      "apy_settlement": "0.0000000000",
      "text": "t-custom-text"
    }
    

##  双币理财资产🔒 需要认证

GET`/earn/dual/balance`

GET `/earn/dual/balance`

_双币理财资产_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | DualGetBalance  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» user_asset_usdt | string | 用户资产折U  
» user_asset_btc | string | 用户资产折BTC  
» user_total_interest_usdt | string | 用户总利息折U  
» user_total_interest_btc | string | 用户总利息折BTC  
  
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
    
    url = '/earn/dual/balance'
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
    url="/earn/dual/balance"
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
      "user_asset_usdt": "30.13",
      "user_asset_btc": "0.00032798",
      "user_total_interest_usdt": "581.19003892",
      "user_total_interest_btc": "0.00632655"
    }
    

##  双币提前赎回预览🔒 需要认证

GET`/earn/dual/order-refund-preview`

GET `/earn/dual/order-refund-preview`

_双币提前赎回预览_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | 请求参数 | string | 是 | 订单ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | DualOrderRefundPreview  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» create_timest | integer(int64) | 订单创建时间戳  
» delivery_timest | integer(int64) | 订单交付时间戳  
» exercise_price | string | 行权价格  
» invest_amount | string | 投资金额  
» invest_currency | string | 投资币种  
» name | string | 订单名称标识  
» order_id | integer(int64) | 订单ID  
» req_id | string | 请求ID，用于实际赎回  
» refund_service_charge | integer(int64) | 退款手续费  
» settle_price | string | 结算价格  
» settlement_amount | string | 结算金额  
» settlement_currency | string | 结算币种  
» settlement_interest | string | 结算利息  
» settlement_principle | string | 结算本金  
» type | string | call: 高卖 put: 低买  
» money_back_timest | integer(int64) | 赎回时间  
  
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
    
    url = '/earn/dual/order-refund-preview'
    query_param = 'order_id=9497'
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
    url="/earn/dual/order-refund-preview"
    query_param="order_id=9497"
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
      "create_timest": 1775027285,
      "delivery_timest": 1775289600,
      "exercise_price": "71303.44279",
      "invest_amount": "1",
      "invest_currency": "BTC",
      "name": "BTC_USDT-20260404-71303.44279-C",
      "order_id": 9497,
      "req_id": "tIvdY7nh",
      "refund_service_charge": 0,
      "settle_price": "68781.0063",
      "settlement_amount": "0.99486528",
      "settlement_currency": "BTC",
      "settlement_interest": "0",
      "settlement_principle": "0.99486528",
      "type": "call",
      "money_back_timest": 1775027958
    }
    

##  双币订单提前赎回🔒 需要认证

POST`/earn/dual/order-refund`

POST `/earn/dual/order-refund`

_双币订单提前赎回_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | DualOrderRefundParams | 是 |   
» order_id | body | string | 是 | 订单ID  
» req_id | body | string | 是 | 请求ID，由order-refund-preview返回  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 赎回成功 | 无  
  
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
    
    url = '/earn/dual/order-refund'
    query_param = ''
    body='{"order_id":"9487","req_id":"OepRSEfv"}'
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
    url="/earn/dual/order-refund"
    query_param=""
    body_param='{"order_id":"9487","req_id":"OepRSEfv"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "order_id": "9487",
      "req_id": "OepRSEfv"
    }
    

##  双币订单复投修改🔒 需要认证

POST`/earn/dual/modify-order-reinvest`

POST `/earn/dual/modify-order-reinvest`

_双币订单复投修改_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | DualModifyOrderReinvestParams | 是 |   
» order_id | body | integer(int64) | 否 | 订单ID  
» status | body | integer(int32) | 否 | 0: 关闭 1: 开启  
» effective_time_duration | body | integer(int64) | 否 | 生效时长(秒)，默认1天(86400)  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 修改成功 | 无  
  
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
    
    url = '/earn/dual/modify-order-reinvest'
    query_param = ''
    body='{"order_id":9497,"status":1,"effective_time_duration":86400}'
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
    url="/earn/dual/modify-order-reinvest"
    query_param=""
    body_param='{"order_id":9497,"status":1,"effective_time_duration":86400}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "order_id": 9497,
      "status": 1,
      "effective_time_duration": 86400
    }
    

##  双币-推荐项目🔒 需要认证

GET`/earn/dual/project-recommend`

GET `/earn/dual/project-recommend`

_双币-推荐项目_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
mode | 请求参数 | string | 否 | 排序模式，默认normal  
senior: 资深推荐(APR/期限择优)  
apy_up: apy升序  
ep_down: 目标价格降序  
ep_up: 目标价格升序  
dt_down: 到期时间降序  
dt_up: 到期时间升序  
coin | 请求参数 | string | 否 | 投资币种  
type | 请求参数 | string | 否 | call: 高卖 put: 低买  
history_pids | 请求参数 | string | 否 | 逗号分隔的项目ID，用于过滤已推荐过的  
  
####  详细描述

**mode** : 排序模式，默认normal  
senior: 资深推荐(APR/期限择优)  
apy_up: apy升序  
ep_down: 目标价格降序  
ep_up: 目标价格升序  
dt_down: 到期时间降序  
dt_up: 到期时间升序

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | [DualProjectRecommend]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | integer(int64) | 项目ID  
» category | integer(int32) | 策略类别  
» type | string | call: 高卖 put: 低买  
» invest_currency | string | 投资币种  
» exercise_currency | string | 行权币种  
» apy_display | string | 年化收益率  
» exercise_price | string | 行权价格  
» delivery_timest | integer(int64) | 结算时间  
» min_amount | string | 最小投资金额  
» max_amount | string | 最大投资金额  
» min_copies | integer(int64) | 最小份数  
» max_copies | integer(int64) | 最大份数  
» invest_days | integer(int64) | 锁仓天数  
» invest_hours | string | 锁仓小时数  
  
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
    
    url = '/earn/dual/project-recommend'
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
    url="/earn/dual/project-recommend"
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
    
    
    [
      {
        "id": 110669,
        "category": 1,
        "type": "call",
        "invest_currency": "BTC",
        "exercise_currency": "USDT",
        "apy_display": "2.60",
        "exercise_price": "71303.44279",
        "delivery_timest": 1775289600,
        "min_amount": "1",
        "max_amount": "100000",
        "min_copies": 1,
        "max_copies": 100000,
        "invest_days": 2,
        "invest_hours": "70.43458031"
      }
    ]
    

##  链上赚币币种🔒 需要认证

GET`/earn/staking/coins`

GET `/earn/staking/coins`

_链上赚币币种_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
cointype | 请求参数 | string | 否 | 币种类型 swap-凭证 lock-锁仓 debt-美债  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» pid | integer | 项目ID  
» productType | integer | 项目类型 0-凭证 1-锁仓 2-美债  
» isDefi | integer | 是否DEFI协议 0-否 1-是  
» currency | string | 质押币种多个逗号分隔  
» estimateApr | string | 预估收益率  
» minStakeAmount | string | 最小质押量  
» maxStakeAmount | string | 最大质押量  
» protocolName | string | 协议名  
» redeemPeriod | string | 赎回期(天)  
» exchangeRate | string | 兑换率  
» exchangeRateReserve | string | 反向兑换率  
» extraInterest | array | 额外奖励  
»» start_time | string | 开始时间戳  
»» end_time | string | 结束时间戳  
»» reward_coin | string | 额外奖励币种  
»» segment_interest | array | 分段奖励信息  
»»» money_min | string | 分段小值  
»»» money_max | string | 分段大值  
»»» money_rate | string | 分段利率  
»» currencyRewards | array | 奖励币种信息  
»»» apr | string | 基础利率  
»»» reward_coin | string | 奖励币种  
»»» reward_delay_days | string | 派息天 -1表示赎回时派息  
»»» interest_delay_days | string | 起息天  
  
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
    
    url = '/earn/staking/coins'
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
    url="/earn/staking/coins"
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
    
    
    [
      {
        "pid": 1,
        "productType": 0,
        "isDefi": 0,
        "currency": "GT",
        "estimateApr": "36.00",
        "minStakeAmount": "1",
        "maxStakeAmount": 700,
        "protocolName": "Gatechain",
        "redeemPeriod": 0,
        "exchangeRate": "1.00000000",
        "exchangeRateReserve": "1.00000000",
        "extraInterest": [
          {
            "start_time": 1749427201,
            "end_time": 1765497600,
            "reward_coin": "GT",
            "segment_interest": [
              {
                "money_min": "0",
                "money_max": "1000",
                "money_rate": "10.00"
              },
              {
                "money_min": "1000",
                "money_max": "2000",
                "money_rate": "15.00"
              },
              {
                "money_min": "2000",
                "money_max": "3000",
                "money_rate": "30.00"
              }
            ]
          }
        ],
        "currencyRewards": [
          {
            "apr": "6.00",
            "reward_coin": "GT2",
            "reward_delay_days": 1,
            "interest_delay_days": 1
          }
        ]
      }
    ]
    

##  链上赚币兑换🔒 需要认证

POST`/earn/staking/swap`

POST `/earn/staking/swap`

_链上赚币兑换_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | SwapCoin | 是 |   
» coin | body | string | 是 | 币种  
» side | body | integer | 是 | 0-质押, 1-赎回  
» amount | body | string | 是 | 数量  
» pid | body | integer | 否 | DEFI类挖矿协议ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 兑换成功 | SwapCoinStruct  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» id | integer | 订单ID  
» pid | integer | 项目ID  
» uid | integer | 用户ID  
» coin | string | 币种  
» type | integer | 类型 0-质押 1-赎回  
» subtype | string | 子类型  
» amount | string | 金额  
» exchange_rate | string | 兑换比例  
» exchange_amount | string | 兑换金额  
» updateStamp | integer | 更新时间戳  
» createStamp | integer | 交易时间戳  
» status | integer | 状态 1-成功  
» protocol_type | integer | DEFI协议类型  
» client_order_id | string | 参考ID  
» source | string | 订单来源  
  
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
    
    url = '/earn/staking/swap'
    query_param = ''
    body='{"coin":"GT","side":"0","amount":"1.5"}'
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
    url="/earn/staking/swap"
    query_param=""
    body_param='{"coin":"GT","side":"0","amount":"1.5"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "coin": "GT",
      "side": "0",
      "amount": "1.5"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": 21000,
      "uid": 12345,
      "coin": "GT",
      "type": 0,
      "exchange_rate": "1.00000000",
      "amount": "2",
      "pid": 1,
      "status": 1,
      "createStamp": 1752200661
    }
    

##  链上赚币订单列表🔒 需要认证

GET`/earn/staking/order_list`

GET `/earn/staking/order_list`

_链上赚币订单列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
pid | 请求参数 | integer | 否 | 项目ID  
coin | 请求参数 | string | 否 | 币种名称  
type | 请求参数 | integer | 否 | 类型 0质押 1赎回  
page | 请求参数 | integer(int32) | 否 | 列表页数  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | OrderListStruct  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» page | integer | 页  
» pageSize | integer | 每页条数  
» pageCount | integer | 总页数  
» totalCount | integer | 总条数  
» list | array |   
»» pid | integer | 项目ID  
»» coin | string | 质押赎回币种  
»» amount | string | 金额  
»» type | integer | 类型 0-质押 1-赎回  
»» status | integer | 状态  
»» redeem_stamp | integer | 赎回到账时间  
»» createStamp | integer | 订单时间  
»» exchange_amount | string | 兑换汇率  
»» fee | string | 手续费  
  
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
    
    url = '/earn/staking/order_list'
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
    url="/earn/staking/order_list"
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
      "page": 1,
      "pageSize": 20,
      "pageCount": 5,
      "totalCount": 90,
      "list": [
        {
          "pid": 2,
          "coin": "SOL",
          "amount": "1.00000000",
          "type": 0,
          "status": 1,
          "redeem_stamp": 0,
          "createStamp": 1756105456,
          "exchange_amount": "1.00000000",
          "fee": "0.0000000000"
        },
        {
          "pid": 2,
          "coin": "SOL",
          "amount": "1.00000000",
          "type": 0,
          "status": 1,
          "redeem_stamp": 0,
          "createStamp": 1755588122,
          "exchange_amount": "0.80000000",
          "fee": "0.0000000000"
        }
      ]
    }
    

##  链上赚币派息记录🔒 需要认证

GET`/earn/staking/award_list`

GET `/earn/staking/award_list`

_链上赚币派息记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
pid | 请求参数 | integer | 否 | 项目ID  
coin | 请求参数 | string | 否 | 币种名称  
page | 请求参数 | integer(int32) | 否 | 列表页数  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | AwardListStruct  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» page | integer | 页  
» pageSize | integer | 每页条数  
» pageCount | integer | 总页数  
» totalCount | integer | 总条数  
» list | array |   
»» pid | integer | 项目ID  
»» mortgage_coin | string | 质押币种  
»» amount | string | 金额  
»» reward_coin | string | 奖励币种  
»» interest | string | 利息金额  
»» fee | string | 手续费  
»» status | integer | 状态  
»» bonus_date | string | 日期  
»» should_bonus_stamp | integer | 应派发时间戳  
  
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
    
    url = '/earn/staking/award_list'
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
    url="/earn/staking/award_list"
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
      "page": 1,
      "pageSize": 20,
      "pageCount": 2,
      "totalCount": 33,
      "list": [
        {
          "pid": 64,
          "mortgage_coin": "USDT",
          "amount": "0.0000019100",
          "reward_coin": "COMP",
          "interest": "0.0000019100",
          "fee": "0.0000000700",
          "status": 4,
          "bonus_date": "2025-08-08 00:00:00",
          "should_bonus_stamp": 1755907200
        },
        {
          "pid": 27,
          "mortgage_coin": "DOT",
          "amount": "0.0023424700",
          "reward_coin": "DOT",
          "interest": "0.0023424700",
          "fee": "0.0001232800",
          "status": 4,
          "bonus_date": "2025-08-11 00:00:00",
          "should_bonus_stamp": 1755043200
        }
      ]
    }
    

##  链上赚币资产🔒 需要认证

GET`/earn/staking/assets`

GET `/earn/staking/assets`

_链上赚币资产_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
coin | 请求参数 | string | 否 | 币种名称  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» pid | integer | 项目ID  
» mortgage_coin | string | 质押币种多个逗号分隔  
» mortgage_amount | string | 持仓金额  
» createStamp | integer | 首次时间戳  
» extra_income | string | 额外奖励折U金额  
» freeze_amount | string | 冻结金额  
» move_income | string |   
» type | integer | 类型 0-凭证 1-锁仓 2-美债  
» status | integer | 状态  
» income_total | string | 币种总收益  
» yesterday_income_multi | array | 昨日收益  
» reward_coins | array | 币种奖励收益  
»» reward_coin | string | 奖励币种  
»» interest_delay_days | integer | 起息天  
»» reward_delay_days | integer | 派息天 -1表示赎回时派息  
» defi_income | object | DEIF收益  
»» total | array |   
»»» coin | string |   
»»» amount | string |   
  
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
    
    url = '/earn/staking/assets'
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
    url="/earn/staking/assets"
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
    
    
    [
      {
        "pid": 1,
        "mortgage_coin": "GT",
        "mortgage_amount": "111.60000000",
        "createStamp": 1728530266,
        "extra_income": "0",
        "freeze_amount": "0.0000000000",
        "move_income": "0.0000000000",
        "type": 0,
        "status": 1,
        "income_total": "0",
        "yesterday_income_multi": [],
        "reward_coins": [
          {
            "reward_coin": "GT2",
            "interest_delay_days": 1,
            "reward_delay_days": 1
          }
        ]
      },
      {
        "pid": 64,
        "mortgage_coin": "USDT",
        "mortgage_amount": "1.0000000000",
        "createStamp": 1750764156,
        "extra_income": "0",
        "freeze_amount": "0.0000000000",
        "move_income": "0.0000000000",
        "type": 1,
        "status": 1,
        "income_total": "0",
        "yesterday_income_multi": [],
        "defi_income": {
          "total": [
            {
              "coin": "COMP",
              "amount": "0.0000076200"
            }
          ]
        },
        "reward_coins": [
          {
            "reward_coin": "USDT",
            "interest_delay_days": 1,
            "reward_delay_days": -1
          },
          {
            "reward_coin": "COMP",
            "interest_delay_days": 1,
            "reward_delay_days": 15
          }
        ]
      }
    ]
    

##  创建定投计划🔒 需要认证

POST`/earn/autoinvest/plans/create`

POST `/earn/autoinvest/plans/create`

_创建定投计划_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AutoInvestPlanCreate | 是 |   
» plan_name | body | string | 否 | 计划名称。长度 0~50 字符  
» plan_des | body | string | 否 | 计划描述  
» plan_money | body | string | 是 | 计价货币，支持USDT，BTC  
» plan_amount | body | string | 是 | 每期定投金额，须 > 0，且不超过该计价货币配置的单笔最大金额  
» plan_period_type | body | string | 是 | 枚举 daily、weekly、biweekly、monthly、hourly、4-hourly  
» plan_period_day | body | integer(int64) | 是 | 周期日。monthly 时表示每月第几天 1~30；weekly/biweekly 时表示周几 1~7（1=周一）；daily/hourly/4-hourly 时忽略  
» plan_period_hour | body | integer(int64) | 是 | 几点执行定投 0-23  
» items | body | array | 是 | 投资组合，不可重复 asset；所有项的 ratio 之和须为 100  
»» asset | body | string | 是 | 投资币种，如 BTC；需为已启用且市场存在；同一 plan 内不可重复  
»» ratio | body | string | 是 | 该币种在组合中的占比，所有 items 的 ratio 之和必须为100  
» fund_source | body | string | 否 | 资金来源 spot 或 earn，默认 spot  
» fund_flow | body | string | 否 | 资金流向 auto_invest 或 earn，默认 auto_invest  
» type | body | integer(int64) | 否 | 0 普通创建, 1 快速投资  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 创建成功 | AutoInvestPlanCreateResp  
  
### 返回格式

状态码 **200**

_创建定投计划响应_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 计划ID  
» amount | string | 每期定投金额  
» money | string | 计价货币  
» next_time | integer(int64) | 下次执行时间  
» period_type | string | 周期类型  
» period_day | integer(int64) | 周期日  
» period_hour | integer(int64) | 周期小时  
» fund_flow | string | 资金流向  
» fund_source | string | 资金来源  
  
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
    
    url = '/earn/autoinvest/plans/create'
    query_param = ''
    body='{"plan_name":"","plan_des":"","plan_period_type":"monthly","plan_period_day":1,"plan_period_hour":1,"plan_money":"USDT","plan_amount":"100","type":0,"items":[{"asset":"BTC","ratio":"33"},{"asset":"GT","ratio":"33"},{"asset":"ETH","ratio":"34"}],"fund_source":"spot","fund_flow":"auto_invest"}'
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
    url="/earn/autoinvest/plans/create"
    query_param=""
    body_param='{"plan_name":"","plan_des":"","plan_period_type":"monthly","plan_period_day":1,"plan_period_hour":1,"plan_money":"USDT","plan_amount":"100","type":0,"items":[{"asset":"BTC","ratio":"33"},{"asset":"GT","ratio":"33"},{"asset":"ETH","ratio":"34"}],"fund_source":"spot","fund_flow":"auto_invest"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "plan_name": "",
      "plan_des": "",
      "plan_period_type": "monthly",
      "plan_period_day": 1,
      "plan_period_hour": 1,
      "plan_money": "USDT",
      "plan_amount": "100",
      "type": 0,
      "items": [
        {
          "asset": "BTC",
          "ratio": "33"
        },
        {
          "asset": "GT",
          "ratio": "33"
        },
        {
          "asset": "ETH",
          "ratio": "34"
        }
      ],
      "fund_source": "spot",
      "fund_flow": "auto_invest"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": 142579,
      "amount": "9",
      "money": "USDT",
      "next_time": 1773734410,
      "period_type": "hourly",
      "period_day": 30,
      "period_hour": 20,
      "fund_flow": "auto_invest",
      "fund_source": "spot"
    }
    

##  更新定投计划🔒 需要认证

POST`/earn/autoinvest/plans/update`

POST `/earn/autoinvest/plans/update`

_更新定投计划_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AutoInvestPlanUpdate | 是 |   
» plan_id | body | integer(int64) | 是 | 计划ID  
» fund_source | body | string | 否 | 资金来源 现货spot 或 余币宝earn，默认 spot  
» fund_flow | body | string | 否 | 资金流向 现货auto_invest 或 余币宝earn，默认 auto_invest  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 更新成功 | 无  
  
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
    
    url = '/earn/autoinvest/plans/update'
    query_param = ''
    body='{"plan_id":142582,"fund_source":"earn","fund_flow":"auto_invest"}'
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
    url="/earn/autoinvest/plans/update"
    query_param=""
    body_param='{"plan_id":142582,"fund_source":"earn","fund_flow":"auto_invest"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "plan_id": 142582,
      "fund_source": "earn",
      "fund_flow": "auto_invest"
    }
    

##  停止定投计划🔒 需要认证

POST`/earn/autoinvest/plans/stop`

POST `/earn/autoinvest/plans/stop`

_停止定投计划_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AutoInvestPlanStop | 是 |   
» plan_id | body | integer(int64) | 是 | 计划ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 停止成功 | 无  
  
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
    
    url = '/earn/autoinvest/plans/stop'
    query_param = ''
    body='{"plan_id":142582}'
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
    url="/earn/autoinvest/plans/stop"
    query_param=""
    body_param='{"plan_id":142582}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "plan_id": 142582
    }
    

##  立即加仓🔒 需要认证

POST`/earn/autoinvest/plans/add_position`

POST `/earn/autoinvest/plans/add_position`

_立即加仓_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AutoInvestPlanAddPosition | 是 |   
» plan_id | body | integer(int64) | 是 | 计划ID  
» amount | body | string | 是 | 金额  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 加仓成功 | 无  
  
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
    
    url = '/earn/autoinvest/plans/add_position'
    query_param = ''
    body='{"plan_id":142583,"amount":"12.345"}'
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
    url="/earn/autoinvest/plans/add_position"
    query_param=""
    body_param='{"plan_id":142583,"amount":"12.345"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "plan_id": 142583,
      "amount": "12.345"
    }
    

##  查询支持定投的币种🔒 需要认证

GET`/earn/autoinvest/coins`

GET `/earn/autoinvest/coins`

_查询支持定投的币种_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
plan_money | 请求参数 | string | 否 | 计价货币，可选 USDT 或 BTC，默认 USDT  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | [AutoInvestCoinsItem]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [支持定投的币种项]  
» _None_ | AutoInvestCoinsItem | 支持定投的币种项  
»» key | string | 币种代码  
»» value | string | 币种名称  
»» asset_icon_url | string | 币种图标URL  
»» sort | integer(int64) | 排序  
  
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
    
    url = '/earn/autoinvest/coins'
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
    url="/earn/autoinvest/coins"
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
    
    
    [
      {
        "key": "BTC",
        "value": "BTC",
        "asset_icon_url": "https://icon.staticimgs.com/images/coin_icon/64/btc.png?v=1743408000",
        "sort": 0
      },
      {
        "key": "ETH",
        "value": "ETH",
        "asset_icon_url": "https://icon.staticimgs.com/images/coin_icon/64/eth.png?v=1743408000",
        "sort": 0
      }
    ]
    

##  查询可投资的最小金额🔒 需要认证

POST`/earn/autoinvest/min_invest_amount`

POST `/earn/autoinvest/min_invest_amount`

_查询可投资的最小金额_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AutoInvestMinInvestAmount | 是 |   
» money | body | string | 是 | 币种，可选USDT或BTC  
» items | body | array | 是 |   
»» asset | body | string | 是 | 币种  
»» ratio | body | string | 是 | 比例，如100  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | AutoInvestMinInvestAmountResp  
  
### 返回格式

状态码 **200**

_可投资最小金额响应_

名称 | 类型 | 描述  
---|---|---  
» min_amount | string | 最小金额  
  
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
    
    url = '/earn/autoinvest/min_invest_amount'
    query_param = ''
    body='{"money":"USDT","items":[{"asset":"BTC","ratio":"33"},{"asset":"ETH","ratio":"33"},{"asset":"SOL","ratio":"34"}]}'
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
    url="/earn/autoinvest/min_invest_amount"
    query_param=""
    body_param='{"money":"USDT","items":[{"asset":"BTC","ratio":"33"},{"asset":"ETH","ratio":"33"},{"asset":"SOL","ratio":"34"}]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "money": "USDT",
      "items": [
        {
          "asset": "BTC",
          "ratio": "33"
        },
        {
          "asset": "ETH",
          "ratio": "33"
        },
        {
          "asset": "SOL",
          "ratio": "34"
        }
      ]
    }
    

> 返回示例

> 200 返回
    
    
    {
      "min_amount": "7.06"
    }
    

##  查询计划执行记录🔒 需要认证

GET`/earn/autoinvest/plans/records`

GET `/earn/autoinvest/plans/records`

_查询计划执行记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
plan_id | 请求参数 | integer(int64) | 是 | 计划ID  
page | 请求参数 | integer(int64) | 否 | 页码  
page_size | 请求参数 | integer(int64) | 否 | 每页条数，上限 100  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | AutoInvestPlanRecordsResp  
  
### 返回格式

状态码 **200**

_计划执行记录分页响应_

名称 | 类型 | 描述  
---|---|---  
» page | integer(int64) | 页码  
» page_size | integer(int64) | 每页条数  
» total_page | integer(int64) | 总页码  
» total | integer(int64) | 总条数  
» list | array |   
»» _None_ | object | 计划执行记录项  
»»» id | integer(int64) | 记录ID  
»»» type | string | 类型  
»»» money | string | 来源币种  
»»» user_id | integer(int64) | 用户ID  
»»» plan_id | integer(int64) | 计划ID  
»»» plan_version | integer(int64) | 计划版本  
»»» amount | string | 投资金额  
»»» create_time | integer(int64) | 投资时间  
»»» update_time | integer(int64) | 更新时间  
»»» status | string | 状态  
»»» status_type | integer(int64) | 状态枚举  
»»» side | integer(int64) | 2 买入，其它 卖出  
»»» status_message | string | 状态描述  
»»» detail | string | 详情  
»»» asset | string | 币种  
  
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
    
    url = '/earn/autoinvest/plans/records'
    query_param = 'plan_id=141378'
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
    url="/earn/autoinvest/plans/records"
    query_param="plan_id=141378"
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
      "page": 1,
      "page_size": 10,
      "total_page": 30,
      "total": 299,
      "list": [
        {
          "id": 1770805384918111,
          "type": "Auto Invest",
          "money": "USDT",
          "asset": "",
          "user_id": 21245786,
          "plan_id": 141378,
          "plan_version": 2,
          "amount": "32.60292",
          "create_time": 1773734410,
          "update_time": 1773734410,
          "status": "Failed",
          "status_type": 2,
          "side": 2,
          "status_message": "put order fail",
          "detail": ""
        }
      ]
    }
    

##  查询计划执行记录详情（订单明细）🔒 需要认证

GET`/earn/autoinvest/orders`

GET `/earn/autoinvest/orders`

_查询计划执行记录详情（订单明细）_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
plan_id | 请求参数 | integer(int64) | 是 | 计划ID  
record_id | 请求参数 | integer(int64) | 是 | 记录ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | [AutoInvestOrderItem]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [定投订单项]  
» _None_ | AutoInvestOrderItem | 定投订单项  
»» id | integer(int64) | 订单ID  
»» type | string | 类型  
»» amount | string | 数量  
»» plan_id | integer(int64) | 计划ID  
»» side | integer(int64) | 方向  
»» asset | string | 币种  
»» record_id | integer(int64) | 记录ID  
»» total_money | string | 总金额  
»» market | string | 交易对  
»» price | string | 价格  
»» create_time | integer(int64) | 创建时间（Unix 时间戳）  
»» total | string | 合计  
»» fund_flow | string | 资金流向  
»» error_code | integer(int64) | 错误码  
»» error_msg | string | 错误信息  
»» status | integer(int64) | 状态  
  
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
    
    url = '/earn/autoinvest/orders'
    query_param = 'plan_id=142583&record_id=1770805384904919'
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
    url="/earn/autoinvest/orders"
    query_param="plan_id=142583&record_id=1770805384904919"
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
    
    
    [
      {
        "id": 6787627,
        "type": "Buy",
        "amount": "0.031",
        "plan_id": 142583,
        "side": 2,
        "asset": "USDT",
        "record_id": 1770805384904919,
        "total_money": "2.72583",
        "market": "SOL/USDT",
        "price": "87.93",
        "create_time": 1773656162,
        "total": "2.72583",
        "fund_flow": "auto_invest",
        "error_code": 0,
        "error_msg": "",
        "status": 1
      },
      {
        "id": 6787626,
        "type": "Buy",
        "amount": "0.001",
        "plan_id": 142583,
        "side": 2,
        "asset": "USDT",
        "record_id": 1770805384904919,
        "total_money": "2.65789",
        "market": "ETH/USDT",
        "price": "2657.89",
        "create_time": 1773656162,
        "total": "2.65789",
        "fund_flow": "auto_invest",
        "error_code": 0,
        "error_msg": "",
        "status": 1
      }
    ]
    

##  查询投资币种配置🔒 需要认证

GET`/earn/autoinvest/config`

GET `/earn/autoinvest/config`

_查询投资币种配置_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | [AutoInvestConfigItem]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [投资币种配置项]  
» _None_ | AutoInvestConfigItem | 投资币种配置项  
»» coin | string | 币种  
»» max_limit | string | 投资上限  
  
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
    
    url = '/earn/autoinvest/config'
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
    url="/earn/autoinvest/config"
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
    
    
    [
      {
        "coin": "BTC",
        "max_limit": "10"
      },
      {
        "coin": "USDT",
        "max_limit": "100000"
      }
    ]
    

##  查询定投计划详情🔒 需要认证

GET`/earn/autoinvest/plans/detail`

GET `/earn/autoinvest/plans/detail`

_查询定投计划详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
plan_id | 请求参数 | integer(int64) | 是 | 计划ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | AutoInvestPlanDetail  
  
### 返回格式

状态码 **200**

_定投计划详情_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 计划ID  
» version | integer(int64) | 计划版本  
» name | string | 计划名称  
» create_time | integer(int64) | 创建时间（Unix 时间戳）  
» update_time | integer(int64) | 更新时间（Unix 时间戳）  
» user_id | integer(int64) | 用户ID  
» money | string | 计价币种  
» amount | string | 每期投资金额  
» period_type | string | 周期类型（如 monthly）  
» period_day | integer(int64) | 周期日  
» period_hour | integer(int64) | 周期小时  
» portfolio | array | 投资组合  
»» _None_ | AutoInvestPlanDetail/properties/portfolio/items | 定投计划投资组合项  
»»» asset | string | 币种  
»»» ratio | string | 占比  
»»» cum_invest | string | 累计投入  
»»» cum_hold | string | 累计持仓  
»»» cum_redeem | string | 累计赎回  
»»» avg_price | string | 平均成本价  
»»» redeem_status | integer(int64) | 赎回状态  
»»» lend_amount | string | 出借数量  
»» next_time | integer(int64) | 下次执行时间（Unix 时间戳）  
»» period | integer(int64) | 已执行期数  
»» fund_source | string | 资金来源（spot/earn）  
»» fund_flow | string | 资金流向（auto_invest/earn）  
  
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
    
    url = '/earn/autoinvest/plans/detail'
    query_param = 'plan_id=142609'
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
    url="/earn/autoinvest/plans/detail"
    query_param="plan_id=142609"
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
      "id": 142609,
      "version": 0,
      "name": "Auto Invest BTC",
      "create_time": 1773733133,
      "update_time": 1773733133,
      "user_id": 2124569786,
      "money": "USDT",
      "amount": "100",
      "period_type": "monthly",
      "period_day": 1,
      "period_hour": 1,
      "portfolio": [
        {
          "asset": "BTC",
          "ratio": "33",
          "cum_invest": "0",
          "cum_hold": "0",
          "cum_redeem": "0",
          "avg_price": "0",
          "redeem_status": 0,
          "lend_amount": "0"
        },
        {
          "asset": "GT",
          "ratio": "33",
          "cum_invest": "0",
          "cum_hold": "0",
          "cum_redeem": "0",
          "avg_price": "0",
          "redeem_status": 0,
          "lend_amount": "0"
        },
        {
          "asset": "ETH",
          "ratio": "34",
          "cum_invest": "0",
          "cum_hold": "0",
          "cum_redeem": "0",
          "avg_price": "0",
          "redeem_status": 0,
          "lend_amount": "0"
        }
      ],
      "next_time": 1775005200,
      "period": 0,
      "fund_source": "spot",
      "fund_flow": "auto_invest"
    }
    

##  查询定投计划列表🔒 需要认证

GET`/earn/autoinvest/plans/list_info`

GET `/earn/autoinvest/plans/list_info`

_查询定投计划列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
status | 请求参数 | string | 是 | 计划状态，历史 history，进行中 active  
page | 请求参数 | integer(int64) | 否 | 页码  
page_size | 请求参数 | integer(int64) | 否 | 每页条数，最大 100  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | AutoInvestPlanListInfoResp  
  
### 返回格式

状态码 **200**

_定投计划列表分页响应_

名称 | 类型 | 描述  
---|---|---  
» page | integer(int64) | 页码  
» page_size | integer(int64) | 每页条数  
» page_count | integer(int64) | 总页数  
» total_count | integer(int64) | 总条数  
» list | array | 计划列表  
»» _None_ | object | 定投计划详情  
»»» id | integer(int64) | 计划ID  
»»» version | integer(int64) | 计划版本  
»»» name | string | 计划名称  
»»» create_time | integer(int64) | 创建时间（Unix 时间戳）  
»»» update_time | integer(int64) | 更新时间（Unix 时间戳）  
»»» user_id | integer(int64) | 用户ID  
»»» money | string | 计价币种  
»»» amount | string | 每期投资金额  
»»» period_type | string | 周期类型（如 monthly）  
»»» period_day | integer(int64) | 周期日  
»»» period_hour | integer(int64) | 周期小时  
»»» portfolio | array | 投资组合  
»»»» _None_ | AutoInvestPlanDetail/properties/portfolio/items | 定投计划投资组合项  
»»»»» asset | string | 币种  
»»»»» ratio | string | 占比  
»»»»» cum_invest | string | 累计投入  
»»»»» cum_hold | string | 累计持仓  
»»»»» cum_redeem | string | 累计赎回  
»»»»» avg_price | string | 平均成本价  
»»»»» redeem_status | integer(int64) | 赎回状态  
»»»»» lend_amount | string | 出借数量  
»»»» next_time | integer(int64) | 下次执行时间（Unix 时间戳）  
»»»» period | integer(int64) | 已执行期数  
»»»» fund_source | string | 资金来源（spot/earn）  
»»»» fund_flow | string | 资金流向（auto_invest/earn）  
  
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
    
    url = '/earn/autoinvest/plans/list_info'
    query_param = 'status=active'
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
    url="/earn/autoinvest/plans/list_info"
    query_param="status=active"
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
      "page": 1,
      "page_size": 10,
      "page_count": 3,
      "total_count": 23,
      "list": [
        {
          "id": 142609,
          "version": 1,
          "name": "Auto Invest BTC",
          "create_time": 1773733133,
          "update_time": 1773733133,
          "user_id": 2124569786,
          "money": "USDT",
          "amount": "100",
          "period_type": "monthly",
          "period_day": 1,
          "period_hour": 1,
          "portfolio": [
            {
              "asset": "BTC",
              "ratio": "33",
              "cum_invest": "0",
              "cum_hold": "0",
              "cum_redeem": "0",
              "avg_price": "0",
              "redeem_status": 0,
              "lend_amount": "0"
            },
            {
              "asset": "GT",
              "ratio": "33",
              "cum_invest": "0",
              "cum_hold": "0",
              "cum_redeem": "0",
              "avg_price": "0",
              "redeem_status": 0,
              "lend_amount": "0"
            },
            {
              "asset": "ETH",
              "ratio": "34",
              "cum_invest": "0",
              "cum_hold": "0",
              "cum_redeem": "0",
              "avg_price": "0",
              "redeem_status": 0,
              "lend_amount": "0"
            }
          ],
          "next_time": 1775005200,
          "period": 0,
          "fund_source": "spot",
          "fund_flow": "auto_invest"
        }
      ]
    }
    

##  获取产品列表

GET`/earn/fixed-term/product`

GET `/earn/fixed-term/product`

_获取产品列表_

查询定期理财产品列表，支持按币种、产品类型、状态等条件过滤，返回产品利率、锁仓期限、额度及奖励活动信息

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
asset | 请求参数 | string | 否 | 币种  
type | 请求参数 | integer | 否 | 产品类型 1：普通 2：vip  
page | 请求参数 | integer | 是 | 页数  
limit | 请求参数 | integer | 是 | 每页大小  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 产品列表查询成功 | ListEarnFixedTermProductsResponse  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 返回码，0 表示成功  
» message | string | 返回信息  
» data | object | 产品列表数据  
»» list | array | 产品列表  
»»» _None_ | FixedTermProduct | 定期理财产品  
»»»» id | integer | 产品ID  
»»»» name | string | 产品名称  
»»»» asset | string | 币种  
»»»» lock_up_period | integer | 锁仓期限（天）  
»»»» min_lend_amount | string | 最小理财限额  
»»»» user_max_lend_amount | string | 用户最大理财限额  
»»»» total_lend_amount | string | 平台理财限额  
»»»» year_rate | string | 年利率  
»»»» type | integer | 产品类型，1 普通 2 vip  
»»»» pre_redeem | integer | 是否支持提前赎回，0 不支持 1 支持  
»»»» reinvest | integer | 是否支持复投，0 不支持 1 支持  
»»»» redeem_account | integer | 是否支持定转活，0 不支持 1 支持  
»»»» min_vip | integer | 最低VIP等级要求，0-16，0 表示无限制  
»»»» max_vip | integer | 最高VIP等级要求，0-16，0 表示无限制  
»»»» status | integer | 产品状态，1 未上架 2 已上架 3 已下架  
»»»» create_time | string | 创建时间  
»»»» user_max_lend_volume | string | 用户最大理财量  
»»»» user_total_amount | string | 用户已理财总量  
»»»» sale_status | integer | 售卖状态，1 售卖中 2 已售罄  
»»» total | integer | 总记录数  
»» timestamp | integer | 响应时间戳（秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/fixed-term/product'
    query_param = 'page=1&limit=100'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/fixed-term/product?page=1&limit=100 \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 11,
            "name": "USDT-TEST",
            "asset": "USDT",
            "lock_up_period": 16,
            "min_lend_amount": "1",
            "user_max_lend_amount": "100000",
            "total_lend_amount": "100000000",
            "year_rate": "0.03",
            "status": 2,
            "create_time": "2024-12-13T03:29:41.103Z",
            "user_total_amount": "0"
          },
          {
            "id": 10,
            "name": "示例",
            "asset": "USDT",
            "lock_up_period": 15,
            "min_lend_amount": "1",
            "user_max_lend_amount": "100000",
            "total_lend_amount": "100000000",
            "year_rate": "0.03",
            "status": 2,
            "create_time": "2024-12-13T03:29:41.103Z",
            "user_total_amount": "0"
          }
        ],
        "total": 12
      },
      "timestamp": 1734338466
    }
    

##  获取单币种产品列表

GET`/earn/fixed-term/product/{asset}/list`

GET `/earn/fixed-term/product/{asset}/list`

_获取单币种产品列表_

按产品期限从小到大

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
asset | URL | string | 是 | 币种名称，如 USDT、BTC  
type | 请求参数 | string | 否 | 产品类型：""或 1:普通产品列表 2:vip产品列表 0:全部产品列表  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 单币种产品列表查询成功 | ListEarnFixedTermProductsByAssetResponse  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 返回码，0 表示成功  
» message | string | 返回信息  
» data | object | 产品列表数据  
»» list | array | 产品列表  
»»» _None_ | FixedTermProductSimple | 定期理财产品（精简）  
»»»» id | integer | 产品ID  
»»»» asset | string | 币种  
»»»» lock_up_period | integer | 锁仓期限（天）  
»»»» year_rate | string | 年利率  
»»»» type | integer | 产品类型，1 普通 2 vip  
»»»» pre_redeem | integer | 是否支持提前赎回，0 不支持 1 支持  
»»»» reinvest | integer | 是否支持复投，0 不支持 1 支持  
»»»» simple_earn | integer | 是否支持定转活，0 不支持 1 支持  
»»»» min_vip | integer | 最低VIP等级要求，0 表示无限制  
»»»» max_vip | integer | 最高VIP等级要求，0 表示无限制  
»»»» sale_status | integer | 售卖状态，1 售卖中 2 已售罄  
»»» timestamp | integer | 响应时间戳（秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/fixed-term/product/USDT/list'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/fixed-term/product/USDT/list \
      -H 'Accept: application/json'
    
    

> 返回示例

> 单币种产品列表查询成功
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 68,
            "asset": "USDT",
            "lock_up_period": 1,
            "year_rate": "0.0289",
            "sale_status": 1
          },
          {
            "id": 61,
            "asset": "USDT",
            "lock_up_period": 30,
            "year_rate": "0.0395",
            "sale_status": 2
          }
        ]
      },
      "timestamp": 1737944222
    }
    
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 29,
            "asset": "ATOM",
            "lock_up_period": 7,
            "year_rate": "0.04",
            "sale_status": 1
          }
        ]
      },
      "timestamp": 1737944009
    }
    

##  申购列表🔒 需要认证

GET`/earn/fixed-term/user/lend`

GET `/earn/fixed-term/user/lend`

_申购列表_

查询用户的定期理财申购订单列表，支持按产品、币种、订单类型等条件过滤，返回订单详情、收益、奖励及加息券信息

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
product_id | 请求参数 | integer | 否 | 产品id  
order_id | 请求参数 | integer(int64) | 否 | 订单id  
asset | 请求参数 | string | 否 | 币种  
order_type | 请求参数 | string | 是 | 订单类型：1 当前订单 2 历史订单  
page | 请求参数 | integer | 是 | 页数  
limit | 请求参数 | integer | 是 | 每页大小  
sub_business | 请求参数 | integer | 否 | 子业务  
business_filter | 请求参数 | string | 否 | 业务过滤条件，JSON 数组格式，如 [{"business":1, "sub_business": 0}]。business 1 普通 2 vip  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 申购订单列表查询成功 | ListEarnFixedTermLendsResponse  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 返回码，0 表示成功  
» message | string | 返回信息  
» data | object | 申购订单列表数据  
»» list | array | 申购订单列表  
»»» _None_ | FixedTermLendOrder | 定期理财申购订单  
»»»» id | integer | 申购记录ID  
»»»» business | integer | 业务类型，1 普通 2 vip  
»»»» order_id | integer(int64) | 订单ID  
»»»» user_id | integer(int64) | 用户ID  
»»»» asset | string | 币种  
»»»» product_id | integer | 产品ID  
»»»» lock_up_period | integer | 锁仓期限（天）  
»»»» principal | string | 申购本金  
»»»» year_rate | string | 年利率  
»»»» product_type | integer | 产品类型，1 普通 2 vip  
»»»» interest | string | 已产生利息  
»»»» status | integer | 订单状态，1 持有中 2 已赎回 3 已到期 4 已结算  
»»»» reinvest_status | integer | 复投状态，0 不复投 1 复投  
»»»» redeem_account_type | integer | 赎回到账账户类型，1 现货账户  
»»»» origin_order | string | 原始订单ID，复投场景下为前序订单ID链  
»»»» redeem_type | integer | 赎回类型，1 提前赎回 2 到期赎回  
»»»» redeem_time | string | 赎回时间  
»»»» finish_time | string | 到期时间  
»»»» create_time | string | 创建时间  
»»»» year_rate_perent | string | 年利率百分比展示值  
»»»» total_year_rate_percent | string | 综合年化收益率百分比（含加息、奖励等）  
»»»» total_interest | string | 总收益（含利息和额外奖励）  
»»»» product_info | FixedTermProductInfo | 产品配置信息  
»»»»» pre_redeem | integer | 是否支持提前赎回，0 不支持 1 支持  
»»»»» reinvest | integer | 是否支持复投，0 不支持 1 支持  
»»»»» redeem_account | integer | 赎回到账账户类型  
»»»»» min_vip | integer | 最低VIP等级要求，0 表示无限制  
»»»»» max_vip | integer | 最高VIP等级要求，0 表示无限制  
»»»» bonus_info | FixedTermBonusInfo | 额外奖励活动信息  
»»»»» id | integer | 活动ID  
»»»»» product_id | integer | 关联产品ID  
»»»»» asset | string | 产品币种  
»»»»» bonus_asset | string | 奖励币种  
»»»»» kyc_limit | string | KYC等级限制，逗号分隔  
»»»»» ladder_apr | array | 阶梯年化利率  
»»»»»» apr | string | 年化利率  
»»»»»» left | string | 区间下限  
»»»»»» right | string | 区间上限  
»»»»» total_bonus_amount | string | 奖励总量  
»»»»» user_total_bonus_amount | string | 单用户奖励上限  
»»»»» status | integer | 活动状态，1 未上架 2 已上架 3 已下架  
»»»»» start_time | string | 活动开始时间  
»»»»» end_time | string | 活动结束时间  
»»»»» create_time | string | 创建时间  
»»»»» start_at | integer | 活动开始时间戳（秒）  
»»»»» end_at | integer | 活动结束时间戳（秒）  
»»»»» total_issued_amount | string | 已发放奖励总量  
»»»»» user_total_issued_amount | string | 该用户已发放奖励总量  
»»»»» bonus_asset_price | string | 奖励币种价格（USDT 计价）  
»»»»» product_asset_price | string | 产品币种价格（USDT 计价）  
»»»»» product_year_rate | string | 产品基础年利率  
»»»» coupon_info | FixedTermCouponInfo | 加息券信息  
»»»»» id | integer | 加息券记录ID  
»»»»» business | integer | 业务类型  
»»»»» user_id | integer(int64) | 用户ID  
»»»»» asset | string | 币种  
»»»»» order_id | integer(int64) | 关联订单ID  
»»»»» financial_rate_id | integer | 加息券ID  
»»»»» buy_limit_low | string | 加息券适用最低申购金额  
»»»»» buy_limit_high | string | 加息券适用最高申购金额  
»»»»» rate_day | integer | 加息天数  
»»»»» rate_ratio | string | 加息利率百分比  
»»»»» coupon_days | integer | 实际加息天数  
»»»»» coupon_principal | string | 加息计算本金  
»»»»» coupon_year_rate | string | 加息年化利率  
»»»»» coupon_interest | string | 加息产生的利息  
»»»»» status | integer | 状态，1 生效中 2 已结算  
»»»»» finish_time | string | 结算时间  
»»»»» create_time | string | 创建时间  
»»»» redeem_at | integer | 赎回时间戳（秒）  
»»»» finish_at | integer | 到期时间戳（秒）  
»»»» create_at | integer | 创建时间戳（秒）  
»»»» icon | string | 币种图标URL  
»»» total | integer | 总记录数  
»» timestamp | integer | 响应时间戳（秒）  
  
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
    
    url = '/earn/fixed-term/user/lend'
    query_param = 'order_type=1&page=1&limit=10'
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
    url="/earn/fixed-term/user/lend"
    query_param="order_type=1&page=1&limit=10"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 申购订单列表查询成功
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 83402,
            "business": 1,
            "order_id": 5846120275,
            "user_id": 2024103749,
            "asset": "USDT",
            "product_id": 239,
            "lock_up_period": 23,
            "principal": "44.12",
            "year_rate": "0.3",
            "product_type": 2,
            "interest": "0.83404931",
            "status": 1,
            "reinvest_status": 1,
            "redeem_account_type": 1,
            "origin_order": "",
            "redeem_type": 2,
            "redeem_time": "2025-08-08T00:00:00Z",
            "finish_time": "2025-08-08T00:00:00Z",
            "create_time": "2025-07-15T03:55:07.304Z",
            "year_rate_perent": "30",
            "total_year_rate_percent": "63.13",
            "total_interest": "0.83996629",
            "product_info": {
              "pre_redeem": 1,
              "reinvest": 1,
              "redeem_account": 1,
              "min_vip": 1,
              "max_vip": 16
            },
            "bonus_info": {
              "id": 142,
              "product_id": 239,
              "asset": "USDT",
              "bonus_asset": "GT",
              "kyc_limit": "1,2,3,4",
              "ladder_apr": [
                {
                  "apr": "0.1",
                  "left": "0",
                  "right": "1"
                },
                {
                  "apr": "0.2",
                  "left": "1",
                  "right": "2"
                }
              ],
              "total_bonus_amount": "100000",
              "user_total_bonus_amount": "100000",
              "status": 2,
              "start_time": "2025-06-20T06:57:46Z",
              "end_time": "2026-06-29T16:00:00Z",
              "create_time": "2025-06-20T06:57:54.796Z",
              "start_at": 1750402666,
              "end_at": 1782748800,
              "total_issued_amount": "19.49",
              "user_total_issued_amount": "0",
              "bonus_asset_price": "17.66",
              "product_asset_price": "1",
              "product_year_rate": "0.3"
            },
            "coupon_info": {
              "id": 63,
              "business": 1,
              "user_id": 2024103749,
              "asset": "USDT",
              "order_id": 5846120275,
              "financial_rate_id": 1506,
              "buy_limit_low": "1",
              "buy_limit_high": "3",
              "rate_day": 30,
              "rate_ratio": "3.13",
              "coupon_days": 23,
              "coupon_principal": "3",
              "coupon_year_rate": "0.0313",
              "coupon_interest": "0.00591698",
              "status": 2,
              "finish_time": "2025-08-08T00:00:00Z",
              "create_time": "2025-07-15T03:55:07.285Z"
            },
            "redeem_at": 1754611200,
            "finish_at": 1754611200,
            "create_at": 1752551707,
            "icon": "https://icon.gateimg.com/images/coin_icon/64/usdt.png"
          }
        ],
        "total": 51
      },
      "timestamp": 1752564887
    }
    
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 83392,
            "business": 1,
            "order_id": 5846112514,
            "user_id": 2024103749,
            "asset": "USDT",
            "product_id": 230,
            "lock_up_period": 1,
            "principal": "1",
            "year_rate": "0.0312",
            "product_type": 1,
            "interest": "0.00008547",
            "status": 1,
            "reinvest_status": 1,
            "redeem_account_type": 1,
            "origin_order": "",
            "redeem_type": 2,
            "redeem_time": "2025-07-16T00:00:00Z",
            "finish_time": "2025-07-16T00:00:00Z",
            "create_time": "2025-07-15T00:30:10.515Z",
            "year_rate_perent": "3.12",
            "total_year_rate_percent": "3.12",
            "total_interest": "0.00008547",
            "product_info": {
              "pre_redeem": 0,
              "reinvest": 1,
              "redeem_account": 1,
              "min_vip": 0,
              "max_vip": 0
            },
            "bonus_info": null,
            "coupon_info": null,
            "redeem_at": 1752624000,
            "finish_at": 1752624000,
            "create_at": 1752539410,
            "icon": "https://icon.gateimg.com/images/coin_icon/64/usdt.png"
          }
        ],
        "total": 10
      },
      "timestamp": 1752564887
    }
    

##  申购🔒 需要认证

POST`/earn/fixed-term/user/lend`

POST `/earn/fixed-term/user/lend`

_申购_

申购定期理财产品，需指定产品ID和申购金额，可选择是否复投及使用加息券

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | FixedTermLendRequest | 否 |   
» product_id | body | integer | 是 | 产品ID  
» amount | body | string | 是 | 申购金额  
» year_rate | body | string | 否 | 年利率  
» reinvest_status | body | integer | 否 | 复投状态，0 不复投 1 复投  
» redeem_account_type | body | integer | 否 | 赎回到账账户类型，1 现货账户  
» financial_rate_id | body | integer | 否 | 加息券ID，0 表示不使用  
» sub_business | body | integer | 否 | 子业务类型  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 申购成功 | CreateEarnFixedTermLendResponse  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 返回码，0 表示成功  
» message | string | 返回信息  
» data | object | 申购结果  
»» order_id | integer(int64) | 申购订单ID  
» timestamp | integer | 响应时间戳（秒）  
  
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
    
    url = '/earn/fixed-term/user/lend'
    query_param = ''
    body='{"product_id":476,"amount":"1","year_rate":"0.0100000000","reinvest_status":1,"redeem_account_type":1,"financial_rate_id":0,"sub_business":13}'
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
    url="/earn/fixed-term/user/lend"
    query_param=""
    body_param='{"product_id":476,"amount":"1","year_rate":"0.0100000000","reinvest_status":1,"redeem_account_type":1,"financial_rate_id":0,"sub_business":13}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "product_id": 476,
      "amount": "1",
      "year_rate": "0.0100000000",
      "reinvest_status": 1,
      "redeem_account_type": 1,
      "financial_rate_id": 0,
      "sub_business": 13
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "order_id": 0
      },
      "timestamp": 0
    }
    

##  赎回🔒 需要认证

POST`/earn/fixed-term/user/pre-redeem`

POST `/earn/fixed-term/user/pre-redeem`

_赎回_

提前赎回定期理财订单，需指定订单ID

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | EarnFixedTermPreRedeemRequest | 否 |   
» order_id | body | string | 是 | 订单ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 赎回成功 | CreateEarnFixedTermPreRedeemResponse  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 返回码，0 表示成功  
» message | string | 返回信息  
» data | object | 赎回结果（成功时为空对象）  
» timestamp | integer | 响应时间戳（秒）  
  
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
    
    url = '/earn/fixed-term/user/pre-redeem'
    query_param = ''
    body='{"order_id":"5862476630"}'
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
    url="/earn/fixed-term/user/pre-redeem"
    query_param=""
    body_param='{"order_id":"5862476630"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "order_id": "5862476630"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "string",
      "data": {},
      "timestamp": 0
    }
    

##  申购历史🔒 需要认证

GET`/earn/fixed-term/user/history`

GET `/earn/fixed-term/user/history`

_申购历史_

查询用户的定期理财历史记录，支持按类型（申购、赎回、利息、额外奖励）和时间范围过滤

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
product_id | 请求参数 | integer | 否 | 产品id  
order_id | 请求参数 | string | 否 | 订单id  
asset | 请求参数 | string | 否 | 币种  
type | 请求参数 | string | 是 | 1 申购 2 赎回 3利息 4 额外奖励  
page | 请求参数 | integer | 是 | 页数  
limit | 请求参数 | integer | 是 | 每页大小  
start_at | 请求参数 | integer | 否 | 开始时间戳  
end_at | 请求参数 | integer | 否 | 结束时间戳  
sub_business | 请求参数 | integer | 否 | 子业务  
business_filter | 请求参数 | string | 否 | 业务过滤条件，JSON 数组格式，如 [{"business":1, "sub_business": 0}]。business 1 普通 2 vip  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 历史记录查询成功 | ListEarnFixedTermHistoryResponse  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 返回码，0 表示成功  
» message | string | 返回信息  
» data | object |   
»» list | array | [定期理财历史记录]  
»»» _None_ | FixedTermHistoryRecord | 定期理财历史记录  
»»»» id | integer | 记录ID  
»»»» order_id | integer(int64) | 订单ID  
»»»» user_id | integer(int64) | 用户ID  
»»»» asset | string | 币种  
»»»» uniq_time | string | 唯一时间标识（日期）  
»»»» bonus_id | integer | 奖励活动ID  
»»»» product_id | integer | 产品ID  
»»»» bonus_asset | string | 奖励币种  
»»»» total_principal | string | 总本金  
»»»» amount | string | 金额  
»»»» asset_price | string | 币种价格  
»»»» status | integer | 状态  
»»»» detail | string | 详情说明  
»»»» create_time | string | 创建时间  
»»»» create_at | integer | 创建时间戳（秒）  
»»»» lock_up_period | integer | 期限  
»»» total | integer | 总记录数  
»» timestamp | integer | 响应时间戳（秒）  
  
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
    
    url = '/earn/fixed-term/user/history'
    query_param = 'type=1&page=1&limit=10'
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
    url="/earn/fixed-term/user/history"
    query_param="type=1&page=1&limit=10"
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
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "timestamp": 0
    }
    

#  模型

##  AutoInvestPlanRecordsResp

_计划执行记录分页响应_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
page | integer(int64) | true | none | 页码  
page_size | integer(int64) | true | none | 每页条数  
total_page | integer(int64) | true | none | 总页码  
total | integer(int64) | true | none | 总条数  
list | array | true | none | none  
» _None_ | object | false | none | 计划执行记录项  
»» id | integer(int64) | true | none | 记录ID  
»» type | string | true | none | 类型  
»» money | string | true | none | 来源币种  
»» user_id | integer(int64) | true | none | 用户ID  
»» plan_id | integer(int64) | true | none | 计划ID  
»» plan_version | integer(int64) | true | none | 计划版本  
»» amount | string | true | none | 投资金额  
»» create_time | integer(int64) | true | none | 投资时间  
»» update_time | integer(int64) | true | none | 更新时间  
»» status | string | true | none | 状态  
»» status_type | integer(int64) | true | none | 状态枚举  
»» side | integer(int64) | true | none | 2 买入，其它 卖出  
»» status_message | string | true | none | 状态描述  
»» detail | string | false | none | 详情  
»» asset | string | false | none | 币种  
      
    
    {
      "page": 0,
      "page_size": 0,
      "total_page": 0,
      "total": 0,
      "list": [
        {
          "id": 0,
          "type": "string",
          "money": "string",
          "user_id": 0,
          "plan_id": 0,
          "plan_version": 0,
          "amount": "string",
          "create_time": 0,
          "update_time": 0,
          "status": "string",
          "status_type": 0,
          "side": 0,
          "status_message": "string",
          "detail": "string",
          "asset": "string"
        }
      ]
    }
    
    

##  FixedTermLendRequest

_申购请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
product_id | integer | true | none | 产品ID  
amount | string | true | none | 申购金额  
year_rate | string | false | none | 年利率  
reinvest_status | integer | false | none | 复投状态，0 不复投 1 复投  
redeem_account_type | integer | false | none | 赎回到账账户类型，1 现货账户  
financial_rate_id | integer | false | none | 加息券ID，0 表示不使用  
sub_business | integer | false | none | 子业务类型  
      
    
    {
      "product_id": 0,
      "amount": "string",
      "year_rate": "string",
      "reinvest_status": 0,
      "redeem_account_type": 0,
      "financial_rate_id": 0,
      "sub_business": 0
    }
    
    

##  AutoInvestPlanListInfoResp

_定投计划列表分页响应_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
page | integer(int64) | true | none | 页码  
page_size | integer(int64) | true | none | 每页条数  
page_count | integer(int64) | true | none | 总页数  
total_count | integer(int64) | true | none | 总条数  
list | array | true | none | 计划列表  
» _None_ | object | false | none | 定投计划详情  
»» id | integer(int64) | true | none | 计划ID  
»» version | integer(int64) | false | none | 计划版本  
»» name | string | true | none | 计划名称  
»» create_time | integer(int64) | true | none | 创建时间（Unix 时间戳）  
»» update_time | integer(int64) | true | none | 更新时间（Unix 时间戳）  
»» user_id | integer(int64) | true | none | 用户ID  
»» money | string | true | none | 计价币种  
»» amount | string | true | none | 每期投资金额  
»» period_type | string | true | none | 周期类型（如 monthly）  
»» period_day | integer(int64) | true | none | 周期日  
»» period_hour | integer(int64) | true | none | 周期小时  
»» portfolio | [AutoInvestPlanDetail/properties/portfolio/items] | true | none | 投资组合  
»» next_time | integer(int64) | true | none | 下次执行时间（Unix 时间戳）  
»» period | integer(int64) | true | none | 已执行期数  
»» fund_source | string | true | none | 资金来源（spot/earn）  
»» fund_flow | string | true | none | 资金流向（auto_invest/earn）  
      
    
    {
      "page": 0,
      "page_size": 0,
      "page_count": 0,
      "total_count": 0,
      "list": [
        {
          "id": 0,
          "version": 0,
          "name": "string",
          "create_time": 0,
          "update_time": 0,
          "user_id": 0,
          "money": "string",
          "amount": "string",
          "period_type": "string",
          "period_day": 0,
          "period_hour": 0,
          "portfolio": [],
          "next_time": 0,
          "period": 0,
          "fund_source": "string",
          "fund_flow": "string"
        }
      ]
    }
    
    

##  AutoInvestPlanAddPosition

_立即加仓请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
plan_id | integer(int64) | true | none | 计划ID  
amount | string | true | none | 金额  
      
    
    {
      "plan_id": 0,
      "amount": "string"
    }
    
    

##  ListEarnFixedTermProductsByAssetResponse

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | 返回码，0 表示成功  
message | string | true | none | 返回信息  
data | object | true | none | 产品列表数据  
» list | [FixedTermProductSimple] | true | none | 产品列表  
timestamp | integer | true | none | 响应时间戳（秒）  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  AutoInvestPlanStop

_停止定投计划请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
plan_id | integer(int64) | true | none | 计划ID  
      
    
    {
      "plan_id": 0
    }
    
    

##  AssetListStruct

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
pid | integer | true | none | 项目ID  
mortgage_coin | string | true | none | 质押币种多个逗号分隔  
mortgage_amount | string | true | none | 持仓金额  
createStamp | integer | true | none | 首次时间戳  
extra_income | string | true | none | 额外奖励折U金额  
freeze_amount | string | true | none | 冻结金额  
move_income | string | true | none | none  
type | integer | true | none | 类型 0-凭证 1-锁仓 2-美债  
status | integer | true | none | 状态  
income_total | string | true | none | 币种总收益  
yesterday_income_multi | array | true | none | 昨日收益  
reward_coins | array | true | none | 币种奖励收益  
» reward_coin | string | true | none | 奖励币种  
» interest_delay_days | integer | true | none | 起息天  
» reward_delay_days | integer | true | none | 派息天 -1表示赎回时派息  
defi_income | object | true | none | DEIF收益  
» total | array | true | none | none  
»» coin | string | true | none | none  
»» amount | string | true | none | none  
      
    
    [
      {
        "pid": 0,
        "mortgage_coin": "string",
        "mortgage_amount": "string",
        "createStamp": 0,
        "extra_income": "string",
        "freeze_amount": "string",
        "move_income": "string",
        "type": 0,
        "status": 0,
        "income_total": "string",
        "yesterday_income_multi": [
          {}
        ],
        "reward_coins": [
          {}
        ],
        "defi_income": {
          "total": []
        }
      }
    ]
    
    

##  AutoInvestPlanDetail

_定投计划详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | true | none | 计划ID  
version | integer(int64) | false | none | 计划版本  
name | string | true | none | 计划名称  
create_time | integer(int64) | true | none | 创建时间（Unix 时间戳）  
update_time | integer(int64) | true | none | 更新时间（Unix 时间戳）  
user_id | integer(int64) | true | none | 用户ID  
money | string | true | none | 计价币种  
amount | string | true | none | 每期投资金额  
period_type | string | true | none | 周期类型（如 monthly）  
period_day | integer(int64) | true | none | 周期日  
period_hour | integer(int64) | true | none | 周期小时  
portfolio | array | true | none | 投资组合  
» _None_ | object | false | none | 定投计划投资组合项  
»» asset | string | true | none | 币种  
»» ratio | string | true | none | 占比  
»» cum_invest | string | true | none | 累计投入  
»» cum_hold | string | true | none | 累计持仓  
»» cum_redeem | string | true | none | 累计赎回  
»» avg_price | string | true | none | 平均成本价  
»» redeem_status | integer(int64) | true | none | 赎回状态  
»» lend_amount | string | true | none | 出借数量  
» next_time | integer(int64) | true | none | 下次执行时间（Unix 时间戳）  
» period | integer(int64) | true | none | 已执行期数  
» fund_source | string | true | none | 资金来源（spot/earn）  
» fund_flow | string | true | none | 资金流向（auto_invest/earn）  
      
    
    {
      "id": 0,
      "version": 0,
      "name": "string",
      "create_time": 0,
      "update_time": 0,
      "user_id": 0,
      "money": "string",
      "amount": "string",
      "period_type": "string",
      "period_day": 0,
      "period_hour": 0,
      "portfolio": [
        {
          "asset": "string",
          "ratio": "string",
          "cum_invest": "string",
          "cum_hold": "string",
          "cum_redeem": "string",
          "avg_price": "string",
          "redeem_status": 0,
          "lend_amount": "string"
        }
      ],
      "next_time": 0,
      "period": 0,
      "fund_source": "string",
      "fund_flow": "string"
    }
    
    

##  AutoInvestMinInvestAmountResp

_可投资最小金额响应_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
min_amount | string | true | none | 最小金额  
      
    
    {
      "min_amount": "string"
    }
    
    

##  AutoInvestPlanCreate

_创建定投计划请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
plan_name | string | false | none | 计划名称。长度 0~50 字符  
plan_des | string | false | none | 计划描述  
plan_money | string | true | none | 计价货币，支持USDT，BTC  
plan_amount | string | true | none | 每期定投金额，须 > 0，且不超过该计价货币配置的单笔最大金额  
plan_period_type | string | true | none | 枚举 daily、weekly、biweekly、monthly、hourly、4-hourly  
plan_period_day | integer(int64) | true | none | 周期日。monthly 时表示每月第几天 1~30；weekly/biweekly 时表示周几 1~7（1=周一）；daily/hourly/4-hourly 时忽略  
plan_period_hour | integer(int64) | true | none | 几点执行定投 0-23  
items | array | true | none | 投资组合，不可重复 asset；所有项的 ratio 之和须为 100  
» asset | string | true | none | 投资币种，如 BTC；需为已启用且市场存在；同一 plan 内不可重复  
» ratio | string | true | none | 该币种在组合中的占比，所有 items 的 ratio 之和必须为100  
fund_source | string | false | none | 资金来源 spot 或 earn，默认 spot  
fund_flow | string | false | none | 资金流向 auto_invest 或 earn，默认 auto_invest  
type | integer(int64) | false | none | 0 普通创建, 1 快速投资  
      
    
    {
      "plan_name": "string",
      "plan_des": "string",
      "plan_money": "string",
      "plan_amount": "string",
      "plan_period_type": "string",
      "plan_period_day": 0,
      "plan_period_hour": 0,
      "items": [
        {
          "asset": "string",
          "ratio": "string"
        }
      ],
      "fund_source": "string",
      "fund_flow": "string",
      "type": 0
    }
    
    

##  ListEarnFixedTermHistoryResponse

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | false | none | 返回码，0 表示成功  
message | string | false | none | 返回信息  
data | object | false | none | none  
» list | [FixedTermHistoryRecord] | false | none | [定期理财历史记录]  
» total | integer | false | none | 总记录数  
timestamp | integer | false | none | 响应时间戳（秒）  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "timestamp": 0
    }
    
    

##  ListEarnFixedTermProductsResponse

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | 返回码，0 表示成功  
message | string | true | none | 返回信息  
data | object | true | none | 产品列表数据  
» list | [FixedTermProduct] | true | none | 产品列表  
» total | integer | true | none | 总记录数  
timestamp | integer | true | none | 响应时间戳（秒）  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "timestamp": 0
    }
    
    

##  AutoInvestPlanCreateResp

_创建定投计划响应_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | true | none | 计划ID  
amount | string | false | none | 每期定投金额  
money | string | false | none | 计价货币  
next_time | integer(int64) | false | none | 下次执行时间  
period_type | string | false | none | 周期类型  
period_day | integer(int64) | false | none | 周期日  
period_hour | integer(int64) | false | none | 周期小时  
fund_flow | string | false | none | 资金流向  
fund_source | string | false | none | 资金来源  
      
    
    {
      "id": 0,
      "amount": "string",
      "money": "string",
      "next_time": 0,
      "period_type": "string",
      "period_day": 0,
      "period_hour": 0,
      "fund_flow": "string",
      "fund_source": "string"
    }
    
    

##  AwardListStruct

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
page | integer | true | none | 页  
pageSize | integer | true | none | 每页条数  
pageCount | integer | true | none | 总页数  
totalCount | integer | true | none | 总条数  
list | array | true | none | none  
» pid | integer | true | none | 项目ID  
» mortgage_coin | string | true | none | 质押币种  
» amount | string | true | none | 金额  
» reward_coin | string | true | none | 奖励币种  
» interest | string | true | none | 利息金额  
» fee | string | true | none | 手续费  
» status | integer | true | none | 状态  
» bonus_date | string | true | none | 日期  
» should_bonus_stamp | integer | true | none | 应派发时间戳  
      
    
    {
      "page": 0,
      "pageSize": 0,
      "pageCount": 0,
      "totalCount": 0,
      "list": [
        {
          "pid": 0,
          "mortgage_coin": "string",
          "amount": "string",
          "reward_coin": "string",
          "interest": "string",
          "fee": "string",
          "status": 0,
          "bonus_date": "string",
          "should_bonus_stamp": 0
        }
      ]
    }
    
    

##  DualOrderRefundPreview

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
create_timest | integer(int64) | false | none | 订单创建时间戳  
delivery_timest | integer(int64) | false | none | 订单交付时间戳  
exercise_price | string | false | none | 行权价格  
invest_amount | string | false | none | 投资金额  
invest_currency | string | false | none | 投资币种  
name | string | false | none | 订单名称标识  
order_id | integer(int64) | false | none | 订单ID  
req_id | string | false | none | 请求ID，用于实际赎回  
refund_service_charge | integer(int64) | false | none | 退款手续费  
settle_price | string | false | none | 结算价格  
settlement_amount | string | false | none | 结算金额  
settlement_currency | string | false | none | 结算币种  
settlement_interest | string | false | none | 结算利息  
settlement_principle | string | false | none | 结算本金  
type | string | false | none | call: 高卖 put: 低买  
money_back_timest | integer(int64) | false | none | 赎回时间  
      
    
    {
      "create_timest": 0,
      "delivery_timest": 0,
      "exercise_price": "string",
      "invest_amount": "string",
      "invest_currency": "string",
      "name": "string",
      "order_id": 0,
      "req_id": "string",
      "refund_service_charge": 0,
      "settle_price": "string",
      "settlement_amount": "string",
      "settlement_currency": "string",
      "settlement_interest": "string",
      "settlement_principle": "string",
      "type": "string",
      "money_back_timest": 0
    }
    
    

##  EarnFixedTermPreRedeemRequest

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | true | none | 订单ID  
      
    
    {
      "order_id": "5862476630"
    }
    
    

##  DualOrderRefundParams

_双币订单提前赎回请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | true | none | 订单ID  
req_id | string | true | none | 请求ID，由order-refund-preview返回  
      
    
    {
      "order_id": "string",
      "req_id": "string"
    }
    
    

##  DualModifyOrderReinvestParams

_双币订单复投修改请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | integer(int64) | false | none | 订单ID  
status | integer(int32) | false | none | 0: 关闭 1: 开启  
effective_time_duration | integer(int64) | false | none | 生效时长(秒)，默认1天(86400)  
      
    
    {
      "order_id": 0,
      "status": 0,
      "effective_time_duration": 0
    }
    
    

##  DualGetBalance

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user_asset_usdt | string | false | none | 用户资产折U  
user_asset_btc | string | false | none | 用户资产折BTC  
user_total_interest_usdt | string | false | none | 用户总利息折U  
user_total_interest_btc | string | false | none | 用户总利息折BTC  
      
    
    {
      "user_asset_usdt": "string",
      "user_asset_btc": "string",
      "user_total_interest_usdt": "string",
      "user_total_interest_btc": "string"
    }
    
    

##  FindCoinStruct

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
pid | integer | true | none | 项目ID  
productType | integer | true | none | 项目类型 0-凭证 1-锁仓 2-美债  
isDefi | integer | true | none | 是否DEFI协议 0-否 1-是  
currency | string | true | none | 质押币种多个逗号分隔  
estimateApr | string | true | none | 预估收益率  
minStakeAmount | string | true | none | 最小质押量  
maxStakeAmount | string | true | none | 最大质押量  
protocolName | string | true | none | 协议名  
redeemPeriod | string | true | none | 赎回期(天)  
exchangeRate | string | true | none | 兑换率  
exchangeRateReserve | string | true | none | 反向兑换率  
extraInterest | array | false | none | 额外奖励  
» start_time | string | true | none | 开始时间戳  
» end_time | string | true | none | 结束时间戳  
» reward_coin | string | true | none | 额外奖励币种  
» segment_interest | array | true | none | 分段奖励信息  
»» money_min | string | true | none | 分段小值  
»» money_max | string | true | none | 分段大值  
»» money_rate | string | true | none | 分段利率  
» currencyRewards | array | true | none | 奖励币种信息  
»» apr | string | true | none | 基础利率  
»» reward_coin | string | true | none | 奖励币种  
»» reward_delay_days | string | true | none | 派息天 -1表示赎回时派息  
»» interest_delay_days | string | true | none | 起息天  
      
    
    [
      {
        "pid": 0,
        "productType": 0,
        "isDefi": 0,
        "currency": "string",
        "estimateApr": "string",
        "minStakeAmount": "string",
        "maxStakeAmount": "string",
        "protocolName": "string",
        "redeemPeriod": "string",
        "exchangeRate": "string",
        "exchangeRateReserve": "string",
        "extraInterest": [
          {}
        ],
        "currencyRewards": [
          {}
        ]
      }
    ]
    
    

##  AutoInvestCoinsItem

_支持定投的币种项_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
key | string | true | none | 币种代码  
value | string | true | none | 币种名称  
asset_icon_url | string | true | none | 币种图标URL  
sort | integer(int64) | false | none | 排序  
      
    
    {
      "key": "string",
      "value": "string",
      "asset_icon_url": "string",
      "sort": 0
    }
    
    

##  PlaceDualInvestmentOrder

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int32) | false | none | 订单ID  
plan_id | integer(int32) | false | none | 项目ID  
invest_amount | string | false | none | 投资数量  
settlement_amount | string | false | none | 结算数量  
create_time | integer(int32) | false | none | 创建时间  
complete_time | integer(int32) | false | none | 完成时间  
status | string | false | none | 状态:  
  
`INIT`-创建  
`SETTLEMENT_SUCCESS`-结算成功  
`SETTLEMENT_PROCESSING`-结算中  
`CANCELED`-取消  
`FAILED`-失败  
invest_currency | string | false | none | 投资币种  
exercise_currency | string | false | none | 行权币种  
exercise_price | string | false | none | 行权价格  
settlement_price | string | false | none | 结算价格  
settlement_currency | string | false | none | 结算币种  
apy_display | string | false | none | 年化收益率  
apy_settlement | string | false | none | 结算年化收益率  
delivery_time | integer(int32) | false | none | 结算时间  
text | string | false | none | 订单自定义信息  
      
    
    {
      "id": 0,
      "plan_id": 0,
      "invest_amount": "string",
      "settlement_amount": "string",
      "create_time": 0,
      "complete_time": 0,
      "status": "string",
      "invest_currency": "string",
      "exercise_currency": "string",
      "exercise_price": "string",
      "settlement_price": "string",
      "settlement_currency": "string",
      "apy_display": "string",
      "apy_settlement": "string",
      "delivery_time": 0,
      "text": "string"
    }
    
    

##  CreateEarnFixedTermLendResponse

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | false | none | 返回码，0 表示成功  
message | string | false | none | 返回信息  
data | object | false | none | 申购结果  
» order_id | integer(int64) | false | none | 申购订单ID  
timestamp | integer | false | none | 响应时间戳（秒）  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "order_id": 0
      },
      "timestamp": 0
    }
    
    

##  FixedTermProductSimple

_定期理财产品（精简）_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer | false | none | 产品ID  
asset | string | false | none | 币种  
lock_up_period | integer | false | none | 锁仓期限（天）  
year_rate | string | false | none | 年利率  
type | integer | false | none | 产品类型，1 普通 2 vip  
pre_redeem | integer | false | none | 是否支持提前赎回，0 不支持 1 支持  
reinvest | integer | false | none | 是否支持复投，0 不支持 1 支持  
simple_earn | integer | false | none | 是否支持定转活，0 不支持 1 支持  
min_vip | integer | false | none | 最低VIP等级要求，0 表示无限制  
max_vip | integer | false | none | 最高VIP等级要求，0 表示无限制  
sale_status | integer | false | none | 售卖状态，1 售卖中 2 已售罄  
      
    
    {
      "id": 0,
      "asset": "string",
      "lock_up_period": 0,
      "year_rate": "string",
      "type": 0,
      "pre_redeem": 0,
      "reinvest": 0,
      "simple_earn": 0,
      "min_vip": 0,
      "max_vip": 0,
      "sale_status": 0
    }
    
    

##  DualGetPlans

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int32) | false | none | 项目ID  
instrument_name | string | false | none | 项目名称  
invest_currency | string | false | none | 投资币种  
exercise_currency | string | false | none | 行权币种  
exercise_price | number(double) | false | none | 行权价格  
delivery_time | integer(int32) | false | none | 结算时间  
apy_display | string | false | none | 年化收益率  
min_amount | string | false | none | 最小投资金额  
start_time | integer(int32) | false | none | 开始时间  
end_time | integer(int32) | false | none | 结束时间  
status | string | false | none | 状态:  
  
`NOTSTARTED`-未开始  
`ONGOING`-进行中  
`ENDED`-已结束  
      
    
    {
      "id": 0,
      "instrument_name": "string",
      "invest_currency": "string",
      "exercise_currency": "string",
      "exercise_price": 0,
      "delivery_time": 0,
      "apy_display": "string",
      "min_amount": "string",
      "start_time": 0,
      "end_time": 0,
      "status": "string"
    }
    
    

##  CreateEarnFixedTermPreRedeemResponse

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | false | none | 返回码，0 表示成功  
message | string | false | none | 返回信息  
data | object | false | none | 赎回结果（成功时为空对象）  
timestamp | integer | false | none | 响应时间戳（秒）  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {},
      "timestamp": 0
    }
    
    

##  AutoInvestPlanUpdate

_更新定投计划请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
plan_id | integer(int64) | true | none | 计划ID  
fund_source | string | false | none | 资金来源 现货spot 或 余币宝earn，默认 spot  
fund_flow | string | false | none | 资金流向 现货auto_invest 或 余币宝earn，默认 auto_invest  
      
    
    {
      "plan_id": 0,
      "fund_source": "string",
      "fund_flow": "string"
    }
    
    

##  DualProjectRecommend

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 项目ID  
category | integer(int32) | false | none | 策略类别  
type | string | false | none | call: 高卖 put: 低买  
invest_currency | string | false | none | 投资币种  
exercise_currency | string | false | none | 行权币种  
apy_display | string | false | none | 年化收益率  
exercise_price | string | false | none | 行权价格  
delivery_timest | integer(int64) | false | none | 结算时间  
min_amount | string | false | none | 最小投资金额  
max_amount | string | false | none | 最大投资金额  
min_copies | integer(int64) | false | none | 最小份数  
max_copies | integer(int64) | false | none | 最大份数  
invest_days | integer(int64) | false | none | 锁仓天数  
invest_hours | string | false | none | 锁仓小时数  
      
    
    {
      "id": 0,
      "category": 0,
      "type": "string",
      "invest_currency": "string",
      "exercise_currency": "string",
      "apy_display": "string",
      "exercise_price": "string",
      "delivery_timest": 0,
      "min_amount": "string",
      "max_amount": "string",
      "min_copies": 0,
      "max_copies": 0,
      "invest_days": 0,
      "invest_hours": "string"
    }
    
    

##  PlaceDualInvestmentOrderParams

_双币宝订单_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
plan_id | string | true | none | 项目ID  
amount | string | true | none | 申购金额  
text | string | false | none | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
      
    
    {
      "plan_id": "string",
      "amount": "string",
      "text": "string"
    }
    
    

##  SwapCoin

_链上挖矿_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
coin | string | true | none | 币种  
side | integer | true | none | 0-质押, 1-赎回  
amount | string | true | none | 数量  
pid | integer | false | none | DEFI类挖矿协议ID  
      
    
    {
      "coin": "string",
      "side": 0,
      "amount": "string",
      "pid": 0
    }
    
    

##  DualGetOrders

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int32) | false | none | 订单ID  
plan_id | integer(int32) | false | none | 项目ID  
invest_amount | string | false | none | 投资数量  
settlement_amount | string | false | none | 结算数量  
create_time | integer(int32) | false | none | 创建时间  
complete_time | integer(int32) | false | none | 完成时间  
status | string | false | none | 状态:  
  
`INIT`-创建  
`SETTLEMENT_SUCCESS`-结算成功  
`SETTLEMENT_PROCESSING`-结算中  
`CANCELED`-取消  
`FAILED`-失败  
invest_currency | string | false | none | 投资币种  
exercise_currency | string | false | none | 行权币种  
exercise_price | string | false | none | 行权价格  
settlement_price | string | false | none | 结算价格  
settlement_currency | string | false | none | 结算币种  
apy_display | string | false | none | 年化收益率  
apy_settlement | string | false | none | 结算年化收益率  
delivery_time | integer(int32) | false | none | 结算时间  
text | string | false | none | 订单自定义信息  
      
    
    {
      "id": 0,
      "plan_id": 0,
      "invest_amount": "string",
      "settlement_amount": "string",
      "create_time": 0,
      "complete_time": 0,
      "status": "string",
      "invest_currency": "string",
      "exercise_currency": "string",
      "exercise_price": "string",
      "settlement_price": "string",
      "settlement_currency": "string",
      "apy_display": "string",
      "apy_settlement": "string",
      "delivery_time": 0,
      "text": "string"
    }
    
    

##  SwapCoinStruct

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer | false | none | 订单ID  
pid | integer | false | none | 项目ID  
uid | integer | false | none | 用户ID  
coin | string | false | none | 币种  
type | integer | false | none | 类型 0-质押 1-赎回  
subtype | string | false | none | 子类型  
amount | string | false | none | 金额  
exchange_rate | string | false | none | 兑换比例  
exchange_amount | string | false | none | 兑换金额  
updateStamp | integer | false | none | 更新时间戳  
createStamp | integer | false | none | 交易时间戳  
status | integer | false | none | 状态 1-成功  
protocol_type | integer | false | none | DEFI协议类型  
client_order_id | string | false | none | 参考ID  
source | string | false | none | 订单来源  
      
    
    {
      "id": 0,
      "pid": 0,
      "uid": 0,
      "coin": "string",
      "type": 0,
      "subtype": "string",
      "amount": "string",
      "exchange_rate": "string",
      "exchange_amount": "string",
      "updateStamp": 0,
      "createStamp": 0,
      "status": 0,
      "protocol_type": 0,
      "client_order_id": "string",
      "source": "string"
    }
    
    

##  AutoInvestOrderItem

_定投订单项_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | true | none | 订单ID  
type | string | true | none | 类型  
amount | string | true | none | 数量  
plan_id | integer(int64) | true | none | 计划ID  
side | integer(int64) | true | none | 方向  
asset | string | true | none | 币种  
record_id | integer(int64) | true | none | 记录ID  
total_money | string | true | none | 总金额  
market | string | true | none | 交易对  
price | string | true | none | 价格  
create_time | integer(int64) | true | none | 创建时间（Unix 时间戳）  
total | string | true | none | 合计  
fund_flow | string | true | none | 资金流向  
error_code | integer(int64) | true | none | 错误码  
error_msg | string | true | none | 错误信息  
status | integer(int64) | true | none | 状态  
      
    
    {
      "id": 0,
      "type": "string",
      "amount": "string",
      "plan_id": 0,
      "side": 0,
      "asset": "string",
      "record_id": 0,
      "total_money": "string",
      "market": "string",
      "price": "string",
      "create_time": 0,
      "total": "string",
      "fund_flow": "string",
      "error_code": 0,
      "error_msg": "string",
      "status": 0
    }
    
    

##  ListEarnFixedTermLendsResponse

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | 返回码，0 表示成功  
message | string | true | none | 返回信息  
data | object | true | none | 申购订单列表数据  
» list | [FixedTermLendOrder] | true | none | 申购订单列表  
» total | integer | true | none | 总记录数  
timestamp | integer | true | none | 响应时间戳（秒）  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "timestamp": 0
    }
    
    

##  AutoInvestMinInvestAmount

_查询可投资最小金额请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
money | string | true | none | 币种，可选USDT或BTC  
items | array | true | none | none  
» asset | string | true | none | 币种  
» ratio | string | true | none | 比例，如100  
      
    
    {
      "money": "string",
      "items": [
        {
          "asset": "string",
          "ratio": "string"
        }
      ]
    }
    
    

##  OrderListStruct

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
page | integer | true | none | 页  
pageSize | integer | true | none | 每页条数  
pageCount | integer | true | none | 总页数  
totalCount | integer | true | none | 总条数  
list | array | true | none | none  
» pid | integer | true | none | 项目ID  
» coin | string | true | none | 质押赎回币种  
» amount | string | true | none | 金额  
» type | integer | true | none | 类型 0-质押 1-赎回  
» status | integer | true | none | 状态  
» redeem_stamp | integer | true | none | 赎回到账时间  
» createStamp | integer | true | none | 订单时间  
» exchange_amount | string | true | none | 兑换汇率  
» fee | string | true | none | 手续费  
      
    
    {
      "page": 0,
      "pageSize": 0,
      "pageCount": 0,
      "totalCount": 0,
      "list": [
        {
          "pid": 0,
          "coin": "string",
          "amount": "string",
          "type": 0,
          "status": 0,
          "redeem_stamp": 0,
          "createStamp": 0,
          "exchange_amount": "string",
          "fee": "string"
        }
      ]
    }
    
    

##  AutoInvestConfigItem

_投资币种配置项_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
coin | string | true | none | 币种  
max_limit | string | true | none | 投资上限  
      
    
    {
      "coin": "string",
      "max_limit": "string"
    }
    
    

##  FixedTermHistoryRecord

_定期理财历史记录_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer | true | none | 记录ID  
order_id | integer(int64) | false | none | 订单ID  
user_id | integer(int64) | true | none | 用户ID  
asset | string | true | none | 币种  
uniq_time | string | false | none | 唯一时间标识（日期）  
bonus_id | integer | false | none | 奖励活动ID  
product_id | integer | true | none | 产品ID  
bonus_asset | string | false | none | 奖励币种  
total_principal | string | false | none | 总本金  
amount | string | false | none | 金额  
asset_price | string | false | none | 币种价格  
status | integer | true | none | 状态  
detail | string | false | none | 详情说明  
create_time | string | true | none | 创建时间  
create_at | integer | true | none | 创建时间戳（秒）  
lock_up_period | integer | false | none | 期限  
      
    
    {
      "id": 0,
      "order_id": 0,
      "user_id": 0,
      "asset": "string",
      "uniq_time": "string",
      "bonus_id": 0,
      "product_id": 0,
      "bonus_asset": "string",
      "total_principal": "string",
      "amount": "string",
      "asset_price": "string",
      "status": 0,
      "detail": "string",
      "create_time": "string",
      "create_at": 0,
      "lock_up_period": 0
    }
    
    

##  FixedTermLendOrder

_定期理财申购订单_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer | false | none | 申购记录ID  
business | integer | false | none | 业务类型，1 普通 2 vip  
order_id | integer(int64) | false | none | 订单ID  
user_id | integer(int64) | false | none | 用户ID  
asset | string | false | none | 币种  
product_id | integer | false | none | 产品ID  
lock_up_period | integer | false | none | 锁仓期限（天）  
principal | string | false | none | 申购本金  
year_rate | string | false | none | 年利率  
product_type | integer | false | none | 产品类型，1 普通 2 vip  
interest | string | false | none | 已产生利息  
status | integer | false | none | 订单状态，1 持有中 2 已赎回 3 已到期 4 已结算  
reinvest_status | integer | false | none | 复投状态，0 不复投 1 复投  
redeem_account_type | integer | false | none | 赎回到账账户类型，1 现货账户  
origin_order | string | false | none | 原始订单ID，复投场景下为前序订单ID链  
redeem_type | integer | false | none | 赎回类型，1 提前赎回 2 到期赎回  
redeem_time | string | false | none | 赎回时间  
finish_time | string | false | none | 到期时间  
create_time | string | false | none | 创建时间  
year_rate_perent | string | false | none | 年利率百分比展示值  
total_year_rate_percent | string | false | none | 综合年化收益率百分比（含加息、奖励等）  
total_interest | string | false | none | 总收益（含利息和额外奖励）  
product_info | FixedTermProductInfo | false | none | 产品配置信息  
bonus_info | FixedTermBonusInfo | false | none | 额外奖励活动信息  
coupon_info | FixedTermCouponInfo | false | none | 加息券信息  
redeem_at | integer | false | none | 赎回时间戳（秒）  
finish_at | integer | false | none | 到期时间戳（秒）  
create_at | integer | false | none | 创建时间戳（秒）  
icon | string | false | none | 币种图标URL  
      
    
    {
      "id": 0,
      "business": 0,
      "order_id": 0,
      "user_id": 0,
      "asset": "string",
      "product_id": 0,
      "lock_up_period": 0,
      "principal": "string",
      "year_rate": "string",
      "product_type": 0,
      "interest": "string",
      "status": 0,
      "reinvest_status": 0,
      "redeem_account_type": 0,
      "origin_order": "string",
      "redeem_type": 0,
      "redeem_time": "string",
      "finish_time": "string",
      "create_time": "string",
      "year_rate_perent": "string",
      "total_year_rate_percent": "string",
      "total_interest": "string",
      "product_info": {
        "pre_redeem": 0,
        "reinvest": 0,
        "redeem_account": 0,
        "min_vip": 0,
        "max_vip": 0
      },
      "bonus_info": {
        "id": 0,
        "product_id": 0,
        "asset": "string",
        "bonus_asset": "string",
        "kyc_limit": "string",
        "ladder_apr": [
          {}
        ],
        "total_bonus_amount": "string",
        "user_total_bonus_amount": "string",
        "status": 0,
        "start_time": "string",
        "end_time": "string",
        "create_time": "string",
        "start_at": 0,
        "end_at": 0,
        "total_issued_amount": "string",
        "user_total_issued_amount": "string",
        "bonus_asset_price": "string",
        "product_asset_price": "string",
        "product_year_rate": "string"
      },
      "coupon_info": {
        "id": 0,
        "business": 0,
        "user_id": 0,
        "asset": "string",
        "order_id": 0,
        "financial_rate_id": 0,
        "buy_limit_low": "string",
        "buy_limit_high": "string",
        "rate_day": 0,
        "rate_ratio": "string",
        "coupon_days": 0,
        "coupon_principal": "string",
        "coupon_year_rate": "string",
        "coupon_interest": "string",
        "status": 0,
        "finish_time": "string",
        "create_time": "string"
      },
      "redeem_at": 0,
      "finish_at": 0,
      "create_at": 0,
      "icon": "string"
    }
    
    

##  FixedTermProduct

_定期理财产品_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer | false | none | 产品ID  
name | string | false | none | 产品名称  
asset | string | false | none | 币种  
lock_up_period | integer | false | none | 锁仓期限（天）  
min_lend_amount | string | false | none | 最小理财限额  
user_max_lend_amount | string | false | none | 用户最大理财限额  
total_lend_amount | string | false | none | 平台理财限额  
year_rate | string | false | none | 年利率  
type | integer | false | none | 产品类型，1 普通 2 vip  
pre_redeem | integer | false | none | 是否支持提前赎回，0 不支持 1 支持  
reinvest | integer | false | none | 是否支持复投，0 不支持 1 支持  
redeem_account | integer | false | none | 是否支持定转活，0 不支持 1 支持  
min_vip | integer | false | none | 最低VIP等级要求，0-16，0 表示无限制  
max_vip | integer | false | none | 最高VIP等级要求，0-16，0 表示无限制  
status | integer | false | none | 产品状态，1 未上架 2 已上架 3 已下架  
create_time | string | false | none | 创建时间  
user_max_lend_volume | string | false | none | 用户最大理财量  
user_total_amount | string | false | none | 用户已理财总量  
sale_status | integer | false | none | 售卖状态，1 售卖中 2 已售罄  
      
    
    {
      "id": 0,
      "name": "string",
      "asset": "string",
      "lock_up_period": 0,
      "min_lend_amount": "string",
      "user_max_lend_amount": "string",
      "total_lend_amount": "string",
      "year_rate": "string",
      "type": 0,
      "pre_redeem": 0,
      "reinvest": 0,
      "redeem_account": 0,
      "min_vip": 0,
      "max_vip": 0,
      "status": 0,
      "create_time": "string",
      "user_max_lend_volume": "string",
      "user_total_amount": "string",
      "sale_status": 0
    }
    
    

##  FixedTermProductInfo

_产品配置信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
pre_redeem | integer | true | none | 是否支持提前赎回，0 不支持 1 支持  
reinvest | integer | true | none | 是否支持复投，0 不支持 1 支持  
redeem_account | integer | true | none | 赎回到账账户类型  
min_vip | integer | true | none | 最低VIP等级要求，0 表示无限制  
max_vip | integer | true | none | 最高VIP等级要求，0 表示无限制  
      
    
    {
      "pre_redeem": 0,
      "reinvest": 0,
      "redeem_account": 0,
      "min_vip": 0,
      "max_vip": 0
    }
    
    

##  FixedTermBonusInfo

_额外奖励活动信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer | false | none | 活动ID  
product_id | integer | false | none | 关联产品ID  
asset | string | false | none | 产品币种  
bonus_asset | string | false | none | 奖励币种  
kyc_limit | string | false | none | KYC等级限制，逗号分隔  
ladder_apr | [LadderApr] | false | none | 阶梯年化利率  
total_bonus_amount | string | false | none | 奖励总量  
user_total_bonus_amount | string | false | none | 单用户奖励上限  
status | integer | false | none | 活动状态，1 未上架 2 已上架 3 已下架  
start_time | string | false | none | 活动开始时间  
end_time | string | false | none | 活动结束时间  
create_time | string | false | none | 创建时间  
start_at | integer | false | none | 活动开始时间戳（秒）  
end_at | integer | false | none | 活动结束时间戳（秒）  
total_issued_amount | string | false | none | 已发放奖励总量  
user_total_issued_amount | string | false | none | 该用户已发放奖励总量  
bonus_asset_price | string | false | none | 奖励币种价格（USDT 计价）  
product_asset_price | string | false | none | 产品币种价格（USDT 计价）  
product_year_rate | string | false | none | 产品基础年利率  
      
    
    {
      "id": 0,
      "product_id": 0,
      "asset": "string",
      "bonus_asset": "string",
      "kyc_limit": "string",
      "ladder_apr": [
        {
          "apr": "string",
          "left": "string",
          "right": "string"
        }
      ],
      "total_bonus_amount": "string",
      "user_total_bonus_amount": "string",
      "status": 0,
      "start_time": "string",
      "end_time": "string",
      "create_time": "string",
      "start_at": 0,
      "end_at": 0,
      "total_issued_amount": "string",
      "user_total_issued_amount": "string",
      "bonus_asset_price": "string",
      "product_asset_price": "string",
      "product_year_rate": "string"
    }
    
    

##  FixedTermCouponInfo

_加息券信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer | true | none | 加息券记录ID  
business | integer | true | none | 业务类型  
user_id | integer(int64) | true | none | 用户ID  
asset | string | true | none | 币种  
order_id | integer(int64) | true | none | 关联订单ID  
financial_rate_id | integer | true | none | 加息券ID  
buy_limit_low | string | true | none | 加息券适用最低申购金额  
buy_limit_high | string | true | none | 加息券适用最高申购金额  
rate_day | integer | true | none | 加息天数  
rate_ratio | string | true | none | 加息利率百分比  
coupon_days | integer | true | none | 实际加息天数  
coupon_principal | string | true | none | 加息计算本金  
coupon_year_rate | string | true | none | 加息年化利率  
coupon_interest | string | true | none | 加息产生的利息  
status | integer | true | none | 状态，1 生效中 2 已结算  
finish_time | string | true | none | 结算时间  
create_time | string | true | none | 创建时间  
      
    
    {
      "id": 0,
      "business": 0,
      "user_id": 0,
      "asset": "string",
      "order_id": 0,
      "financial_rate_id": 0,
      "buy_limit_low": "string",
      "buy_limit_high": "string",
      "rate_day": 0,
      "rate_ratio": "string",
      "coupon_days": 0,
      "coupon_principal": "string",
      "coupon_year_rate": "string",
      "coupon_interest": "string",
      "status": 0,
      "finish_time": "string",
      "create_time": "string"
    }
    
    

##  LadderApr

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
apr | string | true | none | 年化利率  
left | string | true | none | 区间下限  
right | string | true | none | 区间上限  
      
    
    {
      "apr": "string",
      "left": "string",
      "right": "string"
    }