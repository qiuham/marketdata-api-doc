---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-p2p-p2p
api_type: REST
updated_at: 2026-11-26 19:03:56.434256
---

# Classic P2P API

Classic account — P2P merchant, advert and order endpoints.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/p2p/merchantList` — Get P2P Merchant List
- `GET /api/v2/p2p/merchantInfo` — Get Merchant Information
- `GET /api/v2/p2p/advList` — Get Merchant Advertisement List
- `GET /api/v2/p2p/orderList` — Get Merchant P2P Orders

## Get P2P Merchant List

`GET /api/v2/p2p/merchantList`

Rate limit:10 requests/s (UID)

Get P2P merchant list

Operation ID: `classicP2pGetP2PMerchantList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| online | query | string |  | Whether online? <br><br>yes: online<br><br>no: offline |
| idLessThan | query | string |  | The minMerchantId returned from the previous query.<br><br>Returns data whose ID is less than the entry parameter. |
| limit | query | string |  | Number of queries<br><br>The default value is 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.merchantList | string[] |  | Merchant list |
| data.registerTime | string |  | Registration time |
| data.nickName | string |  | Alias |
| data.isOnline | string |  | Whether online |
| data.avgPaymentTime | string |  | Average payment time<br><br>(in minutes) |
| data.avgReleaseTime | string |  | Average time to release coins<br><br>(in minutes) |
| data.totalTrades | string |  | Total traded orders |
| data.totalBuy | string |  | Total number of purchase orders |
| data.totalSell | string |  | Total number of sell orders |
| data.totalCompletionRate | string |  | Total execution rate |
| data.trades30d | string |  | 30-day trading volume |
| data.sell30d | string |  | 30-day sell orders |
| data.buy30d | string |  | 30-day purchase orders |
| data.completionRate30d | string |  | 30-day close rate |
| data.minMerchantId | string |  | Returns the smallest merchantId in the result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681195810516,
  "data": {
    "merchantList": [
      {
        "registerTime": "1678674575000",
        "nickName": "test1",
        "isOnline": "no",
        "avgPaymentTime": "0",
        "avgReleaseTime": "0",
        "totalTrades": "0",
        "totalBuy": "0",
        "totalSell": "0",
        "totalCompletionRate": "0",
        "trades30d": "8",
        "sell30d": "4",
        "buy30d": "4",
        "completionRate30d": "0.8"
      }
    ],
    "minMerchantId": "1"
  }
}
```

## Get Merchant Information

`GET /api/v2/p2p/merchantInfo`

Frequency limit:10 times/1s (UID)

Get Merchant Information

Operation ID: `classicP2pGetMerchantInformation`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.registerTime | string |  | Registration time |
| data.nickName | string |  | Alias |
| data.merchantId | string |  | Merchant ID |
| data.kycStatus | string |  | KYC or not<br><br>yes<br><br>no |
| data.emailBindStatus | string |  | Email bound?<br><br>yes<br><br>no |
| data.mobileBindStatus | string |  | Phone number bound?<br><br>yes<br><br>no |
| data.email | string |  | Email |
| data.mobile | string |  | Phone number |
| data.avgPaymentTime | string |  | Average payment time in minutes |
| data.avgReleaseTime | string |  | Average coin release time in minutes |
| data.totalTrades | string |  | Total traded orders |
| data.totalBuy | string |  | Total number of purchase orders |
| data.totalSell | string |  | Total number of sell orders |
| data.totalCompletionRate | string |  | Total execution rate |
| data.trades30d | string |  | 30-day trading volume |
| data.sell30d | string |  | 30-day sell orders |
| data.buy30d | string |  | 30-day purchase orders |
| data.completionRate30d | string |  | 30-day close rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681194805204,
  "data": {
    "registerTime": "1672039640000",
    "nickName": "lz",
    "merchantId": "1",
    "avgPaymentTime": "172695",
    "avgReleaseTime": "33009",
    "totalTrades": "2",
    "totalBuy": "1",
    "totalSell": "0",
    "totalCompletionRate": "1",
    "trades30d": "12",
    "sell30d": "4",
    "buy30d": "8",
    "completionRate30d": "0.71",
    "kycStatus": "yes",
    "emailBindStatus": "yes",
    "mobileBindStatus": "yes",
    "email": "******@*****.com",
    "mobile": "18*34"
  }
}
```

## Get Merchant Advertisement List

`GET /api/v2/p2p/advList`

Frequency limit:10 times/1s (UID)

Get Merchant Advertisement List

Operation ID: `classicP2pGetP2PAdvList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string | 是 | Start time, Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string |  | End time, Unix millisecond timestamp, e.g. 1690196141868<br><br>Maximum interval between start time and end time is 90 days |
| idLessThan | query | string |  | The minAdvId returned from the previous query. Returns the data whose advId is less than the specified input parameter. |
| limit | query | string |  | Number of queries: Default: 20, max:20. |
| status | query | string | 是 | Advertisement order status<br><br>`online`: Online<br><br>`offline`: Offline<br><br>`editing`: Editing<br><br>`completed`: Completed |
| advNo | query | string |  | Advertisement order |
| side | query | string | 是 | TX type<br><br>buy: Buy<br><br>sell: Sell |
| coin | query | string | 是 | Digital currency |
| language | query | string |  | Language<br><br>zh-CN: Chinese<br><br>en-US: English |
| fiat | query | string | 是 | Fiat |
| orderBy | query | string |  | Sort Fields<br><br>createTime: Create time<br><br>price: Price<br><br>Descending, by createTime by default |
| payMethodId | query | string |  | Payment method id |
| sourceType | query | string |  | Query range<br><br>owner:query owner advertisement(default)<br><br>competitior:query other merchant advertisement<br><br>ownerAndCompetitior:query all advertisement |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.advList | object[] |  | Number of advertisement orders |
| data.advList[].advId | string |  | Advertisement order ID |
| data.advList[].advNo | string |  | Advertisement order number |
| data.advList[].side | string |  | TX type<br><br>sell<br><br>buy |
| data.advList[].advSize | string |  | Total number of advertisement orders |
| data.advList[].size | string |  | Filled quantity |
| data.advList[].coin | string |  | Coins such as BGB, USDT, BTC, ETH etc. |
| data.advList[].price | string |  | Price |
| data.advList[].coinPrecision | string |  | Currency precision, decimala |
| data.advList[].fiat | string |  | Fiat |
| data.advList[].fiatPrecision | string |  | Fiat decimals |
| data.advList[].fiatSymbol | string |  | Currency symbol |
| data.advList[].status | string |  | Advertisement order status<br><br>`online`: Online<br><br>`offline`: Offline<br><br>`editing`: Editing<br><br>`completed`: Completed |
| data.advList[].hide | string |  | Hide the advertisement order or not<br><br>yes: Hide<br><br>no: not hide |
| data.advList[].maxTradeAmount | string |  | Maximum order quantity |
| data.advList[].minTradeAmount | string |  | Minimum order quantity |
| data.advList[].payDuration | string |  | Time period for payment after placing an order, min |
| data.advList[].turnoverNum | string |  | Total trading amount |
| data.advList[].turnoverRate | string |  | Close rate |
| data.advList[].label | string |  | Note |
| data.advList[].ctime | string |  | Creation time, Unix millisecond timestamps |
| data.advList[].utime | string |  | Update time, Unix millisecond timestamps |
| data.advList[].userLimitList | object |  | Upper limit of the advertiser order restricted user |
| data.advList[].userLimitList.minCompleteNum | string |  | Minimum number of completed user orders |
| data.advList[].userLimitList.maxCompleteNum | string |  | Maximum number of completed user orders |
| data.advList[].userLimitList.placeOrderNum | string |  | Maximum number of orders a user can place under this advertisement |
| data.advList[].userLimitList.allowMerchantPlace | string |  | Whether to allow merchants to place orders<br><br>yes: allow<br><br>no: not allow |
| data.advList[].userLimitList.completeRate30d | string |  | 30-day close rate |
| data.advList[].userLimitList.country | string |  | Only people from these countries are allowed to place orders |
| data.advList[].paymentMethodList | object[] |  | Payment methods number |
| data.advList[].paymentMethodList[].paymentMethod | string |  | Payment name |
| data.advList[].paymentMethodList[].paymentId | string |  | Payment ID |
| data.advList[].paymentMethodList[].paymentInfo | object[] |  | Payment method detail information |
| data.advList[].merchantCertifiedList | object[] |  | Merchant authentication number |
| data.advList[].merchantCertifiedList[].imageUrl | string |  | Gold Merchant certification pictures |
| data.advList[].merchantCertifiedList[].desc | string |  | Gold Merchant certification parameter description |
| data.minAdvId | string |  | Returns the minimum advId of the result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696930053072,
  "data": {
    "advList": [
      {
        "advId": "1",
        "advNo": "1",
        "side": "buy",
        "advSize": "0.6",
        "size": "0",
        "coin": "BTC",
        "price": "155570.9",
        "coinPrecision": "36",
        "fiat": "CNY",
        "fiatPrecision": "2",
        "fiatSymbol": "￥",
        "status": "online",
        "hide": "no",
        "maxTradeAmount": "93342.54",
        "minTradeAmount": "100",
        "payDuration": "4",
        "turnoverNum": "8",
        "turnoverRate": "1.00",
        "label": null,
        "userLimitList": {
          "minCompleteNum": "0",
          "maxCompleteNum": "0",
          "placeOrderNum": "0",
          "allowMerchantPlace": "no",
          "completeRate30d": "0",
          "country": ""
        },
        "paymentMethodList": [
          {
            "paymentMethod": "Bank Card",
            "paymentId": "11",
            "paymentInfo": [
              {
                "name": "Bank Card",
                "required": true,
                "type": "txt"
              }
            ]
          },
          {
            "paymentMethod": "WeChat",
            "paymentId": "12",
            "paymentInfo": [
              {
                "name": "Payment code",
                "required": true,
                "type": "file"
              },
              {
                "name": "WeChatAccount",
                "required": true,
                "type": "txt"
              }
            ]
          },
          {
            "paymentMethod": "Alipay",
            "paymentId": "13",
            "paymentInfo": [
              {
                "name": "AlipayAccount",
                "required": true,
                "type": "txt"
              },
              {
                "name": "Payment code",
                "required": true,
                "type": "file"
              }
            ]
          }
        ],
        "merchantCertifiedList": [],
        "utime": "1696733724267",
        "ctime": "1696733724267"
      }
    ],
    "minAdvId": "1"
  }
}
```

## Get Merchant P2P Orders

`GET /api/v2/p2p/orderList`

Frequency limit:10 times/1s (UID)

Merchant queries P2P orders

Operation ID: `classicP2pGetP2POrderList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time, Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string |  | End time, Unix millisecond timestamp, e.g. 1690196141868<br><br>Maximum interval between start time and end time is 90 days |
| idLessThan | query | string |  | The minOrderId returned from the previous query. Returns p2p order data less than the specified entry parameter. |
| limit | query | string |  | Number of queries, default 100 |
| status | query | string |  | P2P order status<br><br>pending_pay: pending payment<br><br>Paid: coins to be released<br><br>Appeal: Appeal in progress<br><br>Completed: Completed<br><br>cancelled: cancelled |
| advNo | query | string |  | Advertisement order number |
| side | query | string |  | TX type<br><br>buy: Buy<br><br>sell: Sell |
| coin | query | string |  | Digital currency name, e.g. USDT |
| language | query | string |  | Language<br><br>zh-CN: Chinese<br><br>en-US: English |
| fiat | query | string |  | Fiat currency name, e.g. USD |
| orderNo | query | string |  | Order no. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderList | object[] |  | Order number |
| data.orderList[].orderId | string |  | ID |
| data.orderList[].orderNo | string |  | Order no. |
| data.orderList[].advNo | string |  | Advertisement order number |
| data.orderList[].side | string |  | Types: buy/sell |
| data.orderList[].count | string |  | Amount |
| data.orderList[].coin | string |  | Fiat Currency |
| data.orderList[].price | string |  | Price |
| data.orderList[].fiat | string |  | Fiat |
| data.orderList[].withdrawTime | string |  | Time of withdrawal of this order |
| data.orderList[].representTime | string |  | Appeal time |
| data.orderList[].releaseTime | string |  | Coin release time |
| data.orderList[].paymentTime | string |  | Repayment time |
| data.orderList[].amount | string |  | Order amount |
| data.orderList[].status | string |  | P2P order status |
| data.orderList[].buyerRealName | string |  | Buyer name |
| data.orderList[].sellerRealName | string |  | Seller name |
| data.orderList[].ctime | string |  | Creation time, Unix millisecond timestamps |
| data.orderList[].utime | string |  | Update time, Unix millisecond timestamps |
| data.orderList[].paymentInfo | object |  | Payment Info |
| data.orderList[].paymentInfo.paymethodName | string |  | Payment method name |
| data.orderList[].paymentInfo.paymethodId | string |  | Payment method ID |
| data.orderList[].paymentInfo.paymethodInfo | object[] |  | Payment method details |
| data.orderList[].paymentInfo.paymethodInfo[].name | string |  | Payment detail name |
| data.orderList[].paymentInfo.paymethodInfo[].required | string |  | Required or not: yes/no |
| data.orderList[].paymentInfo.paymethodInfo[].type | string |  | type, number/file. Ignore this parameter |
| data.orderList[].paymentInfo.paymethodInfo[].value | string |  | Payment information value |
| data.minOrderId | string |  | Returns the minimum orderId of record. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681201761390,
  "data": {
    "orderList": [
      {
        "orderId": "1",
        "orderNo": "1",
        "advNo": "1",
        "price": "1",
        "count": "11",
        "side": "buy",
        "fiat": "USD",
        "coin": "USDT",
        "withdrawTime": "",
        "representTime": "",
        "paymentTime": "",
        "releaseTime": "",
        "amount": "11",
        "buyerRealName": "",
        "sellerRealName": "兰州",
        "status": "cancelled",
        "paymentInfo": {
          "paymethodName": "paypal",
          "paymethodId": "1",
          "paymethodInfo": [
            {
              "name": "繁体中文",
              "required": "yes",
              "type": "number",
              "value": "11****"
            },
            {
              "name": "繁体中文",
              "required": "yes",
              "type": "file",
              "value": "http://abc.x.com/otc/images/20230116/1.jpg"
            }
          ]
        },
        "utime": "1696732368875",
        "ctime": "1681111722251"
      }
    ],
    "minOrderId": "1"
  }
}
```


---

经典账户 — P2P 商家、广告与订单相关接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/p2p/merchantList` — 获取p2p商家列表
- `GET /api/v2/p2p/merchantInfo` — 商家查询自己信息
- `GET /api/v2/p2p/advList` — 获取p2p商家广告单列表
- `GET /api/v2/p2p/orderList` — 商家获取P2P订单

## 获取p2p商家列表

`GET /api/v2/p2p/merchantList`

限速规则 10次/1s (UID)

获取p2p商家列表

Operation ID: `classicP2pGetP2PMerchantList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| online | query | string |  | 是否在线 <br><br>yes在线<br><br>no不在线 |
| idLessThan | query | string |  | 上一次查询返回的minMerchantId，<br><br>返回ID小于该入参的数据 |
| limit | query | string |  | 查询条数<br><br>默认值为100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.merchantList | string[] |  | 商家列表 |
| data.registerTime | string |  | 注册时间 |
| data.nickName | string |  | 昵称 |
| data.isOnline | string |  | 是否在线 |
| data.avgPaymentTime | string |  | 平均支付时间<br><br>单位为分钟 |
| data.avgReleaseTime | string |  | 平均放币时间<br><br>单位为分钟 |
| data.totalTrades | string |  | 总交易订单数 |
| data.totalBuy | string |  | 总买单数 |
| data.totalSell | string |  | 总卖单数 |
| data.totalCompletionRate | string |  | 总成交率 |
| data.trades30d | string |  | 30日总成交数 |
| data.sell30d | string |  | 30日卖单数 |
| data.buy30d | string |  | 30日买单数 |
| data.completionRate30d | string |  | 30日成交率 |
| data.minMerchantId | string |  | 返回结果中的最小merchantId |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681195810516,
  "data": {
    "merchantList": [
      {
        "registerTime": "1678674575000",
        "nickName": "test1",
        "isOnline": "no",
        "avgPaymentTime": "0",
        "avgReleaseTime": "0",
        "totalTrades": "0",
        "totalBuy": "0",
        "totalSell": "0",
        "totalCompletionRate": "0",
        "trades30d": "8",
        "sell30d": "4",
        "buy30d": "4",
        "completionRate30d": "0.8"
      }
    ],
    "minMerchantId": "1"
  }
}
```

## 商家查询自己信息

`GET /api/v2/p2p/merchantInfo`

限速规则 10次/1s (UID)

商家查询自己信息

Operation ID: `classicP2pGetMerchantInformation`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.registerTime | string |  | 注册时间 |
| data.nickName | string |  | 昵称 |
| data.merchantId | string |  | 商家ID |
| data.kycStatus | string |  | 是否KYC<br><br>yes<br><br>no |
| data.emailBindStatus | string |  | 是否绑定email<br><br>yes<br><br>no |
| data.mobileBindStatus | string |  | 是否绑定手机号<br><br>yes<br><br>no |
| data.email | string |  | 邮箱 |
| data.mobile | string |  | 手机号 |
| data.avgPaymentTime | string |  | 平均支付时间, 单位为分钟 |
| data.avgReleaseTime | string |  | 平均放币时间, 单位为分钟 |
| data.totalTrades | string |  | 总交易订单数 |
| data.totalBuy | string |  | 总买单数 |
| data.totalSell | string |  | 总卖单数 |
| data.totalCompletionRate | string |  | 总成交率 |
| data.trades30d | string |  | 30日总成交数 |
| data.sell30d | string |  | 30日卖单数 |
| data.buy30d | string |  | 30日买单数 |
| data.completionRate30d | string |  | 30日成交率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681194805204,
  "data": {
    "registerTime": "1672039640000",
    "nickName": "lz",
    "merchantId": "1",
    "avgPaymentTime": "172695",
    "avgReleaseTime": "33009",
    "totalTrades": "2",
    "totalBuy": "1",
    "totalSell": "0",
    "totalCompletionRate": "1",
    "trades30d": "12",
    "sell30d": "4",
    "buy30d": "8",
    "completionRate30d": "0.71",
    "kycStatus": "yes",
    "emailBindStatus": "yes",
    "mobileBindStatus": "yes",
    "email": "**@**.com",
    "mobile": "18*34"
  }
}
```

## 获取p2p商家广告单列表

`GET /api/v2/p2p/advList`

限速规则 10次/1s (UID)

获取p2p商家广告单列表

Operation ID: `classicP2pGetP2PAdvList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string | 是 | 查询开始时间 (仅限查询90天内数据) |
| endTime | query | string |  | 查询结束时间 |
| idLessThan | query | string |  | 上一次查询返回的minMerchantId，<br><br>返回ID小于该入参的数据 |
| limit | query | string |  | 查询条数<br><br>默认值为20 ，最大值为20 |
| status | query | string | 是 | 广告单状态<br><br>`online` 上架<br><br>`offline` 下架<br><br>`completed` 完成<br><br>`editing`  编辑中 |
| advNo | query | string |  | 广告单号 |
| side | query | string | 是 | buy/sell |
| coin | query | string | 是 | 币种，如USDT |
| language | query | string |  | zh-CN/en-US |
| fiat | query | string | 是 | 法币 |
| orderBy | query | string |  | 排序字段(desc)：createTime/price 默认createTime |
| payMethodId | query | string |  | 支付方式id |
| sourceType | query | string |  | 查询范围<br><br>owner:查询自己的广告单(默认)<br><br>competitior:查询其他商家的广告单<br><br>ownerAndCompetitior:查询所有广告单 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.advList | object[] |  | 查询响应array |
| data.advList[].advId | string |  | ID |
| data.advList[].advNo | string |  | 广告单号 |
| data.advList[].side | string |  | 买/卖类型：sell/buy |
| data.advList[].advSize | string |  | 广告单总数量 |
| data.advList[].size | string |  | 已成交数量 |
| data.advList[].coin | string |  | 币(BGB,USDT,BTC,ETH) |
| data.advList[].price | string |  | 价格(USD, JPY, CNY) |
| data.advList[].coinPrecision | string |  | 币的小数位 |
| data.advList[].fiat | string |  | 法币名称 |
| data.advList[].fiatPrecision | string |  | 法币小数位 |
| data.advList[].fiatSymbol | string |  | 法币符号 |
| data.advList[].status | string |  | 广告单状态<br><br>`online` 上架<br><br>`offline` 下架<br><br>`completed` 完成<br><br>`editing`  编辑中 |
| data.advList[].hide | string |  | 广告单是否隐藏: yes/no |
| data.advList[].maxTradeAmount | string |  | 最大下单数量 |
| data.advList[].minTradeAmount | string |  | 最小下单数量 |
| data.advList[].payDuration | string |  | 下单后支付时间期限, min |
| data.advList[].turnoverNum | string |  | 商户 成单总数 |
| data.advList[].turnoverRate | string |  | 成交率 |
| data.advList[].label | string |  | 备注 |
| data.advList[].ctime | string |  | 创建时间, ms |
| data.advList[].utime | string |  | 最新修改时间, ms |
| data.advList[].userLimitList | object |  | 广告单限制：以下规则用户禁止下单 |
| data.advList[].userLimitList.minCompleteNum | string |  | 用户完成下单最小数量 |
| data.advList[].userLimitList.maxCompleteNum | string |  | 用户完成下单最大数量 |
| data.advList[].userLimitList.placeOrderNum | string |  | 用户在此广告单下最多可以下多少单 |
| data.advList[].userLimitList.allowMerchantPlace | string |  | 是否允许商家下单 |
| data.advList[].userLimitList.completeRate30d | string |  | 30日成交率 |
| data.advList[].userLimitList.country | string |  | 适用国家 |
| data.advList[].paymentMethodList | object[] |  | 支付方式列表 |
| data.advList[].paymentMethodList[].paymentMethod | string |  | 支付名称 |
| data.advList[].paymentMethodList[].paymentId | string |  | 支付ID |
| data.advList[].paymentMethodList[].paymentInfo | object[] |  | 支付方式详情信息 |
| data.advList[].merchantCertifiedList | object[] |  | 商家认证 |
| data.advList[].merchantCertifiedList[].imageUrl | string |  | 金牌商家认证图片 |
| data.advList[].merchantCertifiedList[].desc | string |  | 金牌商家认证描述 |
| data.minAdvId | string |  | 返回结果的最小advId |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696930053072,
  "data": {
    "advList": [
      {
        "advId": "1",
        "advNo": "1",
        "side": "buy",
        "advSize": "0.6",
        "size": "0",
        "coin": "BTC",
        "price": "155570.9",
        "coinPrecision": "36",
        "fiat": "CNY",
        "fiatPrecision": "2",
        "fiatSymbol": "￥",
        "status": "online",
        "hide": "no",
        "maxTradeAmount": "93342.54",
        "minTradeAmount": "100",
        "payDuration": "4",
        "turnoverNum": "8",
        "turnoverRate": "1.00",
        "label": null,
        "userLimitList": {
          "minCompleteNum": "0",
          "maxCompleteNum": "0",
          "placeOrderNum": "0",
          "allowMerchantPlace": "no",
          "completeRate30d": "0",
          "country": ""
        },
        "paymentMethodList": [
          {
            "paymentMethod": "Bank Card",
            "paymentId": "11",
            "paymentInfo": [
              {
                "name": "Bank Card",
                "required": true,
                "type": "txt"
              }
            ]
          },
          {
            "paymentMethod": "WeChat",
            "paymentId": "12",
            "paymentInfo": [
              {
                "name": "Payment code",
                "required": true,
                "type": "file"
              },
              {
                "name": "WeChatAccount",
                "required": true,
                "type": "txt"
              }
            ]
          },
          {
            "paymentMethod": "Alipay",
            "paymentId": "13",
            "paymentInfo": [
              {
                "name": "AlipayAccount",
                "required": true,
                "type": "txt"
              },
              {
                "name": "Payment code",
                "required": true,
                "type": "file"
              }
            ]
          }
        ],
        "merchantCertifiedList": [],
        "utime": "1696733724267",
        "ctime": "1696733724267"
      }
    ],
    "minAdvId": "1"
  }
}
```

## 商家获取P2P订单

`GET /api/v2/p2p/orderList`

限速规则 10次/1s (UID)

商家获取P2P订单

Operation ID: `classicP2pGetP2POrderList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 查询开始时间 (仅限查询90天内数据) |
| endTime | query | string |  | 查询结束时间 |
| idLessThan | query | string |  | 上一次查询返回的minMerchantId，<br><br>返回ID小于该入参的数据 |
| limit | query | string |  | 查询条数<br><br>默认值为100 |
| status | query | string |  | 广告单状态<br><br>待付款:pending_pay<br><br>已付款待放币:paid<br><br>申诉中:appeal<br><br>已完成:completed<br><br>已取消:cancelled |
| advNo | query | string |  | 广告单号 |
| side | query | string |  | buy/sell |
| coin | query | string |  | 币种，如USDT |
| language | query | string |  | zh-CN/en-US |
| fiat | query | string |  | 法币 |
| orderNo | query | string |  | 订单号 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderList | object[] |  | 查询响应array |
| data.orderList[].orderId | string |  | ID |
| data.orderList[].orderNo | string |  | 订单号 |
| data.orderList[].advNo | string |  | 广告单号 |
| data.orderList[].side | string |  | 买/卖类型：buy/sell |
| data.orderList[].count | string |  | 下单数量 |
| data.orderList[].coin | string |  | 币 |
| data.orderList[].price | string |  | 价格 |
| data.orderList[].fiat | string |  | 法币名称 |
| data.orderList[].withdrawTime | string |  | 本条订单资金提现时间 |
| data.orderList[].representTime | string |  | 申诉时间 |
| data.orderList[].releaseTime | string |  | 放币时间 |
| data.orderList[].paymentTime | string |  | 付款时间 |
| data.orderList[].amount | string |  | 下单金额 |
| data.orderList[].status | string |  | 广告单状态<br><br>待付款:pending_pay<br><br>已付款待放币:paid<br><br>申诉中:appeal<br><br>已完成:completed<br><br>已取消:cancelled |
| data.orderList[].buyerRealName | string |  | 买家姓名 |
| data.orderList[].sellerRealName | string |  | 卖家姓名 |
| data.orderList[].ctime | string |  | 创建时间 |
| data.orderList[].utime | string |  | 最新修改时间 |
| data.orderList[].paymentInfo | object |  | 支持的支付方式 |
| data.orderList[].paymentInfo.paymethodName | string |  | 支付方式名称 |
| data.orderList[].paymentInfo.paymethodId | string |  | 支付方式ID |
| data.orderList[].paymentInfo.paymethodInfo | object[] |  | 支付方式详情 |
| data.orderList[].paymentInfo.paymethodInfo[].name | string |  | 支付详情名称 |
| data.orderList[].paymentInfo.paymethodInfo[].required | string |  | 是否必须: yes/no |
| data.orderList[].paymentInfo.paymethodInfo[].type | string |  | 类型, number/file, 请忽略本参数 |
| data.orderList[].paymentInfo.paymethodInfo[].value | string |  | 支付信息值 |
| data.minOrderId | string |  | 返回记录的最小orderId |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681201761390,
  "data": {
    "orderList": [
      {
        "orderId": "1",
        "orderNo": "1",
        "advNo": "1",
        "price": "1",
        "count": "11",
        "side": "buy",
        "fiat": "USD",
        "coin": "USDT",
        "withdrawTime": "",
        "representTime": "",
        "paymentTime": "",
        "releaseTime": "",
        "amount": "11",
        "buyerRealName": "",
        "sellerRealName": "兰州",
        "status": "cancelled",
        "paymentInfo": {
          "paymethodName": "paypal",
          "paymethodId": "3",
          "paymethodInfo": [
            {
              "name": "繁体中文",
              "required": "yes",
              "type": "number",
              "value": "11****"
            },
            {
              "name": "繁体中文",
              "required": "yes",
              "type": "file",
              "value": "http://qrc.bitgetapp.com/otc/images/20230116/498ab1b8-3ba6-44bd-9570-b3e5c118233f.jpg"
            }
          ]
        },
        "utime": "1696732368875",
        "ctime": "1681111722251"
      }
    ],
    "minOrderId": "1"
  }
}
```