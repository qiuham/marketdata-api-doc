---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/margin/isolated/private/Margin-isolated-account-assets
api_type: WebSocket
updated_at: 2026-11-25 19:01:31.785364
---

# Isolated-Margin Account Channel

### Description

<div className="api-aligning">

```json title="Request Example"
{
    "args":[
        {
            "channel":"account-isolated",
            "coin":"default",
            "instType":"MARGIN"
        }
    ],
    "op":"subscribe"
}
```

### Request Parameters

| Parameter     | Type | Required | Description                                                   | 
|:--------------| :---- | :---- |:--------------------------------------------------------------|
| op            | String | Yes | Operation<br/>subscribe Subscribe<br/>unsubscribe Unsubscribe |
| args          | List&lt;Object&gt; | Yes | List of channels to request subscription                      |
| &gt; instType | String | Yes | Product type: MARGIN                                          |
| &gt; channel  | String | Yes | Channel name                                                  |
| &gt; coin     | String | Yes | Coin name，`default` represents all the coins，Only default is supported now                                                     |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event":"subscribe",
    "arg":{
        "instType":"MARGIN",
        "channel":"account-isolated",
        "coin":"default"
    }
}
```

### Response Parameters

| Parameter     | Type | Description | 
|:--------------| :---- | :---- |
| event         | String | Event |
| arg           | Object | Subscribed channels |
| &gt; instType | String | Product type |
| &gt; channel  | String | Channel name |
| &gt; coin     | String | `default` |
| code          | String | Error code, returned only on error |
| msg           | String | Error message |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "action":"snapshot",
  "arg":{
    "instType":"MARGIN",
    "channel":"account-isolated",
    "coin":"default"
  },
  "data":[
    {
      "uTime":"1695881380876",
      "id":"1",
      "coin":"USDT",
      "symbol":"BTCUSDT",
      "available":"989.4502207",
      "borrow":"0",
      "frozen":"0",
      "interest":"0",
      "coupon":"0"
    },
    {
      "uTime":"1695881380876",
      "id":"1000000002",
      "coin":"BTC",
      "symbol":"BTCUSDT",
      "available":"0.00039814",
      "borrow":"0",
      "frozen":"0",
      "interest":"0",
      "coupon":"0"
    },
    {
      "uTime":"1695881380876",
      "id":"1000000001",
      "coin":"USDT",
      "symbol":"ETHUSDT",
      "available":"9607383.17171658",
      "borrow":"0",
      "frozen":"0",
      "interest":"0",
      "coupon":"0"
    },
    {
      "uTime":"1695881380876",
      "id":"1000000000",
      "coin":"ETH",
      "symbol":"ETHUSDT",
      "available":"2.5574646",
      "borrow":"0",
      "frozen":"0",
      "interest":"0",
      "coupon":"0"
    }
  ],
  "ts":1695881380876
}
```

### Push Data Parameters

| Parameter      | Type  | Description                              | 
|:---------------| :---- |:-----------------------------------------|
| arg            | Object | Successful channel subscriptions         |
| &gt; instType  | String | Product type                             |
| &gt; channel   | String | Channel name                             |
| &gt; coin      | String | `default`                                |
| action         | String | Push data action, `snapshot` or `update` |
| data           | List&lt;Object&gt; | Subscribed data                          |
| &gt; available | String | Available amount                         |
| &gt; borrow    | String | Borrow amount                            |
| &gt; symbol    | String | Trading pair                             |
| &gt; coin      | String | Coin name                                |
| &gt; frozen    | String | Amount frozen                            |
| &gt; id        | String | ID                                       |
| &gt; interest  | String | Interest                                 |
| &gt; uTime     | String | Updated time, ms                         |
| &gt; coupon    | String | Coupon                                   |

<div className="api-br-40"></div>

</div>

---

# 逐仓杠杆账户频道

### 描述

<div className="api-aligning">

```json title="请求示例"
{
    "args":[
        {
            "channel":"account-isolated",
            "coin":"default",
            "instType":"MARGIN"
        }
    ],
    "op":"subscribe"
}
```

### 请求参数

| 参数名           | 参数类型 | 是否必须 | 描述                                       | 
|:--------------| :---- | :---- |:-----------------------------------------|
| op            | String | 是 | 操作<br/>subscribe 订阅<br/>unsubscribe 取消订阅 |
| args          | List&lt;Object&gt; | 是 | 请求订阅的频道列表                                |
| &gt; instType | String | 是 | 产品类型                                     |
| &gt; channel  | String | 是 | 频道名                                      |
| &gt; coin     | String | 是 | 币种名称，`default`表示全部币种，目前只支持`default`                                |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event":"subscribe",
    "arg":{
        "instType":"MARGIN",
        "channel":"account-isolated",
        "coin":"default"
    }
}
```

### 返回参数

| 返回字段          | 参数类型 | 字段说明 | 
|:--------------| :---- | :---- |
| event         | String | 事件 |
| arg           | Object | 订阅的频道 |
| &gt; instType | String | 产品类型 |
| &gt; channel  | String | 频道名 |
| &gt; coin     | String | `default` |
| code          | String | 错误码，错误时才会返回 |
| msg           | String | 错误消息 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action":"snapshot",
    "arg":{
        "instType":"MARGIN",
        "channel":"account-isolated",
        "coin":"default"
    },
    "data":[
        {
            "uTime":"1695881380876",
            "id":"1000000003",
            "coin":"USDT",
            "symbol":"BTCUSDT",
            "available":"989.4502207",
            "borrow":"0",
            "frozen":"0",
            "interest":"0",
            "coupon":"0"
        },
        {
            "uTime":"1695881380876",
            "id":"1000000002",
            "coin":"BTC",
            "symbol":"BTCUSDT",
            "available":"0.00039814",
            "borrow":"0",
            "frozen":"0",
            "interest":"0",
            "coupon":"0"
        },
        {
            "uTime":"1695881380876",
            "id":"1000000001",
            "coin":"USDT",
            "symbol":"ETHUSDT",
            "available":"9607383.17171658",
            "borrow":"0",
            "frozen":"0",
            "interest":"0",
            "coupon":"0"
        },
        {
            "uTime":"1695881380876",
            "id":"1000000000",
            "coin":"ETH",
            "symbol":"ETHUSDT",
            "available":"2.5574646",
            "borrow":"0",
            "frozen":"0",
            "interest":"0",
            "coupon":"0"
        }
    ],
    "ts":1695881380876
}
```

### 推送数据参数

| 返回字段           | 参数类型 | 字段说明                  | 
|:---------------| :---- |:----------------------|
| arg            | Object | 订阅成功的频道               |
| &gt; instType  | String | 产品类型                  |
| &gt; channel   | String | 频道名                   |
| &gt; coin      | String | `default`             |
| action         | String | 推送数据动作，增量推送数据还是全量推送数据 |
| data           | List&lt;Object&gt; | 订阅的数据                 |
| &gt; available | String | 可用金额                  |
| &gt; borrow    | String | 借款金额                  |
| &gt; symbol    | String | 交易对                   |
| &gt; coin      | String | 币种名称                  |
| &gt; frozen    | String | 冻结金额                  |
| &gt; id        | String | 序号                    |
| &gt; interest  | String | 利息                    |
| &gt; uTime     | String | 更新时间                  |
| &gt; coupon    | String | 体验金                   |

<div className="api-br-40"></div>

</div>