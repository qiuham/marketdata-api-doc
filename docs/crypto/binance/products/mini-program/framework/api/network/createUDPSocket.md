---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/createUDPSocket
api_type: Guide
updated_at: 2026-11-19 18:47:38.213630
---

# bn.createUDPSocket

▸ **createUDPSocket**(): `undefined` \| `UDPSocket`

**`description`** Create a UDP Socket Instance

**`remark`** supported jssdk >= 4.11.0

**`example`**

```js
const udpSocket = bn.createUDPSocket();
udpSocket.onMessage((res) => {
  console.log(res.message);
});
udpSocket.send({
  address: "",
  port: 1234,
  message: "hello",
});
```

Returns

`undefined` \| `UDPSocket`

## Interface: UDPSocket

| Name         | Type                 | Description                                                                                                                      |
| :----------- | :------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| bind         | (`port?`): `number`  | Bind a system randomly assigned available port or bind a specified port number                                                   |
| close        | (): `void`           | Stop UDP Socket Instance. After close, UDPSocket instance can not send messages, and UDPSocket.send will trigger an error event. |
| connect      | (`options`): `void`  | Preconnect to the specified IP and Port                                                                                          |
| send         | (`payload`): `void`  | send message to target IP and port                                                                                               |
| write        | (`payload`): `void`  | similar to send                                                                                                                  |
| setTTL       | (`ttl`): `void`      | set socket ttl                                                                                                                   |
| onClose      | (`callback`): `void` | regisiter callback for socket close                                                                                              |
| offClose     | (`callback`): `void` | unregisiter callback for socket close                                                                                            |
| onError      | (`callback`): `void` | regisiter callback for errors                                                                                                    |
| offError     | (`callback`): `void` | unregisiter callback for errors                                                                                                  |
| onListening  | (`callback`): `void` | regisiter callback when listener rigistered                                                                                      |
| offListening | (`callback`): `void` | unregisiter callback when listener rigistered                                                                                    |
| onMessage    | (`callback`): `void` | regisiter callback when receive messages                                                                                         |
| offMessage   | (`callback`): `void` | unregisiter callback when receive messages                                                                                       |

### bind

▸ **bind**(`port?`): `number`

Bind a system randomly assigned available port or bind a specified port number

Parameters

| Name    | Type     | Description                                                                                       |
| :------ | :------- | :------------------------------------------------------------------------------------------------ |
| `port?` | `number` | Specifies the port number to bind, or returns the randomly available port number if not specified |

Returns

`number`

Successfully bound port number

---

### close

▸ **close**(): `void`

Stop UDP Socket Instance. After close, UDPSocket instance can not send messages, and UDPSocket.send
will trigger an error event.

Returns

`void`

---

### connect

▸ **connect**(`options`): `void`

Preconnect to the specified IP and Port

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `ConnectOptions` |

Returns

`void`

---

### send

▸ **send**(`payload`): `void`

send message to target IP and port

Parameters

| Name      | Type          |
| :-------- | :------------ |
| `payload` | `SendPaypoad` |

Returns

`void`

---

### write

▸ **write**(`payload`): `void`

similar to send

Parameters

| Name      | Type          |
| :-------- | :------------ |
| `payload` | `SendPaypoad` |

Returns

`void`

---

### setTTL

▸ **setTTL**(`ttl`): `void`

set socket ttl

Parameters

| Name  | Type     | Description               |
| :---- | :------- | :------------------------ |
| `ttl` | `number` | ttl value, range [0, 255] |

Returns

`void`

---

### onClose

▸ **onClose**(`callback`): `void`

regisiter callback for socket close

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `callback` | () => `void` |

Returns

`void`

---

### offClose

▸ **offClose**(`callback`): `void`

unregisiter callback for socket close

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `callback` | () => `void` |

Returns

`void`

---

### onError

▸ **onError**(`callback`): `void`

regisiter callback for errors

Parameters

| Name       | Type            |
| :--------- | :-------------- |
| `callback` | `ErrorCallback` |

Returns

`void`

---

### offError

▸ **offError**(`callback`): `void`

unregisiter callback for errors

Parameters

| Name       | Type            |
| :--------- | :-------------- |
| `callback` | `ErrorCallback` |

Returns

`void`

---

### onListening

▸ **onListening**(`callback`): `void`

regisiter callback when listener rigistered

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `callback` | () => `void` |

Returns

`void`

---

### offListening

▸ **offListening**(`callback`): `void`

unregisiter callback when listener rigistered

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `callback` | () => `void` |

Returns

`void`

---

### onMessage

▸ **onMessage**(`callback`): `void`

regisiter callback when receive messages

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `MessageCallback` |

Returns

`void`

---

### offMessage

▸ **offMessage**(`callback`): `void`

unregisiter callback when receive messages

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `MessageCallback` |

Returns

`void`

## ConnectOptions

Ƭ **ConnectOptions**: `Object`

Type declaration

| Name      | Type     | Description       |
| :-------- | :------- | :---------------- |
| `address` | `string` | target ip address |
| `port`    | `number` | target port       |

---

## SendPaypoad

Ƭ **SendPaypoad**: `Object`

Type declaration

| Name            | Type                      | Description                                                |
| :-------------- | :------------------------ | :--------------------------------------------------------- |
| `address`       | `string`                  | target ip address                                          |
| `port`          | `number`                  | target port                                                |
| `message`       | `string` \| `ArrayBuffer` | message data                                               |
| `offset?`       | `number`                  | offset for arraybuffer, default 0                          |
| `number?`       | `number`                  | message length for arraybuffer, default message.byteLength |
| `setBroadcast?` | `boolean`                 | broadcast the message, default false                       |

---

## ErrorCallback

Ƭ **ErrorCallback**: (`res`: { `errMsg`: `string` }) => `void`

Type declaration

▸ (`res`): `void`

Parameters

| Name         | Type     |
| :----------- | :------- |
| `res`        | `Object` |
| `res.errMsg` | `string` |

Returns

`void`

---

## MessageCallback

Ƭ **MessageCallback**: (`payload`: `MessageCallbackPayload`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `payload` | `MessageCallbackPayload` |

Returns

`void`

---

## MessageCallbackPayload

Ƭ **MessageCallbackPayload**: `Object`

Type declaration

| Name                 | Type                                                                               | Description                      |
| :------------------- | :--------------------------------------------------------------------------------- | :------------------------------- |
| `message`            | `ArrayBuffer`                                                                      | message received                 |
| `remoteInfo`         | { `address`: `string` ; `family`: `string` ; `port`: `number` ; `size`: `number` } | remote address information       |
| `remoteInfo.address` | `string`                                                                           | remote socket address            |
| `remoteInfo.family`  | `string`                                                                           | the protocol family IPv4 or IPv6 |
| `remoteInfo.port`    | `number`                                                                           | port                             |
| `remoteInfo.size`    | `number`                                                                           | message byte size                |
| `localInfo`          | { `address`: `string` ; `family`: `string` ; `port`: `number` }                    | local address information        |
| `localInfo.address`  | `string`                                                                           | local socket address             |
| `localInfo.family`   | `string`                                                                           | the protocol family IPv4 or IPv6 |
| `localInfo.port`     | `number`                                                                           | port                             |

---

# bn.createUDPSocket

▸ **createUDPSocket**(): `undefined` \| `UDPSocket`

**`description`** Create a UDP Socket Instance

**`remark`** supported jssdk >= 4.11.0

**`example`**

```js
const udpSocket = bn.createUDPSocket();
udpSocket.onMessage((res) => {
  console.log(res.message);
});
udpSocket.send({
  address: "",
  port: 1234,
  message: "hello",
});
```

Returns

`undefined` \| `UDPSocket`

## Interface: UDPSocket

| Name         | Type                 | Description                                                                                                                      |
| :----------- | :------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| bind         | (`port?`): `number`  | Bind a system randomly assigned available port or bind a specified port number                                                   |
| close        | (): `void`           | Stop UDP Socket Instance. After close, UDPSocket instance can not send messages, and UDPSocket.send will trigger an error event. |
| connect      | (`options`): `void`  | Preconnect to the specified IP and Port                                                                                          |
| send         | (`payload`): `void`  | send message to target IP and port                                                                                               |
| write        | (`payload`): `void`  | similar to send                                                                                                                  |
| setTTL       | (`ttl`): `void`      | set socket ttl                                                                                                                   |
| onClose      | (`callback`): `void` | regisiter callback for socket close                                                                                              |
| offClose     | (`callback`): `void` | unregisiter callback for socket close                                                                                            |
| onError      | (`callback`): `void` | regisiter callback for errors                                                                                                    |
| offError     | (`callback`): `void` | unregisiter callback for errors                                                                                                  |
| onListening  | (`callback`): `void` | regisiter callback when listener rigistered                                                                                      |
| offListening | (`callback`): `void` | unregisiter callback when listener rigistered                                                                                    |
| onMessage    | (`callback`): `void` | regisiter callback when receive messages                                                                                         |
| offMessage   | (`callback`): `void` | unregisiter callback when receive messages                                                                                       |

### bind

▸ **bind**(`port?`): `number`

Bind a system randomly assigned available port or bind a specified port number

Parameters

| Name    | Type     | Description                                                                                       |
| :------ | :------- | :------------------------------------------------------------------------------------------------ |
| `port?` | `number` | Specifies the port number to bind, or returns the randomly available port number if not specified |

Returns

`number`

Successfully bound port number

---

### close

▸ **close**(): `void`

Stop UDP Socket Instance. After close, UDPSocket instance can not send messages, and UDPSocket.send
will trigger an error event.

Returns

`void`

---

### connect

▸ **connect**(`options`): `void`

Preconnect to the specified IP and Port

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `ConnectOptions` |

Returns

`void`

---

### send

▸ **send**(`payload`): `void`

send message to target IP and port

Parameters

| Name      | Type          |
| :-------- | :------------ |
| `payload` | `SendPaypoad` |

Returns

`void`

---

### write

▸ **write**(`payload`): `void`

similar to send

Parameters

| Name      | Type          |
| :-------- | :------------ |
| `payload` | `SendPaypoad` |

Returns

`void`

---

### setTTL

▸ **setTTL**(`ttl`): `void`

set socket ttl

Parameters

| Name  | Type     | Description               |
| :---- | :------- | :------------------------ |
| `ttl` | `number` | ttl value, range [0, 255] |

Returns

`void`

---

### onClose

▸ **onClose**(`callback`): `void`

regisiter callback for socket close

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `callback` | () => `void` |

Returns

`void`

---

### offClose

▸ **offClose**(`callback`): `void`

unregisiter callback for socket close

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `callback` | () => `void` |

Returns

`void`

---

### onError

▸ **onError**(`callback`): `void`

regisiter callback for errors

Parameters

| Name       | Type            |
| :--------- | :-------------- |
| `callback` | `ErrorCallback` |

Returns

`void`

---

### offError

▸ **offError**(`callback`): `void`

unregisiter callback for errors

Parameters

| Name       | Type            |
| :--------- | :-------------- |
| `callback` | `ErrorCallback` |

Returns

`void`

---

### onListening

▸ **onListening**(`callback`): `void`

regisiter callback when listener rigistered

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `callback` | () => `void` |

Returns

`void`

---

### offListening

▸ **offListening**(`callback`): `void`

unregisiter callback when listener rigistered

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `callback` | () => `void` |

Returns

`void`

---

### onMessage

▸ **onMessage**(`callback`): `void`

regisiter callback when receive messages

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `MessageCallback` |

Returns

`void`

---

### offMessage

▸ **offMessage**(`callback`): `void`

unregisiter callback when receive messages

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `MessageCallback` |

Returns

`void`

## ConnectOptions

Ƭ **ConnectOptions**: `Object`

Type declaration

| Name      | Type     | Description       |
| :-------- | :------- | :---------------- |
| `address` | `string` | target ip address |
| `port`    | `number` | target port       |

---

## SendPaypoad

Ƭ **SendPaypoad**: `Object`

Type declaration

| Name            | Type                      | Description                                                |
| :-------------- | :------------------------ | :--------------------------------------------------------- |
| `address`       | `string`                  | target ip address                                          |
| `port`          | `number`                  | target port                                                |
| `message`       | `string` \| `ArrayBuffer` | message data                                               |
| `offset?`       | `number`                  | offset for arraybuffer, default 0                          |
| `number?`       | `number`                  | message length for arraybuffer, default message.byteLength |
| `setBroadcast?` | `boolean`                 | broadcast the message, default false                       |

---

## ErrorCallback

Ƭ **ErrorCallback**: (`res`: { `errMsg`: `string` }) => `void`

Type declaration

▸ (`res`): `void`

Parameters

| Name         | Type     |
| :----------- | :------- |
| `res`        | `Object` |
| `res.errMsg` | `string` |

Returns

`void`

---

## MessageCallback

Ƭ **MessageCallback**: (`payload`: `MessageCallbackPayload`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `payload` | `MessageCallbackPayload` |

Returns

`void`

---

## MessageCallbackPayload

Ƭ **MessageCallbackPayload**: `Object`

Type declaration

| Name                 | Type                                                                               | Description                      |
| :------------------- | :--------------------------------------------------------------------------------- | :------------------------------- |
| `message`            | `ArrayBuffer`                                                                      | message received                 |
| `remoteInfo`         | { `address`: `string` ; `family`: `string` ; `port`: `number` ; `size`: `number` } | remote address information       |
| `remoteInfo.address` | `string`                                                                           | remote socket address            |
| `remoteInfo.family`  | `string`                                                                           | the protocol family IPv4 or IPv6 |
| `remoteInfo.port`    | `number`                                                                           | port                             |
| `remoteInfo.size`    | `number`                                                                           | message byte size                |
| `localInfo`          | { `address`: `string` ; `family`: `string` ; `port`: `number` }                    | local address information        |
| `localInfo.address`  | `string`                                                                           | local socket address             |
| `localInfo.family`   | `string`                                                                           | the protocol family IPv4 or IPv6 |
| `localInfo.port`     | `number`                                                                           | port                             |