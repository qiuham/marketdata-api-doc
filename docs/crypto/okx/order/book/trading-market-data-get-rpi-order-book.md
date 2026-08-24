---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-rpi-order-book
anchor_id: order-book-trading-market-data-get-rpi-order-book
api_type: API
updated_at: 2026-08-24 19:15:15.912333
---

# GET / RPI order book

Retrieve the consolidated order book of the instrument, combining organic depth with the currently tradeable Retail Price Improvement (RPI) depth at each price level. Non-tradeable RPI orders are filtered out platform-side and are not returned.  
The data is refreshed every 200 milliseconds. This endpoint does not return data immediately. Instead, it returns the latest data once the server-side cache has been updated.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/books-rpi`

> Request Example
    
    
    GET /api/v5/market/books-rpi?instId=BTC-USDT-SWAP&sz=3
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
sz | String | No | Order book depth per side. Maximum 400, e.g. 400 bids + 400 asks   
Defaults to `1` depth level  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "67855.2",
                        "0.5",
                        "0.5",
                        "1"
                    ],
                    [
                        "67856.0",
                        "1.3",
                        "1.0",
                        "4"
                    ],
                    [
                        "67860.5",
                        "0.3",
                        "0",
                        "1"
                    ]
                ],
                "bids": [
                    [
                        "67854.8",
                        "1.7",
                        "1.2",
                        "3"
                    ],
                    [
                        "67853.0",
                        "0.8",
                        "0.8",
                        "1"
                    ]
                ],
                "ts": "1785310731002",
                "seqId": 332042172451
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
asks | Array of Arrays | Order book on sell side. Each element is `[price, totalQty, nonRpiQty, count]`  
bids | Array of Arrays | Order book on buy side. Each element is `[price, totalQty, nonRpiQty, count]`  
ts | String | Order book generation time, Unix timestamp format in milliseconds  
seqId | Integer | Sequence ID of the current message. Provides sequencing parity with the `books-rpi` WebSocket channel  
An example of the array of asks and bids values: ["67856.0", "1.3", "1.0", "4"]  
\- "67856.0" is the depth price  
\- "1.3" is `totalQty` — the total quantity at the price, organic plus currently tradeable RPI (number of contracts for derivatives, quantity in base currency for Spot and Spot Margin)  
\- "1.0" is `nonRpiQty` — the organic (non-RPI) portion of the quantity at the price  
\- "4" is the number of orders at the price, organic plus currently tradeable RPI.  
  
The tradeable RPI quantity at a price level is derived as `totalQty - nonRpiQty`. A taker with RPI access can execute against `totalQty`; a taker without RPI access can execute only against `nonRpiQty`, even though both read the same feed. Set `rpiTakerAccess` to `true` when placing an order to access RPI liquidity.  
  
Note that the third position carries `nonRpiQty` on this endpoint only. On the `books`, `books-full` and `books-lite` endpoints the same position is a deprecated field that is always "0".  
  
A level where `totalQty` equals `nonRpiQty` simply has no tradeable RPI depth at that price. This is expected for instruments with no RPI market maker quoting them, and for any level where resting RPI orders are currently hidden under the matching rules.  This endpoint returns no `checksum`. Use `seqId` for sequencing.  
If the RPI tradeability state is unavailable, the endpoint fails closed: RPI quantity is excluded and every level returns `totalQty` equal to `nonRpiQty`.

---

# GET / 获取 RPI 产品深度

获取产品的合并深度列表，在每个价格档位上将有机深度与当前可成交的 RPI（Retail Price Improvement，散户价格优化）深度合并返回。不可成交的 RPI 订单由平台侧过滤，不会返回。  
数据每 200 毫秒更新一次。该接口收到请求后不会立刻返回，而是会待服务端缓存数据更新后立即返回最新数据。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/books-rpi`

> 请求示例
    
    
    GET /api/v5/market/books-rpi?instId=BTC-USDT-SWAP&sz=3
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT-SWAP`  
sz | String | 否 | 深度档位数量，最大值可传400，即买卖深度共800条   
不填写此参数，默认返回`1`档深度数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "67855.2",
                        "0.5",
                        "0.5",
                        "1"
                    ],
                    [
                        "67856.0",
                        "1.3",
                        "1.0",
                        "4"
                    ],
                    [
                        "67860.5",
                        "0.3",
                        "0",
                        "1"
                    ]
                ],
                "bids": [
                    [
                        "67854.8",
                        "1.7",
                        "1.2",
                        "3"
                    ],
                    [
                        "67853.0",
                        "0.8",
                        "0.8",
                        "1"
                    ]
                ],
                "ts": "1785310731002",
                "seqId": 332042172451
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
asks | Array of Arrays | 卖方深度，每个元素为 `[price, totalQty, nonRpiQty, count]`  
bids | Array of Arrays | 买方深度，每个元素为 `[price, totalQty, nonRpiQty, count]`  
ts | String | 深度产生的时间，Unix 时间戳，单位为毫秒  
seqId | Integer | 当前消息的序列号，与 `books-rpi` WebSocket 频道保持一致  
asks和bids值数组举例说明： ["67856.0", "1.3", "1.0", "4"]  
\- 67856.0 为深度价格  
\- 1.3 为 `totalQty`，即该价格的总数量，包含有机深度与当前可成交的 RPI 深度（合约交易为张数，现货/币币杠杆为交易币的数量）  
\- 1.0 为 `nonRpiQty`，即该价格中有机（非 RPI）部分的数量  
\- 4 为该价格的订单数量，包含有机订单与当前可成交的 RPI 订单  
  
该价格档位上可成交的 RPI 数量为 `totalQty - nonRpiQty`。具备 RPI 权限的 taker 可成交至 `totalQty`；不具备 RPI 权限的 taker 仅可成交至 `nonRpiQty`，即使二者读取同一份数据。下单时将 `rpiTakerAccess` 设为 `true` 即可使用 RPI 流动性。  
  
请注意，仅本接口的第三位为 `nonRpiQty`。在 `books`、`books-full`、`books-lite` 接口中，同一位置为已弃用字段，始终为 "0"。  
  
当某档位的 `totalQty` 与 `nonRpiQty` 相等时，表示该价格上当前没有可成交的 RPI 深度。对于没有 RPI 做市商报价的产品，以及依照撮合规则当前被隐藏的 RPI 挂单，出现该情况均属正常。  本接口不返回 `checksum`，请使用 `seqId` 进行排序校验。  
当 RPI 可成交状态不可用时，本接口以保守方式降级：排除 RPI 数量，每个档位返回的 `totalQty` 与 `nonRpiQty` 相等。