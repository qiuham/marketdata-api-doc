---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/websocket/public/trade
api_type: WebSocket
updated_at: 2026-07-08 19:04:50.120880
---

# Stop Strategy

Stop a running strategy. Once stopped, the strategy cannot be resumed.

**Effects upon stopping:**

  * Strategy status changes to `Terminated`
  * Unfilled orders are automatically canceled
  * Partially filled orders have their remaining quantity canceled
  * Already-filled orders are not affected



### HTTP Request

POST`/v5/strategy/stop`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
strategyId| **true**|  string| ID of the strategy to stop  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
strategyId| string| ID of the stopped strategy  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/strategy/stop HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773711467000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "strategyId": "119b6211-2611-461b-be5e-5ac557099e82"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "strategyId": "119b6211-2611-461b-be5e-5ac557099e82"  
        },  
        "retExtInfo": {},  
        "time": 1773711467052  
    }

---

# 停止策略

停止正在執行的策略。一旦停止，策略無法恢復。

**停止後效果：**

  * 策略狀態變更為 `Terminated`（已終止）
  * 未成交訂單自動取消
  * 部分成交訂單的剩餘數量取消
  * 已成交訂單不受影響



### HTTP 請求

POST`/v5/strategy/stop`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
strategyId| **true**|  string| 要停止的策略 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
strategyId| string| 已停止的策略 ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/strategy/stop HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773711467000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "strategyId": "119b6211-2611-461b-be5e-5ac557099e82"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "strategyId": "119b6211-2611-461b-be5e-5ac557099e82"  
        },  
        "retExtInfo": {},  
        "time": 1773711467052  
    }