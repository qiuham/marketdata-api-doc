---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change
api_type: REST
updated_at: 2026-01-15T23:43:24.008205
---

# Event: Risk level change

## Event Description[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#event-description "Direct link to Event Description")

  * Updates whenever there is an account risk level change. The following are possibly values: 
    * NORMAL
    * REDUCE_ONLY
  * Note: Risk level changes are only applicable to VIP and Market Makers user accounts. VIP and certain Market Maker accounts will be automatically placed into REDUCE_ONLY mode if their margin balance is insufficient to meet their maintenance margin obligations. Once in REDUCE_ONLY mode, the system will re-evaluate the risk level only upon the following events: 
    * Funds transfer
    * Trade fill
    * Option expiry



## URL PATH[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#url-path "Direct link to URL PATH")

`/private`

## Event Name[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#event-name "Direct link to Event Name")

`RISK_LEVEL_CHANGE`

## Update Speed[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#update-speed "Direct link to Update Speed")

**50ms**

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#response-example "Direct link to Response Example")
    
    
    {   
        "e":"RISK_LEVEL_CHANGE", //Event Type   
        "E":1587727187525, //Event Time   
        "s":"REDUCE_ONLY", //risk level  
        "mb":"1534.11708371", //margin balance   
        "mm":"254789.11708371" //maintenance margin   
    }

---

# 追加保证金通知

## 事件描述[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Risk-level-change#事件描述 "事件描述的直接链接")

  * 每当账户风险等级发生变化时进行更新。以下是可能的状态：

    * NORMAL
    * REDUCE_ONLY
  * 需要注意的是，风险等级变化仅适用于VIP和市场做市商用户帐户。如果VIP和某些市场做市商账户的保证金余额不足以满足其维持保证金义务，系统将自动将其风险等级更改为仅减少模式（REDUCE_ONLY）。一旦风险等级被设置为仅减少模式（REDUCE_ONLY），系统将在以下事件发生时重新评估风险等级：

    * 资金转账
    * 成交填充
    * 期权到期



## URL PATH[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Risk-level-change#url-path "URL PATH的直接链接")

`/private`

## 事件类型[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Risk-level-change#事件类型 "事件类型的直接链接")

`RISK_LEVEL_CHANGE`

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Risk-level-change#更新速度 "更新速度的直接链接")

**50ms**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Risk-level-change#响应示例 "响应示例的直接链接")
    
    
    {  
        "e":"RISK_LEVEL_CHANGE", //事件类型    
        "E":1587727187525,       //事件时间  
        "s":"REDUCE_ONLY",       //风险等级  
        "mb":"1534.11708371",    //保证金余额  
        "mm":"254789.11708371"   //维持保证金  
    }