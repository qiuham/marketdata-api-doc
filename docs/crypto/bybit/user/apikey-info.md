---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/apikey-info
api_type: REST
updated_at: 2026-05-27 19:22:51.767876
---

# Get API Key Information

Get the information of the api key. Use the api key pending to be checked to call the endpoint. Both **master and sub user's api key** are applicable.

tip

Any permission can access this endpoint.

### HTTP Request

GET`/v5/user/query-api`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Unique ID. Internal use  
note| string| The remark  
apiKey| string| Api key  
readOnly| integer| `0`: Read and Write. `1`: Read only  
secret| string| Always `""`  
permissions| Object| The types of permission  
> ContractTrade| array| Permission of contract trade `Order`, `Position`  
> Spot| array| Permission of spot `SpotTrade`  
> Wallet| array| Permission of wallet `AccountTransfer`, `SubMemberTransfer`(master account), `SubMemberTransferList`(sub account), `Withdraw`(master account)  
> Options| array| Permission of USDC Contract. It supports trade option and USDC perpetual. `OptionsTrade`  
> Derivatives| array| `DerivativesTrade`  
> Exchange| array| Permission of convert `ExchangeHistory`  
> Earn| array| Permission of earn product `Earn`  
> FiatP2P| array| Permission of P2P `FiatP2POrder`, `Advertising`. Not applicable to subaccount, always `[]`  
> FiatBitPay| array| Permission of Bybit Pay `FaitPayOrder`. Not applicable to subaccount, always `[]`  
> FiatConvertBroker| array| Permission of fiat convert `FiatConvertBrokerOrder`. Not applicable to subaccount, always `[]`  
> BitCard| array| Bybit card permission, `BitCard`. Not applicable to subaccount  
> ByXPost| array| Community post permission, `ByXPost`. Not applicable to subaccount  
> Affiliate| array| Permission of Affiliate. Only affiliate can have this permission, otherwise always `[]`  
> BlockTrade| array| Permission of blocktrade. Not applicable to subaccount, always `[]`  
> NFT| array| **Deprecated** , always `[]`  
> CopyTrading| array| **Deprecated** , always `[]`  
ips| array| IP bound  
type| integer| The type of api key. `1`: personal, `2`: connected to the third-party app  
deadlineDay| integer| The remaining valid days of api key. Only for those api key with no IP bound or the password has been changed  
expiredAt| datetime| The expiry day of the api key. Only for those api key with no IP bound or the password has been changed  
createdAt| datetime| The create day of the api key  
uta| integer| Whether the account to which the account upgrade to unified trade account. `0`: regular account; `1`: unified trade account  
userID| integer| User ID  
inviterID| integer| Inviter ID (the UID of the account which invited this account to the platform)  
[vipLevel](/docs/v5/enum#viplevel)| string| VIP Level  
mktMakerLevel| string| Market maker level  
affiliateID| integer| Affiliate Id. `0` represents that there is no binding relationship.  
rsaPublicKey| string| Rsa public key  
isMaster| boolean| If this api key belongs to master account or not  
parentUid| string| The main account uid. Returns `"0"` when the endpoint is called by main account  
kycLevel| string| Personal account kyc level. `LEVEL_DEFAULT`, `LEVEL_1`, `LEVEL_2`  
kycRegion| string| Personal account kyc region  
unified| integer| **Deprecated**  
[](/docs/api-explorer/v5/user/apikey-info)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/query-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430842094  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_api_key_information())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getQueryApiKey()  
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
            "id": "2208369",  
            "note": "testnet",  
            "apiKey": "XXXXXXXX",  
            "readOnly": 1,  
            "secret": "",  
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
                    "SubMemberTransfer"  
                ],  
                "Options": [],  
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
                "Earn": [  
                    "Earn"  
                ],  
                "FiatP2P": [  
                    "FiatP2POrder",  
                    "Advertising"  
                ],  
                "FiatConvertBroker": [  
                    "FiatConvertBrokerOrder"  
                ],  
                "FiatGlobalPay": [],  
                "FiatBitPay": [  
                    "FaitPayOrder"  
                ],  
                "BitCard": [  
                    "BitCard"  
                ],  
                "ByXPost": [  
                    "ByXPost"  
                ]  
            },  
            "ips": [  
                "18.181.170.164",  
                "13.212.45.47",  
                "13.212.45.48"  
            ],  
            "type": 1,  
            "deadlineDay": -2,  
            "expiredAt": "1970-01-01T00:00:00Z",  
            "createdAt": "2025-10-13T03:20:45Z",  
            "unified": 0,  
            "uta": 1,  
            "userID": 1448939,  
            "inviterID": 0,  
            "vipLevel": "PRO-1",  
            "mktMakerLevel": "0",  
            "affiliateID": 0,  
            "rsaPublicKey": "",  
            "isMaster": true,  
            "parentUid": "0",  
            "kycLevel": "LEVEL_1",  
            "kycRegion": "MYS",  
            "userIDInt64": "0",  
            "inviterIDInt64": "0",  
            "affiliateIDInt64": "0"  
        },  
        "retExtInfo": {},  
        "time": 1776149990532  
    }

---

# 查詢API Key相關信息

獲取API key的相關信息。使用待查詢的api key調用接口。適用於母、子帳戶的api key。

提示

任意權限可以訪問該接口

### HTTP 請求

GET`/v5/user/query-api`

### 請求參數

無

### 返回參數

參數| 類型| 說明  
---|---|---  
id| string| 唯一id. 內部使用  
note| string| 備註  
apiKey| string| Api key  
readOnly| integer| `0`：可讀可寫. `1`：只讀  
secret| string| 總是""  
permissions| Object| 權限類型  
> ContractTrade| array| USDT合約、幣本位合約交易的權限 `Order`, `Position`  
> Spot| array| 現貨交易的權限 `SpotTrade`  
> Wallet| array| 錢包的權限 `AccountTransfer`, `SubMemberTransfer`(母帳戶), `SubMemberTransferList`(子帳戶), `Withdraw`(母帳戶)  
> Options| array| USDC合約和期權 `OptionsTrade`  
> Derivatives| array| `DerivativesTrade`  
> Exchange| array| 兌換的權限 `ExchangeHistory`  
> Earn| array| 理財產品的權限 `Earn`  
> FiatP2P| array| P2P `FiatP2POrder`, `Advertising`  
> FiatBitPay| array| Bybit Pay `FaitPayOrder`。不支持子帳戶，總是 `[]`  
> FiatConvertBroker| array| 數法兌換權限(僅支援經紀商) `FiatConvertBrokerOrder`  
> BitCard| array| Bybit卡權限, `BitCard`. 不支持子帳戶，總是`[]`  
> ByXPost| array| 社區帖子, `ByXPost`. 不支持子帳戶，總是`[]`  
> Affiliate| array| 代理商權限. 僅代理商可以擁有此權限, 否則總是`[]`  
> BlockTrade| array| 大宗交易的權限. 不支持子帳戶，總是[]  
ips| array| 綁定的IP  
type| integer| Api key類型. `1`：個人使用, `2`：綁定到第三方應用  
deadlineDay| integer| API key失效的倒數日. 針對那些未綁定IP的api key或者修改過密碼的帳戶  
expiredAt| datetime| API key的過期日. 針對那些未綁定IP的api key或者修改過密碼的帳戶  
createdAt| datetime| API key的創建日  
uta| integer| API Key所屬的帳戶是否為統一交易帳戶. `0`：經典帳戶; `1`：統一交易账户  
userID| integer| 用戶 ID  
inviterID| integer| 邀請人 ID（邀請該賬號加入平台的賬號的UID）  
[vipLevel](/docs/zh-TW/v5/enum#viplevel)| string| VIP用戶等級  
mktMakerLevel| string| market maker等級  
affiliateID| integer| 代理商Id. `0`: 表示無任何代理綁定關係  
rsaPublicKey| string| RSA公鑰  
isMaster| boolean| 是否為主帳戶下的api key  
parentUid| string| 主帳戶uid. 如果是主帳戶本身調用, 則返回`"0"`  
kycLevel| string| 個人帳戶的kyc等級. `LEVEL_DEFAULT`, `LEVEL_1`， `LEVEL_2`  
kycRegion| string| 個人帳戶的kyc地區  
unified| integer| 該字段**已廢棄**  
[](/docs/zh-TW/api-explorer/v5/user/apikey-info)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/query-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430842094  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_api_key_information())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getQueryApiKey()  
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
            "id": "2208369",  
            "note": "testnet",  
            "apiKey": "XXXXXXXX",  
            "readOnly": 1,  
            "secret": "",  
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
                    "SubMemberTransfer"  
                ],  
                "Options": [],  
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
                "Earn": [  
                    "Earn"  
                ],  
                "FiatP2P": [  
                    "FiatP2POrder",  
                    "Advertising"  
                ],  
                "FiatConvertBroker": [  
                    "FiatConvertBrokerOrder"  
                ],  
                "FiatGlobalPay": [],  
                "FiatBitPay": [  
                    "FaitPayOrder"  
                ],  
                "BitCard": [  
                    "BitCard"  
                ],  
                "ByXPost": [  
                    "ByXPost"  
                ]  
            },  
            "ips": [  
                "18.181.170.164",  
                "13.212.45.47",  
                "13.212.45.48"  
            ],  
            "type": 1,  
            "deadlineDay": -2,  
            "expiredAt": "1970-01-01T00:00:00Z",  
            "createdAt": "2025-10-13T03:20:45Z",  
            "unified": 0,  
            "uta": 1,  
            "userID": 1448939,  
            "inviterID": 0,  
            "vipLevel": "PRO-1",  
            "mktMakerLevel": "0",  
            "affiliateID": 0,  
            "rsaPublicKey": "",  
            "isMaster": true,  
            "parentUid": "0",  
            "kycLevel": "LEVEL_1",  
            "kycRegion": "MYS",  
            "userIDInt64": "0",  
            "inviterIDInt64": "0",  
            "affiliateIDInt64": "0"  
        },  
        "retExtInfo": {},  
        "time": 1776149990532  
    }