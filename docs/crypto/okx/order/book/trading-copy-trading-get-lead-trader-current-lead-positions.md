---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-lead-trader-current-lead-positions
anchor_id: order-book-trading-copy-trading-get-lead-trader-current-lead-positions
api_type: API
updated_at: 2026-07-03 19:39:50.522413
---

# GET / Lead trader current lead positions

Public endpoint. Get current leading positions of lead trader  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/public-current-subpositions`

> Request example
    
    
    GET /api/v5/copytrading/public-current-subpositions?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

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
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "lever": "5",
                "margin": "16.23304",
                "markPx": "2027.31",
                "mgnMode": "isolated",
                "openAvgPx": "2029.13",
                "openTime": "1701144639417",
                "posSide": "short",
                "subPos": "4",
                "subPosId": "649582930998104064",
                "uniqueCode": "D9ADEAB33AE9EABD",
                "upl": "0.0728",
                "uplRatio": "0.0044846806266725"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
subPosId | String | Lead position ID  
posSide | String | Position side  
`long`   
`short`   
`net`  
(Long positions have positive subPos; short positions have negative subPos)  
mgnMode | String | Margin mode. `cross` `isolated`  
lever | String | Leverage  
openAvgPx | String | Average open price  
openTime | String | Open time  
subPos | String | Quantity of positions  
instType | String | Instrument type  
margin | String | Margin  
upl | String | Unrealized profit and loss  
uplRatio | String | Unrealized profit and loss ratio  
markPx | String | Latest mark price, only applicable to contract  
uniqueCode | String | Lead trader unique code  
ccy | String | Currency

---

# GET / 获取交易员当前带单

公共接口，获取交易员当前带单。  
  
  
#### 限速：5次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/public-current-subpositions`

> 请求示例
    
    
    GET /api/v5/copytrading/public-current-subpositions?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SWAP：永续合约，默认值  
uniqueCode | String | 是 | 交易员唯一标识码  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`subPosId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`subPosId`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "lever": "5",
                "margin": "16.23304",
                "markPx": "2027.31",
                "mgnMode": "isolated",
                "openAvgPx": "2029.13",
                "openTime": "1701144639417",
                "posSide": "short",
                "subPos": "4",
                "subPosId": "649582930998104064",
                "uniqueCode": "D9ADEAB33AE9EABD",
                "upl": "0.0728",
                "uplRatio": "0.0044846806266725"
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
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
margin | String | 保证金  
upl | String | 未实现收益  
uplRatio | String | 未实现收益率  
markPx | String | 最新标记价格，仅适用于合约  
uniqueCode | String | 交易员唯一标识代码  
ccy | String | 币种