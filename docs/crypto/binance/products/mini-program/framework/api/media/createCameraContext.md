---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/createCameraContext
api_type: Guide
updated_at: 2026-11-23 18:46:04.811284
---

# bn.createCameraContext

▸ **createCameraContext**(`options?`): `CameraContext`

**`description`** return a CameraContext instance for the current page

**`remark`** supported jssdk >= 4.11.0

**`example`**

```js
const cameraContext = bn.createCameraContext();
cameraContext.takePhoto({}).then((res) => {
  console.log(res);
});
```

Parameters

| Name                  | Type     |
| :-------------------- | :------- |
| `options?`            | `Object` |
| `options.rendererId?` | `number` |

Returns

`CameraContext`

## Interface: CameraContext

| Name        | Type                                                 | Description                                          |
| :---------- | :--------------------------------------------------- | :--------------------------------------------------- |
| takePhoto   | (`options`): `Promise`<`TakePhotoCallbackResult`\>   | take a photo, return the temp file path of the photo |
| startRecord | (`options`): `Promise`<`StartRecordCallbackResult`\> | start record video                                   |
| stopRecord  | (`options`): `Promise`<`StopRecordCallbackResult`\>  | stop record video                                    |
| setZoom     | (`options`): `Promise`<`SetZoomCallbackResult`\>     | set zoom of camera                                   |

### takePhoto

▸ **takePhoto**(`options`): `Promise`<`TakePhotoCallbackResult`\>

take a photo, return the temp file path of the photo

Parameters

| Name      | Type               |
| :-------- | :----------------- |
| `options` | `TakePhotoOptions` |

Returns

`Promise`<`TakePhotoCallbackResult`\>

---

### startRecord

▸ **startRecord**(`options`): `Promise`<`StartRecordCallbackResult`\>

start record video

Parameters

| Name      | Type                 |
| :-------- | :------------------- |
| `options` | `StartRecordOptions` |

Returns

`Promise`<`StartRecordCallbackResult`\>

---

### stopRecord

▸ **stopRecord**(`options`): `Promise`<`StopRecordCallbackResult`\>

stop record video

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `StopRecordOptions` |

Returns

`Promise`<`StopRecordCallbackResult`\>

---

### setZoom

▸ **setZoom**(`options`): `Promise`<`SetZoomCallbackResult`\>

set zoom of camera

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `SetZoomOptions` |

Returns

`Promise`<`SetZoomCallbackResult`\>

## Interface: TakePhotoCallbackResult

| Name          | Type     | Description     |
| :------------ | :------- | :-------------- |
| tempImagePath | `string` | image file path |
| errMsg?       | `string` |                 |

## Interface: TakePhotoOptions

| Name          | Type                              | Description                                                                              |
| :------------ | :-------------------------------- | :--------------------------------------------------------------------------------------- |
| quality?      | `"normal"` \| `"high"` \| `"low"` | photo quality, default normal                                                            |
| selfieMirror? | `boolean`                         | is selfie mirror, default true, only work for front camera. Android is not supported yet |
| onSuccess?    | (`res`): `void`                   | callback when success                                                                    |
| onFail?       | (`err`): `void`                   | callback when fail                                                                       |
| onComplete?   | (`res`): `void`                   | callback when complete (success or fail)                                                 |

### onSuccess

▸ `Optional` **onSuccess**(`res`): `void`

callback when success

Parameters

| Name  | Type                      |
| :---- | :------------------------ |
| `res` | `TakePhotoCallbackResult` |

Returns

`void`

---

### onFail

▸ `Optional` **onFail**(`err`): `void`

callback when fail

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `err` | `OnErrorCallbackResult` |

Returns

`void`

---

### onComplete

▸ `Optional` **onComplete**(`res`): `void`

callback when complete (success or fail)

Parameters

| Name  | Type                                                 |
| :---- | :--------------------------------------------------- |
| `res` | `TakePhotoCallbackResult` \| `OnErrorCallbackResult` |

Returns

`void`

## Interface: OnErrorCallbackResult

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| errno  | `number` |             |
| errMsg | `string` |             |

## Interface: StartRecordCallbackResult

| Name | Type | Description |
| :--- | :--- | :---------- |

## Interface: StartRecordOptions

| Name             | Type                    | Description                                                                              |
| :--------------- | :---------------------- | :--------------------------------------------------------------------------------------- |
| timeout?         | `number`                | largest record time in seconds, default 30s                                              |
| selfieMirror?    | `boolean`               | is selfie mirror, default true, only work for front camera. Android is not supported yet |
| timeoutCallback? | `RecordTimeoutCallback` | record timeout callback                                                                  |
| onSuccess?       | (`res`): `void`         | callback when success                                                                    |
| onFail?          | (`err`): `void`         | callback when fail                                                                       |
| onComplete?      | (`res`): `void`         | callback when complete (success or fail)                                                 |

### onSuccess

▸ `Optional` **onSuccess**(`res`): `void`

callback when success

Parameters

| Name  | Type                        |
| :---- | :-------------------------- |
| `res` | `StartRecordCallbackResult` |

Returns

`void`

---

### onFail

▸ `Optional` **onFail**(`err`): `void`

callback when fail

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `err` | `OnErrorCallbackResult` |

Returns

`void`

---

### onComplete

▸ `Optional` **onComplete**(`res`): `void`

callback when complete (success or fail)

Parameters

| Name  | Type                                                   |
| :---- | :----------------------------------------------------- |
| `res` | `StartRecordCallbackResult` \| `OnErrorCallbackResult` |

Returns

`void`

## Interface: StopRecordCallbackResult

| Name          | Type     | Description         |
| :------------ | :------- | :------------------ |
| tempThumbPath | `string` | thumbnail file path |
| tempVideoPath | `string` | video file path     |
| errMsg?       | `string` |                     |

## Interface: StopRecordOptions

| Name | Type | Description |
| :--- | :--- | :---------- |

## Interface: SetZoomCallbackResult

| Name    | Type     | Description  |
| :------ | :------- | :----------- |
| zoom    | `number` | zoomed value |
| errMsg? | `string` |              |

## Interface: SetZoomOptions

| Name        | Type            | Description                              |
| :---------- | :-------------- | :--------------------------------------- |
| zoom        | `number`        | zoom value, range 1 ~ maxZoom            |
| onSuccess?  | (`res`): `void` | callback when success                    |
| onFail?     | (`err`): `void` | callback when fail                       |
| onComplete? | (`res`): `void` | callback when complete (success or fail) |

### onSuccess

▸ `Optional` **onSuccess**(`res`): `void`

callback when success

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `SetZoomCallbackResult` |

Returns

`void`

---

### onFail

▸ `Optional` **onFail**(`err`): `void`

callback when fail

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `err` | `OnErrorCallbackResult` |

Returns

`void`

---

### onComplete

▸ `Optional` **onComplete**(`res`): `void`

callback when complete (success or fail)

Parameters

| Name  | Type                                               |
| :---- | :------------------------------------------------- |
| `res` | `SetZoomCallbackResult` \| `OnErrorCallbackResult` |

Returns

`void`

---

# bn.createCameraContext

▸ **createCameraContext**(`options?`): `CameraContext`

**`description`** return a CameraContext instance for the current page

**`remark`** supported jssdk >= 4.11.0

**`example`**

```js
const cameraContext = bn.createCameraContext();
cameraContext.takePhoto({}).then((res) => {
  console.log(res);
});
```

Parameters

| Name                  | Type     |
| :-------------------- | :------- |
| `options?`            | `Object` |
| `options.rendererId?` | `number` |

Returns

`CameraContext`

## Interface: CameraContext

| Name        | Type                                                 | Description                                          |
| :---------- | :--------------------------------------------------- | :--------------------------------------------------- |
| takePhoto   | (`options`): `Promise`<`TakePhotoCallbackResult`\>   | take a photo, return the temp file path of the photo |
| startRecord | (`options`): `Promise`<`StartRecordCallbackResult`\> | start record video                                   |
| stopRecord  | (`options`): `Promise`<`StopRecordCallbackResult`\>  | stop record video                                    |
| setZoom     | (`options`): `Promise`<`SetZoomCallbackResult`\>     | set zoom of camera                                   |

### takePhoto

▸ **takePhoto**(`options`): `Promise`<`TakePhotoCallbackResult`\>

take a photo, return the temp file path of the photo

Parameters

| Name      | Type               |
| :-------- | :----------------- |
| `options` | `TakePhotoOptions` |

Returns

`Promise`<`TakePhotoCallbackResult`\>

---

### startRecord

▸ **startRecord**(`options`): `Promise`<`StartRecordCallbackResult`\>

start record video

Parameters

| Name      | Type                 |
| :-------- | :------------------- |
| `options` | `StartRecordOptions` |

Returns

`Promise`<`StartRecordCallbackResult`\>

---

### stopRecord

▸ **stopRecord**(`options`): `Promise`<`StopRecordCallbackResult`\>

stop record video

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `StopRecordOptions` |

Returns

`Promise`<`StopRecordCallbackResult`\>

---

### setZoom

▸ **setZoom**(`options`): `Promise`<`SetZoomCallbackResult`\>

set zoom of camera

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `SetZoomOptions` |

Returns

`Promise`<`SetZoomCallbackResult`\>

## Interface: TakePhotoCallbackResult

| Name          | Type     | Description     |
| :------------ | :------- | :-------------- |
| tempImagePath | `string` | image file path |
| errMsg?       | `string` |                 |

## Interface: TakePhotoOptions

| Name          | Type                              | Description                                                                              |
| :------------ | :-------------------------------- | :--------------------------------------------------------------------------------------- |
| quality?      | `"normal"` \| `"high"` \| `"low"` | photo quality, default normal                                                            |
| selfieMirror? | `boolean`                         | is selfie mirror, default true, only work for front camera. Android is not supported yet |
| onSuccess?    | (`res`): `void`                   | callback when success                                                                    |
| onFail?       | (`err`): `void`                   | callback when fail                                                                       |
| onComplete?   | (`res`): `void`                   | callback when complete (success or fail)                                                 |

### onSuccess

▸ `Optional` **onSuccess**(`res`): `void`

callback when success

Parameters

| Name  | Type                      |
| :---- | :------------------------ |
| `res` | `TakePhotoCallbackResult` |

Returns

`void`

---

### onFail

▸ `Optional` **onFail**(`err`): `void`

callback when fail

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `err` | `OnErrorCallbackResult` |

Returns

`void`

---

### onComplete

▸ `Optional` **onComplete**(`res`): `void`

callback when complete (success or fail)

Parameters

| Name  | Type                                                 |
| :---- | :--------------------------------------------------- |
| `res` | `TakePhotoCallbackResult` \| `OnErrorCallbackResult` |

Returns

`void`

## Interface: OnErrorCallbackResult

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| errno  | `number` |             |
| errMsg | `string` |             |

## Interface: StartRecordCallbackResult

| Name | Type | Description |
| :--- | :--- | :---------- |

## Interface: StartRecordOptions

| Name             | Type                    | Description                                                                              |
| :--------------- | :---------------------- | :--------------------------------------------------------------------------------------- |
| timeout?         | `number`                | largest record time in seconds, default 30s                                              |
| selfieMirror?    | `boolean`               | is selfie mirror, default true, only work for front camera. Android is not supported yet |
| timeoutCallback? | `RecordTimeoutCallback` | record timeout callback                                                                  |
| onSuccess?       | (`res`): `void`         | callback when success                                                                    |
| onFail?          | (`err`): `void`         | callback when fail                                                                       |
| onComplete?      | (`res`): `void`         | callback when complete (success or fail)                                                 |

### onSuccess

▸ `Optional` **onSuccess**(`res`): `void`

callback when success

Parameters

| Name  | Type                        |
| :---- | :-------------------------- |
| `res` | `StartRecordCallbackResult` |

Returns

`void`

---

### onFail

▸ `Optional` **onFail**(`err`): `void`

callback when fail

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `err` | `OnErrorCallbackResult` |

Returns

`void`

---

### onComplete

▸ `Optional` **onComplete**(`res`): `void`

callback when complete (success or fail)

Parameters

| Name  | Type                                                   |
| :---- | :----------------------------------------------------- |
| `res` | `StartRecordCallbackResult` \| `OnErrorCallbackResult` |

Returns

`void`

## Interface: StopRecordCallbackResult

| Name          | Type     | Description         |
| :------------ | :------- | :------------------ |
| tempThumbPath | `string` | thumbnail file path |
| tempVideoPath | `string` | video file path     |
| errMsg?       | `string` |                     |

## Interface: StopRecordOptions

| Name | Type | Description |
| :--- | :--- | :---------- |

## Interface: SetZoomCallbackResult

| Name    | Type     | Description  |
| :------ | :------- | :----------- |
| zoom    | `number` | zoomed value |
| errMsg? | `string` |              |

## Interface: SetZoomOptions

| Name        | Type            | Description                              |
| :---------- | :-------------- | :--------------------------------------- |
| zoom        | `number`        | zoom value, range 1 ~ maxZoom            |
| onSuccess?  | (`res`): `void` | callback when success                    |
| onFail?     | (`err`): `void` | callback when fail                       |
| onComplete? | (`res`): `void` | callback when complete (success or fail) |

### onSuccess

▸ `Optional` **onSuccess**(`res`): `void`

callback when success

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `SetZoomCallbackResult` |

Returns

`void`

---

### onFail

▸ `Optional` **onFail**(`err`): `void`

callback when fail

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `err` | `OnErrorCallbackResult` |

Returns

`void`

---

### onComplete

▸ `Optional` **onComplete**(`res`): `void`

callback when complete (success or fail)

Parameters

| Name  | Type                                               |
| :---- | :------------------------------------------------- |
| `res` | `SetZoomCallbackResult` \| `OnErrorCallbackResult` |

Returns

`void`