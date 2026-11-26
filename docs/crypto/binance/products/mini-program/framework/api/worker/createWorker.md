---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/worker/createWorker
api_type: Guide
updated_at: 2026-11-26 18:44:32.132347
---

# bn.createWorker

▸ **createWorker**(`scriptPath`): `Worker`

**`description`** Create a Worker Thread.

**`example`**

```ts
const worker = bn.createWorker('workers/index.js')
worker.onMessage((msg) => console.log('worker message', msg)
worker.postMessage({ hello: 'world' })
```

Parameters

| Name         | Type     |
| :----------- | :------- |
| `scriptPath` | `string` |

Returns

`Worker`

## Interface: Worker

| Name        | Type                             | Description                                                                           |
| :---------- | :------------------------------- | :------------------------------------------------------------------------------------ |
| postMessage | (`message`): `Promise`<`void`\>  | Main thread/Worker The message sent by the thread.                                    |
| terminate   | (): `Promise`<`void`\>           | End current Worker Threads. Only in the main thread worker Object.                    |
| onMessage   | (`callback`): `Promise`<`void`\> | Monitor main thread/Worker Event of a message sent by a thread to the current thread. |

### postMessage

▸ **postMessage**(`message`): `Promise`<`void`\>

Main thread/Worker The message sent by the thread.

Parameters

| Name      | Type   |
| :-------- | :----- |
| `message` | `Data` |

Returns

`Promise`<`void`\>

---

### terminate

▸ **terminate**(): `Promise`<`void`\>

End current Worker Threads. Only in the main thread worker Object.

Returns

`Promise`<`void`\>

---

### onMessage

▸ **onMessage**(`callback`): `Promise`<`void`\>

Monitor main thread/Worker Event of a message sent by a thread to the current thread.

Parameters

| Name       | Type                |
| :--------- | :------------------ |
| `callback` | `onMessageCallback` |

Returns

`Promise`<`void`\>

## Data

Ƭ **Data**: `Object`

---

## Interface: onMessageCallback

| Name              | Type   | Description |
| :---------------- | :----- | :---------- |
| onMessageCallback | `void` |             |

---

# bn.createWorker

▸ **createWorker**(`scriptPath`): `Worker`

**`description`** Create a Worker Thread.

**`example`**

```ts
const worker = bn.createWorker('workers/index.js')
worker.onMessage((msg) => console.log('worker message', msg)
worker.postMessage({ hello: 'world' })
```

Parameters

| Name         | Type     |
| :----------- | :------- |
| `scriptPath` | `string` |

Returns

`Worker`

## Interface: Worker

| Name        | Type                             | Description                                                                           |
| :---------- | :------------------------------- | :------------------------------------------------------------------------------------ |
| postMessage | (`message`): `Promise`<`void`\>  | Main thread/Worker The message sent by the thread.                                    |
| terminate   | (): `Promise`<`void`\>           | End current Worker Threads. Only in the main thread worker Object.                    |
| onMessage   | (`callback`): `Promise`<`void`\> | Monitor main thread/Worker Event of a message sent by a thread to the current thread. |

### postMessage

▸ **postMessage**(`message`): `Promise`<`void`\>

Main thread/Worker The message sent by the thread.

Parameters

| Name      | Type   |
| :-------- | :----- |
| `message` | `Data` |

Returns

`Promise`<`void`\>

---

### terminate

▸ **terminate**(): `Promise`<`void`\>

End current Worker Threads. Only in the main thread worker Object.

Returns

`Promise`<`void`\>

---

### onMessage

▸ **onMessage**(`callback`): `Promise`<`void`\>

Monitor main thread/Worker Event of a message sent by a thread to the current thread.

Parameters

| Name       | Type                |
| :--------- | :------------------ |
| `callback` | `onMessageCallback` |

Returns

`Promise`<`void`\>

## Data

Ƭ **Data**: `Object`

---

## Interface: onMessageCallback

| Name              | Type   | Description |
| :---------------- | :----- | :---------- |
| onMessageCallback | `void` |             |