---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-fee-rates
anchor_id: trading-account-rest-api-get-fee-rates
api_type: REST
updated_at: 2026-07-09 19:36:36.057131
---

# Get fee rates

#### Rate Limit: 5 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/trade-fee`

> Request Example
    
    
    # Query trade fee rate of SPOT BTC-USDT
    GET /api/v5/account/trade-fee?instType=SPOT&instId=BTC-USDT
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get trading fee rates of current account
    result = accountAPI.get_fee_rates(
        instType="SPOT",
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
Applicable to `SPOT`/`MARGIN`  
Specifying this parameter returns the correct applicable fee rates (e.g., market maker rates for users in incentive programs).  
instFamily | String | No | Instrument family, e.g. `BTC-USD`  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
groupId | String | No | Instrument trading fee group ID  
Only one of groupId and instId/instFamily can be passed in  
  
Users can use instruments endpoint to fetch the mapping of an instrument ID and its trading fee group ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "category": "1",
                "delivery": "",
                "exercise": "",
                "feeGroup": [
                    {
                        "elpMaker": "-0.0008",
                        "groupId": "1",
                        "maker": "-0.0008",
                        "taker": "-0.001"
                    }
                ],
                "fiat": [],
                "instType": "SPOT",
                "level": "Lv1",
                "maker": "-0.0008",
                "makerU": "",
                "makerUSDC": "",
                "ruleType": "normal",
                "taker": "-0.001",
                "takerU": "",
                "takerUSDC": "",
                "ts": "1763979985847"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
level | String | Fee rate Level  
feeGroup | Array of objects | Fee groups.   
Applicable to `SPOT/MARGIN/SWAP/FUTURES/OPTION/EVENTS`  
> taker | String | Taker fee  
K1 parameter for `EVENTS` taker fee formula: `K1 × C × (P × (1-P))` (C = number of contracts, P = price)  
> maker | String | Maker fee  
K2 parameter for `EVENTS` maker fee formula: `K2 × C × (P × (1-P))` (C = number of contracts, P = price)  
> groupId | String | Instrument trading fee group ID  
  
**instType and groupId should be used together to determine a trading fee group. Users should use this endpoint together with[instruments endpoint](/docs-v5/en/#trading-account-rest-api-get-instruments) to get the trading fee of a specific symbol.**  
> elpMaker | String | ELP Maker effective fee rate. Returns `""` if ELP is not applicable to the instrument.  
delivery | String | Delivery fee rate  
exercise | String | Fee rate for exercising the option  
instType | String | Instrument type  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
taker | String | ~~For`SPOT`/`MARGIN`, it is taker fee rate of the USDT trading pairs.   
For `FUTURES`/`SWAP`/`OPTION`, it is the fee rate of crypto-margined contracts~~(deprecated)  
maker | String | ~~For`SPOT`/`MARGIN`, it is maker fee rate of the USDT trading pairs.   
For `FUTURES`/`SWAP`/`OPTION`, it is the fee rate of crypto-margined contracts~~(deprecated)  
takerU | String | ~~Taker fee rate of USDT-margined contracts, only applicable to`FUTURES`/`SWAP`~~(deprecated)  
makerU | String | ~~Maker fee rate of USDT-margined contracts, only applicable to`FUTURES`/`SWAP`~~(deprecated)  
takerUSDC | String | ~~For`SPOT`/`MARGIN`, it is taker fee rate of the USDⓈ&Crypto trading pairs.  
For `FUTURES`/`SWAP`, it is the fee rate of USDC-margined contracts~~(deprecated)  
makerUSDC | String | ~~For`SPOT`/`MARGIN`, it is maker fee rate of the USDⓈ&Crypto trading pairs.  
For `FUTURES`/`SWAP`, it is the fee rate of USDC-margined contracts~~(deprecated)  
ruleType | String | ~~Trading rule types  
`normal`: normal trading  
`pre_market`: pre-market trading~~(deprecated)  
category | String | ~~Currency category.~~(deprecated)  
fiat | Array of objects | ~~Details of fiat fee rate~~(deprecated)  
> ccy | String | Fiat currency.  
> taker | String | Taker fee rate  
> maker | String | Maker fee rate  
settle | String | Settlement fee rate for users whose positions match the event contract settlement result. Users holding the opposite positions will not be charged during settlement. Only applicable to `EVENTS`  
Remarks:   
The fee rate like maker and taker: positive number, which means the rate of rebate; negative number, which means the rate of commission.  
Exception: The values for delivery and exercise are positive numbers, representing the commission rate.  USDⓈ represent the stablecoin besides USDT  The Open API will not reflect zero-fee trading. For zero-fee pairs, please refer to [https://www.okx.com/fees ](https://www.okx.com/fees).  For users in market maker incentive programs: specifying `instId` (for `SPOT`/`MARGIN`) or `instFamily` (for `FUTURES`/`SWAP`/`OPTION`) returns the correct applicable fee rates. Without these parameters, the response reflects the organic base fee rates.

---

# 获取当前账户交易手续费费率

#### 限速：5次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/trade-fee`

> 请求示例
    
    
    # 获取币币BTC-USDT交易手续费率  
    GET /api/v5/account/trade-fee?instType=SPOT&instId=BTC-USDT
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取当前账户交易手续费费率
    result = accountAPI.get_fee_rates(
        instType="SPOT",
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 否 | 产品ID，如 `BTC-USDT`  
仅适用于instType为`币币/币币杠杆`  
指定此参数将返回正确的适用手续费率（如：参与做市激励计划用户的做市商费率）。  
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`，如 `BTC-USD`  
groupId | String | 否 | 交易产品手续费分组ID  
groupId 和 instId/instFamily 只能传入其一  
  
用户可以使用交易产品基础信息接口获取产品ID及其手续费分组ID的对应关系  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "category": "1",
                "delivery": "",
                "exercise": "",
                "feeGroup": [
                    {
                        "elpMaker": "-0.0008",
                        "groupId": "1",
                        "maker": "-0.0008",
                        "taker": "-0.001"
                    }
                ],
                "fiat": [],
                "instType": "SPOT",
                "level": "Lv1",
                "maker": "-0.0008",
                "makerU": "",
                "makerUSDC": "",
                "ruleType": "normal",
                "taker": "-0.001",
                "takerU": "",
                "takerUSDC": "",
                "ts": "1763979985847"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
level | String | 手续费等级  
feeGroup | Array of objects | 手续费分组   
适用于`SPOT/MARGIN/SWAP/FUTURES/OPTION/EVENTS`  
> taker | String | 吃单手续费  
`EVENTS` 吃单手续费公式的 K1 参数：`K1 × C × (P × (1-P))`（C = 合约张数，P = 价格）  
> maker | String | 挂单手续费  
`EVENTS` 挂单手续费公式的 K2 参数：`K2 × C × (P × (1-P))`（C = 合约张数，P = 价格）  
> groupId | String | 交易产品手续费分组ID  
  
**用户需要同时使用instType和groupId来确定一个交易产品的交易手续费分组；用户应该将此接口和[获取交易产品基础信息](/docs-v5/zh/#trading-account-rest-api-get-instruments)一起使用，以获取特定交易产品的手续费率**  
> elpMaker | String | ELP Maker 有效费率。若 ELP 不适用于该交易产品，则返回 `""`。  
delivery | String | 交割手续费率  
exercise | String | 行权手续费率  
instType | String | 产品类型  
ts | String | 数据返回时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
taker | String | ~~对于币币/杠杆，为 USDT 交易区的吃单手续费率；  
对于永续，交割和期权合约，为币本位合约费率~~（已废弃）  
maker | String | ~~对于币币/杠杆，为 USDT 交易区的挂单手续费率；  
对于永续，交割和期权合约，为币本位合约费率~~（已废弃）  
takerU | String | ~~USDT 合约吃单手续费率，仅适用于`交割/永续`~~（已废弃）  
makerU | String | ~~USDT 合约挂单手续费率，仅适用于`交割/永续`~~（已废弃）  
takerUSDC | String | ~~对于币币/杠杆，为 USDⓈ &Crypto 交易区的吃单手续费率；  
对于永续和交割合约，为 USDC 合约费率~~（已废弃）  
makerUSDC | String | ~~对于币币/杠杆，为 USDⓈ &Crypto 交易区的挂单手续费率；  
对于永续和交割合约，为 USDC 合约费率~~（已废弃）  
ruleType | String | ~~交易规则类型  
`normal`：普通交易  
`pre_market`：盘前交易~~（已废弃）  
category | String | ~~币种类别~~ （已废弃）  
fiat | Array of objects | ~~法币费率~~ （已废弃）  
> ccy | String | 法币币种  
> taker | String | 吃单手续费率  
> maker | String | 挂单手续费率  
settle | String | 结算手续费率，适用于持仓方向与事件合约结算结果一致的用户。持反向仓位的用户结算时不收取手续费。仅适用于 `EVENTS`  
备注：  
手续费率的值（如 maker/taker）：正数，代表是返佣的费率；负数，代表平台扣除的费率。  
例外：delivery 和 exercise 为正数，代表平台扣除的费率。  USDⓈ 代表除 USDT 之外的稳定币。  接口不会体现零手续费，零手续费交易对请参考<https://www.okx.com/zh-hans/fees> 对于参与做市激励计划的用户：指定 `instId`（适用于 `SPOT`/`MARGIN`）或 `instFamily`（适用于 `FUTURES`/`SWAP`/`OPTION`）将返回正确的适用手续费率；若不指定上述参数，则返回基础档位手续费率。