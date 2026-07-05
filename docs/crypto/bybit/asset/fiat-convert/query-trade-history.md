---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/fiat-convert/query-trade-history
api_type: REST
updated_at: 2026-07-05 19:06:13.165098
---

# Get Reference Price

### HTTP Request

GET`/v5/fiat/reference-price`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Coin Pair, such as EUR-USDT  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Array of quotes  
> symbol| string| Trading pair symbol  
> fiat| string| Fiat currency of the trading pair (e.g: "EUR")  
> crypto| string| Cryptocurrency of the trading pair (e.g:"USDT")  
> timestamp| string| Unix timestamp  
> buys| array| Array of buy quote objects  
>> unitPrice| string| unitPrice: 1 crypto=x fiat  
>> paymentMethod| string| From coin type. `fiat` or `crypto`  
> sells| array| Array of sell quote objects  
>> unitPrice| string| unitPrice: 1 crypto=x fiat  
>> paymentMethod| string| From coin type. `fiat` or `crypto`  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/fiat/reference-price HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720074159814  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_fiat_reference_price(  
        symbol="EUR-USDT"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "symbol": "EUR-USDT",  
            "fiat": "EUR",  
            "crypto": "USDT",  
            "timestamp": "1765181161",  
            "buys": [  
                {  
                    "unitPrice": "0.8581",  
                    "paymentMethod": "Cash Balance"  
                },  
                {  
                    "unitPrice": "0.9297487",  
                    "paymentMethod": "Credit Card"  
                },  
                {  
                    "unitPrice": "0.9807915",  
                    "paymentMethod": "Apple Pay"  
                },  
                {  
                    "unitPrice": "0.8631747",  
                    "paymentMethod": "Google Pay"  
                }  
            ],  
            "sells": [  
                {  
                    "unitPrice": "0.8581",  
                    "paymentMethod": "Cash Balance"  
                },  
                {  
                    "unitPrice": "0.9297487",  
                    "paymentMethod": "Credit Card"  
                },  
                {  
                    "unitPrice": "0.9807915",  
                    "paymentMethod": "Apple Pay"  
                },  
                {  
                    "unitPrice": "0.8631747",  
                    "paymentMethod": "Google Pay"  
                },  
                {  
                    "unitPrice": "0.8584759",  
                    "paymentMethod": "SEPA"  
                }  
            ]  
        }  
    }

---

# 獲取報價

### HTTP 請求

GET`/v5/fiat/reference-price`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 幣種交易對，例如 EUR-USDT  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| 報價列表  
> symbol| string| 幣種交易對  
> fiat| string| 交易對中的法幣（例如："EUR"）  
> crypto| string| 交易對中的加密貨幣（例如："USDT"）  
> timestamp| string| Unix 時間戳  
> buys| array| 買入報價列表  
>> unitPrice| string| 單價：1 crypto = x fiat  
>> paymentMethod| string| 支付方式,`fiat` 或 `crypto`  
> sells| array| 賣出報價列表  
>> unitPrice| string| 單價：1 crypto = x fiat  
>> paymentMethod| string| 支付方式,`fiat` 或 `crypto`  
  
### 請求示例

  * HTTP


    
    
    GET /v5/fiat/reference-price HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720074159814  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "symbol": "EUR-USDT",  
            "fiat": "EUR",  
            "crypto": "USDT",  
            "timestamp": "1765181161",  
            "buys": [  
                {  
                    "unitPrice": "0.8581",  
                    "paymentMethod": "Cash Balance"  
                },  
                {  
                    "unitPrice": "0.9297487",  
                    "paymentMethod": "Credit Card"  
                },  
                {  
                    "unitPrice": "0.9807915",  
                    "paymentMethod": "Apple Pay"  
                },  
                {  
                    "unitPrice": "0.8631747",  
                    "paymentMethod": "Google Pay"  
                }  
            ],  
            "sells": [  
                {  
                    "unitPrice": "0.8581",  
                    "paymentMethod": "Cash Balance"  
                },  
                {  
                    "unitPrice": "0.9297487",  
                    "paymentMethod": "Credit Card"  
                },  
                {  
                    "unitPrice": "0.9807915",  
                    "paymentMethod": "Apple Pay"  
                },  
                {  
                    "unitPrice": "0.8631747",  
                    "paymentMethod": "Google Pay"  
                },  
                {  
                    "unitPrice": "0.8584759",  
                    "paymentMethod": "SEPA"  
                }  
            ]  
        }  
    }