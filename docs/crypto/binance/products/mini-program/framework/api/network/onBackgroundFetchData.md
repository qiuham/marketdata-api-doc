---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/onBackgroundFetchData
api_type: Guide
updated_at: 2026-11-23 18:45:30.802328
---

# bn.onBackgroundFetchData

▸ **onBackgroundFetchData**(`callback`): `void`

**`description`** Listen on backgroundFetch getting data event. If the event has finished when
listening on, it will not be triggered.

**`example`**

```ts
bn.onBackgroundFetchData((res) => {
  const { fetchType, fetchedData, timeStamp } = res;
});
```

Parameters

| Name       | Type                            |
| :--------- | :------------------------------ |
| `callback` | `OnBackgroundFetchDataCallback` |

Returns

`void`

## OnBackgroundFetchDataCallback

Ƭ **OnBackgroundFetchDataCallback**: (`result`: { `fetchType`: `"periodic"` \| `"pre"` ;
`fetchedData`: `string` ; `timeStamp`: `number` }) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name                 | Type                    | Description                                          |
| :------------------- | :---------------------- | :--------------------------------------------------- |
| `result`             | `Object`                | -                                                    |
| `result.fetchType`   | `"periodic"` \| `"pre"` | Cache data category, with a value of periodic or pre |
| `result.fetchedData` | `string`                | Cache data                                           |
| `result.timeStamp`   | `number`                | The timestamp of client getting the cached data      |

Returns

`void`

---

# bn.onBackgroundFetchData

▸ **onBackgroundFetchData**(`callback`): `void`

**`description`** Listen on backgroundFetch getting data event. If the event has finished when
listening on, it will not be triggered.

**`example`**

```ts
bn.onBackgroundFetchData((res) => {
  const { fetchType, fetchedData, timeStamp } = res;
});
```

Parameters

| Name       | Type                            |
| :--------- | :------------------------------ |
| `callback` | `OnBackgroundFetchDataCallback` |

Returns

`void`

## OnBackgroundFetchDataCallback

Ƭ **OnBackgroundFetchDataCallback**: (`result`: { `fetchType`: `"periodic"` \| `"pre"` ;
`fetchedData`: `string` ; `timeStamp`: `number` }) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name                 | Type                    | Description                                          |
| :------------------- | :---------------------- | :--------------------------------------------------- |
| `result`             | `Object`                | -                                                    |
| `result.fetchType`   | `"periodic"` \| `"pre"` | Cache data category, with a value of periodic or pre |
| `result.fetchedData` | `string`                | Cache data                                           |
| `result.timeStamp`   | `number`                | The timestamp of client getting the cached data      |

Returns

`void`