---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/requestPayment
api_type: Guide
updated_at: 2026-11-21 18:44:12.006162
---

# bn.requestPayment

▸ **requestPayment**(`options`): `Promise`<`PaymentResult`\>

Initiates a request for payment via Binance Pay.

**`example`**

```js
bn.requestPayment({
  certSn: "",
  merchantId: "",
  timeStamp: "",
  nonceStr: "",
  package: "",
  paySign: "", // signature of the parameters
}).then((res) => {
  if (res.status === "0") {
    // success
  }
});
```

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `PaymentOptions` |

Returns

`Promise`<`PaymentResult`\>

Payment result

## Interface: PaymentOptions

| Name       | Type                                  | Description                                                                                                                    |
| :--------- | :------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| certSn     | `string`                              | API identity key issued by Binance payment system                                                                              |
| nonceStr?  | `string`                              | nonceStr for the sign                                                                                                          |
| merchantId | `string`                              | The merchant account id, issued when merchant been created at Binance                                                          |
| package?   | `string`                              | The value of the prepay_id parameter returned by the unified order placement API                                               |
| paySign    | `string`                              | Signature. For specific signature schemes, see [Binance Pay API Documentation](/products/binance-pay-merchant/app-integration) |
| timeStamp  | `string`                              | timestamp of the sign                                                                                                          |
| signType?  | `"MD5"` \| `"HMAC-SHA256"` \| `"RSA"` | sign algorithm                                                                                                                 |

## Interface: PaymentResult

| Name   | Type     | Description                        |
| :----- | :------- | :--------------------------------- |
| status | `number` | 0: pay success; others: pay failed |

---

# bn.requestPayment

▸ **requestPayment**(`options`): `Promise`<`PaymentResult`\>

Initiates a request for payment via Binance Pay.

**`example`**

```js
bn.requestPayment({
  certSn: "",
  merchantId: "",
  timeStamp: "",
  nonceStr: "",
  package: "",
  paySign: "", // signature of the parameters
}).then((res) => {
  if (res.status === "0") {
    // success
  }
});
```

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `PaymentOptions` |

Returns

`Promise`<`PaymentResult`\>

Payment result

## Interface: PaymentOptions

| Name       | Type                                  | Description                                                                                                                    |
| :--------- | :------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| certSn     | `string`                              | API identity key issued by Binance payment system                                                                              |
| nonceStr?  | `string`                              | nonceStr for the sign                                                                                                          |
| merchantId | `string`                              | The merchant account id, issued when merchant been created at Binance                                                          |
| package?   | `string`                              | The value of the prepay_id parameter returned by the unified order placement API                                               |
| paySign    | `string`                              | Signature. For specific signature schemes, see [Binance Pay API Documentation](/products/binance-pay-merchant/app-integration) |
| timeStamp  | `string`                              | timestamp of the sign                                                                                                          |
| signType?  | `"MD5"` \| `"HMAC-SHA256"` \| `"RSA"` | sign algorithm                                                                                                                 |

## Interface: PaymentResult

| Name   | Type     | Description                        |
| :----- | :------- | :--------------------------------- |
| status | `number` | 0: pay success; others: pay failed |