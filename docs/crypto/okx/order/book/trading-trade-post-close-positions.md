---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-close-positions
anchor_id: order-book-trading-trade-post-close-positions
api_type: API
updated_at: 2026-07-23 19:21:11.688279
---

# POST / Close positions

Close the position of an instrument via a market order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### HTTP Request

`POST /api/v5/trade/close-position`

> Request Example
    
    
    POST /api/v5/trade/close-position
    body
    {
        "instId":"BTC-USDT-SWAP",
        "mgnMode":"cross"
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Close the position of an instrument via a market order
    result = tradeAPI.close_positions(
        instId="BTC-USDT-SWAP",
        mgnMode="cross"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID  
posSide | String | Conditional | Position side   
This parameter can be omitted in `net` mode, and the default value is `net`. You can only fill with `net`.  
This parameter must be filled in under the `long/short` mode. Fill in `long` for close-long and `short` for close-short.  
mgnMode | String | Yes | Margin mode  
`cross` `isolated`  
ccy | String | Conditional | Margin currency, required in the case of closing `cross` `MARGIN` position for `Futures mode`.  
autoCxl | Boolean | No | Whether any pending orders for closing out needs to be automatically canceled when close position via a market order.  
`false` or `true`, the default is `false`.  
clOrdId | String | No | Client-supplied ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "clOrdId": "",
                "instId": "BTC-USDT-SWAP",
                "posSide": "long",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
posSide | String | Position side  
clOrdId | String | Client-supplied ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
if there are any pending orders for closing out and the orders do not need to be automatically canceled, it will return an error code and message to prompt users to cancel pending orders before closing the positions.

---

# POST / 市价仓位全平

市价平掉指定交易产品的持仓  
  
#### 限速：20次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### HTTP请求

`POST /api/v5/trade/close-position`

> 请求示例
    
    
    POST /api/v5/trade/close-position
    body
    {
        "instId":"BTC-USDT-SWAP",
        "mgnMode":"cross"
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 市价全平
    result = tradeAPI.close_positions(
        instId="BTC-USDT-SWAP",
        mgnMode="cross"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID  
posSide | String | 可选 | 持仓方向   
买卖模式下：可不填写此参数，默认值net，如果填写，仅可以填写net  
开平仓模式下： 必须填写此参数，且仅可以填写 `long`：平多 ，`short`：平空  
mgnMode | String | 是 | 保证金模式  
`cross`：全仓 ； `isolated`：逐仓  
ccy | String | 可选 | 保证金币种，`合约模式`下的全仓币币杠杆平仓必填  
autoCxl | Boolean | 否 | 当市价全平时，平仓单是否需要自动撤销,默认为false.  
`false`：不自动撤单 `true`：自动撤单  
clOrdId | String | 否 | 客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "clOrdId": "",
                "instId": "BTC-USDT-SWAP",
                "posSide": "long",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
posSide | String | 持仓方向  
clOrdId | String | 客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
如果不自动撤单，那有任何平仓挂单的情况下，市价全平会返回错误码信息，提示用户先撤销平仓挂单