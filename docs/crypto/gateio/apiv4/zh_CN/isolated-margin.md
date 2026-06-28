---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/isolated-margin
api_type: REST
updated_at: 2026-05-27 20:17:22.377273
---

# Isolated-Margin

逐仓

##  杠杆账户列表🔒 需要认证

GET`/margin/accounts`

GET `/margin/accounts`

_杠杆账户列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 交易对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [MarginAccount]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [某交易对的杠杆账户信息，`base` 对应交易货币的账户信息，`quote` 对应计价货币的账户信息]  
» _None_ | MarginAccount | 某交易对的杠杆账户信息，`base` 对应交易货币的账户信息，`quote` 对应计价货币的账户信息  
»» currency_pair | string | 交易对  
»» account_type | string | 账户类型。mmr-维持保证金率账户，inactive - 市场未激活  
»» leverage | string | 用户当前市场杠杆倍数  
»» locked | boolean | 账户是否被锁定  
»» risk | string | 已废弃  
»» mmr | string | 该逐仓杠杆账户当前维持保证金率  
»» base | MarginAccount/properties/base | 货币账户信息  
»»» currency | string | 货币名称  
»»» available | string | 可用于杠杆交易的额度，available = 保证金 + borrowed  
»»» locked | string | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
»»» borrowed | string | 借入资金  
»»» interest | string | 未还利息  
»» quote | MarginAccount/properties/base | 货币账户信息  
»»» currency | string | 货币名称  
»»» available | string | 可用于杠杆交易的额度，available = 保证金 + borrowed  
»»» locked | string | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
»»» borrowed | string | 借入资金  
»»» interest | string | 未还利息  
  
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
    
    url = '/margin/accounts'
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
    url="/margin/accounts"
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
        "currency_pair": "BTC_USDT",
        "account_type": "mmr",
        "leverage": "20",
        "locked": false,
        "risk": "1.3318",
        "mmr": "16.5949188975473644",
        "base": {
          "currency": "BTC",
          "available": "0.047060413211",
          "locked": "0",
          "borrowed": "0.047233",
          "interest": "0"
        },
        "quote": {
          "currency": "USDT",
          "available": "1234",
          "locked": "0",
          "borrowed": "0",
          "interest": "0"
        }
      }
    ]
    

##  查询杠杆账户变动历史🔒 需要认证

GET`/margin/account_book`

GET `/margin/account_book`

_查询杠杆账户变动历史_

当前只提供转入转出到杠杆账户的变动历史，记录查询时间范围不允许超过 30 天

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种查询历史，如果指定 `currency` ，必须同时指定 `currency_pair`  
currency_pair | 请求参数 | string | 否 | 指定杠杆账户交易对，该字段与 `currency` 配合使用，如果不指定 `currency`，该字段忽略  
type | 请求参数 | string | 否 | 指定账户变动类型查询，不指定则包含全部变动类型  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [MarginAccountBook]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | string | 账户变更记录 ID  
» time | string | 账户变更时间戳  
» time_ms | integer(int64) | 账户变更时间戳，毫秒单位  
» currency | string | 变更币种  
» currency_pair | string | 账户交易对  
» change | string | 变更金额，正数表示转入，负数表示转出  
» balance | string | 变更后账户余额  
» type | string | 账户变更类型 , 详见资产流水类型  
  
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
    
    url = '/margin/account_book'
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
    url="/margin/account_book"
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
        "id": "123456",
        "time": "1547633726",
        "time_ms": 1547633726123,
        "currency": "BTC",
        "currency_pair": "BTC_USDT",
        "change": "1.03",
        "balance": "4.59316525194"
      }
    ]
    

##  理财账户列表🔒 需要认证

GET`/margin/funding_accounts`

GET `/margin/funding_accounts`

_理财账户列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FundingAccount]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» currency | string | 账户货币名称  
» available | string | 理财账户可以用于借出的资金，与现货账户里对应币种的 `available` 保持一致  
» locked | string | 冻结资金数额，如正在借出的资金  
» lent | string | 已借出但仍未归还的资金数额  
» total_lent | string | 用于借出的资金总额, total_lent = lent + locked  
  
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
    
    url = '/margin/funding_accounts'
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
    url="/margin/funding_accounts"
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
        "available": "1.238",
        "locked": "0",
        "lent": "3.32",
        "total_lent": "3.32"
      }
    ]
    

##  查询用户自动还款设置🔒 需要认证

GET`/margin/auto_repay`

GET `/margin/auto_repay`

_查询用户自动还款设置_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 用户当前自动还款设置 | Inline  
  
### 返回格式

状态码 **200**

_AutoRepaySetting_

名称 | 类型 | 描述  
---|---|---  
» status | string | 自动还款状态, on - 开启，off - 关闭  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | on  
status | off  
  
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
    
    url = '/margin/auto_repay'
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
    url="/margin/auto_repay"
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
      "status": "on"
    }
    

##  修改用户自动还款设置🔒 需要认证

POST`/margin/auto_repay`

POST `/margin/auto_repay`

_修改用户自动还款设置_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
status | 请求参数 | string | 是 | 是否开启自动还款，on - 开启, off - 关闭  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 用户当前自动还款设置 | Inline  
  
### 返回格式

状态码 **200**

_AutoRepaySetting_

名称 | 类型 | 描述  
---|---|---  
» status | string | 自动还款状态, on - 开启，off - 关闭  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | on  
status | off  
  
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
    
    url = '/margin/auto_repay'
    query_param = 'status=on'
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
    url="/margin/auto_repay"
    query_param="status=on"
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
      "status": "on"
    }
    

##  逐仓杠杆允许的最大转出🔒 需要认证

GET`/margin/transferable`

GET `/margin/transferable`

_逐仓杠杆允许的最大转出_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 是 | 指定币种名称查询  
currency_pair | 请求参数 | string | 否 | 交易对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | MarginTransferable  
  
### 返回格式

状态码 **200**

_MarginTransferable_

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种信息  
» currency_pair | string | 交易对  
» amount | string | 最大可转出的额度  
  
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
    
    url = '/margin/transferable'
    query_param = 'currency=BTC'
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
    url="/margin/transferable"
    query_param="currency=BTC"
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
      "currency": "ETH",
      "currency_pair": "ETH_USDT",
      "amount": "10000"
    }
    

##  查询借贷市场列表

GET`/margin/uni/currency_pairs`

GET `/margin/uni/currency_pairs`

_查询借贷市场列表_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniCurrencyPair]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [借贷交易对]  
» _None_ | UniCurrencyPair | 借贷交易对  
»» currency_pair | string | 交易对  
»» base_min_borrow_amount | string | 交易货币最小借入数量  
»» quote_min_borrow_amount | string | 计价货币最小借入数量  
»» leverage | string | 杠杆倍数  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/margin/uni/currency_pairs'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/margin/uni/currency_pairs \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency_pair": "AE_USDT",
        "base_min_borrow_amount": "100",
        "quote_min_borrow_amount": "100",
        "leverage": "3"
      }
    ]
    

##  查询借贷市场详情

GET`/margin/uni/currency_pairs/{currency_pair}`

GET `/margin/uni/currency_pairs/{currency_pair}`

_查询借贷市场详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | URL | string | 是 | 交易对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UniCurrencyPair  
  
### 返回格式

状态码 **200**

_借贷交易对_

名称 | 类型 | 描述  
---|---|---  
» currency_pair | string | 交易对  
» base_min_borrow_amount | string | 交易货币最小借入数量  
» quote_min_borrow_amount | string | 计价货币最小借入数量  
» leverage | string | 杠杆倍数  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/margin/uni/currency_pairs/AE_USDT'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/margin/uni/currency_pairs/AE_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "currency_pair": "AE_USDT",
      "base_min_borrow_amount": "100",
      "quote_min_borrow_amount": "100",
      "leverage": "3"
    }
    

##  查询逐仓币种的预估利率🔒 需要认证

GET`/margin/uni/estimate_rate`

GET `/margin/uni/estimate_rate`

_查询逐仓币种的预估利率_

因为利率每小时会随借贷深度变化，不能提供完全精确的利率

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currencies | 请求参数 | array[string] | 是 | 指定币种名称查询数组，最大10个  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | Inline  
  
### 返回格式

状态码 **200**

_预估当前小时的借贷利率，按币种进行返回_

名称 | 类型 | 描述  
---|---|---  
» **additionalProperties** | string |   
  
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
    
    url = '/margin/uni/estimate_rate'
    query_param = 'currencies=BTC,GT'
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
    url="/margin/uni/estimate_rate"
    query_param="currencies=BTC,GT"
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
      "BTC": "0.000002",
      "GT": "0.000001"
    }
    

##  查询借贷🔒 需要认证

GET`/margin/uni/loans`

GET `/margin/uni/loans`

_查询借贷_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 交易对  
currency | 请求参数 | string | 否 | 指定币种名称查询  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniLoan]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [借贷]  
» _None_ | UniLoan | 借贷  
»» currency | string | 币种  
»» currency_pair | string | 交易对  
»» amount | string | 待归还数量  
»» type | string | 借贷类型，平台借币 - platform，杠杆借币 - margin  
»» create_time | integer(int64) | 创建时间戳  
»» update_time | integer(int64) | 最近更新时间戳  
  
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
    
    url = '/margin/uni/loans'
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
    url="/margin/uni/loans"
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
        "currency_pari": "GT_USDT",
        "amount": "1",
        "type": "margin",
        "change_time": 1673247054000,
        "create_time": 1673247054000
      }
    ]
    

##  借入或还款🔒 需要认证

POST`/margin/uni/loans`

POST `/margin/uni/loans`

_借入或还款_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CreateUniLoan | 是 |   
» currency | body | string | 是 | 币种  
» type | body | string | 是 | 借贷类型，margin表示为杠杆借币  
» amount | body | string | 是 | 借入或还款数量  
» repaid_all | body | boolean | 否 | 全部还款，仅还款操作使用 ， 为`true`时覆盖`amount` ， 直接全部还款  
» currency_pair | body | string | 是 | 交易对  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» type | borrow  
» type | repay  
  
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
    
    url = '/margin/uni/loans'
    query_param = ''
    body='{"currency":"BTC","amount":"0.1","type":"borrow","currency_pair":"BTC_USDT","repaid_all":false}'
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
    url="/margin/uni/loans"
    query_param=""
    body_param='{"currency":"BTC","amount":"0.1","type":"borrow","currency_pair":"BTC_USDT","repaid_all":false}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "currency": "BTC",
      "amount": "0.1",
      "type": "borrow",
      "currency_pair": "BTC_USDT",
      "repaid_all": false
    }
    

##  查询借贷记录🔒 需要认证

GET`/margin/uni/loan_records`

GET `/margin/uni/loan_records`

_查询借贷记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
type | 请求参数 | string | 否 | 类型 , borrow - 借入 , repay - 还款  
currency | 请求参数 | string | 否 | 指定币种名称查询  
currency_pair | 请求参数 | string | 否 | 交易对  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
type | borrow  
type | repay  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniLoanRecord]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [借贷记录]  
» _None_ | UniLoanRecord | 借贷记录  
»» type | string | 类型 , borrow - 借入 , repay - 还款  
»» currency_pair | string | 交易对  
»» currency | string | 币种  
»» amount | string | 借入或还款数量  
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
    
    url = '/margin/uni/loan_records'
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
    url="/margin/uni/loan_records"
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
        "type": "borrow",
        "currency_pair": "AE_USDT",
        "currency": "USDT",
        "amount": "1000",
        "create_time": 1673247054000
      }
    ]
    

##  查询扣息记录🔒 需要认证

GET`/margin/uni/interest_records`

GET `/margin/uni/interest_records`

_查询扣息记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 交易对  
currency | 请求参数 | string | 否 | 指定币种名称查询  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
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
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniLoanInterestRecord]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [扣息记录]  
» _None_ | UniLoanInterestRecord | 扣息记录  
»» currency | string | 币种名称  
»» currency_pair | string | 交易对  
»» actual_rate | string | 实际利率  
»» interest | string | 利息  
»» status | integer | 状态 0 - 失败 , 1 - 成功  
»» type | string | 借贷类型，margin表示为杠杆借币  
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
    
    url = '/margin/uni/interest_records'
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
    url="/margin/uni/interest_records"
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
        "currency_pair": "BTC_USDT",
        "currency": "USDT",
        "actual_rate": "0.00000236",
        "interest": "0.00006136",
        "type": "platform",
        "create_time": 1673247054000
      }
    ]
    

##  查询币种最大可借🔒 需要认证

GET`/margin/uni/borrowable`

GET `/margin/uni/borrowable`

_查询币种最大可借_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 是 | 指定币种名称查询  
currency_pair | 请求参数 | string | 是 | 交易对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | MaxUniBorrowable  
  
### 返回格式

状态码 **200**

_MaxUniBorrowable_

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种  
» currency_pair | string | 交易对  
» borrowable | string | 最大可借  
  
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
    
    url = '/margin/uni/borrowable'
    query_param = 'currency=BTC&currency_pair=BTC_USDT'
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
    url="/margin/uni/borrowable"
    query_param="currency=BTC&currency_pair=BTC_USDT"
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
      "currency": "AE",
      "borrowable": "1123.344",
      "currency_pair": "AE_USDT"
    }
    

##  查询当前市场下用户自身杠杆借贷梯度🔒 需要认证

GET`/margin/user/loan_margin_tiers`

GET `/margin/user/loan_margin_tiers`

_查询当前市场下用户自身杠杆借贷梯度_

查询指定的逐仓杠杆现货市场的借贷梯度保证金要求，详情交易规则见：新逐仓杠杆底层逻辑（https://www.gate.com/zh/help/trade/margin-trading/42357）

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 是 | 交易对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [MarginLeverageTier]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [市场梯度信息]  
» _None_ | MarginLeverageTier | 市场梯度信息  
»» upper_limit | string | 最大借币限额。由用户设置的杠杆倍数决定，杠杆倍数越低，借币限额越大  
»» mmr | string | 维持保证金率。在梯度保证金要求规则(https://www.gate.com/zh/help/trade/margin-trading/42357)下，维持保证金率为一个综合值  
»» leverage | string | 当下可开的最大杠杆倍数。由用户当前的负债规模决定，负债规模越大，可开的最大杠杆倍数越低  
  
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
    
    url = '/margin/user/loan_margin_tiers'
    query_param = 'currency_pair=BTC_USDT'
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
    url="/margin/user/loan_margin_tiers"
    query_param="currency_pair=BTC_USDT"
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
        "tier_amount": "100",
        "mmr": "0.9",
        "leverage": "1"
      }
    ]
    

##  查询当前市场杠杆借贷梯度

GET`/margin/loan_margin_tiers`

GET `/margin/loan_margin_tiers`

_查询当前市场杠杆借贷梯度_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 是 | 交易对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [MarginLeverageTier]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [市场梯度信息]  
» _None_ | MarginLeverageTier | 市场梯度信息  
»» upper_limit | string | 最大借币限额。由用户设置的杠杆倍数决定，杠杆倍数越低，借币限额越大  
»» mmr | string | 维持保证金率。在梯度保证金要求规则(https://www.gate.com/zh/help/trade/margin-trading/42357)下，维持保证金率为一个综合值  
»» leverage | string | 当下可开的最大杠杆倍数。由用户当前的负债规模决定，负债规模越大，可开的最大杠杆倍数越低  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/margin/loan_margin_tiers'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/margin/loan_margin_tiers?currency_pair=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "tier_amount": "100",
        "mmr": "0.9",
        "leverage": "1"
      }
    ]
    

##  设置用户市场杠杆倍数🔒 需要认证

POST`/margin/leverage/user_market_setting`

POST `/margin/leverage/user_market_setting`

_设置用户市场杠杆倍数_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | MarginMarketLeverage | 是 |   
» currency_pair | body | string | 否 | 市场  
» leverage | body | string | 是 | 杠杆倍数  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 设置成功 | 无  
  
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
    
    url = '/margin/leverage/user_market_setting'
    query_param = ''
    body='{"currency_pair":"BTC_USDT","leverage":"10"}'
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
    url="/margin/leverage/user_market_setting"
    query_param=""
    body_param='{"currency_pair":"BTC_USDT","leverage":"10"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "currency_pair": "BTC_USDT",
      "leverage": "10"
    }
    

##  查询用户逐仓杠杆账户列表🔒 需要认证

GET`/margin/user/account`

GET `/margin/user/account`

_查询用户逐仓杠杆账户列表_

支持查询风险率逐仓账户和保证金率逐仓账户

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 交易对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [MarginAccount]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [某交易对的杠杆账户信息，`base` 对应交易货币的账户信息，`quote` 对应计价货币的账户信息]  
» _None_ | MarginAccount | 某交易对的杠杆账户信息，`base` 对应交易货币的账户信息，`quote` 对应计价货币的账户信息  
»» currency_pair | string | 交易对  
»» account_type | string | 账户类型。mmr-维持保证金率账户，inactive - 市场未激活  
»» leverage | string | 用户当前市场杠杆倍数  
»» locked | boolean | 账户是否被锁定  
»» risk | string | 已废弃  
»» mmr | string | 该逐仓杠杆账户当前维持保证金率  
»» base | MarginAccount/properties/base | 货币账户信息  
»»» currency | string | 货币名称  
»»» available | string | 可用于杠杆交易的额度，available = 保证金 + borrowed  
»»» locked | string | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
»»» borrowed | string | 借入资金  
»»» interest | string | 未还利息  
»» quote | MarginAccount/properties/base | 货币账户信息  
»»» currency | string | 货币名称  
»»» available | string | 可用于杠杆交易的额度，available = 保证金 + borrowed  
»»» locked | string | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
»»» borrowed | string | 借入资金  
»»» interest | string | 未还利息  
  
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
    
    url = '/margin/user/account'
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
    url="/margin/user/account"
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
        "currency_pair": "BTC_USDT",
        "account_type": "mmr",
        "leverage": "20",
        "locked": false,
        "risk": "1.3318",
        "mmr": "16.5949188975473644",
        "base": {
          "currency": "BTC",
          "available": "0.047060413211",
          "locked": "0",
          "borrowed": "0.047233",
          "interest": "0"
        },
        "quote": {
          "currency": "USDT",
          "available": "1234",
          "locked": "0",
          "borrowed": "0",
          "interest": "0"
        }
      }
    ]
    

#  模型

##  UniLoanRecord

_借贷记录_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
type | string | false | 只读 | 类型 , borrow - 借入 , repay - 还款  
currency_pair | string | false | 只读 | 交易对  
currency | string | false | 只读 | 币种  
amount | string | false | 只读 | 借入或还款数量  
create_time | integer(int64) | false | 只读 | 创建时间戳  
      
    
    {
      "type": "string",
      "currency_pair": "string",
      "currency": "string",
      "amount": "string",
      "create_time": 0
    }
    
    

##  MarginAccountBook

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | none | 账户变更记录 ID  
time | string | false | none | 账户变更时间戳  
time_ms | integer(int64) | false | none | 账户变更时间戳，毫秒单位  
currency | string | false | none | 变更币种  
currency_pair | string | false | none | 账户交易对  
change | string | false | none | 变更金额，正数表示转入，负数表示转出  
balance | string | false | none | 变更后账户余额  
type | string | false | none | 账户变更类型 , 详见资产流水类型  
      
    
    {
      "id": "string",
      "time": "string",
      "time_ms": 0,
      "currency": "string",
      "currency_pair": "string",
      "change": "string",
      "balance": "string",
      "type": "string"
    }
    
    

##  UniLoan

_借贷_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | 只读 | 币种  
currency_pair | string | false | 只读 | 交易对  
amount | string | false | 只读 | 待归还数量  
type | string | false | 只读 | 借贷类型，平台借币 - platform，杠杆借币 - margin  
create_time | integer(int64) | false | 只读 | 创建时间戳  
update_time | integer(int64) | false | 只读 | 最近更新时间戳  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "amount": "string",
      "type": "string",
      "create_time": 0,
      "update_time": 0
    }
    
    

##  MarginMarketLeverage

_市场杠杆设置_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | false | none | 市场  
leverage | string | true | none | 杠杆倍数  
      
    
    {
      "currency_pair": "string",
      "leverage": "string"
    }
    
    

##  FundingAccount

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 账户货币名称  
available | string | false | none | 理财账户可以用于借出的资金，与现货账户里对应币种的 `available` 保持一致  
locked | string | false | none | 冻结资金数额，如正在借出的资金  
lent | string | false | none | 已借出但仍未归还的资金数额  
total_lent | string | false | none | 用于借出的资金总额, total_lent = lent + locked  
      
    
    {
      "currency": "string",
      "available": "string",
      "locked": "string",
      "lent": "string",
      "total_lent": "string"
    }
    
    

##  CreateUniLoan

_借入或还款_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | true | none | 币种  
type | string | true | none | 借贷类型，margin表示为杠杆借币  
amount | string | true | none | 借入或还款数量  
repaid_all | boolean | false | none | 全部还款，仅还款操作使用 ， 为`true`时覆盖`amount` ， 直接全部还款  
currency_pair | string | true | none | 交易对  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | borrow  
type | repay  
      
    
    {
      "currency": "string",
      "type": "borrow",
      "amount": "string",
      "repaid_all": true,
      "currency_pair": "string"
    }
    
    

##  UniLoanInterestRecord

_扣息记录_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | 只读 | 币种名称  
currency_pair | string | false | 只读 | 交易对  
actual_rate | string | false | 只读 | 实际利率  
interest | string | false | 只读 | 利息  
status | integer | false | 只读 | 状态 0 - 失败 , 1 - 成功  
type | string | false | 只读 | 借贷类型，margin表示为杠杆借币  
create_time | integer(int64) | false | 只读 | 创建时间戳  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "actual_rate": "string",
      "interest": "string",
      "status": 0,
      "type": "string",
      "create_time": 0
    }
    
    

##  UniCurrencyPair

_借贷交易对_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | false | 只读 | 交易对  
base_min_borrow_amount | string | false | 只读 | 交易货币最小借入数量  
quote_min_borrow_amount | string | false | 只读 | 计价货币最小借入数量  
leverage | string | false | 只读 | 杠杆倍数  
      
    
    {
      "currency_pair": "string",
      "base_min_borrow_amount": "string",
      "quote_min_borrow_amount": "string",
      "leverage": "string"
    }
    
    

##  MaxUniBorrowable

_MaxUniBorrowable_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | true | 只读 | 币种  
currency_pair | string | false | 只读 | 交易对  
borrowable | string | true | 只读 | 最大可借  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "borrowable": "string"
    }
    
    

##  MarginLeverageTier

_市场梯度信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
upper_limit | string | false | none | 最大借币限额。由用户设置的杠杆倍数决定，杠杆倍数越低，借币限额越大  
mmr | string | false | none | 维持保证金率。在梯度保证金要求规则(https://www.gate.com/zh/help/trade/margin-trading/42357)下，维持保证金率为一个综合值  
leverage | string | false | none | 当下可开的最大杠杆倍数。由用户当前的负债规模决定，负债规模越大，可开的最大杠杆倍数越低  
      
    
    {
      "upper_limit": "string",
      "mmr": "string",
      "leverage": "string"
    }
    
    

##  MarginAccount

_某交易对的杠杆账户信息，`base` 对应交易货币的账户信息，`quote` 对应计价货币的账户信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | false | none | 交易对  
account_type | string | false | none | 账户类型。mmr-维持保证金率账户，inactive - 市场未激活  
leverage | string | false | none | 用户当前市场杠杆倍数  
locked | boolean | false | none | 账户是否被锁定  
risk | string | false | none | 已废弃  
mmr | string | false | none | 该逐仓杠杆账户当前维持保证金率  
base | object | false | none | 货币账户信息  
» currency | string | false | none | 货币名称  
» available | string | false | none | 可用于杠杆交易的额度，available = 保证金 + borrowed  
» locked | string | false | none | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
» borrowed | string | false | none | 借入资金  
» interest | string | false | none | 未还利息  
quote | MarginAccount/properties/base | false | none | 货币账户信息  
      
    
    {
      "currency_pair": "string",
      "account_type": "string",
      "leverage": "string",
      "locked": true,
      "risk": "string",
      "mmr": "string",
      "base": {
        "currency": "string",
        "available": "string",
        "locked": "string",
        "borrowed": "string",
        "interest": "string"
      },
      "quote": {
        "currency": "string",
        "available": "string",
        "locked": "string",
        "borrowed": "string",
        "interest": "string"
      }
    }
    
    

##  MarginTransferable

_MarginTransferable_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种信息  
currency_pair | string | false | none | 交易对  
amount | string | false | none | 最大可转出的额度  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "amount": "string"
    }
    
    

##  EstimateRate

_预估当前小时的借贷利率，按币种进行返回_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
**additionalProperties** | string | false | none | none  
      
    
    {
      "property1": "string",
      "property2": "string"
    }