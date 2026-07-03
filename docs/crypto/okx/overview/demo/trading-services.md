---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-demo-trading-services
anchor_id: overview-demo-trading-services
api_type: API
updated_at: 2026-07-03 19:38:38.332062
---

# Demo Trading Services

Currently, the API works for Demo Trading, but some functions are not supported, such as `withdraw`,`deposit`,`purchase/redemption`, etc.

The Demo Trading URL: 

  * REST: `https://openapi.okx.com`  

  * Public WebSocket: `wss://wspap.okx.com:8443/ws/v5/public`  

  * Private WebSocket: `wss://wspap.okx.com:8443/ws/v5/private`  

  * Business WebSocket: `wss://wspap.okx.com:8443/ws/v5/business`

OKX account can be used for login on Demo Trading. If you already have an OKX account, you can log in directly.

Start API Demo Trading by the following steps:  
Login OKX —> Trade —> Demo Trading —> Personal Center —> Demo Trading API -> Create Demo Trading API Key —> Start your Demo Trading

Note: `x-simulated-trading: 1` needs to be added to the header of the Demo Trading request. 

> Http Header Example 
    
    
    Content-Type: application/json
    
    OK-ACCESS-KEY: 37c541a1-****-****-****-10fe7a038418
    
    OK-ACCESS-SIGN: leaVRETrtaoEQ3yI9qEtI1CZ82ikZ4xSG5Kj8gnl3uw=
    
    OK-ACCESS-PASSPHRASE: 1****6
    
    OK-ACCESS-TIMESTAMP: 2020-03-28T12:21:41.274Z
    
    x-simulated-trading: 1
    

### Demo Trading Explorer

You need to sign in to your OKX account before accessing the explorer. The interface only allow access to the demo trading environment.

  * Clicking `Try it out` button in Parameters Panel and editing request parameters.

  * Clicking `Execute` button to send your request. You can check response in Responses panel.

Try [demo trading explorer](/demo-trading-explorer/v5/en)

---

# 模拟盘交易

目前可以进行 API 的模拟盘交易，部分功能不支持如`提币`、`充值`、`申购赎回`等。

模拟盘API交易地址如下： 

  * REST：`https://openapi.okx.com`
  * WebSocket公共频道：`wss://wspap.okx.com:8443/ws/v5/public`  

  * WebSocket私有频道：`wss://wspap.okx.com:8443/ws/v5/private`
  * WebSocket业务频道：`wss://wspap.okx.com:8443/ws/v5/business`

模拟盘的账户与欧易的账户是互通的，如果您已经有欧易账户，可以直接登录。

模拟盘API交易需要在模拟盘上创建APIKey：

登录欧易账户—>交易—>模拟交易—>个人中心—>创建模拟盘APIKey—>开始模拟交易

注意：模拟盘的请求的header里面需要添加 "x-simulated-trading: 1"。 

> 请求头示例
    
    
    Content-Type: application/json
    
    OK-ACCESS-KEY: 37c541a1-****-****-****-10fe7a038418
    
    OK-ACCESS-SIGN: leaVRETrtaoEQ3yI9qEtI1CZ82ikZ4xSG5Kj8gnl3uw=
    
    OK-ACCESS-PASSPHRASE: 1****6
    
    OK-ACCESS-TIMESTAMP: 2020-03-28T12:21:41.274Z
    
    x-simulated-trading: 1
    

### 模拟盘交互式浏览器 

该功能接口用户需先登录，接口只会请求模拟环境

  * Parameters 面板中点击`Try it out`按钮，编辑请求参数。

  * 点击`Execute`按钮发送请求。Responses 面板中查看请求结果。

立即体验 [交互式浏览器](/demo-trading-explorer/v5/zh)