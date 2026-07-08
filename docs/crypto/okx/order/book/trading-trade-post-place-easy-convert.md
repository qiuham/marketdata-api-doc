---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-place-easy-convert
anchor_id: order-book-trading-trade-post-place-easy-convert
api_type: API
updated_at: 2026-07-08 19:27:23.988654
---

# POST / Place easy convert

Convert small currencies to mainstream currencies.   
  
#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/easy-convert`

> Request Example
    
    
    POST /api/v5/trade/easy-convert
    body
    {
        "fromCcy": ["ADA","USDC"], //Seperated by commas
        "toCcy": "OKB" 
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Convert small currencies to mainstream currencies
    result = tradeAPI.easy_convert(
        fromCcy=["ADA", "USDC"],
        toCcy="OKB"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
fromCcy | Array of strings | Yes | Type of small payment currency convert from   
Maximum 5 currencies can be selected in one order. If there are multiple currencies, separate them with commas.  
toCcy | String | Yes | Type of mainstream currency convert to   
Only one receiving currency type can be selected in one order and cannot be the same as the small payment currencies.  
source | String | No | Funding source  
`1`: Trading account  
`2`: Funding account  
The default is `1`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fillFromSz": "6.5807127",
                "fillToSz": "0.17171580105126",
                "fromCcy": "ADA",
                "status": "running",
                "toCcy": "OKB",
                "uTime": "1661419684687"
            },
            {
                "fillFromSz": "2.997",
                "fillToSz": "0.1683755161661844",
                "fromCcy": "USDC",
                "status": "running",
                "toCcy": "OKB",
                "uTime": "1661419684687"
            }
        ],
        "msg": ""
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
status | String | Current status of easy convert   
`running`: Running   
`filled`: Filled   
`failed`: Failed  
fromCcy | String | Type of small payment currency convert from  
toCcy | String | Type of mainstream currency convert to  
fillFromSz | String | Filled amount of small payment currency convert from  
fillToSz | String | Filled amount of mainstream currency convert to  
uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085

---

# POST / 一键兑换主流币交易

进行小币一键兑换主流币交易。  
  
#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/trade/easy-convert`

> 请求示例
    
    
    POST /api/v5/trade/easy-convert
    body
    {
        "fromCcy": ["ADA","USDC"], //逗号分隔小币
        "toCcy": "OKB" 
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 进行小币一键兑换主流币交易
    result = tradeAPI.easy_convert(
        fromCcy=["ADA", "USDC"],
        toCcy="OKB"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
fromCcy | Array of strings | 是 | 小币支付币种   
单次最多同时选择5个币种，如有多个币种则用逗号隔开  
toCcy | String | 是 | 兑换的主流币   
只选择一个币种，且不能和小币支付币种重复  
source | String | 否 | 资金来源  
`1`：交易账户  
`2`：资金账户  
默认为`1`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fillFromSz": "6.5807127",
                "fillToSz": "0.17171580105126",
                "fromCcy": "ADA",
                "status": "running",
                "toCcy": "OKB",
                "uTime": "1661419684687"
            },
            {
                "fillFromSz": "2.997",
                "fillToSz": "0.1683755161661844",
                "fromCcy": "USDC",
                "status": "running",
                "toCcy": "OKB",
                "uTime": "1661419684687"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
status | String | 当前兑换进度/状态   
`running`: 进行中   
`filled`: 已完成   
`failed`: 失败  
fromCcy | String | 小币支付币种  
toCcy | String | 兑换的主流币  
fillFromSz | String | 小币偿还币种支付数量  
fillToSz | String | 兑换的主流币成交数量  
uTime | String | 交易时间戳，Unix时间戳为毫秒数格式，如 1597026383085