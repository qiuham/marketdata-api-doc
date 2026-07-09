---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-websocket-login
anchor_id: overview-websocket-login
api_type: WebSocket
updated_at: 2026-07-09 19:36:22.938978
---

# Login

> Request Example
    
    
    {
      "op": "login",
      "args": [
        {
          "apiKey": "******",
          "passphrase": "******",
          "timestamp": "1538054050",
          "sign": "7L+zFQ+CEgGu5rzCj4+BdV2/uUHGqddA9pI6ztsRRPs="
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
op | String | Yes | Operation  
`login`  
args | Array of objects | Yes | List of account to login  
> apiKey | String | Yes | API Key  
> passphrase | String | Yes | API Key password  
> timestamp | String | Yes | Unix Epoch time, the unit is seconds  
> sign | String | Yes | Signature string  
  
> Successful Response Example
    
    
    {
      "event": "login",
      "code": "0",
      "msg": "",
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "event": "error",
      "code": "60009",
      "msg": "Login failed.",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
event | String | Yes | Operation  
`login`  
`error`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
**apiKey** : Unique identification for invoking API. Requires user to apply one manually.

**passphrase** : API Key password

**timestamp** : the Unix Epoch time, the unit is seconds, e.g. 1704876947

**sign** : signature string, the signature algorithm is as follows:

First concatenate `timestamp`, `method`, `requestPath`, strings, then use HMAC SHA256 method to encrypt the concatenated string with SecretKey, and then perform Base64 encoding.

**secretKey** : The security key generated when the user applies for API key, e.g. `22582BD0CFF14C41EDBF1AB98506286D`

**Example of timestamp** : const timestamp = '' + Date.now() / 1,000

**Among sign example** : sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+'/users/self/verify', secretKey))

**method** : always 'GET'.

**requestPath** : always '/users/self/verify'

The request will expire 30 seconds after the timestamp. If your server time differs from the API server time, we recommended using the REST API to query the API server time and then set the timestamp.

---

# 登录

> 请求示例
    
    
    {
     "op": "login",
     "args":
      [
         {
           "apiKey": "******",
           "passphrase": "******",
           "timestamp": "1538054050",
           "sign": "7L+zFQ+CEgGu5rzCj4+BdV2/uUHGqddA9pI6ztsRRPs=" 
          }
       ]
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
op | String | 是 | 操作，`login`  
args | Array of objectss | 是 | 账户列表  
> apiKey | String | 是 | APIKey  
> passphrase | String | 是 | APIKey 的密码  
> timestamp | String | 是 | 时间戳，Unix Epoch时间，单位是秒  
> sign | String | 是 | 签名字符串  
  
> 全部成功返回示例
    
    
    {
      "event": "login",
      "code": "0",
      "msg": "",
      "connId": "a4d3ae55"
    }
    

> 全部失败返回示例
    
    
    {
      "event": "error",
      "code": "60009",
      "msg": "Login failed.",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
event | String | 是 | 操作，`login` `error`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
**apiKey** :调用API的唯一标识。需要用户手动设置一个 **passphrase** :APIKey的密码 **timestamp** :Unix Epoch 时间戳，单位为秒，如 1704876947 **sign** :签名字符串，签名算法如下：

先将`timestamp` 、 `method` 、`requestPath` 进行字符串拼接，再使用HMAC SHA256方法将拼接后的字符串和SecretKey加密，然后进行Base64编码

**SecretKey:** 用户申请APIKey时所生成的安全密钥，如：22582BD0CFF14C41EDBF1AB98506286D

**其中 timestamp 示例** :const timestamp = '' + Date.now() / 1,000

**其中 sign 示例** : sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+ '/users/self/verify', secret))

**method** 总是 'GET'

**requestPath** 总是 '/users/self/verify'

请求在时间戳之后30秒会失效，如果您的服务器时间和API服务器时间有偏差，推荐使用 REST API查询API服务器的时间，然后设置时间戳