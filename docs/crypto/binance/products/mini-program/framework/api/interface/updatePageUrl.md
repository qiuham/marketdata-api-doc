---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/updatePageUrl
api_type: Guide
updated_at: 2026-11-27 18:45:06.762026
---

# bn.updatePageUrl

▸ **updatePageUrl**(`params`): `void`

**`description`** update the url info on the current page for the native.

**`example`**

```ts
bn.updatePageUrl({
  path: "/pages/index/index",
  query: encodeURIComponent("a=1&b=2"),
  // Starting from APP 3.1.0, the developer can call bn.updatePageUrl({path:"", query: "", target:"deeplink"})
  // to update the path and query of deeplink.
  target: "deeplink",
});
```

Parameters

| Name     | Type                               |
| :------- | :--------------------------------- |
| `params` | `CmdSetUpdatePageQueryOptionsType` |

Returns

`void`

## CmdSetUpdatePageQueryOptionsType

Ƭ **CmdSetUpdatePageQueryOptionsType**: `Object`

Type declaration

| Name      | Type                    |
| :-------- | :---------------------- |
| `path`    | `string`                |
| `query?`  | `undefined` \| `string` |
| `target?` | `undefined` \| `string` |

---

# bn.updatePageUrl

▸ **updatePageUrl**(`params`): `void`

**`description`** update the url info on the current page for the native.

**`example`**

```ts
bn.updatePageUrl({
  path: "/pages/index/index",
  query: encodeURIComponent("a=1&b=2"),
  // Starting from APP 3.1.0, the developer can call bn.updatePageUrl({path:"", query: "", target:"deeplink"})
  // to update the path and query of deeplink.
  target: "deeplink",
});
```

Parameters

| Name     | Type                               |
| :------- | :--------------------------------- |
| `params` | `CmdSetUpdatePageQueryOptionsType` |

Returns

`void`

## CmdSetUpdatePageQueryOptionsType

Ƭ **CmdSetUpdatePageQueryOptionsType**: `Object`

Type declaration

| Name      | Type                    |
| :-------- | :---------------------- |
| `path`    | `string`                |
| `query?`  | `undefined` \| `string` |
| `target?` | `undefined` \| `string` |