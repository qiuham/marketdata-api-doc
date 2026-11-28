---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/DeprecatedInput
api_type: Guide
updated_at: 2026-11-28 18:41:50.015170
---

# Input

A container that hosts web pages. Will automatically cover the entire Mini Program page,**Personal
type Mini Program is not supported for the time being.**

**Example**

```html
<deprecated-input placeholder="welcome to binance" />
```

**Bug & Tip**

- `tip`: input Component is a native component, the font is the system font, so cannot be set
  font-family
- `tip`: in input During focusing, avoid using css animation
- `tip`: For input Is encapsulated in a custom component, and form Outside the custom component,
  form You will not be able to get the input Value of. You need to use the custom component s
  built-in behaviors wx://form-field

## Props

| Name          | Type                     | Description                                                                                            | Default  |
| ------------- | ------------------------ | ------------------------------------------------------------------------------------------------------ | -------- |
| `value`       | `string` &#124; `number` | The initial content of the input box                                                                   |          |
| `type`        | `Type`                   | input Type: 'text' or 'number'                                                                         | `"text"` |
| `password`    | `boolean`                | Is it a password type?                                                                                 | `false`  |
| `placeholder` | `string`                 | Placeholder when input box is empty                                                                    |          |
| `disabled`    | `boolean`                | Is it disabled?                                                                                        | `false`  |
| `maxlength`   | `number`                 | Maximum input length, set to -1 Does not limit the maximum length                                      | `140`    |
| `auto-focus`  | `boolean`                | (Soon to be abandoned, please use directly focus ) Auto focus, pull up the keyboard                    | `false`  |
| `focus`       | `boolean`                | Getting focus                                                                                          | `false`  |
| `manual`      | `boolean`                | If manual is true, you can only change input value by `e.control({value: string})` in `onChange` event | `false`  |
| `pattern`     | `string`                 | Regular expression for input content verification                                                      |          |
| `inputmode`   | `string`                 | Keyboard input type, valid values are: none, text, decimal, numeric, tel, search, email, url           | &nbsp;   |

## Events

| Name                | Description                                                                                                                                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindinput`         | Triggered when keyboard input,<br/>**Arguments**<br/><ul><li>**`event:  detail: Object `**</li><li>**`detail.value:  string `**</li><li>**`detail.cursor:  number `**</li><li>**`detail.keyCode:  number `** — The key code in keyboard</li></ul>         |
| `bindinput-capture` | Trigger when input input event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                     |
| `bindfocus`         | Triggered when input box is focused,<br/>**Arguments**<br/><ul><li>**`event:  detail: Object `** — The event object</li><li>**`detail.height:  number`** — height for keyboard height</li><li>**`detail.value:  string `** — The value of input</li></ul> |
| `bindfocuscapture`  | Trigger when input focus event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                     |
| `bindblur`          | Triggered when the input box loses focus, event. detail = { value, encryptedValue, encryptError }                                                                                                                                                         |
| `bindblurcapture`   | Trigger when input blur event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                      |
| `bindconfirm`       | Triggered when the Finish on is clicked, event.detail = { value }                                                                                                                                                                                         |

---

# Input

A container that hosts web pages. Will automatically cover the entire Mini Program page,**Personal
type Mini Program is not supported for the time being.**

**Example**

```html
<deprecated-input placeholder="welcome to binance" />
```

**Bug & Tip**

- `tip`: input Component is a native component, the font is the system font, so cannot be set
  font-family
- `tip`: in input During focusing, avoid using css animation
- `tip`: For input Is encapsulated in a custom component, and form Outside the custom component,
  form You will not be able to get the input Value of. You need to use the custom component s
  built-in behaviors wx://form-field

## Props

| Name          | Type                     | Description                                                                                            | Default  |
| ------------- | ------------------------ | ------------------------------------------------------------------------------------------------------ | -------- |
| `value`       | `string` &#124; `number` | The initial content of the input box                                                                   |          |
| `type`        | `Type`                   | input Type: 'text' or 'number'                                                                         | `"text"` |
| `password`    | `boolean`                | Is it a password type?                                                                                 | `false`  |
| `placeholder` | `string`                 | Placeholder when input box is empty                                                                    |          |
| `disabled`    | `boolean`                | Is it disabled?                                                                                        | `false`  |
| `maxlength`   | `number`                 | Maximum input length, set to -1 Does not limit the maximum length                                      | `140`    |
| `auto-focus`  | `boolean`                | (Soon to be abandoned, please use directly focus ) Auto focus, pull up the keyboard                    | `false`  |
| `focus`       | `boolean`                | Getting focus                                                                                          | `false`  |
| `manual`      | `boolean`                | If manual is true, you can only change input value by `e.control({value: string})` in `onChange` event | `false`  |
| `pattern`     | `string`                 | Regular expression for input content verification                                                      |          |
| `inputmode`   | `string`                 | Keyboard input type, valid values are: none, text, decimal, numeric, tel, search, email, url           | &nbsp;   |

## Events

| Name                | Description                                                                                                                                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindinput`         | Triggered when keyboard input,<br/>**Arguments**<br/><ul><li>**`event:  detail: Object `**</li><li>**`detail.value:  string `**</li><li>**`detail.cursor:  number `**</li><li>**`detail.keyCode:  number `** — The key code in keyboard</li></ul>         |
| `bindinput-capture` | Trigger when input input event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                     |
| `bindfocus`         | Triggered when input box is focused,<br/>**Arguments**<br/><ul><li>**`event:  detail: Object `** — The event object</li><li>**`detail.height:  number`** — height for keyboard height</li><li>**`detail.value:  string `** — The value of input</li></ul> |
| `bindfocuscapture`  | Trigger when input focus event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                     |
| `bindblur`          | Triggered when the input box loses focus, event. detail = { value, encryptedValue, encryptError }                                                                                                                                                         |
| `bindblurcapture`   | Trigger when input blur event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                      |
| `bindconfirm`       | Triggered when the Finish on is clicked, event.detail = { value }                                                                                                                                                                                         |