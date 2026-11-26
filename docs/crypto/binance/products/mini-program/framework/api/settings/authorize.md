---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/settings/authorize
api_type: Guide
updated_at: 2026-11-26 18:44:55.777115
---

# bn.authorize

▸ **authorize**(`scope`): `Promise`<{}\>

**`description`** Request user's authorization. Once called a dialog will be promoted to ask for
access to user's data. If users have granted the authorization before, the dialog will not be shown
and return success immediately.

**`example`**

```ts
bn.authorize({ scope: "scope.userLocation" })
  .then((res) => console.log(`[authorize] SUCCESS:`, res))
  .catch((err) => console.log(`[authorize] ERROR:`, err));
```

Parameters

| Name    | Type          |
| :------ | :------------ |
| `scope` | `AuthOptions` |

Returns

`Promise`<{}\>

---

## AuthOptions

Ƭ **AuthOptions**: `Object`

Type declaration

| Name    | Type     | Description                                                  |
| :------ | :------- | :----------------------------------------------------------- |
| `scope` | `string` | The scope of authorization requested. e.g scope.userLocation |

---

---

# bn.authorize

▸ **authorize**(`scope`): `Promise`<{}\>

**`description`** Request user's authorization. Once called a dialog will be promoted to ask for
access to user's data. If users have granted the authorization before, the dialog will not be shown
and return success immediately.

**`example`**

```ts
bn.authorize({ scope: "scope.userLocation" })
  .then((res) => console.log(`[authorize] SUCCESS:`, res))
  .catch((err) => console.log(`[authorize] ERROR:`, err));
```

Parameters

| Name    | Type          |
| :------ | :------------ |
| `scope` | `AuthOptions` |

Returns

`Promise`<{}\>

---

## AuthOptions

Ƭ **AuthOptions**: `Object`

Type declaration

| Name    | Type     | Description                                                  |
| :------ | :------- | :----------------------------------------------------------- |
| `scope` | `string` | The scope of authorization requested. e.g scope.userLocation |

---