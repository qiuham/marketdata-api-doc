---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/Exchange-Information
api_type: Market Data
updated_at: 2026-01-15T23:41:03.096009
---

# Exchange Information

## API Description[​](/docs/derivatives/options-trading/market-data/Exchange-Information#api-description "Direct link to API Description")

Current exchange trading rules and symbol information

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Exchange-Information#http-request "Direct link to HTTP Request")

GET `/eapi/v1/exchangeInfo`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Exchange-Information#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Exchange-Information#request-parameters "Direct link to Request Parameters")

NONE

## Response Example[​](/docs/derivatives/options-trading/market-data/Exchange-Information#response-example "Direct link to Response Example")
    
    
    {  
      "timezone": "UTC",                    // Time zone used by the server  
      "serverTime": 1592387337630,          // Current system time  
      "optionContracts": [                  // Option contract underlying asset info  
        {  
          "baseAsset": "BTC",               // Base currency  
          "quoteAsset": "USDT",             // Quotation asset  
          "underlying": "BTCUSDT",          // Name of the underlying asset of the option contract  
          "settleAsset": "USDT"             // Settlement currency  
        }  
      ],  
      "optionAssets": [                     // Option asset info  
        {  
          "name": "USDT"                    // Asset name  
        }  
      ],  
      "optionSymbols": [                    // Option trading pair info  
        {  
            "expiryDate": 1660521600000,    // expiry time  
            "filters": [  
                {  
                    "filterType": "PRICE_FILTER",  
                    "minPrice": "0.02",  
                    "maxPrice": "80000.01",  
                    "tickSize": "0.01"  
                },  
                {  
                    "filterType": "LOT_SIZE",  
                    "minQty": "0.01",  
                    "maxQty": "100",  
                    "stepSize": "0.01"  
                }  
            ],  
            "symbol": "BTC-220815-50000-C",   // Trading pair name  
            "side": "CALL",                   // Direction: CALL long, PUT short  
            "strikePrice": "50000",           // Strike price  
            "underlying": "BTCUSDT",          // Underlying asset of the contract  
            "unit": 1,                        // Contract unit, the quantity of the underlying asset represented by a single contract.  
            "liquidationFeeRate": "0.0019000",// liquidation fee rate  
            "minQty": "0.01",                 // Minimum order quantity  
            "maxQty": "100",                  // Maximum order quantity  
            "initialMargin": "0.15",          // Initial Magin Ratio  
            "maintenanceMargin": "0.075",     // Maintenance Margin Ratio  
            "minInitialMargin": "0.1",        // Min Initial Margin Ratio  
            "minMaintenanceMargin": "0.05",   // Min Maintenance Margin Ratio  
            "priceScale": 2,                  // price precision  
            "quantityScale": 2,               // quantity precision  
            "quoteAsset": "USDT",             // Quotation asset  
            "status": "TRADING"               // Trading Status  
        }  
      ],  
      "rateLimits": [  
        {  
            "rateLimitType": "REQUEST_WEIGHT",  
            "interval": "MINUTE",  
            "intervalNum": 1,  
            "limit": 2400  
        },  
        {  
            "rateLimitType": "ORDERS",  
            "interval": "MINUTE",  
            "intervalNum": 1,  
            "limit": 1200  
        },  
        {  
            "rateLimitType": "ORDERS",  
            "interval": "SECOND",  
            "intervalNum": 10,  
            "limit": 300  
        }  
      ]  
    }

---

# 获取交易规则和交易对

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/Exchange-Information#接口描述 "接口描述的直接链接")

获取交易规则和交易对

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/Exchange-Information#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/exchangeInfo`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/Exchange-Information#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/Exchange-Information#请求参数 "请求参数的直接链接")

NONE

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/Exchange-Information#响应示例 "响应示例的直接链接")
    
    
    {  
      "timezone": "UTC",                    // 服务器时区  
      "serverTime": 1592387337630,          // 请忽略。如果需要获取当前系统时间，请查询接口 “GET /eapi/v1/time”  
      "optionContracts": [                  // 期权合约底层资产信息  
        {  
          "baseAsset": "BTC",               // 标的资产  
          "quoteAsset": "USDT",             // 报价资产  
          "underlying": "BTCUSDT",          // 期权合约底层资产  
          "settleAsset": "USDT"             // 结算资产  
        }  
      ],  
      "optionAssets": [                     // 期权系统支持资产  
        {  
          "name": "USDT"                    // 资产名  
        }  
      ],  
      "optionSymbols": [                    // 期权交易对信息  
        {  
            "expiryDate": 1660521600000,    // 到期时间  
            "filters": [  
                {  
                    "filterType": "PRICE_FILTER",  
                    "minPrice": "0.02",  
                    "maxPrice": "80000.01",  
                    "tickSize": "0.01"  
                },  
                {  
                    "filterType": "LOT_SIZE",  
                    "minQty": "0.01",  
                    "maxQty": "100",  
                    "stepSize": "0.01"  
                }  
            ],  
            "symbol": "BTC-220815-50000-C",   // 交易对  
            "side": "CALL",                   // 期权方向  
            "strikePrice": "50000",           // 行权价  
            "underlying": "BTCUSDT",          // 合约底层资产  
            "unit": 1,                        // 合约单位, 单一合约代表的底层资产数量   
            "liquidationFeeRate": "0.0019000",// 爆仓手续费  
            "minQty": "0.01",                 // 最小下单数量  
            "maxQty": "100",                  // 最大下单数量  
            "initialMargin": "0.15",          // 初始保证金率  
            "maintenanceMargin": "0.075",     // 维持保证金率  
            "minInitialMargin": "0.1",        // 最低初始保证金率  
            "minMaintenanceMargin": "0.05",   // 最低维持保证金率  
            "priceScale": 2,                  // 价格精度  
            "quantityScale": 2,               // 数量精度   
            "quoteAsset": "USDT",             // 报价资产  
            "status": "TRADING"   
        },  
      ],  
      "rateLimits": [  
        {  
            "rateLimitType": "REQUEST_WEIGHT",  
            "interval": "MINUTE",  
            "intervalNum": 1,  
            "limit": 2400  
        },  
        {  
            "rateLimitType": "ORDERS",  
            "interval": "MINUTE",  
            "intervalNum": 1,  
            "limit": 1200  
        },  
        {  
            "rateLimitType": "ORDERS",  
            "interval": "SECOND",  
            "intervalNum": 10,  
            "limit": 300  
        }  
      ]  
    }