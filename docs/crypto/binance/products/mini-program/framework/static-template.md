---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/static-template
api_type: Guide
updated_at: 2026-11-18 02:18:26.936784
---

# Render Template Earlier

Usually, the renderer need to wait worker ready and render template with data from worker. But when
the tamplate is a static template and can render without data, the renderer do not need to wait
worker data and can render template earlier.

For Example, a list page can render an empty list at first earlier, and render the full list when
data ready. It can help improving page FP/FCP perfromance

> Start from SDK library version 4.25.0

## Usage

### 1. Add `staticTemplate` field in page config file

```json
{
  "staticTemplate": {
    "enable": true,
    "removeSkeleton": true, //  Start from SDK library version 4.40.0
    "data": { "userName": "visitor" }
  }
}
```

### 2. Make sure page tamplete is safe for earlier render

```html
<view>
  <!-- The following will render based on staticTemplate config data on first render -->
  <view
    >hi, {{userName}}!<view>
      <view class="list">
        <!-- The list should provide default value because data may not ready on first render when enable staticTemplate -->
        <view bn:for="{{list || []}}" class="list-item">
          <view>{{item.no}}</view>
          <view>{{item.title}}</view>
          <view> </view> </view></view></view></view
></view>
```

---

# Render Template Earlier

Usually, the renderer need to wait worker ready and render template with data from worker. But when
the tamplate is a static template and can render without data, the renderer do not need to wait
worker data and can render template earlier.

For Example, a list page can render an empty list at first earlier, and render the full list when
data ready. It can help improving page FP/FCP perfromance

> Start from SDK library version 4.25.0

## Usage

### 1. Add `staticTemplate` field in page config file

```json
{
  "staticTemplate": {
    "enable": true,
    "removeSkeleton": true, //  Start from SDK library version 4.40.0
    "data": { "userName": "visitor" }
  }
}
```

### 2. Make sure page tamplete is safe for earlier render

```html
<view>
  <!-- The following will render based on staticTemplate config data on first render -->
  <view
    >hi, {{userName}}!<view>
      <view class="list">
        <!-- The list should provide default value because data may not ready on first render when enable staticTemplate -->
        <view bn:for="{{list || []}}" class="list-item">
          <view>{{item.no}}</view>
          <view>{{item.title}}</view>
          <view> </view> </view></view></view></view
></view>
```