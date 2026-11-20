---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/initUniversalWeb3Provider
api_type: Guide
updated_at: 2026-11-20 18:45:58.182144
---

# bn.initUniversalWeb3Provider

▸ **initUniversalWeb3Provider**(`options?`): `Promise`<{ `result`: `UniversalProvider` }\>

Parameters

| Name       | Type                                                             |
| :--------- | :--------------------------------------------------------------- |
| `options?` | `Pick`<`UniversalProviderOptions`, `"topicId"` \| `"metaData"`\> |

Returns

`Promise`<{ `result`: `UniversalProvider` }\>

## Interface: UniversalProviderOptions

| Name      | Type             | Description |
| :-------- | :--------------- | :---------- |
| rpcHooks  | `RPCHooks`       |             |
| topicId?  | `TopicId`        |             |
| metaData? | `ClientMetadata` |             |

## Class: UniversalProvider

| Name                   | Type                                                                                 | Description |
| :--------------------- | :----------------------------------------------------------------------------------- | :---------- |
| topicId                | `TopicId`                                                                            |             |
| metaData?              | `ClientMetadata`                                                                     |             |
| events                 | `SimpleEventEmitter`                                                                 |             |
| namespaces             | `NamespaceRecord` = `{}`                                                             |             |
| rpcAdaptors            | `RpcAdaptorMap` = `{}`                                                               |             |
| rpcHooks               | `RPCHooks`                                                                           |             |
| isConnecting           | `boolean` = `false`                                                                  |             |
| on                     | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| once                   | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| removeListener         | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| off                    | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| emit                   | <E\>(`event`: `E`, `payload`: `EventArguments`[`E`]) => `boolean`                    |             |
| isConnected            | `boolean`                                                                            |             |
| request                | (`args`, `chain?`): `Promise`<`T`\>                                                  |             |
| sendAsync              | (`args`, `callback`, `chain?`): `void`                                               |             |
| enable                 | (`__namedParameters?`): `Promise`<`string`[]\>                                       |             |
| connect                | (`__namedParameters?`): `Promise`<`void`\>                                           |             |
| disconnect             | (): `Promise`<`void`\>                                                               |             |
| setDefaultChain        | (`chain`): `void`                                                                    |             |
| onAccountsChanged      | (`accountsMap`): `void`                                                              |             |
| initialize             | (): `Promise`<`void`\>                                                               |             |
| createAdaptors         | (): `void`                                                                           |             |
| registerEventListeners | (): `void`                                                                           |             |
| getAdaptor             | (`namespace`): `IAdaptor`                                                            |             |
| setNamespaces          | (`accountsMap`): `void`                                                              |             |
| validateChain          | (`chain?`): [`Namespace`, `string`]                                                  |             |
| requestAccounts        | (`chain?`): `Promise`<`string`[]\>                                                   |             |
| onConnect              | (): `void`                                                                           |             |
| onChainChanged         | (`chain`): `void`                                                                    |             |
| init                   | (`options`): `Promise`<`UniversalProvider`\>                                         |             |

### request

▸ **request**<`T`\>(`args`, `chain?`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `args`   | `RequestArgs`                                                                            |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`T`\>

Implementation of

IUniversalProvider.request

---

### sendAsync

▸ **sendAsync**<`T`\>(`args`, `callback`, `chain?`): `void`

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name       | Type                                                                                     |
| :--------- | :--------------------------------------------------------------------------------------- |
| `args`     | `RequestArgs`                                                                            |
| `callback` | (`error`: `null` \| `Error`, `response`: `undefined` \| `T`) => `void`                   |
| `chain?`   | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

Implementation of

IUniversalProvider.sendAsync

---

### enable

▸ **enable**(`__namedParameters?`): `Promise`<`string`[]\>

Parameters

| Name                | Type         |
| :------------------ | :----------- |
| `__namedParameters` | `EnableArgs` |

Returns

`Promise`<`string`[]\>

Implementation of

IUniversalProvider.enable

---

### connect

▸ **connect**(`__namedParameters?`): `Promise`<`void`\>

Parameters

| Name                | Type          |
| :------------------ | :------------ |
| `__namedParameters` | `ConnectArgs` |

Returns

`Promise`<`void`\>

Implementation of

IUniversalProvider.connect

---

### disconnect

▸ **disconnect**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

Implementation of

IUniversalProvider.disconnect

---

### setDefaultChain

▸ **setDefaultChain**(`chain`): `void`

Parameters

| Name    | Type                                                                                     |
| :------ | :--------------------------------------------------------------------------------------- |
| `chain` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

---

### onAccountsChanged

▸ **onAccountsChanged**(`accountsMap`): `void`

Parameters

| Name          | Type          |
| :------------ | :------------ |
| `accountsMap` | `AccountsMap` |

Returns

`void`

---

### initialize

▸ `Private` **initialize**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### createAdaptors

▸ `Private` **createAdaptors**(): `void`

Returns

`void`

---

### registerEventListeners

▸ `Private` **registerEventListeners**(): `void`

Returns

`void`

---

### getAdaptor

▸ `Private` **getAdaptor**(`namespace`): `IAdaptor`

Parameters

| Name        | Type        |
| :---------- | :---------- |
| `namespace` | `Namespace` |

Returns

`IAdaptor`

---

### setNamespaces

▸ `Private` **setNamespaces**(`accountsMap`): `void`

Parameters

| Name          | Type          |
| :------------ | :------------ |
| `accountsMap` | `AccountsMap` |

Returns

`void`

---

### validateChain

▸ `Private` **validateChain**(`chain?`): [`Namespace`, `string`]

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

[`Namespace`, `string`]

---

### requestAccounts

▸ `Private` **requestAccounts**(`chain?`): `Promise`<`string`[]\>

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`string`[]\>

---

### onConnect

▸ `Private` **onConnect**(): `void`

Returns

`void`

---

### onChainChanged

▸ `Private` **onChainChanged**(`chain`): `void`

Parameters

| Name    | Type                                                                                     |
| :------ | :--------------------------------------------------------------------------------------- |
| `chain` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

---

### init

▸ `Static` **init**(`options`): `Promise`<`UniversalProvider`\>

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `options` | `UniversalProviderOptions` |

Returns

`Promise`<`UniversalProvider`\>

## Interface: RequestArgs

| Name      | Type                                          | Description |
| :-------- | :-------------------------------------------- | :---------- |
| method    | `string`                                      |             |
| params?   | `unknown`[] \| `Record`<`string`, `unknown`\> |             |
| metadata? | `ClientMetadata`                              |             |

## Interface: IUniversalProvider

| Name           | Type                                                                                 | Description |
| :------------- | :----------------------------------------------------------------------------------- | :---------- |
| topicId        | `TopicId`                                                                            |             |
| metaData?      | `ClientMetadata`                                                                     |             |
| events         | `SimpleEventEmitter`                                                                 |             |
| namespaces?    | `NamespaceRecord`                                                                    |             |
| rpcAdaptors    | `RpcAdaptorMap`                                                                      |             |
| on             | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| once           | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| off            | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| removeListener | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| emit           | <E\>(`event`: `E`, `payload`: `EventArguments`[`E`]) => `boolean`                    |             |
| request        | (`args`, `chain?`): `Promise`<`T`\>                                                  |             |
| sendAsync      | (`args`, `callback`, `chain?`): `void`                                               |             |
| enable         | (`args?`): `Promise`<`string`[]\>                                                    |             |
| connect        | (`args?`): `Promise`<`void`\>                                                        |             |
| disconnect     | (): `void`                                                                           |             |

### request

▸ **request**<`T`\>(`args`, `chain?`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `args`   | `RequestArgs`                                                                            |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`T`\>

Overrides

EIP1193Provider.request

---

### sendAsync

▸ **sendAsync**<`T`\>(`args`, `callback`, `chain?`): `void`

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name       | Type                                                                   |
| :--------- | :--------------------------------------------------------------------- |
| `args`     | `RequestArgs`                                                          |
| `callback` | (`error`: `null` \| `Error`, `response`: `undefined` \| `T`) => `void` |
| `chain?`   | `string`                                                               |

Returns

`void`

---

### enable

▸ **enable**(`args?`): `Promise`<`string`[]\>

Parameters

| Name    | Type         |
| :------ | :----------- |
| `args?` | `EnableArgs` |

Returns

`Promise`<`string`[]\>

Overrides

EIP1193Provider.enable

---

### connect

▸ **connect**(`args?`): `Promise`<`void`\>

Parameters

| Name    | Type          |
| :------ | :------------ |
| `args?` | `ConnectArgs` |

Returns

`Promise`<`void`\>

---

### disconnect

▸ **disconnect**(): `void`

Returns

`void`

## Interface: RequestArgs

| Name      | Type                                          | Description |
| :-------- | :-------------------------------------------- | :---------- |
| method    | `string`                                      |             |
| params?   | `unknown`[] \| `Record`<`string`, `unknown`\> |             |
| metadata? | `ClientMetadata`                              |             |

## Interface: EIP1193Provider

| Name           | Type                               | Description |
| :------------- | :--------------------------------- | :---------- |
| request        | (`args`): `Promise`<`unknown`\>    |             |
| enable         | (): `Promise`<`ProviderAccounts`\> |             |
| on             | (`event`, `listener`): `void`      |             |
| once           | (`event`, `listener`): `void`      |             |
| removeListener | (`event`, `listener`): `void`      |             |
| off            | (`event`, `listener`): `void`      |             |
| emit           | (`event`, ...`args`): `boolean`    |             |

### request

▸ **request**(`args`): `Promise`<`unknown`\>

Parameters

| Name   | Type          |
| :----- | :------------ |
| `args` | `RequestArgs` |

Returns

`Promise`<`unknown`\>

---

### enable

▸ **enable**(): `Promise`<`ProviderAccounts`\>

Returns

`Promise`<`ProviderAccounts`\>

---

### on

▸ **on**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

Inherited from

SimpleEventEmitter.on

---

### once

▸ **once**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

Inherited from

SimpleEventEmitter.once

---

### removeListener

▸ **removeListener**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

Inherited from

SimpleEventEmitter.removeListener

---

### off

▸ **off**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

Inherited from

SimpleEventEmitter.off

---

### emit

▸ **emit**(`event`, ...`args`): `boolean`

Parameters

| Name      | Type        |
| :-------- | :---------- |
| `event`   | `string`    |
| `...args` | `unknown`[] |

Returns

`boolean`

Inherited from

SimpleEventEmitter.emit

## ProviderAccounts

Ƭ **ProviderAccounts**: `Account`[]

---

## Account

Ƭ **Account**: `string`

---

## Listener

Ƭ **Listener**: (...`args`: `unknown`[]) => `void`

Type declaration

▸ (...`args`): `void`

Parameters

| Name      | Type        |
| :-------- | :---------- |
| `...args` | `unknown`[] |

Returns

`void`

---

## Interface: SimpleEventEmitter

| Name           | Type                            | Description |
| :------------- | :------------------------------ | :---------- |
| on             | (`event`, `listener`): `void`   |             |
| once           | (`event`, `listener`): `void`   |             |
| removeListener | (`event`, `listener`): `void`   |             |
| off            | (`event`, `listener`): `void`   |             |
| emit           | (`event`, ...`args`): `boolean` |             |

### on

▸ **on**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

### once

▸ **once**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

### removeListener

▸ **removeListener**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

### off

▸ **off**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

### emit

▸ **emit**(`event`, ...`args`): `boolean`

Parameters

| Name      | Type        |
| :-------- | :---------- |
| `event`   | `string`    |
| `...args` | `unknown`[] |

Returns

`boolean`

## on

▸ **on**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

## once

▸ **once**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

## removeListener

▸ **removeListener**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

## off

▸ **off**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

## emit

▸ **emit**(`event`, ...`args`): `boolean`

Parameters

| Name      | Type        |
| :-------- | :---------- |
| `event`   | `string`    |
| `...args` | `unknown`[] |

Returns

`boolean`

## request

▸ **request**(`args`): `Promise`<`unknown`\>

Parameters

| Name   | Type          |
| :----- | :------------ |
| `args` | `RequestArgs` |

Returns

`Promise`<`unknown`\>

---

## Interface: EnableArgs

| Name      | Type                                                                                                                                                 | Description |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| chain?    | \`eip155:${string}eip155:${string}\` \| \`cosmos:${string}cosmos:${string}\` \| \`trust:${string}trust:${string}\` \| \`w3w:${string}w3w:${string}\` |             |
| topicId?  | `TopicId`                                                                                                                                            |             |
| metaData? | `ClientMetadata`                                                                                                                                     |             |

## enable

▸ **enable**(): `Promise`<`ProviderAccounts`\>

Returns

`Promise`<`ProviderAccounts`\>

---

## Interface: ConnectArgs

| Name      | Type             | Description |
| :-------- | :--------------- | :---------- |
| topicId?  | `TopicId`        |             |
| metaData? | `ClientMetadata` |             |

## request

▸ **request**<`T`\>(`args`, `chain?`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `args`   | `RequestArgs`                                                                            |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`T`\>

Overrides

EIP1193Provider.request

---

## sendAsync

▸ **sendAsync**<`T`\>(`args`, `callback`, `chain?`): `void`

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name       | Type                                                                   |
| :--------- | :--------------------------------------------------------------------- |
| `args`     | `RequestArgs`                                                          |
| `callback` | (`error`: `null` \| `Error`, `response`: `undefined` \| `T`) => `void` |
| `chain?`   | `string`                                                               |

Returns

`void`

---

## Interface: EnableArgs

| Name      | Type                                                                                                                                                 | Description |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| chain?    | \`eip155:${string}eip155:${string}\` \| \`cosmos:${string}cosmos:${string}\` \| \`trust:${string}trust:${string}\` \| \`w3w:${string}w3w:${string}\` |             |
| topicId?  | `TopicId`                                                                                                                                            |             |
| metaData? | `ClientMetadata`                                                                                                                                     |             |

## enable

▸ **enable**(`args?`): `Promise`<`string`[]\>

Parameters

| Name    | Type         |
| :------ | :----------- |
| `args?` | `EnableArgs` |

Returns

`Promise`<`string`[]\>

Overrides

EIP1193Provider.enable

---

## Interface: ConnectArgs

| Name      | Type             | Description |
| :-------- | :--------------- | :---------- |
| topicId?  | `TopicId`        |             |
| metaData? | `ClientMetadata` |             |

## connect

▸ **connect**(`args?`): `Promise`<`void`\>

Parameters

| Name    | Type          |
| :------ | :------------ |
| `args?` | `ConnectArgs` |

Returns

`Promise`<`void`\>

---

## disconnect

▸ **disconnect**(): `void`

Returns

`void`

## AccountsMap

Ƭ **AccountsMap**: `Object`

Type declaration

| Name     | Type                                                       |
| :------- | :--------------------------------------------------------- |
| `eip155` | `undefined` \| `Record`<\`eip155:${string}\`, `string`[]\> |
| `cosmos` | `undefined` \| `Record`<\`cosmos:${string}\`, `string`[]\> |
| `trust`  | `undefined` \| `Record`<\`trust:${string}\`, `string`[]\>  |
| `w3w`    | `undefined` \| `Record`<\`w3w:${string}\`, `string`[]\>    |

---

## Interface: IAdaptor

| Name              | Type                            | Description |
| :---------------- | :------------------------------ | :---------- |
| name              | `string`                        |             |
| chainId           | `string`                        |             |
| events            | `SimpleEventEmitter`            |             |
| namespace         | `NamespaceConfig`<`Namespace`\> |             |
| request           | (`args`): `Promise`<`T`\>       |             |
| updateNamespace   | (`namespace`): `void`           |             |
| getDefaultChainId | (): `string`                    |             |
| setDefaultChainId | (`chainId`): `void`             |             |
| requestAccounts   | (`chainId?`): `string`[]        |             |

### request

▸ **request**<`T`\>(`args`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name   | Type                 |
| :----- | :------------------- |
| `args` | `AdaptorRequestArgs` |

Returns

`Promise`<`T`\>

---

### updateNamespace

▸ **updateNamespace**(`namespace`): `void`

Parameters

| Name        | Type                            |
| :---------- | :------------------------------ |
| `namespace` | `NamespaceConfig`<`Namespace`\> |

Returns

`void`

---

### getDefaultChainId

▸ **getDefaultChainId**(): `string`

Returns

`string`

---

### setDefaultChainId

▸ **setDefaultChainId**(`chainId`): `void`

Parameters

| Name      | Type     |
| :-------- | :------- |
| `chainId` | `string` |

Returns

`void`

---

### requestAccounts

▸ **requestAccounts**(`chainId?`): `string`[]

Parameters

| Name       | Type     |
| :--------- | :------- |
| `chainId?` | `string` |

Returns

`string`[]

## Interface: AdaptorRequestArgs

| Name      | Type                                          | Description |
| :-------- | :-------------------------------------------- | :---------- |
| chainId   | `string`                                      |             |
| topicId   | `TopicId`                                     |             |
| method    | `string`                                      |             |
| params?   | `unknown`[] \| `Record`<`string`, `unknown`\> |             |
| metadata? | `ClientMetadata`                              |             |

## NamespaceConfig

Ƭ **NamespaceConfig**<`NS`\>: `Object`

Type parameters

| Name | Type                |
| :--- | :------------------ |
| `NS` | extends `Namespace` |

Type declaration

| Name       | Type                           |
| :--------- | :----------------------------- |
| `chains`   | `Chain`<`NS`\>[]               |
| `accounts` | \`${Chain<NS\>}:${Account}\`[] |

---

## Namespace

Ƭ **Namespace**: `"eip155"` \| `"cosmos"` \| `"trust"` \| `"w3w"`

---

## Chain

Ƭ **Chain**<`NS`\>: \`${NS}:${ChainId}\`

Type parameters

| Name | Type                              |
| :--- | :-------------------------------- |
| `NS` | extends `Namespace` = `Namespace` |

---

## Namespace

Ƭ **Namespace**: `"eip155"` \| `"cosmos"` \| `"trust"` \| `"w3w"`

---

## Class: UniversalProvider

| Name                   | Type                                                                                 | Description |
| :--------------------- | :----------------------------------------------------------------------------------- | :---------- |
| topicId                | `TopicId`                                                                            |             |
| metaData?              | `ClientMetadata`                                                                     |             |
| events                 | `SimpleEventEmitter`                                                                 |             |
| namespaces             | `NamespaceRecord` = `{}`                                                             |             |
| rpcAdaptors            | `RpcAdaptorMap` = `{}`                                                               |             |
| rpcHooks               | `RPCHooks`                                                                           |             |
| isConnecting           | `boolean` = `false`                                                                  |             |
| on                     | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| once                   | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| removeListener         | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| off                    | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| emit                   | <E\>(`event`: `E`, `payload`: `EventArguments`[`E`]) => `boolean`                    |             |
| isConnected            | `boolean`                                                                            |             |
| request                | (`args`, `chain?`): `Promise`<`T`\>                                                  |             |
| sendAsync              | (`args`, `callback`, `chain?`): `void`                                               |             |
| enable                 | (`__namedParameters?`): `Promise`<`string`[]\>                                       |             |
| connect                | (`__namedParameters?`): `Promise`<`void`\>                                           |             |
| disconnect             | (): `Promise`<`void`\>                                                               |             |
| setDefaultChain        | (`chain`): `void`                                                                    |             |
| onAccountsChanged      | (`accountsMap`): `void`                                                              |             |
| initialize             | (): `Promise`<`void`\>                                                               |             |
| createAdaptors         | (): `void`                                                                           |             |
| registerEventListeners | (): `void`                                                                           |             |
| getAdaptor             | (`namespace`): `IAdaptor`                                                            |             |
| setNamespaces          | (`accountsMap`): `void`                                                              |             |
| validateChain          | (`chain?`): [`Namespace`, `string`]                                                  |             |
| requestAccounts        | (`chain?`): `Promise`<`string`[]\>                                                   |             |
| onConnect              | (): `void`                                                                           |             |
| onChainChanged         | (`chain`): `void`                                                                    |             |
| init                   | (`options`): `Promise`<`UniversalProvider`\>                                         |             |

### request

▸ **request**<`T`\>(`args`, `chain?`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `args`   | `RequestArgs`                                                                            |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`T`\>

Implementation of

IUniversalProvider.request

---

### sendAsync

▸ **sendAsync**<`T`\>(`args`, `callback`, `chain?`): `void`

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name       | Type                                                                                     |
| :--------- | :--------------------------------------------------------------------------------------- |
| `args`     | `RequestArgs`                                                                            |
| `callback` | (`error`: `null` \| `Error`, `response`: `undefined` \| `T`) => `void`                   |
| `chain?`   | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

Implementation of

IUniversalProvider.sendAsync

---

### enable

▸ **enable**(`__namedParameters?`): `Promise`<`string`[]\>

Parameters

| Name                | Type         |
| :------------------ | :----------- |
| `__namedParameters` | `EnableArgs` |

Returns

`Promise`<`string`[]\>

Implementation of

IUniversalProvider.enable

---

### connect

▸ **connect**(`__namedParameters?`): `Promise`<`void`\>

Parameters

| Name                | Type          |
| :------------------ | :------------ |
| `__namedParameters` | `ConnectArgs` |

Returns

`Promise`<`void`\>

Implementation of

IUniversalProvider.connect

---

### disconnect

▸ **disconnect**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

Implementation of

IUniversalProvider.disconnect

---

### setDefaultChain

▸ **setDefaultChain**(`chain`): `void`

Parameters

| Name    | Type                                                                                     |
| :------ | :--------------------------------------------------------------------------------------- |
| `chain` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

---

### onAccountsChanged

▸ **onAccountsChanged**(`accountsMap`): `void`

Parameters

| Name          | Type          |
| :------------ | :------------ |
| `accountsMap` | `AccountsMap` |

Returns

`void`

---

### initialize

▸ `Private` **initialize**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### createAdaptors

▸ `Private` **createAdaptors**(): `void`

Returns

`void`

---

### registerEventListeners

▸ `Private` **registerEventListeners**(): `void`

Returns

`void`

---

### getAdaptor

▸ `Private` **getAdaptor**(`namespace`): `IAdaptor`

Parameters

| Name        | Type        |
| :---------- | :---------- |
| `namespace` | `Namespace` |

Returns

`IAdaptor`

---

### setNamespaces

▸ `Private` **setNamespaces**(`accountsMap`): `void`

Parameters

| Name          | Type          |
| :------------ | :------------ |
| `accountsMap` | `AccountsMap` |

Returns

`void`

---

### validateChain

▸ `Private` **validateChain**(`chain?`): [`Namespace`, `string`]

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

[`Namespace`, `string`]

---

### requestAccounts

▸ `Private` **requestAccounts**(`chain?`): `Promise`<`string`[]\>

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`string`[]\>

---

### onConnect

▸ `Private` **onConnect**(): `void`

Returns

`void`

---

### onChainChanged

▸ `Private` **onChainChanged**(`chain`): `void`

Parameters

| Name    | Type                                                                                     |
| :------ | :--------------------------------------------------------------------------------------- |
| `chain` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

---

### init

▸ `Static` **init**(`options`): `Promise`<`UniversalProvider`\>

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `options` | `UniversalProviderOptions` |

Returns

`Promise`<`UniversalProvider`\>

## Interface: UniversalProviderOptions

| Name      | Type             | Description |
| :-------- | :--------------- | :---------- |
| rpcHooks  | `RPCHooks`       |             |
| topicId?  | `TopicId`        |             |
| metaData? | `ClientMetadata` |             |

---

# bn.initUniversalWeb3Provider

▸ **initUniversalWeb3Provider**(`options?`): `Promise`<{ `result`: `UniversalProvider` }\>

Parameters

| Name       | Type                                                             |
| :--------- | :--------------------------------------------------------------- |
| `options?` | `Pick`<`UniversalProviderOptions`, `"topicId"` \| `"metaData"`\> |

Returns

`Promise`<{ `result`: `UniversalProvider` }\>

## Interface: UniversalProviderOptions

| Name      | Type             | Description |
| :-------- | :--------------- | :---------- |
| rpcHooks  | `RPCHooks`       |             |
| topicId?  | `TopicId`        |             |
| metaData? | `ClientMetadata` |             |

## Class: UniversalProvider

| Name                   | Type                                                                                 | Description |
| :--------------------- | :----------------------------------------------------------------------------------- | :---------- |
| topicId                | `TopicId`                                                                            |             |
| metaData?              | `ClientMetadata`                                                                     |             |
| events                 | `SimpleEventEmitter`                                                                 |             |
| namespaces             | `NamespaceRecord` = `{}`                                                             |             |
| rpcAdaptors            | `RpcAdaptorMap` = `{}`                                                               |             |
| rpcHooks               | `RPCHooks`                                                                           |             |
| isConnecting           | `boolean` = `false`                                                                  |             |
| on                     | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| once                   | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| removeListener         | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| off                    | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| emit                   | <E\>(`event`: `E`, `payload`: `EventArguments`[`E`]) => `boolean`                    |             |
| isConnected            | `boolean`                                                                            |             |
| request                | (`args`, `chain?`): `Promise`<`T`\>                                                  |             |
| sendAsync              | (`args`, `callback`, `chain?`): `void`                                               |             |
| enable                 | (`__namedParameters?`): `Promise`<`string`[]\>                                       |             |
| connect                | (`__namedParameters?`): `Promise`<`void`\>                                           |             |
| disconnect             | (): `Promise`<`void`\>                                                               |             |
| setDefaultChain        | (`chain`): `void`                                                                    |             |
| onAccountsChanged      | (`accountsMap`): `void`                                                              |             |
| initialize             | (): `Promise`<`void`\>                                                               |             |
| createAdaptors         | (): `void`                                                                           |             |
| registerEventListeners | (): `void`                                                                           |             |
| getAdaptor             | (`namespace`): `IAdaptor`                                                            |             |
| setNamespaces          | (`accountsMap`): `void`                                                              |             |
| validateChain          | (`chain?`): [`Namespace`, `string`]                                                  |             |
| requestAccounts        | (`chain?`): `Promise`<`string`[]\>                                                   |             |
| onConnect              | (): `void`                                                                           |             |
| onChainChanged         | (`chain`): `void`                                                                    |             |
| init                   | (`options`): `Promise`<`UniversalProvider`\>                                         |             |

### request

▸ **request**<`T`\>(`args`, `chain?`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `args`   | `RequestArgs`                                                                            |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`T`\>

Implementation of

IUniversalProvider.request

---

### sendAsync

▸ **sendAsync**<`T`\>(`args`, `callback`, `chain?`): `void`

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name       | Type                                                                                     |
| :--------- | :--------------------------------------------------------------------------------------- |
| `args`     | `RequestArgs`                                                                            |
| `callback` | (`error`: `null` \| `Error`, `response`: `undefined` \| `T`) => `void`                   |
| `chain?`   | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

Implementation of

IUniversalProvider.sendAsync

---

### enable

▸ **enable**(`__namedParameters?`): `Promise`<`string`[]\>

Parameters

| Name                | Type         |
| :------------------ | :----------- |
| `__namedParameters` | `EnableArgs` |

Returns

`Promise`<`string`[]\>

Implementation of

IUniversalProvider.enable

---

### connect

▸ **connect**(`__namedParameters?`): `Promise`<`void`\>

Parameters

| Name                | Type          |
| :------------------ | :------------ |
| `__namedParameters` | `ConnectArgs` |

Returns

`Promise`<`void`\>

Implementation of

IUniversalProvider.connect

---

### disconnect

▸ **disconnect**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

Implementation of

IUniversalProvider.disconnect

---

### setDefaultChain

▸ **setDefaultChain**(`chain`): `void`

Parameters

| Name    | Type                                                                                     |
| :------ | :--------------------------------------------------------------------------------------- |
| `chain` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

---

### onAccountsChanged

▸ **onAccountsChanged**(`accountsMap`): `void`

Parameters

| Name          | Type          |
| :------------ | :------------ |
| `accountsMap` | `AccountsMap` |

Returns

`void`

---

### initialize

▸ `Private` **initialize**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### createAdaptors

▸ `Private` **createAdaptors**(): `void`

Returns

`void`

---

### registerEventListeners

▸ `Private` **registerEventListeners**(): `void`

Returns

`void`

---

### getAdaptor

▸ `Private` **getAdaptor**(`namespace`): `IAdaptor`

Parameters

| Name        | Type        |
| :---------- | :---------- |
| `namespace` | `Namespace` |

Returns

`IAdaptor`

---

### setNamespaces

▸ `Private` **setNamespaces**(`accountsMap`): `void`

Parameters

| Name          | Type          |
| :------------ | :------------ |
| `accountsMap` | `AccountsMap` |

Returns

`void`

---

### validateChain

▸ `Private` **validateChain**(`chain?`): [`Namespace`, `string`]

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

[`Namespace`, `string`]

---

### requestAccounts

▸ `Private` **requestAccounts**(`chain?`): `Promise`<`string`[]\>

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`string`[]\>

---

### onConnect

▸ `Private` **onConnect**(): `void`

Returns

`void`

---

### onChainChanged

▸ `Private` **onChainChanged**(`chain`): `void`

Parameters

| Name    | Type                                                                                     |
| :------ | :--------------------------------------------------------------------------------------- |
| `chain` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

---

### init

▸ `Static` **init**(`options`): `Promise`<`UniversalProvider`\>

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `options` | `UniversalProviderOptions` |

Returns

`Promise`<`UniversalProvider`\>

## Interface: RequestArgs

| Name      | Type                                          | Description |
| :-------- | :-------------------------------------------- | :---------- |
| method    | `string`                                      |             |
| params?   | `unknown`[] \| `Record`<`string`, `unknown`\> |             |
| metadata? | `ClientMetadata`                              |             |

## Interface: IUniversalProvider

| Name           | Type                                                                                 | Description |
| :------------- | :----------------------------------------------------------------------------------- | :---------- |
| topicId        | `TopicId`                                                                            |             |
| metaData?      | `ClientMetadata`                                                                     |             |
| events         | `SimpleEventEmitter`                                                                 |             |
| namespaces?    | `NamespaceRecord`                                                                    |             |
| rpcAdaptors    | `RpcAdaptorMap`                                                                      |             |
| on             | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| once           | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| off            | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| removeListener | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| emit           | <E\>(`event`: `E`, `payload`: `EventArguments`[`E`]) => `boolean`                    |             |
| request        | (`args`, `chain?`): `Promise`<`T`\>                                                  |             |
| sendAsync      | (`args`, `callback`, `chain?`): `void`                                               |             |
| enable         | (`args?`): `Promise`<`string`[]\>                                                    |             |
| connect        | (`args?`): `Promise`<`void`\>                                                        |             |
| disconnect     | (): `void`                                                                           |             |

### request

▸ **request**<`T`\>(`args`, `chain?`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `args`   | `RequestArgs`                                                                            |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`T`\>

Overrides

EIP1193Provider.request

---

### sendAsync

▸ **sendAsync**<`T`\>(`args`, `callback`, `chain?`): `void`

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name       | Type                                                                   |
| :--------- | :--------------------------------------------------------------------- |
| `args`     | `RequestArgs`                                                          |
| `callback` | (`error`: `null` \| `Error`, `response`: `undefined` \| `T`) => `void` |
| `chain?`   | `string`                                                               |

Returns

`void`

---

### enable

▸ **enable**(`args?`): `Promise`<`string`[]\>

Parameters

| Name    | Type         |
| :------ | :----------- |
| `args?` | `EnableArgs` |

Returns

`Promise`<`string`[]\>

Overrides

EIP1193Provider.enable

---

### connect

▸ **connect**(`args?`): `Promise`<`void`\>

Parameters

| Name    | Type          |
| :------ | :------------ |
| `args?` | `ConnectArgs` |

Returns

`Promise`<`void`\>

---

### disconnect

▸ **disconnect**(): `void`

Returns

`void`

## Interface: RequestArgs

| Name      | Type                                          | Description |
| :-------- | :-------------------------------------------- | :---------- |
| method    | `string`                                      |             |
| params?   | `unknown`[] \| `Record`<`string`, `unknown`\> |             |
| metadata? | `ClientMetadata`                              |             |

## Interface: EIP1193Provider

| Name           | Type                               | Description |
| :------------- | :--------------------------------- | :---------- |
| request        | (`args`): `Promise`<`unknown`\>    |             |
| enable         | (): `Promise`<`ProviderAccounts`\> |             |
| on             | (`event`, `listener`): `void`      |             |
| once           | (`event`, `listener`): `void`      |             |
| removeListener | (`event`, `listener`): `void`      |             |
| off            | (`event`, `listener`): `void`      |             |
| emit           | (`event`, ...`args`): `boolean`    |             |

### request

▸ **request**(`args`): `Promise`<`unknown`\>

Parameters

| Name   | Type          |
| :----- | :------------ |
| `args` | `RequestArgs` |

Returns

`Promise`<`unknown`\>

---

### enable

▸ **enable**(): `Promise`<`ProviderAccounts`\>

Returns

`Promise`<`ProviderAccounts`\>

---

### on

▸ **on**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

Inherited from

SimpleEventEmitter.on

---

### once

▸ **once**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

Inherited from

SimpleEventEmitter.once

---

### removeListener

▸ **removeListener**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

Inherited from

SimpleEventEmitter.removeListener

---

### off

▸ **off**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

Inherited from

SimpleEventEmitter.off

---

### emit

▸ **emit**(`event`, ...`args`): `boolean`

Parameters

| Name      | Type        |
| :-------- | :---------- |
| `event`   | `string`    |
| `...args` | `unknown`[] |

Returns

`boolean`

Inherited from

SimpleEventEmitter.emit

## ProviderAccounts

Ƭ **ProviderAccounts**: `Account`[]

---

## Account

Ƭ **Account**: `string`

---

## Listener

Ƭ **Listener**: (...`args`: `unknown`[]) => `void`

Type declaration

▸ (...`args`): `void`

Parameters

| Name      | Type        |
| :-------- | :---------- |
| `...args` | `unknown`[] |

Returns

`void`

---

## Interface: SimpleEventEmitter

| Name           | Type                            | Description |
| :------------- | :------------------------------ | :---------- |
| on             | (`event`, `listener`): `void`   |             |
| once           | (`event`, `listener`): `void`   |             |
| removeListener | (`event`, `listener`): `void`   |             |
| off            | (`event`, `listener`): `void`   |             |
| emit           | (`event`, ...`args`): `boolean` |             |

### on

▸ **on**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

### once

▸ **once**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

### removeListener

▸ **removeListener**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

### off

▸ **off**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

### emit

▸ **emit**(`event`, ...`args`): `boolean`

Parameters

| Name      | Type        |
| :-------- | :---------- |
| `event`   | `string`    |
| `...args` | `unknown`[] |

Returns

`boolean`

## on

▸ **on**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

## once

▸ **once**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

## removeListener

▸ **removeListener**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

## off

▸ **off**(`event`, `listener`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `event`    | `string`   |
| `listener` | `Listener` |

Returns

`void`

---

## emit

▸ **emit**(`event`, ...`args`): `boolean`

Parameters

| Name      | Type        |
| :-------- | :---------- |
| `event`   | `string`    |
| `...args` | `unknown`[] |

Returns

`boolean`

## request

▸ **request**(`args`): `Promise`<`unknown`\>

Parameters

| Name   | Type          |
| :----- | :------------ |
| `args` | `RequestArgs` |

Returns

`Promise`<`unknown`\>

---

## Interface: EnableArgs

| Name      | Type                                                                                                                                                 | Description |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| chain?    | \`eip155:${string}eip155:${string}\` \| \`cosmos:${string}cosmos:${string}\` \| \`trust:${string}trust:${string}\` \| \`w3w:${string}w3w:${string}\` |             |
| topicId?  | `TopicId`                                                                                                                                            |             |
| metaData? | `ClientMetadata`                                                                                                                                     |             |

## enable

▸ **enable**(): `Promise`<`ProviderAccounts`\>

Returns

`Promise`<`ProviderAccounts`\>

---

## Interface: ConnectArgs

| Name      | Type             | Description |
| :-------- | :--------------- | :---------- |
| topicId?  | `TopicId`        |             |
| metaData? | `ClientMetadata` |             |

## request

▸ **request**<`T`\>(`args`, `chain?`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `args`   | `RequestArgs`                                                                            |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`T`\>

Overrides

EIP1193Provider.request

---

## sendAsync

▸ **sendAsync**<`T`\>(`args`, `callback`, `chain?`): `void`

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name       | Type                                                                   |
| :--------- | :--------------------------------------------------------------------- |
| `args`     | `RequestArgs`                                                          |
| `callback` | (`error`: `null` \| `Error`, `response`: `undefined` \| `T`) => `void` |
| `chain?`   | `string`                                                               |

Returns

`void`

---

## Interface: EnableArgs

| Name      | Type                                                                                                                                                 | Description |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| chain?    | \`eip155:${string}eip155:${string}\` \| \`cosmos:${string}cosmos:${string}\` \| \`trust:${string}trust:${string}\` \| \`w3w:${string}w3w:${string}\` |             |
| topicId?  | `TopicId`                                                                                                                                            |             |
| metaData? | `ClientMetadata`                                                                                                                                     |             |

## enable

▸ **enable**(`args?`): `Promise`<`string`[]\>

Parameters

| Name    | Type         |
| :------ | :----------- |
| `args?` | `EnableArgs` |

Returns

`Promise`<`string`[]\>

Overrides

EIP1193Provider.enable

---

## Interface: ConnectArgs

| Name      | Type             | Description |
| :-------- | :--------------- | :---------- |
| topicId?  | `TopicId`        |             |
| metaData? | `ClientMetadata` |             |

## connect

▸ **connect**(`args?`): `Promise`<`void`\>

Parameters

| Name    | Type          |
| :------ | :------------ |
| `args?` | `ConnectArgs` |

Returns

`Promise`<`void`\>

---

## disconnect

▸ **disconnect**(): `void`

Returns

`void`

## AccountsMap

Ƭ **AccountsMap**: `Object`

Type declaration

| Name     | Type                                                       |
| :------- | :--------------------------------------------------------- |
| `eip155` | `undefined` \| `Record`<\`eip155:${string}\`, `string`[]\> |
| `cosmos` | `undefined` \| `Record`<\`cosmos:${string}\`, `string`[]\> |
| `trust`  | `undefined` \| `Record`<\`trust:${string}\`, `string`[]\>  |
| `w3w`    | `undefined` \| `Record`<\`w3w:${string}\`, `string`[]\>    |

---

## Interface: IAdaptor

| Name              | Type                            | Description |
| :---------------- | :------------------------------ | :---------- |
| name              | `string`                        |             |
| chainId           | `string`                        |             |
| events            | `SimpleEventEmitter`            |             |
| namespace         | `NamespaceConfig`<`Namespace`\> |             |
| request           | (`args`): `Promise`<`T`\>       |             |
| updateNamespace   | (`namespace`): `void`           |             |
| getDefaultChainId | (): `string`                    |             |
| setDefaultChainId | (`chainId`): `void`             |             |
| requestAccounts   | (`chainId?`): `string`[]        |             |

### request

▸ **request**<`T`\>(`args`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name   | Type                 |
| :----- | :------------------- |
| `args` | `AdaptorRequestArgs` |

Returns

`Promise`<`T`\>

---

### updateNamespace

▸ **updateNamespace**(`namespace`): `void`

Parameters

| Name        | Type                            |
| :---------- | :------------------------------ |
| `namespace` | `NamespaceConfig`<`Namespace`\> |

Returns

`void`

---

### getDefaultChainId

▸ **getDefaultChainId**(): `string`

Returns

`string`

---

### setDefaultChainId

▸ **setDefaultChainId**(`chainId`): `void`

Parameters

| Name      | Type     |
| :-------- | :------- |
| `chainId` | `string` |

Returns

`void`

---

### requestAccounts

▸ **requestAccounts**(`chainId?`): `string`[]

Parameters

| Name       | Type     |
| :--------- | :------- |
| `chainId?` | `string` |

Returns

`string`[]

## Interface: AdaptorRequestArgs

| Name      | Type                                          | Description |
| :-------- | :-------------------------------------------- | :---------- |
| chainId   | `string`                                      |             |
| topicId   | `TopicId`                                     |             |
| method    | `string`                                      |             |
| params?   | `unknown`[] \| `Record`<`string`, `unknown`\> |             |
| metadata? | `ClientMetadata`                              |             |

## NamespaceConfig

Ƭ **NamespaceConfig**<`NS`\>: `Object`

Type parameters

| Name | Type                |
| :--- | :------------------ |
| `NS` | extends `Namespace` |

Type declaration

| Name       | Type                           |
| :--------- | :----------------------------- |
| `chains`   | `Chain`<`NS`\>[]               |
| `accounts` | \`${Chain<NS\>}:${Account}\`[] |

---

## Namespace

Ƭ **Namespace**: `"eip155"` \| `"cosmos"` \| `"trust"` \| `"w3w"`

---

## Chain

Ƭ **Chain**<`NS`\>: \`${NS}:${ChainId}\`

Type parameters

| Name | Type                              |
| :--- | :-------------------------------- |
| `NS` | extends `Namespace` = `Namespace` |

---

## Namespace

Ƭ **Namespace**: `"eip155"` \| `"cosmos"` \| `"trust"` \| `"w3w"`

---

## Class: UniversalProvider

| Name                   | Type                                                                                 | Description |
| :--------------------- | :----------------------------------------------------------------------------------- | :---------- |
| topicId                | `TopicId`                                                                            |             |
| metaData?              | `ClientMetadata`                                                                     |             |
| events                 | `SimpleEventEmitter`                                                                 |             |
| namespaces             | `NamespaceRecord` = `{}`                                                             |             |
| rpcAdaptors            | `RpcAdaptorMap` = `{}`                                                               |             |
| rpcHooks               | `RPCHooks`                                                                           |             |
| isConnecting           | `boolean` = `false`                                                                  |             |
| on                     | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| once                   | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| removeListener         | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| off                    | <E\>(`event`: `E`, `listener`: ((`args`: `EventArguments`[`E`]) => `void`) => `void` |             |
| emit                   | <E\>(`event`: `E`, `payload`: `EventArguments`[`E`]) => `boolean`                    |             |
| isConnected            | `boolean`                                                                            |             |
| request                | (`args`, `chain?`): `Promise`<`T`\>                                                  |             |
| sendAsync              | (`args`, `callback`, `chain?`): `void`                                               |             |
| enable                 | (`__namedParameters?`): `Promise`<`string`[]\>                                       |             |
| connect                | (`__namedParameters?`): `Promise`<`void`\>                                           |             |
| disconnect             | (): `Promise`<`void`\>                                                               |             |
| setDefaultChain        | (`chain`): `void`                                                                    |             |
| onAccountsChanged      | (`accountsMap`): `void`                                                              |             |
| initialize             | (): `Promise`<`void`\>                                                               |             |
| createAdaptors         | (): `void`                                                                           |             |
| registerEventListeners | (): `void`                                                                           |             |
| getAdaptor             | (`namespace`): `IAdaptor`                                                            |             |
| setNamespaces          | (`accountsMap`): `void`                                                              |             |
| validateChain          | (`chain?`): [`Namespace`, `string`]                                                  |             |
| requestAccounts        | (`chain?`): `Promise`<`string`[]\>                                                   |             |
| onConnect              | (): `void`                                                                           |             |
| onChainChanged         | (`chain`): `void`                                                                    |             |
| init                   | (`options`): `Promise`<`UniversalProvider`\>                                         |             |

### request

▸ **request**<`T`\>(`args`, `chain?`): `Promise`<`T`\>

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `args`   | `RequestArgs`                                                                            |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`T`\>

Implementation of

IUniversalProvider.request

---

### sendAsync

▸ **sendAsync**<`T`\>(`args`, `callback`, `chain?`): `void`

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name       | Type                                                                                     |
| :--------- | :--------------------------------------------------------------------------------------- |
| `args`     | `RequestArgs`                                                                            |
| `callback` | (`error`: `null` \| `Error`, `response`: `undefined` \| `T`) => `void`                   |
| `chain?`   | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

Implementation of

IUniversalProvider.sendAsync

---

### enable

▸ **enable**(`__namedParameters?`): `Promise`<`string`[]\>

Parameters

| Name                | Type         |
| :------------------ | :----------- |
| `__namedParameters` | `EnableArgs` |

Returns

`Promise`<`string`[]\>

Implementation of

IUniversalProvider.enable

---

### connect

▸ **connect**(`__namedParameters?`): `Promise`<`void`\>

Parameters

| Name                | Type          |
| :------------------ | :------------ |
| `__namedParameters` | `ConnectArgs` |

Returns

`Promise`<`void`\>

Implementation of

IUniversalProvider.connect

---

### disconnect

▸ **disconnect**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

Implementation of

IUniversalProvider.disconnect

---

### setDefaultChain

▸ **setDefaultChain**(`chain`): `void`

Parameters

| Name    | Type                                                                                     |
| :------ | :--------------------------------------------------------------------------------------- |
| `chain` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

---

### onAccountsChanged

▸ **onAccountsChanged**(`accountsMap`): `void`

Parameters

| Name          | Type          |
| :------------ | :------------ |
| `accountsMap` | `AccountsMap` |

Returns

`void`

---

### initialize

▸ `Private` **initialize**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### createAdaptors

▸ `Private` **createAdaptors**(): `void`

Returns

`void`

---

### registerEventListeners

▸ `Private` **registerEventListeners**(): `void`

Returns

`void`

---

### getAdaptor

▸ `Private` **getAdaptor**(`namespace`): `IAdaptor`

Parameters

| Name        | Type        |
| :---------- | :---------- |
| `namespace` | `Namespace` |

Returns

`IAdaptor`

---

### setNamespaces

▸ `Private` **setNamespaces**(`accountsMap`): `void`

Parameters

| Name          | Type          |
| :------------ | :------------ |
| `accountsMap` | `AccountsMap` |

Returns

`void`

---

### validateChain

▸ `Private` **validateChain**(`chain?`): [`Namespace`, `string`]

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

[`Namespace`, `string`]

---

### requestAccounts

▸ `Private` **requestAccounts**(`chain?`): `Promise`<`string`[]\>

Parameters

| Name     | Type                                                                                     |
| :------- | :--------------------------------------------------------------------------------------- |
| `chain?` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`Promise`<`string`[]\>

---

### onConnect

▸ `Private` **onConnect**(): `void`

Returns

`void`

---

### onChainChanged

▸ `Private` **onChainChanged**(`chain`): `void`

Parameters

| Name    | Type                                                                                     |
| :------ | :--------------------------------------------------------------------------------------- |
| `chain` | \`eip155:${string}\` \| \`cosmos:${string}\` \| \`trust:${string}\` \| \`w3w:${string}\` |

Returns

`void`

---

### init

▸ `Static` **init**(`options`): `Promise`<`UniversalProvider`\>

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `options` | `UniversalProviderOptions` |

Returns

`Promise`<`UniversalProvider`\>

## Interface: UniversalProviderOptions

| Name      | Type             | Description |
| :-------- | :--------------- | :---------- |
| rpcHooks  | `RPCHooks`       |             |
| topicId?  | `TopicId`        |             |
| metaData? | `ClientMetadata` |             |