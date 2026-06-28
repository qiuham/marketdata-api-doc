---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-copy-traders
anchor_id: order-book-trading-copy-trading-get-copy-traders
api_type: API
updated_at: 2026-05-27 19:35:31.061586
---

# GET / Copy traders

Public endpoint. Retrieve copy trader coming from certain lead trader. Return according to `pnl` from high to low  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/public-copy-traders`

> Request example
    
    
    GET /api/v5/copytrading/public-copy-traders?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "copyTotalPnl": "2060.12242",
                "copyTraderNumChg": "1",
                "copyTraderNumChgRatio": "0.5",
                "copyTraders": [
                    {
                        "beginCopyTime": "1686125051000",
                        "nickName": "bre***@gmail.com",
                        "pnl": "1076.77388",
                        "portLink": ""
                    },
                    {
                        "beginCopyTime": "1698133811000",
                        "nickName": "MrYanDao505",
                        "pnl": "983.34854",
                        "portLink": "https://static.okx.com/cdn/okex/users/headimages/20231010/fd31f45e99fe41f7bb219c0b53ae0ada"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
copyTotalPnl | String | Total copy trader profit and loss  
ccy | String | The currency name of profit and loss  
copyTraderNumChg | String | Number change in last 7 days  
copyTraderNumChgRatio | String | Ratio change in last 7 days  
copyTraders | Array of objects | Copy trader information  
> beginCopyTime | String | Begin copying time. Unix timestamp format in milliseconds, e.g.1597026383085  
> nickName | String | Nick name  
> portLink | String | Copy trader portrait link  
> pnl | String | Copy trading profit and loss

---

# GET / 获取跟单人信息

公共接口，获取交易员的跟单人信息，按收益从高到低返回  
  
#### 限速：5次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/public-copy-traders`

> 请求示例
    
    
    GET /api/v5/copytrading/public-copy-traders?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "copyTotalPnl": "2060.12242",
                "copyTraderNumChg": "1",
                "copyTraderNumChgRatio": "0.5",
                "copyTraders": [
                    {
                        "beginCopyTime": "1686125051000",
                        "nickName": "bre***@gmail.com",
                        "pnl": "1076.77388",
                        "portLink": ""
                    },
                    {
                        "beginCopyTime": "1698133811000",
                        "nickName": "MrYanDao505",
                        "pnl": "983.34854",
                        "portLink": "https://static.okx.com/cdn/okex/users/headimages/20231010/fd31f45e99fe41f7bb219c0b53ae0ada"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
copyTotalPnl | String | 跟单员总收益  
ccy | String | 总收益币种名称  
copyTraderNumChg | String | 近 7 日变化的跟单人数  
copyTraderNumChgRatio | String | 近 7 日跟单人数变化的比率  
copyTraders | Array of objects | 跟单员信息  
> beginCopyTime | String | 跟单开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> nickName | String | 昵称  
> portLink | String | 跟单员头像的链接地址  
> pnl | String | 跟单收益