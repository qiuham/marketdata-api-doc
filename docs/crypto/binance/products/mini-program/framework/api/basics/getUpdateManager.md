---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/getUpdateManager
api_type: Guide
updated_at: 2026-11-22 18:45:19.900774
---

# bn.getUpdateManager

▸ **getUpdateManager**(): `UpdateManager`

**`description`** ObtainGlobally uniqueThe version update manager for managing Mini Program updates.

**`example`**

```ts
const updateManager = bn.getUpdateManager()

updateManager.onCheckForUpdate(function (res) {
  // Callback after requesting new version information
  console.log(res.hasUpdate)
})

updateManager.onUpdateReady(function () {
  bn.showModal({
    title: 'Update tip ',
    content: 'The new version is ready, reboot the app? ' '，
    success: function (res) {
      if (res.confirm) {
        // The new version has been downloaded and calls applyUpdate Apply a new version and restart
        updateManager.applyUpdate()
      }
    }
  })
})

updateManager.onUpdateFailed(function () {
  // New version download failed
})
```

Returns

`UpdateManager`

UpdateManager

## Interface: UpdateManager

| Name             | Type                            | Description                                                                                                                                                                                                          |
| :--------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| applyUpdate      | (`params?`): `Promise`<`void`\> | Force the Mini Program to restart and use the new version. After the new version of the Mini Program has been downloaded (i.e. received onUpdateReady Callback) call.                                                |
| onCheckForUpdate | (`callback`): `void`            | Monitor the BN background request to check the update results event. BN automatically checks updates when the Mini Program is cold started, without the developer taking the initiative to trigger.                  |
| onUpdateReady    | (`callback`): `void`            | Listening Mini Program has a version update event. Active client trigger download (no developer trigger), download success callback                                                                                  |
| onUpdateFailed   | (`callback`): `void`            | Listen for Mini Programs to update failed events. Mini Program has a new version, the client active trigger download (without developer trigger), download failure (may be network reasons, etc.) after the callback |

### applyUpdate

▸ **applyUpdate**(`params?`): `Promise`<`void`\>

Force the Mini Program to restart and use the new version. After the new version of the Mini Program
has been downloaded (i.e. received onUpdateReady Callback) call.

Parameters

| Name         | Type     |
| :----------- | :------- |
| `params?`    | `Object` |
| `params.url` | `string` |

Returns

`Promise`<`void`\>

---

### onCheckForUpdate

▸ **onCheckForUpdate**(`callback`): `void`

Monitor the BN background request to check the update results event. BN automatically checks updates
when the Mini Program is cold started, without the developer taking the initiative to trigger.

Parameters

| Name       | Type                          |
| :--------- | :---------------------------- |
| `callback` | `OnAppCheckForUpdateCallback` |

Returns

`void`

---

### onUpdateReady

▸ **onUpdateReady**(`callback`): `void`

Listening Mini Program has a version update event. Active client trigger download (no developer
trigger), download success callback

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `callback` | `OnAppUpdateReadyCallback` |

Returns

`void`

---

### onUpdateFailed

▸ **onUpdateFailed**(`callback`): `void`

Listen for Mini Programs to update failed events. Mini Program has a new version, the client active
trigger download (without developer trigger), download failure (may be network reasons, etc.) after
the callback

Parameters

| Name       | Type                        |
| :--------- | :-------------------------- |
| `callback` | `OnAppUpdateFailedCallback` |

Returns

`void`

## OnAppCheckForUpdateCallback

Ƭ **OnAppCheckForUpdateCallback**: (`payload`: `EventAppCheckForUpdatePayload`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type                            |
| :-------- | :------------------------------ |
| `payload` | `EventAppCheckForUpdatePayload` |

Returns

`void`

---

## EventAppCheckForUpdatePayload

Ƭ **EventAppCheckForUpdatePayload**: `Object`

Type declaration

| Name             | Type      | Description                                  |
| :--------------- | :-------- | :------------------------------------------- |
| `hasUpdate`      | `boolean` | Indicates whether a new version is available |
| `latestVersion?` | `string`  | The version of the latest app.               |

## OnAppUpdateReadyCallback

Ƭ **OnAppUpdateReadyCallback**: (`payload`: `EventAppCheckForUpdatePayload`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type                            |
| :-------- | :------------------------------ |
| `payload` | `EventAppCheckForUpdatePayload` |

Returns

`void`

---

## OnAppUpdateFailedCallback

Ƭ **OnAppUpdateFailedCallback**: () => `void`

Type declaration

▸ (): `void`

Returns

`void`

---

---

# bn.getUpdateManager

▸ **getUpdateManager**(): `UpdateManager`

**`description`** ObtainGlobally uniqueThe version update manager for managing Mini Program updates.

**`example`**

```ts
const updateManager = bn.getUpdateManager()

updateManager.onCheckForUpdate(function (res) {
  // Callback after requesting new version information
  console.log(res.hasUpdate)
})

updateManager.onUpdateReady(function () {
  bn.showModal({
    title: 'Update tip ',
    content: 'The new version is ready, reboot the app? ' '，
    success: function (res) {
      if (res.confirm) {
        // The new version has been downloaded and calls applyUpdate Apply a new version and restart
        updateManager.applyUpdate()
      }
    }
  })
})

updateManager.onUpdateFailed(function () {
  // New version download failed
})
```

Returns

`UpdateManager`

UpdateManager

## Interface: UpdateManager

| Name             | Type                            | Description                                                                                                                                                                                                          |
| :--------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| applyUpdate      | (`params?`): `Promise`<`void`\> | Force the Mini Program to restart and use the new version. After the new version of the Mini Program has been downloaded (i.e. received onUpdateReady Callback) call.                                                |
| onCheckForUpdate | (`callback`): `void`            | Monitor the BN background request to check the update results event. BN automatically checks updates when the Mini Program is cold started, without the developer taking the initiative to trigger.                  |
| onUpdateReady    | (`callback`): `void`            | Listening Mini Program has a version update event. Active client trigger download (no developer trigger), download success callback                                                                                  |
| onUpdateFailed   | (`callback`): `void`            | Listen for Mini Programs to update failed events. Mini Program has a new version, the client active trigger download (without developer trigger), download failure (may be network reasons, etc.) after the callback |

### applyUpdate

▸ **applyUpdate**(`params?`): `Promise`<`void`\>

Force the Mini Program to restart and use the new version. After the new version of the Mini Program
has been downloaded (i.e. received onUpdateReady Callback) call.

Parameters

| Name         | Type     |
| :----------- | :------- |
| `params?`    | `Object` |
| `params.url` | `string` |

Returns

`Promise`<`void`\>

---

### onCheckForUpdate

▸ **onCheckForUpdate**(`callback`): `void`

Monitor the BN background request to check the update results event. BN automatically checks updates
when the Mini Program is cold started, without the developer taking the initiative to trigger.

Parameters

| Name       | Type                          |
| :--------- | :---------------------------- |
| `callback` | `OnAppCheckForUpdateCallback` |

Returns

`void`

---

### onUpdateReady

▸ **onUpdateReady**(`callback`): `void`

Listening Mini Program has a version update event. Active client trigger download (no developer
trigger), download success callback

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `callback` | `OnAppUpdateReadyCallback` |

Returns

`void`

---

### onUpdateFailed

▸ **onUpdateFailed**(`callback`): `void`

Listen for Mini Programs to update failed events. Mini Program has a new version, the client active
trigger download (without developer trigger), download failure (may be network reasons, etc.) after
the callback

Parameters

| Name       | Type                        |
| :--------- | :-------------------------- |
| `callback` | `OnAppUpdateFailedCallback` |

Returns

`void`

## OnAppCheckForUpdateCallback

Ƭ **OnAppCheckForUpdateCallback**: (`payload`: `EventAppCheckForUpdatePayload`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type                            |
| :-------- | :------------------------------ |
| `payload` | `EventAppCheckForUpdatePayload` |

Returns

`void`

---

## EventAppCheckForUpdatePayload

Ƭ **EventAppCheckForUpdatePayload**: `Object`

Type declaration

| Name             | Type      | Description                                  |
| :--------------- | :-------- | :------------------------------------------- |
| `hasUpdate`      | `boolean` | Indicates whether a new version is available |
| `latestVersion?` | `string`  | The version of the latest app.               |

## OnAppUpdateReadyCallback

Ƭ **OnAppUpdateReadyCallback**: (`payload`: `EventAppCheckForUpdatePayload`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type                            |
| :-------- | :------------------------------ |
| `payload` | `EventAppCheckForUpdatePayload` |

Returns

`void`

---

## OnAppUpdateFailedCallback

Ƭ **OnAppUpdateFailedCallback**: () => `void`

Type declaration

▸ (): `void`

Returns

`void`

---