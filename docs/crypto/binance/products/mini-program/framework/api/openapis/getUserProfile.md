---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/getUserProfile
api_type: Guide
updated_at: 2026-11-26 18:45:31.578251
---

# bn.getUserProfile

▸ **getUserProfile**(): `Promise`<`UserProfileResponse`\>

**`description`** Get user information. The page generates a click event(such as button). Each
request will pop up an authorization window after the user agrees to return userInfo

**`example`**

```ts
bn.getUserProfile({
  desc: "Used to improve member information",
  success: (res) => {
    this.setData({
      userInfo: res.userInfo,
      hasUserInfo: true,
    });
  },
});
```

Returns

`Promise`<`UserProfileResponse`\>

UserProfileResponse

## UserProfileResponse

Ƭ **UserProfileResponse**: `Object`

Type declaration

| Name       | Type       |
| :--------- | :--------- |
| `userInfo` | `UserInfo` |

---

## UserInfo

Ƭ **UserInfo**: `Object`

Type declaration

| Name        | Type     | Description                           |
| :---------- | :------- | :------------------------------------ |
| `nickName`  | `string` | User's Nickname                       |
| `avatarUrl` | `string` | The URL of the user's avatar picture. |

---

# bn.getUserProfile

▸ **getUserProfile**(): `Promise`<`UserProfileResponse`\>

**`description`** Get user information. The page generates a click event(such as button). Each
request will pop up an authorization window after the user agrees to return userInfo

**`example`**

```ts
bn.getUserProfile({
  desc: "Used to improve member information",
  success: (res) => {
    this.setData({
      userInfo: res.userInfo,
      hasUserInfo: true,
    });
  },
});
```

Returns

`Promise`<`UserProfileResponse`\>

UserProfileResponse

## UserProfileResponse

Ƭ **UserProfileResponse**: `Object`

Type declaration

| Name       | Type       |
| :--------- | :--------- |
| `userInfo` | `UserInfo` |

---

## UserInfo

Ƭ **UserInfo**: `Object`

Type declaration

| Name        | Type     | Description                           |
| :---------- | :------- | :------------------------------------ |
| `nickName`  | `string` | User's Nickname                       |
| `avatarUrl` | `string` | The URL of the user's avatar picture. |