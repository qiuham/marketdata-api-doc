---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-rest-authentication-signature
anchor_id: overview-rest-authentication-signature
api_type: REST
updated_at: 2026-07-04 19:36:58.131311
---

# Signature

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

# 签名

> 生成签名

`OK-ACCESS-SIGN`的请求头是对`timestamp + method + requestPath + body`字符串（+表示字符串连接），以及SecretKey，使用HMAC SHA256方法加密，通过Base-64编码输出而得到的。

如：`sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp + 'GET' + '/api/v5/account/balance?ccy=BTC', SecretKey))`

其中，`timestamp`的值与`OK-ACCESS-TIMESTAMP`请求头相同，为ISO格式，如`2020-12-08T09:08:57.715Z`。

method是请求方法，字母全部大写：`GET/POST`。

requestPath是请求接口路径。如：`/api/v5/account/balance`

body是指请求主体的字符串，如果请求没有主体（通常为GET请求）则body可省略。如：`{"instId":"BTC-USDT","lever":"5","mgnMode":"isolated"}`

GET请求参数是算作requestPath，不算body 

SecretKey为用户申请APIKey时所生成。如：`22582BD0CFF14C41EDBF1AB98506286D`