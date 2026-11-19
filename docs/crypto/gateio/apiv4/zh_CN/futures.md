---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/futures
api_type: Trading
updated_at: 2026-11-19 19:01:35.275556
---

# Futures

永续合约

##  查询所有的合约信息

GET`/futures/{settle}/contracts`

GET `/futures/{settle}/contracts`

_查询所有的合约信息_

查询小数张数合约的实际下单上下限时，请携带 `X-Gate-Size-Decimal: 1`。用返回的 `enable_decimal` 判断每个合约是否支持小数张数。

以 `ETH_USDT` 为例，带请求头 `X-Gate-Size-Decimal: 1` 时，其 `order_size_min` 为字符串 `"0.1"`。省略该请求头或设为 `0` 时，返回的整数 `0` 是截去小数部分后的值，实际最小下单张数仍为 `0.1`。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
X-Gate-Size-Decimal | 请求头部 | string | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [Contract]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约详情

类型 | 约束  
---|---  
Contract |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
name | string | Optional |  | 合约标识  
type | string | Optional | enum: ["inverse","direct"] | 合约类型, inverse - 反向合约, direct - 正向合约  
quanto_multiplier | string | Optional |  | 合约乘数，表示一张合约的面值为多少个标的物币种  
leverage_min | string | Optional |  | 最小杠杆  
leverage_max | string | Optional |  | 最大杠杆  
maintenance_rate | string | Optional |  | 风险限额的第一档维持保证金率要求  
mark_type | string | Optional | enum: ["internal","index"] | 已废弃  
mark_price | string | Optional |  | 当前标记价格  
index_price | string | Optional |  | 当前指数价格  
last_price | string | Optional |  | 上一次成交价格  
maker_fee_rate | string | Optional |  | 挂单成交的手续费率，负数代表返还后续费  
taker_fee_rate | string | Optional |  | 吃单成交的手续费率  
order_price_round | string | Optional |  | 委托价格最小单位  
mark_price_round | string | Optional |  | 标记价格的最小单位  
funding_rate | string | Optional |  | 当前资金费率  
funding_interval | integer | Optional |  | 资金费率应用间隔，以秒为单位  
funding_next_apply | number(double) | Optional |  | 下次资金费率应用时间  
risk_limit_base | string | Optional |  | 基础风险限额,已废弃  
interest_rate | string | Optional |  | 永续合约资金费率及溢价相关计算中使用的利率参数。以字符串表示的小数比率（如 `0.0003`），与 `funding_rate` 等同为比率而非百分数。  
risk_limit_step | string | Optional |  | 风险限额调整步长,已废弃  
risk_limit_max | string | Optional |  | 合约允许的最大风险限额,已废弃,建议使用/futures/{settle}/risk_limit_tiers来查询风险限额  
order_size_min | string | Optional |  | 最小下单张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数，实际最小张数小于 1 时会显示为 0。  
enable_decimal | boolean | Optional |  | 是否支持小数张数。为 `true` 时，可携带 `X-Gate-Size-Decimal: 1` 提交小数张数。为 `false` 时，合约仅支持整张数量。  
order_size_max | string | Optional |  | 最大下单张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
order_price_deviate | string | Optional |  | 下单价与当前标记价格允许的正负偏移量， 即下单价 `order_price` 需满足如下条件:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | Optional |  | 被推荐人享受交易费率折扣  
ref_rebate_rate | string | Optional |  | 推荐人享受交易费率返佣比例  
orderbook_id | integer(int64) | Optional |  | orderbook更新ID  
trade_id | integer(int64) | Optional |  | 当前成交ID  
trade_size | string | Optional |  | 历史累计成交  
position_size | string | Optional |  | 当前做多用户持有仓位总和  
config_change_time | number(double) | Optional |  | 配置最后更新时间  
in_delisting | boolean | Optional |  | `in_delisting=true` 并且position_size>0时候 表示该合约处于下线过渡期  
`in_delisting=true`` 并且position_size=0时候 表示该合约处于下线状态  
orders_limit | integer | Optional |  | 最多挂单数量  
enable_bonus | boolean | Optional |  | 是否支持体验金  
enable_credit | boolean | Optional |  | 该合约是否支持统一账户。  
create_time | number(double) | Optional |  | 表示合约的创建时间  
funding_cap_ratio | string | Optional |  | 已废弃  
status | string | Optional |  | 合约状态 类型包含：prelaunch（预上线）, trading（交易中）,delisting（下架中）, delisted（已下架）, circuit_breaker（熔断)  
launch_time | integer(int64) | Optional |  | 合约开盘时间。  
delisting_time | integer(int64) | Optional |  | 合约进入只减仓状态时间  
delisted_time | integer(int64) | Optional |  | 合约下架时间  
market_order_slip_ratio | string | Optional |  | 合约市价下单支持的最大滑点比率，比率计算以市场最新价格为基准  
market_order_size_max | string | Optional |  | 合约市价下单支持的最大张数，默认值为0，为默认值时取`order_size_max`字段作为最大张数限制  
funding_rate_limit | string | Optional |  | 资金费率上限值  
contract_type | string | Optional |  | 合约分类类型，如 stocks-股票, metals-金属, indices-指数, forex-外汇, commodities-大宗商品等  
funding_impact_value | string | Optional |  | 资金费用深度影响额  
enable_circuit_breaker | boolean | Optional |  | 新开盘的合约是否启动标记价格熔断（如果平台要对某个新开盘的合约市场启动该机制以避免开盘后价格发生大幅波动导致过多爆仓，会提前发公告告知）  
  
该请求不需要认证 

示例代码
    
    
    import requests
    
    url = "https://api.gateio.ws/api/v4/futures/usdt/contracts"
    response = requests.get(url, headers={"X-Gate-Size-Decimal": "1"}, timeout=10)
    response.raise_for_status()
    print(response.json())
    
    
    
    curl 'https://api.gateio.ws/api/v4/futures/usdt/contracts' -H 'X-Gate-Size-Decimal: 1'
    

> 返回示例

> 200 返回
    
    
    [
      {
        "name": "BTC_USDT",
        "type": "direct",
        "quanto_multiplier": "0.0001",
        "ref_discount_rate": "0",
        "order_price_deviate": "0.5",
        "maintenance_rate": "0.005",
        "mark_type": "index",
        "last_price": "38026",
        "mark_price": "37985.6",
        "index_price": "37954.92",
        "funding_rate_indicative": "0.000219",
        "mark_price_round": "0.01",
        "funding_offset": 0,
        "in_delisting": false,
        "risk_limit_base": "1000000",
        "interest_rate": "0.0003",
        "order_price_round": "0.1",
        "order_size_min": "1",
        "enable_decimal": false,
        "ref_rebate_rate": "0.2",
        "funding_interval": 28800,
        "risk_limit_step": "1000000",
        "leverage_min": "1",
        "leverage_max": "100",
        "risk_limit_max": "8000000",
        "maker_fee_rate": "-0.00025",
        "taker_fee_rate": "0.00075",
        "funding_rate": "0.002053",
        "order_size_max": "1000000",
        "funding_next_apply": 1610035200,
        "short_users": 977,
        "config_change_time": 1609899548,
        "trade_size": "28530850594",
        "position_size": "5223816",
        "long_users": 455,
        "funding_impact_value": "60000",
        "orders_limit": 50,
        "trade_id": 10851092,
        "orderbook_id": 2129638396,
        "enable_bonus": true,
        "enable_credit": true,
        "create_time": 1669688556,
        "funding_cap_ratio": "0.75",
        "status": "trading",
        "launch_time": 1609899548,
        "delisting_time": 1609899548,
        "delisted_time": 1609899548,
        "market_order_slip_ratio": "0.05",
        "market_order_size_max": "0",
        "funding_rate_limit": "0.003",
        "contract_type": "indices",
        "enable_circuit_breaker": false
      }
    ]
    

##  查询所有的合约信息（包含已下架）

GET`/futures/{settle}/contracts_all`

GET `/futures/{settle}/contracts_all`

_查询所有的合约信息（包含已下架）_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [Contract]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约详情

类型 | 约束  
---|---  
Contract |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
name | string | Optional |  | 合约标识  
type | string | Optional | enum: ["inverse","direct"] | 合约类型, inverse - 反向合约, direct - 正向合约  
quanto_multiplier | string | Optional |  | 合约乘数，表示一张合约的面值为多少个标的物币种  
leverage_min | string | Optional |  | 最小杠杆  
leverage_max | string | Optional |  | 最大杠杆  
maintenance_rate | string | Optional |  | 风险限额的第一档维持保证金率要求  
mark_type | string | Optional | enum: ["internal","index"] | 已废弃  
mark_price | string | Optional |  | 当前标记价格  
index_price | string | Optional |  | 当前指数价格  
last_price | string | Optional |  | 上一次成交价格  
maker_fee_rate | string | Optional |  | 挂单成交的手续费率，负数代表返还后续费  
taker_fee_rate | string | Optional |  | 吃单成交的手续费率  
order_price_round | string | Optional |  | 委托价格最小单位  
mark_price_round | string | Optional |  | 标记价格的最小单位  
funding_rate | string | Optional |  | 当前资金费率  
funding_interval | integer | Optional |  | 资金费率应用间隔，以秒为单位  
funding_next_apply | number(double) | Optional |  | 下次资金费率应用时间  
risk_limit_base | string | Optional |  | 基础风险限额,已废弃  
interest_rate | string | Optional |  | 永续合约资金费率及溢价相关计算中使用的利率参数。以字符串表示的小数比率（如 `0.0003`），与 `funding_rate` 等同为比率而非百分数。  
risk_limit_step | string | Optional |  | 风险限额调整步长,已废弃  
risk_limit_max | string | Optional |  | 合约允许的最大风险限额,已废弃,建议使用/futures/{settle}/risk_limit_tiers来查询风险限额  
order_size_min | string | Optional |  | 最小下单张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数，实际最小张数小于 1 时会显示为 0。  
enable_decimal | boolean | Optional |  | 是否支持小数张数。为 `true` 时，可携带 `X-Gate-Size-Decimal: 1` 提交小数张数。为 `false` 时，合约仅支持整张数量。  
order_size_max | string | Optional |  | 最大下单张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
order_price_deviate | string | Optional |  | 下单价与当前标记价格允许的正负偏移量， 即下单价 `order_price` 需满足如下条件:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | Optional |  | 被推荐人享受交易费率折扣  
ref_rebate_rate | string | Optional |  | 推荐人享受交易费率返佣比例  
orderbook_id | integer(int64) | Optional |  | orderbook更新ID  
trade_id | integer(int64) | Optional |  | 当前成交ID  
trade_size | string | Optional |  | 历史累计成交  
position_size | string | Optional |  | 当前做多用户持有仓位总和  
config_change_time | number(double) | Optional |  | 配置最后更新时间  
in_delisting | boolean | Optional |  | `in_delisting=true` 并且position_size>0时候 表示该合约处于下线过渡期  
`in_delisting=true`` 并且position_size=0时候 表示该合约处于下线状态  
orders_limit | integer | Optional |  | 最多挂单数量  
enable_bonus | boolean | Optional |  | 是否支持体验金  
enable_credit | boolean | Optional |  | 该合约是否支持统一账户。  
create_time | number(double) | Optional |  | 表示合约的创建时间  
funding_cap_ratio | string | Optional |  | 已废弃  
status | string | Optional |  | 合约状态 类型包含：prelaunch（预上线）, trading（交易中）,delisting（下架中）, delisted（已下架）, circuit_breaker（熔断)  
launch_time | integer(int64) | Optional |  | 合约开盘时间。  
delisting_time | integer(int64) | Optional |  | 合约进入只减仓状态时间  
delisted_time | integer(int64) | Optional |  | 合约下架时间  
market_order_slip_ratio | string | Optional |  | 合约市价下单支持的最大滑点比率，比率计算以市场最新价格为基准  
market_order_size_max | string | Optional |  | 合约市价下单支持的最大张数，默认值为0，为默认值时取`order_size_max`字段作为最大张数限制  
funding_rate_limit | string | Optional |  | 资金费率上限值  
contract_type | string | Optional |  | 合约分类类型，如 stocks-股票, metals-金属, indices-指数, forex-外汇, commodities-大宗商品等  
funding_impact_value | string | Optional |  | 资金费用深度影响额  
enable_circuit_breaker | boolean | Optional |  | 新开盘的合约是否启动标记价格熔断（如果平台要对某个新开盘的合约市场启动该机制以避免开盘后价格发生大幅波动导致过多爆仓，会提前发公告告知）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/contracts_all'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/contracts_all \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "name": "BTC_USDT",
        "type": "direct",
        "quanto_multiplier": "0.0001",
        "ref_discount_rate": "0",
        "order_price_deviate": "0.5",
        "maintenance_rate": "0.005",
        "mark_type": "index",
        "last_price": "38026",
        "mark_price": "37985.6",
        "index_price": "37954.92",
        "funding_rate_indicative": "0.000219",
        "mark_price_round": "0.01",
        "funding_offset": 0,
        "in_delisting": false,
        "risk_limit_base": "1000000",
        "interest_rate": "0.0003",
        "order_price_round": "0.1",
        "order_size_min": "1",
        "enable_decimal": false,
        "ref_rebate_rate": "0.2",
        "funding_interval": 28800,
        "risk_limit_step": "1000000",
        "leverage_min": "1",
        "leverage_max": "100",
        "risk_limit_max": "8000000",
        "maker_fee_rate": "-0.00025",
        "taker_fee_rate": "0.00075",
        "funding_rate": "0.002053",
        "order_size_max": "1000000",
        "funding_next_apply": 1610035200,
        "short_users": 977,
        "config_change_time": 1609899548,
        "trade_size": "28530850594",
        "position_size": "5223816",
        "long_users": 455,
        "funding_impact_value": "60000",
        "orders_limit": 50,
        "trade_id": 10851092,
        "orderbook_id": 2129638396,
        "enable_bonus": true,
        "enable_credit": true,
        "create_time": 1669688556,
        "funding_cap_ratio": "0.75",
        "status": "trading",
        "launch_time": 1609899548,
        "delisting_time": 1609899548,
        "delisted_time": 1609899548,
        "market_order_slip_ratio": "0.05",
        "market_order_size_max": "0",
        "funding_rate_limit": "0.003",
        "contract_type": "indices",
        "enable_circuit_breaker": false
      }
    ]
    

##  查询单个合约信息

GET`/futures/{settle}/contracts/{contract}`

GET `/futures/{settle}/contracts/{contract}`

_查询单个合约信息_

带 `X-Gate-Size-Decimal: 1` 查询实际下单上下限。`ETH_USDT` 的 `order_size_min` 返回字符串 `"0.1"`。省略请求头或设为 `0` 时，该字段返回整数 `0`，实际最小下单张数仍为 `0.1`。

是否支持小数张数以目标合约的 `enable_decimal` 为准。参见 [API 张数字段兼容规则 ](https://www.gate.com/zh/announcements/article/48788)和[市场张数精度调整公告 ](https://www.gate.com/zh/announcements/article/50325)。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
X-Gate-Size-Decimal | 请求头部 | string | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 合约信息 | Contract  
  
### 返回格式

状态码 **200**

合约详情

类型 | 约束  
---|---  
Contract |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
name | string | Optional |  | 合约标识  
type | string | Optional | enum: ["inverse","direct"] | 合约类型, inverse - 反向合约, direct - 正向合约  
quanto_multiplier | string | Optional |  | 合约乘数，表示一张合约的面值为多少个标的物币种  
leverage_min | string | Optional |  | 最小杠杆  
leverage_max | string | Optional |  | 最大杠杆  
maintenance_rate | string | Optional |  | 风险限额的第一档维持保证金率要求  
mark_type | string | Optional | enum: ["internal","index"] | 已废弃  
mark_price | string | Optional |  | 当前标记价格  
index_price | string | Optional |  | 当前指数价格  
last_price | string | Optional |  | 上一次成交价格  
maker_fee_rate | string | Optional |  | 挂单成交的手续费率，负数代表返还后续费  
taker_fee_rate | string | Optional |  | 吃单成交的手续费率  
order_price_round | string | Optional |  | 委托价格最小单位  
mark_price_round | string | Optional |  | 标记价格的最小单位  
funding_rate | string | Optional |  | 当前资金费率  
funding_interval | integer | Optional |  | 资金费率应用间隔，以秒为单位  
funding_next_apply | number(double) | Optional |  | 下次资金费率应用时间  
risk_limit_base | string | Optional |  | 基础风险限额,已废弃  
interest_rate | string | Optional |  | 永续合约资金费率及溢价相关计算中使用的利率参数。以字符串表示的小数比率（如 `0.0003`），与 `funding_rate` 等同为比率而非百分数。  
risk_limit_step | string | Optional |  | 风险限额调整步长,已废弃  
risk_limit_max | string | Optional |  | 合约允许的最大风险限额,已废弃,建议使用/futures/{settle}/risk_limit_tiers来查询风险限额  
order_size_min | string | Optional |  | 最小下单张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数，实际最小张数小于 1 时会显示为 0。  
enable_decimal | boolean | Optional |  | 是否支持小数张数。为 `true` 时，可携带 `X-Gate-Size-Decimal: 1` 提交小数张数。为 `false` 时，合约仅支持整张数量。  
order_size_max | string | Optional |  | 最大下单张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
order_price_deviate | string | Optional |  | 下单价与当前标记价格允许的正负偏移量， 即下单价 `order_price` 需满足如下条件:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | Optional |  | 被推荐人享受交易费率折扣  
ref_rebate_rate | string | Optional |  | 推荐人享受交易费率返佣比例  
orderbook_id | integer(int64) | Optional |  | orderbook更新ID  
trade_id | integer(int64) | Optional |  | 当前成交ID  
trade_size | string | Optional |  | 历史累计成交  
position_size | string | Optional |  | 当前做多用户持有仓位总和  
config_change_time | number(double) | Optional |  | 配置最后更新时间  
in_delisting | boolean | Optional |  | `in_delisting=true` 并且position_size>0时候 表示该合约处于下线过渡期  
`in_delisting=true`` 并且position_size=0时候 表示该合约处于下线状态  
orders_limit | integer | Optional |  | 最多挂单数量  
enable_bonus | boolean | Optional |  | 是否支持体验金  
enable_credit | boolean | Optional |  | 该合约是否支持统一账户。  
create_time | number(double) | Optional |  | 表示合约的创建时间  
funding_cap_ratio | string | Optional |  | 已废弃  
status | string | Optional |  | 合约状态 类型包含：prelaunch（预上线）, trading（交易中）,delisting（下架中）, delisted（已下架）, circuit_breaker（熔断)  
launch_time | integer(int64) | Optional |  | 合约开盘时间。  
delisting_time | integer(int64) | Optional |  | 合约进入只减仓状态时间  
delisted_time | integer(int64) | Optional |  | 合约下架时间  
market_order_slip_ratio | string | Optional |  | 合约市价下单支持的最大滑点比率，比率计算以市场最新价格为基准  
market_order_size_max | string | Optional |  | 合约市价下单支持的最大张数，默认值为0，为默认值时取`order_size_max`字段作为最大张数限制  
funding_rate_limit | string | Optional |  | 资金费率上限值  
contract_type | string | Optional |  | 合约分类类型，如 stocks-股票, metals-金属, indices-指数, forex-外汇, commodities-大宗商品等  
funding_impact_value | string | Optional |  | 资金费用深度影响额  
enable_circuit_breaker | boolean | Optional |  | 新开盘的合约是否启动标记价格熔断（如果平台要对某个新开盘的合约市场启动该机制以避免开盘后价格发生大幅波动导致过多爆仓，会提前发公告告知）  
  
该请求不需要认证 

示例代码
    
    
    import requests
    
    url = "https://api.gateio.ws/api/v4/futures/usdt/contracts/ETH_USDT"
    response = requests.get(url, headers={"X-Gate-Size-Decimal": "1"}, timeout=10)
    response.raise_for_status()
    print(response.json())
    
    
    
    curl 'https://api.gateio.ws/api/v4/futures/usdt/contracts/ETH_USDT' -H 'X-Gate-Size-Decimal: 1'
    

> 返回示例

> 200 返回
    
    
    {
      "name": "ETH_USDT",
      "enable_decimal": true,
      "order_size_min": "0.1",
      "order_size_max": "10000000"
    }
    

##  查询市场级 ADL 风险状态

GET`/futures/{settle}/adl_risk_states`

GET `/futures/{settle}/adl_risk_states`

_查询市场级 ADL 风险状态_

查询指定结算币种下所有合约市场当前的 ADL 风险状态

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | FuturesADLRiskStates  
  
### 返回格式

状态码 **200**

FuturesADLRiskStates

类型 | 约束  
---|---  
FuturesADLRiskStates | required: ["settle","states"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
settle | string | Required |  | 结算货币  
states | object | Required |  | 合约市场与 ADL 风险状态的映射  
  
**states**

合约市场与 ADL 风险状态的映射

类型 | 约束  
---|---  
object |   
  
**states / additionalProperties**

FuturesADLRiskState

类型 | 约束  
---|---  
FuturesADLRiskState | required: ["state","calculated_at_ms"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
state | string | Required | enum: ["normal","warning","adl_risk"] | 市场 ADL 风险状态  
calculated_at_ms | integer(int64) | Required |  | 状态计算时间，Unix 毫秒时间戳  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/adl_risk_states'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/adl_risk_states \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "settle": "usdt",
      "states": {
        "BTC_USDT": {
          "state": "normal",
          "calculated_at_ms": 1786695185345
        },
        "GT_USDT": {
          "state": "warning",
          "calculated_at_ms": 1786695185345
        },
        "HYPE_USDT": {
          "state": "adl_risk",
          "calculated_at_ms": 1786695185345
        }
      }
    }
    

##  查询合约市场深度信息

GET`/futures/{settle}/order_book`

GET `/futures/{settle}/order_book`

_查询合约市场深度信息_

买单会按照价格从高到低排序，卖单反之

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 是 | 合约标识  
interval | 请求参数 | string | 否 | 合并深度指定的价格精度，0 为不合并，不指定则默认为 0  
limit | 请求参数 | integer | 否 | 深度档位数量  
with_id | 请求参数 | boolean | 否 | 是否返回深度更新 ID。深度每发生一次变化，该 ID 自增 1  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 深度查询成功 | FuturesOrderBook  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
FuturesOrderBook | required: ["asks","bids"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 深度更新 ID，深度每发生一次变化，该 ID 加 1，只有设置 `with_id=true` 时才返回  
current | number(double) | Optional |  | 接口数据返回时间戳  
update | number(double) | Optional |  | 深度变化时间戳  
asks | array | Required |  | 卖方深度列表  
bids | array | Required |  | 买方深度列表  
  
**asks**

卖方深度列表

类型 | 约束  
---|---  
array |   
  
**asks / items**

FuturesOrderBookItem

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
p | string | Optional |  | 价格 (计价货币)  
s | string | Optional |  | 数量  
  
**bids**

买方深度列表

类型 | 约束  
---|---  
array |   
  
**bids / items**

FuturesOrderBookItem

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
p | string | Optional |  | 价格 (计价货币)  
s | string | Optional |  | 数量  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/order_book'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/order_book?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "id": 123456,
      "current": 1623898993.123456,
      "update": 1623898993.121456,
      "asks": [
        {
          "p": "1.52",
          "s": "100"
        },
        {
          "p": "1.53",
          "s": "40"
        }
      ],
      "bids": [
        {
          "p": "1.17",
          "s": "150"
        },
        {
          "p": "1.16",
          "s": "203"
        }
      ]
    }
    

##  查询合约市场RPI深度信息

GET`/futures/{settle}/rpi_order_book`

GET `/futures/{settle}/rpi_order_book`

_查询合约市场RPI深度信息_

买单会按照价格从高到低排序，卖单反之

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 是 | 合约标识  
interval | 请求参数 | string | 否 | 合并深度指定的价格精度，0 为不合并，不指定则默认为 0  
limit | 请求参数 | integer | 否 | 深度档位数量  
with_id | 请求参数 | boolean | 否 | 是否返回深度更新 ID。深度每发生一次变化，该 ID 自增 1  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 深度查询成功 | FuturesOrderBook  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
FuturesOrderBook | required: ["asks","bids"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 深度更新 ID，深度每发生一次变化，该 ID 加 1，只有设置 `with_id=true` 时才返回  
current | number(double) | Optional |  | 接口数据返回时间戳  
update | number(double) | Optional |  | 深度变化时间戳  
asks | array | Required |  | 卖方深度列表  
bids | array | Required |  | 买方深度列表  
  
**asks**

卖方深度列表

类型 | 约束  
---|---  
array |   
  
**asks / items**

FuturesOrderBookItem

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
p | string | Optional |  | 价格 (计价货币)  
s | string | Optional |  | 数量  
  
**bids**

买方深度列表

类型 | 约束  
---|---  
array |   
  
**bids / items**

FuturesOrderBookItem

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
p | string | Optional |  | 价格 (计价货币)  
s | string | Optional |  | 数量  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/rpi_order_book'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/rpi_order_book?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "id": 123456,
      "current": 1623898993.123456,
      "update": 1623898993.121456,
      "asks": [
        {
          "p": "1.52",
          "s": "100"
        },
        {
          "p": "1.53",
          "s": "40"
        }
      ],
      "bids": [
        {
          "p": "1.17",
          "s": "150"
        },
        {
          "p": "1.16",
          "s": "203"
        }
      ]
    }
    

##  合约市场成交记录

GET`/futures/{settle}/trades`

GET `/futures/{settle}/trades`

_合约市场成交记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 是 | 合约标识  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
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
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FuturesTrade]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
FuturesTrade |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 成交记录 ID  
create_time | number(double) | Optional |  | 成交时间  
create_time_ms | number(double) | Optional |  | 成交时间，保留 3 位小数的毫秒精度  
contract | string | Optional |  | 合约标识  
size | string | Optional |  | 成交数量  
price | string | Optional |  | 成交价格 (计价货币)  
is_internal | boolean | Optional |  | 已废弃  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/trades'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/trades?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "id": 121234231,
        "create_time": 1514764800,
        "contract": "BTC_USDT",
        "size": "-100",
        "price": "100.123"
      }
    ]
    

##  合约市场 K 线图

GET`/futures/{settle}/candlesticks`

GET `/futures/{settle}/candlesticks`

_合约市场 K 线图_

如果 `contract` 字段在合约标识前增加了 `mark_` 前缀则返回标记价格数据(如mark_BTC_USD)， 如果增加了 `index_` 则返回指数价格的数据(如index_BTC_USD)

K 线图数据单次请求最大返回 2000 个点，指定 from, to 和 interval 的时候注意点数不能过多。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 是 | 合约标识  
from | 请求参数 | integer(int64) | 否 | 指定 K 线图的起始时间，注意时间格式为秒(s)精度的 Unix 时间戳，不指定则默认为 to - 100 * interval，即向前最多 100 个点的时间  
to | 请求参数 | integer(int64) | 否 | 指定 K 线图的结束时间，不指定则默认当前时间，注意时间格式为秒(s)精度的 Unix 时间戳  
limit | 请求参数 | integer | 否 | 指定数据点的数量，适用于取最近 `limit` 数量的数据，该字段与 `from`, `to` 互斥，如果指定了 `from`, `to` 中的任意字段，该字段会被拒绝  
interval | 请求参数 | string | 否 | 数据点的时间间隔，注意 1w 代表一个自然周，7d 的时间是和 Unix 初始时间对齐, 30d 代表一个自然月  
timezone | 请求参数 | string | 否 | 时区,all/utc0/utc8，默认utc0  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
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
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | [FuturesCandlestick]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

每个时间粒度的 K 线数据

类型 | 约束  
---|---  
FuturesCandlestick |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | number(double) | Optional |  | 秒 s 精度的 Unix 时间戳  
v | string | Optional |  | 交易量，只有市场行情的 K 线数据里有该值 (合约张数)  
c | string | Optional |  | 收盘价 (计价货币)  
h | string | Optional |  | 最高价 (计价货币)  
l | string | Optional |  | 最低价 (计价货币)  
o | string | Optional |  | 开盘价 (计价货币)  
sum | string | Optional |  | 交易额，单位是计价货币  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/candlesticks'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/candlesticks?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "t": 1539852480,
        "v": "97151",
        "c": "1.032",
        "h": "1.032",
        "l": "1.032",
        "o": "1.032",
        "sum": "3580"
      }
    ]
    

##  合约溢价指数 K 线图

GET`/futures/{settle}/premium_index`

GET `/futures/{settle}/premium_index`

_合约溢价指数 K 线图_

K 线图数据单次请求最大返回 1000 个点，指定 from, to 和 interval 的时候注意点数不能过多

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 是 | 合约标识  
from | 请求参数 | integer(int64) | 否 | 指定 K 线图的起始时间，注意时间格式为秒(s)精度的 Unix 时间戳，不指定则默认为 to - 100 * interval，即向前最多 100 个点的时间  
to | 请求参数 | integer(int64) | 否 | 指定 K 线图的结束时间，不指定则默认当前时间，注意时间格式为秒(s)精度的 Unix 时间戳  
limit | 请求参数 | integer | 否 | 指定数据点的数量，适用于取最近 `limit` 数量的数据，该字段与 `from`, `to` 互斥，如果指定了 `from`, `to` 中的任意字段，该字段会被拒绝  
interval | 请求参数 | string | 否 | 数据点的时间间隔  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
interval | 1m  
interval | 5m  
interval | 15m  
interval | 30m  
interval | 1h  
interval | 4h  
interval | 8h  
interval | 1d  
interval | 7d  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功查询 | [FuturesPremiumIndex]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

每个时间粒度的 K 线数据

类型 | 约束  
---|---  
FuturesPremiumIndex |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | number(double) | Optional |  | 秒 s 精度的 Unix 时间戳  
c | string | Optional |  | 收盘价  
h | string | Optional |  | 最高价  
l | string | Optional |  | 最低价  
o | string | Optional |  | 开盘价  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/premium_index'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/premium_index?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "t": 1539852480,
        "c": "0",
        "h": "0.00023",
        "l": "0",
        "o": "0"
      }
    ]
    

##  获取所有合约交易行情统计

GET`/futures/{settle}/tickers`

GET `/futures/{settle}/tickers`

_获取所有合约交易行情统计_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [FuturesTicker]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
FuturesTicker |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional |  | 合约标识  
last | string | Optional |  | 最新成交价  
change_percentage | string | Optional |  | 涨跌百分比，跌用负数标识，如 -7.45  
total_size | string | Optional |  | 当前合约总持仓量  
low_24h | string | Optional |  | 最近24小时最低价  
high_24h | string | Optional |  | 最近24小时最高价  
volume_24h | string | Optional |  | 最近24小时成交总量  
volume_24h_btc | string | Optional |  | 最近24小时成交总量，BTC单位(即将废弃，建议使用 `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle`)  
volume_24h_usd | string | Optional |  | 最近24小时成交总量，USD单位(即将废弃，建议使用 `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle`)  
volume_24h_base | string | Optional |  | 最近24小时成交量，以基础货币为单位  
volume_24h_quote | string | Optional |  | 最近24小时成交量，以计价货币为单位  
volume_24h_settle | string | Optional |  | 最近24小时成交量，以结算货币为单位  
mark_price | string | Optional |  | 最近标记价格  
funding_rate | string | Optional |  | 资金费率  
funding_rate_indicative | string | Optional |  | 下一周期预测资金费率（已弃用，改用funding_rate）  
index_price | string | Optional |  | 指数价格  
quanto_base_rate | string | Optional |  | 已废弃  
lowest_ask | string | Optional |  | 最新卖方最低价  
lowest_size | string | Optional |  | 最新卖方最低价的挂单量  
highest_bid | string | Optional |  | 最新买方最高价  
highest_size | string | Optional |  | 最新买方最高价的挂单量  
change_utc0 | string | Optional |  | utc0 涨跌百分比，跌用负数标识，如 -7.45  
change_utc8 | string | Optional |  | utc8 涨跌百分比，跌用负数标识，如 -7.45  
change_price | string | Optional |  | 24h 涨跌额，跌用负数标识，如 -7.45  
change_utc0_price | string | Optional |  | utc0 涨跌额，跌用负数标识，如 -7.45  
change_utc8_price | string | Optional |  | utc8 涨跌额，跌用负数标识，如 -7.45  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/tickers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/tickers \
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
    

##  合约市场历史资金费率

GET`/futures/{settle}/funding_rate`

GET `/futures/{settle}/funding_rate`

_合约市场历史资金费率_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 是 | 合约标识  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
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
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 历史查询成功 | [FundingRateRecord]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
FundingRateRecord |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | integer(int64) | Optional |  | 秒 s 精度的 Unix 时间戳  
r | string | Optional |  | 资金费率  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/funding_rate'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/funding_rate?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "t": 1543968000,
        "r": "0.000157"
      }
    ]
    

##  批量查询永续合约的资金费率历史数据

POST`/futures/{settle}/funding_rates`

POST `/futures/{settle}/funding_rates`

_批量查询永续合约的资金费率历史数据_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
body | body | BatchFundingRatesRequest | 是 |   
contracts | body | array | 是 | 合约名称数组  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

请求体结构类型 | 约束  
---|---  
BatchFundingRatesRequest | required: ["contracts"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contracts | array | Required | minItems: 1  
maxItems: 200 | 合约名称数组  
  
**contracts**

合约名称数组

请求体结构类型 | 约束  
---|---  
array | minItems: 1  
maxItems: 200  
  
**contracts / items**

请求体结构类型 | 约束  
---|---  
string |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 批量查询成功 | [BatchFundingRatesResponse]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
BatchFundingRatesResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional |  | 合约名称  
data | array | Optional |  | 资金费率数组  
  
**items / data**

资金费率数组

类型 | 约束  
---|---  
array |   
  
**items / data / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | integer(int64) | Optional |  | 秒 s 精度的 Unix 时间戳  
r | string | Optional |  | 资金费率  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/funding_rates'
    query_param = ''
    body='{"contracts":["BTC_USDT","ETH_USDT"]}'
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    curl -X POST https://api.gateio.ws/api/v4/futures/usdt/funding_rates \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    
    

> 请求体示例
    
    
    {
      "contracts": [
        "BTC_USDT",
        "ETH_USDT"
      ]
    }
    

> 返回示例

> 200 返回
    
    
    [
      [
        {
          "contract": "BTC_USDT",
          "data": [
            {
              "t": 1543968000,
              "r": "0.000157"
            },
            {
              "t": 1544054400,
              "r": "0.000145"
            }
          ]
        }
      ]
    ]
    

##  合约市场保险基金历史

GET`/futures/{settle}/insurance`

GET `/futures/{settle}/insurance`

_合约市场保险基金历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [InsuranceRecord]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
InsuranceRecord |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | integer(int64) | Optional |  | 秒 s 精度的 Unix 时间戳  
b | string | Optional |  | 保险基金余额  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/insurance'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/insurance \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "t": 1543968000,
        "b": "83.0031"
      }
    ]
    

##  合约统计信息

GET`/futures/{settle}/contract_stats`

GET `/futures/{settle}/contract_stats`

_合约统计信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 是 | 合约标识  
from | 请求参数 | integer(int64) | 否 | 开始时间戳  
interval | 请求参数 | string | 否 |   
limit | 请求参数 | integer | 否 |   
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [ContractStat]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
ContractStat |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional |  | 统计时间  
lsr_taker | number(double) | Optional |  | 多空吃单比  
lsr_account | number(double) | Optional |  | 多空持仓用户比  
long_liq_size | string | Optional |  | 做多爆仓量（张）  
long_liq_amount | number(double) | Optional |  | 做多爆仓量（交易币种）  
long_liq_usd | number(double) | Optional |  | 做多爆仓量（计价币种）  
long_liq_usd_new | number(double) | Optional |  | 做多爆仓量（计价币种，USDT结算公式：long_liq_size _multiplier_ mark_price）  
short_liq_size | string | Optional |  | 做空爆仓量（张）  
short_liq_amount | number(double) | Optional |  | 做空爆仓量（交易币种）  
short_liq_usd | number(double) | Optional |  | 做空爆仓量（计价币种）  
short_liq_usd_new | number(double) | Optional |  | 做空爆仓量（计价币种，USDT结算公式：short_liq_size _multiplier_ mark_price）  
open_interest | string | Optional |  | 总持仓量（张）  
open_interest_usd | number(double) | Optional |  | 总持仓量（计价币种）  
top_lsr_account | number(double) | Optional |  | 大户多空账户比  
top_lsr_size | string | Optional |  | 大户多空持仓比  
mark_price | number(double) | Optional |  | 标记价格  
top_long_size | string | Optional |  | 大户做多持仓量（张）  
top_short_size | string | Optional |  | 大户做空持仓量（张）  
long_taker_size | string | Optional |  | 多头吃单交易量（张）  
short_taker_size | string | Optional |  | 空头吃单交易量（张）  
top_long_account | integer(int64) | Optional |  | 大户做多账户数  
top_short_account | integer(int64) | Optional |  | 大户做空账户数  
long_users | integer(int64) | Optional |  | 多头持仓用户数量  
short_users | integer(int64) | Optional |  | 空头持仓用户数量  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/contract_stats'
    query_param = 'contract=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/contract_stats?contract=BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "time": 1603865400,
        "lsr_taker": 100,
        "lsr_account": 0.5,
        "long_liq_size": "0",
        "short_liq_size": "0",
        "open_interest": "124724",
        "short_liq_usd": 0,
        "mark_price": "8865",
        "top_lsr_size": "1.02",
        "short_liq_amount": 0,
        "long_liq_amount": 0,
        "open_interest_usd": 1511,
        "top_lsr_account": 1.5,
        "long_liq_usd": 0
      }
    ]
    

##  查询指数来源

GET`/futures/{settle}/index_constituents/{index}`

GET `/futures/{settle}/index_constituents/{index}`

_查询指数来源_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
index | URL | string | 是 | 指数名称  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | FuturesIndexConstituents  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
FuturesIndexConstituents |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
index | string | Optional | readOnly: true | 指数名称  
constituents | array | Optional | readOnly: true | 成分  
  
**constituents**

成分

类型 | 约束  
---|---  
array | readOnly: true  
  
**constituents / items**

IndexConstituent

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
exchange | string | Optional |  | 交易所  
symbols | array | Optional |  | 交易对列表  
  
**constituents / items / symbols**

交易对列表

类型 | 约束  
---|---  
array |   
  
**constituents / items / symbols / items**

类型 | 约束  
---|---  
string |   
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/index_constituents/BTC_USDT'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/index_constituents/BTC_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "index": "BTC_USDT",
      "constituents": [
        {
          "exchange": "Binance",
          "symbols": [
            "BTC_USDT"
          ]
        },
        {
          "exchange": "Gate.com",
          "symbols": [
            "BTC_USDT"
          ]
        },
        {
          "exchange": "Huobi",
          "symbols": [
            "BTC_USDT"
          ]
        }
      ]
    }
    

##  查询强平委托历史

GET`/futures/{settle}/liq_orders`

GET `/futures/{settle}/liq_orders`

_查询强平委托历史_

`from` 和 `to` 的时间间隔最大为 3600。部分私有字段公共接口不会返回，具体参照字段描述

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FuturesLiqOrder]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
FuturesLiqOrder |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | 强制平仓时间  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 用户仓位大小  
order_size | string | Optional | readOnly: true | 强平委托数量  
order_price | string | Optional | readOnly: true | 强平委托价  
fill_price | string | Optional | readOnly: true | 强平委托吃单平均成交价  
left | string | Optional | readOnly: true | 保留字段，当前无业务含义  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/liq_orders'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/liq_orders \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "time": 1548654951,
        "contract": "BTC_USDT",
        "size": "600",
        "order_size": "-600",
        "order_price": "3405",
        "fill_price": "3424",
        "left": "0"
      }
    ]
    

##  查询风险限额等级

GET`/futures/{settle}/risk_limit_tiers`

GET `/futures/{settle}/risk_limit_tiers`

_查询风险限额等级_

contract 参数不传,默认查询前 100 个市场的风险限额,limit 和 offset 对应市场维度的分页查询,不对应返回数组的长度,仅当 contract 参数为空时生效

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [FuturesLimitRiskTiers]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

返回某个指定合同下,不同档位的风险限额配置

类型 | 约束  
---|---  
FuturesLimitRiskTiers |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tier | integer(int) | Optional |  | 档位  
risk_limit | string | Optional |  | 风险限额  
initial_rate | string | Optional |  | 初始保证金率  
maintenance_rate | string | Optional |  | 风险限额的第一档维持保证金率要求  
leverage_max | string | Optional |  | 最大杠杆  
contract | string | Optional |  | 市场,仅当市场分页请求时可见  
deduction | string | Optional |  | 维持保证金速算扣减额  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/risk_limit_tiers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/risk_limit_tiers \
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
    

##  获取合约账号🔒 需要认证

GET`/futures/{settle}/accounts`

GET `/futures/{settle}/accounts`

_获取合约账号_

该接口支持查询经典合约账户和统一账户的合约业务相关信息

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | FuturesAccount  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
FuturesAccount |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | string | Optional |  | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional |  | 未实现盈亏  
position_margin | string | Optional |  | 已废弃  
order_margin | string | Optional |  | 所有未完成订单的起始保证金  
available | string | Optional |  | 指的是逐仓可用的转出或交易的额度，统一账户下包含授信额度的逐仓可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
point | string | Optional |  | 点卡数额  
currency | string | Optional |  | 结算币种  
in_dual_mode | boolean | Optional |  | 是否为双向持仓模式  
enable_credit | boolean | Optional |  | 是否开启统一账户模式  
position_initial_margin | string | Optional |  | 头寸占用的起始保证金，适用于统一账户模式  
maintenance_margin | string | Optional |  | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
bonus | string | Optional |  | 体验金  
enable_evolved_classic | boolean | Optional |  | 已废弃  
cross_order_margin | string | Optional |  | 全仓挂单保证金，适用于新经典账户保证金模式  
cross_initial_margin | string | Optional |  | 全仓初始保证金，适用于新经典账户保证金模式  
cross_maintenance_margin | string | Optional |  | 全仓维持保证金，适用于新经典账户保证金模式  
cross_unrealised_pnl | string | Optional |  | 全仓未实现盈亏，适用于新经典账户保证金模式  
cross_available | string | Optional |  | 全仓可用额度，适用于新经典账户保证金模式  
cross_margin_balance | string | Optional |  | 全仓保证金余额，适用于新经典账户保证金模式  
cross_mmr | string | Optional |  | 全仓维持保证金率，适用于新经典账户保证金模式  
cross_imr | string | Optional |  | 全仓初始保证金率，适用于新经典账户保证金模式  
isolated_position_margin | string | Optional |  | 逐仓仓位保证金，适用于新经典账户保证金模式  
enable_new_dual_mode | boolean | Optional |  | 已废弃  
margin_mode | integer | Optional |  | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
enable_tiered_mm | boolean | Optional |  | 是否开启梯度式计算维持保证金  
enable_dual_plus | boolean | Optional |  | 是否支持分仓模式  
position_mode | string | Optional |  | 持仓模式 single-单向持仓 dual-双向持仓 dual_plus-分仓  
history | object | Optional |  | 累计统计数据  
  
**history**

累计统计数据

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
dnw | string | Optional |  | 累计转入转出  
pnl | string | Optional |  | 累计交易盈亏  
fee | string | Optional |  | 累计手续费  
refr | string | Optional |  | 累计获取的推荐人返佣  
fund | string | Optional |  | 累计资金费用  
point_dnw | string | Optional |  | 累计点卡转入转出  
point_fee | string | Optional |  | 累计点卡抵扣手续费  
point_refr | string | Optional |  | 累计获取的点卡推荐人返佣  
bonus_dnw | string | Optional |  | 累计体验金转入转出  
bonus_offset | string | Optional |  | 累计体验金抵扣  
cross_settle | string | Optional |  | 代表统一账户模式下，合约账户盈利被结算到现货数值。负数代表从合约结算到现货的，正数代表从现货结算到合约的。此数值为累计值  
  
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
    
    url = '/futures/usdt/accounts'
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
    url="/futures/usdt/accounts"
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
      "enable_tiered_mm": true,
      "position_mode": "dual_plus",
      "enable_dual_plus": true
    }
    

##  查询合约账户变更历史🔒 需要认证

GET`/futures/{settle}/account_book`

GET `/futures/{settle}/account_book`

_查询合约账户变更历史_

如果传入`contract`字段，只能筛选2023-10-30后包含该字段的记录。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
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
\- bonus_offset: 体验金抵扣  
\- dividend: 分红派息  
  
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
\- bonus_offset: 体验金抵扣  
\- dividend: 分红派息

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FuturesAccountBook]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
FuturesAccountBook |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | number(double) | Optional |  | 时间  
change | string | Optional |  | 变更金额  
balance | string | Optional |  | 变更后账户余额  
type | string | Optional | enum: ["dnw","pnl","fee","refr","fund","point_dnw","point_fee","point_refr","bonus_offset","dividend"] | 变更类型：  
  
\- dnw: 转入转出  
\- pnl: 减仓盈亏  
\- fee: 交易手续费  
\- refr: 推荐人返佣  
\- fund: 资金费用  
\- point_dnw: 点卡转入转出  
\- point_fee: 点卡交易手续费  
\- point_refr: 点卡推荐人返佣  
\- bonus_offset: 体验金抵扣  
\- dividend: 分红派息  
text | string | Optional |  | 注释  
contract | string | Optional |  | 合约标识，只有2023-10-30后的数据才有该字段  
trade_id | string | Optional |  | 成交 id  
id | string | Optional |  | 账户变更记录 id  
  
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
    
    url = '/futures/usdt/account_book'
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
    url="/futures/usdt/account_book"
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

GET`/futures/{settle}/positions`

GET `/futures/{settle}/positions`

_获取用户仓位列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
holding | 请求参数 | boolean | 否 | 只返回真实持仓-true,全部返回-false  
limit | 请求参数 | integer | 否 | 列表返回的最大数量，不传时默认返回当前全部的仓位，传入时则只允许传入[1,100]的范围  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [Position]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**items / close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/positions'
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
    url="/futures/usdt/positions"
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
        "size": "-9440",
        "hedge_status": "partial_hedged",
        "hedged_size": "12",
        "unhedged_size": "9428",
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
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  根据时间获取用户历史仓位信息列表🔒 需要认证

GET`/futures/{settle}/positions_timerange`

GET `/futures/{settle}/positions_timerange`

_根据时间获取用户历史仓位信息列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 是 | 合约标识  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [PositionTimerange]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约仓位详情(历史数据)

类型 | 约束  
---|---  
PositionTimerange |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
leverage | string | Optional |  | 杠杆倍数，0代表全仓，正数代表逐仓  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 风险限额的第一档维持保证金率要求  
margin | string | Optional |  | 保证金  
liq_price | string | Optional | readOnly: true | 爆仓价格  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏  
history_pnl | string | Optional | readOnly: true | 已平仓的仓位总盈亏  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
mode | string | Optional |  | 持仓模式。包括：  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数（即 `leverage` 为 0 时）  
entry_price | string | Optional | readOnly: true | 开仓价格  
time | integer(int64) | Optional |  | 时间戳  
  
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
    
    url = '/futures/usdt/positions_timerange'
    query_param = 'contract=BTC_USDT'
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
    url="/futures/usdt/positions_timerange"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "hedge_status": "partial_hedged",
        "hedged_size": "12",
        "unhedged_size": "9428",
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
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  获取单个仓位信息🔒 需要认证

GET`/futures/{settle}/positions/{contract}`

GET `/futures/{settle}/positions/{contract}`

_获取单个仓位信息_

获取指定合约市场下的仓位信息。如果您在一个合约市场下持有双向的两个仓位，请使用此接口：/futures/{settle}/dual_comp/positions/{contract}

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | Position  
  
### 返回格式

状态码 **200**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT'
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
    url="/futures/usdt/positions/BTC_USDT"
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
      "size": "-9440",
      "hedge_status": "partial_hedged",
      "hedged_size": "12",
      "unhedged_size": "9428",
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
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  获取指定模式的杠杆信息🔒 需要认证

GET`/futures/{settle}/get_leverage/{contract}`

GET `/futures/{settle}/get_leverage/{contract}`

_获取指定模式的杠杆信息_

获取指定模式的杠杆信息

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
pos_margin_mode | 请求参数 | string | 是 | 仓位保证金模式, 分仓模式必传，取值isolated/cross。  
dual_side | 请求参数 | string | 是 | dual_long - 多 dual_short - 空  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询杠杆成功 | FuturesLeverage  
  
### 返回格式

状态码 **200**

返回结果包含Lever字段

类型 | 约束  
---|---  
FuturesLeverage |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
Lever | string | Optional |  | 杠杆  
  
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
    
    url = '/futures/usdt/get_leverage/BTC_USDT'
    query_param = 'pos_margin_mode=isolated&dual_side=dual_long'
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
    url="/futures/usdt/get_leverage/BTC_USDT"
    query_param="pos_margin_mode=isolated&dual_side=dual_long"
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
      "Lever": "10"
    }
    

##  更新仓位保证金🔒 需要认证

POST`/futures/{settle}/positions/{contract}/margin`

POST `/futures/{settle}/positions/{contract}/margin`

_更新仓位保证金_

在新的风险限额规则(https://www.gate.com/zh/help/futures/futures-logic/22162)下，持仓限额和杠杆倍数相关，设置越低的杠杆倍数即会获得越大的持仓限额。请使用调整杠杆倍数的接口来调整限额。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
change | 请求参数 | string | 是 | 保证金变化数额，正数增加，负数减少  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | Position  
  
### 返回格式

状态码 **200**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT/margin'
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
    url="/futures/usdt/positions/BTC_USDT/margin"
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
      "size": "-9440",
      "hedge_status": "partial_hedged",
      "hedged_size": "12",
      "unhedged_size": "9428",
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
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  更新仓位杠杆🔒 需要认证

POST`/futures/{settle}/positions/{contract}/leverage`

POST `/futures/{settle}/positions/{contract}/leverage`

_更新仓位杠杆_

⚠️ 仓位模式切换规则：

  * leverage ≠ 0：逐仓模式（无论是否填写 cross_leverage_limit，该参数都会被忽略）
  * leverage = 0：全仓模式（使用 cross_leverage_limit 设置杠杆倍数）

示例：

  * 设置逐仓 10 倍杠杆：leverage=10
  * 设置全仓 10 倍杠杆：leverage=0&cross_leverage_limit=10
  * leverage=5&cross_leverage_limit=10 → 结果为逐仓 5 倍（cross_leverage_limit 被忽略）

⚠️ 警告：错误设置可能导致仓位模式意外切换，影响风险管理。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
leverage | 请求参数 | string | 是 | 该字段用于设置逐仓的杠杆倍数，且设置逐仓杠杆倍数时需要“cross_leverage_limit”字段设置为空  
cross_leverage_limit | 请求参数 | string | 否 | 该字段用于设置全仓的杠杆倍数，且设置全仓杠杆倍数时需同时将“leverage”字段设置为0  
pid | 请求参数 | integer(int32) | 否 | 产品ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | Position  
  
### 返回格式

状态码 **200**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT/leverage'
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
    url="/futures/usdt/positions/BTC_USDT/leverage"
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
      "size": "-9440",
      "hedge_status": "partial_hedged",
      "hedged_size": "12",
      "unhedged_size": "9428",
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
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  更新指定模式的杠杆🔒 需要认证

POST`/futures/{settle}/positions/{contract}/set_leverage`

POST `/futures/{settle}/positions/{contract}/set_leverage`

_更新指定模式的杠杆_

为了简化leverage接口复杂逻辑，新增修改杠杆的接口

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
leverage | 请求参数 | string | 是 | 仓位杠杆倍数  
margin_mode | 请求参数 | string | 是 | 保证金模式 isolated/cross  
dual_side | 请求参数 | string | 否 | dual_long - 多 dual_short - 空  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | Position  
  
### 返回格式

状态码 **200**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT/set_leverage'
    query_param = 'leverage=10&margin_mode=cross'
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
    url="/futures/usdt/positions/BTC_USDT/set_leverage"
    query_param="leverage=10&margin_mode=cross"
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
      "size": "-9440",
      "hedge_status": "partial_hedged",
      "hedged_size": "12",
      "unhedged_size": "9428",
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
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  切换全逐仓模式🔒 需要认证

POST`/futures/{settle}/positions/cross_mode`

POST `/futures/{settle}/positions/cross_mode`

_切换全逐仓模式_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
body | body | FuturesPositionCrossMode | 是 |   
mode | body | string | 是 | 全逐仓模式，ISOLATED-逐仓，CROSS-全仓  
contract | body | string | 是 | 合约市场  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

FuturesPositionCrossMode

请求体结构类型 | 约束  
---|---  
FuturesPositionCrossMode | required: ["mode","contract"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
mode | string | Required |  | 全逐仓模式，ISOLATED-逐仓，CROSS-全仓  
contract | string | Required |  | 合约市场  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | Position  
  
### 返回格式

状态码 **200**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/positions/cross_mode'
    query_param = ''
    body='{"mode":"ISOLATED","contract":"BTC_USDT"}'
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
    url="/futures/usdt/positions/cross_mode"
    query_param=""
    body_param='{"mode":"ISOLATED","contract":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "mode": "ISOLATED",
      "contract": "BTC_USDT"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "user": 10000,
      "contract": "BTC_USDT",
      "size": "-9440",
      "hedge_status": "partial_hedged",
      "hedged_size": "12",
      "unhedged_size": "9428",
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
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  双仓模式下切换全逐仓模式🔒 需要认证

POST`/futures/{settle}/dual_comp/positions/cross_mode`

POST `/futures/{settle}/dual_comp/positions/cross_mode`

_双仓模式下切换全逐仓模式_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
body | body | UpdateDualCompPositionCrossModeRequest | 是 |   
mode | body | string | 是 | 全逐仓模式，ISOLATED-逐仓，CROSS-全仓  
contract | body | string | 是 | 合约市场  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

UpdateDualCompPositionCrossModeRequest

请求体结构类型 | 约束  
---|---  
UpdateDualCompPositionCrossModeRequest | required: ["mode","contract"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
mode | string | Required |  | 全逐仓模式，ISOLATED-逐仓，CROSS-全仓  
contract | string | Required |  | 合约市场  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [Position]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**items / close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/dual_comp/positions/cross_mode'
    query_param = ''
    body='{"mode":"ISOLATED","contract":"BTC_USDT"}'
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
    url="/futures/usdt/dual_comp/positions/cross_mode"
    query_param=""
    body_param='{"mode":"ISOLATED","contract":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "mode": "ISOLATED",
      "contract": "BTC_USDT"
    }
    

> 返回示例

> 200 返回
    
    
    [
      {
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "hedge_status": "partial_hedged",
        "hedged_size": "12",
        "unhedged_size": "9428",
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
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  更新仓位风险限额🔒 需要认证

POST`/futures/{settle}/positions/{contract}/risk_limit`

POST `/futures/{settle}/positions/{contract}/risk_limit`

_更新仓位风险限额_

在新的风险限额规则(https://www.gate.com/zh/help/futures/futures-logic/22162)下，持仓限额和杠杆倍数相关，设置越低的杠杆倍数即会获得越大的持仓限额。请使用调整杠杆倍数的接口来调整限额。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
risk_limit | 请求参数 | string | 是 | 新的风险限额价值  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 仓位信息 | Position  
  
### 返回格式

状态码 **200**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/positions/BTC_USDT/risk_limit'
    query_param = 'risk_limit=1000000'
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
    url="/futures/usdt/positions/BTC_USDT/risk_limit"
    query_param="risk_limit=1000000"
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
      "size": "-9440",
      "hedge_status": "partial_hedged",
      "hedged_size": "12",
      "unhedged_size": "9428",
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
      "average_maintenance_rate": "0.005",
      "pos_margin_mode": "isolated",
      "lever": "30"
    }
    

##  设置持仓模式🔒 需要认证

POST`/futures/{settle}/dual_mode`

POST `/futures/{settle}/dual_mode`

_设置持仓模式_

变更模式的前提是，所有仓位没有持仓，并且没有挂单

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
dual_mode | 请求参数 | boolean | 是 | 是否设置为双向持仓  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 修改成功 | FuturesAccount  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
FuturesAccount |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | string | Optional |  | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional |  | 未实现盈亏  
position_margin | string | Optional |  | 已废弃  
order_margin | string | Optional |  | 所有未完成订单的起始保证金  
available | string | Optional |  | 指的是逐仓可用的转出或交易的额度，统一账户下包含授信额度的逐仓可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
point | string | Optional |  | 点卡数额  
currency | string | Optional |  | 结算币种  
in_dual_mode | boolean | Optional |  | 是否为双向持仓模式  
enable_credit | boolean | Optional |  | 是否开启统一账户模式  
position_initial_margin | string | Optional |  | 头寸占用的起始保证金，适用于统一账户模式  
maintenance_margin | string | Optional |  | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
bonus | string | Optional |  | 体验金  
enable_evolved_classic | boolean | Optional |  | 已废弃  
cross_order_margin | string | Optional |  | 全仓挂单保证金，适用于新经典账户保证金模式  
cross_initial_margin | string | Optional |  | 全仓初始保证金，适用于新经典账户保证金模式  
cross_maintenance_margin | string | Optional |  | 全仓维持保证金，适用于新经典账户保证金模式  
cross_unrealised_pnl | string | Optional |  | 全仓未实现盈亏，适用于新经典账户保证金模式  
cross_available | string | Optional |  | 全仓可用额度，适用于新经典账户保证金模式  
cross_margin_balance | string | Optional |  | 全仓保证金余额，适用于新经典账户保证金模式  
cross_mmr | string | Optional |  | 全仓维持保证金率，适用于新经典账户保证金模式  
cross_imr | string | Optional |  | 全仓初始保证金率，适用于新经典账户保证金模式  
isolated_position_margin | string | Optional |  | 逐仓仓位保证金，适用于新经典账户保证金模式  
enable_new_dual_mode | boolean | Optional |  | 已废弃  
margin_mode | integer | Optional |  | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
enable_tiered_mm | boolean | Optional |  | 是否开启梯度式计算维持保证金  
enable_dual_plus | boolean | Optional |  | 是否支持分仓模式  
position_mode | string | Optional |  | 持仓模式 single-单向持仓 dual-双向持仓 dual_plus-分仓  
history | object | Optional |  | 累计统计数据  
  
**history**

累计统计数据

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
dnw | string | Optional |  | 累计转入转出  
pnl | string | Optional |  | 累计交易盈亏  
fee | string | Optional |  | 累计手续费  
refr | string | Optional |  | 累计获取的推荐人返佣  
fund | string | Optional |  | 累计资金费用  
point_dnw | string | Optional |  | 累计点卡转入转出  
point_fee | string | Optional |  | 累计点卡抵扣手续费  
point_refr | string | Optional |  | 累计获取的点卡推荐人返佣  
bonus_dnw | string | Optional |  | 累计体验金转入转出  
bonus_offset | string | Optional |  | 累计体验金抵扣  
cross_settle | string | Optional |  | 代表统一账户模式下，合约账户盈利被结算到现货数值。负数代表从合约结算到现货的，正数代表从现货结算到合约的。此数值为累计值  
  
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
    
    url = '/futures/usdt/dual_mode'
    query_param = 'dual_mode=true'
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
    url="/futures/usdt/dual_mode"
    query_param="dual_mode=true"
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
      "enable_tiered_mm": true,
      "position_mode": "dual_plus",
      "enable_dual_plus": true
    }
    

##  设置持仓模式,替换dual_mode接口🔒 需要认证

POST`/futures/{settle}/set_position_mode`

POST `/futures/{settle}/set_position_mode`

_设置持仓模式,替换dual_mode接口_

变更模式的前提是，所有仓位没有持仓，并且没有挂单

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
position_mode | 请求参数 | string | 是 | 可选值：single, dual, dual_plus，分别表示单向、双向、分仓  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 修改成功 | FuturesAccount  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
FuturesAccount |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | string | Optional |  | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional |  | 未实现盈亏  
position_margin | string | Optional |  | 已废弃  
order_margin | string | Optional |  | 所有未完成订单的起始保证金  
available | string | Optional |  | 指的是逐仓可用的转出或交易的额度，统一账户下包含授信额度的逐仓可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
point | string | Optional |  | 点卡数额  
currency | string | Optional |  | 结算币种  
in_dual_mode | boolean | Optional |  | 是否为双向持仓模式  
enable_credit | boolean | Optional |  | 是否开启统一账户模式  
position_initial_margin | string | Optional |  | 头寸占用的起始保证金，适用于统一账户模式  
maintenance_margin | string | Optional |  | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
bonus | string | Optional |  | 体验金  
enable_evolved_classic | boolean | Optional |  | 已废弃  
cross_order_margin | string | Optional |  | 全仓挂单保证金，适用于新经典账户保证金模式  
cross_initial_margin | string | Optional |  | 全仓初始保证金，适用于新经典账户保证金模式  
cross_maintenance_margin | string | Optional |  | 全仓维持保证金，适用于新经典账户保证金模式  
cross_unrealised_pnl | string | Optional |  | 全仓未实现盈亏，适用于新经典账户保证金模式  
cross_available | string | Optional |  | 全仓可用额度，适用于新经典账户保证金模式  
cross_margin_balance | string | Optional |  | 全仓保证金余额，适用于新经典账户保证金模式  
cross_mmr | string | Optional |  | 全仓维持保证金率，适用于新经典账户保证金模式  
cross_imr | string | Optional |  | 全仓初始保证金率，适用于新经典账户保证金模式  
isolated_position_margin | string | Optional |  | 逐仓仓位保证金，适用于新经典账户保证金模式  
enable_new_dual_mode | boolean | Optional |  | 已废弃  
margin_mode | integer | Optional |  | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
enable_tiered_mm | boolean | Optional |  | 是否开启梯度式计算维持保证金  
enable_dual_plus | boolean | Optional |  | 是否支持分仓模式  
position_mode | string | Optional |  | 持仓模式 single-单向持仓 dual-双向持仓 dual_plus-分仓  
history | object | Optional |  | 累计统计数据  
  
**history**

累计统计数据

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
dnw | string | Optional |  | 累计转入转出  
pnl | string | Optional |  | 累计交易盈亏  
fee | string | Optional |  | 累计手续费  
refr | string | Optional |  | 累计获取的推荐人返佣  
fund | string | Optional |  | 累计资金费用  
point_dnw | string | Optional |  | 累计点卡转入转出  
point_fee | string | Optional |  | 累计点卡抵扣手续费  
point_refr | string | Optional |  | 累计获取的点卡推荐人返佣  
bonus_dnw | string | Optional |  | 累计体验金转入转出  
bonus_offset | string | Optional |  | 累计体验金抵扣  
cross_settle | string | Optional |  | 代表统一账户模式下，合约账户盈利被结算到现货数值。负数代表从合约结算到现货的，正数代表从现货结算到合约的。此数值为累计值  
  
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
    
    url = '/futures/usdt/set_position_mode'
    query_param = 'position_mode=dual_plus'
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
    url="/futures/usdt/set_position_mode"
    query_param="position_mode=dual_plus"
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
      "enable_tiered_mm": true,
      "position_mode": "dual_plus",
      "enable_dual_plus": true
    }
    

##  获取双仓模式下的持仓信息🔒 需要认证

GET`/futures/{settle}/dual_comp/positions/{contract}`

GET `/futures/{settle}/dual_comp/positions/{contract}`

_获取双仓模式下的持仓信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [Position]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**items / close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/dual_comp/positions/BTC_USDT'
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
    url="/futures/usdt/dual_comp/positions/BTC_USDT"
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
        "size": "-9440",
        "hedge_status": "partial_hedged",
        "hedged_size": "12",
        "unhedged_size": "9428",
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
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  更新双仓模式下的保证金🔒 需要认证

POST`/futures/{settle}/dual_comp/positions/{contract}/margin`

POST `/futures/{settle}/dual_comp/positions/{contract}/margin`

_更新双仓模式下的保证金_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
change | 请求参数 | string | 是 | 保证金变化数额，正数增加，负数减少  
dual_side | 请求参数 | string | 是 | 多头或空头仓位  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [Position]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**items / close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/dual_comp/positions/BTC_USDT/margin'
    query_param = 'change=0.01&dual_side=dual_long'
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
    url="/futures/usdt/dual_comp/positions/BTC_USDT/margin"
    query_param="change=0.01&dual_side=dual_long"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "hedge_status": "partial_hedged",
        "hedged_size": "12",
        "unhedged_size": "9428",
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
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  更新双仓模式下的杠杆🔒 需要认证

POST`/futures/{settle}/dual_comp/positions/{contract}/leverage`

POST `/futures/{settle}/dual_comp/positions/{contract}/leverage`

_更新双仓模式下的杠杆_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
leverage | 请求参数 | string | 是 | 新的杠杆倍数  
cross_leverage_limit | 请求参数 | string | 否 | 全仓模式下的杠杆倍数（即 `leverage` 为 0 时）  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [Position]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**items / close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/dual_comp/positions/BTC_USDT/leverage'
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
    url="/futures/usdt/dual_comp/positions/BTC_USDT/leverage"
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
    
    
    [
      {
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "hedge_status": "partial_hedged",
        "hedged_size": "12",
        "unhedged_size": "9428",
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
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  更新双仓模式下的风险限额🔒 需要认证

POST`/futures/{settle}/dual_comp/positions/{contract}/risk_limit`

POST `/futures/{settle}/dual_comp/positions/{contract}/risk_limit`

_更新双仓模式下的风险限额_

在新的风险限额规则(https://www.gate.com/zh/help/futures/futures-logic/22162)下，持仓限额和杠杆倍数相关，设置越低的杠杆倍数即会获得越大的持仓限额。请使用调整杠杆倍数的接口来调整限额。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | URL | string | 是 | 合约标识  
risk_limit | 请求参数 | string | 是 | 新的风险限额价值  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [Position]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约仓位详情

类型 | 约束  
---|---  
Position |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**items / close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
  
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
    
    url = '/futures/usdt/dual_comp/positions/BTC_USDT/risk_limit'
    query_param = 'risk_limit=1000000'
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
    url="/futures/usdt/dual_comp/positions/BTC_USDT/risk_limit"
    query_param="risk_limit=1000000"
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
        "user": 10000,
        "contract": "BTC_USDT",
        "size": "-9440",
        "hedge_status": "partial_hedged",
        "hedged_size": "12",
        "unhedged_size": "9428",
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
        "average_maintenance_rate": "0.005",
        "pos_margin_mode": "isolated",
        "lever": "30"
      }
    ]
    

##  查询合约订单列表🔒 需要认证

GET`/futures/{settle}/orders`

GET `/futures/{settle}/orders`

_查询合约订单列表_

  * 零成交且已撤销的订单，自撤单 10 分钟后无法再通过该查询接口获取。
  * 历史委托订单，默认只支持查询半年内的数据，如果需要查询更久的数据，请使用`GET /futures/{settle}/orders_timerange`

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
status | 请求参数 | string | 是 | 基于状态查询订单列表  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
last_id | 请求参数 | string | 否 | 以上个列表的最后一条记录的 ID 作为下个列表的起点  
  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后，在结束之后 1 小时内可查，过期之后只能使用订单 ID  
settle | URL | string | 是 | 永续合约结算货币  
  
####  详细描述

**last_id** : 以上个列表的最后一条记录的 ID 作为下个列表的起点  
  
基于自定义 ID 的操作只在挂单中可查，当结束订单（成交/取消）后，在结束之后 1 小时内可查，过期之后只能使用订单 ID

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FuturesOrder]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约订单详情

类型 | 约束  
---|---  
FuturesOrder | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
  
###  返回头部

返回头部状态码 | 头部 | 类型 | 格式 | 描述  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | 分页时指定的 limit  
200 | X-Pagination-Offset | integer |  | 分页时指定的 offset  
  
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
    
    url = '/futures/usdt/orders'
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
    url="/futures/usdt/orders"
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
        "create_time": 1546569968.123456,
        "update_time": 1546569970.456789,
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
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
        "finish_time": 1546569970.456789,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "order_value": "64112.2099000000005",
        "trade_value": "64112.2099000000005",
        "market_order_slip_ratio": "0.03",
        "pos_margin_mode": "isolated",
        "tpsl_tp_trigger_price": "3800",
        "tpsl_sl_trigger_price": "3700"
      }
    ]
    

##  合约交易下单🔒 需要认证

POST`/futures/{settle}/orders`

POST `/futures/{settle}/orders`

_合约交易下单_

  * 下单时指定的是合约张数 `size` ，而非币的数量，每一张合约对应的币的数量是合约详情接口里返回的 `quanto_multiplier`
  * 下单使用小数张数时，请带 `X-Gate-Size-Decimal: 1` 查询目标合约，确认 `enable_decimal` 为 `true`，并读取 `order_size_min` 和 `order_size_max`。下单时携带相同请求头，并用十进制字符串传入小数 `size` 或小数冰山显示张数 `iceberg`。
  * 0 成交的订单在撤单 10 分钟之后无法再获取到，会提到订单不存在
  * 设置 `reduce_only` 为 `true` 可以防止在减仓的时候穿仓
  * 单仓模式下，如果需要平仓，需要设置 `size` 为 0 ，`close` 为 `true`
  * 双仓模式下，
  * 减仓：reduce_only=true，size 为正数表示减空仓，负数表示减多仓
  * 加仓：reduce_only=false，size 为正数表示加多仓，负数表示加空仓
  * 平仓：size=0，根据 auto_size 设置平仓的方向，并同时设置 `reduce_only` 为 true
  * reduce_only：确保只执行减仓操作，防止增加仓位
  * 设置 `stp_act` 决定使用限制用户自成交的策略，详细用法参考body参数`stp_act`

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | FuturesOrder | 是 |   
id | body | integer(int64) | 否 | 合约订单 ID  
user | body | integer | 否 | 用户 ID  
create_time | body | number(double) | 否 | 订单创建时间  
update_time | body | number(double) | 否 | 订单更新时间  
finish_time | body | number(double) | 否 | 订单结束时间，未结束订单无此字段返回  
finish_as | body | string | 否 | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
  
status | body | string | 否 | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
  
contract | body | string | 是 | 合约标识  
size | body | string | 是 | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
  
iceberg | body | string | 否 | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
  
price | body | string | 是 | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | body | boolean | 否 | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | body | boolean | 否 | 是否为平仓委托。对应请求中的`close`。  
reduce_only | body | boolean | 否 | 设置为 true 的时候，为只减仓委托  
is_reduce_only | body | boolean | 否 | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | body | boolean | 否 | 是否为强制平仓委托  
tif | body | string | 否 | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
  
left | body | string | 否 | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
  
fill_price | body | string | 否 | 成交价  
text | body | string | 否 | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
  
tkfr | body | string | 否 | 吃单手续费率。  
mkfr | body | string | 否 | 挂单手续费率。  
refu | body | integer | 否 | 推荐人用户 ID  
auto_size | body | string | 否 | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | body | integer | 否 | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
  
stp_act | body | string | 否 | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
  
amend_text | body | string | 否 | 用户修改订单时备注的信息  
pid | body | integer(int64) | 否 | 仓位ID  
market_order_slip_ratio | body | string | 否 | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | body | string | 否 | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | body | string | 否 | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
  
tpsl_tp_trigger_price | body | string | 否 | 止盈价  
tpsl_sl_trigger_price | body | string | 否 | 止损价  
tpsl_tp_bbo_type | body | string | 否 | 止盈bbo类型  
tpsl_sl_bbo_type | body | string | 否 | 止损bbo类型  
settle | URL | string | 是 | 永续合约结算货币  
  
####  详细描述

** finish_as**: 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  

** status**: 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  

** size**: 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  

** iceberg**: 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  

** tif**: Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  

** left**: 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  

** text**: 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  

** stp_id**: 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  

** stp_act**: Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  

** action_mode**: 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  

####  枚举值列表

枚举值列表参数 | 值  
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
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

合约订单详情

请求体结构类型 | 约束  
---|---  
FuturesOrder | required: ["contract","size","price"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 订单详情 | FuturesOrder  
  
### 返回格式

状态码 **201**

合约订单详情

类型 | 约束  
---|---  
FuturesOrder | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
  
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
    
    url = '/futures/usdt/orders'
    query_param = ''
    body='{"contract":"BTC_USDT","size":"6024","iceberg":"0","price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-","order_value":"64112.2099000000005","trade_value":"64112.2099000000005","market_order_slip_ratio":"0.03","pos_margin_mode":"isolated","tpsl_tp_trigger_price":"3800","tpsl_sl_trigger_price":"3700"}'
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
    url="/futures/usdt/orders"
    query_param=""
    body_param='{"contract":"BTC_USDT","size":"6024","iceberg":"0","price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-","order_value":"64112.2099000000005","trade_value":"64112.2099000000005","market_order_slip_ratio":"0.03","pos_margin_mode":"isolated","tpsl_tp_trigger_price":"3800","tpsl_sl_trigger_price":"3700"}'
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
      "size": "6024",
      "iceberg": "0",
      "price": "3765",
      "tif": "gtc",
      "text": "t-my-custom-id",
      "stp_act": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

> 返回示例

> 201 返回
    
    
    {
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968.123456,
      "update_time": 1546569970.456789,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
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
      "finish_time": 1546569970.456789,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  批量取消状态为 open 的订单🔒 需要认证

DELETE`/futures/{settle}/orders`

DELETE `/futures/{settle}/orders`

_批量取消状态为 open 的订单_

0 成交的订单在撤单 10 分钟之后无法获取

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只撤销该合约相关挂单  
action_mode | 请求参数 | string | 否 | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
side | 请求参数 | string | 否 | 指定全部买单或全部卖单，不指定则两者都包括。撤销全部买单设置为bid，撤销全部卖单设置为ask  
exclude_reduce_only | 请求参数 | boolean | 否 | 是否排除仅减仓订单  
text | 请求参数 | string | 否 | 取消订单的备注信息  
settle | URL | string | 是 | 永续合约结算货币  
  
####  详细描述

**action_mode** : 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 批量撤销成功 | [FuturesOrder]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约订单详情

类型 | 约束  
---|---  
FuturesOrder | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
  
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
    
    url = '/futures/usdt/orders'
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
    url="/futures/usdt/orders"
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
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968.123456,
        "update_time": 1546569970.456789,
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
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
        "finish_time": 1546569970.456789,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "order_value": "64112.2099000000005",
        "trade_value": "64112.2099000000005",
        "market_order_slip_ratio": "0.03",
        "pos_margin_mode": "isolated",
        "tpsl_tp_trigger_price": "3800",
        "tpsl_sl_trigger_price": "3700"
      }
    ]
    

##  查询合约订单列表(时间区间)🔒 需要认证

GET`/futures/{settle}/orders_timerange`

GET `/futures/{settle}/orders_timerange`

_查询合约订单列表(时间区间)_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FuturesOrderTimerange]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约订单详情

类型 | 约束  
---|---  
FuturesOrderTimerange | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | string | Optional | readOnly: true | 订单更新时间  
finish_time | string | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 未成交数量  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单费率  
mkfr | string | Optional | readOnly: true | 做单费率  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
  
###  返回头部

返回头部状态码 | 头部 | 类型 | 格式 | 描述  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | 分页时指定的 limit  
200 | X-Pagination-Offset | integer |  | 分页时指定的 offset  
  
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
    
    url = '/futures/usdt/orders_timerange'
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
    url="/futures/usdt/orders_timerange"
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
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968.123456,
        "update_time": "1546569970.456789",
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
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
        "finish_time": "1546569970.456789",
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "order_value": "64112.2099000000005",
        "trade_value": "64112.2099000000005",
        "market_order_slip_ratio": "0.03",
        "pos_margin_mode": "isolated",
        "tpsl_tp_trigger_price": "3800",
        "tpsl_sl_trigger_price": "3700"
      }
    ]
    

##  合约交易批量下单🔒 需要认证

POST`/futures/{settle}/batch_orders`

POST `/futures/{settle}/batch_orders`

_合约交易批量下单_

  * 最多指定10个委托
  * 如果有某个委托的参数缺失或格式错误，则全部不执行，并直接返回400错误
  * 如果参数检查通过，则全部执行。即便中间有业务逻辑错误（比如资金不足），也不会影响其他执行委托
  * 返回结果是数组格式，顺序跟请求体中的委托一一对应
  * 返回结果的数组成员中，通过bool类型的`succeeded`字段，代表是否执行成功
  * 如果执行成功，则包含正常委托内容；如果执行失败，则包括`label`字段表示错误原因
  * 在访问频率限制中，每个委托都单独计一次

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | array[FuturesOrder] | 是 |   
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

请求体结构类型 | 约束  
---|---  
array |   
  
**items**

合约订单详情

请求体结构类型 | 约束  
---|---  
FuturesOrder | required: ["contract","size","price"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求执行完成 | [BatchFuturesOrder]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约订单详情

类型 | 约束  
---|---  
BatchFuturesOrder |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
succeeded | boolean | Optional |  | 请求执行结果  
label | string | Optional |  | 错误标识，仅当执行失败时存在  
detail | string | Optional |  | 错误详情，仅当执行失败并需要给出详情时存在  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
contract | string | Optional |  | 合约标识  
size | string | Optional |  | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Optional |  | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 未成交数量  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
tkfr | string | Optional | readOnly: true | 吃单费率  
mkfr | string | Optional | readOnly: true | 做单费率  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
market_order_slip_ratio | string | Optional |  | 最大滑点比率  
  
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
    
    url = '/futures/usdt/batch_orders'
    query_param = ''
    body='[{"contract":"BTC_USDT","size":"6024","iceberg":"0","price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-","order_value":"64112.2099000000005","trade_value":"64112.2099000000005","market_order_slip_ratio":"0.03","pos_margin_mode":"isolated","tpsl_tp_trigger_price":"3800","tpsl_sl_trigger_price":"3700"}]'
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
    url="/futures/usdt/batch_orders"
    query_param=""
    body_param='[{"contract":"BTC_USDT","size":"6024","iceberg":"0","price":"3765","tif":"gtc","text":"t-my-custom-id","stp_act":"-","order_value":"64112.2099000000005","trade_value":"64112.2099000000005","market_order_slip_ratio":"0.03","pos_margin_mode":"isolated","tpsl_tp_trigger_price":"3800","tpsl_sl_trigger_price":"3700"}]'
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
        "contract": "BTC_USDT",
        "size": "6024",
        "iceberg": "0",
        "price": "3765",
        "tif": "gtc",
        "text": "t-my-custom-id",
        "stp_act": "-",
        "order_value": "64112.2099000000005",
        "trade_value": "64112.2099000000005",
        "market_order_slip_ratio": "0.03",
        "pos_margin_mode": "isolated",
        "tpsl_tp_trigger_price": "3800",
        "tpsl_sl_trigger_price": "3700"
      }
    ]
    

> 返回示例

> 200 返回
    
    
    [
      {
        "succeeded": true,
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968.123456,
        "update_time": 1546569970.456789,
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
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
        "finish_time": 1546569970.456789,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "market_order_slip_ratio": "0.03"
      }
    ]
    

##  查询单个订单详情🔒 需要认证

GET`/futures/{settle}/orders/{order_id}`

GET `/futures/{settle}/orders/{order_id}`

_查询单个订单详情_

  * 零成交且已撤销的订单，自撤单 10 分钟后无法再通过该查询接口获取。
  * 历史委托订单详情，默认只支持查询半年内的数据。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
order_id | URL | string | 是 | 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID(即 text field)。基于自定义id text字段：  
1\. 如果订单没有成交且已撤单，60 秒后无法使用 text 字段查询该订单的信息，继续使用该字段查询会返回 ORDER_NOT_FOUND 错误。  
2\. 如果订单已完全成交或部分成交，您可以无限期地使用 text 字段查询该订单信息。  
  
####  详细描述

**order_id** : 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID(即 text field)。基于自定义id text字段：  
1\. 如果订单没有成交且已撤单，60 秒后无法使用 text 字段查询该订单的信息，继续使用该字段查询会返回 ORDER_NOT_FOUND 错误。  
2\. 如果订单已完全成交或部分成交，您可以无限期地使用 text 字段查询该订单信息。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单详情 | FuturesOrder  
  
### 返回格式

状态码 **200**

合约订单详情

类型 | 约束  
---|---  
FuturesOrder | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
  
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
    
    url = '/futures/usdt/orders/12345'
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
    url="/futures/usdt/orders/12345"
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
      "create_time": 1546569968.123456,
      "update_time": 1546569970.456789,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
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
      "finish_time": 1546569970.456789,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  修改单个订单🔒 需要认证

PUT`/futures/{settle}/orders/{order_id}`

PUT `/futures/{settle}/orders/{order_id}`

_修改单个订单_

将委托张数改为小数时，请带 `X-Gate-Size-Decimal: 1` 查询原订单所属合约，确认 `enable_decimal` 为 `true`，并读取 `order_size_min` 和 `order_size_max`。改单时携带相同请求头，并用十进制字符串传入新的 `size`。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | FuturesOrderAmendment | 是 |   
size | body | string | 否 | 新的委托大小。包括已成交委托的部分。  
  
\- 如果小于等于已成交数量，则撤销委托。  
\- 新的委托买卖方向必须跟原有的一致。  
\- 不能修改平仓单的size。  
\- 对于只减仓委托，如果调大size，则可能踢出其他只减仓委托。  
\- 如果不修改价格，则调小size不会影响深度排队，调大size会排到当前价位最后。  
price | body | string | 否 | 新的委托价格。  
amend_text | body | string | 否 | 用户可以备注这次修改的信息。  
text | body | string | 否 | 内部用户可以在text修改信息。  
action_mode | body | string | 否 | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
settle | URL | string | 是 | 永续合约结算货币  
order_id | URL | string | 是 | 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID(即 text field)。基于自定义id text字段：  
1\. 如果订单没有成交且已撤单，60 秒后无法使用 text 字段查询该订单的信息，继续使用该字段查询会返回 ORDER_NOT_FOUND 错误。  
2\. 如果订单已完全成交或部分成交，您可以无限期地使用 text 字段查询该订单信息。  
  
####  详细描述

** size**: 新的委托大小。包括已成交委托的部分。  
  
\- 如果小于等于已成交数量，则撤销委托。  
\- 新的委托买卖方向必须跟原有的一致。  
\- 不能修改平仓单的size。  
\- 对于只减仓委托，如果调大size，则可能踢出其他只减仓委托。  
\- 如果不修改价格，则调小size不会影响深度排队，调大size会排到当前价位最后。

** action_mode**: 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）

**order_id** : 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID(即 text field)。基于自定义id text字段：  
1\. 如果订单没有成交且已撤单，60 秒后无法使用 text 字段查询该订单的信息，继续使用该字段查询会返回 ORDER_NOT_FOUND 错误。  
2\. 如果订单已完全成交或部分成交，您可以无限期地使用 text 字段查询该订单信息。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

FuturesOrderAmendment

请求体结构类型 | 约束  
---|---  
FuturesOrderAmendment |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
size | string | Optional |  | 新的委托大小。包括已成交委托的部分。  
  
\- 如果小于等于已成交数量，则撤销委托。  
\- 新的委托买卖方向必须跟原有的一致。  
\- 不能修改平仓单的size。  
\- 对于只减仓委托，如果调大size，则可能踢出其他只减仓委托。  
\- 如果不修改价格，则调小size不会影响深度排队，调大size会排到当前价位最后。  
price | string | Optional |  | 新的委托价格。  
amend_text | string | Optional |  | 用户可以备注这次修改的信息。  
text | string | Optional |  | 内部用户可以在text修改信息。  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单详情 | FuturesOrder  
  
### 返回格式

状态码 **200**

合约订单详情

类型 | 约束  
---|---  
FuturesOrder | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
  
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
    
    url = '/futures/usdt/orders/12345'
    query_param = ''
    body='{"size":"100","price":"54321","contract":"BTC_USDT"}'
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
    url="/futures/usdt/orders/12345"
    query_param=""
    body_param='{"size":"100","price":"54321","contract":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "size": "100",
      "price": "54321",
      "contract": "BTC_USDT"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968.123456,
      "update_time": 1546569970.456789,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
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
      "finish_time": 1546569970.456789,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  撤销单个订单🔒 需要认证

DELETE`/futures/{settle}/orders/{order_id}`

DELETE `/futures/{settle}/orders/{order_id}`

_撤销单个订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
action_mode | 请求参数 | string | 否 | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
settle | URL | string | 是 | 永续合约结算货币  
order_id | URL | string | 是 | 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID(即 text field)。基于自定义id text字段：  
1\. 如果订单没有成交且已撤单，60 秒后无法使用 text 字段查询该订单的信息，继续使用该字段查询会返回 ORDER_NOT_FOUND 错误。  
2\. 如果订单已完全成交或部分成交，您可以无限期地使用 text 字段查询该订单信息。  
  
####  详细描述

**action_mode** : 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）

**order_id** : 成功创建订单时返回的订单 ID 或者用户创建时指定的自定义 ID(即 text field)。基于自定义id text字段：  
1\. 如果订单没有成交且已撤单，60 秒后无法使用 text 字段查询该订单的信息，继续使用该字段查询会返回 ORDER_NOT_FOUND 错误。  
2\. 如果订单已完全成交或部分成交，您可以无限期地使用 text 字段查询该订单信息。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 订单详情 | FuturesOrder  
  
### 返回格式

状态码 **200**

合约订单详情

类型 | 约束  
---|---  
FuturesOrder | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
  
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
    
    url = '/futures/usdt/orders/12345'
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
    url="/futures/usdt/orders/12345"
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
      "create_time": 1546569968.123456,
      "update_time": 1546569970.456789,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
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
      "finish_time": 1546569970.456789,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  查询个人成交记录🔒 需要认证

GET`/futures/{settle}/my_trades`

GET `/futures/{settle}/my_trades`

_查询个人成交记录_

默认只支持查询半年内的数据,如果需要查询更久的数据，请使用`GET /futures/{settle}/my_trades_timerange`

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
order | 请求参数 | integer(int64) | 否 | 委托ID，如果指定则返回该委托相关数据  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
last_id | 请求参数 | string | 否 | 以上个列表的最后一条记录的 ID 作为下个列表的起点。  
  
该字段不再继续支持，如果需要遍历查询更多记录，建议使用`GET /futures/{settle}/my_trades_timerange`  
  
####  详细描述

**last_id** : 以上个列表的最后一条记录的 ID 作为下个列表的起点。  
  
该字段不再继续支持，如果需要遍历查询更多记录，建议使用`GET /futures/{settle}/my_trades_timerange`

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [MyFuturesTrade]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
MyFuturesTrade |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 成交记录 ID  
create_time | number(double) | Optional |  | 成交时间  
contract | string | Optional |  | 合约标识  
order_id | string | Optional |  | 成交记录关联订单 ID  
size | string | Optional |  | 成交数量  
close_size | string | Optional |  | 平仓数量:  
  
close_size=0 && size＞0 开多  
close_size=0 && size＜0 开空  
close_size>0 && size>0 && size <= close_size 平空  
close_size>0 && size>0 && size > close_size 平空且开多  
close_size<0 && size<0 && size >= close_size 平多  
close_size<0 && size<0 && size < close_size 平多且开空  
price | string | Optional |  | 成交价格  
role | string | Optional | enum: ["taker","maker"] | 成交角色， taker - 吃单, maker - 做单  
text | string | Optional |  | 订单的自定义信息  
fee | string | Optional |  | 成交手续费  
point_fee | string | Optional |  | 成交点卡手续费  
trade_value | string | Optional |  | 成交价值  
  
###  返回头部

返回头部状态码 | 头部 | 类型 | 格式 | 描述  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | 分页时指定的 limit  
200 | X-Pagination-Offset | integer |  | 分页时指定的 offset  
  
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
    
    url = '/futures/usdt/my_trades'
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
    url="/futures/usdt/my_trades"
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
        "size": "100",
        "price": "100.123",
        "text": "t-123456",
        "fee": "0.01",
        "point_fee": "0",
        "role": "taker",
        "close_size": "0",
        "trade_value": "28601.83"
      }
    ]
    

##  查询个人成交记录(时间区间)🔒 需要认证

GET`/futures/{settle}/my_trades_timerange`

GET `/futures/{settle}/my_trades_timerange`

_查询个人成交记录(时间区间)_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
role | 请求参数 | string | 否 | 查询角色，Maker 或 Taker  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [MyFuturesTradeTimeRange]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
MyFuturesTradeTimeRange |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
trade_id | string | Optional |  | 成交记录 ID  
create_time | number(double) | Optional |  | 成交时间  
contract | string | Optional |  | 合约标识  
order_id | string | Optional |  | 成交记录关联订单 ID  
size | string | Optional |  | 成交数量  
close_size | string | Optional |  | 平仓数量:  
  
close_size=0 && size＞0 开多  
close_size=0 && size＜0 开空  
close_size>0 && size>0 && size <= close_size 平空  
close_size>0 && size>0 && size > close_size 平空且开多  
close_size<0 && size<0 && size >= close_size 平多  
close_size<0 && size<0 && size < close_size 平多且开空  
price | string | Optional |  | 成交价格  
role | string | Optional | enum: ["taker","maker"] | 成交角色， taker - 吃单, maker - 做单  
text | string | Optional |  | 订单的自定义信息  
fee | string | Optional |  | 成交手续费  
point_fee | string | Optional |  | 成交点卡手续费  
  
###  返回头部

返回头部状态码 | 头部 | 类型 | 格式 | 描述  
---|---|---|---|---  
200 | X-Pagination-Limit | integer |  | 分页时指定的 limit  
200 | X-Pagination-Offset | integer |  | 分页时指定的 offset  
  
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
    
    url = '/futures/usdt/my_trades_timerange'
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
    url="/futures/usdt/my_trades_timerange"
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
        "trade_id": "121234231",
        "create_time": 1514764800.123,
        "contract": "BTC_USDT",
        "order_id": "21893289839",
        "size": "100",
        "price": "100.123",
        "text": "t-123456",
        "fee": "0.01",
        "point_fee": "0",
        "role": "taker",
        "close_size": "0"
      }
    ]
    

##  查询平仓历史🔒 需要认证

GET`/futures/{settle}/position_close`

GET `/futures/{settle}/position_close`

_查询平仓历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
side | 请求参数 | string | 否 | 方向筛选，做多(long)或做空(short)  
pnl | 请求参数 | string | 否 | 盈亏判断，盈利(profit)或亏损(loss)  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [PositionClose]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
PositionClose |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | number(double) | Optional | readOnly: true | 平仓时间  
contract | string | Optional | readOnly: true | 合约标识  
side | string | Optional | enum: ["long","short"]  
readOnly: true | 多空方向  
  
\- `long`: 做多  
\- `short`: 做空  
pnl | string | Optional | readOnly: true | 盈亏  
pnl_pnl | string | Optional | readOnly: true | 盈亏-仓位盈亏  
pnl_fund | string | Optional | readOnly: true | 盈亏-资金费用  
pnl_fee | string | Optional | readOnly: true | 盈亏-手续费  
text | string | Optional | readOnly: true | 平仓委托的来源，具体取值参见`order.text`字段  
max_size | string | Optional | readOnly: true | 最大持仓量  
accum_size | string | Optional | readOnly: true | 累计平仓量  
first_open_time | integer(int64) | Optional | readOnly: true | 开仓时间  
long_price | string | Optional | readOnly: true | side为long时表示开仓均价，为short时表示平仓均价  
short_price | string | Optional | readOnly: true | side为long时表示平仓均价，为short时表示开仓均价  
  
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
    
    url = '/futures/usdt/position_close'
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
    url="/futures/usdt/position_close"
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

GET`/futures/{settle}/liquidates`

GET `/futures/{settle}/liquidates`

_查询强制平仓历史_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
at | 请求参数 | integer | 否 | 指定时间戳的强平历史  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FuturesLiquidate]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
FuturesLiquidate |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | 强制平仓时间  
contract | string | Optional | readOnly: true | 合约标识  
leverage | string | Optional | readOnly: true | 杠杆倍数，公共接口无该字段返回  
size | string | Optional | readOnly: true | 仓位大小  
margin | string | Optional | readOnly: true | 保证金，公共接口无该字段返回  
entry_price | string | Optional | readOnly: true | 平均开仓价，公共接口无该字段返回  
liq_price | string | Optional | readOnly: true | 强制平仓价，公共接口无该字段返回  
mark_price | string | Optional | readOnly: true | 市场标记价，公共接口无该字段返回  
order_id | integer(int64) | Optional | readOnly: true | 强平委托ID，公共接口无该字段返回  
order_price | string | Optional | readOnly: true | 强平委托价  
fill_price | string | Optional | readOnly: true | 强平委托吃单平均成交价  
left | string | Optional | readOnly: true | 强平委托挂单大小  
  
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
    
    url = '/futures/usdt/liquidates'
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
    url="/futures/usdt/liquidates"
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
        "size": "600",
        "leverage": "25",
        "margin": "0.006705256878",
        "entry_price": "3536.123",
        "liq_price": "3421.54",
        "mark_price": "3420.27",
        "order_id": 317393847,
        "order_price": "3405",
        "fill_price": "3424",
        "left": "0"
      }
    ]
    

##  查询ADL自动减仓订单信息🔒 需要认证

GET`/futures/{settle}/auto_deleverages`

GET `/futures/{settle}/auto_deleverages`

_查询ADL自动减仓订单信息_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
from | 请求参数 | integer(int64) | 否 | 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)  
to | 请求参数 | integer(int64) | 否 | 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳  
at | 请求参数 | integer | 否 | 指定时间戳的自动减仓订单信息  
  
####  详细描述

**from** : 起始时间戳  
  
指定起始时间，时间格式为Unix时间戳。不指定则默认为(to和limit实际返回的时间范围的数据起始时间)

**to** : 终止时间戳  
  
指定结束时间，不指定则默认为当前时间，时间格式为Unix时间戳

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FuturesAutoDeleverage]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
FuturesAutoDeleverage |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | 自动减仓时间  
user | integer(int64) | Optional | readOnly: true | 用户ID  
order_id | integer(int64) | Optional | readOnly: true | 减仓委托ID，2023-02-20之前的数据order_id为null  
contract | string | Optional | readOnly: true | 合约标识  
leverage | string | Optional | readOnly: true | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
cross_leverage_limit | string | Optional | readOnly: true | 全仓模式下的杠杆倍数  
entry_price | string | Optional | readOnly: true | 平均开仓价  
fill_price | string | Optional | readOnly: true | 平均成交价  
trade_size | string | Optional | readOnly: true | 成交数量  
position_size | string | Optional | readOnly: true | 自动减仓后的持仓量  
  
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
    
    url = '/futures/usdt/auto_deleverages'
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
    url="/futures/usdt/auto_deleverages"
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
        "time": 1675841679,
        "contract": "ACH_USDT",
        "order_id": 73873128,
        "user": 1666,
        "cross_leverage_limit": "0",
        "leverage": "0",
        "entry_price": "2649.648633636364",
        "fill_price": "2790.8082",
        "position_size": "1",
        "trade_size": "-10"
      }
    ]
    

##  倒计时取消订单🔒 需要认证

POST`/futures/{settle}/countdown_cancel_all`

POST `/futures/{settle}/countdown_cancel_all`

_倒计时取消订单_

合约订单心跳检测，在到达用户设置的`timeout`时间时如果没有取消既有倒计时或设置新的倒计时将会自动取消相关的`合约挂单`。 该接口可重复调用，以便设置新的倒计时或取消倒计时。 用法示例： 以30s的间隔重复此接口，每次倒计时`timeout`设置为30(秒)。 如果在30秒内未再次调用此接口，则您指定`market`上的所有挂单都会被自动撤销。 如果在30秒内以将`timeout`设置为0，则倒数计时器将终止，自动撤单功能取消。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CountdownCancelAllFuturesTask | 是 |   
timeout | body | integer(int32) | 是 | 倒计时时间，单位 秒  
至少5秒，为0时表示取消倒计时  
contract | body | string | 否 | 合约标识  
settle | URL | string | 是 | 永续合约结算货币  
  
####  详细描述

** timeout**: 倒计时时间，单位 秒  
至少5秒，为0时表示取消倒计时

####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

CountdownCancelAllFuturesTask

倒计时任务详情

请求体结构类型 | 约束  
---|---  
CountdownCancelAllFuturesTask | required: ["timeout","market"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
timeout | integer(int32) | Required |  | 倒计时时间，单位 秒  
至少5秒，为0时表示取消倒计时  
contract | string | Optional |  | 合约标识  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 设置倒计时成功 | TriggerTime  
  
### 返回格式

状态码 **200**

triggerTime

类型 | 约束  
---|---  
TriggerTime |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
triggerTime | integer(int64) | Optional |  | 倒计时结束时的时间戳，毫秒  
  
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
    
    url = '/futures/usdt/countdown_cancel_all'
    query_param = ''
    body='{"timeout":30,"contract":"BTC_USDT"}'
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
    url="/futures/usdt/countdown_cancel_all"
    query_param=""
    body_param='{"timeout":30,"contract":"BTC_USDT"}'
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
      "contract": "BTC_USDT"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "triggerTime": "1660039145000"
    }
    

##  查询合约市场交易费率🔒 需要认证

GET`/futures/{settle}/fee`

GET `/futures/{settle}/fee`

_查询合约市场交易费率_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | Inline  
  
### 返回格式

状态码 **200**

FuturesFee

类型 | 约束  
---|---  
object |   
  
**additionalProperties**

返回结果是map类型，key是市场，value是吃单挂单费率

类型 | 约束  
---|---  
FuturesFee |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
taker_fee | string | Optional | readOnly: true | 吃单费率  
maker_fee | string | Optional | readOnly: true | 挂单费率  
  
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
    
    url = '/futures/usdt/fee'
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
    url="/futures/usdt/fee"
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
      "1INCH_USDT": {
        "taker_fee": "0.00025",
        "maker_fee": "-0.00010"
      },
      "AAVE_USDT": {
        "taker_fee": "0.00025",
        "maker_fee": "-0.00010"
      }
    }
    

##  批量撤销指定 ID 的订单列表🔒 需要认证

POST`/futures/{settle}/batch_cancel_orders`

POST `/futures/{settle}/batch_cancel_orders`

_批量撤销指定 ID 的订单列表_

可以指定多个不同的订单id。一次请求最多只能撤销 20 条记录

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | CancelBatchFutureOrdersRequest | 是 |   
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

订单id数组

请求体结构类型 | 约束  
---|---  
CancelBatchFutureOrdersRequest |   
  
**items**

请求体结构类型 | 约束  
---|---  
string |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 撤单操作完成 | [Inline]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

FutureCancelOrderResult

订单撤销结果

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 订单id  
user_id | integer(int64) | Optional |  | 用户id  
succeeded | boolean | Optional |  | 是否撤销成功  
message | string | Optional |  | 撤销失败时的错误描述，成功时为空  
  
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
    
    url = '/futures/usdt/batch_cancel_orders'
    query_param = ''
    body='["1","2","3"]'
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
    url="/futures/usdt/batch_cancel_orders"
    query_param=""
    body_param='["1","2","3"]'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    [
      "1",
      "2",
      "3"
    ]
    

> 返回示例

> 200 返回
    
    
    [
      {
        "user_id": 111,
        "id": "123456",
        "succeeded": true,
        "message": ""
      }
    ]
    

##  批量修改指定 ID 的订单🔒 需要认证

POST`/futures/{settle}/batch_amend_orders`

POST `/futures/{settle}/batch_amend_orders`

_批量修改指定 ID 的订单_

可以指定多个不同的订单id。一次请求最多只能修改 10 个订单

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | array[BatchAmendOrderReq] | 是 |   
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

请求体结构类型 | 约束  
---|---  
array |   
  
**items**

修改合约订单参数

请求体结构类型 | 约束  
---|---  
BatchAmendOrderReq |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | 订单id，order_id和text至少传一个  
text | string | Optional |  | 用户自定义订单text，order_id和text至少传一个  
size | string | Optional |  | 新的委托大小。包括已成交委托的部分。  
\- 如果小于等于已成交数量，则撤销委托。  
\- 新的委托买卖方向必须跟原有的一致。  
\- 不能修改平仓单的size。  
\- 对于只减仓委托，如果调大size，则可能踢出其他只减仓委托。  
\- 如果不修改价格，则调小size不会影响深度排队，调大size会排到当前价位最后。  
price | string | Optional |  | 新的委托价格。  
amend_text | string | Optional |  | 用户可以备注这次修改的信息。  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求执行完成 | [BatchFuturesOrder]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约订单详情

类型 | 约束  
---|---  
BatchFuturesOrder |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
succeeded | boolean | Optional |  | 请求执行结果  
label | string | Optional |  | 错误标识，仅当执行失败时存在  
detail | string | Optional |  | 错误详情，仅当执行失败并需要给出详情时存在  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
contract | string | Optional |  | 合约标识  
size | string | Optional |  | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Optional |  | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 未成交数量  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
tkfr | string | Optional | readOnly: true | 吃单费率  
mkfr | string | Optional | readOnly: true | 做单费率  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
market_order_slip_ratio | string | Optional |  | 最大滑点比率  
  
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
    
    url = '/futures/usdt/batch_amend_orders'
    query_param = ''
    body='[{"order_id":121212,"amend_text":"batch amend text","size":"100","price":"54321"}]'
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
    url="/futures/usdt/batch_amend_orders"
    query_param=""
    body_param='[{"order_id":121212,"amend_text":"batch amend text","size":"100","price":"54321"}]'
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
        "order_id": 121212,
        "amend_text": "batch amend text",
        "size": "100",
        "price": "54321"
      }
    ]
    

> 返回示例

> 200 返回
    
    
    [
      {
        "succeeded": true,
        "id": 15675394,
        "user": 100000,
        "contract": "BTC_USDT",
        "create_time": 1546569968.123456,
        "update_time": 1546569970.456789,
        "size": "6024",
        "iceberg": "0",
        "left": "6024",
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
        "finish_time": 1546569970.456789,
        "finish_as": "cancelled",
        "stp_id": 0,
        "stp_act": "-",
        "amend_text": "-",
        "market_order_slip_ratio": "0.03"
      }
    ]
    

##  根据table_id查询风险限额梯度表

GET`/futures/{settle}/risk_limit_table`

GET `/futures/{settle}/risk_limit_table`

_根据table_id查询风险限额梯度表_

只需要传入table_id即可

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
table_id | 请求参数 | string | 是 | 梯度风险限额表id  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [FuturesRiskLimitTier]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

梯度风险限额的每个档位信息

类型 | 约束  
---|---  
FuturesRiskLimitTier |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tier | integer(int) | Optional |  | 档位  
risk_limit | string | Optional |  | 风险限额  
initial_rate | string | Optional |  | 初始保证金率  
maintenance_rate | string | Optional |  | 风险限额的第一档维持保证金率要求  
leverage_max | string | Optional |  | 最大杠杆  
deduction | string | Optional |  | 维持保证金速算扣减额  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/futures/usdt/risk_limit_table'
    query_param = 'table_id=CYBER_USDT_20241122'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/futures/usdt/risk_limit_table?table_id=CYBER_USDT_20241122 \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "tier": 1,
        "risk_limit": "10000",
        "initial_rate": "0.025",
        "maintenance_rate": "0.015",
        "leverage_max": "40",
        "deduction": "0"
      },
      {
        "tier": 2,
        "risk_limit": "30000",
        "initial_rate": "0.03333",
        "maintenance_rate": "0.02",
        "leverage_max": "30",
        "deduction": "50"
      },
      {
        "tier": 3,
        "risk_limit": "50000",
        "initial_rate": "0.04545",
        "maintenance_rate": "0.03",
        "leverage_max": "22",
        "deduction": "350"
      },
      {
        "tier": 4,
        "risk_limit": "70000",
        "initial_rate": "0.05555",
        "maintenance_rate": "0.04",
        "leverage_max": "18",
        "deduction": "850"
      },
      {
        "tier": 5,
        "risk_limit": "100000",
        "initial_rate": "0.1",
        "maintenance_rate": "0.085",
        "leverage_max": "10",
        "deduction": "4000"
      },
      {
        "tier": 6,
        "risk_limit": "150000",
        "initial_rate": "0.333",
        "maintenance_rate": "0.3",
        "leverage_max": "3",
        "deduction": "25500"
      },
      {
        "tier": 7,
        "risk_limit": "200000",
        "initial_rate": "0.5",
        "maintenance_rate": "0.45",
        "leverage_max": "2",
        "deduction": "48000"
      },
      {
        "tier": 8,
        "risk_limit": "300000",
        "initial_rate": "1",
        "maintenance_rate": "0.95",
        "leverage_max": "1",
        "deduction": "148000"
      }
    ]
    

##  档位bbo合约下单🔒 需要认证

POST`/futures/{settle}/bbo_orders`

POST `/futures/{settle}/bbo_orders`

_档位bbo合约下单_

对比合约交易下单接口（futures/{settle}/orders），添加了`level`和`direction`参数。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
x-gate-exptime | 请求头部 | string | 否 | 指定过期时间(毫秒); 如果 Gate 收到请求的时间大于过期时间, 请求将被拒绝  
body | body | FuturesBBOOrder | 是 |   
contract | body | string | 是 | 合约标识  
size | body | integer(int64) | 是 | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
  
direction | body | string | 是 | 方向，sell取买盘，buy取卖盘。  
iceberg | body | integer(int64) | 否 | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
  
level | body | integer(int64) | 是 | 档位，最大20档  
close | body | boolean | 否 | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | body | boolean | 否 | 是否为平仓委托。对应请求中的`close`。  
reduce_only | body | boolean | 否 | 设置为 true 的时候，为只减仓委托  
is_reduce_only | body | boolean | 否 | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | body | boolean | 否 | 是否为强制平仓委托  
tif | body | string | 否 | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
  
left | body | integer(int64) | 否 | 未成交数量  
fill_price | body | string | 否 | 成交价  
text | body | string | 否 | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
  
tkfr | body | string | 否 | 吃单费率  
mkfr | body | string | 否 | 做单费率  
refu | body | integer | 否 | 推荐人用户 ID  
auto_size | body | string | 否 | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | body | integer | 否 | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
  
stp_act | body | string | 否 | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
  
amend_text | body | string | 否 | 用户修改订单时备注的信息  
pid | body | integer(int64) | 否 | 仓位ID  
settle | URL | string | 是 | 永续合约结算货币  
  
####  详细描述

** size**: 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  

** iceberg**: 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  

** tif**: Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  

** text**: 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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

** stp_id**: 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  

** stp_act**: Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
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
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

合约BBO订单详情

请求体结构类型 | 约束  
---|---  
FuturesBBOOrder | required: ["contract","size","level","direction"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约标识  
size | integer(int64) | Required |  | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
direction | string | Required |  | 方向，sell取买盘，buy取卖盘。  
iceberg | integer(int64) | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
level | integer(int64) | Required | writeOnly: true | 档位，最大20档  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | integer(int64) | Optional | readOnly: true | 未成交数量  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
tkfr | string | Optional | readOnly: true | 吃单费率  
mkfr | string | Optional | readOnly: true | 做单费率  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 订单详情 | FuturesOrder  
  
### 返回格式

状态码 **201**

合约订单详情

类型 | 约束  
---|---  
FuturesOrder | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
  
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
    
    url = '/futures/usdt/bbo_orders'
    query_param = ''
    body='{"contract":"PI_USDT","level":8,"direction":"sell","size":1}'
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
    url="/futures/usdt/bbo_orders"
    query_param=""
    body_param='{"contract":"PI_USDT","level":8,"direction":"sell","size":1}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "contract": "PI_USDT",
      "level": 8,
      "direction": "sell",
      "size": 1
    }
    

> 返回示例

> 201 返回
    
    
    {
      "id": 15675394,
      "user": 100000,
      "contract": "BTC_USDT",
      "create_time": 1546569968.123456,
      "update_time": 1546569970.456789,
      "size": "6024",
      "iceberg": "0",
      "left": "6024",
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
      "finish_time": 1546569970.456789,
      "finish_as": "cancelled",
      "stp_id": 0,
      "stp_act": "-",
      "amend_text": "-",
      "order_value": "64112.2099000000005",
      "trade_value": "64112.2099000000005",
      "market_order_slip_ratio": "0.03",
      "pos_margin_mode": "isolated",
      "tpsl_tp_trigger_price": "3800",
      "tpsl_sl_trigger_price": "3700"
    }
    

##  创建追踪委托🔒 需要认证

POST`/futures/{settle}/autoorder/v1/trail/create`

POST `/futures/{settle}/autoorder/v1/trail/create`

_创建追踪委托_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CreateTrailOrder | 是 |   
contract | body | string | 是 | 合约名称  
amount | body | string | 是 | 交易数量，单位是张，正数表示买，负数表示卖  
activation_price | body | string | 否 | 激活价格，为0表示立即触发  
is_gte | body | boolean | 否 | true：市场价大于等于激活价时激活，false：小于等于  
price_type | body | integer(int32) | 是 | 激活价格的类型，必填，1-最新价格，2-指数价格，3-标记价格；调用方须显式指定  
price_offset | body | string | 否 | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
reduce_only | body | boolean | 否 | 是否只减仓  
position_related | body | boolean | 否 | 是否和仓位绑定(如果 position_related = true（关联仓位），那么 reduce_only 必须也是 true)  
text | body | string | 否 | 订单自定义信息，可选字段。用于标识订单来源或设置用户自定义 ID。  
  
**如果非空** ，必须满足以下规则之一：  
  
**1\. 内部保留字段（标识订单来源）** ：  
\- `apiv4`: API 调用  
**2\. 用户自定义字段（设置自定义 ID）** ：  
\- 必须以 `t-` 开头  
\- `t-` 后面的内容长度不能超过 28 字节  
\- 只能包含：数字、字母、下划线(_)、中划线(-) 或者点(.)  
\- 示例：`t-my-order-001`、`t-trail_2024.01`  
  
**注意** ：用户自定义字段不能与内部保留字段冲突。  
pos_margin_mode | body | string | 否 | 仓位保证金模式 逐仓isolated/全仓cross  
position_mode | body | string | 否 | 持仓模式 single、dual和dual_plus  
settle | URL | string | 是 | 永续合约结算货币  
  
####  详细描述

** text**: 订单自定义信息，可选字段。用于标识订单来源或设置用户自定义 ID。  
  
**如果非空** ，必须满足以下规则之一：  
  
**1\. 内部保留字段（标识订单来源）** ：  
\- `apiv4`: API 调用  
**2\. 用户自定义字段（设置自定义 ID）** ：  
\- 必须以 `t-` 开头  
\- `t-` 后面的内容长度不能超过 28 字节  
\- 只能包含：数字、字母、下划线(_)、中划线(-) 或者点(.)  
\- 示例：`t-my-order-001`、`t-trail_2024.01`  
  
**注意** ：用户自定义字段不能与内部保留字段冲突。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
price_type | 1  
price_type | 2  
price_type | 3  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

CreateTrailOrder

请求体结构类型 | 约束  
---|---  
CreateTrailOrder | required: ["contract","amount","price_type"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约名称  
amount | string | Required |  | 交易数量，单位是张，正数表示买，负数表示卖  
activation_price | string | Optional | default: "0" | 激活价格，为0表示立即触发  
is_gte | boolean | Optional |  | true：市场价大于等于激活价时激活，false：小于等于  
price_type | integer(int32) | Required | enum: [1,2,3] | 激活价格的类型，必填，1-最新价格，2-指数价格，3-标记价格；调用方须显式指定  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
reduce_only | boolean | Optional | default: false | 是否只减仓  
position_related | boolean | Optional | default: false | 是否和仓位绑定(如果 position_related = true（关联仓位），那么 reduce_only 必须也是 true)  
text | string | Optional | default: "apiv4" | 订单自定义信息，可选字段。用于标识订单来源或设置用户自定义 ID。  
  
**如果非空** ，必须满足以下规则之一：  
  
**1\. 内部保留字段（标识订单来源）** ：  
\- `apiv4`: API 调用  
**2\. 用户自定义字段（设置自定义 ID）** ：  
\- 必须以 `t-` 开头  
\- `t-` 后面的内容长度不能超过 28 字节  
\- 只能包含：数字、字母、下划线(_)、中划线(-) 或者点(.)  
\- 示例：`t-my-order-001`、`t-trail_2024.01`  
  
**注意** ：用户自定义字段不能与内部保留字段冲突。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 逐仓isolated/全仓cross  
position_mode | string | Optional |  | 持仓模式 single、dual和dual_plus  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 创建成功 | CreateTrailOrderResponse  
  
### 返回格式

状态码 **201**

CreateTrailOrderResponse

类型 | 约束  
---|---  
CreateTrailOrderResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

CreateTrailOrderResult

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托ID  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/create'
    query_param = ''
    body='{"contract":"BTC_USDT","amount":"10","activation_price":"50000","is_gte":true,"price_type":1,"price_offset":"0.1%","reduce_only":false,"text":"apiv4"}'
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
    url="/futures/usdt/autoorder/v1/trail/create"
    query_param=""
    body_param='{"contract":"BTC_USDT","amount":"10","activation_price":"50000","is_gte":true,"price_type":1,"price_offset":"0.1%","reduce_only":false,"text":"apiv4"}'
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
      "amount": "10",
      "activation_price": "50000",
      "is_gte": true,
      "price_type": 1,
      "price_offset": "0.1%",
      "reduce_only": false,
      "text": "apiv4"
    }
    

> 返回示例

> 201 返回
    
    
    {
      "code": 0,
      "message": "ok",
      "data": {
        "id": "63648"
      },
      "timestamp": 1769583885680
    }
    

##  终止追踪委托🔒 需要认证

POST`/futures/{settle}/autoorder/v1/trail/stop`

POST `/futures/{settle}/autoorder/v1/trail/stop`

_终止追踪委托_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | StopTrailOrder | 是 |   
id | body | integer(int64) | 否 | 委托ID，指定了id就不需要text  
text | body | string | 否 | 自定义文本，如果不指定id，就根据user_id和text终止  
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

StopTrailOrder

请求体结构类型 | 约束  
---|---  
StopTrailOrder |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID，指定了id就不需要text  
text | string | Optional |  | 自定义文本，如果不指定id，就根据user_id和text终止  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 终止成功 | TrailOrderDetailResponse  
  
### 返回格式

状态码 **200**

TrailOrderDetailResponse

类型 | 约束  
---|---  
TrailOrderDetailResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

TrailOrderResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order | object | Optional |  | 追踪委托详情  
  
**data / order**

TrailOrder

追踪委托详情

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 委托ID  
user_id | string | Optional | readOnly: true | 用户ID  
user | string | Optional | readOnly: true | 用户ID  
contract | string | Optional |  | 合约名称  
settle | string | Optional |  | 结算货币  
amount | string | Optional |  | 交易数量，单位是张，正数买，负数卖  
is_gte | boolean | Optional |  | true：市场价大于等于激活价时激活，false：小于等于  
activation_price | string | Optional |  | 激活价格，为0表示立即触发  
price_type | integer(int32) | Optional | enum: [0,1,2,3] | 激活价格的类型，0-未知，1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
text | string | Optional |  | 自定义字段  
reduce_only | boolean | Optional |  | 只减仓  
position_related | boolean | Optional |  | 是否和仓位绑定  
created_at | string | Optional | readOnly: true | 创建时间  
activated_at | string | Optional | readOnly: true | 激活时间  
finished_at | string | Optional | readOnly: true | 结束时间  
create_time | string | Optional | readOnly: true | 创建时间  
active_time | string | Optional | readOnly: true | 激活时间  
finish_time | string | Optional | readOnly: true | 结束时间  
reason | string | Optional | readOnly: true | 结束原因  
suborder_text | string | Optional | readOnly: true | 子订单的 text 字段。  
is_dual_mode | boolean | Optional | readOnly: true | 创建委托时是否双向持仓  
trigger_price | string | Optional | readOnly: true | 触发价  
suborder_id | string | Optional | readOnly: true | 子订单 ID。  
side_label | string | Optional | readOnly: true | 订单方向标签，做多/做空/开多/开空/平多/平空  
original_status | integer(int32) | Optional | readOnly: true | 委托状态  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 简化后的委托状态：open/finished  
position_side_output | string | Optional | readOnly: true | 同 side_label，客户端要求和其他类型订单保持一致  
updated_at | string | Optional | readOnly: true | 更新时间  
extremum_price | string | Optional | readOnly: true | 极值价格  
status_code | string | Optional | readOnly: true | status状态值  
created_at_precise | string | Optional | readOnly: true | 创建时间（高精度，秒.微秒格式）  
finished_at_precise | string | Optional | readOnly: true | 结束时间（高精度，秒.微秒格式）  
activated_at_precise | string | Optional | readOnly: true | 激活时间（高精度，秒.微秒格式）  
status_label | string | Optional | readOnly: true | 状态国际化标签（翻译后的状态文本）  
pos_margin_mode | string | Optional | readOnly: true | 仓位保证金模式 逐仓isolated/全仓cross  
position_mode | string | Optional | readOnly: true | 持仓模式 single、dual和dual_plus  
error_label | string | Optional | readOnly: true | 错误标签  
leverage | string | Optional | readOnly: true | 杠杆  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/stop'
    query_param = ''
    body='{"id":123456789}'
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
    url="/futures/usdt/autoorder/v1/trail/stop"
    query_param=""
    body_param='{"id":123456789}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "id": 123456789
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "ok",
      "data": {
        "order": {
          "id": "63585",
          "user_id": "2124438083",
          "contract": "BTC_USDT",
          "settle": "usdt",
          "amount": "10",
          "is_gte": false,
          "activation_price": "0",
          "price_type": 1,
          "price_offset": "5%",
          "text": "apiv4",
          "reduce_only": false,
          "position_related": false,
          "created_at": "1769569837",
          "activated_at": "1769569837",
          "finished_at": "1769584936",
          "reason": "",
          "suborder_text": "apiv4-auto-trail-o-1d29",
          "is_dual_mode": false,
          "trigger_price": "91047.4",
          "suborder_id": "94294117233225616",
          "side_label": "买入",
          "original_status": 5,
          "status": "finished",
          "user": "2124438083",
          "create_time": "1769569837",
          "active_time": "1769569837",
          "finish_time": "1769584936",
          "position_side_output": "买入",
          "updated_at": "1769584936",
          "extremum_price": "86711.9",
          "status_code": "cancelled",
          "created_at_precise": "1769569837778000",
          "finished_at_precise": "1769584936814000",
          "activated_at_precise": "1769569837976010",
          "status_label": "Canceled",
          "pos_margin_mode": "",
          "position_mode": "single",
          "error_label": "",
          "leverage": ""
        }
      },
      "timestamp": 1769584936814
    }
    

##  批量终止追踪委托🔒 需要认证

POST`/futures/{settle}/autoorder/v1/trail/stop_all`

POST `/futures/{settle}/autoorder/v1/trail/stop_all`

_批量终止追踪委托_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | StopAllTrailOrders | 是 |   
contract | body | string | 否 | 合约名称  
related_position | body | integer(int32) | 否 | 关联仓位，如果传了就只撤和这个仓位关联的委托，1-多仓，2-空仓  
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
related_position | 1  
related_position | 2  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

StopAllTrailOrders

请求体结构类型 | 约束  
---|---  
StopAllTrailOrders |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional |  | 合约名称  
related_position | integer(int32) | Optional | enum: [1,2] | 关联仓位，如果传了就只撤和这个仓位关联的委托，1-多仓，2-空仓  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 终止成功 | Inline  
  
### 返回格式

状态码 **200**

TrailOrderListResponseEnvelope

跟踪委托列表响应，订单列表位于 data.orders。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

TrailOrderListResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
orders | array | Optional |  |   
  
**data / orders**

类型 | 约束  
---|---  
array |   
  
**data / orders / items**

TrailOrder

追踪委托详情

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 委托ID  
user_id | string | Optional | readOnly: true | 用户ID  
user | string | Optional | readOnly: true | 用户ID  
contract | string | Optional |  | 合约名称  
settle | string | Optional |  | 结算货币  
amount | string | Optional |  | 交易数量，单位是张，正数买，负数卖  
is_gte | boolean | Optional |  | true：市场价大于等于激活价时激活，false：小于等于  
activation_price | string | Optional |  | 激活价格，为0表示立即触发  
price_type | integer(int32) | Optional | enum: [0,1,2,3] | 激活价格的类型，0-未知，1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
text | string | Optional |  | 自定义字段  
reduce_only | boolean | Optional |  | 只减仓  
position_related | boolean | Optional |  | 是否和仓位绑定  
created_at | string | Optional | readOnly: true | 创建时间  
activated_at | string | Optional | readOnly: true | 激活时间  
finished_at | string | Optional | readOnly: true | 结束时间  
create_time | string | Optional | readOnly: true | 创建时间  
active_time | string | Optional | readOnly: true | 激活时间  
finish_time | string | Optional | readOnly: true | 结束时间  
reason | string | Optional | readOnly: true | 结束原因  
suborder_text | string | Optional | readOnly: true | 子订单的 text 字段。  
is_dual_mode | boolean | Optional | readOnly: true | 创建委托时是否双向持仓  
trigger_price | string | Optional | readOnly: true | 触发价  
suborder_id | string | Optional | readOnly: true | 子订单 ID。  
side_label | string | Optional | readOnly: true | 订单方向标签，做多/做空/开多/开空/平多/平空  
original_status | integer(int32) | Optional | readOnly: true | 委托状态  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 简化后的委托状态：open/finished  
position_side_output | string | Optional | readOnly: true | 同 side_label，客户端要求和其他类型订单保持一致  
updated_at | string | Optional | readOnly: true | 更新时间  
extremum_price | string | Optional | readOnly: true | 极值价格  
status_code | string | Optional | readOnly: true | status状态值  
created_at_precise | string | Optional | readOnly: true | 创建时间（高精度，秒.微秒格式）  
finished_at_precise | string | Optional | readOnly: true | 结束时间（高精度，秒.微秒格式）  
activated_at_precise | string | Optional | readOnly: true | 激活时间（高精度，秒.微秒格式）  
status_label | string | Optional | readOnly: true | 状态国际化标签（翻译后的状态文本）  
pos_margin_mode | string | Optional | readOnly: true | 仓位保证金模式 逐仓isolated/全仓cross  
position_mode | string | Optional | readOnly: true | 持仓模式 single、dual和dual_plus  
error_label | string | Optional | readOnly: true | 错误标签  
leverage | string | Optional | readOnly: true | 杠杆  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/stop_all'
    query_param = ''
    body='{"contract":"BTC_USDT"}'
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
    url="/futures/usdt/autoorder/v1/trail/stop_all"
    query_param=""
    body_param='{"contract":"BTC_USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "contract": "BTC_USDT"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "ok",
      "data": {
        "orders": [
          {
            "id": "70948",
            "contract": "BTC_USDT",
            "settle": "usdt",
            "amount": "0.01",
            "activation_price": "7711",
            "is_gte": false,
            "price_type": 1,
            "price_offset": "1%",
            "status": "finished",
            "status_code": "cancelled",
            "created_at": "1793671122",
            "finished_at": "1793671123",
            "updated_at": "1793671123"
          }
        ]
      },
      "timestamp": 1793671123827
    }
    

##  获取追踪委托列表🔒 需要认证

GET`/futures/{settle}/autoorder/v1/trail/list`

GET `/futures/{settle}/autoorder/v1/trail/list`

_获取追踪委托列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 合约名称  
is_finished | 请求参数 | boolean | 否 | 是否历史委托  
start_at | 请求参数 | integer(int64) | 否 | 时间范围的开始时间  
end_at | 请求参数 | integer(int64) | 否 | 时间范围的结束时间  
page_num | 请求参数 | integer(int32) | 否 | 页号，从1开始  
page_size | 请求参数 | integer(int32) | 否 | 一页的数量  
sort_by | 请求参数 | integer(int32) | 否 | 通用排序字段，1-创建时间，2-结束时间  
hide_cancel | 请求参数 | boolean | 否 | 隐藏取消的委托  
related_position | 请求参数 | integer(int32) | 否 | 关联仓位，如果传了就只返回和这个仓位关联的委托，1-多仓，2-空仓  
sort_by_trigger | 请求参数 | boolean | 否 | 根据触发价格和激活价格排序，易触发或易激活靠前，仅限关联仓位的当前委托  
reduce_only | 请求参数 | integer(int32) | 否 | 是否只减仓，1-是，2-否  
side | 请求参数 | integer(int32) | 否 | 方向，1-多仓，2-空仓  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
sort_by | 1  
sort_by | 2  
related_position | 1  
related_position | 2  
reduce_only | 1  
reduce_only | 2  
side | 1  
side | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | Inline  
  
### 返回格式

状态码 **200**

TrailOrderListResponseEnvelope

跟踪委托列表响应，订单列表位于 data.orders。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

TrailOrderListResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
orders | array | Optional |  |   
  
**data / orders**

类型 | 约束  
---|---  
array |   
  
**data / orders / items**

TrailOrder

追踪委托详情

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 委托ID  
user_id | string | Optional | readOnly: true | 用户ID  
user | string | Optional | readOnly: true | 用户ID  
contract | string | Optional |  | 合约名称  
settle | string | Optional |  | 结算货币  
amount | string | Optional |  | 交易数量，单位是张，正数买，负数卖  
is_gte | boolean | Optional |  | true：市场价大于等于激活价时激活，false：小于等于  
activation_price | string | Optional |  | 激活价格，为0表示立即触发  
price_type | integer(int32) | Optional | enum: [0,1,2,3] | 激活价格的类型，0-未知，1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
text | string | Optional |  | 自定义字段  
reduce_only | boolean | Optional |  | 只减仓  
position_related | boolean | Optional |  | 是否和仓位绑定  
created_at | string | Optional | readOnly: true | 创建时间  
activated_at | string | Optional | readOnly: true | 激活时间  
finished_at | string | Optional | readOnly: true | 结束时间  
create_time | string | Optional | readOnly: true | 创建时间  
active_time | string | Optional | readOnly: true | 激活时间  
finish_time | string | Optional | readOnly: true | 结束时间  
reason | string | Optional | readOnly: true | 结束原因  
suborder_text | string | Optional | readOnly: true | 子订单的 text 字段。  
is_dual_mode | boolean | Optional | readOnly: true | 创建委托时是否双向持仓  
trigger_price | string | Optional | readOnly: true | 触发价  
suborder_id | string | Optional | readOnly: true | 子订单 ID。  
side_label | string | Optional | readOnly: true | 订单方向标签，做多/做空/开多/开空/平多/平空  
original_status | integer(int32) | Optional | readOnly: true | 委托状态  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 简化后的委托状态：open/finished  
position_side_output | string | Optional | readOnly: true | 同 side_label，客户端要求和其他类型订单保持一致  
updated_at | string | Optional | readOnly: true | 更新时间  
extremum_price | string | Optional | readOnly: true | 极值价格  
status_code | string | Optional | readOnly: true | status状态值  
created_at_precise | string | Optional | readOnly: true | 创建时间（高精度，秒.微秒格式）  
finished_at_precise | string | Optional | readOnly: true | 结束时间（高精度，秒.微秒格式）  
activated_at_precise | string | Optional | readOnly: true | 激活时间（高精度，秒.微秒格式）  
status_label | string | Optional | readOnly: true | 状态国际化标签（翻译后的状态文本）  
pos_margin_mode | string | Optional | readOnly: true | 仓位保证金模式 逐仓isolated/全仓cross  
position_mode | string | Optional | readOnly: true | 持仓模式 single、dual和dual_plus  
error_label | string | Optional | readOnly: true | 错误标签  
leverage | string | Optional | readOnly: true | 杠杆  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/list'
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
    url="/futures/usdt/autoorder/v1/trail/list"
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
      "code": 0,
      "message": "ok",
      "data": {
        "orders": [
          {
            "id": "9007199254740993",
            "contract": "BTC_USDT",
            "settle": "usdt",
            "amount": "1",
            "activation_price": "100000",
            "price_offset": "1%",
            "status": "open"
          }
        ]
      },
      "timestamp": 1793582374966
    }
    

##  获取追踪委托详情🔒 需要认证

GET`/futures/{settle}/autoorder/v1/trail/detail`

GET `/futures/{settle}/autoorder/v1/trail/detail`

_获取追踪委托详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
id | 请求参数 | integer(int64) | 是 | 委托ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | TrailOrderDetailResponse  
  
### 返回格式

状态码 **200**

TrailOrderDetailResponse

类型 | 约束  
---|---  
TrailOrderDetailResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

TrailOrderResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order | object | Optional |  | 追踪委托详情  
  
**data / order**

TrailOrder

追踪委托详情

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 委托ID  
user_id | string | Optional | readOnly: true | 用户ID  
user | string | Optional | readOnly: true | 用户ID  
contract | string | Optional |  | 合约名称  
settle | string | Optional |  | 结算货币  
amount | string | Optional |  | 交易数量，单位是张，正数买，负数卖  
is_gte | boolean | Optional |  | true：市场价大于等于激活价时激活，false：小于等于  
activation_price | string | Optional |  | 激活价格，为0表示立即触发  
price_type | integer(int32) | Optional | enum: [0,1,2,3] | 激活价格的类型，0-未知，1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
text | string | Optional |  | 自定义字段  
reduce_only | boolean | Optional |  | 只减仓  
position_related | boolean | Optional |  | 是否和仓位绑定  
created_at | string | Optional | readOnly: true | 创建时间  
activated_at | string | Optional | readOnly: true | 激活时间  
finished_at | string | Optional | readOnly: true | 结束时间  
create_time | string | Optional | readOnly: true | 创建时间  
active_time | string | Optional | readOnly: true | 激活时间  
finish_time | string | Optional | readOnly: true | 结束时间  
reason | string | Optional | readOnly: true | 结束原因  
suborder_text | string | Optional | readOnly: true | 子订单的 text 字段。  
is_dual_mode | boolean | Optional | readOnly: true | 创建委托时是否双向持仓  
trigger_price | string | Optional | readOnly: true | 触发价  
suborder_id | string | Optional | readOnly: true | 子订单 ID。  
side_label | string | Optional | readOnly: true | 订单方向标签，做多/做空/开多/开空/平多/平空  
original_status | integer(int32) | Optional | readOnly: true | 委托状态  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 简化后的委托状态：open/finished  
position_side_output | string | Optional | readOnly: true | 同 side_label，客户端要求和其他类型订单保持一致  
updated_at | string | Optional | readOnly: true | 更新时间  
extremum_price | string | Optional | readOnly: true | 极值价格  
status_code | string | Optional | readOnly: true | status状态值  
created_at_precise | string | Optional | readOnly: true | 创建时间（高精度，秒.微秒格式）  
finished_at_precise | string | Optional | readOnly: true | 结束时间（高精度，秒.微秒格式）  
activated_at_precise | string | Optional | readOnly: true | 激活时间（高精度，秒.微秒格式）  
status_label | string | Optional | readOnly: true | 状态国际化标签（翻译后的状态文本）  
pos_margin_mode | string | Optional | readOnly: true | 仓位保证金模式 逐仓isolated/全仓cross  
position_mode | string | Optional | readOnly: true | 持仓模式 single、dual和dual_plus  
error_label | string | Optional | readOnly: true | 错误标签  
leverage | string | Optional | readOnly: true | 杠杆  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/detail'
    query_param = 'id=0'
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
    url="/futures/usdt/autoorder/v1/trail/detail"
    query_param="id=0"
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
      "code": 0,
      "message": "ok",
      "data": {
        "order": {
          "id": "63585",
          "user_id": "2124438083",
          "contract": "BTC_USDT",
          "settle": "usdt",
          "amount": "10",
          "is_gte": false,
          "activation_price": "0",
          "price_type": 1,
          "price_offset": "5%",
          "text": "apiv4",
          "reduce_only": false,
          "position_related": false,
          "created_at": "1769569837",
          "activated_at": "1769569837",
          "finished_at": "1769578529",
          "reason": "",
          "suborder_text": "apiv4-auto-trail-o-1d29",
          "is_dual_mode": false,
          "trigger_price": "91047.4",
          "suborder_id": "94294117233225616",
          "side_label": "买入",
          "original_status": 4,
          "status": "finished",
          "user": "2124438083",
          "create_time": "1769569837",
          "active_time": "1769569837",
          "finish_time": "1769578529",
          "position_side_output": "买入",
          "updated_at": "1769578529",
          "extremum_price": "86711.9",
          "status_code": "success",
          "created_at_precise": "1769569837778000",
          "finished_at_precise": "1769578529853294",
          "activated_at_precise": "1769569837976010",
          "status_label": "已完成",
          "pos_margin_mode": "",
          "position_mode": "single",
          "error_label": "",
          "leverage": ""
        }
      },
      "timestamp": 1769584936814
    }
    

##  修改追踪委托🔒 需要认证

POST`/futures/{settle}/autoorder/v1/trail/update`

POST `/futures/{settle}/autoorder/v1/trail/update`

_修改追踪委托_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | UpdateTrailOrder | 是 |   
id | body | integer(int64) | 是 | 委托ID  
amount | body | string | 否 | 交易总数，单位是张，正数表示买，负数表示卖，0表示不修改  
activation_price | body | string | 否 | 激活价格，为0表示立即触发，空表示不修改  
is_gte_str | body | string | 否 | true：市场价大于等于激活价时激活，false：小于等于，空表示不修改  
price_type | body | integer(int32) | 否 | 激活价格的类型，不传或者0表示不修改，1-最新价格，2-指数价格，3-标记价格  
price_offset | body | string | 否 | 回调比例或者价距，比如 `0.1` 或者 `0.1%`，空表示不修改  
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
price_type | 3  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

UpdateTrailOrder

请求体结构类型 | 约束  
---|---  
UpdateTrailOrder | required: ["id"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Required |  | 委托ID  
amount | string | Optional |  | 交易总数，单位是张，正数表示买，负数表示卖，0表示不修改  
activation_price | string | Optional |  | 激活价格，为0表示立即触发，空表示不修改  
is_gte_str | string | Optional |  | true：市场价大于等于激活价时激活，false：小于等于，空表示不修改  
price_type | integer(int32) | Optional | enum: [0,1,2,3] | 激活价格的类型，不传或者0表示不修改，1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`，空表示不修改  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 修改成功 | TrailOrderDetailResponse  
  
### 返回格式

状态码 **200**

TrailOrderDetailResponse

类型 | 约束  
---|---  
TrailOrderDetailResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

TrailOrderResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order | object | Optional |  | 追踪委托详情  
  
**data / order**

TrailOrder

追踪委托详情

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 委托ID  
user_id | string | Optional | readOnly: true | 用户ID  
user | string | Optional | readOnly: true | 用户ID  
contract | string | Optional |  | 合约名称  
settle | string | Optional |  | 结算货币  
amount | string | Optional |  | 交易数量，单位是张，正数买，负数卖  
is_gte | boolean | Optional |  | true：市场价大于等于激活价时激活，false：小于等于  
activation_price | string | Optional |  | 激活价格，为0表示立即触发  
price_type | integer(int32) | Optional | enum: [0,1,2,3] | 激活价格的类型，0-未知，1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
text | string | Optional |  | 自定义字段  
reduce_only | boolean | Optional |  | 只减仓  
position_related | boolean | Optional |  | 是否和仓位绑定  
created_at | string | Optional | readOnly: true | 创建时间  
activated_at | string | Optional | readOnly: true | 激活时间  
finished_at | string | Optional | readOnly: true | 结束时间  
create_time | string | Optional | readOnly: true | 创建时间  
active_time | string | Optional | readOnly: true | 激活时间  
finish_time | string | Optional | readOnly: true | 结束时间  
reason | string | Optional | readOnly: true | 结束原因  
suborder_text | string | Optional | readOnly: true | 子订单的 text 字段。  
is_dual_mode | boolean | Optional | readOnly: true | 创建委托时是否双向持仓  
trigger_price | string | Optional | readOnly: true | 触发价  
suborder_id | string | Optional | readOnly: true | 子订单 ID。  
side_label | string | Optional | readOnly: true | 订单方向标签，做多/做空/开多/开空/平多/平空  
original_status | integer(int32) | Optional | readOnly: true | 委托状态  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 简化后的委托状态：open/finished  
position_side_output | string | Optional | readOnly: true | 同 side_label，客户端要求和其他类型订单保持一致  
updated_at | string | Optional | readOnly: true | 更新时间  
extremum_price | string | Optional | readOnly: true | 极值价格  
status_code | string | Optional | readOnly: true | status状态值  
created_at_precise | string | Optional | readOnly: true | 创建时间（高精度，秒.微秒格式）  
finished_at_precise | string | Optional | readOnly: true | 结束时间（高精度，秒.微秒格式）  
activated_at_precise | string | Optional | readOnly: true | 激活时间（高精度，秒.微秒格式）  
status_label | string | Optional | readOnly: true | 状态国际化标签（翻译后的状态文本）  
pos_margin_mode | string | Optional | readOnly: true | 仓位保证金模式 逐仓isolated/全仓cross  
position_mode | string | Optional | readOnly: true | 持仓模式 single、dual和dual_plus  
error_label | string | Optional | readOnly: true | 错误标签  
leverage | string | Optional | readOnly: true | 杠杆  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/update'
    query_param = ''
    body='{"id":123456789,"amount":"20","activation_price":"51000","price_offset":"0.2%"}'
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
    url="/futures/usdt/autoorder/v1/trail/update"
    query_param=""
    body_param='{"id":123456789,"amount":"20","activation_price":"51000","price_offset":"0.2%"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "id": 123456789,
      "amount": "20",
      "activation_price": "51000",
      "price_offset": "0.2%"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "message": "ok",
      "data": {
        "order": {
          "id": "63585",
          "user_id": "2124438083",
          "contract": "BTC_USDT",
          "settle": "usdt",
          "amount": "10",
          "is_gte": false,
          "activation_price": "0",
          "price_type": 1,
          "price_offset": "5%",
          "text": "apiv4",
          "reduce_only": false,
          "position_related": false,
          "created_at": "1769569837",
          "activated_at": "1769569837",
          "finished_at": "1769578529",
          "reason": "",
          "suborder_text": "apiv4-auto-trail-o-1d29",
          "is_dual_mode": false,
          "trigger_price": "91047.4",
          "suborder_id": "94294117233225616",
          "side_label": "买入",
          "original_status": 4,
          "status": "finished",
          "user": "2124438083",
          "create_time": "1769569837",
          "active_time": "1769569837",
          "finish_time": "1769578529",
          "position_side_output": "买入",
          "updated_at": "1769578529",
          "extremum_price": "86711.9",
          "status_code": "success",
          "created_at_precise": "1769569837778000",
          "finished_at_precise": "1769578529853294",
          "activated_at_precise": "1769569837976010",
          "status_label": "已完成",
          "pos_margin_mode": "",
          "position_mode": "single",
          "error_label": "",
          "leverage": ""
        }
      },
      "timestamp": 1769584936814
    }
    

##  获取追踪委托用户改单记录🔒 需要认证

GET`/futures/{settle}/autoorder/v1/trail/change_log`

GET `/futures/{settle}/autoorder/v1/trail/change_log`

_获取追踪委托用户改单记录_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
id | 请求参数 | integer(int64) | 是 | 委托ID  
page_num | 请求参数 | integer(int32) | 否 | 页号，从1开始  
page_size | 请求参数 | integer(int32) | 否 | 一页的数量  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | TrailOrderChangeLogResponse  
  
### 返回格式

状态码 **200**

TrailOrderChangeLogResponse

类型 | 约束  
---|---  
TrailOrderChangeLogResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

TrailOrderChangeLogData

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
change_log | array | Optional |  |   
  
**data / change_log**

类型 | 约束  
---|---  
array |   
  
**data / change_log / items**

追踪委托改单记录

类型 | 约束  
---|---  
TrailChangeLog |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
updated_at | string | Optional | readOnly: true | 更新时间  
amount | string | Optional | readOnly: true | 交易数量，单位是张，正数买，负数卖  
is_gte | boolean | Optional | readOnly: true | true：市场价大于等于激活价时激活，false：小于等于  
activation_price | string | Optional | readOnly: true | 激活价格，为0表示立即触发  
price_type | integer(int32) | Optional | enum: [0,1,2,3]  
readOnly: true | 激活价格的类型，0-未知,1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional | readOnly: true | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
is_create | boolean | Optional | readOnly: true | true-委托创建，false-委托修改  
  
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
    
    url = '/futures/usdt/autoorder/v1/trail/change_log'
    query_param = 'id=0'
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
    url="/futures/usdt/autoorder/v1/trail/change_log"
    query_param="id=0"
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
      "code": 0,
      "message": "ok",
      "data": {
        "change_log": [
          {
            "updated_at": "1546569968",
            "amount": "10",
            "is_gte": true,
            "activation_price": "50000",
            "price_type": 1,
            "price_offset": "0.1%",
            "is_create": true
          },
          {
            "updated_at": "1546570000",
            "amount": "20",
            "is_gte": true,
            "activation_price": "51000",
            "price_type": 1,
            "price_offset": "0.2%",
            "is_create": false
          },
          {
            "updated_at": "1546570100",
            "amount": "20",
            "is_gte": true,
            "activation_price": "51000",
            "price_type": 2,
            "price_offset": "0.2%",
            "is_create": false
          }
        ]
      },
      "timestamp": 1793627143000
    }
    

##  创建追逐限价单🔒 需要认证

POST`/futures/{settle}/autoorder/v1/chase/create`

POST `/futures/{settle}/autoorder/v1/chase/create`

_创建追逐限价单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
body | body | CreateChaseOrderReq | 是 |   
contract | body | string | 是 | 合约名称；服务端转为大写  
settle | body | string | 否 | 结算货币，由路径覆盖并转小写  
amount | body | string | 是 | 委托总张数，字符串十进制，正数买、负数卖。不可为 0  
price_limit | body | string | 是 | 最高追逐价，合法十进制字符串；未设置限价时请传 "0"  
offset_limit | body | string | 否 | 相对一档价的最大追逐距离，与 price_limit 互斥  
reduce_only | body | boolean | 否 | 是否只减仓  
text | body | string | 否 | 可选自定义标记  
is_dual_mode | body | boolean | 否 | 是否为双仓模式  
price_type | body | integer(int64) | 否 | 价格类型，1 买一卖一；2 买一卖一距离  
price_gap_type | body | integer(int64) | 否 | 在 price_type == 2 时使用：1 绝对价距，2 百分比  
price_gap_value | body | string | 否 | 与 price_gap_type 配套的价距取值  
pos_margin_mode | body | string | 否 | 仓位保证金模式，如逐仓 isolated、全仓 cross  
position_mode | body | string | 否 | 持仓模式（如 single、dual、dual_plus）  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

创建追逐限价单请求

请求体结构类型 | 约束  
---|---  
CreateChaseOrderReq | required: ["contract","amount","price_limit"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约名称；服务端转为大写  
settle | string | Optional |  | 结算货币，由路径覆盖并转小写  
amount | string | Required |  | 委托总张数，字符串十进制，正数买、负数卖。不可为 0  
price_limit | string | Required |  | 最高追逐价，合法十进制字符串；未设置限价时请传 "0"  
offset_limit | string | Optional |  | 相对一档价的最大追逐距离，与 price_limit 互斥  
reduce_only | boolean | Optional |  | 是否只减仓  
text | string | Optional |  | 可选自定义标记  
is_dual_mode | boolean | Optional |  | 是否为双仓模式  
price_type | integer(int64) | Optional |  | 价格类型，1 买一卖一；2 买一卖一距离  
price_gap_type | integer(int64) | Optional |  | 在 price_type == 2 时使用：1 绝对价距，2 百分比  
price_gap_value | string | Optional |  | 与 price_gap_type 配套的价距取值  
pos_margin_mode | string | Optional |  | 仓位保证金模式，如逐仓 isolated、全仓 cross  
position_mode | string | Optional |  | 持仓模式（如 single、dual、dual_plus）  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | CreateChaseOrderResp  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
CreateChaseOrderResp |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 新建委托 ID  
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/create'
    query_param = ''
    body='{"contract":"string","settle":"string","amount":"string","price_limit":"string","offset_limit":"string","reduce_only":true,"text":"string","is_dual_mode":true,"price_type":0,"price_gap_type":0,"price_gap_value":"string","pos_margin_mode":"string","position_mode":"string"}'
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
    url="/futures/usdt/autoorder/v1/chase/create"
    query_param=""
    body_param='{"contract":"string","settle":"string","amount":"string","price_limit":"string","offset_limit":"string","reduce_only":true,"text":"string","is_dual_mode":true,"price_type":0,"price_gap_type":0,"price_gap_value":"string","pos_margin_mode":"string","position_mode":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "contract": "string",
      "settle": "string",
      "amount": "string",
      "price_limit": "string",
      "offset_limit": "string",
      "reduce_only": true,
      "text": "string",
      "is_dual_mode": true,
      "price_type": 0,
      "price_gap_type": 0,
      "price_gap_value": "string",
      "pos_margin_mode": "string",
      "position_mode": "string"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": "string"
    }
    

##  终止追逐限价单🔒 需要认证

POST`/futures/{settle}/autoorder/v1/chase/stop`

POST `/futures/{settle}/autoorder/v1/chase/stop`

_终止追逐限价单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
body | body | StopChaseOrderReq | 是 |   
id | body | string | 否 | 委托 ID。与 text 二选一  
text | body | string | 否 | 自定义文本。仅当 id 为 0 或未传时必填  
settle | body | string | 否 | 由路径覆盖  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

终止追逐限价单请求

请求体结构类型 | 约束  
---|---  
StopChaseOrderReq |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托 ID。与 text 二选一  
text | string | Optional |  | 自定义文本。仅当 id 为 0 或未传时必填  
settle | string | Optional |  | 由路径覆盖  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | StopChaseOrderResp  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StopChaseOrderResp |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order | ChaseOrder | Optional |  | 追逐限价单详情/列表项  
  
**order**

追逐限价单详情/列表项

类型 | 约束  
---|---  
ChaseOrder |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  |   
user | string | Optional |  |   
contract | string | Optional |  |   
settle | string | Optional |  |   
amount | string | Optional |  | 总张数；正买负卖  
price_limit | string | Optional |  |   
reduce_only | boolean | Optional |  |   
text | string | Optional |  |   
create_time | integer(int64) | Optional |  |   
finish_time | integer(int64) | Optional |  |   
original_status | integer | Optional |  | 原始状态枚举  
status | string | Optional |  | 简化状态，如 open / finished  
reason | string | Optional |  |   
fill_amount | string | Optional |  |   
average_fill_price | string | Optional |  |   
suborder_id | string | Optional |  |   
is_dual_mode | boolean | Optional |  |   
side_label | string | Optional |  |   
position_side_output | string | Optional |  |   
chase_price | string | Optional |  |   
interval_sec | integer(uint32) | Optional |  |   
updated_at | integer(int64) | Optional |  |   
suborder_price | string | Optional |  |   
suborder_ongoing | boolean | Optional |  |   
suborder_finish_as | string | Optional |  |   
price_type | integer | Optional |  | PriceType 枚举：1 latest；2 index；3 mark  
price_gap_type | string | Optional |  |   
price_gap_value | string | Optional |  |   
status_code | string | Optional |  |   
create_time_precise | string | Optional |  | 创建时间（秒.微秒）  
finish_time_precise | string | Optional |  |   
pos_margin_mode | string | Optional |  |   
position_mode | string | Optional |  |   
leverage | string | Optional |  |   
error_label | string | Optional |  |   
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/stop'
    query_param = ''
    body='{"id":"string","text":"string","settle":"string"}'
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
    url="/futures/usdt/autoorder/v1/chase/stop"
    query_param=""
    body_param='{"id":"string","text":"string","settle":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "id": "string",
      "text": "string",
      "settle": "string"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "order": {
        "id": "string",
        "user": "string",
        "contract": "string",
        "settle": "string",
        "amount": "string",
        "price_limit": "string",
        "reduce_only": true,
        "text": "string",
        "create_time": 0,
        "finish_time": 0,
        "original_status": 0,
        "status": "string",
        "reason": "string",
        "fill_amount": "string",
        "average_fill_price": "string",
        "suborder_id": "string",
        "is_dual_mode": true,
        "side_label": "string",
        "position_side_output": "string",
        "chase_price": "string",
        "interval_sec": 0,
        "updated_at": 0,
        "suborder_price": "string",
        "suborder_ongoing": true,
        "suborder_finish_as": "string",
        "price_type": 0,
        "price_gap_type": "string",
        "price_gap_value": "string",
        "status_code": "string",
        "create_time_precise": "string",
        "finish_time_precise": "string",
        "pos_margin_mode": "string",
        "position_mode": "string",
        "leverage": "string",
        "error_label": "string"
      }
    }
    

##  批量终止追逐限价单🔒 需要认证

POST`/futures/{settle}/autoorder/v1/chase/stop_all`

POST `/futures/{settle}/autoorder/v1/chase/stop_all`

_批量终止追逐限价单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
body | body | StopAllChaseOrdersReq | 是 |   
contract | body | string | 否 | 可选合约名称  
settle | body | string | 否 | 由路径覆盖  
pos_margin_mode | body | string | 否 | 可选保证金模式  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

批量终止追逐限价单请求

请求体结构类型 | 约束  
---|---  
StopAllChaseOrdersReq |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional |  | 可选合约名称  
settle | string | Optional |  | 由路径覆盖  
pos_margin_mode | string | Optional |  | 可选保证金模式  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | StopAllChaseOrdersResp  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StopAllChaseOrdersResp |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
orders | array | Optional |  |   
  
**orders**

类型 | 约束  
---|---  
array |   
  
**orders / items**

追逐限价单详情/列表项

类型 | 约束  
---|---  
ChaseOrder |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  |   
user | string | Optional |  |   
contract | string | Optional |  |   
settle | string | Optional |  |   
amount | string | Optional |  | 总张数；正买负卖  
price_limit | string | Optional |  |   
reduce_only | boolean | Optional |  |   
text | string | Optional |  |   
create_time | integer(int64) | Optional |  |   
finish_time | integer(int64) | Optional |  |   
original_status | integer | Optional |  | 原始状态枚举  
status | string | Optional |  | 简化状态，如 open / finished  
reason | string | Optional |  |   
fill_amount | string | Optional |  |   
average_fill_price | string | Optional |  |   
suborder_id | string | Optional |  |   
is_dual_mode | boolean | Optional |  |   
side_label | string | Optional |  |   
position_side_output | string | Optional |  |   
chase_price | string | Optional |  |   
interval_sec | integer(uint32) | Optional |  |   
updated_at | integer(int64) | Optional |  |   
suborder_price | string | Optional |  |   
suborder_ongoing | boolean | Optional |  |   
suborder_finish_as | string | Optional |  |   
price_type | integer | Optional |  | PriceType 枚举：1 latest；2 index；3 mark  
price_gap_type | string | Optional |  |   
price_gap_value | string | Optional |  |   
status_code | string | Optional |  |   
create_time_precise | string | Optional |  | 创建时间（秒.微秒）  
finish_time_precise | string | Optional |  |   
pos_margin_mode | string | Optional |  |   
position_mode | string | Optional |  |   
leverage | string | Optional |  |   
error_label | string | Optional |  |   
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/stop_all'
    query_param = ''
    body='{"contract":"string","settle":"string","pos_margin_mode":"string"}'
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
    url="/futures/usdt/autoorder/v1/chase/stop_all"
    query_param=""
    body_param='{"contract":"string","settle":"string","pos_margin_mode":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "contract": "string",
      "settle": "string",
      "pos_margin_mode": "string"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "orders": [
        {
          "id": "string",
          "user": "string",
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "price_limit": "string",
          "reduce_only": true,
          "text": "string",
          "create_time": 0,
          "finish_time": 0,
          "original_status": 0,
          "status": "string",
          "reason": "string",
          "fill_amount": "string",
          "average_fill_price": "string",
          "suborder_id": "string",
          "is_dual_mode": true,
          "side_label": "string",
          "position_side_output": "string",
          "chase_price": "string",
          "interval_sec": 0,
          "updated_at": 0,
          "suborder_price": "string",
          "suborder_ongoing": true,
          "suborder_finish_as": "string",
          "price_type": 0,
          "price_gap_type": "string",
          "price_gap_value": "string",
          "status_code": "string",
          "create_time_precise": "string",
          "finish_time_precise": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "leverage": "string",
          "error_label": "string"
        }
      ]
    }
    

##  获取追逐限价单列表🔒 需要认证

GET`/futures/{settle}/autoorder/v1/chase/list`

GET `/futures/{settle}/autoorder/v1/chase/list`

_获取追逐限价单列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
contract | 请求参数 | string | 否 | 可选。非空时须为有效合约（与路径 settle 在行情缓存校验）；服务端转大写  
is_finished | 请求参数 | boolean | 否 | true 查历史单，false 查当前进行中等  
start_at | 请求参数 | integer(int64) | 否 | 与 end_at 搭配用于历史列表的时间下界；is_finished 为 true 时必填  
end_at | 请求参数 | integer(int64) | 否 | 与 start_at 搭配用于历史列表的时间上界；is_finished 为 true 时必填  
page_num | 请求参数 | integer(uint32) | 否 | 页码，从 1 开始  
page_size | 请求参数 | integer(uint32) | 否 | 每页条数；须为 1–100  
sort_by | 请求参数 | integer | 是 | 排序字段：1 按创建时间；2 按结束时间。不能传 0。  
hide_cancel | 请求参数 | boolean | 否 | 为 true 时在列表中隐藏已取消的委托  
reduce_only | 请求参数 | integer | 否 | OptionalBool：0 unknown、1 true、2 false；用于按是否只减仓筛选  
side | 请求参数 | integer | 否 | 多/空方向筛选，1 long，2 short  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
sort_by | 1  
sort_by | 2  
reduce_only | 0  
reduce_only | 1  
reduce_only | 2  
side | 0  
side | 1  
side | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | GetChaseOrdersResp  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
GetChaseOrdersResp |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
orders | array | Optional |  |   
  
**orders**

类型 | 约束  
---|---  
array |   
  
**orders / items**

追逐限价单详情/列表项

类型 | 约束  
---|---  
ChaseOrder |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  |   
user | string | Optional |  |   
contract | string | Optional |  |   
settle | string | Optional |  |   
amount | string | Optional |  | 总张数；正买负卖  
price_limit | string | Optional |  |   
reduce_only | boolean | Optional |  |   
text | string | Optional |  |   
create_time | integer(int64) | Optional |  |   
finish_time | integer(int64) | Optional |  |   
original_status | integer | Optional |  | 原始状态枚举  
status | string | Optional |  | 简化状态，如 open / finished  
reason | string | Optional |  |   
fill_amount | string | Optional |  |   
average_fill_price | string | Optional |  |   
suborder_id | string | Optional |  |   
is_dual_mode | boolean | Optional |  |   
side_label | string | Optional |  |   
position_side_output | string | Optional |  |   
chase_price | string | Optional |  |   
interval_sec | integer(uint32) | Optional |  |   
updated_at | integer(int64) | Optional |  |   
suborder_price | string | Optional |  |   
suborder_ongoing | boolean | Optional |  |   
suborder_finish_as | string | Optional |  |   
price_type | integer | Optional |  | PriceType 枚举：1 latest；2 index；3 mark  
price_gap_type | string | Optional |  |   
price_gap_value | string | Optional |  |   
status_code | string | Optional |  |   
create_time_precise | string | Optional |  | 创建时间（秒.微秒）  
finish_time_precise | string | Optional |  |   
pos_margin_mode | string | Optional |  |   
position_mode | string | Optional |  |   
leverage | string | Optional |  |   
error_label | string | Optional |  |   
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/list'
    query_param = 'sort_by=1'
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
    url="/futures/usdt/autoorder/v1/chase/list"
    query_param="sort_by=1"
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
      "orders": [
        {
          "id": "string",
          "user": "string",
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "price_limit": "string",
          "reduce_only": true,
          "text": "string",
          "create_time": 0,
          "finish_time": 0,
          "original_status": 0,
          "status": "string",
          "reason": "string",
          "fill_amount": "string",
          "average_fill_price": "string",
          "suborder_id": "string",
          "is_dual_mode": true,
          "side_label": "string",
          "position_side_output": "string",
          "chase_price": "string",
          "interval_sec": 0,
          "updated_at": 0,
          "suborder_price": "string",
          "suborder_ongoing": true,
          "suborder_finish_as": "string",
          "price_type": 0,
          "price_gap_type": "string",
          "price_gap_value": "string",
          "status_code": "string",
          "create_time_precise": "string",
          "finish_time_precise": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "leverage": "string",
          "error_label": "string"
        }
      ]
    }
    

##  获取追逐限价单详情🔒 需要认证

GET`/futures/{settle}/autoorder/v1/chase/detail`

GET `/futures/{settle}/autoorder/v1/chase/detail`

_获取追逐限价单详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
id | 请求参数 | string | 是 | 委托 ID，须为非 0 正整数  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | GetChaseOrderDetailResp  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
GetChaseOrderDetailResp |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order | ChaseOrder | Optional |  | 追逐限价单详情/列表项  
  
**order**

追逐限价单详情/列表项

类型 | 约束  
---|---  
ChaseOrder |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  |   
user | string | Optional |  |   
contract | string | Optional |  |   
settle | string | Optional |  |   
amount | string | Optional |  | 总张数；正买负卖  
price_limit | string | Optional |  |   
reduce_only | boolean | Optional |  |   
text | string | Optional |  |   
create_time | integer(int64) | Optional |  |   
finish_time | integer(int64) | Optional |  |   
original_status | integer | Optional |  | 原始状态枚举  
status | string | Optional |  | 简化状态，如 open / finished  
reason | string | Optional |  |   
fill_amount | string | Optional |  |   
average_fill_price | string | Optional |  |   
suborder_id | string | Optional |  |   
is_dual_mode | boolean | Optional |  |   
side_label | string | Optional |  |   
position_side_output | string | Optional |  |   
chase_price | string | Optional |  |   
interval_sec | integer(uint32) | Optional |  |   
updated_at | integer(int64) | Optional |  |   
suborder_price | string | Optional |  |   
suborder_ongoing | boolean | Optional |  |   
suborder_finish_as | string | Optional |  |   
price_type | integer | Optional |  | PriceType 枚举：1 latest；2 index；3 mark  
price_gap_type | string | Optional |  |   
price_gap_value | string | Optional |  |   
status_code | string | Optional |  |   
create_time_precise | string | Optional |  | 创建时间（秒.微秒）  
finish_time_precise | string | Optional |  |   
pos_margin_mode | string | Optional |  |   
position_mode | string | Optional |  |   
leverage | string | Optional |  |   
error_label | string | Optional |  |   
  
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
    
    url = '/futures/usdt/autoorder/v1/chase/detail'
    query_param = 'id=string'
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
    url="/futures/usdt/autoorder/v1/chase/detail"
    query_param="id=string"
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
      "order": {
        "id": "string",
        "user": "string",
        "contract": "string",
        "settle": "string",
        "amount": "string",
        "price_limit": "string",
        "reduce_only": true,
        "text": "string",
        "create_time": 0,
        "finish_time": 0,
        "original_status": 0,
        "status": "string",
        "reason": "string",
        "fill_amount": "string",
        "average_fill_price": "string",
        "suborder_id": "string",
        "is_dual_mode": true,
        "side_label": "string",
        "position_side_output": "string",
        "chase_price": "string",
        "interval_sec": 0,
        "updated_at": 0,
        "suborder_price": "string",
        "suborder_ongoing": true,
        "suborder_finish_as": "string",
        "price_type": 0,
        "price_gap_type": "string",
        "price_gap_value": "string",
        "status_code": "string",
        "create_time_precise": "string",
        "finish_time_precise": "string",
        "pos_margin_mode": "string",
        "position_mode": "string",
        "leverage": "string",
        "error_label": "string"
      }
    }
    

##  查询自动订单列表🔒 需要认证

GET`/futures/{settle}/price_orders`

GET `/futures/{settle}/price_orders`

_查询自动订单列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
status | 请求参数 | string | 是 | 基于状态查询订单列表  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
offset | 请求参数 | integer | 否 | 列表返回的偏移量，从 0 开始  
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
status | open  
status | finished  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 列表查询成功 | [FuturesPriceTriggeredOrder]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约价格单详情

类型 | 约束  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | 自动订单 ID  
id_string | string | Optional | readOnly: true | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 创建时间  
finish_time | number(double) | Optional | readOnly: true | 结束时间  
trade_id | integer(int64) | Optional | readOnly: true | 触发后委托单ID  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
reason | string | Optional | readOnly: true | 订单结束的附加描述信息  
order_type | string | Optional |  | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
me_order_id | integer(int64) | Optional | readOnly: true | 委托单止盈止损对应的委托 ID  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
**items / initial**

类型 | 约束  
---|---  
object | required: ["contract","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约标识  
size | integer(int64) | Optional |  | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
amount | string | Optional |  | 同size参数，用于兼容小数,同时存在时以amount为准  
price | string | Required |  | 交易价，当价格为 0 时，表示通过市价方式来下单  
close | boolean | Optional | default: false  
writeOnly: true | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
reduce_only | boolean | Optional | default: false | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
auto_size | string | Optional | writeOnly: true | 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
  
**items / trigger**

类型 | 约束  
---|---  
object | required: ["price","rule"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
price_type | integer(int32) | Optional | enum: [0,1,2] | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
price | string | Required |  | 价格触发时为价格，价差触发时为价差  
rule | integer(int32) | Required | enum: [1,2] | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
expiration | integer | Optional |  | 最长等待触发时间，超时则取消该订单，单位是秒 s  
  
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
    
    url = '/futures/usdt/price_orders'
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
    url="/futures/usdt/price_orders"
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

POST`/futures/{settle}/price_orders`

POST `/futures/{settle}/price_orders`

_创建价格触发订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | FuturesPriceTriggeredOrder | 是 |   
initial | body | object | 是 |   
» contract | body | string | 是 | 合约标识  
» size | body | integer(int64) | 否 | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
  
» amount | body | string | 否 | 同size参数，用于兼容小数,同时存在时以amount为准  
» price | body | string | 是 | 交易价，当价格为 0 时，表示通过市价方式来下单  
» close | body | boolean | 否 | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
  
» tif | body | string | 否 | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
  
» text | body | string | 否 | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
  
» reduce_only | body | boolean | 否 | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
» auto_size | body | string | 否 | 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  
  
» is_reduce_only | body | boolean | 否 | 是否为只减仓委托。对应请求中的`reduce_only`。  
» is_close | body | boolean | 否 | 是否为平仓委托。对应请求中的`close`。  
trigger | body | object | 是 |   
» strategy_type | body | integer(int32) | 否 | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
  
» price_type | body | integer(int32) | 否 | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
» price | body | string | 是 | 价格触发时为价格，价差触发时为价差  
» rule | body | integer(int32) | 是 | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
  
» expiration | body | integer | 否 | 最长等待触发时间，超时则取消该订单，单位是秒 s  
id | body | integer(int64) | 否 | 自动订单 ID  
id_string | body | string | 否 | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
  
user | body | integer | 否 | 用户 ID  
create_time | body | number(double) | 否 | 创建时间  
finish_time | body | number(double) | 否 | 结束时间  
trade_id | body | integer(int64) | 否 | 触发后委托单ID  
status | body | string | 否 | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
  
finish_as | body | string | 否 | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
reason | body | string | 否 | 订单结束的附加描述信息  
order_type | body | string | 否 | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
  
me_order_id | body | integer(int64) | 否 | 委托单止盈止损对应的委托 ID  
pos_margin_mode | body | string | 否 | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
settle | URL | string | 是 | 永续合约结算货币  
  
####  详细描述

**» size** : 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  

**» close** : 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  

**» tif** : Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  

**» text** : 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  

**» auto_size** : 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  

**» strategy_type** : 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  

**» rule** : 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  

** id_string**: 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  

** status**: 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  

** order_type**: 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  

** pos_margin_mode**: 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» tif | gtc  
» tif | ioc  
» strategy_type | 0  
» strategy_type | 1  
» price_type | 0  
» price_type | 1  
» price_type | 2  
» rule | 1  
» rule | 2  
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
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

合约价格单详情

请求体结构类型 | 约束  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | 自动订单 ID  
id_string | string | Optional | readOnly: true | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 创建时间  
finish_time | number(double) | Optional | readOnly: true | 结束时间  
trade_id | integer(int64) | Optional | readOnly: true | 触发后委托单ID  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
reason | string | Optional | readOnly: true | 订单结束的附加描述信息  
order_type | string | Optional |  | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
me_order_id | integer(int64) | Optional | readOnly: true | 委托单止盈止损对应的委托 ID  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
**initial**

请求体结构类型 | 约束  
---|---  
object | required: ["contract","price"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约标识  
size | integer(int64) | Optional |  | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
amount | string | Optional |  | 同size参数，用于兼容小数,同时存在时以amount为准  
price | string | Required |  | 交易价，当价格为 0 时，表示通过市价方式来下单  
close | boolean | Optional | default: false  
writeOnly: true | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
reduce_only | boolean | Optional | default: false | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
auto_size | string | Optional | writeOnly: true | 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
  
**trigger**

请求体结构类型 | 约束  
---|---  
object | required: ["price","rule"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
price_type | integer(int32) | Optional | enum: [0,1,2] | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
price | string | Required |  | 价格触发时为价格，价差触发时为价差  
rule | integer(int32) | Required | enum: [1,2] | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
expiration | integer | Optional |  | 最长等待触发时间，超时则取消该订单，单位是秒 s  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 成功下单 | TriggerOrderResponse  
  
### 返回格式

状态码 **201**

TriggerOrderResponse

类型 | 约束  
---|---  
TriggerOrderResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 自动订单 ID  
id_string | string | Optional | readOnly: true | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
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
    
    url = '/futures/usdt/price_orders'
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
    url="/futures/usdt/price_orders"
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
      "id": 1432329,
      "id_string": "1432329"
    }
    

##  批量取消自动订单🔒 需要认证

DELETE`/futures/{settle}/price_orders`

DELETE `/futures/{settle}/price_orders`

_批量取消自动订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
contract | 请求参数 | string | 否 | 合约标识，如果指定则只返回该合约相关数据  
settle | URL | string | 是 | 永续合约结算货币  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 批量撤销请求接收并处理，是否成功根据订单列表来决定 | [FuturesPriceTriggeredOrder]  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
array |   
  
**items**

合约价格单详情

类型 | 约束  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | 自动订单 ID  
id_string | string | Optional | readOnly: true | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 创建时间  
finish_time | number(double) | Optional | readOnly: true | 结束时间  
trade_id | integer(int64) | Optional | readOnly: true | 触发后委托单ID  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
reason | string | Optional | readOnly: true | 订单结束的附加描述信息  
order_type | string | Optional |  | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
me_order_id | integer(int64) | Optional | readOnly: true | 委托单止盈止损对应的委托 ID  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
**items / initial**

类型 | 约束  
---|---  
object | required: ["contract","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约标识  
size | integer(int64) | Optional |  | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
amount | string | Optional |  | 同size参数，用于兼容小数,同时存在时以amount为准  
price | string | Required |  | 交易价，当价格为 0 时，表示通过市价方式来下单  
close | boolean | Optional | default: false  
writeOnly: true | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
reduce_only | boolean | Optional | default: false | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
auto_size | string | Optional | writeOnly: true | 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
  
**items / trigger**

类型 | 约束  
---|---  
object | required: ["price","rule"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
price_type | integer(int32) | Optional | enum: [0,1,2] | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
price | string | Required |  | 价格触发时为价格，价差触发时为价差  
rule | integer(int32) | Required | enum: [1,2] | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
expiration | integer | Optional |  | 最长等待触发时间，超时则取消该订单，单位是秒 s  
  
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
    
    url = '/futures/usdt/price_orders'
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
    url="/futures/usdt/price_orders"
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

GET`/futures/{settle}/price_orders/{order_id}`

GET `/futures/{settle}/price_orders/{order_id}`

_查询单个自动订单详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
order_id | URL | integer(int64) | 是 | 成功创建订单时返回的 ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 自动订单详情 | FuturesPriceTriggeredOrder  
205 | [Reset Content ](https://tools.ietf.org/html/rfc7231#section-6.3.6) | 条件单不存在时的业务错误响应（HTTP 205）。 | Inline  
  
### 返回格式

状态码 **200**

合约价格单详情

类型 | 约束  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | 自动订单 ID  
id_string | string | Optional | readOnly: true | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 创建时间  
finish_time | number(double) | Optional | readOnly: true | 结束时间  
trade_id | integer(int64) | Optional | readOnly: true | 触发后委托单ID  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
reason | string | Optional | readOnly: true | 订单结束的附加描述信息  
order_type | string | Optional |  | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
me_order_id | integer(int64) | Optional | readOnly: true | 委托单止盈止损对应的委托 ID  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
**initial**

类型 | 约束  
---|---  
object | required: ["contract","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约标识  
size | integer(int64) | Optional |  | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
amount | string | Optional |  | 同size参数，用于兼容小数,同时存在时以amount为准  
price | string | Required |  | 交易价，当价格为 0 时，表示通过市价方式来下单  
close | boolean | Optional | default: false  
writeOnly: true | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
reduce_only | boolean | Optional | default: false | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
auto_size | string | Optional | writeOnly: true | 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
  
**trigger**

类型 | 约束  
---|---  
object | required: ["price","rule"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
price_type | integer(int32) | Optional | enum: [0,1,2] | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
price | string | Required |  | 价格触发时为价格，价差触发时为价差  
rule | integer(int32) | Required | enum: [1,2] | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
expiration | integer | Optional |  | 最长等待触发时间，超时则取消该订单，单位是秒 s  
  
状态码 **205**

FuturesPriceTriggeredOrderError

条件单业务错误信息

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | string | Optional |  | 业务错误码  
label | string | Optional |  | 错误标识符  
message | string | Optional |  | 详细错误描述  
  
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
    
    url = '/futures/usdt/price_orders/0'
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
    url="/futures/usdt/price_orders/0"
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
    

> 205 返回
    
    
    {
      "code": "1034",
      "label": "AUTO_ORDER_NOT_FOUND",
      "message": "no orderID match"
    }
    

##  撤销单个自动订单🔒 需要认证

DELETE`/futures/{settle}/price_orders/{order_id}`

DELETE `/futures/{settle}/price_orders/{order_id}`

_撤销单个自动订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
settle | URL | string | 是 | 永续合约结算货币  
order_id | URL | integer(int64) | 是 | 成功创建订单时返回的 ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
settle | btc  
settle | usdt  
settle | usd1  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 自动订单详情 | FuturesPriceTriggeredOrder  
  
### 返回格式

状态码 **200**

合约价格单详情

类型 | 约束  
---|---  
FuturesPriceTriggeredOrder | required: ["initial","trigger"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | 自动订单 ID  
id_string | string | Optional | readOnly: true | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 创建时间  
finish_time | number(double) | Optional | readOnly: true | 结束时间  
trade_id | integer(int64) | Optional | readOnly: true | 触发后委托单ID  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
reason | string | Optional | readOnly: true | 订单结束的附加描述信息  
order_type | string | Optional |  | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
me_order_id | integer(int64) | Optional | readOnly: true | 委托单止盈止损对应的委托 ID  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
**initial**

类型 | 约束  
---|---  
object | required: ["contract","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约标识  
size | integer(int64) | Optional |  | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
amount | string | Optional |  | 同size参数，用于兼容小数,同时存在时以amount为准  
price | string | Required |  | 交易价，当价格为 0 时，表示通过市价方式来下单  
close | boolean | Optional | default: false  
writeOnly: true | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
reduce_only | boolean | Optional | default: false | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
auto_size | string | Optional | writeOnly: true | 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
  
**trigger**

类型 | 约束  
---|---  
object | required: ["price","rule"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
price_type | integer(int32) | Optional | enum: [0,1,2] | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
price | string | Required |  | 价格触发时为价格，价差触发时为价差  
rule | integer(int32) | Required | enum: [1,2] | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
expiration | integer | Optional |  | 最长等待触发时间，超时则取消该订单，单位是秒 s  
  
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
    
    url = '/futures/usdt/price_orders/0'
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
    url="/futures/usdt/price_orders/0"
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
    

##  修改单个自动订单🔒 需要认证

PUT`/futures/{settle}/price_orders/amend/{order_id}`

PUT `/futures/{settle}/price_orders/amend/{order_id}`

_修改单个自动订单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | FuturesUpdatePriceTriggeredOrder | 是 |   
settle | body | string | 否 | 永续合约结算币种，例如 usdt、btc、usd1  
order_id | body | integer(int64) | 是 | 待修改的止盈/止损触发单 ID  
size | body | integer(int64) | 否 | 修改后的合约张数，全平：0；部分平仓：正负代表方向（同创建接口逻辑）  
amount | body | string | 否 | 同size参数，用于兼容小数,同时存在时以amount为准  
price | body | string | 否 | 代表修改后的交易价，当价格为 0 时，表示通过市价方式来下单  
trigger_price | body | string | 否 | 修改后的触发价格  
price_type | body | integer(int32) | 否 | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
auto_size | body | string | 否 | 单仓模式不需设置auto_size  
双仓模式部分平仓(size≠0)时，不需设置auto_size  
双仓模式全部平仓(size=0)时，必须设置auto_size，close_long 平多头， close_short 平空头  
  
close | body | boolean | 否 | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
  
settle | URL | string | 是 | 永续合约结算货币  
order_id | URL | string | 是 | 成功创建订单时返回的 ID  
  
####  详细描述

** auto_size**: 单仓模式不需设置auto_size  
双仓模式部分平仓(size≠0)时，不需设置auto_size  
双仓模式全部平仓(size=0)时，必须设置auto_size，close_long 平多头， close_short 平空头  

** close**: 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
price_type | 0  
price_type | 1  
price_type | 2  
settle | btc  
settle | usdt  
settle | usd1  
  
####  请求体结构

修改价格单详情

请求体结构类型 | 约束  
---|---  
FuturesUpdatePriceTriggeredOrder | required: ["order_id"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
settle | string | Optional |  | 永续合约结算币种，例如 usdt、btc、usd1  
order_id | integer(int64) | Required |  | 待修改的止盈/止损触发单 ID  
size | integer(int64) | Optional |  | 修改后的合约张数，全平：0；部分平仓：正负代表方向（同创建接口逻辑）  
amount | string | Optional |  | 同size参数，用于兼容小数,同时存在时以amount为准  
price | string | Optional |  | 代表修改后的交易价，当价格为 0 时，表示通过市价方式来下单  
trigger_price | string | Optional |  | 修改后的触发价格  
price_type | integer(int32) | Optional | enum: [0,1,2] | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
auto_size | string | Optional |  | 单仓模式不需设置auto_size  
双仓模式部分平仓(size≠0)时，不需设置auto_size  
双仓模式全部平仓(size=0)时，必须设置auto_size，close_long 平多头， close_short 平空头  
close | boolean | Optional |  | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功下单 | TriggerOrderResponse  
  
### 返回格式

状态码 **200**

TriggerOrderResponse

类型 | 约束  
---|---  
TriggerOrderResponse |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 自动订单 ID  
id_string | string | Optional | readOnly: true | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
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
    
    url = '/futures/usdt/price_orders/amend/2110911746238578688'
    query_param = ''
    body='{"order_id":123456789,"size":0,"price":"0","trigger_price":"988888","price_type":0,"auto_size":"close_long"}'
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
    url="/futures/usdt/price_orders/amend/2110911746238578688"
    query_param=""
    body_param='{"order_id":123456789,"size":0,"price":"0","trigger_price":"988888","price_type":0,"auto_size":"close_long"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "order_id": 123456789,
      "size": 0,
      "price": "0",
      "trigger_price": "988888",
      "price_type": 0,
      "auto_size": "close_long"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "id": 1432329,
      "id_string": "1432329"
    }
    

#  模型

##  CreateChaseOrderReq

创建追逐限价单请求

类型 | 约束  
---|---  
object | required: ["contract","amount","price_limit"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约名称；服务端转为大写  
settle | string | Optional |  | 结算货币，由路径覆盖并转小写  
amount | string | Required |  | 委托总张数，字符串十进制，正数买、负数卖。不可为 0  
price_limit | string | Required |  | 最高追逐价，合法十进制字符串；未设置限价时请传 "0"  
offset_limit | string | Optional |  | 相对一档价的最大追逐距离，与 price_limit 互斥  
reduce_only | boolean | Optional |  | 是否只减仓  
text | string | Optional |  | 可选自定义标记  
is_dual_mode | boolean | Optional |  | 是否为双仓模式  
price_type | integer(int64) | Optional |  | 价格类型，1 买一卖一；2 买一卖一距离  
price_gap_type | integer(int64) | Optional |  | 在 price_type == 2 时使用：1 绝对价距，2 百分比  
price_gap_value | string | Optional |  | 与 price_gap_type 配套的价距取值  
pos_margin_mode | string | Optional |  | 仓位保证金模式，如逐仓 isolated、全仓 cross  
position_mode | string | Optional |  | 持仓模式（如 single、dual、dual_plus）  
      
    
    {
      "contract": "string",
      "settle": "string",
      "amount": "string",
      "price_limit": "string",
      "offset_limit": "string",
      "reduce_only": true,
      "text": "string",
      "is_dual_mode": true,
      "price_type": 0,
      "price_gap_type": 0,
      "price_gap_value": "string",
      "pos_margin_mode": "string",
      "position_mode": "string"
    }
    
    

##  CountdownCancelAllFuturesTask

CountdownCancelAllFuturesTask

倒计时任务详情

类型 | 约束  
---|---  
object | required: ["timeout","market"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
timeout | integer(int32) | Required |  | 倒计时时间，单位 秒  
至少5秒，为0时表示取消倒计时  
contract | string | Optional |  | 合约标识  
      
    
    {
      "timeout": 0,
      "contract": "string"
    }
    
    

##  FuturesRiskLimitTier

梯度风险限额的每个档位信息

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tier | integer(int) | Optional |  | 档位  
risk_limit | string | Optional |  | 风险限额  
initial_rate | string | Optional |  | 初始保证金率  
maintenance_rate | string | Optional |  | 风险限额的第一档维持保证金率要求  
leverage_max | string | Optional |  | 最大杠杆  
deduction | string | Optional |  | 维持保证金速算扣减额  
      
    
    {
      "tier": 0,
      "risk_limit": "string",
      "initial_rate": "string",
      "maintenance_rate": "string",
      "leverage_max": "string",
      "deduction": "string"
    }
    
    

##  UpdateDualCompPositionCrossModeRequest

UpdateDualCompPositionCrossModeRequest

类型 | 约束  
---|---  
object | required: ["mode","contract"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
mode | string | Required |  | 全逐仓模式，ISOLATED-逐仓，CROSS-全仓  
contract | string | Required |  | 合约市场  
      
    
    {
      "mode": "string",
      "contract": "BTC_USDT"
    }
    
    

##  FuturesOrderTimerange

合约订单详情

类型 | 约束  
---|---  
object | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | string | Optional | readOnly: true | 订单更新时间  
finish_time | string | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 未成交数量  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单费率  
mkfr | string | Optional | readOnly: true | 做单费率  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
      
    
    {
      "id": 0,
      "user": 0,
      "create_time": 0,
      "update_time": "string",
      "finish_time": "string",
      "finish_as": "filled",
      "status": "open",
      "contract": "string",
      "size": "string",
      "iceberg": "string",
      "price": "string",
      "close": false,
      "is_close": true,
      "reduce_only": false,
      "is_reduce_only": true,
      "is_liq": true,
      "tif": "gtc",
      "left": "string",
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "auto_size": "close_long",
      "stp_id": 0,
      "stp_act": "co",
      "amend_text": "string",
      "pid": 0,
      "market_order_slip_ratio": "string",
      "pos_margin_mode": "string",
      "tpsl_tp_trigger_price": "string",
      "tpsl_sl_trigger_price": "string"
    }
    
    

##  CreateTrailOrderResponse

CreateTrailOrderResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

CreateTrailOrderResult

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托ID  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "id": "string"
      },
      "timestamp": 0
    }
    
    

##  PositionClose

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | number(double) | Optional | readOnly: true | 平仓时间  
contract | string | Optional | readOnly: true | 合约标识  
side | string | Optional | enum: ["long","short"]  
readOnly: true | 多空方向  
  
\- `long`: 做多  
\- `short`: 做空  
pnl | string | Optional | readOnly: true | 盈亏  
pnl_pnl | string | Optional | readOnly: true | 盈亏-仓位盈亏  
pnl_fund | string | Optional | readOnly: true | 盈亏-资金费用  
pnl_fee | string | Optional | readOnly: true | 盈亏-手续费  
text | string | Optional | readOnly: true | 平仓委托的来源，具体取值参见`order.text`字段  
max_size | string | Optional | readOnly: true | 最大持仓量  
accum_size | string | Optional | readOnly: true | 累计平仓量  
first_open_time | integer(int64) | Optional | readOnly: true | 开仓时间  
long_price | string | Optional | readOnly: true | side为long时表示开仓均价，为short时表示平仓均价  
short_price | string | Optional | readOnly: true | side为long时表示平仓均价，为short时表示开仓均价  
      
    
    {
      "time": 0,
      "contract": "string",
      "side": "long",
      "pnl": "string",
      "pnl_pnl": "string",
      "pnl_fund": "string",
      "pnl_fee": "string",
      "text": "string",
      "max_size": "string",
      "accum_size": "string",
      "first_open_time": 0,
      "long_price": "string",
      "short_price": "string"
    }
    
    

##  CreateChaseOrderResp

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 新建委托 ID  
      
    
    {
      "id": "string"
    }
    
    

##  FuturesLiqOrder

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | 强制平仓时间  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 用户仓位大小  
order_size | string | Optional | readOnly: true | 强平委托数量  
order_price | string | Optional | readOnly: true | 强平委托价  
fill_price | string | Optional | readOnly: true | 强平委托吃单平均成交价  
left | string | Optional | readOnly: true | 保留字段，当前无业务含义  
      
    
    {
      "time": 0,
      "contract": "string",
      "size": "string",
      "order_size": "string",
      "order_price": "string",
      "fill_price": "string",
      "left": "string"
    }
    
    

##  BatchAmendOrderReq

修改合约订单参数

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | 订单id，order_id和text至少传一个  
text | string | Optional |  | 用户自定义订单text，order_id和text至少传一个  
size | string | Optional |  | 新的委托大小。包括已成交委托的部分。  
\- 如果小于等于已成交数量，则撤销委托。  
\- 新的委托买卖方向必须跟原有的一致。  
\- 不能修改平仓单的size。  
\- 对于只减仓委托，如果调大size，则可能踢出其他只减仓委托。  
\- 如果不修改价格，则调小size不会影响深度排队，调大size会排到当前价位最后。  
price | string | Optional |  | 新的委托价格。  
amend_text | string | Optional |  | 用户可以备注这次修改的信息。  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
      
    
    {
      "order_id": 0,
      "text": "string",
      "size": "string",
      "price": "string",
      "amend_text": "string",
      "action_mode": "string"
    }
    
    

##  FuturesUpdatePriceTriggeredOrder

修改价格单详情

类型 | 约束  
---|---  
object | required: ["order_id"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
settle | string | Optional |  | 永续合约结算币种，例如 usdt、btc、usd1  
order_id | integer(int64) | Required |  | 待修改的止盈/止损触发单 ID  
size | integer(int64) | Optional |  | 修改后的合约张数，全平：0；部分平仓：正负代表方向（同创建接口逻辑）  
amount | string | Optional |  | 同size参数，用于兼容小数,同时存在时以amount为准  
price | string | Optional |  | 代表修改后的交易价，当价格为 0 时，表示通过市价方式来下单  
trigger_price | string | Optional |  | 修改后的触发价格  
price_type | integer(int32) | Optional | enum: [0,1,2] | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
auto_size | string | Optional |  | 单仓模式不需设置auto_size  
双仓模式部分平仓(size≠0)时，不需设置auto_size  
双仓模式全部平仓(size=0)时，必须设置auto_size，close_long 平多头， close_short 平空头  
close | boolean | Optional |  | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
      
    
    {
      "settle": "string",
      "order_id": 0,
      "size": 0,
      "amount": "string",
      "price": "string",
      "trigger_price": "string",
      "price_type": 0,
      "auto_size": "string",
      "close": true
    }
    
    

##  StopAllTrailOrders

StopAllTrailOrders

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional |  | 合约名称  
related_position | integer(int32) | Optional | enum: [1,2] | 关联仓位，如果传了就只撤和这个仓位关联的委托，1-多仓，2-空仓  
      
    
    {
      "contract": "string",
      "related_position": 1
    }
    
    

##  FuturesOrder

合约订单详情

类型 | 约束  
---|---  
object | required: ["contract","size","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态：  
  
\- `open`：等待处理  
\- `finished`：订单已结束  
contract | string | Required |  | 合约标识  
size | string | Required |  | 必填。委托数量，单位为合约张数；正数买入，负数卖出。平仓委托设为 0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Required |  | 必选。委托价，价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 剩余未成交张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
\- clear: 合约下架清退  
tkfr | string | Optional | readOnly: true | 吃单手续费率。  
mkfr | string | Optional | readOnly: true | 挂单手续费率。  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
market_order_slip_ratio | string | Optional |  | 市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓 只在简易分仓模式下传递  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
tpsl_tp_trigger_price | string | Optional |  | 止盈价  
tpsl_sl_trigger_price | string | Optional |  | 止损价  
tpsl_tp_bbo_type | string | Optional |  | 止盈bbo类型  
tpsl_sl_bbo_type | string | Optional |  | 止损bbo类型  
      
    
    {
      "id": 0,
      "user": 0,
      "create_time": 0,
      "update_time": 0,
      "finish_time": 0,
      "finish_as": "filled",
      "status": "open",
      "contract": "string",
      "size": "string",
      "iceberg": "string",
      "price": "string",
      "close": false,
      "is_close": true,
      "reduce_only": false,
      "is_reduce_only": true,
      "is_liq": true,
      "tif": "gtc",
      "left": "string",
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "auto_size": "close_long",
      "stp_id": 0,
      "stp_act": "co",
      "amend_text": "string",
      "pid": 0,
      "market_order_slip_ratio": "string",
      "pos_margin_mode": "string",
      "action_mode": "string",
      "tpsl_tp_trigger_price": "string",
      "tpsl_sl_trigger_price": "string",
      "tpsl_tp_bbo_type": "string",
      "tpsl_sl_bbo_type": "string"
    }
    
    

##  BatchFuturesOrder

合约订单详情

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
succeeded | boolean | Optional |  | 请求执行结果  
label | string | Optional |  | 错误标识，仅当执行失败时存在  
detail | string | Optional |  | 错误详情，仅当执行失败并需要给出详情时存在  
id | integer(int64) | Optional | readOnly: true | 合约订单 ID  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 订单创建时间  
update_time | number(double) | Optional | readOnly: true | 订单更新时间  
finish_time | number(double) | Optional | readOnly: true | 订单结束时间，未结束订单无此字段返回  
finish_as | string | Optional | enum: ["filled","cancelled","liquidated","ioc","auto_deleveraged","reduce_only","position_closed","reduce_out","stp"]  
readOnly: true | 结束方式，包括：  
  
\- filled: 完全成交  
\- cancelled: 用户撤销  
\- liquidated: 强制平仓撤销  
\- ioc: 未立即完全成交，因为tif设置为ioc  
\- auto_deleveraged: 自动减仓撤销  
\- reduce_only: 增持仓位撤销，因为设置reduce_only或平仓  
\- position_closed: 因为仓位平掉了，所以挂单被撤掉  
\- reduce_out: 只减仓被排除的不容易成交的挂单  
\- stp: 订单发生自成交限制而被撤销  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 订单状态。  
  
\- `open`: 等待处理  
\- `finished`: 已结束的订单  
contract | string | Optional |  | 合约标识  
size | string | Optional |  | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
iceberg | string | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
price | string | Optional |  | 委托价。价格为0并且`tif`为`ioc`，代表市价委托。  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | string | Optional | readOnly: true | 未成交数量  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
tkfr | string | Optional | readOnly: true | 吃单费率  
mkfr | string | Optional | readOnly: true | 做单费率  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
market_order_slip_ratio | string | Optional |  | 最大滑点比率  
      
    
    {
      "succeeded": true,
      "label": "string",
      "detail": "string",
      "id": 0,
      "user": 0,
      "create_time": 0,
      "update_time": 0,
      "finish_time": 0,
      "finish_as": "filled",
      "status": "open",
      "contract": "string",
      "size": "string",
      "iceberg": "string",
      "price": "string",
      "close": false,
      "is_close": true,
      "reduce_only": false,
      "is_reduce_only": true,
      "is_liq": true,
      "tif": "gtc",
      "left": "string",
      "fill_price": "string",
      "text": "string",
      "tkfr": "string",
      "mkfr": "string",
      "refu": 0,
      "auto_size": "close_long",
      "stp_act": "co",
      "stp_id": 0,
      "market_order_slip_ratio": "string"
    }
    
    

##  CreateTrailOrder

CreateTrailOrder

类型 | 约束  
---|---  
object | required: ["contract","amount","price_type"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约名称  
amount | string | Required |  | 交易数量，单位是张，正数表示买，负数表示卖  
activation_price | string | Optional | default: "0" | 激活价格，为0表示立即触发  
is_gte | boolean | Optional |  | true：市场价大于等于激活价时激活，false：小于等于  
price_type | integer(int32) | Required | enum: [1,2,3] | 激活价格的类型，必填，1-最新价格，2-指数价格，3-标记价格；调用方须显式指定  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
reduce_only | boolean | Optional | default: false | 是否只减仓  
position_related | boolean | Optional | default: false | 是否和仓位绑定(如果 position_related = true（关联仓位），那么 reduce_only 必须也是 true)  
text | string | Optional | default: "apiv4" | 订单自定义信息，可选字段。用于标识订单来源或设置用户自定义 ID。  
  
**如果非空** ，必须满足以下规则之一：  
  
**1\. 内部保留字段（标识订单来源）** ：  
\- `apiv4`: API 调用  
**2\. 用户自定义字段（设置自定义 ID）** ：  
\- 必须以 `t-` 开头  
\- `t-` 后面的内容长度不能超过 28 字节  
\- 只能包含：数字、字母、下划线(_)、中划线(-) 或者点(.)  
\- 示例：`t-my-order-001`、`t-trail_2024.01`  
  
**注意** ：用户自定义字段不能与内部保留字段冲突。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 逐仓isolated/全仓cross  
position_mode | string | Optional |  | 持仓模式 single、dual和dual_plus  
      
    
    {
      "contract": "string",
      "amount": "string",
      "activation_price": "0",
      "is_gte": true,
      "price_type": 1,
      "price_offset": "string",
      "reduce_only": false,
      "position_related": false,
      "text": "apiv4",
      "pos_margin_mode": "string",
      "position_mode": "string"
    }
    
    

##  BatchFundingRatesRequest

类型 | 约束  
---|---  
object | required: ["contracts"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contracts | array | Required | minItems: 1  
maxItems: 200 | 合约名称数组  
  
**contracts**

合约名称数组

类型 | 约束  
---|---  
array | minItems: 1  
maxItems: 200  
  
**contracts / items**

类型 | 约束  
---|---  
string |   
      
    
    {
      "contracts": [
        "BTC_USDT",
        "ETH_USDT"
      ]
    }
    
    

##  GetChaseOrdersResp

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
orders | array | Optional |  |   
  
**orders**

类型 | 约束  
---|---  
array |   
  
**orders / items**

追逐限价单详情/列表项

类型 | 约束  
---|---  
ChaseOrder |   
      
    
    {
      "orders": [
        {
          "id": "string",
          "user": "string",
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "price_limit": "string",
          "reduce_only": true,
          "text": "string",
          "create_time": 0,
          "finish_time": 0,
          "original_status": 0,
          "status": "string",
          "reason": "string",
          "fill_amount": "string",
          "average_fill_price": "string",
          "suborder_id": "string",
          "is_dual_mode": true,
          "side_label": "string",
          "position_side_output": "string",
          "chase_price": "string",
          "interval_sec": 0,
          "updated_at": 0,
          "suborder_price": "string",
          "suborder_ongoing": true,
          "suborder_finish_as": "string",
          "price_type": 0,
          "price_gap_type": "string",
          "price_gap_value": "string",
          "status_code": "string",
          "create_time_precise": "string",
          "finish_time_precise": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "leverage": "string",
          "error_label": "string"
        }
      ]
    }
    
    

##  FuturesAutoDeleverage

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | 自动减仓时间  
user | integer(int64) | Optional | readOnly: true | 用户ID  
order_id | integer(int64) | Optional | readOnly: true | 减仓委托ID，2023-02-20之前的数据order_id为null  
contract | string | Optional | readOnly: true | 合约标识  
leverage | string | Optional | readOnly: true | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
cross_leverage_limit | string | Optional | readOnly: true | 全仓模式下的杠杆倍数  
entry_price | string | Optional | readOnly: true | 平均开仓价  
fill_price | string | Optional | readOnly: true | 平均成交价  
trade_size | string | Optional | readOnly: true | 成交数量  
position_size | string | Optional | readOnly: true | 自动减仓后的持仓量  
      
    
    {
      "time": 0,
      "user": 0,
      "order_id": 0,
      "contract": "string",
      "leverage": "string",
      "cross_leverage_limit": "string",
      "entry_price": "string",
      "fill_price": "string",
      "trade_size": "string",
      "position_size": "string"
    }
    
    

##  FuturesPositionCrossMode

FuturesPositionCrossMode

类型 | 约束  
---|---  
object | required: ["mode","contract"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
mode | string | Required |  | 全逐仓模式，ISOLATED-逐仓，CROSS-全仓  
contract | string | Required |  | 合约市场  
      
    
    {
      "mode": "string",
      "contract": "BTC_USDT"
    }
    
    

##  MyFuturesTradeTimeRange

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
trade_id | string | Optional |  | 成交记录 ID  
create_time | number(double) | Optional |  | 成交时间  
contract | string | Optional |  | 合约标识  
order_id | string | Optional |  | 成交记录关联订单 ID  
size | string | Optional |  | 成交数量  
close_size | string | Optional |  | 平仓数量:  
  
close_size=0 && size＞0 开多  
close_size=0 && size＜0 开空  
close_size>0 && size>0 && size <= close_size 平空  
close_size>0 && size>0 && size > close_size 平空且开多  
close_size<0 && size<0 && size >= close_size 平多  
close_size<0 && size<0 && size < close_size 平多且开空  
price | string | Optional |  | 成交价格  
role | string | Optional | enum: ["taker","maker"] | 成交角色， taker - 吃单, maker - 做单  
text | string | Optional |  | 订单的自定义信息  
fee | string | Optional |  | 成交手续费  
point_fee | string | Optional |  | 成交点卡手续费  
      
    
    {
      "trade_id": "string",
      "create_time": 0,
      "contract": "string",
      "order_id": "string",
      "size": "string",
      "close_size": "string",
      "price": "string",
      "role": "taker",
      "text": "string",
      "fee": "string",
      "point_fee": "string"
    }
    
    

##  InsuranceRecord

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | integer(int64) | Optional |  | 秒 s 精度的 Unix 时间戳  
b | string | Optional |  | 保险基金余额  
      
    
    {
      "t": 0,
      "b": "string"
    }
    
    

##  StopTrailOrder

StopTrailOrder

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID，指定了id就不需要text  
text | string | Optional |  | 自定义文本，如果不指定id，就根据user_id和text终止  
      
    
    {
      "id": 0,
      "text": "string"
    }
    
    

##  TriggerTime

triggerTime

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
triggerTime | integer(int64) | Optional |  | 倒计时结束时的时间戳，毫秒  
      
    
    {
      "triggerTime": "1660039145000"
    }
    
    

##  FuturesADLRiskStates

FuturesADLRiskStates

类型 | 约束  
---|---  
object | required: ["settle","states"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
settle | string | Required |  | 结算货币  
states | object | Required |  | 合约市场与 ADL 风险状态的映射  
  
**states**

合约市场与 ADL 风险状态的映射

类型 | 约束  
---|---  
object |   
  
**states / additionalProperties**

FuturesADLRiskState

类型 | 约束  
---|---  
FuturesADLRiskState | required: ["state","calculated_at_ms"]  
      
    
    {
      "settle": "usdt",
      "states": {
        "property1": {
          "state": "normal",
          "calculated_at_ms": 1786695185345
        },
        "property2": {
          "state": "normal",
          "calculated_at_ms": 1786695185345
        }
      }
    }
    
    

##  FuturesOrderBook

类型 | 约束  
---|---  
object | required: ["asks","bids"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 深度更新 ID，深度每发生一次变化，该 ID 加 1，只有设置 `with_id=true` 时才返回  
current | number(double) | Optional |  | 接口数据返回时间戳  
update | number(double) | Optional |  | 深度变化时间戳  
asks | array | Required |  | 卖方深度列表  
bids | array | Required |  | 买方深度列表  
  
**asks**

卖方深度列表

类型 | 约束  
---|---  
array |   
  
**asks / items**

FuturesOrderBookItem

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
p | string | Optional |  | 价格 (计价货币)  
s | string | Optional |  | 数量  
  
**bids**

买方深度列表

类型 | 约束  
---|---  
array |   
  
**bids / items**

FuturesOrderBookItem

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
p | string | Optional |  | 价格 (计价货币)  
s | string | Optional |  | 数量  
      
    
    {
      "id": 0,
      "current": 0,
      "update": 0,
      "asks": [
        {
          "p": "string",
          "s": "string"
        }
      ],
      "bids": [
        {
          "p": "string",
          "s": "string"
        }
      ]
    }
    
    

##  PositionTimerange

合约仓位详情(历史数据)

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
leverage | string | Optional |  | 杠杆倍数，0代表全仓，正数代表逐仓  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 风险限额的第一档维持保证金率要求  
margin | string | Optional |  | 保证金  
liq_price | string | Optional | readOnly: true | 爆仓价格  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏  
history_pnl | string | Optional | readOnly: true | 已平仓的仓位总盈亏  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
mode | string | Optional |  | 持仓模式。包括：  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数（即 `leverage` 为 0 时）  
entry_price | string | Optional | readOnly: true | 开仓价格  
time | integer(int64) | Optional |  | 时间戳  
      
    
    {
      "contract": "string",
      "size": "string",
      "leverage": "string",
      "risk_limit": "string",
      "leverage_max": "string",
      "maintenance_rate": "string",
      "margin": "string",
      "liq_price": "string",
      "realised_pnl": "string",
      "history_pnl": "string",
      "last_close_pnl": "string",
      "realised_point": "string",
      "history_point": "string",
      "mode": "string",
      "cross_leverage_limit": "string",
      "entry_price": "string",
      "time": 0
    }
    
    

##  TrailOrderDetailResponse

TrailOrderDetailResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

TrailOrderResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order | object | Optional |  | 追踪委托详情  
  
**data / order**

TrailOrder

追踪委托详情

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional | readOnly: true | 委托ID  
user_id | string | Optional | readOnly: true | 用户ID  
user | string | Optional | readOnly: true | 用户ID  
contract | string | Optional |  | 合约名称  
settle | string | Optional |  | 结算货币  
amount | string | Optional |  | 交易数量，单位是张，正数买，负数卖  
is_gte | boolean | Optional |  | true：市场价大于等于激活价时激活，false：小于等于  
activation_price | string | Optional |  | 激活价格，为0表示立即触发  
price_type | integer(int32) | Optional | enum: [0,1,2,3] | 激活价格的类型，0-未知，1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
text | string | Optional |  | 自定义字段  
reduce_only | boolean | Optional |  | 只减仓  
position_related | boolean | Optional |  | 是否和仓位绑定  
created_at | string | Optional | readOnly: true | 创建时间  
activated_at | string | Optional | readOnly: true | 激活时间  
finished_at | string | Optional | readOnly: true | 结束时间  
create_time | string | Optional | readOnly: true | 创建时间  
active_time | string | Optional | readOnly: true | 激活时间  
finish_time | string | Optional | readOnly: true | 结束时间  
reason | string | Optional | readOnly: true | 结束原因  
suborder_text | string | Optional | readOnly: true | 子订单的 text 字段。  
is_dual_mode | boolean | Optional | readOnly: true | 创建委托时是否双向持仓  
trigger_price | string | Optional | readOnly: true | 触发价  
suborder_id | string | Optional | readOnly: true | 子订单 ID。  
side_label | string | Optional | readOnly: true | 订单方向标签，做多/做空/开多/开空/平多/平空  
original_status | integer(int32) | Optional | readOnly: true | 委托状态  
status | string | Optional | enum: ["open","finished"]  
readOnly: true | 简化后的委托状态：open/finished  
position_side_output | string | Optional | readOnly: true | 同 side_label，客户端要求和其他类型订单保持一致  
updated_at | string | Optional | readOnly: true | 更新时间  
extremum_price | string | Optional | readOnly: true | 极值价格  
status_code | string | Optional | readOnly: true | status状态值  
created_at_precise | string | Optional | readOnly: true | 创建时间（高精度，秒.微秒格式）  
finished_at_precise | string | Optional | readOnly: true | 结束时间（高精度，秒.微秒格式）  
activated_at_precise | string | Optional | readOnly: true | 激活时间（高精度，秒.微秒格式）  
status_label | string | Optional | readOnly: true | 状态国际化标签（翻译后的状态文本）  
pos_margin_mode | string | Optional | readOnly: true | 仓位保证金模式 逐仓isolated/全仓cross  
position_mode | string | Optional | readOnly: true | 持仓模式 single、dual和dual_plus  
error_label | string | Optional | readOnly: true | 错误标签  
leverage | string | Optional | readOnly: true | 杠杆  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "order": {
          "id": "string",
          "user_id": "string",
          "user": "string",
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "is_gte": true,
          "activation_price": "string",
          "price_type": 0,
          "price_offset": "string",
          "text": "string",
          "reduce_only": true,
          "position_related": true,
          "created_at": "string",
          "activated_at": "string",
          "finished_at": "string",
          "create_time": "string",
          "active_time": "string",
          "finish_time": "string",
          "reason": "string",
          "suborder_text": "string",
          "is_dual_mode": true,
          "trigger_price": "string",
          "suborder_id": "string",
          "side_label": "string",
          "original_status": 0,
          "status": "open",
          "position_side_output": "string",
          "updated_at": "string",
          "extremum_price": "string",
          "status_code": "string",
          "created_at_precise": "string",
          "finished_at_precise": "string",
          "activated_at_precise": "string",
          "status_label": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "error_label": "string",
          "leverage": "string"
        }
      },
      "timestamp": 0
    }
    
    

##  FuturesPriceTriggeredOrder

合约价格单详情

类型 | 约束  
---|---  
object | required: ["initial","trigger"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
initial | object | Required | required: ["contract","price"] |   
trigger | object | Required | required: ["price","rule"] |   
id | integer(int64) | Optional | readOnly: true | 自动订单 ID  
id_string | string | Optional | readOnly: true | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
user | integer | Optional | readOnly: true | 用户 ID  
create_time | number(double) | Optional | readOnly: true | 创建时间  
finish_time | number(double) | Optional | readOnly: true | 结束时间  
trade_id | integer(int64) | Optional | readOnly: true | 触发后委托单ID  
status | string | Optional | enum: ["open","finished","inactive","invalid"]  
readOnly: true | 订单状态  
  
\- `open`: 活跃中  
\- `finished`: 已结束  
\- `inactive`: 未生效，只针对委托单止盈止损  
\- `invalid`: 无效，只针对委托单止盈止损  
finish_as | string | Optional | enum: ["cancelled","succeeded","failed","expired"]  
readOnly: true | 结束状态，cancelled - 被取消；succeeded - 成功；failed - 失败；expired - 过期  
reason | string | Optional | readOnly: true | 订单结束的附加描述信息  
order_type | string | Optional |  | 止盈止损的类型，包括：  
  
\- `close-long-order`: 委托单止盈止损，平做多仓  
\- `close-short-order`: 委托单止盈止损，平做空仓  
\- `close-long-position`: 仓位止盈止损，用于全部平多仓  
\- `close-short-position`: 仓位止盈止损，用于全部平空仓  
\- `plan-close-long-position`: 仓位计划止盈止损，用于全部平多仓或部分平多仓  
\- `plan-close-short-position`: 仓位计划止盈止损，用于全部平空仓或部分平空仓  
  
其中委托单止盈止损的两种类型只读，不能通过请求传入  
me_order_id | integer(int64) | Optional | readOnly: true | 委托单止盈止损对应的委托 ID  
pos_margin_mode | string | Optional | enum: ["isolated","cross"] | 仓位保证金模式：`isolated`（逐仓）、`cross`（全仓）。  
在简易分仓模式下服务端会返回；写入场景下请仅使用下列取值。  
  
**initial**

类型 | 约束  
---|---  
object | required: ["contract","price"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约标识  
size | integer(int64) | Optional |  | 代表需要平仓的合约张数，全平仓:size=0  
部分平仓:plan-close-short-position size>0   
部分平仓:plan-close-long-position size<0  
amount | string | Optional |  | 同size参数，用于兼容小数,同时存在时以amount为准  
price | string | Required |  | 交易价，当价格为 0 时，表示通过市价方式来下单  
close | boolean | Optional | default: false  
writeOnly: true | 单仓模式全部平仓时,必须设置为true执行平仓操作  
单仓模式部分平仓时/双仓模式下，可以不设置close，或close=false  
tif | string | Optional | enum: ["gtc","ioc"]  
default: "gtc" | Time in force 策略,默认为gtc，市价单当前只支持 ioc 模式市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled  
text | string | Optional |  | 订单的来源，包括：  
  
\- web: 网页  
\- api: API 调用  
\- app: 移动端  
reduce_only | boolean | Optional | default: false | 设置为 true 的时候执行自动减仓操作，设为 true可确保订单不会开新仓，只用于平仓或减仓  
auto_size | string | Optional | writeOnly: true | 单仓模式不需设置auto_size  
双仓模式全部平仓（size=0）时，必须设置auto_size，close_long 平多头， close_short 平空头  
双仓模式部分平仓（size≠0）时，不需设置auto_size  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
  
**trigger**

类型 | 约束  
---|---  
object | required: ["price","rule"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
strategy_type | integer(int32) | Optional | enum: [0,1] | 触发策略  
  
\- 0: 价格触发，即当价格满足条件时触发  
\- 1: 价差触发，即指定 `price_type` 的最近一次价格减去倒数第二个价格的差值  
目前暂时只支持0即最新成交价  
price_type | integer(int32) | Optional | enum: [0,1,2] | 参考价格类型。 0 - 最新成交价，1 - 标记价格，2 - 指数价格  
price | string | Required |  | 价格触发时为价格，价差触发时为价差  
rule | integer(int32) | Required | enum: [1,2] | 价格条件类型  
  
\- 1: 表示根据 `strategy_type` 和 `price_type` 算出的价格大于等于 `Trigger.Price` 时触发，同时Trigger.Price must > last_price  
\- 2: 表示根据 `strategy_type` 和 `price_type` 算出的价格小于等于 `Trigger.Price` 时触发，同时Trigger.Price must < last_price  
expiration | integer | Optional |  | 最长等待触发时间，超时则取消该订单，单位是秒 s  
      
    
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
    
    

##  ContractStat

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional |  | 统计时间  
lsr_taker | number(double) | Optional |  | 多空吃单比  
lsr_account | number(double) | Optional |  | 多空持仓用户比  
long_liq_size | string | Optional |  | 做多爆仓量（张）  
long_liq_amount | number(double) | Optional |  | 做多爆仓量（交易币种）  
long_liq_usd | number(double) | Optional |  | 做多爆仓量（计价币种）  
long_liq_usd_new | number(double) | Optional |  | 做多爆仓量（计价币种，USDT结算公式：long_liq_size _multiplier_ mark_price）  
short_liq_size | string | Optional |  | 做空爆仓量（张）  
short_liq_amount | number(double) | Optional |  | 做空爆仓量（交易币种）  
short_liq_usd | number(double) | Optional |  | 做空爆仓量（计价币种）  
short_liq_usd_new | number(double) | Optional |  | 做空爆仓量（计价币种，USDT结算公式：short_liq_size _multiplier_ mark_price）  
open_interest | string | Optional |  | 总持仓量（张）  
open_interest_usd | number(double) | Optional |  | 总持仓量（计价币种）  
top_lsr_account | number(double) | Optional |  | 大户多空账户比  
top_lsr_size | string | Optional |  | 大户多空持仓比  
mark_price | number(double) | Optional |  | 标记价格  
top_long_size | string | Optional |  | 大户做多持仓量（张）  
top_short_size | string | Optional |  | 大户做空持仓量（张）  
long_taker_size | string | Optional |  | 多头吃单交易量（张）  
short_taker_size | string | Optional |  | 空头吃单交易量（张）  
top_long_account | integer(int64) | Optional |  | 大户做多账户数  
top_short_account | integer(int64) | Optional |  | 大户做空账户数  
long_users | integer(int64) | Optional |  | 多头持仓用户数量  
short_users | integer(int64) | Optional |  | 空头持仓用户数量  
      
    
    {
      "time": 0,
      "lsr_taker": 0,
      "lsr_account": 0,
      "long_liq_size": "string",
      "long_liq_amount": 0,
      "long_liq_usd": 0,
      "long_liq_usd_new": 0,
      "short_liq_size": "string",
      "short_liq_amount": 0,
      "short_liq_usd": 0,
      "short_liq_usd_new": 0,
      "open_interest": "string",
      "open_interest_usd": 0,
      "top_lsr_account": 0,
      "top_lsr_size": "string",
      "mark_price": 0,
      "top_long_size": "string",
      "top_short_size": "string",
      "long_taker_size": "string",
      "short_taker_size": "string",
      "top_long_account": 0,
      "top_short_account": 0,
      "long_users": 0,
      "short_users": 0
    }
    
    

##  FuturesLiquidate

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | integer(int64) | Optional | readOnly: true | 强制平仓时间  
contract | string | Optional | readOnly: true | 合约标识  
leverage | string | Optional | readOnly: true | 杠杆倍数，公共接口无该字段返回  
size | string | Optional | readOnly: true | 仓位大小  
margin | string | Optional | readOnly: true | 保证金，公共接口无该字段返回  
entry_price | string | Optional | readOnly: true | 平均开仓价，公共接口无该字段返回  
liq_price | string | Optional | readOnly: true | 强制平仓价，公共接口无该字段返回  
mark_price | string | Optional | readOnly: true | 市场标记价，公共接口无该字段返回  
order_id | integer(int64) | Optional | readOnly: true | 强平委托ID，公共接口无该字段返回  
order_price | string | Optional | readOnly: true | 强平委托价  
fill_price | string | Optional | readOnly: true | 强平委托吃单平均成交价  
left | string | Optional | readOnly: true | 强平委托挂单大小  
      
    
    {
      "time": 0,
      "contract": "string",
      "leverage": "string",
      "size": "string",
      "margin": "string",
      "entry_price": "string",
      "liq_price": "string",
      "mark_price": "string",
      "order_id": 0,
      "order_price": "string",
      "fill_price": "string",
      "left": "string"
    }
    
    

##  FuturesAccountBook

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
time | number(double) | Optional |  | 时间  
change | string | Optional |  | 变更金额  
balance | string | Optional |  | 变更后账户余额  
type | string | Optional | enum: ["dnw","pnl","fee","refr","fund","point_dnw","point_fee","point_refr","bonus_offset","dividend"] | 变更类型：  
  
\- dnw: 转入转出  
\- pnl: 减仓盈亏  
\- fee: 交易手续费  
\- refr: 推荐人返佣  
\- fund: 资金费用  
\- point_dnw: 点卡转入转出  
\- point_fee: 点卡交易手续费  
\- point_refr: 点卡推荐人返佣  
\- bonus_offset: 体验金抵扣  
\- dividend: 分红派息  
text | string | Optional |  | 注释  
contract | string | Optional |  | 合约标识，只有2023-10-30后的数据才有该字段  
trade_id | string | Optional |  | 成交 id  
id | string | Optional |  | 账户变更记录 id  
      
    
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
    
    

##  FuturesBBOOrder

合约BBO订单详情

类型 | 约束  
---|---  
object | required: ["contract","size","level","direction"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Required |  | 合约标识  
size | integer(int64) | Required |  | 必选。交易数量，正数为买入，负数为卖出。平仓委托则设置为0。  
direction | string | Required |  | 方向，sell取买盘，buy取卖盘。  
iceberg | integer(int64) | Optional |  | 冰山委托显示数量。0为完全不隐藏。注意，隐藏部分成交按照taker收取手续费。  
level | integer(int64) | Required | writeOnly: true | 档位，最大20档  
close | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候执行平仓操作，并且`size`应设置为0  
is_close | boolean | Optional | readOnly: true | 是否为平仓委托。对应请求中的`close`。  
reduce_only | boolean | Optional | default: false  
writeOnly: true | 设置为 true 的时候，为只减仓委托  
is_reduce_only | boolean | Optional | readOnly: true | 是否为只减仓委托。对应请求中的`reduce_only`。  
is_liq | boolean | Optional | readOnly: true | 是否为强制平仓委托  
tif | string | Optional | enum: ["gtc","ioc","poc","fok"]  
default: "gtc" | Time in force 策略，市价单当前只支持 ioc 模式  
  
\- gtc: GoodTillCancelled  
\- ioc: ImmediateOrCancelled，立即成交或者取消，只吃单不挂单  
\- poc: PendingOrCancelled，被动委托，只挂单不吃单  
\- fok: FillOrKill, 完全成交，或者完全取消  
left | integer(int64) | Optional | readOnly: true | 未成交数量  
fill_price | string | Optional | readOnly: true | 成交价  
text | string | Optional |  | 订单自定义信息，用户可以用该字段设置自定义 ID，用户自定义字段必须满足以下条件：  
  
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
tkfr | string | Optional | readOnly: true | 吃单费率  
mkfr | string | Optional | readOnly: true | 做单费率  
refu | integer | Optional | readOnly: true | 推荐人用户 ID  
auto_size | string | Optional | enum: ["close_long","close_short"]  
writeOnly: true | 双仓模式下用于设置平仓的方向，`close_long` 平多头， `close_short` 平空头，需要同时设置 `size` 为 0  
stp_id | integer | Optional | readOnly: true | 订单所属的`STP用户组`id，同一个`STP用户组`内用户之间的订单不允许发生自成交。  
  
1\. 如果撮合时两个订单的 `stp_id` 非 `0` 且相等，则不成交，而是根据 `taker` 的 `stp_act` 执行相应策略。  
2\. 没有设置`STP用户组`成交的订单，`stp_id` 默认返回 `0`。  
stp_act | string | Optional | enum: ["co","cn","cb","-"] | Self-Trading Prevention Action,用户可以用该字段设置自定义限制自成交策略。  
  
1\. 用户在设置加入`STP用户组`后，可以通过传递 `stp_act` 来限制用户发生自成交的策略，没有传递 `stp_act` 默认按照 `cn` 的策略。  
2\. 用户在没有设置加入`STP用户组`时，传递 `stp_act` 参数会报错。  
3\. 用户没有使用 `stp_act` 发生成交的订单，`stp_act` 返回 `-`。  
  
\- cn: Cancel newest,取消新订单，保留老订单  
\- co: Cancel oldest,取消⽼订单，保留新订单  
\- cb: Cancel both,新旧订单都取消  
amend_text | string | Optional | readOnly: true | 用户修改订单时备注的信息  
pid | integer(int64) | Optional | writeOnly: true | 仓位ID  
      
    
    {
      "contract": "string",
      "size": 0,
      "direction": "string",
      "iceberg": 0,
      "level": 0,
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
      "amend_text": "string",
      "pid": 0
    }
    
    

##  FuturesPremiumIndex

每个时间粒度的 K 线数据

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | number(double) | Optional |  | 秒 s 精度的 Unix 时间戳  
c | string | Optional |  | 收盘价  
h | string | Optional |  | 最高价  
l | string | Optional |  | 最低价  
o | string | Optional |  | 开盘价  
      
    
    {
      "t": 0,
      "c": "string",
      "h": "string",
      "l": "string",
      "o": "string"
    }
    
    

##  FuturesLimitRiskTiers

返回某个指定合同下,不同档位的风险限额配置

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
tier | integer(int) | Optional |  | 档位  
risk_limit | string | Optional |  | 风险限额  
initial_rate | string | Optional |  | 初始保证金率  
maintenance_rate | string | Optional |  | 风险限额的第一档维持保证金率要求  
leverage_max | string | Optional |  | 最大杠杆  
contract | string | Optional |  | 市场,仅当市场分页请求时可见  
deduction | string | Optional |  | 维持保证金速算扣减额  
      
    
    {
      "tier": 0,
      "risk_limit": "string",
      "initial_rate": "string",
      "maintenance_rate": "string",
      "leverage_max": "string",
      "contract": "string",
      "deduction": "string"
    }
    
    

##  FuturesIndexConstituents

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
index | string | Optional | readOnly: true | 指数名称  
constituents | array | Optional | readOnly: true | 成分  
  
**constituents**

成分

类型 | 约束  
---|---  
array | readOnly: true  
  
**constituents / items**

IndexConstituent

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
exchange | string | Optional |  | 交易所  
symbols | array | Optional |  | 交易对列表  
  
**constituents / items / symbols**

交易对列表

类型 | 约束  
---|---  
array |   
  
**constituents / items / symbols / items**

类型 | 约束  
---|---  
string |   
      
    
    {
      "index": "string",
      "constituents": [
        {
          "exchange": "string",
          "symbols": []
        }
      ]
    }
    
    

##  FundingRateRecord

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | integer(int64) | Optional |  | 秒 s 精度的 Unix 时间戳  
r | string | Optional |  | 资金费率  
      
    
    {
      "t": 0,
      "r": "string"
    }
    
    

##  FuturesLeverage

返回结果包含Lever字段

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
Lever | string | Optional |  | 杠杆  
      
    
    {
      "Lever": "string"
    }
    
    

##  StopAllChaseOrdersReq

批量终止追逐限价单请求

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional |  | 可选合约名称  
settle | string | Optional |  | 由路径覆盖  
pos_margin_mode | string | Optional |  | 可选保证金模式  
      
    
    {
      "contract": "string",
      "settle": "string",
      "pos_margin_mode": "string"
    }
    
    

##  FuturesADLRiskState

FuturesADLRiskState

类型 | 约束  
---|---  
object | required: ["state","calculated_at_ms"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
state | string | Required | enum: ["normal","warning","adl_risk"] | 市场 ADL 风险状态  
calculated_at_ms | integer(int64) | Required |  | 状态计算时间，Unix 毫秒时间戳  
      
    
    {
      "state": "normal",
      "calculated_at_ms": 1786695185345
    }
    
    

##  FuturesFee

返回结果是map类型，key是市场，value是吃单挂单费率

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
taker_fee | string | Optional | readOnly: true | 吃单费率  
maker_fee | string | Optional | readOnly: true | 挂单费率  
      
    
    {
      "taker_fee": "string",
      "maker_fee": "string"
    }
    
    

##  FuturesTicker

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional |  | 合约标识  
last | string | Optional |  | 最新成交价  
change_percentage | string | Optional |  | 涨跌百分比，跌用负数标识，如 -7.45  
total_size | string | Optional |  | 当前合约总持仓量  
low_24h | string | Optional |  | 最近24小时最低价  
high_24h | string | Optional |  | 最近24小时最高价  
volume_24h | string | Optional |  | 最近24小时成交总量  
volume_24h_btc | string | Optional |  | 最近24小时成交总量，BTC单位(即将废弃，建议使用 `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle`)  
volume_24h_usd | string | Optional |  | 最近24小时成交总量，USD单位(即将废弃，建议使用 `volume_24h_base`, `volume_24h_quote`, `volume_24h_settle`)  
volume_24h_base | string | Optional |  | 最近24小时成交量，以基础货币为单位  
volume_24h_quote | string | Optional |  | 最近24小时成交量，以计价货币为单位  
volume_24h_settle | string | Optional |  | 最近24小时成交量，以结算货币为单位  
mark_price | string | Optional |  | 最近标记价格  
funding_rate | string | Optional |  | 资金费率  
funding_rate_indicative | string | Optional |  | 下一周期预测资金费率（已弃用，改用funding_rate）  
index_price | string | Optional |  | 指数价格  
quanto_base_rate | string | Optional |  | 已废弃  
lowest_ask | string | Optional |  | 最新卖方最低价  
lowest_size | string | Optional |  | 最新卖方最低价的挂单量  
highest_bid | string | Optional |  | 最新买方最高价  
highest_size | string | Optional |  | 最新买方最高价的挂单量  
change_utc0 | string | Optional |  | utc0 涨跌百分比，跌用负数标识，如 -7.45  
change_utc8 | string | Optional |  | utc8 涨跌百分比，跌用负数标识，如 -7.45  
change_price | string | Optional |  | 24h 涨跌额，跌用负数标识，如 -7.45  
change_utc0_price | string | Optional |  | utc0 涨跌额，跌用负数标识，如 -7.45  
change_utc8_price | string | Optional |  | utc8 涨跌额，跌用负数标识，如 -7.45  
      
    
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
      "lowest_ask": "string",
      "lowest_size": "string",
      "highest_bid": "string",
      "highest_size": "string",
      "change_utc0": "string",
      "change_utc8": "string",
      "change_price": "string",
      "change_utc0_price": "string",
      "change_utc8_price": "string"
    }
    
    

##  FuturesOrderAmendment

FuturesOrderAmendment

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
size | string | Optional |  | 新的委托大小。包括已成交委托的部分。  
  
\- 如果小于等于已成交数量，则撤销委托。  
\- 新的委托买卖方向必须跟原有的一致。  
\- 不能修改平仓单的size。  
\- 对于只减仓委托，如果调大size，则可能踢出其他只减仓委托。  
\- 如果不修改价格，则调小size不会影响深度排队，调大size会排到当前价位最后。  
price | string | Optional |  | 新的委托价格。  
amend_text | string | Optional |  | 用户可以备注这次修改的信息。  
text | string | Optional |  | 内部用户可以在text修改信息。  
action_mode | string | Optional |  | 处理模式  
  
下单时根据action_mode返回不同的字段  
  
\- `ACK`: 异步模式，只返回订单关键字段  
\- `RESULT`: 无清算信息  
\- `FULL`: 完整模式（默认）  
      
    
    {
      "size": "string",
      "price": "string",
      "amend_text": "string",
      "text": "string",
      "action_mode": "string"
    }
    
    

##  StopAllChaseOrdersResp

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
orders | array | Optional |  |   
  
**orders**

类型 | 约束  
---|---  
array |   
  
**orders / items**

追逐限价单详情/列表项

类型 | 约束  
---|---  
ChaseOrder |   
      
    
    {
      "orders": [
        {
          "id": "string",
          "user": "string",
          "contract": "string",
          "settle": "string",
          "amount": "string",
          "price_limit": "string",
          "reduce_only": true,
          "text": "string",
          "create_time": 0,
          "finish_time": 0,
          "original_status": 0,
          "status": "string",
          "reason": "string",
          "fill_amount": "string",
          "average_fill_price": "string",
          "suborder_id": "string",
          "is_dual_mode": true,
          "side_label": "string",
          "position_side_output": "string",
          "chase_price": "string",
          "interval_sec": 0,
          "updated_at": 0,
          "suborder_price": "string",
          "suborder_ongoing": true,
          "suborder_finish_as": "string",
          "price_type": 0,
          "price_gap_type": "string",
          "price_gap_value": "string",
          "status_code": "string",
          "create_time_precise": "string",
          "finish_time_precise": "string",
          "pos_margin_mode": "string",
          "position_mode": "string",
          "leverage": "string",
          "error_label": "string"
        }
      ]
    }
    
    

##  MyFuturesTrade

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 成交记录 ID  
create_time | number(double) | Optional |  | 成交时间  
contract | string | Optional |  | 合约标识  
order_id | string | Optional |  | 成交记录关联订单 ID  
size | string | Optional |  | 成交数量  
close_size | string | Optional |  | 平仓数量:  
  
close_size=0 && size＞0 开多  
close_size=0 && size＜0 开空  
close_size>0 && size>0 && size <= close_size 平空  
close_size>0 && size>0 && size > close_size 平空且开多  
close_size<0 && size<0 && size >= close_size 平多  
close_size<0 && size<0 && size < close_size 平多且开空  
price | string | Optional |  | 成交价格  
role | string | Optional | enum: ["taker","maker"] | 成交角色， taker - 吃单, maker - 做单  
text | string | Optional |  | 订单的自定义信息  
fee | string | Optional |  | 成交手续费  
point_fee | string | Optional |  | 成交点卡手续费  
trade_value | string | Optional |  | 成交价值  
      
    
    {
      "id": 0,
      "create_time": 0,
      "contract": "string",
      "order_id": "string",
      "size": "string",
      "close_size": "string",
      "price": "string",
      "role": "taker",
      "text": "string",
      "fee": "string",
      "point_fee": "string",
      "trade_value": "string"
    }
    
    

##  GetChaseOrderDetailResp

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order | ChaseOrder | Optional |  | 追逐限价单详情/列表项  
      
    
    {
      "order": {
        "id": "string",
        "user": "string",
        "contract": "string",
        "settle": "string",
        "amount": "string",
        "price_limit": "string",
        "reduce_only": true,
        "text": "string",
        "create_time": 0,
        "finish_time": 0,
        "original_status": 0,
        "status": "string",
        "reason": "string",
        "fill_amount": "string",
        "average_fill_price": "string",
        "suborder_id": "string",
        "is_dual_mode": true,
        "side_label": "string",
        "position_side_output": "string",
        "chase_price": "string",
        "interval_sec": 0,
        "updated_at": 0,
        "suborder_price": "string",
        "suborder_ongoing": true,
        "suborder_finish_as": "string",
        "price_type": 0,
        "price_gap_type": "string",
        "price_gap_value": "string",
        "status_code": "string",
        "create_time_precise": "string",
        "finish_time_precise": "string",
        "pos_margin_mode": "string",
        "position_mode": "string",
        "leverage": "string",
        "error_label": "string"
      }
    }
    
    

##  ChaseOrder

追逐限价单详情/列表项

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  |   
user | string | Optional |  |   
contract | string | Optional |  |   
settle | string | Optional |  |   
amount | string | Optional |  | 总张数；正买负卖  
price_limit | string | Optional |  |   
reduce_only | boolean | Optional |  |   
text | string | Optional |  |   
create_time | integer(int64) | Optional |  |   
finish_time | integer(int64) | Optional |  |   
original_status | integer | Optional |  | 原始状态枚举  
status | string | Optional |  | 简化状态，如 open / finished  
reason | string | Optional |  |   
fill_amount | string | Optional |  |   
average_fill_price | string | Optional |  |   
suborder_id | string | Optional |  |   
is_dual_mode | boolean | Optional |  |   
side_label | string | Optional |  |   
position_side_output | string | Optional |  |   
chase_price | string | Optional |  |   
interval_sec | integer(uint32) | Optional |  |   
updated_at | integer(int64) | Optional |  |   
suborder_price | string | Optional |  |   
suborder_ongoing | boolean | Optional |  |   
suborder_finish_as | string | Optional |  |   
price_type | integer | Optional |  | PriceType 枚举：1 latest；2 index；3 mark  
price_gap_type | string | Optional |  |   
price_gap_value | string | Optional |  |   
status_code | string | Optional |  |   
create_time_precise | string | Optional |  | 创建时间（秒.微秒）  
finish_time_precise | string | Optional |  |   
pos_margin_mode | string | Optional |  |   
position_mode | string | Optional |  |   
leverage | string | Optional |  |   
error_label | string | Optional |  |   
      
    
    {
      "id": "string",
      "user": "string",
      "contract": "string",
      "settle": "string",
      "amount": "string",
      "price_limit": "string",
      "reduce_only": true,
      "text": "string",
      "create_time": 0,
      "finish_time": 0,
      "original_status": 0,
      "status": "string",
      "reason": "string",
      "fill_amount": "string",
      "average_fill_price": "string",
      "suborder_id": "string",
      "is_dual_mode": true,
      "side_label": "string",
      "position_side_output": "string",
      "chase_price": "string",
      "interval_sec": 0,
      "updated_at": 0,
      "suborder_price": "string",
      "suborder_ongoing": true,
      "suborder_finish_as": "string",
      "price_type": 0,
      "price_gap_type": "string",
      "price_gap_value": "string",
      "status_code": "string",
      "create_time_precise": "string",
      "finish_time_precise": "string",
      "pos_margin_mode": "string",
      "position_mode": "string",
      "leverage": "string",
      "error_label": "string"
    }
    
    

##  StopChaseOrderResp

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order | ChaseOrder | Optional |  | 追逐限价单详情/列表项  
      
    
    {
      "order": {
        "id": "string",
        "user": "string",
        "contract": "string",
        "settle": "string",
        "amount": "string",
        "price_limit": "string",
        "reduce_only": true,
        "text": "string",
        "create_time": 0,
        "finish_time": 0,
        "original_status": 0,
        "status": "string",
        "reason": "string",
        "fill_amount": "string",
        "average_fill_price": "string",
        "suborder_id": "string",
        "is_dual_mode": true,
        "side_label": "string",
        "position_side_output": "string",
        "chase_price": "string",
        "interval_sec": 0,
        "updated_at": 0,
        "suborder_price": "string",
        "suborder_ongoing": true,
        "suborder_finish_as": "string",
        "price_type": 0,
        "price_gap_type": "string",
        "price_gap_value": "string",
        "status_code": "string",
        "create_time_precise": "string",
        "finish_time_precise": "string",
        "pos_margin_mode": "string",
        "position_mode": "string",
        "leverage": "string",
        "error_label": "string"
      }
    }
    
    

##  Contract

合约详情

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
name | string | Optional |  | 合约标识  
type | string | Optional | enum: ["inverse","direct"] | 合约类型, inverse - 反向合约, direct - 正向合约  
quanto_multiplier | string | Optional |  | 合约乘数，表示一张合约的面值为多少个标的物币种  
leverage_min | string | Optional |  | 最小杠杆  
leverage_max | string | Optional |  | 最大杠杆  
maintenance_rate | string | Optional |  | 风险限额的第一档维持保证金率要求  
mark_type | string | Optional | enum: ["internal","index"] | 已废弃  
mark_price | string | Optional |  | 当前标记价格  
index_price | string | Optional |  | 当前指数价格  
last_price | string | Optional |  | 上一次成交价格  
maker_fee_rate | string | Optional |  | 挂单成交的手续费率，负数代表返还后续费  
taker_fee_rate | string | Optional |  | 吃单成交的手续费率  
order_price_round | string | Optional |  | 委托价格最小单位  
mark_price_round | string | Optional |  | 标记价格的最小单位  
funding_rate | string | Optional |  | 当前资金费率  
funding_interval | integer | Optional |  | 资金费率应用间隔，以秒为单位  
funding_next_apply | number(double) | Optional |  | 下次资金费率应用时间  
risk_limit_base | string | Optional |  | 基础风险限额,已废弃  
interest_rate | string | Optional |  | 永续合约资金费率及溢价相关计算中使用的利率参数。以字符串表示的小数比率（如 `0.0003`），与 `funding_rate` 等同为比率而非百分数。  
risk_limit_step | string | Optional |  | 风险限额调整步长,已废弃  
risk_limit_max | string | Optional |  | 合约允许的最大风险限额,已废弃,建议使用/futures/{settle}/risk_limit_tiers来查询风险限额  
order_size_min | string | Optional |  | 最小下单张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数，实际最小张数小于 1 时会显示为 0。  
enable_decimal | boolean | Optional |  | 是否支持小数张数。为 `true` 时，可携带 `X-Gate-Size-Decimal: 1` 提交小数张数。为 `false` 时，合约仅支持整张数量。  
order_size_max | string | Optional |  | 最大下单张数。带 `X-Gate-Size-Decimal: 1` 返回保留小数的字符串。设为 `0` 或省略时返回截去小数部分的整数。  
order_price_deviate | string | Optional |  | 下单价与当前标记价格允许的正负偏移量， 即下单价 `order_price` 需满足如下条件:  
  
abs(order_price - mark_price) <= mark_price * order_price_deviate  
ref_discount_rate | string | Optional |  | 被推荐人享受交易费率折扣  
ref_rebate_rate | string | Optional |  | 推荐人享受交易费率返佣比例  
orderbook_id | integer(int64) | Optional |  | orderbook更新ID  
trade_id | integer(int64) | Optional |  | 当前成交ID  
trade_size | string | Optional |  | 历史累计成交  
position_size | string | Optional |  | 当前做多用户持有仓位总和  
config_change_time | number(double) | Optional |  | 配置最后更新时间  
in_delisting | boolean | Optional |  | `in_delisting=true` 并且position_size>0时候 表示该合约处于下线过渡期  
`in_delisting=true`` 并且position_size=0时候 表示该合约处于下线状态  
orders_limit | integer | Optional |  | 最多挂单数量  
enable_bonus | boolean | Optional |  | 是否支持体验金  
enable_credit | boolean | Optional |  | 该合约是否支持统一账户。  
create_time | number(double) | Optional |  | 表示合约的创建时间  
funding_cap_ratio | string | Optional |  | 已废弃  
status | string | Optional |  | 合约状态 类型包含：prelaunch（预上线）, trading（交易中）,delisting（下架中）, delisted（已下架）, circuit_breaker（熔断)  
launch_time | integer(int64) | Optional |  | 合约开盘时间。  
delisting_time | integer(int64) | Optional |  | 合约进入只减仓状态时间  
delisted_time | integer(int64) | Optional |  | 合约下架时间  
market_order_slip_ratio | string | Optional |  | 合约市价下单支持的最大滑点比率，比率计算以市场最新价格为基准  
market_order_size_max | string | Optional |  | 合约市价下单支持的最大张数，默认值为0，为默认值时取`order_size_max`字段作为最大张数限制  
funding_rate_limit | string | Optional |  | 资金费率上限值  
contract_type | string | Optional |  | 合约分类类型，如 stocks-股票, metals-金属, indices-指数, forex-外汇, commodities-大宗商品等  
funding_impact_value | string | Optional |  | 资金费用深度影响额  
enable_circuit_breaker | boolean | Optional |  | 新开盘的合约是否启动标记价格熔断（如果平台要对某个新开盘的合约市场启动该机制以避免开盘后价格发生大幅波动导致过多爆仓，会提前发公告告知）  
      
    
    {
      "name": "string",
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
      "funding_rate": "string",
      "funding_interval": 0,
      "funding_next_apply": 0,
      "risk_limit_base": "string",
      "interest_rate": "string",
      "risk_limit_step": "string",
      "risk_limit_max": "string",
      "order_size_min": "string",
      "enable_decimal": true,
      "order_size_max": "string",
      "order_price_deviate": "string",
      "ref_discount_rate": "string",
      "ref_rebate_rate": "string",
      "orderbook_id": 0,
      "trade_id": 0,
      "trade_size": "string",
      "position_size": "string",
      "config_change_time": 0,
      "in_delisting": true,
      "orders_limit": 0,
      "enable_bonus": true,
      "enable_credit": true,
      "create_time": 0,
      "funding_cap_ratio": "string",
      "status": "string",
      "launch_time": 0,
      "delisting_time": 0,
      "delisted_time": 0,
      "market_order_slip_ratio": "string",
      "market_order_size_max": "string",
      "funding_rate_limit": "string",
      "contract_type": "string",
      "funding_impact_value": "string",
      "enable_circuit_breaker": true
    }
    
    

##  FuturesCandlestick

每个时间粒度的 K 线数据

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | number(double) | Optional |  | 秒 s 精度的 Unix 时间戳  
v | string | Optional |  | 交易量，只有市场行情的 K 线数据里有该值 (合约张数)  
c | string | Optional |  | 收盘价 (计价货币)  
h | string | Optional |  | 最高价 (计价货币)  
l | string | Optional |  | 最低价 (计价货币)  
o | string | Optional |  | 开盘价 (计价货币)  
sum | string | Optional |  | 交易额，单位是计价货币  
      
    
    {
      "t": 0,
      "v": "string",
      "c": "string",
      "h": "string",
      "l": "string",
      "o": "string",
      "sum": "string"
    }
    
    

##  FuturesTrade

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 成交记录 ID  
create_time | number(double) | Optional |  | 成交时间  
create_time_ms | number(double) | Optional |  | 成交时间，保留 3 位小数的毫秒精度  
contract | string | Optional |  | 合约标识  
size | string | Optional |  | 成交数量  
price | string | Optional |  | 成交价格 (计价货币)  
is_internal | boolean | Optional |  | 已废弃  
      
    
    {
      "id": 0,
      "create_time": 0,
      "create_time_ms": 0,
      "contract": "string",
      "size": "string",
      "price": "string",
      "is_internal": true
    }
    
    

##  Position

合约仓位详情

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
user | integer(int64) | Optional | readOnly: true | 用户ID  
contract | string | Optional | readOnly: true | 合约标识  
size | string | Optional | readOnly: true | 头寸大小  
hedge_status | string | Optional | enum: ["partial_hedged","full_hedged"]  
readOnly: true | 中性策略下仓位的对冲状态。包括：  
  
\- `partial_hedged`: 部分对冲  
\- `full_hedged`: 完全对冲  
hedged_size | string | Optional | readOnly: true | 中性策略下已对冲的仓位数量。  
unhedged_size | string | Optional | readOnly: true | 中性策略下未对冲的仓位数量，计算方式为 `max(abs(size) - abs(hedged_size), 0)`。  
leverage | string | Optional |  | 逐仓模式下的杠杆倍数。如果是0，表示当下为全仓模式。全仓杠杆模式下的倍数请以“cross_leverage_limit”为准。  
risk_limit | string | Optional |  | 风险限额  
leverage_max | string | Optional | readOnly: true | 在当前的仓位规模下，允许可开的最大杠杆倍数。当下仓位规模越大，可开的杠杆倍数越低。  
maintenance_rate | string | Optional | readOnly: true | 当前仓位规模所处的那一档的风险限额的维持保证金率要求。由于仓位维持保证金已启动梯度式计算，该仓位的实际维持保证金率要求以`average_maintenance_rate`为准  
value | string | Optional | readOnly: true | 按结算币种标记价格计算的合约价值  
margin | string | Optional |  | 保证金  
entry_price | string | Optional | readOnly: true | 开仓价格  
liq_price | string | Optional | readOnly: true | 预估强平价，仅提供参考。实际强平触发以仓位保证金率或者账户维持保证金率为准。  
mark_price | string | Optional | readOnly: true | 合约当前标记价格  
initial_margin | string | Optional | readOnly: true | 仓位占用的起始保证金  
maintenance_margin | string | Optional | readOnly: true | 仓位所需的维持保证金  
unrealised_pnl | string | Optional | readOnly: true | 未实现盈亏  
realised_pnl | string | Optional | readOnly: true | 已实现盈亏，该仓位产生的所有平仓结算、资金费结算、手续费支出的资金流水之和  
pnl_pnl | string | Optional | readOnly: true | 已实现盈亏中的平仓结算盈亏  
pnl_fund | string | Optional | readOnly: true | 已实现盈亏中的资金费结算盈亏  
pnl_fee | string | Optional | readOnly: true | 已实现盈亏中的总手续费支出  
history_pnl | string | Optional | readOnly: true | 该合约市场下所有平仓结算盈亏，包括所有历史仓位  
last_close_pnl | string | Optional | readOnly: true | 最近一次平仓的盈亏  
realised_point | string | Optional | readOnly: true | 点卡已实现盈亏  
history_point | string | Optional | readOnly: true | 已平仓的点卡总盈亏  
adl_ranking | integer | Optional | readOnly: true | 自动减仓排名，共1-5个等级，`1` 最高，`5` 最低，特殊情况 `6` 是没有持仓或在爆仓中  
pending_orders | integer | Optional | readOnly: true | 当前未完成委托数量  
close_order | object|null | Optional | nullable: true  
readOnly: true | 当前平仓委托信息，如果没有平仓则为`null`  
mode | string | Optional | enum: ["single","dual_long","dual_short"] | 持仓模式。包括：  
  
\- `single`: 单向持仓模式  
\- `dual_long`: 双向持仓模式下的做多仓位  
\- `dual_short`: 双向持仓模式下的做空仓位  
cross_leverage_limit | string | Optional |  | 全仓模式下的杠杆倍数  
update_time | integer(int64) | Optional | readOnly: true | 最后更新时间  
update_id | integer(int64) | Optional | readOnly: true | 更新id，仓位每更新一次，数值会+1  
open_time | integer(int64) | Optional |  | 开仓时间  
risk_limit_table | string | Optional | readOnly: true | 风险限额梯度表id  
average_maintenance_rate | string | Optional | readOnly: true | 平均维持保证金率  
pid | integer(int64) | Optional | readOnly: true | 分仓仓位 ID。  
pos_margin_mode | string | Optional |  | 仓位保证金模式 isolated - 逐仓, cross - 全仓  
lever | string | Optional |  | 表示仓位当前杠杆，逐仓和全仓都可以该字段表示 逐步替换当前的leverage和cross_leverage_limit  
  
**close_order**

当前平仓委托信息，如果没有平仓则为`null`

类型 | 约束  
---|---  
object|null | nullable: true  
readOnly: true  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 委托ID  
price | string | Optional |  | 委托价格  
is_liq | boolean | Optional |  | 是否为强制平仓  
      
    
    {
      "user": 0,
      "contract": "string",
      "size": "string",
      "hedge_status": "partial_hedged",
      "hedged_size": "string",
      "unhedged_size": "string",
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
      "average_maintenance_rate": "string",
      "pid": 0,
      "pos_margin_mode": "string",
      "lever": "string"
    }
    
    

##  TriggerOrderResponse

TriggerOrderResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Optional |  | 自动订单 ID  
id_string | string | Optional | readOnly: true | 自动订单 ID 的字符串形式，与数值字段 `id` 表示同一笔订单，为 `id` 的十进制字符串，便于在 JavaScript 等环境中避免 int64 精度丢失。  
前端展示订单编号或需要字符串类型唯一标识时建议使用本字段；与 `id` 一一对应。合约价格触发单相关 REST 与 `futures.orders`、`futures.autoorders` 等 WebSocket 推送中的同名字段含义一致。  
      
    
    {
      "id": 0,
      "id_string": "string"
    }
    
    

##  FuturesAccount

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | string | Optional |  | 钱包余额，只适用于经典合约账户。钱包余额为所有历史已发生的资金流水之和，包括历史转入转出、平仓结算、手续费支出等，不包含仓位的未实现盈亏。total = SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund)  
unrealised_pnl | string | Optional |  | 未实现盈亏  
position_margin | string | Optional |  | 已废弃  
order_margin | string | Optional |  | 所有未完成订单的起始保证金  
available | string | Optional |  | 指的是逐仓可用的转出或交易的额度，统一账户下包含授信额度的逐仓可用额度(有包含体验金,体验金无法转出,所以要转出,转出金额需要扣除体验金)  
point | string | Optional |  | 点卡数额  
currency | string | Optional |  | 结算币种  
in_dual_mode | boolean | Optional |  | 是否为双向持仓模式  
enable_credit | boolean | Optional |  | 是否开启统一账户模式  
position_initial_margin | string | Optional |  | 头寸占用的起始保证金，适用于统一账户模式  
maintenance_margin | string | Optional |  | 头寸占用的维持保证金，适用于新经典账户保证金模式和统一账户模式  
bonus | string | Optional |  | 体验金  
enable_evolved_classic | boolean | Optional |  | 已废弃  
cross_order_margin | string | Optional |  | 全仓挂单保证金，适用于新经典账户保证金模式  
cross_initial_margin | string | Optional |  | 全仓初始保证金，适用于新经典账户保证金模式  
cross_maintenance_margin | string | Optional |  | 全仓维持保证金，适用于新经典账户保证金模式  
cross_unrealised_pnl | string | Optional |  | 全仓未实现盈亏，适用于新经典账户保证金模式  
cross_available | string | Optional |  | 全仓可用额度，适用于新经典账户保证金模式  
cross_margin_balance | string | Optional |  | 全仓保证金余额，适用于新经典账户保证金模式  
cross_mmr | string | Optional |  | 全仓维持保证金率，适用于新经典账户保证金模式  
cross_imr | string | Optional |  | 全仓初始保证金率，适用于新经典账户保证金模式  
isolated_position_margin | string | Optional |  | 逐仓仓位保证金，适用于新经典账户保证金模式  
enable_new_dual_mode | boolean | Optional |  | 已废弃  
margin_mode | integer | Optional |  | 保证金模式，0-经典保证金模式，1-跨币种保证金模式，2-组合保证金模式，3-单币种保证金模式  
enable_tiered_mm | boolean | Optional |  | 是否开启梯度式计算维持保证金  
enable_dual_plus | boolean | Optional |  | 是否支持分仓模式  
position_mode | string | Optional |  | 持仓模式 single-单向持仓 dual-双向持仓 dual_plus-分仓  
history | object | Optional |  | 累计统计数据  
  
**history**

累计统计数据

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
dnw | string | Optional |  | 累计转入转出  
pnl | string | Optional |  | 累计交易盈亏  
fee | string | Optional |  | 累计手续费  
refr | string | Optional |  | 累计获取的推荐人返佣  
fund | string | Optional |  | 累计资金费用  
point_dnw | string | Optional |  | 累计点卡转入转出  
point_fee | string | Optional |  | 累计点卡抵扣手续费  
point_refr | string | Optional |  | 累计获取的点卡推荐人返佣  
bonus_dnw | string | Optional |  | 累计体验金转入转出  
bonus_offset | string | Optional |  | 累计体验金抵扣  
cross_settle | string | Optional |  | 代表统一账户模式下，合约账户盈利被结算到现货数值。负数代表从合约结算到现货的，正数代表从现货结算到合约的。此数值为累计值  
      
    
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
      "enable_dual_plus": true,
      "position_mode": "string",
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
        "bonus_offset": "string",
        "cross_settle": "string"
      }
    }
    
    

##  CancelBatchFutureOrdersRequest

订单id数组

类型 | 约束  
---|---  
array |   
  
**items**

类型 | 约束  
---|---  
string |   
      
    
    [
      "string"
    ]
    
    

##  StopChaseOrderReq

终止追逐限价单请求

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托 ID。与 text 二选一  
text | string | Optional |  | 自定义文本。仅当 id 为 0 或未传时必填  
settle | string | Optional |  | 由路径覆盖  
      
    
    {
      "id": "string",
      "text": "string",
      "settle": "string"
    }
    
    

##  UpdateTrailOrder

UpdateTrailOrder

类型 | 约束  
---|---  
object | required: ["id"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer(int64) | Required |  | 委托ID  
amount | string | Optional |  | 交易总数，单位是张，正数表示买，负数表示卖，0表示不修改  
activation_price | string | Optional |  | 激活价格，为0表示立即触发，空表示不修改  
is_gte_str | string | Optional |  | true：市场价大于等于激活价时激活，false：小于等于，空表示不修改  
price_type | integer(int32) | Optional | enum: [0,1,2,3] | 激活价格的类型，不传或者0表示不修改，1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional |  | 回调比例或者价距，比如 `0.1` 或者 `0.1%`，空表示不修改  
      
    
    {
      "id": 0,
      "amount": "string",
      "activation_price": "string",
      "is_gte_str": "string",
      "price_type": 0,
      "price_offset": "string"
    }
    
    

##  BatchFundingRatesResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
contract | string | Optional |  | 合约名称  
data | array | Optional |  | 资金费率数组  
  
**data**

资金费率数组

类型 | 约束  
---|---  
array |   
  
**data / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
t | integer(int64) | Optional |  | 秒 s 精度的 Unix 时间戳  
r | string | Optional |  | 资金费率  
      
    
    {
      "contract": "string",
      "data": [
        {
          "t": 0,
          "r": "string"
        }
      ]
    }
    
    

##  TrailOrderChangeLogResponse

TrailOrderChangeLogResponse

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer(int32) | Optional |  | 状态码，0表示成功  
message | string | Optional |  | 响应消息  
data | object | Optional |  |   
timestamp | integer(int64) | Optional |  | 响应时间戳（毫秒）  
  
**data**

TrailOrderChangeLogData

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
change_log | array | Optional |  |   
  
**data / change_log**

类型 | 约束  
---|---  
array |   
  
**data / change_log / items**

追踪委托改单记录

类型 | 约束  
---|---  
TrailChangeLog |   
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "change_log": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TrailChangeLog

追踪委托改单记录

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
updated_at | string | Optional | readOnly: true | 更新时间  
amount | string | Optional | readOnly: true | 交易数量，单位是张，正数买，负数卖  
is_gte | boolean | Optional | readOnly: true | true：市场价大于等于激活价时激活，false：小于等于  
activation_price | string | Optional | readOnly: true | 激活价格，为0表示立即触发  
price_type | integer(int32) | Optional | enum: [0,1,2,3]  
readOnly: true | 激活价格的类型，0-未知,1-最新价格，2-指数价格，3-标记价格  
price_offset | string | Optional | readOnly: true | 回调比例或者价距，比如 `0.1` 或者 `0.1%`  
is_create | boolean | Optional | readOnly: true | true-委托创建，false-委托修改  
      
    
    {
      "updated_at": "string",
      "amount": "string",
      "is_gte": true,
      "activation_price": "string",
      "price_type": 0,
      "price_offset": "string",
      "is_create": true
    }