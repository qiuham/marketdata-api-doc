---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-lead-trader-lead-position-history
anchor_id: order-book-trading-copy-trading-get-lead-trader-lead-position-history
api_type: API
updated_at: 2026-07-21 19:26:18.953678
---

# GET / Lead trader lead position history

Public endpoint. Retrieve the lead trader completed leading position of the last 3 months.  
Returns reverse chronological order with `subPosId`.   
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-subpositions-history`

> Request example
    
    
    GET /api/v5/copytrading/public-subpositions-history?instType=SWAP&uniqueCode=9A8534AB09862774
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value.  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
after | String | No | Pagination of data to return records earlier than the requested `subPosId`.  
before | String | No | Pagination of data to return records newer than the requested `subPosId`.  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "closeAvgPx": "28385.9",
                "closeTime": "1697709137162",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "20",
                "margin": "4.245285",
                "mgnMode": "isolated",
                "openAvgPx": "28301.9",
                "openTime": "1697698048031",
                "pnl": "0.252",
                "pnlRatio": "0.05935997229868",
                "posSide": "long",
                "subPos": "3",
                "subPosId": "635126416883355648",
                "uniqueCode": "9A8534AB09862774"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
subPosId | String | Lead position ID  
posSide | String | Position side  
`long`   
`short`   
`net`  
(long position has positive subPos; short position has negative subPos)  
mgnMode | String | Margin mode. `cross` `isolated`  
lever | String | Leverage  
openAvgPx | String | Average open price  
openTime | String | Time of opening  
subPos | String | Quantity of positions  
closeTime | String | Time of closing position  
closeAvgPx | String | Average price of closing position  
pnl | String | Profit and loss  
pnlRatio | String | P&L ratio  
instType | String | Instrument type  
margin | String | Margin  
ccy | String | Currency  
uniqueCode | String | Lead trader unique code

---

# GET / 获取交易员历史带单

公共接口，获取交易员最近三个月的已经平仓的带单仓位，按照`subPosId`倒序排序。  
  
#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-subpositions-history`

> 请求示例
    
    
    GET /api/v5/copytrading/public-subpositions-history?instType=SWAP&uniqueCode=9A8534AB09862774
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SWAP：永续合约，默认值  
uniqueCode | String | 是 | 交易员唯一标识码  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`subPosId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`subPosId`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "closeAvgPx": "28385.9",
                "closeTime": "1697709137162",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "20",
                "margin": "4.245285",
                "mgnMode": "isolated",
                "openAvgPx": "28301.9",
                "openTime": "1697698048031",
                "pnl": "0.252",
                "pnlRatio": "0.05935997229868",
                "posSide": "long",
                "subPos": "3",
                "subPosId": "635126416883355648",
                "uniqueCode": "9A8534AB09862774"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
subPosId | String | 带单仓位ID  
posSide | String | 持仓方向  
long：开平仓模式开多   
short：开平仓模式开空   
net：买卖模式（subPos为正代表开多，subPos为负代表开空）  
mgnMode | String | 保证金模式，`isolated`：逐仓 ；`cross`：全仓  
lever | String | 杠杆倍数  
openAvgPx | String | 开仓均价  
openTime | String | 开仓时间  
subPos | String | 持仓张数  
closeTime | String | 平仓时间(最近一次平仓的时间)  
closeAvgPx | String | 平仓均价  
pnl | String | 收益额  
pnlRatio | String | 收益率  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
margin | String | 保证金  
ccy | String | 币种  
uniqueCode | String | 交易员唯一标识代码