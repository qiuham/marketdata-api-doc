---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-websocket-deposit-info-channel
anchor_id: funding-account-websocket-deposit-info-channel
api_type: WebSocket
updated_at: 2026-07-14 19:20:50.597545
---

# Deposit info channel

A push notification is triggered when a deposit is initiated or the deposit status changes.  
Supports subscriptions for accounts  
  
  
  * If it is a master account subscription, you can receive the push of the deposit info of both the master account and the sub-account.
  * If it is a sub-account subscription, only the push of sub-account deposit info you can receive.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "deposit-info"
            }
        ]
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
        args = [
            {
                "channel": "deposit-info"
            }
        ]
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
`deposit-info`  
> ccy | String | No | Currency, e.g. `BTC`  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "deposit-info"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"deposit-info\""}]}",
        "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`deposit-info`  
> ccy | String | No | Currency, e.g. `BTC`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "deposit-info",
            "uid": "289320****60975104"
        },
        "data": [{
            "actualDepBlkConfirm": "0",
            "amt": "1",
            "areaCodeFrom": "",
            "ccy": "USDT",
            "chain": "USDT-TRC20",
            "depId": "88165462",
            "from": "",
            "fromWdId": "",
            "pTime": "1674103661147",
            "state": "0",
            "subAcct": "test",
            "to": "TEhFAqpuHa3LY*****8ByNoGnrmexeGMw",
            "ts": "1674103661123",
            "txId": "bc5376817*****************dbb0d729f6b",
            "uid": "289320****60975104"
        }]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
`deposit-info`  
> uid | String | User Identifier  
> ccy | String | Currency, e.g. `BTC`  
data | Array of objects | Subscribed data  
> uid | String | User Identifier of the message producer  
> subAcct | String | Sub-account name  
If the message producer is master account, the parameter will return ""  
> pTime | String | Push time, the millisecond format of the Unix timestamp, e.g. `1597026383085`  
> ccy | String | Currency  
> chain | String | Chain name  
> amt | String | Deposit amount  
> from | String | Deposit account  
Only the internal OKX account (masked mobile phone number or email address) is returned, not the address on the blockchain.  
> areaCodeFrom | String | If `from` is a phone number, this parameter return area code of the phone number  
> to | String | Deposit address  
> txId | String | Hash record of the deposit  
> ts | String | Time of deposit record is created, Unix timestamp format in milliseconds, e.g. `1655251200000`  
> state | String | Status of deposit  
`0`: waiting for confirmation  
`1`: deposit credited   
`2`: deposit successful   
`8`: pending due to temporary deposit suspension on this crypto currency  
`11`: match the address blacklist  
`12`: account or deposit is frozen  
`13`: sub-account deposit interception  
`14`: KYC limit  
> depId | String | Deposit ID  
> fromWdId | String | Internal transfer initiator's withdrawal ID  
If the deposit comes from internal transfer, this field displays the withdrawal ID of the internal transfer initiator, and will return "" in other cases  
> actualDepBlkConfirm | String | The actual amount of blockchain confirmed in a single deposit

---

# 充值信息频道

当发起充值或者充值状态发生变化时会触发消息推送。  
支持母账户或者子账户的订阅   
  
  
  * 如果是母账户订阅，可以同时接受母账户与子账户的充值信息的推送  

  * 如果是子账户订阅，则仅支持子账户充值信息的推送  

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "deposit-info"
            }
        ]
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
        args = [
            {
                "channel": "deposit-info"
            }
        ]
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`deposit-info`  
> ccy | String | 否 | 币种名称，如 `BTC`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "deposit-info"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"deposit-info\""}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`deposit-info`  
> ccy | String | 否 | 币种名称，如 `BTC`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "deposit-info",
            "uid": "289320****60975104"
        },
        "data": [{
            "actualDepBlkConfirm": "0",
            "amt": "1",
            "areaCodeFrom": "",
            "ccy": "USDT",
            "chain": "USDT-TRC20",
            "depId": "88165462",
            "from": "",
            "fromWdId": "",
            "pTime": "1674103661147",
            "state": "0",
            "subAcct": "test",
            "to": "TEhFAqpuHa3LY*****8ByNoGnrmexeGMw",
            "ts": "1674103661123",
            "txId": "bc5376817*****************dbb0d729f6b",
            "uid": "289320****60975104"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
`deposit-info`  
> uid | String | 用户标识  
> ccy | String | 币种名称，如 `BTC`  
data | Array of objects | 订阅的数据  
> uid | String | (产生数据者的）用户标识  
> subAcct | String | 子账户名称  
如果是母账户产生的数据，该字段返回""  
> pTime | String | 推送时间，Unix时间戳的毫秒数格式，如 1597026383085  
> ccy | String | 币种名称，如 `BTC`  
> chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
> amt | String | 充值数量  
> from | String | 充值账户，仅展示内部账户的转账地址（手机号和邮箱将做脱敏处理），不展示区块链充值地址  
> areaCodeFrom | String | 如果`from`为手机号，该字段为该手机号的区号  
> to | String | 到账地址  
> txId | String | 区块转账哈希记录  
> ts | String | 充值记录创建时间，Unix 时间戳的毫秒数格式，如 `1655251200000`  
> state | String | 充值状态  
`0`：等待确认   
`1`：确认到账   
`2`：充值成功   
`8`：因该币种暂停充值而未到账，恢复充值后自动到账  
`11`：命中地址黑名单  
`12`：账户或充值被冻结  
`13`：子账户充值拦截  
`14`：KYC限额  
> depId | String | 充值记录 ID  
> fromWdId | String | 内部转账发起者提币申请 ID  
如果该笔充值来自于内部转账，则该字段展示内部转账发起者的提币申请 ID，其他情况返回""  
> actualDepBlkConfirm | String | 最新的充币网络确认数