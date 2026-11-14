---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bybit-card/point/item-list
api_type: REST
updated_at: 2026-11-13 19:22:19.625587
---

# Query Mall Item List

Query the list of items available in the card reward mall. Supports pagination, sorting, and filtering by item type.

### HTTP Request

POST`/v5/card/reward/mall/item/list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
pageNo| false| integer| Page number. Default: `1`. Min: `1`  
pageSize| false| integer| Number of items per page. Default: `10`. Min: `1`  
itemType| false| integer| Item type. `1`: Virtual item, `2`: Physical item  
itemBizType| false| integer| Item sub-type. `1`: POINTS, `2`: CURRENCY  
orderBy| false| integer| Sort type. `1`: Priority, `2`: Listing time, `3`: Price  
asc| false| boolean| Whether to sort in ascending order  
source| false| integer| Query source. `0`: Default, `1`: VIP item list  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Business return code. `0`: success; non-zero: failure  
retMsg| string| Return message  
result| object|   
> pageNo| integer| Current page number  
> pageSize| integer| Number of items per page  
> totalCount| integer| Total number of records  
> data| array| Item list  
>> itemId| string| Item ID  
>> itemName| string| Item name  
>> priority| integer| Priority  
>> onTime| string| Listing time (Unix ms timestamp)  
>> offTime| string| Delisting time (Unix ms timestamp)  
>> price| string| Price  
>> discountPrice| string| Discounted price  
>> totalNum| integer| Total quantity  
>> redeemNum| integer| Redeemed quantity  
>> picPath| string| Image path  
>> currency| string| Currency. `USDT`, `USDC`, `BTC`, `ETH`, `POINT`  
>> currencyType| integer| Currency type. `FIAT`, `CRYPTO`, `POINT`  
>> itemType| integer| Item type. `VIRTUAL`, `ENTITY`  
>> itemBizType| integer| Item sub-type. `POINTS`, `CURRENCY`  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/mall/item/list?pageNo=1&pageSize=10 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/mall/item/list"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    params = {  
        "pageNo": 1,  
        "pageSize": 10  
    }  
    response = requests.post(url, headers=headers, params=params)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/mall/item/list';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const params = { pageNo: 1, pageSize: 10 };  
      
    axios.post(url, {}, { headers, params })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pageNo": 1,  
            "pageSize": 10,  
            "totalCount": 5,  
            "data": [  
                {  
                    "itemId": "ITEM001",  
                    "itemName": "Amazon Gift Card $10",  
                    "priority": 1,  
                    "onTime": "1672211918471",  
                    "offTime": "1704000000000",  
                    "price": "5000",  
                    "discountPrice": "4500",  
                    "totalNum": 1000,  
                    "redeemNum": 200,  
                    "picPath": "/images/item001.png",  
                    "currency": "POINT",  
                    "currencyType": 3,  
                    "itemType": 1,  
                    "itemBizType": 1  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 查詢商城商品列表

查詢積分商城商品列表，支持分頁、排序及類型過濾。

### HTTP 請求

POST`/v5/card/reward/mall/item/list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
pageNo| false| integer| 頁碼，默認 `1`，最小值 `1`  
pageSize| false| integer| 每頁條數，默認 `10`，最小值 `1`  
itemType| false| integer| 商品類型。`1`: 虛擬商品，`2`: 實體商品  
itemBizType| false| integer| 商品子類型。`1`: POINTS，`2`: CURRENCY  
orderBy| false| integer| 排序類型。`1`: 優先級，`2`: 上架時間，`3`: 價格  
asc| false| boolean| 是否升序排列  
source| false| integer| 查詢來源。`0`: 默認，`1`: VIP 商品列表  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 業務返回碼。`0`: 成功；非零: 失敗  
retMsg| string| 返回消息  
result| object|   
> pageNo| integer| 當前頁碼  
> pageSize| integer| 每頁條數  
> totalCount| integer| 總記錄數  
> data| array| 商品列表  
>> itemId| string| 商品 ID  
>> itemName| string| 商品名稱  
>> priority| integer| 優先級  
>> onTime| string| 上架時間（Unix 毫秒時間戳）  
>> offTime| string| 下架時間（Unix 毫秒時間戳）  
>> price| string| 價格  
>> discountPrice| string| 折扣價  
>> totalNum| integer| 總數量  
>> redeemNum| integer| 已兌換數量  
>> picPath| string| 圖片路徑  
>> currency| string| 幣種。`USDT`、`USDC`、`BTC`、`ETH`、`POINT`  
>> currencyType| integer| 幣種類型。`FIAT`、`CRYPTO`、`POINT`  
>> itemType| integer| 商品類型。`VIRTUAL`、`ENTITY`  
>> itemBizType| integer| 商品子類型。`POINTS`、`CURRENCY`  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/mall/item/list?pageNo=1&pageSize=10 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/mall/item/list"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    params = {  
        "pageNo": 1,  
        "pageSize": 10  
    }  
    response = requests.post(url, headers=headers, params=params)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/mall/item/list';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const params = { pageNo: 1, pageSize: 10 };  
      
    axios.post(url, {}, { headers, params })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pageNo": 1,  
            "pageSize": 10,  
            "totalCount": 5,  
            "data": [  
                {  
                    "itemId": "ITEM001",  
                    "itemName": "Amazon Gift Card $10",  
                    "priority": 1,  
                    "onTime": "1672211918471",  
                    "offTime": "1704000000000",  
                    "price": "5000",  
                    "discountPrice": "4500",  
                    "totalNum": 1000,  
                    "redeemNum": 200,  
                    "picPath": "/images/item001.png",  
                    "currency": "POINT",  
                    "currencyType": 3,  
                    "itemType": 1,  
                    "itemBizType": 1  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }