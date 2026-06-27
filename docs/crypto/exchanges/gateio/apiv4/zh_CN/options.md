---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/options
api_type: Trading
updated_at: 2026-05-27 20:17:31.621652
---

# Options

期权接口

##  列出所有标的

GET`/options/underlyings`

GET `/options/underlyings`

_列出所有标的_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsUnderlying]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» name | string | 标的名  
» index_price | string | 现货指数价格 (计价货币)  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/underlyings'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/underlyings \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "name": "BTC_USDT",
        "index_price": "70000"
      }
    ]
    

##  列出所有到期时间

GET`/options/expirations`

GET `/options/expirations`

_列出所有到期时间_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 标的物 (可透过列出所有标的接口获得)  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列出指定标的下的到期时间 | [integer]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» _None_ | integer(int64) | 到期时间的Unix时间戳  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/expirations'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/expirations?underlying=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      1637913600
    ]
    

##  列出指定标的和到期时间下的所有合约

GET`/options/contracts`

GET `/options/contracts`

_列出指定标的和到期时间下的所有合约_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 标的物 (可透过列出所有标的接口获得)  
expiration | 请求参数 | integer(int64) | 否 | 到期时间的Unix时间戳  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsContract]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [期权合约详情]  
» _None_ | OptionsContract | 期权合约详情  
»» name | string | 期权合约标识  
»» tag | string | 到期周期，有day、week、month  
»» create_time | number(double) | 创建时间  
»» expiration_time | number(double) | 到期时间  
»» is_call | boolean | true为Call看涨, false为Put看跌  
»» multiplier | string | 期权合约乘数，表示一张合约的面值为多少个标的物币种  
»» underlying | string | 标的物  
»» underlying_price | string | 对应交割日期的远期期货价格  
»» last_price | string | 上一次成交价格  
»» mark_price | string | 当前标记价格 (计价货币)  
»» index_price | string | 当前指数价格 (计价货币)  
»» maker_fee_rate | string | 挂单成交的手续费率，负数代表返还后续费  
»» taker_fee_rate | string | 吃单成交的手续费率  
»» order_price_round | string | 委托价格最小单位  
»» mark_price_round | string | 标记价格的最小单位  
»» order_size_min | integer(int64) | 最小下单数量  
»» order_size_max | integer(int64) | 最大下单数量  
»» order_price_deviate | string | 已废弃  
»» ref_discount_rate | string | 被推荐人享受交易费率折扣  
»» ref_rebate_rate | string | 推荐人享受交易费率返佣比例  
»» orderbook_id | integer(int64) | orderbook更新ID  
»» trade_id | integer(int64) | 已废弃  
»» trade_size | integer(int64) | 历史累计成交  
»» position_size | integer(int64) | 当前做多用户持有仓位总和  
»» orders_limit | integer | 每个用户在该盘口最多可挂的订单数量  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/contracts'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/contracts?underlying=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "name": "BTC_USDT-20211130-65000-C",
        "tag": "WEEK",
        "create_time": 1636702700,
        "expiration_time": 1637913600,
        "is_call": true,
        "strike_price": "65000",
        "last_price": "13000",
        "mark_price": "14010",
        "orderbook_id": 9,
        "trade_id": 1,
        "trade_size": 10,
        "position_size": 10,
        "underlying": "BTC_USDT",
        "underlying_price": "70000",
        "multiplier": "0.0001",
        "order_price_round": "0.1",
        "mark_price_round": "0.1",
        "maker_fee_rate": "0.0004",
        "taker_fee_rate": "0.0004",
        "price_limit_fee_rate": "0.1",
        "ref_discount_rate": "0",
        "ref_rebate_rate": "0",
        "order_price_deviate": "0.5",
        "order_size_min": 1,
        "order_size_max": 100000,
        "orders_limit": 50
      }
    ]
    

##  请求指定合约

GET`/options/contracts/{contract}`

GET `/options/contracts/{contract}`

_请求指定合约_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | URL | string | 是 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OptionsContract  
  
### 返回格式

状态码 **200**

_期权合约详情_

名称 | 类型 | 描述  
---|---|---  
» name | string | 期权合约标识  
» tag | string | 到期周期，有day、week、month  
» create_time | number(double) | 创建时间  
» expiration_time | number(double) | 到期时间  
» is_call | boolean | true为Call看涨, false为Put看跌  
» multiplier | string | 期权合约乘数，表示一张合约的面值为多少个标的物币种  
» underlying | string | 标的物  
» underlying_price | string | 对应交割日期的远期期货价格  
» last_price | string | 上一次成交价格  
» mark_price | string | 当前标记价格 (计价货币)  
» index_price | string | 当前指数价格 (计价货币)  
» maker_fee_rate | string | 挂单成交的手续费率，负数代表返还后续费  
» taker_fee_rate | string | 吃单成交的手续费率  
» order_price_round | string | 委托价格最小单位  
» mark_price_round | string | 标记价格的最小单位  
» order_size_min | integer(int64) | 最小下单数量  
» order_size_max | integer(int64) | 最大下单数量  
» order_price_deviate | string | 已废弃  
» ref_discount_rate | string | 被推荐人享受交易费率折扣  
» ref_rebate_rate | string | 推荐人享受交易费率返佣比例  
» orderbook_id | integer(int64) | orderbook更新ID  
» trade_id | integer(int64) | 已废弃  
» trade_size | integer(int64) | 历史累计成交  
» position_size | integer(int64) | 当前做多用户持有仓位总和  
» orders_limit | integer | 每个用户在该盘口最多可挂的订单数量  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/contracts/BTC_USDT-20211130-65000-C'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/contracts/BTC_USDT-20211130-65000-C \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "name": "BTC_USDT-20211130-65000-C",
      "tag": "WEEK",
      "create_time": 1636702700,
      "expiration_time": 1637913600,
      "is_call": true,
      "strike_price": "65000",
      "last_price": "13000",
      "mark_price": "14010",
      "orderbook_id": 9,
      "trade_id": 1,
      "trade_size": 10,
      "position_size": 10,
      "underlying": "BTC_USDT",
      "underlying_price": "70000",
      "multiplier": "0.0001",
      "order_price_round": "0.1",
      "mark_price_round": "0.1",
      "maker_fee_rate": "0.0004",
      "taker_fee_rate": "0.0004",
      "price_limit_fee_rate": "0.1",
      "ref_discount_rate": "0",
      "ref_rebate_rate": "0",
      "order_price_deviate": "0.5",
      "order_size_min": 1,
      "order_size_max": 100000,
      "orders_limit": 50
    }
    

##  列出结算历史

GET`/options/settlements`

GET `/options/settlements`

_列出结算历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 标的物 (可透过列出所有标的接口获得)  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsSettlement]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» time | number(double) | 配置最后更新时间  
» contract | string | 期权合约名  
» profit | string | 单张结算盈利 (计价货币)  
» fee | string | 单张结算手续费 (计价货币)  
» strike_price | string | 行权价格 (计价货币)  
» settle_price | string | 结算价格 (计价货币)  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/settlements'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/settlements?underlying=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "time": 1598839200,
        "profit": "312.35",
        "fee": "0.3284",
        "settle_price": "11687.65",
        "contract": "BTC-WEEKLY-200824-11000-P",
        "strike_price": "12000"
      }
    ]
    

##  请求指定合约结算信息

GET`/options/settlements/{contract}`

GET `/options/settlements/{contract}`

_请求指定合约结算信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | URL | string | 是 |   
underlying | 请求参数 | string | 是 | 标的物 (可透过列出所有标的接口获得)  
at | 请求参数 | integer(int64) | 是 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OptionsSettlement  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» time | number(double) | 配置最后更新时间  
» contract | string | 期权合约名  
» profit | string | 单张结算盈利 (计价货币)  
» fee | string | 单张结算手续费 (计价货币)  
» strike_price | string | 行权价格 (计价货币)  
» settle_price | string | 结算价格 (计价货币)  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/settlements/BTC_USDT-20211130-65000-C'
    query_param = 'underlying=BTC_USDT&at=0'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/settlements/BTC_USDT-20211130-65000-C?underlying=BTC_USDT&at=0 \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "time": 1598839200,
      "profit": "312.35",
      "fee": "0.3284",
      "settle_price": "11687.65",
      "contract": "BTC-WEEKLY-200824-11000-P",
      "strike_price": "12000"
    }
    

##  查询个人结算记录🔒 需要认证

GET`/options/my_settlements`

GET `/options/my_settlements`

_查询个人结算记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 标的物 (可透过列出所有标的接口获得)  
contract | 请求参数 | string | 否 | 期权合约名称  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsMySettlements]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» time | number(double) | 结算时间  
» underlying | string | 标的  
» contract | string | 期权合约标识  
» strike_price | string | 行权价格 (计价货币)  
» settle_price | string | 结算价格 (计价货币)  
» size | integer(int64) | 结算张数  
» settle_profit | string | 结算收益 (计价货币)  
» fee | string | 结算费用 (计价货币)  
» realised_pnl | string | 开仓累计盈亏，包括权益金，手续费，结算盈利等。(计价货币)  
  
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
    
    url = '/options/my_settlements'
    query_param = 'underlying=BTC_USDT'
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
    url="/options/my_settlements"
    query_param="underlying=BTC_USDT"
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
        "size": -1,
        "settle_profit": "0",
        "contract": "BTC_USDT-20220624-26000-C",
        "strike_price": "26000",
        "time": 1656057600,
        "settle_price": "20917.461281337048",
        "underlying": "BTC_USDT",
        "realised_pnl": "-0.00116042",
        "fee": "0"
      }
    ]
    

##  查询期权合约市场深度信息

GET`/options/order_book`

GET `/options/order_book`

_查询期权合约市场深度信息_

买单会按照价格从高到低排序，卖单反之

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 是 | 期权合约标识  
interval | 请求参数 | string | 否 | 合并深度指定的价格精度，0 为不合并，不指定则默认为 0  
limit | 请求参数 | integer | 否 | 深度档位数量  
with_id | 请求参数 | boolean | 否 | 是否返回深度更新 ID。深度每发生一次变化，该 ID 自增 1  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
interval | 0  
interval | 0.1  
interval | 0.01  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 深度查询成功 | OptionsOrderBook  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 深度更新 ID，深度每发生一次变化，该 ID 加 1，只有设置 `with_id=true` 时才返回  
» current | number(double) | 接口数据返回时间戳  
» update | number(double) | 深度变化时间戳  
» asks | array | 卖方深度列表  
»» options_order_book_item | object |   
»»» p | string | 价格 (计价货币)  
»»» s | integer(int64) | 数量  
»» bids | array | 买方深度列表  
»»» options_order_book_item | object |   
»»»» p | string | 价格 (计价货币)  
»»»» s | integer(int64) | 数量  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/order_book'
    query_param = 'contract=BTC_USDT-20210916-5000-C'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/order_book?contract=BTC_USDT-20210916-5000-C \
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
    

##  查询期权市场ticker信息

GET`/options/tickers`

GET `/options/tickers`

_查询期权市场ticker信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 标的物 (可透过列出所有标的接口获得)  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [OptionsTicker]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [期权合约详情]  
» _None_ | OptionsTicker | 期权合约详情  
»» name | string | 期权合约标识  
»» last_price | string | 上一次成交价格 (计价货币)  
»» mark_price | string | 当前标记价格 (计价货币)  
»» index_price | string | 当前指数价格 (计价货币)  
»» ask1_size | integer(int64) | 卖1深度大小  
»» ask1_price | string | 卖1深度价格  
»» bid1_size | integer(int64) | 买1深度大小  
»» bid1_price | string | 买1深度价格  
»» position_size | integer(int64) | 当前做多用户持有仓位总和  
»» mark_iv | string | 隐含波动率  
»» bid_iv | string | 买方隐含波动率  
»» ask_iv | string | 卖方隐含波动率  
»» leverage | string | 杠杆倍数 = underlying_price / (mark_price * delta)，该数值仅供参考  
»» delta | string | 希腊字母delta  
»» gamma | string | 希腊字母gamma  
»» vega | string | 希腊字母vega  
»» theta | string | 希腊字母theta  
»» rho | string | 希腊字母rho  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/tickers'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/tickers?underlying=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "name": "BTC_USDT-20211130-65000-C",
        "last_price": "13000",
        "mark_price": "14010",
        "position_size": 10,
        "ask1_size": 0,
        "ask1_price": "0",
        "bid1_size": 1,
        "bid1_price": "11",
        "vega": "41.41202",
        "theta": "-120.1506",
        "rho": "6.52485",
        "gamma": "0.00004",
        "delta": "0.33505",
        "mark_iv": "0.123",
        "bid_iv": "0.023",
        "ask_iv": "0.342",
        "leverage": "13"
      }
    ]
    

##  查询标的ticker信息

GET`/options/underlying/tickers/{underlying}`

GET `/options/underlying/tickers/{underlying}`

_查询标的ticker信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | URL | string | 是 | 标的物  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OptionsUnderlyingTicker  
  
### 返回格式

状态码 **200**

_期权标的详情_

名称 | 类型 | 描述  
---|---|---  
» trade_put | integer(int64) | 所有看跌合约24小时总成交量  
» trade_call | integer(int64) | 所有看涨合约24小时总成交量  
» index_price | string | 指数价格 (计价货币)  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/underlying/tickers/BTC_USDT'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/underlying/tickers/BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "trade_put": 33505,
      "trade_call": 123,
      "index_price": "76543.3"
    }
    

##  期权合约市场 K 线图

GET`/options/candlesticks`

GET `/options/candlesticks`

_期权合约市场 K 线图_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 是 | 期权合约标识  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
interval | 请求参数 | string | 否 | 数据点的时间间隔  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | [OptionsCandlestick]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [每个时间粒度的 K 线数据]  
» _None_ | OptionsCandlestick | 每个时间粒度的 K 线数据  
»» t | number(double) | 秒 s 精度的 Unix 时间戳  
»» v | integer(int64) | 交易量，只有市场行情的 K 线数据里有该值 (合约张数)  
»» c | string | 收盘价 (计价货币, 单位:标的对应的期权价格)  
»» h | string | 最高价 (计价货币, 单位:标的对应的期权价格)  
»» l | string | 最低价 (计价货币, 单位:标的对应的期权价格)  
»» o | string | 开盘价 (计价货币, 单位:标的对应的期权价格)  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/candlesticks'
    query_param = 'contract=BTC_USDT-20210916-5000-C'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/candlesticks?contract=BTC_USDT-20210916-5000-C \
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
    

##  标的指数价格 K 线图

GET`/options/underlying/candlesticks`

GET `/options/underlying/candlesticks`

_标的指数价格 K 线图_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 标的物 (可透过列出所有标的接口获得)  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
interval | 请求参数 | string | 否 | 数据点的时间间隔  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | [OptionsCandlestick]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [每个时间粒度的 K 线数据]  
» _None_ | OptionsCandlestick | 每个时间粒度的 K 线数据  
»» t | number(double) | 秒 s 精度的 Unix 时间戳  
»» v | integer(int64) | 交易量，只有市场行情的 K 线数据里有该值 (合约张数)  
»» c | string | 收盘价 (计价货币, 单位:标的对应的期权价格)  
»» h | string | 最高价 (计价货币, 单位:标的对应的期权价格)  
»» l | string | 最低价 (计价货币, 单位:标的对应的期权价格)  
»» o | string | 开盘价 (计价货币, 单位:标的对应的期权价格)  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/underlying/candlesticks'
    query_param = 'underlying=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/underlying/candlesticks?underlying=BTC_USDT \
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
    

##  市场成交记录

GET`/options/trades`

GET `/options/trades`

_市场成交记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 否 | 期权合约名称  
type | 请求参数 | string(P) | 否 | C为看涨，P为看跌  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsTrade]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | integer(int64) | 成交记录 ID  
» create_time | integer(int64) | 成交时间  
» contract | string | 期权合约标识  
» size | integer(int64) | 成交数量  
» price | string | 成交价格 (计价货币, 单位:标的对应的期权价格)  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/options/trades'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/options/trades \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": 121234231,
        "create_time": 1514764800,
        "contract": "BTC_USDT-20211130-65000-C",
        "size": 100,
        "price": "1.032"
      }
    ]
    

##  查询账户信息🔒 需要认证

GET`/options/accounts`

GET `/options/accounts`

_查询账户信息_

此接口既可查询经典期权账户，也可以查询统一账户

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OptionsAccount  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» user | integer(int64) | 用户 ID  
» total | string | 账户余额（如果是统一账户，则此字段无效）  
» position_value | string | 仓位价值，做多仓位价值为正，做空仓位价值为负  
» equity | string | 账户权益，账户余额与仓位价值的和。（如果是统一账户，则此字段无效）  
» short_enabled | boolean | 是否允许做空  
» mmp_enabled | boolean | 是否启用MMP  
» liq_triggered | boolean | 账户是否处于强平状态  
» margin_mode | integer(int32) | 此字段表示统一账户所使用的保证金模式：  
  
\- 0：经典现货保证金模式  
\- 1：跨币种保证金模式  
\- 2：组合保证金模式  
\- 3: 表示为单币种保证金模式  
» unrealised_pnl | string | 未实现盈亏，该数值仅供参考。仓位未实现盈亏 = (标记价格 - 开仓均价) * 仓位数量，其中空头仓位数量为负数，多头仓位数量为正数，均为币数单位。  
» init_margin | string | 仓位初始保证金  
» maint_margin | string | 仓位维持保证金  
» order_margin | string | 未完成订单的保证金  
» ask_order_margin | string | 未完成卖单的保证金  
» bid_order_margin | string | 未完成买单的保证金  
» available | string | 可用的转出或交易的额度  
» point | string | 点卡数额  
» currency | string | 结算币种  
» orders_limit | integer(int32) | 未完成订单数量上限  
» position_notional_limit | integer(int64) | 名义价值上限，包含仓位以及未完成订单的名义价值  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
  
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
    
    url = '/options/accounts'
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
    url="/options/accounts"
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
      "user": 666,
      "currency": "USDT",
      "short_enabled": true,
      "mmp_enabled": false,
      "liq_triggered": false,
      "margin_mode": 0,
      "total": "1650.443022",
      "position_value": "-40.1136",
      "equity": "1610.329422",
      "unrealised_pnl": "-0.7811",
      "init_margin": "0",
      "maint_margin": "135.541485",
      "order_margin": "139.74496",
      "ask_order_margin": "139.74496",
      "bid_order_margin": "0",
      "available": "1514.901537",
      "point": "0",
      "orders_limit": 10,
      "position_notional_limit": 1000000
    }
    

##  查询账户变更历史🔒 需要认证

GET`/options/account_book`

GET `/options/account_book`

_查询账户变更历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
type | 请求参数 | string | 否 | 变更类型：  
\- dnw: 转入转出  
\- prem: 交易权利金  
\- fee: 手续费  
\- refr: 推荐人返佣  
\- set: 结算盈亏  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

**type** : 变更类型：  
\- dnw: 转入转出  
\- prem: 交易权利金  
\- fee: 手续费  
\- refr: 推荐人返佣  
\- set: 结算盈亏

####  枚举值列表

枚举值列表参数 | 值  
---|---  
type | dnw  
type | prem  
type | fee  
type | refr  
type | set  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsAccountBook]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» time | number(double) | 时间  
» change | string | 变更数量 (USDT)  
» balance | string | 变更后账户总资产 (USDT)  
» type | string | 变更类型：  
  
\- dnw, 充提  
\- prem, 交易权益金  
\- fee, 交易手续费  
\- set, 结算  
\- refr, 推荐人返佣  
\- point_dnw  
\- point_fee  
\- point_refr  
» text | string | 备注  
  
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
    
    url = '/options/account_book'
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
    url="/options/account_book"
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
        "time": 1636426005,
        "change": "-0.16",
        "balance": "7378.189",
        "text": "BTC_USDT-20211216-5000-P:25",
        "type": "fee"
      }
    ]
    

##  列出指定标的下的用户仓位🔒 需要认证

GET`/options/positions`

GET `/options/positions`

_列出指定标的下的用户仓位_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 否 | 标的物  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsPosition]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [期权合约仓位详情]  
» _None_ | OptionsPosition | 期权合约仓位详情  
»» user | integer | 用户ID  
»» underlying | string | 标的物  
»» underlying_price | string | 对应交割日期的远期期货价格  
»» contract | string | 期权合约标识  
»» size | integer(int64) | 头寸大小 (合约张数)  
»» entry_price | string | 开仓价格 (计价货币)  
»» mark_price | string | 期权合约当前标记价格 (计价货币)  
»» mark_iv | string | 隐含波动率  
»» realised_pnl | string | 已实现盈亏  
»» unrealised_pnl | string | 未实现盈亏，该数值仅供参考。仓位未实现盈亏 = (标记价格 - 开仓均价) * 仓位数量，其中空头仓位数量为负数，多头仓位数量为正数，均为币数单位。  
»» pending_orders | integer | 当前未完成委托数量  
»» close_order | object|null | 当前平仓委托信息，如果没有平仓则为`null`  
»»» id | integer(int64) | 委托ID  
»»» price | string | 委托价格 (计价货币)  
»»» is_liq | boolean | 是否为强制平仓  
»» delta | string | 希腊字母delta  
»» gamma | string | 希腊字母gamma  
»» vega | string | 希腊字母vega  
»» theta | string | 希腊字母theta  
  
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
    
    url = '/options/positions'
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
    url="/options/positions"
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
        "user": 11027586,
        "underlying": "BTC_USDT",
        "underlying_price": "70000",
        "contract": "BTC_USDT-20211216-5000-P",
        "size": 10,
        "entry_price": "1234",
        "realised_pnl": "120",
        "mark_price": "6000",
        "mark_iv": "0.9638",
        "unrealised_pnl": "-320",
        "pending_orders": 1,
        "close_order": {
          "id": 232323,
          "price": "5779",
          "is_liq": false
        },
        "delta": "-0.0046",
        "gamma": "0",
        "vega": "2.87656",
        "theta": "-1.00247"
      }
    ]
    

##  请求指定仓位🔒 需要认证

GET`/options/positions/{contract}`

GET `/options/positions/{contract}`

_请求指定仓位_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | URL | string | 是 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | OptionsPosition  
  
### 返回格式

状态码 **200**

_期权合约仓位详情_

名称 | 类型 | 描述  
---|---|---  
» user | integer | 用户ID  
» underlying | string | 标的物  
» underlying_price | string | 对应交割日期的远期期货价格  
» contract | string | 期权合约标识  
» size | integer(int64) | 头寸大小 (合约张数)  
» entry_price | string | 开仓价格 (计价货币)  
» mark_price | string | 期权合约当前标记价格 (计价货币)  
» mark_iv | string | 隐含波动率  
» realised_pnl | string | 已实现盈亏  
» unrealised_pnl | string | 未实现盈亏，该数值仅供参考。仓位未实现盈亏 = (标记价格 - 开仓均价) * 仓位数量，其中空头仓位数量为负数，多头仓位数量为正数，均为币数单位。  
» pending_orders | integer | 当前未完成委托数量  
» close_order | object|null | 当前平仓委托信息，如果没有平仓则为`null`  
»» id | integer(int64) | 委托ID  
»» price | string | 委托价格 (计价货币)  
»» is_liq | boolean | 是否为强制平仓  
» delta | string | 希腊字母delta  
» gamma | string | 希腊字母gamma  
» vega | string | 希腊字母vega  
» theta | string | 希腊字母theta  
  
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
    
    url = '/options/positions/BTC_USDT-20211130-65000-C'
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
    url="/options/positions/BTC_USDT-20211130-65000-C"
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
      "user": 11027586,
      "underlying": "BTC_USDT",
      "underlying_price": "70000",
      "contract": "BTC_USDT-20211216-5000-P",
      "size": 10,
      "entry_price": "1234",
      "realised_pnl": "120",
      "mark_price": "6000",
      "mark_iv": "0.9638",
      "unrealised_pnl": "-320",
      "pending_orders": 1,
      "close_order": {
        "id": 232323,
        "price": "5779",
        "is_liq": false
      },
      "delta": "-0.0046",
      "gamma": "0",
      "vega": "2.87656",
      "theta": "-1.00247"
    }
    

##  列出指定标的下的用户平仓历史🔒 需要认证

GET`/options/position_close`

GET `/options/position_close`

_列出指定标的下的用户平仓历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 标的物 (可透过列出所有标的接口获得)  
contract | 请求参数 | string | 否 | 期权合约名称  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsPositionClose]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» time | number(double) | 平仓时间  
» contract | string | 期权合约标识  
» side | string | 多空方向  
  
\- `long`: 做多  
\- `short`: 做空  
» pnl | string | 盈亏  
» text | string | 平仓委托的来源，具体取值参见`order.text`字段  
» settle_size | string | 结算仓位大小  
  
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
    
    url = '/options/position_close'
    query_param = 'underlying=BTC_USDT'
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
    url="/options/position_close"
    query_param="underlying=BTC_USDT"
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
        "time": 1631764800,
        "pnl": "-42914.291",
        "settle_size": "-10001",
        "side": "short",
        "contract": "BTC_USDT-20210916-5000-C",
        "text": "settled"
      }
    ]
    

##  查询期权合约订单列表🔒 需要认证

GET`/options/orders`

GET `/options/orders`

_查询期权合约订单列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 否 | 期权合约名称  
underlying | 请求参数 | string | 否 | 标的物  
status | 请求参数 | string | 是 | 基于状态查询订单列表  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
status | open  
status | finished  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [期权订单详情]  
» _None_ | OptionsOrder | 期权订单详情  
»» id | integer(int64) | 期权订单 ID  
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
\- mmp_cancelled: MMP撤销  
»» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
»» contract | string | 期权标识  
»» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
»» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
»» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。(计价货币)  
»» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
»» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
»» is_liq | boolean | 是否为强制平仓委托  
»» is_mmp | boolean | 是否为MMP委托。对应请求中的`mmp`。  
»» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
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
\- liquidation: 强制平仓  
\- insurance: 保险  
»» tkfr | string | 吃单费率  
»» mkfr | string | 做单费率  
»» refu | integer | 推荐人用户 ID  
»» refr | string | 推荐人返佣  
  
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
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders'
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
    url="/options/orders"
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
        "status": "finished",
        "size": -1,
        "id": 2,
        "iceberg": 0,
        "is_liq": false,
        "is_close": false,
        "is_mmp": false,
        "contract": "BTC_USDT-20210916-5000-C",
        "text": "-",
        "fill_price": "100",
        "finish_as": "filled",
        "left": 0,
        "tif": "gtc",
        "is_reduce_only": false,
        "create_time": 1631763361,
        "finish_time": 1631763397,
        "price": "100"
      }
    ]
    

##  交易下单🔒 需要认证

POST`/options/orders`

POST `/options/orders`

_交易下单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OptionsOrder | 是 |   
» contract | body | string | 是 | 期权标识  
» size | body | integer(int64) | 是 | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
» iceberg | body | integer(int64) | 否 | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
» price | body | string | 否 | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。(计价货币)  
» close | body | boolean | 否 | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
» reduce_only | body | boolean | 否 | 设置为 true 的时候，为只减仓委托  
» mmp | body | boolean | 否 | 设置为 true 的时候，为MMP委托  
» tif | body | string | 否 | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
» text | body | string | 否 | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: 强制平仓  
\- insurance: 保险  
  
####  详细描述

**» tif** : Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单

**» text** : 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
1\. 必须以 `t-` 开头  
2\. 不计算 `t-` ，长度不能超过 28 字节  
3\. 输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)  
  
除用户自定义信息以外，以下为内部保留字段，标识订单来源:  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
\- auto_deleveraging: 自动减仓  
\- liquidation: 强制平仓  
\- insurance: 保险

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» tif | gtc  
» tif | ioc  
» tif | poc  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 订单信息 | OptionsOrder  
  
### 返回格式

状态码 **201**

_期权订单详情_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 期权订单 ID  
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
\- mmp_cancelled: MMP撤销  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
» contract | string | 期权标识  
» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。(计价货币)  
» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
» is_liq | boolean | 是否为强制平仓委托  
» is_mmp | boolean | 是否为MMP委托。对应请求中的`mmp`。  
» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
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
\- liquidation: 强制平仓  
\- insurance: 保险  
» tkfr | string | 吃单费率  
» mkfr | string | 做单费率  
» refu | integer | 推荐人用户 ID  
» refr | string | 推荐人返佣  
  
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
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders'
    query_param = ''
    body='{"size":-1,"iceberg":0,"contract":"BTC_USDT-20210916-5000-C","text":"-","tif":"gtc","price":"100"}'
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
    url="/options/orders"
    query_param=""
    body_param='{"size":-1,"iceberg":0,"contract":"BTC_USDT-20210916-5000-C","text":"-","tif":"gtc","price":"100"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "size": -1,
      "iceberg": 0,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "tif": "gtc",
      "price": "100"
    }
    

> 返回示例

> 201 返回
    
    
    {
      "status": "finished",
      "size": -1,
      "id": 2,
      "iceberg": 0,
      "is_liq": false,
      "is_close": false,
      "is_mmp": false,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "fill_price": "100",
      "finish_as": "filled",
      "left": 0,
      "tif": "gtc",
      "is_reduce_only": false,
      "create_time": 1631763361,
      "finish_time": 1631763397,
      "price": "100"
    }
    

##  批量取消状态为 open 的订单🔒 需要认证

DELETE`/options/orders`

DELETE `/options/orders`

_批量取消状态为 open 的订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 否 | 期权合约名称  
underlying | 请求参数 | string | 否 | 标的物  
side | 请求参数 | string | 否 | 指定全部买单或全部卖单，不指定则两者都包括  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
side | ask  
side | bid  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 批量撤销成功 | [OptionsOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [期权订单详情]  
» _None_ | OptionsOrder | 期权订单详情  
»» id | integer(int64) | 期权订单 ID  
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
\- mmp_cancelled: MMP撤销  
»» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
»» contract | string | 期权标识  
»» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
»» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
»» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。(计价货币)  
»» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
»» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
»» is_liq | boolean | 是否为强制平仓委托  
»» is_mmp | boolean | 是否为MMP委托。对应请求中的`mmp`。  
»» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
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
\- liquidation: 强制平仓  
\- insurance: 保险  
»» tkfr | string | 吃单费率  
»» mkfr | string | 做单费率  
»» refu | integer | 推荐人用户 ID  
»» refr | string | 推荐人返佣  
  
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
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders'
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
    url="/options/orders"
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
        "status": "finished",
        "size": -1,
        "id": 2,
        "iceberg": 0,
        "is_liq": false,
        "is_close": false,
        "is_mmp": false,
        "contract": "BTC_USDT-20210916-5000-C",
        "text": "-",
        "fill_price": "100",
        "finish_as": "filled",
        "left": 0,
        "tif": "gtc",
        "is_reduce_only": false,
        "create_time": 1631763361,
        "finish_time": 1631763397,
        "price": "100"
      }
    ]
    

##  查询单个订单详情🔒 需要认证

GET`/options/orders/{order_id}`

GET `/options/orders/{order_id}`

_查询单个订单详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | integer(int64) | 是 | 成功创建订单时返回的订单 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单信息 | OptionsOrder  
  
### 返回格式

状态码 **200**

_期权订单详情_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 期权订单 ID  
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
\- mmp_cancelled: MMP撤销  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
» contract | string | 期权标识  
» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。(计价货币)  
» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
» is_liq | boolean | 是否为强制平仓委托  
» is_mmp | boolean | 是否为MMP委托。对应请求中的`mmp`。  
» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
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
\- liquidation: 强制平仓  
\- insurance: 保险  
» tkfr | string | 吃单费率  
» mkfr | string | 做单费率  
» refu | integer | 推荐人用户 ID  
» refr | string | 推荐人返佣  
  
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
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders/12345'
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
    url="/options/orders/12345"
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
      "status": "finished",
      "size": -1,
      "id": 2,
      "iceberg": 0,
      "is_liq": false,
      "is_close": false,
      "is_mmp": false,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "fill_price": "100",
      "finish_as": "filled",
      "left": 0,
      "tif": "gtc",
      "is_reduce_only": false,
      "create_time": 1631763361,
      "finish_time": 1631763397,
      "price": "100"
    }
    

##  期权改单🔒 需要认证

PUT`/options/orders/{order_id}`

PUT `/options/orders/{order_id}`

_期权改单_

修改指定订单的委托价格和/或数量，仅支持状态为 open 的订单

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AmendOptionsOrderRequest | 是 |   
» contract | body | string | 是 | 期权合约名称  
» price | body | string | 是 | 委托价  
» size | body | integer(int64) | 是 | 交易数量  
order_id | URL | integer(int64) | 是 | 成功创建订单时返回的订单 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单信息 | OptionsOrder  
  
### 返回格式

状态码 **200**

_期权订单详情_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 期权订单 ID  
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
\- mmp_cancelled: MMP撤销  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
» contract | string | 期权标识  
» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。(计价货币)  
» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
» is_liq | boolean | 是否为强制平仓委托  
» is_mmp | boolean | 是否为MMP委托。对应请求中的`mmp`。  
» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
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
\- liquidation: 强制平仓  
\- insurance: 保险  
» tkfr | string | 吃单费率  
» mkfr | string | 做单费率  
» refu | integer | 推荐人用户 ID  
» refr | string | 推荐人返佣  
  
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
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders/12345'
    query_param = ''
    body='{"contract":"BTC_USDT-20260320-75000-C","price":"1661","size":10}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('PUT', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('PUT', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="PUT"
    url="/options/orders/12345"
    query_param=""
    body_param='{"contract":"BTC_USDT-20260320-75000-C","price":"1661","size":10}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "contract": "BTC_USDT-20260320-75000-C",
      "price": "1661",
      "size": 10
    }
    

> 返回示例

> 200 返回
    
    
    {
      "status": "finished",
      "size": -1,
      "id": 2,
      "iceberg": 0,
      "is_liq": false,
      "is_close": false,
      "is_mmp": false,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "fill_price": "100",
      "finish_as": "filled",
      "left": 0,
      "tif": "gtc",
      "is_reduce_only": false,
      "create_time": 1631763361,
      "finish_time": 1631763397,
      "price": "100"
    }
    

##  撤销单个订单🔒 需要认证

DELETE`/options/orders/{order_id}`

DELETE `/options/orders/{order_id}`

_撤销单个订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | integer(int64) | 是 | 成功创建订单时返回的订单 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单信息 | OptionsOrder  
  
### 返回格式

状态码 **200**

_期权订单详情_

名称 | 类型 | 描述  
---|---|---  
» id | integer(int64) | 期权订单 ID  
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
\- mmp_cancelled: MMP撤销  
» status | string | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
» contract | string | 期权标识  
» size | integer(int64) | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
» iceberg | integer(int64) | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
» price | string | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。(计价货币)  
» is_close | boolean | 是否为平仓委托。对应请求中的`close`。  
» is_reduce_only | boolean | 是否为只减仓委托。对应请求中的`reduce_only`。  
» is_liq | boolean | 是否为强制平仓委托  
» is_mmp | boolean | 是否为MMP委托。对应请求中的`mmp`。  
» tif | string | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
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
\- liquidation: 强制平仓  
\- insurance: 保险  
» tkfr | string | 吃单费率  
» mkfr | string | 做单费率  
» refu | integer | 推荐人用户 ID  
» refr | string | 推荐人返佣  
  
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
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
  
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
    
    url = '/options/orders/12345'
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
    url="/options/orders/12345"
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
      "status": "finished",
      "size": -1,
      "id": 2,
      "iceberg": 0,
      "is_liq": false,
      "is_close": false,
      "is_mmp": false,
      "contract": "BTC_USDT-20210916-5000-C",
      "text": "-",
      "fill_price": "100",
      "finish_as": "filled",
      "left": 0,
      "tif": "gtc",
      "is_reduce_only": false,
      "create_time": 1631763361,
      "finish_time": 1631763397,
      "price": "100"
    }
    

##  倒计时取消订单🔒 需要认证

POST`/options/countdown_cancel_all`

POST `/options/countdown_cancel_all`

_倒计时取消订单_

期权订单心跳检测，在到达用户设置的`timeout`时间时如果没有取消既有倒计时或设置新的倒计时将会自动取消相关的`期权挂单`。 该接口可重复调用，以便设置新的倒计时或取消倒计时。 用法示例： 以30s的间隔重复此接口，每次倒计时`timeout`设置为30(秒)。 如果在30秒内未再次调用此接口，则您指定的`underlying` `contract`上的所有挂单都会被自动撤销，若未指定`underlying` `contract`则会自动撤销用户的全部挂单 如果在30秒内以将`timeout`设置为0，则倒数计时器将终止，自动撤单功能取消。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CountdownCancelAllOptionsTask | 是 |   
» timeout | body | integer(int32) | 是 | 倒计时时间，单位 秒  
至少5秒，为0时表示取消倒计时  
» contract | body | string | 否 | 期权合约名称  
» underlying | body | string | 否 | 标的物  
  
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
    
    url = '/options/countdown_cancel_all'
    query_param = ''
    body='{"timeout":30,"contract":"BTC_USDT-20241001-46000-C","underlying":"BTC_USDT"}'
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
    url="/options/countdown_cancel_all"
    query_param=""
    body_param='{"timeout":30,"contract":"BTC_USDT-20241001-46000-C","underlying":"BTC_USDT"}'
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
      "contract": "BTC_USDT-20241001-46000-C",
      "underlying": "BTC_USDT"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "triggerTime": "1660039145000"
    }
    

##  查询个人成交记录🔒 需要认证

GET`/options/my_trades`

GET `/options/my_trades`

_查询个人成交记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 标的物 (可透过列出所有标的接口获得)  
contract | 请求参数 | string | 否 | 期权合约名称  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [OptionsMyTrade]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» id | integer(int64) | 成交记录 ID  
» create_time | number(double) | 成交时间  
» contract | string | 期权合约标识  
» order_id | integer | 成交记录关联订单 ID  
» size | integer(int64) | 成交数量  
» price | string | 成交价格 (计价货币)  
» underlying_price | string | 对应交割日期的远期期货价格  
» role | string | 成交角色， taker - 吃单, maker - 做单  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
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
    
    url = '/options/my_trades'
    query_param = 'underlying=BTC_USDT'
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
    url="/options/my_trades"
    query_param="underlying=BTC_USDT"
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
        "underlying_price": "48000",
        "size": 1,
        "contract": "BTC_USDT-20210916-5000-C",
        "id": 1,
        "role": "taker",
        "create_time": 1631763397,
        "order_id": 4,
        "price": "100"
      }
    ]
    

##  MMP查询🔒 需要认证

GET`/options/mmp`

GET `/options/mmp`

_MMP查询_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 否 | 标的物  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [OptionsMMP]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [MMP设置]  
» _None_ | OptionsMMP | MMP设置  
»» underlying | string | 标的物  
»» window | integer(int32) | 时间窗口（毫秒），1-5000之间，0表示停用MMP  
»» frozen_period | integer(int32) | 冻结时长（毫秒），0表示一直冻结，需要调用重置API解冻  
»» qty_limit | string | 成交量上限（正数，至多2位小数）  
»» delta_limit | string | 净delta值上限（正数，至多2位小数）  
»» trigger_time_ms | integer(int64) | 触发冻结时间（毫秒），0表示没有触发冻结  
»» frozen_until_ms | integer(int64) | 解冻时间（毫秒），如果未配置冻结时长，触发冻结后无解冻时间  
  
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
    
    url = '/options/mmp'
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
    url="/options/mmp"
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
        "underlying": "BTC_USDT",
        "window": 5000,
        "frozen_period": 200,
        "qty_limit": "10",
        "delta_limit": "10",
        "trigger_time_ms": 0,
        "frozen_until_ms": 0
      }
    ]
    

##  MMP设置🔒 需要认证

POST`/options/mmp`

POST `/options/mmp`

_MMP设置_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OptionsMMP | 是 |   
» underlying | body | string | 是 | 标的物  
» window | body | integer(int32) | 是 | 时间窗口（毫秒），1-5000之间，0表示停用MMP  
» frozen_period | body | integer(int32) | 是 | 冻结时长（毫秒），0表示一直冻结，需要调用重置API解冻  
» qty_limit | body | string | 是 | 成交量上限（正数，至多2位小数）  
» delta_limit | body | string | 是 | 净delta值上限（正数，至多2位小数）  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | MMP信息 | OptionsMMP  
  
### 返回格式

状态码 **200**

_MMP设置_

名称 | 类型 | 描述  
---|---|---  
» underlying | string | 标的物  
» window | integer(int32) | 时间窗口（毫秒），1-5000之间，0表示停用MMP  
» frozen_period | integer(int32) | 冻结时长（毫秒），0表示一直冻结，需要调用重置API解冻  
» qty_limit | string | 成交量上限（正数，至多2位小数）  
» delta_limit | string | 净delta值上限（正数，至多2位小数）  
» trigger_time_ms | integer(int64) | 触发冻结时间（毫秒），0表示没有触发冻结  
» frozen_until_ms | integer(int64) | 解冻时间（毫秒），如果未配置冻结时长，触发冻结后无解冻时间  
  
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
    
    url = '/options/mmp'
    query_param = ''
    body='{"underlying":"BTC_USDT","window":5000,"frozen_period":200,"qty_limit":"10","delta_limit":"10"}'
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
    url="/options/mmp"
    query_param=""
    body_param='{"underlying":"BTC_USDT","window":5000,"frozen_period":200,"qty_limit":"10","delta_limit":"10"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "underlying": "BTC_USDT",
      "window": 5000,
      "frozen_period": 200,
      "qty_limit": "10",
      "delta_limit": "10"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "underlying": "BTC_USDT",
      "window": 5000,
      "frozen_period": 200,
      "qty_limit": "10",
      "delta_limit": "10",
      "trigger_time_ms": 0,
      "frozen_until_ms": 0
    }
    

##  MMP重置🔒 需要认证

POST`/options/mmp/reset`

POST `/options/mmp/reset`

_MMP重置_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | OptionsMMPReset | 是 |   
» underlying | body | string | 是 | 标的物  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | MMP信息 | OptionsMMP  
  
### 返回格式

状态码 **200**

_MMP设置_

名称 | 类型 | 描述  
---|---|---  
» underlying | string | 标的物  
» window | integer(int32) | 时间窗口（毫秒），1-5000之间，0表示停用MMP  
» frozen_period | integer(int32) | 冻结时长（毫秒），0表示一直冻结，需要调用重置API解冻  
» qty_limit | string | 成交量上限（正数，至多2位小数）  
» delta_limit | string | 净delta值上限（正数，至多2位小数）  
» trigger_time_ms | integer(int64) | 触发冻结时间（毫秒），0表示没有触发冻结  
» frozen_until_ms | integer(int64) | 解冻时间（毫秒），如果未配置冻结时长，触发冻结后无解冻时间  
  
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
    
    url = '/options/mmp/reset'
    query_param = ''
    body='{"underlying":"BTC_USDT"}'
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
    url="/options/mmp/reset"
    query_param=""
    body_param='{"underlying":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "underlying": "BTC_USDT"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "underlying": "BTC_USDT",
      "window": 5000,
      "frozen_period": 200,
      "qty_limit": "10",
      "delta_limit": "10",
      "trigger_time_ms": 0,
      "frozen_until_ms": 0
    }
    

#  模型

##  OptionsContract

_期权合约详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
name | string | false | none | 期权合约标识  
tag | string | false | none | 到期周期，有day、week、month  
create_time | number(double) | false | none | 创建时间  
expiration_time | number(double) | false | none | 到期时间  
is_call | boolean | false | none | true为Call看涨, false为Put看跌  
multiplier | string | false | none | 期权合约乘数，表示一张合约的面值为多少个标的物币种  
underlying | string | false | none | 标的物  
underlying_price | string | false | none | 对应交割日期的远期期货价格  
last_price | string | false | none | 上一次成交价格  
mark_price | string | false | none | 当前标记价格 (计价货币)  
index_price | string | false | none | 当前指数价格 (计价货币)  
maker_fee_rate | string | false | none | 挂单成交的手续费率，负数代表返还后续费  
taker_fee_rate | string | false | none | 吃单成交的手续费率  
order_price_round | string | false | none | 委托价格最小单位  
mark_price_round | string | false | none | 标记价格的最小单位  
order_size_min | integer(int64) | false | none | 最小下单数量  
order_size_max | integer(int64) | false | none | 最大下单数量  
order_price_deviate | string | false | none | 已废弃  
ref_discount_rate | string | false | none | 被推荐人享受交易费率折扣  
ref_rebate_rate | string | false | none | 推荐人享受交易费率返佣比例  
orderbook_id | integer(int64) | false | none | orderbook更新ID  
trade_id | integer(int64) | false | none | 已废弃  
trade_size | integer(int64) | false | none | 历史累计成交  
position_size | integer(int64) | false | none | 当前做多用户持有仓位总和  
orders_limit | integer | false | none | 每个用户在该盘口最多可挂的订单数量  
      
    
    {
      "name": "string",
      "tag": "string",
      "create_time": 0,
      "expiration_time": 0,
      "is_call": true,
      "multiplier": "string",
      "underlying": "string",
      "underlying_price": "string",
      "last_price": "string",
      "mark_price": "string",
      "index_price": "string",
      "maker_fee_rate": "string",
      "taker_fee_rate": "string",
      "order_price_round": "string",
      "mark_price_round": "string",
      "order_size_min": 0,
      "order_size_max": 0,
      "order_price_deviate": "string",
      "ref_discount_rate": "string",
      "ref_rebate_rate": "string",
      "orderbook_id": 0,
      "trade_id": 0,
      "trade_size": 0,
      "position_size": 0,
      "orders_limit": 0
    }
    
    

##  OptionsOrder

_期权订单详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | 只读 | 期权订单 ID  
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
\- mmp_cancelled: MMP撤销  
status | string | false | 只读 | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
contract | string | true | none | 期权标识  
size | integer(int64) | true | none | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
iceberg | integer(int64) | false | none | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | false | none | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。(计价货币)  
close | boolean | false | 只写 | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | false | 只读 | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | false | 只写 | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | false | 只读 | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | false | 只读 | 是否为强制平仓委托  
mmp | boolean | false | 只写 | 设置为 true 的时候，为MMP委托  
is_mmp | boolean | false | 只读 | 是否为MMP委托。对应请求中的`mmp`。  
tif | string | false | none | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
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
\- liquidation: 强制平仓  
\- insurance: 保险  
tkfr | string | false | 只读 | 吃单费率  
mkfr | string | false | 只读 | 做单费率  
refu | integer | false | 只读 | 推荐人用户 ID  
refr | string | false | 只读 | 推荐人返佣  
  
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
finish_as | mmp_cancelled  
status | open  
status | finished  
tif | gtc  
tif | ioc  
tif | poc  
      
    
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
      "mmp": false,
      "is_mmp": true,
      "tif": "gtc",
      "left": 0,
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "refr": "string"
    }
    
    

##  OptionsMMP

_MMP设置_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
underlying | string | true | none | 标的物  
window | integer(int32) | true | none | 时间窗口（毫秒），1-5000之间，0表示停用MMP  
frozen_period | integer(int32) | true | none | 冻结时长（毫秒），0表示一直冻结，需要调用重置API解冻  
qty_limit | string | true | none | 成交量上限（正数，至多2位小数）  
delta_limit | string | true | none | 净delta值上限（正数，至多2位小数）  
trigger_time_ms | integer(int64) | false | 只读 | 触发冻结时间（毫秒），0表示没有触发冻结  
frozen_until_ms | integer(int64) | false | 只读 | 解冻时间（毫秒），如果未配置冻结时长，触发冻结后无解冻时间  
      
    
    {
      "underlying": "string",
      "window": 0,
      "frozen_period": 0,
      "qty_limit": "string",
      "delta_limit": "string",
      "trigger_time_ms": 0,
      "frozen_until_ms": 0
    }
    
    

##  OptionsTicker

_期权合约详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
name | string | false | none | 期权合约标识  
last_price | string | false | none | 上一次成交价格 (计价货币)  
mark_price | string | false | none | 当前标记价格 (计价货币)  
index_price | string | false | none | 当前指数价格 (计价货币)  
ask1_size | integer(int64) | false | none | 卖1深度大小  
ask1_price | string | false | none | 卖1深度价格  
bid1_size | integer(int64) | false | none | 买1深度大小  
bid1_price | string | false | none | 买1深度价格  
position_size | integer(int64) | false | none | 当前做多用户持有仓位总和  
mark_iv | string | false | none | 隐含波动率  
bid_iv | string | false | none | 买方隐含波动率  
ask_iv | string | false | none | 卖方隐含波动率  
leverage | string | false | none | 杠杆倍数 = underlying_price / (mark_price * delta)，该数值仅供参考  
delta | string | false | none | 希腊字母delta  
gamma | string | false | none | 希腊字母gamma  
vega | string | false | none | 希腊字母vega  
theta | string | false | none | 希腊字母theta  
rho | string | false | none | 希腊字母rho  
      
    
    {
      "name": "string",
      "last_price": "string",
      "mark_price": "string",
      "index_price": "string",
      "ask1_size": 0,
      "ask1_price": "string",
      "bid1_size": 0,
      "bid1_price": "string",
      "position_size": 0,
      "mark_iv": "string",
      "bid_iv": "string",
      "ask_iv": "string",
      "leverage": "string",
      "delta": "string",
      "gamma": "string",
      "vega": "string",
      "theta": "string",
      "rho": "string"
    }
    
    

##  CountdownCancelAllOptionsTask

_CountdownCancelAllOptionsTask_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timeout | integer(int32) | true | none | 倒计时时间，单位 秒  
至少5秒，为0时表示取消倒计时  
contract | string | false | none | 期权合约名称  
underlying | string | false | none | 标的物  
      
    
    {
      "timeout": 0,
      "contract": "string",
      "underlying": "string"
    }
    
    

##  OptionsPosition

_期权合约仓位详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user | integer | false | 只读 | 用户ID  
underlying | string | false | 只读 | 标的物  
underlying_price | string | false | 只读 | 对应交割日期的远期期货价格  
contract | string | false | 只读 | 期权合约标识  
size | integer(int64) | false | 只读 | 头寸大小 (合约张数)  
entry_price | string | false | 只读 | 开仓价格 (计价货币)  
mark_price | string | false | 只读 | 期权合约当前标记价格 (计价货币)  
mark_iv | string | false | 只读 | 隐含波动率  
realised_pnl | string | false | 只读 | 已实现盈亏  
unrealised_pnl | string | false | 只读 | 未实现盈亏，该数值仅供参考。仓位未实现盈亏 = (标记价格 - 开仓均价) * 仓位数量，其中空头仓位数量为负数，多头仓位数量为正数，均为币数单位。  
pending_orders | integer | false | 只读 | 当前未完成委托数量  
close_order | object|null | false | 只读 | 当前平仓委托信息，如果没有平仓则为`null`  
» id | integer(int64) | false | none | 委托ID  
» price | string | false | none | 委托价格 (计价货币)  
» is_liq | boolean | false | none | 是否为强制平仓  
delta | string | false | 只读 | 希腊字母delta  
gamma | string | false | 只读 | 希腊字母gamma  
vega | string | false | 只读 | 希腊字母vega  
theta | string | false | 只读 | 希腊字母theta  
      
    
    {
      "user": 0,
      "underlying": "string",
      "underlying_price": "string",
      "contract": "string",
      "size": 0,
      "entry_price": "string",
      "mark_price": "string",
      "mark_iv": "string",
      "realised_pnl": "string",
      "unrealised_pnl": "string",
      "pending_orders": 0,
      "close_order": {
        "id": 0,
        "price": "string",
        "is_liq": true
      },
      "delta": "string",
      "gamma": "string",
      "vega": "string",
      "theta": "string"
    }
    
    

##  AmendOptionsOrderRequest

_AmendOptionsOrderRequest_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
contract | string | true | none | 期权合约名称  
price | string | true | none | 委托价  
size | integer(int64) | true | none | 交易数量  
      
    
    {
      "contract": "string",
      "price": "string",
      "size": 0
    }
    
    

##  OptionsSettlement

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
time | number(double) | false | none | 配置最后更新时间  
contract | string | false | none | 期权合约名  
profit | string | false | none | 单张结算盈利 (计价货币)  
fee | string | false | none | 单张结算手续费 (计价货币)  
strike_price | string | false | none | 行权价格 (计价货币)  
settle_price | string | false | none | 结算价格 (计价货币)  
      
    
    {
      "time": 0,
      "contract": "string",
      "profit": "string",
      "fee": "string",
      "strike_price": "string",
      "settle_price": "string"
    }
    
    

##  OptionsMySettlements

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
time | number(double) | false | none | 结算时间  
underlying | string | false | none | 标的  
contract | string | false | none | 期权合约标识  
strike_price | string | false | none | 行权价格 (计价货币)  
settle_price | string | false | none | 结算价格 (计价货币)  
size | integer(int64) | false | none | 结算张数  
settle_profit | string | false | none | 结算收益 (计价货币)  
fee | string | false | none | 结算费用 (计价货币)  
realised_pnl | string | false | none | 开仓累计盈亏，包括权益金，手续费，结算盈利等。(计价货币)  
      
    
    {
      "time": 0,
      "underlying": "string",
      "contract": "string",
      "strike_price": "string",
      "settle_price": "string",
      "size": 0,
      "settle_profit": "string",
      "fee": "string",
      "realised_pnl": "string"
    }
    
    

##  OptionsUnderlying

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
name | string | false | none | 标的名  
index_price | string | false | none | 现货指数价格 (计价货币)  
      
    
    {
      "name": "string",
      "index_price": "string"
    }
    
    

##  OptionsCandlestick

_每个时间粒度的 K 线数据_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
t | number(double) | false | none | 秒 s 精度的 Unix 时间戳  
v | integer(int64) | false | none | 交易量，只有市场行情的 K 线数据里有该值 (合约张数)  
c | string | false | none | 收盘价 (计价货币, 单位:标的对应的期权价格)  
h | string | false | none | 最高价 (计价货币, 单位:标的对应的期权价格)  
l | string | false | none | 最低价 (计价货币, 单位:标的对应的期权价格)  
o | string | false | none | 开盘价 (计价货币, 单位:标的对应的期权价格)  
      
    
    {
      "t": 0,
      "v": 0,
      "c": "string",
      "h": "string",
      "l": "string",
      "o": "string"
    }
    
    

##  OptionsAccountBook

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
time | number(double) | false | none | 时间  
change | string | false | none | 变更数量 (USDT)  
balance | string | false | none | 变更后账户总资产 (USDT)  
type | string | false | none | 变更类型：  
  
\- dnw, 充提  
\- prem, 交易权益金  
\- fee, 交易手续费  
\- set, 结算  
\- refr, 推荐人返佣  
\- point_dnw  
\- point_fee  
\- point_refr  
text | string | false | none | 备注  
      
    
    {
      "time": 0,
      "change": "string",
      "balance": "string",
      "type": "string",
      "text": "string"
    }
    
    

##  OptionsOrderBook

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 深度更新 ID，深度每发生一次变化，该 ID 加 1，只有设置 `with_id=true` 时才返回  
current | number(double) | false | none | 接口数据返回时间戳  
update | number(double) | false | none | 深度变化时间戳  
asks | array | true | none | 卖方深度列表  
» options_order_book_item | object | false | none | none  
»» p | string | false | none | 价格 (计价货币)  
»» s | integer(int64) | false | none | 数量  
» bids | array | true | none | 买方深度列表  
»» options_order_book_item | object | false | none | none  
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
    
    

##  OptionsTrade

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 成交记录 ID  
create_time | integer(int64) | false | none | 成交时间  
contract | string | false | none | 期权合约标识  
size | integer(int64) | false | none | 成交数量  
price | string | false | none | 成交价格 (计价货币, 单位:标的对应的期权价格)  
      
    
    {
      "id": 0,
      "create_time": 0,
      "contract": "string",
      "size": 0,
      "price": "string"
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
    
    

##  OptionsUnderlyingTicker

_期权标的详情_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
trade_put | integer(int64) | false | none | 所有看跌合约24小时总成交量  
trade_call | integer(int64) | false | none | 所有看涨合约24小时总成交量  
index_price | string | false | none | 指数价格 (计价货币)  
      
    
    {
      "trade_put": 0,
      "trade_call": 0,
      "index_price": "string"
    }
    
    

##  OptionsMyTrade

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer(int64) | false | none | 成交记录 ID  
create_time | number(double) | false | none | 成交时间  
contract | string | false | none | 期权合约标识  
order_id | integer | false | none | 成交记录关联订单 ID  
size | integer(int64) | false | none | 成交数量  
price | string | false | none | 成交价格 (计价货币)  
underlying_price | string | false | none | 对应交割日期的远期期货价格  
role | string | false | none | 成交角色， taker - 吃单, maker - 做单  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
role | taker  
role | maker  
      
    
    {
      "id": 0,
      "create_time": 0,
      "contract": "string",
      "order_id": 0,
      "size": 0,
      "price": "string",
      "underlying_price": "string",
      "role": "taker"
    }
    
    

##  OptionsMMPReset

_MMP重置_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
underlying | string | true | none | 标的物  
window | integer(int32) | false | 只读 | 时间窗口（毫秒），1-5000之间，0表示停用MMP  
frozen_period | integer(int32) | false | 只读 | 冻结时长（毫秒），0表示一直冻结，需要调用重置API解冻  
qty_limit | string | false | 只读 | 成交量上限（正数，至多2位小数）  
delta_limit | string | false | 只读 | 净delta值上限（正数，至多2位小数）  
trigger_time_ms | integer(int64) | false | 只读 | 触发冻结时间（毫秒），0表示没有触发冻结  
frozen_until_ms | integer(int64) | false | 只读 | 解冻时间（毫秒），如果未配置冻结时长，触发冻结后无解冻时间  
      
    
    {
      "underlying": "string",
      "window": 0,
      "frozen_period": 0,
      "qty_limit": "string",
      "delta_limit": "string",
      "trigger_time_ms": 0,
      "frozen_until_ms": 0
    }
    
    

##  OptionsAccount

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user | integer(int64) | false | none | 用户 ID  
total | string | false | none | 账户余额（如果是统一账户，则此字段无效）  
position_value | string | false | none | 仓位价值，做多仓位价值为正，做空仓位价值为负  
equity | string | false | none | 账户权益，账户余额与仓位价值的和。（如果是统一账户，则此字段无效）  
short_enabled | boolean | false | none | 是否允许做空  
mmp_enabled | boolean | false | none | 是否启用MMP  
liq_triggered | boolean | false | none | 账户是否处于强平状态  
margin_mode | integer(int32) | false | none | 此字段表示统一账户所使用的保证金模式：  
  
\- 0：经典现货保证金模式  
\- 1：跨币种保证金模式  
\- 2：组合保证金模式  
\- 3: 表示为单币种保证金模式  
unrealised_pnl | string | false | none | 未实现盈亏，该数值仅供参考。仓位未实现盈亏 = (标记价格 - 开仓均价) * 仓位数量，其中空头仓位数量为负数，多头仓位数量为正数，均为币数单位。  
init_margin | string | false | none | 仓位初始保证金  
maint_margin | string | false | none | 仓位维持保证金  
order_margin | string | false | none | 未完成订单的保证金  
ask_order_margin | string | false | none | 未完成卖单的保证金  
bid_order_margin | string | false | none | 未完成买单的保证金  
available | string | false | none | 可用的转出或交易的额度  
point | string | false | none | 点卡数额  
currency | string | false | none | 结算币种  
orders_limit | integer(int32) | false | none | 未完成订单数量上限  
position_notional_limit | integer(int64) | false | none | 名义价值上限，包含仓位以及未完成订单的名义价值  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
      
    
    {
      "user": 0,
      "total": "string",
      "position_value": "string",
      "equity": "string",
      "short_enabled": true,
      "mmp_enabled": true,
      "liq_triggered": true,
      "margin_mode": 0,
      "unrealised_pnl": "string",
      "init_margin": "string",
      "maint_margin": "string",
      "order_margin": "string",
      "ask_order_margin": "string",
      "bid_order_margin": "string",
      "available": "string",
      "point": "string",
      "currency": "string",
      "orders_limit": 0,
      "position_notional_limit": 0
    }
    
    

##  OptionsPositionClose

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
time | number(double) | false | 只读 | 平仓时间  
contract | string | false | 只读 | 期权合约标识  
side | string | false | 只读 | 多空方向  
  
\- `long`: 做多  
\- `short`: 做空  
pnl | string | false | 只读 | 盈亏  
text | string | false | 只读 | 平仓委托的来源，具体取值参见`order.text`字段  
settle_size | string | false | 只读 | 结算仓位大小  
  
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
      "text": "string",
      "settle_size": "string"
    }