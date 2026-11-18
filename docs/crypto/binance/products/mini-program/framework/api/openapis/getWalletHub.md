---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/getWalletHub
api_type: Guide
updated_at: 2026-11-18 02:36:06.761602
---

# bn.getWalletHub

▸ **getWalletHub**(): `WalletHub`

**`description`** The api to get wallet hub

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
// get walletHub and open by uri and chainId
const walletHub = bn.getWalletHub();
const response = await walletHub.open({
  uri: "my-uri",
  chainId: 1,
});
console.log(response);
```

Returns

`WalletHub`

## Class: WalletHub

| Name       | Type                                      | Description |
| :--------- | :---------------------------------------- | :---------- |
| \_rpcHooks | `RPCHooks`                                |             |
| open       | (`__namedParameters`): `Promise`<`void`\> |             |
| close      | (): `Promise`<`void`\>                    |             |
| openWallet | (`__namedParameters`): `Promise`<`void`\> |             |

### open

▸ **open**(`__namedParameters`): `Promise`<`void`\>

Parameters

| Name                | Type                   |
| :------------------ | :--------------------- |
| `__namedParameters` | `WalletHubOpenPayload` |

Returns

`Promise`<`void`\>

---

### close

▸ **close**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### openWallet

▸ **openWallet**(`__namedParameters`): `Promise`<`void`\>

Parameters

| Name                | Type                         |
| :------------------ | :--------------------------- |
| `__namedParameters` | `WalletHubOpenWalletPayload` |

Returns

`Promise`<`void`\>

## WalletHubOpenPayload

Ƭ **WalletHubOpenPayload**: `Object`

Type declaration

| Name      | Type     |
| :-------- | :------- |
| `uri`     | `string` |
| `chainId` | `number` |

---

## WalletHubOpenWalletPayload

Ƭ **WalletHubOpenWalletPayload**: `Object`

Type declaration

| Name | Type     |
| :--- | :------- |
| `id` | `string` |

---

---

# bn.getWalletHub

▸ **getWalletHub**(): `WalletHub`

**`description`** The api to get wallet hub

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
// get walletHub and open by uri and chainId
const walletHub = bn.getWalletHub();
const response = await walletHub.open({
  uri: "my-uri",
  chainId: 1,
});
console.log(response);
```

Returns

`WalletHub`

## Class: WalletHub

| Name       | Type                                      | Description |
| :--------- | :---------------------------------------- | :---------- |
| \_rpcHooks | `RPCHooks`                                |             |
| open       | (`__namedParameters`): `Promise`<`void`\> |             |
| close      | (): `Promise`<`void`\>                    |             |
| openWallet | (`__namedParameters`): `Promise`<`void`\> |             |

### open

▸ **open**(`__namedParameters`): `Promise`<`void`\>

Parameters

| Name                | Type                   |
| :------------------ | :--------------------- |
| `__namedParameters` | `WalletHubOpenPayload` |

Returns

`Promise`<`void`\>

---

### close

▸ **close**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### openWallet

▸ **openWallet**(`__namedParameters`): `Promise`<`void`\>

Parameters

| Name                | Type                         |
| :------------------ | :--------------------------- |
| `__namedParameters` | `WalletHubOpenWalletPayload` |

Returns

`Promise`<`void`\>

## WalletHubOpenPayload

Ƭ **WalletHubOpenPayload**: `Object`

Type declaration

| Name      | Type     |
| :-------- | :------- |
| `uri`     | `string` |
| `chainId` | `number` |

---

## WalletHubOpenWalletPayload

Ƭ **WalletHubOpenWalletPayload**: `Object`

Type declaration

| Name | Type     |
| :--- | :------- |
| `id` | `string` |

---