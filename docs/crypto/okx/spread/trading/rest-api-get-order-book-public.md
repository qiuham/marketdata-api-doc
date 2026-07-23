---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-rest-api-get-order-book-public
anchor_id: spread-trading-rest-api-get-order-book-public
api_type: REST
updated_at: 2026-07-23 19:22:23.111326
---

# Get order book (Public)

Retrieve the order book of the spread.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/sprd/books`

> Request Example
    
    
    GET /api/v5/sprd/books?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get order book
    result = spreadAPI.get_order_book(sprdId="BTC-USDT_BTC-USDT-SWAP", sz=20)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USDT-SWAP  
sz | String | No | Order book depth per side. Maximum value is 400. Default value is 5.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8", // price
                        "0.60038921", // quantity
                        "1" // number of orders at the price
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "2"
                    ]
                ],
                "ts": "1629966436396"
            }
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
asks | Array of arrays | Order book on sell side  
bids | Array of arrays | Order book on buy side  
ts | String | Order book generation time  
An example of the array of asks and bids values: ["411.8", "10", "4"]  
\- "411.8" is the depth price  
\- "10" is the quantity at the price (Unit: szCcy)  
\- "4" is the number of orders at the price.

---

# 获取Spread产品深度（公共）

获取Spread产品深度列表  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/sprd/books`

> 请求示例
    
    
    GET /api/v5/sprd/books?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取深度
    result = spreadAPI.get_order_book(sprdId="BTC-USDT_BTC-USDT-SWAP", sz=20)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 是 | spread ID，如BTC-USDT_BTC-USDT-SWAP  
sz | String | 否 | 深度档位数量。最大值为400。默认值为5。  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8", // 价格
                        "0.60038921", // 数量
                        "1" // 此价格上订单数量
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "2"
                    ]
                ],
                "ts": "1629966436396"
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
asks | Array of Arrays | 卖方深度  
bids | Array of Arrays | 买方深度  
ts | String | 深度产生的时间  
asks和bids值数组举例说明： ["411.8", "10", "4"]   
\- 411.8为深度价格   
\- 10为此价格的数量 (单位为szCcy）  
\- 4为此价格的订单数量