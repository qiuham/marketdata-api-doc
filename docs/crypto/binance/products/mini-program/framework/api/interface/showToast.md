---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/showToast
api_type: Guide
updated_at: 2026-11-25 18:46:22.121575
---

# bn.showToast

▸ **showToast**(`options?`): `Promise`<`void`\>

**`description`** The api to show toast

**`remark`** supported jssdk >= 1.1.0

**`example`**

```ts
bn.showToast({
  title: "Success!",
  icon: "success",
  duration: 2000,
});
```

Parameters

| Name       | Type                          |
| :--------- | :---------------------------- |
| `options?` | `Partial`<`CmdToastOptions`\> |

Returns

`Promise`<`void`\>

---

## CmdToastOptions

Ƭ **CmdToastOptions**: `Object`

Type declaration

| Name        | Type                                                | Description       |
| :---------- | :-------------------------------------------------- | :---------------- |
| `title`     | `string`                                            | Prompt content    |
| `icon?`     | `"success"` \| `"loading"` \| `"none"` \| `"error"` | icon              |
| `duration?` | `number`                                            | Prompt delay time |

---

# bn.showToast

▸ **showToast**(`options?`): `Promise`<`void`\>

**`description`** The api to show toast

**`remark`** supported jssdk >= 1.1.0

**`example`**

```ts
bn.showToast({
  title: "Success!",
  icon: "success",
  duration: 2000,
});
```

Parameters

| Name       | Type                          |
| :--------- | :---------------------------- |
| `options?` | `Partial`<`CmdToastOptions`\> |

Returns

`Promise`<`void`\>

---

## CmdToastOptions

Ƭ **CmdToastOptions**: `Object`

Type declaration

| Name        | Type                                                | Description       |
| :---------- | :-------------------------------------------------- | :---------------- |
| `title`     | `string`                                            | Prompt content    |
| `icon?`     | `"success"` \| `"loading"` \| `"none"` \| `"error"` | icon              |
| `duration?` | `number`                                            | Prompt delay time |