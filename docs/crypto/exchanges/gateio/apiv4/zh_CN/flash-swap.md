---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/flash-swap
api_type: REST
updated_at: 2026-05-27 20:17:11.972342
---

# Flash_swap

闪兑

##  查询支持闪兑的所有交易对列表

GET`/flash_swap/currency_pairs`

GET `/flash_swap/currency_pairs`

_查询支持闪兑的所有交易对列表_

`BTC_GT`表示卖出`BTC`买入`GT` ， 每个币种在每个交易对中的限额不同，两个能闪兑的币种不一定能相互兑换 ， 比如可能存在 卖出`BTC`买入`GT` ， 不一定可以卖出`GT`BTC`, 即支持`BTC_GT`不一定支持`GT_BTC`

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为1000，最小1，最大1000。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [FlashSwapCurrencyPair]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [查询闪兑的交易对列表]  
» _None_ | FlashSwapCurrencyPair | 查询闪兑的交易对列表  
»» currency_pair | string | 交易对 ， `BTC_USDT` 表示卖`BTC`买`USDT`  
»» sell_currency | string | 卖出币种  
»» buy_currency | string | 买入币种  
»» sell_min_amount | string | 卖出最小数量  
»» sell_max_amount | string | 卖出最大数量  
»» buy_min_amount | string | 买入最小数量  
»» buy_max_amount | string | 买入最大数量  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/flash_swap/currency_pairs'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/flash_swap/currency_pairs \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency_pair": "BTC_USDT",
        "sell_currency": "BTC",
        "buy_currency": "USDT",
        "sell_min_amount": "0.00001",
        "sell_max_amount": "100",
        "buy_min_amount": "10",
        "buy_max_amount": "10000000"
      }
    ]
    

##  闪兑订单列表查询🔒 需要认证

GET`/flash_swap/orders`

GET `/flash_swap/orders`

_闪兑订单列表查询_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
status | 请求参数 | integer | 否 | 闪兑订单状态  
\- `1`: 成功  
\- `2`: 失败  
sell_currency | 请求参数 | string | 否 | 卖出的资产名称  
\- 根据接口`查询支持闪兑的货币列表 GET /flash_swap/currencies`获取  
buy_currency | 请求参数 | string | 否 | 买入的资产名称  
\- 根据接口`查询支持闪兑的货币列表 GET /flash_swap/currencies`获取  
reverse | 请求参数 | boolean | 否 | 根据id正序或反向排列，默认`true`  
\- `true` ： id反序（最近时间的数据）  
\- `false` ： id正序（最远时间的数据）  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
page | 请求参数 | integer(int32) | 否 | 列表页数  
  
####  详细描述

**status** : 闪兑订单状态  
\- `1`: 成功  
\- `2`: 失败

**sell_currency** : 卖出的资产名称  
\- 根据接口`查询支持闪兑的货币列表 GET /flash_swap/currencies`获取

**buy_currency** : 买入的资产名称  
\- 根据接口`查询支持闪兑的货币列表 GET /flash_swap/currencies`获取

**reverse** : 根据id正序或反向排列，默认`true`  
\- `true` ： id反序（最近时间的数据）  
\- `false` ： id正序（最远时间的数据）

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FlashSwapOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [闪兑订单]  
» _None_ | FlashSwapOrder | 闪兑订单  
»» id | integer(int64) | 闪兑订单id  
»» create_time | integer(int64) | 订单创建时间，毫秒精度  
»» user_id | integer(int64) | 用户id  
»» sell_currency | string | 卖出的资产名称  
»» sell_amount | string | 卖出的资产数量  
»» buy_currency | string | 买入的资产名称  
»» buy_amount | string | 买入的资产数量  
»» price | string | 价格  
»» status | integer | 闪兑订单状态  
  
\- `1`: 成功  
\- `2`: 失败  
  
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
    
    url = '/flash_swap/orders'
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
    url="/flash_swap/orders"
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
        "id": 54646,
        "create_time": 1651116876378,
        "update_time": 1651116876378,
        "user_id": 11135567,
        "sell_currency": "BTC",
        "sell_amount": "0.01",
        "buy_currency": "USDT",
        "buy_amount": "10",
        "price": "100",
        "status": 1
      }
    ]
    

##  创建闪兑订单🔒 需要认证

POST`/flash_swap/orders`

POST `/flash_swap/orders`

_创建闪兑订单_

需要先进行闪兑预览，创建闪兑订单时需要传入预览结果

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | FlashSwapOrderRequest | 是 |   
» preview_id | body | string | 是 | 预览结果id  
» sell_currency | body | string | 是 | 卖出的资产名称，根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取  
» sell_amount | body | string | 是 | 卖出的资产数量(根据预览结果)  
» buy_currency | body | string | 是 | 买入的资产名称，根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取  
» buy_amount | body | string | 是 | 买入的资产数量(根据预览结果)  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 创建闪兑订单成功 | FlashSwapOrder  
  
### 返回格式

状态码 **201**

_闪兑订单_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 闪兑订单id  
» create_time | integer(int64) | 订单创建时间，毫秒精度  
» user_id | integer(int64) | 用户id  
» sell_currency | string | 卖出的资产名称  
» sell_amount | string | 卖出的资产数量  
» buy_currency | string | 买入的资产名称  
» buy_amount | string | 买入的资产数量  
» price | string | 价格  
» status | integer | 闪兑订单状态  
  
\- `1`: 成功  
\- `2`: 失败  
  
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
    
    url = '/flash_swap/orders'
    query_param = ''
    body='{"preview_id":"4564564","sell_currency":"BTC","sell_amount":"0.1","buy_currency":"USDT","buy_amount":"10"}'
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
    url="/flash_swap/orders"
    query_param=""
    body_param='{"preview_id":"4564564","sell_currency":"BTC","sell_amount":"0.1","buy_currency":"USDT","buy_amount":"10"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "preview_id": "4564564",
      "sell_currency": "BTC",
      "sell_amount": "0.1",
      "buy_currency": "USDT",
      "buy_amount": "10"
    }
    

> 返回示例

> 201 返回
    
    
    {
      "id": 54646,
      "create_time": 1651116876378,
      "update_time": 1651116876378,
      "user_id": 11135567,
      "sell_currency": "BTC",
      "sell_amount": "0.01",
      "buy_currency": "USDT",
      "buy_amount": "10",
      "price": "100",
      "status": 1
    }
    

##  查询单张闪兑订单🔒 需要认证

GET`/flash_swap/orders/{order_id}`

GET `/flash_swap/orders/{order_id}`

_查询单张闪兑订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | integer | 是 | 闪兑订单id  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | FlashSwapOrder  
  
### 返回格式

状态码 **200**

_闪兑订单_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 闪兑订单id  
» create_time | integer(int64) | 订单创建时间，毫秒精度  
» user_id | integer(int64) | 用户id  
» sell_currency | string | 卖出的资产名称  
» sell_amount | string | 卖出的资产数量  
» buy_currency | string | 买入的资产名称  
» buy_amount | string | 买入的资产数量  
» price | string | 价格  
» status | integer | 闪兑订单状态  
  
\- `1`: 成功  
\- `2`: 失败  
  
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
    
    url = '/flash_swap/orders/1'
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
    url="/flash_swap/orders/1"
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
      "id": 54646,
      "create_time": 1651116876378,
      "update_time": 1651116876378,
      "user_id": 11135567,
      "sell_currency": "BTC",
      "sell_amount": "0.01",
      "buy_currency": "USDT",
      "buy_amount": "10",
      "price": "100",
      "status": 1
    }
    

##  闪兑订单预览🔒 需要认证

POST`/flash_swap/orders/preview`

POST `/flash_swap/orders/preview`

_闪兑订单预览_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | FlashSwapPreviewRequest | 是 |   
» sell_currency | body | string | 是 | 卖出的资产名称，  
根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取  
» sell_amount | body | string | 否 | 卖出的资产数量，  
`sell_amount`和`buy_amount`二选一必填  
» buy_currency | body | string | 是 | 买入的资产名称，  
根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取  
» buy_amount | body | string | 否 | 买入的资产数量，  
`sell_amount`和`buy_amount`二选一必填  
  
####  详细描述

**» sell_currency** : 卖出的资产名称，  
根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取

**» sell_amount** : 卖出的资产数量，  
`sell_amount`和`buy_amount`二选一必填

**» buy_currency** : 买入的资产名称，  
根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取

**» buy_amount** : 买入的资产数量，  
`sell_amount`和`buy_amount`二选一必填

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 闪兑订单预览成功 | FlashSwapOrderPreview  
  
### 返回格式

状态码 **200**

_闪兑订单预览_

名称 | 类型 | 描述  
---|---|---  
» preview_id | string | 预览结果id  
» sell_currency | string | 卖出的资产名称，  
根据接口`查询支持闪兑的货币列表 GET /flash_swap/currencies`获取  
» sell_amount | string | 卖出的资产数量  
» buy_currency | string | 买入的资产名称，  
根据接口`查询支持闪兑的货币列表 GET /flash_swap/currencies`获取  
» buy_amount | string | 买入的资产数量  
» price | string | 价格  
  
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
    
    url = '/flash_swap/orders/preview'
    query_param = ''
    body='{"sell_currency":"BTC","sell_amount":"0.1","buy_currency":"USDT"}'
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
    url="/flash_swap/orders/preview"
    query_param=""
    body_param='{"sell_currency":"BTC","sell_amount":"0.1","buy_currency":"USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "sell_currency": "BTC",
      "sell_amount": "0.1",
      "buy_currency": "USDT"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "preview_id": "3453434",
      "sell_currency": "BTC",
      "sell_amount": "0.1",
      "buy_currency": "USDT",
      "buy_amount": "10",
      "price": "100"
    }
    

#  模型

##  FlashSwapPreviewRequest

_创建闪兑订单参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
sell_currency | string | true | none | 卖出的资产名称，  
根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取  
sell_amount | string | false | none | 卖出的资产数量，  
`sell_amount`和`buy_amount`二选一必填  
buy_currency | string | true | none | 买入的资产名称，  
根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取  
buy_amount | string | false | none | 买入的资产数量，  
`sell_amount`和`buy_amount`二选一必填  
      
    
    {
      "sell_currency": "string",
      "sell_amount": "string",
      "buy_currency": "string",
      "buy_amount": "string"
    }
    
    

##  FlashSwapOrderPreview

_闪兑订单预览_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
preview_id | string | false | none | 预览结果id  
sell_currency | string | false | none | 卖出的资产名称，  
根据接口`查询支持闪兑的货币列表 GET /flash_swap/currencies`获取  
sell_amount | string | false | none | 卖出的资产数量  
buy_currency | string | false | none | 买入的资产名称，  
根据接口`查询支持闪兑的货币列表 GET /flash_swap/currencies`获取  
buy_amount | string | false | none | 买入的资产数量  
price | string | false | none | 价格  
      
    
    {
      "preview_id": "string",
      "sell_currency": "string",
      "sell_amount": "string",
      "buy_currency": "string",
      "buy_amount": "string",
      "price": "string"
    }
    
    

##  FlashSwapOrderRequest

_创建闪兑订单参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
preview_id | string | true | none | 预览结果id  
sell_currency | string | true | none | 卖出的资产名称，根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取  
sell_amount | string | true | none | 卖出的资产数量(根据预览结果)  
buy_currency | string | true | none | 买入的资产名称，根据接口`查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs`获取  
buy_amount | string | true | none | 买入的资产数量(根据预览结果)  
      
    
    {
      "preview_id": "string",
      "sell_currency": "string",
      "sell_amount": "string",
      "buy_currency": "string",
      "buy_amount": "string"
    }
    
    

##  FlashSwapCurrencyPair

_查询闪兑的交易对列表_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | false | 只读 | 交易对 ， `BTC_USDT` 表示卖`BTC`买`USDT`  
sell_currency | string | false | 只读 | 卖出币种  
buy_currency | string | false | 只读 | 买入币种  
sell_min_amount | string | false | 只读 | 卖出最小数量  
sell_max_amount | string | false | 只读 | 卖出最大数量  
buy_min_amount | string | false | 只读 | 买入最小数量  
buy_max_amount | string | false | 只读 | 买入最大数量  
      
    
    {
      "currency_pair": "string",
      "sell_currency": "BTC",
      "buy_currency": "USDT",
      "sell_min_amount": "0.00001",
      "sell_max_amount": "100",
      "buy_min_amount": "10",
      "buy_max_amount": "10000000"
    }
    
    

##  FlashSwapOrder

_闪兑订单_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | 只读 | 闪兑订单id  
create_time | integer(int64) | false | 只读 | 订单创建时间，毫秒精度  
user_id | integer(int64) | false | 只读 | 用户id  
sell_currency | string | false | 只读 | 卖出的资产名称  
sell_amount | string | false | 只读 | 卖出的资产数量  
buy_currency | string | false | 只读 | 买入的资产名称  
buy_amount | string | false | 只读 | 买入的资产数量  
price | string | false | 只读 | 价格  
status | integer | false | 只读 | 闪兑订单状态  
  
\- `1`: 成功  
\- `2`: 失败  
      
    
    {
      "id": 0,
      "create_time": 0,
      "user_id": 0,
      "sell_currency": "string",
      "sell_amount": "string",
      "buy_currency": "string",
      "buy_amount": "string",
      "price": "string",
      "status": 0
    }