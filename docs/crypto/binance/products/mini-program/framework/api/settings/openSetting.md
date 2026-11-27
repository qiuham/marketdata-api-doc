---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/settings/openSetting
api_type: Guide
updated_at: 2026-11-27 18:43:20.660228
---

# bn.openSetting

▸ **openSetting**(): `Promise`<`Settings`\>

**`description`** Set up the client Mini Program setup interface, return the result of user setup.
The interface only contains what the Mini Program has already requested from the user.

**`example`**

```ts
const res = await bn.openSetting();
console.log(res.authSetting);
```

Returns

`Promise`<`Settings`\>

## Settings

Ƭ **Settings**: `Object`

Type declaration

| Name          | Type           | Description                 |
| :------------ | :------------- | :-------------------------- |
| `authSetting` | `AuthSettings` | Result of user's permission |

---

## AuthSettings

Ƭ **AuthSettings**: `Object`

Type declaration

| Name                      | Type      | Description                |
| :------------------------ | :-------- | :------------------------- |
| `scope.camera?`           | `boolean` | camera                     |
| `scope.userLocation?`     | `boolean` | physical location          |
| `scope.writePhotosAlbum?` | `boolean` | add picture to photo album |

---

# bn.openSetting

▸ **openSetting**(): `Promise`<`Settings`\>

**`description`** Set up the client Mini Program setup interface, return the result of user setup.
The interface only contains what the Mini Program has already requested from the user.

**`example`**

```ts
const res = await bn.openSetting();
console.log(res.authSetting);
```

Returns

`Promise`<`Settings`\>

## Settings

Ƭ **Settings**: `Object`

Type declaration

| Name          | Type           | Description                 |
| :------------ | :------------- | :-------------------------- |
| `authSetting` | `AuthSettings` | Result of user's permission |

---

## AuthSettings

Ƭ **AuthSettings**: `Object`

Type declaration

| Name                      | Type      | Description                |
| :------------------------ | :-------- | :------------------------- |
| `scope.camera?`           | `boolean` | camera                     |
| `scope.userLocation?`     | `boolean` | physical location          |
| `scope.writePhotosAlbum?` | `boolean` | add picture to photo album |