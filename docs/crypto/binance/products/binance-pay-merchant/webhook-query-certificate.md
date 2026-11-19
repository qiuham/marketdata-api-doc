---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-query-certificate
api_type: Guide
updated_at: 2026-11-19 18:35:04.075868
---

# Webhook query certificate

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

# Webhook query certificate

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