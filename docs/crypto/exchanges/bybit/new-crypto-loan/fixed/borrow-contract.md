---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/borrow-contract
api_type: REST
updated_at: 2026-05-27 19:18:44.147907
---

# Get Borrow Order Info

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-fixed/borrow-order-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
orderCurrency| false| string| Loan coin name  
state| false| string| Borrow order status, `1`: matching; `2`: partially filled and cancelled; `3`: Fully filled; `4`: Cancelled  
term| false| string| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> annualRate| string| Annual rate for the borrowing  
> orderId| long| Loan order ID  
> orderTime| string| Order created time  
> filledQty| string| Filled qty  
> orderQty| string| Order qty  
> orderCurrency| string| Coin name  
> state| integer| Borrow order status, `1`: matching; `2`: partially filled and cancelled; `3`: Fully filled; `4`: Cancelled; `5`: fail  
> term| integer| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
> repayType| string| `1`:Auto Repayment; `2`:Transfer to flexible loan; `0`: No Automatic Repayment. Compatible with existing orders;  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/borrow-order-info?orderId=13010 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752655239825  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrowing_orders_fixed_crypto_loan(  
        orderId="13010"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "0.01",  
                    "filledQty": "0",  
                    "orderCurrency": "MANA",  
                    "orderId": 13010,  
                    "orderQty": "2000",  
                    "orderTime": "1752654035179",  
                    "repayType": "2",  
                    "state": 1,  
                    "term": 30  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1752655241090  
    }

---

# 查詢個人借款訂單

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-fixed/borrow-order-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借款訂單 ID  
orderCurrency| false| string| 借款幣種名稱  
state| false| string| 借款訂單狀態，`1`: 等待匹配; `2`: 部分成交並已取消；`3`: 全部成交；`4`: 已取消  
term| false| string| 固定期限 `7`: 7 天；`14`: 14 天；`30`: 30 天；`90`: 90 天；`180`: 180 天  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> annualRate| string| 借款年化利率  
> orderId| long| 借款訂單 ID  
> orderTime| string| 訂單建立時間  
> filledQty| string| 成交數量  
> orderQty| string| 訂單數量  
> orderCurrency| string| 幣種名稱  
> state| integer| 借款訂單狀態，`1`: 等待匹配；`2`: 部分成交並已取消；`3`: 全部成交；`4`: 已取消；`5`: 失敗  
> term| integer| 固定期限 `7`: 7 天；`14`: 14 天；`30`: 30 天；`90`: 90 天；`180`: 180 天  
> repayType| string| `1`:自動還款; `2`:轉活期; `0`: 不自動還款. 兼容存量訂單;  
nextPageCursor| string| 下一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/borrow-order-info?orderId=13010 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752655239825  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "0.01",  
                    "filledQty": "0",  
                    "orderCurrency": "MANA",  
                    "orderId": 13010,  
                    "orderQty": "2000",  
                    "orderTime": "1752654035179",  
                    "repayType": "2",  
                    "state": 1,  
                    "term": 30  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1752655241090  
    }