---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/broker/exchange-broker/rate-limit/introduction
api_type: REST
updated_at: 2026-11-13 19:22:12.895546
---

# Introduction

## API Rate Limit For Exchange Broker Client

By default, all accounts under the Exchange Broker entity are subject to the default API rate limits. If you have special requirements based on your business needs, please contact your **account manager** to apply for a higher Exchange Broker–level cap and subaccount UID caps. Once approved, you will be able to allocate the rate limit quota across each subaccount accordingly.

instructions for API rate limit

  * All of the existing subaccounts still have their original API rate limits.
  * The default API rate limit for a new subaccount is not counted in the eb-level API rate limit. 
  * If the aggregate eb-level API rate limit is exceeded, you must reduce one or several account's API rate limit(s) first. After the API rate limit is less than the aggregate eb API rate limit cap, you can increase the API rate limit of an account.



## Default Rate limit

| Unified Account  
---|---  
Level\Product| **Futures**| **Option**| **Spot**  
Default| 10/s| 10/s| 20/s

---

# 限頻介紹

## 交易所經紀商API頻率規則

預設情況下，交易所經紀商（Exchange Broker）實體底下的所有帳戶都適用於標準的 API 速率限制。 若您基於業務需求有特殊要求，請聯繫您的**客戶經理** （Account Manager） 申請更高的 Exchange Broker 層級上限以及子帳戶 UID 的速率限制上限。審核通過後，您即可依需求將速率限制配額分配至各個子帳戶。

信息

  * 所有現有子帳戶仍享有原有的 API 速率限制。
  * 新子帳戶的預設 API 速率限制不計入EB API 速率限制總配額。
  * 如果超出EB API 速率限制總配額，您只能先降低帳戶的 API 速率限制。當 API 速率限制總配額低於機構 API 速率限制總配額後，您才能提高帳戶的 API 速率限制。



## UID默認頻率

| 統一帳戶  
---|---  
Level\Product| **期貨**| **期權**| **現貨**  
默認| 10/s| 10/s| 20/s