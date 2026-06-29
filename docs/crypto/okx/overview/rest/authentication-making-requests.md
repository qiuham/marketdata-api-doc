---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-rest-authentication-making-requests
anchor_id: overview-rest-authentication-making-requests
api_type: REST
updated_at: 2026-06-29 19:55:20.132566
---

# Making Requests

All private REST requests must contain the following headers:

  * `OK-ACCESS-KEY` The API key as a String.

  * `OK-ACCESS-SIGN` The Base64-encoded signature (see Signing Messages subsection for details).

  * `OK-ACCESS-TIMESTAMP` Request timestamp in ISO 8601 UTC format with millisecond precision, e.g. `2020-12-08T09:08:57.715Z`. The server rejects requests where this differs from server time by more than 30 seconds (error 50102). Always use UTC — local timezone offset is the most common cause of error 50102. Synchronise with GET /api/v5/public/time before placing orders.

  * `OK-ACCESS-PASSPHRASE` The passphrase you specified when creating the API key.

Request bodies should have content type `application/json` and be in valid JSON format.

---

# 发起请求

所有REST私有请求头都必须包含以下内容：

  * `OK-ACCESS-KEY`字符串类型的APIKey。

  * `OK-ACCESS-SIGN`使用HMAC SHA256哈希函数获得哈希值，再使用Base-64编码（请参阅签名）。

  * `OK-ACCESS-TIMESTAMP` 请求时间戳，ISO 8601 UTC格式，精确到毫秒，如：`2020-12-08T09:08:57.715Z`。服务器将拒绝与服务器时间相差超过30秒的请求（错误码50102）。请务必使用UTC时间——时区偏差是导致50102错误最常见的原因。建议在下单前通过 GET /api/v5/public/time 与服务器时间同步。

  * `OK-ACCESS-PASSPHRASE`您在创建API密钥时指定的Passphrase。

所有请求都应该含有application/json类型内容，并且是有效的JSON。