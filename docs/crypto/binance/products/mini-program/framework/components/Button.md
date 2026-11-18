---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Button
api_type: Guide
updated_at: 2026-11-18 02:33:05.377039
---

# Button

Button.

**Example**

js

```js
const types = ["default", "primary", "warn"];
const pageObject = {
  data: {
    defaultSize: "default",
    primarySize: "default",
    warnSize: "default",
    disabled: false,
    plain: false,
    loading: false,
  },

  onShareAppMessage() {
    return {
      title: "button",
      path: "page/component/pages/button/button",
    };
  },

  setDisabled() {
    this.setData({
      disabled: !this.data.disabled,
    });
  },

  setPlain() {
    this.setData({
      plain: !this.data.plain,
    });
  },

  setLoading() {
    this.setData({
      loading: !this.data.loading,
    });
  },

  handleContact(e) {
    console.log(e.detail);
  },

  handleGetPhoneNumber(e) {
    console.log(e.detail);
  },

  handleGetUserInfo(e) {
    console.log(e.detail);
  },

  handleOpenSetting(e) {
    console.log(e.detail.authSetting);
  },

  handleGetUserInfo(e) {
    console.log(e.detail.userInfo);
  },
};

for (let i = 0; i < types.length; ++i) {
  (function (type) {
    pageObject[type] = function () {
      const key = type + "Size";
      const changedData = {};
      changedData[key] = this.data[key] === "default" ? "mini" : "default";
      this.setData(changedData);
    };
  })(types[i]);
}

Page(pageObject);
```

bxml

```html
<view class="page-body">
  <view class="btn-area" id="buttonContainer">
    <button type="primary">Page Main Normal</button>
    <button type="primary" loading="true">Page Main Loading</button>
    <button type="primary" disabled="true">Page Main Disabled</button>

    <button type="default">Page Second Normal</button>
    <button type="default" disabled="true">Page Second Disabled</button>

    <button type="warn">Warn Normal</button>
    <button type="warn" disabled="true">Warn Disabled</button>

    <view class="button-sp-area">
      <button type="primary" plain="true">Button</button>
      <button type="primary" disabled="true" plain="true">Disable Button</button>

      <button type="default" plain="true"></button>
      <button type="default" disabled="true" plain="true">Button</button>

      <button class="mini-btn" type="primary" size="mini">Button</button>
      <button class="mini-btn" type="default" size="mini">Button</button>
      <button class="mini-btn" type="warn" size="mini">Button</button>
    </view>
  </view>
</view>
```

bxss

```css
button {
  margin-top: 30rpx;
  margin-bottom: 30rpx;
}
.button-sp-area {
  margin: 0 auto;
  width: 60%;
}
.mini-btn {
  margin-right: 10rpx;
}
```

**Bug & Tip**

- `tip`: button-hover Default is{background-color: rgba(0, 0, 0, 0.1) opacity: 0.7}
- `tip`: Currently set form-type of button Object in the current component form Effective. Thus,
  will button Is encapsulated in a custom component, and form In addition to the custom component,
  the button of form-type Failure.

## Props

| Name                     | Type       | Description                                                                                                   | Default          |
| ------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------- | ---------------- |
| `size`                   | `string`   | Button size                                                                                                   |                  |
| `type`                   | `string`   | Style type of on                                                                                              | `"default"`      |
| `plain`                  | `boolean`  | Whether the on is hollow, the background color is transparent                                                 | `false`          |
| `disabled`               | `boolean`  | Is it disabled?                                                                                               | `false`          |
| `loading`                | `boolean`  | Does the name come with loading icon                                                                          | `false`          |
| `hover-class`            | `string`   | Specifies the style class for which the on is pressed. when hover-class="none" There is no click state effect | `"button-hover"` |
| `hover-stop-propagation` | `boolean`  | Specifies whether to prevent this node's ancestor from clicking                                               | `false`          |
| `hover-start-time`       | `number`   | How long does it take to click, in milliseconds?                                                              | `20`             |
| `hover-stay-time`        | `number`   | Click hold time after finger release, in milliseconds                                                         | `70`             |
| `form-type`              | `FormType` | Used for form Component, click separately to trigger form Component submit/reset event                        |                  |
| `open-type`              | `OpenType` | Mini Program open ability                                                                                     | &nbsp;           |

## Events

| Name                  | Description                                                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `bindtap`             | The tap event handler of the button                                                                                  |
| `bindtapcapture`      | Trigger when button tap event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/) |
| `bindtouchstart`      | The start event When touch the button                                                                                |
| `bindopensetting`     | Callback after opening the authorization settings page, open type = openSetting                                      |
| `bindgetuserprofile`  | When the user clicks the on, the user information will be returned, open-type."getuserprofile" is valid              |
| `bindgetphonenumber`  | Gets the user's phone number callback, valid when open-type = getPhoneNumber                                         |
| `bindgetemailaddress` | Gets the user's email address callback                                                                               |

---

# Button

Button.

**Example**

js

```js
const types = ["default", "primary", "warn"];
const pageObject = {
  data: {
    defaultSize: "default",
    primarySize: "default",
    warnSize: "default",
    disabled: false,
    plain: false,
    loading: false,
  },

  onShareAppMessage() {
    return {
      title: "button",
      path: "page/component/pages/button/button",
    };
  },

  setDisabled() {
    this.setData({
      disabled: !this.data.disabled,
    });
  },

  setPlain() {
    this.setData({
      plain: !this.data.plain,
    });
  },

  setLoading() {
    this.setData({
      loading: !this.data.loading,
    });
  },

  handleContact(e) {
    console.log(e.detail);
  },

  handleGetPhoneNumber(e) {
    console.log(e.detail);
  },

  handleGetUserInfo(e) {
    console.log(e.detail);
  },

  handleOpenSetting(e) {
    console.log(e.detail.authSetting);
  },

  handleGetUserInfo(e) {
    console.log(e.detail.userInfo);
  },
};

for (let i = 0; i < types.length; ++i) {
  (function (type) {
    pageObject[type] = function () {
      const key = type + "Size";
      const changedData = {};
      changedData[key] = this.data[key] === "default" ? "mini" : "default";
      this.setData(changedData);
    };
  })(types[i]);
}

Page(pageObject);
```

bxml

```html
<view class="page-body">
  <view class="btn-area" id="buttonContainer">
    <button type="primary">Page Main Normal</button>
    <button type="primary" loading="true">Page Main Loading</button>
    <button type="primary" disabled="true">Page Main Disabled</button>

    <button type="default">Page Second Normal</button>
    <button type="default" disabled="true">Page Second Disabled</button>

    <button type="warn">Warn Normal</button>
    <button type="warn" disabled="true">Warn Disabled</button>

    <view class="button-sp-area">
      <button type="primary" plain="true">Button</button>
      <button type="primary" disabled="true" plain="true">Disable Button</button>

      <button type="default" plain="true"></button>
      <button type="default" disabled="true" plain="true">Button</button>

      <button class="mini-btn" type="primary" size="mini">Button</button>
      <button class="mini-btn" type="default" size="mini">Button</button>
      <button class="mini-btn" type="warn" size="mini">Button</button>
    </view>
  </view>
</view>
```

bxss

```css
button {
  margin-top: 30rpx;
  margin-bottom: 30rpx;
}
.button-sp-area {
  margin: 0 auto;
  width: 60%;
}
.mini-btn {
  margin-right: 10rpx;
}
```

**Bug & Tip**

- `tip`: button-hover Default is{background-color: rgba(0, 0, 0, 0.1) opacity: 0.7}
- `tip`: Currently set form-type of button Object in the current component form Effective. Thus,
  will button Is encapsulated in a custom component, and form In addition to the custom component,
  the button of form-type Failure.

## Props

| Name                     | Type       | Description                                                                                                   | Default          |
| ------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------- | ---------------- |
| `size`                   | `string`   | Button size                                                                                                   |                  |
| `type`                   | `string`   | Style type of on                                                                                              | `"default"`      |
| `plain`                  | `boolean`  | Whether the on is hollow, the background color is transparent                                                 | `false`          |
| `disabled`               | `boolean`  | Is it disabled?                                                                                               | `false`          |
| `loading`                | `boolean`  | Does the name come with loading icon                                                                          | `false`          |
| `hover-class`            | `string`   | Specifies the style class for which the on is pressed. when hover-class="none" There is no click state effect | `"button-hover"` |
| `hover-stop-propagation` | `boolean`  | Specifies whether to prevent this node's ancestor from clicking                                               | `false`          |
| `hover-start-time`       | `number`   | How long does it take to click, in milliseconds?                                                              | `20`             |
| `hover-stay-time`        | `number`   | Click hold time after finger release, in milliseconds                                                         | `70`             |
| `form-type`              | `FormType` | Used for form Component, click separately to trigger form Component submit/reset event                        |                  |
| `open-type`              | `OpenType` | Mini Program open ability                                                                                     | &nbsp;           |

## Events

| Name                  | Description                                                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `bindtap`             | The tap event handler of the button                                                                                  |
| `bindtapcapture`      | Trigger when button tap event capture phase, see more about [DOM3-EVENTS](https://www.w3.org/TR/DOM-Level-3-Events/) |
| `bindtouchstart`      | The start event When touch the button                                                                                |
| `bindopensetting`     | Callback after opening the authorization settings page, open type = openSetting                                      |
| `bindgetuserprofile`  | When the user clicks the on, the user information will be returned, open-type."getuserprofile" is valid              |
| `bindgetphonenumber`  | Gets the user's phone number callback, valid when open-type = getPhoneNumber                                         |
| `bindgetemailaddress` | Gets the user's email address callback                                                                               |