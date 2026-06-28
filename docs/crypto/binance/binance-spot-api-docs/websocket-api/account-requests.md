---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/account-requests
api_type: WebSocket
updated_at: 2026-05-27 18:54:57.820852
---

# Authentication requests

**Note:** Only _Ed25519_ keys are supported for this feature.

### Log in with API key (SIGNED)[​](/docs/binance-spot-api-docs/websocket-api/authentication-requests#log-in-with-api-key-signed "Direct link to Log in with API key \(SIGNED\)")
    
    
    {  
        "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  
        "method": "session.logon",  
        "params": {  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "1cf54395b336b0a9727ef27d5d98987962bc47aca6e13fe978612d0adee066ed",  
            "timestamp": 1649729878532  
        }  
    }  
    

Authenticate WebSocket connection using the provided API key.

After calling `session.logon`, you can omit `apiKey` and `signature` parameters for future requests that require them.

Note that only one API key can be authenticated. Calling `session.logon` multiple times changes the current authenticated API key.

**Weight:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`signature`| STRING| YES|   
`timestamp`| LONG| YES|   
  
**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  
        "status": 200,  
        "result": {  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "authorizedSince": 1649729878532,  
            "connectedSince": 1649729873021,  
            "returnRateLimits": false,  
            "serverTime": 1649729878630,  
            "userDataStream": false // is User Data Stream subscription active?  
        }  
    }  
    

### Query session status[​](/docs/binance-spot-api-docs/websocket-api/authentication-requests#query-session-status "Direct link to Query session status")
    
    
    {  
        "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",  
        "method": "session.status"  
    }  
    

Query the status of the WebSocket connection, inspecting which API key (if any) is used to authorize requests.

**Weight:** 2

**Parameters:** NONE

**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",  
        "status": 200,  
        "result": {  
            // if the connection is not authenticated, "apiKey" and "authorizedSince" will be shown as null  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "authorizedSince": 1649729878532,  
            "connectedSince": 1649729873021,  
            "returnRateLimits": false,  
            "serverTime": 1649730611671,  
            "userDataStream": true     // is User Data Stream subscription active?  
        }  
    }  
    

### Log out of the session[​](/docs/binance-spot-api-docs/websocket-api/authentication-requests#log-out-of-the-session "Direct link to Log out of the session")
    
    
    {  
        "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  
        "method": "session.logout"  
    }  
    

Forget the API key previously authenticated. If the connection is not authenticated, this request does nothing.

Note that the WebSocket connection stays open after `session.logout` request. You can continue using the connection, but now you will have to explicitly provide the `apiKey` and `signature` parameters where needed.

**Weight:** 2

**Parameters:** NONE

**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  
        "status": 200,  
        "result": {  
            "apiKey": null,  
            "authorizedSince": null,  
            "connectedSince": 1649729873021,  
            "returnRateLimits": false,  
            "serverTime": 1649730611671,  
            "userDataStream": false // is User Data Stream subscription active?  
        }  
    }

---

# 身份验证请求

**注意：** 仅支持 _Ed25519_ 密钥用于此功能。

### 用API key登录 (SIGNED)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#用api-key登录-signed "用API key登录 \(SIGNED\)的直接链接")
    
    
    {  
        "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  
        "method": "session.logon",  
        "params": {  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "1cf54395b336b0a9727ef27d5d98987962bc47aca6e13fe978612d0adee066ed",  
            "timestamp": 1649729878532  
        }  
    }  
    

使用提供的API密钥进行WebSocket连接身份验证。

在调用`session.logon`后，将来的需要`apiKey`和`signature`参数的请求可以省略它们。

请注意，只能认证一个API密钥。 多次调用`session.logon`将更改当前已认证的API密钥。

**权重:** 2

**参数:**

参数名| 类型| 是否必需| 描述  
---|---|---|---  
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`signature`| STRING| YES|   
`timestamp`| LONG| YES|   
  
**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  
        "status": 200,  
        "result": {  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "authorizedSince": 1649729878532,  
            "connectedSince": 1649729873021,  
            "returnRateLimits": false,  
            "serverTime": 1649729878630,  
            "userDataStream": false // User Data Stream 订阅是否有效？  
        }  
    }  
    

### 查询会话状态[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#查询会话状态 "查询会话状态的直接链接")
    
    
    {  
        "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",  
        "method": "session.status"  
    }  
    

查询WebSocket连接的状态，检查用于授权请求的API密钥（如果有的话）。

**权重:** 2

**参数:** NONE

**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",  
        "status": 200,  
        "result": {  
            // 如果连接未经身份验证，"apiKey" 和 "authorizedSince" 将显示为 null。  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "authorizedSince": 1649729878532,  
            "connectedSince": 1649729873021,  
            "returnRateLimits": false,  
            "serverTime": 1649730611671,  
            "userDataStream": true     // User Data Stream 订阅是否有效？  
        }  
    }  
    

### 退出会话[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#退出会话 "退出会话的直接链接")
    
    
    {  
        "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  
        "method": "session.logout"  
    }  
    

忘记之前认证的API密钥。 如果连接未经身份验证，此请求不会有任何作用。

请注意，`session.logout`请求后，WebSocket连接仍然保持打开状态。 你可以继续使用连接，但现在必须在需要的地方明确提供`apiKey`和`signature`参数。

**权重:** 2

**参数:** NONE

**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  
        "status": 200,  
        "result": {  
            "apiKey": null,  
            "authorizedSince": null,  
            "connectedSince": 1649729873021,  
            "returnRateLimits": false,  
            "serverTime": 1649730611671,  
            "userDataStream": false // User Data Stream 订阅是否有效？  
        }  
    }