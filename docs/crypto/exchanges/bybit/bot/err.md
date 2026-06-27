---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/err
api_type: REST
updated_at: 2026-05-27 19:15:37.018351
---

# Bot Error Codes

HTTP-level error codes returned by the Bot APIs.

## Futures Combo Bot

Applies to: [Create](/docs/v5/bot/futures-combo/create), [Close](/docs/v5/bot/futures-combo/close), [Get Detail](/docs/v5/bot/futures-combo/get-detail), [Get Limit](/docs/v5/bot/futures-combo/get-limit)

error_code| error_msg| Applicable Endpoint(s)  
---|---|---  
400| Invalid request parameters| All  
401| Authentication required| All  
421| User group banned — `ban_reason_text` contains the localized reason| Create  
429| Rate limit exceeded| All  
  
* * *

## Futures Grid Bot

Applies to: [Create](/docs/v5/bot/futures-grid/create), [Close](/docs/v5/bot/futures-grid/close), [Get Detail](/docs/v5/bot/futures-grid/get-detail), [Validate Input](/docs/v5/bot/futures-grid/validate-input)

error_code| error_msg| Applicable Endpoint(s)  
---|---|---  
400| Invalid request parameters| All  
401| Authentication required| All  
421| User group banned — `ban_reason_text` contains the localized reason| Create  
429| Rate limit exceeded| All  
  
* * *

## Futures Martingale Bot

Applies to: [Create](/docs/v5/bot/futures-martingale/create), [Close](/docs/v5/bot/futures-martingale/close), [Get Detail](/docs/v5/bot/futures-martingale/get-detail), [Get Limit](/docs/v5/bot/futures-martingale/get-limit)

error_code| error_msg| Applicable Endpoint(s)  
---|---|---  
400| Invalid request parameters| All  
401| Authentication required| All  
421| User group banned — `ban_reason_text` contains the localized reason| Create  
429| Rate limit exceeded| All  
  
* * *

## DCA Bot

Applies to: [Create](/docs/v5/bot/dca/create), [Close](/docs/v5/bot/dca/close)

error_code| error_msg| Applicable Endpoint(s)  
---|---|---  
400| Invalid parameters (e.g., duplicated symbols, invalid frequency)| Create  
421| User is banned| Create  
503| Bot cannot be closed currently (investment cycle in progress)| Close  
  
* * *

## Spot Grid Bot

Applies to: [Create](/docs/v5/bot/spot-grid/create), [Close](/docs/v5/bot/spot-grid/close), [Get Detail](/docs/v5/bot/spot-grid/get-detail), [Validate Input](/docs/v5/bot/spot-grid/validate-input)

error_code| error_msg| Applicable Endpoint(s)  
---|---|---  
400| Invalid request parameters| Create, Validate Input  
401| Insufficient balance| Create  
404| Grid bot not found| Get Detail  
405| Grid cannot be cancelled (already in CANCELLING or COMPLETED state)| Close  
421| User is banned| Create

---

# 機器人錯誤碼

Bot API 返回的 HTTP 層級錯誤碼。

## 合約組合機器人（Futures Combo Bot）

適用端點：[創建](/docs/zh-TW/v5/bot/futures-combo/create)、[關閉](/docs/zh-TW/v5/bot/futures-combo/close)、[查詢詳情](/docs/zh-TW/v5/bot/futures-combo/get-detail)、[查詢限制參數](/docs/zh-TW/v5/bot/futures-combo/get-limit)

error_code| error_msg| 適用端點  
---|---|---  
400| Invalid request parameters（請求參數無效）| 所有  
401| Authentication required（需要身份驗證）| 所有  
421| User group banned — `ban_reason_text` contains the localized reason（用戶群組已被封禁 — `ban_reason_text` 包含本地化原因）| 創建  
429| Rate limit exceeded（超過頻率限制）| 所有  
  
* * *

## 合約網格機器人（Futures Grid Bot）

適用端點：[創建](/docs/zh-TW/v5/bot/futures-grid/create)、[關閉](/docs/zh-TW/v5/bot/futures-grid/close)、[查詢詳情](/docs/zh-TW/v5/bot/futures-grid/get-detail)、[驗證輸入](/docs/zh-TW/v5/bot/futures-grid/validate-input)

error_code| error_msg| 適用端點  
---|---|---  
400| Invalid request parameters（請求參數無效）| 所有  
401| Authentication required（需要身份驗證）| 所有  
421| User group banned — `ban_reason_text` contains the localized reason（用戶群組已被封禁 — `ban_reason_text` 包含本地化原因）| 創建  
429| Rate limit exceeded（超過頻率限制）| 所有  
  
* * *

## 合約馬丁格爾機器人（Futures Martingale Bot）

適用端點：[創建](/docs/zh-TW/v5/bot/futures-martingale/create)、[關閉](/docs/zh-TW/v5/bot/futures-martingale/close)、[查詢詳情](/docs/zh-TW/v5/bot/futures-martingale/get-detail)、[查詢限制參數](/docs/zh-TW/v5/bot/futures-martingale/get-limit)

error_code| error_msg| 適用端點  
---|---|---  
400| Invalid request parameters（請求參數無效）| 所有  
401| Authentication required（需要身份驗證）| 所有  
421| User group banned — `ban_reason_text` contains the localized reason（用戶群組已被封禁 — `ban_reason_text` 包含本地化原因）| 創建  
429| Rate limit exceeded（超過頻率限制）| 所有  
  
* * *

## 定投機器人（DCA Bot）

適用端點：[創建](/docs/zh-TW/v5/bot/dca/create)、[關閉](/docs/zh-TW/v5/bot/dca/close)

error_code| error_msg| 適用端點  
---|---|---  
400| Invalid parameters (e.g., duplicated symbols, invalid frequency)（參數無效，例如重複的交易對或無效的頻率）| 創建  
421| User is banned（用戶已被封禁）| 創建  
503| Bot cannot be closed currently (investment cycle in progress)（機器人當前無法關閉，投資週期進行中）| 關閉  
  
* * *

## 現貨網格機器人（Spot Grid Bot）

適用端點：[創建](/docs/zh-TW/v5/bot/spot-grid/create)、[關閉](/docs/zh-TW/v5/bot/spot-grid/close)、[查詢詳情](/docs/zh-TW/v5/bot/spot-grid/get-detail)、[驗證輸入](/docs/zh-TW/v5/bot/spot-grid/validate-input)

error_code| error_msg| 適用端點  
---|---|---  
400| Invalid request parameters（請求參數無效）| 創建、驗證輸入  
401| Insufficient balance（餘額不足）| 創建  
404| Grid bot not found（找不到網格機器人）| 查詢詳情  
405| Grid cannot be cancelled (already in CANCELLING or COMPLETED state)（網格無法取消，已處於取消中或已完成狀態）| 關閉  
421| User is banned（用戶已被封禁）| 創建