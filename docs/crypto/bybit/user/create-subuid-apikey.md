---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/create-subuid-apikey
api_type: REST
updated_at: 2026-07-03 19:17:30.420833
---

# Get Sub Account All API Keys

Query all api keys information of a sub UID.

tip

  * Any permission can access this endpoint
  * Only master account can call this endpoint



### HTTP Request

GET`/v5/user/sub-apikeys`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
subMemberId| **true**|  string| Sub UID  
limit| false| integer| Limit for data size per page. [`1`, `20`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Object  
> id| string| Unique ID. Internal use  
> ips| array<string>| IP bound  
> apiKey| string| Api key  
> note| string| The remark  
> status| integer| `1`: permanent, `2`: expired, `3`: within the validity period, `4`: expires soon (less than 7 days)  
> expiredAt| datetime| The expiry day of the api key. Only for those api key with no IP bound or the password has been changed  
> createdAt| datetime| The create day of the api key  
> type| integer| The type of api key. `1`: personal, `2`: connected to the third-party app  
> permissions| Object| The types of permission  
>> ContractTrade| array| Permission of contract trade `Order`, `Position`  
>> Spot| array| Permission of spot `SpotTrade`  
>> Wallet| array| Permission of wallet `AccountTransfer`, `SubMemberTransferList`  
>> Options| array| Permission of USDC Contract. It supports trade option and USDC perpetual. `OptionsTrade`  
>> Derivatives| array| `DerivativesTrade`  
>> Exchange| array| Permission of convert `ExchangeHistory`  
>> Earn| array| Permission of earn product `Earn`  
>> Affiliate| array| Not applicable to sub account, always `[]`  
>> BlockTrade| array| Not applicable to subaccount, always `[]`  
>> NFT| array| **Deprecated** , always `[]`  
>> CopyTrading| array| **Deprecated** , always `[]`  
> secret| string| Always `"******"`  
> readOnly| boolean| `true`, `false`  
> deadlineDay| integer| The remaining valid days of api key. Only for those api key with no IP bound or the password has been changed  
> flag| string| Api key type  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/user/list-sub-apikeys)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/sub-apikeys?subMemberId=100400345 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1699515251088  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_all_sub_api_keys(  
        subMemberId="100400345",  
        limit=20  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSubAccountAllApiKeys({  
        subMemberId: 'subUID',  
        limit: 20,  
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
        "retMsg": "",  
        "result": {  
            "result": [  
                {  
                    "id": "24828209",  
                    "ips": [  
                        "*"  
                    ],  
                    "apiKey": "XXXXXX",  
                    "note": "UTA",  
                    "status": 3,  
                    "expiredAt": "2023-12-01T02:36:06Z",  
                    "createdAt": "2023-08-25T06:42:39Z",  
                    "type": 1,  
                    "permissions": {  
                        "ContractTrade": [  
                            "Order",  
                            "Position"  
                        ],  
                        "Spot": [  
                            "SpotTrade"  
                        ],  
                        "Wallet": [  
                            "AccountTransfer",  
                            "SubMemberTransferList"  
                        ],  
                        "Options": [  
                            "OptionsTrade"  
                        ],  
                        "Derivatives": [  
                            "DerivativesTrade"  
                        ],  
                        "CopyTrading": [],  
                        "BlockTrade": [],  
                        "Exchange": [  
                            "ExchangeHistory"  
                        ],  
                        "NFT": [],  
                        "Affiliate": [],  
                        "Earn": []  
                    },  
                    "secret": "******",  
                    "readOnly": false,  
                    "deadlineDay": 21,  
                    "flag": "hmac"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1699515251698  
    }

---

# 查詢子帳戶的所有API Key信息

查詢某個子帳戶下所有的api key

提示

  * 任意權限可以訪問該接口
  * 僅支持母帳戶調用



### HTTP 請求

GET`/v5/user/sub-apikeys`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
subMemberId| **true**|  string| 子帳戶UID  
limit| false| integer| 每頁數量限制. [`1`, `20`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
result| array| Object  
> id| string| 唯一id. 內部使用  
> ips| array<string>| 綁定的IP, 未綁定IP則是`*`  
> apiKey| string| Api key  
> note| string| 備註  
> status| integer| 當前狀態 `1`: 永久, `2`: 已過期, `3`: 仍在有效期內, `4`: 即將過期 (少於7天)  
> expiredAt| datetime| API key的過期日. 針對那些未綁定IP的api key或者修改過密碼的帳戶  
> createdAt| datetime| API key的創建日  
> type| integer| Api key類型. `1`：個人使用, `2`：綁定到第三方應用  
> permissions| Object| 權限類型  
>> ContractTrade| array| 合約交易的權限 `Order`, `Position`  
>> Spot| array| 現貨交易的權限 `SpotTrade`  
>> Wallet| array| 錢包的權限 `AccountTransfer`, `SubMemberTransferList`  
>> Options| array| USDC合約的權限. 該權限支持USDC合約下的期權和永續交易 `OptionsTrade`  
>> Derivatives| array| 統一交易帳戶默認賦予的權限  
>> Exchange| array| 兌換的權限 `ExchangeHistory`  
>> Earn| array| 理財產品的權限 `Earn`  
>> Affiliate| array| 子帳戶暫不支持, 總是 `[]`  
>> BlockTrade| array| 子帳戶暫不支持，總是[]  
>> NFT| array| **廢棄** , 總是[]  
>> CopyTrading| array| **廢棄** , 總是[]  
> secret| string| 總是`"******"`  
> readOnly| boolean| `true`：可讀可寫. `false`：只讀  
> deadlineDay| integer| API key失效的倒數日. 針對那些未綁定IP的api key或者修改過密碼的帳戶  
> flag| string| API Key的類型  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/user/list-sub-apikeys)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/sub-apikeys?subMemberId=100400345 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1699515251088  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSubAccountAllApiKeys({  
        subMemberId: 'subUID',  
        limit: 20,  
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
        "retMsg": "",  
        "result": {  
            "result": [  
                {  
                    "id": "24828209",  
                    "ips": [  
                        "*"  
                    ],  
                    "apiKey": "XXXXXX",  
                    "note": "UTA",  
                    "status": 3,  
                    "expiredAt": "2023-12-01T02:36:06Z",  
                    "createdAt": "2023-08-25T06:42:39Z",  
                    "type": 1,  
                    "permissions": {  
                        "ContractTrade": [  
                            "Order",  
                            "Position"  
                        ],  
                        "Spot": [  
                            "SpotTrade"  
                        ],  
                        "Wallet": [  
                            "AccountTransfer",  
                            "SubMemberTransferList"  
                        ],  
                        "Options": [  
                            "OptionsTrade"  
                        ],  
                        "Derivatives": [  
                            "DerivativesTrade"  
                        ],  
                        "CopyTrading": [],  
                        "BlockTrade": [],  
                        "Exchange": [  
                            "ExchangeHistory"  
                        ],  
                        "NFT": [],  
                        "Affiliate": []  
                    },  
                    "secret": "******",  
                    "readOnly": false,  
                    "deadlineDay": 21,  
                    "flag": "hmac"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1699515251698  
    }