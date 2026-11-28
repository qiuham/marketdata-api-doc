---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/getUserKycStatus
api_type: Guide
updated_at: 2026-11-28 18:43:09.595969
---

# bn.getUserKycStatus

▸ **getUserKycStatus**(): `Promise`<`GetUserKycStatusResponse`\>

**`description`** Get the user kyc status.

**`remark`** support jssdk >= 4.7.0

**`example`**

```ts
const response = await bn.getUserKycStatus();
```

Returns

`Promise`<`GetUserKycStatusResponse`\>

GetUserKycStatusResponse

## Interface: GetUserKycStatusResponse

| Name      | Type                      | Description                                                                  |
| :-------- | :------------------------ | :--------------------------------------------------------------------------- |
| type      | `"user"` \| `"company"`   | kys type.                                                                    |
| kycStatus | `0` \| `2` \| `1` \| `-1` | kys status: -1 : Unverified, 0 : Verifying, 1 : Verify Pass, 2: Verify Fail. |

---

# bn.getUserKycStatus

▸ **getUserKycStatus**(): `Promise`<`GetUserKycStatusResponse`\>

**`description`** Get the user kyc status.

**`remark`** support jssdk >= 4.7.0

**`example`**

```ts
const response = await bn.getUserKycStatus();
```

Returns

`Promise`<`GetUserKycStatusResponse`\>

GetUserKycStatusResponse

## Interface: GetUserKycStatusResponse

| Name      | Type                      | Description                                                                  |
| :-------- | :------------------------ | :--------------------------------------------------------------------------- |
| type      | `"user"` \| `"company"`   | kys type.                                                                    |
| kycStatus | `0` \| `2` \| `1` \| `-1` | kys status: -1 : Unverified, 0 : Verifying, 1 : Verify Pass, 2: Verify Fail. |