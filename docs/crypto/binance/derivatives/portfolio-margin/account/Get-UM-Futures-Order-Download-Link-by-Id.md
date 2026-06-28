---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id
api_type: Account
updated_at: 2026-01-15T23:44:58.799744
---

# Get UM Futures Order Download Link by Id(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#api-description "Direct link to API Description")

Get UM futures order download link by Id

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/order/asyn/id`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#request-weight "Direct link to Request Weight")

**10**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
downloadId| STRING| YES| get by download id api  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Download link expiration: 24h
> 


## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#response-example "Direct link to Response Example")

> **Response:**
    
    
    {  
    	"downloadId":"545923594199212032",  
      	"status":"completed",     // Enum：completed，processing  
      	"url":"www.binance.com",  // The link is mapped to download id  
    	"s3Link": null,  
      	"notified":true,          // ignore  
      	"expirationTimestamp":1645009771000,  // The link would expire after this timestamp  
      	"isExpired":null,  
    }  
    

> **OR** (Response when server is processing)
    
    
    {  
    	"downloadId":"545923594199212032",  
      	"status":"processing",  
      	"url":"",   
    	"s3Link": null,  
      	"notified":false,  
      	"expirationTimestamp":-1  
      	"isExpired":null,  
      	  
    }

---

# 通过下载Id获取UM合约订单历史下载链接 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#接口描述 "接口描述的直接链接")

通过下载Id获取UM合约订单历史下载链接

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/order/asyn/id`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#请求权重 "请求权重的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
downloadId| STRING| YES| 通过下载id 接口获取  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 下载链接有效期：24小时。
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#响应示例 "响应示例的直接链接")

> **响应:**
    
    
    {  
    	"downloadId":"545923594199212032", // 下载Id  
      	"status":"completed",     // 状态，枚举类型：completed 已完成，processing 处理中  
      	"url":"www.binance.com",  // 适配该笔ID请求的下载链接   
        "s3Link": null,        
      	"notified":true,          // 忽略  
      	"expirationTimestamp":1645009771000,  // 晚于该时间戳之后链接将自动失效  
      	"isExpired":null,  
    }  
    

> **或** (服务器仍在处理中会返回)
    
    
    {  
    	"downloadId":"545923594199212032",  
      	"status":"processing",  
      	"url":"",   
        "s3Link": null,  
      	"notified":false,  
      	"expirationTimestamp":-1  
      	"isExpired":null, 	  
    }