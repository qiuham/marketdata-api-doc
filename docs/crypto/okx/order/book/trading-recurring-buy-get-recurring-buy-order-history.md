---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-recurring-buy-get-recurring-buy-order-history
anchor_id: order-book-trading-recurring-buy-get-recurring-buy-order-history
api_type: API
updated_at: 2026-06-29 19:56:24.864096
---

# GET / Recurring buy order history

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/recurring/orders-algo-history`

> Request Example
    
    
    GET /api/v5/tradingBot/recurring/orders-algo-history
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | No | Algo ID  
after | String | No | Pagination of data to return records earlier than the requested `algoId`.  
before | String | No | Pagination of data to return records newer than the requested `algoId`.  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "644496098429767680",
                "algoOrdType": "recurring",
                "amt": "100",
                "cTime": "1699931844050",
                "cycles": "0",
                "instType": "SPOT",
                "investmentAmt": "0",
                "investmentCcy": "USDC",
                "mktCap": "0",
                "period": "hourly",
                "pnlRatio": "0",
                "recurringDay": "",
                "recurringHour": "1",
                "recurringList": [
                    {
                        "ccy": "BTC",
                        "ratio": "0.2",
                        "minPx": "",
                        "maxPx": ""
                    },
                    {
                        "ccy": "ETH",
                        "ratio": "0.8",
                        "minPx": "",
                        "maxPx": ""
                    }
                ],
                "recurringTime": "0",
                "state": "stopped",
                "stgyName": "stg1",
                "tag": "",
                "timeZone": "8",
                "totalAnnRate": "0",
                "totalPnl": "0",
                "uTime": "1699932177659",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
instType | String | Instrument type  
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
algoOrdType | String | Algo order type  
`recurring`: recurring buy  
state | String | Algo order state  
`stopped`  
stgyName | String | Custom name for trading bot, no more than 40 characters  
recurringList | Array of objects | Recurring buy info  
> ccy | String | Recurring currency, e.g. `BTC`  
> ratio | String | Proportion of recurring currency assets, e.g. "0.2" representing 20%  
> minPx | String | Minimum price of recurring currency. `""` means no limit  
> maxPx | String | Maximum price of recurring currency. `""` means no limit  
period | String | Period  
`monthly`  
`weekly`  
`daily`  
`hourly`  
recurringDay | String | Recurring buy date  
When the period is `monthly`, the value range is an integer of [1,28]  
When the period is `weekly`, the value range is an integer of [1,7]  
recurringHour | String | Recurring buy by hourly  
`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour"  
recurringTime | String | Recurring buy time, the value range is an integer of [0,23]  
timeZone | String | UTC time zone, the value range is an integer of [-12,14]  
e.g. "8" representing UTC+8 (East 8 District), Beijing Time  
amt | String | Quantity invested per cycle  
investmentAmt | String | Accumulate quantity invested  
investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC`  
totalPnl | String | Total P&L  
totalAnnRate | String | Total annualized rate of yield  
pnlRatio | String | Rate of yield  
mktCap | String | Market value in unit of `USDT`  
cycles | String | Accumulate recurring buy cycles  
tag | String | Order tag  
tradeQuoteCcy | String | The quote currency for trading.  
source | Array | Funding source  
`1`: Trading account  
`2`: Funding account  
`3`: Simple earn account  
recurringTimeType | String | Recurring buy time type  
`1`: Custom time  
`2`: Immediate trigger  
recurringTimeMinutes | String | Recurring buy time in minutes, integer of [0,59]

---

# GET / 获取历史定投策略委托单列表

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/recurring/orders-algo-history`

> 请求示例
    
    
    GET /api/v5/tradingBot/recurring/orders-algo-history
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 否 | 策略订单ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`algoId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`algoId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "644496098429767680",
                "algoOrdType": "recurring",
                "amt": "100",
                "cTime": "1699931844050",
                "cycles": "0",
                "instType": "SPOT",
                "investmentAmt": "0",
                "investmentCcy": "USDC",
                "mktCap": "0",
                "period": "hourly",
                "pnlRatio": "0",
                "recurringDay": "",
                "recurringHour": "1",
                "recurringList": [
                    {
                        "ccy": "BTC",
                        "ratio": "0.2",
                        "minPx": "",
                        "maxPx": ""
                    },
                    {
                        "ccy": "ETH",
                        "ratio": "0.8",
                        "minPx": "",
                        "maxPx": ""
                    }
                ],
                "recurringTime": "0",
                "state": "stopped",
                "stgyName": "stg1",
                "tag": "",
                "timeZone": "8",
                "totalAnnRate": "0",
                "totalPnl": "0",
                "uTime": "1699932177659",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义订单ID  
instType | String | 产品类型  
`SPOT`：现货  
cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
algoOrdType | String | 策略订单类型  
`recurring`：定投  
state | String | 订单状态  
`stopped`：已停止  
stgyName | String | 策略自定义名称，不超过40个字符  
recurringList | Array of objects | 定投信息  
> ccy | String | 定投币种，如 `BTC`  
> ratio | String | 定投币种资产占比，如 "0.2"代表占比20%  
> minPx | String | 定投币种价格下限，`""`代表没有限制  
> maxPx | String | 定投币种价格上限，`""`代表没有限制  
period | String | 周期类型  
`monthly`：月  
`weekly`：周  
`daily`：日  
`hourly`：小时  
recurringDay | String | 投资日  
当周期类型为`monthly`，则取值范围是 [1,28] 的整数  
当周期类型为`weekly`，则取值范围是 [1,7] 的整数  
recurringHour | String | 小时级别定投的间隔  
`1`/`4`/`8`/`12`  
如：`1`代表每隔`1`个小时定投  
recurringTime | String | 投资时间，取值范围是 [0,23] 的整数  
timeZone | String | 时区（UTC），取值范围是 [-12,14] 的整数  
如 `8`表示UTC+8（东8区），北京时间  
amt | String | 每期投入数量  
investmentAmt | String | 累计投入数量  
investmentCcy | String | 投入数量单位，只能是`USDT`/`USDC`  
totalPnl | String | 总收益  
totalAnnRate | String | 总年化  
pnlRatio | String | 收益率  
mktCap | String | 当前总市值，单位为`USDT`  
cycles | String | 定投累计轮数  
tag | String | 订单标签  
tradeQuoteCcy | String | 用于交易的计价币种。  
source | Array | 资金来源  
`1`：交易账户  
`2`：资金账户  
`3`：简单赚币账户  
recurringTimeType | String | 定投周期类型  
`1`：自定义时间  
`2`：立即触发  
recurringTimeMinutes | String | 定投时间（分钟），取值范围是 [0,59] 的整数