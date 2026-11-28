---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Camera
api_type: Guide
updated_at: 2026-11-28 18:41:56.938163
---

# Camera

Camera component for mp

**Example**

bxml

```html
<view class="container">
  <camera style="position: absolute, height: 100vh, width: 100%, z-index: -1" resolution="medium" device-position="back" flash="auto" />
  <view class="camera-content"> This text should be on top of the camera </view>
</view>
```

json

```json
{
  "backgroundColor": "#00000000"
}
```

- **remark** - supported jssdk >= 4.11.0
- **remark** - inorder to put other components behinds camera, camera component should set z-index
  to -1 and page background-color to transparent

## Props

| Name              | Type     | Description | Default                       |
| ----------------- | -------- | ----------- | ----------------------------- | ---------------------------------- | --------------------------- | -------- |
| `resolution`      | `'low'   | 'medium'    | 'high'`                       | preview resolution, default medium | `"medium"`                  |
| `device-position` | `'front' | 'back'`     | camera position, default back | `"back"`                           |
| `flash`           | `'auto'  | 'on'        | 'off'                         | 'torch'`                           | is open flash, default auto | `"auto"` |

---

# Camera

Camera component for mp

**Example**

bxml

```html
<view class="container">
  <camera style="position: absolute, height: 100vh, width: 100%, z-index: -1" resolution="medium" device-position="back" flash="auto" />
  <view class="camera-content"> This text should be on top of the camera </view>
</view>
```

json

```json
{
  "backgroundColor": "#00000000"
}
```

- **remark** - supported jssdk >= 4.11.0
- **remark** - inorder to put other components behinds camera, camera component should set z-index
  to -1 and page background-color to transparent

## Props

| Name              | Type     | Description | Default                       |
| ----------------- | -------- | ----------- | ----------------------------- | ---------------------------------- | --------------------------- | -------- |
| `resolution`      | `'low'   | 'medium'    | 'high'`                       | preview resolution, default medium | `"medium"`                  |
| `device-position` | `'front' | 'back'`     | camera position, default back | `"back"`                           |
| `flash`           | `'auto'  | 'on'        | 'off'                         | 'torch'`                           | is open flash, default auto | `"auto"` |