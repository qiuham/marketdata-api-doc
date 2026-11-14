---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/coin-info
api_type: REST
updated_at: 2026-11-13 19:21:27.386933
---

# Get Coin Info

Query coin information, including chain information, withdraw and deposit status.

### HTTP Request

GET`/v5/asset/coin/query-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Coin, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
rows| array| Object  
> name| string| Coin name  
> coin| string| Coin  
> chains| array| Object  
>> chain| string| Chain  
>> chainType| string| Chain type  
>> confirmation| string| Number of confirmations for deposit: Once this number is reached, your funds will be credited to your account and available for trading  
>> withdrawFee| string| withdraw fee. _If withdraw fee is empty, It means that this coin does not support withdrawal_  
>> depositMin| string| Min. deposit  
>> withdrawMin| string| Min. withdraw  
>> minAccuracy| string| The precision of withdraw or deposit  
>> chainDeposit| string| The chain status of deposit. `0`: suspend. `1`: normal  
>> chainWithdraw| string| The chain status of withdraw. `0`: suspend. `1`: normal  
>> withdrawPercentageFee| string| The withdraw fee percentage. It is a real figure, e.g., 0.022 means 2.2%  
>> contractAddress| string| Contract address. `""` means no contract address  
>> safeConfirmNumber| string| Number of security confirmations: Once this number is reached, your USD equivalent worth funds will be fully unlocked and available for withdrawal.  
>> withdrawMax| string| The maximum amount that can be withdrawn per transaction on this chain; -1 indicates no limit  
> remainAmount| string| **Deprecated** field, please ignore  
[](/docs/api-explorer/v5/asset/coin-info)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/coin/query-info?coin=MNT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672194580887  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_coin_info(  
        coin="MNT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getCoinInfo('MNT')  
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
            "rows": [  
                {  
                    "name": "MNT",  
                    "coin": "MNT",  
                    "remainAmount": "10000000",  
                    "chains": [  
                        {  
                            "chainType": "Ethereum",  
                            "confirmation": "6",  
                            "withdrawFee": "3",  
                            "depositMin": "0",  
                            "withdrawMin": "3",  
                            "chain": "ETH",  
                            "chainDeposit": "1",  
                            "chainWithdraw": "1",  
                            "minAccuracy": "8",  
                            "withdrawPercentageFee": "0",  
                            "contractAddress": "0x3c3a81e81dc49a522a592e7622a7e711c06bf354",  
                            "safeConfirmNumber": "65",  
                            "withdrawMax": "10000000"  
                        },  
                        {  
                            "chainType": "Mantle Network",  
                            "confirmation": "100",  
                            "withdrawFee": "0",  
                            "depositMin": "0",  
                            "withdrawMin": "10",  
                            "chain": "MANTLE",  
                            "chainDeposit": "1",  
                            "chainWithdraw": "1",  
                            "minAccuracy": "8",  
                            "withdrawPercentageFee": "0",  
                            "contractAddress": "",  
                            "safeConfirmNumber": "100",  
                            "withdrawMax": "10000000"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1736395486989  
    }

---

# 查詢幣種信息

獲取幣種信息，包括鏈信息，是否可充可提

### HTTP 請求

GET`/v5/asset/coin/query-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 幣種  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
rows| array| Object  
> name| integer| 幣種名稱  
> coin| string| 幣種  
> chains| array| Object  
>> chain| string| 鏈名  
>> chainType| string| 鏈類型  
>> confirmation| string| 充值上賬確認數, 當到達該高度, 資金可用於交易  
>> withdrawFee| string| 提現手續費. _如果提現費為空，則表示該幣不支持提現_  
>> depositMin| string| 最小充值數量  
>> withdrawMin| string| 最小提現數量  
>> minAccuracy| string| 充提幣的最小精度  
>> chainDeposit| string| 幣鏈是否可充值. `0`: 暫停. `1`: 正常  
>> chainWithdraw| string| 幣鏈是否可提幣. `0`: 暫停. `1`: 正常  
>> withdrawPercentageFee| string| 提現手續費百分比. 該字段的值是實際數字，即0.022表示為2.2%  
>> contractAddress| string| 合約地址. `""` 表示沒有合約地址  
>> safeConfirmNumber| string| 風險高度數, 當入金抵達這個高度後, 風險完全解鎖, USD等值的資金允許提走  
>> withdrawMax| string| 該鏈允許的最大的單筆提幣金額, `-1`表示無上限  
> remainAmount| string| **廢棄** 字段, 請忽視  
[](/docs/zh-TW/api-explorer/v5/asset/coin-info)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/coin/query-info?coin=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672194580887  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_coin_info(  
        coin="ETH",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getCoinInfo('ETH')  
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
            "rows": [  
                {  
                    "name": "MNT",  
                    "coin": "MNT",  
                    "remainAmount": "10000000",  
                    "chains": [  
                        {  
                            "chainType": "Ethereum",  
                            "confirmation": "6",  
                            "withdrawFee": "3",  
                            "depositMin": "0",  
                            "withdrawMin": "3",  
                            "chain": "ETH",  
                            "chainDeposit": "1",  
                            "chainWithdraw": "1",  
                            "minAccuracy": "8",  
                            "withdrawPercentageFee": "0",  
                            "contractAddress": "0x3c3a81e81dc49a522a592e7622a7e711c06bf354",  
                            "safeConfirmNumber": "65",  
                            "withdrawMax": "10000000"  
                        },  
                        {  
                            "chainType": "Mantle Network",  
                            "confirmation": "100",  
                            "withdrawFee": "0",  
                            "depositMin": "0",  
                            "withdrawMin": "10",  
                            "chain": "MANTLE",  
                            "chainDeposit": "1",  
                            "chainWithdraw": "1",  
                            "minAccuracy": "8",  
                            "withdrawPercentageFee": "0",  
                            "contractAddress": "",  
                            "safeConfirmNumber": "100",  
                            "withdrawMax": "10000000"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1736395486989  
    }