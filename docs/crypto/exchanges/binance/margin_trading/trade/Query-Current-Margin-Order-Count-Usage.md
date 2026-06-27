---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Current-Margin-Order-Count-Usage
api_type: Trading
updated_at: 2026-05-27 18:57:42.652240
---

# Query Liquidation Loan (USER_DATA)

## Description[​](/docs/margin_trading/trade/Query-Liquidation-Loan#description "Direct link to Description")

Query the current user's cross-margin liquidation loan information, including the original loan amount, repaid amount, and remaining amount.

When a cross-margin account is liquidated and the account equity turns negative (i.e., bankruptcy occurs), the system automatically generates a liquidation loan record to represent the deficit. Use this endpoint to check the current status of any outstanding liquidation loan.

## HTTP Request[​](/docs/margin_trading/trade/Query-Liquidation-Loan#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/liquidation-loan`

## Request Weight[​](/docs/margin_trading/trade/Query-Liquidation-Loan#request-weight "Direct link to Request Weight")

**100(UID)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Liquidation-Loan#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Query-Liquidation-Loan#response-example "Direct link to Response Example")
    
    
    {  
        "asset": "USDC",  
        "amount": "1000.00000000",  
        "repaidAmount": "300.00000000",  
        "remainingAmount": "700.00000000"  
    }  
    

## Response Parameters[​](/docs/margin_trading/trade/Query-Liquidation-Loan#response-parameters "Direct link to Response Parameters")

Name| Type| Description  
---|---|---  
asset| STRING| The asset of the liquidation loan (USDC by default)  
amount| DECIMAL| Total liquidation loan amount  
repaidAmount| DECIMAL| Amount that has been repaid  
remainingAmount| DECIMAL| Outstanding amount remaining to be repaid

---

# 查询强平穿仓欠款 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan#接口描述 "接口描述的直接链接")

查询当前用户的全仓杠杆强平穿仓欠款信息，包括欠款总额、已还金额和剩余待偿还金额。

当用户的全仓杠杆账户触发强制平仓且发生穿仓时，系统会产生强平欠款记录（即穿仓导致的负债）。此接口允许用户查看尚未偿还的强平穿仓欠款余额。

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/liquidation-loan`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan#请求权重 "请求权重的直接链接")

**100(UID)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan#响应示例 "响应示例的直接链接")
    
    
    {  
        "asset": "USDC",  
        "amount": "1000.00000000",  
        "repaidAmount": "300.00000000",  
        "remainingAmount": "700.00000000"  
    }  
    

## 响应参数[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan#响应参数 "响应参数的直接链接")

名称| 类型| 描述  
---|---|---  
asset| STRING| 强平欠款资产（默认为USDC）  
amount| DECIMAL| 强平穿仓欠款总额  
repaidAmount| DECIMAL| 已偿还金额  
remainingAmount| DECIMAL| 剩余未偿还金额