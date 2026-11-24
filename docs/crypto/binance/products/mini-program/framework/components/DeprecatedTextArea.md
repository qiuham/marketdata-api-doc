---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/DeprecatedTextArea
api_type: Guide
updated_at: 2026-11-24 18:43:30.254127
---

# TextArea

Multiline input box. This component is Native component, please note the limitations.

**Example**

```js
Page({
  data: {
    textareaValue: "controlled",
    inputValue3: "",
    lineCount: 0,
    inputValue4: "1234567890",
    inputValue5: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    confirmType: 5,
    confirmTypes: ["send", "search", "next", "go", "done", "return"],
  },
  onLoad(query) {
    console.log("onload", this, query);
  },
  onShow() {
    console.log(`[LifeCycle][Textarea] useEffect`);
  },
  onReady() {
    console.log(`[LifeCycle][Textarea] useReady`);
  },
  onHide() {
    console.log(`[LifeCycle][Textarea] useDidHide`);
  },
  onTextareaValueInput(e) {
    this.setData({
      textareaValue: e.detail.value,
    });
    console.log(`[onTextareaValueInput] textarea`, e);
  },
  onInputValue3Click(e) {
    this.setData({
      inputValue3: e.detail.value,
    });
    console.log("[Textarea] Click", e);
  },
  onInputValue4Input(e) {
    this.setData({
      inputValue4: e.detail.value,
    });
    console.log(`[onInputValue4Input] textarea`, e);
  },
  onInputValue4Focus(e) {
    console.log("[Textarea] bindfocus", e);
  },
  onInputValue4Blur(e) {
    console.log("[Textarea] bindblur", e);
  },
  onInputValue4Click(e) {
    console.log("[Textarea] Click", e);
  },
  onInputValue4Longpress(e) {
    console.log("[Textarea] longpress", e);
  },
  onInputValue4Confirm(e) {
    console.log("[Textarea] bindconfirm", e);
  },
  onInputValue4KeyboardHeightChange(e) {
    console.log("[Textarea] bindkeyboardheightchange", e);
  },
  onInputValue4LineChange(e) {
    console.log("[Textarea] bindlinechange", e);
  },
  onLineCountLineChange(e) {
    console.log("[Textarea] bindlinechange", e);
    this.setData({
      lineCount: e.detail.lineCount,
    });
  },
  onInputValue5Input(e) {
    this.setData({
      inputValue5: e.detail.value,
    });
    console.log(`[onInputValue5Input] textarea`, e);
  },
  onConfirmTypeChange(e) {
    this.setData({
      confirmType: e.detail.value === "string" ? parseInt(e.detail.value) : e.detail.value,
    });
  },
});
```

**Bug & Tip**

- `tip`: textarea of blur The event will be later than the tap Event, if needed in the button Click
  event acquisition textarea, can be used form of bindsubmit。
- `tip`: Modifying user input over multiple lines of text is not recommended, so textarea of
  bindinput Handler does not reflect the return value to the textarea Up.
- `tip` : If the keyboard height changes, the keyboardheightchange event may be triggered multiple
  times. Developers should ignore the same height value

## Props

| Name                | Type                                       | Description                                                                              | Default  |
| ------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------- | -------- |
| `value`             | `string`                                   | Enter the contents of the box                                                            |          |
| `placeholder`       | `string`                                   | Placeholder when input box is empty                                                      |          |
| `disabled`          | `boolean`                                  | Is it disabled?                                                                          | `false`  |
| `maxlength`         | `number`                                   | Maximum input length, set to -1 Does not limit the maximum length                        | `140`    |
| `auto-focus`        | `boolean`                                  | Autofocus, pull up the keyboard.                                                         | `false`  |
| `focus`             | `boolean`                                  | Getting focus                                                                            | `false`  |
| `placeholder-class` | `string`                                   | Custom class name for placeholder jssdk > 4.33.0                                         |          |
| `force`             | `boolean`                                  | whether to force update the value of the textarea, default is false                      | `false`  |
| `auto-height`       | `boolean`                                  | whether to update the height of the textarea automaticly text overflow, default is false | `false`  |
| `autocapitalize`    | `TextareaHTMLAttributes['autocapitalize']` |                                                                                          | `"none"` |
| `autocorrect`       | `TextareaHTMLAttributes['autocorrect']`    | https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/autocorrect#on       | `"off"`  |

## Events

| Name               | Description                                                                                                                                                                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindinput`        | When keyboard input, triggers input Event, event.detail = {value, cursor, keyCode}, keyCode Is a key value and currently the tool does not support returning keyCode parameters. bindinput The return value of the handler is not reflected in the textarea on |
| `bindinputcapture` | Trigger when textarea input event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                       |
| `bindfocus`        | `bindfocus` Triggered when input box is focused,<br/>**Arguments**<br/><ul><li>**`detail:  value: string, height: number `** — height For keyboard height</li></ul>                                                                                            |
| `bindfocuscapture` | Trigger when textarea focus event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                       |
| `bindblur`         | Triggered when the input box loses focus, event. detail = {value, cursor}                                                                                                                                                                                      |
| `bindblurcapture`  | Trigger when textarea focus event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                       |
| `bindlinechange`   | Called when the number of lines in the input box changes,<br/>**Arguments**<br/><ul><li>**`event:  detail: Object `** — detail = {height: 0, heightRpx: 0, lineCount: 0}</li></ul>                                                                             |

---

# TextArea

Multiline input box. This component is Native component, please note the limitations.

**Example**

```js
Page({
  data: {
    textareaValue: "controlled",
    inputValue3: "",
    lineCount: 0,
    inputValue4: "1234567890",
    inputValue5: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    confirmType: 5,
    confirmTypes: ["send", "search", "next", "go", "done", "return"],
  },
  onLoad(query) {
    console.log("onload", this, query);
  },
  onShow() {
    console.log(`[LifeCycle][Textarea] useEffect`);
  },
  onReady() {
    console.log(`[LifeCycle][Textarea] useReady`);
  },
  onHide() {
    console.log(`[LifeCycle][Textarea] useDidHide`);
  },
  onTextareaValueInput(e) {
    this.setData({
      textareaValue: e.detail.value,
    });
    console.log(`[onTextareaValueInput] textarea`, e);
  },
  onInputValue3Click(e) {
    this.setData({
      inputValue3: e.detail.value,
    });
    console.log("[Textarea] Click", e);
  },
  onInputValue4Input(e) {
    this.setData({
      inputValue4: e.detail.value,
    });
    console.log(`[onInputValue4Input] textarea`, e);
  },
  onInputValue4Focus(e) {
    console.log("[Textarea] bindfocus", e);
  },
  onInputValue4Blur(e) {
    console.log("[Textarea] bindblur", e);
  },
  onInputValue4Click(e) {
    console.log("[Textarea] Click", e);
  },
  onInputValue4Longpress(e) {
    console.log("[Textarea] longpress", e);
  },
  onInputValue4Confirm(e) {
    console.log("[Textarea] bindconfirm", e);
  },
  onInputValue4KeyboardHeightChange(e) {
    console.log("[Textarea] bindkeyboardheightchange", e);
  },
  onInputValue4LineChange(e) {
    console.log("[Textarea] bindlinechange", e);
  },
  onLineCountLineChange(e) {
    console.log("[Textarea] bindlinechange", e);
    this.setData({
      lineCount: e.detail.lineCount,
    });
  },
  onInputValue5Input(e) {
    this.setData({
      inputValue5: e.detail.value,
    });
    console.log(`[onInputValue5Input] textarea`, e);
  },
  onConfirmTypeChange(e) {
    this.setData({
      confirmType: e.detail.value === "string" ? parseInt(e.detail.value) : e.detail.value,
    });
  },
});
```

**Bug & Tip**

- `tip`: textarea of blur The event will be later than the tap Event, if needed in the button Click
  event acquisition textarea, can be used form of bindsubmit。
- `tip`: Modifying user input over multiple lines of text is not recommended, so textarea of
  bindinput Handler does not reflect the return value to the textarea Up.
- `tip` : If the keyboard height changes, the keyboardheightchange event may be triggered multiple
  times. Developers should ignore the same height value

## Props

| Name                | Type                                       | Description                                                                              | Default  |
| ------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------- | -------- |
| `value`             | `string`                                   | Enter the contents of the box                                                            |          |
| `placeholder`       | `string`                                   | Placeholder when input box is empty                                                      |          |
| `disabled`          | `boolean`                                  | Is it disabled?                                                                          | `false`  |
| `maxlength`         | `number`                                   | Maximum input length, set to -1 Does not limit the maximum length                        | `140`    |
| `auto-focus`        | `boolean`                                  | Autofocus, pull up the keyboard.                                                         | `false`  |
| `focus`             | `boolean`                                  | Getting focus                                                                            | `false`  |
| `placeholder-class` | `string`                                   | Custom class name for placeholder jssdk > 4.33.0                                         |          |
| `force`             | `boolean`                                  | whether to force update the value of the textarea, default is false                      | `false`  |
| `auto-height`       | `boolean`                                  | whether to update the height of the textarea automaticly text overflow, default is false | `false`  |
| `autocapitalize`    | `TextareaHTMLAttributes['autocapitalize']` |                                                                                          | `"none"` |
| `autocorrect`       | `TextareaHTMLAttributes['autocorrect']`    | https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/autocorrect#on       | `"off"`  |

## Events

| Name               | Description                                                                                                                                                                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindinput`        | When keyboard input, triggers input Event, event.detail = {value, cursor, keyCode}, keyCode Is a key value and currently the tool does not support returning keyCode parameters. bindinput The return value of the handler is not reflected in the textarea on |
| `bindinputcapture` | Trigger when textarea input event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                       |
| `bindfocus`        | `bindfocus` Triggered when input box is focused,<br/>**Arguments**<br/><ul><li>**`detail:  value: string, height: number `** — height For keyboard height</li></ul>                                                                                            |
| `bindfocuscapture` | Trigger when textarea focus event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                       |
| `bindblur`         | Triggered when the input box loses focus, event. detail = {value, cursor}                                                                                                                                                                                      |
| `bindblurcapture`  | Trigger when textarea focus event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/)                                                                                                                                       |
| `bindlinechange`   | Called when the number of lines in the input box changes,<br/>**Arguments**<br/><ul><li>**`event:  detail: Object `** — detail = {height: 0, heightRpx: 0, lineCount: 0}</li></ul>                                                                             |