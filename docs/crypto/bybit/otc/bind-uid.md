---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/otc/bind-uid
api_type: REST
updated_at: 2026-07-10 19:04:23.275763
---

# Get LTV

Get your loan-to-value (LTV) ratio.

important

  * In cases where an institutional user makes frequent transfers, LTV calculations may become inaccurate, and this endpoint will return retCode = 100016, retMsg = "Transfers within your risk unit are too frequent. Please reduce the transfer frequency and try again."
  * If you encounter this error, it is recommended to reduce the transfer frequency first and retry
  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery
  * When a user is in a state such as liquidation, transfer, or manual repayment, LTV is not calculated. We have added a new `liqStatus` to represent these states. When `liqStatus` != 0, `ltvInfo` returns empty strings for `ltv`, `unpaidAmount` and `balance`, and `unpaidInfo` and `balanceInfo` return empty arrays.



### HTTP Request

GET`/v5/ins-loan/ltv-convert`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
ltvInfo| array| Object  
> ltv| string| Risk rate 

  * ltv is calculated in real time
  * If you have an INS loan, it is highly recommended to query this data every second. Liquidation occurs when it reachs 0.9 (90%)

. When `liqStatus` != 0, empty string is returned.  
> rst| string| Remaining liquidation time (UTC time in seconds). When it is not triggered, it is displayed as an empty string. When `liqStatus` != 0, empty string is returned.  
> parentUid| string| The designated Risk Unit ID that was used to bind with the INS loan  
> subAccountUids| array| Bound user ID  
> unpaidAmount| string| Total debt(USD). When `liqStatus` != 0, empty string is returned.  
> unpaidInfo| array| Debt details. When `liqStatus` != 0, empty array is returned.  
>> token| string| coin  
>> unpaidQty| string| Unpaid principle  
>> unpaidInterest| string| Useless field, please ignore this for now  
> balance| string| Total asset (margin coins converted to USDT). Please read [here](https://www.bybit.com/en-US/help-center/s/article/Over-the-counter-OTC-Lending) to understand the calculation. When `liqStatus` != 0, empty string is returned.  
> balanceInfo| array| Asset details. When `liqStatus` != 0, empty array is returned.  
>> token| string| Margin coin  
>> price| string| Margin coin price  
>> qty| string| Margin coin quantity  
>> convertedAmount| string| Margin conversion amount  
> liqStatus| integer| Liquidation status. 

  * `0`: Normal
  * `1`: Under liquidation
  * `2`: Manual repayment in progress
  * `3`: Transfer in progress

  
liqStatus| integer| Liquidation status. 

  * `0`: Normal
  * `1`: Under liquidation
  * `2`: Manual repayment in progress
  * `3`: Transfer in progress

  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/ltv-convert HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686638165351  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_ltv())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingLTVWithLadderConversionRate()  
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
            "ltvInfo": [  
                {  
                    "ltv": "0.75",  
                    "rst": "",  
                    "parentUid": "xxxxx",  
                    "subAccountUids": [  
                        "60568258"  
                    ],  
                    "unpaidAmount": "30",  
                    "unpaidInfo": [  
                        {  
                            "token": "USDT",  
                            "unpaidQty": "30",  
                            "unpaidInterest": "0"  
                        }  
                    ],  
                    "balance": "40",  
                    "balanceInfo": [  
                        {  
                            "token": "USDT",  
                            "price": "1",  
                            "qty": "40",  
                            "convertedAmount": "40"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686638166323  
    }  
      
    When `liqStatus` != 0:  
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "ltvInfo": [  
                {  
                    "ltv": "",  
                    "parentUid": "100331354",  
                    "subAccountUids": [  
                        "100334094",  
                        "100334098"  
                    ],  
                    "unpaidAmount": "",  
                    "unpaidInfo": [],  
                    "balance": "",  
                    "balanceInfo": [],  
                    "rst": "",  
                    "liqStatus": 3  
                }  
            ],  
            "liqStatus": 3  
        },  
        "retExtInfo": {},  
        "time": 1766462020703  
    }

---

# 查詢風險率

important

  * 如果機構用戶頻繁轉帳，LTV 計算可能會變得不準確，此端點將返回 retCode = 100016，retMsg = "Transfers within your risk unit are too frequent. Please reduce the transfer frequency and try again."
  * 遇到這個報錯，建議先減少轉帳頻率，再重試
  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況
  * 當用戶發生強平、劃轉、手工還款等過程中的狀態時，LTV不進行計算。我們新增了一個`liqStatus`來表示這些狀態。當`liqStatus`!=0時，此時`ltvInfo`裡`ltv`、`unpaidAmount`、`balance`都是空字串，`unpaidInfo`、`balanceInfo`都是空數組。



### HTTP 請求

GET`/v5/ins-loan/ltv-convert`

### 請求參數

無

### 返回參數

參數| 類型| 說明  
---|---|---  
ltvInfo| array| Object  
> ltv| string| 風險率 

  * 該數據是實時計算
  * 如果持有機構借貸, 強烈建議每秒查詢一次ltv。當達到0.9 (90%)時即觸發強平

. 當 `liqStatus` != 0 時，傳回空字串。  
> rst| string| 剩餘清算時間（UTC 時間，以秒為單位）。 未觸發時顯示為空字串。當 `liqStatus` != 0 時，傳回空字串。  
> parentUid| string| 被指定綁定為機構借貸產品的風險單元Id  
> subAccountUids| array| 綁定場外借貸產品的UID  
> unpaidAmount| string| 總負債 (USD)。當 `liqStatus` != 0 時，傳回空字串。  
> unpaidInfo| array| 負債明細。 當 `liqStatus` != 0 時，傳回空數組。  
>> token| string| 幣種  
>> unpaidQty| string| 未還本金  
>> unpaidInterest| string| 該字段無效, 暫時請忽略  
> balance| string| 總資產(保證金幣種資產折算為USDT資產). 可以參考[這裡](https://www.bybit.com/zh-MY/help-center/s/article/Over-the-counter-OTC-Lending)了解詳細計算。當 `liqStatus` != 0 時，傳回空字串。  
> balanceInfo| array| 資產明細。當 `liqStatus` != 0 時，傳回空數組。  
>> token| string| 保證金幣種  
>> price| string| 保證金幣種價格  
>> qty| string| 保證金數量  
>> convertedAmount| string| 保證金折算金額  
> liqStatus| integer| 清算狀態。 

  * `0`: 正常
  * `1`: 強平
  * `2`: 手工還款
  * `3`: 劃轉

  
liqStatus| integer| 清算狀態。 

  * `0`: 正常
  * `1`: 強平
  * `2`: 手工還款
  * `3`: 劃轉

  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/ltv-convert HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686638165351  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_ltv())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingLTVWithLadderConversionRate()  
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
            "ltvInfo": [  
                {  
                    "ltv": "0.75",  
                    "rst": "",  
                    "parentUid": "xxxxx",  
                    "subAccountUids": [  
                        "60568258"  
                    ],  
                    "unpaidAmount": "30",  
                    "unpaidInfo": [  
                        {  
                            "token": "USDT",  
                            "unpaidQty": "30",  
                            "unpaidInterest": "0"  
                        }  
                    ],  
                    "balance": "40",  
                    "balanceInfo": [  
                        {  
                            "token": "USDT",  
                            "price": "1",  
                            "qty": "40",  
                            "convertedAmount": "40"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686638166323  
    }  
      
    When `liqStatus` != 0:  
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "ltvInfo": [  
                {  
                    "ltv": "",  
                    "parentUid": "100331354",  
                    "subAccountUids": [  
                        "100334094",  
                        "100334098"  
                    ],  
                    "unpaidAmount": "",  
                    "unpaidInfo": [],  
                    "balance": "",  
                    "balanceInfo": [],  
                    "rst": "",  
                    "liqStatus": 3  
                }  
            ],  
            "liqStatus": 3  
        },  
        "retExtInfo": {},  
        "time": 1766462020703  
    }