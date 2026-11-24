---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/dateTimeFormat
api_type: Guide
updated_at: 2026-11-24 18:45:04.477954
---

# bn.dateTimeFormat

▸ **dateTimeFormat**(`timestamp`, `options`): `string`

**`description`** format date time.

**`remark`** supported jssdk >= 4.36.0

**`example`**

```ts
bn.dateTimeFormat(1659971700000, {
  year: "numeric",
  month: "short",
  day: "numeric",
});
// => "Aug 8, 2022"

bn.dateTimeFormat(1659971700000, {
  hour: "numeric",
  minute: "numeric",
});
// => "11:15 PM"
```

Parameters

| Name        | Type                    |
| :---------- | :---------------------- |
| `timestamp` | `number`                |
| `options`   | `DateTimeFormatOptions` |

Returns

`string`

string

## Interface: DateTimeFormatOptions

| Name       | Type                                                              | Description |
| :--------- | :---------------------------------------------------------------- | :---------- |
| weekday?   | `"long"` \| `"short"` \| `"narrow"`                               |             |
| year?      | `"numeric"` \| `"2-digit"`                                        |             |
| month?     | `"long"` \| `"short"` \| `"narrow"` \| `"numeric"` \| `"2-digit"` |             |
| day?       | `"numeric"` \| `"2-digit"`                                        |             |
| hour?      | `"numeric"` \| `"2-digit"`                                        |             |
| minute?    | `"numeric"` \| `"2-digit"`                                        |             |
| second?    | `"numeric"` \| `"2-digit"`                                        |             |
| dateStyle? | `"medium"` \| `"long"` \| `"short"` \| `"full"`                   |             |
| timeStyle? | `"medium"` \| `"long"` \| `"short"` \| `"full"`                   |             |

---

# bn.dateTimeFormat

▸ **dateTimeFormat**(`timestamp`, `options`): `string`

**`description`** format date time.

**`remark`** supported jssdk >= 4.36.0

**`example`**

```ts
bn.dateTimeFormat(1659971700000, {
  year: "numeric",
  month: "short",
  day: "numeric",
});
// => "Aug 8, 2022"

bn.dateTimeFormat(1659971700000, {
  hour: "numeric",
  minute: "numeric",
});
// => "11:15 PM"
```

Parameters

| Name        | Type                    |
| :---------- | :---------------------- |
| `timestamp` | `number`                |
| `options`   | `DateTimeFormatOptions` |

Returns

`string`

string

## Interface: DateTimeFormatOptions

| Name       | Type                                                              | Description |
| :--------- | :---------------------------------------------------------------- | :---------- |
| weekday?   | `"long"` \| `"short"` \| `"narrow"`                               |             |
| year?      | `"numeric"` \| `"2-digit"`                                        |             |
| month?     | `"long"` \| `"short"` \| `"narrow"` \| `"numeric"` \| `"2-digit"` |             |
| day?       | `"numeric"` \| `"2-digit"`                                        |             |
| hour?      | `"numeric"` \| `"2-digit"`                                        |             |
| minute?    | `"numeric"` \| `"2-digit"`                                        |             |
| second?    | `"numeric"` \| `"2-digit"`                                        |             |
| dateStyle? | `"medium"` \| `"long"` \| `"short"` \| `"full"`                   |             |
| timeStyle? | `"medium"` \| `"long"` \| `"short"` \| `"full"`                   |             |