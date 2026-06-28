---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/otc
api_type: REST
updated_at: 2026-05-27 20:17:35.690639
---

# OTC

* Python 
  * Shell 


OTC交易

##  法币和稳定币询价🔒 需要认证

POST`/otc/quote`

POST `/otc/quote`

_法币和稳定币询价_

创建法币和稳定币询价，支持PAY和GET两种询价方向

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcQuoteRequest | 是 |   
» side | body | string | 是 | PAY/GET 询价方向 PAY 代表用户输入pay amount GET 代表用户输入get amount。如果是PAY pay amount 必传。如果是GET get amount 必传  
» pay_coin | body | string | 是 | 用户支付币种 支持币种 从otc web 询价页面查询  
» get_coin | body | string | 是 | 用户兑换币种 支持币种 从otc web 询价页面查询  
» pay_amount | body | string | 否 | 用户支付币种数量  
» get_amount | body | string | 否 | 用户兑换币种数量  
» create_quote_token | body | string | 否 | 创建询价token 0:询价预览 1:创建询价token 用于下单  
» promotion_code | body | string | 否 | 优惠码 选填  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 询价成功 | OtcQuoteResponse  
  
### 返回格式

状态码 **200**

_OtcQuoteResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» data | object |   
»» type | string | BUY 入金 SELL 出金  
»» pay_coin | string | 支付币种  
»» get_coin | string | 兑换币种  
»» pay_amount | string | 支付金额  
»» get_amount | string | 兑换金额  
»» rate | string | 汇率  
»» rate_reci | string | 汇率倒数  
»» promotion_code | string | 优惠码  
»» side | string | 询价方式  
»» order_type | string | 订单类型 FIAT 法币 /STABLE 稳定币  
»» quote_token | string | 下单时需要用到的询价token  
  
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
    
    url = '/otc/quote'
    query_param = ''
    body='{"side":"PAY","pay_coin":"USDT","get_coin":"USD","pay_amount":"30000","get_amount":"30000","create_quote_token":"0","promotion_code":""}'
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
    url="/otc/quote"
    query_param=""
    body_param='{"side":"PAY","pay_coin":"USDT","get_coin":"USD","pay_amount":"30000","get_amount":"30000","create_quote_token":"0","promotion_code":""}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "side": "PAY",
      "pay_coin": "USDT",
      "get_coin": "USD",
      "pay_amount": "30000",
      "get_amount": "30000",
      "create_quote_token": "0",
      "promotion_code": ""
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "url": "",
        "memo": "",
        "type": "BUY",
        "pay_coin": "USD",
        "get_coin": "USDT",
        "pay_amount": "30000.00",
        "get_amount": "29891.00",
        "rate": "1.0036",
        "rate_reci": "0.9964",
        "promotion_code": "",
        "side": "PAY",
        "has_signature": "0",
        "validity_period": "300",
        "ex_rate": "0.9967",
        "usdc_rate": "0.99990000",
        "is_need_file": "0",
        "gate_bank_id": "1",
        "gate_bank_name": "",
        "order_type": "FIAT",
        "quote_token": "",
        "refresh_limit": 20,
        "refresh_limit_msg": ""
      },
      "timestamp": 1752051076
    }
    

##  法币下单🔒 需要认证

POST`/otc/order/create`

POST `/otc/order/create`

_法币下单_

创建法币订单，支持BUY入金和SELL出金

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcOrderRequest | 是 |   
» type | body | string | 是 | BUY 入金 SELL 出金  
» side | body | string | 是 | 询价 接口返回的参数 side （用户下单校验）  
» crypto_currency | body | string | 是 | 数字货币币种 支持币种从otc web 法币 询价页面查询  
» fiat_currency | body | string | 是 | 法币币种 支持币种从otc web 法币询价页面查询  
» crypto_amount | body | string | 是 | 数字货币数量  
» fiat_amount | body | string | 是 | 法币数量  
» promotion_code | body | string | 否 | 优惠码  
» quote_token | body | string | 是 | 询价接口返回参数  
» bank_id | body | string | 是 | 用户下单使用的银行卡ID 通过获取默认银行卡接口获取  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单创建成功 | OtcActionResponse  
  
### 返回格式

状态码 **200**

_OtcActionResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» timestamp | integer |   
  
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
    
    url = '/otc/order/create'
    query_param = ''
    body='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2"}'
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
    url="/otc/order/create"
    query_param=""
    body_param='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "type": "BUY",
      "side": "FIAT",
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "crypto_amount": "30000",
      "fiat_amount": "30000",
      "promotion_code": "",
      "quote_token": "",
      "bank_id": "2"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "success",
      "timestamp": 1752051076
    }
    

##  稳定币下单🔒 需要认证

POST`/otc/stable_coin/order/create`

POST `/otc/stable_coin/order/create`

_稳定币下单_

创建稳定币订单

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcStableCoinOrderRequest | 是 |   
» pay_coin | body | string | 否 | 用户支付币种 支持币种 从otc web 稳定币询价页面查询  
» get_coin | body | string | 否 | 用户兑换币种 支持币种 从otc web 稳定币询价页面查询  
» pay_amount | body | string | 否 | 用户支付币种数量  
» get_amount | body | string | 否 | 用户兑换币种数量  
» side | body | string | 否 | 询价 接口返回的参数 side （用户下单校验）  
» promotion_code | body | string | 否 | promotion code  
» quote_token | body | string | 否 | 询价接口返回参数  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 稳定币订单创建成功 | OtcStableCoinOrderCreateResponse  
  
### 返回格式

状态码 **200**

_OtcStableCoinOrderCreateResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
  
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
    
    url = '/otc/stable_coin/order/create'
    query_param = ''
    body='{"pay_coin":"USDC","get_coin":"USDT","pay_amount":"30000","get_amount":"20000","side":"PAY","promotion_code":"","quote_token":"dsafjkdshfjdsjkfah"}'
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
    url="/otc/stable_coin/order/create"
    query_param=""
    body_param='{"pay_coin":"USDC","get_coin":"USDT","pay_amount":"30000","get_amount":"20000","side":"PAY","promotion_code":"","quote_token":"dsafjkdshfjdsjkfah"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "pay_coin": "USDC",
      "get_coin": "USDT",
      "pay_amount": "30000",
      "get_amount": "20000",
      "side": "PAY",
      "promotion_code": "",
      "quote_token": "dsafjkdshfjdsjkfah"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "string"
    }
    

##  获取用户默认银行卡信息🔒 需要认证

GET`/otc/get_user_def_bank`

GET `/otc/get_user_def_bank`

_获取用户默认银行卡信息_

获取用户默认银行卡信息，用于下单时选择银行卡

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OtcUserDefaultBankResponse  
  
### 返回格式

状态码 **200**

_OtcUserDefaultBankResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» data | object |   
»» id | string | 银行ID 下单时候需要  
»» bank_account_name | string |   
»» bank_name | string |   
»» bank_country | string |   
»» bank_address | string |   
»» bank_code | string |   
»» branch_code | string |   
» timestamp | integer |   
  
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
    
    url = '/otc/get_user_def_bank'
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
    url="/otc/get_user_def_bank"
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
      "code": 0,
      "message": "success",
      "data": {
        "show": 1,
        "message": "test",
        "url": "/otc/apply_person"
      },
      "timestamp": 1751434613
    }
    

##  获取用户银行卡列表🔒 需要认证

GET`/otc/bank_list`

GET `/otc/bank_list`

_获取用户银行卡列表_

获取用户银行卡列表，用于下单时选择银行卡

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OtcBankListResponse  
  
### 返回格式

状态码 **200**

_OtcBankListResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» data | object |   
»» lists | array | 银行卡列表  
»»» OtcBankListItem | object |   
»»»» id | string | 银行ID 下单时候需要  
»»»» bank_account_name | string | 银行账户名称  
»»»» bank_name | string | 银行名称  
»»»» bank_country | string | 银行所在国家  
»»»» bank_address | string | 银行地址  
»»»» bank_code | string | 银行代码  
»»»» branch_code | string | 支行代码  
»»»» iban | string | IBAN号码  
»»»» swift | string | SWIFT代码  
»»»» remittance_line_number | string | 汇款路线号  
»»»» agent_bank_name | string | 代理银行名称  
»»»» agent_bank_swift | string | 代理银行SWIFT代码  
»»»» submit_time | string | 提交时间  
»»»» update_time | string | 更新时间  
»»»» status | string | 状态  
»»»» documentation_file_type | string | 文档文件类型  
»»»» memo | string | 备注  
»»»» is_default | integer | 是否默认银行卡 1是 0否  
»»»» bank_id | string | 银行ID  
»»»» documentation_file_key_url | string | 文档文件URL  
»»» timestamp | integer |   
  
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
    
    url = '/otc/bank_list'
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
    url="/otc/bank_list"
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
      "code": 0,
      "message": "success",
      "data": {
        "lists": [
          {
            "id": "762",
            "bank_account_name": "hshsbshhh",
            "bank_name": "jjjsjhs",
            "bank_country": "Anguilla",
            "bank_address": "jshhtestaddress879hao",
            "bank_code": "",
            "branch_code": "",
            "iban": "1554 **** 8756",
            "swift": "455876663",
            "remittance_line_number": "4867645497945",
            "agent_bank_name": "",
            "agent_bank_swift": "",
            "submit_time": "2026-01-21 05:56:49",
            "update_time": "2026-01-21 05:57:09",
            "status": "1",
            "documentation_file_type": "",
            "memo": "",
            "is_default": 1,
            "bank_id": "762",
            "documentation_file_key_url": ""
          }
        ]
      },
      "timestamp": 1769998217
    }
    

##  法币订单设置已付款🔒 需要认证

POST`/otc/order/paid`

POST `/otc/order/paid`

_法币订单设置已付款_

标记法币订单为已付款状态

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcMarkOrderPaidRequest | 是 |   
» order_id | body | string | 是 | 订单 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单已标记为已付款 | OtcActionResponse  
  
### 返回格式

状态码 **200**

_OtcActionResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» timestamp | integer |   
  
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
    
    url = '/otc/order/paid'
    query_param = ''
    body='{"order_id":"203"}'
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
    url="/otc/order/paid"
    query_param=""
    body_param='{"order_id":"203"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "order_id": "203"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "success",
      "timestamp": 1752051076
    }
    

##  法币订单取消🔒 需要认证

POST`/otc/order/cancel`

POST `/otc/order/cancel`

_法币订单取消_

取消法币订单

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | 请求参数 | string | 是 | 订单ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单取消成功 | OtcActionResponse  
  
### 返回格式

状态码 **200**

_OtcActionResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» timestamp | integer |   
  
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
    
    url = '/otc/order/cancel'
    query_param = 'order_id=string'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/order/cancel"
    query_param="order_id=string"
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
      "message": "success",
      "timestamp": 1752051076
    }
    

##  法币订单列表🔒 需要认证

GET`/otc/order/list`

GET `/otc/order/list`

_法币订单列表_

查询法币订单列表，支持按类型、币种、时间范围、状态等条件筛选

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
type | 请求参数 | string | 否 | BUY 入金 SELL 出金  
fiat_currency | 请求参数 | string | 否 | 法币币种  
crypto_currency | 请求参数 | string | 否 | 数字货币币种  
start_time | 请求参数 | string | 否 | 开始时间 for example : 2025-09-09  
end_time | 请求参数 | string | 否 | 结束时间 for example :2025-09-09  
status | 请求参数 | string | 否 | DONE ：完成  
CANCEL ：取消  
PROCESSING ：进行中  
pn | 请求参数 | string | 否 | 分页第几页  
ps | 请求参数 | string | 否 | 分页每页显示数量  
  
####  详细描述

**status** : DONE ：完成  
CANCEL ：取消  
PROCESSING ：进行中

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OtcOrderListResponse  
  
### 返回格式

状态码 **200**

_OtcOrderListResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» data | object |   
»» pn | integer |   
»» ps | integer |   
»» total_pn | integer |   
»» count | integer |   
»» list | array |   
»»» OtcOrderListItem | object |   
»»»» time | string | 当前时间  
»»»» timestamp | integer | 当前时间戳  
»»»» order_id | string | 订单Id  
»»»» trade_no | string | 交易号  
»»»» type | string | 询价方向 buy/sell/all  
»»»» status | string | 订单状态  
»»»» db_status | string |   
»»»» fiat_currency | string | 法币类型  
»»»» fiat_currency_info | object |   
»»»»» name | string | 名称  
»»»»» icon | string | 图片  
»»»» fiat_amount | string | 法币金额  
»»»» crypto_currency | string | 稳定币类型  
»»»» crypto_currency_info | object |   
»»»»» name | string |   
»»»»» icon | string |   
»»»» crypto_amount | string | 稳定币金额  
»»»» rate | string | 汇率  
»»»» transfer_remark | string | 备注  
»»»» gate_bank_account_iban | string | 银行账户  
»»»» promotion_code | string | 优惠码  
  
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
    
    url = '/otc/order/list'
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
    url="/otc/order/list"
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
      "code": 0,
      "message": "Success",
      "data": {
        "pn": 1,
        "ps": 10,
        "total_pn": 1,
        "count": 2,
        "list": [
          {
            "time": "2025-02-11 07:45:06",
            "timestamp": 1739000013,
            "order_id": "41",
            "trade_no": "20250207043457590939",
            "type": "SELL",
            "status": "PROCESSIONG",
            "db_status": "PAID",
            "fiat_currency": "USD",
            "fiat_currency_info": {
              "name": "USD",
              "icon": "http://icon.url"
            },
            "fiat_amount": "199600",
            "ceypto_currency": "USDT",
            "crypto_currency_info": {
              "name": "USDT",
              "icon": "http://icon.url"
            },
            "crypto_amount": "200000",
            "rate": "0.998000",
            "transfer_remark": "",
            "gate_bank_account_iban": "89b9b9b9b",
            "promotion_code": ""
          }
        ]
      }
    }
    

##  稳定币订单列表🔒 需要认证

GET`/otc/stable_coin/order/list`

GET `/otc/stable_coin/order/list`

_稳定币订单列表_

查询稳定币订单列表，支持按币种、时间范围、状态等条件筛选

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page_size | 请求参数 | string | 否 | 分页 每页显示数量  
page_number | 请求参数 | string | 否 | 分页 第几页  
coin_name | 请求参数 | string | 否 | 订单币种  
start_time | 请求参数 | string | 否 | 开始时间  
end_time | 请求参数 | string | 否 | 结束时间  
status | 请求参数 | string | 否 | 状态 PROCESSING 进行中 / DONE 完成 / FAILED 失败  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OtcStableCoinOrderListResponse  
  
### 返回格式

状态码 **200**

_OtcStableCoinOrderListResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» data | object |   
»» total | integer |   
»» page_size | integer |   
»» page_number | integer |   
»» total_page | integer |   
»» list | array |   
»»» OtcStableCoinOrderListItem | object |   
»»»» id | integer | 订单ID  
»»»» trade_no | string | 交易流水号  
»»»» pay_coin | string | 支付币种  
»»»» pay_amount | string | 支付金额  
»»»» get_coin | string | 获得币种  
»»»» get_amount | string | 获得金额  
»»»» rate | string | 汇率  
»»»» rate_reci | string | 汇率倒数  
»»»» status | string | PROCESSING 进行中/ DONE 完成 / FAILED失败  
»»»» create_timest | integer | 时间时间戳  
»»»» create_time | string | 创建时间  
  
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
    
    url = '/otc/stable_coin/order/list'
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
    url="/otc/stable_coin/order/list"
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
      "code": 0,
      "message": "success",
      "data": {
        "total": 20,
        "page_size": 10,
        "page_number": 1,
        "total_page": 10,
        "list": [
          {
            "id": 1,
            "trade_no": "89875324974",
            "pay_coin": "USDT",
            "pay_icon": "https://icon.com",
            "pay_amount": "30000.00",
            "get_coin": "JDUSD",
            "get_icon": "https://icon.com",
            "get_amount": "20000.00",
            "rate": "1.5",
            "rate_reci": "0.6667",
            "status": "PROCESSING",
            "create_timest": 17878979789,
            "create_time": "2025-09-09 10:00:00"
          }
        ]
      }
    }
    

##  法币订单详情🔒 需要认证

GET`/otc/order/detail`

GET `/otc/order/detail`

_法币订单详情_

查询法币订单详情信息

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | 请求参数 | string | 是 | 订单ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OtcOrderDetailResponse  
  
### 返回格式

状态码 **200**

_OtcOrderDetailResponse_

名称 | 类型 | 描述  
---|---|---  
» message | string |   
» code | integer |   
» data | object |   
»» order_id | string | 订单ID  
»» uid | string | 用户ID  
»» type | string | 订单类型  
»» fiat_currency | string | 法币类型  
»» fiat_amount | string | 法币金额  
»» crypto_currency | string | 稳定币类型  
»» crypto_amount | string | 稳定币金额  
»» rate | string | 汇率  
»» transfer_remark | string | 备注  
»» status | string | 状态  
»» db_status | string |   
»» create_time | string | 创建时间  
»» memo | string | 取消或拒绝原因  
»» side | string | 询价方向  
»» promotion_code | string | 优惠码  
»» trade_no | string | 交易号  
  
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
    
    url = '/otc/order/detail'
    query_param = 'order_id=string'
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
    url="/otc/order/detail"
    query_param="order_id=string"
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
      "message": "成功",
      "code": 0,
      "data": {
        "order_id": "265",
        "uid": "2124269088",
        "type": "BUY",
        "fiat_currency": "USD",
        "fiat_amount": "300000",
        "crypto_currency": "USDT",
        "crypto_amount": "299700",
        "rate": "1.001001",
        "transfer_remark": "Bank Code: 016, Branch Code: 478",
        "status": "PROCESSIONG",
        "db_status": "PAID",
        "create_time": "2025-03-07 07:51:52",
        "memo": "",
        "side": "FIAT",
        "promotion_code": "",
        "trade_no": "20250307075152206853"
      }
    }
    

#  模型

##  OtcActionResponse

_OtcActionResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | none  
message | string | true | none | none  
timestamp | integer | true | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    
    

##  OtcStableCoinOrderListResponse

_OtcStableCoinOrderListResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | none  
message | string | true | none | none  
data | object | true | none | none  
» total | integer | true | none | none  
» page_size | integer | true | none | none  
» page_number | integer | true | none | none  
» total_page | integer | true | none | none  
» list | array | true | none | none  
»» OtcStableCoinOrderListItem | object | false | none | none  
»»» id | integer | false | none | 订单ID  
»»» trade_no | string | false | none | 交易流水号  
»»» pay_coin | string | false | none | 支付币种  
»»» pay_amount | string | false | none | 支付金额  
»»» get_coin | string | false | none | 获得币种  
»»» get_amount | string | false | none | 获得金额  
»»» rate | string | false | none | 汇率  
»»» rate_reci | string | false | none | 汇率倒数  
»»» status | string | false | none | PROCESSING 进行中/ DONE 完成 / FAILED失败  
»»» create_timest | integer | false | none | 时间时间戳  
»»» create_time | string | false | none | 创建时间  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "total": 0,
        "page_size": 0,
        "page_number": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      }
    }
    
    

##  OtcMarkOrderPaidRequest

_法币订单设置已付款请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | true | none | 订单 ID  
      
    
    {
      "order_id": "203"
    }
    
    

##  OtcStableCoinOrderRequest

_稳定币下单请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
pay_coin | string | false | none | 用户支付币种 支持币种 从otc web 稳定币询价页面查询  
get_coin | string | false | none | 用户兑换币种 支持币种 从otc web 稳定币询价页面查询  
pay_amount | string | false | none | 用户支付币种数量  
get_amount | string | false | none | 用户兑换币种数量  
side | string | false | none | 询价 接口返回的参数 side （用户下单校验）  
promotion_code | string | false | none | promotion code  
quote_token | string | false | none | 询价接口返回参数  
      
    
    {
      "pay_coin": "USDC",
      "get_coin": "USDT",
      "pay_amount": "30000",
      "get_amount": "20000",
      "side": "PAY",
      "promotion_code": "",
      "quote_token": "dsafjkdshfjdsjkfah"
    }
    
    

##  OtcUserDefaultBankResponse

_OtcUserDefaultBankResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | none  
message | string | true | none | none  
data | object | true | none | none  
» id | string | true | none | 银行ID 下单时候需要  
» bank_account_name | string | true | none | none  
» bank_name | string | true | none | none  
» bank_country | string | true | none | none  
» bank_address | string | true | none | none  
» bank_code | string | true | none | none  
» branch_code | string | true | none | none  
timestamp | integer | true | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "id": "string",
        "bank_account_name": "string",
        "bank_name": "string",
        "bank_country": "string",
        "bank_address": "string",
        "bank_code": "string",
        "branch_code": "string"
      },
      "timestamp": 0
    }
    
    

##  OtcQuoteRequest

_法币和稳定币询价请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
side | string | true | none | PAY/GET 询价方向 PAY 代表用户输入pay amount GET 代表用户输入get amount。如果是PAY pay amount 必传。如果是GET get amount 必传  
pay_coin | string | true | none | 用户支付币种 支持币种 从otc web 询价页面查询  
get_coin | string | true | none | 用户兑换币种 支持币种 从otc web 询价页面查询  
pay_amount | string | false | none | 用户支付币种数量  
get_amount | string | false | none | 用户兑换币种数量  
create_quote_token | string | false | none | 创建询价token 0:询价预览 1:创建询价token 用于下单  
promotion_code | string | false | none | 优惠码 选填  
      
    
    {
      "side": "PAY",
      "pay_coin": "USDT",
      "get_coin": "USD",
      "pay_amount": "30000",
      "get_amount": "30000",
      "create_quote_token": "0",
      "promotion_code": ""
    }
    
    

##  OtcOrderDetailResponse

_OtcOrderDetailResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
message | string | true | none | none  
code | integer | true | none | none  
data | object | true | none | none  
» order_id | string | true | none | 订单ID  
» uid | string | true | none | 用户ID  
» type | string | true | none | 订单类型  
» fiat_currency | string | true | none | 法币类型  
» fiat_amount | string | true | none | 法币金额  
» crypto_currency | string | true | none | 稳定币类型  
» crypto_amount | string | true | none | 稳定币金额  
» rate | string | true | none | 汇率  
» transfer_remark | string | true | none | 备注  
» status | string | true | none | 状态  
» db_status | string | true | none | none  
» create_time | string | true | none | 创建时间  
» memo | string | true | none | 取消或拒绝原因  
» side | string | true | none | 询价方向  
» promotion_code | string | true | none | 优惠码  
» trade_no | string | true | none | 交易号  
      
    
    {
      "message": "string",
      "code": 0,
      "data": {
        "order_id": "string",
        "uid": "string",
        "type": "string",
        "fiat_currency": "string",
        "fiat_amount": "string",
        "crypto_currency": "string",
        "crypto_amount": "string",
        "rate": "string",
        "transfer_remark": "string",
        "status": "string",
        "db_status": "string",
        "create_time": "string",
        "memo": "string",
        "side": "string",
        "promotion_code": "string",
        "trade_no": "string"
      }
    }
    
    

##  OtcBankListResponse

_OtcBankListResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | none  
message | string | true | none | none  
data | object | true | none | none  
» lists | array | true | none | 银行卡列表  
»» OtcBankListItem | object | false | none | none  
»»» id | string | true | none | 银行ID 下单时候需要  
»»» bank_account_name | string | true | none | 银行账户名称  
»»» bank_name | string | true | none | 银行名称  
»»» bank_country | string | false | none | 银行所在国家  
»»» bank_address | string | false | none | 银行地址  
»»» bank_code | string | false | none | 银行代码  
»»» branch_code | string | false | none | 支行代码  
»»» iban | string | false | none | IBAN号码  
»»» swift | string | false | none | SWIFT代码  
»»» remittance_line_number | string | false | none | 汇款路线号  
»»» agent_bank_name | string | false | none | 代理银行名称  
»»» agent_bank_swift | string | false | none | 代理银行SWIFT代码  
»»» submit_time | string | false | none | 提交时间  
»»» update_time | string | false | none | 更新时间  
»»» status | string | false | none | 状态  
»»» documentation_file_type | string | false | none | 文档文件类型  
»»» memo | string | false | none | 备注  
»»» is_default | integer | false | none | 是否默认银行卡 1是 0否  
»»» bank_id | string | false | none | 银行ID  
»»» documentation_file_key_url | string | false | none | 文档文件URL  
»» timestamp | integer | true | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "lists": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  OtcOrderListResponse

_OtcOrderListResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | none  
message | string | true | none | none  
data | object | true | none | none  
» pn | integer | true | none | none  
» ps | integer | true | none | none  
» total_pn | integer | true | none | none  
» count | integer | true | none | none  
» list | array | true | none | none  
»» OtcOrderListItem | object | false | none | none  
»»» time | string | false | none | 当前时间  
»»» timestamp | integer | false | none | 当前时间戳  
»»» order_id | string | false | none | 订单Id  
»»» trade_no | string | false | none | 交易号  
»»» type | string | false | none | 询价方向 buy/sell/all  
»»» status | string | false | none | 订单状态  
»»» db_status | string | false | none | none  
»»» fiat_currency | string | false | none | 法币类型  
»»» fiat_currency_info | object | false | none | none  
»»»» name | string | true | none | 名称  
»»»» icon | string | true | none | 图片  
»»» fiat_amount | string | false | none | 法币金额  
»»» crypto_currency | string | false | none | 稳定币类型  
»»» crypto_currency_info | object | false | none | none  
»»»» name | string | true | none | none  
»»»» icon | string | true | none | none  
»»» crypto_amount | string | false | none | 稳定币金额  
»»» rate | string | false | none | 汇率  
»»» transfer_remark | string | false | none | 备注  
»»» gate_bank_account_iban | string | false | none | 银行账户  
»»» promotion_code | string | false | none | 优惠码  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "pn": 0,
        "ps": 0,
        "total_pn": 0,
        "count": 0,
        "list": [
          {}
        ]
      }
    }
    
    

##  OtcQuoteResponse

_OtcQuoteResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | none  
message | string | true | none | none  
data | object | true | none | none  
» type | string | true | none | BUY 入金 SELL 出金  
» pay_coin | string | true | none | 支付币种  
» get_coin | string | true | none | 兑换币种  
» pay_amount | string | true | none | 支付金额  
» get_amount | string | true | none | 兑换金额  
» rate | string | true | none | 汇率  
» rate_reci | string | true | none | 汇率倒数  
» promotion_code | string | true | none | 优惠码  
» side | string | true | none | 询价方式  
» order_type | string | true | none | 订单类型 FIAT 法币 /STABLE 稳定币  
» quote_token | string | true | none | 下单时需要用到的询价token  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "type": "string",
        "pay_coin": "string",
        "get_coin": "string",
        "pay_amount": "string",
        "get_amount": "string",
        "rate": "string",
        "rate_reci": "string",
        "promotion_code": "string",
        "side": "string",
        "order_type": "string",
        "quote_token": "string"
      }
    }
    
    

##  OtcOrderRequest

_法币下单请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
type | string | true | none | BUY 入金 SELL 出金  
side | string | true | none | 询价 接口返回的参数 side （用户下单校验）  
crypto_currency | string | true | none | 数字货币币种 支持币种从otc web 法币 询价页面查询  
fiat_currency | string | true | none | 法币币种 支持币种从otc web 法币询价页面查询  
crypto_amount | string | true | none | 数字货币数量  
fiat_amount | string | true | none | 法币数量  
promotion_code | string | false | none | 优惠码  
quote_token | string | true | none | 询价接口返回参数  
bank_id | string | true | none | 用户下单使用的银行卡ID 通过获取默认银行卡接口获取  
      
    
    {
      "type": "BUY",
      "side": "FIAT",
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "crypto_amount": "30000",
      "fiat_amount": "30000",
      "promotion_code": "",
      "quote_token": "",
      "bank_id": "2"
    }
    
    

##  OtcStableCoinOrderCreateResponse

_OtcStableCoinOrderCreateResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | none  
message | string | true | none | none  
      
    
    {
      "code": 0,
      "message": "string"
    }