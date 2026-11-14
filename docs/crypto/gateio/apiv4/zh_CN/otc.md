---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/otc
api_type: REST
updated_at: 2026-11-13 20:58:02.567784
---

# OTC

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
» side | body | string | 是 | PAY：输入支付数量（pay_amount 必传）；GET：输入获得数量（get_amount 必传）  
» pay_coin | body | string | 是 | 支付币种，支持币种从 OTC web 询价页查询  
» get_coin | body | string | 是 | 获得币种，支持币种从 OTC web 询价页查询  
» pay_amount | body | string | 否 | 用户支付币种数量  
» get_amount | body | string | 否 | 用户兑换币种数量  
» create_quote_token | body | string | 否 | 创建询价token 0:询价预览 1:创建询价token 用于下单  
» promotion_code | body | string | 否 | 优惠码  
  
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
»» validity_period | string | 报价有效期（秒）  
»» refresh_limit | integer | 报价刷新次数限制  
»» refresh_limit_msg | string | 刷新限制提示文案  
» timestamp | integer | 服务端秒级时间戳  
  
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
        "type": "BUY",
        "pay_coin": "USD",
        "get_coin": "USDT",
        "pay_amount": "30000.00",
        "get_amount": "29891.00",
        "rate": "1.0036",
        "rate_reci": "0.9964",
        "promotion_code": "",
        "side": "PAY",
        "validity_period": "300",
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
» side | body | string | 是 | 询价接口返回的 side（下单校验用）。兼容历史传参 `FIAT`/`CRYPTO` 或 `PAY`/`GET`；新接入请与询价响应保持一致。  
» crypto_currency | body | string | 是 | 数字货币币种 支持币种从otc web 法币 询价页面查询  
» fiat_currency | body | string | 是 | 法币币种 支持币种从otc web 法币询价页面查询  
» crypto_amount | body | string | 是 | 数字货币数量  
» fiat_amount | body | string | 是 | 法币数量  
» promotion_code | body | string | 否 | 优惠码  
» quote_token | body | string | 是 | 询价接口返回参数  
» bank_id | body | string | 是 | 下单使用的银行卡 ID；请从 `GET /otc/bank/list`返回列表中选取，默认卡对应 `is_default=1`  
» receive_type | body | string | 否 | 汇款名义。按用户类型传允许值：  
企业用户：YOU（以您本公司名义汇款）、GATE（以 Gate 名义汇款）、RECIPIENT（以收款人名义汇款）；  
个人用户：GATE（以 Gate 名义汇款）、PERSON（以用户本人汇款）。  
  
####  详细描述

**» receive_type** : 汇款名义。按用户类型传允许值：  
企业用户：YOU（以您本公司名义汇款）、GATE（以 Gate 名义汇款）、RECIPIENT（以收款人名义汇款）；  
个人用户：GATE（以 Gate 名义汇款）、PERSON（以用户本人汇款）。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» receive_type | YOU  
» receive_type | GATE  
» receive_type | RECIPIENT  
» receive_type | PERSON  
  
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
    body='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2","receive_type":"GATE"}'
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
    body_param='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2","receive_type":"GATE"}'
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
      "bank_id": "2",
      "receive_type": "GATE"
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

创建稳定币订单。除 `promotion_code` 外，请求体字段均为必填。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcStableCoinOrderRequest | 是 |   
» pay_coin | body | string | 是 | 用户支付币种 支持币种 从otc web 稳定币询价页面查询  
» get_coin | body | string | 是 | 用户兑换币种 支持币种 从otc web 稳定币询价页面查询  
» pay_amount | body | string | 是 | 用户支付币种数量  
» get_amount | body | string | 是 | 用户兑换币种数量  
» side | body | string | 是 | 询价接口返回的 side（下单校验用）。兼容历史传参 `PAY`/`GET`；新接入请与询价响应保持一致。  
» promotion_code | body | string | 否 | 优惠码（选填）  
» quote_token | body | string | 是 | 询价接口返回参数  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 稳定币订单创建成功 | OtcStableCoinOrderCreateResponse  
  
### 返回格式

状态码 **200**

_OtcStableCoinOrderCreateResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer | 业务码，0 成功  
» message | string | 提示信息  
» timestamp | integer | 服务端秒级时间戳  
  
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
      "message": "success",
      "timestamp": 1752051076
    }
    

##  获取用户银行卡列表🔒 需要认证

GET`/otc/bank/list`

GET `/otc/bank/list`

_获取用户银行卡列表_

获取用户银行卡列表，用于下单时选择银行卡。 **默认卡** ：以列表项字段 `is_default`（1=默认）为准，无需再调用已弃用的「默认银行卡」单独接口。

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
»»»» id | string | 银行卡 ID（下单时使用；与 `bank_id` 同义字段已收敛为 `id`）  
»»»» bank_account_name | string | 银行账户名称  
»»»» bank_name | string | 银行名称  
»»»» bank_country | string | 银行所在国家  
»»»» bank_address | string | 银行地址  
»»»» iban | string | IBAN号码  
»»»» swift | string | SWIFT代码  
»»»» remittance_line_number | string | 汇款路线号  
»»»» agent_bank_name | string | 代理银行名称  
»»»» agent_bank_swift | string | 代理银行SWIFT代码  
»»»» submit_time | string | 提交时间  
»»»» update_time | string | 更新时间  
»»»» status | string | 状态  
»»»» is_default | integer | 是否默认银行卡 1是 0否  
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
    
    url = '/otc/bank/list'
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
    url="/otc/bank/list"
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
      "message": "string",
      "data": {
        "lists": [
          {}
        ]
      },
      "timestamp": 0
    }
    

##  创建银行卡🔒 需要认证

POST`/otc/bank/create`

POST `/otc/bank/create`

_创建银行卡_

绑定银行卡。Global 主体下非同名账户可能进入人工审核（`status` 待审），需后续补充材料。 对应 Inner：`POST /bank/create`。字段与协议以现网表单/网关为准；`bank_account_name` 部分环境为 Base64 编码传递，详见联调说明。

开户证明文件支持两种方式（二选一）：

  1. **预上传（推荐）** ：先调用 `POST /otc/upload/pre_upload`（`scene=bank`）获取临时桶 Policy 并直传 S3，再在本接口传 `documentation_file_key` \+ `file_type`；
  2. **multipart 直传** ：传 `documentation_file` 文件字段，服务端直接写入正式桶。

使用预上传时，服务端会校验对象存在性与 `file_key` 路径中的 uid 是否为调用方，校验通过后搬迁至正式桶再落库。跨用户引用返回 `Invalid parameters file_key`，未完成直传返回 `Invalid parameters file not uploaded`。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcBankCreateMultipartRequest | 是 |   
» bank_account_name | body | string | 是 |   
» bank_name | body | string | 是 |   
» bank_country | body | string | 是 |   
» bank_address | body | string | 是 |   
» iban | body | string | 是 |   
» swift | body | string | 是 |   
» remittance_line_number | body | string | 否 |   
» agent_bank_name | body | string | 否 |   
» agent_bank_swift | body | string | 否 |   
» documentation_file | body | string | 否 | multipart 直传方式；与 documentation_file_key 二选一  
» documentation_file_key | body | string | 否 | 预上传方式；pre_upload 返回的 file_key（明文或 base64 均可识别）  
» file_type | body | string | 否 | 使用 documentation_file_key 时必填；明文 MIME 或其 base64  
» _None_ | body | object | 否 |   
» _None_ | body | object | 否 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 受理成功 | OtcBankCreateResponse  
  
### 返回格式

状态码 **200**

_创建银行卡成功（Inner 返回 bank_id、status）_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» data | object |   
»» bank_id | integer | otc_rds 银行卡主键  
»» status | integer | 审核状态（如待审）  
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
    
    url = '/otc/bank/create'
    query_param = ''
    body='{}'
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
    url="/otc/bank/create"
    query_param=""
    body_param='{}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {}
    
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "bank_id": 0,
        "status": 0
      },
      "timestamp": 0
    }
    

##  删除银行卡🔒 需要认证

POST`/otc/bank/delete`

POST `/otc/bank/delete`

_删除银行卡_

删除指定银行卡。对应 Inner：`POST /bank/delete`。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcBankIdRequest | 是 |   
» bank_id | body | string | 是 | 银行卡 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 删除成功 | OtcActionResponse  
  
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
    
    url = '/otc/bank/delete'
    query_param = ''
    body='{"bank_id":"string"}'
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
    url="/otc/bank/delete"
    query_param=""
    body_param='{"bank_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "bank_id": "string"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  设置默认银行卡🔒 需要认证

POST`/otc/bank/set_default`

POST `/otc/bank/set_default`

_设置默认银行卡_

将指定银行卡设为默认。对应 Inner：`POST /bank/set_default`。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcBankIdRequest | 是 |   
» bank_id | body | string | 是 | 银行卡 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 设置成功 | OtcActionResponse  
  
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
    
    url = '/otc/bank/set_default'
    query_param = ''
    body='{"bank_id":"string"}'
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
    url="/otc/bank/set_default"
    query_param=""
    body_param='{"bank_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "bank_id": "string"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  查询银行卡待补充资料清单🔒 需要认证

GET`/otc/bank/bank_supplement_checklist`

GET `/otc/bank/bank_supplement_checklist`

_查询银行卡待补充资料清单_

**①** 须指定 `bank_id`：校验卡归属当前用户且状态允许补充后，按该用户**已通过的专业认证类型** （个人/企业）返回待补充资料项；每项以 `description` 描述提交补件要求。 对应 Inner：`GET /bank/bank_supplement_checklist`。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
bank_id | 请求参数 | string | 是 | 银行卡 ID（otc_rds / 列表返回的 id）  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OtcBankSupplementChecklistResponse  
  
### 返回格式

状态码 **200**

_OtcBankSupplementChecklistResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer |   
» message | string |   
» data | object |   
»» user_type | string | personal 或 enterprise，与提交补件类型一致；`items[].description` 为各资料项提交补件描述  
»» items | array | [待补充资料项]  
»»» _None_ | OtcBankSupplementChecklistItem | 待补充资料项  
»»»» description | string | 提交补件描述  
»»» timestamp | integer |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
user_type | personal  
user_type | enterprise  
  
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
    
    url = '/otc/bank/bank_supplement_checklist'
    query_param = 'bank_id=string'
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
    url="/otc/bank/bank_supplement_checklist"
    query_param="bank_id=string"
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
        "user_type": "personal",
        "items": [
          {}
        ]
      },
      "timestamp": 0
    }
    

##  提交银行卡补充材料（个人）🔒 需要认证

POST`/otc/bank/personal/bank_supplement`

POST `/otc/bank/personal/bank_supplement`

_提交银行卡补充材料（个人）_

**个人专业认证（type=1）** 用户提交非同人/补件材料。须与 `GET /otc/bank/bank_supplement_checklist?bank_id=` 返回的 `user_type=personal` 一致，否则拒绝。

两种提交方式（可混用）：

  1. **预上传（推荐）** ：先调用 `POST /otc/upload/pre_upload`（`scene=bank`）直传临时桶，再在 `relationship_proof` JSON 中按分类填写文件项；**`key` 传明文** object path（`base64_decode(pre_upload.file_key)`，形如 `otc_temp/{uid}/bank/xxx.png`），`file_type` 传明文 MIME；服务端落库前会统一 base64 编码，勿直接传 base64 的 `file_key`；
  2. **multipart 直传** ：每个资料项单独文件字段，字段名与清单 `code` 一致（`id_document_front`、`id_document_back`、`address_proof`）。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcBankPersonalSupplementMultipartRequest | 是 |   
» bank_id | body | string | 是 |   
» id_document_front | body | string | 否 | 身份证明正面文件内容（multipart 文件字段，二进制/Base64）  
» id_document_back | body | string | 否 | 身份证明背面文件内容（multipart 文件字段，二进制/Base64）  
» address_proof | body | string | 否 | 地址证明文件内容（multipart 文件字段，二进制/Base64）  
» relationship_proof | body | string | 否 | 可选，relationship_proof 的 JSON 字符串  
» _None_ | body | object | 否 |   
» _None_ | body | object | 否 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 受理成功 | OtcActionResponse  
  
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
    
    url = '/otc/bank/personal/bank_supplement'
    query_param = ''
    body='{}'
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
    url="/otc/bank/personal/bank_supplement"
    query_param=""
    body_param='{}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {}
    
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  提交银行卡补充材料（企业）🔒 需要认证

POST`/otc/bank/enterprise/bank_supplement`

POST `/otc/bank/enterprise/bank_supplement`

_提交银行卡补充材料（企业）_

**企业专业认证（type=2）** 用户提交补件材料。须与 checklist 返回的 `user_type=enterprise` 一致。

两种提交方式（可混用）：

  1. **预上传（推荐）** ：先调用 `POST /otc/upload/pre_upload`（`scene=bank`），在 `relationship_proof` 中按分类填文件项；**`key` 传明文** object path（`base64_decode(pre_upload.file_key)`），`file_type` 传明文 MIME；
  2. **multipart 直传** ：文件字段名 `certificate`、`share_holders`、`passport`、`share_holding_structure`；可选 `funds_statement`、`additional`。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcBankEnterpriseSupplementMultipartRequest | 是 |   
» uid | body | string | 否 |   
» bank_id | body | string | 是 |   
» certificate | body | string | 否 | 营业执照/注册证书文件内容（multipart 文件字段，二进制/Base64）  
» share_holders | body | string | 否 | 股东名册文件内容（multipart 文件字段，二进制/Base64）  
» passport | body | string | 否 | 法人/股东护照文件内容（multipart 文件字段，二进制/Base64）  
» share_holding_structure | body | string | 否 | 股权结构图文件内容（multipart 文件字段，二进制/Base64）  
» funds_statement | body | string | 否 | 资金证明文件内容（multipart 文件字段，二进制/Base64，可选）  
» additional | body | string | 否 | 其他补充材料文件内容（multipart 文件字段，二进制/Base64，可选）  
» relationship_proof | body | string | 否 | 可选，relationship_proof 的 JSON 字符串  
» _None_ | body | object | 否 |   
» _None_ | body | object | 否 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 受理成功 | OtcActionResponse  
  
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
    
    url = '/otc/bank/enterprise/bank_supplement'
    query_param = ''
    body='{}'
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
    url="/otc/bank/enterprise/bank_supplement"
    query_param=""
    body_param='{}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {}
    
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  文件预上传（临时桶）🔒 需要认证

POST`/otc/upload/pre_upload`

POST `/otc/upload/pre_upload`

_文件预上传（临时桶）_

客户端选定文件后先调用本接口，获取临时桶 POST Policy 与 `file_key`；再按返回的 `url`、`fields` 直传 S3（成功 HTTP 204）；最后在业务提交接口（如 `POST /otc/order/paid`、`POST /otc/bank/create`）携带**同一 base64`file_key` 原值**（不要解码），服务端校验归属与对象存在后搬迁至正式桶并落库。未提交的文件留在临时桶，由生命周期规则回收。

对应 Inner：`POST /upload/pre_upload`。

**`content_type` 须 base64 传输**（明文含 `/` 可能被网关拦截）。仅支持以下 MIME：

MIME | base64 | 后缀  
---|---|---  
image/png | aW1hZ2UvcG5n | .png  
image/jpeg | aW1hZ2UvanBlZw== | .jpeg  
image/jpg | aW1hZ2UvanBn | .jpg  
application/pdf | YXBwbGljYXRpb24vcGRm | .pdf  
  
**`scene` 与下游接口对应关系**：

scene | 典型用途  
---|---  
general | 法币买单付款凭证（`POST /otc/order/paid` 的 `payment_receipt_file_key`）  
bank | 加卡、银行卡补件  
assessment | 专业认证材料  
credit | 提额申请材料  
  
**凭证有效期** ：响应 `expires_in` 为 **5400 秒（90 分钟）** ；`fields.Policy` 内 `expiration` 与之对应。须在有效期内完成 S3 直传，过期后需重新调用本接口获取新凭证。

**文件大小** ：S3 POST Policy 通过 `content-length-range` 限制单文件 **1 字节 ~ 10MB** （10485760 字节）。超出上限直传将被 S3 拒绝；所有 `scene` 共用此限制。

**直传 S3** ：`url` 为上传地址；`fields` 中每个键值对作为 form-data 字段原样发送，`file` 字段必须放在最后。对象路径由服务端生成为 `otc_temp/{uid}/{scene}/{唯一文件名}`，uid 取自登录态。

本接口错误：`content type is required.`（缺 `content_type`）。`file_key` 的归属与对象存在性由后续业务提交接口校验。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcUploadPreUploadRequest | 是 |   
» content_type | body | string | 是 | 文件 MIME 类型的 **base64** ，必填。仅支持 image/png、image/jpeg、image/jpg、application/pdf。  
» scene | body | string | 否 | 业务场景，选填，默认 general；决定临时路径与搬迁后的正式目录  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» content_type | aW1hZ2UvcG5n  
» content_type | aW1hZ2UvanBlZw==  
» content_type | aW1hZ2UvanBn  
» content_type | YXBwbGljYXRpb24vcGRm  
» scene | general  
» scene | bank  
» scene | assessment  
» scene | credit  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 预上传凭证签发成功 | OtcUploadPreUploadResponse  
  
### 返回格式

状态码 **200**

_OtcUploadPreUploadResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer | 0 成功；10010400 参数错误  
» message | string | 响应消息  
» data | OtcUploadPreUploadData | 预上传凭证与 S3 直传参数  
»» file_key | string | 临时 object 路径的 base64；业务提交时**原样回传** ，不要解码  
»» url | string | S3 直传地址  
»» fields | OtcUploadPreUploadPolicyFields | S3 POST Policy 签名字段，直传时作为 form-data 原样发送  
»»» key | string | 临时 object 明文路径，与 base64_decode(file_key) 一致  
»»» Content-Type | string | 须与预上传请求的 content_type 解码后一致  
»»» X-Amz-Credential | string | AWS 临时凭证与作用域，直传时原样提交  
»»» X-Amz-Algorithm | string | AWS 签名算法，直传时原样提交  
»»» X-Amz-Date | string | AWS 签名时间，直传时原样提交  
»»» Policy | string | base64 编码的 S3 POST Policy，直传时原样提交  
»»» X-Amz-Signature | string | S3 POST Policy 签名，直传时原样提交  
»» expires_in | integer | Policy 有效期（秒），当前为 5400（90 分钟）；与 `fields.Policy` 内 `expiration` 对齐，过期后须重新调用本接口  
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
    
    url = '/otc/upload/pre_upload'
    query_param = ''
    body='{"content_type":"aW1hZ2UvcG5n","scene":"bank"}'
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
    url="/otc/upload/pre_upload"
    query_param=""
    body_param='{"content_type":"aW1hZ2UvcG5n","scene":"bank"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "content_type": "aW1hZ2UvcG5n",
      "scene": "bank"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "file_key": "b3RjX3RlbXAvMTIzNDU2Nzg5MC9iYW5rLzIwMjYwODMxMDc1MTI1MjgyMjMzOTQ1OS5wbmc=",
        "url": "https://example-bucket.s3.us-east-2.amazonaws.com",
        "fields": {
          "key": "otc_temp/1234567890/bank/202608310751252822339459.png",
          "Content-Type": "image/png",
          "X-Amz-Credential": "AKIAEXAMPLE/20260831/us-east-2/s3/aws4_request",
          "X-Amz-Algorithm": "AWS4-HMAC-SHA256",
          "X-Amz-Date": "20260831T075125Z",
          "Policy": "eyJleHBpcmF0aW9uIjoiMjAyNi0wOC0zMVQwOToyMToyNVoiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMSwxMDQ4NTc2MF1dfQ==",
          "X-Amz-Signature": "EXAMPLE_SIGNATURE"
        },
        "expires_in": 5400
      },
      "timestamp": 1788162685
    }
    

##  法币订单设置已付款（入金确认）🔒 需要认证

POST`/otc/order/paid`

POST `/otc/order/paid`

_法币订单设置已付款（入金确认）_

标记法币买单为已付款（入金确认）。**须上传用户付款回执** ：`payment_receipt_file_key` 必填；文件格式 jpg / jpeg / png / pdf，单文件不超过 10MB（服务端与网关协同校验）。 兼容字段名 `payment_receipt` 以网关/现网为准。持久化字段见 `otc_trade_record.payment_receipt_file_key`。 Pay Inner 路径为 `POST .../pay/order_set_paid`（常以 `client_order_id` 关联订单）；本 OpenAPI 路径对应 Inner `POST /order/paid` 仍以 `order_id` 为主——若网关统一为商户订单号，以网关文档为准。

**推荐预上传流程** ：先 `POST /otc/upload/pre_upload`（`scene=general`）直传临时桶，再在本接口传返回的 **base64`file_key` 原值**（不要解码）；服务端校验 uid 与对象存在后搬迁至正式桶。跨用户 key 返回 `Invalid parameters file_key`，未直传返回 `Invalid parameters file not uploaded`。仍兼容旧链路直传正式桶的 base64 key。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OtcMarkOrderPaidRequest | 是 |   
» order_id | body | string | 是 | 订单 ID  
» client_order_id | body | string | 否 | 客户端订单号（部分网关/Inner Pay 路径使用，可选）  
» payment_receipt_file_key | body | string | 是 | 用户付款回执：**必填** 。推荐先 `POST /otc/upload/pre_upload`（`scene=general`）直传临时桶，再传返回的 **base64 file_key 原值** （不要解码）；服务端搬迁至正式桶后落库。仍兼容旧链路直传正式桶的 base64 key。单文件；jpg/jpeg/png/pdf；≤10MB。  
» payment_receipt | body | string | 否 | 与 `payment_receipt_file_key` 兼容的别名（视网关对外字段名）  
  
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
    body='{"order_id":"203","client_order_id":"","payment_receipt_file_key":"b3RjX3RlbXAvMTIzNDU2Nzg5MC9nZW5lcmFsLzIwMjYwODMxMjEwMDEyMzQ1Njc4LnBuZw==","payment_receipt":""}'
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
    body_param='{"order_id":"203","client_order_id":"","payment_receipt_file_key":"b3RjX3RlbXAvMTIzNDU2Nzg5MC9nZW5lcmFsLzIwMjYwODMxMjEwMDEyMzQ1Njc4LnBuZw==","payment_receipt":""}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "order_id": "203",
      "client_order_id": "",
      "payment_receipt_file_key": "b3RjX3RlbXAvMTIzNDU2Nzg5MC9nZW5lcmFsLzIwMjYwODMxMjEwMDEyMzQ1Njc4LnBuZw==",
      "payment_receipt": ""
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
status | 请求参数 | string | 否 | DONE：完成  
CANCEL：取消  
PROCESSING：进行中  
DISBURSED：已出款  
pn | 请求参数 | string | 否 | 分页第几页  
ps | 请求参数 | string | 否 | 分页每页显示数量  
  
####  详细描述

**status** : DONE：完成  
CANCEL：取消  
PROCESSING：进行中  
DISBURSED：已出款

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
»» lists | array |   
»»» OtcOrderListItem | object |   
»»»» time | string | 当前时间  
»»»» timestamp | integer | 当前时间戳  
»»»» order_id | string | 订单Id  
»»»» trade_no | string | 交易号  
»»»» type | string | BUY 入金 / SELL 出金  
»»»» status | string | 订单状态  
»»»» fiat_currency | string | 法币币种  
»»»» fiat_currency_info | object |   
»»»»» name | string | 名称  
»»»»» icon | string | 图片  
»»»» fiat_amount | string | 法币金额  
»»»» crypto_currency | string | 数字货币币种  
»»»» crypto_currency_info | object |   
»»»»» name | string |   
»»»»» icon | string |   
»»»» crypto_amount | string | 数字货币金额  
»»»» rate | string | 汇率  
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
        "lists": [
          {
            "time": "2025-02-11 07:45:06",
            "timestamp": 1739000013,
            "order_id": "41",
            "trade_no": "20250207043457590939",
            "type": "SELL",
            "status": "PROCESSING",
            "fiat_currency": "USD",
            "fiat_currency_info": {
              "name": "USD",
              "icon": "http://icon.url"
            },
            "fiat_amount": "199600",
            "crypto_currency": "USDT",
            "crypto_currency_info": {
              "name": "USDT",
              "icon": "http://icon.url"
            },
            "crypto_amount": "200000",
            "rate": "0.998000",
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
»» lists | array |   
»»» OtcStableCoinOrderListItem | object |   
»»»» id | integer | 订单ID  
»»»» trade_no | string | 交易流水号  
»»»» pay_coin | string | 支付币种  
»»»» pay_icon | string | 支付币种图标  
»»»» pay_amount | string | 支付金额  
»»»» get_coin | string | 获得币种  
»»»» get_icon | string | 获得币种图标  
»»»» get_amount | string | 获得金额  
»»»» rate | string | 汇率  
»»»» rate_reci | string | 汇率倒数  
»»»» status | string | PROCESSING 进行中/ DONE 完成 / FAILED失败  
»»»» create_timest | integer | 创建时间戳  
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
        "lists": [
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
»» fiat_currency | string | 法币币种  
»» fiat_amount | string | 法币金额  
»» crypto_currency | string | 数字货币币种  
»» crypto_amount | string | 数字货币金额  
»» rate | string | 汇率  
»» bank_account_name | string | 用户付款/收款名称  
»» bank_name | string | 用户付款/收款银行名称  
»» bank_country | string | 用户付款/收款银行所在国家  
»» bank_address | string | 用户付款/收款银行地址  
»» bank_account_number_iban | string | 用户付款/收款银行账户号码/IBAN  
»» swift_code | string | 用户付款/收款银行 SWIFT  
»» intermediate_bank_name | string | 用户付款/收款银行中间行名称  
»» intermediary_bank_swift_code | string | 用户付款/收款银行中间行 SWIFT  
»» gate_bank_account_name | string | Gate 收款名称，仅 BUY 展示  
»» gate_bank_name | string | Gate 收款银行名称，仅 BUY 展示  
»» gate_bank_country | string | Gate 收款银行所在国家，仅 BUY 展示  
»» gate_bank_address | string | Gate 收款银行地址，仅 BUY 展示  
»» gate_bank_account_number_iban | string | Gate 收款银行账户号码/IBAN，仅 BUY 展示  
»» gate_swift_code | string | Gate 收款银行 SWIFT，仅 BUY 展示  
»» gate_intermediary_bank_name | string | Gate 收款银行中间行名称，仅 BUY 展示  
»» gate_intermediary_bank_swift_code | string | Gate 收款银行中间行 SWIFT，仅 BUY 展示  
»» gate_transfer_remark | string | 转账备注（与 gate_reference_code 互斥；入金买单有参考码时为空），仅 BUY 展示  
»» gate_reference_code | string | 汇款时请务必填写参考代码，以确保您的订单及时处理。（与 gate_transfer_remark 互斥）  
»» status | string | 状态  
»» create_time | string | 创建时间  
  
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
        "bank_account_name": "",
        "bank_name": "",
        "bank_country": "",
        "bank_address": "",
        "bank_account_number_iban": "",
        "swift_code": "",
        "intermediate_bank_name": "",
        "intermediary_bank_swift_code": "",
        "gate_bank_account_name": "",
        "gate_bank_name": "",
        "gate_bank_country": "",
        "gate_bank_address": "",
        "gate_bank_account_number_iban": "",
        "gate_swift_code": "",
        "gate_intermediary_bank_name": "",
        "gate_intermediary_bank_swift_code": "",
        "gate_transfer_remark": "",
        "gate_reference_code": "OTIK7M39QF42",
        "status": "PROCESSING",
        "create_time": "2025-03-07 07:51:52"
      },
      "timestamp": 1752051076
    }
    

#  模型

##  OtcUploadPreUploadResponse

_OtcUploadPreUploadResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | 0 成功；10010400 参数错误  
message | string | true | none | 响应消息  
data | OtcUploadPreUploadData | true | none | 预上传凭证与 S3 直传参数  
timestamp | integer | true | none | 响应时间戳（秒）  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "file_key": "string",
        "url": "string",
        "fields": {
          "key": "string",
          "Content-Type": "string",
          "X-Amz-Credential": "string",
          "X-Amz-Algorithm": "string",
          "X-Amz-Date": "string",
          "Policy": "string",
          "X-Amz-Signature": "string"
        },
        "expires_in": 0
      },
      "timestamp": 0
    }
    
    

##  OtcQuoteRequest

_法币和稳定币询价请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
side | string | true | none | PAY：输入支付数量（pay_amount 必传）；GET：输入获得数量（get_amount 必传）  
pay_coin | string | true | none | 支付币种，支持币种从 OTC web 询价页查询  
get_coin | string | true | none | 获得币种，支持币种从 OTC web 询价页查询  
pay_amount | string | false | none | 用户支付币种数量  
get_amount | string | false | none | 用户兑换币种数量  
create_quote_token | string | false | none | 创建询价token 0:询价预览 1:创建询价token 用于下单  
promotion_code | string | false | none | 优惠码  
      
    
    {
      "side": "PAY",
      "pay_coin": "USDT",
      "get_coin": "USD",
      "pay_amount": "30000",
      "get_amount": "30000",
      "create_quote_token": "0",
      "promotion_code": ""
    }
    
    

##  OtcStableCoinOrderCreateResponse

_OtcStableCoinOrderCreateResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | 业务码，0 成功  
message | string | true | none | 提示信息  
timestamp | integer | true | none | 服务端秒级时间戳  
      
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    
    

##  OtcBankEnterpriseSupplementMultipartRequest

_企业补件`multipart/form-data`。文件字段名：`certificate`、`share_holders`、`passport`、`share_holding_structure`；可选 `funds_statement`、`additional`。可选字符串 `relationship_proof`（JSON）合并入参。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
uid | string | false | none | none  
bank_id | string | true | none | none  
certificate | string | false | none | 营业执照/注册证书文件内容（multipart 文件字段，二进制/Base64）  
share_holders | string | false | none | 股东名册文件内容（multipart 文件字段，二进制/Base64）  
passport | string | false | none | 法人/股东护照文件内容（multipart 文件字段，二进制/Base64）  
share_holding_structure | string | false | none | 股权结构图文件内容（multipart 文件字段，二进制/Base64）  
funds_statement | string | false | none | 资金证明文件内容（multipart 文件字段，二进制/Base64，可选）  
additional | string | false | none | 其他补充材料文件内容（multipart 文件字段，二进制/Base64，可选）  
relationship_proof | string | false | none | 可选，relationship_proof 的 JSON 字符串  
  
_anyOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
  
_or_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
      
    
    {}
    
    

##  OtcUploadPreUploadData

_预上传凭证与 S3 直传参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
file_key | string | true | none | 临时 object 路径的 base64；业务提交时**原样回传** ，不要解码  
url | string | true | none | S3 直传地址  
fields | OtcUploadPreUploadPolicyFields | true | none | S3 POST Policy 签名字段，直传时作为 form-data 原样发送  
expires_in | integer | true | none | Policy 有效期（秒），当前为 5400（90 分钟）；与 `fields.Policy` 内 `expiration` 对齐，过期后须重新调用本接口  
      
    
    {
      "file_key": "string",
      "url": "string",
      "fields": {
        "key": "string",
        "Content-Type": "string",
        "X-Amz-Credential": "string",
        "X-Amz-Algorithm": "string",
        "X-Amz-Date": "string",
        "Policy": "string",
        "X-Amz-Signature": "string"
      },
      "expires_in": 0
    }
    
    

##  OtcBankCreateMultipartRequest

*Inner 创建银行卡 `multipart/form-data`。开户证明文件二选一：

  * **预上传** ：`documentation_file_key` \+ `file_type`（先 `POST /otc/upload/pre_upload`，`scene=bank`）；
  * **multipart 直传** ：`documentation_file` 文件字段。*

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
bank_account_name | string | true | none | none  
bank_name | string | true | none | none  
bank_country | string | true | none | none  
bank_address | string | true | none | none  
iban | string | true | none | none  
swift | string | true | none | none  
remittance_line_number | string | false | none | none  
agent_bank_name | string | false | none | none  
agent_bank_swift | string | false | none | none  
documentation_file | string | false | none | multipart 直传方式；与 documentation_file_key 二选一  
documentation_file_key | string | false | none | 预上传方式；pre_upload 返回的 file_key（明文或 base64 均可识别）  
file_type | string | false | none | 使用 documentation_file_key 时必填；明文 MIME 或其 base64  
  
_oneOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
  
_xor_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
      
    
    {}
    
    

##  OtcBankSupplementChecklistResponse

_OtcBankSupplementChecklistResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | none  
message | string | true | none | none  
data | object | true | none | none  
» user_type | string | true | none | personal 或 enterprise，与提交补件类型一致；`items[].description` 为各资料项提交补件描述  
» items | [OtcBankSupplementChecklistItem] | true | none | [待补充资料项]  
timestamp | integer | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
user_type | personal  
user_type | enterprise  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "user_type": "personal",
        "items": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  OtcUploadPreUploadRequest

_文件预上传请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
content_type | string | true | none | 文件 MIME 类型的 **base64** ，必填。仅支持 image/png、image/jpeg、image/jpg、application/pdf。  
scene | string | false | none | 业务场景，选填，默认 general；决定临时路径与搬迁后的正式目录  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
content_type | aW1hZ2UvcG5n  
content_type | aW1hZ2UvanBlZw==  
content_type | aW1hZ2UvanBn  
content_type | YXBwbGljYXRpb24vcGRm  
scene | general  
scene | bank  
scene | assessment  
scene | credit  
      
    
    {
      "content_type": "aW1hZ2UvcG5n",
      "scene": "bank"
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
» lists | array | true | none | none  
»» OtcStableCoinOrderListItem | object | false | none | none  
»»» id | integer | false | none | 订单ID  
»»» trade_no | string | false | none | 交易流水号  
»»» pay_coin | string | false | none | 支付币种  
»»» pay_icon | string | false | none | 支付币种图标  
»»» pay_amount | string | false | none | 支付金额  
»»» get_coin | string | false | none | 获得币种  
»»» get_icon | string | false | none | 获得币种图标  
»»» get_amount | string | false | none | 获得金额  
»»» rate | string | false | none | 汇率  
»»» rate_reci | string | false | none | 汇率倒数  
»»» status | string | false | none | PROCESSING 进行中/ DONE 完成 / FAILED失败  
»»» create_timest | integer | false | none | 创建时间戳  
»»» create_time | string | false | none | 创建时间  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "total": 0,
        "page_size": 0,
        "page_number": 0,
        "total_page": 0,
        "lists": [
          {}
        ]
      }
    }
    
    

##  OtcBankIdRequest

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
bank_id | string | true | none | 银行卡 ID  
      
    
    {
      "bank_id": "string"
    }
    
    

##  OtcBankPersonalSupplementMultipartRequest

_个人补件`multipart/form-data`。文件字段名固定为 `id_document_front`、`id_document_back`、`address_proof`（与 checklist `code` 一致）；可额外传字符串字段 `relationship_proof`（JSON 文本）与上传结果合并。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
bank_id | string | true | none | none  
id_document_front | string | false | none | 身份证明正面文件内容（multipart 文件字段，二进制/Base64）  
id_document_back | string | false | none | 身份证明背面文件内容（multipart 文件字段，二进制/Base64）  
address_proof | string | false | none | 地址证明文件内容（multipart 文件字段，二进制/Base64）  
relationship_proof | string | false | none | 可选，relationship_proof 的 JSON 字符串  
  
_anyOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
  
_or_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
      
    
    {}
    
    

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
» lists | array | true | none | none  
»» OtcOrderListItem | object | false | none | none  
»»» time | string | false | none | 当前时间  
»»» timestamp | integer | false | none | 当前时间戳  
»»» order_id | string | false | none | 订单Id  
»»» trade_no | string | false | none | 交易号  
»»» type | string | false | none | BUY 入金 / SELL 出金  
»»» status | string | false | none | 订单状态  
»»» fiat_currency | string | false | none | 法币币种  
»»» fiat_currency_info | object | false | none | none  
»»»» name | string | true | none | 名称  
»»»» icon | string | true | none | 图片  
»»» fiat_amount | string | false | none | 法币金额  
»»» crypto_currency | string | false | none | 数字货币币种  
»»» crypto_currency_info | object | false | none | none  
»»»» name | string | true | none | none  
»»»» icon | string | true | none | none  
»»» crypto_amount | string | false | none | 数字货币金额  
»»» rate | string | false | none | 汇率  
»»» promotion_code | string | false | none | 优惠码  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "pn": 0,
        "ps": 0,
        "total_pn": 0,
        "count": 0,
        "lists": [
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
» validity_period | string | false | none | 报价有效期（秒）  
» refresh_limit | integer | false | none | 报价刷新次数限制  
» refresh_limit_msg | string | false | none | 刷新限制提示文案  
timestamp | integer | true | none | 服务端秒级时间戳  
      
    
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
        "quote_token": "string",
        "validity_period": "string",
        "refresh_limit": 0,
        "refresh_limit_msg": "string"
      },
      "timestamp": 0
    }
    
    

##  OtcStableCoinOrderRequest

_稳定币下单请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
pay_coin | string | true | none | 用户支付币种 支持币种 从otc web 稳定币询价页面查询  
get_coin | string | true | none | 用户兑换币种 支持币种 从otc web 稳定币询价页面查询  
pay_amount | string | true | none | 用户支付币种数量  
get_amount | string | true | none | 用户兑换币种数量  
side | string | true | none | 询价接口返回的 side（下单校验用）。兼容历史传参 `PAY`/`GET`；新接入请与询价响应保持一致。  
promotion_code | string | false | none | 优惠码（选填）  
quote_token | string | true | none | 询价接口返回参数  
      
    
    {
      "pay_coin": "USDC",
      "get_coin": "USDT",
      "pay_amount": "30000",
      "get_amount": "20000",
      "side": "PAY",
      "promotion_code": "",
      "quote_token": "dsafjkdshfjdsjkfah"
    }
    
    

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
» fiat_currency | string | true | none | 法币币种  
» fiat_amount | string | true | none | 法币金额  
» crypto_currency | string | true | none | 数字货币币种  
» crypto_amount | string | true | none | 数字货币金额  
» rate | string | true | none | 汇率  
» bank_account_name | string | false | none | 用户付款/收款名称  
» bank_name | string | false | none | 用户付款/收款银行名称  
» bank_country | string | false | none | 用户付款/收款银行所在国家  
» bank_address | string | false | none | 用户付款/收款银行地址  
» bank_account_number_iban | string | false | none | 用户付款/收款银行账户号码/IBAN  
» swift_code | string | false | none | 用户付款/收款银行 SWIFT  
» intermediate_bank_name | string | false | none | 用户付款/收款银行中间行名称  
» intermediary_bank_swift_code | string | false | none | 用户付款/收款银行中间行 SWIFT  
» gate_bank_account_name | string | false | none | Gate 收款名称，仅 BUY 展示  
» gate_bank_name | string | false | none | Gate 收款银行名称，仅 BUY 展示  
» gate_bank_country | string | false | none | Gate 收款银行所在国家，仅 BUY 展示  
» gate_bank_address | string | false | none | Gate 收款银行地址，仅 BUY 展示  
» gate_bank_account_number_iban | string | false | none | Gate 收款银行账户号码/IBAN，仅 BUY 展示  
» gate_swift_code | string | false | none | Gate 收款银行 SWIFT，仅 BUY 展示  
» gate_intermediary_bank_name | string | false | none | Gate 收款银行中间行名称，仅 BUY 展示  
» gate_intermediary_bank_swift_code | string | false | none | Gate 收款银行中间行 SWIFT，仅 BUY 展示  
» gate_transfer_remark | string | false | none | 转账备注（与 gate_reference_code 互斥；入金买单有参考码时为空），仅 BUY 展示  
» gate_reference_code | string | false | none | 汇款时请务必填写参考代码，以确保您的订单及时处理。（与 gate_transfer_remark 互斥）  
» status | string | true | none | 状态  
» create_time | string | true | none | 创建时间  
      
    
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
        "bank_account_name": "string",
        "bank_name": "string",
        "bank_country": "string",
        "bank_address": "string",
        "bank_account_number_iban": "string",
        "swift_code": "string",
        "intermediate_bank_name": "string",
        "intermediary_bank_swift_code": "string",
        "gate_bank_account_name": "string",
        "gate_bank_name": "string",
        "gate_bank_country": "string",
        "gate_bank_address": "string",
        "gate_bank_account_number_iban": "string",
        "gate_swift_code": "string",
        "gate_intermediary_bank_name": "string",
        "gate_intermediary_bank_swift_code": "string",
        "gate_transfer_remark": "string",
        "gate_reference_code": "string",
        "status": "string",
        "create_time": "string"
      }
    }
    
    

##  OtcBankSupplementChecklistItem

_待补充资料项_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
description | string | true | none | 提交补件描述  
      
    
    {
      "description": "string"
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
»»» id | string | true | none | 银行卡 ID（下单时使用；与 `bank_id` 同义字段已收敛为 `id`）  
»»» bank_account_name | string | true | none | 银行账户名称  
»»» bank_name | string | true | none | 银行名称  
»»» bank_country | string | false | none | 银行所在国家  
»»» bank_address | string | false | none | 银行地址  
»»» iban | string | false | none | IBAN号码  
»»» swift | string | false | none | SWIFT代码  
»»» remittance_line_number | string | false | none | 汇款路线号  
»»» agent_bank_name | string | false | none | 代理银行名称  
»»» agent_bank_swift | string | false | none | 代理银行SWIFT代码  
»»» submit_time | string | false | none | 提交时间  
»»» update_time | string | false | none | 更新时间  
»»» status | string | false | none | 状态  
»»» is_default | integer | false | none | 是否默认银行卡 1是 0否  
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
    
    

##  OtcOrderRequest

_法币下单请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
type | string | true | none | BUY 入金 SELL 出金  
side | string | true | none | 询价接口返回的 side（下单校验用）。兼容历史传参 `FIAT`/`CRYPTO` 或 `PAY`/`GET`；新接入请与询价响应保持一致。  
crypto_currency | string | true | none | 数字货币币种 支持币种从otc web 法币 询价页面查询  
fiat_currency | string | true | none | 法币币种 支持币种从otc web 法币询价页面查询  
crypto_amount | string | true | none | 数字货币数量  
fiat_amount | string | true | none | 法币数量  
promotion_code | string | false | none | 优惠码  
quote_token | string | true | none | 询价接口返回参数  
bank_id | string | true | none | 下单使用的银行卡 ID；请从 `GET /otc/bank/list`返回列表中选取，默认卡对应 `is_default=1`  
receive_type | string | false | none | 汇款名义。按用户类型传允许值：  
企业用户：YOU（以您本公司名义汇款）、GATE（以 Gate 名义汇款）、RECIPIENT（以收款人名义汇款）；  
个人用户：GATE（以 Gate 名义汇款）、PERSON（以用户本人汇款）。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
receive_type | YOU  
receive_type | GATE  
receive_type | RECIPIENT  
receive_type | PERSON  
      
    
    {
      "type": "BUY",
      "side": "FIAT",
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "crypto_amount": "30000",
      "fiat_amount": "30000",
      "promotion_code": "",
      "quote_token": "",
      "bank_id": "2",
      "receive_type": "GATE"
    }
    
    

##  OtcBankCreateResponse

_创建银行卡成功（Inner 返回 bank_id、status）_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | none  
message | string | true | none | none  
data | object | true | none | none  
» bank_id | integer | true | none | otc_rds 银行卡主键  
» status | integer | true | none | 审核状态（如待审）  
timestamp | integer | false | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "bank_id": 0,
        "status": 0
      },
      "timestamp": 0
    }
    
    

##  OtcMarkOrderPaidRequest

_法币订单设置已付款（入金确认）请求体。须包含用户付款回执（与 §3.2 一致）。**`payment_receipt_file_key` 必填**；订单主键在此路径为 `order_id`。经 Pay 网关访问时若使用 `client_order_id`，以网关转写字段为准。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | true | none | 订单 ID  
client_order_id | string | false | none | 客户端订单号（部分网关/Inner Pay 路径使用，可选）  
payment_receipt_file_key | string | true | none | 用户付款回执：**必填** 。推荐先 `POST /otc/upload/pre_upload`（`scene=general`）直传临时桶，再传返回的 **base64 file_key 原值** （不要解码）；服务端搬迁至正式桶后落库。仍兼容旧链路直传正式桶的 base64 key。单文件；jpg/jpeg/png/pdf；≤10MB。  
payment_receipt | string | false | none | 与 `payment_receipt_file_key` 兼容的别名（视网关对外字段名）  
      
    
    {
      "order_id": "203",
      "client_order_id": "",
      "payment_receipt_file_key": "b3RjX3RlbXAvMTIzNDU2Nzg5MC9nZW5lcmFsLzIwMjYwODMxMjEwMDEyMzQ1Njc4LnBuZw==",
      "payment_receipt": ""
    }
    
    

##  OtcUploadPreUploadPolicyFields

_S3 POST Policy 签名字段，直传时作为 form-data 原样发送_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
key | string | true | none | 临时 object 明文路径，与 base64_decode(file_key) 一致  
Content-Type | string | true | none | 须与预上传请求的 content_type 解码后一致  
X-Amz-Credential | string | true | none | AWS 临时凭证与作用域，直传时原样提交  
X-Amz-Algorithm | string | true | none | AWS 签名算法，直传时原样提交  
X-Amz-Date | string | true | none | AWS 签名时间，直传时原样提交  
Policy | string | true | none | base64 编码的 S3 POST Policy，直传时原样提交  
X-Amz-Signature | string | true | none | S3 POST Policy 签名，直传时原样提交  
      
    
    {
      "key": "string",
      "Content-Type": "string",
      "X-Amz-Credential": "string",
      "X-Amz-Algorithm": "string",
      "X-Amz-Date": "string",
      "Policy": "string",
      "X-Amz-Signature": "string"
    }