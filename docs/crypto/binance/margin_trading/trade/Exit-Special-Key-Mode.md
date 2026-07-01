---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Exit-Special-Key-Mode
api_type: Trading
updated_at: 2026-07-01 19:09:09.043730
---

# Exit Special Key Mode (TRADE)

## Description[​](/docs/margin_trading/trade/Exit-Special-Key-Mode#description "Direct link to Description")

Exit the Margin Special Key mode for Cross Margin Classic accounts.

**All outstanding liabilities under the Cross Margin Classic account must be fully repaid before calling this endpoint.** Deleting the Margin Special Key alone does not constitute a valid exit.

When a user creates a Margin Special API Key, the account enters "Special Key Mode". Upon a successful request, the following actions will be performed atomically:

  1. All existing Margin Special API Keys under the Cross Margin Classic mode account will be deleted.
  2. All pre-execution margin checks (including Open-order-loss calculation) will revert to standard mode.
  3. A cooldown period (default: 24 hours) will be enforced, during which the account will not be permitted to create new Margin Special API Keys.



For more information, please refer to [FAQ](https://www.binance.com/en/support/faq/detail/3208663e900d4d2e9fec4140e1832f4e).

## HTTP Request[​](/docs/margin_trading/trade/Exit-Special-Key-Mode#http-request "Direct link to HTTP Request")

POST `/sapi/v1/margin/exit-special-key-mode`

## Request Weight[​](/docs/margin_trading/trade/Exit-Special-Key-Mode#request-weight "Direct link to Request Weight")

**10(UID)**

## Request Parameters[​](/docs/margin_trading/trade/Exit-Special-Key-Mode#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Preconditions[​](/docs/margin_trading/trade/Exit-Special-Key-Mode#preconditions "Direct link to Preconditions")

The following conditions must be met; otherwise the request will be rejected:

  * Account type must be **Cross Margin Classic**.
  * Account must currently be in **Special Key Mode**. If not, the request silently succeeds.
  * Account must **not be in liquidation**.
  * Account must **have no liability**.



## Response Example[​](/docs/margin_trading/trade/Exit-Special-Key-Mode#response-example "Direct link to Response Example")
    
    
    {}

---

# 退出Special Key模式 (TRADE)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Exit-Special-Key-Mode#接口描述 "接口描述的直接链接")

退出全仓杠杆账户经典模式的 Margin Special Key 模式。

**调用本接口前，须确保全仓杠杆账户经典模式下负债已全额还清。**请注意，仅删除 Margin Special Key 并不构成有效退出。

当用户创建 Margin Special Key 后，账户即进入"Margin Special Key 模式"。此接口请求成功后，将自动执行以下操作：

  1. 全仓杠杆账户经典模式下的所有 Margin Special Key 将被删除。
  2. 所有操作前的保证金检查（包括开仓亏损计算）将恢复为标准模式。
  3. 将执行冷却期（默认：24 小时），冷却期内账户不得创建新的 Margin Special Key。



更多信息请参考 [FAQ](https://www.binance.com/zh-CN/support/faq/detail/3208663e900d4d2e9fec4140e1832f4e)。

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Exit-Special-Key-Mode#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/margin/exit-special-key-mode`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Exit-Special-Key-Mode#请求权重 "请求权重的直接链接")

**10(UID)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Exit-Special-Key-Mode#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 前置条件[​](/docs/zh-CN/margin_trading/trade/Exit-Special-Key-Mode#前置条件 "前置条件的直接链接")

请求需满足以下条件，否则将被拒绝：

  * 账户类型必须为**全仓经典(Cross Margin Classic)** 。
  * 账户必须当前处于 **Special Key 模式** 。如不在该模式下，请求将静默成功。
  * 账户**不能处于强制平仓中** 。
  * 账户**不能有负债** 。



## 响应示例[​](/docs/zh-CN/margin_trading/trade/Exit-Special-Key-Mode#响应示例 "响应示例的直接链接")
    
    
    {}