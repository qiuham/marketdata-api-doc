---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-query-certificate
api_type: Guide
updated_at: 2026-11-20 18:34:47.235233
---

# Webhook query certificate (Deprecated)

**The API is deprecated and will be retired soon, please migrate to
[Query New Certificate API](webhook-query-certificate-new) ASAP.** Look up the public key there by
the `BinancePay-Certificate-SN-New` webhook header, see
[Verify the New Signature](webhook-common#verify-the-new-signature).

For Security Purpose, Binance will add signature for webhook notification. Partner need to verify
the signature using the public key issued from Binance Pay. Public key can be queried from this API

## EndPoint

```http request
POST /binancepay/openapi/certificates
```

## Response Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**       |
| -------------- | -------- | ------------ | -------------- | --------------------- |
| **certSerial** | string   | Y            | -              | public key hash value |
| **certPublic** | string   | Y            | -              | public key            |

---

# Webhook query certificate (Deprecated)

**The API is deprecated and will be retired soon, please migrate to
[Query New Certificate API](webhook-query-certificate-new) ASAP.** Look up the public key there by
the `BinancePay-Certificate-SN-New` webhook header, see
[Verify the New Signature](webhook-common#verify-the-new-signature).

For Security Purpose, Binance will add signature for webhook notification. Partner need to verify
the signature using the public key issued from Binance Pay. Public key can be queried from this API

## EndPoint

```http request
POST /binancepay/openapi/certificates
```

## Response Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**       |
| -------------- | -------- | ------------ | -------------- | --------------------- |
| **certSerial** | string   | Y            | -              | public key hash value |
| **certPublic** | string   | Y            | -              | public key            |