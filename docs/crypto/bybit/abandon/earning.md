---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/earning
api_type: REST
updated_at: 2026-05-27 19:13:43.122376
---

# Get Broker Earning

danger

This endpoint has been deprecated, please move to new [Get Exchange Broker Earning](/docs/v5/broker/exchange-broker/exchange-earning)

info

  * Use exchange broker master account to query
  * The data can support up to past 6 months until T-1
  * `startTime` & `endTime` are either entered at the same time or not entered



### HTTP Request

GET`/v5/broker/earning-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
bizType| false| string| Business type. `SPOT`, `DERIVATIVES`, `OPTIONS`  
startTime| false| integer| The start timestamp(ms)  
endTime| false| integer| The end timestamp(ms)  
limit| false| integer| Limit for data size per page. [`1`, `1000`]. Default: `1000`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> userId| string| UID  
> bizType| string| Business type  
> symbol| string| Symbol name  
> coin| string| Coin name. The currency of earning  
> earning| string| Commission  
> orderId| string| Order ID  
> execTime| string| Execution timestamp (ms)  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/broker/earning-record?bizType=SPOT&startTime=1686240000000&endTime=1686326400000&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686708862669  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "userId": "xxxx",  
                    "bizType": "SPOT",  
                    "symbol": "BTCUSDT",  
                    "coin": "BTC",  
                    "earning": "0.000015",  
                    "orderId": "1531607271849858304",  
                    "execTime": "1686306035957"  
                }  
            ],  
            "nextPageCursor": "0%2C1"  
        },  
        "retExtInfo": {},  
        "time": 1686708863283  
    }

---

# 查詢經紀商返佣

危險

該接口已經廢棄, 請使用[查詢經紀商返佣信息](/docs/zh-TW/v5/broker/exchange-broker/exchange-earning)

信息

  * 使用經紀商的母帳戶進行查詢
  * 支持查詢過去6個月的數據
  * `startTime` & `endTime`兩個入参, 要麼同時輸入, 要麼都不輸入



### HTTP 請求

GET`/v5/broker/earning-record`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
bizType| false| string| 業務類型. `SPOT`, `DERIVATIVES`, `OPTIONS`  
startTime| false| integer| 開始時間戳 (毫秒)  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `1000`]. 默認: `1000`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> userId| string| uid  
> bizType| string| 業務類型  
> symbol| string| 合約名稱  
> coin| string| 幣種名稱. 即`earning`的單位  
> earning| string| 佣金  
> orderId| string| 訂單ID  
> execTime| string| 成交時間戳 (毫秒)  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例

  * HTTP
  * Python


    
    
    GET /v5/broker/earning-record?bizType=SPOT&startTime=1686240000000&endTime=1686326400000&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686708862669  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "userId": "xxxx",  
                    "bizType": "SPOT",  
                    "symbol": "BTCUSDT",  
                    "coin": "BTC",  
                    "earning": "0.000015",  
                    "orderId": "1531607271849858304",  
                    "execTime": "1686306035957"  
                }  
            ],  
            "nextPageCursor": "0%2C1"  
        },  
        "retExtInfo": {},  
        "time": 1686708863283  
    }