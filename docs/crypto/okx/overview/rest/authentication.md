---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-rest-authentication
anchor_id: overview-rest-authentication
api_type: REST
updated_at: 2026-07-21 19:25:02.387522
---

# REST Authentication

### Making Requests

All private REST requests must contain the following headers:

  * `OK-ACCESS-KEY` The API key as a String.

  * `OK-ACCESS-SIGN` The Base64-encoded signature (see Signing Messages subsection for details).

  * `OK-ACCESS-TIMESTAMP` Request timestamp in ISO 8601 UTC format with millisecond precision, e.g. `2020-12-08T09:08:57.715Z`. The server rejects requests where this differs from server time by more than 30 seconds (error 50102). Always use UTC — local timezone offset is the most common cause of error 50102. Synchronise with GET /api/v5/public/time before placing orders.

  * `OK-ACCESS-PASSPHRASE` The passphrase you specified when creating the API key.

Request bodies should have content type `application/json` and be in valid JSON format.

### Signature

> Signing Messages

The `OK-ACCESS-SIGN` header is generated as follows:

  * Create a pre-hash string of timestamp + method + requestPath + body (where + represents String concatenation).
  * Prepare the SecretKey.
  * Sign the pre-hash string with the SecretKey using the HMAC SHA256.
  * Encode the signature in the Base64 format.

Example: `sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp + 'GET' + '/api/v5/account/balance?ccy=BTC', SecretKey))`

The `timestamp` value is the same as the `OK-ACCESS-TIMESTAMP` header with millisecond ISO format, e.g. `2020-12-08T09:08:57.715Z`.

The request method should be in UPPERCASE: e.g. `GET` and `POST`.

The `requestPath` is the path of requesting an endpoint.

Example: `/api/v5/account/balance`

The `body` refers to the String of the request body. It can be omitted if there is no request body (frequently the case for `GET` requests).

Example: `{"instId":"BTC-USDT","lever":"5","mgnMode":"isolated"}`

`GET` request parameters are counted as requestpath, not body 

The SecretKey is generated when you create an API key.

Example: `22582BD0CFF14C41EDBF1AB98506286D`

---

# REST 请求验证

### 发起请求 

所有REST私有请求头都必须包含以下内容：

  * `OK-ACCESS-KEY`字符串类型的APIKey。

  * `OK-ACCESS-SIGN`使用HMAC SHA256哈希函数获得哈希值，再使用Base-64编码（请参阅签名）。

  * `OK-ACCESS-TIMESTAMP` 请求时间戳，ISO 8601 UTC格式，精确到毫秒，如：`2020-12-08T09:08:57.715Z`。服务器将拒绝与服务器时间相差超过30秒的请求（错误码50102）。请务必使用UTC时间——时区偏差是导致50102错误最常见的原因。建议在下单前通过 GET /api/v5/public/time 与服务器时间同步。

  * `OK-ACCESS-PASSPHRASE`您在创建API密钥时指定的Passphrase。

所有请求都应该含有application/json类型内容，并且是有效的JSON。

### 签名 

> 生成签名

`OK-ACCESS-SIGN`的请求头是对`timestamp + method + requestPath + body`字符串（+表示字符串连接），以及SecretKey，使用HMAC SHA256方法加密，通过Base-64编码输出而得到的。

如：`sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp + 'GET' + '/api/v5/account/balance?ccy=BTC', SecretKey))`

其中，`timestamp`的值与`OK-ACCESS-TIMESTAMP`请求头相同，为ISO格式，如`2020-12-08T09:08:57.715Z`。

method是请求方法，字母全部大写：`GET/POST`。

requestPath是请求接口路径。如：`/api/v5/account/balance`

body是指请求主体的字符串，如果请求没有主体（通常为GET请求）则body可省略。如：`{"instId":"BTC-USDT","lever":"5","mgnMode":"isolated"}`

GET请求参数是算作requestPath，不算body 

SecretKey为用户申请APIKey时所生成。如：`22582BD0CFF14C41EDBF1AB98506286D`