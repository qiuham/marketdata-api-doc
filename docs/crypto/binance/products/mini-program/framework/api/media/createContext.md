---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/createContext
api_type: Guide
updated_at: 2026-11-22 18:43:00.308679
---

# bn.createContext

▸ **createContext**(`id`, `options?`): `any`

**`description`** create render context object with component element id. no need to call
createSelectorQuery any more

**`example`**

```ts
const videoContext = bn.createContext("test-id", "video");
const webviewContext = bn.createContext("test-id", { type: "webview-component", rendererId: 1 });
```

Parameters

| Name       | Type                                       |
| :--------- | :----------------------------------------- |
| `id`       | `string`                                   |
| `options?` | `CmdCreateContextOptions` \| `ContextType` |

Returns

`any`

Any

## Interface: CmdCreateContextOptions

| Name        | Type          | Description |
| :---------- | :------------ | :---------- |
| type?       | `ContextType` |             |
| rendererId? | `number`      |             |

## ContextType

Ƭ **ContextType**: `"video"` \| `"custom-native-component"` \| `"webview-component"` \| `"editor"`

---

# bn.createContext

▸ **createContext**(`id`, `options?`): `any`

**`description`** create render context object with component element id. no need to call
createSelectorQuery any more

**`example`**

```ts
const videoContext = bn.createContext("test-id", "video");
const webviewContext = bn.createContext("test-id", { type: "webview-component", rendererId: 1 });
```

Parameters

| Name       | Type                                       |
| :--------- | :----------------------------------------- |
| `id`       | `string`                                   |
| `options?` | `CmdCreateContextOptions` \| `ContextType` |

Returns

`any`

Any

## Interface: CmdCreateContextOptions

| Name        | Type          | Description |
| :---------- | :------------ | :---------- |
| type?       | `ContextType` |             |
| rendererId? | `number`      |             |

## ContextType

Ƭ **ContextType**: `"video"` \| `"custom-native-component"` \| `"webview-component"` \| `"editor"`