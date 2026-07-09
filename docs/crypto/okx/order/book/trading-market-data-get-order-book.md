---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book
anchor_id: order-book-trading-market-data-get-order-book
api_type: API
updated_at: 2026-07-09 19:37:37.486110
---

# GET / Order book

Retrieve order book of the instrument. The data will be updated once every 50 milliseconds. Best ask price may be lower than the best bid price during the pre-open period.  
This endpoint does not return data immediately. Instead, it returns the latest data once the server-side cache has been updated.  
  
#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/books`

> Request Example
    
    
    GET /api/v5/market/books?instId=BTC-USDT
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve order book of the instrument
    result = marketDataAPI.get_orderbook(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
sz | String | No | Order book depth per side. Maximum 400, e.g. 400 bids + 400 asks   
Default returns to `1` depth data  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8",
                        "0.60038921",
                        "0",
                        "1"
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "0",
                        "2"
                    ]
                ],
                "ts": "1629966436396",
                "seqId": 3235851742
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
asks | Array of Arrays | Order book on sell side  
bids | Array of Arrays | Order book on buy side  
ts | String | Order book generation time  
seqId | Integer | Sequence ID of the current message  
An example of the array of asks and bids values: ["411.8", "10", "0", "4"]  
\- "411.8" is the depth price  
\- "10" is the quantity at the price (number of contracts for derivatives, quantity in base currency for Spot and Spot Margin)  
\- "0" is part of a deprecated feature and it is always "0"  
\- "4" is the number of orders at the price.  
The order book data will be updated around once a second during the call auction.

---

# GET / 获取产品深度

获取产品深度列表，数据每 50 毫秒更新一次。在提前挂单阶段，best ask的价格有机会低于best bid。  
该接口收到请求后不会立刻返回，而是会待服务端缓存数据更新后立即返回最新数据。  
  
#### 限速：40次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/books`

> 请求示例
    
    
    GET /api/v5/market/books?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取产品深度
    result = marketDataAPI.get_orderbook(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
sz | String | 否 | 深度档位数量，最大值可传400，即买卖深度共800条   
不填写此参数，默认返回`1`档深度数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8",
                        "0.60038921",
                        "0",
                        "1"
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "0",
                        "2"
                    ]
                ],
                "ts": "1629966436396",
                "seqId": 3235851742
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
asks | Array of Arrays | 卖方深度  
bids | Array of Arrays | 买方深度  
ts | String | 深度产生的时间  
seqId | Integer | 当前消息的序列号  
合约的asks和bids值数组举例说明： ["411.8","10", "0","4"] 411.8为深度价格，10为此价格的合约张数，0该字段已弃用(始终为0)，4为此价格的订单数量  
现货/币币杠杆的asks和bids值数组举例说明： ["411.8","10", "0","4"] 411.8为深度价格，10为此价格的交易币的数量，0该字段已弃用(始终为0)，4为此价格的订单数量 asks和bids值数组举例说明： ["411.8", "10", "0", "4"]  
\- 411.8为深度价格  
\- 10为此价格的数量 （合约交易为张数，现货/币币杠杆为交易币的数量）  
\- 0该字段已弃用(始终为0)  
\- 4为此价格的订单数量  集合竞价期间，深度数据大约每秒更新一次