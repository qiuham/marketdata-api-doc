---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/otc/margin-coin-convert-info
api_type: REST
updated_at: 2026-08-20 18:45:00.296694
---

# Get Margin Coin Info

tip

  * When queried without an API key, this endpoint returns public margin data
  * If your UID is bound with an OTC loan, then you can get your private margin data by calling with your API key
  * If your UID is not bound with an OTC loan but you passed your API key, this endpoint returns public margin data



### HTTP Request

GET`/v5/ins-loan/ensure-tokens-convert`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| false| string| Product ID. If not passed, returns all margin products. For spot, it returns coins with a `convertRatio` greater than 0.  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
marginToken| array| Object  
> productId| string| Product Id  
> tokenInfo| array| Spot margin coin  
>> token| string| Margin coin  
>> convertRatioList| array| Margin coin convert ratio List  
>>> ladder| string| ladder  
>>> convertRatio| string| Margin coin convert ratio  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/ensure-tokens-convert HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_margin_coin_info())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingMarginCoinInfoWithConversionRate({  
        productId: '81',  
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
            "marginToken": [  
                {  
                    "productId": "81",  
                    "tokenInfo": [  
                        {  
                            "token": "USDT",  
                            "convertRatioList": [  
                                {  
                                    "ladder": "0-500",  
                                    "convertRatio": "0.95"  
                                },  
                                {  
                                    "ladder": "500-1000",  
                                    "convertRatio": "0.9"  
                                },  
                                {  
                                    "ladder": "1000-2000",  
                                    "convertRatio": "0.8"  
                                },  
                                {  
                                    "ladder": "2000-4000",  
                                    "convertRatio": "0.7"  
                                },  
                                {  
                                    "ladder": "4000-99999999999",  
                                    "convertRatio": "0.6"  
                                }  
                            ]  
                        }  
                      ...  
                    ]  
                },  
                {  
                    "productId": "82",  
                    "tokenInfo": [  
                        ...  
                        {  
                            "token": "USDT",  
                            "convertRatioList": [  
                                {  
                                    "ladder": "0-1000",  
                                    "convertRatio": "0.7"  
                                },  
                                {  
                                    "ladder": "1000-2000",  
                                    "convertRatio": "0.65"  
                                },  
                                {  
                                    "ladder": "2000-99999999999",  
                                    "convertRatio": "0.6"  
                                }  
                            ]  
                        }  
                    ]  
                },  
                {  
                    "productId": "84",  
                    "tokenInfo": [  
                        ...  
                        {  
                            "token": "BTC",  
                            "convertRatioList": [  
                                {  
                                    "ladder": "0-1000",  
                                    "convertRatio": "1"  
                                },  
                                {  
                                    "ladder": "1000-5000",  
                                    "convertRatio": "0.9"  
                                },  
                                {  
                                    "ladder": "5000-99999999999",  
                                    "convertRatio": "0.55"  
                                }  
                            ]  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1683276016497  
    }

---

# 查詢保證金幣種信息

提示

  * 該接口在不傳入api key和secret進行鑒權時, 則返回公共數據
  * 該接口在傳入api key和secret進行鑒權時且uid綁定了場外借貸產品, 則返回特定的保證金幣種數據



### HTTP 請求

GET`/v5/ins-loan/ensure-tokens-convert`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
productId| false| string| 產品ID. 若不傳，則返回所有產品的保證金幣種信息. 現貨返回折算率大於0的幣種.  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
marginToken| array| Object  
> productId| string| 產品ID  
> tokenInfo| array| 現貨保證金幣種信息  
>> token| string| 保證金幣種  
>> convertRatioList| array| 保證金幣種折算率列  
>>> ladder| string| 階梯  
>>> convertRatio| string| 折算率  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/ensure-tokens HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_margin_coin_info())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingMarginCoinInfoWithConversionRate({  
        productId: '81',  
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
            "marginToken": [  
                {  
                    "productId": "81",  
                    "tokenInfo": [  
                        {  
                            "token": "USDT",  
                            "convertRatioList": [  
                                {  
                                    "ladder": "0-500",  
                                    "convertRatio": "0.95"  
                                },  
                                {  
                                    "ladder": "500-1000",  
                                    "convertRatio": "0.9"  
                                },  
                                {  
                                    "ladder": "1000-2000",  
                                    "convertRatio": "0.8"  
                                },  
                                {  
                                    "ladder": "2000-4000",  
                                    "convertRatio": "0.7"  
                                },  
                                {  
                                    "ladder": "4000-99999999999",  
                                    "convertRatio": "0.6"  
                                }  
                            ]  
                        }  
                      ...  
                    ]  
                },  
                {  
                    "productId": "82",  
                    "tokenInfo": [  
                        ...  
                        {  
                            "token": "USDT",  
                            "convertRatioList": [  
                                {  
                                    "ladder": "0-1000",  
                                    "convertRatio": "0.7"  
                                },  
                                {  
                                    "ladder": "1000-2000",  
                                    "convertRatio": "0.65"  
                                },  
                                {  
                                    "ladder": "2000-99999999999",  
                                    "convertRatio": "0.6"  
                                }  
                            ]  
                        }  
                    ]  
                },  
                {  
                    "productId": "84",  
                    "tokenInfo": [  
                        ...  
                        {  
                            "token": "BTC",  
                            "convertRatioList": [  
                                {  
                                    "ladder": "0-1000",  
                                    "convertRatio": "1"  
                                },  
                                {  
                                    "ladder": "1000-5000",  
                                    "convertRatio": "0.9"  
                                },  
                                {  
                                    "ladder": "5000-99999999999",  
                                    "convertRatio": "0.55"  
                                }  
                            ]  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1683276016497  
    }