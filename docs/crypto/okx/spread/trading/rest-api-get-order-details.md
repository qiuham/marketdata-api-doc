---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-rest-api-get-order-details
anchor_id: spread-trading-rest-api-get-order-details
api_type: REST
updated_at: 2026-07-12 19:16:39.239719
---

# Get order details

Retrieve order details.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/order`

> Request Example
    
    
    GET /api/v5/sprd/order?ordId=2510789768709120
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get order details
    result = spreadAPI.get_order_details(ordId='1905309079888199680')
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used  
clOrdId | String | Conditional | Client Order ID as assigned by the client. The latest order will be returned.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "instId": "BTC-USD-200329",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price  
sz | String | Quantity to buy or sell  
ordType | String | Order type  
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
side | String | Order side  
fillSz | String | Last fill quantity  
fillPx | String | Last fill price  
tradeId | String | Last trade ID  
accFillSz | String | Accumulated fill quantity  
pendingFillSz | String | Live quantity  
pendingSettleSz | String | Quantity that's pending settlement  
canceledSz | String | Quantity canceled due order cancellations or trade rejections  
avgPx | String | Average filled price. If none is filled, it will return "0".  
state | String | State   
`canceled`   
`live`   
`partially_filled`   
`filled`  
cancelSource | String | Source of the order cancellation.Valid values and the corresponding meanings are:   
`0`: Order canceled by system   
`1`: Order canceled by user   
`14`: Order canceled: IOC order was partially canceled due to incompletely filled  
`15`: Order canceled: The order price is beyond the limit  
`20`: Cancel all after triggered   
`31`: The post-only order will take liquidity in maker orders  
`32`: Self trade prevention  
`34`: Order failed to settle due to insufficient margin   
`35`: Order cancellation due to insufficient margin from another order  
`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit.  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
Order sizes equation: pendingFillSz + canceledSz + accFillSz = sz

---

# 获取订单信息

查订单信息

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/order`

> 请求示例
    
    
    GET /api/v5/sprd/order?ordId=2510789768709120
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取订单详情
    result = spreadAPI.get_order_details(ordId='1905309079888199680')
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 可选 | 订单ID，`ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义ID，如果`clOrdId`关联了多个订单，只会返回最近的那笔订单  
  
> 返回示例
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "sprdId": "BTC-USD-SWAP_BTC-USD-200329",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | Spread ID  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格  
sz | String | 委托数量  
ordType | String | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
side | String | 订单方向  
fillSz | String | 最新成交数量  
fillPx | String | 最新成交价格  
tradeId | String | 最近成交ID  
accFillSz | String | 累计成交数量  
pendingFillSz | String | 待成交数量（包括待结算数量）  
pendingSettleSz | String | 待结算数量  
canceledSz | String | 被取消数量  
avgPx | String | 成交均价，如果成交数量为0，该字段为"0"  
state | String | 订单状态  
`canceled`：撤单成功  
`live`：等待成交  
`partially_filled`：部分成交  
`filled`：完全成交  
cancelSource | String | 撤单原因  
`0`: 系统撤单  
`1`: 用户撤单   
`14`: 已撤单：IOC 委托订单未完全成交，仅部分成交，导致部分挂单被撤回  
`15`: 已撤单：该订单委托价不在限价范围内  
`20`: 系统倒计时撤单   
`31`: 当前只挂单订单 (Post only) 将会吃掉挂单深度  
`32`: 自成交保护  
`34`: 订单结算失败因为保证金不足   
`35`: 撤单因为其他订单保证金不足  
`44`：由于该币种的可用余额不足，无法在触发自动换币后进行兑换，您的订单已撤销，撤销订单后恢复的余额将用于自动换币。当该币种的总抵押借贷量达到平台抵押借贷风控上限时，则会触发自动换币。  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式， 如 `1597026383085`  
订单数量等式: pendingFillSz + canceledSz + accFillSz = sz