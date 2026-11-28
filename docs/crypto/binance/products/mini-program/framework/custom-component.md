---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/custom-component
api_type: Guide
updated_at: 2026-11-28 18:36:58.922195
---

# Custom Component

## Custom Component

Developers can abstract parts of a page into custom components for use across different pages, or to
divide a page into multiple low-coupling modules for easy maintenance. Custom components work almost
in the same way as basic components.

### Creating a Custom Component

Like a page, a custom component includes json, bxml, bxss, and js files. To create a custom
component, first declare the custom component in the json file.

```json
{
  "component": true
}
```

You can then write a component template in the bxml file and a component style in the bxss file, as
you would when creating a page.

Code example:

```html
<!-- This is the BXML structure of the custom component -->
<view class="inner"> {{innerText}} </view>
<slot></slot>
```

```css
/* This style applies only to this custom component */
.inner {
  color: red;
}
```

Note: You should not use ID selectors, attribute selectors, or tag name selectors in the component's
bxss.

In the js file of the custom component, you should register the component using `Component()`,
specifying the component's property definitions, data, and custom methods.

The component's property values and data are used to render the bxml of the component. The property
values are passed to the component externally.

Code example:

```js
Component({
  properties: {
    // The innerText property is defined here, and the property value can be set when the component is used.
    innerText: {
      type: String,
      value: "default value",
    },
  },
  data: {
    // Here are some internal component data
    someData: {},
  },
  methods: {
    // A custom method
    customMethod: function () {},
  },
});
```

### Using a Custom Component

To use a registered custom component, you need to declare a reference to it in the page's json file.
You should specify the tag name of each custom component and the file path to the appropriate custom
component:

```json
{
  "usingComponents": {
    "component-tag-name": "path/to/the/custom/component"
  }
}
```

Then, you can use the custom components in the page's bxml in much the same way as you would use
base components. The node name is the custom component's tag name, and the node property is the
property value passed to the component.

Code example:

```html
<view>
  <!-- Using a custom component -->
  <component-tag-name inner-text="Some text"></component-tag-name>
</view>
```

Once the custom component's bxml node structure is combined with the data, it will be inserted at
the referenced location.

---

# Custom Component

## Custom Component

Developers can abstract parts of a page into custom components for use across different pages, or to
divide a page into multiple low-coupling modules for easy maintenance. Custom components work almost
in the same way as basic components.

### Creating a Custom Component

Like a page, a custom component includes json, bxml, bxss, and js files. To create a custom
component, first declare the custom component in the json file.

```json
{
  "component": true
}
```

You can then write a component template in the bxml file and a component style in the bxss file, as
you would when creating a page.

Code example:

```html
<!-- This is the BXML structure of the custom component -->
<view class="inner"> {{innerText}} </view>
<slot></slot>
```

```css
/* This style applies only to this custom component */
.inner {
  color: red;
}
```

Note: You should not use ID selectors, attribute selectors, or tag name selectors in the component's
bxss.

In the js file of the custom component, you should register the component using `Component()`,
specifying the component's property definitions, data, and custom methods.

The component's property values and data are used to render the bxml of the component. The property
values are passed to the component externally.

Code example:

```js
Component({
  properties: {
    // The innerText property is defined here, and the property value can be set when the component is used.
    innerText: {
      type: String,
      value: "default value",
    },
  },
  data: {
    // Here are some internal component data
    someData: {},
  },
  methods: {
    // A custom method
    customMethod: function () {},
  },
});
```

### Using a Custom Component

To use a registered custom component, you need to declare a reference to it in the page's json file.
You should specify the tag name of each custom component and the file path to the appropriate custom
component:

```json
{
  "usingComponents": {
    "component-tag-name": "path/to/the/custom/component"
  }
}
```

Then, you can use the custom components in the page's bxml in much the same way as you would use
base components. The node name is the custom component's tag name, and the node property is the
property value passed to the component.

Code example:

```html
<view>
  <!-- Using a custom component -->
  <component-tag-name inner-text="Some text"></component-tag-name>
</view>
```

Once the custom component's bxml node structure is combined with the data, it will be inserted at
the referenced location.