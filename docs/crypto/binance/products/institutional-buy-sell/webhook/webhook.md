---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/institutional-buy-sell/webhook/webhook
api_type: Guide
updated_at: 2026-11-23 18:39:04.863155
---

# Webhook

Whenever a key event (currently only "order status change") occurs, Institutional Crypto Buy/Sell
Solution will send a webhook message, and the partner (client) can receive this message at the
webhook callback url and react accordingly, such as updating order data and frontend UI.

### Request Headers

| **Field**              | **Type**  | **Remarks**                                              |
| ---------------------- | --------- | -------------------------------------------------------- |
| X-BN-Connect-Timestamp | timestamp | timestamp                                                |
| X-BN-Connect-Signature | string    | SHA256withRSA(**requestBody** + **X-Connect-Timestamp**) |
| X-BN-Connect-For       | string    | Same with your client id (X-Tesla-ClientId)              |

### Request Body

| Field            | Type      | Remarks                                          |
| ---------------- | --------- | ------------------------------------------------ |
| webhookEventType | string    | fixed value: prime_order_event                   |
| orderId          | string    | Binance order ID                                 |
| clientOrderId    | string    | Client side order ID                             |
| direction        | string    | BUY or SELL                                      |
| fiatCurrency     | string    | Fiat currency                                    |
| cryptoCurrency   | string    | Crypto currency                                  |
| fiatAmount       | decimal   | Fiat amount                                      |
| cryptoAmount     | decimal   | Crypto Amount                                    |
| price            | decimal   | Price. 1 crypto currency = {price} fiat currency |
| status           | string    | FILLED/FAILED                                    |
| createTime       | timestamp | Order creation time (UTC)                        |
| settleTime       | timestamp | Settlement time (UTC)                            |

### Response Body

- HTTP status code is 200
- Response body is in JSON format.

| **Field**     | **Type** | **Remarks**                                                                        |
| ------------- | -------- | ---------------------------------------------------------------------------------- |
| returnCode    | string   | SUCCESS or other code you wish to return to Institutional Crypto Buy/Sell Solution |
| returnMessage | string   | the message you wish to return to Institutional Crypto Buy/Sell Solution           |

### How signature works

The encryption/decryption and verification process of webhook is exactly the opposite/mirrored of
API request process. The sender and receiver of the two are opposite, but they are both processes
that signed by the sender with a private key and verified by the receiver with a public key.

For API requests, the partner (client) generates a pair of keys. The private key is kept securely
and privately by the partner (client). Then the partner (client) uses the private key to sign when
initiating API requests. The public key is shared to Institutional Crypto Buy/Sell Solution, with
which Binance will verify the signature of the API request to ensure that the request is indeed
initiated by the partner (client).

For webhook, it's an opposite/mirrored process. Institutional Crypto Buy/Sell Solution generates a
pair of keys. The private key is kept securely and privately by Institutional Crypto Buy/Sell
Solution. Then Institutional Crypto Buy/Sell Solution uses the private key to sign when initiating
the webhook message. The public key is shared to the partner (client), with which the partner
(client) can verify the signature of the webhook message to ensure that the message is indeed
initiated by Binance.

#### The webhook signature flow is as follows:

![signature-Webhook.png](../images/signature-Webhook-prime.png)

### Verify signature

As mentioned above, Institutional Crypto Buy/Sell Solution initiates a webhook request to the
webhook callback url provided by the partner ( client). And the partner (client) should verify the
identity of the request initiator based on the public key provided by Institutional Crypto Buy/Sell
Solution.

The example code below shows how to verify signature with public key:

```java
public static boolean verify(String srcData, PublicKey publicKey, String sign) throws Exception {
    Signature signature = Signature.getInstance("SHA256withRSA");
    signature.initVerify(publicKey);
    signature.update(srcData.getBytes());
    return signature.verify(Base64.decodeBase64(sign.getBytes()));
}
```

#

### Example

Request Body:

```json
{
  "webhookEventType": "prime_order_event",
  "orderId": "1234567890",
  "clientOrderId": "myOrder001",
  "direction": "BUY",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "BTC",
  "fiatAmount": 100,
  "cryptoAmount": 0.00102181,
  "price": 97849.27,
  "status": "FILLED",
  "createTime": 1692951399,
  "settleTime": 1692954999
}
```

---

# Webhook

Whenever a key event (currently only "order status change") occurs, Institutional Crypto Buy/Sell
Solution will send a webhook message, and the partner (client) can receive this message at the
webhook callback url and react accordingly, such as updating order data and frontend UI.

### Request Headers

| **Field**              | **Type**  | **Remarks**                                              |
| ---------------------- | --------- | -------------------------------------------------------- |
| X-BN-Connect-Timestamp | timestamp | timestamp                                                |
| X-BN-Connect-Signature | string    | SHA256withRSA(**requestBody** + **X-Connect-Timestamp**) |
| X-BN-Connect-For       | string    | Same with your client id (X-Tesla-ClientId)              |

### Request Body

| Field            | Type      | Remarks                                          |
| ---------------- | --------- | ------------------------------------------------ |
| webhookEventType | string    | fixed value: prime_order_event                   |
| orderId          | string    | Binance order ID                                 |
| clientOrderId    | string    | Client side order ID                             |
| direction        | string    | BUY or SELL                                      |
| fiatCurrency     | string    | Fiat currency                                    |
| cryptoCurrency   | string    | Crypto currency                                  |
| fiatAmount       | decimal   | Fiat amount                                      |
| cryptoAmount     | decimal   | Crypto Amount                                    |
| price            | decimal   | Price. 1 crypto currency = {price} fiat currency |
| status           | string    | FILLED/FAILED                                    |
| createTime       | timestamp | Order creation time (UTC)                        |
| settleTime       | timestamp | Settlement time (UTC)                            |

### Response Body

- HTTP status code is 200
- Response body is in JSON format.

| **Field**     | **Type** | **Remarks**                                                                        |
| ------------- | -------- | ---------------------------------------------------------------------------------- |
| returnCode    | string   | SUCCESS or other code you wish to return to Institutional Crypto Buy/Sell Solution |
| returnMessage | string   | the message you wish to return to Institutional Crypto Buy/Sell Solution           |

### How signature works

The encryption/decryption and verification process of webhook is exactly the opposite/mirrored of
API request process. The sender and receiver of the two are opposite, but they are both processes
that signed by the sender with a private key and verified by the receiver with a public key.

For API requests, the partner (client) generates a pair of keys. The private key is kept securely
and privately by the partner (client). Then the partner (client) uses the private key to sign when
initiating API requests. The public key is shared to Institutional Crypto Buy/Sell Solution, with
which Binance will verify the signature of the API request to ensure that the request is indeed
initiated by the partner (client).

For webhook, it's an opposite/mirrored process. Institutional Crypto Buy/Sell Solution generates a
pair of keys. The private key is kept securely and privately by Institutional Crypto Buy/Sell
Solution. Then Institutional Crypto Buy/Sell Solution uses the private key to sign when initiating
the webhook message. The public key is shared to the partner (client), with which the partner
(client) can verify the signature of the webhook message to ensure that the message is indeed
initiated by Binance.

#### The webhook signature flow is as follows:

![signature-Webhook.png](../images/signature-Webhook-prime.png)

### Verify signature

As mentioned above, Institutional Crypto Buy/Sell Solution initiates a webhook request to the
webhook callback url provided by the partner ( client). And the partner (client) should verify the
identity of the request initiator based on the public key provided by Institutional Crypto Buy/Sell
Solution.

The example code below shows how to verify signature with public key:

```java
public static boolean verify(String srcData, PublicKey publicKey, String sign) throws Exception {
    Signature signature = Signature.getInstance("SHA256withRSA");
    signature.initVerify(publicKey);
    signature.update(srcData.getBytes());
    return signature.verify(Base64.decodeBase64(sign.getBytes()));
}
```

#

### Example

Request Body:

```json
{
  "webhookEventType": "prime_order_event",
  "orderId": "1234567890",
  "clientOrderId": "myOrder001",
  "direction": "BUY",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "BTC",
  "fiatAmount": 100,
  "cryptoAmount": 0.00102181,
  "price": 97849.27,
  "status": "FILLED",
  "createTime": 1692951399,
  "settleTime": 1692954999
}
```