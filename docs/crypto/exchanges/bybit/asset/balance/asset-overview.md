---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/balance/asset-overview
api_type: REST
updated_at: 2026-05-27 19:14:44.328671
---

# Get Withdrawable Amount

info

**How can partial funds be subject to delayed withdrawal requests?**

  * **On-chain deposit** : If the number of on-chain confirmations has not reached a risk-controlled level, a portion of the funds will be frozen for a period of time until they are unfrozen.
  * **Buying crypto** : If there is a risk, the funds will be frozen for a certain period of time and cannot be withdrawn.



**During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery**

### HTTP Request

GET`/v5/asset/withdraw/withdrawable-amount`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
limitAmountUsd| string| The frozen amount due to risk, in USD  
withdrawableAmount| Object|   
> SPOT| Object| Spot wallet, it is not returned if spot wallet is removed  
>> coin| string| Coin name  
>> withdrawableAmount| string| Amount that can be withdrawn  
>> availableBalance| string| Available balance  
> FUND| Object| Funding wallet  
>> coin| string| Coin name  
>> withdrawableAmount| string| Amount that can be withdrawn  
>> availableBalance| string| Available balance  
> UTA| Object| Unified wallet  
>> coin| string| Coin name  
>> withdrawableAmount| string| Amount that can be withdrawn  
>> availableBalance| string| Available balance  
> EARN| Object| Earn account, it is not returned when the coin does not support to be withdrawn via Earn account  
>> coin| string| Coin name  
>> withdrawableAmount| string| Amount that can be withdrawn  
>> availableBalance| string| Available balance  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/withdraw/withdrawable-amount?coin=USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1677565621998  
    X-BAPI-RECV-WINDOW: 50000  
    X-BAPI-SIGN: XXXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_withdrawable_amount(  
        coin="USDT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getWithdrawableAmount({  
        coin: 'USDT',  
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
        "retMsg": "success",  
        "result": {  
            "limitAmountUsd": "595051.7",  
            "withdrawableAmount": {  
                "FUND": {  
                    "coin": "USDT",  
                    "withdrawableAmount": "155805.847",  
                    "availableBalance": "155805.847"  
                },  
                "UTA": {  
                    "coin": "USDT",  
                    "withdrawableAmount": "498751.0882",  
                    "availableBalance": "498751.0882"  
                }  
            }  
        },  
        "retExtInfo": {},  
        "time": 1754009688289  
    }

---

# 查詢可提現金額

信息

**如何會導致部分資金被要求延遲提幣？**

  * **鏈上充值** : 鏈上區塊確認數未達到該幣種風險高度數時，部分資金將被凍結一段時間，直至解凍；具體風險高度數可查看 [查詢幣種信息](/docs/zh-TW/v5/asset/coin-info) 的返回值 `safeConfirmNumber`
  * **買幣** : 若存在風險, 則一定時間內被凍結, 無法提幣



**在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況**

### HTTP 請求

GET`/v5/asset/withdraw/withdrawable-amount`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
limitAmountUsd| string| 延遲提幣凍結金額 (USD)  
withdrawableAmount| Object|   
> SPOT| Object| 現貨錢包, 若該錢包被移除, 則不會返回該對象  
>> coin| string| 幣種名稱  
>> withdrawableAmount| string| 可提現金額  
>> availableBalance| string| 可用餘額  
> FUND| Object| 資金錢包  
>> coin| string| 幣種名稱  
>> withdrawableAmount| string| 可提現金額  
>> availableBalance| string| 可用餘額  
> UTA| Object| Unified錢包  
>> coin| string| 幣種名稱  
>> withdrawableAmount| string| 可提現金額  
>> availableBalance| string| 可用餘額  
> EARN| Object| 理財帳戶, 如果幣種不支持從理財帳戶出金, 則不返回  
>> coin| string| 幣種  
>> withdrawableAmount| string| 可提現金額  
>> availableBalance| string| 可用餘額  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/withdraw/withdrawable-amount?coin=USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1677565621998  
    X-BAPI-RECV-WINDOW: 50000  
    X-BAPI-SIGN: XXXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_withdrawable_amount(  
        coin="USDT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getWithdrawableAmount({  
        coin: 'USDT',  
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
        "retMsg": "success",  
        "result": {  
            "limitAmountUsd": "595051.7",  
            "withdrawableAmount": {  
                "FUND": {  
                    "coin": "USDT",  
                    "withdrawableAmount": "155805.847",  
                    "availableBalance": "155805.847"  
                },  
                "UTA": {  
                    "coin": "USDT",  
                    "withdrawableAmount": "498751.0882",  
                    "availableBalance": "498751.0882"  
                }  
            }  
        },  
        "retExtInfo": {},  
        "time": 1754009688289  
    }