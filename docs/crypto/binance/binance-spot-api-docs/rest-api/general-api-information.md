---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-api-information
api_type: REST
updated_at: 2026-05-27 18:54:20.322783
---

# General endpoints

### Test connectivity[​](/docs/binance-spot-api-docs/rest-api/general-endpoints#test-connectivity "Direct link to Test connectivity")
    
    
    GET /api/v3/ping  
    

Test connectivity to the Rest API.

**Weight:** 1

**Parameters:** NONE

**Data Source:** Memory

**Response:**
    
    
    {}  
    

### Check server time[​](/docs/binance-spot-api-docs/rest-api/general-endpoints#check-server-time "Direct link to Check server time")
    
    
    GET /api/v3/time  
    

Test connectivity to the Rest API and get the current server time.

**Weight:** 1

**Parameters:** NONE

**Data Source:** Memory

**Response:**
    
    
    {  
        "serverTime": 1499827319559  
    }  
    

### Exchange information[​](/docs/binance-spot-api-docs/rest-api/general-endpoints#exchange-information "Direct link to Exchange information")
    
    
    GET /api/v3/exchangeInfo  
    

Current exchange trading rules and symbol information

**Weight:** 20

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| No| Example: curl -X GET "<https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC>"  
symbols| ARRAY OF STRING| No| Examples: curl -X GET "<https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D>"   
or   
curl -g -X GET '[https://api.binance.com/api/v3/exchangeInfo?symbols=["BTCUSDT","BNBBTC](https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BTCUSDT%22,%22BNBBTC)"]'  
permissions| ENUM| No| Examples: curl -X GET "<https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT>"   
or   
curl -X GET "<https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D>"   
or   
curl -g -X GET '[https://api.binance.com/api/v3/exchangeInfo?permissions=["MARGIN","LEVERAGED](https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22,%22LEVERAGED)"]'  
showPermissionSets| BOOLEAN| No| Controls whether the content of the `permissionSets` field is populated or not. Defaults to `true`  
symbolStatus| ENUM| No| Filters for symbols that have this `tradingStatus`. Valid values: `TRADING`, `HALT`, `BREAK`   
Cannot be used in combination with `symbols` or `symbol`.  
  
**Notes:**

  * If the value provided to `symbol` or `symbols` do not exist, the endpoint will throw an error saying the symbol is invalid.
  * All parameters are optional.
  * `permissions` can support single or multiple values (e.g. `SPOT`, `["MARGIN","LEVERAGED"]`). This cannot be used in combination with `symbol` or `symbols`.
  * If `permissions` parameter not provided, all symbols that have either `SPOT`, `MARGIN`, or `LEVERAGED` permission will be exposed. 
    * To display symbols with any permission you need to specify them explicitly in `permissions`: (e.g. `["SPOT","MARGIN",...]`.). See [Account and Symbol Permissions](/docs/binance-spot-api-docs/enums#account-and-symbol-permissions) for the full list.



**Examples of Symbol Permissions Interpretation from the Response:**

  * `[["A","B"]]` means you may place an order if your account has either permission "A" **or** permission "B".
  * `[["A"],["B"]]` means you can place an order if your account has permission "A" **and** permission "B".
  * `[["A"],["B","C"]]` means you can place an order if your account has permission "A" **and** permission "B" or permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission "B" and permission "C".)



**Data Source:** Memory

**Response:**
    
    
    {  
        "timezone": "UTC",  
        "serverTime": 1565246363776,  
        "rateLimits": [  
            {  
                // These are defined in the `ENUM definitions` section under `Rate Limiters (rateLimitType)`.  
                // All limits are optional  
            }  
        ],  
        "exchangeFilters": [  
            // These are the defined filters in the `Filters` section.  
            // All filters are optional.  
        ],  
        "symbols": [  
            {  
                "symbol": "ETHBTC",  
                "status": "TRADING",  
                "baseAsset": "ETH",  
                "baseAssetPrecision": 8,  
                "quoteAsset": "BTC",  
                "quotePrecision": 8,     // will be removed in future api versions (v4+)  
                "quoteAssetPrecision": 8,  
                "baseCommissionPrecision": 8,  
                "quoteCommissionPrecision": 8,  
                "orderTypes": [  
                    "LIMIT",  
                    "LIMIT_MAKER",  
                    "MARKET",  
                    "STOP_LOSS",  
                    "STOP_LOSS_LIMIT",  
                    "TAKE_PROFIT",  
                    "TAKE_PROFIT_LIMIT"  
                ],  
                "icebergAllowed": true,  
                "ocoAllowed": true,  
                "otoAllowed": true,  
                "opoAllowed": true,  
                "quoteOrderQtyMarketAllowed": true,  
                "allowTrailingStop": false,  
                "cancelReplaceAllowed": false,  
                "amendAllowed": false,  
                "pegInstructionsAllowed": true,  
                "isSpotTradingAllowed": true,  
                "isMarginTradingAllowed": true,  
                "filters": [  
                    // These are defined in the Filters section.  
                    // All filters are optional  
                ],  
                "permissions": [],  
                "permissionSets": [["SPOT", "MARGIN"]],  
                "defaultSelfTradePreventionMode": "NONE",  
                "allowedSelfTradePreventionModes": ["NONE"]  
            }  
        ],  
        // Optional field. Present only when SOR is available.  
        // https://github.com/binance/binance-spot-api-docs/blob/master/faqs/sor_faq.md  
        "sors": [  
            {  
                "baseAsset": "BTC",  
                "symbols": ["BTCUSDT", "BTCUSDC"]  
            }  
        ]  
    }  
    

### Query Execution Rules[​](/docs/binance-spot-api-docs/rest-api/general-endpoints#query-execution-rules "Direct link to Query Execution Rules")
    
    
    GET /api/v3/executionRules  
    

**Weight**

Parameter| Weight  
---|---  
`symbol`| 2  
`symbols`| 2 for each `symbol`, capped at a max of 40  
`symbolStatus`| 40  
None| 40  
  
**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| No| Query for specified symbol  
`symbols`| STRING| No| Query for multiple symbols  
`symbolStatus`| ENUM| Query for all symbols with the specified status. Supported values: `TRADING`, `HALT`, `BREAK`|   
  
**Note:** No combination of multiple parameters is allowed.

**Data Source:** Memory

**Response:**
    
    
    {  
        "symbolRules": [  
            {  
                "symbol": "BAZUSD",  
                "rules": [  
                    {  
                        "ruleType": "PRICE_RANGE",  
                        "bidLimitMultUp": "1.0001",  
                        "bidLimitMultDown": "0.9999",  
                        "askLimitMultUp": "1.0001",  
                        "askLimitMultDown": "0.9999"  
                    }  
                ]  
            }  
        ]  
    }

---

# 通用接口

### 测试服务器连通性 PING[​](/docs/zh-CN/binance-spot-api-docs/rest-api/general-endpoints#测试服务器连通性-ping "测试服务器连通性 PING的直接链接")
    
    
    GET /api/v3/ping  
    

测试能否联通

**权重:** 1

**参数:** NONE

**数据源:** 缓存

**响应:**
    
    
    {}  
    

### 获取服务器时间[​](/docs/zh-CN/binance-spot-api-docs/rest-api/general-endpoints#获取服务器时间 "获取服务器时间的直接链接")
    
    
    GET /api/v3/time  
    

获取服务器时间

**权重:** 1

**参数:** NONE

**数据源:** 缓存

**响应:**
    
    
    {  
        "serverTime": 1499827319559  
    }  
    

### 交易规范信息[​](/docs/zh-CN/binance-spot-api-docs/rest-api/general-endpoints#交易规范信息 "交易规范信息的直接链接")
    
    
    GET /api/v3/exchangeInfo  
    

获取此时的交易规范信息

**权重:** 20

**参数:**

名称| 类型| 是否必须| 描述  
---|---|---|---  
symbol| STRING| No| 示例：curl -X GET "<https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC>"  
symbols| ARRAY OF STRING| No| 示例：curl -X GET "<https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D>"   
或   
curl -g -X GET '[https://api.binance.com/api/v3/exchangeInfo?symbols=["BTCUSDT","BNBBTC](https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BTCUSDT%22,%22BNBBTC)"]'  
permissions| ENUM| No| 示例：curl -X GET "<https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT>"   
or   
curl -X GET "<https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D>"   
or   
curl -g -X GET '[https://api.binance.com/api/v3/exchangeInfo?permissions=["MARGIN","LEVERAGED](https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22,%22LEVERAGED)"]'  
showPermissionSets| BOOLEAN| No| 用于控制是否提供 `permissionSets` 字段的内容。默认为 `true`  
symbolStatus| ENUM| No| 用于过滤具有此 `tradingStatus` 的交易对。有效值： `TRADING`， `HALT`， `BREAK`   
不能与 `symbols` 或 `symbol` 组合使用。  
  
**备注** :

  * 如果参数 `symbol` 或者 `symbols` 提供的交易对不存在, 系统会返回错误并提示交易对不正确。
  * 所有的参数都是可选的。
  * `permissions` 可以支持单个或多个值（例如 `SPOT`, `["MARGIN","LEVERAGED"]`）。此参数不能与 `symbol` 或 `symbols` 组合使用。
  * 如果未提供 `permissions` 参数，那么所有具有 `SPOT`、`MARGIN` 或 `LEVERAGED` 权限的交易对都将被返回。 
    * 要显示具有任何权限的交易对，您需要在 `permissions` 中明确指定它们：（例如 `["SPOT","MARGIN",...]`)。有关完整列表，请参阅 [可用权限](/docs/zh-CN/binance-spot-api-docs/enums#account-and-symbol-permissions)



**解释响应中的`permissionSets`：**

  * `[["A","B"]]` \- 有权限"A"**或** 权限"B"的账户可以下订单。
  * `[["A"],["B"]]` \- 有权限"A"**和** 权限"B"的账户可以下订单。
  * `[["A"],["B","C"]]` \- 有权限"A"**和** 权限"B"或权限"C"的账户可以下订单。（此处应用的是包含或，而不是排除或，因此账户可以同时拥有权限"B"和权限"C"。）



**数据源:** 缓存

**响应:**
    
    
    {  
        "timezone": "UTC",  
        "serverTime": 1508631584636,  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUESTS_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 1200       // 每分钟调用的所有接口权重之和不得超过1200  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 1,  
                "limit": 10         // 每秒钟所有订单/撤单次数不得超过10  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 100000     // 每天订单/撤单不得超过10万  
            },  
            {  
                "rateLimitType": "RAW_REQUESTS",  
                "interval": "MINUTE",  
                "intervalNum": 5,  
                "limit": 5000       // 每5分钟调用订单次数不得超过5000  
            }  
        ],  
        "exchangeFilters": [],  
        "symbols": [  
            {  
                "symbol": "ETHBTC",  
                "status": "TRADING",  
                "baseAsset": "ETH",  
                "baseAssetPrecision": 8,  
                "quoteAsset": "BTC",  
                "quotePrecision": 8,  
                "quoteAssetPrecision": 8,  
                "baseCommissionPrecision": 8,  
                "quoteCommissionPrecision": 8,  
                "orderTypes": ["LIMIT", "MARKET"],  
                "icebergAllowed": false,  
                "ocoAllowed": true,  
                "otoAllowed": true,  
                "opoAllowed": true,  
                "quoteOrderQtyMarketAllowed": true,  
                "allowTrailingStop": false,  
                "cancelReplaceAllowed": false,  
                "amendAllowed": false,  
                "pegInstructionsAllowed": true,  
                "isSpotTradingAllowed": true,  
                "isMarginTradingAllowed": true,  
                "filters": [  
                    // 这些在“过滤器”部分定义。  
                    // 所有过滤器均为可选  
                ],  
                "permissions": [],  
                "permissionSets": [["SPOT", "MARGIN"]],  
                "defaultSelfTradePreventionMode": "NONE",  
                "allowedSelfTradePreventionModes": ["NONE"]  
            }  
        ],  
        // 可选字段，仅当 SOR 可用时才会被显示出来。  
        // https://github.com/binance/binance-spot-api-docs/blob/master/faqs/sor_faq_CN.md  
        "sors": [  
            {  
                "baseAsset": "BTC",  
                "symbols": ["BTCUSDT", "BTCUSDC"]  
            }  
        ]  
    }  
    

### 查询执行规则[​](/docs/zh-CN/binance-spot-api-docs/rest-api/general-endpoints#查询执行规则 "查询执行规则的直接链接")
    
    
    GET /api/v3/executionRules  
    

**权重:**

限制| 权重  
---|---  
`symbol`| 2  
`symbols`| 权重为 2，最多支持 40  
`symbolStatus`| 40  
None| 40  
  
**参数:**

名称| 类型| 是否必须| 描述  
---|---|---|---  
`symbol`| STRING| No| 查询指定的交易对  
`symbols`| STRING| No| 查询多个交易对  
`symbolStatus`| ENUM| 查询指定状态的所有交易对  
支持的值：`TRADING`（正常交易中）、`HALT`（交易终止）、BREAK（交易暂停)|   
  
**注意：** 不允许多个参数组合使用。

**数据源：** 缓存

**响应：**
    
    
    {  
        "symbolRules": [  
            {  
                "symbol": "BAZUSD",  
                "rules": [  
                    {  
                        "ruleType": "PRICE_RANGE",  
                        "bidLimitMultUp": "1.0001",  
                        "bidLimitMultDown": "0.9999",  
                        "askLimitMultUp": "1.0001",  
                        "askLimitMultDown": "0.9999"  
                    }  
                ]  
            }  
        ]  
    }