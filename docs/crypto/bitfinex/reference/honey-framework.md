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
source_url: 'https://docs.bitfinex.com/reference/honey-framework'
updated_at: 2026-11-18
---

# Honey Framework

The Bitfinex Honey Framework is a collection of libraries that provide functionality to automate trading operations. It is composed of two major components, `bfx-hf-algo` and `bfx-hf-strategy`, along with various other supporting libraries.

Two isolated systems are provided, one for developing algorithmic orders and another for trading strategies. While similar, they are separated by their use cases; algorithmic orders mirror the functionality of the standard atomic orders available on the Bitfinex platform, being submitted through the trading UI with preset parameters and executing to completion. Trading strategies on the other hand are meant to be run programatically and are long-lived, executing on the live markets until stopped.

To complement these systems, a trading indicator library with 40+ indicators is available as `bfx-hf-indicators`. The full list of Honey Framework libraries is below:

* [`bfx-hf-algo`](https://github.com/bitfinexcom/bfx-hf-algo) - algorithmic orders implementation
* [`bfx-hf-algo-server`](https://github.com/bitfinexcom/bfx-hf-algo-server) - standalone server for executing algo orders from the Bitfinex UI
* [`bfx-hf-strategy`](https://github.com/bitfinexcom/bfx-hf-strategy) - trading strategy library
* [`bfx-hf-backtest`](https://github.com/bitfinexcom/bfx-hf-backtest) - utility library for running backtests on trading strategies
* [`bfx-hf-util`](https://github.com/bitfinexcom/bfx-hf-util) - general internal utility library
* [`bfx-hf-models`](https://github.com/bitfinexcom/bfx-hf-models) - DB models shared by all HF libraries

The HF makes use of a custom Node.JS API implementation available at [`bfx-api-node-core`](https://github.com/bitfinexcom/bfx-api-node-core), which is separate from the primary `bitfinex-api-node` library.

## Algorithmic Orders

As part of the algorithmic order system, four algo orders are provided within `bfx-hf-algo`: `Accumulate/Distribute`, `TWAP`, `Iceberg`, and `Ping/Pong`. These orders can be either managed using `bfx-hf-algo` or submitted via the trading UI by using `bfx-hf-algo-server`.

### Managing Algo Orders via `bfx-hf-algo`

Algo orders are managed by a class named `AOHost`, which maintains a connection to the Bitfinex API and routes received events to all running algo orders, managing their reactions and handling order submission. To use, create an `AOHost` instance and call `startAO(id, args)`:

```js
const {
  AOHost, PingPong, Iceberg, TWAP, AccumulateDistribute
} = require('bfx-hf-algo')

const host = new AOHost({
  aos: [PingPong, Iceberg, TWAP, AccumulateDistribute],
  apiKey: '...',
  apiSecret: '...',
  wsURL: '...',
  restURL: '...',
})

host.on('ao:start', (instance) => {
  const { state = {} } = instance
  const { id, gid } = state
  console.log('started AO %s [gid %s]', id, gid)
})

host.on('ao:stop', (instance) => {
  const { state = {} } = instance
  const { id, gid } = state
  console.log('stopped AO %s [gid %s]', id, gid)
})

host.on('ws2:auth:error', (packet) => {
  console.log('error authenticating: %j', packet)
})

host.on('error', (err) => {
  console.log('error: %s', err)
})

host.once('ws2:auth:success', async () => {

  // Start an Iceberg order instance
  const gid = await host.startAO('bfx.iceberg', {
    symbol: 'tBTCUSD',
    price: 21000,
    amount: -0.5,
    sliceAmount: -0.1,
    excessAsHidden: true,
    orderType: 'LIMIT',
    submitDelay: 150,
    cancelDelay: 150,
    _margin: false,
  })

  // later, host.stopAO(gid)
})
```

### Algo Order Host

The `AOHost` class provides a wrapper around the algo order system, and manages lifetime events/order execution. Internally it hosts a `Manager` instance from `bfx-api-node-core` for communication with the Bitfinex API, and listens for websocket stream events in order to update order state/trigger algo order events.

Execution is handled by an event system, with events being triggered by Bitfinex API websocket stream payloads, and the algo orders themselves.

The host must be instantiated with a valid API key/secret pair, and websocket/REST endpoints, along with an optional proxy agent. These parameters are the same as those passed to the `bfx-api-node-core` `Manager` constructor. Note that the `Manager` is instantiated with the dead-man-switch active (dms: 4).

To start/stop algo orders, `gid = startAO(id, args)` and `stopAO(gid)` methods are provided, with the generated group ID (`gid`) being the same as that used for all atomic orders created by the individual algo orders.

See the above usage example for instantiation

## Algo Order System

Algorithmic orders are defined by an ID/Name pair, a set of meta functions describing the order, and a set of event handlers to be triggered during the orders lifetime/execution. A `defineAlgoOrder` helper is provided to construct the final AO definition object:

```js
const AO = defineAlgoOrder({
  id: 'some.ao.identifier',
  name: 'Descriptive AO Label',

  // meta functions describing the order/execution environment
  meta: {
    validateParams,  // validates processed parameters
    processParams,   // prepares raw parameters for execution
    declareEvents,   // declares/hooks up custom internal event handlers
    declareChannels, // declares needed data channels, to be managed by the AO host
    getUIDef,        // returns the Bitfinex Order Form definition schema
    genOrderLabel,   // constructs a label for generated atomic orders
    genPreview,      // generates preview orders for rendering in the bfx UI
    initState,       // creates the initial AO state object
    serialize,       // serializes state for DB persistence
    unserialize,     // unserializes loaded DB states for execution
  },

  events: {
    self: {
      // internal events, bound in declareEvents()
    },

    life: {
      start, // triggered on execution start, should handle initialisation
      stop,  // triggered on execution stop, should handle teardown
    },

    orders: {
      order_snapshot, // triggered upon receival of an account order snapshot
      order_new,      // triggered when a new order is opened
      order_update,   // triggered when an order is updated
      order_close,    // triggered when an order is closed
      order_fill,     // triggered on any order fill (order new/update/close)
      order_cancel,   // triggered when an order is closed via cancellation
    },

    data: {
      managedCandles, // triggered by receipt of a managed candle dataset
      managedBook,    // triggered by receipt of a managed order book
      notification,   // triggered by receipt of a notification
      candles,        // triggered by receipt of candles
      ticker,         // triggered by receipt of a ticker
      trades,         // triggered by receipt of trades
      book,           // triggered by receipt of an order book snapshot/update
    },

    errors: {
      minimum_size,   // triggered when an order fails due to being below the
                      // minimum size for its symbol; the AO may need to be stopped
    }
  }
})
```

### AO Event Handlers & Helpers

All event handlers receive the same arguments: `(instance = {}, ...args)`. The instance contains two objects, `{ state = {}, h = {} }` with `state` being the current AO state, and `h` being a helper object.

The provided helpers are:

* `debug(str, ...args)` - for logging information to the console, tagged by AO GID
* `emitSelf(eventName, ...args)` - triggers an event on the 'self' section
* `emitSelfAsync(eventName, ...args)` - same as `emitSelf` but operates on next tick
* `emit(eventName, ...args)` - raw event emitter, i.e. `emit('life:start')`
* `emitAsync(eventName, ...args)` - same as `emit` but operates on next tick
* `notifyUI(level, message)` - generates and sends a notification which appears on the Bitfinex UI
* `cancelOrderWithDelay(state, delay, order)` - takes current algo state, delay in ms
* `cancelAllOrdersWithDelay(state, delay)` - cancels all active atomic orders on the AO state, delay in ms
* `submitOrderWithDelay(state, delay, order)` - takes current algo state, submits a new order, delay in ms
* `declareEvent(instance, host, eventName, path)` - declares an internal AO event, see section below
* `declareChannel(instance, host, channel, filter)` - declares a required data channel, see section below
* `updateState(instance, update)` - update the current state for an AO instance

### Custom AO Event Handlers

To declare custom events to be triggered by the `emitSelf` or `emitSelfAsync` helpers, use the `declareEvent` helper inside of the `declareEvents` meta method in order to register the event names on AO startup. For an example, see the `Iceberg` event definition handler:

```js
module.exports = (instance = {}, host) => {
  const { h = {} } = instance
  const { declareEvent } = h

  // All declared events are expected to be handled on the 'self' section, but can have any path/label

  // Map self:submit_order to the 'submit_order' handler
  declareEvent(instance, host, 'self:submit_order', 'submit_order')

  // Map self:interval_tick to the 'interval_tick' handler
  declareEvent(instance, host, 'self:interval_tick', 'interval_tick')
}
```

Later, these events are triggered within other `Iceberg` event handlers, such as `submit_orders` within the `life:start` handler:

```js
module.exports = async (instance = {}) => {
  const { h = {} } = instance
  const { emitSelf } = h

  // ...

  await emitSelf('submit_orders')
}
```

### Subscribing to Data Channels

To subscribe to Bitfinex websocket API data channels, use the `declareChannel` helper within the `declareChannels()` meta method. Channel subscribe/unsubscribe calls will be handled automatically by the AO host during execution, with the relevant data being passed to the `data` section event handlers upon receival. For an example, see the `TWAP` channel declaration:

```js
module.exports = async (instance = {}, host) => {
  const { h = {}, state = {} } = instance
  const { args = {} } = state
  const { symbol, priceTarget } = args
  const { declareChannel } = h

  if (hasTradeTarget(args)) {
    await declareChannel(instance, host, 'trades', { symbol })
  } else if (hasOBTarget(args)) {
    await declareChannel(instance, host, 'book', {
      symbol,
      prec: 'R0',
      len: '25'
    })
  } else {
    throw new Error(`invalid price target ${priceTarget}`)
  }
}
```

## Trading Strategies

Trading strategies consist of a set of position management methods and an architecture compatible with `bfx-hf-data-server` and `bfx-hf-backtest` for backtests on historical candle/trade data, which can be transitioned seamlessly to trading on the live markets.

Strategies written using this framework must define a set of update methods, called on each tick (with either a trade or a candle), along with a set of indicators which are automatically updated on each tick. The indicators are made available to the strategy methods, and can be queried to direct trading behavior.

### Defining a Strategy

The `define` method is provided to construct a trading strategy from a set of indicators & update methods. Strategies created with it can be used with `bfx-hf-backtest` or with the `exec` method to run on the live market. An example strategy follows below:

```js
const { SYMBOLS, TIME_FRAMES } = require('bfx-hf-util')
const { EMA } = require('bfx-hf-indicators')

HFS.define({
  id: 'ema_cross',
  name: 'ema_cross',
  symbol: SYMBOLS.BTC_USD,
  tf: TIME_FRAMES.ONE_MINUTE,

  indicators: {
    emaL: new EMA([100]),
    emaS: new EMA([20])
  },

  onEnter: require('./on_enter'),
  onUpdateLong: require('./on_update_long'),
  onUpdateShort: require('./on_update_short')
})
```

The above strategy defines two EMA indicators, `emaL` and `emaS`, with periods of 100 and 20 respectively, and 3 update methods; In total, 5 update methods are available:

* `onEnter` - called when no position is open
* `onUpdateLong` - called when a long position is open
* `onUpdateShort` - called when a short position is open
* `onUpdate` - called when any position is open
* `onPriceUpdate` - called on every tick

### Update Handlers

All update handlers must be asynchronous, and receive the same arguments of `(state = {}, update = {})`. The update has the following fields:

* `type` - 'candle' or 'trade', indicating which fields are available
* `mts` - timestamp, in ms
* `price` - candle or trade price (depends on `candlePrice` strategy setting)
* for candles, `open`, `high`, `low`, `close`, and `vol` are provided

Update handlers must return the next state object after performing any actions, or the current state object if no modifications were made.

The `state` object can be queried for historical candle data, indicators & indicator values, open positions, and previous strategy trades. Various helpers are provided to query this data; for an example, see the EMA cross example `onEnter` handler below:

```js
const _get = require('lodash/get')
const HFS = require('bfx-hf-strategy')

module.exports = async (state = {}, update = {}) => {
  const { price, mts } = update
  const i = HFS.indicators(state)
  const iv = HFS.indicatorValues(state)
  const { emaS } = i // full indicator object
  const l = iv.emaL
  const s = iv.emaS

  // Note that the default strategy symbol is used if no symbol is specified
  if (emaS.crossed(l)) {
    if (s > l) {
      return HFS.openLongPositionMarket(state, {
        mtsCreate: mts,
        amount: 1,
        price
      })
    } else {
      return HFS.openShortPositionMarket(state, {
        mtsCreate: mts,
        amount: 1,
        price
      })
    }
  }

  return state
}
```

### Managing Positions

Within the update handlers, several async helpers are available to open/update/close positions:

* `openLongPositionMarket(state, args = {})`
* `openLongPositionLimit(state, args = {})`
* `openLongPosition(state, args = {})`
* `openShortPositionMarket(state, args = {})`
* `openShortPositionLimit(state, args = {})`
* `openShortPosition(state, args = {})`
* `openPosition(state, args = {})`
* `updateLongPositionMarket(state, args = {})`
* `updateLongPositionLimit(state, args = {})`
* `updateLongPosition(state, args = {})`
* `updateShortPositionMarket(state, args = {})`
* `updateShortPositionLimit(state, args = {})`
* `updateShortPosition(state, args = {})`
* `updatePosition(state, args = {})`
* `closePositionMarket(state, args = {})`
* `closePositionLimit(state, args = {})`
* `closePosition(state, args = {})`

The `price` and `mtsCreate` timestamp must both be provided to all update handlers, even those operating with MARKET orders, in order to record the price and timestamp during backtests. If these are not provided, backtests run via `bfx-hf-backtest` will fail.

### Executing on Live Markets

To run a strategy against the live marketplace, attach a `WSv2` instance from `bitfinex-api-node` to the strategy object on `ws` and call the `exec` method to bind the Bitfinex API listeners to the various strategy update methods:

```js
const debug = require('debug')('bfx:hf:strategy:example:exec')
const HFS = require('bfx-hf-strategy')
const { SYMBOLS, TIME_FRAMES } = require('bfx-hf-util')
const { Manager } = require('bfx-api-node-core')
const WDPlugin = require('bfx-api-node-plugin-wd')
const S = require('./some/strategy')

const m = new Manager({
  plugins: [WDPlugin({ // automatically reconnect if the connection drops
    packetWDDelay: 30000,
  })],

  apiKey: '...',
  apiSecret: '...',
  transform: true,
})

const run = async () => {
  const strat = await S({ /* strategy arguments */ })

  m.onWS('open', {}, (state = {}) => {
    debug('open')
  })

  m.onceWS('event:auth:success', {}, async (authEvent, ws) => {
    debug('authenticated')
    debug('executing strategy...')

    strat.ws = ws // attach websocket

    await HFS.exec(strat, m, {
      symbol: SYMBOLS.ETH_USD,
      tf: TIME_FRAMES.ONE_MINUTE,
      includeTrades: true,
    })
  })

  debug('opening socket...')

  m.openWS()
}

try {
  run()
} catch (err) {
  debug('error: %s', err)
}
```

## Indicators

Included with the HF is a library of +40 indicators, [bfx-hf-indicators](https://github.com/bitfinexcom/bfx-hf-indicators) which are leveraged to create algo orders/trading strategies with complex behaviors that react to market movements in real time.

These indicators are packaged separately from the other components of the HF, and can be used independently in other projects. They support incremental updates, both from trade and candle data (depending on the indicator). All indicators provide the same set of base methods:

* `reset()` - clears indicator values
* `update(value or candle)` - updates the current indicator value with a different data point
* `add(value or candle)` - adds a new data point/value to the indicator
* `l()` - returns the number of available indicator values
* `v()` - returns the current indicator value
* `prev(n = 1)` - returns the nth previous indicator value

#### Indicator Seeding

All indicators have a seed period which should be respected before valid data can be obtained, which can be read via `i.getSeedPeriod()`

#### Indicator Data Types

To query which type of data an indicator requires, `getDataType()` and `getDataKey()` are available. The data type can be either `'trade'`, `'candle'`, or `'*'` to signal that both are acceptable. For candle data, the data key will be either `'open`', `'high'`, `'low'`, or `'close'`.

### Indicator Metadata

All indicators provide a set of meta values describing how they should be rendered on a chart. Specifically:

* `Indicator.args` - an array describing the indicator arguments, with objects of the form \{ label, default }
* `Indicator.ui` - an object describing how to render the indicator, details below
* `Indicator.id` - the internal unique identifier for the indicator
* `Indicator.label` - the short, uppercase label for the indicator
* `Indicator.humanLabel` - the complete descriptive indicator label

As an example, here is the metadata for bollinger bands:

```js
BollingerBands.id = 'bbands'
BollingerBands.label = 'BB'
BollingerBands.humanLabel = 'Bollinger Bands'
BollingerBands.ui = {
  position: 'overlay',
  type: 'bbands'
}

BollingerBands.args = [{
  label: 'Period',
  default: 20,
}, {
  label: 'Multiplier',
  default: 2,
}]
```

### Indicator Rendering

For each indicator, the `Indicator.ui` field contains an object describing how it should render on a chart, with `position` and `type` keys. Two positions are possible, `'external'` to be shown below a chart and `'overlay'` to be shown on top of candle data. Supported types are `'line'`, `'lines'`, `'bbands'`, `'rsi'`, and `'macd'`, with indicators of type `'lines'` having an extra `lines: [...]` field naming the indicator values that should be plotted.

For indicators with multiple values on each data point, such as Envelope, the `lines` keys should correspond to the keys on the indicator data points:

```js
Envelope.ui = {
  position: 'overlay',
  type: 'lines',
  lines: ['upper', 'basis', 'lower']
}
```

### Example Usage

```js
const { RSI } = require('bfx-hf-indicators')

const rsi = new RSI([14])

rsi.add(14000)
rsi.add(14010)
rsi.add(14025)
rsi.add(14035)
// ...
// 8 more data points
// ...
rsi.add(13998)
rsi.add(13952)

const v = rsi.v() // query current RSI(14) value
```
