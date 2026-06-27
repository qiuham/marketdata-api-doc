---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-move-positions
anchor_id: trading-account-rest-api-move-positions
api_type: REST
updated_at: 2026-05-27 19:34:38.636272
---

# Move positions

Only applicable to users with a trading level greater than or equal to VIP6, and can only be called through the API Key of the master account. Users can check their trading level through the fee details table on the [My trading fees](https://www.okx.com/balance/fee) page.  
  
  
To move positions between different accounts under the same master account. Each source account can trigger up to fifteen move position requests every 24 hours. There is no limitation to the destination account to receive positions. Refer to the "Things to note" part for more details.

#### Rate limit: 1 request per second

#### Rate limit rule: Master account User ID

#### HTTP Request

`POST /api/v5/account/move-positions`

> Request example
    
    
    {
       "fromAcct":"0",
       "toAcct":"test",
       "legs":[
          {
             "from":{
                "posId":"2065471111340792832",
                "side":"sell",
                "sz":"1"
             },
             "to":{
                "posSide":"net",
                "tdMode":"cross"
             }
          },
          {
             "from":{
                "posId":"2063111180412153856",
                "side":"sell",
                "sz":"1"
             },
             "to":{
                "posSide":"net",
                "tdMode":"cross"
             }
          }
       ],
       "clientId":"test"
    }
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
fromAcct | String | Yes | Source account name. If it's a master account, it should be "0"  
toAcct | String | Yes | Destination account name. If it's a master account, it should be "0"  
legs | Array of Objects | Yes | An array of objects containing details of each position to be moved  
> from | Object | yes | Details of the position in the source account  
>> posId | String | Yes | Position ID in the source account  
>> sz | String | Yes | Number of contracts.  
>> side | String | Yes | Trade side from the perspective of source account  
`buy`  
`sell`  
> to | Object | Yes | Details of the configuration of the destination account  
>> tdMode | String | No | Trading mode in the destination account.  
`cross`  
`isolated`  
If not provided, tdMode will take the default values as shown below:  
Buy options in `Futures mode`/`Multi-currency margin mode`: `isolated`  
Other cases: `cross`  
>> posSide | String | No | Position side  
`net`  
`long`  
`short`  
This parameter is not mandatory if the destination sub-account is in **net** mode. If you pass it through, the only valid value is `net`.It can only be `long` or `short` if the destination sub-account is in long/short mode. If not specified, destination account in long/short mode always open new positions.  
>> ccy | String | No | Margin currency in destination accountOnly applicable to cross margin positions in `Futures mode`.  
clientId | String | Yes | Client-supplied ID. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Response example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "clientId": "test",
                "blockTdId": "2065832911119076864",
                "state": "filled",
                "ts": "1734069018526",
                "fromAcct": "0",
                "toAcct": "test",
                "legs": [
                    {
                        "from": {
                            "posId": "2065471111340792832",
                            "instId": "BTC-USD-SWAP",
                            "px": "100042.7",
                            "side": "sell",
                            "sz": "1",
                            "sCode": "0",
                            "sMsg": ""
                        },
                        "to": {
                            "instId": "BTC-USD-SWAP",
                            "px": "100042.7",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": "",
                            "sCode": "0",
                            "sMsg": ""
                        }
                    },
                    {
                        "from": {
                            "posId": "2063111180412153856",
                            "instId": "BTC-USDT-SWAP",
                            "px": "100008.1",
                            "side": "sell",
                            "sz": "1",
                            "sCode": "0",
                            "sMsg": ""
                        },
                        "to": {
                            "instId": "BTC-USDT-SWAP",
                            "px": "100008.1",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": "",
                            "sCode": "0",
                            "sMsg": ""
                        }
                    }
                ]
            }
        ]
    }
    
    

> Response example:failure
    
    
    // The destination account position mode (net/longShort) is not matched with the posSide field
    {
        "code": "51000",
        "msg": "Incorrect type of posSide (leg with Instrument Id [BTC-USD-SWAP])",
        "data": []
    }
    
    // The BTC amount in the destination account is not enough to open the position.
    {
        "code": "51008",
        "msg": "Order failed. Insufficient BTC margin in account",
        "data": []
    }
    
    // TradeFi positions are not supported.
    {
        "code": "70004",
        "msg": "Invalid instrument ID XAG-USDT-SWAP",
        "data": []
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
blockTdId | String | Block trade ID  
clientId | String | Client-supplied ID  
state | String | Status of the order `filled`, `failed`  
fromAcct | String | Source account name  
toAcct | String | Destination account name  
legs | Array | An array of objects containing details of each position to be moved  
> from | Object | Object describing the "from" leg  
>> instId | String | Instrument ID  
>> posId | String | Position ID  
>> px | String | Transfer price, typically a 60-minute TWAP of the mark price  
>> side | String | Direction of the leg in the source account  
`buy`  
`sell`  
>> sz | String | Number of Contracts  
>> sCode | String | The code of the event execution result, 0 means success  
>> sMsg | String | Rejection message if the request is unsuccessful  
> to | Object | Object describing the "to" leg  
>> instId | String | Instrument ID  
>> side | String | Trade side of the trade in the destination account  
>> posSide | String | Position side of the trade in the destination account  
>> tdMode | String | Trade mode  
>> px | String | Transfer price, typically a 60-minute TWAP of the mark price  
>> ccy | String | Margin currency  
>> sCode | String | The code of the event execution result, 0 means success  
>> sMsg | String | Rejection message if the request is unsuccessful  
ts | String | Unix timestamp in milliseconds indicating when the transfer request was processed  
  
#### Things to note

  1. Only applicable to users with a trading level greater than or equal to VIP6, and can only be called through the API Key of the master account.
  2. The source and destination accounts for move positions must be accounts under the same master account and they must be different.
  3. For source account, a maximum of fifteen move position requests can be triggered within a 24-hour period. There is no limitation to the destination account to receive positions. Only successful requests are counted toward this limit.
  4. The maximum number of legs per move position request is 30.
  5. No move position fee will be charged at this time.
  6. Moving positions is not supported in margin trading now.
  7. TradeFi positions are not supported.
  8. The move position price is determined by the TWAP (Time-Weighted Average Price) of the mark price over the past 60 minutes, using the closing mark price per minute. If the symbol is newly listed and a 60-minute TWAP is unavailable, the move position will be rejected with error code 70065
  9. The move position will share the same price limit as those in the order book. The move position will fail if the 60-minute mark price TWAP is outside of the price limit.
  10. For the source account, move positions must be conducted in a reduce-only manner. You must choose the opposite side of your current position and specify a size equal to or smaller than your existing position size. The system will also process move position requests in a best-effort reduce-only manner.
  11. The side field of source account leg (from) should be `sell` if you are holding a long position while the side of destination account leg (to) should be `buy`, vice versa for a short position.
  12. The posSide field of destination account (to) should be `net` if it's in one-way mode; `long`/`short` if it's in hedge mode. If in hedge mode, you need to specify `long`/`short` to decide whether to close current positions or open reverse positions. Otherwise, it will always open new positions. 
     1. Open long: buy and open long (side: buy; posSide: long)
     2. Open short: sell and open short (side: sell; posSide: short)
     3. Close long: sell and close long (side: sell; posSide: long)
     4. Close short: buy and close short (side: buy; posSide: short)
  13. Historical records of move positions can be fetched from the _Get move positions history_ endpoint but only for pending or successful requests.
  14. Move positions operation counting example.

Transfer done within the day | Account A count (total) | Account B count (total) | Account C count (total) | Account D count (total)  
---|---|---|---|---  
Account A to Account B | 1 | 0 | 0 | 0  
Account B to Account C | 1 | 1 | 0 | 0  
Account B to Account D | 1 | 2 | 0 | 0

---

# 移仓

仅适用于交易等级大于等于VIP6的用户，仅能通过母账户的API Key调用。用户可通过[我的手续费](https://www.okx.com/balance/fee)页面的手续费详情表格查看自己的交易等级。  
  
  
支持同一母账户下的子账户间仓位划转。每个源账户每24小时最多可触发15次移仓请求，目标账户接受移仓不受次数限制。参考下文“注意事项”部分，以获取详情。

#### 限速：1次/1s

#### 限速规则：母账户 User ID

#### HTTP请求

`POST /api/v5/account/move-positions`

> 请求示例
    
    
    {
       "fromAcct":"0",
       "toAcct":"test",
       "legs":[
          {
             "from":{
                "posId":"2065471111340792832",
                "side":"sell",
                "sz":"1"
             },
             "to":{
                "posSide":"net",
                "tdMode":"cross"
             }
          },
          {
             "from":{
                "posId":"2063111180412153856",
                "side":"sell",
                "sz":"1"
             },
             "to":{
                "posSide":"net",
                "tdMode":"cross"
             }
          }
       ],
       "clientId":"test"
    }
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
fromAcct | String | 是 | 源账户名，使用"0"代表母账户  
toAcct | String | 是 | 目标账户名，使用"0"代表母账户  
legs | Array of Objects | 是 | 移仓仓位列表，每次最多支持30个仓位  
> from | Object | 是 | 源账户仓位  
>> posId | String | 是 | 源账户持仓ID  
>> sz | String | 是 | 合约数量  
>> side | String | 是 | 源账户的交易方向  
`buy`  
`sell`  
> to | Object | 是 | 目标账户移仓配置  
>> tdMode | String | 否 | 目标账户的交易模式  
`cross`：全仓  
`isolated`：逐仓  
若未提供，tdMode会采用以下默认值：  
在合约模式或跨币种保证金模式下买入期权：`isolated`  
其他情况：`cross`  
>> posSide | String | 否 | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
当目标账户处于买卖模式时，用户不需传入该参数，若传入，唯一有效值为`net`；当处于开平仓模式时，有效值为`long`，`short`，若未指定，目标账户将总是开仓  
>> ccy | String | 否 | 目标账户保证金币种  
仅适用于`合约模式`下的全仓杠杆仓位  
clientId | String | 是 | 客户自定义ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "clientId": "test",
                "blockTdId": "2065832911119076864",
                "state": "filled",
                "ts": "1734069018526",
                "fromAcct": "0",
                "toAcct": "test",
                "legs": [
                    {
                        "from": {
                            "posId": "2065471111340792832",
                            "instId": "BTC-USD-SWAP",
                            "px": "100042.7",
                            "side": "sell",
                            "sz": "1",
                            "sCode": "0",
                            "sMsg": ""
                        },
                        "to": {
                            "instId": "BTC-USD-SWAP",
                            "px": "100042.7",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": "",
                            "sCode": "0",
                            "sMsg": ""
                        }
                    },
                    {
                        "from": {
                            "posId": "2063111180412153856",
                            "instId": "BTC-USDT-SWAP",
                            "px": "100008.1",
                            "side": "sell",
                            "sz": "1",
                            "sCode": "0",
                            "sMsg": ""
                        },
                        "to": {
                            "instId": "BTC-USDT-SWAP",
                            "px": "100008.1",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": "",
                            "sCode": "0",
                            "sMsg": ""
                        }
                    }
                ]
            }
        ]
    }
    
    

> 返回示例:失败
    
    
    // 目标账户处于开平仓模式，传入posSide:net不匹配
    {
        "code": "51000",
        "msg": "Incorrect type of posSide (leg with Instrument Id [BTC-USD-SWAP])",
        "data": []
    }
    
    // 目标账户的BTC余额不足以开新仓位
    {
        "code": "51008",
        "msg": "Order failed. Insufficient BTC margin in account",
        "data": []
    }
    
    // TradeFi仓位不支持移仓
    {
        "code": "70004",
        "msg": "Invalid instrument ID XAG-USDT-SWAP",
        "data": []
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
blockTdId | String | 大宗交易ID  
clientId | String | 客户自定义ID  
state | String | 移仓状态，`filled` `failed`  
fromAcct | String | 源账户名  
toAcct | String | 目标账户名  
legs | Array | 移仓仓位列表  
> from | Object | 源账户仓位  
>> instId | String | 产品ID  
>> posId | String | 持仓ID  
>> px | String | 移仓价格，过去60分钟的标记价格TWAP  
>> side | String | 源账户的交易方向  
`buy`  
`sell`  
>> sz | String | 合约数量  
>> sCode | String | 事件执行结果的code，0代表成功  
>> sMsg | String | 事件执行失败或成功时的msg  
> to | Object | 目标账户移仓配置  
>> instId | String | 产品ID  
>> side | String | 目标账户交易方向  
>> posSide | String | 目标账户持仓方向  
>> tdMode | String | 目标账户的交易模式  
>> px | String | 移仓价格，过去60分钟的标记价格TWAP  
>> ccy | String | 保证金币种  
>> sCode | String | 事件执行结果的code，0代表成功  
>> sMsg | String | 事件执行失败或成功时的msg  
ts | String | 移仓请求处理时间戳，Unix时间戳的毫秒数格式，如`1597026383085`  
  
#### 注意事项

  1. 仅适用于交易等级大于等于VIP6的用户，仅能通过母账户的API Key调用
  2. 移仓的源账户和目标账户必须是统一主账户下的子账户，且两者不能相同
  3. 对于源账户，24小时内最多可触发15次移仓请求，目标账户接收仓位没有次数限制，只有成功的请求才会计入该限制
  4. 每个移仓请求最多支持30个仓位
  5. 目前暂不收取移仓手续费
  6. 目前币币杠杆交易产生的仓位不支持移仓
  7. TradeFi仓位不支持移仓
  8. 移仓价格采用过去60分钟内每分钟标记价格收盘价的TWAP（时间加权平均价格），若交易对为新上币且无法获取60分钟TWAP，移仓将被拒绝并返回错误码70065
  9. 移仓适用于订单簿相同的限价，若标记价格TWAP超出限价范围，移仓将失败
  10. 对源账户而言，移仓必须以只减仓模式进行；必须选择当前持仓的相反方向，且划转数量需小于或等于现有持仓量；系统将以尽力而为的方式按只减仓原则处理移仓请求
  11. 当持有多仓时，源账户的side字段应为sell，目标账户则应为buy；空仓时，方向相反
  12. 目标账户若为买卖模式，posSide应为net；若为开平仓模式，则需指定posSide为long/short以决定平仓或反向开仓，未指定时默认开新仓： 
     1. 开多：买入开多（side: buy; posSide: long）
     2. 开空：卖出开空（side: sell; posSide: short）
     3. 平多：卖出平多（side: sell; posSide: long）
     4. 平空：买入平空（side: buy; posSide: short
  13. 移仓历史可通过”获取移仓历史”接口查询，该接口仅包含处理中或成功的请求
  14. 移仓操作计数示例

移仓操作 | 账户A总计次数 | 账户B总计次数 | 账户C总计次数 | 账户D总计次数  
---|---|---|---|---  
账户A到账户B | 1 | 0 | 0 | 0  
账户B到账户C | 1 | 1 | 0 | 0  
账户B到账户D | 1 | 2 | 0 | 0