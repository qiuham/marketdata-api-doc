---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/views/createSelectorQuery
api_type: Guide
updated_at: 2026-11-22 18:41:22.020383
---

# bn.createSelectorQuery

▸ **createSelectorQuery**(`component?`): `SelectorQuery`

**`description`** Returns a SelectorQuery Object instance which contains information or method of
selected node.

**`example`**

```ts
bn.createSelectorQuery()
  .select("#canvas")
  .fields({ node: true, size: true })
  .exec((res) => {
    const canvas = res[0].node;
    const ctx = canvas.getContext("2d");
    ctx.fillRect(0, 0, 100, 100);
  });
```

Parameters

| Name         | Type                |
| :----------- | :------------------ |
| `component?` | `ComponentInstance` |

Returns

`SelectorQuery`

## Interface: ComponentInstance

| Name      | Type         | Description |
| :-------- | :----------- | :---------- |
| id        | `string`     | instance id |
| getPageId | (): `number` | renderer id |

### getPageId

▸ **getPageId**(): `number`

renderer id

Returns

`number`

## Class: SelectorQuery

| Name                                                                     | Type                                                                             | Description                                                                                                                                                           |
| :----------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_rendererId                                                             | `number`                                                                         |                                                                                                                                                                       |
| \_queue                                                                  | `QueryItem`[] = `[]`                                                             |                                                                                                                                                                       |
| \_queueCb                                                                | (`null` \| `Function`)[] = `[]`                                                  |                                                                                                                                                                       |
| \_component                                                              | `string`                                                                         |                                                                                                                                                                       |
| \_options                                                                | `SelectorQueryOptions`                                                           |                                                                                                                                                                       |
| exec                                                                     | (`callback?`): `void`                                                            | Execute all requests. The request results form an array in the order requested and are returned in the first parameter of callback.                                   |
| select                                                                   | (`selector`, `options?`): `NodesRef`<`true`\>                                    | Select the first node matches with `selector`. return a `NodesRef` object instance, used to get node info.                                                            |
| selectAll                                                                | (`selector`): `NodesRef`<`false`\>                                               | selector grammar                                                                                                                                                      |
| Selectors are similar to CSS But only the following syntax is supported. |
| selectViewport                                                           | (): `NodesRef`<`true`\>                                                          | Select the display area. Can be used to obtain display area size, scroll position and other information.                                                              |
| in                                                                       | (`component`): `SelectorQuery`                                                   | Change the selection of a selector to a custom component component Inside. Initially, the selector selects only page-scoped nodes, not nodes in any custom component. |
| \_push                                                                   | (`selector`, `component`, `single`, `rootPortal`, `fields`, `callback?`): `void` |                                                                                                                                                                       |

### exec

▸ **exec**(`callback?`): `void`

Execute all requests. The request results form an array in the order requested and are returned in
the first parameter of callback.

Parameters

| Name        | Type                          |
| :---------- | :---------------------------- |
| `callback?` | (...`args`: `any`[]) => `any` |

Returns

`void`

---

### select

▸ **select**(`selector`, `options?`): `NodesRef`<`true`\>

Select the first node matches with `selector`. return a `NodesRef` object instance, used to get node
info.

**selector grammar**

selector acts like selector of CSS, but only support following grammar.

- id: #the-id
- class (can specify multiple classes): .a-class.another-class
- child element: .the-parent > .the-child
- descendant selector: .the-ancestor .the-descendant
- descendant selector across custom components: .the-ancestor >>> .the-descendant
- Union of multiple selectors：#a-node, .some-other-nodes

**`example`**

```tsx
bn.createSelectorQuery()
  .select("#the-id")
  .fields(
    {
      dataset: true,
      size: true,
      scrollOffset: true,
      properties: ["scrollX", "scrollY"],
    },
    function (res) {
      res.dataset;
      res.width;
      res.height;
      res.scrollLeft;
      res.scrollTop;
      res.scrollX;
      res.scrollY;
    },
  )
  .exec();
```

Parameters

| Name                  | Type      |
| :-------------------- | :-------- |
| `selector`            | `string`  |
| `options?`            | `Object`  |
| `options.rootPortal?` | `boolean` |

Returns

`NodesRef`<`true`\>

---

### selectAll

▸ **selectAll**(`selector`): `NodesRef`<`false`\>

selector grammar Selectors are similar to CSS But only the following syntax is supported.

ID selector:#the-id Class selector (you can specify more than one in a row):. a-class.another-class
Child element selector:. The-parent > .the-child Descendant selector:. The-ancester .the-descendant
Descendant selector across custom components:. The-ancester >>> .the-descendant Union of multiple
selectors:#a-node, .some-other-nodes

Parameters

| Name       | Type     |
| :--------- | :------- |
| `selector` | `string` |

Returns

`NodesRef`<`false`\>

---

### selectViewport

▸ **selectViewport**(): `NodesRef`<`true`\>

Select the display area. Can be used to obtain display area size, scroll position and other
information.

**`example`**

```tsx
bn.createSelectorQuery()
  .selectViewport()
  .scrollOffset(function (res) {
    res.id;
    res.dataset;
    res.scrollLeft;
    res.scrollTop;
  })
  .exec();
```

Returns

`NodesRef`<`true`\>

---

### in

▸ **in**(`component`): `SelectorQuery`

Change the selection of a selector to a custom component component Inside. Initially, the selector
selects only page-scoped nodes, not nodes in any custom component.

**`example`**

```tsx
Component({
  queryMultipleNodes() {
    const query = bn.createSelectorQuery().in(this);
    query
      .select("#the-id")
      .boundingClientRect(function (res) {
        res.top; // top coordinate of node with id #the-id in this component
      })
      .exec();
  },
});
```

Parameters

| Name             | Type     |
| :--------------- | :------- |
| `component`      | `Object` |
| `component._`    | `Object` |
| `component._.id` | `string` |

Returns

`SelectorQuery`

---

### \_push

▸ **\_push**(`selector`, `component`, `single`, `rootPortal`, `fields`, `callback?`): `void`

Parameters

| Name         | Type                 | Default value |
| :----------- | :------------------- | :------------ |
| `selector`   | `string`             | `undefined`   |
| `component`  | `string`             | `undefined`   |
| `single`     | `boolean`            | `undefined`   |
| `rootPortal` | `boolean`            | `undefined`   |
| `fields`     | `Fields`             | `undefined`   |
| `callback`   | `null` \| `Function` | `null`        |

Returns

`void`

## Class: NodesRef<Single\>

| Name               | Type                                     | Description                                                                                                                                         |
| :----------------- | :--------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_component        | `string`                                 |                                                                                                                                                     |
| \_selector         | `string`                                 |                                                                                                                                                     |
| \_selectorQuery    | `SelectorQuery`                          |                                                                                                                                                     |
| \_single           | `Single`                                 |                                                                                                                                                     |
| \_rootPortal       | `boolean`                                |                                                                                                                                                     |
| boundingClientRect | (`callback?`): `SelectorQuery`           | Add a query request for the layout location of the node. In pixels relative to the display area. This function is similar to getBoundingClientRect. |
| context            | (`callback?`): `SelectorQuery`           | Add node Context Object query request. Currently support VideoContext, CanvasContext, EditorContext.                                                |
| fields             | (`fields`, `callback?`): `SelectorQuery` | Gets information about the node. The fields to fetch are specified in fields                                                                        |
| node               | (`_callback?`): `SelectorQuery`          | Obtain Node Node instance                                                                                                                           |
| scrollOffset       | (`callback?`): `SelectorQuery`           | Adds a scrolling position query request for the node. In pixels. Nodes must be scroll-view or viewport.                                             |

### boundingClientRect

▸ **boundingClientRect**(`callback?`): `SelectorQuery`

Add a query request for the layout location of the node. In pixels relative to the display area.
This function is similar to getBoundingClientRect.

**`example`**

```tsx
bn.createSelectorQuery().select('#the-id').boundingClientRect(function(rect){
  rect.id      // node id
  rect.dataset // node dataset
  rect.left    // node left bound coordinate
  rect.right   // node right bound coordinate
  rect.top     // node top bound coordinate
  rect.bottom  // node bottom bound coordinate
  rect.width   // node width
  rect.height  // node height
}).exec()
@example
```

```tsx
bn.createSelectorQuery()
  .selectAll(".a-class")
  .boundingClientRect(function (rects) {
    rects.forEach(function (rect) {
      rect.id; // node id
      rect.dataset; // node dataset
      rect.left; // node left bound coordinate
      rect.right; // node right bound coordinate
      rect.top; // node top bound coordinate
      rect.bottom; // node bottom bound coordinate
      rect.width; // node width
      rect.height; // node height
    });
  })
  .exec();
```

Parameters

| Name        | Type                                    |
| :---------- | :-------------------------------------- |
| `callback?` | `BoundingClientRectCallback`<`Single`\> |

Returns

`SelectorQuery`

---

### context

▸ **context**(`callback?`): `SelectorQuery`

Add node Context Object query request. Currently support VideoContext, CanvasContext, EditorContext.

**`example`**

```tsx
bn.createSelectorQuery()
  .select(".the-video-class")
  .context(function (res) {
    console.log(res.context);
  })
  .exec();
```

Parameters

| Name        | Type              |
| :---------- | :---------------- |
| `callback?` | `ContextCallback` |

Returns

`SelectorQuery`

---

### fields

▸ **fields**(`fields`, `callback?`): `SelectorQuery`

Gets information about the node. The fields to fetch are specified in fields

Be careful computedStyle Has a higher priority than Size, when at the same time computedStyle Lee
specified width/height And passed in size: True, returns first computedStyle Acquired width/height.

**`example`**

```tsx
bn.createSelectorQuery()
  .select("#the-id")
  .fields(
    {
      dataset: true,
      size: true,
      scrollOffset: true,
      properties: ["scrollX", "scrollY"],
      computedStyle: ["margin", "backgroundColor"],
      context: true,
    },
    function (res) {
      rect.id; // node id
      rect.dataset; // node dataset
      rect.left; // node left bound coordinate
      rect.right; // node right bound coordinate
      rect.top; // node top bound coordinate
      rect.bottom; // node bottom bound coordinate
      rect.width; // node width
      rect.height; // node height
    },
  )
  .exec();
```

Parameters

| Name        | Type                        |
| :---------- | :-------------------------- |
| `fields`    | `Fields`                    |
| `callback?` | `FieldsCallback`<`Single`\> |

Returns

`SelectorQuery`

---

### node

▸ **node**(`_callback?`): `SelectorQuery`

Obtain Node Node instance

**`example`**

```tsx
bn.createSelectorQuery()
  .select(".canvas")
  .node(function (res) {
    console.log(res.node); // canvas instance
  })
  .exec();
```

Parameters

| Name         | Type           |
| :----------- | :------------- |
| `_callback?` | `NodeCallback` |

Returns

`SelectorQuery`

---

### scrollOffset

▸ **scrollOffset**(`callback?`): `SelectorQuery`

Adds a scrolling position query request for the node. In pixels. Nodes must be scroll-view or
viewport.

**`example`**

```tsx
bn.createSelectorQuery()
  .selectViewport()
  .scrollOffset(function (res) {
    res.id; // node id
    res.dataset; // node dataset
    res.scrollLeft; // Horizontal scrolling position of node
    res.scrollTop; // Vertical scroll position of node
  })
  .exec();
```

Parameters

| Name        | Type                   |
| :---------- | :--------------------- |
| `callback?` | `ScrollOffsetCallback` |

Returns

`SelectorQuery`

## Class: SelectorQuery

| Name                                                                     | Type                                                                             | Description                                                                                                                                                           |
| :----------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_rendererId                                                             | `number`                                                                         |                                                                                                                                                                       |
| \_queue                                                                  | `QueryItem`[] = `[]`                                                             |                                                                                                                                                                       |
| \_queueCb                                                                | (`null` \| `Function`)[] = `[]`                                                  |                                                                                                                                                                       |
| \_component                                                              | `string`                                                                         |                                                                                                                                                                       |
| \_options                                                                | `SelectorQueryOptions`                                                           |                                                                                                                                                                       |
| exec                                                                     | (`callback?`): `void`                                                            | Execute all requests. The request results form an array in the order requested and are returned in the first parameter of callback.                                   |
| select                                                                   | (`selector`, `options?`): `NodesRef`<`true`\>                                    | Select the first node matches with `selector`. return a `NodesRef` object instance, used to get node info.                                                            |
| selectAll                                                                | (`selector`): `NodesRef`<`false`\>                                               | selector grammar                                                                                                                                                      |
| Selectors are similar to CSS But only the following syntax is supported. |
| selectViewport                                                           | (): `NodesRef`<`true`\>                                                          | Select the display area. Can be used to obtain display area size, scroll position and other information.                                                              |
| in                                                                       | (`component`): `SelectorQuery`                                                   | Change the selection of a selector to a custom component component Inside. Initially, the selector selects only page-scoped nodes, not nodes in any custom component. |
| \_push                                                                   | (`selector`, `component`, `single`, `rootPortal`, `fields`, `callback?`): `void` |                                                                                                                                                                       |

### exec

▸ **exec**(`callback?`): `void`

Execute all requests. The request results form an array in the order requested and are returned in
the first parameter of callback.

Parameters

| Name        | Type                          |
| :---------- | :---------------------------- |
| `callback?` | (...`args`: `any`[]) => `any` |

Returns

`void`

---

### select

▸ **select**(`selector`, `options?`): `NodesRef`<`true`\>

Select the first node matches with `selector`. return a `NodesRef` object instance, used to get node
info.

**selector grammar**

selector acts like selector of CSS, but only support following grammar.

- id: #the-id
- class (can specify multiple classes): .a-class.another-class
- child element: .the-parent > .the-child
- descendant selector: .the-ancestor .the-descendant
- descendant selector across custom components: .the-ancestor >>> .the-descendant
- Union of multiple selectors：#a-node, .some-other-nodes

**`example`**

```tsx
bn.createSelectorQuery()
  .select("#the-id")
  .fields(
    {
      dataset: true,
      size: true,
      scrollOffset: true,
      properties: ["scrollX", "scrollY"],
    },
    function (res) {
      res.dataset;
      res.width;
      res.height;
      res.scrollLeft;
      res.scrollTop;
      res.scrollX;
      res.scrollY;
    },
  )
  .exec();
```

Parameters

| Name                  | Type      |
| :-------------------- | :-------- |
| `selector`            | `string`  |
| `options?`            | `Object`  |
| `options.rootPortal?` | `boolean` |

Returns

`NodesRef`<`true`\>

---

### selectAll

▸ **selectAll**(`selector`): `NodesRef`<`false`\>

selector grammar Selectors are similar to CSS But only the following syntax is supported.

ID selector:#the-id Class selector (you can specify more than one in a row):. a-class.another-class
Child element selector:. The-parent > .the-child Descendant selector:. The-ancester .the-descendant
Descendant selector across custom components:. The-ancester >>> .the-descendant Union of multiple
selectors:#a-node, .some-other-nodes

Parameters

| Name       | Type     |
| :--------- | :------- |
| `selector` | `string` |

Returns

`NodesRef`<`false`\>

---

### selectViewport

▸ **selectViewport**(): `NodesRef`<`true`\>

Select the display area. Can be used to obtain display area size, scroll position and other
information.

**`example`**

```tsx
bn.createSelectorQuery()
  .selectViewport()
  .scrollOffset(function (res) {
    res.id;
    res.dataset;
    res.scrollLeft;
    res.scrollTop;
  })
  .exec();
```

Returns

`NodesRef`<`true`\>

---

### in

▸ **in**(`component`): `SelectorQuery`

Change the selection of a selector to a custom component component Inside. Initially, the selector
selects only page-scoped nodes, not nodes in any custom component.

**`example`**

```tsx
Component({
  queryMultipleNodes() {
    const query = bn.createSelectorQuery().in(this);
    query
      .select("#the-id")
      .boundingClientRect(function (res) {
        res.top; // top coordinate of node with id #the-id in this component
      })
      .exec();
  },
});
```

Parameters

| Name             | Type     |
| :--------------- | :------- |
| `component`      | `Object` |
| `component._`    | `Object` |
| `component._.id` | `string` |

Returns

`SelectorQuery`

---

### \_push

▸ **\_push**(`selector`, `component`, `single`, `rootPortal`, `fields`, `callback?`): `void`

Parameters

| Name         | Type                 | Default value |
| :----------- | :------------------- | :------------ |
| `selector`   | `string`             | `undefined`   |
| `component`  | `string`             | `undefined`   |
| `single`     | `boolean`            | `undefined`   |
| `rootPortal` | `boolean`            | `undefined`   |
| `fields`     | `Fields`             | `undefined`   |
| `callback`   | `null` \| `Function` | `null`        |

Returns

`void`

## Interface: Fields

| Name           | Type       | Description                                                                                                                                                                                |
| :------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| computedStyle? | `string`[] | Specifies a list of style names and returns the current value of the node corresponding to the style name                                                                                  |
| context?       | `boolean`  | Returns the corresponding node Context object                                                                                                                                              |
| dataset?       | `boolean`  | Returns a node dataset                                                                                                                                                                     |
| id?            | `boolean`  | Returns a node id                                                                                                                                                                          |
| mark?          | `boolean`  | Returns a node mark                                                                                                                                                                        |
| node?          | `boolean`  | Returns the corresponding node Node Example                                                                                                                                                |
| properties?    | `string`[] | Specifies a list of property names that returns the current property value of the node corresponding to the property name. class style And event - bound property values are not available |
| rect?          | `boolean`  | Returns the node layout location（`left` `right` `top` `bottom`）                                                                                                                          |
| scrollOffset?  | `boolean`  | Whether to return a node's scrollLeft scrollTopNode must be scroll-view or viewport                                                                                                        |
| size?          | `boolean`  | Returns the node size（`width` `height`）                                                                                                                                                  |

## BoundingClientRectCallback

Ƭ **BoundingClientRectCallback**<`Single`\>: (`result`: `Single` extends `true` ?
`BoundingClientRect` : `BoundingClientRect`[]) => `void`

Type parameters

| Name     | Type              |
| :------- | :---------------- |
| `Single` | extends `boolean` |

Type declaration

▸ (`result`): `void`

Callback function，after executing `SelectorQuery.exec`, node info return in callback function

Parameters

| Name     | Type                                                                    |
| :------- | :---------------------------------------------------------------------- |
| `result` | `Single` extends `true` ? `BoundingClientRect` : `BoundingClientRect`[] |

Returns

`void`

---

## Interface: BoundingClientRect

| Name    | Type                       | Description                         |
| :------ | :------------------------- | :---------------------------------- |
| bottom  | `number`                   | Lower boundary coordinates of nodes |
| dataset | `Record`<`string`, `any`\> | Node dataset                        |
| height  | `number`                   | Node height                         |
| id      | `string`                   | Node ID                             |
| left    | `number`                   | Left boundary coordinates of nodes  |
| right   | `number`                   | Node's right boundary coordinates   |
| top     | `number`                   | Upper boundary coordinates of nodes |
| width   | `number`                   | Node width                          |

## ContextCallback

Ƭ **ContextCallback**: (`result`: `ContextCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function，after executing `SelectorQuery.exec`, node info return in callback function

Parameters

| Name     | Type                    |
| :------- | :---------------------- |
| `result` | `ContextCallbackResult` |

Returns

`void`

---

## Interface: ContextCallbackResult

| Name    | Type                           | Description             |
| :------ | :----------------------------- | :---------------------- |
| context | `Record`<`string`, `unknown`\> | node's context instance |

## FieldsCallback

Ƭ **FieldsCallback**<`Single`\>: (`res`: `Single` extends `true` ? `Record`<`string`, `unknown`\> :
`Record`<`string`, `unknown`\>[]) => `void`

Type parameters

| Name     | Type              |
| :------- | :---------------- |
| `Single` | extends `boolean` |

Type declaration

▸ (`res`): `void`

callback function

Parameters

| Name  | Type                                                                                        |
| :---- | :------------------------------------------------------------------------------------------ |
| `res` | `Single` extends `true` ? `Record`<`string`, `unknown`\> : `Record`<`string`, `unknown`\>[] |

Returns

`void`

---

## NodeCallback

Ƭ **NodeCallback**: (`result`: `NodeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function，after executing `SelectorQuery.exec`, node info return in callback function

Parameters

| Name     | Type                 |
| :------- | :------------------- |
| `result` | `NodeCallbackResult` |

Returns

`void`

---

## Interface: NodeCallbackResult

| Name | Type                           | Description   |
| :--- | :----------------------------- | :------------ |
| node | `Record`<`string`, `unknown`\> | node instance |

## ScrollOffsetCallback

Ƭ **ScrollOffsetCallback**: (`result`: `ScrollOffsetCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function，after executing `SelectorQuery.exec`, node info return in callback function

Parameters

| Name     | Type                         |
| :------- | :--------------------------- |
| `result` | `ScrollOffsetCallbackResult` |

Returns

`void`

## Interface: ScrollOffsetCallbackResult

| Name       | Type                           | Description                           |
| :--------- | :----------------------------- | :------------------------------------ |
| dataset    | `Record`<`string`, `unknown`\> | node dataset                          |
| id         | `string`                       | node ID                               |
| scrollLeft | `number`                       | Horizontal scrolling position of node |
| scrollTop  | `number`                       | Vertical scroll position of node      |

---

# bn.createSelectorQuery

▸ **createSelectorQuery**(`component?`): `SelectorQuery`

**`description`** Returns a SelectorQuery Object instance which contains information or method of
selected node.

**`example`**

```ts
bn.createSelectorQuery()
  .select("#canvas")
  .fields({ node: true, size: true })
  .exec((res) => {
    const canvas = res[0].node;
    const ctx = canvas.getContext("2d");
    ctx.fillRect(0, 0, 100, 100);
  });
```

Parameters

| Name         | Type                |
| :----------- | :------------------ |
| `component?` | `ComponentInstance` |

Returns

`SelectorQuery`

## Interface: ComponentInstance

| Name      | Type         | Description |
| :-------- | :----------- | :---------- |
| id        | `string`     | instance id |
| getPageId | (): `number` | renderer id |

### getPageId

▸ **getPageId**(): `number`

renderer id

Returns

`number`

## Class: SelectorQuery

| Name                                                                     | Type                                                                             | Description                                                                                                                                                           |
| :----------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_rendererId                                                             | `number`                                                                         |                                                                                                                                                                       |
| \_queue                                                                  | `QueryItem`[] = `[]`                                                             |                                                                                                                                                                       |
| \_queueCb                                                                | (`null` \| `Function`)[] = `[]`                                                  |                                                                                                                                                                       |
| \_component                                                              | `string`                                                                         |                                                                                                                                                                       |
| \_options                                                                | `SelectorQueryOptions`                                                           |                                                                                                                                                                       |
| exec                                                                     | (`callback?`): `void`                                                            | Execute all requests. The request results form an array in the order requested and are returned in the first parameter of callback.                                   |
| select                                                                   | (`selector`, `options?`): `NodesRef`<`true`\>                                    | Select the first node matches with `selector`. return a `NodesRef` object instance, used to get node info.                                                            |
| selectAll                                                                | (`selector`): `NodesRef`<`false`\>                                               | selector grammar                                                                                                                                                      |
| Selectors are similar to CSS But only the following syntax is supported. |
| selectViewport                                                           | (): `NodesRef`<`true`\>                                                          | Select the display area. Can be used to obtain display area size, scroll position and other information.                                                              |
| in                                                                       | (`component`): `SelectorQuery`                                                   | Change the selection of a selector to a custom component component Inside. Initially, the selector selects only page-scoped nodes, not nodes in any custom component. |
| \_push                                                                   | (`selector`, `component`, `single`, `rootPortal`, `fields`, `callback?`): `void` |                                                                                                                                                                       |

### exec

▸ **exec**(`callback?`): `void`

Execute all requests. The request results form an array in the order requested and are returned in
the first parameter of callback.

Parameters

| Name        | Type                          |
| :---------- | :---------------------------- |
| `callback?` | (...`args`: `any`[]) => `any` |

Returns

`void`

---

### select

▸ **select**(`selector`, `options?`): `NodesRef`<`true`\>

Select the first node matches with `selector`. return a `NodesRef` object instance, used to get node
info.

**selector grammar**

selector acts like selector of CSS, but only support following grammar.

- id: #the-id
- class (can specify multiple classes): .a-class.another-class
- child element: .the-parent > .the-child
- descendant selector: .the-ancestor .the-descendant
- descendant selector across custom components: .the-ancestor >>> .the-descendant
- Union of multiple selectors：#a-node, .some-other-nodes

**`example`**

```tsx
bn.createSelectorQuery()
  .select("#the-id")
  .fields(
    {
      dataset: true,
      size: true,
      scrollOffset: true,
      properties: ["scrollX", "scrollY"],
    },
    function (res) {
      res.dataset;
      res.width;
      res.height;
      res.scrollLeft;
      res.scrollTop;
      res.scrollX;
      res.scrollY;
    },
  )
  .exec();
```

Parameters

| Name                  | Type      |
| :-------------------- | :-------- |
| `selector`            | `string`  |
| `options?`            | `Object`  |
| `options.rootPortal?` | `boolean` |

Returns

`NodesRef`<`true`\>

---

### selectAll

▸ **selectAll**(`selector`): `NodesRef`<`false`\>

selector grammar Selectors are similar to CSS But only the following syntax is supported.

ID selector:#the-id Class selector (you can specify more than one in a row):. a-class.another-class
Child element selector:. The-parent > .the-child Descendant selector:. The-ancester .the-descendant
Descendant selector across custom components:. The-ancester >>> .the-descendant Union of multiple
selectors:#a-node, .some-other-nodes

Parameters

| Name       | Type     |
| :--------- | :------- |
| `selector` | `string` |

Returns

`NodesRef`<`false`\>

---

### selectViewport

▸ **selectViewport**(): `NodesRef`<`true`\>

Select the display area. Can be used to obtain display area size, scroll position and other
information.

**`example`**

```tsx
bn.createSelectorQuery()
  .selectViewport()
  .scrollOffset(function (res) {
    res.id;
    res.dataset;
    res.scrollLeft;
    res.scrollTop;
  })
  .exec();
```

Returns

`NodesRef`<`true`\>

---

### in

▸ **in**(`component`): `SelectorQuery`

Change the selection of a selector to a custom component component Inside. Initially, the selector
selects only page-scoped nodes, not nodes in any custom component.

**`example`**

```tsx
Component({
  queryMultipleNodes() {
    const query = bn.createSelectorQuery().in(this);
    query
      .select("#the-id")
      .boundingClientRect(function (res) {
        res.top; // top coordinate of node with id #the-id in this component
      })
      .exec();
  },
});
```

Parameters

| Name             | Type     |
| :--------------- | :------- |
| `component`      | `Object` |
| `component._`    | `Object` |
| `component._.id` | `string` |

Returns

`SelectorQuery`

---

### \_push

▸ **\_push**(`selector`, `component`, `single`, `rootPortal`, `fields`, `callback?`): `void`

Parameters

| Name         | Type                 | Default value |
| :----------- | :------------------- | :------------ |
| `selector`   | `string`             | `undefined`   |
| `component`  | `string`             | `undefined`   |
| `single`     | `boolean`            | `undefined`   |
| `rootPortal` | `boolean`            | `undefined`   |
| `fields`     | `Fields`             | `undefined`   |
| `callback`   | `null` \| `Function` | `null`        |

Returns

`void`

## Class: NodesRef<Single\>

| Name               | Type                                     | Description                                                                                                                                         |
| :----------------- | :--------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_component        | `string`                                 |                                                                                                                                                     |
| \_selector         | `string`                                 |                                                                                                                                                     |
| \_selectorQuery    | `SelectorQuery`                          |                                                                                                                                                     |
| \_single           | `Single`                                 |                                                                                                                                                     |
| \_rootPortal       | `boolean`                                |                                                                                                                                                     |
| boundingClientRect | (`callback?`): `SelectorQuery`           | Add a query request for the layout location of the node. In pixels relative to the display area. This function is similar to getBoundingClientRect. |
| context            | (`callback?`): `SelectorQuery`           | Add node Context Object query request. Currently support VideoContext, CanvasContext, EditorContext.                                                |
| fields             | (`fields`, `callback?`): `SelectorQuery` | Gets information about the node. The fields to fetch are specified in fields                                                                        |
| node               | (`_callback?`): `SelectorQuery`          | Obtain Node Node instance                                                                                                                           |
| scrollOffset       | (`callback?`): `SelectorQuery`           | Adds a scrolling position query request for the node. In pixels. Nodes must be scroll-view or viewport.                                             |

### boundingClientRect

▸ **boundingClientRect**(`callback?`): `SelectorQuery`

Add a query request for the layout location of the node. In pixels relative to the display area.
This function is similar to getBoundingClientRect.

**`example`**

```tsx
bn.createSelectorQuery().select('#the-id').boundingClientRect(function(rect){
  rect.id      // node id
  rect.dataset // node dataset
  rect.left    // node left bound coordinate
  rect.right   // node right bound coordinate
  rect.top     // node top bound coordinate
  rect.bottom  // node bottom bound coordinate
  rect.width   // node width
  rect.height  // node height
}).exec()
@example
```

```tsx
bn.createSelectorQuery()
  .selectAll(".a-class")
  .boundingClientRect(function (rects) {
    rects.forEach(function (rect) {
      rect.id; // node id
      rect.dataset; // node dataset
      rect.left; // node left bound coordinate
      rect.right; // node right bound coordinate
      rect.top; // node top bound coordinate
      rect.bottom; // node bottom bound coordinate
      rect.width; // node width
      rect.height; // node height
    });
  })
  .exec();
```

Parameters

| Name        | Type                                    |
| :---------- | :-------------------------------------- |
| `callback?` | `BoundingClientRectCallback`<`Single`\> |

Returns

`SelectorQuery`

---

### context

▸ **context**(`callback?`): `SelectorQuery`

Add node Context Object query request. Currently support VideoContext, CanvasContext, EditorContext.

**`example`**

```tsx
bn.createSelectorQuery()
  .select(".the-video-class")
  .context(function (res) {
    console.log(res.context);
  })
  .exec();
```

Parameters

| Name        | Type              |
| :---------- | :---------------- |
| `callback?` | `ContextCallback` |

Returns

`SelectorQuery`

---

### fields

▸ **fields**(`fields`, `callback?`): `SelectorQuery`

Gets information about the node. The fields to fetch are specified in fields

Be careful computedStyle Has a higher priority than Size, when at the same time computedStyle Lee
specified width/height And passed in size: True, returns first computedStyle Acquired width/height.

**`example`**

```tsx
bn.createSelectorQuery()
  .select("#the-id")
  .fields(
    {
      dataset: true,
      size: true,
      scrollOffset: true,
      properties: ["scrollX", "scrollY"],
      computedStyle: ["margin", "backgroundColor"],
      context: true,
    },
    function (res) {
      rect.id; // node id
      rect.dataset; // node dataset
      rect.left; // node left bound coordinate
      rect.right; // node right bound coordinate
      rect.top; // node top bound coordinate
      rect.bottom; // node bottom bound coordinate
      rect.width; // node width
      rect.height; // node height
    },
  )
  .exec();
```

Parameters

| Name        | Type                        |
| :---------- | :-------------------------- |
| `fields`    | `Fields`                    |
| `callback?` | `FieldsCallback`<`Single`\> |

Returns

`SelectorQuery`

---

### node

▸ **node**(`_callback?`): `SelectorQuery`

Obtain Node Node instance

**`example`**

```tsx
bn.createSelectorQuery()
  .select(".canvas")
  .node(function (res) {
    console.log(res.node); // canvas instance
  })
  .exec();
```

Parameters

| Name         | Type           |
| :----------- | :------------- |
| `_callback?` | `NodeCallback` |

Returns

`SelectorQuery`

---

### scrollOffset

▸ **scrollOffset**(`callback?`): `SelectorQuery`

Adds a scrolling position query request for the node. In pixels. Nodes must be scroll-view or
viewport.

**`example`**

```tsx
bn.createSelectorQuery()
  .selectViewport()
  .scrollOffset(function (res) {
    res.id; // node id
    res.dataset; // node dataset
    res.scrollLeft; // Horizontal scrolling position of node
    res.scrollTop; // Vertical scroll position of node
  })
  .exec();
```

Parameters

| Name        | Type                   |
| :---------- | :--------------------- |
| `callback?` | `ScrollOffsetCallback` |

Returns

`SelectorQuery`

## Class: SelectorQuery

| Name                                                                     | Type                                                                             | Description                                                                                                                                                           |
| :----------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_rendererId                                                             | `number`                                                                         |                                                                                                                                                                       |
| \_queue                                                                  | `QueryItem`[] = `[]`                                                             |                                                                                                                                                                       |
| \_queueCb                                                                | (`null` \| `Function`)[] = `[]`                                                  |                                                                                                                                                                       |
| \_component                                                              | `string`                                                                         |                                                                                                                                                                       |
| \_options                                                                | `SelectorQueryOptions`                                                           |                                                                                                                                                                       |
| exec                                                                     | (`callback?`): `void`                                                            | Execute all requests. The request results form an array in the order requested and are returned in the first parameter of callback.                                   |
| select                                                                   | (`selector`, `options?`): `NodesRef`<`true`\>                                    | Select the first node matches with `selector`. return a `NodesRef` object instance, used to get node info.                                                            |
| selectAll                                                                | (`selector`): `NodesRef`<`false`\>                                               | selector grammar                                                                                                                                                      |
| Selectors are similar to CSS But only the following syntax is supported. |
| selectViewport                                                           | (): `NodesRef`<`true`\>                                                          | Select the display area. Can be used to obtain display area size, scroll position and other information.                                                              |
| in                                                                       | (`component`): `SelectorQuery`                                                   | Change the selection of a selector to a custom component component Inside. Initially, the selector selects only page-scoped nodes, not nodes in any custom component. |
| \_push                                                                   | (`selector`, `component`, `single`, `rootPortal`, `fields`, `callback?`): `void` |                                                                                                                                                                       |

### exec

▸ **exec**(`callback?`): `void`

Execute all requests. The request results form an array in the order requested and are returned in
the first parameter of callback.

Parameters

| Name        | Type                          |
| :---------- | :---------------------------- |
| `callback?` | (...`args`: `any`[]) => `any` |

Returns

`void`

---

### select

▸ **select**(`selector`, `options?`): `NodesRef`<`true`\>

Select the first node matches with `selector`. return a `NodesRef` object instance, used to get node
info.

**selector grammar**

selector acts like selector of CSS, but only support following grammar.

- id: #the-id
- class (can specify multiple classes): .a-class.another-class
- child element: .the-parent > .the-child
- descendant selector: .the-ancestor .the-descendant
- descendant selector across custom components: .the-ancestor >>> .the-descendant
- Union of multiple selectors：#a-node, .some-other-nodes

**`example`**

```tsx
bn.createSelectorQuery()
  .select("#the-id")
  .fields(
    {
      dataset: true,
      size: true,
      scrollOffset: true,
      properties: ["scrollX", "scrollY"],
    },
    function (res) {
      res.dataset;
      res.width;
      res.height;
      res.scrollLeft;
      res.scrollTop;
      res.scrollX;
      res.scrollY;
    },
  )
  .exec();
```

Parameters

| Name                  | Type      |
| :-------------------- | :-------- |
| `selector`            | `string`  |
| `options?`            | `Object`  |
| `options.rootPortal?` | `boolean` |

Returns

`NodesRef`<`true`\>

---

### selectAll

▸ **selectAll**(`selector`): `NodesRef`<`false`\>

selector grammar Selectors are similar to CSS But only the following syntax is supported.

ID selector:#the-id Class selector (you can specify more than one in a row):. a-class.another-class
Child element selector:. The-parent > .the-child Descendant selector:. The-ancester .the-descendant
Descendant selector across custom components:. The-ancester >>> .the-descendant Union of multiple
selectors:#a-node, .some-other-nodes

Parameters

| Name       | Type     |
| :--------- | :------- |
| `selector` | `string` |

Returns

`NodesRef`<`false`\>

---

### selectViewport

▸ **selectViewport**(): `NodesRef`<`true`\>

Select the display area. Can be used to obtain display area size, scroll position and other
information.

**`example`**

```tsx
bn.createSelectorQuery()
  .selectViewport()
  .scrollOffset(function (res) {
    res.id;
    res.dataset;
    res.scrollLeft;
    res.scrollTop;
  })
  .exec();
```

Returns

`NodesRef`<`true`\>

---

### in

▸ **in**(`component`): `SelectorQuery`

Change the selection of a selector to a custom component component Inside. Initially, the selector
selects only page-scoped nodes, not nodes in any custom component.

**`example`**

```tsx
Component({
  queryMultipleNodes() {
    const query = bn.createSelectorQuery().in(this);
    query
      .select("#the-id")
      .boundingClientRect(function (res) {
        res.top; // top coordinate of node with id #the-id in this component
      })
      .exec();
  },
});
```

Parameters

| Name             | Type     |
| :--------------- | :------- |
| `component`      | `Object` |
| `component._`    | `Object` |
| `component._.id` | `string` |

Returns

`SelectorQuery`

---

### \_push

▸ **\_push**(`selector`, `component`, `single`, `rootPortal`, `fields`, `callback?`): `void`

Parameters

| Name         | Type                 | Default value |
| :----------- | :------------------- | :------------ |
| `selector`   | `string`             | `undefined`   |
| `component`  | `string`             | `undefined`   |
| `single`     | `boolean`            | `undefined`   |
| `rootPortal` | `boolean`            | `undefined`   |
| `fields`     | `Fields`             | `undefined`   |
| `callback`   | `null` \| `Function` | `null`        |

Returns

`void`

## Interface: Fields

| Name           | Type       | Description                                                                                                                                                                                |
| :------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| computedStyle? | `string`[] | Specifies a list of style names and returns the current value of the node corresponding to the style name                                                                                  |
| context?       | `boolean`  | Returns the corresponding node Context object                                                                                                                                              |
| dataset?       | `boolean`  | Returns a node dataset                                                                                                                                                                     |
| id?            | `boolean`  | Returns a node id                                                                                                                                                                          |
| mark?          | `boolean`  | Returns a node mark                                                                                                                                                                        |
| node?          | `boolean`  | Returns the corresponding node Node Example                                                                                                                                                |
| properties?    | `string`[] | Specifies a list of property names that returns the current property value of the node corresponding to the property name. class style And event - bound property values are not available |
| rect?          | `boolean`  | Returns the node layout location（`left` `right` `top` `bottom`）                                                                                                                          |
| scrollOffset?  | `boolean`  | Whether to return a node's scrollLeft scrollTopNode must be scroll-view or viewport                                                                                                        |
| size?          | `boolean`  | Returns the node size（`width` `height`）                                                                                                                                                  |

## BoundingClientRectCallback

Ƭ **BoundingClientRectCallback**<`Single`\>: (`result`: `Single` extends `true` ?
`BoundingClientRect` : `BoundingClientRect`[]) => `void`

Type parameters

| Name     | Type              |
| :------- | :---------------- |
| `Single` | extends `boolean` |

Type declaration

▸ (`result`): `void`

Callback function，after executing `SelectorQuery.exec`, node info return in callback function

Parameters

| Name     | Type                                                                    |
| :------- | :---------------------------------------------------------------------- |
| `result` | `Single` extends `true` ? `BoundingClientRect` : `BoundingClientRect`[] |

Returns

`void`

---

## Interface: BoundingClientRect

| Name    | Type                       | Description                         |
| :------ | :------------------------- | :---------------------------------- |
| bottom  | `number`                   | Lower boundary coordinates of nodes |
| dataset | `Record`<`string`, `any`\> | Node dataset                        |
| height  | `number`                   | Node height                         |
| id      | `string`                   | Node ID                             |
| left    | `number`                   | Left boundary coordinates of nodes  |
| right   | `number`                   | Node's right boundary coordinates   |
| top     | `number`                   | Upper boundary coordinates of nodes |
| width   | `number`                   | Node width                          |

## ContextCallback

Ƭ **ContextCallback**: (`result`: `ContextCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function，after executing `SelectorQuery.exec`, node info return in callback function

Parameters

| Name     | Type                    |
| :------- | :---------------------- |
| `result` | `ContextCallbackResult` |

Returns

`void`

---

## Interface: ContextCallbackResult

| Name    | Type                           | Description             |
| :------ | :----------------------------- | :---------------------- |
| context | `Record`<`string`, `unknown`\> | node's context instance |

## FieldsCallback

Ƭ **FieldsCallback**<`Single`\>: (`res`: `Single` extends `true` ? `Record`<`string`, `unknown`\> :
`Record`<`string`, `unknown`\>[]) => `void`

Type parameters

| Name     | Type              |
| :------- | :---------------- |
| `Single` | extends `boolean` |

Type declaration

▸ (`res`): `void`

callback function

Parameters

| Name  | Type                                                                                        |
| :---- | :------------------------------------------------------------------------------------------ |
| `res` | `Single` extends `true` ? `Record`<`string`, `unknown`\> : `Record`<`string`, `unknown`\>[] |

Returns

`void`

---

## NodeCallback

Ƭ **NodeCallback**: (`result`: `NodeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function，after executing `SelectorQuery.exec`, node info return in callback function

Parameters

| Name     | Type                 |
| :------- | :------------------- |
| `result` | `NodeCallbackResult` |

Returns

`void`

---

## Interface: NodeCallbackResult

| Name | Type                           | Description   |
| :--- | :----------------------------- | :------------ |
| node | `Record`<`string`, `unknown`\> | node instance |

## ScrollOffsetCallback

Ƭ **ScrollOffsetCallback**: (`result`: `ScrollOffsetCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function，after executing `SelectorQuery.exec`, node info return in callback function

Parameters

| Name     | Type                         |
| :------- | :--------------------------- |
| `result` | `ScrollOffsetCallbackResult` |

Returns

`void`

## Interface: ScrollOffsetCallbackResult

| Name       | Type                           | Description                           |
| :--------- | :----------------------------- | :------------------------------------ |
| dataset    | `Record`<`string`, `unknown`\> | node dataset                          |
| id         | `string`                       | node ID                               |
| scrollLeft | `number`                       | Horizontal scrolling position of node |
| scrollTop  | `number`                       | Vertical scroll position of node      |