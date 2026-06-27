---
exchange: binance
source_url: https://developers.binance.com/docs/algo/spot-algo/Query-Current-Algo-Open-Orders
api_type: REST
updated_at: 2026-05-27 18:58:33.308583
---

# Query Current Algo Open Orders(USER_DATA)

## API Description[​](/docs/algo/spot-algo/Query-Current-Algo-Open-Orders#api-description "Direct link to API Description")

Get all open SPOT TWAP orders

## HTTP Request[​](/docs/algo/spot-algo/Query-Current-Algo-Open-Orders#http-request "Direct link to HTTP Request")

GET `/sapi/v1/algo/spot/openOrders`

## Request Weight(IP)[​](/docs/algo/spot-algo/Query-Current-Algo-Open-Orders#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/algo/spot-algo/Query-Current-Algo-Open-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/algo/spot-algo/Query-Current-Algo-Open-Orders#response-example "Direct link to Response Example")
    
    
    {  
        "total": 1,  
        "orders": [  
            {  
                "algoId": 14517,  
                "symbol": "ETHUSDT",  
                "side": "SELL",  
                "totalQty": "5.000",  
                "executedQty": "0.000",  
                "executedAmt": "0.00000000",  
                "avgPrice": "0.00",  
                "clientAlgoId": "d7096549481642f8a0bb69e9e2e31f2e",  
                "bookTime": 1649756817004,  
                "endTime": 0,  
                "algoStatus": "WORKING",  
                "algoType": "TWAP",  
                "urgency": "LOW"  
            }  
        ]  
    }

---

# 查询当前策略订单挂单(USER_DATA)

## 接口描述[​](/docs/zh-CN/algo/spot-algo/Query-Current-Algo-Open-Orders#接口描述 "接口描述的直接链接")

查询当前策略订单挂单

## HTTP请求[​](/docs/zh-CN/algo/spot-algo/Query-Current-Algo-Open-Orders#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/algo/spot/openOrders`

## 请求权重(IP)[​](/docs/zh-CN/algo/spot-algo/Query-Current-Algo-Open-Orders#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/algo/spot-algo/Query-Current-Algo-Open-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/algo/spot-algo/Query-Current-Algo-Open-Orders#响应示例 "响应示例的直接链接")
    
    
    {  
        "total": 1,  
        "orders": [  
            {   
                "algoId": 14517,      //策略订单ID  
                "symbol": "ETHUSDT",  //交易对  
                "side": "SELL",       //买卖方向  
                "totalQty": "5.000",     //总共下单数量  
                "executedQty": "0.000",  //执行数量  
                "executedAmt": "0.00000000",   //执行价值  
                "avgPrice": "0.00",            //平均价格  
                "clientAlgoId": "d7096549481642f8a0bb69e9e2e31f2e",  //用户自定义策略订单ID  
                "bookTime": 1649756817004,     //用户下单时间   
                "endTime": 0,                  //结束时间  
                "algoStatus": "WORKING",       //策略订单状态  
                "algoType": "VP",              //策略订单类型  
                "urgency": "LOW"               //执行速率  
            }  
        ]  
    }