---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/PickerView
api_type: Guide
updated_at: 2026-11-27 18:42:01.186616
---

# picker-view

PickerView.

**Example**

js

```js
const date = new Date();
const years = [];
const months = [];
const days = [];

for (let i = 1990; i <= date.getFullYear(); i++) {
  years.push(i);
}

for (let i = 1; i <= 12; i++) {
  months.push(i);
}

for (let i = 1; i <= 31; i++) {
  days.push(i);
}

Page({
  data: {
    years: years,
    year: date.getFullYear(),
    months: months,
    month: 2,
    days: days,
    day: 2,
    value: [9999, 1, 1],
  },
  bindChange: function (e) {
    const val = e.detail.value;
    this.setData({
      year: this.data.years[val[0]],
      month: this.data.months[val[1]],
      day: this.data.days[val[2]],
    });
  },
});
```

index.bxml

```html
<view>
  <view>{{year}}年{{month}}月{{day}}日</view>
  <picker-view indicator-style="height: 50px;" style="width: 100%; height: 300px;" value="{{value}}" bindchange="bindChange">
    <picker-view-column>
      <view bn:for="{{years}}" style="line-height: 50px">{{item}}年</view>
    </picker-view-column>
    <picker-view-column>
      <view bn:for="{{months}}" style="line-height: 50px">{{item}}月</view>
    </picker-view-column>
    <picker-view-column>
      <view bn:for="{{days}}" style="line-height: 50px">{{item}}日</view>
    </picker-view-column>
  </picker-view>
</view>
```

**Bug & Tip**

- `tip`: `navigator-hover` Default is `{background-color: rgba(0, 0, 0, 0.1) opacity: 0.7}`,
  navigator Child node background color should be transparent

## Props

| Name    | Type                     | Description |
| ------- | ------------------------ | ----------- |
| `value` | `number[]`               |             |
| `style` | `string` &#124; `object` | &nbsp;      |

## Events

| Name            | Description |
| --------------- | ----------- |
| `bindchange`    |             |
| `bindpickstart` |             |
| `bindpickend`   | &nbsp;      |

---

# picker-view

PickerView.

**Example**

js

```js
const date = new Date();
const years = [];
const months = [];
const days = [];

for (let i = 1990; i <= date.getFullYear(); i++) {
  years.push(i);
}

for (let i = 1; i <= 12; i++) {
  months.push(i);
}

for (let i = 1; i <= 31; i++) {
  days.push(i);
}

Page({
  data: {
    years: years,
    year: date.getFullYear(),
    months: months,
    month: 2,
    days: days,
    day: 2,
    value: [9999, 1, 1],
  },
  bindChange: function (e) {
    const val = e.detail.value;
    this.setData({
      year: this.data.years[val[0]],
      month: this.data.months[val[1]],
      day: this.data.days[val[2]],
    });
  },
});
```

index.bxml

```html
<view>
  <view>{{year}}年{{month}}月{{day}}日</view>
  <picker-view indicator-style="height: 50px;" style="width: 100%; height: 300px;" value="{{value}}" bindchange="bindChange">
    <picker-view-column>
      <view bn:for="{{years}}" style="line-height: 50px">{{item}}年</view>
    </picker-view-column>
    <picker-view-column>
      <view bn:for="{{months}}" style="line-height: 50px">{{item}}月</view>
    </picker-view-column>
    <picker-view-column>
      <view bn:for="{{days}}" style="line-height: 50px">{{item}}日</view>
    </picker-view-column>
  </picker-view>
</view>
```

**Bug & Tip**

- `tip`: `navigator-hover` Default is `{background-color: rgba(0, 0, 0, 0.1) opacity: 0.7}`,
  navigator Child node background color should be transparent

## Props

| Name    | Type                     | Description |
| ------- | ------------------------ | ----------- |
| `value` | `number[]`               |             |
| `style` | `string` &#124; `object` | &nbsp;      |

## Events

| Name            | Description |
| --------------- | ----------- |
| `bindchange`    |             |
| `bindpickstart` |             |
| `bindpickend`   | &nbsp;      |