---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/createWebview
api_type: Guide
updated_at: 2026-11-21 18:46:35.023245
---

# bn.createWebview

▸ **createWebview**(`options`): `Webview`

**`remark`** supported jssdk > 3.13.0

**`description`** Create a webview displayed above mini game. Only one webview is supported at the
same time

**`example`**

```ts
const webview = bn.createWebview({
 // required, resource url, support local file path
 src: '/root/src/index.html',
 // position
 x: 0,
 y: 0,
 // size
 height: 500,
 width: 500,
 // background color in #rrggbbaa format
 backgroundColor: '#FFFFFFFF'
 success (res) {}
}
})
// update webview properties
webview.update({
  x: 100,
  y: 100,
})
// close webview
webview.close()

// send message to webview
webview.postMessage('test')

// listen event on webview
webview.onLoad(() => {})

```

Parameters

| Name      | Type                   | Description            |
| :-------- | :--------------------- | :--------------------- |
| `options` | `CreateWebviewOptions` | create webview options |

Returns

`Webview`

Webview - the webview instance

## CreateWebviewOptions

Ƭ **CreateWebviewOptions**: `Object`

Type declaration

| Name                        | Type                                                   | Description                                                                                                                                                                                            |
| :-------------------------- | :----------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`                       | `string`                                               | Src of webview page supports http:// https:// or local file path                                                                                                                                       |
| `height?`                   | `number`                                               | Height of webview component                                                                                                                                                                            |
| `width?`                    | `number`                                               | Width of webview component                                                                                                                                                                             |
| `x?`                        | `number`                                               | Horizontal position of webview                                                                                                                                                                         |
| `y?`                        | `number`                                               | Vertical position of webview                                                                                                                                                                           |
| `backgroundColor?`          | `string`                                               | 8 digit hex value #ffffffff                                                                                                                                                                            |
| `injected?`                 | `string`[]                                             | Inject specific javascript script file before page loaded                                                                                                                                              |
| `bounce?`                   | `boolean`                                              | whether the page bounces when scroll beyond top/bottom                                                                                                                                                 |
| `loadingBar?`               | `boolean`                                              | whether the page shows loading bar when loading page                                                                                                                                                   |
| `webPreferences?`           | { `[key: string]`: `unknown`; `userAgent?`: `string` } | Setting web preferences, currently only `userAgent` is supported                                                                                                                                       |
| `webPreferences.userAgent?` | `string`                                               | -                                                                                                                                                                                                      |
| `pageId?`                   | `number`                                               | Page id, used to identify the page to show webview. Required in widget. **`example`** `ts   const pageId = getCurrentInstance().page.getPageId();   createWebview({     ...options,     pageId,   }) ` |
| `success?`                  | `CreateWebviewSuccessCallback`                         | -                                                                                                                                                                                                      |
| `fail?`                     | `CreateWebviewCallback`                                | -                                                                                                                                                                                                      |
| `complete?`                 | `CreateWebviewCallback`                                | -                                                                                                                                                                                                      |

---

## CreateWebviewSuccessCallback

Ƭ **CreateWebviewSuccessCallback**: (`{   errMsg,   webview, }`: { `errMsg`: `string` ; `webview`:
`IWebview` }) => `void`

Type declaration

▸ (`{   errMsg,   webview, }`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `{         |            |
| errMsg,    |            |
| webview,   |            |
| }`         | `Object`   |
| `{         |            |
| errMsg,    |            |
| webview,   |            |
| }.errMsg`  | `string`   |
| `{         |            |
| errMsg,    |            |
| webview,   |            |
| }.webview` | `IWebview` |

Returns

`void`

---

## Interface: IWebview

| Name              | Type                                                  | Description |
| :---------------- | :---------------------------------------------------- | :---------- |
| src               | `string`                                              |             |
| x                 | `number`                                              |             |
| y                 | `number`                                              |             |
| backgroundColor   | `string`                                              |             |
| update            | (`options`): `void`                                   |             |
| close             | (): `void`                                            |             |
| postMessage       | (`message`): `void`                                   |             |
| canGoBack         | (): `Promise`<`boolean`\>                             |             |
| canGoForward      | (): `Promise`<`boolean`\>                             |             |
| url               | (): `Promise`<`string`\>                              |             |
| title             | (): `Promise`<`string`\>                              |             |
| goBack            | (): `Promise`<`void`\>                                |             |
| goForward         | (): `Promise`<`void`\>                                |             |
| refresh           | (): `Promise`<`void`\>                                |             |
| clearCache        | (): `Promise`<`void`\>                                |             |
| invoke            | (`method`, `payload?`, `options?`): `Promise`<`any`\> |             |
| clearScrollStatus | (): `Promise`<`void`\>                                |             |
| onMessage         | (`handler`): `void`                                   |             |
| offMessage        | (`handler`): `void`                                   |             |
| onLoad            | (`handler`): `void`                                   |             |
| offLoad           | (`handler`): `void`                                   |             |
| onError           | (`handler`): `void`                                   |             |
| offError          | (`handler`): `void`                                   |             |

### update

▸ **update**(`options`): `void`

Parameters

| Name      | Type                                |
| :-------- | :---------------------------------- |
| `options` | `Optional`<`CreateWebviewOptions`\> |

Returns

`void`

---

### close

▸ **close**(): `void`

Returns

`void`

---

### postMessage

▸ **postMessage**(`message`): `void`

Parameters

| Name      | Type     |
| :-------- | :------- |
| `message` | `string` |

Returns

`void`

---

### canGoBack

▸ **canGoBack**(): `Promise`<`boolean`\>

Returns

`Promise`<`boolean`\>

---

### canGoForward

▸ **canGoForward**(): `Promise`<`boolean`\>

Returns

`Promise`<`boolean`\>

---

### url

▸ **url**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

### title

▸ **title**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

### goBack

▸ **goBack**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### goForward

▸ **goForward**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### refresh

▸ **refresh**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### clearCache

▸ **clearCache**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### invoke

▸ **invoke**(`method`, `payload?`, `options?`): `Promise`<`any`\>

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `method`   | `string`                   |
| `payload?` | `Record`<`string`, `any`\> |
| `options?` | `Record`<`string`, `any`\> |

Returns

`Promise`<`any`\>

---

### clearScrollStatus

▸ **clearScrollStatus**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### onMessage

▸ **onMessage**(`handler`): `void`

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `handler` | `Handler`<`MessageEvent`\> |

Returns

`void`

---

### offMessage

▸ **offMessage**(`handler`): `void`

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `handler` | `Handler`<`MessageEvent`\> |

Returns

`void`

---

### onLoad

▸ **onLoad**(`handler`): `void`

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `handler` | `Handler`<`LoadEvent`\> |

Returns

`void`

---

### offLoad

▸ **offLoad**(`handler`): `void`

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `handler` | `Handler`<`LoadEvent`\> |

Returns

`void`

---

### onError

▸ **onError**(`handler`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `handler` | `Handler`<`ErrorEvent`\> |

Returns

`void`

---

### offError

▸ **offError**(`handler`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `handler` | `Handler`<`ErrorEvent`\> |

Returns

`void`

## Optional

Ƭ **Optional**<`T`\>: `Object`

Type parameters

| Name |
| :--- |
| `T`  |

---

## Handler

Ƭ **Handler**<`T`\>: (`ev`: `T`) => `void`

Type parameters

| Name |
| :--- |
| `T`  |

Type declaration

▸ (`ev`): `void`

Parameters

| Name | Type |
| :--- | :--- |
| `ev` | `T`  |

Returns

`void`

---

## Interface: MessageEvent

| Name | Type  | Description |
| :--- | :---- | :---------- |
| data | `any` |             |

## Interface: LoadEvent

| Name | Type     | Description |
| :--- | :------- | :---------- |
| src  | `string` |             |

## Interface: ErrorEvent

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| src    | `string` |             |
| error? | `string` |             |

## CreateWebviewCallback

Ƭ **CreateWebviewCallback**: (`{ errMsg }`: { `errMsg`: `string` }) => `void`

Type declaration

▸ (`{ errMsg }`): `void`

Parameters

| Name                | Type     |
| :------------------ | :------- |
| `{ errMsg }`        | `Object` |
| `{ errMsg }.errMsg` | `string` |

Returns

`void`

---

## Class: Webview

| Name              | Type                                                   | Description                                                                                                                                                      |
| :---------------- | :----------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_x               | `number`                                               |                                                                                                                                                                  |
| \_y               | `number`                                               |                                                                                                                                                                  |
| \_backgroundColor | `string`                                               |                                                                                                                                                                  |
| \_src             | `string`                                               |                                                                                                                                                                  |
| id                | `number`                                               |                                                                                                                                                                  |
| rpcNative         | `NativeRPC`                                            |                                                                                                                                                                  |
| rpcWebview        | `AppRPC`                                               |                                                                                                                                                                  |
| rendererId        | `number`                                               |                                                                                                                                                                  |
| task              | `TaskState`<`TaskContext`\>                            |                                                                                                                                                                  |
| manager           | `KVManager`<`string`, `TaskState`<`TaskContext`\>\>    |                                                                                                                                                                  |
| x                 | `number`                                               | Horizontal position of webview• `set` **x**(`value`): `void`Horizontal position of webview                                                                       |
| y                 | `number`                                               | Vertical position of webview• `set` **y**(`value`): `void`Vertical position of webview                                                                           |
| backgroundColor   | `string`                                               | 8 digit hex value #ffffffff• `set` **backgroundColor**(`value`): `void`8 digit hex value #ffffffff                                                               |
| src               | `string`                                               | Src of webview page supports http:// https:// or local file path• `set` **src**(`value`): `void`Src of webview page supports http:// https:// or local file path |
| close             | (): `Promise`<`void`\>                                 | Close webview                                                                                                                                                    |
| update            | (`options`): `Promise`<{}\>                            | Update properties of webview                                                                                                                                     |
| postMessage       | (`message`): `Promise`<`void`\>                        | Send message to webview page.                                                                                                                                    |
| canGoBack         | (): `Promise`<`boolean`\>                              | Check if can go back from this page                                                                                                                              |
| canGoForward      | (): `Promise`<`boolean`\>                              | Check if can go forward from this page                                                                                                                           |
| url               | (): `Promise`<`string`\>                               | Get current url                                                                                                                                                  |
| title             | (): `Promise`<`string`\>                               | Get current title                                                                                                                                                |
| goBack            | (): `Promise`<`void`\>                                 | Go back to previous page                                                                                                                                         |
| goForward         | (): `Promise`<`void`\>                                 | Go forward to next page                                                                                                                                          |
| refresh           | (): `Promise`<`void`\>                                 | Refresh current page                                                                                                                                             |
| clearCache        | (): `Promise`<`void`\>                                 | Clear webview cache                                                                                                                                              |
| clearScrollStatus | (): `Promise`<`void`\>                                 | Clear scroll status                                                                                                                                              |
| invoke            | (`method`, `payload?`, `options?`): `Promise`<`void`\> | General API for calling webview method                                                                                                                           |
| snapshot          | (): `Promise`<`string`\>                               |                                                                                                                                                                  |
| onMessage         | (`handler`): `void`                                    | Listen message event. Triggered when webview page send message to webview instance.                                                                              |
| offMessage        | (`handler`): `void`                                    | Un-listen message event.                                                                                                                                         |
| onLoad            | (`handler`): `void`                                    | Listen load event. Triggered when webview completes loading.                                                                                                     |
| offLoad           | (`handler`): `void`                                    | Un-listen onload event.                                                                                                                                          |
| onError           | (`handler`): `void`                                    | Listen error event. Triggered when error occurs                                                                                                                  |
| offError          | (`handler`): `void`                                    | Un-listen error event.                                                                                                                                           |
| onUrlChange       | (`handler`): `void`                                    | Listen url change event. Triggered when url changes                                                                                                              |
| offUrlChange      | (`handler`): `void`                                    | Un-listen url change event.                                                                                                                                      |
| onTitleChange     | (`handler`): `void`                                    | Listen title change event. Triggered when title changes                                                                                                          |
| offTitleChange    | (`handler`): `void`                                    | Un-listen title change event.                                                                                                                                    |
| onScrollChange    | (`handler`): `void`                                    | Listen scroll change event. Triggered when title changes                                                                                                         |
| offScrollChange   | (`handler`): `void`                                    | Un-listen scroll change event.                                                                                                                                   |

### close

▸ **close**(): `Promise`<`void`\>

Close webview

Returns

`Promise`<`void`\>

Implementation of

IWebview.close

---

### update

▸ **update**(`options`): `Promise`<{}\>

Update properties of webview

Parameters

| Name      | Type                                |
| :-------- | :---------------------------------- |
| `options` | `Optional`<`CreateWebviewOptions`\> |

Returns

`Promise`<{}\>

Implementation of

IWebview.update

---

### postMessage

▸ **postMessage**(`message`): `Promise`<`void`\>

Send message to webview page.

Parameters

| Name      | Type     |
| :-------- | :------- |
| `message` | `string` |

Returns

`Promise`<`void`\>

Implementation of

IWebview.postMessage

---

### canGoBack

▸ **canGoBack**(): `Promise`<`boolean`\>

Check if can go back from this page

Returns

`Promise`<`boolean`\>

Implementation of

IWebview.canGoBack

---

### canGoForward

▸ **canGoForward**(): `Promise`<`boolean`\>

Check if can go forward from this page

Returns

`Promise`<`boolean`\>

Implementation of

IWebview.canGoForward

---

### url

▸ **url**(): `Promise`<`string`\>

Get current url

Returns

`Promise`<`string`\>

Implementation of

IWebview.url

---

### title

▸ **title**(): `Promise`<`string`\>

Get current title

Returns

`Promise`<`string`\>

Implementation of

IWebview.title

---

### goBack

▸ **goBack**(): `Promise`<`void`\>

Go back to previous page

Returns

`Promise`<`void`\>

Implementation of

IWebview.goBack

---

### goForward

▸ **goForward**(): `Promise`<`void`\>

Go forward to next page

Returns

`Promise`<`void`\>

Implementation of

IWebview.goForward

---

### refresh

▸ **refresh**(): `Promise`<`void`\>

Refresh current page

Returns

`Promise`<`void`\>

Implementation of

IWebview.refresh

---

### clearCache

▸ **clearCache**(): `Promise`<`void`\>

Clear webview cache

Returns

`Promise`<`void`\>

Implementation of

IWebview.clearCache

---

### clearScrollStatus

▸ **clearScrollStatus**(): `Promise`<`void`\>

Clear scroll status

Returns

`Promise`<`void`\>

Implementation of

IWebview.clearScrollStatus

---

### invoke

▸ **invoke**(`method`, `payload?`, `options?`): `Promise`<`void`\>

General API for calling webview method

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `method`   | `string`                   |
| `payload?` | `Record`<`string`, `any`\> |
| `options?` | `Record`<`string`, `any`\> |

Returns

`Promise`<`void`\>

Implementation of

IWebview.invoke

---

### snapshot

▸ **snapshot**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

### onMessage

▸ **onMessage**(`handler`): `void`

Listen message event. Triggered when webview page send message to webview instance.

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `handler` | (`ev`: `MessageEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.onMessage

---

### offMessage

▸ **offMessage**(`handler`): `void`

Un-listen message event.

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `handler` | (`ev`: `MessageEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.offMessage

---

### onLoad

▸ **onLoad**(`handler`): `void`

Listen load event. Triggered when webview completes loading.

Parameters

| Name      | Type                          |
| :-------- | :---------------------------- |
| `handler` | (`ev`: `LoadEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.onLoad

---

### offLoad

▸ **offLoad**(`handler`): `void`

Un-listen onload event.

Parameters

| Name      | Type                          |
| :-------- | :---------------------------- |
| `handler` | (`ev`: `LoadEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.offLoad

---

### onError

▸ **onError**(`handler`): `void`

Listen error event. Triggered when error occurs

Parameters

| Name      | Type                           |
| :-------- | :----------------------------- |
| `handler` | (`ev`: `ErrorEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.onError

---

### offError

▸ **offError**(`handler`): `void`

Un-listen error event.

Parameters

| Name      | Type                           |
| :-------- | :----------------------------- |
| `handler` | (`ev`: `ErrorEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.offError

---

### onUrlChange

▸ **onUrlChange**(`handler`): `void`

Listen url change event. Triggered when url changes

Parameters

| Name      | Type                                            |
| :-------- | :---------------------------------------------- |
| `handler` | (`payload?`: `WebviewUrlChangeEvent`) => `void` |

Returns

`void`

---

### offUrlChange

▸ **offUrlChange**(`handler`): `void`

Un-listen url change event.

Parameters

| Name      | Type                                            |
| :-------- | :---------------------------------------------- |
| `handler` | (`payload?`: `WebviewUrlChangeEvent`) => `void` |

Returns

`void`

---

### onTitleChange

▸ **onTitleChange**(`handler`): `void`

Listen title change event. Triggered when title changes

Parameters

| Name      | Type                                              |
| :-------- | :------------------------------------------------ |
| `handler` | (`payload?`: `WebviewTitleChangeEvent`) => `void` |

Returns

`void`

---

### offTitleChange

▸ **offTitleChange**(`handler`): `void`

Un-listen title change event.

Parameters

| Name      | Type                                              |
| :-------- | :------------------------------------------------ |
| `handler` | (`payload?`: `WebviewTitleChangeEvent`) => `void` |

Returns

`void`

---

### onScrollChange

▸ **onScrollChange**(`handler`): `void`

Listen scroll change event. Triggered when title changes

Parameters

| Name      | Type                                               |
| :-------- | :------------------------------------------------- |
| `handler` | (`payload?`: `WebviewScrollChangeEvent`) => `void` |

Returns

`void`

---

### offScrollChange

▸ **offScrollChange**(`handler`): `void`

Un-listen scroll change event.

Parameters

| Name      | Type                                               |
| :-------- | :------------------------------------------------- |
| `handler` | (`payload?`: `WebviewScrollChangeEvent`) => `void` |

Returns

`void`

## close

▸ **close**(): `void`

Returns

`void`

---

## update

▸ **update**(`options`): `void`

Parameters

| Name      | Type                                |
| :-------- | :---------------------------------- |
| `options` | `Optional`<`CreateWebviewOptions`\> |

Returns

`void`

---

## postMessage

▸ **postMessage**(`message`): `void`

Parameters

| Name      | Type     |
| :-------- | :------- |
| `message` | `string` |

Returns

`void`

---

## canGoBack

▸ **canGoBack**(): `Promise`<`boolean`\>

Returns

`Promise`<`boolean`\>

---

## canGoForward

▸ **canGoForward**(): `Promise`<`boolean`\>

Returns

`Promise`<`boolean`\>

---

## url

▸ **url**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

## title

▸ **title**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

## goBack

▸ **goBack**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## goForward

▸ **goForward**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## refresh

▸ **refresh**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## clearCache

▸ **clearCache**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## clearScrollStatus

▸ **clearScrollStatus**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## invoke

▸ **invoke**(`method`, `payload?`, `options?`): `Promise`<`any`\>

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `method`   | `string`                   |
| `payload?` | `Record`<`string`, `any`\> |
| `options?` | `Record`<`string`, `any`\> |

Returns

`Promise`<`any`\>

---

## Interface: MessageEvent

| Name | Type  | Description |
| :--- | :---- | :---------- |
| data | `any` |             |

## onMessage

▸ **onMessage**(`handler`): `void`

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `handler` | `Handler`<`MessageEvent`\> |

Returns

`void`

---

## offMessage

▸ **offMessage**(`handler`): `void`

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `handler` | `Handler`<`MessageEvent`\> |

Returns

`void`

---

## Interface: LoadEvent

| Name | Type     | Description |
| :--- | :------- | :---------- |
| src  | `string` |             |

## onLoad

▸ **onLoad**(`handler`): `void`

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `handler` | `Handler`<`LoadEvent`\> |

Returns

`void`

---

## offLoad

▸ **offLoad**(`handler`): `void`

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `handler` | `Handler`<`LoadEvent`\> |

Returns

`void`

---

## Interface: ErrorEvent

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| src    | `string` |             |
| error? | `string` |             |

## onError

▸ **onError**(`handler`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `handler` | `Handler`<`ErrorEvent`\> |

Returns

`void`

---

## offError

▸ **offError**(`handler`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `handler` | `Handler`<`ErrorEvent`\> |

Returns

`void`

## Interface: WebviewUrlChangeEvent

| Name         | Type      | Description |
| :----------- | :-------- | :---------- |
| url          | `string`  |             |
| canGoBack    | `boolean` |             |
| canGoForward | `boolean` |             |

## Interface: WebviewTitleChangeEvent

| Name  | Type     | Description |
| :---- | :------- | :---------- |
| title | `string` |             |

## Interface: WebviewScrollChangeEvent

| Name   | Type               | Description |
| :----- | :----------------- | :---------- |
| scroll | `"up"` \| `"down"` |             |

---

# bn.createWebview

▸ **createWebview**(`options`): `Webview`

**`remark`** supported jssdk > 3.13.0

**`description`** Create a webview displayed above mini game. Only one webview is supported at the
same time

**`example`**

```ts
const webview = bn.createWebview({
 // required, resource url, support local file path
 src: '/root/src/index.html',
 // position
 x: 0,
 y: 0,
 // size
 height: 500,
 width: 500,
 // background color in #rrggbbaa format
 backgroundColor: '#FFFFFFFF'
 success (res) {}
}
})
// update webview properties
webview.update({
  x: 100,
  y: 100,
})
// close webview
webview.close()

// send message to webview
webview.postMessage('test')

// listen event on webview
webview.onLoad(() => {})

```

Parameters

| Name      | Type                   | Description            |
| :-------- | :--------------------- | :--------------------- |
| `options` | `CreateWebviewOptions` | create webview options |

Returns

`Webview`

Webview - the webview instance

## CreateWebviewOptions

Ƭ **CreateWebviewOptions**: `Object`

Type declaration

| Name                        | Type                                                   | Description                                                                                                                                                                                            |
| :-------------------------- | :----------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`                       | `string`                                               | Src of webview page supports http:// https:// or local file path                                                                                                                                       |
| `height?`                   | `number`                                               | Height of webview component                                                                                                                                                                            |
| `width?`                    | `number`                                               | Width of webview component                                                                                                                                                                             |
| `x?`                        | `number`                                               | Horizontal position of webview                                                                                                                                                                         |
| `y?`                        | `number`                                               | Vertical position of webview                                                                                                                                                                           |
| `backgroundColor?`          | `string`                                               | 8 digit hex value #ffffffff                                                                                                                                                                            |
| `injected?`                 | `string`[]                                             | Inject specific javascript script file before page loaded                                                                                                                                              |
| `bounce?`                   | `boolean`                                              | whether the page bounces when scroll beyond top/bottom                                                                                                                                                 |
| `loadingBar?`               | `boolean`                                              | whether the page shows loading bar when loading page                                                                                                                                                   |
| `webPreferences?`           | { `[key: string]`: `unknown`; `userAgent?`: `string` } | Setting web preferences, currently only `userAgent` is supported                                                                                                                                       |
| `webPreferences.userAgent?` | `string`                                               | -                                                                                                                                                                                                      |
| `pageId?`                   | `number`                                               | Page id, used to identify the page to show webview. Required in widget. **`example`** `ts   const pageId = getCurrentInstance().page.getPageId();   createWebview({     ...options,     pageId,   }) ` |
| `success?`                  | `CreateWebviewSuccessCallback`                         | -                                                                                                                                                                                                      |
| `fail?`                     | `CreateWebviewCallback`                                | -                                                                                                                                                                                                      |
| `complete?`                 | `CreateWebviewCallback`                                | -                                                                                                                                                                                                      |

---

## CreateWebviewSuccessCallback

Ƭ **CreateWebviewSuccessCallback**: (`{   errMsg,   webview, }`: { `errMsg`: `string` ; `webview`:
`IWebview` }) => `void`

Type declaration

▸ (`{   errMsg,   webview, }`): `void`

Parameters

| Name       | Type       |
| :--------- | :--------- |
| `{         |            |
| errMsg,    |            |
| webview,   |            |
| }`         | `Object`   |
| `{         |            |
| errMsg,    |            |
| webview,   |            |
| }.errMsg`  | `string`   |
| `{         |            |
| errMsg,    |            |
| webview,   |            |
| }.webview` | `IWebview` |

Returns

`void`

---

## Interface: IWebview

| Name              | Type                                                  | Description |
| :---------------- | :---------------------------------------------------- | :---------- |
| src               | `string`                                              |             |
| x                 | `number`                                              |             |
| y                 | `number`                                              |             |
| backgroundColor   | `string`                                              |             |
| update            | (`options`): `void`                                   |             |
| close             | (): `void`                                            |             |
| postMessage       | (`message`): `void`                                   |             |
| canGoBack         | (): `Promise`<`boolean`\>                             |             |
| canGoForward      | (): `Promise`<`boolean`\>                             |             |
| url               | (): `Promise`<`string`\>                              |             |
| title             | (): `Promise`<`string`\>                              |             |
| goBack            | (): `Promise`<`void`\>                                |             |
| goForward         | (): `Promise`<`void`\>                                |             |
| refresh           | (): `Promise`<`void`\>                                |             |
| clearCache        | (): `Promise`<`void`\>                                |             |
| invoke            | (`method`, `payload?`, `options?`): `Promise`<`any`\> |             |
| clearScrollStatus | (): `Promise`<`void`\>                                |             |
| onMessage         | (`handler`): `void`                                   |             |
| offMessage        | (`handler`): `void`                                   |             |
| onLoad            | (`handler`): `void`                                   |             |
| offLoad           | (`handler`): `void`                                   |             |
| onError           | (`handler`): `void`                                   |             |
| offError          | (`handler`): `void`                                   |             |

### update

▸ **update**(`options`): `void`

Parameters

| Name      | Type                                |
| :-------- | :---------------------------------- |
| `options` | `Optional`<`CreateWebviewOptions`\> |

Returns

`void`

---

### close

▸ **close**(): `void`

Returns

`void`

---

### postMessage

▸ **postMessage**(`message`): `void`

Parameters

| Name      | Type     |
| :-------- | :------- |
| `message` | `string` |

Returns

`void`

---

### canGoBack

▸ **canGoBack**(): `Promise`<`boolean`\>

Returns

`Promise`<`boolean`\>

---

### canGoForward

▸ **canGoForward**(): `Promise`<`boolean`\>

Returns

`Promise`<`boolean`\>

---

### url

▸ **url**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

### title

▸ **title**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

### goBack

▸ **goBack**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### goForward

▸ **goForward**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### refresh

▸ **refresh**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### clearCache

▸ **clearCache**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### invoke

▸ **invoke**(`method`, `payload?`, `options?`): `Promise`<`any`\>

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `method`   | `string`                   |
| `payload?` | `Record`<`string`, `any`\> |
| `options?` | `Record`<`string`, `any`\> |

Returns

`Promise`<`any`\>

---

### clearScrollStatus

▸ **clearScrollStatus**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

### onMessage

▸ **onMessage**(`handler`): `void`

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `handler` | `Handler`<`MessageEvent`\> |

Returns

`void`

---

### offMessage

▸ **offMessage**(`handler`): `void`

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `handler` | `Handler`<`MessageEvent`\> |

Returns

`void`

---

### onLoad

▸ **onLoad**(`handler`): `void`

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `handler` | `Handler`<`LoadEvent`\> |

Returns

`void`

---

### offLoad

▸ **offLoad**(`handler`): `void`

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `handler` | `Handler`<`LoadEvent`\> |

Returns

`void`

---

### onError

▸ **onError**(`handler`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `handler` | `Handler`<`ErrorEvent`\> |

Returns

`void`

---

### offError

▸ **offError**(`handler`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `handler` | `Handler`<`ErrorEvent`\> |

Returns

`void`

## Optional

Ƭ **Optional**<`T`\>: `Object`

Type parameters

| Name |
| :--- |
| `T`  |

---

## Handler

Ƭ **Handler**<`T`\>: (`ev`: `T`) => `void`

Type parameters

| Name |
| :--- |
| `T`  |

Type declaration

▸ (`ev`): `void`

Parameters

| Name | Type |
| :--- | :--- |
| `ev` | `T`  |

Returns

`void`

---

## Interface: MessageEvent

| Name | Type  | Description |
| :--- | :---- | :---------- |
| data | `any` |             |

## Interface: LoadEvent

| Name | Type     | Description |
| :--- | :------- | :---------- |
| src  | `string` |             |

## Interface: ErrorEvent

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| src    | `string` |             |
| error? | `string` |             |

## CreateWebviewCallback

Ƭ **CreateWebviewCallback**: (`{ errMsg }`: { `errMsg`: `string` }) => `void`

Type declaration

▸ (`{ errMsg }`): `void`

Parameters

| Name                | Type     |
| :------------------ | :------- |
| `{ errMsg }`        | `Object` |
| `{ errMsg }.errMsg` | `string` |

Returns

`void`

---

## Class: Webview

| Name              | Type                                                   | Description                                                                                                                                                      |
| :---------------- | :----------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_x               | `number`                                               |                                                                                                                                                                  |
| \_y               | `number`                                               |                                                                                                                                                                  |
| \_backgroundColor | `string`                                               |                                                                                                                                                                  |
| \_src             | `string`                                               |                                                                                                                                                                  |
| id                | `number`                                               |                                                                                                                                                                  |
| rpcNative         | `NativeRPC`                                            |                                                                                                                                                                  |
| rpcWebview        | `AppRPC`                                               |                                                                                                                                                                  |
| rendererId        | `number`                                               |                                                                                                                                                                  |
| task              | `TaskState`<`TaskContext`\>                            |                                                                                                                                                                  |
| manager           | `KVManager`<`string`, `TaskState`<`TaskContext`\>\>    |                                                                                                                                                                  |
| x                 | `number`                                               | Horizontal position of webview• `set` **x**(`value`): `void`Horizontal position of webview                                                                       |
| y                 | `number`                                               | Vertical position of webview• `set` **y**(`value`): `void`Vertical position of webview                                                                           |
| backgroundColor   | `string`                                               | 8 digit hex value #ffffffff• `set` **backgroundColor**(`value`): `void`8 digit hex value #ffffffff                                                               |
| src               | `string`                                               | Src of webview page supports http:// https:// or local file path• `set` **src**(`value`): `void`Src of webview page supports http:// https:// or local file path |
| close             | (): `Promise`<`void`\>                                 | Close webview                                                                                                                                                    |
| update            | (`options`): `Promise`<{}\>                            | Update properties of webview                                                                                                                                     |
| postMessage       | (`message`): `Promise`<`void`\>                        | Send message to webview page.                                                                                                                                    |
| canGoBack         | (): `Promise`<`boolean`\>                              | Check if can go back from this page                                                                                                                              |
| canGoForward      | (): `Promise`<`boolean`\>                              | Check if can go forward from this page                                                                                                                           |
| url               | (): `Promise`<`string`\>                               | Get current url                                                                                                                                                  |
| title             | (): `Promise`<`string`\>                               | Get current title                                                                                                                                                |
| goBack            | (): `Promise`<`void`\>                                 | Go back to previous page                                                                                                                                         |
| goForward         | (): `Promise`<`void`\>                                 | Go forward to next page                                                                                                                                          |
| refresh           | (): `Promise`<`void`\>                                 | Refresh current page                                                                                                                                             |
| clearCache        | (): `Promise`<`void`\>                                 | Clear webview cache                                                                                                                                              |
| clearScrollStatus | (): `Promise`<`void`\>                                 | Clear scroll status                                                                                                                                              |
| invoke            | (`method`, `payload?`, `options?`): `Promise`<`void`\> | General API for calling webview method                                                                                                                           |
| snapshot          | (): `Promise`<`string`\>                               |                                                                                                                                                                  |
| onMessage         | (`handler`): `void`                                    | Listen message event. Triggered when webview page send message to webview instance.                                                                              |
| offMessage        | (`handler`): `void`                                    | Un-listen message event.                                                                                                                                         |
| onLoad            | (`handler`): `void`                                    | Listen load event. Triggered when webview completes loading.                                                                                                     |
| offLoad           | (`handler`): `void`                                    | Un-listen onload event.                                                                                                                                          |
| onError           | (`handler`): `void`                                    | Listen error event. Triggered when error occurs                                                                                                                  |
| offError          | (`handler`): `void`                                    | Un-listen error event.                                                                                                                                           |
| onUrlChange       | (`handler`): `void`                                    | Listen url change event. Triggered when url changes                                                                                                              |
| offUrlChange      | (`handler`): `void`                                    | Un-listen url change event.                                                                                                                                      |
| onTitleChange     | (`handler`): `void`                                    | Listen title change event. Triggered when title changes                                                                                                          |
| offTitleChange    | (`handler`): `void`                                    | Un-listen title change event.                                                                                                                                    |
| onScrollChange    | (`handler`): `void`                                    | Listen scroll change event. Triggered when title changes                                                                                                         |
| offScrollChange   | (`handler`): `void`                                    | Un-listen scroll change event.                                                                                                                                   |

### close

▸ **close**(): `Promise`<`void`\>

Close webview

Returns

`Promise`<`void`\>

Implementation of

IWebview.close

---

### update

▸ **update**(`options`): `Promise`<{}\>

Update properties of webview

Parameters

| Name      | Type                                |
| :-------- | :---------------------------------- |
| `options` | `Optional`<`CreateWebviewOptions`\> |

Returns

`Promise`<{}\>

Implementation of

IWebview.update

---

### postMessage

▸ **postMessage**(`message`): `Promise`<`void`\>

Send message to webview page.

Parameters

| Name      | Type     |
| :-------- | :------- |
| `message` | `string` |

Returns

`Promise`<`void`\>

Implementation of

IWebview.postMessage

---

### canGoBack

▸ **canGoBack**(): `Promise`<`boolean`\>

Check if can go back from this page

Returns

`Promise`<`boolean`\>

Implementation of

IWebview.canGoBack

---

### canGoForward

▸ **canGoForward**(): `Promise`<`boolean`\>

Check if can go forward from this page

Returns

`Promise`<`boolean`\>

Implementation of

IWebview.canGoForward

---

### url

▸ **url**(): `Promise`<`string`\>

Get current url

Returns

`Promise`<`string`\>

Implementation of

IWebview.url

---

### title

▸ **title**(): `Promise`<`string`\>

Get current title

Returns

`Promise`<`string`\>

Implementation of

IWebview.title

---

### goBack

▸ **goBack**(): `Promise`<`void`\>

Go back to previous page

Returns

`Promise`<`void`\>

Implementation of

IWebview.goBack

---

### goForward

▸ **goForward**(): `Promise`<`void`\>

Go forward to next page

Returns

`Promise`<`void`\>

Implementation of

IWebview.goForward

---

### refresh

▸ **refresh**(): `Promise`<`void`\>

Refresh current page

Returns

`Promise`<`void`\>

Implementation of

IWebview.refresh

---

### clearCache

▸ **clearCache**(): `Promise`<`void`\>

Clear webview cache

Returns

`Promise`<`void`\>

Implementation of

IWebview.clearCache

---

### clearScrollStatus

▸ **clearScrollStatus**(): `Promise`<`void`\>

Clear scroll status

Returns

`Promise`<`void`\>

Implementation of

IWebview.clearScrollStatus

---

### invoke

▸ **invoke**(`method`, `payload?`, `options?`): `Promise`<`void`\>

General API for calling webview method

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `method`   | `string`                   |
| `payload?` | `Record`<`string`, `any`\> |
| `options?` | `Record`<`string`, `any`\> |

Returns

`Promise`<`void`\>

Implementation of

IWebview.invoke

---

### snapshot

▸ **snapshot**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

### onMessage

▸ **onMessage**(`handler`): `void`

Listen message event. Triggered when webview page send message to webview instance.

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `handler` | (`ev`: `MessageEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.onMessage

---

### offMessage

▸ **offMessage**(`handler`): `void`

Un-listen message event.

Parameters

| Name      | Type                             |
| :-------- | :------------------------------- |
| `handler` | (`ev`: `MessageEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.offMessage

---

### onLoad

▸ **onLoad**(`handler`): `void`

Listen load event. Triggered when webview completes loading.

Parameters

| Name      | Type                          |
| :-------- | :---------------------------- |
| `handler` | (`ev`: `LoadEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.onLoad

---

### offLoad

▸ **offLoad**(`handler`): `void`

Un-listen onload event.

Parameters

| Name      | Type                          |
| :-------- | :---------------------------- |
| `handler` | (`ev`: `LoadEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.offLoad

---

### onError

▸ **onError**(`handler`): `void`

Listen error event. Triggered when error occurs

Parameters

| Name      | Type                           |
| :-------- | :----------------------------- |
| `handler` | (`ev`: `ErrorEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.onError

---

### offError

▸ **offError**(`handler`): `void`

Un-listen error event.

Parameters

| Name      | Type                           |
| :-------- | :----------------------------- |
| `handler` | (`ev`: `ErrorEvent`) => `void` |

Returns

`void`

Implementation of

IWebview.offError

---

### onUrlChange

▸ **onUrlChange**(`handler`): `void`

Listen url change event. Triggered when url changes

Parameters

| Name      | Type                                            |
| :-------- | :---------------------------------------------- |
| `handler` | (`payload?`: `WebviewUrlChangeEvent`) => `void` |

Returns

`void`

---

### offUrlChange

▸ **offUrlChange**(`handler`): `void`

Un-listen url change event.

Parameters

| Name      | Type                                            |
| :-------- | :---------------------------------------------- |
| `handler` | (`payload?`: `WebviewUrlChangeEvent`) => `void` |

Returns

`void`

---

### onTitleChange

▸ **onTitleChange**(`handler`): `void`

Listen title change event. Triggered when title changes

Parameters

| Name      | Type                                              |
| :-------- | :------------------------------------------------ |
| `handler` | (`payload?`: `WebviewTitleChangeEvent`) => `void` |

Returns

`void`

---

### offTitleChange

▸ **offTitleChange**(`handler`): `void`

Un-listen title change event.

Parameters

| Name      | Type                                              |
| :-------- | :------------------------------------------------ |
| `handler` | (`payload?`: `WebviewTitleChangeEvent`) => `void` |

Returns

`void`

---

### onScrollChange

▸ **onScrollChange**(`handler`): `void`

Listen scroll change event. Triggered when title changes

Parameters

| Name      | Type                                               |
| :-------- | :------------------------------------------------- |
| `handler` | (`payload?`: `WebviewScrollChangeEvent`) => `void` |

Returns

`void`

---

### offScrollChange

▸ **offScrollChange**(`handler`): `void`

Un-listen scroll change event.

Parameters

| Name      | Type                                               |
| :-------- | :------------------------------------------------- |
| `handler` | (`payload?`: `WebviewScrollChangeEvent`) => `void` |

Returns

`void`

## close

▸ **close**(): `void`

Returns

`void`

---

## update

▸ **update**(`options`): `void`

Parameters

| Name      | Type                                |
| :-------- | :---------------------------------- |
| `options` | `Optional`<`CreateWebviewOptions`\> |

Returns

`void`

---

## postMessage

▸ **postMessage**(`message`): `void`

Parameters

| Name      | Type     |
| :-------- | :------- |
| `message` | `string` |

Returns

`void`

---

## canGoBack

▸ **canGoBack**(): `Promise`<`boolean`\>

Returns

`Promise`<`boolean`\>

---

## canGoForward

▸ **canGoForward**(): `Promise`<`boolean`\>

Returns

`Promise`<`boolean`\>

---

## url

▸ **url**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

## title

▸ **title**(): `Promise`<`string`\>

Returns

`Promise`<`string`\>

---

## goBack

▸ **goBack**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## goForward

▸ **goForward**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## refresh

▸ **refresh**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## clearCache

▸ **clearCache**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## clearScrollStatus

▸ **clearScrollStatus**(): `Promise`<`void`\>

Returns

`Promise`<`void`\>

---

## invoke

▸ **invoke**(`method`, `payload?`, `options?`): `Promise`<`any`\>

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `method`   | `string`                   |
| `payload?` | `Record`<`string`, `any`\> |
| `options?` | `Record`<`string`, `any`\> |

Returns

`Promise`<`any`\>

---

## Interface: MessageEvent

| Name | Type  | Description |
| :--- | :---- | :---------- |
| data | `any` |             |

## onMessage

▸ **onMessage**(`handler`): `void`

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `handler` | `Handler`<`MessageEvent`\> |

Returns

`void`

---

## offMessage

▸ **offMessage**(`handler`): `void`

Parameters

| Name      | Type                       |
| :-------- | :------------------------- |
| `handler` | `Handler`<`MessageEvent`\> |

Returns

`void`

---

## Interface: LoadEvent

| Name | Type     | Description |
| :--- | :------- | :---------- |
| src  | `string` |             |

## onLoad

▸ **onLoad**(`handler`): `void`

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `handler` | `Handler`<`LoadEvent`\> |

Returns

`void`

---

## offLoad

▸ **offLoad**(`handler`): `void`

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `handler` | `Handler`<`LoadEvent`\> |

Returns

`void`

---

## Interface: ErrorEvent

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| src    | `string` |             |
| error? | `string` |             |

## onError

▸ **onError**(`handler`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `handler` | `Handler`<`ErrorEvent`\> |

Returns

`void`

---

## offError

▸ **offError**(`handler`): `void`

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `handler` | `Handler`<`ErrorEvent`\> |

Returns

`void`

## Interface: WebviewUrlChangeEvent

| Name         | Type      | Description |
| :----------- | :-------- | :---------- |
| url          | `string`  |             |
| canGoBack    | `boolean` |             |
| canGoForward | `boolean` |             |

## Interface: WebviewTitleChangeEvent

| Name  | Type     | Description |
| :---- | :------- | :---------- |
| title | `string` |             |

## Interface: WebviewScrollChangeEvent

| Name   | Type               | Description |
| :----- | :----------------- | :---------- |
| scroll | `"up"` \| `"down"` |             |