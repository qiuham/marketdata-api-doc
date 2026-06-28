---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/p2p
api_type: REST
updated_at: 2026-05-27 20:17:40.245322
---

# P2p

P2P交易

##  获取账户信息🔒 需要认证

POST`/p2p/merchant/account/get_user_info`

POST `/p2p/merchant/account/get_user_info`

_获取账户信息_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMerchantUserInfoResponse  
  
### 返回格式

状态码 **200**

_P2pMerchantUserInfoResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» is_self | boolean | 是否本人  
»» user_timest | string | 用户注册时间，格式化字符串  
»» counterparties_num | integer | 交易对手数  
»» email_verified | string | 是否验证过邮箱，1：已验证，0：未验证  
»» verified | string | 是否完成 KYC，1：已完成，0：未完成  
»» has_phone | string | 是否绑定过手机，1：已绑定，0：未绑定  
»» user_name | string | 用户名  
»» user_note | string | 用户备注信息  
»» complete_transactions | string | 总完成订单数  
»» paid_transactions | string | 已完成买单订单数量  
»» accepted_transactions | string | 已完成卖单订单数量  
»» transactions_used_time | string | 确认收款平均用时  
»» cancelled_used_time_month | string | 近30天取消用时  
»» complete_transactions_month | string | 近30天完成订单数量  
»» complete_rate_month | number | 近30天完成率  
»» orders_buy_rate_month | number | 近30天买单占比  
»» is_black | integer | 是否已拉黑该用户，1：是，0：否  
»» is_follow | integer | 是否已关注该用户，1：是，0：否  
»» have_traded | integer | 是否与本人交易过，1：是，0：否  
»» biz_uid | string | 加密uid  
»» blue_vip | integer | 蓝V皇冠神盾  
»» work_status | integer | 商家工作状态  
»» registration_days | integer | 注册天数  
»» first_trade_days | integer | 首次交易到现在的天数  
»» need_replenish | integer | 是否需要补充保证金，1：需要，0：不需要  
»» merchant_info | object | 用户可挂单的市场  
»»» type | string |   
»»» market | string |   
»» online_status | integer | 商家在线状态，1：在线，0：离线  
»» work_hours | object|null | 商家在线状态详情  
»» transactions_month | number | 30天交易量  
»» transactions_all | number | 总交易量  
»» trade_versatile | boolean | 单一用户还是复合用户  
» version | string |   
  
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
    
    url = '/p2p/merchant/account/get_user_info'
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
    url="/p2p/merchant/account/get_user_info"
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
      "timestamp": 1767151138.989862,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "is_self": true,
        "user_timest": "2025/11/19",
        "counterparties_num": 12,
        "email_verified": "1",
        "verified": "1",
        "has_phone": "1",
        "user_name": "merchant_demo",
        "user_note": "Preferred counterparty",
        "complete_transactions": "128",
        "paid_transactions": "68",
        "accepted_transactions": "60",
        "transactions_used_time": "300",
        "cancelled_used_time_month": "2",
        "complete_transactions_month": "32",
        "complete_rate_month": 96,
        "orders_buy_rate_month": 53,
        "is_black": 0,
        "is_follow": 0,
        "have_traded": 1,
        "biz_uid": "biz_uid_demo_9f3a7c",
        "blue_vip": 0,
        "work_status": 1,
        "registration_days": 42,
        "first_trade_days": 30,
        "need_replenish": 0,
        "merchant_info": {
          "type": "0",
          "market": "USD"
        },
        "online_status": 1,
        "work_hours": null,
        "transactions_month": 6400.5,
        "transactions_all": 28600.75,
        "trade_versatile": false
      },
      "version": "1.0.0"
    }
    

##  获取对手方信息🔒 需要认证

POST`/p2p/merchant/account/get_counterparty_user_info`

POST `/p2p/merchant/account/get_counterparty_user_info`

_获取对手方信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | GetCounterpartyUserInfoRequest | 是 |   
» biz_uid | body | string | 是 | 对手方加密 UID，可从订单列表 its_uid 或订单详情 its_uid 获取  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pCounterpartyUserInfoResponse  
  
### 返回格式

状态码 **200**

_P2pCounterpartyUserInfoResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» user_timest | string | 用户注册时间，格式化字符串  
»» email_verified | string | 是否验证过邮箱，1：已验证，0：未验证  
»» verified | string | 是否完成 KYC，1：已完成，0：未完成  
»» has_phone | string | 是否绑定过手机，1：已绑定，0：未绑定  
»» user_name | string | 用户名  
»» user_note | string | 用户备注信息  
»» complete_transactions | string | 总完成订单数  
»» paid_transactions | string | 已完成买单订单数量  
»» accepted_transactions | string | 已完成卖单订单数量  
»» transactions_used_time | string | 确认收款平均用时  
»» cancelled_used_time_month | string | 近30天取消用时  
»» complete_transactions_month | string | 近30天完成订单数量  
»» complete_rate_month | number | 近30天完成率  
»» is_follow | integer | 是否已关注该用户，1：是，0：否  
»» have_traded | integer | 是否与本人交易过，1：是，0：否  
»» biz_uid | string | 加密uid  
»» registration_days | integer | 注册天数  
»» first_trade_days | integer | 首次交易到现在的天数  
»» trade_versatile | boolean | 单一用户还是复合用户  
» version | string |   
  
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
    
    url = '/p2p/merchant/account/get_counterparty_user_info'
    query_param = ''
    body='{"biz_uid":"biz_uid_demo_9f3a7c"}'
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
    url="/p2p/merchant/account/get_counterparty_user_info"
    query_param=""
    body_param='{"biz_uid":"biz_uid_demo_9f3a7c"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "biz_uid": "biz_uid_demo_9f3a7c"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767152416.755602,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "user_timest": "2025/11/19",
        "email_verified": "1",
        "verified": "1",
        "has_phone": "1",
        "user_name": "counterparty_demo",
        "user_note": "",
        "complete_transactions": "86",
        "paid_transactions": "44",
        "accepted_transactions": "42",
        "transactions_used_time": "420",
        "cancelled_used_time_month": "1",
        "complete_transactions_month": "18",
        "complete_rate_month": 95,
        "is_follow": 0,
        "have_traded": 0,
        "biz_uid": "biz_uid_demo_b84d21",
        "registration_days": 180,
        "first_trade_days": 90,
        "trade_versatile": false
      },
      "version": "1.0.0"
    }
    

##  获取支付方式列表🔒 需要认证

POST`/p2p/merchant/account/get_myself_payment`

POST `/p2p/merchant/account/get_myself_payment`

_获取支付方式列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | GetMyselfPaymentRequest | 否 |   
» fiat | body | string | 否 | 法币币种。不传时返回全部可用支付方式  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pPaymentMethodsResponse  
  
### 返回格式

状态码 **200**

_P2pPaymentMethodsResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | array |   
»» P2pPaymentMethodGroup | object |   
»»» pay_type | string | 支付方式类型  
»»» pay_name | string | 支付方式名称  
»»» ids | array | 用户当前绑定的支付方式，主键id  
»»» list | array |   
»»»» P2pPaymentMethodAccount | object |   
»»»»» uid | integer | 用户uid  
»»»»» bankid | string | 用户当前绑定的支付方式，主键id  
»»»»» nickname | integer | 持卡人uid  
»»»»» bankname | string | 银行名称  
»»»»» bankbranch | string | 银行支行名  
»»»»» bankcity | string | 银行所在城市  
»»»»» bankprov | string | 银行所在省  
»»»»» bankaddr | string | 银行卡号或脱敏银行卡号  
»»»»» bankdesc | string | 银行备注  
»»»»» hold_uid | integer | 持卡人uid  
»»»»» hold_username | string | 持卡人名称  
»»»»» real_name | string | 用户实名展示名  
»»»»» id | string | 用户当前绑定的支付方式，主键id  
»»»»» account_des | string | 支付方式描述  
»»»»» pay_type | string | 支付方式类型  
»»»»» file | string | 支付方式文件链接  
»»»»» file_key | string | 支付方式文件key  
»»»»» account | string | 支付账号或脱敏支付账号  
»»»»» memo | string | 支付方式备注  
»»»»» code | string | 支付方式code  
»»»»» memo_ext | string | 支付方式额外备注  
»»»»» trade_tips | string | 支付方式交易信息  
»»»» version | string |   
  
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
    
    url = '/p2p/merchant/account/get_myself_payment'
    query_param = ''
    body='{"fiat":"USD"}'
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
    url="/p2p/merchant/account/get_myself_payment"
    query_param=""
    body_param='{"fiat":"USD"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "fiat": "USD"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767152532.08744,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": [
        {
          "pay_type": "bank",
          "pay_name": "Bank Transfer",
          "ids": [
            10001
          ],
          "list": [
            {
              "uid": 1000001,
              "bankid": "10001",
              "nickname": 1000001,
              "bankname": "Demo Bank",
              "bankbranch": "Main Branch",
              "bankcity": "New York",
              "bankprov": "NY",
              "bankaddr": "****1234",
              "bankdesc": "Corporate settlement account",
              "hold_uid": 1000001,
              "hold_username": "merchant_demo",
              "real_name": "Merchant Demo"
            }
          ]
        },
        {
          "pay_type": "swift",
          "pay_name": "SWIFT International Remittance",
          "ids": [
            10002
          ],
          "list": [
            {
              "id": "10002",
              "account_des": "Business USD account",
              "pay_type": "swift",
              "file": "",
              "file_key": "",
              "account": "****5678",
              "memo": "Use order txid as reference",
              "code": "",
              "memo_ext": "",
              "trade_tips": "Please pay from an account under your real name",
              "real_name": "Merchant Demo"
            }
          ]
        }
      ],
      "version": "1.0.0"
    }
    

##  获取进行中订单🔒 需要认证

POST`/p2p/merchant/transaction/get_pending_transaction_list`

POST `/p2p/merchant/transaction/get_pending_transaction_list`

_获取进行中订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | GetPendingTransactionListRequest | 是 |   
» crypto_currency | body | string | 是 | 加密币币种  
» fiat_currency | body | string | 是 | 法币币种  
» order_tab | body | string | 否 | 订单标签页，pending：处理中订单（OPEN、PAID、LOCKED、TEMP），dispute：申诉中订单；默认 pending  
» select_type | body | string | 否 | 订单方向筛选，buy：买单，sell：卖单，空字符串或不传：全部  
» status | body | string | 否 | 订单状态筛选。open：未付款（OPEN）；paid：已付款（PAID）；locked：已锁定（LOCKED）；  
dispute：申诉中；空字符串或不传时按 order_tab 的默认状态范围查询。  
» txid | body | integer | 否 | 订单号  
» start_time | body | integer | 否 | 开始时间时间戳，默认89天前0点  
» end_time | body | integer | 否 | 结束时间时间戳，默认今天23:59:59  
  
####  详细描述

**» status** : 订单状态筛选。open：未付款（OPEN）；paid：已付款（PAID）；locked：已锁定（LOCKED）；  
dispute：申诉中；空字符串或不传时按 order_tab 的默认状态范围查询。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» order_tab | pending  
» order_tab | dispute  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionListResponse  
  
### 返回格式

状态码 **200**

_P2pTransactionListResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» list | array |   
»»» P2pTransactionListItem | object |   
»»»» type_buy | integer | 当前用户视角的订单方向，1：买单，0：卖单  
»»»» timest | string | 订单创建时间  
»»»» timest_expire | string | 订单过期时间  
»»»» timestamp | integer | 订单创建时间戳  
»»»» rate | string | 订单价格，按法币计价  
»»»» amount | string | 订单加密币数量  
»»»» total | string | 订单法币总金额  
»»»» txid | integer | 订单号  
»»»» status | string | 订单展示状态，unpay：待付款，paid：买家已付款，unconfirmed：待卖家确认收款，locked：已锁定，finished：已完成，cancel：已取消，expired：已过期，bclosed：仲裁成交，sclosed：仲裁取消  
»»»» its_realname | string | 交易对手真实姓名或实名展示名  
»»»» its_uid | string | 交易对手加密 UID  
»»»» its_nick | string | 交易对手昵称  
»»»» seller_realname | string | 卖家真实姓名或实名展示名  
»»»» buyer_realname | string | 买家真实姓名或实名展示名  
»»»» cancelable | integer | 是否可取消订单，1：可取消，0：不可取消  
»»»» currency_type | string | 加密币币种  
»»»» want_type | string | 法币币种  
»»»» hide_payment | integer | 是否隐藏支付方式，1：隐藏，0：不隐藏  
»»»» sel_paytype | string | 当前订单选择的支付方式类型，例如 bank、alipay、wechat、paypal、swift、wu  
»»»» pay_others | array | 其他支付方式信息，历史订单可能返回  
»»»»» pay_type | string | 支付方式类型  
»»»»» pay_name | string | 支付方式名称  
»»»» cd_time | integer | 当前订单倒计时秒数  
»»»» order_type | integer | 订单类型，1：普通订单，2：三方合作订单，3：闪兑订单，4：Web3 订单  
»»»» order_tag | array | 订单标签  
»»»» convert_info | object | 闪兑订单信息  
»»»»» convert_type | string | 闪兑目标币种  
»»»»» convert_status | string | 闪兑订单状态  
»»»»» pre_rate | string | 下单时预期价格  
»»»»» rate | string | 成交时价格  
»»»»» pre_fiat_rate | string | 下单时法币预期价格  
»»»»» fiat_rate | string | 成交时法币价格  
»»»»» amount | string | 数量  
»»»»» convert_amount | string | 兑换数量  
»»»»» slippage | string | 滑点计算，滑点 =（下单预期价格-自动兑换时实时价格）/ 下单预期价格  
»»»»» status | string | 闪兑订单展示状态  
»»»» trans_time | array | 倒计时时间  
»»»»» P2pTransactionTimeMarker | object |   
»»»»»» od_time | integer |   
»»»»» count | integer | 订单数  
»»»»» exported_num | integer | 导出次数  
»»»» version | string |   
  
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
    
    url = '/p2p/merchant/transaction/get_pending_transaction_list'
    query_param = ''
    body='{"crypto_currency":"USDT","fiat_currency":"USD","order_tab":"pending","select_type":"sell","status":"open","txid":40000001,"start_time":1764547200,"end_time":1767139199}'
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
    url="/p2p/merchant/transaction/get_pending_transaction_list"
    query_param=""
    body_param='{"crypto_currency":"USDT","fiat_currency":"USD","order_tab":"pending","select_type":"sell","status":"open","txid":40000001,"start_time":1764547200,"end_time":1767139199}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "order_tab": "pending",
      "select_type": "sell",
      "status": "open",
      "txid": 40000001,
      "start_time": 1764547200,
      "end_time": 1767139199
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767153378.888855,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "list": [
          {
            "type_buy": 1,
            "timest": "2025-12-15 08:27:09",
            "timest_expire": "2025-12-15 10:27:09",
            "timestamp": 1765787229,
            "rate": "1.100",
            "amount": "8.00",
            "total": "8.800",
            "txid": 40000001,
            "status": "paid",
            "its_realname": "Counterparty Demo",
            "its_uid": "biz_uid_demo_b84d21",
            "its_nick": "counterparty_demo",
            "seller_realname": "Merchant Demo",
            "buyer_realname": "Counterparty Demo",
            "cancelable": 1,
            "currency_type": "USDT",
            "want_type": "USD",
            "hide_payment": 0,
            "sel_paytype": "bank",
            "cd_time": 600,
            "order_type": 1,
            "order_tag": [
              "fast"
            ],
            "convert_info": {}
          }
        ],
        "trans_time": [
          {
            "od_time": 600
          }
        ],
        "count": 1,
        "exported_num": 0
      },
      "version": "1.0.0"
    }
    

##  获取所有/历史订单🔒 需要认证

POST`/p2p/merchant/transaction/get_completed_transaction_list`

POST `/p2p/merchant/transaction/get_completed_transaction_list`

_获取所有/历史订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | GetCompletedTransactionListRequest | 是 |   
» crypto_currency | body | string | 是 | 加密币币种  
» fiat_currency | body | string | 是 | 法币币种  
» select_type | body | string | 否 | 订单方向筛选，buy：买单，sell：卖单，空字符串或不传：全部  
» status | body | string | 否 | 订单状态筛选。closed：已成交（ACCEPT、BCLOSED）；cancel：已取消（CANCEL、BECANCEL、SCLOSED、SCANCEL）；  
locked：已锁定（LOCKED）；open：未付款（OPEN）；paid：已付款（PAID）；  
completed：已完成或已取消（CANCEL、BECANCEL、SCLOSED、SCANCEL、ACCEPT、BCLOSED）；  
空字符串或不传时按接口默认范围查询。  
» txid | body | integer | 否 | 订单号  
» start_time | body | integer | 否 | 开始时间时间戳，默认89天前0点  
» end_time | body | integer | 否 | 结束时间时间戳，默认今天23:59:59  
» query_dispute | body | integer | 否 | 是否在返回结果中标记申诉状态，1：标记，0：不标记  
» page | body | integer | 否 | 页码，从 1 开始；小于 1 时按 1 处理  
» per_page | body | integer | 否 | 每页订单数，默认 10，最大 200  
  
####  详细描述

**» status** : 订单状态筛选。closed：已成交（ACCEPT、BCLOSED）；cancel：已取消（CANCEL、BECANCEL、SCLOSED、SCANCEL）；  
locked：已锁定（LOCKED）；open：未付款（OPEN）；paid：已付款（PAID）；  
completed：已完成或已取消（CANCEL、BECANCEL、SCLOSED、SCANCEL、ACCEPT、BCLOSED）；  
空字符串或不传时按接口默认范围查询。

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionListResponse  
  
### 返回格式

状态码 **200**

_P2pTransactionListResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» list | array |   
»»» P2pTransactionListItem | object |   
»»»» type_buy | integer | 当前用户视角的订单方向，1：买单，0：卖单  
»»»» timest | string | 订单创建时间  
»»»» timest_expire | string | 订单过期时间  
»»»» timestamp | integer | 订单创建时间戳  
»»»» rate | string | 订单价格，按法币计价  
»»»» amount | string | 订单加密币数量  
»»»» total | string | 订单法币总金额  
»»»» txid | integer | 订单号  
»»»» status | string | 订单展示状态，unpay：待付款，paid：买家已付款，unconfirmed：待卖家确认收款，locked：已锁定，finished：已完成，cancel：已取消，expired：已过期，bclosed：仲裁成交，sclosed：仲裁取消  
»»»» its_realname | string | 交易对手真实姓名或实名展示名  
»»»» its_uid | string | 交易对手加密 UID  
»»»» its_nick | string | 交易对手昵称  
»»»» seller_realname | string | 卖家真实姓名或实名展示名  
»»»» buyer_realname | string | 买家真实姓名或实名展示名  
»»»» cancelable | integer | 是否可取消订单，1：可取消，0：不可取消  
»»»» currency_type | string | 加密币币种  
»»»» want_type | string | 法币币种  
»»»» hide_payment | integer | 是否隐藏支付方式，1：隐藏，0：不隐藏  
»»»» sel_paytype | string | 当前订单选择的支付方式类型，例如 bank、alipay、wechat、paypal、swift、wu  
»»»» pay_others | array | 其他支付方式信息，历史订单可能返回  
»»»»» pay_type | string | 支付方式类型  
»»»»» pay_name | string | 支付方式名称  
»»»» cd_time | integer | 当前订单倒计时秒数  
»»»» order_type | integer | 订单类型，1：普通订单，2：三方合作订单，3：闪兑订单，4：Web3 订单  
»»»» order_tag | array | 订单标签  
»»»» convert_info | object | 闪兑订单信息  
»»»»» convert_type | string | 闪兑目标币种  
»»»»» convert_status | string | 闪兑订单状态  
»»»»» pre_rate | string | 下单时预期价格  
»»»»» rate | string | 成交时价格  
»»»»» pre_fiat_rate | string | 下单时法币预期价格  
»»»»» fiat_rate | string | 成交时法币价格  
»»»»» amount | string | 数量  
»»»»» convert_amount | string | 兑换数量  
»»»»» slippage | string | 滑点计算，滑点 =（下单预期价格-自动兑换时实时价格）/ 下单预期价格  
»»»»» status | string | 闪兑订单展示状态  
»»»» trans_time | array | 倒计时时间  
»»»»» P2pTransactionTimeMarker | object |   
»»»»»» od_time | integer |   
»»»»» count | integer | 订单数  
»»»»» exported_num | integer | 导出次数  
»»»» version | string |   
  
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
    
    url = '/p2p/merchant/transaction/get_completed_transaction_list'
    query_param = ''
    body='{"crypto_currency":"USDT","fiat_currency":"USD","select_type":"buy","status":"closed","txid":40000001,"start_time":1764547200,"end_time":1767139199,"query_dispute":0,"page":1,"per_page":20}'
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
    url="/p2p/merchant/transaction/get_completed_transaction_list"
    query_param=""
    body_param='{"crypto_currency":"USDT","fiat_currency":"USD","select_type":"buy","status":"closed","txid":40000001,"start_time":1764547200,"end_time":1767139199,"query_dispute":0,"page":1,"per_page":20}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "select_type": "buy",
      "status": "closed",
      "txid": 40000001,
      "start_time": 1764547200,
      "end_time": 1767139199,
      "query_dispute": 0,
      "page": 1,
      "per_page": 20
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767153378.888855,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "list": [
          {
            "type_buy": 1,
            "timest": "2025-12-15 08:27:09",
            "timest_expire": "2025-12-15 10:27:09",
            "timestamp": 1765787229,
            "rate": "1.100",
            "amount": "8.00",
            "total": "8.800",
            "txid": 40000001,
            "status": "finished",
            "its_realname": "Counterparty Demo",
            "its_uid": "biz_uid_demo_b84d21",
            "its_nick": "counterparty_demo",
            "seller_realname": "Merchant Demo",
            "buyer_realname": "Counterparty Demo",
            "cancelable": 0,
            "currency_type": "USDT",
            "want_type": "USD",
            "hide_payment": 0,
            "sel_paytype": "bank",
            "pay_others": [
              {
                "pay_type": "swift",
                "pay_name": "SWIFT International Remittance"
              }
            ],
            "cd_time": 0,
            "order_type": 1,
            "order_tag": [],
            "convert_info": {}
          }
        ],
        "trans_time": [
          {
            "od_time": 0
          }
        ],
        "count": 1,
        "exported_num": 0
      },
      "version": "1.0.0"
    }
    

##  查询订单详情🔒 需要认证

POST`/p2p/merchant/transaction/get_transaction_details`

POST `/p2p/merchant/transaction/get_transaction_details`

_查询订单详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | GetTransactionDetailsRequest | 是 |   
» txid | body | integer | 是 | 订单号  
» channel | body | string | 否 | 渠道标识，普通 P2P 订单不传或传空字符串；Web3 订单传 web3  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionDetailResponse  
  
### 返回格式

状态码 **200**

_P2pTransactionDetailResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» is_sell | integer | 当前用户是否为卖家，1：是，0：否  
»» txid | integer | 订单号  
»» orderid | integer | 挂单号  
»» timest | integer | 订单创建时间戳  
»» last_pay_time | integer | 终止付款时间  
»» remain_pay_time | integer | 剩余付款时间，单位秒；小于等于 0 表示已超时  
»» currency_type | string | 加密币币种  
»» want_type | string | 法币币种  
»» symbol | string | 法币符号  
»» rate | string | 订单价格，按 want_type 计价  
»» amount | string | 订单加密币数量  
»» total | string | 订单法币总金额  
»» status | string | 订单展示状态，unpay：待付款，hide_payment：待付款但支付信息隐藏，paid：买家已付款，unconfirmed：待卖家确认收款，locked：已锁定，finished：已完成，cancel：已取消，expired：已过期，bclosed：仲裁成交，sclosed：仲裁取消  
»» reason_id | string | 取消原因 ID，空字符串表示无取消原因；常见值：1 不想再买币，2 无法联系卖家，3 不会支付，4 卖家未提供真实账号，6 实际单价或金额不一致，9 其他，10 卖家无法放行且已退款，11 不满足广告交易条款，12 卖家收款账户被风控  
»» reason_desc | string | 取消原因说明  
»» cancel_time | string | 取消时间  
»» in_appeal | integer | 是否申诉中，1：是，0：否  
»» dispute_time | integer | 允许发起申诉的时间戳  
»» cancelable | integer | 是否允许取消订单，1：允许，0：不允许  
»» hide_payment | integer | 是否隐藏支付方式，1：隐藏，0：不隐藏  
»» trade_tips | string | 交易条款  
»» show_bank | string | 是否展示银行转账信息，1：展示，0：不展示  
»» bankname | string | 银行名称  
»» bankbranch | string | 银行支行名称  
»» bankid | string | 银行账号或脱敏银行账号  
»» bank_holder_realname | string | 银行持卡人姓名  
»» show_ali | string | 是否展示支付宝信息，1：展示，0：不展示  
»» aliname | string | 支付宝账户名  
»» is_alicode | integer | 是否存在支付宝收款码，1：存在，0：不存在  
»» show_wechat | string | 是否展示微信信息，1：展示，0：不展示  
»» wename | string | 微信账户名  
»» show_others | string | 是否展示其他支付方式，1：展示，0：不展示  
»» pay_others | array | 其他支付方式  
»»» id | string | 支付方式记录 ID  
»»» account_des | string | 支付方式描述  
»»» pay_type | string | 支付方式类型  
»»» account | string | 支付账号或脱敏账号  
»»» memo | string | 支付备注  
»»» trade_tips | string | 支付提示  
»»» pay_name | string | 支付方式展示名称  
»» sel_paytype | string | 当前订单选择的支付方式类型，例如 bank、alipay、wechat、paypal、swift、wu  
»» its_uid | string | 对手方加密 UID  
»» its_nickname | string | 对方昵称  
»» its_realname | string | 对方真实姓名或实名展示名  
»» have_traded | integer | 是否与对方交易过，1：是，0：否  
»» appeal_allow_cancel | integer | 是否允许撤销申诉，1：允许，0：不允许  
»» appeal_verdict_has_open | string | 申诉结果或申诉中提示文案  
»» im_unread | integer | 聊天未读消息数  
»» payment_voucher_url | array | 支付凭证  
»» timest_paid | integer | 买家确认付款时间戳  
»» own_realname | string | 当前用户真实姓名或实名展示名  
»» order_type | integer | 订单类型，1：普通订单，2：三方合作订单，3：闪兑订单，4：Web3 订单  
»» is_show_receive | integer | 申诉中是否展示确认收款入口，1：展示，0：不展示  
»» show_seller_contact_info | boolean | 是否展示卖家联系方式  
»» supported_pay_types | array | 当前订单支持的支付方式类型，例如 bank、alipay、wechat、paypal、swift、wu  
» version | string |   
  
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
    
    url = '/p2p/merchant/transaction/get_transaction_details'
    query_param = ''
    body='{"txid":40000001,"channel":""}'
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
    url="/p2p/merchant/transaction/get_transaction_details"
    query_param=""
    body_param='{"txid":40000001,"channel":""}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "txid": 40000001,
      "channel": ""
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767859489.457123,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "is_sell": 1,
        "txid": 40000001,
        "orderid": 2124000001,
        "timest": 1767530241,
        "last_pay_time": 1767531441,
        "remain_pay_time": 600,
        "currency_type": "USDT",
        "want_type": "USD",
        "symbol": "$",
        "rate": "1.230",
        "amount": "3",
        "total": "3.690",
        "status": "paid",
        "reason_id": "",
        "reason_desc": "",
        "cancel_time": "",
        "in_appeal": 0,
        "dispute_time": 0,
        "cancelable": 1,
        "hide_payment": 0,
        "trade_tips": "Please pay from an account under your real name",
        "show_bank": "1",
        "bankname": "Demo Bank",
        "bankbranch": "Main Branch",
        "bankid": "****1234",
        "bank_holder_realname": "Merchant Demo",
        "show_ali": "0",
        "aliname": "",
        "is_alicode": 0,
        "show_wechat": "0",
        "wename": "",
        "show_others": "0",
        "pay_others": [],
        "sel_paytype": "bank",
        "its_uid": "biz_uid_demo_b84d21",
        "its_nickname": "counterparty_demo",
        "its_realname": "Counterparty Demo",
        "have_traded": 1,
        "appeal_allow_cancel": 0,
        "appeal_verdict_has_open": "",
        "im_unread": 0,
        "payment_voucher_url": [],
        "timest_paid": 1767530257,
        "own_realname": "Merchant Demo",
        "order_type": 1,
        "is_show_receive": 0,
        "show_seller_contact_info": false,
        "supported_pay_types": [
          "bank",
          "swift"
        ]
      },
      "version": "1.0.0"
    }
    

##  确认付款🔒 需要认证

POST`/p2p/merchant/transaction/confirm-payment`

POST `/p2p/merchant/transaction/confirm-payment`

_确认付款_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | ConfirmPayment | 是 |   
» txid | body | string | 是 | 订单号  
» payment_method | body | string | 否 | 本次付款使用的支付方式类型；可选，传入时必须是订单支持的支付方式。可从订单详情 supported_pay_types 或支付方式列表 pay_type 获取，例如 bank、alipay、wechat、paypal、swift、wu  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionActionResponse  
  
### 返回格式

状态码 **200**

_P2pTransactionActionResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number | 响应时间戳  
» method | string | 请求方法占位字段  
» code | integer | 响应码，0 表示成功  
» message | string | 响应消息  
» data | object | 操作成功时为空对象  
» version | string | API 版本  
  
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
    
    url = '/p2p/merchant/transaction/confirm-payment'
    query_param = ''
    body='{"txid":"40000001","payment_method":"bank"}'
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
    url="/p2p/merchant/transaction/confirm-payment"
    query_param=""
    body_param='{"txid":"40000001","payment_method":"bank"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "txid": "40000001",
      "payment_method": "bank"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  确认收款🔒 需要认证

POST`/p2p/merchant/transaction/confirm-receipt`

POST `/p2p/merchant/transaction/confirm-receipt`

_确认收款_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | ConfirmReceipt | 是 |   
» txid | body | string | 是 | 订单号  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionActionResponse  
  
### 返回格式

状态码 **200**

_P2pTransactionActionResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number | 响应时间戳  
» method | string | 请求方法占位字段  
» code | integer | 响应码，0 表示成功  
» message | string | 响应消息  
» data | object | 操作成功时为空对象  
» version | string | API 版本  
  
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
    
    url = '/p2p/merchant/transaction/confirm-receipt'
    query_param = ''
    body='{"txid":"40000001"}'
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
    url="/p2p/merchant/transaction/confirm-receipt"
    query_param=""
    body_param='{"txid":"40000001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "txid": "40000001"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  取消订单🔒 需要认证

POST`/p2p/merchant/transaction/cancel`

POST `/p2p/merchant/transaction/cancel`

_取消订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CancelOrder | 是 |   
» txid | body | string | 是 | 订单号  
» reason_id | body | string | 否 | 取消原因 ID。1：不想再买币；2：无法联系卖家；3：不会支付；4：卖家未提供真实账号；5：收款账户有问题；6：实际单价或金额与展示不一致；7：与卖家协商一致取消；8：卖家沟通不友好；9：其他；10：卖家无法放行且已退款；11：不满足广告交易条款；12：卖家收款账户被风控  
» reason_memo | body | string | 否 | 取消原因补充说明，reason_id 为 9 或需要补充说明时填写  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionActionResponse  
  
### 返回格式

状态码 **200**

_P2pTransactionActionResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number | 响应时间戳  
» method | string | 请求方法占位字段  
» code | integer | 响应码，0 表示成功  
» message | string | 响应消息  
» data | object | 操作成功时为空对象  
» version | string | API 版本  
  
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
    
    url = '/p2p/merchant/transaction/cancel'
    query_param = ''
    body='{"txid":"40000001","reason_id":"1","reason_memo":"Canceled after agreement with the counterparty"}'
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
    url="/p2p/merchant/transaction/cancel"
    query_param=""
    body_param='{"txid":"40000001","reason_id":"1","reason_memo":"Canceled after agreement with the counterparty"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "txid": "40000001",
      "reason_id": "1",
      "reason_memo": "Canceled after agreement with the counterparty"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  发布广告挂单🔒 需要认证

POST`/p2p/merchant/books/place_biz_push_order`

POST `/p2p/merchant/books/place_biz_push_order`

_发布广告挂单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | PlaceBizPushOrder | 是 |   
» currencyType | body | string | 是 | 加密币币种  
» exchangeType | body | string | 是 | 法币币种  
» type | body | string | 是 | 广告操作类型，0：发布卖币广告，1：发布买币广告，2：编辑卖币广告，3：编辑买币广告  
» unitPrice | body | string | 是 | 固定价格模式下的广告单价  
» number | body | string | 是 | 广告数量，按 currencyType 计价  
» payType | body | string | 是 | 支付方式类型，多个类型用逗号分隔；可从支付方式列表 pay_type 获取，例如 bank、alipay、wechat、paypal、swift、wu  
» pay_type_json | body | string | 否 | 支付方式和支付方式 ID 的 JSON 字符串，key 为支付方式类型，value 为当前用户支付方式 ID  
» rateFixed | body | string | 否 | 价格类型，0：浮动价格，1：固定价格  
» oid | body | string | 否 | 编辑广告时传广告 ID；发布新广告时不传或传空字符串  
» minAmount | body | string | 是 | 单笔最小交易金额，按 exchangeType 计价  
» maxAmount | body | string | 是 | 单笔最大交易金额，按 exchangeType 计价  
» tierLimit | body | string | 否 | 交易对手 VIP 等级限制，0 表示不限制  
» verifiedLimit | body | string | 否 | 交易对手认证等级限制，0 表示不限制  
» regTimeLimit | body | string | 否 | 交易对手注册天数限制，0 表示不限制  
» advertisersLimit | body | string | 否 | 是否限制与广告商交易，0：不限制，1：限制  
» expire_min | body | string | 否 | 订单付款超时时间，单位分钟  
» trade_tips | body | string | 否 | 广告交易条款，展示给下单用户  
» auto_reply | body | string | 否 | 订单创建后的自动回复内容  
» min_completed_limit | body | string | 否 | 交易对手已完成订单数最小值限制，-1 表示不限制  
» max_completed_limit | body | string | 否 | 交易对手已完成订单数最大值限制，-1 表示不限制  
» completed_rate_limit | body | string | 否 | 交易对手近 30 天完成率限制，-1 表示不限制  
» user_country_limit | body | string | 否 | KYC 国籍限制，-1 表示不限制  
» user_order_limit | body | string | 否 | 交易对手最大下单数限制，-1 表示不限制  
» rateReferenceId | body | string | 否 | 浮动价参考基准，1：平台参考价，2：Gate 参考价，3：现货参考价  
» rateOffset | body | string | 否 | 浮动价偏移比例的绝对值，例如 0.5 表示 0.5%  
» float_trend | body | string | 否 | 浮动价方向，0：上浮，1：下浮  
» team_payment_uid | body | string | 否 | 团队收款人 UID；非团队商家可不传  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» type | 0  
» type | 1  
» type | 2  
» type | 3  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMerchantBooksPlaceBizPushOrderResponse  
  
### 返回格式

状态码 **200**

_P2pMerchantBooksPlaceBizPushOrderResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number | 响应时间戳  
» method | string | 请求方法占位字段  
» code | integer | 响应码，0 表示成功  
» message | string | 响应消息  
» data | object | 发布或编辑广告成功时为空对象  
» version | string | API 版本  
  
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
    
    url = '/p2p/merchant/books/place_biz_push_order'
    query_param = ''
    body='{"currencyType":"USDT","exchangeType":"USD","type":"0","unitPrice":"1.1","number":"100","payType":"bank","pay_type_json":"{\"bank\":\"10001\",\"swift\":\"10002\"}","rateFixed":"1","oid":"2124000001","minAmount":"10","maxAmount":"500","tierLimit":"0","verifiedLimit":"0","regTimeLimit":"0","advertisersLimit":"0","expire_min":"20","trade_tips":"Please pay from an account under your own name","auto_reply":"Please tap Paid after completing the transfer","min_completed_limit":"-1","max_completed_limit":"-1","completed_rate_limit":"-1","user_country_limit":"-1","user_order_limit":"-1","rateReferenceId":"3","rateOffset":"0.5","float_trend":"0","team_payment_uid":"1000001"}'
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
    url="/p2p/merchant/books/place_biz_push_order"
    query_param=""
    body_param='{"currencyType":"USDT","exchangeType":"USD","type":"0","unitPrice":"1.1","number":"100","payType":"bank","pay_type_json":"{\"bank\":\"10001\",\"swift\":\"10002\"}","rateFixed":"1","oid":"2124000001","minAmount":"10","maxAmount":"500","tierLimit":"0","verifiedLimit":"0","regTimeLimit":"0","advertisersLimit":"0","expire_min":"20","trade_tips":"Please pay from an account under your own name","auto_reply":"Please tap Paid after completing the transfer","min_completed_limit":"-1","max_completed_limit":"-1","completed_rate_limit":"-1","user_country_limit":"-1","user_order_limit":"-1","rateReferenceId":"3","rateOffset":"0.5","float_trend":"0","team_payment_uid":"1000001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "currencyType": "USDT",
      "exchangeType": "USD",
      "type": "0",
      "unitPrice": "1.1",
      "number": "100",
      "payType": "bank",
      "pay_type_json": "{\"bank\":\"10001\",\"swift\":\"10002\"}",
      "rateFixed": "1",
      "oid": "2124000001",
      "minAmount": "10",
      "maxAmount": "500",
      "tierLimit": "0",
      "verifiedLimit": "0",
      "regTimeLimit": "0",
      "advertisersLimit": "0",
      "expire_min": "20",
      "trade_tips": "Please pay from an account under your own name",
      "auto_reply": "Please tap Paid after completing the transfer",
      "min_completed_limit": "-1",
      "max_completed_limit": "-1",
      "completed_rate_limit": "-1",
      "user_country_limit": "-1",
      "user_order_limit": "-1",
      "rateReferenceId": "3",
      "rateOffset": "0.5",
      "float_trend": "0",
      "team_payment_uid": "1000001"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  广告单状态更新🔒 需要认证

POST`/p2p/merchant/books/ads_update_status`

POST `/p2p/merchant/books/ads_update_status`

_广告单状态更新_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AdsUpdateStatus | 是 |   
» adv_no | body | integer | 是 | 广告 ID  
» adv_status | body | integer | 是 | 广告状态，1：上架，3：下架，4：关闭  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» adv_status | 1  
» adv_status | 3  
» adv_status | 4  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pAdsUpdateStatusResponse  
  
### 返回格式

状态码 **200**

_P2pAdsUpdateStatusResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» status | integer | 更新成功后的广告状态，1：上架，3：下架，4：关闭  
» version | string |   
  
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
    
    url = '/p2p/merchant/books/ads_update_status'
    query_param = ''
    body='{"adv_no":2124000001,"adv_status":3}'
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
    url="/p2p/merchant/books/ads_update_status"
    query_param=""
    body_param='{"adv_no":2124000001,"adv_status":3}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "adv_no": 2124000001,
      "adv_status": 3
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "status": 3
      },
      "version": "1.0.0"
    }
    

##  查询广告详情🔒 需要认证

POST`/p2p/merchant/books/ads_detail`

POST `/p2p/merchant/books/ads_detail`

_查询广告详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AdsDetailRequest | 是 |   
» adv_no | body | string | 是 | 广告 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pAdDetailResponse  
  
### 返回格式

状态码 **200**

_P2pAdDetailResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» rate | string | 广告价格  
»» type | string | 广告方向，buy：买币广告，sell：卖币广告  
»» amount | string | 广告剩余加密币数量  
»» min_amount | string | 单笔最小交易金额，按 want_type 计价  
»» max_amount | string | 单笔最大交易金额，按 want_type 计价  
»» total | string | 法币金额  
»» pay_ali | integer | 是否支持支付宝支付，1：支持，0：不支持  
»» pay_bank | integer | 是否支持银行转账，1：支持，0：不支持  
»» pay_paypal | integer | 是否支持 PayPal，1：支持，0：不支持  
»» pay_wechat | integer | 是否支持微信支付，1：支持，0：不支持  
»» pay_type_num | string | 支付方式数字列表  
»» pay_type_json | string | 支付方式配置详情，JSON 字符串，key 为支付方式类型，value 为支付方式 ID  
»» locked_amount | string | 锁定数量  
»» orderid | integer | 订单号  
»» timestamp | integer | 创建时间  
»» currency_type | string | 加密币币种  
»» want_type | string | 法币类型  
»» hide_rate | string | 隐藏价格  
»» trade_tips | string | 交易条款  
»» auto_reply | string | 自动回复  
»» rate_ref_id | integer | 浮动价参考基准，1：平台参考价，2：Gate 参考价，3：现货参考价；小于等于 0 表示固定价格  
»» rate_offset | number | 浮动比例（绝对值）  
»» status | string | 广告状态，OPEN：上架，OFFLIN：下架，CLOSED：关闭，CANCEL：取消  
»» rate_fixed | integer | 价格类型，0：浮动价格，1：固定价格  
»» float_trend | integer | 浮动价方向，0：上浮，1：下浮  
»» expire_min | integer | 超时时间（分钟）  
»» tier_limit | integer | 等级限制  
»» reg_time_limit | integer | 注册时间限制  
»» advertisers_limit | integer | 是否限制与广告商交易，0：不限制，1：限制  
»» min_completed_limit | integer | 完成订单数最小值限制  
»» max_completed_limit | integer | 完成订单数最大值限制  
»» user_orders_limit | integer | 下单数限制  
»» completed_rate_limit | number | 30日完成率限制  
»» limit_country_cn | string | 限制国籍中文名  
»» limit_country_en | string | 限制国籍英文名  
»» is_hedge | integer | 是否自动委托，1：是，0：否  
»» hide_payment | integer | 是否隐藏支付方式，1：隐藏，0：不隐藏  
» version | string |   
  
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
    
    url = '/p2p/merchant/books/ads_detail'
    query_param = ''
    body='{"adv_no":"2124000001"}'
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
    url="/p2p/merchant/books/ads_detail"
    query_param=""
    body_param='{"adv_no":"2124000001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "adv_no": "2124000001"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767149820.871772,
      "method": "--",
      "code": 0,
      "message": "Success",
      "data": {
        "rate": "0.908",
        "type": "sell",
        "amount": "100.00",
        "min_amount": "10",
        "max_amount": "500",
        "total": "90.800",
        "pay_ali": 0,
        "pay_bank": 1,
        "pay_paypal": 0,
        "pay_wechat": 0,
        "pay_type_num": "2,5",
        "pay_type_json": "{\"bank\":\"10001\",\"swift\":\"10002\"}",
        "locked_amount": "0",
        "orderid": 2124000001,
        "timestamp": 1766988136,
        "currency_type": "USDT",
        "want_type": "USD",
        "hide_rate": "0.000",
        "trade_tips": "Please pay from an account under your real name",
        "auto_reply": "Thanks for your order. I will process it soon.",
        "rate_ref_id": 3,
        "rate_offset": 0.5,
        "status": "OPEN",
        "rate_fixed": 0,
        "float_trend": 0,
        "expire_min": 20,
        "tier_limit": 0,
        "reg_time_limit": 0,
        "advertisers_limit": 0,
        "min_completed_limit": -1,
        "max_completed_limit": -1,
        "user_orders_limit": -1,
        "completed_rate_limit": -1,
        "limit_country_cn": "",
        "limit_country_en": "",
        "is_hedge": 0,
        "hide_payment": 0
      },
      "version": "1.0.0"
    }
    

##  获取我的广告列表🔒 需要认证

POST`/p2p/merchant/books/my_ads_list`

POST `/p2p/merchant/books/my_ads_list`

_获取我的广告列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | MyAdsListRequest | 否 |   
» asset | body | string | 否 | 加密币币种。不传时不按加密币筛选  
» fiat_unit | body | string | 否 | 法币币种。不传时不按法币筛选  
» trade_type | body | string | 否 | 广告方向，buy 表示买币广告，sell 表示卖币广告；不传时返回全部方向  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMyAdsListResponse  
  
### 返回格式

状态码 **200**

_P2pMyAdsListResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» lists | array |   
»»» P2pMyAd | object |   
»»»» type | string | 广告方向，buy：买币广告，sell：卖币广告  
»»»» rate | string | 价格  
»»»» original_rate | string | 原始价格  
»»»» amount | string | 广告剩余加密币数量  
»»»» total | string | 广告剩余法币金额  
»»»» limit_total | string | 单笔限额范围-数字币  
»»»» limit_fiat | string | 单笔限额范围-法币  
»»»» min_amount | string | 单笔最小数量  
»»»» max_amount | string | 单笔最大数量  
»»»» pay_type_num | string | 支付方式 Id 列表  
»»»» pay_type_json | string | 支付方式配置详情，JSON 字符串，key 为支付方式类型，value 为支付方式 ID  
»»»» expire_min | string | 广告过期时间(分钟)  
»»»» tier_limit | string | VIP 限制  
»»»» advertisers_limit | integer | 是否限制与广告商交易，0：不限制，1：限制  
»»»» reg_time_limit | integer | 注册时间限制  
»»»» verified_limit | integer | KYC 等级限制  
»»»» min_completed_limit | integer | 交易对手已完成的订单数最小值限制  
»»»» max_completed_limit | integer | 交易对手已完成的订单数最大值限制  
»»»» user_country_limit | integer | KYC国籍限制  
»»»» completed_rate_limit | number | 30天完成率限制  
»»»» user_orders_limit | integer | 交易对方最大下单数限制  
»»»» hide_payment | string | 是否隐藏支付方式，1：隐藏，0：不隐藏  
»»»» currencyType | string | 加密币币种  
»»»» want_type | string | 法币  
»»»» trade_tips | string | 交易条款  
»»»» new_hand | integer | 特殊广告类型，0：普通单，1：新手引导单，2：新手折扣单，3：精选特惠单，4：KOL 广告单，5：卡券广告单  
»»»» id | string | 广告 ID  
»»»» status | string | 广告状态，OPEN：上架，OFFLIN：下架，CLOSED：关闭，CANCEL：取消  
»»»» locked_amount | string | 广告冻结金额  
»»»» hide_rate | string | 隐藏价格  
»»»» is_out_time | integer | 广告当前是否超时，1：已超时，0：未超时  
»»»» rate_ref_id | integer | 浮动价参考基准，1：平台参考价，2：Gate 参考价，3：现货参考价；小于等于 0 表示固定价格  
»»»» rate_offset | string | 浮动比例  
»»»» rate_fixed | integer | 价格类型，0：浮动价格，1：固定价格  
»»»» float_trend | integer | 浮动价方向，0：上浮，1：下浮  
»»»» in_dispute | integer | 广告是否存在申诉交易，1：存在，0：不存在  
»»»» auto_reply | string | 自动回复数据  
»»»» timestamp | integer | 广告创建时间  
»»»» is_hedge | integer | 是否自动委托，1：是，0：否  
»»» version | string | 版本号  
  
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
    
    url = '/p2p/merchant/books/my_ads_list'
    query_param = ''
    body='{"asset":"USDT","fiat_unit":"USD","trade_type":"sell"}'
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
    url="/p2p/merchant/books/my_ads_list"
    query_param=""
    body_param='{"asset":"USDT","fiat_unit":"USD","trade_type":"sell"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767088873.074896,
      "method": "--",
      "code": 0,
      "message": "Success",
      "data": {
        "lists": [
          {
            "type": "sell",
            "rate": "1.270",
            "original_rate": "1.270",
            "amount": "100.00",
            "total": "127.000",
            "limit_total": "10~500",
            "limit_fiat": "12.7~635",
            "min_amount": "10",
            "max_amount": "500",
            "pay_type_num": "2,4",
            "pay_type_json": "{\"bank\":\"10001\",\"wu\":\"10003\"}",
            "expire_min": "45",
            "tier_limit": "1",
            "advertisers_limit": 1,
            "reg_time_limit": 90,
            "verified_limit": 0,
            "min_completed_limit": 8,
            "max_completed_limit": 9,
            "user_country_limit": 4,
            "completed_rate_limit": 6,
            "user_orders_limit": 7,
            "hide_payment": "1",
            "currencyType": "USDT",
            "want_type": "USD",
            "trade_tips": "Please pay from an account under your real name",
            "new_hand": 0,
            "id": "2124000001",
            "status": "OFFLIN",
            "locked_amount": "0",
            "hide_rate": "0.000",
            "is_out_time": 0,
            "rate_ref_id": -1,
            "rate_offset": "0",
            "rate_fixed": 1,
            "float_trend": 0,
            "in_dispute": 0,
            "auto_reply": "Thanks for your order. I will process it soon.",
            "timestamp": 1767008930,
            "is_hedge": 0
          }
        ]
      },
      "version": "1.0.0"
    }
    

##  获取广告列表🔒 需要认证

POST`/p2p/merchant/books/ads_list`

POST `/p2p/merchant/books/ads_list`

_获取广告列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AdsListRequest | 是 |   
» asset | body | string | 是 | 加密币币种  
» fiat_unit | body | string | 是 | 法币币种  
» trade_type | body | string | 是 | 广告方向，buy 表示买币广告，sell 表示卖币广告  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pAdsListResponse  
  
### 返回格式

状态码 **200**

_P2pAdsListResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | array |   
»» P2pAdsListItem | object |   
»»» index | integer | 序号  
»»» asset | string | 加密货币  
»»» fiat_unit | string | 法币  
»»» adv_no | integer | 广告id  
»»» price | string | 价格  
»»» max_single_trans_amount | string | 单笔最大加密币交易数量  
»»» min_single_trans_amount | string | 单笔最小加密币交易数量  
»»» nick_name | string | 广告商昵称  
»» version | string |   
  
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
    
    url = '/p2p/merchant/books/ads_list'
    query_param = ''
    body='{"asset":"USDT","fiat_unit":"USD","trade_type":"sell"}'
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
    url="/p2p/merchant/books/ads_list"
    query_param=""
    body_param='{"asset":"USDT","fiat_unit":"USD","trade_type":"sell"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1769573081.981503,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": [
        {
          "index": 1,
          "asset": "USDT",
          "fiat_unit": "USD",
          "adv_no": 2124000001,
          "price": "0.800",
          "max_single_trans_amount": "4975.5",
          "min_single_trans_amount": "1",
          "nick_name": "merchant_demo_01"
        },
        {
          "index": 2,
          "asset": "USDT",
          "fiat_unit": "USD",
          "adv_no": 2124000002,
          "price": "0.880",
          "max_single_trans_amount": "12379.15",
          "min_single_trans_amount": "10",
          "nick_name": "merchant_demo_02"
        },
        {
          "index": 3,
          "asset": "USDT",
          "fiat_unit": "USD",
          "adv_no": 2124000003,
          "price": "1.000",
          "max_single_trans_amount": "2",
          "min_single_trans_amount": "1",
          "nick_name": "merchant_demo_03"
        }
      ],
      "version": "1.0.0"
    }
    

##  获取聊天记录🔒 需要认证

POST`/p2p/merchant/chat/get_chats_list`

POST `/p2p/merchant/chat/get_chats_list`

_获取聊天记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | GetChatsListRequest | 是 |   
» txid | body | integer | 否 | 订单号。不传或传 0 时，返回当前用户最近一笔有聊天记录的订单  
» lastreceived | body | integer | 否 | 已接收的最后一条消息时间戳，用于向后增量拉取；首次加载可不传  
» firstreceived | body | integer | 否 | 已接收的第一条消息时间戳，用于向前翻页；首次加载可不传  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pChatListResponse  
  
### 返回格式

状态码 **200**

_P2pChatListResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» messages | array | 消息列表  
»»» P2pChatMessage | object |   
»»»» is_sell | integer | 当前用户是否为卖家，1：是，0：否  
»»»» msg_type | integer | 消息类型，0：文本，1：文件，2：模板消息，3：挂单分享，4：支付方式分享，5：订单状态流转消息  
»»»» msg | string | 消息内容。文件消息时通常为文件 URL 或文件 key  
»»»» username | string | 消息发送用户名  
»»»» timest | integer | 消息发送时间戳  
»»»» msg_obj | object |   
»»»»» status | string | 发送消息时的订单状态，常见值：OPEN、PAID、LOCKED、ACCEPT、BCLOSED、CANCEL、BECANCEL、SCLOSED、SCANCEL  
»»»»» text | string | 消息内容  
»»»»» payment_voucher | array | 支付凭证  
»»»»» reason_id | integer | 取消原因 ID。1：不想再买币；2：无法联系卖家；3：不会支付；4：卖家未提供真实账号；5：收款账户有问题；6：实际单价或金额与展示不一致；7：与卖家协商一致取消；8：卖家沟通不友好；9：其他；10：卖家无法放行且已退款；11：不满足广告交易条款；12：卖家收款账户被风控  
»»»»» toast_id | integer | 取消原因弹窗  
»»»»» reason_memo | string | 取消原因说明  
»»»»» cancel_time | integer | 取消时间  
»»»»» seller_confirm | integer | 卖家是否确认取消原因，0：未确认，1：已确认，2：已拒绝  
»»»»» id | string | 支付方式信息id  
»»»»» account_des | string | 支付方式描述  
»»»»» pay_type | string | 支付方式类型  
»»»»» file | string | 支付方式文件链接  
»»»»» file_key | string | 支付方式文件key  
»»»»» account | string | 支付账号或脱敏支付账号  
»»»»» memo | string | 支付方式备注  
»»»»» code | string | 支付方式code  
»»»»» memo_ext | string | 支付方式额外备注  
»»»»» trade_tips | string | 支付方式提示信息  
»»»»» real_name | string | 支付方式用户名  
»»»»» is_delete | integer | 支付方式是否已删除，1：已删除，0：未删除  
»»»»» pay_name | string | 支付方式全称  
»»»» uid | string | 消息发送方加密 UID；系统消息可能为 System 或空字符串  
»»»» type | integer | 展示类型，1：文件消息，2：系统消息  
»»»» pic | string | 文件链接  
»»»» file_key | string | 文件key  
»»»» file_type | string | 文件类型，image：图片，video：视频  
»»» memo | string | 支付提示，仅首页展示  
»»» has_history | boolean | 是否存在历史记录  
»»» txid | integer | 订单号  
»»» SRVTM | integer | 最新一条消息的时间戳  
»»» order_status | string | 订单数据库状态，常见值：OPEN、PAID、LOCKED、ACCEPT、BCLOSED、CANCEL、BECANCEL、SCLOSED、SCANCEL  
»» version | string |   
  
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
    
    url = '/p2p/merchant/chat/get_chats_list'
    query_param = ''
    body='{"txid":40000001,"lastreceived":1767009884,"firstreceived":1767009000}'
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
    url="/p2p/merchant/chat/get_chats_list"
    query_param=""
    body_param='{"txid":40000001,"lastreceived":1767009884,"firstreceived":1767009000}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "txid": 40000001,
      "lastreceived": 1767009884,
      "firstreceived": 1767009000
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767086748.178922,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "messages": [
          {
            "is_sell": 1,
            "msg_type": 0,
            "msg": "Please tap Paid after completing the transfer",
            "username": "Self",
            "timest": 1767009000
          },
          {
            "is_sell": 1,
            "msg_type": 5,
            "msg": "",
            "username": "Other",
            "msg_obj": {
              "status": "OPEN",
              "text": "Order created. Awaiting buyer's payment.",
              "payment_voucher": []
            },
            "uid": "",
            "timest": 1767009001
          },
          {
            "is_sell": 1,
            "msg_type": 5,
            "msg": "",
            "username": "Other",
            "msg_obj": {
              "status": "CANCEL",
              "text": "The buyer has canceled the order.",
              "reason_id": 1,
              "toast_id": 1,
              "reason_memo": "I don't want to buy the coins anymore.",
              "cancel_time": 1767009300,
              "seller_confirm": 0,
              "payment_voucher": []
            },
            "uid": "",
            "timest": 1767009300
          },
          {
            "uid": "System",
            "username": "System",
            "type": 2,
            "msg": "Please keep all communication within the Gate platform.",
            "timest": 1767009400
          },
          {
            "is_sell": 1,
            "msg_type": 4,
            "msg": "",
            "username": "Other",
            "uid": "biz_uid_demo_b84d21",
            "timest": 1767009500,
            "msg_obj": {
              "id": "10002",
              "account_des": "Business USD account",
              "pay_type": "swift",
              "file": "",
              "file_key": "",
              "account": "****5678",
              "memo": "Use order txid as reference",
              "code": "",
              "memo_ext": "",
              "trade_tips": "Please pay from an account under your real name",
              "real_name": "Merchant Demo",
              "is_delete": 1,
              "pay_name": "SWIFT International Remittance"
            }
          },
          {
            "is_sell": 1,
            "msg_type": 0,
            "msg": "Payment completed, please check",
            "username": "Other",
            "timest": 1767009600
          },
          {
            "is_sell": 1,
            "msg_type": 1,
            "msg": "https://example.com/p2p/chat/receipt.png",
            "username": "Other",
            "timest": 1767009700,
            "pic": "https://example.com/p2p/chat/receipt.png",
            "file_key": "c2cchat_image/c2ctrade-demo-receipt|s3-gateio-payments",
            "file_type": "image",
            "type": 1
          }
        ],
        "memo": "",
        "has_history": false,
        "txid": 40000001,
        "SRVTM": 1767009700,
        "order_status": "CANCEL"
      },
      "version": "1.0.0"
    }
    

##  发送文本消息🔒 需要认证

POST`/p2p/merchant/chat/send_chat_message`

POST `/p2p/merchant/chat/send_chat_message`

_发送文本消息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | SendChatMessageRequest | 是 |   
» txid | body | integer | 是 | 订单号  
» type | body | integer | 否 | 消息类型，0：文本，1：文件（图片或视频）；不传默认为 0  
» message | body | string | 是 | 消息内容。type=0 时传文本，最长 500 个字符；type=1 时传 upload_chat_file 返回的 file_key  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» type | 0  
» type | 1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pSendChatMessageResponse  
  
### 返回格式

状态码 **200**

_P2pSendChatMessageResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» SRVTM | integer | 成功发送消息的时间（当前时间戳）  
» version | string |   
  
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
    
    url = '/p2p/merchant/chat/send_chat_message'
    query_param = ''
    body='{"txid":40000001,"type":0,"message":"Payment completed, please check"}'
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
    url="/p2p/merchant/chat/send_chat_message"
    query_param=""
    body_param='{"txid":40000001,"type":0,"message":"Payment completed, please check"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "txid": 40000001,
      "type": 0,
      "message": "Payment completed, please check"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "SRVTM": 1767009886638
      },
      "version": "1.0.0"
    }
    

##  上传聊天文件🔒 需要认证

POST`/p2p/merchant/chat/upload_chat_file`

POST `/p2p/merchant/chat/upload_chat_file`

_上传聊天文件_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | UploadChatFile | 是 |   
» image_content_type | body | string | 是 | 文件 MIME 类型，支持 image/jpeg、image/jpg、image/png、video/mp4  
» base64_img | body | string | 是 | 文件内容的 Base64 编码，最大 20 MB  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» image_content_type | image/jpeg  
» image_content_type | image/jpg  
» image_content_type | image/png  
» image_content_type | video/mp4  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pUploadChatFileResponse  
  
### 返回格式

状态码 **200**

_P2pUploadChatFileResponse_

名称 | 类型 | 描述  
---|---|---  
» timestamp | number |   
» method | string |   
» code | integer |   
» message | string |   
» data | object |   
»» file_key | string | 文件key  
» version | string |   
  
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
    
    url = '/p2p/merchant/chat/upload_chat_file'
    query_param = ''
    body='{"image_content_type":"image/png","base64_img":"iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."}'
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
    url="/p2p/merchant/chat/upload_chat_file"
    query_param=""
    body_param='{"image_content_type":"image/png","base64_img":"iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "image_content_type": "image/png",
      "base64_img": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1767009875.525072,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "file_key": "c2cchat_image/c2ctrade-demo-receipt|s3-gateio-payments"
      },
      "version": "1.0.0"
    }
    

#  模型

##  P2pAdDetailResponse

_P2pAdDetailResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» rate | string | false | none | 广告价格  
» type | string | false | none | 广告方向，buy：买币广告，sell：卖币广告  
» amount | string | false | none | 广告剩余加密币数量  
» min_amount | string | false | none | 单笔最小交易金额，按 want_type 计价  
» max_amount | string | false | none | 单笔最大交易金额，按 want_type 计价  
» total | string | false | none | 法币金额  
» pay_ali | integer | false | none | 是否支持支付宝支付，1：支持，0：不支持  
» pay_bank | integer | false | none | 是否支持银行转账，1：支持，0：不支持  
» pay_paypal | integer | false | none | 是否支持 PayPal，1：支持，0：不支持  
» pay_wechat | integer | false | none | 是否支持微信支付，1：支持，0：不支持  
» pay_type_num | string | false | none | 支付方式数字列表  
» pay_type_json | string | false | none | 支付方式配置详情，JSON 字符串，key 为支付方式类型，value 为支付方式 ID  
» locked_amount | string | false | none | 锁定数量  
» orderid | integer | false | none | 订单号  
» timestamp | integer | false | none | 创建时间  
» currency_type | string | false | none | 加密币币种  
» want_type | string | false | none | 法币类型  
» hide_rate | string | false | none | 隐藏价格  
» trade_tips | string | false | none | 交易条款  
» auto_reply | string | false | none | 自动回复  
» rate_ref_id | integer | false | none | 浮动价参考基准，1：平台参考价，2：Gate 参考价，3：现货参考价；小于等于 0 表示固定价格  
» rate_offset | number | false | none | 浮动比例（绝对值）  
» status | string | false | none | 广告状态，OPEN：上架，OFFLIN：下架，CLOSED：关闭，CANCEL：取消  
» rate_fixed | integer | false | none | 价格类型，0：浮动价格，1：固定价格  
» float_trend | integer | false | none | 浮动价方向，0：上浮，1：下浮  
» expire_min | integer | false | none | 超时时间（分钟）  
» tier_limit | integer | false | none | 等级限制  
» reg_time_limit | integer | false | none | 注册时间限制  
» advertisers_limit | integer | false | none | 是否限制与广告商交易，0：不限制，1：限制  
» min_completed_limit | integer | false | none | 完成订单数最小值限制  
» max_completed_limit | integer | false | none | 完成订单数最大值限制  
» user_orders_limit | integer | false | none | 下单数限制  
» completed_rate_limit | number | false | none | 30日完成率限制  
» limit_country_cn | string | false | none | 限制国籍中文名  
» limit_country_en | string | false | none | 限制国籍英文名  
» is_hedge | integer | false | none | 是否自动委托，1：是，0：否  
» hide_payment | integer | false | none | 是否隐藏支付方式，1：隐藏，0：不隐藏  
version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "rate": "string",
        "type": "string",
        "amount": "string",
        "min_amount": "string",
        "max_amount": "string",
        "total": "string",
        "pay_ali": 0,
        "pay_bank": 0,
        "pay_paypal": 0,
        "pay_wechat": 0,
        "pay_type_num": "string",
        "pay_type_json": "string",
        "locked_amount": "string",
        "orderid": 0,
        "timestamp": 0,
        "currency_type": "string",
        "want_type": "string",
        "hide_rate": "string",
        "trade_tips": "string",
        "auto_reply": "string",
        "rate_ref_id": 0,
        "rate_offset": 0,
        "status": "string",
        "rate_fixed": 0,
        "float_trend": 0,
        "expire_min": 0,
        "tier_limit": 0,
        "reg_time_limit": 0,
        "advertisers_limit": 0,
        "min_completed_limit": 0,
        "max_completed_limit": 0,
        "user_orders_limit": 0,
        "completed_rate_limit": 0,
        "limit_country_cn": "string",
        "limit_country_en": "string",
        "is_hedge": 0,
        "hide_payment": 0
      },
      "version": "string"
    }
    
    

##  P2pTransactionDetailResponse

_P2pTransactionDetailResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» is_sell | integer | false | none | 当前用户是否为卖家，1：是，0：否  
» txid | integer | false | none | 订单号  
» orderid | integer | false | none | 挂单号  
» timest | integer | false | none | 订单创建时间戳  
» last_pay_time | integer | false | none | 终止付款时间  
» remain_pay_time | integer | false | none | 剩余付款时间，单位秒；小于等于 0 表示已超时  
» currency_type | string | false | none | 加密币币种  
» want_type | string | false | none | 法币币种  
» symbol | string | false | none | 法币符号  
» rate | string | false | none | 订单价格，按 want_type 计价  
» amount | string | false | none | 订单加密币数量  
» total | string | false | none | 订单法币总金额  
» status | string | false | none | 订单展示状态，unpay：待付款，hide_payment：待付款但支付信息隐藏，paid：买家已付款，unconfirmed：待卖家确认收款，locked：已锁定，finished：已完成，cancel：已取消，expired：已过期，bclosed：仲裁成交，sclosed：仲裁取消  
» reason_id | string | false | none | 取消原因 ID，空字符串表示无取消原因；常见值：1 不想再买币，2 无法联系卖家，3 不会支付，4 卖家未提供真实账号，6 实际单价或金额不一致，9 其他，10 卖家无法放行且已退款，11 不满足广告交易条款，12 卖家收款账户被风控  
» reason_desc | string | false | none | 取消原因说明  
» cancel_time | string | false | none | 取消时间  
» in_appeal | integer | false | none | 是否申诉中，1：是，0：否  
» dispute_time | integer | false | none | 允许发起申诉的时间戳  
» cancelable | integer | false | none | 是否允许取消订单，1：允许，0：不允许  
» hide_payment | integer | false | none | 是否隐藏支付方式，1：隐藏，0：不隐藏  
» trade_tips | string | false | none | 交易条款  
» show_bank | string | false | none | 是否展示银行转账信息，1：展示，0：不展示  
» bankname | string | false | none | 银行名称  
» bankbranch | string | false | none | 银行支行名称  
» bankid | string | false | none | 银行账号或脱敏银行账号  
» bank_holder_realname | string | false | none | 银行持卡人姓名  
» show_ali | string | false | none | 是否展示支付宝信息，1：展示，0：不展示  
» aliname | string | false | none | 支付宝账户名  
» is_alicode | integer | false | none | 是否存在支付宝收款码，1：存在，0：不存在  
» show_wechat | string | false | none | 是否展示微信信息，1：展示，0：不展示  
» wename | string | false | none | 微信账户名  
» show_others | string | false | none | 是否展示其他支付方式，1：展示，0：不展示  
» pay_others | array | false | none | 其他支付方式  
»» id | string | false | none | 支付方式记录 ID  
»» account_des | string | false | none | 支付方式描述  
»» pay_type | string | false | none | 支付方式类型  
»» account | string | false | none | 支付账号或脱敏账号  
»» memo | string | false | none | 支付备注  
»» trade_tips | string | false | none | 支付提示  
»» pay_name | string | false | none | 支付方式展示名称  
» sel_paytype | string | false | none | 当前订单选择的支付方式类型，例如 bank、alipay、wechat、paypal、swift、wu  
» its_uid | string | false | none | 对手方加密 UID  
» its_nickname | string | false | none | 对方昵称  
» its_realname | string | false | none | 对方真实姓名或实名展示名  
» have_traded | integer | false | none | 是否与对方交易过，1：是，0：否  
» appeal_allow_cancel | integer | false | none | 是否允许撤销申诉，1：允许，0：不允许  
» appeal_verdict_has_open | string | false | none | 申诉结果或申诉中提示文案  
» im_unread | integer | false | none | 聊天未读消息数  
» payment_voucher_url | array | false | none | 支付凭证  
» timest_paid | integer | false | none | 买家确认付款时间戳  
» own_realname | string | false | none | 当前用户真实姓名或实名展示名  
» order_type | integer | false | none | 订单类型，1：普通订单，2：三方合作订单，3：闪兑订单，4：Web3 订单  
» is_show_receive | integer | false | none | 申诉中是否展示确认收款入口，1：展示，0：不展示  
» show_seller_contact_info | boolean | false | none | 是否展示卖家联系方式  
» supported_pay_types | array | false | none | 当前订单支持的支付方式类型，例如 bank、alipay、wechat、paypal、swift、wu  
version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "is_sell": 0,
        "txid": 0,
        "orderid": 0,
        "timest": 0,
        "last_pay_time": 0,
        "remain_pay_time": 0,
        "currency_type": "string",
        "want_type": "string",
        "symbol": "string",
        "rate": "string",
        "amount": "string",
        "total": "string",
        "status": "string",
        "reason_id": "string",
        "reason_desc": "string",
        "cancel_time": "string",
        "in_appeal": 0,
        "dispute_time": 0,
        "cancelable": 0,
        "hide_payment": 0,
        "trade_tips": "string",
        "show_bank": "string",
        "bankname": "string",
        "bankbranch": "string",
        "bankid": "string",
        "bank_holder_realname": "string",
        "show_ali": "string",
        "aliname": "string",
        "is_alicode": 0,
        "show_wechat": "string",
        "wename": "string",
        "show_others": "string",
        "pay_others": [
          {}
        ],
        "sel_paytype": "string",
        "its_uid": "string",
        "its_nickname": "string",
        "its_realname": "string",
        "have_traded": 0,
        "appeal_allow_cancel": 0,
        "appeal_verdict_has_open": "string",
        "im_unread": 0,
        "payment_voucher_url": [
          "string"
        ],
        "timest_paid": 0,
        "own_realname": "string",
        "order_type": 0,
        "is_show_receive": 0,
        "show_seller_contact_info": true,
        "supported_pay_types": [
          "string"
        ]
      },
      "version": "string"
    }
    
    

##  GetTransactionDetailsRequest

_获取订单详情请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
txid | integer | true | none | 订单号  
channel | string | false | none | 渠道标识，普通 P2P 订单不传或传空字符串；Web3 订单传 web3  
      
    
    {
      "txid": 40000001,
      "channel": ""
    }
    
    

##  SendChatMessageRequest

_发送聊天消息请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
txid | integer | true | none | 订单号  
type | integer | false | none | 消息类型，0：文本，1：文件（图片或视频）；不传默认为 0  
message | string | true | none | 消息内容。type=0 时传文本，最长 500 个字符；type=1 时传 upload_chat_file 返回的 file_key  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | 0  
type | 1  
      
    
    {
      "txid": 40000001,
      "type": 0,
      "message": "Payment completed, please check"
    }
    
    

##  CancelOrder

_取消订单请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
txid | string | true | none | 订单号  
reason_id | string | false | none | 取消原因 ID。1：不想再买币；2：无法联系卖家；3：不会支付；4：卖家未提供真实账号；5：收款账户有问题；6：实际单价或金额与展示不一致；7：与卖家协商一致取消；8：卖家沟通不友好；9：其他；10：卖家无法放行且已退款；11：不满足广告交易条款；12：卖家收款账户被风控  
reason_memo | string | false | none | 取消原因补充说明，reason_id 为 9 或需要补充说明时填写  
      
    
    {
      "txid": "40000001",
      "reason_id": "1",
      "reason_memo": "Canceled after agreement with the counterparty"
    }
    
    

##  P2pTransactionActionResponse

_P2pTransactionActionResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | 响应时间戳  
method | string | false | none | 请求方法占位字段  
code | integer | false | none | 响应码，0 表示成功  
message | string | false | none | 响应消息  
data | object | false | none | 操作成功时为空对象  
version | string | false | none | API 版本  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {},
      "version": "string"
    }
    
    

##  MyAdsListRequest

_获取我的广告列表请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
asset | string | false | none | 加密币币种。不传时不按加密币筛选  
fiat_unit | string | false | none | 法币币种。不传时不按法币筛选  
trade_type | string | false | none | 广告方向，buy 表示买币广告，sell 表示卖币广告；不传时返回全部方向  
      
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    
    

##  GetCompletedTransactionListRequest

_获取所有/历史订单请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
crypto_currency | string | true | none | 加密币币种  
fiat_currency | string | true | none | 法币币种  
select_type | string | false | none | 订单方向筛选，buy：买单，sell：卖单，空字符串或不传：全部  
status | string | false | none | 订单状态筛选。closed：已成交（ACCEPT、BCLOSED）；cancel：已取消（CANCEL、BECANCEL、SCLOSED、SCANCEL）；  
locked：已锁定（LOCKED）；open：未付款（OPEN）；paid：已付款（PAID）；  
completed：已完成或已取消（CANCEL、BECANCEL、SCLOSED、SCANCEL、ACCEPT、BCLOSED）；  
空字符串或不传时按接口默认范围查询。  
txid | integer | false | none | 订单号  
start_time | integer | false | none | 开始时间时间戳，默认89天前0点  
end_time | integer | false | none | 结束时间时间戳，默认今天23:59:59  
query_dispute | integer | false | none | 是否在返回结果中标记申诉状态，1：标记，0：不标记  
page | integer | false | none | 页码，从 1 开始；小于 1 时按 1 处理  
per_page | integer | false | none | 每页订单数，默认 10，最大 200  
      
    
    {
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "select_type": "buy",
      "status": "closed",
      "txid": 40000001,
      "start_time": 1764547200,
      "end_time": 1767139199,
      "query_dispute": 0,
      "page": 1,
      "per_page": 20
    }
    
    

##  GetChatsListRequest

_获取聊天记录请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
txid | integer | false | none | 订单号。不传或传 0 时，返回当前用户最近一笔有聊天记录的订单  
lastreceived | integer | false | none | 已接收的最后一条消息时间戳，用于向后增量拉取；首次加载可不传  
firstreceived | integer | false | none | 已接收的第一条消息时间戳，用于向前翻页；首次加载可不传  
      
    
    {
      "txid": 40000001,
      "lastreceived": 1767009884,
      "firstreceived": 1767009000
    }
    
    

##  P2pMerchantBooksPlaceBizPushOrderResponse

_P2pMerchantBooksPlaceBizPushOrderResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | 响应时间戳  
method | string | false | none | 请求方法占位字段  
code | integer | false | none | 响应码，0 表示成功  
message | string | false | none | 响应消息  
data | object | false | none | 发布或编辑广告成功时为空对象  
version | string | false | none | API 版本  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {},
      "version": "string"
    }
    
    

##  UploadChatFile

_上传聊天文件请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
image_content_type | string | true | none | 文件 MIME 类型，支持 image/jpeg、image/jpg、image/png、video/mp4  
base64_img | string | true | none | 文件内容的 Base64 编码，最大 20 MB  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
image_content_type | image/jpeg  
image_content_type | image/jpg  
image_content_type | image/png  
image_content_type | video/mp4  
      
    
    {
      "image_content_type": "image/png",
      "base64_img": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."
    }
    
    

##  P2pAdsUpdateStatusResponse

_P2pAdsUpdateStatusResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» status | integer | false | none | 更新成功后的广告状态，1：上架，3：下架，4：关闭  
version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "status": 0
      },
      "version": "string"
    }
    
    

##  P2pChatListResponse

_P2pChatListResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» messages | array | false | none | 消息列表  
»» P2pChatMessage | object | false | none | none  
»»» is_sell | integer | false | none | 当前用户是否为卖家，1：是，0：否  
»»» msg_type | integer | false | none | 消息类型，0：文本，1：文件，2：模板消息，3：挂单分享，4：支付方式分享，5：订单状态流转消息  
»»» msg | string | false | none | 消息内容。文件消息时通常为文件 URL 或文件 key  
»»» username | string | false | none | 消息发送用户名  
»»» timest | integer | false | none | 消息发送时间戳  
»»» msg_obj | object | false | none | none  
»»»» status | string | false | none | 发送消息时的订单状态，常见值：OPEN、PAID、LOCKED、ACCEPT、BCLOSED、CANCEL、BECANCEL、SCLOSED、SCANCEL  
»»»» text | string | false | none | 消息内容  
»»»» payment_voucher | array | false | none | 支付凭证  
»»»» reason_id | integer | false | none | 取消原因 ID。1：不想再买币；2：无法联系卖家；3：不会支付；4：卖家未提供真实账号；5：收款账户有问题；6：实际单价或金额与展示不一致；7：与卖家协商一致取消；8：卖家沟通不友好；9：其他；10：卖家无法放行且已退款；11：不满足广告交易条款；12：卖家收款账户被风控  
»»»» toast_id | integer | false | none | 取消原因弹窗  
»»»» reason_memo | string | false | none | 取消原因说明  
»»»» cancel_time | integer | false | none | 取消时间  
»»»» seller_confirm | integer | false | none | 卖家是否确认取消原因，0：未确认，1：已确认，2：已拒绝  
»»»» id | string | false | none | 支付方式信息id  
»»»» account_des | string | false | none | 支付方式描述  
»»»» pay_type | string | false | none | 支付方式类型  
»»»» file | string | false | none | 支付方式文件链接  
»»»» file_key | string | false | none | 支付方式文件key  
»»»» account | string | false | none | 支付账号或脱敏支付账号  
»»»» memo | string | false | none | 支付方式备注  
»»»» code | string | false | none | 支付方式code  
»»»» memo_ext | string | false | none | 支付方式额外备注  
»»»» trade_tips | string | false | none | 支付方式提示信息  
»»»» real_name | string | false | none | 支付方式用户名  
»»»» is_delete | integer | false | none | 支付方式是否已删除，1：已删除，0：未删除  
»»»» pay_name | string | false | none | 支付方式全称  
»»» uid | string | false | none | 消息发送方加密 UID；系统消息可能为 System 或空字符串  
»»» type | integer | false | none | 展示类型，1：文件消息，2：系统消息  
»»» pic | string | false | none | 文件链接  
»»» file_key | string | false | none | 文件key  
»»» file_type | string | false | none | 文件类型，image：图片，video：视频  
»» memo | string | false | none | 支付提示，仅首页展示  
»» has_history | boolean | false | none | 是否存在历史记录  
»» txid | integer | false | none | 订单号  
»» SRVTM | integer | false | none | 最新一条消息的时间戳  
»» order_status | string | false | none | 订单数据库状态，常见值：OPEN、PAID、LOCKED、ACCEPT、BCLOSED、CANCEL、BECANCEL、SCLOSED、SCANCEL  
» version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "messages": [
          {}
        ],
        "memo": "string",
        "has_history": true,
        "txid": 0,
        "SRVTM": 0,
        "order_status": "string"
      },
      "version": "string"
    }
    
    

##  P2pAdsListResponse

_P2pAdsListResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | array | false | none | none  
» P2pAdsListItem | object | false | none | none  
»» index | integer | false | none | 序号  
»» asset | string | false | none | 加密货币  
»» fiat_unit | string | false | none | 法币  
»» adv_no | integer | false | none | 广告id  
»» price | string | false | none | 价格  
»» max_single_trans_amount | string | false | none | 单笔最大加密币交易数量  
»» min_single_trans_amount | string | false | none | 单笔最小加密币交易数量  
»» nick_name | string | false | none | 广告商昵称  
» version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": [
        {
          "index": 0,
          "asset": "string",
          "fiat_unit": "string",
          "adv_no": 0,
          "price": "string",
          "max_single_trans_amount": "string",
          "min_single_trans_amount": "string",
          "nick_name": "string"
        }
      ],
      "version": "string"
    }
    
    

##  GetPendingTransactionListRequest

_获取进行中订单请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
crypto_currency | string | true | none | 加密币币种  
fiat_currency | string | true | none | 法币币种  
order_tab | string | false | none | 订单标签页，pending：处理中订单（OPEN、PAID、LOCKED、TEMP），dispute：申诉中订单；默认 pending  
select_type | string | false | none | 订单方向筛选，buy：买单，sell：卖单，空字符串或不传：全部  
status | string | false | none | 订单状态筛选。open：未付款（OPEN）；paid：已付款（PAID）；locked：已锁定（LOCKED）；  
dispute：申诉中；空字符串或不传时按 order_tab 的默认状态范围查询。  
txid | integer | false | none | 订单号  
start_time | integer | false | none | 开始时间时间戳，默认89天前0点  
end_time | integer | false | none | 结束时间时间戳，默认今天23:59:59  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
order_tab | pending  
order_tab | dispute  
      
    
    {
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "order_tab": "pending",
      "select_type": "sell",
      "status": "open",
      "txid": 40000001,
      "start_time": 1764547200,
      "end_time": 1767139199
    }
    
    

##  P2pMyAdsListResponse

_P2pMyAdsListResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» lists | array | false | none | none  
»» P2pMyAd | object | false | none | none  
»»» type | string | false | none | 广告方向，buy：买币广告，sell：卖币广告  
»»» rate | string | false | none | 价格  
»»» original_rate | string | false | none | 原始价格  
»»» amount | string | false | none | 广告剩余加密币数量  
»»» total | string | false | none | 广告剩余法币金额  
»»» limit_total | string | false | none | 单笔限额范围-数字币  
»»» limit_fiat | string | false | none | 单笔限额范围-法币  
»»» min_amount | string | false | none | 单笔最小数量  
»»» max_amount | string | false | none | 单笔最大数量  
»»» pay_type_num | string | false | none | 支付方式 Id 列表  
»»» pay_type_json | string | false | none | 支付方式配置详情，JSON 字符串，key 为支付方式类型，value 为支付方式 ID  
»»» expire_min | string | false | none | 广告过期时间(分钟)  
»»» tier_limit | string | false | none | VIP 限制  
»»» advertisers_limit | integer | false | none | 是否限制与广告商交易，0：不限制，1：限制  
»»» reg_time_limit | integer | false | none | 注册时间限制  
»»» verified_limit | integer | false | none | KYC 等级限制  
»»» min_completed_limit | integer | false | none | 交易对手已完成的订单数最小值限制  
»»» max_completed_limit | integer | false | none | 交易对手已完成的订单数最大值限制  
»»» user_country_limit | integer | false | none | KYC国籍限制  
»»» completed_rate_limit | number | false | none | 30天完成率限制  
»»» user_orders_limit | integer | false | none | 交易对方最大下单数限制  
»»» hide_payment | string | false | none | 是否隐藏支付方式，1：隐藏，0：不隐藏  
»»» currencyType | string | false | none | 加密币币种  
»»» want_type | string | false | none | 法币  
»»» trade_tips | string | false | none | 交易条款  
»»» new_hand | integer | false | none | 特殊广告类型，0：普通单，1：新手引导单，2：新手折扣单，3：精选特惠单，4：KOL 广告单，5：卡券广告单  
»»» id | string | false | none | 广告 ID  
»»» status | string | false | none | 广告状态，OPEN：上架，OFFLIN：下架，CLOSED：关闭，CANCEL：取消  
»»» locked_amount | string | false | none | 广告冻结金额  
»»» hide_rate | string | false | none | 隐藏价格  
»»» is_out_time | integer | false | none | 广告当前是否超时，1：已超时，0：未超时  
»»» rate_ref_id | integer | false | none | 浮动价参考基准，1：平台参考价，2：Gate 参考价，3：现货参考价；小于等于 0 表示固定价格  
»»» rate_offset | string | false | none | 浮动比例  
»»» rate_fixed | integer | false | none | 价格类型，0：浮动价格，1：固定价格  
»»» float_trend | integer | false | none | 浮动价方向，0：上浮，1：下浮  
»»» in_dispute | integer | false | none | 广告是否存在申诉交易，1：存在，0：不存在  
»»» auto_reply | string | false | none | 自动回复数据  
»»» timestamp | integer | false | none | 广告创建时间  
»»» is_hedge | integer | false | none | 是否自动委托，1：是，0：否  
»» version | string | false | none | 版本号  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "lists": [
          {}
        ]
      },
      "version": "string"
    }
    
    

##  GetCounterpartyUserInfoRequest

_获取对手方用户信息请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
biz_uid | string | true | none | 对手方加密 UID，可从订单列表 its_uid 或订单详情 its_uid 获取  
      
    
    {
      "biz_uid": "biz_uid_demo_9f3a7c"
    }
    
    

##  ConfirmPayment

_确认付款请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
txid | string | true | none | 订单号  
payment_method | string | false | none | 本次付款使用的支付方式类型；可选，传入时必须是订单支持的支付方式。可从订单详情 supported_pay_types 或支付方式列表 pay_type 获取，例如 bank、alipay、wechat、paypal、swift、wu  
      
    
    {
      "txid": "40000001",
      "payment_method": "bank"
    }
    
    

##  AdsDetailRequest

_获取广告详情请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
adv_no | string | true | none | 广告 ID  
      
    
    {
      "adv_no": "2124000001"
    }
    
    

##  PlaceBizPushOrder

_发布广告挂单请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currencyType | string | true | none | 加密币币种  
exchangeType | string | true | none | 法币币种  
type | string | true | none | 广告操作类型，0：发布卖币广告，1：发布买币广告，2：编辑卖币广告，3：编辑买币广告  
unitPrice | string | true | none | 固定价格模式下的广告单价  
number | string | true | none | 广告数量，按 currencyType 计价  
payType | string | true | none | 支付方式类型，多个类型用逗号分隔；可从支付方式列表 pay_type 获取，例如 bank、alipay、wechat、paypal、swift、wu  
pay_type_json | string | false | none | 支付方式和支付方式 ID 的 JSON 字符串，key 为支付方式类型，value 为当前用户支付方式 ID  
rateFixed | string | false | none | 价格类型，0：浮动价格，1：固定价格  
oid | string | false | none | 编辑广告时传广告 ID；发布新广告时不传或传空字符串  
minAmount | string | true | none | 单笔最小交易金额，按 exchangeType 计价  
maxAmount | string | true | none | 单笔最大交易金额，按 exchangeType 计价  
tierLimit | string | false | none | 交易对手 VIP 等级限制，0 表示不限制  
verifiedLimit | string | false | none | 交易对手认证等级限制，0 表示不限制  
regTimeLimit | string | false | none | 交易对手注册天数限制，0 表示不限制  
advertisersLimit | string | false | none | 是否限制与广告商交易，0：不限制，1：限制  
expire_min | string | false | none | 订单付款超时时间，单位分钟  
trade_tips | string | false | none | 广告交易条款，展示给下单用户  
auto_reply | string | false | none | 订单创建后的自动回复内容  
min_completed_limit | string | false | none | 交易对手已完成订单数最小值限制，-1 表示不限制  
max_completed_limit | string | false | none | 交易对手已完成订单数最大值限制，-1 表示不限制  
completed_rate_limit | string | false | none | 交易对手近 30 天完成率限制，-1 表示不限制  
user_country_limit | string | false | none | KYC 国籍限制，-1 表示不限制  
user_order_limit | string | false | none | 交易对手最大下单数限制，-1 表示不限制  
rateReferenceId | string | false | none | 浮动价参考基准，1：平台参考价，2：Gate 参考价，3：现货参考价  
rateOffset | string | false | none | 浮动价偏移比例的绝对值，例如 0.5 表示 0.5%  
float_trend | string | false | none | 浮动价方向，0：上浮，1：下浮  
team_payment_uid | string | false | none | 团队收款人 UID；非团队商家可不传  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | 0  
type | 1  
type | 2  
type | 3  
      
    
    {
      "currencyType": "USDT",
      "exchangeType": "USD",
      "type": "0",
      "unitPrice": "1.1",
      "number": "100",
      "payType": "bank",
      "pay_type_json": "{\"bank\":\"10001\",\"swift\":\"10002\"}",
      "rateFixed": "1",
      "oid": "2124000001",
      "minAmount": "10",
      "maxAmount": "500",
      "tierLimit": "0",
      "verifiedLimit": "0",
      "regTimeLimit": "0",
      "advertisersLimit": "0",
      "expire_min": "20",
      "trade_tips": "Please pay from an account under your own name",
      "auto_reply": "Please tap Paid after completing the transfer",
      "min_completed_limit": "-1",
      "max_completed_limit": "-1",
      "completed_rate_limit": "-1",
      "user_country_limit": "-1",
      "user_order_limit": "-1",
      "rateReferenceId": "3",
      "rateOffset": "0.5",
      "float_trend": "0",
      "team_payment_uid": "1000001"
    }
    
    

##  GetMyselfPaymentRequest

_获取支付方式列表请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
fiat | string | false | none | 法币币种。不传时返回全部可用支付方式  
      
    
    {
      "fiat": "USD"
    }
    
    

##  P2pUploadChatFileResponse

_P2pUploadChatFileResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» file_key | string | false | none | 文件key  
version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "file_key": "string"
      },
      "version": "string"
    }
    
    

##  P2pSendChatMessageResponse

_P2pSendChatMessageResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» SRVTM | integer | false | none | 成功发送消息的时间（当前时间戳）  
version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "SRVTM": 0
      },
      "version": "string"
    }
    
    

##  P2pTransactionListResponse

_P2pTransactionListResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» list | array | false | none | none  
»» P2pTransactionListItem | object | false | none | none  
»»» type_buy | integer | false | none | 当前用户视角的订单方向，1：买单，0：卖单  
»»» timest | string | false | none | 订单创建时间  
»»» timest_expire | string | false | none | 订单过期时间  
»»» timestamp | integer | false | none | 订单创建时间戳  
»»» rate | string | false | none | 订单价格，按法币计价  
»»» amount | string | false | none | 订单加密币数量  
»»» total | string | false | none | 订单法币总金额  
»»» txid | integer | false | none | 订单号  
»»» status | string | false | none | 订单展示状态，unpay：待付款，paid：买家已付款，unconfirmed：待卖家确认收款，locked：已锁定，finished：已完成，cancel：已取消，expired：已过期，bclosed：仲裁成交，sclosed：仲裁取消  
»»» its_realname | string | false | none | 交易对手真实姓名或实名展示名  
»»» its_uid | string | false | none | 交易对手加密 UID  
»»» its_nick | string | false | none | 交易对手昵称  
»»» seller_realname | string | false | none | 卖家真实姓名或实名展示名  
»»» buyer_realname | string | false | none | 买家真实姓名或实名展示名  
»»» cancelable | integer | false | none | 是否可取消订单，1：可取消，0：不可取消  
»»» currency_type | string | false | none | 加密币币种  
»»» want_type | string | false | none | 法币币种  
»»» hide_payment | integer | false | none | 是否隐藏支付方式，1：隐藏，0：不隐藏  
»»» sel_paytype | string | false | none | 当前订单选择的支付方式类型，例如 bank、alipay、wechat、paypal、swift、wu  
»»» pay_others | array | false | none | 其他支付方式信息，历史订单可能返回  
»»»» pay_type | string | false | none | 支付方式类型  
»»»» pay_name | string | false | none | 支付方式名称  
»»» cd_time | integer | false | none | 当前订单倒计时秒数  
»»» order_type | integer | false | none | 订单类型，1：普通订单，2：三方合作订单，3：闪兑订单，4：Web3 订单  
»»» order_tag | array | false | none | 订单标签  
»»» convert_info | object | false | none | 闪兑订单信息  
»»»» convert_type | string | false | none | 闪兑目标币种  
»»»» convert_status | string | false | none | 闪兑订单状态  
»»»» pre_rate | string | false | none | 下单时预期价格  
»»»» rate | string | false | none | 成交时价格  
»»»» pre_fiat_rate | string | false | none | 下单时法币预期价格  
»»»» fiat_rate | string | false | none | 成交时法币价格  
»»»» amount | string | false | none | 数量  
»»»» convert_amount | string | false | none | 兑换数量  
»»»» slippage | string | false | none | 滑点计算，滑点 =（下单预期价格-自动兑换时实时价格）/ 下单预期价格  
»»»» status | string | false | none | 闪兑订单展示状态  
»»» trans_time | array | false | none | 倒计时时间  
»»»» P2pTransactionTimeMarker | object | false | none | none  
»»»»» od_time | integer | false | none | none  
»»»» count | integer | false | none | 订单数  
»»»» exported_num | integer | false | none | 导出次数  
»»» version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "trans_time": [
          {}
        ],
        "count": 0,
        "exported_num": 0
      },
      "version": "string"
    }
    
    

##  ConfirmReceipt

_确认收款请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
txid | string | true | none | 订单号  
      
    
    {
      "txid": "40000001"
    }
    
    

##  P2pCounterpartyUserInfoResponse

_P2pCounterpartyUserInfoResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» user_timest | string | false | none | 用户注册时间，格式化字符串  
» email_verified | string | false | none | 是否验证过邮箱，1：已验证，0：未验证  
» verified | string | false | none | 是否完成 KYC，1：已完成，0：未完成  
» has_phone | string | false | none | 是否绑定过手机，1：已绑定，0：未绑定  
» user_name | string | false | none | 用户名  
» user_note | string | false | none | 用户备注信息  
» complete_transactions | string | false | none | 总完成订单数  
» paid_transactions | string | false | none | 已完成买单订单数量  
» accepted_transactions | string | false | none | 已完成卖单订单数量  
» transactions_used_time | string | false | none | 确认收款平均用时  
» cancelled_used_time_month | string | false | none | 近30天取消用时  
» complete_transactions_month | string | false | none | 近30天完成订单数量  
» complete_rate_month | number | false | none | 近30天完成率  
» is_follow | integer | false | none | 是否已关注该用户，1：是，0：否  
» have_traded | integer | false | none | 是否与本人交易过，1：是，0：否  
» biz_uid | string | false | none | 加密uid  
» registration_days | integer | false | none | 注册天数  
» first_trade_days | integer | false | none | 首次交易到现在的天数  
» trade_versatile | boolean | false | none | 单一用户还是复合用户  
version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "user_timest": "string",
        "email_verified": "string",
        "verified": "string",
        "has_phone": "string",
        "user_name": "string",
        "user_note": "string",
        "complete_transactions": "string",
        "paid_transactions": "string",
        "accepted_transactions": "string",
        "transactions_used_time": "string",
        "cancelled_used_time_month": "string",
        "complete_transactions_month": "string",
        "complete_rate_month": 0,
        "is_follow": 0,
        "have_traded": 0,
        "biz_uid": "string",
        "registration_days": 0,
        "first_trade_days": 0,
        "trade_versatile": true
      },
      "version": "string"
    }
    
    

##  AdsListRequest

_获取市场广告列表请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
asset | string | true | none | 加密币币种  
fiat_unit | string | true | none | 法币币种  
trade_type | string | true | none | 广告方向，buy 表示买币广告，sell 表示卖币广告  
      
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    
    

##  P2pMerchantUserInfoResponse

_P2pMerchantUserInfoResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | object | false | none | none  
» is_self | boolean | false | none | 是否本人  
» user_timest | string | false | none | 用户注册时间，格式化字符串  
» counterparties_num | integer | false | none | 交易对手数  
» email_verified | string | false | none | 是否验证过邮箱，1：已验证，0：未验证  
» verified | string | false | none | 是否完成 KYC，1：已完成，0：未完成  
» has_phone | string | false | none | 是否绑定过手机，1：已绑定，0：未绑定  
» user_name | string | false | none | 用户名  
» user_note | string | false | none | 用户备注信息  
» complete_transactions | string | false | none | 总完成订单数  
» paid_transactions | string | false | none | 已完成买单订单数量  
» accepted_transactions | string | false | none | 已完成卖单订单数量  
» transactions_used_time | string | false | none | 确认收款平均用时  
» cancelled_used_time_month | string | false | none | 近30天取消用时  
» complete_transactions_month | string | false | none | 近30天完成订单数量  
» complete_rate_month | number | false | none | 近30天完成率  
» orders_buy_rate_month | number | false | none | 近30天买单占比  
» is_black | integer | false | none | 是否已拉黑该用户，1：是，0：否  
» is_follow | integer | false | none | 是否已关注该用户，1：是，0：否  
» have_traded | integer | false | none | 是否与本人交易过，1：是，0：否  
» biz_uid | string | false | none | 加密uid  
» blue_vip | integer | false | none | 蓝V皇冠神盾  
» work_status | integer | false | none | 商家工作状态  
» registration_days | integer | false | none | 注册天数  
» first_trade_days | integer | false | none | 首次交易到现在的天数  
» need_replenish | integer | false | none | 是否需要补充保证金，1：需要，0：不需要  
» merchant_info | object | false | none | 用户可挂单的市场  
»» type | string | false | none | none  
»» market | string | false | none | none  
» online_status | integer | false | none | 商家在线状态，1：在线，0：离线  
» work_hours | object|null | false | none | 商家在线状态详情  
» transactions_month | number | false | none | 30天交易量  
» transactions_all | number | false | none | 总交易量  
» trade_versatile | boolean | false | none | 单一用户还是复合用户  
version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "is_self": true,
        "user_timest": "string",
        "counterparties_num": 0,
        "email_verified": "string",
        "verified": "string",
        "has_phone": "string",
        "user_name": "string",
        "user_note": "string",
        "complete_transactions": "string",
        "paid_transactions": "string",
        "accepted_transactions": "string",
        "transactions_used_time": "string",
        "cancelled_used_time_month": "string",
        "complete_transactions_month": "string",
        "complete_rate_month": 0,
        "orders_buy_rate_month": 0,
        "is_black": 0,
        "is_follow": 0,
        "have_traded": 0,
        "biz_uid": "string",
        "blue_vip": 0,
        "work_status": 0,
        "registration_days": 0,
        "first_trade_days": 0,
        "need_replenish": 0,
        "merchant_info": {
          "type": "string",
          "market": "string"
        },
        "online_status": 0,
        "work_hours": {},
        "transactions_month": 0,
        "transactions_all": 0,
        "trade_versatile": true
      },
      "version": "string"
    }
    
    

##  AdsUpdateStatus

_广告单状态更新请求_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
adv_no | integer | true | none | 广告 ID  
adv_status | integer | true | none | 广告状态，1：上架，3：下架，4：关闭  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
adv_status | 1  
adv_status | 3  
adv_status | 4  
      
    
    {
      "adv_no": 2124000001,
      "adv_status": 3
    }
    
    

##  P2pPaymentMethodsResponse

_P2pPaymentMethodsResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | number | false | none | none  
method | string | false | none | none  
code | integer | false | none | none  
message | string | false | none | none  
data | array | false | none | none  
» P2pPaymentMethodGroup | object | false | none | none  
»» pay_type | string | false | none | 支付方式类型  
»» pay_name | string | false | none | 支付方式名称  
»» ids | array | false | none | 用户当前绑定的支付方式，主键id  
»» list | array | false | none | none  
»»» P2pPaymentMethodAccount | object | false | none | none  
»»»» uid | integer | false | none | 用户uid  
»»»» bankid | string | false | none | 用户当前绑定的支付方式，主键id  
»»»» nickname | integer | false | none | 持卡人uid  
»»»» bankname | string | false | none | 银行名称  
»»»» bankbranch | string | false | none | 银行支行名  
»»»» bankcity | string | false | none | 银行所在城市  
»»»» bankprov | string | false | none | 银行所在省  
»»»» bankaddr | string | false | none | 银行卡号或脱敏银行卡号  
»»»» bankdesc | string | false | none | 银行备注  
»»»» hold_uid | integer | false | none | 持卡人uid  
»»»» hold_username | string | false | none | 持卡人名称  
»»»» real_name | string | false | none | 用户实名展示名  
»»»» id | string | false | none | 用户当前绑定的支付方式，主键id  
»»»» account_des | string | false | none | 支付方式描述  
»»»» pay_type | string | false | none | 支付方式类型  
»»»» file | string | false | none | 支付方式文件链接  
»»»» file_key | string | false | none | 支付方式文件key  
»»»» account | string | false | none | 支付账号或脱敏支付账号  
»»»» memo | string | false | none | 支付方式备注  
»»»» code | string | false | none | 支付方式code  
»»»» memo_ext | string | false | none | 支付方式额外备注  
»»»» trade_tips | string | false | none | 支付方式交易信息  
»»» version | string | false | none | none  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": [
        {
          "pay_type": "string",
          "pay_name": "string",
          "ids": [],
          "list": []
        }
      ],
      "version": "string"
    }