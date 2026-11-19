---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/uploadFile
api_type: Guide
updated_at: 2026-11-19 18:47:23.670624
---

# bn.uploadFile

▸ **uploadFile**(`options`): `UploadTask`

**`description`** Uploads local resources to the server. The client initiates a HTTPS POST Request,
wherein content-type for multipart/form-data.

**`example`**

```ts
bn.chooseImage({
  success(res) {
    const tempFilePaths = res.tempFilePaths;
    bn.uploadFile({
      url: "https://example/upload", //Example only, not real interface address
      filePath: tempFilePaths[0],
      name: "file",
      formData: {
        user: "test",
      },
      success(res) {
        const data = res.data;
        //of the something
      },
    });
  },
});
```

Parameters

| Name      | Type               |
| :-------- | :----------------- |
| `options` | `UploadFileOption` |

Returns

`UploadTask`

UploadTask

## Interface: UploadFileOption

| Name      | Type                          | Description                                                                                                                 |
| :-------- | :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| url       | `string`                      | Developer server address                                                                                                    |
| filePath  | `string`                      | Path to upload file resource (local path)                                                                                   |
| name      | `string`                      | The key corresponding to the file, the developer can get the binary content of the file through this key on the server side |
| header?   | `Headers`                     | Header of HTTP request, Referer cannot be set in Header                                                                     |
| formData? | `Record`<`string`, `string`\> | Other additional form data in the HTTP request                                                                              |
| timeout?  | `number`                      | Timeout time.default 2000                                                                                                   |
| method?   | `"POST"` \| `"PUT"`           | **`remark`** sdk > 4.9.0; Method used when upload file, support 'POST' or 'PUT'.                                            |
| complete? | `UploadFileCompleteCallback`  | The callback function for the end of the interface call (it will be executed when the call succeeds or fails)               |
| fail?     | `UploadFileFailCallback`      | The callback function of interface call failure                                                                             |
| success?  | `UploadFileSuccessCallback`   | Callback function for successful interface call                                                                             |

## Interface: UploadTask

| Name               | Type                  | Description                                                                                 |
| :----------------- | :-------------------- | :------------------------------------------------------------------------------------------ |
| abort              | (): `void`            | Interrupt upload task                                                                       |
| offHeadersReceived | (`callback?`): `void` | Cancel listening to the HTTP Response Header event                                          |
| offProgressUpdate  | (`callback?`): `void` | Cancel listening to upload progress change events                                           |
| onHeadersReceived  | (`callback`): `void`  | Listen to the HTTP Response Header event. Will be earlier than the request completion event |
| onProgressUpdate   | (`callback`): `void`  | Listen to upload progress change events                                                     |

### abort

▸ **abort**(): `void`

Interrupt upload task

Returns

`void`

---

### offHeadersReceived

▸ **offHeadersReceived**(`callback?`): `void`

Cancel listening to the HTTP Response Header event

Parameters

| Name        | Type                         |
| :---------- | :--------------------------- |
| `callback?` | `OffHeadersReceivedCallback` |

Returns

`void`

---

### offProgressUpdate

▸ **offProgressUpdate**(`callback?`): `void`

Cancel listening to upload progress change events

Parameters

| Name        | Type                                  |
| :---------- | :------------------------------------ |
| `callback?` | `UploadTaskOffProgressUpdateCallback` |

Returns

`void`

---

### onHeadersReceived

▸ **onHeadersReceived**(`callback`): `void`

Listen to the HTTP Response Header event. Will be earlier than the request completion event

Parameters

| Name       | Type                        |
| :--------- | :-------------------------- |
| `callback` | `OnHeadersReceivedCallback` |

Returns

`void`

---

### onProgressUpdate

▸ **onProgressUpdate**(`callback`): `void`

Listen to upload progress change events

Parameters

| Name       | Type                                 |
| :--------- | :----------------------------------- |
| `callback` | `UploadTaskOnProgressUpdateCallback` |

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

| Name   | Type      | Description                                           |
| :----- | :-------- | :---------------------------------------------------- |
| header | `Headers` | HTTP Response Header returned by the developer server |

## UploadTaskOffProgressUpdateCallback

Ƭ **UploadTaskOffProgressUpdateCallback**: (`result`: `UploadTaskOnProgressUpdateCallbackResult`) =>
`void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                       |
| :------- | :----------------------------------------- |
| `result` | `UploadTaskOnProgressUpdateCallbackResult` |

Returns

`void`

---

## Interface: UploadTaskOnProgressUpdateCallbackResult

| Name                     | Type     | Description                                            |
| :----------------------- | :------- | :----------------------------------------------------- |
| progress                 | `number` | Upload progress percentage                             |
| totalBytesExpectedToSend | `number` | Expected total length of data to be uploaded, in Bytes |
| totalBytesSent           | `number` | The length of the uploaded data, in Bytes              |

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

## UploadTaskOnProgressUpdateCallback

Ƭ **UploadTaskOnProgressUpdateCallback**: (`result`: `UploadTaskOnProgressUpdateCallbackResult`) =>
`void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                       |
| :------- | :----------------------------------------- |
| `result` | `UploadTaskOnProgressUpdateCallbackResult` |

Returns

`void`

---

# bn.uploadFile

▸ **uploadFile**(`options`): `UploadTask`

**`description`** Uploads local resources to the server. The client initiates a HTTPS POST Request,
wherein content-type for multipart/form-data.

**`example`**

```ts
bn.chooseImage({
  success(res) {
    const tempFilePaths = res.tempFilePaths;
    bn.uploadFile({
      url: "https://example/upload", //Example only, not real interface address
      filePath: tempFilePaths[0],
      name: "file",
      formData: {
        user: "test",
      },
      success(res) {
        const data = res.data;
        //of the something
      },
    });
  },
});
```

Parameters

| Name      | Type               |
| :-------- | :----------------- |
| `options` | `UploadFileOption` |

Returns

`UploadTask`

UploadTask

## Interface: UploadFileOption

| Name      | Type                          | Description                                                                                                                 |
| :-------- | :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| url       | `string`                      | Developer server address                                                                                                    |
| filePath  | `string`                      | Path to upload file resource (local path)                                                                                   |
| name      | `string`                      | The key corresponding to the file, the developer can get the binary content of the file through this key on the server side |
| header?   | `Headers`                     | Header of HTTP request, Referer cannot be set in Header                                                                     |
| formData? | `Record`<`string`, `string`\> | Other additional form data in the HTTP request                                                                              |
| timeout?  | `number`                      | Timeout time.default 2000                                                                                                   |
| method?   | `"POST"` \| `"PUT"`           | **`remark`** sdk > 4.9.0; Method used when upload file, support 'POST' or 'PUT'.                                            |
| complete? | `UploadFileCompleteCallback`  | The callback function for the end of the interface call (it will be executed when the call succeeds or fails)               |
| fail?     | `UploadFileFailCallback`      | The callback function of interface call failure                                                                             |
| success?  | `UploadFileSuccessCallback`   | Callback function for successful interface call                                                                             |

## Interface: UploadTask

| Name               | Type                  | Description                                                                                 |
| :----------------- | :-------------------- | :------------------------------------------------------------------------------------------ |
| abort              | (): `void`            | Interrupt upload task                                                                       |
| offHeadersReceived | (`callback?`): `void` | Cancel listening to the HTTP Response Header event                                          |
| offProgressUpdate  | (`callback?`): `void` | Cancel listening to upload progress change events                                           |
| onHeadersReceived  | (`callback`): `void`  | Listen to the HTTP Response Header event. Will be earlier than the request completion event |
| onProgressUpdate   | (`callback`): `void`  | Listen to upload progress change events                                                     |

### abort

▸ **abort**(): `void`

Interrupt upload task

Returns

`void`

---

### offHeadersReceived

▸ **offHeadersReceived**(`callback?`): `void`

Cancel listening to the HTTP Response Header event

Parameters

| Name        | Type                         |
| :---------- | :--------------------------- |
| `callback?` | `OffHeadersReceivedCallback` |

Returns

`void`

---

### offProgressUpdate

▸ **offProgressUpdate**(`callback?`): `void`

Cancel listening to upload progress change events

Parameters

| Name        | Type                                  |
| :---------- | :------------------------------------ |
| `callback?` | `UploadTaskOffProgressUpdateCallback` |

Returns

`void`

---

### onHeadersReceived

▸ **onHeadersReceived**(`callback`): `void`

Listen to the HTTP Response Header event. Will be earlier than the request completion event

Parameters

| Name       | Type                        |
| :--------- | :-------------------------- |
| `callback` | `OnHeadersReceivedCallback` |

Returns

`void`

---

### onProgressUpdate

▸ **onProgressUpdate**(`callback`): `void`

Listen to upload progress change events

Parameters

| Name       | Type                                 |
| :--------- | :----------------------------------- |
| `callback` | `UploadTaskOnProgressUpdateCallback` |

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

| Name   | Type      | Description                                           |
| :----- | :-------- | :---------------------------------------------------- |
| header | `Headers` | HTTP Response Header returned by the developer server |

## UploadTaskOffProgressUpdateCallback

Ƭ **UploadTaskOffProgressUpdateCallback**: (`result`: `UploadTaskOnProgressUpdateCallbackResult`) =>
`void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                       |
| :------- | :----------------------------------------- |
| `result` | `UploadTaskOnProgressUpdateCallbackResult` |

Returns

`void`

---

## Interface: UploadTaskOnProgressUpdateCallbackResult

| Name                     | Type     | Description                                            |
| :----------------------- | :------- | :----------------------------------------------------- |
| progress                 | `number` | Upload progress percentage                             |
| totalBytesExpectedToSend | `number` | Expected total length of data to be uploaded, in Bytes |
| totalBytesSent           | `number` | The length of the uploaded data, in Bytes              |

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

## UploadTaskOnProgressUpdateCallback

Ƭ **UploadTaskOnProgressUpdateCallback**: (`result`: `UploadTaskOnProgressUpdateCallbackResult`) =>
`void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                       |
| :------- | :----------------------------------------- |
| `result` | `UploadTaskOnProgressUpdateCallbackResult` |

Returns

`void`