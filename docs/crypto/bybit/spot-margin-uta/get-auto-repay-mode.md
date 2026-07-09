---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/get-auto-repay-mode
api_type: REST
updated_at: 2026-07-09 19:12:13.608496
---

# Get Historical Interest Rate

You can query up to six months borrowing interest rate of Margin trading.

info

  * Need authentication, the api key needs "Spot" permission
  * Only supports Unified account 
  * It is public data, i.e., different users get the same historical interest rate for the same VIP/Pro



### HTTP Request

GET`/v5/spot-margin-trade/interest-rate-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Coin name, uppercase only  
[vipLevel](/docs/v5/enum#viplevel)| false| string| VIP level 

  * Please note that "No VIP" should be passed like "No%20VIP" in the query string
  * If not passed, it returns your account's VIP level data

  
startTime| false| integer| The start timestamp (ms) 

  * Either both time parameters are passed or neither is passed.
  * Returns 7 days data when both are not passed
  * Supports up to 30 days interval when both are passed

  
endTime| false| integer| The end timestamp (ms)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array<object>|   
> timestamp| long| timestamp  
> currency| string| coin name  
> hourlyBorrowRate| string| Hourly borrowing rate  
> vipLevel| string| VIP/Pro level  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/spot-margin-trade/interest-rate-history?currency=USDC&vipLevel=No%20VIP&startTime=1721458800000&endTime=1721469600000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1721891663064  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_historical_interest_rate(  
        currency="BTC"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "timestamp": 1721469600000,  
                    "currency": "USDC",  
                    "hourlyBorrowRate": "0.000014621596",  
                    "vipLevel": "No VIP"  
                },  
                {  
                    "timestamp": 1721466000000,  
                    "currency": "USDC",  
                    "hourlyBorrowRate": "0.000014621596",  
                    "vipLevel": "No VIP"  
                },  
                {  
                    "timestamp": 1721462400000,  
                    "currency": "USDC",  
                    "hourlyBorrowRate": "0.000014621596",  
                    "vipLevel": "No VIP"  
                },  
                {  
                    "timestamp": 1721458800000,  
                    "currency": "USDC",  
                    "hourlyBorrowRate": "0.000014621596",  
                    "vipLevel": "No VIP"  
                }  
            ]  
        },  
        "retExtInfo": "{}",  
        "time": 1721899048991  
    }

---

# 查詢借貸歷史利率

您可以查詢最多過去6個月的借貸利率數據

信息

  * 需要鑒權, API密鑰需要有"現貨"權限
  * 僅支持統一帳戶訪問
  * 返回的是公共數據, i.e., 不同用戶在查詢相同的vip等級時, 拿到的是相同的歷史利率



### HTTP 請求

GET`/v5/spot-margin-trade/interest-rate-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 幣種名稱, 必須大寫  
[vipLevel](/docs/zh-TW/v5/enum#viplevel)| false| string| VIP等級 

  * 請注意對於"No VIP", 需要傳入"No%20VIP"
  * 若不傳, 則返回匹配您帳戶等級的數據

  
startTime| false| integer| 開始時間戳 (毫秒) 

  * 兩個時間參數要麼都傳要麼都不傳
  * 當都不傳時, 默認返回過去7天的數據
  * 當都傳時, 最多支持30天的時間跨度

  
endTime| false| integer| 結束時間戳 (毫秒)  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array<object>|   
> timestamp| long| 時間  
> currency| string| 幣種名稱  
> hourlyBorrowRate| string| 每小時利率  
> vipLevel| string| VIP等級  
  
### 請求示例

  * HTTP
  * Python


    
    
    GET /v5/spot-margin-trade/interest-rate-history?currency=USDC&vipLevel=No%20VIP&startTime=1721458800000&endTime=1721469600000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1721891663064  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "timestamp": 1721469600000,  
                    "currency": "USDC",  
                    "hourlyBorrowRate": "0.000014621596",  
                    "vipLevel": "No VIP"  
                },  
                {  
                    "timestamp": 1721466000000,  
                    "currency": "USDC",  
                    "hourlyBorrowRate": "0.000014621596",  
                    "vipLevel": "No VIP"  
                },  
                {  
                    "timestamp": 1721462400000,  
                    "currency": "USDC",  
                    "hourlyBorrowRate": "0.000014621596",  
                    "vipLevel": "No VIP"  
                },  
                {  
                    "timestamp": 1721458800000,  
                    "currency": "USDC",  
                    "hourlyBorrowRate": "0.000014621596",  
                    "vipLevel": "No VIP"  
                }  
            ]  
        },  
        "retExtInfo": "{}",  
        "time": 1721899048991  
    }