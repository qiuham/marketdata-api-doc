---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/delivery
api_type: REST
updated_at: 2026-07-16 18:50:19.729950
---

# Get Delivery Record

Query delivery records of Invese Futures, USDC Futures, USDT Futures and Options, sorted by `deliveryTime` in descending order

info

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/asset/delivery-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `inverse`(inverse futures), `linear`(USDT/USDC futures), `option`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
startTime| false| integer| The start timestamp (ms) 

  * startTime and endTime are not passed, return 30 days by default
  * Only startTime is passed, return range between startTime and startTime + 30 days 
  * Only endTime is passed, return range between endTime - 30 days and endTime
  * If both are passed, the rule is endTime - startTime <= 30 days

  
endTime| false| integer| The end timestamp (ms)  
expDate| false| string| Expiry date. `25MAR22`. Default: return all  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> deliveryTime| number| Delivery time (ms)  
> symbol| string| Symbol name  
> side| string| `Buy`,`Sell`  
> position| string| Executed size  
> entryPrice| string| Avg entry price  
> deliveryPrice| string| Delivery price  
> strike| string| Exercise price  
> fee| string| Trading fee  
> deliveryRpl| string| Realized PnL of the delivery  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/asset/delivery)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/delivery-record?expDate=29DEC22&category=option HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672362112944  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_option_delivery_record(  
        category="option",  
        expDate="29DEC22",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getDeliveryRecord({ category: 'option', expDate: '29DEC22' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "132791%3A0%2C132791%3A0",  
            "category": "option",  
            "list": [  
                {  
                    "symbol": "BTC-29DEC22-16000-P",  
                    "side": "Buy",  
                    "deliveryTime": 1672300800860,  
                    "strike": "16000",  
                    "fee": "0.00000000",  
                    "position": "0.01",  
                    "deliveryPrice": "16541.86369547",  
                    "deliveryRpl": "3.5"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672362116184  
    }

---

# 查詢交割紀錄

查詢反向交割 / USDT交割 / USDC交割 / 期權的交割紀錄, 返回結果按照`deliveryTime`降序排列

信息

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP 請求

GET`/v5/asset/delivery-record`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `inverse`(反向交割), `linear`(USDT/USDC交割), `option`(期權交割)  
symbol| false| string| 合約名稱  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近30天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 30天
  * 若只傳startTime，則查詢startTime和startTime+30天的數據
  * 若只傳endTime，則查詢endTime-30天和endTime的數據

  
endTime| false| integer| 結束時間 (毫秒)  
expDate| false| string| 過期日. 格式示例: `25MAR22`. 默認: 返回所有日期數據  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> deliveryTime| number| 交割時間戳 (毫秒)  
> symbol| string| 合約名稱  
> side| string| `Buy`,`Sell`  
> position| string| 交割數量  
> entryPrice| string| 平均入場價  
> deliveryPrice| string| 交割價格  
> strike| string| 行權價  
> fee| string| 手續費，正數表支出，負數表收取  
> deliveryRpl| string| 交割已實現盈虧  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/asset/delivery)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/delivery-record?expDate=29DEC22&category=option HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672362112944  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_option_delivery_record(  
        category="option",  
        expDate="29DEC22",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getDeliveryRecord({ category: 'option', expDate: '29DEC22' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "132791%3A0%2C132791%3A0",  
            "category": "option",  
            "list": [  
                {  
                    "symbol": "BTC-29DEC22-16000-P",  
                    "side": "Buy",  
                    "deliveryTime": 1672300800860,  
                    "strike": "16000",  
                    "fee": "0.00000000",  
                    "position": "0.01",  
                    "deliveryPrice": "16541.86369547",  
                    "deliveryRpl": "3.5"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672362116184  
    }