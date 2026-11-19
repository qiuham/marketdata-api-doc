---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/withdrawal
api_type: Account
updated_at: 2026-11-19 19:01:11.265556
---

# Withdrawal

Withdrawal API

##  Withdraw🔒 Authenticated

POST`/withdrawals`

POST `/withdrawals`

_Withdraw_

If the recipient's on-chain address is also Gate, no transaction fee will be charged

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | LedgerRecord | Required | none  
id | body | string | Optional | Record ID  
txid | body | string | Optional | Hash record of the withdrawal  
withdraw_order_id | body | string | Optional | User-defined order number for withdrawal. Default is empty. When not empty, the specified user-defined order number record will be queried  
timestamp | body | string | Optional | Operation time  
amount | body | string | Required | Token amount  
currency | body | string | Required | Currency name  
address | body | string | Optional | Withdrawal address. Required for withdrawals  
memo | body | string | Optional | Additional remarks with regards to the withdrawal  
withdraw_id | body | string | Optional | Withdrawal record ID starts with 'w', such as: w1879219868. When withdraw_id is not empty, only this specific withdrawal record will be queried, and time-based querying will be disabled  
asset_class | body | string | Optional | Withdrawal record currency type, empty by default. Supports users to query withdrawal records in main area and innovation area on demand.  
Valid values: SPOT, PILOT  
  
SPOT: Main area  
PILOT: Innovation area  
status | body | string | Optional | Transaction status  
  
\- DONE: Completed  
\- CANCEL: Cancelled  
\- REQUEST: Requesting  
\- MANUAL: Pending manual review  
\- BCODE: GateCode operation  
\- EXTPEND: Sent, waiting for confirmation  
\- FAIL: Failed on chain, waiting for confirmation  
\- INVALID: Invalid order  
\- VERIFY: Verifying  
\- PROCES: Processing  
\- PEND: Processing  
\- DMOVE: Pending manual review  
\- REVIEW: Under review  
chain | body | string | Required | Name of the chain used in withdrawals  
  
####  Detailed descriptions

** asset_class**: Withdrawal record currency type, empty by default. Supports users to query withdrawal records in main area and innovation area on demand.  
Valid values: SPOT, PILOT  
  
SPOT: Main area  
PILOT: Innovation area

** status**: Transaction status  
  
\- DONE: Completed  
\- CANCEL: Cancelled  
\- REQUEST: Requesting  
\- MANUAL: Pending manual review  
\- BCODE: GateCode operation  
\- EXTPEND: Sent, waiting for confirmation  
\- FAIL: Failed on chain, waiting for confirmation  
\- INVALID: Invalid order  
\- VERIFY: Verifying  
\- PROCES: Processing  
\- PEND: Processing  
\- DMOVE: Pending manual review  
\- REVIEW: Under review

####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
LedgerRecord | required: ["currency","amount","chain"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Record ID  
txid | string | Optional | readOnly: true | Hash record of the withdrawal  
withdraw_order_id | string | Optional |  | User-defined order number for withdrawal. Default is empty. When not empty, the specified user-defined order number record will be queried  
timestamp | string | Optional | readOnly: true | Operation time  
amount | string | Required |  | Token amount  
currency | string | Required |  | Currency name  
address | string | Optional |  | Withdrawal address. Required for withdrawals  
memo | string | Optional |  | Additional remarks with regards to the withdrawal  
withdraw_id | string | Optional |  | Withdrawal record ID starts with 'w', such as: w1879219868. When withdraw_id is not empty, only this specific withdrawal record will be queried, and time-based querying will be disabled  
asset_class | string | Optional |  | Withdrawal record currency type, empty by default. Supports users to query withdrawal records in main area and innovation area on demand.  
Valid values: SPOT, PILOT  
  
SPOT: Main area  
PILOT: Innovation area  
status | string | Optional | readOnly: true | Transaction status  
  
\- DONE: Completed  
\- CANCEL: Cancelled  
\- REQUEST: Requesting  
\- MANUAL: Pending manual review  
\- BCODE: GateCode operation  
\- EXTPEND: Sent, waiting for confirmation  
\- FAIL: Failed on chain, waiting for confirmation  
\- INVALID: Invalid order  
\- VERIFY: Verifying  
\- PROCES: Processing  
\- PEND: Processing  
\- DMOVE: Pending manual review  
\- REVIEW: Under review  
chain | string | Required |  | Name of the chain used in withdrawals  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Withdrawal request accepted. Check withdrawal record status for processing result | LedgerRecord  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
LedgerRecord | required: ["currency","amount","chain"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Record ID  
txid | string | Optional | readOnly: true | Hash record of the withdrawal  
withdraw_order_id | string | Optional |  | User-defined order number for withdrawal. Default is empty. When not empty, the specified user-defined order number record will be queried  
timestamp | string | Optional | readOnly: true | Operation time  
amount | string | Required |  | Token amount  
currency | string | Required |  | Currency name  
address | string | Optional |  | Withdrawal address. Required for withdrawals  
memo | string | Optional |  | Additional remarks with regards to the withdrawal  
withdraw_id | string | Optional |  | Withdrawal record ID starts with 'w', such as: w1879219868. When withdraw_id is not empty, only this specific withdrawal record will be queried, and time-based querying will be disabled  
asset_class | string | Optional |  | Withdrawal record currency type, empty by default. Supports users to query withdrawal records in main area and innovation area on demand.  
Valid values: SPOT, PILOT  
  
SPOT: Main area  
PILOT: Innovation area  
status | string | Optional | readOnly: true | Transaction status  
  
\- DONE: Completed  
\- CANCEL: Cancelled  
\- REQUEST: Requesting  
\- MANUAL: Pending manual review  
\- BCODE: GateCode operation  
\- EXTPEND: Sent, waiting for confirmation  
\- FAIL: Failed on chain, waiting for confirmation  
\- INVALID: Invalid order  
\- VERIFY: Verifying  
\- PROCES: Processing  
\- PEND: Processing  
\- DMOVE: Pending manual review  
\- REVIEW: Under review  
chain | string | Required |  | Name of the chain used in withdrawals  
  
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
    
    url = '/withdrawals'
    query_param = ''
    body='{"withdraw_order_id":"order_123456","currency":"USDT","address":"1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs","amount":"222.61","memo":"","chain":"TRX"}'
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
    
    

> Body parameter
    
    
    {
      "withdraw_order_id": "order_123456",
      "currency": "USDT",
      "address": "1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs",
      "amount": "222.61",
      "memo": "",
      "chain": "TRX"
    }
    

> Example responses

> 200 Response
    
    
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
    

##  UID transfer🔒 Authenticated

POST`/withdrawals/push`

POST `/withdrawals/push`

_UID transfer_

Transfers between main spot accounts. Both parties cannot be sub-accounts

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | UidPushWithdrawal | Required | none  
receive_uid | body | integer(int64) | Required | Recipient UID  
currency | body | string | Required | Currency name  
amount | body | string | Required | Transfer amount  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
UidPushWithdrawal | required: ["receive_uid","currency","amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
receive_uid | integer(int64) | Required |  | Recipient UID  
currency | string | Required |  | Currency name  
amount | string | Required |  | Transfer amount  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request accepted. Check withdrawal record status for processing result | UidPushWithdrawalResp  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
UidPushWithdrawalResp |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID  
  
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
    
    url = '/withdrawals/push'
    query_param = ''
    body='{"receive_uid":12233,"currency":"USDT","amount":"1.1"}'
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
    
    

> Body parameter
    
    
    {
      "receive_uid": 12233,
      "currency": "USDT",
      "amount": "1.1"
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": "111"
    }
    

##  Cancel withdrawal with specified ID🔒 Authenticated

DELETE`/withdrawals/{withdrawal_id}`

DELETE `/withdrawals/{withdrawal_id}`

_Cancel withdrawal with specified ID_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
withdrawal_id | path | string | Required | none  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | Cancellation request accepted. Check record status for cancellation result | WithdrawalsDel  
  
### Response Schema

Status Code **202**

Type | Constraints  
---|---  
WithdrawalsDel | required: ["currency","amount","chain"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Record ID  
txid | string | Optional | readOnly: true | Hash record of the withdrawal  
timestamp | string | Optional | readOnly: true | Operation time  
amount | string | Required |  | Token amount  
currency | string | Required |  | Currency name  
address | string | Optional |  | Withdrawal address. Required for withdrawals  
memo | string | Optional |  | Additional remarks with regards to the withdrawal  
block_number | string | Optional | readOnly: true | Block Number  
status | string | Optional | readOnly: true | Transaction Status  
  
\- BCODE: Deposit Code Operation  
\- CANCEL: Cancelled  
\- CANCELPEND: Withdrawal Cancellation Pending  
\- DMOVE: Pending Manual Review  
\- DONE: Completed (Only considered truly on-chain when block_number > 0)  
\- EXTPEND: Sent and Waiting for Confirmation  
\- FAIL: On-Chain Failure Pending Confirmation  
\- FVERIFY: Facial Verification in Progress  
\- LOCKED: Wallet-Side Order Locked  
\- MANUAL: Pending Manual Review  
\- REJECT: Rejected  
\- REQUEST: Request in Progress  
\- REVIEW: Under Review  
chain | string | Required |  | Name of the chain used in withdrawals  
  
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
    
    url = '/withdrawals/210496'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 202 Response
    
    
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
    

#  Schemas

##  UidPushWithdrawal

Type | Constraints  
---|---  
object | required: ["receive_uid","currency","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
receive_uid | integer(int64) | Required |  | Recipient UID  
currency | string | Required |  | Currency name  
amount | string | Required |  | Transfer amount  
      
    
    {
      "receive_uid": 0,
      "currency": "string",
      "amount": "string"
    }
    
    

##  WithdrawalsDel

Type | Constraints  
---|---  
object | required: ["currency","amount","chain"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Record ID  
txid | string | Optional | readOnly: true | Hash record of the withdrawal  
timestamp | string | Optional | readOnly: true | Operation time  
amount | string | Required |  | Token amount  
currency | string | Required |  | Currency name  
address | string | Optional |  | Withdrawal address. Required for withdrawals  
memo | string | Optional |  | Additional remarks with regards to the withdrawal  
block_number | string | Optional | readOnly: true | Block Number  
status | string | Optional | readOnly: true | Transaction Status  
  
\- BCODE: Deposit Code Operation  
\- CANCEL: Cancelled  
\- CANCELPEND: Withdrawal Cancellation Pending  
\- DMOVE: Pending Manual Review  
\- DONE: Completed (Only considered truly on-chain when block_number > 0)  
\- EXTPEND: Sent and Waiting for Confirmation  
\- FAIL: On-Chain Failure Pending Confirmation  
\- FVERIFY: Facial Verification in Progress  
\- LOCKED: Wallet-Side Order Locked  
\- MANUAL: Pending Manual Review  
\- REJECT: Rejected  
\- REQUEST: Request in Progress  
\- REVIEW: Under Review  
chain | string | Required |  | Name of the chain used in withdrawals  
      
    
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
    
    

##  LedgerRecord

Type | Constraints  
---|---  
object | required: ["currency","amount","chain"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional | readOnly: true | Record ID  
txid | string | Optional | readOnly: true | Hash record of the withdrawal  
withdraw_order_id | string | Optional |  | User-defined order number for withdrawal. Default is empty. When not empty, the specified user-defined order number record will be queried  
timestamp | string | Optional | readOnly: true | Operation time  
amount | string | Required |  | Token amount  
currency | string | Required |  | Currency name  
address | string | Optional |  | Withdrawal address. Required for withdrawals  
memo | string | Optional |  | Additional remarks with regards to the withdrawal  
withdraw_id | string | Optional |  | Withdrawal record ID starts with 'w', such as: w1879219868. When withdraw_id is not empty, only this specific withdrawal record will be queried, and time-based querying will be disabled  
asset_class | string | Optional |  | Withdrawal record currency type, empty by default. Supports users to query withdrawal records in main area and innovation area on demand.  
Valid values: SPOT, PILOT  
  
SPOT: Main area  
PILOT: Innovation area  
status | string | Optional | readOnly: true | Transaction status  
  
\- DONE: Completed  
\- CANCEL: Cancelled  
\- REQUEST: Requesting  
\- MANUAL: Pending manual review  
\- BCODE: GateCode operation  
\- EXTPEND: Sent, waiting for confirmation  
\- FAIL: Failed on chain, waiting for confirmation  
\- INVALID: Invalid order  
\- VERIFY: Verifying  
\- PROCES: Processing  
\- PEND: Processing  
\- DMOVE: Pending manual review  
\- REVIEW: Under review  
chain | string | Required |  | Name of the chain used in withdrawals  
      
    
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

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Order ID  
      
    
    {
      "id": "string"
    }