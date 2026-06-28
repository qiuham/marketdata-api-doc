---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/wallet
api_type: Account
updated_at: 2026-05-27 20:16:21.378356
---

# Wallet

Wallet API

##  Query chains supported for specified currency

GET`/wallet/currency_chains`

GET `/wallet/currency_chains`

_Query chains supported for specified currency_

API operations are not supported for tokens with low liquidity or extremely low value. Please use the Web or App interface to query and process.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Required | Currency name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [CurrencyChain]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» chain | string | Chain name  
» name_cn | string | Chain name in Chinese  
» name_en | string | Chain name in English  
» contract_address | string | Smart contract address for the currency; if no address is available, it will be an empty string  
» is_disabled | integer(int32) | If it is disabled. 0 means NOT being disabled  
» is_deposit_disabled | integer(int32) | Is deposit disabled. 0 means not disabled  
» is_withdraw_disabled | integer(int32) | Is withdrawal disabled. 0 means not disabled  
» decimal | string | Withdrawal precision  
» is_tag | integer | Whether to Include Tag  
  
This operation does not require authentication 

Code samples
    
    
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Generate currency deposit address🔒 Authenticated

GET`/wallet/deposit_address`

GET `/wallet/deposit_address`

_Generate currency deposit address_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Required | Currency name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Address successfully generated

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Address successfully generated | DepositAddress  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» currency | string | Currency detail  
» address | string | Deposit address  
» min_deposit_amount | string | Minimum Deposit Amount  
» multichain_addresses | array | none  
»» MultiChainAddressItem | object | none  
»»» chain | string | Name of the chain  
»»» address | string | Deposit address  
»»» payment_id | string | Notes that some currencies required(e.g., Tag, Memo) when depositing  
»»» payment_name | string | Note type, `Tag` or `Memo`  
»»» obtain_failed | integer | The obtain failed status- 0: address successfully obtained- 1: failed to obtain address  
»»» min_confirms | integer | Minimum Confirmation Count  
  
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
    
    url = '/wallet/deposit_address'
    query_param = 'currency=USDT'
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Get withdrawal records🔒 Authenticated

GET`/wallet/withdrawals`

GET `/wallet/withdrawals`

Get `withdrawal records`

Record query time range cannot exceed 30 days

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Specify the currency. If not specified, returns all currencies  
withdraw_id | query | string | Optional | Withdrawal record ID starts with 'w', such as: w1879219868. When withdraw_id is not empty, only this specific withdrawal record will be queried, and time-based querying will be disabled  
asset_class | query | string | Optional | Currency type of withdrawal record, empty by default. Supports querying withdrawal records in main zone and innovation zone on demand.  
Value range: SPOT, PILOT  
  
SPOT: Main Zone  
PILOT: Innovation Zone  
withdraw_order_id | query | string | Optional | User-defined order number for withdrawal. Default is empty. When not empty, the specified user-defined order number record will be queried  
from | query | integer(int64) | Optional | Start time for querying records. If not specified, defaults to 7 days before current time  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
####  Detailed descriptions

**asset_class** : Currency type of withdrawal record, empty by default. Supports querying withdrawal records in main zone and innovation zone on demand.  
Value range: SPOT, PILOT  
  
SPOT: Main Zone  
PILOT: Innovation Zone

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [WithdrawalRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | string | Record ID  
» txid | string | Hash record of the withdrawal  
» block_number | string | Block Number  
» withdraw_order_id | string | Client order id, up to 32 length and can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
» timestamp | string | Operation time  
» amount | string | Token amount  
» fee | string | fee  
» currency | string | Currency name  
» address | string | Withdrawal address  
» type | string | Business Type  
» fail_reason | string | Reason for withdrawal failure. Has a value when status = CANCEL, empty for all other statuses  
» timestamp2 | string | Withdrawal final time, i.e.: withdrawal cancellation time or withdrawal success time  
When status = CANCEL, corresponds to cancellation time  
When status = DONE, it is the withdrawal success time  
» memo | string | Additional remarks with regards to the withdrawal  
» status | string | Transaction Status  
  
\- BCODE: Deposit Code Operation  
\- CANCEL: Cancelled  
\- CANCELPEND: Withdrawal Cancellation Pending  
\- DONE: Completed  
\- EXTPEND: Sent and Waiting for Confirmation  
\- FAIL: On-Chain Failure Pending Confirmation  
\- FVERIFY: Facial Verification in Progress  
\- LOCKED: Wallet-Side Order Locked  
\- MANUAL: Pending Manual Review  
\- REJECT: Rejected  
\- REQUEST: Request in Progress  
\- REVIEW: Under Review  
» chain | string | Name of the chain used in withdrawals  
  
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
    
    url = '/wallet/withdrawals'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Get deposit records🔒 Authenticated

GET`/wallet/deposits`

GET `/wallet/deposits`

Get `deposit records`

Record query time range cannot exceed 30 days

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Specify the currency. If not specified, returns all currencies  
from | query | integer(int64) | Optional | Start time for querying records. If not specified, defaults to 7 days before current time  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
limit | query | integer | Optional | Maximum number of entries returned in the list, limited to 500 transactions  
offset | query | integer | Optional | List offset, starting from 0  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [DepositRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | string | Record ID  
» txid | string | Hash record of the withdrawal  
» timestamp | string | Operation time  
» amount | string | Token amount  
» currency | string | Currency name  
» address | string | Withdrawal address. Required for withdrawals  
» memo | string | Additional remarks with regards to the withdrawal  
» status | string | Transaction Status  
  
\- BLOCKED: Deposit Blocked  
\- DEP_CREDITED: Deposit Credited, Withdrawal Pending Unlock  
\- DONE: Funds Credited to Spot Account  
\- INVALID: Invalid Transaction  
\- MANUAL: Manual Review Required  
\- PEND: Processing  
\- REVIEW: Under Compliance Review  
\- TRACK: Tracking Block Confirmations, Pending Spot Account Credit  
» chain | string | Name of the chain used in withdrawals  
  
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
    
    url = '/wallet/deposits'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Transfer between trading accounts🔒 Authenticated

POST`/wallet/transfers`

POST `/wallet/transfers`

_Transfer between trading accounts_

Balance transfers between personal trading accounts. Currently supports the following transfer operations:

  1. Spot account - Margin account
  2. Spot account - Perpetual futures account
  3. Spot account - Delivery futures account
  4. Spot account - Options account

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | Transfer | Required | none  
↳ currency | body | string | Required | Transfer currency name. For contract accounts, `currency` can be set to `POINT` (points) or supported settlement currencies (e.g., `BTC`, `USDT`)  
↳ from | body | string | Required | Account to transfer from  
↳ to | body | string | Required | Account to transfer to  
↳ amount | body | string | Required | Transfer Amount, supports up to 8 decimal places, must be greater than 0  
↳ currency_pair | body | string | Optional | Margin trading pair. Required when transferring to or from margin account  
↳ settle | body | string | Optional | Contract settlement currency. Required when transferring to or from contract account  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
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
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Transfer operation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Transfer operation successful | TransactionID  
  
### Response Schema

Status Code **200**

_TransactionID_

Name | Type | Description  
---|---|---  
» tx_id | integer(int64) | Order ID  
  
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
    
    url = '/wallet/transfers'
    query_param = ''
    body='{"currency":"BTC","from":"spot","to":"margin","amount":"1","currency_pair":"BTC_USDT","settle":""}'
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
    
    

> Body parameter
    
    
    {
      "currency": "BTC",
      "from": "spot",
      "to": "margin",
      "amount": "1",
      "currency_pair": "BTC_USDT",
      "settle": ""
    }
    

> Example responses

> 200 Response
    
    
    {
      "tx_id": 59636381286
    }
    

##  Get transfer records between main and sub accounts🔒 Authenticated

GET`/wallet/sub_account_transfers`

GET `/wallet/sub_account_transfers`

Get `transfer records between main and sub accounts`

Record query time range cannot exceed 30 days

> Note: Only records after 2020-04-10 can be retrieved

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
sub_uid | query | string | Optional | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts  
from | query | integer(int64) | Optional | Start time for querying records. If not specified, defaults to 7 days before current time  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SubAccountTransferRecordItem]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» timest | string | Transfer timestamp  
» uid | string | Main account user ID  
» sub_account | string | Sub account user ID  
» sub_account_type | string | Target sub-account trading account: spot - spot account, futures - perpetual contract account, delivery - delivery contract account, options - options account  
» currency | string | Transfer currency name  
» amount | string | Transfer Amount  
» direction | string | Transfer direction: to - transfer into sub-account, from - transfer out from sub-account  
» source | string | Source of the transfer operation  
» client_order_id | string | Customer-defined ID to prevent duplicate transfers. Can be a combination of letters (case-sensitive), numbers, hyphens '-', and underscores '_'. Can be pure letters or pure numbers with length between 1-64 characters  
» status | string | Sub-account transfer record status, currently only 'success'  
  
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
    
    url = '/wallet/sub_account_transfers'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Transfer between main and sub accounts🔒 Authenticated

POST`/wallet/sub_account_transfers`

POST `/wallet/sub_account_transfers`

_Transfer between main and sub accounts_

Supports transfers to/from sub-account's spot or futures accounts. Note that regardless of which sub-account is operated, only the main account's spot account is used

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | SubAccountTransfer | Required | none  
↳ sub_account | body | string | Required | Sub account user ID  
↳ sub_account_type | body | string | Optional | Target sub-account trading account: spot - spot account, futures - perpetual contract account, delivery - delivery contract account, options - options account  
↳ currency | body | string | Required | Transfer currency name  
↳ amount | body | string | Required | Transfer Amount, supports up to 8 decimal places, must be greater than 0  
↳ direction | body | string | Required | Transfer direction: to - transfer into sub-account, from - transfer out from sub-account  
↳ client_order_id | body | string | Optional | Customer-defined ID to prevent duplicate transfers. Can be a combination of letters (case-sensitive), numbers, hyphens '-', and underscores '_'. Can be pure letters or pure numbers with length between 1-64 characters  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Transfer operation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Transfer operation successful | TransactionID  
  
### Response Schema

Status Code **200**

_TransactionID_

Name | Type | Description  
---|---|---  
» tx_id | integer(int64) | Order ID  
  
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
    
    url = '/wallet/sub_account_transfers'
    query_param = ''
    body='{"sub_account":"10002","sub_account_type":"spot","currency":"BTC","amount":"1","direction":"to","client_order_id":"da3ce7a088c8b0372b741419c7829033"}'
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
    
    

> Body parameter
    
    
    {
      "sub_account": "10002",
      "sub_account_type": "spot",
      "currency": "BTC",
      "amount": "1",
      "direction": "to",
      "client_order_id": "da3ce7a088c8b0372b741419c7829033"
    }
    

> Example responses

> 200 Response
    
    
    {
      "tx_id": 59636381286
    }
    

##  Transfer between sub-accounts🔒 Authenticated

POST`/wallet/sub_account_to_sub_account`

POST `/wallet/sub_account_to_sub_account`

_Transfer between sub-accounts_

Supports balance transfers between two sub-accounts under the same main account. You can use either the main account's API Key or the source sub-account's API Key to perform the operation

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | SubAccountToSubAccount | Required | none  
↳ currency | body | string | Required | Transfer currency name  
↳ sub_account_type | body | string | Optional | Transfer from account (deprecated, use `sub_account_from_type` and `sub_account_to_type` instead)  
↳ sub_account_from | body | string | Required | Transfer from the user id of the sub-account  
↳ sub_account_from_type | body | string | Required | Source sub-account trading account: spot - spot account, futures - perpetual contract account, delivery - delivery contract account  
↳ sub_account_to | body | string | Required | Transfer to the user id of the sub-account  
↳ sub_account_to_type | body | string | Required | Target sub-account trading account: spot - spot account, futures - perpetual contract account, delivery - delivery contract account  
↳ amount | body | string | Required | Transfer Amount, supports up to 8 decimal places, must be greater than 0  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Transfer operation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Transfer operation successful | TransactionID  
  
### Response Schema

Status Code **200**

_TransactionID_

Name | Type | Description  
---|---|---  
» tx_id | integer(int64) | Order ID  
  
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
    
    url = '/wallet/sub_account_to_sub_account'
    query_param = ''
    body='{"currency":"usdt","sub_account_from":"10001","sub_account_from_type":"spot","sub_account_to":"10002","sub_account_to_type":"spot","amount":"1"}'
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
    
    

> Body parameter
    
    
    {
      "currency": "usdt",
      "sub_account_from": "10001",
      "sub_account_from_type": "spot",
      "sub_account_to": "10002",
      "sub_account_to_type": "spot",
      "amount": "1"
    }
    

> Example responses

> 200 Response
    
    
    {
      "tx_id": 59636381286
    }
    

##  Main-Sub Account Transfer Status Query🔒 Authenticated

GET`/wallet/order_status`

GET `/wallet/order_status`

_Main-Sub Account Transfer Status Query_

Supports querying Main-Sub Account Transfer Status based on user-defined client_order_id or tx_id returned by the transfer interface

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
client_order_id | query | string | Optional | Customer-defined ID to prevent duplicate transfers. Can be a combination of letters (case-sensitive), numbers, hyphens '-', and underscores '_'. Can be pure letters or pure numbers with length between 1-64 characters  
tx_id | query | string | Optional | Transfer operation number, cannot be empty at the same time as client_order_id  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Main-Sub Account Transfer Status Retrieval Successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Main-Sub Account Transfer Status Retrieval Successful | TransferOrderStatus  
  
### Response Schema

Status Code **200**

_TransferOrderStatus_

Name | Type | Description  
---|---|---  
» tx_id | string | Order ID  
» status | string | Transfer status: PENDING - Processing, SUCCESS - Transfer successful, FAIL - Transfer failed, PARTIAL_SUCCESS - Partially successful (this status appears when transferring between sub-accounts)  
  
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
    
    url = '/wallet/order_status'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
    {
      "tx_id": "59636381286",
      "status": "SUCCESS"
    }
    

##  Query withdrawal status🔒 Authenticated

GET`/wallet/withdraw_status`

GET `/wallet/withdraw_status`

_Query withdrawal status_

API operations are not supported for tokens with low liquidity or extremely low value. Please use the Web or App interface to query and process.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [WithdrawStatus]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» currency | string | Currency  
» name | string | Currency name  
» name_cn | string | Currency Chinese name  
» deposit | string | Deposit fee  
» withdraw_percent | string | Withdrawal fee rate percentage  
» withdraw_fix | string | Fixed withdrawal fee  
» withdraw_day_limit | string | Daily allowed withdrawal amount  
» withdraw_amount_mini | string | Minimum withdrawal amount  
» withdraw_day_limit_remain | string | Daily withdrawal amount left  
» withdraw_eachtime_limit | string | Maximum amount for each withdrawal  
» withdraw_fix_on_chains | object | Fixed withdrawal fee on multiple chains  
»» **additionalProperties** | string | none  
» withdraw_percent_on_chains | object | Percentage withdrawal fee on multiple chains  
»» **additionalProperties** | string | none  
  
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
    
    url = '/wallet/withdraw_status'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Query sub-account balance information🔒 Authenticated

GET`/wallet/sub_account_balances`

GET `/wallet/sub_account_balances`

_Query sub-account balance information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
sub_uid | query | string | Optional | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of records returned. Default 20, max 100.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SubAccountBalance]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» uid | string | User ID  
» available | object | Available balances of currencies  
»» **additionalProperties** | string | none  
» locking | object | Locked amount by currency  
»» **additionalProperties** | string | none  
  
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
    
    url = '/wallet/sub_account_balances'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Query sub-account isolated margin account balance information🔒 Authenticated

GET`/wallet/sub_account_margin_balances`

GET `/wallet/sub_account_margin_balances`

_Query sub-account isolated margin account balance information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
sub_uid | query | string | Optional | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SubAccountMarginBalance]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» uid | string | User ID  
» available | array | Margin account balances  
»» _None_ | object | Margin account information for a trading pair. `base` corresponds to base currency account information, `quote` corresponds to quote currency account information  
»»» currency_pair | string | Currency pair  
»»» account_type | string | Account Type mmr: maintenance margin rate account;inactive: market not activated  
»»» leverage | string | User's current market leverage multiplier  
»»» locked | boolean | Whether the account is locked  
»»» risk | string | Deprecated  
»»» mmr | string | Current Maintenance Margin Rate of the account  
»»» base | SubAccountMarginBalance/properties/available/items/properties/base | Currency account information  
»»»» currency | string | Currency name  
»»»» available | string | Amount available for margin trading, available = margin + borrowed  
»»»» locked | string | Frozen funds, such as amounts already placed in margin market for order trading  
»»»» borrowed | string | Borrowed funds  
»»»» interest | string | Unpaid interest  
»»» quote | SubAccountMarginBalance/properties/available/items/properties/base | Currency account information  
»»»» currency | string | Currency name  
»»»» available | string | Amount available for margin trading, available = margin + borrowed  
»»»» locked | string | Frozen funds, such as amounts already placed in margin market for order trading  
»»»» borrowed | string | Borrowed funds  
»»»» interest | string | Unpaid interest  
  
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
    
    url = '/wallet/sub_account_margin_balances'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Query sub-account perpetual futures account balance information🔒 Authenticated

GET`/wallet/sub_account_futures_balances`

GET `/wallet/sub_account_futures_balances`

_Query sub-account perpetual futures account balance information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
sub_uid | query | string | Optional | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts  
settle | query | string | Optional | Query balance of specified settlement currency  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SubAccountFuturesBalance]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» uid | string | User ID  
» available | object | Futures account balances  
»» **additionalProperties** | object | none  
»»» total | string | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
»»» unrealised_pnl | string | Unrealized PNL  
»»» position_margin | string | Deprecated  
»»» order_margin | string | initial margin of all open orders  
»»» available | string | Refers to the available withdrawal or trading amount in per-position, specifically the per-position available balance under the unified account that includes the credit line (which incorporates trial funds; since trial funds cannot be withdrawn, the actual withdrawal amount needs to deduct the trial fund portion when processing withdrawals)  
»»» point | string | Point card amount  
»»» currency | string | Settlement currency  
»»» in_dual_mode | boolean | Whether Hedge Mode is enabled  
»»» enable_credit | boolean | Whether portfolio margin account mode is enabled  
»»» position_initial_margin | string | Initial margin occupied by positions, applicable to unified account mode  
»»» maintenance_margin | string | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode  
»»» bonus | string | Bonus  
»»» enable_evolved_classic | boolean | Deprecated  
»»» cross_order_margin | string | Cross margin order margin, applicable to new classic account margin mode  
»»» cross_initial_margin | string | Cross margin initial margin, applicable to new classic account margin mode  
»»» cross_maintenance_margin | string | Cross margin maintenance margin, applicable to new classic account margin mode  
»»» cross_unrealised_pnl | string | Cross margin unrealized P&L, applicable to new classic account margin mode  
»»» cross_available | string | Cross margin available balance, applicable to new classic account margin mode  
»»» cross_margin_balance | string | Cross margin balance, applicable to new classic account margin mode  
»»» cross_mmr | string | Cross margin maintenance margin rate, applicable to new classic account margin mode  
»»» cross_imr | string | Cross margin initial margin rate, applicable to new classic account margin mode  
»»» isolated_position_margin | string | Isolated position margin, applicable to new classic account margin mode  
»»» enable_new_dual_mode | boolean | Deprecated  
»»» margin_mode | integer | Margin mode of the account  
0: classic future account or Classic Spot Margin Mode of unified account;  
1: Multi-Currency Margin Mode;  
2: Portoforlio Margin Mode;  
3: Single-Currency Margin Mode  
»»» enable_tiered_mm | boolean | Whether to enable tiered maintenance margin calculation  
»»» enable_dual_plus | boolean | Whether to Support Split Position Mode  
»»» position_mode | string | Position Holding Mode single - Single Direction Position, dual - Dual Direction Position, dual_plus - Split Position  
»»» history | object | Statistical data  
»»»» dnw | string | total amount of deposit and withdraw  
»»»» pnl | string | total amount of trading profit and loss  
»»»» fee | string | total amount of fee  
»»»» refr | string | total amount of referrer rebates  
»»»» fund | string | total amount of funding costs  
»»»» point_dnw | string | total amount of point deposit and withdraw  
»»»» point_fee | string | total amount of point fee  
»»»» point_refr | string | total amount of referrer rebates of point fee  
»»»» bonus_dnw | string | total amount of perpetual contract bonus transfer  
»»»» bonus_offset | string | total amount of perpetual contract bonus deduction  
»»»» cross_settle | string | Represents the value of profit settlement from the futures account to the spot account under Unified Account Mode. Negative values indicate settlement from futures to spot, while positive values indicate settlement from spot to futures. This value is cumulative.  
  
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
    
    url = '/wallet/sub_account_futures_balances'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Query sub-account cross margin account balance information🔒 Authenticated

GET`/wallet/sub_account_cross_margin_balances`

GET `/wallet/sub_account_cross_margin_balances`

_Query sub-account cross margin account balance information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
sub_uid | query | string | Optional | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SubAccountCrossMarginBalance]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» uid | string | User ID  
» available | object | none  
»» user_id | integer(int64) | Cross margin account user ID. 0 means this sub-account has not yet opened a cross margin account  
»» locked | boolean | Whether the account is locked  
»» balances | object | none  
»»» CrossMarginBalance | object | none  
»»»» available | string | Available balance  
»»»» freeze | string | Locked balance  
»»»» borrowed | string | Borrowed balance  
»»»» interest | string | Unpaid interest  
»»» total | string | Total account value in USDT, i.e., the sum of all currencies' `(available+freeze)*price*discount`  
»»» borrowed | string | Total borrowed value in USDT, i.e., the sum of all currencies' `borrowed*price*discount`  
»»» borrowed_net | string | Total borrowed value in USDT * leverage factor  
»»» net | string | Total net assets in USDT  
»»» leverage | string | Position leverage  
»»» interest | string | Total unpaid interest in USDT, i.e., the sum of all currencies' `interest*price*discount`  
»»» risk | string | Risk rate. When it falls below 110%, liquidation will be triggered. Calculation formula: `total / (borrowed+interest)`  
»»» total_initial_margin | string | Total initial margin  
»»» total_margin_balance | string | Total margin balance  
»»» total_maintenance_margin | string | Total maintenance margin  
»»» total_initial_margin_rate | string | Total initial margin rate  
»»» total_maintenance_margin_rate | string | Total maintenance margin rate  
»»» total_available_margin | string | Total available margin  
  
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
    
    url = '/wallet/sub_account_cross_margin_balances'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Query withdrawal address whitelist🔒 Authenticated

GET`/wallet/saved_address`

GET `/wallet/saved_address`

_Query withdrawal address whitelist_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Required | Currency  
chain | query | string | Optional | Chain name  
limit | query | string | Optional | Maximum number returned, up to 100  
page | query | integer | Optional | page number  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SavedAddress]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» currency | string | Currency  
» chain | string | Chain name  
» address | string | Address  
» name | string | Name  
» tag | string | Tag  
» verified | string | Whether to pass the verification 0-unverified, 1-verified  
  
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
    
    url = '/wallet/saved_address'
    query_param = 'currency=USDT'
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Query personal trading fees🔒 Authenticated

GET`/wallet/fee`

GET `/wallet/fee`

_Query personal trading fees_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Specify currency pair to get more accurate fee settings.  
  
This field is optional. Usually fee settings are the same for all currency pairs.  
settle | query | string | Optional | Specify the settlement currency of the contract to get more accurate fee settings.  
  
This field is optional. Generally, the fee settings for all settlement currencies are the same.  
  
####  Detailed descriptions

**currency_pair** : Specify currency pair to get more accurate fee settings.  
  
This field is optional. Usually fee settings are the same for all currency pairs.

**settle** : Specify the settlement currency of the contract to get more accurate fee settings.  
  
This field is optional. Generally, the fee settings for all settlement currencies are the same.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
settle | BTC  
settle | USDT  
settle | USD  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | TradeFee  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» user_id | integer(int64) | User ID  
» taker_fee | string | spot taker fee rate  
» maker_fee | string | spot maker fee rate  
» rpi_maker_fee | string | spot RPI MM maker fee rate  
» gt_discount | boolean | Whether GT deduction discount is enabled  
» gt_taker_fee | string | Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  
» gt_maker_fee | string | Maker fee rate with GT deduction. Returns 0 if GT deduction is disabled  
» loan_fee | string | Loan fee rate of margin lending  
» point_type | string | Point card type: 0 - Original version, 1 - New version since 202009  
» futures_taker_fee | string | Perpetual contract taker fee rate  
» futures_maker_fee | string | Perpetual contract maker fee rate  
» futures_rpi_maker_fee | string | contract RPI MM maker fee rate  
» delivery_taker_fee | string | Delivery contract taker fee rate  
» delivery_maker_fee | string | Delivery contract maker fee rate  
» debit_fee | integer | Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  
» rpi_mm | integer | RPI MM Level  
  
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
    
    url = '/wallet/fee'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Query personal account totals🔒 Authenticated

GET`/wallet/total_balance`

GET `/wallet/total_balance`

_Query personal account totals_

This query endpoint returns the total _estimated value_ of all currencies in each account converted to the input currency. Exchange rates and related account balance information may be cached for up to 1 minute. It is not recommended to use this interface data for real-time calculations.

For real-time calculations, query the corresponding balance interface based on account type, such as:

  * `GET /spot/accounts` to query spot account
  * `GET /margin/accounts` to query margin account
  * `GET /futures/{settle}/accounts` to query futures account

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Target currency type for statistical conversion. Accepts BTC, CNY, USD, and USDT. USDT is the default value  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Request is valid and successfully returned

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Request is valid and successfully returned | TotalBalance  
  
### Response Schema

Status Code **200**

_User's total balance information_

Name | Type | Description  
---|---|---  
» total | TotalBalance/properties/total | Total balances calculated with specified currency unit  
»» amount | string | Account total balance amount  
»» currency | string | Currency  
»» unrealised_pnl | string | Unrealised_pnl, this field will only appear in futures, options, delivery, and total accounts  
»» borrowed | string | Total borrowed amount, this field will only appear in margin and cross_margin accounts  
» details | object | Total Balances of All Accounts  
  
\- cross_margin: Cross Margin Account  
\- spot: Spot Account  
\- finance: Finance Account  
\- margin: Margin Account  
\- quant: Quantitative Account  
\- futures: Futures Account (Perpetual Contracts)  
\- delivery: Delivery Account (Delivery Contracts)  
\- warrant: Warrant Account  
\- cbbc: CBBC Account (Covered Bull/Bear Contract)  
\- meme_box: Alpha Account  
\- options: Options Account  
\- payment: Payment Account  
»» **additionalProperties** | TotalBalance/properties/total | Total balances calculated with specified currency unit  
»»» amount | string | Account total balance amount  
»»» currency | string | Currency  
»»» unrealised_pnl | string | Unrealised_pnl, this field will only appear in futures, options, delivery, and total accounts  
»»» borrowed | string | Total borrowed amount, this field will only appear in margin and cross_margin accounts  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
    
    url = '/wallet/total_balance'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Get list of convertible small balance currencies🔒 Authenticated

GET`/wallet/small_balance`

GET `/wallet/small_balance`

Get `list of convertible small balance currencies`

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | [SmallBalance]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Small Balance Conversion]  
» _None_ | SmallBalance | Small Balance Conversion  
»» currency | string | Currency  
»» available_balance | string | Available balance  
»» estimated_as_btc | string | Estimated as BTC  
»» convertible_to_gt | string | Estimated conversion to GT  
  
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
    
    url = '/wallet/small_balance'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Convert small balance currency🔒 Authenticated

POST`/wallet/small_balance`

POST `/wallet/small_balance`

_Convert small balance currency_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | ConvertSmallBalance | Required | none  
↳ currency | body | array | Optional | Currency to be converted  
↳ is_all | body | boolean | Optional | Whether to convert all  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | None  
  
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
    
    url = '/wallet/small_balance'
    query_param = ''
    body='{"currency":["FLOKI","MBLK"],"is_all":true}'
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
    
    

> Body parameter
    
    
    {
      "currency": [
        "FLOKI",
        "MBLK"
      ],
      "is_all": true
    }
    

##  Get convertible small balance currency history🔒 Authenticated

GET`/wallet/small_balance_history`

GET `/wallet/small_balance_history`

Get `convertible small balance currency history`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Currency to convert  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | [SmallBalanceHistory]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Small Balance Conversion]  
» _None_ | SmallBalanceHistory | Small Balance Conversion  
»» id | string | Order ID  
»» currency | string | Currency  
»» amount | string | Swap Amount  
»» gt_amount | string | GT amount  
»» create_time | integer(int64) | Exchange time (in seconds)  
  
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
    
    url = '/wallet/small_balance_history'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Get UID transfer history🔒 Authenticated

GET`/wallet/push`

GET `/wallet/push`

Get `UID transfer history`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
id | query | integer(int32) | Optional | Order ID  
from | query | integer(int32) | Optional | Start time for querying records. If not specified, defaults to 7 days before the current time. Unix timestamp in seconds  
to | query | integer(int32) | Optional | End time for querying records. If not specified, defaults to the current time. Unix timestamp in seconds  
limit | query | integer(int32) | Optional | Maximum number of items returned in the list, default value is 100  
offset | query | integer(int32) | Optional | List offset, starting from 0  
transaction_type | query | string | Optional | Order type returned in the list: `withdraw`, `deposit`. Default is `withdraw`.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | [UidPushOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int64) | Order ID  
» push_uid | integer(int64) | Initiator User ID  
» receive_uid | integer(int64) | Recipient User ID  
» currency | string | Currency name  
» amount | string | Transfer amount  
» create_time | integer(int64) | Created time  
» status | string | Withdrawal status:  
  
\- CREATING: Creating  
\- PENDING: Waiting for recipient (Please contact the recipient to accept the transfer on Gate official website)  
\- CANCELLING: Cancelling  
\- CANCELLED: Cancelled  
\- REFUSING: Refusing  
\- REFUSED: Refused  
\- RECEIVING: Receiving  
\- RECEIVED: Success  
» message | string | PENDING reason tips  
» transaction_type | string | Order Type  
  
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
    
    url = '/wallet/push'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> 200 Response
    
    
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
    

##  Retrieve the list of low-liquidity or low-cap tokens🔒 Authenticated

GET`/wallet/getLowCapExchangeList`

GET `/wallet/getLowCapExchangeList`

_Retrieve the list of low-liquidity or low-cap tokens_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Returns a string array on success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Returns a string array on success | [string]  
  
### Response Schema

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
    
    url = '/wallet/getLowCapExchangeList'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
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
    
    

> Example responses

> Returns a string array on success
    
    
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
    

#  Schemas

##  WithdrawStatus

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency  
name | string | Optional | none | Currency name  
name_cn | string | Optional | none | Currency Chinese name  
deposit | string | Optional | none | Deposit fee  
withdraw_percent | string | Optional | none | Withdrawal fee rate percentage  
withdraw_fix | string | Optional | none | Fixed withdrawal fee  
withdraw_day_limit | string | Optional | none | Daily allowed withdrawal amount  
withdraw_amount_mini | string | Optional | none | Minimum withdrawal amount  
withdraw_day_limit_remain | string | Optional | none | Daily withdrawal amount left  
withdraw_eachtime_limit | string | Optional | none | Maximum amount for each withdrawal  
withdraw_fix_on_chains | object | Optional | none | Fixed withdrawal fee on multiple chains  
↳ additionalProperties | string | Optional | none | none  
withdraw_percent_on_chains | object | Optional | none | Percentage withdrawal fee on multiple chains  
↳ additionalProperties | string | Optional | none | none  
      
    
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
    
    

##  SavedAddress

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency  
chain | string | Optional | none | Chain name  
address | string | Optional | none | Address  
name | string | Optional | none | Name  
tag | string | Optional | none | Tag  
verified | string | Optional | none | Whether to pass the verification 0-unverified, 1-verified  
      
    
    {
      "currency": "string",
      "chain": "string",
      "address": "string",
      "name": "string",
      "tag": "string",
      "verified": "string"
    }
    
    

##  SubAccountMarginBalance

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
uid | string | Optional | none | User ID  
available | array | Optional | none | Margin account balances  
↳ None | object | Optional | none | Margin account information for a trading pair. `base` corresponds to base currency account information, `quote` corresponds to quote currency account information  
↳ currency_pair | string | Optional | none | Currency pair  
↳ account_type | string | Optional | none | Account Type mmr: maintenance margin rate account;inactive: market not activated  
↳ leverage | string | Optional | none | User's current market leverage multiplier  
↳ locked | boolean | Optional | none | Whether the account is locked  
↳ risk | string | Optional | none | Deprecated  
↳ mmr | string | Optional | none | Current Maintenance Margin Rate of the account  
↳ base | object | Optional | none | Currency account information  
↳ currency | string | Optional | none | Currency name  
↳ available | string | Optional | none | Amount available for margin trading, available = margin + borrowed  
↳ locked | string | Optional | none | Frozen funds, such as amounts already placed in margin market for order trading  
↳ borrowed | string | Optional | none | Borrowed funds  
↳ interest | string | Optional | none | Unpaid interest  
↳ quote | SubAccountMarginBalance/properties/available/items/properties/base | Optional | none | Currency account information  
      
    
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
    
    

##  SubAccountTransferRecordItem

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
timest | string | Optional | read-only | Transfer timestamp  
uid | string | Optional | read-only | Main account user ID  
sub_account | string | Required | none | Sub account user ID  
sub_account_type | string | Optional | none | Target sub-account trading account: spot - spot account, futures - perpetual contract account, delivery - delivery contract account, options - options account  
currency | string | Required | none | Transfer currency name  
amount | string | Required | none | Transfer Amount  
direction | string | Required | none | Transfer direction: to - transfer into sub-account, from - transfer out from sub-account  
source | string | Optional | read-only | Source of the transfer operation  
client_order_id | string | Optional | none | Customer-defined ID to prevent duplicate transfers. Can be a combination of letters (case-sensitive), numbers, hyphens '-', and underscores '_'. Can be pure letters or pure numbers with length between 1-64 characters  
status | string | Optional | none | Sub-account transfer record status, currently only 'success'  
      
    
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
    
    

##  SubAccountFuturesBalance

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
uid | string | Optional | none | User ID  
available | object | Optional | none | Futures account balances  
↳ additionalProperties | object | Optional | none | none  
↳ total | string | Optional | none | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
↳ unrealised_pnl | string | Optional | none | Unrealized PNL  
↳ position_margin | string | Optional | none | Deprecated  
↳ order_margin | string | Optional | none | initial margin of all open orders  
↳ available | string | Optional | none | Refers to the available withdrawal or trading amount in per-position, specifically the per-position available balance under the unified account that includes the credit line (which incorporates trial funds; since trial funds cannot be withdrawn, the actual withdrawal amount needs to deduct the trial fund portion when processing withdrawals)  
↳ point | string | Optional | none | Point card amount  
↳ currency | string | Optional | none | Settlement currency  
↳ in_dual_mode | boolean | Optional | none | Whether Hedge Mode is enabled  
↳ enable_credit | boolean | Optional | none | Whether portfolio margin account mode is enabled  
↳ position_initial_margin | string | Optional | none | Initial margin occupied by positions, applicable to unified account mode  
↳ maintenance_margin | string | Optional | none | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode  
↳ bonus | string | Optional | none | Bonus  
↳ enable_evolved_classic | boolean | Optional | none | Deprecated  
↳ cross_order_margin | string | Optional | none | Cross margin order margin, applicable to new classic account margin mode  
↳ cross_initial_margin | string | Optional | none | Cross margin initial margin, applicable to new classic account margin mode  
↳ cross_maintenance_margin | string | Optional | none | Cross margin maintenance margin, applicable to new classic account margin mode  
↳ cross_unrealised_pnl | string | Optional | none | Cross margin unrealized P&L, applicable to new classic account margin mode  
↳ cross_available | string | Optional | none | Cross margin available balance, applicable to new classic account margin mode  
↳ cross_margin_balance | string | Optional | none | Cross margin balance, applicable to new classic account margin mode  
↳ cross_mmr | string | Optional | none | Cross margin maintenance margin rate, applicable to new classic account margin mode  
↳ cross_imr | string | Optional | none | Cross margin initial margin rate, applicable to new classic account margin mode  
↳ isolated_position_margin | string | Optional | none | Isolated position margin, applicable to new classic account margin mode  
↳ enable_new_dual_mode | boolean | Optional | none | Deprecated  
↳ margin_mode | integer | Optional | none | Margin mode of the account  
0: classic future account or Classic Spot Margin Mode of unified account;  
1: Multi-Currency Margin Mode;  
2: Portoforlio Margin Mode;  
3: Single-Currency Margin Mode  
↳ enable_tiered_mm | boolean | Optional | none | Whether to enable tiered maintenance margin calculation  
↳ enable_dual_plus | boolean | Optional | none | Whether to Support Split Position Mode  
↳ position_mode | string | Optional | none | Position Holding Mode single - Single Direction Position, dual - Dual Direction Position, dual_plus - Split Position  
↳ history | object | Optional | none | Statistical data  
↳ dnw | string | Optional | none | total amount of deposit and withdraw  
↳ pnl | string | Optional | none | total amount of trading profit and loss  
↳ fee | string | Optional | none | total amount of fee  
↳ refr | string | Optional | none | total amount of referrer rebates  
↳ fund | string | Optional | none | total amount of funding costs  
↳ point_dnw | string | Optional | none | total amount of point deposit and withdraw  
↳ point_fee | string | Optional | none | total amount of point fee  
↳ point_refr | string | Optional | none | total amount of referrer rebates of point fee  
↳ bonus_dnw | string | Optional | none | total amount of perpetual contract bonus transfer  
↳ bonus_offset | string | Optional | none | total amount of perpetual contract bonus deduction  
↳ cross_settle | string | Optional | none | Represents the value of profit settlement from the futures account to the spot account under Unified Account Mode. Negative values indicate settlement from futures to spot, while positive values indicate settlement from spot to futures. This value is cumulative.  
      
    
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

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
sub_account | string | Required | none | Sub account user ID  
sub_account_type | string | Optional | none | Target sub-account trading account: spot - spot account, futures - perpetual contract account, delivery - delivery contract account, options - options account  
currency | string | Required | none | Transfer currency name  
amount | string | Required | none | Transfer Amount, supports up to 8 decimal places, must be greater than 0  
direction | string | Required | none | Transfer direction: to - transfer into sub-account, from - transfer out from sub-account  
client_order_id | string | Optional | none | Customer-defined ID to prevent duplicate transfers. Can be a combination of letters (case-sensitive), numbers, hyphens '-', and underscores '_'. Can be pure letters or pure numbers with length between 1-64 characters  
      
    
    {
      "sub_account": "string",
      "sub_account_type": "spot",
      "currency": "string",
      "amount": "string",
      "direction": "string",
      "client_order_id": "string"
    }
    
    

##  SmallBalance

_Small Balance Conversion_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency  
available_balance | string | Optional | none | Available balance  
estimated_as_btc | string | Optional | none | Estimated as BTC  
convertible_to_gt | string | Optional | none | Estimated conversion to GT  
      
    
    {
      "currency": "string",
      "available_balance": "string",
      "estimated_as_btc": "string",
      "convertible_to_gt": "string"
    }
    
    

##  UidPushOrder

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Order ID  
push_uid | integer(int64) | Optional | none | Initiator User ID  
receive_uid | integer(int64) | Optional | none | Recipient User ID  
currency | string | Optional | none | Currency name  
amount | string | Optional | none | Transfer amount  
create_time | integer(int64) | Optional | none | Created time  
status | string | Optional | none | Withdrawal status:  
  
\- CREATING: Creating  
\- PENDING: Waiting for recipient (Please contact the recipient to accept the transfer on Gate official website)  
\- CANCELLING: Cancelling  
\- CANCELLED: Cancelled  
\- REFUSING: Refusing  
\- REFUSED: Refused  
\- RECEIVING: Receiving  
\- RECEIVED: Success  
message | string | Optional | none | PENDING reason tips  
transaction_type | string | Optional | none | Order Type  
      
    
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
    
    

##  SubAccountCrossMarginBalance

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
uid | string | Optional | none | User ID  
available | object | Optional | none | none  
↳ user_id | integer(int64) | Optional | none | Cross margin account user ID. 0 means this sub-account has not yet opened a cross margin account  
↳ locked | boolean | Optional | none | Whether the account is locked  
↳ balances | object | Optional | none | none  
↳ CrossMarginBalance | object | Optional | none | none  
↳ available | string | Optional | none | Available balance  
↳ freeze | string | Optional | none | Locked balance  
↳ borrowed | string | Optional | none | Borrowed balance  
↳ interest | string | Optional | none | Unpaid interest  
↳ total | string | Optional | none | Total account value in USDT, i.e., the sum of all currencies' `(available+freeze)*price*discount`  
↳ borrowed | string | Optional | none | Total borrowed value in USDT, i.e., the sum of all currencies' `borrowed*price*discount`  
↳ borrowed_net | string | Optional | none | Total borrowed value in USDT * leverage factor  
↳ net | string | Optional | none | Total net assets in USDT  
↳ leverage | string | Optional | none | Position leverage  
↳ interest | string | Optional | none | Total unpaid interest in USDT, i.e., the sum of all currencies' `interest*price*discount`  
↳ risk | string | Optional | none | Risk rate. When it falls below 110%, liquidation will be triggered. Calculation formula: `total / (borrowed+interest)`  
↳ total_initial_margin | string | Optional | none | Total initial margin  
↳ total_margin_balance | string | Optional | none | Total margin balance  
↳ total_maintenance_margin | string | Optional | none | Total maintenance margin  
↳ total_initial_margin_rate | string | Optional | none | Total initial margin rate  
↳ total_maintenance_margin_rate | string | Optional | none | Total maintenance margin rate  
↳ total_available_margin | string | Optional | none | Total available margin  
      
    
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
    
    

##  ConvertSmallBalance

_Small Balance Conversion_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | array | Optional | none | Currency to be converted  
is_all | boolean | Optional | none | Whether to convert all  
      
    
    {
      "currency": [
        "string"
      ],
      "is_all": true
    }
    
    

##  DepositRecord

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | read-only | Record ID  
txid | string | Optional | read-only | Hash record of the withdrawal  
timestamp | string | Optional | read-only | Operation time  
amount | string | Required | none | Token amount  
currency | string | Required | none | Currency name  
address | string | Optional | none | Withdrawal address. Required for withdrawals  
memo | string | Optional | none | Additional remarks with regards to the withdrawal  
status | string | Optional | read-only | Transaction Status  
  
\- BLOCKED: Deposit Blocked  
\- DEP_CREDITED: Deposit Credited, Withdrawal Pending Unlock  
\- DONE: Funds Credited to Spot Account  
\- INVALID: Invalid Transaction  
\- MANUAL: Manual Review Required  
\- PEND: Processing  
\- REVIEW: Under Compliance Review  
\- TRACK: Tracking Block Confirmations, Pending Spot Account Credit  
chain | string | Required | none | Name of the chain used in withdrawals  
      
    
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
    
    

##  TransferOrderStatus

_TransferOrderStatus_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
tx_id | string | Optional | none | Order ID  
status | string | Optional | none | Transfer status: PENDING - Processing, SUCCESS - Transfer successful, FAIL - Transfer failed, PARTIAL_SUCCESS - Partially successful (this status appears when transferring between sub-accounts)  
      
    
    {
      "tx_id": "string",
      "status": "string"
    }
    
    

##  WithdrawalRecord

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | read-only | Record ID  
txid | string | Optional | read-only | Hash record of the withdrawal  
block_number | string | Optional | read-only | Block Number  
withdraw_order_id | string | Optional | none | Client order id, up to 32 length and can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  
timestamp | string | Optional | read-only | Operation time  
amount | string | Required | none | Token amount  
fee | string | Optional | read-only | fee  
currency | string | Required | none | Currency name  
address | string | Optional | none | Withdrawal address  
type | string | Optional | none | Business Type  
fail_reason | string | Optional | none | Reason for withdrawal failure. Has a value when status = CANCEL, empty for all other statuses  
timestamp2 | string | Optional | none | Withdrawal final time, i.e.: withdrawal cancellation time or withdrawal success time  
When status = CANCEL, corresponds to cancellation time  
When status = DONE, it is the withdrawal success time  
memo | string | Optional | none | Additional remarks with regards to the withdrawal  
status | string | Optional | read-only | Transaction Status  
  
\- BCODE: Deposit Code Operation  
\- CANCEL: Cancelled  
\- CANCELPEND: Withdrawal Cancellation Pending  
\- DONE: Completed  
\- EXTPEND: Sent and Waiting for Confirmation  
\- FAIL: On-Chain Failure Pending Confirmation  
\- FVERIFY: Facial Verification in Progress  
\- LOCKED: Wallet-Side Order Locked  
\- MANUAL: Pending Manual Review  
\- REJECT: Rejected  
\- REQUEST: Request in Progress  
\- REVIEW: Under Review  
chain | string | Required | none | Name of the chain used in withdrawals  
      
    
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
    
    

##  SubAccountBalance

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
uid | string | Optional | none | User ID  
available | object | Optional | none | Available balances of currencies  
↳ additionalProperties | string | Optional | none | none  
locking | object | Optional | none | Locked amount by currency  
↳ additionalProperties | string | Optional | none | none  
      
    
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
    
    

##  DepositAddress

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Required | none | Currency detail  
address | string | Required | none | Deposit address  
min_deposit_amount | string | Optional | none | Minimum Deposit Amount  
multichain_addresses | array | Optional | none | none  
↳ MultiChainAddressItem | object | Optional | none | none  
↳ chain | string | Optional | none | Name of the chain  
↳ address | string | Optional | none | Deposit address  
↳ payment_id | string | Optional | none | Notes that some currencies required(e.g., Tag, Memo) when depositing  
↳ payment_name | string | Optional | none | Note type, `Tag` or `Memo`  
↳ obtain_failed | integer | Optional | none | The obtain failed status- 0: address successfully obtained- 1: failed to obtain address  
↳ min_confirms | integer | Optional | none | Minimum Confirmation Count  
      
    
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
    
    

##  CurrencyChain

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
chain | string | Optional | none | Chain name  
name_cn | string | Optional | none | Chain name in Chinese  
name_en | string | Optional | none | Chain name in English  
contract_address | string | Optional | none | Smart contract address for the currency; if no address is available, it will be an empty string  
is_disabled | integer(int32) | Optional | none | If it is disabled. 0 means NOT being disabled  
is_deposit_disabled | integer(int32) | Optional | none | Is deposit disabled. 0 means not disabled  
is_withdraw_disabled | integer(int32) | Optional | none | Is withdrawal disabled. 0 means not disabled  
decimal | string | Optional | none | Withdrawal precision  
is_tag | integer | Optional | none | Whether to Include Tag  
      
    
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
    
    

##  TradeFee

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional | none | User ID  
taker_fee | string | Optional | none | spot taker fee rate  
maker_fee | string | Optional | none | spot maker fee rate  
rpi_maker_fee | string | Optional | none | spot RPI MM maker fee rate  
gt_discount | boolean | Optional | none | Whether GT deduction discount is enabled  
gt_taker_fee | string | Optional | none | Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  
gt_maker_fee | string | Optional | none | Maker fee rate with GT deduction. Returns 0 if GT deduction is disabled  
loan_fee | string | Optional | none | Loan fee rate of margin lending  
point_type | string | Optional | none | Point card type: 0 - Original version, 1 - New version since 202009  
futures_taker_fee | string | Optional | none | Perpetual contract taker fee rate  
futures_maker_fee | string | Optional | none | Perpetual contract maker fee rate  
futures_rpi_maker_fee | string | Optional | none | contract RPI MM maker fee rate  
delivery_taker_fee | string | Optional | none | Delivery contract taker fee rate  
delivery_maker_fee | string | Optional | none | Delivery contract maker fee rate  
debit_fee | integer | Optional | none | Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  
rpi_mm | integer | Optional | none | RPI MM Level  
      
    
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
    
    

##  Transfer

*Accounts available to transfer:

  * `spot`: spot account
  * `margin`: margin account
  * `futures`: perpetual futures account
  * `delivery`: delivery futures account
  * `options`: options account*

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Required | none | Transfer currency name. For contract accounts, `currency` can be set to `POINT` (points) or supported settlement currencies (e.g., `BTC`, `USDT`)  
from | string | Required | none | Account to transfer from  
to | string | Required | none | Account to transfer to  
amount | string | Required | none | Transfer Amount, supports up to 8 decimal places, must be greater than 0  
currency_pair | string | Optional | none | Margin trading pair. Required when transferring to or from margin account  
settle | string | Optional | none | Contract settlement currency. Required when transferring to or from contract account  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
    
    

##  SmallBalanceHistory

_Small Balance Conversion_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | read-only | Order ID  
currency | string | Optional | read-only | Currency  
amount | string | Optional | read-only | Swap Amount  
gt_amount | string | Optional | read-only | GT amount  
create_time | integer(int64) | Optional | read-only | Exchange time (in seconds)  
      
    
    {
      "id": "string",
      "currency": "string",
      "amount": "string",
      "gt_amount": "string",
      "create_time": 0
    }
    
    

##  TransactionID

_TransactionID_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
tx_id | integer(int64) | Optional | none | Order ID  
      
    
    {
      "tx_id": 0
    }
    
    

##  TotalBalance

_User's total balance information_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
total | object | Optional | none | Total balances calculated with specified currency unit  
↳ amount | string | Optional | none | Account total balance amount  
↳ currency | string | Optional | none | Currency  
↳ unrealised_pnl | string | Optional | none | Unrealised_pnl, this field will only appear in futures, options, delivery, and total accounts  
↳ borrowed | string | Optional | none | Total borrowed amount, this field will only appear in margin and cross_margin accounts  
details | object | Optional | none | Total Balances of All Accounts  
  
\- cross_margin: Cross Margin Account  
\- spot: Spot Account  
\- finance: Finance Account  
\- margin: Margin Account  
\- quant: Quantitative Account  
\- futures: Futures Account (Perpetual Contracts)  
\- delivery: Delivery Account (Delivery Contracts)  
\- warrant: Warrant Account  
\- cbbc: CBBC Account (Covered Bull/Bear Contract)  
\- meme_box: Alpha Account  
\- options: Options Account  
\- payment: Payment Account  
↳ additionalProperties | TotalBalance/properties/total | Optional | none | Total balances calculated with specified currency unit  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
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
    
    

##  SubAccountToSubAccount

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Required | none | Transfer currency name  
sub_account_type | string | Optional | none | Transfer from account (deprecated, use `sub_account_from_type` and `sub_account_to_type` instead)  
sub_account_from | string | Required | none | Transfer from the user id of the sub-account  
sub_account_from_type | string | Required | none | Source sub-account trading account: spot - spot account, futures - perpetual contract account, delivery - delivery contract account  
sub_account_to | string | Required | none | Transfer to the user id of the sub-account  
sub_account_to_type | string | Required | none | Target sub-account trading account: spot - spot account, futures - perpetual contract account, delivery - delivery contract account  
amount | string | Required | none | Transfer Amount, supports up to 8 decimal places, must be greater than 0  
      
    
    {
      "currency": "string",
      "sub_account_type": "string",
      "sub_account_from": "string",
      "sub_account_from_type": "string",
      "sub_account_to": "string",
      "sub_account_to_type": "string",
      "amount": "string"
    }