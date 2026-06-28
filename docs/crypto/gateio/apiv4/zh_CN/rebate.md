---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/rebate
api_type: Earn
updated_at: 2026-05-27 20:17:44.573613
---

# Rebate

返佣相关接口，包括代理商、合伙人、经纪商的交易记录查询和返佣记录查询

##  代理商获取推荐用户的交易记录🔒 需要认证

GET`/rebate/agency/transaction_history`

GET `/rebate/agency/transaction_history`

_代理商获取推荐用户的交易记录_

记录查询时间范围不允许超过 30 天

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 指定查询交易对，不指定返回全部交易对  
user_id | 请求参数 | integer(int64) | 否 | 用户 ID，不指定则返回所有用户的记录  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间，不指定则默认从当前时间开始向前推 7 天  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | Inline  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» currency_pair | string | 交易对  
» total | integer(int64) | 该查询下数据总数  
» list | array | 交易列表  
»» AgencyTransaction | object |   
»»» transaction_time | integer(int64) | 交易时间，秒级 Unix 时间戳  
»»» user_id | integer(int64) | 用户 ID  
»»» group_name | string | 分组名称  
»»» fee | string | 手续费数量  
»»» fee_asset | string | 手续费币种  
»»» currency_pair | string | 交易对  
»»» amount | string | 交易金额数量  
»»» amount_asset | string | 交易金额币种  
»»» source | string | 返佣交易类型, SPOT - 现货返佣, FUTURES - 合约返佣  
  
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
    
    url = '/rebate/agency/transaction_history'
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
    url="/rebate/agency/transaction_history"
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
      "total": 100,
      "list": [
        {
          "transaction_time": 1539852480,
          "user_id": 10000,
          "group_name": "gateio",
          "fee": "1",
          "fee_asset": "GT",
          "currency_pair": "GT_USDT",
          "amount": "1000",
          "source": "SPOT",
          "amount_asset": "GT"
        }
      ]
    }
    

##  代理商获取推荐用户的返佣记录🔒 需要认证

GET`/rebate/agency/commission_history`

GET `/rebate/agency/commission_history`

_代理商获取推荐用户的返佣记录_

记录查询时间范围不允许超过 30 天

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定查询币种，不指定返回全部币种  
commission_type | 请求参数 | integer | 否 | 返佣类型 1-直接返佣, 2-间接返佣, 3-自身返佣  
user_id | 请求参数 | integer(int64) | 否 | 用户 ID，不指定则返回所有用户的记录  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间，不指定则默认从当前时间开始向前推 7 天  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | Inline  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» currency_pair | string | 交易对  
» total | integer(int64) | 该查询下数据总数  
» list | array | 返佣列表  
»» AgencyCommission | object |   
»»» commission_time | integer(int64) | 返佣时间，秒级 Unix 时间戳  
»»» user_id | integer(int64) | 用户ID  
»»» group_name | string | 分组名称  
»»» commission_amount | string | 返佣金额数量  
»»» commission_asset | string | 返佣金额币种  
»»» source | string | 返佣交易类型, SPOT - 现货返佣, FUTURES - 合约返佣  
  
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
    
    url = '/rebate/agency/commission_history'
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
    url="/rebate/agency/commission_history"
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
      "total": 100,
      "list": [
        {
          "commission_time": 1539852480,
          "user_id": 10000,
          "group_name": "gateio",
          "commission_amount": "1000",
          "source": "SPOT",
          "commission_asset": "GT"
        }
      ]
    }
    

##  合伙人获取推荐用户的交易记录🔒 需要认证

GET`/rebate/partner/transaction_history`

GET `/rebate/partner/transaction_history`

_合伙人获取推荐用户的交易记录_

记录查询时间范围不允许超过 30 天

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 指定查询交易对，不指定返回全部交易对  
user_id | 请求参数 | integer(int64) | 否 | 用户 ID，不指定则返回所有用户的记录  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间，不指定则默认从当前时间开始向前推 7 天  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | PartnerTransactionHistory  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» total | integer(int64) | 该查询下数据总数  
» list | array | 交易列表  
»» PartnerTransaction | object |   
»»» transaction_time | integer(int64) | 交易时间，秒级 Unix 时间戳  
»»» user_id | integer(int64) | 用户 ID  
»»» group_name | string | 分组名称  
»»» fee | string | 手续费数量  
»»» fee_asset | string | 手续费币种  
»»» currency_pair | string | 交易对  
»»» amount | string | 交易金额数量  
»»» amount_asset | string | 交易金额币种  
»»» source | string | 返佣交易类型, SPOT - 现货返佣, FUTURES - 合约返佣  
  
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
    
    url = '/rebate/partner/transaction_history'
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
    url="/rebate/partner/transaction_history"
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
      "total": 15,
      "list": [
        {
          "user_id": 1879032535,
          "group_name": "test",
          "fee": "0.00044800",
          "transaction_time": 1718615824,
          "amount": "29.98688000",
          "amount_asset": "USDT",
          "currency_pair": "BCH_USDT",
          "source": "SPOT",
          "fee_asset": "BCH"
        }
      ]
    }
    

##  合伙人获取推荐用户的返佣记录🔒 需要认证

GET`/rebate/partner/commission_history`

GET `/rebate/partner/commission_history`

_合伙人获取推荐用户的返佣记录_

记录查询时间范围不允许超过 30 天

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定查询币种，不指定返回全部币种  
user_id | 请求参数 | integer(int64) | 否 | 用户 ID，不指定则返回所有用户的记录  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间，不指定则默认从当前时间开始向前推 7 天  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | PartnerCommissionHistory  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» total | integer(int64) | 该查询下数据总数  
» list | array | 返佣列表  
»» PartnerCommission | object |   
»»» commission_time | integer(int64) | 返佣时间，秒级 Unix 时间戳  
»»» user_id | integer(int64) | 用户ID  
»»» group_name | string | 分组名称  
»»» commission_amount | string | 返佣金额数量  
»»» commission_asset | string | 返佣金额币种  
»»» source | string | 返佣交易类型, SPOT - 现货返佣, FUTURES - 合约返佣  
  
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
    
    url = '/rebate/partner/commission_history'
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
    url="/rebate/partner/commission_history"
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
      "total": 52,
      "list": [
        {
          "user_id": 1879043947,
          "commission_time": 1718616728,
          "commission_amount": "0.2216934846",
          "commission_asset": "USDT",
          "source": "SPOT",
          "group_name": "test"
        }
      ]
    }
    

##  合伙人下级列表🔒 需要认证

GET`/rebate/partner/sub_list`

GET `/rebate/partner/sub_list`

_合伙人下级列表_

包含下级代理、直接直客、间接直客

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id | 请求参数 | integer(int64) | 否 | 用户 ID，不指定则返回所有用户的记录  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | PartnerSubList  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» total | integer(int64) | 该查询下数据总数  
» list | array | 下级列表  
»» PartnerSub | object |   
»»» user_id | integer(int64) | 用户 ID  
»»» user_join_time | integer(int64) | 用户加入体系的时间，秒级 Unix 时间戳  
»»» type | integer(int64) | 类型(1-子代理 2-间接直客 3-直接直客)  
  
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
    
    url = '/rebate/partner/sub_list'
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
    url="/rebate/partner/sub_list"
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
      "total": 3,
      "list": [
        {
          "user_id": 1,
          "user_join_time": 1666255731,
          "type": 1
        },
        {
          "user_id": 2,
          "user_join_time": 1666271213,
          "type": 2
        },
        {
          "user_id": 3,
          "user_join_time": 1666422143,
          "type": 3
        }
      ]
    }
    

##  经纪商获取用户的返佣记录🔒 需要认证

GET`/rebate/broker/commission_history`

GET `/rebate/broker/commission_history`

_经纪商获取用户的返佣记录_

记录查询时间范围不允许超过 30 天

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
user_id | 请求参数 | integer(int64) | 否 | 用户 ID，不指定则返回所有用户的记录  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间，不指定则默认从当前时间开始向前推 30 天  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | Inline  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» total | integer(int64) | 该查询下数据总数  
» list | array | 返佣列表  
»» BrokerCommissionItem | object |   
»»» commission_time | integer(int64) | 返佣时间，秒级 Unix 时间戳  
»»» user_id | integer(int64) | 用户ID  
»»» group_name | string | 分组名称  
»»» amount | string | 返佣金额  
»»» fee | string | 手续费数量  
»»» fee_asset | string | 手续费币种  
»»» rebate_fee | string | 折算为USDT后返还收入  
»»» source | string | 返佣交易类型：Spot、Futures、Options、Alpha、TradFi  
»»» currency_pair | string | 交易对  
»»» sub_broker_info | object | 子经纪商信息  
»»»» user_id | integer(int64) | 子经纪商用户ID  
»»»» original_commission_rate | string | 子经纪商原始返佣比例  
»»»» relative_commission_rate | string | 子经纪商相对返佣比例  
»»»» commission_rate | string | 子经纪商实际返佣比例  
»»» alpha_contract_addr | string | Alpha合约地址  
  
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
    
    url = '/rebate/broker/commission_history'
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
    url="/rebate/broker/commission_history"
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
      "list": [
        {
          "user_id": 110285113,
          "group_name": "",
          "commission_time": 1702545051,
          "fee": "0.0020000000",
          "source": "SPOT",
          "amount": "0.00040000",
          "rebate_fee": "0.0004000000",
          "fee_asset": "BEAM",
          "currency_pair": "BEAM_USDT",
          "sub_broker_info": {
            "user_id": 110285114,
            "original_commission_rate": "0.2",
            "relative_commission_rate": "0.5",
            "commission_rate": "0.1"
          },
          "alpha_contract_addr": "0x9a26f5433671751c3276a065f57e5a02d2817973"
        }
      ],
      "total": 47
    }
    

##  经纪商获取用户的交易记录🔒 需要认证

GET`/rebate/broker/transaction_history`

GET `/rebate/broker/transaction_history`

_经纪商获取用户的交易记录_

记录查询时间范围不允许超过 30 天

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
user_id | 请求参数 | integer(int64) | 否 | 用户 ID，不指定则返回所有用户的记录  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间，不指定则默认从当前时间开始向前推 30 天  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | Inline  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» BrokerTransactionHistory | BrokerTransactionHistory |   
»» total | integer(int64) | 该查询下数据总数  
»» list | array | 交易列表  
»»» BrokerTransaction | object |   
»»»» transaction_time | integer(int64) | 交易时间，秒级 Unix 时间戳  
»»»» user_id | integer(int64) | 用户 ID  
»»»» group_name | string | 分组名称  
»»»» fee | string | 手续费数量 (usdt)  
»»»» currency_pair | string | 交易对  
»»»» amount | string | 交易金额数量  
»»»» fee_asset | string | 手续费币种  
»»»» source | string | 返佣交易类型：Spot、Futures、Options、Alpha、TradFi  
»»»» sub_broker_info | object | 子经纪商信息  
»»»»» user_id | integer(int64) | 子经纪商用户ID  
»»»»» original_commission_rate | string | 子经纪商原始返佣比例  
»»»»» relative_commission_rate | string | 子经纪商相对返佣比例  
»»»»» commission_rate | string | 子经纪商实际返佣比例  
»»»» alpha_contract_addr | string | Alpha合约地址  
  
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
    
    url = '/rebate/broker/transaction_history'
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
    url="/rebate/broker/transaction_history"
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
      "list": [
        {
          "user_id": 110285442,
          "group_name": "",
          "fee": "0.5000045000",
          "transaction_time": 1702545051,
          "amount": "-1000.00900000",
          "currency_pair": "DOGE_USDT",
          "source": "Futures",
          "fee_asset": "USDT",
          "sub_broker_info": {
            "user_id": 110285114,
            "original_commission_rate": "0.2",
            "relative_commission_rate": "0.5",
            "commission_rate": "0.1"
          },
          "alpha_contract_addr": "0x9a26f5433671751c3276a065f57e5a02d2817973"
        }
      ],
      "total": 47
    }
    

##  用户获取返佣信息🔒 需要认证

GET`/rebate/user/info`

GET `/rebate/user/info`

_用户获取返佣信息_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | Inline  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» _None_ | RebateUserInfo | 获取用户返佣信息  
»» invite_uid | integer(int64) | 我的邀请人UID  
  
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
    
    url = '/rebate/user/info'
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
    url="/rebate/user/info"
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
      "invite_uid": 987
    }
    

##  用户下级关系🔒 需要认证

GET`/rebate/user/sub_relation`

GET `/rebate/user/sub_relation`

_用户下级关系_

查询指定用户是否在体系内

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id_list | 请求参数 | string | 是 | 查询用户的ID列表，以,分割，超过100个则取100个  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | UserSubRelation  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» list | array | 下级关系列表  
»» UserSub | object |   
»»» uid | integer(int64) | 用户ID  
»»» belong | string | 用户所属体系(partner / referral)，为空表示不属于任何体系  
»»» type | integer(int64) | 类型(0-不在体系 1-直接下级代理 2-间接下级代理 3-直接直客 4-间接直客 5-普通用户)  
»»» ref_uid | integer(int64) | 邀请人用户ID  
  
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
    
    url = '/rebate/user/sub_relation'
    query_param = 'user_id_list=1, 2, 3'
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
    url="/rebate/user/sub_relation"
    query_param="user_id_list=1, 2, 3"
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
      "list": [
        {
          "belong": "",
          "ref_uid": 0,
          "type": 0,
          "uid": 9
        },
        {
          "belong": "partner",
          "type": 1,
          "ref_uid": 1,
          "uid": 2
        },
        {
          "belong": "referral",
          "type": 5,
          "ref_uid": 1,
          "uid": 3
        }
      ]
    }
    

##  获取最近的合伙人申请记录🔒 需要认证

GET`/rebate/partner/applications/recent`

GET `/rebate/partner/applications/recent`

_获取最近的合伙人申请记录_

获取当前用户最近的合伙人申请记录。

此接口返回用户最近 30 天内的申请记录，包括申请状态、审核信息、申请材料等详细信息。

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功响应 | Inline  
  
### 返回格式

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
    
    url = '/rebate/partner/applications/recent'
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
    url="/rebate/partner/applications/recent"
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

> 成功响应
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "id": 64779,
        "uid": 19669134,
        "language": "cn",
        "country_id": 37,
        "firstname": "交易员",
        "lastname": "",
        "email": "992937821@qq.com",
        "join_uid": 19669134,
        "join_country_id": 0,
        "identity_comment": "内容创作者",
        "promotion_channels": "19|15|1",
        "contact_details": "{\"4\":\"992937821\",\"2\":\"13169503913\"}",
        "know_details": "",
        "question_lang": "cn",
        "create_timest": "2026-03-16 02:22:28",
        "update_timest": "2026-03-16 02:22:28",
        "apply_type": 1,
        "audit_status": 0,
        "edit_counts": 1,
        "proof_images": "rebate/gateio/referral/apply_partner/69b76933b6583",
        "proof_videos": "",
        "proof_url": "https://mp.weixin.qq.com/s/zotzOCVoxKeukzM7hY4VWA",
        "audit_reason": 0,
        "channel_type": 3,
        "region": "cn",
        "phone": "13169503913",
        "telegram": "",
        "other_contact": {
          "type": 4,
          "value": "992937821"
        },
        "proof_images_url_list": [
          "https://gateio-service-private.gateio.services/rebate/gateio/referral/apply_partner/69b76933b6583?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&..."
        ],
        "proof_videos_url_list": [],
        "apply_msg": "您的代理申请已成功提交，正在审核中，我们将于 1-3 个工作日内完成审核并与您取得联系",
        "jump_url": "/referral/affiliate/program-application"
      },
      "timestamp": 1773637797
    }
    

##  检查合伙人申请资格🔒 需要认证

GET`/rebate/partner/eligibility`

GET `/rebate/partner/eligibility`

_检查合伙人申请资格_

检查当前用户是否有资格申请成为合伙人。

此接口会检查多个条件：

  * 账户状态（是否被封禁）
  * 是否为子账号
  * 是否已经是合伙人
  * KYC 认证状态
  * 是否在其他代理商的邀请链下
  * 是否在黑名单中
  * 其他业务规则限制

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功响应 | Inline  
  
### 返回格式

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
    
    url = '/rebate/partner/eligibility'
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
    url="/rebate/partner/eligibility"
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

> 成功响应
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "eligible": true,
        "block_reasons": [],
        "block_reason_codes": []
      },
      "timestamp": 1738886400
    }
    
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "eligible": false,
        "block_reasons": [
          "当前账号为子账号，请您切换至主账号完成申请。"
        ],
        "block_reason_codes": [
          "sub_account"
        ]
      },
      "timestamp": 1738886400
    }
    

##  代理数据聚合查询🔒 需要认证

GET`/rebate/partner/data/aggregated`

GET `/rebate/partner/data/aggregated`

_代理数据聚合查询_

查询指定时间范围内合伙人代理的数据聚合统计，包括返佣金额、交易量、净手续费、客户数和交易人数。

**注意事项：**

  * 交易人数 `trading_user_count` 仅在 `business_type=0`（全部）时返回
  * 时间参数使用 UTC+8 时区
  * 如不传时间参数，默认查询近 7 天数据
  * 仅限合伙人代理访问，子账号无权限

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
start_date | 请求参数 | string | 否 | 查询开始时间，格式：yyyy-mm-dd hh:ii:ss（UTC+8）  
  
不传时默认为近 7 日开始时间  
end_date | 请求参数 | string | 否 | 查询结束时间，格式：yyyy-mm-dd hh:ii:ss（UTC+8）  
  
不传时默认为近 7 日结束时间  
business_type | 请求参数 | integer | 否 | 业务类型筛选：  
\- 0: 全部（默认）  
\- 1: 现货  
\- 2: 合约  
\- 3: Alpha  
\- 4: Web3  
\- 5: Perps(DEX)  
\- 6: Exchange All  
\- 7: Web3 All  
\- 8: TradFi  
  
####  详细描述

**start_date** : 查询开始时间，格式：yyyy-mm-dd hh:ii:ss（UTC+8）  
  
不传时默认为近 7 日开始时间

**end_date** : 查询结束时间，格式：yyyy-mm-dd hh:ii:ss（UTC+8）  
  
不传时默认为近 7 日结束时间

**business_type** : 业务类型筛选：  
\- 0: 全部（默认）  
\- 1: 现货  
\- 2: 合约  
\- 3: Alpha  
\- 4: Web3  
\- 5: Perps(DEX)  
\- 6: Exchange All  
\- 7: Web3 All  
\- 8: TradFi

####  枚举值列表

枚举值列表参数 | 值  
---|---  
business_type | 0  
business_type | 1  
business_type | 2  
business_type | 3  
business_type | 4  
business_type | 5  
business_type | 6  
business_type | 7  
business_type | 8  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求参数错误 | ErrorResponse  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | 未授权访问 | ErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 访问被拒绝 | ErrorResponse  
  
### 返回格式

####  枚举值列表

枚举值列表属性 | 值  
---|---  
business_type | 0  
business_type | 1  
business_type | 2  
business_type | 3  
business_type | 4  
business_type | 5  
business_type | 6  
business_type | 7  
business_type | 8  
  
状态码 **400**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 错误码  
» message | string | 错误信息  
» data | object | 空对象  
» timestamp | integer(int64) | Unix 时间戳  
  
状态码 **401**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 错误码  
» message | string | 错误信息  
» data | object | 空对象  
» timestamp | integer(int64) | Unix 时间戳  
  
状态码 **403**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 错误码  
» message | string | 错误信息  
» data | object | 空对象  
» timestamp | integer(int64) | Unix 时间戳  
  
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
    
    url = '/rebate/partner/data/aggregated'
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
    url="/rebate/partner/data/aggregated"
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

> 查询成功
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "rebate_amount": "1234.567890",
        "trade_volume": "9876543.210000",
        "net_fee": "543.210000",
        "customer_count": 150,
        "trading_user_count": "85",
        "time_range_desc": "2024-01-01 ~ 2024-01-07",
        "business_type": 0,
        "business_type_desc": "全部"
      },
      "timestamp": 1738886400
    }
    
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "rebate_amount": "456.123000",
        "trade_volume": "2345678.900000",
        "net_fee": "234.560000",
        "customer_count": 75,
        "trading_user_count": null,
        "time_range_desc": "2024-01-01 ~ 2024-01-07",
        "business_type": 1,
        "business_type_desc": "现货"
      },
      "timestamp": 1738886400
    }
    

> 请求参数错误
    
    
    {
      "code": 400,
      "message": "Invalid time range parameter",
      "data": {},
      "timestamp": 1738886400
    }
    

> 未授权访问
    
    
    {
      "code": 401,
      "message": "Unauthorized",
      "data": {},
      "timestamp": 1738886400
    }
    

> 访问被拒绝
    
    
    {
      "code": 403,
      "message": "Sub-accounts are not allowed to access this API",
      "data": {},
      "timestamp": 1738886400
    }
    
    
    
    {
      "code": 403,
      "message": "Current account is not a partner agent",
      "data": {},
      "timestamp": 1738886400
    }
    

#  模型

##  PartnerCommissionHistory

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
total | integer(int64) | false | none | 该查询下数据总数  
list | array | false | none | 返佣列表  
» PartnerCommission | object | false | none | none  
»» commission_time | integer(int64) | false | none | 返佣时间，秒级 Unix 时间戳  
»» user_id | integer(int64) | false | none | 用户ID  
»» group_name | string | false | none | 分组名称  
»» commission_amount | string | false | none | 返佣金额数量  
»» commission_asset | string | false | none | 返佣金额币种  
»» source | string | false | none | 返佣交易类型, SPOT - 现货返佣, FUTURES - 合约返佣  
      
    
    {
      "total": 0,
      "list": [
        {
          "commission_time": 0,
          "user_id": 0,
          "group_name": "string",
          "commission_amount": "string",
          "commission_asset": "string",
          "source": "string"
        }
      ]
    }
    
    

##  PartnerSubList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
total | integer(int64) | false | none | 该查询下数据总数  
list | array | false | none | 下级列表  
» PartnerSub | object | false | none | none  
»» user_id | integer(int64) | false | none | 用户 ID  
»» user_join_time | integer(int64) | false | none | 用户加入体系的时间，秒级 Unix 时间戳  
»» type | integer(int64) | false | none | 类型(1-子代理 2-间接直客 3-直接直客)  
      
    
    {
      "total": 0,
      "list": [
        {
          "user_id": 0,
          "user_join_time": 0,
          "type": 0
        }
      ]
    }
    
    

##  UserSubRelation

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
list | array | false | none | 下级关系列表  
» UserSub | object | false | none | none  
»» uid | integer(int64) | false | none | 用户ID  
»» belong | string | false | none | 用户所属体系(partner / referral)，为空表示不属于任何体系  
»» type | integer(int64) | false | none | 类型(0-不在体系 1-直接下级代理 2-间接下级代理 3-直接直客 4-间接直客 5-普通用户)  
»» ref_uid | integer(int64) | false | none | 邀请人用户ID  
      
    
    {
      "list": [
        {
          "uid": 0,
          "belong": "string",
          "type": 0,
          "ref_uid": 0
        }
      ]
    }
    
    

##  AgencyCommissionHistory

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | false | none | 交易对  
total | integer(int64) | false | none | 该查询下数据总数  
list | array | false | none | 返佣列表  
» AgencyCommission | object | false | none | none  
»» commission_time | integer(int64) | false | none | 返佣时间，秒级 Unix 时间戳  
»» user_id | integer(int64) | false | none | 用户ID  
»» group_name | string | false | none | 分组名称  
»» commission_amount | string | false | none | 返佣金额数量  
»» commission_asset | string | false | none | 返佣金额币种  
»» source | string | false | none | 返佣交易类型, SPOT - 现货返佣, FUTURES - 合约返佣  
      
    
    {
      "currency_pair": "string",
      "total": 0,
      "list": [
        {
          "commission_time": 0,
          "user_id": 0,
          "group_name": "string",
          "commission_amount": "string",
          "commission_asset": "string",
          "source": "string"
        }
      ]
    }
    
    

##  ErrorResponse

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | 错误码  
message | string | true | none | 错误信息  
data | object | true | none | 空对象  
timestamp | integer(int64) | true | none | Unix 时间戳  
      
    
    {
      "code": 401,
      "message": "Unauthorized",
      "data": {},
      "timestamp": 1773637797
    }
    
    

##  AgencyTransactionHistory

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | false | none | 交易对  
total | integer(int64) | false | none | 该查询下数据总数  
list | array | false | none | 交易列表  
» AgencyTransaction | object | false | none | none  
»» transaction_time | integer(int64) | false | none | 交易时间，秒级 Unix 时间戳  
»» user_id | integer(int64) | false | none | 用户 ID  
»» group_name | string | false | none | 分组名称  
»» fee | string | false | none | 手续费数量  
»» fee_asset | string | false | none | 手续费币种  
»» currency_pair | string | false | none | 交易对  
»» amount | string | false | none | 交易金额数量  
»» amount_asset | string | false | none | 交易金额币种  
»» source | string | false | none | 返佣交易类型, SPOT - 现货返佣, FUTURES - 合约返佣  
      
    
    {
      "currency_pair": "string",
      "total": 0,
      "list": [
        {
          "transaction_time": 0,
          "user_id": 0,
          "group_name": "string",
          "fee": "string",
          "fee_asset": "string",
          "currency_pair": "string",
          "amount": "string",
          "amount_asset": "string",
          "source": "string"
        }
      ]
    }
    
    

##  BrokerTransactionHistory

_BrokerTransactionHistory_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
total | integer(int64) | false | none | 该查询下数据总数  
list | array | false | none | 交易列表  
» BrokerTransaction | object | false | none | none  
»» transaction_time | integer(int64) | false | none | 交易时间，秒级 Unix 时间戳  
»» user_id | integer(int64) | false | none | 用户 ID  
»» group_name | string | false | none | 分组名称  
»» fee | string | false | none | 手续费数量 (usdt)  
»» currency_pair | string | false | none | 交易对  
»» amount | string | false | none | 交易金额数量  
»» fee_asset | string | false | none | 手续费币种  
»» source | string | false | none | 返佣交易类型：Spot、Futures、Options、Alpha、TradFi  
»» sub_broker_info | object | false | none | 子经纪商信息  
»»» user_id | integer(int64) | false | none | 子经纪商用户ID  
»»» original_commission_rate | string | false | none | 子经纪商原始返佣比例  
»»» relative_commission_rate | string | false | none | 子经纪商相对返佣比例  
»»» commission_rate | string | false | none | 子经纪商实际返佣比例  
»» alpha_contract_addr | string | false | none | Alpha合约地址  
      
    
    {
      "total": 0,
      "list": [
        {
          "transaction_time": 0,
          "user_id": 0,
          "group_name": "string",
          "fee": "string",
          "currency_pair": "string",
          "amount": "string",
          "fee_asset": "string",
          "source": "string",
          "sub_broker_info": {},
          "alpha_contract_addr": "string"
        }
      ]
    }
    
    

##  PartnerTransactionHistory

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
total | integer(int64) | false | none | 该查询下数据总数  
list | array | false | none | 交易列表  
» PartnerTransaction | object | false | none | none  
»» transaction_time | integer(int64) | false | none | 交易时间，秒级 Unix 时间戳  
»» user_id | integer(int64) | false | none | 用户 ID  
»» group_name | string | false | none | 分组名称  
»» fee | string | false | none | 手续费数量  
»» fee_asset | string | false | none | 手续费币种  
»» currency_pair | string | false | none | 交易对  
»» amount | string | false | none | 交易金额数量  
»» amount_asset | string | false | none | 交易金额币种  
»» source | string | false | none | 返佣交易类型, SPOT - 现货返佣, FUTURES - 合约返佣  
      
    
    {
      "total": 0,
      "list": [
        {
          "transaction_time": 0,
          "user_id": 0,
          "group_name": "string",
          "fee": "string",
          "fee_asset": "string",
          "currency_pair": "string",
          "amount": "string",
          "amount_asset": "string",
          "source": "string"
        }
      ]
    }
    
    

##  PartnerApplicationResponse

###  属性

_allOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
» code | integer | true | none | 错误码，0 表示成功  
» message | string | true | none | 错误信息描述  
» data | object | true | none | 响应数据  
» timestamp | integer(int64) | true | none | Unix 时间戳  
  
_and_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
» data | object | false | none | none  
»» id | integer | false | none | 申请记录 ID  
»» uid | integer | false | none | 用户 ID  
»» language | string | false | none | 语言代码  
»» country_id | integer | false | none | 国家 ID  
»» firstname | string | false | none | 名  
»» lastname | string | false | none | 姓  
»» email | string(email) | false | none | 邮箱地址  
»» join_uid | integer | false | none | 加入的用户 ID  
»» join_country_id | integer | false | none | 加入的国家 ID  
»» identity_comment | string | false | none | 身份说明  
»» promotion_channels | string | false | none | 推广渠道，多个渠道用  
»» contact_details | string | false | none | 联系方式详情（JSON 字符串）  
»» know_details | string | false | none | 了解详情  
»» question_lang | string | false | none | 问题语言  
»» create_timest | string(date-time) | false | none | 创建时间  
»» update_timest | string(date-time) | false | none | 更新时间  
»» apply_type | integer | false | none | 申请类型  
»» audit_status | integer | false | none | 审核状态（0-待审核，1-通过，2-拒绝）  
»» edit_counts | integer | false | none | 编辑次数  
»» proof_images | string | false | none | 证明图片路径  
»» proof_videos | string | false | none | 证明视频路径  
»» proof_url | string(uri) | false | none | 证明链接  
»» audit_reason | integer | false | none | 审核原因代码  
»» channel_type | integer | false | none | 渠道类型  
»» region | string | false | none | 地区  
»» phone | string | false | none | 电话号码  
»» telegram | string | false | none | Telegram 账号  
»» other_contact | object | false | none | 其他联系方式  
»»» type | integer | false | none | 联系方式类型  
»»» value | string | false | none | 联系方式值  
»» proof_images_url_list | array | false | none | 证明图片 URL 列表  
»» proof_videos_url_list | array | false | none | 证明视频 URL 列表  
»» apply_msg | string | false | none | 申请消息  
»» jump_url | string | false | none | 跳转 URL  
      
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "id": 64779,
        "uid": 19669134,
        "language": "cn",
        "country_id": 37,
        "firstname": "交易员",
        "lastname": "",
        "email": "992937821@qq.com",
        "join_uid": 19669134,
        "join_country_id": 0,
        "identity_comment": "内容创作者",
        "promotion_channels": "19|15|1",
        "contact_details": "{\"4\":\"992937821\",\"2\":\"13169503913\"}",
        "know_details": "",
        "question_lang": "cn",
        "create_timest": "2026-03-16 02:22:28",
        "update_timest": "2026-03-16 02:22:28",
        "apply_type": 1,
        "audit_status": 0,
        "edit_counts": 1,
        "proof_images": "rebate/gateio/referral/apply_partner/69b76933b6583",
        "proof_videos": "",
        "proof_url": "https://mp.weixin.qq.com/s/zotzOCVoxKeukzM7hY4VWA",
        "audit_reason": 0,
        "channel_type": 3,
        "region": "cn",
        "phone": "13169503913",
        "telegram": "",
        "other_contact": {
          "type": 4,
          "value": "992937821"
        },
        "proof_images_url_list": [
          "https://gateio-service-private.gateio.services/rebate/gateio/referral/apply_partner/69b76933b6583?..."
        ],
        "proof_videos_url_list": [],
        "apply_msg": "您的代理申请已成功提交，正在审核中，我们将于 1-3 个工作日内完成审核并与您取得联系",
        "jump_url": "/referral/affiliate/program-application"
      },
      "timestamp": 1773637797
    }
    
    

##  BrokerCommission

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
total | integer(int64) | false | none | 该查询下数据总数  
list | array | false | none | 返佣列表  
» BrokerCommissionItem | object | false | none | none  
»» commission_time | integer(int64) | false | none | 返佣时间，秒级 Unix 时间戳  
»» user_id | integer(int64) | false | none | 用户ID  
»» group_name | string | false | none | 分组名称  
»» amount | string | false | none | 返佣金额  
»» fee | string | false | none | 手续费数量  
»» fee_asset | string | false | none | 手续费币种  
»» rebate_fee | string | false | none | 折算为USDT后返还收入  
»» source | string | false | none | 返佣交易类型：Spot、Futures、Options、Alpha、TradFi  
»» currency_pair | string | false | none | 交易对  
»» sub_broker_info | object | false | none | 子经纪商信息  
»»» user_id | integer(int64) | false | none | 子经纪商用户ID  
»»» original_commission_rate | string | false | none | 子经纪商原始返佣比例  
»»» relative_commission_rate | string | false | none | 子经纪商相对返佣比例  
»»» commission_rate | string | false | none | 子经纪商实际返佣比例  
»» alpha_contract_addr | string | false | none | Alpha合约地址  
      
    
    {
      "total": 0,
      "list": [
        {
          "commission_time": 0,
          "user_id": 0,
          "group_name": "string",
          "amount": "string",
          "fee": "string",
          "fee_asset": "string",
          "rebate_fee": "string",
          "source": "string",
          "currency_pair": "string",
          "sub_broker_info": {},
          "alpha_contract_addr": "string"
        }
      ]
    }
    
    

##  RebateUserInfo

_获取用户返佣信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
invite_uid | integer(int64) | false | none | 我的邀请人UID  
      
    
    {
      "invite_uid": 0
    }
    
    

##  PartnerDataAggregatedResponse

###  属性

_allOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | PartnerApplicationResponse/allOf/0 | false | none | none  
  
_and_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
» data | object | false | none | none  
»» rebate_amount | string | true | none | 返佣金额，字符串格式保证精度  
  
最多保留 6 位小数，去除尾零  
»» trade_volume | string | true | none | 交易量，字符串格式保证精度  
  
最多保留 6 位小数，去除尾零  
»» net_fee | string | true | none | 净手续费，字符串格式保证精度  
  
最多保留 6 位小数，去除尾零  
»» customer_count | integer | true | none | 客户数（邀请人数）  
»» trading_user_count | string|null | true | none | 交易人数，字符串形式（与线上 JSON 序列化一致）  
  
仅在 business_type=0（全部）时返回具体数值，其他业务类型返回 null  
»» time_range_desc | string | true | none | 时间范围描述  
»» business_type | integer | true | none | 业务类型  
»» business_type_desc | string | true | none | 业务类型描述，可取值：全部, 现货, 合约, Alpha, Web3, Perps(DEX), Exchange All, Web3 All, TradFi  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
business_type | 0  
business_type | 1  
business_type | 2  
business_type | 3  
business_type | 4  
business_type | 5  
business_type | 6  
business_type | 7  
business_type | 8  
      
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "rebate_amount": "1234.567890",
        "trade_volume": "9876543.210000",
        "net_fee": "543.210000",
        "customer_count": 150,
        "trading_user_count": "85",
        "time_range_desc": "2024-01-01 ~ 2024-01-07",
        "business_type": 0,
        "business_type_desc": "全部"
      },
      "timestamp": 1773637797
    }
    
    

##  EligibilityResponse

###  属性

_allOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | PartnerApplicationResponse/allOf/0 | false | none | none  
  
_and_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
» data | object | false | none | none  
»» eligible | boolean | true | none | 是否符合申请资格  
»» block_reasons | array | true | none | 不符合资格的原因描述列表  
»» block_reason_codes | array | true | none | 不符合资格的原因代码列表  
      
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "eligible": false,
        "block_reasons": [
          "当前账号为子账号，请您切换至主账号完成申请。"
        ],
        "block_reason_codes": [
          "sub_account"
        ]
      },
      "timestamp": 1773637797
    }