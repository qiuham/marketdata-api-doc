---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/convert/guideline
api_type: REST
updated_at: 2026-11-13 19:21:34.385123
---

# Convert Guideline

info

  * All convert API endpoints need authentication
  * API key permission: "Exchange"



## Workflow

### Step 1: [Get Convert Coin List](/docs/v5/asset/convert/convert-coin-list)

  * Query the supported coin list of convert to/from in the different account types.
  * The balance is also given when querying the convert from coin list.



### Step 2: [Request a Quote](/docs/v5/asset/convert/apply-quote)

  * Select fromCoin, toCoin, acccountType, define the qty of fromCoin to get a quote
  * There is balance pre-check at this stage.



### Step 3: [Confirm a Quote](/docs/v5/asset/convert/confirm-quote)

  * Confirm your quote in the valid time slot (15 secs). Once confirmed, the system processes your transactions.
  * This operation is async, so it can be failed if you have funds transferred out. Please check the transaction result by step 4.



### Step 4: [Get Convert Status](/docs/v5/asset/convert/get-convert-result)

Check the final status of the coin convert.

## Error

Code| Msg| Comment  
---|---|---  
32024| exceeds exchange threshold| If the real-time exchange rate (comfirm quote) and quoted rate (apply quote) differ by more than 0.5%, your convert will be rejected/cancelled  
790000| system error, please try again later|   
700000| parameter error|   
700001| quote fail: no deler can be used|   
700002| quote fial: not support quote type| when requestCoin=toCoin during request quote stage  
700003| order status not allowed|   
700004| order does not exit| 1\. check if quoteTxId is correct; 2. check if quoteTxId is matched with accountType  
700005| Your available balance is insufficient or wallet does not exist|   
700006| Low amount limit| the request amount cannot be smaller than minFromCoinLimit  
700007| Large amount limit| the request amount cannot be larger than maxFromCoinLimit  
700008| quote fail: price time out| 1\. the quote is expired; 2. The quoteTxId does not exist  
700009| quoteTxId has already been used| get this error when you call confirm quote more than once before expiry time  
700010| INS loan user cannot perform conversion|   
700011| illegal operation| when request a quote with user A, but confirm the quote with user B  
  
## API Rate Limit

Method| Path| Limit| Upgradable  
---|---|---|---  
GET| /v5/asset/exchange/query-coin-list| 100 req/s| N  
POST| /v5/asset/exchange/quote-apply| 50 req/s| N  
POST| /v5/asset/exchange/convert-execute| 50 req/s| N  
GET| /v5/asset/exchange/convert-result-query| 100 req/s| N  
GET| /v5/asset/exchange/query-convert-history| 100 req/s| N

---

# 閃兌接入指南

信息

  * 所有接口都需要進行鑒權
  * API key的權限要求: "兌換"



## 流程

### Step1 [查詢兌換幣種列表](/docs/zh-TW/v5/asset/convert/convert-coin-list)

  * 查詢不同錢包內的支持的兌入兌出幣種列表
  * 當查詢兌出幣種列表時, 會有幣種餘額返回



### Step2 [申請報價](/docs/zh-TW/v5/asset/convert/apply-quote)

  * 選擇兌出幣種, 兌入幣種, 錢包類型, 設定號兌出幣種的數量來獲取報價
  * 該階段會核驗餘額



### Step3 [確認報價](/docs/zh-TW/v5/asset/convert/confirm-quote)

  * 在有效時間內確認報價 (15秒). 一旦確認, 系統會處理交易
  * 該操作環節是異步的, 所以當餘額被劃轉出去後, 最終兌換可能會失敗



### Step4 [查詢報價單狀態](/docs/zh-TW/v5/asset/convert/get-convert-result)

在確認報價後, 通過該接口查詢最終報價單的處理狀態

## 錯誤碼

錯誤碼| 消息| 備註  
---|---|---  
32024| exceeds exchange threshold| 當提交報價和確認報價時的兌換率滑點超過0.5%, 那麼確認報價會被拒絕  
790000| system error, please try again later| 系統繁忙  
700000| parameter error| 參數錯誤  
700001| quote fail: no deler can be used|   
700002| quote fial: not support quote type| 在提交報價時, requestCoin=兌入幣種, 會返回該錯誤  
700003| order status not allowed|   
700004| order does not exit| 1\. 檢查quoteTxId是否正確; 2. 檢查quoteTxId和accountType是否匹配  
700005| Your available balance is insufficient or wallet does not exist|   
700006| Low amount limit| 請求的數量小於minFromCoinLimit  
700007| Large amount limit| 請求的數量大於maxFromCoinLimit  
700008| quote fail: price time out| 1\. 報價單已經失效; 2.傳入quoteTxId不正確  
700009| quoteTxId has already been used| 在報價單有效期內, 同一個quoteTxId多次請求確認接口  
700010| INS loan user cannot perform conversion|   
700011| illegal operation| 當提交報價的是用戶A, 確認報價的是用戶B  
  
## API頻率

方法| 路徑| 頻率| 是否可提升  
---|---|---|---  
GET| /v5/asset/exchange/query-coin-list| 100 req/s| N  
POST| /v5/asset/exchange/quote-apply| 50 req/s| N  
POST| /v5/asset/exchange/convert-execute| 50 req/s| N  
GET| /v5/asset/exchange/convert-result-query| 100 req/s| N  
GET| /v5/asset/exchange/query-convert-history| 100 req/s| N