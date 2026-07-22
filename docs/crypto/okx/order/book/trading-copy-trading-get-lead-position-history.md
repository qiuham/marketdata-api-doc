---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-lead-position-history
anchor_id: order-book-trading-copy-trading-get-lead-position-history
api_type: API
updated_at: 2026-07-22 19:19:41.041003
---

# GET / Lead position history

Retrieve the completed lead position of the last 3 months.  
Returns reverse chronological order with `subPosId`.   
  
#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/subpositions-history`

> Request example
    
    
    GET /api/v5/copytrading/subpositions-history?instId=BTC-USDT-SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
It returns all types by default.  
instId | String | No | Instrument ID, e.g. BTC-USDT-SWAP  
after | String | No | Pagination of data to return records earlier than the requested `subPosId`.  
before | String | No | Pagination of data to return records newer than the requested `subPosId`.  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "closeAvgPx": "37617.5",
                "closeTime": "1701188587950",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "37.41",
                "markPx": "38203.4",
                "mgnMode": "isolated",
                "openAvgPx": "37410",
                "openOrdId": "",
                "openTime": "1701184638702",
                "pnl": "0.6225",
                "pnlRatio": "0.0166399358460306",
                "posSide": "net",
                "profitSharingAmt": "0.0407967",
                "subPos": "3",
                "closeSubPos": "2",
                "type": "1",
                "subPosId": "649750700213698561",
                "uniqueCode": "25CD5A80241D6FE6"
            },
            {
                "ccy": "USDT",
                "closeAvgPx": "37617.5",
                "closeTime": "1701188587950",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "24.94",
                "markPx": "38203.4",
                "mgnMode": "isolated",
                "openAvgPx": "37410",
                "openOrdId": "",
                "openTime": "1701184635381",
                "pnl": "0.415",
                "pnlRatio": "0.0166399358460306",
                "posSide": "net",
                "profitSharingAmt": "0.0271978",
                "subPos": "2",
                "closeSubPos": "2",
                "type": "2",
                "subPosId": "649750686292803585",
                "uniqueCode": "25CD5A80241D6FE6"
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
openOrdId | String | Order ID for opening position, only applicable to lead position  
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
markPx | String | Latest mark price, only applicable to contract  
uniqueCode | String | Lead trader unique code  
profitSharingAmt | String | Profit sharing amount, only applicable to copy trading. Note: this parameter is already deprecated.  
closeSubPos | String | Quantity of positions that is already closed  
type | String | The type of closing position  
`1`：Close position partially;  
`2`：Close all

---

# GET / 获取历史带单

获取最近三个月的已经平仓的带单仓位，按照`subPosId`倒序排序。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/subpositions-history`

> 请求示例
    
    
    GET /api/v5/copytrading/subpositions-history?instId=BTC-USDT-SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约  
默认返回所有业务线的信息  
instId | String | 否 | 产品ID ，如`BTC-USDT-SWAP`  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`subPosId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`subPosId`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "closeAvgPx": "37617.5",
                "closeTime": "1701188587950",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "37.41",
                "markPx": "38203.4",
                "mgnMode": "isolated",
                "openAvgPx": "37410",
                "openOrdId": "",
                "openTime": "1701184638702",
                "pnl": "0.6225",
                "pnlRatio": "0.0166399358460306",
                "posSide": "net",
                "profitSharingAmt": "0.0407967",
                "subPos": "3",
                "closeSubPos": "2",
                "type": "1",
                "subPosId": "649750700213698561",
                "uniqueCode": "25CD5A80241D6FE6"
            },
            {
                "ccy": "USDT",
                "closeAvgPx": "37617.5",
                "closeTime": "1701188587950",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "24.94",
                "markPx": "38203.4",
                "mgnMode": "isolated",
                "openAvgPx": "37410",
                "openOrdId": "",
                "openTime": "1701184635381",
                "pnl": "0.415",
                "pnlRatio": "0.0166399358460306",
                "posSide": "net",
                "profitSharingAmt": "0.0271978",
                "subPos": "2",
                "closeSubPos": "2",
                "type": "2",
                "subPosId": "649750686292803585",
                "uniqueCode": "25CD5A80241D6FE6"
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
openOrdId | String | 交易员开仓订单号，仅适用于带单仓位  
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
markPx | String | 最新标记价格，仅适用于合约  
uniqueCode | String | 交易员唯一标识代码  
profitSharingAmt | String | 跟单分润额，仅适用于跟单，已经废弃。  
closeSubPos | String | 已平仓量  
type | String | 平仓类型  
`1`：部分平仓;  
`2`：完全平仓;