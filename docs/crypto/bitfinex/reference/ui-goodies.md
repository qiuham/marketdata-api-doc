---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: bitfinex
provider_name: Bitfinex
product: api
product_id: bitfinex
source_url: 'https://docs.bitfinex.com/reference/ui-goodies'
updated_at: 2026-11-21
---

# UI Goodies

## UI Goodies examples repository

<https://github.com/bitfinexcom/bfx-stuff-ui> : small examples to master Bitfinex UI Goodies

## Chart Marks

## Overview

Chart markers allow you to display certain events, such as important news, on the Bitfinex UI chart. All markers are associated with a specific timestamp which determines the candle above which the mark will be shown.

![2205](https://files.readme.io/6b14588-chart.jpg "chart.jpg")

## API

Chart markers can be manipulated with websocket messages:

### Create a new mark

```text Javascript
wss.send(JSON.stringify([0, 'n', 12345, {
  type: 'ucm-ui-chart',
  info: {
    type: 'marker_create',
    id: 'mark_0',
    ts: Date.now(), // timestamp in milliseconds
    symbol: 'tBTCUSD', // not required. If not present applies to all symbols
		content: 'lorem <a href="https://www.bitfinex.com/assets/bfx-stacked.png">here</a>', // content to show in tooltip
    color_bg: '#FF1133', // RGB
    color_text: '#FF1133', // RGB
    color_border: '#FF1133', // RGB
    label: 'M', // marker letter
    size_min: 8,
  } 
}]))
```

### Clear all existing marks

```text Javascript
wss.send(JSON.stringify([0, 'n', 12345, {
  type: 'ucm-ui-chart', info: {
  type: 'marker_clear',
} }]))
```

## Fields

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Name
      </th>

      <th>
        Type
      </th>

      <th>
        Required
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        type
      </td>

      <td>
        String, one of [‘marker\_create’, ‘marker\_clear’][‘marker_create’, ‘marker_clear’]
      </td>

      <td>
        yes
      </td>

      <td>
        The type of the action
      </td>
    </tr>

    <tr>
      <td>
        id
      </td>

      <td>
        string
      </td>

      <td>
        yes
      </td>

      <td>
        Unique id of the mark. It’s necessary to allow the UI to distinguish the marks, and to easily determine that the given mark is already added to the chart in a possible scenario in which the same mark is broadcasted multiple times.
      </td>
    </tr>

    <tr>
      <td>
        ts
      </td>

      <td>
        number
      </td>

      <td>
        yes
      </td>

      <td>
        Unix timestamp in milliseconds of the event. The mark of the event will be associated with the candle that overlaps with this moment in time.
      </td>
    </tr>

    <tr>
      <td>
        symbol
      </td>

      <td>
        string
      </td>

      <td>
        no
      </td>

      <td>
        Symbol that the mark applies to e.g. “tBTCUSD”. If not provided, or provided value is “ANY” the mark applies to each existing pair.
      </td>
    </tr>

    <tr>
      <td>
        content
      </td>

      <td>
        string(HTML)
      </td>

      <td>
        no
      </td>

      <td>
        HTML content displayed in the tooltip. Tooltip appears on mark hover and disappears on mark blur. This library is used to sanitize HTML to prevent potentially malicious tags from being injected:\
        [https://www.npmjs.com/package/sanitize-html](https://www.npmjs.com/package/sanitize-html)
      </td>
    </tr>

    <tr>
      <td>
        color\_bg
      </td>

      <td>
        string
      </td>

      <td>
        no
      </td>

      <td>
        Background color of the mark. Must be in a form of RGB color such as “#FF0099”
      </td>
    </tr>

    <tr>
      <td>
        color\_border
      </td>

      <td>
        string
      </td>

      <td>
        no
      </td>

      <td>
        Border color of the mark. Must be in a form of RGB color such as “#FF0099”
      </td>
    </tr>

    <tr>
      <td>
        color\_text
      </td>

      <td>
        string
      </td>

      <td>
        no
      </td>

      <td>
        Text color of the mark. Must be in a form of RGB color such as “#FF0099”. Should not be confused with tooltip text color. (See “label” below)
      </td>
    </tr>

    <tr>
      <td>
        label
      </td>

      <td>
        string with length = 1
      </td>

      <td>
        no
      </td>

      <td>
        Optional single char that is displayed inside the mark circle when it’s zoomed in enough. Note: chart marks tend to become smaller when zooming out, and become bigger when zooming in. See also “size\_min”.
      </td>
    </tr>

    <tr>
      <td>
        size\_min
      </td>

      <td>
        number
      </td>

      <td>
        no
      </td>

      <td>
        Minimum mark size in pixels. See also “label” above.
      </td>
    </tr>
  </tbody>
</Table>

### HTML Sanitize settings

Definition of allowed HTML tags and attributes

```text Javascript
const SANITIZE_SETTINGS = {
 allowedTags: ['h3', 'h4', 'h5', 'h6', 'blockquote', 'p', 'a', 'ul', 'ol',
   'li', 'b', 'i', 'strong', 'em', 'code', 'hr', 'br', 'div',
   'table', 'thead', 'caption', 'tbody', 'tr', 'th', 'td', 'pre', 'img'],
 allowedAttributes: {
   a: ['href', 'name', 'target'],
   img: ['src', 'height', 'width'],
 },
}
```

## Custom Notifications

Broadcasts a custom notification to all connected websockets belonging to the authenticated user.

<Image title="notification-1.png" alt={469} src="https://files.readme.io/aeab2a2-notification-1.png">
  Simple notification
</Image>

## Fields

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Name
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        message
      </td>

      <td>
        Notification content
      </td>
    </tr>

    <tr>
      <td>
        type
      </td>

      <td>
        all, browser, desktop
      </td>
    </tr>

    <tr>
      <td>
        level
      </td>

      <td>
        success, info, warning, error
      </td>
    </tr>

    <tr>
      <td>
        image
      </td>

      <td>
        URL to any image (not supported for desktop notifications on macOS)
      </td>
    </tr>

    <tr>
      <td>
        link
      </td>

      <td>
        URL to open when notification is clicked
      </td>
    </tr>

    <tr>
      <td>
        title
      </td>

      <td>
        Header content
      </td>
    </tr>

    <tr>
      <td>
        ttl
      </td>

      <td>
        Time in milliseconds to display notification for
      </td>
    </tr>

    <tr>
      <td>
        sound: \{ tone: TONE }
      </td>

      <td>
        TONE=tone|wob|tripleChime| tripleBeep|doubleTap|pingUp| pingDown
      </td>
    </tr>
  </tbody>
</Table>

## Functionality

* Display entire message content
* Play a sound, if provided, according to the specified user setting or provided tone (see structure above)
* Display an image, if provided, underneath the message content
* If a link is provided, the notification should open the link
* Display the title, if provided, above the message
* Close after either the provided TTL or the default

```text
wss.send(JSON.stringify([0, 'n', 12345, {
  type: 'ucm-notify-ui', info: {
  type: 'all',
  level: 'success',
  image: 'https://www.bitfinex.com/assets/bfx-stacked.png',
  link: 'http://www.bitfinex.com',
  message: 'This is a test notification',
  sound: {
     tone: 'pingUp',
  }
} }]))
```

<Image title="Screenshot_2018-10-26_14-00-22.png" alt={2216} src="https://files.readme.io/3b3e3a9-Screenshot_2018-10-26_14-00-22.png">
  Chart Markers + Custom notifications from Twitter
</Image>
