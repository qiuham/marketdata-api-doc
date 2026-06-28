---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/spot
api_type: Trading
updated_at: 2026-05-27 20:17:50.111088
---

# Spot

现货交易

##  查询所有币种信息

GET`/spot/currencies`

GET `/spot/currencies`

_查询所有币种信息_

一个币种对应多个链时可以通过 `chains` 字段查询多链的信息，比如链的充提状态、标识等

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [Currency]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» currency | string | 币种符号  
» name | string | 币种名称  
» delisted | boolean | 是否下架  
» withdraw_disabled | boolean | 是否暂停提现（废弃）  
» withdraw_delayed | boolean | 提现是否存在延迟（废弃）  
» deposit_disabled | boolean | 是否暂停充值（废弃）  
» trade_disabled | boolean | 是否暂停交易  
» fixed_rate | string | 固定交易手续费率。仅限固定交易费率的币种，普通币种该字段无效  
» chain | string | 币对应的主链  
» chains | array | 币对应的所有链  
»» SpotCurrencyChain | object |   
»»» name | string | 链名  
»»» addr | string | token地址  
»»» withdraw_disabled | boolean | 是否暂停提现  
»»» withdraw_delayed | boolean | 提现是否存在延迟  
»»» deposit_disabled | boolean | 是否暂停充值  
»» total_supply | string | 币种总供应量  
»» market_cap | string | 币种市值  
»» category | array | 币种分类  
  
\- stocks: 股票  
\- metals: 金属  
\- indices: 指数  
\- forex: 外汇  
\- commodities: 大宗商品  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/currencies'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/currencies \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency": "GT",
        "name": "GateToken",
        "delisted": false,
        "withdraw_disabled": false,
        "withdraw_delayed": false,
        "deposit_disabled": false,
        "trade_disabled": false,
        "chain": "GT",
        "chains": [
          {
            "name": "GT",
            "addr": "",
            "withdraw_disabled": false,
            "withdraw_delayed": false,
            "deposit_disabled": false
          },
          {
            "name": "ETH",
            "withdraw_disabled": false,
            "withdraw_delayed": false,
            "deposit_disabled": false,
            "addr": "0xE66747a101bFF2dBA3697199DCcE5b743b454759"
          },
          {
            "name": "GTEVM",
            "withdraw_disabled": false,
            "withdraw_delayed": false,
            "deposit_disabled": false,
            "addr": ""
          }
        ],
        "total_supply": "2100000",
        "market_cap": "18880000",
        "category": []
      }
    ]
    

##  查询单个币种信息

GET`/spot/currencies/{currency}`

GET `/spot/currencies/{currency}`

_查询单个币种信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | URL | any | 是 | 币种名称  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | Currency  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» currency | string | 币种符号  
» name | string | 币种名称  
» delisted | boolean | 是否下架  
» withdraw_disabled | boolean | 是否暂停提现（废弃）  
» withdraw_delayed | boolean | 提现是否存在延迟（废弃）  
» deposit_disabled | boolean | 是否暂停充值（废弃）  
» trade_disabled | boolean | 是否暂停交易  
» fixed_rate | string | 固定交易手续费率。仅限固定交易费率的币种，普通币种该字段无效  
» chain | string | 币对应的主链  
» chains | array | 币对应的所有链  
»» SpotCurrencyChain | object |   
»»» name | string | 链名  
»»» addr | string | token地址  
»»» withdraw_disabled | boolean | 是否暂停提现  
»»» withdraw_delayed | boolean | 提现是否存在延迟  
»»» deposit_disabled | boolean | 是否暂停充值  
»» total_supply | string | 币种总供应量  
»» market_cap | string | 币种市值  
»» category | array | 币种分类  
  
\- stocks: 股票  
\- metals: 金属  
\- indices: 指数  
\- forex: 外汇  
\- commodities: 大宗商品  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/currencies/GT'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/currencies/GT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "currency": "GT",
      "name": "GateToken",
      "delisted": false,
      "withdraw_disabled": false,
      "withdraw_delayed": false,
      "deposit_disabled": false,
      "trade_disabled": false,
      "chain": "GT",
      "chains": [
        {
          "name": "GT",
          "addr": "",
          "withdraw_disabled": false,
          "withdraw_delayed": false,
          "deposit_disabled": false
        },
        {
          "name": "ETH",
          "withdraw_disabled": false,
          "withdraw_delayed": false,
          "deposit_disabled": false,
          "addr": "0xE66747a101bFF2dBA3697199DCcE5b743b454759"
        },
        {
          "name": "GTEVM",
          "withdraw_disabled": false,
          "withdraw_delayed": false,
          "deposit_disabled": false,
          "addr": ""
        }
      ],
      "total_supply": "2100000",
      "market_cap": "18880000",
      "category": []
    }
    

##  查询支持的所有交易对

GET`/spot/currency_pairs`

GET `/spot/currency_pairs`

_查询支持的所有交易对_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询到所有交易对 | [CurrencyPair]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [现货交易对]  
» _None_ | CurrencyPair | 现货交易对  
»» id | string | 交易对  
»» base | string | 交易货币  
»» base_name | string | 交易货币名称  
»» quote | string | 计价货币  
»» quote_name | string | 计价货币名称  
»» fee | string | 交易费率(已废弃)  
»» min_base_amount | string | 交易货币最低交易数量，null 表示无限制  
»» min_quote_amount | string | 计价货币最低交易数量，null 表示无限制  
»» max_base_amount | string | 交易货币最大交易数量，null 表示无限制  
»» max_quote_amount | string | 计价货币最大交易数量，null 表示无限制  
»» amount_precision | integer | 数量精度  
»» precision | integer | 价格精度  
»» trade_status | string | 交易状态  
  
\- untradable: 不可交易  
\- buyable: 可买  
\- sellable: 可卖  
\- tradable: 买卖均可交易  
»» sell_start | integer(int64) | 允许卖出时间，秒级 Unix 时间戳  
»» buy_start | integer(int64) | 允许买入时间，秒级 Unix 时间戳  
»» delisting_time | integer(int64) | 预计下架时间，秒级 Unix 时间戳  
»» type | string | 交易对类型，normal:常规, premarket:盘前  
»» trade_url | string | 交易链接  
»» st_tag | boolean | 币对是否在ST风险评估中，false - 否，true - 是  
»» up_rate | string | 报价最大涨幅百分比  
»» down_rate | string | 报价最大跌幅百分比  
»» slippage | string | 现货市价下单支持的最大滑点比率，以下单时的市场最新价格为基准计算（示例：0.03即3%）  
»» market_order_max_stock | string | 市价单最大下单数量  
»» market_order_max_money | string | 市价单最大下单金额  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
trade_status | untradable  
trade_status | buyable  
trade_status | sellable  
trade_status | tradable  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/currency_pairs'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/currency_pairs \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": "ETH_USDT",
        "base": "ETH",
        "base_name": "Ethereum",
        "quote": "USDT",
        "quote_name": "Tether",
        "fee": "0.2",
        "min_base_amount": "0.001",
        "min_quote_amount": "1.0",
        "max_base_amount": "10000",
        "max_quote_amount": "10000000",
        "amount_precision": 3,
        "precision": 6,
        "trade_status": "tradable",
        "sell_start": 1516378650,
        "buy_start": 1516378650,
        "delisting_time": 0,
        "trade_url": "https://www.gate.io/trade/ETH_USDT",
        "st_tag": false,
        "up_rate": "0.05",
        "down_rate": "0.02",
        "slippage": "0.05",
        "max_market_order_stock": "100000",
        "max_market_order_money": "1000000"
      }
    ]
    

##  查询单个交易对详情

GET`/spot/currency_pairs/{currency_pair}`

GET `/spot/currency_pairs/{currency_pair}`

_查询单个交易对详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | URL | string | 是 | 交易对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | CurrencyPair  
  
### 返回格式

状态码 **200**

_现货交易对_

名称 | 类型 | 描述  
---|---|---  
» id | string | 交易对  
» base | string | 交易货币  
» base_name | string | 交易货币名称  
» quote | string | 计价货币  
» quote_name | string | 计价货币名称  
» fee | string | 交易费率(已废弃)  
» min_base_amount | string | 交易货币最低交易数量，null 表示无限制  
» min_quote_amount | string | 计价货币最低交易数量，null 表示无限制  
» max_base_amount | string | 交易货币最大交易数量，null 表示无限制  
» max_quote_amount | string | 计价货币最大交易数量，null 表示无限制  
» amount_precision | integer | 数量精度  
» precision | integer | 价格精度  
» trade_status | string | 交易状态  
  
\- untradable: 不可交易  
\- buyable: 可买  
\- sellable: 可卖  
\- tradable: 买卖均可交易  
» sell_start | integer(int64) | 允许卖出时间，秒级 Unix 时间戳  
» buy_start | integer(int64) | 允许买入时间，秒级 Unix 时间戳  
» delisting_time | integer(int64) | 预计下架时间，秒级 Unix 时间戳  
» type | string | 交易对类型，normal:常规, premarket:盘前  
» trade_url | string | 交易链接  
» st_tag | boolean | 币对是否在ST风险评估中，false - 否，true - 是  
» up_rate | string | 报价最大涨幅百分比  
» down_rate | string | 报价最大跌幅百分比  
» slippage | string | 现货市价下单支持的最大滑点比率，以下单时的市场最新价格为基准计算（示例：0.03即3%）  
» market_order_max_stock | string | 市价单最大下单数量  
» market_order_max_money | string | 市价单最大下单金额  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
trade_status | untradable  
trade_status | buyable  
trade_status | sellable  
trade_status | tradable  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/currency_pairs/ETH_BTC'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/currency_pairs/ETH_BTC \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "id": "ETH_USDT",
      "base": "ETH",
      "base_name": "Ethereum",
      "quote": "USDT",
      "quote_name": "Tether",
      "fee": "0.2",
      "min_base_amount": "0.001",
      "min_quote_amount": "1.0",
      "max_base_amount": "10000",
      "max_quote_amount": "10000000",
      "amount_precision": 3,
      "precision": 6,
      "trade_status": "tradable",
      "sell_start": 1516378650,
      "buy_start": 1516378650,
      "delisting_time": 0,
      "trade_url": "https://www.gate.io/trade/ETH_USDT",
      "st_tag": false,
      "up_rate": "0.05",
      "down_rate": "0.02",
      "slippage": "0.05",
      "max_market_order_stock": "100000",
      "max_market_order_money": "1000000"
    }
    

##  获取交易对 ticker 信息

GET`/spot/tickers`

GET `/spot/tickers`

_获取交易对 ticker 信息_

如果指定 `currency_pair` 则只查询该交易对，否则返回全部信息

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 交易对  
timezone | 请求参数 | string | 否 | 时区  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
timezone | utc0  
timezone | utc8  
timezone | all  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | [Ticker]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» currency_pair | string | 交易对  
» last | string | 最新成交价  
» lowest_ask | string | 最新卖方最低价  
» lowest_size | string | 最新卖方最低价数量；批量查询时不存在；单个查询时存在,如果没有数据时为空  
» highest_bid | string | 最新买方最高价  
» highest_size | string | 最新买方最高价数量；批量查询时不存在；单个查询时存在,如果没有数据时为空  
» change_percentage | string | 最近24h涨跌百分比，跌用负数标识，如 -7.45  
» change_utc0 | string | utc0时区，最近24h涨跌百分比，跌用负数标识，如 -7.45  
» change_utc8 | string | utc8时区，最近24h涨跌百分比，跌用负数标识，如 -7.45  
» base_volume | string | 最近24h交易货币成交量  
» quote_volume | string | 最近24h计价货币成交量  
» high_24h | string | 24小时最高价  
» low_24h | string | 24小时最低价  
» etf_net_value | string | ETF 净值  
» etf_pre_net_value | string|null | ETF 前一再平衡点净值  
» etf_pre_timestamp | integer(int64)|null | ETF 前一再平衡时间  
» etf_leverage | string|null | ETF 当前杠杆率  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/tickers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/tickers \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency_pair": "BTC3L_USDT",
        "last": "2.46140352",
        "lowest_ask": "2.477",
        "highest_bid": "2.4606821",
        "change_percentage": "-8.91",
        "change_utc0": "-8.91",
        "change_utc8": "-8.91",
        "base_volume": "656614.0845820589",
        "quote_volume": "1602221.66468375534639404191",
        "high_24h": "2.7431",
        "low_24h": "1.9863",
        "etf_net_value": "2.46316141",
        "etf_pre_net_value": "2.43201848",
        "etf_pre_timestamp": 1611244800,
        "etf_leverage": "2.2803019447281203"
      }
    ]
    

##  获取市场深度信息

GET`/spot/order_book`

GET `/spot/order_book`

_获取市场深度信息_

市场深度买单会按照价格从高到低排序，卖单反之

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 是 | 交易对  
interval | 请求参数 | string | 否 | 合并深度指定的价格精度，0 为不合并，不指定则默认为 0  
limit | 请求参数 | integer | 否 | 深度档位数量  
with_id | 请求参数 | boolean | 否 | 返回深度更新 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | OrderBook  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 深度更新ID。深度每发生一次变化，ID 就会更新一次。仅在 `with_id` 设置为 `true` 该值有效  
» current | integer(int64) | 接口数据返回 ms 时间戳  
» update | integer(int64) | 深度变化 ms 时间戳  
» asks | array | 卖方深度列表  
»» _None_ | array | 价格，数量的二元组  
» bids | array | 买方深度列表  
»» _None_ | array | 价格，数量的二元组  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/order_book'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/order_book?currency_pair=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "id": 123456,
      "current": 1623898993123,
      "update": 1623898993121,
      "asks": [
        [
          "1.52",
          "1.151"
        ],
        [
          "1.53",
          "1.218"
        ]
      ],
      "bids": [
        [
          "1.17",
          "201.863"
        ],
        [
          "1.16",
          "725.464"
        ]
      ]
    }
    

##  查询市场成交记录

GET`/spot/trades`

GET `/spot/trades`

_查询市场成交记录_

支持指定 `from` 和 `to` 按时间范围查询或基于 `last_id` 的翻页查询。默认按时间范围查询,查询范围为最近30天。

基于 `last_id` 翻页的查询方式不再推荐继续使用。如果指定 `last_id` ，时间范围查询参数会被忽略。

使用 limit&page分页功能检索数据时最大分页数量为100,000条，即 limit * (page - 1) <= 100000。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 是 | 交易对  
limit | 请求参数 | integer(int32) | 否 | 列表返回的最大数量。默认为100，最小1，最大1000。  
last_id | 请求参数 | string | 否 | 以上个列表的最后一条记录的 ID 作为下个列表的起点  
  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后，在结束之后 1 小时内可查，过期之后只能使用订单 ID  
reverse | 请求参数 | boolean | 否 | 是否获取小于 `last_id` 的数据，默认返回大于 `last_id` 的记录。  
  
设置该字段为 `true` 可以用来回溯市场成交记录，为 `false` 可以用来获取最新成交。  
  
当 `last_id` 未设置时，该字段无效。  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
page | 请求参数 | integer(int32) | 否 | 列表页数  
  
####  详细描述

**last_id** : 以上个列表的最后一条记录的 ID 作为下个列表的起点  
  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后，在结束之后 1 小时内可查，过期之后只能使用订单 ID

**reverse** : 是否获取小于 `last_id` 的数据，默认返回大于 `last_id` 的记录。  
  
设置该字段为 `true` 可以用来回溯市场成交记录，为 `false` 可以用来获取最新成交。  
  
当 `last_id` 未设置时，该字段无效。

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [Trade]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | string | 成交记录 ID  
» create_time | string | 成交时间  
» create_time_ms | string | 成交时间，毫秒精度  
» currency_pair | string | 交易货币对  
» side | string | 买单或者卖单  
» role | string | 交易角色，公共接口无此字段返回  
» amount | string | 交易数量  
» price | string | 交易价  
» order_id | string | 关联的订单 ID，公共接口无此字段返回  
» fee | string | 成交扣除的手续费，公共接口无此字段返回  
» fee_currency | string | 手续费计价单位，公共接口无此字段返回  
» point_fee | string | 手续费抵扣使用的点卡数量，公共接口无此字段返回  
» gt_fee | string | 手续费抵扣使用的 GT 数量，公共接口无此字段返回  
» amend_text | string | 用户修改订单时备注的信息  
» sequence_id | string | 单市场连续成交ID  
» text | string | 订单的自定义信息，公共接口无此字段返回  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
» deal | string | 本次成交总额  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
side | buy  
side | sell  
role | taker  
role | maker  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/trades'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/trades?currency_pair=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": "1232893232",
        "create_time": "1548000000",
        "create_time_ms": "1548000000123.456",
        "order_id": "4128442423",
        "side": "buy",
        "role": "maker",
        "amount": "0.15",
        "price": "0.03",
        "fee": "0.0005",
        "fee_currency": "ETH",
        "point_fee": "0",
        "gt_fee": "0",
        "sequence_id": "588018",
        "text": "t-test",
        "deal": "0.0045"
      }
    ]
    

##  市场 K 线图

GET`/spot/candlesticks`

GET `/spot/candlesticks`

_市场 K 线图_

K 线图数据单次请求最大返回 1000 个点，指定 from, to 和 interval 的时候注意点数不能过多

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 是 | 交易对  
limit | 请求参数 | integer | 否 | 指定数据点的数量，适用于取最近 `limit` 数量的数据，该字段与 `from`, `to` 互斥，如果指定了 `from`, `to` 中的任意字段，该字段会被拒绝  
from | 请求参数 | integer(int64) | 否 | 指定 K 线图的起始时间，注意时间格式为秒(s)精度的 Unix 时间戳，不指定则默认为 to - 100 * interval，即向前最多 100 个点的时间  
to | 请求参数 | integer(int64) | 否 | 指定 K 线图的结束时间，不指定则默认当前时间，注意时间格式为秒(s)精度的 Unix 时间戳  
interval | 请求参数 | string | 否 | 数据点的时间间隔， 注意 `30d` 代表的是自然月，不是按30天对齐  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
interval | 1s  
interval | 10s  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
interval | 4h  
interval | 8h  
interval | 1d  
interval | 7d  
interval | 30d  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | [[string]]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» _None_ | array | 每个时间粒度的 K 线数据，从左到右依次为:  
  
\- 秒(s)精度的 Unix 时间戳  
\- 计价货币交易额  
\- 收盘价  
\- 最高价  
\- 最低价  
\- 开盘价  
\- 基础货币交易量  
\- 窗口是否关闭，true 代表此段K线蜡烛图数据结束，false 代表此段K线蜡烛图数据尚未结束  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/candlesticks'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      [
        "1539852480",
        "971519.677",
        "0.0021724",
        "0.0021922",
        "0.0021724",
        "0.0021737",
        "true"
      ]
    ]
    

##  查询账户费率🔒 需要认证

GET`/spot/fee`

GET `/spot/fee`

_查询账户费率_

该接口已废弃，不再推荐使用，新的费率查询接口为 `/wallet/fee`

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 指定交易对获取更准确的费率设置。  
  
该字段可选，通常情况下所有交易对的费率设置是一样的。  
  
####  详细描述

**currency_pair** : 指定交易对获取更准确的费率设置。  
  
该字段可选，通常情况下所有交易对的费率设置是一样的。

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | SpotFee  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» user_id | integer(int64) | 用户 ID  
» taker_fee | string | taker 费率  
» maker_fee | string | maker 费率  
» rpi_maker_fee | string | RPI MM maker 费率  
» gt_discount | boolean | 是否开启 GT 抵扣折扣  
» gt_taker_fee | string | GT 抵扣 taker 费率，未开启 GT 抵扣则为 0  
» gt_maker_fee | string | GT 抵扣 maker 费率，未开启 GT 抵扣则为 0  
» loan_fee | string | 杠杆理财的费率  
» point_type | string | 点卡类型，0 - 初版点卡，1 - 202009 启用的新点卡  
» currency_pair | string | 交易对  
» debit_fee | integer | 费率抵扣类型 , 1 - GT抵扣 , 2 - 点卡抵扣 , 3 - VIP费率  
» rpi_mm | integer | RPI MM等级  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/fee'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/fee"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    {
      "user_id": 10001,
      "taker_fee": "0.002",
      "maker_fee": "0.002",
      "gt_discount": false,
      "gt_taker_fee": "0",
      "gt_maker_fee": "0",
      "loan_fee": "0.18",
      "point_type": "1",
      "currency_pair": "BTC_USDT",
      "debit_fee": 3
    }
    

##  批量查询账户费率🔒 需要认证

GET`/spot/batch_fee`

GET `/spot/batch_fee`

_批量查询账户费率_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pairs | 请求参数 | string | 是 | 一次请求最多只能查询 50 个交易对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | Inline  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» **additionalProperties** | SpotFee |   
»» user_id | integer(int64) | 用户 ID  
»» taker_fee | string | taker 费率  
»» maker_fee | string | maker 费率  
»» rpi_maker_fee | string | RPI MM maker 费率  
»» gt_discount | boolean | 是否开启 GT 抵扣折扣  
»» gt_taker_fee | string | GT 抵扣 taker 费率，未开启 GT 抵扣则为 0  
»» gt_maker_fee | string | GT 抵扣 maker 费率，未开启 GT 抵扣则为 0  
»» loan_fee | string | 杠杆理财的费率  
»» point_type | string | 点卡类型，0 - 初版点卡，1 - 202009 启用的新点卡  
»» currency_pair | string | 交易对  
»» debit_fee | integer | 费率抵扣类型 , 1 - GT抵扣 , 2 - 点卡抵扣 , 3 - VIP费率  
»» rpi_mm | integer | RPI MM等级  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/batch_fee'
    query_param = 'currency_pairs=BTC_USDT,ETH_USDT'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/batch_fee"
    query_param="currency_pairs=BTC_USDT,ETH_USDT"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    {
      "BTC_USDT": {
        "user_id": 10001,
        "taker_fee": "0.002",
        "maker_fee": "0.002",
        "rpi_maker_fee": "-0.00175",
        "gt_discount": false,
        "gt_taker_fee": "0",
        "gt_maker_fee": "0",
        "loan_fee": "0.18",
        "point_type": "1",
        "currency_pair": "BTC_USDT",
        "debit_fee": 3,
        "rpi_mm": 2
      },
      "GT_USDT": {
        "user_id": 10001,
        "taker_fee": "0.002",
        "maker_fee": "0.002",
        "rpi_maker_fee": "-0.00175",
        "gt_discount": false,
        "gt_taker_fee": "0",
        "gt_maker_fee": "0",
        "loan_fee": "0.18",
        "point_type": "1",
        "currency_pair": "GT_USDT",
        "debit_fee": 3,
        "rpi_mm": 2
      },
      "ETH_USDT": {
        "user_id": 10001,
        "taker_fee": "0.002",
        "maker_fee": "0.002",
        "rpi_maker_fee": "-0.00175",
        "gt_discount": false,
        "gt_taker_fee": "0",
        "gt_maker_fee": "0",
        "loan_fee": "0.18",
        "point_type": "1",
        "currency_pair": "ETH_USDT",
        "debit_fee": 3,
        "rpi_mm": 2
      }
    }
    

##  获取现货交易账户列表🔒 需要认证

GET`/spot/accounts`

GET `/spot/accounts`

_获取现货交易账户列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [SpotAccount]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» currency | string | 币种信息  
» available | string | 可用金额  
» locked | string | 冻结金额  
» update_id | integer(int64) | 版本号  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/accounts'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/accounts"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency": "ETH",
        "available": "968.8",
        "locked": "0",
        "update_id": 98
      }
    ]
    

##  查询现货账户变动历史🔒 需要认证

GET`/spot/account_book`

GET `/spot/account_book`

_查询现货账户变动历史_

记录查询时间范围不允许超过 30 天。

使用 limit&page分页功能检索数据时最大分页数量为100,000条，即 limit * (page - 1) <= 100000。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency | 请求参数 | string | 否 | 指定币种名称查询  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
type | 请求参数 | string | 否 | 指定账户变动类型查询，不指定则包含全部变动类型  
code | 请求参数 | string | 否 | 指定账户变动code查询，不指定则包含全部变动类型, 优先级高于 `type`  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [SpotAccountBook]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | string | 账户变更记录 ID  
» time | integer(int64) | 账户变更时间戳，毫秒单位  
» currency | string | 变更币种  
» change | string | 变更金额，正数表示转入，负数表示转出  
» balance | string | 变更后账户余额  
» type | string | 账户变更类型 , 已弃用（参考 code 账户变更编码）  
» code | string | 账户变更编码 , 详见资产流水编码  
» text | string | 附加信息  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/account_book'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/account_book"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": "123456",
        "time": 1547633726123,
        "currency": "BTC",
        "change": "1.03",
        "balance": "4.59316525194",
        "type": "margin_in",
        "text": "3815099"
      }
    ]
    

##  批量下单🔒 需要认证

POST`/spot/batch_orders`

POST `/spot/batch_orders`

_批量下单_

批量下单要求：

  1. 用户自定义订单信息 `text` 必须指定
  2. 每次只能下最多 4 个交易对且每个交易对只可批量下 10 个单
  3. 现货交易和杠杆交易不能同时存在，即同个请求里所有 `account` 必须一致

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | array[Order] | 是 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求执行完成 | [BatchOrder]  
  
### 返回格式

状态码 **200**

_包含多个订单对象，订单对象具体结构参考/spot/orders下单接口的结构_

名称 | 类型 | 描述  
---|---|---  
_None_ | array | 包含多个订单对象，订单对象具体结构参考/spot/orders下单接口的结构  
» _None_ | BatchOrder | 批量订单信息  
»» order_id | string | 订单 ID  
»» amend_text | string | 用户修改订单时备注的信息  
»» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
»» succeeded | boolean | 请求执行结果  
»» label | string | 错误标识，当订单成功时该字段为空串  
»» message | string | 错误详情，当订单成功时改字段为空串  
»» id | string | 订单 ID  
»» create_time | string | 订单创建时间  
»» update_time | string | 订单最新修改时间  
»» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
»» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
»» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
»» currency_pair | string | 交易货币对  
»» type | string | 订单类型   
  
\- limit : 限价单  
\- market : 市价单  
»» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
»» side | string | 买单或者卖单  
»» amount | string | 交易数量  
»» price | string | 交易价  
»» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
»» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
»» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
»» left | string | 交易货币未成交数量  
»» filled_amount | string | 交易货币已成交数量  
»» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
»» filled_total | string | 已成交总金额  
»» avg_deal_price | string | 平均成交价  
»» fee | string | 成交扣除的手续费  
»» fee_currency | string | 手续费计价单位  
»» point_fee | string | 手续费抵扣使用的点卡数量  
»» gt_fee | string | 手续费抵扣使用的 GT 数量  
»» gt_discount | boolean | 是否开启GT抵扣  
»» rebated_fee | string | 返还的手续费  
»» rebated_fee_currency | string | 返还手续费计价单位  
»» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
»» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回`-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
»» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
»» stop_profit | object | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»»» trigger_price | string | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»»» order_price | string | 止盈委托价  
»» stop_loss | object | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»»» trigger_price | string | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»»» order_price | string | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
account | spot  
account | margin  
account | cross_margin  
account | unified  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/batch_orders'
    query_param = ''
    body='[{"text":"t-abc123","currency_pair":"BTC_USDT","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}]'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/spot/batch_orders"
    query_param=""
    body_param='[{"text":"t-abc123","currency_pair":"BTC_USDT","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}]'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    [
      {
        "text": "t-abc123",
        "currency_pair": "BTC_USDT",
        "type": "limit",
        "account": "unified",
        "side": "buy",
        "amount": "0.001",
        "price": "65000",
        "time_in_force": "gtc",
        "iceberg": "0",
        "slippage": "0.05",
        "stop_profit": {
          "trigger_price": "67000",
          "order_price": "67000"
        },
        "stop_loss": {
          "trigger_price": "63000",
          "order_price": "63000"
        }
      }
    ]
    

> 返回示例

> 200 返回
    
    
    [
      {
        "order_id": "12332324",
        "amend_text": "t-123456",
        "text": "t-123456",
        "succeeded": true,
        "label": "",
        "message": "",
        "id": "12332324",
        "create_time": "1548000000",
        "update_time": "1548000100",
        "create_time_ms": 1548000000123,
        "update_time_ms": 1548000100123,
        "currency_pair": "ETC_BTC",
        "status": "cancelled",
        "type": "limit",
        "account": "spot",
        "side": "buy",
        "amount": "1",
        "price": "5.00032",
        "time_in_force": "gtc",
        "iceberg": "0",
        "left": "0.5",
        "filled_amount": "1.242",
        "filled_total": "2.50016",
        "avg_deal_price": "5.00032",
        "fee": "0.005",
        "fee_currency": "ETH",
        "point_fee": "0",
        "gt_fee": "0",
        "gt_discount": false,
        "rebated_fee": "0",
        "rebated_fee_currency": "BTC",
        "stp_act": "cn",
        "finish_as": "stp",
        "stp_id": 10240
      }
    ]
    

##  查询所有挂单🔒 需要认证

GET`/spot/open_orders`

GET `/spot/open_orders`

_查询所有挂单_

查询所有交易对的当前挂单列表。

注意分页参数控制的是每个交易对里的挂单数量，交易对个数没有分页控制，所有有挂单的交易对全部返回。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 每个交易对每页最多返回的数量  
account | 请求参数 | string | 否 | 指定查询账户。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OpenOrders]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» currency_pair | string | 交易对  
» total | integer | 该交易对当前页面的挂单总数  
» orders | array |   
»» _None_ | object | 现货单详情  
»»» id | string | 订单 ID  
»»» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
»»» amend_text | string | 用户修改订单时备注的信息  
»»» create_time | string | 订单创建时间  
»»» update_time | string | 订单最新修改时间  
»»» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
»»» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
»»» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
»»» currency_pair | string | 交易货币对  
»»» type | string | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
»»» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
»»» side | string | 买单或者卖单  
»»» amount | string | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
»»» price | string | 交易价,`type`=`limit`时必填  
»»» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
»»» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
»»» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
»»» left | string | 交易货币未成交数量  
»»» filled_amount | string | 交易货币已成交数量  
»»» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
»»» filled_total | string | 已成交总金额  
»»» avg_deal_price | string | 平均成交价  
»»» fee | string | 成交扣除的手续费  
»»» fee_currency | string | 手续费计价单位  
»»» point_fee | string | 手续费抵扣使用的点卡数量  
»»» gt_fee | string | 手续费抵扣使用的 GT 数量  
»»» gt_maker_fee | string | 手续费maker抵扣使用的 GT 数量  
»»» gt_taker_fee | string | 手续费taker抵扣使用的 GT 数量  
»»» gt_discount | boolean | 是否开启GT抵扣  
»»» rebated_fee | string | 返还的手续费  
»»» rebated_fee_currency | string | 返还手续费计价单位  
»»» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
»»» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
»»» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
»»» stop_profit | object | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»»»» trigger_price | string | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»»»» order_price | string | 止盈委托价  
»»» stop_loss | object | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»»»» trigger_price | string | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»»»» order_price | string | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/open_orders'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/open_orders"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency_pair": "ETH_BTC",
        "total": 1,
        "orders": [
          {
            "id": "12332324",
            "text": "t-123456",
            "create_time": "1548000000",
            "update_time": "1548000100",
            "currency_pair": "ETH_BTC",
            "status": "open",
            "type": "limit",
            "account": "spot",
            "side": "buy",
            "amount": "1",
            "price": "5.00032",
            "time_in_force": "gtc",
            "left": "0.5",
            "filled_total": "2.50016",
            "fee": "0.005",
            "fee_currency": "ETH",
            "point_fee": "0",
            "gt_fee": "0",
            "gt_discount": false,
            "rebated_fee": "0",
            "rebated_fee_currency": "BTC"
          }
        ]
      }
    ]
    

##  禁用币种下平仓单🔒 需要认证

POST`/spot/cross_liquidate_orders`

POST `/spot/cross_liquidate_orders`

_禁用币种下平仓单_

目前只支持全仓账户对禁用币种进行买入下单 最大买入数量 = (未还本息 - 币种余额 - 挂单该币种数量) / 0.998

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | LiquidateOrder | 是 |   
» text | body | string | 否 | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
» currency_pair | body | string | 是 | 交易货币对  
» amount | body | string | 是 | 交易数量  
» price | body | string | 是 | 交易价  
» action_mode | body | string | 否 | 处理模式:  
  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
  
####  详细描述

**» text** : 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)

**» action_mode** : 处理模式:  
  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 交易成功执行 | Order  
  
### 返回格式

状态码 **201**

_现货单详情_

名称 | 类型 | 描述  
---|---|---  
» id | string | 订单 ID  
» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
» amend_text | string | 用户修改订单时备注的信息  
» create_time | string | 订单创建时间  
» update_time | string | 订单最新修改时间  
» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
» currency_pair | string | 交易货币对  
» type | string | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
» side | string | 买单或者卖单  
» amount | string | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
» price | string | 交易价,`type`=`limit`时必填  
» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
» left | string | 交易货币未成交数量  
» filled_amount | string | 交易货币已成交数量  
» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
» filled_total | string | 已成交总金额  
» avg_deal_price | string | 平均成交价  
» fee | string | 成交扣除的手续费  
» fee_currency | string | 手续费计价单位  
» point_fee | string | 手续费抵扣使用的点卡数量  
» gt_fee | string | 手续费抵扣使用的 GT 数量  
» gt_maker_fee | string | 手续费maker抵扣使用的 GT 数量  
» gt_taker_fee | string | 手续费taker抵扣使用的 GT 数量  
» gt_discount | boolean | 是否开启GT抵扣  
» rebated_fee | string | 返还的手续费  
» rebated_fee_currency | string | 返还手续费计价单位  
» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
» stop_profit | object | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»» trigger_price | string | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»» order_price | string | 止盈委托价  
» stop_loss | object | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»» trigger_price | string | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»» order_price | string | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/cross_liquidate_orders'
    query_param = ''
    body='{"currency_pair":"GT_USDT","amount":"12","price":"10.15","text":"t-34535"}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/spot/cross_liquidate_orders"
    query_param=""
    body_param='{"currency_pair":"GT_USDT","amount":"12","price":"10.15","text":"t-34535"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "currency_pair": "GT_USDT",
      "amount": "12",
      "price": "10.15",
      "text": "t-34535"
    }
    

> 返回示例

> 201 返回
    
    
    {
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      }
    }
    

##  查询订单列表🔒 需要认证

GET`/spot/orders`

GET `/spot/orders`

_查询订单列表_

注意查询结果默认是现货，统一账户和逐仓杠杆账户的现货订单列表。

`status` 设置为 `open` ，即查询挂单列表时，只支持 `page` 和 `limit` 的分页控制。 `limit` 最大只允许设置到 100 。 不支持 `side` 和按时间范围查询的 `from`, `to` 参数。

`status` 设置为 `finished` ，即查询历史委托的时候， 除分页查询以外，还支持 `from` 和 `to` 按时间范围的查询。 此外还支持设置 `side` 参数筛选单边历史。

时间范围筛选的参数均是按订单**结束** 时间来处理。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 是 | 指定交易对查询。如果查询挂单的记录，该字段必选。如果查询已成交的记录，该字段可以不指定。  
status | 请求参数 | string | 是 | 基于状态查询订单列表  
  
`open` \- 挂单中  
`finished` \- 已结束  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量，如果 status 设置为 `open` ，`limit` 最大允许 100  
account | 请求参数 | string | 否 | 指定查询账户。  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
side | 请求参数 | string | 否 | 指定全部买单或全部卖单，不指定则两者都包括  
  
####  详细描述

**status** : 基于状态查询订单列表  
  
`open` \- 挂单中  
`finished` \- 已结束

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [Order]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [现货单详情]  
» _None_ | Order | 现货单详情  
»» id | string | 订单 ID  
»» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
»» amend_text | string | 用户修改订单时备注的信息  
»» create_time | string | 订单创建时间  
»» update_time | string | 订单最新修改时间  
»» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
»» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
»» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
»» currency_pair | string | 交易货币对  
»» type | string | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
»» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
»» side | string | 买单或者卖单  
»» amount | string | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
»» price | string | 交易价,`type`=`limit`时必填  
»» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
»» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
»» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
»» left | string | 交易货币未成交数量  
»» filled_amount | string | 交易货币已成交数量  
»» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
»» filled_total | string | 已成交总金额  
»» avg_deal_price | string | 平均成交价  
»» fee | string | 成交扣除的手续费  
»» fee_currency | string | 手续费计价单位  
»» point_fee | string | 手续费抵扣使用的点卡数量  
»» gt_fee | string | 手续费抵扣使用的 GT 数量  
»» gt_maker_fee | string | 手续费maker抵扣使用的 GT 数量  
»» gt_taker_fee | string | 手续费taker抵扣使用的 GT 数量  
»» gt_discount | boolean | 是否开启GT抵扣  
»» rebated_fee | string | 返还的手续费  
»» rebated_fee_currency | string | 返还手续费计价单位  
»» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
»» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
»» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
»» stop_profit | object | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»»» trigger_price | string | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»»» order_price | string | 止盈委托价  
»» stop_loss | object | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»»» trigger_price | string | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»»» order_price | string | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/orders'
    query_param = 'currency_pair=BTC_USDT&status=open'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/orders"
    query_param="currency_pair=BTC_USDT&status=open"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": "1852454420",
        "text": "t-abc123",
        "amend_text": "-",
        "create_time": "1710488334",
        "update_time": "1710488334",
        "create_time_ms": 1710488334073,
        "update_time_ms": 1710488334074,
        "status": "closed",
        "currency_pair": "BTC_USDT",
        "type": "limit",
        "account": "unified",
        "side": "buy",
        "amount": "0.001",
        "price": "65000",
        "time_in_force": "gtc",
        "iceberg": "0",
        "left": "0",
        "filled_amount": "0.001",
        "fill_price": "63.4693",
        "filled_total": "63.4693",
        "avg_deal_price": "63469.3",
        "fee": "0.00000022",
        "fee_currency": "BTC",
        "point_fee": "0",
        "gt_fee": "0",
        "gt_maker_fee": "0",
        "gt_taker_fee": "0",
        "gt_discount": false,
        "rebated_fee": "0",
        "rebated_fee_currency": "USDT",
        "finish_as": "filled",
        "stop_profit": {
          "trigger_price": "67000",
          "order_price": "67000"
        },
        "stop_loss": {
          "trigger_price": "63000",
          "order_price": "63000"
        }
      }
    ]
    

##  下单🔒 需要认证

POST`/spot/orders`

POST `/spot/orders`

_下单_

支持现货、保证金、杠杆、全仓杠杆下单。通过 `account` 字段来使用不同的账户，默认为 `spot` ，即使用现货账户下单，如果用户是 `unified` 账户，默认是用统一账户下单

使用杠杆账户交易，即 `account` 设置为 `margin` 的时候，可以设置 `auto_borrow` 为 `true`， 在账户余额不足的情况，由系统自动执行 `POST /margin/uni/loans` 借入不足部分。 杠杆下单成交之后的获取到的资产是否自动用于归还逐仓杠杆账户的借入单，取决于用户逐仓杠杆**账户** 的自动还款设置， 该账户自动还款设置可以通过 `/margin/auto_repay` 来查询和设置。

使用统一账户交易，即 `account` 设置为 `unified` 的时候，同样可以启用 `auto_borrow` 来实现自动借入不足部分，但是与逐仓杠杆账户不同的是，统一账户的委托是否自动还款取决于下单时的 `auto_repay` 设置，该设置只对当前委托生效，即只有该委托成交之后获取到的资产会用来还款全仓杠杆账户的借入单。 统一账户下单目前支持同时开启 `auto_borrow` 和 `auto_repay`。

自动还款会在订单结束时触发，即 `status` 为 `cancelled` 或者 `closed` 。

**委托状态**

挂单中的委托状态是 `open` ，在数量全部成交之前保持为 `open` 。如果被全部吃掉，则订单结束，状态变成 `closed` 。 假如全部成交之前，订单被撤销，不管是否有部分成交，状态都会变为 `cancelled`

**冰山委托**

`iceberg` 用来设置冰山委托显示的数量，不支持完全隐藏。注意隐藏部分成交时按照taker 的手续费率收取。

**限制用户自成交**

设置 `stp_act` 来决定使用限制用户自成交的策略

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | Order | 是 |   
» text | body | string | 否 | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
» currency_pair | body | string | 是 | 交易货币对  
» type | body | string | 否 | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
» account | body | string | 否 | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
» side | body | string | 是 | 买单或者卖单  
» amount | body | string | 是 | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
» price | body | string | 否 | 交易价,`type`=`limit`时必填  
» time_in_force | body | string | 否 | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
» iceberg | body | string | 否 | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
» auto_borrow | body | boolean | 否 | 杠杆(包括逐仓全仓)交易时，如果账户余额不足，是否由系统自动借入不足部分  
» auto_repay | body | boolean | 否 | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
» stp_act | body | string | 否 | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
» action_mode | body | string | 否 | 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
» slippage | body | string | 否 | 现货市价下单支持的最大滑点比率，以下单时的市场最新价格为基准计算（示例：0.03即3%）  
» stop_profit | body | object | 否 | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»» trigger_price | body | string | 否 | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»» order_price | body | string | 否 | 止盈委托价  
» stop_loss | body | object | 否 | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»» trigger_price | body | string | 否 | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»» order_price | body | string | 否 | 止损委托价  
  
####  详细描述

**» text** : 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单

**» type** : 订单类型  
  
\- limit : 限价单  
\- market : 市价单

**» amount** : 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`

**» time_in_force** : Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`

**» auto_repay** : 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启

**» stp_act** : Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消

**» action_mode** : 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）

**»» trigger_price** : 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`

**»» trigger_price** : 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» type | limit  
» type | market  
» side | buy  
» side | sell  
» time_in_force | gtc  
» time_in_force | ioc  
» time_in_force | poc  
» time_in_force | fok  
» stp_act | cn  
» stp_act | co  
» stp_act | cb  
» stp_act | -  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 交易成功执行。具体执行结果根据下单时的 Time in force 策略来决定 | Order  
  
### 返回格式

状态码 **201**

_现货单详情_

名称 | 类型 | 描述  
---|---|---  
» id | string | 订单 ID  
» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
» amend_text | string | 用户修改订单时备注的信息  
» create_time | string | 订单创建时间  
» update_time | string | 订单最新修改时间  
» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
» currency_pair | string | 交易货币对  
» type | string | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
» side | string | 买单或者卖单  
» amount | string | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
» price | string | 交易价,`type`=`limit`时必填  
» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
» auto_borrow | boolean | 杠杆(包括逐仓全仓)交易时，如果账户余额不足，是否由系统自动借入不足部分  
» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
» left | string | 交易货币未成交数量  
» filled_amount | string | 交易货币已成交数量  
» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
» filled_total | string | 已成交总金额  
» avg_deal_price | string | 平均成交价  
» fee | string | 成交扣除的手续费  
» fee_currency | string | 手续费计价单位  
» point_fee | string | 手续费抵扣使用的点卡数量  
» gt_fee | string | 手续费抵扣使用的 GT 数量  
» gt_maker_fee | string | 手续费maker抵扣使用的 GT 数量  
» gt_taker_fee | string | 手续费taker抵扣使用的 GT 数量  
» gt_discount | boolean | 是否开启GT抵扣  
» rebated_fee | string | 返还的手续费  
» rebated_fee_currency | string | 返还手续费计价单位  
» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
» action_mode | string | 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
» slippage | string | 现货市价下单支持的最大滑点比率，以下单时的市场最新价格为基准计算（示例：0.03即3%）  
» stop_profit | object | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»» trigger_price | string | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»» order_price | string | 止盈委托价  
» stop_loss | object | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»» trigger_price | string | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»» order_price | string | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/orders'
    query_param = ''
    body='{"text":"t-abc123","currency_pair":"BTC_USDT","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/spot/orders"
    query_param=""
    body_param='{"text":"t-abc123","currency_pair":"BTC_USDT","type":"limit","account":"unified","side":"buy","amount":"0.001","price":"65000","time_in_force":"gtc","iceberg":"0","slippage":"0.05","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "text": "t-abc123",
      "currency_pair": "BTC_USDT",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "slippage": "0.05",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      }
    }
    

> 返回示例

> ACK response body example
    
    
    {
      "id": "12332324",
      "text": "t-123456",
      "amend_text": "test2"
    }
    

> RESULT response body example
    
    
    {
      "id": "12332324",
      "text": "t-123456",
      "create_time": "1548000000",
      "update_time": "1548000100",
      "create_time_ms": 1548000000123,
      "update_time_ms": 1548000100123,
      "currency_pair": "ETH_BTC",
      "status": "cancelled",
      "type": "limit",
      "account": "spot",
      "side": "buy",
      "iceberg": "0",
      "amount": "1",
      "price": "5.00032",
      "time_in_force": "gtc",
      "auto_borrow": false,
      "left": "0.5",
      "filled_total": "2.50016",
      "avg_deal_price": "5.00032",
      "stp_act": "cn",
      "finish_as": "stp",
      "stp_id": 10240
    }
    

> FULL response body example
    
    
    {
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "slippage": "0.05",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      }
    }
    

##  批量取消一个交易对里状态为 `open` 的订单🔒 需要认证

DELETE`/spot/orders`

DELETE `/spot/orders`

_批量取消一个交易对里状态为`open` 的订单_

不指定 `account` 参数时，包括现货、统一账户、逐仓杠杆在内的所有挂单都会执行撤销操作。 不指定 `currency_pair`时，会撤销所有交易对的挂单 可以单独指定某一种账户，撤销指定账户下的所有挂单

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 交易对  
side | 请求参数 | string | 否 | 指定全部买单或全部卖单，不指定则两者都包括  
account | 请求参数 | string | 否 | 指定账户类型  
  
\- 经典账户：不指定则全部包含  
\- 统一账户：指定`unified`  
action_mode | 请求参数 | string | 否 | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
  
####  详细描述

**account** : 指定账户类型  
  
\- 经典账户：不指定则全部包含  
\- 统一账户：指定`unified`

**action_mode** : 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 批量撤销请求接收并处理，是否成功根据订单列表来决定 | [OrderCancel]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [现货单详情]  
» _None_ | OrderCancel | 现货单详情  
»» id | string | 订单 ID  
»» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
»» amend_text | string | 用户修改订单时备注的信息  
»» succeeded | boolean | 请求执行结果  
»» label | string | 错误标识，当订单成功时该字段为空串  
»» message | string | 错误详情，当订单成功时改字段为空串  
»» create_time | string | 订单创建时间  
»» update_time | string | 订单最新修改时间  
»» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
»» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
»» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
»» currency_pair | string | 交易货币对  
»» type | string | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
»» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
»» side | string | 买单或者卖单  
»» amount | string | 交易数量   
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。   
`type`为`market`时，根据买卖不同指代不同   
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
»» price | string | 交易价,`type`=`limit`时必填  
»» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
»» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
»» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
»» left | string | 交易货币未成交数量  
»» filled_amount | string | 交易货币已成交数量  
»» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
»» filled_total | string | 已成交总金额  
»» avg_deal_price | string | 平均成交价  
»» fee | string | 成交扣除的手续费  
»» fee_currency | string | 手续费计价单位  
»» point_fee | string | 手续费抵扣使用的点卡数量  
»» gt_fee | string | 手续费抵扣使用的 GT 数量  
»» gt_maker_fee | string | 手续费maker抵扣使用的 GT 数量  
»» gt_taker_fee | string | 手续费taker抵扣使用的 GT 数量  
»» gt_discount | boolean | 是否开启GT抵扣  
»» rebated_fee | string | 返还的手续费  
»» rebated_fee_currency | string | 返还手续费计价单位  
»» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
»» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
»» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- ioc: 未立即完全成交，因为 tif 设置为 ioc  
\- stp: 订单发生自成交限制而被撤销  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | ioc  
finish_as | stp  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/orders'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/spot/orders"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": "1852454420",
        "text": "t-abc123",
        "amend_text": "-",
        "succeeded": true,
        "create_time": "1710488334",
        "update_time": "1710488334",
        "create_time_ms": 1710488334073,
        "update_time_ms": 1710488334074,
        "status": "closed",
        "currency_pair": "BTC_USDT",
        "type": "limit",
        "account": "unified",
        "side": "buy",
        "amount": "0.001",
        "price": "65000",
        "time_in_force": "gtc",
        "iceberg": "0",
        "left": "0",
        "filled_amount": "0.001",
        "fill_price": "63.4693",
        "filled_total": "63.4693",
        "avg_deal_price": "63469.3",
        "fee": "0.00000022",
        "fee_currency": "BTC",
        "point_fee": "0",
        "gt_fee": "0",
        "gt_maker_fee": "0",
        "gt_taker_fee": "0",
        "gt_discount": false,
        "rebated_fee": "0",
        "rebated_fee_currency": "USDT",
        "finish_as": "filled"
      }
    ]
    

##  批量撤销指定 ID 的订单列表🔒 需要认证

POST`/spot/cancel_batch_orders`

POST `/spot/cancel_batch_orders`

_批量撤销指定 ID 的订单列表_

可以指定多个不同的交易对。一次请求最多只能撤销 20 条记录

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | array[CancelBatchOrder] | 是 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 撤销任务执行完成 | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CancelOrderResult | object | 订单撤销结果  
»» currency_pair | string | 订单的交易对  
»» id | string | 订单 ID  
»» text | string | 订单自定义信息  
»» succeeded | boolean | 是否撤销成功  
»» label | string | 撤销失败时的错误标识，成功时为空  
»» message | string | 撤销失败时的错误描述，成功时为空  
»» account | string | 默认为空 (废弃)  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/cancel_batch_orders'
    query_param = ''
    body='[{"currency_pair":"BTC_USDT","id":"123456"}]'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/spot/cancel_batch_orders"
    query_param=""
    body_param='[{"currency_pair":"BTC_USDT","id":"123456"}]'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    [
      {
        "currency_pair": "BTC_USDT",
        "id": "123456"
      }
    ]
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency_pair": "BTC_USDT",
        "id": "123456",
        "text": "123456",
        "succeeded": true,
        "label": null,
        "message": null
      }
    ]
    

##  查询单个订单详情🔒 需要认证

GET`/spot/orders/{order_id}`

GET `/spot/orders/{order_id}`

_查询单个订单详情_

默认查询现货、统一账户和逐仓杠杆账户的订单。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID（即 `text` 字段）。  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后只能使用订单 ID  
currency_pair | 请求参数 | string | 是 | 指定交易对查询。如果查询挂单的记录，该字段必选。如果查询已成交的记录，该字段可以不指定  
account | 请求参数 | string | 否 | 指定查询账户。  
  
####  详细描述

**order_id** : 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID（即 `text` 字段）。  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后只能使用订单 ID

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 详情查询成功 | Order  
  
### 返回格式

状态码 **200**

_现货单详情_

名称 | 类型 | 描述  
---|---|---  
» id | string | 订单 ID  
» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
» amend_text | string | 用户修改订单时备注的信息  
» create_time | string | 订单创建时间  
» update_time | string | 订单最新修改时间  
» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
» currency_pair | string | 交易货币对  
» type | string | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
» side | string | 买单或者卖单  
» amount | string | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
» price | string | 交易价,`type`=`limit`时必填  
» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
» left | string | 交易货币未成交数量  
» filled_amount | string | 交易货币已成交数量  
» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
» filled_total | string | 已成交总金额  
» avg_deal_price | string | 平均成交价  
» fee | string | 成交扣除的手续费  
» fee_currency | string | 手续费计价单位  
» point_fee | string | 手续费抵扣使用的点卡数量  
» gt_fee | string | 手续费抵扣使用的 GT 数量  
» gt_maker_fee | string | 手续费maker抵扣使用的 GT 数量  
» gt_taker_fee | string | 手续费taker抵扣使用的 GT 数量  
» gt_discount | boolean | 是否开启GT抵扣  
» rebated_fee | string | 返还的手续费  
» rebated_fee_currency | string | 返还手续费计价单位  
» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
» stop_profit | object | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»» trigger_price | string | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»» order_price | string | 止盈委托价  
» stop_loss | object | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»» trigger_price | string | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»» order_price | string | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/orders/12345'
    query_param = 'currency_pair=BTC_USDT'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/orders/12345"
    query_param="currency_pair=BTC_USDT"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    {
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      }
    }
    

##  修改单个订单🔒 需要认证

PATCH`/spot/orders/{order_id}`

PATCH `/spot/orders/{order_id}`

_修改单个订单_

默认修改现货、统一账户和逐仓杠杆账户的订单。

目前请求体和query都支持currency_pair和account传参，但请求体优先级更高

currency_pair必须在请求体或query中二选一填入

关于限速：修改订单和创建订单共享限速规则

关于匹配优先级：只修改数量变小不影响匹配优先级，修改价格或修改数量变大则优先级将调整到新价格最后面

注意事项:修改数量小于已成交数量会触发撤单操作

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID（即 `text` 字段）。  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后只能使用订单 ID  
currency_pair | 请求参数 | string | 否 | 交易对  
account | 请求参数 | string | 否 | 指定查询账户。  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | OrderPatch | 是 |   
» currency_pair | body | string | 否 | 交易对  
» account | body | string | 否 | 指定查询账户。  
» amount | body | string | 否 | 交易数量，`amount`和`price`必须指定其中一个  
» price | body | string | 否 | 交易价，`amount`和`price`必须指定其中一个  
» amend_text | body | string | 否 | 用户可以备注这次修改的信息。  
» action_mode | body | string | 否 | 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
» stop_profit | body | object | 否 | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»» trigger_price | body | string | 否 | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»» order_price | body | string | 否 | 止盈委托价  
» stop_loss | body | object | 否 | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»» trigger_price | body | string | 否 | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»» order_price | body | string | 否 | 止损委托价  
  
####  详细描述

**order_id** : 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID（即 `text` 字段）。  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后只能使用订单 ID

**» action_mode** : 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）

**»» trigger_price** : 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`

**»» trigger_price** : 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 修改成功 | Order  
  
### 返回格式

状态码 **200**

_现货单详情_

名称 | 类型 | 描述  
---|---|---  
» id | string | 订单 ID  
» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
» amend_text | string | 用户修改订单时备注的信息  
» create_time | string | 订单创建时间  
» update_time | string | 订单最新修改时间  
» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
» currency_pair | string | 交易货币对  
» type | string | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
» side | string | 买单或者卖单  
» amount | string | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
» price | string | 交易价,`type`=`limit`时必填  
» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
» left | string | 交易货币未成交数量  
» filled_amount | string | 交易货币已成交数量  
» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
» filled_total | string | 已成交总金额  
» avg_deal_price | string | 平均成交价  
» fee | string | 成交扣除的手续费  
» fee_currency | string | 手续费计价单位  
» point_fee | string | 手续费抵扣使用的点卡数量  
» gt_fee | string | 手续费抵扣使用的 GT 数量  
» gt_maker_fee | string | 手续费maker抵扣使用的 GT 数量  
» gt_taker_fee | string | 手续费taker抵扣使用的 GT 数量  
» gt_discount | boolean | 是否开启GT抵扣  
» rebated_fee | string | 返还的手续费  
» rebated_fee_currency | string | 返还手续费计价单位  
» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
» stop_profit | object | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»» trigger_price | string | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»» order_price | string | 止盈委托价  
» stop_loss | object | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»» trigger_price | string | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»» order_price | string | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/orders/12345'
    query_param = ''
    body='{"currency_pair":"BTC_USDT","account":"spot","amount":"1","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('PATCH', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('PATCH', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="PATCH"
    url="/spot/orders/12345"
    query_param=""
    body_param='{"currency_pair":"BTC_USDT","account":"spot","amount":"1","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "currency_pair": "BTC_USDT",
      "account": "spot",
      "amount": "1",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      }
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      }
    }
    

##  撤销单个订单🔒 需要认证

DELETE`/spot/orders/{order_id}`

DELETE `/spot/orders/{order_id}`

_撤销单个订单_

默认撤销现货、统一账户和逐仓杠杆账户的订单。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID（即 `text` 字段）。  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后只能使用订单 ID  
currency_pair | 请求参数 | string | 是 | 交易对  
account | 请求参数 | string | 否 | 指定查询账户。  
action_mode | 请求参数 | string | 否 | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
  
####  详细描述

**order_id** : 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID（即 `text` 字段）。  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后只能使用订单 ID

**action_mode** : 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单撤销成功 | Order  
  
### 返回格式

状态码 **200**

_现货单详情_

名称 | 类型 | 描述  
---|---|---  
» id | string | 订单 ID  
» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
» amend_text | string | 用户修改订单时备注的信息  
» create_time | string | 订单创建时间  
» update_time | string | 订单最新修改时间  
» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
» currency_pair | string | 交易货币对  
» type | string | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
» side | string | 买单或者卖单  
» amount | string | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
» price | string | 交易价,`type`=`limit`时必填  
» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
» left | string | 交易货币未成交数量  
» filled_amount | string | 交易货币已成交数量  
» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
» filled_total | string | 已成交总金额  
» avg_deal_price | string | 平均成交价  
» fee | string | 成交扣除的手续费  
» fee_currency | string | 手续费计价单位  
» point_fee | string | 手续费抵扣使用的点卡数量  
» gt_fee | string | 手续费抵扣使用的 GT 数量  
» gt_maker_fee | string | 手续费maker抵扣使用的 GT 数量  
» gt_taker_fee | string | 手续费taker抵扣使用的 GT 数量  
» gt_discount | boolean | 是否开启GT抵扣  
» rebated_fee | string | 返还的手续费  
» rebated_fee_currency | string | 返还手续费计价单位  
» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
» stop_profit | object | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»» trigger_price | string | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»» order_price | string | 止盈委托价  
» stop_loss | object | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»» trigger_price | string | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»» order_price | string | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/orders/12345'
    query_param = 'currency_pair=BTC_USDT'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/spot/orders/12345"
    query_param="currency_pair=BTC_USDT"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    {
      "id": "1852454420",
      "text": "t-abc123",
      "amend_text": "-",
      "create_time": "1710488334",
      "update_time": "1710488334",
      "create_time_ms": 1710488334073,
      "update_time_ms": 1710488334074,
      "status": "closed",
      "currency_pair": "BTC_USDT",
      "type": "limit",
      "account": "unified",
      "side": "buy",
      "amount": "0.001",
      "price": "65000",
      "time_in_force": "gtc",
      "iceberg": "0",
      "left": "0",
      "filled_amount": "0.001",
      "fill_price": "63.4693",
      "filled_total": "63.4693",
      "avg_deal_price": "63469.3",
      "fee": "0.00000022",
      "fee_currency": "BTC",
      "point_fee": "0",
      "gt_fee": "0",
      "gt_maker_fee": "0",
      "gt_taker_fee": "0",
      "gt_discount": false,
      "rebated_fee": "0",
      "rebated_fee_currency": "USDT",
      "finish_as": "filled",
      "stop_profit": {
        "trigger_price": "67000",
        "order_price": "67000"
      },
      "stop_loss": {
        "trigger_price": "63000",
        "order_price": "63000"
      }
    }
    

##  查询个人成交记录🔒 需要认证

GET`/spot/my_trades`

GET `/spot/my_trades`

_查询个人成交记录_

默认查询现货、统一账户和逐仓杠杆账户的成交记录 。

可以通过指定 `from` 或(和) `to` 来查询指定时间范围内的历史。

  * 如果不指定任何时间参数，只能获取最近 7 天的数据。
  * 如果只指定 `from` 或 `to` 的任一参数，也同样只返回指定时间开始（或结束）的 7 天范围的数据。
  * `from` 和 `to` 的范围不允许超过 30 天 。

时间范围筛选的参数均是按订单**结束** 时间来处理。

使用 limit&page分页功能检索数据时最大分页数量为100,000条，即 limit * (page - 1) <= 100000。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
currency_pair | 请求参数 | string | 否 | 指定交易对查询  
limit | 请求参数 | integer | 否 | 列表返回的最大数量。默认为100，最小1，最大1000。  
page | 请求参数 | integer(int32) | 否 | 列表页数  
order_id | 请求参数 | string | 否 | 指定查询订单 ID 的成交记录。指定该参数时 `currency_pair` 要求必填  
account | 请求参数 | string | 否 | account参数已过期。接口支持查询账户的全部成交记录。  
from | 请求参数 | integer(int64) | 否 | 查询记录的起始时间  
to | 请求参数 | integer(int64) | 否 | 查询记录的结束时间，不指定则默认为当前时间  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [Trade]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | string | 成交记录 ID  
» create_time | string | 成交时间  
» create_time_ms | string | 成交时间，毫秒精度  
» currency_pair | string | 交易货币对  
» side | string | 买单或者卖单  
» role | string | 交易角色，公共接口无此字段返回  
» amount | string | 交易数量  
» price | string | 交易价  
» order_id | string | 关联的订单 ID，公共接口无此字段返回  
» fee | string | 成交扣除的手续费，公共接口无此字段返回  
» fee_currency | string | 手续费计价单位，公共接口无此字段返回  
» point_fee | string | 手续费抵扣使用的点卡数量，公共接口无此字段返回  
» gt_fee | string | 手续费抵扣使用的 GT 数量，公共接口无此字段返回  
» amend_text | string | 用户修改订单时备注的信息  
» sequence_id | string | 单市场连续成交ID  
» text | string | 订单的自定义信息，公共接口无此字段返回  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
» deal | string | 本次成交总额  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
side | buy  
side | sell  
role | taker  
role | maker  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/my_trades'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/my_trades"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": "1232893232",
        "create_time": "1548000000",
        "create_time_ms": "1548000000123.456",
        "order_id": "4128442423",
        "side": "buy",
        "role": "maker",
        "amount": "0.15",
        "price": "0.03",
        "fee": "0.0005",
        "fee_currency": "ETH",
        "point_fee": "0",
        "gt_fee": "0",
        "sequence_id": "588018",
        "text": "t-test",
        "deal": "0.0045"
      }
    ]
    

##  获取服务器当前时间

GET`/spot/time`

GET `/spot/time`

_获取服务器当前时间_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | SystemTime  
  
### 返回格式

状态码 **200**

_SystemTime_

名称 | 类型 | 描述  
---|---|---  
» server_time | integer(int64) | 服务器当前时间(ms)  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/time'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/time \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "server_time": 1597026383085
    }
    

##  倒计时取消订单🔒 需要认证

POST`/spot/countdown_cancel_all`

POST `/spot/countdown_cancel_all`

_倒计时取消订单_

现货订单心跳检测，在到达用户设置的`timeout`时间时如果没有`取消既有倒计时`或`设置新的倒计时`将会自动取消相关的`现货挂单`。 该接口可重复调用，以便设置新的倒计时或取消倒计时。 用法示例： 以30s的间隔重复此接口，每次倒计时`timeout`设置为`30(秒)`。 如果在30秒内未再次调用此接口，则您指定`market`上的所有挂单都会被自动撤销，如果未指定`market`，则撤销所有市场挂单。 如果在30秒内以将`timeout`设置为0，则倒数计时器将终止，自动撤单功能取消。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CountdownCancelAllSpotTask | 是 |   
» timeout | body | integer(int32) | 是 | 倒计时时间，单位 秒  
至少5秒，为0时表示取消倒计时  
» currency_pair | body | string | 否 | 交易货币对  
  
####  详细描述

**» timeout** : 倒计时时间，单位 秒  
至少5秒，为0时表示取消倒计时

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 设置倒计时成功 | TriggerTime  
  
### 返回格式

状态码 **200**

_triggerTime_

名称 | 类型 | 描述  
---|---|---  
» triggerTime | integer(int64) | 倒计时结束时的时间戳，毫秒  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/countdown_cancel_all'
    query_param = ''
    body='{"timeout":30,"currency_pair":"BTC_USDT"}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/spot/countdown_cancel_all"
    query_param=""
    body_param='{"timeout":30,"currency_pair":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "timeout": 30,
      "currency_pair": "BTC_USDT"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "triggerTime": "1660039145000"
    }
    

##  批量修改订单🔒 需要认证

POST`/spot/amend_batch_orders`

POST `/spot/amend_batch_orders`

_批量修改订单_

默认修改现货、统一账户和逐仓杠杆账户的订单。 修改未完成的订单，一次最多可批量修改5个订单。请求参数应该按数组格式传递。 批量修改过程中有订单修改失败会继续执行下个订单的修改，执行后返回会携带相应订单的失败信息 批量修改订单的调用顺序与订单列表顺序一致 批量修改订单的返回内容顺序,与订单列表顺序一致

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | array[BatchAmendItem] | 是 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 修改订单执行完成 | [BatchOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [批量订单信息]  
» _None_ | BatchOrder | 批量订单信息  
»» order_id | string | 订单 ID  
»» amend_text | string | 用户修改订单时备注的信息  
»» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
»» succeeded | boolean | 请求执行结果  
»» label | string | 错误标识，当订单成功时该字段为空串  
»» message | string | 错误详情，当订单成功时改字段为空串  
»» id | string | 订单 ID  
»» create_time | string | 订单创建时间  
»» update_time | string | 订单最新修改时间  
»» create_time_ms | integer(int64) | 订单创建时间，毫秒精度  
»» update_time_ms | integer(int64) | 订单最近修改时间，毫秒精度  
»» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
»» currency_pair | string | 交易货币对  
»» type | string | 订单类型   
  
\- limit : 限价单  
\- market : 市价单  
»» account | string | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
»» side | string | 买单或者卖单  
»» amount | string | 交易数量  
»» price | string | 交易价  
»» time_in_force | string | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
»» iceberg | string | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
»» auto_repay | boolean | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
»» left | string | 交易货币未成交数量  
»» filled_amount | string | 交易货币已成交数量  
»» fill_price | string | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
»» filled_total | string | 已成交总金额  
»» avg_deal_price | string | 平均成交价  
»» fee | string | 成交扣除的手续费  
»» fee_currency | string | 手续费计价单位  
»» point_fee | string | 手续费抵扣使用的点卡数量  
»» gt_fee | string | 手续费抵扣使用的 GT 数量  
»» gt_discount | boolean | 是否开启GT抵扣  
»» rebated_fee | string | 返还的手续费  
»» rebated_fee_currency | string | 返还手续费计价单位  
»» stp_id | integer | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
»» stp_act | string | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回`-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
»» finish_as | string | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
»» stop_profit | object | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»»» trigger_price | string | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»»» order_price | string | 止盈委托价  
»» stop_loss | object | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»»» trigger_price | string | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»»» order_price | string | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
account | spot  
account | margin  
account | cross_margin  
account | unified  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/amend_batch_orders'
    query_param = ''
    body='[{"order_id":"121212","currency_pair":"BTC_USDT","account":"spot","amount":"1","amend_text":"test","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}]'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/spot/amend_batch_orders"
    query_param=""
    body_param='[{"order_id":"121212","currency_pair":"BTC_USDT","account":"spot","amount":"1","amend_text":"test","stop_profit":{"trigger_price":"67000","order_price":"67000"},"stop_loss":{"trigger_price":"63000","order_price":"63000"}}]'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    [
      {
        "order_id": "121212",
        "currency_pair": "BTC_USDT",
        "account": "spot",
        "amount": "1",
        "amend_text": "test",
        "stop_profit": {
          "trigger_price": "67000",
          "order_price": "67000"
        },
        "stop_loss": {
          "trigger_price": "63000",
          "order_price": "63000"
        }
      }
    ]
    

> 返回示例

> 200 返回
    
    
    [
      {
        "order_id": "12332324",
        "amend_text": "t-123456",
        "text": "t-123456",
        "succeeded": true,
        "label": "",
        "message": "",
        "id": "12332324",
        "create_time": "1548000000",
        "update_time": "1548000100",
        "create_time_ms": 1548000000123,
        "update_time_ms": 1548000100123,
        "currency_pair": "ETC_BTC",
        "status": "cancelled",
        "type": "limit",
        "account": "spot",
        "side": "buy",
        "amount": "1",
        "price": "5.00032",
        "time_in_force": "gtc",
        "iceberg": "0",
        "left": "0.5",
        "filled_amount": "1.242",
        "filled_total": "2.50016",
        "avg_deal_price": "5.00032",
        "fee": "0.005",
        "fee_currency": "ETH",
        "point_fee": "0",
        "gt_fee": "0",
        "gt_discount": false,
        "rebated_fee": "0",
        "rebated_fee_currency": "BTC",
        "stp_act": "cn",
        "finish_as": "stp",
        "stp_id": 10240
      }
    ]
    

##  查询现货保险基金历史数据

GET`/spot/insurance_history`

GET `/spot/insurance_history`

_查询现货保险基金历史数据_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
business | 请求参数 | string | 是 | 杠杆业务，margin - 逐仓；unified - 统一账户  
currency | 请求参数 | string | 是 | 币种  
page | 请求参数 | integer(int32) | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量, 默认值30  
from | 请求参数 | integer(int64) | 是 | 起始时间戳，秒级  
to | 请求参数 | integer(int64) | 是 | 终止时间戳，秒级  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [SpotInsuranceHistory]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» currency | string | 币种  
» balance | string | 余额  
» time | integer(int64) | 创建时间，时间戳，毫秒级  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/insurance_history'
    query_param = 'business=margin&currency=BTC&from=1547706332&to=1547706332'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/spot/insurance_history?business=margin&currency=BTC&from=1547706332&to=1547706332 \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "currency": "BTC",
        "balance": "1021.21",
        "time": 1727054547
      }
    ]
    

##  查询进行中自动订单列表🔒 需要认证

GET`/spot/price_orders`

GET `/spot/price_orders`

_查询进行中自动订单列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
status | 请求参数 | string | 是 | 基于状态查询订单列表  
market | 请求参数 | string | 否 | 交易市场  
account | 请求参数 | string | 否 | 交易账户类型，统一账户只能设置 unified  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
status | open  
status | finished  
account | normal  
account | margin  
account | unified  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [SpotPriceTriggeredOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [现货价格单详情]  
» _None_ | SpotPriceTriggeredOrder | 现货价格单详情  
»» trigger | SpotPriceTrigger |   
»»» price | string | 触发价格  
»»» rule | string | 价格条件类型  
\- `>=`: 表示市场价格大于等于 `price`时触发  
\- `<=`: 表示市场价格小于等于 `price`时触发  
»»» expiration | integer | 最长等待触发时间，超时则取消该订单，单位是秒 s  
»» put | SpotPricePutOrder |   
»»» type | string | 订单类型，默认为限价单  
  
\- limit : 限价单  
\- market : 市价单  
»»» side | string | 买卖方向  
  
\- buy: 买  
\- sell: 卖  
»»» price | string | 挂单价格  
»»» amount | string | 交易数量，指交易货币的交易数量，即需要交易的货币，如BTC_USDT中指BTC的数量  
»»» account | string | 交易账户类型，统一账户只能设置 unified  
  
\- normal: 现货交易  
\- margin: 杠杆交易  
\- unified: 统一账户  
»»» time_in_force | string | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
»»» auto_borrow | boolean | 是否自动借币  
»»» auto_repay | boolean | 是否自动还款  
»»» text | string | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
»» id | integer(int64) | 自动订单 ID  
»» user | integer | 用户 ID  
»» market | string | 市场  
»» ctime | integer(int64) | 创建时间  
»» ftime | integer(int64) | 结束时间  
»» fired_order_id | integer(int64) | 触发后委托单ID  
»» status | string | 状态  
  
\- open: 正在运行  
\- cancelled: 被取消  
\- finish: 成功结束  
\- failed: 失败  
\- expired - 过期  
»» reason | string | 订单结束的附加描述信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
rule | >=  
rule | <=  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/price_orders'
    query_param = 'status=open'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/price_orders"
    query_param="status=open"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "trigger": {
          "price": "100",
          "rule": ">=",
          "expiration": 3600
        },
        "put": {
          "type": "limit",
          "side": "buy",
          "price": "2.15",
          "amount": "2.00000000",
          "account": "normal",
          "time_in_force": "gtc",
          "text": "api"
        },
        "id": 1283293,
        "user": 1234,
        "market": "GT_USDT",
        "ctime": 1616397800,
        "ftime": 1616397801,
        "fired_order_id": 0,
        "status": "",
        "reason": ""
      }
    ]
    

##  创建价格触发订单🔒 需要认证

POST`/spot/price_orders`

POST `/spot/price_orders`

_创建价格触发订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | SpotPriceTriggeredOrder | 是 |   
» trigger | body | SpotPriceTrigger | 是 |   
»» price | body | string | 是 | 触发价格  
»» rule | body | string | 是 | 价格条件类型  
\- `>=`: 表示市场价格大于等于 `price`时触发  
\- `<=`: 表示市场价格小于等于 `price`时触发  
»» expiration | body | integer | 否 | 最长等待触发时间，超时则取消该订单，单位是秒 s  
» put | body | SpotPricePutOrder | 是 |   
»» type | body | string | 否 | 订单类型，默认为限价单  
  
\- limit : 限价单  
\- market : 市价单  
»» side | body | string | 是 | 买卖方向  
  
\- buy: 买  
\- sell: 卖  
»» price | body | string | 是 | 挂单价格  
»» amount | body | string | 是 | 交易数量，指交易货币的交易数量，即需要交易的货币，如BTC_USDT中指BTC的数量  
»» account | body | string | 是 | 交易账户类型，统一账户只能设置 unified  
  
\- normal: 现货交易  
\- margin: 杠杆交易  
\- unified: 统一账户  
»» time_in_force | body | string | 是 | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
»» auto_borrow | body | boolean | 否 | 是否自动借币  
»» auto_repay | body | boolean | 否 | 是否自动还款  
»» text | body | string | 否 | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
» market | body | string | 是 | 市场  
  
####  详细描述

**»» rule** : 价格条件类型  
\- `>=`: 表示市场价格大于等于 `price`时触发  
\- `<=`: 表示市场价格小于等于 `price`时触发

**»» type** : 订单类型，默认为限价单  
  
\- limit : 限价单  
\- market : 市价单

**»» side** : 买卖方向  
  
\- buy: 买  
\- sell: 卖

**»» account** : 交易账户类型，统一账户只能设置 unified  
  
\- normal: 现货交易  
\- margin: 杠杆交易  
\- unified: 统一账户

**»» time_in_force** : time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单

**»» text** : 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端

####  枚举值列表

枚举值列表参数 | 值  
---|---  
»» rule | >=  
»» rule | <=  
»» type | limit  
»» type | market  
»» side | buy  
»» side | sell  
»» account | normal  
»» account | margin  
»» account | unified  
»» time_in_force | gtc  
»» time_in_force | ioc  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 成功下单 | TriggerOrderResponse  
  
### 返回格式

状态码 **201**

_TriggerOrderResponse_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 自动订单 ID  
» id_string | string | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/price_orders'
    query_param = ''
    body='{"trigger":{"price":"100","rule":">=","expiration":3600},"put":{"type":"limit","side":"buy","price":"2.15","amount":"2.00000000","account":"normal","time_in_force":"gtc","text":"api"},"market":"GT_USDT"}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/spot/price_orders"
    query_param=""
    body_param='{"trigger":{"price":"100","rule":">=","expiration":3600},"put":{"type":"limit","side":"buy","price":"2.15","amount":"2.00000000","account":"normal","time_in_force":"gtc","text":"api"},"market":"GT_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "trigger": {
        "price": "100",
        "rule": ">=",
        "expiration": 3600
      },
      "put": {
        "type": "limit",
        "side": "buy",
        "price": "2.15",
        "amount": "2.00000000",
        "account": "normal",
        "time_in_force": "gtc",
        "text": "api"
      },
      "market": "GT_USDT"
    }
    

> 返回示例

> 201 返回
    
    
    {
      "id": 1432329
    }
    

##  批量取消自动订单🔒 需要认证

DELETE`/spot/price_orders`

DELETE `/spot/price_orders`

_批量取消自动订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
market | 请求参数 | string | 否 | 交易市场  
account | 请求参数 | string | 否 | 交易账户类型，统一账户只能设置 unified  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
account | normal  
account | margin  
account | unified  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 批量撤销请求接收并处理，是否成功根据订单列表来决定 | [SpotPriceTriggeredOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [现货价格单详情]  
» _None_ | SpotPriceTriggeredOrder | 现货价格单详情  
»» trigger | SpotPriceTrigger |   
»»» price | string | 触发价格  
»»» rule | string | 价格条件类型  
\- `>=`: 表示市场价格大于等于 `price`时触发  
\- `<=`: 表示市场价格小于等于 `price`时触发  
»»» expiration | integer | 最长等待触发时间，超时则取消该订单，单位是秒 s  
»» put | SpotPricePutOrder |   
»»» type | string | 订单类型，默认为限价单  
  
\- limit : 限价单  
\- market : 市价单  
»»» side | string | 买卖方向  
  
\- buy: 买  
\- sell: 卖  
»»» price | string | 挂单价格  
»»» amount | string | 交易数量，指交易货币的交易数量，即需要交易的货币，如BTC_USDT中指BTC的数量  
»»» account | string | 交易账户类型，统一账户只能设置 unified  
  
\- normal: 现货交易  
\- margin: 杠杆交易  
\- unified: 统一账户  
»»» time_in_force | string | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
»»» auto_borrow | boolean | 是否自动借币  
»»» auto_repay | boolean | 是否自动还款  
»»» text | string | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
»» id | integer(int64) | 自动订单 ID  
»» user | integer | 用户 ID  
»» market | string | 市场  
»» ctime | integer(int64) | 创建时间  
»» ftime | integer(int64) | 结束时间  
»» fired_order_id | integer(int64) | 触发后委托单ID  
»» status | string | 状态  
  
\- open: 正在运行  
\- cancelled: 被取消  
\- finish: 成功结束  
\- failed: 失败  
\- expired - 过期  
»» reason | string | 订单结束的附加描述信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
rule | >=  
rule | <=  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/price_orders'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/spot/price_orders"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "trigger": {
          "price": "100",
          "rule": ">=",
          "expiration": 3600
        },
        "put": {
          "type": "limit",
          "side": "buy",
          "price": "2.15",
          "amount": "2.00000000",
          "account": "normal",
          "time_in_force": "gtc",
          "text": "api"
        },
        "id": 1283293,
        "user": 1234,
        "market": "GT_USDT",
        "ctime": 1616397800,
        "ftime": 1616397801,
        "fired_order_id": 0,
        "status": "",
        "reason": ""
      }
    ]
    

##  查询单个自动订单详情🔒 需要认证

GET`/spot/price_orders/{order_id}`

GET `/spot/price_orders/{order_id}`

_查询单个自动订单详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 成功创建订单时返回的 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 自动订单详情 | SpotPriceTriggeredOrder  
  
### 返回格式

状态码 **200**

_现货价格单详情_

名称 | 类型 | 描述  
---|---|---  
» trigger | SpotPriceTrigger |   
»» price | string | 触发价格  
»» rule | string | 价格条件类型  
\- `>=`: 表示市场价格大于等于 `price`时触发  
\- `<=`: 表示市场价格小于等于 `price`时触发  
»» expiration | integer | 最长等待触发时间，超时则取消该订单，单位是秒 s  
» put | SpotPricePutOrder |   
»» type | string | 订单类型，默认为限价单  
  
\- limit : 限价单  
\- market : 市价单  
»» side | string | 买卖方向  
  
\- buy: 买  
\- sell: 卖  
»» price | string | 挂单价格  
»» amount | string | 交易数量，指交易货币的交易数量，即需要交易的货币，如BTC_USDT中指BTC的数量  
»» account | string | 交易账户类型，统一账户只能设置 unified  
  
\- normal: 现货交易  
\- margin: 杠杆交易  
\- unified: 统一账户  
»» time_in_force | string | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
»» auto_borrow | boolean | 是否自动借币  
»» auto_repay | boolean | 是否自动还款  
»» text | string | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
» id | integer(int64) | 自动订单 ID  
» user | integer | 用户 ID  
» market | string | 市场  
» ctime | integer(int64) | 创建时间  
» ftime | integer(int64) | 结束时间  
» fired_order_id | integer(int64) | 触发后委托单ID  
» status | string | 状态  
  
\- open: 正在运行  
\- cancelled: 被取消  
\- finish: 成功结束  
\- failed: 失败  
\- expired - 过期  
» reason | string | 订单结束的附加描述信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
rule | >=  
rule | <=  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/price_orders/string'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/spot/price_orders/string"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    {
      "trigger": {
        "price": "100",
        "rule": ">=",
        "expiration": 3600
      },
      "put": {
        "type": "limit",
        "side": "buy",
        "price": "2.15",
        "amount": "2.00000000",
        "account": "normal",
        "time_in_force": "gtc",
        "text": "api"
      },
      "id": 1283293,
      "user": 1234,
      "market": "GT_USDT",
      "ctime": 1616397800,
      "ftime": 1616397801,
      "fired_order_id": 0,
      "status": "",
      "reason": ""
    }
    

##  撤销单个自动订单🔒 需要认证

DELETE`/spot/price_orders/{order_id}`

DELETE `/spot/price_orders/{order_id}`

_撤销单个自动订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 成功创建订单时返回的 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 自动订单详情 | SpotPriceTriggeredOrder  
  
### 返回格式

状态码 **200**

_现货价格单详情_

名称 | 类型 | 描述  
---|---|---  
» trigger | SpotPriceTrigger |   
»» price | string | 触发价格  
»» rule | string | 价格条件类型  
\- `>=`: 表示市场价格大于等于 `price`时触发  
\- `<=`: 表示市场价格小于等于 `price`时触发  
»» expiration | integer | 最长等待触发时间，超时则取消该订单，单位是秒 s  
» put | SpotPricePutOrder |   
»» type | string | 订单类型，默认为限价单  
  
\- limit : 限价单  
\- market : 市价单  
»» side | string | 买卖方向  
  
\- buy: 买  
\- sell: 卖  
»» price | string | 挂单价格  
»» amount | string | 交易数量，指交易货币的交易数量，即需要交易的货币，如BTC_USDT中指BTC的数量  
»» account | string | 交易账户类型，统一账户只能设置 unified  
  
\- normal: 现货交易  
\- margin: 杠杆交易  
\- unified: 统一账户  
»» time_in_force | string | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
»» auto_borrow | boolean | 是否自动借币  
»» auto_repay | boolean | 是否自动还款  
»» text | string | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
» id | integer(int64) | 自动订单 ID  
» user | integer | 用户 ID  
» market | string | 市场  
» ctime | integer(int64) | 创建时间  
» ftime | integer(int64) | 结束时间  
» fired_order_id | integer(int64) | 触发后委托单ID  
» status | string | 状态  
  
\- open: 正在运行  
\- cancelled: 被取消  
\- finish: 成功结束  
\- failed: 失败  
\- expired - 过期  
» reason | string | 订单结束的附加描述信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
rule | >=  
rule | <=  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
  
WARNING

该请求需要 API key 和 secret 认证

示例代码
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/spot/price_orders/string'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/spot/price_orders/string"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 返回示例

> 200 返回
    
    
    {
      "trigger": {
        "price": "100",
        "rule": ">=",
        "expiration": 3600
      },
      "put": {
        "type": "limit",
        "side": "buy",
        "price": "2.15",
        "amount": "2.00000000",
        "account": "normal",
        "time_in_force": "gtc",
        "text": "api"
      },
      "id": 1283293,
      "user": 1234,
      "market": "GT_USDT",
      "ctime": 1616397800,
      "ftime": 1616397801,
      "fired_order_id": 0,
      "status": "",
      "reason": ""
    }
    

#  模型

##  BatchAmendItem

_需要修改的订单信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | true | none | 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID（即 text 字段）。  
currency_pair | string | true | none | 交易对  
account | string | false | none | 默认现货、统一账户和逐仓杠杆账户。  
amount | string | false | none | 交易数量，`amount`和`price`只能指定一个  
price | string | false | none | 交易价，`amount`和`price`只能指定一个  
amend_text | string | false | none | 用户可以备注这次修改的信息。  
action_mode | string | false | none | 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
stop_profit | object | false | none | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
» trigger_price | string | false | none | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
» order_price | string | false | none | 止盈委托价  
stop_loss | object | false | none | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
» trigger_price | string | false | none | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
» order_price | string | false | none | 止损委托价  
      
    
    {
      "order_id": "string",
      "currency_pair": "string",
      "account": "string",
      "amount": "string",
      "price": "string",
      "amend_text": "string",
      "action_mode": "string",
      "stop_profit": {
        "trigger_price": "string",
        "order_price": "string"
      },
      "stop_loss": {
        "trigger_price": "string",
        "order_price": "string"
      }
    }
    
    

##  OrderBook

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 深度更新ID。深度每发生一次变化，ID 就会更新一次。仅在 `with_id` 设置为 `true` 该值有效  
current | integer(int64) | false | none | 接口数据返回 ms 时间戳  
update | integer(int64) | false | none | 深度变化 ms 时间戳  
asks | array | true | none | 卖方深度列表  
» _None_ | array | false | none | 价格，数量的二元组  
bids | array | true | none | 买方深度列表  
» _None_ | array | false | none | 价格，数量的二元组  
      
    
    {
      "id": 0,
      "current": 0,
      "update": 0,
      "asks": [
        [
          "string",
          "string"
        ]
      ],
      "bids": [
        [
          "string",
          "string"
        ]
      ]
    }
    
    

##  Currency

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种符号  
name | string | false | none | 币种名称  
delisted | boolean | false | none | 是否下架  
withdraw_disabled | boolean | false | none | 是否暂停提现（废弃）  
withdraw_delayed | boolean | false | none | 提现是否存在延迟（废弃）  
deposit_disabled | boolean | false | none | 是否暂停充值（废弃）  
trade_disabled | boolean | false | none | 是否暂停交易  
fixed_rate | string | false | none | 固定交易手续费率。仅限固定交易费率的币种，普通币种该字段无效  
chain | string | false | none | 币对应的主链  
chains | array | false | none | 币对应的所有链  
» SpotCurrencyChain | object | false | none | none  
»» name | string | false | none | 链名  
»» addr | string | false | none | token地址  
»» withdraw_disabled | boolean | false | none | 是否暂停提现  
»» withdraw_delayed | boolean | false | none | 提现是否存在延迟  
»» deposit_disabled | boolean | false | none | 是否暂停充值  
» total_supply | string | false | none | 币种总供应量  
» market_cap | string | false | none | 币种市值  
» category | array | false | none | 币种分类  
  
\- stocks: 股票  
\- metals: 金属  
\- indices: 指数  
\- forex: 外汇  
\- commodities: 大宗商品  
      
    
    {
      "currency": "string",
      "name": "string",
      "delisted": true,
      "withdraw_disabled": true,
      "withdraw_delayed": true,
      "deposit_disabled": true,
      "trade_disabled": true,
      "fixed_rate": "string",
      "chain": "string",
      "chains": [
        {
          "name": "string",
          "addr": "string",
          "withdraw_disabled": true,
          "withdraw_delayed": true,
          "deposit_disabled": true
        }
      ],
      "total_supply": "string",
      "market_cap": "string",
      "category": [
        "string"
      ]
    }
    
    

##  OpenOrders

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | false | none | 交易对  
total | integer | false | none | 该交易对当前页面的挂单总数  
orders | array | false | none | none  
» _None_ | object | false | none | 现货单详情  
»» id | string | false | 只读 | 订单 ID  
»» text | string | false | none | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
»» amend_text | string | false | 只读 | 用户修改订单时备注的信息  
»» create_time | string | false | 只读 | 订单创建时间  
»» update_time | string | false | 只读 | 订单最新修改时间  
»» create_time_ms | integer(int64) | false | 只读 | 订单创建时间，毫秒精度  
»» update_time_ms | integer(int64) | false | 只读 | 订单最近修改时间，毫秒精度  
»» status | string | false | 只读 | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
»» currency_pair | string | true | none | 交易货币对  
»» type | string | false | none | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
»» account | string | false | none | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
»» side | string | true | none | 买单或者卖单  
»» amount | string | true | none | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
»» price | string | false | none | 交易价,`type`=`limit`时必填  
»» time_in_force | string | false | none | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
»» iceberg | string | false | none | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
»» auto_borrow | boolean | false | 只写 | 杠杆(包括逐仓全仓)交易时，如果账户余额不足，是否由系统自动借入不足部分  
»» auto_repay | boolean | false | none | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
»» left | string | false | 只读 | 交易货币未成交数量  
»» filled_amount | string | false | 只读 | 交易货币已成交数量  
»» fill_price | string | false | 只读 | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
»» filled_total | string | false | 只读 | 已成交总金额  
»» avg_deal_price | string | false | 只读 | 平均成交价  
»» fee | string | false | 只读 | 成交扣除的手续费  
»» fee_currency | string | false | 只读 | 手续费计价单位  
»» point_fee | string | false | 只读 | 手续费抵扣使用的点卡数量  
»» gt_fee | string | false | 只读 | 手续费抵扣使用的 GT 数量  
»» gt_maker_fee | string | false | 只读 | 手续费maker抵扣使用的 GT 数量  
»» gt_taker_fee | string | false | 只读 | 手续费taker抵扣使用的 GT 数量  
»» gt_discount | boolean | false | 只读 | 是否开启GT抵扣  
»» rebated_fee | string | false | 只读 | 返还的手续费  
»» rebated_fee_currency | string | false | 只读 | 返还手续费计价单位  
»» stp_id | integer | false | 只读 | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
»» stp_act | string | false | none | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
»» finish_as | string | false | 只读 | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
»» action_mode | string | false | 只写 | 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
»» slippage | string | false | 只写 | 现货市价下单支持的最大滑点比率，以下单时的市场最新价格为基准计算（示例：0.03即3%）  
»» stop_profit | object | false | none | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
»»» trigger_price | string | false | none | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
»»» order_price | string | false | none | 止盈委托价  
»» stop_loss | object | false | none | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
»»» trigger_price | string | false | none | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
»»» order_price | string | false | none | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
      
    
    {
      "currency_pair": "string",
      "total": 0,
      "orders": [
        {
          "id": "string",
          "text": "string",
          "amend_text": "string",
          "create_time": "string",
          "update_time": "string",
          "create_time_ms": 0,
          "update_time_ms": 0,
          "status": "open",
          "currency_pair": "string",
          "type": "limit",
          "account": "spot",
          "side": "buy",
          "amount": "string",
          "price": "string",
          "time_in_force": "gtc",
          "iceberg": "string",
          "auto_borrow": true,
          "auto_repay": true,
          "left": "string",
          "filled_amount": "string",
          "fill_price": "string",
          "filled_total": "string",
          "avg_deal_price": "string",
          "fee": "string",
          "fee_currency": "string",
          "point_fee": "string",
          "gt_fee": "string",
          "gt_maker_fee": "string",
          "gt_taker_fee": "string",
          "gt_discount": true,
          "rebated_fee": "string",
          "rebated_fee_currency": "string",
          "stp_id": 0,
          "stp_act": "cn",
          "finish_as": "open",
          "action_mode": "string",
          "slippage": "string",
          "stop_profit": {},
          "stop_loss": {}
        }
      ]
    }
    
    

##  SpotFee

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user_id | integer(int64) | false | none | 用户 ID  
taker_fee | string | false | none | taker 费率  
maker_fee | string | false | none | maker 费率  
rpi_maker_fee | string | false | none | RPI MM maker 费率  
gt_discount | boolean | false | none | 是否开启 GT 抵扣折扣  
gt_taker_fee | string | false | none | GT 抵扣 taker 费率，未开启 GT 抵扣则为 0  
gt_maker_fee | string | false | none | GT 抵扣 maker 费率，未开启 GT 抵扣则为 0  
loan_fee | string | false | none | 杠杆理财的费率  
point_type | string | false | none | 点卡类型，0 - 初版点卡，1 - 202009 启用的新点卡  
currency_pair | string | false | none | 交易对  
debit_fee | integer | false | none | 费率抵扣类型 , 1 - GT抵扣 , 2 - 点卡抵扣 , 3 - VIP费率  
rpi_mm | integer | false | none | RPI MM等级  
      
    
    {
      "user_id": 0,
      "taker_fee": "string",
      "maker_fee": "string",
      "rpi_maker_fee": "string",
      "gt_discount": true,
      "gt_taker_fee": "string",
      "gt_maker_fee": "string",
      "loan_fee": "string",
      "point_type": "string",
      "currency_pair": "string",
      "debit_fee": 0,
      "rpi_mm": 0
    }
    
    

##  CancelBatchOrder

_需要撤销的订单信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | true | none | 订单的交易对  
id | string | true | none | 订单 ID 或者用户自定义 ID 。  
如果使用自定义 ID，只能在订单创建后的 30 分钟内有效  
account | string | false | none | 撤销的订单如果是统一账户apikey，该字段必须指定且设置为 `unified`  
action_mode | string | false | none | 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
      
    
    {
      "currency_pair": "string",
      "id": "string",
      "account": "string",
      "action_mode": "string"
    }
    
    

##  Ticker

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | false | none | 交易对  
last | string | false | none | 最新成交价  
lowest_ask | string | false | none | 最新卖方最低价  
lowest_size | string | false | none | 最新卖方最低价数量；批量查询时不存在；单个查询时存在,如果没有数据时为空  
highest_bid | string | false | none | 最新买方最高价  
highest_size | string | false | none | 最新买方最高价数量；批量查询时不存在；单个查询时存在,如果没有数据时为空  
change_percentage | string | false | none | 最近24h涨跌百分比，跌用负数标识，如 -7.45  
change_utc0 | string | false | none | utc0时区，最近24h涨跌百分比，跌用负数标识，如 -7.45  
change_utc8 | string | false | none | utc8时区，最近24h涨跌百分比，跌用负数标识，如 -7.45  
base_volume | string | false | none | 最近24h交易货币成交量  
quote_volume | string | false | none | 最近24h计价货币成交量  
high_24h | string | false | none | 24小时最高价  
low_24h | string | false | none | 24小时最低价  
etf_net_value | string | false | none | ETF 净值  
etf_pre_net_value | string|null | false | none | ETF 前一再平衡点净值  
etf_pre_timestamp | integer(int64)|null | false | none | ETF 前一再平衡时间  
etf_leverage | string|null | false | none | ETF 当前杠杆率  
      
    
    {
      "currency_pair": "string",
      "last": "string",
      "lowest_ask": "string",
      "lowest_size": "string",
      "highest_bid": "string",
      "highest_size": "string",
      "change_percentage": "string",
      "change_utc0": "string",
      "change_utc8": "string",
      "base_volume": "string",
      "quote_volume": "string",
      "high_24h": "string",
      "low_24h": "string",
      "etf_net_value": "string",
      "etf_pre_net_value": "string",
      "etf_pre_timestamp": 0,
      "etf_leverage": "string"
    }
    
    

##  SpotAccountBook

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | none | 账户变更记录 ID  
time | integer(int64) | false | none | 账户变更时间戳，毫秒单位  
currency | string | false | none | 变更币种  
change | string | false | none | 变更金额，正数表示转入，负数表示转出  
balance | string | false | none | 变更后账户余额  
type | string | false | none | 账户变更类型 , 已弃用（参考 code 账户变更编码）  
code | string | false | none | 账户变更编码 , 详见资产流水编码  
text | string | false | none | 附加信息  
      
    
    {
      "id": "string",
      "time": 0,
      "currency": "string",
      "change": "string",
      "balance": "string",
      "type": "string",
      "code": "string",
      "text": "string"
    }
    
    

##  CountdownCancelAllSpotTask

_CountdownCancelAllSpotTask_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timeout | integer(int32) | true | none | 倒计时时间，单位 秒  
至少5秒，为0时表示取消倒计时  
currency_pair | string | false | none | 交易货币对  
      
    
    {
      "timeout": 0,
      "currency_pair": "string"
    }
    
    

##  OrderPatch

_现货单详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency_pair | string | false | none | 交易对  
account | string | false | none | 指定查询账户。  
amount | string | false | none | 交易数量，`amount`和`price`必须指定其中一个  
price | string | false | none | 交易价，`amount`和`price`必须指定其中一个  
amend_text | string | false | none | 用户可以备注这次修改的信息。  
action_mode | string | false | none | 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
stop_profit | object | false | none | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
» trigger_price | string | false | none | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
» order_price | string | false | none | 止盈委托价  
stop_loss | object | false | none | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
» trigger_price | string | false | none | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
» order_price | string | false | none | 止损委托价  
      
    
    {
      "currency_pair": "string",
      "account": "string",
      "amount": "string",
      "price": "string",
      "amend_text": "string",
      "action_mode": "string",
      "stop_profit": {
        "trigger_price": "string",
        "order_price": "string"
      },
      "stop_loss": {
        "trigger_price": "string",
        "order_price": "string"
      }
    }
    
    

##  TriggerOrderResponse

_TriggerOrderResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 自动订单 ID  
id_string | string | false | 只读 | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
      
    
    {
      "id": 0,
      "id_string": "string"
    }
    
    

##  Trade

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | none | 成交记录 ID  
create_time | string | false | none | 成交时间  
create_time_ms | string | false | none | 成交时间，毫秒精度  
currency_pair | string | false | none | 交易货币对  
side | string | false | none | 买单或者卖单  
role | string | false | none | 交易角色，公共接口无此字段返回  
amount | string | false | none | 交易数量  
price | string | false | none | 交易价  
order_id | string | false | none | 关联的订单 ID，公共接口无此字段返回  
fee | string | false | none | 成交扣除的手续费，公共接口无此字段返回  
fee_currency | string | false | none | 手续费计价单位，公共接口无此字段返回  
point_fee | string | false | none | 手续费抵扣使用的点卡数量，公共接口无此字段返回  
gt_fee | string | false | none | 手续费抵扣使用的 GT 数量，公共接口无此字段返回  
amend_text | string | false | none | 用户修改订单时备注的信息  
sequence_id | string | false | none | 单市场连续成交ID  
text | string | false | none | 订单的自定义信息，公共接口无此字段返回  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
deal | string | false | none | 本次成交总额  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
side | buy  
side | sell  
role | taker  
role | maker  
      
    
    {
      "id": "string",
      "create_time": "string",
      "create_time_ms": "string",
      "currency_pair": "string",
      "side": "buy",
      "role": "taker",
      "amount": "string",
      "price": "string",
      "order_id": "string",
      "fee": "string",
      "fee_currency": "string",
      "point_fee": "string",
      "gt_fee": "string",
      "amend_text": "string",
      "sequence_id": "string",
      "text": "string",
      "deal": "string"
    }
    
    

##  SpotInsuranceHistory

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种  
balance | string | false | none | 余额  
time | integer(int64) | false | none | 创建时间，时间戳，毫秒级  
      
    
    {
      "currency": "string",
      "balance": "string",
      "time": 0
    }
    
    

##  TriggerTime

_triggerTime_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
triggerTime | integer(int64) | false | none | 倒计时结束时的时间戳，毫秒  
      
    
    {
      "triggerTime": "1660039145000"
    }
    
    

##  OrderCancel

_现货单详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | 只读 | 订单 ID  
text | string | false | none | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
amend_text | string | false | 只读 | 用户修改订单时备注的信息  
succeeded | boolean | false | none | 请求执行结果  
label | string | false | none | 错误标识，当订单成功时该字段为空串  
message | string | false | none | 错误详情，当订单成功时改字段为空串  
create_time | string | false | 只读 | 订单创建时间  
update_time | string | false | 只读 | 订单最新修改时间  
create_time_ms | integer(int64) | false | 只读 | 订单创建时间，毫秒精度  
update_time_ms | integer(int64) | false | 只读 | 订单最近修改时间，毫秒精度  
status | string | false | 只读 | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
currency_pair | string | true | none | 交易货币对  
type | string | false | none | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
account | string | false | none | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
side | string | true | none | 买单或者卖单  
amount | string | true | none | 交易数量   
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。   
`type`为`market`时，根据买卖不同指代不同   
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
price | string | false | none | 交易价,`type`=`limit`时必填  
time_in_force | string | false | none | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
iceberg | string | false | none | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
auto_borrow | boolean | false | 只写 | 杠杆(包括逐仓全仓)交易时，如果账户余额不足，是否由系统自动借入不足部分  
auto_repay | boolean | false | none | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
left | string | false | 只读 | 交易货币未成交数量  
filled_amount | string | false | 只读 | 交易货币已成交数量  
fill_price | string | false | 只读 | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
filled_total | string | false | 只读 | 已成交总金额  
avg_deal_price | string | false | 只读 | 平均成交价  
fee | string | false | 只读 | 成交扣除的手续费  
fee_currency | string | false | 只读 | 手续费计价单位  
point_fee | string | false | 只读 | 手续费抵扣使用的点卡数量  
gt_fee | string | false | 只读 | 手续费抵扣使用的 GT 数量  
gt_maker_fee | string | false | 只读 | 手续费maker抵扣使用的 GT 数量  
gt_taker_fee | string | false | 只读 | 手续费taker抵扣使用的 GT 数量  
gt_discount | boolean | false | 只读 | 是否开启GT抵扣  
rebated_fee | string | false | 只读 | 返还的手续费  
rebated_fee_currency | string | false | 只读 | 返还手续费计价单位  
stp_id | integer | false | 只读 | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | false | none | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
finish_as | string | false | 只读 | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- ioc: 未立即完全成交，因为 tif 设置为 ioc  
\- stp: 订单发生自成交限制而被撤销  
action_mode | string | false | 只写 | 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | ioc  
finish_as | stp  
      
    
    {
      "id": "string",
      "text": "string",
      "amend_text": "string",
      "succeeded": true,
      "label": "string",
      "message": "string",
      "create_time": "string",
      "update_time": "string",
      "create_time_ms": 0,
      "update_time_ms": 0,
      "status": "open",
      "currency_pair": "string",
      "type": "limit",
      "account": "spot",
      "side": "buy",
      "amount": "string",
      "price": "string",
      "time_in_force": "gtc",
      "iceberg": "string",
      "auto_borrow": true,
      "auto_repay": true,
      "left": "string",
      "filled_amount": "string",
      "fill_price": "string",
      "filled_total": "string",
      "avg_deal_price": "string",
      "fee": "string",
      "fee_currency": "string",
      "point_fee": "string",
      "gt_fee": "string",
      "gt_maker_fee": "string",
      "gt_taker_fee": "string",
      "gt_discount": true,
      "rebated_fee": "string",
      "rebated_fee_currency": "string",
      "stp_id": 0,
      "stp_act": "cn",
      "finish_as": "open",
      "action_mode": "string"
    }
    
    

##  CurrencyPair

_现货交易对_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | none | 交易对  
base | string | false | none | 交易货币  
base_name | string | false | none | 交易货币名称  
quote | string | false | none | 计价货币  
quote_name | string | false | none | 计价货币名称  
fee | string | false | none | 交易费率(已废弃)  
min_base_amount | string | false | none | 交易货币最低交易数量，null 表示无限制  
min_quote_amount | string | false | none | 计价货币最低交易数量，null 表示无限制  
max_base_amount | string | false | none | 交易货币最大交易数量，null 表示无限制  
max_quote_amount | string | false | none | 计价货币最大交易数量，null 表示无限制  
amount_precision | integer | false | none | 数量精度  
precision | integer | false | none | 价格精度  
trade_status | string | false | none | 交易状态  
  
\- untradable: 不可交易  
\- buyable: 可买  
\- sellable: 可卖  
\- tradable: 买卖均可交易  
sell_start | integer(int64) | false | none | 允许卖出时间，秒级 Unix 时间戳  
buy_start | integer(int64) | false | none | 允许买入时间，秒级 Unix 时间戳  
delisting_time | integer(int64) | false | none | 预计下架时间，秒级 Unix 时间戳  
type | string | false | none | 交易对类型，normal:常规, premarket:盘前  
trade_url | string | false | none | 交易链接  
st_tag | boolean | false | none | 币对是否在ST风险评估中，false - 否，true - 是  
up_rate | string | false | none | 报价最大涨幅百分比  
down_rate | string | false | none | 报价最大跌幅百分比  
slippage | string | false | none | 现货市价下单支持的最大滑点比率，以下单时的市场最新价格为基准计算（示例：0.03即3%）  
market_order_max_stock | string | false | none | 市价单最大下单数量  
market_order_max_money | string | false | none | 市价单最大下单金额  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
trade_status | untradable  
trade_status | buyable  
trade_status | sellable  
trade_status | tradable  
      
    
    {
      "id": "string",
      "base": "string",
      "base_name": "string",
      "quote": "string",
      "quote_name": "string",
      "fee": "string",
      "min_base_amount": "string",
      "min_quote_amount": "string",
      "max_base_amount": "string",
      "max_quote_amount": "string",
      "amount_precision": 0,
      "precision": 0,
      "trade_status": "untradable",
      "sell_start": 0,
      "buy_start": 0,
      "delisting_time": 0,
      "type": "string",
      "trade_url": "string",
      "st_tag": true,
      "up_rate": "string",
      "down_rate": "string",
      "slippage": "string",
      "market_order_max_stock": "string",
      "market_order_max_money": "string"
    }
    
    

##  SpotAccount

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
currency | string | false | none | 币种信息  
available | string | false | none | 可用金额  
locked | string | false | none | 冻结金额  
update_id | integer(int64) | false | none | 版本号  
      
    
    {
      "currency": "string",
      "available": "string",
      "locked": "string",
      "update_id": 0
    }
    
    

##  SpotPriceTriggeredOrder

_现货价格单详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
trigger | SpotPriceTrigger | true | none | none  
put | SpotPricePutOrder | true | none | none  
id | integer(int64) | false | 只读 | 自动订单 ID  
user | integer | false | 只读 | 用户 ID  
market | string | true | none | 市场  
ctime | integer(int64) | false | 只读 | 创建时间  
ftime | integer(int64) | false | 只读 | 结束时间  
fired_order_id | integer(int64) | false | 只读 | 触发后委托单ID  
status | string | false | 只读 | 状态  
  
\- open: 正在运行  
\- cancelled: 被取消  
\- finish: 成功结束  
\- failed: 失败  
\- expired - 过期  
reason | string | false | 只读 | 订单结束的附加描述信息  
      
    
    {
      "trigger": {
        "price": "string",
        "rule": ">=",
        "expiration": 0
      },
      "put": {
        "type": "limit",
        "side": "buy",
        "price": "string",
        "amount": "string",
        "account": "normal",
        "time_in_force": "gtc",
        "auto_borrow": false,
        "auto_repay": false,
        "text": "string"
      },
      "id": 0,
      "user": 0,
      "market": "string",
      "ctime": 0,
      "ftime": 0,
      "fired_order_id": 0,
      "status": "string",
      "reason": "string"
    }
    
    

##  Order

_现货单详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | string | false | 只读 | 订单 ID  
text | string | false | none | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
101 代表 `android` 下单  
102 代表 `IOS` 下单  
103 代表 `IPAD` 下单  
104 代表 `webapp` 下单  
3 代表 `web` 下单  
2 代表 `apiv2` 下单  
apiv4 代表 `apiv4` 下单  
pm_liquidate、comb_margin_liquidate、scm_liquidate 这三种场景代表全仓强平订单  
liquidate 代表逐仓强平订单  
amend_text | string | false | 只读 | 用户修改订单时备注的信息  
create_time | string | false | 只读 | 订单创建时间  
update_time | string | false | 只读 | 订单最新修改时间  
create_time_ms | integer(int64) | false | 只读 | 订单创建时间，毫秒精度  
update_time_ms | integer(int64) | false | 只读 | 订单最近修改时间，毫秒精度  
status | string | false | 只读 | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
currency_pair | string | true | none | 交易货币对  
type | string | false | none | 订单类型  
  
\- limit : 限价单  
\- market : 市价单  
account | string | false | none | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
side | string | true | none | 买单或者卖单  
amount | string | true | none | 交易数量  
`type`为`limit`时，指交易货币，即需要交易的货币，如`BTC_USDT`中指`BTC`。  
`type`为`market`时，根据买卖不同指代不同  
\- `side` : `buy` 指代计价货币，`BTC_USDT`中指`USDT`  
\- `side` : `sell` 指代交易货币，`BTC_USDT`中指`BTC`  
price | string | false | none | 交易价,`type`=`limit`时必填  
time_in_force | string | false | none | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
  
`type`=`market`时仅支持`ioc`和`fok`  
iceberg | string | false | none | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
auto_borrow | boolean | false | 只写 | 杠杆(包括逐仓全仓)交易时，如果账户余额不足，是否由系统自动借入不足部分  
auto_repay | boolean | false | none | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
left | string | false | 只读 | 交易货币未成交数量  
filled_amount | string | false | 只读 | 交易货币已成交数量  
fill_price | string | false | 只读 | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
filled_total | string | false | 只读 | 已成交总金额  
avg_deal_price | string | false | 只读 | 平均成交价  
fee | string | false | 只读 | 成交扣除的手续费  
fee_currency | string | false | 只读 | 手续费计价单位  
point_fee | string | false | 只读 | 手续费抵扣使用的点卡数量  
gt_fee | string | false | 只读 | 手续费抵扣使用的 GT 数量  
gt_maker_fee | string | false | 只读 | 手续费maker抵扣使用的 GT 数量  
gt_taker_fee | string | false | 只读 | 手续费taker抵扣使用的 GT 数量  
gt_discount | boolean | false | 只读 | 是否开启GT抵扣  
rebated_fee | string | false | 只读 | 返还的手续费  
rebated_fee_currency | string | false | 只读 | 返还手续费计价单位  
stp_id | integer | false | 只读 | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | false | none | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
finish_as | string | false | 只读 | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
action_mode | string | false | 只写 | 处理模式:  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
slippage | string | false | 只写 | 现货市价下单支持的最大滑点比率，以下单时的市场最新价格为基准计算（示例：0.03即3%）  
stop_profit | object | false | none | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
» trigger_price | string | false | none | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
» order_price | string | false | none | 止盈委托价  
stop_loss | object | false | none | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
» trigger_price | string | false | none | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
» order_price | string | false | none | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
      
    
    {
      "id": "string",
      "text": "string",
      "amend_text": "string",
      "create_time": "string",
      "update_time": "string",
      "create_time_ms": 0,
      "update_time_ms": 0,
      "status": "open",
      "currency_pair": "string",
      "type": "limit",
      "account": "spot",
      "side": "buy",
      "amount": "string",
      "price": "string",
      "time_in_force": "gtc",
      "iceberg": "string",
      "auto_borrow": true,
      "auto_repay": true,
      "left": "string",
      "filled_amount": "string",
      "fill_price": "string",
      "filled_total": "string",
      "avg_deal_price": "string",
      "fee": "string",
      "fee_currency": "string",
      "point_fee": "string",
      "gt_fee": "string",
      "gt_maker_fee": "string",
      "gt_taker_fee": "string",
      "gt_discount": true,
      "rebated_fee": "string",
      "rebated_fee_currency": "string",
      "stp_id": 0,
      "stp_act": "cn",
      "finish_as": "open",
      "action_mode": "string",
      "slippage": "string",
      "stop_profit": {
        "trigger_price": "string",
        "order_price": "string"
      },
      "stop_loss": {
        "trigger_price": "string",
        "order_price": "string"
      }
    }
    
    

##  SystemTime

_SystemTime_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
server_time | integer(int64) | false | none | 服务器当前时间(ms)  
      
    
    {
      "server_time": 0
    }
    
    

##  BatchOrder

_批量订单信息_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | false | none | 订单 ID  
amend_text | string | false | none | 用户修改订单时备注的信息  
text | string | false | none | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
succeeded | boolean | false | none | 请求执行结果  
label | string | false | none | 错误标识，当订单成功时该字段为空串  
message | string | false | none | 错误详情，当订单成功时改字段为空串  
id | string | false | 只读 | 订单 ID  
create_time | string | false | 只读 | 订单创建时间  
update_time | string | false | 只读 | 订单最新修改时间  
create_time_ms | integer(int64) | false | 只读 | 订单创建时间，毫秒精度  
update_time_ms | integer(int64) | false | 只读 | 订单最近修改时间，毫秒精度  
status | string | false | 只读 | 订单状态。  
  
\- `open`: 等待处理  
\- `closed`: 已结束的订单  
\- `cancelled`: 订单撤销  
currency_pair | string | false | none | 交易货币对  
type | string | false | none | 订单类型   
  
\- limit : 限价单  
\- market : 市价单  
account | string | false | none | 账户类型，spot - 现货账户，margin - 杠杆账户，unified - 统一账户  
side | string | false | none | 买单或者卖单  
amount | string | false | none | 交易数量  
price | string | false | none | 交易价  
time_in_force | string | false | none | Time in force 策略。  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill，全部成交或者全部取消  
iceberg | string | false | none | 冰山下单显示的数量，不指定或传 0 都默认为普通下单。目前不支持全部冰山。  
auto_borrow | boolean | false | 只写 | 杠杆(包括逐仓全仓)交易时，如果账户余额不足，是否由系统自动借入不足部分  
auto_repay | boolean | false | none | 全仓杠杆下单是否开启自动还款，默认关闭。需要注意的是:  
  
1\. 此字段仅针对全仓杠杆有效。逐仓杠杆不支持订单级别的自动还款设置，只能通过 `POST /margin/auto_repay` 修改用户级别的设置  
2\. `auto_borrow` 与 `auto_repay` 支持同时开启  
left | string | false | 只读 | 交易货币未成交数量  
filled_amount | string | false | 只读 | 交易货币已成交数量  
fill_price | string | false | 只读 | 已成交的计价币种总额，该字段废弃，建议使用相同意义的 `filled_total`  
filled_total | string | false | 只读 | 已成交总金额  
avg_deal_price | string | false | 只读 | 平均成交价  
fee | string | false | 只读 | 成交扣除的手续费  
fee_currency | string | false | 只读 | 手续费计价单位  
point_fee | string | false | 只读 | 手续费抵扣使用的点卡数量  
gt_fee | string | false | 只读 | 手续费抵扣使用的 GT 数量  
gt_discount | boolean | false | 只读 | 是否开启GT抵扣  
rebated_fee | string | false | 只读 | 返还的手续费  
rebated_fee_currency | string | false | 只读 | 返还手续费计价单位  
stp_id | integer | false | 只读 | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | false | none | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回`-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
finish_as | string | false | 只读 | 订单结束方式，包括：  
  
\- open: 等待处理  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidate_cancelled: 爆仓撤销  
\- small: 订单数量太小  
\- depth_not_enough: 深度不足导致撤单  
\- trader_not_enough: 对手方不足导致撤单  
\- ioc: 未立即成交，因为 tif 设置为 ioc  
\- poc: 未满足挂单策略，因为 tif 设置为 poc/rvt/rat/rpi表示只想成为maker, 经检查会成为taker被拒绝  
\- fok: 未立即完全成交，因为 tif 设置为 fok  
\- stp: 订单发生自成交限制而被撤销  
\- price_protect_cancelled: 价格保护导致撤单  
\- unknown: 未知  
slippage | string | false | 只写 | 现货市价下单支持的最大滑点比率，以下单时的市场最新价格为基准计算（示例：0.03即3%）  
stop_profit | object | false | none | 限价单止盈，取消止盈时传{}, 传null表示不进行止盈修改  
» trigger_price | string | false | none | 止盈触发价  
`side == "buy"` 时， `trigger_price` 需大于 `price`  
`side == "sell"` 时， `trigger_price` 需小于 `price`  
» order_price | string | false | none | 止盈委托价  
stop_loss | object | false | none | 限价单止损，取消止损时传{}, 传null表示不进行止损修改  
» trigger_price | string | false | none | 止损触发价  
`side == "buy"` 时， `trigger_price` 需小于 `price`  
`side == "sell"` 时， `trigger_price` 需大于 `price`  
» order_price | string | false | none | 止损委托价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
status | open  
status | closed  
status | cancelled  
type | limit  
type | market  
account | spot  
account | margin  
account | cross_margin  
account | unified  
side | buy  
side | sell  
time_in_force | gtc  
time_in_force | ioc  
time_in_force | poc  
time_in_force | fok  
stp_act | cn  
stp_act | co  
stp_act | cb  
stp_act | -  
finish_as | open  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidate_cancelled  
finish_as | depth_not_enough  
finish_as | trader_not_enough  
finish_as | small  
finish_as | ioc  
finish_as | poc  
finish_as | fok  
finish_as | stp  
finish_as | price_protect_cancelled  
finish_as | unknown  
      
    
    {
      "order_id": "string",
      "amend_text": "string",
      "text": "string",
      "succeeded": true,
      "label": "string",
      "message": "string",
      "id": "string",
      "create_time": "string",
      "update_time": "string",
      "create_time_ms": 0,
      "update_time_ms": 0,
      "status": "open",
      "currency_pair": "string",
      "type": "limit",
      "account": "spot",
      "side": "buy",
      "amount": "string",
      "price": "string",
      "time_in_force": "gtc",
      "iceberg": "string",
      "auto_borrow": true,
      "auto_repay": true,
      "left": "string",
      "filled_amount": "string",
      "fill_price": "string",
      "filled_total": "string",
      "avg_deal_price": "string",
      "fee": "string",
      "fee_currency": "string",
      "point_fee": "string",
      "gt_fee": "string",
      "gt_discount": true,
      "rebated_fee": "string",
      "rebated_fee_currency": "string",
      "stp_id": 0,
      "stp_act": "cn",
      "finish_as": "open",
      "slippage": "string",
      "stop_profit": {
        "trigger_price": "string",
        "order_price": "string"
      },
      "stop_loss": {
        "trigger_price": "string",
        "order_price": "string"
      }
    }
    
    

##  LiquidateOrder

_现货平仓单详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
text | string | false | none | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
currency_pair | string | true | none | 交易货币对  
amount | string | true | none | 交易数量  
price | string | true | none | 交易价  
action_mode | string | false | none | 处理模式:  
  
下单时根据action_mode返回不同的字段, 该字段只在请求时有效，响应结果中不包含该字段  
`ACK`: 异步模式，只返回订单关键字段  
`RESULT`: 无清算信息  
`FULL`: 完整模式（默认）  
      
    
    {
      "text": "string",
      "currency_pair": "string",
      "amount": "string",
      "price": "string",
      "action_mode": "string"
    }
    
    

##  SpotPricePutOrder

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
type | string | false | none | 订单类型，默认为限价单  
  
\- limit : 限价单  
\- market : 市价单  
side | string | true | none | 买卖方向  
  
\- buy: 买  
\- sell: 卖  
price | string | true | none | 挂单价格  
amount | string | true | none | 交易数量，指交易货币的交易数量，即需要交易的货币，如BTC_USDT中指BTC的数量  
account | string | true | none | 交易账户类型，统一账户只能设置 unified  
  
\- normal: 现货交易  
\- margin: 杠杆交易  
\- unified: 统一账户  
time_in_force | string | true | none | time_in_force  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
auto_borrow | boolean | false | none | 是否自动借币  
auto_repay | boolean | false | none | 是否自动还款  
text | string | false | none | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | limit  
type | market  
side | buy  
side | sell  
account | normal  
account | margin  
account | unified  
time_in_force | gtc  
time_in_force | ioc  
      
    
    {
      "type": "limit",
      "side": "buy",
      "price": "string",
      "amount": "string",
      "account": "normal",
      "time_in_force": "gtc",
      "auto_borrow": false,
      "auto_repay": false,
      "text": "string"
    }
    
    

##  SpotPriceTrigger

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
price | string | true | none | 触发价格  
rule | string | true | none | 价格条件类型  
\- `>=`: 表示市场价格大于等于 `price`时触发  
\- `<=`: 表示市场价格小于等于 `price`时触发  
expiration | integer | false | none | 最长等待触发时间，超时则取消该订单，单位是秒 s  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
rule | >=  
rule | <=  
      
    
    {
      "price": "string",
      "rule": ">=",
      "expiration": 0
    }