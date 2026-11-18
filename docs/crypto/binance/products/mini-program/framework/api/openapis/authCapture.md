---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/authCapture
api_type: Guide
updated_at: 2026-11-18 18:44:13.350823
---

# bn.authCapture

▸ **authCapture**(`options?`): `Promise`<`AuthCaptureResponse`\>

**`description`** AuthCapture is the entrance to initiate auth capture for merchants.
Pre-authorization is a function launched by Binance Pay for merchants in consumption scenarios (such
as taxis, hotel reservations, etc.) that require users to make guarantees in advance. The user needs
to make a fund authorization when the service is started. When the service is settled, the
consumption amount will be deducted from the authorized fund, and the rest will be returned to the
user.

**`example`**

```ts
const { status } = await bn.authCapture({
  certSn: string,
  merchantId: string,
  noncestr: string,
  cashierId: string,
  timeStamp: string,
  paySign: string,
});
```

Parameters

| Name       | Type                 |
| :--------- | :------------------- |
| `options?` | `AuthCaptureOptions` |

Returns

`Promise`<`AuthCaptureResponse`\>

## Interface: AuthCaptureOptions

| Name       | Type     | Description                                                                                                           |
| :--------- | :------- | :-------------------------------------------------------------------------------------------------------------------- |
| certSn     | `string` | API identity key issued by Binance payment system                                                                     |
| merchantId | `string` | The merchant account id, issued when merchant been created at Binance.                                                |
| noncestr   | `string` | A random string with 32 bytes, e.g. random ascii decimal within a-z and A-Z and loop 32 times to form a random string |
| cashierId  | `string` | The cashierId got from generateCashierUrl API                                                                         |
| timeStamp  | `string` | UnixTimestamp in millisecond that the requests send, guarantee the machine time is sync with the network              |
| paySign    | `string` | A signature generated according to a certain logic.                                                                   |

## Interface: AuthCaptureResponse

| Name   | Type     | Description                          |
| :----- | :------- | :----------------------------------- |
| status | `string` | "SUCCESS" or "FAIL". "0" for success |

---

# bn.authCapture

▸ **authCapture**(`options?`): `Promise`<`AuthCaptureResponse`\>

**`description`** AuthCapture is the entrance to initiate auth capture for merchants.
Pre-authorization is a function launched by Binance Pay for merchants in consumption scenarios (such
as taxis, hotel reservations, etc.) that require users to make guarantees in advance. The user needs
to make a fund authorization when the service is started. When the service is settled, the
consumption amount will be deducted from the authorized fund, and the rest will be returned to the
user.

**`example`**

```ts
const { status } = await bn.authCapture({
  certSn: string,
  merchantId: string,
  noncestr: string,
  cashierId: string,
  timeStamp: string,
  paySign: string,
});
```

Parameters

| Name       | Type                 |
| :--------- | :------------------- |
| `options?` | `AuthCaptureOptions` |

Returns

`Promise`<`AuthCaptureResponse`\>

## Interface: AuthCaptureOptions

| Name       | Type     | Description                                                                                                           |
| :--------- | :------- | :-------------------------------------------------------------------------------------------------------------------- |
| certSn     | `string` | API identity key issued by Binance payment system                                                                     |
| merchantId | `string` | The merchant account id, issued when merchant been created at Binance.                                                |
| noncestr   | `string` | A random string with 32 bytes, e.g. random ascii decimal within a-z and A-Z and loop 32 times to form a random string |
| cashierId  | `string` | The cashierId got from generateCashierUrl API                                                                         |
| timeStamp  | `string` | UnixTimestamp in millisecond that the requests send, guarantee the machine time is sync with the network              |
| paySign    | `string` | A signature generated according to a certain logic.                                                                   |

## Interface: AuthCaptureResponse

| Name   | Type     | Description                          |
| :----- | :------- | :----------------------------------- |
| status | `string` | "SUCCESS" or "FAIL". "0" for success |