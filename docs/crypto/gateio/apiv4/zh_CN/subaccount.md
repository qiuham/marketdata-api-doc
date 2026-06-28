---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/subaccount
api_type: Account
updated_at: 2026-05-27 20:17:55.276874
---

# SubAccount

子账户管理

##  获取子账户列表🔒 需要认证

GET`/sub_accounts`

GET `/sub_accounts`

_获取子账户列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
type | 请求参数 | string | 否 | 输入 0 则列出所有类型子账户（目前支持全仓杠杆子账户和普通子账户）输入1查询普通子账户,如果不传默认只查询普通子账户。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [SubAccount]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» remark | string | 备注  
» login_name | string | 子账户登录名：仅支持字母、数字、下划线，不可包含其他非法字符。  
» password | string | 子账户密码  
不传默认跟随主账户  
» email | string | 子账户邮箱  
不传默认跟随主账户  
» state | integer(int32) | 子账户状态 1正常,2冻结  
» type | integer(int32) | 子账号类型 1-普通子账号 3-全仓杠杆子账户  
» user_id | integer(int64) | 子账户 user_id  
» create_time | integer(int64) | 创建时间戳  
  
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
    
    url = '/sub_accounts'
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
    url="/sub_accounts"
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
        "remark": "remark",
        "login_name": "sub_account_for_trades",
        "user_id": 10001,
        "state": 1,
        "create_time": 168888888
      }
    ]
    

##  创建新的子账户🔒 需要认证

POST`/sub_accounts`

POST `/sub_accounts`

_创建新的子账户_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | SubAccount | 是 |   
» remark | body | string | 否 | 备注  
» login_name | body | string | 是 | 子账户登录名：仅支持字母、数字、下划线，不可包含其他非法字符。  
» password | body | string | 否 | 子账户密码  
不传默认跟随主账户  
» email | body | string | 否 | 子账户邮箱  
不传默认跟随主账户  
  
####  详细描述

**» password** : 子账户密码  
不传默认跟随主账户

**» email** : 子账户邮箱  
不传默认跟随主账户

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 创建成功 | SubAccount  
  
### 返回格式

状态码 **201**

名称 | 类型 | 描述  
---|---|---  
» remark | string | 备注  
» login_name | string | 子账户登录名：仅支持字母、数字、下划线，不可包含其他非法字符。  
» password | string | 子账户密码  
不传默认跟随主账户  
» email | string | 子账户邮箱  
不传默认跟随主账户  
» state | integer(int32) | 子账户状态 1正常,2冻结  
» type | integer(int32) | 子账号类型 1-普通子账号 3-全仓杠杆子账户  
» user_id | integer(int64) | 子账户 user_id  
» create_time | integer(int64) | 创建时间戳  
  
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
    
    url = '/sub_accounts'
    query_param = ''
    body='{"remark":"remark","login_name":"sub_account_for_trades"}'
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
    url="/sub_accounts"
    query_param=""
    body_param='{"remark":"remark","login_name":"sub_account_for_trades"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "remark": "remark",
      "login_name": "sub_account_for_trades"
    }
    

> 返回示例

> 201 返回
    
    
    {
      "remark": "remark",
      "login_name": "sub_account_for_trades",
      "user_id": 10001,
      "state": 1,
      "create_time": 168888888
    }
    

##  获取子账户🔒 需要认证

GET`/sub_accounts/{user_id}`

GET `/sub_accounts/{user_id}`

_获取子账户_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id | URL | integer(int64) | 是 | 子账户 UserID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | SubAccount  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» remark | string | 备注  
» login_name | string | 子账户登录名：仅支持字母、数字、下划线，不可包含其他非法字符。  
» password | string | 子账户密码  
不传默认跟随主账户  
» email | string | 子账户邮箱  
不传默认跟随主账户  
» state | integer(int32) | 子账户状态 1正常,2冻结  
» type | integer(int32) | 子账号类型 1-普通子账号 3-全仓杠杆子账户  
» user_id | integer(int64) | 子账户 user_id  
» create_time | integer(int64) | 创建时间戳  
  
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
    
    url = '/sub_accounts/0'
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
    url="/sub_accounts/0"
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
      "remark": "remark",
      "login_name": "sub_account_for_trades",
      "user_id": 10001,
      "state": 1,
      "create_time": 168888888
    }
    

##  获取子账户所有密钥对🔒 需要认证

GET`/sub_accounts/{user_id}/keys`

GET `/sub_accounts/{user_id}/keys`

_获取子账户所有密钥对_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id | URL | integer | 是 | 子账户 UserID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [SubAccountKey]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» user_id | integer(int64) | 用户ID  
» mode | integer(int32) | 模式 1 - 经典帐户 2 - 统一账户  
» name | string | API Key名称  
» perms | array |   
»» name | string | 权限功能名称（不传值即为清空）  
\- wallet: 钱包  
\- spot: 现货/杠杆  
\- futures: 永续合约  
\- delivery: 交割合约  
\- earn: 理财  
\- custody: 托管  
\- options: 期权  
\- account: 账户信息  
\- loan: 借贷  
\- margin: 杠杆  
\- unified: 统一账户  
\- copy: 跟单  
»» read_only | boolean | 该功能是否只读  
» ip_whitelist | array | IP白名单列表（不传值即为清空）  
» key | string | API Key  
» state | integer(int32) | 状态 1 - 正常 2 - 冻结 3 - 锁定  
» created_at | integer(int64) | 创建时间  
» updated_at | integer(int64) | 最近更新时间  
» last_access | integer(int64) | 最近使用时间  
  
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
    
    url = '/sub_accounts/0/keys'
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
    url="/sub_accounts/0/keys"
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
        "name": "spot",
        "user_id": 1000000,
        "perms": [
          {
            "name": "futures",
            "read_only": false
          },
          {
            "name": "wallet",
            "read_only": false
          },
          {
            "name": "delivery",
            "read_only": false
          },
          {
            "name": "options",
            "read_only": false
          },
          {
            "name": "spot",
            "read_only": false
          }
        ],
        "mode": 1,
        "ip_whitelist": [
          "127.0.0.1",
          "127.0.0.2"
        ],
        "key": "75c3264105b74693d8cb5c7f1a8e2420",
        "created_at": 1663642892,
        "last_access": 1663642892,
        "update_at": 1663642892
      }
    ]
    

##  创建新的子账户 API 密钥对🔒 需要认证

POST`/sub_accounts/{user_id}/keys`

POST `/sub_accounts/{user_id}/keys`

_创建新的子账户 API 密钥对_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id | URL | integer(int64) | 是 | 子账户 UserID  
body | body | SubAccountKey | 是 |   
» mode | body | integer(int32) | 否 | 模式 1 - 经典帐户 2 - 统一账户  
» name | body | string | 否 | API Key名称  
» perms | body | array | 否 |   
»» name | body | string | 否 | 权限功能名称（不传值即为清空）  
\- wallet: 钱包  
\- spot: 现货/杠杆  
\- futures: 永续合约  
\- delivery: 交割合约  
\- earn: 理财  
\- custody: 托管  
\- options: 期权  
\- account: 账户信息  
\- loan: 借贷  
\- margin: 杠杆  
\- unified: 统一账户  
\- copy: 跟单  
»» read_only | body | boolean | 否 | 该功能是否只读  
» ip_whitelist | body | array | 否 | IP白名单列表（不传值即为清空）  
  
####  详细描述

**»» name** : 权限功能名称（不传值即为清空）  
\- wallet: 钱包  
\- spot: 现货/杠杆  
\- futures: 永续合约  
\- delivery: 交割合约  
\- earn: 理财  
\- custody: 托管  
\- options: 期权  
\- account: 账户信息  
\- loan: 借贷  
\- margin: 杠杆  
\- unified: 统一账户  
\- copy: 跟单

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 创建成功 | SubAccountKey  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» user_id | integer(int64) | 用户ID  
» mode | integer(int32) | 模式 1 - 经典帐户 2 - 统一账户  
» name | string | API Key名称  
» perms | array |   
»» name | string | 权限功能名称（不传值即为清空）  
\- wallet: 钱包  
\- spot: 现货/杠杆  
\- futures: 永续合约  
\- delivery: 交割合约  
\- earn: 理财  
\- custody: 托管  
\- options: 期权  
\- account: 账户信息  
\- loan: 借贷  
\- margin: 杠杆  
\- unified: 统一账户  
\- copy: 跟单  
»» read_only | boolean | 该功能是否只读  
» ip_whitelist | array | IP白名单列表（不传值即为清空）  
» key | string | API Key  
» state | integer(int32) | 状态 1 - 正常 2 - 冻结 3 - 锁定  
» created_at | integer(int64) | 创建时间  
» updated_at | integer(int64) | 最近更新时间  
» last_access | integer(int64) | 最近使用时间  
  
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
    
    url = '/sub_accounts/0/keys'
    query_param = ''
    body='{"mode":1,"name":"spot","perms":[{"read_only":false,"name":"options"},{"read_only":false,"name":"spot"},{"read_only":false,"name":"delivery"},{"read_only":false,"name":"wallet"},{"read_only":false,"name":"futures"}],"ip_whitelist":["127.0.0.1","127.0.0.2"]}'
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
    url="/sub_accounts/0/keys"
    query_param=""
    body_param='{"mode":1,"name":"spot","perms":[{"read_only":false,"name":"options"},{"read_only":false,"name":"spot"},{"read_only":false,"name":"delivery"},{"read_only":false,"name":"wallet"},{"read_only":false,"name":"futures"}],"ip_whitelist":["127.0.0.1","127.0.0.2"]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "mode": 1,
      "name": "spot",
      "perms": [
        {
          "read_only": false,
          "name": "options"
        },
        {
          "read_only": false,
          "name": "spot"
        },
        {
          "read_only": false,
          "name": "delivery"
        },
        {
          "read_only": false,
          "name": "wallet"
        },
        {
          "read_only": false,
          "name": "futures"
        }
      ],
      "ip_whitelist": [
        "127.0.0.1",
        "127.0.0.2"
      ]
    }
    

> 返回示例

> 200 返回
    
    
    {
      "state": 1,
      "name": "spot",
      "user_id": 100000,
      "perms": [
        {
          "name": "options",
          "read_only": false
        },
        {
          "name": "spot",
          "read_only": false
        },
        {
          "name": "delivery",
          "read_only": false
        },
        {
          "name": "wallet",
          "read_only": false
        },
        {
          "name": "futures",
          "read_only": false
        }
      ],
      "ip_whitelist": [
        "127.0.0.1",
        "127.0.0.2"
      ],
      "mode": 1,
      "secret": "cddcc6e5e78060e013860bdbe5e737830b96821c027664586fb38b411808f4fd",
      "key": "eb8815bf99d7bb5f8ad6497bdc4774a8",
      "created_at": 1663683330,
      "updated_at": 1663683330
    }
    

##  获取子账户 API 特定密钥对🔒 需要认证

GET`/sub_accounts/{user_id}/keys/{key}`

GET `/sub_accounts/{user_id}/keys/{key}`

_获取子账户 API 特定密钥对_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id | URL | integer | 是 | 子账户 UserID  
key | URL | string | 是 | 子账户 APIKey  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 获取成功 | SubAccountKey  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» user_id | integer(int64) | 用户ID  
» mode | integer(int32) | 模式 1 - 经典帐户 2 - 统一账户  
» name | string | API Key名称  
» perms | array |   
»» name | string | 权限功能名称（不传值即为清空）  
\- wallet: 钱包  
\- spot: 现货/杠杆  
\- futures: 永续合约  
\- delivery: 交割合约  
\- earn: 理财  
\- custody: 托管  
\- options: 期权  
\- account: 账户信息  
\- loan: 借贷  
\- margin: 杠杆  
\- unified: 统一账户  
\- copy: 跟单  
»» read_only | boolean | 该功能是否只读  
» ip_whitelist | array | IP白名单列表（不传值即为清空）  
» key | string | API Key  
» state | integer(int32) | 状态 1 - 正常 2 - 冻结 3 - 锁定  
» created_at | integer(int64) | 创建时间  
» updated_at | integer(int64) | 最近更新时间  
» last_access | integer(int64) | 最近使用时间  
  
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
    
    url = '/sub_accounts/0/keys/string'
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
    url="/sub_accounts/0/keys/string"
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
      "state": 1,
      "name": "spot",
      "user_id": 1000000,
      "perms": [
        {
          "name": "futures",
          "read_only": false
        },
        {
          "name": "wallet",
          "read_only": false
        },
        {
          "name": "delivery",
          "read_only": false
        },
        {
          "name": "options",
          "read_only": false
        },
        {
          "name": "spot",
          "read_only": false
        }
      ],
      "mode": 1,
      "ip_whitelist": [
        "127.0.0.1",
        "127.0.0.2"
      ],
      "key": "75c3264105b74693d8cb5c7f1a8e2420",
      "created_at": 1663642892,
      "last_access": 1663642892,
      "update_at": 1663642892
    }
    

##  修改子账户 API 密钥对🔒 需要认证

PUT`/sub_accounts/{user_id}/keys/{key}`

PUT `/sub_accounts/{user_id}/keys/{key}`

_修改子账户 API 密钥对_

修改子账户 API 密钥对 (注意：此接口无法修改mode 账户类型属性)

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id | URL | integer | 是 | 子账户 UserID  
key | URL | string | 是 | 子账户 APIKey  
body | body | SubAccountKey | 是 |   
» mode | body | integer(int32) | 否 | 模式 1 - 经典帐户 2 - 统一账户  
» name | body | string | 否 | API Key名称  
» perms | body | array | 否 |   
»» name | body | string | 否 | 权限功能名称（不传值即为清空）  
\- wallet: 钱包  
\- spot: 现货/杠杆  
\- futures: 永续合约  
\- delivery: 交割合约  
\- earn: 理财  
\- custody: 托管  
\- options: 期权  
\- account: 账户信息  
\- loan: 借贷  
\- margin: 杠杆  
\- unified: 统一账户  
\- copy: 跟单  
»» read_only | body | boolean | 否 | 该功能是否只读  
» ip_whitelist | body | array | 否 | IP白名单列表（不传值即为清空）  
  
####  详细描述

**»» name** : 权限功能名称（不传值即为清空）  
\- wallet: 钱包  
\- spot: 现货/杠杆  
\- futures: 永续合约  
\- delivery: 交割合约  
\- earn: 理财  
\- custody: 托管  
\- options: 期权  
\- account: 账户信息  
\- loan: 借贷  
\- margin: 杠杆  
\- unified: 统一账户  
\- copy: 跟单

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
    
    url = '/sub_accounts/0/keys/string'
    query_param = ''
    body='{"mode":1,"name":"spot","perms":[{"read_only":false,"name":"options"},{"read_only":false,"name":"spot"},{"read_only":false,"name":"delivery"},{"read_only":false,"name":"wallet"},{"read_only":false,"name":"futures"}],"ip_whitelist":["127.0.0.1","127.0.0.2"]}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('PUT', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('PUT', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="PUT"
    url="/sub_accounts/0/keys/string"
    query_param=""
    body_param='{"mode":1,"name":"spot","perms":[{"read_only":false,"name":"options"},{"read_only":false,"name":"spot"},{"read_only":false,"name":"delivery"},{"read_only":false,"name":"wallet"},{"read_only":false,"name":"futures"}],"ip_whitelist":["127.0.0.1","127.0.0.2"]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "mode": 1,
      "name": "spot",
      "perms": [
        {
          "read_only": false,
          "name": "options"
        },
        {
          "read_only": false,
          "name": "spot"
        },
        {
          "read_only": false,
          "name": "delivery"
        },
        {
          "read_only": false,
          "name": "wallet"
        },
        {
          "read_only": false,
          "name": "futures"
        }
      ],
      "ip_whitelist": [
        "127.0.0.1",
        "127.0.0.2"
      ]
    }
    

##  删除子账户 API 密钥对🔒 需要认证

DELETE`/sub_accounts/{user_id}/keys/{key}`

DELETE `/sub_accounts/{user_id}/keys/{key}`

_删除子账户 API 密钥对_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id | URL | integer | 是 | 子账户 UserID  
key | URL | string | 是 | 子账户 APIKey  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 删除成功 | 无  
  
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
    
    url = '/sub_accounts/0/keys/string'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/sub_accounts/0/keys/string"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

##  锁定子账户🔒 需要认证

POST`/sub_accounts/{user_id}/lock`

POST `/sub_accounts/{user_id}/lock`

_锁定子账户_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id | URL | integer(int64) | 是 | 子账户UserID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 锁定成功 | 无  
  
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
    
    url = '/sub_accounts/0/lock'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/sub_accounts/0/lock"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

##  解锁子账户🔒 需要认证

POST`/sub_accounts/{user_id}/unlock`

POST `/sub_accounts/{user_id}/unlock`

_解锁子账户_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
user_id | URL | integer(int64) | 是 | 子账户UserID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 解锁成功 | 无  
  
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
    
    url = '/sub_accounts/0/unlock'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/sub_accounts/0/unlock"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

##  获取子帐号模式🔒 需要认证

GET`/sub_accounts/unified_mode`

GET `/sub_accounts/unified_mode`

_获取子帐号模式_

统一账户模式：

  * `classic`: 经典账户模式
  * `multi_currency`: 跨币种保证金模式
  * `portfolio`: 组合保证金模式
  * `single_currency`: 单币种保证金模式

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [SubUserMode]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» user_id | integer(int64) | 用户id  
» is_unified | boolean | 是否是统一账户  
» mode | string | 统一账户模式：  
\- `classic`: 经典账户模式  
\- `multi_currency`: 跨币种保证金模式  
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  
  
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
    
    url = '/sub_accounts/unified_mode'
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
    url="/sub_accounts/unified_mode"
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
        "user_id": 110285555,
        "is_unified": true,
        "mode": "multi_currency"
      }
    ]
    

#  模型

##  SubUserMode

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user_id | integer(int64) | false | none | 用户id  
is_unified | boolean | false | none | 是否是统一账户  
mode | string | false | none | 统一账户模式：  
\- `classic`: 经典账户模式  
\- `multi_currency`: 跨币种保证金模式  
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  
      
    
    {
      "user_id": 0,
      "is_unified": true,
      "mode": "string"
    }
    
    

##  SubAccount

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
remark | string | false | none | 备注  
login_name | string | true | none | 子账户登录名：仅支持字母、数字、下划线，不可包含其他非法字符。  
password | string | false | none | 子账户密码  
不传默认跟随主账户  
email | string | false | none | 子账户邮箱  
不传默认跟随主账户  
state | integer(int32) | false | 只读 | 子账户状态 1正常,2冻结  
type | integer(int32) | false | 只读 | 子账号类型 1-普通子账号 3-全仓杠杆子账户  
user_id | integer(int64) | false | 只读 | 子账户 user_id  
create_time | integer(int64) | false | 只读 | 创建时间戳  
      
    
    {
      "remark": "string",
      "login_name": "string",
      "password": "string",
      "email": "string",
      "state": 0,
      "type": 0,
      "user_id": 0,
      "create_time": 0
    }
    
    

##  SubAccountKey

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user_id | integer(int64) | false | 只读 | 用户ID  
mode | integer(int32) | false | none | 模式 1 - 经典帐户 2 - 统一账户  
name | string | false | none | API Key名称  
perms | array | false | none | none  
» name | string | false | none | 权限功能名称（不传值即为清空）  
\- wallet: 钱包  
\- spot: 现货/杠杆  
\- futures: 永续合约  
\- delivery: 交割合约  
\- earn: 理财  
\- custody: 托管  
\- options: 期权  
\- account: 账户信息  
\- loan: 借贷  
\- margin: 杠杆  
\- unified: 统一账户  
\- copy: 跟单  
» read_only | boolean | false | none | 该功能是否只读  
ip_whitelist | array | false | none | IP白名单列表（不传值即为清空）  
key | string | false | 只读 | API Key  
state | integer(int32) | false | 只读 | 状态 1 - 正常 2 - 冻结 3 - 锁定  
created_at | integer(int64) | false | 只读 | 创建时间  
updated_at | integer(int64) | false | 只读 | 最近更新时间  
last_access | integer(int64) | false | 只读 | 最近使用时间  
      
    
    {
      "user_id": 0,
      "mode": 0,
      "name": "string",
      "perms": [
        {
          "name": "string",
          "read_only": true
        }
      ],
      "ip_whitelist": [
        "string"
      ],
      "key": "string",
      "state": 0,
      "created_at": 0,
      "updated_at": 0,
      "last_access": 0
    }