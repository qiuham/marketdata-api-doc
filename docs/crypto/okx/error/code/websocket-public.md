---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#error-code-websocket-public
anchor_id: error-code-websocket-public
api_type: WebSocket
updated_at: 2026-07-20 19:37:56.582871
---

# Public

Error Code from 60000 to 64002

#### General Class

Error Code | Error Message  
---|---  
60004 | Invalid timestamp  
60005 | Invalid apiKey  
60006 | Timestamp request expired  
60007 | Invalid sign  
60008 | The current WebSocket endpoint does not support subscribing to {0} channels. Please check the WebSocket URL  
60009 | Login failure  
60011 | Please log in  
60012 | Invalid request  
60013 | Invalid args  
60014 | Requests too frequent  
60018 | Wrong URL or {0} doesn't exist. Please use the correct URL, channel and parameters referring to API document.  
60019 | Invalid op: {op}  
60023 | Bulk login requests too frequent  
60024 | Wrong passphrase  
60026 | Batch login by APIKey and token simultaneously is not supported.  
60027 | Parameter {0} can not be empty.  
60028 | The current operation is not supported by this URL. Please use the correct WebSocket URL for the operation.  
60031 | The WebSocket endpoint does not allow multiple or repeated logins.  
60032 | API key doesn't exist.  
60033 | Parameter {param0} error.  
63999 | Login failed due to internal error. Please try again later.  
64000 | Subscription parameter uly is unavailable anymore, please replace uly with instFamily. More details can refer to: https://www.okx.com/help-center/changes-to-v5-api-websocket-subscription-parameter-and-url.  
64001 | This channel has been migrated to the '/business' URL. Please subscribe using the new URL. More details can refer to: https://www.okx.com/help-center/changes-to-v5-api-websocket-subscription-parameter-and-url.  
64002 | This channel is not supported by "/business" URL. Please use "/private" URL(for private channels), or "/public" URL(for public channels). More details can refer to: https://www.okx.com/help-center/changes-to-v5-api-websocket-subscription-parameter-and-url.  
64003 | Your trading fee tier doesn't meet the requirement to access this channel  
64004 | Subscribe to both {channelName} and books-l2-tbt for {instId} is not allowed. Unsubscribe books-l2-tbt first.  
64007 | Operation {0} failed due to WebSocket internal error. Please try again later.  
64008 | The connection will soon be closed for a service upgrade. Please reconnect.  
  
#### Close Frame

Status Code | Reason Text  
---|---  
1009 | Request message exceeds the maximum frame length  
4001 | Login Failed  
4002 | Invalid Request  
4003 | APIKey subscription amount exceeds the limit 100  
4004 | No data received in 30s  
4005 | Buffer is full, cannot write data  
4006 | Abnormal disconnection  
4007 | API key has been updated or deleted. Please reconnect.  
4008 | The number of subscribed channels exceeds the maximum limit.  
4009 | The number of subscription channels for this connection exceeds the limit  
Disclaimer: The availability of products and services listed on this page will depend on your region. Please see your applicable Terms of Service for more detail.

---

# 公共

错误码从 60000 到 64002

#### 通用类

错误码 | 错误消息  
---|---  
60004 | 无效的 timestamp  
60005 | 无效的 apiKey  
60006 | 请求时间戳过期  
60007 | 无效的签名  
60008 | 当前服务不支持订阅{0}频道，请检查WebSocket地址  
60009 | 登录失败  
60011 | 用户需要登录  
60012 | 不合法的请求  
60013 | 无效的参数 args  
60014 | 用户请求频率过快，超过该接口允许的限额  
60018 | 错误的 URL 或者 {0} 不存在，请参考 API 文档使用正确的 URL，频道和参数  
60019 | 无效的op{0}  
60023 | 批量登录请求过于频繁  
60024 | passphrase不正确  
60026 | 不支持APIKey和token同时登录  
60027 | 参数{0}不可为空  
60028 | 当前服务不支持此功能，请检查WebSocket地址  
60031 | WebSocket地址不支持多账户和重复登录  
60032 | API key 不存在  
60033 | {param0} 参数错误  
63999 | 由于内部错误，登录失败，请稍后重试。  
64000 | 订阅参数 uly 已失效，请您尽快将 uly 替换为 instFamily，更多详情可参考: https://www.okx.com/cn/help-center/changes-to-v5-api-websocket-subscription-parameter-and-url.  
64001 | 该频道到已经迁移到了 '/business' URL，请使用新的 URL。更多详情可参考：https://www.okx.com/cn/help-center/changes-to-v5-api-websocket-subscription-parameter-and-url.  
64002 | "/business" URL 不支持该频道. 请使用"/private" URL(对于私有频道), 或者"/public" URL(对于公有频道)，更多详情可参考：https://www.okx.com/cn/help-center/changes-to-v5-api-websocket-subscription-parameter-and-url.  
64003 | 用户交易费等级不支持访问该频道  
64004 | 不允许为 {instId} 同时订阅 {channelName} 以及 books-l2-tbt。请先取消订阅 books-l2-tbt。  
64007 | 由于 WebSocket 内部错误导致操作 {0} 失败，请稍后再试。  
64008 | 因服务升级，该连接即将关闭。请重新连接。  
  
#### 关闭帧

状态码 | 文案  
---|---  
1009 | 用户订阅请求过大  
4001 | 登录失败  
4002 | 参数不合法  
4003 | 登录账户多于100个  
4004 | 空闲超时30秒  
4005 | 写缓冲区满  
4006 | 异常场景关闭  
4007 | API key已更新或删除，请重新连接  
4008 | 总订阅频道数量超过最大限制  
4009 | 该连接订阅频道数超限制  
请注意：此页面展示的产品与服务是否可用，将视您所在的地区而定。请参阅您所在地区适用的服务条款了解更多详情。