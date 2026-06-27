---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/crossex
api_type: Trading
updated_at: 2026-05-27 20:16:54.918928
---

# CrossEx

CrossEx是一个跨交易所交易平台,允许用户通过统一账户在多个交易所(币安、欧易、Gate、Bybit、Kraken)进行交易。CrossEx API提供完整的账户管理、资产划转、下单和仓位管理功能,支持跨交易所操作。

  * REST API BaseURL 实盘交易: `https://api.gateio.ws/api/v4`
  * [帮助中心 ](https://www.gate.com/help/crossex/functional)
  * [跨所交易 ](https://www.gate.com/crossex)

##  查询币对信息

GET`/crossex/rule/symbols`

GET `/crossex/rule/symbols`

_查询币对信息_

查询交易对信息

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 否 | 币对列表，多个以逗号分隔  
示例值:  
BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT  
  
####  详细描述

**symbols** : 币对列表，多个以逗号分隔  
示例值:  
BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Symbol]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» symbol | string | 交易对唯一标识，格式为 ExchangeType_BusinessType_Base_Counter  
» exchange_type | string | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN）  
» business_type | string | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆）  
» state | string | 状态（live 在线 / suspend 暂停）  
» min_size | string | 最小下单数量  
» min_notional | string | 最小下单价值  
» lot_size | string | 数量步长  
» tick_size | string | 价格步长  
» max_num_orders | string | 最大挂单数量  
» max_market_size | string | 市价单最大下单数量  
» max_limit_size | string | 限价单最大下单数量  
» contract_size | string | 合约乘数  
» liquidation_fee | string | 清算费率  
» delist_time | string | 毫秒时间戳，0 表示正常未下架  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/rule/symbols'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/crossex/rule/symbols \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "exchange_type": "BINANCE",
        "business_type": "FUTURE",
        "state": "live",
        "min_size": "1",
        "min_notional": "5",
        "lot_size": "1",
        "tick_size": "0.00010",
        "max_num_orders": "200",
        "max_market_size": "300000",
        "max_limit_size": "2000000",
        "contract_size": "1",
        "liquidation_fee": "0.012500",
        "delist_time": "0"
      },
      {
        "symbol": "OKX_FUTURE_ADA_USDT",
        "exchange_type": "OKX",
        "business_type": "FUTURE",
        "state": "suspend",
        "min_size": "10",
        "min_notional": "0",
        "lot_size": "10",
        "tick_size": "0.0001",
        "max_num_orders": "10",
        "max_market_size": "1000000",
        "max_limit_size": "10000000000",
        "contract_size": "100",
        "liquidation_fee": "0",
        "delist_time": "1762163297615"
      }
    ]
    

##  查询风险限额信息

GET`/crossex/rule/risk_limits`

GET `/crossex/rule/risk_limits`

_查询风险限额信息_

查询合约/杠杆交易对风险限额信息

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 是 | 币对列表，多个以逗号分隔  
示例值:  
BINANCE_FUTURE_ADA_USDT,GATE_MARGIN_ADA_USDT  
  
####  详细描述

**symbols** : 币对列表，多个以逗号分隔  
示例值:  
BINANCE_FUTURE_ADA_USDT,GATE_MARGIN_ADA_USDT

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexRiskLimit | object |   
»» symbol | string |   
»» tiers | array |   
»»» CrossexRiskLimitTier | object |   
»»»» min_risk_limit_value | string | 最小风险限额价值  
»»»» max_risk_limit_value | string | 最大风险限额价值  
»»»» quick_cal_amount | string | 速算额  
»»»» leverage_max | string | 最大杠杆  
»»»» maintenance_rate | string | 维持保证金率  
»»»» tier | string | 档位  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/rule/risk_limits'
    query_param = 'symbols=BINANCE_FUTURE_AAVE_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/crossex/rule/risk_limits?symbols=BINANCE_FUTURE_AAVE_USDT \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "symbol": "BINANCE_FUTURE_BTC_USDT",
        "tiers": [
          {
            "min_risk_limit_value": "0",
            "max_risk_limit_value": "50000",
            "quick_cal_amount": "0",
            "leverage_max": "20",
            "maintenance_rate": "0.004",
            "tier": "1"
          },
          {
            "min_risk_limit_value": "50000",
            "max_risk_limit_value": "100000",
            "quick_cal_amount": "50",
            "leverage_max": "18",
            "maintenance_rate": "0.005",
            "tier": "2"
          }
        ]
      }
    ]
    

##  查询划转币种支持

GET`/crossex/transfers/coin`

GET `/crossex/transfers/coin`

_查询划转币种支持_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
coin | 请求参数 | string | 否 | 指定币种名称查询  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexTransferCoin | object |   
»» coin | string | 币种  
»» min_trans_amount | number | 最小划转数量(需要加上预估手续费)  
»» est_fee | number | 预估手续费  
»» precision | integer | 精度  
»» is_disabled | integer | 是否禁用，0 表示未禁用  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/transfers/coin'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/crossex/transfers/coin \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "coin": "string",
        "min_trans_amount": 0,
        "est_fee": 0,
        "precision": 0,
        "is_disabled": 0
      }
    ]
    

##  查询资金划转历史🔒 需要认证

GET`/crossex/transfers`

GET `/crossex/transfers`

_查询资金划转历史_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
coin | 请求参数 | string | 否 | 指定币种名称查询  
order_id | 请求参数 | string | 否 | 支持查询创建订单时返回的订单ID即tx_id字段，支持用户创建时指定的自定义ID即text字段  
from | 请求参数 | integer | 否 | 查询记录的起始时间  
to | 请求参数 | integer | 否 | 查询记录的结束时间，不指定则默认为当前时间  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量，最大1000  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexTransferRecord | object |   
»» id | string | 订单 ID  
»» text | string | 客户自定义Id  
»» from_account_type | string | 操作的from账户（CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX, SPOT）  
»» to_account_type | string | 操作的to账户（CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX, SPOT）  
»» coin | string | 币种  
»» amount | string | 转账数量，发起请求转账的数量  
»» actual_receive | string | 真实到帐金额（当 status = SUCCESS 时有值，其余状态时为空）  
»» status | string | 划转状态  
\- `FAIL` : 失败  
\- `SUCCESS` : 成功  
\- `PENDING` : 划转执行中  
»» fail_reason | string | 失败原因（当 status = FAIL时有值，其余状态时为空）  
»» create_time | integer | 订单创建时间  
»» update_time | integer | 订单更新时间  
  
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
    
    url = '/crossex/transfers'
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
    url="/crossex/transfers"
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
        "id": "33829017692939266",
        "text": "33829017692939266",
        "from_account_type": "CROSSEX_BINANCE",
        "to_account_type": "CROSSEX_OKX",
        "coin": "BTC",
        "amount": "1.1234567",
        "actual_receive": "1.123",
        "status": "SUCCESS",
        "fail_reason": null,
        "create_time": 1750681141933,
        "update_time": 1750681141933
      },
      {
        "id": "38083797492939266",
        "text": "38083797492939266",
        "from_account_type": "CROSSEX",
        "to_account_type": "SPOT",
        "coin": "USDT",
        "amount": "100",
        "actual_receive": null,
        "status": "FAIL",
        "fail_reason": "Insufficient transferAvailable",
        "create_time": 1750681141933,
        "update_time": 1750681141933
      }
    ]
    

##  资金划转🔒 需要认证

POST`/crossex/transfers`

POST `/crossex/transfers`

_资金划转_

限频：每10秒10次请求

  * 在跨所模式下，划转USDT，`from` & `to`任意一侧必须为`SPOT`， 相应地另一侧应该是`CROSSEX` 如果填写的是`CROSSEX_${exchange_type}`(如`CROSSEX_GATE`)，会默认为你设置为`CROSSEX`
  * 在分所模式下，划转USDT，`from` & `to`任意一侧必须为`CROSSEX_${exchange_type}`，相应地另一侧应该是`SPOT`或者`CROSSEX_${exchange_type}` 如果填写的是`CROSSEX`，会默认为你设置为`CROSSEX_GATE`
  * 划转非USDT币种时，从CrossEx 进行转入或者转出，`from` & `to` 任意一侧都不可以是`CROSSEX`，必须指定为`CROSSEX_${exchange_type}`
  * 划转非USDT币种时，可以进行`CROSSEX_{exchange_type}` 的划转，如from = `CROSSEX_BINANCE` , to = `CROSSEX_GATE`

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexTransferRequest | 否 |   
» coin | body | string | 是 | 币种  
» amount | body | string | 是 | 转账数量  
» from | body | string | 是 | 转入账户: CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX, SPOT  
» to | body | string | 是 | 转出账户: CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX, SPOT  
» text | body | string | 否 | 用户自定义id  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexTransferResponse  
  
### 返回格式

状态码 **200**

_CrossexTransferResponse_

名称 | 类型 | 描述  
---|---|---  
» tx_id | string | 操作单号  
» text | string | 用户自定义订单号  
  
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
    
    url = '/crossex/transfers'
    query_param = ''
    body='{"coin":"USDT","amount":"242.45","from":"SPOT","to":"CROSSEX"}'
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
    url="/crossex/transfers"
    query_param=""
    body_param='{"coin":"USDT","amount":"242.45","from":"SPOT","to":"CROSSEX"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "coin": "USDT",
      "amount": "242.45",
      "from": "SPOT",
      "to": "CROSSEX"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "tx_id": "23453",
      "text": "23453"
    }
    

##  下单🔒 需要认证

POST`/crossex/orders`

POST `/crossex/orders`

_下单_

限频：每10秒100次请求，单个用户的最大挂单数为1,000个

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexOrderRequest | 否 |   
» text | body | string | 否 | 客户定义的订单ID，仅支持字母（a-z）、数字（0-9）、符号（-，_）  
» symbol | body | string | 是 | 唯一标识 Exchange_Business_Base_Counter  
示例：  
如果您想在BINANCE交易所上为ADA/USDT交易对下现货订单，您可以使用这样的唯一标识符：`BINANCE_SPOT_ADA_USDT`;  
如果您想在OKX交易所上为ADA/USDT交易对下U本位永续合约订单，您可以使用这样的唯一标识符：`OKX_FUTURE_ADA_USDT`;  
如果您想在GATE交易所上为ADA/USDT交易对下现货杠杆订单，您可以使用这样的唯一标识符：`GATE_MARGIN_ADA_USDT`;  
如果您想在BYBIT交易所上为ADA/USDT交易对下现货订单，您可以使用这样的唯一标识符：`BYBIT_SPOT_ADA_USDT`;  
如果您想在KRAKEN交易所上为ADA/USDT交易对下合约订单，您可以使用这样的唯一标识符：`KRAKEN_FUTURE_ADA_USD`;  
目前支持三种订单：现货订单、U本位永续合约订单和现货杠杆订单, BYBIT暂不支持现货杠杆订单, KRAKEN暂不支持现货与杠杆订单  
» side | body | string | 是 | BUY, SELL  
» type | body | string | 否 | 订单类型（默认`LIMIT`，支持类型列举：`LIMIT`、`MARKET`）  
» time_in_force | body | string | 否 | 默认GTC，支持类型枚举，`GTC`，`IOC`，`FOK`，`POC`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
» qty | body | string | 否 | 订单数量（强制性，除非现货市价买入）  
» price | body | string | 否 | 限价订单价格（限价订单必须）  
» quote_qty | body | string | 否 | 订单报价数量，现货和杠杆市价买单必传  
» reduce_only | body | string | 否 | 只减仓：`true`或者`false`  
» position_side | body | string | 否 | 仓位方向：`NONE`, `LONG`, `SHORT`  
不传默认单向持仓`NONE`  
  
####  详细描述

**» symbol** : 唯一标识 Exchange_Business_Base_Counter  
示例：  
如果您想在BINANCE交易所上为ADA/USDT交易对下现货订单，您可以使用这样的唯一标识符：`BINANCE_SPOT_ADA_USDT`;  
如果您想在OKX交易所上为ADA/USDT交易对下U本位永续合约订单，您可以使用这样的唯一标识符：`OKX_FUTURE_ADA_USDT`;  
如果您想在GATE交易所上为ADA/USDT交易对下现货杠杆订单，您可以使用这样的唯一标识符：`GATE_MARGIN_ADA_USDT`;  
如果您想在BYBIT交易所上为ADA/USDT交易对下现货订单，您可以使用这样的唯一标识符：`BYBIT_SPOT_ADA_USDT`;  
如果您想在KRAKEN交易所上为ADA/USDT交易对下合约订单，您可以使用这样的唯一标识符：`KRAKEN_FUTURE_ADA_USD`;  
目前支持三种订单：现货订单、U本位永续合约订单和现货杠杆订单, BYBIT暂不支持现货杠杆订单, KRAKEN暂不支持现货与杠杆订单

**» time_in_force** : 默认GTC，支持类型枚举，`GTC`，`IOC`，`FOK`，`POC`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly

**» position_side** : 仓位方向：`NONE`, `LONG`, `SHORT`  
不传默认单向持仓`NONE`

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» side | BUY  
» side | SELL  
» type | LIMIT  
» type | MARKET  
» time_in_force | GTC  
» time_in_force | IOC  
» time_in_force | FOK  
» time_in_force | POC  
» reduce_only | true  
» reduce_only | false  
» position_side | LONG  
» position_side | SHORT  
» position_side | NONE  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrderActionResponse  
  
### 返回格式

状态码 **200**

_CrossexOrderActionResponse_

名称 | 类型 | 描述  
---|---|---  
» order_id | string | 订单号  
» text | string | 用户自定义订单号  
  
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
    
    url = '/crossex/orders'
    query_param = ''
    body='{"symbol":"BINANCE_SPOT_ADA_USDT","side":"BUY","type":"MARKET","quote_qty":"10"}'
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
    url="/crossex/orders"
    query_param=""
    body_param='{"symbol":"BINANCE_SPOT_ADA_USDT","side":"BUY","type":"MARKET","quote_qty":"10"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "symbol": "BINANCE_SPOT_ADA_USDT",
      "side": "BUY",
      "type": "MARKET",
      "quote_qty": "10"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "order_id": "123456",
      "text": "cross-test-1"
    }
    

##  查询订单详情🔒 需要认证

GET`/crossex/orders/{order_id}`

GET `/crossex/orders/{order_id}`

_查询订单详情_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 1\. 支持查询创建订单时返回的订单 ID  
2\. 支持用户创建时指定的自定义 ID（即 text 字段）  
  
####  详细描述

**order_id** : 1. 支持查询创建订单时返回的订单 ID  
2\. 支持用户创建时指定的自定义 ID（即 text 字段）

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrder  
  
### 返回格式

状态码 **200**

_CrossexOrder_

名称 | 类型 | 描述  
---|---|---  
» user_id | string | 用户 ID  
» order_id | string | 订单 ID  
» text | string | 客户自定义订单 ID  
» state | string | 订单状态：  
  
NEW：订单已通过校验，等待发送到交易所  
  
OPEN：订单已挂在交易所订单簿上  
  
PARTIALLY_FILLED：订单已部分成交  
  
FILLED：订单已完全成交  
  
FAIL：CrossEx 内部校验未通过，请查看 reason 字段了解失败原因  
  
REJECT：订单被交易所拒绝，请查看 reason 字段了解失败原因  
» symbol | string | 交易对唯一标识，示例：  
BINANCE_SPOT_BTC_USDT、BINANCE_FUTURE_BTC_USDT  
» side | string | 方向（BUY 买入 / SELL 卖出）  
» type | string | 订单类型（LIMIT 限价 / MARKET 市价）  
» attribute | string | 订单属性（COMMON 普通单 / LIQ 强平接管单 / REDUCE 强平减仓单 / ADL 自动减仓 / SETTLEMENT 下架清算）  
» exchange_type | string | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN）  
» business_type | string | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆）  
» qty | string | 基础货币下单数量  
» quote_qty | string | 报价币种下单数量  
» price | string | 订单价格  
» time_in_force | string | 时效策略（默认 GTC，枚举值：GTC / IOC / FOK / POC）  
» executed_qty | string | 已成交基础货币数量  
» executed_amount | string | 已成交报价币种金额  
» executed_avg_price | string | 已成交均价  
» fee_coin | string | 手续费币种  
» fee | string | 手续费金额  
» reduce_only | string | 是否仅减仓订单（"true" 或 "false"）  
» leverage | string | 订单杠杆倍数  
» reason | string | 失败原因描述  
» last_executed_qty | string | 最新一次成交数量  
» last_executed_price | string | 最新一次成交价格  
» last_executed_amount | string | 最新一次成交金额  
» position_side | string | 仓位方向（NONE 无仓位 / LONG 多仓 / SHORT 空仓）  
» create_time | string | 创建时间  
» update_time | string | 更新时间  
  
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
    
    url = '/crossex/orders/2048522992198912'
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
    url="/crossex/orders/2048522992198912"
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
      "user_id": "10001004",
      "order_id": "2048522992198912",
      "text": "2048522992198912",
      "state": "FILLED",
      "symbol": "BINANCE_SPOT_ADA_USDT",
      "side": "BUY",
      "type": "MARKET",
      "attribute": "COMMON",
      "exchange_type": "BINANCE",
      "business_type": "SPOT",
      "qty": "0",
      "quote_qty": "7",
      "price": "0",
      "time_in_force": "GTC",
      "executed_qty": "12.9",
      "executed_amount": "6.96471",
      "executed_avg_price": "0.5399",
      "fee_coin": "ADA",
      "fee": "0.0129",
      "reduce_only": "false",
      "leverage": "1",
      "reason": "",
      "last_executed_qty": "12.9",
      "last_executed_price": "0.5399",
      "last_executed_amount": "6.96471",
      "position_side": "NONE",
      "create_time": "1750681141933",
      "update_time": "1750681142379"
    }
    

##  改单🔒 需要认证

PUT`/crossex/orders/{order_id}`

PUT `/crossex/orders/{order_id}`

_改单_

限频：每10秒100次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 支持订单id或text改单  
body | body | CrossexOrderUpdateRequest | 否 |   
» qty | body | string | 否 | 修改数量  
» price | body | string | 否 | 修改价格  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrderActionResponse  
  
### 返回格式

状态码 **200**

_CrossexOrderActionResponse_

名称 | 类型 | 描述  
---|---|---  
» order_id | string | 订单号  
» text | string | 用户自定义订单号  
  
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
    
    url = '/crossex/orders/string'
    query_param = ''
    body='{"qty":"20","price":"0.65"}'
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
    url="/crossex/orders/string"
    query_param=""
    body_param='{"qty":"20","price":"0.65"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "qty": "20",
      "price": "0.65"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "order_id": "123",
      "text": "crossx-test-1"
    }
    

##  撤单🔒 需要认证

DELETE`/crossex/orders/{order_id}`

DELETE `/crossex/orders/{order_id}`

_撤单_

限频：每10秒100次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 支持订单id或text撤单  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexOrderActionResponse  
  
### 返回格式

状态码 **200**

_CrossexOrderActionResponse_

名称 | 类型 | 描述  
---|---|---  
» order_id | string | 订单号  
» text | string | 用户自定义订单号  
  
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
    
    url = '/crossex/orders/string'
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
    url="/crossex/orders/string"
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
      "order_id": "123456",
      "text": "crossex-test-1"
    }
    

##  闪兑询价🔒 需要认证

POST`/crossex/convert/quote`

POST `/crossex/convert/quote`

_闪兑询价_

限频：每天100次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexConvertQuoteRequest | 否 |   
» exchange_type | body | string | 是 | 交易所类型  
» from_coin | body | string | 是 | 卖出的资产  
» to_coin | body | string | 是 | 买入的资产名称（OKX, GATE 只允许买入BTC, ETH, USDT, BN 只允许买入USDT）  
» from_amount | body | string | 是 | 卖出的资产数量  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexConvertQuoteResponse  
  
### 返回格式

状态码 **200**

_CrossexConvertQuoteResponse_

名称 | 类型 | 描述  
---|---|---  
» quote_id | string | 报价id  
» valid_ms | string | 有效时间（毫秒时间戳）  
» from_coin | string | 卖出的资产  
» to_coin | string | 买入的资产  
» from_amount | string | 卖出的资产数量  
» to_amount | string | 买入的资产数量  
» price | string | 价格  
  
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
    
    url = '/crossex/convert/quote'
    query_param = ''
    body='{"exchange_type":"GATE","from_coin":"BTC","to_coin":"USDT","from_amount":"0.00008"}'
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
    url="/crossex/convert/quote"
    query_param=""
    body_param='{"exchange_type":"GATE","from_coin":"BTC","to_coin":"USDT","from_amount":"0.00008"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "exchange_type": "GATE",
      "from_coin": "BTC",
      "to_coin": "USDT",
      "from_amount": "0.00008"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "quote_id": "2074460878500352",
      "valid_ms": "5000",
      "from_coin": "USDT",
      "to_coin": "BTC",
      "from_amount": "3",
      "to_amount": "0.000027",
      "price": "0.000009"
    }
    

##  闪兑交易🔒 需要认证

POST`/crossex/convert/orders`

POST `/crossex/convert/orders`

_闪兑交易_

限频：每10秒10次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexConvertOrderRequest | 否 |   
» quote_id | body | string | 是 | 询价ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexConvertOrderResponse  
  
### 返回格式

状态码 **200**

_CrossexConvertOrderResponse_

名称 | 类型 | 描述  
---|---|---  
» order_id | string | 订单号  
» text | string | 订单号(无法自定义)  
  
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
    
    url = '/crossex/convert/orders'
    query_param = ''
    body='{"quote_id":"232321331"}'
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
    url="/crossex/convert/orders"
    query_param=""
    body_param='{"quote_id":"232321331"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "quote_id": "232321331"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "order_id": "123456",
      "text": "123456"
    }
    

##  查询账户资产🔒 需要认证

GET`/crossex/accounts`

GET `/crossex/accounts`

_查询账户资产_

限频：每10秒200次请求 100% <= initial_margin_rate < 110%，禁止划出保证金币种。 initial_margin_rate < 100%，系统自动撤单，只能平仓不能开仓 maintenance_margin_rate <= 100%，系统强制平仓

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
exchange_type | 请求参数 | string | 否 | 交易所。当跨所模式下不用传，当分所模式下必传(BINANCE/OKX/GATE/BYBIT/KRAKEN)  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexAccount  
  
### 返回格式

状态码 **200**

_CrossexAccount_

名称 | 类型 | 描述  
---|---|---  
» user_id | string | 用户id  
» available_margin | string | 可用保证金  
» margin_balance | string | 保证金余额  
» initial_margin | string | 初始保证金  
» maintenance_margin | string | 维持保证金  
» initial_margin_rate | string | 初始保证金率  
» maintenance_margin_rate | string | 维持保证金率  
» position_mode | string | 合约仓位模式  
» account_limit | string | 账户限额  
» create_time | string | 创建时间  
» update_time | string | 更新时间  
» account_mode | string | 账户模式。CROSS_EXCHANGE：跨所模式。ISOLATED_EXCHANGE：分所模式  
» exchange_type | string | 交易所类型。当account_mode为CROSS_EXCHANGE时，必为CROSSEX。否则则为其他交易所  
» assets | array | 资产列表，按交易所与币种维度返回各账户余额、保证金及盈亏明细  
»» CrossexAccountAsset | object |   
»»» user_id | string | 用户id  
»»» coin | string | 币种  
»»» exchange_type | string | 交易所  
»»» balance | string | 余额  
»»» upnl | string | 未结盈亏  
»»» equity | string | 权益（只有USDT才有值，其他资产为0）  
»»» futures_initial_margin | string | 合约初始保证金（只有USDT才有值，其他资产为0）  
»»» futures_maintenance_margin | string | 合约维持保证金（只有USDT才有值，其他资产为0）  
»»» borrowing_initial_margin | string | 杠杆交易初始保证金（只有USDT才有值，其他资产为0）  
»»» borrowing_maintenance_margin | string | 杠杆交易维持保证金（只有USDT才有值，其他资产为0）  
»»» available_balance | string | 可用余额  
»»» liability | string | 负债（仅分所模式下才有意义。跨所模式下始终为0）  
  
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
    
    url = '/crossex/accounts'
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
    url="/crossex/accounts"
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
      "user_id": "123456789",
      "available_margin": "1200",
      "margin_balance": "1200",
      "initial_margin": "500",
      "maintenance_margin": "250",
      "initial_margin_rate": "2.4",
      "maintenance_margin_rate": "4.8",
      "position_mode": "SINGLE",
      "account_limit": "5000",
      "create_time": "1687573845000",
      "update_time": "1687588938000",
      "account_mode": "CROSS_EXCHANGE",
      "exchange_type": "CROSSEX",
      "assets": [
        {
          "user_id": "123456789",
          "coin": "USDT",
          "exchange_type": "BINANCE",
          "balance": "1000",
          "upnl": "200",
          "equity": "1200",
          "futures_initial_margin": "400",
          "futures_maintenance_margin": "130",
          "borrowing_initial_margin": "100",
          "borrowing_maintenance_margin": "120",
          "available_balance": "1000.0",
          "liability": "0"
        }
      ]
    }
    

##  更改账户合约仓位模式或账户模式🔒 需要认证

PUT`/crossex/accounts`

PUT `/crossex/accounts`

_更改账户合约仓位模式或账户模式_

限频：每60秒100次请求，position_mode+exchange_type更改合约仓位模式（当前用户的账户模式为分所时，exchange_type必传）；account_mode更改用户的账户模式。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexAccountUpdateRequest | 否 |   
» position_mode | body | string | 否 | 合约仓位模式（SINGLE/DUAL）  
» account_mode | body | string | 否 | 账户模式（CROSS_EXCHANGE/ISOLATED_EXCHANGE，默认：CROSS_EXCHANGE）  
» exchange_type | body | string | 否 | 交易所（BINANCE/OKX/GATE/BYBIT/KRAKEN/CROSSEX，当账户模式为ISOLATED_EXCHANGE时，修改合约仓位模式必须指定交易所）  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexAccountUpdateResponse  
  
### 返回格式

状态码 **202**

_CrossexAccountUpdateResponse_

名称 | 类型 | 描述  
---|---|---  
» position_mode | string | 请求修改的合约仓位模式（SINGLE/DUAL）  
» account_mode | string | 请求修改的账户模式（CROSS_EXCHANGE/ISOLATED_EXCHANGE，默认：CROSS_EXCHANGE）  
» exchange_type | string | 请求修改的交易所（BINANCE/OKX/GATE/BYBIT/KRAKEN/CROSSEX，当账户模式为ISOLATED_EXCHANGE时，修改合约仓位模式必须指定交易所）  
  
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
    
    url = '/crossex/accounts'
    query_param = ''
    body='{"position_mode":"string","account_mode":"string","exchange_type":"string"}'
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
    url="/crossex/accounts"
    query_param=""
    body_param='{"position_mode":"string","account_mode":"string","exchange_type":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    

> 返回示例

> 202 返回
    
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    

##  查询合约交易对的杠杆倍数🔒 需要认证

GET`/crossex/positions/leverage`

GET `/crossex/positions/leverage`

_查询合约交易对的杠杆倍数_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 否 | 币对列表，多个以逗号分隔  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline  
  
### 返回格式

状态码 **200**

_交易对到杠杆倍数的映射_

名称 | 类型 | 描述  
---|---|---  
» **additionalProperties** | string | 对应交易对的杠杆倍数  
  
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
    
    url = '/crossex/positions/leverage'
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
    url="/crossex/positions/leverage"
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
      "BINANCE_FUTURE_BTC_USDT": "3",
      "OKX_FUTURE_BTC_USDT": "3",
      "GATE_FUTURE_BTC_USDT": "3"
    }
    

##  更改合约交易币对的杠杆倍数🔒 需要认证

POST`/crossex/positions/leverage`

POST `/crossex/positions/leverage`

_更改合约交易币对的杠杆倍数_

限频：每10秒100次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexLeverageRequest | 否 |   
» symbol | body | string | 是 | 交易对  
» leverage | body | string | 是 | 杠杆  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexLeverageResponse  
  
### 返回格式

状态码 **202**

_CrossexLeverageResponse_

名称 | 类型 | 描述  
---|---|---  
» symbol | string | 交易对  
» leverage | string | 请求修改的杠杆倍数  
  
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
    
    url = '/crossex/positions/leverage'
    query_param = ''
    body='{"symbol":"OKX_FUTURE_ADA_USDT","leverage":"1"}'
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
    url="/crossex/positions/leverage"
    query_param=""
    body_param='{"symbol":"OKX_FUTURE_ADA_USDT","leverage":"1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "symbol": "OKX_FUTURE_ADA_USDT",
      "leverage": "1"
    }
    

> 返回示例

> 202 返回
    
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    

##  查询杠杆交易对的杠杆倍数🔒 需要认证

GET`/crossex/margin_positions/leverage`

GET `/crossex/margin_positions/leverage`

_查询杠杆交易对的杠杆倍数_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 否 | 币对列表，多个以逗号分隔  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline  
  
### 返回格式

状态码 **200**

_交易对到杠杆倍数的映射_

名称 | 类型 | 描述  
---|---|---  
» **additionalProperties** | string | 对应交易对的杠杆倍数  
  
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
    
    url = '/crossex/margin_positions/leverage'
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
    url="/crossex/margin_positions/leverage"
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
      "BINANCE_MARGIN_BTC_USDT": "3",
      "OKX_MARGIN_BTC_USDT": "3",
      "GATE_MARGIN_BTC_USDT": "3"
    }
    

##  更改杠杆交易币对的杠杆倍数🔒 需要认证

POST`/crossex/margin_positions/leverage`

POST `/crossex/margin_positions/leverage`

_更改杠杆交易币对的杠杆倍数_

限频：每10秒100次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexLeverageRequest | 否 |   
» symbol | body | string | 是 | 交易对  
» leverage | body | string | 是 | 杠杆  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexLeverageResponse  
  
### 返回格式

状态码 **202**

_CrossexLeverageResponse_

名称 | 类型 | 描述  
---|---|---  
» symbol | string | 交易对  
» leverage | string | 请求修改的杠杆倍数  
  
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
    
    url = '/crossex/margin_positions/leverage'
    query_param = ''
    body='{"symbol":"OKX_MARGIN_ADA_USDT","leverage":"1"}'
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
    url="/crossex/margin_positions/leverage"
    query_param=""
    body_param='{"symbol":"OKX_MARGIN_ADA_USDT","leverage":"1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "symbol": "OKX_MARGIN_ADA_USDT",
      "leverage": "1"
    }
    

> 返回示例

> 202 返回
    
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    

##  完全平仓🔒 需要认证

POST`/crossex/position`

POST `/crossex/position`

_完全平仓_

限频：每天100次请求。自动平仓规则。支持平仓FUTURE仓位或者MARGIN仓位

使用本接口前，需要满足以下前置条件：

  * 当前账户中不存在该symbol的任何挂单。
  * 在满足前置条件的情况下，当系统检测到仓位在满足以下任一限制时：
  * 小于或等于最小名义金额（minNotional）
  * 小于或等于最小下单数量（minSize）

满足条件后，系统将自动生成一笔平仓委托，并对该仓位进行立即的完全平仓处理。 该接口用于避免因订单规模过小而触发无法在交易所下单的问题，确保小额仓位在达到阈值时能够顺利被平掉。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexClosePositionRequest | 否 |   
» symbol | body | string | 是 | 交易币对  
1\. 支持杠杆交易币对, 如 BINANCE_MARGIN_SOL_USDT  
2\. 支持合约交易币对, 如 OKX_FUTURE_ETH_USDT  
» position_side | body | string | 否 | 仓位方向  
1\. 针对杠杆仓位, 必须传递此参数  
2\. 针对合约仓位, 需要根据你的合约持仓方式选择性传递  
  
####  详细描述

**» symbol** : 交易币对  
1\. 支持杠杆交易币对, 如 BINANCE_MARGIN_SOL_USDT  
2\. 支持合约交易币对, 如 OKX_FUTURE_ETH_USDT

**» position_side** : 仓位方向  
1\. 针对杠杆仓位, 必须传递此参数  
2\. 针对合约仓位, 需要根据你的合约持仓方式选择性传递

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexOrderActionResponse  
  
### 返回格式

状态码 **202**

_CrossexOrderActionResponse_

名称 | 类型 | 描述  
---|---|---  
» order_id | string | 订单号  
» text | string | 用户自定义订单号  
  
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
    
    url = '/crossex/position'
    query_param = ''
    body='{"symbol":"BINANCE_FUTURE_SOL_USDT","position_side":"LONG"}'
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
    url="/crossex/position"
    query_param=""
    body_param='{"symbol":"BINANCE_FUTURE_SOL_USDT","position_side":"LONG"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "symbol": "BINANCE_FUTURE_SOL_USDT",
      "position_side": "LONG"
    }
    

> 返回示例

> 202 返回
    
    
    {
      "order_id": "123456",
      "text": "123456"
    }
    

##  查询杠杆币种利率🔒 需要认证

GET`/crossex/interest_rate`

GET `/crossex/interest_rate`

_查询杠杆币种利率_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
coin | 请求参数 | string | 否 | 指定币种名称查询  
exchange_type | 请求参数 | string | 否 | 交易所  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexInterestRate | object |   
»» coin | string | 币种  
»» exchange_type | string | 交易所  
»» hour_interest_rate | string | 小时利率  
»» time | string | 毫秒时间戳  
  
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
    
    url = '/crossex/interest_rate'
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
    url="/crossex/interest_rate"
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
        "coin": "BCH",
        "exchange_type": "GATE",
        "hour_interest_rate": "0.00000485",
        "time": "1763971200000"
      },
      {
        "coin": "ADA",
        "exchange_type": "BINANCE",
        "hour_interest_rate": "0.0000036558334",
        "time": "1763971200000"
      },
      {
        "coin": "BCH",
        "exchange_type": "OKX",
        "hour_interest_rate": "0.00000115",
        "time": "1763971200000"
      }
    ]
    

##  查询用户手续费率🔒 需要认证

GET`/crossex/fee`

GET `/crossex/fee`

_查询用户手续费率_

限频：每10秒200次请求

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

_CrossexFee_

名称 | 类型 | 描述  
---|---|---  
CrossexFee | array |   
» exchange_type | string | 交易所  
» spot_maker_fee | string | 现货Maker费率  
» spot_taker_fee | string | 现货Taker费率  
» future_maker_fee | string | 合约Maker费率  
» future_taker_fee | string | 合约Taker费率  
» special_fee_list | array |   
»» CrossexSpecialFee | object |   
»»» symbol | string | 交易对  
»»» taker_fee_rate | string | Taker费率  
»»» maker_fee_rate | string | Maker费率  
  
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
    
    url = '/crossex/fee'
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
    url="/crossex/fee"
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
        "exchange_type": "BINANCE",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "special_fee_list": []
      },
      {
        "exchange_type": "OKX",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "special_fee_list": [
          {
            "symbol": "OKX_SPOT_FLOW_USDT",
            "taker_fee_rate": "0.0004",
            "maker_fee_rate": "0.0001"
          }
        ]
      },
      {
        "exchange_type": "GATE",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "special_fee_list": []
      },
      {
        "exchange_type": "BYBIT",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "special_fee_list": [
          {
            "symbol": "BYBIT_FUTURE_BLAST_USDT",
            "taker_fee_rate": "0.00029",
            "maker_fee_rate": "0.00006"
          }
        ]
      },
      {
        "exchange_type": "KRAKEN",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022"
      }
    ]
    

##  查询合约仓位🔒 需要认证

GET`/crossex/positions`

GET `/crossex/positions`

_查询合约仓位_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | 请求参数 | string | 否 | 币对  
exchange_type | 请求参数 | string | 否 | 交易所  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexPosition | object |   
»» user_id | string | 用户id  
»» position_id | string | 仓位id  
»» symbol | string | 交易对  
»» position_side | string | 仓位方向  
»» initial_margin | string | 初始保证金  
»» maintenance_margin | string | 维持保证金  
»» position_qty | string | 仓位数量  
»» position_value | string | 仓位价值  
»» upnl | string | 未结盈亏  
»» upnl_rate | string | 未结盈亏比  
»» entry_price | string | 仓位入场均价  
»» mark_price | string | 标记价格  
»» leverage | string | 仓位杠杆  
»» max_leverage | string | 最大杠杆  
»» risk_limit | string | 风险限额  
»» fee | string | 仓位手续费  
»» funding_fee | string | 仓位资金费  
»» funding_time | string | 仓位资金费收取时间（0代表还未收取过）  
»» create_time | string | 仓位创建时间  
»» update_time | string | 仓位更新时间  
»» closed_pnl | string | 已结盈亏  
  
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
    
    url = '/crossex/positions'
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
    url="/crossex/positions"
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
        "user_id": "10001004",
        "position_id": "20062926505289216",
        "symbol": "OKX_FUTURE_ADA_USDT",
        "position_side": "LONG",
        "initial_margin": "5.79934625",
        "maintenance_margin": "0.06229625",
        "position_qty": "10",
        "position_value": "5.795",
        "upnl": "0.369",
        "upnl_rate": "0.068005897530409141",
        "entry_price": "0.5426",
        "mark_price": "0.5795",
        "leverage": "1",
        "max_leverage": "18",
        "risk_limit": "1",
        "fee": "0.002713",
        "funding_fee": "0",
        "funding_time": "0",
        "create_time": "1750682334273",
        "update_time": "1750730699867",
        "closed_pnl": "12"
      }
    ]
    

##  查询杠杆仓位🔒 需要认证

GET`/crossex/margin_positions`

GET `/crossex/margin_positions`

_查询杠杆仓位_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | 请求参数 | string | 否 | 交易对  
exchange_type | 请求参数 | string | 否 | 交易所  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexMarginPosition | object |   
»» user_id | string | 用户id  
»» position_id | string | 杠杆仓位Id  
»» symbol | string | 币对  
»» position_side | string | 仓位方向  
»» initial_margin | string | 仓位初始保证金  
»» maintenance_margin | string | 仓位维持保证金  
»» asset_qty | string | 仓位资产数量  
»» asset_coin | string | 仓位资产币种  
»» position_value | string | 仓位价值  
»» liability | string | 负债数量  
»» liability_coin | string | 负债币种  
»» interest | string | 已扣利息  
»» max_position_qty | string | 最大持仓量  
»» entry_price | string | 持仓成本价(开仓均价)  
»» index_price | string | 指数价格  
»» upnl | string | 未结盈亏  
»» upnl_rate | string | 未结盈亏比  
»» leverage | string | 开仓杠杆  
»» max_leverage | string | 最大杠杆  
»» create_time | string | 创建时间  
»» update_time | string | 更新时间  
  
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
    
    url = '/crossex/margin_positions'
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
    url="/crossex/margin_positions"
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
        "user_id": "12345",
        "position_id": "20126312530221056",
        "symbol": "BINANCE_MARGIN_ADA_USDT",
        "position_side": "LONG",
        "initial_margin": "0",
        "maintenance_margin": "0",
        "asset_qty": "0",
        "asset_coin": "ADA",
        "position_value": "0",
        "liability": "0.0001708920658",
        "liability_coin": "USDT",
        "interest": "0.0001708920658",
        "max_position_qty": "0",
        "entry_price": "0",
        "index_price": "0.35466844",
        "upnl": "-0.0001708920658",
        "upnl_rate": "-3",
        "leverage": "3",
        "max_leverage": "5",
        "create_time": "1765794740152",
        "update_time": "1766716075010"
      }
    ]
    

##  查询ADL减仓灯🔒 需要认证

GET`/crossex/adl_rank`

GET `/crossex/adl_rank`

_查询ADL减仓灯_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | 请求参数 | string | 是 | 币对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexAdlRank | object |   
»» user_id | string | 用户id  
»» symbol | string | 交易对  
»» crossex_adl_rank | string | crossex减仓灯排名（1-5，数字越大排名越前）  
»» exchange_adl_rank | string | 交易所原始信息（BINANCE：0-4，数字越大越靠前，OKX：0-5，数字越大越靠前，GATE：1-5，数字越小越靠前，BYBIT：0-5，数字越大越靠前）  
  
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
    
    url = '/crossex/adl_rank'
    query_param = 'symbol=BINANCE_FUTURE_ADA_USDT'
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
    url="/crossex/adl_rank"
    query_param="symbol=BINANCE_FUTURE_ADA_USDT"
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
        "user_id": "111",
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "crossex_adl_rank": "1",
        "exchange_adl_rank": "1"
      }
    ]
    

##  查询当前所有挂单🔒 需要认证

GET`/crossex/open_orders`

GET `/crossex/open_orders`

_查询当前所有挂单_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | 请求参数 | string | 否 | 币对  
exchange_type | 请求参数 | string | 否 | 交易所  
business_type | 请求参数 | string | 否 | 业务类型  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [CrossexOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» CrossexOrder | CrossexOrder |   
»» user_id | string | 用户 ID  
»» order_id | string | 订单 ID  
»» text | string | 客户自定义订单 ID  
»» state | string | 订单状态：  
  
NEW：订单已通过校验，等待发送到交易所  
  
OPEN：订单已挂在交易所订单簿上  
  
PARTIALLY_FILLED：订单已部分成交  
  
FILLED：订单已完全成交  
  
FAIL：CrossEx 内部校验未通过，请查看 reason 字段了解失败原因  
  
REJECT：订单被交易所拒绝，请查看 reason 字段了解失败原因  
»» symbol | string | 交易对唯一标识，示例：  
BINANCE_SPOT_BTC_USDT、BINANCE_FUTURE_BTC_USDT  
»» side | string | 方向（BUY 买入 / SELL 卖出）  
»» type | string | 订单类型（LIMIT 限价 / MARKET 市价）  
»» attribute | string | 订单属性（COMMON 普通单 / LIQ 强平接管单 / REDUCE 强平减仓单 / ADL 自动减仓 / SETTLEMENT 下架清算）  
»» exchange_type | string | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN）  
»» business_type | string | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆）  
»» qty | string | 基础货币下单数量  
»» quote_qty | string | 报价币种下单数量  
»» price | string | 订单价格  
»» time_in_force | string | 时效策略（默认 GTC，枚举值：GTC / IOC / FOK / POC）  
»» executed_qty | string | 已成交基础货币数量  
»» executed_amount | string | 已成交报价币种金额  
»» executed_avg_price | string | 已成交均价  
»» fee_coin | string | 手续费币种  
»» fee | string | 手续费金额  
»» reduce_only | string | 是否仅减仓订单（"true" 或 "false"）  
»» leverage | string | 订单杠杆倍数  
»» reason | string | 失败原因描述  
»» last_executed_qty | string | 最新一次成交数量  
»» last_executed_price | string | 最新一次成交价格  
»» last_executed_amount | string | 最新一次成交金额  
»» position_side | string | 仓位方向（NONE 无仓位 / LONG 多仓 / SHORT 空仓）  
»» create_time | string | 创建时间  
»» update_time | string | 更新时间  
  
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
    
    url = '/crossex/open_orders'
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
    url="/crossex/open_orders"
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
        "user_id": "10001004",
        "order_id": "2048529119934720",
        "client_order_id": "2048529119934720",
        "state": "PARTIALLY_FILLED",
        "symbol": "OKX_SPOT_ADA_USDT",
        "side": "BUY",
        "type": "MARKET",
        "attribute": "COMMON",
        "exchange_type": "OKX",
        "business_type": "SPOT",
        "qty": "6",
        "quote_qty": "6",
        "price": "0",
        "time_in_force": "GTC",
        "executed_qty": "11.0354",
        "executed_amount": "5.99994698",
        "executed_avg_price": "0.5437",
        "fee_coin": "ADA",
        "fee": "0.0110354",
        "reduce_only": "false",
        "leverage": "1",
        "reason": "",
        "last_executed_qty": "11.0354",
        "last_executed_price": "0.5437",
        "last_executed_amount": "5.99994698",
        "position_side": "NONE",
        "create_time": "1750682602377",
        "update_time": "1750682602413"
      }
    ]
    

##  查询订单历史🔒 需要认证

GET`/crossex/history_orders`

GET `/crossex/history_orders`

_查询订单历史_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量  
symbol | 请求参数 | string | 否 | 交易对  
from | 请求参数 | integer | 否 | 起始毫秒时间戳  
to | 请求参数 | integer | 否 | 终止毫秒时间戳  
attributes | 请求参数 | string | 否 | 订单属性（COMMON 普通单 / LIQ 强平接管单 / REDUCE 强平减仓单 / ADL 自动减仓 / SETTLEMENT 下架清算）多个以逗号分隔  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [CrossexOrder]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» CrossexOrder | CrossexOrder |   
»» user_id | string | 用户 ID  
»» order_id | string | 订单 ID  
»» text | string | 客户自定义订单 ID  
»» state | string | 订单状态：  
  
NEW：订单已通过校验，等待发送到交易所  
  
OPEN：订单已挂在交易所订单簿上  
  
PARTIALLY_FILLED：订单已部分成交  
  
FILLED：订单已完全成交  
  
FAIL：CrossEx 内部校验未通过，请查看 reason 字段了解失败原因  
  
REJECT：订单被交易所拒绝，请查看 reason 字段了解失败原因  
»» symbol | string | 交易对唯一标识，示例：  
BINANCE_SPOT_BTC_USDT、BINANCE_FUTURE_BTC_USDT  
»» side | string | 方向（BUY 买入 / SELL 卖出）  
»» type | string | 订单类型（LIMIT 限价 / MARKET 市价）  
»» attribute | string | 订单属性（COMMON 普通单 / LIQ 强平接管单 / REDUCE 强平减仓单 / ADL 自动减仓 / SETTLEMENT 下架清算）  
»» exchange_type | string | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN）  
»» business_type | string | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆）  
»» qty | string | 基础货币下单数量  
»» quote_qty | string | 报价币种下单数量  
»» price | string | 订单价格  
»» time_in_force | string | 时效策略（默认 GTC，枚举值：GTC / IOC / FOK / POC）  
»» executed_qty | string | 已成交基础货币数量  
»» executed_amount | string | 已成交报价币种金额  
»» executed_avg_price | string | 已成交均价  
»» fee_coin | string | 手续费币种  
»» fee | string | 手续费金额  
»» reduce_only | string | 是否仅减仓订单（"true" 或 "false"）  
»» leverage | string | 订单杠杆倍数  
»» reason | string | 失败原因描述  
»» last_executed_qty | string | 最新一次成交数量  
»» last_executed_price | string | 最新一次成交价格  
»» last_executed_amount | string | 最新一次成交金额  
»» position_side | string | 仓位方向（NONE 无仓位 / LONG 多仓 / SHORT 空仓）  
»» create_time | string | 创建时间  
»» update_time | string | 更新时间  
  
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
    
    url = '/crossex/history_orders'
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
    url="/crossex/history_orders"
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
        "user_id": "10001004",
        "order_id": "2048522992198912",
        "text": "2048522992198912",
        "state": "FILLED",
        "symbol": "BINANCE_SPOT_ADA_USDT",
        "side": "BUY",
        "type": "MARKET",
        "attribute": "COMMON",
        "exchange_type": "BINANCE",
        "business_type": "SPOT",
        "qty": "0",
        "quote_qty": "7",
        "price": "0",
        "time_in_force": "GTC",
        "executed_qty": "12.9",
        "executed_amount": "6.96471",
        "executed_avg_price": "0.5399",
        "fee_coin": "ADA",
        "fee": "0.0129",
        "reduce_only": "false",
        "leverage": "1",
        "reason": "",
        "last_executed_qty": "12.9",
        "last_executed_price": "0.5399",
        "last_executed_amount": "6.96471",
        "position_side": "NONE",
        "create_time": "1750681141933",
        "update_time": "1750681142379"
      }
    ]
    

##  查询合约仓位历史🔒 需要认证

GET`/crossex/history_positions`

GET `/crossex/history_positions`

_查询合约仓位历史_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量，最大1000  
symbol | 请求参数 | string | 否 | 交易对  
from | 请求参数 | integer | 否 | 起始毫秒时间戳  
to | 请求参数 | integer | 否 | 终止毫秒时间戳  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexHistoricalPosition | object |   
»» position_id | string | 仓位id  
»» user_id | string | 用户id  
»» symbol | string | 交易对  
»» closed_type | string | 平仓类型（PARTIAL_CLOSED 部分成交，COMPLETE_CLOSED 完全成交）  
»» closed_pnl | string | 平仓盈亏  
»» closed_pnl_rate | string | 平仓盈亏率  
»» open_avg_price | string | 开仓均价  
»» closed_avg_price | string | 平仓均价  
»» max_position_qty | string | 最大持仓量  
»» closed_qty | string | 平仓量  
»» closed_value | string | 平仓价值  
»» fee | string | 仓位累计手续费  
»» liq_fee | string | 强平费  
»» funding_fee | string | 资金费  
»» position_side | string | 平仓前仓位方向  
»» position_mode | string | 平仓时的仓位模式  
»» leverage | string | 平仓时的杠杆  
»» business_type | string | 业务类型  
»» create_time | string | 创建时间  
»» update_time | string | 更新时间  
  
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
    
    url = '/crossex/history_positions'
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
    url="/crossex/history_positions"
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
        "position_id": "20064013106942976",
        "user_id": "12345678",
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "closed_type": "COMPLETE_CLOSED",
        "closed_pnl": "-0.001",
        "closed_pnl_rate": "-0.001",
        "open_avg_price": "0.5598",
        "closed_avg_price": "0.5597",
        "max_position_qty": "10",
        "closed_qty": "10",
        "closed_value": "5.597",
        "fee": "0.0055975",
        "liq_fee": "0",
        "funding_fee": "0",
        "position_side": "LONG",
        "position_mode": "DUAL",
        "leverage": "1",
        "create_time": "1750941400632",
        "update_time": "1750941402661"
      }
    ]
    

##  查询杠杆仓位历史🔒 需要认证

GET`/crossex/history_margin_positions`

GET `/crossex/history_margin_positions`

_查询杠杆仓位历史_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量，最大1000  
symbol | 请求参数 | string | 否 | 交易对  
from | 请求参数 | integer | 否 | 起始毫秒时间戳  
to | 请求参数 | integer | 否 | 终止毫秒时间戳  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexHistoricalMarginPosition | object |   
»» position_id | string | 仓位id  
»» user_id | string | 用户id  
»» symbol | string | 交易对  
»» closed_type | string | 平仓类型（PARTIAL_CLOSED 部分成交，COMPLETE_CLOSED 完全成交）  
»» closed_pnl | string | 平仓盈亏  
»» closed_pnl_rate | string | 平仓盈亏率  
»» open_avg_price | string | 开仓均价  
»» closed_avg_price | string | 平仓均价  
»» max_position_qty | string | 最大持仓量  
»» closed_qty | string | 平仓量  
»» closed_value | string | 平仓价值  
»» liq_fee | string | 强平费  
»» position_side | string | 平仓前仓位方向  
»» leverage | string | 平仓时的杠杆  
»» interest | string | 已扣总利息  
»» business_type | string | 仓位业务类型  
»» create_time | string | 创建时间  
»» update_time | string | 更新时间  
  
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
    
    url = '/crossex/history_margin_positions'
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
    url="/crossex/history_margin_positions"
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
        "position_id": "20064013106942976",
        "user_id": "12345678",
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "closed_type": "COMPLETE_CLOSED",
        "closed_pnl": "-0.001",
        "closed_pnl_rate": "-0.001",
        "open_avg_price": "0.5598",
        "closed_avg_price": "0.5597",
        "max_position_qty": "10",
        "closed_qty": "10",
        "closed_value": "5.597",
        "liq_fee": "0",
        "position_side": "LONG",
        "leverage": "1",
        "interest": "0.2",
        "business_type": "MARGIN",
        "create_time": "1750941400632",
        "update_time": "1750941402661"
      }
    ]
    

##  查询杠杆扣息历史🔒 需要认证

GET`/crossex/history_margin_interests`

GET `/crossex/history_margin_interests`

_查询杠杆扣息历史_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | 请求参数 | string | 否 | 交易对  
from | 请求参数 | integer | 否 |   
to | 请求参数 | integer | 否 |   
page | 请求参数 | integer | 否 |   
limit | 请求参数 | integer | 否 |   
exchange_type | 请求参数 | string | 否 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexMarginInterestRecord | object |   
»» userId | string | 用户Id  
»» symbol | string | 币对  
»» interest_id | string | 扣息Id  
»» liability_id | string | 负债源Id,可以是挂单Id 或者仓位Id  
»» liability | string | 负债数量  
»» liability_coin | string | 负债币种  
»» interest | string | 利息  
»» interest_rate | string | 利率  
»» interest_type | string | 扣息类型（`PERIODIC_POSITION` 整点仓位收息，`PERIODIC_OPEN_ORDER` 整点挂单收息，`IMMEDIATE_OPEN_ORDER` 开单收息，`PERIODIC_ISOLATED` 整点负债收息）  
»» create_time | string | 创建时间  
»» exchange_type | string | 交易所  
  
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
    
    url = '/crossex/history_margin_interests'
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
    url="/crossex/history_margin_interests"
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
        "user_id": "2124575357",
        "symbol": "OKX_MARGIN_WLD_USDT",
        "interest_id": "2115944013038336",
        "liability_id": "2115944013038080",
        "liability": "2",
        "liability_coin": "USDT",
        "interest": "0.00000732",
        "interest_rate": "0.00000366",
        "interest_type": "IMMEDIATE_OPEN_ORDER",
        "create_time": "1766755565807",
        "exchange_type": "OKX"
      },
      {
        "user_id": "2124575357",
        "symbol": "OKX_MARGIN_WLD_USDT",
        "interest_id": "2114666587422976",
        "liability_id": "2114666587422720",
        "liability": "2",
        "liability_coin": "USDT",
        "interest": "0.00000732",
        "interest_rate": "0.00000366",
        "interest_type": "IMMEDIATE_OPEN_ORDER",
        "create_time": "1766451003780",
        "exchange_type": ""
      }
    ]
    

##  查询成交历史🔒 需要认证

GET`/crossex/history_trades`

GET `/crossex/history_trades`

_查询成交历史_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量，最大1000  
symbol | 请求参数 | string | 否 | 交易对  
from | 请求参数 | integer | 否 | 起始毫秒时间戳  
to | 请求参数 | integer | 否 | 终止毫秒时间戳  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexTrade | object |   
»» user_id | string | 用户ID  
»» transaction_id | string | 成交记录ID  
»» order_id | string | 订单ID  
»» text | string | 用户订单号  
»» symbol | string | 交易对  
»» exchange_type | string | 交易所  
»» business_type | string | 业务类型  
»» side | string | 买卖方向  
»» qty | string | 成交数量  
»» price | string | 成交价格  
»» fee | string | 手续费  
»» fee_coin | string | 手续费币种  
»» fee_rate | string | 手续费率  
»» match_role | string | 成交角色  
»» rpnl | string | 实现盈亏  
»» position_mode | string | 仓位模式  
»» position_side | string | 仓位方向  
»» create_time | string | 创建时间  
  
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
    
    url = '/crossex/history_trades'
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
    url="/crossex/history_trades"
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
        "user_id": "3511316454450547",
        "transaction_id": "2049614605858560",
        "order_id": "2049614605857536",
        "text": "2049614605857536",
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "exchange_type": "BINANCE",
        "business_type": "FUTURE",
        "side": "SELL",
        "qty": "10",
        "price": "0.5597",
        "fee": "0.002798500000000000",
        "fee_coin": "USDT",
        "fee_rate": "0.0005",
        "match_role": "MAKER",
        "rpnl": "-0.001",
        "position_mode": "BOTH",
        "position_side": "LONG",
        "create_time": "1750941402661"
      }
    ]
    

##  查询账户资产变更历史🔒 需要认证

GET`/crossex/account_book`

GET `/crossex/account_book`

_查询账户资产变更历史_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量，最大1000  
coin | 请求参数 | string | 否 | 指定币种名称查询  
statement_type | 请求参数 | string | 否 | 账单流水类型  
from | 请求参数 | integer | 否 | 起始毫秒时间戳  
to | 请求参数 | integer | 否 | 终止毫秒时间戳  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexAccountBookRecord | object |   
»» id | string | 账户变更记录ID  
»» user_id | string | 用户ID  
»» business_id | string | 业务ID  
»» statement_type | string | 账单流水类型  
»» exchange_type | string | 交易所  
»» coin | string | 币种  
»» change | string | 变更金额（正数表示转入，负数表示转出）  
»» balance | string | 变更后账户余额  
»» create_time | string | 创建时间  
  
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
    
    url = '/crossex/account_book'
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
    url="/crossex/account_book"
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
        "id": "121",
        "user_id": "12345678",
        "business_id": "20818182821",
        "statement_type": "TRADING_FEE",
        "exchange_type": "BINANCE",
        "coin": "USDT",
        "change": "-0.002",
        "balance": "81",
        "create_time": "1750941402661"
      }
    ]
    

##  查询币种折扣率🔒 需要认证

GET`/crossex/coin_discount_rate`

GET `/crossex/coin_discount_rate`

_查询币种折扣率_

Rate Limit: 200 requests per 10 seconds

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
coin | 请求参数 | string | 否 | 指定币种名称查询  
exchange_type | 请求参数 | string | 否 | OKX/GATE/BINANCE/BYBIT/KRAKEN  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexCoinDiscountRate | object |   
»» coin | string | 币种  
»» exchange_type | string | 交易所  
»» tier | string | 等级  
»» min_value | string | 价值最小值  
»» max_value | string | 价值最大值  
»» discount_rate | string | 折扣率  
  
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
    
    url = '/crossex/coin_discount_rate'
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
    url="/crossex/coin_discount_rate"
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
        "coin": "SOL",
        "exchange_type": "GATE",
        "tier": "1",
        "min_value": "0",
        "max_value": "10000",
        "discount_rate": "0.95"
      },
      {
        "coin": "SOL",
        "exchange_type": "GATE",
        "tier": "2",
        "min_value": "10000",
        "max_value": "20000",
        "discount_rate": "0.93"
      },
      {
        "coin": "SOL",
        "exchange_type": "GATE",
        "tier": "3",
        "min_value": "20000",
        "max_value": "30000",
        "discount_rate": "0.2"
      }
    ]
    

#  模型

##  CrossexOrderActionResponse

_CrossexOrderActionResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | true | none | 订单号  
text | string | true | none | 用户自定义订单号  
      
    
    {
      "order_id": "string",
      "text": "string"
    }
    
    

##  CrossexTransferRequest

_资金划转请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
coin | string | true | none | 币种  
amount | string | true | none | 转账数量  
from | string | true | none | 转入账户: CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX, SPOT  
to | string | true | none | 转出账户: CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX, SPOT  
text | string | false | none | 用户自定义id  
      
    
    {
      "coin": "string",
      "amount": "string",
      "from": "string",
      "to": "string",
      "text": "string"
    }
    
    

##  CrossexAccountUpdateRequest

_更改账户请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
position_mode | string | false | none | 合约仓位模式（SINGLE/DUAL）  
account_mode | string | false | none | 账户模式（CROSS_EXCHANGE/ISOLATED_EXCHANGE，默认：CROSS_EXCHANGE）  
exchange_type | string | false | none | 交易所（BINANCE/OKX/GATE/BYBIT/KRAKEN/CROSSEX，当账户模式为ISOLATED_EXCHANGE时，修改合约仓位模式必须指定交易所）  
      
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    
    

##  CrossexTransferResponse

_CrossexTransferResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
tx_id | string | true | none | 操作单号  
text | string | true | none | 用户自定义订单号  
      
    
    {
      "tx_id": "string",
      "text": "string"
    }
    
    

##  CrossexClosePositionRequest

_完全平仓请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | 交易币对  
1\. 支持杠杆交易币对, 如 BINANCE_MARGIN_SOL_USDT  
2\. 支持合约交易币对, 如 OKX_FUTURE_ETH_USDT  
position_side | string | false | none | 仓位方向  
1\. 针对杠杆仓位, 必须传递此参数  
2\. 针对合约仓位, 需要根据你的合约持仓方式选择性传递  
      
    
    {
      "symbol": "string",
      "position_side": "string"
    }
    
    

##  CrossexConvertQuoteResponse

_CrossexConvertQuoteResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
quote_id | string | true | none | 报价id  
valid_ms | string | true | none | 有效时间（毫秒时间戳）  
from_coin | string | true | none | 卖出的资产  
to_coin | string | true | none | 买入的资产  
from_amount | string | true | none | 卖出的资产数量  
to_amount | string | true | none | 买入的资产数量  
price | string | true | none | 价格  
      
    
    {
      "quote_id": "string",
      "valid_ms": "string",
      "from_coin": "string",
      "to_coin": "string",
      "from_amount": "string",
      "to_amount": "string",
      "price": "string"
    }
    
    

##  Symbol

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | 交易对唯一标识，格式为 ExchangeType_BusinessType_Base_Counter  
exchange_type | string | true | none | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN）  
business_type | string | true | none | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆）  
state | string | true | none | 状态（live 在线 / suspend 暂停）  
min_size | string | true | none | 最小下单数量  
min_notional | string | true | none | 最小下单价值  
lot_size | string | true | none | 数量步长  
tick_size | string | true | none | 价格步长  
max_num_orders | string | true | none | 最大挂单数量  
max_market_size | string | true | none | 市价单最大下单数量  
max_limit_size | string | true | none | 限价单最大下单数量  
contract_size | string | true | none | 合约乘数  
liquidation_fee | string | true | none | 清算费率  
delist_time | string | true | none | 毫秒时间戳，0 表示正常未下架  
      
    
    {
      "symbol": "string",
      "exchange_type": "string",
      "business_type": "string",
      "state": "string",
      "min_size": "string",
      "min_notional": "string",
      "lot_size": "string",
      "tick_size": "string",
      "max_num_orders": "string",
      "max_market_size": "string",
      "max_limit_size": "string",
      "contract_size": "string",
      "liquidation_fee": "string",
      "delist_time": "string"
    }
    
    

##  CrossexConvertQuoteRequest

_闪兑询价请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
exchange_type | string | true | none | 交易所类型  
from_coin | string | true | none | 卖出的资产  
to_coin | string | true | none | 买入的资产名称（OKX, GATE 只允许买入BTC, ETH, USDT, BN 只允许买入USDT）  
from_amount | string | true | none | 卖出的资产数量  
      
    
    {
      "exchange_type": "string",
      "from_coin": "string",
      "to_coin": "string",
      "from_amount": "string"
    }
    
    

##  CrossexLeverageResponse

_CrossexLeverageResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | 交易对  
leverage | string | true | none | 请求修改的杠杆倍数  
      
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    
    

##  CrossexOrderUpdateRequest

_改单请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
qty | string | false | none | 修改数量  
price | string | false | none | 修改价格  
      
    
    {
      "qty": "string",
      "price": "string"
    }
    
    

##  CrossexAccount

_CrossexAccount_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user_id | string | true | none | 用户id  
available_margin | string | true | none | 可用保证金  
margin_balance | string | true | none | 保证金余额  
initial_margin | string | true | none | 初始保证金  
maintenance_margin | string | true | none | 维持保证金  
initial_margin_rate | string | true | none | 初始保证金率  
maintenance_margin_rate | string | true | none | 维持保证金率  
position_mode | string | true | none | 合约仓位模式  
account_limit | string | false | none | 账户限额  
create_time | string | true | none | 创建时间  
update_time | string | true | none | 更新时间  
account_mode | string | false | none | 账户模式。CROSS_EXCHANGE：跨所模式。ISOLATED_EXCHANGE：分所模式  
exchange_type | string | false | none | 交易所类型。当account_mode为CROSS_EXCHANGE时，必为CROSSEX。否则则为其他交易所  
assets | array | true | none | 资产列表，按交易所与币种维度返回各账户余额、保证金及盈亏明细  
» CrossexAccountAsset | object | false | none | none  
»» user_id | string | false | none | 用户id  
»» coin | string | false | none | 币种  
»» exchange_type | string | false | none | 交易所  
»» balance | string | false | none | 余额  
»» upnl | string | false | none | 未结盈亏  
»» equity | string | false | none | 权益（只有USDT才有值，其他资产为0）  
»» futures_initial_margin | string | false | none | 合约初始保证金（只有USDT才有值，其他资产为0）  
»» futures_maintenance_margin | string | false | none | 合约维持保证金（只有USDT才有值，其他资产为0）  
»» borrowing_initial_margin | string | true | none | 杠杆交易初始保证金（只有USDT才有值，其他资产为0）  
»» borrowing_maintenance_margin | string | true | none | 杠杆交易维持保证金（只有USDT才有值，其他资产为0）  
»» available_balance | string | false | none | 可用余额  
»» liability | string | false | none | 负债（仅分所模式下才有意义。跨所模式下始终为0）  
      
    
    {
      "user_id": "string",
      "available_margin": "string",
      "margin_balance": "string",
      "initial_margin": "string",
      "maintenance_margin": "string",
      "initial_margin_rate": "string",
      "maintenance_margin_rate": "string",
      "position_mode": "string",
      "account_limit": "string",
      "create_time": "string",
      "update_time": "string",
      "account_mode": "string",
      "exchange_type": "string",
      "assets": [
        {
          "user_id": "string",
          "coin": "string",
          "exchange_type": "string",
          "balance": "string",
          "upnl": "string",
          "equity": "string",
          "futures_initial_margin": "string",
          "futures_maintenance_margin": "string",
          "borrowing_initial_margin": "string",
          "borrowing_maintenance_margin": "string",
          "available_balance": "string",
          "liability": "string"
        }
      ]
    }
    
    

##  CrossexConvertOrderResponse

_CrossexConvertOrderResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | true | none | 订单号  
text | string | true | none | 订单号(无法自定义)  
      
    
    {
      "order_id": "string",
      "text": "string"
    }
    
    

##  CrossexLeverageRequest

_更改杠杆请求体（合约/杠杆通用）_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | 交易对  
leverage | string | true | none | 杠杆  
      
    
    {
      "symbol": "string",
      "leverage": "string"
    }
    
    

##  CrossexOrderRequest

_下单请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
text | string | false | none | 客户定义的订单ID，仅支持字母（a-z）、数字（0-9）、符号（-，_）  
symbol | string | true | none | 唯一标识 Exchange_Business_Base_Counter  
示例：  
如果您想在BINANCE交易所上为ADA/USDT交易对下现货订单，您可以使用这样的唯一标识符：`BINANCE_SPOT_ADA_USDT`;  
如果您想在OKX交易所上为ADA/USDT交易对下U本位永续合约订单，您可以使用这样的唯一标识符：`OKX_FUTURE_ADA_USDT`;  
如果您想在GATE交易所上为ADA/USDT交易对下现货杠杆订单，您可以使用这样的唯一标识符：`GATE_MARGIN_ADA_USDT`;  
如果您想在BYBIT交易所上为ADA/USDT交易对下现货订单，您可以使用这样的唯一标识符：`BYBIT_SPOT_ADA_USDT`;  
如果您想在KRAKEN交易所上为ADA/USDT交易对下合约订单，您可以使用这样的唯一标识符：`KRAKEN_FUTURE_ADA_USD`;  
目前支持三种订单：现货订单、U本位永续合约订单和现货杠杆订单, BYBIT暂不支持现货杠杆订单, KRAKEN暂不支持现货与杠杆订单  
side | string | true | none | BUY, SELL  
type | string | false | none | 订单类型（默认`LIMIT`，支持类型列举：`LIMIT`、`MARKET`）  
time_in_force | string | false | none | 默认GTC，支持类型枚举，`GTC`，`IOC`，`FOK`，`POC`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
qty | string | false | none | 订单数量（强制性，除非现货市价买入）  
price | string | false | none | 限价订单价格（限价订单必须）  
quote_qty | string | false | none | 订单报价数量，现货和杠杆市价买单必传  
reduce_only | string | false | none | 只减仓：`true`或者`false`  
position_side | string | false | none | 仓位方向：`NONE`, `LONG`, `SHORT`  
不传默认单向持仓`NONE`  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
side | BUY  
side | SELL  
type | LIMIT  
type | MARKET  
time_in_force | GTC  
time_in_force | IOC  
time_in_force | FOK  
time_in_force | POC  
reduce_only | true  
reduce_only | false  
position_side | LONG  
position_side | SHORT  
position_side | NONE  
      
    
    {
      "text": "string",
      "symbol": "string",
      "side": "BUY",
      "type": "LIMIT",
      "time_in_force": "GTC",
      "qty": "string",
      "price": "string",
      "quote_qty": "string",
      "reduce_only": "true",
      "position_side": "LONG"
    }
    
    

##  CrossexConvertOrderRequest

_闪兑交易请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
quote_id | string | true | none | 询价ID  
      
    
    {
      "quote_id": "string"
    }
    
    

##  CrossexOrder

_CrossexOrder_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
user_id | string | true | none | 用户 ID  
order_id | string | true | none | 订单 ID  
text | string | true | none | 客户自定义订单 ID  
state | string | true | none | 订单状态：  
  
NEW：订单已通过校验，等待发送到交易所  
  
OPEN：订单已挂在交易所订单簿上  
  
PARTIALLY_FILLED：订单已部分成交  
  
FILLED：订单已完全成交  
  
FAIL：CrossEx 内部校验未通过，请查看 reason 字段了解失败原因  
  
REJECT：订单被交易所拒绝，请查看 reason 字段了解失败原因  
symbol | string | true | none | 交易对唯一标识，示例：  
BINANCE_SPOT_BTC_USDT、BINANCE_FUTURE_BTC_USDT  
side | string | true | none | 方向（BUY 买入 / SELL 卖出）  
type | string | true | none | 订单类型（LIMIT 限价 / MARKET 市价）  
attribute | string | true | none | 订单属性（COMMON 普通单 / LIQ 强平接管单 / REDUCE 强平减仓单 / ADL 自动减仓 / SETTLEMENT 下架清算）  
exchange_type | string | true | none | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN）  
business_type | string | true | none | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆）  
qty | string | true | none | 基础货币下单数量  
quote_qty | string | true | none | 报价币种下单数量  
price | string | true | none | 订单价格  
time_in_force | string | true | none | 时效策略（默认 GTC，枚举值：GTC / IOC / FOK / POC）  
executed_qty | string | true | none | 已成交基础货币数量  
executed_amount | string | true | none | 已成交报价币种金额  
executed_avg_price | string | true | none | 已成交均价  
fee_coin | string | true | none | 手续费币种  
fee | string | true | none | 手续费金额  
reduce_only | string | true | none | 是否仅减仓订单（"true" 或 "false"）  
leverage | string | true | none | 订单杠杆倍数  
reason | string | true | none | 失败原因描述  
last_executed_qty | string | true | none | 最新一次成交数量  
last_executed_price | string | true | none | 最新一次成交价格  
last_executed_amount | string | true | none | 最新一次成交金额  
position_side | string | true | none | 仓位方向（NONE 无仓位 / LONG 多仓 / SHORT 空仓）  
create_time | string | true | none | 创建时间  
update_time | string | true | none | 更新时间  
      
    
    {
      "user_id": "string",
      "order_id": "string",
      "text": "string",
      "state": "string",
      "symbol": "string",
      "side": "string",
      "type": "string",
      "attribute": "string",
      "exchange_type": "string",
      "business_type": "string",
      "qty": "string",
      "quote_qty": "string",
      "price": "string",
      "time_in_force": "string",
      "executed_qty": "string",
      "executed_amount": "string",
      "executed_avg_price": "string",
      "fee_coin": "string",
      "fee": "string",
      "reduce_only": "string",
      "leverage": "string",
      "reason": "string",
      "last_executed_qty": "string",
      "last_executed_price": "string",
      "last_executed_amount": "string",
      "position_side": "string",
      "create_time": "string",
      "update_time": "string"
    }
    
    

##  CrossexAccountUpdateResponse

_CrossexAccountUpdateResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
position_mode | string | false | none | 请求修改的合约仓位模式（SINGLE/DUAL）  
account_mode | string | false | none | 请求修改的账户模式（CROSS_EXCHANGE/ISOLATED_EXCHANGE，默认：CROSS_EXCHANGE）  
exchange_type | string | false | none | 请求修改的交易所（BINANCE/OKX/GATE/BYBIT/KRAKEN/CROSSEX，当账户模式为ISOLATED_EXCHANGE时，修改合约仓位模式必须指定交易所）  
      
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }