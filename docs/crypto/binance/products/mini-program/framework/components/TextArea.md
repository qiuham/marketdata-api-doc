---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/TextArea
api_type: Guide
updated_at: 2026-11-18 18:41:25.612494
---

# textarea

## Props

| Property                     | Type          | Default Value          | Required | Description                                                                                                                                                                                                |
| ---------------------------- | ------------- | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value                        | String        |                        |          | The initial content in the input box.                                                                                                                                                                      |
| placeholder                  | String        |                        |          | The placeholder used when the input box is empty.                                                                                                                                                          |
| placeholderStyle             | String        |                        |          | Specifies the style of the placeholder. Only color, font-size, and font-weight styles are supported.                                                                                                       |
| placeholderClass             | String        | `textarea-placeholder` |          | Specifies the style class of the placeholder.                                                                                                                                                              |
| disabled                     | Boolean       | `false`                |          | Specifies whether to disable the component.                                                                                                                                                                |
| maxlength                    | Number        | `140`                  |          | The maximum length. When it is set to `-1`, the maximum length is not limited.                                                                                                                             |
| autoFocus                    | Boolean       | `false`                |          | (Will be discarded soon. Use the focus instead.) Auto focus. The keyboard is automatically displayed.                                                                                                      |
| focus                        | Boolean       | `false`                |          | Gets focus.                                                                                                                                                                                                |
| autoHeight                   | Boolean       | `false`                |          | Specifies whether the height automatically increases. If this property is specified, style.height does not take effect.                                                                                    |
| fixed                        | Boolean       | `false`                |          | If the textarea is in an area of `position:fixed`, the value of the specified property should always be true.                                                                                              |
| cursorSpacing                | Number        | `0`                    |          | Specifies the distance between the cursor and the keyboard. It is either the distance between `textarea` and the bottom of the screen or the distance specified via `cursorSpacing`, whichever is smaller. |
| cursor                       | Number        | `-1`                   |          | Specifies the cursor position during focusing.                                                                                                                                                             |
| showConfirmBar               | Boolean       | `true`                 |          | Specifies whether to display the bar containing the `Done` button above the keyboard.                                                                                                                      |
| selectionStart               | Number        | `-1`                   |          | The start position of the cursor. It takes effect only during auto focusing, and needs to used with selection-end.                                                                                         |
| selectionEnd                 | Number        | `-1`                   |          | The end position of the cursor. It takes effect only during auto focusing, and needs to used with selection-start.                                                                                         |
| adjustPosition               | Boolean       | `true`                 |          | Specifies whether to automatically push up the page when the keyboard is displayed.                                                                                                                        |
| holdKeyboard                 | Boolean       | `false`                |          | Specifies whether to hide the keyboard when clicking page while the input is focused.                                                                                                                      |
| disableDefaultPadding        | Boolean       | `false`                |          | Specifies whether to remove the default padding behavior on iOS.                                                                                                                                           |
| confirmType                  | String        | `return`               |          | Sets the text on the lower-right button on the keyboard. It takes effect only when type='text'.                                                                                                            |
| confirmHold                  | Boolean       | `false`                |          | Specifies whether the keyboard is not hidden when the lower-right button on the keyboard is tapped.                                                                                                        |
| onInput                      | Event handler |                        |          | Triggered when the user taps the keyboard. `event.detail = { value, cursor, keyCode }`, where keyCode is the key value.box.                                                                                |
| onFocus                      | Event handler |                        |          | Triggered when the input box is focused. `event.detail = { value, height }`                                                                                                                                |
| onBlur                       | Event handler |                        |          | Triggered when the input box is unfocused. `event.detail = { value, cursor }`.                                                                                                                             |
| onLineChange                 | Event handler |                        |          | Called when the number of lines in the input box changes. `event.detail = { height: number, heightRpx: number, lineCount: number }`                                                                        |
| onConfirm                    | Event handler |                        |          | Triggered when the Done button is tapped. `event.detail = { value }`.                                                                                                                                      |
| onKeyboardHeightChange       | Event handler |                        |          | Triggered when the height of the keyboard changes. `event.detail = { height, duration}`.                                                                                                                   |
| keyboardAccessoryItems       | String[]      |                        |          | The array of keyboard accessory items, the items'length must be 2-5                                                                                                                                        |
| onKeyboardAccessoryItemClick | Event handler |                        |          | Triggered when the accessory item is clicked. `event.detail = { index }`.                                                                                                                                  |

#### Valid values of `confirm-type`

| Value    | Description                                                    |
| -------- | -------------------------------------------------------------- |
| `send`   | Indicates that the button in the lower right corner is Send.   |
| `search` | Indicates that the button in the lower right corner is Search. |
| `next`   | Indicates that the button in the lower right corner is Next.   |
| `go`     | Indicates that the button in the lower right corner is GO.     |
| `done`   | Indicates that the button in the lower right corner is Done.   |
| `return` | Indicates that the button in the lower right corner is Return. |

### bug & tips

- `tip`: if developer need change the caret-color of input component, developer should use css class
  to set it instead of inline style
- `tip`: keyboardAccessoryItems's length must be 2-5 , otherwise the ui will be abnormal , and the
  onKeyboardAccessoryItemClick can listen the click event of the accessory item

**Example**

```html
<!-- bxml -->
<textarea class="caret-color-red"></textarea>
<!-- css class -->
<style>
  .caret-color-red {
    caret-color: red;
  }
</style>
```

---

# textarea

## Props

| Property                     | Type          | Default Value          | Required | Description                                                                                                                                                                                                |
| ---------------------------- | ------------- | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value                        | String        |                        |          | The initial content in the input box.                                                                                                                                                                      |
| placeholder                  | String        |                        |          | The placeholder used when the input box is empty.                                                                                                                                                          |
| placeholderStyle             | String        |                        |          | Specifies the style of the placeholder. Only color, font-size, and font-weight styles are supported.                                                                                                       |
| placeholderClass             | String        | `textarea-placeholder` |          | Specifies the style class of the placeholder.                                                                                                                                                              |
| disabled                     | Boolean       | `false`                |          | Specifies whether to disable the component.                                                                                                                                                                |
| maxlength                    | Number        | `140`                  |          | The maximum length. When it is set to `-1`, the maximum length is not limited.                                                                                                                             |
| autoFocus                    | Boolean       | `false`                |          | (Will be discarded soon. Use the focus instead.) Auto focus. The keyboard is automatically displayed.                                                                                                      |
| focus                        | Boolean       | `false`                |          | Gets focus.                                                                                                                                                                                                |
| autoHeight                   | Boolean       | `false`                |          | Specifies whether the height automatically increases. If this property is specified, style.height does not take effect.                                                                                    |
| fixed                        | Boolean       | `false`                |          | If the textarea is in an area of `position:fixed`, the value of the specified property should always be true.                                                                                              |
| cursorSpacing                | Number        | `0`                    |          | Specifies the distance between the cursor and the keyboard. It is either the distance between `textarea` and the bottom of the screen or the distance specified via `cursorSpacing`, whichever is smaller. |
| cursor                       | Number        | `-1`                   |          | Specifies the cursor position during focusing.                                                                                                                                                             |
| showConfirmBar               | Boolean       | `true`                 |          | Specifies whether to display the bar containing the `Done` button above the keyboard.                                                                                                                      |
| selectionStart               | Number        | `-1`                   |          | The start position of the cursor. It takes effect only during auto focusing, and needs to used with selection-end.                                                                                         |
| selectionEnd                 | Number        | `-1`                   |          | The end position of the cursor. It takes effect only during auto focusing, and needs to used with selection-start.                                                                                         |
| adjustPosition               | Boolean       | `true`                 |          | Specifies whether to automatically push up the page when the keyboard is displayed.                                                                                                                        |
| holdKeyboard                 | Boolean       | `false`                |          | Specifies whether to hide the keyboard when clicking page while the input is focused.                                                                                                                      |
| disableDefaultPadding        | Boolean       | `false`                |          | Specifies whether to remove the default padding behavior on iOS.                                                                                                                                           |
| confirmType                  | String        | `return`               |          | Sets the text on the lower-right button on the keyboard. It takes effect only when type='text'.                                                                                                            |
| confirmHold                  | Boolean       | `false`                |          | Specifies whether the keyboard is not hidden when the lower-right button on the keyboard is tapped.                                                                                                        |
| onInput                      | Event handler |                        |          | Triggered when the user taps the keyboard. `event.detail = { value, cursor, keyCode }`, where keyCode is the key value.box.                                                                                |
| onFocus                      | Event handler |                        |          | Triggered when the input box is focused. `event.detail = { value, height }`                                                                                                                                |
| onBlur                       | Event handler |                        |          | Triggered when the input box is unfocused. `event.detail = { value, cursor }`.                                                                                                                             |
| onLineChange                 | Event handler |                        |          | Called when the number of lines in the input box changes. `event.detail = { height: number, heightRpx: number, lineCount: number }`                                                                        |
| onConfirm                    | Event handler |                        |          | Triggered when the Done button is tapped. `event.detail = { value }`.                                                                                                                                      |
| onKeyboardHeightChange       | Event handler |                        |          | Triggered when the height of the keyboard changes. `event.detail = { height, duration}`.                                                                                                                   |
| keyboardAccessoryItems       | String[]      |                        |          | The array of keyboard accessory items, the items'length must be 2-5                                                                                                                                        |
| onKeyboardAccessoryItemClick | Event handler |                        |          | Triggered when the accessory item is clicked. `event.detail = { index }`.                                                                                                                                  |

#### Valid values of `confirm-type`

| Value    | Description                                                    |
| -------- | -------------------------------------------------------------- |
| `send`   | Indicates that the button in the lower right corner is Send.   |
| `search` | Indicates that the button in the lower right corner is Search. |
| `next`   | Indicates that the button in the lower right corner is Next.   |
| `go`     | Indicates that the button in the lower right corner is GO.     |
| `done`   | Indicates that the button in the lower right corner is Done.   |
| `return` | Indicates that the button in the lower right corner is Return. |

### bug & tips

- `tip`: if developer need change the caret-color of input component, developer should use css class
  to set it instead of inline style
- `tip`: keyboardAccessoryItems's length must be 2-5 , otherwise the ui will be abnormal , and the
  onKeyboardAccessoryItemClick can listen the click event of the accessory item

**Example**

```html
<!-- bxml -->
<textarea class="caret-color-red"></textarea>
<!-- css class -->
<style>
  .caret-color-red {
    caret-color: red;
  }
</style>
```