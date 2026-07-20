---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-leverage
anchor_id: trading-account-rest-api-set-leverage
api_type: REST
updated_at: 2026-07-20 19:35:08.970513
---

# Set leverage

There are 10 different scenarios for leverage setting:   
  
1\. Set leverage for `MARGIN` instruments under `isolated-margin` trade mode at pairs level.   
2\. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Spot mode (enabled borrow) at currency level.   
3\. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Futures mode account mode at pairs level.   
4\. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Multi-currency margin at currency level.   
5\. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Portfolio margin at currency level.   
6\. Set leverage for `FUTURES` instruments under `cross-margin` trade mode at underlying level.   
7\. Set leverage for `FUTURES` instruments under `isolated-margin` trade mode and buy/sell position mode at contract level.   
8\. Set leverage for `FUTURES` instruments under `isolated-margin` trade mode and long/short position mode at contract and position side level.   
9\. Set leverage for `SWAP` instruments under `cross-margin` trade at contract level.   
10\. Set leverage for `SWAP` instruments under `isolated-margin` trade mode and buy/sell position mode at contract level.   
11\. Set leverage for `SWAP` instruments under `isolated-margin` trade mode and long/short position mode at contract and position side level.   
  

Note that the request parameter `posSide` is only required when margin mode is isolated in long/short position mode for FUTURES/SWAP instruments (see scenario 8 and 11 above).   
Please refer to the request examples on the right for each case.   

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-leverage`

> Request Example
    
    
    # 1. Set leverage for `MARGIN` instruments under `isolated-margin` trade mode at pairs level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 2. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Spot mode (enabled borrow) at currency level.
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 3. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Futures mode account mode at pairs level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 4. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Multi-currency margin at currency level.
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 5. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Portfolio margin at currency level.
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 6. Set leverage for `FUTURES` instruments under `cross-margin` trade mode at underlying level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 7. Set leverage for `FUTURES` instruments under `isolated-margin` trade mode and buy/sell order placement mode at contract level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 8. Set leverage for `FUTURES` instruments under `isolated-margin` trade mode and long/short order placement mode at contract and position side level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "posSide":"long",
        "mgnMode":"isolated"
    }
    
    # 9. Set leverage for `SWAP` instruments under `cross-margin` trade at contract level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 10. Set leverage for `SWAP` instruments under `isolated-margin` trade mode and buy/sell order placement mode at contract level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 11. Set leverage for `SWAP` instruments under `isolated-margin` trade mode and long/short order placement mode at contract and position side level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "posSide":"long",
        "mgnMode":"isolated"
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set leverage for MARGIN instruments under isolated-margin trade mode at pairs level.
    result = accountAPI.set_leverage(
        instId="BTC-USDT",
        lever="5",
        mgnMode="isolated"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Conditional | Instrument ID  
Only applicable to `cross` `FUTURES` `SWAP` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`, `cross` `MARGIN``FUTURES``SWAP` and `isolated` position.  
And required in applicable scenarios.  
ccy | String | Conditional | Currency used for margin, used for the leverage setting for the currency in auto borrow.  
Only applicable to `cross` `MARGIN` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`.  
And required in applicable scenarios.  
lever | String | Yes | Leverage  
mgnMode | String | Yes | Margin mode  
`isolated` `cross`   
Can only be `cross` if `ccy` is passed.  
posSide | String | Conditional | Position side  
`long` `short`  
Only required when margin mode is `isolated` in `long/short` mode for `FUTURES`/`SWAP`.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "lever": "30",
          "mgnMode": "isolated",
          "instId": "BTC-USDT-SWAP",
          "posSide": "long"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
lever | String | Leverage  
mgnMode | String | Margin mode  
`cross` `isolated`  
instId | String | Instrument ID  
posSide | String | Position side  
When setting leverage for `cross` `FUTURES`/`SWAP` at the underlying level, pass in any instId and mgnMode(`cross`).  Leverage cannot be adjusted for the cross positions of Expiry Futures and Perpetual Futures under the portfolio margin account.

---

# 设置杠杆倍数

一个产品可以有如下10种杠杆倍数的设置场景：  
  
  
  
  1. 在`逐仓`交易模式下，设置`币币杠杆`的杠杆倍数（币对层面）；  

  2. `现货模式`账户已开通借币功能，在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）；  

  3. `合约模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币对层面）；  

  4. `跨币种保证金模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）；  

  5. `组合保证金模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）；  

  6. 在`全仓`交易模式下，设置`交割`的杠杆倍数（指数层面）；  

  7. 在`逐仓`交易模式、`买卖`持仓模式下，设置`交割`的杠杆倍数（合约层面）；  

  8. 在`逐仓`交易模式、`开平仓`持仓模式下，设置`交割`的杠杆倍数（合约与持仓方向层面）；  

  9. 在`全仓`交易模式下，设置`永续`的杠杆倍数（合约层面）；  

  10. 在`逐仓`交易模式、`买卖`持仓模式下，设置`永续`的杠杆倍数（合约层面）；  

  11. 在`逐仓`交易模式、`开平仓`持仓模式下，设置`永续`的杠杆倍数（合约与持仓方向层面）；  

注意请求参数 posSide 仅在`交割/永续`的`开平仓`持仓模式下才需要填写（参见场景8和11）。  
请参阅右侧对应的每个案例的请求示例。  

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-leverage`

> 请求示例
    
    
    # 1.在`逐仓`交易模式下，设置`币币杠杆`的杠杆倍数（币对层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 2.`现货模式`账户已开通借币功能，在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    
    # 3.`合约模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币对层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 4.`跨币种保证金模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 5. `组合保证金模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 6.在`全仓`交易模式下，设置`交割`的杠杆倍数（指数层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 7.在`逐仓`交易模式、`买卖`持仓模式下，设置`交割`的杠杆倍数（合约层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 8.在`逐仓`交易模式、`开平仓`持仓模式下，设置`交割`的杠杆倍数（合约与头寸层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "posSide":"long",
        "mgnMode":"isolated"
    }
    
    # 9.在`全仓`交易模式下，设置`永续`的杠杆倍数（合约层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 10.在`逐仓`交易模式、`买卖`持仓模式下，设置`永续`的杠杆倍数（合约层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 11.在`逐仓`交易模式、`开平仓`持仓模式下，设置`永续`的杠杆倍数（合约与头寸层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "posSide":"long",
        "mgnMode":"isolated"
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 在逐仓交易模式下，设置币币杠杆的杠杆倍数（币对层面）
    result = accountAPI.set_leverage(
        instId="BTC-USDT",
        lever="5",
        mgnMode="isolated"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 可选 | 产品ID：币对、合约  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`的`全仓``交割``永续`，`合约模式`的`全仓``币币杠杆``交割``永续` 以及`逐仓`。  
且在适用场景下必填。  
ccy | String | 可选 | 保证金币种，用于设置开启自动借币模式下币种维度的杠杆。  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`的`全仓``币币杠杆`。  
且在适用场景下必填。  
lever | String | 是 | 杠杆倍数  
mgnMode | String | 是 | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
如果`ccy`有效传值，该参数值只能为`cross`。  
posSide | String | 可选 | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
仅适用于逐仓`交割`/`永续`  
在开平仓模式且保证金模式为逐仓条件下必填  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "lever": "30",
            "mgnMode": "isolated",
            "instId": "BTC-USDT-SWAP",
            "posSide": "long"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
lever | String | 杠杆倍数  
mgnMode | String | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
instId | String | 产品ID  
posSide | String | 持仓方向  
当希望在指数层面设置交割/永续的全仓杠杆倍数时，传入任意产品ID 和保证金模式（全仓）即可。  组合保证金账户下交割和永续的全仓不能调整杠杆倍数。