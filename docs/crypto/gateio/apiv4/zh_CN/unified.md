---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/unified
api_type: Account
updated_at: 2026-11-28 18:56:28.744077
---

# Unified

统一账户

##  获取统一账户信息🔒 需要认证

GET`/unified/accounts`

GET `/unified/accounts`

_获取统一账户信息_

账户内的各币种资产将会根据其流动性，定义相应的调整系数，再统一折算为USD，来统一计算账户的资产及持仓价值

具体公式可查询[保证金公式 ](https://www.gate.com/zh/help/unified-account/risk_control_mechanism/33018)

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
sub_uid | 请求参数 | string | 否 | 子账号用户 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | UnifiedAccount  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
UnifiedAccount |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
mode | string | Optional |  | 统一账户模式：  
\- classic: 经典账户模式  
\- multi_currency: 跨币种保证金模式  
\- portfolio: 组合保证金模式  
\- single_currency: 单币种保证金模式  
user_id | integer(int64) | Optional |  | 用户 ID  
refresh_time | integer(int64) | Optional |  | 最近一次刷新时间  
locked | boolean | Optional |  | 账户是否被锁定：在跨币种保证金模式和组合保证金模式下有效；其他模式（如单币种保证金模式）下为 false。  
balances | object | Optional |  |   
total | string | Optional |  | 折算成 USD 的账户总资产，即所有币种 `(available + freeze) * price` 之和,(已废弃，待下线字段，用unified_account_total代替)  
borrowed | string | Optional |  | 折算成 USD 的账户总借入数量，即所有币种(不包括点卡)的 `borrowed * price` 之和,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_initial_margin | string | Optional |  | 总初始保证金(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_margin_balance | string | Optional |  | 总保证金余额(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_maintenance_margin | string | Optional |  | 总维持保证金(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_initial_margin_rate | string | Optional |  | 总初始保证金率(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_maintenance_margin_rate | string | Optional |  | 总维持保证金率(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_available_margin | string | Optional |  | 可用的保证金额度,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
unified_account_total | string | Optional |  | 统一账户总资产,单币种/跨币种模式下包括全仓总资产和逐仓总资产,组合保证金模式下只包括全仓总资产  
unified_account_total_liab | string | Optional |  | 统一账户总借贷,即全仓总借贷,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
unified_account_total_equity | string | Optional |  | 统一账户总权益,单币种/跨币种模式下包括全仓总权益和逐仓总权益,组合保证金模式下只包括全仓总权益  
leverage | string | Optional | readOnly: true | 账户杠杆倍数，在跨币种保证金/组合保证金模式下有效（已废弃）币种杠杆倍数查询接口：GET /unified/leverage/user_currency_setting  
spot_order_loss | string | Optional |  | 现货挂单损失，单位为USDT，只在跨币种模式和组合保证金模式下有效。  
options_order_loss | string | Optional |  | 期权挂单损失，单位为USDT，只在组合保证金模式下有效。  
spot_hedge | boolean | Optional |  | 现货对冲状态, true - 启用，false - 未启用  
use_funding | boolean | Optional |  | 是否将余币宝理财资金作为保证金  
is_all_collateral | boolean | Optional |  | 是否所有币种均作为保证金，true - 所有币种作为保证金，false - 否  
  
**balances**

类型 | 约束  
---|---  
object |   
  
**balances / additionalProperties**

UnifiedBalance

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
available | string | Optional |  | 全仓可用余额，已扣除合约逐仓占用及冻结（合约逐仓占用，即合约逐仓余额），在单币种/跨币种/组合保证金模式下有效。  
freeze | string | Optional |  | 被冻结的额度,在单币种保证金/跨币种保证金/组合保证金模式模式下有效  
borrowed | string | Optional |  | 借入额度,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
negative_liab | string | Optional |  | 负余额借贷,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
futures_pos_liab | string | Optional |  | 合约开仓借币(已废弃,待下线字段)  
equity | string | Optional |  | 币种权益数量（全仓）,在单币种保证金/跨币种保证金/组合保证金模式模式下有效  
total_freeze | string | Optional |  | 总占用(已废弃,待下线字段)  
total_liab | string | Optional |  | 总借款,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
spot_in_use | string | Optional |  | 现货对冲占用数量,在组合保证金模式下有效，其他如单币种、跨币种保证金模式下是0  
funding | string | Optional |  | 余币宝理财数量,在余币宝理财作为统一账户保证金开关打开有效  
funding_version | string | Optional |  | 余币宝理财版本号  
cross_balance | string | Optional |  | 全仓余额,在单币种保证金模式、跨币种保证金模式下有效，其他如组合保证金模式下是0  
iso_balance | string | Optional |  | 合约逐仓余额，在单币种保证金模式、跨币种保证金模式下有效，其他如组合保证金模式下是0  
im | string | Optional |  | 全仓初始保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
mm | string | Optional |  | 全仓维持保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
imr | string | Optional |  | 全仓初始保证金率,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
mmr | string | Optional |  | 全仓维持保证金率,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
margin_balance | string | Optional |  | 全仓保证金余额,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
available_margin | string | Optional |  | 全仓可用保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
enabled_collateral | boolean | Optional |  | 币种开启作为保证金，true - 启用，false - 未启用  
balance_version | number(int64) | Optional |  | 余额版本号  
  
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
    
    url = '/unified/accounts'
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
    url="/unified/accounts"
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
      "user_id": 10001,
      "locked": false,
      "balances": {
        "ETH": {
          "available": "0",
          "freeze": "0",
          "borrowed": "0.075393666654",
          "negative_liab": "0",
          "futures_pos_liab": "0",
          "equity": "1016.1",
          "total_freeze": "0",
          "total_liab": "0",
          "spot_in_use": "1.111"
        },
        "POINT": {
          "available": "9999999999.017023138734",
          "freeze": "0",
          "borrowed": "0",
          "negative_liab": "0",
          "futures_pos_liab": "0",
          "equity": "12016.1",
          "total_freeze": "0",
          "total_liab": "0",
          "spot_in_use": "12"
        },
        "USDT": {
          "available": "0.00000062023",
          "freeze": "0",
          "borrowed": "0",
          "negative_liab": "0",
          "futures_pos_liab": "0",
          "equity": "16.1",
          "total_freeze": "0",
          "total_liab": "0",
          "spot_in_use": "12"
        }
      },
      "total": "230.94621713",
      "borrowed": "161.66395521",
      "total_initial_margin": "1025.0524665088",
      "total_margin_balance": "3382495.944473949183",
      "total_maintenance_margin": "205.01049330176",
      "total_initial_margin_rate": "3299.827135672679",
      "total_maintenance_margin_rate": "16499.135678363399",
      "total_available_margin": "3381470.892007440383",
      "unified_account_total": "3381470.892007440383",
      "unified_account_total_liab": "0",
      "unified_account_total_equity": "100016.1",
      "leverage": "2",
      "spot_order_loss": "12",
      "spot_hedge": false
    }
    

##  查询统一账户最多可借入🔒 需要认证

GET`/unified/borrowable`

GET `/unified/borrowable`

_查询统一账户最多可借入_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 是 | 指定币种名称查询  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UnifiedBorrowable  
  
### 返回格式

状态码 **200**

UnifiedBorrowable

统一账户最多可借入额度

类型 | 约束  
---|---  
UnifiedBorrowable |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种信息  
amount | string | Optional |  | 最多可借入的额度  
  
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
    
    url = '/unified/borrowable'
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
    url="/unified/borrowable"
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
      "amount": "10000"
    }
    

##  查询统一账户最多可转出🔒 需要认证

GET`/unified/transferable`

GET `/unified/transferable`

_查询统一账户最多可转出_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 是 | 指定币种名称查询  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UnifiedTransferable  
  
### 返回格式

状态码 **200**

UnifiedTransferable

类型 | 约束  
---|---  
UnifiedTransferable |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种信息  
amount | string | Optional |  | 最多可转出的额度  
  
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
    
    url = '/unified/transferable'
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
    url="/unified/transferable"
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
      "amount": "10000"
    }
    

##  批量查询统一账户最大可转出金额🔒 需要认证

GET`/unified/transferables`

GET `/unified/transferables`

_批量查询统一账户最大可转出金额_

每个币种返回其最大可转出金额；用户提币后，所有币种的可转金额都会变更。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currencies | 请求参数 | string | 是 | 指定币种名称批量查询，最多一次支持 100 个传参。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [Inline]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

TransferablesResult

批量查询统一账户最多可转出结果

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种信息  
amount | string | Optional |  | 最多可转出的额度  
  
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
    
    url = '/unified/transferables'
    query_param = 'currencies=BTC,ETH'
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
    url="/unified/transferables"
    query_param="currencies=BTC,ETH"
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
        "amount": "123456"
      }
    ]
    

##  批量查询统一账户最多可借🔒 需要认证

GET`/unified/batch_borrowable`

GET `/unified/batch_borrowable`

_批量查询统一账户最多可借_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currencies | 请求参数 | array[string] | 是 | 指定币种名称查询数组，数组用逗号分割，最大10个  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UnifiedBorrowable]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

UnifiedBorrowable

统一账户最多可借入额度

类型 | 约束  
---|---  
UnifiedBorrowable |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种信息  
amount | string | Optional |  | 最多可借入的额度  
  
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
    
    url = '/unified/batch_borrowable'
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
    url="/unified/batch_borrowable"
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
    
    
    [
      {
        "currency": "BTC",
        "amount": "123456"
      }
    ]
    

##  查询借贷🔒 需要认证

GET`/unified/loans`

GET `/unified/loans`

_查询借贷_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大100。  
type | 请求参数 | string | 否 | 借贷类型，平台借币 - platform，杠杆借币 - margin  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniLoan]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

借贷

类型 | 约束  
---|---  
UniLoan |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional | readOnly: true | 币种  
currency_pair | string | Optional | readOnly: true | 交易对  
amount | string | Optional | readOnly: true | 待归还数量  
type | string | Optional | readOnly: true | 借贷类型，平台借币 - platform，杠杆借币 - margin  
create_time | integer(int64) | Optional | readOnly: true | 创建时间戳  
update_time | integer(int64) | Optional | readOnly: true | 最近更新时间戳  
  
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
    
    url = '/unified/loans'
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
    url="/unified/loans"
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

POST`/unified/loans`

POST `/unified/loans`

_借入或还款_

借入时必须保证不能少于币种最小借入量，不能超过平台及用户最大可借数量

借款利息会定期从账户自动扣除，用户需自主处理借款部分的还款

还款支持`repaid_all=true`全部还款

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | UnifiedLoan | 是 |   
currency | body | string | 是 | 币种  
type | body | string | 是 | 类型 , borrow - 借入 , repay - 还款  
amount | body | string | 是 | 借入或还款数量  
repaid_all | body | boolean | 否 | 全部还款，仅还款操作使用，为 `true` 时覆盖 `amount` ，直接全部还款  
text | body | string | 否 | 用户自定义 ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
type | borrow  
type | repay  
  
####  请求体结构

借入或还款

请求体结构类型 | 约束  
---|---  
UnifiedLoan | required: ["currency","amount","type"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种  
type | string | Required | enum: ["borrow","repay"] | 类型 , borrow - 借入 , repay - 还款  
amount | string | Required |  | 借入或还款数量  
repaid_all | boolean | Optional |  | 全部还款，仅还款操作使用，为 `true` 时覆盖 `amount` ，直接全部还款  
text | string | Optional |  | 用户自定义 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 操作成功 | UnifiedLoanResult  
  
### 返回格式

状态码 **200**

统一账户借还款响应结果

类型 | 约束  
---|---  
UnifiedLoanResult |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tran_id | integer(int64) | Optional |  | 交易id  
  
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
    
    url = '/unified/loans'
    query_param = ''
    body='{"currency":"BTC","amount":"0.1","type":"borrow","repaid_all":false,"text":"t-test"}'
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
    url="/unified/loans"
    query_param=""
    body_param='{"currency":"BTC","amount":"0.1","type":"borrow","repaid_all":false,"text":"t-test"}'
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
      "repaid_all": false,
      "text": "t-test"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "tran_id": 9527
    }
    

##  查询借贷记录🔒 需要认证

GET`/unified/loan_records`

GET `/unified/loan_records`

_查询借贷记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
type | 请求参数 | string | 否 | 借贷记录类型 , borrow - 借入 , repay - 还款  
currency | 请求参数 | string | 否 | 指定币种名称查询  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大100。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UnifiedLoanRecord]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

借贷记录

类型 | 约束  
---|---  
UnifiedLoanRecord |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | id  
type | string | Optional | readOnly: true | 类型 , borrow - 借入 , repay - 还款  
repayment_type | string | Optional | readOnly: true | 还款类型 , none - 无还款类型, manual_repay - 手动还款 , auto_repay - 自动还款, cancel_auto_repay - 撤单后自动还款, different_currencies_repayment - 异币种还款  
borrow_type | string | Optional |  | 借款类型, 查询借款记录时返回，manual_borrow - 手动还款 , auto_borrow - 自动还款  
currency_pair | string | Optional | readOnly: true | 交易对  
currency | string | Optional | readOnly: true | 币种  
amount | string | Optional | readOnly: true | 借入或还款数量  
create_time | integer(int64) | Optional | readOnly: true | 创建时间戳  
  
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
    
    url = '/unified/loan_records'
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
    url="/unified/loan_records"
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
        "id": 16442,
        "type": "borrow",
        "margin_mode": "cross",
        "currency_pair": "AE_USDT",
        "currency": "USDT",
        "amount": "1000",
        "create_time": 1673247054000,
        "repayment_type": "auto_repay"
      }
    ]
    

##  查询扣息记录🔒 需要认证

GET`/unified/interest_records`

GET `/unified/interest_records`

_查询扣息记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大100。  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
type | 请求参数 | string | 否 | 借贷类型，平台借币 - platform，杠杆借币 - margin，不传时默认为margin  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UniLoanInterestRecord]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

扣息记录

类型 | 约束  
---|---  
UniLoanInterestRecord |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional | readOnly: true | 币种名称  
currency_pair | string | Optional | readOnly: true | 交易对  
actual_rate | string | Optional | readOnly: true | 实际利率  
interest | string | Optional | readOnly: true | 利息  
status | integer | Optional | readOnly: true | 状态 0 - 失败 , 1 - 成功  
type | string | Optional | readOnly: true | 借贷类型，margin表示为杠杆借币  
create_time | integer(int64) | Optional | readOnly: true | 创建时间戳  
  
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
    
    url = '/unified/interest_records'
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
    url="/unified/interest_records"
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
    

##  获取用户风险单元详情🔒 需要认证

GET`/unified/risk_units`

GET `/unified/risk_units`

_获取用户风险单元详情_

获取用户风险单元详情，仅在组合保证金模式有效

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UnifiedRiskUnits  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
UnifiedRiskUnits |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | 用户 ID  
spot_hedge | boolean | Optional |  | 现货对冲状态, true - 启用，false - 未启用  
risk_units | array | Optional |  | 风险单元  
  
**risk_units**

风险单元

类型 | 约束  
---|---  
array |   
  
**risk_units / items**

RiskUnits

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 风险单元标志  
spot_in_use | string | Optional |  | 现货对冲占用数量  
maintain_margin | string | Optional |  | 风险单元的维持保证金  
initial_margin | string | Optional |  | 风险单元的起始保证金  
delta | string | Optional |  | 风险单元的 总 delta  
gamma | string | Optional |  | 风险单元的 总 gamma  
theta | string | Optional |  | 风险单元的 总 theta  
vega | string | Optional |  | 风险单元的 总 vega  
  
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
    
    url = '/unified/risk_units'
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
    url="/unified/risk_units"
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
      "user_id": 0,
      "spot_hedge": true,
      "risk_units": [
        {
          "symbol": "BTC",
          "spot_in_use": "-13500.000001223",
          "maintain_margin": "2334.002",
          "initial_margin": "2334.002",
          "delta": "0.22",
          "gamma": "0.42",
          "theta": "0.29",
          "vega": "0.22"
        }
      ]
    }
    

##  查询统一账户模式🔒 需要认证

GET`/unified/unified_mode`

GET `/unified/unified_mode`

_查询统一账户模式_

统一账户模式：

  * `classic`: 经典账户模式
  * `multi_currency`: 跨币种保证金模式
  * `portfolio`: 组合保证金模式
  * `single_currency`: 单币种保证金模式

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UnifiedModeSet  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
UnifiedModeSet | required: ["mode"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
mode | string | Required |  | 统一账户模式：   
\- `classic`: 经典账户模式   
\- `multi_currency`: 跨币种保证金模式   
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  
settings | object | Optional |  |   
  
**settings**

UnifiedSettings

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
usdt_futures | boolean | Optional |  | USDT合约开关。跨币种保证金模式下只能打开不能关闭  
spot_hedge | boolean | Optional |  | 现货对冲开关。  
use_funding | boolean | Optional |  | 余币宝开关，当mode为跨币种保证金模式时,是否将余币宝理财资金作为保证金  
options | boolean | Optional |  | 期权开关。跨币种保证金模式下只能打开不能关闭  
  
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
    
    url = '/unified/unified_mode'
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
    url="/unified/unified_mode"
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
      "mode": "portfolio",
      "settings": {
        "spot_hedge": true,
        "usdt_futures": true,
        "options": true
      }
    }
    

##  设置统一账户模式🔒 需要认证

PUT`/unified/unified_mode`

PUT `/unified/unified_mode`

_设置统一账户模式_

每种账户模式的切换只需要传对应账户模式的参数，同时支持在切换账户模式时打开或关闭对应账户模式下的配置开关

  * 开通经典账户模式时，mode=classic

    
    
        PUT /unified/unified_mode
        {
          "mode": "classic"
        }
    

  * 开通跨币种保证金模式，mode=multi_currency

    
    
        PUT /unified/unified_mode
        {
          "mode": "multi_currency",
          "settings": {
             "usdt_futures": true
          }
        }
    

  * 开通组合保证金模式时，mode=portfolio

    
    
        PUT /unified/unified_mode
        {
          "mode": "portfolio",
          "settings": {
             "spot_hedge": true
          }
        }
    

  * 开通单币种保证金模式时，mode=single_currency

    
    
        PUT /unified/unified_mode
        {
          "mode": "single_currency"
        }
    

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | UnifiedModeSet | 是 |   
mode | body | string | 是 | 统一账户模式：   
\- `classic`: 经典账户模式   
\- `multi_currency`: 跨币种保证金模式   
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  
  
settings | body | object | 否 |   
» usdt_futures | body | boolean | 否 | USDT合约开关。跨币种保证金模式下只能打开不能关闭  
» spot_hedge | body | boolean | 否 | 现货对冲开关。  
» use_funding | body | boolean | 否 | 余币宝开关，当mode为跨币种保证金模式时,是否将余币宝理财资金作为保证金  
» options | body | boolean | 否 | 期权开关。跨币种保证金模式下只能打开不能关闭  
  
####  详细描述

** mode**: 统一账户模式：   
\- `classic`: 经典账户模式   
\- `multi_currency`: 跨币种保证金模式   
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  

####  请求体结构

请求体结构类型 | 约束  
---|---  
UnifiedModeSet | required: ["mode"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
mode | string | Required |  | 统一账户模式：   
\- `classic`: 经典账户模式   
\- `multi_currency`: 跨币种保证金模式   
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  
settings | object | Optional |  |   
  
**settings**

UnifiedSettings

请求体结构类型 | 约束  
---|---  
object |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
usdt_futures | boolean | Optional |  | USDT合约开关。跨币种保证金模式下只能打开不能关闭  
spot_hedge | boolean | Optional |  | 现货对冲开关。  
use_funding | boolean | Optional |  | 余币宝开关，当mode为跨币种保证金模式时,是否将余币宝理财资金作为保证金  
options | boolean | Optional |  | 期权开关。跨币种保证金模式下只能打开不能关闭  
  
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
    
    url = '/unified/unified_mode'
    query_param = ''
    body='{"mode":"portfolio","settings":{"spot_hedge":true,"usdt_futures":true,"options":true}}'
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
    url="/unified/unified_mode"
    query_param=""
    body_param='{"mode":"portfolio","settings":{"spot_hedge":true,"usdt_futures":true,"options":true}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "mode": "portfolio",
      "settings": {
        "spot_hedge": true,
        "usdt_futures": true,
        "options": true
      }
    }
    

##  查询统一账户的预估利率🔒 需要认证

GET`/unified/estimate_rate`

GET `/unified/estimate_rate`

_查询统一账户的预估利率_

因为利率每小时会随借贷深度变化，不能提供完全精确的利率；当币种不支持时，返回利率为空字符串

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currencies | 请求参数 | array[string] | 是 | 指定币种名称查询数组，数组用逗号分割，最大10个  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | EstimateRate  
  
### 返回格式

状态码 **200**

预估当前小时的借贷利率，按币种进行返回

类型 | 约束  
---|---  
EstimateRate |   
  
**additionalProperties**

类型 | 约束  
---|---  
string |   
  
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
    
    url = '/unified/estimate_rate'
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
    url="/unified/estimate_rate"
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
      "GT": "0.000001",
      "ETH": ""
    }
    

##  查询统一账户币种保证金折扣梯度

GET`/unified/currency_discount_tiers`

GET `/unified/currency_discount_tiers`

_查询统一账户币种保证金折扣梯度_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UnifiedDiscount]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

统一账户梯度discount

类型 | 约束  
---|---  
UnifiedDiscount |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
discount_tiers | array | Optional |  | 阶梯式discount  
  
**items / discount_tiers**

阶梯式discount

类型 | 约束  
---|---  
array |   
  
**items / discount_tiers / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tier | string | Optional |  | 档位  
discount | string | Optional |  | 保证金折扣系数  
lower_limit | string | Optional |  | 下限  
upper_limit | string | Optional |  | 上限, +表示正无穷  
leverage | string | Optional |  | 杠杆倍数  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/currency_discount_tiers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/unified/currency_discount_tiers \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      [
        {
          "currency": "USDT",
          "discount_tiers": [
            {
              "tier": "1",
              "discount": "1",
              "lower_limit": "0",
              "leverage": "10",
              "upper_limit": "+"
            }
          ]
        },
        {
          "currency": "USDC",
          "discount_tiers": [
            {
              "tier": "1",
              "discount": "1",
              "lower_limit": "0",
              "leverage": "10",
              "upper_limit": "10000000"
            },
            {
              "tier": "2",
              "discount": "0.98",
              "lower_limit": "10000000",
              "leverage": "10",
              "upper_limit": "15000000"
            },
            {
              "tier": "3",
              "discount": "0.95",
              "lower_limit": "15000000",
              "leverage": "10",
              "upper_limit": "20000000"
            },
            {
              "tier": "4",
              "discount": "0.925",
              "lower_limit": "20000000",
              "leverage": "10",
              "upper_limit": "50000000"
            },
            {
              "tier": "5",
              "discount": "0.9",
              "lower_limit": "50000000",
              "leverage": "10",
              "upper_limit": "100000000"
            },
            {
              "tier": "6",
              "discount": "0",
              "lower_limit": "100000000",
              "leverage": "10",
              "upper_limit": "+"
            }
          ]
        },
        {
          "currency": "BTC",
          "discount_tiers": [
            {
              "tier": "1",
              "discount": "0.98",
              "lower_limit": "0",
              "leverage": "10",
              "upper_limit": "1000"
            },
            {
              "tier": "2",
              "discount": "0.95",
              "lower_limit": "1000",
              "leverage": "10",
              "upper_limit": "10000"
            },
            {
              "tier": "3",
              "discount": "0.9",
              "lower_limit": "10000",
              "leverage": "10",
              "upper_limit": "50000"
            },
            {
              "tier": "4",
              "discount": "0.85",
              "lower_limit": "50000",
              "leverage": "10",
              "upper_limit": "+"
            }
          ]
        },
        {
          "currency": "ETH",
          "discount_tiers": [
            {
              "tier": "1",
              "discount": "0.98",
              "lower_limit": "0",
              "leverage": "10",
              "upper_limit": "1000"
            },
            {
              "tier": "2",
              "discount": "0.95",
              "lower_limit": "1000",
              "leverage": "10",
              "upper_limit": "10000"
            },
            {
              "tier": "3",
              "discount": "0.9",
              "lower_limit": "10000",
              "leverage": "10",
              "upper_limit": "50000"
            },
            {
              "tier": "4",
              "discount": "0.85",
              "lower_limit": "50000",
              "leverage": "10",
              "upper_limit": "+"
            }
          ]
        }
      ]
    ]
    

##  查询统一账户借贷梯度保证金

GET`/unified/loan_margin_tiers`

GET `/unified/loan_margin_tiers`

_查询统一账户借贷梯度保证金_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UnifiedMarginTiers]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

统一账户借贷保证金梯度

类型 | 约束  
---|---  
UnifiedMarginTiers |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
margin_tiers | array | Optional |  | 阶梯式保证金  
  
**items / margin_tiers**

阶梯式保证金

类型 | 约束  
---|---  
array |   
  
**items / margin_tiers / items**

MarginTiers

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tier | string | Optional |  | 档位  
margin_rate | string | Optional |  | 保证金系数  
lower_limit | string | Optional |  | 下限  
upper_limit | string | Optional |  | 上限, ``表示大于(最后一个档位)  
leverage | string | Optional |  | 杠杆倍数  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/loan_margin_tiers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/unified/loan_margin_tiers \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency": "USDT",
        "margin_tiers": [
          {
            "tier": "1",
            "margin_rate": "0.02",
            "lower_limit": "200000",
            "upper_limit": "400000",
            "leverage": "3"
          }
        ]
      }
    ]
    

##  组合保证金计算器计算

POST`/unified/portfolio_calculator`

POST `/unified/portfolio_calculator`

_组合保证金计算器计算_

组合保证金计算器

该接口支持对自定义的模拟仓位组合和挂单组合试算组合保证金模式下的维持保证金和起始保证金要求，目前已支持所有已开放期权交易的标的物币种。模拟仓位组合的每个仓位需要仓位名和持有量信息；模拟挂单需要市场标识、挂单价、挂单量信息，不支持市价单。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | UnifiedPortfolioInput | 是 |   
spot_balances | body | array | 否 | 现货  
» currency | body | string | 是 | 币种名称  
» equity | body | string | 是 | 币种权益 = 余额 - 已借，表示现货净 Delta 敞口，可为负数。  
spot_orders | body | array | 否 | 现货订单  
» currency_pairs | body | string | 是 | 市场  
» order_price | body | string | 是 | 价格  
» count | body | string | 否 | 现货交易对初始挂单数量，不参与实际计算。  
» left | body | string | 是 | 未成交数量，参与实际计算  
» type | body | string | 是 | 订单类型，sell - 卖出单，buy - 买入单  
futures_positions | body | array | 否 | 合约仓位  
» contract | body | string | 是 | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
» size | body | string | 是 | 仓位大小，单位是张数  
futures_orders | body | array | 否 | 合约订单  
» contract | body | string | 是 | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
» size | body | string | 是 | 合约张数，为初始挂单数量，不参与实际结算  
» left | body | string | 是 | 未成交张数，参与实际计算  
options_positions | body | array | 否 | 期权仓位  
» options_name | body | string | 是 | 期权合约市场名称，目前支持所有期权合约市场  
» size | body | string | 是 | 仓位大小，单位是张数  
options_orders | body | array | 否 | 期权订单  
» options_name | body | string | 是 | 期权合约市场名称，目前支持所有期权合约市场  
» size | body | string | 是 | 初始挂单张数，不参与实际计算  
» left | body | string | 是 | 未成交张数，参与实际计算  
spot_hedge | body | boolean | 否 | 是否开启现货对冲  
  
####  请求体结构

组合保证金计算器输入

请求体结构类型 | 约束  
---|---  
UnifiedPortfolioInput |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
spot_balances | array | Optional |  | 现货  
spot_orders | array | Optional |  | 现货订单  
futures_positions | array | Optional |  | 合约仓位  
futures_orders | array | Optional |  | 合约订单  
options_positions | array | Optional |  | 期权仓位  
options_orders | array | Optional |  | 期权订单  
spot_hedge | boolean | Optional |  | 是否开启现货对冲  
  
**spot_balances**

现货

请求体结构类型 | 约束  
---|---  
array |   
  
**spot_balances / items**

现货

请求体结构类型 | 约束  
---|---  
object | required: ["currency","equity"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种名称  
equity | string | Required |  | 币种权益 = 余额 - 已借，表示现货净 Delta 敞口，可为负数。  
  
**spot_orders**

现货订单

请求体结构类型 | 约束  
---|---  
array |   
  
**spot_orders / items**

现货订单

请求体结构类型 | 约束  
---|---  
object | required: ["currency_pairs","order_price","size","left","type"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency_pairs | string | Required |  | 市场  
order_price | string | Required |  | 价格  
count | string | Optional |  | 现货交易对初始挂单数量，不参与实际计算。  
left | string | Required |  | 未成交数量，参与实际计算  
type | string | Required |  | 订单类型，sell - 卖出单，buy - 买入单  
  
**futures_positions**

合约仓位

请求体结构类型 | 约束  
---|---  
array |   
  
**futures_positions / items**

合约仓位

请求体结构类型 | 约束  
---|---  
object | required: ["contract","size"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
size | string | Required |  | 仓位大小，单位是张数  
  
**futures_orders**

合约订单

请求体结构类型 | 约束  
---|---  
array |   
  
**futures_orders / items**

合约订单

请求体结构类型 | 约束  
---|---  
object | required: ["contract","size","left"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
size | string | Required |  | 合约张数，为初始挂单数量，不参与实际结算  
left | string | Required |  | 未成交张数，参与实际计算  
  
**options_positions**

期权仓位

请求体结构类型 | 约束  
---|---  
array |   
  
**options_positions / items**

期权仓位

请求体结构类型 | 约束  
---|---  
object | required: ["options_name","size"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
options_name | string | Required |  | 期权合约市场名称，目前支持所有期权合约市场  
size | string | Required |  | 仓位大小，单位是张数  
  
**options_orders**

期权订单

请求体结构类型 | 约束  
---|---  
array |   
  
**options_orders / items**

期权订单

请求体结构类型 | 约束  
---|---  
object | required: ["options_name","size","left"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
options_name | string | Required |  | 期权合约市场名称，目前支持所有期权合约市场  
size | string | Required |  | 初始挂单张数，不参与实际计算  
left | string | Required |  | 未成交张数，参与实际计算  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UnifiedPortfolioOutput  
  
### 返回格式

状态码 **200**

组合保证金计算器输出

类型 | 约束  
---|---  
UnifiedPortfolioOutput |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
maintain_margin_total | string | Optional |  | 总维持保证金，只包含risk unit的仓位的组合保证金计算结果，不包含借币保证金。如果存在借币，实际还会产生常规的借币保证金要求。  
initial_margin_total | string | Optional |  | 总起始保证金，为以下三个组合的最大计算结果：仓位、仓位+正delta挂单、仓位+负delta挂单  
calculate_time | integer(int64) | Optional |  | 计算时间  
risk_unit | array | Optional |  | 风险单元  
  
**risk_unit**

风险单元

类型 | 约束  
---|---  
array |   
  
**risk_unit / items**

风险单元

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 风险单元名称  
spot_in_use | string | Optional |  | 现货对冲使用量  
maintain_margin | string | Optional |  | 维持保证金  
initial_margin | string | Optional |  | 起始保证金  
margin_result | array | Optional |  | 保证金结果  
delta | string | Optional |  | 风险单元的 总 delta  
gamma | string | Optional |  | 风险单元的 总 gamma  
theta | string | Optional |  | 风险单元的 总 theta  
vega | string | Optional |  | 风险单元的 总 vega  
  
**risk_unit / items / margin_result**

保证金结果

类型 | 约束  
---|---  
array |   
  
**risk_unit / items / margin_result / items**

保证金结果

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
type | string | Optional |  | 仓位组合类型  
`original_position` \- 原始仓位  
`long_delta_original_position` \- 正向delta+原始仓位  
`short_delta_original_position` \- 负向delta+原始仓位  
profit_loss_ranges | array | Optional |  | mr1的33个压力场景测试结果  
max_loss | object | Optional |  | 盈亏范围  
mr1 | string | Optional |  | 压力测试  
mr2 | string | Optional |  | 基差跨期风险  
mr3 | string | Optional |  | 波动率跨期风险  
mr4 | string | Optional |  | 期权空头风险  
  
**risk_unit / items / margin_result / items / profit_loss_ranges**

mr1的33个压力场景测试结果

类型 | 约束  
---|---  
array |   
  
**risk_unit / items / margin_result / items / profit_loss_ranges / items**

盈亏范围

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price_percentage | string | Optional |  | 价格变动百分比  
implied_volatility_percentage | string | Optional |  | 隐含波动率变动百分比  
profit_loss | string | Optional |  | 盈亏  
  
**risk_unit / items / margin_result / items / max_loss**

盈亏范围

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price_percentage | string | Optional |  | 价格变动百分比  
implied_volatility_percentage | string | Optional |  | 隐含波动率变动百分比  
profit_loss | string | Optional |  | 盈亏  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/portfolio_calculator'
    query_param = ''
    body='{"spot_balances":[{"currency":"BTC","equity":"-1","freeze":"10"}],"spot_orders":[{"currency_pairs":"BTC_USDT","order_price":"344","size":"100","left":"100","type":"sell"}],"futures_positions":[{"contract":"BTC_USDT","size":"100"}],"futures_orders":[{"contract":"BTC_USDT","size":"10","left":"8"}],"options_positions":[{"options_name":"BTC_USDT-20240329-32000-C","size":"10"}],"options_orders":[{"options_name":"BTC_USDT-20240329-32000-C","size":"100","left":"80"}],"spot_hedge":false}'
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    curl -X POST https://api.gateio.ws/api/v4/unified/portfolio_calculator \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    
    

> 请求体示例
    
    
    {
      "spot_balances": [
        {
          "currency": "BTC",
          "equity": "-1",
          "freeze": "10"
        }
      ],
      "spot_orders": [
        {
          "currency_pairs": "BTC_USDT",
          "order_price": "344",
          "size": "100",
          "left": "100",
          "type": "sell"
        }
      ],
      "futures_positions": [
        {
          "contract": "BTC_USDT",
          "size": "100"
        }
      ],
      "futures_orders": [
        {
          "contract": "BTC_USDT",
          "size": "10",
          "left": "8"
        }
      ],
      "options_positions": [
        {
          "options_name": "BTC_USDT-20240329-32000-C",
          "size": "10"
        }
      ],
      "options_orders": [
        {
          "options_name": "BTC_USDT-20240329-32000-C",
          "size": "100",
          "left": "80"
        }
      ],
      "spot_hedge": false
    }
    

> 返回示例

> 200 返回
    
    
    {
      "maintain_margin_total": "0.000000000000",
      "initial_margin_total": "0.000000000000",
      "calculate_time": "1709014486",
      "risk_unit": [
        {
          "symbol": "BTC",
          "margin_result": [
            {
              "type": "original_position",
              "profit_loss_ranges": [
                {
                  "price_percentage": "-0.200000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "-0.160000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "-0.120000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "-0.080000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "-0.040000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.000000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.040000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.080000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.120000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.160000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.200000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                }
              ],
              "max_loss": {
                "price_percentage": "-0.200000000000",
                "implied_volatility_percentage": "-0.300000000000",
                "profit_loss": "0.000000000000"
              },
              "mr1": "0.000000000000",
              "mr2": "0.000000000000",
              "mr3": "0.000000000000",
              "mr4": "0.000000000000"
            }
          ],
          "maintain_margin": "0.000000000000",
          "initial_margin": "0.000000000000"
        }
      ]
    }
    

##  设置用户所有借贷币种杠杆倍数🔒 需要认证

POST`/unified/leverage/user_setting`

POST `/unified/leverage/user_setting`

_设置用户所有借贷币种杠杆倍数_

使用时需要注意以下几点：

  * 存在借贷的币种不能进行修改
  * 超过杠杆阈值的币种按阈值设置
  * 设置失败不会进行回滚，而是只影响失败的币种，比如USDT存在借贷，则仅仅USDT杠杆倍数不会被修改

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | object | 是 |   
leverage | body | string | 否 | 杠杆倍数（超出币种杠杆倍数阈值按阈值设置）  
  
####  请求体结构

UserLeverageSetting

用户杠杆倍数设置

请求体结构类型 | 约束  
---|---  
object |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
leverage | string | Optional |  | 杠杆倍数（超出币种杠杆倍数阈值按阈值设置）  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 设置成功 | [Inline]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

LeverageFailedCurrencies

设置杠杆倍数失败的币种列表

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 设置失败的币种  
reason | string | Optional |  | 杠杆倍数设置失败原因  
  
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
    
    url = '/unified/leverage/user_setting'
    query_param = ''
    body='{"leverage":"10"}'
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
    url="/unified/leverage/user_setting"
    query_param=""
    body_param='{"leverage":"10"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "leverage": "10"
    }
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency": "string",
        "reason": "string"
      }
    ]
    

##  用户最大、最小可设置币种杠杆倍数🔒 需要认证

GET`/unified/leverage/user_currency_config`

GET `/unified/leverage/user_currency_config`

_用户最大、最小可设置币种杠杆倍数_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 是 | 币种  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UnifiedLeverageConfig  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
UnifiedLeverageConfig |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
current_leverage | string | Optional |  | 当前杠杆倍数  
min_leverage | string | Optional |  | 最小可调杠杆倍数  
max_leverage | string | Optional |  | 最大可调杠杆倍数  
debit | string | Optional |  | 当前负债  
available_margin | string | Optional |  | 可用保证金  
borrowable | string | Optional |  | 当前选择杠杆可借  
except_leverage_borrowable | string | Optional |  | 保证金最大可借、余币宝最大可借，两者取较小的值  
  
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
    
    url = '/unified/leverage/user_currency_config'
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
    url="/unified/leverage/user_currency_config"
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
      "current_leverage": "2",
      "min_leverage": "0",
      "max_leverage": "0",
      "debit": "0",
      "available_margin": "0",
      "borrowable": "0",
      "except_leverage_borrowable": "0"
    }
    

##  获取用户币种杠杆倍数🔒 需要认证

GET`/unified/leverage/user_currency_setting`

GET `/unified/leverage/user_currency_setting`

_获取用户币种杠杆倍数_

获取用户币种杠杆倍数，currency不传则查询全部币种

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 币种  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UnifiedLeverageSetting]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

借贷币种杠杆倍数

类型 | 约束  
---|---  
UnifiedLeverageSetting | required: ["currency","leverage"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种名称  
leverage | string | Required |  | 倍数  
  
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
    
    url = '/unified/leverage/user_currency_setting'
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
    url="/unified/leverage/user_currency_setting"
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
        "leverage": "3"
      }
    ]
    

##  设置借贷币种杠杆倍数🔒 需要认证

POST`/unified/leverage/user_currency_setting`

POST `/unified/leverage/user_currency_setting`

_设置借贷币种杠杆倍数_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | UnifiedLeverageSetting | 是 |   
currency | body | string | 是 | 币种名称  
leverage | body | string | 是 | 倍数  
  
####  请求体结构

借贷币种杠杆倍数

请求体结构类型 | 约束  
---|---  
UnifiedLeverageSetting | required: ["currency","leverage"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种名称  
leverage | string | Required |  | 倍数  
  
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
    
    url = '/unified/leverage/user_currency_setting'
    query_param = ''
    body='{"currency":"BTC","leverage":"3"}'
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
    url="/unified/leverage/user_currency_setting"
    query_param=""
    body_param='{"currency":"BTC","leverage":"3"}'
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
      "leverage": "3"
    }
    

##  统一账户支持的借贷币种列表

GET`/unified/currencies`

GET `/unified/currencies`

_统一账户支持的借贷币种列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 币种  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [UnifiedCurrency]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
UnifiedCurrency |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
name | string | Optional |  | 币种名称  
prec | string | Optional |  | 币种精度  
min_borrow_amount | string | Optional |  | 最小可借限额，单位是币  
user_max_borrow_amount | string | Optional |  | 用户最大可借限额，单位是 USDT  
total_max_borrow_amount | string | Optional |  | 平台最大可借限额，单位是 USDT  
loan_status | string | Optional |  | 是否借贷状态  
\- `disable` : 禁止借贷  
\- `enable` : 支持借贷  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/currencies'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/unified/currencies \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "name": "BTC",
        "prec": "0.000001",
        "min_borrow_amount": "0.01",
        "user_max_borrow_amount": "1000000",
        "total_max_borrow_amount": "1000000",
        "loan_status": "enable"
      }
    ]
    

##  获取历史借币利率

GET`/unified/history_loan_rate`

GET `/unified/history_loan_rate`

_获取历史借币利率_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
tier | 请求参数 | string | 否 | 需要查询的上浮费率的vip等级  
currency | 请求参数 | string | 是 | 币种  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大100。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UnifiedHistoryLoanRate  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
UnifiedHistoryLoanRate |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
tier | string | Optional |  | 需要获取的上浮费率的vip等级  
tier_up_rate | string | Optional |  | vip等级对应的上浮费率  
rates | array | Optional |  | 历史利率信息，每个整点小时一个数据，数组大小根据接口请求参数提供的page和limit参数确定，按照时间从近到远排序  
  
**rates**

历史利率信息，每个整点小时一个数据，数组大小根据接口请求参数提供的page和limit参数确定，按照时间从近到远排序

类型 | 约束  
---|---  
array |   
  
**rates / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional |  | 该利率对应的整点小时时间戳，单位为毫秒  
rate | string | Optional |  | 该整点小时的历史利率  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/history_loan_rate'
    query_param = 'currency=USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/unified/history_loan_rate?currency=USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "currency": "USDT",
      "tier": "1",
      "tier_up_rate": "1.18",
      "rates": [
        {
          "time": 1729047616000,
          "rate": "0.00010287"
        }
      ]
    }
    

##  设置抵押币种🔒 需要认证

POST`/unified/collateral_currencies`

POST `/unified/collateral_currencies`

_设置抵押币种_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | UnifiedCollateralReq | 是 |   
collateral_type | body | integer | 否 | 用户设置抵押物模式 0(all)-全部币种作为抵押物,1(custom)-自定义币种作为抵押物,collateral_type为0(all)时，enable_list与disable_list参数无效  
enable_list | body | array | 否 | 币种列表，collateral_type=1(custom)表示追加的逻辑  
disable_list | body | array | 否 | 取消列表，表示取消的逻辑  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
collateral_type | 0  
collateral_type | 1  
  
####  请求体结构

请求体结构类型 | 约束  
---|---  
UnifiedCollateralReq |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
collateral_type | integer | Optional | enum: [0,1] | 用户设置抵押物模式 0(all)-全部币种作为抵押物,1(custom)-自定义币种作为抵押物,collateral_type为0(all)时，enable_list与disable_list参数无效  
enable_list | array | Optional |  | 币种列表，collateral_type=1(custom)表示追加的逻辑  
disable_list | array | Optional |  | 取消列表，表示取消的逻辑  
  
**enable_list**

币种列表，collateral_type=1(custom)表示追加的逻辑

请求体结构类型 | 约束  
---|---  
array |   
  
**enable_list / items**

请求体结构类型 | 约束  
---|---  
string |   
  
**disable_list**

取消列表，表示取消的逻辑

请求体结构类型 | 约束  
---|---  
array |   
  
**disable_list / items**

请求体结构类型 | 约束  
---|---  
string |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 更新成功 | UnifiedCollateralRes  
  
### 返回格式

状态码 **200**

统一账户抵押模式设置返回

类型 | 约束  
---|---  
UnifiedCollateralRes |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
is_success | boolean | Optional |  | 是否设置成功  
  
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
    
    url = '/unified/collateral_currencies'
    query_param = ''
    body='{"collateral_type":1,"enable_list":["BTC","ETH"],"disable_list":["SOL","GT"]}'
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
    url="/unified/collateral_currencies"
    query_param=""
    body_param='{"collateral_type":1,"enable_list":["BTC","ETH"],"disable_list":["SOL","GT"]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "collateral_type": 1,
      "enable_list": [
        "BTC",
        "ETH"
      ],
      "disable_list": [
        "SOL",
        "GT"
      ]
    }
    

> 返回示例

> 200 返回
    
    
    {
      "is_success": true
    }
    

##  预估快捷还款信息🔒 需要认证

GET`/unified/estimated_quick_repayment`

GET `/unified/estimated_quick_repayment`

_预估快捷还款信息_

仅限统一账户跨币种保证金模式与组合保证金模式

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | QuickEstimatedRepayment  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求参数错误 | GateErrorResponse  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | 认证失败 | GateErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 拒绝访问（如账户模式不支持快捷还款） | GateErrorResponse  
  
### 返回格式

状态码 **200**

QuickEstimatedRepayment

类型 | 约束  
---|---  
QuickEstimatedRepayment |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
debt_currencies | array | Optional |  | 负债币种列表  
available_currencies | array | Optional |  | 可用于还款币种列表  
  
**debt_currencies**

负债币种列表

类型 | 约束  
---|---  
array |   
  
**debt_currencies / items**

UnifiedDebtCurrencies

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
debt_amount | string | Optional |  | 负债数量  
estimated_usd | string | Optional |  | 预估USD价值  
borrowed | string | Optional |  | 已借数量  
neg_balance | string | Optional |  | 负余额  
  
**available_currencies**

可用于还款币种列表

类型 | 约束  
---|---  
array |   
  
**available_currencies / items**

UnifiedAvailableCurrencies

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
available | string | Optional |  | 可用余额  
estimated_usd | string | Optional |  | 预估USD价值  
  
状态码 **400**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
状态码 **401**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
状态码 **403**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
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
    
    url = '/unified/estimated_quick_repayment'
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
    url="/unified/estimated_quick_repayment"
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
      "debt_currencies": [
        {
          "currency": "ETH",
          "debt_amount": "1.5",
          "estimated_usd": "4500",
          "borrowed": "1.5",
          "neg_balance": "0"
        }
      ],
      "available_currencies": [
        {
          "currency": "USDT",
          "available": "5000",
          "estimated_usd": "5000"
        }
      ]
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_PARAM",
      "message": "invalid request"
    }
    

> 401 返回
    
    
    {
      "label": "INVALID_KEY",
      "message": "Invalid API key"
    }
    

> 403 返回
    
    
    {
      "label": "FORBIDDEN",
      "message": "quick repayment is only available in cross-currency margin or portfolio margin mode"
    }
    

##  快捷还款🔒 需要认证

POST`/unified/quick_repayment`

POST `/unified/quick_repayment`

_快捷还款_

仅限统一账户跨币种保证金模式与组合保证金模式。 可使用 `GET /unified/estimated_quick_repayment` 查询负债和待还款信息。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | QuickRepaymentRequest | 是 |   
debt_currencies | body | array | 是 | 负债币种列表  
available_currencies | body | array | 是 | 用于还款的币种列表  
  
####  请求体结构

QuickRepaymentInfo

请求体结构类型 | 约束  
---|---  
QuickRepaymentRequest | required: ["debt_currencies","available_currencies"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
debt_currencies | array | Required |  | 负债币种列表  
available_currencies | array | Required |  | 用于还款的币种列表  
  
**debt_currencies**

负债币种列表

请求体结构类型 | 约束  
---|---  
array |   
  
**debt_currencies / items**

请求体结构类型 | 约束  
---|---  
string |   
  
**available_currencies**

用于还款的币种列表

请求体结构类型 | 约束  
---|---  
array |   
  
**available_currencies / items**

请求体结构类型 | 约束  
---|---  
string |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 还款成功 | QuickRepaymentResponse  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求参数错误 | GateErrorResponse  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | 认证失败 | GateErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 拒绝访问（如账户模式不支持快捷还款） | GateErrorResponse  
  
### 返回格式

状态码 **200**

QuickRepaymentResp

快捷还款信息

类型 | 约束  
---|---  
QuickRepaymentResponse | required: ["order_id","repaid_infos","used_infos"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Required |  | 订单ID  
repaid_infos | array | Required |  | 还款币种信息：currency 是币种名称，repaid 是已还款数量，left 是剩余负债数量。  
used_infos | array | Required |  | 用于还款的币种信息：currency 是币种名称，used 是已兑换数量。  
  
**repaid_infos**

还款币种信息：currency 是币种名称，repaid 是已还款数量，left 是剩余负债数量。

类型 | 约束  
---|---  
array |   
  
**repaid_infos / items**

RepaidInfo

还款信息

类型 | 约束  
---|---  
object | required: ["currency","repaid","left"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种名称  
repaid | string | Required |  | 已还款数量  
left | string | Required |  | 剩余负债数量  
  
**used_infos**

用于还款的币种信息：currency 是币种名称，used 是已兑换数量。

类型 | 约束  
---|---  
array |   
  
**used_infos / items**

UsedInfo

还款信息

类型 | 约束  
---|---  
object | required: ["currency","used"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种名称  
used | string | Required |  | 已兑换数量  
  
状态码 **400**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
状态码 **401**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
状态码 **403**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
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
    
    url = '/unified/quick_repayment'
    query_param = ''
    body='{"debt_currencies":["ETH"],"available_currencies":["USDT","BTC"]}'
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
    url="/unified/quick_repayment"
    query_param=""
    body_param='{"debt_currencies":["ETH"],"available_currencies":["USDT","BTC"]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "debt_currencies": [
        "ETH"
      ],
      "available_currencies": [
        "USDT",
        "BTC"
      ]
    }
    

> 返回示例

> 200 返回
    
    
    {
      "order_id": "qr_123456",
      "repaid_infos": [
        {
          "currency": "ETH",
          "repaid": "0.5",
          "left": "1.0"
        }
      ],
      "used_infos": [
        {
          "currency": "USDT",
          "used": "1500"
        }
      ]
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_PARAM",
      "message": "invalid request body"
    }
    

> 401 返回
    
    
    {
      "label": "INVALID_KEY",
      "message": "Invalid API key"
    }
    

> 403 返回
    
    
    {
      "label": "FORBIDDEN",
      "message": "quick repayment is only available in cross-currency margin or portfolio margin mode"
    }
    

##  查询账户Delta中性策略模式设置🔒 需要认证

GET`/unified/delta_neutral`

GET `/unified/delta_neutral`

_查询账户Delta中性策略模式设置_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | DeltaNeutralEnabled  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | 认证失败 | GateErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 拒绝访问（如 VIP 等级不足或账户非跨币种保证金模式） | GateErrorResponse  
  
### 返回格式

状态码 **200**

DeltaNeutralEnabled

类型 | 约束  
---|---  
DeltaNeutralEnabled | required: ["enabled"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
enabled | boolean | Required |  | 是否开启账户Delta中性策略模式  
  
状态码 **401**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
状态码 **403**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
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
    
    url = '/unified/delta_neutral'
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
    url="/unified/delta_neutral"
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
    

> 401 返回
    
    
    {
      "label": "INVALID_KEY",
      "message": "Invalid API key"
    }
    

> 403 返回
    
    
    {
      "label": "FORBIDDEN",
      "message": "delta neutral strategy is only available for accounts with VIP level >= 4 in cross-currency margin mode"
    }
    

##  设置账户Delta中性策略模式🔒 需要认证

POST`/unified/delta_neutral`

POST `/unified/delta_neutral`

_设置账户Delta中性策略模式_

设置账户 Delta 中性策略模式的开启或关闭。

开启条件：VIP 等级 >= 4 且账户处于跨币种保证金模式，条件不满足时返回 403。 设置成功后返回设置后的开启状态。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | DeltaNeutralEnabled | 是 |   
enabled | body | boolean | 是 | 是否开启账户Delta中性策略模式  
  
####  请求体结构

DeltaNeutralEnabled

请求体结构类型 | 约束  
---|---  
DeltaNeutralEnabled | required: ["enabled"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
enabled | boolean | Required |  | 是否开启账户Delta中性策略模式  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 设置成功 | DeltaNeutralEnabled  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求参数错误 | GateErrorResponse  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | 认证失败 | GateErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 拒绝访问（如 VIP 等级不足或账户非跨币种保证金模式） | GateErrorResponse  
  
### 返回格式

状态码 **200**

DeltaNeutralEnabled

类型 | 约束  
---|---  
DeltaNeutralEnabled | required: ["enabled"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
enabled | boolean | Required |  | 是否开启账户Delta中性策略模式  
  
状态码 **400**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
状态码 **401**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
状态码 **403**

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
GateErrorResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
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
    
    url = '/unified/delta_neutral'
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
    url="/unified/delta_neutral"
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
    

> 返回示例

> 200 返回
    
    
    {
      "enabled": true
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_PARAM",
      "message": "invalid request body"
    }
    

> 401 返回
    
    
    {
      "label": "INVALID_KEY",
      "message": "Invalid API key"
    }
    

> 403 返回
    
    
    {
      "label": "FORBIDDEN",
      "message": "delta neutral strategy is only available for accounts with VIP level >= 4 in cross-currency margin mode"
    }
    

#  模型

##  UnifiedPortfolioOutput

组合保证金计算器输出

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
maintain_margin_total | string | Optional |  | 总维持保证金，只包含risk unit的仓位的组合保证金计算结果，不包含借币保证金。如果存在借币，实际还会产生常规的借币保证金要求。  
initial_margin_total | string | Optional |  | 总起始保证金，为以下三个组合的最大计算结果：仓位、仓位+正delta挂单、仓位+负delta挂单  
calculate_time | integer(int64) | Optional |  | 计算时间  
risk_unit | array | Optional |  | 风险单元  
  
**risk_unit**

风险单元

类型 | 约束  
---|---  
array |   
  
**risk_unit / items**

风险单元

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 风险单元名称  
spot_in_use | string | Optional |  | 现货对冲使用量  
maintain_margin | string | Optional |  | 维持保证金  
initial_margin | string | Optional |  | 起始保证金  
margin_result | array | Optional |  | 保证金结果  
delta | string | Optional |  | 风险单元的 总 delta  
gamma | string | Optional |  | 风险单元的 总 gamma  
theta | string | Optional |  | 风险单元的 总 theta  
vega | string | Optional |  | 风险单元的 总 vega  
  
**risk_unit / items / margin_result**

保证金结果

类型 | 约束  
---|---  
array |   
  
**risk_unit / items / margin_result / items**

保证金结果

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
type | string | Optional |  | 仓位组合类型  
`original_position` \- 原始仓位  
`long_delta_original_position` \- 正向delta+原始仓位  
`short_delta_original_position` \- 负向delta+原始仓位  
profit_loss_ranges | array | Optional |  | mr1的33个压力场景测试结果  
max_loss | object | Optional |  | 盈亏范围  
mr1 | string | Optional |  | 压力测试  
mr2 | string | Optional |  | 基差跨期风险  
mr3 | string | Optional |  | 波动率跨期风险  
mr4 | string | Optional |  | 期权空头风险  
  
**risk_unit / items / margin_result / items / profit_loss_ranges**

mr1的33个压力场景测试结果

类型 | 约束  
---|---  
array |   
  
**risk_unit / items / margin_result / items / profit_loss_ranges / items**

盈亏范围

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price_percentage | string | Optional |  | 价格变动百分比  
implied_volatility_percentage | string | Optional |  | 隐含波动率变动百分比  
profit_loss | string | Optional |  | 盈亏  
      
    
    {
      "maintain_margin_total": "string",
      "initial_margin_total": "string",
      "calculate_time": 0,
      "risk_unit": [
        {
          "symbol": "string",
          "spot_in_use": "string",
          "maintain_margin": "string",
          "initial_margin": "string",
          "margin_result": [],
          "delta": "string",
          "gamma": "string",
          "theta": "string",
          "vega": "string"
        }
      ]
    }
    
    

##  UnifiedMarginTiers

统一账户借贷保证金梯度

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
margin_tiers | array | Optional |  | 阶梯式保证金  
  
**margin_tiers**

阶梯式保证金

类型 | 约束  
---|---  
array |   
  
**margin_tiers / items**

MarginTiers

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tier | string | Optional |  | 档位  
margin_rate | string | Optional |  | 保证金系数  
lower_limit | string | Optional |  | 下限  
upper_limit | string | Optional |  | 上限, ``表示大于(最后一个档位)  
leverage | string | Optional |  | 杠杆倍数  
      
    
    {
      "currency": "string",
      "margin_tiers": [
        {
          "tier": "string",
          "margin_rate": "string",
          "lower_limit": "string",
          "upper_limit": "string",
          "leverage": "string"
        }
      ]
    }
    
    

##  UnifiedHistoryLoanRate

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
tier | string | Optional |  | 需要获取的上浮费率的vip等级  
tier_up_rate | string | Optional |  | vip等级对应的上浮费率  
rates | array | Optional |  | 历史利率信息，每个整点小时一个数据，数组大小根据接口请求参数提供的page和limit参数确定，按照时间从近到远排序  
  
**rates**

历史利率信息，每个整点小时一个数据，数组大小根据接口请求参数提供的page和limit参数确定，按照时间从近到远排序

类型 | 约束  
---|---  
array |   
  
**rates / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional |  | 该利率对应的整点小时时间戳，单位为毫秒  
rate | string | Optional |  | 该整点小时的历史利率  
      
    
    {
      "currency": "string",
      "tier": "string",
      "tier_up_rate": "string",
      "rates": [
        {
          "time": 0,
          "rate": "string"
        }
      ]
    }
    
    

##  UnifiedBorrowable

UnifiedBorrowable

统一账户最多可借入额度

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种信息  
amount | string | Optional |  | 最多可借入的额度  
      
    
    {
      "currency": "string",
      "amount": "string"
    }
    
    

##  UnifiedDiscount

统一账户梯度discount

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
discount_tiers | array | Optional |  | 阶梯式discount  
  
**discount_tiers**

阶梯式discount

类型 | 约束  
---|---  
array |   
  
**discount_tiers / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tier | string | Optional |  | 档位  
discount | string | Optional |  | 保证金折扣系数  
lower_limit | string | Optional |  | 下限  
upper_limit | string | Optional |  | 上限, +表示正无穷  
leverage | string | Optional |  | 杠杆倍数  
      
    
    {
      "currency": "string",
      "discount_tiers": [
        {
          "tier": "string",
          "discount": "string",
          "lower_limit": "string",
          "upper_limit": "string",
          "leverage": "string"
        }
      ]
    }
    
    

##  UniLoan

借贷

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional | readOnly: true | 币种  
currency_pair | string | Optional | readOnly: true | 交易对  
amount | string | Optional | readOnly: true | 待归还数量  
type | string | Optional | readOnly: true | 借贷类型，平台借币 - platform，杠杆借币 - margin  
create_time | integer(int64) | Optional | readOnly: true | 创建时间戳  
update_time | integer(int64) | Optional | readOnly: true | 最近更新时间戳  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "amount": "string",
      "type": "string",
      "create_time": 0,
      "update_time": 0
    }
    
    

##  QuickEstimatedRepayment

QuickEstimatedRepayment

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
debt_currencies | array | Optional |  | 负债币种列表  
available_currencies | array | Optional |  | 可用于还款币种列表  
  
**debt_currencies**

负债币种列表

类型 | 约束  
---|---  
array |   
  
**debt_currencies / items**

UnifiedDebtCurrencies

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
debt_amount | string | Optional |  | 负债数量  
estimated_usd | string | Optional |  | 预估USD价值  
borrowed | string | Optional |  | 已借数量  
neg_balance | string | Optional |  | 负余额  
  
**available_currencies**

可用于还款币种列表

类型 | 约束  
---|---  
array |   
  
**available_currencies / items**

UnifiedAvailableCurrencies

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种名称  
available | string | Optional |  | 可用余额  
estimated_usd | string | Optional |  | 预估USD价值  
      
    
    {
      "debt_currencies": [
        {
          "currency": "string",
          "debt_amount": "string",
          "estimated_usd": "string",
          "borrowed": "string",
          "neg_balance": "string"
        }
      ],
      "available_currencies": [
        {
          "currency": "string",
          "available": "string",
          "estimated_usd": "string"
        }
      ]
    }
    
    

##  UniLoanInterestRecord

扣息记录

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional | readOnly: true | 币种名称  
currency_pair | string | Optional | readOnly: true | 交易对  
actual_rate | string | Optional | readOnly: true | 实际利率  
interest | string | Optional | readOnly: true | 利息  
status | integer | Optional | readOnly: true | 状态 0 - 失败 , 1 - 成功  
type | string | Optional | readOnly: true | 借贷类型，margin表示为杠杆借币  
create_time | integer(int64) | Optional | readOnly: true | 创建时间戳  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "actual_rate": "string",
      "interest": "string",
      "status": 0,
      "type": "string",
      "create_time": 0
    }
    
    

##  UnifiedTransferable

UnifiedTransferable

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种信息  
amount | string | Optional |  | 最多可转出的额度  
      
    
    {
      "currency": "string",
      "amount": "string"
    }
    
    

##  UnifiedLoanResult

统一账户借还款响应结果

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tran_id | integer(int64) | Optional |  | 交易id  
      
    
    {
      "tran_id": 0
    }
    
    

##  UnifiedLeverageConfig

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
current_leverage | string | Optional |  | 当前杠杆倍数  
min_leverage | string | Optional |  | 最小可调杠杆倍数  
max_leverage | string | Optional |  | 最大可调杠杆倍数  
debit | string | Optional |  | 当前负债  
available_margin | string | Optional |  | 可用保证金  
borrowable | string | Optional |  | 当前选择杠杆可借  
except_leverage_borrowable | string | Optional |  | 保证金最大可借、余币宝最大可借，两者取较小的值  
      
    
    {
      "current_leverage": "string",
      "min_leverage": "string",
      "max_leverage": "string",
      "debit": "string",
      "available_margin": "string",
      "borrowable": "string",
      "except_leverage_borrowable": "string"
    }
    
    

##  UnifiedModeSet

类型 | 约束  
---|---  
object | required: ["mode"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
mode | string | Required |  | 统一账户模式：   
\- `classic`: 经典账户模式   
\- `multi_currency`: 跨币种保证金模式   
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  
settings | object | Optional |  |   
  
**settings**

UnifiedSettings

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
usdt_futures | boolean | Optional |  | USDT合约开关。跨币种保证金模式下只能打开不能关闭  
spot_hedge | boolean | Optional |  | 现货对冲开关。  
use_funding | boolean | Optional |  | 余币宝开关，当mode为跨币种保证金模式时,是否将余币宝理财资金作为保证金  
options | boolean | Optional |  | 期权开关。跨币种保证金模式下只能打开不能关闭  
      
    
    {
      "mode": "string",
      "settings": {
        "usdt_futures": true,
        "spot_hedge": true,
        "use_funding": true,
        "options": true
      }
    }
    
    

##  EstimateRate

预估当前小时的借贷利率，按币种进行返回

类型 | 约束  
---|---  
object |   
  
**additionalProperties**

类型 | 约束  
---|---  
string |   
      
    
    {
      "property1": "string",
      "property2": "string"
    }
    
    

##  UnifiedCollateralRes

统一账户抵押模式设置返回

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
is_success | boolean | Optional |  | 是否设置成功  
      
    
    {
      "is_success": true
    }
    
    

##  QuickRepaymentResponse

QuickRepaymentResp

快捷还款信息

类型 | 约束  
---|---  
object | required: ["order_id","repaid_infos","used_infos"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Required |  | 订单ID  
repaid_infos | array | Required |  | 还款币种信息：currency 是币种名称，repaid 是已还款数量，left 是剩余负债数量。  
used_infos | array | Required |  | 用于还款的币种信息：currency 是币种名称，used 是已兑换数量。  
  
**repaid_infos**

还款币种信息：currency 是币种名称，repaid 是已还款数量，left 是剩余负债数量。

类型 | 约束  
---|---  
array |   
  
**repaid_infos / items**

RepaidInfo

还款信息

类型 | 约束  
---|---  
object | required: ["currency","repaid","left"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种名称  
repaid | string | Required |  | 已还款数量  
left | string | Required |  | 剩余负债数量  
  
**used_infos**

用于还款的币种信息：currency 是币种名称，used 是已兑换数量。

类型 | 约束  
---|---  
array |   
  
**used_infos / items**

UsedInfo

还款信息

类型 | 约束  
---|---  
object | required: ["currency","used"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种名称  
used | string | Required |  | 已兑换数量  
      
    
    {
      "order_id": "string",
      "repaid_infos": [
        {
          "currency": "string",
          "repaid": "string",
          "left": "string"
        }
      ],
      "used_infos": [
        {
          "currency": "string",
          "used": "string"
        }
      ]
    }
    
    

##  UnifiedLeverageSetting

借贷币种杠杆倍数

类型 | 约束  
---|---  
object | required: ["currency","leverage"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种名称  
leverage | string | Required |  | 倍数  
      
    
    {
      "currency": "string",
      "leverage": "string"
    }
    
    

##  UnifiedCollateralReq

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
collateral_type | integer | Optional | enum: [0,1] | 用户设置抵押物模式 0(all)-全部币种作为抵押物,1(custom)-自定义币种作为抵押物,collateral_type为0(all)时，enable_list与disable_list参数无效  
enable_list | array | Optional |  | 币种列表，collateral_type=1(custom)表示追加的逻辑  
disable_list | array | Optional |  | 取消列表，表示取消的逻辑  
  
**enable_list**

币种列表，collateral_type=1(custom)表示追加的逻辑

类型 | 约束  
---|---  
array |   
  
**enable_list / items**

类型 | 约束  
---|---  
string |   
  
**disable_list**

取消列表，表示取消的逻辑

类型 | 约束  
---|---  
array |   
  
**disable_list / items**

类型 | 约束  
---|---  
string |   
      
    
    {
      "collateral_type": 0,
      "enable_list": [
        "string"
      ],
      "disable_list": [
        "string"
      ]
    }
    
    

##  UnifiedPortfolioInput

组合保证金计算器输入

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
spot_balances | array | Optional |  | 现货  
spot_orders | array | Optional |  | 现货订单  
futures_positions | array | Optional |  | 合约仓位  
futures_orders | array | Optional |  | 合约订单  
options_positions | array | Optional |  | 期权仓位  
options_orders | array | Optional |  | 期权订单  
spot_hedge | boolean | Optional |  | 是否开启现货对冲  
  
**spot_balances**

现货

类型 | 约束  
---|---  
array |   
  
**spot_balances / items**

现货

类型 | 约束  
---|---  
object | required: ["currency","equity"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种名称  
equity | string | Required |  | 币种权益 = 余额 - 已借，表示现货净 Delta 敞口，可为负数。  
  
**spot_orders**

现货订单

类型 | 约束  
---|---  
array |   
  
**spot_orders / items**

现货订单

类型 | 约束  
---|---  
object | required: ["currency_pairs","order_price","size","left","type"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency_pairs | string | Required |  | 市场  
order_price | string | Required |  | 价格  
count | string | Optional |  | 现货交易对初始挂单数量，不参与实际计算。  
left | string | Required |  | 未成交数量，参与实际计算  
type | string | Required |  | 订单类型，sell - 卖出单，buy - 买入单  
  
**futures_positions**

合约仓位

类型 | 约束  
---|---  
array |   
  
**futures_positions / items**

合约仓位

类型 | 约束  
---|---  
object | required: ["contract","size"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
size | string | Required |  | 仓位大小，单位是张数  
  
**futures_orders**

合约订单

类型 | 约束  
---|---  
array |   
  
**futures_orders / items**

合约订单

类型 | 约束  
---|---  
object | required: ["contract","size","left"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
size | string | Required |  | 合约张数，为初始挂单数量，不参与实际结算  
left | string | Required |  | 未成交张数，参与实际计算  
  
**options_positions**

期权仓位

类型 | 约束  
---|---  
array |   
  
**options_positions / items**

期权仓位

类型 | 约束  
---|---  
object | required: ["options_name","size"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
options_name | string | Required |  | 期权合约市场名称，目前支持所有期权合约市场  
size | string | Required |  | 仓位大小，单位是张数  
  
**options_orders**

期权订单

类型 | 约束  
---|---  
array |   
  
**options_orders / items**

期权订单

类型 | 约束  
---|---  
object | required: ["options_name","size","left"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
options_name | string | Required |  | 期权合约市场名称，目前支持所有期权合约市场  
size | string | Required |  | 初始挂单张数，不参与实际计算  
left | string | Required |  | 未成交张数，参与实际计算  
      
    
    {
      "spot_balances": [
        {
          "currency": "string",
          "equity": "string"
        }
      ],
      "spot_orders": [
        {
          "currency_pairs": "string",
          "order_price": "string",
          "count": "string",
          "left": "string",
          "type": "string"
        }
      ],
      "futures_positions": [
        {
          "contract": "string",
          "size": "string"
        }
      ],
      "futures_orders": [
        {
          "contract": "string",
          "size": "string",
          "left": "string"
        }
      ],
      "options_positions": [
        {
          "options_name": "string",
          "size": "string"
        }
      ],
      "options_orders": [
        {
          "options_name": "string",
          "size": "string",
          "left": "string"
        }
      ],
      "spot_hedge": true
    }
    
    

##  UnifiedCurrency

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
name | string | Optional |  | 币种名称  
prec | string | Optional |  | 币种精度  
min_borrow_amount | string | Optional |  | 最小可借限额，单位是币  
user_max_borrow_amount | string | Optional |  | 用户最大可借限额，单位是 USDT  
total_max_borrow_amount | string | Optional |  | 平台最大可借限额，单位是 USDT  
loan_status | string | Optional |  | 是否借贷状态  
\- `disable` : 禁止借贷  
\- `enable` : 支持借贷  
      
    
    {
      "name": "string",
      "prec": "string",
      "min_borrow_amount": "string",
      "user_max_borrow_amount": "string",
      "total_max_borrow_amount": "string",
      "loan_status": "string"
    }
    
    

##  UnifiedRiskUnits

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | 用户 ID  
spot_hedge | boolean | Optional |  | 现货对冲状态, true - 启用，false - 未启用  
risk_units | array | Optional |  | 风险单元  
  
**risk_units**

风险单元

类型 | 约束  
---|---  
array |   
  
**risk_units / items**

RiskUnits

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 风险单元标志  
spot_in_use | string | Optional |  | 现货对冲占用数量  
maintain_margin | string | Optional |  | 风险单元的维持保证金  
initial_margin | string | Optional |  | 风险单元的起始保证金  
delta | string | Optional |  | 风险单元的 总 delta  
gamma | string | Optional |  | 风险单元的 总 gamma  
theta | string | Optional |  | 风险单元的 总 theta  
vega | string | Optional |  | 风险单元的 总 vega  
      
    
    {
      "user_id": 0,
      "spot_hedge": true,
      "risk_units": [
        {
          "symbol": "BTC_USDT",
          "spot_in_use": "string",
          "maintain_margin": "string",
          "initial_margin": "string",
          "delta": "string",
          "gamma": "string",
          "theta": "string",
          "vega": "string"
        }
      ]
    }
    
    

##  DeltaNeutralEnabled

DeltaNeutralEnabled

类型 | 约束  
---|---  
object | required: ["enabled"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
enabled | boolean | Required |  | 是否开启账户Delta中性策略模式  
      
    
    {
      "enabled": true
    }
    
    

##  UnifiedLoanRecord

借贷记录

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | id  
type | string | Optional | readOnly: true | 类型 , borrow - 借入 , repay - 还款  
repayment_type | string | Optional | readOnly: true | 还款类型 , none - 无还款类型, manual_repay - 手动还款 , auto_repay - 自动还款, cancel_auto_repay - 撤单后自动还款, different_currencies_repayment - 异币种还款  
borrow_type | string | Optional |  | 借款类型, 查询借款记录时返回，manual_borrow - 手动还款 , auto_borrow - 自动还款  
currency_pair | string | Optional | readOnly: true | 交易对  
currency | string | Optional | readOnly: true | 币种  
amount | string | Optional | readOnly: true | 借入或还款数量  
create_time | integer(int64) | Optional | readOnly: true | 创建时间戳  
      
    
    {
      "id": 0,
      "type": "string",
      "repayment_type": "string",
      "borrow_type": "string",
      "currency_pair": "string",
      "currency": "string",
      "amount": "string",
      "create_time": 0
    }
    
    

##  QuickRepaymentRequest

QuickRepaymentInfo

类型 | 约束  
---|---  
object | required: ["debt_currencies","available_currencies"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
debt_currencies | array | Required |  | 负债币种列表  
available_currencies | array | Required |  | 用于还款的币种列表  
  
**debt_currencies**

负债币种列表

类型 | 约束  
---|---  
array |   
  
**debt_currencies / items**

类型 | 约束  
---|---  
string |   
  
**available_currencies**

用于还款的币种列表

类型 | 约束  
---|---  
array |   
  
**available_currencies / items**

类型 | 约束  
---|---  
string |   
      
    
    {
      "debt_currencies": [
        "string"
      ],
      "available_currencies": [
        "string"
      ]
    }
    
    

##  GateErrorResponse

非 2xx 状态码时的异常描述信息

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
      
    
    {
      "label": "string",
      "message": "string"
    }
    
    

##  UnifiedAccount

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
mode | string | Optional |  | 统一账户模式：  
\- classic: 经典账户模式  
\- multi_currency: 跨币种保证金模式  
\- portfolio: 组合保证金模式  
\- single_currency: 单币种保证金模式  
user_id | integer(int64) | Optional |  | 用户 ID  
refresh_time | integer(int64) | Optional |  | 最近一次刷新时间  
locked | boolean | Optional |  | 账户是否被锁定：在跨币种保证金模式和组合保证金模式下有效；其他模式（如单币种保证金模式）下为 false。  
balances | object | Optional |  |   
total | string | Optional |  | 折算成 USD 的账户总资产，即所有币种 `(available + freeze) * price` 之和,(已废弃，待下线字段，用unified_account_total代替)  
borrowed | string | Optional |  | 折算成 USD 的账户总借入数量，即所有币种(不包括点卡)的 `borrowed * price` 之和,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_initial_margin | string | Optional |  | 总初始保证金(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_margin_balance | string | Optional |  | 总保证金余额(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_maintenance_margin | string | Optional |  | 总维持保证金(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_initial_margin_rate | string | Optional |  | 总初始保证金率(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_maintenance_margin_rate | string | Optional |  | 总维持保证金率(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
total_available_margin | string | Optional |  | 可用的保证金额度,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
unified_account_total | string | Optional |  | 统一账户总资产,单币种/跨币种模式下包括全仓总资产和逐仓总资产,组合保证金模式下只包括全仓总资产  
unified_account_total_liab | string | Optional |  | 统一账户总借贷,即全仓总借贷,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
unified_account_total_equity | string | Optional |  | 统一账户总权益,单币种/跨币种模式下包括全仓总权益和逐仓总权益,组合保证金模式下只包括全仓总权益  
leverage | string | Optional | readOnly: true | 账户杠杆倍数，在跨币种保证金/组合保证金模式下有效（已废弃）币种杠杆倍数查询接口：GET /unified/leverage/user_currency_setting  
spot_order_loss | string | Optional |  | 现货挂单损失，单位为USDT，只在跨币种模式和组合保证金模式下有效。  
options_order_loss | string | Optional |  | 期权挂单损失，单位为USDT，只在组合保证金模式下有效。  
spot_hedge | boolean | Optional |  | 现货对冲状态, true - 启用，false - 未启用  
use_funding | boolean | Optional |  | 是否将余币宝理财资金作为保证金  
is_all_collateral | boolean | Optional |  | 是否所有币种均作为保证金，true - 所有币种作为保证金，false - 否  
  
**balances**

类型 | 约束  
---|---  
object |   
  
**balances / additionalProperties**

UnifiedBalance

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
available | string | Optional |  | 全仓可用余额，已扣除合约逐仓占用及冻结（合约逐仓占用，即合约逐仓余额），在单币种/跨币种/组合保证金模式下有效。  
freeze | string | Optional |  | 被冻结的额度,在单币种保证金/跨币种保证金/组合保证金模式模式下有效  
borrowed | string | Optional |  | 借入额度,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
negative_liab | string | Optional |  | 负余额借贷,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
futures_pos_liab | string | Optional |  | 合约开仓借币(已废弃,待下线字段)  
equity | string | Optional |  | 币种权益数量（全仓）,在单币种保证金/跨币种保证金/组合保证金模式模式下有效  
total_freeze | string | Optional |  | 总占用(已废弃,待下线字段)  
total_liab | string | Optional |  | 总借款,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
spot_in_use | string | Optional |  | 现货对冲占用数量,在组合保证金模式下有效，其他如单币种、跨币种保证金模式下是0  
funding | string | Optional |  | 余币宝理财数量,在余币宝理财作为统一账户保证金开关打开有效  
funding_version | string | Optional |  | 余币宝理财版本号  
cross_balance | string | Optional |  | 全仓余额,在单币种保证金模式、跨币种保证金模式下有效，其他如组合保证金模式下是0  
iso_balance | string | Optional |  | 合约逐仓余额，在单币种保证金模式、跨币种保证金模式下有效，其他如组合保证金模式下是0  
im | string | Optional |  | 全仓初始保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
mm | string | Optional |  | 全仓维持保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
imr | string | Optional |  | 全仓初始保证金率,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
mmr | string | Optional |  | 全仓维持保证金率,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
margin_balance | string | Optional |  | 全仓保证金余额,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
available_margin | string | Optional |  | 全仓可用保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
enabled_collateral | boolean | Optional |  | 币种开启作为保证金，true - 启用，false - 未启用  
balance_version | number(int64) | Optional |  | 余额版本号  
      
    
    {
      "mode": "string",
      "user_id": 0,
      "refresh_time": 0,
      "locked": true,
      "balances": {
        "property1": {
          "available": "string",
          "freeze": "string",
          "borrowed": "string",
          "negative_liab": "string",
          "futures_pos_liab": "string",
          "equity": "string",
          "total_freeze": "string",
          "total_liab": "string",
          "spot_in_use": "string",
          "funding": "string",
          "funding_version": "string",
          "cross_balance": "string",
          "iso_balance": "string",
          "im": "string",
          "mm": "string",
          "imr": "string",
          "mmr": "string",
          "margin_balance": "string",
          "available_margin": "string",
          "enabled_collateral": true,
          "balance_version": 0
        },
        "property2": {
          "available": "string",
          "freeze": "string",
          "borrowed": "string",
          "negative_liab": "string",
          "futures_pos_liab": "string",
          "equity": "string",
          "total_freeze": "string",
          "total_liab": "string",
          "spot_in_use": "string",
          "funding": "string",
          "funding_version": "string",
          "cross_balance": "string",
          "iso_balance": "string",
          "im": "string",
          "mm": "string",
          "imr": "string",
          "mmr": "string",
          "margin_balance": "string",
          "available_margin": "string",
          "enabled_collateral": true,
          "balance_version": 0
        }
      },
      "total": "string",
      "borrowed": "string",
      "total_initial_margin": "string",
      "total_margin_balance": "string",
      "total_maintenance_margin": "string",
      "total_initial_margin_rate": "string",
      "total_maintenance_margin_rate": "string",
      "total_available_margin": "string",
      "unified_account_total": "string",
      "unified_account_total_liab": "string",
      "unified_account_total_equity": "string",
      "leverage": "string",
      "spot_order_loss": "string",
      "options_order_loss": "string",
      "spot_hedge": true,
      "use_funding": true,
      "is_all_collateral": true
    }
    
    

##  UnifiedLoan

借入或还款

类型 | 约束  
---|---  
object | required: ["currency","amount","type"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种  
type | string | Required | enum: ["borrow","repay"] | 类型 , borrow - 借入 , repay - 还款  
amount | string | Required |  | 借入或还款数量  
repaid_all | boolean | Optional |  | 全部还款，仅还款操作使用，为 `true` 时覆盖 `amount` ，直接全部还款  
text | string | Optional |  | 用户自定义 ID  
      
    
    {
      "currency": "string",
      "type": "borrow",
      "amount": "string",
      "repaid_all": true,
      "text": "string"
    }