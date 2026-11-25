---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/bns
api_type: Guide
updated_at: 2026-11-25 18:38:45.823885
---

# BNS

## BNS

BNS (Binance Script) is a scripting language designed for Mini Programs. Alongside BXML, it helps
construct the page structure.

### Introduction

BNS code can either be drafted within the `<bns>...</bns>` tags in a bxml file or in a .bns file.

Each .bns file and `<bns>...</bns>` tag constitutes an individual module.

Each module maintains its separate scope. Essentially, variables and functions established in a
module are naturally private and hidden from other modules.

If a module needs to expose its internal private variables and functions, it can only do so through
module.exports.

The `<bns>...</bns>` tag has two attributes - module and src. The module attribute is mandatory and
ought to be unique. The src attribute is optional. If it isn't specified, the content within the
`<bns>...</bns>` tags serves as the module code.

### Event Binding

BNS functions can be employed to react to Mini Program events. At present, they can only respond to
built-in component events, and do not support custom component events. Besides pure logical
operations, BNS functions can also interact with the encapsulated ComponentDescriptor instance and
set the component's classes and styles. For interactive animation, setting the style and class is
sufficient.

Example:

BXML:

```xml
<view class="container">
    <bns module="foo" src="./foo.bns"></bns>
    <bns module="bar">
        module.exports = {
            changeToRed(e, instance) {
                instance.setClass('red');
            },
            changeToBlue(e, instance) {
                instance.setClass('blue')
            },
        }
    </bns>
    <view bindtap="foo.changeTo20Px">Click to change font-size to 20px</view>
    <view bindtap="bar.changeToRed">Click to change color to red</view>
    <view bindtap="bar.changeToBlue">Click to change color to blue</view>
</view>
```

JS:

```js
// /pages/comm.bns
module.exports = {
  changeTo20Px(e, instance) {
    instance.setStyle({
      "font-size": "20px",
    });
  },
};
```

The event handler accepts two parameters: e and instance.

- e is the Event Target, the same as the event object in the Mini Program event binding function.
- instance is the ComponentDescriptor instance of the current component, which can be used to set
  the class and style of the component. Currently, only two methods are supported, setClass and
  setStyle.

---

# BNS

## BNS

BNS (Binance Script) is a scripting language designed for Mini Programs. Alongside BXML, it helps
construct the page structure.

### Introduction

BNS code can either be drafted within the `<bns>...</bns>` tags in a bxml file or in a .bns file.

Each .bns file and `<bns>...</bns>` tag constitutes an individual module.

Each module maintains its separate scope. Essentially, variables and functions established in a
module are naturally private and hidden from other modules.

If a module needs to expose its internal private variables and functions, it can only do so through
module.exports.

The `<bns>...</bns>` tag has two attributes - module and src. The module attribute is mandatory and
ought to be unique. The src attribute is optional. If it isn't specified, the content within the
`<bns>...</bns>` tags serves as the module code.

### Event Binding

BNS functions can be employed to react to Mini Program events. At present, they can only respond to
built-in component events, and do not support custom component events. Besides pure logical
operations, BNS functions can also interact with the encapsulated ComponentDescriptor instance and
set the component's classes and styles. For interactive animation, setting the style and class is
sufficient.

Example:

BXML:

```xml
<view class="container">
    <bns module="foo" src="./foo.bns"></bns>
    <bns module="bar">
        module.exports = {
            changeToRed(e, instance) {
                instance.setClass('red');
            },
            changeToBlue(e, instance) {
                instance.setClass('blue')
            },
        }
    </bns>
    <view bindtap="foo.changeTo20Px">Click to change font-size to 20px</view>
    <view bindtap="bar.changeToRed">Click to change color to red</view>
    <view bindtap="bar.changeToBlue">Click to change color to blue</view>
</view>
```

JS:

```js
// /pages/comm.bns
module.exports = {
  changeTo20Px(e, instance) {
    instance.setStyle({
      "font-size": "20px",
    });
  },
};
```

The event handler accepts two parameters: e and instance.

- e is the Event Target, the same as the event object in the Mini Program event binding function.
- instance is the ComponentDescriptor instance of the current component, which can be used to set
  the class and style of the component. Currently, only two methods are supported, setClass and
  setStyle.