---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/getDeviceInfo
api_type: Guide
updated_at: 2026-11-24 18:48:32.415301
---

# bn.getDeviceInfo

▸ **getDeviceInfo**(): `DeviceInfo`

**`description`** The api to get system window info

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
const deviceInfo = bn.getDeviceInfo();
console.log(deviceInfo.abi);
console.log(deviceInfo.benchmarkLevel);
console.log(deviceInfo.brand);
console.log(deviceInfo.model);
console.log(deviceInfo.platform);
console.log(deviceInfo.system);
```

Returns

`DeviceInfo`

DeviceInfo

## DeviceInfo

Ƭ **DeviceInfo**: `Object`

Type declaration

| Name       | Type     | Description                                                                                    |
| :--------- | :------- | :--------------------------------------------------------------------------------------------- |
| `brand`    | `string` | Equipment brand                                                                                |
| `model`    | `string` | Device model. New models will show unknown for a while, WeChat will adapt as soon as possible. |
| `system`   | `string` | Operating System and Version                                                                   |
| `platform` | `string` | Client platform                                                                                |

---

---

# bn.getDeviceInfo

▸ **getDeviceInfo**(): `DeviceInfo`

**`description`** The api to get system window info

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
const deviceInfo = bn.getDeviceInfo();
console.log(deviceInfo.abi);
console.log(deviceInfo.benchmarkLevel);
console.log(deviceInfo.brand);
console.log(deviceInfo.model);
console.log(deviceInfo.platform);
console.log(deviceInfo.system);
```

Returns

`DeviceInfo`

DeviceInfo

## DeviceInfo

Ƭ **DeviceInfo**: `Object`

Type declaration

| Name       | Type     | Description                                                                                    |
| :--------- | :------- | :--------------------------------------------------------------------------------------------- |
| `brand`    | `string` | Equipment brand                                                                                |
| `model`    | `string` | Device model. New models will show unknown for a while, WeChat will adapt as soon as possible. |
| `system`   | `string` | Operating System and Version                                                                   |
| `platform` | `string` | Client platform                                                                                |

---