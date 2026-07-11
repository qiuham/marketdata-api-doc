---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-maximum-available-balance-equity
anchor_id: trading-account-rest-api-get-maximum-available-balance-equity
api_type: REST
updated_at: 2026-07-11 19:12:08.722338
---

# Get maximum available balance/equity

Available balance for isolated margin positions and SPOT, available equity for cross margin positions.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/max-avail-size`

> Request Example
    
    
    # Query maximum available transaction amount when cross MARGIN BTC-USDT use BTC as margin
    GET /api/v5/account/max-avail-size?instId=BTC-USDT&tdMode=cross&ccy=BTC
    
    # Query maximum available transaction amount for SPOT BTC-USDT
    GET /api/v5/account/max-avail-size?instId=BTC-USDT&tdMode=cash
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get maximum available transaction amount for SPOT BTC-USDT
    result = accountAPI.get_max_avail_size(
        instId="BTC-USDT",
        tdMode="cash"
    )
    print(result)
    

#### Request Parameters

**Parameter** | **Type** | Required | Description  
---|---|---|---  
instId | String | Yes | Single instrument or multiple instruments (no more than 5) separated with comma, e.g. `BTC-USDT,ETH-USDT`  
ccy | String | Conditional | Currency used for margin  
Applicable to `isolated` `MARGIN` and `cross` `MARGIN` in `Futures mode`.  
tdMode | String | Yes | Trade mode  
`cross`  
`isolated`  
`cash`  
`spot_isolated`: only applicable to `Futures mode`  
reduceOnly | Boolean | No | Whether to reduce position only   
Only applicable to `MARGIN`  
px | String | No | The price of closing position.   
Only applicable to reduceOnly `MARGIN`.  
tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`.   
The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "instId": "BTC-USDT",
          "availBuy": "100",
          "availSell": "1"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
availBuy | String | Maximum available balance/equity to buy  
availSell | String | Maximum available balance/equity to sell  
In the case of SPOT/MARGIN, availBuy is in the quote currency, and availSell is in the base currency.  
In the case of MARGIN with cross tdMode, both availBuy and availSell are in the currency passed in **ccy**.

---

# 获取最大可用余额/保证金

币币和逐仓时为可用余额，全仓时为可用保证金  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/max-avail-size`

> 请求示例
    
    
    # 获取BTC-USDT全仓币币杠杆指定BTC作为保证金最大可用数量
    GET /api/v5/account/max-avail-size?instId=BTC-USDT&tdMode=cross&ccy=BTC
    
    # 获取BTC-USDT币币最大可用数量
    GET /api/v5/account/max-avail-size?instId=BTC-USDT&tdMode=cash
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取BTC-USDT币币最大可用数量
    result = accountAPI.get_max_avail_size(
        instId="BTC-USDT",
        tdMode="cash"
    )
    print(result)
    

#### 请求参数

**参数名** | **类型** | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
支持多产品ID查询（不超过5个），半角逗号分隔  
tdMode | String | 是 | 交易模式  
`cross`：全仓  
`isolated`：逐仓  
`cash`：非保证金  
`spot_isolated`：现货逐仓，仅适用于`合约模式`  
ccy | String | 可选 | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`  
reduceOnly | Boolean | 否 | 是否为只减仓模式，仅适用于`币币杠杆`  
px | String | 否 | 平仓价格，默认为市价。  
仅适用于杠杆只减仓  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "instId": "BTC-USDT",
            "availBuy": "100",
            "availSell": "1"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
availBuy | String | 最大买入可用余额/保证金  
availSell | String | 最大卖出可用余额/保证金  
币币/币币杠杆时availBuy为计价货币，availSell为交易货币。  
全仓币币杠杆时，availBuy和availSell均为指定保证金的币种。