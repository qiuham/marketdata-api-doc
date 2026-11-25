---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/private/Account-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:01:32.731869
---

# Account Channel

### Description

Get account information, push data according to the subscription dimensions for the first subscription. 

Data will be pushed when the following events occurred:
1. Orders are filled
2. Transfer
3. Deposit
4. Withdrawal

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "account",
            "coin": "default"
        }
    ]
}
```

### Request Parameters

| Parameter     | Type               | Required | Description                              | 
|:--------------|:-------------------|:---------|:-----------------------------------------|
| op            | String             | Yes      | Operation, subscribe unsubscribe         |
| args          | List&lt;Object&gt; | Yes      | List of channels to request subscription |
| &gt; instType | String             | Yes      | Product Type, `SPOT`                     |
| &gt; channel  | String             | Yes      | Channel name, `account`                  |
| &gt; coin     | String             | Yes      | Coin name，`default` represents all the coins，Only default is supported now                   |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "SPOT",
    "channel": "account",
    "coin": "default"
  }
}
```

### Response Parameters

| Parameter     | Type   | Description                                  | 
|:--------------|:-------|:---------------------------------------------|
| event         | String | Yes<br/>Event                                |
| arg           | Object | Subscribed channels                   |
| &gt; instType | String | Product Type, `SPOT`                        |
| &gt; channel  | String | Channel name, `account`                         |
| &gt; coin     | String | `default` |
| code          | String | Error code, returned only on error    |
| msg           | String | Error message                         |

</div>

```json title="Push Data"
{
    "action": "snapshot",
    "arg": {
        "instType": "SPOT",
        "channel": "account",
        "coin": "default"
    },
    "data": [
        {
            "coin": "USDT",
            "available": "100000",
            "frozen": "0",
            "locked": "0",
            "limitAvailable": "0",
            "uTime":"1697092295506"
        }
    ],
    "ts": 1695713887792
}
```

### Push Parameters

| Parameter            | Type               | Description                                                                       | 
|:---------------------|:-------------------|:----------------------------------------------------------------------------------|
| arg                  | Object             | Channels with successful subscription                                             |
| &gt; instType        | String             | Product Type, `SPOT`                                                                 |
| &gt; channel         | String             | Channel name, `account`                                                                      |
| &gt; coin            | String             | `default`                                                 | 
| action               | String             | Push data action, `snapshot` or `update`                  |
| data                 | List&lt;Object&gt; | Subscription data                                                                 |
| &gt; coin            | String             | Token name                                                                        |
| &gt; available       | String             | Available coin assets                                                             |
| &gt; frozen          | String             | Amount of frozen assets    Usually frozen when the order is placed                |  
| &gt; locked          | String             | Amount of locked assets  Locked assests required to become a fiat merchants, etc. |  
| &gt; limitAvailable  | String             | Restricted availability    For spot copy trading                                  |  
| &gt; uTime           | String             | Update time                                                                       |

---

# 账户频道

### 描述

获取账户信息，首次订阅按照订阅维度推送数据

以下事件发生时将推送数据：
1. 订单成交
2. 划转
3. 充值
4. 提现

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "account",
            "coin": "default"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                      | 
| :---- | :---- | :---- |:------------------------|
| op | String | 是 | 操作，subscribe unsubscribe |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表               |
| &gt; instType | String | 是 | 产品线类型, `SPOT`           |
| &gt; channel | String | 是 | 频道名, `account`          |
| coin | String | 是 | 币种名称，`default` 表示全部币种，目前只支持`default`   |

</div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "account",
        "coin": "default"
    }
}
```

### 返回参数

| 返回字段          | 参数类型 | 字段说明 | 
|:--------------| :---- | :---- |
| event         | String | 事件，subscribe unsubscribe error |
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
    "action": "snapshot",
    "arg": {
        "instType": "SPOT",
        "channel": "account",
        "coin": "default"
    },
    "data": [
        {
            "coin": "USDT",
            "available": "100000",
            "frozen": "0",
            "locked": "0",
            "limitAvailable": "0",
            "uTime":"1697092295506"
        }
    ],
    "ts": 1695713887792
}
```

### 推送数据参数

| 返回字段 | 参数类型 | 字段说明                  | 
| :---- | :---- |:----------------------|
| arg | Object | 订阅成功的频道               |
| &gt; instType | String | 产品类型                  |
| &gt; channel | String | 频道名                   |
| coin | String | `default`   |
| action | String | 推送数据动作, `snapshot` or `update`  |
| data | List&lt;Object&gt; | 订阅的数据                 |
| &gt; coin | String | 币种名称                  |
| &gt; available | String | 币种可用资产                |
| &gt; frozen | String | 冻结资产数量， 通常是下单时冻结      |
| &gt; locked | String | 锁仓资产数量， 成为法币商家等的锁仓    |
| &gt; limitAvailable | String | 受限可用， 用于现货跟单场景        |
| &gt; uTime | String | 更新时间，Unix时间戳的毫秒数格式，如 1597026383085                  |

</div>