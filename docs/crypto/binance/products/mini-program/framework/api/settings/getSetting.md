---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/settings/getSetting
api_type: Guide
updated_at: 2026-11-25 18:44:20.244869
---

# bn.getSetting

▸ **getSetting**(): `Promise`<`Settings`\>

**`description`** Gets the user's current settings. The return value only contains what the Mini
Program has already requested from the user.

**`example`**

```ts
const res = await bn.getSetting();
console.log(res.authSetting["scope.userLocation"]); // boolean
```

Returns

`Promise`<`Settings`\>

---

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

# bn.getSetting

▸ **getSetting**(): `Promise`<`Settings`\>

**`description`** Gets the user's current settings. The return value only contains what the Mini
Program has already requested from the user.

**`example`**

```ts
const res = await bn.getSetting();
console.log(res.authSetting["scope.userLocation"]); // boolean
```

Returns

`Promise`<`Settings`\>

---

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