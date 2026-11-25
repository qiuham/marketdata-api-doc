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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-input-calc'
updated_at: 2026-11-25
---

# Calc

Send calc requests to trigger specific calculations.

Calc requests can be sent through WebSocket to trigger specific updates from the server. Calculations can be requested by constructing a payload using the "calc" abbreviation. The calc parameters need to be included in the payload as an array. Please look to the sidebar for example payloads and example updates.

Calc requests require you to run authentication code along with additional code for sending the payload. The authentication code can be found on our [Authenticated Channels](https://docs.bitfinex.com/docs/ws-auth) page and the additional code for inputs can be found on the [Websocket Inputs](https://docs.bitfinex.com/reference/ws-auth-input) page. Please note that in the Websocket Inputs example, the inputDetails are sent as an object. For calc requests, the inputDetails will need to be sent as an array.

```javascript Payload Examples
//Single Calc Request
[
  0,
  "calc",
  null,
  [
    ["margin_base"]
  ]
]

//Multiple Calc Requests
[
  0,
  "calc",
  null,
  [
    ["margin_base"],
    ["margin_sym_tBTCUSD"],
    ["funding_sym_fUSD"],
    ["position_tBTCUSD"],
    ["wallet_margin_BTC"],
    ["balance"]
  ]
]
```
```javascript Updates ('miu', 'fiu', 'pu', 'wu', 'bu')
//Margin Base Update
[
  CHAN_ID,
  TYPE, // 'miu'
  [
    'base',
    [
      USER_PL, 
      USER_SWAPS, 
      MARGIN_BALANCE, 
      MARGIN_NET,
      MARGIN_REQUIRED
      ...
    ]
   ]
]

[0,"miu",["base",[-13.014640000000007,0,49331.70267297,49318.68803297,27]]]

//Margin Symbol Update
[
  CHAN_ID,
  TYPE, // 'miu'
  [
    'sym',
    SYMBOL,
    [
      TRADABLE_BALANCE,
      GROSS_BALANCE,
      BUY,
      SELL,
      ...
    ]
   ]
]
  
[0,"miu",["sym","tETHUSD",[149361.09689202666,149639.26293509,830.0182168075556,895.0658432466332,null,null,null,null]]]

//Funding Info Update  
  [
  CHAN_ID, 
  'fiu',
  [
    'sym',
    SYMBOL
    [
      YIELD_LOAN,
      YIELD_LEND,
      DURATION_LOAN,
      DURATION_LEND,
      ...
    ],
    ...
  ]
]
    
//Positions Update   
[
  CHAN_ID, 
  TYPE, // <‘pn’, ’pu’, ‘pc’>
  [
      SYMBOL, 
      STATUS, 
      AMOUNT, 
      BASE_PRICE, 
      MARGIN_FUNDING, 
      MARGIN_FUNDING_TYPE,
      PL,
      PL_PERC,
      PRICE_LIQ,
      LEVERAGE,
      FLAG,
      POSITION_ID,
      MTS_CREATE,
      MTS_UPDATE,
      PLACEHOLDER,
      TYPE,
      PLACEHOLDER,
      COLLATERAL,
      COLLATERAL_MIN,
      META
  ]
]

[0,"pu",["tETHUST","ACTIVE",0.2,153.71,0,0,-0.07944800000000068,-0.05855181835925015,67.52755254906451,1.409288545397275,null,142420429,null,null,null,0,null,0,0,{"reason":"TRADE","order_id":34934099168,"order_id_oppo":34934090814,"liq_stage":null,"trade_price":"153.71","trade_amount":"0.2"}]]
    
//Wallets Update 
[
  CHAN_ID, 
  TYPE, //'wu'
  [
    WALLET_TYPE, 
    CURRENCY, 
    BALANCE, 
    UNSETTLED_INTEREST,
    BALANCE_AVAILABLE,
    DESCRIPTION,
    META
  ]
]

[0,"wu",["exchange","BTC",1.61169184,0,null,"Exchange 0.01 BTC for USD @ 7804.6",{"reason":"TRADE","order_id":34988418651,"order_id_oppo":34990541044,"trade_price":"7804.6","trade_amount":"0.01"}]]
    
//Balance Update   
[
  CHAN_ID,
  TYPE, //'bu'
  [
    AUM,
    AUM_NET,
    ...
  ]
]
 
[0,"bu",[4131.85,4131.85]]
```

## Available Calc Requests:

* `margin_base`\
  Requests a [Margin Info](https://docs.bitfinex.com/reference/ws-auth-margin-info)  update for 'base'. ('miu')

* `margin_sym_SYMBOL`\
  Requests a [Margin Info](https://docs.bitfinex.com/reference/ws-auth-margin-info)  update for 'sym'. ('miu')

* `funding_sym_SYMBOL`\
  Requests a [Funding Info](https://docs.bitfinex.com/reference/ws-auth-funding) update. ('fiu')

* `position_SYMBOL`\
  Requests a [Positions](https://docs.bitfinex.com/reference/ws-auth-positions)  update for a specific pair. ('pu')

* `wallet_WALLET-TYPE_CURRENCY`\
  Requests a [Wallets](https://docs.bitfinex.com/reference/ws-auth-wallets)  update for a specific currency. ('wu')

* `balance`\
  Requests a [Balance Info](https://docs.bitfinex.com/reference/ws-auth-balance-info)  update. ('bu')

> 🚧 Limitations
>
> Calculations are on demand, so we no longer need to stream unnecessary data.
>
> * Websocket server allows up to 30 calculations per batch. If the client sends too many concurrent requests (or tries to spam) requests, it will receive an error and potentially a disconnection.
>
> * The Websocket server performs a maximum of 8 calculations per second per client.
