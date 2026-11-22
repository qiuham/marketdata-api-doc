---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/addPhoneRepeatCalendar
api_type: Guide
updated_at: 2026-11-22 18:45:46.816269
---

# bn.addPhoneRepeatCalendar

▸ **addPhoneRepeatCalendar**(`options`): `Promise`<{}\>

**`description`** Add events to the system calendar

**`remark`** supported jssdk > 4.47.0

**`example`**

```ts
const res = await bn.addPhoneRepeatCalendar({
  title: "Project Kickoff Meeting",
  startTime: 1687075200, // Unix timestamp for 2023-06-18 10:00:00 UTC
  endTime: 1687082400, // Unix timestamp for 2023-06-18 12:00:00 UTC
  allDay: false,
  description: "Discuss project goals and timeline",
  location: "Conference Room A",
  alarm: true,
  alarmOffset: 900, // Alarm 15 minutes before start
  repeatInterval: "month", // Repeat every month
  repeatEndTime: 1718534400, // Repeat until 2024-06-18 10:00:00 UTC
});
```

Parameters

| Name      | Type                            |
| :-------- | :------------------------------ |
| `options` | `AddPhoneRepeatCalendarOptions` |

Returns

`Promise`<{}\>

## Interface: AddPhoneRepeatCalendarOptions

| Name            | Type                                         | Description                                                                                                                                                                                                                |
| :-------------- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| repeatInterval? | `"year"` \| `"month"` \| `"day"` \| `"week"` | Repeat interval.; Default is 'month' (repeat every month).Valid values:- 'day': repeat every day; - 'week': repeat every week; - 'month': repeat every month (date cannot be greater than 28); - 'year': repeat every year |
| repeatEndTime?  | `number`                                     | Unix timestamp for the end time of the repeat period.; If not provided, the event repeats indefinitely.                                                                                                                    |
| title           | `string`                                     | Event title, required                                                                                                                                                                                                      |
| startTime       | `number`                                     | Start time as a Unix timestamp, required                                                                                                                                                                                   |
| allDay?         | `boolean`                                    | Whether the event lasts all day, default is false                                                                                                                                                                          |
| description?    | `string`                                     | Event description                                                                                                                                                                                                          |
| location?       | `string`                                     | Event location                                                                                                                                                                                                             |
| endTime?        | `number`                                     | End time as a Unix timestamp, defaults to startTime if not provided                                                                                                                                                        |
| alarm?          | `boolean`                                    | Whether to set an alarm, default is true                                                                                                                                                                                   |
| alarmOffset?    | `number`                                     | Alarm offset in seconds, default 0 means alarm at start time                                                                                                                                                               |

---

# bn.addPhoneRepeatCalendar

▸ **addPhoneRepeatCalendar**(`options`): `Promise`<{}\>

**`description`** Add events to the system calendar

**`remark`** supported jssdk > 4.47.0

**`example`**

```ts
const res = await bn.addPhoneRepeatCalendar({
  title: "Project Kickoff Meeting",
  startTime: 1687075200, // Unix timestamp for 2023-06-18 10:00:00 UTC
  endTime: 1687082400, // Unix timestamp for 2023-06-18 12:00:00 UTC
  allDay: false,
  description: "Discuss project goals and timeline",
  location: "Conference Room A",
  alarm: true,
  alarmOffset: 900, // Alarm 15 minutes before start
  repeatInterval: "month", // Repeat every month
  repeatEndTime: 1718534400, // Repeat until 2024-06-18 10:00:00 UTC
});
```

Parameters

| Name      | Type                            |
| :-------- | :------------------------------ |
| `options` | `AddPhoneRepeatCalendarOptions` |

Returns

`Promise`<{}\>

## Interface: AddPhoneRepeatCalendarOptions

| Name            | Type                                         | Description                                                                                                                                                                                                                |
| :-------------- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| repeatInterval? | `"year"` \| `"month"` \| `"day"` \| `"week"` | Repeat interval.; Default is 'month' (repeat every month).Valid values:- 'day': repeat every day; - 'week': repeat every week; - 'month': repeat every month (date cannot be greater than 28); - 'year': repeat every year |
| repeatEndTime?  | `number`                                     | Unix timestamp for the end time of the repeat period.; If not provided, the event repeats indefinitely.                                                                                                                    |
| title           | `string`                                     | Event title, required                                                                                                                                                                                                      |
| startTime       | `number`                                     | Start time as a Unix timestamp, required                                                                                                                                                                                   |
| allDay?         | `boolean`                                    | Whether the event lasts all day, default is false                                                                                                                                                                          |
| description?    | `string`                                     | Event description                                                                                                                                                                                                          |
| location?       | `string`                                     | Event location                                                                                                                                                                                                             |
| endTime?        | `number`                                     | End time as a Unix timestamp, defaults to startTime if not provided                                                                                                                                                        |
| alarm?          | `boolean`                                    | Whether to set an alarm, default is true                                                                                                                                                                                   |
| alarmOffset?    | `number`                                     | Alarm offset in seconds, default 0 means alarm at start time                                                                                                                                                               |