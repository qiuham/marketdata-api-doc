---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/chooseMedia
api_type: Guide
updated_at: 2026-11-19 18:48:08.351317
---

# bn.chooseMedia

▸ **chooseMedia**(`options`): `Promise`<`ChooseMediaResponse`\>

**`description`** Select images or videos from the local album or takes a photo or video with the
camera.

**`remark`** supported jssdk >= 4.8.0

**`example`**

```ts
const res = await bn.ChooseMedia({
  count: 9,
  mediaType: ["image"],
  sizeType: ["original"],
  sourceType: ["album", "camera"],
});
console.log(res.tempFiles);
```

Parameters

| Name      | Type                 |
| :-------- | :------------------- |
| `options` | `ChooseMediaOptions` |

Returns

`Promise`<`ChooseMediaResponse`\>

## Interface: ChooseMediaOptions

| Name          | Type                                  | Description                                                                                                                                                                                                                        |
| :------------ | :------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| count?        | `number`                              | The maximum number of images. For Android < 13, `count` cannot limit file numbers, `count` > 1 means multiple. Because of the native limits, users may select more files than expected, but the API will return only `count` files |
| sizeType      | (`"original"` \| `"compressed"`)[]    | Required. Use compressed file or original file, can choose only 1 of them for now. Compressed option not work for videos.; valid options：- 'original';; - 'compressed'                                                            |
| mediaType     | (`"video"` \| `"image"` \| `"mix"`)[] | Required. The selectable file type, can choose only 1 of them for now; valid options：- 'image'; - 'video'; - 'mix'                                                                                                                |
| sourceType?   | (`"album"` \| `"camera"`)[]           | The source of the image, default value is ['album', 'camera']; valid options：- 'album'; - 'camera'                                                                                                                                |
| camera?       | `"front"` \| `"back"`                 | Use back or front camera                                                                                                                                                                                                           |
| maxVideoSize? | `number`                              | Max video size in byte, require JSSDK version > 4.38.0                                                                                                                                                                             |
| maxImageSize? | `number`                              | Max image size in byte, require JSSDK version > 4.38.0                                                                                                                                                                             |

## Interface: ChooseMediaResponse

| Name      | Type              | Description                       |
| :-------- | :---------------- | :-------------------------------- |
| tempFiles | `MediaTempFile`[] | The list of local temporary files |

---

# bn.chooseMedia

▸ **chooseMedia**(`options`): `Promise`<`ChooseMediaResponse`\>

**`description`** Select images or videos from the local album or takes a photo or video with the
camera.

**`remark`** supported jssdk >= 4.8.0

**`example`**

```ts
const res = await bn.ChooseMedia({
  count: 9,
  mediaType: ["image"],
  sizeType: ["original"],
  sourceType: ["album", "camera"],
});
console.log(res.tempFiles);
```

Parameters

| Name      | Type                 |
| :-------- | :------------------- |
| `options` | `ChooseMediaOptions` |

Returns

`Promise`<`ChooseMediaResponse`\>

## Interface: ChooseMediaOptions

| Name          | Type                                  | Description                                                                                                                                                                                                                        |
| :------------ | :------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| count?        | `number`                              | The maximum number of images. For Android < 13, `count` cannot limit file numbers, `count` > 1 means multiple. Because of the native limits, users may select more files than expected, but the API will return only `count` files |
| sizeType      | (`"original"` \| `"compressed"`)[]    | Required. Use compressed file or original file, can choose only 1 of them for now. Compressed option not work for videos.; valid options：- 'original';; - 'compressed'                                                            |
| mediaType     | (`"video"` \| `"image"` \| `"mix"`)[] | Required. The selectable file type, can choose only 1 of them for now; valid options：- 'image'; - 'video'; - 'mix'                                                                                                                |
| sourceType?   | (`"album"` \| `"camera"`)[]           | The source of the image, default value is ['album', 'camera']; valid options：- 'album'; - 'camera'                                                                                                                                |
| camera?       | `"front"` \| `"back"`                 | Use back or front camera                                                                                                                                                                                                           |
| maxVideoSize? | `number`                              | Max video size in byte, require JSSDK version > 4.38.0                                                                                                                                                                             |
| maxImageSize? | `number`                              | Max image size in byte, require JSSDK version > 4.38.0                                                                                                                                                                             |

## Interface: ChooseMediaResponse

| Name      | Type              | Description                       |
| :-------- | :---------------- | :-------------------------------- |
| tempFiles | `MediaTempFile`[] | The list of local temporary files |