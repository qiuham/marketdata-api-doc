---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/deposit/deposit-record
api_type: REST
updated_at: 2026-07-07 19:10:08.008954
---

# Get Sub Deposit Address

Query the deposit address information of SUB account.

info

  * Use master UID's api key **only**
  * Custodial sub account deposit address cannot be obtained



### HTTP Request

GET`/v5/asset/deposit/query-sub-member-address`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Coin, uppercase only  
chainType| **true**|  string| Please use the value of `chain` from [coin-info](/docs/v5/asset/coin-info) endpoint  
subMemberId| **true**|  string| Sub user ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
coin| string| Coin  
chains| array| Object  
> chainType| string| Chain type  
> addressDeposit| string| The address for deposit  
> tagDeposit| string| Tag of deposit  
> chain| string| Chain  
> batchReleaseLimit| string| The deposit limit for this coin in this chain. `"-1"` means no limit  
> contractAddress| string| The contract address of the coin. Only display last 6 characters, if there is no contract address, it shows `""`  
[](/docs/api-explorer/v5/asset/sub-deposit-addr)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/deposit/query-sub-member-address?coin=USDT&chainType=TRX&subMemberId=592334 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672194349421  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_sub_deposit_address(  
        coin="USDT",  
        chainType="TRX",  
        subMemberId=592334,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSubDepositAddress('USDT', 'TRX', '592334')  
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
            "coin": "USDT",  
            "chains": {  
                "chainType": "TRC20",  
                "addressDeposit": "XXXXXX",  
                "tagDeposit": "",  
                "chain": "TRX",  
                "batchReleaseLimit": "-1",  
                "contractAddress": "gjLj6t"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1736394845821  
    }

---

# 查詢子帳號充值地址

信息

  * 僅能使用該**母帳號** 的API key
  * 託管子帳戶不支持獲取入金地址



### HTTP 請求

GET`/v5/asset/deposit/query-sub-member-address`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 幣種  
chainType| **true**|  string| 請使用[查詢幣種信息](/docs/zh-TW/v5/asset/coin-info)響應字段`chain`作為這個字段的輸入  
subMemberId| **true**|  string| 子帳號Id  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
coin| string| 幣種  
chains| array| Object  
> chainType| string| 鏈類型  
> addressDeposit| string| 充值地址  
> tagDeposit| string| 地址的tag  
> chain| string| 鏈名  
> batchReleaseLimit| string| 當前幣鏈每日充值限額. `"-1"`表示無限制  
> contractAddress| string| 合約地址, 僅展示後6位. 如果沒有合約地址, 則為空字符串`""`  
[](/docs/zh-TW/api-explorer/v5/asset/sub-deposit-addr)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/deposit/query-sub-member-address?coin=USDT&chainType=TRX&subMemberId=592334 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672194349421  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_sub_deposit_address(  
        coin="USDT",  
        chainType="TRX",  
        subMemberId=592334,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSubDepositAddress('USDT', 'TRX', '592334')  
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
            "coin": "USDT",  
            "chains": {  
                "chainType": "TRC20",  
                "addressDeposit": "XXXXXX",  
                "tagDeposit": "",  
                "chain": "TRX",  
                "batchReleaseLimit": "-1",  
                "contractAddress": "gjLj6t"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1736394845821  
    }