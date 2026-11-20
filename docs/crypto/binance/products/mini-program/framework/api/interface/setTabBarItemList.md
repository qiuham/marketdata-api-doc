---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/setTabBarItemList
api_type: Guide
updated_at: 2026-11-20 18:47:47.848608
---

# bn.setTabBarItemList

▸ **setTabBarItemList**(`options`): `Promise`<{}\>

**`description`** Dynamic set the tabbar list of mini program. The list parameter must be configure
in the tabBar attribute in app.json.

**`example`**

```ts
bn.setTabBarItemList({
  list: ["/pages/index/index", "/pages/logs/logs"],
  selectedIndex: 0,
});
```

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `options` | `TabBarItemListOptions` |

Returns

`Promise`<{}\>

---

## TabBarItemListOptions

Ƭ **TabBarItemListOptions**: `Object`

Type declaration

| Name             | Type       | Description                                                                                                                                                                                                                          |
| :--------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list`           | `string`[] | List accepts an array and can only configure a minimum of 2 and a maximum of 5 tabs. Tab is sorted in the order of the array. Each item is a page path, which must have been configured in the list of tabBar attribute in app.json. |
| `selectedIndex?` | `number`   | Set the selected index of the current tab. If it is not passed, the first tab in the list will be selected.                                                                                                                          |

---

---

# bn.setTabBarItemList

▸ **setTabBarItemList**(`options`): `Promise`<{}\>

**`description`** Dynamic set the tabbar list of mini program. The list parameter must be configure
in the tabBar attribute in app.json.

**`example`**

```ts
bn.setTabBarItemList({
  list: ["/pages/index/index", "/pages/logs/logs"],
  selectedIndex: 0,
});
```

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `options` | `TabBarItemListOptions` |

Returns

`Promise`<{}\>

---

## TabBarItemListOptions

Ƭ **TabBarItemListOptions**: `Object`

Type declaration

| Name             | Type       | Description                                                                                                                                                                                                                          |
| :--------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list`           | `string`[] | List accepts an array and can only configure a minimum of 2 and a maximum of 5 tabs. Tab is sorted in the order of the array. Each item is a page path, which must have been configured in the list of tabBar attribute in app.json. |
| `selectedIndex?` | `number`   | Set the selected index of the current tab. If it is not passed, the first tab in the list will be selected.                                                                                                                          |

---