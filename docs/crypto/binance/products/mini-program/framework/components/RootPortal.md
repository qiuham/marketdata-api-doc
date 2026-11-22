---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/RootPortal
api_type: Guide
updated_at: 2026-11-22 18:40:12.924846
---

# root-portal

Makes the entire subtree off the page, similar to using fixed position in CSS. It is mainly used to
make pop-up windows, pop-up layers, etc.

**Example**

bxml

```html
<root-portal enable="{{enable}}">
  <view class="dialog"> I'm a dialog </view>
</root-portal>
```

js

```js
Page({
  data() {
    return {
      enable: true,
    };
  },
});
```

when use bn.createSelectorQuery, you may not get the dom in <root-portal>. add a second parameter in
select funtion will make it work.

**Example**

````html
<root-portal enable="{{enable}}">
  <canvas id="canvas"></canvas>
</root-portal>

``` ts bn.createSelectorQuery() .select('#canvas', { rootPortal: true }}) .fields({ node: true, size: true }) .exec(res => { const canvas = res[0].node const ctx = canvas.getContext('2d') ctx.fillRect(0, 0, 100, 100) })
````

## Props

| Name     | Type      | Description                    | Default |
| -------- | --------- | ------------------------------ | ------- |
| `enable` | `boolean` | whether detached from the page | `true`  |

---

# root-portal

Makes the entire subtree off the page, similar to using fixed position in CSS. It is mainly used to
make pop-up windows, pop-up layers, etc.

**Example**

bxml

```html
<root-portal enable="{{enable}}">
  <view class="dialog"> I'm a dialog </view>
</root-portal>
```

js

```js
Page({
  data() {
    return {
      enable: true,
    };
  },
});
```

when use bn.createSelectorQuery, you may not get the dom in <root-portal>. add a second parameter in
select funtion will make it work.

**Example**

````html
<root-portal enable="{{enable}}">
  <canvas id="canvas"></canvas>
</root-portal>

``` ts bn.createSelectorQuery() .select('#canvas', { rootPortal: true }}) .fields({ node: true, size: true }) .exec(res => { const canvas = res[0].node const ctx = canvas.getContext('2d') ctx.fillRect(0, 0, 100, 100) })
````

## Props

| Name     | Type      | Description                    | Default |
| -------- | --------- | ------------------------------ | ------- |
| `enable` | `boolean` | whether detached from the page | `true`  |