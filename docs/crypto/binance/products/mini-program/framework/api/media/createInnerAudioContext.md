---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/createInnerAudioContext
api_type: Guide
updated_at: 2026-11-20 18:46:55.971581
---

# bn.createInnerAudioContext

▸ **createInnerAudioContext**(`options?`): `InnerAudioContext`

**`description`** Creates the context InnerAudioContext object for an internal audio

**`example`**

```js
const innerAudioContext = bn.createInnerAudioContext();
innerAudioContext.autoplay = true;
innerAudioContext.src = "https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3";
innerAudioContext.onPlay(() => {
  console.log("Start playback");
});
innerAudioContext.onError((res) => {
  console.log(res.errMsg);
  console.log(res.errCode);
});
```

Parameters

| Name       | Type                            | Description                        |
| :--------- | :------------------------------ | :--------------------------------- |
| `options?` | `CreateInnerAudioContextOption` | InnerAudioContext creation options |

Returns

`InnerAudioContext`

---

## Interface: CreateInnerAudioContextOption

| Name                  | Type      | Description                                                                                                                                                                                                   |
| :-------------------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| useWebAudioImplement? | `boolean` | Whether or not to use WebAudio. Turns off by default. For short audio, frequent audio is recommended to enable this option, open will get better performance, for long audio recommended to close this option |

## Interface: InnerAudioContext

| Name           | Type                                  | Description                                                                                                                                                 |
| :------------- | :------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| destroy        | (): `void`                            | Terminates the current instance                                                                                                                             |
| offCanplay     | (`callback?`): `void`                 | Unlistens on the event that an audio file is ready for playback                                                                                             |
| offEnded       | (`callback?`): `void`                 | Unlistens on the event of playing an audio file to the end without interruption                                                                             |
| offError       | (`callback?`): `void`                 | Unlistens on the audio playback error event                                                                                                                 |
| offPause       | (`callback?`): `void`                 | Unlistens on the audio pause event                                                                                                                          |
| offPlay        | (`callback?`): `void`                 | Unlistens on the audio playback event                                                                                                                       |
| offSeeked      | (`callback?`): `void`                 | Unlistens on the event of finishing the jump to a specific position in the audio file                                                                       |
| offSeeking     | (`callback?`): `void`                 | Unlistens on the event of jumping to a specific position in the audio file                                                                                  |
| offStop        | (`callback?`): `void`                 | Unlistens on the event of stopping audio playback                                                                                                           |
| offTimeUpdate  | (`callback?`): `void`                 | Unlistens on the event of updating audio playback progress.                                                                                                 |
| offWaiting     | (`callback?`): `void`                 | Unlistens on the audio loading event                                                                                                                        |
| onCanplay      | (`callback`): `void`                  | Listens on the event that an audio file is ready for playback. A smooth playback is not guaranteed                                                          |
| onEnded        | (`callback`): `void`                  | Listens on the event of playing an audio file to the end without interruption                                                                               |
| onError        | (`callback`): `void`                  | Listens on the audio playback error event                                                                                                                   |
| onPause        | (`callback`): `void`                  | Listens on the audio pause event                                                                                                                            |
| onPlay         | (`callback`): `void`                  | Listens on the audio playback event                                                                                                                         |
| onSeeked       | (`callback`): `void`                  | Listens on the event of finishing the jump to a specific position in the audio file                                                                         |
| onSeeking      | (`callback`): `void`                  | Listens on the event of jumping to a specific position in the audio file                                                                                    |
| onStop         | (`callback`): `void`                  | Listens on the event of stopping audio playback                                                                                                             |
| onTimeUpdate   | (`callback`): `void`                  | Listens on the event of updating audio playback progress                                                                                                    |
| onWaiting      | (`callback`): `void`                  | Listens on the audio loading event. It is triggered when the playback of an audio file stops to load the file due to insufficient data                      |
| pause          | (): `void`                            | Pauses the audio playback. The playback is resumed at the point where it was paused                                                                         |
| play           | (): `void`                            | Plays an audio file                                                                                                                                         |
| seek           | (`position`): `void`                  | Jumps to the specific position                                                                                                                              |
| stop           | (): `void`                            | Stops the audio playback. The playback starts from the beginning if the file is played again                                                                |
| autoplay       | `boolean`                             | Whether to enable auto playback. It is false by default                                                                                                     |
| buffered       | `number`                              | The position where the audio is buffered. Only the part between the position where the playback has got to and this position is buffered (read only)        |
| currentTime    | `number`                              | The position where the playback has got to (in sec). It is only returned when a valid src attribute exists and is rounded to six decimal places (read only) |
| duration       | `number`                              | The length of the audio file (in sec). It is only returned when a valid src attribute exists (read only)                                                    |
| loop           | `boolean`                             | Whether to enable loop playback. It is false by default                                                                                                     |
| obeyMuteSwitch | `boolean`                             | Whether to follow the "Mute" switch. It is true by default. If it is set to false, the audio file still sounds even if the "Mute" switch is on              |
| paused         | `boolean`                             | Whether the playback is paused or stopped (read only)                                                                                                       |
| playbackRate   | `number`                              | Specifies the playbackRate, which ranges from 0.5 to 2. It is 1 by default                                                                                  |
| src            | `string`                              | The audio file address which can be used to play the audio file directly                                                                                    |
| startTime      | `number`                              | The position where the playback starts (in sec). It is 0 by default                                                                                         |
| volume         | `number`                              | Specifies the volume, which ranges from 0 to 1. It is 1 by default                                                                                          |
| referrerPolicy | `""` \| `"origin"` \| `"no-referrer"` | referrer policy; origin - send request with referrer; no-referrer - do send with referrer                                                                   |

### destroy

▸ **destroy**(): `void`

Terminates the current instance

Returns

`void`

---

### offCanplay

▸ **offCanplay**(`callback?`): `void`

Unlistens on the event that an audio file is ready for playback

Parameters

| Name        | Type                 |
| :---------- | :------------------- |
| `callback?` | `OffCanplayCallback` |

Returns

`void`

---

### offEnded

▸ **offEnded**(`callback?`): `void`

Unlistens on the event of playing an audio file to the end without interruption

Parameters

| Name        | Type               |
| :---------- | :----------------- |
| `callback?` | `OffEndedCallback` |

Returns

`void`

---

### offError

▸ **offError**(`callback?`): `void`

Unlistens on the audio playback error event

Parameters

| Name        | Type               |
| :---------- | :----------------- |
| `callback?` | `OffErrorCallback` |

Returns

`void`

---

### offPause

▸ **offPause**(`callback?`): `void`

Unlistens on the audio pause event

Parameters

| Name        | Type               |
| :---------- | :----------------- |
| `callback?` | `OffPauseCallback` |

Returns

`void`

---

### offPlay

▸ **offPlay**(`callback?`): `void`

Unlistens on the audio playback event

Parameters

| Name        | Type              |
| :---------- | :---------------- |
| `callback?` | `OffPlayCallback` |

Returns

`void`

---

### offSeeked

▸ **offSeeked**(`callback?`): `void`

Unlistens on the event of finishing the jump to a specific position in the audio file

Parameters

| Name        | Type                |
| :---------- | :------------------ |
| `callback?` | `OffSeekedCallback` |

Returns

`void`

---

### offSeeking

▸ **offSeeking**(`callback?`): `void`

Unlistens on the event of jumping to a specific position in the audio file

Parameters

| Name        | Type                 |
| :---------- | :------------------- |
| `callback?` | `OffSeekingCallback` |

Returns

`void`

---

### offStop

▸ **offStop**(`callback?`): `void`

Unlistens on the event of stopping audio playback

Parameters

| Name        | Type              |
| :---------- | :---------------- |
| `callback?` | `OffStopCallback` |

Returns

`void`

---

### offTimeUpdate

▸ **offTimeUpdate**(`callback?`): `void`

Unlistens on the event of updating audio playback progress.

Parameters

| Name        | Type                    |
| :---------- | :---------------------- |
| `callback?` | `OffTimeUpdateCallback` |

Returns

`void`

---

### offWaiting

▸ **offWaiting**(`callback?`): `void`

Unlistens on the audio loading event

Parameters

| Name        | Type                 |
| :---------- | :------------------- |
| `callback?` | `OffWaitingCallback` |

Returns

`void`

---

### onCanplay

▸ **onCanplay**(`callback`): `void`

Listens on the event that an audio file is ready for playback. A smooth playback is not guaranteed

Parameters

| Name       | Type                |
| :--------- | :------------------ |
| `callback` | `OnCanplayCallback` |

Returns

`void`

---

### onEnded

▸ **onEnded**(`callback`): `void`

Listens on the event of playing an audio file to the end without interruption

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `OnEndedCallback` |

Returns

`void`

---

### onError

▸ **onError**(`callback`): `void`

Listens on the audio playback error event

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `OnErrorCallback` |

Returns

`void`

---

### onPause

▸ **onPause**(`callback`): `void`

Listens on the audio pause event

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `OnPauseCallback` |

Returns

`void`

---

### onPlay

▸ **onPlay**(`callback`): `void`

Listens on the audio playback event

Parameters

| Name       | Type             |
| :--------- | :--------------- |
| `callback` | `OnPlayCallback` |

Returns

`void`

---

### onSeeked

▸ **onSeeked**(`callback`): `void`

Listens on the event of finishing the jump to a specific position in the audio file

Parameters

| Name       | Type               |
| :--------- | :----------------- |
| `callback` | `OnSeekedCallback` |

Returns

`void`

---

### onSeeking

▸ **onSeeking**(`callback`): `void`

Listens on the event of jumping to a specific position in the audio file

Parameters

| Name       | Type                |
| :--------- | :------------------ |
| `callback` | `OnSeekingCallback` |

Returns

`void`

---

### onStop

▸ **onStop**(`callback`): `void`

Listens on the event of stopping audio playback

Parameters

| Name       | Type             |
| :--------- | :--------------- |
| `callback` | `OnStopCallback` |

Returns

`void`

---

### onTimeUpdate

▸ **onTimeUpdate**(`callback`): `void`

Listens on the event of updating audio playback progress

Parameters

| Name       | Type                   |
| :--------- | :--------------------- |
| `callback` | `OnTimeUpdateCallback` |

Returns

`void`

---

### onWaiting

▸ **onWaiting**(`callback`): `void`

Listens on the audio loading event. It is triggered when the playback of an audio file stops to load
the file due to insufficient data

Parameters

| Name       | Type                |
| :--------- | :------------------ |
| `callback` | `OnWaitingCallback` |

Returns

`void`

---

### pause

▸ **pause**(): `void`

Pauses the audio playback. The playback is resumed at the point where it was paused

Returns

`void`

---

### play

▸ **play**(): `void`

Plays an audio file

Returns

`void`

---

### seek

▸ **seek**(`position`): `void`

Jumps to the specific position

Parameters

| Name       | Type     |
| :--------- | :------- |
| `position` | `number` |

Returns

`void`

---

### stop

▸ **stop**(): `void`

Stops the audio playback. The playback starts from the beginning if the file is played again

Returns

`void`

---

# bn.createInnerAudioContext

▸ **createInnerAudioContext**(`options?`): `InnerAudioContext`

**`description`** Creates the context InnerAudioContext object for an internal audio

**`example`**

```js
const innerAudioContext = bn.createInnerAudioContext();
innerAudioContext.autoplay = true;
innerAudioContext.src = "https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3";
innerAudioContext.onPlay(() => {
  console.log("Start playback");
});
innerAudioContext.onError((res) => {
  console.log(res.errMsg);
  console.log(res.errCode);
});
```

Parameters

| Name       | Type                            | Description                        |
| :--------- | :------------------------------ | :--------------------------------- |
| `options?` | `CreateInnerAudioContextOption` | InnerAudioContext creation options |

Returns

`InnerAudioContext`

---

## Interface: CreateInnerAudioContextOption

| Name                  | Type      | Description                                                                                                                                                                                                   |
| :-------------------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| useWebAudioImplement? | `boolean` | Whether or not to use WebAudio. Turns off by default. For short audio, frequent audio is recommended to enable this option, open will get better performance, for long audio recommended to close this option |

## Interface: InnerAudioContext

| Name           | Type                                  | Description                                                                                                                                                 |
| :------------- | :------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| destroy        | (): `void`                            | Terminates the current instance                                                                                                                             |
| offCanplay     | (`callback?`): `void`                 | Unlistens on the event that an audio file is ready for playback                                                                                             |
| offEnded       | (`callback?`): `void`                 | Unlistens on the event of playing an audio file to the end without interruption                                                                             |
| offError       | (`callback?`): `void`                 | Unlistens on the audio playback error event                                                                                                                 |
| offPause       | (`callback?`): `void`                 | Unlistens on the audio pause event                                                                                                                          |
| offPlay        | (`callback?`): `void`                 | Unlistens on the audio playback event                                                                                                                       |
| offSeeked      | (`callback?`): `void`                 | Unlistens on the event of finishing the jump to a specific position in the audio file                                                                       |
| offSeeking     | (`callback?`): `void`                 | Unlistens on the event of jumping to a specific position in the audio file                                                                                  |
| offStop        | (`callback?`): `void`                 | Unlistens on the event of stopping audio playback                                                                                                           |
| offTimeUpdate  | (`callback?`): `void`                 | Unlistens on the event of updating audio playback progress.                                                                                                 |
| offWaiting     | (`callback?`): `void`                 | Unlistens on the audio loading event                                                                                                                        |
| onCanplay      | (`callback`): `void`                  | Listens on the event that an audio file is ready for playback. A smooth playback is not guaranteed                                                          |
| onEnded        | (`callback`): `void`                  | Listens on the event of playing an audio file to the end without interruption                                                                               |
| onError        | (`callback`): `void`                  | Listens on the audio playback error event                                                                                                                   |
| onPause        | (`callback`): `void`                  | Listens on the audio pause event                                                                                                                            |
| onPlay         | (`callback`): `void`                  | Listens on the audio playback event                                                                                                                         |
| onSeeked       | (`callback`): `void`                  | Listens on the event of finishing the jump to a specific position in the audio file                                                                         |
| onSeeking      | (`callback`): `void`                  | Listens on the event of jumping to a specific position in the audio file                                                                                    |
| onStop         | (`callback`): `void`                  | Listens on the event of stopping audio playback                                                                                                             |
| onTimeUpdate   | (`callback`): `void`                  | Listens on the event of updating audio playback progress                                                                                                    |
| onWaiting      | (`callback`): `void`                  | Listens on the audio loading event. It is triggered when the playback of an audio file stops to load the file due to insufficient data                      |
| pause          | (): `void`                            | Pauses the audio playback. The playback is resumed at the point where it was paused                                                                         |
| play           | (): `void`                            | Plays an audio file                                                                                                                                         |
| seek           | (`position`): `void`                  | Jumps to the specific position                                                                                                                              |
| stop           | (): `void`                            | Stops the audio playback. The playback starts from the beginning if the file is played again                                                                |
| autoplay       | `boolean`                             | Whether to enable auto playback. It is false by default                                                                                                     |
| buffered       | `number`                              | The position where the audio is buffered. Only the part between the position where the playback has got to and this position is buffered (read only)        |
| currentTime    | `number`                              | The position where the playback has got to (in sec). It is only returned when a valid src attribute exists and is rounded to six decimal places (read only) |
| duration       | `number`                              | The length of the audio file (in sec). It is only returned when a valid src attribute exists (read only)                                                    |
| loop           | `boolean`                             | Whether to enable loop playback. It is false by default                                                                                                     |
| obeyMuteSwitch | `boolean`                             | Whether to follow the "Mute" switch. It is true by default. If it is set to false, the audio file still sounds even if the "Mute" switch is on              |
| paused         | `boolean`                             | Whether the playback is paused or stopped (read only)                                                                                                       |
| playbackRate   | `number`                              | Specifies the playbackRate, which ranges from 0.5 to 2. It is 1 by default                                                                                  |
| src            | `string`                              | The audio file address which can be used to play the audio file directly                                                                                    |
| startTime      | `number`                              | The position where the playback starts (in sec). It is 0 by default                                                                                         |
| volume         | `number`                              | Specifies the volume, which ranges from 0 to 1. It is 1 by default                                                                                          |
| referrerPolicy | `""` \| `"origin"` \| `"no-referrer"` | referrer policy; origin - send request with referrer; no-referrer - do send with referrer                                                                   |

### destroy

▸ **destroy**(): `void`

Terminates the current instance

Returns

`void`

---

### offCanplay

▸ **offCanplay**(`callback?`): `void`

Unlistens on the event that an audio file is ready for playback

Parameters

| Name        | Type                 |
| :---------- | :------------------- |
| `callback?` | `OffCanplayCallback` |

Returns

`void`

---

### offEnded

▸ **offEnded**(`callback?`): `void`

Unlistens on the event of playing an audio file to the end without interruption

Parameters

| Name        | Type               |
| :---------- | :----------------- |
| `callback?` | `OffEndedCallback` |

Returns

`void`

---

### offError

▸ **offError**(`callback?`): `void`

Unlistens on the audio playback error event

Parameters

| Name        | Type               |
| :---------- | :----------------- |
| `callback?` | `OffErrorCallback` |

Returns

`void`

---

### offPause

▸ **offPause**(`callback?`): `void`

Unlistens on the audio pause event

Parameters

| Name        | Type               |
| :---------- | :----------------- |
| `callback?` | `OffPauseCallback` |

Returns

`void`

---

### offPlay

▸ **offPlay**(`callback?`): `void`

Unlistens on the audio playback event

Parameters

| Name        | Type              |
| :---------- | :---------------- |
| `callback?` | `OffPlayCallback` |

Returns

`void`

---

### offSeeked

▸ **offSeeked**(`callback?`): `void`

Unlistens on the event of finishing the jump to a specific position in the audio file

Parameters

| Name        | Type                |
| :---------- | :------------------ |
| `callback?` | `OffSeekedCallback` |

Returns

`void`

---

### offSeeking

▸ **offSeeking**(`callback?`): `void`

Unlistens on the event of jumping to a specific position in the audio file

Parameters

| Name        | Type                 |
| :---------- | :------------------- |
| `callback?` | `OffSeekingCallback` |

Returns

`void`

---

### offStop

▸ **offStop**(`callback?`): `void`

Unlistens on the event of stopping audio playback

Parameters

| Name        | Type              |
| :---------- | :---------------- |
| `callback?` | `OffStopCallback` |

Returns

`void`

---

### offTimeUpdate

▸ **offTimeUpdate**(`callback?`): `void`

Unlistens on the event of updating audio playback progress.

Parameters

| Name        | Type                    |
| :---------- | :---------------------- |
| `callback?` | `OffTimeUpdateCallback` |

Returns

`void`

---

### offWaiting

▸ **offWaiting**(`callback?`): `void`

Unlistens on the audio loading event

Parameters

| Name        | Type                 |
| :---------- | :------------------- |
| `callback?` | `OffWaitingCallback` |

Returns

`void`

---

### onCanplay

▸ **onCanplay**(`callback`): `void`

Listens on the event that an audio file is ready for playback. A smooth playback is not guaranteed

Parameters

| Name       | Type                |
| :--------- | :------------------ |
| `callback` | `OnCanplayCallback` |

Returns

`void`

---

### onEnded

▸ **onEnded**(`callback`): `void`

Listens on the event of playing an audio file to the end without interruption

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `OnEndedCallback` |

Returns

`void`

---

### onError

▸ **onError**(`callback`): `void`

Listens on the audio playback error event

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `OnErrorCallback` |

Returns

`void`

---

### onPause

▸ **onPause**(`callback`): `void`

Listens on the audio pause event

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `callback` | `OnPauseCallback` |

Returns

`void`

---

### onPlay

▸ **onPlay**(`callback`): `void`

Listens on the audio playback event

Parameters

| Name       | Type             |
| :--------- | :--------------- |
| `callback` | `OnPlayCallback` |

Returns

`void`

---

### onSeeked

▸ **onSeeked**(`callback`): `void`

Listens on the event of finishing the jump to a specific position in the audio file

Parameters

| Name       | Type               |
| :--------- | :----------------- |
| `callback` | `OnSeekedCallback` |

Returns

`void`

---

### onSeeking

▸ **onSeeking**(`callback`): `void`

Listens on the event of jumping to a specific position in the audio file

Parameters

| Name       | Type                |
| :--------- | :------------------ |
| `callback` | `OnSeekingCallback` |

Returns

`void`

---

### onStop

▸ **onStop**(`callback`): `void`

Listens on the event of stopping audio playback

Parameters

| Name       | Type             |
| :--------- | :--------------- |
| `callback` | `OnStopCallback` |

Returns

`void`

---

### onTimeUpdate

▸ **onTimeUpdate**(`callback`): `void`

Listens on the event of updating audio playback progress

Parameters

| Name       | Type                   |
| :--------- | :--------------------- |
| `callback` | `OnTimeUpdateCallback` |

Returns

`void`

---

### onWaiting

▸ **onWaiting**(`callback`): `void`

Listens on the audio loading event. It is triggered when the playback of an audio file stops to load
the file due to insufficient data

Parameters

| Name       | Type                |
| :--------- | :------------------ |
| `callback` | `OnWaitingCallback` |

Returns

`void`

---

### pause

▸ **pause**(): `void`

Pauses the audio playback. The playback is resumed at the point where it was paused

Returns

`void`

---

### play

▸ **play**(): `void`

Plays an audio file

Returns

`void`

---

### seek

▸ **seek**(`position`): `void`

Jumps to the specific position

Parameters

| Name       | Type     |
| :--------- | :------- |
| `position` | `number` |

Returns

`void`

---

### stop

▸ **stop**(): `void`

Stops the audio playback. The playback starts from the beginning if the file is played again

Returns

`void`