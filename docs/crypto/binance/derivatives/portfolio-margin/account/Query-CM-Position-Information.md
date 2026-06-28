---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information
api_type: Account
updated_at: 2026-01-15T23:45:06.496205
---

# Query CM Position Information(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#api-description "Direct link to API Description")

Get current CM position information.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/positionRisk`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
marginAsset| STRING| NO|   
pair| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If neither `marginAsset` nor `pair` is sent, positions of all symbols with `TRADING` status will be returned.
>   * for One-way Mode user, the response will only show the "BOTH" positions
>   * for Hedge Mode user, the response will show "LONG", and "SHORT" positions.
> 


**Note**

>   * Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#response-example "Direct link to Response Example")

  * For One-way position mode:


    
    
    [  
        {  
            "symbol": "BTCUSD_201225",  
            "positionAmt": "1",  
            "entryPrice": "11707.70000003",  
            "markPrice": "11788.66626667",  
            "unRealizedProfit": "0.00005866",  
            "liquidationPrice": "6170.20509059",   
            "leverage": "125",  
            "positionSide": "LONG",  
            "updateTime": 1627026881327,  
            "maxQty": "50",  
            "notionalValue": "0.00084827"    
        }  
    ]  
    

>   * For Hedge position mode(only return with position):
> 

    
    
    [  
        {  
            "symbol": "BTCUSD_201225",  
            "positionAmt": "1",  
            "entryPrice": "11707.70000003",  
            "markPrice": "11788.66626667",  
            "unRealizedProfit": "0.00005866",  
            "liquidationPrice": "6170.20509059",   
            "leverage": "125",  
            "positionSide": "LONG",  
            "updateTime": 1627026881327,  
            "maxQty": "50",  
            "notionalValue": "0.00084827"   
        },  
        {  
            "symbol": "BTCUSD_201225",  
            "positionAmt": "1",  
            "entryPrice": "11707.70000003",  
            "markPrice": "11788.66626667",  
            "unRealizedProfit": "0.00005866",  
            "liquidationPrice": "6170.20509059",   
            "leverage": "125",  
            "positionSide": "LONG",  
            "updateTime": 1627026881327,  
            "maxQty": "50",  
            "notionalValue": "0.00084827"   
        }  
    ]

---

# 用户CM持仓风险(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-CM-Position-Information#接口描述 "接口描述的直接链接")

获取用户CM持仓风险

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-CM-Position-Information#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/positionRisk`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-CM-Position-Information#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-CM-Position-Information#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
marginAsset| STRING| NO|   
pair| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `marginAsset` 和 `pair` 不要同时提供
>   * `marginAsset` 和 `pair` 均不提供则返回所有上市状态和结算中的symbol
>   * 对于单向持仓模式，仅会展示`BOTH`方向的持仓
>   * 对于双向持仓模式，会展示所有`BOTH`，`LONG`，和`SHORT`方向的持仓
>   * 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-CM-Position-Information#响应示例 "响应示例的直接链接")

> 单向持仓模式下:
    
    
    [  
        {  
            "symbol": "BTCUSD_201225", // 交易对  
            "positionAmt": "0", // 头寸数量, 符号代表多空方向, 正数为多, 负数为空  
            "entryPrice": "0.0", // 开仓均价  
            "markPrice": "0.00000000", // 当前标记价格  
            "unRealizedProfit": "0.00000000", // 持仓未实现盈亏  
            "liquidationPrice": "6170.20509059", // 爆仓价  
            "leverage": "125", // 当前杠杆倍数  
            "positionSide": "BOTH", // 持仓方向  
            "updateTime": 0, // 最新更新时间  
            "maxQty": "50",  // 当前杠杆倍数允许的数量上限(标的数量)  
            "notionalValue": "0.00084827"  
        }  
    ]  
    

> 或双向持仓模式下(存在持仓才会返回):
    
    
    [  
        {  
            "symbol": "BTCUSD_201225",  
            "positionAmt": "1",  
            "entryPrice": "11707.70000003",  
            "markPrice": "11788.66626667",  
            "unRealizedProfit": "0.00005866",  
            "liquidationPrice": "6170.20509059", // 爆仓价  
            "leverage": "125",  
            "positionSide": "LONG",  
            "updateTime": 1627026881327,  
            "maxQty": "50",  
            "notionalValue": "0.00084827"   
        },  
        {  
            "symbol": "BTCUSD_201225",  
            "positionAmt": "1",  
            "entryPrice": "11707.70000003",  
            "markPrice": "11788.66626667",  
            "unRealizedProfit": "0.00005866",  
            "liquidationPrice": "6170.20509059", // 爆仓价  
            "leverage": "125",  
            "positionSide": "LONG",  
            "updateTime": 1627026881327,  
            "maxQty": "50",  
            "notionalValue": "0.00084827"   
        }  
    ]