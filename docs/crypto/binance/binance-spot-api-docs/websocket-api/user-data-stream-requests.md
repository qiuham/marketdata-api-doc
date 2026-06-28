---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests
api_type: WebSocket
updated_at: 2026-05-27 18:55:22.283123
---

# User Data Stream requests

### User Data Stream subscription[​](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#user-data-stream-subscription "Direct link to User Data Stream subscription")

**General information:**

  * [User Data Stream](/docs/binance-spot-api-docs/user-data-stream) subscriptions allow you to receive all the events related to a given account on a WebSocket connection.
  * There are 2 ways to start a subscription: 
    * If you have an authenticated session, then you can subscribe to events for that authenticated account using [`userDataStream.subscribe`](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#user-data-stream-subscribe).
    * In any session, authenticated or not, you can subscribe to events for one or more accounts for which you can provide an API Key signature, using [`userDataStream.subscribe.signature`](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#user-data-signature).
    * You can have only one active subscription for a given account on a given connection.
  * Subscriptions are identified by a `subscriptionId` which is returned when starting the subscription. That `subscriptionId` allows you to map the events you receive to a given subscription. 
    * All active subscriptions for a session can be found using [`session.subscriptions`](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#session-subscription).
  * Limits 
    * A single session supports **up to 1,000 active subscriptions** simultaneously. 
      * Attempting to start a new subscription beyond this limit will result in an error.
      * If your accounts are very active, we suggest not opening too many subscriptions at once, in order to not overload your connection.
    * A single session can handle a maximum of **65,535 total subscriptions** over its lifetime. 
      * If this limit is reached, you will receive an error and must re-establish a new connection to be able to start new subscriptions.
  * To verify the status of User Data Stream subscriptions, check the `userDataStream` field in [`session.status`](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#query-session-status): 
    * `null` \- User Data Stream subscriptions are **not available** on this WebSocket API.
    * `true` \- There is at **least one subscription active** in this session.
    * `false` \- There are **no active subscriptions** in this session.



#### Subscribe to User Data Stream (USER_STREAM)[​](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#subscribe-to-user-data-stream-user_stream "Direct link to Subscribe to User Data Stream \(USER_STREAM\)")
    
    
    {  
        "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  
        "method": "userDataStream.subscribe"  
    }  
    

Subscribe to the User Data Stream in the current WebSocket connection.

**Notes:**

  * This method requires an authenticated WebSocket connection using Ed25519 keys. Please refer to [`session.logon`](/docs/binance-spot-api-docs/websocket-api/authentication-requests#session-logon).
  * To check the subscription status, use [`session.status`](/docs/binance-spot-api-docs/websocket-api/authentication-requests#session-status), see the `userDataStream` flag indicating you have have an active subscription.
  * User Data Stream events are available in both JSON and [SBE](/docs/binance-spot-api-docs/faqs/sbe_faq) sessions. 
    * Please refer to [User Data Streams](/docs/binance-spot-api-docs/user-data-stream) for the event format details.
    * For SBE, only SBE schema 2:1 or later is supported.



**Weight** : 2

**Parameters** : NONE

**Response** :
    
    
    {  
        "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  
        "status": 200,  
        "result": {  
            "subscriptionId": 0  
        }  
    }  
    

#### Unsubscribe from User Data Stream[​](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#unsubscribe-from-user-data-stream "Direct link to Unsubscribe from User Data Stream")
    
    
    {  
        "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  
        "method": "userDataStream.unsubscribe"  
    }  
    

Stop listening to the User Data Stream in the current WebSocket connection.

Note that `session.logout` will only close the subscription created with `userDataStream.subscribe` but not subscriptions opened with `userDataStream.subscribe.signature`.

**Weight** : 2

**Parameters** :

Name| Type| Mandatory| Description  
---|---|---|---  
`subscriptionId`| INT| No| When called with no parameter, this will close all subscriptions.   
When called with the `subscriptionId` parameter, this will attempt to close the subscription with that subscription id, if it exists.  
  
**Response** :
    
    
    {  
        "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  
        "status": 200,  
        "result": {}  
    }  
    

#### Listing all subscriptions[​](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#listing-all-subscriptions "Direct link to Listing all subscriptions")
    
    
    {  
        "id": "d3df5a22-88ea-4fe0-9f4e-0fcea5d418b7",  
        "method": "session.subscriptions",  
        "params": {}  
    }  
    

**Note:**

  * Users are expected to track on their side which subscription corresponds to which account.



**Weight** : 2

**Data Source** : Memory

**Response** :
    
    
    {  
        "id": "d3df5a22-88ea-4fe0-9f4e-0fcea5d418b7",  
        "status": 200,  
        "result": [  
            {  
                "subscriptionId": 0  
            },  
            {  
                "subscriptionId": 1  
            }  
        ]  
    }  
    

#### Subscribe to User Data Stream through signature subscription (USER_STREAM)[​](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#subscribe-to-user-data-stream-through-signature-subscription-user_stream "Direct link to Subscribe to User Data Stream through signature subscription \(USER_STREAM\)")
    
    
    {  
        "id": "d3df8a22-98ea-4fe0-9f4e-0fcea5d418b7",  
        "method": "userDataStream.subscribe.signature",  
        "params": {  
            "apiKey": "mjcKCrJzTU6TChLsnPmgnQJJMR616J4yWvdZWDUeXkk6vL6dLyS7rcVOQlADlVjA",  
            "timestamp": 1747385641636,  
            "signature": "yN1vWpXb+qoZ3/dGiFs9vmpNdV7e3FxkA+BstzbezDKwObcijvk/CVkWxIwMCtCJbP270R0OempYwEpS6rDZCQ=="  
        }  
    }  
    

**Weight:** 2

**Parameters** :

Name| Type| Mandatory| Description  
---|---|---|---  
`apiKey`| STRING| Yes|   
`timestamp`| LONG| Yes|   
`signature`| STRING| Yes|   
`recvWindow`| DECIMAL| No| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
  
**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "d3df8a22-98ea-4fe0-9f4e-0fcea5d418b7",  
        "status": 200,  
        "result": {  
            "subscriptionId": 0  
        }  
    }

---

# 用户数据流请求

### 用户数据流订阅[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#用户数据流订阅 "用户数据流订阅的直接链接")

**常规信息：**

  * [用户数据流订阅](/docs/zh-CN/binance-spot-api-docs/user-data-stream)允许您通过 WebSocket 连接接收与指定帐户相关的所有事件。
  * 有两种方式可以启用订阅： 
    * 如果您拥有已通过验证的会话，则可以使用 [`userDataStream.subscribe`](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#user-data-stream-subscribe) 来订阅该已通过验证帐户的相关事件。
    * 在任何会话中，无论是否通过验证，如果您能为相关账户提供 API Key， 那么您可以使用 [`userdataStream.subscribe.signature`](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#user-data-signature) 来订阅一个或多个账户的相关事件。
    * 一个帐户在指定连接上只能有一个有效订阅。
  * 订阅由用订阅时返回的 `subscriptionId` 标识。该 `subscriptionId` 允许您将收到的事件映射到给定的订阅。
  * 可以使用 [`session.subscriptions`](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#session-subscription) 查找会话的所有有效订阅。
  * 限制 
    * 单个会话最多可同时支持**1,000 个有效订阅** 。 
      * 尝试启用超出此限制的新订阅将导致错误。
      * 如果您的帐户非常活跃，我们建议您不要一次启用过多的订阅，以免连接过载。
    * 单个会话在其生命周期内最多可处理**65,535 个订阅** 。 
      * 如果达到此限制，您将收到错误，并且必须重新建立连接才能启用新的订阅。
  * 要验证用户数据流订阅的状态，请检查 [`session.status`](/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#query-session-status) 中的 `userDataStream` 字段： 
    * `null` \- 此 WebSocket API 上**不提供** 用户数据流订阅。
    * `true` \- 此会话中**至少有一个有效订阅** 。
    * `false` \- 此会话中**没有有效订阅** 。



#### 订阅用户数据流 (USER_STREAM)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#订阅用户数据流-user_stream "订阅用户数据流 \(USER_STREAM\)的直接链接")
    
    
    {  
        "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  
        "method": "userDataStream.subscribe"  
    }  
    

订阅当前 WebSocket 连接中的用户数据流。

**注意：**

  * 此方法需要使用 Ed25519 密钥并经过鉴权的 WebSocket 连接。请参考 [`session.logon`](/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#session-logon)。
  * 如果需要查看订阅状态,可以通过 [`session.status `](/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#query-session-status)查询，当`userDataStream` 字段值为 `true` 时,表示您有一个有效的订阅.
  * 用户数据流在 JSON 和 [SBE 会话](/docs/zh-CN/binance-spot-api-docs/faqs/sbe_faq) 中均可用。 
    * 有关事件格式详情，请参阅 [用户数据流](/docs/zh-CN/binance-spot-api-docs/user-data-stream)。
    * 对于 SBE，仅支持 SBE 模式 2:1 或更高版本。



**权重:** 2

**参数:** 无

**响应:**
    
    
    {  
        "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  
        "status": 200,  
        "result": {  
            "subscriptionId": 0  
        }  
    }  
    

#### 取消订阅用户数据流[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#取消订阅用户数据流 "取消订阅用户数据流的直接链接")
    
    
    {  
        "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  
        "method": "userDataStream.unsubscribe"  
    }  
    

取消订阅当前 WebSocket 连接中的用户数据流。

请注意 `session.logout` 只会关闭由 `userDataStream.subscribe` 创建的订阅，并不会关闭通过 `userDataStream.subscribe.signature` 创建的订阅。

**权重:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`subscriptionId`| INT| No| 如果在进行调用时不用该参数，将会关闭所有订阅。   
如果在进行调用时使用 `subscriptionId` 参数，如果该 ID 存在的话，将尝试关闭与该 ID 匹配的订阅。  
  
**响应:**
    
    
    {  
        "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  
        "status": 200,  
        "result": {}  
    }  
    

#### 显示所有订阅[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#显示所有订阅 "显示所有订阅的直接链接")
    
    
    {  
        "id": "d3df5a22-88ea-4fe0-9f4e-0fcea5d418b7",  
        "method": "session.subscriptions",  
        "params": {}  
    }  
    

**注意：**

  * 用户按需要跟踪相关帐户的对应订阅情况。



**权重:** 2

**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "d3df5a22-88ea-4fe0-9f4e-0fcea5d418b7",  
        "status": 200,  
        "result": [  
            {  
                "subscriptionId": 0  
            },  
            {  
                "subscriptionId": 1  
            }  
        ]  
    }  
    

#### 通过签名订阅的方式订阅用户数据流 (USER_STREAM)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#通过签名订阅的方式订阅用户数据流-user_stream "通过签名订阅的方式订阅用户数据流 \(USER_STREAM\)的直接链接")
    
    
    {  
        "id": "d3df8a22-98ea-4fe0-9f4e-0fcea5d418b7",  
        "method": "userDataStream.subscribe.signature",  
        "params": {  
            "apiKey": "mjcKCrJzTU6TChLsnPmgnQJJMR616J4yWvdZWDUeXkk6vL6dLyS7rcVOQlADlVjA",  
            "timestamp": 1747385641636,  
            "signature": "yN1vWpXb+qoZ3/dGiFs9vmpNdV7e3FxkA+BstzbezDKwObcijvk/CVkWxIwMCtCJbP270R0OempYwEpS6rDZCQ=="  
        }  
    }  
    

**权重:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`apiKey`| STRING| Yes|   
`timestamp`| LONG| Yes|   
`signature`| STRING| Yes|   
`recvWindow`| DECIMAL| No| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
  
**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "d3df8a22-98ea-4fe0-9f4e-0fcea5d418b7",  
        "status": 200,  
        "result": {  
            "subscriptionId": 0  
        }  
    }