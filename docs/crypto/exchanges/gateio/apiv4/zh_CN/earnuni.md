---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/earnuni
api_type: Earn
updated_at: 2026-05-27 20:17:08.222853
---

# EarnUni

余币宝理财

##  查询理财币种列表

GET`/earn/uni/currencies`

GET `/earn/uni/currencies`

_查询理财币种列表_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniCurrency]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [借贷币种]  
» _None_ | UniCurrency | 借贷币种  
»» currency | string | 币种名称  
»» min_lend_amount | string | 最小借出数量,单位该币种  
»» max_lend_amount | string | 累计最大借出数量，单位USDT  
»» max_rate | string | 最大利率（小时）  
»» min_rate | string | 最小利率（小时）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/uni/currencies'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/uni/currencies \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency": "AE",
        "min_lend_amount": "100",
        "max_lend_amount": "200000000",
        "max_rate": "0.00057",
        "min_rate": "0.000001"
      }
    ]
    

##  查询单个理财币种详情

GET`/earn/uni/currencies/{currency}`

GET `/earn/uni/currencies/{currency}`

_查询单个理财币种详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | URL | string | 是 | 币种  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UniCurrency  
  
### 返回格式

状态码 **200**

_借贷币种_

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种名称  
» min_lend_amount | string | 最小借出数量,单位该币种  
» max_lend_amount | string | 累计最大借出数量，单位USDT  
» max_rate | string | 最大利率（小时）  
» min_rate | string | 最小利率（小时）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/uni/currencies/btc'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/uni/currencies/btc \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "currency": "AE",
      "min_lend_amount": "100",
      "max_lend_amount": "200000000",
      "max_rate": "0.00057",
      "min_rate": "0.000001"
    }
    

##  查询用户币种理财列表🔒 需要认证

GET`/earn/uni/lends`

GET `/earn/uni/lends`

_查询用户币种理财列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大100。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniLend]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [理财信息]  
» _None_ | UniLend | 理财信息  
»» currency | string | 币种  
»» current_amount | string | 本次理财数量  
»» amount | string | 理财总数量  
»» lent_amount | string | 已借出数量  
»» frozen_amount | string | 已申请赎回未到账数量  
»» min_rate | string | 最小利率  
»» interest_status | string | 利息状态; interest_dividend - 正常派息, interest_reinvest - 利息复投  
»» reinvest_left_amount | string | 未复投金额  
»» create_time | integer(int64) | 理财创建时间  
»» update_time | integer(int64) | 理财最新修改时间  
  
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
    
    url = '/earn/uni/lends'
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
    url="/earn/uni/lends"
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
        "currency": "BTC",
        "current_amount": "20.999992",
        "amount": "20.999992",
        "lent_amount": "0",
        "frozen_amount": "0",
        "min_rate": "0.1",
        "interest_status": "interest_dividend",
        "reinvest_left_amount": 0,
        "create_time": 1673247054000,
        "update_time": 1673247054000
      }
    ]
    

##  创建理财或赎回🔒 需要认证

POST`/earn/uni/lends`

POST `/earn/uni/lends`

_创建理财或赎回_

借出：在借出时需要设置最低借出利率，整点判定借出成功后按照判定的利率计算收益， 每个整点结算该小时收益，若由于利率过高导致借出失败则该小时无法获得利息， 若在整点判定前赎回资金则该小时无法获得利息。 关于优先级：相同利率下先创建或先修改的理财优先被借出。 赎回：借出失败的资金，赎回可立即到账， 对于借出成功的资金，享受该小时收益，赎回后将在下个整点到账。 注意：整点前后两分钟为结算时间，禁止理财和赎回

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CreateUniLend | 是 |   
» currency | body | string | 是 | 币种名称  
» amount | body | string | 是 | 投入理财池数量  
» type | body | string | 是 | 操作类型 ; lend - 借出 ， redeem - 赎回  
» min_rate | body | string | 否 | 最小利率，如设置过高可能导致借出失败则该无法获得利息，借出时必填  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» type | lend  
» type | redeem  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 操作成功 | 无  
  
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
    
    url = '/earn/uni/lends'
    query_param = ''
    body='{"currency":"AE","amount":"100","min_rate":"0.00001","type":"lend"}'
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
    url="/earn/uni/lends"
    query_param=""
    body_param='{"currency":"AE","amount":"100","min_rate":"0.00001","type":"lend"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "currency": "AE",
      "amount": "100",
      "min_rate": "0.00001",
      "type": "lend"
    }
    

##  修改用户理财信息🔒 需要认证

PATCH`/earn/uni/lends`

PATCH `/earn/uni/lends`

_修改用户理财信息_

目前只支持修改最小利率（小时）

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | PatchUniLend | 是 |   
» currency | body | string | 否 | 币种名称  
» min_rate | body | string | 否 | 最小利率  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 修改成功 | 无  
  
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
    
    url = '/earn/uni/lends'
    query_param = ''
    body='{"currency":"AE","min_rate":"0.0001"}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('PATCH', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('PATCH', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="PATCH"
    url="/earn/uni/lends"
    query_param=""
    body_param='{"currency":"AE","min_rate":"0.0001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "currency": "AE",
      "min_rate": "0.0001"
    }
    

##  查询理财的流水记录🔒 需要认证

GET`/earn/uni/lend_records`

GET `/earn/uni/lend_records`

_查询理财的流水记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大100。  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
type | 请求参数 | string | 否 | 操作类型 ; lend - 借出 ， redeem - 赎回  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
type | lend  
type | redeem  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniLendRecord]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [理财记录]  
» _None_ | UniLendRecord | 理财记录  
»» currency | string | 币种名称  
»» amount | string | 本次借出或赎回数量  
»» last_wallet_amount | string | 该记录之前待理财数量  
»» last_lent_amount | string | 该记录之前已借出数量  
»» last_frozen_amount | string | 该记录之前已冻结待待赎回数量  
»» type | string | 记录类型 lend - 借出 , redeem - 赎回  
»» create_time | integer(int64) | 创建时间戳  
  
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
    
    url = '/earn/uni/lend_records'
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
    url="/earn/uni/lend_records"
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
        "type": "lend",
        "currency": "BTC",
        "amount": "1",
        "last_wallet_amount": "0.2",
        "last_lent_amount": "0",
        "last_frozen_amount": "0",
        "create_time": 1673247054000
      }
    ]
    

##  查询用户单币种总利息收益🔒 需要认证

GET`/earn/uni/interests/{currency}`

GET `/earn/uni/interests/{currency}`

_查询用户单币种总利息收益_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | URL | string | 是 | 币种  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UniLendInterest  
  
### 返回格式

状态码 **200**

_UniLendInterest_

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种  
» interest | string | 利息收益  
  
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
    
    url = '/earn/uni/interests/btc'
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
    url="/earn/uni/interests/btc"
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
      "currency": "AE",
      "interest": "123.345"
    }
    

##  查询用户派息记录🔒 需要认证

GET`/earn/uni/interest_records`

GET `/earn/uni/interest_records`

_查询用户派息记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大100。  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniInterestRecord]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [派息记录]  
» _None_ | UniInterestRecord | 派息记录  
»» status | integer | 状态 0 - 失败 , 1 - 成功  
»» currency | string | 币种  
»» actual_rate | string | 真实利率  
»» interest | string | 利息  
»» interest_status | string | 利息状态; interest_dividend - 正常派息, interest_reinvest - 利息复投  
»» create_time | integer(int64) | 创建时间戳  
  
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
    
    url = '/earn/uni/interest_records'
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
    url="/earn/uni/interest_records"
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
        "status": 1,
        "currency": "AE",
        "actual_rate": "0.0005",
        "interest": "0.05",
        "interest_status": "interest_dividend",
        "create_time": 1673247054000
      }
    ]
    

##  查询币种利息复利状态🔒 需要认证

GET`/earn/uni/interest_status/{currency}`

GET `/earn/uni/interest_status/{currency}`

_查询币种利息复利状态_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | URL | string | 是 | 币种  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UniCurrencyInterest  
  
### 返回格式

状态码 **200**

_UniCurrencyInterest_

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种  
» interest_status | string | 利息状态; interest_dividend - 正常派息, interest_reinvest - 利息复投  
  
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
    
    url = '/earn/uni/interest_status/btc'
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
    url="/earn/uni/interest_status/btc"
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
      "currency": "BTC",
      "interest_status": "interest_dividend"
    }
    

##  余币宝币种年化走势图🔒 需要认证

GET`/earn/uni/chart`

GET `/earn/uni/chart`

_余币宝币种年化走势图_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
from | 请求参数 | integer(int64) | 是 | 开始时间戳，单位s，最大跨度30天  
to | 请求参数 | integer(int64) | 是 | 结束时间戳，单位s，最大跨度30天  
asset | 请求参数 | string | 是 | 币种名称  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» UniChartPoint | object |   
»» time | integer(int64) |   
»» value | string |   
  
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
    
    url = '/earn/uni/chart'
    query_param = 'from=1719763200&to=1722441600&asset=BTC'
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
    url="/earn/uni/chart"
    query_param="from=1719763200&to=1722441600&asset=BTC"
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
        "time": 1719705600,
        "value": "0.01"
      }
    ]
    

##  币种预估年化利率🔒 需要认证

GET`/earn/uni/rate`

GET `/earn/uni/rate`

_币种预估年化利率_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» UniEstimatedRate | object |   
»» currency | string |   
»» est_rate | string | 预估年化利率，例如，`est_rate`: `0.8014` 为 80.14% 的年化利率  
  
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
    
    url = '/earn/uni/rate'
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
    url="/earn/uni/rate"
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
        "currency": "USDT",
        "est_rate": "0.0226"
      }
    ]
    

#  模型

##  UniLendInterest

_UniLendInterest_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | 只读 | 币种  
interest | string | false | 只读 | 利息收益  
      
    
    {
      "currency": "string",
      "interest": "string"
    }
    
    

##  CreateUniLend

_创建理财或赎回_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | true | none | 币种名称  
amount | string | true | none | 投入理财池数量  
type | string | true | none | 操作类型 ; lend - 借出 ， redeem - 赎回  
min_rate | string | false | none | 最小利率，如设置过高可能导致借出失败则该无法获得利息，借出时必填  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | lend  
type | redeem  
      
    
    {
      "currency": "string",
      "amount": "string",
      "type": "lend",
      "min_rate": "string"
    }
    
    

##  UniCurrency

_借贷币种_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | 只读 | 币种名称  
min_lend_amount | string | false | 只读 | 最小借出数量,单位该币种  
max_lend_amount | string | false | 只读 | 累计最大借出数量，单位USDT  
max_rate | string | false | 只读 | 最大利率（小时）  
min_rate | string | false | 只读 | 最小利率（小时）  
      
    
    {
      "currency": "string",
      "min_lend_amount": "string",
      "max_lend_amount": "string",
      "max_rate": "string",
      "min_rate": "string"
    }
    
    

##  UniLend

_理财信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | 只读 | 币种  
current_amount | string | false | 只读 | 本次理财数量  
amount | string | false | 只读 | 理财总数量  
lent_amount | string | false | 只读 | 已借出数量  
frozen_amount | string | false | 只读 | 已申请赎回未到账数量  
min_rate | string | false | 只读 | 最小利率  
interest_status | string | false | 只读 | 利息状态; interest_dividend - 正常派息, interest_reinvest - 利息复投  
reinvest_left_amount | string | false | 只读 | 未复投金额  
create_time | integer(int64) | false | 只读 | 理财创建时间  
update_time | integer(int64) | false | 只读 | 理财最新修改时间  
      
    
    {
      "currency": "string",
      "current_amount": "string",
      "amount": "string",
      "lent_amount": "string",
      "frozen_amount": "string",
      "min_rate": "string",
      "interest_status": "string",
      "reinvest_left_amount": "string",
      "create_time": 0,
      "update_time": 0
    }
    
    

##  UniLendRecord

_理财记录_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | 只读 | 币种名称  
amount | string | false | 只读 | 本次借出或赎回数量  
last_wallet_amount | string | false | 只读 | 该记录之前待理财数量  
last_lent_amount | string | false | 只读 | 该记录之前已借出数量  
last_frozen_amount | string | false | 只读 | 该记录之前已冻结待待赎回数量  
type | string | false | 只读 | 记录类型 lend - 借出 , redeem - 赎回  
create_time | integer(int64) | false | 只读 | 创建时间戳  
      
    
    {
      "currency": "string",
      "amount": "string",
      "last_wallet_amount": "string",
      "last_lent_amount": "string",
      "last_frozen_amount": "string",
      "type": "string",
      "create_time": 0
    }
    
    

##  UniInterestRecord

_派息记录_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
status | integer | false | 只读 | 状态 0 - 失败 , 1 - 成功  
currency | string | false | 只读 | 币种  
actual_rate | string | false | 只读 | 真实利率  
interest | string | false | 只读 | 利息  
interest_status | string | false | 只读 | 利息状态; interest_dividend - 正常派息, interest_reinvest - 利息复投  
create_time | integer(int64) | false | 只读 | 创建时间戳  
      
    
    {
      "status": 0,
      "currency": "string",
      "actual_rate": "string",
      "interest": "string",
      "interest_status": "string",
      "create_time": 0
    }
    
    

##  UniCurrencyInterest

_UniCurrencyInterest_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | 只读 | 币种  
interest_status | string | false | 只读 | 利息状态; interest_dividend - 正常派息, interest_reinvest - 利息复投  
      
    
    {
      "currency": "string",
      "interest_status": "string"
    }
    
    

##  PatchUniLend

_PatchUniLend_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种名称  
min_rate | string | false | none | 最小利率  
      
    
    {
      "currency": "string",
      "min_rate": "string"
    }