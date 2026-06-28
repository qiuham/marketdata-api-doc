---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints
api_type: REST
updated_at: 2026-01-15T23:39:24.493253
---

# Classic Portfolio Margin Account Information (USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#api-description "Direct link to API Description")

Get Classic Portfolio Margin current account information.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#http-request "Direct link to HTTP Request")

GET `/dapi/v1/pmAccountInfo`

## Request Weight(IP)[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#request-weightip "Direct link to Request Weight\(IP\)")

**5**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO|   
  
>   * maxWithdrawAmount is for asset transfer out to the spot wallet.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#response-example "Direct link to Response Example")
    
    
    {  
        "maxWithdrawAmountUSD": "25347.92083245",   // Classic Portfolio margin maximum virtual amount for transfer out in USD  
        "asset": "BTC",            // asset name  
        "maxWithdrawAmount": "1.33663654",        // maximum amount for transfer out  
    }

---

# 查询经典统一账户账户信息 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/portfolio-margin-endpoints#接口描述 "接口描述的直接链接")

查询经典统一账户当前账户信息

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/portfolio-margin-endpoints#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/pmAccountInfo`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/coin-margined-futures/portfolio-margin-endpoints#请求权重ip "请求权重\(IP\)的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/portfolio-margin-endpoints#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO|   
  
>   * 最大可转出余额指可以转出到现货钱包到金额。
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/portfolio-margin-endpoints#响应示例 "响应示例的直接链接")
    
    
    {  
        "maxWithdrawAmountUSD": "25347.92083245",   //统一账户以USD计价的最大可转出余额  
        "asset": "BTC",            // 资产  
        "maxWithdrawAmount": "1.33663654",        //最大可转出余额  
    }