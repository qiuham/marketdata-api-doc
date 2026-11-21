---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/setTabBarItem
api_type: Guide
updated_at: 2026-11-21 18:46:12.369014
---

# bn.setTabBarItem

▸ **setTabBarItem**(`options`): `Promise`<{}\>

**`description`** Dynamically set the content of a tabBar item

**`example`**

```ts
bn.setTabBarItem({
  index: 0,
  text: "text",
  iconPath: "/path/to/iconPath",
  selectedIconPath: "/path/to/selectedIconPath",
});
```

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `TabBarItemOptions` |

Returns

`Promise`<{}\>

---

## TabBarItemOptions

Ƭ **TabBarItemOptions**: `Object`

Type declaration

| Name                | Type     | Description                                                                                                                                               |
| :------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `index`             | `number` | Which item of the tabBar, counting from the left                                                                                                          |
| `text?`             | `string` | button text on tab                                                                                                                                        |
| `iconPath?`         | `string` | Image path, icon size is limited to 40kb, recommended size is 81px \* 81px, when position is top, this parameter is invalid                               |
| `selectedIconPath?` | `string` | The image path when selected, the icon size is limited to 40kb, the recommended size is 81px \* 81px, when the position is top, this parameter is invalid |

---

---

# bn.setTabBarItem

▸ **setTabBarItem**(`options`): `Promise`<{}\>

**`description`** Dynamically set the content of a tabBar item

**`example`**

```ts
bn.setTabBarItem({
  index: 0,
  text: "text",
  iconPath: "/path/to/iconPath",
  selectedIconPath: "/path/to/selectedIconPath",
});
```

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `TabBarItemOptions` |

Returns

`Promise`<{}\>

---

## TabBarItemOptions

Ƭ **TabBarItemOptions**: `Object`

Type declaration

| Name                | Type     | Description                                                                                                                                               |
| :------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `index`             | `number` | Which item of the tabBar, counting from the left                                                                                                          |
| `text?`             | `string` | button text on tab                                                                                                                                        |
| `iconPath?`         | `string` | Image path, icon size is limited to 40kb, recommended size is 81px \* 81px, when position is top, this parameter is invalid                               |
| `selectedIconPath?` | `string` | The image path when selected, the icon size is limited to 40kb, the recommended size is 81px \* 81px, when the position is top, this parameter is invalid |

---