---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Input
api_type: Guide
updated_at: 2026-11-22 18:40:29.223391
---

# input

## Props

| Property                     | Type           | Default Value       | Required | Description                                                                                                                                                                                                    |
| ---------------------------- | -------------- | ------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value                        | String, Number |                     |          | The initial content in the input box.                                                                                                                                                                          |
| type                         | String         | `text`              |          | The type of input.                                                                                                                                                                                             |
| password                     | Boolean        | `false`             |          | Specifies whether the input is password-type content.                                                                                                                                                          |
| placeholder                  | String         |                     |          | The placeholder used when the input box is empty.                                                                                                                                                              |
| placeholderStyle             | String         |                     |          | Specifies the style of the placeholder.                                                                                                                                                                        |
| placeholderClass             | String         | `input-placeholder` |          | Specifies the style class of the placeholder.                                                                                                                                                                  |
| disabled                     | Boolean        | `false`             |          | Specifies whether to disable the component.                                                                                                                                                                    |
| maxlength                    | Number         | `140`               |          | The maximum length. When it is set to `-1`, the maximum length is not limited.                                                                                                                                 |
| cursorSpacing                | Number         | `0`                 |          | Specifies the distance between the cursor and the keyboard. It is either the distance between the input box and the bottom of the screen or the distance specified via `cursorSpacing`, whichever is smaller.. |
| autoFocus                    | Boolean        | `false`             |          | (Will be discarded soon. Use the focus instead.) Auto focus. The keyboard is automatically displayed.                                                                                                          |
| focus                        | Boolean        | `false`             |          | Gets focus.                                                                                                                                                                                                    |
| confirmType                  | String         | `done`              |          | Sets the text on the lower-right button on the keyboard. It takes effect only when type='text'.                                                                                                                |
| confirmHold                  | Boolean        | `false`             |          | Specifies whether the keyboard is not hidden when the lower-right button on the keyboard is tapped.                                                                                                            |
| cursor                       | Number         |                     |          | Specifies the cursor position during focusing.                                                                                                                                                                 |
| selectionStart               | Number         | `-1`                |          | The start position of the cursor. It takes effect only during auto focusing, and needs to used with selection-end.                                                                                             |
| selectionEnd                 | Number         | `-1`                |          | The end position of the cursor. It takes effect only during auto focusing, and needs to used with selection-start.                                                                                             |
| adjustPosition               | Boolean        | `true`              |          | Specifies whether to automatically push up the page when the keyboard is displayed.                                                                                                                            |
| holdKeyboard                 | Boolean        | `false`             |          | Specifies whether to hide the keyboard when clicking page while the input is focused.                                                                                                                          |
| onInput                      | Event handler  |                     |          | Triggered when the user taps the keyboard. `event.detail = { value, cursor, keyCode }`, where keyCode is the key value.box.                                                                                    |
| onFocus                      | Event handler  |                     |          | Triggered when the input box is focused. `event.detail = { value, height }`, where height is the height of the keyboard.                                                                                       |
| onBlur                       | Event handler  |                     |          | Triggered when the input box is unfocused. `event.detail = { value }`.                                                                                                                                         |
| onConfirm                    | Event handler  |                     |          | Triggered when the Done button is tapped. `event.detail = { value }`.                                                                                                                                          |
| onKeyboardHeightChange       | Event handler  |                     |          | Triggered when the height of the keyboard changes. `event.detail = { height, duration}`.                                                                                                                       |
| autoFill                     | String         |                     |          | 'username', 'password', 'newPassword', 'oneTime2FA', 'oneTimeEmail', 'oneTimeSMS', 'none'                                                                                                                      |
| showConfirmBar               | Boolean        | `false`             |          | Specifies whether to display the bar containing the `Done` button above the keyboard.                                                                                                                          |
| keyboardAccessoryItems       | String[]       |                     |          | The array of keyboard accessory items, the items'length must be 2-5                                                                                                                                            |
| onKeyboardAccessoryItemClick | Event handler  |                     |          | Triggered when the accessory item is clicked. `event.detail = { index }`.                                                                                                                                      |

### Valid values of `type`

| Value    | Description                        |
| -------- | ---------------------------------- |
| `text`   | Keyboard for text input.           |
| `number` | Keyboard for number input.         |
| `digit`  | Numeric keypad with decimal point. |

### Valid values of `confirm-type`

| Value    | Description                                                    |
| -------- | -------------------------------------------------------------- |
| `send`   | Indicates that the button in the lower right corner is Send.   |
| `search` | Indicates that the button in the lower right corner is Search. |
| `next`   | Indicates that the button in the lower right corner is Next.   |
| `go`     | Indicates that the button in the lower right corner is GO.     |
| `done`   | Indicates that the button in the lower right corner is Done.   |

#### open-type Legal value

| Value   | Description                |
| ------- | -------------------------- |
| `share` | Trigger the user to share. |

**Example**

js

```js
Page({
  data: {
    inputValue: "",
  },
  bindKeyInput: function (e) {
    this.setData({
      inputValue: e.detail.value,
    });
  },
});
```

bxml

```html
<theme-context>
  <view class="container">
    <view>Auto focus input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input auto-focus placeholder="Auto focus" />
        </view>
      </view>
    </view>

    <view>The maximum length input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input maxlength="10" placeholder="The maximum length is 10" />
        </view>
      </view>
    </view>

    <view>get input value：{{inputValue}}</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input maxlength="10" bindinput="bindKeyInput" placeholder="please input the value" />
        </view>
      </view>
    </view>

    <view>number input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input type="number" placeholder="number input" />
        </view>
      </view>
    </view>

    <view>password input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input type="password" placeholder="password input" />
        </view>
      </view>
    </view>

    <view>digit input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input type="digit" placeholder="digit input" />
        </view>
      </view>
    </view>

    <view>An input that controls the color of the placeholder</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input placeholder-style="color:#F76260" placeholder="placeholder font is red" />
        </view>
      </view>
    </view>
  </view>
</theme-context>
```

### bug & tips

- `tip`: if developer need change the caret-color of input component, developer should use css class
  to set it instead of inline style
- `tip`: keyboardAccessoryItems's length must be 2-5 , otherwise the ui will be abnormal , and the
  onKeyboardAccessoryItemClick can listen the click event of the accessory item

---

# input

## Props

| Property                     | Type           | Default Value       | Required | Description                                                                                                                                                                                                    |
| ---------------------------- | -------------- | ------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value                        | String, Number |                     |          | The initial content in the input box.                                                                                                                                                                          |
| type                         | String         | `text`              |          | The type of input.                                                                                                                                                                                             |
| password                     | Boolean        | `false`             |          | Specifies whether the input is password-type content.                                                                                                                                                          |
| placeholder                  | String         |                     |          | The placeholder used when the input box is empty.                                                                                                                                                              |
| placeholderStyle             | String         |                     |          | Specifies the style of the placeholder.                                                                                                                                                                        |
| placeholderClass             | String         | `input-placeholder` |          | Specifies the style class of the placeholder.                                                                                                                                                                  |
| disabled                     | Boolean        | `false`             |          | Specifies whether to disable the component.                                                                                                                                                                    |
| maxlength                    | Number         | `140`               |          | The maximum length. When it is set to `-1`, the maximum length is not limited.                                                                                                                                 |
| cursorSpacing                | Number         | `0`                 |          | Specifies the distance between the cursor and the keyboard. It is either the distance between the input box and the bottom of the screen or the distance specified via `cursorSpacing`, whichever is smaller.. |
| autoFocus                    | Boolean        | `false`             |          | (Will be discarded soon. Use the focus instead.) Auto focus. The keyboard is automatically displayed.                                                                                                          |
| focus                        | Boolean        | `false`             |          | Gets focus.                                                                                                                                                                                                    |
| confirmType                  | String         | `done`              |          | Sets the text on the lower-right button on the keyboard. It takes effect only when type='text'.                                                                                                                |
| confirmHold                  | Boolean        | `false`             |          | Specifies whether the keyboard is not hidden when the lower-right button on the keyboard is tapped.                                                                                                            |
| cursor                       | Number         |                     |          | Specifies the cursor position during focusing.                                                                                                                                                                 |
| selectionStart               | Number         | `-1`                |          | The start position of the cursor. It takes effect only during auto focusing, and needs to used with selection-end.                                                                                             |
| selectionEnd                 | Number         | `-1`                |          | The end position of the cursor. It takes effect only during auto focusing, and needs to used with selection-start.                                                                                             |
| adjustPosition               | Boolean        | `true`              |          | Specifies whether to automatically push up the page when the keyboard is displayed.                                                                                                                            |
| holdKeyboard                 | Boolean        | `false`             |          | Specifies whether to hide the keyboard when clicking page while the input is focused.                                                                                                                          |
| onInput                      | Event handler  |                     |          | Triggered when the user taps the keyboard. `event.detail = { value, cursor, keyCode }`, where keyCode is the key value.box.                                                                                    |
| onFocus                      | Event handler  |                     |          | Triggered when the input box is focused. `event.detail = { value, height }`, where height is the height of the keyboard.                                                                                       |
| onBlur                       | Event handler  |                     |          | Triggered when the input box is unfocused. `event.detail = { value }`.                                                                                                                                         |
| onConfirm                    | Event handler  |                     |          | Triggered when the Done button is tapped. `event.detail = { value }`.                                                                                                                                          |
| onKeyboardHeightChange       | Event handler  |                     |          | Triggered when the height of the keyboard changes. `event.detail = { height, duration}`.                                                                                                                       |
| autoFill                     | String         |                     |          | 'username', 'password', 'newPassword', 'oneTime2FA', 'oneTimeEmail', 'oneTimeSMS', 'none'                                                                                                                      |
| showConfirmBar               | Boolean        | `false`             |          | Specifies whether to display the bar containing the `Done` button above the keyboard.                                                                                                                          |
| keyboardAccessoryItems       | String[]       |                     |          | The array of keyboard accessory items, the items'length must be 2-5                                                                                                                                            |
| onKeyboardAccessoryItemClick | Event handler  |                     |          | Triggered when the accessory item is clicked. `event.detail = { index }`.                                                                                                                                      |

### Valid values of `type`

| Value    | Description                        |
| -------- | ---------------------------------- |
| `text`   | Keyboard for text input.           |
| `number` | Keyboard for number input.         |
| `digit`  | Numeric keypad with decimal point. |

### Valid values of `confirm-type`

| Value    | Description                                                    |
| -------- | -------------------------------------------------------------- |
| `send`   | Indicates that the button in the lower right corner is Send.   |
| `search` | Indicates that the button in the lower right corner is Search. |
| `next`   | Indicates that the button in the lower right corner is Next.   |
| `go`     | Indicates that the button in the lower right corner is GO.     |
| `done`   | Indicates that the button in the lower right corner is Done.   |

#### open-type Legal value

| Value   | Description                |
| ------- | -------------------------- |
| `share` | Trigger the user to share. |

**Example**

js

```js
Page({
  data: {
    inputValue: "",
  },
  bindKeyInput: function (e) {
    this.setData({
      inputValue: e.detail.value,
    });
  },
});
```

bxml

```html
<theme-context>
  <view class="container">
    <view>Auto focus input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input auto-focus placeholder="Auto focus" />
        </view>
      </view>
    </view>

    <view>The maximum length input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input maxlength="10" placeholder="The maximum length is 10" />
        </view>
      </view>
    </view>

    <view>get input value：{{inputValue}}</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input maxlength="10" bindinput="bindKeyInput" placeholder="please input the value" />
        </view>
      </view>
    </view>

    <view>number input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input type="number" placeholder="number input" />
        </view>
      </view>
    </view>

    <view>password input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input type="password" placeholder="password input" />
        </view>
      </view>
    </view>

    <view>digit input</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input type="digit" placeholder="digit input" />
        </view>
      </view>
    </view>

    <view>An input that controls the color of the placeholder</view>
    <view class="bnui-cells bnui-cells_after-title">
      <view class="bnui-cell bnui-cell_input">
        <view class="bnui-cell__bd">
          <input placeholder-style="color:#F76260" placeholder="placeholder font is red" />
        </view>
      </view>
    </view>
  </view>
</theme-context>
```

### bug & tips

- `tip`: if developer need change the caret-color of input component, developer should use css class
  to set it instead of inline style
- `tip`: keyboardAccessoryItems's length must be 2-5 , otherwise the ui will be abnormal , and the
  onKeyboardAccessoryItemClick can listen the click event of the accessory item