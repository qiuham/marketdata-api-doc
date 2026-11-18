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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-notifications'
updated_at: 2026-11-18
---

# Notifications

The Notifications channel is a work in progress that will be used for different changes in status, price alerts, etc.

Subscribe to the account information channel to keep track of your notifications. The account information channel will provide a feed of your notifications for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Notification events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Notification events can be recognised by the 'n' (notification) abbreviation.

```json Update ('n')
[
  0, //CHAN_ID
  "n", //TYPE
  [
    1575282446099, //MTS
    "fon-req", //TYPE
    null, //MESSAGE_ID
    null, //PLACEHOLDER
    [
      //Notification goes here, comes as an array or object and is different per notification
    ], //NOTIFY_INFO
    null, //CODE
    "SUCCESS", //STATUS
    "Submitting funding bid of 1000.0 USD at 0.2000 for 2 days." //TEXT
  ] //NOTIFY_UPDATE_ARRAY
]
```
```javascript on-req / oc-req
notify_info =  [ 
  ID, 
  GID,
  CID,
  SYMBOL, 
  MTS_CREATE, 
  MTS_UPDATE, 
  AMOUNT, 
  AMOUNT_ORIG, 
  TYPE,
  TYPE_PREV,
  _PLACEHOLDER,
  _PLACEHOLDER,
  FLAGS,
  STATUS,
  _PLACEHOLDER,
  _PLACEHOLDER,
  PRICE,
  PRICE_AVG,
  PRICE_TRAILING,
  PRICE_AUX_LIMIT,
  _PLACEHOLDER,
  _PLACEHOLDER,
  _PLACEHOLDER,
  NOTIFY, 
  HIDDEN, 
  PLACED_ID,
  ...
]
```
```javascript uca / price
notify_info = [ 
  KEY, 
  ‘price’, 
  SYMBOL, 
  PRICE, 
  COUNT, 
  DIRECTION 
]
```
```javascript fon-req / foc-req
notify_info = [
  ID,
  SYMBOL,
  MTS_CREATED,
  MTS_UPDATED,
  AMOUNT,
  AMOUNT_ORIG,
  TYPE,
  _PLACEHOLDER,
  _PLACEHOLDER,
  FLAGS,
  STATUS,
  _PLACEHOLDER,
  _PLACEHOLDER,
  _PLACEHOLDER,
  RATE,
  PERIOD,
  NOTIFY,
  HIDDEN,
  _PLACEHOLDER,
  RENEW,
  RATE_REAL,
  ...
]
```

> 🚧 Work In Progress
>
> This section (Notifications) is currently a work in progress, but it will be a way to be alerted as to different changes in status, price alerts, etc

#### Notification update data

| Index | Term                  | Type   | Description                                                                                                                                         |
| :---- | :-------------------- | :----- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[0]  | CHAN\_ID              | Int    | Identification number for the channel subscribtion. Funding trades events are always sent through the account information channel with CHAN\_ID = 0 |
| \[1]  | TYPE                  | String | 'fte' (funding trade executed), 'ftu' (funding trade update)                                                                                        |
| \[2]  | NOTIFY\_UPDATE\_ARRAY | Array  | [Notify update array](#notify-update-arrays-index-2)                                                                                                |

#### Notify update arrays (Index \[2])

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Index</th>
      <th>Field</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>[0]</td><td>MTS</td><td>Int</td><td>Millisecond Time Stamp of the update</td></tr>
    <tr><td>[1]</td><td>TYPE</td><td>String</td><td>Purpose of notification ('on-req', 'oc-req', 'uca', 'fon-req', 'foc-req') - an overview of all types can be found in our <a href="https://docs.bitfinex.com/docs/abbreviations-glossary" title="Abbreviation Glossary">Abbreviation Glossary</a></td></tr>
    <tr><td>[2]</td><td>MESSAGE_ID</td><td>Int</td><td>Unique ID of the message</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[4]</td><td>NOTIFY_INFO</td><td>Array/Object</td><td>A message containing information regarding the notification</td></tr>
    <tr><td>[5]</td><td>CODE</td><td>Null or Integer</td><td>Work in progress</td></tr>
    <tr><td>[6]</td><td>STATUS</td><td>String</td><td>Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...)</td></tr>
    <tr><td>[7]</td><td>TEXT</td><td>String</td><td>Text of the notification</td></tr>
  </tbody>
</table>

<style>
  td:has(div.placeholders) {
    background-color: #ebebeb;
  }

  .placeholders {
    height: 10px;
    text-align: center;
    font-size: 16px;
    line-height: 8px;
  }
</style>
`}</HTMLBlock>

#### Custom Notifications

The following javascript example will allow you to create a custom notification.

```javascript
const obj = [
  0,
  'n',
  MESSAGE_ID, // can be null
  {
    type: 'ucm-test',
    info: {
      foo: 1,
      bar: 2
    }
  }
]

w1.send(JSON.stringify(obj))
```

A custom notification will be broadcasted to every channel that the user is subscribed to.
