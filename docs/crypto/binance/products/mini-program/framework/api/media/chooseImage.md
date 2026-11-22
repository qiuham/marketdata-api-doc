---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/chooseImage
api_type: Guide
updated_at: 2026-11-22 18:43:05.472846
---

# bn.chooseImage

▸ **chooseImage**(`options`): `Promise`<`ChooseImageResponse`\>

**`description`** Selects an image from the local album or takes a photo with the camera.

**`example`**

```ts
const res = await bn.chooseImage({
  count: 9,
  sizeType: ["original"],
  sourceType: ["album"],
});
console.log(res.tempFilePaths, res.tempFiles);
```

Parameters

| Name      | Type                 |
| :-------- | :------------------- |
| `options` | `ChooseImageOptions` |

Returns

`Promise`<`ChooseImageResponse`\>

## Interface: ChooseImageOptions

| Name                  | Type                               | Description                                                                |
| :-------------------- | :--------------------------------- | :------------------------------------------------------------------------- |
| count?                | `number`                           | The maximum number of images allowed range is [1,9]                        |
| sizeType?             | (`"original"` \| `"compressed"`)[] | The size of the select image; valid options：- 'original';; - 'compressed' |
| sourceType?           | (`"album"` \| `"camera"`)[]        | The source of the image; valid options：- 'album'; - 'camera'              |
| compressionThreshold? | `number`                           | The max size of image, unit bit; JSSDK version >= 4.31.0                   |

## Interface: ChooseImageResponse

| Name          | Type          | Description                                      |
| :------------ | :------------ | :----------------------------------------------- |
| tempFilePaths | `string`[]    | The list of local temporary file paths to images |
| tempFiles     | `ImageFile`[] | The local temporary file list for images         |

---

# bn.chooseImage

▸ **chooseImage**(`options`): `Promise`<`ChooseImageResponse`\>

**`description`** Selects an image from the local album or takes a photo with the camera.

**`example`**

```ts
const res = await bn.chooseImage({
  count: 9,
  sizeType: ["original"],
  sourceType: ["album"],
});
console.log(res.tempFilePaths, res.tempFiles);
```

Parameters

| Name      | Type                 |
| :-------- | :------------------- |
| `options` | `ChooseImageOptions` |

Returns

`Promise`<`ChooseImageResponse`\>

## Interface: ChooseImageOptions

| Name                  | Type                               | Description                                                                |
| :-------------------- | :--------------------------------- | :------------------------------------------------------------------------- |
| count?                | `number`                           | The maximum number of images allowed range is [1,9]                        |
| sizeType?             | (`"original"` \| `"compressed"`)[] | The size of the select image; valid options：- 'original';; - 'compressed' |
| sourceType?           | (`"album"` \| `"camera"`)[]        | The source of the image; valid options：- 'album'; - 'camera'              |
| compressionThreshold? | `number`                           | The max size of image, unit bit; JSSDK version >= 4.31.0                   |

## Interface: ChooseImageResponse

| Name          | Type          | Description                                      |
| :------------ | :------------ | :----------------------------------------------- |
| tempFilePaths | `string`[]    | The list of local temporary file paths to images |
| tempFiles     | `ImageFile`[] | The local temporary file list for images         |