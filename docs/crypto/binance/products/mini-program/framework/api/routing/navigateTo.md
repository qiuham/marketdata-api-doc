---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/routing/navigateTo
api_type: Guide
updated_at: 2026-11-28 18:42:41.604596
---

# bn.navigateTo

▸ **navigateTo**(`options`): `Promise`<{ `eventChannel?`: `PublicEventChannel` }\>

**`description`** Navigate to a specified page within the Mini Program.

**`example`**

```ts
bn.navigateTo({
  url: "/pages/example/index",
});
```

Parameters

| Name              | Type                            | Description                                        |
| :---------------- | :------------------------------ | :------------------------------------------------- |
| `options`         | `Object`                        | -                                                  |
| `options.url`     | `string`                        | Target URL                                         |
| `options.target?` | `string`                        | Navigation target, either 'deeplink' or 'external' |
| `options.events?` | `Record`<`string`, `Function`\> | -                                                  |

Returns

`Promise`<{ `eventChannel?`: `PublicEventChannel` }\>

---

## PublicEventChannel

Ƭ **PublicEventChannel**: `Object`

Type declaration

| Name    | Type                       |
| :------ | :------------------------- |
| `emit?` | `EventChannel`[``"emit"``] |
| `on?`   | `EventChannel`[``"on"``]   |
| `once?` | `EventChannel`[``"once"``] |
| `off?`  | `EventChannel`[``"off"``]  |

---

## Interface: EventChannel

| Name | Type                             | Description |
| :--- | :------------------------------- | :---------- |
| emit | (`eventName`, ...`args`): `void` |             |
| off  | (`eventName`, `fn`): `void`      |             |
| on   | (`eventName`, `fn`): `void`      |             |
| once | (`eventName`, `fn`): `void`      |             |

### emit

▸ **emit**(`eventName`, ...`args`): `void`

Parameters

| Name        | Type     |
| :---------- | :------- |
| `eventName` | `string` |
| `...args`   | `any`    |

Returns

`void`

---

### off

▸ **off**(`eventName`, `fn`): `void`

Parameters

| Name        | Type            |
| :---------- | :-------------- |
| `eventName` | `string`        |
| `fn`        | `EventCallback` |

Returns

`void`

---

### on

▸ **on**(`eventName`, `fn`): `void`

Parameters

| Name        | Type            |
| :---------- | :-------------- |
| `eventName` | `string`        |
| `fn`        | `EventCallback` |

Returns

`void`

---

### once

▸ **once**(`eventName`, `fn`): `void`

Parameters

| Name        | Type            |
| :---------- | :-------------- |
| `eventName` | `string`        |
| `fn`        | `EventCallback` |

Returns

`void`

## EventCallback

Ƭ **EventCallback**: (...`args`: `Any`) => `void`

Type declaration

▸ (...`args`): `void`

Parameters

| Name      | Type  |
| :-------- | :---- |
| `...args` | `Any` |

Returns

`void`

## Any

Ƭ **Any**: `any`

---

---

# bn.navigateTo

▸ **navigateTo**(`options`): `Promise`<{ `eventChannel?`: `PublicEventChannel` }\>

**`description`** Navigate to a specified page within the Mini Program.

**`example`**

```ts
bn.navigateTo({
  url: "/pages/example/index",
});
```

Parameters

| Name              | Type                            | Description                                        |
| :---------------- | :------------------------------ | :------------------------------------------------- |
| `options`         | `Object`                        | -                                                  |
| `options.url`     | `string`                        | Target URL                                         |
| `options.target?` | `string`                        | Navigation target, either 'deeplink' or 'external' |
| `options.events?` | `Record`<`string`, `Function`\> | -                                                  |

Returns

`Promise`<{ `eventChannel?`: `PublicEventChannel` }\>

---

## PublicEventChannel

Ƭ **PublicEventChannel**: `Object`

Type declaration

| Name    | Type                       |
| :------ | :------------------------- |
| `emit?` | `EventChannel`[``"emit"``] |
| `on?`   | `EventChannel`[``"on"``]   |
| `once?` | `EventChannel`[``"once"``] |
| `off?`  | `EventChannel`[``"off"``]  |

---

## Interface: EventChannel

| Name | Type                             | Description |
| :--- | :------------------------------- | :---------- |
| emit | (`eventName`, ...`args`): `void` |             |
| off  | (`eventName`, `fn`): `void`      |             |
| on   | (`eventName`, `fn`): `void`      |             |
| once | (`eventName`, `fn`): `void`      |             |

### emit

▸ **emit**(`eventName`, ...`args`): `void`

Parameters

| Name        | Type     |
| :---------- | :------- |
| `eventName` | `string` |
| `...args`   | `any`    |

Returns

`void`

---

### off

▸ **off**(`eventName`, `fn`): `void`

Parameters

| Name        | Type            |
| :---------- | :-------------- |
| `eventName` | `string`        |
| `fn`        | `EventCallback` |

Returns

`void`

---

### on

▸ **on**(`eventName`, `fn`): `void`

Parameters

| Name        | Type            |
| :---------- | :-------------- |
| `eventName` | `string`        |
| `fn`        | `EventCallback` |

Returns

`void`

---

### once

▸ **once**(`eventName`, `fn`): `void`

Parameters

| Name        | Type            |
| :---------- | :-------------- |
| `eventName` | `string`        |
| `fn`        | `EventCallback` |

Returns

`void`

## EventCallback

Ƭ **EventCallback**: (...`args`: `Any`) => `void`

Type declaration

▸ (...`args`): `void`

Parameters

| Name      | Type  |
| :-------- | :---- |
| `...args` | `Any` |

Returns

`void`

## Any

Ƭ **Any**: `any`

---