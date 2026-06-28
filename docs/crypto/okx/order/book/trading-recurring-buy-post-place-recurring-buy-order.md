---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-recurring-buy-post-place-recurring-buy-order
anchor_id: order-book-trading-recurring-buy-post-place-recurring-buy-order
api_type: API
updated_at: 2026-06-28 19:37:04.968752
---

# POST / Place recurring buy order

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/order-algo
    body
    {
      "stgyName": "BTC|ETH recurring buy monthly",     
      "amt":"100",
      "recurringList":[    
        {
             "ccy":"BTC",
             "ratio":"0.2"
        },
        {
             "ccy":"ETH",
             "ratio":"0.8"
        }
      ],
      "period":"monthly",
      "recurringDay":"1",
      "recurringTime":"0",
      "timeZone":"8",   // UTC +8
      "tdMode":"cross",
      "investmentCcy":"USDT"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
stgyName | String | Yes | Custom name for trading bot, no more than 40 characters  
recurringList | Array of objects | Yes | Recurring buy info  
> ccy | String | Yes | Recurring currency, e.g. `BTC`  
> ratio | String | Yes | Proportion of recurring currency assets, e.g. "0.2" representing 20%  
> minPx | String | No | Minimum price of recurring currency. `""` means no limit  
> maxPx | String | No | Maximum price of recurring currency. `""` means no limit  
period | String | Yes | Period  
`monthly`  
`weekly`  
`daily`  
`hourly`  
recurringDay | String | Conditional | Recurring buy date  
When the period is `monthly`, the value range is an integer of [1,28]  
When the period is `weekly`, the value range is an integer of [1,7]  
When the period is `daily`/`hourly`, the parameter is not required.  
recurringHour | String | Conditional | Recurring buy by hourly  
`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour"  
When the period is `hourly`, the parameter is required.  
recurringTime | String | Yes | Recurring buy time, the value range is an integer of [0,23]  
When the period is `hourly`, the parameter is the time of the first investment occurs.  
timeZone | String | Yes | UTC time zone, the value range is an integer of [-12,14]  
e.g. "8" representing UTC+8 (East 8 District), Beijing Time  
amt | String | Yes | Quantity invested per cycle  
investmentCcy | String | Yes | The invested quantity unit, can only be `USDT`/`USDC`  
tdMode | String | Yes | Trading mode  
Margin mode: `cross`  
Non-Margin mode: `cash`  
algoClOrdId | String | No | Client-supplied Algo ID  
There will be a value when algo order attaching algoClOrdId is triggered, or it will be "".  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
tradeQuoteCcy | String | No | The quote currency for trading.  
source | Array | No | Funding source  
`1`: Trading account  
`2`: Funding account  
`3`: Simple earn account  
Default is `1`  
recurringTimeType | String | No | Recurring buy time type  
`1`: Custom time  
`2`: Immediate trigger  
Default is `1`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"560472804207104000",
                "algoClOrdId":"",
                "sCode":"0",
                "sMsg":"",
                "tag":""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful  
tag | String | Order tag

---

# POST / 定投策略委托下单

#### 限速：20次/2s  
  
#### 限速规则 ：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/recurring/order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/order-algo
    body
    {
      "stgyName": "BTC|ETH recurring buy monthly",     
      "amt":"100",
      "recurringList":[    
        {
             "ccy":"BTC",
             "ratio":"0.2"
        },
        {
             "ccy":"ETH",
             "ratio":"0.8"
        }
      ],
      "period":"monthly",
      "recurringDay":"1",
      "recurringTime":"0",
      "timeZone":"8",   // 东8区
      "tdMode":"cross",
      "investmentCcy":"USDT"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
stgyName | String | 是 | 策略自定义名称，不超过40个字符  
recurringList | Array of objects | 是 | 定投信息  
> ccy | String | 是 | 定投币种，如 `BTC`  
> ratio | String | 是 | 定投币种资产占比，如 "0.2"代表占比20%  
> minPx | String | 否 | 定投币种价格下限，`""`代表没有限制  
> maxPx | String | 否 | 定投币种价格上限，`""`代表没有限制  
period | String | 是 | 周期类型  
`monthly`：月  
`weekly`：周  
`daily`：日  
`hourly`：小时  
recurringDay | String | 可选 | 投资日  
当周期类型为`monthly`，则取值范围是 [1,28] 的整数  
当周期类型为`weekly`，则取值范围是 [1,7] 的整数  
当周期类型为`daily`/`hourly`，该参数可不填。  
recurringHour | String | 可选 | 小时级别定投的间隔  
`1`/`4`/`8`/`12`  
如：`1`代表每隔`1`个小时定投  
当周期类型选择`hourly`，该字段必填。  
recurringTime | String | 是 | 投资时间，取值范围是 [0,23] 的整数  
当周期类型选择`hourly`代表首次定投发生的时间  
timeZone | String | 是 | 时区（UTC），取值范围是 [-12,14] 的整数  
如 `8`表示UTC+8（东8区），北京时间  
amt | String | 是 | 每期投入数量  
investmentCcy | String | 是 | 投入数量单位，只能是`USDT`/`USDC`  
tdMode | String | 是 | 交易模式  
`跨币种保证金模式`/`组合保证金模式`下选择 `cross`：全仓  
`现货模式`/`合约模式`下选择 `cash`：非保证金  
algoClOrdId | String | 否 | 客户自定义订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。  
source | Array | 否 | 资金来源  
`1`：交易账户  
`2`：资金账户  
`3`：简单赚币账户  
默认为`1`  
recurringTimeType | String | 否 | 定投周期类型  
`1`：自定义时间  
`2`：立即触发  
默认为`1`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"560472804207104000",
                "algoClOrdId":"",
                "sCode":"0",
                "sMsg":"",
                "tag":""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义订单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | 订单标签