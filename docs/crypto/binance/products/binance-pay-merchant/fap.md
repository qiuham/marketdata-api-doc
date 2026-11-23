---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/fap
api_type: Guide
updated_at: 2026-11-23 18:34:00.962908
---

# FAQ

Frequently Asked Questions

## 403 ERROR.

Exception Details:

```
The request could not be satisfied.
Request blocked. We can't connect to the server for this app or website at this time. There might be too much traffic or a configuration error. Try again later, or contact the app or website owner.
If you provide content to customers through CloudFront, you can find steps to troubleshoot and help prevent this error by reviewing the CloudFront documentation.
```

Solution: Please carefully check your request path is following document, for example:

```angular2html
create order: https://bpay.binanceapi.com/binancepay/openapi/v3/order
```

## Error code "100001001".

Exception Details:

```angular2html
{"status":"ERROR","type":"SYS","code":"100001001","errorData":"System abnormality"}
```

Solution:

- Please check if you used GET, **POST** method should be used.
- Please check if you didn't put **content-type: application/json** in request header
- Please check if you didn't post body in request

## Error code "400002"

Exception Details:

```angular2html
{"code":"400002","msg":"Signature for this request is not valid."}
```

### Solution A

Please check if your sign logic is incorrect. You can test with below parameters:

Timestamp:

```json
1611232922428
```

Nonce:

```json
5RhaTrZPhknNv0kDSA2UQ67cPMVNS4sA
```

Notification body:

```json
{
  "merchantId": "98765987",
  "subMerchantId": "98765987",
  "merchantTradeNo": "9825382937292",
  "totalFee": 25.17,
  "productDetail": "Greentea ice cream cone",
  "currency": "USDT",
  "returnUrl": "",
  "tradeType": "APP",
  "productType": "Food",
  "productName": "Ice Cream"
}
```

The generated payload must be (there MUST be one new line at the end):

```json
1611232922428
5RhaTrZPhknNv0kDSA2UQ67cPMVNS4sA
{"merchantId":"98765987","subMerchantId":"98765987","merchantTradeNo":"9825382937292","totalFee":25.17,"productDetail":"Greentea ice cream cone","currency":"USDT","returnUrl":"","tradeType":"APP","productType":"Food","productName":"Ice Cream"}

```

API Secret Key:

```json
uahr4nhailyq55yubuhuncnprfac73bcbz2qfafsevic1jruwunioxtoaozy122f
```

Signature Should be:

```json
253B9241C7331C0F02A0F5417BDDD4CD88124D3E188C0BA0E3EF121D36844B7F4D1A69AD8A1C3C7FF34901115E35A2530B672CF7430902E9862D69867689FD9F
```

### Solution B

Please check if your json request body used **'**, should use **"**

### Solution C

Please check if your code changed the request json body after signing. Some may reformat the json.

### Solution D

Please check if you made the signature to upper case

### Solution E

Please check the API Secret used. Ensure the API secret is generated from the merchant dashboard and
saved immediately. A hashed API will be displayed after refresh, the hashed secret cannot be used.

## Error code "400003"

Exception Details:

```angular2html
{"code":"400003","msg":"Timestamp for this request is outside of the recvWindow."}
```

Solution:

- Please check the request header field 'BinancePay-Timestamp', it should be UnixTimestamp in
  milliseconds, not in seconds.
- Please check if the request timestamp was within 1s to Binance Server.

## Error code "400606"

Exception Details:

```angular2html
{"code":"400606","errorMessage": "Account has no accessibility to this function"."}
```

400606 error typically occurs when there’s an issue with your merchant account or API keys used.

Solution:

- Check the API key and secret used are generated from the merchant dashboard and are saved
  immediately. As hashed keys will be displayed shortly, these hashed keys cannot be used.
- The necessary access for the API keys has been enabled, such as Process Payment.
- Check if there’s any outstanding action required from your end to activate your merchant account.

## Error code “400004”

Exception Details:

```angular2html
{"code":"400004" "errorMessage": "Invalid API-key, IP, or permissions for action, request ip: 44.xx.xx"}
```

400004 error typically occurs when there’s an issue with the API keys used or on your whitelisted IP
address.

Solution:

- Check the API key and secret used is generated from the merchant dashboard and saved immediately.
  As hashed keys will be displayed shortly, these hashed keys cannot be used.
- Please check if there’s any IP input in the "IP Access Restrictions" field on the merchant
  dashboard. Ensure that API call is from the IP input.

## Webhook

### Unable to verify signature

Failed to verify the signature in webhook notification

#### Solution A

       Please check if your sign logic is incorrect. Test your code logic with these parameters, if it's not successful, then you need to double check your code logic.

### Order notification showing different BizId

Timestamp:

```json
1611232922428
```

Nonce:

```json
5RhaTrZPhknNv0kDSA2UQ67cPMVNS4sA
```

Notification body:

```json
{
  "bizType": "PAY",
  "data": "{\"merchantTradeNo\":\"9825382937292\",\"totalFee\":0.88000000,\"transactTime\":1619508939664,\"currency\":\"EUR\",\"commission\":0,\"openUserId\":\"1211HS10K81f4273ac031\",\"productType\":\"Food\",\"productName\":\"Ice Cream\",\"tradeType\":\"WEB\",\"transactionId\":\"M_R_282737362839373\"}",
  "bizId": 29383937493038367292,
  "bizStatus": "PAY_SUCCESS"
}
```

The generated payload must be (there MUST be one new line at the end):

```java
1611232922428
5RhaTrZPhknNv0kDSA2UQ67cPMVNS4sA
{"bizType":"PAY","data":"{\"merchantTradeNo\":\"9825382937292\",\"totalFee\":0.88000000,\"transactTime\":1619508939664,\"currency\":\"EUR\",\"commission\":0,\"openUserId\":\"1211HS10K81f4273ac031\",\"productType\":\"Food\",\"productName\":\"Ice Cream\",\"tradeType\":\"WEB\",\"transactionId\":\"M_R_282737362839373\"}","bizId":29383937493038367292,"bizStatus":"PAY_SUCCESS"}

```

Public key:

```angular2html
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVAMXVTMIuttHcP1kvSk9V39S7
BqDbY+LC9JfwMzyoubo3fdsqBf4EmB1PfBUigcOL5YBqMKGEE6xmVw6SXCTH4JwX
dqJ4IRiXf76YMt6PB0dMzu/qCmhaGFGkqT6vJM0hHyEbtS/P3FR9ZU+eaOvynLWb
FvXTzIoctZM1IvDrCwIDAQAB
-----END PUBLIC KEY-----
```

Verification must be passed against this original signature in header:

```angular2html
VtniwOFAi4oBKFnvHhY6UZ+wPARf7+yWVbE61Hc7JVdRgqKJ40Yk9k5Gb2Y0S0VLUYOOOhUNUsD7R8GDEr6WH84sAEf8bXa1xYMiyjgeGleTg1MxRJCtrHcxMeMCEXPWmKTeLhn6O+cdvDGq4ZpcTTiQnEvk5xHPcxFrBT637zg=
```

### Solution B

If above testing is working fine, please check if you formatted the notification body and used the
formatted body for signature check

## Pay Order Webhook notification showing different BizIds.

This is a common error if you are using nodejs. What we sent over are actually the same BizIds,
however there is a problem with nodejs parsing and processing large numbers, hence resulting in this
error.

### Solution A

Treating the whole body as string instead.

### Solution B

Please turn off any body parser middleware if you are using it.

### Solution C

Turn off any body parser middleware and treat the whole body as string.

---

# FAQ

Frequently Asked Questions

## 403 ERROR.

Exception Details:

```
The request could not be satisfied.
Request blocked. We can't connect to the server for this app or website at this time. There might be too much traffic or a configuration error. Try again later, or contact the app or website owner.
If you provide content to customers through CloudFront, you can find steps to troubleshoot and help prevent this error by reviewing the CloudFront documentation.
```

Solution: Please carefully check your request path is following document, for example:

```angular2html
create order: https://bpay.binanceapi.com/binancepay/openapi/v3/order
```

## Error code "100001001".

Exception Details:

```angular2html
{"status":"ERROR","type":"SYS","code":"100001001","errorData":"System abnormality"}
```

Solution:

- Please check if you used GET, **POST** method should be used.
- Please check if you didn't put **content-type: application/json** in request header
- Please check if you didn't post body in request

## Error code "400002"

Exception Details:

```angular2html
{"code":"400002","msg":"Signature for this request is not valid."}
```

### Solution A

Please check if your sign logic is incorrect. You can test with below parameters:

Timestamp:

```json
1611232922428
```

Nonce:

```json
5RhaTrZPhknNv0kDSA2UQ67cPMVNS4sA
```

Notification body:

```json
{
  "merchantId": "98765987",
  "subMerchantId": "98765987",
  "merchantTradeNo": "9825382937292",
  "totalFee": 25.17,
  "productDetail": "Greentea ice cream cone",
  "currency": "USDT",
  "returnUrl": "",
  "tradeType": "APP",
  "productType": "Food",
  "productName": "Ice Cream"
}
```

The generated payload must be (there MUST be one new line at the end):

```json
1611232922428
5RhaTrZPhknNv0kDSA2UQ67cPMVNS4sA
{"merchantId":"98765987","subMerchantId":"98765987","merchantTradeNo":"9825382937292","totalFee":25.17,"productDetail":"Greentea ice cream cone","currency":"USDT","returnUrl":"","tradeType":"APP","productType":"Food","productName":"Ice Cream"}

```

API Secret Key:

```json
uahr4nhailyq55yubuhuncnprfac73bcbz2qfafsevic1jruwunioxtoaozy122f
```

Signature Should be:

```json
253B9241C7331C0F02A0F5417BDDD4CD88124D3E188C0BA0E3EF121D36844B7F4D1A69AD8A1C3C7FF34901115E35A2530B672CF7430902E9862D69867689FD9F
```

### Solution B

Please check if your json request body used **'**, should use **"**

### Solution C

Please check if your code changed the request json body after signing. Some may reformat the json.

### Solution D

Please check if you made the signature to upper case

### Solution E

Please check the API Secret used. Ensure the API secret is generated from the merchant dashboard and
saved immediately. A hashed API will be displayed after refresh, the hashed secret cannot be used.

## Error code "400003"

Exception Details:

```angular2html
{"code":"400003","msg":"Timestamp for this request is outside of the recvWindow."}
```

Solution:

- Please check the request header field 'BinancePay-Timestamp', it should be UnixTimestamp in
  milliseconds, not in seconds.
- Please check if the request timestamp was within 1s to Binance Server.

## Error code "400606"

Exception Details:

```angular2html
{"code":"400606","errorMessage": "Account has no accessibility to this function"."}
```

400606 error typically occurs when there’s an issue with your merchant account or API keys used.

Solution:

- Check the API key and secret used are generated from the merchant dashboard and are saved
  immediately. As hashed keys will be displayed shortly, these hashed keys cannot be used.
- The necessary access for the API keys has been enabled, such as Process Payment.
- Check if there’s any outstanding action required from your end to activate your merchant account.

## Error code “400004”

Exception Details:

```angular2html
{"code":"400004" "errorMessage": "Invalid API-key, IP, or permissions for action, request ip: 44.xx.xx"}
```

400004 error typically occurs when there’s an issue with the API keys used or on your whitelisted IP
address.

Solution:

- Check the API key and secret used is generated from the merchant dashboard and saved immediately.
  As hashed keys will be displayed shortly, these hashed keys cannot be used.
- Please check if there’s any IP input in the "IP Access Restrictions" field on the merchant
  dashboard. Ensure that API call is from the IP input.

## Webhook

### Unable to verify signature

Failed to verify the signature in webhook notification

#### Solution A

       Please check if your sign logic is incorrect. Test your code logic with these parameters, if it's not successful, then you need to double check your code logic.

### Order notification showing different BizId

Timestamp:

```json
1611232922428
```

Nonce:

```json
5RhaTrZPhknNv0kDSA2UQ67cPMVNS4sA
```

Notification body:

```json
{
  "bizType": "PAY",
  "data": "{\"merchantTradeNo\":\"9825382937292\",\"totalFee\":0.88000000,\"transactTime\":1619508939664,\"currency\":\"EUR\",\"commission\":0,\"openUserId\":\"1211HS10K81f4273ac031\",\"productType\":\"Food\",\"productName\":\"Ice Cream\",\"tradeType\":\"WEB\",\"transactionId\":\"M_R_282737362839373\"}",
  "bizId": 29383937493038367292,
  "bizStatus": "PAY_SUCCESS"
}
```

The generated payload must be (there MUST be one new line at the end):

```java
1611232922428
5RhaTrZPhknNv0kDSA2UQ67cPMVNS4sA
{"bizType":"PAY","data":"{\"merchantTradeNo\":\"9825382937292\",\"totalFee\":0.88000000,\"transactTime\":1619508939664,\"currency\":\"EUR\",\"commission\":0,\"openUserId\":\"1211HS10K81f4273ac031\",\"productType\":\"Food\",\"productName\":\"Ice Cream\",\"tradeType\":\"WEB\",\"transactionId\":\"M_R_282737362839373\"}","bizId":29383937493038367292,"bizStatus":"PAY_SUCCESS"}

```

Public key:

```angular2html
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVAMXVTMIuttHcP1kvSk9V39S7
BqDbY+LC9JfwMzyoubo3fdsqBf4EmB1PfBUigcOL5YBqMKGEE6xmVw6SXCTH4JwX
dqJ4IRiXf76YMt6PB0dMzu/qCmhaGFGkqT6vJM0hHyEbtS/P3FR9ZU+eaOvynLWb
FvXTzIoctZM1IvDrCwIDAQAB
-----END PUBLIC KEY-----
```

Verification must be passed against this original signature in header:

```angular2html
VtniwOFAi4oBKFnvHhY6UZ+wPARf7+yWVbE61Hc7JVdRgqKJ40Yk9k5Gb2Y0S0VLUYOOOhUNUsD7R8GDEr6WH84sAEf8bXa1xYMiyjgeGleTg1MxRJCtrHcxMeMCEXPWmKTeLhn6O+cdvDGq4ZpcTTiQnEvk5xHPcxFrBT637zg=
```

### Solution B

If above testing is working fine, please check if you formatted the notification body and used the
formatted body for signature check

## Pay Order Webhook notification showing different BizIds.

This is a common error if you are using nodejs. What we sent over are actually the same BizIds,
however there is a problem with nodejs parsing and processing large numbers, hence resulting in this
error.

### Solution A

Treating the whole body as string instead.

### Solution B

Please turn off any body parser middleware if you are using it.

### Solution C

Turn off any body parser middleware and treat the whole body as string.