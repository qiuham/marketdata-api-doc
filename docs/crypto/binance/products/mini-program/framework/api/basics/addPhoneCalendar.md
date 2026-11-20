---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/addPhoneCalendar
api_type: Guide
updated_at: 2026-11-20 18:50:07.263866
---

# bn.addPhoneCalendar

▸ **addPhoneCalendar**(`options`): `Promise`<{}\>

**`description`** Add events to the system calendar

**`remark`** supported jssdk > 4.47.0

**`example`**

```ts
const res = await bn.addPhoneCalendar({
  title: "Project Kickoff Meeting",
  startTime: 1687075200, // Unix timestamp for 2023-06-18 10:00:00 UTC
  endTime: 1687082400, // Unix timestamp for 2023-06-18 12:00:00 UTC
  allDay: false,
  description: "Discuss project goals and timeline",
  location: "Conference Room A",
  alarm: true,
  alarmOffset: 900, // Alarm 15 minutes before start
});
```

Parameters

| Name      | Type                      |
| :-------- | :------------------------ |
| `options` | `AddPhoneCalendarOptions` |

Returns

`Promise`<{}\>

---

## Interface: AddPhoneCalendarOptions

| Name         | Type      | Description                                                         |
| :----------- | :-------- | :------------------------------------------------------------------ |
| title        | `string`  | Event title, required                                               |
| startTime    | `number`  | Start time as a Unix timestamp, required                            |
| allDay?      | `boolean` | Whether the event lasts all day, default is false                   |
| description? | `string`  | Event description                                                   |
| location?    | `string`  | Event location                                                      |
| endTime?     | `number`  | End time as a Unix timestamp, defaults to startTime if not provided |
| alarm?       | `boolean` | Whether to set an alarm, default is true                            |
| alarmOffset? | `number`  | Alarm offset in seconds, default 0 means alarm at start time        |

---

# bn.addPhoneCalendar

▸ **addPhoneCalendar**(`options`): `Promise`<{}\>

**`description`** Add events to the system calendar

**`remark`** supported jssdk > 4.47.0

**`example`**

```ts
const res = await bn.addPhoneCalendar({
  title: "Project Kickoff Meeting",
  startTime: 1687075200, // Unix timestamp for 2023-06-18 10:00:00 UTC
  endTime: 1687082400, // Unix timestamp for 2023-06-18 12:00:00 UTC
  allDay: false,
  description: "Discuss project goals and timeline",
  location: "Conference Room A",
  alarm: true,
  alarmOffset: 900, // Alarm 15 minutes before start
});
```

Parameters

| Name      | Type                      |
| :-------- | :------------------------ |
| `options` | `AddPhoneCalendarOptions` |

Returns

`Promise`<{}\>

---

## Interface: AddPhoneCalendarOptions

| Name         | Type      | Description                                                         |
| :----------- | :-------- | :------------------------------------------------------------------ |
| title        | `string`  | Event title, required                                               |
| startTime    | `number`  | Start time as a Unix timestamp, required                            |
| allDay?      | `boolean` | Whether the event lasts all day, default is false                   |
| description? | `string`  | Event description                                                   |
| location?    | `string`  | Event location                                                      |
| endTime?     | `number`  | End time as a Unix timestamp, defaults to startTime if not provided |
| alarm?       | `boolean` | Whether to set an alarm, default is true                            |
| alarmOffset? | `number`  | Alarm offset in seconds, default 0 means alarm at start time        |