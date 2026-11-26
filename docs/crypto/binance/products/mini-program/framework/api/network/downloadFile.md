---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/downloadFile
api_type: Guide
updated_at: 2026-11-26 18:45:57.437715
---

# bn.downloadFile

▸ **downloadFile**(`options`): `DownloadTask`

**`description`** Download file from url

**`example`**

```ts
bn.downloadFile({
  url: "https://example.com/audio/123", //example, not real path
  success(res) {
    // If only server responses, response data will be write into file and call success callback.
    // need to check whether the content is correct if you need.
    if (res.statusCode === 200) {
      console.log(res.tempFilePath);
    }
  },
});
```

Parameters

| Name      | Type                 | Description           |
| :-------- | :------------------- | :-------------------- |
| `options` | `DownloadFileOption` | download file options |

Returns

`DownloadTask`

DownloadTask - A task object that can be used to control and query the download

## Interface: DownloadFileOption

| Name      | Type                          | Description                                  |
| :-------- | :---------------------------- | :------------------------------------------- |
| url       | `string`                      | requested resource's url                     |
| header?   | `Record`<`string`, `string`\> | HTTP request header, cannot set referer here |
| timeout?  | `number`                      | timeout**`default`** 2000                    |
| filePath? | `string`                      | save path after file is downloaded           |
| success?  | (`result`): `void`            | success callback                             |
| fail?     | (`res`): `void`               | fail callback                                |
| complete? | (`res`): `void`               | complete callback                            |

### success

▸ `Optional` **success**(`result`): `void`

success callback

Parameters

| Name     | Type                            |
| :------- | :------------------------------ |
| `result` | `DownloadSuccessCallbackResult` |

Returns

`void`

---

### fail

▸ `Optional` **fail**(`res`): `void`

fail callback

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### complete

▸ `Optional` **complete**(`res`): `void`

complete callback

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

## Interface: DownloadSuccessCallbackResult

| Name          | Type     | Description                                                                         |
| :------------ | :------- | :---------------------------------------------------------------------------------- |
| filePath?     | `string` | File path. Same as filePath in parameter                                            |
| statusCode    | `number` | Server HTTP status code                                                             |
| tempFilePath? | `string` | Temp file path, if no filePath in parameter, file will be saved in a temp file path |
| errMsg        | `string` | Call result                                                                         |

## Interface: GeneralCallbackResult

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| errMsg | `string` |             |

## Interface: DownloadTask

| Name               | Type                  | Description                                                        |
| :----------------- | :-------------------- | :----------------------------------------------------------------- |
| abort              | (): `void`            | abort download task                                                |
| offHeadersReceived | (`callback?`): `void` | un-listen HTTP Response Header event                               |
| offProgressUpdate  | (`callback?`): `void` | un-listen download task progress update event                      |
| onHeadersReceived  | (`callback`): `void`  | listen HTTP Response Header event. Triggered before task completes |
| onProgressUpdate   | (`callback`): `void`  | listen download task progress update event                         |

### abort

▸ **abort**(): `void`

abort download task

Returns

`void`

---

### offHeadersReceived

▸ **offHeadersReceived**(`callback?`): `void`

un-listen HTTP Response Header event

Parameters

| Name        | Type                         |
| :---------- | :--------------------------- |
| `callback?` | `OffHeadersReceivedCallback` |

Returns

`void`

---

### offProgressUpdate

▸ **offProgressUpdate**(`callback?`): `void`

un-listen download task progress update event

Parameters

| Name        | Type                                    |
| :---------- | :-------------------------------------- |
| `callback?` | `DownloadTaskOffProgressUpdateCallback` |

Returns

`void`

---

### onHeadersReceived

▸ **onHeadersReceived**(`callback`): `void`

listen HTTP Response Header event. Triggered before task completes

Parameters

| Name       | Type                        |
| :--------- | :-------------------------- |
| `callback` | `OnHeadersReceivedCallback` |

Returns

`void`

---

### onProgressUpdate

▸ **onProgressUpdate**(`callback`): `void`

listen download task progress update event

Parameters

| Name       | Type                                   |
| :--------- | :------------------------------------- |
| `callback` | `DownloadTaskOnProgressUpdateCallback` |

Returns

`void`

## OffHeadersReceivedCallback

Ƭ **OffHeadersReceivedCallback**: (`result`: `OnHeadersReceivedCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnHeadersReceivedCallbackResult` |

Returns

`void`

---

## Interface: OnHeadersReceivedCallbackResult

| Name   | Type      | Description                             |
| :----- | :-------- | :-------------------------------------- |
| header | `Headers` | 开发者服务器返回的 HTTP Response Header |

## DownloadTaskOffProgressUpdateCallback

Ƭ **DownloadTaskOffProgressUpdateCallback**: (`result`:
`DownloadTaskOnProgressUpdateCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                         |
| :------- | :------------------------------------------- |
| `result` | `DownloadTaskOnProgressUpdateCallbackResult` |

Returns

`void`

---

## Interface: DownloadTaskOnProgressUpdateCallbackResult

| Name                      | Type     | Description                          |
| :------------------------ | :------- | :----------------------------------- |
| progress                  | `number` | 下载进度百分比                       |
| totalBytesExpectedToWrite | `number` | 预期需要下载的数据总长度，单位 Bytes |
| totalBytesWritten         | `number` | 已经上传的数据长度，单位 Bytes       |

## OnHeadersReceivedCallback

Ƭ **OnHeadersReceivedCallback**: (`result`: `OnHeadersReceivedCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnHeadersReceivedCallbackResult` |

Returns

`void`

---

## DownloadTaskOnProgressUpdateCallback

Ƭ **DownloadTaskOnProgressUpdateCallback**: (`result`: `DownloadTaskOnProgressUpdateCallbackResult`)
=> `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                         |
| :------- | :------------------------------------------- |
| `result` | `DownloadTaskOnProgressUpdateCallbackResult` |

Returns

`void`

---

---

# bn.downloadFile

▸ **downloadFile**(`options`): `DownloadTask`

**`description`** Download file from url

**`example`**

```ts
bn.downloadFile({
  url: "https://example.com/audio/123", //example, not real path
  success(res) {
    // If only server responses, response data will be write into file and call success callback.
    // need to check whether the content is correct if you need.
    if (res.statusCode === 200) {
      console.log(res.tempFilePath);
    }
  },
});
```

Parameters

| Name      | Type                 | Description           |
| :-------- | :------------------- | :-------------------- |
| `options` | `DownloadFileOption` | download file options |

Returns

`DownloadTask`

DownloadTask - A task object that can be used to control and query the download

## Interface: DownloadFileOption

| Name      | Type                          | Description                                  |
| :-------- | :---------------------------- | :------------------------------------------- |
| url       | `string`                      | requested resource's url                     |
| header?   | `Record`<`string`, `string`\> | HTTP request header, cannot set referer here |
| timeout?  | `number`                      | timeout**`default`** 2000                    |
| filePath? | `string`                      | save path after file is downloaded           |
| success?  | (`result`): `void`            | success callback                             |
| fail?     | (`res`): `void`               | fail callback                                |
| complete? | (`res`): `void`               | complete callback                            |

### success

▸ `Optional` **success**(`result`): `void`

success callback

Parameters

| Name     | Type                            |
| :------- | :------------------------------ |
| `result` | `DownloadSuccessCallbackResult` |

Returns

`void`

---

### fail

▸ `Optional` **fail**(`res`): `void`

fail callback

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### complete

▸ `Optional` **complete**(`res`): `void`

complete callback

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

## Interface: DownloadSuccessCallbackResult

| Name          | Type     | Description                                                                         |
| :------------ | :------- | :---------------------------------------------------------------------------------- |
| filePath?     | `string` | File path. Same as filePath in parameter                                            |
| statusCode    | `number` | Server HTTP status code                                                             |
| tempFilePath? | `string` | Temp file path, if no filePath in parameter, file will be saved in a temp file path |
| errMsg        | `string` | Call result                                                                         |

## Interface: GeneralCallbackResult

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| errMsg | `string` |             |

## Interface: DownloadTask

| Name               | Type                  | Description                                                        |
| :----------------- | :-------------------- | :----------------------------------------------------------------- |
| abort              | (): `void`            | abort download task                                                |
| offHeadersReceived | (`callback?`): `void` | un-listen HTTP Response Header event                               |
| offProgressUpdate  | (`callback?`): `void` | un-listen download task progress update event                      |
| onHeadersReceived  | (`callback`): `void`  | listen HTTP Response Header event. Triggered before task completes |
| onProgressUpdate   | (`callback`): `void`  | listen download task progress update event                         |

### abort

▸ **abort**(): `void`

abort download task

Returns

`void`

---

### offHeadersReceived

▸ **offHeadersReceived**(`callback?`): `void`

un-listen HTTP Response Header event

Parameters

| Name        | Type                         |
| :---------- | :--------------------------- |
| `callback?` | `OffHeadersReceivedCallback` |

Returns

`void`

---

### offProgressUpdate

▸ **offProgressUpdate**(`callback?`): `void`

un-listen download task progress update event

Parameters

| Name        | Type                                    |
| :---------- | :-------------------------------------- |
| `callback?` | `DownloadTaskOffProgressUpdateCallback` |

Returns

`void`

---

### onHeadersReceived

▸ **onHeadersReceived**(`callback`): `void`

listen HTTP Response Header event. Triggered before task completes

Parameters

| Name       | Type                        |
| :--------- | :-------------------------- |
| `callback` | `OnHeadersReceivedCallback` |

Returns

`void`

---

### onProgressUpdate

▸ **onProgressUpdate**(`callback`): `void`

listen download task progress update event

Parameters

| Name       | Type                                   |
| :--------- | :------------------------------------- |
| `callback` | `DownloadTaskOnProgressUpdateCallback` |

Returns

`void`

## OffHeadersReceivedCallback

Ƭ **OffHeadersReceivedCallback**: (`result`: `OnHeadersReceivedCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnHeadersReceivedCallbackResult` |

Returns

`void`

---

## Interface: OnHeadersReceivedCallbackResult

| Name   | Type      | Description                             |
| :----- | :-------- | :-------------------------------------- |
| header | `Headers` | 开发者服务器返回的 HTTP Response Header |

## DownloadTaskOffProgressUpdateCallback

Ƭ **DownloadTaskOffProgressUpdateCallback**: (`result`:
`DownloadTaskOnProgressUpdateCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                         |
| :------- | :------------------------------------------- |
| `result` | `DownloadTaskOnProgressUpdateCallbackResult` |

Returns

`void`

---

## Interface: DownloadTaskOnProgressUpdateCallbackResult

| Name                      | Type     | Description                          |
| :------------------------ | :------- | :----------------------------------- |
| progress                  | `number` | 下载进度百分比                       |
| totalBytesExpectedToWrite | `number` | 预期需要下载的数据总长度，单位 Bytes |
| totalBytesWritten         | `number` | 已经上传的数据长度，单位 Bytes       |

## OnHeadersReceivedCallback

Ƭ **OnHeadersReceivedCallback**: (`result`: `OnHeadersReceivedCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnHeadersReceivedCallbackResult` |

Returns

`void`

---

## DownloadTaskOnProgressUpdateCallback

Ƭ **DownloadTaskOnProgressUpdateCallback**: (`result`: `DownloadTaskOnProgressUpdateCallbackResult`)
=> `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                         |
| :------- | :------------------------------------------- |
| `result` | `DownloadTaskOnProgressUpdateCallbackResult` |

Returns

`void`

---