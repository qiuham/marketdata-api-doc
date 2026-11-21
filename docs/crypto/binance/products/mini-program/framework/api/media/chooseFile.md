---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/chooseFile
api_type: Guide
updated_at: 2026-11-21 18:45:28.943617
---

# bn.chooseFile

▸ **chooseFile**(`options`): `Promise`<`ChooseFileResponse`\>

**`description`** Select files from the file system.

**`remark`** supported jssdk >= 4.8.0

**`example`**

```ts
const res = await bn.chooseFile({
  count: 9,
  extension: ["pdf"],
});
console.log(res.tempFiles);
```

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `ChooseFileOptions` |

Returns

`Promise`<`ChooseFileResponse`\>

## Interface: ChooseFileOptions

| Name         | Type       | Description                                                                                                                                                              |
| :----------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| count        | `number`   | The maximum number of images allowed range is [1,9]. Because of the native limits, users may select more files than expected, but the API will return only `count` files |
| extension?   | `string`[] | Filter by filename extension. No filter by default                                                                                                                       |
| maxFileSize? | `number`   | Max file Size in byte, require JSSDK version > 4.38.0                                                                                                                    |

## Interface: ChooseFileResponse

| Name      | Type         | Description                              |
| :-------- | :----------- | :--------------------------------------- |
| tempFiles | `TempFile`[] | The local temporary file list for images |

---

# bn.chooseFile

▸ **chooseFile**(`options`): `Promise`<`ChooseFileResponse`\>

**`description`** Select files from the file system.

**`remark`** supported jssdk >= 4.8.0

**`example`**

```ts
const res = await bn.chooseFile({
  count: 9,
  extension: ["pdf"],
});
console.log(res.tempFiles);
```

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `ChooseFileOptions` |

Returns

`Promise`<`ChooseFileResponse`\>

## Interface: ChooseFileOptions

| Name         | Type       | Description                                                                                                                                                              |
| :----------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| count        | `number`   | The maximum number of images allowed range is [1,9]. Because of the native limits, users may select more files than expected, but the API will return only `count` files |
| extension?   | `string`[] | Filter by filename extension. No filter by default                                                                                                                       |
| maxFileSize? | `number`   | Max file Size in byte, require JSSDK version > 4.38.0                                                                                                                    |

## Interface: ChooseFileResponse

| Name      | Type         | Description                              |
| :-------- | :----------- | :--------------------------------------- |
| tempFiles | `TempFile`[] | The local temporary file list for images |