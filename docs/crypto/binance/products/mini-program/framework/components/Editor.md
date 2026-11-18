---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Editor
api_type: Guide
updated_at: 2026-11-18 18:42:31.200943
---

# editor

**Example**

```html
<editor id="editor" placeholder="write something..." bindready="onEditorReady" bindstatuschange="bindstatuschange" bindinput="bindinput" bindfocus="bindfocus" bindblur="bindblur" bindselectionupdate="bindselectionupdate"></editor>
```

- **remark** - sdk >= 4.7.0

## Props

| Name          | Type                                                   | Description                   | Default |
| ------------- | ------------------------------------------------------ | ----------------------------- | ------- |
| `id`          | `string`                                               |                               |         |
| `read-only`   | `boolean`                                              | The editor is readOnly or not | `false` |
| `placeholder` | `string`                                               | The editor placeholder        |         |
| `plugins`     | `Array<{ name: string, config: Record<string, Any> }>` | the plugin setting            | &nbsp;  |

## Events

| Name                  | Description                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| `bindready`           | Triggered when editor initialization is complete                                                      |
| `bindinput`           | Triggered when editor content changes ,                                                               |
| `bindblur`            | Triggered when editor blur                                                                            |
| `bindfocus`           | Triggered when editor focus                                                                           |
| `bindstatuschange`    | adopt Context Method to change a style in the editor, returning a style already set for the selection |
| `bindselectionupdate` | when the editor selection update                                                                      |
| `bindpaste`           | when paste content from clipboard                                                                     |

---

# editor

**Example**

```html
<editor id="editor" placeholder="write something..." bindready="onEditorReady" bindstatuschange="bindstatuschange" bindinput="bindinput" bindfocus="bindfocus" bindblur="bindblur" bindselectionupdate="bindselectionupdate"></editor>
```

- **remark** - sdk >= 4.7.0

## Props

| Name          | Type                                                   | Description                   | Default |
| ------------- | ------------------------------------------------------ | ----------------------------- | ------- |
| `id`          | `string`                                               |                               |         |
| `read-only`   | `boolean`                                              | The editor is readOnly or not | `false` |
| `placeholder` | `string`                                               | The editor placeholder        |         |
| `plugins`     | `Array<{ name: string, config: Record<string, Any> }>` | the plugin setting            | &nbsp;  |

## Events

| Name                  | Description                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| `bindready`           | Triggered when editor initialization is complete                                                      |
| `bindinput`           | Triggered when editor content changes ,                                                               |
| `bindblur`            | Triggered when editor blur                                                                            |
| `bindfocus`           | Triggered when editor focus                                                                           |
| `bindstatuschange`    | adopt Context Method to change a style in the editor, returning a style already set for the selection |
| `bindselectionupdate` | when the editor selection update                                                                      |
| `bindpaste`           | when paste content from clipboard                                                                     |