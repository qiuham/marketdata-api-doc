---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Label
api_type: Guide
updated_at: 2026-11-22 18:40:27.612138
---

# label

Label.

**Example**

js

```js
Page({
  data: {
    radioItems: [{ name: "USA" }, { name: "CHN", checked: "true" }, { name: "BRA" }, { name: "JPN" }, { name: "ENG" }, { name: "TUR" }],
    hidden: false,
  },
});
```

bxml

```html
<theme-context>
  <view class="container">
    <view class="section section_gap">
      <view class="section__title">label用for标识表单组件</view>
      <radio-group class="group">
        <view class="label-2" bn:for="{{radioItems}}">
          <radio id="{{item.name}}" hidden value="{{item.name}}" checked="{{item.checked}}"></radio>
          <view class="label-2__icon">
            <view class="label-2__icon-checked" style="opacity:{{item.checked ? 1: 0}}"></view>
          </view>
          <label class="label-2__text" for="{{item.name}}"><text>{{item.name}}</text></label>
        </view>
      </radio-group>
    </view>
  </view>
</theme-context>
```

bxss

```css
.label-2 {
  margin-bottom: 15px;
}
.label-2__text {
  display: inline-block;
  vertical-align: middle;
}
.label-2__icon {
  position: relative;
  display: inline-block;
  vertical-align: middle;
  margin-right: 10px;
  width: 18px;
  height: 18px;
  background: #fcfff4;
  border-radius: 50px;
}

.label-2__icon-checked {
  position: absolute;
  left: 3px;
  top: 3px;
  width: 12px;
  height: 12px;
  background: #1aad19;
  border-radius: 50%;
}

.label-4_text {
  text-align: center;
  margin-top: 15px;
}
```

## Props

| Name  | Type     | Description |
| ----- | -------- | ----------- |
| `for` | `string` | &nbsp;      |

## Events

| Name      | Description |
| --------- | ----------- |
| `bindtap` | &nbsp;      |

---

# label

Label.

**Example**

js

```js
Page({
  data: {
    radioItems: [{ name: "USA" }, { name: "CHN", checked: "true" }, { name: "BRA" }, { name: "JPN" }, { name: "ENG" }, { name: "TUR" }],
    hidden: false,
  },
});
```

bxml

```html
<theme-context>
  <view class="container">
    <view class="section section_gap">
      <view class="section__title">label用for标识表单组件</view>
      <radio-group class="group">
        <view class="label-2" bn:for="{{radioItems}}">
          <radio id="{{item.name}}" hidden value="{{item.name}}" checked="{{item.checked}}"></radio>
          <view class="label-2__icon">
            <view class="label-2__icon-checked" style="opacity:{{item.checked ? 1: 0}}"></view>
          </view>
          <label class="label-2__text" for="{{item.name}}"><text>{{item.name}}</text></label>
        </view>
      </radio-group>
    </view>
  </view>
</theme-context>
```

bxss

```css
.label-2 {
  margin-bottom: 15px;
}
.label-2__text {
  display: inline-block;
  vertical-align: middle;
}
.label-2__icon {
  position: relative;
  display: inline-block;
  vertical-align: middle;
  margin-right: 10px;
  width: 18px;
  height: 18px;
  background: #fcfff4;
  border-radius: 50px;
}

.label-2__icon-checked {
  position: absolute;
  left: 3px;
  top: 3px;
  width: 12px;
  height: 12px;
  background: #1aad19;
  border-radius: 50%;
}

.label-4_text {
  text-align: center;
  margin-top: 15px;
}
```

## Props

| Name  | Type     | Description |
| ----- | -------- | ----------- |
| `for` | `string` | &nbsp;      |

## Events

| Name      | Description |
| --------- | ----------- |
| `bindtap` | &nbsp;      |