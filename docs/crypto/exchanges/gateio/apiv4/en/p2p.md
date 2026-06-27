---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/p2p
api_type: REST
updated_at: 2026-05-27 20:15:43.657497
---

# P2p

P2P trading

##  Get account information🔒 Authenticated

POST`/p2p/merchant/account/get_user_info`

POST `/p2p/merchant/account/get_user_info`

Get `account information`

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMerchantUserInfoResponse  
  
### Response Schema

Status Code **200**

_P2pMerchantUserInfoResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» is_self | boolean | Whether self  
»» user_timest | string | User registration time (formatted string)  
»» counterparties_num | integer | Number of counterparties  
»» email_verified | string | Whether email is verified. `1`: yes; `0`: no.  
»» verified | string | Whether KYC is completed. `1`: yes; `0`: no.  
»» has_phone | string | Whether a phone number is bound. `1`: yes; `0`: no.  
»» user_name | string | Username  
»» user_note | string | User note information  
»» complete_transactions | string | Total completed orders  
»» paid_transactions | string | Number of completed buy orders  
»» accepted_transactions | string | Number of completed sell orders  
»» transactions_used_time | string | Average time to confirm receipt  
»» cancelled_used_time_month | string | Cancellation time in last 30 days  
»» complete_transactions_month | string | Number of completed orders in last 30 days  
»» complete_rate_month | number | Completion rate in last 30 days  
»» orders_buy_rate_month | number | Buy order ratio in last 30 days  
»» is_black | integer | Whether the user is blocked. `1`: yes; `0`: no.  
»» is_follow | integer | Whether you follow this user. `1`: yes; `0`: no.  
»» have_traded | integer | Whether you have traded with this user before. `1`: yes; `0`: no.  
»» biz_uid | string | Encrypted UID  
»» blue_vip | integer | Blue V Crown Shield  
»» work_status | integer | Merchant work status  
»» registration_days | integer | Registration days  
»» first_trade_days | integer | Days since first trade  
»» need_replenish | integer | Whether additional margin is required. `1`: yes; `0`: no.  
»» merchant_info | object | Markets where user can place orders  
»»» type | string | none  
»»» market | string | none  
»» online_status | integer | Merchant online status: `1` online; `0` offline.  
»» work_hours | object|null | Merchant online status details  
»» transactions_month | number | 30-day transaction volume  
»» transactions_all | number | Total transaction volume  
»» trade_versatile | boolean | Single user or composite user  
» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Get counterparty information🔒 Authenticated

POST`/p2p/merchant/account/get_counterparty_user_info`

POST `/p2p/merchant/account/get_counterparty_user_info`

Get `counterparty information`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetCounterpartyUserInfoRequest | Required | none  
↳ biz_uid | body | string | Required | Counterparty crypto UID from order list or detail field `its_uid`.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pCounterpartyUserInfoResponse  
  
### Response Schema

Status Code **200**

_P2pCounterpartyUserInfoResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» user_timest | string | User registration time (formatted string)  
»» email_verified | string | Whether email is verified. `1`: yes; `0`: no.  
»» verified | string | Whether KYC is completed. `1`: yes; `0`: no.  
»» has_phone | string | Whether a phone number is bound. `1`: yes; `0`: no.  
»» user_name | string | Username  
»» user_note | string | User note information  
»» complete_transactions | string | Total completed orders  
»» paid_transactions | string | Number of completed buy orders  
»» accepted_transactions | string | Number of completed sell orders  
»» transactions_used_time | string | Average time to confirm receipt  
»» cancelled_used_time_month | string | Cancellation time in last 30 days  
»» complete_transactions_month | string | Number of completed orders in last 30 days  
»» complete_rate_month | number | Completion rate in last 30 days  
»» is_follow | integer | Whether you follow this user. `1`: yes; `0`: no.  
»» have_traded | integer | Whether you have traded with this user before. `1`: yes; `0`: no.  
»» biz_uid | string | Encrypted UID  
»» registration_days | integer | Registration days  
»» first_trade_days | integer | Days since first trade  
»» trade_versatile | boolean | Single user or composite user  
» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "biz_uid": "biz_uid_demo_9f3a7c"
    }
    

> Example responses

> 200 Response
    
    
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
    

##  Get payment method list🔒 Authenticated

POST`/p2p/merchant/account/get_myself_payment`

POST `/p2p/merchant/account/get_myself_payment`

Get `payment method list`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetMyselfPaymentRequest | Optional | none  
↳ fiat | body | string | Optional | Fiat currency; omit to return all available payment methods.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pPaymentMethodsResponse  
  
### Response Schema

Status Code **200**

_P2pPaymentMethodsResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | array | none  
»» P2pPaymentMethodGroup | object | none  
»»» pay_type | string | Payment method type  
»»» pay_name | string | Payment method name  
»»» ids | array | User's currently bound payment method (primary key ID)  
»»» list | array | none  
»»»» P2pPaymentMethodAccount | object | none  
»»»»» uid | integer | useruID  
»»»»» bankid | string | User's currently bound payment method (primary key ID)  
»»»»» nickname | integer | Cardholder UID  
»»»»» bankname | string | Bank name  
»»»»» bankbranch | string | Bank branch name  
»»»»» bankcity | string | Bank city  
»»»»» bankprov | string | Bank province  
»»»»» bankaddr | string | Bank card number or masked card number.  
»»»»» bankdesc | string | Bank note  
»»»»» hold_uid | integer | Cardholder UID  
»»»»» hold_username | string | Cardholder name  
»»»»» real_name | string | User verified display name.  
»»»»» id | string | User's currently bound payment method (primary key ID)  
»»»»» account_des | string | Payment method description  
»»»»» pay_type | string | Payment method type  
»»»»» file | string | Payment method file link  
»»»»» file_key | string | Payment method file key  
»»»»» account | string | Payment account or masked payment account.  
»»»»» memo | string | Payment method note  
»»»»» code | string | Payment method code  
»»»»» memo_ext | string | Payment method additional note  
»»»»» trade_tips | string | Payment method transaction information  
»»»» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "fiat": "USD"
    }
    

> Example responses

> 200 Response
    
    
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
    

##  Get pending orders🔒 Authenticated

POST`/p2p/merchant/transaction/get_pending_transaction_list`

POST `/p2p/merchant/transaction/get_pending_transaction_list`

Get `pending orders`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetPendingTransactionListRequest | Required | none  
↳ crypto_currency | body | string | Required | Cryptocurrency symbol.  
↳ fiat_currency | body | string | Required | Fiat currency  
↳ order_tab | body | string | Optional | Order tab: `pending` in progress (`OPEN`, `PAID`, `LOCKED`, `TEMP`); `dispute` in dispute; default `pending`.  
↳ select_type | body | string | Optional | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
↳ status | body | string | Optional | Order status filter. `open` unpaid (`OPEN`); `paid` paid (`PAID`); `locked` locked (`LOCKED`);  
`dispute` in dispute; empty or omitted uses the default range for `order_tab`.  
↳ txid | body | integer | Optional | Order ID  
↳ start_time | body | integer | Optional | Start timestamp, default is 00:00 89 days ago  
↳ end_time | body | integer | Optional | End timestamp, default is 23:59:59 today  
  
####  Detailed descriptions

**» status** : Order status filter. `open` unpaid (`OPEN`); `paid` paid (`PAID`); `locked` locked (`LOCKED`);  
`dispute` in dispute; empty or omitted uses the default range for `order_tab`.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» order_tab | pending  
» order_tab | dispute  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionListResponse  
  
### Response Schema

Status Code **200**

_P2pTransactionListResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» list | array | none  
»»» P2pTransactionListItem | object | none  
»»»» type_buy | integer | Order side from current user's view. `1`: buy; `0`: sell.  
»»»» timest | string | Creation time of order  
»»»» timest_expire | string | Order expiration time  
»»»» timestamp | integer | Order creation timestamp  
»»»» rate | string | Order price in fiat currency.  
»»»» amount | string | Order size in cryptocurrency.  
»»»» total | string | Total fiat amount of the order.  
»»»» txid | integer | Order ID  
»»»» status | string | Display status: `unpay` awaiting payment; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` completed; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
»»»» its_realname | string | Counterparty real name or verified display name.  
»»»» its_uid | string | Counterparty crypto UID.  
»»»» its_nick | string | Counterparty nickname  
»»»» seller_realname | string | Seller real name or verified display name.  
»»»» buyer_realname | string | Buyer real name or verified display name.  
»»»» cancelable | integer | Whether the order can be canceled. `1`: yes; `0`: no.  
»»»» currency_type | string | Cryptocurrency symbol.  
»»»» want_type | string | Fiat currency  
»»»» hide_payment | integer | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
»»»» sel_paytype | string | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
»»»» pay_others | array | Other payment method details; may appear on historical orders.  
»»»»» pay_type | string | Payment method type  
»»»»» pay_name | string | Payment method name  
»»»» cd_time | integer | Countdown seconds for the current order.  
»»»» order_type | integer | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
»»»» order_tag | array | Order tags  
»»»» convert_info | object | Flash swap order information  
»»»»» convert_type | string | Flash swap target currency  
»»»»» convert_status | string | Flash swap order status  
»»»»» pre_rate | string | Expected price when placing order  
»»»»» rate | string | Execution price  
»»»»» pre_fiat_rate | string | Expected fiat price when placing order  
»»»»» fiat_rate | string | Fiat price at execution  
»»»»» amount | string | Size  
»»»»» convert_amount | string | Swap Amount  
»»»»» slippage | string | Slippage calculation: slippage = (expected price when placing order - real-time price during auto swap) / expected price when placing order  
»»»»» status | string | Flash swap order display status  
»»»» trans_time | array | Countdown time  
»»»»» P2pTransactionTimeMarker | object | none  
»»»»»» od_time | integer | none  
»»»»» count | integer | Number of orders  
»»»»» exported_num | integer | Export count  
»»»» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
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
    

> Example responses

> 200 Response
    
    
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
    

##  Get all/historical orders🔒 Authenticated

POST`/p2p/merchant/transaction/get_completed_transaction_list`

POST `/p2p/merchant/transaction/get_completed_transaction_list`

Get `all/historical orders`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetCompletedTransactionListRequest | Required | none  
↳ crypto_currency | body | string | Required | Cryptocurrency symbol.  
↳ fiat_currency | body | string | Required | Fiat currency  
↳ select_type | body | string | Optional | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
↳ status | body | string | Optional | Order status filter. `closed`: filled (`ACCEPT`, `BCLOSED`); `cancel`: canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`);  
`locked`: locked (`LOCKED`); `open`: unpaid (`OPEN`); `paid`: paid (`PAID`);  
`completed`: finished or canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`, `ACCEPT`, `BCLOSED`);  
Empty or omitted uses the endpoint default range.  
↳ txid | body | integer | Optional | Order ID  
↳ start_time | body | integer | Optional | Start timestamp, default is 00:00 89 days ago  
↳ end_time | body | integer | Optional | End timestamp, default is 23:59:59 today  
↳ query_dispute | body | integer | Optional | Whether to flag dispute status in the response. `1`: yes; `0`: no.  
↳ page | body | integer | Optional | Page number starting at 1; values below 1 are treated as 1.  
↳ per_page | body | integer | Optional | Orders per page; default 10, max 200.  
  
####  Detailed descriptions

**» status** : Order status filter. `closed`: filled (`ACCEPT`, `BCLOSED`); `cancel`: canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`);  
`locked`: locked (`LOCKED`); `open`: unpaid (`OPEN`); `paid`: paid (`PAID`);  
`completed`: finished or canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`, `ACCEPT`, `BCLOSED`);  
Empty or omitted uses the endpoint default range.

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionListResponse  
  
### Response Schema

Status Code **200**

_P2pTransactionListResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» list | array | none  
»»» P2pTransactionListItem | object | none  
»»»» type_buy | integer | Order side from current user's view. `1`: buy; `0`: sell.  
»»»» timest | string | Creation time of order  
»»»» timest_expire | string | Order expiration time  
»»»» timestamp | integer | Order creation timestamp  
»»»» rate | string | Order price in fiat currency.  
»»»» amount | string | Order size in cryptocurrency.  
»»»» total | string | Total fiat amount of the order.  
»»»» txid | integer | Order ID  
»»»» status | string | Display status: `unpay` awaiting payment; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` completed; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
»»»» its_realname | string | Counterparty real name or verified display name.  
»»»» its_uid | string | Counterparty crypto UID.  
»»»» its_nick | string | Counterparty nickname  
»»»» seller_realname | string | Seller real name or verified display name.  
»»»» buyer_realname | string | Buyer real name or verified display name.  
»»»» cancelable | integer | Whether the order can be canceled. `1`: yes; `0`: no.  
»»»» currency_type | string | Cryptocurrency symbol.  
»»»» want_type | string | Fiat currency  
»»»» hide_payment | integer | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
»»»» sel_paytype | string | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
»»»» pay_others | array | Other payment method details; may appear on historical orders.  
»»»»» pay_type | string | Payment method type  
»»»»» pay_name | string | Payment method name  
»»»» cd_time | integer | Countdown seconds for the current order.  
»»»» order_type | integer | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
»»»» order_tag | array | Order tags  
»»»» convert_info | object | Flash swap order information  
»»»»» convert_type | string | Flash swap target currency  
»»»»» convert_status | string | Flash swap order status  
»»»»» pre_rate | string | Expected price when placing order  
»»»»» rate | string | Execution price  
»»»»» pre_fiat_rate | string | Expected fiat price when placing order  
»»»»» fiat_rate | string | Fiat price at execution  
»»»»» amount | string | Size  
»»»»» convert_amount | string | Swap Amount  
»»»»» slippage | string | Slippage calculation: slippage = (expected price when placing order - real-time price during auto swap) / expected price when placing order  
»»»»» status | string | Flash swap order display status  
»»»» trans_time | array | Countdown time  
»»»»» P2pTransactionTimeMarker | object | none  
»»»»»» od_time | integer | none  
»»»»» count | integer | Number of orders  
»»»»» exported_num | integer | Export count  
»»»» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
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
    

> Example responses

> 200 Response
    
    
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
    

##  Query order details🔒 Authenticated

POST`/p2p/merchant/transaction/get_transaction_details`

POST `/p2p/merchant/transaction/get_transaction_details`

_Query order details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetTransactionDetailsRequest | Required | none  
↳ txid | body | integer | Required | Order ID  
↳ channel | body | string | Optional | Channel tag: omit or empty for normal P2P; use `web3` for Web3 orders.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionDetailResponse  
  
### Response Schema

Status Code **200**

_P2pTransactionDetailResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» is_sell | integer | Whether the current user is the seller. `1`: yes; `0`: no.  
»» txid | integer | Order ID  
»» orderid | integer | Order ID  
»» timest | integer | Order creation timestamp  
»» last_pay_time | integer | Payment deadline  
»» remain_pay_time | integer | Seconds left to pay; `<= 0` means overdue.  
»» currency_type | string | Cryptocurrency symbol.  
»» want_type | string | Fiat currency  
»» symbol | string | Fiat currency symbol  
»» rate | string | Order price in `want_type` units.  
»» amount | string | Order size in cryptocurrency.  
»» total | string | Total fiat amount of the order.  
»» status | string | Display status: `unpay` unpaid; `hide_payment` unpaid with payment info hidden; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` done; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
»» reason_id | string | Cancel reason ID; empty string means none. Examples: `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller did not provide a real account; `6` price/amount mismatch; `9` other; `10` seller cannot release and refund issued; `11` terms not met; `12` seller payout account risk-controlled.  
»» reason_desc | string | Cancel reason description.  
»» cancel_time | string | Cancellation time  
»» in_appeal | integer | Whether a dispute is active. `1`: yes; `0`: no.  
»» dispute_time | integer | Earliest timestamp when a dispute may be opened.  
»» cancelable | integer | Whether cancellation is allowed. `1`: yes; `0`: no.  
»» hide_payment | integer | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
»» trade_tips | string | Trading terms  
»» show_bank | string | Whether to show bank transfer details. `1`: show; `0`: hide.  
»» bankname | string | Bank name  
»» bankbranch | string | Bank branch name  
»» bankid | string | Bank account or masked account.  
»» bank_holder_realname | string | Bank cardholder name  
»» show_ali | string | Whether to show Alipay details. `1`: show; `0`: hide.  
»» aliname | string | Alipay account name  
»» is_alicode | integer | Whether an Alipay QR exists. `1`: yes; `0`: no.  
»» show_wechat | string | Whether to show WeChat details. `1`: show; `0`: hide.  
»» wename | string | WeChat account name  
»» show_others | string | Whether to show other payment methods. `1`: show; `0`: hide.  
»» pay_others | array | Other payment methods  
»»» id | string | Payment method record ID.  
»»» account_des | string | Payment method description  
»»» pay_type | string | Payment method type  
»»» account | string | Payment account or masked account.  
»»» memo | string | Payment note or memo.  
»»» trade_tips | string | Payment instructions or tips.  
»»» pay_name | string | Display name of the payment method.  
»» sel_paytype | string | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
»» its_uid | string | Counterparty crypto UID.  
»» its_nickname | string | Counterparty nickname  
»» its_realname | string | Counterparty real name or verified display name.  
»» have_traded | integer | Whether you traded with the counterparty before. `1`: yes; `0`: no.  
»» appeal_allow_cancel | integer | Whether the dispute can be withdrawn. `1`: allowed; `0`: not allowed.  
»» appeal_verdict_has_open | string | Dispute outcome or in-dispute notice text.  
»» im_unread | integer | Unread chat message count.  
»» payment_voucher_url | array | Payment voucher  
»» timest_paid | integer | Timestamp when the buyer confirmed payment.  
»» own_realname | string | Current user's real name or verified display name.  
»» order_type | integer | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
»» is_show_receive | integer | Whether to show confirm-receipt during dispute. `1`: show; `0`: hide.  
»» show_seller_contact_info | boolean | Whether to display seller contact information  
»» supported_pay_types | array | Supported payment method types for the order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "txid": 40000001,
      "channel": ""
    }
    

> Example responses

> 200 Response
    
    
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
    

##  Confirm payment🔒 Authenticated

POST`/p2p/merchant/transaction/confirm-payment`

POST `/p2p/merchant/transaction/confirm-payment`

_Confirm payment_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | ConfirmPayment | Required | none  
↳ txid | body | string | Required | Order ID  
↳ payment_method | body | string | Optional | Payment type used for this payment; optional but must be among order-supported types. Use `supported_pay_types` on the order or `pay_type` list, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionActionResponse  
  
### Response Schema

Status Code **200**

_P2pTransactionActionResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | Response timestamp.  
» method | string | Placeholder for request method.  
» code | integer | Response code, 0 means success  
» message | string | Response message  
» data | object | Empty object on success.  
» version | string | API version.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "txid": "40000001",
      "payment_method": "bank"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  Confirm receipt🔒 Authenticated

POST`/p2p/merchant/transaction/confirm-receipt`

POST `/p2p/merchant/transaction/confirm-receipt`

_Confirm receipt_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | ConfirmReceipt | Required | none  
↳ txid | body | string | Required | Order ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionActionResponse  
  
### Response Schema

Status Code **200**

_P2pTransactionActionResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | Response timestamp.  
» method | string | Placeholder for request method.  
» code | integer | Response code, 0 means success  
» message | string | Response message  
» data | object | Empty object on success.  
» version | string | API version.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "txid": "40000001"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  Cancel order🔒 Authenticated

POST`/p2p/merchant/transaction/cancel`

POST `/p2p/merchant/transaction/cancel`

_Cancel order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CancelOrder | Required | none  
↳ txid | body | string | Required | Order ID  
↳ reason_id | body | string | Optional | Cancel reason ID. `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller account not real; `5` payout account issue; `6` price mismatch; `7` mutually agreed cancel; `8` poor communication; `9` other; `10` seller cannot release with refund; `11` terms not met; `12` seller payout risk-controlled.  
↳ reason_memo | body | string | Optional | Extra cancel notes when `reason_id` is `9` or explanation is required.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionActionResponse  
  
### Response Schema

Status Code **200**

_P2pTransactionActionResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | Response timestamp.  
» method | string | Placeholder for request method.  
» code | integer | Response code, 0 means success  
» message | string | Response message  
» data | object | Empty object on success.  
» version | string | API version.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "txid": "40000001",
      "reason_id": "1",
      "reason_memo": "Canceled after agreement with the counterparty"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  Publish ad order🔒 Authenticated

POST`/p2p/merchant/books/place_biz_push_order`

POST `/p2p/merchant/books/place_biz_push_order`

_Publish ad order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | PlaceBizPushOrder | Required | none  
↳ currencyType | body | string | Required | Cryptocurrency symbol.  
↳ exchangeType | body | string | Required | Fiat currency  
↳ type | body | string | Required | Ad operation type. `0`: publish sell ad; `1`: publish buy ad; `2`: edit sell ad; `3`: edit buy ad.  
↳ unitPrice | body | string | Required | Per-unit price in fixed-price mode.  
↳ number | body | string | Required | Ad amount priced in `currencyType`.  
↳ payType | body | string | Required | Payment types, comma-separated; from pay type list `pay_type`, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
↳ pay_type_json | body | string | Optional | JSON map of payment type -> user's payment method ID.  
↳ rateFixed | body | string | Optional | Price type: `0` floating; `1` fixed.  
↳ oid | body | string | Optional | Pass ad ID when editing; omit or empty when publishing a new ad.  
↳ minAmount | body | string | Required | Minimum trade amount in `exchangeType`.  
↳ maxAmount | body | string | Required | Maximum amount per trade in `exchangeType` fiat units.  
↳ tierLimit | body | string | Optional | Minimum counterparty VIP level; `0` means no requirement.  
↳ verifiedLimit | body | string | Optional | Minimum counterparty verification level; `0` means no limit.  
↳ regTimeLimit | body | string | Optional | Minimum counterparty account age in days; `0` means no limit.  
↳ advertisersLimit | body | string | Optional | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
↳ expire_min | body | string | Optional | Payment timeout in minutes.  
↳ trade_tips | body | string | Optional | Ad trading terms shown to the taker.  
↳ auto_reply | body | string | Optional | Auto-reply message after order creation.  
↳ min_completed_limit | body | string | Optional | Minimum completed orders for counterparty; `-1` unlimited.  
↳ max_completed_limit | body | string | Optional | Maximum completed orders for counterparty; `-1` unlimited.  
↳ completed_rate_limit | body | string | Optional | Counterparty minimum 30-day completion rate; `-1` means no limit.  
↳ user_country_limit | body | string | Optional | KYC nationality restriction; `-1` means no restriction.  
↳ user_order_limit | body | string | Optional | Maximum concurrent orders allowed for the counterparty. `-1`: unlimited.  
↳ rateReferenceId | body | string | Optional | Floating price reference. `1`: platform reference; `2`: Gate reference; `3`: spot reference.  
↳ rateOffset | body | string | Optional | Absolute floating offset ratio, e.g. `0.5` means 0.5%.  
↳ float_trend | body | string | Optional | Floating direction: `0` markup; `1` markdown.  
↳ team_payment_uid | body | string | Optional | Team payee UID; optional for non-team merchants.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» type | 0  
» type | 1  
» type | 2  
» type | 3  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMerchantBooksPlaceBizPushOrderResponse  
  
### Response Schema

Status Code **200**

_P2pMerchantBooksPlaceBizPushOrderResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | Response timestamp.  
» method | string | Placeholder for request method.  
» code | integer | Response code, 0 means success  
» message | string | Response message  
» data | object | Empty object on successful publish or edit.  
» version | string | API version.  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
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
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  Update ad status🔒 Authenticated

POST`/p2p/merchant/books/ads_update_status`

POST `/p2p/merchant/books/ads_update_status`

_Update ad status_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AdsUpdateStatus | Required | none  
↳ adv_no | body | integer | Required | Advertisement ID.  
↳ adv_status | body | integer | Required | Ad status. `1`: listed; `3`: delisted; `4`: closed.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» adv_status | 1  
» adv_status | 3  
» adv_status | 4  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pAdsUpdateStatusResponse  
  
### Response Schema

Status Code **200**

_P2pAdsUpdateStatusResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» status | integer | Ad status after update: `1` listed; `3` delisted; `4` closed.  
» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "adv_no": 2124000001,
      "adv_status": 3
    }
    

> Example responses

> 200 Response
    
    
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
    

##  Query ad details🔒 Authenticated

POST`/p2p/merchant/books/ads_detail`

POST `/p2p/merchant/books/ads_detail`

_Query ad details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AdsDetailRequest | Required | none  
↳ adv_no | body | string | Required | Advertisement ID.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pAdDetailResponse  
  
### Response Schema

Status Code **200**

_P2pAdDetailResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» rate | string | Advertisement price.  
»» type | string | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
»» amount | string | Remaining crypto amount on the ad.  
»» min_amount | string | Minimum trade amount in `want_type`.  
»» max_amount | string | Maximum trade amount priced in `want_type`.  
»» total | string | Fiat amount  
»» pay_ali | integer | Whether Alipay is supported. `1`: yes; `0`: no.  
»» pay_bank | integer | Whether bank transfer is supported. `1`: yes; `0`: no.  
»» pay_paypal | integer | Whether PayPal is supported. `1`: yes; `0`: no.  
»» pay_wechat | integer | Whether WeChat Pay is supported. `1`: yes; `0`: no.  
»» pay_type_num | string | Payment method ID list  
»» pay_type_json | string | JSON map of payment type -> payment method ID.  
»» locked_amount | string | Locked amount  
»» orderid | integer | Order ID  
»» timestamp | integer | Created time  
»» currency_type | string | Cryptocurrency symbol.  
»» want_type | string | Fiat type  
»» hide_rate | string | Hidden price  
»» trade_tips | string | Trading terms  
»» auto_reply | string | Auto reply  
»» rate_ref_id | integer | Floating reference: `1` platform; `2` Gate; `3` spot; `<= 0` means fixed price.  
»» rate_offset | number | Floating ratio (absolute value)  
»» status | string | Ad status: `OPEN` listed; `OFFLIN` delisted; `CLOSED` closed; `CANCEL` canceled.  
»» rate_fixed | integer | Price type: `0` floating; `1` fixed.  
»» float_trend | integer | Floating direction: `0` markup; `1` markdown.  
»» expire_min | integer | Timeout (minutes)  
»» tier_limit | integer | Tier limit  
»» reg_time_limit | integer | Registration time limit  
»» advertisers_limit | integer | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
»» min_completed_limit | integer | Minimum limit of completed orders  
»» max_completed_limit | integer | Maximum limit of completed orders  
»» user_orders_limit | integer | Order count limit  
»» completed_rate_limit | number | 30-day completion rate limit  
»» limit_country_cn | string | Restricted nationality (Chinese)  
»» limit_country_en | string | Restricted nationality (English)  
»» is_hedge | integer | Whether auto-delegation is enabled. `1`: yes; `0`: no.  
»» hide_payment | integer | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "adv_no": "2124000001"
    }
    

> Example responses

> 200 Response
    
    
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
    

##  Get my ad list🔒 Authenticated

POST`/p2p/merchant/books/my_ads_list`

POST `/p2p/merchant/books/my_ads_list`

Get `my ad list`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | MyAdsListRequest | Optional | none  
↳ asset | body | string | Optional | Crypto asset; omit to skip asset filter.  
↳ fiat_unit | body | string | Optional | Fiat currency; omit to skip fiat filter.  
↳ trade_type | body | string | Optional | Ad side: `buy` for buy-crypto ads, `sell` for sell-crypto ads; omit for all sides.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMyAdsListResponse  
  
### Response Schema

Status Code **200**

_P2pMyAdsListResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» lists | array | none  
»»» P2pMyAd | object | none  
»»»» type | string | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
»»»» rate | string | Price  
»»»» original_rate | string | Original price  
»»»» amount | string | Remaining crypto amount on the ad.  
»»»» total | string | Remaining fiat amount of ad  
»»»» limit_total | string | Single order limit range (cryptocurrency)  
»»»» limit_fiat | string | Single order limit range (fiat)  
»»»» min_amount | string | Minimum quantity per order  
»»»» max_amount | string | Maximum quantity per order  
»»»» pay_type_num | string | Payment method ID list  
»»»» pay_type_json | string | JSON map of payment type -> payment method ID.  
»»»» expire_min | string | Ad expiration time (minutes)  
»»»» tier_limit | string | VIP limit  
»»»» advertisers_limit | integer | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
»»»» reg_time_limit | integer | Registration time limit  
»»»» verified_limit | integer | KYC level limit  
»»»» min_completed_limit | integer | Minimum limit of completed orders by counterparty  
»»»» max_completed_limit | integer | Maximum limit of completed orders by counterparty  
»»»» user_country_limit | integer | KYC nationality restriction  
»»»» completed_rate_limit | number | 30-day completion rate limit  
»»»» user_orders_limit | integer | Maximum order limit for counterparty  
»»»» hide_payment | string | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
»»»» currencyType | string | Cryptocurrency symbol.  
»»»» want_type | string | Fiat currency  
»»»» trade_tips | string | Trading terms  
»»»» new_hand | integer | Special ad type. `0` normal; `1` newcomer guide; `2` newcomer discount; `3` featured promo; `4` KOL ad; `5` coupon ad.  
»»»» id | string | Advertisement ID.  
»»»» status | string | Ad status: `OPEN` listed; `OFFLIN` delisted; `CLOSED` closed; `CANCEL` canceled.  
»»»» locked_amount | string | Ad frozen amount  
»»»» hide_rate | string | Hidden price  
»»»» is_out_time | integer | Whether the ad timed out. `1`: timed out; `0`: not yet.  
»»»» rate_ref_id | integer | Floating reference: `1` platform; `2` Gate; `3` spot; `<= 0` means fixed price.  
»»»» rate_offset | string | Floating ratio  
»»»» rate_fixed | integer | Price type: `0` floating; `1` fixed.  
»»»» float_trend | integer | Floating direction: `0` markup; `1` markdown.  
»»»» in_dispute | integer | Whether the ad had a disputed trade. `1`: yes; `0`: no.  
»»»» auto_reply | string | Auto reply data  
»»»» timestamp | integer | Ad creation time  
»»»» is_hedge | integer | Whether auto-delegation is enabled. `1`: yes; `0`: no.  
»»» version | string | Version number  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    

> Example responses

> 200 Response
    
    
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
    

##  Get Advertisement List🔒 Authenticated

POST`/p2p/merchant/books/ads_list`

POST `/p2p/merchant/books/ads_list`

Get `Advertisement List`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AdsListRequest | Required | none  
↳ asset | body | string | Required | Cryptocurrency symbol.  
↳ fiat_unit | body | string | Required | Fiat currency  
↳ trade_type | body | string | Required | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pAdsListResponse  
  
### Response Schema

Status Code **200**

_P2pAdsListResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | array | none  
»» P2pAdsListItem | object | none  
»»» index | integer | Serial number  
»»» asset | string | Cryptocurrency  
»»» fiat_unit | string | Fiat currency  
»»» adv_no | integer | Ad ID  
»»» price | string | Price  
»»» max_single_trans_amount | string | Maximum crypto size per trade.  
»»» min_single_trans_amount | string | Minimum crypto size per trade.  
»»» nick_name | string | Advertiser Nickname  
»» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    

> Example responses

> 200 Response
    
    
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
    

##  Get chat history🔒 Authenticated

POST`/p2p/merchant/chat/get_chats_list`

POST `/p2p/merchant/chat/get_chats_list`

Get `chat history`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetChatsListRequest | Required | none  
↳ txid | body | integer | Optional | Order ID; omit or `0` to return the latest order with chat for the user.  
↳ lastreceived | body | integer | Optional | Timestamp of the last received message for backward incremental fetch; omit on first load.  
↳ firstreceived | body | integer | Optional | Timestamp of first received message for paging backward; omit on first load.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pChatListResponse  
  
### Response Schema

Status Code **200**

_P2pChatListResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» messages | array | Message List  
»»» P2pChatMessage | object | none  
»»»» is_sell | integer | Whether the current user is the seller. `1`: yes; `0`: no.  
»»»» msg_type | integer | Message type: `0` text; `1` file; `2` template; `3` order-share; `4` payment-share; `5` status update.  
»»»» msg | string | Message content; for file messages, usually URL or file key.  
»»»» username | string | Message sender username  
»»»» timest | integer | Message timestamp  
»»»» msg_obj | object | none  
»»»»» status | string | Order status when sending a message. Typical values: `OPEN`, `PAID`, `LOCKED`, `ACCEPT`, `BCLOSED`, `CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`.  
»»»»» text | string | Message content  
»»»»» payment_voucher | array | Payment voucher  
»»»»» reason_id | integer | Cancel reason ID. `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller account not real; `5` payout account issue; `6` price mismatch; `7` mutually agreed cancel; `8` poor communication; `9` other; `10` seller cannot release with refund; `11` terms not met; `12` seller payout risk-controlled.  
»»»»» toast_id | integer | Cancellation reason popup  
»»»»» reason_memo | string | Cancel reason description.  
»»»»» cancel_time | integer | Cancellation time  
»»»»» seller_confirm | integer | Seller confirmation of cancel reason: `0` pending; `1` confirmed; `2` rejected.  
»»»»» id | string | Payment method information ID  
»»»»» account_des | string | Payment method description  
»»»»» pay_type | string | Payment method type  
»»»»» file | string | Payment method file link  
»»»»» file_key | string | Payment method file key  
»»»»» account | string | Payment account or masked payment account.  
»»»»» memo | string | Payment method note  
»»»»» code | string | Payment method code  
»»»»» memo_ext | string | Payment method additional note  
»»»»» trade_tips | string | Payment method tip  
»»»»» real_name | string | Payment method username  
»»»»» is_delete | integer | Whether the payment method was deleted. `1`: deleted; `0`: not deleted.  
»»»»» pay_name | string | Payment method full name  
»»»» uid | string | Sender's crypto UID; system messages may use `System` or an empty string.  
»»»» type | integer | Display type: `1` file message; `2` system message.  
»»»» pic | string | File link  
»»»» file_key | string | File key  
»»»» file_type | string | File type: `image` for images, `video` for videos.  
»»» memo | string | Payment tip (displayed on homepage only)  
»»» has_history | boolean | Whether historical records exist  
»»» txid | integer | Order ID  
»»» SRVTM | integer | Timestamp of the latest message.  
»»» order_status | string | Raw order status in DB; typical values: `OPEN`, `PAID`, `LOCKED`, `ACCEPT`, `BCLOSED`, `CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`.  
»» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "txid": 40000001,
      "lastreceived": 1767009884,
      "firstreceived": 1767009000
    }
    

> Example responses

> 200 Response
    
    
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
    

##  Send text message🔒 Authenticated

POST`/p2p/merchant/chat/send_chat_message`

POST `/p2p/merchant/chat/send_chat_message`

_Send text message_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | SendChatMessageRequest | Required | none  
↳ txid | body | integer | Required | Order ID  
↳ type | body | integer | Optional | Message type: `0` text; `1` file (image or video); defaults to `0`.  
↳ message | body | string | Required | Message body. For `type=0`, plain text up to 500 characters; for `type=1`, pass the `file_key` returned by `upload_chat_file`.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» type | 0  
» type | 1  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pSendChatMessageResponse  
  
### Response Schema

Status Code **200**

_P2pSendChatMessageResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» SRVTM | integer | Timestamp when message was successfully sent (current timestamp)  
» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "txid": 40000001,
      "type": 0,
      "message": "Payment completed, please check"
    }
    

> Example responses

> 200 Response
    
    
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
    

##  Upload chat file🔒 Authenticated

POST`/p2p/merchant/chat/upload_chat_file`

POST `/p2p/merchant/chat/upload_chat_file`

_Upload chat file_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | UploadChatFile | Required | none  
↳ image_content_type | body | string | Required | File MIME type: supports `image/jpeg`, `image/jpg`, `image/png`, `video/mp4`.  
↳ base64_img | body | string | Required | Base64 file content; max 20 MB.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» image_content_type | image/jpeg  
» image_content_type | image/jpg  
» image_content_type | image/png  
» image_content_type | video/mp4  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pUploadChatFileResponse  
  
### Response Schema

Status Code **200**

_P2pUploadChatFileResponse_

Name | Type | Description  
---|---|---  
» timestamp | number | none  
» method | string | none  
» code | integer | none  
» message | string | none  
» data | object | none  
»» file_key | string | File key  
» version | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
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
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Body parameter
    
    
    {
      "image_content_type": "image/png",
      "base64_img": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."
    }
    

> Example responses

> 200 Response
    
    
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
    

#  Schemas

##  UploadChatFile

_Upload chat file request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
image_content_type | string | Required | none | File MIME type: supports `image/jpeg`, `image/jpg`, `image/png`, `video/mp4`.  
base64_img | string | Required | none | Base64 file content; max 20 MB.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
image_content_type | image/jpeg  
image_content_type | image/jpg  
image_content_type | image/png  
image_content_type | video/mp4  
      
    
    {
      "image_content_type": "image/png",
      "base64_img": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."
    }
    
    

##  ConfirmPayment

_Confirm payment request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
txid | string | Required | none | Order ID  
payment_method | string | Optional | none | Payment type used for this payment; optional but must be among order-supported types. Use `supported_pay_types` on the order or `pay_type` list, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
      
    
    {
      "txid": "40000001",
      "payment_method": "bank"
    }
    
    

##  GetCompletedTransactionListRequest

Get`completed/historical transaction list request`

Get `completed/historical transaction list request`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
crypto_currency | string | Required | none | Cryptocurrency symbol.  
fiat_currency | string | Required | none | Fiat currency  
select_type | string | Optional | none | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
status | string | Optional | none | Order status filter. `closed`: filled (`ACCEPT`, `BCLOSED`); `cancel`: canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`);  
`locked`: locked (`LOCKED`); `open`: unpaid (`OPEN`); `paid`: paid (`PAID`);  
`completed`: finished or canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`, `ACCEPT`, `BCLOSED`);  
Empty or omitted uses the endpoint default range.  
txid | integer | Optional | none | Order ID  
start_time | integer | Optional | none | Start timestamp, default is 00:00 89 days ago  
end_time | integer | Optional | none | End timestamp, default is 23:59:59 today  
query_dispute | integer | Optional | none | Whether to flag dispute status in the response. `1`: yes; `0`: no.  
page | integer | Optional | none | Page number starting at 1; values below 1 are treated as 1.  
per_page | integer | Optional | none | Orders per page; default 10, max 200.  
      
    
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
    
    

##  P2pUploadChatFileResponse

_P2pUploadChatFileResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ file_key | string | Optional | none | File key  
version | string | Optional | none | none  
      
    
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
    
    

##  SendChatMessageRequest

_Send chat message request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
txid | integer | Required | none | Order ID  
type | integer | Optional | none | Message type: `0` text; `1` file (image or video); defaults to `0`.  
message | string | Required | none | Message body. For `type=0`, plain text up to 500 characters; for `type=1`, pass the `file_key` returned by `upload_chat_file`.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | 0  
type | 1  
      
    
    {
      "txid": 40000001,
      "type": 0,
      "message": "Payment completed, please check"
    }
    
    

##  CancelOrder

_Cancel order request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
txid | string | Required | none | Order ID  
reason_id | string | Optional | none | Cancel reason ID. `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller account not real; `5` payout account issue; `6` price mismatch; `7` mutually agreed cancel; `8` poor communication; `9` other; `10` seller cannot release with refund; `11` terms not met; `12` seller payout risk-controlled.  
reason_memo | string | Optional | none | Extra cancel notes when `reason_id` is `9` or explanation is required.  
      
    
    {
      "txid": "40000001",
      "reason_id": "1",
      "reason_memo": "Canceled after agreement with the counterparty"
    }
    
    

##  P2pChatListResponse

_P2pChatListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ messages | array | Optional | none | Message List  
↳ P2pChatMessage | object | Optional | none | none  
↳ is_sell | integer | Optional | none | Whether the current user is the seller. `1`: yes; `0`: no.  
↳ msg_type | integer | Optional | none | Message type: `0` text; `1` file; `2` template; `3` order-share; `4` payment-share; `5` status update.  
↳ msg | string | Optional | none | Message content; for file messages, usually URL or file key.  
↳ username | string | Optional | none | Message sender username  
↳ timest | integer | Optional | none | Message timestamp  
↳ msg_obj | object | Optional | none | none  
↳ status | string | Optional | none | Order status when sending a message. Typical values: `OPEN`, `PAID`, `LOCKED`, `ACCEPT`, `BCLOSED`, `CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`.  
↳ text | string | Optional | none | Message content  
↳ payment_voucher | array | Optional | none | Payment voucher  
↳ reason_id | integer | Optional | none | Cancel reason ID. `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller account not real; `5` payout account issue; `6` price mismatch; `7` mutually agreed cancel; `8` poor communication; `9` other; `10` seller cannot release with refund; `11` terms not met; `12` seller payout risk-controlled.  
↳ toast_id | integer | Optional | none | Cancellation reason popup  
↳ reason_memo | string | Optional | none | Cancel reason description.  
↳ cancel_time | integer | Optional | none | Cancellation time  
↳ seller_confirm | integer | Optional | none | Seller confirmation of cancel reason: `0` pending; `1` confirmed; `2` rejected.  
↳ id | string | Optional | none | Payment method information ID  
↳ account_des | string | Optional | none | Payment method description  
↳ pay_type | string | Optional | none | Payment method type  
↳ file | string | Optional | none | Payment method file link  
↳ file_key | string | Optional | none | Payment method file key  
↳ account | string | Optional | none | Payment account or masked payment account.  
↳ memo | string | Optional | none | Payment method note  
↳ code | string | Optional | none | Payment method code  
↳ memo_ext | string | Optional | none | Payment method additional note  
↳ trade_tips | string | Optional | none | Payment method tip  
↳ real_name | string | Optional | none | Payment method username  
↳ is_delete | integer | Optional | none | Whether the payment method was deleted. `1`: deleted; `0`: not deleted.  
↳ pay_name | string | Optional | none | Payment method full name  
↳ uid | string | Optional | none | Sender's crypto UID; system messages may use `System` or an empty string.  
↳ type | integer | Optional | none | Display type: `1` file message; `2` system message.  
↳ pic | string | Optional | none | File link  
↳ file_key | string | Optional | none | File key  
↳ file_type | string | Optional | none | File type: `image` for images, `video` for videos.  
↳ memo | string | Optional | none | Payment tip (displayed on homepage only)  
↳ has_history | boolean | Optional | none | Whether historical records exist  
↳ txid | integer | Optional | none | Order ID  
↳ SRVTM | integer | Optional | none | Timestamp of the latest message.  
↳ order_status | string | Optional | none | Raw order status in DB; typical values: `OPEN`, `PAID`, `LOCKED`, `ACCEPT`, `BCLOSED`, `CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`.  
↳ version | string | Optional | none | none  
      
    
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
    
    

##  P2pTransactionDetailResponse

_P2pTransactionDetailResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ is_sell | integer | Optional | none | Whether the current user is the seller. `1`: yes; `0`: no.  
↳ txid | integer | Optional | none | Order ID  
↳ orderid | integer | Optional | none | Order ID  
↳ timest | integer | Optional | none | Order creation timestamp  
↳ last_pay_time | integer | Optional | none | Payment deadline  
↳ remain_pay_time | integer | Optional | none | Seconds left to pay; `<= 0` means overdue.  
↳ currency_type | string | Optional | none | Cryptocurrency symbol.  
↳ want_type | string | Optional | none | Fiat currency  
↳ symbol | string | Optional | none | Fiat currency symbol  
↳ rate | string | Optional | none | Order price in `want_type` units.  
↳ amount | string | Optional | none | Order size in cryptocurrency.  
↳ total | string | Optional | none | Total fiat amount of the order.  
↳ status | string | Optional | none | Display status: `unpay` unpaid; `hide_payment` unpaid with payment info hidden; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` done; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
↳ reason_id | string | Optional | none | Cancel reason ID; empty string means none. Examples: `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller did not provide a real account; `6` price/amount mismatch; `9` other; `10` seller cannot release and refund issued; `11` terms not met; `12` seller payout account risk-controlled.  
↳ reason_desc | string | Optional | none | Cancel reason description.  
↳ cancel_time | string | Optional | none | Cancellation time  
↳ in_appeal | integer | Optional | none | Whether a dispute is active. `1`: yes; `0`: no.  
↳ dispute_time | integer | Optional | none | Earliest timestamp when a dispute may be opened.  
↳ cancelable | integer | Optional | none | Whether cancellation is allowed. `1`: yes; `0`: no.  
↳ hide_payment | integer | Optional | none | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
↳ trade_tips | string | Optional | none | Trading terms  
↳ show_bank | string | Optional | none | Whether to show bank transfer details. `1`: show; `0`: hide.  
↳ bankname | string | Optional | none | Bank name  
↳ bankbranch | string | Optional | none | Bank branch name  
↳ bankid | string | Optional | none | Bank account or masked account.  
↳ bank_holder_realname | string | Optional | none | Bank cardholder name  
↳ show_ali | string | Optional | none | Whether to show Alipay details. `1`: show; `0`: hide.  
↳ aliname | string | Optional | none | Alipay account name  
↳ is_alicode | integer | Optional | none | Whether an Alipay QR exists. `1`: yes; `0`: no.  
↳ show_wechat | string | Optional | none | Whether to show WeChat details. `1`: show; `0`: hide.  
↳ wename | string | Optional | none | WeChat account name  
↳ show_others | string | Optional | none | Whether to show other payment methods. `1`: show; `0`: hide.  
↳ pay_others | array | Optional | none | Other payment methods  
↳ id | string | Optional | none | Payment method record ID.  
↳ account_des | string | Optional | none | Payment method description  
↳ pay_type | string | Optional | none | Payment method type  
↳ account | string | Optional | none | Payment account or masked account.  
↳ memo | string | Optional | none | Payment note or memo.  
↳ trade_tips | string | Optional | none | Payment instructions or tips.  
↳ pay_name | string | Optional | none | Display name of the payment method.  
↳ sel_paytype | string | Optional | none | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
↳ its_uid | string | Optional | none | Counterparty crypto UID.  
↳ its_nickname | string | Optional | none | Counterparty nickname  
↳ its_realname | string | Optional | none | Counterparty real name or verified display name.  
↳ have_traded | integer | Optional | none | Whether you traded with the counterparty before. `1`: yes; `0`: no.  
↳ appeal_allow_cancel | integer | Optional | none | Whether the dispute can be withdrawn. `1`: allowed; `0`: not allowed.  
↳ appeal_verdict_has_open | string | Optional | none | Dispute outcome or in-dispute notice text.  
↳ im_unread | integer | Optional | none | Unread chat message count.  
↳ payment_voucher_url | array | Optional | none | Payment voucher  
↳ timest_paid | integer | Optional | none | Timestamp when the buyer confirmed payment.  
↳ own_realname | string | Optional | none | Current user's real name or verified display name.  
↳ order_type | integer | Optional | none | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
↳ is_show_receive | integer | Optional | none | Whether to show confirm-receipt during dispute. `1`: show; `0`: hide.  
↳ show_seller_contact_info | boolean | Optional | none | Whether to display seller contact information  
↳ supported_pay_types | array | Optional | none | Supported payment method types for the order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
version | string | Optional | none | none  
      
    
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
    
    

##  AdsListRequest

Get`market ads list request`

Get `market ads list request`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
asset | string | Required | none | Cryptocurrency symbol.  
fiat_unit | string | Required | none | Fiat currency  
trade_type | string | Required | none | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
      
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    
    

##  AdsUpdateStatus

_Ad status update request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
adv_no | integer | Required | none | Advertisement ID.  
adv_status | integer | Required | none | Ad status. `1`: listed; `3`: delisted; `4`: closed.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
adv_status | 1  
adv_status | 3  
adv_status | 4  
      
    
    {
      "adv_no": 2124000001,
      "adv_status": 3
    }
    
    

##  AdsDetailRequest

Get`ad details request`

Get `ad details request`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
adv_no | string | Required | none | Advertisement ID.  
      
    
    {
      "adv_no": "2124000001"
    }
    
    

##  P2pSendChatMessageResponse

_P2pSendChatMessageResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ SRVTM | integer | Optional | none | Timestamp when message was successfully sent (current timestamp)  
version | string | Optional | none | none  
      
    
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
    
    

##  P2pAdsListResponse

_P2pAdsListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | array | Optional | none | none  
↳ P2pAdsListItem | object | Optional | none | none  
↳ index | integer | Optional | none | Serial number  
↳ asset | string | Optional | none | Cryptocurrency  
↳ fiat_unit | string | Optional | none | Fiat currency  
↳ adv_no | integer | Optional | none | Ad ID  
↳ price | string | Optional | none | Price  
↳ max_single_trans_amount | string | Optional | none | Maximum crypto size per trade.  
↳ min_single_trans_amount | string | Optional | none | Minimum crypto size per trade.  
↳ nick_name | string | Optional | none | Advertiser Nickname  
↳ version | string | Optional | none | none  
      
    
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
    
    

##  P2pMyAdsListResponse

_P2pMyAdsListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ lists | array | Optional | none | none  
↳ P2pMyAd | object | Optional | none | none  
↳ type | string | Optional | none | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
↳ rate | string | Optional | none | Price  
↳ original_rate | string | Optional | none | Original price  
↳ amount | string | Optional | none | Remaining crypto amount on the ad.  
↳ total | string | Optional | none | Remaining fiat amount of ad  
↳ limit_total | string | Optional | none | Single order limit range (cryptocurrency)  
↳ limit_fiat | string | Optional | none | Single order limit range (fiat)  
↳ min_amount | string | Optional | none | Minimum quantity per order  
↳ max_amount | string | Optional | none | Maximum quantity per order  
↳ pay_type_num | string | Optional | none | Payment method ID list  
↳ pay_type_json | string | Optional | none | JSON map of payment type -> payment method ID.  
↳ expire_min | string | Optional | none | Ad expiration time (minutes)  
↳ tier_limit | string | Optional | none | VIP limit  
↳ advertisers_limit | integer | Optional | none | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
↳ reg_time_limit | integer | Optional | none | Registration time limit  
↳ verified_limit | integer | Optional | none | KYC level limit  
↳ min_completed_limit | integer | Optional | none | Minimum limit of completed orders by counterparty  
↳ max_completed_limit | integer | Optional | none | Maximum limit of completed orders by counterparty  
↳ user_country_limit | integer | Optional | none | KYC nationality restriction  
↳ completed_rate_limit | number | Optional | none | 30-day completion rate limit  
↳ user_orders_limit | integer | Optional | none | Maximum order limit for counterparty  
↳ hide_payment | string | Optional | none | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
↳ currencyType | string | Optional | none | Cryptocurrency symbol.  
↳ want_type | string | Optional | none | Fiat currency  
↳ trade_tips | string | Optional | none | Trading terms  
↳ new_hand | integer | Optional | none | Special ad type. `0` normal; `1` newcomer guide; `2` newcomer discount; `3` featured promo; `4` KOL ad; `5` coupon ad.  
↳ id | string | Optional | none | Advertisement ID.  
↳ status | string | Optional | none | Ad status: `OPEN` listed; `OFFLIN` delisted; `CLOSED` closed; `CANCEL` canceled.  
↳ locked_amount | string | Optional | none | Ad frozen amount  
↳ hide_rate | string | Optional | none | Hidden price  
↳ is_out_time | integer | Optional | none | Whether the ad timed out. `1`: timed out; `0`: not yet.  
↳ rate_ref_id | integer | Optional | none | Floating reference: `1` platform; `2` Gate; `3` spot; `<= 0` means fixed price.  
↳ rate_offset | string | Optional | none | Floating ratio  
↳ rate_fixed | integer | Optional | none | Price type: `0` floating; `1` fixed.  
↳ float_trend | integer | Optional | none | Floating direction: `0` markup; `1` markdown.  
↳ in_dispute | integer | Optional | none | Whether the ad had a disputed trade. `1`: yes; `0`: no.  
↳ auto_reply | string | Optional | none | Auto reply data  
↳ timestamp | integer | Optional | none | Ad creation time  
↳ is_hedge | integer | Optional | none | Whether auto-delegation is enabled. `1`: yes; `0`: no.  
↳ version | string | Optional | none | Version number  
      
    
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
    
    

##  P2pAdsUpdateStatusResponse

_P2pAdsUpdateStatusResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ status | integer | Optional | none | Ad status after update: `1` listed; `3` delisted; `4` closed.  
version | string | Optional | none | none  
      
    
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
    
    

##  P2pMerchantUserInfoResponse

_P2pMerchantUserInfoResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ is_self | boolean | Optional | none | Whether self  
↳ user_timest | string | Optional | none | User registration time (formatted string)  
↳ counterparties_num | integer | Optional | none | Number of counterparties  
↳ email_verified | string | Optional | none | Whether email is verified. `1`: yes; `0`: no.  
↳ verified | string | Optional | none | Whether KYC is completed. `1`: yes; `0`: no.  
↳ has_phone | string | Optional | none | Whether a phone number is bound. `1`: yes; `0`: no.  
↳ user_name | string | Optional | none | Username  
↳ user_note | string | Optional | none | User note information  
↳ complete_transactions | string | Optional | none | Total completed orders  
↳ paid_transactions | string | Optional | none | Number of completed buy orders  
↳ accepted_transactions | string | Optional | none | Number of completed sell orders  
↳ transactions_used_time | string | Optional | none | Average time to confirm receipt  
↳ cancelled_used_time_month | string | Optional | none | Cancellation time in last 30 days  
↳ complete_transactions_month | string | Optional | none | Number of completed orders in last 30 days  
↳ complete_rate_month | number | Optional | none | Completion rate in last 30 days  
↳ orders_buy_rate_month | number | Optional | none | Buy order ratio in last 30 days  
↳ is_black | integer | Optional | none | Whether the user is blocked. `1`: yes; `0`: no.  
↳ is_follow | integer | Optional | none | Whether you follow this user. `1`: yes; `0`: no.  
↳ have_traded | integer | Optional | none | Whether you have traded with this user before. `1`: yes; `0`: no.  
↳ biz_uid | string | Optional | none | Encrypted UID  
↳ blue_vip | integer | Optional | none | Blue V Crown Shield  
↳ work_status | integer | Optional | none | Merchant work status  
↳ registration_days | integer | Optional | none | Registration days  
↳ first_trade_days | integer | Optional | none | Days since first trade  
↳ need_replenish | integer | Optional | none | Whether additional margin is required. `1`: yes; `0`: no.  
↳ merchant_info | object | Optional | none | Markets where user can place orders  
↳ type | string | Optional | none | none  
↳ market | string | Optional | none | none  
↳ online_status | integer | Optional | none | Merchant online status: `1` online; `0` offline.  
↳ work_hours | object|null | Optional | none | Merchant online status details  
↳ transactions_month | number | Optional | none | 30-day transaction volume  
↳ transactions_all | number | Optional | none | Total transaction volume  
↳ trade_versatile | boolean | Optional | none | Single user or composite user  
version | string | Optional | none | none  
      
    
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
    
    

##  GetChatsListRequest

Get`chat history request`

Get `chat history request`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
txid | integer | Optional | none | Order ID; omit or `0` to return the latest order with chat for the user.  
lastreceived | integer | Optional | none | Timestamp of the last received message for backward incremental fetch; omit on first load.  
firstreceived | integer | Optional | none | Timestamp of first received message for paging backward; omit on first load.  
      
    
    {
      "txid": 40000001,
      "lastreceived": 1767009884,
      "firstreceived": 1767009000
    }
    
    

##  P2pTransactionListResponse

_P2pTransactionListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ list | array | Optional | none | none  
↳ P2pTransactionListItem | object | Optional | none | none  
↳ type_buy | integer | Optional | none | Order side from current user's view. `1`: buy; `0`: sell.  
↳ timest | string | Optional | none | Creation time of order  
↳ timest_expire | string | Optional | none | Order expiration time  
↳ timestamp | integer | Optional | none | Order creation timestamp  
↳ rate | string | Optional | none | Order price in fiat currency.  
↳ amount | string | Optional | none | Order size in cryptocurrency.  
↳ total | string | Optional | none | Total fiat amount of the order.  
↳ txid | integer | Optional | none | Order ID  
↳ status | string | Optional | none | Display status: `unpay` awaiting payment; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` completed; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
↳ its_realname | string | Optional | none | Counterparty real name or verified display name.  
↳ its_uid | string | Optional | none | Counterparty crypto UID.  
↳ its_nick | string | Optional | none | Counterparty nickname  
↳ seller_realname | string | Optional | none | Seller real name or verified display name.  
↳ buyer_realname | string | Optional | none | Buyer real name or verified display name.  
↳ cancelable | integer | Optional | none | Whether the order can be canceled. `1`: yes; `0`: no.  
↳ currency_type | string | Optional | none | Cryptocurrency symbol.  
↳ want_type | string | Optional | none | Fiat currency  
↳ hide_payment | integer | Optional | none | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
↳ sel_paytype | string | Optional | none | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
↳ pay_others | array | Optional | none | Other payment method details; may appear on historical orders.  
↳ pay_type | string | Optional | none | Payment method type  
↳ pay_name | string | Optional | none | Payment method name  
↳ cd_time | integer | Optional | none | Countdown seconds for the current order.  
↳ order_type | integer | Optional | none | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
↳ order_tag | array | Optional | none | Order tags  
↳ convert_info | object | Optional | none | Flash swap order information  
↳ convert_type | string | Optional | none | Flash swap target currency  
↳ convert_status | string | Optional | none | Flash swap order status  
↳ pre_rate | string | Optional | none | Expected price when placing order  
↳ rate | string | Optional | none | Execution price  
↳ pre_fiat_rate | string | Optional | none | Expected fiat price when placing order  
↳ fiat_rate | string | Optional | none | Fiat price at execution  
↳ amount | string | Optional | none | Size  
↳ convert_amount | string | Optional | none | Swap Amount  
↳ slippage | string | Optional | none | Slippage calculation: slippage = (expected price when placing order - real-time price during auto swap) / expected price when placing order  
↳ status | string | Optional | none | Flash swap order display status  
↳ trans_time | array | Optional | none | Countdown time  
↳ P2pTransactionTimeMarker | object | Optional | none | none  
↳ od_time | integer | Optional | none | none  
↳ count | integer | Optional | none | Number of orders  
↳ exported_num | integer | Optional | none | Export count  
↳ version | string | Optional | none | none  
      
    
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
    
    

##  P2pAdDetailResponse

_P2pAdDetailResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ rate | string | Optional | none | Advertisement price.  
↳ type | string | Optional | none | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
↳ amount | string | Optional | none | Remaining crypto amount on the ad.  
↳ min_amount | string | Optional | none | Minimum trade amount in `want_type`.  
↳ max_amount | string | Optional | none | Maximum trade amount priced in `want_type`.  
↳ total | string | Optional | none | Fiat amount  
↳ pay_ali | integer | Optional | none | Whether Alipay is supported. `1`: yes; `0`: no.  
↳ pay_bank | integer | Optional | none | Whether bank transfer is supported. `1`: yes; `0`: no.  
↳ pay_paypal | integer | Optional | none | Whether PayPal is supported. `1`: yes; `0`: no.  
↳ pay_wechat | integer | Optional | none | Whether WeChat Pay is supported. `1`: yes; `0`: no.  
↳ pay_type_num | string | Optional | none | Payment method ID list  
↳ pay_type_json | string | Optional | none | JSON map of payment type -> payment method ID.  
↳ locked_amount | string | Optional | none | Locked amount  
↳ orderid | integer | Optional | none | Order ID  
↳ timestamp | integer | Optional | none | Created time  
↳ currency_type | string | Optional | none | Cryptocurrency symbol.  
↳ want_type | string | Optional | none | Fiat type  
↳ hide_rate | string | Optional | none | Hidden price  
↳ trade_tips | string | Optional | none | Trading terms  
↳ auto_reply | string | Optional | none | Auto reply  
↳ rate_ref_id | integer | Optional | none | Floating reference: `1` platform; `2` Gate; `3` spot; `<= 0` means fixed price.  
↳ rate_offset | number | Optional | none | Floating ratio (absolute value)  
↳ status | string | Optional | none | Ad status: `OPEN` listed; `OFFLIN` delisted; `CLOSED` closed; `CANCEL` canceled.  
↳ rate_fixed | integer | Optional | none | Price type: `0` floating; `1` fixed.  
↳ float_trend | integer | Optional | none | Floating direction: `0` markup; `1` markdown.  
↳ expire_min | integer | Optional | none | Timeout (minutes)  
↳ tier_limit | integer | Optional | none | Tier limit  
↳ reg_time_limit | integer | Optional | none | Registration time limit  
↳ advertisers_limit | integer | Optional | none | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
↳ min_completed_limit | integer | Optional | none | Minimum limit of completed orders  
↳ max_completed_limit | integer | Optional | none | Maximum limit of completed orders  
↳ user_orders_limit | integer | Optional | none | Order count limit  
↳ completed_rate_limit | number | Optional | none | 30-day completion rate limit  
↳ limit_country_cn | string | Optional | none | Restricted nationality (Chinese)  
↳ limit_country_en | string | Optional | none | Restricted nationality (English)  
↳ is_hedge | integer | Optional | none | Whether auto-delegation is enabled. `1`: yes; `0`: no.  
↳ hide_payment | integer | Optional | none | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
version | string | Optional | none | none  
      
    
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
    
    

##  GetCounterpartyUserInfoRequest

Get`counterparty user info request`

Get `counterparty user info request`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
biz_uid | string | Required | none | Counterparty crypto UID from order list or detail field `its_uid`.  
      
    
    {
      "biz_uid": "biz_uid_demo_9f3a7c"
    }
    
    

##  P2pMerchantBooksPlaceBizPushOrderResponse

_P2pMerchantBooksPlaceBizPushOrderResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | Response timestamp.  
method | string | Optional | none | Placeholder for request method.  
code | integer | Optional | none | Response code, 0 means success  
message | string | Optional | none | Response message  
data | object | Optional | none | Empty object on successful publish or edit.  
version | string | Optional | none | API version.  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {},
      "version": "string"
    }
    
    

##  ConfirmReceipt

_Confirm receipt request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
txid | string | Required | none | Order ID  
      
    
    {
      "txid": "40000001"
    }
    
    

##  PlaceBizPushOrder

_Place ad order request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currencyType | string | Required | none | Cryptocurrency symbol.  
exchangeType | string | Required | none | Fiat currency  
type | string | Required | none | Ad operation type. `0`: publish sell ad; `1`: publish buy ad; `2`: edit sell ad; `3`: edit buy ad.  
unitPrice | string | Required | none | Per-unit price in fixed-price mode.  
number | string | Required | none | Ad amount priced in `currencyType`.  
payType | string | Required | none | Payment types, comma-separated; from pay type list `pay_type`, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
pay_type_json | string | Optional | none | JSON map of payment type -> user's payment method ID.  
rateFixed | string | Optional | none | Price type: `0` floating; `1` fixed.  
oid | string | Optional | none | Pass ad ID when editing; omit or empty when publishing a new ad.  
minAmount | string | Required | none | Minimum trade amount in `exchangeType`.  
maxAmount | string | Required | none | Maximum amount per trade in `exchangeType` fiat units.  
tierLimit | string | Optional | none | Minimum counterparty VIP level; `0` means no requirement.  
verifiedLimit | string | Optional | none | Minimum counterparty verification level; `0` means no limit.  
regTimeLimit | string | Optional | none | Minimum counterparty account age in days; `0` means no limit.  
advertisersLimit | string | Optional | none | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
expire_min | string | Optional | none | Payment timeout in minutes.  
trade_tips | string | Optional | none | Ad trading terms shown to the taker.  
auto_reply | string | Optional | none | Auto-reply message after order creation.  
min_completed_limit | string | Optional | none | Minimum completed orders for counterparty; `-1` unlimited.  
max_completed_limit | string | Optional | none | Maximum completed orders for counterparty; `-1` unlimited.  
completed_rate_limit | string | Optional | none | Counterparty minimum 30-day completion rate; `-1` means no limit.  
user_country_limit | string | Optional | none | KYC nationality restriction; `-1` means no restriction.  
user_order_limit | string | Optional | none | Maximum concurrent orders allowed for the counterparty. `-1`: unlimited.  
rateReferenceId | string | Optional | none | Floating price reference. `1`: platform reference; `2`: Gate reference; `3`: spot reference.  
rateOffset | string | Optional | none | Absolute floating offset ratio, e.g. `0.5` means 0.5%.  
float_trend | string | Optional | none | Floating direction: `0` markup; `1` markdown.  
team_payment_uid | string | Optional | none | Team payee UID; optional for non-team merchants.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
    
    

##  P2pCounterpartyUserInfoResponse

_P2pCounterpartyUserInfoResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | object | Optional | none | none  
↳ user_timest | string | Optional | none | User registration time (formatted string)  
↳ email_verified | string | Optional | none | Whether email is verified. `1`: yes; `0`: no.  
↳ verified | string | Optional | none | Whether KYC is completed. `1`: yes; `0`: no.  
↳ has_phone | string | Optional | none | Whether a phone number is bound. `1`: yes; `0`: no.  
↳ user_name | string | Optional | none | Username  
↳ user_note | string | Optional | none | User note information  
↳ complete_transactions | string | Optional | none | Total completed orders  
↳ paid_transactions | string | Optional | none | Number of completed buy orders  
↳ accepted_transactions | string | Optional | none | Number of completed sell orders  
↳ transactions_used_time | string | Optional | none | Average time to confirm receipt  
↳ cancelled_used_time_month | string | Optional | none | Cancellation time in last 30 days  
↳ complete_transactions_month | string | Optional | none | Number of completed orders in last 30 days  
↳ complete_rate_month | number | Optional | none | Completion rate in last 30 days  
↳ is_follow | integer | Optional | none | Whether you follow this user. `1`: yes; `0`: no.  
↳ have_traded | integer | Optional | none | Whether you have traded with this user before. `1`: yes; `0`: no.  
↳ biz_uid | string | Optional | none | Encrypted UID  
↳ registration_days | integer | Optional | none | Registration days  
↳ first_trade_days | integer | Optional | none | Days since first trade  
↳ trade_versatile | boolean | Optional | none | Single user or composite user  
version | string | Optional | none | none  
      
    
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
    
    

##  P2pTransactionActionResponse

_P2pTransactionActionResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | Response timestamp.  
method | string | Optional | none | Placeholder for request method.  
code | integer | Optional | none | Response code, 0 means success  
message | string | Optional | none | Response message  
data | object | Optional | none | Empty object on success.  
version | string | Optional | none | API version.  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {},
      "version": "string"
    }
    
    

##  GetTransactionDetailsRequest

Get`transaction details request`

Get `transaction details request`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
txid | integer | Required | none | Order ID  
channel | string | Optional | none | Channel tag: omit or empty for normal P2P; use `web3` for Web3 orders.  
      
    
    {
      "txid": 40000001,
      "channel": ""
    }
    
    

##  GetMyselfPaymentRequest

Get`payment method list request`

Get `payment method list request`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
fiat | string | Optional | none | Fiat currency; omit to return all available payment methods.  
      
    
    {
      "fiat": "USD"
    }
    
    

##  GetPendingTransactionListRequest

Get`pending transaction list request`

Get `pending transaction list request`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
crypto_currency | string | Required | none | Cryptocurrency symbol.  
fiat_currency | string | Required | none | Fiat currency  
order_tab | string | Optional | none | Order tab: `pending` in progress (`OPEN`, `PAID`, `LOCKED`, `TEMP`); `dispute` in dispute; default `pending`.  
select_type | string | Optional | none | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
status | string | Optional | none | Order status filter. `open` unpaid (`OPEN`); `paid` paid (`PAID`); `locked` locked (`LOCKED`);  
`dispute` in dispute; empty or omitted uses the default range for `order_tab`.  
txid | integer | Optional | none | Order ID  
start_time | integer | Optional | none | Start timestamp, default is 00:00 89 days ago  
end_time | integer | Optional | none | End timestamp, default is 23:59:59 today  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
    
    

##  P2pPaymentMethodsResponse

_P2pPaymentMethodsResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timestamp | number | Optional | none | none  
method | string | Optional | none | none  
code | integer | Optional | none | none  
message | string | Optional | none | none  
data | array | Optional | none | none  
↳ P2pPaymentMethodGroup | object | Optional | none | none  
↳ pay_type | string | Optional | none | Payment method type  
↳ pay_name | string | Optional | none | Payment method name  
↳ ids | array | Optional | none | User's currently bound payment method (primary key ID)  
↳ list | array | Optional | none | none  
↳ P2pPaymentMethodAccount | object | Optional | none | none  
↳ uid | integer | Optional | none | useruID  
↳ bankid | string | Optional | none | User's currently bound payment method (primary key ID)  
↳ nickname | integer | Optional | none | Cardholder UID  
↳ bankname | string | Optional | none | Bank name  
↳ bankbranch | string | Optional | none | Bank branch name  
↳ bankcity | string | Optional | none | Bank city  
↳ bankprov | string | Optional | none | Bank province  
↳ bankaddr | string | Optional | none | Bank card number or masked card number.  
↳ bankdesc | string | Optional | none | Bank note  
↳ hold_uid | integer | Optional | none | Cardholder UID  
↳ hold_username | string | Optional | none | Cardholder name  
↳ real_name | string | Optional | none | User verified display name.  
↳ id | string | Optional | none | User's currently bound payment method (primary key ID)  
↳ account_des | string | Optional | none | Payment method description  
↳ pay_type | string | Optional | none | Payment method type  
↳ file | string | Optional | none | Payment method file link  
↳ file_key | string | Optional | none | Payment method file key  
↳ account | string | Optional | none | Payment account or masked payment account.  
↳ memo | string | Optional | none | Payment method note  
↳ code | string | Optional | none | Payment method code  
↳ memo_ext | string | Optional | none | Payment method additional note  
↳ trade_tips | string | Optional | none | Payment method transaction information  
↳ version | string | Optional | none | none  
      
    
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
    
    

##  MyAdsListRequest

Get`my ads list request`

Get `my ads list request`

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
asset | string | Optional | none | Crypto asset; omit to skip asset filter.  
fiat_unit | string | Optional | none | Fiat currency; omit to skip fiat filter.  
trade_type | string | Optional | none | Ad side: `buy` for buy-crypto ads, `sell` for sell-crypto ads; omit for all sides.  
      
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }