---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Income-History
api_type: Account
updated_at: 2026-01-15T23:45:03.153476
---

# Get UM Income History(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-UM-Income-History#api-description "Direct link to API Description")

Get UM Income History

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-UM-Income-History#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/income`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-UM-Income-History#request-weight "Direct link to Request Weight")

**30**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-UM-Income-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
incomeType| STRING| NO| TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE  
startTime| LONG| NO| Timestamp in ms to get funding from INCLUSIVE.  
endTime| LONG| NO| Timestamp in ms to get funding until INCLUSIVE.  
page| INT| NO|   
limit| INT| NO| Default 100; max 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If neither `startTime` nor `endTime` is sent, the recent 7-day data will be returned.
>   * If `incomeType` is not sent, all kinds of flow will be returned
>   * "trandId" is unique in the same incomeType for a user
>   * Income history only contains data for the last three months
> 


## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-UM-Income-History#response-example "Direct link to Response Example")
    
    
      
    [  
        {  
            "symbol": "",                   // trade symbol, if existing  
            "incomeType": "TRANSFER",   // income type  
            "income": "-0.37500000",  // income amount  
            "asset": "USDT",                // income asset  
            "info":"TRANSFER",          // extra information  
            "time": 1570608000000,        
            "tranId":"9689322392",      // transaction id  
            "tradeId":""                    // trade id, if existing  
        },  
        {  
            "symbol": "BTCUSDT",  
            "incomeType": "COMMISSION",   
            "income": "-0.01000000",  
            "asset": "USDT",  
            "info":"COMMISSION",  
            "time": 1570636800000,  
            "tranId":"9689322392",  
            "tradeId":"2059192"  
        }  
    ]

---

# 获取UM损益资金流水(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Income-History#接口描述 "接口描述的直接链接")

获取UM损益资金流水

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Income-History#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/income`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Income-History#请求权重 "请求权重的直接链接")

**30**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Income-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
incomeType| STRING| NO| TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
page| INT| NO| 分页数  
limit| INT| NO| 默认 100; 最大 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 如果`startTime` 和 `endTime` 均未发送, 只会返回最近7天的数据.
>   * 如果`incomeType`没有发送，返回所有类型账户损益资金流水。
>   * `trandId` 在相同用户的同一种收益流水类型中是唯一的。
>   * 仅保留最近3个月的数据。
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Income-History#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "",               // 交易对，仅针对涉及交易对的资金流  
            "incomeType": "TRANSFER",   // 资金流类型  
            "income": "-0.37500000",    // 资金流数量，正数代表流入，负数代表流出  
            "asset": "USDT",            // 资产内容  
            "info":"TRANSFER",          // 备注信息，取决于流水类型  
            "time": 1570608000000,        
            "tranId":"9689322392",      // 划转ID  
            "tradeId":""                // 引起流水产生的原始交易ID   
        },  
        {  
            "symbol": "BTCUSDT",  
            "incomeType": "COMMISSION",   
            "income": "-0.01000000",  
            "asset": "USDT",  
            "info":"COMMISSION",  
            "time": 1570636800000,  
            "tranId":"9689322392",  
            "tradeId":"2059192"  
        }  
    ]