---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/system/system-status
api_type: WebSocket
updated_at: 2026-07-31 19:04:00.273231
---

# Websocket Trade Guideline

## URL

  * **Mainnet:**  
`wss://stream.bybit.com/v5/trade`



info

  * Turkey users registered from "[www.bybit.tr"](http://www.bybit.tr%22), please use `wss://stream.bybit.tr/v5/trade`
  * Kazakhstan users registered from "[www.bybit.kz"](http://www.bybit.kz%22), please use `wss://stream.bybit.kz/v5/trade`



  * **Testnet:**  
`wss://stream-testnet.bybit.com/v5/trade`



## Scope

  * **Support** : USDT Contract, USDC Contract, Spot, Options, Inverse contract
  * **Not support** : demo trading, spread trading



## Authentication

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
reqId| false| string| Optional field, used to match the response 

  * If not passed, this field will not be returned in response

  
op| **true**|  string| Op type. `auth`  
args| **true**|  string| ["api key", expiry timestamp, "signature"]. Please click [here](/docs/v5/ws/connect#authentication) to generate signature  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
reqId| string| 

  * If it is passed on the request, then it is returned in the response
  * If it is not passed, then it is not returned in the response

  
retCode| integer| 

  * `0`: auth success
  * `20001`: repeat auth
  * `10004`: invalid sign
  * `10001`: param error

  
retMsg| string| 

  * `OK`
  * Error message

  
op| string| Op type  
connId| string| Connection id, the unique id for the connection  
  
### Request Example
    
    
    {  
        "op": "auth",  
        "args": [  
            "XXXXXX",  
            1711010121452,  
            "ec71040eff72b163a36153d770b69d6637bcb29348fbfbb16c269a76595ececf"  
        ]  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "op": "auth",  
        "connId": "cnt5leec0hvan15eukcg-2t"  
    }  
    

## Create/Amend/Cancel Order

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
reqId| false| string| Used to identify the uniqueness of the request, the response will return it when passed. The length cannot exceed 36 characters. 

  * If passed, it can't be duplicated, otherwise you will get "20006"

  
header| **true**|  object| Request headers  
> X-BAPI-TIMESTAMP| **true**|  string| Current timestamp  
> X-BAPI-RECV-WINDOW| false| string| 5000(ms) by default. Request will be rejected when not satisfy this rule: _Bybit_server_time - X-BAPI-RECV-WINDOW <= X-BAPI-TIMESTAMP < Bybit_server_time + 1000_  
> Referer| false| string| The referer identifier for API broker user  
op| **true**|  string| Op type 

  * `order.create`: create an order
  * `order.amend`: amend an order
  * `order.cancel`: cancel an order

  
args| **true**|  array<object>| Args array, support one item only for now 

  * `order.create`: refer to [create order request](/docs/v5/order/create-order#request-parameters)
  * `order.amend`: refer to [amend order request](/docs/v5/order/amend-order#request-parameters)
  * `order.cancel`: refer to [cancel order request](/docs/v5/order/cancel-order#request-parameters)

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
reqId| string| 

  * If it is passed on the request, then it is returned in the response
  * If it is not passed, then it is not returned in the response

  
retCode| integer| 

  * `0`: success
  * `10403`: exceed IP rate limit. 3000 requests per second per IP
  * `10404`: 1. op type is not found; 2. `category` is not correct/supported
  * `10429`: System level frequency protection
  * `20006`: reqId is duplicated
  * `10016`: 1. internal server error; 2. Service is restarting
  * `10019`: ws trade service is restarting, do not accept new request, but the request in the process is not affected. You can build new connection to be routed to normal service

  
retMsg| string| 

  * `OK`
  * `""`
  * Error message

  
op| string| Op type  
data| object| Business data, keep the same as `result` on rest api response 

  * `order.create`: refer to [create order response](/docs/v5/order/create-order#response-parameters)
  * `order.amend`: refer to [amend order response](/docs/v5/order/amend-order#response-parameters)
  * `order.cancel`: refer to [cancel order response](/docs/v5/order/cancel-order#response-parameters)

  
retExtInfo| object| Always empty object  
header| object| Header info  
> TraceId| string| Trace ID, used to track the trip of request  
> Timenow| string| Current timestamp  
> X-Bapi-Limit| string| The total rate limit of the current account for this op type  
> X-Bapi-Limit-Status| string| The remaining rate limit of the current account for this op type  
> X-Bapi-Limit-Reset-Timestamp| string| The timestamp indicates when your request limit resets if you have exceeded your rate limit. Otherwise, this is just the current timestamp (it may not exactly match `timeNow`)  
connId| string| Connection id, the unique id for the connection  
  
info

The ack of create/amend/cancel order request indicates that the request is successfully accepted. Please use websocket order stream to confirm the order status

### Request Example
    
    
    {  
        "reqId": "test-005",  
        "header": {  
            "X-BAPI-TIMESTAMP": "1711001595207",  
            "X-BAPI-RECV-WINDOW": "8000",  
            "Referer": "bot-001" // for api broker  
        },  
        "op": "order.create",  
        "args": [  
            {  
                "symbol": "ETHUSDT",  
                "side": "Buy",  
                "orderType": "Limit",  
                "qty": "0.2",  
                "price": "2800",  
                "category": "linear",  
                "timeInForce": "PostOnly"  
            }  
        ]  
    }  
    

### Response Example
    
    
    {  
        "reqId": "test-005",  
        "retCode": 0,  
        "retMsg": "OK",  
        "op": "order.create",  
        "data": {  
            "orderId": "a4c1718e-fe53-4659-a118-1f6ecce04ad9",  
            "orderLinkId": ""  
        },  
        "retExtInfo": {},  
        "header": {  
            "X-Bapi-Limit": "10",  
            "X-Bapi-Limit-Status": "9",  
            "X-Bapi-Limit-Reset-Timestamp": "1711001595208",  
            "Traceid": "38b7977b430f9bd228f4b19724794dfd",  
            "Timenow": "1711001595209"  
        },  
        "connId": "cnt5leec0hvan15eukcg-2v"  
    }  
    

## Batch Create/Amend/Cancel Order

info

  * A maximum of 20 orders (option), 20 orders (inverse), 20 orders (linear), 10 orders (spot) can be placed per request. The returned data list is divided into two lists. The first list indicates whether or not the order creation was successful and the second list details the created order information. The structure of the two lists are completely consistent.


  * **Option rate limt** instruction: its rate limit is count based on the actual number of request sent, e.g., by default, option trading rate limit is 10 reqs per sec, so you can send up to 20 * 10 = 200 orders in one second. 
  * **Perpetual, Futures, Spot rate limit instruction** , please check [here](/docs/v5/rate-limit#api-rate-limit-rules-for-vips)


  * The account rate limit is shared between websocket and http batch orders
  * The acknowledgement of batch create/amend/cancel order requests indicates that the request was sucessfully accepted. The request is asynchronous so please use the websocket to confirm the order status.



### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
reqId| false| string| Used to identify the uniqueness of the request, the response will return it when passed. The length cannot exceed 36 characters. 

  * If passed, it can't be duplicated, otherwise you will get "20006"

  
header| **true**|  object| Request headers  
> X-BAPI-TIMESTAMP| **true**|  string| Current timestamp  
> X-BAPI-RECV-WINDOW| false| string| 5000(ms) by default. Request will be rejected when not satisfy this rule: _Bybit_server_time - X-BAPI-RECV-WINDOW <= X-BAPI-TIMESTAMP < Bybit_server_time + 1000_  
> Referer| false| string| The referer identifier for API broker user  
op| **true**|  string| Op type 

  * `order.create-batch`: batch create orders
  * `order.amend-batch`: batch amend orders
  * `order.cancel-batch`: batch cancel orders

  
args| **true**|  array<object>| Args array 

  * `order.create-batch`: refer to [Batch Place Order request](/docs/v5/order/batch-place#request-parameters)
  * `order.amend-batch`: refer to [Batch Amend Order request](/docs/v5/order/batch-amend#request-parameters)
  * `order.cancel-batch`: refer to [Batch Cancel Order request](/docs/v5/order/batch-cancel#request-parameters)

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
reqId| string| 

  * If it is passed on the request, then it is returned in the response
  * If it is not passed, then it is not returned in the response

  
retCode| integer| 

  * `0`: success
  * `10403`: exceed IP rate limit. 3000 requests per second per IP
  * `10404`: 1. op type is not found; 2. `category` is not correct/supported
  * `10429`: System level frequency protection
  * `20006`: reqId is duplicated
  * `10016`: 1. internal server error; 2. Service is restarting
  * `10019`: ws trade service is restarting, do not accept new request, but the request in the process is not affected. You can build new connection to be routed to normal service

  
retMsg| string| 

  * `OK`
  * `""`
  * Error message

  
op| string| Op type  
data| object| Business data, keep the same as `result` on rest api response 

  * `order.create-batch`: refer to [Batch Place Order response](/docs/v5/order/batch-place#response-parameters)
  * `order.amend-batch`: refer to [Batch Amend Order response](/docs/v5/order/batch-amend#response-parameters)
  * `order.cancel-batch`: refer to [Batch Cancel Order response](/docs/v5/order/batch-cancel#response-parameters)

  
retExtInfo| object|   
> list| array<object>|   
>> code| number| Success/error code  
>> msg| string| Success/error message  
header| object| Header info  
> TraceId| string| Trace ID, used to track the trip of request  
> Timenow| string| Current timestamp  
> X-Bapi-Limit| string| The total rate limit of the current account for this op type  
> X-Bapi-Limit-Status| string| The remaining rate limit of the current account for this op type  
> X-Bapi-Limit-Reset-Timestamp| string| The timestamp indicates when your request limit resets if you have exceeded your rate limit. Otherwise, this is just the current timestamp (it may not exactly match `timeNow`)  
connId| string| Connection id, the unique id for the connection  
  
### Request Example
    
    
      
    {  
        "op": "order.create-batch",  
        "header": {  
            "X-BAPI-TIMESTAMP": "1740453381256",  
            "X-BAPI-RECV-WINDOW": "1000"  
        },  
        "args": [  
            {  
                "category": "linear",  
                "request": [  
                    {  
                        "symbol": "SOLUSDT",  
                        "qty": "10",  
                        "price": "500",  
                        "orderType": "Limit",  
                        "timeInForce": "GTC",  
                        "orderLinkId": "-batch-000",  
                        "side": "Buy"  
                    },  
                    {  
                        "symbol": "SOLUSDT",  
                        "qty": "20",  
                        "price": "1000",  
                        "orderType": "Limit",  
                        "timeInForce": "GTC",  
                        "orderLinkId": "batch-001",  
                        "side": "Buy"  
                    },  
                    {  
                        "symbol": "SOLUSDT",  
                        "qty": "30",  
                        "price": "1500",  
                        "orderType": "Limit",  
                        "timeInForce": "GTC",  
                        "orderLinkId": "batch-002",  
                        "side": "Buy"  
                    }  
                ]  
            }  
        ]  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "op": "order.create-batch",  
        "data": {  
            "list": [  
                {  
                    "category": "linear",  
                    "symbol": "SOLUSDT",  
                    "orderId": "",  
                    "orderLinkId": "batch-000",  
                    "createAt": ""  
                },  
                {  
                    "category": "linear",  
                    "symbol": "SOLUSDT",  
                    "orderId": "",  
                    "orderLinkId": "batch-001",  
                    "createAt": ""  
                },  
                {  
                    "category": "linear",  
                    "symbol": "SOLUSDT",  
                    "orderId": "",  
                    "orderLinkId": "batch-002",  
                    "createAt": ""  
                }  
            ]  
        },  
        "retExtInfo": {  
            "list": [  
                {  
                    "code": 10001,  
                    "msg": "position idx not match position mode"  
                },  
                {  
                    "code": 10001,  
                    "msg": "position idx not match position mode"  
                },  
                {  
                    "code": 10001,  
                    "msg": "position idx not match position mode"  
                }  
            ]  
        },  
        "header": {  
            "Timenow": "1740453408556",  
            "X-Bapi-Limit": "150",  
            "X-Bapi-Limit-Status": "147",  
            "X-Bapi-Limit-Reset-Timestamp": "1740453408555",  
            "Traceid": "0e32b551b3e17aae77651aadf6a5be80"  
        },  
        "connId": "cupviqn88smf24t2kpb0-536o"  
    }  
    

## Ping

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
op| **true**|  string| Op type. `ping`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Result code  
retMsg| string| Result message  
op| string| Op type `pong`  
data| array| One item in the array, current timestamp (string)  
connId| string| Connection id, the unique id for the connection  
  
### Request Example
    
    
    {  
        "op": "ping"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "op": "pong",  
        "data": [  
            "1711002002529"  
        ],  
        "connId": "cnt5leec0hvan15eukcg-2v"  
    }

---

# Websocket下單指南

## 路徑

  * **主網:**  
`wss://stream.bybit.com/v5/trade`



信息

帳戶創建自"[www.bybit.tr"的用戶](http://www.bybit.tr%22%E7%9A%84%E7%94%A8%E6%88%B6), 請使用`wss://stream.bybit.tr/v5/trade`

  * **測試網:**  
`wss://stream-testnet.bybit.com/v5/trade`



## 支持範圍

  * [統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620): USDT永續, USDC合約, 期權, 現貨, 反向合約
  * [統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610): USDT永續, USDC合約, 期權, 現貨



## 鑒權請求

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
reqId| false| string| 可選參數, 可用於匹配響應。長度不能超過36個字串。 

  * 若不傳, 該字段不會從響應種返回

  
op| **true**|  string| Op類型 `auth`  
args| **true**|  string| ["api密鑰", 過期時間, "簽名"]. 請參閱[這裡](/docs/zh-TW/v5/ws/connect#%E9%91%92%E6%AC%8A)來生成簽名  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
reqId| string| 

  * 若請求有傳, 則響應存在該字段
  * 若請求不傳, 則響應沒有該字段

  
retCode| integer| 

  * `0`: 鑒權成功
  * `20001`: 重複請求
  * `10004`: 無效簽名
  * `10001`: 參數錯誤

  
retMsg| string| 

  * `OK`
  * 報錯信息

  
op| string| Op類型  
connId| string| 連接的唯一id  
  
### 請求示例
    
    
    {  
        "op": "auth",  
        "args": [  
            "XXXXXX",  
            1711010121452,  
            "ec71040eff72b163a36153d770b69d6637bcb29348fbfbb16c269a76595ececf"  
        ]  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "op": "auth",  
        "connId": "cnt5leec0hvan15eukcg-2t"  
    }  
    

## 下單/改單/撤單

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
reqId| false| string| 請求reqId, 可作為請求的唯一標識, 若有傳, 則響應會返回該字段 

  * 當傳, 需保證唯一, 否則將會拿到錯誤 "20006"

  
header| **true**|  object| 請求頭  
> X-BAPI-TIMESTAMP| **true**|  string| 當前時間戳  
> X-BAPI-RECV-WINDOW| false| string| 默認5000(毫秒). 請求的時間需要滿足該公式: _Bybit服務器時間 - X-BAPI-RECV-WINDOW <= X-BAPI-TIMESTAMP < Bybit服務器時間 + 1000_  
> Referer| false| string| API broker用戶返佣標識  
op| **true**|  string| Op類型 

  * `order.create`: 創建訂單
  * `order.amend`: 修改訂單
  * `order.cancel`: 撤銷訂單

  
args| **true**|  array<object>| 參數數組, 僅支持一個訂單 

  * `order.create`: 請參閱[創建訂單請求參數](/docs/zh-TW/v5/order/create-order#%E8%AB%8B%E6%B1%82%E5%8F%83%E6%95%B8)
  * `order.amend`: 請參閱[修改訂單參數](/docs/zh-TW/v5/order/amend-order#%E8%AB%8B%E6%B1%82%E5%8F%83%E6%95%B8)
  * `order.cancel`: 請參閱[撤銷訂單參數](/docs/zh-TW/v5/order/cancel-order#%E8%AB%8B%E6%B1%82%E5%8F%83%E6%95%B8)

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
reqId| string| 

  * 若請求有傳, 則響應存在該字段
  * 若請求不傳, 則響應沒有該字段

  
retCode| integer| 

  * `0`: 成功
  * `10403`: 超過了IP頻率. 單個IP最多允許3000次/秒的請求頻率
  * `10404`: 1. op類型未找到; 2. `category`不支持/未找到
  * `10429`: 觸發系統級別的頻率保護
  * `20006`: `reqId`重複
  * `10016`: 1.內部錯誤; 2. 服務重啟
  * `10019`: ws下單服務正在重啟, 拒絕新的請求, 正在處理中的請求不受影響. 您可以重新/新建連接, 會分配到正常的服務上

  
retMsg| string| 

  * `OK`
  * `""`
  * 報錯信息

  
op| string| Op類型  
data| object| 業務數據, 和rest api響應的`result`字段業務數據一致 

  * `order.create`: 請參閱[創建訂單響應參數](/docs/zh-TW/v5/order/create-order#%E9%9F%BF%E6%87%89%E5%8F%83%E6%95%B8)
  * `order.amend`: 請參閱[修改訂單響應參數](/docs/zh-TW/v5/order/amend-order#%E9%9F%BF%E6%87%89%E5%8F%83%E6%95%B8)
  * `order.cancel`: 請參閱[取消訂單響應參數](/docs/zh-TW/v5/order/cancel-order#%E9%9F%BF%E6%87%89%E5%8F%83%E6%95%B8)

  
retExtInfo| object| 總是為空的對象  
header| object| 響應頭信息  
> TraceId| string| Trace ID, 用於追蹤請求鏈路 (內部使用)  
> Timenow| string| 當前時間戳  
> X-Bapi-Limit| string| 該類型請求的帳戶總頻率  
> X-Bapi-Limit-Status| string| 該類型請求的帳戶剩餘可用頻率  
> X-Bapi-Limit-Reset-Timestamp| string| 如果您已超過該接口當前窗口頻率限製，該字段表示下個可用時間窗口的時間戳（毫秒）即什麽時候可以恢復訪問；如果您未超過該接口當前窗口頻率限製，該字段表示返回的是當前服務器時間（毫秒).  
connId| string| 連接的唯一id  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

### 請求示例
    
    
    {  
        "reqId": "test-005",  
        "header": {  
            "X-BAPI-TIMESTAMP": "1711001595207",  
            "X-BAPI-RECV-WINDOW": "8000",  
            "Referer": "bot-001" // for api broker  
        },  
        "op": "order.create",  
        "args": [  
            {  
                "symbol": "ETHUSDT",  
                "side": "Buy",  
                "orderType": "Limit",  
                "qty": "0.2",  
                "price": "2800",  
                "category": "linear",  
                "timeInForce": "PostOnly"  
            }  
        ]  
    }  
    

### 響應示例
    
    
    {  
        "reqId": "test-005",  
        "retCode": 0,  
        "retMsg": "OK",  
        "op": "order.create",  
        "data": {  
            "orderId": "a4c1718e-fe53-4659-a118-1f6ecce04ad9",  
            "orderLinkId": ""  
        },  
        "retExtInfo": {},  
        "header": {  
            "X-Bapi-Limit": "10",  
            "X-Bapi-Limit-Status": "9",  
            "X-Bapi-Limit-Reset-Timestamp": "1711001595208",  
            "Traceid": "38b7977b430f9bd228f4b19724794dfd",  
            "Timenow": "1711001595209"  
        },  
        "connId": "cnt5leec0hvan15eukcg-2v"  
    }  
    

## 批量下單/改單/撤單

信息

  * 每個請求包含的訂單數最大是: 20筆(期权), 20筆(反向合約), 20筆(正向合約), 10筆(現貨), 返回的數據列表中分成兩個list，訂單創建的列表和創建結果的信息返回，兩個list的訂單的序列是完全保持一致的。
  * **期權** 批量接口頻率規則: 期權是按照實際發送的請求次數來統計頻率的, 因此如果帳戶頻率是10次/秒, 每次請求發送20筆訂單, 則可以每秒發送200筆訂單;
  * **期貨和現貨** 的批量接口頻率規則: 請從[這裡](/docs/zh-TW/v5/rate-limit#%E4%B8%8D%E5%90%8Cvip%E7%AD%89%E7%B4%9A%E7%9A%84%E6%8E%A5%E5%8F%A3%E9%99%90%E9%A0%BB%E8%A6%8F%E5%89%87)查閱其API限頻說明
  * ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態
  * websocket和http批量下單共享帳戶頻率



### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
reqId| false| string| 請求reqId, 可作為請求的唯一標識, 若有傳, 則響應會返回該字段 

  * 當傳, 需保證唯一, 否則將會拿到錯誤 "20006"

  
header| **true**|  object| 請求頭  
> X-BAPI-TIMESTAMP| **true**|  string| 當前時間戳  
> X-BAPI-RECV-WINDOW| false| string| 默認5000(毫秒). 請求的時間需要滿足該公式: _Bybit服務器時間 - X-BAPI-RECV-WINDOW <= X-BAPI-TIMESTAMP < Bybit服務器時間 + 1000_  
> Referer| false| string| API broker用戶返佣標識  
op| **true**|  string| Op類型 

  * `order.create-batch`: 批量創建訂單
  * `order.amend-batch`: 批量修改訂單
  * `order.cancel-batch`: 批量撤銷訂單

  
args| **true**|  array<object>| 參數數組 

  * `order.create-batch`: 請參閱[批量創建訂單請求參數](/docs/zh-TW/v5/order/batch-place#%E8%AB%8B%E6%B1%82%E5%8F%83%E6%95%B8)
  * `order.amend-batch`: 請參閱[批量修改訂單參數](/docs/zh-TW/v5/order/batch-amend#%E8%AB%8B%E6%B1%82%E5%8F%83%E6%95%B8)
  * `order.cancel-batch`: 請參閱[批量撤銷訂單參數](/docs/zh-TW/v5/order/batch-cancel#%E8%AB%8B%E6%B1%82%E5%8F%83%E6%95%B8)

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
reqId| string| 

  * 若請求有傳, 則響應存在該字段
  * 若請求不傳, 則響應沒有該字段

  
retCode| integer| 

  * `0`: 成功
  * `10403`: 超過了IP頻率. 單個IP最多允許3000次/秒的請求頻率
  * `10404`: 1. op類型未找到; 2. `category`不支持/未找到
  * `10429`: 觸發系統級別的頻率保護
  * `20006`: `reqId`重複
  * `10016`: 1.內部錯誤; 2. 服務重啟
  * `10019`: ws下單服務正在重啟, 拒絕新的請求, 正在處理中的請求不受影響. 您可以重新/新建連接, 會分配到正常的服務上

  
retMsg| string| 

  * `OK`
  * `""`
  * 報錯信息

  
op| string| Op類型  
data| object| 業務數據, 和rest api響應的`result`字段業務數據一致 

  * `order.create-batch`: 請參閱[批量創建訂單響應參數](/docs/zh-TW/v5/order/batch-place#%E9%9F%BF%E6%87%89%E5%8F%83%E6%95%B8)
  * `order.amend-batch`: 請參閱[批量修改訂單響應參數](/docs/zh-TW/v5/order/batch-amend#%E9%9F%BF%E6%87%89%E5%8F%83%E6%95%B8)
  * `order.cancel-batch`: 請參閱[批量撤銷訂單響應參數](/docs/zh-TW/v5/order/batch-cancel#%E9%9F%BF%E6%87%89%E5%8F%83%E6%95%B8)

  
retExtInfo| object|   
> list| array<object>|   
>> code| number| 成功/錯誤碼  
>> msg| string| 成功/錯誤消息  
header| object| 響應頭信息  
> TraceId| string| Trace ID, 用於追蹤請求鏈路 (內部使用)  
> Timenow| string| 當前時間戳  
> X-Bapi-Limit| string| 該類型請求的帳戶總頻率  
> X-Bapi-Limit-Status| string| 該類型請求的帳戶剩餘可用頻率  
> X-Bapi-Limit-Reset-Timestamp| string| 如果您已超過該接口當前窗口頻率限製，該字段表示下個可用時間窗口的時間戳（毫秒）即什麽時候可以恢復訪問；如果您未超過該接口當前窗口頻率限製，該字段表示返回的是當前服務器時間（毫秒).  
connId| string| 連接的唯一id  
  
### 請求示例
    
    
      
    {  
        "op": "order.create-batch",  
        "header": {  
            "X-BAPI-TIMESTAMP": "1740453381256",  
            "X-BAPI-RECV-WINDOW": "1000"  
        },  
        "args": [  
            {  
                "category": "linear",  
                "request": [  
                    {  
                        "symbol": "SOLUSDT",  
                        "qty": "10",  
                        "price": "500",  
                        "orderType": "Limit",  
                        "timeInForce": "GTC",  
                        "orderLinkId": "-batch-000",  
                        "side": "Buy"  
                    },  
                    {  
                        "symbol": "SOLUSDT",  
                        "qty": "20",  
                        "price": "1000",  
                        "orderType": "Limit",  
                        "timeInForce": "GTC",  
                        "orderLinkId": "batch-001",  
                        "side": "Buy"  
                    },  
                    {  
                        "symbol": "SOLUSDT",  
                        "qty": "30",  
                        "price": "1500",  
                        "orderType": "Limit",  
                        "timeInForce": "GTC",  
                        "orderLinkId": "batch-002",  
                        "side": "Buy"  
                    }  
                ]  
            }  
        ]  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "op": "order.create-batch",  
        "data": {  
            "list": [  
                {  
                    "category": "linear",  
                    "symbol": "SOLUSDT",  
                    "orderId": "",  
                    "orderLinkId": "batch-000",  
                    "createAt": ""  
                },  
                {  
                    "category": "linear",  
                    "symbol": "SOLUSDT",  
                    "orderId": "",  
                    "orderLinkId": "batch-001",  
                    "createAt": ""  
                },  
                {  
                    "category": "linear",  
                    "symbol": "SOLUSDT",  
                    "orderId": "",  
                    "orderLinkId": "batch-002",  
                    "createAt": ""  
                }  
            ]  
        },  
        "retExtInfo": {  
            "list": [  
                {  
                    "code": 10001,  
                    "msg": "position idx not match position mode"  
                },  
                {  
                    "code": 10001,  
                    "msg": "position idx not match position mode"  
                },  
                {  
                    "code": 10001,  
                    "msg": "position idx not match position mode"  
                }  
            ]  
        },  
        "header": {  
            "Timenow": "1740453408556",  
            "X-Bapi-Limit": "150",  
            "X-Bapi-Limit-Status": "147",  
            "X-Bapi-Limit-Reset-Timestamp": "1740453408555",  
            "Traceid": "0e32b551b3e17aae77651aadf6a5be80"  
        },  
        "connId": "cupviqn88smf24t2kpb0-536o"  
    }  
    

## Ping

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
op| **true**|  string| Op類型. `ping`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 響應碼  
retMsg| string| 響應信息  
op| string| Op類型 `pong`  
data| array| 數組會有有一個元素, 當前時間戳 (字符串類型)  
connId| string| 連接的唯一id  
  
### 請求示例
    
    
    {  
        "op": "ping"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "op": "pong",  
        "data": [  
            "1711002002529"  
        ],  
        "connId": "cnt5leec0hvan15eukcg-2v"  
    }