---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/portfolio-margin-endpoints
api_type: REST
updated_at: 2026-01-15T23:47:06.222305
---

# Classic Portfolio Margin Account Information (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/portfolio-margin-endpoints#api-description "Direct link to API Description")

Get Classic Portfolio Margin current account information.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/portfolio-margin-endpoints#http-request "Direct link to HTTP Request")

GET `/fapi/v1/pmAccountInfo`

## Request Weight[​](/docs/derivatives/usds-margined-futures/portfolio-margin-endpoints#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/portfolio-margin-endpoints#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * maxWithdrawAmount is for asset transfer out to the spot wallet.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/portfolio-margin-endpoints#response-example "Direct link to Response Example")
    
    
    {  
    	"maxWithdrawAmountUSD": "1627523.32459208",   // Classic Portfolio margin maximum virtual amount for transfer out in USD  
    	"asset": "BTC",            // asset name  
    	"maxWithdrawAmount": "27.43689636",        // maximum amount for transfer out  
    }

---

# Classic Portfolio Margin Account Information

## 查询经典统一账户账户信息 (USER_DATA)[​](/docs/zh-CN/derivatives/usds-margined-futures/portfolio-margin-endpoints#查询经典统一账户账户信息-user_data "查询经典统一账户账户信息 \(USER_DATA\)的直接链接")

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/portfolio-margin-endpoints#接口描述 "接口描述的直接链接")

查询经典统一账户当前账户信息

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/portfolio-margin-endpoints#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/pmAccountInfo`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/portfolio-margin-endpoints#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/portfolio-margin-endpoints#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 最大可转出余额指可以转出到现货钱包到金额。
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/portfolio-margin-endpoints#响应示例 "响应示例的直接链接")
    
    
    {  
        "maxWithdrawAmountUSD": "1627523.32459208",   //经典统一账户以USD计价的最大可转出余额  
        "asset": "BTC",            // 资产  
        "maxWithdrawAmount": "27.43689636",        //最大可转出余额  
    }