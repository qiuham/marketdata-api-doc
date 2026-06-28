---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-public-single-leg-transactions-of-block-trades
anchor_id: block-trading-rest-api-get-public-single-leg-transactions-of-block-trades
api_type: REST
updated_at: 2026-06-28 19:37:35.063613
---

# Get public single-leg transactions of block trades

Retrieve the recent block trading transactions of an instrument. Descending order by tradeId. The data will be updated 15 minutes after the block trade execution.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/block-trades`

> Request Example
    
    
    GET /api/v5/public/block-trades?instId=BTC-USDT
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "fillVol": "5",
                "fwdPx": "26857.86591585",
                "groupId": "",
                "idxPx": "26889.7",
                "instId": "BTC-USD-231013-22000-P",
                "markPx": "0.0000000000000001",
                "px": "0.0026",
                "side": "buy",
                "sz": "1",
                "tradeId": "632960608383700997",
                "ts": "1697181568974"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
tradeId | String | Trade ID  
px | String | Trade price  
sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
side | String | Trade side   
`buy`   
`sell`  
fillVol | String | Implied volatility   
Only applicable to `OPTION`  
fwdPx | String | Forward price   
Only applicable to `OPTION`  
idxPx | String | Index price   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
markPx | String | Mark price   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
Up to 500 most recent historical public transaction data can be retrieved.  Group RFQ introduction  
  
1\. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.  
2\. Data return by this endpoint should be at **child RFQ execution level** but split into a single leg. tradeId will be populated.

---

# 获取大宗交易公共单腿成交数据

查询市场上交易产品维度的大宗交易公共成交数据，根据 tradeId 倒序排序。数据将在大宗交易执行15分钟后更新。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/block-trades`

> 请求示例
    
    
    GET /api/v5/public/block-trades?instId=BTC-USDT
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "fillVol": "5",
                "fwdPx": "26857.86591585",
                "groupId": "",
                "idxPx": "26889.7",
                "instId": "BTC-USD-231013-22000-P",
                "markPx": "0.0000000000000001",
                "px": "0.0026",
                "side": "buy",
                "sz": "1",
                "tradeId": "632960608383700997",
                "ts": "1697181568974"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
tradeId | String | 成交ID  
px | String | 成交价格  
sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
side | String | 成交方向   
`buy`：买   
`sell`：卖  
fillVol | String | 成交时的隐含波动率   
仅适用于 `期权`  
fwdPx | String | 成交时的远期价格   
仅适用于 `期权`  
idxPx | String | 成交时的指数价格   
适用于 `交割`, `永续`, `期权`  
markPx | String | 成交时的标记价格   
适用于 `交割`, `永续`, `期权`  
groupId | String | 组合询价单ID  
只适用于组合询价单，普通询价单返回 ""  
ts | String | 成交时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
最多获取最近500条历史公共成交数据  组合询价单介绍  
  
1\. 新增返回参数 groupId，协助用户将子账户执行映射到组合询价单。仅适用于组合询价单，对普通询价单返回 ""。  
2\. 该接口返回的交易数据应为子级询价单，但拆分为单腿，tradeId 有值