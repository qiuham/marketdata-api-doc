---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/canvasToTempFilePath
api_type: Guide
updated_at: 2026-11-24 18:48:41.366009
---

# bn.canvasToTempFilePath

▸ **canvasToTempFilePath**(`options`, `compInst?`): `Promise`<`ToFilePathResult`\>

Parameters

| Name        | Type                          |
| :---------- | :---------------------------- |
| `options`   | `CanvasToTempFilePathOptions` |
| `compInst?` | `ComponentInstance`           |

Returns

`Promise`<`ToFilePathResult`\>

## CanvasToTempFilePathOptions

Ƭ **CanvasToTempFilePathOptions**: `Object`

Type declaration

| Name          | Type               | Description                                                                                                                     |
| :------------ | :----------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `x?`          | `number`           | The upper-left vertical position of the specified canvas area                                                                   |
| `y?`          | `number`           | The upper-left horizontal position of the specified canvas area                                                                 |
| `width?`      | `number`           | Width of the specified canvas area                                                                                              |
| `height?`     | `number`           | Height of the specified canvas area                                                                                             |
| `destWidth?`  | `number`           | Width of output picture                                                                                                         |
| `destHeight?` | `number`           | Height of output picture                                                                                                        |
| `canvasId?`   | `string`           | Canvas identity, passed in canvas Component canvas-id                                                                           |
| `canvas?`     | `Canvas`           | Canvas identity, passed in canvas Component instance. This property is used when the canvas type="2d".                          |
| `fileType?`   | `"png"` \| `"jpg"` | Type of destination file, valid values are 'png' or 'jpg'                                                                       |
| `quality?`    | `number`           | The quality of the picture is currently only jpg Effective. The range is (0, 1]. When not within the scope of 1.0 will be used. |

---

## Canvas

Ƭ **Canvas**: `Object`

Type declaration

| Name                    | Type                                                           |
| :---------------------- | :------------------------------------------------------------- |
| `width`                 | `number`                                                       |
| `height`                | `number`                                                       |
| `createImage`           | () => `Image`                                                  |
| `createImageData`       | () => `ImageData`                                              |
| `getContext`            | (`type`: `RenderingContextId`) => `null` \| `RenderingContext` |
| `requestAnimationFrame` | (`callback`: `FrameRequestCallback`) => `number`               |
| `cancelAnimationFrame`  | (`handle`: `number`) => `void`                                 |
| `style`                 | `any`                                                          |
| `toDataURL`             | () => `string`                                                 |
| `toTempFilePath`        | (`arg`: `any`) => `any`                                        |
| `toTempFilePathSync`    | (`arg`: `any`) => `any`                                        |

---

## Interface: Image

| Name    | Type               | Description                                      |
| :------ | :----------------- | :----------------------------------------------- |
| height  | `number`           | The real height of image                         |
| src     | `string`           | The url of image support base64 data             |
| width   | `number`           | The real width of image                          |
| onerror | (...`args`): `any` | Triggered when error occurs during loading image |
| onload  | (...`args`): `any` | Triggered when image finishes loading            |

### onerror

▸ **onerror**(...`args`): `any`

Triggered when error occurs during loading image

Parameters

| Name      | Type    |
| :-------- | :------ |
| `...args` | `any`[] |

Returns

`any`

---

### onload

▸ **onload**(...`args`): `any`

Triggered when image finishes loading

Parameters

| Name      | Type    |
| :-------- | :------ |
| `...args` | `any`[] |

Returns

`any`

## RenderingContextId

Ƭ **RenderingContextId**: `"2d"` \| `"bitmaprenderer"` \| `"webgl"` \| `"webgl2"`

## Interface: ComponentInstance

| Name | Type     | Description  |
| :--- | :------- | :----------- |
| id   | `string` | Component id |

## ToFilePathResult

Ƭ **ToFilePathResult**: `Object`

Type declaration

| Name           | Type     | Description                |
| :------------- | :------- | :------------------------- |
| `tempFilePath` | `string` | The path of the image file |

---

---

# bn.canvasToTempFilePath

▸ **canvasToTempFilePath**(`options`, `compInst?`): `Promise`<`ToFilePathResult`\>

Parameters

| Name        | Type                          |
| :---------- | :---------------------------- |
| `options`   | `CanvasToTempFilePathOptions` |
| `compInst?` | `ComponentInstance`           |

Returns

`Promise`<`ToFilePathResult`\>

## CanvasToTempFilePathOptions

Ƭ **CanvasToTempFilePathOptions**: `Object`

Type declaration

| Name          | Type               | Description                                                                                                                     |
| :------------ | :----------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `x?`          | `number`           | The upper-left vertical position of the specified canvas area                                                                   |
| `y?`          | `number`           | The upper-left horizontal position of the specified canvas area                                                                 |
| `width?`      | `number`           | Width of the specified canvas area                                                                                              |
| `height?`     | `number`           | Height of the specified canvas area                                                                                             |
| `destWidth?`  | `number`           | Width of output picture                                                                                                         |
| `destHeight?` | `number`           | Height of output picture                                                                                                        |
| `canvasId?`   | `string`           | Canvas identity, passed in canvas Component canvas-id                                                                           |
| `canvas?`     | `Canvas`           | Canvas identity, passed in canvas Component instance. This property is used when the canvas type="2d".                          |
| `fileType?`   | `"png"` \| `"jpg"` | Type of destination file, valid values are 'png' or 'jpg'                                                                       |
| `quality?`    | `number`           | The quality of the picture is currently only jpg Effective. The range is (0, 1]. When not within the scope of 1.0 will be used. |

---

## Canvas

Ƭ **Canvas**: `Object`

Type declaration

| Name                    | Type                                                           |
| :---------------------- | :------------------------------------------------------------- |
| `width`                 | `number`                                                       |
| `height`                | `number`                                                       |
| `createImage`           | () => `Image`                                                  |
| `createImageData`       | () => `ImageData`                                              |
| `getContext`            | (`type`: `RenderingContextId`) => `null` \| `RenderingContext` |
| `requestAnimationFrame` | (`callback`: `FrameRequestCallback`) => `number`               |
| `cancelAnimationFrame`  | (`handle`: `number`) => `void`                                 |
| `style`                 | `any`                                                          |
| `toDataURL`             | () => `string`                                                 |
| `toTempFilePath`        | (`arg`: `any`) => `any`                                        |
| `toTempFilePathSync`    | (`arg`: `any`) => `any`                                        |

---

## Interface: Image

| Name    | Type               | Description                                      |
| :------ | :----------------- | :----------------------------------------------- |
| height  | `number`           | The real height of image                         |
| src     | `string`           | The url of image support base64 data             |
| width   | `number`           | The real width of image                          |
| onerror | (...`args`): `any` | Triggered when error occurs during loading image |
| onload  | (...`args`): `any` | Triggered when image finishes loading            |

### onerror

▸ **onerror**(...`args`): `any`

Triggered when error occurs during loading image

Parameters

| Name      | Type    |
| :-------- | :------ |
| `...args` | `any`[] |

Returns

`any`

---

### onload

▸ **onload**(...`args`): `any`

Triggered when image finishes loading

Parameters

| Name      | Type    |
| :-------- | :------ |
| `...args` | `any`[] |

Returns

`any`

## RenderingContextId

Ƭ **RenderingContextId**: `"2d"` \| `"bitmaprenderer"` \| `"webgl"` \| `"webgl2"`

## Interface: ComponentInstance

| Name | Type     | Description  |
| :--- | :------- | :----------- |
| id   | `string` | Component id |

## ToFilePathResult

Ƭ **ToFilePathResult**: `Object`

Type declaration

| Name           | Type     | Description                |
| :------------- | :------- | :------------------------- |
| `tempFilePath` | `string` | The path of the image file |

---