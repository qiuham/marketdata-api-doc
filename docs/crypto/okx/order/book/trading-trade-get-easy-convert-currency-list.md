---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-easy-convert-currency-list
anchor_id: order-book-trading-trade-get-easy-convert-currency-list
api_type: API
updated_at: 2026-07-07 19:41:43.932881
---

# GET / Easy convert currency list

Get list of small convertibles and mainstream currencies. Only applicable to the crypto balance less than $10.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/easy-convert-currency-list`

> Request Example
    
    
    GET /api/v5/trade/easy-convert-currency-list
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get list of small convertibles and mainstream currencies
    result = tradeAPI.get_easy_convert_currency_list()
    print(result)
    

#### Request Parameters

Parameters | Type | Required | Description  
---|---|---|---  
source | String | No | Funding source  
`1`: Trading account  
`2`: Funding account  
The default is `1`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fromData": [
                    {
                        "fromAmt": "6.580712708344864",
                        "fromCcy": "ADA"
                    },
                    {
                        "fromAmt": "2.9970000013055097",
                        "fromCcy": "USDC"
                    }
                ],
                "toCcy": [
                    "USDT",
                    "BTC",
                    "ETH",
                    "OKB"
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fromData | Array of objects | Currently owned and convertible small currency list  
> fromCcy | String | Type of small payment currency convert from, e.g. `BTC`  
> fromAmt | String | Amount of small payment currency convert from  
toCcy | Array of strings | Type of mainstream currency convert to, e.g. `USDT`

---

# GET / 获取一键兑换主流币币种列表

获取小币一键兑换主流币币种列表。仅可兑换余额在 $10 以下币种。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/easy-convert-currency-list`

> 请求示例
    
    
    GET /api/v5/trade/easy-convert-currency-list
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取小币一键兑换主流币币种列表
    result = tradeAPI.get_easy_convert_currency_list()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
source | String | 否 | 资金来源  
`1`：交易账户  
`2`：资金账户  
默认为`1`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fromData": [
                    {
                        "fromAmt": "6.580712708344864",
                        "fromCcy": "ADA"
                    },
                    {
                        "fromAmt": "2.9970000013055097",
                        "fromCcy": "USDC"
                    }
                ],
                "toCcy": [
                    "USDT",
                    "BTC",
                    "ETH",
                    "OKB"
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
fromData | Array of objects | 当前拥有并可兑换的小币币种列表信息  
> fromCcy | String | 可兑换币种  
> fromAmt | String | 可兑换币种数量  
toCcy | Array of strings | 可转换成的主流币币种列表