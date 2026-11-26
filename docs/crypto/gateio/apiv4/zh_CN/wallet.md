---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/wallet
api_type: Account
updated_at: 2026-11-26 18:59:22.497679
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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
CurrencyChain |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
chain | string | Optional |  | 链名称  
name_cn | string | Optional |  | 链的中文名称  
name_en | string | Optional |  | 链的英文名称  
contract_address | string | Optional |  | 币种智能合约地址，如果没有地址则为空字串  
is_disabled | integer(int32) | Optional |  | 是否禁用，0 表示未禁用  
is_deposit_disabled | integer(int32) | Optional |  | 充值是否禁用，0 表示未禁用  
is_withdraw_disabled | integer(int32) | Optional |  | 提现是否禁用，0 表示未禁用  
decimal | string | Optional |  | 提币精度  
is_tag | integer | Optional |  | 是否包含tag  
  
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

类型 | 约束  
---|---  
DepositAddress | required: ["currency","address"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种信息  
address | string | Required |  | 充值地址  
min_deposit_amount | string | Optional |  | 最小充值额度  
multichain_addresses | array | Optional |  |   
  
**multichain_addresses**

类型 | 约束  
---|---  
array |   
  
**multichain_addresses / items**

MultiChainAddressItem

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
chain | string | Optional |  | 链的名称  
address | string | Optional |  | 充值地址  
payment_id | string | Optional |  | 部分币种充值时必须填写的备注，例如 Tag 或 Memo。  
payment_name | string | Optional |  | 备注类型, `Tag` 或 `Memo`  
obtain_failed | integer | Optional |  | 地址获取是否失败：0 获取成功；1 获取失败，可能需要重新获取。  
min_confirms | integer | Optional |  | 最小确认数  
  
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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
WithdrawalRecord | required: ["currency","amount","chain"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 交易记录 ID  
txid | string | Optional | readOnly: true | 区块转账哈希记录  
block_number | string | Optional | readOnly: true | 区块编号  
withdraw_order_id | string | Optional |  | 用户端订单编号,最长32个，输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
timestamp | string | Optional | readOnly: true | 操作时间  
amount | string | Required |  | 币的数量  
fee | string | Optional | readOnly: true | 手续费  
currency | string | Required |  | 币种名称  
address | string | Optional |  | 提现地址  
type | string | Optional |  | 业务类型  
fail_reason | string | Optional |  | 提现失败原因，当 status = CANCEL时有值，其余状态时为空  
timestamp2 | string | Optional |  | 提现终态时间，即： 提现取消时间或提现成功时间  
当 status = CANCEL 时，对应 取消时间  
当 status = DONE 时，为提现成功时间  
memo | string | Optional |  | 转账memo等备注信息  
status | string | Optional | readOnly: true | 交易状态  
  
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
chain | string | Required |  | 提现的链名称  
  
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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
DepositRecord | required: ["currency","amount","chain"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 交易记录 ID  
txid | string | Optional | readOnly: true | 区块转账哈希记录  
timestamp | string | Optional | readOnly: true | 操作时间  
amount | string | Required |  | 币的数量  
currency | string | Required |  | 币种名称  
address | string | Optional |  | 提现地址。提现操作必填  
memo | string | Optional |  | 转账memo等备注信息  
status | string | Optional | readOnly: true | 交易状态  
  
\- BLOCKED: 拒绝充值  
\- DEP_CREDITED: 充值到账，提现未解锁  
\- DONE: 已经给账户增加资金  
\- INVALID: 无效数据  
\- MANUAL: 转人工审核  
\- PEND: 处理中  
\- REVIEW: 充值审核中(合规审查)  
\- TRACK: 跟踪确认数，等待给用户添加资金(现货)  
refund_status | string | Optional | readOnly: true | 拦截充值的退款状态。仅当充值记录存在拦截充值退款记录且退款状态非空时返回该字段，无退款记录或退款状态为空时不返回  
  
\- REFUNDING: 退款中  
\- REFUNDED: 退款完成  
\- REFUND_FAILED: 退款失败  
\- REJECTED: 退款被拒绝  
chain | string | Required |  | 提现的链名称  
  
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
        "id": "d123456",
        "timestamp": "1780896616",
        "currency": "USDT",
        "address": "0x1234567890abcdef",
        "txid": "0xabcdef",
        "amount": "10",
        "memo": "",
        "status": "BLOCKED",
        "refund_status": "REFUNDING",
        "chain": "ETH"
      },
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
    

##  查询交易账户划转订单🔒 需要认证

GET`/wallet/transfers`

GET `/wallet/transfers`

_查询交易账户划转订单_

根据划转接口返回的 tx_id 查询当前用户的交易账户划转订单详情

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
tx_id | 请求参数 | string | 是 | 划转操作单号  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 交易账户划转订单获取成功 | AccountTransferDetail  
  
### 返回格式

状态码 **200**

交易账户划转订单详情

类型 | 约束  
---|---  
AccountTransferDetail | required: ["tx_id","status","currency","amount","from_account","to_account","settle","currency_pair"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tx_id | string | Required | readOnly: true | 划转操作单号  
status | string | Required | enum: ["pending","success","fail"]  
readOnly: true | 划转状态：  
  
\- `pending`：处理中  
\- `success`：划转成功  
\- `fail`：划转失败  
currency | string | Required | readOnly: true | 划转币种  
amount | string | Required | readOnly: true | 划转数量  
from_account | string | Required | enum: ["spot","margin","futures","delivery","options","unknown"]  
readOnly: true | 转出账户类型：  
  
\- `spot`：现货账户  
\- `margin`：杠杆账户  
\- `futures`：永续合约账户  
\- `delivery`：交割合约账户  
\- `options`：期权账户  
\- `unknown`：无法识别的账户类型  
to_account | string | Required | enum: ["spot","margin","futures","delivery","options","unknown"]  
readOnly: true | 转入账户类型：  
  
\- `spot`：现货账户  
\- `margin`：杠杆账户  
\- `futures`：永续合约账户  
\- `delivery`：交割合约账户  
\- `options`：期权账户  
\- `unknown`：无法识别的账户类型  
settle | string|null | Required | nullable: true  
readOnly: true | futures、delivery、options 划转时返回结算币种，否则返回 null  
currency_pair | string|null | Required | nullable: true  
readOnly: true | margin 划转时返回交易对，否则返回 null  
  
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
    query_param = 'tx_id=59636381286'
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
    url="/wallet/transfers"
    query_param="tx_id=59636381286"
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
      "tx_id": "59636381286",
      "status": "success",
      "currency": "USDT",
      "amount": "10",
      "from_account": "spot",
      "to_account": "futures",
      "settle": "usdt",
      "currency_pair": null
    }
    

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
currency | body | string | 是 | 转账货币名称。关联合约账户时，currency 可以设置的值为`POINT`(即点卡) 和支持的结算货币(如 `BTC`, `USDT`)  
  
from | body | string | 是 | 转出账户  
to | body | string | 是 | 转入账户  
amount | body | string | 是 | 划转金额，最多支持8位小数，必须大于0  
currency_pair | body | string | 否 | 杠杆交易对。转入或转出杠杆账户时必填  
settle | body | string | 否 | 合约结算币种。 转入转出合约账户时必填  
  
####  详细描述

** currency**: 转账货币名称。关联合约账户时，currency 可以设置的值为`POINT`(即点卡) 和支持的结算货币(如 `BTC`, `USDT`)  

####  枚举值列表

枚举值列表参数 | 值  
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
  
####  请求体结构

转入转出账户列表:

  * `spot`: 现货账户
  * `margin`: 杠杆账户
  * `futures`: 永续合约账户
  * `delivery`: 交割合约账户
  * `options`: 期权账户

请求体结构类型 | 约束  
---|---  
Transfer | required: ["currency","from","to","amount"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 转账货币名称。关联合约账户时，currency 可以设置的值为`POINT`(即点卡) 和支持的结算货币(如 `BTC`, `USDT`)  
from | string | Required | enum: ["spot","margin","futures","delivery","options"] | 转出账户  
to | string | Required | enum: ["spot","margin","futures","delivery","options"] | 转入账户  
amount | string | Required |  | 划转金额，最多支持8位小数，必须大于0  
currency_pair | string | Optional |  | 杠杆交易对。转入或转出杠杆账户时必填  
settle | string | Optional |  | 合约结算币种。 转入转出合约账户时必填  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 转账操作成功 | TransactionID  
  
### 返回格式

状态码 **200**

TransactionID

类型 | 约束  
---|---  
TransactionID |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tx_id | integer(int64) | Optional |  | 操作单号  
  
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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
SubAccountTransferRecordItem | required: ["currency","sub_account","direction","amount"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
timest | string | Optional | readOnly: true | 转账时间戳  
uid | string | Optional | readOnly: true | 主账号用户 ID  
sub_account | string | Required |  | 子账号用户 ID  
sub_account_type | string | Optional | default: "spot" | 操作的子账号交易账户， spot - 现货账户， futures - 永续合约账户， delivery - 交割合约账户, options - 期权账户  
currency | string | Required |  | 转账货币名称  
amount | string | Required |  | 划转金额  
direction | string | Required |  | 资金流向，to - 转入子账号, from - 转出子账号  
source | string | Optional | readOnly: true | 转账操作来源  
client_order_id | string | Optional |  | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
status | string | Optional |  | 子账户划转记录状态，目前只有success  
  
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
sub_account | body | string | 是 | 子账号用户 ID  
sub_account_type | body | string | 否 | 操作的子账号交易账户， spot - 现货账户， futures - 永续合约账户， delivery - 交割合约账户, options - 期权账户  
currency | body | string | 是 | 转账货币名称  
amount | body | string | 是 | 划转金额，最多支持8位小数，必须大于0  
direction | body | string | 是 | 资金流向，to - 转入子账号, from - 转出子账号  
client_order_id | body | string | 否 | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
  
####  请求体结构

请求体结构类型 | 约束  
---|---  
SubAccountTransfer | required: ["currency","sub_account","direction","amount"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
sub_account | string | Required |  | 子账号用户 ID  
sub_account_type | string | Optional | default: "spot" | 操作的子账号交易账户， spot - 现货账户， futures - 永续合约账户， delivery - 交割合约账户, options - 期权账户  
currency | string | Required |  | 转账货币名称  
amount | string | Required |  | 划转金额，最多支持8位小数，必须大于0  
direction | string | Required |  | 资金流向，to - 转入子账号, from - 转出子账号  
client_order_id | string | Optional |  | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 转账操作成功 | TransactionID  
  
### 返回格式

状态码 **200**

TransactionID

类型 | 约束  
---|---  
TransactionID |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tx_id | integer(int64) | Optional |  | 操作单号  
  
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
currency | body | string | 是 | 转账货币名称  
sub_account_type | body | string | 否 | 转出的子账号交易账户 (已弃用, 改用 `sub_account_from_type` 和 `sub_account_to_type`)  
sub_account_from | body | string | 是 | 转出子账号用户 ID  
sub_account_from_type | body | string | 是 | 转出的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
sub_account_to | body | string | 是 | 转入子账号用户 ID  
sub_account_to_type | body | string | 是 | 转入的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
amount | body | string | 是 | 划转金额，最多支持8位小数，必须大于0  
  
####  请求体结构

请求体结构类型 | 约束  
---|---  
SubAccountToSubAccount | required: ["currency","sub_account_from","sub_account_from_type","sub_account_to","sub_account_to_type","amount"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 转账货币名称  
sub_account_type | string | Optional |  | 转出的子账号交易账户 (已弃用, 改用 `sub_account_from_type` 和 `sub_account_to_type`)  
sub_account_from | string | Required |  | 转出子账号用户 ID  
sub_account_from_type | string | Required |  | 转出的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
sub_account_to | string | Required |  | 转入子账号用户 ID  
sub_account_to_type | string | Required |  | 转入的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
amount | string | Required |  | 划转金额，最多支持8位小数，必须大于0  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 转账操作成功 | TransactionID  
  
### 返回格式

状态码 **200**

TransactionID

类型 | 约束  
---|---  
TransactionID |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tx_id | integer(int64) | Optional |  | 操作单号  
  
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

TransferOrderStatus

类型 | 约束  
---|---  
TransferOrderStatus |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tx_id | string | Optional |  | 操作单号  
status | string | Optional |  | 划转状态，PENDING - 处理中，SUCCESS - 划转成功，FAIL - 划转失败，PARTIAL_SUCCESS - 部分成功（子子划转时会出现此状态）  
  
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
    

##  查询币种提现手续费与额度信息，可按 currency 筛选。🔒 需要认证

GET`/wallet/withdraw_status`

GET `/wallet/withdraw_status`

_查询币种提现手续费与额度信息，可按 currency 筛选。_

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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
WithdrawStatus |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种  
name | string | Optional |  | 币种名称  
name_cn | string | Optional |  | 币种中文名称  
deposit | string | Optional |  | 充值手续费  
withdraw_percent | string | Optional |  | 提现手续费率百分比  
withdraw_fix | string | Optional |  | 固定提现手续费用  
withdraw_day_limit | string | Optional |  | 日提现额度  
withdraw_amount_mini | string | Optional |  | 最少提现额度  
withdraw_day_limit_remain | string | Optional |  | 剩余日提现额度  
withdraw_eachtime_limit | string | Optional |  | 单次最多提现额度  
withdraw_fix_on_chains | object | Optional |  | 多链的固定提现手续费用  
withdraw_percent_on_chains | object | Optional |  | 多链的百分比提现手续费用  
  
**items / withdraw_fix_on_chains**

多链的固定提现手续费用

类型 | 约束  
---|---  
object |   
  
**items / withdraw_fix_on_chains / additionalProperties**

类型 | 约束  
---|---  
string |   
  
**items / withdraw_percent_on_chains**

多链的百分比提现手续费用

类型 | 约束  
---|---  
object |   
  
**items / withdraw_percent_on_chains / additionalProperties**

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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
SubAccountBalance |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
uid | string | Optional |  | 用户 ID  
available | object | Optional |  | 币种可用余额  
locking | object | Optional |  | 币种锁定金额  
  
**items / available**

币种可用余额

类型 | 约束  
---|---  
object |   
  
**items / available / additionalProperties**

类型 | 约束  
---|---  
string |   
  
**items / locking**

币种锁定金额

类型 | 约束  
---|---  
object |   
  
**items / locking / additionalProperties**

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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
SubAccountMarginBalance |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
uid | string | Optional |  | 用户 ID  
available | array | Optional |  | 账户余额信息  
  
**items / available**

账户余额信息

类型 | 约束  
---|---  
array |   
  
**items / available / items**

某交易对的杠杆账户信息，`base` 对应交易货币的账户信息，`quote` 对应计价货币的账户信息

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency_pair | string | Optional |  | 交易对  
account_type | string | Optional |  | 账户类型。mmr-维持保证金率账户，inactive - 市场未激活  
leverage | string | Optional |  | 用户当前市场杠杆倍数  
locked | boolean | Optional |  | 账户是否被锁定  
risk | string | Optional |  | 已废弃  
mmr | string | Optional |  | 该逐仓杠杆账户当前维持保证金率  
base | object | Optional |  | 货币账户信息  
quote | object | Optional |  | 货币账户信息  
  
**items / available / items / base**

货币账户信息

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 货币名称  
available | string | Optional |  | 可用于杠杆交易的额度，available = 保证金 + borrowed  
locked | string | Optional |  | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
borrowed | string | Optional |  | 借入资金  
interest | string | Optional |  | 未还利息  
  
**items / available / items / quote**

货币账户信息

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 货币名称  
available | string | Optional |  | 可用于杠杆交易的额度，available = 保证金 + borrowed  
locked | string | Optional |  | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
borrowed | string | Optional |  | 借入资金  
interest | string | Optional |  | 未还利息  
  
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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
SubAccountFuturesBalance |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
uid | string | Optional |  | 用户 ID  
available | object | Optional |  | 各结算账户信息  
  
**items / available**

各结算账户信息

类型 | 约束  
---|---  
object |   
  
**items / available / additionalProperties**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | string | Optional |  | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional |  | 未实现盈亏  
position_margin | string | Optional |  | 已废弃  
order_margin | string | Optional |  | 所有未完成订单的起始保证金  
available | string | Optional |  | 指的是逐仓可用的转出或交易的额度，统一账户下包含授信额度的逐仓可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
point | string | Optional |  | 点卡数额  
currency | string | Optional |  | 结算币种  
in_dual_mode | boolean | Optional |  | 是否为双向持仓模式  
enable_credit | boolean | Optional |  | 是否开启统一账户模式  
position_initial_margin | string | Optional |  | 头寸占用的起始保证金，适用于统一账户模式  
maintenance_margin | string | Optional |  | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
bonus | string | Optional |  | 体验金  
enable_evolved_classic | boolean | Optional |  | 已废弃  
cross_order_margin | string | Optional |  | 全仓挂单保证金，适用于新经典账户保证金模式  
cross_initial_margin | string | Optional |  | 全仓初始保证金，适用于新经典账户保证金模式  
cross_maintenance_margin | string | Optional |  | 全仓维持保证金，适用于新经典账户保证金模式  
cross_unrealised_pnl | string | Optional |  | 全仓未实现盈亏，适用于新经典账户保证金模式  
cross_available | string | Optional |  | 全仓可用额度，适用于新经典账户保证金模式  
cross_margin_balance | string | Optional |  | 全仓保证金余额，适用于新经典账户保证金模式  
cross_mmr | string | Optional |  | 全仓维持保证金率，适用于新经典账户保证金模式  
cross_imr | string | Optional |  | 全仓初始保证金率，适用于新经典账户保证金模式  
isolated_position_margin | string | Optional |  | 逐仓仓位保证金，适用于新经典账户保证金模式  
enable_new_dual_mode | boolean | Optional |  | 已废弃  
margin_mode | integer | Optional |  | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
enable_tiered_mm | boolean | Optional |  | 是否开启梯度式计算维持保证金  
enable_dual_plus | boolean | Optional |  | 是否支持分仓模式  
position_mode | string | Optional |  | 持仓模式 single-单向持仓 dual-双向持仓 dual_plus-分仓  
history | object | Optional |  | 累计统计数据  
  
**items / available / additionalProperties / history**

累计统计数据

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
dnw | string | Optional |  | 累计转入转出  
pnl | string | Optional |  | 累计交易盈亏  
fee | string | Optional |  | 累计手续费  
refr | string | Optional |  | 累计获取的推荐人返佣  
fund | string | Optional |  | 累计资金费用  
point_dnw | string | Optional |  | 累计点卡转入转出  
point_fee | string | Optional |  | 累计点卡抵扣手续费  
point_refr | string | Optional |  | 累计获取的点卡推荐人返佣  
bonus_dnw | string | Optional |  | 累计体验金转入转出  
bonus_offset | string | Optional |  | 累计体验金抵扣  
cross_settle | string | Optional |  | 代表统一账户模式下，合约账户盈利被结算到现货数值。负数代表从合约结算到现货的，正数代表从现货结算到合约的。此数值为累计值  
  
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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
SubAccountCrossMarginBalance |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
uid | string | Optional |  | 用户 ID  
available | object | Optional |  |   
  
**items / available**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | 全仓帐户用户ID，如果 0 代表这个子帐号尚未开通全仓帐户  
locked | boolean | Optional |  | 账户是否被锁定  
balances | object | Optional |  |   
total | string | Optional |  | 折算成 USDT 的账户总资产，即所有币种(不包括点卡)的 `(available+freeze)*price*discount` 之和  
borrowed | string | Optional |  | 折算成 USDT 的账户总借入数量，即所有币种(不包括点卡)的 `borrowed*price*discount` 之和  
borrowed_net | string | Optional |  | 折算成 USDT 的账户总借入数量 * 放大系数  
net | string | Optional |  | 折算成 USDT 的净资产  
leverage | string | Optional |  | 杠杆倍数  
interest | string | Optional |  | 折算成 USDT 的账户未接利息的总和，即所有币种(不包括点卡)的 `interest*price*discount` 之和  
risk | string | Optional |  | 风险率，风险率小于 110% 会被爆仓，计算方式 `total / (borrowed+interest)`  
total_initial_margin | string | Optional |  | 总初始保证金  
total_margin_balance | string | Optional |  | 总保证金余额  
total_maintenance_margin | string | Optional |  | 总维持保证金  
total_initial_margin_rate | string | Optional |  | 总初始保证金率  
total_maintenance_margin_rate | string | Optional |  | 总维持保证金率  
total_available_margin | string | Optional |  | 可用的保证金额度  
  
**items / available / balances**

类型 | 约束  
---|---  
object |   
  
**items / available / balances / additionalProperties**

CrossMarginBalance

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
available | string | Optional |  | 可用额度  
freeze | string | Optional |  | 被锁定的额度  
borrowed | string | Optional |  | 借入额度  
interest | string | Optional |  | 未还利息  
  
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
    

##  查询提币地址簿地址🔒 需要认证

GET`/wallet/saved_address`

GET `/wallet/saved_address`

_查询提币地址簿地址_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 币种  
chain | 请求参数 | string | 否 | 链名称  
  
verified | 请求参数 | string | 否 | 1 是免验证地址，0 是普通地址，空字符串表示不限制  
  
limit | 请求参数 | string | 否 | 列表返回的最大数量, 最多 100  
  
page | 请求参数 | integer | 否 | 页码  
  
####  详细描述

**chain** : 链名称  

**verified** : 1 是免验证地址，0 是普通地址，空字符串表示不限制  

**limit** : 列表返回的最大数量, 最多 100  

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表获取成功 | [SavedAddress]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
SavedAddress |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种  
chain | string | Optional |  | 链名称  
address | string | Optional |  | 地址  
name | string | Optional |  | 名称  
tag | string | Optional |  | 标签  
verified | string | Optional |  | 是否通过验证 0-未验证, 1-已验正  
  
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
    url="/wallet/saved_address"
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

类型 | 约束  
---|---  
TradeFee |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | 用户 ID  
taker_fee | string | Optional |  | 现货 taker 费率  
maker_fee | string | Optional |  | 现货 maker 费率  
rpi_maker_fee | string | Optional |  | 现货 RPI MM maker 费率  
gt_discount | boolean | Optional |  | 是否开启 GT 抵扣折扣  
gt_taker_fee | string | Optional |  | GT 抵扣 taker 费率，未开启 GT 抵扣则为 0  
gt_maker_fee | string | Optional |  | GT 抵扣 maker 费率，未开启 GT 抵扣则为 0  
loan_fee | string | Optional |  | 杠杆理财的费率  
point_type | string | Optional |  | 点卡类型，0 - 初版点卡，1 - 202009 启用的新点卡  
futures_taker_fee | string | Optional |  | 合约 taker 费率  
futures_maker_fee | string | Optional |  | 合约 maker 费率  
futures_rpi_maker_fee | string | Optional |  | 合约 RPI MM maker 费率  
delivery_taker_fee | string | Optional |  | 交割合约 taker 费率  
delivery_maker_fee | string | Optional |  | 交割合约 maker 费率  
debit_fee | integer | Optional |  | 费率抵扣类型 , 1 - GT抵扣 , 2 - 点卡抵扣 , 3 - VIP费率  
rpi_mm | integer | Optional |  | RPI MM等级  
  
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
  
  
####  详细描述

**currency** : 用于统计换算的目标货币类型，可接受BTC，CNY，USD，USDT四个值。USDT是默认值  

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求有效且成功返回 | TotalBalance  
  
### 返回格式

状态码 **200**

用户总资产信息

类型 | 约束  
---|---  
TotalBalance |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | object | Optional |  | 换算成目标币种的账户总额  
details | object | Optional |  | 各账户总额  
  
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
  
**total**

换算成目标币种的账户总额

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
amount | string | Optional |  | 账户总额数字  
currency | string | Optional | enum: ["BTC","CNY","USD","USDT"] | 币种  
unrealised_pnl | string | Optional |  | 未实现盈亏总和,这个字段只会在futures,options,delivery,total 账户中出现  
borrowed | string | Optional |  | 杠杆借贷总和,这个字段只会在margin,cross_margin账户中出现  
  
**details**

各账户总额

  * cross_margin: 全仓杠杆账户
  * spot: 现货账户
  * finance: 金融账户
  * margin: 杠杆账户
  * quant: 量化账户
  * futures: 永续合约账户
  * delivery: 交割合约账户
  * warrant: warrant 账户
  * cbbc: 牛熊证账户
  * meme_box: alpha账户
  * options: 期权账户
  * payment: 支付账户

类型 | 约束  
---|---  
object |   
  
**details / additionalProperties**

换算成目标币种的账户总额

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
amount | string | Optional |  | 账户总额数字  
currency | string | Optional | enum: ["BTC","CNY","USD","USDT"] | 币种  
unrealised_pnl | string | Optional |  | 未实现盈亏总和,这个字段只会在futures,options,delivery,total 账户中出现  
borrowed | string | Optional |  | 杠杆借贷总和,这个字段只会在margin,cross_margin账户中出现  
  
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

类型 | 约束  
---|---  
array |   
  
**items**

小额兑换币种

类型 | 约束  
---|---  
SmallBalance |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种  
available_balance | string | Optional |  | 可转换金额  
estimated_as_btc | string | Optional |  | 预计用 BTC 计价金额  
convertible_to_gt | string | Optional |  | 预计可转换成多少 GT  
  
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
currency | body | array | 否 | 需要被兑换的币种  
is_all | body | boolean | 否 | 是否全部兑换  
  
####  请求体结构

小额兑换币种

请求体结构类型 | 约束  
---|---  
ConvertSmallBalance |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | array | Optional |  | 需要被兑换的币种  
is_all | boolean | Optional |  | 是否全部兑换  
  
**currency**

需要被兑换的币种

请求体结构类型 | 约束  
---|---  
array |   
  
**currency / items**

请求体结构类型 | 约束  
---|---  
string |   
  
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
    

##  查询小额资产兑换历史🔒 需要认证

GET`/wallet/small_balance_history`

GET `/wallet/small_balance_history`

_查询小额资产兑换历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 按兑换币种筛选。  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大100。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | [SmallBalanceHistory]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

小额兑换币种

类型 | 约束  
---|---  
SmallBalanceHistory |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 订单ID  
currency | string | Optional | readOnly: true | 兑换币种  
amount | string | Optional | readOnly: true | 兑换数量  
gt_amount | string | Optional | readOnly: true | 被兑换到的 GT 数量  
create_time | integer(int64) | Optional | readOnly: true | 兑换时间(秒)  
  
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

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
UidPushOrder |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 订单 ID  
push_uid | integer(int64) | Optional |  | 发起方用户ID  
receive_uid | integer(int64) | Optional |  | 接收方用户ID  
currency | string | Optional |  | 币种名称  
amount | string | Optional |  | 转账数量  
create_time | integer(int64) | Optional |  | 创建时间  
status | string | Optional |  | 提现状态:  
  
\- CREATING: 创建中  
\- PENDING: 等待接收 (请联系对方在 Gate 官网接受转帐)  
\- CANCELLING: 撤销中  
\- CANCELLED: 已撤销  
\- REFUSING: 拒绝中  
\- REFUSED: 已拒绝  
\- RECEIVING: 正在接收  
\- RECEIVED: 成功  
message | string | Optional |  | PENDING原因提示  
transaction_type | string | Optional |  | 订单类型  
  
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

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

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

##  DepositRecord

类型 | 约束  
---|---  
object | required: ["currency","amount","chain"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 交易记录 ID  
txid | string | Optional | readOnly: true | 区块转账哈希记录  
timestamp | string | Optional | readOnly: true | 操作时间  
amount | string | Required |  | 币的数量  
currency | string | Required |  | 币种名称  
address | string | Optional |  | 提现地址。提现操作必填  
memo | string | Optional |  | 转账memo等备注信息  
status | string | Optional | readOnly: true | 交易状态  
  
\- BLOCKED: 拒绝充值  
\- DEP_CREDITED: 充值到账，提现未解锁  
\- DONE: 已经给账户增加资金  
\- INVALID: 无效数据  
\- MANUAL: 转人工审核  
\- PEND: 处理中  
\- REVIEW: 充值审核中(合规审查)  
\- TRACK: 跟踪确认数，等待给用户添加资金(现货)  
refund_status | string | Optional | readOnly: true | 拦截充值的退款状态。仅当充值记录存在拦截充值退款记录且退款状态非空时返回该字段，无退款记录或退款状态为空时不返回  
  
\- REFUNDING: 退款中  
\- REFUNDED: 退款完成  
\- REFUND_FAILED: 退款失败  
\- REJECTED: 退款被拒绝  
chain | string | Required |  | 提现的链名称  
      
    
    {
      "id": "string",
      "txid": "string",
      "timestamp": "string",
      "amount": "string",
      "currency": "string",
      "address": "string",
      "memo": "string",
      "status": "string",
      "refund_status": "string",
      "chain": "string"
    }
    
    

##  TransferOrderStatus

TransferOrderStatus

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tx_id | string | Optional |  | 操作单号  
status | string | Optional |  | 划转状态，PENDING - 处理中，SUCCESS - 划转成功，FAIL - 划转失败，PARTIAL_SUCCESS - 部分成功（子子划转时会出现此状态）  
      
    
    {
      "tx_id": "string",
      "status": "string"
    }
    
    

##  TransactionID

TransactionID

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tx_id | integer(int64) | Optional |  | 操作单号  
      
    
    {
      "tx_id": 0
    }
    
    

##  CurrencyChain

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
chain | string | Optional |  | 链名称  
name_cn | string | Optional |  | 链的中文名称  
name_en | string | Optional |  | 链的英文名称  
contract_address | string | Optional |  | 币种智能合约地址，如果没有地址则为空字串  
is_disabled | integer(int32) | Optional |  | 是否禁用，0 表示未禁用  
is_deposit_disabled | integer(int32) | Optional |  | 充值是否禁用，0 表示未禁用  
is_withdraw_disabled | integer(int32) | Optional |  | 提现是否禁用，0 表示未禁用  
decimal | string | Optional |  | 提币精度  
is_tag | integer | Optional |  | 是否包含tag  
      
    
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
    
    

##  TotalBalance

用户总资产信息

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | object | Optional |  | 换算成目标币种的账户总额  
details | object | Optional |  | 各账户总额  
  
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
  
**total**

换算成目标币种的账户总额

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
amount | string | Optional |  | 账户总额数字  
currency | string | Optional | enum: ["BTC","CNY","USD","USDT"] | 币种  
unrealised_pnl | string | Optional |  | 未实现盈亏总和,这个字段只会在futures,options,delivery,total 账户中出现  
borrowed | string | Optional |  | 杠杆借贷总和,这个字段只会在margin,cross_margin账户中出现  
  
**details**

各账户总额

  * cross_margin: 全仓杠杆账户
  * spot: 现货账户
  * finance: 金融账户
  * margin: 杠杆账户
  * quant: 量化账户
  * futures: 永续合约账户
  * delivery: 交割合约账户
  * warrant: warrant 账户
  * cbbc: 牛熊证账户
  * meme_box: alpha账户
  * options: 期权账户
  * payment: 支付账户

类型 | 约束  
---|---  
object |   
  
**details / additionalProperties**

换算成目标币种的账户总额

类型 | 约束  
---|---  
object |   
      
    
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
    
    

##  DepositAddress

类型 | 约束  
---|---  
object | required: ["currency","address"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 币种信息  
address | string | Required |  | 充值地址  
min_deposit_amount | string | Optional |  | 最小充值额度  
multichain_addresses | array | Optional |  |   
  
**multichain_addresses**

类型 | 约束  
---|---  
array |   
  
**multichain_addresses / items**

MultiChainAddressItem

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
chain | string | Optional |  | 链的名称  
address | string | Optional |  | 充值地址  
payment_id | string | Optional |  | 部分币种充值时必须填写的备注，例如 Tag 或 Memo。  
payment_name | string | Optional |  | 备注类型, `Tag` 或 `Memo`  
obtain_failed | integer | Optional |  | 地址获取是否失败：0 获取成功；1 获取失败，可能需要重新获取。  
min_confirms | integer | Optional |  | 最小确认数  
      
    
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
    
    

##  SubAccountFuturesBalance

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
uid | string | Optional |  | 用户 ID  
available | object | Optional |  | 各结算账户信息  
  
**available**

各结算账户信息

类型 | 约束  
---|---  
object |   
  
**available / additionalProperties**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | string | Optional |  | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional |  | 未实现盈亏  
position_margin | string | Optional |  | 已废弃  
order_margin | string | Optional |  | 所有未完成订单的起始保证金  
available | string | Optional |  | 指的是逐仓可用的转出或交易的额度，统一账户下包含授信额度的逐仓可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
point | string | Optional |  | 点卡数额  
currency | string | Optional |  | 结算币种  
in_dual_mode | boolean | Optional |  | 是否为双向持仓模式  
enable_credit | boolean | Optional |  | 是否开启统一账户模式  
position_initial_margin | string | Optional |  | 头寸占用的起始保证金，适用于统一账户模式  
maintenance_margin | string | Optional |  | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
bonus | string | Optional |  | 体验金  
enable_evolved_classic | boolean | Optional |  | 已废弃  
cross_order_margin | string | Optional |  | 全仓挂单保证金，适用于新经典账户保证金模式  
cross_initial_margin | string | Optional |  | 全仓初始保证金，适用于新经典账户保证金模式  
cross_maintenance_margin | string | Optional |  | 全仓维持保证金，适用于新经典账户保证金模式  
cross_unrealised_pnl | string | Optional |  | 全仓未实现盈亏，适用于新经典账户保证金模式  
cross_available | string | Optional |  | 全仓可用额度，适用于新经典账户保证金模式  
cross_margin_balance | string | Optional |  | 全仓保证金余额，适用于新经典账户保证金模式  
cross_mmr | string | Optional |  | 全仓维持保证金率，适用于新经典账户保证金模式  
cross_imr | string | Optional |  | 全仓初始保证金率，适用于新经典账户保证金模式  
isolated_position_margin | string | Optional |  | 逐仓仓位保证金，适用于新经典账户保证金模式  
enable_new_dual_mode | boolean | Optional |  | 已废弃  
margin_mode | integer | Optional |  | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
enable_tiered_mm | boolean | Optional |  | 是否开启梯度式计算维持保证金  
enable_dual_plus | boolean | Optional |  | 是否支持分仓模式  
position_mode | string | Optional |  | 持仓模式 single-单向持仓 dual-双向持仓 dual_plus-分仓  
history | object | Optional |  | 累计统计数据  
  
**available / additionalProperties / history**

累计统计数据

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
dnw | string | Optional |  | 累计转入转出  
pnl | string | Optional |  | 累计交易盈亏  
fee | string | Optional |  | 累计手续费  
refr | string | Optional |  | 累计获取的推荐人返佣  
fund | string | Optional |  | 累计资金费用  
point_dnw | string | Optional |  | 累计点卡转入转出  
point_fee | string | Optional |  | 累计点卡抵扣手续费  
point_refr | string | Optional |  | 累计获取的点卡推荐人返佣  
bonus_dnw | string | Optional |  | 累计体验金转入转出  
bonus_offset | string | Optional |  | 累计体验金抵扣  
cross_settle | string | Optional |  | 代表统一账户模式下，合约账户盈利被结算到现货数值。负数代表从合约结算到现货的，正数代表从现货结算到合约的。此数值为累计值  
      
    
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
    
    

##  SubAccountTransfer

类型 | 约束  
---|---  
object | required: ["currency","sub_account","direction","amount"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
sub_account | string | Required |  | 子账号用户 ID  
sub_account_type | string | Optional | default: "spot" | 操作的子账号交易账户， spot - 现货账户， futures - 永续合约账户， delivery - 交割合约账户, options - 期权账户  
currency | string | Required |  | 转账货币名称  
amount | string | Required |  | 划转金额，最多支持8位小数，必须大于0  
direction | string | Required |  | 资金流向，to - 转入子账号, from - 转出子账号  
client_order_id | string | Optional |  | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
      
    
    {
      "sub_account": "string",
      "sub_account_type": "spot",
      "currency": "string",
      "amount": "string",
      "direction": "string",
      "client_order_id": "string"
    }
    
    

##  SubAccountMarginBalance

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
uid | string | Optional |  | 用户 ID  
available | array | Optional |  | 账户余额信息  
  
**available**

账户余额信息

类型 | 约束  
---|---  
array |   
  
**available / items**

某交易对的杠杆账户信息，`base` 对应交易货币的账户信息，`quote` 对应计价货币的账户信息

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency_pair | string | Optional |  | 交易对  
account_type | string | Optional |  | 账户类型。mmr-维持保证金率账户，inactive - 市场未激活  
leverage | string | Optional |  | 用户当前市场杠杆倍数  
locked | boolean | Optional |  | 账户是否被锁定  
risk | string | Optional |  | 已废弃  
mmr | string | Optional |  | 该逐仓杠杆账户当前维持保证金率  
base | object | Optional |  | 货币账户信息  
quote | object | Optional |  | 货币账户信息  
  
**available / items / base**

货币账户信息

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 货币名称  
available | string | Optional |  | 可用于杠杆交易的额度，available = 保证金 + borrowed  
locked | string | Optional |  | 冻结资金，如已经放在杠杆市场里挂单交易的数额  
borrowed | string | Optional |  | 借入资金  
interest | string | Optional |  | 未还利息  
      
    
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
    
    

##  WithdrawStatus

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种  
name | string | Optional |  | 币种名称  
name_cn | string | Optional |  | 币种中文名称  
deposit | string | Optional |  | 充值手续费  
withdraw_percent | string | Optional |  | 提现手续费率百分比  
withdraw_fix | string | Optional |  | 固定提现手续费用  
withdraw_day_limit | string | Optional |  | 日提现额度  
withdraw_amount_mini | string | Optional |  | 最少提现额度  
withdraw_day_limit_remain | string | Optional |  | 剩余日提现额度  
withdraw_eachtime_limit | string | Optional |  | 单次最多提现额度  
withdraw_fix_on_chains | object | Optional |  | 多链的固定提现手续费用  
withdraw_percent_on_chains | object | Optional |  | 多链的百分比提现手续费用  
  
**withdraw_fix_on_chains**

多链的固定提现手续费用

类型 | 约束  
---|---  
object |   
  
**withdraw_fix_on_chains / additionalProperties**

类型 | 约束  
---|---  
string |   
  
**withdraw_percent_on_chains**

多链的百分比提现手续费用

类型 | 约束  
---|---  
object |   
  
**withdraw_percent_on_chains / additionalProperties**

类型 | 约束  
---|---  
string |   
      
    
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
    
    

##  SmallBalance

小额兑换币种

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种  
available_balance | string | Optional |  | 可转换金额  
estimated_as_btc | string | Optional |  | 预计用 BTC 计价金额  
convertible_to_gt | string | Optional |  | 预计可转换成多少 GT  
      
    
    {
      "currency": "string",
      "available_balance": "string",
      "estimated_as_btc": "string",
      "convertible_to_gt": "string"
    }
    
    

##  SubAccountToSubAccount

类型 | 约束  
---|---  
object | required: ["currency","sub_account_from","sub_account_from_type","sub_account_to","sub_account_to_type","amount"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 转账货币名称  
sub_account_type | string | Optional |  | 转出的子账号交易账户 (已弃用, 改用 `sub_account_from_type` 和 `sub_account_to_type`)  
sub_account_from | string | Required |  | 转出子账号用户 ID  
sub_account_from_type | string | Required |  | 转出的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
sub_account_to | string | Required |  | 转入子账号用户 ID  
sub_account_to_type | string | Required |  | 转入的子账号交易账户, spot - 现货账户, futures - 永续合约账户, delivery - 交割合约账户  
amount | string | Required |  | 划转金额，最多支持8位小数，必须大于0  
      
    
    {
      "currency": "string",
      "sub_account_type": "string",
      "sub_account_from": "string",
      "sub_account_from_type": "string",
      "sub_account_to": "string",
      "sub_account_to_type": "string",
      "amount": "string"
    }
    
    

##  AccountTransferDetail

交易账户划转订单详情

类型 | 约束  
---|---  
object | required: ["tx_id","status","currency","amount","from_account","to_account","settle","currency_pair"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tx_id | string | Required | readOnly: true | 划转操作单号  
status | string | Required | enum: ["pending","success","fail"]  
readOnly: true | 划转状态：  
  
\- `pending`：处理中  
\- `success`：划转成功  
\- `fail`：划转失败  
currency | string | Required | readOnly: true | 划转币种  
amount | string | Required | readOnly: true | 划转数量  
from_account | string | Required | enum: ["spot","margin","futures","delivery","options","unknown"]  
readOnly: true | 转出账户类型：  
  
\- `spot`：现货账户  
\- `margin`：杠杆账户  
\- `futures`：永续合约账户  
\- `delivery`：交割合约账户  
\- `options`：期权账户  
\- `unknown`：无法识别的账户类型  
to_account | string | Required | enum: ["spot","margin","futures","delivery","options","unknown"]  
readOnly: true | 转入账户类型：  
  
\- `spot`：现货账户  
\- `margin`：杠杆账户  
\- `futures`：永续合约账户  
\- `delivery`：交割合约账户  
\- `options`：期权账户  
\- `unknown`：无法识别的账户类型  
settle | string|null | Required | nullable: true  
readOnly: true | futures、delivery、options 划转时返回结算币种，否则返回 null  
currency_pair | string|null | Required | nullable: true  
readOnly: true | margin 划转时返回交易对，否则返回 null  
      
    
    {
      "tx_id": "string",
      "status": "pending",
      "currency": "string",
      "amount": "string",
      "from_account": "spot",
      "to_account": "spot",
      "settle": "string",
      "currency_pair": "string"
    }
    
    

##  SubAccountTransferRecordItem

类型 | 约束  
---|---  
object | required: ["currency","sub_account","direction","amount"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
timest | string | Optional | readOnly: true | 转账时间戳  
uid | string | Optional | readOnly: true | 主账号用户 ID  
sub_account | string | Required |  | 子账号用户 ID  
sub_account_type | string | Optional | default: "spot" | 操作的子账号交易账户， spot - 现货账户， futures - 永续合约账户， delivery - 交割合约账户, options - 期权账户  
currency | string | Required |  | 转账货币名称  
amount | string | Required |  | 划转金额  
direction | string | Required |  | 资金流向，to - 转入子账号, from - 转出子账号  
source | string | Optional | readOnly: true | 转账操作来源  
client_order_id | string | Optional |  | 客户自定义ID，防止重复划转，字母（区分大小写）、数字、连字符'-'和下划线'_'的组合，可以是纯字母、纯数字且长度要在1-64位之间  
status | string | Optional |  | 子账户划转记录状态，目前只有success  
      
    
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
    
    

##  TradeFee

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | 用户 ID  
taker_fee | string | Optional |  | 现货 taker 费率  
maker_fee | string | Optional |  | 现货 maker 费率  
rpi_maker_fee | string | Optional |  | 现货 RPI MM maker 费率  
gt_discount | boolean | Optional |  | 是否开启 GT 抵扣折扣  
gt_taker_fee | string | Optional |  | GT 抵扣 taker 费率，未开启 GT 抵扣则为 0  
gt_maker_fee | string | Optional |  | GT 抵扣 maker 费率，未开启 GT 抵扣则为 0  
loan_fee | string | Optional |  | 杠杆理财的费率  
point_type | string | Optional |  | 点卡类型，0 - 初版点卡，1 - 202009 启用的新点卡  
futures_taker_fee | string | Optional |  | 合约 taker 费率  
futures_maker_fee | string | Optional |  | 合约 maker 费率  
futures_rpi_maker_fee | string | Optional |  | 合约 RPI MM maker 费率  
delivery_taker_fee | string | Optional |  | 交割合约 taker 费率  
delivery_maker_fee | string | Optional |  | 交割合约 maker 费率  
debit_fee | integer | Optional |  | 费率抵扣类型 , 1 - GT抵扣 , 2 - 点卡抵扣 , 3 - VIP费率  
rpi_mm | integer | Optional |  | RPI MM等级  
      
    
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
    
    

##  SavedAddress

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Optional |  | 币种  
chain | string | Optional |  | 链名称  
address | string | Optional |  | 地址  
name | string | Optional |  | 名称  
tag | string | Optional |  | 标签  
verified | string | Optional |  | 是否通过验证 0-未验证, 1-已验正  
      
    
    {
      "currency": "string",
      "chain": "string",
      "address": "string",
      "name": "string",
      "tag": "string",
      "verified": "string"
    }
    
    

##  SmallBalanceHistory

小额兑换币种

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 订单ID  
currency | string | Optional | readOnly: true | 兑换币种  
amount | string | Optional | readOnly: true | 兑换数量  
gt_amount | string | Optional | readOnly: true | 被兑换到的 GT 数量  
create_time | integer(int64) | Optional | readOnly: true | 兑换时间(秒)  
      
    
    {
      "id": "string",
      "currency": "string",
      "amount": "string",
      "gt_amount": "string",
      "create_time": 0
    }
    
    

##  UidPushOrder

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 订单 ID  
push_uid | integer(int64) | Optional |  | 发起方用户ID  
receive_uid | integer(int64) | Optional |  | 接收方用户ID  
currency | string | Optional |  | 币种名称  
amount | string | Optional |  | 转账数量  
create_time | integer(int64) | Optional |  | 创建时间  
status | string | Optional |  | 提现状态:  
  
\- CREATING: 创建中  
\- PENDING: 等待接收 (请联系对方在 Gate 官网接受转帐)  
\- CANCELLING: 撤销中  
\- CANCELLED: 已撤销  
\- REFUSING: 拒绝中  
\- REFUSED: 已拒绝  
\- RECEIVING: 正在接收  
\- RECEIVED: 成功  
message | string | Optional |  | PENDING原因提示  
transaction_type | string | Optional |  | 订单类型  
      
    
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
    
    

##  ConvertSmallBalance

小额兑换币种

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | array | Optional |  | 需要被兑换的币种  
is_all | boolean | Optional |  | 是否全部兑换  
  
**currency**

需要被兑换的币种

类型 | 约束  
---|---  
array |   
  
**currency / items**

类型 | 约束  
---|---  
string |   
      
    
    {
      "currency": [
        "string"
      ],
      "is_all": true
    }
    
    

##  WithdrawalRecord

类型 | 约束  
---|---  
object | required: ["currency","amount","chain"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 交易记录 ID  
txid | string | Optional | readOnly: true | 区块转账哈希记录  
block_number | string | Optional | readOnly: true | 区块编号  
withdraw_order_id | string | Optional |  | 用户端订单编号,最长32个，输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
timestamp | string | Optional | readOnly: true | 操作时间  
amount | string | Required |  | 币的数量  
fee | string | Optional | readOnly: true | 手续费  
currency | string | Required |  | 币种名称  
address | string | Optional |  | 提现地址  
type | string | Optional |  | 业务类型  
fail_reason | string | Optional |  | 提现失败原因，当 status = CANCEL时有值，其余状态时为空  
timestamp2 | string | Optional |  | 提现终态时间，即： 提现取消时间或提现成功时间  
当 status = CANCEL 时，对应 取消时间  
当 status = DONE 时，为提现成功时间  
memo | string | Optional |  | 转账memo等备注信息  
status | string | Optional | readOnly: true | 交易状态  
  
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
chain | string | Required |  | 提现的链名称  
      
    
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
    
    

##  SubAccountCrossMarginBalance

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
uid | string | Optional |  | 用户 ID  
available | object | Optional |  |   
  
**available**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | 全仓帐户用户ID，如果 0 代表这个子帐号尚未开通全仓帐户  
locked | boolean | Optional |  | 账户是否被锁定  
balances | object | Optional |  |   
total | string | Optional |  | 折算成 USDT 的账户总资产，即所有币种(不包括点卡)的 `(available+freeze)*price*discount` 之和  
borrowed | string | Optional |  | 折算成 USDT 的账户总借入数量，即所有币种(不包括点卡)的 `borrowed*price*discount` 之和  
borrowed_net | string | Optional |  | 折算成 USDT 的账户总借入数量 * 放大系数  
net | string | Optional |  | 折算成 USDT 的净资产  
leverage | string | Optional |  | 杠杆倍数  
interest | string | Optional |  | 折算成 USDT 的账户未接利息的总和，即所有币种(不包括点卡)的 `interest*price*discount` 之和  
risk | string | Optional |  | 风险率，风险率小于 110% 会被爆仓，计算方式 `total / (borrowed+interest)`  
total_initial_margin | string | Optional |  | 总初始保证金  
total_margin_balance | string | Optional |  | 总保证金余额  
total_maintenance_margin | string | Optional |  | 总维持保证金  
total_initial_margin_rate | string | Optional |  | 总初始保证金率  
total_maintenance_margin_rate | string | Optional |  | 总维持保证金率  
total_available_margin | string | Optional |  | 可用的保证金额度  
  
**available / balances**

类型 | 约束  
---|---  
object |   
  
**available / balances / additionalProperties**

CrossMarginBalance

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
available | string | Optional |  | 可用额度  
freeze | string | Optional |  | 被锁定的额度  
borrowed | string | Optional |  | 借入额度  
interest | string | Optional |  | 未还利息  
      
    
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
    
    

##  SubAccountBalance

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
uid | string | Optional |  | 用户 ID  
available | object | Optional |  | 币种可用余额  
locking | object | Optional |  | 币种锁定金额  
  
**available**

币种可用余额

类型 | 约束  
---|---  
object |   
  
**available / additionalProperties**

类型 | 约束  
---|---  
string |   
  
**locking**

币种锁定金额

类型 | 约束  
---|---  
object |   
  
**locking / additionalProperties**

类型 | 约束  
---|---  
string |   
      
    
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
    
    

##  Transfer

转入转出账户列表:

  * `spot`: 现货账户
  * `margin`: 杠杆账户
  * `futures`: 永续合约账户
  * `delivery`: 交割合约账户
  * `options`: 期权账户

类型 | 约束  
---|---  
object | required: ["currency","from","to","amount"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
currency | string | Required |  | 转账货币名称。关联合约账户时，currency 可以设置的值为`POINT`(即点卡) 和支持的结算货币(如 `BTC`, `USDT`)  
from | string | Required | enum: ["spot","margin","futures","delivery","options"] | 转出账户  
to | string | Required | enum: ["spot","margin","futures","delivery","options"] | 转入账户  
amount | string | Required |  | 划转金额，最多支持8位小数，必须大于0  
currency_pair | string | Optional |  | 杠杆交易对。转入或转出杠杆账户时必填  
settle | string | Optional |  | 合约结算币种。 转入转出合约账户时必填  
      
    
    {
      "currency": "string",
      "from": "spot",
      "to": "spot",
      "amount": "string",
      "currency_pair": "string",
      "settle": "string"
    }