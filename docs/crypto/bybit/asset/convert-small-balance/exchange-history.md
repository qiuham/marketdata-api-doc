---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/convert-small-balance/exchange-history
api_type: REST
updated_at: 2026-06-30 19:23:16.647702
---

# Request a Quote

Custody accounts, like copper, fireblock, etc are **not supported** to make a convertion

info

  * API key permission: `Convert`
  * API rate limit: `5 req /s`
  * In a Unified Trading Account, your **actual executed amounts may be less than your available balance**. If you submit convert requests for multiple cryptocurrencies simultaneously, partial executions may occur. Please refer to the actual credited amounts.



### HTTP Request

POST`/v5/asset/covert/get-quote`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
accountType| **true**|  string| Wallet type `eb_convert_uta`. Only supports the Unified wallet  
fromCoinList| **true**|  array<string>| Source currency list `["BTC", "XRP", "ETH"]`, up to 20 coins in one transaction  
toCoin| **true**|  string| Target currency, each request supports one of MNT, USDT, or USDC  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
quoteId| string| Quote transaction ID. It is system generated, and it is used to confirm quote and query the result of transaction  
result| object|   
> quoteCreateTime| string| Quote created ts  
> quoteExpireTime| string| Quote expired ts, 30 seconds  
> exchangeCoins| array<object>| Quote details  
>> fromCoin| string| Source currency  
>> supportConvert| integer| `1`: support, `2`: not supported  
>> availableBalance| string| Withdrawable balance  
>> baseValue| string| USDT equivalent value  
>> toCoin| string| Target currency  
>> toAmount| string| Est.received amount  
>> exchangeRate| string| Exchange rate  
>> feeInfo| object| Exchange fee info  
>>> feeCoin| string| Fee currency  
>>> amount| string| Fee  
>>> feeRate| string| Fee rate  
>> taxFeeInfo| object| Tax fee info  
>>> totalAmount| string| Tax fee  
>>> feeCoin| string| Tax fee coin  
>>> taxFeeItems| array| Tax fee items  
> totalFeeInfo| object| Total exchange fee details  
>> feeCoin| string| Fee currency  
>> amount| string| Total fee  
>> feeRate| string| Fee rate  
> totalTaxFeeInfo| object| Total tax fee info  
>> totalAmount| string| Total tax fee  
>> feeCoin| string| Tax fee coin  
>> taxFeeItems| array| Tax fee items  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/covert/get-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1766126592271  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    Content-Length: 97  
      
    {  
        "accountType": "eb_convert_uta",  
        "fromCoinList": ["XRP", "SOL"],  
        "toCoin": "USDC"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.request_a_quote_small_balance(  
        accountType="eb_convert_uta",  
        fromCoinList=["XRP", "SOL"],  
        toCoin="USDC",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "quoteId": "1010075157602510902217555968",  
            "result": {  
                "quoteCreateTime": "1766126593232",  
                "quoteExpireTime": "1766126623231",  
                "exchangeCoins": [  
                    {  
                        "fromCoin": "SOL",  
                        "supportConvert": 1,  
                        "availableBalance": "0.000003",  
                        "baseValue": "0.00036837",  
                        "toCoin": "USDC",  
                        "toAmount": "0.00035721396701649",  
                        "exchangeRate": "119.07132233883026",  
                        "feeInfo": {  
                            "feeCoin": "USDC",  
                            "amount": "0.00000729008095952",  
                            "feeRate": "0.02"  
                        },  
                        "taxFeeInfo": {  
                            "totalAmount": "0",  
                            "feeCoin": "",  
                            "taxFeeItems": []  
                        }  
                    },  
                    {  
                        "fromCoin": "XRP",  
                        "supportConvert": 1,  
                        "availableBalance": "0.0002",  
                        "baseValue": "0.00024536",  
                        "toCoin": "USDC",  
                        "toAmount": "0.000359866676661744",  
                        "exchangeRate": "1.79933338330872",  
                        "feeInfo": {  
                            "feeCoin": "USDC",  
                            "amount": "0.000007344217891056",  
                            "feeRate": "0.02"  
                        },  
                        "taxFeeInfo": {  
                            "totalAmount": "0",  
                            "feeCoin": "",  
                            "taxFeeItems": []  
                        }  
                    }  
                ],  
                "totalFeeInfo": {  
                    "feeCoin": "USDC",  
                    "amount": "0.000014634298850576",  
                    "feeRate": "0.02"  
                },  
                "totalTaxFeeInfo": {  
                    "totalAmount": "0",  
                    "feeCoin": "",  
                    "taxFeeItems": []  
                }  
            }  
        },  
        "retExtInfo": {},  
        "time": 1766126593232  
    }

---

# 獲取報價

三方託管帳戶, 比如copper, fireblock等帳戶是**無法** 做兌換的

信息

  * API密鑰權限: `Convert`
  * API速率限制: `5 req /s`
  * 在統一交易賬戶下，您**真實的成交數量可能小於可用餘額** ，若您同時提交多個幣種的兌換請求，則可能會部分成交，請您以實際到賬數量爲準。



### HTTP 請求

POST`/v5/asset/covert/get-quote`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
accountType| **true**|  string| 錢包類型，`eb_convert_uta`，僅支持統一錢包  
fromCoinList| **true**|  array<string>| 源幣種列表，例如`["BTC", "XRP", "ETH"]`，每筆交易最多支持20種幣種  
toCoin| **true**|  string| 目標幣種，每次請求支持MNT、USDT或USDC之一  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
quoteId| string| 報價交易ID，由系統生成，用於確認報價和查詢交易結果  
result| object|   
> quoteCreateTime| string| 報價創建時間戳  
> quoteExpireTime| string| 報價過期時間戳，有效期30秒  
> exchangeCoins| array<object>| 報價詳情  
>> fromCoin| string| 源幣種  
>> supportConvert| integer| `1`: 支持, `2`: 不支持  
>> availableBalance| string| 可提现餘額  
>> baseValue| string| USDT等值金額  
>> toCoin| string| 目標幣種  
>> toAmount| string| 預計接收金額  
>> exchangeRate| string| 匯率  
>> feeInfo| object| 兌換手續費信息  
>>> feeCoin| string| 手續費幣種  
>>> amount| string| 手續費金額  
>>> feeRate| string| 手續費率  
>> taxFeeInfo| object| 稅費信息  
>>> totalAmount| string| 稅費總額  
>>> feeCoin| string| 稅費幣種  
>>> taxFeeItems| array| 稅費項目  
> totalFeeInfo| object| 總兌換手續費詳情  
>> feeCoin| string| 手續費幣種  
>> amount| string| 總手續費金額  
>> feeRate| string| 手續費率  
> totalTaxFeeInfo| object| 總稅費信息  
>> totalAmount| string| 總稅費金額  
>> feeCoin| string| 稅費幣種  
>> taxFeeItems| array| 稅費項目  
  
### 請求示例

  * HTTP
  * Python


    
    
    POST /v5/asset/covert/get-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1766126592271  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    Content-Length: 97  
      
    {  
        "accountType": "eb_convert_uta",  
        "fromCoinList": ["XRP", "SOL"],  
        "toCoin": "USDC"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.request_a_quote_small_balance(  
        accountType="eb_convert_uta",  
        fromCoinList=["XRP", "SOL"],  
        toCoin="USDC",  
    ))  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "quoteId": "1010075157602510902217555968",  
            "result": {  
                "quoteCreateTime": "1766126593232",  
                "quoteExpireTime": "1766126623231",  
                "exchangeCoins": [  
                    {  
                        "fromCoin": "SOL",  
                        "supportConvert": 1,  
                        "availableBalance": "0.000003",  
                        "baseValue": "0.00036837",  
                        "toCoin": "USDC",  
                        "toAmount": "0.00035721396701649",  
                        "exchangeRate": "119.07132233883026",  
                        "feeInfo": {  
                            "feeCoin": "USDC",  
                            "amount": "0.00000729008095952",  
                            "feeRate": "0.02"  
                        },  
                        "taxFeeInfo": {  
                            "totalAmount": "0",  
                            "feeCoin": "",  
                            "taxFeeItems": []  
                        }  
                    },  
                    {  
                        "fromCoin": "XRP",  
                        "supportConvert": 1,  
                        "availableBalance": "0.0002",  
                        "baseValue": "0.00024536",  
                        "toCoin": "USDC",  
                        "toAmount": "0.000359866676661744",  
                        "exchangeRate": "1.79933338330872",  
                        "feeInfo": {  
                            "feeCoin": "USDC",  
                            "amount": "0.000007344217891056",  
                            "feeRate": "0.02"  
                        },  
                        "taxFeeInfo": {  
                            "totalAmount": "0",  
                            "feeCoin": "",  
                            "taxFeeItems": []  
                        }  
                    }  
                ],  
                "totalFeeInfo": {  
                    "feeCoin": "USDC",  
                    "amount": "0.000014634298850576",  
                    "feeRate": "0.02"  
                },  
                "totalTaxFeeInfo": {  
                    "totalAmount": "0",  
                    "feeCoin": "",  
                    "taxFeeItems": []  
                }  
            }  
        },  
        "retExtInfo": {},  
        "time": 1766126593232  
    }