---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/stake
api_type: REST
updated_at: 2026-07-01 19:25:43.350532
---

# Get Trade Quote

Get a price quote before executing a purchase or redeem trade. This is a **mandatory step** before calling [Execute Purchase](/docs/v5/alpha/trade-purchase) or [Execute Redeem](/docs/v5/alpha/trade-redeem).

info

  * Returns estimated receive amount, exchange rate, platform fee, gas cost, and slippage
  * `quoteData` and `correctingCode` must be passed as-is to the execution endpoint — do not modify
  * Quote expires at `expireTime`; re-fetch if expired before executing
  * `correctingCode` is an MD5 of `(quoteData + fromTokenCode + fromTokenAmount + toTokenCode)` for tamper protection
  * Token codes can be obtained from [Get Pay Token List](/docs/v5/alpha/pay-token-list) (CEX tokens) and [Get Biz Token List](/docs/v5/alpha/biz-token-list) (DEX tokens)



### HTTP Request

POST`/v5/alpha/trade/quote`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tradeType| **true**|  integer| Trade type. `1`: Purchase (buy on-chain token with payment token), `2`: Redeem (sell on-chain token for payment token)  
fromTokenCode| **true**|  string| Source token code (`CEX_<id>` or `DEX_<id>`). Purchase: CEX token (e.g. `CEX_1` for USDT); Redeem: DEX token (e.g. `DEX_123`)  
fromTokenAmount| **true**|  string| Amount to pay, string-formatted positive decimal. Must be greater than 0  
toTokenCode| **true**|  string| Target token code (`CEX_<id>` or `DEX_<id>`). Purchase: DEX token; Redeem: CEX token (e.g. `CEX_1` for USDT)  
quoteMode| false| integer| Quote mode. `0`: Auto (default), `1`: Price Priority, `2`: Success Rate Priority  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tradeType| integer| Trade type echoed back  
fromTokenCode| string| Source token code  
fromTokenAmount| string| Amount to pay  
fromTokenAmountUsd| string| Payment amount in USD  
toTokenCode| string| Target token code  
toTokenAmount| string| Expected amount to receive  
toTokenAmountUsd| string| Expected receive amount in USD  
minToTokenAmount| string| Minimum amount to receive after slippage  
slippage| string| Estimated slippage as decimal, e.g. `0.005` = 0.5%  
gas| string| Estimated gas fee in native token unit  
gasUsd| string| Gas fee in USD  
platformFee| string| Platform fee  
platformFeeUsd| string| Platform fee in USD  
swapRate| string| Exchange rate (toToken per fromToken)  
lossRate| string| Estimated loss rate from fees and slippage  
quoteData| string| Base64-encoded quote context. **Must be passed as-is to the execution endpoint**  
correctingCode| string| MD5 checksum for data integrity. **Must be passed as-is to the execution endpoint**  
quoteMode| integer| Actual quote mode used  
quoteDataId| string| Unique quote ID for idempotency  
expireTime| integer| Quote expiration time (ms). Do not execute with an expired quote  
timestamp| integer| Quote timestamp (ms). Use to compare freshness across multiple quotes  
chargeAmount| string| Fee charge amount  
modeEstimations| array| Alternative mode estimations for comparison  
> quoteMode| integer| Quote mode  
> estimatedGas| string| Estimated gas fee in this mode  
> estimatedGasUsd| string| Estimated gas in USD  
> estimatedSlippage| string| Estimated slippage  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/quote HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tradeType": 1,  
        "fromTokenCode": "CEX_1",  
        "fromTokenAmount": "100",  
        "toTokenCode": "DEX_123",  
        "quoteMode": 0  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tradeType": 1,  
            "fromTokenCode": "CEX_1",  
            "fromTokenAmount": "100",  
            "fromTokenAmountUsd": "100.00",  
            "toTokenCode": "DEX_123",  
            "toTokenAmount": "12500000",  
            "toTokenAmountUsd": "99.50",  
            "minToTokenAmount": "12375000",  
            "slippage": "0.005",  
            "gas": "0.0003",  
            "gasUsd": "0.30",  
            "platformFee": "0.20",  
            "platformFeeUsd": "0.20",  
            "swapRate": "125000",  
            "lossRate": "0.005",  
            "quoteData": "eyJhbGciOiJIUzI1NiJ9...",  
            "correctingCode": "a1b2c3d4e5f6",  
            "quoteMode": 0,  
            "quoteDataId": "QD_20240101_001",  
            "expireTime": 1704067230000,  
            "modeEstimations": [  
                {  
                    "quoteMode": 1,  
                    "estimatedGas": "12600000",  
                    "estimatedGasUsd": "0.28",  
                    "estimatedSlippage": "0.008"  
                },  
                {  
                    "quoteMode": 2,  
                    "estimatedGas": "12400000",  
                    "estimatedGasUsd": "0.35",  
                    "estimatedSlippage": "0.003"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取交易報價

在執行購買或贖回交易前獲取價格報價。調用 [執行購買](/docs/zh-TW/v5/alpha/trade-purchase) 或 [執行贖回](/docs/zh-TW/v5/alpha/trade-redeem) 前**必須** 先調用此接口。

信息

  * 返回預估接收數量、匯率、平台手續費、Gas 費用及滑點
  * `quoteData` 和 `correctingCode` 必須原樣傳入執行接口，不得修改
  * 報價在 `expireTime` 後過期，過期後須重新獲取
  * `correctingCode` 為 `(quoteData + fromTokenCode + fromTokenAmount + toTokenCode)` 的 MD5 校驗碼，用於防篡改
  * 代幣代碼可通過 [獲取支付代幣列表](/docs/zh-TW/v5/alpha/pay-token-list)（CEX 代幣）及 [獲取業務代幣列表](/docs/zh-TW/v5/alpha/biz-token-list)（DEX 代幣）獲取



### HTTP 請求

POST`/v5/alpha/trade/quote`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tradeType| **true**|  integer| 交易類型。`1`: 購買（用支付代幣買入鏈上代幣），`2`: 贖回（賣出鏈上代幣換支付代幣）  
fromTokenCode| **true**|  string| 源代幣代碼（`CEX_<id>` 或 `DEX_<id>`）。購買填 CEX 代幣（如 USDT 對應 `CEX_1`）；贖回填 DEX 代幣（如 `DEX_123`）  
fromTokenAmount| **true**|  string| 支付數量，字符串格式的正小數，須大於 0  
toTokenCode| **true**|  string| 目標代幣代碼（`CEX_<id>` 或 `DEX_<id>`）。購買填 DEX 代幣；贖回填 CEX 代幣（如 USDT 對應 `CEX_1`）  
quoteMode| false| integer| 報價模式。`0`: 自動（默認），`1`: 價格優先，`2`: 成功率優先  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tradeType| integer| 交易類型回顯  
fromTokenCode| string| 源代幣代碼  
fromTokenAmount| string| 支付數量  
fromTokenAmountUsd| string| 支付金額（USD）  
toTokenCode| string| 目標代幣代碼  
toTokenAmount| string| 預估接收數量  
toTokenAmountUsd| string| 預估接收金額（USD）  
minToTokenAmount| string| 扣除滑點後最低接收數量  
slippage| string| 預估滑點（小數），如 `0.005` = 0.5%  
gas| string| 預估 Gas 費用（原生代幣單位）  
gasUsd| string| Gas 費用（USD）  
platformFee| string| 平台手續費  
platformFeeUsd| string| 平台手續費（USD）  
swapRate| string| 兌換匯率（每單位 fromToken 可換 toToken 數量）  
lossRate| string| 含手續費與滑點的預估損耗率  
quoteData| string| Base64 編碼報價數據。**必須原樣傳入執行接口，不得修改**  
correctingCode| string| 數據完整性 MD5 校驗碼。**必須原樣傳入執行接口**  
quoteMode| integer| 實際使用的報價模式  
quoteDataId| string| 唯一報價 ID，用於冪等性控制  
expireTime| integer| 報價過期時間（ms），過期後請勿使用該報價執行交易  
timestamp| integer| 報價時間戳（ms），可用於比較多個報價的新鮮度  
chargeAmount| string| 收費金額  
modeEstimations| array| 其他模式的預估數據，供對比參考  
> quoteMode| integer| 報價模式  
> estimatedGas| string| 該模式預估 Gas 費用  
> estimatedGasUsd| string| 該模式預估 Gas 費用（USD）  
> estimatedSlippage| string| 該模式預估滑點  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/quote HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tradeType": 1,  
        "fromTokenCode": "CEX_1",  
        "fromTokenAmount": "100",  
        "toTokenCode": "DEX_123",  
        "quoteMode": 0  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tradeType": 1,  
            "fromTokenCode": "CEX_1",  
            "fromTokenAmount": "100",  
            "fromTokenAmountUsd": "100.00",  
            "toTokenCode": "DEX_123",  
            "toTokenAmount": "12500000",  
            "toTokenAmountUsd": "99.50",  
            "minToTokenAmount": "12375000",  
            "slippage": "0.005",  
            "gas": "0.0003",  
            "gasUsd": "0.30",  
            "platformFee": "0.20",  
            "platformFeeUsd": "0.20",  
            "swapRate": "125000",  
            "lossRate": "0.005",  
            "quoteData": "eyJhbGciOiJIUzI1NiJ9...",  
            "correctingCode": "a1b2c3d4e5f6",  
            "quoteMode": 0,  
            "quoteDataId": "QD_20240101_001",  
            "expireTime": 1704067230000,  
            "modeEstimations": [  
                {  
                    "quoteMode": 1,  
                    "estimatedGas": "12600000",  
                    "estimatedGasUsd": "0.28",  
                    "estimatedSlippage": "0.008"  
                },  
                {  
                    "quoteMode": 2,  
                    "estimatedGas": "12400000",  
                    "estimatedGasUsd": "0.35",  
                    "estimatedSlippage": "0.003"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }