---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/multi-collateral-loan
api_type: REST
updated_at: 2026-05-27 20:17:26.649207
---

# Multi-collateral-loan

多币质押

##  查询多币质押订单列表🔒 需要认证

GET`/loan/multi_collateral/orders`

GET `/loan/multi_collateral/orders`

_查询多币质押订单列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
sort | 请求参数 | string | 否 | 排序类型，`time_desc` \- 默认按照创建时间降序, `ltv_asc` \- 质押率升序, `ltv_desc` \- 质押率降序  
order_type | 请求参数 | string | 否 | 订单类型，`current` \- 查询活期订单, `fixed` \- 查询定期订单，不传的话默认查询活期订单  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [MultiCollateralOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [多币质押订单]  
» _None_ | MultiCollateralOrder | 多币质押订单  
»» order_id | string | 订单id  
»» order_type | string | current - 活期，fixed - 定期  
»» fixed_type | string | 固定利率借贷周期，7d - 7日，30d - 30日  
»» fixed_rate | string | 定期利率  
»» expire_time | integer(int64) | 到期时间，时间戳，单位秒  
»» auto_renew | boolean | 固定利率，自动续借  
»» auto_repay | boolean | 固定利率，自动还款  
»» current_ltv | string | 当前质押率  
»» status | string | 订单状态:  
\- initial: 下单初始状态  
\- collateral_deducted: 扣除质押物成功  
\- collateral_returning: 放款失败-待退回质押物  
\- lent: 放款成功  
\- repaying: 还款中  
\- liquidating: 平仓中  
\- finished: 已完成  
\- closed_liquidated: 已结束-平仓还款结束  
»» borrow_time | integer(int64) | 借款时间，时间戳，单位秒  
»» total_left_repay_usdt | string | 换算成USDT后的总待还价值  
»» total_left_collateral_usdt | string | 换算成USDT后的总质押价值  
»» borrow_currencies | array | 借款币种信息列表  
»»» BorrowCurrencyInfo | object |   
»»»» currency | string | 币种  
»»»» index_price | string | 币种指数价格  
»»»» left_repay_principal | string | 待还本金  
»»»» left_repay_interest | string | 待还利息  
»»»» left_repay_usdt | string | 换算成USDT后的剩余待还总价值  
»»» collateral_currencies | array | 质押币种信息列表  
»»»» CollateralCurrencyInfo | object |   
»»»»» currency | string | 币种  
»»»»» index_price | string | 币种指数价格  
»»»»» left_collateral | string | 剩余质押数量  
»»»»» left_collateral_usdt | string | 换算成USDT后的剩余质押价值  
  
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
    
    url = '/loan/multi_collateral/orders'
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
    url="/loan/multi_collateral/orders"
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
        "order_id": "10005578",
        "order_type": "fixed",
        "fixed_type": "7d",
        "fixed_rate": 0.00001,
        "expire_time": 1703820105,
        "auto_renew": true,
        "auto_repay": true,
        "current_ltv": "0.0001004349664281",
        "status": "lent",
        "borrow_time": 1702615021,
        "total_left_repay_usdt": "106.491212982",
        "total_left_collateral_usdt": "1060300.18",
        "borrow_currencies": [
          {
            "currency": "GT",
            "index_price": "10.6491",
            "left_repay_principal": "10",
            "left_repay_interest": "0.00002",
            "left_repay_usdt": "106.491212982"
          }
        ],
        "collateral_currencies": [
          {
            "currency": "BTC",
            "index_price": "112794.7",
            "left_collateral": "9.4",
            "left_collateral_usdt": "1060270.18"
          },
          {
            "currency": "USDT",
            "index_price": "1",
            "left_collateral": "30",
            "left_collateral_usdt": "30"
          }
        ]
      }
    ]
    

##  多币质押下单🔒 需要认证

POST`/loan/multi_collateral/orders`

POST `/loan/multi_collateral/orders`

_多币质押下单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CreateMultiCollateralOrder | 是 |   
» order_id | body | string | 否 | 订单id  
» order_type | body | string | 否 | current - 活期，fixed - 定期，不传的话默认活期  
» fixed_type | body | string | 否 | 固定利率借贷周期，7d - 7日，30d - 30日, 定期时必传  
» fixed_rate | body | string | 否 | 定期利率, 定期时必传  
» auto_renew | body | boolean | 否 | 固定利率，自动续借  
» auto_repay | body | boolean | 否 | 固定利率，自动还款  
» borrow_currency | body | string | 是 | 借款币种  
» borrow_amount | body | string | 是 | 借款数量  
» collateral_currencies | body | array | 否 | 质押币种以及数量  
»» CollateralCurrency | body | object | 否 |   
»»» currency | body | string | 否 | 币种  
»»» amount | body | string | 否 | 数量  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 下单成功 | OrderResp  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» order_id | integer(int64) | 订单id  
  
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
    
    url = '/loan/multi_collateral/orders'
    query_param = ''
    body='{"order_id":1721387470,"order_type":"fixed","fixed_type":"7d","fixed_rate":0.00001,"auto_renew":true,"auto_repay":true,"borrow_currency":"BTC","borrow_amount":"1","collateral_currencies":[{"currency":"USDT","amount":"1000"}]}'
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
    url="/loan/multi_collateral/orders"
    query_param=""
    body_param='{"order_id":1721387470,"order_type":"fixed","fixed_type":"7d","fixed_rate":0.00001,"auto_renew":true,"auto_repay":true,"borrow_currency":"BTC","borrow_amount":"1","collateral_currencies":[{"currency":"USDT","amount":"1000"}]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "order_id": 1721387470,
      "order_type": "fixed",
      "fixed_type": "7d",
      "fixed_rate": 0.00001,
      "auto_renew": true,
      "auto_repay": true,
      "borrow_currency": "BTC",
      "borrow_amount": "1",
      "collateral_currencies": [
        {
          "currency": "USDT",
          "amount": "1000"
        }
      ]
    }
    

> 返回示例

> 200 返回
    
    
    {
      "order_id": 10005578
    }
    

##  查询订单详情🔒 需要认证

GET`/loan/multi_collateral/orders/{order_id}`

GET `/loan/multi_collateral/orders/{order_id}`

_查询订单详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 成功创建订单时返回的订单 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单详情查询成功 | MultiCollateralOrder  
  
### 返回格式

状态码 **200**

_多币质押订单_

名称 | 类型 | 描述  
---|---|---  
» order_id | string | 订单id  
» order_type | string | current - 活期，fixed - 定期  
» fixed_type | string | 固定利率借贷周期，7d - 7日，30d - 30日  
» fixed_rate | string | 定期利率  
» expire_time | integer(int64) | 到期时间，时间戳，单位秒  
» auto_renew | boolean | 固定利率，自动续借  
» auto_repay | boolean | 固定利率，自动还款  
» current_ltv | string | 当前质押率  
» status | string | 订单状态:  
\- initial: 下单初始状态  
\- collateral_deducted: 扣除质押物成功  
\- collateral_returning: 放款失败-待退回质押物  
\- lent: 放款成功  
\- repaying: 还款中  
\- liquidating: 平仓中  
\- finished: 已完成  
\- closed_liquidated: 已结束-平仓还款结束  
» borrow_time | integer(int64) | 借款时间，时间戳，单位秒  
» total_left_repay_usdt | string | 换算成USDT后的总待还价值  
» total_left_collateral_usdt | string | 换算成USDT后的总质押价值  
» borrow_currencies | array | 借款币种信息列表  
»» BorrowCurrencyInfo | object |   
»»» currency | string | 币种  
»»» index_price | string | 币种指数价格  
»»» left_repay_principal | string | 待还本金  
»»» left_repay_interest | string | 待还利息  
»»» left_repay_usdt | string | 换算成USDT后的剩余待还总价值  
»» collateral_currencies | array | 质押币种信息列表  
»»» CollateralCurrencyInfo | object |   
»»»» currency | string | 币种  
»»»» index_price | string | 币种指数价格  
»»»» left_collateral | string | 剩余质押数量  
»»»» left_collateral_usdt | string | 换算成USDT后的剩余质押价值  
  
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
    
    url = '/loan/multi_collateral/orders/12345'
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
    url="/loan/multi_collateral/orders/12345"
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
      "order_id": "10005578",
      "order_type": "fixed",
      "fixed_type": "7d",
      "fixed_rate": 0.00001,
      "expire_time": 1703820105,
      "auto_renew": true,
      "auto_repay": true,
      "current_ltv": "0.0001004349664281",
      "status": "lent",
      "borrow_time": 1702615021,
      "total_left_repay_usdt": "106.491212982",
      "total_left_collateral_usdt": "1060300.18",
      "borrow_currencies": [
        {
          "currency": "GT",
          "index_price": "10.6491",
          "left_repay_principal": "10",
          "left_repay_interest": "0.00002",
          "left_repay_usdt": "106.491212982"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "BTC",
          "index_price": "112794.7",
          "left_collateral": "9.4",
          "left_collateral_usdt": "1060270.18"
        },
        {
          "currency": "USDT",
          "index_price": "1",
          "left_collateral": "30",
          "left_collateral_usdt": "30"
        }
      ]
    }
    

##  查询多币质押还款记录🔒 需要认证

GET`/loan/multi_collateral/repay`

GET `/loan/multi_collateral/repay`

_查询多币质押还款记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
type | 请求参数 | string | 是 | 操作类型 ; repay - 普通还款, liquidate - 平仓  
borrow_currency | 请求参数 | string | 否 | 借款币种  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [MultiRepayRecord]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [多币质押还款记录]  
» _None_ | MultiRepayRecord | 多币质押还款记录  
»» order_id | integer(int64) | 订单id  
»» record_id | integer(int64) | 还款记录 id  
»» init_ltv | string | 初始质押率  
»» before_ltv | string | 操作前质押率  
»» after_ltv | string | 操作后质押率  
»» borrow_time | integer(int64) | 借款时间，时间戳, 秒级  
»» repay_time | integer(int64) | 还款时间，时间戳, 秒级  
»» borrow_currencies | array | 借款信息列表  
»»» currency | string | 币种  
»»» index_price | string | 币种指数价格  
»»» before_amount | string | 操作前数量  
»»» before_amount_usdt | string | 换算成usdt的操作前价值  
»»» after_amount | string | 操作后数量  
»»» after_amount_usdt | string | 换算成usdt的操作后价值  
»» collateral_currencies | array | 保证金信息列表  
»»» currency | string | 币种  
»»» index_price | string | 币种指数价格  
»»» before_amount | string | 操作前数量  
»»» before_amount_usdt | string | 换算成usdt的操作前价值  
»»» after_amount | string | 操作后数量  
»»» after_amount_usdt | string | 换算成usdt的操作后价值  
»» repaid_currencies | array | 还款币种列表  
»»» RepayRecordRepaidCurrency | object |   
»»»» currency | string | 还款币种  
»»»» index_price | string | 币种指数价格  
»»»» repaid_amount | string | 还款数量  
»»»» repaid_principal | string | 本金  
»»»» repaid_interest | string | 利息  
»»»» repaid_amount_usdt | string | 换算成usdt的还款数量  
»»» total_interest_list | array | 总计息列表  
»»»» RepayRecordTotalInterest | object |   
»»»»» currency | string | 币种  
»»»»» index_price | string | 币种指数价格  
»»»»» amount | string | 利息数量  
»»»»» amount_usdt | string | 换算成USDT的利息数量  
»»»» left_repay_interest_list | array | 剩余待还利息列表  
»»»»» RepayRecordLeftInterest | object |   
»»»»»» currency | string | 币种  
»»»»»» index_price | string | 币种指数价格  
»»»»»» before_amount | string | 还款前利息数量  
»»»»»» before_amount_usdt | string | 换算成USDT的还款前利息数量  
»»»»»» after_amount | string | 还款后利息数量  
»»»»»» after_amount_usdt | string | 换算成USDT的还款后利息数量  
  
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
    
    url = '/loan/multi_collateral/repay'
    query_param = 'type=repay'
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
    url="/loan/multi_collateral/repay"
    query_param="type=repay"
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
        "order_id": 10005679,
        "record_id": 1348,
        "init_ltv": "0.2141",
        "before_ltv": "0.215",
        "after_ltv": "0.312",
        "borrow_time": 1702995889,
        "repay_time": 1703053927,
        "borrow_currencies": [
          {
            "currency": "BAT",
            "index_price": "103.02",
            "before_amount": "1",
            "before_amount_usdt": "103.02",
            "after_amount": "0.999017",
            "after_amount_usdt": "102.91873134"
          }
        ],
        "collateral_currencies": [
          {
            "currency": "ETC",
            "index_price": "0.6014228107",
            "before_amount": "1000",
            "before_amount_usdt": "601.4228107",
            "after_amount": "1000",
            "after_amount_usdt": "601.4228107"
          }
        ],
        "repaid_currencies": [
          {
            "currency": "BAT",
            "index_price": "103.02",
            "repaid_amount": "0.001",
            "repaid_principal": "0.000983",
            "repaid_interest": "0.000017",
            "repaid_amount_usdt": "0.10302"
          }
        ],
        "total_interest_list": [
          {
            "currency": "BAT",
            "index_price": "103.02",
            "amount": "0.000017",
            "amount_usdt": "0.00175134"
          }
        ],
        "left_repay_interest_list": [
          {
            "currency": "BAT",
            "index_price": "103.02",
            "before_amount": "0.000017",
            "before_amount_usdt": "0.00175134",
            "after_amount": "0",
            "after_amount_usdt": "0"
          }
        ]
      }
    ]
    

##  多币质押还款🔒 需要认证

POST`/loan/multi_collateral/repay`

POST `/loan/multi_collateral/repay`

_多币质押还款_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | RepayMultiLoan | 是 |   
» order_id | body | integer(int64) | 是 | 订单id  
» repay_items | body | array | 是 | 还款币种项  
»» MultiLoanRepayItem | body | object | 否 |   
»»» currency | body | string | 否 | 还款币种  
»»» amount | body | string | 否 | 数量  
»»» repaid_all | body | boolean | 是 | 还款方式, 为`true`时全部还款, 为`false`时部分还款;  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 操作成功 | MultiRepayResp  
  
### 返回格式

状态码 **200**

_多币质押还款_

名称 | 类型 | 描述  
---|---|---  
» order_id | integer(int64) | 订单id  
» repaid_currencies | array | 还款币种列表  
»» RepayCurrencyRes | object |   
»»» succeeded | boolean | 是否还款成功  
»»» label | string | 操作失败时的错误标识，成功时为空  
»»» message | string | 操作失败时的错误描述，成功时为空  
»»» currency | string | 还款币种  
»»» repaid_principal | string | 本金  
»»» repaid_interest | string | 本金  
  
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
    
    url = '/loan/multi_collateral/repay'
    query_param = ''
    body='{"order_id":10005578,"repay_items":[{"currency":"btc","amount":"1","repaid_all":false}]}'
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
    url="/loan/multi_collateral/repay"
    query_param=""
    body_param='{"order_id":10005578,"repay_items":[{"currency":"btc","amount":"1","repaid_all":false}]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "order_id": 10005578,
      "repay_items": [
        {
          "currency": "btc",
          "amount": "1",
          "repaid_all": false
        }
      ]
    }
    

> 返回示例

> 200 返回
    
    
    {
      "order_id": 10005679,
      "repaid_currencies": [
        {
          "succeeded": false,
          "label": "INVALID_PARAM_VALUE",
          "message": "Invalid parameter value",
          "currency": "BTC",
          "repaid_principal": "1",
          "repaid_interest": "0.0001"
        },
        {
          "succeeded": true,
          "currency": "BTC",
          "repaid_principal": "1",
          "repaid_interest": "0.0001"
        }
      ]
    }
    

##  查询质押物调整记录🔒 需要认证

GET`/loan/multi_collateral/mortgage`

GET `/loan/multi_collateral/mortgage`

_查询质押物调整记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
collateral_currency | 请求参数 | string | 否 | 质押币种  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [MultiCollateralRecord]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [质押物调整记录]  
» _None_ | MultiCollateralRecord | 质押物调整记录  
»» order_id | integer(int64) | 订单id  
»» record_id | integer(int64) | 质押物记录 id  
»» before_ltv | string | 调整前质押率  
»» after_ltv | string | 调整前质押率  
»» operate_time | integer(int64) | 操作时间, 时间戳, 秒级  
»» borrow_currencies | array | 借款币种信息列表  
»»» currency | string | 币种  
»»» index_price | string | 币种指数价格  
»»» before_amount | string | 操作前数量  
»»» before_amount_usdt | string | 换算成usdt的操作前价值  
»»» after_amount | string | 操作后数量  
»»» after_amount_usdt | string | 换算成usdt的操作后价值  
»» collateral_currencies | array | 质押币种信息列表  
»»» currency | string | 币种  
»»» index_price | string | 币种指数价格  
»»» before_amount | string | 操作前数量  
»»» before_amount_usdt | string | 换算成usdt的操作前价值  
»»» after_amount | string | 操作后数量  
»»» after_amount_usdt | string | 换算成usdt的操作后价值  
  
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
    
    url = '/loan/multi_collateral/mortgage'
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
    url="/loan/multi_collateral/mortgage"
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
        "order_id": 10000417,
        "record_id": 10000452,
        "before_ltv": "0.00039345555621480000",
        "after_ltv": "0.00019672777810740000",
        "operate_time": 1688461924,
        "borrow_currencies": [
          {
            "currency": "BTC",
            "index_price": "30000",
            "before_amount": "0.1",
            "before_amount_usdt": "1000",
            "after_amount": "0.6",
            "after_amount_usdt": "1006"
          }
        ],
        "collateral_currencies": [
          {
            "currency": "BTC",
            "index_price": "30000",
            "before_amount": "0.1",
            "before_amount_usdt": "1000",
            "after_amount": "0.6",
            "after_amount_usdt": "1006"
          }
        ]
      }
    ]
    

##  补充或提取质押物🔒 需要认证

POST`/loan/multi_collateral/mortgage`

POST `/loan/multi_collateral/mortgage`

_补充或提取质押物_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CollateralAdjust | 是 |   
» order_id | body | integer(int64) | 是 | 订单id  
» type | body | string | 是 | 操作类型, append - 补充 , redeem - 提取  
» collaterals | body | array | 否 | 质押币种列表  
»» currency | body | string | 否 | 币种  
»» amount | body | string | 否 | 数量  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 操作成功 | CollateralAdjustRes  
  
### 返回格式

状态码 **200**

_多币质押调整质押物返回结果_

名称 | 类型 | 描述  
---|---|---  
» order_id | integer(int64) | 订单id  
» collateral_currencies | array | 质押币种信息  
»» CollateralCurrencyRes | object |   
»»» succeeded | boolean | 是否更新成功  
»»» label | string | 操作失败时的错误标识，成功时为空  
»»» message | string | 操作失败时的错误描述，成功时为空  
»»» currency | string | 币种  
»»» amount | string | 操作质押物成功的数量，操作失败时为0  
  
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
    
    url = '/loan/multi_collateral/mortgage'
    query_param = ''
    body='{"order_id":10005578,"type":"append","collaterals":[{"currency":"btc","amount":"0.5"}]}'
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
    url="/loan/multi_collateral/mortgage"
    query_param=""
    body_param='{"order_id":10005578,"type":"append","collaterals":[{"currency":"btc","amount":"0.5"}]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "order_id": 10005578,
      "type": "append",
      "collaterals": [
        {
          "currency": "btc",
          "amount": "0.5"
        }
      ]
    }
    

> 返回示例

> 200 返回
    
    
    {
      "order_id": 10005679,
      "collateral_currencies": [
        {
          "succeeded": true,
          "currency": "btc",
          "amount": "0.5"
        }
      ]
    }
    

##  查询用户质押币种和借款币种限额信息🔒 需要认证

GET`/loan/multi_collateral/currency_quota`

GET `/loan/multi_collateral/currency_quota`

_查询用户质押币种和借款币种限额信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
type | 请求参数 | string | 是 | 币种类型，collateral - 质押币种, borrow - 借款币种  
currency | 请求参数 | string | 是 | 当为质押币种时，可以用逗号分割传多个币种；当为借款币种时，只能传一个币种  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [CurrencyQuota]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [币种配额]  
» _None_ | CurrencyQuota | 币种配额  
»» currency | string | 币种  
»» index_price | string | 币种指数价格  
»» min_quota | string | 币种最小`可借/质押`限额  
»» left_quota | string | 币种剩余`可借/质押`限额(入参`type`为`borrow`时，代表活期币种)  
»» left_quote_usdt | string | 币种换算成USDT的剩余币种限额(入参`type`为`borrow`时，代表活期币种)  
»» left_quota_fixed | string | 定期币种剩余`可借/质押`限额  
»» left_quote_usdt_fixed | string | 定期币种换算成USDT的剩余币种限额  
  
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
    
    url = '/loan/multi_collateral/currency_quota'
    query_param = 'type=collateral&currency=BTC'
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
    url="/loan/multi_collateral/currency_quota"
    query_param="type=collateral&currency=BTC"
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
        "currency": "BTC",
        "index_price": "35306.1",
        "min_quota": "0",
        "left_quota": "2768152.4958445218723677",
        "left_quote_usdt": "97732668833.536273678"
      }
    ]
    

##  查询多币质押支持的借款币种和抵押币种

GET`/loan/multi_collateral/currencies`

GET `/loan/multi_collateral/currencies`

_查询多币质押支持的借款币种和抵押币种_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | MultiCollateralCurrency  
  
### 返回格式

状态码 **200**

_多币质押支持的借款币种和抵押币种_

名称 | 类型 | 描述  
---|---|---  
» loan_currencies | array | 支持的借款币种列表  
»» MultiLoanItem | object |   
»»» currency | string | 币种  
»»» price | string | 币种最新价格  
»» collateral_currencies | array | 支持的抵押币种列表  
»»» MultiCollateralItem | object |   
»»»» currency | string | 币种  
»»»» index_price | string | 币种指数价格  
»»»» discount | string | 保证金系数  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/loan/multi_collateral/currencies'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/loan/multi_collateral/currencies \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "loan_currencies": [
        {
          "currency": "BTC",
          "price": "1212"
        },
        {
          "currency": "GT",
          "price": "12"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "BTC",
          "index_price": "1212",
          "discount": "0.7"
        }
      ]
    }
    

##  查询质押率信息

GET`/loan/multi_collateral/ltv`

GET `/loan/multi_collateral/ltv`

_查询质押率信息_

多币质押质押率固定，与币种无关

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | CollateralLtv  
  
### 返回格式

状态码 **200**

_多币质押质押率_

名称 | 类型 | 描述  
---|---|---  
» init_ltv | string | 初始质押率  
» alert_ltv | string | 预警质押率  
» liquidate_ltv | string | 平仓质押率  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/loan/multi_collateral/ltv'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/loan/multi_collateral/ltv \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "init_ltv": "0.7",
      "alert_ltv": "0.8",
      "liquidate_ltv": "0.9"
    }
    

##  查询币种7日固定利率和30日固定利率

GET`/loan/multi_collateral/fixed_rate`

GET `/loan/multi_collateral/fixed_rate`

_查询币种7日固定利率和30日固定利率_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [CollateralFixRate]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [多币质押固定利率]  
» _None_ | CollateralFixRate | 多币质押固定利率  
»» currency | string | 币种  
»» rate_7d | string | 借贷周期为7天时的固定利率  
»» rate_30d | string | 借贷周期为30天时的固定利率  
»» update_time | integer(int64) | 更新时间，时间戳，单位秒  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/loan/multi_collateral/fixed_rate'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/loan/multi_collateral/fixed_rate \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency": "BTC",
        "rate_7d": "0.000023",
        "rate_30d": "0.1",
        "update_time": 1703820105
      }
    ]
    

##  查询币种活期利率

GET`/loan/multi_collateral/current_rate`

GET `/loan/multi_collateral/current_rate`

_查询币种活期利率_

查询币种上一小时活期利率，活期利率每小时更新一次

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currencies | 请求参数 | array[string] | 是 | 指定币种名称查询数组，数组用逗号分割，最大100个  
vip_level | 请求参数 | string | 否 | vip等级，不传默认为0  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [CollateralCurrentRate]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [多币质押活期利率]  
» _None_ | CollateralCurrentRate | 多币质押活期利率  
»» currency | string | 币种  
»» current_rate | string | 币种活期利率  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/loan/multi_collateral/current_rate'
    query_param = 'currencies=BTC,GT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/loan/multi_collateral/current_rate?currencies=BTC,GT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency": "BTC",
        "current_rate": "0.000023"
      }
    ]
    

#  模型

##  MultiCollateralCurrency

_多币质押支持的借款币种和抵押币种_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
loan_currencies | array | false | none | 支持的借款币种列表  
» MultiLoanItem | object | false | none | none  
»» currency | string | false | none | 币种  
»» price | string | false | none | 币种最新价格  
» collateral_currencies | array | false | none | 支持的抵押币种列表  
»» MultiCollateralItem | object | false | none | none  
»»» currency | string | false | none | 币种  
»»» index_price | string | false | none | 币种指数价格  
»»» discount | string | false | none | 保证金系数  
      
    
    {
      "loan_currencies": [
        {
          "currency": "string",
          "price": "string"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "discount": "string"
        }
      ]
    }
    
    

##  OrderResp

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | integer(int64) | false | none | 订单id  
      
    
    {
      "order_id": 0
    }
    
    

##  CollateralAdjust

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | integer(int64) | true | none | 订单id  
type | string | true | none | 操作类型, append - 补充 , redeem - 提取  
collaterals | array | false | none | 质押币种列表  
» currency | string | false | none | 币种  
» amount | string | false | none | 数量  
      
    
    {
      "order_id": 0,
      "type": "string",
      "collaterals": [
        {
          "currency": "string",
          "amount": "string"
        }
      ]
    }
    
    

##  MultiCollateralOrder

_多币质押订单_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | false | none | 订单id  
order_type | string | false | none | current - 活期，fixed - 定期  
fixed_type | string | false | none | 固定利率借贷周期，7d - 7日，30d - 30日  
fixed_rate | string | false | none | 定期利率  
expire_time | integer(int64) | false | none | 到期时间，时间戳，单位秒  
auto_renew | boolean | false | none | 固定利率，自动续借  
auto_repay | boolean | false | none | 固定利率，自动还款  
current_ltv | string | false | none | 当前质押率  
status | string | false | none | 订单状态:  
\- initial: 下单初始状态  
\- collateral_deducted: 扣除质押物成功  
\- collateral_returning: 放款失败-待退回质押物  
\- lent: 放款成功  
\- repaying: 还款中  
\- liquidating: 平仓中  
\- finished: 已完成  
\- closed_liquidated: 已结束-平仓还款结束  
borrow_time | integer(int64) | false | none | 借款时间，时间戳，单位秒  
total_left_repay_usdt | string | false | none | 换算成USDT后的总待还价值  
total_left_collateral_usdt | string | false | none | 换算成USDT后的总质押价值  
borrow_currencies | array | false | none | 借款币种信息列表  
» BorrowCurrencyInfo | object | false | none | none  
»» currency | string | false | none | 币种  
»» index_price | string | false | none | 币种指数价格  
»» left_repay_principal | string | false | none | 待还本金  
»» left_repay_interest | string | false | none | 待还利息  
»» left_repay_usdt | string | false | none | 换算成USDT后的剩余待还总价值  
» collateral_currencies | array | false | none | 质押币种信息列表  
»» CollateralCurrencyInfo | object | false | none | none  
»»» currency | string | false | none | 币种  
»»» index_price | string | false | none | 币种指数价格  
»»» left_collateral | string | false | none | 剩余质押数量  
»»» left_collateral_usdt | string | false | none | 换算成USDT后的剩余质押价值  
      
    
    {
      "order_id": "string",
      "order_type": "string",
      "fixed_type": "string",
      "fixed_rate": "string",
      "expire_time": 0,
      "auto_renew": true,
      "auto_repay": true,
      "current_ltv": "string",
      "status": "string",
      "borrow_time": 0,
      "total_left_repay_usdt": "string",
      "total_left_collateral_usdt": "string",
      "borrow_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "left_repay_principal": "string",
          "left_repay_interest": "string",
          "left_repay_usdt": "string"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "left_collateral": "string",
          "left_collateral_usdt": "string"
        }
      ]
    }
    
    

##  CreateMultiCollateralOrder

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | false | none | 订单id  
order_type | string | false | none | current - 活期，fixed - 定期，不传的话默认活期  
fixed_type | string | false | none | 固定利率借贷周期，7d - 7日，30d - 30日, 定期时必传  
fixed_rate | string | false | none | 定期利率, 定期时必传  
auto_renew | boolean | false | none | 固定利率，自动续借  
auto_repay | boolean | false | none | 固定利率，自动还款  
borrow_currency | string | true | none | 借款币种  
borrow_amount | string | true | none | 借款数量  
collateral_currencies | array | false | none | 质押币种以及数量  
» CollateralCurrency | object | false | none | none  
»» currency | string | false | none | 币种  
»» amount | string | false | none | 数量  
      
    
    {
      "order_id": "string",
      "order_type": "string",
      "fixed_type": "string",
      "fixed_rate": "string",
      "auto_renew": true,
      "auto_repay": true,
      "borrow_currency": "string",
      "borrow_amount": "string",
      "collateral_currencies": [
        {
          "currency": "string",
          "amount": "string"
        }
      ]
    }
    
    

##  CurrencyQuota

_币种配额_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种  
index_price | string | false | none | 币种指数价格  
min_quota | string | false | none | 币种最小`可借/质押`限额  
left_quota | string | false | none | 币种剩余`可借/质押`限额(入参`type`为`borrow`时，代表活期币种)  
left_quote_usdt | string | false | none | 币种换算成USDT的剩余币种限额(入参`type`为`borrow`时，代表活期币种)  
left_quota_fixed | string | false | none | 定期币种剩余`可借/质押`限额  
left_quote_usdt_fixed | string | false | none | 定期币种换算成USDT的剩余币种限额  
      
    
    {
      "currency": "string",
      "index_price": "string",
      "min_quota": "string",
      "left_quota": "string",
      "left_quote_usdt": "string",
      "left_quota_fixed": "string",
      "left_quote_usdt_fixed": "string"
    }
    
    

##  CollateralFixRate

_多币质押固定利率_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种  
rate_7d | string | false | none | 借贷周期为7天时的固定利率  
rate_30d | string | false | none | 借贷周期为30天时的固定利率  
update_time | integer(int64) | false | none | 更新时间，时间戳，单位秒  
      
    
    {
      "currency": "string",
      "rate_7d": "string",
      "rate_30d": "string",
      "update_time": 0
    }
    
    

##  MultiRepayResp

_多币质押还款_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | integer(int64) | false | none | 订单id  
repaid_currencies | array | false | none | 还款币种列表  
» RepayCurrencyRes | object | false | none | none  
»» succeeded | boolean | false | none | 是否还款成功  
»» label | string | false | none | 操作失败时的错误标识，成功时为空  
»» message | string | false | none | 操作失败时的错误描述，成功时为空  
»» currency | string | false | none | 还款币种  
»» repaid_principal | string | false | none | 本金  
»» repaid_interest | string | false | none | 本金  
      
    
    {
      "order_id": 0,
      "repaid_currencies": [
        {
          "succeeded": true,
          "label": "string",
          "message": "string",
          "currency": "string",
          "repaid_principal": "string",
          "repaid_interest": "string"
        }
      ]
    }
    
    

##  MultiRepayRecord

_多币质押还款记录_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | integer(int64) | false | none | 订单id  
record_id | integer(int64) | false | none | 还款记录 id  
init_ltv | string | false | none | 初始质押率  
before_ltv | string | false | none | 操作前质押率  
after_ltv | string | false | none | 操作后质押率  
borrow_time | integer(int64) | false | none | 借款时间，时间戳, 秒级  
repay_time | integer(int64) | false | none | 还款时间，时间戳, 秒级  
borrow_currencies | array | false | none | 借款信息列表  
» currency | string | false | none | 币种  
» index_price | string | false | none | 币种指数价格  
» before_amount | string | false | none | 操作前数量  
» before_amount_usdt | string | false | none | 换算成usdt的操作前价值  
» after_amount | string | false | none | 操作后数量  
» after_amount_usdt | string | false | none | 换算成usdt的操作后价值  
collateral_currencies | [MultiRepayRecord/properties/borrow_currencies/items] | false | none | 保证金信息列表  
repaid_currencies | array | false | none | 还款币种列表  
» RepayRecordRepaidCurrency | object | false | none | none  
»» currency | string | false | none | 还款币种  
»» index_price | string | false | none | 币种指数价格  
»» repaid_amount | string | false | none | 还款数量  
»» repaid_principal | string | false | none | 本金  
»» repaid_interest | string | false | none | 利息  
»» repaid_amount_usdt | string | false | none | 换算成usdt的还款数量  
» total_interest_list | array | false | none | 总计息列表  
»» RepayRecordTotalInterest | object | false | none | none  
»»» currency | string | false | none | 币种  
»»» index_price | string | false | none | 币种指数价格  
»»» amount | string | false | none | 利息数量  
»»» amount_usdt | string | false | none | 换算成USDT的利息数量  
»» left_repay_interest_list | array | false | none | 剩余待还利息列表  
»»» RepayRecordLeftInterest | object | false | none | none  
»»»» currency | string | false | none | 币种  
»»»» index_price | string | false | none | 币种指数价格  
»»»» before_amount | string | false | none | 还款前利息数量  
»»»» before_amount_usdt | string | false | none | 换算成USDT的还款前利息数量  
»»»» after_amount | string | false | none | 还款后利息数量  
»»»» after_amount_usdt | string | false | none | 换算成USDT的还款后利息数量  
      
    
    {
      "order_id": 0,
      "record_id": 0,
      "init_ltv": "string",
      "before_ltv": "string",
      "after_ltv": "string",
      "borrow_time": 0,
      "repay_time": 0,
      "borrow_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ],
      "repaid_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "repaid_amount": "string",
          "repaid_principal": "string",
          "repaid_interest": "string",
          "repaid_amount_usdt": "string"
        }
      ],
      "total_interest_list": [
        {
          "currency": "string",
          "index_price": "string",
          "amount": "string",
          "amount_usdt": "string"
        }
      ],
      "left_repay_interest_list": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ]
    }
    
    

##  CollateralAdjustRes

_多币质押调整质押物返回结果_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | integer(int64) | false | none | 订单id  
collateral_currencies | array | false | none | 质押币种信息  
» CollateralCurrencyRes | object | false | none | none  
»» succeeded | boolean | false | none | 是否更新成功  
»» label | string | false | none | 操作失败时的错误标识，成功时为空  
»» message | string | false | none | 操作失败时的错误描述，成功时为空  
»» currency | string | false | none | 币种  
»» amount | string | false | none | 操作质押物成功的数量，操作失败时为0  
      
    
    {
      "order_id": 0,
      "collateral_currencies": [
        {
          "succeeded": true,
          "label": "string",
          "message": "string",
          "currency": "string",
          "amount": "string"
        }
      ]
    }
    
    

##  RepayMultiLoan

_多币质押还款_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | integer(int64) | true | none | 订单id  
repay_items | array | true | none | 还款币种项  
» MultiLoanRepayItem | object | false | none | none  
»» currency | string | false | none | 还款币种  
»» amount | string | false | none | 数量  
»» repaid_all | boolean | true | none | 还款方式, 为`true`时全部还款, 为`false`时部分还款;  
      
    
    {
      "order_id": 0,
      "repay_items": [
        {
          "currency": "string",
          "amount": "string",
          "repaid_all": true
        }
      ]
    }
    
    

##  CollateralLtv

_多币质押质押率_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
init_ltv | string | false | none | 初始质押率  
alert_ltv | string | false | none | 预警质押率  
liquidate_ltv | string | false | none | 平仓质押率  
      
    
    {
      "init_ltv": "string",
      "alert_ltv": "string",
      "liquidate_ltv": "string"
    }
    
    

##  CollateralCurrentRate

_多币质押活期利率_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种  
current_rate | string | false | none | 币种活期利率  
      
    
    {
      "currency": "string",
      "current_rate": "string"
    }
    
    

##  MultiCollateralRecord

_质押物调整记录_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | integer(int64) | false | none | 订单id  
record_id | integer(int64) | false | none | 质押物记录 id  
before_ltv | string | false | none | 调整前质押率  
after_ltv | string | false | none | 调整前质押率  
operate_time | integer(int64) | false | none | 操作时间, 时间戳, 秒级  
borrow_currencies | array | false | none | 借款币种信息列表  
» currency | string | false | none | 币种  
» index_price | string | false | none | 币种指数价格  
» before_amount | string | false | none | 操作前数量  
» before_amount_usdt | string | false | none | 换算成usdt的操作前价值  
» after_amount | string | false | none | 操作后数量  
» after_amount_usdt | string | false | none | 换算成usdt的操作后价值  
collateral_currencies | [MultiCollateralRecord/properties/borrow_currencies/items] | false | none | 质押币种信息列表  
      
    
    {
      "order_id": 0,
      "record_id": 0,
      "before_ltv": "string",
      "after_ltv": "string",
      "operate_time": 0,
      "borrow_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ]
    }