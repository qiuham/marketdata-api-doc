---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-query-certificate-new
api_type: Guide
updated_at: 2026-11-25 18:33:26.423903
---

# Webhook query new certificate

Binance Pay is introducing a new platform certificate for webhook signatures. Webhooks signed with
it carry `BinancePay-Certificate-SN-New` and `BinancePay-Signature-New` next to the existing
headers, see [Webhook Common Rules](webhook-common#verify-the-new-signature). This API returns the
list of public keys for `BinancePay-Signature-New`. Find the public key for a webhook in this list
by the `BinancePay-Certificate-SN-New` header.

Always get the public key from this API. Do not hard-code it in your code or configuration: Binance
Pay can replace the certificate, and a hard-coded key stops verifying from that moment.

## EndPoint

```http request
POST /binancepay/openapi/certificates-new
```

The request is signed like every other Binance Pay API request, see [API Common Rules](api-common).
It takes no request parameters.

## Response Parameters

| **Attributes**   | **Type**          | **Required** | **Limitation**      | **Description**                                              |
| ---------------- | ----------------- | ------------ | ------------------- | ------------------------------------------------------------ |
| **status**       | string            | Y            | "SUCCESS" or "FAIL" | status of the API request                                    |
| **code**         | string            | Y            | -                   | request result code, refer to [API Common Rules](api-common) |
| **data**         | List(Certificate) | Y            | -                   | certificate **list**, [refer to](#certificate)               |
| **errorMessage** | string            | N            | maximum length 256  |                                                              |

`data` is a **list**, not a single certificate:

- Each element is one certificate, identified by its `certSerial`.
- The list can hold more than one certificate, for example while Binance Pay replaces the
  certificate. It is empty until Binance Pay enables the new certificate; a non-empty list means
  webhooks now carry the new headers.
- The order of the elements has no meaning. Find the certificate for a webhook by its
  `BinancePay-Certificate-SN-New` header, see
  [Find the Public Key by the Webhook Header](#find-the-public-key-by-the-webhook-header).
- `/binancepay/openapi/certificates` does not return these certificates.

## Child Attribute

### Certificate

<span id="certificate"></span>

| **Attributes** | **Type** | **Required** | **Limitation**                     | **Description**                                                                                                                                                                |
| -------------- | -------- | ------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **certSerial** | string   | Y            | 32-character uppercase hexadecimal | Certificate serial number. Equals the `BinancePay-Certificate-SN-New` header of the webhooks this certificate signs, character for character: compare the two as exact strings |
| **certPublic** | string   | Y            | -                                  | Public key (PEM) of this certificate. Verifies `BinancePay-Signature-New` of a webhook whose `BinancePay-Certificate-SN-New` equals `certSerial`                               |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": [
    {
      "certSerial": "F31065629063153EF6476244DFB6872E",
      "certPublic": "-----BEGIN PUBLIC KEY-----\n<public key>\n-----END PUBLIC KEY-----"
    }
  ]
}
```

## Find the Public Key by the Webhook Header

1. Call this API and cache `data` as a map from `certSerial` to `certPublic`.
2. When a webhook arrives, read its `BinancePay-Certificate-SN-New` header.
3. Look up that value in the map. The matching `certPublic` is the public key that verifies the
   webhook's `BinancePay-Signature-New`. Never pick a key by its position in `data`, such as the
   first or the last element.
4. If the value is not in the map and the map was rebuilt less than a minute ago, reject the webhook
   without calling this API. Otherwise call this API again, rebuild the map, and reject the webhook
   if the value is still not found. Anyone who can reach your webhook URL can send an unknown value,
   so never call this API once per webhook. Binance Pay retries a rejected webhook, so a genuine
   webhook signed by a certificate you have not cached yet passes on a later retry.
5. Refresh the cache at least once a day, even when no unknown value appears.

---

# Webhook query new certificate

Binance Pay is introducing a new platform certificate for webhook signatures. Webhooks signed with
it carry `BinancePay-Certificate-SN-New` and `BinancePay-Signature-New` next to the existing
headers, see [Webhook Common Rules](webhook-common#verify-the-new-signature). This API returns the
list of public keys for `BinancePay-Signature-New`. Find the public key for a webhook in this list
by the `BinancePay-Certificate-SN-New` header.

Always get the public key from this API. Do not hard-code it in your code or configuration: Binance
Pay can replace the certificate, and a hard-coded key stops verifying from that moment.

## EndPoint

```http request
POST /binancepay/openapi/certificates-new
```

The request is signed like every other Binance Pay API request, see [API Common Rules](api-common).
It takes no request parameters.

## Response Parameters

| **Attributes**   | **Type**          | **Required** | **Limitation**      | **Description**                                              |
| ---------------- | ----------------- | ------------ | ------------------- | ------------------------------------------------------------ |
| **status**       | string            | Y            | "SUCCESS" or "FAIL" | status of the API request                                    |
| **code**         | string            | Y            | -                   | request result code, refer to [API Common Rules](api-common) |
| **data**         | List(Certificate) | Y            | -                   | certificate **list**, [refer to](#certificate)               |
| **errorMessage** | string            | N            | maximum length 256  |                                                              |

`data` is a **list**, not a single certificate:

- Each element is one certificate, identified by its `certSerial`.
- The list can hold more than one certificate, for example while Binance Pay replaces the
  certificate. It is empty until Binance Pay enables the new certificate; a non-empty list means
  webhooks now carry the new headers.
- The order of the elements has no meaning. Find the certificate for a webhook by its
  `BinancePay-Certificate-SN-New` header, see
  [Find the Public Key by the Webhook Header](#find-the-public-key-by-the-webhook-header).
- `/binancepay/openapi/certificates` does not return these certificates.

## Child Attribute

### Certificate

<span id="certificate"></span>

| **Attributes** | **Type** | **Required** | **Limitation**                     | **Description**                                                                                                                                                                |
| -------------- | -------- | ------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **certSerial** | string   | Y            | 32-character uppercase hexadecimal | Certificate serial number. Equals the `BinancePay-Certificate-SN-New` header of the webhooks this certificate signs, character for character: compare the two as exact strings |
| **certPublic** | string   | Y            | -                                  | Public key (PEM) of this certificate. Verifies `BinancePay-Signature-New` of a webhook whose `BinancePay-Certificate-SN-New` equals `certSerial`                               |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": [
    {
      "certSerial": "F31065629063153EF6476244DFB6872E",
      "certPublic": "-----BEGIN PUBLIC KEY-----\n<public key>\n-----END PUBLIC KEY-----"
    }
  ]
}
```

## Find the Public Key by the Webhook Header

1. Call this API and cache `data` as a map from `certSerial` to `certPublic`.
2. When a webhook arrives, read its `BinancePay-Certificate-SN-New` header.
3. Look up that value in the map. The matching `certPublic` is the public key that verifies the
   webhook's `BinancePay-Signature-New`. Never pick a key by its position in `data`, such as the
   first or the last element.
4. If the value is not in the map and the map was rebuilt less than a minute ago, reject the webhook
   without calling this API. Otherwise call this API again, rebuild the map, and reject the webhook
   if the value is still not found. Anyone who can reach your webhook URL can send an unknown value,
   so never call this API once per webhook. Binance Pay retries a rejected webhook, so a genuine
   webhook signed by a certificate you have not cached yet passes on a later retry.
5. Refresh the cache at least once a day, even when no unknown value appears.