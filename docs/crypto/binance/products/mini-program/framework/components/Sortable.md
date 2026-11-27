---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Sortable
api_type: Guide
updated_at: 2026-11-27 18:41:48.589280
---

# Sortable

A sortable list component that supports drag-and-drop sorting

**Example**

bxml

```html
<theme-context>
  <view class="container">
    <head title="sortable"></head>
    <view class="page-body">
      <view class="item">
        <view class="left">
          <image class="icon" src="https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/87496d50-2408-43e1-ad4c-78b47b448a6a.png" />
          <view>btc</view>
        </view>
        <view class="handle">
          <view class="line disable"></view>
          <view class="line line2 disable"></view>
        </view>
      </view>
      <sortable bind:reorder="onReorder">
        <sortable-item bn:for="{{list}}">
          <view class="item">
            <view class="left">
              <image class="icon" src="{{item.icon}}" />
              <view>{{item.title}}</view>
            </view>
            <sortable-handle>
              <view class="handle">
                <view class="line"></view>
                <view class="line line2"></view>
              </view>
            </sortable-handle>
          </view>
        </sortable-item>
      </sortable>
      <view>data:</view>
      <view bn:for="{{list}}" bn:key="index">
        <view>{{index}}: {{item.title}}</view>
      </view>
    </view>
  </view>
</theme-context>
```

js

```js
Page({
  data: {
    list: [
      {
        title: "eth",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/3a8c9fe6-2a76-4ace-aa07-415d994de6f0.png",
      },
      {
        title: "bnb",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20220218/94863af2-c980-42cf-a139-7b9f462a36c2.png",
      },
      {
        title: "xrp",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/4766a9cc-8545-4c2b-bfa4-cad2be91c135.png",
      },
      {
        title: "sol",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "ada",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "ltc",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "trx",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "bch",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "bsv",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
    ],
  },
  onReorder(e) {
    const { oldIndex, newIndex } = e.detail;
    const list = this.data.list;
    const item = list.splice(oldIndex, 1)[0];
    list.splice(newIndex, 0, item);
    this.setData({ list });
    bn.showToast({ title: `from ${oldIndex} to ${newIndex}` });
  },
});
```

bxss

```css
.handle {
  height: 20px;
  width: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.icon {
  width: 20px;
  height: 20px;
  margin-right: 4px;
}

.left {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.line {
  width: 13px;
  height: 2.5px;
  background-color: #929aa5;
  margin-bottom: 3px;
}

.disable {
  background-color: pink;
}

.line2 {
  margin-bottom: 0;
}

.item {
  height: 54px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 15px;
  font-size: 16px;
  line-height: 24px;
  background-color: white;
}

.app {
  height: 100vh;
  width: 100vw;
  background: #f0f0f0;
}

.title {
  width: 100%;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  line-height: 24px;
  font-weight: bold;
}
```

- **remark** - supported jssdk >= 4.37.0
- **remark** - The configuration of being fixed at the top and not draggable is not supported. If
  you have similar requirements, please use two lists to implement it.
- **remark** - If you use Pika to develop miniprogram, please do not use state to control sorting
  when using the Sortable component. React does not work well with sortablejs yet. Please use React
  ref to store the latest sorting state.

## Props

| Name                   | Type      | Description                                                | Default |
| ---------------------- | --------- | ---------------------------------------------------------- | ------- |
| `enable-vibrate-short` | `boolean` | whether to enable vibration feedback                       | `true`  |
| `direction`            | `string`  | Set gesture direction, support x-axis/y-axis/free dragging | `"y"`   |

## Events

| Name          | Description                                                                     |
| ------------- | ------------------------------------------------------------------------------- |
| `bindreorder` | Triggered when the dragging item dropped，event.detail = { oldIndex, newIndex } |

---

# Sortable

A sortable list component that supports drag-and-drop sorting

**Example**

bxml

```html
<theme-context>
  <view class="container">
    <head title="sortable"></head>
    <view class="page-body">
      <view class="item">
        <view class="left">
          <image class="icon" src="https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/87496d50-2408-43e1-ad4c-78b47b448a6a.png" />
          <view>btc</view>
        </view>
        <view class="handle">
          <view class="line disable"></view>
          <view class="line line2 disable"></view>
        </view>
      </view>
      <sortable bind:reorder="onReorder">
        <sortable-item bn:for="{{list}}">
          <view class="item">
            <view class="left">
              <image class="icon" src="{{item.icon}}" />
              <view>{{item.title}}</view>
            </view>
            <sortable-handle>
              <view class="handle">
                <view class="line"></view>
                <view class="line line2"></view>
              </view>
            </sortable-handle>
          </view>
        </sortable-item>
      </sortable>
      <view>data:</view>
      <view bn:for="{{list}}" bn:key="index">
        <view>{{index}}: {{item.title}}</view>
      </view>
    </view>
  </view>
</theme-context>
```

js

```js
Page({
  data: {
    list: [
      {
        title: "eth",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/3a8c9fe6-2a76-4ace-aa07-415d994de6f0.png",
      },
      {
        title: "bnb",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20220218/94863af2-c980-42cf-a139-7b9f462a36c2.png",
      },
      {
        title: "xrp",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/4766a9cc-8545-4c2b-bfa4-cad2be91c135.png",
      },
      {
        title: "sol",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "ada",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "ltc",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "trx",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "bch",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
      {
        title: "bsv",
        icon: "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20230404/b2f0c70f-4fb2-4472-9fe7-480ad1592421.png",
      },
    ],
  },
  onReorder(e) {
    const { oldIndex, newIndex } = e.detail;
    const list = this.data.list;
    const item = list.splice(oldIndex, 1)[0];
    list.splice(newIndex, 0, item);
    this.setData({ list });
    bn.showToast({ title: `from ${oldIndex} to ${newIndex}` });
  },
});
```

bxss

```css
.handle {
  height: 20px;
  width: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.icon {
  width: 20px;
  height: 20px;
  margin-right: 4px;
}

.left {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.line {
  width: 13px;
  height: 2.5px;
  background-color: #929aa5;
  margin-bottom: 3px;
}

.disable {
  background-color: pink;
}

.line2 {
  margin-bottom: 0;
}

.item {
  height: 54px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 15px;
  font-size: 16px;
  line-height: 24px;
  background-color: white;
}

.app {
  height: 100vh;
  width: 100vw;
  background: #f0f0f0;
}

.title {
  width: 100%;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  line-height: 24px;
  font-weight: bold;
}
```

- **remark** - supported jssdk >= 4.37.0
- **remark** - The configuration of being fixed at the top and not draggable is not supported. If
  you have similar requirements, please use two lists to implement it.
- **remark** - If you use Pika to develop miniprogram, please do not use state to control sorting
  when using the Sortable component. React does not work well with sortablejs yet. Please use React
  ref to store the latest sorting state.

## Props

| Name                   | Type      | Description                                                | Default |
| ---------------------- | --------- | ---------------------------------------------------------- | ------- |
| `enable-vibrate-short` | `boolean` | whether to enable vibration feedback                       | `true`  |
| `direction`            | `string`  | Set gesture direction, support x-axis/y-axis/free dragging | `"y"`   |

## Events

| Name          | Description                                                                     |
| ------------- | ------------------------------------------------------------------------------- |
| `bindreorder` | Triggered when the dragging item dropped，event.detail = { oldIndex, newIndex } |