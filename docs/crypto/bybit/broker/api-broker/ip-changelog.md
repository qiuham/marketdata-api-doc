---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/broker/api-broker/ip-changelog
api_type: REST
updated_at: 2026-07-01 19:27:12.393748
---

# Get Earning

info

  * Use exchange broker master account to query
  * The data can support up to past 1 months until T-1. To extract data from over a month ago, please contact your Relationship Manager
  * `begin` & `end` are either entered at the same time or not entered, and latest 7 days data are returned by default



> API rate limit: 10 req / sec

### HTTP Request

GET`/v5/broker/earnings-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
bizType| false| string| Business type. `SPOT`, `DERIVATIVES`, `OPTIONS`, `CONVERT`  
begin| false| string| Begin date, in the format of YYYYMMDD, e.g, 20231201, search the data from 1st Dec 2023 00:00:00 UTC (include)  
end| false| string| End date, in the format of YYYYMMDD, e.g, 20231201, search the data before 2nd Dec 2023 00:00:00 UTC (exclude)  
uid| false| string| 

  * To get results for a specific subaccount: Enter the subaccount UID
  * To get results for all subaccounts: Leave the field empty

  
limit| false| integer| Limit for data size per page. [`1`, `1000`]. Default: `1000`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
totalEarningCat| Object| Category statistics for total earning data  
> spot| array| Object. Earning for Spot trading. If do not have any rebate, keep empty array  
>> coin| string| Rebate coin name  
>> earning| string| Rebate amount of the coin  
> derivatives| array| Object. Earning for Derivatives trading. If do not have any rebate, keep empty array  
>> coin| string| Rebate coin name  
>> earning| string| Rebate amount of the coin  
> options| array| Object. Earning for Option trading. If do not have any rebate, keep empty array  
>> coin| string| Rebate coin name  
>> earning| string| Rebate amount of the coin  
> convert| array| Object. Earning for Convert trading. If do not have any rebate, keep empty array  
>> coin| string| Rebate coin name  
>> earning| string| Rebate amount of the coin  
> total| array| Object. Sum earnings of all categories. If do not have any rebate, keep empty array  
>> coin| string| Rebate coin name  
>> earning| string| Rebate amount of the coin  
details| array| Object. Detailed trading information for each sub UID and each category  
> userId| string| Sub UID  
> bizType| string| Business type. `SPOT`, `DERIVATIVES`, `OPTIONS`, `CONVERT`  
> symbol| string| Symbol name  
> coin| string| Rebate coin name  
> earning| string| Rebate amount  
> markupEarning| string| Earning generated from markup fee rate  
> baseFeeEarning| string| Earning generated from base fee rate  
> orderId| string| Order ID  
> execId| string| Trade ID  
> execTime| string| Order execution timestamp (ms)  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/broker/earnings-info?begin=20231129&end=20231129&uid=117894077 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1701399431920  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: 32d2aa1bc205ddfb89849b85e2a8b7e23b1f8f69fe95d6f2cb9c87562f9086a6  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_exchange_broker_earnings(  
        begin="20231129",  
        end="20231129",  
        uid="117894077",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getExchangeBrokerEarnings({  
        bizType: 'SPOT',  
        begin: '20231201',  
        end: '20231207',  
        limit: 1000,  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "totalEarningCat": {  
                "spot": [],  
                "derivatives": [  
                    {  
                        "coin": "USDT",  
                        "earning": "0.00027844"  
                    }  
                ],  
                "options": [],  
                "total": [  
                    {  
                        "coin": "USDT",  
                        "earning": "0.00027844"  
                    }  
                ]  
            },  
            "details": [  
                {  
                    "userId": "117894077",  
                    "bizType": "DERIVATIVES",  
                    "symbol": "DOGEUSDT",  
                    "coin": "USDT",  
                    "earning": "0.00016166",  
                    "markupEarning": "0.000032332",  
                    "baseFeeEarning": "0.000129328",  
                    "orderId": "ec2132f2-a7e0-4a0c-9219-9f3cbcd8e878",  
                    "execId": "c8f418a0-2ccc-594f-ae72-effedf24d0c4",  
                    "execTime": "1701275846033"  
                },  
                {  
                    "userId": "117894077",  
                    "bizType": "DERIVATIVES",  
                    "symbol": "TRXUSDT",  
                    "coin": "USDT",  
                    "earning": "0.00011678",  
                    "markupEarning": "0.000023356",  
                    "baseFeeEarning": "0.000093424",  
                    "orderId": "28b29c2b-ba14-450e-9ce7-3cee0c1fa6da",  
                    "execId": "632c7705-7f3a-5350-b69c-d41a8b3d0697",  
                    "execTime": "1701245285017"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1701398193964  
    }

---

# 查詢返佣信息

信息

  * 使用經紀商的母帳戶進行查詢
  * 支持查詢過去1個月的數據至T-1. 要取得1個月之前的數據, 請聯繫您的客戶經理
  * `begin` & `end`兩個入参, 要麼同時輸入, 要麼都不輸入. 当不输入时, 默认返回最近7天的数据



> API頻率: 10次/秒

### HTTP 請求

GET`/v5/broker/earnings-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
bizType| false| string| 業務類型. `SPOT`, `DERIVATIVES`, `OPTIONS`, `CONVERT`  
begin| false| string| 開始時間, 格式: YYYYMMDD, 比如, 20231201, 表示搜尋時間是從2023年12月1日 00:00:00 UTC (包含)  
end| false| string| 結束時間, 格式: YYYYMMDD, 比如, 20231201, 表示搜尋時間是結束於2023年12月2日 00:00:00 UTC (不包含)  
uid| false| string| 

  * 輸入子UID來查詢指定UID的具體數據
  * 要向獲得所有子UID的數據, 則不傳

  
limit| false| integer| 每頁數量限制. [`1`, `1000`]. 默認: `1000`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
totalEarningCat| Object| 按照業務類型統計的總的返佣數據  
> spot| array| Object. 現貨交易的返佣. 如果沒有對應的返佣或者沒有查詢該類型, 則返回空數組 `[]`  
>> coin| string| 返佣幣種  
>> earning| string| 返佣金額  
> derivatives| array| Object. 期貨交易的返佣. 如果沒有對應的返佣或者沒有查詢該類型, 則返回空數組 `[]`  
>> coin| string| 返佣幣種  
>> earning| string| 返佣金額  
> options| array| Object. 期權交易的返佣. 如果沒有對應的返佣或者沒有查詢該類型, 則返回空數組 `[]`  
>> coin| string| 返佣幣種  
>> earning| string| 返佣金額  
> convert| array| Object. 閃兌交易的返佣. 如果沒有對應的返佣或者沒有查詢該類型, 則返回空數組 `[]`  
>> coin| string| 返佣幣種  
>> earning| string| 返佣金額  
> total| array| Object. 所有業務類型的返佣總和. 如果沒有對應的返佣或者沒有查詢該類型, 則返回空數組 `[]`  
>> coin| string| 返佣幣種  
>> earning| string| 返佣金額  
details| array| Object. 每個子UID以及每個業務類型的交易細節  
> userId| string| 子帳戶  
> bizType| string| 業務類型. `SPOT`, `DERIVATIVES`, `OPTIONS`, `CONVERT`  
> symbol| string| 幣對名  
> coin| string| 返佣幣種  
> earning| string| 返佣金額  
> markupEarning| string| 加點佣金  
> baseFeeEarning| string| 基礎佣金  
> orderId| string| 訂單ID  
> execId| string| 成交ID  
> execTime| string| 訂單執行時間戳 (毫秒)  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/broker/earnings-info?begin=20231129&end=20231129&uid=117894077 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1701399431920  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: 32d2aa1bc205ddfb89849b85e2a8b7e23b1f8f69fe95d6f2cb9c87562f9086a6  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_exchange_broker_earnings(  
        begin="20231129",  
        end="20231129",  
        uid="117894077",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getExchangeBrokerEarnings({  
        bizType: 'SPOT',  
        begin: '20231201',  
        end: '20231207',  
        limit: 1000,  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "totalEarningCat": {  
                "spot": [],  
                "derivatives": [  
                    {  
                        "coin": "USDT",  
                        "earning": "0.00027844"  
                    }  
                ],  
                "options": [],  
                "total": [  
                    {  
                        "coin": "USDT",  
                        "earning": "0.00027844"  
                    }  
                ]  
            },  
            "details": [  
                {  
                    "userId": "117894077",  
                    "bizType": "DERIVATIVES",  
                    "symbol": "DOGEUSDT",  
                    "coin": "USDT",  
                    "earning": "0.00016166",  
                    "markupEarning": "0.000032332",  
                    "baseFeeEarning": "0.000129328",  
                    "orderId": "ec2132f2-a7e0-4a0c-9219-9f3cbcd8e878",  
                    "execId": "c8f418a0-2ccc-594f-ae72-effedf24d0c4",  
                    "execTime": "1701275846033"  
                },  
                {  
                    "userId": "117894077",  
                    "bizType": "DERIVATIVES",  
                    "symbol": "TRXUSDT",  
                    "coin": "USDT",  
                    "earning": "0.00011678",  
                    "markupEarning": "0.000023356",  
                    "baseFeeEarning": "0.000093424",  
                    "orderId": "28b29c2b-ba14-450e-9ce7-3cee0c1fa6da",  
                    "execId": "632c7705-7f3a-5350-b69c-d41a8b3d0697",  
                    "execTime": "1701245285017"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1701398193964  
    }