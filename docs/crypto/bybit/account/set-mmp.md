---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/set-mmp
api_type: Account
updated_at: 2026-11-13 19:20:55.375608
---

# Set MMP

info

## What is MMP?

_Market Maker Protection_ (MMP) is an automated mechanism designed to protect market makers (MM) against liquidity risks and over-exposure in the market. It prevents simultaneous trade executions on quotes provided by the MM within a short time span. The MM can automatically pull their quotes if the number of contracts traded for an underlying asset exceeds the configured threshold within a certain time frame. Once MMP is triggered, any pre-existing MMP orders will be **automatically cancelled** , and new orders tagged as MMP will be **rejected** for a specific duration — known as the frozen period — so that MM can reassess the market and modify the quotes.

## How to enable MMP

Send an email to Bybit ([financial.inst@bybit.com](mailto:financial.inst@bybit.com)) or contact your business development (BD) manager to apply for MMP. After processed, the default settings are as below table:

Parameter| Type| Comments| Default value  
---|---|---|---  
baseCoin| string| Base coin| BTC  
window| string| Time window (millisecond)| 5000  
frozenPeriod| string| Frozen period (millisecond)| 100  
qtyLimit| string| Quantity limit| 100  
deltaLimit| string| Delta limit| 100  
vegaLimit| string| Vega limit| 500000  
  
## Applicable

Effective for **options** only. When you place an `option` order, set `mmp`=true, which means you mark this order as a mmp order.

## Some points to note

  1. Only maker order qty and delta will be counted into `qtyLimit` and `deltaLimit`.
  2. `qty_limit` is the sum of absolute value of qty of each trade executions. `delta_limit` is the absolute value of the sum of qty*delta. If any of these reaches or exceeds the limit amount, the account's market maker protection will be triggered.



### HTTP Request

POST`/v5/account/mmp-modify`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
baseCoin| **true**|  string| Base coin, uppercase only  
window| **true**|  string| Time window (ms)  
frozenPeriod| **true**|  string| Frozen period (ms). "0" means the trade will remain frozen until manually reset  
qtyLimit| **true**|  string| Trade qty limit (positive and up to 2 decimal places)  
deltaLimit| **true**|  string| Delta limit (positive and up to 2 decimal places)  
vegaLimit| false| string| Vega limit (positive and up to 2 decimal places). Default: `500000`  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/mmp-modify HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675833524616  
    X-BAPI-RECV-WINDOW: 50000  
    Content-Type: application/json  
      
    {  
        "baseCoin": "ETH",  
        "window": "5000",  
        "frozenPeriod": "100000",  
        "qtyLimit": "50",  
        "deltaLimit": "20"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_mmp(  
        baseCoin="ETH",  
        window="5000",  
        frozenPeriod="100000",  
        qtyLimit="50",  
        deltaLimit="20"  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setMMP({  
            baseCoin: 'ETH',  
            window: '5000',  
            frozenPeriod: '100000',  
            qtyLimit: '50',  
            deltaLimit: '20',  
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
        "retMsg": "success"  
    }

---

# 设置市商保護

信息

## 什麼是MMP?

_市商保護機制_(Market Maker Protection)，旨在保護為平台提供流動性的做市商，防止在一定時間窗口內產生大量成交，導致流動性風險過度集中甚至擊穿某個做市商流動性。一旦某個賬戶 在短時間內的總交易額超過了配置的限額，該賬戶的做市商保護將被觸發。當做市商保護被觸發時，賬戶現有的做市商保護訂單（被標記為做市商保護的訂單）將被 交易引擎**自動取消** ，而該賬戶新的做市商保護訂單將在未來一段時間（稱為凍結期）被**拒絕** （常規非MMP訂單不受影響）。用戶可以利用這段時間重新評估行情並修改報價。

## 如何開通MMP

您可通過郵件Bybit【[financial.inst@bybit.com](mailto:financial.inst@bybit.com)】或聯繫對應的客戶經理申請開通。 開通後，MMP的默認配置為:

參數| 類型| 說明| 默認值  
---|---|---|---  
baseCoin| string| 交易幣種| BTC  
window| string| 時間窗口 (毫秒)| 5000  
frozenPeriod| string| 凍結時間段 (毫秒)| 100  
qtyLimit| string| 成交數量上限| 100  
deltaLimit| string| Delta值上限| 100  
vegaLimit| string| Vega 上限| 500000  
  
## 適用對象

僅適用於**期權** 交易. 當創建期權訂單時, 設置參數`mmp`=true, 則表示將此訂單納入市商保護。

## 一些注意事項

  1. 只有掛單成交qty和delta會被計入`qtyLimit`和`deltaLimit`。
  2. `qty_limit` 是每筆交易執行數量的絕對值總和。 `delta_limit` 是 qty*delta 總和的絕對值。 如果其中任何一項達到或超過限額，該帳戶的做市商保護將會被觸發。



### HTTP 請求

POST`/v5/account/mmp-modify`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
baseCoin| **true**|  string| 交易幣種  
window| **true**|  string| 時間窗口 (毫秒)  
frozenPeriod| **true**|  string| 凍結時間長度 (毫秒). 設置為"0"則表示帳戶會保持凍結狀態，除非手動重置  
qtyLimit| **true**|  string| 成交數量上限 (正數，至多2位小數)  
deltaLimit| **true**|  string| Delta上限 (正數，至多2位小數)  
vegaLimit| false| string| Vega 上限（正數，至多2位小數），預設值：`500000`  
  
### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/mmp-modify HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675833524616  
    X-BAPI-RECV-WINDOW: 50000  
    Content-Type: application/json  
      
    {  
        "baseCoin": "ETH",  
        "window": "5000",  
        "frozenPeriod": "100000",  
        "qtyLimit": "50",  
        "deltaLimit": "20"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_mmp(  
        baseCoin="ETH",  
        window="5000",  
        frozenPeriod="100000",  
        qtyLimit="50",  
        deltaLimit="20"  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setMMP({  
            baseCoin: 'ETH',  
            window: '5000',  
            frozenPeriod: '100000',  
            qtyLimit: '50',  
            deltaLimit: '20',  
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
        "retMsg": "success"  
    }