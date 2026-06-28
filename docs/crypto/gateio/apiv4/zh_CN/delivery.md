---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/delivery
api_type: Trading
updated_at: 2026-05-27 20:16:59.321523
---

# Delivery

交割合约

##  查询所有的合约信息

GET`/delivery/{settle}/contracts`

GET `/delivery/{settle}/contracts`

_查询所有的合约信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DeliveryContract]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [合约详情]  
» _None_ | DeliveryContract | 合约详情  
»» name | string | 合约标识  
»» underlying | string | 标的物  
»» cycle | string | 周期类型, 季度合约, 周合约等  
»» type | string | 合约类型, inverse - 反向合约, direct - 正向合约  
»» quanto_multiplier | string | 合约乘数，表示一张合约的面值为多少个标的物币种  
»» leverage_min | string | 最小杠杆  
»» leverage_max | string | 最大杠杆  
»» maintenance_rate | string | 风险限额的第一档维持保证金率要求  
»» mark_type | string | 已废弃  
»» mark_price | string | 当前标记价格  
»» index_price | string | 当前指数价格  
»» last_price | string | 上一次成交价格  
»» maker_fee_rate | string | 挂单成交的手续费率，负数代表返还后续费  
»» taker_fee_rate | string | 吃单成交的手续费率  
»» order_price_round | string | 委托价格最小单位  
»» mark_price_round | string | 标记价格的最小单位  
»» basis_rate | string | 当前合理基差率  
»» basis_value | string | 当前合理基差值  
»» basis_impact_value | string | 计算合理基差率时加权深度影响额  
»» settle_price | string | 预计结算价格  
»» settle_price_interval | integer | 结算价格更新间隔  
»» settle_price_duration | integer | 加权平均计算结算价格时长, 单位秒  
»» expire_time | integer(int64) | 合约到期时间戳  
»» risk_limit_base | string | 基础风险限额  
»» risk_limit_step | string | 风险限额调整步长  
»» risk_limit_max | string | 合约允许的最大风险限额  
»» order_size_min | integer(int64) | 最小下单数量  
»» order_size_max | integer(int64) | 最大下单数量  
»» order_price_deviate | string | 下单价与当前标记价格允许的正负偏移量， 即下单价 `order_price` 需满足如下条件:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
»» ref_discount_rate | string | 被推荐人享受交易费率折扣  
»» ref_rebate_rate | string | 推荐人享受交易费率返佣比例  
»» orderbook_id | integer(int64) | orderbook更新ID  
»» trade_id | integer(int64) | 当前成交ID  
»» trade_size | integer(int64) | 历史累计成交  
»» position_size | integer(int64) | 当前做多用户持有仓位总和  
»» config_change_time | number(double) | 配置最后更新时间  
»» in_delisting | boolean | 合约下线中  
»» orders_limit | integer | 最多挂单数量  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
cycle | WEEKLY  
cycle | BI-WEEKLY  
cycle | QUARTERLY  
cycle | BI-QUARTERLY  
type | inverse  
type | direct  
mark_type | internal  
mark_type | index  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/contracts'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/contracts \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "name": "BTC_USDT_20200814",
        "underlying": "BTC_USDT",
        "cycle": "WEEKLY",
        "type": "direct",
        "quanto_multiplier": "0.0001",
        "mark_type": "index",
        "last_price": "9017",
        "mark_price": "9019",
        "index_price": "9005.3",
        "basis_rate": "0.185095",
        "basis_value": "13.7",
        "basis_impact_value": "100000",
        "settle_price": "0",
        "settle_price_interval": 60,
        "settle_price_duration": 1800,
        "settle_fee_rate": "0.0015",
        "expire_time": 1593763200,
        "order_price_round": "0.1",
        "mark_price_round": "0.1",
        "leverage_min": "1",
        "leverage_max": "100",
        "maintenance_rate": "1000000",
        "risk_limit_base": "140.726652109199",
        "risk_limit_step": "1000000",
        "risk_limit_max": "8000000",
        "maker_fee_rate": "-0.00025",
        "taker_fee_rate": "0.00075",
        "ref_discount_rate": "0",
        "ref_rebate_rate": "0.2",
        "order_price_deviate": "0.5",
        "order_size_min": 1,
        "order_size_max": 1000000,
        "orders_limit": 50,
        "orderbook_id": 63,
        "trade_id": 26,
        "trade_size": 435,
        "position_size": 130,
        "config_change_time": 1593158867,
        "in_delisting": false
      }
    ]
    

##  查询单个合约信息

GET`/delivery/{settle}/contracts/{contract}`

GET `/delivery/{settle}/contracts/{contract}`

_查询单个合约信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | URL | string | 是 | 合约标识  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 合约信息 | DeliveryContract  
  
### 返回格式

状态码 **200**

_合约详情_

名称 | 类型 | 描述  
---|---|---  
» name | string | 合约标识  
» underlying | string | 标的物  
» cycle | string | 周期类型, 季度合约, 周合约等  
» type | string | 合约类型, inverse - 反向合约, direct - 正向合约  
» quanto_multiplier | string | 合约乘数，表示一张合约的面值为多少个标的物币种  
» leverage_min | string | 最小杠杆  
» leverage_max | string | 最大杠杆  
» maintenance_rate | string | 风险限额的第一档维持保证金率要求  
» mark_type | string | 已废弃  
» mark_price | string | 当前标记价格  
» index_price | string | 当前指数价格  
» last_price | string | 上一次成交价格  
» maker_fee_rate | string | 挂单成交的手续费率，负数代表返还后续费  
» taker_fee_rate | string | 吃单成交的手续费率  
» order_price_round | string | 委托价格最小单位  
» mark_price_round | string | 标记价格的最小单位  
» basis_rate | string | 当前合理基差率  
» basis_value | string | 当前合理基差值  
» basis_impact_value | string | 计算合理基差率时加权深度影响额  
» settle_price | string | 预计结算价格  
» settle_price_interval | integer | 结算价格更新间隔  
» settle_price_duration | integer | 加权平均计算结算价格时长, 单位秒  
» expire_time | integer(int64) | 合约到期时间戳  
» risk_limit_base | string | 基础风险限额  
» risk_limit_step | string | 风险限额调整步长  
» risk_limit_max | string | 合约允许的最大风险限额  
» order_size_min | integer(int64) | 最小下单数量  
» order_size_max | integer(int64) | 最大下单数量  
» order_price_deviate | string | 下单价与当前标记价格允许的正负偏移量， 即下单价 `order_price` 需满足如下条件:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
» ref_discount_rate | string | 被推荐人享受交易费率折扣  
» ref_rebate_rate | string | 推荐人享受交易费率返佣比例  
» orderbook_id | integer(int64) | orderbook更新ID  
» trade_id | integer(int64) | 当前成交ID  
» trade_size | integer(int64) | 历史累计成交  
» position_size | integer(int64) | 当前做多用户持有仓位总和  
» config_change_time | number(double) | 配置最后更新时间  
» in_delisting | boolean | 合约下线中  
» orders_limit | integer | 最多挂单数量  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
cycle | WEEKLY  
cycle | BI-WEEKLY  
cycle | QUARTERLY  
cycle | BI-QUARTERLY  
type | inverse  
type | direct  
mark_type | internal  
mark_type | index  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/contracts/BTC_USDT_20200814'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/contracts/BTC_USDT_20200814 \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "name": "BTC_USDT_20200814",
      "underlying": "BTC_USDT",
      "cycle": "WEEKLY",
      "type": "direct",
      "quanto_multiplier": "0.0001",
      "mark_type": "index",
      "last_price": "9017",
      "mark_price": "9019",
      "index_price": "9005.3",
      "basis_rate": "0.185095",
      "basis_value": "13.7",
      "basis_impact_value": "100000",
      "settle_price": "0",
      "settle_price_interval": 60,
      "settle_price_duration": 1800,
      "settle_fee_rate": "0.0015",
      "expire_time": 1593763200,
      "order_price_round": "0.1",
      "mark_price_round": "0.1",
      "leverage_min": "1",
      "leverage_max": "100",
      "maintenance_rate": "1000000",
      "risk_limit_base": "140.726652109199",
      "risk_limit_step": "1000000",
      "risk_limit_max": "8000000",
      "maker_fee_rate": "-0.00025",
      "taker_fee_rate": "0.00075",
      "ref_discount_rate": "0",
      "ref_rebate_rate": "0.2",
      "order_price_deviate": "0.5",
      "order_size_min": 1,
      "order_size_max": 1000000,
      "orders_limit": 50,
      "orderbook_id": 63,
      "trade_id": 26,
      "trade_size": 435,
      "position_size": 130,
      "config_change_time": 1593158867,
      "in_delisting": false
    }
    

##  查询合约市场深度信息

GET`/delivery/{settle}/order_book`

GET `/delivery/{settle}/order_book`

_查询合约市场深度信息_

买单会按照价格从高到低排序，卖单反之

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | 请求参数 | string | 是 | 合约标识  
interval | 请求参数 | string | 否 | 合并深度指定的价格精度，0 为不合并，不指定则默认为 0  
limit | 请求参数 | integer | 否 | 深度档位数量  
with_id | 请求参数 | boolean | 否 | 是否返回深度更新 ID。深度每发生一次变化，该 ID 自增 1  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
interval | 0  
interval | 0.1  
interval | 0.01  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 深度查询成功 | DeliveryOrderBook  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 深度更新 ID，深度每发生一次变化，该 ID 加 1，只有设置 `with_id=true` 时才返回  
» current | number(double) | 接口数据返回时间戳  
» update | number(double) | 深度变化时间戳  
» asks | array | 卖方深度列表  
»» DeliveryOrderBookItem | object |   
»»» p | string | 价格 (计价货币)  
»»» s | integer(int64) | 数量  
»» bids | array | 买方深度列表  
»»» DeliveryOrderBookItem | object |   
»»»» p | string | 价格 (计价货币)  
»»»» s | integer(int64) | 数量  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/order_book'
    query_param = 'contract=BTC_USDT_20200814'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/order_book?contract=BTC_USDT_20200814 \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "id": 123456,
      "current": 1623898993.123,
      "update": 1623898993.121,
      "asks": [
        {
          "p": "1.52",
          "s": 100
        },
        {
          "p": "1.53",
          "s": 40
        }
      ],
      "bids": [
        {
          "p": "1.17",
          "s": 150
        },
        {
          "p": "1.16",
          "s": 203
        }
      ]
    }
    

##  合约市场成交记录

GET`/delivery/{settle}/trades`

GET `/delivery/{settle}/trades`

_合约市场成交记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | 请求参数 | string | 是 | 合约标识  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
last_id | 请求参数 | string | 否 | 以上个列表的最后一条记录的 ID 作为下个列表的起点。  
该字段不再继续支持，新的请求请使用 `from` 和 `to` 字段来限定时间范围  
from | 请求参数 | integer(int64) | 否 | 指定起始时间，时间格式为秒(s)精度的 Unix 时间戳。 不指定则按照 to 和 limit 来限定返回的数量。  
如果 from 和 to 指定的时间范围内的数量超过 limit，只返回 limit 数量  
to | 请求参数 | integer(int64) | 否 | 指定结束时间，不指定则默认当前时间，时间格式为秒(s)精度的 Unix 时间戳  
  
####  详细描述

**last_id** : 以上个列表的最后一条记录的 ID 作为下个列表的起点。  
该字段不再继续支持，新的请求请使用 `from` 和 `to` 字段来限定时间范围

**from** : 指定起始时间，时间格式为秒(s)精度的 Unix 时间戳。 不指定则按照 to 和 limit 来限定返回的数量。  
如果 from 和 to 指定的时间范围内的数量超过 limit，只返回 limit 数量

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DeliveryTrade]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | integer(int64) | 成交记录 ID  
» create_time | number(double) | 成交时间  
» create_time_ms | number(double) | 成交时间，保留 3 位小数的毫秒精度  
» contract | string | 合约标识  
» size | integer(int64) | 成交数量  
» price | string | 成交价格 (计价货币)  
» is_internal | boolean | 已废弃  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/trades'
    query_param = 'contract=BTC_USDT_20200814'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/trades?contract=BTC_USDT_20200814 \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": 121234231,
        "create_time": 1514764800,
        "contract": "BTC_USDT",
        "size": -100,
        "price": "100.123"
      }
    ]
    

##  合约市场 K 线图

GET`/delivery/{settle}/candlesticks`

GET `/delivery/{settle}/candlesticks`

_合约市场 K 线图_

如果 `contract` 字段在合约标识前增加了 `mark_` 前缀则返回标记价格数据(如mark_BTC_USD)， 如果增加了 `index_` 则返回指数价格的数据(如index_BTC_USD) K 线图数据单次请求最大返回 2000 个点，指定 from, to 和 interval 的时候注意点数不能过多。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | 请求参数 | string | 是 | 合约标识  
from | 请求参数 | integer(int64) | 否 | 指定 K 线图的起始时间，注意时间格式为秒(s)精度的 Unix 时间戳，不指定则默认为 to - 100 * interval，即向前最多 100 个点的时间  
to | 请求参数 | integer(int64) | 否 | 指定 K 线图的结束时间，不指定则默认当前时间，注意时间格式为秒(s)精度的 Unix 时间戳  
limit | 请求参数 | integer | 否 | 指定数据点的数量，适用于取最近 `limit` 数量的数据，该字段与 `from`, `to` 互斥，如果指定了 `from`, `to` 中的任意字段，该字段会被拒绝  
interval | 请求参数 | string | 否 | 数据点的时间间隔，注意 1w 代表一个自然周，7d 的时间是和 Unix 初始时间对齐  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
interval | 10s  
interval | 30s  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
interval | 2h  
interval | 4h  
interval | 6h  
interval | 8h  
interval | 12h  
interval | 1d  
interval | 7d  
interval | 1w  
interval | 30d  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | [DeliveryCandlestick]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [每个时间粒度的 K 线数据]  
» _None_ | DeliveryCandlestick | 每个时间粒度的 K 线数据  
»» t | number(double) | 秒 s 精度的 Unix 时间戳  
»» v | integer(int64) | 交易量，只有市场行情的 K 线数据里有该值 (合约张数)  
»» c | string | 收盘价 (计价货币)  
»» h | string | 最高价 (计价货币)  
»» l | string | 最低价 (计价货币)  
»» o | string | 开盘价 (计价货币)  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/candlesticks'
    query_param = 'contract=BTC_USDT_20200814'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/candlesticks?contract=BTC_USDT_20200814 \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "t": 1539852480,
        "v": 97151,
        "c": "1.032",
        "h": "1.032",
        "l": "1.032",
        "o": "1.032"
      }
    ]
    

##  获取所有合约交易行情统计

GET`/delivery/{settle}/tickers`

GET `/delivery/{settle}/tickers`

_获取所有合约交易行情统计_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | 请求参数 | string | 否 | 合约标识  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [DeliveryTicker]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» contract | string | 合约标识  
» last | string | 最新成交价  
» change_percentage | string | 涨跌百分比，跌用负数标识，如 -7.45  
» total_size | string | 当前合约总持仓量  
» low_24h | string | 最近24小时最低价  
» high_24h | string | 最近24小时最高价  
» volume_24h | string | 最近24小时成交总量  
» volume_24h_btc | string | 最近24小时成交总量，BTC单位(即将废弃，建议使用 `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle`)  
» volume_24h_usd | string | 最近24小时成交总量，USD单位(即将废弃，建议使用 `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle`)  
» volume_24h_base | string | 最近24小时成交量，以基础货币为单位  
» volume_24h_quote | string | 最近24小时成交量，以计价货币为单位  
» volume_24h_settle | string | 最近24小时成交量，以结算货币为单位  
» mark_price | string | 最近标记价格  
» funding_rate | string | 资金费率  
» funding_rate_indicative | string | 下一周期预测资金费率（已弃用，改用funding_rate）  
» index_price | string | 指数价格  
» quanto_base_rate | string | 已废弃  
» basis_rate | string | 基差率  
» basis_value | string | 基差数值  
» lowest_ask | string | 最新卖方最低价  
» lowest_size | string | 最新卖方最低价的挂单量  
» highest_bid | string | 最新买方最高价  
» highest_size | string | 最新买方最高价的挂单量  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/tickers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/tickers \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "contract": "BTC_USDT",
        "last": "6432",
        "low_24h": "6278",
        "high_24h": "6790",
        "change_percentage": "4.43",
        "total_size": "32323904",
        "volume_24h": "184040233284",
        "volume_24h_btc": "28613220",
        "volume_24h_usd": "184040233284",
        "volume_24h_base": "28613220",
        "volume_24h_quote": "184040233284",
        "volume_24h_settle": "28613220",
        "mark_price": "6534",
        "funding_rate": "0.0001",
        "funding_rate_indicative": "0.0001",
        "index_price": "6531",
        "highest_bid": "34089.7",
        "highest_size": "100",
        "lowest_ask": "34217.9",
        "lowest_size": "1000"
      }
    ]
    

##  合约市场保险基金历史

GET`/delivery/{settle}/insurance`

GET `/delivery/{settle}/insurance`

_合约市场保险基金历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [InsuranceRecord]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» t | integer(int64) | 秒 s 精度的 Unix 时间戳  
» b | string | 保险基金余额  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/insurance'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/insurance \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "t": 1543968000,
        "b": "83.0031"
      }
    ]
    

##  获取合约账号🔒 需要认证

GET`/delivery/{settle}/accounts`

GET `/delivery/{settle}/accounts`

_获取合约账号_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | DeliveryAccount  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» total | string | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
» unrealised_pnl | string | 未实现盈亏  
» position_margin | string | 已废弃  
» order_margin | string | 所有未完成订单的起始保证金  
» available | string | 可用的转出或交易的额度，统一账户下包含授信额度的可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
» point | string | 点卡数额  
» currency | string | 结算币种  
» in_dual_mode | boolean | 是否为双向持仓模式  
» enable_credit | boolean | 是否开启统一账户模式  
» position_initial_margin | string | 头寸占用的起始保证金，适用于统一账户模式  
» maintenance_margin | string | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
» bonus | string | 体验金  
» enable_evolved_classic | boolean | 已废弃  
» cross_order_margin | string | 全仓挂单保证金，适用于新经典账户保证金模式  
» cross_initial_margin | string | 全仓初始保证金，适用于新经典账户保证金模式  
» cross_maintenance_margin | string | 全仓维持保证金，适用于新经典账户保证金模式  
» cross_unrealised_pnl | string | 全仓未实现盈亏，适用于新经典账户保证金模式  
» cross_available | string | 全仓可用额度，适用于新经典账户保证金模式  
» cross_margin_balance | string | 全仓保证金余额，适用于新经典账户保证金模式  
» cross_mmr | string | 全仓维持保证金率，适用于新经典账户保证金模式  
» cross_imr | string | 全仓初始保证金率，适用于新经典账户保证金模式  
» isolated_position_margin | string | 逐仓仓位保证金，适用于新经典账户保证金模式  
» enable_new_dual_mode | boolean | 已废弃  
» margin_mode | integer | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
» enable_tiered_mm | boolean | 是否开启梯度式计算维持保证金  
» history | object | 累计统计数据  
»» dnw | string | 累计转入转出  
»» pnl | string | 累计交易盈亏  
»» fee | string | 累计手续费  
»» refr | string | 累计获取的推荐人返佣  
»» fund | string | 累计资金费用  
»» point_dnw | string | 累计点卡转入转出  
»» point_fee | string | 累计点卡抵扣手续费  
»» point_refr | string | 累计获取的点卡推荐人返佣  
»» bonus_dnw | string | 累计体验金转入转出  
»» bonus_offset | string | 累计体验金抵扣  
  
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
    
    url = '/delivery/usdt/accounts'
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
    url="/delivery/usdt/accounts"
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
      "user": 1666,
      "currency": "USDT",
      "total": "9707.803567115145",
      "unrealised_pnl": "3371.248828",
      "position_margin": "38.712189181",
      "order_margin": "0",
      "available": "9669.091377934145",
      "point": "0",
      "bonus": "0",
      "in_dual_mode": false,
      "enable_evolved_classic": false,
      "cross_initial_margin": "61855.56788525",
      "cross_maintenance_margin": "682.04678105",
      "cross_order_margin": "0",
      "cross_unrealised_pnl": "1501.178222634128",
      "cross_available": "27549.406108813951",
      "cross_margin_balance": "10371.77306201952",
      "cross_mmr": "797.2134",
      "cross_imr": "116.6097",
      "isolated_position_margin": "0",
      "history": {
        "dnw": "10000",
        "pnl": "68.3685",
        "fee": "-1.645812875",
        "refr": "0",
        "fund": "-358.919120009855",
        "point_dnw": "0",
        "point_fee": "0",
        "point_refr": "0",
        "bonus_dnw": "0",
        "bonus_offset": "0"
      },
      "enable_tiered_mm": true
    }
    

##  查询合约账户变更历史🔒 需要认证

GET`/delivery/{settle}/account_book`

GET `/delivery/{settle}/account_book`

_查询合约账户变更历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
type | 请求参数 | string | 否 | 变更类型：  
\- dnw: 转入转出  
\- pnl: 减仓盈亏  
\- fee: 交易手续费  
\- refr: 推荐人返佣  
\- fund: 资金费用  
\- point_dnw: 点卡转入转出  
\- point_fee: 点卡交易手续费  
\- point_refr: 点卡推荐人返佣  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

**type** : 变更类型：  
\- dnw: 转入转出  
\- pnl: 减仓盈亏  
\- fee: 交易手续费  
\- refr: 推荐人返佣  
\- fund: 资金费用  
\- point_dnw: 点卡转入转出  
\- point_fee: 点卡交易手续费  
\- point_refr: 点卡推荐人返佣

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
type | dnw  
type | pnl  
type | fee  
type | refr  
type | fund  
type | point_dnw  
type | point_fee  
type | point_refr  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DeliveryAccountBook]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» time | number(double) | 时间  
» change | string | 变更金额  
» balance | string | 变更后账户余额  
» type | string | 变更类型：  
  
\- dnw: 转入转出  
\- pnl: 减仓盈亏  
\- fee: 交易手续费  
\- refr: 推荐人返佣  
\- fund: 资金费用  
\- point_dnw: 点卡转入转出  
\- point_fee: 点卡交易手续费  
\- point_refr: 点卡推荐人返佣  
\- bonus_offset: 体验金抵扣  
» text | string | 注释  
» contract | string | 合约标识，只有2023-10-30后的数据才有该字段  
» trade_id | string | 成交 id  
» id | string | 账户变更记录 id  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | dnw  
type | pnl  
type | fee  
type | refr  
type | fund  
type | point_dnw  
type | point_fee  
type | point_refr  
type | bonus_offset  
  
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
    
    url = '/delivery/usdt/account_book'
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
    url="/delivery/usdt/account_book"
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
        "time": 1682294400.123456,
        "change": "0.000010152188",
        "balance": "4.59316525194",
        "text": "ETH_USD:6086261",
        "type": "fee",
        "contract": "ETH_USD",
        "trade_id": "1",
        "id": "1"
      }
    ]
    

##  获取用户仓位列表🔒 需要认证

GET`/delivery/{settle}/positions`

GET `/delivery/{settle}/positions`

_获取用户仓位列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DeliveryPosition]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [合约仓位详情]  
» _None_ | DeliveryPosition | 合约仓位详情  
»» user | integer(int64) | 用户ID  
»» contract | string | 合约标识  
»» size | integer(int64) | 头寸大小  
»» leverage | string | 杠杆倍数，0代表全仓，正数代表逐仓  
»» risk_limit | string | 风险限额  
»» leverage_max | string | 当前风险限额下，允许的最大杠杆倍数  
»» maintenance_rate | string | 风险限额的第一档维持保证金率要求  
»» value | string | 按结算币种标记价格计算的合约价值  
»» margin | string | 保证金  
»» entry_price | string | 开仓价格  
»» liq_price | string | 爆仓价格  
»» mark_price | string | 合约当前标记价格  
»» initial_margin | string | 仓位占用的起始保证金，适用于统一账户  
»» maintenance_margin | string | 仓位所需的维持保证金，适用于统一账户  
»» unrealised_pnl | string | 未实现盈亏  
»» realised_pnl | string | 已实现盈亏  
»» pnl_pnl | string | 已实现盈亏-仓位盈亏  
»» pnl_fund | string | 已实现盈亏-资金费用  
»» pnl_fee | string | 已实现盈亏-手续费  
»» history_pnl | string | 已平仓的仓位总盈亏  
»» last_close_pnl | string | 最近一次平仓的盈亏  
»» realised_point | string | 点卡已实现盈亏  
»» history_point | string | 已平仓的点卡总盈亏  
»» adl_ranking | integer | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
»» pending_orders | integer | 当前未完成委托数量  
»» close_order | object|null | 当前平仓委托信息，如果没有平仓则为`null`  
»»» id | integer(int64) | 委托ID  
»»» price | string | 委托价格  
»»» is_liq | boolean | 是否为强制平仓  
»» mode | string | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
»» cross_leverage_limit | string | 全仓模式下的杠杆倍数（即 `leverage` 为 0 时）  
»» update_time | integer(int64) | 最后更新时间  
»» update_id | integer(int64) | 更新id，仓位每更新一次，数值会+1  
»» open_time | integer(int64) | 开仓时间  
»» risk_limit_table | string | 风险限额梯度表id  
»» average_maintenance_rate | string | 平均维持保证金率  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/delivery/usdt/positions'
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
    url="/delivery/usdt/positions"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": -9440,
        "leverage": "0",
        "risk_limit": "100",
        "leverage_max": "100",
        "maintenance_rate": "0.005",
        "value": "3568.62",
        "margin": "4.431548146258",
        "entry_price": "3779.55",
        "liq_price": "99999999",
        "mark_price": "3780.32",
        "unrealised_pnl": "-0.000507486844",
        "realised_pnl": "0.045543982432",
        "pnl_pnl": "0.045543982432",
        "pnl_fund": "0",
        "pnl_fee": "0",
        "history_pnl": "0",
        "last_close_pnl": "0",
        "realised_point": "0",
        "history_point": "0",
        "adl_ranking": 5,
        "pending_orders": 16,
        "close_order": {
          "id": 232323,
          "price": "3779",
          "is_liq": false
        },
        "mode": "single",
        "update_time": 1684994406,
        "update_id": 1,
        "cross_leverage_limit": "0",
        "risk_limit_table": "BIG_HOT_COIN_50X_V2",
        "average_maintenance_rate": "0.005"
      }
    ]
    

##  获取单个仓位信息🔒 需要认证

GET`/delivery/{settle}/positions/{contract}`

GET `/delivery/{settle}/positions/{contract}`

_获取单个仓位信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | URL | string | 是 | 合约标识  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | DeliveryPosition  
  
### 返回格式

状态码 **200**

_合约仓位详情_

名称 | 类型 | 描述  
---|---|---  
» user | integer(int64) | 用户ID  
» contract | string | 合约标识  
» size | integer(int64) | 头寸大小  
» leverage | string | 杠杆倍数，0代表全仓，正数代表逐仓  
» risk_limit | string | 风险限额  
» leverage_max | string | 当前风险限额下，允许的最大杠杆倍数  
» maintenance_rate | string | 风险限额的第一档维持保证金率要求  
» value | string | 按结算币种标记价格计算的合约价值  
» margin | string | 保证金  
» entry_price | string | 开仓价格  
» liq_price | string | 爆仓价格  
» mark_price | string | 合约当前标记价格  
» initial_margin | string | 仓位占用的起始保证金，适用于统一账户  
» maintenance_margin | string | 仓位所需的维持保证金，适用于统一账户  
» unrealised_pnl | string | 未实现盈亏  
» realised_pnl | string | 已实现盈亏  
» pnl_pnl | string | 已实现盈亏-仓位盈亏  
» pnl_fund | string | 已实现盈亏-资金费用  
» pnl_fee | string | 已实现盈亏-手续费  
» history_pnl | string | 已平仓的仓位总盈亏  
» last_close_pnl | string | 最近一次平仓的盈亏  
» realised_point | string | 点卡已实现盈亏  
» history_point | string | 已平仓的点卡总盈亏  
» adl_ranking | integer | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
» pending_orders | integer | 当前未完成委托数量  
» close_order | object|null | 当前平仓委托信息，如果没有平仓则为`null`  
»» id | integer(int64) | 委托ID  
»» price | string | 委托价格  
»» is_liq | boolean | 是否为强制平仓  
» mode | string | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
» cross_leverage_limit | string | 全仓模式下的杠杆倍数（即 `leverage` 为 0 时）  
» update_time | integer(int64) | 最后更新时间  
» update_id | integer(int64) | 更新id，仓位每更新一次，数值会+1  
» open_time | integer(int64) | 开仓时间  
» risk_limit_table | string | 风险限额梯度表id  
» average_maintenance_rate | string | 平均维持保证金率  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/delivery/usdt/positions/BTC_USDT_20200814'
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
    url="/delivery/usdt/positions/BTC_USDT_20200814"
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
      "user": 10000,
      "contract": "BTC_USDT",
      "size": -9440,
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005"
    }
    

##  更新仓位保证金🔒 需要认证

POST`/delivery/{settle}/positions/{contract}/margin`

POST `/delivery/{settle}/positions/{contract}/margin`

_更新仓位保证金_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | URL | string | 是 | 合约标识  
change | 请求参数 | string | 是 | 保证金变化数额，正数增加，负数减少  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | DeliveryPosition  
  
### 返回格式

状态码 **200**

_合约仓位详情_

名称 | 类型 | 描述  
---|---|---  
» user | integer(int64) | 用户ID  
» contract | string | 合约标识  
» size | integer(int64) | 头寸大小  
» leverage | string | 杠杆倍数，0代表全仓，正数代表逐仓  
» risk_limit | string | 风险限额  
» leverage_max | string | 当前风险限额下，允许的最大杠杆倍数  
» maintenance_rate | string | 风险限额的第一档维持保证金率要求  
» value | string | 按结算币种标记价格计算的合约价值  
» margin | string | 保证金  
» entry_price | string | 开仓价格  
» liq_price | string | 爆仓价格  
» mark_price | string | 合约当前标记价格  
» initial_margin | string | 仓位占用的起始保证金，适用于统一账户  
» maintenance_margin | string | 仓位所需的维持保证金，适用于统一账户  
» unrealised_pnl | string | 未实现盈亏  
» realised_pnl | string | 已实现盈亏  
» pnl_pnl | string | 已实现盈亏-仓位盈亏  
» pnl_fund | string | 已实现盈亏-资金费用  
» pnl_fee | string | 已实现盈亏-手续费  
» history_pnl | string | 已平仓的仓位总盈亏  
» last_close_pnl | string | 最近一次平仓的盈亏  
» realised_point | string | 点卡已实现盈亏  
» history_point | string | 已平仓的点卡总盈亏  
» adl_ranking | integer | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
» pending_orders | integer | 当前未完成委托数量  
» close_order | object|null | 当前平仓委托信息，如果没有平仓则为`null`  
»» id | integer(int64) | 委托ID  
»» price | string | 委托价格  
»» is_liq | boolean | 是否为强制平仓  
» mode | string | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
» cross_leverage_limit | string | 全仓模式下的杠杆倍数（即 `leverage` 为 0 时）  
» update_time | integer(int64) | 最后更新时间  
» update_id | integer(int64) | 更新id，仓位每更新一次，数值会+1  
» open_time | integer(int64) | 开仓时间  
» risk_limit_table | string | 风险限额梯度表id  
» average_maintenance_rate | string | 平均维持保证金率  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/delivery/usdt/positions/BTC_USDT_20200814/margin'
    query_param = 'change=0.01'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/delivery/usdt/positions/BTC_USDT_20200814/margin"
    query_param="change=0.01"
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
      "user": 10000,
      "contract": "BTC_USDT",
      "size": -9440,
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005"
    }
    

##  更新仓位杠杆🔒 需要认证

POST`/delivery/{settle}/positions/{contract}/leverage`

POST `/delivery/{settle}/positions/{contract}/leverage`

_更新仓位杠杆_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | URL | string | 是 | 合约标识  
leverage | 请求参数 | string | 是 | 新的杠杆倍数  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | DeliveryPosition  
  
### 返回格式

状态码 **200**

_合约仓位详情_

名称 | 类型 | 描述  
---|---|---  
» user | integer(int64) | 用户ID  
» contract | string | 合约标识  
» size | integer(int64) | 头寸大小  
» leverage | string | 杠杆倍数，0代表全仓，正数代表逐仓  
» risk_limit | string | 风险限额  
» leverage_max | string | 当前风险限额下，允许的最大杠杆倍数  
» maintenance_rate | string | 风险限额的第一档维持保证金率要求  
» value | string | 按结算币种标记价格计算的合约价值  
» margin | string | 保证金  
» entry_price | string | 开仓价格  
» liq_price | string | 爆仓价格  
» mark_price | string | 合约当前标记价格  
» initial_margin | string | 仓位占用的起始保证金，适用于统一账户  
» maintenance_margin | string | 仓位所需的维持保证金，适用于统一账户  
» unrealised_pnl | string | 未实现盈亏  
» realised_pnl | string | 已实现盈亏  
» pnl_pnl | string | 已实现盈亏-仓位盈亏  
» pnl_fund | string | 已实现盈亏-资金费用  
» pnl_fee | string | 已实现盈亏-手续费  
» history_pnl | string | 已平仓的仓位总盈亏  
» last_close_pnl | string | 最近一次平仓的盈亏  
» realised_point | string | 点卡已实现盈亏  
» history_point | string | 已平仓的点卡总盈亏  
» adl_ranking | integer | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
» pending_orders | integer | 当前未完成委托数量  
» close_order | object|null | 当前平仓委托信息，如果没有平仓则为`null`  
»» id | integer(int64) | 委托ID  
»» price | string | 委托价格  
»» is_liq | boolean | 是否为强制平仓  
» mode | string | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
» cross_leverage_limit | string | 全仓模式下的杠杆倍数（即 `leverage` 为 0 时）  
» update_time | integer(int64) | 最后更新时间  
» update_id | integer(int64) | 更新id，仓位每更新一次，数值会+1  
» open_time | integer(int64) | 开仓时间  
» risk_limit_table | string | 风险限额梯度表id  
» average_maintenance_rate | string | 平均维持保证金率  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/delivery/usdt/positions/BTC_USDT_20200814/leverage'
    query_param = 'leverage=10'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/delivery/usdt/positions/BTC_USDT_20200814/leverage"
    query_param="leverage=10"
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
      "user": 10000,
      "contract": "BTC_USDT",
      "size": -9440,
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005"
    }
    

##  更新仓位风险限额🔒 需要认证

POST`/delivery/{settle}/positions/{contract}/risk_limit`

POST `/delivery/{settle}/positions/{contract}/risk_limit`

_更新仓位风险限额_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | URL | string | 是 | 合约标识  
risk_limit | 请求参数 | string | 是 | 新的风险限额  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | DeliveryPosition  
  
### 返回格式

状态码 **200**

_合约仓位详情_

名称 | 类型 | 描述  
---|---|---  
» user | integer(int64) | 用户ID  
» contract | string | 合约标识  
» size | integer(int64) | 头寸大小  
» leverage | string | 杠杆倍数，0代表全仓，正数代表逐仓  
» risk_limit | string | 风险限额  
» leverage_max | string | 当前风险限额下，允许的最大杠杆倍数  
» maintenance_rate | string | 风险限额的第一档维持保证金率要求  
» value | string | 按结算币种标记价格计算的合约价值  
» margin | string | 保证金  
» entry_price | string | 开仓价格  
» liq_price | string | 爆仓价格  
» mark_price | string | 合约当前标记价格  
» initial_margin | string | 仓位占用的起始保证金，适用于统一账户  
» maintenance_margin | string | 仓位所需的维持保证金，适用于统一账户  
» unrealised_pnl | string | 未实现盈亏  
» realised_pnl | string | 已实现盈亏  
» pnl_pnl | string | 已实现盈亏-仓位盈亏  
» pnl_fund | string | 已实现盈亏-资金费用  
» pnl_fee | string | 已实现盈亏-手续费  
» history_pnl | string | 已平仓的仓位总盈亏  
» last_close_pnl | string | 最近一次平仓的盈亏  
» realised_point | string | 点卡已实现盈亏  
» history_point | string | 已平仓的点卡总盈亏  
» adl_ranking | integer | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
» pending_orders | integer | 当前未完成委托数量  
» close_order | object|null | 当前平仓委托信息，如果没有平仓则为`null`  
»» id | integer(int64) | 委托ID  
»» price | string | 委托价格  
»» is_liq | boolean | 是否为强制平仓  
» mode | string | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
» cross_leverage_limit | string | 全仓模式下的杠杆倍数（即 `leverage` 为 0 时）  
» update_time | integer(int64) | 最后更新时间  
» update_id | integer(int64) | 更新id，仓位每更新一次，数值会+1  
» open_time | integer(int64) | 开仓时间  
» risk_limit_table | string | 风险限额梯度表id  
» average_maintenance_rate | string | 平均维持保证金率  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
  
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
    
    url = '/delivery/usdt/positions/BTC_USDT_20200814/risk_limit'
    query_param = 'risk_limit=10'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/delivery/usdt/positions/BTC_USDT_20200814/risk_limit"
    query_param="risk_limit=10"
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
      "user": 10000,
      "contract": "BTC_USDT",
      "size": -9440,
      "leverage": "0",
      "risk_limit": "100",
      "leverage_max": "100",
      "maintenance_rate": "0.005",
      "value": "3568.62",
      "margin": "4.431548146258",
      "entry_price": "3779.55",
      "liq_price": "99999999",
      "mark_price": "3780.32",
      "unrealised_pnl": "-0.000507486844",
      "realised_pnl": "0.045543982432",
      "pnl_pnl": "0.045543982432",
      "pnl_fund": "0",
      "pnl_fee": "0",
      "history_pnl": "0",
      "last_close_pnl": "0",
      "realised_point": "0",
      "history_point": "0",
      "adl_ranking": 5,
      "pending_orders": 16,
      "close_order": {
        "id": 232323,
        "price": "3779",
        "is_liq": false
      },
      "mode": "single",
      "update_time": 1684994406,
      "update_id": 1,
      "cross_leverage_limit": "0",
      "risk_limit_table": "BIG_HOT_COIN_50X_V2",
      "average_maintenance_rate": "0.005"
    }
    

##  查询合约订单列表🔒 需要认证

GET`/delivery/{settle}/orders`

GET `/delivery/{settle}/orders`

_查询合约订单列表_

0 成交的订单在撤单 10 分钟之后无法获取

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 否 | 合约标识  
status | 请求参数 | string | 是 | 基于状态查询订单列表  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
last_id | 请求参数 | string | 否 | 以上个列表的最后一条记录的 ID 作为下个列表的起点  
  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后，在结束之后 1 小时内可查，过期之后只能使用订单 ID  
count_total | 请求参数 | integer | 否 | 是否需要返回列表总数，默认为 0 不返回  
settle | URL | string | 是 | 结算货币  
  
####  详细描述

**last_id** : 以上个列表的最后一条记录的 ID 作为下个列表的起点  
  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后，在结束之后 1 小时内可查，过期之后只能使用订单 ID

####  枚举值列表

枚举值列表参数 | 值  
---|---  
status | open  
status | finished  
count_total | 0  
count_total | 1  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DeliveryOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [合约订单详情]  
» _None_ | DeliveryOrder | 合约订单详情  
»» id | integer(int64) | 合约订单 ID  
»» user | integer | 用户 ID  
»» create_time | number(double) | 订单创建时间  
»» finish_time | number(double) | 订单结束时间，未结束订单无此字段返回  
»» finish_as | string | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
»» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
»» contract | string | 合约标识  
»» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
»» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
»» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
»» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
»» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
»» is_liq | boolean | 是否为强制平仓委托  
»» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
»» left | integer(int64) | 未成交数量  
»» fill_price | string | 成交价  
»» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: ⽼经典模式仓位强制平仓  
\- liq-xxx: a. 新经典模式仓位强制平仓，包含逐仓、单向全仓、双向全仓⾮对冲仓位强平。 b. 统⼀账户单币种保证金模式逐仓强制平仓  
\- hedge-liq-xxx: 新经典模式双向全仓对冲部分强制平仓，即同时平多空仓位  
\- pm_liquidate: 统⼀账户跨币种保证金模式强制平仓  
\- comb_margin_liquidate: 统⼀账户组合保证金模式强制平仓  
\- scm_liquidate: 统⼀账户单币种保证金模式仓位强制平仓  
\- insurance: 保险  
»» tkfr | string | 吃单费率  
»» mkfr | string | 做单费率  
»» refu | integer | 推荐人用户 ID  
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
»» amend_text | string | 用户修改订单时备注的信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
###  返回头部

返回头部状态码 | 头部 | 类型 | 格式 | 描述  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | 分页时指定的 limit  
200 | X-Pagination-Offset | integer |  | 分页时指定的 offset  
200 | X-Pagination-Total | integer |  | 满足条件的列表总数，只有设置 `count_total` 为 1 时才返回  
  
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
    
    url = '/delivery/usdt/orders'
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
    url="/delivery/usdt/orders"
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
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968,
        "size": 6024,
        "iceberg": 0,
        "left": 6024,
        "price": "3765",
        "fill_price": "0",
        "mkfr": "-0.00025",
        "tkfr": "0.00075",
        "tif": "gtc",
        "refu": 0,
        "is_reduce_only": false,
        "is_close": false,
        "is_liq": false,
        "text": "t-my-custom-id",
        "status": "finished",
        "finish_time": 1514764900,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-"
      }
    ]
    

##  合约交易下单🔒 需要认证

POST`/delivery/{settle}/orders`

POST `/delivery/{settle}/orders`

_合约交易下单_

0 成交的订单在撤单 10 分钟之后无法获取

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | DeliveryOrder | 是 |   
» contract | body | string | 是 | 合约标识  
» size | body | integer(int64) | 是 | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
» iceberg | body | integer(int64) | 否 | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
» price | body | string | 否 | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
» close | body | boolean | 否 | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
» reduce_only | body | boolean | 否 | 设置为 true 的时候，为只减仓委托  
» tif | body | string | 否 | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
» text | body | string | 否 | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: ⽼经典模式仓位强制平仓  
\- liq-xxx: a. 新经典模式仓位强制平仓，包含逐仓、单向全仓、双向全仓⾮对冲仓位强平。 b. 统⼀账户单币种保证金模式逐仓强制平仓  
\- hedge-liq-xxx: 新经典模式双向全仓对冲部分强制平仓，即同时平多空仓位  
\- pm_liquidate: 统⼀账户跨币种保证金模式强制平仓  
\- comb_margin_liquidate: 统⼀账户组合保证金模式强制平仓  
\- scm_liquidate: 统⼀账户单币种保证金模式仓位强制平仓  
\- insurance: 保险  
» auto_size | body | string | 否 | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
» stp_act | body | string | 否 | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
settle | URL | string | 是 | 结算货币  
  
####  详细描述

**» tif** : Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消

**» text** : 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: ⽼经典模式仓位强制平仓  
\- liq-xxx: a. 新经典模式仓位强制平仓，包含逐仓、单向全仓、双向全仓⾮对冲仓位强平。 b. 统⼀账户单币种保证金模式逐仓强制平仓  
\- hedge-liq-xxx: 新经典模式双向全仓对冲部分强制平仓，即同时平多空仓位  
\- pm_liquidate: 统⼀账户跨币种保证金模式强制平仓  
\- comb_margin_liquidate: 统⼀账户组合保证金模式强制平仓  
\- scm_liquidate: 统⼀账户单币种保证金模式仓位强制平仓  
\- insurance: 保险

**» stp_act** : Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» tif | gtc  
» tif | ioc  
» tif | poc  
» tif | fok  
» auto_size | close_long  
» auto_size | close_short  
» stp_act | co  
» stp_act | cn  
» stp_act | cb  
» stp_act | -  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 订单详情 | DeliveryOrder  
  
### 返回格式

状态码 **201**

_合约订单详情_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 合约订单 ID  
» user | integer | 用户 ID  
» create_time | number(double) | 订单创建时间  
» finish_time | number(double) | 订单结束时间，未结束订单无此字段返回  
» finish_as | string | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
» contract | string | 合约标识  
» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
» is_liq | boolean | 是否为强制平仓委托  
» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
» left | integer(int64) | 未成交数量  
» fill_price | string | 成交价  
» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: ⽼经典模式仓位强制平仓  
\- liq-xxx: a. 新经典模式仓位强制平仓，包含逐仓、单向全仓、双向全仓⾮对冲仓位强平。 b. 统⼀账户单币种保证金模式逐仓强制平仓  
\- hedge-liq-xxx: 新经典模式双向全仓对冲部分强制平仓，即同时平多空仓位  
\- pm_liquidate: 统⼀账户跨币种保证金模式强制平仓  
\- comb_margin_liquidate: 统⼀账户组合保证金模式强制平仓  
\- scm_liquidate: 统⼀账户单币种保证金模式仓位强制平仓  
\- insurance: 保险  
» tkfr | string | 吃单费率  
» mkfr | string | 做单费率  
» refu | integer | 推荐人用户 ID  
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
» amend_text | string | 用户修改订单时备注的信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/delivery/usdt/orders'
    query_param = ''
    body='{"contract":"BTC_USDT","size":6024,"iceberg":0,"price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-"}'
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
    url="/delivery/usdt/orders"
    query_param=""
    body_param='{"contract":"BTC_USDT","size":6024,"iceberg":0,"price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "contract": "BTC_USDT",
      "size": 6024,
      "iceberg": 0,
      "price": "3765",
      "tif": "gtc",
      "text": "t-my-custom-id",
      "stp_act": "-"
    }
    

> 返回示例

> 201 返回
    
    
    {
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968,
      "size": 6024,
      "iceberg": 0,
      "left": 6024,
      "price": "3765",
      "fill_price": "0",
      "mkfr": "-0.00025",
      "tkfr": "0.00075",
      "tif": "gtc",
      "refu": 0,
      "is_reduce_only": false,
      "is_close": false,
      "is_liq": false,
      "text": "t-my-custom-id",
      "status": "finished",
      "finish_time": 1514764900,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-"
    }
    

##  批量取消状态为 open 的订单🔒 需要认证

DELETE`/delivery/{settle}/orders`

DELETE `/delivery/{settle}/orders`

_批量取消状态为 open 的订单_

0 成交的订单在撤单 10 分钟之后无法获取

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 是 | 合约标识  
side | 请求参数 | string | 否 | 指定全部买单或全部卖单，不指定则两者都包括  
settle | URL | string | 是 | 结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
side | ask  
side | bid  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 批量撤销成功 | [DeliveryOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [合约订单详情]  
» _None_ | DeliveryOrder | 合约订单详情  
»» id | integer(int64) | 合约订单 ID  
»» user | integer | 用户 ID  
»» create_time | number(double) | 订单创建时间  
»» finish_time | number(double) | 订单结束时间，未结束订单无此字段返回  
»» finish_as | string | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
»» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
»» contract | string | 合约标识  
»» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
»» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
»» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
»» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
»» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
»» is_liq | boolean | 是否为强制平仓委托  
»» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
»» left | integer(int64) | 未成交数量  
»» fill_price | string | 成交价  
»» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: ⽼经典模式仓位强制平仓  
\- liq-xxx: a. 新经典模式仓位强制平仓，包含逐仓、单向全仓、双向全仓⾮对冲仓位强平。 b. 统⼀账户单币种保证金模式逐仓强制平仓  
\- hedge-liq-xxx: 新经典模式双向全仓对冲部分强制平仓，即同时平多空仓位  
\- pm_liquidate: 统⼀账户跨币种保证金模式强制平仓  
\- comb_margin_liquidate: 统⼀账户组合保证金模式强制平仓  
\- scm_liquidate: 统⼀账户单币种保证金模式仓位强制平仓  
\- insurance: 保险  
»» tkfr | string | 吃单费率  
»» mkfr | string | 做单费率  
»» refu | integer | 推荐人用户 ID  
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
»» amend_text | string | 用户修改订单时备注的信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/delivery/usdt/orders'
    query_param = 'contract=BTC_USDT_20200814'
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
    url="/delivery/usdt/orders"
    query_param="contract=BTC_USDT_20200814"
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
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968,
        "size": 6024,
        "iceberg": 0,
        "left": 6024,
        "price": "3765",
        "fill_price": "0",
        "mkfr": "-0.00025",
        "tkfr": "0.00075",
        "tif": "gtc",
        "refu": 0,
        "is_reduce_only": false,
        "is_close": false,
        "is_liq": false,
        "text": "t-my-custom-id",
        "status": "finished",
        "finish_time": 1514764900,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-"
      }
    ]
    

##  查询单个订单详情🔒 需要认证

GET`/delivery/{settle}/orders/{order_id}`

GET `/delivery/{settle}/orders/{order_id}`

_查询单个订单详情_

0 成交的订单在撤单 10 分钟之后无法获取

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
order_id | URL | string | 是 | 成功创建订单时返回的 ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单详情 | DeliveryOrder  
  
### 返回格式

状态码 **200**

_合约订单详情_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 合约订单 ID  
» user | integer | 用户 ID  
» create_time | number(double) | 订单创建时间  
» finish_time | number(double) | 订单结束时间，未结束订单无此字段返回  
» finish_as | string | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
» contract | string | 合约标识  
» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
» is_liq | boolean | 是否为强制平仓委托  
» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
» left | integer(int64) | 未成交数量  
» fill_price | string | 成交价  
» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: ⽼经典模式仓位强制平仓  
\- liq-xxx: a. 新经典模式仓位强制平仓，包含逐仓、单向全仓、双向全仓⾮对冲仓位强平。 b. 统⼀账户单币种保证金模式逐仓强制平仓  
\- hedge-liq-xxx: 新经典模式双向全仓对冲部分强制平仓，即同时平多空仓位  
\- pm_liquidate: 统⼀账户跨币种保证金模式强制平仓  
\- comb_margin_liquidate: 统⼀账户组合保证金模式强制平仓  
\- scm_liquidate: 统⼀账户单币种保证金模式仓位强制平仓  
\- insurance: 保险  
» tkfr | string | 吃单费率  
» mkfr | string | 做单费率  
» refu | integer | 推荐人用户 ID  
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
» amend_text | string | 用户修改订单时备注的信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/delivery/usdt/orders/12345'
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
    url="/delivery/usdt/orders/12345"
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
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968,
      "size": 6024,
      "iceberg": 0,
      "left": 6024,
      "price": "3765",
      "fill_price": "0",
      "mkfr": "-0.00025",
      "tkfr": "0.00075",
      "tif": "gtc",
      "refu": 0,
      "is_reduce_only": false,
      "is_close": false,
      "is_liq": false,
      "text": "t-my-custom-id",
      "status": "finished",
      "finish_time": 1514764900,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-"
    }
    

##  撤销单个订单🔒 需要认证

DELETE`/delivery/{settle}/orders/{order_id}`

DELETE `/delivery/{settle}/orders/{order_id}`

_撤销单个订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
order_id | URL | string | 是 | 成功创建订单时返回的 ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单详情 | DeliveryOrder  
  
### 返回格式

状态码 **200**

_合约订单详情_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 合约订单 ID  
» user | integer | 用户 ID  
» create_time | number(double) | 订单创建时间  
» finish_time | number(double) | 订单结束时间，未结束订单无此字段返回  
» finish_as | string | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
» contract | string | 合约标识  
» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
» is_liq | boolean | 是否为强制平仓委托  
» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
» left | integer(int64) | 未成交数量  
» fill_price | string | 成交价  
» text | string | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: ⽼经典模式仓位强制平仓  
\- liq-xxx: a. 新经典模式仓位强制平仓，包含逐仓、单向全仓、双向全仓⾮对冲仓位强平。 b. 统⼀账户单币种保证金模式逐仓强制平仓  
\- hedge-liq-xxx: 新经典模式双向全仓对冲部分强制平仓，即同时平多空仓位  
\- pm_liquidate: 统⼀账户跨币种保证金模式强制平仓  
\- comb_margin_liquidate: 统⼀账户组合保证金模式强制平仓  
\- scm_liquidate: 统⼀账户单币种保证金模式仓位强制平仓  
\- insurance: 保险  
» tkfr | string | 吃单费率  
» mkfr | string | 做单费率  
» refu | integer | 推荐人用户 ID  
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
» amend_text | string | 用户修改订单时备注的信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
  
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
    
    url = '/delivery/usdt/orders/12345'
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
    url="/delivery/usdt/orders/12345"
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
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968,
      "size": 6024,
      "iceberg": 0,
      "left": 6024,
      "price": "3765",
      "fill_price": "0",
      "mkfr": "-0.00025",
      "tkfr": "0.00075",
      "tif": "gtc",
      "refu": 0,
      "is_reduce_only": false,
      "is_close": false,
      "is_liq": false,
      "text": "t-my-custom-id",
      "status": "finished",
      "finish_time": 1514764900,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-"
    }
    

##  查询个人成交记录🔒 需要认证

GET`/delivery/{settle}/my_trades`

GET `/delivery/{settle}/my_trades`

_查询个人成交记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | 请求参数 | string | 否 | 合约标识  
order | 请求参数 | integer(int64) | 否 | 委托ID，如果指定则返回该委托相关数据  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
last_id | 请求参数 | string | 否 | 以上个列表的最后一条记录的 ID 作为下个列表的起点  
  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后，在结束之后 1 小时内可查，过期之后只能使用订单 ID  
count_total | 请求参数 | integer | 否 | 是否需要返回列表总数，默认为 0 不返回  
  
####  详细描述

**last_id** : 以上个列表的最后一条记录的 ID 作为下个列表的起点  
  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后，在结束之后 1 小时内可查，过期之后只能使用订单 ID

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
count_total | 0  
count_total | 1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DeliveryMyTrade]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | integer(int64) | 成交记录 ID  
» create_time | number(double) | 成交时间  
» contract | string | 合约标识  
» order_id | string | 成交记录关联订单 ID  
» size | integer(int64) | 成交数量  
» close_size | integer(int64) | 平仓数量:  
  
close_size=0 && size＞0 开多  
close_size=0 && size＜0 开空  
close_size>0 && size>0 && size <= close_size 平空  
close_size>0 && size>0 && size > close_size 平空且开多  
close_size<0 && size<0 && size >= close_size 平多  
close_size<0 && size<0 && size < close_size 平多且开空  
» price | string | 成交价格  
» role | string | 成交角色， taker - 吃单, maker - 做单  
» text | string | 订单的自定义信息  
» fee | string | 成交手续费  
» point_fee | string | 成交点卡手续费  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
role | taker  
role | maker  
  
###  返回头部

返回头部状态码 | 头部 | 类型 | 格式 | 描述  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | 分页时指定的 limit  
200 | X-Pagination-Offset | integer |  | 分页时指定的 offset  
200 | X-Pagination-Total | integer |  | 满足条件的列表总数，只有设置 `count_total` 为 1 时才返回  
  
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
    
    url = '/delivery/usdt/my_trades'
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
    url="/delivery/usdt/my_trades"
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
        "id": 121234231,
        "create_time": 1514764800.123,
        "contract": "BTC_USDT",
        "order_id": "21893289839",
        "size": 100,
        "price": "100.123",
        "text": "t-123456",
        "fee": "0.01",
        "point_fee": "0",
        "role": "taker",
        "close_size": 0
      }
    ]
    

##  查询平仓历史🔒 需要认证

GET`/delivery/{settle}/position_close`

GET `/delivery/{settle}/position_close`

_查询平仓历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | 请求参数 | string | 否 | 合约标识  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DeliveryPositionClose]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» time | number(double) | 平仓时间  
» contract | string | 合约标识  
» side | string | 多空方向  
  
\- `long`: 做多  
\- `short`: 做空  
» pnl | string | 盈亏  
» pnl_pnl | string | 盈亏-仓位盈亏  
» pnl_fund | string | 盈亏-资金费用  
» pnl_fee | string | 盈亏-手续费  
» text | string | 平仓委托的来源，具体取值参见`order.text`字段  
» max_size | integer(int64) | 最大持仓量  
» accum_size | integer(int64) | 累计平仓量  
» first_open_time | integer(int64) | 开仓时间  
» long_price | string | side为long时表示开仓均价，为short时表示平仓均价  
» short_price | string | side为long时表示平仓均价，为short时表示开仓均价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
side | long  
side | short  
  
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
    
    url = '/delivery/usdt/position_close'
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
    url="/delivery/usdt/position_close"
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
        "time": 1546487347,
        "pnl": "0.00013",
        "pnl_pnl": "0.00011",
        "pnl_fund": "0.00001",
        "pnl_fee": "0.00001",
        "side": "long",
        "contract": "BTC_USDT",
        "text": "web",
        "max_size": "100",
        "accum_size": "100",
        "first_open_time": 1546487347,
        "long_price": "2026.87",
        "short_price": "2544.4"
      }
    ]
    

##  查询强制平仓历史🔒 需要认证

GET`/delivery/{settle}/liquidates`

GET `/delivery/{settle}/liquidates`

_查询强制平仓历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | 请求参数 | string | 否 | 合约标识  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
at | 请求参数 | integer | 否 | 指定时间戳的强平历史  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DeliveryLiquidate]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» time | integer(int64) | 强制平仓时间  
» contract | string | 合约标识  
» leverage | string | 杠杆倍数，公共接口无该字段返回  
» size | integer(int64) | 仓位大小  
» margin | string | 保证金，公共接口无该字段返回  
» entry_price | string | 平均开仓价，公共接口无该字段返回  
» liq_price | string | 强制平仓价，公共接口无该字段返回  
» mark_price | string | 市场标记价，公共接口无该字段返回  
» order_id | integer(int64) | 强平委托ID，公共接口无该字段返回  
» order_price | string | 强平委托价  
» fill_price | string | 强平委托吃单平均成交价  
» left | integer(int64) | 强平委托挂单大小  
  
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
    
    url = '/delivery/usdt/liquidates'
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
    url="/delivery/usdt/liquidates"
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
        "time": 1548654951,
        "contract": "BTC_USDT",
        "size": 600,
        "leverage": "25",
        "margin": "0.006705256878",
        "entry_price": "3536.123",
        "liq_price": "3421.54",
        "mark_price": "3420.27",
        "order_id": 317393847,
        "order_price": "3405",
        "fill_price": "3424",
        "left": 0
      }
    ]
    

##  查询结算记录🔒 需要认证

GET`/delivery/{settle}/settlements`

GET `/delivery/{settle}/settlements`

_查询结算记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | 请求参数 | string | 否 | 合约标识  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
at | 请求参数 | integer | 否 | 指定时间戳的结算历史  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [DeliverySettlement]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» time | integer(int64) | 强制平仓时间  
» contract | string | 合约标识  
» leverage | string | 杠杆倍数  
» size | integer(int64) | 仓位大小  
» margin | string | 保证金  
» entry_price | string | 平均开仓价  
» settle_price | string | 结算价  
» profit | string | 盈利  
» fee | string | 结算费  
  
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
    
    url = '/delivery/usdt/settlements'
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
    url="/delivery/usdt/settlements"
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
        "time": 1548654951,
        "contract": "BTC_USDT",
        "size": 600,
        "leverage": "25",
        "margin": "0.006705256878",
        "entry_price": "3536.123",
        "settle_price": "3421.54",
        "profit": "-6.87498",
        "fee": "0.03079386"
      }
    ]
    

##  查询风险限额等级

GET`/delivery/{settle}/risk_limit_tiers`

GET `/delivery/{settle}/risk_limit_tiers`

_查询风险限额等级_

contract 参数不传,默认查询前 100 个市场的风险限额,limit 和 offset 对应市场维度的分页查询,不对应返回数组的长度,仅当 contract 参数为空时生效

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
contract | 请求参数 | string | 否 | 合约标识  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [DeliveryLimitRiskTiers]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [返回某个指定合同下,不同档位的风险限额配置]  
» _None_ | DeliveryLimitRiskTiers | 返回某个指定合同下,不同档位的风险限额配置  
»» tier | integer(int) | 档位  
»» risk_limit | string | 风险限额  
»» initial_rate | string | 初始保证金率  
»» maintenance_rate | string | 风险限额的第一档维持保证金率要求  
»» leverage_max | string | 最大杠杆  
»» contract | string | 市场,仅当市场分页请求时可见  
»» deduction | string | 维持保证金速算扣减额  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/delivery/usdt/risk_limit_tiers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/delivery/usdt/risk_limit_tiers \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "maintenance_rate": "0.01",
        "tier": 1,
        "initial_rate": "0.02",
        "leverage_max": "50",
        "risk_limit": "20000",
        "contract": "ZTX_USDT",
        "deduction": "0"
      },
      {
        "maintenance_rate": "0.013",
        "tier": 2,
        "initial_rate": "0.025",
        "leverage_max": "40",
        "risk_limit": "30000",
        "contract": "ZTX_USDT",
        "deduction": "60"
      },
      {
        "maintenance_rate": "0.015",
        "tier": 3,
        "initial_rate": "0.02857",
        "leverage_max": "35",
        "risk_limit": "50000",
        "contract": "ZTX_USDT",
        "deduction": "120"
      },
      {
        "maintenance_rate": "0.02",
        "tier": 4,
        "initial_rate": "0.03333",
        "leverage_max": "30",
        "risk_limit": "70000",
        "contract": "ZTX_USDT",
        "deduction": "370"
      },
      {
        "maintenance_rate": "0.025",
        "tier": 5,
        "initial_rate": "0.04",
        "leverage_max": "25",
        "risk_limit": "100000",
        "contract": "ZTX_USDT",
        "deduction": "720"
      }
    ]
    

##  查询自动订单列表🔒 需要认证

GET`/delivery/{settle}/price_orders`

GET `/delivery/{settle}/price_orders`

_查询自动订单列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
status | 请求参数 | string | 是 | 基于状态查询订单列表  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
settle | URL | string | 是 | 结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
status | open  
status | finished  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FuturesPriceTriggeredOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [合约价格单详情]  
» _None_ | FuturesPriceTriggeredOrder | 合约价格单详情  
»» initial | object |   
»»» contract | string | 合约标识  
»»» size | integer(int64) | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
»»» amount | string | 同size参数，用于兼容小数,同时存在时以amount为准  
»»» price | string | 交易价，当价格为 0 时，表示通过市价方式来下单  
»»» tif | string | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
»»» text | string | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
»»» reduce_only | boolean | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
»»» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
»»» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
»» trigger | object |   
»»» strategy_type | integer(int32) | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
»»» price_type | integer(int32) | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
»»» price | string | 价格触发时为价格，价差触发时为价差  
»»» rule | integer(int32) | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
»»» expiration | integer | 最长等待触发时间，超时则取消该订单，单位是秒 s  
»» id | integer(int64) | 自动订单 ID  
»» id_string | string | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
»» user | integer | 用户 ID  
»» create_time | number(double) | 创建时间  
»» finish_time | number(double) | 结束时间  
»» trade_id | integer(int64) | 触发后委托单ID  
»» status | string | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
»» finish_as | string | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
»» reason | string | 订单结束的附加描述信息  
»» order_type | string | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
»» me_order_id | integer(int64) | 委托单止盈止损对应的委托 ID  
»» pos_margin_mode | string | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
  
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
    
    url = '/delivery/usdt/price_orders'
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
    url="/delivery/usdt/price_orders"
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
        "initial": {
          "contract": "BTC_USDT",
          "size": 100,
          "price": "5.03"
        },
        "trigger": {
          "strategy_type": 0,
          "price_type": 0,
          "price": "3000",
          "rule": 1,
          "expiration": 86400
        },
        "id": 1283293,
        "id_string": "1283293",
        "user": 1234,
        "create_time": 1514764800,
        "finish_time": 1514764900,
        "trade_id": 13566,
        "status": "finished",
        "finish_as": "cancelled",
        "reason": "",
        "order_type": "close-long-order",
        "pos_margin_mode": "isolated"
      }
    ]
    

##  创建价格触发订单🔒 需要认证

POST`/delivery/{settle}/price_orders`

POST `/delivery/{settle}/price_orders`

_创建价格触发订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | FuturesPriceTriggeredOrder | 是 |   
» initial | body | object | 是 |   
»» contract | body | string | 是 | 合约标识  
»» size | body | integer(int64) | 否 | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
»» amount | body | string | 否 | 同size参数，用于兼容小数,同时存在时以amount为准  
»» price | body | string | 是 | 交易价，当价格为 0 时，表示通过市价方式来下单  
»» close | body | boolean | 否 | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
»» tif | body | string | 否 | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
»» text | body | string | 否 | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
»» reduce_only | body | boolean | 否 | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
»» auto_size | body | string | 否 | 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  
» trigger | body | object | 是 |   
»» strategy_type | body | integer(int32) | 否 | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
»» price_type | body | integer(int32) | 否 | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
»» price | body | string | 是 | 价格触发时为价格，价差触发时为价差  
»» rule | body | integer(int32) | 是 | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
»» expiration | body | integer | 否 | 最长等待触发时间，超时则取消该订单，单位是秒 s  
» order_type | body | string | 否 | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
» pos_margin_mode | body | string | 否 | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
settle | URL | string | 是 | 结算货币  
  
####  详细描述

**»» size** : 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0

**»» close** : 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false

**»» tif** : Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled

**»» text** : 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端

**»» auto_size** : 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size

**»» strategy_type** : 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价

**»» rule** : 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price

**» order_type** : 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入

**» pos_margin_mode** : 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
»» tif | gtc  
»» tif | ioc  
»» strategy_type | 0  
»» strategy_type | 1  
»» price_type | 0  
»» price_type | 1  
»» price_type | 2  
»» rule | 1  
»» rule | 2  
» pos_margin_mode | isolated  
» pos_margin_mode | cross  
settle | usdt  
  
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
    
    url = '/delivery/usdt/price_orders'
    query_param = ''
    body='{"initial":{"contract":"BTC_USDT","size":100,"price":"5.03"},"trigger":{"strategy_type":0,"price_type":0,"price":"3000","rule":1,"expiration":86400},"order_type":"close-long-order","pos_margin_mode":"isolated"}'
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
    url="/delivery/usdt/price_orders"
    query_param=""
    body_param='{"initial":{"contract":"BTC_USDT","size":100,"price":"5.03"},"trigger":{"strategy_type":0,"price_type":0,"price":"3000","rule":1,"expiration":86400},"order_type":"close-long-order","pos_margin_mode":"isolated"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "initial": {
        "contract": "BTC_USDT",
        "size": 100,
        "price": "5.03"
      },
      "trigger": {
        "strategy_type": 0,
        "price_type": 0,
        "price": "3000",
        "rule": 1,
        "expiration": 86400
      },
      "order_type": "close-long-order",
      "pos_margin_mode": "isolated"
    }
    

> 返回示例

> 201 返回
    
    
    {
      "id": 1432329
    }
    

##  批量取消自动订单🔒 需要认证

DELETE`/delivery/{settle}/price_orders`

DELETE `/delivery/{settle}/price_orders`

_批量取消自动订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 是 | 合约标识  
settle | URL | string | 是 | 结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 批量撤销请求接收并处理，是否成功根据订单列表来决定 | [FuturesPriceTriggeredOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [合约价格单详情]  
» _None_ | FuturesPriceTriggeredOrder | 合约价格单详情  
»» initial | object |   
»»» contract | string | 合约标识  
»»» size | integer(int64) | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
»»» amount | string | 同size参数，用于兼容小数,同时存在时以amount为准  
»»» price | string | 交易价，当价格为 0 时，表示通过市价方式来下单  
»»» tif | string | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
»»» text | string | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
»»» reduce_only | boolean | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
»»» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
»»» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
»» trigger | object |   
»»» strategy_type | integer(int32) | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
»»» price_type | integer(int32) | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
»»» price | string | 价格触发时为价格，价差触发时为价差  
»»» rule | integer(int32) | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
»»» expiration | integer | 最长等待触发时间，超时则取消该订单，单位是秒 s  
»» id | integer(int64) | 自动订单 ID  
»» id_string | string | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
»» user | integer | 用户 ID  
»» create_time | number(double) | 创建时间  
»» finish_time | number(double) | 结束时间  
»» trade_id | integer(int64) | 触发后委托单ID  
»» status | string | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
»» finish_as | string | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
»» reason | string | 订单结束的附加描述信息  
»» order_type | string | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
»» me_order_id | integer(int64) | 委托单止盈止损对应的委托 ID  
»» pos_margin_mode | string | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
  
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
    
    url = '/delivery/usdt/price_orders'
    query_param = 'contract=BTC_USDT'
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
    url="/delivery/usdt/price_orders"
    query_param="contract=BTC_USDT"
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
        "initial": {
          "contract": "BTC_USDT",
          "size": 100,
          "price": "5.03"
        },
        "trigger": {
          "strategy_type": 0,
          "price_type": 0,
          "price": "3000",
          "rule": 1,
          "expiration": 86400
        },
        "id": 1283293,
        "id_string": "1283293",
        "user": 1234,
        "create_time": 1514764800,
        "finish_time": 1514764900,
        "trade_id": 13566,
        "status": "finished",
        "finish_as": "cancelled",
        "reason": "",
        "order_type": "close-long-order",
        "pos_margin_mode": "isolated"
      }
    ]
    

##  查询单个自动订单详情🔒 需要认证

GET`/delivery/{settle}/price_orders/{order_id}`

GET `/delivery/{settle}/price_orders/{order_id}`

_查询单个自动订单详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
order_id | URL | string | 是 | 成功创建订单时返回的 ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 自动订单详情 | FuturesPriceTriggeredOrder  
  
### 返回格式

状态码 **200**

_合约价格单详情_

名称 | 类型 | 描述  
---|---|---  
» initial | object |   
»» contract | string | 合约标识  
»» size | integer(int64) | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
»» amount | string | 同size参数，用于兼容小数,同时存在时以amount为准  
»» price | string | 交易价，当价格为 0 时，表示通过市价方式来下单  
»» tif | string | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
»» text | string | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
»» reduce_only | boolean | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
»» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
»» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
» trigger | object |   
»» strategy_type | integer(int32) | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
»» price_type | integer(int32) | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
»» price | string | 价格触发时为价格，价差触发时为价差  
»» rule | integer(int32) | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
»» expiration | integer | 最长等待触发时间，超时则取消该订单，单位是秒 s  
» id | integer(int64) | 自动订单 ID  
» id_string | string | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
» user | integer | 用户 ID  
» create_time | number(double) | 创建时间  
» finish_time | number(double) | 结束时间  
» trade_id | integer(int64) | 触发后委托单ID  
» status | string | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
» finish_as | string | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
» reason | string | 订单结束的附加描述信息  
» order_type | string | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
» me_order_id | integer(int64) | 委托单止盈止损对应的委托 ID  
» pos_margin_mode | string | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
  
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
    
    url = '/delivery/usdt/price_orders/string'
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
    url="/delivery/usdt/price_orders/string"
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
      "initial": {
        "contract": "BTC_USDT",
        "size": 100,
        "price": "5.03"
      },
      "trigger": {
        "strategy_type": 0,
        "price_type": 0,
        "price": "3000",
        "rule": 1,
        "expiration": 86400
      },
      "id": 1283293,
      "id_string": "1283293",
      "user": 1234,
      "create_time": 1514764800,
      "finish_time": 1514764900,
      "trade_id": 13566,
      "status": "finished",
      "finish_as": "cancelled",
      "reason": "",
      "order_type": "close-long-order",
      "pos_margin_mode": "isolated"
    }
    

##  撤销单个自动订单🔒 需要认证

DELETE`/delivery/{settle}/price_orders/{order_id}`

DELETE `/delivery/{settle}/price_orders/{order_id}`

_撤销单个自动订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 结算货币  
order_id | URL | string | 是 | 成功创建订单时返回的 ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | usdt  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 自动订单详情 | FuturesPriceTriggeredOrder  
  
### 返回格式

状态码 **200**

_合约价格单详情_

名称 | 类型 | 描述  
---|---|---  
» initial | object |   
»» contract | string | 合约标识  
»» size | integer(int64) | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
»» amount | string | 同size参数，用于兼容小数,同时存在时以amount为准  
»» price | string | 交易价，当价格为 0 时，表示通过市价方式来下单  
»» tif | string | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
»» text | string | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
»» reduce_only | boolean | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
»» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
»» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
» trigger | object |   
»» strategy_type | integer(int32) | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
»» price_type | integer(int32) | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
»» price | string | 价格触发时为价格，价差触发时为价差  
»» rule | integer(int32) | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
»» expiration | integer | 最长等待触发时间，超时则取消该订单，单位是秒 s  
» id | integer(int64) | 自动订单 ID  
» id_string | string | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
» user | integer | 用户 ID  
» create_time | number(double) | 创建时间  
» finish_time | number(double) | 结束时间  
» trade_id | integer(int64) | 触发后委托单ID  
» status | string | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
» finish_as | string | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
» reason | string | 订单结束的附加描述信息  
» order_type | string | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
» me_order_id | integer(int64) | 委托单止盈止损对应的委托 ID  
» pos_margin_mode | string | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
  
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
    
    url = '/delivery/usdt/price_orders/string'
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
    url="/delivery/usdt/price_orders/string"
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
      "initial": {
        "contract": "BTC_USDT",
        "size": 100,
        "price": "5.03"
      },
      "trigger": {
        "strategy_type": 0,
        "price_type": 0,
        "price": "3000",
        "rule": 1,
        "expiration": 86400
      },
      "id": 1283293,
      "id_string": "1283293",
      "user": 1234,
      "create_time": 1514764800,
      "finish_time": 1514764900,
      "trade_id": 13566,
      "status": "finished",
      "finish_as": "cancelled",
      "reason": "",
      "order_type": "close-long-order",
      "pos_margin_mode": "isolated"
    }
    

#  模型

##  DeliveryLimitRiskTiers

_返回某个指定合同下,不同档位的风险限额配置_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
tier | integer(int) | false | none | 档位  
risk_limit | string | false | none | 风险限额  
initial_rate | string | false | none | 初始保证金率  
maintenance_rate | string | false | none | 风险限额的第一档维持保证金率要求  
leverage_max | string | false | none | 最大杠杆  
contract | string | false | none | 市场,仅当市场分页请求时可见  
deduction | string | false | none | 维持保证金速算扣减额  
      
    
    {
      "tier": 0,
      "risk_limit": "string",
      "initial_rate": "string",
      "maintenance_rate": "string",
      "leverage_max": "string",
      "contract": "string",
      "deduction": "string"
    }
    
    

##  DeliveryMyTrade

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 成交记录 ID  
create_time | number(double) | false | none | 成交时间  
contract | string | false | none | 合约标识  
order_id | string | false | none | 成交记录关联订单 ID  
size | integer(int64) | false | none | 成交数量  
close_size | integer(int64) | false | none | 平仓数量:  
  
close_size=0 && size＞0 开多  
close_size=0 && size＜0 开空  
close_size>0 && size>0 && size <= close_size 平空  
close_size>0 && size>0 && size > close_size 平空且开多  
close_size<0 && size<0 && size >= close_size 平多  
close_size<0 && size<0 && size < close_size 平多且开空  
price | string | false | none | 成交价格  
role | string | false | none | 成交角色， taker - 吃单, maker - 做单  
text | string | false | none | 订单的自定义信息  
fee | string | false | none | 成交手续费  
point_fee | string | false | none | 成交点卡手续费  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
role | taker  
role | maker  
      
    
    {
      "id": 0,
      "create_time": 0,
      "contract": "string",
      "order_id": "string",
      "size": 0,
      "close_size": 0,
      "price": "string",
      "role": "taker",
      "text": "string",
      "fee": "string",
      "point_fee": "string"
    }
    
    

##  DeliveryOrderBook

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 深度更新 ID，深度每发生一次变化，该 ID 加 1，只有设置 `with_id=true` 时才返回  
current | number(double) | false | none | 接口数据返回时间戳  
update | number(double) | false | none | 深度变化时间戳  
asks | array | true | none | 卖方深度列表  
» DeliveryOrderBookItem | object | false | none | none  
»» p | string | false | none | 价格 (计价货币)  
»» s | integer(int64) | false | none | 数量  
» bids | array | true | none | 买方深度列表  
»» DeliveryOrderBookItem | object | false | none | none  
»»» p | string | false | none | 价格 (计价货币)  
»»» s | integer(int64) | false | none | 数量  
      
    
    {
      "id": 0,
      "current": 0,
      "update": 0,
      "asks": [
        {
          "p": "string",
          "s": 0
        }
      ],
      "bids": [
        {
          "p": "string",
          "s": 0
        }
      ]
    }
    
    

##  DeliveryTicker

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
contract | string | false | none | 合约标识  
last | string | false | none | 最新成交价  
change_percentage | string | false | none | 涨跌百分比，跌用负数标识，如 -7.45  
total_size | string | false | none | 当前合约总持仓量  
low_24h | string | false | none | 最近24小时最低价  
high_24h | string | false | none | 最近24小时最高价  
volume_24h | string | false | none | 最近24小时成交总量  
volume_24h_btc | string | false | none | 最近24小时成交总量，BTC单位(即将废弃，建议使用 `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle`)  
volume_24h_usd | string | false | none | 最近24小时成交总量，USD单位(即将废弃，建议使用 `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle`)  
volume_24h_base | string | false | none | 最近24小时成交量，以基础货币为单位  
volume_24h_quote | string | false | none | 最近24小时成交量，以计价货币为单位  
volume_24h_settle | string | false | none | 最近24小时成交量，以结算货币为单位  
mark_price | string | false | none | 最近标记价格  
funding_rate | string | false | none | 资金费率  
funding_rate_indicative | string | false | none | 下一周期预测资金费率（已弃用，改用funding_rate）  
index_price | string | false | none | 指数价格  
quanto_base_rate | string | false | none | 已废弃  
basis_rate | string | false | none | 基差率  
basis_value | string | false | none | 基差数值  
lowest_ask | string | false | none | 最新卖方最低价  
lowest_size | string | false | none | 最新卖方最低价的挂单量  
highest_bid | string | false | none | 最新买方最高价  
highest_size | string | false | none | 最新买方最高价的挂单量  
      
    
    {
      "contract": "string",
      "last": "string",
      "change_percentage": "string",
      "total_size": "string",
      "low_24h": "string",
      "high_24h": "string",
      "volume_24h": "string",
      "volume_24h_btc": "string",
      "volume_24h_usd": "string",
      "volume_24h_base": "string",
      "volume_24h_quote": "string",
      "volume_24h_settle": "string",
      "mark_price": "string",
      "funding_rate": "string",
      "funding_rate_indicative": "string",
      "index_price": "string",
      "quanto_base_rate": "string",
      "basis_rate": "string",
      "basis_value": "string",
      "lowest_ask": "string",
      "lowest_size": "string",
      "highest_bid": "string",
      "highest_size": "string"
    }
    
    

##  InsuranceRecord

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
t | integer(int64) | false | none | 秒 s 精度的 Unix 时间戳  
b | string | false | none | 保险基金余额  
      
    
    {
      "t": 0,
      "b": "string"
    }
    
    

##  DeliveryLiquidate

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
time | integer(int64) | false | 只读 | 强制平仓时间  
contract | string | false | 只读 | 合约标识  
leverage | string | false | 只读 | 杠杆倍数，公共接口无该字段返回  
size | integer(int64) | false | 只读 | 仓位大小  
margin | string | false | 只读 | 保证金，公共接口无该字段返回  
entry_price | string | false | 只读 | 平均开仓价，公共接口无该字段返回  
liq_price | string | false | 只读 | 强制平仓价，公共接口无该字段返回  
mark_price | string | false | 只读 | 市场标记价，公共接口无该字段返回  
order_id | integer(int64) | false | 只读 | 强平委托ID，公共接口无该字段返回  
order_price | string | false | 只读 | 强平委托价  
fill_price | string | false | 只读 | 强平委托吃单平均成交价  
left | integer(int64) | false | 只读 | 强平委托挂单大小  
      
    
    {
      "time": 0,
      "contract": "string",
      "leverage": "string",
      "size": 0,
      "margin": "string",
      "entry_price": "string",
      "liq_price": "string",
      "mark_price": "string",
      "order_id": 0,
      "order_price": "string",
      "fill_price": "string",
      "left": 0
    }
    
    

##  DeliverySettlement

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
time | integer(int64) | false | 只读 | 强制平仓时间  
contract | string | false | 只读 | 合约标识  
leverage | string | false | 只读 | 杠杆倍数  
size | integer(int64) | false | 只读 | 仓位大小  
margin | string | false | 只读 | 保证金  
entry_price | string | false | 只读 | 平均开仓价  
settle_price | string | false | 只读 | 结算价  
profit | string | false | 只读 | 盈利  
fee | string | false | 只读 | 结算费  
      
    
    {
      "time": 0,
      "contract": "string",
      "leverage": "string",
      "size": 0,
      "margin": "string",
      "entry_price": "string",
      "settle_price": "string",
      "profit": "string",
      "fee": "string"
    }
    
    

##  DeliveryContract

_合约详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
name | string | false | none | 合约标识  
underlying | string | false | none | 标的物  
cycle | string | false | none | 周期类型, 季度合约, 周合约等  
type | string | false | none | 合约类型, inverse - 反向合约, direct - 正向合约  
quanto_multiplier | string | false | none | 合约乘数，表示一张合约的面值为多少个标的物币种  
leverage_min | string | false | none | 最小杠杆  
leverage_max | string | false | none | 最大杠杆  
maintenance_rate | string | false | none | 风险限额的第一档维持保证金率要求  
mark_type | string | false | none | 已废弃  
mark_price | string | false | none | 当前标记价格  
index_price | string | false | none | 当前指数价格  
last_price | string | false | none | 上一次成交价格  
maker_fee_rate | string | false | none | 挂单成交的手续费率，负数代表返还后续费  
taker_fee_rate | string | false | none | 吃单成交的手续费率  
order_price_round | string | false | none | 委托价格最小单位  
mark_price_round | string | false | none | 标记价格的最小单位  
basis_rate | string | false | none | 当前合理基差率  
basis_value | string | false | none | 当前合理基差值  
basis_impact_value | string | false | none | 计算合理基差率时加权深度影响额  
settle_price | string | false | none | 预计结算价格  
settle_price_interval | integer | false | none | 结算价格更新间隔  
settle_price_duration | integer | false | none | 加权平均计算结算价格时长, 单位秒  
expire_time | integer(int64) | false | none | 合约到期时间戳  
risk_limit_base | string | false | none | 基础风险限额  
risk_limit_step | string | false | none | 风险限额调整步长  
risk_limit_max | string | false | none | 合约允许的最大风险限额  
order_size_min | integer(int64) | false | none | 最小下单数量  
order_size_max | integer(int64) | false | none | 最大下单数量  
order_price_deviate | string | false | none | 下单价与当前标记价格允许的正负偏移量， 即下单价 `order_price` 需满足如下条件:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | false | none | 被推荐人享受交易费率折扣  
ref_rebate_rate | string | false | none | 推荐人享受交易费率返佣比例  
orderbook_id | integer(int64) | false | none | orderbook更新ID  
trade_id | integer(int64) | false | none | 当前成交ID  
trade_size | integer(int64) | false | none | 历史累计成交  
position_size | integer(int64) | false | none | 当前做多用户持有仓位总和  
config_change_time | number(double) | false | none | 配置最后更新时间  
in_delisting | boolean | false | none | 合约下线中  
orders_limit | integer | false | none | 最多挂单数量  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
cycle | WEEKLY  
cycle | BI-WEEKLY  
cycle | QUARTERLY  
cycle | BI-QUARTERLY  
type | inverse  
type | direct  
mark_type | internal  
mark_type | index  
      
    
    {
      "name": "string",
      "underlying": "string",
      "cycle": "WEEKLY",
      "type": "inverse",
      "quanto_multiplier": "string",
      "leverage_min": "string",
      "leverage_max": "string",
      "maintenance_rate": "string",
      "mark_type": "internal",
      "mark_price": "string",
      "index_price": "string",
      "last_price": "string",
      "maker_fee_rate": "string",
      "taker_fee_rate": "string",
      "order_price_round": "string",
      "mark_price_round": "string",
      "basis_rate": "string",
      "basis_value": "string",
      "basis_impact_value": "string",
      "settle_price": "string",
      "settle_price_interval": 0,
      "settle_price_duration": 0,
      "expire_time": 0,
      "risk_limit_base": "string",
      "risk_limit_step": "string",
      "risk_limit_max": "string",
      "order_size_min": 0,
      "order_size_max": 0,
      "order_price_deviate": "string",
      "ref_discount_rate": "string",
      "ref_rebate_rate": "string",
      "orderbook_id": 0,
      "trade_id": 0,
      "trade_size": 0,
      "position_size": 0,
      "config_change_time": 0,
      "in_delisting": true,
      "orders_limit": 0
    }
    
    

##  DeliveryPositionClose

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
time | number(double) | false | 只读 | 平仓时间  
contract | string | false | 只读 | 合约标识  
side | string | false | 只读 | 多空方向  
  
\- `long`: 做多  
\- `short`: 做空  
pnl | string | false | 只读 | 盈亏  
pnl_pnl | string | false | 只读 | 盈亏-仓位盈亏  
pnl_fund | string | false | 只读 | 盈亏-资金费用  
pnl_fee | string | false | 只读 | 盈亏-手续费  
text | string | false | 只读 | 平仓委托的来源，具体取值参见`order.text`字段  
max_size | integer(int64) | false | 只读 | 最大持仓量  
accum_size | integer(int64) | false | 只读 | 累计平仓量  
first_open_time | integer(int64) | false | 只读 | 开仓时间  
long_price | string | false | 只读 | side为long时表示开仓均价，为short时表示平仓均价  
short_price | string | false | 只读 | side为long时表示平仓均价，为short时表示开仓均价  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
side | long  
side | short  
      
    
    {
      "time": 0,
      "contract": "string",
      "side": "long",
      "pnl": "string",
      "pnl_pnl": "string",
      "pnl_fund": "string",
      "pnl_fee": "string",
      "text": "string",
      "max_size": 0,
      "accum_size": 0,
      "first_open_time": 0,
      "long_price": "string",
      "short_price": "string"
    }
    
    

##  DeliveryCandlestick

_每个时间粒度的 K 线数据_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
t | number(double) | false | none | 秒 s 精度的 Unix 时间戳  
v | integer(int64) | false | none | 交易量，只有市场行情的 K 线数据里有该值 (合约张数)  
c | string | false | none | 收盘价 (计价货币)  
h | string | false | none | 最高价 (计价货币)  
l | string | false | none | 最低价 (计价货币)  
o | string | false | none | 开盘价 (计价货币)  
      
    
    {
      "t": 0,
      "v": 0,
      "c": "string",
      "h": "string",
      "l": "string",
      "o": "string"
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
    
    

##  DeliveryAccount

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
total | string | false | none | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | false | none | 未实现盈亏  
position_margin | string | false | none | 已废弃  
order_margin | string | false | none | 所有未完成订单的起始保证金  
available | string | false | none | 可用的转出或交易的额度，统一账户下包含授信额度的可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
point | string | false | none | 点卡数额  
currency | string | false | none | 结算币种  
in_dual_mode | boolean | false | none | 是否为双向持仓模式  
enable_credit | boolean | false | none | 是否开启统一账户模式  
position_initial_margin | string | false | none | 头寸占用的起始保证金，适用于统一账户模式  
maintenance_margin | string | false | none | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
bonus | string | false | none | 体验金  
enable_evolved_classic | boolean | false | none | 已废弃  
cross_order_margin | string | false | none | 全仓挂单保证金，适用于新经典账户保证金模式  
cross_initial_margin | string | false | none | 全仓初始保证金，适用于新经典账户保证金模式  
cross_maintenance_margin | string | false | none | 全仓维持保证金，适用于新经典账户保证金模式  
cross_unrealised_pnl | string | false | none | 全仓未实现盈亏，适用于新经典账户保证金模式  
cross_available | string | false | none | 全仓可用额度，适用于新经典账户保证金模式  
cross_margin_balance | string | false | none | 全仓保证金余额，适用于新经典账户保证金模式  
cross_mmr | string | false | none | 全仓维持保证金率，适用于新经典账户保证金模式  
cross_imr | string | false | none | 全仓初始保证金率，适用于新经典账户保证金模式  
isolated_position_margin | string | false | none | 逐仓仓位保证金，适用于新经典账户保证金模式  
enable_new_dual_mode | boolean | false | none | 已废弃  
margin_mode | integer | false | none | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
enable_tiered_mm | boolean | false | none | 是否开启梯度式计算维持保证金  
history | object | false | none | 累计统计数据  
» dnw | string | false | none | 累计转入转出  
» pnl | string | false | none | 累计交易盈亏  
» fee | string | false | none | 累计手续费  
» refr | string | false | none | 累计获取的推荐人返佣  
» fund | string | false | none | 累计资金费用  
» point_dnw | string | false | none | 累计点卡转入转出  
» point_fee | string | false | none | 累计点卡抵扣手续费  
» point_refr | string | false | none | 累计获取的点卡推荐人返佣  
» bonus_dnw | string | false | none | 累计体验金转入转出  
» bonus_offset | string | false | none | 累计体验金抵扣  
      
    
    {
      "total": "string",
      "unrealised_pnl": "string",
      "position_margin": "string",
      "order_margin": "string",
      "available": "string",
      "point": "string",
      "currency": "string",
      "in_dual_mode": true,
      "enable_credit": true,
      "position_initial_margin": "string",
      "maintenance_margin": "string",
      "bonus": "string",
      "enable_evolved_classic": true,
      "cross_order_margin": "string",
      "cross_initial_margin": "string",
      "cross_maintenance_margin": "string",
      "cross_unrealised_pnl": "string",
      "cross_available": "string",
      "cross_margin_balance": "string",
      "cross_mmr": "string",
      "cross_imr": "string",
      "isolated_position_margin": "string",
      "enable_new_dual_mode": true,
      "margin_mode": 0,
      "enable_tiered_mm": true,
      "history": {
        "dnw": "string",
        "pnl": "string",
        "fee": "string",
        "refr": "string",
        "fund": "string",
        "point_dnw": "string",
        "point_fee": "string",
        "point_refr": "string",
        "bonus_dnw": "string",
        "bonus_offset": "string"
      }
    }
    
    

##  DeliveryOrder

_合约订单详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | 只读 | 合约订单 ID  
user | integer | false | 只读 | 用户 ID  
create_time | number(double) | false | 只读 | 订单创建时间  
finish_time | number(double) | false | 只读 | 订单结束时间，未结束订单无此字段返回  
finish_as | string | false | 只读 | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | false | 只读 | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
contract | string | true | none | 合约标识  
size | integer(int64) | true | none | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
iceberg | integer(int64) | false | none | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | false | none | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | false | 只写 | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | false | 只读 | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | false | 只写 | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | false | 只读 | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | false | 只读 | 是否为强制平仓委托  
tif | string | false | none | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | integer(int64) | false | 只读 | 未成交数量  
fill_price | string | false | 只读 | 成交价  
text | string | false | none | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: ⽼经典模式仓位强制平仓  
\- liq-xxx: a. 新经典模式仓位强制平仓，包含逐仓、单向全仓、双向全仓⾮对冲仓位强平。 b. 统⼀账户单币种保证金模式逐仓强制平仓  
\- hedge-liq-xxx: 新经典模式双向全仓对冲部分强制平仓，即同时平多空仓位  
\- pm_liquidate: 统⼀账户跨币种保证金模式强制平仓  
\- comb_margin_liquidate: 统⼀账户组合保证金模式强制平仓  
\- scm_liquidate: 统⼀账户单币种保证金模式仓位强制平仓  
\- insurance: 保险  
tkfr | string | false | 只读 | 吃单费率  
mkfr | string | false | 只读 | 做单费率  
refu | integer | false | 只读 | 推荐人用户 ID  
auto_size | string | false | 只写 | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
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
amend_text | string | false | 只读 | 用户修改订单时备注的信息  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
finish_as | filled  
finish_as | cancelled  
finish_as | liquidated  
finish_as | ioc  
finish_as | auto_deleveraged  
finish_as | reduce_only  
finish_as | position_closed  
finish_as | reduce_out  
finish_as | stp  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
tif | fok  
auto_size | close_long  
auto_size | close_short  
stp_act | co  
stp_act | cn  
stp_act | cb  
stp_act | -  
      
    
    {
      "id": 0,
      "user": 0,
      "create_time": 0,
      "finish_time": 0,
      "finish_as": "filled",
      "status": "open",
      "contract": "string",
      "size": 0,
      "iceberg": 0,
      "price": "string",
      "close": false,
      "is_close": true,
      "reduce_only": false,
      "is_reduce_only": true,
      "is_liq": true,
      "tif": "gtc",
      "left": 0,
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "auto_size": "close_long",
      "stp_id": 0,
      "stp_act": "co",
      "amend_text": "string"
    }
    
    

##  FuturesPriceTriggeredOrder

_合约价格单详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
initial | object | true | none | none  
» contract | string | true | none | 合约标识  
» size | integer(int64) | false | none | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
» amount | string | false | none | 同size参数，用于兼容小数,同时存在时以amount为准  
» price | string | true | none | 交易价，当价格为 0 时，表示通过市价方式来下单  
» close | boolean | false | 只写 | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
» tif | string | false | none | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
» text | string | false | none | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
» reduce_only | boolean | false | none | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
» auto_size | string | false | 只写 | 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  
» is_reduce_only | boolean | false | 只读 | 是否为只减仓委托。对应请求中的`reduce_only`。  
» is_close | boolean | false | 只读 | 是否为平仓委托。对应请求中的`close`。  
trigger | object | true | none | none  
» strategy_type | integer(int32) | false | none | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
» price_type | integer(int32) | false | none | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
» price | string | true | none | 价格触发时为价格，价差触发时为价差  
» rule | integer(int32) | true | none | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
» expiration | integer | false | none | 最长等待触发时间，超时则取消该订单，单位是秒 s  
id | integer(int64) | false | 只读 | 自动订单 ID  
id_string | string | false | 只读 | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
user | integer | false | 只读 | 用户 ID  
create_time | number(double) | false | 只读 | 创建时间  
finish_time | number(double) | false | 只读 | 结束时间  
trade_id | integer(int64) | false | 只读 | 触发后委托单ID  
status | string | false | 只读 | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
finish_as | string | false | 只读 | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
reason | string | false | 只读 | 订单结束的附加描述信息  
order_type | string | false | none | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
me_order_id | integer(int64) | false | 只读 | 委托单止盈止损对应的委托 ID  
pos_margin_mode | string | false | none | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
tif | gtc  
tif | ioc  
strategy_type | 0  
strategy_type | 1  
price_type | 0  
price_type | 1  
price_type | 2  
rule | 1  
rule | 2  
status | open  
status | finished  
status | inactive  
status | invalid  
finish_as | cancelled  
finish_as | succeeded  
finish_as | failed  
finish_as | expired  
pos_margin_mode | isolated  
pos_margin_mode | cross  
      
    
    {
      "initial": {
        "contract": "string",
        "size": 0,
        "amount": "string",
        "price": "string",
        "close": false,
        "tif": "gtc",
        "text": "string",
        "reduce_only": false,
        "auto_size": "string",
        "is_reduce_only": true,
        "is_close": true
      },
      "trigger": {
        "strategy_type": 0,
        "price_type": 0,
        "price": "string",
        "rule": 1,
        "expiration": 0
      },
      "id": 0,
      "id_string": "string",
      "user": 0,
      "create_time": 0,
      "finish_time": 0,
      "trade_id": 0,
      "status": "open",
      "finish_as": "cancelled",
      "reason": "string",
      "order_type": "string",
      "me_order_id": 0,
      "pos_margin_mode": "isolated"
    }
    
    

##  DeliveryTrade

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 成交记录 ID  
create_time | number(double) | false | none | 成交时间  
create_time_ms | number(double) | false | none | 成交时间，保留 3 位小数的毫秒精度  
contract | string | false | none | 合约标识  
size | integer(int64) | false | none | 成交数量  
price | string | false | none | 成交价格 (计价货币)  
is_internal | boolean | false | none | 已废弃  
      
    
    {
      "id": 0,
      "create_time": 0,
      "create_time_ms": 0,
      "contract": "string",
      "size": 0,
      "price": "string",
      "is_internal": true
    }
    
    

##  DeliveryAccountBook

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
time | number(double) | false | none | 时间  
change | string | false | none | 变更金额  
balance | string | false | none | 变更后账户余额  
type | string | false | none | 变更类型：  
  
\- dnw: 转入转出  
\- pnl: 减仓盈亏  
\- fee: 交易手续费  
\- refr: 推荐人返佣  
\- fund: 资金费用  
\- point_dnw: 点卡转入转出  
\- point_fee: 点卡交易手续费  
\- point_refr: 点卡推荐人返佣  
\- bonus_offset: 体验金抵扣  
text | string | false | none | 注释  
contract | string | false | none | 合约标识，只有2023-10-30后的数据才有该字段  
trade_id | string | false | none | 成交 id  
id | string | false | none | 账户变更记录 id  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | dnw  
type | pnl  
type | fee  
type | refr  
type | fund  
type | point_dnw  
type | point_fee  
type | point_refr  
type | bonus_offset  
      
    
    {
      "time": 0,
      "change": "string",
      "balance": "string",
      "type": "dnw",
      "text": "string",
      "contract": "string",
      "trade_id": "string",
      "id": "string"
    }
    
    

##  DeliveryPosition

_合约仓位详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user | integer(int64) | false | 只读 | 用户ID  
contract | string | false | 只读 | 合约标识  
size | integer(int64) | false | 只读 | 头寸大小  
leverage | string | false | none | 杠杆倍数，0代表全仓，正数代表逐仓  
risk_limit | string | false | none | 风险限额  
leverage_max | string | false | 只读 | 当前风险限额下，允许的最大杠杆倍数  
maintenance_rate | string | false | 只读 | 风险限额的第一档维持保证金率要求  
value | string | false | 只读 | 按结算币种标记价格计算的合约价值  
margin | string | false | none | 保证金  
entry_price | string | false | 只读 | 开仓价格  
liq_price | string | false | 只读 | 爆仓价格  
mark_price | string | false | 只读 | 合约当前标记价格  
initial_margin | string | false | 只读 | 仓位占用的起始保证金，适用于统一账户  
maintenance_margin | string | false | 只读 | 仓位所需的维持保证金，适用于统一账户  
unrealised_pnl | string | false | 只读 | 未实现盈亏  
realised_pnl | string | false | 只读 | 已实现盈亏  
pnl_pnl | string | false | 只读 | 已实现盈亏-仓位盈亏  
pnl_fund | string | false | 只读 | 已实现盈亏-资金费用  
pnl_fee | string | false | 只读 | 已实现盈亏-手续费  
history_pnl | string | false | 只读 | 已平仓的仓位总盈亏  
last_close_pnl | string | false | 只读 | 最近一次平仓的盈亏  
realised_point | string | false | 只读 | 点卡已实现盈亏  
history_point | string | false | 只读 | 已平仓的点卡总盈亏  
adl_ranking | integer | false | 只读 | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | false | 只读 | 当前未完成委托数量  
close_order | object|null | false | 只读 | 当前平仓委托信息，如果没有平仓则为`null`  
» id | integer(int64) | false | none | 委托ID  
» price | string | false | none | 委托价格  
» is_liq | boolean | false | none | 是否为强制平仓  
mode | string | false | none | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | false | none | 全仓模式下的杠杆倍数（即 `leverage` 为 0 时）  
update_time | integer(int64) | false | 只读 | 最后更新时间  
update_id | integer(int64) | false | 只读 | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | false | none | 开仓时间  
risk_limit_table | string | false | 只读 | 风险限额梯度表id  
average_maintenance_rate | string | false | 只读 | 平均维持保证金率  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
mode | single  
mode | dual_long  
mode | dual_short  
      
    
    {
      "user": 0,
      "contract": "string",
      "size": 0,
      "leverage": "string",
      "risk_limit": "string",
      "leverage_max": "string",
      "maintenance_rate": "string",
      "value": "string",
      "margin": "string",
      "entry_price": "string",
      "liq_price": "string",
      "mark_price": "string",
      "initial_margin": "string",
      "maintenance_margin": "string",
      "unrealised_pnl": "string",
      "realised_pnl": "string",
      "pnl_pnl": "string",
      "pnl_fund": "string",
      "pnl_fee": "string",
      "history_pnl": "string",
      "last_close_pnl": "string",
      "realised_point": "string",
      "history_point": "string",
      "adl_ranking": 0,
      "pending_orders": 0,
      "close_order": {
        "id": 0,
        "price": "string",
        "is_liq": true
      },
      "mode": "single",
      "cross_leverage_limit": "string",
      "update_time": 0,
      "update_id": 0,
      "open_time": 0,
      "risk_limit_table": "string",
      "average_maintenance_rate": "string"
    }