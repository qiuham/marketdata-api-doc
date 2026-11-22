---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/connect-2.0/webhook/webhook
api_type: Guide
updated_at: 2026-11-22 18:38:13.006597
---

# Webhook

Whenever a key event (currently only "order status change") occurs, Binance Pay Onchain will send a
webhook message, and the partner (client) can receive this message at the webhook callback url and
react accordingly, such as updating order data and frontend UI.

### Request Headers

| **Field**              | **Type**  | **Remarks**                                              |
| ---------------------- | --------- | -------------------------------------------------------- |
| X-BN-Connect-Timestamp | timestamp | timestamp                                                |
| X-BN-Connect-Signature | string    | SHA256withRSA(**requestBody** + **X-Connect-Timestamp**) |
| X-BN-Connect-For       | string    | Same with your client id (X-Tesla-ClientId)              |

### Request Body

| **Field**             | **Type**  | **Remarks**                                                                                                                                                                                          |
| --------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| webhookEventType      | string    | A fixed value: connect_order_event                                                                                                                                                                   |
| externalOrderId       | string    | The unique order id from the partner side.                                                                                                                                                           |
| type                  | int       | 1: buy, 2: sell, 3: send                                                                                                                                                                             |
| businessType          | int       | 1: fiat, 2: p2p, 3: send, 4: convert                                                                                                                                                                 |
| status                | int       | Please refer to "[Order status](../basics/7.order-status.md)"                                                                                                                                        |
| payMethodCode         | string    | The payment method code is from payment method list API                                                                                                                                              |
| payMethodSubCode      | string    | The payment method sub code is from payment method list API                                                                                                                                          |
| fiatCurrency          | string    | fiat currency                                                                                                                                                                                        |
| cryptoCurrency        | string    | crypto currency                                                                                                                                                                                      |
| openUserId            | string    | OpenUserId represents a Binance user ID that has been securely hashed. This field is provided to merchants to facilitate the identification of whether multiple orders originate from the same user. |
| fiatAmount            | string    | fiat amount                                                                                                                                                                                          |
| cryptoAmount          | string    | crypto amount                                                                                                                                                                                        |
| feeAmount             | string    | fee amount                                                                                                                                                                                           |
| feeCurrency           | string    | fee currency, USD or crypto                                                                                                                                                                          |
| revenueAmount         | string    | partner revenue amount                                                                                                                                                                               |
| revenueCurrency       | string    | partner revenue currency, USD or crypto                                                                                                                                                              |
| networkFee            | string    | network fee amount                                                                                                                                                                                   |
| withdrawWalletAddress | string    | withdraw wallet address                                                                                                                                                                              |
| withdrawNetwork       | string    | withdraw network                                                                                                                                                                                     |
| withdrawMemo          | string    | withdraw network memo                                                                                                                                                                                |
| withdrawTxHash        | string    | withdraw tx hash                                                                                                                                                                                     |
| orderDetailLink       | string    | order detail link                                                                                                                                                                                    |
| orderTime             | timestamp | order time                                                                                                                                                                                           |
| completionTime        | timestamp | completion time                                                                                                                                                                                      |
| updateTime            | timestamp | update time                                                                                                                                                                                          |
| convertInfo           | object    | Convert information. This field is only present for Convert orders. Refer to **ConvertInfo**                                                                                                         |
| swapDetailInfoVo      | object    | If the order has swap operation. Then this field has value. Refer to **SwapDetailInfoVo**                                                                                                            |
| userData              | string    | AES-encrypted JSON string (see details below). Disabled by default; contact us to enable                                                                                                             |

#### SwapDetailInfoVo

| **Field**                         | **Type** | **Remarks**                                                                       |
| --------------------------------- | -------- | --------------------------------------------------------------------------------- |
| fromCryptoCurrencyContractAddress | string   | The "from" crypto contract address, typically a stablecoin or native token.       |
| toCryptoCurrencyContractAddress   | string   | The contract address of the target coin the user intends to swap online.          |
| toCryptoCurrencyAmount            | string   | The final amount of cryptocurrency the user swapped and received in their wallet. |

#### ConvertInfo

| **Field**      | **Type** | **Remarks**                                         |
| -------------- | -------- | --------------------------------------------------- |
| fromCoin       | string   | The source cryptocurrency being converted from      |
| fromCoinAmount | string   | The amount of source cryptocurrency being converted |

#### userData field

Some webhook payloads may include user-level or refund-related data when Compliance and Refund Data
Sharing is approved and enabled for the partner.

See
[Compliance and Refund Data Sharing](../compliance-refund-data-sharing/1.use-cases-and-eligibility.md)
for field definitions and eligibility details.

### Response Body

- HTTP status code is 200
- Response body is in JSON format.

| **Field**     | **Type** | **Remarks**                                                     |
| ------------- | -------- | --------------------------------------------------------------- |
| returnCode    | string   | SUCCESS or other code you wish to return to Binance Pay Onchain |
| returnMessage | string   | the message you wish to return to Binance Pay Onchain           |

### How signature works

The encryption/decryption and verification process of webhook is exactly the opposite/mirrored of
API request process. The sender and receiver of the two are opposite, but they are both processes
that signed by the sender with a private key and verified by the receiver with a public key.

For API requests, the partner (client) generates a pair of keys. The private key is kept securely
and privately by the partner (client). Then the partner (client) uses the private key to sign when
initiating API requests. The public key is shared to Binance Pay Onchain, with which Binance will
verify the signature of the API request to ensure that the request is indeed initiated by the
partner (client).

For webhook, it's an opposite/mirrored process. Binance Pay Onchain generates a pair of keys. The
private key is kept securely and privately by Binance Pay Onchain. Then Binance Pay Onchain uses the
private key to sign when initiating the webhook message. The public key is shared to the partner
(client), with which the partner (client) can verify the signature of the webhook message to ensure
that the message is indeed initiated by Binance.

#### The webhook signature flow is as follows:

![signature-Webhook.png](../images/signature-Webhook.png)

### Verify signature

As mentioned above, Binance Pay Onchain initiates a webhook request to the webhook callback url
provided by the partner ( client). And the partner (client) should verify the identity of the
request initiator based on the public key provided by Binance Pay Onchain.

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
  "webhookEventType": "connect_order_event",
  "externalOrderId": "180401941923045",
  "type": 1,
  "businessType": 1,
  "status": 2,
  "payMethodCode": "BUY_P2P",
  "payMethodSubCode": "BANK",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "USDT",
  "openUserId": "f47ac10b58cc4372a5670e02b2c3d479",
  "fiatAmount": "100",
  "cryptoAmount": "107.8",
  "feeAmount": "1",
  "feeCurrency": "USDT",
  "revenueAmount": "0.08",
  "revenueCurrency": "USDT",
  "networkFee": "0.5",
  "withdrawWalletAddress": "0xbb4CdB98Bd36B01bD1cBaEA52De08d9173bc095c",
  "withdrawNetwork": "BSC",
  "withdrawMemo": "",
  "withdrawTxHash": "0xcb163e2e6322cd6aa7bc4d45306029e846c0c06e9cdee45a06e88801d1231e71",
  "orderDetailLink": "https://www.binance.com/en/my/wallet/exchange/buysell-history?type=buy",
  "orderTime": 1723186761000,
  "completionTime": 1723206761000,
  "updateTime": 1734446642930
}
```

### Example (Convert Order)

Request Body:

```json
{
  "webhookEventType": "connect_order_event",
  "networkFee": null,
  "feeCurrency": "USDT",
  "type": 1,
  "businessType": 4,
  "withdrawMemo": "",
  "revenueAmount": null,
  "cryptoCurrency": "USDT",
  "withdrawTxHash": "",
  "completionTime": null,
  "orderTime": 1753344231742,
  "payMethodSubCode": "CUMBERLAND",
  "cryptoAmount": "1.03",
  "orderDetailLink": null,
  "payMethodCode": "SPOT",
  "revenueCurrency": "USDT",
  "convertInfo": {
    "fromCoin": "BNB",
    "fromCoinAmount": 0.00137386
  },
  "swapDetailInfoVo": null,
  "updateTime": 1753344255279,
  "externalOrderId": "830315252102",
  "withdrawWalletAddress": "0xbb4CdB98Bd36B01bD1cBaEA52De08d9173bc095c",
  "fiatCurrency": "",
  "fiatAmount": "0",
  "withdrawNetwork": "ETH",
  "status": 11
}
```

---

# Webhook

Whenever a key event (currently only "order status change") occurs, Binance Pay Onchain will send a
webhook message, and the partner (client) can receive this message at the webhook callback url and
react accordingly, such as updating order data and frontend UI.

### Request Headers

| **Field**              | **Type**  | **Remarks**                                              |
| ---------------------- | --------- | -------------------------------------------------------- |
| X-BN-Connect-Timestamp | timestamp | timestamp                                                |
| X-BN-Connect-Signature | string    | SHA256withRSA(**requestBody** + **X-Connect-Timestamp**) |
| X-BN-Connect-For       | string    | Same with your client id (X-Tesla-ClientId)              |

### Request Body

| **Field**             | **Type**  | **Remarks**                                                                                                                                                                                          |
| --------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| webhookEventType      | string    | A fixed value: connect_order_event                                                                                                                                                                   |
| externalOrderId       | string    | The unique order id from the partner side.                                                                                                                                                           |
| type                  | int       | 1: buy, 2: sell, 3: send                                                                                                                                                                             |
| businessType          | int       | 1: fiat, 2: p2p, 3: send, 4: convert                                                                                                                                                                 |
| status                | int       | Please refer to "[Order status](../basics/7.order-status.md)"                                                                                                                                        |
| payMethodCode         | string    | The payment method code is from payment method list API                                                                                                                                              |
| payMethodSubCode      | string    | The payment method sub code is from payment method list API                                                                                                                                          |
| fiatCurrency          | string    | fiat currency                                                                                                                                                                                        |
| cryptoCurrency        | string    | crypto currency                                                                                                                                                                                      |
| openUserId            | string    | OpenUserId represents a Binance user ID that has been securely hashed. This field is provided to merchants to facilitate the identification of whether multiple orders originate from the same user. |
| fiatAmount            | string    | fiat amount                                                                                                                                                                                          |
| cryptoAmount          | string    | crypto amount                                                                                                                                                                                        |
| feeAmount             | string    | fee amount                                                                                                                                                                                           |
| feeCurrency           | string    | fee currency, USD or crypto                                                                                                                                                                          |
| revenueAmount         | string    | partner revenue amount                                                                                                                                                                               |
| revenueCurrency       | string    | partner revenue currency, USD or crypto                                                                                                                                                              |
| networkFee            | string    | network fee amount                                                                                                                                                                                   |
| withdrawWalletAddress | string    | withdraw wallet address                                                                                                                                                                              |
| withdrawNetwork       | string    | withdraw network                                                                                                                                                                                     |
| withdrawMemo          | string    | withdraw network memo                                                                                                                                                                                |
| withdrawTxHash        | string    | withdraw tx hash                                                                                                                                                                                     |
| orderDetailLink       | string    | order detail link                                                                                                                                                                                    |
| orderTime             | timestamp | order time                                                                                                                                                                                           |
| completionTime        | timestamp | completion time                                                                                                                                                                                      |
| updateTime            | timestamp | update time                                                                                                                                                                                          |
| convertInfo           | object    | Convert information. This field is only present for Convert orders. Refer to **ConvertInfo**                                                                                                         |
| swapDetailInfoVo      | object    | If the order has swap operation. Then this field has value. Refer to **SwapDetailInfoVo**                                                                                                            |
| userData              | string    | AES-encrypted JSON string (see details below). Disabled by default; contact us to enable                                                                                                             |

#### SwapDetailInfoVo

| **Field**                         | **Type** | **Remarks**                                                                       |
| --------------------------------- | -------- | --------------------------------------------------------------------------------- |
| fromCryptoCurrencyContractAddress | string   | The "from" crypto contract address, typically a stablecoin or native token.       |
| toCryptoCurrencyContractAddress   | string   | The contract address of the target coin the user intends to swap online.          |
| toCryptoCurrencyAmount            | string   | The final amount of cryptocurrency the user swapped and received in their wallet. |

#### ConvertInfo

| **Field**      | **Type** | **Remarks**                                         |
| -------------- | -------- | --------------------------------------------------- |
| fromCoin       | string   | The source cryptocurrency being converted from      |
| fromCoinAmount | string   | The amount of source cryptocurrency being converted |

#### userData field

Some webhook payloads may include user-level or refund-related data when Compliance and Refund Data
Sharing is approved and enabled for the partner.

See
[Compliance and Refund Data Sharing](../compliance-refund-data-sharing/1.use-cases-and-eligibility.md)
for field definitions and eligibility details.

### Response Body

- HTTP status code is 200
- Response body is in JSON format.

| **Field**     | **Type** | **Remarks**                                                     |
| ------------- | -------- | --------------------------------------------------------------- |
| returnCode    | string   | SUCCESS or other code you wish to return to Binance Pay Onchain |
| returnMessage | string   | the message you wish to return to Binance Pay Onchain           |

### How signature works

The encryption/decryption and verification process of webhook is exactly the opposite/mirrored of
API request process. The sender and receiver of the two are opposite, but they are both processes
that signed by the sender with a private key and verified by the receiver with a public key.

For API requests, the partner (client) generates a pair of keys. The private key is kept securely
and privately by the partner (client). Then the partner (client) uses the private key to sign when
initiating API requests. The public key is shared to Binance Pay Onchain, with which Binance will
verify the signature of the API request to ensure that the request is indeed initiated by the
partner (client).

For webhook, it's an opposite/mirrored process. Binance Pay Onchain generates a pair of keys. The
private key is kept securely and privately by Binance Pay Onchain. Then Binance Pay Onchain uses the
private key to sign when initiating the webhook message. The public key is shared to the partner
(client), with which the partner (client) can verify the signature of the webhook message to ensure
that the message is indeed initiated by Binance.

#### The webhook signature flow is as follows:

![signature-Webhook.png](../images/signature-Webhook.png)

### Verify signature

As mentioned above, Binance Pay Onchain initiates a webhook request to the webhook callback url
provided by the partner ( client). And the partner (client) should verify the identity of the
request initiator based on the public key provided by Binance Pay Onchain.

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
  "webhookEventType": "connect_order_event",
  "externalOrderId": "180401941923045",
  "type": 1,
  "businessType": 1,
  "status": 2,
  "payMethodCode": "BUY_P2P",
  "payMethodSubCode": "BANK",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "USDT",
  "openUserId": "f47ac10b58cc4372a5670e02b2c3d479",
  "fiatAmount": "100",
  "cryptoAmount": "107.8",
  "feeAmount": "1",
  "feeCurrency": "USDT",
  "revenueAmount": "0.08",
  "revenueCurrency": "USDT",
  "networkFee": "0.5",
  "withdrawWalletAddress": "0xbb4CdB98Bd36B01bD1cBaEA52De08d9173bc095c",
  "withdrawNetwork": "BSC",
  "withdrawMemo": "",
  "withdrawTxHash": "0xcb163e2e6322cd6aa7bc4d45306029e846c0c06e9cdee45a06e88801d1231e71",
  "orderDetailLink": "https://www.binance.com/en/my/wallet/exchange/buysell-history?type=buy",
  "orderTime": 1723186761000,
  "completionTime": 1723206761000,
  "updateTime": 1734446642930
}
```

### Example (Convert Order)

Request Body:

```json
{
  "webhookEventType": "connect_order_event",
  "networkFee": null,
  "feeCurrency": "USDT",
  "type": 1,
  "businessType": 4,
  "withdrawMemo": "",
  "revenueAmount": null,
  "cryptoCurrency": "USDT",
  "withdrawTxHash": "",
  "completionTime": null,
  "orderTime": 1753344231742,
  "payMethodSubCode": "CUMBERLAND",
  "cryptoAmount": "1.03",
  "orderDetailLink": null,
  "payMethodCode": "SPOT",
  "revenueCurrency": "USDT",
  "convertInfo": {
    "fromCoin": "BNB",
    "fromCoinAmount": 0.00137386
  },
  "swapDetailInfoVo": null,
  "updateTime": 1753344255279,
  "externalOrderId": "830315252102",
  "withdrawWalletAddress": "0xbb4CdB98Bd36B01bD1cBaEA52De08d9173bc095c",
  "fiatCurrency": "",
  "fiatAmount": "0",
  "withdrawNetwork": "ETH",
  "status": 11
}
```