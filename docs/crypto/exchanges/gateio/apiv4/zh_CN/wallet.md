---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/wallet
api_type: Account
updated_at: 2026-05-27 20:18:09.322255
---

# Wallet

钱包接口

##  查询币种支持的链

GET`/wallet/currency_chains`

GET `/wallet/currency_chains`

_查询币种支持的链_

流通性或者价值极低的币种不支持api操作，请通过Web或App页面进行查询以及处理

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 是 | 币种名称  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [CurrencyChain]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» chain | string | 链名称  
» name_cn | string | 链的中文名称  
» name_en | string | 链的英文名称  
» contract_address | string | 币种智能合约地址，如果没有地址则为空字串  
» is_disabled | integer(int32) | 是否禁用，0 表示未禁用  
» is_deposit_disabled | integer(int32) | 充值是否禁用，0 表示未禁用  
» is_withdraw_disabled | integer(int32) | 提现是否禁用，0 表示未禁用  
» decimal | string | 提币精度  
» is_tag | integer | 是否包含tag  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/wallet/currency_chains'
    query_param = 'currency=GT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/wallet/currency_chains?currency=GT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "chain": "ETH",
        "name_cn": "以太坊ERC20",
        "name_en": "ETH/ERC20",
        "contract_address": "",
        "is_disabled": 0,
        "is_deposit_disabled": 0,
        "is_withdraw_disabled": 0,
        "is_tag": 0
      }
    ]
    

##  获取币种充值地址🔒 需要认证

GET`/wallet/deposit_address`

GET `/wallet/deposit_address`

_获取币种充值地址_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 是 | 币种名称  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 地址获取成功 | DepositAddress  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种信息  
» address | string | 充值地址  
» min_deposit_amount | string | 最小充值额度  
» multichain_addresses | array |   
»» MultiChainAddressItem | object |   
»»» chain | string | 链的名称  
»»» address | string | 充值地址  
»»» payment_id | string | 部分币种充值时必须填写的备注  
»»» payment_name | string | 备注类型, `Tag` 或 `Memo`  
»»» obtain_failed | integer | 地址是否获取成功，0 表示成功，1 表示失败，可能需要重新获取  
»»» min_confirms | integer | 最小确认数  
  
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
    
    url = '/wallet/deposit_address'
    query_param = 'currency=USDT'
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
    url="/wallet/deposit_address"
    query_param="currency=USDT"
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
      "currency": "USDT",
      "address": "LPXtk1kWHioP62SzfqwKbYE3Z7Wt2ujYEc",
      "multichain_addresses": [
        {
          "chain": "TRX",
          "address": "LPXtk1kWHioP62SzfqwKbYE3Z7Wt2ujYEc",
          "payment_id": "",
          "payment_name": "",
          "obtain_failed": 0,
          "min_confirms": 1
        }
      ],
      "min_deposit_amount": "0.000006"
    }
    

##  获取提现记录🔒 需要认证

GET`/wallet/withdrawals`

GET `/wallet/withdrawals`

_获取提现记录_

记录查询时间范围不允许超过 30 天

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定查询币种，不指定返回全部币种  
withdraw_id | 请求参数 | string | 否 | 提现记录id， 以w开头，如： w1879219868。 当withdraw_id 不为空时，则值查询这一条提现记录，不再按照时间进行查询  
asset_class | 请求参数 | string | 否 | 提现记录币种类型，默认为空。即支持用户按需查询主区和创新区的提现记录。  
取值范围：SPOT、PILOT  
  
SPOT ： 主区  
PILOT： 创新区  
withdraw_order_id | 请求参数 | string | 否 | 提现时用户自定义的单号。 默认为空。 非空时 会查询指定用户自定义单号记录  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间，不指定则默认从当前时间开始向前推 7 天  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
####  详细描述

**asset_class** : 提现记录币种类型，默认为空。即支持用户按需查询主区和创新区的提现记录。  
取值范围：SPOT、PILOT  
  
SPOT ： 主区  
PILOT： 创新区

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [WithdrawalRecord]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | string | 交易记录 ID  
» txid | string | 区块转账哈希记录  
» block_number | string | 区块编号  
» withdraw_order_id | string | 用户端订单编号,最长32个，输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
» timestamp | string | 操作时间  
» amount | string | 币的数量  
» fee | string | 手续费  
» currency | string | 币种名称  
» address | string | 提现地址  
» type | string | 业务类型  
» fail_reason | string | 提现失败原因，当 status = CANCEL时有值，其余状态时为空  
» timestamp2 | string | 提现终态时间，即： 提现取消时间或提现成功时间  
当 status = CANCEL 时，对应 取消时间  
当 status = DONE 时，为提现成功时间  
» memo | string | 转账memo等备注信息  
» status | string | 交易状态  
  
\- BCODE: 充值码操作  
\- CANCEL: 已取消  
\- CANCELPEND: 取消提现中  
\- DONE: 完成  
\- EXTPEND: 已经发送等待确认  
\- FAIL: 链上失败等待确认  
\- FVERIFY: 人脸审核处理中  
\- LOCKED: 钱包侧锁单  
\- MANUAL: 待人工审核  
\- REJECT: 拒绝  
\- REQUEST: 请求中  
\- REVIEW: 审核中  
» chain | string | 提现的链名称  
  
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
    
    url = '/wallet/withdrawals'
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
    url="/wallet/withdrawals"
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
      [
        {
          "id": "w1879219868",
          "currency": "USDT",
          "address": "THISISTESTADDRESSFORGATEPAY",
          "amount": "4.023",
          "fee": "0",
          "txid": "Internal transaction 260594131",
          "chain": "BSC",
          "timestamp": "1745220149",
          "status": "DONE",
          "withdraw_order_id": "202504211521368538928",
          "block_number": "1000",
          "fail_reason": "",
          "type": "appbankgp",
          "timestamp2": "1745220149",
          "memo": ""
        }
      ]
    ]
    

##  获取充值记录🔒 需要认证

GET`/wallet/deposits`

GET `/wallet/deposits`

_获取充值记录_

记录查询时间范围不允许超过 30 天

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定查询币种，不指定返回全部币种  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间，不指定则默认从当前时间开始向前推 7 天  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
limit | 请求参数 | integer | 否 | 列表返回的最大数量，上限 500 笔  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DepositRecord]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | string | 交易记录 ID  
» txid | string | 区块转账哈希记录  
» timestamp | string | 操作时间  
» amount | string | 币的数量  
» currency | string | 币种名称  
» address | string | 提现地址。提现操作必填  
» memo | string | 转账memo等备注信息  
» status | string | 交易状态  
  
\- BLOCKED: 拒绝充值  
\- DEP_CREDITED: 充值到账，提现未解锁  
\- DONE: 已经给账户增加资金  
\- INVALID: 无效数据  
\- MANUAL: 转人工审核  
\- PEND: 处理中  
\- REVIEW: 充值审核中(合规审查)  
\- TRACK: 跟踪确认数，等待给用户添加资金(现货)  
» chain | string | 提现的链名称  
  
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
    
    url = '/wallet/deposits'
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
    url="/wallet/deposits"
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
        "id": "210496",
        "timestamp": "1542000000",
        "currency": "USDT",
        "address": "1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs",
        "txid": "128988928203223323290",
        "amount": "222.61",
        "memo": "",
        "status": "DONE",
        "chain": "TRX"
      }
    ]
    

##  交易账户互转🔒 需要认证

POST`/wallet/transfers`

POST `/wallet/transfers`

_交易账户互转_

个人交易账户之间的余额互转，目前支持以下互转操作：

  1. 现货账户 - 杠杆账户
  2. 现货账户 - 永续合约账户
  3. 现货账户 - 交割合约账户
  4. 现货账户 - 期权账户

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | Transfer | 是 |   
» currency | body | string | 是 | 转账货币名称。关联合约账户时，currency 可以设置的值为`POINT`(即点卡) 和支持的结算货币(如 `BTC`, `USDT`)  
» from | body | string | 是 | 转出账户  
» to | body | string | 是 | 转入账户  
» amount | body | string | 是 | 划转金额，最多支持8位小数，必须大于0  
» currency_pair | body | string | 否 | 杠杆交易对。转入或转出杠杆账户时必填  
» settle | body | string | 否 | 合约结算币种。 转入转出合约账户时必填  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» from | spot  
» from | margin  
» from | futures  
» from | delivery  
» from | options  
» to | spot  
» to | margin  
» to | futures  
» to | delivery  
» to | options  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 转账操作成功 | TransactionID  
  
### 返回格式

状态码 **200**

_TransactionID_

名称 | 类型 | 描述  
---|---|---  
» tx_id | integer(int64) | 操作单号  
  
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
    
    url = '/wallet/transfers'
    query_param = ''
    body='{"currency":"BTC","from":"spot","to":"margin","amount":"1","currency_pair":"BTC_USDT","settle":""}'
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
    url="/wallet/transfers"
    query_param=""
    body_param='{"currency":"BTC","from":"spot","to":"margin","amount":"1","currency_pair":"BTC_USDT","settle":""}'
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
      "from": "spot",
      "to": "margin",
      "amount": "1",
      "currency_pair": "BTC_USDT",
      "settle": ""
    }
    

> 返回示例

> 200 返回
    
    
    {
      "tx_id": 59636381286
    }
    

##  主子账号划转记录🔒 需要认证

GET`/wallet/sub_account_transfers`

GET `/wallet/sub_account_transfers`

_主子账号划转记录_

记录查询时间范围不允许超过 30 天

> 注：只能查询到 2020-04-10 之后的记录

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
sub_uid | 请求参数 | string | 否 | 子账号用户 ID，可查多笔中间用`,`隔开，不指定则返回所有子账号的记录  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间，不指定则默认从当前时间开始向前推 7 天  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表获取成功 | [SubAccountTransferRecordItem]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» timest | string | 转账时间戳  
» uid | string | 主账号用户 ID  
» sub_account | string | 子账号用户 ID  
» sub_account_type | string | 操作的子账号交易账户， spot - 现货账户， futures - 永续合约账户， delivery - 交割合约账户, options - 期权账户  
» currency | string | 转账货币名称  
» amount | string | 划转金额  
» direction | string | 资金流向，to - 转入子账号, from - 转出子账号  
» source | string | 转账操作来源  
» client_order_id | string | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
» status | string | 子账户划转记录状态，目前只有success  
  
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
    
    url = '/wallet/sub_account_transfers'
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
    url="/wallet/sub_account_transfers"
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
        "timest": "1592809000",
        "uid": "10001",
        "sub_account": "10002",
        "sub_account_type": "spot",
        "currency": "BTC",
        "amount": "1",
        "direction": "to",
        "source": "web",
        "client_order_id": "da3ce7a088c8b0372b741419c7829033",
        "status": "success"
      }
    ]
    

##  主子账号互转🔒 需要认证

POST`/wallet/sub_account_transfers`

POST `/wallet/sub_account_transfers`

_主子账号互转_

支持转入转出到子账号的现货或合约账户，注意不管操作子账号的哪个账户，主账号的账户只使用现货账户

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | SubAccountTransfer | 是 |   
» sub_account | body | string | 是 | 子账号用户 ID  
» sub_account_type | body | string | 否 | 操作的子账号交易账户， spot - 现货账户， futures - 永续合约账户， delivery - 交割合约账户, options - 期权账户  
» currency | body | string | 是 | 转账货币名称  
» amount | body | string | 是 | 划转金额，最多支持8位小数，必须大于0  
» direction | body | string | 是 | 资金流向，to - 转入子账号, from - 转出子账号  
» client_order_id | body | string | 否 | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 转账操作成功 | TransactionID  
  
### 返回格式

状态码 **200**

_TransactionID_

名称 | 类型 | 描述  
---|---|---  
» tx_id | integer(int64) | 操作单号  
  
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
    
    url = '/wallet/sub_account_transfers'
    query_param = ''
    body='{"sub_account":"10002","sub_account_type":"spot","currency":"BTC","amount":"1","direction":"to","client_order_id":"da3ce7a088c8b0372b741419c7829033"}'
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
    url="/wallet/sub_account_transfers"
    query_param=""
    body_param='{"sub_account":"10002","sub_account_type":"spot","currency":"BTC","amount":"1","direction":"to","client_order_id":"da3ce7a088c8b0372b741419c7829033"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "sub_account": "10002",
      "sub_account_type": "spot",
      "currency": "BTC",
      "amount": "1",
      "direction": "to",
      "client_order_id": "da3ce7a088c8b0372b741419c7829033"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "tx_id": 59636381286
    }
    

##  子账号与子帐号互转🔒 需要认证

POST`/wallet/sub_account_to_sub_account`

POST `/wallet/sub_account_to_sub_account`

_子账号与子帐号互转_

支持同一个主账户下的两个子账户之间进行余额互转，可以使用主账户API Key或者转出子账户API Key进行操作

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | SubAccountToSubAccount | 是 |   
» currency | body | string | 是 | 转账货币名称  
» sub_account_type | body | string | 否 | 转出的子账号交易账户 (已弃用, 改用 `sub_account_from_type` 和 `sub_account_to_type`)  
» sub_account_from | body | string | 是 | 转出子账号用户 ID  
» sub_account_from_type | body | string | 是 | 转出的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
» sub_account_to | body | string | 是 | 转入子账号用户 ID  
» sub_account_to_type | body | string | 是 | 转入的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
» amount | body | string | 是 | 划转金额，最多支持8位小数，必须大于0  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 转账操作成功 | TransactionID  
  
### 返回格式

状态码 **200**

_TransactionID_

名称 | 类型 | 描述  
---|---|---  
» tx_id | integer(int64) | 操作单号  
  
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
    
    url = '/wallet/sub_account_to_sub_account'
    query_param = ''
    body='{"currency":"usdt","sub_account_from":"10001","sub_account_from_type":"spot","sub_account_to":"10002","sub_account_to_type":"spot","amount":"1"}'
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
    url="/wallet/sub_account_to_sub_account"
    query_param=""
    body_param='{"currency":"usdt","sub_account_from":"10001","sub_account_from_type":"spot","sub_account_to":"10002","sub_account_to_type":"spot","amount":"1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "currency": "usdt",
      "sub_account_from": "10001",
      "sub_account_from_type": "spot",
      "sub_account_to": "10002",
      "sub_account_to_type": "spot",
      "amount": "1"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "tx_id": 59636381286
    }
    

##  主子账户划转状态查询🔒 需要认证

GET`/wallet/order_status`

GET `/wallet/order_status`

_主子账户划转状态查询_

支持根据用户自定义client_order_id或者划转接口返回的tx_id查询主子账户划转状态

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
client_order_id | 请求参数 | string | 否 | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
tx_id | 请求参数 | string | 否 | 划转操作单号，和client_order_id不能同时为空  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 主子账户划转状态获取成功 | TransferOrderStatus  
  
### 返回格式

状态码 **200**

_TransferOrderStatus_

名称 | 类型 | 描述  
---|---|---  
» tx_id | string | 操作单号  
» status | string | 划转状态，PENDING - 处理中，SUCCESS - 划转成功，FAIL - 划转失败，PARTIAL_SUCCESS - 部分成功（子子划转时会出现此状态）  
  
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
    
    url = '/wallet/order_status'
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
    url="/wallet/order_status"
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
      "tx_id": "59636381286",
      "status": "SUCCESS"
    }
    

##  查询提现状态🔒 需要认证

GET`/wallet/withdraw_status`

GET `/wallet/withdraw_status`

_查询提现状态_

流通性或者价值极低的币种不支持api操作，请通过Web或App页面进行查询以及处理

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表获取成功 | [WithdrawStatus]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» currency | string | 币种  
» name | string | 币种名称  
» name_cn | string | 币种中文名称  
» deposit | string | 充值手续费  
» withdraw_percent | string | 提现手续费率百分比  
» withdraw_fix | string | 固定提现手续费用  
» withdraw_day_limit | string | 日提现额度  
» withdraw_amount_mini | string | 最少提现额度  
» withdraw_day_limit_remain | string | 剩余日提现额度  
» withdraw_eachtime_limit | string | 单次最多提现额度  
» withdraw_fix_on_chains | object | 多链的固定提现手续费用  
»» **additionalProperties** | string |   
» withdraw_percent_on_chains | object | 多链的百分比提现手续费用  
»» **additionalProperties** | string |   
  
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
    
    url = '/wallet/withdraw_status'
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
    url="/wallet/withdraw_status"
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
        "currency": "GT",
        "name": "GateToken",
        "name_cn": "GateToken",
        "deposit": "0",
        "withdraw_percent": "0%",
        "withdraw_fix": "0.01",
        "withdraw_day_limit": "20000",
        "withdraw_day_limit_remain": "20000",
        "withdraw_amount_mini": "0.11",
        "withdraw_eachtime_limit": "20000",
        "withdraw_fix_on_chains": {
          "BTC": "20",
          "ETH": "15",
          "TRX": "0",
          "EOS": "2.5"
        },
        "withdraw_percent_on_chains": {
          "ETH": "0%",
          "GTEVM": "0%"
        }
      }
    ]
    

##  查询子账号余额信息🔒 需要认证

GET`/wallet/sub_account_balances`

GET `/wallet/sub_account_balances`

_查询子账号余额信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
sub_uid | 请求参数 | string | 否 | 子账号用户 ID，可查多笔中间用`,`隔开，不指定则返回所有子账号的记录  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为20,最大100。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表获取成功 | [SubAccountBalance]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» uid | string | 用户 ID  
» available | object | 币种可用余额  
»» **additionalProperties** | string |   
» locking | object | 币种锁定金额  
»» **additionalProperties** | string |   
  
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
    
    url = '/wallet/sub_account_balances'
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
    url="/wallet/sub_account_balances"
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
        "uid": "10003",
        "available": {
          "BTC": "0.1",
          "GT": "2000",
          "USDT": "10"
        },
        "locking": {
          "BTC": "0",
          "GT": "0",
          "USDT": "0"
        }
      }
    ]
    

##  查询子账号逐仓杠杆账户余额信息🔒 需要认证

GET`/wallet/sub_account_margin_balances`

GET `/wallet/sub_account_margin_balances`

_查询子账号逐仓杠杆账户余额信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
sub_uid | 请求参数 | string | 否 | 子账号用户 ID，可查多笔中间用`,`隔开，不指定则返回所有子账号的记录  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表获取成功 | [SubAccountMarginBalance]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» uid | string | 用户 ID  
» available | array | 账户余额信息  
»» _None_ | object | 某交易对的杠杆账户信息，`base` 对应交易货币的账户信息，`quote` 对应计价货币的账户信息  
»»» currency_pair | string | 交易对  
»»» account_type | string | 账户类型。mmr-维持保证金率账户，inactive - 市场未激活  
»»» leverage | string | 用户当前市场杠杆倍数  
»»» locked | boolean | 账户是否被锁定  
»»» risk | string | 已废弃  
»»» mmr | string | 该逐仓杠杆账户当前维持保证金率  
»»» base | SubAccountMarginBalance/properties/available/items/properties/base | 货币账户信息  
»»»» currency | string | 货币名称  
»»»» available | string | 可用于杠杆交易的额度，available = 保证金 + borrowed  
»»»» locked | string | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
»»»» borrowed | string | 借入资金  
»»»» interest | string | 未还利息  
»»» quote | SubAccountMarginBalance/properties/available/items/properties/base | 货币账户信息  
»»»» currency | string | 货币名称  
»»»» available | string | 可用于杠杆交易的额度，available = 保证金 + borrowed  
»»»» locked | string | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
»»»» borrowed | string | 借入资金  
»»»» interest | string | 未还利息  
  
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
    
    url = '/wallet/sub_account_margin_balances'
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
    url="/wallet/sub_account_margin_balances"
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
        "uid": "10000",
        "available": [
          {
            "locked": false,
            "currency_pair": "BTC_USDT",
            "risk": "9999.99",
            "base": {
              "available": "0.1",
              "borrowed": "0",
              "interest": "0",
              "currency": "BTC",
              "locked": "0"
            },
            "quote": {
              "available": "0",
              "borrowed": "0",
              "interest": "0",
              "currency": "USDT",
              "locked": "0"
            }
          }
        ]
      }
    ]
    

##  查询子账号永续合约账户余额信息🔒 需要认证

GET`/wallet/sub_account_futures_balances`

GET `/wallet/sub_account_futures_balances`

_查询子账号永续合约账户余额信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
sub_uid | 请求参数 | string | 否 | 子账号用户 ID，可查多笔中间用`,`隔开，不指定则返回所有子账号的记录  
settle | 请求参数 | string | 否 | 指定查询某个结算币种的余额  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表获取成功 | [SubAccountFuturesBalance]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» uid | string | 用户 ID  
» available | object | 各结算账户信息  
»» **additionalProperties** | object |   
»»» total | string | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
»»» unrealised_pnl | string | 未实现盈亏  
»»» position_margin | string | 已废弃  
»»» order_margin | string | 所有未完成订单的起始保证金  
»»» available | string | 指的是逐仓可用的转出或交易的额度，统一账户下包含授信额度的逐仓可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
»»» point | string | 点卡数额  
»»» currency | string | 结算币种  
»»» in_dual_mode | boolean | 是否为双向持仓模式  
»»» enable_credit | boolean | 是否开启统一账户模式  
»»» position_initial_margin | string | 头寸占用的起始保证金，适用于统一账户模式  
»»» maintenance_margin | string | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
»»» bonus | string | 体验金  
»»» enable_evolved_classic | boolean | 已废弃  
»»» cross_order_margin | string | 全仓挂单保证金，适用于新经典账户保证金模式  
»»» cross_initial_margin | string | 全仓初始保证金，适用于新经典账户保证金模式  
»»» cross_maintenance_margin | string | 全仓维持保证金，适用于新经典账户保证金模式  
»»» cross_unrealised_pnl | string | 全仓未实现盈亏，适用于新经典账户保证金模式  
»»» cross_available | string | 全仓可用额度，适用于新经典账户保证金模式  
»»» cross_margin_balance | string | 全仓保证金余额，适用于新经典账户保证金模式  
»»» cross_mmr | string | 全仓维持保证金率，适用于新经典账户保证金模式  
»»» cross_imr | string | 全仓初始保证金率，适用于新经典账户保证金模式  
»»» isolated_position_margin | string | 逐仓仓位保证金，适用于新经典账户保证金模式  
»»» enable_new_dual_mode | boolean | 已废弃  
»»» margin_mode | integer | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
»»» enable_tiered_mm | boolean | 是否开启梯度式计算维持保证金  
»»» enable_dual_plus | boolean | 是否支持分仓模式  
»»» position_mode | string | 持仓模式 single-单向持仓 dual-双向持仓 dual_plus-分仓  
»»» history | object | 累计统计数据  
»»»» dnw | string | 累计转入转出  
»»»» pnl | string | 累计交易盈亏  
»»»» fee | string | 累计手续费  
»»»» refr | string | 累计获取的推荐人返佣  
»»»» fund | string | 累计资金费用  
»»»» point_dnw | string | 累计点卡转入转出  
»»»» point_fee | string | 累计点卡抵扣手续费  
»»»» point_refr | string | 累计获取的点卡推荐人返佣  
»»»» bonus_dnw | string | 累计体验金转入转出  
»»»» bonus_offset | string | 累计体验金抵扣  
»»»» cross_settle | string | 代表统一账户模式下，合约账户盈利被结算到现货数值。负数代表从合约结算到现货的，正数代表从现货结算到合约的。此数值为累计值  
  
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
    
    url = '/wallet/sub_account_futures_balances'
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
    url="/wallet/sub_account_futures_balances"
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
      [
        {
          "available": {
            "btc": {
              "available": "0.0009",
              "bonus": "0",
              "cross_available": "0.0009",
              "cross_initial_margin": "0",
              "cross_maintenance_margin": "0",
              "cross_order_margin": "0",
              "cross_unrealised_pnl": "0",
              "currency": "BTC",
              "enable_credit": false,
              "enable_evolved_classic": true,
              "enable_new_dual_mode": false,
              "history": {
                "bonus_dnw": "0",
                "bonus_offset": "0",
                "cross_settle": "0",
                "dnw": "0.0009",
                "fee": "0",
                "fund": "0",
                "pnl": "0",
                "point_dnw": "0",
                "point_fee": "0",
                "point_refr": "0",
                "refr": "0"
              },
              "in_dual_mode": false,
              "isolated_position_margin": "0",
              "maintenance_margin": "0",
              "margin_mode": 0,
              "margin_mode_name": "classic",
              "order_margin": "0",
              "point": "0",
              "position_initial_margin": "0",
              "position_margin": "0",
              "total": "0.0009",
              "unrealised_pnl": "0",
              "update_id": 11,
              "update_time": 1741766400,
              "user": 10003
            },
            "usd": {},
            "usdt": {
              "available": "500.7",
              "bonus": "0",
              "cross_available": "500.7",
              "cross_initial_margin": "0",
              "cross_maintenance_margin": "0",
              "cross_order_margin": "0",
              "cross_unrealised_pnl": "0",
              "currency": "USDT",
              "enable_credit": true,
              "enable_evolved_classic": true,
              "enable_new_dual_mode": true,
              "history": {
                "bonus_dnw": "0",
                "bonus_offset": "0",
                "cross_settle": "-1.854650083",
                "dnw": "1.89047097",
                "fee": "-0.141010882",
                "fund": "0",
                "pnl": "0.10519",
                "point_dnw": "0",
                "point_fee": "0",
                "point_refr": "0",
                "refr": "0"
              },
              "in_dual_mode": true,
              "isolated_position_margin": "0",
              "maintenance_margin": "0",
              "margin_mode": 1,
              "margin_mode_name": "multi_currency",
              "order_margin": "0",
              "point": "0",
              "position_initial_margin": "0",
              "position_margin": "0",
              "total": "0.000000005",
              "unrealised_pnl": "0",
              "update_id": 37,
              "update_time": 1741766400,
              "user": 10003
            }
          },
          "uid": "10003"
        }
      ]
    ]
    

##  查询子账号全仓杠杆账户余额信息🔒 需要认证

GET`/wallet/sub_account_cross_margin_balances`

GET `/wallet/sub_account_cross_margin_balances`

_查询子账号全仓杠杆账户余额信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
sub_uid | 请求参数 | string | 否 | 子账号用户 ID，可查多笔中间用`,`隔开，不指定则返回所有子账号的记录  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表获取成功 | [SubAccountCrossMarginBalance]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» uid | string | 用户 ID  
» available | object |   
»» user_id | integer(int64) | 全仓帐户用户ID，如果 0 代表这个子帐号尚未开通全仓帐户  
»» locked | boolean | 账户是否被锁定  
»» balances | object |   
»»» CrossMarginBalance | object |   
»»»» available | string | 可用额度  
»»»» freeze | string | 被锁定的额度  
»»»» borrowed | string | 借入额度  
»»»» interest | string | 未还利息  
»»» total | string | 折算成 USDT 的账户总资产，即所有币种(不包括点卡)的 `(available+freeze)*price*discount` 之和  
»»» borrowed | string | 折算成 USDT 的账户总借入数量，即所有币种(不包括点卡)的 `borrowed*price*discount` 之和  
»»» borrowed_net | string | 折算成 USDT 的账户总借入数量 * 放大系数  
»»» net | string | 折算成 USDT 的净资产  
»»» leverage | string | 杠杆倍数  
»»» interest | string | 折算成 USDT 的账户未接利息的总和，即所有币种(不包括点卡)的 `interest*price*discount` 之和  
»»» risk | string | 风险率，风险率小于 110% 会被爆仓，计算方式 `total / (borrowed+interest)`  
»»» total_initial_margin | string | 总初始保证金  
»»» total_margin_balance | string | 总保证金余额  
»»» total_maintenance_margin | string | 总维持保证金  
»»» total_initial_margin_rate | string | 总初始保证金率  
»»» total_maintenance_margin_rate | string | 总维持保证金率  
»»» total_available_margin | string | 可用的保证金额度  
  
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
    
    url = '/wallet/sub_account_cross_margin_balances'
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
    url="/wallet/sub_account_cross_margin_balances"
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
        "uid": "100000",
        "available": {
          "user_id": 100003,
          "locked": false,
          "total": "20.000000",
          "borrowed": "0.000000",
          "interest": "0",
          "borrowed_net": "0",
          "net": "20",
          "leverage": "3",
          "risk": "9999.99",
          "total_initial_margin": "0.00",
          "total_margin_balance": "20.00",
          "total_maintenance_margin": "0.00",
          "total_initial_margin_rate": "9999.9900",
          "total_maintenance_margin_rate": "9999.9900",
          "total_available_margin": "20.00",
          "balances": {
            "USDT": {
              "available": "20.000000",
              "freeze": "0.000000",
              "borrowed": "0.000000",
              "interest": "0.000000"
            }
          }
        }
      }
    ]
    

##  查询提币地址白名单🔒 需要认证

GET`/wallet/saved_address`

GET `/wallet/saved_address`

_查询提币地址白名单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 是 | 币种  
chain | 请求参数 | string | 否 | 链名称  
limit | 请求参数 | string | 否 | 列表返回的最大数量, 最多 100  
page | 请求参数 | integer | 否 | 页码  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表获取成功 | [SavedAddress]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» currency | string | 币种  
» chain | string | 链名称  
» address | string | 地址  
» name | string | 名称  
» tag | string | 标签  
» verified | string | 是否通过验证 0-未验证, 1-已验正  
  
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
    
    url = '/wallet/saved_address'
    query_param = 'currency=USDT'
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
    url="/wallet/saved_address"
    query_param="currency=USDT"
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
        "currency": "usdt",
        "chain": "TRX",
        "address": "TWYirLzw2RARB2jfeFcfRPmeuU3rC7rakT",
        "name": "gate",
        "tag": "",
        "verified": "1"
      }
    ]
    

##  查询个人交易费率🔒 需要认证

GET`/wallet/fee`

GET `/wallet/fee`

_查询个人交易费率_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 指定交易对获取更准确的费率设置。  
  
该字段可选，通常情况下所有交易对的费率设置是一样的。  
settle | 请求参数 | string | 否 | 指定合约的结算币种获取更准确的费率设置。  
  
该字段可选，通常情况下所有结算币种的费率设置是一样的。  
  
####  详细描述

**currency_pair** : 指定交易对获取更准确的费率设置。  
  
该字段可选，通常情况下所有交易对的费率设置是一样的。

**settle** : 指定合约的结算币种获取更准确的费率设置。  
  
该字段可选，通常情况下所有结算币种的费率设置是一样的。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | BTC  
settle | USDT  
settle | USD  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | TradeFee  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» user_id | integer(int64) | 用户 ID  
» taker_fee | string | 现货 taker 费率  
» maker_fee | string | 现货 maker 费率  
» rpi_maker_fee | string | 现货 RPI MM maker 费率  
» gt_discount | boolean | 是否开启 GT 抵扣折扣  
» gt_taker_fee | string | GT 抵扣 taker 费率，未开启 GT 抵扣则为 0  
» gt_maker_fee | string | GT 抵扣 maker 费率，未开启 GT 抵扣则为 0  
» loan_fee | string | 杠杆理财的费率  
» point_type | string | 点卡类型，0 - 初版点卡，1 - 202009 启用的新点卡  
» futures_taker_fee | string | 合约 taker 费率  
» futures_maker_fee | string | 合约 maker 费率  
» futures_rpi_maker_fee | string | 合约 RPI MM maker 费率  
» delivery_taker_fee | string | 交割合约 taker 费率  
» delivery_maker_fee | string | 交割合约 maker 费率  
» debit_fee | integer | 费率抵扣类型 , 1 - GT抵扣 , 2 - 点卡抵扣 , 3 - VIP费率  
» rpi_mm | integer | RPI MM等级  
  
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
    
    url = '/wallet/fee'
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
    url="/wallet/fee"
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
      "taker_fee": "0.002",
      "maker_fee": "0.002",
      "rpi_maker_fee": "-0.00175",
      "futures_taker_fee": "-0.00025",
      "futures_maker_fee": "0.00075",
      "futures_rpi_maker_fee": "-0.00175",
      "gt_discount": false,
      "gt_taker_fee": "0",
      "gt_maker_fee": "0",
      "loan_fee": "0.18",
      "point_type": "1",
      "delivery_taker_fee": "0.00016",
      "delivery_maker_fee": "-0.00015",
      "debit_fee": 3,
      "rpi_mm": 2
    }
    

##  查询个人账户总额🔒 需要认证

GET`/wallet/total_balance`

GET `/wallet/total_balance`

_查询个人账户总额_

该查询接口返回的是各账户里所有币按照传入币种折算之后的总 _估值_ ，折算价以及相关各账户的余额信息最长会有1分钟的缓存， 不推荐在即时计算时使用该接口的数据。

即时计算可根据账户类型查询对应的余额接口，如：

  * `GET /spot/accounts` 查询现货账户
  * `GET /margin/accounts` 查询杠杆账户
  * `GET /futures/{settle}/accounts` 查询合约账户

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 用于统计换算的目标货币类型，可接受BTC，CNY，USD，USDT四个值。USDT是默认值  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求有效且成功返回 | TotalBalance  
  
### 返回格式

状态码 **200**

_用户总资产信息_

名称 | 类型 | 描述  
---|---|---  
» total | TotalBalance/properties/total | 换算成目标币种的账户总额  
»» amount | string | 账户总额数字  
»» currency | string | 币种  
»» unrealised_pnl | string | 未实现盈亏总和,这个字段只会在futures,options,delivery,total 账户中出现  
»» borrowed | string | 杠杆借贷总和,这个字段只会在margin,cross_margin账户中出现  
» details | object | 各账户总额  
  
\- cross_margin: 全仓杠杆账户  
\- spot: 现货账户  
\- finance: 金融账户  
\- margin: 杠杆账户  
\- quant: 量化账户  
\- futures: 永续合约账户  
\- delivery: 交割合约账户  
\- warrant: warrant 账户  
\- cbbc: 牛熊证账户  
\- meme_box: alpha账户  
\- options: 期权账户  
\- payment: 支付账户  
»» **additionalProperties** | TotalBalance/properties/total | 换算成目标币种的账户总额  
»»» amount | string | 账户总额数字  
»»» currency | string | 币种  
»»» unrealised_pnl | string | 未实现盈亏总和,这个字段只会在futures,options,delivery,total 账户中出现  
»»» borrowed | string | 杠杆借贷总和,这个字段只会在margin,cross_margin账户中出现  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
currency | BTC  
currency | CNY  
currency | USD  
currency | USDT  
currency | BTC  
currency | CNY  
currency | USD  
currency | USDT  
  
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
    
    url = '/wallet/total_balance'
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
    url="/wallet/total_balance"
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
      "details": {
        "cross_margin": {
          "amount": "0",
          "currency": "USDT"
        },
        "spot": {
          "currency": "USDT",
          "amount": "42264489969935775.5160259954878034182418"
        },
        "finance": {
          "amount": "662714381.70310327810191647181",
          "currency": "USDT"
        },
        "margin": {
          "amount": "1259175.664137668554329559",
          "currency": "USDT",
          "borrowed": "0.00"
        },
        "quant": {
          "amount": "591702859674467879.6488202650892478553852",
          "currency": "USDT"
        },
        "futures": {
          "amount": "2384175.5606114082065",
          "currency": "USDT",
          "unrealised_pnl": "0.00"
        },
        "delivery": {
          "currency": "USDT",
          "amount": "1519804.9756702",
          "unrealised_pnl": "0.00"
        },
        "warrant": {
          "amount": "0",
          "currency": "USDT"
        },
        "cbbc": {
          "currency": "USDT",
          "amount": "0"
        },
        "meme_box": {
          "currency": "USDT",
          "amount": "0"
        },
        "options": {
          "currency": "USDT",
          "amount": "0"
        },
        "payment": {
          "currency": "USDT",
          "amount": "0"
        }
      },
      "total": {
        "currency": "USDT",
        "amount": "633967350312281193.068368815439797304437",
        "unrealised_pnl": "0.00",
        "borrowed": "0.00"
      }
    }
    

##  获取可兑换的小额币种清单🔒 需要认证

GET`/wallet/small_balance`

GET `/wallet/small_balance`

_获取可兑换的小额币种清单_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | [SmallBalance]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [小额兑换币种]  
» _None_ | SmallBalance | 小额兑换币种  
»» currency | string | 币种  
»» available_balance | string | 可转换金额  
»» estimated_as_btc | string | 预计用 BTC 计价金额  
»» convertible_to_gt | string | 预计可转换成多少 GT  
  
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
    
    url = '/wallet/small_balance'
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
    url="/wallet/small_balance"
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
      [
        {
          "currency": "FLOKI",
          "available_balance": "182.29400000",
          "estimated_as_btc": "0.00000012",
          "convertible_to_gt": "0.001080"
        },
        {
          "currency": "MBLK",
          "available_balance": "0.91723337",
          "estimated_as_btc": "0.00000102",
          "convertible_to_gt": "0.009188"
        }
      ]
    ]
    

##  兑换的小额币种🔒 需要认证

POST`/wallet/small_balance`

POST `/wallet/small_balance`

_兑换的小额币种_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | ConvertSmallBalance | 是 |   
» currency | body | array | 否 | 需要被兑换的币种  
» is_all | body | boolean | 否 | 是否全部兑换  
  
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
    
    url = '/wallet/small_balance'
    query_param = ''
    body='{"currency":["FLOKI","MBLK"],"is_all":true}'
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
    url="/wallet/small_balance"
    query_param=""
    body_param='{"currency":["FLOKI","MBLK"],"is_all":true}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "currency": [
        "FLOKI",
        "MBLK"
      ],
      "is_all": true
    }
    

##  获取可兑换的小额币种历史纪录🔒 需要认证

GET`/wallet/small_balance_history`

GET `/wallet/small_balance_history`

_获取可兑换的小额币种历史纪录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 兑换的币种  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大100。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | [SmallBalanceHistory]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [小额兑换币种]  
» _None_ | SmallBalanceHistory | 小额兑换币种  
»» id | string | 订单ID  
»» currency | string | 兑换币种  
»» amount | string | 兑换数量  
»» gt_amount | string | 被兑换到的 GT 数量  
»» create_time | integer(int64) | 兑换时间(秒)  
  
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
    
    url = '/wallet/small_balance_history'
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
    url="/wallet/small_balance_history"
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
      [
        {
          "id": "28583810",
          "create_time": 1706670777,
          "currency": "FLOKI",
          "amount": "182.29400000",
          "gt_amount": "0.001079"
        }
      ]
    ]
    

##  获取UID转帐历史纪录🔒 需要认证

GET`/wallet/push`

GET `/wallet/push`

_获取UID转帐历史纪录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
id | 请求参数 | integer(int32) | 否 | 订单ID  
from | 请求参数 | integer(int32) | 否 | 查询记录的起始时间,不指定则默认从当前时间开始向前推7天,秒级Unix的时间戳  
to | 请求参数 | integer(int32) | 否 | 查询记录的结束时间,不指定则默认为当前时间,秒级Unix的时间戳  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量，默认值是 100  
offset | 请求参数 | integer(int32) | 否 | 列表返回的偏移量，从 0 开始  
transaction_type | 请求参数 | string | 否 | 列表返回订单类型 `withdraw`, `deposit`,默认为`withdraw`.  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | [UidPushOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | integer(int64) | 订单 ID  
» push_uid | integer(int64) | 发起方用户ID  
» receive_uid | integer(int64) | 接收方用户ID  
» currency | string | 币种名称  
» amount | string | 转账数量  
» create_time | integer(int64) | 创建时间  
» status | string | 提现状态:  
  
\- CREATING: 创建中  
\- PENDING: 等待接收 (请联系对方在 Gate 官网接受转帐)  
\- CANCELLING: 撤销中  
\- CANCELLED: 已撤销  
\- REFUSING: 拒绝中  
\- REFUSED: 已拒绝  
\- RECEIVING: 正在接收  
\- RECEIVED: 成功  
» message | string | PENDING原因提示  
» transaction_type | string | 订单类型  
  
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
    
    url = '/wallet/push'
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
    url="/wallet/push"
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
        "id": 111,
        "push_uid": 1132,
        "receive_uid": 12324,
        "currency": "BTC",
        "amount": "1.2",
        "status": "PENDING",
        "create_time": 1706670777,
        "message": "The other party has not completed KYC,There is a security risk in your account, please contact customer service",
        "transaction_type": "withdraw"
      }
    ]
    

##  获取低价值币种列表🔒 需要认证

GET`/wallet/getLowCapExchangeList`

GET `/wallet/getLowCapExchangeList`

_获取低价值币种列表_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功返回字符串数组 | [string]  
  
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
    
    url = '/wallet/getLowCapExchangeList'
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
    url="/wallet/getLowCapExchangeList"
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

> 成功返回字符串数组
    
    
    [
      "0DOG",
      "100X",
      "1ART",
      "1INCH3L",
      "1INCH3S",
      "10N8",
      "20EX",
      "3AC",
      "3AC_OLD",
      "3KM",
      "4"
    ]
    

#  模型

##  TradeFee

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user_id | integer(int64) | false | none | 用户 ID  
taker_fee | string | false | none | 现货 taker 费率  
maker_fee | string | false | none | 现货 maker 费率  
rpi_maker_fee | string | false | none | 现货 RPI MM maker 费率  
gt_discount | boolean | false | none | 是否开启 GT 抵扣折扣  
gt_taker_fee | string | false | none | GT 抵扣 taker 费率，未开启 GT 抵扣则为 0  
gt_maker_fee | string | false | none | GT 抵扣 maker 费率，未开启 GT 抵扣则为 0  
loan_fee | string | false | none | 杠杆理财的费率  
point_type | string | false | none | 点卡类型，0 - 初版点卡，1 - 202009 启用的新点卡  
futures_taker_fee | string | false | none | 合约 taker 费率  
futures_maker_fee | string | false | none | 合约 maker 费率  
futures_rpi_maker_fee | string | false | none | 合约 RPI MM maker 费率  
delivery_taker_fee | string | false | none | 交割合约 taker 费率  
delivery_maker_fee | string | false | none | 交割合约 maker 费率  
debit_fee | integer | false | none | 费率抵扣类型 , 1 - GT抵扣 , 2 - 点卡抵扣 , 3 - VIP费率  
rpi_mm | integer | false | none | RPI MM等级  
      
    
    {
      "user_id": 0,
      "taker_fee": "string",
      "maker_fee": "string",
      "rpi_maker_fee": "string",
      "gt_discount": true,
      "gt_taker_fee": "string",
      "gt_maker_fee": "string",
      "loan_fee": "string",
      "point_type": "string",
      "futures_taker_fee": "string",
      "futures_maker_fee": "string",
      "futures_rpi_maker_fee": "string",
      "delivery_taker_fee": "string",
      "delivery_maker_fee": "string",
      "debit_fee": 0,
      "rpi_mm": 0
    }
    
    

##  TransferOrderStatus

_TransferOrderStatus_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
tx_id | string | false | none | 操作单号  
status | string | false | none | 划转状态，PENDING - 处理中，SUCCESS - 划转成功，FAIL - 划转失败，PARTIAL_SUCCESS - 部分成功（子子划转时会出现此状态）  
      
    
    {
      "tx_id": "string",
      "status": "string"
    }
    
    

##  SubAccountFuturesBalance

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
uid | string | false | none | 用户 ID  
available | object | false | none | 各结算账户信息  
» **additionalProperties** | object | false | none | none  
»» total | string | false | none | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
»» unrealised_pnl | string | false | none | 未实现盈亏  
»» position_margin | string | false | none | 已废弃  
»» order_margin | string | false | none | 所有未完成订单的起始保证金  
»» available | string | false | none | 指的是逐仓可用的转出或交易的额度，统一账户下包含授信额度的逐仓可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
»» point | string | false | none | 点卡数额  
»» currency | string | false | none | 结算币种  
»» in_dual_mode | boolean | false | none | 是否为双向持仓模式  
»» enable_credit | boolean | false | none | 是否开启统一账户模式  
»» position_initial_margin | string | false | none | 头寸占用的起始保证金，适用于统一账户模式  
»» maintenance_margin | string | false | none | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
»» bonus | string | false | none | 体验金  
»» enable_evolved_classic | boolean | false | none | 已废弃  
»» cross_order_margin | string | false | none | 全仓挂单保证金，适用于新经典账户保证金模式  
»» cross_initial_margin | string | false | none | 全仓初始保证金，适用于新经典账户保证金模式  
»» cross_maintenance_margin | string | false | none | 全仓维持保证金，适用于新经典账户保证金模式  
»» cross_unrealised_pnl | string | false | none | 全仓未实现盈亏，适用于新经典账户保证金模式  
»» cross_available | string | false | none | 全仓可用额度，适用于新经典账户保证金模式  
»» cross_margin_balance | string | false | none | 全仓保证金余额，适用于新经典账户保证金模式  
»» cross_mmr | string | false | none | 全仓维持保证金率，适用于新经典账户保证金模式  
»» cross_imr | string | false | none | 全仓初始保证金率，适用于新经典账户保证金模式  
»» isolated_position_margin | string | false | none | 逐仓仓位保证金，适用于新经典账户保证金模式  
»» enable_new_dual_mode | boolean | false | none | 已废弃  
»» margin_mode | integer | false | none | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
»» enable_tiered_mm | boolean | false | none | 是否开启梯度式计算维持保证金  
»» enable_dual_plus | boolean | false | none | 是否支持分仓模式  
»» position_mode | string | false | none | 持仓模式 single-单向持仓 dual-双向持仓 dual_plus-分仓  
»» history | object | false | none | 累计统计数据  
»»» dnw | string | false | none | 累计转入转出  
»»» pnl | string | false | none | 累计交易盈亏  
»»» fee | string | false | none | 累计手续费  
»»» refr | string | false | none | 累计获取的推荐人返佣  
»»» fund | string | false | none | 累计资金费用  
»»» point_dnw | string | false | none | 累计点卡转入转出  
»»» point_fee | string | false | none | 累计点卡抵扣手续费  
»»» point_refr | string | false | none | 累计获取的点卡推荐人返佣  
»»» bonus_dnw | string | false | none | 累计体验金转入转出  
»»» bonus_offset | string | false | none | 累计体验金抵扣  
»»» cross_settle | string | false | none | 代表统一账户模式下，合约账户盈利被结算到现货数值。负数代表从合约结算到现货的，正数代表从现货结算到合约的。此数值为累计值  
      
    
    {
      "uid": "string",
      "available": {
        "property1": {
          "total": "string",
          "unrealised_pnl": "string",
          "position_margin": "string",
          "order_margin": "string",
          "available": "string",
          "point": "string",
          "currency": "string",
          "in_dual_mode": true,
          "enable_credit": true,
          "position_initial_margin": "string",
          "maintenance_margin": "string",
          "bonus": "string",
          "enable_evolved_classic": true,
          "cross_order_margin": "string",
          "cross_initial_margin": "string",
          "cross_maintenance_margin": "string",
          "cross_unrealised_pnl": "string",
          "cross_available": "string",
          "cross_margin_balance": "string",
          "cross_mmr": "string",
          "cross_imr": "string",
          "isolated_position_margin": "string",
          "enable_new_dual_mode": true,
          "margin_mode": 0,
          "enable_tiered_mm": true,
          "enable_dual_plus": true,
          "position_mode": "string",
          "history": {}
        },
        "property2": {
          "total": "string",
          "unrealised_pnl": "string",
          "position_margin": "string",
          "order_margin": "string",
          "available": "string",
          "point": "string",
          "currency": "string",
          "in_dual_mode": true,
          "enable_credit": true,
          "position_initial_margin": "string",
          "maintenance_margin": "string",
          "bonus": "string",
          "enable_evolved_classic": true,
          "cross_order_margin": "string",
          "cross_initial_margin": "string",
          "cross_maintenance_margin": "string",
          "cross_unrealised_pnl": "string",
          "cross_available": "string",
          "cross_margin_balance": "string",
          "cross_mmr": "string",
          "cross_imr": "string",
          "isolated_position_margin": "string",
          "enable_new_dual_mode": true,
          "margin_mode": 0,
          "enable_tiered_mm": true,
          "enable_dual_plus": true,
          "position_mode": "string",
          "history": {}
        }
      }
    }
    
    

##  SubAccountTransferRecordItem

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timest | string | false | 只读 | 转账时间戳  
uid | string | false | 只读 | 主账号用户 ID  
sub_account | string | true | none | 子账号用户 ID  
sub_account_type | string | false | none | 操作的子账号交易账户， spot - 现货账户， futures - 永续合约账户， delivery - 交割合约账户, options - 期权账户  
currency | string | true | none | 转账货币名称  
amount | string | true | none | 划转金额  
direction | string | true | none | 资金流向，to - 转入子账号, from - 转出子账号  
source | string | false | 只读 | 转账操作来源  
client_order_id | string | false | none | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
status | string | false | none | 子账户划转记录状态，目前只有success  
      
    
    {
      "timest": "string",
      "uid": "string",
      "sub_account": "string",
      "sub_account_type": "spot",
      "currency": "string",
      "amount": "string",
      "direction": "string",
      "source": "string",
      "client_order_id": "string",
      "status": "string"
    }
    
    

##  DepositAddress

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | true | none | 币种信息  
address | string | true | none | 充值地址  
min_deposit_amount | string | false | none | 最小充值额度  
multichain_addresses | array | false | none | none  
» MultiChainAddressItem | object | false | none | none  
»» chain | string | false | none | 链的名称  
»» address | string | false | none | 充值地址  
»» payment_id | string | false | none | 部分币种充值时必须填写的备注  
»» payment_name | string | false | none | 备注类型, `Tag` 或 `Memo`  
»» obtain_failed | integer | false | none | 地址是否获取成功，0 表示成功，1 表示失败，可能需要重新获取  
»» min_confirms | integer | false | none | 最小确认数  
      
    
    {
      "currency": "string",
      "address": "string",
      "min_deposit_amount": "string",
      "multichain_addresses": [
        {
          "chain": "string",
          "address": "string",
          "payment_id": "string",
          "payment_name": "string",
          "obtain_failed": 0,
          "min_confirms": 0
        }
      ]
    }
    
    

##  ConvertSmallBalance

_小额兑换币种_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | array | false | none | 需要被兑换的币种  
is_all | boolean | false | none | 是否全部兑换  
      
    
    {
      "currency": [
        "string"
      ],
      "is_all": true
    }
    
    

##  WithdrawalRecord

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | 只读 | 交易记录 ID  
txid | string | false | 只读 | 区块转账哈希记录  
block_number | string | false | 只读 | 区块编号  
withdraw_order_id | string | false | none | 用户端订单编号,最长32个，输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
timestamp | string | false | 只读 | 操作时间  
amount | string | true | none | 币的数量  
fee | string | false | 只读 | 手续费  
currency | string | true | none | 币种名称  
address | string | false | none | 提现地址  
type | string | false | none | 业务类型  
fail_reason | string | false | none | 提现失败原因，当 status = CANCEL时有值，其余状态时为空  
timestamp2 | string | false | none | 提现终态时间，即： 提现取消时间或提现成功时间  
当 status = CANCEL 时，对应 取消时间  
当 status = DONE 时，为提现成功时间  
memo | string | false | none | 转账memo等备注信息  
status | string | false | 只读 | 交易状态  
  
\- BCODE: 充值码操作  
\- CANCEL: 已取消  
\- CANCELPEND: 取消提现中  
\- DONE: 完成  
\- EXTPEND: 已经发送等待确认  
\- FAIL: 链上失败等待确认  
\- FVERIFY: 人脸审核处理中  
\- LOCKED: 钱包侧锁单  
\- MANUAL: 待人工审核  
\- REJECT: 拒绝  
\- REQUEST: 请求中  
\- REVIEW: 审核中  
chain | string | true | none | 提现的链名称  
      
    
    {
      "id": "string",
      "txid": "string",
      "block_number": "string",
      "withdraw_order_id": "string",
      "timestamp": "string",
      "amount": "string",
      "fee": "string",
      "currency": "string",
      "address": "string",
      "type": "string",
      "fail_reason": "string",
      "timestamp2": "string",
      "memo": "string",
      "status": "string",
      "chain": "string"
    }
    
    

##  DepositRecord

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | 只读 | 交易记录 ID  
txid | string | false | 只读 | 区块转账哈希记录  
timestamp | string | false | 只读 | 操作时间  
amount | string | true | none | 币的数量  
currency | string | true | none | 币种名称  
address | string | false | none | 提现地址。提现操作必填  
memo | string | false | none | 转账memo等备注信息  
status | string | false | 只读 | 交易状态  
  
\- BLOCKED: 拒绝充值  
\- DEP_CREDITED: 充值到账，提现未解锁  
\- DONE: 已经给账户增加资金  
\- INVALID: 无效数据  
\- MANUAL: 转人工审核  
\- PEND: 处理中  
\- REVIEW: 充值审核中(合规审查)  
\- TRACK: 跟踪确认数，等待给用户添加资金(现货)  
chain | string | true | none | 提现的链名称  
      
    
    {
      "id": "string",
      "txid": "string",
      "timestamp": "string",
      "amount": "string",
      "currency": "string",
      "address": "string",
      "memo": "string",
      "status": "string",
      "chain": "string"
    }
    
    

##  SubAccountCrossMarginBalance

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
uid | string | false | none | 用户 ID  
available | object | false | none | none  
» user_id | integer(int64) | false | none | 全仓帐户用户ID，如果 0 代表这个子帐号尚未开通全仓帐户  
» locked | boolean | false | none | 账户是否被锁定  
» balances | object | false | none | none  
»» CrossMarginBalance | object | false | none | none  
»»» available | string | false | none | 可用额度  
»»» freeze | string | false | none | 被锁定的额度  
»»» borrowed | string | false | none | 借入额度  
»»» interest | string | false | none | 未还利息  
»» total | string | false | none | 折算成 USDT 的账户总资产，即所有币种(不包括点卡)的 `(available+freeze)*price*discount` 之和  
»» borrowed | string | false | none | 折算成 USDT 的账户总借入数量，即所有币种(不包括点卡)的 `borrowed*price*discount` 之和  
»» borrowed_net | string | false | none | 折算成 USDT 的账户总借入数量 * 放大系数  
»» net | string | false | none | 折算成 USDT 的净资产  
»» leverage | string | false | none | 杠杆倍数  
»» interest | string | false | none | 折算成 USDT 的账户未接利息的总和，即所有币种(不包括点卡)的 `interest*price*discount` 之和  
»» risk | string | false | none | 风险率，风险率小于 110% 会被爆仓，计算方式 `total / (borrowed+interest)`  
»» total_initial_margin | string | false | none | 总初始保证金  
»» total_margin_balance | string | false | none | 总保证金余额  
»» total_maintenance_margin | string | false | none | 总维持保证金  
»» total_initial_margin_rate | string | false | none | 总初始保证金率  
»» total_maintenance_margin_rate | string | false | none | 总维持保证金率  
»» total_available_margin | string | false | none | 可用的保证金额度  
      
    
    {
      "uid": "string",
      "available": {
        "user_id": 0,
        "locked": true,
        "balances": {
          "property1": {},
          "property2": {}
        },
        "total": "string",
        "borrowed": "string",
        "borrowed_net": "string",
        "net": "string",
        "leverage": "string",
        "interest": "string",
        "risk": "string",
        "total_initial_margin": "string",
        "total_margin_balance": "string",
        "total_maintenance_margin": "string",
        "total_initial_margin_rate": "string",
        "total_maintenance_margin_rate": "string",
        "total_available_margin": "string"
      }
    }
    
    

##  TransactionID

_TransactionID_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
tx_id | integer(int64) | false | none | 操作单号  
      
    
    {
      "tx_id": 0
    }
    
    

##  Transfer

*转入转出账户列表:

  * `spot`: 现货账户
  * `margin`: 杠杆账户
  * `futures`: 永续合约账户
  * `delivery`: 交割合约账户
  * `options`: 期权账户

  * 

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | true | none | 转账货币名称。关联合约账户时，currency 可以设置的值为`POINT`(即点卡) 和支持的结算货币(如 `BTC`, `USDT`)  
from | string | true | none | 转出账户  
to | string | true | none | 转入账户  
amount | string | true | none | 划转金额，最多支持8位小数，必须大于0  
currency_pair | string | false | none | 杠杆交易对。转入或转出杠杆账户时必填  
settle | string | false | none | 合约结算币种。 转入转出合约账户时必填  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
from | spot  
from | margin  
from | futures  
from | delivery  
from | options  
to | spot  
to | margin  
to | futures  
to | delivery  
to | options  
      
    
    {
      "currency": "string",
      "from": "spot",
      "to": "spot",
      "amount": "string",
      "currency_pair": "string",
      "settle": "string"
    }
    
    

##  WithdrawStatus

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种  
name | string | false | none | 币种名称  
name_cn | string | false | none | 币种中文名称  
deposit | string | false | none | 充值手续费  
withdraw_percent | string | false | none | 提现手续费率百分比  
withdraw_fix | string | false | none | 固定提现手续费用  
withdraw_day_limit | string | false | none | 日提现额度  
withdraw_amount_mini | string | false | none | 最少提现额度  
withdraw_day_limit_remain | string | false | none | 剩余日提现额度  
withdraw_eachtime_limit | string | false | none | 单次最多提现额度  
withdraw_fix_on_chains | object | false | none | 多链的固定提现手续费用  
» **additionalProperties** | string | false | none | none  
withdraw_percent_on_chains | object | false | none | 多链的百分比提现手续费用  
» **additionalProperties** | string | false | none | none  
      
    
    {
      "currency": "string",
      "name": "string",
      "name_cn": "string",
      "deposit": "string",
      "withdraw_percent": "string",
      "withdraw_fix": "string",
      "withdraw_day_limit": "string",
      "withdraw_amount_mini": "string",
      "withdraw_day_limit_remain": "string",
      "withdraw_eachtime_limit": "string",
      "withdraw_fix_on_chains": {
        "property1": "string",
        "property2": "string"
      },
      "withdraw_percent_on_chains": {
        "property1": "string",
        "property2": "string"
      }
    }
    
    

##  SmallBalanceHistory

_小额兑换币种_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | 只读 | 订单ID  
currency | string | false | 只读 | 兑换币种  
amount | string | false | 只读 | 兑换数量  
gt_amount | string | false | 只读 | 被兑换到的 GT 数量  
create_time | integer(int64) | false | 只读 | 兑换时间(秒)  
      
    
    {
      "id": "string",
      "currency": "string",
      "amount": "string",
      "gt_amount": "string",
      "create_time": 0
    }
    
    

##  SmallBalance

_小额兑换币种_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种  
available_balance | string | false | none | 可转换金额  
estimated_as_btc | string | false | none | 预计用 BTC 计价金额  
convertible_to_gt | string | false | none | 预计可转换成多少 GT  
      
    
    {
      "currency": "string",
      "available_balance": "string",
      "estimated_as_btc": "string",
      "convertible_to_gt": "string"
    }
    
    

##  TotalBalance

_用户总资产信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
total | object | false | none | 换算成目标币种的账户总额  
» amount | string | false | none | 账户总额数字  
» currency | string | false | none | 币种  
» unrealised_pnl | string | false | none | 未实现盈亏总和,这个字段只会在futures,options,delivery,total 账户中出现  
» borrowed | string | false | none | 杠杆借贷总和,这个字段只会在margin,cross_margin账户中出现  
details | object | false | none | 各账户总额  
  
\- cross_margin: 全仓杠杆账户  
\- spot: 现货账户  
\- finance: 金融账户  
\- margin: 杠杆账户  
\- quant: 量化账户  
\- futures: 永续合约账户  
\- delivery: 交割合约账户  
\- warrant: warrant 账户  
\- cbbc: 牛熊证账户  
\- meme_box: alpha账户  
\- options: 期权账户  
\- payment: 支付账户  
» **additionalProperties** | TotalBalance/properties/total | false | none | 换算成目标币种的账户总额  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
currency | BTC  
currency | CNY  
currency | USD  
currency | USDT  
      
    
    {
      "total": {
        "amount": "string",
        "currency": "BTC",
        "unrealised_pnl": "string",
        "borrowed": "string"
      },
      "details": {
        "property1": {
          "amount": "string",
          "currency": "BTC",
          "unrealised_pnl": "string",
          "borrowed": "string"
        },
        "property2": {
          "amount": "string",
          "currency": "BTC",
          "unrealised_pnl": "string",
          "borrowed": "string"
        }
      }
    }
    
    

##  SubAccountMarginBalance

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
uid | string | false | none | 用户 ID  
available | array | false | none | 账户余额信息  
» _None_ | object | false | none | 某交易对的杠杆账户信息，`base` 对应交易货币的账户信息，`quote` 对应计价货币的账户信息  
»» currency_pair | string | false | none | 交易对  
»» account_type | string | false | none | 账户类型。mmr-维持保证金率账户，inactive - 市场未激活  
»» leverage | string | false | none | 用户当前市场杠杆倍数  
»» locked | boolean | false | none | 账户是否被锁定  
»» risk | string | false | none | 已废弃  
»» mmr | string | false | none | 该逐仓杠杆账户当前维持保证金率  
»» base | object | false | none | 货币账户信息  
»»» currency | string | false | none | 货币名称  
»»» available | string | false | none | 可用于杠杆交易的额度，available = 保证金 + borrowed  
»»» locked | string | false | none | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
»»» borrowed | string | false | none | 借入资金  
»»» interest | string | false | none | 未还利息  
»» quote | SubAccountMarginBalance/properties/available/items/properties/base | false | none | 货币账户信息  
      
    
    {
      "uid": "string",
      "available": [
        {
          "currency_pair": "string",
          "account_type": "string",
          "leverage": "string",
          "locked": true,
          "risk": "string",
          "mmr": "string",
          "base": {},
          "quote": {}
        }
      ]
    }
    
    

##  UidPushOrder

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 订单 ID  
push_uid | integer(int64) | false | none | 发起方用户ID  
receive_uid | integer(int64) | false | none | 接收方用户ID  
currency | string | false | none | 币种名称  
amount | string | false | none | 转账数量  
create_time | integer(int64) | false | none | 创建时间  
status | string | false | none | 提现状态:  
  
\- CREATING: 创建中  
\- PENDING: 等待接收 (请联系对方在 Gate 官网接受转帐)  
\- CANCELLING: 撤销中  
\- CANCELLED: 已撤销  
\- REFUSING: 拒绝中  
\- REFUSED: 已拒绝  
\- RECEIVING: 正在接收  
\- RECEIVED: 成功  
message | string | false | none | PENDING原因提示  
transaction_type | string | false | none | 订单类型  
      
    
    {
      "id": 0,
      "push_uid": 0,
      "receive_uid": 0,
      "currency": "string",
      "amount": "string",
      "create_time": 0,
      "status": "string",
      "message": "string",
      "transaction_type": "string"
    }
    
    

##  SubAccountBalance

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
uid | string | false | none | 用户 ID  
available | object | false | none | 币种可用余额  
» **additionalProperties** | string | false | none | none  
locking | object | false | none | 币种锁定金额  
» **additionalProperties** | string | false | none | none  
      
    
    {
      "uid": "string",
      "available": {
        "property1": "string",
        "property2": "string"
      },
      "locking": {
        "property1": "string",
        "property2": "string"
      }
    }
    
    

##  SubAccountTransfer

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
sub_account | string | true | none | 子账号用户 ID  
sub_account_type | string | false | none | 操作的子账号交易账户， spot - 现货账户， futures - 永续合约账户， delivery - 交割合约账户, options - 期权账户  
currency | string | true | none | 转账货币名称  
amount | string | true | none | 划转金额，最多支持8位小数，必须大于0  
direction | string | true | none | 资金流向，to - 转入子账号, from - 转出子账号  
client_order_id | string | false | none | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
      
    
    {
      "sub_account": "string",
      "sub_account_type": "spot",
      "currency": "string",
      "amount": "string",
      "direction": "string",
      "client_order_id": "string"
    }
    
    

##  SavedAddress

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种  
chain | string | false | none | 链名称  
address | string | false | none | 地址  
name | string | false | none | 名称  
tag | string | false | none | 标签  
verified | string | false | none | 是否通过验证 0-未验证, 1-已验正  
      
    
    {
      "currency": "string",
      "chain": "string",
      "address": "string",
      "name": "string",
      "tag": "string",
      "verified": "string"
    }
    
    

##  SubAccountToSubAccount

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | true | none | 转账货币名称  
sub_account_type | string | false | none | 转出的子账号交易账户 (已弃用, 改用 `sub_account_from_type` 和 `sub_account_to_type`)  
sub_account_from | string | true | none | 转出子账号用户 ID  
sub_account_from_type | string | true | none | 转出的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
sub_account_to | string | true | none | 转入子账号用户 ID  
sub_account_to_type | string | true | none | 转入的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
amount | string | true | none | 划转金额，最多支持8位小数，必须大于0  
      
    
    {
      "currency": "string",
      "sub_account_type": "string",
      "sub_account_from": "string",
      "sub_account_from_type": "string",
      "sub_account_to": "string",
      "sub_account_to_type": "string",
      "amount": "string"
    }
    
    

##  CurrencyChain

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
chain | string | false | none | 链名称  
name_cn | string | false | none | 链的中文名称  
name_en | string | false | none | 链的英文名称  
contract_address | string | false | none | 币种智能合约地址，如果没有地址则为空字串  
is_disabled | integer(int32) | false | none | 是否禁用，0 表示未禁用  
is_deposit_disabled | integer(int32) | false | none | 充值是否禁用，0 表示未禁用  
is_withdraw_disabled | integer(int32) | false | none | 提现是否禁用，0 表示未禁用  
decimal | string | false | none | 提币精度  
is_tag | integer | false | none | 是否包含tag  
      
    
    {
      "chain": "string",
      "name_cn": "string",
      "name_en": "string",
      "contract_address": "string",
      "is_disabled": 0,
      "is_deposit_disabled": 0,
      "is_withdraw_disabled": 0,
      "decimal": "string",
      "is_tag": 0
    }