---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Trade-Lite
api_type: Trading
updated_at: 2026-01-15T23:47:45.990280
---

# Event: Trade Lite Update

## Event Description[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Trade-Lite#event-description "Direct link to Event Description")

Fast trade stream reduces data latency compared original `ORDER_TRADE_UPDATE` stream. However, it only pushes TRADE Execution Type, and fewer data fields.

## Event Name[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Trade-Lite#event-name "Direct link to Event Name")

`TRADE_LITE`

## Response Example[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Trade-Lite#response-example "Direct link to Response Example")
    
    
    {  
      "e":"TRADE_LITE",             // Event Type  
      "E":1721895408092,            // Event Time  
      "T":1721895408214,            // Transaction Time                            
      "s":"BTCUSDT",                // Symbol  
      "q":"0.001",                  // Original Quantity  
      "p":"0",                      // Original Price  
      "m":false,                    // Is this trade the maker side?  
      "c":"z8hcUoOsqEdKMeKPSABslD", // Client Order Id  
          // special client order id:  
          // starts with "autoclose-": liquidation order  
          // "adl_autoclose": ADL auto close order  
          // "settlement_autoclose-": settlement order for delisting or delivery  
      "S":"BUY",                   // Side  
      "L":"64089.20",              // Last Filled Price  
      "l":"0.040",                 // Order Last Filled Quantity  
      "t":109100866,               // Trade Id  
      "i":8886774,                // Order Id  
    }

---

# 精简交易推送

精简交易推送相比原有的`ORDER_TRADE_UPDATE`流减少了数据延迟，但该交易推送仅推送和交易相关的字段。

## 事件类型[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Trade-Lite#事件类型 "事件类型的直接链接")

`TRADE_LITE`

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Trade-Lite#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"TRADE_LITE",             // 事件类型  
      "E":1721895408092,            // 事件时间  
      "T":1721895408214,            // 交易时间  
      "s":"BTCUSDT",                // 交易对  
      "q":"0.001",                  // 订单原始数量  
      "p":"0",                      // 订单原始价格  
      "m":false,                    // 该成交是作为挂单成交吗？  
      "c":"z8hcUoOsqEdKMeKPSABslD", // 客户端自定订单ID  
          // 特殊的自定义订单ID:  
          // "autoclose-"开头的字符串: 系统强平订单  
          // "adl_autoclose": ADL自动减仓订单  
          // "settlement_autoclose-": 下架或交割的结算订单  
      "S":"BUY",                    // 订单方向  
      "L":"64089.20",               // 订单末次成交价格  
      "l":"0.040",                  // 订单末次成交量  
      "t":109100866,                // 成交ID  
      "i":8886774,                  // 订单ID  
    }