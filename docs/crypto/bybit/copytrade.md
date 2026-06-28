---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/copytrade
api_type: REST
updated_at: 2026-01-16T09:39:02.039810
---

# How To Start Copy Trading

## Become A Master Trader

Please go [here](https://www.bybit.com/copyTrade/) to apply to become a Master Trader

## Create The API KEY

"Contract - Orders & Positions" are mandatory permissions for Copy Trading orders

## Understand The Scope

From time being copy trading accounts can only trade USDT Perpetual symbols. Please check the field `copyTrading` from [Get Instruments Info](/docs/v5/market/instrument)

## Place The Copy Trading Order

Use V5 [Place Order](/docs/v5/order/create-order) endpoint to place a Copy Trading order
    
    
    POST /v5/order/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1698376189371  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 207  
      
    {  
        "symbol": "BTCUSDT",  
        "side": "Buy",  
        "orderType": "Limit",  
        "category": "linear",  
        "qty": "0.1",  
        "price": "29000",  
        "timeInForce": "GTC",  
        "positionIdx": 1  
    }

---

# 如何使用API帶單

## 成為交易達人

請前往[這裡](https://www.bybit.com/copyTrade/)申請成為交易達人

## 創建API KEY

"合約 - 訂單 持倉"是跟單交易的必選權限項

## 支持範圍

目前, 統一帳戶支持跟單交易, 但是只能交易部分USDT永續合約對. 請通過該[查詢可交易產品的規格信息](/docs/zh-TW/v5/market/instrument)接口, 檢查其中的`copyTrading`字段, 來了解 支持的具體交易對

## 下單示例

使用V5[創建訂單](/docs/zh-TW/v5/order/create-order)接口來創建一個帶單
    
    
    POST /v5/order/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1698376189371  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 207  
      
    {  
        "symbol": "BTCUSDT",  
        "side": "Buy",  
        "orderType": "Limit",  
        "category": "linear",  
        "qty": "0.1",  
        "price": "29000",  
        "timeInForce": "GTC",  
        "positionIdx": 1  
    }