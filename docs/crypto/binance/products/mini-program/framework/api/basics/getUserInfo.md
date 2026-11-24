---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/getUserInfo
api_type: Guide
updated_at: 2026-11-24 18:48:20.343950
---

# bn.getUserInfo

▸ **getUserInfo**(): `Promise`<`UserInfoResponse`\>

**`description`** Get user information, including sensitive information such as encryptedData.

**`example`**

```ts
bn.getUserInfo({
  success: (res) => {
    console.log(res.userInfo);
  },
});
```

Returns

`Promise`<`UserInfoResponse`\>

---

## UserInfoResponse

Ƭ **UserInfoResponse**: `Object`

Type declaration

| Name       | Type       |
| :--------- | :--------- |
| `userInfo` | `UserInfo` |

---

## Interface: UserInfo

| Name | Type | Description |
| :--- | :--- | :---------- |

---

# bn.getUserInfo

▸ **getUserInfo**(): `Promise`<`UserInfoResponse`\>

**`description`** Get user information, including sensitive information such as encryptedData.

**`example`**

```ts
bn.getUserInfo({
  success: (res) => {
    console.log(res.userInfo);
  },
});
```

Returns

`Promise`<`UserInfoResponse`\>

---

## UserInfoResponse

Ƭ **UserInfoResponse**: `Object`

Type declaration

| Name       | Type       |
| :--------- | :--------- |
| `userInfo` | `UserInfo` |

---

## Interface: UserInfo

| Name | Type | Description |
| :--- | :--- | :---------- |