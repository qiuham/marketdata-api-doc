---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/demo-trading/rest-api
api_type: Guide
updated_at: 2026-11-26 19:03:07.744248
---

# Demo Trading (REST API)

Demo trading allows you to practice trading and test strategies in a real-market environment using virtual funds, helping you improve your skills and reduce the risk of losses. KYC is needed.

## API Key

To perform demo trading via API, you'll need to create a Demo API Key in the first place. The steps are as follows:

Log in to your account → Switch to Demo mode → Go to the Personal Center → Go to the API Key Management → Create a Demo API Key → Use the Demo API Key to start trading.

![Demo trading entry](https://www.bitget.com/docs-static/images/demo-trading/entry-en.png)

![Personal Center](https://www.bitget.com/docs-static/images/demo-trading/person-center-en.png)

![Create API Key](https://www.bitget.com/docs-static/images/demo-trading/create-api-key-en.png)

## REST

Please use the created Demo API Key for API calls, and add `paptrading` in the request header, with the value set to `1`.

## Request Header Example

```http title="Request Example"
GET /api/v3/market/instruments?category=usdt-futures HTTP/1.1
ACCESS-KEY: bg_xxx
ACCESS-SIGN: xxxx=
ACCESS-TIMESTAMP: 1787033528294
ACCESS-PASSPHRASE: xxxxxx
locale: zh-CN
Content-Type: application/json
paptrading: 1   <---- please add this filed in the request header
User-Agent: PostmanRuntime/7.43.0
Accept: */*
Postman-Token: xxxx
Host: api.bitget.com
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: xxxx
```

---

# REST API 模拟盘

RestAPI/Websocket 模拟盘使用前需要用户先通过KYC

模拟盘通过虚拟资金让您在实时市场环境练习交易、测试策略，从而提高熟练度并降低亏损风险

## API Key

若要进行模拟盘API交易，请先创建模拟盘API Key。操作步骤如下：

登录Bitget账户 → 切换至模拟盘 → 进入个人中心 → 访问API Key管理 → 创建模拟盘API Key → 使用模拟盘API Key开始交易

![模拟盘入口](https://www.bitget.com/docs-static/images/demo-trading/entry.png)

![个人中心](https://www.bitget.com/docs-static/images/demo-trading/person-center.png)

![创建 API Key](https://www.bitget.com/docs-static/images/demo-trading/create-api-key.png)

## REST

请使用创建的模拟盘API Key进行接口调用，并在请求头中添加`paptrading`参数，值设置为 `1`

## 请求头案例

```http title="请求案例"
GET /api/v3/market/instruments?category=usdt-futures HTTP/1.1
ACCESS-KEY: bg_xxx
ACCESS-SIGN: xxxx=
ACCESS-TIMESTAMP: 1787033528294
ACCESS-PASSPHRASE: xxxxxx
locale: zh-CN
Content-Type: application/json
paptrading: 1 <------- 请在请求头中添加此参数
User-Agent: PostmanRuntime/7.43.0
Accept: */*
Postman-Token: xxxx
Host: api.bitget.com
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: xxxx
```