---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/withdrawal
api_type: Account
updated_at: 2026-05-27 20:18:13.971930
---

# Withdrawal

提现接口

##  提现🔒 需要认证

POST`/withdrawals`

POST `/withdrawals`

_提现_

如果对方的链上地址也是Gate的话, 则不收取手续费

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | LedgerRecord | 是 |   
» withdraw_order_id | body | string | 否 | 提现时用户自定义的单号。 默认为空。 非空时 会查询指定用户自定义单号记录  
» amount | body | string | 是 | 币的数量  
» currency | body | string | 是 | 币种名称  
» address | body | string | 否 | 提现地址。提现操作必填  
» memo | body | string | 否 | 转账memo等备注信息  
» withdraw_id | body | string | 否 | 提现记录id， 以w开头，如： w1879219868。 当withdraw_id 不为空时，则值查询这一条提现记录，不再按照时间进行查询  
» asset_class | body | string | 否 | 提现记录币种类型，默认为空。即支持用户按需查询主区和创新区的提现记录。  
取值范围：SPOT、PILOT  
  
SPOT ： 主区   
PILOT： 创新区  
» chain | body | string | 是 | 提现的链名称  
  
####  详细描述

**» asset_class** : 提现记录币种类型，默认为空。即支持用户按需查询主区和创新区的提现记录。  
取值范围：SPOT、PILOT  
  
SPOT ： 主区   
PILOT： 创新区

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 提现请求已受理，处理结果查看该提现记录状态 | LedgerRecord  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» id | string | 交易记录 ID  
» txid | string | 区块转账哈希记录  
» withdraw_order_id | string | 提现时用户自定义的单号。 默认为空。 非空时 会查询指定用户自定义单号记录  
» timestamp | string | 操作时间  
» amount | string | 币的数量  
» currency | string | 币种名称  
» address | string | 提现地址。提现操作必填  
» memo | string | 转账memo等备注信息  
» withdraw_id | string | 提现记录id， 以w开头，如： w1879219868。 当withdraw_id 不为空时，则值查询这一条提现记录，不再按照时间进行查询  
» asset_class | string | 提现记录币种类型，默认为空。即支持用户按需查询主区和创新区的提现记录。  
取值范围：SPOT、PILOT  
  
SPOT ： 主区   
PILOT： 创新区  
» status | string | 交易状态  
  
\- DONE: 完成  
\- CANCEL: 已取消  
\- REQUEST: 请求中  
\- MANUAL: 待人工审核  
\- BCODE: 充值码操作  
\- EXTPEND: 已经发送等待确认  
\- FAIL: 链上失败等待确认  
\- INVALID: 无效订单  
\- VERIFY: 验证中  
\- PROCES: 处理中  
\- PEND: 处理中  
\- DMOVE: 待人工审核  
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
    
    url = '/withdrawals'
    query_param = ''
    body='{"withdraw_order_id":"order_123456","currency":"USDT","address":"1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs","amount":"222.61","memo":"","chain":"TRX"}'
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
    url="/withdrawals"
    query_param=""
    body_param='{"withdraw_order_id":"order_123456","currency":"USDT","address":"1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs","amount":"222.61","memo":"","chain":"TRX"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "withdraw_order_id": "order_123456",
      "currency": "USDT",
      "address": "1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs",
      "amount": "222.61",
      "memo": "",
      "chain": "TRX"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": "210496",
      "timestamp": "1542000000",
      "withdraw_order_id": "order_123456",
      "currency": "USDT",
      "address": "1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs",
      "txid": "128988928203223323290",
      "amount": "222.61",
      "memo": "",
      "status": "DONE",
      "chain": "TRX"
    }
    

##  UID 转帐🔒 需要认证

POST`/withdrawals/push`

POST `/withdrawals/push`

_UID 转帐_

现货主账号之间转帐,转帐双方不可为子账号

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | UidPushWithdrawal | 是 |   
» receive_uid | body | integer(int64) | 是 | 接收方uid  
» currency | body | string | 是 | 币种名称  
» amount | body | string | 是 | 转账数量  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求已受理，处理结果查看该提现记录状态 | UidPushWithdrawalResp  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» id | string | 订单ID  
  
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
    
    url = '/withdrawals/push'
    query_param = ''
    body='{"receive_uid":12233,"currency":"USDT","amount":"1.1"}'
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
    url="/withdrawals/push"
    query_param=""
    body_param='{"receive_uid":12233,"currency":"USDT","amount":"1.1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "receive_uid": 12233,
      "currency": "USDT",
      "amount": "1.1"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": "111"
    }
    

##  取消指定 ID 的提现操作🔒 需要认证

DELETE`/withdrawals/{withdrawal_id}`

DELETE `/withdrawals/{withdrawal_id}`

_取消指定 ID 的提现操作_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
withdrawal_id | URL | string | 是 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | 取消请求已受理，处理结果查看该提现记录状态 | WithdrawalsDel  
  
### 返回格式

状态码 **202**

名称 | 类型 | 描述  
---|---|---  
» id | string | 交易记录 ID  
» txid | string | 区块转账哈希记录  
» timestamp | string | 操作时间  
» amount | string | 币的数量  
» currency | string | 币种名称  
» address | string | 提现地址。提现操作必填  
» memo | string | 转账memo等备注信息  
» block_number | string | 区块编号  
» status | string | 交易状态  
  
\- BCODE: 充值码操作  
\- CANCEL: 已取消  
\- CANCELPEND: 取消提现中  
\- DMOVE: 待人工审核  
\- DONE: 完成 (block_number > 0 时表示已完成上链)  
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
    
    url = '/withdrawals/210496'
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
    url="/withdrawals/210496"
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

> 202 返回
    
    
    {
      "id": "210496",
      "timestamp": "1542000000",
      "currency": "USDT",
      "address": "1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs",
      "txid": "128988928203223323290",
      "amount": "222.61",
      "memo": "",
      "block_number": "18217349",
      "status": "DONE",
      "chain": "TRX"
    }
    

#  模型

##  WithdrawalsDel

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
block_number | string | false | 只读 | 区块编号  
status | string | false | 只读 | 交易状态  
  
\- BCODE: 充值码操作  
\- CANCEL: 已取消  
\- CANCELPEND: 取消提现中  
\- DMOVE: 待人工审核  
\- DONE: 完成 (block_number > 0 时表示已完成上链)  
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
      "timestamp": "string",
      "amount": "string",
      "currency": "string",
      "address": "string",
      "memo": "string",
      "block_number": "string",
      "status": "string",
      "chain": "string"
    }
    
    

##  UidPushWithdrawal

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
receive_uid | integer(int64) | true | none | 接收方uid  
currency | string | true | none | 币种名称  
amount | string | true | none | 转账数量  
      
    
    {
      "receive_uid": 0,
      "currency": "string",
      "amount": "string"
    }
    
    

##  LedgerRecord

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | 只读 | 交易记录 ID  
txid | string | false | 只读 | 区块转账哈希记录  
withdraw_order_id | string | false | none | 提现时用户自定义的单号。 默认为空。 非空时 会查询指定用户自定义单号记录  
timestamp | string | false | 只读 | 操作时间  
amount | string | true | none | 币的数量  
currency | string | true | none | 币种名称  
address | string | false | none | 提现地址。提现操作必填  
memo | string | false | none | 转账memo等备注信息  
withdraw_id | string | false | none | 提现记录id， 以w开头，如： w1879219868。 当withdraw_id 不为空时，则值查询这一条提现记录，不再按照时间进行查询  
asset_class | string | false | none | 提现记录币种类型，默认为空。即支持用户按需查询主区和创新区的提现记录。  
取值范围：SPOT、PILOT  
  
SPOT ： 主区   
PILOT： 创新区  
status | string | false | 只读 | 交易状态  
  
\- DONE: 完成  
\- CANCEL: 已取消  
\- REQUEST: 请求中  
\- MANUAL: 待人工审核  
\- BCODE: 充值码操作  
\- EXTPEND: 已经发送等待确认  
\- FAIL: 链上失败等待确认  
\- INVALID: 无效订单  
\- VERIFY: 验证中  
\- PROCES: 处理中  
\- PEND: 处理中  
\- DMOVE: 待人工审核  
\- REVIEW: 审核中  
chain | string | true | none | 提现的链名称  
      
    
    {
      "id": "string",
      "txid": "string",
      "withdraw_order_id": "string",
      "timestamp": "string",
      "amount": "string",
      "currency": "string",
      "address": "string",
      "memo": "string",
      "withdraw_id": "string",
      "asset_class": "string",
      "status": "string",
      "chain": "string"
    }
    
    

##  UidPushWithdrawalResp

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | none | 订单ID  
      
    
    {
      "id": "string"
    }