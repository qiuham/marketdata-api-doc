---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/fiat-convert/query-coin-list
api_type: REST
updated_at: 2026-11-13 19:21:44.087245
---

# Get Trading Pair List

Query for the list of coins you can convert to/from.

### HTTP Request

GET`/v5/fiat/query-coin-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
side| false| string| `0`: buy, buy crypto sell fiat; `1`: sell, sell crypto buy fiat  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
fiats| array| Fiat coin list  
> coin| string| Fiat coin code  
> fullName| string| Fiat full coin name  
> icon| string| Coin icon url  
> iconNight| string| Coin icon url (dark mode)  
> precision| integer| Fiat precision  
> disable| boolean| `true`: the coin is disabled, `false`: the coin is allowed  
> singleFromMinLimit| string| For buy side, the minimum amount of fiatCoin per transaction  
> singleFromMaxLimit| string| For buy side, the maximum amount of fiatCoin per transaction  
cryptos| array| Crypto coin list  
> coin| string| Fiat coin code  
> fullName| string| Fiat full coin name  
> icon| string| Coin icon url  
> iconNight| string| Coin icon url (dark mode)  
> precision| integer| Fiat precision  
> disable| boolean| `true`: the coin is disabled, `false`: the coin is allowed  
> singleFromMinLimit| string| For sell side, the minimum amount of cryptoCoin per transaction  
> singleFromMaxLimit| string| For sell side, the maximum amount of cryptoCoin per transaction  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/fiat/query-coin-list?side=0 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720064061248  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_fiat_trading_pair_list(  
        side="0"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "fiats": [  
                {  
                    "coin": "GEL",  
                    "fullName": "Georgian Lari",  
                    "icon": "https://s1.bycsi.com/common-static/wove/fiat-admin/2023-5-4/Tyoe=GEL.svg",  
                    "iconNight": "https://s1.bycsi.com/common-static/wove/fiat-admin/2023-5-4/Tyoe=GEL.svg",  
                    "precision": 2,  
                    "disable": false,  
                    "singleFromMinLimit": "10",  
                    "singleFromMaxLimit": "100000"  
                }  
            ],  
            "cryptos": [  
                {  
                    "coin": "USDT",  
                    "fullName": "Tether USDT",  
                    "icon": "https://s1.bycsi.com/common-static/wove/fiat-admin/2024-8-5/8e50959d5f3e45bebf522e0cad456439_1726814031848.svg",  
                    "iconNight": "https://s1.bycsi.com/common-static/wove/fiat-admin/2024-8-5/8e50959d5f3e45bebf522e0cad456439_1726814031848.svg",  
                    "precision": 4,  
                    "disable": false,  
                    "singleFromMinLimit": "10",  
                    "singleFromMaxLimit": "10000"  
                },  
                {  
                    "coin": "BTC",  
                    "fullName": "Bitcoin",  
                    "icon": "https://s1.bycsi.com/common-static/wove/fiat-admin/20d09e76a0ab401f80bd545ae874c6a3_48x48.svg",  
                    "iconNight": "https://s1.bycsi.com/common-static/wove/fiat-admin/20d09e76a0ab401f80bd545ae874c6a3_48x48.svg",  
                    "precision": 8,  
                    "disable": false,  
                    "singleFromMinLimit": "0.0001",  
                    "singleFromMaxLimit": "1"  
                },  
                {  
                    "coin": "ETH",  
                    "fullName": "Ethereum",  
                    "icon": "https://s1.bycsi.com/common-static/wove/fiat-admin/40b217058a474e17b5d88653b039055c_48x48.svg",  
                    "iconNight": "https://s1.bycsi.com/common-static/wove/fiat-admin/40b217058a474e17b5d88653b039055c_48x48.svg",  
                    "precision": 8,  
                    "disable": false,  
                    "singleFromMinLimit": "0.002",  
                    "singleFromMaxLimit": "5"  
                }  
            ]  
        }  
    }

---

# 查詢兌換幣種列表

查詢可兌換的幣種列表 

### HTTP 請求

GET`/v5/fiat/query-coin-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
side| false| integer| `0`: 買入，即買入加密貨幣賣出法幣；`1`: 賣出，即賣出加密貨幣買入法幣  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
fiats| array| 法幣列表  
> coin| string| 法幣代碼code  
> fullName| string| 法幣全名  
> icon| string| 幣種icon URL  
> iconNight| string| 幣種icon URL（深色模式）  
> precision| integer| 法幣精度  
> disable| boolean| `true`: 該幣種被禁用，`false`: 該幣種可用  
> singleFromMinLimit| string| 對於買入方向，每筆交易的最小法幣數量  
> singleFromMaxLimit| string| 對於買入方向，每筆交易的最大法幣數量  
cryptos| array| 加密貨幣列表  
> coin| string| 加密貨幣代碼code  
> fullName| string| 加密貨幣全名  
> icon| string| 幣種icon URL  
> iconNight| string| 幣種icon URL（深色模式）  
> precision| integer| 加密貨幣精度  
> disable| boolean| `true`: 該幣種被禁用，`false`: 該幣種可用  
> singleFromMinLimit| string| 對於賣出方向，每筆交易的最小加密貨幣數量  
> singleFromMaxLimit| string| 對於賣出方向，每筆交易的最大加密貨幣數量  
  
### 請求示例

  * HTTP


    
    
    GET /v5/fiat/query-coin-list?side=0 HTTP/1.1    
    Host: api-testnet.bybit.com    
    X-BAPI-SIGN: XXXXXX    
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx    
    X-BAPI-TIMESTAMP: 1720064061248    
    X-BAPI-RECV-WINDOW: 5000    
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "fiats": [  
                {  
                    "coin": "GEL",  
                    "fullName": "Georgian Lari",  
                    "icon": "https://s1.bycsi.com/common-static/wove/fiat-admin/2023-5-4/Tyoe=GEL.svg",  
                    "iconNight": "https://s1.bycsi.com/common-static/wove/fiat-admin/2023-5-4/Tyoe=GEL.svg",  
                    "precision": 2,  
                    "disable": false,  
                    "singleFromMinLimit": "10",  
                    "singleFromMaxLimit": "100000"  
                }  
            ],  
            "cryptos": [  
                {  
                    "coin": "USDT",  
                    "fullName": "Tether USDT",  
                    "icon": "https://s1.bycsi.com/common-static/wove/fiat-admin/2024-8-5/8e50959d5f3e45bebf522e0cad456439_1726814031848.svg",  
                    "iconNight": "https://s1.bycsi.com/common-static/wove/fiat-admin/2024-8-5/8e50959d5f3e45bebf522e0cad456439_1726814031848.svg",  
                    "precision": 4,  
                    "disable": false,  
                    "singleFromMinLimit": "10",  
                    "singleFromMaxLimit": "10000"  
                },  
                {  
                    "coin": "BTC",  
                    "fullName": "Bitcoin",  
                    "icon": "https://s1.bycsi.com/common-static/wove/fiat-admin/20d09e76a0ab401f80bd545ae874c6a3_48x48.svg",  
                    "iconNight": "https://s1.bycsi.com/common-static/wove/fiat-admin/20d09e76a0ab401f80bd545ae874c6a3_48x48.svg",  
                    "precision": 8,  
                    "disable": false,  
                    "singleFromMinLimit": "0.0001",  
                    "singleFromMaxLimit": "1"  
                },  
                {  
                    "coin": "ETH",  
                    "fullName": "Ethereum",  
                    "icon": "https://s1.bycsi.com/common-static/wove/fiat-admin/40b217058a474e17b5d88653b039055c_48x48.svg",  
                    "iconNight": "https://s1.bycsi.com/common-static/wove/fiat-admin/40b217058a474e17b5d88653b039055c_48x48.svg",  
                    "precision": 8,  
                    "disable": false,  
                    "singleFromMinLimit": "0.002",  
                    "singleFromMaxLimit": "5"  
                }  
            ]  
        }  
    }