---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/stockoptions
api_type: REST
updated_at: 2026-11-23 18:58:06.993975
---

# StockOptions

期权业务提供期权标的、合约、行情、仓位和委托管理能力。

  * 文档路由前缀: `/stock_options`
  * 期权 API 的认证、签名和公共错误结构与 APIv4 保持一致。

##  查询期权交易费用率

GET`/stock_options/fee-rate`

GET `/stock_options/fee-rate`

_查询期权交易费用率_

查询期权交易涉及的费用配置，供下单前了解费用组成。 返回 SEC、TAF、OCC、ORF、CAT 等费用的费率及适用的最低、最高费用配置。

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 期权交易费用配置 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionConfigResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
sec | string | Optional |  | SEC 费率。  
min_sec | string | Optional |  | SEC 最低费用。  
max_sec | string | Optional |  | SEC 最高费用；为空表示不限制。  
taf | string | Optional |  | TAF 费率。  
min_taf | string | Optional |  | TAF 最低费用。  
max_taf | string | Optional |  | TAF 最高费用。  
occ | string | Optional |  | OCC 费用。  
orf | string | Optional |  | ORF 费用。  
cat | string | Optional |  | CAT 费用。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/fee-rate'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/fee-rate \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "sec": "0.0000206",
        "min_sec": "0.01",
        "max_sec": "",
        "taf": "0.00279",
        "min_taf": "0.01",
        "max_taf": "9.79",
        "occ": "0.025",
        "orf": "0.012",
        "cat": "0.0003"
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  查询期权标的列表

GET`/stock_options/underlyings`

GET `/stock_options/underlyings`

_查询期权标的列表_

查询可用的期权标的列表，供选择标的后继续查询合约、到期日和期权链。 返回标的代码、名称、多语言描述、图标和下单精度、数量限制。 `underlyings` 支持英文逗号分隔的多个标的；不传时查询全部可用标的。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlyings | 请求参数 | string | 否 | 期权标的代码列表，多个使用英文逗号分隔，例如 AAPL,TSLA；不传时查询全部可用标的。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 期权标的列表 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionSymbolListResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
underlying | string | Optional |  | 期权标的代码。  
description | string | Optional |  | 标的描述。  
descs | array | Optional |  | 标的的多语言描述。  
icon_link | string | Optional |  | 标的图标链接。  
price_precision | integer | Optional |  | 价格小数位数。  
min_order_volume | string | Optional |  | 最小委托数量。  
max_order_volume | string | Optional |  | 最大委托数量。  
step_order_volume | string | Optional |  | 委托数量步长。  
  
**allOf[1] / data / list / items / descs**

标的的多语言描述。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items / descs / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
lang | string | Optional |  | 语言代码。  
value | string | Optional |  | 该语言的标的描述。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/underlyings'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/underlyings \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "list": [
          {
            "underlying": "AAPL",
            "description": "Apple Inc.",
            "descs": [
              {
                "lang": "en",
                "value": "Apple Inc."
              }
            ],
            "icon_link": "https://example.com/aapl.png",
            "price_precision": 2,
            "min_order_volume": "1",
            "max_order_volume": "1000",
            "step_order_volume": "1"
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  查询期权合约列表

GET`/stock_options/contracts`

GET `/stock_options/contracts`

_查询期权合约列表_

查询指定标的下的期权合约，供获取合约代码、行权价、到期日及交易规则。 `underlying` 必填，可按到期日和看涨、看跌类型筛选；当前仅提供美国市场（`us`）合约。 结果按合约代码升序分页，返回总记录数、总页数和当前页列表。`page_size` 默认及上限均为 1000。 返回的价格精度、最小和最大委托数量等字段可用于下单前检查。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 期权标的代码，例如 AAPL；本参数为单个标的，不是期权合约代码。  
exchange | 请求参数 | string | 否 | 交易市场筛选；当前仅提供美国市场（us）合约。不传或为空时按 us 查询。  
\- us: 美国市场。  
  
expiration_date | 请求参数 | string(date) | 否 | 期权到期日，格式 YYYY-MM-DD；不传时不按到期日筛选。  
option_type | 请求参数 | StockOptionOptionType | 否 | 合约列表的期权类型筛选；不传表示不过滤。  
\- call: 看涨期权。  
\- put: 看跌期权。  
  
page | 请求参数 | integer | 否 | 页码，从 1 开始；不传时默认为 1。  
page_size | 请求参数 | integer | 否 | 合约列表每页数量；不传时默认为 1000，超过 1000 按 1000 处理。  
  
####  详细描述

**exchange** : 交易市场筛选；当前仅提供美国市场（us）合约。不传或为空时按 us 查询。  
\- us: 美国市场。  

**option_type** : 合约列表的期权类型筛选；不传表示不过滤。  
\- call: 看涨期权。  
\- put: 看跌期权。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
exchange | us  
option_type | call  
option_type | put  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 期权合约列表 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionContractListResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | integer(int64) | Optional |  | 匹配条件的总记录数。  
total_page | integer | Optional |  | 总页数。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
exchange | string | Optional |  | 交易市场。  
expiration_date | string(date) | Optional |  | 期权到期日，格式 YYYY-MM-DD。  
settlement_date | string(date) | Optional |  | 期权结算日，格式 YYYY-MM-DD。  
strike_price | string | Optional |  | 行权价。  
option_type | string | Optional | enum: ["call","put"] | 期权类型。  
\- call: 看涨期权。  
\- put: 看跌期权。  
multiplier | string | Optional |  | 合约乘数。  
open_interest | string | Optional |  | 未平仓合约数量。  
quote_currency | string | Optional |  | 报价币种。  
settlement_type | string | Optional |  | 结算方式。  
trade_status | string | Optional | enum: ["open","closed"] | 合约当前交易状态。  
\- open: 处于可交易时段，且合约及标的均可交易。  
\- closed: 当前不可交易，包括非交易时段、合约非有效状态或标的未启用。  
trade_mode | integer | Optional | enum: [0,4] | 当前交易模式。  
\- 0: 禁止交易。  
\- 4: 允许买入和卖出；普通账户卖出仍须有足够的可用多头持仓。  
price_precision | integer | Optional |  | 价格小数位数。  
min_order_volume | string | Optional |  | 最小委托数量。  
max_order_volume | string | Optional |  | 最大委托数量。  
step_order_volume | string | Optional |  | 委托数量步长。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/contracts'
    query_param = 'underlying=AAPL'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/contracts?underlying=AAPL \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "symbol": "AAPL260814P00130000",
            "symbol_display": "AAPL-260814-130-P",
            "underlying": "AAPL",
            "exchange": "us",
            "expiration_date": "2026-08-14",
            "settlement_date": "2026-08-15",
            "strike_price": "130",
            "option_type": "put",
            "multiplier": "100",
            "open_interest": "100",
            "quote_currency": "USD",
            "settlement_type": "physical",
            "trade_status": "open",
            "trade_mode": 4,
            "price_precision": 2,
            "min_order_volume": "1",
            "max_order_volume": "1000",
            "step_order_volume": "1"
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  查询期权到期日列表

GET`/stock_options/market/expirations`

GET `/stock_options/market/expirations`

_查询期权到期日列表_

查询指定期权标的的到期日列表，供选择期权合约的到期日。 `underlying` 必填；返回各到期日期及对应的 Unix 时间戳，所选日期可用于查询期权链。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 期权标的代码，例如 AAPL；本参数为单个标的，不是期权合约代码。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 期权到期日列表 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionExpirationListResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
underlying | string | Optional |  | 期权标的代码。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
expiration_date | string(date) | Optional |  | 期权到期日，格式 YYYY-MM-DD。  
expiration_date_ts | integer(int64) | Optional |  | 到期日对应的 Unix 时间戳。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/market/expirations'
    query_param = 'underlying=AAPL'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/market/expirations?underlying=AAPL \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "underlying": "AAPL",
        "list": [
          {
            "expiration_date": "2026-08-14",
            "expiration_date_ts": 1786665600
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  查询期权链

GET`/stock_options/market/chain`

GET `/stock_options/market/chain`

_查询期权链_

查询同一标的、同一到期日下不同执行价的期权行情，供比较看涨、看跌合约。 `underlying` 和 `expiration_date` 必填；`option_type` 可筛选 `call` 或 `put`，不传或传 `all` 时返回全部类型。 返回合约代码、执行价、买卖报价、最新价、标记价格、隐含波动率和希腊值等行情字段。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 是 | 期权标的代码，例如 AAPL；本参数为单个标的，不是期权合约代码。  
expiration_date | 请求参数 | string(date) | 是 | 要查询的期权到期日，格式 YYYY-MM-DD，可从到期日列表获取。  
option_type | 请求参数 | string | 否 | 期权链的期权类型筛选。  
\- call: 仅看涨期权。  
\- put: 仅看跌期权。  
\- all: 全部类型，与不传此参数相同。  
  
  
####  详细描述

**option_type** : 期权链的期权类型筛选。  
\- call: 仅看涨期权。  
\- put: 仅看跌期权。  
\- all: 全部类型，与不传此参数相同。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
option_type | call  
option_type | put  
option_type | all  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 期权链 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionOptionChainResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
underlying | string | Optional |  | 期权标的代码。  
expiration_date | string(date) | Optional |  | 期权到期日，格式 YYYY-MM-DD。  
expiration_date_ts | integer(int64) | Optional |  | 到期日对应的 Unix 时间戳。  
index_price | string | Optional |  | 标的指数价格；无有效值时为空。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
strike_price | string | Optional |  | 行权价。  
option_type | string | Optional | enum: ["call","put"] | 期权类型。  
\- call: 看涨期权。  
\- put: 看跌期权。  
bid | string | Optional |  | 最佳买入报价。  
ask | string | Optional |  | 最佳卖出报价。  
mark_price | string | Optional |  | 标记价格。  
mark_iv | string | Optional |  | 标记隐含波动率。  
last | string | Optional |  | 最新成交价。  
display_price | string | Optional |  | 展示价格。  
breakeven_price | string | Optional |  | 盈亏平衡价格。  
to_breakeven_pct | string | Optional |  | 距离盈亏平衡价格的百分比。  
today_change_pct | string | Optional |  | 今日价格变化百分比。  
open_interest | string | Optional |  | 未平仓合约数量。  
position | string | Optional |  | 仓位数量。  
delta | string | Optional |  | 期权 Delta。  
gamma | string | Optional |  | 期权 Gamma。  
theta | string | Optional |  | 期权 Theta。  
vega | string | Optional |  | 期权 Vega。  
rho | string | Optional |  | 期权 Rho。  
trade_status | string | Optional | enum: ["open","closed"] | 合约当前交易状态。  
\- open: 处于可交易时段，且合约及标的均可交易。  
\- closed: 当前不可交易，包括非交易时段、合约非有效状态或标的未启用。  
trade_mode | integer | Optional | enum: [0,4] | 当前交易模式。  
\- 0: 禁止交易。  
\- 4: 允许买入和卖出；普通账户卖出仍须有足够的可用多头持仓。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/market/chain'
    query_param = 'underlying=AAPL&expiration_date=2026-08-14'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/market/chain?underlying=AAPL&expiration_date=2026-08-14 \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "underlying": "AAPL",
        "expiration_date": "2026-08-14",
        "expiration_date_ts": 1786665600,
        "index_price": "130.25",
        "list": [
          {
            "symbol": "AAPL260814P00130000",
            "symbol_display": "AAPL-260814-130-P",
            "strike_price": "130",
            "option_type": "put",
            "bid": "1.10",
            "ask": "1.20",
            "mark_price": "1.15",
            "mark_iv": "0.25",
            "last": "1.18",
            "display_price": "1.15",
            "breakeven_price": "128.85",
            "to_breakeven_pct": "-0.0108",
            "today_change_pct": "0.05",
            "open_interest": "100",
            "position": "0",
            "delta": "-0.45",
            "gamma": "0.03",
            "theta": "-0.02",
            "vega": "0.10",
            "rho": "-0.01",
            "trade_status": "open",
            "trade_mode": 4
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  查询期权盘口

GET`/stock_options/market/{symbol}/orderbook`

GET `/stock_options/market/{symbol}/orderbook`

_查询期权盘口_

查询指定期权合约的最佳买入、卖出报价，供查看当前盘口价格。 `symbol` 为期权合约代码。`bids`、`asks` 每侧最多返回一档价格，不提供挂单数量。 无可用报价时，对应一侧返回空数组；查询不到合约时两侧均为空数组。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | URL | string | 是 | 期权合约代码  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 期权盘口 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionOrderBookResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
bids | array | Optional |  | 买入报价列表；最多一档，无报价时为空数组。  
asks | array | Optional |  | 卖出报价列表；最多一档，无报价时为空数组。  
  
**allOf[1] / data / bids**

买入报价列表；最多一档，无报价时为空数组。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / bids / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price | string | Optional |  | 报价价格。  
  
**allOf[1] / data / asks**

卖出报价列表；最多一档，无报价时为空数组。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / asks / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price | string | Optional |  | 报价价格。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock_options/market/AAPL260814P00130000/orderbook'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock_options/market/AAPL260814P00130000/orderbook \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "symbol": "AAPL260814P00130000",
        "symbol_display": "AAPL-260814-130-P",
        "bids": [
          {
            "price": "1.10"
          }
        ],
        "asks": [
          {
            "price": "1.20"
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  查询当前期权仓位🔒 需要认证

GET`/stock_options/positions`

GET `/stock_options/positions`

_查询当前期权仓位_

查询当前用户的期权持仓及市值、盈亏，供查看持仓风险和可用数量。 可按 `underlying` 或 `symbol` 筛选；指定 `symbol` 时须为存在的期权合约，没有持仓则返回空列表。 `price_type` 控制市值、未实现盈亏和今日盈亏的计价价格：`latest`（默认）为最新成交价，`mark` 为标记价格。 汇总 `today_pnl` 包含当前持仓及今日已全部平仓合约。列表按 `open_time` 降序，相同时按 `symbol` 升序。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 否 | 期权标的代码，例如 AAPL；不传时不按标的筛选。当前委托查询仅支持单个标的。  
symbol | 请求参数 | string | 否 | 完整期权合约代码，例如 AAPL260814P00130000；不传时不按合约筛选。  
price_type | 请求参数 | StockOptionPositionPnlPriceType | 否 | 仓位市值 / 未实现盈亏 / 今日盈亏的计价价格类型。  
可选：`latest`（最新成交价）、`mark`（标记价格）。不传或为空时按 `latest`。  
  
  
####  详细描述

**price_type** : 仓位市值 / 未实现盈亏 / 今日盈亏的计价价格类型。  
可选：`latest`（最新成交价）、`mark`（标记价格）。不传或为空时按 `latest`。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
price_type | latest  
price_type | mark  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 当前期权仓位列表 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionPositionListResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
today_pnl | string | Optional |  | 期权今日盈亏汇总 = 当前持仓各合约 today_pnl 之和 + 今日已全部平仓合约的今日盈亏。  
当前持仓部分的计价价格受请求参数 `price_type` 影响。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
side | string | Optional | enum: ["long","short"] | 仓位方向。  
\- long: 多头仓位。  
\- short: 空头仓位。  
open_time | integer(int64) | Optional |  | 开仓时间，秒级时间戳；无有效值时为 0。  
quantity | string | Optional |  | 持仓数量。  
available | string | Optional |  | 可用数量；当前与 quantity 一致。  
frozen | string | Optional |  | 冻结数量；当前未单独计算时可能为空。  
avg_entry_price | string | Optional |  | 开仓均价。  
last_price | string | Optional |  | 最新成交价；无有效值时为 0。  
mark_price | string | Optional |  | 标记价格；无有效值时为 0。  
previous_close | string | Optional |  | 昨收。  
无有效正值时不返回有效昨收（字段可能为空），此时跳过今日盈亏计算。  
market_value | string | Optional |  | 市值 = 计价价格 × 带符号持仓数量 × 合约乘数。  
计价价格由 `price_type` 决定（`latest`→last_price，`mark`→mark_price）。  
unrealized_pnl | string | Optional |  | 未实现盈亏 = (计价价格 − 开仓均价) × 带符号持仓数量 × 合约乘数。  
开仓均价或数量无效时为 0。计价价格规则同 market_value。  
today_pnl | string | Optional |  | 单合约今日盈亏。依赖有效 previous_close；无昨收时为 0。  
计价价格规则同 market_value。  
today_buy_qty | string | Optional |  | 今日买入数量（用户日交易汇总）。  
today_sell_qty | string | Optional |  | 今日卖出数量（用户日交易汇总）。  
today_buy_value | string | Optional |  | 今日买入金额（用户日交易汇总）。  
today_sell_value | string | Optional |  | 今日卖出金额（用户日交易汇总）。  
trade_status | string | Optional | enum: ["open","closed"] | 合约当前交易状态。  
\- open: 处于可交易时段，且合约及标的均可交易。  
\- closed: 当前不可交易，包括非交易时段、合约非有效状态或标的未启用。  
trade_mode | integer | Optional | enum: [0,4] | 当前交易模式。  
\- 0: 禁止交易。  
\- 4: 允许买入和卖出；普通账户卖出仍须有足够的可用多头持仓。  
multiplier | string | Optional |  | 合约乘数。  
price_precision | integer | Optional |  | 价格小数位数。  
min_order_volume | string | Optional |  | 最小委托数量。  
max_order_volume | string | Optional |  | 最大委托数量。  
step_order_volume | string | Optional |  | 委托数量步长。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
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
    
    url = '/stock_options/positions'
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
    url="/stock_options/positions"
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
      "label": "",
      "data": {
        "today_pnl": "68.50",
        "list": [
          {
            "symbol": "AAPL260821C00210000",
            "symbol_display": "AAPL-260821-210-C",
            "underlying": "AAPL",
            "side": "long",
            "open_time": 1785919118,
            "quantity": "2",
            "available": "2",
            "frozen": "0",
            "avg_entry_price": "10.95",
            "last_price": "12.18",
            "mark_price": "12.05",
            "previous_close": "11.20",
            "market_value": "2436.00",
            "unrealized_pnl": "246.00",
            "today_pnl": "54.00",
            "today_buy_qty": "1",
            "today_sell_qty": "0",
            "today_buy_value": "100.00",
            "today_sell_value": "0",
            "trade_status": "open",
            "trade_mode": 4,
            "multiplier": "100",
            "price_precision": 2,
            "min_order_volume": "1",
            "max_order_volume": "1000",
            "step_order_volume": "1"
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  平期权仓位🔒 需要认证

POST`/stock_options/positions/close`

POST `/stock_options/positions/close`

_平期权仓位_

为指定期权持仓提交平仓委托，支持按数量部分平仓或全部平仓。 `symbol`、`quantity` 必填，平仓数量须为正数，不得超过可用持仓，并须满足合约的最小、最大数量及数量步长规则。 `order_type` 不传或为空时按 `market` 市价平仓；选择 `limit` 时须提供正数 `price`，市价平仓忽略 `price`。 平仓方向由持仓自动确定，有效期固定为 `day`。成功返回平仓委托的 `order_id`，后续可查询委托状态。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | StockOptionClosePositionRequest | 是 |   
symbol | body | string | 是 | 要平仓的期权合约代码，须有对应的可用持仓。  
quantity | body | string | 是 | 本次平仓数量，使用正数十进制字符串，不得超过可用持仓；须满足合约最小、最大数量和数量步长规则。  
order_type | body | string | 否 | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
  
price | body | string | 否 | 限价平仓必填的正数价格，使用普通十进制字符串，最多 64 个字符，不支持科学计数法；市价平仓忽略。  
client_order_id | body | string | 否 | 自定义平仓委托标识；不传或仅为空白时自动生成。  
  
####  详细描述

** order_type**: 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  

####  请求体结构

`order_type` 可选。缺省或为空时按市价平仓；仅支持 `market` 或 `limit`。

请求体结构类型 | 约束  
---|---  
StockOptionClosePositionRequest | required: ["symbol","quantity"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Required |  | 要平仓的期权合约代码，须有对应的可用持仓。  
quantity | string | Required |  | 本次平仓数量，使用正数十进制字符串，不得超过可用持仓；须满足合约最小、最大数量和数量步长规则。  
order_type | string | Optional | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
price | string | Optional |  | 限价平仓必填的正数价格，使用普通十进制字符串，最多 64 个字符，不支持科学计数法；市价平仓忽略。  
client_order_id | string | Optional |  | 自定义平仓委托标识；不传或仅为空白时自动生成。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 平仓响应 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionClosePositionResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Optional |  | 委托 ID。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
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
    
    url = '/stock_options/positions/close'
    query_param = ''
    body='{"symbol":"string","quantity":"string","order_type":"market","price":"1.00","client_order_id":"string"}'
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
    url="/stock_options/positions/close"
    query_param=""
    body_param='{"symbol":"string","quantity":"string","order_type":"market","price":"1.00","client_order_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "symbol": "string",
      "quantity": "string",
      "order_type": "market",
      "price": "1.00",
      "client_order_id": "string"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "order_id": "8000000001"
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  查询当前期权委托🔒 需要认证

GET`/stock_options/orders`

GET `/stock_options/orders`

_查询当前期权委托_

查询当前用户尚未结束的期权委托，供查看挂单和部分成交情况。 可按 `underlying`、`symbol`、`side` 筛选；`underlying` 仅支持一个标的，不能使用逗号分隔多个标的。 `status` 仅包含 1（新订单）和 2（部分成交）；终态委托请查询历史委托列表。 返回符合条件的当前委托，按委托创建时间 `time_setup` 降序排列；本接口不提供分页参数。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 否 | 期权标的代码，例如 AAPL；不传时不按标的筛选。当前委托查询仅支持单个标的。  
symbol | 请求参数 | string | 否 | 完整期权合约代码，例如 AAPL260814P00130000；不传时不按合约筛选。  
side | 请求参数 | StockOptionOrderListSide | 否 | 委托方向筛选。  
不传表示查询全部方向。  
\- 1: 仅卖出委托。  
\- 2: 仅买入委托。  
  
  
####  详细描述

**side** : 委托方向筛选。  
不传表示查询全部方向。  
\- 1: 仅卖出委托。  
\- 2: 仅买入委托。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
side | 1  
side | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 当前期权委托列表 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionOrderListResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

当前未结束的委托，不包含全部成交、已撤销或下单拒绝的终态委托。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Optional |  | 委托 ID。  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
side | integer | Optional | enum: [1,2] | 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  
order_type | string | Optional | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
status | integer | Optional | enum: [1,2] | 当前委托状态：  
\- 1: 新订单，已验证并等待处理。  
\- 2: 部分成交，仍有未成交数量。  
status_desc | string | Optional |  | 委托状态的可读说明，随请求语言返回。  
time_in_force | string | Optional | enum: ["day","gtc"] | 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  
quantity | string | Optional |  | 委托数量。  
filled_quantity | string | Optional |  | 已成交数量。  
price | string | Optional |  | 委托价格。  
time_setup | integer(int64) | Optional |  | 委托创建时间。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
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
    
    url = '/stock_options/orders'
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
    url="/stock_options/orders"
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
      "label": "",
      "data": {
        "list": [
          {
            "order_id": "8000000001",
            "symbol": "AAPL260814P00130000",
            "symbol_display": "AAPL-260814-130-P",
            "underlying": "AAPL",
            "side": 2,
            "order_type": "limit",
            "status": 1,
            "status_desc": "new",
            "time_in_force": "day",
            "quantity": "1",
            "filled_quantity": "0",
            "price": "1.20",
            "time_setup": 1785919118
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  创建期权委托🔒 需要认证

POST`/stock_options/orders`

POST `/stock_options/orders`

_创建期权委托_

为指定期权合约提交买入或卖出委托，成功返回委托 ID。 `symbol`、`side`、`order_type`、`time_in_force` 和 `quantity` 必填；`side` 为 1（卖出）或 2（买入）。 限价单须提供正数 `price`，有效期支持 `day` 或 `gtc`；市价单忽略 `price`，有效期仅支持 `day`。 数量使用正数十进制字符串，并须满足合约的最小和最大委托数量限制。卖出单须有足够的可用多头持仓。 `client_order_id` 可选，不传或仅为空白时自动生成。返回委托 ID 后，可通过当前委托或委托详情查询后续状态。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | StockOptionPutOrderRequest | 是 |   
symbol | body | string | 是 | 要下单的完整期权合约代码，可从合约列表或期权链获取。  
side | body | integer | 是 | 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  
  
order_type | body | string | 是 | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
  
time_in_force | body | string | 是 | 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  
  
price | body | string | 否 | 限价单必填的委托价格，须为大于 0 的普通十进制字符串，最多 64 个字符，不支持科学计数法；市价单忽略。  
quantity | body | string | 是 | 委托数量，须为大于 0 的十进制字符串，并满足合约的最小、最大委托数量限制。  
client_order_id | body | string | 否 | 自定义委托标识，可选，按 UTF-8 编码最多 30 字节；不传或仅为空白时自动生成。  
  
####  详细描述

** side**: 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  

** order_type**: 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  

** time_in_force**: 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
side | 1  
side | 2  
order_type | market  
order_type | limit  
time_in_force | day  
time_in_force | gtc  
  
####  请求体结构

请求体结构类型 | 约束  
---|---  
StockOptionPutOrderRequest | required: ["symbol","side","order_type","time_in_force","quantity"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Required |  | 要下单的完整期权合约代码，可从合约列表或期权链获取。  
side | integer | Required | enum: [1,2] | 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  
order_type | string | Required | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
time_in_force | string | Required | enum: ["day","gtc"] | 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  
price | string | Optional |  | 限价单必填的委托价格，须为大于 0 的普通十进制字符串，最多 64 个字符，不支持科学计数法；市价单忽略。  
quantity | string | Required |  | 委托数量，须为大于 0 的十进制字符串，并满足合约的最小、最大委托数量限制。  
client_order_id | string | Optional | maxLength: 30 | 自定义委托标识，可选，按 UTF-8 编码最多 30 字节；不传或仅为空白时自动生成。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 创建委托响应 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionPutOrderResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托 ID。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
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
    
    url = '/stock_options/orders'
    query_param = ''
    body='{"symbol":"AAPL260814P00130000","side":1,"order_type":"market","time_in_force":"day","price":"1.00","quantity":"1","client_order_id":"string"}'
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
    url="/stock_options/orders"
    query_param=""
    body_param='{"symbol":"AAPL260814P00130000","side":1,"order_type":"market","time_in_force":"day","price":"1.00","quantity":"1","client_order_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "symbol": "AAPL260814P00130000",
      "side": 1,
      "order_type": "market",
      "time_in_force": "day",
      "price": "1.00",
      "quantity": "1",
      "client_order_id": "string"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "id": "8000000001"
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  撤销全部期权限价委托🔒 需要认证

DELETE`/stock_options/orders`

DELETE `/stock_options/orders`

_撤销全部期权限价委托_

批量撤销当前用户的期权限价委托，供一次撤销全部或指定范围的挂单。 请求体可省略，也可传空对象；不指定筛选条件时撤销全部限价委托。 可提供 `underlying`、`symbol`、`side` 筛选撤单范围；`side` 支持 1（卖出）和 2（买入），不传时不区分方向。 成功返回撤单请求结果，委托的后续状态可通过查询接口确认。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | StockOptionCancelAllOrdersRequest | 否 |   
underlying | body | string | 否 | 期权标的代码；为空或不传时不指定标的筛选条件。  
symbol | body | string | 否 | 期权合约代码；为空或不传时不指定合约筛选条件。  
side | body | integer | 否 | 委托方向筛选。  
不传表示查询全部方向。  
\- 1: 仅卖出委托。  
\- 2: 仅买入委托。  
  
  
####  详细描述

** side**: 委托方向筛选。  
不传表示查询全部方向。  
\- 1: 仅卖出委托。  
\- 2: 仅买入委托。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
side | 1  
side | 2  
  
####  请求体结构

批量撤销限价委托的筛选条件；side 为 1（卖出）或 2（买入），不传时不区分方向。

请求体结构类型 | 约束  
---|---  
StockOptionCancelAllOrdersRequest |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
underlying | string | Optional |  | 期权标的代码；为空或不传时不指定标的筛选条件。  
symbol | string | Optional |  | 期权合约代码；为空或不传时不指定合约筛选条件。  
side | integer | Optional | enum: [1,2] | 委托方向筛选。  
不传表示查询全部方向。  
\- 1: 仅卖出委托。  
\- 2: 仅买入委托。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 全部撤单响应 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionCancelAllOrdersResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
success | boolean | Optional |  | 撤单请求是否成功。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
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
    
    url = '/stock_options/orders'
    query_param = ''
    body='{"underlying":"AAPL","symbol":"string","side":1}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('DELETE', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/stock_options/orders"
    query_param=""
    body_param='{"underlying":"AAPL","symbol":"string","side":1}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "underlying": "AAPL",
      "symbol": "string",
      "side": 1
    }
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "success": true
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  查询期权委托明细🔒 需要认证

GET`/stock_options/orders/{order_id}`

GET `/stock_options/orders/{order_id}`

_查询期权委托明细_

按委托 ID 查询当前用户的单笔期权委托，供跟踪委托状态、成交数量和成交均价。 `order_id` 必填，须为正整数形式的字符串。可查询当前委托和已结束的委托，不按是否为终态筛选。 返回委托价格、数量、已成交数量、状态说明、成交均价、手续费和时间等信息。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 期权委托 ID，使用正整数形式的字符串，可从下单结果或委托查询结果获取。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 期权委托明细 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionOrderDetailResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  | 委托详情，可包含当前委托或已结束的委托。  
  
**allOf[1] / data**

委托详情，可包含当前委托或已结束的委托。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Optional |  | 委托 ID。  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
side | integer | Optional | enum: [1,2] | 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  
order_type | string | Optional | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
status | integer | Optional |  | 订单详情中的委托状态，以下说明业务状态；详情接口不按状态过滤。  
\- 1: 新订单，已验证并等待处理。  
\- 2: 部分成交，仍有未成交数量。  
\- 3: 全部成交，终态。  
\- 4: 已撤销，终态；此前可能已有部分成交。  
\- 5: 下单拒绝，终态。  
当前委托列表仅返回 1、2；历史委托列表仅返回 3、4、5。  
status_desc | string | Optional |  | 委托状态的可读说明，随请求语言返回。  
time_in_force | string | Optional | enum: ["day","gtc"] | 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  
quantity | string | Optional |  | 委托数量。  
filled_quantity | string | Optional |  | 已成交数量。  
price | string | Optional |  | 委托价格。  
time_setup | integer(int64) | Optional |  | 委托创建时间。  
avg_fill_price | string | Optional |  | 成交均价。  
fee | string | Optional |  | 手续费。  
time_done | integer(int64) | Optional |  | 委托结束时间。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
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
    
    url = '/stock_options/orders/8000000001'
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
    url="/stock_options/orders/8000000001"
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
      "label": "",
      "data": {
        "order_id": "8000000001",
        "symbol": "AAPL260814P00130000",
        "symbol_display": "AAPL-260814-130-P",
        "underlying": "AAPL",
        "side": 2,
        "order_type": "limit",
        "status": 3,
        "status_desc": "filled",
        "time_in_force": "day",
        "quantity": "1",
        "filled_quantity": "1",
        "price": "1.20",
        "avg_fill_price": "1.20",
        "fee": "0.025",
        "time_setup": 1785919118,
        "time_done": 1785919120
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  修改期权限价委托🔒 需要认证

PUT`/stock_options/orders/{order_id}`

PUT `/stock_options/orders/{order_id}`

_修改期权限价委托_

修改当前用户的一笔期权限价委托的价格和总数量。 路径中的 `order_id` 及请求体中的 `price`、`quantity` 均必填；市价委托不支持改单。 `quantity` 是修改后的委托总数量，不能小于已成交数量 `filled_quantity`，不是剩余未成交数量。 卖出改单还须有足够的可用持仓覆盖修改后的未成交数量。成功返回委托 ID，后续可查询委托状态。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 期权委托 ID，使用正整数形式的字符串，可从下单结果或委托查询结果获取。  
body | body | StockOptionUpdateOrderRequest | 是 |   
price | body | string | 是 | 新的限价，必填，须为正数普通十进制字符串，最多 64 个字符，不支持科学计数法。  
quantity | body | string | 是 | 修改后的委托总数量，使用正数十进制字符串；不是剩余未成交数量，须大于等于已成交数量 filled_quantity。  
  
####  请求体结构

请求体结构类型 | 约束  
---|---  
StockOptionUpdateOrderRequest | required: ["price","quantity"]  
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price | string | Required |  | 新的限价，必填，须为正数普通十进制字符串，最多 64 个字符，不支持科学计数法。  
quantity | string | Required |  | 修改后的委托总数量，使用正数十进制字符串；不是剩余未成交数量，须大于等于已成交数量 filled_quantity。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 改单响应 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionUpdateOrderResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托 ID。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
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
    
    url = '/stock_options/orders/72057594037983901'
    query_param = ''
    body='{"price":"1.25","quantity":"2"}'
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
    url="/stock_options/orders/72057594037983901"
    query_param=""
    body_param='{"price":"1.25","quantity":"2"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "price": "1.25",
      "quantity": "2"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "label": "",
      "data": {
        "id": "8000000001"
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  撤销期权限价委托🔒 需要认证

DELETE`/stock_options/orders/{order_id}`

DELETE `/stock_options/orders/{order_id}`

_撤销期权限价委托_

按委托 ID 撤销当前用户的一笔期权限价委托。 `order_id` 必填；仅限价委托可撤，已成交部分不受撤单影响。 成功返回委托 ID，后续可通过委托详情或历史委托列表查询最终状态。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | string | 是 | 期权委托 ID，使用正整数形式的字符串，可从下单结果或委托查询结果获取。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 撤单响应 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionCancelOrderResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托 ID。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
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
    
    url = '/stock_options/orders/72057594037983901'
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
    url="/stock_options/orders/72057594037983901"
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
      "label": "",
      "data": {
        "id": "8000000001"
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

##  查询历史期权委托🔒 需要认证

GET`/stock_options/orders/history`

GET `/stock_options/orders/history`

_查询历史期权委托_

分页查询当前用户已结束的期权委托，供核对历史委托、成交结果和手续费。 `status` 仅包含 3（全部成交）、4（已撤销）和 5（下单拒绝）。 可按标的、合约、方向及委托创建时间筛选；`begin_time`、`end_time` 为秒级 Unix 时间戳，同时传入时起始时间不得晚于结束时间。 返回总记录数、总页数和当前页列表。`page_size` 默认及上限均为 100。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
underlying | 请求参数 | string | 否 | 期权标的代码，例如 AAPL；不传时不按标的筛选。当前委托查询仅支持单个标的。  
symbol | 请求参数 | string | 否 | 完整期权合约代码，例如 AAPL260814P00130000；不传时不按合约筛选。  
begin_time | 请求参数 | integer(int64) | 否 | 委托创建时间的筛选起点，秒级 Unix 时间戳；不传时不设起始时间，同时传入 end_time 时不得晚于 end_time。  
end_time | 请求参数 | integer(int64) | 否 | 委托创建时间的筛选终点，秒级 Unix 时间戳；不传时不设结束时间，同时传入 begin_time 时不得早于 begin_time。  
side | 请求参数 | StockOptionOrderListSide | 否 | 委托方向筛选。  
不传表示查询全部方向。  
\- 1: 仅卖出委托。  
\- 2: 仅买入委托。  
  
page | 请求参数 | integer | 否 | 页码，从 1 开始；不传时默认为 1。  
page_size | 请求参数 | integer | 否 | 每页数量，最大为 100；不传时默认为 100，超过 100 按 100 处理。  
  
####  详细描述

**side** : 委托方向筛选。  
不传表示查询全部方向。  
\- 1: 仅卖出委托。  
\- 2: 仅买入委托。  

####  枚举值列表

枚举值列表参数 | 值  
---|---  
side | 1  
side | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 历史期权委托列表 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | StockOptionApiResponse  
  
### 返回格式

状态码 **200**

类型 | 约束  
---|---  
StockOptionOrderHistoryResponse |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | integer(int64) | Optional |  | 匹配条件的总记录数。  
total_page | integer | Optional |  | 总页数。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

已结束的委托，仅包含全部成交、已撤销和下单拒绝的终态委托。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Optional |  | 委托 ID。  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
side | integer | Optional | enum: [1,2] | 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  
order_type | string | Optional | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
status | integer | Optional | enum: [3,4,5] | 历史委托状态：  
\- 3: 全部成交。  
\- 4: 已撤销，此前可能已有部分成交。  
\- 5: 下单拒绝。  
status_desc | string | Optional |  | 委托状态的可读说明，随请求语言返回。  
time_in_force | string | Optional | enum: ["day","gtc"] | 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  
quantity | string | Optional |  | 委托数量。  
filled_quantity | string | Optional |  | 已成交数量。  
price | string | Optional |  | 委托价格。  
time_setup | integer(int64) | Optional |  | 委托创建时间。  
avg_fill_price | string | Optional |  | 成交均价。  
fee | string | Optional |  | 手续费。  
time_done | integer(int64) | Optional |  | 委托结束时间。  
  
状态码 **400**

类型 | 约束  
---|---  
StockOptionApiResponse | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
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
    
    url = '/stock_options/orders/history'
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
    url="/stock_options/orders/history"
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
      "label": "",
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "order_id": "8000000001",
            "symbol": "AAPL260814P00130000",
            "symbol_display": "AAPL-260814-130-P",
            "underlying": "AAPL",
            "side": 2,
            "order_type": "limit",
            "status": 3,
            "status_desc": "filled",
            "time_in_force": "day",
            "quantity": "1",
            "filled_quantity": "1",
            "price": "1.20",
            "avg_fill_price": "1.20",
            "fee": "0.025",
            "time_setup": 1785919118,
            "time_done": 1785919120
          }
        ]
      },
      "timestamp": 1785919118845
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "timestamp": 1785919118845
    }
    

#  模型

##  StockOptionOrderDetailResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  | 委托详情，可包含当前委托或已结束的委托。  
  
**allOf[1] / data**

委托详情，可包含当前委托或已结束的委托。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Optional |  | 委托 ID。  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
side | integer | Optional | enum: [1,2] | 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  
order_type | string | Optional | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
status | integer | Optional |  | 订单详情中的委托状态，以下说明业务状态；详情接口不按状态过滤。  
\- 1: 新订单，已验证并等待处理。  
\- 2: 部分成交，仍有未成交数量。  
\- 3: 全部成交，终态。  
\- 4: 已撤销，终态；此前可能已有部分成交。  
\- 5: 下单拒绝，终态。  
当前委托列表仅返回 1、2；历史委托列表仅返回 3、4、5。  
status_desc | string | Optional |  | 委托状态的可读说明，随请求语言返回。  
time_in_force | string | Optional | enum: ["day","gtc"] | 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  
quantity | string | Optional |  | 委托数量。  
filled_quantity | string | Optional |  | 已成交数量。  
price | string | Optional |  | 委托价格。  
time_setup | integer(int64) | Optional |  | 委托创建时间。  
avg_fill_price | string | Optional |  | 成交均价。  
fee | string | Optional |  | 手续费。  
time_done | integer(int64) | Optional |  | 委托结束时间。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "order_id": "string",
        "symbol": "string",
        "symbol_display": "string",
        "underlying": "string",
        "side": 1,
        "order_type": "market",
        "status": 0,
        "status_desc": "string",
        "time_in_force": "day",
        "quantity": "string",
        "filled_quantity": "string",
        "price": "string",
        "time_setup": 0,
        "avg_fill_price": "string",
        "fee": "string",
        "time_done": 0
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionCancelAllOrdersResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
success | boolean | Optional |  | 撤单请求是否成功。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "success": true
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionUpdateOrderRequest

类型 | 约束  
---|---  
object | required: ["price","quantity"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price | string | Required |  | 新的限价，必填，须为正数普通十进制字符串，最多 64 个字符，不支持科学计数法。  
quantity | string | Required |  | 修改后的委托总数量，使用正数十进制字符串；不是剩余未成交数量，须大于等于已成交数量 filled_quantity。  
      
    
    {
      "price": "1.25",
      "quantity": "2"
    }
    
    

##  StockOptionPutOrderRequest

类型 | 约束  
---|---  
object | required: ["symbol","side","order_type","time_in_force","quantity"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Required |  | 要下单的完整期权合约代码，可从合约列表或期权链获取。  
side | integer | Required | enum: [1,2] | 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  
order_type | string | Required | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
time_in_force | string | Required | enum: ["day","gtc"] | 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  
price | string | Optional |  | 限价单必填的委托价格，须为大于 0 的普通十进制字符串，最多 64 个字符，不支持科学计数法；市价单忽略。  
quantity | string | Required |  | 委托数量，须为大于 0 的十进制字符串，并满足合约的最小、最大委托数量限制。  
client_order_id | string | Optional | maxLength: 30 | 自定义委托标识，可选，按 UTF-8 编码最多 30 字节；不传或仅为空白时自动生成。  
      
    
    {
      "symbol": "AAPL260814P00130000",
      "side": 1,
      "order_type": "market",
      "time_in_force": "day",
      "price": "1.00",
      "quantity": "1",
      "client_order_id": "string"
    }
    
    

##  StockOptionContractListResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | integer(int64) | Optional |  | 匹配条件的总记录数。  
total_page | integer | Optional |  | 总页数。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
exchange | string | Optional |  | 交易市场。  
expiration_date | string(date) | Optional |  | 期权到期日，格式 YYYY-MM-DD。  
settlement_date | string(date) | Optional |  | 期权结算日，格式 YYYY-MM-DD。  
strike_price | string | Optional |  | 行权价。  
option_type | string | Optional | enum: ["call","put"] | 期权类型。  
\- call: 看涨期权。  
\- put: 看跌期权。  
multiplier | string | Optional |  | 合约乘数。  
open_interest | string | Optional |  | 未平仓合约数量。  
quote_currency | string | Optional |  | 报价币种。  
settlement_type | string | Optional |  | 结算方式。  
trade_status | string | Optional | enum: ["open","closed"] | 合约当前交易状态。  
\- open: 处于可交易时段，且合约及标的均可交易。  
\- closed: 当前不可交易，包括非交易时段、合约非有效状态或标的未启用。  
trade_mode | integer | Optional | enum: [0,4] | 当前交易模式。  
\- 0: 禁止交易。  
\- 4: 允许买入和卖出；普通账户卖出仍须有足够的可用多头持仓。  
price_precision | integer | Optional |  | 价格小数位数。  
min_order_volume | string | Optional |  | 最小委托数量。  
max_order_volume | string | Optional |  | 最大委托数量。  
step_order_volume | string | Optional |  | 委托数量步长。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionPositionListResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
today_pnl | string | Optional |  | 期权今日盈亏汇总 = 当前持仓各合约 today_pnl 之和 + 今日已全部平仓合约的今日盈亏。  
当前持仓部分的计价价格受请求参数 `price_type` 影响。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
side | string | Optional | enum: ["long","short"] | 仓位方向。  
\- long: 多头仓位。  
\- short: 空头仓位。  
open_time | integer(int64) | Optional |  | 开仓时间，秒级时间戳；无有效值时为 0。  
quantity | string | Optional |  | 持仓数量。  
available | string | Optional |  | 可用数量；当前与 quantity 一致。  
frozen | string | Optional |  | 冻结数量；当前未单独计算时可能为空。  
avg_entry_price | string | Optional |  | 开仓均价。  
last_price | string | Optional |  | 最新成交价；无有效值时为 0。  
mark_price | string | Optional |  | 标记价格；无有效值时为 0。  
previous_close | string | Optional |  | 昨收。  
无有效正值时不返回有效昨收（字段可能为空），此时跳过今日盈亏计算。  
market_value | string | Optional |  | 市值 = 计价价格 × 带符号持仓数量 × 合约乘数。  
计价价格由 `price_type` 决定（`latest`→last_price，`mark`→mark_price）。  
unrealized_pnl | string | Optional |  | 未实现盈亏 = (计价价格 − 开仓均价) × 带符号持仓数量 × 合约乘数。  
开仓均价或数量无效时为 0。计价价格规则同 market_value。  
today_pnl | string | Optional |  | 单合约今日盈亏。依赖有效 previous_close；无昨收时为 0。  
计价价格规则同 market_value。  
today_buy_qty | string | Optional |  | 今日买入数量（用户日交易汇总）。  
today_sell_qty | string | Optional |  | 今日卖出数量（用户日交易汇总）。  
today_buy_value | string | Optional |  | 今日买入金额（用户日交易汇总）。  
today_sell_value | string | Optional |  | 今日卖出金额（用户日交易汇总）。  
trade_status | string | Optional | enum: ["open","closed"] | 合约当前交易状态。  
\- open: 处于可交易时段，且合约及标的均可交易。  
\- closed: 当前不可交易，包括非交易时段、合约非有效状态或标的未启用。  
trade_mode | integer | Optional | enum: [0,4] | 当前交易模式。  
\- 0: 禁止交易。  
\- 4: 允许买入和卖出；普通账户卖出仍须有足够的可用多头持仓。  
multiplier | string | Optional |  | 合约乘数。  
price_precision | integer | Optional |  | 价格小数位数。  
min_order_volume | string | Optional |  | 最小委托数量。  
max_order_volume | string | Optional |  | 最大委托数量。  
step_order_volume | string | Optional |  | 委托数量步长。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "today_pnl": "68.50",
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionCancelOrderResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托 ID。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "id": "string"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionExpirationListResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
underlying | string | Optional |  | 期权标的代码。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
expiration_date | string(date) | Optional |  | 期权到期日，格式 YYYY-MM-DD。  
expiration_date_ts | integer(int64) | Optional |  | 到期日对应的 Unix 时间戳。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "underlying": "string",
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionClosePositionResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Optional |  | 委托 ID。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "order_id": "string"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionOrderHistoryResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
total | integer(int64) | Optional |  | 匹配条件的总记录数。  
total_page | integer | Optional |  | 总页数。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

已结束的委托，仅包含全部成交、已撤销和下单拒绝的终态委托。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Optional |  | 委托 ID。  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
side | integer | Optional | enum: [1,2] | 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  
order_type | string | Optional | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
status | integer | Optional | enum: [3,4,5] | 历史委托状态：  
\- 3: 全部成交。  
\- 4: 已撤销，此前可能已有部分成交。  
\- 5: 下单拒绝。  
status_desc | string | Optional |  | 委托状态的可读说明，随请求语言返回。  
time_in_force | string | Optional | enum: ["day","gtc"] | 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  
quantity | string | Optional |  | 委托数量。  
filled_quantity | string | Optional |  | 已成交数量。  
price | string | Optional |  | 委托价格。  
time_setup | integer(int64) | Optional |  | 委托创建时间。  
avg_fill_price | string | Optional |  | 成交均价。  
fee | string | Optional |  | 手续费。  
time_done | integer(int64) | Optional |  | 委托结束时间。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionOptionChainResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
underlying | string | Optional |  | 期权标的代码。  
expiration_date | string(date) | Optional |  | 期权到期日，格式 YYYY-MM-DD。  
expiration_date_ts | integer(int64) | Optional |  | 到期日对应的 Unix 时间戳。  
index_price | string | Optional |  | 标的指数价格；无有效值时为空。  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
strike_price | string | Optional |  | 行权价。  
option_type | string | Optional | enum: ["call","put"] | 期权类型。  
\- call: 看涨期权。  
\- put: 看跌期权。  
bid | string | Optional |  | 最佳买入报价。  
ask | string | Optional |  | 最佳卖出报价。  
mark_price | string | Optional |  | 标记价格。  
mark_iv | string | Optional |  | 标记隐含波动率。  
last | string | Optional |  | 最新成交价。  
display_price | string | Optional |  | 展示价格。  
breakeven_price | string | Optional |  | 盈亏平衡价格。  
to_breakeven_pct | string | Optional |  | 距离盈亏平衡价格的百分比。  
today_change_pct | string | Optional |  | 今日价格变化百分比。  
open_interest | string | Optional |  | 未平仓合约数量。  
position | string | Optional |  | 仓位数量。  
delta | string | Optional |  | 期权 Delta。  
gamma | string | Optional |  | 期权 Gamma。  
theta | string | Optional |  | 期权 Theta。  
vega | string | Optional |  | 期权 Vega。  
rho | string | Optional |  | 期权 Rho。  
trade_status | string | Optional | enum: ["open","closed"] | 合约当前交易状态。  
\- open: 处于可交易时段，且合约及标的均可交易。  
\- closed: 当前不可交易，包括非交易时段、合约非有效状态或标的未启用。  
trade_mode | integer | Optional | enum: [0,4] | 当前交易模式。  
\- 0: 禁止交易。  
\- 4: 允许买入和卖出；普通账户卖出仍须有足够的可用多头持仓。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "underlying": "string",
        "expiration_date": "2026-11-20",
        "expiration_date_ts": 0,
        "index_price": "string",
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionOrderBookResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
bids | array | Optional |  | 买入报价列表；最多一档，无报价时为空数组。  
asks | array | Optional |  | 卖出报价列表；最多一档，无报价时为空数组。  
  
**allOf[1] / data / bids**

买入报价列表；最多一档，无报价时为空数组。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / bids / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
price | string | Optional |  | 报价价格。  
  
**allOf[1] / data / asks**

卖出报价列表；最多一档，无报价时为空数组。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / asks / items**

类型 | 约束  
---|---  
object |   
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "symbol": "string",
        "symbol_display": "string",
        "bids": [
          {}
        ],
        "asks": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionConfigResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
sec | string | Optional |  | SEC 费率。  
min_sec | string | Optional |  | SEC 最低费用。  
max_sec | string | Optional |  | SEC 最高费用；为空表示不限制。  
taf | string | Optional |  | TAF 费率。  
min_taf | string | Optional |  | TAF 最低费用。  
max_taf | string | Optional |  | TAF 最高费用。  
occ | string | Optional |  | OCC 费用。  
orf | string | Optional |  | ORF 费用。  
cat | string | Optional |  | CAT 费用。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "sec": "0.0000206",
        "min_sec": "0.01",
        "max_sec": "",
        "taf": "0.00279",
        "min_taf": "0.01",
        "max_taf": "9.79",
        "occ": "0.025",
        "orf": "0.012",
        "cat": "0.0003"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionUpdateOrderResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托 ID。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "id": "string"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionOrderListSide

委托方向筛选。 不传表示查询全部方向。

  * 1: 仅卖出委托。
  * 2: 仅买入委托。

类型 | 约束  
---|---  
integer |   
  
**枚举值列表**

值  
---  
1  
2  
      
    
    1
    
    

##  StockOptionSymbolListResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
underlying | string | Optional |  | 期权标的代码。  
description | string | Optional |  | 标的描述。  
descs | array | Optional |  | 标的的多语言描述。  
icon_link | string | Optional |  | 标的图标链接。  
price_precision | integer | Optional |  | 价格小数位数。  
min_order_volume | string | Optional |  | 最小委托数量。  
max_order_volume | string | Optional |  | 最大委托数量。  
step_order_volume | string | Optional |  | 委托数量步长。  
  
**allOf[1] / data / list / items / descs**

标的的多语言描述。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items / descs / items**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
lang | string | Optional |  | 语言代码。  
value | string | Optional |  | 该语言的标的描述。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionClosePositionRequest

`order_type` 可选。缺省或为空时按市价平仓；仅支持 `market` 或 `limit`。

类型 | 约束  
---|---  
object | required: ["symbol","quantity"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
symbol | string | Required |  | 要平仓的期权合约代码，须有对应的可用持仓。  
quantity | string | Required |  | 本次平仓数量，使用正数十进制字符串，不得超过可用持仓；须满足合约最小、最大数量和数量步长规则。  
order_type | string | Optional | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
price | string | Optional |  | 限价平仓必填的正数价格，使用普通十进制字符串，最多 64 个字符，不支持科学计数法；市价平仓忽略。  
client_order_id | string | Optional |  | 自定义平仓委托标识；不传或仅为空白时自动生成。  
      
    
    {
      "symbol": "string",
      "quantity": "string",
      "order_type": "market",
      "price": "1.00",
      "client_order_id": "string"
    }
    
    

##  StockOptionOptionType

期权类型。

  * call: 看涨期权。
  * put: 看跌期权。

类型 | 约束  
---|---  
string |   
  
**枚举值列表**

值  
---  
"call"  
"put"  
      
    
    "call"
    
    

##  StockOptionApiResponse

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
label | string | Required |  | 业务错误标签。请求成功时为空字符串。  
message | string | Optional |  | 错误信息。请求成功时不返回。  
data | any|null | Required | nullable: true | 业务响应数据。  
timestamp | integer(int64) | Required |  | 服务器时间戳（毫秒）。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1785919118845
    }
    
    

##  StockOptionPositionPnlPriceType

仓位盈亏计价价格类型。

  * latest: 最新成交价；不传或为空时使用此值。
  * mark: 标记价格。

类型 | 约束  
---|---  
string | default: "latest"  
  
**枚举值列表**

值  
---  
"latest"  
"mark"  
      
    
    "latest"
    
    

##  StockOptionPutOrderResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | string | Optional |  | 委托 ID。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "id": "string"
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionOrderListResponse

类型 | 约束  
---|---  
allOf |   
  
**allOf[0]**

类型 | 约束  
---|---  
object | required: ["label","data","timestamp"]  
  
**allOf[1]**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
list | array | Optional |  | 查询结果列表。  
  
**allOf[1] / data / list**

查询结果列表。

类型 | 约束  
---|---  
array |   
  
**allOf[1] / data / list / items**

当前未结束的委托，不包含全部成交、已撤销或下单拒绝的终态委托。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
order_id | string | Optional |  | 委托 ID。  
symbol | string | Optional |  | 完整期权合约代码。  
symbol_display | string | Optional |  | 用于展示的期权合约名称。  
underlying | string | Optional |  | 期权标的代码。  
side | integer | Optional | enum: [1,2] | 委托方向。  
\- 1: 卖出。  
\- 2: 买入。  
order_type | string | Optional | enum: ["market","limit"] | 委托类型。  
\- market: 市价委托，按可成交的市场价格执行。  
\- limit: 限价委托，须提供委托价格 price。  
status | integer | Optional | enum: [1,2] | 当前委托状态：  
\- 1: 新订单，已验证并等待处理。  
\- 2: 部分成交，仍有未成交数量。  
status_desc | string | Optional |  | 委托状态的可读说明，随请求语言返回。  
time_in_force | string | Optional | enum: ["day","gtc"] | 委托有效期。限价单支持 day、gtc；市价单仅支持 day。  
\- day: 当日有效，未成交部分在当日有效期结束后取消。  
\- gtc: 撤销前有效。  
平仓接口固定使用 day。  
quantity | string | Optional |  | 委托数量。  
filled_quantity | string | Optional |  | 已成交数量。  
price | string | Optional |  | 委托价格。  
time_setup | integer(int64) | Optional |  | 委托创建时间。  
      
    
    {
      "label": "",
      "message": "invalid argument",
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 1785919118845
    }
    
    

##  StockOptionCancelAllOrdersRequest

批量撤销限价委托的筛选条件；side 为 1（卖出）或 2（买入），不传时不区分方向。

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
underlying | string | Optional |  | 期权标的代码；为空或不传时不指定标的筛选条件。  
symbol | string | Optional |  | 期权合约代码；为空或不传时不指定合约筛选条件。  
side | integer | Optional | enum: [1,2] | 委托方向筛选。  
不传表示查询全部方向。  
\- 1: 仅卖出委托。  
\- 2: 仅买入委托。  
      
    
    {
      "underlying": "AAPL",
      "symbol": "string",
      "side": 1
    }