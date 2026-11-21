---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/connectSocket
api_type: Guide
updated_at: 2026-11-21 18:45:01.687697
---

# bn.connectSocket

▸ **connectSocket**(`options`): `SocketTask`

**`description`** Create a WebSocket Connect.

**`example`**

```ts
 bn.connectSocket({
   url: 'wss://binance.com'
   header:{
     'content-type': 'application/json'
   },
   protocols: ['protocol1']
 })
```

Parameters

| Name      | Type                  |
| :-------- | :-------------------- |
| `options` | `ConnectSocketOption` |

Returns

`SocketTask`

## Interface: ConnectSocketOption

| Name               | Type            | Description                                                     |
| :----------------- | :-------------- | :-------------------------------------------------------------- |
| url                | `string`        | Developer Server wss Interface address                          |
| header?            | `any`           | HTTP Header，Header Can not be set Refer                        |
| perMessageDeflate? | `boolean`       | Enable compression expansion                                    |
| protocols?         | `string`[]      | Subprotocol array                                               |
| tcpNoDelay?        | `boolean`       | establish TCP At the time of the connection. TCP_NODELAY Set up |
| timeout?           | `number`        | Timeout in milliseconds                                         |
| success?           | (`res`): `void` |                                                                 |
| complete?          | (`res`): `void` |                                                                 |
| fail?              | (`res`): `void` |                                                                 |

### success

▸ `Optional` **success**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### complete

▸ `Optional` **complete**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### fail

▸ `Optional` **fail**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

## Interface: GeneralCallbackResult

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| errMsg | `string` |             |

## Interface: SocketTask

| Name          | Type             | Description                                             |
| :------------ | :--------------- | :------------------------------------------------------ |
| send          | (`args`): `void` | adopt WebSocket Connect to send data                    |
| close         | (`args`): `void` | Stop WebSocket Connect                                  |
| onOpen        | (`cb`): `void`   | to monitor WebSocket Connection Open Event              |
| onClose       | (`cb`): `void`   | to monitor WebSocket Connection Closure Event           |
| onError       | (`cb`): `void`   | to monitor WebSocket Error event                        |
| onMessage     | (`cb`): `void`   | to monitor WebSocket Message event received from server |
| socketTaskId? | `string`         |                                                         |
| readyState    | `number`         |                                                         |
| errMsg        | `string`         |                                                         |
| CONNECTING    | `0`              |                                                         |
| OPEN          | `1`              |                                                         |
| CLOSING       | `2`              |                                                         |
| CLOSED        | `3`              |                                                         |
| \_id          | `string`         |                                                         |

### send

▸ **send**(`args`): `void`

adopt WebSocket Connect to send data

Parameters

| Name        | Type            |
| :---------- | :-------------- |
| `args`      | `Object`        |
| `args.data` | `WebSocketData` |

Returns

`void`

---

### close

▸ **close**(`args`): `void`

Stop WebSocket Connect

Parameters

| Name   | Type                                     |
| :----- | :--------------------------------------- |
| `args` | `Omit`<`WebSocketCloseOptions`, `"id"`\> |

Returns

`void`

---

### onOpen

▸ **onOpen**(`cb`): `void`

to monitor WebSocket Connection Open Event

Parameters

| Name | Type     |
| :--- | :------- |
| `cb` | `OnOpen` |

Returns

`void`

---

### onClose

▸ **onClose**(`cb`): `void`

to monitor WebSocket Connection Closure Event

Parameters

| Name | Type      |
| :--- | :-------- |
| `cb` | `OnClose` |

Returns

`void`

---

### onError

▸ **onError**(`cb`): `void`

to monitor WebSocket Error event

Parameters

| Name | Type      |
| :--- | :-------- |
| `cb` | `OnError` |

Returns

`void`

---

### onMessage

▸ **onMessage**(`cb`): `void`

to monitor WebSocket Message event received from server

Parameters

| Name | Type        |
| :--- | :---------- |
| `cb` | `OnMessage` |

Returns

`void`

---

# bn.connectSocket

▸ **connectSocket**(`options`): `SocketTask`

**`description`** Create a WebSocket Connect.

**`example`**

```ts
 bn.connectSocket({
   url: 'wss://binance.com'
   header:{
     'content-type': 'application/json'
   },
   protocols: ['protocol1']
 })
```

Parameters

| Name      | Type                  |
| :-------- | :-------------------- |
| `options` | `ConnectSocketOption` |

Returns

`SocketTask`

## Interface: ConnectSocketOption

| Name               | Type            | Description                                                     |
| :----------------- | :-------------- | :-------------------------------------------------------------- |
| url                | `string`        | Developer Server wss Interface address                          |
| header?            | `any`           | HTTP Header，Header Can not be set Refer                        |
| perMessageDeflate? | `boolean`       | Enable compression expansion                                    |
| protocols?         | `string`[]      | Subprotocol array                                               |
| tcpNoDelay?        | `boolean`       | establish TCP At the time of the connection. TCP_NODELAY Set up |
| timeout?           | `number`        | Timeout in milliseconds                                         |
| success?           | (`res`): `void` |                                                                 |
| complete?          | (`res`): `void` |                                                                 |
| fail?              | (`res`): `void` |                                                                 |

### success

▸ `Optional` **success**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### complete

▸ `Optional` **complete**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### fail

▸ `Optional` **fail**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

## Interface: GeneralCallbackResult

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| errMsg | `string` |             |

## Interface: SocketTask

| Name          | Type             | Description                                             |
| :------------ | :--------------- | :------------------------------------------------------ |
| send          | (`args`): `void` | adopt WebSocket Connect to send data                    |
| close         | (`args`): `void` | Stop WebSocket Connect                                  |
| onOpen        | (`cb`): `void`   | to monitor WebSocket Connection Open Event              |
| onClose       | (`cb`): `void`   | to monitor WebSocket Connection Closure Event           |
| onError       | (`cb`): `void`   | to monitor WebSocket Error event                        |
| onMessage     | (`cb`): `void`   | to monitor WebSocket Message event received from server |
| socketTaskId? | `string`         |                                                         |
| readyState    | `number`         |                                                         |
| errMsg        | `string`         |                                                         |
| CONNECTING    | `0`              |                                                         |
| OPEN          | `1`              |                                                         |
| CLOSING       | `2`              |                                                         |
| CLOSED        | `3`              |                                                         |
| \_id          | `string`         |                                                         |

### send

▸ **send**(`args`): `void`

adopt WebSocket Connect to send data

Parameters

| Name        | Type            |
| :---------- | :-------------- |
| `args`      | `Object`        |
| `args.data` | `WebSocketData` |

Returns

`void`

---

### close

▸ **close**(`args`): `void`

Stop WebSocket Connect

Parameters

| Name   | Type                                     |
| :----- | :--------------------------------------- |
| `args` | `Omit`<`WebSocketCloseOptions`, `"id"`\> |

Returns

`void`

---

### onOpen

▸ **onOpen**(`cb`): `void`

to monitor WebSocket Connection Open Event

Parameters

| Name | Type     |
| :--- | :------- |
| `cb` | `OnOpen` |

Returns

`void`

---

### onClose

▸ **onClose**(`cb`): `void`

to monitor WebSocket Connection Closure Event

Parameters

| Name | Type      |
| :--- | :-------- |
| `cb` | `OnClose` |

Returns

`void`

---

### onError

▸ **onError**(`cb`): `void`

to monitor WebSocket Error event

Parameters

| Name | Type      |
| :--- | :-------- |
| `cb` | `OnError` |

Returns

`void`

---

### onMessage

▸ **onMessage**(`cb`): `void`

to monitor WebSocket Message event received from server

Parameters

| Name | Type        |
| :--- | :---------- |
| `cb` | `OnMessage` |

Returns

`void`