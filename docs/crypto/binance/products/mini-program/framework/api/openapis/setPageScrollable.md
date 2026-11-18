---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/setPageScrollable
api_type: Guide
updated_at: 2026-11-18 02:35:23.946170
---

# bn.setPageScrollable

▸ **setPageScrollable**(`scrollable`, `options?`): `void`

**`description`** set page scrollable

**`example`**

```ts
bn.setPageScrollable(false);
bn.showModal({
  title: "title",
  content: "content",
  success: function (res) {
    bn.setPageScrollable(true);
  },
  fail: function (res) {
    bn.setPageScrollable(true);
  },
});
```

Parameters

| Name         | Type                          | Description                |
| :----------- | :---------------------------- | :------------------------- |
| `scrollable` | `boolean`                     | whether page is scrollable |
| `options?`   | `CmdSetPageScrollableOptions` | -                          |

Returns

`void`

## Interface: CmdSetPageScrollableOptions

| Name        | Type     | Description |
| :---------- | :------- | :---------- |
| rendererId? | `number` |             |

---

# bn.setPageScrollable

▸ **setPageScrollable**(`scrollable`, `options?`): `void`

**`description`** set page scrollable

**`example`**

```ts
bn.setPageScrollable(false);
bn.showModal({
  title: "title",
  content: "content",
  success: function (res) {
    bn.setPageScrollable(true);
  },
  fail: function (res) {
    bn.setPageScrollable(true);
  },
});
```

Parameters

| Name         | Type                          | Description                |
| :----------- | :---------------------------- | :------------------------- |
| `scrollable` | `boolean`                     | whether page is scrollable |
| `options?`   | `CmdSetPageScrollableOptions` | -                          |

Returns

`void`

## Interface: CmdSetPageScrollableOptions

| Name        | Type     | Description |
| :---------- | :------- | :---------- |
| rendererId? | `number` |             |