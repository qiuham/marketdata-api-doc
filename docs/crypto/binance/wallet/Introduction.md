---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/Introduction
api_type: REST
updated_at: 2026-06-30 19:08:49.525038
---

# Get API Key Permission (USER_DATA)

## API Description[​](/docs/wallet/account/api-key-permission#api-description "Direct link to API Description")

Get API Key Permission

## HTTP Request[​](/docs/wallet/account/api-key-permission#http-request "Direct link to HTTP Request")

GET `/sapi/v1/account/apiRestrictions`

## Request Weight(IP)[​](/docs/wallet/account/api-key-permission#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/account/api-key-permission#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/account/api-key-permission#response-example "Direct link to Response Example")
    
    
    {  
        "ipRestrict": false,  
        "createTime": 1698645219000,  
        "enableReading": true,  
        "enableWithdrawals": false,              // This option allows you to withdraw via API. You must apply the IP Access Restriction filter in order to enable withdrawals  
        "enableInternalTransfer": false,         // This option authorizes this key to transfer funds between your master account and your sub account instantly  
        "enableMargin": false,                   // This option can be adjusted after the Cross Margin account transfer is completed  
        "enableFutures": false,                  // The Futures API cannot be used if the API key was created before the Futures account was opened, or if you have enabled portfolio margin.  
        "permitsUniversalTransfer": false,       // Authorizes this key to be used for a dedicated universal transfer API to transfer multiple supported currencies. Each business's own transfer API rights are not affected by this authorization  
        "enableVanillaOptions": false,           // Authorizes this key to Vanilla options trading  
        "enableFixApiTrade": false,              //   
        "enableFixReadOnly": true,  
        "enableSpotAndMarginTrading": false,     // Spot and margin trading  
        "enablePortfolioMarginTrading": true     // API Key created before your activate portfolio margin does not support portfolio margin API service  
    }

---

# 查询用户API Key权限(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/account/api-key-permission#接口描述 "接口描述的直接链接")

查询用户API Key权

## HTTP请求[​](/docs/zh-CN/wallet/account/api-key-permission#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/account/apiRestrictions`

## 请求权重(IP)[​](/docs/zh-CN/wallet/account/api-key-permission#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/account/api-key-permission#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/account/api-key-permission#响应示例 "响应示例的直接链接")
    
    
    {  
        "ipRestrict": false,                     // 是否限制ip访问  
        "createTime": 1623840271000,             // 创建时间  
        "enableReading": true,  
        "enableWithdrawals": false,              // 此选项允许通过此api提现。开启提现选项必须添加IP访问限制过滤器  
        "enableInternalTransfer": true,          // 此选项授权此密钥在您的母账户和子账户之间划转资金  
        "enableMargin": false,                   // 此选项在全仓账户完成划转后可编辑  
        "enableFutures": false,                  // 合约交易权限，需注意开通合约账户之前创建的API Key不支持合约API功能  
        "permitsUniversalTransfer": true,        // 授权该密钥可用于专用的万向划转接口，用以操作其支持的多种类型资金划转。各业务自身的划转接口使用权限，不受本授权影响  
        "enableVanillaOptions": false,           // 欧式期权交易权限  
        "enableFixApiTrade": false,              // FIX API交易权限  
        "enableFixReadOnly": true,               // FIX API读取权限  
        "enableSpotAndMarginTrading": false,     // 现货和杠杆交易权限  
        "enablePortfolioMarginTrading": true     // 统一账户交易权限  
    }