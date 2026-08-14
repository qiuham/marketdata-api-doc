---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-place-grid-algo-order
anchor_id: order-book-trading-grid-trading-post-place-grid-algo-order
api_type: API
updated_at: 2026-08-14 19:10:59.869373
---

# POST / Place grid algo order

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID + Instrument ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/order-algo`

> Request Example
    
    
    # Place spot grid algo order
    POST /api/v5/tradingBot/grid/order-algo
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "grid",
        "maxPx": "5000",
        "minPx": "400",
        "gridNum": "10",
        "runType": "1",
        "quoteSz": "25",
        "triggerParams":[
          {
             "triggerAction":"stop",
             "triggerStrategy":"price",  
             "triggerPx":"1000"
          }
        ]
    }
    
    # Place contract grid algo order
    POST /api/v5/tradingBot/grid/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "algoOrdType": "contract_grid",
        "maxPx": "5000",
        "minPx": "400",
        "gridNum": "10",
        "runType": "1",
        "sz": "200", 
        "direction": "long",
        "lever": "2",
        "triggerParams":[
          {
             "triggerAction":"start", 
             "triggerStrategy":"rsi", 
             "timeframe":"30m",
             "thold":"10",
             "triggerCond":"cross",
             "timePeriod":"14"
          },
          {
             "triggerAction":"stop",
             "triggerStrategy":"price",
             "triggerPx":"1000",
             "stopType":"2"
          }
       ]
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
maxPx | String | Yes | Upper price of price range  
minPx | String | Yes | Lower price of price range  
gridNum | String | Yes | Grid quantity  
runType | String | No | Grid type  
`1`: Arithmetic, `2`: Geometric  
Default is Arithmetic  
tpTriggerPx | String | No | TP tigger price  
Applicable to `Spot grid`/`Contract grid`  
slTriggerPx | String | No | SL tigger price  
Applicable to `Spot grid`/`Contract grid`  
algoClOrdId | String | No | Client-supplied Algo ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag  
profitSharingRatio | String | No | Profit sharing ratio, it only supports these values  
`0`,`0.1`,`0.2`,`0.3`  
0.1 represents 10%  
triggerParams | Array of objects | No | Trigger Parameters  
Applicable to `Spot grid`/`Contract grid`  
> triggerAction | String | Yes | Trigger action  
`start`  
`stop`  
> triggerStrategy | String | Yes | Trigger strategy  
`instant`  
`price`  
`rsi`  
Default is `instant`  
> delaySeconds | String | No | Delay seconds after action triggered  
> timeframe | String | No | K-line type  
`3m`, `5m`, `15m`, `30m` (`m`: minute)  
`1H`, `4H` (`H`: hour)  
`1D` (`D`: day)  
This field is only valid when `triggerStrategy` is `rsi`  
> thold | String | No | Threshold  
The value should be an integer between 1 to 100  
This field is only valid when `triggerStrategy` is `rsi`  
> triggerCond | String | No | Trigger condition  
`cross_up`  
`cross_down`  
`above`  
`below`  
`cross`  
This field is only valid when `triggerStrategy` is `rsi`  
> timePeriod | String | No | Time Period  
`14`  
This field is only valid when `triggerStrategy` is `rsi`  
> triggerPx | String | No | Trigger Price  
This field is only valid when `triggerStrategy` is `price`  
> stopType | String | No | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
This field is only valid when `triggerAction` is `stop`  
  
Spot Grid Order

Parameter | Type | Required | Description  
---|---|---|---  
quoteSz | String | Conditional | Invest amount for quote currency  
Either `quoteSz` or `baseSz` is required  
baseSz | String | Conditional | Invest amount for base currency  
Either `quoteSz` or `baseSz` is required  
tradeQuoteCcy | String | No | The quote currency for trading. Only applicable to SPOT.  
The default value is the quote currency of instId, e.g. USD for BTC-USD.  
  
Contract Grid Order

Parameter | Type | Required | Description  
---|---|---|---  
sz | String | Yes | Used margin based on `USDT`  
direction | String | Yes | Contract grid type  
`long`,`short`,`neutral`  
lever | String | Yes | Leverage  
basePos | Boolean | No | Whether or not open a position when the strategy activates   
Default is `false`  
Neutral contract grid should omit the parameter  
tpRatio | String | No | Take profit ratio, 0.1 represents 10%  
slRatio | String | No | Stop loss ratio, 0.1 represents 10%  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "447053782921515008",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
tag | String | Order tag

---

# POST / 网格策略委托下单

#### 限速：20次/2s  
  
#### 限速规则：User ID + Instrument ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/order-algo`

> 请求示例
    
    
    # 现货网格下单
    POST /api/v5/tradingBot/grid/order-algo
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "grid",
        "maxPx": "5000",
        "minPx": "400",
        "gridNum": "10",
        "runType": "1",
        "quoteSz": "25",
        "triggerParams":[
          {
             "triggerAction":"stop",
             "triggerStrategy":"price",  
             "triggerPx":"1000"
          }
        ]
    }
    
    # 合约网格下单
    POST /api/v5/tradingBot/grid/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "algoOrdType": "contract_grid",
        "maxPx": "5000",
        "minPx": "400",
        "gridNum": "10",
        "runType": "1",
        "sz": "200", 
        "direction": "long",
        "lever": "2",
        "triggerParams":[
          {
             "triggerAction":"start", 
             "triggerStrategy":"rsi", 
             "timeframe":"30m",
             "thold":"10",
             "triggerCond":"cross",
             "timePeriod":"14"
          },
          {
             "triggerAction":"stop",
             "triggerStrategy":"price",
             "triggerPx":"1000",
             "stopType":"2"
          }
       ]
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USDT`  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
maxPx | String | 是 | 区间最高价格  
minPx | String | 是 | 区间最低价格  
gridNum | String | 是 | 网格数量  
runType | String | 否 | 网格类型  
`1`：等差，`2`：等比  
默认为等差  
tpTriggerPx | String | 否 | 止盈触发价  
适用于`现货网格`/`合约网格`  
slTriggerPx | String | 否 | 止损触发价  
适用于`现货网格`/`合约网格`  
algoClOrdId | String | 否 | 用户自定义策略ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
profitSharingRatio | String | 否 | 带单员分润比例，仅支持固定比例分润  
`0`,`0.1`,`0.2`,`0.3`  
triggerParams | Array of objects | 否 | 信号触发参数  
适用于`现货网格`/`合约网格`  
> triggerAction | String | 是 | 触发行为  
`start`：网格启动  
`stop`：网格停止  
> triggerStrategy | String | 是 | 触发策略  
`instant`：立即触发  
`price`：价格触发  
`rsi`：rsi指标触发  
默认为`instant`  
> delaySeconds | String | 否 | 延迟触发时间，单位为秒，默认为`0`  
> timeframe | String | 否 | K线种类  
`3m`, `5m`, `15m`, `30m` (`m`代表分钟)  
`1H`, `4H` (`H`代表小时)  
`1D` (`D`代表天)  
该字段只在`triggerStrategy`为`rsi`时有效  
> thold | String | 否 | 阈值  
取值[1,100]的整数  
该字段只在`triggerStrategy`为`rsi`时有效  
> triggerCond | String | 否 | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
该字段只在`triggerStrategy`为`rsi`时有效  
> timePeriod | String | 否 | 周期  
`14`  
该字段只在`triggerStrategy`为`rsi`下有效  
> triggerPx | String | 否 | 触发价格  
该字段只在`triggerStrategy`为`price`下有效  
> stopType | String | 否 | 策略停止类型  
现货 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：停止平仓，`2`：停止不平仓   
该字段只在`triggerAction`为`stop`时有效  
  
现货网格

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteSz | String | 可选 | 计价币投入数量  
`quoteSz`和`baseSz`至少指定一个  
baseSz | String | 可选 | 交易币投入数量  
`quoteSz`和`baseSz`至少指定一个  
tradeQuoteCcy | String | No | 用于交易的计价币种。仅适用于现货网格。  
默认值为 instId 的计价币种，例如 BTC-USD 的计价币种为 USD。  
  
合约网格

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sz | String | 是 | 投入保证金,单位为`USDT`  
direction | String | 是 | 合约网格类型  
`long`：做多，`short`：做空，`neutral`：中性  
lever | String | 是 | 杠杆倍数  
basePos | Boolean | 否 | 是否开底仓  
默认为`false`  
中性合约网格忽略该参数  
tpRatio | String | 否 | 止盈比率，0.1 代表 10%  
slRatio | String | 否 | 止损比率，0.1 代表 10%  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "447053782921515008",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | 订单标签