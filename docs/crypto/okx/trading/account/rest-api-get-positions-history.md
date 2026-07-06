---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-positions-history
anchor_id: trading-account-rest-api-get-positions-history
api_type: REST
updated_at: 2026-07-06 19:52:17.241955
---

# Get positions history

Retrieve the updated position data for the last 3 months. Return in reverse chronological order using utime. Getting positions history is supported under Portfolio margin mode since **04:00 AM (UTC) on November 11, 2024**.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/positions-history`

> Request Example
    
    
    GET /api/v5/account/positions-history
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get positions history
    result = accountAPI.get_positions_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | No | Instrument ID, e.g. `BTC-USD-SWAP`  
mgnMode | String | No | Margin mode  
`cross` `isolated`  
type | String | No | The type of latest close position  
`1`: Close position partially;`2`：Close all;`3`：Liquidation;`4`：Partial liquidation; `5`：ADL - position not fully closed; `6`：ADL - position fully closed  
It is the latest type if there are several types for the same position.  
posId | String | No | Position ID. There is attribute expiration. The posId will be expired if it is more than 30 days after the last full close position, then position will use new posId.  
after | String | No | Pagination of data to return records earlier than the requested `uTime`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `uTime`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100. All records that have the same `uTime` will be returned at the current request  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "cTime": "1654177169995",
                "ccy": "BTC",
                "closeAvgPx": "29786.5999999789081085",
                "closeTotalPos": "1",
                "instId": "BTC-USD-SWAP",
                "instType": "SWAP",
                "lever": "10.0",
                "mgnMode": "cross",
                "openAvgPx": "29783.8999999995535393",
                "openMaxPos": "1",
                "realizedPnl": "0.001",
                "fee": "-0.0001",
                "fundingFee": "0",
                "liqPenalty": "0",
                "pnl": "0.0011",
                "pnlRatio": "0.000906447858888",
                "posId": "452587086133239818",
                "posSide": "long",
                "direction": "long",
                "triggerPx": "",
                "type": "1",
                "uTime": "1654177174419",
                "uly": "BTC-USD",
                "nonSettleAvgPx":"",
                "settledPnl":""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
instType | String | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | Instrument ID  
mgnMode | String | Margin mode  
`cross` `isolated`  
type | String | The type of latest close position  
`1`：Close position partially;`2`：Close all;`3`：Liquidation;`4`：Partial liquidation; `5`：ADL;   
It is the latest type if there are several types for the same position.  
cTime | String | Created time of position  
uTime | String | Updated time of position  
openAvgPx | String | Average price of opening position  
Under cross-margin mode, the entry price of expiry futures will update at settlement to the last settlement price, and when the position is opened or increased.  
nonSettleAvgPx | String | Non-settlement entry price  
The non-settlement entry price only reflects the average price at which the position is opened or increased.  
Only applicable to `cross` `FUTURES`  
closeAvgPx | String | Average price of closing position  
posId | String | Position ID  
openMaxPos | String | Max quantity of position  
closeTotalPos | String | Position's cumulative closed volume  
realizedPnl | String | Realized profit and loss  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
`realizedPnl`=`pnl`+`fee`+`fundingFee`+`liqPenalty`+`settledPnl`  
settledPnl | String | Accumulated settled profit and loss (calculated by settlement price)  
Only applicable to `cross` `FUTURES`  
pnlRatio | String | Realized P&L ratio  
fee | String | Accumulated fee  
Negative number represents the user transaction fee charged by the platform.Positive number represents rebate.  
fundingFee | String | Accumulated funding fee  
liqPenalty | String | Accumulated liquidation penalty. It is negative when there is a value.  
pnl | String | Profit and loss (excluding the fee).  
posSide | String | Position mode side  
`long`: Hedge mode long  
`short`: Hedge mode short  
`net`: Net mode  
lever | String | Leverage  
direction | String | Direction: `long` `short`  
Only applicable to `MARGIN/FUTURES/SWAP/OPTION`  
triggerPx | String | trigger mark price. There is value when `type` is equal to `3`, `4` or `5`. It is "" when `type` is equal to `1` or `2`  
uly | String | Underlying  
ccy | String | Currency used for margin

---

# 查看历史持仓信息

获取最近3个月有更新的仓位信息，按照仓位更新时间倒序排列。于**2024年11月11日中午12:00（UTC+8）** 开始支持组合保证金账户模式下的历史持仓。

#### 限速：10次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/positions-history`

> 请求示例
    
    
    GET /api/v5/account/positions-history
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看历史持仓信息
    result = accountAPI.get_positions_history()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 否 | 交易产品ID，如：`BTC-USD-SWAP`  
mgnMode | String | 否 | 保证金模式  
`cross`：全仓，`isolated`：逐仓  
type | String | 否 | 最近一次平仓的类型  
`1`：部分平仓;`2`：完全平仓;`3`：强平;`4`：强减; `5`：ADL自动减仓 - 仓位未完全平仓; `6`：ADL自动减仓 - 仓位完全平仓  
状态叠加时，以最新的平仓类型为准状态为准。  
posId | String | 否 | 持仓ID。存在有效期的属性，自最近一次完全平仓算起，满30天 posId 会失效，之后的仓位，会使用新的 posId。  
after | String | 否 | 查询仓位更新 (uTime) 之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询仓位更新 (uTime) 之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回结果的数量，最大为100，默认100条，uTime 相同的记录均会在当前请求中全部返回  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "cTime": "1654177169995",
                "ccy": "BTC",
                "closeAvgPx": "29786.5999999789081085",
                "closeTotalPos": "1",
                "instId": "BTC-USD-SWAP",
                "instType": "SWAP",
                "lever": "10.0",
                "mgnMode": "cross",
                "openAvgPx": "29783.8999999995535393",
                "openMaxPos": "1",
                "realizedPnl": "0.001",
                "fee": "-0.0001",
                "fundingFee": "0",
                "liqPenalty": "0",
                "pnl": "0.0011",
                "pnlRatio": "0.000906447858888",
                "posId": "452587086133239818",
                "posSide": "long",
                "direction": "long",
                "triggerPx": "",
                "type": "1",
                "uTime": "1654177174419",
                "uly": "BTC-USD",
                "nonSettleAvgPx":"",
                "settledPnl":""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instType | String | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 交易产品ID  
mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
type | String | 最近一次平仓的类型  
`1`：部分平仓  
`2`：完全平仓  
`3`：强平  
`4`：强减  
`5`：ADL自动减仓  
状态叠加时，以最新的平仓类型为准状态为准。  
cTime | String | 仓位创建时间  
uTime | String | 仓位更新时间  
openAvgPx | String | 开仓均价  
会随结算周期变化，特别是在交割合约全仓模式下，结算时开仓均价会更新为结算价格，同时新增头寸也会改变开仓均价。  
nonSettleAvgPx | String | 未结算均价  
不受结算影响的加权开仓价格，仅在新增头寸时更新，和开仓均价的主要区别在于是否受到结算影响。  
仅适用于`全仓``交割`  
closeAvgPx | String | 平仓均价  
posId | String | 仓位ID  
openMaxPos | String | 最大持仓量  
closeTotalPos | String | 累计平仓量  
realizedPnl | String | 已实现收益  
仅适用于`交割`/`永续`/`期权`  
`realizedPnl`=`pnl`+`fee`+`fundingFee`+`liqPenalty`+`settledPnl`  
settledPnl | String | 已实现收益  
仅适用于`全仓``交割`  
pnlRatio | String | 已实现收益率  
fee | String | 累计手续费金额  
正数代表平台返佣，负数代表平台扣除。  
fundingFee | String | 累计资金费用  
liqPenalty | String | 累计爆仓罚金，有值时为负数。  
pnl | String | 已实现收益(不包括手续费)  
posSide | String | 持仓模式方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
lever | String | 杠杆倍数  
direction | String | 持仓方向  
`long`：多  
`short`：空  
仅适用于 `杠杆`/`交割`/`永续`/`期权`  
triggerPx | String | 触发标记价格  
`type` 为`3`,`4`,`5`时有值；为`1`, `2` 时为空  
uly | String | 标的指数  
ccy | String | 占用保证金的币种