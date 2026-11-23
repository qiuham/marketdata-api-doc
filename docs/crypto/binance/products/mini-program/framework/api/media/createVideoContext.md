---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/createVideoContext
api_type: Guide
updated_at: 2026-11-23 18:45:57.332071
---

# bn.createVideoContext

▸ **createVideoContext**(`id`): `VideoContext`

**`description`** create video context VideoContext Object. Recommended use bn.createSelectorQuery
Obtain context Object

**`example`**

```ts
const videoContextCurrent = bn.createVideoContext("test-id");
```

Parameters

| Name | Type     |
| :--- | :------- |
| `id` | `string` |

Returns

`VideoContext`

VideoContext

## Interface: VideoContext

| Name                      | Type                 | Description                                                                                                                        |
| :------------------------ | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| exitBackgroundPlayback    | (): `void`           | Exit background audio playback mode.                                                                                               |
| exitFullScreen            | (): `void`           | Exit Full Screen.                                                                                                                  |
| exitPictureInPicture      | (`option?`): `void`  | Exit window, which can be called on any page.                                                                                      |
| hideStatusBar             | (): `void`           | Hide the status bar, only available in full iOS screen.                                                                            |
| pause                     | (): `void`           | Pause video.                                                                                                                       |
| play                      | (): `void`           | Play the video.                                                                                                                    |
| playbackRate              | (`rate`): `void`     | Set playback speed.                                                                                                                |
| requestBackgroundPlayback | (): `void`           | Enter background audio playback mode.                                                                                              |
| requestFullScreen         | (`option`): `void`   | Go to full screen. If you have custom content that needs to be displayed at full screen, place the content node in the video Node. |
| seek                      | (`position`): `void` | Jump to the specified location.                                                                                                    |
| showStatusBar             | (): `void`           | Display status bar, valid for iOS full screen only.                                                                                |
| stop                      | (): `void`           | Stop the video.                                                                                                                    |

### exitBackgroundPlayback

▸ **exitBackgroundPlayback**(): `void`

Exit background audio playback mode.

Returns

`void`

---

### exitFullScreen

▸ **exitFullScreen**(): `void`

Exit Full Screen.

Returns

`void`

---

### exitPictureInPicture

▸ **exitPictureInPicture**(`option?`): `void`

Exit window, which can be called on any page.

Parameters

| Name      | Type                         |
| :-------- | :--------------------------- |
| `option?` | `ExitPictureInPictureOption` |

Returns

`void`

---

### hideStatusBar

▸ **hideStatusBar**(): `void`

Hide the status bar, only available in full iOS screen.

Returns

`void`

---

### pause

▸ **pause**(): `void`

Pause video.

Returns

`void`

---

### play

▸ **play**(): `void`

Play the video.

Returns

`void`

---

### playbackRate

▸ **playbackRate**(`rate`): `void`

Set playback speed.

Parameters

| Name   | Type     |
| :----- | :------- |
| `rate` | `number` |

Returns

`void`

---

### requestBackgroundPlayback

▸ **requestBackgroundPlayback**(): `void`

Enter background audio playback mode.

Returns

`void`

---

### requestFullScreen

▸ **requestFullScreen**(`option`): `void`

Go to full screen. If you have custom content that needs to be displayed at full screen, place the
content node in the video Node.

Parameters

| Name     | Type                                  |
| :------- | :------------------------------------ |
| `option` | `VideoContextRequestFullScreenOption` |

Returns

`void`

---

### seek

▸ **seek**(`position`): `void`

Jump to the specified location.

Parameters

| Name       | Type     |
| :--------- | :------- |
| `position` | `number` |

Returns

`void`

---

### showStatusBar

▸ **showStatusBar**(): `void`

Display status bar, valid for iOS full screen only.

Returns

`void`

---

### stop

▸ **stop**(): `void`

Stop the video.

Returns

`void`

## Interface: ExitPictureInPictureOption

| Name      | Type            | Description |
| :-------- | :-------------- | :---------- |
| complete? | (`res`): `void` |             |
| fail?     | (`res`): `void` |             |
| success?  | (`res`): `void` |             |

### complete

▸ `Optional` **complete**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### fail

▸ `Optional` **fail**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### success

▸ `Optional` **success**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

## Interface: GeneralCallbackResult

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| errMsg | `string` |             |

## Interface: VideoContextRequestFullScreenOption

| Name       | Type                 | Description                                                                                                                                                                                                                                                        |
| :--------- | :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| direction? | `0` \| `90` \| `-90` | Set the direction of the video at full screen. If not specified, it will be judged automatically according to the aspect ratio.; object.direction Legal value; 0: Normal vertical; 90: The screen is 90 degrees counterclockwise; -90: Screen 90 degrees clockwise |

---

# bn.createVideoContext

▸ **createVideoContext**(`id`): `VideoContext`

**`description`** create video context VideoContext Object. Recommended use bn.createSelectorQuery
Obtain context Object

**`example`**

```ts
const videoContextCurrent = bn.createVideoContext("test-id");
```

Parameters

| Name | Type     |
| :--- | :------- |
| `id` | `string` |

Returns

`VideoContext`

VideoContext

## Interface: VideoContext

| Name                      | Type                 | Description                                                                                                                        |
| :------------------------ | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| exitBackgroundPlayback    | (): `void`           | Exit background audio playback mode.                                                                                               |
| exitFullScreen            | (): `void`           | Exit Full Screen.                                                                                                                  |
| exitPictureInPicture      | (`option?`): `void`  | Exit window, which can be called on any page.                                                                                      |
| hideStatusBar             | (): `void`           | Hide the status bar, only available in full iOS screen.                                                                            |
| pause                     | (): `void`           | Pause video.                                                                                                                       |
| play                      | (): `void`           | Play the video.                                                                                                                    |
| playbackRate              | (`rate`): `void`     | Set playback speed.                                                                                                                |
| requestBackgroundPlayback | (): `void`           | Enter background audio playback mode.                                                                                              |
| requestFullScreen         | (`option`): `void`   | Go to full screen. If you have custom content that needs to be displayed at full screen, place the content node in the video Node. |
| seek                      | (`position`): `void` | Jump to the specified location.                                                                                                    |
| showStatusBar             | (): `void`           | Display status bar, valid for iOS full screen only.                                                                                |
| stop                      | (): `void`           | Stop the video.                                                                                                                    |

### exitBackgroundPlayback

▸ **exitBackgroundPlayback**(): `void`

Exit background audio playback mode.

Returns

`void`

---

### exitFullScreen

▸ **exitFullScreen**(): `void`

Exit Full Screen.

Returns

`void`

---

### exitPictureInPicture

▸ **exitPictureInPicture**(`option?`): `void`

Exit window, which can be called on any page.

Parameters

| Name      | Type                         |
| :-------- | :--------------------------- |
| `option?` | `ExitPictureInPictureOption` |

Returns

`void`

---

### hideStatusBar

▸ **hideStatusBar**(): `void`

Hide the status bar, only available in full iOS screen.

Returns

`void`

---

### pause

▸ **pause**(): `void`

Pause video.

Returns

`void`

---

### play

▸ **play**(): `void`

Play the video.

Returns

`void`

---

### playbackRate

▸ **playbackRate**(`rate`): `void`

Set playback speed.

Parameters

| Name   | Type     |
| :----- | :------- |
| `rate` | `number` |

Returns

`void`

---

### requestBackgroundPlayback

▸ **requestBackgroundPlayback**(): `void`

Enter background audio playback mode.

Returns

`void`

---

### requestFullScreen

▸ **requestFullScreen**(`option`): `void`

Go to full screen. If you have custom content that needs to be displayed at full screen, place the
content node in the video Node.

Parameters

| Name     | Type                                  |
| :------- | :------------------------------------ |
| `option` | `VideoContextRequestFullScreenOption` |

Returns

`void`

---

### seek

▸ **seek**(`position`): `void`

Jump to the specified location.

Parameters

| Name       | Type     |
| :--------- | :------- |
| `position` | `number` |

Returns

`void`

---

### showStatusBar

▸ **showStatusBar**(): `void`

Display status bar, valid for iOS full screen only.

Returns

`void`

---

### stop

▸ **stop**(): `void`

Stop the video.

Returns

`void`

## Interface: ExitPictureInPictureOption

| Name      | Type            | Description |
| :-------- | :-------------- | :---------- |
| complete? | (`res`): `void` |             |
| fail?     | (`res`): `void` |             |
| success?  | (`res`): `void` |             |

### complete

▸ `Optional` **complete**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### fail

▸ `Optional` **fail**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### success

▸ `Optional` **success**(`res`): `void`

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

## Interface: GeneralCallbackResult

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| errMsg | `string` |             |

## Interface: VideoContextRequestFullScreenOption

| Name       | Type                 | Description                                                                                                                                                                                                                                                        |
| :--------- | :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| direction? | `0` \| `90` \| `-90` | Set the direction of the video at full screen. If not specified, it will be judged automatically according to the aspect ratio.; object.direction Legal value; 0: Normal vertical; 90: The screen is 90 degrees counterclockwise; -90: Screen 90 degrees clockwise |