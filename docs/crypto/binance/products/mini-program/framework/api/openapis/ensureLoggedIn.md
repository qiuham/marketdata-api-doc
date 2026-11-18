---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/ensureLoggedIn
api_type: Guide
updated_at: 2026-11-18 02:36:34.110843
---

# bn.ensureLoggedIn

▸ **ensureLoggedIn**(): `Promise`<`EnsureLoggedInResponse`\>

**`description`** Ensure user has logged in, if not, show login dialog. Return user log in result

**`example`**

```ts
const { alreadyLogged, logged, abort } = await bn.ensureLoggedIn();
```

Returns

`Promise`<`EnsureLoggedInResponse`\>

## Interface: EnsureLoggedInResponse

| Name          | Type      | Description                                                                                                              |
| :------------ | :-------- | :----------------------------------------------------------------------------------------------------------------------- |
| abort         | `boolean` | User aborts logging in                                                                                                   |
| alreadyLogged | `boolean` | already logged                                                                                                           |
| logged        | `boolean` | If the user logged out before calling ensureLogged(), and has logged in successfully, then this property should be true. |

---

# bn.ensureLoggedIn

▸ **ensureLoggedIn**(): `Promise`<`EnsureLoggedInResponse`\>

**`description`** Ensure user has logged in, if not, show login dialog. Return user log in result

**`example`**

```ts
const { alreadyLogged, logged, abort } = await bn.ensureLoggedIn();
```

Returns

`Promise`<`EnsureLoggedInResponse`\>

## Interface: EnsureLoggedInResponse

| Name          | Type      | Description                                                                                                              |
| :------------ | :-------- | :----------------------------------------------------------------------------------------------------------------------- |
| abort         | `boolean` | User aborts logging in                                                                                                   |
| alreadyLogged | `boolean` | already logged                                                                                                           |
| logged        | `boolean` | If the user logged out before calling ensureLogged(), and has logged in successfully, then this property should be true. |