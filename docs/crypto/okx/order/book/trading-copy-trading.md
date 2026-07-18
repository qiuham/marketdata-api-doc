---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading
anchor_id: order-book-trading-copy-trading
api_type: API
updated_at: 2026-07-18 20:03:49.438794
---

# Copy Trading

Lead trading API Workflow as follows:  
  
  
  
**1\. Apply to become a leading trader.**

  * The procedure can refer to [How to become a lead trader](https://www.okx.com/help/11639154398221);  

  * You can know whether you are a lead trader by checking whether `roleType` or `spotRoleType` from [Get account configuration](/docs-v5/en/#trading-account-rest-api-get-account-configuration) is 1.

**2\. Leading instruments:**

  * [GET / Leading instruments](/docs-v5/en/#order-book-trading-copy-trading-get-leading-instruments) can get instruments that are supported to have leading trades and the instruments that you enable leading trade. For instruments that are disenabled copy trading, you can still trade normally, but copy trading will not be triggered;  

  * [Amend leading instruments](/docs-v5/en/#order-book-trading-copy-trading-amend-leading-instruments) can amend your leading instruments. You need to set initial leading instruments while applying to become a leading trader. All non-leading contracts can't have position or pending orders for the current request when setting non-leading contracts as leading contracts.  

**3\. Open position:**

  * You can open the position by placing order endpoints and channels including [Place order](/docs-v5/en/#order-book-trading-trade-post-place-order) endpoint, [Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders) endpoint, [Place order channel](/docs-v5/en/#order-book-trading-trade-ws-place-order), [Place multiple orders channel](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders), `tdMode` should be `spot_isolated` for `SPOT` lead trading.   

  * For buy/sell mode, the orders must be in the same direction as your existing positions and open orders. You can select the direction you want if the instrument does not have position and pending orders.
  * For long/short mode, you can open long or open short as you want.

**4\. Close position**

  * You can close the position with customized price or size by placing order endpoints and channels including [Place order](/docs-v5/en/#order-book-trading-trade-post-place-order) endpoint, [Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders) endpoint, [Place order channel](/docs-v5/en/#order-book-trading-trade-ws-place-order), [Place multiple orders channel](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders), or close the position by [Close positions](/docs-v5/en/#order-book-trading-trade-post-close-positions) / [Close lead position](/docs-v5/en/#order-book-trading-copy-trading-post-close-lead-position);  

  * [Close positions](/docs-v5/en/#order-book-trading-trade-post-close-positions) can close certain position under the current instrument(e.g. the long or short position under long/shor mode ), which can contain multiple leading positions;  

  * [Close lead position](/docs-v5/en/#order-book-trading-copy-trading-post-close-lead-position) can only close a leading position once a time. It is required to pass subPosId which can get from [Get existing leading positions](/docs-v5/en/#order-book-trading-copy-trading-get-existing-lead-positions).

**5\. TP/SL**

  * TP/SL can be set by [Place algo order](/docs-v5/en/#order-book-trading-trade-ws-mass-cancel-order) or [Place lead stop order](/docs-v5/en/#order-book-trading-copy-trading-post-place-lead-stop-order);  

  * [Place algo order](/docs-v5/en/#order-book-trading-trade-ws-mass-cancel-order) can set TP/SL for certain position under the current instrument(e.g. the long or short position under long/shor mode ), which can contain multiple leading positions;  

  * [Place lead stop order](/docs-v5/en/#order-book-trading-copy-trading-post-place-lead-stop-order) set set TP/SL for only a leading position once a time. It is required to pass subPosId which can get from [Get existing leading positions](/docs-v5/en/#order-book-trading-copy-trading-get-existing-lead-positions).

### GET / Existing lead positions

Retrieve lead positions that are not closed.  

Returns reverse chronological order with `openTime`

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/current-subpositions`

> Request example
    
    
    GET /api/v5/copytrading/current-subpositions?instId=BTC-USDT-SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
It returns all types by default.  
instId | String | No | Instrument ID, e.g. BTC-USDT-SWAP  
after | String | No | Pagination of data to return records earlier than the requested `subPosId`.  
before | String | No | Pagination of data to return records newer than the requested `subPosId`.  
limit | String | No | Number of results per request. Maximum is 500. Default is 500.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "",
                "ccy": "USDT",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "12.6417",
                "markPx": "38205.8",
                "mgnMode": "isolated",
                "openAvgPx": "37925.1",
                "openOrdId": "",
                "openTime": "1701231120479",
                "posSide": "net",
                "slOrdPx": "",
                "slTriggerPx": "",
                "subPos": "1",
                "subPosId": "649945658862370816",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0.2807",
                "uplRatio": "0.0222042921442527",
                "availSubPos": "1"
            },
            {
                "algoId": "",
                "ccy": "USDT",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "12.6263333333333333",
                "markPx": "38205.8",
                "mgnMode": "isolated",
                "openAvgPx": "37879",
                "openOrdId": "",
                "openTime": "1701225074786",
                "posSide": "net",
                "slOrdPx": "",
                "slTriggerPx": "",
                "subPos": "1",
                "subPosId": "649920301388038144",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0.3268",
                "uplRatio": "0.0258824150584758",
                "availSubPos": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
subPosId | String | Lead position ID  
posSide | String | Position side  
`long`   
`short`   
`net`  
(Long positions have positive subPos; short positions have negative subPos)  
mgnMode | String | Margin mode. `cross` `isolated`  
lever | String | Leverage  
openOrdId | String | Order ID for opening position, only applicable to lead position  
openAvgPx | String | Average open price  
openTime | String | Open time  
subPos | String | Quantity of positions  
tpTriggerPx | String | Take-profit trigger price.  
slTriggerPx | String | Stop-loss trigger price.  
algoId | String | Stop order ID  
instType | String | Instrument type  
tpOrdPx | String | Take-profit order price, it is -1 for market price  
slOrdPx | String | Stop-loss order price, it is -1 for market price  
margin | String | Margin  
upl | String | Unrealized profit and loss  
uplRatio | String | Unrealized profit and loss ratio  
markPx | String | Latest mark price, only applicable to contract  
uniqueCode | String | Lead trader unique code  
ccy | String | Margin currency  
availSubPos | String | Quantity of positions that can be closed  
  
### GET / Lead position history

Retrieve the completed lead position of the last 3 months.  
Returns reverse chronological order with `subPosId`. 

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/subpositions-history`

> Request example
    
    
    GET /api/v5/copytrading/subpositions-history?instId=BTC-USDT-SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
It returns all types by default.  
instId | String | No | Instrument ID, e.g. BTC-USDT-SWAP  
after | String | No | Pagination of data to return records earlier than the requested `subPosId`.  
before | String | No | Pagination of data to return records newer than the requested `subPosId`.  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "closeAvgPx": "37617.5",
                "closeTime": "1701188587950",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "37.41",
                "markPx": "38203.4",
                "mgnMode": "isolated",
                "openAvgPx": "37410",
                "openOrdId": "",
                "openTime": "1701184638702",
                "pnl": "0.6225",
                "pnlRatio": "0.0166399358460306",
                "posSide": "net",
                "profitSharingAmt": "0.0407967",
                "subPos": "3",
                "closeSubPos": "2",
                "type": "1",
                "subPosId": "649750700213698561",
                "uniqueCode": "25CD5A80241D6FE6"
            },
            {
                "ccy": "USDT",
                "closeAvgPx": "37617.5",
                "closeTime": "1701188587950",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "24.94",
                "markPx": "38203.4",
                "mgnMode": "isolated",
                "openAvgPx": "37410",
                "openOrdId": "",
                "openTime": "1701184635381",
                "pnl": "0.415",
                "pnlRatio": "0.0166399358460306",
                "posSide": "net",
                "profitSharingAmt": "0.0271978",
                "subPos": "2",
                "closeSubPos": "2",
                "type": "2",
                "subPosId": "649750686292803585",
                "uniqueCode": "25CD5A80241D6FE6"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
subPosId | String | Lead position ID  
posSide | String | Position side  
`long`   
`short`   
`net`  
(long position has positive subPos; short position has negative subPos)  
mgnMode | String | Margin mode. `cross` `isolated`  
lever | String | Leverage  
openOrdId | String | Order ID for opening position, only applicable to lead position  
openAvgPx | String | Average open price  
openTime | String | Time of opening  
subPos | String | Quantity of positions  
closeTime | String | Time of closing position  
closeAvgPx | String | Average price of closing position  
pnl | String | Profit and loss  
pnlRatio | String | P&L ratio  
instType | String | Instrument type  
margin | String | Margin  
ccy | String | Currency  
markPx | String | Latest mark price, only applicable to contract  
uniqueCode | String | Lead trader unique code  
profitSharingAmt | String | Profit sharing amount, only applicable to copy trading. Note: this parameter is already deprecated.  
closeSubPos | String | Quantity of positions that is already closed  
type | String | The type of closing position  
`1`：Close position partially;  
`2`：Close all  
  
### POST / Place lead stop order

Set TP/SL for the current lead position that are not closed.

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/copytrading/algo-order`

> Request example
    
    
    POST /api/v5/copytrading/algo-order
    body
    {
        "subPosId": "518541406042591232",
        "tpTriggerPx": "10000"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`, the default value  
subPosId | String | Yes | Lead position ID  
tpTriggerPx | String | Conditional | Take-profit trigger price. Take-profit order price will be the market price after triggering. At least one of tpTriggerPx and slTriggerPx must be filled  
The take profit order will be deleted if it is 0  
slTriggerPx | String | Conditional | Stop-loss trigger price. Stop-loss order price will be the market price after triggering. The stop loss order will be deleted if it is 0  
tpOrdPx | String | No | Take-profit order price  
If the price is -1, take-profit will be executed at the market price, the default is `-1`  
Only applicable to `SPOT` lead trader  
slOrdPx | String | No | Stop-loss order price  
If the price is -1, stop-loss will be executed at the market price, the default is `-1`  
Only applicable to `SPOT` lead trader  
tpTriggerPxType | String | No | Take-profit trigger price type   
  
`last`: last price  
`index`: index price  
`mark`: mark price   
Default is `last`  
slTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
Default is last  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "subPosId": "518560559046594560",
                "tag":""
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
subPosId | String | Lead position ID  
tag | String | Order tag  
  
### POST / Close lead position

You can only close a lead position once a time.   
It is required to pass subPosId which can get from [Get existing leading positions](/docs-v5/en/#order-book-trading-copy-trading-get-existing-lead-positions).

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/close-subposition`

> Request example
    
    
    POST /api/v5/copytrading/close-subposition
    body
    {
        "subPosId": "518541406042591232",
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`, the default value  
subPosId | String | Yes | Lead position ID  
ordType | String | No | Order type  
`market`：Market order, the default value  
`limit`：Limit order  
  
px | String | No | Order price. Only applicable to `limit` order and `SPOT` lead trader   
If the price is 0, the pending order will be canceled.   
It is modifying order if you set `px` after placing limit order.  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "subPosId": "518560559046594560",
                "tag":""
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
subPosId | String | Lead position ID  
tag | String | Order tag  
  
### GET / Leading instruments

Retrieve instruments that are supported to lead by the platform. Retrieve instruments that the lead trader has set.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/instruments`

> Request example
    
    
    GET /api/v5/copytrading/instruments
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`, the default value  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "enabled": true,
                "instId": "BTC-USDT-SWAP"
            },
            {
                "enabled": true,
                "instId": "ETH-USDT-SWAP"
            },
            {
                "enabled": false,
                "instId": "ADA-USDT-SWAP"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
enabled | Boolean | Whether instrument is a lead instrument. `true` or `false`  
  
### POST / Amend leading instruments

The leading trader can amend current leading instruments, need to set initial leading instruments while applying to become a leading trader.  
All non-leading instruments can't have position or pending orders for the current request when setting non-leading instruments as leading instruments.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/set-instruments`

> Request example
    
    
    POST /api/v5/copytrading/set-instruments
    body
    {
        "instId": "BTC-USDT-SWAP,ETH-USDT-SWAP"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`, the default value  
instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP. If there are multiple instruments, separate them with commas.  
The value of `instId` must include all instruments that you are going to have the lead trading with because the previous settings will be overwritten after the current request is set successfully  

> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "enabled": true,
                "instId": "BTC-USDT-SWAP"
            },
            {
                "enabled": true,
                "instId": "ETH-USDT-SWAP"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
enabled | Boolean | Whether you set it successfully  
`true` or `false`  
  
### GET / Profit sharing details

The leading trader gets profits shared details for the last 3 months.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/profit-sharing-details`

> Request example
    
    
    GET /api/v5/copytrading/profit-sharing-details?limit=2
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
It returns all types by default.  
after | String | No | Pagination of data to return records earlier than the requested `profitSharingId`  
before | String | No | Pagination of data to return records newer than the requested `profitSharingId`  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "nickName": "Potato",
                "profitSharingAmt": "0.00536",
                "profitSharingId": "148",
                "portLink": "",
                "ts": "1723392000000",
                "instType": "SWAP"
            },
            {
                "ccy": "USDT",
                "nickName": "Apple",
                "profitSharingAmt": "0.00336",
                "profitSharingId": "20",
                "portLink": "",
                "ts": "1723392000000",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | The currency of profit sharing.  
profitSharingAmt | String | Profit sharing amount. It would be 0 if there is no any profit sharing.  
nickName | String | Nickname of copy trader.  
profitSharingId | String | Profit sharing ID.  
instType | String | Instrument type  
portLink | String | Portrait link  
ts | String | Profit sharing time.  
  
### GET / Total profit sharing

The leading trader gets the total amount of profit shared since joining the platform.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/total-profit-sharing`

> Request example
    
    
    GET /api/v5/copytrading/total-profit-sharing
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
It returns all types by default.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "totalProfitSharingAmt": "0.6584928",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | The currency of profit sharing.  
totalProfitSharingAmt | String | Total profit sharing amount.  
instType | String | Instrument type  
  
### GET / Unrealized profit sharing details

The leading trader gets the profit sharing details that are expected to be shared in the next settlement cycle.  
The unrealized profit sharing details will update once there copy position is closed.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/unrealized-profit-sharing-details`

> Request example
    
    
    GET /api/v5/copytrading/unrealized-profit-sharing-details
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
It returns all types by default.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "nickName": "Potato",
                "portLink": "",
                "ts": "1669901824779",
                "unrealizedProfitSharingAmt": "0.455472",
                "instType": "SWAP"
            },
            {
                "ccy": "USDT",
                "nickName": "Apple",
                "portLink": "",
                "ts": "1669460210113",
                "unrealizedProfitSharingAmt": "0.033608",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | The currency of profit sharing. e.g. USDT  
unrealizedProfitSharingAmt | String | Unrealized profit sharing amount.  
nickName | String | Nickname of copy trader.  
instType | String | Instrument type  
portLink | String | Portrait link  
ts | String | Update time.  
  
### GET / Total unrealized profit sharing

The leading trader gets the total unrealized amount of profit shared.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/total-unrealized-profit-sharing`

> Request example
    
    
    GET /api/v5/copytrading/total-unrealized-profit-sharing
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "profitSharingTs": "1705852800000",
                "totalUnrealizedProfitSharingAmt": "0.114402985553185"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
profitSharingTs | String | The settlement time for the total unrealized profit sharing amount. Unix timestamp format in milliseconds, e.g.1597026383085  
totalUnrealizedProfitSharingAmt | String | Total unrealized profit sharing amount  
  
### POST / Amend profit sharing ratio

It is used to amend profit sharing ratio. 

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/amend-profit-sharing-ratio`

> Request example
    
    
    POST /api/v5/copytrading/amend-profit-sharing-ratio
    body
    {
        "instType": "SWAP",
        "profitSharingRatio": "0.1"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`  
profitSharingRatio | String | Yes | Profit sharing ratio.   
0.1 represents 10%  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
result | Boolean | The result of setting   
`true`  
  
### GET / Account configuration

Retrieve current account configuration related to copy/lead trading.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/config`

> Request example
    
    
    GET /api/v5/copytrading/config
    
    

#### Request Parameters

None

> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "copyTraderNum": "1",
                        "instType": "SWAP",
                        "maxCopyTraderNum": "100",
                        "profitSharingRatio": "0",
                        "roleType": "1"
                    },
                    {
                        "copyTraderNum": "",
                        "instType": "SPOT",
                        "maxCopyTraderNum": "",
                        "profitSharingRatio": "",
                        "roleType": "0"
                    }
                ],
                "nickName": "155***9957",
                "portLink": "",
                "uniqueCode": "5506D3681454A304"
            }
        ],
        "msg": ""
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
uniqueCode | String | User unique code  
nickName | String | Nickname  
portLink | String | Portrait link  
details | Array of objects | Details  
> instType | String | Instrument type  
`SPOT`  
`SWAP`  
> roleType | String | Role type  
`0`: General user  
`1`: Leading trader  
`2`: Copy trader  
> profitSharingRatio | String | Profit sharing ratio.   
Only applicable to lead trader, or it will be "". 0.1 represents 10%  
> maxCopyTraderNum | String | Maximum number of copy traders  
> copyTraderNum | String | Current number of copy traders  
  
### POST / First copy settings

The first copy settings for the certain lead trader. You need to first copy settings after stopping copying.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/first-copy-settings`

> Request example
    
    
    POST /api/v5/copytrading/first-copy-settings
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "copyMgnMode": "cross",
        "copyInstIdType": "copy",
        "copyMode": "ratio_copy",
        "copyRatio": "1",
        "copyTotalAmt": "500",
        "subPosCloseType": "copy_close"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
copyMgnMode | String | Yes | Copy margin mode  
`cross`: cross  
`isolated`: isolated  
`copy`: Use the same margin mode as lead trader when opening positions  
copyInstIdType | String | Yes | Copy contract type setted  
`custom`: custom by `instId` which is required；  
`copy`: Keep your contracts consistent with this trader by automatically adding or removing contracts when they do  
instId | String | Conditional | Instrument ID.   
If there are multiple instruments, separate them with commas.  
copyMode | String | No | Copy mode  
`fixed_amount`: set the same fixed amount for each order, and `copyAmt` is required；  
`ratio_copy`: set amount as a multiple of the lead trader’s order value, and `copyRatio` is required   
The default is `fixed_amount`  
copyTotalAmt | String | Yes | Maximum total amount in USDT.   
The maximum total amount you'll invest at any given time across all orders in this copy trade  
You won’t copy new orders if you exceed this amount  
copyAmt | String | Conditional | Copy amount per order in USDT.  
copyRatio | String | Conditional | Copy ratio per order.  
tpRatio | String | No | Take profit per order. 0.1 represents 10%  
slRatio | String | No | Stop loss per order. 0.1 represents 10%  
slTotalAmt | String | No | Total stop loss in USDT for trader.   
If your net loss (total profit - total loss) reaches this amount, you'll stop copying this trader  
subPosCloseType | String | Yes | Action type for open positions  
`market_close`: immediately close at market price  
`copy_close`：close when trader closes  
`manual_close`: close manually  
The default is `copy_close`  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
result | Boolean | The result of setting   
`true`  
  
### POST / Amend copy settings

You need to use this endpoint to amend copy settings

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/amend-copy-settings`

> Request example
    
    
    POST /api/v5/copytrading/amend-copy-settings
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "copyMgnMode": "cross",
        "copyInstIdType": "copy",
        "copyMode": "ratio_copy",
        "copyRatio": "1",
        "copyTotalAmt": "500",
        "subPosCloseType": "copy_close"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
copyMgnMode | String | Yes | Copy margin mode  
`cross`: cross  
`isolated`: isolated  
`copy`: Use the same margin mode as lead trader when opening positions  
copyInstIdType | String | Yes | Copy contract type setted  
`custom`: custom by `instId` which is required；  
`copy`: Keep your contracts consistent with this trader by automatically adding or removing contracts when they do  
instId | String | Conditional | Instrument ID.   
If there are multiple instruments, separate them with commas.  
copyMode | String | No | Copy mode  
`fixed_amount`: set the same fixed amount for each order, and `copyAmt` is required；  
`ratio_copy`: set amount as a multiple of the lead trader’s order value, and `copyRatio` is required   
The default is `fixed_amount`  
copyTotalAmt | String | Yes | Maximum total amount in USDT.   
The maximum total amount you'll invest at any given time across all orders in this copy trade  
You won’t copy new orders if you exceed this amount  
copyAmt | String | Conditional | Copy amount per order in USDT  
copyRatio | String | Conditional | Copy ratio per order.  
tpRatio | String | No | Take profit per order. 0.1 represents 10%  
slRatio | String | No | Stop loss per order. 0.1 represents 10%  
slTotalAmt | String | No | Total stop loss in USDT for trader.  
If your net loss (total profit - total loss) reaches this amount, you'll stop copying this trader  
subPosCloseType | String | Yes | Action type for open positions  
`market_close`: immediately close at market price  
`copy_close`：close when trader closes  
`manual_close`: close manually  
The default is `copy_close`  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
result | Boolean | The result of setting   
`true`  
  
### POST / Stop copying

You need to use this endpoint to stop copy trading

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/stop-copy-trading`

> Request example
    
    
    POST /api/v5/copytrading/stop-copy-trading
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "subPosCloseType": "manual_close"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
subPosCloseType | String | Yes | Action type for open positions, it is required if you have related copy position  
`market_close`: immediately close at market price  
`copy_close`：close when trader closes  
`manual_close`: close manually  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
result | Boolean | The result of setting   
`true`  
  
### GET / Copy settings

Retrieve the copy settings about certain lead trader.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/copy-settings`

> Request example
    
    
    GET /api/v5/copytrading/copy-settings?instType=SWAP&uniqueCode=25CD5A80241D6FE6
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "copyAmt": "",
                "copyInstIdType": "copy",
                "copyMgnMode": "isolated",
                "copyMode": "ratio_copy",
                "copyRatio": "1",
                "copyState": "1",
                "copyTotalAmt": "500",
                "instIds": [
                    {
                        "enabled": "1",
                        "instId": "ADA-USDT-SWAP"
                    },
                    {
                        "enabled": "1",
                        "instId": "YFII-USDT-SWAP"
                    }
                ],
                "slRatio": "",
                "slTotalAmt": "",
                "subPosCloseType": "copy_close",
                "tpRatio": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
copyMode | String | Copy mode  
`fixed_amount` `ratio_copy`  
copyAmt | String | Copy amount in USDT per order.  
copyRatio | String | Copy ratio per order.  
copyTotalAmt | String | Maximum total amount in USDT.   
The maximum total amount you'll invest at any given time across all orders in this copy trade  
tpRatio | String | Take profit per order. 0.1 represents 10%  
slRatio | String | Stop loss per order. 0.1 represents 10%  
copyInstIdType | String | Copy contract type setted  
`custom`: custom by `instId` which is required；  
`copy`: Keep your contracts consistent with this trader by automatically adding or removing contracts when they do  
instIds | Array of objects | Instrument list. It will return all lead contracts of the lead trader  
> instId | String | Instrument ID  
> enabled | String | Whether copying this `instId`  
`0` `1`  
slTotalAmt | String | Total stop loss in USDT for trader.  
subPosCloseType | String | Action type for open positions  
`market_close`: immediately close at market price  
`copy_close`：close when trader closes  
`manual_close`: close manually  
copyMgnMode | String | Copy margin mode  
`cross`: cross  
`isolated`: isolated  
`copy`: Use the same margin mode as lead trader when opening positions  
ccy | String | Margin currency  
copyState | String | Current copy state   
`0`: non-copy, `1`: copy  
tag | String | Order tag  
  
### GET / My lead traders

Retrieve my lead traders.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/current-lead-traders`

> Request example
    
    
    GET /api/v5/copytrading/current-lead-traders?instType=SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "beginCopyTime": "1701224821936",
                "ccy": "USDT",
                "copyTotalAmt": "500",
                "copyTotalPnl": "0",
                "leadMode": "public",
                "margin": "1.89395",
                "nickName": "Trader9527",
                "portLink": "",
                "profitSharingRatio": "0.08",
                "todayPnl": "0",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
portLink | String | Portrait link  
nickName | String | Nick name  
margin | String | Margin for copy trading  
copyTotalAmt | String | Copy total amount  
copyTotalPnl | String | Copy total pnl  
uniqueCode | String | Lead trader unique code  
ccy | String | margin currency  
profitSharingRatio | String | Profit sharing ratio. 0.1 represents 10%  
beginCopyTime | String | Begin copying time. Unix timestamp format in milliseconds, e.g.1597026383085  
upl | String | Unrealized profit & loss  
todayPnl | String | Today pnl  
leadMode | String | Lead mode `public` `private`  
  
### GET / Copy trading configuration

Public endpoint. Retrieve copy trading parameter configuration information of copy settings

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-config`

> Request example
    
    
    GET /api/v5/copytrading/public-config?instType=SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "maxCopyAmt": "1000",
                "maxCopyRatio": "100",
                "maxCopyTotalAmt": "30000",
                "maxSlRatio": "0.75",
                "maxTpRatio": "1.5",
                "minCopyAmt": "20",
                "minCopyRatio": "0.01"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
maxCopyAmt | String | Maximum copy amount per order in USDT when you are using copy mode `fixed_amount`  
minCopyAmt | String | Minimum copy amount per order in USDT when you are using copy mode `fixed_amount`  
maxCopyTotalAmt | String | Maximum copy total amount under the certain lead trader, the minimum is the same with `minCopyAmt`  
minCopyRatio | String | Minimum ratio per order when you are using copy mode `ratio_copy`  
maxCopyRatio | String | Maximum ratio per order when you are using copy mode `ratio_copy`  
maxTpRatio | String | Maximum ratio of taking profit per order, the minimum is 0  
maxSlRatio | String | Maximum ratio of stopping loss per order, the minimum is 0  
  
### GET / Lead trader ranks

Public endpoint. Retrieve lead trader ranks.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-lead-traders`

> Request example
    
    
    GET /api/v5/copytrading/public-lead-traders?instType=SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
sortType | String | No | Sort type  
`overview`: overview, the default value  
`pnl`: profit and loss  
`aum`: assets under management  
`win_ratio`: win ratio  
`pnl_ratio`: pnl ratio  
`current_copy_trader_pnl`: current copy trader pnl  
state | String | No | Lead trader state  
`0`: All lead traders, the default, including vacancy and non-vacancy   
`1`: lead traders who have vacancy  
minLeadDays | String | No | Minimum lead days  
`1`: 7 days  
`2`: 30 days  
`3`: 90 days  
`4`: 180 days  
minAssets | String | No | Minimum assets in USDT  
maxAssets | String | No | Maximum assets in USDT  
minAum | String | No | Minimum assets in USDT under management.  
maxAum | String | No | Maximum assets in USDT under management.  
dataVer | String | No | Data version. It is 14 numbers. e.g. 20231010182400. Generally, it is used for pagination   
A new version will be generated every 10 minutes. Only last 5 versions are stored  
The default is latest version. If it is not exist, error will not be throwed and the latest version will be used.  
page | String | No | Page for pagination  
limit | String | No | Number of results per request. The maximum is 20; the default is 10  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "dataVer": "20231129213200",
                "ranks": [
                    {
                        "accCopyTraderNum": "3536",
                        "aum": "1509265.3238761567721365",
                        "ccy": "USDT",
                        "copyState": "0",
                        "copyTraderNum": "999",
                        "leadDays": "156",
                        "maxCopyTraderNum": "1000",
                        "nickName": "Crypto to the moon",
                        "pnl": "48805.1105999999972258",
                        "pnlRatio": "1.6898",
                        "pnlRatios": [
                            {
                                "beginTs": "1701187200000",
                                "pnlRatio": "1.6744"
                            },
                            {
                                "beginTs": "1700755200000",
                                "pnlRatio": "1.649"
                            }
                        ],
                        "portLink": "https://static.okx.com/cdn/okex/users/headimages/20230624/f49a683aaf5949ea88b01bbc771fb9fc",
                        "traderInsts": [
                            "ICP-USDT-SWAP",
                            "MINA-USDT-SWAP"
    
                        ],
                        "uniqueCode": "540D011FDACCB47A",
                        "winRatio": "0.6957"
                    }
                ],
                "totalPage": "1"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
dataVer | String | Data version  
totalPage | String | Total number of pages  
ranks | Array of objects | The rank information of lead traders  
> aum | String | assets under management  
> copyState | String | Current copy state   
`0`: non-copy, `1`: copy  
> maxCopyTraderNum | String | Maximum number of copy traders  
> copyTraderNum | String | Current number of copy traders  
> accCopyTraderNum | String | Accumulated number of copy traders  
> portLink | String | Portrait link  
> nickName | String | Nick name  
> ccy | String | Margin currency  
> uniqueCode | String | Lead trader unique code  
> winRatio | String | Win ratio, 0.1 represents 10%  
> leadDays | String | Lead days  
> traderInsts | Array of strings | Contract list which lead trader is leading  
> pnl | String | Pnl (in USDT) of last 90 days.  
> pnlRatio | String | Pnl ratio of last 90 days. 0.1 represents 10%  
> pnlRatios | Array of objects | Pnl ratios  
>> beginTs | String | Begin time of pnl ratio on that day  
>> pnlRatio | String | Pnl ratio on that day  
  
### GET / Lead trader weekly pnl

Public endpoint. Retrieve lead trader weekly pnl. Results are returned in counter chronological order.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-weekly-pnl`

> Request example
    
    
    GET /api/v5/copytrading/public-weekly-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "beginTs": "1701014400000",
                "pnl": "-2.8428",
                "pnlRatio": "-0.0106"
            },
            {
                "beginTs": "1700409600000",
                "pnl": "81.8446",
                "pnlRatio": "0.3036"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
beginTs | String | Begin time of pnl ratio on that week  
pnl | String | Pnl on that week  
pnlRatio | String | Pnl ratio on that week  
  
### GET / Lead trader daily pnl

Public endpoint. Retrieve lead trader daily pnl. Results are returned in counter chronological order.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-pnl`

> Request example
    
    
    GET /api/v5/copytrading/public-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
lastDays | String | Yes | Last days  
`1`: last 7 days   
`2`: last 30 days  
`3`: last 90 days   
`4`: last 365 days  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "beginTs": "1701100800000",
                "pnl": "97.3309",
                "pnlRatio": "0.3672"
            },
            {
                "beginTs": "1701014400000",
                "pnl": "96.7755",
                "pnlRatio": "0.3651"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
beginTs | String | Begin time on that day  
pnl | String | Accumulated pnl  
pnlRatio | String | Accumulated pnl ratio  
  
### GET / Lead trader stats

Public endpoint. Key data related to lead trader performance.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-stats`

> Request example
    
    
    GET /api/v5/copytrading/public-stats?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
lastDays | String | Yes | Last days  
`1`: last 7 days   
`2`: last 30 days  
`3`: last 90 days   
`4`: last 365 days  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "avgSubPosNotional": "213.1038",
                "ccy": "USDT",
                "curCopyTraderPnl": "96.8071",
                "investAmt": "265.095252476476294",
                "lossDays": "1",
                "profitDays": "2",
                "winRatio": "0.6667"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
winRatio | String | Win ratio  
profitDays | String | Profit days  
lossDays | String | Loss days  
curCopyTraderPnl | String | Current copy trader pnl (USDT)  
avgSubPosNotional | String | Average lead position notional (USDT)  
investAmt | String | Investment amount (USDT)  
ccy | String | Margin currency  
  
### GET / Lead trader currency preferences

Public endpoint. The most frequently traded crypto of this lead trader. Results are sorted by ratio from large to small.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-preference-currency`

> Request example
    
    
    GET /api/v5/copytrading/public-preference-currency?instType=SWAP&uniqueCode=CB4594A3BB5D3538
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "ETH",
                "ratio": "0.8881"
            },
            {
                "ccy": "BTC",
                "ratio": "0.0666"
            },
            {
                "ccy": "YFII",
                "ratio": "0.0453"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency  
ratio | String | Ratio. 0.1 represents 10%  
  
### GET / Lead trader current lead positions

Public endpoint. Get current leading positions of lead trader

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-current-subpositions`

> Request example
    
    
    GET /api/v5/copytrading/public-current-subpositions?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value.  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
after | String | No | Pagination of data to return records earlier than the requested `subPosId`.  
before | String | No | Pagination of data to return records newer than the requested `subPosId`.  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "lever": "5",
                "margin": "16.23304",
                "markPx": "2027.31",
                "mgnMode": "isolated",
                "openAvgPx": "2029.13",
                "openTime": "1701144639417",
                "posSide": "short",
                "subPos": "4",
                "subPosId": "649582930998104064",
                "uniqueCode": "D9ADEAB33AE9EABD",
                "upl": "0.0728",
                "uplRatio": "0.0044846806266725"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
subPosId | String | Lead position ID  
posSide | String | Position side  
`long`   
`short`   
`net`  
(Long positions have positive subPos; short positions have negative subPos)  
mgnMode | String | Margin mode. `cross` `isolated`  
lever | String | Leverage  
openAvgPx | String | Average open price  
openTime | String | Open time  
subPos | String | Quantity of positions  
instType | String | Instrument type  
margin | String | Margin  
upl | String | Unrealized profit and loss  
uplRatio | String | Unrealized profit and loss ratio  
markPx | String | Latest mark price, only applicable to contract  
uniqueCode | String | Lead trader unique code  
ccy | String | Currency  
  
### GET / Lead trader lead position history

Public endpoint. Retrieve the lead trader completed leading position of the last 3 months.  
Returns reverse chronological order with `subPosId`. 

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-subpositions-history`

> Request example
    
    
    GET /api/v5/copytrading/public-subpositions-history?instType=SWAP&uniqueCode=9A8534AB09862774
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value.  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
after | String | No | Pagination of data to return records earlier than the requested `subPosId`.  
before | String | No | Pagination of data to return records newer than the requested `subPosId`.  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "closeAvgPx": "28385.9",
                "closeTime": "1697709137162",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "20",
                "margin": "4.245285",
                "mgnMode": "isolated",
                "openAvgPx": "28301.9",
                "openTime": "1697698048031",
                "pnl": "0.252",
                "pnlRatio": "0.05935997229868",
                "posSide": "long",
                "subPos": "3",
                "subPosId": "635126416883355648",
                "uniqueCode": "9A8534AB09862774"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
subPosId | String | Lead position ID  
posSide | String | Position side  
`long`   
`short`   
`net`  
(long position has positive subPos; short position has negative subPos)  
mgnMode | String | Margin mode. `cross` `isolated`  
lever | String | Leverage  
openAvgPx | String | Average open price  
openTime | String | Time of opening  
subPos | String | Quantity of positions  
closeTime | String | Time of closing position  
closeAvgPx | String | Average price of closing position  
pnl | String | Profit and loss  
pnlRatio | String | P&L ratio  
instType | String | Instrument type  
margin | String | Margin  
ccy | String | Currency  
uniqueCode | String | Lead trader unique code  
  
### GET / Copy traders

Public endpoint. Retrieve copy trader coming from certain lead trader. Return according to `pnl` from high to low

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-copy-traders`

> Request example
    
    
    GET /api/v5/copytrading/public-copy-traders?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "copyTotalPnl": "2060.12242",
                "copyTraderNumChg": "1",
                "copyTraderNumChgRatio": "0.5",
                "copyTraders": [
                    {
                        "beginCopyTime": "1686125051000",
                        "nickName": "bre***@gmail.com",
                        "pnl": "1076.77388",
                        "portLink": ""
                    },
                    {
                        "beginCopyTime": "1698133811000",
                        "nickName": "MrYanDao505",
                        "pnl": "983.34854",
                        "portLink": "https://static.okx.com/cdn/okex/users/headimages/20231010/fd31f45e99fe41f7bb219c0b53ae0ada"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
copyTotalPnl | String | Total copy trader profit and loss  
ccy | String | The currency name of profit and loss  
copyTraderNumChg | String | Number change in last 7 days  
copyTraderNumChgRatio | String | Ratio change in last 7 days  
copyTraders | Array of objects | Copy trader information  
> beginCopyTime | String | Begin copying time. Unix timestamp format in milliseconds, e.g.1597026383085  
> nickName | String | Nick name  
> portLink | String | Copy trader portrait link  
> pnl | String | Copy trading profit and loss  
  
### WS / Lead trading notification channel

The notification when failing to lead trade.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "copytrading-lead-notification",
            "instType": "SWAP"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "copytrading-lead-notification",
            "instType": "SWAP"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`copytrading-lead-notification`  
> instType | String | Yes | Instrument type  
`SWAP`  
> instId | String | No | Instrument ID  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "copytrading-lead-notification",
            "instType": "SWAP"
        },
        "connId": "aa993428"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"copytrading-lead-notification\", \"instType\" : \"FUTURES\"}]}",
      "connId":"a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> instType | String | Yes | Instrument type  
`SWAP`  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: 
    
    
    {
        "arg": {
            "channel": "copytrading-lead-notification",
            "instType": "SWAP",
            "uid": "525627088439549953"
        },
        "data": [
            {
                "infoType": "2",
                "instId": "",
                "instType": "SWAP",
                "maxLeadTraderNum": "3",
                "minLeadEq": "",
                "posSide": "",
                "side": "",
                "subPosId": "667695035433385984",
                "uniqueCode": "3AF72F63E3EAD701"
            }
        ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> instType | String | Instrument type  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> infoType | String | Information type  
`1`: lead trading failed due to touch max position limitation   
`2`: lead trading failed due to touch the maximum daily number of lead trading   
`3`: lead trading failed due to your USDT equity less than the minimum USDT equity of lead trading  
> subPosId | String | Lead position ID  
> uniqueCode | String | Lead trader unique code  
> instId | String | Instrument ID  
> side | String | Side `buy` `sell`  
> posSide | String | Position side   
`long`  
`short`  
`net`  
> maxLeadTraderNum | String | Maximum daily number of lead trading.  
> minLeadEq | String | Minimum USDT equity of lead trading.

---

# 跟单

带单 API 交易工作流程如下：  
  
  
  
**1\. 申请成为带单交易员**  

  * 申请流程可以参考 [如何申请成为交易员](https://www.okx.com/cn/help/11639154398221)；  

  * 可通过[查看账户配置](/docs-v5/zh/#trading-account-rest-api-get-account-configuration)接口的`roleType` 或者 `spotRoleType` 是否为 1，判断当前账户是否为带单交易员。  

**2\. 带单合约**  

  * [获取带单产品](/docs-v5/zh/#order-book-trading-copy-trading-get-leading-instruments)接口，用于查看平台哪些合约支持带单，以及您开启了哪些合约的带单。对于您未开启带单的合约，依旧可以正常交易，只是不会触发跟单；  

  * [交易员修改带单合约](/docs-v5/zh/#order-book-trading-copy-trading-post-amend-leading-instruments)接口，初始带单合约在申请带单交易员时进行设置，该接口用于修改您的带单合约。非带单合约修改为带单合约时，该次请求中所有的非带单合约合约不能有持仓或者挂单。  

**3\. 开仓**

  * 需要通过下单接口和频道进行开仓，包括：[下单](/docs-v5/zh/#order-book-trading-trade-post-place-order)接口、[批量下单](/docs-v5/zh/#order-book-trading-trade-post-place-multiple-orders)接口、[下单频道](/docs-v5/zh/#order-book-trading-trade-ws-place-order)、[批量下单频道](/docs-v5/zh/#order-book-trading-trade-ws-place-multiple-orders)。现货带单时，`tdMode` 的值需要指定为`spot_isolated`
  * 在买卖模式下，委托的方向必须与现有持仓和挂单保持一致，如果对应产品没有持仓和挂单，可根据自己的需求选择委托方向；
  * 开平仓模式下，可根据自己的需求选择开多或开空。

**4\. 平仓**

  * 可以通过下单接口和频道进行平仓，支持自定义价格和数量，包括：[下单](/docs-v5/zh/#order-book-trading-trade-post-place-order)接口、[批量下单](/docs-v5/zh/#order-book-trading-trade-post-place-multiple-orders)接口、[下单频道](/docs-v5/zh/#order-book-trading-trade-ws-place-order)、[批量下单频道](/docs-v5/zh/#order-book-trading-trade-ws-place-multiple-orders)，也可以通过[市价仓位全平](/docs-v5/zh/#order-book-trading-trade-post-close-positions)接口或者[平仓带单](/docs-v5/zh/#order-book-trading-copy-trading-post-close-lead-position)接口进行平仓；
  * [市价仓位全平](/docs-v5/zh/#order-book-trading-trade-post-close-positions)接口，平掉当前产品下指定的仓位（如：开平模式下，全仓模式下的多仓或空仓），可能包含多个带单；
  * [平仓带单](/docs-v5/zh/#order-book-trading-copy-trading-post-close-lead-position)接口，一次仅平仓某一个带单仓位。带单ID（subPosId）为必填参数，需要通过[获取当前带单](/docs-v5/zh/#order-book-trading-copy-trading-get-existing-lead-positions)接口获取。

**5\. 止盈止损**

  * 可以通过[带单仓位止盈止损](/docs-v5/zh/#order-book-trading-copy-trading-post-place-lead-stop-order)接口或者[策略委托下单](/docs-v5/zh/#order-book-trading-algo-trading-post-place-algo-order)接口设置止盈止损；
  * [ 带单仓位止盈止损](/docs-v5/zh/#order-book-trading-copy-trading-post-place-lead-stop-order)接口，一次仅为一个带单仓位设置。带单ID（subPosId）为必填参数，需要通过[获取当前带单](/docs-v5/zh/#order-book-trading-copy-trading-get-existing-lead-positions)接口获取。
  * [策略委托下单](/docs-v5/zh/#order-book-trading-algo-trading-post-place-algo-order)接口，为当前产品下指定的仓位（如：开平模式下，全仓模式下的多仓或空仓）设置，可能包含多个带单；

### GET / 获取当前带单 

获取当前未平仓的带单仓位。  

按照开仓时间倒序排列。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/current-subpositions`

> 请求示例
    
    
    GET /api/v5/copytrading/current-subpositions?instId=BTC-USDT-SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约  
默认返回所有业务线的信息  
instId | String | 否 | 产品ID ，如`BTC-USDT-SWAP`  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`subPosId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`subPosId`  
limit | String | 否 | 分页返回的结果集数量，最大为500，不填默认返回500条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "",
                "ccy": "USDT",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "12.6417",
                "markPx": "38205.8",
                "mgnMode": "isolated",
                "openAvgPx": "37925.1",
                "openOrdId": "",
                "openTime": "1701231120479",
                "posSide": "net",
                "slOrdPx": "",
                "slTriggerPx": "",
                "subPos": "1",
                "subPosId": "649945658862370816",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0.2807",
                "uplRatio": "0.0222042921442527",
                "availSubPos": "1"
            },
            {
                "algoId": "",
                "ccy": "USDT",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "12.6263333333333333",
                "markPx": "38205.8",
                "mgnMode": "isolated",
                "openAvgPx": "37879",
                "openOrdId": "",
                "openTime": "1701225074786",
                "posSide": "net",
                "slOrdPx": "",
                "slTriggerPx": "",
                "subPos": "1",
                "subPosId": "649920301388038144",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0.3268",
                "uplRatio": "0.0258824150584758",
                "availSubPos": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
subPosId | String | 带单仓位ID  
posSide | String | 持仓方向  
long：开平仓模式开多   
short：开平仓模式开空   
net：买卖模式（subPos为正代表开多，subPos为负代表开空）  
mgnMode | String | 保证金模式，`isolated`：逐仓 ；`cross`：全仓  
lever | String | 杠杆倍数  
openOrdId | String | 交易员开仓订单号，仅适用于带单仓位  
openAvgPx | String | 开仓均价  
openTime | String | 开仓时间  
subPos | String | 持仓张数  
tpTriggerPx | String | 止盈触发价  
slTriggerPx | String | 止损触发价  
algoId | String | 止盈止损委托单ID  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
tpOrdPx | String | 止盈委托价，市价时为-1  
slOrdPx | String | 止损委托价，市价时为-1  
margin | String | 保证金  
upl | String | 未实现收益  
uplRatio | String | 未实现收益率  
markPx | String | 最新标记价格，仅适用于合约  
uniqueCode | String | 交易员唯一标识代码  
ccy | String | 保证金币种  
availSubPos | String | 可平张数/币数  
  
### GET / 获取历史带单 

获取最近三个月的已经平仓的带单仓位，按照`subPosId`倒序排序。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/subpositions-history`

> 请求示例
    
    
    GET /api/v5/copytrading/subpositions-history?instId=BTC-USDT-SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约  
默认返回所有业务线的信息  
instId | String | 否 | 产品ID ，如`BTC-USDT-SWAP`  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`subPosId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`subPosId`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "closeAvgPx": "37617.5",
                "closeTime": "1701188587950",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "37.41",
                "markPx": "38203.4",
                "mgnMode": "isolated",
                "openAvgPx": "37410",
                "openOrdId": "",
                "openTime": "1701184638702",
                "pnl": "0.6225",
                "pnlRatio": "0.0166399358460306",
                "posSide": "net",
                "profitSharingAmt": "0.0407967",
                "subPos": "3",
                "closeSubPos": "2",
                "type": "1",
                "subPosId": "649750700213698561",
                "uniqueCode": "25CD5A80241D6FE6"
            },
            {
                "ccy": "USDT",
                "closeAvgPx": "37617.5",
                "closeTime": "1701188587950",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "24.94",
                "markPx": "38203.4",
                "mgnMode": "isolated",
                "openAvgPx": "37410",
                "openOrdId": "",
                "openTime": "1701184635381",
                "pnl": "0.415",
                "pnlRatio": "0.0166399358460306",
                "posSide": "net",
                "profitSharingAmt": "0.0271978",
                "subPos": "2",
                "closeSubPos": "2",
                "type": "2",
                "subPosId": "649750686292803585",
                "uniqueCode": "25CD5A80241D6FE6"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
subPosId | String | 带单仓位ID  
posSide | String | 持仓方向  
long：开平仓模式开多   
short：开平仓模式开空   
net：买卖模式（subPos为正代表开多，subPos为负代表开空）  
mgnMode | String | 保证金模式，`isolated`：逐仓 ；`cross`：全仓  
lever | String | 杠杆倍数  
openOrdId | String | 交易员开仓订单号，仅适用于带单仓位  
openAvgPx | String | 开仓均价  
openTime | String | 开仓时间  
subPos | String | 持仓张数  
closeTime | String | 平仓时间(最近一次平仓的时间)  
closeAvgPx | String | 平仓均价  
pnl | String | 收益额  
pnlRatio | String | 收益率  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
margin | String | 保证金  
ccy | String | 币种  
markPx | String | 最新标记价格，仅适用于合约  
uniqueCode | String | 交易员唯一标识代码  
profitSharingAmt | String | 跟单分润额，仅适用于跟单，已经废弃。  
closeSubPos | String | 已平仓量  
type | String | 平仓类型  
`1`：部分平仓;  
`2`：完全平仓;  
  
### POST / 带单或跟单仓位止盈止损 

为当前未平仓的带单仓位设置止盈止损。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/algo-order`

> 请求示例
    
    
    POST /api/v5/copytrading/algo-order
    body
    {
        "subPosId": "518541406042591232",
        "tpTriggerPx": "10000"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约，默认值  
subPosId | String | 是 | 带单或者跟单仓位ID  
tpTriggerPx | String | 可选 | 止盈触发价，tpTriggerPx 和 slTriggerPx 至少需要填写一个  
如果止盈触发价为0，那代表删除止盈。  
slTriggerPx | String | 可选 | 止损触发价，  
如果止损触发价为0，那代表删除止损  
tpOrdPx | String | 否 | 止盈委托价  
委托价格为-1时，执行市价止盈，默认为市价止盈  
仅适用于现货交易员  
slOrdPx | String | 否 | 止损委托价  
委托价格为-1时，执行市价止损，默认为市价止损  
仅适用于现货交易员  
tpTriggerPxType | String | 否 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为last  
slTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为last  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
subPosType | String | 否 | 数据的类型  
`lead`: 带单，默认值  
`copy`: 跟单  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "subPosId": "518560559046594560",
                "tag":""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subPosId | String | 带单或者跟单仓位ID  
tag | String | 订单标签  
  
### POST / 平仓带单 

一次仅可平仓一个带单仓位。  
`subPosId` 为必填参数，需要通过[交易员获取当前带单](/docs-v5/zh/#order-book-trading-copy-trading-get-existing-lead-positions)接口获取。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/close-subposition`

> 请求示例
    
    
    POST /api/v5/copytrading/close-subposition
    body
    {
        "subPosId": "518541406042591232"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约，默认值  
subPosId | String | 是 | 带单仓位ID  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
ordType | String | 否 | 订单类型  
`market`：市价单  
`limit`：限价单  
默认为市价单  
px | String | 否 | 委托价格，仅适用于`limit`类型的订单，且仅适用于现货交易员  
委托价格为 0 代表撤销挂单  
已经设置了限价单，仍为该条目设置价格时，视为改单。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "subPosId": "518560559046594560",
                "tag":""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subPosId | String | 带单仓位ID  
tag | String | 订单标签  
  
### GET / 获取带单产品 

获取平台支持带单的产品，以及获取带单员正在带单的产品

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/instruments`

> 请求示例
    
    
    GET /api/v5/copytrading/instruments
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约，默认值  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "enabled": true,
                "instId": "BTC-USDT-SWAP"
            },
            {
                "enabled": true,
                "instId": "ETH-USDT-SWAP"
            },
            {
                "enabled": false,
                "instId": "ADA-USDT-SWAP"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
enabled | Boolean | 是否设置了带单 `true` 或 `false`  
  
### POST / 交易员修改带单产品 

交易员修改带单产品的设置。初始带单产品在申请带单交易员时进行设置。  
非带单产品修改为带单产品时，该次请求中所有的非带单产品不能有持仓或者挂单。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/set-instruments`

> 请求示例
    
    
    POST /api/v5/copytrading/set-instruments
    body
    {
        "instId": "BTC-USDT-SWAP,ETH-USDT-SWAP"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约，默认值  
instId | String | 是 | 产品ID，如 BTC-USDT-SWAP，多个产品用半角逗号隔开  
如果进行多个产品带单，`instId`传值需要包括所有将要带单的产品，因为当前请求设置成功后，之前的设置会被覆盖掉  

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "enabled": true,
                "instId": "BTC-USDT-SWAP"
            },
            {
                "enabled": true,
                "instId": "ETH-USDT-SWAP"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品id， 如 BTC-USDT-SWAP  
enabled | Boolean | `true` 或 `false`  
`true` 代表设置成功  
`false` 代表设置失败  
  
### GET / 交易员历史分润明细 

交易员获取最近三个月的分润明细。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/profit-sharing-details`

> 请求示例
    
    
    GET /api/v5/copytrading/profit-sharing-details?limit=2
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约  
默认返回所有业务线的信息  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`profitSharingId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`profitSharingId`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "nickName": "Potato",
                "profitSharingAmt": "0.00536",
                "profitSharingId": "148",
                "portLink": "",
                "ts": "1723392000000",
                "instType": "SWAP"
            },
            {
                "ccy": "USDT",
                "nickName": "Apple",
                "profitSharingAmt": "0.00336",
                "profitSharingId": "20",
                "portLink": "",
                "ts": "1723392000000",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 分润币种  
profitSharingAmt | String | 分润额，没有分润时，默认返回0  
nickName | String | 跟单人的昵称  
profitSharingId | String | 分润ID  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
portLink | String | 跟单员头像的链接地址  
ts | String | 分润时间  
  
### GET / 交易员历史分润汇总 

交易员获取自入驻平台以来，累计获得的总分润金额。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/total-profit-sharing`

> 请求示例
    
    
    GET /api/v5/copytrading/total-profit-sharing
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约  
默认返回所有业务线的信息  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "totalProfitSharingAmt": "0.6584928",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 分润币种  
totalProfitSharingAmt | String | 历史分润汇总  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
  
### GET / 交易员待分润明细 

交易员获取预计在下一个周期分到的分润金额明细。  
当有跟单仓位平仓时，待分润明细会进行更新。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/unrealized-profit-sharing-details`

> 请求示例
    
    
    GET /api/v5/copytrading/unrealized-profit-sharing-details
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约  
默认返回所有业务线的信息  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "nickName": "Potato",
                "portLink": "",
                "ts": "1669901824779",
                "unrealizedProfitSharingAmt": "0.455472",
                "instType": "SWAP"
            },
            {
                "ccy": "USDT",
                "nickName": "Apple",
                "portLink": "",
                "ts": "1669460210113",
                "unrealizedProfitSharingAmt": "0.033608",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 分润币种，如：`USDT`  
unrealizedProfitSharingAmt | String | 待分润额  
nickName | String | 跟单人昵称  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
portLink | String | 跟单员头像的链接地址  
ts | String | 数据更新时间  
  
### GET / 交易员待分润汇总 

交易员获取待分润汇总。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/total-unrealized-profit-sharing`

> 请求示例
    
    
    GET /api/v5/copytrading/total-unrealized-profit-sharing
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SWAP：永续合约，默认值  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "profitSharingTs": "1705852800000",
                "totalUnrealizedProfitSharingAmt": "0.114402985553185"
            }
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
profitSharingTs | String | 当前周期待分润总额的结算时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
totalUnrealizedProfitSharingAmt | String | 待分润总额  
  
### POST / 修改分润比例 

修改分润比例

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/amend-profit-sharing-ratio`

> 请求示例
    
    
    POST /api/v5/copytrading/amend-profit-sharing-ratio
    body
    {
        "instType": "SWAP",
        "profitSharingRatio": "0.1"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
profitSharingRatio | String | 是 | 分润比例。0.1 代表10%  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
result | Boolean | 设置结果  
`true`：设置成功  
  
### GET / 查看账户配置信息 

获取跟单交易和带单交易相关的账户配置信息

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/config`

> 请求示例
    
    
    GET /api/v5/copytrading/config
    
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "copyTraderNum": "1",
                        "instType": "SWAP",
                        "maxCopyTraderNum": "100",
                        "profitSharingRatio": "0",
                        "roleType": "1"
                    },
                    {
                        "copyTraderNum": "",
                        "instType": "SPOT",
                        "maxCopyTraderNum": "",
                        "profitSharingRatio": "",
                        "roleType": "0"
                    }
                ],
                "nickName": "155***9957",
                "portLink": "",
                "uniqueCode": "5506D3681454A304"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
uniqueCode | String | 交易员唯一标识代码  
nickName | String | 昵称  
portLink | String | 头像的链接地址  
details | Array of objects | 详情  
> instType | String | 产品类型  
`SPOT`: 币币  
`SWAP`: 永续合约  
> roleType | String | 用户角色  
`0`：普通用户  
`1`：带单者  
`2`：跟单者  
> profitSharingRatio | String | 分润比例，仅适用于带单员，0.1 代表 10%，否则为""  
> maxCopyTraderNum | String | 最大跟单人数，仅适用于带单员  
> copyTraderNum | String | 当前跟单人数，仅适用于带单员  
  
### POST / 首次跟单设置 

跟随某一交易员的首次设置，停止跟单后需先进行首次设置；  

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/first-copy-settings`

> 请求示例
    
    
    POST /api/v5/copytrading/first-copy-settings
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "copyMgnMode": "cross",
        "copyInstIdType": "copy",
        "copyMode": "ratio_copy",
        "copyRatio": "1",
        "copyTotalAmt": "500",
        "subPosCloseType": "copy_close"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
copyMgnMode | String | 是 | 跟单时的保证金模式  
`cross`: 全仓；  
`isolated`: 逐仓；  
`copy`: 跟随带单员  
copyInstIdType | String | 是 | 跟单合约设置的类型  
`custom`: 用户自定义，instId 必填；  
`copy`: 跟随交易员，自动同步交易员的合约变更  
instId | String | 可选 | 产品 ID  
可传入多条，以逗号区分  
copyMode | String | 否 | 跟单模式  
`fixed_amount`: 固定金额跟单，`copyAmt`必填；  
`ratio_copy`: 比例跟单，`copyRatio`必填   
默认是`fixed_amount`  
copyTotalAmt | String | 是 | 跟单该交易员投入的最大跟单金额，单位为USDT。  
超过该金额后将不再触发跟单行为  
copyAmt | String | 可选 | 单笔跟随金额，单位为USDT  
copyRatio | String | 可选 | 跟单比例  
tpRatio | String | 否 | 单笔止盈百分比，0.1 代表10%  
slRatio | String | 否 | 单笔止损百分比，0.1 代表10%  
slTotalAmt | String | 否 | 跟单止损总金额，单位为USDT  
净损失达到该金额时，将自动解除跟单关系  
subPosCloseType | String | 是 | 剩余仓位处理方式  
`market_close`: 立即市价全平  
`copy_close`：跟随交易员平仓  
`manual_close`: 手动处理  
默认为 `copy_close`  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
result | Boolean | 设置结果  
`true`：设置成功  
  
### POST / 修改跟单设置 

跟随某一交易员，完成首次设置后，修改设置时，需要使用该接口  

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/amend-copy-settings`

> 请求示例
    
    
    POST /api/v5/copytrading/amend-copy-settings
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "copyMgnMode": "cross",
        "copyInstIdType": "copy",
        "copyMode": "ratio_copy",
        "copyRatio": "1",
        "copyTotalAmt": "500",
        "subPosCloseType": "copy_close"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
copyMgnMode | String | 是 | 跟单时的保证金模式  
`cross`: 全仓；  
`isolated`: 逐仓；  
`copy`: 跟随带单员  
copyInstIdType | String | 是 | 跟单合约设置的类型  
`custom`: 用户自定义，instId 必填；  
`copy`: 跟随交易员，自动同步交易员的合约变更  
instId | String | 可选 | 产品 ID  
可传入多条，以逗号区分  
copyMode | String | 否 | 跟单模式  
`fixed_amount`: 固定金额跟单，`copyAmt`必填；  
`ratio_copy`: 比例跟单，`copyRatio`必填   
默认是`fixed_amount`  
copyTotalAmt | String | 是 | 跟单该交易员投入的最大跟单金额，单位为USDT。  
超过该金额后将不再触发跟单行为  
copyAmt | String | 可选 | 单笔跟随金额，单位为USDT  
copyRatio | String | 可选 | 跟单比例  
tpRatio | String | 否 | 单笔止盈百分比，0.1 代表10%  
slRatio | String | 否 | 单笔止损百分比，0.1 代表10%  
slTotalAmt | String | 否 | 跟单止损总金额，单位为USDT  
净损失达到该金额时，将自动解除跟单关系  
subPosCloseType | String | 是 | 剩余仓位处理方式  
`market_close`: 立即市价全平  
`copy_close`：跟随交易员平仓  
`manual_close`: 手动处理  
默认为 `copy_close`  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
result | Boolean | 设置结果  
`true`：设置成功  
  
### POST / 停止跟单 

该接口用来停止跟单  

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/stop-copy-trading`

> 请求示例
    
    
    POST /api/v5/copytrading/stop-copy-trading
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "subPosCloseType": "manual_close"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
subPosCloseType | String | 可选 | 剩余仓位处理方式，有相关的跟单条目时必填  
`market_close`: 立即市价全平  
`copy_close`：跟随交易员平仓  
`manual_close`: 手动处理  
  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
result | Boolean | 设置结果  
`true`：设置成功  
  
### GET / 获取跟单设置 

获取针对某个交易员的跟单设置

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/copy-settings`

> 请求示例
    
    
    GET /api/v5/copytrading/copy-settings?instType=SWAP&uniqueCode=25CD5A80241D6FE6
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "copyAmt": "",
                "copyInstIdType": "copy",
                "copyMgnMode": "isolated",
                "copyMode": "ratio_copy",
                "copyRatio": "1",
                "copyState": "1",
                "copyTotalAmt": "500",
                "instIds": [
                    {
                        "enabled": "1",
                        "instId": "ADA-USDT-SWAP"
                    },
                    {
                        "enabled": "1",
                        "instId": "YFII-USDT-SWAP"
                    }
                ],
                "slRatio": "",
                "slTotalAmt": "",
                "subPosCloseType": "copy_close",
                "tpRatio": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
copyMode | String | 跟单模式  
`fixed_amount`: 固定金额跟单  
`ratio_copy`: 比例跟单  
copyAmt | String | 单笔跟随金额，单位为 USDT  
copyRatio | String | 跟单比例  
copyTotalAmt | String | 跟单该交易员投入的最大跟单金额，单位为USDT  
tpRatio | String | 单笔止盈百分比，0.1 代表10%  
slRatio | String | 单笔止损百分比，0.1 代表10%  
copyInstIdType | String | 跟单合约设置的类型  
`custom`: 用户自定义   
`copy`: 跟随交易员，自动同步交易员的合约变更  
instIds | Array of objects | 可跟单的合约列表，会返回交易员所有带单合约  
> instId | String | 产品 ID  
> enabled | String | 是否在跟单  
`0`: 没有在跟单 `1`: 在跟单  
slTotalAmt | String | 跟单止损总金额，单位为 USDT  
subPosCloseType | String | 剩余仓位处理方式  
`market_close`: 立即市价全平  
`copy_close`：跟随交易员平仓  
`manual_close`: 手动处理  
copyMgnMode | String | 跟单时的保证金模式  
`cross`: 全仓；  
`isolated`: 逐仓；  
`copy`: 跟随带单员  
ccy | String | 保证金币种  
copyState | String | 当前跟单状态   
`0`: 没在跟单  
`1`：在跟单  
tag | String | 订单标签  
  
### GET / 获取我的交易员 

获取当前跟随的交易员

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/copytrading/current-lead-traders`

> 请求示例
    
    
    GET /api/v5/copytrading/current-lead-traders?instType=SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "beginCopyTime": "1701224821936",
                "ccy": "USDT",
                "copyTotalAmt": "500",
                "copyTotalPnl": "0",
                "leadMode": "public",
                "margin": "1.89395",
                "nickName": "Trader9527",
                "portLink": "",
                "profitSharingRatio": "0.08",
                "todayPnl": "0",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
portLink | String | 头像  
nickName | String | 昵称  
margin | String | 跟单交易占用的保证金  
copyTotalAmt | String | 跟单员设置的跟单总金额  
copyTotalPnl | String | 跟单总收益 (USDT)  
uniqueCode | String | 带单员唯一标识代码  
ccy | String | 保证金币种  
profitSharingRatio | String | 分润比例，0.1 代表 10%  
beginCopyTime | String | 跟单开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
upl | String | 未实现盈亏  
todayPnl | String | 今日已实现收益  
leadMode | String | 带单模式  
`public`: 公开模式  
`private`: 私域模式  
  
### GET / 获取跟单配置信息 

公共接口，获取跟单设置时的参数配置信息

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-config`

> 请求示例
    
    
    GET /api/v5/copytrading/public-config?instType=SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "maxCopyAmt": "1000",
                "maxCopyRatio": "100",
                "maxCopyTotalAmt": "30000",
                "maxSlRatio": "0.75",
                "maxTpRatio": "1.5",
                "minCopyAmt": "20",
                "minCopyRatio": "0.01"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
maxCopyAmt | String | 固定金额跟单时，单笔最大跟随金额  
minCopyAmt | String | 固定金额跟单时，单笔最小跟随金额  
maxCopyTotalAmt | String | 最大跟单金额（针对单个带单员），最小跟单金额同`minCopyAmt`  
minCopyRatio | String | 比例跟单的单笔最小比率  
maxCopyRatio | String | 比例跟单的单笔最大比率  
maxTpRatio | String | 单笔最大止盈比率，最小为 0  
maxSlRatio | String | 单笔最大止损比率，最小为 0  
  
### GET / 获取交易员排名 

公共接口，获取交易员排名信息。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-lead-traders`

> 请求示例
    
    
    GET /api/v5/copytrading/public-lead-traders?instType=SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
sortType | String | 否 | 排名类型  
`overview`: 综合排序，默认值  
`pnl`: 按照交易员收益额排序  
`aum`: 按照带单规模排序  
`win_ratio`: 胜率  
`pnl_ratio`: 收益率  
`current_copy_trader_pnl`: 当前跟单人的收益额  
state | String | 否 | 交易员的状态  
`0`: 所有交易员，默认值，包括有空缺和没有空缺   
`1`: 有空缺的交易员  
minLeadDays | String | 否 | 最短带单时长  
`1`: 7 天  
`2`: 30 天  
`3`: 90 天  
`4`: 180天  
minAssets | String | 否 | 交易员资产范围的最小值，单位为 USDT  
maxAssets | String | 否 | 交易员资产范围的最大值，单位为 USDT  
minAum | String | 否 | 带单规模的最小值，单位为 USDT  
maxAum | String | 否 | 带单规模的最大值，单位为 USDT  
dataVer | String | 否 | 排名数据的版本，14 位数字，如：20231010182400，主要在分页时使用   
每10分钟生成一版，仅保留最新的5个版本  
默认使用最近的版本；不存在时不会报错，会使用最近的版本。  
page | String | 否 | 查询页数  
limit | String | 否 | 分页返回的结果集数量，最大为 20，不填默认返回 10 条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "dataVer": "20231129213200",
                "ranks": [
                    {
                        "accCopyTraderNum": "3536",
                        "aum": "1509265.3238761567721365",
                        "ccy": "USDT",
                        "copyState": "0",
                        "copyTraderNum": "999",
                        "leadDays": "156",
                        "maxCopyTraderNum": "1000",
                        "nickName": "Crypto to the moon",
                        "pnl": "48805.1105999999972258",
                        "pnlRatio": "1.6898",
                        "pnlRatios": [
                            {
                                "beginTs": "1701187200000",
                                "pnlRatio": "1.6744"
                            },
                            {
                                "beginTs": "1700755200000",
                                "pnlRatio": "1.649"
                            }
                        ],
                        "portLink": "https://static.okx.com/cdn/okex/users/headimages/20230624/f49a683aaf5949ea88b01bbc771fb9fc",
                        "traderInsts": [
                            "ICP-USDT-SWAP",
                            "MINA-USDT-SWAP"
    
                        ],
                        "uniqueCode": "540D011FDACCB47A",
                        "winRatio": "0.6957"
                    }
                ],
                "totalPage": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
dataVer | String | 排名数据的版本  
totalPage | String | 总的页数  
ranks | Array of objects | 交易员排名信息  
> aum | String | 带单规模，单位为USDT  
> copyState | String | 当前跟单状态   
`0`: 没在跟单  
`1`：在跟单  
> maxCopyTraderNum | String | 最大跟单人数  
> copyTraderNum | String | 跟单人数  
> accCopyTraderNum | String | 累计跟单人数  
> portLink | String | 头像  
> nickName | String | 昵称  
> ccy | String | 保证金币种  
> uniqueCode | String | 交易员唯一标识码  
> winRatio | String | 胜率，0.1 代表 10%  
> leadDays | String | 带单天数  
> traderInsts | Array of strings | 交易员带单的合约列表  
> pnl | String | 近90日交易员收益，单位为 USDT  
> pnlRatio | String | 近90日交易员收益率，0.1 代表 10%  
> pnlRatios | Array of objects | 收益率数据  
>> beginTs | String | 当天收益率的开始时间  
>> pnlRatio | String | 当天收益率  
  
### GET / 获取交易员收益周表现 

公共接口，获取交易员最近12周的收益表现，按时间倒序返回

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-weekly-pnl`

> 请求示例
    
    
    GET /api/v5/copytrading/public-weekly-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "beginTs": "1701014400000",
                "pnl": "-2.8428",
                "pnlRatio": "-0.0106"
            },
            {
                "beginTs": "1700409600000",
                "pnl": "81.8446",
                "pnlRatio": "0.3036"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
beginTs | String | 当周收益率的开始时间  
pnl | String | 当周收益额  
pnlRatio | String | 当周收益率  
  
### GET / 获取交易员收益日表现 

公共接口，获取交易员每日的收益表现，按时间倒序返回

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-pnl`

> 请求示例
    
    
    GET /api/v5/copytrading/public-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
lastDays | String | 是 | 最近天数  
`1`: 近 7 天   
`2`: 近 30 天  
`3`: 近 90 天，   
`4`: 近 365 天  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "beginTs": "1701100800000",
                "pnl": "97.3309",
                "pnlRatio": "0.3672"
            },
            {
                "beginTs": "1701014400000",
                "pnl": "96.7755",
                "pnlRatio": "0.3651"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
beginTs | String | 当天开始时间  
pnl | String | 累计收益额  
pnlRatio | String | 累计收益率  
  
### GET / 获取交易员带单情况 

公共接口，获取交易员带单情况。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-stats`

> 请求示例
    
    
    GET /api/v5/copytrading/public-stats?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
lastDays | String | 是 | 最近天数  
`1`: 近 7 天   
`2`: 近 30 天  
`3`: 近 90 天，   
`4`: 近 365 天  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "avgSubPosNotional": "213.1038",
                "ccy": "USDT",
                "curCopyTraderPnl": "96.8071",
                "investAmt": "265.095252476476294",
                "lossDays": "1",
                "profitDays": "2",
                "winRatio": "0.6667"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
winRatio | String | 胜率  
profitDays | String | 盈利天数  
lossDays | String | 亏损天数  
curCopyTraderPnl | String | 当前跟随者收益 (USDT)  
avgSubPosNotional | String | 平均仓位价值 (USDT)  
investAmt | String | 带单本金 (USDT)  
ccy | String | 保证金币种  
  
### GET / 获取交易员币种偏好 

公共接口，获取交易员币种偏好，返回结果按 ratio 从大到小排序

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-preference-currency`

> 请求示例
    
    
    GET /api/v5/copytrading/public-preference-currency?instType=SWAP&uniqueCode=CB4594A3BB5D3538
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "ETH",
                "ratio": "0.8881"
            },
            {
                "ccy": "BTC",
                "ratio": "0.0666"
            },
            {
                "ccy": "YFII",
                "ratio": "0.0453"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 币种  
ratio | String | 占比，0.1 代表 10%  
  
### GET / 获取交易员当前带单 

公共接口，获取交易员当前带单。  

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-current-subpositions`

> 请求示例
    
    
    GET /api/v5/copytrading/public-current-subpositions?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SWAP：永续合约，默认值  
uniqueCode | String | 是 | 交易员唯一标识码  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`subPosId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`subPosId`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "lever": "5",
                "margin": "16.23304",
                "markPx": "2027.31",
                "mgnMode": "isolated",
                "openAvgPx": "2029.13",
                "openTime": "1701144639417",
                "posSide": "short",
                "subPos": "4",
                "subPosId": "649582930998104064",
                "uniqueCode": "D9ADEAB33AE9EABD",
                "upl": "0.0728",
                "uplRatio": "0.0044846806266725"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
subPosId | String | 带单仓位ID  
posSide | String | 持仓方向  
long：开平仓模式开多   
short：开平仓模式开空   
net：买卖模式（subPos为正代表开多，subPos为负代表开空）  
mgnMode | String | 保证金模式，`isolated`：逐仓 ；`cross`：全仓  
lever | String | 杠杆倍数  
openAvgPx | String | 开仓均价  
openTime | String | 开仓时间  
subPos | String | 持仓张数  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
margin | String | 保证金  
upl | String | 未实现收益  
uplRatio | String | 未实现收益率  
markPx | String | 最新标记价格，仅适用于合约  
uniqueCode | String | 交易员唯一标识代码  
ccy | String | 币种  
  
### GET / 获取交易员历史带单 

公共接口，获取交易员最近三个月的已经平仓的带单仓位，按照`subPosId`倒序排序。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-subpositions-history`

> 请求示例
    
    
    GET /api/v5/copytrading/public-subpositions-history?instType=SWAP&uniqueCode=9A8534AB09862774
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SWAP：永续合约，默认值  
uniqueCode | String | 是 | 交易员唯一标识码  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`subPosId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`subPosId`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "closeAvgPx": "28385.9",
                "closeTime": "1697709137162",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "20",
                "margin": "4.245285",
                "mgnMode": "isolated",
                "openAvgPx": "28301.9",
                "openTime": "1697698048031",
                "pnl": "0.252",
                "pnlRatio": "0.05935997229868",
                "posSide": "long",
                "subPos": "3",
                "subPosId": "635126416883355648",
                "uniqueCode": "9A8534AB09862774"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
subPosId | String | 带单仓位ID  
posSide | String | 持仓方向  
long：开平仓模式开多   
short：开平仓模式开空   
net：买卖模式（subPos为正代表开多，subPos为负代表开空）  
mgnMode | String | 保证金模式，`isolated`：逐仓 ；`cross`：全仓  
lever | String | 杠杆倍数  
openAvgPx | String | 开仓均价  
openTime | String | 开仓时间  
subPos | String | 持仓张数  
closeTime | String | 平仓时间(最近一次平仓的时间)  
closeAvgPx | String | 平仓均价  
pnl | String | 收益额  
pnlRatio | String | 收益率  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
margin | String | 保证金  
ccy | String | 币种  
uniqueCode | String | 交易员唯一标识代码  
  
### GET / 获取跟单人信息 

公共接口，获取交易员的跟单人信息，按收益从高到低返回

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-copy-traders`

> 请求示例
    
    
    GET /api/v5/copytrading/public-copy-traders?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "copyTotalPnl": "2060.12242",
                "copyTraderNumChg": "1",
                "copyTraderNumChgRatio": "0.5",
                "copyTraders": [
                    {
                        "beginCopyTime": "1686125051000",
                        "nickName": "bre***@gmail.com",
                        "pnl": "1076.77388",
                        "portLink": ""
                    },
                    {
                        "beginCopyTime": "1698133811000",
                        "nickName": "MrYanDao505",
                        "pnl": "983.34854",
                        "portLink": "https://static.okx.com/cdn/okex/users/headimages/20231010/fd31f45e99fe41f7bb219c0b53ae0ada"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
copyTotalPnl | String | 跟单员总收益  
ccy | String | 总收益币种名称  
copyTraderNumChg | String | 近 7 日变化的跟单人数  
copyTraderNumChgRatio | String | 近 7 日跟单人数变化的比率  
copyTraders | Array of objects | 跟单员信息  
> beginCopyTime | String | 跟单开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> nickName | String | 昵称  
> portLink | String | 跟单员头像的链接地址  
> pnl | String | 跟单收益  
  
### WS / 带单消息通知频道 

带单失败时的消息通知

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "copytrading-lead-notification",
            "instType": "SWAP"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "copytrading-lead-notification",
            "instType": "SWAP"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`copytrading-lead-notification`  
> instType | String | 是 | 产品类型  
`SWAP`：永续合约  
> instId | String | 否 | 产品ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "copytrading-lead-notification",
            "instType": "SWAP"
        },
        "connId": "aa993428"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"copytrading-lead-notification\", \"instType\" : \"FUTURES\"}]}",
        "connId":"a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> instType | String | 是 | 产品类型  
`SWAP`：永续合约  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket 连接ID  
  
> 推送示例：
    
    
    {
        "arg": {
            "channel": "copytrading-lead-notification",
            "instType": "SWAP",
            "uid": "525627088439549953"
        },
        "data": [
            {
                "infoType": "2",
                "instId": "",
                "instType": "SWAP",
                "maxLeadTraderNum": "3",
                "minLeadEq": "",
                "posSide": "",
                "side": "",
                "subPosId": "667695035433385984",
                "uniqueCode": "3AF72F63E3EAD701"
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instType | String | 产品类型  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> infoType | String | 消息类型  
`1`: 带单失败，触发最大仓位限制  
`2`: 带单失败，触发带单次数限制  
`3`: 带单失败，交易账户 USDT 低于最小权益  
> subPosId | String | 带单仓位 ID  
> uniqueCode | String | 交易员唯一标识码  
> instId | String | 产品 ID  
> side | String | 订单方向，`buy` `sell`  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
> maxLeadTraderNum | String | 当前交易员单日最大带单次数  
> minLeadEq | String | 带单最小 USDT 权益