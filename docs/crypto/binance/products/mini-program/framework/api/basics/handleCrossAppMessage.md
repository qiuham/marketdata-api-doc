---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/handleCrossAppMessage
api_type: Guide
updated_at: 2026-11-24 18:48:17.257208
---

# bn.handleCrossAppMessage

▸ **handleCrossAppMessage**(`action`, `callback`): `void`

**`description`** Used for handle cross mini-app communication. A same action name can only be
registered once. Otherwise, the later one will be ignored.

**`remark`** supported jssdk > 4.26.0

**`example`**

```ts
bn.handleCrossAppMessage("action", (options) => {
  console.log(options);
  return { code: 0 };
});

bn.handleCrossAppMessage("wrong-action", (options) => {
  throw { code: 1, message: "error" };
});
```

Parameters

| Name       | Type                                                            |
| :--------- | :-------------------------------------------------------------- |
| `action`   | `string`                                                        |
| `callback` | (`options`: `undefined` \| `Record`<`string`, `any`\>) => `any` |

Returns

`void`

---

# bn.handleCrossAppMessage

▸ **handleCrossAppMessage**(`action`, `callback`): `void`

**`description`** Used for handle cross mini-app communication. A same action name can only be
registered once. Otherwise, the later one will be ignored.

**`remark`** supported jssdk > 4.26.0

**`example`**

```ts
bn.handleCrossAppMessage("action", (options) => {
  console.log(options);
  return { code: 0 };
});

bn.handleCrossAppMessage("wrong-action", (options) => {
  throw { code: 1, message: "error" };
});
```

Parameters

| Name       | Type                                                            |
| :--------- | :-------------------------------------------------------------- |
| `action`   | `string`                                                        |
| `callback` | (`options`: `undefined` \| `Record`<`string`, `any`\>) => `any` |

Returns

`void`