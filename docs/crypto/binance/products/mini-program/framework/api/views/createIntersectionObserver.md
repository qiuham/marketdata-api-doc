---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/views/createIntersectionObserver
api_type: Guide
updated_at: 2026-11-24 18:44:00.051935
---

# bn.createIntersectionObserver

▸ **createIntersectionObserver**(`component`, `options?`): `IntersectionObserver`

**`description`** Creates and returns a IntersectionObserver Object instance. In a custom component
or a page that contains it, you should use the this.createIntersectionObserver([options]) To
replace.

**`remark`** support from jssdk > 4.0.0

**`example`**

```ts
Page({
 onLoad() {
  const observer = bn.createIntersectionObserver(this, {
     thresholds: [0.1]
  })
this._observer.relativeTo('.container').observe('.start', res => {
   console.log('createIntersectionObserver start: ', res)
})
```

Parameters

| Name        | Type                |
| :---------- | :------------------ |
| `component` | `ComponentInstance` |
| `options?`  | `Options`           |

Returns

`IntersectionObserver`

## ComponentInstance

Ƭ **ComponentInstance**: `Object`

Type declaration

| Name        | Type           | Description  |
| :---------- | :------------- | :----------- |
| `id`        | `string`       | Component id |
| `getPageId` | () => `number` | Renderer id  |

---

## Options

Ƭ **Options**: `Object`

Type declaration

| Name           | Type       | Description                                                                                                                                                                                                                                               |
| :------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `thresholds`   | `number`[] | An array of values containing all thresholds. @default [0]                                                                                                                                                                                                |
| `initialRatio` | `number`   | The initial intersection ratio, which triggers a listener callback if the intersection ratio detected when called is not equal to this value and reaches a threshold. @default 0                                                                          |
| `observeAll`   | `boolean`  | Whether multiple target nodes are observed simultaneously (instead of one), if set to true ，observe of targetSelector Multiple nodes will be selected (Note: Selecting too many nodes at the same time will affect rendering performance) @default false |

---

## Class: IntersectionObserver

| Name               | Type                                                                  | Description                                                                                 |
| :----------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| \_component        | `undefined` \| `ComponentInstance`                                    |                                                                                             |
| \_options          | `Options`                                                             |                                                                                             |
| \_relativeInfo     | `RelativeInfo`[]                                                      |                                                                                             |
| \_observerId       | `null` \| `number` \| `""`                                            |                                                                                             |
| disconnected       | `boolean`                                                             |                                                                                             |
| \_rendererId       | `undefined` \| `number`                                               |                                                                                             |
| callback           | `ObserverCallback`                                                    |                                                                                             |
| relativeTo         | (`selector`, `margins?`): `IntersectionObserver`                      | Use the selector to specify a node as one of the reference ranges                           |
| relativeToViewport | (`margins`): `IntersectionObserver`                                   | Specify the page display area as one of the reference areas                                 |
| observe            | (`targetSelector`, `callback`): `undefined` \| `IntersectionObserver` | Specify the target node and start listening for changes in the intersection state parameter |
| disconnect         | (): `void`                                                            | Stop listening. The callback function will no longer trigger                                |

### relativeTo

▸ **relativeTo**(`selector`, `margins?`): `IntersectionObserver`

Use the selector to specify a node as one of the reference ranges

Parameters

| Name       | Type                                                                                        |
| :--------- | :------------------------------------------------------------------------------------------ |
| `selector` | `null` \| `string`                                                                          |
| `margins?` | `Partial`<{ `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` }\> |

Returns

`IntersectionObserver`

---

### relativeToViewport

▸ **relativeToViewport**(`margins`): `IntersectionObserver`

Specify the page display area as one of the reference areas

Parameters

| Name      | Type                                                                                        |
| :-------- | :------------------------------------------------------------------------------------------ |
| `margins` | `Partial`<{ `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` }\> |

Returns

`IntersectionObserver`

---

### observe

▸ **observe**(`targetSelector`, `callback`): `undefined` \| `IntersectionObserver`

Specify the target node and start listening for changes in the intersection state parameter

Parameters

| Name             | Type               |
| :--------------- | :----------------- |
| `targetSelector` | `string`           |
| `callback`       | `ObserverCallback` |

Returns

`undefined` \| `IntersectionObserver`

---

### disconnect

▸ **disconnect**(): `void`

Stop listening. The callback function will no longer trigger

Returns

`void`

## Class: IntersectionObserver

| Name               | Type                                                                  | Description                                                                                 |
| :----------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| \_component        | `undefined` \| `ComponentInstance`                                    |                                                                                             |
| \_options          | `Options`                                                             |                                                                                             |
| \_relativeInfo     | `RelativeInfo`[]                                                      |                                                                                             |
| \_observerId       | `null` \| `number` \| `""`                                            |                                                                                             |
| disconnected       | `boolean`                                                             |                                                                                             |
| \_rendererId       | `undefined` \| `number`                                               |                                                                                             |
| callback           | `ObserverCallback`                                                    |                                                                                             |
| relativeTo         | (`selector`, `margins?`): `IntersectionObserver`                      | Use the selector to specify a node as one of the reference ranges                           |
| relativeToViewport | (`margins`): `IntersectionObserver`                                   | Specify the page display area as one of the reference areas                                 |
| observe            | (`targetSelector`, `callback`): `undefined` \| `IntersectionObserver` | Specify the target node and start listening for changes in the intersection state parameter |
| disconnect         | (): `void`                                                            | Stop listening. The callback function will no longer trigger                                |

### relativeTo

▸ **relativeTo**(`selector`, `margins?`): `IntersectionObserver`

Use the selector to specify a node as one of the reference ranges

Parameters

| Name       | Type                                                                                        |
| :--------- | :------------------------------------------------------------------------------------------ |
| `selector` | `null` \| `string`                                                                          |
| `margins?` | `Partial`<{ `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` }\> |

Returns

`IntersectionObserver`

---

### relativeToViewport

▸ **relativeToViewport**(`margins`): `IntersectionObserver`

Specify the page display area as one of the reference areas

Parameters

| Name      | Type                                                                                        |
| :-------- | :------------------------------------------------------------------------------------------ |
| `margins` | `Partial`<{ `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` }\> |

Returns

`IntersectionObserver`

---

### observe

▸ **observe**(`targetSelector`, `callback`): `undefined` \| `IntersectionObserver`

Specify the target node and start listening for changes in the intersection state parameter

Parameters

| Name             | Type               |
| :--------------- | :----------------- |
| `targetSelector` | `string`           |
| `callback`       | `ObserverCallback` |

Returns

`undefined` \| `IntersectionObserver`

---

### disconnect

▸ **disconnect**(): `void`

Stop listening. The callback function will no longer trigger

Returns

`void`

## ObserverCallback

Ƭ **ObserverCallback**: (`res`: `Response`) => `void`

Type declaration

▸ (`res`): `void`

Parameters

| Name  | Type       |
| :---- | :--------- |
| `res` | `Response` |

Returns

`void`

---

## Response

Ƭ **Response**: `Object`

Type declaration

| Name                 | Type                                                     | Description                                                                                                                                                                                                                                     |
| :------------------- | :------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `boundingClientRect` | `Omit`<`DOMRectReadOnly`, `"x"` \| `"y"` \| `"toJSON"`\> | Target boundary                                                                                                                                                                                                                                 |
| `dataset`            | `Record`<`string`, `Any`\>                               | Node Custom Data Properties                                                                                                                                                                                                                     |
| `id`                 | `number` \| `string`                                     | Node id                                                                                                                                                                                                                                         |
| `intersectionRatio`  | `number`                                                 | Intersecting proportion. How much of the target element is currently visible within the root's intersection ratio, as a value between 0.0 and 1.0. https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRatio |
| `intersectionRect`   | `Omit`<`DOMRectReadOnly`, `"x"` \| `"y"` \| `"toJSON"`\> | Boundary of intersecting region                                                                                                                                                                                                                 |
| `relativeRect`       | `Rect`                                                   | Boundary of reference area                                                                                                                                                                                                                      |
| `time`               | `number`                                                 | Time Stamp for Intersection Detection                                                                                                                                                                                                           |

---

## Any

Ƭ **Any**: `any`

---

## Rect

Ƭ **Rect**: `Object`

Type declaration

| Name     | Type     | Description    |
| :------- | :------- | :------------- |
| `left`   | `number` | Left boundary  |
| `right`  | `number` | Right boundary |
| `top`    | `number` | Upper boundary |
| `bottom` | `number` | Lower boundary |

---

# bn.createIntersectionObserver

▸ **createIntersectionObserver**(`component`, `options?`): `IntersectionObserver`

**`description`** Creates and returns a IntersectionObserver Object instance. In a custom component
or a page that contains it, you should use the this.createIntersectionObserver([options]) To
replace.

**`remark`** support from jssdk > 4.0.0

**`example`**

```ts
Page({
 onLoad() {
  const observer = bn.createIntersectionObserver(this, {
     thresholds: [0.1]
  })
this._observer.relativeTo('.container').observe('.start', res => {
   console.log('createIntersectionObserver start: ', res)
})
```

Parameters

| Name        | Type                |
| :---------- | :------------------ |
| `component` | `ComponentInstance` |
| `options?`  | `Options`           |

Returns

`IntersectionObserver`

## ComponentInstance

Ƭ **ComponentInstance**: `Object`

Type declaration

| Name        | Type           | Description  |
| :---------- | :------------- | :----------- |
| `id`        | `string`       | Component id |
| `getPageId` | () => `number` | Renderer id  |

---

## Options

Ƭ **Options**: `Object`

Type declaration

| Name           | Type       | Description                                                                                                                                                                                                                                               |
| :------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `thresholds`   | `number`[] | An array of values containing all thresholds. @default [0]                                                                                                                                                                                                |
| `initialRatio` | `number`   | The initial intersection ratio, which triggers a listener callback if the intersection ratio detected when called is not equal to this value and reaches a threshold. @default 0                                                                          |
| `observeAll`   | `boolean`  | Whether multiple target nodes are observed simultaneously (instead of one), if set to true ，observe of targetSelector Multiple nodes will be selected (Note: Selecting too many nodes at the same time will affect rendering performance) @default false |

---

## Class: IntersectionObserver

| Name               | Type                                                                  | Description                                                                                 |
| :----------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| \_component        | `undefined` \| `ComponentInstance`                                    |                                                                                             |
| \_options          | `Options`                                                             |                                                                                             |
| \_relativeInfo     | `RelativeInfo`[]                                                      |                                                                                             |
| \_observerId       | `null` \| `number` \| `""`                                            |                                                                                             |
| disconnected       | `boolean`                                                             |                                                                                             |
| \_rendererId       | `undefined` \| `number`                                               |                                                                                             |
| callback           | `ObserverCallback`                                                    |                                                                                             |
| relativeTo         | (`selector`, `margins?`): `IntersectionObserver`                      | Use the selector to specify a node as one of the reference ranges                           |
| relativeToViewport | (`margins`): `IntersectionObserver`                                   | Specify the page display area as one of the reference areas                                 |
| observe            | (`targetSelector`, `callback`): `undefined` \| `IntersectionObserver` | Specify the target node and start listening for changes in the intersection state parameter |
| disconnect         | (): `void`                                                            | Stop listening. The callback function will no longer trigger                                |

### relativeTo

▸ **relativeTo**(`selector`, `margins?`): `IntersectionObserver`

Use the selector to specify a node as one of the reference ranges

Parameters

| Name       | Type                                                                                        |
| :--------- | :------------------------------------------------------------------------------------------ |
| `selector` | `null` \| `string`                                                                          |
| `margins?` | `Partial`<{ `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` }\> |

Returns

`IntersectionObserver`

---

### relativeToViewport

▸ **relativeToViewport**(`margins`): `IntersectionObserver`

Specify the page display area as one of the reference areas

Parameters

| Name      | Type                                                                                        |
| :-------- | :------------------------------------------------------------------------------------------ |
| `margins` | `Partial`<{ `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` }\> |

Returns

`IntersectionObserver`

---

### observe

▸ **observe**(`targetSelector`, `callback`): `undefined` \| `IntersectionObserver`

Specify the target node and start listening for changes in the intersection state parameter

Parameters

| Name             | Type               |
| :--------------- | :----------------- |
| `targetSelector` | `string`           |
| `callback`       | `ObserverCallback` |

Returns

`undefined` \| `IntersectionObserver`

---

### disconnect

▸ **disconnect**(): `void`

Stop listening. The callback function will no longer trigger

Returns

`void`

## Class: IntersectionObserver

| Name               | Type                                                                  | Description                                                                                 |
| :----------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| \_component        | `undefined` \| `ComponentInstance`                                    |                                                                                             |
| \_options          | `Options`                                                             |                                                                                             |
| \_relativeInfo     | `RelativeInfo`[]                                                      |                                                                                             |
| \_observerId       | `null` \| `number` \| `""`                                            |                                                                                             |
| disconnected       | `boolean`                                                             |                                                                                             |
| \_rendererId       | `undefined` \| `number`                                               |                                                                                             |
| callback           | `ObserverCallback`                                                    |                                                                                             |
| relativeTo         | (`selector`, `margins?`): `IntersectionObserver`                      | Use the selector to specify a node as one of the reference ranges                           |
| relativeToViewport | (`margins`): `IntersectionObserver`                                   | Specify the page display area as one of the reference areas                                 |
| observe            | (`targetSelector`, `callback`): `undefined` \| `IntersectionObserver` | Specify the target node and start listening for changes in the intersection state parameter |
| disconnect         | (): `void`                                                            | Stop listening. The callback function will no longer trigger                                |

### relativeTo

▸ **relativeTo**(`selector`, `margins?`): `IntersectionObserver`

Use the selector to specify a node as one of the reference ranges

Parameters

| Name       | Type                                                                                        |
| :--------- | :------------------------------------------------------------------------------------------ |
| `selector` | `null` \| `string`                                                                          |
| `margins?` | `Partial`<{ `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` }\> |

Returns

`IntersectionObserver`

---

### relativeToViewport

▸ **relativeToViewport**(`margins`): `IntersectionObserver`

Specify the page display area as one of the reference areas

Parameters

| Name      | Type                                                                                        |
| :-------- | :------------------------------------------------------------------------------------------ |
| `margins` | `Partial`<{ `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` }\> |

Returns

`IntersectionObserver`

---

### observe

▸ **observe**(`targetSelector`, `callback`): `undefined` \| `IntersectionObserver`

Specify the target node and start listening for changes in the intersection state parameter

Parameters

| Name             | Type               |
| :--------------- | :----------------- |
| `targetSelector` | `string`           |
| `callback`       | `ObserverCallback` |

Returns

`undefined` \| `IntersectionObserver`

---

### disconnect

▸ **disconnect**(): `void`

Stop listening. The callback function will no longer trigger

Returns

`void`

## ObserverCallback

Ƭ **ObserverCallback**: (`res`: `Response`) => `void`

Type declaration

▸ (`res`): `void`

Parameters

| Name  | Type       |
| :---- | :--------- |
| `res` | `Response` |

Returns

`void`

---

## Response

Ƭ **Response**: `Object`

Type declaration

| Name                 | Type                                                     | Description                                                                                                                                                                                                                                     |
| :------------------- | :------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `boundingClientRect` | `Omit`<`DOMRectReadOnly`, `"x"` \| `"y"` \| `"toJSON"`\> | Target boundary                                                                                                                                                                                                                                 |
| `dataset`            | `Record`<`string`, `Any`\>                               | Node Custom Data Properties                                                                                                                                                                                                                     |
| `id`                 | `number` \| `string`                                     | Node id                                                                                                                                                                                                                                         |
| `intersectionRatio`  | `number`                                                 | Intersecting proportion. How much of the target element is currently visible within the root's intersection ratio, as a value between 0.0 and 1.0. https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRatio |
| `intersectionRect`   | `Omit`<`DOMRectReadOnly`, `"x"` \| `"y"` \| `"toJSON"`\> | Boundary of intersecting region                                                                                                                                                                                                                 |
| `relativeRect`       | `Rect`                                                   | Boundary of reference area                                                                                                                                                                                                                      |
| `time`               | `number`                                                 | Time Stamp for Intersection Detection                                                                                                                                                                                                           |

---

## Any

Ƭ **Any**: `any`

---

## Rect

Ƭ **Rect**: `Object`

Type declaration

| Name     | Type     | Description    |
| :------- | :------- | :------------- |
| `left`   | `number` | Left boundary  |
| `right`  | `number` | Right boundary |
| `top`    | `number` | Upper boundary |
| `bottom` | `number` | Lower boundary |