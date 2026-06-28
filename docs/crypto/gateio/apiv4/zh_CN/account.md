---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/account
api_type: Account
updated_at: 2026-05-27 20:16:46.153964
---

# Account

获取用户账户信息

##  获取用户账户信息🔒 需要认证

GET`/account/detail`

GET `/account/detail`

_获取用户账户信息_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | AccountDetail  
  
### 返回格式

状态码 **200**

_AccountDetail_

名称 | 类型 | 描述  
---|---|---  
» ip_whitelist | array | IP 白名单  
» currency_pairs | array | 交易对白名单  
» user_id | integer(int64) | 用户ID  
» tier | integer(int64) | 用户 vip 等级  
» key | object | API Key 详情  
»» mode | integer(int32) | 模式： 1 - 经典模式 2 - 旧版统一模式  
» copy_trading_role | integer(int32) | 用户角色： 0 - 普通用户 1 - 带单者 2 - 跟单者 3 - 带单者与跟单者  
  
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
    
    url = '/account/detail'
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
    url="/account/detail"
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
      "user_id": 1667201533,
      "ip_whitelist": [
        "127.0.0.1"
      ],
      "currency_pairs": [
        "USDT_BTC"
      ],
      "key": {
        "mode": 1
      },
      "tier": 2,
      "copy_trading_role": 1
    }
    

##  查询主账户下的全部Key信息🔒 需要认证

GET`/account/main_keys`

GET `/account/main_keys`

_查询主账户下的全部Key信息_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | AccountKeyInfo  
  
### 返回格式

状态码 **200**

_AccountKeyInfo_

名称 | 类型 | 描述  
---|---|---  
» state | integer(int32) | apikey状态： 1 - 正常状态 2 - 锁定状态 3 - 冻结状态(只能修改，创建默认为1）  
» mode | integer(int32) | 用户模式： 1 - 经典模式 2 - 旧版统一模式 (只能创建时指定，不能修改）  
» name | string | api key 备注  
» currency_pairs | array | 交易对白名单列表，最多 30 个交易对  
» user_id | integer(int64) | 用户ID  
» ip_whitelist | array | IP 白名单  
» perms | array |   
»» name | string | 权限功能名称（不传值即为清空）  
  
\- `wallet`: 钱包  
\- `spot`: 现货/杠杆  
\- `futures`: 永续合约  
\- `delivery`: 交割合约  
\- `earn`: 理财  
\- `custody`: 托管  
\- `options`: 期权  
\- `account`: 账户信息  
\- `loan`: 借贷  
\- `margin`: 杠杆  
\- `unified`: 统一账户  
\- `copy`: 跟单  
\- `pilot`: 创新  
\- `otc`: otc  
\- `alpha`: alpha  
\- `crossx`: 跨所  
»» read_only | boolean | 该功能是否只读  
» key | object | API Key 详情  
»» mode | integer(int32) | 模式： 1 - 经典模式 2 - 旧版统一模式  
» created_at | string | 创建时间  
» updated_at | string | 最近更新时间  
» last_access | string | 最近使用时间  
  
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
    
    url = '/account/main_keys'
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
    url="/account/main_keys"
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
        "state": 1,
        "mode": 1,
        "name": "test1",
        "user_id": 1,
        "perms": [
          {
            "name": "account",
            "read_only": false
          },
          {
            "name": "spot",
            "read_only": false
          }
        ],
        "ip_whitelist": [],
        "currency_pairs": [
          "BTC_USD",
          "ETH_USD"
        ],
        "key": "c5dcfbf1f3a7*****",
        "created_at": 1753030929,
        "update_at": 1756300567,
        "last_access": 1753030929
      },
      {
        "state": 1,
        "mode": 1,
        "name": "test2",
        "user_id": 1,
        "perms": [
          {
            "name": "spot",
            "read_only": false
          },
          {
            "name": "account",
            "read_only": false
          }
        ],
        "ip_whitelist": [],
        "currency_pairs": [
          "BTC_USD",
          "ETH_USD"
        ],
        "key": "52fd0035f665*****",
        "created_at": 1753897991,
        "update_at": 1756300567,
        "last_access": 1753897991
      }
    ]
    

##  获取用户成交比率限频信息🔒 需要认证

GET`/account/rate_limit`

GET `/account/rate_limit`

_获取用户成交比率限频信息_

该接口暂未开放使用

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | [AccountRateLimit]  
  
### 返回格式

状态码 **200**

_AccountRateLimit_

名称 | 类型 | 描述  
---|---|---  
AccountRateLimit | array | 账户限流  
» tier | string | 限频等级（详细限频规则查看成交比率限频）  
» ratio | string | 成交率  
» main_ratio | string | 主账户合计成交比率  
» updated_at | string | 更新时间  
  
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
    
    url = '/account/rate_limit'
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
    url="/account/rate_limit"
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
        "type": "spot",
        "tier": "1",
        "ratio": "0",
        "main_ratio": "0",
        "updated_at": "1728230400"
      },
      {
        "type": "futures",
        "tier": "1",
        "ratio": "0",
        "main_ratio": "0",
        "updated_at": "1728230400"
      }
    ]
    

##  查询用户创建的STP用户组🔒 需要认证

GET`/account/stp_groups`

GET `/account/stp_groups`

_查询用户创建的STP用户组_

只查询当前主账号用户新建的 STP 用户组列表

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
name | 请求参数 | string | 否 | 根据名称模糊查询  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [StpGroup]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | integer(int64) | STP用户组ID  
» name | string | STP用户组名称  
» creator_id | integer(int64) | 创建人账户ID  
» create_time | integer(int64) | 创建时间  
  
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
    
    url = '/account/stp_groups'
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
    url="/account/stp_groups"
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
        "id": 123435,
        "name": "group",
        "create_time": 1548000000,
        "creator_id": 10000
      }
    ]
    

##  新建STP用户组🔒 需要认证

POST`/account/stp_groups`

POST `/account/stp_groups`

_新建STP用户组_

只允许用户主账号新建STP用户组

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | StpGroup | 是 |   
» id | body | integer(int64) | 否 | STP用户组ID  
» name | body | string | 是 | STP用户组名称  
» creator_id | body | integer(int64) | 否 | 创建人账户ID  
» create_time | body | integer(int64) | 否 | 创建时间  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 添加用户成功，返回当前STP组内用户 | StpGroup  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | STP用户组ID  
» name | string | STP用户组名称  
» creator_id | integer(int64) | 创建人账户ID  
» create_time | integer(int64) | 创建时间  
  
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
    
    url = '/account/stp_groups'
    query_param = ''
    body='{"name":"stp_name"}'
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
    url="/account/stp_groups"
    query_param=""
    body_param='{"name":"stp_name"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "name": "stp_name"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": 123435,
      "name": "group",
      "create_time": 1548000000,
      "creator_id": 10000
    }
    

##  查询STP用户组中的用户🔒 需要认证

GET`/account/stp_groups/{stp_id}/users`

GET `/account/stp_groups/{stp_id}/users`

_查询STP用户组中的用户_

只允许创建此STP组的主账户查询当前STP组的账户ID列表

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
stp_id | URL | integer(int64) | 是 | STP用户组ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [StpGroupUser]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» user_id | integer(int64) | 用户ID  
» stp_id | integer(int64) | STP用户组ID  
» create_time | integer(int64) | 创建时间  
  
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
    
    url = '/account/stp_groups/1/users'
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
    url="/account/stp_groups/1/users"
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
        "user_id": 10000,
        "stp_id": 1,
        "create_time": 1548000000
      }
    ]
    

##  STP用户组中添加用户🔒 需要认证

POST`/account/stp_groups/{stp_id}/users`

POST `/account/stp_groups/{stp_id}/users`

_STP用户组中添加用户_

  * 只允许创建此STP组的主账号添加STP用户组用户
  * 只允许添加当前主账户下的账户，不允许跨主账户

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
stp_id | URL | integer(int64) | 是 | STP用户组ID  
body | body | AddSTPGroupUsersRequest | 是 | 用户ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 添加用户成功，返回当前STP组内用户 | [StpGroupUser]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» user_id | integer(int64) | 用户ID  
» stp_id | integer(int64) | STP用户组ID  
» create_time | integer(int64) | 创建时间  
  
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
    
    url = '/account/stp_groups/1/users'
    query_param = ''
    body='[1,2,3]'
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
    url="/account/stp_groups/1/users"
    query_param=""
    body_param='[1,2,3]'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    [
      1,
      2,
      3
    ]
    

> 返回示例

> 200 返回
    
    
    [
      {
        "user_id": 10000,
        "stp_id": 1,
        "create_time": 1548000000
      }
    ]
    

##  STP用户组中删除用户🔒 需要认证

DELETE`/account/stp_groups/{stp_id}/users`

DELETE `/account/stp_groups/{stp_id}/users`

_STP用户组中删除用户_

  * 只允许创建此STP组的主账号删除STP用户组用户
  * 只允许删除当前主账户下的账户，不允许跨主账户

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
stp_id | URL | integer(int64) | 是 | STP用户组ID  
user_id | 请求参数 | integer(int64) | 是 | STP用户ID，多个可以用逗号隔开  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 删除用户成功，返回当前STP组内用户 | [StpGroupUser]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» user_id | integer(int64) | 用户ID  
» stp_id | integer(int64) | STP用户组ID  
» create_time | integer(int64) | 创建时间  
  
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
    
    url = '/account/stp_groups/1/users'
    query_param = 'user_id=1'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/account/stp_groups/1/users"
    query_param="user_id=1"
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
        "user_id": 10000,
        "stp_id": 1,
        "create_time": 1548000000
      }
    ]
    

##  查询GT抵扣配置🔒 需要认证

GET`/account/debit_fee`

GET `/account/debit_fee`

_查询GT抵扣配置_

查询当前帐户的GT抵扣配置

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | DebitFee  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» enabled | boolean | 是否开启GT抵扣  
  
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
    
    url = '/account/debit_fee'
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
    url="/account/debit_fee"
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
      "enabled": true
    }
    

##  设定GT抵扣🔒 需要认证

POST`/account/debit_fee`

POST `/account/debit_fee`

_设定GT抵扣_

开启或关闭当前帐户的GT抵扣

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | DebitFee | 是 |   
» enabled | body | boolean | 是 | 是否开启GT抵扣  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | 无  
  
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
    
    url = '/account/debit_fee'
    query_param = ''
    body='{"enabled":true}'
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
    url="/account/debit_fee"
    query_param=""
    body_param='{"enabled":true}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "enabled": true
    }
    

#  模型

##  StpGroup

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | STP用户组ID  
name | string | true | none | STP用户组名称  
creator_id | integer(int64) | false | none | 创建人账户ID  
create_time | integer(int64) | false | none | 创建时间  
      
    
    {
      "id": 0,
      "name": "string",
      "creator_id": 0,
      "create_time": 0
    }
    
    

##  AccountKeyInfo

_AccountKeyInfo_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
state | integer(int32) | false | none | apikey状态： 1 - 正常状态 2 - 锁定状态 3 - 冻结状态(只能修改，创建默认为1）  
mode | integer(int32) | false | none | 用户模式： 1 - 经典模式 2 - 旧版统一模式 (只能创建时指定，不能修改）  
name | string | false | none | api key 备注  
currency_pairs | array | false | none | 交易对白名单列表，最多 30 个交易对  
user_id | integer(int64) | false | none | 用户ID  
ip_whitelist | array | false | none | IP 白名单  
perms | array | false | none | none  
» name | string | false | none | 权限功能名称（不传值即为清空）  
  
\- `wallet`: 钱包  
\- `spot`: 现货/杠杆  
\- `futures`: 永续合约  
\- `delivery`: 交割合约  
\- `earn`: 理财  
\- `custody`: 托管  
\- `options`: 期权  
\- `account`: 账户信息  
\- `loan`: 借贷  
\- `margin`: 杠杆  
\- `unified`: 统一账户  
\- `copy`: 跟单  
\- `pilot`: 创新  
\- `otc`: otc  
\- `alpha`: alpha  
\- `crossx`: 跨所  
» read_only | boolean | false | none | 该功能是否只读  
key | object | false | none | API Key 详情  
» mode | integer(int32) | false | none | 模式： 1 - 经典模式 2 - 旧版统一模式  
created_at | string | false | 只读 | 创建时间  
updated_at | string | false | 只读 | 最近更新时间  
last_access | string | false | 只读 | 最近使用时间  
      
    
    {
      "state": 0,
      "mode": 0,
      "name": "string",
      "currency_pairs": [
        "string"
      ],
      "user_id": 0,
      "ip_whitelist": [
        "string"
      ],
      "perms": [
        {
          "name": "string",
          "read_only": true
        }
      ],
      "key": {
        "mode": 0
      },
      "created_at": "string",
      "updated_at": "string",
      "last_access": "string"
    }
    
    

##  AccountDetail

_AccountDetail_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
ip_whitelist | array | false | none | IP 白名单  
currency_pairs | array | false | none | 交易对白名单  
user_id | integer(int64) | false | none | 用户ID  
tier | integer(int64) | false | none | 用户 vip 等级  
key | object | false | none | API Key 详情  
» mode | integer(int32) | false | none | 模式： 1 - 经典模式 2 - 旧版统一模式  
copy_trading_role | integer(int32) | false | none | 用户角色： 0 - 普通用户 1 - 带单者 2 - 跟单者 3 - 带单者与跟单者  
      
    
    {
      "ip_whitelist": [
        "string"
      ],
      "currency_pairs": [
        "string"
      ],
      "user_id": 0,
      "tier": 0,
      "key": {
        "mode": 0
      },
      "copy_trading_role": 0
    }
    
    

##  AccountRateLimit

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
tier | string | false | none | 限频等级（详细限频规则查看成交比率限频）  
ratio | string | false | none | 成交率  
main_ratio | string | false | none | 主账户合计成交比率  
updated_at | string | false | none | 更新时间  
      
    
    {
      "tier": "string",
      "ratio": "string",
      "main_ratio": "string",
      "updated_at": "string"
    }
    
    

##  StpGroupUser

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user_id | integer(int64) | false | none | 用户ID  
stp_id | integer(int64) | false | none | STP用户组ID  
create_time | integer(int64) | false | none | 创建时间  
      
    
    {
      "user_id": 0,
      "stp_id": 0,
      "create_time": 0
    }
    
    

##  DebitFee

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
enabled | boolean | true | none | 是否开启GT抵扣  
      
    
    {
      "enabled": true
    }
    
    

##  AddSTPGroupUsersRequest

###  属性

_无_
    
    
    [
      0
    ]