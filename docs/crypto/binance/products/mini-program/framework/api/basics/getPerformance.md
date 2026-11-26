---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/getPerformance
api_type: Guide
updated_at: 2026-11-26 18:49:04.062492
---

# bn.getPerformance

▸ **getPerformance**(): `Performance`

Gets the performance information

**`example`**

```js
const performance = bn.getPerformance();
const entries = performance.getEntries();
console.log(entries);
```

Returns

`Performance`

performance

## Interface: Performance

| Name       | Type          | Description                              |
| :--------- | :------------ | :--------------------------------------- |
| getEntries | (): `Entry`[] | Get all current performance information. |

### getEntries

▸ **getEntries**(): `Entry`[]

Get all current performance information.

Returns

`Entry`[]

Inherited from

EntryList.getEntries

## Entry

Ƭ **Entry**: `AppLaunchEntry` \| `NavigationEntry` \| `ScriptEntry` \| `PackageEntry` \|
`RenderEntry` \| `FPEntry` \| `FCPEntry` \| `LCPEntry` \| `NativeCanvasRenderEntry`

---

## Interface: AppLaunchEntry

| Name           | Type           | Description              |
| :------------- | :------------- | :----------------------- |
| entryType      | `"navigation"` |                          |
| name           | `"appLaunch"`  |                          |
| navigationType | `"appLaunch"`  |                          |
| path           | `string`       | entry page path          |
| startTime      | `number`       | start time of app launch |
| duration       | `number`       | total time of app launch |

## Interface: NavigationEntry

| Name            | Type              | Description                 |
| :-------------- | :---------------- | :-------------------------- |
| entryType       | `"navigation"`    |                             |
| name            | `"route"`         |                             |
| navigationType  | `RouteChangeType` | route type                  |
| navigationStart | `number`          | the real time of navigation |
| path            | `string`          | navigate path               |
| startTime       | `number`          | start time of navigation    |
| duration        | `number`          | total time of navigation    |

## Interface: ScriptEntry

| Name       | Type               | Description                   |
| :--------- | :----------------- | :---------------------------- |
| entryType  | `"script"`         |                               |
| name       | `"evaluateScript"` |                               |
| startTime  | `number`           | start time of evaluate script |
| duration   | `number`           | total time of evaluate script |
| moduleName | `string`           |                               |
| fileList   | `string`[]         |                               |

## Interface: PackageEntry

| Name         | Type                | Description                    |
| :----------- | :------------------ | :----------------------------- |
| entryType    | `"loadPackage"`     |                                |
| name         | `"downloadPackage"` |                                |
| startTime    | `number`            | start time of download package |
| duration     | `number`            | total time of download package |
| packageName  | `string`            |                                |
| packageSize  | `number`            |                                |
| isLocalCache | `boolean`           | is from local cache            |

## Interface: RenderEntry

| Name                     | Type            | Description                |
| :----------------------- | :-------------- | :------------------------- |
| entryType                | `"render"`      |                            |
| name                     | `"firstRender"` |                            |
| path                     | `string`        | page path                  |
| startTime                | `number`        | start time of page render  |
| duration                 | `number`        | total time of first render |
| viewLayerReadyTime       | `number`        |                            |
| initDataSendTime         | `number`        |                            |
| initDataRecvTime         | `number`        |                            |
| viewLayerRenderStartTime | `number`        |                            |
| viewLayerRenderEndTime   | `number`        |                            |

## Interface: FPEntry

| Name      | Type           | Description  |
| :-------- | :------------- | :----------- |
| entryType | `"render"`     |              |
| name      | `"firstPaint"` |              |
| path      | `string`       | page path    |
| startTime | `number`       | FP timestamp |

## Interface: FCPEntry

| Name      | Type                     | Description   |
| :-------- | :----------------------- | :------------ |
| entryType | `"render"`               |               |
| name      | `"firstContentfulPaint"` |               |
| path      | `string`                 | page path     |
| startTime | `number`                 | FCP timestamp |

## Interface: LCPEntry

| Name      | Type                       | Description   |
| :-------- | :------------------------- | :------------ |
| entryType | `"render"`                 |               |
| name      | `"largestContentfulPaint"` |               |
| path      | `string`                   | page path     |
| startTime | `number`                   | LCP timestamp |

## Interface: NativeCanvasRenderEntry

| Name                    | Type                         | Description |
| :---------------------- | :--------------------------- | :---------- |
| entryType               | `"canvas"`                   |             |
| name                    | `"canvasRender"`             |             |
| drawCommandsLength      | `number`                     |             |
| callEnable?             | `CanvasRenderApiPerformance` |             |
| callEnableDebug?        | `CanvasRenderApiPerformance` |             |
| callEnableDisableCombo? | `CanvasRenderApiPerformance` |             |
| callSetContextType?     | `CanvasRenderApiPerformance` |             |
| render?                 | `CanvasRenderApiPerformance` |             |
| render2d?               | `CanvasRenderApiPerformance` |             |
| flushNative?            | `CanvasRenderApiPerformance` |             |
| callNative?             | `CanvasRenderApiPerformance` |             |
| texImage2D?             | `CanvasRenderApiPerformance` |             |
| texSubImage2D?          | `CanvasRenderApiPerformance` |             |
| bindImageTexture?       | `CanvasRenderApiPerformance` |             |
| bindCanvasTexture?      | `CanvasRenderApiPerformance` |             |
| createOffscreenCanvas?  | `CanvasRenderApiPerformance` |             |
| resizeOffscreenCanvas?  | `CanvasRenderApiPerformance` |             |
| destroyOffscreenCanvas? | `CanvasRenderApiPerformance` |             |
| perloadImage?           | `CanvasRenderApiPerformance` |             |
| measureTextWidth?       | `CanvasRenderApiPerformance` |             |

## Interface: EntryList

| Name       | Type          | Description                              |
| :--------- | :------------ | :--------------------------------------- |
| getEntries | (): `Entry`[] | Get all current performance information. |

### getEntries

▸ **getEntries**(): `Entry`[]

Get all current performance information.

Returns

`Entry`[]

## getEntries

▸ **getEntries**(): `Entry`[]

Get all current performance information.

Returns

`Entry`[]

---

# bn.getPerformance

▸ **getPerformance**(): `Performance`

Gets the performance information

**`example`**

```js
const performance = bn.getPerformance();
const entries = performance.getEntries();
console.log(entries);
```

Returns

`Performance`

performance

## Interface: Performance

| Name       | Type          | Description                              |
| :--------- | :------------ | :--------------------------------------- |
| getEntries | (): `Entry`[] | Get all current performance information. |

### getEntries

▸ **getEntries**(): `Entry`[]

Get all current performance information.

Returns

`Entry`[]

Inherited from

EntryList.getEntries

## Entry

Ƭ **Entry**: `AppLaunchEntry` \| `NavigationEntry` \| `ScriptEntry` \| `PackageEntry` \|
`RenderEntry` \| `FPEntry` \| `FCPEntry` \| `LCPEntry` \| `NativeCanvasRenderEntry`

---

## Interface: AppLaunchEntry

| Name           | Type           | Description              |
| :------------- | :------------- | :----------------------- |
| entryType      | `"navigation"` |                          |
| name           | `"appLaunch"`  |                          |
| navigationType | `"appLaunch"`  |                          |
| path           | `string`       | entry page path          |
| startTime      | `number`       | start time of app launch |
| duration       | `number`       | total time of app launch |

## Interface: NavigationEntry

| Name            | Type              | Description                 |
| :-------------- | :---------------- | :-------------------------- |
| entryType       | `"navigation"`    |                             |
| name            | `"route"`         |                             |
| navigationType  | `RouteChangeType` | route type                  |
| navigationStart | `number`          | the real time of navigation |
| path            | `string`          | navigate path               |
| startTime       | `number`          | start time of navigation    |
| duration        | `number`          | total time of navigation    |

## Interface: ScriptEntry

| Name       | Type               | Description                   |
| :--------- | :----------------- | :---------------------------- |
| entryType  | `"script"`         |                               |
| name       | `"evaluateScript"` |                               |
| startTime  | `number`           | start time of evaluate script |
| duration   | `number`           | total time of evaluate script |
| moduleName | `string`           |                               |
| fileList   | `string`[]         |                               |

## Interface: PackageEntry

| Name         | Type                | Description                    |
| :----------- | :------------------ | :----------------------------- |
| entryType    | `"loadPackage"`     |                                |
| name         | `"downloadPackage"` |                                |
| startTime    | `number`            | start time of download package |
| duration     | `number`            | total time of download package |
| packageName  | `string`            |                                |
| packageSize  | `number`            |                                |
| isLocalCache | `boolean`           | is from local cache            |

## Interface: RenderEntry

| Name                     | Type            | Description                |
| :----------------------- | :-------------- | :------------------------- |
| entryType                | `"render"`      |                            |
| name                     | `"firstRender"` |                            |
| path                     | `string`        | page path                  |
| startTime                | `number`        | start time of page render  |
| duration                 | `number`        | total time of first render |
| viewLayerReadyTime       | `number`        |                            |
| initDataSendTime         | `number`        |                            |
| initDataRecvTime         | `number`        |                            |
| viewLayerRenderStartTime | `number`        |                            |
| viewLayerRenderEndTime   | `number`        |                            |

## Interface: FPEntry

| Name      | Type           | Description  |
| :-------- | :------------- | :----------- |
| entryType | `"render"`     |              |
| name      | `"firstPaint"` |              |
| path      | `string`       | page path    |
| startTime | `number`       | FP timestamp |

## Interface: FCPEntry

| Name      | Type                     | Description   |
| :-------- | :----------------------- | :------------ |
| entryType | `"render"`               |               |
| name      | `"firstContentfulPaint"` |               |
| path      | `string`                 | page path     |
| startTime | `number`                 | FCP timestamp |

## Interface: LCPEntry

| Name      | Type                       | Description   |
| :-------- | :------------------------- | :------------ |
| entryType | `"render"`                 |               |
| name      | `"largestContentfulPaint"` |               |
| path      | `string`                   | page path     |
| startTime | `number`                   | LCP timestamp |

## Interface: NativeCanvasRenderEntry

| Name                    | Type                         | Description |
| :---------------------- | :--------------------------- | :---------- |
| entryType               | `"canvas"`                   |             |
| name                    | `"canvasRender"`             |             |
| drawCommandsLength      | `number`                     |             |
| callEnable?             | `CanvasRenderApiPerformance` |             |
| callEnableDebug?        | `CanvasRenderApiPerformance` |             |
| callEnableDisableCombo? | `CanvasRenderApiPerformance` |             |
| callSetContextType?     | `CanvasRenderApiPerformance` |             |
| render?                 | `CanvasRenderApiPerformance` |             |
| render2d?               | `CanvasRenderApiPerformance` |             |
| flushNative?            | `CanvasRenderApiPerformance` |             |
| callNative?             | `CanvasRenderApiPerformance` |             |
| texImage2D?             | `CanvasRenderApiPerformance` |             |
| texSubImage2D?          | `CanvasRenderApiPerformance` |             |
| bindImageTexture?       | `CanvasRenderApiPerformance` |             |
| bindCanvasTexture?      | `CanvasRenderApiPerformance` |             |
| createOffscreenCanvas?  | `CanvasRenderApiPerformance` |             |
| resizeOffscreenCanvas?  | `CanvasRenderApiPerformance` |             |
| destroyOffscreenCanvas? | `CanvasRenderApiPerformance` |             |
| perloadImage?           | `CanvasRenderApiPerformance` |             |
| measureTextWidth?       | `CanvasRenderApiPerformance` |             |

## Interface: EntryList

| Name       | Type          | Description                              |
| :--------- | :------------ | :--------------------------------------- |
| getEntries | (): `Entry`[] | Get all current performance information. |

### getEntries

▸ **getEntries**(): `Entry`[]

Get all current performance information.

Returns

`Entry`[]

## getEntries

▸ **getEntries**(): `Entry`[]

Get all current performance information.

Returns

`Entry`[]