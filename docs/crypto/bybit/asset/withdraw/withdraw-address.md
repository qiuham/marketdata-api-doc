---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/withdraw/withdraw-address
api_type: REST
updated_at: 2026-11-13 19:21:56.608507
---

# Get Withdrawal Address List

Query the withdrawal addresses in the address book.

tip

  * The API key for querying this endpoint must have withdrawal permissions.



### HTTP Request

GET`/v5/asset/withdraw/query-address`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Coin: 

  * When passing `coin=baseCoin`, it refers to the universal addresses.
  * When passing a coin name, it refers to the regular address on the chain.

  
chain| false| string| Chain name:

  * When only passing the chain name, it returns both regular addresses and universal addresses.
  * When passing the chain name and `coin=baseCoin`, it only returns the universal address corresponding to the chain.

  
addressType| false| integer| Address type. `0`: OnChain Address Type(Regular Address Type and Universal Address Type). `1`: Internal Transfer Address Type(Invalid "coin" & "chain" Parameters) `2`: On chain address and internal transfer address type (Invalid "coin" & "chain" Parameters)  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
rows| array| Object  
> coin| string| Coin  
> chain| string| Chain name  
> address| string| Address  
> tag| string| Address tag  
> remark| string| remark  
> status| integer| Address status:`0`: Normal. `1`: New Addresses are prohibited from withdrawing coins for 24 Hours.  
> addressType| integer| Address type. `0`: OnChain Address Type(Regular Address Type And Universal Address Type) `1`: Internal Transfer Address Type. `2`: Internal Transfer Address Type And OnChain Address Type  
> verified| integer| Whether the address has been verified or not: `0`: Unverified Address. `1`: Verified Address.  
> createAt| string| Address create time  
nextPageCursor| string| Cursor. Used for pagination  
  
* * *

### Request Example

  * HTTP


    
    
    GET /v5/asset/withdraw/query-address HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672194949557  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "rows": [  
                {  
                    "coin": "USDT",  
                    "chain": "ETH",  
                    "address": "0x48101adb67d426cb15e46be5f1d9f6ab25f311ea",  
                    "tag": "",  
                    "remark": "",  
                    "status": 0,  
                    "addressType": 0,  
                    "verified": 0,  
                    "createdAt": "1760951195"  
                },  
                {  
                    "coin": "baseCoin",  
                    "chain": "ETH",  
                    "address": "0x48101adb67d426cb15e46be5f1d9f6ab25f311ea",  
                    "tag": "",  
                    "remark": "Universal Address",  
                    "status": 0,  
                    "addressType": 0,  
                    "verified": 0,  
                    "createdAt": "1760951332"  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTA1MDgsIm1heElEIjoxMDUwOX0="  
        },  
        "retExtInfo": {},  
        "time": 1760960379395  
    }

---

# 查詢地址簿提幣地址

查詢地址簿中的提幣地址

提示

  * 查詢此端點的apikey必須具備提幣權限.



### HTTP 請求

GET`/v5/asset/withdraw/query-address`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 幣種：

  * 當傳入 `coin=baseCoin` 時，表示通用地址
  * 當傳入幣種名稱時，表示此幣種的鏈上地址

  
chain| false| string| 鏈名稱：

  * 僅傳入鏈名稱時，返回普通地址和通用地址
  * 傳入鏈名稱 + `coin=baseCoin`時，僅返回該鏈對應的通用地址

  
addressType| false| integer| 地址類型:`0`:鏈上地址類型（普通地址類型和通用地址類型）`1`:內部轉賬地址類型（"coin" 和 "chain" 參數無效）`2`:鏈上地址和內部轉賬地址類型（"coin" 和 "chain" 參數無效）  
limit| false| integer| 每頁數據大小的限制。範圍:[`1`, `50`]。默認值:`50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
rows| array| Object  
> coin| string| 幣種  
> chain| string| 鏈名稱  
> address| string| 地址  
> tag| string| 地址標籤  
> remark| string| 備註  
> status| integer| 地址狀態：`0`:正常`1`:新地址禁止提幣 24 小時  
> addressType| integer| 地址類型:`0`:鏈上地址類型（普通地址類型和通用地址類型）`1`:內部轉賬地址類型`2`:內部轉賬地址類型和鏈上地址類型  
> verified| integer| 地址是否已驗證:`0`:未驗證地址`1`:已驗證地址  
> createAt| string| 地址創建時間  
nextPageCursor| string| 游標，用於分頁  
  
* * *

### 請求示例

  * HTTP


    
    
    GET /v5/asset/withdraw/query-address HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672194949557  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "rows": [  
                {  
                    "coin": "USDT",  
                    "chain": "ETH",  
                    "address": "0x48101adb67d426cb15e46be5f1d9f6ab25f311ea",  
                    "tag": "",  
                    "remark": "",  
                    "status": 0,  
                    "addressType": 0,  
                    "verified": 0,  
                    "createdAt": "1760951195"  
                },  
                {  
                    "coin": "baseCoin",  
                    "chain": "ETH",  
                    "address": "0x48101adb67d426cb15e46be5f1d9f6ab25f311ea",  
                    "tag": "",  
                    "remark": "Universal Address",  
                    "status": 0,  
                    "addressType": 0,  
                    "verified": 0,  
                    "createdAt": "1760951332"  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTA1MDgsIm1heElEIjoxMDUwOX0="  
        },  
        "retExtInfo": {},  
        "time": 1760960379395  
    }