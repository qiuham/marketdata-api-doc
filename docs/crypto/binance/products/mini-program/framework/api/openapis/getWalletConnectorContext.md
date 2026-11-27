---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/getWalletConnectorContext
api_type: Guide
updated_at: 2026-11-27 18:43:55.523800
---

# bn.getWalletConnectorContext

▸ **getWalletConnectorContext**(): `WalletConnectorContext`

**`description`** The api to get WalletConnectorContext

**`example`**

```ts
const walletConnectorContext = bn.getWalletConnectorContext();
```

Returns

`WalletConnectorContext`

## Class: WalletConnectorContext

| Name                        | Type                                                                                                             | Description |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------- | :---------- |
| \_rpcHooks                  | `RPCHooks`                                                                                                       |             |
| callbacks                   | `Map`<`number`, (`error`: `null` \| `Error` \| `ProviderRpcError`, `response`: `Maybe`<`string`[]\>) => `void`\> |             |
| requestId                   | `number`                                                                                                         |             |
| wallet                      | `null` \| `WalletType` = `null`                                                                                  |             |
| isProcessingRequestAccounts | `boolean` = `false`                                                                                              |             |
| web3Provider                | `Web3Provider`                                                                                                   |             |
| walletConnectProvider       | `WalletConnectProvider`                                                                                          |             |
| experimental                | `Experimental`                                                                                                   |             |
| request                     | (`payload`): `Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>                                         |             |
| disconnect                  | (): `void`                                                                                                       |             |
| handleInitialRequest        | (`payload`): `Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>                                         |             |
| setIncomingMessages         | (`socketMessage`): `void`                                                                                        |             |
| registerEvent               | (): `Promise`<`void`\>                                                                                           |             |
| resetConnection             | (): `void`                                                                                                       |             |
| updateWallet                | (`wallet`, `walletId?`): `void`                                                                                  |             |

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

### disconnect

▸ **disconnect**(): `void`

Returns

`void`

---

### handleInitialRequest

▸ `Private` **handleInitialRequest**<`T`\>(`payload`):
`Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>

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

### setIncomingMessages

▸ **setIncomingMessages**(`socketMessage`): `void`

Parameters

| Name            | Type                                 |
| :-------------- | :----------------------------------- |
| `socketMessage` | `WalletConnectorEventMessagePayload` |

Returns

`void`

---

### registerEvent

▸ `Private` **registerEvent**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### resetConnection

▸ `Private` **resetConnection**(): `void`

Returns

`void`

---

### updateWallet

▸ `Private` **updateWallet**(`wallet`, `walletId?`): `void`

Parameters

| Name        | Type                   |
| :---------- | :--------------------- |
| `wallet`    | `null` \| `WalletType` |
| `walletId?` | `string`               |

Returns

`void`

## Interface: EthJsonRpc

| Name                            | Type                                                                                                                                                                                                                     | Description |
| :------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| eth_requestAccounts             | `JsonRpc`<`"eth_requestAccounts"`, [`number`], `string`[]\>                                                                                                                                                              |             |
| eth_signTypedData               | `JsonRpc`<`"eth_signTypedData"`, [`string`, `string`], `string`\>                                                                                                                                                        |             |
| eth_signTypedData_v1            | `JsonRpc`<`"eth_signTypedData_v1"`, [`string`, `string`], `string`\>                                                                                                                                                     |             |
| eth_signTypedData_v2            | `JsonRpc`<`"eth_signTypedData_v2"`, [`string`, `string`], `string`\>                                                                                                                                                     |             |
| eth_signTypedData_v3            | `JsonRpc`<`"eth_signTypedData_v3"`, [`string`, `string`], `string`\>                                                                                                                                                     |             |
| eth_signTypedData_v4            | `JsonRpc`<`"eth_signTypedData_v4"`, [`string`, `string`], `string`\>                                                                                                                                                     |             |
| wallet_getPermissions           | `JsonRpc`<`"wallet_getPermissions"`, `undefined`, `boolean`\>                                                                                                                                                            |             |
| wallet_requestPermissions       | `JsonRpc`<`"wallet_requestPermissions"`, `undefined`, `boolean`\>                                                                                                                                                        |             |
| wallet_registerOnboarding       | `JsonRpc`<`"wallet_registerOnboarding"`, `undefined`, `boolean`\>                                                                                                                                                        |             |
| wallet_scanQRCode               | `JsonRpc`<`"wallet_scanQRCode"`, `undefined`, `boolean`\>                                                                                                                                                                |             |
| unknown                         | `JsonRpc`<`"unknown"`, `unknown`, `UnknownResponse`\>                                                                                                                                                                    |             |
| eth_accounts                    | `JsonRpc`<`"eth_accounts"`, `undefined`, `string`[]\>                                                                                                                                                                    |             |
| eth_coinbase                    | `JsonRpc`<`"eth_coinbase"`, `undefined`, `string`\>                                                                                                                                                                      |             |
| net_version                     | `JsonRpc`<`"net_version"`, `undefined`, `string`\>                                                                                                                                                                       |             |
| eth_chainId                     | `JsonRpc`<`"eth_chainId"`, `undefined`, `string`\>                                                                                                                                                                       |             |
| eth_sign                        | `JsonRpc`<`"eth_sign"`, [`string`, `string`], `string`\>                                                                                                                                                                 |             |
| personal_sign                   | `JsonRpc`<`"personal_sign"`, [`string`], `string`\>                                                                                                                                                                      |             |
| personal_ecRecover              | `JsonRpc`<`"personal_ecRecover"`, [`string`, `string`], `string`\>                                                                                                                                                       |             |
| eth_sendTransaction             | `JsonRpc`<`"eth_sendTransaction"`, [`EthTransaction`], `string`\>                                                                                                                                                        |             |
| eth_sendRawTransaction          | `JsonRpc`<`"eth_sendRawTransaction"`, [`string`], `string`\>                                                                                                                                                             |             |
| eth_signTransaction             | `JsonRpc`<`"eth_signTransaction"`, [`EthTransaction`], `string`\>                                                                                                                                                        |             |
| eth_privateRequestAccounts      | `JsonRpc`<`"eth_privateRequestAccounts"`, `undefined`, `string`[]\>                                                                                                                                                      |             |
| eth_getTransactionCount         | `JsonRpc`<`"eth_getTransactionCount"`, [`string`, `BlockTag`], `string`\>                                                                                                                                                |             |
| eth_gasPrice                    | `JsonRpc`<`"eth_gasPrice"`, `undefined`, `string`\>                                                                                                                                                                      |             |
| eth_estimateGas                 | `JsonRpc`<`"eth_estimateGas"`, [`EthTransaction`], `string`\>                                                                                                                                                            |             |
| wallet_watchAsset               | `JsonRpc`<`"wallet_watchAsset"`, `WatchAssetParameter`, `boolean`\>                                                                                                                                                      |             |
| wallet_addEthereumChain         | `JsonRpc`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }], `null`\> |             |
| wallet_switchEthereumChain      | `JsonRpc`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }], `null`\>                                                                                   |             |
| eth_newFilter                   | `JsonRpc`<`"eth_newFilter"`, `never`, `never`\>                                                                                                                                                                          |             |
| eth_newBlockFilter              | `JsonRpc`<`"eth_newBlockFilter"`, `never`, `never`\>                                                                                                                                                                     |             |
| eth_newPendingTransactionFilter | `JsonRpc`<`"eth_newPendingTransactionFilter"`, `never`, `never`\>                                                                                                                                                        |             |
| eth_uninstallFilter             | `JsonRpc`<`"eth_uninstallFilter"`, `never`, `never`\>                                                                                                                                                                    |             |
| eth_subscribe                   | `JsonRpc`<`"eth_subscribe"`, `never`, `never`\>                                                                                                                                                                          |             |

## Interface: WalletConnectorEventMessagePayload

| Name    | Type     | Description |
| :------ | :------- | :---------- |
| topic   | `string` |             |
| payload | `string` |             |

## Enumeration: WalletType

| Name | Type | Description |
| :--- | :--- | :---------- |

Enumeration members

### internalWallet

• **internalWallet** = `"internalWallet"`

---

### externalWallet

• **externalWallet** = `"externalWallet"`

---

# bn.getWalletConnectorContext

▸ **getWalletConnectorContext**(): `WalletConnectorContext`

**`description`** The api to get WalletConnectorContext

**`example`**

```ts
const walletConnectorContext = bn.getWalletConnectorContext();
```

Returns

`WalletConnectorContext`

## Class: WalletConnectorContext

| Name                        | Type                                                                                                             | Description |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------- | :---------- |
| \_rpcHooks                  | `RPCHooks`                                                                                                       |             |
| callbacks                   | `Map`<`number`, (`error`: `null` \| `Error` \| `ProviderRpcError`, `response`: `Maybe`<`string`[]\>) => `void`\> |             |
| requestId                   | `number`                                                                                                         |             |
| wallet                      | `null` \| `WalletType` = `null`                                                                                  |             |
| isProcessingRequestAccounts | `boolean` = `false`                                                                                              |             |
| web3Provider                | `Web3Provider`                                                                                                   |             |
| walletConnectProvider       | `WalletConnectProvider`                                                                                          |             |
| experimental                | `Experimental`                                                                                                   |             |
| request                     | (`payload`): `Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>                                         |             |
| disconnect                  | (): `void`                                                                                                       |             |
| handleInitialRequest        | (`payload`): `Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>                                         |             |
| setIncomingMessages         | (`socketMessage`): `void`                                                                                        |             |
| registerEvent               | (): `Promise`<`void`\>                                                                                           |             |
| resetConnection             | (): `void`                                                                                                       |             |
| updateWallet                | (`wallet`, `walletId?`): `void`                                                                                  |             |

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

### disconnect

▸ **disconnect**(): `void`

Returns

`void`

---

### handleInitialRequest

▸ `Private` **handleInitialRequest**<`T`\>(`payload`):
`Promise`<`EthJsonRpc`[`T`][``"response"``][``"result"``]\>

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

### setIncomingMessages

▸ **setIncomingMessages**(`socketMessage`): `void`

Parameters

| Name            | Type                                 |
| :-------------- | :----------------------------------- |
| `socketMessage` | `WalletConnectorEventMessagePayload` |

Returns

`void`

---

### registerEvent

▸ `Private` **registerEvent**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### resetConnection

▸ `Private` **resetConnection**(): `void`

Returns

`void`

---

### updateWallet

▸ `Private` **updateWallet**(`wallet`, `walletId?`): `void`

Parameters

| Name        | Type                   |
| :---------- | :--------------------- |
| `wallet`    | `null` \| `WalletType` |
| `walletId?` | `string`               |

Returns

`void`

## Interface: EthJsonRpc

| Name                            | Type                                                                                                                                                                                                                     | Description |
| :------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| eth_requestAccounts             | `JsonRpc`<`"eth_requestAccounts"`, [`number`], `string`[]\>                                                                                                                                                              |             |
| eth_signTypedData               | `JsonRpc`<`"eth_signTypedData"`, [`string`, `string`], `string`\>                                                                                                                                                        |             |
| eth_signTypedData_v1            | `JsonRpc`<`"eth_signTypedData_v1"`, [`string`, `string`], `string`\>                                                                                                                                                     |             |
| eth_signTypedData_v2            | `JsonRpc`<`"eth_signTypedData_v2"`, [`string`, `string`], `string`\>                                                                                                                                                     |             |
| eth_signTypedData_v3            | `JsonRpc`<`"eth_signTypedData_v3"`, [`string`, `string`], `string`\>                                                                                                                                                     |             |
| eth_signTypedData_v4            | `JsonRpc`<`"eth_signTypedData_v4"`, [`string`, `string`], `string`\>                                                                                                                                                     |             |
| wallet_getPermissions           | `JsonRpc`<`"wallet_getPermissions"`, `undefined`, `boolean`\>                                                                                                                                                            |             |
| wallet_requestPermissions       | `JsonRpc`<`"wallet_requestPermissions"`, `undefined`, `boolean`\>                                                                                                                                                        |             |
| wallet_registerOnboarding       | `JsonRpc`<`"wallet_registerOnboarding"`, `undefined`, `boolean`\>                                                                                                                                                        |             |
| wallet_scanQRCode               | `JsonRpc`<`"wallet_scanQRCode"`, `undefined`, `boolean`\>                                                                                                                                                                |             |
| unknown                         | `JsonRpc`<`"unknown"`, `unknown`, `UnknownResponse`\>                                                                                                                                                                    |             |
| eth_accounts                    | `JsonRpc`<`"eth_accounts"`, `undefined`, `string`[]\>                                                                                                                                                                    |             |
| eth_coinbase                    | `JsonRpc`<`"eth_coinbase"`, `undefined`, `string`\>                                                                                                                                                                      |             |
| net_version                     | `JsonRpc`<`"net_version"`, `undefined`, `string`\>                                                                                                                                                                       |             |
| eth_chainId                     | `JsonRpc`<`"eth_chainId"`, `undefined`, `string`\>                                                                                                                                                                       |             |
| eth_sign                        | `JsonRpc`<`"eth_sign"`, [`string`, `string`], `string`\>                                                                                                                                                                 |             |
| personal_sign                   | `JsonRpc`<`"personal_sign"`, [`string`], `string`\>                                                                                                                                                                      |             |
| personal_ecRecover              | `JsonRpc`<`"personal_ecRecover"`, [`string`, `string`], `string`\>                                                                                                                                                       |             |
| eth_sendTransaction             | `JsonRpc`<`"eth_sendTransaction"`, [`EthTransaction`], `string`\>                                                                                                                                                        |             |
| eth_sendRawTransaction          | `JsonRpc`<`"eth_sendRawTransaction"`, [`string`], `string`\>                                                                                                                                                             |             |
| eth_signTransaction             | `JsonRpc`<`"eth_signTransaction"`, [`EthTransaction`], `string`\>                                                                                                                                                        |             |
| eth_privateRequestAccounts      | `JsonRpc`<`"eth_privateRequestAccounts"`, `undefined`, `string`[]\>                                                                                                                                                      |             |
| eth_getTransactionCount         | `JsonRpc`<`"eth_getTransactionCount"`, [`string`, `BlockTag`], `string`\>                                                                                                                                                |             |
| eth_gasPrice                    | `JsonRpc`<`"eth_gasPrice"`, `undefined`, `string`\>                                                                                                                                                                      |             |
| eth_estimateGas                 | `JsonRpc`<`"eth_estimateGas"`, [`EthTransaction`], `string`\>                                                                                                                                                            |             |
| wallet_watchAsset               | `JsonRpc`<`"wallet_watchAsset"`, `WatchAssetParameter`, `boolean`\>                                                                                                                                                      |             |
| wallet_addEthereumChain         | `JsonRpc`<`"wallet_addEthereumChain"`, [`Pick`<`AddEthereumChainParameter`, ``"chainName"`` \| ``"nativeCurrency"`` \| ``"rpcUrls"`` \| ``"blockExplorerUrls"`` \| ``"iconUrls"``\> & { `chainId`: `string` }], `null`\> |             |
| wallet_switchEthereumChain      | `JsonRpc`<`"wallet_switchEthereumChain"`, [`Omit`<`SwitchEthereumChainParameter`, ``"chainId"``\> & { `chainId`: `string` }], `null`\>                                                                                   |             |
| eth_newFilter                   | `JsonRpc`<`"eth_newFilter"`, `never`, `never`\>                                                                                                                                                                          |             |
| eth_newBlockFilter              | `JsonRpc`<`"eth_newBlockFilter"`, `never`, `never`\>                                                                                                                                                                     |             |
| eth_newPendingTransactionFilter | `JsonRpc`<`"eth_newPendingTransactionFilter"`, `never`, `never`\>                                                                                                                                                        |             |
| eth_uninstallFilter             | `JsonRpc`<`"eth_uninstallFilter"`, `never`, `never`\>                                                                                                                                                                    |             |
| eth_subscribe                   | `JsonRpc`<`"eth_subscribe"`, `never`, `never`\>                                                                                                                                                                          |             |

## Interface: WalletConnectorEventMessagePayload

| Name    | Type     | Description |
| :------ | :------- | :---------- |
| topic   | `string` |             |
| payload | `string` |             |

## Enumeration: WalletType

| Name | Type | Description |
| :--- | :--- | :---------- |

Enumeration members

### internalWallet

• **internalWallet** = `"internalWallet"`

---

### externalWallet

• **externalWallet** = `"externalWallet"`