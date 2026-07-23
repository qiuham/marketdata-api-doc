---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-my-lead-traders
anchor_id: order-book-trading-copy-trading-get-my-lead-traders
api_type: API
updated_at: 2026-07-23 19:21:52.099256
---

# GET / My lead traders

Retrieve my lead traders.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/current-lead-traders`

> Request example
    
    
    GET /api/v5/copytrading/current-lead-traders?instType=SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "beginCopyTime": "1701224821936",
                "ccy": "USDT",
                "copyTotalAmt": "500",
                "copyTotalPnl": "0",
                "leadMode": "public",
                "margin": "1.89395",
                "nickName": "Trader9527",
                "portLink": "",
                "profitSharingRatio": "0.08",
                "todayPnl": "0",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
portLink | String | Portrait link  
nickName | String | Nick name  
margin | String | Margin for copy trading  
copyTotalAmt | String | Copy total amount  
copyTotalPnl | String | Copy total pnl  
uniqueCode | String | Lead trader unique code  
ccy | String | margin currency  
profitSharingRatio | String | Profit sharing ratio. 0.1 represents 10%  
beginCopyTime | String | Begin copying time. Unix timestamp format in milliseconds, e.g.1597026383085  
upl | String | Unrealized profit & loss  
todayPnl | String | Today pnl  
leadMode | String | Lead mode `public` `private`

---

# GET / 获取我的交易员

获取当前跟随的交易员  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/current-lead-traders`

> 请求示例
    
    
    GET /api/v5/copytrading/current-lead-traders?instType=SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "beginCopyTime": "1701224821936",
                "ccy": "USDT",
                "copyTotalAmt": "500",
                "copyTotalPnl": "0",
                "leadMode": "public",
                "margin": "1.89395",
                "nickName": "Trader9527",
                "portLink": "",
                "profitSharingRatio": "0.08",
                "todayPnl": "0",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
portLink | String | 头像  
nickName | String | 昵称  
margin | String | 跟单交易占用的保证金  
copyTotalAmt | String | 跟单员设置的跟单总金额  
copyTotalPnl | String | 跟单总收益 (USDT)  
uniqueCode | String | 带单员唯一标识代码  
ccy | String | 保证金币种  
profitSharingRatio | String | 分润比例，0.1 代表 10%  
beginCopyTime | String | 跟单开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
upl | String | 未实现盈亏  
todayPnl | String | 今日已实现收益  
leadMode | String | 带单模式  
`public`: 公开模式  
`private`: 私域模式