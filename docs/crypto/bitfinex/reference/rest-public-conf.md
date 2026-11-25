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
source_url: 'https://docs.bitfinex.com/reference/rest-public-conf'
updated_at: 2026-11-25
---

# Configs

Fetch site configuration data

#### Mapping Requests

You can use a mapping request to retrieve a mapping of symbols to related details. For example, you can send a request to *pub:map:currency:label* to map symbols to their verbose friendly names (e.g. BTC -> Bitcoin)

| Request                   | Description                                                                                                         |
| :------------------------ | :------------------------------------------------------------------------------------------------------------------ |
| pub:map:currency:sym      | Map symbols to their API symbols (e.g. DSH -> DASH)                                                                 |
| pub:map:currency:label    | Maps symbols to their verbose friendly name (e.g. BTC -> Bitcoin                                                    |
| pub:map:currency:unit     | Maps symbols to their unit of measure (where applicable) (e.g. IOT -> MegaIOTA)                                     |
| pub:map:currency:undl     | Maps derivatives symbols to their underlying currency (e.g. BTCF0 -> BTC)                                           |
| pub:map:currency:pool     | Maps symbols to the underlying network/protocol they operate on (e.g.  BAT ->  ETH)                                 |
| pub:map:currency:explorer | Maps symbols to their recognised block explorer URLs (e.g. ETH -> <https://etherscan.io>)                           |
| pub:map:currency:tx:fee   | Maps currencies to their current withdrawal fee amount                                                              |
| pub:map:tx:method         | Maps currencies to their appropriate method(s) for API withdrawals (e.g. UST -> \[TETHERUSDTBCH, TETHERUSDTALG, …]) |

#### Listing Requests

You can use a listing request to retrieve lists of currencies, trading pairs, or leaderboard competitions.

| Request                  | Description                                                          |
| :----------------------- | :------------------------------------------------------------------- |
| pub:list:pair:exchange   | Fetch a list of valid exchange trading pairs                         |
| pub:list:pair:margin     | Fetch a list of valid margin trading pairs                           |
| pub:list:pair:futures    | Fetch a list of valid derivative pairs                               |
| pub:list:pair:securities | Fetch a list of valid securities pairs                               |
| pub:list:currency        | Fetch a list of all currencies available on the platform             |
| pub:list:currency:margin | Fetch a list of all currencies that can be used as margin collateral |
| pub:list:competitions    | Fetch a list of all active leaderboard competitions                  |

#### Info Requests

You can use an info request to fetch detailed information about pairs or transactions

| Request               | Description                                                                                                                                                                                                               | Mapping                                                                                                                                                                                                                                                        |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pub:info:pair         | Fetches an array of market information for each trading pair                                                                                                                                                              | \[\[PAIR, \[FIRST\_TRADE, PLACEHOLDER, PLACEHOLDER, MIN\_ORDER\_SIZE, MAX\_ORDER\_SIZE, PLACEHOLDER, PLACEHOLDER, PLACEHOLDER, INITIAL\_MARGIN, MIN\_MARGIN, PLACEHOLDER, PLACEHOLDER]],...]                                                                   |
| pub:info:pair:futures | Fetches an array of market information for each derivative trading pair                                                                                                                                                   | \[\[PAIR, \[FIRST\_TRADE, PLACEHOLDER, PLACEHOLDER, MIN\_ORDER\_SIZE, MAX\_ORDER\_SIZE, PLACEHOLDER, PLACEHOLDER, PLACEHOLDER, INITIAL\_MARGIN, MIN\_MARGIN]],...]                                                                                             |
| pub:info:tx:status    | Fetches an array showing the wallet status for each currency for deposits and withdrawals (1 = active, 0 = maintenance) Also shows if payment IDs are allowed for deposits and withdrawals (1 = allowed, 0 = not allowed) | \[METHOD, DEP\_STATUS, WD\_STATUS, PH, PH, PH, PH, PAYMENT\_ID\_DEP, PAYMENT\_ID\_WD, PH, PH, DEPOSIT\_CONFIRMATIONS\_REQUIRED]\[METHOD, DEP\_STATUS, WD\_STATUS, PH, PH, PH, PH, PAYMENT\_ID\_DEP, PAYMENT\_ID\_WD, PH, PH, DEPOSIT\_CONFIRMATIONS\_REQUIRED] |

#### Other Requests

Requests that aren't grouped in the Map, List, or Info categories.

| Request         | Description                                                            |
| :-------------- | :--------------------------------------------------------------------- |
| pub:spec:margin | Fetches lists of active haircuts and risk coefficients on margin pairs |
| pub:fees        | Fetch derivatives fees config                                          |

#### Requesting multiple configurations

Instead of performing a request for each configuration item, it is possible to fetch multiple configurations in a single request. To do this, append each request into a single string separated by comma's without any spaces.

Example of a multi-request that will fetch both margin and exchange trading pairs:<br />pub:list:pair:exchange,pub:list:pair:margin

**Ratelimit**: 90 req/min

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "api-settings-public",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api-pub.bitfinex.com/v2"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/conf/pub:{Action}:{Object}:{Detail}": {
      "get": {
        "summary": "Configs",
        "description": "Fetch site configuration data",
        "operationId": "rest-public-conf",
        "parameters": [
          {
            "name": "Action",
            "in": "path",
            "description": "**Valid action values:** : 'map', 'list', 'info', 'fees', 'spec'",
            "schema": {
              "type": "string",
              "default": "list"
            },
            "required": true
          },
          {
            "name": "Object",
            "in": "path",
            "description": "**Valid object values for the map action:** 'currency', 'tx'.<br/> **Valid object values for the list action:** 'currency', 'pair', 'competitions'.<br/> **Valid object values for the info action:** 'pair', 'tx'<br/>**Valid object values for the fees action:** none<br/>**Valid object values for the spec action:** 'margin'",
            "schema": {
              "type": "string",
              "default": "pair"
            },
            "required": true
          },
          {
            "name": "Detail",
            "in": "path",
            "description": "***The detail parameter is only required for the below action:object values:***<br/>A **map:currency** request requires one of the following **detail** values:<br/>'sym', 'label', 'unit', 'undl', 'pool', 'explorer'.<br/> A **map:tx** request requires the following **detail** value:<br/>'method'.<br/>A **list:pair** request requires one of the following **detail** values:<br/>'exchange', 'margin', 'futures', 'securities' </br> A **list:currency** request can optionally use the following **detail** value:<br/>'margin'.<br/> A **info:tx** request requires the following **detail** value:<br/>'status'.<br/>",
            "schema": {
              "type": "string",
              "default": "exchange"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "pub:map:currency:sym": {
                    "value": "[\n    [\n        [\n            \"ABS\",\n            \"ABYSS\"\n        ],\n        [\n            \"AIO\",\n            \"AION\"\n        ],\n        [\n            \"AMP\",\n            \"AMPL\"\n        ],\n        [\n            \"ATO\",\n            \"ATOM\"\n        ],\n        [\n            \"BAB\",\n            \"BCH\"\n        ],\n        [\n            \"CNHT\",\n            \"CNHt\"\n        ],\n        [\n            \"CSX\",\n            \"CS\"\n        ],\n        [\n            \"CTX\",\n            \"CTXC\"\n        ],\n        [\n            \"DAD\",\n            \"EDGE\"\n        ],\n        [\n            \"DAT\",\n            \"DATA\"\n        ],\n        [\n            \"DRN\",\n            \"DRGN\"\n        ],\n        [\n            \"DSH\",\n            \"DASH\"\n        ],\n        [\n            \"DTX\",\n            \"DT\"\n        ],\n        [\n            \"EUS\",\n            \"EURS\"\n        ],\n        [\n            \"EUT\",\n            \"EURt\"\n        ],\n        [\n            \"GSD\",\n            \"GUSD\"\n        ],\n        [\n            \"IOS\",\n            \"IOST\"\n        ],\n        [\n            \"IOT\",\n            \"IOTA\"\n        ],\n        [\n            \"LBT\",\n            \"LBTC\"\n        ],\n        [\n            \"LES\",\n            \"LEO-EOS\"\n        ],\n        [\n            \"LET\",\n            \"LEO-ERC20\"\n        ],\n        [\n            \"MIT\",\n            \"MITH\"\n        ],\n        [\n            \"MNA\",\n            \"MANA\"\n        ],\n        [\n            \"NCA\",\n            \"NCASH\"\n        ],\n        [\n            \"OMN\",\n            \"OMNI\"\n        ],\n        [\n            \"PAS\",\n            \"PASS\"\n        ],\n        [\n            \"POY\",\n            \"POLY\"\n        ],\n        [\n            \"QSH\",\n            \"QASH\"\n        ],\n        [\n            \"QTM\",\n            \"QTUM\"\n        ],\n        [\n            \"RBT\",\n            \"RBTC\"\n        ],\n        [\n            \"SCR\",\n            \"XD\"\n        ],\n        [\n            \"SNG\",\n            \"SNGLS\"\n        ],\n        [\n            \"SPK\",\n            \"SPANK\"\n        ],\n        [\n            \"STJ\",\n            \"STORJ\"\n        ],\n        [\n            \"TSD\",\n            \"TUSD\"\n        ],\n        [\n            \"UDC\",\n            \"USDC\"\n        ],\n        [\n            \"USK\",\n            \"USDK\"\n        ],\n        [\n            \"UST\",\n            \"USDt\"\n        ],\n        [\n            \"USTF0\",\n            \"USDt0\"\n        ],\n        [\n            \"UTN\",\n            \"UTNP\"\n        ],\n        [\n            \"VSY\",\n            \"VSYS\"\n        ],\n        [\n            \"WBT\",\n            \"WBTC\"\n        ],\n        [\n            \"XCH\",\n            \"XCHF\"\n        ],\n        [\n            \"YGG\",\n            \"YEED\"\n        ],\n        [\n            \"YYW\",\n            \"YOYOW\"\n        ]\n    ]\n]"
                  },
                  "pub:list:pair:exchange": {
                    "value": "[\n    [\n        \"ABSETH\",\n        \"ABSUSD\",\n        \"AGIBTC\",\n        \"AGIETH\",\n        \"AGIUSD\",\n        \"AIDBTC\",\n        \"AIDETH\",\n        \"AIDUSD\",\n        \"AIOBTC\",\n        \"AIOETH\",\n        \"AIOUSD\",\n        \"ALGBTC\",\n        \"ALGUSD\",\n        \"ALGUST\",\n        \"AMPBTC\",\n        \"AMPUSD\",\n        \"AMPUST\",\n        \"ANTBTC\",\n        \"ANTETH\",\n        \"ANTUSD\",\n        \"ASTETH\",\n        \"ASTUSD\",\n        \"ATMBTC\",\n        \"ATMETH\",\n        \"ATMUSD\",\n        \"ATOBTC\",\n        \"ATOETH\",\n        \"ATOUSD\",\n        \"AUCBTC\",\n        \"AUCETH\",\n        \"AUCUSD\",\n        \"AVTBTC\",\n        \"AVTETH\",\n        \"AVTUSD\",\n        \"BABBTC\",\n        \"BABUSD\",\n        \"BABUST\",\n        \"BATBTC\",\n        \"BATETH\",\n        \"BATUSD\",\n        \"BBNETH\",\n        \"BBNUSD\",\n        \"BCIBTC\",\n        \"BCIUSD\",\n        \"BFTBTC\",\n        \"BFTETH\",\n        \"BFTUSD\",\n        \"BNTBTC\",\n        \"BNTETH\",\n        \"BNTUSD\",\n        \"BOXETH\",\n        \"BOXUSD\",\n        \"BSVBTC\",\n        \"BSVUSD\",\n        \"BTC:CNHT\",\n        \"BTCEUR\",\n        \"BTCGBP\",\n        \"BTCJPY\",\n        \"BTCUSD\",\n        \"BTCUST\",\n        \"BTCXCH\",\n        \"BTGBTC\",\n        \"BTGUSD\",\n        \"BTTBTC\",\n        \"BTTUSD\",\n        \"CBTBTC\",\n        \"CBTETH\",\n        \"CBTUSD\",\n        \"CLOBTC\",\n        \"CLOUSD\",\n        \"CNDBTC\",\n        \"CNDETH\",\n        \"CNDUSD\",\n        \"CNH:CNHT\",\n        \"CNNETH\",\n        \"CNNUSD\",\n        \"CSXETH\",\n        \"CSXUSD\",\n        \"CTXBTC\",\n        \"CTXETH\",\n        \"CTXUSD\",\n        \"DADBTC\",\n        \"DADETH\",\n        \"DADUSD\",\n        \"DAIBTC\",\n        \"DAIETH\",\n        \"DAIUSD\",\n        \"DATBTC\",\n        \"DATETH\",\n        \"DATUSD\",\n        \"DGBBTC\",\n        \"DGBUSD\",\n        \"DGXETH\",\n        \"DGXUSD\",\n        \"DRNETH\",\n        \"DRNUSD\",\n        \"DSHBTC\",\n        \"DSHUSD\",\n        \"DTABTC\",\n        \"DTAETH\",\n        \"DTAUSD\",\n        \"DTHBTC\",\n        \"DTHETH\",\n        \"DTHUSD\",\n        \"DTXUSD\",\n        \"DTXUST\",\n        \"DUSK:BTC\",\n        \"DUSK:USD\",\n        \"EDOBTC\",\n        \"EDOETH\",\n        \"EDOUSD\",\n        \"ELFBTC\",\n        \"ELFETH\",\n        \"ELFUSD\",\n        \"ENJETH\",\n        \"ENJUSD\",\n        \"EOSBTC\",\n        \"EOSETH\",\n        \"EOSEUR\",\n        \"EOSGBP\",\n        \"EOSJPY\",\n        \"EOSUSD\",\n        \"EOSUST\",\n        \"ESSBTC\",\n        \"ESSETH\",\n        \"ESSUSD\",\n        \"ETCBTC\",\n        \"ETCUSD\",\n        \"ETHBTC\",\n        \"ETHEUR\",\n        \"ETHGBP\",\n        \"ETHJPY\",\n        \"ETHUSD\",\n        \"ETHUST\",\n        \"ETPBTC\",\n        \"ETPETH\",\n        \"ETPUSD\",\n        \"EUSETH\",\n        \"EUSUSD\",\n        \"EUTEUR\",\n        \"EUTUSD\",\n        \"EVTUSD\",\n        \"FOAETH\",\n        \"FOAUSD\",\n        \"FSNBTC\",\n        \"FSNETH\",\n        \"FSNUSD\",\n        \"FTTUSD\",\n        \"FTTUST\",\n        \"FUNBTC\",\n        \"FUNETH\",\n        \"FUNUSD\",\n        \"GENETH\",\n        \"GENUSD\",\n        \"GNOETH\",\n        \"GNOUSD\",\n        \"GNTBTC\",\n        \"GNTETH\",\n        \"GNTUSD\",\n        \"GOTETH\",\n        \"GOTEUR\",\n        \"GOTUSD\",\n        \"GSDUSD\",\n        \"GTXUSD\",\n        \"GTXUST\",\n        \"HOTBTC\",\n        \"HOTETH\",\n        \"HOTUSD\",\n        \"IMPETH\",\n        \"IMPUSD\",\n        \"INTETH\",\n        \"INTUSD\",\n        \"IOSBTC\",\n        \"IOSETH\",\n        \"IOSUSD\",\n        \"IOTBTC\",\n        \"IOTETH\",\n        \"IOTEUR\",\n        \"IOTGBP\",\n        \"IOTJPY\",\n        \"IOTUSD\",\n        \"IQXBTC\",\n        \"IQXEOS\",\n        \"IQXUSD\",\n        \"KANUSD\",\n        \"KANUST\",\n        \"KNCBTC\",\n        \"KNCETH\",\n        \"KNCUSD\",\n        \"LEOBTC\",\n        \"LEOEOS\",\n        \"LEOETH\",\n        \"LEOUSD\",\n        \"LEOUST\",\n        \"LOOETH\",\n        \"LOOUSD\",\n        \"LRCBTC\",\n        \"LRCETH\",\n        \"LRCUSD\",\n        \"LTCBTC\",\n        \"LTCUSD\",\n        \"LTCUST\",\n        \"LYMBTC\",\n        \"LYMETH\",\n        \"LYMUSD\",\n        \"MANETH\",\n        \"MANUSD\",\n        \"MGOETH\",\n        \"MGOUSD\",\n        \"MITBTC\",\n        \"MITETH\",\n        \"MITUSD\",\n        \"MKRBTC\",\n        \"MKRDAI\",\n        \"MKRETH\",\n        \"MKRUSD\",\n        \"MLNETH\",\n        \"MLNUSD\",\n        \"MNABTC\",\n        \"MNAETH\",\n        \"MNAUSD\",\n        \"MTNBTC\",\n        \"MTNETH\",\n        \"MTNUSD\",\n        \"NCABTC\",\n        \"NCAETH\",\n        \"NCAUSD\",\n        \"NECBTC\",\n        \"NECETH\",\n        \"NECUSD\",\n        \"NEOBTC\",\n        \"NEOETH\",\n        \"NEOEUR\",\n        \"NEOGBP\",\n        \"NEOJPY\",\n        \"NEOUSD\",\n        \"NIOETH\",\n        \"NIOUSD\",\n        \"ODEBTC\",\n        \"ODEETH\",\n        \"ODEUSD\",\n        \"OKBBTC\",\n        \"OKBETH\",\n        \"OKBUSD\",\n        \"OKBUST\",\n        \"OMGBTC\",\n        \"OMGDAI\",\n        \"OMGETH\",\n        \"OMGUSD\",\n        \"OMNBTC\",\n        \"OMNUSD\",\n        \"ONLETH\",\n        \"ONLUSD\",\n        \"ORSBTC\",\n        \"ORSETH\",\n        \"ORSUSD\",\n        \"PAIBTC\",\n        \"PAIUSD\",\n        \"PASETH\",\n        \"PASUSD\",\n        \"PAXUSD\",\n        \"PAXUST\",\n        \"PNKETH\",\n        \"PNKUSD\",\n        \"POABTC\",\n        \"POAETH\",\n        \"POAUSD\",\n        \"POYBTC\",\n        \"POYETH\",\n        \"POYUSD\",\n        \"QSHBTC\",\n        \"QSHETH\",\n        \"QSHUSD\",\n        \"QTMBTC\",\n        \"QTMETH\",\n        \"QTMUSD\",\n        \"RBTBTC\",\n        \"RBTUSD\",\n        \"RCNBTC\",\n        \"RCNETH\",\n        \"RCNUSD\",\n        \"RDNBTC\",\n        \"RDNETH\",\n        \"RDNUSD\",\n        \"REPBTC\",\n        \"REPETH\",\n        \"REPUSD\",\n        \"REQBTC\",\n        \"REQETH\",\n        \"REQUSD\",\n        \"RIFBTC\",\n        \"RIFUSD\",\n        \"RLCBTC\",\n        \"RLCETH\",\n        \"RLCUSD\",\n        \"RRBUSD\",\n        \"RRBUST\",\n        \"RRTBTC\",\n        \"RRTUSD\",\n        \"RTEETH\",\n        \"RTEUSD\",\n        \"SANBTC\",\n        \"SANETH\",\n        \"SANUSD\",\n        \"SCRETH\",\n        \"SCRUSD\",\n        \"SEEBTC\",\n        \"SEEETH\",\n        \"SEEUSD\",\n        \"SENBTC\",\n        \"SENETH\",\n        \"SENUSD\",\n        \"SNGBTC\",\n        \"SNGETH\",\n        \"SNGUSD\",\n        \"SNTBTC\",\n        \"SNTETH\",\n        \"SNTUSD\",\n        \"SPKBTC\",\n        \"SPKETH\",\n        \"SPKUSD\",\n        \"STJBTC\",\n        \"STJETH\",\n        \"STJUSD\",\n        \"SWMETH\",\n        \"SWMUSD\",\n        \"TKNETH\",\n        \"TKNUSD\",\n        \"TNBBTC\",\n        \"TNBETH\",\n        \"TNBUSD\",\n        \"TRIETH\",\n        \"TRIUSD\",\n        \"TRXBTC\",\n        \"TRXETH\",\n        \"TRXEUR\",\n        \"TRXGBP\",\n        \"TRXJPY\",\n        \"TRXUSD\",\n        \"TSDUSD\",\n        \"TSDUST\",\n        \"UDCUSD\",\n        \"UDCUST\",\n        \"UFRETH\",\n        \"UFRUSD\",\n        \"UOSBTC\",\n        \"UOSUSD\",\n        \"USKBTC\",\n        \"USKEOS\",\n        \"USKETH\",\n        \"USKUSD\",\n        \"USKUST\",\n        \"UST:CNHT\",\n        \"USTUSD\",\n        \"UTKBTC\",\n        \"UTKETH\",\n        \"UTKUSD\",\n        \"UTNETH\",\n        \"UTNUSD\",\n        \"VEEBTC\",\n        \"VEEETH\",\n        \"VEEUSD\",\n        \"VETBTC\",\n        \"VETETH\",\n        \"VETUSD\",\n        \"VLDETH\",\n        \"VLDUSD\",\n        \"VSYBTC\",\n        \"VSYUSD\",\n        \"WAXBTC\",\n        \"WAXETH\",\n        \"WAXUSD\",\n        \"WBTETH\",\n        \"WBTUSD\",\n        \"WLOUSD\",\n        \"WLOXLM\",\n        \"WPRBTC\",\n        \"WPRETH\",\n        \"WPRUSD\",\n        \"WTCETH\",\n        \"WTCUSD\",\n        \"XCHETH\",\n        \"XCHUSD\",\n        \"XLMBTC\",\n        \"XLMETH\",\n        \"XLMEUR\",\n        \"XLMGBP\",\n        \"XLMJPY\",\n        \"XLMUSD\",\n        \"XMRBTC\",\n        \"XMRUSD\",\n        \"XRAETH\",\n        \"XRAUSD\",\n        \"XRPBTC\",\n        \"XRPUSD\",\n        \"XTZBTC\",\n        \"XTZUSD\",\n        \"XVGBTC\",\n        \"XVGETH\",\n        \"XVGEUR\",\n        \"XVGGBP\",\n        \"XVGJPY\",\n        \"XVGUSD\",\n        \"YGGETH\",\n        \"YGGUSD\",\n        \"YYWBTC\",\n        \"YYWETH\",\n        \"YYWUSD\",\n        \"ZBTUSD\",\n        \"ZBTUST\",\n        \"ZCNBTC\",\n        \"ZCNETH\",\n        \"ZCNUSD\",\n        \"ZECBTC\",\n        \"ZECUSD\",\n        \"ZILBTC\",\n        \"ZILETH\",\n        \"ZILUSD\",\n        \"ZRXBTC\",\n        \"ZRXDAI\",\n        \"ZRXETH\",\n        \"ZRXUSD\"\n    ]\n]"
                  },
                  "pub:list:currency": {
                    "value": "[\n    [\n        \"ABS\",\n        \"ADD\",\n        \"AGI\",\n        \"AID\",\n        \"AIO\",\n        \"ALG\",\n        \"AMP\",\n        \"ANT\",\n        \"AST\",\n        \"ATD\",\n        \"ATM\",\n        \"ATO\",\n        \"AUC\",\n        \"AVT\",\n        \"BAB\",\n        \"BAT\",\n        \"BBN\",\n        \"BCH\",\n        \"BCI\",\n        \"BFT\",\n        \"BNT\",\n        \"BOX\",\n        \"BSV\",\n        \"BTC\",\n        \"BTCF0\",\n        \"BTG\",\n        \"BTT\",\n        \"CBT\",\n        \"CFI\",\n        \"CLO\",\n        \"CND\",\n        \"CNH\",\n        \"CNHT\",\n        \"CNN\",\n        \"CSX\",\n        \"CTX\",\n        \"DAD\",\n        \"DAI\",\n        \"DAT\",\n        \"DGB\",\n        \"DGX\",\n        \"DRN\",\n        \"DSH\",\n        \"DTA\",\n        \"DTH\",\n        \"DTX\",\n        \"DUSK\",\n        \"EDO\",\n        \"ELF\",\n        \"ENJ\",\n        \"EOS\",\n        \"EOX\",\n        \"ESS\",\n        \"ETC\",\n        \"ETH\",\n        \"ETHF0\",\n        \"ETP\",\n        \"EUR\",\n        \"EUS\",\n        \"EUT\",\n        \"EVT\",\n        \"FOA\",\n        \"FSN\",\n        \"FTT\",\n        \"FUN\",\n        \"GBP\",\n        \"GEN\",\n        \"GNO\",\n        \"GNT\",\n        \"GOT\",\n        \"GSD\",\n        \"GTX\",\n        \"HOT\",\n        \"IMP\",\n        \"INT\",\n        \"IOS\",\n        \"IOT\",\n        \"IQX\",\n        \"JPY\",\n        \"KAN\",\n        \"KNC\",\n        \"LBT\",\n        \"LEO\",\n        \"LES\",\n        \"LET\",\n        \"LOO\",\n        \"LRC\",\n        \"LTC\",\n        \"LYM\",\n        \"MAN\",\n        \"MGO\",\n        \"MIT\",\n        \"MKR\",\n        \"MLN\",\n        \"MNA\",\n        \"MTN\",\n        \"MTO\",\n        \"NCA\",\n        \"NEC\",\n        \"NEO\",\n        \"NIO\",\n        \"ODE\",\n        \"OKB\",\n        \"OMG\",\n        \"OMN\",\n        \"ONL\",\n        \"ORS\",\n        \"PAI\",\n        \"PAS\",\n        \"PAX\",\n        \"PNK\",\n        \"POA\",\n        \"POY\",\n        \"QSH\",\n        \"QTM\",\n        \"RBT\",\n        \"RCN\",\n        \"RDN\",\n        \"REP\",\n        \"REQ\",\n        \"RIF\",\n        \"RLC\",\n        \"RRB\",\n        \"RRT\",\n        \"RTE\",\n        \"SAN\",\n        \"SCR\",\n        \"SEE\",\n        \"SEN\",\n        \"SNG\",\n        \"SNT\",\n        \"SPK\",\n        \"STJ\",\n        \"SWM\",\n        \"TKN\",\n        \"TNB\",\n        \"TRI\",\n        \"TRX\",\n        \"TSD\",\n        \"UDC\",\n        \"UFR\",\n        \"UOS\",\n        \"USD\",\n        \"USK\",\n        \"UST\",\n        \"USTF0\",\n        \"UTK\",\n        \"UTN\",\n        \"VEE\",\n        \"VEN\",\n        \"VET\",\n        \"VLD\",\n        \"VSY\",\n        \"WAX\",\n        \"WBT\",\n        \"WLO\",\n        \"WPR\",\n        \"WTC\",\n        \"XCH\",\n        \"XLM\",\n        \"XMR\",\n        \"XRA\",\n        \"XRP\",\n        \"XTZ\",\n        \"XVG\",\n        \"YGG\",\n        \"YYW\",\n        \"ZBT\",\n        \"ZCN\",\n        \"ZEC\",\n        \"ZIL\",\n        \"ZRX\"\n    ]\n]"
                  },
                  "pub:map:currency:label": {
                    "value": "[\n    [\n        [\n            \"ABS\",\n            \"The Abyss\"\n        ],\n        [\n            \"ADD\",\n            \"ADD\"\n        ],\n        [\n            \"AGI\",\n            \"SingularityNET\"\n        ],\n        [\n            \"AID\",\n            \"AidCoin\"\n        ],\n        [\n            \"AIO\",\n            \"Aion\"\n        ],\n        [\n            \"ALG\",\n            \"Algorand\"\n        ],\n        [\n            \"AMP\",\n            \"Ampleforth\"\n        ],\n        [\n            \"ANT\",\n            \"Aragon\"\n        ],\n        [\n            \"AST\",\n            \"AirSwap\"\n        ],\n        [\n            \"ATD\",\n            \"Atidium\"\n        ],\n        [\n            \"ATM\",\n            \"Atonomi\"\n        ],\n        [\n            \"ATO\",\n            \"Cosmos-Atom\"\n        ],\n        [\n            \"AUC\",\n            \"Auctus\"\n        ],\n        [\n            \"AVT\",\n            \"Aventus\"\n        ],\n        [\n            \"BAB\",\n            \"Bitcoin Cash\"\n        ],\n        [\n            \"BAT\",\n            \"Basic Attention Token\"\n        ],\n        [\n            \"BBN\",\n            \"Banyan Network\"\n        ],\n        [\n            \"BCH\",\n            \"Bitcoin Cash\"\n        ],\n        [\n            \"BCI\",\n            \"BitcoinInterest\"\n        ],\n        [\n            \"BFT\",\n            \"BnkToTheFuture\"\n        ],\n        [\n            \"BNT\",\n            \"Bancor\"\n        ],\n        [\n            \"BOX\",\n            \"ContentBox\"\n        ],\n        [\n            \"BSV\",\n            \"Bitcoin SV\"\n        ],\n        [\n            \"BTC\",\n            \"Bitcoin\"\n        ],\n        [\n            \"BTG\",\n            \"Bitcoin Gold\"\n        ],\n        [\n            \"BTT\",\n            \"BitTorrent\"\n        ],\n        [\n            \"CBT\",\n            \"CommerceBlock\"\n        ],\n        [\n            \"CFI\",\n            \"Cofound.it\"\n        ],\n        [\n            \"CLO\",\n            \"Callisto\"\n        ],\n        [\n            \"CND\",\n            \"Cindicator\"\n        ],\n        [\n            \"CNHT\",\n            \"Tether CNHt\"\n        ],\n        [\n            \"CNN\",\n            \"Content Neutrality Network\"\n        ],\n        [\n            \"CSX\",\n            \"Credits\"\n        ],\n        [\n            \"CTX\",\n            \"Cortex\"\n        ],\n        [\n            \"DAD\",\n            \"DADI\"\n        ],\n        [\n            \"DAI\",\n            \"Dai Stablecoin\"\n        ],\n        [\n            \"DAT\",\n            \"Streamr\"\n        ],\n        [\n            \"DGB\",\n            \"Digibyte\"\n        ],\n        [\n            \"DGX\",\n            \"Digix Gold Token\"\n        ],\n        [\n            \"DRN\",\n            \"Dragonchain\"\n        ],\n        [\n            \"DSH\",\n            \"Dash\"\n        ],\n        [\n            \"DTA\",\n            \"Data\"\n        ],\n        [\n            \"DTH\",\n            \"Dether\"\n        ],\n        [\n            \"DTX\",\n            \"DragonToken\"\n        ],\n        [\n            \"DUSK\",\n            \"Dusk Network\"\n        ],\n        [\n            \"EDO\",\n            \"Eidoo\"\n        ],\n        [\n            \"ELF\",\n            \"aelf\"\n        ],\n        [\n            \"ENJ\",\n            \"Enjin\"\n        ],\n        [\n            \"EOX\",\n            \"eosfinex token\"\n        ],\n        [\n            \"ESS\",\n            \"Essentia\"\n        ],\n        [\n            \"ETC\",\n            \"Ethereum Classic\"\n        ],\n        [\n            \"ETH\",\n            \"Ethereum\"\n        ],\n        [\n            \"ETP\",\n            \"ETP\"\n        ],\n        [\n            \"EUR\",\n            \"Euro\"\n        ],\n        [\n            \"EUS\",\n            \"EURS\"\n        ],\n        [\n            \"EUT\",\n            \"Tether EURt\"\n        ],\n        [\n            \"EVT\",\n            \"Ethfinex Voting Token\"\n        ],\n        [\n            \"FOA\",\n            \"FOAM\"\n        ],\n        [\n            \"FSN\",\n            \"Fusion\"\n        ],\n        [\n            \"FTT\",\n            \"FTX.com\"\n        ],\n        [\n            \"FUN\",\n            \"FunFair\"\n        ],\n        [\n            \"GBP\",\n            \"Pound Sterling\"\n        ],\n        [\n            \"GEN\",\n            \"DAOstack\"\n        ],\n        [\n            \"GNO\",\n            \"Gnosis\"\n        ],\n        [\n            \"GNT\",\n            \"Golem\"\n        ],\n        [\n            \"GOT\",\n            \"ParkinGO\"\n        ],\n        [\n            \"GSD\",\n            \"GUSD\"\n        ],\n        [\n            \"GTX\",\n            \"Gate.IO\"\n        ],\n        [\n            \"HOT\",\n            \"Hydro Protocol\"\n        ],\n        [\n            \"IMP\",\n            \"Ether Kingdoms\"\n        ],\n        [\n            \"INT\",\n            \"Internet Node Token\"\n        ],\n        [\n            \"IOS\",\n            \"IOSToken\"\n        ],\n        [\n            \"IOT\",\n            \"Iota\"\n        ],\n        [\n            \"IQX\",\n            \"Everipedia\"\n        ],\n        [\n            \"JPY\",\n            \"Japanese Yen\"\n        ],\n        [\n            \"KAN\",\n            \"BitKan\"\n        ],\n        [\n            \"KNC\",\n            \"Kyber\"\n        ],\n        [\n            \"LBT\",\n            \"LiquidBTC\"\n        ],\n        [\n            \"LEO\",\n            \"Unus Sed LEO\"\n        ],\n        [\n            \"LES\",\n            \"Unus Sed LEO (EOS)\"\n        ],\n        [\n            \"LET\",\n            \"Unus Sed LEO (ERC20)\"\n        ],\n        [\n            \"LOO\",\n            \"Loom\"\n        ],\n        [\n            \"LRC\",\n            \"Loopring\"\n        ],\n        [\n            \"LTC\",\n            \"Litecoin\"\n        ],\n        [\n            \"LYM\",\n            \"Lympo\"\n        ],\n        [\n            \"MAN\",\n            \"Matrix\"\n        ],\n        [\n            \"MGO\",\n            \"MobileGo\"\n        ],\n        [\n            \"MIT\",\n            \"Mithril\"\n        ],\n        [\n            \"MKR\",\n            \"Maker\"\n        ],\n        [\n            \"MLN\",\n            \"Melon\"\n        ],\n        [\n            \"MNA\",\n            \"Decentraland\"\n        ],\n        [\n            \"MTN\",\n            \"Medicalchain\"\n        ],\n        [\n            \"MTO\",\n            \"MEET.ONE\"\n        ],\n        [\n            \"NCA\",\n            \"Nucleus Vision\"\n        ],\n        [\n            \"NEC\",\n            \"Ethfinex Nectar Token\"\n        ],\n        [\n            \"NEO\",\n            \"NEO\"\n        ],\n        [\n            \"NIO\",\n            \"Autonio\"\n        ],\n        [\n            \"ODE\",\n            \"Odem\"\n        ],\n        [\n            \"OKB\",\n            \"OKB\"\n        ],\n        [\n            \"OMG\",\n            \"OmiseGO\"\n        ],\n        [\n            \"OMN\",\n            \"Omni\"\n        ],\n        [\n            \"ONL\",\n            \"On.Live\"\n        ],\n        [\n            \"ORS\",\n            \"ORS\"\n        ],\n        [\n            \"PAI\",\n            \"PAI Project\"\n        ],\n        [\n            \"PAS\",\n            \"Blockpass\"\n        ],\n        [\n            \"PAX\",\n            \"Paxos\"\n        ],\n        [\n            \"PNK\",\n            \"Kleros\"\n        ],\n        [\n            \"POA\",\n            \"POA Network (erc20)\"\n        ],\n        [\n            \"POY\",\n            \"Polymath\"\n        ],\n        [\n            \"QSH\",\n            \"QASH\"\n        ],\n        [\n            \"QTM\",\n            \"Qtum\"\n        ],\n        [\n            \"RBT\",\n            \"RBTC\"\n        ],\n        [\n            \"RCN\",\n            \"RCN\"\n        ],\n        [\n            \"RDN\",\n            \"Raiden\"\n        ],\n        [\n            \"REP\",\n            \"Augur\"\n        ],\n        [\n            \"REQ\",\n            \"Request Network\"\n        ],\n        [\n            \"RIF\",\n            \"RIF\"\n        ],\n        [\n            \"RLC\",\n            \"iExec\"\n        ],\n        [\n            \"RRB\",\n            \"RenrenBit\"\n        ],\n        [\n            \"RRT\",\n            \"Recovery Right Tokens\"\n        ],\n        [\n            \"RTE\",\n            \"Rate3\"\n        ],\n        [\n            \"SAN\",\n            \"Santiment\"\n        ],\n        [\n            \"SCR\",\n            \"Data Transaction Token\"\n        ],\n        [\n            \"SEE\",\n            \"Seer\"\n        ],\n        [\n            \"SEN\",\n            \"Consensus AI\"\n        ],\n        [\n            \"SNG\",\n            \"SingularDTV\"\n        ],\n        [\n            \"SNT\",\n            \"Status\"\n        ],\n        [\n            \"SPK\",\n            \"SpankChain\"\n        ],\n        [\n            \"STJ\",\n            \"Storj\"\n        ],\n        [\n            \"SWM\",\n            \"Swarm\"\n        ],\n        [\n            \"TKN\",\n            \"TokenCard\"\n        ],\n        [\n            \"TNB\",\n            \"Time New Bank\"\n        ],\n        [\n            \"TRI\",\n            \"Tripio\"\n        ],\n        [\n            \"TRX\",\n            \"TRON\"\n        ],\n        [\n            \"TSD\",\n            \"TrueUSD\"\n        ],\n        [\n            \"UDC\",\n            \"USDc\"\n        ],\n        [\n            \"UFR\",\n            \"Upfiring\"\n        ],\n        [\n            \"UOS\",\n            \"Ultra\"\n        ],\n        [\n            \"USD\",\n            \"US Dollar\"\n        ],\n        [\n            \"USK\",\n            \"USDk\"\n        ],\n        [\n            \"UST\",\n            \"Tether USDt\"\n        ],\n        [\n            \"UTK\",\n            \"UTRUST\"\n        ],\n        [\n            \"UTN\",\n            \"Universa\"\n        ],\n        [\n            \"VEE\",\n            \"BLOCKv\"\n        ],\n        [\n            \"VEN\",\n            \"VeChain\"\n        ],\n        [\n            \"VET\",\n            \"VeChain\"\n        ],\n        [\n            \"VLD\",\n            \"Vetri\"\n        ],\n        [\n            \"VSY\",\n            \"V-SYSTEMS\"\n        ],\n        [\n            \"WAX\",\n            \"WAX\"\n        ],\n        [\n            \"WBT\",\n            \"Wrapped Bitcoin\"\n        ],\n        [\n            \"WLO\",\n            \"WLO\"\n        ],\n        [\n            \"WPR\",\n            \"WePower\"\n        ],\n        [\n            \"WTC\",\n            \"Walton\"\n        ],\n        [\n            \"XCH\",\n            \"CryptoFranc\"\n        ],\n        [\n            \"XLM\",\n            \"Stellar Lumen\"\n        ],\n        [\n            \"XMR\",\n            \"Monero\"\n        ],\n        [\n            \"XRA\",\n            \"Xriba\"\n        ],\n        [\n            \"XRP\",\n            \"Ripple\"\n        ],\n        [\n            \"XTZ\",\n            \"Tezos\"\n        ],\n        [\n            \"XVG\",\n            \"Verge\"\n        ],\n        [\n            \"YGG\",\n            \"Yggdrash\"\n        ],\n        [\n            \"YYW\",\n            \"YOYOW\"\n        ],\n        [\n            \"ZBT\",\n            \"ZB Token\"\n        ],\n        [\n            \"ZCN\",\n            \"0Chain\"\n        ],\n        [\n            \"ZEC\",\n            \"Zcash\"\n        ],\n        [\n            \"ZIL\",\n            \"Zilliqa\"\n        ],\n        [\n            \"ZRX\",\n            \"0x\"\n        ]\n    ]\n]"
                  },
                  "pub:map:currency:unit": {
                    "value": "[\n    [\n        [\n            \"IOT\",\n            \"Mi|MegaIOTA\"\n        ]\n    ]\n]"
                  },
                  "pub:map:currency:undl": {
                    "value": "[\n    [\n        [\n            \"USTF0\",\n            \"UST\"\n        ],\n        [\n            \"BTCF0\",\n            \"BTC\"\n        ],\n        [\n            \"ETHF0\",\n            \"ETH\"\n        ]\n    ]\n]"
                  },
                  "pub:map:currency:pool": {
                    "value": "[\n    [\n        [\n            \"SAN\",\n            \"ETH\"\n        ],\n        [\n            \"OMG\",\n            \"ETH\"\n        ],\n        [\n            \"AVT\",\n            \"ETH\"\n        ],\n        [\n            \"EDO\",\n            \"ETH\"\n        ],\n        [\n            \"DAT\",\n            \"ETH\"\n        ],\n        [\n            \"QSH\",\n            \"ETH\"\n        ],\n        [\n            \"GNT\",\n            \"ETH\"\n        ],\n        [\n            \"SNT\",\n            \"ETH\"\n        ],\n        [\n            \"BAT\",\n            \"ETH\"\n        ],\n        [\n            \"MNA\",\n            \"ETH\"\n        ],\n        [\n            \"FUN\",\n            \"ETH\"\n        ],\n        [\n            \"ZRX\",\n            \"ETH\"\n        ],\n        [\n            \"TNB\",\n            \"ETH\"\n        ],\n        [\n            \"SPK\",\n            \"ETH\"\n        ],\n        [\n            \"RCN\",\n            \"ETH\"\n        ],\n        [\n            \"RLC\",\n            \"ETH\"\n        ],\n        [\n            \"AID\",\n            \"ETH\"\n        ],\n        [\n            \"SNG\",\n            \"ETH\"\n        ],\n        [\n            \"REP\",\n            \"ETH\"\n        ],\n        [\n            \"ELF\",\n            \"ETH\"\n        ],\n        [\n            \"NEC\",\n            \"ETH\"\n        ],\n        [\n            \"IOS\",\n            \"ETH\"\n        ],\n        [\n            \"REQ\",\n            \"ETH\"\n        ],\n        [\n            \"RDN\",\n            \"ETH\"\n        ],\n        [\n            \"LRC\",\n            \"ETH\"\n        ],\n        [\n            \"WAX\",\n            \"ETH\"\n        ],\n        [\n            \"DAI\",\n            \"ETH\"\n        ],\n        [\n            \"CFI\",\n            \"ETH\"\n        ],\n        [\n            \"AGI\",\n            \"ETH\"\n        ],\n        [\n            \"BFT\",\n            \"ETH\"\n        ],\n        [\n            \"MTN\",\n            \"ETH\"\n        ],\n        [\n            \"ODE\",\n            \"ETH\"\n        ],\n        [\n            \"ANT\",\n            \"ETH\"\n        ],\n        [\n            \"DTH\",\n            \"ETH\"\n        ],\n        [\n            \"MIT\",\n            \"ETH\"\n        ],\n        [\n            \"STJ\",\n            \"ETH\"\n        ],\n        [\n            \"MKR\",\n            \"ETH\"\n        ],\n        [\n            \"VEN\",\n            \"ETH\"\n        ],\n        [\n            \"KNC\",\n            \"ETH\"\n        ],\n        [\n            \"POA\",\n            \"ETH\"\n        ],\n        [\n            \"EVT\",\n            \"ETH\"\n        ],\n        [\n            \"LYM\",\n            \"ETH\"\n        ],\n        [\n            \"UTK\",\n            \"ETH\"\n        ],\n        [\n            \"VEE\",\n            \"ETH\"\n        ],\n        [\n            \"DAD\",\n            \"ETH\"\n        ],\n        [\n            \"ORS\",\n            \"ETH\"\n        ],\n        [\n            \"AUC\",\n            \"ETH\"\n        ],\n        [\n            \"POY\",\n            \"ETH\"\n        ],\n        [\n            \"FSN\",\n            \"ETH\"\n        ],\n        [\n            \"CBT\",\n            \"ETH\"\n        ],\n        [\n            \"ZCN\",\n            \"ETH\"\n        ],\n        [\n            \"SEN\",\n            \"ETH\"\n        ],\n        [\n            \"NCA\",\n            \"ETH\"\n        ],\n        [\n            \"CND\",\n            \"ETH\"\n        ],\n        [\n            \"CTX\",\n            \"ETH\"\n        ],\n        [\n            \"SEE\",\n            \"ETH\"\n        ],\n        [\n            \"ESS\",\n            \"ETH\"\n        ],\n        [\n            \"ATD\",\n            \"EOS\"\n        ],\n        [\n            \"ADD\",\n            \"EOS\"\n        ],\n        [\n            \"MTO\",\n            \"EOS\"\n        ],\n        [\n            \"ATM\",\n            \"ETH\"\n        ],\n        [\n            \"HOT\",\n            \"ETH\"\n        ],\n        [\n            \"DTA\",\n            \"ETH\"\n        ],\n        [\n            \"IQX\",\n            \"EOS\"\n        ],\n        [\n            \"WPR\",\n            \"ETH\"\n        ],\n        [\n            \"ZIL\",\n            \"ETH\"\n        ],\n        [\n            \"BNT\",\n            \"ETH\"\n        ],\n        [\n            \"ABS\",\n            \"ETH\"\n        ],\n        [\n            \"XRA\",\n            \"ETH\"\n        ],\n        [\n            \"MAN\",\n            \"ETH\"\n        ],\n        [\n            \"BBN\",\n            \"ETH\"\n        ],\n        [\n            \"NIO\",\n            \"ETH\"\n        ],\n        [\n            \"DGX\",\n            \"ETH\"\n        ],\n        [\n            \"UTN\",\n            \"ETH\"\n        ],\n        [\n            \"TKN\",\n            \"ETH\"\n        ],\n        [\n            \"GOT\",\n            \"ETH\"\n        ],\n        [\n            \"CNN\",\n            \"ETH\"\n        ],\n        [\n            \"BOX\",\n            \"ETH\"\n        ],\n        [\n            \"MGO\",\n            \"ETH\"\n        ],\n        [\n            \"RTE\",\n            \"ETH\"\n        ],\n        [\n            \"YGG\",\n            \"ETH\"\n        ],\n        [\n            \"MLN\",\n            \"ETH\"\n        ],\n        [\n            \"WTC\",\n            \"ETH\"\n        ],\n        [\n            \"CSX\",\n            \"ETH\"\n        ],\n        [\n            \"DRN\",\n            \"ETH\"\n        ],\n        [\n            \"PNK\",\n            \"ETH\"\n        ],\n        [\n            \"BAB\",\n            \"BCH\"\n        ],\n        [\n            \"WLO\",\n            \"XLM\"\n        ],\n        [\n            \"VLD\",\n            \"ETH\"\n        ],\n        [\n            \"ENJ\",\n            \"ETH\"\n        ],\n        [\n            \"ONL\",\n            \"ETH\"\n        ],\n        [\n            \"GSD\",\n            \"ETH\"\n        ],\n        [\n            \"UDC\",\n            \"ETH\"\n        ],\n        [\n            \"TSD\",\n            \"ETH\"\n        ],\n        [\n            \"PAX\",\n            \"ETH\"\n        ],\n        [\n            \"RIF\",\n            \"RBT\"\n        ],\n        [\n            \"PAS\",\n            \"ETH\"\n        ],\n        [\n            \"BTT\",\n            \"TRX\"\n        ],\n        [\n            \"IMP\",\n            \"ETH\"\n        ],\n        [\n            \"SCR\",\n            \"ETH\"\n        ],\n        [\n            \"GNO\",\n            \"ETH\"\n        ],\n        [\n            \"GEN\",\n            \"ETH\"\n        ],\n        [\n            \"WBT\",\n            \"ETH\"\n        ],\n        [\n            \"XCH\",\n            \"ETH\"\n        ],\n        [\n            \"EUS\",\n            \"ETH\"\n        ],\n        [\n            \"LES\",\n            \"EOS\"\n        ],\n        [\n            \"LET\",\n            \"ETH\"\n        ],\n        [\n            \"AST\",\n            \"ETH\"\n        ],\n        [\n            \"FOA\",\n            \"ETH\"\n        ],\n        [\n            \"UFR\",\n            \"ETH\"\n        ],\n        [\n            \"ZBT\",\n            \"ETH\"\n        ],\n        [\n            \"OKB\",\n            \"ETH\"\n        ],\n        [\n            \"USK\",\n            \"ETH\"\n        ],\n        [\n            \"GTX\",\n            \"ETH\"\n        ],\n        [\n            \"KAN\",\n            \"ETH\"\n        ],\n        [\n            \"AMP\",\n            \"ETH\"\n        ],\n        [\n            \"SWM\",\n            \"ETH\"\n        ],\n        [\n            \"TRI\",\n            \"ETH\"\n        ],\n        [\n            \"LOO\",\n            \"ETH\"\n        ],\n        [\n            \"DUSK\",\n            \"ETH\"\n        ],\n        [\n            \"UOS\",\n            \"ETH\"\n        ],\n        [\n            \"RRB\",\n            \"ETH\"\n        ],\n        [\n            \"EOX\",\n            \"EOS\"\n        ],\n        [\n            \"DTX\",\n            \"ETH\"\n        ],\n        [\n            \"FTT\",\n            \"ETH\"\n        ]\n    ]\n]"
                  },
                  "pub:map:currency:explorer": {
                    "value": "[\n    [\n        [\n            \"AIO\",\n            [\n                \"https://mainnet.aion.network\",\n                \"https://mainnet.aion.network/#/account/VAL\",\n                \"https://mainnet.aion.network/#/transaction/VAL\"\n            ]\n        ],\n        [\n            \"ALG\",\n            [\n                \"https://algoexplorer.io\",\n                \"https://algoexplorer.io/address/VAL\",\n                \"https://algoexplorer.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"ATO\",\n            [\n                \"https://hubble.figment.network/cosmos/chains/cosmoshub-2\",\n                \"https://hubble.figment.network/cosmos/chains/cosmoshub-2/accounts/VAL\",\n                \"https://hubble.figment.network/cosmos/chains/cosmoshub-2/transactions/VAL\"\n            ]\n        ],\n        [\n            \"BCI\",\n            [\n                \"https://explorer.bitcoininterest.io\",\n                \"https://explorer.bitcoininterest.io/address/VAL\",\n                \"https://explorer.bitcoininterest.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"BSV\",\n            [\n                \"https://whatsonchain.com\",\n                \"https://whatsonchain.com/address/VAL\",\n                \"https://whatsonchain.com/tx/VAL\"\n            ]\n        ],\n        [\n            \"BTC\",\n            [\n                \"https://blockstream.info\",\n                \"https://blockstream.info/address/VAL\",\n                \"https://blockstream.info/tx/VAL\"\n            ]\n        ],\n        [\n            \"BTG\",\n            [\n                \"https://explorer.bitcoingold.org/insight\",\n                \"https://explorer.bitcoingold.org/insight/address/VAL\",\n                \"https://explorer.bitcoingold.org/insight/tx/VAL\"\n            ]\n        ],\n        [\n            \"CLO\",\n            [\n                \"https://explorer2.callisto.network\",\n                \"https://explorer2.callisto.network/addr/VAL\",\n                \"https://explorer2.callisto.network/tx/VAL\"\n            ]\n        ],\n        [\n            \"DGB\",\n            [\n                \"https://digiexplorer.info\",\n                \"https://digiexplorer.info/address/VAL\",\n                \"https://digiexplorer.info/tx/VAL\"\n            ]\n        ],\n        [\n            \"DSH\",\n            [\n                \"https://explorer.dash.org\",\n                \"https://explorer.dash.org/address/VAL\",\n                \"https://explorer.dash.org/tx/VAL\"\n            ]\n        ],\n        [\n            \"EOS\",\n            [\n                \"https://bloks.io\",\n                \"https://bloks.io/account/VAL\",\n                \"https://bloks.io/transaction/VAL\"\n            ]\n        ],\n        [\n            \"ETC\",\n            [\n                \"http://gastracker.io\",\n                \"http://gastracker.io/addr/VAL\",\n                \"http://gastracker.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"ETH\",\n            [\n                \"https://etherscan.io\",\n                \"https://etherscan.io/address/VAL\",\n                \"https://etherscan.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"ETP\",\n            [\n                \"http://explorer.mvs.live/#!\",\n                \"http://explorer.mvs.live/#!/adr/VAL\",\n                \"http://explorer.mvs.live/#!/tx/VAL\"\n            ]\n        ],\n        [\n            \"INT\",\n            [\n                \"https://explorer.intchain.io/#\",\n                \"https://explorer.intchain.io/#/blockchain/accountdetail/1?address=VAL\",\n                \"https://explorer.intchain.io/#/blockchain/txdetail?hash=VAL\"\n            ]\n        ],\n        [\n            \"IOT\",\n            [\n                \"https://thetangle.org\",\n                \"https://thetangle.org/address/VAL\",\n                \"https://thetangle.org/transaction/VAL\"\n            ]\n        ],\n        [\n            \"LBT\",\n            [\n                \"https://blockstream.info/liquid\",\n                \"https://blockstream.info/liquid/address/VAL\",\n                \"https://blockstream.info/liquid/tx/VAL\"\n            ]\n        ],\n        [\n            \"LEO\",\n            [\n                \"https://live.blockcypher.com/leo\",\n                \"https://live.blockcypher.com/leo/address/VAL\",\n                \"https://live.blockcypher.com/leo/tx/VAL\"\n            ]\n        ],\n        [\n            \"LTC\",\n            [\n                \"https://live.blockcypher.com/ltc\",\n                \"https://live.blockcypher.com/ltc/address/VAL\",\n                \"https://live.blockcypher.com/ltc/tx/VAL\"\n            ]\n        ],\n        [\n            \"NEO\",\n            [\n                \"https://neotracker.io\",\n                \"https://neotracker.io/address/VAL\",\n                \"https://neotracker.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"OMN\",\n            [\n                \"http://omniexplorer.info\",\n                \"http://omniexplorer.info/lookupadd.aspx?address=VAL\",\n                \"http://omniexplorer.info/lookuptx.aspx?txid=VAL\"\n            ]\n        ],\n        [\n            \"PAI\",\n            [\n                \"https://paichain.info\",\n                \"https://paichain.info/address/VAL\",\n                \"https://paichain.info/tx/VAL\"\n            ]\n        ],\n        [\n            \"QTM\",\n            [\n                \"https://explorer.qtum.org\",\n                \"https://explorer.qtum.org/address/VAL\",\n                \"https://explorer.qtum.org/tx/VAL\"\n            ]\n        ],\n        [\n            \"RBT\",\n            [\n                \"https://explorer.rsk.co\",\n                \"https://explorer.rsk.co/address/VAL\",\n                \"https://explorer.rsk.co/tx/VAL\"\n            ]\n        ],\n        [\n            \"TRX\",\n            [\n                \"https://tronscan.org/#\",\n                \"https://tronscan.org/#/address/VAL\",\n                \"https://tronscan.org/#/transaction/VAL\"\n            ]\n        ],\n        [\n            \"VET\",\n            [\n                \"https://explore.veforge.com\",\n                \"https://explore.veforge.com/accounts/VAL\",\n                \"https://explore.veforge.com/transactions/VAL\"\n            ]\n        ],\n        [\n            \"VSY\",\n            [\n                \"https://explorer.v.systems\",\n                \"https://explorer.v.systems/address/VAL\",\n                \"https://explorer.v.systems/transactions/VAL\"\n            ]\n        ],\n        [\n            \"XLM\",\n            [\n                \"https://stellarchain.io\",\n                \"https://stellarchain.io/address/VAL\",\n                \"https://stellarchain.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"XMR\",\n            [\n                \"https://moneroblocks.info\",\n                \"https://moneroblocks.info/search/VAL\",\n                \"https://moneroblocks.info/search/VAL\"\n            ]\n        ],\n        [\n            \"XRP\",\n            [\n                \"https://xrpscan.com\",\n                \"https://xrpscan.com/account/VAL\",\n                \"https://xrpscan.com/tx/VAL\"\n            ]\n        ],\n        [\n            \"XTZ\",\n            [\n                \"https://tzscan.io\",\n                \"https://tzscan.io/VAL\",\n                \"https://tzscan.io/VAL\"\n            ]\n        ],\n        [\n            \"XVG\",\n            [\n                \"https://verge-blockchain.info\",\n                \"https://verge-blockchain.info/address/VAL\",\n                \"https://verge-blockchain.info/tx/VAL\"\n            ]\n        ],\n        [\n            \"YYW\",\n            [\n                \"https://live.blockcypher.com/yyw\",\n                \"https://live.blockcypher.com/yyw/address/VAL\",\n                \"https://live.blockcypher.com/yyw/tx/VAL\"\n            ]\n        ],\n        [\n            \"ZEC\",\n            [\n                \"https://zcashnetwork.info\",\n                \"https://zcashnetwork.info/address/VAL\",\n                \"https://zcashnetwork.info/tx/VAL\"\n            ]\n        ]\n    ]\n]"
                  },
                  "pub:list:pair:margin": {
                    "value": "[\n    [\n        \"BABBTC\",\n        \"BABUSD\",\n        \"BSVBTC\",\n        \"BSVUSD\",\n        \"BTCEUR\",\n        \"BTCGBP\",\n        \"BTCJPY\",\n        \"BTCUSD\",\n        \"BTCUST\",\n        \"BTGBTC\",\n        \"BTGUSD\",\n        \"DSHBTC\",\n        \"DSHUSD\",\n        \"EDOBTC\",\n        \"EDOETH\",\n        \"EDOUSD\",\n        \"EOSBTC\",\n        \"EOSETH\",\n        \"EOSEUR\",\n        \"EOSGBP\",\n        \"EOSJPY\",\n        \"EOSUSD\",\n        \"ETCBTC\",\n        \"ETCUSD\",\n        \"ETHBTC\",\n        \"ETHEUR\",\n        \"ETHGBP\",\n        \"ETHJPY\",\n        \"ETHUSD\",\n        \"ETHUST\",\n        \"ETPBTC\",\n        \"ETPETH\",\n        \"ETPUSD\",\n        \"IOTBTC\",\n        \"IOTETH\",\n        \"IOTEUR\",\n        \"IOTGBP\",\n        \"IOTJPY\",\n        \"IOTUSD\",\n        \"LEOUSD\",\n        \"LEOUST\",\n        \"LTCBTC\",\n        \"LTCUSD\",\n        \"NEOBTC\",\n        \"NEOETH\",\n        \"NEOEUR\",\n        \"NEOGBP\",\n        \"NEOJPY\",\n        \"NEOUSD\",\n        \"OMGBTC\",\n        \"OMGETH\",\n        \"OMGUSD\",\n        \"SANBTC\",\n        \"SANETH\",\n        \"SANUSD\",\n        \"USTUSD\",\n        \"XLMBTC\",\n        \"XLMUSD\",\n        \"XMRBTC\",\n        \"XMRUSD\",\n        \"XRPBTC\",\n        \"XRPUSD\",\n        \"XTZBTC\",\n        \"XTZUSD\",\n        \"ZECBTC\",\n        \"ZECUSD\",\n        \"ZRXETH\",\n        \"ZRXUSD\"\n    ]\n]"
                  },
                  "pub:info:pair": {
                    "value": "[\n  [\n    [\n      \"1INCH:USD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"1INCH:UST\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AAVE:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AAVE:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ADABTC\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ADAUSD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ADAUST\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ALGBTC\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"150000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ALGUSD\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"150000.0\",\n        null,\n        null,\n        null,\n        0.5,\n        0.25,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ALGUST\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"150000.0\",\n        null,\n        null,\n        null,\n        0.5,\n        0.25,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ALT2612:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"360000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ALT2612:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"360000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AMPBTC\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"25000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AMPUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"25000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AMPUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"25000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"APENFT:USD\",\n      [\n        null,\n        null,\n        null,\n        \"3669724.0\",\n        \"40000000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"APENFT:UST\",\n      [\n        null,\n        null,\n        null,\n        \"3669724.0\",\n        \"40000000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"APEUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.8\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.6,\n        0.3,\n        null,\n        null\n      ]\n    ],\n    [\n      \"APEUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.8\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.6,\n        0.3,\n        null,\n        null\n      ]\n    ],\n    [\n      \"APPUSD\",\n      [\n        null,\n        null,\n        null,\n        \"68.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"APPUST\",\n      [\n        null,\n        null,\n        null,\n        \"68.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"APTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"30000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"APTUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"30000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ARBUSD\",\n      [\n        null,\n        null,\n        null,\n        \"1.0\",\n        \"75000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ARBUST\",\n      [\n        null,\n        null,\n        null,\n        \"1.0\",\n        \"75000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ATOBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ATOUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.5,\n        0.25,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ATOUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AVAX:BTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.08\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AVAX:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.08\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AVAX:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.08\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AXSUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AXSUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AZERO:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"45000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"AZERO:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"45000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"B2MUSD\",\n      [\n        null,\n        null,\n        null,\n        \"210.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"B2MUST\",\n      [\n        null,\n        null,\n        null,\n        \"210.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BALUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.4\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BALUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.4\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BAND:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BAND:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BATUSD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"200000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BCHN:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.006\",\n        \"1000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BEST:USD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BGBUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BGBUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BLUR:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"75000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BLUR:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"75000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BMNBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.000006\",\n        \"1.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BMNUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.000006\",\n        \"1.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BOBA:USD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BONK:USD\",\n      [\n        null,\n        null,\n        null,\n        \"79634.0\",\n        \"2000000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BONK:UST\",\n      [\n        null,\n        null,\n        null,\n        \"79634.0\",\n        \"2000000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BORG:BTC\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BORG:USD\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BORG:UST\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BOSON:USD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BOSON:UST\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTC:CNHT\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTC:MXNT\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"500.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTC:XAUT\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"250.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTCEUR\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTCEUT\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTCGBP\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTCJPY\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTCMIM\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"2500.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTCTRY\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTCUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.1,\n        0.05,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTCUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.1,\n        0.05,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BTTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"1970444.0\",\n        \"25000000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BXNUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"2200000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"BXNUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"2200000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CCDUSD\",\n      [\n        null,\n        null,\n        null,\n        \"336.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CCDUST\",\n      [\n        null,\n        null,\n        null,\n        \"336.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CELO:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"65000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CELO:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"65000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CHEX:USD\",\n      [\n        null,\n        null,\n        null,\n        \"30.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CHZUSD\",\n      [\n        null,\n        null,\n        null,\n        \"16.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CHZUST\",\n      [\n        null,\n        null,\n        null,\n        \"16.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CNH:CNHT\",\n      [\n        null,\n        null,\n        null,\n        \"14.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"COMP:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"COMP:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"COQUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"15000000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"COQUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"15000000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CRVUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"CRVUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DAIUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"200000.0\",\n        null,\n        null,\n        null,\n        0.66,\n        0.33,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DOGE:BTC\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DOGE:USD\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DOGE:UST\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DORA:USD\",\n      [\n        null,\n        null,\n        null,\n        \"14.0\",\n        \"25000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DOTBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DOTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DOTUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DSHBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.06\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DSHUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.06\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DUSK:USD\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DVFUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DYMUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.4\",\n        \"11000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"DYMUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.4\",\n        \"11000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EGLD:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EGLD:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ENAUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"300000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ENAUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"300000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EOSBTC\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EOSETH\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EOSUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EOSUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETCBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.1\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETCUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.1\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETCUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.1\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETH2X:ETH\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETH2X:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETH2X:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETH:MXNT\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETH:XAUT\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"2500.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETHBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETHEUR\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETHEUT\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETHGBP\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETHJPY\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETHUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETHUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETHW:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.6,\n        0.3,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ETHW:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.6,\n        0.3,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EURUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EUT:MXNT\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EUTEUR\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EUTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"EUTUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FCLUSD\",\n      [\n        null,\n        null,\n        null,\n        \"134.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FCLUST\",\n      [\n        null,\n        null,\n        null,\n        \"134.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FETUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FETUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FILUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FILUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FLOKI:USD\",\n      [\n        null,\n        null,\n        null,\n        \"14046.0\",\n        \"2500000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FLOKI:UST\",\n      [\n        null,\n        null,\n        null,\n        \"14046.0\",\n        \"2500000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FLRUSD\",\n      [\n        null,\n        null,\n        null,\n        \"46.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FLRUST\",\n      [\n        null,\n        null,\n        null,\n        \"46.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FORTH:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FORTH:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FTMUSD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FTMUST\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"FUNUSD\",\n      [\n        null,\n        null,\n        null,\n        \"330.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GALA:USD\",\n      [\n        null,\n        null,\n        null,\n        \"44.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GALA:UST\",\n      [\n        null,\n        null,\n        null,\n        \"44.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GBPEUT\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GBPUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GMMT:USD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GMMT:UST\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GNOUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.008\",\n        \"1000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GOCUSD\",\n      [\n        null,\n        null,\n        null,\n        \"208.0\",\n        \"1600000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GOCUST\",\n      [\n        null,\n        null,\n        null,\n        \"208.0\",\n        \"1600000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GOMINING:USD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"360000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GOMINING:UST\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"360000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GRTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"10.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GRTUST\",\n      [\n        null,\n        null,\n        null,\n        \"10.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GTXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"GTXUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"HILSV:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"100.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"HIXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"3618.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"HIXUST\",\n      [\n        null,\n        null,\n        null,\n        \"3618.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"HMTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"54.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"HMTUST\",\n      [\n        null,\n        null,\n        null,\n        \"54.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"HTXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"HTXUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ICPUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ICPUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"IDXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"24.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"INJUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"1350.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"INJUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"1350.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"IOTBTC\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"IOTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"JASMY:USD\",\n      [\n        null,\n        null,\n        null,\n        \"144.0\",\n        \"2500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"JASMY:UST\",\n      [\n        null,\n        null,\n        null,\n        \"144.0\",\n        \"2500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"JPYUST\",\n      [\n        null,\n        null,\n        null,\n        \"300.0\",\n        \"100000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"JSTBTC\",\n      [\n        null,\n        null,\n        null,\n        \"52.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"JSTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"52.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"JSTUST\",\n      [\n        null,\n        null,\n        null,\n        \"52.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"JUPUSD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"350000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"JUPUST\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"350000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"KANUSD\",\n      [\n        null,\n        null,\n        null,\n        \"1556.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"KANUST\",\n      [\n        null,\n        null,\n        null,\n        \"1556.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"KARATE:USD\",\n      [\n        null,\n        null,\n        null,\n        \"482.0\",\n        \"70000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"KARATE:UST\",\n      [\n        null,\n        null,\n        null,\n        \"482.0\",\n        \"70000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"KAVA:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"KAVA:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"KNCUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"KSMUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"KSMUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LDOUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LDOUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LEOBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LEOETH\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LEOUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LEOUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LIFIII:USD\",\n      [\n        null,\n        null,\n        null,\n        \"74.0\",\n        \"800000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LIFIII:UST\",\n      [\n        null,\n        null,\n        null,\n        \"74.0\",\n        \"800000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LINK:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LINK:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LRCUSD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LTCBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LTCUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LTCUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LUNA2:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LUNA2:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LYMUSD\",\n      [\n        null,\n        null,\n        null,\n        \"740.0\",\n        \"10000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"LYMUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MATIC:BTC\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MATIC:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MATIC:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MEME:USD\",\n      [\n        null,\n        null,\n        null,\n        \"42.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MEME:UST\",\n      [\n        null,\n        null,\n        null,\n        \"42.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MIMUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MIMUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MKRUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"2500.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MKRUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"2500.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MLNUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.1\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MNABTC\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"200000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MNAUSD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"200000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MODE:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"650000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MODE:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"650000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MPCUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"125000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MPCUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"125000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"MXNT:USD\",\n      [\n        null,\n        null,\n        null,\n        \"34.0\",\n        \"10000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NEAR:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.4\",\n        \"25000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NEAR:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.4\",\n        \"25000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NEOBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NEOUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NEOUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NEXO:BTC\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NEXO:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NEXO:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NOMUSD\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"20000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NOMUST\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"20000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NOTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NOTUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"NXRA:USD\",\n      [\n        null,\n        null,\n        null,\n        \"14.0\",\n        \"200000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OCEAN:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OCEAN:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OGNUSD\",\n      [\n        null,\n        null,\n        null,\n        \"10.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OGNUST\",\n      [\n        null,\n        null,\n        null,\n        \"10.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OMGBTC\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OMGETH\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OMGUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OMNUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.8\",\n        \"20000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OPXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"OPXUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"PAXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"PAXUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"PEPE:USD\",\n      [\n        null,\n        null,\n        null,\n        \"392156.0\",\n        \"50000000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"PEPE:UST\",\n      [\n        null,\n        null,\n        null,\n        \"392156.0\",\n        \"50000000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"PLUUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.4\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"PNKUSD\",\n      [\n        null,\n        null,\n        null,\n        \"52.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"PORTAL:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"55000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"PORTAL:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"55000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"QRDO:USD\",\n      [\n        null,\n        null,\n        null,\n        \"34.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"QRDO:UST\",\n      [\n        null,\n        null,\n        null,\n        \"34.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"QTFBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"QTFUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"QTMUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"REQUSD\",\n      [\n        null,\n        null,\n        null,\n        \"16.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"RLYUSD\",\n      [\n        null,\n        null,\n        null,\n        \"192.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"RLYUST\",\n      [\n        null,\n        null,\n        null,\n        \"192.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"RRTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SAND:USD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SAND:UST\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SEIUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SEIUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SENATE:USD\",\n      [\n        null,\n        null,\n        null,\n        \"20.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SGBUSD\",\n      [\n        null,\n        null,\n        null,\n        \"124.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SGBUST\",\n      [\n        null,\n        null,\n        null,\n        \"124.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SHIB:USD\",\n      [\n        null,\n        null,\n        null,\n        \"141010.0\",\n        \"5000000000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SHIB:UST\",\n      [\n        null,\n        null,\n        null,\n        \"141010.0\",\n        \"5000000000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SIDUS:USD\",\n      [\n        null,\n        null,\n        null,\n        \"452.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SMRUSD\",\n      [\n        null,\n        null,\n        null,\n        \"102.0\",\n        \"700000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SMRUST\",\n      [\n        null,\n        null,\n        null,\n        \"102.0\",\n        \"700000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SNXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SNXUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SOLBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SOLUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SOLUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SPEC:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"22000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SPEC:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"22000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SPELL:USD\",\n      [\n        null,\n        null,\n        null,\n        \"1640.0\",\n        \"2500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SPELL:UST\",\n      [\n        null,\n        null,\n        null,\n        \"1640.0\",\n        \"2500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"STGUSD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"STGUST\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"STRK:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"30000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"STRK:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"30000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SUIUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SUIUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SUKU:USD\",\n      [\n        null,\n        null,\n        null,\n        \"20.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SUKU:UST\",\n      [\n        null,\n        null,\n        null,\n        \"20.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SUNUSD\",\n      [\n        null,\n        null,\n        null,\n        \"216.0\",\n        \"10000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SUNUST\",\n      [\n        null,\n        null,\n        null,\n        \"216.0\",\n        \"10000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SUSHI:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SUSHI:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SWEAT:USD\",\n      [\n        null,\n        null,\n        null,\n        \"168.0\",\n        \"7000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"SWEAT:UST\",\n      [\n        null,\n        null,\n        null,\n        \"168.0\",\n        \"7000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TAIKO:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"23000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TAIKO:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"23000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTADA:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTALGO:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTAPT:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTAVAX:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTBTC:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"100.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTBTC:TESTUSDT\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"100.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTDOGE:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTDOT:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTEOS:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTETH:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTFIL:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTLTC:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTMATIC:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTMATIC:TESTUSDT\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTNEAR:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTSOL:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTXAUT:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TESTXTZ:TESTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"THETA:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"THETA:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TIAUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TIAUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TLOS:USD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TOKEN:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"650000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TOKEN:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"650000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TOMI:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"16500.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TOMI:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"16500.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TONUSD\",\n      [\n        null,\n        null,\n        null,\n        \"1.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TONUST\",\n      [\n        null,\n        null,\n        null,\n        \"1.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TRADE:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"2500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TRADE:UST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"2500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TRXBTC\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TRXETH\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TRXEUR\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TRXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TRXUST\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TRYUST\",\n      [\n        null,\n        null,\n        null,\n        \"62.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TSDUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"TSDUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"UDCUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"UDCUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"UNIUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"UNIUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"UOSBTC\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"400000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"UOSUSD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"400000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"UST:CNHT\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"UST:MXNT\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"USTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        0.1,\n        0.05,\n        null,\n        null\n      ]\n    ],\n    [\n      \"VELAR:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"VELAR:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"VETBTC\",\n      [\n        null,\n        null,\n        null,\n        \"62.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"VETUSD\",\n      [\n        null,\n        null,\n        null,\n        \"62.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"VETUST\",\n      [\n        null,\n        null,\n        null,\n        \"62.0\",\n        \"5000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"VRAUSD\",\n      [\n        null,\n        null,\n        null,\n        \"232.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"VRAUST\",\n      [\n        null,\n        null,\n        null,\n        \"232.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WAVES:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WAVES:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WBTBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WBTUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WHBT:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"12500.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WHBT:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"12500.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WIFUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WIFUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WILD:USD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WILD:UST\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WMINIMA:USD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"150000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WMINIMA:UST\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"150000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WNCG:USD\",\n      [\n        null,\n        null,\n        null,\n        \"20.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WOOUSD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"2500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WOOUST\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"2500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WXXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"35000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"WXXUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.001\",\n        \"35000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XAUT:BTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"400.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XAUT:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"400.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XAUT:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"400.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XCAD:USD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"15000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XDCUSD\",\n      [\n        null,\n        null,\n        null,\n        \"54.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XDCUST\",\n      [\n        null,\n        null,\n        null,\n        \"54.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XLMBTC\",\n      [\n        null,\n        null,\n        null,\n        \"14.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        0.5,\n        0.25,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XLMUSD\",\n      [\n        null,\n        null,\n        null,\n        \"14.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        0.5,\n        0.25,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XLMUST\",\n      [\n        null,\n        null,\n        null,\n        \"14.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XMRBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XMRUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XMRUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XRDBTC\",\n      [\n        null,\n        null,\n        null,\n        \"44.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XRDUSD\",\n      [\n        null,\n        null,\n        null,\n        \"44.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XRPBTC\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"2000000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XRPUSD\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"2000000.0\",\n        null,\n        null,\n        null,\n        0.2,\n        0.1,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XRPUST\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"2000000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XTPUSD\",\n      [\n        null,\n        null,\n        null,\n        \"1026.0\",\n        \"10000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XTPUST\",\n      [\n        null,\n        null,\n        null,\n        \"1026.0\",\n        \"10000000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XTZBTC\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XTZUSD\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XTZUST\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"XVGUSD\",\n      [\n        null,\n        null,\n        null,\n        \"432.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"YFIUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.0002\",\n        \"100.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"YFIUST\",\n      [\n        null,\n        null,\n        null,\n        \"0.0002\",\n        \"100.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ZECBTC\",\n      [\n        null,\n        null,\n        null,\n        \"0.06\",\n        \"20000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ZECUSD\",\n      [\n        null,\n        null,\n        null,\n        \"0.06\",\n        \"20000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ZETA:USD\",\n      [\n        null,\n        null,\n        null,\n        \"0.8\",\n        \"350000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ZETA:UST\",\n      [\n        null,\n        null,\n        null,\n        \"0.8\",\n        \"350000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ZILUSD\",\n      [\n        null,\n        null,\n        null,\n        \"66.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        null,\n        null,\n        null,\n        null\n      ]\n    ],\n    [\n      \"ZRXUSD\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"200000.0\",\n        null,\n        null,\n        null,\n        0.3,\n        0.15,\n        null,\n        null\n      ]\n    ]\n  ]\n]"
                  },
                  "pub:map:currency:pool,pub:map:currency:explorer,pub:map:currency:sym": {
                    "value": "[\n    [\n        [\n            \"1INCH\",\n            \"ETH\"\n        ],\n        [\n            \"AAVE\",\n            \"ETH\"\n        ],\n        [\n            \"ADD\",\n            \"EOS\"\n        ],\n        [\n            \"ALBT\",\n            \"ETH\"\n        ],\n        [\n            \"AMP\",\n            \"ETH\"\n        ],\n        [\n            \"ANT\",\n            \"ETH\"\n        ],\n        [\n            \"ATD\",\n            \"EOS\"\n        ],\n        [\n            \"B21X\",\n            \"ETH\"\n        ],\n        [\n            \"BAL\",\n            \"ETH\"\n        ],\n        [\n            \"BAND\",\n            \"ETH\"\n        ],\n        [\n            \"BAT\",\n            \"ETH\"\n        ],\n        [\n            \"BEST\",\n            \"ETH\"\n        ],\n        [\n            \"BFT\",\n            \"ETH\"\n        ],\n        [\n            \"BMI\",\n            \"ETH\"\n        ],\n        [\n            \"BNT\",\n            \"ETH\"\n        ],\n        [\n            \"BOSON\",\n            \"ETH\"\n        ],\n        [\n            \"BTSE\",\n            \"LBT\"\n        ],\n        [\n            \"BTT\",\n            \"TRX\"\n        ],\n        [\n            \"CEL\",\n            \"ETH\"\n        ],\n        [\n            \"CHEX\",\n            \"EOS\"\n        ],\n        [\n            \"CHZ\",\n            \"ETH\"\n        ],\n        [\n            \"CNHTE\",\n            \"ETH\"\n        ],\n        [\n            \"COMP\",\n            \"ETH\"\n        ],\n        [\n            \"DAI\",\n            \"ETH\"\n        ],\n        [\n            \"DAPP\",\n            \"EOS\"\n        ],\n        [\n            \"DAT\",\n            \"ETH\"\n        ],\n        [\n            \"DGX\",\n            \"ETH\"\n        ],\n        [\n            \"DUSK\",\n            \"ETH\"\n        ],\n        [\n            \"EDO\",\n            \"ETH\"\n        ],\n        [\n            \"ENJ\",\n            \"ETH\"\n        ],\n        [\n            \"EOSDT\",\n            \"EOS\"\n        ],\n        [\n            \"ESS\",\n            \"ETH\"\n        ],\n        [\n            \"EUE\",\n            \"ETH\"\n        ],\n        [\n            \"EUS\",\n            \"ETH\"\n        ],\n        [\n            \"EXRD\",\n            \"ETH\"\n        ],\n        [\n            \"FET\",\n            \"ETH\"\n        ],\n        [\n            \"FORTH\",\n            \"ETH\"\n        ],\n        [\n            \"FTT\",\n            \"ETH\"\n        ],\n        [\n            \"FUN\",\n            \"ETH\"\n        ],\n        [\n            \"GNO\",\n            \"ETH\"\n        ],\n        [\n            \"GNT\",\n            \"ETH\"\n        ],\n        [\n            \"GOT\",\n            \"ETH\"\n        ],\n        [\n            \"GTX\",\n            \"ETH\"\n        ],\n        [\n            \"HEZ\",\n            \"ETH\"\n        ],\n        [\n            \"ICE\",\n            \"ETH\"\n        ],\n        [\n            \"IDX\",\n            \"ETH\"\n        ],\n        [\n            \"IQX\",\n            \"EOS\"\n        ],\n        [\n            \"JST\",\n            \"TRX\"\n        ],\n        [\n            \"KAN\",\n            \"ETH\"\n        ],\n        [\n            \"KNC\",\n            \"ETH\"\n        ],\n        [\n            \"LES\",\n            \"EOS\"\n        ],\n        [\n            \"LET\",\n            \"ETH\"\n        ],\n        [\n            \"LINK\",\n            \"ETH\"\n        ],\n        [\n            \"LRC\",\n            \"ETH\"\n        ],\n        [\n            \"LYM\",\n            \"ETH\"\n        ],\n        [\n            \"MKR\",\n            \"ETH\"\n        ],\n        [\n            \"MLN\",\n            \"ETH\"\n        ],\n        [\n            \"MNA\",\n            \"ETH\"\n        ],\n        [\n            \"MTO\",\n            \"EOS\"\n        ],\n        [\n            \"NEC\",\n            \"ETH\"\n        ],\n        [\n            \"NUT\",\n            \"EOS\"\n        ],\n        [\n            \"OCEAN\",\n            \"ETH\"\n        ],\n        [\n            \"ODE\",\n            \"ETH\"\n        ],\n        [\n            \"OMG\",\n            \"ETH\"\n        ],\n        [\n            \"ORS\",\n            \"ETH\"\n        ],\n        [\n            \"PANTEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PAS\",\n            \"ETH\"\n        ],\n        [\n            \"PAX\",\n            \"ETH\"\n        ],\n        [\n            \"PBALEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PBANDEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PBATEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PBTCEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PBTCETH\",\n            \"ETH\"\n        ],\n        [\n            \"PCOMPEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PDAIEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PEOSETH\",\n            \"ETH\"\n        ],\n        [\n            \"PETHEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PLINKEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PLRCEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PLTCEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PLTCETH\",\n            \"ETH\"\n        ],\n        [\n            \"PLU\",\n            \"ETH\"\n        ],\n        [\n            \"PMKREOS\",\n            \"EOS\"\n        ],\n        [\n            \"PNK\",\n            \"ETH\"\n        ],\n        [\n            \"POA\",\n            \"ETH\"\n        ],\n        [\n            \"POMGEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PPNKEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PPNTEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PREPEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PSNXEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PUNIEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PUOSEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PYFIEOS\",\n            \"EOS\"\n        ],\n        [\n            \"PZRXEOS\",\n            \"EOS\"\n        ],\n        [\n            \"QSH\",\n            \"ETH\"\n        ],\n        [\n            \"QTF\",\n            \"ETH\"\n        ],\n        [\n            \"REP\",\n            \"ETH\"\n        ],\n        [\n            \"REQ\",\n            \"ETH\"\n        ],\n        [\n            \"RINGX\",\n            \"ETH\"\n        ],\n        [\n            \"RRB\",\n            \"ETH\"\n        ],\n        [\n            \"SAN\",\n            \"ETH\"\n        ],\n        [\n            \"SNG\",\n            \"ETH\"\n        ],\n        [\n            \"SNT\",\n            \"ETH\"\n        ],\n        [\n            \"SNX\",\n            \"ETH\"\n        ],\n        [\n            \"STJ\",\n            \"ETH\"\n        ],\n        [\n            \"SUKU\",\n            \"ETH\"\n        ],\n        [\n            \"SUN\",\n            \"TRX\"\n        ],\n        [\n            \"SUSHI\",\n            \"ETH\"\n        ],\n        [\n            \"TSD\",\n            \"ETH\"\n        ],\n        [\n            \"UDC\",\n            \"ETH\"\n        ],\n        [\n            \"UNI\",\n            \"ETH\"\n        ],\n        [\n            \"UOP\",\n            \"ETH\"\n        ],\n        [\n            \"UOS\",\n            \"ETH\"\n        ],\n        [\n            \"USE\",\n            \"ETH\"\n        ],\n        [\n            \"USK\",\n            \"ETH\"\n        ],\n        [\n            \"USL\",\n            \"LBT\"\n        ],\n        [\n            \"USS\",\n            \"EOS\"\n        ],\n        [\n            \"USX\",\n            \"TRX\"\n        ],\n        [\n            \"UTK\",\n            \"ETH\"\n        ],\n        [\n            \"VEE\",\n            \"ETH\"\n        ],\n        [\n            \"WBT\",\n            \"ETH\"\n        ],\n        [\n            \"XAUTE\",\n            \"ETH\"\n        ],\n        [\n            \"XCH\",\n            \"ETH\"\n        ],\n        [\n            \"XRA\",\n            \"ETH\"\n        ],\n        [\n            \"YFI\",\n            \"ETH\"\n        ],\n        [\n            \"YGG\",\n            \"ETH\"\n        ],\n        [\n            \"ZBT\",\n            \"ETH\"\n        ],\n        [\n            \"ZCN\",\n            \"ETH\"\n        ],\n        [\n            \"ZRX\",\n            \"ETH\"\n        ]\n    ],\n    [\n        [\n            \"ADA\",\n            [\n                \"https://cardanoexplorer.com\",\n                \"https://cardanoexplorer.com/address/VAL\",\n                \"https://cardanoexplorer.com/tx/VAL\"\n            ]\n        ],\n        [\n            \"ALG\",\n            [\n                \"https://algoexplorer.io\",\n                \"https://algoexplorer.io/address/VAL\",\n                \"https://algoexplorer.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"ATO\",\n            [\n                \"https://www.mintscan.io/cosmos\",\n                \"https://www.mintscan.io/cosmos/account/VAL\",\n                \"https://www.mintscan.io/cosmos/txs/VAL\"\n            ]\n        ],\n        [\n            \"AVAX\",\n            [\n                \"https://explorer.avax.network\",\n                \"https://explorer.avax.network/address/VAL\",\n                \"https://explorer.avax.network/tx/VAL\"\n            ]\n        ],\n        [\n            \"BCHN\",\n            [\n                \"https://blockdozer.com\",\n                \"https://blockdozer.com/address/VAL\",\n                \"https://blockdozer.com/tx/VAL\"\n            ]\n        ],\n        [\n            \"BSV\",\n            [\n                \"https://whatsonchain.com\",\n                \"https://whatsonchain.com/address/VAL\",\n                \"https://whatsonchain.com/tx/VAL\"\n            ]\n        ],\n        [\n            \"BTC\",\n            [\n                \"https://blockstream.info\",\n                \"https://blockstream.info/address/VAL\",\n                \"https://blockstream.info/tx/VAL\"\n            ]\n        ],\n        [\n            \"BTG\",\n            [\n                \"https://explorer.bitcoingold.org/insight\",\n                \"https://explorer.bitcoingold.org/insight/address/VAL\",\n                \"https://explorer.bitcoingold.org/insight/tx/VAL\"\n            ]\n        ],\n        [\n            \"CLO\",\n            [\n                \"https://explorer2.callisto.network\",\n                \"https://explorer2.callisto.network/addr/VAL\",\n                \"https://explorer2.callisto.network/tx/VAL\"\n            ]\n        ],\n        [\n            \"CTK\",\n            [\n                \"https://explorer.certik.foundation\",\n                \"https://explorer.certik.foundation/accounts/VAL?net=shentu-1\",\n                \"https://explorer.certik.foundation/transactions/VAL?net=shentu-1\"\n            ]\n        ],\n        [\n            \"DGB\",\n            [\n                \"https://digiexplorer.info\",\n                \"https://digiexplorer.info/address/VAL\",\n                \"https://digiexplorer.info/tx/VAL\"\n            ]\n        ],\n        [\n            \"DOG\",\n            [\n                \"https://dogechain.info\",\n                \"https://dogechain.info/address/VAL\",\n                \"https://dogechain.info/tx/VAL\"\n            ]\n        ],\n        [\n            \"DOT\",\n            [\n                \"https://polkadot.subscan.io\",\n                \"https://polkadot.subscan.io/account/VAL\",\n                \"https://polkadot.subscan.io/extrinsic/VAL\"\n            ]\n        ],\n        [\n            \"DSH\",\n            [\n                \"https://explorer.dash.org\",\n                \"https://explorer.dash.org/address/VAL\",\n                \"https://explorer.dash.org/tx/VAL\"\n            ]\n        ],\n        [\n            \"EGLD\",\n            [\n                \"https://explorer.elrond.com\",\n                \"https://explorer.elrond.com/address/VAL\",\n                \"https://explorer.elrond.com/transactions/VAL\"\n            ]\n        ],\n        [\n            \"EOS\",\n            [\n                \"https://bloks.io\",\n                \"https://bloks.io/account/VAL\",\n                \"https://bloks.io/transaction/VAL\"\n            ]\n        ],\n        [\n            \"ETC\",\n            [\n                \"https://blockscout.com/etc/mainnet\",\n                \"https://blockscout.com/etc/mainnet/address/VAL\",\n                \"https://blockscout.com/etc/mainnet/tx/VAL\"\n            ]\n        ],\n        [\n            \"ETH\",\n            [\n                \"https://etherscan.io\",\n                \"https://etherscan.io/address/VAL\",\n                \"https://etherscan.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"ETP\",\n            [\n                \"http://explorer.mvs.live/#!\",\n                \"http://explorer.mvs.live/#!/adr/VAL\",\n                \"http://explorer.mvs.live/#!/tx/VAL\"\n            ]\n        ],\n        [\n            \"FIL\",\n            [\n                \"https://filfox.info/en\",\n                \"https://filfox.info/en/address/VAL\",\n                \"https://filfox.info/en/message/VAL\"\n            ]\n        ],\n        [\n            \"FTM\",\n            [\n                \"https://ftmscan.com\",\n                \"https://ftmscan.com/address/VAL\",\n                \"https://ftmscan.com/tx/VAL\"\n            ]\n        ],\n        [\n            \"IOT\",\n            [\n                \"https://explorer.iota.org/mainnet\",\n                \"https://explorer.iota.org/mainnet/addr/VAL\",\n                \"https://explorer.iota.org/mainnet/message/VAL\"\n            ]\n        ],\n        [\n            \"KSM\",\n            [\n                \"https://kusama.subscan.io\",\n                \"https://kusama.subscan.io/account/VAL\",\n                \"https://kusama.subscan.io/extrinsic/VAL\"\n            ]\n        ],\n        [\n            \"LBT\",\n            [\n                \"https://blockstream.info/liquid\",\n                \"https://blockstream.info/liquid/address/VAL\",\n                \"https://blockstream.info/liquid/tx/VAL\"\n            ]\n        ],\n        [\n            \"NEAR\",\n            [\n                \"https://explorer.near.org\",\n                \"https://explorer.near.org/accounts/VAL\",\n                \"https://explorer.near.org/transactions/VAL\"\n            ]\n        ],\n        [\n            \"NEO\",\n            [\n                \"https://neotracker.io\",\n                \"https://neotracker.io/address/VAL\",\n                \"https://neotracker.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"OMN\",\n            [\n                \"http://omniexplorer.info\",\n                \"http://omniexplorer.info/lookupadd.aspx?address=VAL\",\n                \"http://omniexplorer.info/lookuptx.aspx?txid=VAL\"\n            ]\n        ],\n        [\n            \"QTM\",\n            [\n                \"https://explorer.qtum.org\",\n                \"https://explorer.qtum.org/address/VAL\",\n                \"https://explorer.qtum.org/tx/VAL\"\n            ]\n        ],\n        [\n            \"RBT\",\n            [\n                \"https://explorer.rsk.co\",\n                \"https://explorer.rsk.co/address/VAL\",\n                \"https://explorer.rsk.co/tx/VAL\"\n            ]\n        ],\n        [\n            \"SOL\",\n            [\n                \"https://explorer.solana.com\",\n                \"https://explorer.solana.com/address/VAL\",\n                \"https://explorer.solana.com/tx/VAL\"\n            ]\n        ],\n        [\n            \"TRX\",\n            [\n                \"https://tronscan.org/#\",\n                \"https://tronscan.org/#/address/VAL\",\n                \"https://tronscan.org/#/transaction/VAL\"\n            ]\n        ],\n        [\n            \"USDTALG\",\n            [\n                \"https://algoexplorer.io\",\n                \"https://algoexplorer.io/address/VAL\",\n                \"https://algoexplorer.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"USDTOMG\",\n            [\n                \"https://blockexplorer.mainnet.v1.omg.network\",\n                \"https://blockexplorer.mainnet.v1.omg.network/address/VAL\",\n                \"https://blockexplorer.mainnet.v1.omg.network/transaction/VAL\"\n            ]\n        ],\n        [\n            \"USO\",\n            [\n                \"http://omniexplorer.info\",\n                \"http://omniexplorer.info/lookupadd.aspx?address=VAL\",\n                \"http://omniexplorer.info/lookuptx.aspx?txid=VAL\"\n            ]\n        ],\n        [\n            \"VET\",\n            [\n                \"https://insight.vecha.in/#/\",\n                \"https://insight.vecha.in/#//accounts/VAL\",\n                \"https://insight.vecha.in/#//txs/VAL\"\n            ]\n        ],\n        [\n            \"VSY\",\n            [\n                \"https://explorer.v.systems\",\n                \"https://explorer.v.systems/address/VAL\",\n                \"https://explorer.v.systems/transactions/VAL\"\n            ]\n        ],\n        [\n            \"WAX\",\n            [\n                \"https://wax.bloks.io\",\n                \"https://wax.bloks.io/account/VAL\",\n                \"https://wax.bloks.io/transaction/VAL\"\n            ]\n        ],\n        [\n            \"XLM\",\n            [\n                \"https://stellarchain.io\",\n                \"https://stellarchain.io/address/VAL\",\n                \"https://stellarchain.io/tx/VAL\"\n            ]\n        ],\n        [\n            \"XMR\",\n            [\n                \"https://moneroblocks.info\",\n                \"https://moneroblocks.info/search/VAL\",\n                \"https://moneroblocks.info/search/VAL\"\n            ]\n        ],\n        [\n            \"XRP\",\n            [\n                \"https://xrpscan.com\",\n                \"https://xrpscan.com/account/VAL\",\n                \"https://xrpscan.com/tx/VAL\"\n            ]\n        ],\n        [\n            \"XSN\",\n            [\n                \"https://xsnexplorer.io\",\n                \"https://xsnexplorer.io/addresses/VAL\",\n                \"https://xsnexplorer.io/transactions/VAL\"\n            ]\n        ],\n        [\n            \"XTZ\",\n            [\n                \"https://tzstats.com\",\n                \"https://tzstats.com/account/VAL\",\n                \"https://tzstats.com/operation/VAL\"\n            ]\n        ],\n        [\n            \"XVG\",\n            [\n                \"https://verge-blockchain.info\",\n                \"https://verge-blockchain.info/address/VAL\",\n                \"https://verge-blockchain.info/tx/VAL\"\n            ]\n        ],\n        [\n            \"ZEC\",\n            [\n                \"https://explorer.zcha.in\",\n                \"https://explorer.zcha.in/accounts/VAL\",\n                \"https://explorer.zcha.in/transactions/VAL\"\n            ]\n        ],\n        [\n            \"ZIL\",\n            [\n                \"https://viewblock.io/zilliqa\",\n                \"https://viewblock.io/zilliqa/address/VAL\",\n                \"https://viewblock.io/zilliqa/tx/VAL\"\n            ]\n        ]\n    ],\n    [\n        [\n            \"AAA\",\n            \"TESTAAA\"\n        ],\n        [\n            \"ALG\",\n            \"ALGO\"\n        ],\n        [\n            \"AMP\",\n            \"AMPL\"\n        ],\n        [\n            \"AMPF0\",\n            \"AMPLF0\"\n        ],\n        [\n            \"ATO\",\n            \"ATOM\"\n        ],\n        [\n            \"B21X\",\n            \"B21\"\n        ],\n        [\n            \"BBB\",\n            \"TESTBBB\"\n        ],\n        [\n            \"BTCF0\",\n            \"BTC\"\n        ],\n        [\n            \"CNHT\",\n            \"CNHt\"\n        ],\n        [\n            \"DAT\",\n            \"DATA\"\n        ],\n        [\n            \"DOG\",\n            \"MDOGE\"\n        ],\n        [\n            \"DSH\",\n            \"DASH\"\n        ],\n        [\n            \"EDO\",\n            \"PNT\"\n        ],\n        [\n            \"ETH2P\",\n            \"ETH2Pending\"\n        ],\n        [\n            \"ETH2R\",\n            \"ETH2Rewards\"\n        ],\n        [\n            \"ETH2X\",\n            \"ETH2\"\n        ],\n        [\n            \"EUS\",\n            \"EURS\"\n        ],\n        [\n            \"EUT\",\n            \"EURt\"\n        ],\n        [\n            \"GNT\",\n            \"GLM\"\n        ],\n        [\n            \"IDX\",\n            \"ID\"\n        ],\n        [\n            \"IOT\",\n            \"IOTA\"\n        ],\n        [\n            \"LBT\",\n            \"LBTC\"\n        ],\n        [\n            \"LES\",\n            \"LEO-EOS\"\n        ],\n        [\n            \"LET\",\n            \"LEO-ERC20\"\n        ],\n        [\n            \"LNX\",\n            \"LN-BTC\"\n        ],\n        [\n            \"MNA\",\n            \"MANA\"\n        ],\n        [\n            \"OMN\",\n            \"OMNI\"\n        ],\n        [\n            \"PAS\",\n            \"PASS\"\n        ],\n        [\n            \"PBTCEOS\",\n            \"pBTC-EOS\"\n        ],\n        [\n            \"PBTCETH\",\n            \"PBTC-ETH\"\n        ],\n        [\n            \"PETHEOS\",\n            \"pETH-EOS\"\n        ],\n        [\n            \"PLTCEOS\",\n            \"PLTC-EOS\"\n        ],\n        [\n            \"PLTCETH\",\n            \"PLTC-ETH\"\n        ],\n        [\n            \"QSH\",\n            \"QASH\"\n        ],\n        [\n            \"QTM\",\n            \"QTUM\"\n        ],\n        [\n            \"RBT\",\n            \"RBTC\"\n        ],\n        [\n            \"REP\",\n            \"REP2\"\n        ],\n        [\n            \"SNG\",\n            \"SNGLS\"\n        ],\n        [\n            \"STJ\",\n            \"STORJ\"\n        ],\n        [\n            \"TSD\",\n            \"TUSD\"\n        ],\n        [\n            \"UDC\",\n            \"USDC\"\n        ],\n        [\n            \"USK\",\n            \"USDK\"\n        ],\n        [\n            \"UST\",\n            \"USDt\"\n        ],\n        [\n            \"USTF0\",\n            \"USDt\"\n        ],\n        [\n            \"VSY\",\n            \"VSYS\"\n        ],\n        [\n            \"WBT\",\n            \"WBTC\"\n        ],\n        [\n            \"XAUT\",\n            \"XAUt\"\n        ],\n        [\n            \"XCH\",\n            \"XCHF\"\n        ],\n        [\n            \"YGG\",\n            \"MCS\"\n        ],\n        [\n            \"YYW\",\n            \"YOYOW\"\n        ]\n    ]\n]"
                  },
                  "Result": {
                    "value": "[\n    {\n        \"deriv_perp\": {\n            \"correction_clamp_min\": 0.0025,\n            \"correction_clamp_insurance\": 0.0015,\n            \"correction_slope\": 0.2\n        }\n    }\n]"
                  },
                  "pub:fees": {
                    "value": "[{\"deriv_perp\":{\"correction_clamp_min\":0.0025,\"correction_clamp_insurance\":0.0015,\"correction_slope\":0.2}}]"
                  },
                  "pub:list:competitions": {
                    "value": "[\t\n  [\n\t\"plu_diff:1w:tGLOBAL:USD\",\n\t\"plu_diff:1M:tGLOBAL:USD\",\n\t\"plu:1w:tGLOBAL:USD\",\n\t\"plu:3h:tGLOBAL:USD\",\n\t\"vol:1w:tGLOBAL:USD\",\n\t\"vol:1M:tGLOBAL:USD\",\n\t\"vol:3h:tGLOBAL:USD\",\n\t\"plr:1M:tGLOBAL:USD\",\n\t\"plu:3h:tBTCUSD\",\n\t\"plu:3h:tBTCF0:USTF0\",\n\t\"plu:3h:tBTCUST\",\n\t\"plu:3h:tBTCEUR\",\n\t\"plu:3h:tLEOUSD\",\n\t\"plu:3h:tETHUSD\",\n\t\"plu:3h:tETHF0:USTF0\",\n\t\"plu:3h:tETHUST\",\n\t\"plu:3h:tEOSUSD\",\n\t\"plu:3h:tLTCUSD\",\n\t\"plu:3h:tETCUSD\",\n\t\"vol:3h:tBTCUSD\",\n\t\"vol:3h:tBTCF0:USTF0\",\n\t\"vol:3h:tBTCUST\",\n\t\"vol:3h:tETHUSD\",\n  \"vol:3h:tETHF0:USTF0\",\n  \"vol:3h:tETHUST\",\n  \"vol:3h:tEOSUSD\",\n  \"vol:3h:tLTCUSD\",\n  \"vol:3h:tETCUSD\"\n  ]\n]"
                  },
                  "pub:info:tx:status": {
                    "value": "[[[\"BITCOIN\",1,1,null,null,null,null,0,0],[\"LITECOIN\",1,1,null,null,null,null,0,0],[\"ETHEREUM\",1,1,null,null,null,null,0,0],[\"ETHEREUMC\",1,1,null,null,null,null,0,0],[\"ZCASH\",1,1,null,null,null,null,0,0],[\"MONERO\",1,1,null,null,null,null,0,0],[\"DASH\",1,1,null,null,null,null,0,0],[\"RIPPLE\",1,1,null,null,null,null,1,1],[\"IOTA\",1,1,null,null,null,null,0,0],[\"TETHERUSO\",1,1,null,null,null,null,0,0],[\"EOS\",1,1,null,null,null,null,1,1],[\"SANTIMENT\",1,1,null,null,null,null,0,0],[\"OMISEGO\",1,1,null,null,null,null,0,0],[\"NEO\",1,1,null,null,null,null,0,0],[\"METAVERSE\",1,1,null,null,null,null,0,0],[\"QTUM\",1,1,null,null,null,null,0,0],[\"AVENTUS\",1,1,null,null,null,null,0,0],[\"EIDOO\",1,1,null,null,null,null,0,0],[\"BGOLD\",1,1,null,null,null,null,0,0],[\"DATACOIN\",1,1,null,null,null,null,0,0],[\"TETHERUSE\",1,1,null,null,null,null,0,0],[\"QASH\",1,1,null,null,null,null,0,0],[\"YYW\",0,1,null,null,null,null,1,1],[\"GOLEM\",1,1,null,null,null,null,0,0],[\"STATUS\",1,1,null,null,null,null,0,0],[\"TETHEREUE\",1,1,null,null,null,null,0,0],[\"BAT\",1,1,null,null,null,null,0,0],[\"MNA\",1,1,null,null,null,null,0,0],[\"FUN\",1,1,null,null,null,null,0,0],[\"ZRX\",1,1,null,null,null,null,0,0],[\"TNB\",1,1,null,null,null,null,0,0],[\"SPK\",1,1,null,null,null,null,0,0],[\"TRX\",1,1,null,null,null,null,0,0],[\"RCN\",1,1,null,null,null,null,0,0],[\"RLC\",1,1,null,null,null,null,0,0],[\"AID\",1,1,null,null,null,null,0,0],[\"SNG\",1,1,null,null,null,null,0,0],[\"REP\",1,1,null,null,null,null,0,0],[\"ELF\",1,1,null,null,null,null,0,0],[\"NEC\",1,1,null,null,null,null,0,0],[\"IOS\",1,1,null,null,null,null,0,0],[\"AIO\",1,1,null,null,null,null,0,0],[\"REQ\",1,1,null,null,null,null,0,0],[\"RDN\",1,1,null,null,null,null,0,0],[\"LRC\",1,1,null,null,null,null,0,0],[\"WAX\",1,1,null,null,null,null,1,1],[\"DAI\",1,1,null,null,null,null,0,0],[\"AGI\",1,1,null,null,null,null,0,0],[\"BFT\",1,1,null,null,null,null,0,0],[\"MTN\",1,1,null,null,null,null,0,0],[\"ODE\",1,1,null,null,null,null,0,0],[\"ANT\",1,1,null,null,null,null,0,0],[\"DTH\",1,1,null,null,null,null,0,0],[\"MIT\",1,1,null,null,null,null,0,0],[\"STJ\",1,1,null,null,null,null,0,0],[\"XLM\",1,1,null,null,null,null,1,1],[\"XVG\",1,1,null,null,null,null,0,0],[\"MKR\",1,1,null,null,null,null,0,0],[\"KNC\",1,1,null,null,null,null,0,0],[\"POA\",0,0,null,null,null,null,0,0],[\"EVT\",0,0,null,null,null,null,0,0],[\"LYM\",1,1,null,null,null,null,0,0],[\"UTK\",1,1,null,null,null,null,0,0],[\"VEE\",1,1,null,null,null,null,0,0],[\"DAD\",0,0,null,null,null,null,0,0],[\"ORS\",1,1,null,null,null,null,0,0],[\"AUC\",1,1,null,null,null,null,0,0],[\"POY\",1,1,null,null,null,null,0,0],[\"FSN\",1,1,null,null,null,null,0,0],[\"CBT\",1,1,null,null,null,null,0,0],[\"ZCN\",1,1,null,null,null,null,0,0],[\"NCA\",1,1,null,null,null,null,0,0],[\"CND\",1,1,null,null,null,null,0,0],[\"CTX\",1,1,null,null,null,null,0,0],[\"PAI\",1,1,null,null,null,null,0,0],[\"SEE\",1,1,null,null,null,null,0,0],[\"ESS\",1,1,null,null,null,null,0,0],[\"ATD\",0,1,null,null,null,null,1,1],[\"ADD\",0,1,null,null,null,null,1,1],[\"MTO\",0,1,null,null,null,null,0,0],[\"ATM\",1,1,null,null,null,null,0,0],[\"HOT\",1,1,null,null,null,null,0,0],[\"DTA\",1,1,null,null,null,null,0,0],[\"IQX\",1,1,null,null,null,null,1,1],[\"WPR\",1,1,null,null,null,null,0,0],[\"ZIL\",1,1,null,null,null,null,0,0],[\"BNT\",1,1,null,null,null,null,0,0],[\"ABS\",1,1,null,null,null,null,0,0],[\"XRA\",1,1,null,null,null,null,0,0],[\"MAN\",0,0,null,null,null,null,0,0],[\"DGX\",1,1,null,null,null,null,0,0],[\"VET\",1,1,null,null,null,null,0,0],[\"UTN\",1,1,null,null,null,null,0,0],[\"TKN\",1,1,null,null,null,null,0,0],[\"GOT\",1,1,null,null,null,null,0,0],[\"XTZ\",1,1,null,null,null,null,0,0],[\"CNN\",1,1,null,null,null,null,0,0],[\"BOX\",1,1,null,null,null,null,0,0],[\"MGO\",1,1,null,null,null,null,0,0],[\"RTE\",1,1,null,null,null,null,0,0],[\"YGG\",1,1,null,null,null,null,0,0],[\"MLN\",1,1,null,null,null,null,0,0],[\"WTC\",1,1,null,null,null,null,0,0],[\"CSX\",1,1,null,null,null,null,0,0],[\"OMN\",1,1,null,null,null,null,0,0],[\"INT\",1,1,null,null,null,null,0,0],[\"DRN\",1,1,null,null,null,null,0,0],[\"PNK\",1,1,null,null,null,null,0,0],[\"DGB\",1,1,null,null,null,null,0,0],[\"BSV\",1,1,null,null,null,null,0,0],[\"BAB\",1,1,null,null,null,null,0,0],[\"WLO\",1,1,null,null,null,null,1,1],[\"VLD\",1,1,null,null,null,null,0,0],[\"ENJ\",1,1,null,null,null,null,0,0],[\"ONL\",1,1,null,null,null,null,0,0],[\"RBT\",1,1,null,null,null,null,0,0],[\"GSD\",1,1,null,null,null,null,0,0],[\"UDC\",1,1,null,null,null,null,0,0],[\"TSD\",1,1,null,null,null,null,0,0],[\"PAX\",1,1,null,null,null,null,0,0],[\"RIF\",1,1,null,null,null,null,0,0],[\"PAS\",1,1,null,null,null,null,0,0],[\"VSY\",1,1,null,null,null,null,0,0],[\"BTT\",1,1,null,null,null,null,0,0],[\"CLO\",1,1,null,null,null,null,0,0],[\"IMP\",1,1,null,null,null,null,0,0],[\"SCR\",0,0,null,null,null,null,0,0],[\"GNO\",1,1,null,null,null,null,0,0],[\"GEN\",1,1,null,null,null,null,0,0],[\"ATO\",1,1,null,null,null,null,0,0],[\"WBT\",1,1,null,null,null,null,0,0],[\"XCH\",1,1,null,null,null,null,0,0],[\"EUS\",1,1,null,null,null,null,0,0],[\"LBT\",1,1,null,null,null,null,0,0],[\"LES\",1,1,null,null,null,null,1,1],[\"LET\",1,1,null,null,null,null,0,0],[\"AST\",1,1,null,null,null,null,0,0],[\"FOA\",1,1,null,null,null,null,0,0],[\"UFR\",1,1,null,null,null,null,0,0],[\"ZBT\",1,0,null,null,null,null,0,0],[\"OKB\",1,1,null,null,null,null,0,0],[\"USK\",1,1,null,null,null,null,0,0],[\"GTX\",1,1,null,null,null,null,0,0],[\"KAN\",1,1,null,null,null,null,0,0],[\"AMP\",1,1,null,null,null,null,0,0],[\"ALG\",1,1,null,null,null,null,0,0],[\"SWM\",1,1,null,null,null,null,0,0],[\"TRI\",1,1,null,null,null,null,0,0],[\"LOO\",1,1,null,null,null,null,0,0],[\"DUSK\",1,1,null,null,null,null,0,0],[\"UOS\",1,1,null,null,null,null,0,0],[\"TETHERUSX\",1,1,null,null,null,null,0,0],[\"TETHERUSL\",1,1,null,null,null,null,0,0],[\"RRB\",1,1,null,null,null,null,0,0],[\"TETHERUSS\",1,1,null,null,null,null,1,1],[\"EOX\",0,0,null,null,null,null,0,0],[\"DTX\",1,1,null,null,null,null,0,0],[\"FTT\",1,1,null,null,null,null,0,0],[\"TETHERCNHTE\",1,1,null,null,null,null,0,0],[\"CHZ\",1,1,null,null,null,null,0,0],[\"LNX\",1,1,null,null,null,null,0,0],[\"TETHERXAUTE\",1,1,null,null,null,null,0,0],[\"TETHERUSDTALG\",1,1,null,null,null,null,0,0],[\"TETHERUSDTBCH\",1,1,null,null,null,null,0,0],[\"RINGX\",1,1,null,null,null,null,0,0],[\"BTSE\",1,0,null,null,null,null,0,0],[\"DOG\",1,1,null,null,null,null,0,0],[\"DOT\",1,0,null,null,null,null,0,0],[\"ADA\",1,1,null,null,null,null,0,0]]]"
                  },
                  "pub:list:pair:futures": {
                    "value": "[\n\t[\n  \"AMPF0:USTF0\",\n  \"BTCDOMF0:USTF0\",\n  \"BTCF0:USTF0\"\n  \"DOTF0:USTF0\",\n  \"EOSF0:USTF0\",\n  \"ETHF0:USTF0\",\n  \"EURF0:USTF0\",\n  \"EUROPE50IXF0:USTF0\",\n  \"GBPF0:USTF0\",\n  \"GERMANY30IXF0:USTF0\",\n  \"JPYF0:USTF0\",\n  \"LTCF0:USTF0\",\n  \"TESTBTCF0:TESTUSDTF0\",\n  \"XAGF0:USTF0\",\n  \"XAUTF0:USTF0\"\n  ]\n]"
                  },
                  "pub:map:tx:method": {
                    "value": "[\n  [\n    [\"BITCOIN\",[\"BTC\"]],\n    [\"LITECOIN\",[\"LTC\"]],\n    [\"ETHEREUM\",[\"ETH\"]],\n    [\"ETHEREUMC\",[\"ETC\"]],\n    [\"TETHERUSO\",[\"UST\"]],\n    [\"ZCASH\",[\"ZEC\"]],\n    [\"MONERO\",[\"XMR\"]],\n    [\"IOTA\",[\"IOT\"]],\n    [\"RIPPLE\",[\"XRP\"]],\n    [\"DASH\",[\"DSH\"]],\n    [\"WIRE\",[\"USD\",\"GBP\",\"HKD\",\"EUR\",\"SGD\",\"TWD\",\"CHF\",\"JPY\",\"CNH\"]],\n    [\"EOS\",[\"EOS\"]],\n    [\"SANTIMENT\",[\"SAN\"]],\n    [\"OMISEGO\",[\"OMG\"]],\n    [\"NEO\",[\"NEO\"]],\n    [\"METAVERSE\",[\"ETP\"]],\n    [\"QTUM\",[\"QTM\"]],\n    [\"AVENTUS\",[\"AVT\"]],\n    [\"EIDOO\",[\"EDO\"]],\n    [\"DATACOIN\",[\"DAT\"]],\n    [\"TETHERUSE\",[\"UST\"]],\n    [\"BGOLD\",[\"BTG\"]],\n    [\"QASH\",[\"QSH\"]],\n    [\"GOLEM\",[\"GNT\"]],\n    [\"STATUS\",[\"SNT\"]],\n    [\"TETHEREUE\",[\"EUT\"]],\n    [\"BAT\",[\"BAT\"]],\n    [\"MNA\",[\"MNA\"]],\n    [\"FUN\",[\"FUN\"]],\n    [\"ZRX\",[\"ZRX\"]],\n    [\"TNB\",[\"TNB\"]],\n    [\"SPK\",[\"SPK\"]],\n    [\"TRX\",[\"TRX\"]],\n    [\"RCN\",[\"RCN\"]],\n    [\"RLC\",[\"RLC\"]],\n    [\"AID\",[\"AID\"]],\n    [\"SNG\",[\"SNG\"]],\n    [\"REP\",[\"REP\"]],\n    [\"ELF\",[\"ELF\"]],\n    [\"NEC\",[\"NEC\"]],\n    [\"IOS\",[\"IOS\"]],\n    [\"AIO\",[\"AIO\"]],\n    [\"REQ\",[\"REQ\"]],\n    [\"RDN\",[\"RDN\"]],\n    [\"LRC\",[\"LRC\"]],\n    [\"WAX\",[\"WAX\"]],\n    [\"DAI\",[\"DAI\"]],\n    [\"AGI\",[\"AGI\"]],\n    [\"BFT\",[\"BFT\"]],\n    [\"MTN\",[\"MTN\"]],\n    [\"ODE\",[\"ODE\"]],\n    [\"ANT\",[\"ANT\"]],\n    [\"DTH\",[\"DTH\"]],\n    [\"MIT\",[\"MIT\"]],\n    [\"STJ\",[\"STJ\"]],\n    [\"XLM\",[\"XLM\"]],\n    [\"XVG\",[\"XVG\"]],\n    [\"MKR\",[\"MKR\"]],\n    [\"KNC\",[\"KNC\"]],\n    [\"POA\",[\"POA\"]],\n    [\"EVT\",[\"EVT\"]],\n    [\"LYM\",[\"LYM\"]],\n    [\"UTK\",[\"UTK\"]],\n    [\"VEE\",[\"VEE\"]],\n    [\"ORS\",[\"ORS\"]],\n    [\"AUC\",[\"AUC\"]],\n    [\"POY\",[\"POY\"]],\n    [\"FSN\",[\"FSN\"]],\n    [\"CBT\",[\"CBT\"]],\n    [\"ZCN\",[\"ZCN\"]],\n    [\"NCA\",[\"NCA\"]],\n    [\"CND\",[\"CND\"]],\n    [\"CTX\",[\"CTX\"]],\n    [\"PAI\",[\"PAI\"]],\n    [\"SEE\",[\"SEE\"]],\n    [\"ESS\",[\"ESS\"]],\n    [\"ATD\",[\"ATD\"]],\n    [\"ADD\",[\"ADD\"]],\n    [\"MTO\",[\"MTO\"]],\n    [\"ATM\",[\"ATM\"]],\n    [\"HOT\",[\"HOT\"]],\n    [\"DTA\",[\"DTA\"]],\n    [\"IQX\",[\"IQX\"]],\n    [\"WPR\",[\"WPR\"]],\n    [\"ZIL\",[\"ZIL\"]],\n    [\"BNT\",[\"BNT\"]],\n    [\"ABS\",[\"ABS\"]],\n    [\"XRA\",[\"XRA\"]],\n    [\"MAN\",[\"MAN\"]],\n    [\"DGX\",[\"DGX\"]],\n    [\"VET\",[\"VET\"]],\n    [\"UTN\",[\"UTN\"]],\n    [\"TKN\",[\"TKN\"]],\n    [\"GOT\",[\"GOT\"]],\n    [\"XTZ\",[\"XTZ\"]],\n    [\"CNN\",[\"CNN\"]],\n    [\"BOX\",[\"BOX\"]],\n    [\"MGO\",[\"MGO\"]],\n    [\"RTE\",[\"RTE\"]],\n    [\"YGG\",[\"YGG\"]],\n    [\"MLN\",[\"MLN\"]],\n    [\"WTC\",[\"WTC\"]],\n    [\"CSX\",[\"CSX\"]],\n    [\"OMN\",[\"OMN\"]],\n    [\"DRN\",[\"DRN\"]],\n    [\"PNK\",[\"PNK\"]],\n    [\"DGB\",[\"DGB\"]],\n    [\"BSV\",[\"BSV\"]],\n    [\"VLD\",[\"VLD\"]],\n    [\"ENJ\",[\"ENJ\"]],\n    [\"ONL\",[\"ONL\"]],\n    [\"RBT\",[\"RBT\"]],\n    [\"GSD\",[\"GSD\"]],\n    [\"UDC\",[\"UDC\"]],\n    [\"TSD\",[\"TSD\"]],\n    [\"PAX\",[\"PAX\"]],\n    [\"RIF\",[\"RIF\"]],\n    [\"PAS\",[\"PAS\"]],\n    [\"VSY\",[\"VSY\"]],\n    [\"BTT\",[\"BTT\"]],\n    [\"CLO\",[\"CLO\"]],\n    [\"IMP\",[\"IMP\"]],\n    [\"SCR\",[\"SCR\"]],\n    [\"GNO\",[\"GNO\"]],\n    [\"GEN\",[\"GEN\"]],\n    [\"ATO\",[\"ATO\"]],\n    [\"WBT\",[\"WBT\"]],\n    [\"XCH\",[\"XCH\"]],\n    [\"EUS\",[\"EUS\"]],\n    [\"LBT\",[\"LBT\"]],\n    [\"LET\",[\"LET\"]],\n    [\"LES\",[\"LES\"]],\n    [\"AST\",[\"AST\"]],\n    [\"FOA\",[\"FOA\"]],\n    [\"UFR\",[\"UFR\"]],\n    [\"ZBT\",[\"ZBT\"]],\n    [\"OKB\",[\"OKB\"]],\n    [\"USK\",[\"USK\"]],\n    [\"GTX\",[\"GTX\"]],\n    [\"KAN\",[\"KAN\"]],\n    [\"AMP\",[\"AMP\"]],\n    [\"ALG\",[\"ALG\"]],\n    [\"SWM\",[\"SWM\"]],\n    [\"TRI\",[\"TRI\"]],\n    [\"LOO\",[\"LOO\"]],\n    [\"DUSK\",[\"DUSK\"]],\n    [\"UOS\",[\"UOS\"]],\n    [\"TETHERUSX\",[\"UST\"]],\n    [\"TETHERUSL\",[\"UST\"]],\n    [\"RRB\",[\"RRB\"]],\n    [\"TETHERUSS\",[\"UST\"]],\n    [\"EOX\",[\"EOX\"]],\n    [\"DTX\",[\"DTX\"]],\n    [\"FTT\",[\"FTT\"]],\n    [\"TETHERCNHTE\",[\"CNHT\"]],\n    [\"CHZ\",[\"CHZ\"]],\n    [\"LNX\",[\"LNX\"]],\n    [\"TETHERXAUTE\",[\"XAUT\"]],\n    [\"TETHERUSDTALG\",[\"UST\"]],\n    [\"TETHERUSDTBCH\",[\"UST\"]],\n    [\"RINGX\",[\"RINGX\"]],\n    [\"BTSE\",[\"BTSE\"]],\n    [\"DOG\",[\"DOG\"]],\n    [\"DOT\",[\"DOT\"]],\n    [\"YYW\",[\"YYW\"]],\n    [\"ADA\",[\"ADA\"]],\n    [\"FET\",[\"FET\"]],\n    [\"TETHERUSDTOMG\",[\"UST\"]],\n    [\"LINK\",[\"LINK\"]],\n    [\"COMP\",[\"COMP\"]],\n    [\"KSM\",[\"KSM\"]],\n    [\"EGLD\",[\"EGLD\"]],\n    [\"UNI\",[\"UNI\"]],\n    [\"BAND\",[\"BAND\"]],\n    [\"AVAX\",[\"AVAX\"]],\n    [\"SNX\",[\"SNX\"]],\n    [\"YFI\",[\"YFI\"]],\n    [\"BAL\",[\"BAL\"]],\n    [\"PBTCEOS\",[\"PBTCEOS\"]],\n    [\"EOSDT\",[\"EOSDT\"]],\n    [\"NUT\",[\"NUT\"]],\n    [\"PLTCEOS\",[\"PLTCEOS\"]],\n    [\"PETHEOS\",[\"PETHEOS\"]],\n    [\"DAPP\",[\"DAPP\"]],\n    [\"FIL\",[\"FIL\"]],\n    [\"PBTCETH\",[\"PBTCETH\"]],\n    [\"PEOSETH\",[\"PEOSETH\"]],\n    [\"PLTCETH\",[\"PLTCETH\"]],\n    [\"PPNTEOS\",[\"PPNTEOS\"]],\n    [\"PLINKEOS\",[\"PLINKEOS\"]],\n    [\"PMKREOS\",[\"PMKREOS\"]],\n    [\"PYFIEOS\",[\"PYFIEOS\"]],\n    [\"JST\",[\"JST\"]],\n    [\"HEZ\",[\"HEZ\"]],\n    [\"BCHABC\",[\"BCHABC\"]],\n    [\"BCHN\",[\"BCHN\"]],\n    [\"XDC\",[\"XDC\"]]\n  ]\n]"
                  },
                  "pub:spec:margin": {
                    "value": "[{\"conf\":{\"base_size_thres\":0,\"base_size_incr\":1,\"base_step\":0,\"base_haircut\":1,\"IOT_haircut\":0.5,\"SAN_haircut\":0.001,\"OMG_haircut\":0.5,\"ETP_haircut\":0.001,\"EDO_haircut\":0.001,\"BTG_haircut\":0.001,\"TRX_haircut\":0.5,\"DAI_haircut\":0.75,\"XLM_haircut\":0.5,\"XTZ_haircut\":0.7,\"BSV_haircut\":0.25,\"ATO_haircut\":0.3,\"AMP_haircut\":0.5,\"ALG_haircut\":0.25,\"FTT_haircut\":0.001,\"DOT_haircut\":0.3,\"ADA_haircut\":0.5,\"LINK_haircut\":0.1,\"UNI_haircut\":0.1,\"YFI_haircut\":0.1,\"FIL_haircut\":0.5,\"SUSHI_haircut\":0.1},\"initial\":{\"base\":0.3,\"base_cap\":1,\"BTCUSD\":0.2,\"LTCUSD\":0.2,\"LTCBTC\":0.3,\"ETHUSD\":0.2,\"ETHBTC\":0.2,\"ETCBTC\":0.3,\"ETCUSD\":0.3,\"ZECUSD\":0.3,\"ZECBTC\":0.3,\"XMRUSD\":0.3,\"XMRBTC\":0.3,\"DSHUSD\":0.3,\"DSHBTC\":0.3,\"BTCEUR\":0.2,\"BTCJPY\":0.3,\"XRPUSD\":0.2,\"XRPBTC\":0.2,\"IOTUSD\":0.3,\"IOTBTC\":0.3,\"IOTETH\":0.3,\"EOSUSD\":0.2,\"EOSBTC\":0.3,\"EOSETH\":0.3,\"SANUSD\":0.3,\"SANUSD_risk\":0.6,\"SANBTC\":0.3,\"SANBTC_risk\":0.6,\"SANETH\":0.3,\"SANETH_risk\":0.6,\"OMGUSD\":0.3,\"OMGBTC\":0.3,\"OMGETH\":0.3,\"NEOUSD\":0.3,\"NEOBTC\":0.3,\"NEOETH\":0.3,\"ETPUSD\":0.3,\"ETPUSD_risk\":0.6,\"ETPBTC\":0.3,\"ETPBTC_risk\":0.6,\"ETPETH\":0.3,\"ETPETH_risk\":0.6,\"EDOUSD\":0.3,\"EDOUSD_risk\":0.6,\"EDOBTC\":0.3,\"EDOBTC_risk\":0.6,\"EDOETH\":0.3,\"EDOETH_risk\":0.6,\"BTGUSD\":0.3,\"BTGUSD_risk\":0.6,\"BTGBTC\":0.3,\"BTGBTC_risk\":0.6,\"IOTEUR\":0.3,\"ZRXUSD\":0.3,\"ZRXETH\":0.3,\"TRXUSD\":0.3,\"BTCGBP\":0.3,\"ETHEUR\":0.3,\"ETHJPY\":0.3,\"ETHGBP\":0.3,\"NEOEUR\":0.3,\"NEOJPY\":0.3,\"NEOGBP\":0.3,\"EOSEUR\":0.3,\"EOSJPY\":0.3,\"EOSGBP\":0.3,\"IOTJPY\":0.3,\"IOTGBP\":0.3,\"DAIUSD\":0.3,\"XLMUSD\":0.5,\"XLMBTC\":0.5,\"XTZUSD\":0.3,\"XTZBTC\":0.3,\"BSVUSD\":0.3,\"BSVUSD_risk\":0.4,\"BSVBTC\":0.3,\"BSVBTC_risk\":0.4,\"USTUSD\":0.3,\"BTCUST\":0.2,\"ETHUST\":0.2,\"LTCUST\":0.2,\"EOSUST\":0.2,\"ATOUSD\":0.5,\"LEOUSD\":0.3,\"LEOUST\":0.3,\"ALGUSD\":0.5,\"ALGUST\":0.5,\"FTTUSD\":0.6,\"XAUT:USD\":0.2,\"XAUT:BTC\":0.2,\"XAUT:UST\":0.2,\"TESTBTC:TESTUSD\":0.3,\"TESTBTC:TESTUSDT\":0.3,\"DOTUSD\":0.3,\"ADAUSD\":0.3,\"ADAUST\":0.3,\"DOTUST\":0.3,\"LINK:USD\":0.3,\"LINK:UST\":0.3,\"UNIUSD\":0.3,\"UNIUST\":0.3,\"YFIUSD\":0.3,\"YFIUST\":0.3,\"FILUSD\":0.3,\"FILUST\":0.3,\"SUSHI:USD\":0.3,\"SUSHI:UST\":0.3,\"DOTBTC\":0.3},\"minimum\":{\"base\":0.15,\"base_cap\":1,\"BTCUSD\":0.1,\"LTCUSD\":0.1,\"LTCBTC\":0.15,\"ETHUSD\":0.1,\"ETHBTC\":0.1,\"ETCBTC\":0.15,\"ETCUSD\":0.15,\"ZECUSD\":0.15,\"ZECBTC\":0.15,\"XMRUSD\":0.15,\"XMRBTC\":0.15,\"DSHUSD\":0.15,\"DSHBTC\":0.15,\"BTCEUR\":0.1,\"BTCJPY\":0.15,\"XRPUSD\":0.1,\"XRPBTC\":0.1,\"IOTUSD\":0.15,\"IOTBTC\":0.15,\"IOTETH\":0.15,\"EOSUSD\":0.1,\"EOSBTC\":0.15,\"EOSETH\":0.15,\"SANUSD\":0.15,\"SANUSD_risk\":0.3,\"SANBTC\":0.15,\"SANBTC_risk\":0.3,\"SANETH\":0.15,\"SANETH_risk\":0.3,\"OMGUSD\":0.15,\"OMGBTC\":0.15,\"OMGETH\":0.15,\"NEOUSD\":0.15,\"NEOBTC\":0.15,\"NEOETH\":0.15,\"ETPUSD\":0.15,\"ETPUSD_risk\":0.3,\"ETPBTC\":0.15,\"ETPBTC_risk\":0.3,\"ETPETH\":0.15,\"ETPETH_risk\":0.3,\"EDOUSD\":0.15,\"EDOUSD_risk\":0.3,\"EDOBTC\":0.15,\"EDOBTC_risk\":0.3,\"EDOETH\":0.15,\"EDOETH_risk\":0.3,\"BTGUSD\":0.15,\"BTGUSD_risk\":0.3,\"BTGBTC\":0.15,\"BTGBTC_risk\":0.3,\"IOTEUR\":0.15,\"ZRXUSD\":0.15,\"ZRXETH\":0.15,\"TRXUSD\":0.15,\"BTCGBP\":0.15,\"ETHEUR\":0.15,\"ETHJPY\":0.15,\"ETHGBP\":0.15,\"NEOEUR\":0.15,\"NEOJPY\":0.15,\"NEOGBP\":0.15,\"EOSEUR\":0.15,\"EOSJPY\":0.15,\"EOSGBP\":0.15,\"IOTJPY\":0.15,\"IOTGBP\":0.15,\"DAIUSD\":0.15,\"XLMUSD\":0.25,\"XLMBTC\":0.25,\"XTZUSD\":0.15,\"XTZBTC\":0.15,\"BSVUSD\":0.15,\"BSVUSD_risk\":0.2,\"BSVBTC\":0.15,\"BSVBTC_risk\":0.2,\"USTUSD\":0.15,\"BTCUST\":0.1,\"ETHUST\":0.1,\"LTCUST\":0.1,\"EOSUST\":0.1,\"ATOUSD\":0.25,\"LEOUSD\":0.15,\"LEOUST\":0.15,\"ALGUSD\":0.25,\"ALGUST\":0.25,\"FTTUSD\":0.3,\"XAUT:USD\":0.1,\"XAUT:BTC\":0.1,\"XAUT:UST\":0.1,\"TESTBTC:TESTUSD\":0.15,\"TESTBTC:TESTUSDT\":0.15,\"DOTUSD\":0.15,\"ADAUSD\":0.15,\"ADAUST\":0.15,\"DOTUST\":0.15,\"LINK:USD\":0.15,\"LINK:UST\":0.15,\"UNIUSD\":0.15,\"UNIUST\":0.15,\"YFIUSD\":0.15,\"YFIUST\":0.15,\"FILUSD\":0.15,\"FILUST\":0.15,\"SUSHI:USD\":0.15,\"SUSHI:UST\":0.15,\"DOTBTC\":0.15}}]"
                  },
                  "pub:info:pair:futures": {
                    "value": "[\n  [\n    [\n      \"AAVEF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ADAF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ALGF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"8.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"APEF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.8\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"APTF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"30000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ARBF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"1.0\",\n        \"75000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ATOF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"AUSTRALIA200IXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0004\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"AVAXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.08\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"AXSF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"BNBF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.004\",\n        \"100.0\",\n        null,\n        null,\n        null,\n        0.05,\n        0.025\n      ]\n    ],\n    [\n      \"BTCDOMF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.006\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"BTCF0:EUTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"2000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"BTCF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"100.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"BVIVF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.05\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.05,\n        0.025\n      ]\n    ],\n    [\n      \"COMPF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"CRVF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"DOGEF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1500000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"DOTF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"EGLDF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"EOSF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ETCF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.1\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ETHF0:BTCF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"100.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ETHF0:EUTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"5000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ETHF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0008\",\n        \"1000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"EURF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"EUROPE50IXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0006\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"EVIVF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.05\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.05,\n        0.025\n      ]\n    ],\n    [\n      \"FILF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"FRANCE40IXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0004\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"FTMF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"GALAF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"44.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"GBPF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"GERMANY40IXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0002\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"HONGKONG50IXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0002\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ICPF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"IOTF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"6.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"JAPAN225IXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.00008\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"JASMYF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"144.0\",\n        \"2500000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"JPYF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"300.0\",\n        \"100000000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"KNCF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"LINKF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"LTCF0:BTCF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"7500.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"LTCF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.04\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"MATICF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"MKRF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"2500.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"NEARF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.4\",\n        \"25000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"NEOF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"OMGF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"SANDF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"SHIBF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"141010.0\",\n        \"5000000000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"SOLF0:BTCF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.05,\n        0.025\n      ]\n    ],\n    [\n      \"SOLF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.05,\n        0.025\n      ]\n    ],\n    [\n      \"SPAIN35IXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0002\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"STGF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"SUSHIF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTADAF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTALGOF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTAPTF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTAVAXF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTBTCF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.00004\",\n        \"1000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTDOGEF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTDOTF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTEOSF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTETHF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTFILF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTLTCF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTMATICF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTNEARF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTSOLF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTXAUTF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TESTXTZF0:TESTUSDTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TRXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"22.0\",\n        \"1000000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"TRYF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"62.0\",\n        \"10000000.0\",\n        null,\n        null,\n        null,\n        0.1,\n        0.05\n      ]\n    ],\n    [\n      \"UK100IXF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.0004\",\n        \"10.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"UKOILF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"UNIF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.2\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"WAVESF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.6\",\n        \"50000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XAGF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.1\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XAUTF0:BTCF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"500.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XAUTF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"400.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XLMF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"14.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XMRF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.02\",\n        \"10000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XPDF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"1000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XPTF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.002\",\n        \"1000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XRPF0:BTCF0\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"250000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XRPF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"4.0\",\n        \"500000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"XTZF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"2.0\",\n        \"100000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ],\n    [\n      \"ZECF0:USTF0\",\n      [\n        null,\n        null,\n        null,\n        \"0.06\",\n        \"20000.0\",\n        null,\n        null,\n        null,\n        0.01,\n        0.005\n      ]\n    ]\n  ]\n]"
                  },
                  "pub:map:currency:tx:fee": {
                    "value": "[\n  [\n    [\"1INCH\",[0,2.2167]],\n    [\"AAA\",[0,0]],\n    [\"AAVE\",[0,0.024124]],\n    [\"ADA\",[0,0.3]],\n    [\"ADD\",[0,0]],\n    [\"ALBT\",[0,18.181]],\n    [\"ALG\",[0,0]],\n    [\"AMP\",[0,6.2763]],\n    [\"ANT\",[0,1.5522]],\n    [\"ATD\",[0,0]],\n    [\"ATO\",[0,0]],\n    [\"AVAX\",[0,0]],\n    [\"B21X\",[0,48.483]],\n    [\"BAL\",[0,0.29189]],\n    [\"BAND\",[0,1.0422]],\n    [\"BAT\",[0,9.8073]],\n    [\"BBB\",[0,0]],\n    [\"BCHABC\",[0,0]],\n    [\"BCHN\",[0,0]],\n    [\"BEST\",[0,5.1628]],\n    [\"BFT\",[0,299.37]],\n    [\"BMI\",[0,9.4487]],\n    [\"BNT\",[0,1.752]],\n    [\"BOSON\",[0,8.0063]],\n    [\"BSV\",[0,0.001]],\n    [\"BTC\",[0,0.0004]],\n    [\"BTG\",[0,0.001]],\n    [\"BTSE\",[0,0]],\n    [\"BTT\",[0,50]],\n    [\"CEL\",[0,0.92338]],\n    [\"CHEX\",[0,0]],\n    [\"CHZ\",[0,22.489]],\n    [\"CLO\",[0,1]],\n    [\"CNHTE\",[0,35.123]],\n    [\"COMP\",[0,0.017492]],\n    [\"CSTBCHABC\",[0,0]],\n    [\"CSTBCHN\",[0,0]],\n    [\"CTK\",[0,0]],\n    [\"DAI\",[0,4.8035]],\n    [\"DAPP\",[0,0]],\n    [\"DAT\",[0,46.244]],\n    [\"DGB\",[0,0.5]],\n    [\"DGX\",[0,0.0026391]],\n    [\"DOG\",[0,0]],\n    [\"DOGE\",[0,0]],\n    [\"DOT\",[0,0]],\n    [\"DSH\",[0,0.002]],\n    [\"DUSK\",[0,48.313]],\n    [\"EDO\",[0,7.6915]],\n    [\"EGLD\",[0,0]],\n    [\"ENJ\",[0,5.3214]],\n    [\"EOS\",[0,0]],\n    [\"EOSDT\",[0,0]],\n    [\"ESS\",[0,2673.7]],\n    [\"ETC\",[0,0.01]],\n    [\"ETH\",[0,0.0026391]],\n    [\"ETH2P\",[0,0]],\n    [\"ETH2R\",[0,0]],\n    [\"ETH2X\",[0,0]],\n    [\"ETP\",[0,0.01]],\n    [\"EUE\",[0,4.6105]],\n    [\"EUS\",[0,4.5665]],\n    [\"EXRD\",[0,49.198]],\n    [\"FET\",[0,26.129]],\n    [\"FIL\",[0,0]],\n    [\"FORTH\",[0,0.26383]],\n    [\"FTM\",[0,0]],\n    [\"FTT\",[0,0.2151]],\n    [\"FUN\",[0,277.01]],\n    [\"GNO\",[0,0.034866]],\n    [\"GNT\",[0,21.178]],\n    [\"GOT\",[0,76.681]],\n    [\"GTX\",[0,1.7196]],\n    [\"HEZ\",[0,1.5295]],\n    [\"ICE\",[0,2.7031]],\n    [\"IDX\",[0,22.945]],\n    [\"IOT\",[0,0.5]],\n    [\"IQX\",[0,10]],\n    [\"JST\",[0,0]],\n    [\"KAN\",[0,2378.4]],\n    [\"KNC\",[0,3.8844]],\n    [\"KSM\",[0,0]],\n    [\"LBT\",[0,0]],\n    [\"LEO\",[0,0]],\n    [\"LES\",[0,0]],\n    [\"LET\",[0,2.2789]],\n    [\"LINK\",[0,0.29151]],\n    [\"LNX\",[0,0.000001]],\n    [\"LRC\",[0,19.476]],\n    [\"LTC\",[0,0.001]],\n    [\"LUNA\",[0,0]],\n    [\"LYM\",[0,611.72]],\n    [\"MKR\",[0,0.0024711]],\n    [\"MLN\",[0,0.081168]],\n    [\"MNA\",[0,10.786]],\n    [\"MOB\",[0,0]],\n    [\"MTO\",[0,3872.9]],\n    [\"NEAR\",[0,0]],\n    [\"NEC\",[0,103.97]],\n    [\"NEO\",[0,0]],\n    [\"NUT\",[0,0]],\n    [\"OCEAN\",[0,12.871]],\n    [\"ODE\",[0,349.7]],\n    [\"OMG\",[0,1.4169]],\n    [\"OMN\",[0,1]],\n    [\"ORS\",[0,1075.4]],\n    [\"OXY\",[0,0]],\n    [\"PANTEOS\",[0,0]],\n    [\"PAS\",[0,1811.8]],\n    [\"PAX\",[0,5.5038]],\n    [\"PBALEOS\",[0,0]],\n    [\"PBANDEOS\",[0,0]],\n    [\"PBATEOS\",[0,0]],\n    [\"PBTCEOS\",[0,0]],\n    [\"PBTCETH\",[0,0.00016001]],\n    [\"PCOMPEOS\",[0,0]],\n    [\"PDAIEOS\",[0,0]],\n    [\"PEOSETH\",[0,1.4354]],\n    [\"PETHEOS\",[0,0]],\n    [\"PLANETS\",[0,0]],\n    [\"PLINKEOS\",[0,0]],\n    [\"PLRCEOS\",[0,0]],\n    [\"PLTCEOS\",[0,0]],\n    [\"PLTCETH\",[0,0.040123]],\n    [\"PLU\",[0,1.1241]],\n    [\"PMKREOS\",[0,0]],\n    [\"PNK\",[0,52.466]],\n    [\"POA\",[0,0.0026391]],\n    [\"POMGEOS\",[0,0]],\n    [\"PPNKEOS\",[0,0]],\n    [\"PPNTEOS\",[0,0]],\n    [\"PREPEOS\",[0,0]],\n    [\"PSNXEOS\",[0,0]],\n    [\"PUNIEOS\",[0,0]],\n    [\"PUOSEOS\",[0,0]],\n    [\"PYFIEOS\",[0,0]],\n    [\"PZRXEOS\",[0,0]],\n    [\"QSH\",[0,91.889]],\n    [\"QTF\",[0,0.97245]],\n    [\"QTM\",[0,0.01]],\n    [\"RBT\",[0,0.001]],\n    [\"REP\",[0,0.40578]],\n    [\"REQ\",[0,105.71]],\n    [\"RINGX\",[0,407.98]],\n    [\"RRB\",[0,5.6021]],\n    [\"SAN\",[0,30.223]],\n    [\"SNG\",[0,678.37]],\n    [\"SNT\",[0,111.79]],\n    [\"SNX\",[0,0.77976]],\n    [\"SOL\",[0,0]],\n    [\"STJ\",[0,7.7428]],\n    [\"SUKU\",[0,23.215]],\n    [\"SUN\",[0,0]],\n    [\"SUSHI\",[0,0.7218]],\n    [\"TESTBTC\",[0,0]],\n    [\"TESTUSD\",[0,0]],\n    [\"TESTUSDT\",[0,0]],\n    [\"TRX\",[0,1]],\n    [\"TSD\",[0,5.5033]],\n    [\"UDC\",[0,5.5038]],\n    [\"UNI\",[0,0.30958]],\n    [\"UOP\",[0,26.929]],\n    [\"UOS\",[0,10.202]],\n    [\"USDTALG\",[0,0]],\n    [\"USDTBCH\",[0,0]],\n    [\"USDTHEZ\",[0,0]],\n    [\"USDTOMG\",[0,0]],\n    [\"USDTSOL\",[0,0]],\n    [\"USE\",[0,5.504]],\n    [\"USK\",[0,0.0026391]],\n    [\"USL\",[0,0]],\n    [\"USO\",[0,5]],\n    [\"USS\",[0,0]],\n    [\"USX\",[0,0]],\n    [\"UTK\",[0,24.919]],\n    [\"VEE\",[0,484.53]],\n    [\"VEN\",[0,0.0026391]],\n    [\"VET\",[0,100]],\n    [\"VSY\",[0,1]],\n    [\"WAX\",[0,3.7504]],\n    [\"WBT\",[0,0.00015814]],\n    [\"XAUTE\",[0,0.0030956]],\n    [\"XCH\",[0,5.0659]],\n    [\"XDC\",[0,0]],\n    [\"XLM\",[0,0]],\n    [\"XMR\",[0,0.0001]],\n    [\"XRA\",[0,313.56]],\n    [\"XRP\",[0,0.1]],\n    [\"XSN\",[0,0]],\n    [\"XTZ\",[0,0.2]],\n    [\"XVG\",[0,0.1]],\n    [\"YFI\",[0,0.00017491]],\n    [\"YGG\",[0,9335]],\n    [\"YYW\",[0,9.3966]],\n    [\"ZBT\",[0,0.0026391]],\n    [\"ZCN\",[0,15.57]],\n    [\"ZEC\",[0,0.003]],\n    [\"ZIL\",[0,27.552]],\n    [\"ZRX\",[0,7.7756]]\n  ]\n]"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "title": "pub:map:currency:sym",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "ABS"
                          }
                        }
                      }
                    },
                    {
                      "title": "pub:list:pair:exchange",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "example": "ABSETH"
                        }
                      }
                    },
                    {
                      "title": "pub:list:currency",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "example": "ABS"
                        }
                      }
                    },
                    {
                      "title": "pub:map:currency:label",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "ABS"
                          }
                        }
                      }
                    },
                    {
                      "title": "pub:map:currency:unit",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "IOT"
                          }
                        }
                      }
                    },
                    {
                      "title": "pub:map:currency:undl",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "USTF0"
                          }
                        }
                      }
                    },
                    {
                      "title": "pub:map:currency:pool",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "SAN"
                          }
                        }
                      }
                    },
                    {
                      "title": "pub:map:currency:explorer",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array"
                        }
                      }
                    },
                    {
                      "title": "pub:list:pair:margin",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "example": "BABBTC"
                        }
                      }
                    },
                    {
                      "title": "pub:info:pair",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array"
                        }
                      }
                    },
                    {
                      "title": "pub:map:currency:pool,pub:map:currency:explorer,pub:map:currency:sym",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "1INCH"
                          }
                        }
                      }
                    },
                    {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "deriv_perp": {
                            "type": "object",
                            "properties": {
                              "correction_clamp_min": {
                                "type": "number",
                                "example": 0.0025,
                                "default": 0
                              },
                              "correction_clamp_insurance": {
                                "type": "number",
                                "example": 0.0015,
                                "default": 0
                              },
                              "correction_slope": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              }
                            }
                          }
                        }
                      }
                    },
                    {
                      "title": "pub:fees",
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "deriv_perp": {
                            "type": "object",
                            "properties": {
                              "correction_clamp_min": {
                                "type": "number",
                                "example": 0.0025,
                                "default": 0
                              },
                              "correction_clamp_insurance": {
                                "type": "number",
                                "example": 0.0015,
                                "default": 0
                              },
                              "correction_slope": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              }
                            }
                          }
                        }
                      }
                    },
                    {
                      "title": "pub:list:competitions",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "example": "plu_diff:1w:tGLOBAL:USD"
                        }
                      }
                    },
                    {
                      "title": "pub:info:tx:status",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array"
                        }
                      }
                    },
                    {
                      "title": "pub:map:tx:method",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array"
                        }
                      }
                    },
                    {
                      "title": "pub:spec:margin",
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "conf": {
                            "type": "object",
                            "properties": {
                              "base_size_thres": {
                                "type": "integer",
                                "example": 0,
                                "default": 0
                              },
                              "base_size_incr": {
                                "type": "integer",
                                "example": 1,
                                "default": 0
                              },
                              "base_step": {
                                "type": "integer",
                                "example": 0,
                                "default": 0
                              },
                              "base_haircut": {
                                "type": "integer",
                                "example": 1,
                                "default": 0
                              },
                              "IOT_haircut": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "SAN_haircut": {
                                "type": "number",
                                "example": 0.001,
                                "default": 0
                              },
                              "OMG_haircut": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "ETP_haircut": {
                                "type": "number",
                                "example": 0.001,
                                "default": 0
                              },
                              "EDO_haircut": {
                                "type": "number",
                                "example": 0.001,
                                "default": 0
                              },
                              "BTG_haircut": {
                                "type": "number",
                                "example": 0.001,
                                "default": 0
                              },
                              "TRX_haircut": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "DAI_haircut": {
                                "type": "number",
                                "example": 0.75,
                                "default": 0
                              },
                              "XLM_haircut": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "XTZ_haircut": {
                                "type": "number",
                                "example": 0.7,
                                "default": 0
                              },
                              "BSV_haircut": {
                                "type": "number",
                                "example": 0.25,
                                "default": 0
                              },
                              "ATO_haircut": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "AMP_haircut": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "ALG_haircut": {
                                "type": "number",
                                "example": 0.25,
                                "default": 0
                              },
                              "FTT_haircut": {
                                "type": "number",
                                "example": 0.001,
                                "default": 0
                              },
                              "DOT_haircut": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ADA_haircut": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "LINK_haircut": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "UNI_haircut": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "YFI_haircut": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "FIL_haircut": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "SUSHI_haircut": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              }
                            }
                          },
                          "initial": {
                            "type": "object",
                            "properties": {
                              "base": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "base_cap": {
                                "type": "integer",
                                "example": 1,
                                "default": 0
                              },
                              "BTCUSD": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "LTCUSD": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "LTCBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETHUSD": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "ETHBTC": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "ETCBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETCUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ZECUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ZECBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "XMRUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "XMRBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "DSHUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "DSHBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BTCEUR": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "BTCJPY": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "XRPUSD": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "XRPBTC": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "IOTUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "IOTBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "IOTETH": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EOSUSD": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "EOSBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EOSETH": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "SANUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "SANUSD_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "SANBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "SANBTC_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "SANETH": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "SANETH_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "OMGUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "OMGBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "OMGETH": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "NEOUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "NEOBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "NEOETH": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETPUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETPUSD_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "ETPBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETPBTC_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "ETPETH": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETPETH_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "EDOUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EDOUSD_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "EDOBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EDOBTC_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "EDOETH": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EDOETH_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "BTGUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BTGUSD_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "BTGBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BTGBTC_risk": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "IOTEUR": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ZRXUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ZRXETH": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "TRXUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BTCGBP": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETHEUR": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETHJPY": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETHGBP": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "NEOEUR": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "NEOJPY": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "NEOGBP": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EOSEUR": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EOSJPY": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EOSGBP": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "IOTJPY": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "IOTGBP": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "DAIUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "XLMUSD": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "XLMBTC": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "XTZUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "XTZBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BSVUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BSVUSD_risk": {
                                "type": "number",
                                "example": 0.4,
                                "default": 0
                              },
                              "BSVBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BSVBTC_risk": {
                                "type": "number",
                                "example": 0.4,
                                "default": 0
                              },
                              "USTUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BTCUST": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "ETHUST": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "LTCUST": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "EOSUST": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "ATOUSD": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "LEOUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "LEOUST": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ALGUSD": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "ALGUST": {
                                "type": "number",
                                "example": 0.5,
                                "default": 0
                              },
                              "FTTUSD": {
                                "type": "number",
                                "example": 0.6,
                                "default": 0
                              },
                              "XAUT:USD": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "XAUT:BTC": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "XAUT:UST": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "TESTBTC:TESTUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "TESTBTC:TESTUSDT": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "DOTUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ADAUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ADAUST": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "DOTUST": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "LINK:USD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "LINK:UST": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "UNIUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "UNIUST": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "YFIUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "YFIUST": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "FILUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "FILUST": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "SUSHI:USD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "SUSHI:UST": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "DOTBTC": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              }
                            }
                          },
                          "minimum": {
                            "type": "object",
                            "properties": {
                              "base": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "base_cap": {
                                "type": "integer",
                                "example": 1,
                                "default": 0
                              },
                              "BTCUSD": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "LTCUSD": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "LTCBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ETHUSD": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "ETHBTC": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "ETCBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ETCUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ZECUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ZECBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "XMRUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "XMRBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "DSHUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "DSHBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "BTCEUR": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "BTCJPY": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "XRPUSD": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "XRPBTC": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "IOTUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "IOTBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "IOTETH": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "EOSUSD": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "EOSBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "EOSETH": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "SANUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "SANUSD_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "SANBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "SANBTC_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "SANETH": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "SANETH_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "OMGUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "OMGBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "OMGETH": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "NEOUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "NEOBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "NEOETH": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ETPUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ETPUSD_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETPBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ETPBTC_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "ETPETH": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ETPETH_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EDOUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "EDOUSD_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EDOBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "EDOBTC_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "EDOETH": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "EDOETH_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BTGUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "BTGUSD_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "BTGBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "BTGBTC_risk": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "IOTEUR": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ZRXUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ZRXETH": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "TRXUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "BTCGBP": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ETHEUR": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ETHJPY": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ETHGBP": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "NEOEUR": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "NEOJPY": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "NEOGBP": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "EOSEUR": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "EOSJPY": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "EOSGBP": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "IOTJPY": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "IOTGBP": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "DAIUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "XLMUSD": {
                                "type": "number",
                                "example": 0.25,
                                "default": 0
                              },
                              "XLMBTC": {
                                "type": "number",
                                "example": 0.25,
                                "default": 0
                              },
                              "XTZUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "XTZBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "BSVUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "BSVUSD_risk": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "BSVBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "BSVBTC_risk": {
                                "type": "number",
                                "example": 0.2,
                                "default": 0
                              },
                              "USTUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "BTCUST": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "ETHUST": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "LTCUST": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "EOSUST": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "ATOUSD": {
                                "type": "number",
                                "example": 0.25,
                                "default": 0
                              },
                              "LEOUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "LEOUST": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ALGUSD": {
                                "type": "number",
                                "example": 0.25,
                                "default": 0
                              },
                              "ALGUST": {
                                "type": "number",
                                "example": 0.25,
                                "default": 0
                              },
                              "FTTUSD": {
                                "type": "number",
                                "example": 0.3,
                                "default": 0
                              },
                              "XAUT:USD": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "XAUT:BTC": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "XAUT:UST": {
                                "type": "number",
                                "example": 0.1,
                                "default": 0
                              },
                              "TESTBTC:TESTUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "TESTBTC:TESTUSDT": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "DOTUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ADAUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "ADAUST": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "DOTUST": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "LINK:USD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "LINK:UST": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "UNIUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "UNIUST": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "YFIUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "YFIUST": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "FILUSD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "FILUST": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "SUSHI:USD": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "SUSHI:UST": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              },
                              "DOTBTC": {
                                "type": "number",
                                "example": 0.15,
                                "default": 0
                              }
                            }
                          }
                        }
                      }
                    },
                    {
                      "title": "pub:info:pair:futures",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array"
                        }
                      }
                    },
                    {
                      "title": "pub:map:currency:tx:fee",
                      "type": "array",
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "array"
                        }
                      }
                    }
                  ]
                }
              },
              "text/plain": {
                "examples": {
                  "pub:list:pair:securities": {
                    "value": "[\n    [\n        \"BMNBTC\", \n        \"BMNUSD\", \n        \"EXOUSD\"\n    ]\n ]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "example": "BMNBTC"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "no result available": {
                    "value": "// If a bad request is performed, e.g. if incorrect params are sent, then an array containing null will be returned.\n[\n    null\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {}
                }
              }
            }
          }
        },
        "security": [],
        "x-readme": {
          "code-samples": [
            {
              "language": "javascript",
              "code": "const axios = require('axios')\n\nconst baseUrl = \"https://api-pub.bitfinex.com/v2/\";\n\nfunction request(pathParams){\n    axios.get(`${baseUrl}/conf/${pathParams}`)\n    .then(response => {\n        console.log(response.data);\n    }, error => {\n        console.log(error);\n    })\n}"
            }
          ],
          "samples-languages": [
            "javascript"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```
