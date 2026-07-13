---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-maximum-order-quantity
anchor_id: trading-account-rest-api-get-maximum-order-quantity
api_type: REST
updated_at: 2026-07-13 19:27:04.333526
---

# Get maximum order quantity

The maximum quantity to buy or sell. It corresponds to the "sz" from placement.

Under the Portfolio Margin account, the calculation of the maximum buy/sell amount or open amount is not supported under the cross mode of derivatives. 

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/max-size`

> Request Example
    
    
    GET /api/v5/account/max-size?instId=BTC-USDT&tdMode=isolated
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get maximum buy/sell amount or open amount
    result = accountAPI.get_max_order_size(
        instId="BTC-USDT",
        tdMode="isolated"
    )
    print(result)
    

#### Request Parameters

**Parameter** | **Type** | Required | Description  
---|---|---|---  
instId | String | Yes | Single instrument or multiple instruments (no more than 5) in the same instrument type separated with comma, e.g. `BTC-USDT,ETH-USDT`  
tdMode | String | Yes | Trade mode  
`cross`  
`isolated`  
`cash`  
`spot_isolated`: only applicable to `Futures mode`.  
ccy | String | Conditional | Currency used for margin   
Applicable to `isolated` `MARGIN` and `cross` `MARGIN` orders in `Futures mode`.  
px | String | No | Price  
When the price is not specified, it will be calculated according to the current limit price for `FUTURES` and `SWAP`, the last traded price for other instrument types.  
The parameter will be ignored when multiple instruments are specified.  
leverage | String | No | Leverage for instrument  
The default is current leverage  
Only applicable to `MARGIN/FUTURES/SWAP`  
tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`.   
The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`.  
outcome | String | No | Market outcome to trade on.  
`yes`  
`no`  
Only applicable and optional for `EVENTS`, the default value is `yes`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "instId": "BTC-USDT",
            "maxBuy": "0.0500695098559788",
            "maxSell": "64.4798671570072269"
      }]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
ccy | String | Currency used for margin  
maxBuy | String | `SPOT`/`MARGIN`: The maximum quantity in base currency that you can buy  
The cross-margin order under `Futures mode` mode, quantity of coins is based on base currency.  
`FUTURES`/`SWAP`/`OPTIONS`: The maximum quantity of contracts that you can buy  
maxSell | String | `SPOT`/`MARGIN`: The maximum quantity in quote currency that you can sell  
The cross-margin order under `Futures mode` mode, quantity of coins is based on base currency.  
`FUTURES`/`SWAP`/`OPTIONS`: The maximum quantity of contracts that you can sell

---

# 获取最大可下单数量

获取最大可下单数量，可对应下单时的 "sz" 字段

Portfolio Margin 账户下，衍生品的全仓模式不支持最大可买卖/开仓数量的计算。 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/max-size`

> 请求示例
    
    
    GET /api/v5/account/max-size?instId=BTC-USDT&tdMode=isolated
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取最大可买卖/开仓数量
    result = accountAPI.get_max_order_size(
        instId="BTC-USDT",
        tdMode="isolated"
    )
    print(result)
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
支持同一业务线下的多产品ID查询（不超过5个），半角逗号分隔  
tdMode | String | 是 | 交易模式  
`cross`：全仓  
`isolated`：逐仓  
`cash`：非保证金  
`spot_isolated`：现货逐仓，仅适用于`合约模式`  
ccy | String | 可选 | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单  
px | String | 否 | 委托价格  
当不填委托价时，交割和永续会取当前限价计算，其他业务线会按当前最新成交价计算  
当指定多个产品ID查询时，忽略该参数，当未填写处理  
leverage | String | 否 | 开仓杠杆倍数  
默认为当前杠杆倍数  
仅适用于`币币杠杆/交割/永续`  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
outcome | String | 可选 | 交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`，选填，默认值为`yes`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "instId": "BTC-USDT",
            "maxBuy": "0.0500695098559788",
            "maxSell": "64.4798671570072269"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
ccy | String | 保证金币种  
maxBuy | String | `币币/币币杠杆`：最大可买的交易币数量  
`合约模式`下的全仓杠杆订单，为交易币数量  
`交割`/`永续`/`期权`：最大可开多的合约张数  
maxSell | String | `币币/币币杠杆`：最大可卖的计价币数量  
`合约模式`下的全仓杠杆订单，为交易币数量  
`交割`/`永续`/`期权`：最大可开空的合约张数