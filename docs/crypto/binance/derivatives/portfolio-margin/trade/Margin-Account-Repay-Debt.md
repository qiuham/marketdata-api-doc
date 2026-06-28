---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt
api_type: Trading
updated_at: 2026-01-15T23:45:33.401426
---

# Margin Account Repay Debt(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#api-description "Direct link to API Description")

Repay debt for a margin loan.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#http-request "Direct link to HTTP Request")

POST `/papi/v1/margin/repay-debt`

## Request Weight(Order)[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#request-weightorder "Direct link to Request Weight\(Order\)")

**3000**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
amount| STRING| NO|   
specifyRepayAssets| STRING| NO| Specific asset list to repay debt; Can be added in batch, separated by commas  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
>   * The repay asset amount cannot exceed 50000 USD equivalent value for a single request.
>   * If `amount` is not sent, all the asset loan will be repaid if having enough specific repay assets.
>   * If `amount` is sent, only the certain amount of the asset loan will be repaid if having enough specific repay assets.
>   * The system will use the same asset to repay the loan first (if have) no matter whether put the asset in `specifyRepayAssets`
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#response-example "Direct link to Response Example")
    
    
    {  
        "amount": "0.10000000",  
    	"asset": "BNB",  
        "specifyRepayAssets": [  
        "USDT",  
        "BTC"  
    	],  
        "updateTime": 1636371437000  
    	"success": true  
    }

---

# 杠杆账户还款(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#接口描述 "接口描述的直接链接")

杠杆账户还款

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#http请求 "HTTP请求的直接链接")

POST `/papi/v1/margin/repay-debt`

## 请求权重(Order)[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#请求权重order "请求权重\(Order\)的直接链接")

**3000**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
amount| STRING| NO|   
specifyRepayAssets| STRING| NO| 指定还款资产，多资产用逗号分隔  
recvWindow| LONG| NO| 赋值不能超过`60000`  
timestamp| LONG| YES|   
  
>   * 单次还款价值需小于等于 50000 USD
>   * 如果`amount`未发送，则在有足够的特定偿还资产的情况下，将偿还所有资产负债。
>   * 如果发送`amount`，则在有足够的特定还款资产的情况下，仅偿还指定`amount`的资产负债。
>   * 无论是否将需要偿还的负债资产放入`specifyRepayAssets`中，系统都会先使用相同的资产（如果有）来偿还负债
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt#响应示例 "响应示例的直接链接")
    
    
    {  
        "amount": "0.10000000",  
    	"asset": "BNB",  
        "specifyRepayAssets": [  
        "USDT",  
        "BTC"  
    	],  
        "updateTime": 1636371437000  
    	"success": true  
    }