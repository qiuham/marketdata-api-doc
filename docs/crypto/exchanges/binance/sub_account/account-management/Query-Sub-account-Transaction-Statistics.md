---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/account-management/Query-Sub-account-Transaction-Statistics
api_type: Account
updated_at: 2026-05-27 19:02:04.379524
---

# Query Sub-account Transaction Statistics (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/account-management/Query-Sub-account-Transaction-Statistics#api-description "Direct link to API Description")

Query Sub-account Transaction statistics (For Master Account).

## HTTP Request[​](/docs/sub_account/account-management/Query-Sub-account-Transaction-Statistics#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/transaction-statistics`

## Request Weight[​](/docs/sub_account/account-management/Query-Sub-account-Transaction-Statistics#request-weight "Direct link to Request Weight")

**60**

## Request Parameters[​](/docs/sub_account/account-management/Query-Sub-account-Transaction-Statistics#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| NO| Sub user email  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/account-management/Query-Sub-account-Transaction-Statistics#response-example "Direct link to Response Example")
    
    
    {  
        "recent30BtcTotal": "0",  
        "recent30BtcFuturesTotal": "0",  
        "recent30BtcMarginTotal": "0",  
        "recent30BusdTotal": "0",  
        "recent30BusdFuturesTotal": "0",  
        "recent30BusdMarginTotal": "0",  
        "tradeInfoVos": []  
    }  
    

> OR
    
    
    {  
        "recent30BtcTotal": "0",  
        "recent30BtcFuturesTotal": "0",  
        "recent30BtcMarginTotal": "0",  
        "recent30BusdTotal": "0",  
        "recent30BusdFuturesTotal": "0",  
        "recent30BusdMarginTotal": "0",  
        "tradeInfoVos": [  
            {  
                "userId": 1000138138384,  
                "btc": 0,  
                "btcFutures": 0,  
                "btcMargin": 0,  
                "busd": 0,  
                "busdFutures": 0,  
                "busdMargin": 0,  
                "date": 1676851200000  
            },  
            {  
                "userId": 1000138138384,  
                "btc": 0,  
                "btcFutures": 0,  
                "btcMargin": 0,  
                "busd": 0,  
                "busdFutures": 0,  
                "busdMargin": 0,  
                "date": 1677110400000  
            },  
            {  
                "userId": 1000138138384,  
                "btc": 0,  
                "btcFutures": 0,  
                "btcMargin": 0,  
                "busd": 0,  
                "busdFutures": 0,  
                "busdMargin": 0,  
                "date": 1677369600000  
            }  
        ]  
    }

---

# 查询子账户交易量统计列表 (适用母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-Transaction-Statistics#接口描述 "接口描述的直接链接")

查询子账户交易量统计列表 (适用母账户)

## HTTP请求[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-Transaction-Statistics#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/transaction-statistics`

## 请求权重(UID)[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-Transaction-Statistics#请求权重uid "请求权重\(UID\)的直接链接")

**60**

## 请求参数[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-Transaction-Statistics#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| NO| 子账户邮箱  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-Transaction-Statistics#响应示例 "响应示例的直接链接")
    
    
    {  
        "recent30BtcTotal": "0",  
        "recent30BtcFuturesTotal": "0",  
        "recent30BtcMarginTotal": "0",  
        "recent30BusdTotal": "0",  
        "recent30BusdFuturesTotal": "0",  
        "recent30BusdMarginTotal": "0",  
        "tradeInfoVos": []  
    }  
    

> OR
    
    
    {  
        "recent30BtcTotal": "0",  
        "recent30BtcFuturesTotal": "0",  
        "recent30BtcMarginTotal": "0",  
        "recent30BusdTotal": "0",  
        "recent30BusdFuturesTotal": "0",  
        "recent30BusdMarginTotal": "0",  
        "tradeInfoVos": [  
            {  
                "userId": 1000138138384,  
                "btc": 0,  
                "btcFutures": 0,  
                "btcMargin": 0,  
                "busd": 0,  
                "busdFutures": 0,  
                "busdMargin": 0,  
                "date": 1676851200000  
            },  
            {  
                "userId": 1000138138384,  
                "btc": 0,  
                "btcFutures": 0,  
                "btcMargin": 0,  
                "busd": 0,  
                "busdFutures": 0,  
                "busdMargin": 0,  
                "date": 1676937600000  
            },  
            {  
                "userId": 1000138138384,  
                "btc": 0,  
                "btcFutures": 0,  
                "btcMargin": 0,  
                "busd": 0,  
                "busdFutures": 0,  
                "busdMargin": 0,  
                "date": 1677024000000  
            }  
        ]  
    }