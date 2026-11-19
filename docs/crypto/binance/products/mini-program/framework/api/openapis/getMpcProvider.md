---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/getMpcProvider
api_type: Guide
updated_at: 2026-11-19 18:47:15.838128
---

# bn.getMpcProvider

▸ **getMpcProvider**(): `Web3Provider`

**`description`** The api to get web3 provider

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
//eg1: get web3 provider and then request with method
bn.getMpcProvider()
  .request({
    method: "eth_requestAccounts",
  })
  .then((accounts) => {
    console.log("accounts", accounts);
  });
```

Returns

`Web3Provider`

## Class: Web3Provider

| Name                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                   |
| :--------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| idMapping                                                                                                                                | `default`                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| rpc                                                                                                                                      | `default`                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| callbacks                                                                                                                                | `Map`<`number`, `JsonRpcCallback`<`JsonRpcCallbackResponse`\>\>                                                                                                                                                                                                                                                                                                                     |                                                                                                                               |
| wrapResults                                                                                                                              | `Map`<`number`, `boolean`\>                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                               |
| isDebug                                                                                                                                  | `undefined` \| `boolean`                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                               |
| address                                                                                                                                  | `string`[] = `[]`                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                               |
| ready                                                                                                                                    | `boolean` = `false`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| chainId?                                                                                                                                 | `string`                                                                                                                                                                                                                                                                                                                                                                            | The chain ID of the currently connected Ethereum chain.; See [chainId.network](https://chainid.network) for more information. |
| \_rpcHooks                                                                                                                               | `RPCHooks`                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                               |
| isProcessingRequestAccounts                                                                                                              | `boolean` = `false`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| ProviderRpcError                                                                                                                         | typeof `ProviderRpcError`                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| setChainId                                                                                                                               | (`value?`): `void`                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                               |
| setAddress                                                                                                                               | (`value?`): `void`                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                               |
| setRpc                                                                                                                                   | (`rpcUrl`, `rpcHooks?`): `void`                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                               |
| request                                                                                                                                  | (`payload`): `Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>                                                                                                                                                                                                                                                                                                            |                                                                                                                               |
| isConnected                                                                                                                              | (): `boolean`                                                                                                                                                                                                                                                                                                                                                                       | **`deprecated`** Listen to "connect" event instead.                                                                           |
| enable                                                                                                                                   | (): `Promise`<`Maybe`<`string`[]\>\>                                                                                                                                                                                                                                                                                                                                                | **`deprecated`** Use request({ method: "eth_requestAccounts" }) instead.                                                      |
| send                                                                                                                                     | (`payload`): `EthJsonRpc`[`T`][``"response"``]                                                                                                                                                                                                                                                                                                                                      | **`deprecated`** Use request() method instead.                                                                                |
| sendAsync                                                                                                                                | (`payload`, `callback`): `void`                                                                                                                                                                                                                                                                                                                                                     | **`deprecated`** Use request() method instead.                                                                                |
| \_request                                                                                                                                | (`payload`, `wrapResult?`): `Promise`<`undefined` \| `null` \| `string` \| `boolean` \| `object` \| `JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \| `JsonRpcSuccess`<`string`\> \| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \| `JsonRpcSuccess`<`never`\> \| ( (`undefined` \| `string` \| `object`)[] \| ( (`undefined` \| `string`)[]\> |                                                                                                                               |
| eth_accounts                                                                                                                             | (): `string`[]                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                               |
| eth_coinbase                                                                                                                             | (): `undefined` \| `string`                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                               |
| net_version                                                                                                                              | (): `null` \| `string`                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                               |
| eth_chainId                                                                                                                              | (): `null` \| `string`                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                               |
| eth_sign                                                                                                                                 | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| personal_sign                                                                                                                            | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| eth_signTypedData                                                                                                                        | (`payload`, `version`): `void`                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                               |
| getAccounts                                                                                                                              | (): `Promise`<`string`[]\>                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                               |
| requestAccounts                                                                                                                          | (): `Promise`<`string`[]\>                                                                                                                                                                                                                                                                                                                                                          | Metamask 行為描述                                                                                                             |
| 比照流程：https://github.com/MetaMask/metamask-extension/blob/develop/app/scripts/controllers/permissions/permissionsMethodMiddleware.js |
| eth_sendTransaction                                                                                                                      | (`payload`): `Promise`<`Maybe`<`string`\>\>                                                                                                                                                                                                                                                                                                                                         |                                                                                                                               |
| populateTransaction                                                                                                                      | (`payload`): `Promise`<`EthTransaction`\>                                                                                                                                                                                                                                                                                                                                           | populate the transaction params                                                                                               |
| eth_sendRawTransaction                                                                                                                   | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| wallet_watchAsset                                                                                                                        | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| wallet_addEthereumChain                                                                                                                  | (`payload`): `Promise`<`Maybe`<`null`\>\>                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| wallet_switchEthereumChain                                                                                                               | (`payload`): `Promise`<`Maybe`<`null`\>\>                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| postMessage                                                                                                                              | (`action`, `id`, `object`): `void`                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                               |
| \_isJsonRpc                                                                                                                              | (`result`): result is JsonRpcSuccess<UnknownResponse\>                                                                                                                                                                                                                                                                                                                              |                                                                                                                               |
| sendResponse                                                                                                                             | (`id`, `result`): `void`                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                               |
| sendError                                                                                                                                | (`id`, `error`): `void`                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                               |

### setChainId

▸ **setChainId**(`value?`): `void`

Parameters

| Name     | Type                 |
| :------- | :------------------- |
| `value?` | `string` \| `number` |

Returns

`void`

---

### setAddress

▸ **setAddress**(`value?`): `void`

Parameters

| Name    | Type       | Default value |
| :------ | :--------- | :------------ |
| `value` | `string`[] | `[]`          |

Returns

`void`

---

### setRpc

▸ `Private` **setRpc**(`rpcUrl`, `rpcHooks?`): `void`

Parameters

| Name        | Type                    |
| :---------- | :---------------------- |
| `rpcUrl`    | `undefined` \| `string` |
| `rpcHooks?` | `RPCHooks`              |

Returns

`void`

---

### request

▸ **request**<`T`\>(`payload`): `Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>

Type parameters

| Name | Type                       |
| :--- | :------------------------- |
| `T`  | extends keyof `EthJsonRpc` |

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `payload` | `EthJsonRpc`[`T`][``"request"``] |

Returns

`Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>

---

### isConnected

▸ **isConnected**(): `boolean`

**`deprecated`** Listen to "connect" event instead.

Returns

`boolean`

---

### enable

▸ **enable**(): `Promise`<`Maybe`<`string`[]\>\>

**`deprecated`** Use request({ method: "eth_requestAccounts" }) instead.

Returns

`Promise`<`Maybe`<`string`[]\>\>

---

### send

▸ **send**<`T`\>(`payload`): `EthJsonRpc`[`T`][``"response"``]

**`deprecated`** Use request() method instead.

Type parameters

| Name | Type                       |
| :--- | :------------------------- |
| `T`  | extends keyof `EthJsonRpc` |

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `payload` | `EthJsonRpc`[`T`][``"request"``] |

Returns

`EthJsonRpc`[`T`][``"response"``]

---

### sendAsync

▸ **sendAsync**<`T`\>(`payload`, `callback`): `void`

**`deprecated`** Use request() method instead.

Type parameters

| Name | Type                       |
| :--- | :------------------------- |
| `T`  | extends keyof `EthJsonRpc` |

Parameters

| Name       | Type                                                                                         |
| :--------- | :------------------------------------------------------------------------------------------- |
| `payload`  | `EthJsonRpc`[`T`][``"request"``] \| `EthJsonRpc`[`T`][``"request"``][]                       |
| `callback` | `JsonRpcCallback`<`EthJsonRpc`[`T`][``"response"``] \| `EthJsonRpc`[`T`][``"response"``][]\> |

Returns

`void`

---

### \_request

▸ `Private` **\_request**(`payload`, `wrapResult?`): `Promise`<`undefined` \| `null` \| `string` \|
`boolean` \| `object` \| `JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \|
`JsonRpcSuccess`<`string`\> \| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \|
`JsonRpcSuccess`<`never`\> \| (`undefined` \| `string` \| `object`)[] \| (`undefined` \|
`string`)[]\>

Parameters

| Name         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Default value |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ |
| `payload`    | `JsonRpcRequest`<`"unknown"`, `unknown`\> \| `JsonRpcRequest`<`"eth_accounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_coinbase"`, `undefined`\> \| `JsonRpcRequest`<`"net_version"`, `undefined`\> \| `JsonRpcRequest`<`"eth_chainId"`, `undefined`\> \| `JsonRpcRequest`<`"eth_sign"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"personal_sign"`, [`string`]\> \| `JsonRpcRequest`<`"personal_ecRecover"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_sendRawTransaction"`, [`string`]\> \| `JsonRpcRequest`<`"eth_signTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_requestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_privateRequestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_getTransactionCount"`, [`string`, `BlockTag`]\> \| `JsonRpcRequest`<`"eth_gasPrice"`, `undefined`\> \| `JsonRpcRequest`<`"eth_estimateGas"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"wallet_watchAsset"`, `WatchAssetParameter`\> \| `JsonRpcRequest`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"eth_newFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newBlockFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newPendingTransactionFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_uninstallFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_subscribe"`, `never`\> | `undefined`   |
| `wrapResult` | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `true`        |

Returns

`Promise`<`undefined` \| `null` \| `string` \| `boolean` \| `object` \|
`JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \| `JsonRpcSuccess`<`string`\>
\| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \| `JsonRpcSuccess`<`never`\> \|
(`undefined` \| `string` \| `object`)[] \| (`undefined` \| `string`)[]\>

---

### eth_accounts

▸ `Private` **eth_accounts**(): `string`[]

Returns

`string`[]

---

### eth_coinbase

▸ `Private` **eth_coinbase**(): `undefined` \| `string`

Returns

`undefined` \| `string`

---

### net_version

▸ `Private` **net_version**(): `null` \| `string`

Returns

`null` \| `string`

---

### eth_chainId

▸ `Private` **eth_chainId**(): `null` \| `string`

Returns

`null` \| `string`

---

### eth_sign

▸ `Private` **eth_sign**(`payload`): `void`

Parameters

| Name      | Type                                                  |
| :-------- | :---------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_sign"`, [`string`, `string`]\> |

Returns

`void`

---

### personal_sign

▸ `Private` **personal_sign**(`payload`): `void`

Parameters

| Name      | Type                                             |
| :-------- | :----------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"personal_sign"`, [`string`]\> |

Returns

`void`

---

### eth_signTypedData

▸ `Private` **eth_signTypedData**(`payload`, `version`): `void`

Parameters

| Name      | Type                                                                                                                   |
| :-------- | :--------------------------------------------------------------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`string`, `string`]\> |
| `version` | `V3` \| `V4`                                                                                                           |

Returns

`void`

---

### getAccounts

▸ `Private` **getAccounts**(): `Promise`<`string`[]\>

Returns

`Promise`<`string`[]\>

---

### requestAccounts

▸ `Private` **requestAccounts**(): `Promise`<`string`[]\>

Metamask 行為描述比照流程：https://github.com/MetaMask/metamask-extension/blob/develop/app/scripts/controllers/permissions/permissionsMethodMiddleware.js

Returns

`Promise`<`string`[]\>

---

### eth_sendTransaction

▸ `Private` **eth_sendTransaction**(`payload`): `Promise`<`Maybe`<`string`\>\>

Parameters

| Name      | Type                                                           |
| :-------- | :------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> |

Returns

`Promise`<`Maybe`<`string`\>\>

---

### populateTransaction

▸ `Private` **populateTransaction**(`payload`): `Promise`<`EthTransaction`\>

populate the transaction params

Parameters

| Name      | Type                                                           |
| :-------- | :------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> |

Returns

`Promise`<`EthTransaction`\>

---

### eth_sendRawTransaction

▸ `Private` **eth_sendRawTransaction**(`payload`): `void`

Parameters

| Name      | Type                                                      |
| :-------- | :-------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_sendRawTransaction"`, [`string`]\> |

Returns

`void`

---

### wallet_watchAsset

▸ `Private` **wallet_watchAsset**(`payload`): `void`

Parameters

| Name      | Type                                                            |
| :-------- | :-------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"wallet_watchAsset"`, `WatchAssetParameter`\> |

Returns

`void`

---

### wallet_addEthereumChain

▸ `Private` **wallet_addEthereumChain**(`payload`): `Promise`<`Maybe`<`null`\>\>

Parameters

| Name      | Type                                                                                                                                                                                                                    |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }]\> |

Returns

`Promise`<`Maybe`<`null`\>\>

---

### wallet_switchEthereumChain

▸ `Private` **wallet_switchEthereumChain**(`payload`): `Promise`<`Maybe`<`null`\>\>

Parameters

| Name      | Type                                                                                                                                  |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| `payload` | `JsonRpcRequest`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }]\> |

Returns

`Promise`<`Maybe`<`null`\>\>

---

### postMessage

▸ `Private` **postMessage**<`T`\>(`action`, `id`, `object`): `void`

Type parameters

| Name | Type                               |
| :--- | :--------------------------------- |
| `T`  | extends keyof `PostMessagePayload` |

Parameters

| Name     | Type                                    |
| :------- | :-------------------------------------- |
| `action` | `T`                                     |
| `id`     | `number`                                |
| `object` | `PostMessagePayload`[`T`][``"object"``] |

Returns

`void`

---

### \_isJsonRpc

▸ `Private` **\_isJsonRpc**(`result`): result is JsonRpcSuccess<UnknownResponse\>

Parameters

| Name     | Type                                                                |
| :------- | :------------------------------------------------------------------ |
| `result` | `JsonRpcSuccess`<`UnknownResponse`\> \| `Maybe`<`UnknownResponse`\> |

Returns

result is JsonRpcSuccess<UnknownResponse\>

---

### sendResponse

▸ `Private` **sendResponse**<`T`\>(`id`, `result`): `void`

Type parameters

| Name | Type                       |
| :--- | :------------------------- |
| `T`  | extends keyof `EthJsonRpc` |

Parameters

| Name     | Type                                                                                 |
| :------- | :----------------------------------------------------------------------------------- |
| `id`     | `number`                                                                             |
| `result` | `EthJsonRpc`[`T`][``"response"``] \| `EthJsonRpc`[`T`][``"response"``][``"result"``] |

Returns

`void`

---

### sendError

▸ `Private` **sendError**(`id`, `error`): `void`

Parameters

| Name    | Type                                      |
| :------ | :---------------------------------------- |
| `id`    | `number`                                  |
| `error` | `string` \| `Error` \| `ProviderRpcError` |

Returns

`void`

## Interface: RPCHooks

| Name                | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------- |
| addEthereumChain    | (`payload`): `Promise`<`void`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| switchEthereumChain | (`payload`): `Promise`<`void`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| postMessage         | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| getAccounts         | (): `Promise`<`string`[]\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |
| sendTransaction     | (`payload`): `Promise`<`Maybe`<`string`\>\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| createAccount       | (): `Promise`<`void`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |             |
| rpcCall             | (`_payload`: `JsonRpcRequest`<`"unknown"`, `unknown`\> \| `JsonRpcRequest`<`"eth_accounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_coinbase"`, `undefined`\> \| `JsonRpcRequest`<`"net_version"`, `undefined`\> \| `JsonRpcRequest`<`"eth_chainId"`, `undefined`\> \| `JsonRpcRequest`<`"eth_sign"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"personal_sign"`, [`string`]\> \| `JsonRpcRequest`<`"personal_ecRecover"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_sendRawTransaction"`, [`string`]\> \| `JsonRpcRequest`<`"eth_signTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_requestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_privateRequestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_getTransactionCount"`, [`string`, `BlockTag`]\> \| `JsonRpcRequest`<`"eth_gasPrice"`, `undefined`\> \| `JsonRpcRequest`<`"eth_estimateGas"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"wallet_watchAsset"`, `WatchAssetParameter`\> \| `JsonRpcRequest`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"eth_newFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newBlockFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newPendingTransactionFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_uninstallFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_subscribe"`, `never`\>) => `Promise`<`JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \| `JsonRpcSuccess`<`string`\> \| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \| `JsonRpcSuccess`<`never`\>\> |             |

### addEthereumChain

▸ **addEthereumChain**(`payload`): `Promise`<`void`\>

Parameters

| Name      | Type                        |
| :-------- | :-------------------------- |
| `payload` | `AddEthereumChainParameter` |

Returns

`Promise`<`void`\>

---

### switchEthereumChain

▸ **switchEthereumChain**(`payload`): `Promise`<`void`\>

Parameters

| Name      | Type                           |
| :-------- | :----------------------------- |
| `payload` | `SwitchEthereumChainParameter` |

Returns

`Promise`<`void`\>

---

### postMessage

▸ **postMessage**(`payload`): `void`

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `payload` | `ValueOf`<`PostMessagePayload`\> |

Returns

`void`

---

### getAccounts

▸ **getAccounts**(): `Promise`<`string`[]\>

Returns

`Promise`<`string`[]\>

---

### sendTransaction

▸ **sendTransaction**(`payload`): `Promise`<`Maybe`<`string`\>\>

Parameters

| Name      | Type               |
| :-------- | :----------------- |
| `payload` | [`EthTransaction`] |

Returns

`Promise`<`Maybe`<`string`\>\>

---

### createAccount

▸ **createAccount**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

## EthJsonRpc

Ƭ **EthJsonRpc**: `Object`

Type declaration

| Name                              | Type                                                                                                                                                                                                                         |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `unknown`                         | `JsonRpc`<`"unknown"`, `undefined` \| `unknown`, `UnknownResponse`\>                                                                                                                                                         |
| `eth_accounts`                    | `JsonRpc`<`"eth_accounts"`, `undefined`, `Address`[]\>                                                                                                                                                                       |
| `eth_coinbase`                    | `JsonRpc`<`"eth_coinbase"`, `undefined`, `Address`\>                                                                                                                                                                         |
| `net_version`                     | `JsonRpc`<`"net_version"`, `undefined`, `ChainId`\>                                                                                                                                                                          |
| `eth_chainId`                     | `JsonRpc`<`"eth_chainId"`, `undefined`, `ChainIdHex`\>                                                                                                                                                                       |
| `eth_sign`                        | `JsonRpc`<`"eth_sign"`, [`Address`, `Message`], `SignedSignature`\>                                                                                                                                                          |
| `personal_sign`                   | `JsonRpc`<`"personal_sign"`, [`Message`], `SignedSignature`\>                                                                                                                                                                |
| `personal_ecRecover`              | `JsonRpc`<`"personal_ecRecover"`, [`Message`, `SignedSignature`], `Address`\>                                                                                                                                                |
| `eth_signTypedData`               | `JsonRpc`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`Address`, `string`], `SignedSignature`\>                                                                                          |
| `eth_sendTransaction`             | `JsonRpc`<`"eth_sendTransaction"`, [`EthTransaction`], `TransactionHash`\>                                                                                                                                                   |
| `eth_sendRawTransaction`          | `JsonRpc`<`"eth_sendRawTransaction"`, [`SignedTransaction`], `TransactionHash`\>                                                                                                                                             |
| `eth_signTransaction`             | `JsonRpc`<`"eth_signTransaction"`, [`EthTransaction`], `SignedTransaction`\>                                                                                                                                                 |
| `eth_requestAccounts`             | `JsonRpc`<`"eth_requestAccounts"`, `undefined`, `Address`[]\>                                                                                                                                                                |
| `eth_privateRequestAccounts`      | `JsonRpc`<`"eth_privateRequestAccounts"`, `undefined`, `Address`[]\>                                                                                                                                                         |
| `eth_getTransactionCount`         | `JsonRpc`<`"eth_getTransactionCount"`, [`Address`, `BlockTag`], `string`\>                                                                                                                                                   |
| `eth_gasPrice`                    | `JsonRpc`<`"eth_gasPrice"`, `undefined`, `string`\>                                                                                                                                                                          |
| `eth_estimateGas`                 | `JsonRpc`<`"eth_estimateGas"`, [`EthTransaction`], `string`\>                                                                                                                                                                |
| `wallet_watchAsset`               | `JsonRpc`<`"wallet_watchAsset"`, `WatchAssetParameter`, `boolean`\>                                                                                                                                                          |
| `wallet_addEthereumChain`         | `JsonRpc`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `ChainIdHex` }], `null`\> |
| `wallet_switchEthereumChain`      | `JsonRpc`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `ChainIdHex` }], `null`\>                                                                                   |
| `eth_newFilter`                   | `JsonRpc`<`"eth_newFilter"`, `never`, `never`\>                                                                                                                                                                              |
| `eth_newBlockFilter`              | `JsonRpc`<`"eth_newBlockFilter"`, `never`, `never`\>                                                                                                                                                                         |
| `eth_newPendingTransactionFilter` | `JsonRpc`<`"eth_newPendingTransactionFilter"`, `never`, `never`\>                                                                                                                                                            |
| `eth_uninstallFilter`             | `JsonRpc`<`"eth_uninstallFilter"`, `never`, `never`\>                                                                                                                                                                        |
| `eth_subscribe`                   | `JsonRpc`<`"eth_subscribe"`, `never`, `never`\>                                                                                                                                                                              |

---

## Interface: JsonRpc<Method, Params, Result\>

| Name     | Type                                  | Description |
| :------- | :------------------------------------ | :---------- |
| request  | `JsonRpcRequest`<`Method`, `Params`\> |             |
| response | `JsonRpcSuccess`<`Result`\>           |             |

## UnknownResponse

Ƭ **UnknownResponse**: `boolean` \| `string` \| `object` \| (`string` \| `object`)[]

---

## Address

Ƭ **Address**: `string`

---

## ChainId

Ƭ **ChainId**: `string`

---

## ChainIdHex

Ƭ **ChainIdHex**: `string`

---

## Message

Ƭ **Message**: `string`

---

## SignedSignature

Ƭ **SignedSignature**: `string`

---

## Interface: EthTransaction

| Name      | Type     | Description |
| :-------- | :------- | :---------- |
| from      | `string` |             |
| to?       | `string` |             |
| gas?      | `string` |             |
| gasPrice? | `string` |             |
| value?    | `string` |             |
| data      | `string` |             |
| nonce?    | `string` |             |

## TransactionHash

Ƭ **TransactionHash**: `string`

---

## SignedTransaction

Ƭ **SignedTransaction**: `string`

---

## BlockTag

Ƭ **BlockTag**: `"pending"` \| `"latest"`

---

## Interface: WatchAssetParameter

| Name    | Type      | Description |
| :------ | :-------- | :---------- |
| type    | `"ERC20"` |             |
| options | `Object`  |             |

## Interface: AddEthereumChainParameter

| Name               | Type       | Description |
| :----------------- | :--------- | :---------- |
| chainId            | `number`   |             |
| chainName          | `string`   |             |
| nativeCurrency     | `Object`   |             |
| rpcUrls            | `string`[] |             |
| blockExplorerUrls? | `string`[] |             |
| iconUrls?          | `string`[] |             |

## Interface: SwitchEthereumChainParameter

| Name    | Type     | Description |
| :------ | :------- | :---------- |
| chainId | `number` |             |

## JsonRpcCallback

Ƭ **JsonRpcCallback**<`T`\>: (`error`: `ProviderRpcError` \| `Error` \| `null`, `response`: `T` \|
`null`) => `void`

Type parameters

| Name | Type                      |
| :--- | :------------------------ |
| `T`  | `JsonRpcCallbackResponse` |

Type declaration

▸ (`error`, `response`): `void`

Parameters

| Name       | Type                                    |
| :--------- | :-------------------------------------- |
| `error`    | `ProviderRpcError` \| `Error` \| `null` |
| `response` | `T` \| `null`                           |

Returns

`void`

---

## Class: ProviderRpcError

| Name     | Type         | Description |
| :------- | :----------- | :---------- |
| code     | `number`     |             |
| toString | (): `string` |             |

### toString

▸ **toString**(): `string`

Returns

`string`

## JsonRpcCallbackResponse

Ƭ **JsonRpcCallbackResponse**: `EthJsonRpcValue`[``"response"``][] \|
`EthJsonRpcValue`[``"response"``] \| `EthJsonRpcValue`[`"response"`][``"result"``][] \|
`EthJsonRpcValue`[`"response"`][``"result"``]

---

## EthJsonRpcValue

Ƭ **EthJsonRpcValue**: `Object`

Type declaration

| Name       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`  | `JsonRpcRequest`<`"unknown"`, `unknown`\> \| `JsonRpcRequest`<`"eth_accounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_coinbase"`, `undefined`\> \| `JsonRpcRequest`<`"net_version"`, `undefined`\> \| `JsonRpcRequest`<`"eth_chainId"`, `undefined`\> \| `JsonRpcRequest`<`"eth_sign"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"personal_sign"`, [`string`]\> \| `JsonRpcRequest`<`"personal_ecRecover"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_sendRawTransaction"`, [`string`]\> \| `JsonRpcRequest`<`"eth_signTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_requestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_privateRequestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_getTransactionCount"`, [`string`, `BlockTag`]\> \| `JsonRpcRequest`<`"eth_gasPrice"`, `undefined`\> \| `JsonRpcRequest`<`"eth_estimateGas"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"wallet_watchAsset"`, `WatchAssetParameter`\> \| `JsonRpcRequest`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"eth_newFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newBlockFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newPendingTransactionFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_uninstallFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_subscribe"`, `never`\> |
| `response` | `JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \| `JsonRpcSuccess`<`string`\> \| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \| `JsonRpcSuccess`<`never`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

---

## Interface: JsonRpcRequest<Method, Params\>

| Name    | Type                                         | Description |
| :------ | :------------------------------------------- | :---------- |
| jsonrpc | `"2.0"`                                      |             |
| method  | `Method`                                     |             |
| id      | `number`                                     |             |
| params  | `Params` extends `undefined` ? [] : `Params` |             |

## Interface: JsonRpcSuccess<T\>

| Name    | Type          | Description |
| :------ | :------------ | :---------- |
| result  | `Maybe`<`T`\> |             |
| jsonrpc | `"2.0"`       |             |
| id      | `number`      |             |

## UnknownResponse

Ƭ **UnknownResponse**: `boolean` \| `string` \| `object` \| (`string` \| `object`)[]

---

## BlockTag

Ƭ **BlockTag**: `"pending"` \| `"latest"`

---

## V3

• **V3**: `Object` = `"V3"`

---

## V4

• **V4**: `Object` = `"V4"`

---

## Class: ProviderRpcError

| Name     | Type         | Description |
| :------- | :----------- | :---------- |
| code     | `number`     |             |
| toString | (): `string` |             |

### toString

▸ **toString**(): `string`

Returns

`string`

---

# bn.getMpcProvider

▸ **getMpcProvider**(): `Web3Provider`

**`description`** The api to get web3 provider

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
//eg1: get web3 provider and then request with method
bn.getMpcProvider()
  .request({
    method: "eth_requestAccounts",
  })
  .then((accounts) => {
    console.log("accounts", accounts);
  });
```

Returns

`Web3Provider`

## Class: Web3Provider

| Name                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                   |
| :--------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| idMapping                                                                                                                                | `default`                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| rpc                                                                                                                                      | `default`                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| callbacks                                                                                                                                | `Map`<`number`, `JsonRpcCallback`<`JsonRpcCallbackResponse`\>\>                                                                                                                                                                                                                                                                                                                     |                                                                                                                               |
| wrapResults                                                                                                                              | `Map`<`number`, `boolean`\>                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                               |
| isDebug                                                                                                                                  | `undefined` \| `boolean`                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                               |
| address                                                                                                                                  | `string`[] = `[]`                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                               |
| ready                                                                                                                                    | `boolean` = `false`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| chainId?                                                                                                                                 | `string`                                                                                                                                                                                                                                                                                                                                                                            | The chain ID of the currently connected Ethereum chain.; See [chainId.network](https://chainid.network) for more information. |
| \_rpcHooks                                                                                                                               | `RPCHooks`                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                               |
| isProcessingRequestAccounts                                                                                                              | `boolean` = `false`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| ProviderRpcError                                                                                                                         | typeof `ProviderRpcError`                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| setChainId                                                                                                                               | (`value?`): `void`                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                               |
| setAddress                                                                                                                               | (`value?`): `void`                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                               |
| setRpc                                                                                                                                   | (`rpcUrl`, `rpcHooks?`): `void`                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                               |
| request                                                                                                                                  | (`payload`): `Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>                                                                                                                                                                                                                                                                                                            |                                                                                                                               |
| isConnected                                                                                                                              | (): `boolean`                                                                                                                                                                                                                                                                                                                                                                       | **`deprecated`** Listen to "connect" event instead.                                                                           |
| enable                                                                                                                                   | (): `Promise`<`Maybe`<`string`[]\>\>                                                                                                                                                                                                                                                                                                                                                | **`deprecated`** Use request({ method: "eth_requestAccounts" }) instead.                                                      |
| send                                                                                                                                     | (`payload`): `EthJsonRpc`[`T`][``"response"``]                                                                                                                                                                                                                                                                                                                                      | **`deprecated`** Use request() method instead.                                                                                |
| sendAsync                                                                                                                                | (`payload`, `callback`): `void`                                                                                                                                                                                                                                                                                                                                                     | **`deprecated`** Use request() method instead.                                                                                |
| \_request                                                                                                                                | (`payload`, `wrapResult?`): `Promise`<`undefined` \| `null` \| `string` \| `boolean` \| `object` \| `JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \| `JsonRpcSuccess`<`string`\> \| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \| `JsonRpcSuccess`<`never`\> \| ( (`undefined` \| `string` \| `object`)[] \| ( (`undefined` \| `string`)[]\> |                                                                                                                               |
| eth_accounts                                                                                                                             | (): `string`[]                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                               |
| eth_coinbase                                                                                                                             | (): `undefined` \| `string`                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                               |
| net_version                                                                                                                              | (): `null` \| `string`                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                               |
| eth_chainId                                                                                                                              | (): `null` \| `string`                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                               |
| eth_sign                                                                                                                                 | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| personal_sign                                                                                                                            | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| eth_signTypedData                                                                                                                        | (`payload`, `version`): `void`                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                               |
| getAccounts                                                                                                                              | (): `Promise`<`string`[]\>                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                               |
| requestAccounts                                                                                                                          | (): `Promise`<`string`[]\>                                                                                                                                                                                                                                                                                                                                                          | Metamask 行為描述                                                                                                             |
| 比照流程：https://github.com/MetaMask/metamask-extension/blob/develop/app/scripts/controllers/permissions/permissionsMethodMiddleware.js |
| eth_sendTransaction                                                                                                                      | (`payload`): `Promise`<`Maybe`<`string`\>\>                                                                                                                                                                                                                                                                                                                                         |                                                                                                                               |
| populateTransaction                                                                                                                      | (`payload`): `Promise`<`EthTransaction`\>                                                                                                                                                                                                                                                                                                                                           | populate the transaction params                                                                                               |
| eth_sendRawTransaction                                                                                                                   | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| wallet_watchAsset                                                                                                                        | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                               |
| wallet_addEthereumChain                                                                                                                  | (`payload`): `Promise`<`Maybe`<`null`\>\>                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| wallet_switchEthereumChain                                                                                                               | (`payload`): `Promise`<`Maybe`<`null`\>\>                                                                                                                                                                                                                                                                                                                                           |                                                                                                                               |
| postMessage                                                                                                                              | (`action`, `id`, `object`): `void`                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                               |
| \_isJsonRpc                                                                                                                              | (`result`): result is JsonRpcSuccess<UnknownResponse\>                                                                                                                                                                                                                                                                                                                              |                                                                                                                               |
| sendResponse                                                                                                                             | (`id`, `result`): `void`                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                               |
| sendError                                                                                                                                | (`id`, `error`): `void`                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                               |

### setChainId

▸ **setChainId**(`value?`): `void`

Parameters

| Name     | Type                 |
| :------- | :------------------- |
| `value?` | `string` \| `number` |

Returns

`void`

---

### setAddress

▸ **setAddress**(`value?`): `void`

Parameters

| Name    | Type       | Default value |
| :------ | :--------- | :------------ |
| `value` | `string`[] | `[]`          |

Returns

`void`

---

### setRpc

▸ `Private` **setRpc**(`rpcUrl`, `rpcHooks?`): `void`

Parameters

| Name        | Type                    |
| :---------- | :---------------------- |
| `rpcUrl`    | `undefined` \| `string` |
| `rpcHooks?` | `RPCHooks`              |

Returns

`void`

---

### request

▸ **request**<`T`\>(`payload`): `Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>

Type parameters

| Name | Type                       |
| :--- | :------------------------- |
| `T`  | extends keyof `EthJsonRpc` |

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `payload` | `EthJsonRpc`[`T`][``"request"``] |

Returns

`Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>

---

### isConnected

▸ **isConnected**(): `boolean`

**`deprecated`** Listen to "connect" event instead.

Returns

`boolean`

---

### enable

▸ **enable**(): `Promise`<`Maybe`<`string`[]\>\>

**`deprecated`** Use request({ method: "eth_requestAccounts" }) instead.

Returns

`Promise`<`Maybe`<`string`[]\>\>

---

### send

▸ **send**<`T`\>(`payload`): `EthJsonRpc`[`T`][``"response"``]

**`deprecated`** Use request() method instead.

Type parameters

| Name | Type                       |
| :--- | :------------------------- |
| `T`  | extends keyof `EthJsonRpc` |

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `payload` | `EthJsonRpc`[`T`][``"request"``] |

Returns

`EthJsonRpc`[`T`][``"response"``]

---

### sendAsync

▸ **sendAsync**<`T`\>(`payload`, `callback`): `void`

**`deprecated`** Use request() method instead.

Type parameters

| Name | Type                       |
| :--- | :------------------------- |
| `T`  | extends keyof `EthJsonRpc` |

Parameters

| Name       | Type                                                                                         |
| :--------- | :------------------------------------------------------------------------------------------- |
| `payload`  | `EthJsonRpc`[`T`][``"request"``] \| `EthJsonRpc`[`T`][``"request"``][]                       |
| `callback` | `JsonRpcCallback`<`EthJsonRpc`[`T`][``"response"``] \| `EthJsonRpc`[`T`][``"response"``][]\> |

Returns

`void`

---

### \_request

▸ `Private` **\_request**(`payload`, `wrapResult?`): `Promise`<`undefined` \| `null` \| `string` \|
`boolean` \| `object` \| `JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \|
`JsonRpcSuccess`<`string`\> \| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \|
`JsonRpcSuccess`<`never`\> \| (`undefined` \| `string` \| `object`)[] \| (`undefined` \|
`string`)[]\>

Parameters

| Name         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Default value |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ |
| `payload`    | `JsonRpcRequest`<`"unknown"`, `unknown`\> \| `JsonRpcRequest`<`"eth_accounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_coinbase"`, `undefined`\> \| `JsonRpcRequest`<`"net_version"`, `undefined`\> \| `JsonRpcRequest`<`"eth_chainId"`, `undefined`\> \| `JsonRpcRequest`<`"eth_sign"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"personal_sign"`, [`string`]\> \| `JsonRpcRequest`<`"personal_ecRecover"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_sendRawTransaction"`, [`string`]\> \| `JsonRpcRequest`<`"eth_signTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_requestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_privateRequestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_getTransactionCount"`, [`string`, `BlockTag`]\> \| `JsonRpcRequest`<`"eth_gasPrice"`, `undefined`\> \| `JsonRpcRequest`<`"eth_estimateGas"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"wallet_watchAsset"`, `WatchAssetParameter`\> \| `JsonRpcRequest`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"eth_newFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newBlockFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newPendingTransactionFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_uninstallFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_subscribe"`, `never`\> | `undefined`   |
| `wrapResult` | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `true`        |

Returns

`Promise`<`undefined` \| `null` \| `string` \| `boolean` \| `object` \|
`JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \| `JsonRpcSuccess`<`string`\>
\| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \| `JsonRpcSuccess`<`never`\> \|
(`undefined` \| `string` \| `object`)[] \| (`undefined` \| `string`)[]\>

---

### eth_accounts

▸ `Private` **eth_accounts**(): `string`[]

Returns

`string`[]

---

### eth_coinbase

▸ `Private` **eth_coinbase**(): `undefined` \| `string`

Returns

`undefined` \| `string`

---

### net_version

▸ `Private` **net_version**(): `null` \| `string`

Returns

`null` \| `string`

---

### eth_chainId

▸ `Private` **eth_chainId**(): `null` \| `string`

Returns

`null` \| `string`

---

### eth_sign

▸ `Private` **eth_sign**(`payload`): `void`

Parameters

| Name      | Type                                                  |
| :-------- | :---------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_sign"`, [`string`, `string`]\> |

Returns

`void`

---

### personal_sign

▸ `Private` **personal_sign**(`payload`): `void`

Parameters

| Name      | Type                                             |
| :-------- | :----------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"personal_sign"`, [`string`]\> |

Returns

`void`

---

### eth_signTypedData

▸ `Private` **eth_signTypedData**(`payload`, `version`): `void`

Parameters

| Name      | Type                                                                                                                   |
| :-------- | :--------------------------------------------------------------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`string`, `string`]\> |
| `version` | `V3` \| `V4`                                                                                                           |

Returns

`void`

---

### getAccounts

▸ `Private` **getAccounts**(): `Promise`<`string`[]\>

Returns

`Promise`<`string`[]\>

---

### requestAccounts

▸ `Private` **requestAccounts**(): `Promise`<`string`[]\>

Metamask 行為描述比照流程：https://github.com/MetaMask/metamask-extension/blob/develop/app/scripts/controllers/permissions/permissionsMethodMiddleware.js

Returns

`Promise`<`string`[]\>

---

### eth_sendTransaction

▸ `Private` **eth_sendTransaction**(`payload`): `Promise`<`Maybe`<`string`\>\>

Parameters

| Name      | Type                                                           |
| :-------- | :------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> |

Returns

`Promise`<`Maybe`<`string`\>\>

---

### populateTransaction

▸ `Private` **populateTransaction**(`payload`): `Promise`<`EthTransaction`\>

populate the transaction params

Parameters

| Name      | Type                                                           |
| :-------- | :------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> |

Returns

`Promise`<`EthTransaction`\>

---

### eth_sendRawTransaction

▸ `Private` **eth_sendRawTransaction**(`payload`): `void`

Parameters

| Name      | Type                                                      |
| :-------- | :-------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"eth_sendRawTransaction"`, [`string`]\> |

Returns

`void`

---

### wallet_watchAsset

▸ `Private` **wallet_watchAsset**(`payload`): `void`

Parameters

| Name      | Type                                                            |
| :-------- | :-------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"wallet_watchAsset"`, `WatchAssetParameter`\> |

Returns

`void`

---

### wallet_addEthereumChain

▸ `Private` **wallet_addEthereumChain**(`payload`): `Promise`<`Maybe`<`null`\>\>

Parameters

| Name      | Type                                                                                                                                                                                                                    |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payload` | `JsonRpcRequest`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }]\> |

Returns

`Promise`<`Maybe`<`null`\>\>

---

### wallet_switchEthereumChain

▸ `Private` **wallet_switchEthereumChain**(`payload`): `Promise`<`Maybe`<`null`\>\>

Parameters

| Name      | Type                                                                                                                                  |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| `payload` | `JsonRpcRequest`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }]\> |

Returns

`Promise`<`Maybe`<`null`\>\>

---

### postMessage

▸ `Private` **postMessage**<`T`\>(`action`, `id`, `object`): `void`

Type parameters

| Name | Type                               |
| :--- | :--------------------------------- |
| `T`  | extends keyof `PostMessagePayload` |

Parameters

| Name     | Type                                    |
| :------- | :-------------------------------------- |
| `action` | `T`                                     |
| `id`     | `number`                                |
| `object` | `PostMessagePayload`[`T`][``"object"``] |

Returns

`void`

---

### \_isJsonRpc

▸ `Private` **\_isJsonRpc**(`result`): result is JsonRpcSuccess<UnknownResponse\>

Parameters

| Name     | Type                                                                |
| :------- | :------------------------------------------------------------------ |
| `result` | `JsonRpcSuccess`<`UnknownResponse`\> \| `Maybe`<`UnknownResponse`\> |

Returns

result is JsonRpcSuccess<UnknownResponse\>

---

### sendResponse

▸ `Private` **sendResponse**<`T`\>(`id`, `result`): `void`

Type parameters

| Name | Type                       |
| :--- | :------------------------- |
| `T`  | extends keyof `EthJsonRpc` |

Parameters

| Name     | Type                                                                                 |
| :------- | :----------------------------------------------------------------------------------- |
| `id`     | `number`                                                                             |
| `result` | `EthJsonRpc`[`T`][``"response"``] \| `EthJsonRpc`[`T`][``"response"``][``"result"``] |

Returns

`void`

---

### sendError

▸ `Private` **sendError**(`id`, `error`): `void`

Parameters

| Name    | Type                                      |
| :------ | :---------------------------------------- |
| `id`    | `number`                                  |
| `error` | `string` \| `Error` \| `ProviderRpcError` |

Returns

`void`

## Interface: RPCHooks

| Name                | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------- |
| addEthereumChain    | (`payload`): `Promise`<`void`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| switchEthereumChain | (`payload`): `Promise`<`void`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| postMessage         | (`payload`): `void`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| getAccounts         | (): `Promise`<`string`[]\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |
| sendTransaction     | (`payload`): `Promise`<`Maybe`<`string`\>\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| createAccount       | (): `Promise`<`void`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |             |
| rpcCall             | (`_payload`: `JsonRpcRequest`<`"unknown"`, `unknown`\> \| `JsonRpcRequest`<`"eth_accounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_coinbase"`, `undefined`\> \| `JsonRpcRequest`<`"net_version"`, `undefined`\> \| `JsonRpcRequest`<`"eth_chainId"`, `undefined`\> \| `JsonRpcRequest`<`"eth_sign"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"personal_sign"`, [`string`]\> \| `JsonRpcRequest`<`"personal_ecRecover"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_sendRawTransaction"`, [`string`]\> \| `JsonRpcRequest`<`"eth_signTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_requestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_privateRequestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_getTransactionCount"`, [`string`, `BlockTag`]\> \| `JsonRpcRequest`<`"eth_gasPrice"`, `undefined`\> \| `JsonRpcRequest`<`"eth_estimateGas"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"wallet_watchAsset"`, `WatchAssetParameter`\> \| `JsonRpcRequest`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"eth_newFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newBlockFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newPendingTransactionFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_uninstallFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_subscribe"`, `never`\>) => `Promise`<`JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \| `JsonRpcSuccess`<`string`\> \| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \| `JsonRpcSuccess`<`never`\>\> |             |

### addEthereumChain

▸ **addEthereumChain**(`payload`): `Promise`<`void`\>

Parameters

| Name      | Type                        |
| :-------- | :-------------------------- |
| `payload` | `AddEthereumChainParameter` |

Returns

`Promise`<`void`\>

---

### switchEthereumChain

▸ **switchEthereumChain**(`payload`): `Promise`<`void`\>

Parameters

| Name      | Type                           |
| :-------- | :----------------------------- |
| `payload` | `SwitchEthereumChainParameter` |

Returns

`Promise`<`void`\>

---

### postMessage

▸ **postMessage**(`payload`): `void`

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `payload` | `ValueOf`<`PostMessagePayload`\> |

Returns

`void`

---

### getAccounts

▸ **getAccounts**(): `Promise`<`string`[]\>

Returns

`Promise`<`string`[]\>

---

### sendTransaction

▸ **sendTransaction**(`payload`): `Promise`<`Maybe`<`string`\>\>

Parameters

| Name      | Type               |
| :-------- | :----------------- |
| `payload` | [`EthTransaction`] |

Returns

`Promise`<`Maybe`<`string`\>\>

---

### createAccount

▸ **createAccount**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

## EthJsonRpc

Ƭ **EthJsonRpc**: `Object`

Type declaration

| Name                              | Type                                                                                                                                                                                                                         |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `unknown`                         | `JsonRpc`<`"unknown"`, `undefined` \| `unknown`, `UnknownResponse`\>                                                                                                                                                         |
| `eth_accounts`                    | `JsonRpc`<`"eth_accounts"`, `undefined`, `Address`[]\>                                                                                                                                                                       |
| `eth_coinbase`                    | `JsonRpc`<`"eth_coinbase"`, `undefined`, `Address`\>                                                                                                                                                                         |
| `net_version`                     | `JsonRpc`<`"net_version"`, `undefined`, `ChainId`\>                                                                                                                                                                          |
| `eth_chainId`                     | `JsonRpc`<`"eth_chainId"`, `undefined`, `ChainIdHex`\>                                                                                                                                                                       |
| `eth_sign`                        | `JsonRpc`<`"eth_sign"`, [`Address`, `Message`], `SignedSignature`\>                                                                                                                                                          |
| `personal_sign`                   | `JsonRpc`<`"personal_sign"`, [`Message`], `SignedSignature`\>                                                                                                                                                                |
| `personal_ecRecover`              | `JsonRpc`<`"personal_ecRecover"`, [`Message`, `SignedSignature`], `Address`\>                                                                                                                                                |
| `eth_signTypedData`               | `JsonRpc`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`Address`, `string`], `SignedSignature`\>                                                                                          |
| `eth_sendTransaction`             | `JsonRpc`<`"eth_sendTransaction"`, [`EthTransaction`], `TransactionHash`\>                                                                                                                                                   |
| `eth_sendRawTransaction`          | `JsonRpc`<`"eth_sendRawTransaction"`, [`SignedTransaction`], `TransactionHash`\>                                                                                                                                             |
| `eth_signTransaction`             | `JsonRpc`<`"eth_signTransaction"`, [`EthTransaction`], `SignedTransaction`\>                                                                                                                                                 |
| `eth_requestAccounts`             | `JsonRpc`<`"eth_requestAccounts"`, `undefined`, `Address`[]\>                                                                                                                                                                |
| `eth_privateRequestAccounts`      | `JsonRpc`<`"eth_privateRequestAccounts"`, `undefined`, `Address`[]\>                                                                                                                                                         |
| `eth_getTransactionCount`         | `JsonRpc`<`"eth_getTransactionCount"`, [`Address`, `BlockTag`], `string`\>                                                                                                                                                   |
| `eth_gasPrice`                    | `JsonRpc`<`"eth_gasPrice"`, `undefined`, `string`\>                                                                                                                                                                          |
| `eth_estimateGas`                 | `JsonRpc`<`"eth_estimateGas"`, [`EthTransaction`], `string`\>                                                                                                                                                                |
| `wallet_watchAsset`               | `JsonRpc`<`"wallet_watchAsset"`, `WatchAssetParameter`, `boolean`\>                                                                                                                                                          |
| `wallet_addEthereumChain`         | `JsonRpc`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `ChainIdHex` }], `null`\> |
| `wallet_switchEthereumChain`      | `JsonRpc`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `ChainIdHex` }], `null`\>                                                                                   |
| `eth_newFilter`                   | `JsonRpc`<`"eth_newFilter"`, `never`, `never`\>                                                                                                                                                                              |
| `eth_newBlockFilter`              | `JsonRpc`<`"eth_newBlockFilter"`, `never`, `never`\>                                                                                                                                                                         |
| `eth_newPendingTransactionFilter` | `JsonRpc`<`"eth_newPendingTransactionFilter"`, `never`, `never`\>                                                                                                                                                            |
| `eth_uninstallFilter`             | `JsonRpc`<`"eth_uninstallFilter"`, `never`, `never`\>                                                                                                                                                                        |
| `eth_subscribe`                   | `JsonRpc`<`"eth_subscribe"`, `never`, `never`\>                                                                                                                                                                              |

---

## Interface: JsonRpc<Method, Params, Result\>

| Name     | Type                                  | Description |
| :------- | :------------------------------------ | :---------- |
| request  | `JsonRpcRequest`<`Method`, `Params`\> |             |
| response | `JsonRpcSuccess`<`Result`\>           |             |

## UnknownResponse

Ƭ **UnknownResponse**: `boolean` \| `string` \| `object` \| (`string` \| `object`)[]

---

## Address

Ƭ **Address**: `string`

---

## ChainId

Ƭ **ChainId**: `string`

---

## ChainIdHex

Ƭ **ChainIdHex**: `string`

---

## Message

Ƭ **Message**: `string`

---

## SignedSignature

Ƭ **SignedSignature**: `string`

---

## Interface: EthTransaction

| Name      | Type     | Description |
| :-------- | :------- | :---------- |
| from      | `string` |             |
| to?       | `string` |             |
| gas?      | `string` |             |
| gasPrice? | `string` |             |
| value?    | `string` |             |
| data      | `string` |             |
| nonce?    | `string` |             |

## TransactionHash

Ƭ **TransactionHash**: `string`

---

## SignedTransaction

Ƭ **SignedTransaction**: `string`

---

## BlockTag

Ƭ **BlockTag**: `"pending"` \| `"latest"`

---

## Interface: WatchAssetParameter

| Name    | Type      | Description |
| :------ | :-------- | :---------- |
| type    | `"ERC20"` |             |
| options | `Object`  |             |

## Interface: AddEthereumChainParameter

| Name               | Type       | Description |
| :----------------- | :--------- | :---------- |
| chainId            | `number`   |             |
| chainName          | `string`   |             |
| nativeCurrency     | `Object`   |             |
| rpcUrls            | `string`[] |             |
| blockExplorerUrls? | `string`[] |             |
| iconUrls?          | `string`[] |             |

## Interface: SwitchEthereumChainParameter

| Name    | Type     | Description |
| :------ | :------- | :---------- |
| chainId | `number` |             |

## JsonRpcCallback

Ƭ **JsonRpcCallback**<`T`\>: (`error`: `ProviderRpcError` \| `Error` \| `null`, `response`: `T` \|
`null`) => `void`

Type parameters

| Name | Type                      |
| :--- | :------------------------ |
| `T`  | `JsonRpcCallbackResponse` |

Type declaration

▸ (`error`, `response`): `void`

Parameters

| Name       | Type                                    |
| :--------- | :-------------------------------------- |
| `error`    | `ProviderRpcError` \| `Error` \| `null` |
| `response` | `T` \| `null`                           |

Returns

`void`

---

## Class: ProviderRpcError

| Name     | Type         | Description |
| :------- | :----------- | :---------- |
| code     | `number`     |             |
| toString | (): `string` |             |

### toString

▸ **toString**(): `string`

Returns

`string`

## JsonRpcCallbackResponse

Ƭ **JsonRpcCallbackResponse**: `EthJsonRpcValue`[``"response"``][] \|
`EthJsonRpcValue`[``"response"``] \| `EthJsonRpcValue`[`"response"`][``"result"``][] \|
`EthJsonRpcValue`[`"response"`][``"result"``]

---

## EthJsonRpcValue

Ƭ **EthJsonRpcValue**: `Object`

Type declaration

| Name       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`  | `JsonRpcRequest`<`"unknown"`, `unknown`\> \| `JsonRpcRequest`<`"eth_accounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_coinbase"`, `undefined`\> \| `JsonRpcRequest`<`"net_version"`, `undefined`\> \| `JsonRpcRequest`<`"eth_chainId"`, `undefined`\> \| `JsonRpcRequest`<`"eth_sign"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"personal_sign"`, [`string`]\> \| `JsonRpcRequest`<`"personal_ecRecover"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_signTypedData"` \| `"eth_signTypedData_v3"` \| `"eth_signTypedData_v4"`, [`string`, `string`]\> \| `JsonRpcRequest`<`"eth_sendTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_sendRawTransaction"`, [`string`]\> \| `JsonRpcRequest`<`"eth_signTransaction"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"eth_requestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_privateRequestAccounts"`, `undefined`\> \| `JsonRpcRequest`<`"eth_getTransactionCount"`, [`string`, `BlockTag`]\> \| `JsonRpcRequest`<`"eth_gasPrice"`, `undefined`\> \| `JsonRpcRequest`<`"eth_estimateGas"`, [`EthTransaction`]\> \| `JsonRpcRequest`<`"wallet_watchAsset"`, `WatchAssetParameter`\> \| `JsonRpcRequest`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }]\> \| `JsonRpcRequest`<`"eth_newFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newBlockFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_newPendingTransactionFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_uninstallFilter"`, `never`\> \| `JsonRpcRequest`<`"eth_subscribe"`, `never`\> |
| `response` | `JsonRpcSuccess`<`UnknownResponse`\> \| `JsonRpcSuccess`<`string`[]\> \| `JsonRpcSuccess`<`string`\> \| `JsonRpcSuccess`<`boolean`\> \| `JsonRpcSuccess`<`null`\> \| `JsonRpcSuccess`<`never`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

---

## Interface: JsonRpcRequest<Method, Params\>

| Name    | Type                                         | Description |
| :------ | :------------------------------------------- | :---------- |
| jsonrpc | `"2.0"`                                      |             |
| method  | `Method`                                     |             |
| id      | `number`                                     |             |
| params  | `Params` extends `undefined` ? [] : `Params` |             |

## Interface: JsonRpcSuccess<T\>

| Name    | Type          | Description |
| :------ | :------------ | :---------- |
| result  | `Maybe`<`T`\> |             |
| jsonrpc | `"2.0"`       |             |
| id      | `number`      |             |

## UnknownResponse

Ƭ **UnknownResponse**: `boolean` \| `string` \| `object` \| (`string` \| `object`)[]

---

## BlockTag

Ƭ **BlockTag**: `"pending"` \| `"latest"`

---

## V3

• **V3**: `Object` = `"V3"`

---

## V4

• **V4**: `Object` = `"V4"`

---

## Class: ProviderRpcError

| Name     | Type         | Description |
| :------- | :----------- | :---------- |
| code     | `number`     |             |
| toString | (): `string` |             |

### toString

▸ **toString**(): `string`

Returns

`string`