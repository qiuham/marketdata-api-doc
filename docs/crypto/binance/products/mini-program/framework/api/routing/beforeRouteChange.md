---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/routing/beforeRouteChange
api_type: Guide
updated_at: 2026-11-25 18:44:36.937392
---

# bn.beforeRouteChange

▸ **beforeRouteChange**(`guard`): () => `NavigationGuard`[]

**`description`** Register a route change guard.

**`example`**

```ts
bn.beforeRouteChange((to, from, next) => {
  if (to.path === "/pages/protected/index") {
    // Perform authentication check
    if (isAuthenticated()) {
      next();
    } else {
      bn.navigateTo({ url: "/pages/login/index" });
    }
  } else {
    next();
  }
});
```

Parameters

| Name    | Type              |
| :------ | :---------------- |
| `guard` | `NavigationGuard` |

Returns

`fn`

▸ (): `NavigationGuard`[]

Returns

`NavigationGuard`[]

## NavigationGuard

Ƭ **NavigationGuard**: (`to`: `INavigationTo`, `from`: `INavigationFrom`, `next`: () => `void`) =>
`Promise`<`Any`\> \| `void`

Type declaration

▸ (`to`, `from`, `next`): `Promise`<`Any`\> \| `void`

Parameters

| Name   | Type              |
| :----- | :---------------- |
| `to`   | `INavigationTo`   |
| `from` | `INavigationFrom` |
| `next` | () => `void`      |

Returns

`Promise`<`Any`\> \| `void`

---

## Interface: INavigationTo

| Name     | Type                     | Description |
| :------- | :----------------------- | :---------- |
| type     | `RouteChangeType`        |             |
| path     | `string`                 |             |
| query    | `string`                 |             |
| payload? | `EventTabItemTapOptions` |             |

## Interface: INavigationFrom

| Name  | Type     | Description |
| :---- | :------- | :---------- |
| path  | `string` |             |
| query | `string` |             |

## Any

Ƭ **Any**: `any`

---

---

# bn.beforeRouteChange

▸ **beforeRouteChange**(`guard`): () => `NavigationGuard`[]

**`description`** Register a route change guard.

**`example`**

```ts
bn.beforeRouteChange((to, from, next) => {
  if (to.path === "/pages/protected/index") {
    // Perform authentication check
    if (isAuthenticated()) {
      next();
    } else {
      bn.navigateTo({ url: "/pages/login/index" });
    }
  } else {
    next();
  }
});
```

Parameters

| Name    | Type              |
| :------ | :---------------- |
| `guard` | `NavigationGuard` |

Returns

`fn`

▸ (): `NavigationGuard`[]

Returns

`NavigationGuard`[]

## NavigationGuard

Ƭ **NavigationGuard**: (`to`: `INavigationTo`, `from`: `INavigationFrom`, `next`: () => `void`) =>
`Promise`<`Any`\> \| `void`

Type declaration

▸ (`to`, `from`, `next`): `Promise`<`Any`\> \| `void`

Parameters

| Name   | Type              |
| :----- | :---------------- |
| `to`   | `INavigationTo`   |
| `from` | `INavigationFrom` |
| `next` | () => `void`      |

Returns

`Promise`<`Any`\> \| `void`

---

## Interface: INavigationTo

| Name     | Type                     | Description |
| :------- | :----------------------- | :---------- |
| type     | `RouteChangeType`        |             |
| path     | `string`                 |             |
| query    | `string`                 |             |
| payload? | `EventTabItemTapOptions` |             |

## Interface: INavigationFrom

| Name  | Type     | Description |
| :---- | :------- | :---------- |
| path  | `string` |             |
| query | `string` |             |

## Any

Ƭ **Any**: `any`

---