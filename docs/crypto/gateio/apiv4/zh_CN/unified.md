---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/unified
api_type: Account
updated_at: 2026-05-27 20:18:04.003996
---

# Unified

统一账户

##  获取统一账户信息🔒 需要认证

GET`/unified/accounts`

GET `/unified/accounts`

_获取统一账户信息_

账户内的各币种资产将会根据其流动性，定义相应的调整系数，再统一折算为USD，来统一计算账户的资产及持仓价值

具体公式可查询保证金公式

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

名称 | 类型 | 描述  
---|---|---  
» mode | string | 统一账户模式：  
\- classic: 经典账户模式  
\- multi_currency: 跨币种保证金模式  
\- portfolio: 组合保证金模式  
\- single_currency: 单币种保证金模式  
» user_id | integer(int64) | 用户 ID  
» refresh_time | integer(int64) | 最近一次刷新时间  
» locked | boolean | 账户是否被锁定,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是false  
» balances | object |   
»» UnifiedBalance | object |   
»»» available | string | 全仓可用余额，已扣除合约逐仓占用及冻结（合约逐仓占用，即合约逐仓余额），在单币种/跨币种/组合保证金模式下有效。  
»»» freeze | string | 被冻结的额度,在单币种保证金/跨币种保证金/组合保证金模式模式下有效  
»»» borrowed | string | 借入额度,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»»» negative_liab | string | 负余额借贷,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»»» futures_pos_liab | string | 合约开仓借币(已废弃,待下线字段)  
»»» equity | string | 币种权益数量（全仓）,在单币种保证金/跨币种保证金/组合保证金模式模式下有效  
»»» total_freeze | string | 总占用(已废弃,待下线字段)  
»»» total_liab | string | 总借款,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»»» spot_in_use | string | 现货对冲占用数量,在组合保证金模式下有效，其他如单币种、跨币种保证金模式下是0  
»»» funding | string | 余币宝理财数量,在余币宝理财作为统一账户保证金开关打开有效  
»»» funding_version | string | 余币宝理财版本号  
»»» cross_balance | string | 全仓余额,在单币种保证金模式、跨币种保证金模式下有效，其他如组合保证金模式下是0  
»»» iso_balance | string | 合约逐仓余额，在单币种保证金模式、跨币种保证金模式下有效，其他如组合保证金模式下是0  
»»» im | string | 全仓初始保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»»» mm | string | 全仓维持保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»»» imr | string | 全仓初始保证金率,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»»» mmr | string | 全仓维持保证金率,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»»» margin_balance | string | 全仓保证金余额,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»»» available_margin | string | 全仓可用保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»»» enabled_collateral | boolean | 币种开启作为保证金，true - 启用，false - 未启用  
»»» balance_version | number(int64) | 余额版本号  
»» total | string | 折算成 USD 的账户总资产，即所有币种 `(available + freeze) * price` 之和,(已废弃，待下线字段，用unified_account_total代替)  
»» borrowed | string | 折算成 USD 的账户总借入数量，即所有币种(不包括点卡)的 `borrowed * price` 之和,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» total_initial_margin | string | 总初始保证金(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» total_margin_balance | string | 总保证金余额(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» total_maintenance_margin | string | 总维持保证金(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» total_initial_margin_rate | string | 总初始保证金率(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» total_maintenance_margin_rate | string | 总维持保证金率(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» total_available_margin | string | 可用的保证金额度,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» unified_account_total | string | 统一账户总资产,单币种/跨币种模式下包括全仓总资产和逐仓总资产,组合保证金模式下只包括全仓总资产  
»» unified_account_total_liab | string | 统一账户总借贷,即全仓总借贷,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» unified_account_total_equity | string | 统一账户总权益,单币种/跨币种模式下包括全仓总权益和逐仓总权益,组合保证金模式下只包括全仓总权益  
»» leverage | string | 账户杠杆倍数，在跨币种保证金/组合保证金模式下有效（已废弃）币种杠杆倍数查询接口：GET /unified/leverage/user_currency_setting  
»» spot_order_loss | string | 现货挂单损失，单位为USDT，只在跨币种模式和组合保证金模式下有效。  
»» options_order_loss | string | 期权挂单损失，单位为USDT，只在组合保证金模式下有效。  
»» spot_hedge | boolean | 现货对冲状态, true - 启用，false - 未启用  
»» use_funding | boolean | 是否将余币宝理财资金作为保证金  
»» is_all_collateral | boolean | 是否所有币种均作为保证金，true - 所有币种作为保证金，false - 否  
  
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

_UnifiedBorrowable_

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种信息  
» amount | string | 最多可借入的额度  
  
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

_UnifiedTransferable_

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种信息  
» amount | string | 最多可转出的额度  
  
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
    

##  批量查询统一账户最多可转出；每一个币种都是最大值, 用户提币之后, 所有币种可转金额都会变更🔒 需要认证

GET`/unified/transferables`

GET `/unified/transferables`

_批量查询统一账户最多可转出；每一个币种都是最大值, 用户提币之后, 所有币种可转金额都会变更_

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

名称 | 类型 | 描述  
---|---|---  
» TransferablesResult | object | 批量查询统一账户最多可转出结果  
»» currency | string | 币种信息  
»» amount | string | 最多可转出的额度  
  
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

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [统一账户最多可借入额度]  
» UnifiedBorrowable | UnifiedBorrowable | 统一账户最多可借入额度  
»» currency | string | 币种信息  
»» amount | string | 最多可借入的额度  
  
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
» currency | body | string | 是 | 币种  
» type | body | string | 是 | 类型 , borrow - 借入 , repay - 还款  
» amount | body | string | 是 | 借入或还款数量  
» repaid_all | body | boolean | 否 | 全部还款，仅还款操作使用，为 `true` 时覆盖 `amount` ，直接全部还款  
» text | body | string | 否 | 用户自定义 ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» type | borrow  
» type | repay  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 操作成功 | UnifiedLoanResult  
  
### 返回格式

状态码 **200**

_统一账户借还款响应结果_

名称 | 类型 | 描述  
---|---|---  
» tran_id | integer(int64) | 交易id  
  
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

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [借贷记录]  
» _None_ | UnifiedLoanRecord | 借贷记录  
»» id | integer(int64) | id  
»» type | string | 类型 , borrow - 借入 , repay - 还款  
»» repayment_type | string | 还款类型 , none - 无还款类型, manual_repay - 手动还款 , auto_repay - 自动还款, cancel_auto_repay - 撤单后自动还款, different_currencies_repayment - 异币种还款  
»» borrow_type | string | 借款类型, 查询借款记录时返回，manual_borrow - 手动还款 , auto_borrow - 自动还款  
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

名称 | 类型 | 描述  
---|---|---  
» user_id | integer(int64) | 用户 ID  
» spot_hedge | boolean | 现货对冲状态, true - 启用，false - 未启用  
» risk_units | array | 风险单元  
»» RiskUnits | object |   
»»» symbol | string | 风险单元标志  
»»» spot_in_use | string | 现货对冲占用数量  
»»» maintain_margin | string | 风险单元的维持保证金  
»»» initial_margin | string | 风险单元的起始保证金  
»»» delta | string | 风险单元的 总 delta  
»»» gamma | string | 风险单元的 总 gamma  
»»» theta | string | 风险单元的 总 theta  
»»» vega | string | 风险单元的 总 vega  
  
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

名称 | 类型 | 描述  
---|---|---  
» mode | string | 统一账户模式：   
\- `classic`: 经典账户模式   
\- `multi_currency`: 跨币种保证金模式   
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  
» settings | object |   
»» usdt_futures | boolean | USDT合约开关。跨币种保证金模式下只能打开不能关闭  
»» spot_hedge | boolean | 现货对冲开关。  
»» use_funding | boolean | 余币宝开关，当mode为跨币种保证金模式时,是否将余币宝理财资金作为保证金  
»» options | boolean | 期权开关。跨币种保证金模式下只能打开不能关闭  
  
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
» mode | body | string | 是 | 统一账户模式：   
\- `classic`: 经典账户模式   
\- `multi_currency`: 跨币种保证金模式   
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  
» settings | body | object | 否 |   
»» usdt_futures | body | boolean | 否 | USDT合约开关。跨币种保证金模式下只能打开不能关闭  
»» spot_hedge | body | boolean | 否 | 现货对冲开关。  
»» use_funding | body | boolean | 否 | 余币宝开关，当mode为跨币种保证金模式时,是否将余币宝理财资金作为保证金  
»» options | body | boolean | 否 | 期权开关。跨币种保证金模式下只能打开不能关闭  
  
####  详细描述

**» mode** : 统一账户模式：   
\- `classic`: 经典账户模式   
\- `multi_currency`: 跨币种保证金模式   
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式

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
    

##  查询统一账户梯度式

GET`/unified/currency_discount_tiers`

GET `/unified/currency_discount_tiers`

_查询统一账户梯度式_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [UnifiedDiscount]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [统一账户梯度discount]  
» _None_ | UnifiedDiscount | 统一账户梯度discount  
»» currency | string | 币种名称  
»» discount_tiers | array | 阶梯式discount  
»»» tier | string | 档位  
»»» discount | string | 保证金折扣系数  
»»» lower_limit | string | 下限  
»»» upper_limit | string | 上限, +表示正无穷  
»»» leverage | string | 杠杆倍数  
  
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

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [统一账户借贷保证金梯度]  
» _None_ | UnifiedMarginTiers | 统一账户借贷保证金梯度  
»» currency | string | 币种名称  
»» margin_tiers | array | 阶梯式保证金  
»»» MarginTiers | object |   
»»»» tier | string | 档位  
»»»» margin_rate | string | 保证金系数  
»»»» lower_limit | string | 下限  
»»»» upper_limit | string | 上限, ``表示大于(最后一个档位)  
»»»» leverage | string | 杠杆倍数  
  
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
» spot_balances | body | array | 否 | 现货  
»» _None_ | body | object | 否 | 现货  
»»» currency | body | string | 是 | 币种名称  
»»» equity | body | string | 是 | 币种权益，权益 = 余额 - 已借，表示您在现货部位的净delta敞口，可以为负数。  
»» spot_orders | body | array | 否 | 现货订单  
»»» _None_ | body | object | 否 | 现货订单  
»»»» currency_pairs | body | string | 是 | 市场  
»»»» order_price | body | string | 是 | 价格  
»»»» count | body | string | 否 | 现货交易对初始挂单数量，不参与实际计算。  
»»»» left | body | string | 是 | 未成交数量，参与实际计算  
»»»» type | body | string | 是 | 订单类型，sell - 卖出单，buy - 买入单  
»»» futures_positions | body | array | 否 | 合约仓位  
»»»» _None_ | body | object | 否 | 合约仓位  
»»»»» contract | body | string | 是 | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
»»»»» size | body | string | 是 | 仓位大小，单位是张数  
»»»» futures_orders | body | array | 否 | 合约订单  
»»»»» _None_ | body | object | 否 | 合约订单  
»»»»»» contract | body | string | 是 | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
»»»»»» size | body | string | 是 | 合约张数，为初始挂单数量，不参与实际结算  
»»»»»» left | body | string | 是 | 未成交张数，参与实际计算  
»»»»» options_positions | body | array | 否 | 期权仓位  
»»»»»» _None_ | body | object | 否 | 期权仓位  
»»»»»»» options_name | body | string | 是 | 期权合约市场名称，目前支持所有期权合约市场  
»»»»»»» size | body | string | 是 | 仓位大小，单位是张数  
»»»»»» options_orders | body | array | 否 | 期权订单  
»»»»»»» _None_ | body | object | 否 | 期权订单  
»»»»»»»» options_name | body | string | 是 | 期权合约市场名称，目前支持所有期权合约市场  
»»»»»»»» size | body | string | 是 | 初始挂单张数，不参与实际计算  
»»»»»»»» left | body | string | 是 | 未成交张数，参与实际计算  
»»»»»»» spot_hedge | body | boolean | 否 | 是否开启现货对冲  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | UnifiedPortfolioOutput  
  
### 返回格式

状态码 **200**

_组合保证金计算器输出_

名称 | 类型 | 描述  
---|---|---  
» maintain_margin_total | string | 总维持保证金，只包含risk unit的仓位的组合保证金计算结果，不包含借币保证金。如果存在借币，实际还会产生常规的借币保证金要求。  
» initial_margin_total | string | 总起始保证金，为以下三个组合的最大计算结果：仓位、仓位+正delta挂单、仓位+负delta挂单  
» calculate_time | integer(int64) | 计算时间  
» risk_unit | array | 风险单元  
»» _None_ | object | 风险单元  
»»» symbol | string | 风险单元名称  
»»» spot_in_use | string | 现货对冲使用量  
»»» maintain_margin | string | 维持保证金  
»»» initial_margin | string | 起始保证金  
»»» margin_result | array | 保证金结果  
»»»» _None_ | object | 保证金结果  
»»»»» type | string | 仓位组合类型  
`original_position` \- 原始仓位  
`long_delta_original_position` \- 正向delta+原始仓位  
`short_delta_original_position` \- 负向delta+原始仓位  
»»»»» profit_loss_ranges | array | mr1的33个压力场景测试结果  
»»»»»» _None_ | UnifiedPortfolioOutput/properties/risk_unit/items/properties/margin_result/items/properties/profit_loss_ranges/items | 盈亏范围  
»»»»»»» price_percentage | string | 价格变动百分比  
»»»»»»» implied_volatility_percentage | string | 隐含波动率变动百分比  
»»»»»»» profit_loss | string | 盈亏  
»»»»»» max_loss | UnifiedPortfolioOutput/properties/risk_unit/items/properties/margin_result/items/properties/profit_loss_ranges/items | 盈亏范围  
»»»»»»» price_percentage | string | 价格变动百分比  
»»»»»»» implied_volatility_percentage | string | 隐含波动率变动百分比  
»»»»»»» profit_loss | string | 盈亏  
»»»»»» mr1 | string | 压力测试  
»»»»»» mr2 | string | 基差跨期风险  
»»»»»» mr3 | string | 波动率跨期风险  
»»»»»» mr4 | string | 期权空头风险  
»»»»» delta | string | 风险单元的 总 delta  
»»»»» gamma | string | 风险单元的 总 gamma  
»»»»» theta | string | 风险单元的 总 theta  
»»»»» vega | string | 风险单元的 总 vega  
  
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

名称 | 类型 | 描述  
---|---|---  
» current_leverage | string | 当前杠杆倍数  
» min_leverage | string | 最小可调杠杆倍数  
» max_leverage | string | 最大可调杠杆倍数  
» debit | string | 当前负债  
» available_margin | string | 可用保证金  
» borrowable | string | 当前选择杠杆可借  
» except_leverage_borrowable | string | 保证金最大可借、余币宝最大可借，两者取较小的值  
  
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

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [借贷币种杠杆倍数]  
» _None_ | UnifiedLeverageSetting | 借贷币种杠杆倍数  
»» currency | string | 币种名称  
»» leverage | string | 倍数  
  
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
» currency | body | string | 是 | 币种名称  
» leverage | body | string | 是 | 倍数  
  
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

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» name | string | 币种名称  
» prec | string | 币种精度  
» min_borrow_amount | string | 最小可借限额，单位是币  
» user_max_borrow_amount | string | 用户最大可借限额，单位是 USDT  
» total_max_borrow_amount | string | 平台最大可借限额，单位是 USDT  
» loan_status | string | 是否借贷状态  
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

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种名称  
» tier | string | 需要获取的上浮费率的vip等级  
» tier_up_rate | string | vip等级对应的上浮费率  
» rates | array | 历史利率信息，每个整点小时一个数据，数组大小根据接口请求参数提供的page和limit参数确定，按照时间从近到远排序  
»» time | integer(int64) | 该利率对应的整点小时时间戳，单位为毫秒  
»» rate | string | 该整点小时的历史利率  
  
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
» collateral_type | body | integer | 否 | 用户设置抵押物模式 0(all)-全部币种作为抵押物,1(custom)-自定义币种作为抵押物,collateral_type为0(all)时，enable_list与disable_list参数无效  
» enable_list | body | array | 否 | 币种列表，collateral_type=1(custom)表示追加的逻辑  
» disable_list | body | array | 否 | 取消列表，表示取消的逻辑  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» collateral_type | 0  
» collateral_type | 1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 更新成功 | UnifiedCollateralRes  
  
### 返回格式

状态码 **200**

_统一账户抵押模式设置返回_

名称 | 类型 | 描述  
---|---|---  
» is_success | boolean | 是否设置成功  
  
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

_QuickEstimatedRepayment_

名称 | 类型 | 描述  
---|---|---  
» debt_currencies | array | 负债币种列表  
»» UnifiedDebtCurrencies | object |   
»»» currency | string | 币种名称  
»»» debt_amount | string | 负债数量  
»»» estimated_usd | string | 预估USD价值  
»»» borrowed | string | 已借数量  
»»» neg_balance | string | 负余额  
»» available_currencies | array | 可用于还款币种列表  
»»» UnifiedAvailableCurrencies | object |   
»»»» currency | string | 币种名称  
»»»» available | string | 可用余额  
»»»» estimated_usd | string | 预估USD价值  
  
状态码 **400**

_非 2xx 状态码时的异常描述信息_

名称 | 类型 | 描述  
---|---|---  
» label | string | 错误标识符  
» message | string | 详细错误描述  
  
状态码 **401**

_非 2xx 状态码时的异常描述信息_

名称 | 类型 | 描述  
---|---|---  
» label | string | 错误标识符  
» message | string | 详细错误描述  
  
状态码 **403**

_非 2xx 状态码时的异常描述信息_

名称 | 类型 | 描述  
---|---|---  
» label | string | 错误标识符  
» message | string | 详细错误描述  
  
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
» debt_currencies | body | array | 是 | 负债币种列表  
» available_currencies | body | array | 是 | 用于还款的币种列表  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 还款成功 | QuickRepaymentResponse  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求参数错误 | GateErrorResponse  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | 认证失败 | GateErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 拒绝访问（如账户模式不支持快捷还款） | GateErrorResponse  
  
### 返回格式

状态码 **200**

_QuickRepaymentResp_

名称 | 类型 | 描述  
---|---|---  
» order_id | string | 订单ID  
» repaid_infos | array | 还款币种信息  
»» RepaidInfo | object | 还款信息  
»»» currency | string | 币种名称  
»»» repaid | string | 已还款数量  
»»» left | string | 剩余负债数量  
»» used_infos | array | 用于还款币种信息  
»»» UsedInfo | object | 还款信息  
»»»» currency | string | 币种名称  
»»»» used | string | 已兑换数量  
  
状态码 **400**

_非 2xx 状态码时的异常描述信息_

名称 | 类型 | 描述  
---|---|---  
» label | string | 错误标识符  
» message | string | 详细错误描述  
  
状态码 **401**

_非 2xx 状态码时的异常描述信息_

名称 | 类型 | 描述  
---|---|---  
» label | string | 错误标识符  
» message | string | 详细错误描述  
  
状态码 **403**

_非 2xx 状态码时的异常描述信息_

名称 | 类型 | 描述  
---|---|---  
» label | string | 错误标识符  
» message | string | 详细错误描述  
  
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
    

#  模型

##  UnifiedAccount

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
mode | string | false | none | 统一账户模式：  
\- classic: 经典账户模式  
\- multi_currency: 跨币种保证金模式  
\- portfolio: 组合保证金模式  
\- single_currency: 单币种保证金模式  
user_id | integer(int64) | false | none | 用户 ID  
refresh_time | integer(int64) | false | none | 最近一次刷新时间  
locked | boolean | false | none | 账户是否被锁定,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是false  
balances | object | false | none | none  
» UnifiedBalance | object | false | none | none  
»» available | string | false | none | 全仓可用余额，已扣除合约逐仓占用及冻结（合约逐仓占用，即合约逐仓余额），在单币种/跨币种/组合保证金模式下有效。  
»» freeze | string | false | none | 被冻结的额度,在单币种保证金/跨币种保证金/组合保证金模式模式下有效  
»» borrowed | string | false | none | 借入额度,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» negative_liab | string | false | none | 负余额借贷,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» futures_pos_liab | string | false | none | 合约开仓借币(已废弃,待下线字段)  
»» equity | string | false | none | 币种权益数量（全仓）,在单币种保证金/跨币种保证金/组合保证金模式模式下有效  
»» total_freeze | string | false | none | 总占用(已废弃,待下线字段)  
»» total_liab | string | false | none | 总借款,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
»» spot_in_use | string | false | none | 现货对冲占用数量,在组合保证金模式下有效，其他如单币种、跨币种保证金模式下是0  
»» funding | string | false | none | 余币宝理财数量,在余币宝理财作为统一账户保证金开关打开有效  
»» funding_version | string | false | none | 余币宝理财版本号  
»» cross_balance | string | false | none | 全仓余额,在单币种保证金模式、跨币种保证金模式下有效，其他如组合保证金模式下是0  
»» iso_balance | string | false | none | 合约逐仓余额，在单币种保证金模式、跨币种保证金模式下有效，其他如组合保证金模式下是0  
»» im | string | false | none | 全仓初始保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»» mm | string | false | none | 全仓维持保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»» imr | string | false | none | 全仓初始保证金率,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»» mmr | string | false | none | 全仓维持保证金率,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»» margin_balance | string | false | none | 全仓保证金余额,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»» available_margin | string | false | none | 全仓可用保证金,在单币种保证金模式下的仅对USDT有效，其他如跨币种保证金/组合保证金模式下是0  
»» enabled_collateral | boolean | false | none | 币种开启作为保证金，true - 启用，false - 未启用  
»» balance_version | number(int64) | false | none | 余额版本号  
» total | string | false | none | 折算成 USD 的账户总资产，即所有币种 `(available + freeze) * price` 之和,(已废弃，待下线字段，用unified_account_total代替)  
» borrowed | string | false | none | 折算成 USD 的账户总借入数量，即所有币种(不包括点卡)的 `borrowed * price` 之和,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
» total_initial_margin | string | false | none | 总初始保证金(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
» total_margin_balance | string | false | none | 总保证金余额(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
» total_maintenance_margin | string | false | none | 总维持保证金(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
» total_initial_margin_rate | string | false | none | 总初始保证金率(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
» total_maintenance_margin_rate | string | false | none | 总维持保证金率(全仓),在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
» total_available_margin | string | false | none | 可用的保证金额度,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
» unified_account_total | string | false | none | 统一账户总资产,单币种/跨币种模式下包括全仓总资产和逐仓总资产,组合保证金模式下只包括全仓总资产  
» unified_account_total_liab | string | false | none | 统一账户总借贷,即全仓总借贷,在跨币种保证金/组合保证金模式下有效，其他如单币种保证金模式下是0  
» unified_account_total_equity | string | false | none | 统一账户总权益,单币种/跨币种模式下包括全仓总权益和逐仓总权益,组合保证金模式下只包括全仓总权益  
» leverage | string | false | 只读 | 账户杠杆倍数，在跨币种保证金/组合保证金模式下有效（已废弃）币种杠杆倍数查询接口：GET /unified/leverage/user_currency_setting  
» spot_order_loss | string | false | none | 现货挂单损失，单位为USDT，只在跨币种模式和组合保证金模式下有效。  
» options_order_loss | string | false | none | 期权挂单损失，单位为USDT，只在组合保证金模式下有效。  
» spot_hedge | boolean | false | none | 现货对冲状态, true - 启用，false - 未启用  
» use_funding | boolean | false | none | 是否将余币宝理财资金作为保证金  
» is_all_collateral | boolean | false | none | 是否所有币种均作为保证金，true - 所有币种作为保证金，false - 否  
      
    
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

_借入或还款_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | true | none | 币种  
type | string | true | none | 类型 , borrow - 借入 , repay - 还款  
amount | string | true | none | 借入或还款数量  
repaid_all | boolean | false | none | 全部还款，仅还款操作使用，为 `true` 时覆盖 `amount` ，直接全部还款  
text | string | false | none | 用户自定义 ID  
  
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
      "text": "string"
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
    
    

##  UnifiedBorrowable

_UnifiedBorrowable_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种信息  
amount | string | false | none | 最多可借入的额度  
      
    
    {
      "currency": "string",
      "amount": "string"
    }
    
    

##  UnifiedLeverageSetting

_借贷币种杠杆倍数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | true | none | 币种名称  
leverage | string | true | none | 倍数  
      
    
    {
      "currency": "string",
      "leverage": "string"
    }
    
    

##  UnifiedLeverageConfig

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
current_leverage | string | false | none | 当前杠杆倍数  
min_leverage | string | false | none | 最小可调杠杆倍数  
max_leverage | string | false | none | 最大可调杠杆倍数  
debit | string | false | none | 当前负债  
available_margin | string | false | none | 可用保证金  
borrowable | string | false | none | 当前选择杠杆可借  
except_leverage_borrowable | string | false | none | 保证金最大可借、余币宝最大可借，两者取较小的值  
      
    
    {
      "current_leverage": "string",
      "min_leverage": "string",
      "max_leverage": "string",
      "debit": "string",
      "available_margin": "string",
      "borrowable": "string",
      "except_leverage_borrowable": "string"
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
    
    

##  QuickRepaymentRequest

_QuickRepaymentInfo_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
debt_currencies | array | true | none | 负债币种列表  
available_currencies | array | true | none | 用于还款的币种列表  
      
    
    {
      "debt_currencies": [
        "string"
      ],
      "available_currencies": [
        "string"
      ]
    }
    
    

##  QuickEstimatedRepayment

_QuickEstimatedRepayment_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
debt_currencies | array | false | none | 负债币种列表  
» UnifiedDebtCurrencies | object | false | none | none  
»» currency | string | false | none | 币种名称  
»» debt_amount | string | false | none | 负债数量  
»» estimated_usd | string | false | none | 预估USD价值  
»» borrowed | string | false | none | 已借数量  
»» neg_balance | string | false | none | 负余额  
» available_currencies | array | false | none | 可用于还款币种列表  
»» UnifiedAvailableCurrencies | object | false | none | none  
»»» currency | string | false | none | 币种名称  
»»» available | string | false | none | 可用余额  
»»» estimated_usd | string | false | none | 预估USD价值  
      
    
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
    
    

##  UnifiedCollateralRes

_统一账户抵押模式设置返回_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
is_success | boolean | false | none | 是否设置成功  
      
    
    {
      "is_success": true
    }
    
    

##  UnifiedPortfolioInput

_组合保证金计算器输入_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
spot_balances | array | false | none | 现货  
» _None_ | object | false | none | 现货  
»» currency | string | true | none | 币种名称  
»» equity | string | true | none | 币种权益，权益 = 余额 - 已借，表示您在现货部位的净delta敞口，可以为负数。  
» spot_orders | array | false | none | 现货订单  
»» _None_ | object | false | none | 现货订单  
»»» currency_pairs | string | true | none | 市场  
»»» order_price | string | true | none | 价格  
»»» count | string | false | none | 现货交易对初始挂单数量，不参与实际计算。  
»»» left | string | true | none | 未成交数量，参与实际计算  
»»» type | string | true | none | 订单类型，sell - 卖出单，buy - 买入单  
»» futures_positions | array | false | none | 合约仓位  
»»» _None_ | object | false | none | 合约仓位  
»»»» contract | string | true | none | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
»»»» size | string | true | none | 仓位大小，单位是张数  
»»» futures_orders | array | false | none | 合约订单  
»»»» _None_ | object | false | none | 合约订单  
»»»»» contract | string | true | none | 永续合约名，只支持已开放期权交易的标的物的USDT永续合约  
»»»»» size | string | true | none | 合约张数，为初始挂单数量，不参与实际结算  
»»»»» left | string | true | none | 未成交张数，参与实际计算  
»»»» options_positions | array | false | none | 期权仓位  
»»»»» _None_ | object | false | none | 期权仓位  
»»»»»» options_name | string | true | none | 期权合约市场名称，目前支持所有期权合约市场  
»»»»»» size | string | true | none | 仓位大小，单位是张数  
»»»»» options_orders | array | false | none | 期权订单  
»»»»»» _None_ | object | false | none | 期权订单  
»»»»»»» options_name | string | true | none | 期权合约市场名称，目前支持所有期权合约市场  
»»»»»»» size | string | true | none | 初始挂单张数，不参与实际计算  
»»»»»»» left | string | true | none | 未成交张数，参与实际计算  
»»»»»» spot_hedge | boolean | false | none | 是否开启现货对冲  
      
    
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
    
    

##  UnifiedHistoryLoanRate

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种名称  
tier | string | false | none | 需要获取的上浮费率的vip等级  
tier_up_rate | string | false | none | vip等级对应的上浮费率  
rates | array | false | none | 历史利率信息，每个整点小时一个数据，数组大小根据接口请求参数提供的page和limit参数确定，按照时间从近到远排序  
» time | integer(int64) | false | none | 该利率对应的整点小时时间戳，单位为毫秒  
» rate | string | false | none | 该整点小时的历史利率  
      
    
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
    
    

##  UnifiedModeSet

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
mode | string | true | none | 统一账户模式：   
\- `classic`: 经典账户模式   
\- `multi_currency`: 跨币种保证金模式   
\- `portfolio`: 组合保证金模式  
\- `single_currency`: 单币种保证金模式  
settings | object | false | none | none  
» usdt_futures | boolean | false | none | USDT合约开关。跨币种保证金模式下只能打开不能关闭  
» spot_hedge | boolean | false | none | 现货对冲开关。  
» use_funding | boolean | false | none | 余币宝开关，当mode为跨币种保证金模式时,是否将余币宝理财资金作为保证金  
» options | boolean | false | none | 期权开关。跨币种保证金模式下只能打开不能关闭  
      
    
    {
      "mode": "string",
      "settings": {
        "usdt_futures": true,
        "spot_hedge": true,
        "use_funding": true,
        "options": true
      }
    }
    
    

##  UnifiedMarginTiers

_统一账户借贷保证金梯度_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种名称  
margin_tiers | array | false | none | 阶梯式保证金  
» MarginTiers | object | false | none | none  
»» tier | string | false | none | 档位  
»» margin_rate | string | false | none | 保证金系数  
»» lower_limit | string | false | none | 下限  
»» upper_limit | string | false | none | 上限, ``表示大于(最后一个档位)  
»» leverage | string | false | none | 杠杆倍数  
      
    
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
    
    

##  UnifiedLoanRecord

_借贷记录_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | 只读 | id  
type | string | false | 只读 | 类型 , borrow - 借入 , repay - 还款  
repayment_type | string | false | 只读 | 还款类型 , none - 无还款类型, manual_repay - 手动还款 , auto_repay - 自动还款, cancel_auto_repay - 撤单后自动还款, different_currencies_repayment - 异币种还款  
borrow_type | string | false | none | 借款类型, 查询借款记录时返回，manual_borrow - 手动还款 , auto_borrow - 自动还款  
currency_pair | string | false | 只读 | 交易对  
currency | string | false | 只读 | 币种  
amount | string | false | 只读 | 借入或还款数量  
create_time | integer(int64) | false | 只读 | 创建时间戳  
      
    
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
    
    

##  UnifiedPortfolioOutput

_组合保证金计算器输出_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
maintain_margin_total | string | false | none | 总维持保证金，只包含risk unit的仓位的组合保证金计算结果，不包含借币保证金。如果存在借币，实际还会产生常规的借币保证金要求。  
initial_margin_total | string | false | none | 总起始保证金，为以下三个组合的最大计算结果：仓位、仓位+正delta挂单、仓位+负delta挂单  
calculate_time | integer(int64) | false | none | 计算时间  
risk_unit | array | false | none | 风险单元  
» _None_ | object | false | none | 风险单元  
»» symbol | string | false | none | 风险单元名称  
»» spot_in_use | string | false | none | 现货对冲使用量  
»» maintain_margin | string | false | none | 维持保证金  
»» initial_margin | string | false | none | 起始保证金  
»» margin_result | array | false | none | 保证金结果  
»»» _None_ | object | false | none | 保证金结果  
»»»» type | string | false | none | 仓位组合类型  
`original_position` \- 原始仓位  
`long_delta_original_position` \- 正向delta+原始仓位  
`short_delta_original_position` \- 负向delta+原始仓位  
»»»» profit_loss_ranges | array | false | none | mr1的33个压力场景测试结果  
»»»»» _None_ | object | false | none | 盈亏范围  
»»»»»» price_percentage | string | false | none | 价格变动百分比  
»»»»»» implied_volatility_percentage | string | false | none | 隐含波动率变动百分比  
»»»»»» profit_loss | string | false | none | 盈亏  
»»»»» max_loss | UnifiedPortfolioOutput/properties/risk_unit/items/properties/margin_result/items/properties/profit_loss_ranges/items | false | none | 盈亏范围  
»»»»» mr1 | string | false | none | 压力测试  
»»»»» mr2 | string | false | none | 基差跨期风险  
»»»»» mr3 | string | false | none | 波动率跨期风险  
»»»»» mr4 | string | false | none | 期权空头风险  
»»»» delta | string | false | none | 风险单元的 总 delta  
»»»» gamma | string | false | none | 风险单元的 总 gamma  
»»»» theta | string | false | none | 风险单元的 总 theta  
»»»» vega | string | false | none | 风险单元的 总 vega  
      
    
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
    
    

##  UnifiedCollateralReq

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
collateral_type | integer | false | none | 用户设置抵押物模式 0(all)-全部币种作为抵押物,1(custom)-自定义币种作为抵押物,collateral_type为0(all)时，enable_list与disable_list参数无效  
enable_list | array | false | none | 币种列表，collateral_type=1(custom)表示追加的逻辑  
disable_list | array | false | none | 取消列表，表示取消的逻辑  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
collateral_type | 0  
collateral_type | 1  
      
    
    {
      "collateral_type": 0,
      "enable_list": [
        "string"
      ],
      "disable_list": [
        "string"
      ]
    }
    
    

##  QuickRepaymentResponse

_QuickRepaymentResp_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | true | none | 订单ID  
repaid_infos | array | true | none | 还款币种信息  
» RepaidInfo | object | false | none | 还款信息  
»» currency | string | true | none | 币种名称  
»» repaid | string | true | none | 已还款数量  
»» left | string | true | none | 剩余负债数量  
» used_infos | array | true | none | 用于还款币种信息  
»» UsedInfo | object | false | none | 还款信息  
»»» currency | string | true | none | 币种名称  
»»» used | string | true | none | 已兑换数量  
      
    
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
    
    

##  UnifiedLoanResult

_统一账户借还款响应结果_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
tran_id | integer(int64) | false | none | 交易id  
      
    
    {
      "tran_id": 0
    }
    
    

##  GateErrorResponse

_非 2xx 状态码时的异常描述信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
label | string | false | none | 错误标识符  
message | string | false | none | 详细错误描述  
      
    
    {
      "label": "string",
      "message": "string"
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
    
    

##  UnifiedRiskUnits

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user_id | integer(int64) | false | none | 用户 ID  
spot_hedge | boolean | false | none | 现货对冲状态, true - 启用，false - 未启用  
risk_units | array | false | none | 风险单元  
» RiskUnits | object | false | none | none  
»» symbol | string | false | none | 风险单元标志  
»» spot_in_use | string | false | none | 现货对冲占用数量  
»» maintain_margin | string | false | none | 风险单元的维持保证金  
»» initial_margin | string | false | none | 风险单元的起始保证金  
»» delta | string | false | none | 风险单元的 总 delta  
»» gamma | string | false | none | 风险单元的 总 gamma  
»» theta | string | false | none | 风险单元的 总 theta  
»» vega | string | false | none | 风险单元的 总 vega  
      
    
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
    
    

##  UnifiedDiscount

_统一账户梯度discount_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种名称  
discount_tiers | array | false | none | 阶梯式discount  
» tier | string | false | none | 档位  
» discount | string | false | none | 保证金折扣系数  
» lower_limit | string | false | none | 下限  
» upper_limit | string | false | none | 上限, +表示正无穷  
» leverage | string | false | none | 杠杆倍数  
      
    
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
    
    

##  UnifiedCurrency

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
name | string | false | none | 币种名称  
prec | string | false | none | 币种精度  
min_borrow_amount | string | false | none | 最小可借限额，单位是币  
user_max_borrow_amount | string | false | none | 用户最大可借限额，单位是 USDT  
total_max_borrow_amount | string | false | none | 平台最大可借限额，单位是 USDT  
loan_status | string | false | none | 是否借贷状态  
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
    
    

##  UnifiedTransferable

_UnifiedTransferable_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种信息  
amount | string | false | none | 最多可转出的额度  
      
    
    {
      "currency": "string",
      "amount": "string"
    }