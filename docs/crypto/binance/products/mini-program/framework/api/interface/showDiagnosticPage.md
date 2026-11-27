---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/showDiagnosticPage
api_type: Guide
updated_at: 2026-11-27 18:45:22.874031
---

# bn.showDiagnosticPage

▸ **showDiagnosticPage**(`options?`): `Promise`<`void`\>

**`description`** Show an diagnostic page with the specified options. support msv >= 4.39.0

**`example`**

```ts
bn.onPageNotFound({
  description: "The page you are looking for does not exist. Please try again.",
  actions: ["log-submit", "cache-clear"],
});
```

Parameters

| Name       | Type                    |
| :--------- | :---------------------- |
| `options?` | `PageDiagnosticOptions` |

Returns

`Promise`<`void`\>

## Interface: PageDiagnosticOptions

| Name            | Type                                  | Description |
| :-------------- | :------------------------------------ | :---------- |
| description?    | `string`                              |             |
| descriptionKey? | `string`                              |             |
| actions?        | (`"log-submit"` \| `"cache-clear"`)[] |             |

---

# bn.showDiagnosticPage

▸ **showDiagnosticPage**(`options?`): `Promise`<`void`\>

**`description`** Show an diagnostic page with the specified options. support msv >= 4.39.0

**`example`**

```ts
bn.onPageNotFound({
  description: "The page you are looking for does not exist. Please try again.",
  actions: ["log-submit", "cache-clear"],
});
```

Parameters

| Name       | Type                    |
| :--------- | :---------------------- |
| `options?` | `PageDiagnosticOptions` |

Returns

`Promise`<`void`\>

## Interface: PageDiagnosticOptions

| Name            | Type                                  | Description |
| :-------------- | :------------------------------------ | :---------- |
| description?    | `string`                              |             |
| descriptionKey? | `string`                              |             |
| actions?        | (`"log-submit"` \| `"cache-clear"`)[] |             |