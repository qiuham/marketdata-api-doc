---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/create-subuid-apikey
api_type: REST
updated_at: 2026-07-29 18:54:06.707996
---

# Create Sub UID API Key

To create new API key for those newly created sub UID. Use **master user's api key** **only**.

tip

The API key must have one of the below permissions in order to call this endpoint..

  * master API key: "Account Transfer", "Subaccount Transfer", "Withdrawal"



### HTTP Request

POST`/v5/user/create-sub-api`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
subuid| **true**|  integer| Sub user Id  
note| false| string| Set a remark  
readOnly| **true**|  integer| `0`: Read and Write. `1`: Read only  
ips| false| string| Set the IP bind. example: `"192.168.0.1,192.168.0.2"`**note:**

  * don't pass ips or pass with `"*"` means no bind
  * No ip bound api key will be **invalid after 90 days**
  * api key without IP bound will be invalid after **7 days** once the account password is changed

  
permissions| **true**|  Object| Tick the types of permission.

  * one of below types must be passed, otherwise the error is thrown

  
> ContractTrade| false| array| Contract Trade. `["Order","Position"]`  
> Spot| false| array| Spot Trade. `["SpotTrade"]`  
> Options| false| array| USDC Contract. `["OptionsTrade"]`  
> Wallet| false| array| Wallet. `["AccountTransfer","SubMemberTransferList"]`  
_Note: Fund Custodial account is not supported_  
> Exchange| false| array| Convert. `["ExchangeHistory"]`  
> Earn| false| array| Earn product. `["Earn"]`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Unique id. Internal used  
note| string| The remark  
apiKey| string| Api key  
readOnly| integer| `0`: Read and Write. `1`: Read only  
secret| string| The secret paired with api key.

  * The secret can't be queried by GET api. Please keep it properly

  
permissions| Object| The types of permission  
> ContractTrade| array| Permisson of contract trade  
> Spot| array| Permisson of spot  
> Wallet| array| Permisson of wallet  
> Options| array| Permission of USDC Contract. It supports trade option and usdc perpetual.  
> Derivatives| array| Permission of Unified account  
> Exchange| array| Permission of convert  
> Earn| array| Permission of earn product  
> BlockTrade| array| Not applicable to sub account, always `[]`  
> Affiliate| array| Not applicable to sub account, always `[]`  
> FiatP2P| array| Not applicable to sub account, always `[]`  
> FiatConvertBroker| array| Not applicable to sub account, always `[]`  
> NFT| array| **Deprecated** , always `[]`  
> CopyTrading| array| **Deprecated** always `[]`  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/create-sub-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430005459  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "subuid": 53888000,  
        "note": "testxxx",  
        "readOnly": 0,  
        "permissions": {  
            "Wallet": [  
                "AccountTransfer"  
            ]  
        }  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_sub_api_key(  
        subuid=53888000,  
        note="testxxx",  
        readOnly=0,  
        permissions={  
            "Wallet": [  
                "AccountTransfer"  
            ]  
        },  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .createSubUIDAPIKey({  
        subuid: 53888000,  
        note: 'testxxx',  
        readOnly: 0,  
        permissions: {  
          Wallet: ['AccountTransfer'],  
        },  
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
            "id": "16651283",  
            "note": "testxxx",  
            "apiKey": "xxxxx",  
            "readOnly": 0,  
            "secret": "xxxxxxxx",  
            "permissions": {  
                "ContractTrade": [],  
                "Spot": [],  
                "Wallet": [  
                    "AccountTransfer"  
                ],  
                "Options": [],  
                "CopyTrading": [],  
                "BlockTrade": [],  
                "Exchange": [],  
                "NFT": [],  
                "Earn": ["Earn"]  
            }  
        },  
        "retExtInfo": {},  
        "time": 1676430007643  
    }

---

# 新建子帳戶的API Key

給新建好的子帳戶創建新的API key。需使用**母** 帳戶的API key。

提示

在調用接口時，使用的API key至少需要擁有以下其中一種權限

  * 母API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）", "Withdrawal（提幣）"



### HTTP 請求

POST`/v5/user/create-sub-api`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
subuid| **true**|  integer| 子帳戶userId  
note| false| string| 設置備註  
readOnly| **true**|  integer| `0`：可讀可寫. `1`：只讀  
ips| false| string| 綁定IP. 比如: "192.168.0.1,192.168.0.2"**注意:**

  * 不傳參數ips 或者入参值為`"*"`意味著不綁定
  * 不綁定IP的api key將有**90天的有效期限**
  * 一旦帳戶密碼做了修改，帳戶下的非永久api key將在**7天後失效**

  
permissions| **true**|  Object| 勾選api key權限.

  * 注意: 必須傳入以下權限類型的任意一種, 否則報錯

  
> ContractTrade| false| array| USDT合約, 幣本位合約. ["Order","Position"]  
> Spot| false| array| 現貨. ["SpotTrade"]  
> Wallet| false| array| 錢包. ["AccountTransfer","SubMemberTransferList"] _注意: 基金託管子帳戶不支持這兩個權限項_  
> Options| false| array| USDC合約和期權. ["OptionsTrade"]  
> Derivatives| false| array| ["DerivativesTrade"]  
> Exchange| false| array| 兌換. ["ExchangeHistory"]  
> Earn| false| array| 理財產品的權限 ["Earn"]  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
id| string| 唯一id. 內部使用  
note| string| 備註  
apiKey| string| Api key  
readOnly| integer| `0`：可讀可寫. `1`：只讀  
secret| string| Api密鑰密碼.

  * 注意: Api密鑰密碼只會在這裡出現一次，除此之外沒有任何地方還可以獲取到密碼。請妥善保存。

  
permissions| Object| 權限類型  
> ContractTrade| array| 合約交易的權限  
> Spot| array| 現貨交易的權限  
> Wallet| array| 錢包的權限  
> Options| array| USDC合約和期權  
> Derivatives| array| 統一帳戶權限  
> Earn| array| 理財產品的權限 `Earn`  
> Exchange| array| 兌換的權限  
> BlockTrade| array| 子帳戶暫不支持，總是[]  
> FiatP2P| array| 子帳戶暫不支持，總是[]  
> FiatConvertBroker| array| 子帳戶暫不支持，總是[]  
> Affiliate| array| 子帳戶暫不支持，總是[]  
> NFT| array| **廢棄** , 總是[]  
> CopyTrading| array| **廢棄** , 總是[]  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/create-sub-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430005459  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "subuid": 53888000,  
        "note": "testxxx",  
        "readOnly": 0,  
        "permissions": {  
            "Wallet": [  
                "AccountTransfer"  
            ]  
        }  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_sub_api_key(  
        subuid=53888000,  
        note="testxxx",  
        readOnly=0,  
        permissions={  
            "Wallet": [  
                "AccountTransfer"  
            ]  
        },  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .createSubUIDAPIKey({  
        subuid: 53888000,  
        note: 'testxxx',  
        readOnly: 0,  
        permissions: {  
          Wallet: ['AccountTransfer'],  
        },  
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
            "id": "16651283",  
            "note": "testxxx",  
            "apiKey": "xxxxx",  
            "readOnly": 0,  
            "secret": "xxxxxxxx",  
            "permissions": {  
                "ContractTrade": [],  
                "Spot": [],  
                "Wallet": [  
                    "AccountTransfer"  
                ],  
                "Options": [],  
                "Derivatives": [],  
                "CopyTrading": [],  
                "BlockTrade": [],  
                "Exchange": [],  
                "NFT": []  
            }  
        },  
        "retExtInfo": {},  
        "time": 1676430007643  
    }