---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/otc/bind-uid
api_type: REST
updated_at: 2026-05-27 19:20:55.995492
---

# Get Loan Orders

Get up to 2 years worth of historical loan orders.

### HTTP Request

GET`/v5/ins-loan/loan-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID. If not passed, returns all orders sorted by `loanTime` in descending order  
startTime| false| integer| The start timestamp (ms)  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size. [`1`, `100`], Default: `10`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
loanInfo| array| Object  
> orderId| string| Loan order ID  
> orderProductId| string| Product ID  
> parentUid| string| The designated UID that was used to bind with the INS loan  
> loanTime| string| Loan timestamp, in milliseconds  
> loanCoin| string| Loan coin  
> loanAmount| string| Loan amount  
> unpaidAmount| string| Unpaid principal  
> unpaidInterest| string| Unpaid interest  
> repaidAmount| string| Repaid principal  
> repaidInterest| string| Repaid interest  
> interestRate| string| Daily interest rate  
> status| string| `1`: outstanding; `2`: paid off  
> leverage| string| The maximum leverage for this loan product  
> supportSpot| string| Whether to support spot. `0`:false; `1`:true  
> supportContract| string| Whether to support contract . `0`:false; `1`:true  
> withdrawLine| string| Restrict line for withdrawal  
> transferLine| string| Restrict line for transfer  
> spotBuyLine| string| Restrict line for SPOT buy  
> spotSellLine| string| Restrict line for SPOT sell  
> contractOpenLine| string| Restrict line for USDT Perpetual open position  
> deferredLiquidationLine| string| Line for deferred liquidation  
> deferredLiquidationTime| string| Time for deferred liquidation  
> reserveToken| string| Reserve token  
> reserveQuantity| string| Reserve token qty  
> liquidationLine| string| Line for liquidation  
> stopLiquidationLine| string| Line for stop liquidation  
> contractLeverage| string| The allowed default leverage for USDT Perpetual  
> transferRatio| string| The transfer ratio for loan funds to transfer from Spot wallet to Contract wallet  
> spotSymbols| array| The whitelist of spot trading pairs. If there is no whitelist, then "[]"  
> contractSymbols| array| The whitelist of contract trading pairs 

  * If `supportContract`="0", then this is "[]"
  * If there is no whitelist, this is "[]"

  
> supportUSDCContract| string| Whether to support USDC contract. `"0"`:false; `"1"`:true  
> supportUSDCOptions| string| Whether to support Option. `"0"`:false; `"1"`:true  
> supportMarginTrading| string| Whether to support Spot margin trading. `"0"`:false; `"1"`:true  
> USDTPerpetualOpenLine| string| Restrict line to open USDT Perpetual position  
> USDCContractOpenLine| string| Restrict line to open USDC Contract position  
> USDCOptionsOpenLine| string| Restrict line to open Option position  
> USDTPerpetualCloseLine| string| Restrict line to trade USDT Perpetual position  
> USDCContractCloseLine| string| Restrict line to trade USDC Contract position  
> USDCOptionsCloseLine| string| Restrict line to trade Option position  
> USDCContractSymbols| array| The whitelist of USDC contract trading pairs 

  * If no whitelist symbols, it is `[]`, and you can trade any
  * If supportUSDCContract="0", it is `[]`

  
> USDCOptionsSymbols| array| The whitelist of Option symbols 

  * If no whitelisted, it is `[]`, and you can trade any
  * If supportUSDCOptions="0", it is `[]`

  
> marginLeverage| string| The allowable maximum leverage for Spot margin  
> USDTPerpetualLeverage| array| Object 

  * If supportContract="0", it is `[]`
  * If no whitelist USDT perp symbols, it returns all trading symbols and leverage by default
  * If there are whitelist symbols, it return those whitelist data

  
>> symbol| string| Symbol name  
>> leverage| string| Maximum leverage  
> USDCContractLeverage| array| Object 

  * If supportUSDCContract="0", it is `[]`
  * If no whitelist USDC contract symbols, it returns all trading symbols and leverage by default
  * If there are whitelist symbols, it return those whitelist data

  
>> symbol| string| Symbol name  
>> leverage| string| Maximum leverage  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/loan-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1678687874060  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_loan_orders())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingLoanOrders({  
        limit: 10,  
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
            "loanInfo": [  
                {  
                    "orderId": "1468005106166530304",  
                    "orderProductId": "96",  
                    "parentUid": "1631521",  
                    "loanTime": "1689735916000",  
                    "loanCoin": "USDT",  
                    "loanAmount": "204",  
                    "unpaidAmount": "52.07924201",  
                    "unpaidInterest": "0",  
                    "repaidAmount": "151.92075799",  
                    "repaidInterest": "0",  
                    "interestRate": "0.00019178",  
                    "status": "1",  
                    "leverage": "4",  
                    "supportSpot": "1",  
                    "supportContract": "1",  
                    "withdrawLine": "",  
                    "transferLine": "",  
                    "spotBuyLine": "0.71",  
                    "spotSellLine": "0.71",  
                    "contractOpenLine": "0.71",  
                    "liquidationLine": "0.75",  
                    "stopLiquidationLine": "0.35000000",  
                    "contractLeverage": "7",  
                    "transferRatio": "1",  
                    "spotSymbols": [],  
                    "contractSymbols": [],  
                    "supportUSDCContract": "1",  
                    "supportUSDCOptions": "1",  
                    "USDTPerpetualOpenLine": "0.71",  
                    "USDCContractOpenLine": "0.71",  
                    "USDCOptionsOpenLine": "0.71",  
                    "USDTPerpetualCloseLine": "0.71",  
                    "USDCContractCloseLine": "0.71",  
                    "USDCOptionsCloseLine": "0.71",  
                    "USDCContractSymbols": [],  
                    "USDCOptionsSymbols": [],  
                    "deferredLiquidationLine":"",  
                    "deferredLiquidationTime":"",  
                    "marginLeverage": "4",  
                    "USDTPerpetualLeverage": [  
                        {  
                            "symbol": "SUSHIUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "INJUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "RDNTUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "ZRXUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "HIGHUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "WAVESUSDT",  
                            "leverage": "7"  
                        },  
                        ...  
                        {  
                            "symbol": "ACHUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "SUNUSDT",  
                            "leverage": "7"  
                        }  
                    ],  
                    "USDCContractLeverage": [  
                        {  
                            "symbol": "BTCPERP",  
                            "leverage": "8"  
                        },  
                        {  
                            "symbol": "BTC-Futures",  
                            "leverage": "8"  
                        },  
                        ...  
                        {  
                            "symbol": "ETH-Futures",  
                            "leverage": "8"  
                        },  
                        {  
                            "symbol": "SOLPERP",  
                            "leverage": "8"  
                        },  
                        {  
                            "symbol": "ETHPERP",  
                            "leverage": "8"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1689745773187  
    }

---

# 查詢借貸訂單信息

查詢借貸訂單的詳情

提示

  * 默認查詢過去2年的數據
  * 最多支持查詢過去2年的數據



### HTTP 請求

GET`/v5/ins-loan/loan-order`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
orderId| false| string| 借貸訂單ID. 若不傳，則返回全部. 按照`loanTime`降序排列  
startTime| false| integer| 開始時間戳 (毫秒)  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 返回數量限制. [`1`, `100`], 默認: `10`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
loanInfo| array| Object  
> orderId| string| 借貸訂單ID  
> orderProductId| string| 產品ID  
> parentUid| string| 綁定場外借貸產品的UID  
> loanTime| string| 放款時間（毫秒）  
> loanCoin| string| 借款幣種  
> loanAmount| string| 借款金額  
> unpaidAmount| string| 未還本金  
> unpaidInterest| string| 未還利息  
> repaidAmount| string| 已還本金  
> repaidInterest| string| 已還利息  
> interestRate| string| 日利率  
> status| string| `1`：未還清; `2`：已還清  
> leverage| string| 該借貸產品的最大槓桿倍數  
> supportSpot| string| 是否支持現貨. `0`:否; `1`:是  
> supportContract| string| 是否支持合約 . `0`: 否; `1`: 是  
> supportMarginTrading| string| 是否支持現貨槓桿交易. `0`: 否; `1`: 是  
> withdrawLine| string| 限制提幣線  
> transferLine| string| 限制劃轉線  
> spotBuyLine| string| 限制現貨買入線  
> spotSellLine| string| 限制現貨交易線  
> contractOpenLine| string| 限制USDT永續合約開倉線  
> deferredLiquidationLine| string| 延期清算線  
> deferredLiquidationTime| string| 延期清算時間  
> reserveToken| string| 備付金幣種  
> reserveQuantity| string| 備付金幣種數量  
> liquidationLine| string| 強平線  
> stopLiquidationLine| string| 停止強平線  
> contractLeverage| string| 允許USDT永續默認開倉倍數  
> transferRatio| string| 現貨帳戶到合約帳戶的借貸資金劃轉比例  
> spotSymbols| array| 現貨交易對白名單. 若沒有配置白名單, 則返回[]  
> contractSymbols| array| USDT永續合約交易對白名單 

  * 若沒有配置白名單, 則返回[]
  * 若supportContract="0", 則也是[]

  
> supportUSDCContract| string| 是否支持USDC合約交易. `'0'`:否; `'1'`:是  
> supportUSDCOptions| string| 是否支持期權交易. `'0'`:false; `'1'`:true  
> USDTPerpetualOpenLine| string| 限制USDT永續的開倉線  
> USDCContractOpenLine| string| 限制USDC合約的開倉線  
> USDCOptionsOpenLine| string| 限制期權的開倉線  
> USDTPerpetualCloseLine| string| 限制USDT永續的交易線  
> USDCContractCloseLine| string| 限制USDC合約的交易線  
> USDCOptionsCloseLine| string| 限制期權的交易線  
> USDCContractSymbols| array| USDC合約的白名單交易對 

  * 若沒有配置白名單, 則是空數組`[]`, 可以交易任何合約
  * 如果 supportUSDCContract="0", 則也是空數組`[]`

  
> USDCOptionsSymbols| array| 期權的白名單交易對 

  * 若沒有配置白名單, 則是空數組`[]`, 可以交易任何合約
  * 如果 supportUSDCOptions="0", 則也是空數組`[]`

  
> marginLeverage| string| 全倉槓桿允許可開的最高槓桿  
> USDTPerpetualLeverage| array| Object 

  * 如果 supportContract="0", 則返回空數組`[]`
  * 如果沒有配置USDT永續交易對白名單, 則返回所有的合約和槓桿
  * 如果有白名單配置, 則只返回白名單列表的合約和槓桿

  
>> symbol| string| 合約名  
>> leverage| string| 最高可開槓桿  
> USDCContractLeverage| array| Object 

  * 如果 supportUSDCContract="0", 則返回空數組`[]`
  * 如果沒有配置USDC合約交易對白名單, 則返回所有的合約和槓桿
  * 如果有白名單配置, 則只返回白名單列表的合約和槓桿

  
>> symbol| string| 合約名  
>> leverage| string| 最高可開槓桿  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/loan-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1678687874060  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_loan_orders())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingLoanOrders({  
        limit: 10,  
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
            "loanInfo": [  
                {  
                    "orderId": "1468005106166530304",  
                    "orderProductId": "96",  
                    "parentUid": "1631521",  
                    "loanTime": "1689735916000",  
                    "loanCoin": "USDT",  
                    "loanAmount": "204",  
                    "unpaidAmount": "52.07924201",  
                    "unpaidInterest": "0",  
                    "repaidAmount": "151.92075799",  
                    "repaidInterest": "0",  
                    "interestRate": "0.00019178",  
                    "status": "1",  
                    "leverage": "4",  
                    "supportSpot": "1",  
                    "supportContract": "1",  
                    "withdrawLine": "",  
                    "transferLine": "",  
                    "spotBuyLine": "0.71",  
                    "spotSellLine": "0.71",  
                    "contractOpenLine": "0.71",  
                    "liquidationLine": "0.75",  
                    "stopLiquidationLine": "0.35000000",  
                    "contractLeverage": "7",  
                    "transferRatio": "1",  
                    "spotSymbols": [],  
                    "contractSymbols": [],  
                    "supportUSDCContract": "1",  
                    "supportUSDCOptions": "1",  
                    "USDTPerpetualOpenLine": "0.71",  
                    "USDCContractOpenLine": "0.71",  
                    "USDCOptionsOpenLine": "0.71",  
                    "USDTPerpetualCloseLine": "0.71",  
                    "USDCContractCloseLine": "0.71",  
                    "USDCOptionsCloseLine": "0.71",  
                    "USDCContractSymbols": [],  
                    "USDCOptionsSymbols": [],  
                    "deferredLiquidationLine":"",  
                    "deferredLiquidationTime":"",  
                    "marginLeverage": "4",  
                    "USDTPerpetualLeverage": [  
                        {  
                            "symbol": "SUSHIUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "INJUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "RDNTUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "ZRXUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "HIGHUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "WAVESUSDT",  
                            "leverage": "7"  
                        },  
                        ...  
                        {  
                            "symbol": "ACHUSDT",  
                            "leverage": "7"  
                        },  
                        {  
                            "symbol": "SUNUSDT",  
                            "leverage": "7"  
                        }  
                    ],  
                    "USDCContractLeverage": [  
                        {  
                            "symbol": "BTCPERP",  
                            "leverage": "8"  
                        },  
                        {  
                            "symbol": "BTC-Futures",  
                            "leverage": "8"  
                        },  
                        ...  
                        {  
                            "symbol": "ETH-Futures",  
                            "leverage": "8"  
                        },  
                        {  
                            "symbol": "SOLPERP",  
                            "leverage": "8"  
                        },  
                        {  
                            "symbol": "ETHPERP",  
                            "leverage": "8"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1689745773187  
    }