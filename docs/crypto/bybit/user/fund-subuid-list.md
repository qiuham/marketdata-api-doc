---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/fund-subuid-list
api_type: REST
updated_at: 2026-07-01 19:32:57.835934
---

# Modify Sub API Key

Modify the settings of sub api key. Use the sub account api key pending to be modified to call the endpoint or use master account api key to manage its sub account api key.

tip

The API key must have one of the below permissions in order to call this endpoint

  * sub API key: "Account Transfer", "Sub Member Transfer"
  * master API Key: "Account Transfer", "Sub Member Transfer", "Withdrawal"



### HTTP Request

POST`/v5/user/update-sub-api`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
apikey| false| string| Sub account api key 

  * You must pass this param when you use master account manage sub account api key settings
  * If you use corresponding sub uid api key call this endpoint, `apikey` param cannot be passed, otherwise throwing an error

  
readOnly| false| integer| `0` (default): Read and Write. `1`: Read only  
ips| false| string| Set the IP bind. example: `"192.168.0.1,192.168.0.2"`**note:**

  * don't pass ips or pass with `"*"` means no bind
  * No ip bound api key will be **invalid after 90 days**
  * api key will be invalid after **7 days** once the account password is changed

  
permissions| false| Object| Tick the types of permission. Don't send this param if you don't want to change the permission  
> ContractTrade| false| array| Contract Trade. `["Order","Position"]`  
> Spot| false| array| Spot Trade. `["SpotTrade"]`  
> Wallet| false| array| Wallet. `["AccountTransfer", "SubMemberTransferList"]`  
_Note: fund custodial account is not supported_  
> Options| false| array| USDC Contract. `["OptionsTrade"]`  
> Derivatives| false| array| `["DerivativesTrade"]`  
> Exchange| false| array| Convert. `["ExchangeHistory"]`  
> Earn| false| array| Earn product. `["Earn"]`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Unique id. Internal used  
note| string| The remark  
apiKey| string| Api key  
readOnly| integer| `0`: Read and Write. `1`: Read only  
secret| string| Always `""`  
permissions| Object| The types of permission  
> ContractTrade| array| Permisson of contract trade  
> Spot| array| Permisson of spot  
> Wallet| array| Permisson of wallet  
> Options| array| Permission of USDC Contract. It supports trade option and usdc perpetual.  
> Derivatives| array| Permission of Unified account  
> Exchange| array| Permission of convert  
> Earn| array| Permission of Earn  
> BlockTrade| array| Not applicable to sub account, always `[]`  
> Affiliate| array| Not applicable to sub account, always `[]`  
> FiatP2P| array| Not applicable to sub account, always `[]`  
> FiatConvertBroker| array| Not applicable to sub account, always `[]`  
> NFT| array| **Deprecated** , always `[]`  
> CopyTrading| array| **Deprecated** , always `[]`  
ips| array| IP bound  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/update-sub-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676431795752  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "readOnly": 0,  
        "ips": "*",  
        "permissions": {  
                "ContractTrade": [],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer"  
                ],  
                "Options": [],  
                "CopyTrading": [],  
                "BlockTrade": [],  
                "Exchange": [],  
                "NFT": []  
            }  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.modify_sub_api_key(  
        readOnly=0,  
        ips="*",  
        permissions={  
                "ContractTrade": [],  
                "Spot": [  
                    "SpotTrade"  
                ],  
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
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .updateSubApiKey({  
        readOnly: 0,  
        ips: ['*'],  
        permissions: {  
          ContractTrade: [],  
          Spot: ['SpotTrade'],  
          Wallet: ['AccountTransfer'],  
          Options: [],  
          Derivatives: [],  
          CopyTrading: [],  
          BlockTrade: [],  
          Exchange: [],  
          NFT: [],  
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
            "id": "16651472",  
            "note": "testxxx",  
            "apiKey": "xxxxxx",  
            "readOnly": 0,  
            "secret": "",  
            "permissions": {  
                "ContractTrade": [],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer"  
                ],  
                "Options": [],  
                "Derivatives": [],  
                "CopyTrading": [],  
                "BlockTrade": [],  
                "Exchange": [],  
                "NFT": []  
            },  
            "ips": [  
                "*"  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1676431796263  
    }

---

# 修改子帳戶的API Key設置

修改子帳戶API key的設置, 支持母帳戶管理子帳戶key的設置, 或者子帳戶key直接修改本身。

提示

在調用接口時，使用的API key至少需要擁有以下其中一種權限

  * 子API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）"
  * 母API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）", "Withdrawal（提幣）"



### HTTP 請求

POST`/v5/user/update-sub-api`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
apikey| false| string| 子帳戶的api key 

  * 當您要使用母帳戶來管理子帳戶的key時, 該字段必傳
  * 如果您是用對應的子帳戶api key修改本身, 該字段請不要傳入, 否則報錯

  
readOnly| false| integer| `0` (默認)：可讀可寫. `1`：只讀  
ips| false| string| 綁定IP. 比如: "192.168.0.1,192.168.0.2"**注意:**

  * 不傳參數ips 或者入参值為`"*"`意味著不綁定
  * 不綁定IP的api key將有**90天的有效期限**
  * 一旦帳戶密碼做了修改，帳戶下的非永久api key將在**7天後失效**

  
permissions| false| Object| 勾選api key權限. 如果不修改權限, 則不要傳入該參數  
> ContractTrade| false| array| 合約. ["Order","Position"]  
> Spot| false| array| 現貨. ["SpotTrade"]  
> Wallet| false| array| 錢包. ["AccountTransfer","SubMemberTransferList"]  
> Options| false| array| USDC合約和期權. ["OptionsTrade"]  
> Derivatives| false| array| 統一帳戶權限. ["DerivativesTrade"]  
> Exchange| false| array| 兌換. ["ExchangeHistory"]  
> Earn| false| array| 理財產品的權限 ["Earn"]  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
id| string| 唯一id. 內部使用  
note| string| 備註  
apiKey| string| api key  
readOnly| integer| `0`：可讀可寫. `1`：只讀  
secret| string| 總是 `""`  
permissions| Object| 權限類型  
> ContractTrade| array| 合約交易的權限  
> Spot| array| 現貨交易的權限  
> Wallet| array| 錢包的權限  
> Options| array| USDC合約和期權  
> Derivatives| array| 統一帳戶權限  
> Exchange| array| 兌換的權限  
> Earn| array| 理財產品的權限 ["Earn"]  
> BlockTrade| array| 子帳戶暫不支持，總是[]  
> FiatP2P| array| 子帳戶暫不支持，總是[]  
> FiatConvertBroker| array| 子帳戶暫不支持，總是[]  
> Affiliate| array| 子帳戶暫不支持，總是[]  
> NFT| array| **廢棄** , 總是[]  
> CopyTrading| array| **廢棄** , 總是[]  
ips| array| IP綁定  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/update-sub-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676431795752  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "readOnly": 0,  
        "ips": "*",  
        "permissions": {  
                "ContractTrade": [],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer"  
                ],  
                "Options": [],  
                "CopyTrading": [],  
                "BlockTrade": [],  
                "Exchange": [],  
                "NFT": []  
            }  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.modify_sub_api_key(  
        readOnly=0,  
        ips=["*"],  
        permissions={  
                "ContractTrade": [],  
                "Spot": [  
                    "SpotTrade"  
                ],  
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
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .updateSubApiKey({  
        readOnly: 0,  
        ips: ['*'],  
        permissions: {  
          ContractTrade: [],  
          Spot: ['SpotTrade'],  
          Wallet: ['AccountTransfer'],  
          Options: [],  
          Derivatives: [],  
          CopyTrading: [],  
          BlockTrade: [],  
          Exchange: [],  
          NFT: [],  
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
            "id": "16651472",  
            "note": "testxxx",  
            "apiKey": "xxxxxx",  
            "readOnly": 0,  
            "secret": "",  
            "permissions": {  
                "ContractTrade": [],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer"  
                ],  
                "Options": [],  
                "Derivatives": [],  
                "CopyTrading": [],  
                "BlockTrade": [],  
                "Exchange": [],  
                "NFT": []  
            },  
            "ips": [  
                "*"  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1676431796263  
    }