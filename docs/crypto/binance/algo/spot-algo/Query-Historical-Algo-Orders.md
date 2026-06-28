---
exchange: binance
source_url: https://developers.binance.com/docs/algo/spot-algo/Query-Historical-Algo-Orders
api_type: REST
updated_at: 2026-05-27 18:58:35.952894
---

# Query Sub Orders(USER_DATA)

## API Description[​](/docs/algo/spot-algo/Query-Sub-Orders#api-description "Direct link to API Description")

Get respective sub orders for a specified algoId

## HTTP Request[​](/docs/algo/spot-algo/Query-Sub-Orders#http-request "Direct link to HTTP Request")

GET `/sapi/v1/algo/spot/subOrders`

## Request Weight(IP)[​](/docs/algo/spot-algo/Query-Sub-Orders#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/algo/spot-algo/Query-Sub-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
algoId| LONG| YES|   
page| INT| NO| Default is 1  
pageSize| INT| NO| MIN 1, MAX 100; Default 100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/algo/spot-algo/Query-Sub-Orders#response-example "Direct link to Response Example")
    
    
    {  
        "total": 1,  
        "executedQty": "1.000",  
        "executedAmt": "3229.44000000",  
        "subOrders": [  
            {  
                "algoId": 13723,  
                "orderId": 8389765519993908929,  
                "orderStatus": "FILLED",  
                "executedQty": "1.000",  
                "executedAmt": "3229.44000000",  
                "feeAmt": "-1.61471999",  
                "feeAsset": "USDT",  
                "bookTime": 1649319001964,  
                "avgPrice": "3229.44",  
                "side": "SELL",  
                "symbol": "ETHUSDT",  
                "subId": 1,  
                "timeInForce": "IMMEDIATE_OR_CANCEL",  
                "origQty": "1.000"  
            }  
        ]  
    }

---

# 查询执行子订单(USER_DATA)

## 接口描述[​](/docs/zh-CN/algo/spot-algo/Query-Sub-Orders#接口描述 "接口描述的直接链接")

获取指定 algoId 的相应子订单

## HTTP请求[​](/docs/zh-CN/algo/spot-algo/Query-Sub-Orders#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/algo/spot/subOrders`

## 请求权重[​](/docs/zh-CN/algo/spot-algo/Query-Sub-Orders#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/algo/spot-algo/Query-Sub-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
algoId| LONG| YES|   
page| INT| NO| 默认1  
pageSize| INT| NO| 最小 1， 最大 100; 默认 100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/algo/spot-algo/Query-Sub-Orders#响应示例 "响应示例的直接链接")
    
    
    {  
        "total": 1,  
        "executedQty": "1.000",  
        "executedAmt": "3229.44000000",  
        "subOrders": [  
            {  
                "algoId": 13723,    //策略订单ID  
                "orderId": 8389765519993908929,  //子订单ID  
                "orderStatus": "FILLED",         //子订单状态  
                "executedQty": "1.000",          //执行数量  
                "executedAmt": "3229.44000000",  //执行价值  
                "feeAmt": "-1.61471999",         //手续费  
                "feeAsset": "USDT",              //手续费币种  
                "bookTime": 1649319001964,       //下单时间  
                "avgPrice": "3229.44",           //平均价格  
                "side": "SELL",                  //买卖方向  
                "symbol": "ETHUSDT",             //交易对  
                "subId": 1,                      //子订单执行顺序ID  
                "timeInForce": "IMMEDIATE_OR_CANCEL",  //有效方式  
                "origQty": "1.000"              //原始委托数量  
            }  
        ]  
    }