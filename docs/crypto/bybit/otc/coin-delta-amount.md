---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/otc/coin-delta-amount
api_type: REST
updated_at: 2026-07-01 19:30:53.644375
---

# Get Product Info

tip

  * When queried without an API key, this endpoint returns public product data
  * If your UID is bound with an OTC loan, then you can get your private product data by calling with your API key
  * If your UID is not bound with an OTC loan but you passed your API key, this endpoint returns public product data



### HTTP Request

GET`/v5/ins-loan/product-infos`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| false| string| Product ID. If not passed, returns all products  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
marginProductInfo| array| Object  
> productId| string| Product ID  
> leverage| string| The maximum leverage for this loan product  
> supportSpot| integer| Whether or not Spot is supported. 0:false; 1:true  
> supportContract| integer| Whether USDT Perpetuals are supported. 0:false; 1:true  
> supportMarginTrading| integer| Whether or not Spot margin trading is supported. 0:false; 1:true  
> deferredLiquidationLine| string| Line for deferred liquidation  
> deferredLiquidationTime| string| Time for deferred liquidation  
> withdrawLine| string| Restrict line for withdrawal  
> transferLine| string| Restrict line for transfer  
> spotBuyLine| string| Restrict line for Spot buy  
> spotSellLine| string| Restrict line for Spot trading  
> contractOpenLine| string| Restrict line for USDT Perpetual open position  
> liquidationLine| string| Line for liquidation  
> stopLiquidationLine| string| Line for stop liquidation  
> contractLeverage| string| The allowed default leverage for USDT Perpetual  
> transferRatio| string| The transfer ratio for loan funds to transfer from Spot wallet to Contract wallet  
> spotSymbols| array| The whitelist of spot trading pairs 

  * If `supportSpot`="0", then it returns "[]"
  * If empty array, then you can trade any symbols
  * If not empty, then you can only trade listed symbols

  
> contractSymbols| array| The whitelist of contract trading pairs 

  * If `supportContract`="0", then it returns "[]"
  * If empty array, then you can trade any symbols
  * If not empty, then you can only trade listed symbols

  
> supportUSDCContract| integer| Whether or not USDC contracts are supported. `'0'`:false; `'1'`:true  
> supportUSDCOptions| integer| Whether or not Options are supported. `'0'`:false; `'1'`:true  
> USDTPerpetualOpenLine| string| Restrict line to open USDT Perpetual position  
> USDCContractOpenLine| string| Restrict line to open USDC Contract position  
> USDCOptionsOpenLine| string| Restrict line to open Option position  
> USDTPerpetualCloseLine| string| Restrict line to trade USDT Perpetual  
> USDCContractCloseLine| string| Restrict line to trade USDC Contract  
> USDCOptionsCloseLine| string| Restrict line to trade Option  
> USDCContractSymbols| array| The whitelist of USDC contract trading pairs 

  * If `supportContract`="0", then it returns "[]"
  * If no whitelist symbols, it is `[]`, and you can trade any
  * If supportUSDCContract="0", it is `[]`

  
> USDCOptionsSymbols| array| The whitelist of Option symbols 

  * If `supportContract`="0", then it returns "[]"
  * If no whitelisted, it is `[]`, and you can trade any
  * If supportUSDCOptions="0", it is `[]`

  
> marginLeverage| string| The allowable maximum leverage for Spot margin trading. If `supportMarginTrading`=0, then it returns ""  
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
> productType| string| Product type. `0`: Default, `1`: CTA, `2`: Hedge  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/product-infos?productId=91 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_product_info(productId="91"))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingProductInfo({  
        productId: '91',  
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
            "marginProductInfo": [  
                {  
                    "productId": "91",  
                    "leverage": "4.00000000",  
                    "supportSpot": 1,  
                    "supportContract": 0,  
                    "withdrawLine": "",  
                    "transferLine": "",  
                    "spotBuyLine": "",  
                    "spotSellLine": "",  
                    "contractOpenLine": "",  
                    "liquidationLine": "0.75",  
                    "stopLiquidationLine": "0.35000000",  
                    "contractLeverage": "0",  
                    "transferRatio": "0",  
                    "spotSymbols": [],  
                    "contractSymbols": [],  
                    "supportUSDCContract": 0,  
                    "supportUSDCOptions": 0,  
                    "USDTPerpetualOpenLine": "",  
                    "USDCContractOpenLine": "",  
                    "USDCOptionsOpenLine": "",  
                    "USDTPerpetualCloseLine": "",  
                    "USDCContractCloseLine": "",  
                    "USDCOptionsCloseLine": "",  
                    "USDCContractSymbols": [],  
                    "USDCOptionsSymbols": [],  
                    "marginLeverage": "0",  
                    "USDTPerpetualLeverage": [],  
                    "USDCContractLeverage": [],  
                    "deferredLiquidationLine":"",  
                    "deferredLiquidationTime":"",  
                    "productType": "0"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1689747746332  
    }

---

# 查詢產品信息

提示

  * 該接口在不傳入api key和secret進行鑒權時, 則返回公共產品數據
  * 該接口在傳入api key和secret進行鑒權時且uid綁定了場外借貸產品, 則返回特定的產品數據



### HTTP 請求

GET`/v5/ins-loan/product-infos`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
productId| false| string| 產品ID. 若不傳，則返回所有產品數據  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
marginProductInfo| array| Object  
> productId| string| 產品ID  
> leverage| string| 該借貸產品的最大槓桿倍數  
> supportSpot| integer| 是否支持現貨. `0`:否; `1`:是  
> supportContract| integer| 是否支持合約 . `0`: 否; `1`: 是  
> withdrawLine| string| 限制提幣線  
> transferLine| string| 限制劃轉線  
> spotBuyLine| string| 限制現貨買入線  
> spotSellLine| string| 限制現貨交易線  
> contractOpenLine| string| 限制合約開倉線  
> liquidationLine| string| 強平線  
> stopLiquidationLine| string| 停止強平線  
> contractLeverage| string| 允許USDT永續默認開倉倍數  
> transferRatio| string| 現貨帳戶到合約帳戶的借貸資金劃轉比例  
> spotSymbols| array| 現貨交易對白名單. 若沒有配置白名單, 則返回[]  
> contractSymbols| array| USDT永續合約交易對白名單 

  * 若沒有配置白名單, 則返回[]
  * 若supportContract="0", 則也是[]

  
> supportUSDCContract| integer| 是否支持USDC合約交易. `'0'`:否; `'1'`:是  
> supportUSDCOptions| integer| 是否支持期權交易. `'0'`:false; `'1'`:true  
> supportMarginTrading| integer| 是否支持現貨槓桿交易. `0`: 否; `1`: 是  
> deferredLiquidationLine| string| 延期清算線  
> deferredLiquidationTime| string| 延期清算時間  
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
> productType| string| 產品類型. `0`: 默認, `1`: CTA, `2`: 對沖  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/product-infos?productId=91 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_product_info(productId="91"))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingProductInfo({  
        productId: '91',  
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
            "marginProductInfo": [  
                {  
                    "productId": "91",  
                    "leverage": "4.00000000",  
                    "supportSpot": 1,  
                    "supportContract": 0,  
                    "withdrawLine": "",  
                    "transferLine": "",  
                    "spotBuyLine": "",  
                    "spotSellLine": "",  
                    "contractOpenLine": "",  
                    "liquidationLine": "0.75",  
                    "stopLiquidationLine": "0.35000000",  
                    "contractLeverage": "0",  
                    "transferRatio": "0",  
                    "spotSymbols": [],  
                    "contractSymbols": [],  
                    "supportUSDCContract": 0,  
                    "supportUSDCOptions": 0,  
                    "USDTPerpetualOpenLine": "",  
                    "USDCContractOpenLine": "",  
                    "USDCOptionsOpenLine": "",  
                    "USDTPerpetualCloseLine": "",  
                    "USDCContractCloseLine": "",  
                    "USDCOptionsCloseLine": "",  
                    "USDCContractSymbols": [],  
                    "USDCOptionsSymbols": [],  
                    "marginLeverage": "0",  
                    "USDTPerpetualLeverage": [],  
                    "USDCContractLeverage": [],  
                    "deferredLiquidationLine":"",  
                    "deferredLiquidationTime":"",  
                    "productType": "0"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1689747746332  
    }