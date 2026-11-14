---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/stock
api_type: REST
updated_at: 2026-11-13 20:58:09.801857
---

# 股票

股票业务提供传统金融股票现货交易能力。接口返回 APIV4 兼容响应结构，成功返回 `data` 与 `timestamp`，失败返回 `label`、`message`、`data` 与 `timestamp`。

  * REST API BaseURL 实盘交易: `https://api.gateio.ws/api/v4/`
  * 文档路由前缀: `/stock`
  * APIv4 带单交易需添加请求头 `x-gate-trader-copy-type: stock_copy`（带单交易不含资金转入转出、资金流水接口）

##  查询用户资产🔒 需要认证

GET`/stock/users/assets`

GET `/stock/users/assets`

_查询用户资产_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
pnl_calc_type | 请求参数 | integer | 否 | 盈亏计算成本类型，不传默认按平均成本价计算（1=平均成本价，2=摊薄成本价）  
pnl_calc_price | 请求参数 | integer | 否 | 盈亏计算价格类型，不传默认按盘中价计算（1=盘中价，2=延长时段最新价格）  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
pnl_calc_type | 1  
pnl_calc_type | 2  
pnl_calc_price | 1  
pnl_calc_price | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradfiSpotUserAssetResp  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» equity | string | 账户净值  
»» balance | string | 账户余额  
»» available | string | 可用余额  
»» loan_amount | string | 借款金额。非负；由原始可用余额为负时取其绝对值，否则为 0。  
»» buy_power | string | 购买力  
»» leverage | string | 杠杆  
»» leave_liquidity | string | 剩余流动性  
»» leave_liquidity_rate | string | 剩余流动性比率  
»» aee | string | 可用资产（Available Excess Equity）  
»» options_margin | string | 期权保证金  
»» position_market_value | string | 持仓市值  
»» position_pnl | string | 持仓盈亏  
»» today_pnl | string | 今日盈亏  
»» option_position_market_value | string | 期权持仓市值  
»» option_position_pnl | string | 期权持仓盈亏  
»» option_today_pnl | string | 期权今日盈亏  
»» user_exists | boolean | 用户是否已开通业务  
»» margin_enabled | boolean | 是否已开启融资功能  
»» long_borrowing_rate | string | 融资年利率。空字符串表示暂无有效利率。  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/users/assets'
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
    url="/stock/users/assets"
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
      "data": {
        "equity": "10000.12",
        "balance": "8000",
        "available": "6500.5",
        "loan_amount": "0",
        "buy_power": "13000",
        "leverage": "2",
        "leave_liquidity": "5000",
        "leave_liquidity_rate": "0.5",
        "aee": "4800",
        "options_margin": "0",
        "position_market_value": "1500.25",
        "position_pnl": "12.5",
        "today_pnl": "3.2",
        "option_position_market_value": "0",
        "option_position_pnl": "0",
        "option_today_pnl": "0",
        "user_exists": true,
        "margin_enabled": true,
        "long_borrowing_rate": "0.03"
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  设置融资功能开关🔒 需要认证

PUT`/stock/users/margin-feature`

PUT `/stock/users/margin-feature`

_设置融资功能开关_

限流：5 qps。 开启或关闭用户融资功能。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | TradFiSpotSetMarginFeatureRequest | 是 |   
» margin_feature | body | boolean | 是 | 是否开启融资功能。true 表示开启，false 表示关闭。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | SetMarginFeature  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object | 成功时返回空对象  
» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/users/margin-feature'
    query_param = ''
    body='{"margin_feature":true}'
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
    url="/stock/users/margin-feature"
    query_param=""
    body_param='{"margin_feature":true}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "margin_feature": true
    }
    

> 返回示例

> 200 返回
    
    
    {
      "data": {},
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询股票交易对列表

GET`/stock/symbols`

GET `/stock/symbols`

_查询股票交易对列表_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 否 | 交易对代码列表，多个用英文逗号分隔  
exchange | 请求参数 | string | 否 | 交易市场代码。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
with_desc_i18n | 请求参数 | boolean | 否 | 是否返回多语言交易对描述  
page | 请求参数 | integer | 否 | 页码，不传默认第 1 页  
page_size | 请求参数 | integer | 否 | 每页数量，不传默认 10，最大 500；超过 500 时服务端按 500 处理。  
  
####  详细描述

**exchange** : 交易市场代码。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradfiSpotSymbols  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» total | integer(int64) | 总数量  
»» total_page | integer | 总页数  
»» list | array | 交易对列表  
»»» symbol | string | 交易对代码  
»»» exchange | string | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»»» exchange_desc | string | 交易所描述  
»»» quote_currency | string | 报价币种  
»»» quote_currency_precision | integer | 报价币种精度  
»»» fx_rate | string | 报价币种对美元的汇率  
»»» symbol_desc | string | 交易对描述  
»»» category | string | Symbol 分类。  
\- CS: 股票。  
\- ETF: 交易所基金。  
\- ADRC、ADR: 美股里的外国公司股票凭证。  
\- ETV: 交易所交易产品。  
\- PFD: 优先股。  
\- ETS: 交易所交易证券。  
\- ETN: 交易所票据。  
\- FUND: 基金。  
»»» asset_type | string | 资产类型。  
\- STOCK: 股票。  
\- ETF: 交易所基金。  
»»» trade_status | string | 交易状态。  
\- pre_market: 盘前。  
\- open: 盘中。  
\- post_market: 盘后。  
»»» trade_mode | integer | 当前时段交易模式。  
\- 0: 禁止交易。  
\- 1: 仅允许买入。  
\- 2: 仅允许卖出。  
\- 4: 支持买入和卖出。  
\- 5: 交易暂停。  
\- 6: 交易暂停。  
\- 7: 交易暂停。  
\- 8: 交易暂停。  
»»» order_fill_timing | integer | 下单可成交时机（1=立即成交，2=盘前开始后可成交，3=盘中开始后可成交）  
»»» icon_link | string | 图标链接  
»»» quote_currency_symbol | string | 报价币种符号  
»»» price_precision | integer | 价格精度  
»»» volume_precision | integer | 数量精度  
»»» is_ipo | boolean | 是否 IPO 交易对  
»»» ipo_price | string | IPO 价格  
»»» sell_price_protection | string | 卖出价格保护比例  
»»» buy_price_protection | string | 买入价格保护比例  
»»» symbol_descs | array | 多语言交易对描述  
»»»» lang | string | 语言  
»»»» value | string | 多语言描述  
»»» margin_mode | integer | 融资融券模式。  
\- 0: 不支持融资融券。  
\- 1: 可融资。  
\- 2: 可融券。  
\- 3: 可融资和融券。  
»»» long_im | string | 多头初始保证金率  
»»» long_mm | string | 多头维持保证金率  
»»» short_im | string | 空头初始保证金率  
»»» short_mm | string | 空头维持保证金率  
»»» long_borrowing_rate | string | 融资年利率。空字符串表示暂无有效利率。  
»»» short_borrowing_rate | string | 融券年利率。空字符串表示暂无有效利率。  
»» timestamp | integer(int64) |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
category | CS  
category | ETF  
category | ADRC  
category | ADR  
category | ETV  
category | PFD  
category | ETS  
category | ETN  
category | FUND  
asset_type | STOCK  
asset_type | ETF  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
order_fill_timing | 1  
order_fill_timing | 2  
order_fill_timing | 3  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/symbols'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/symbols \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "symbol": "AAPL",
            "exchange": "us",
            "exchange_desc": "United States",
            "quote_currency": "USD",
            "quote_currency_precision": 2,
            "fx_rate": "1",
            "symbol_desc": "Apple Inc.",
            "category": "CS",
            "asset_type": "STOCK",
            "trade_status": "open",
            "trade_mode": 4,
            "order_fill_timing": 1,
            "icon_link": "https://static.gate.com/aapl.png",
            "quote_currency_symbol": "$",
            "price_precision": 2,
            "volume_precision": 4,
            "is_ipo": false,
            "sell_price_protection": "0.1",
            "buy_price_protection": "0.1",
            "symbol_descs": [
              {
                "lang": "en",
                "value": "Apple Inc."
              }
            ],
            "margin_mode": 1,
            "long_im": "0.25",
            "long_mm": "0.45",
            "short_im": "0.3",
            "short_mm": "0.5",
            "long_borrowing_rate": "0.03",
            "short_borrowing_rate": ""
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询股票交易对详情

GET`/stock/symbols/detail`

GET `/stock/symbols/detail`

_查询股票交易对详情_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 否 | 交易对代码列表，多个用英文逗号分隔  
exchange | 请求参数 | string | 否 | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
page | 请求参数 | integer | 否 | 页码，不传默认第 1 页  
page_size | 请求参数 | integer | 否 | 每页数量，不传默认 10，最大 500；超过 500 时服务端按 500 处理。  
  
####  详细描述

**exchange** : 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | SymbolDetail  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» total | integer(int64) | 总数量  
»» total_page | integer | 总页数  
»» list | array |   
»»» symbol | string | 交易对代码  
»»» exchange | string | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»»» exchange_desc | string | 交易所描述  
»»» quote_currency | string | 报价币种  
»»» quote_currency_precision | integer | 报价币种精度  
»»» fx_rate | string | 报价币种对美元的汇率  
»»» symbol_desc | string | 交易对描述  
»»» category | string | Symbol 分类。  
\- CS: 股票。  
\- ETF: 交易所基金。  
\- ADRC、ADR: 美股里的外国公司股票凭证。  
\- ETV: 交易所交易产品。  
\- PFD: 优先股。  
\- ETS: 交易所交易证券。  
\- ETN: 交易所票据。  
\- FUND: 基金。  
»»» asset_type | string | 资产类型。  
\- STOCK: 股票。  
\- ETF: 交易所基金。  
»»» settlement_currency | string | 结算币种  
»»» max_order_volume | string | 最大下单数量  
»»» step_order_volume | string | 下单步长  
»»» min_order_volume | string | 最小下单数量  
»»» price_precision | integer | 价格精度  
»»» volume_precision | integer | 数量精度  
»»» is_ipo | boolean | 是否 IPO 交易对  
»»» ipo_price | string | IPO 价格  
»»» price_protection | string | 价格保护范围  
»»» sell_price_protection | string | 卖出价格保护比例  
»»» buy_price_protection | string | 买入价格保护比例  
»»» slippage_rate | string | 滑点  
»»» commission_rate | string | 手续费率  
»»» trade_status | string | 交易状态。  
\- pre_market: 盘前。  
\- open: 盘中。  
\- post_market: 盘后。  
»»» trade_mode | integer | 当前时段交易模式。  
\- 0: 禁止交易。  
\- 1: 仅允许买入。  
\- 2: 仅允许卖出。  
\- 4: 支持买入和卖出。  
\- 5: 交易暂停。  
\- 6: 交易暂停。  
\- 7: 交易暂停。  
\- 8: 交易暂停。  
»»» order_fill_timing | integer | 下单可成交时机（1=立即成交，2=盘前开始后可成交，3=盘中开始后可成交）  
»»» symbol_descs | array | 多语言交易对描述  
»»»» lang | string | 语言  
»»»» value | string | 多语言描述  
»»» icon_link | string | 图标链接  
»»» margin_mode | integer | 融资融券模式。  
\- 0: 不支持融资融券。  
\- 1: 可融资。  
\- 2: 可融券。  
\- 3: 可融资和融券。  
»»» long_im | string | 多头初始保证金率  
»»» long_mm | string | 多头维持保证金率  
»»» short_im | string | 空头初始保证金率  
»»» short_mm | string | 空头维持保证金率  
»»» long_borrowing_rate | string | 融资年利率。空字符串表示暂无有效利率。  
»»» short_borrowing_rate | string | 融券年利率。空字符串表示暂无有效利率。  
»» timestamp | integer(int64) |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
category | CS  
category | ETF  
category | ADRC  
category | ADR  
category | ETV  
category | PFD  
category | ETS  
category | ETN  
category | FUND  
asset_type | STOCK  
asset_type | ETF  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
order_fill_timing | 1  
order_fill_timing | 2  
order_fill_timing | 3  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/symbols/detail'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/symbols/detail \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "symbol": "AAPL",
            "exchange": "us",
            "exchange_desc": "United States",
            "quote_currency": "USD",
            "quote_currency_precision": 2,
            "fx_rate": "1",
            "symbol_desc": "Apple Inc.",
            "category": "CS",
            "asset_type": "STOCK",
            "settlement_currency": "USD",
            "max_order_volume": "10000",
            "step_order_volume": "1",
            "min_order_volume": "1",
            "price_precision": 2,
            "volume_precision": 4,
            "is_ipo": false,
            "ipo_price": "15",
            "price_protection": "0.1",
            "sell_price_protection": "0.1",
            "buy_price_protection": "0.1",
            "slippage_rate": "0.001",
            "commission_rate": "0.001",
            "trade_status": "open",
            "trade_mode": 4,
            "order_fill_timing": 1,
            "symbol_descs": [
              {
                "lang": "en",
                "value": "Apple Inc."
              }
            ],
            "icon_link": "https://static.gate.com/aapl.png",
            "margin_mode": 1,
            "long_im": "0.25",
            "long_mm": "0.45",
            "short_im": "0.3",
            "short_mm": "0.5",
            "long_borrowing_rate": "0.03",
            "short_borrowing_rate": ""
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询市场订单簿

GET`/stock/market/{symbol}/orderbook`

GET `/stock/market/{symbol}/orderbook`

_查询市场订单簿_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | URL | string | 是 | 交易对代码  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradfiSpotOrderBook  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» symbol | string | 交易对代码  
»» bids | array | 买盘  
»»» p | string | 价格  
»»» user_order | boolean | 是否为用户自己的订单  
»» asks | array | 卖盘  
»»» p | string | 价格  
»»» user_order | boolean | 是否为用户自己的订单  
»» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/market/AAPL/orderbook'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/market/AAPL/orderbook \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "symbol": "AAPL",
        "bids": [
          {
            "p": "200.11",
            "user_order": false
          }
        ],
        "asks": [
          {
            "p": "200.12",
            "user_order": false
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询当前委托单列表🔒 需要认证

GET`/stock/orders`

GET `/stock/orders`

_查询当前委托单列表_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | 请求参数 | string | 否 | 交易对代码  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradfiSpotOrderList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» list | array | 当前委托单列表  
»»» order_id | string | 订单 ID  
»»» symbol | string | 交易对代码  
»»» exchange | string | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»»» quote_currency | string | 报价币种  
»»» fx_rate | string | 报价币种对美元的汇率  
»»» symbol_desc | string | 交易对描述  
»»» trade_status | string | 交易状态。  
\- pre_market: 盘前。  
\- open: 盘中。  
\- post_market: 盘后。  
»»» trade_mode | integer | 当前时段交易模式。  
\- 0: 禁止交易。  
\- 1: 仅允许买入。  
\- 2: 仅允许卖出。  
\- 4: 支持买入和卖出。  
\- 5: 交易暂停。  
\- 6: 交易暂停。  
\- 7: 交易暂停。  
\- 8: 交易暂停。  
»»» price_type | string | 价格类型（market=市价，limit=限价）  
»»» side | integer | 买卖方向（1=卖，2=买）  
»»» status | integer | 订单状态。  
\- 0: 未知。  
\- 1: 新订单，订单已验证，等待处理。  
\- 2: 部分成交。  
\- 3: 全部成交。  
\- 4: 已撤销。  
\- 5: 下单被拒绝。  
\- 6: 撤单被拒绝。  
\- 7: 改单成功。  
\- 8: 改单拒绝。  
»»» volume | string | 委托数量  
»»» fill_volume | string | 成交数量  
»»» price | string | 委托价格  
»»» time_setup | integer(int64) | 下单时间（Unix 时间戳，秒）  
»»» time_update | integer(int64) | 订单更新时间（Unix 时间戳，秒）  
»»» max_order_volume | string | 最大下单数量  
»»» step_order_volume | string | 下单步长  
»»» min_order_volume | string | 最小下单数量  
»»» price_precision | integer | 价格精度  
»»» price_protection | string | 价格保护范围  
»»» sell_price_protection | string | 卖出价格保护比例  
»»» buy_price_protection | string | 买入价格保护比例  
»»» commission_rate | string | 手续费率  
»»» slippage_rate | string | 滑点  
»» timestamp | integer(int64) |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
price_type | market  
price_type | limit  
side | 1  
side | 2  
status | 0  
status | 1  
status | 2  
status | 3  
status | 4  
status | 5  
status | 6  
status | 7  
status | 8  
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/orders'
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
    url="/stock/orders"
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
      "data": {
        "list": [
          {
            "order_id": "123456",
            "symbol": "AAPL",
            "exchange": "us",
            "quote_currency": "USD",
            "fx_rate": "1",
            "symbol_desc": "Apple Inc.",
            "trade_status": "open",
            "trade_mode": 3,
            "price_type": "limit",
            "side": 2,
            "status": 1,
            "volume": "10",
            "fill_volume": "2",
            "price": "200.12",
            "time_setup": 1769378400,
            "time_update": 1769378500,
            "max_order_volume": "10000",
            "step_order_volume": "1",
            "min_order_volume": "1",
            "price_precision": 2,
            "price_protection": "0.1",
            "sell_price_protection": "0.1",
            "buy_price_protection": "0.1",
            "commission_rate": "0.001",
            "slippage_rate": "0.001"
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  下单🔒 需要认证

POST`/stock/orders`

POST `/stock/orders`

_下单_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | TradFiSpotOrderRequest | 是 |   
» volume | body | string | 是 | 下单数量  
» symbol | body | string | 是 | 交易对代码  
» side | body | integer | 是 | 买卖方向（1=卖，2=买）  
» price_type | body | string | 是 | 价格类型（market=市价，limit=限价）  
» trading_session | body | string | 是 | 交易时段。  
限价单仅支持 all，市价单仅支持 regular。  
» time_in_force | body | string | 是 | 订单有效方式。  
\- day: 当日有效。  
» price | body | string | 否 | 委托价格，限价单使用  
» client_order_id | body | string | 否 | 客户端自定义订单 ID  
  
####  详细描述

**» trading_session** : 交易时段。  
限价单仅支持 all，市价单仅支持 regular。

**» time_in_force** : 订单有效方式。  
\- day: 当日有效。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» side | 1  
» side | 2  
» price_type | market  
» price_type | limit  
» trading_session | regular  
» trading_session | all  
» time_in_force | day  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 下单成功 | TradfiSpotCreateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» id | string | 订单 ID  
» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/orders'
    query_param = ''
    body='{"volume":"10","symbol":"AAPL","side":2,"price_type":"limit","trading_session":"all","time_in_force":"day","price":"200.12","client_order_id":"client-202607070001"}'
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
    url="/stock/orders"
    query_param=""
    body_param='{"volume":"10","symbol":"AAPL","side":2,"price_type":"limit","trading_session":"all","time_in_force":"day","price":"200.12","client_order_id":"client-202607070001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "volume": "10",
      "symbol": "AAPL",
      "side": 2,
      "price_type": "limit",
      "trading_session": "all",
      "time_in_force": "day",
      "price": "200.12",
      "client_order_id": "client-202607070001"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "id": "123456"
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  撤销全部委托单🔒 需要认证

DELETE`/stock/orders`

DELETE `/stock/orders`

_撤销全部委托单_

限流：5 qps。

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | DeleteOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object | 成功时返回空对象  
» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/orders'
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
    url="/stock/orders"
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
      "data": {},
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询历史委托单列表🔒 需要认证

GET`/stock/orders/history`

GET `/stock/orders/history`

_查询历史委托单列表_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | 请求参数 | string | 否 | 交易对代码  
order_ids | 请求参数 | string | 否 | 订单 ID 列表，多个用英文逗号分隔；最多支持 20 个，且每个 ID 必须为正整数。  
begin_time | 请求参数 | integer(int32) | 否 | 开始时间（Unix 时间戳，秒）。begin_time 和 end_time 同时传入时，end_time 必须大于等于 begin_time，且查询时间跨度不能超过 3 个月。  
end_time | 请求参数 | integer(int32) | 否 | 结束时间（Unix 时间戳，秒）。begin_time 和 end_time 同时传入时，end_time 必须大于等于 begin_time，且查询时间跨度不能超过 3 个月。  
side | 请求参数 | integer | 否 | 买卖方向（1=卖，2=买）  
page | 请求参数 | integer | 否 | 页码，不传默认第 1 页  
page_size | 请求参数 | integer | 否 | 每页数量，不传默认 10，最大 500；超过 500 时服务端按 500 处理。  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
side | 1  
side | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradfiSpotOrderHistoryList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» total | integer(int64) | 总数量  
»» total_page | integer | 总页数  
»» list | array | 历史委托单列表  
»»» order_id | string | 订单 ID  
»»» symbol | string | 交易对代码  
»»» exchange | string | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»»» quote_currency | string | 报价币种  
»»» fx_rate | string | 报价币种对美元的汇率  
»»» symbol_desc | string | 交易对描述  
»»» price_type | string | 价格类型（market=市价，limit=限价）  
»»» status | integer | 订单状态。  
\- 0: 未知。  
\- 1: 新订单，订单已验证，等待处理。  
\- 2: 部分成交。  
\- 3: 全部成交。  
\- 4: 已撤销。  
\- 5: 下单被拒绝。  
\- 6: 撤单被拒绝。  
\- 7: 改单成功。  
\- 8: 改单拒绝。  
»»» status_desc | string | 订单状态描述  
»»» status_detail | object|null | 订单状态详情  
»»»» title | string | 状态标题  
»»»» message | string | 状态说明  
»»» finish_as | integer | 订单完成原因。  
\- 0: 未知。  
\- 1: 没有找到报价。  
\- 2: 没有找到匹配。  
\- 3: 触发价格超出。  
\- 4: 订单价值超出限制。  
\- 5: 拒单未知。  
\- 6: 撤单未知。  
\- 7: 用户主动撤销。  
\- 8: 超过订单有效期自动撤单。  
\- 9: 当前交易时段暂不支持交易。  
\- 13: 公司行动撤单。  
»»» side | integer | 买卖方向（1=卖，2=买）  
»»» time_in_force | string | 订单有效方式。  
\- day: 当日有效。  
»»» volume | string | 委托数量  
»»» fill_volume | string | 成交数量  
»»» price | string | 委托价格  
»»» avg_fill_price | string|null | 平均成交价格  
»»» commission | string | 手续费  
»»» time_setup | integer(int64) | 下单时间（Unix 时间戳，秒）  
»»» time_done | integer(int64) | 订单完成时间（Unix 时间戳，秒）  
»» timestamp | integer(int64) |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
price_type | market  
price_type | limit  
status | 0  
status | 1  
status | 2  
status | 3  
status | 4  
status | 5  
status | 6  
status | 7  
status | 8  
finish_as | 0  
finish_as | 1  
finish_as | 2  
finish_as | 3  
finish_as | 4  
finish_as | 5  
finish_as | 6  
finish_as | 7  
finish_as | 8  
finish_as | 9  
finish_as | 13  
side | 1  
side | 2  
time_in_force | day  
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/orders/history'
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
    url="/stock/orders/history"
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
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "order_id": "123456",
            "symbol": "AAPL",
            "exchange": "us",
            "quote_currency": "USD",
            "fx_rate": "1",
            "symbol_desc": "Apple Inc.",
            "price_type": "limit",
            "status": 3,
            "status_desc": "filled",
            "status_detail": {
              "title": "Filled",
              "message": "Order filled"
            },
            "finish_as": 0,
            "side": 2,
            "time_in_force": "day",
            "volume": "10",
            "fill_volume": "10",
            "price": "200.12",
            "avg_fill_price": "200.10",
            "commission": "2.001",
            "time_setup": 1769378400,
            "time_done": 1769378500
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询订单成交流水🔒 需要认证

GET`/stock/orders/deals`

GET `/stock/orders/deals`

_查询订单成交流水_

限流：5 qps。 按订单 ID 查询当前用户的成交流水。`price`、`value`、`fee` 以标的交易币种计价（如美股 USD、港股 HKD、日股 JPY、韩股 KRW）。 `role` 返回 `maker` 或 `taker`。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | 请求参数 | integer(int64) | 是 | 订单 ID  
page | 请求参数 | integer | 否 | 页码，不传默认第 1 页  
page_size | 请求参数 | integer | 否 | 每页数量，不传默认 10，最大 100；超过 100 时服务端按 100 处理。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | OrderDealList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» total | integer(int64) | 总数量  
»» total_page | integer(int64) | 总页数  
»» list | array | 成交流水列表  
»»» id | integer(int64) | 成交流水主键 ID  
»»» deal_id | integer(int64) | 成交 ID  
»»» order_id | integer(int64) | 订单 ID  
»»» client_order_id | string | 客户端自定义订单 ID  
»»» user_id | integer | 用户 ID  
»»» symbol | string | 交易对代码  
»»» exchange | string | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»»» side | integer | 买卖方向（1=卖，2=买）  
»»» role | string | 成交角色。  
\- maker: 挂单方。  
\- taker: 吃单方。  
»»» price | string | 成交价格，以标的交易币种计价  
»»» quantity | string | 成交数量  
»»» position_qty | string | 成交后持仓数量  
»»» avg_entry_price | string | 平均开仓价格  
»»» value | string | 成交金额，以标的交易币种计价  
»»» fx_rate | string | 报价币种对美元的汇率  
»»» fee | string | 手续费，以标的交易币种计价  
»» timestamp | integer(int64) |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
side | 1  
side | 2  
role | maker  
role | taker  
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/orders/deals'
    query_param = 'order_id=123456'
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
    url="/stock/orders/deals"
    query_param="order_id=123456"
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
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "id": 10001,
            "deal_id": 90001,
            "order_id": 123456,
            "client_order_id": "client-202607070001",
            "user_id": 100001,
            "symbol": "AAPL",
            "exchange": "us",
            "side": 2,
            "role": "taker",
            "price": "200.10",
            "quantity": "5",
            "position_qty": "15",
            "avg_entry_price": "198.50",
            "value": "1000.50",
            "fx_rate": "1",
            "fee": "1.001"
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  修改委托单🔒 需要认证

PUT`/stock/orders/{order_id}`

PUT `/stock/orders/{order_id}`

_修改委托单_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | TradFiSpotOrderUpdateRequest | 是 |   
» volume | body | string | 是 | 修改后的委托数量  
» price | body | string | 是 | 修改后的委托价格  
order_id | URL | integer(int64) | 是 | 订单 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradfiSpotUpdateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» order_id | integer(int64) | 订单 ID  
» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/orders/123456'
    query_param = ''
    body='{"volume":"8","price":"201.23"}'
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
    url="/stock/orders/123456"
    query_param=""
    body_param='{"volume":"8","price":"201.23"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "volume": "8",
      "price": "201.23"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  撤销委托单🔒 需要认证

DELETE`/stock/orders/{order_id}`

DELETE `/stock/orders/{order_id}`

_撤销委托单_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | integer(int64) | 是 | 订单 ID  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | DeleteOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object | 成功时返回空对象  
» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/orders/123456'
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
    url="/stock/orders/123456"
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
      "data": {},
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询当前仓位列表🔒 需要认证

GET`/stock/positions`

GET `/stock/positions`

_查询当前仓位列表_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
pnl_calc_type | 请求参数 | integer | 否 | 盈亏计算成本类型，不传默认按平均成本价计算（1=平均成本价，2=摊薄成本价）  
pnl_calc_price | 请求参数 | integer | 否 | 盈亏计算价格类型，不传默认按盘中价计算（1=盘中价，2=延长时段最新价格）  
symbol | 请求参数 | string | 否 | 交易对代码  
exchange | 请求参数 | string | 否 | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
  
####  详细描述

**exchange** : 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
pnl_calc_type | 1  
pnl_calc_type | 2  
pnl_calc_price | 1  
pnl_calc_price | 2  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradfiSpotPositionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» list | array | 当前仓位列表  
»»» symbol | string | 交易对代码  
»»» exchange | string | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»»» quote_currency | string | 报价币种  
»»» quote_currency_precision | integer | 报价币种精度  
»»» fx_rate | string | 报价币种对美元的汇率  
»»» trade_status | string | 交易状态。  
\- pre_market: 盘前。  
\- open: 盘中。  
\- post_market: 盘后。  
»»» symbol_desc | string | 交易对描述  
»»» position_pnl | string | 持仓盈亏  
»»» today_pnl | string | 今日盈亏  
»»» pnl_rate | string | 收益率  
»»» today_sell_amount | string | 今日卖出额  
»»» today_buy_amount | string | 今日买入额  
»»» today_sell_volume | string | 今日卖出量  
»»» today_buy_volume | string | 今日买入量  
»»» yesterday_volume | string | 昨日收盘持仓量  
»»» volume | string | 持仓量  
»»» available | string | 可用持仓量  
»»» transfer_out_pending_qty | string | 股票转出处理中数量  
»»» avg_cost_price | string | 成本价  
»»» diluted_cost_price | string | 摊薄成本价  
»»» last_price | string | 最新价格  
»»» extended_last_price | string|null | 延长时段最新价格  
»»» max_order_volume | string | 最大下单数量  
»»» step_order_volume | string | 下单步长  
»»» min_order_volume | string | 最小下单数量  
»»» price_precision | integer | 价格精度  
»»» price_protection | string | 价格保护范围  
»»» sell_price_protection | string | 卖出价格保护比例  
»»» buy_price_protection | string | 买入价格保护比例  
»»» commission_rate | string | 手续费率  
»»» slippage_rate | string | 滑点  
»» timestamp | integer(int64) |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/positions'
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
    url="/stock/positions"
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
      "data": {
        "list": [
          {
            "symbol": "AAPL",
            "exchange": "us",
            "quote_currency": "USD",
            "quote_currency_precision": 2,
            "fx_rate": "1",
            "trade_status": "open",
            "symbol_desc": "Apple Inc.",
            "position_pnl": "12.5",
            "today_pnl": "3.2",
            "pnl_rate": "0.012",
            "today_sell_amount": "0",
            "today_buy_amount": "2001.2",
            "today_sell_volume": "0",
            "today_buy_volume": "10",
            "yesterday_volume": "8",
            "volume": "10",
            "available": "8",
            "transfer_out_pending_qty": "0",
            "avg_cost_price": "198.11",
            "diluted_cost_price": "198.11",
            "last_price": "200.12",
            "extended_last_price": "200.2",
            "max_order_volume": "10000",
            "step_order_volume": "1",
            "min_order_volume": "1",
            "price_precision": 2,
            "price_protection": "0.1",
            "sell_price_protection": "0.1",
            "buy_price_protection": "0.1",
            "commission_rate": "0.001",
            "slippage_rate": "0.001"
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  平仓🔒 需要认证

POST`/stock/positions/close`

POST `/stock/positions/close`

_平仓_

限流：5 qps。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | TradFiSpotClosePositionRequest | 是 |   
» symbol | body | string | 是 | 交易对代码  
» close_volume | body | string | 否 | 平仓数量；部分平仓时必填  
» close_type | body | integer | 是 | 平仓类型（1=部分平仓，2=全平）  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» close_type | 1  
» close_type | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | ClosePosition  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» order_id | integer(int64) | 平仓订单 ID  
» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/positions/close'
    query_param = ''
    body='{"symbol":"AAPL","close_volume":"2","close_type":1}'
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
    url="/stock/positions/close"
    query_param=""
    body_param='{"symbol":"AAPL","close_volume":"2","close_type":1}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "symbol": "AAPL",
      "close_volume": "2",
      "close_type": 1
    }
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询资金流水🔒 需要认证

GET`/stock/transactions`

GET `/stock/transactions`

_查询资金流水_

限流：5 qps。 查询股票账户资金流水，包括资金转入转出、交易买卖、手续费、分红派息、奖励和股票转移等流水。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
begin_time | 请求参数 | integer(int64) | 否 | 开始时间（Unix 时间戳，秒）。begin_time 和 end_time 同时传入时，end_time 必须大于等于 begin_time，且查询时间跨度不能超过 3 个月。  
end_time | 请求参数 | integer(int64) | 否 | 结束时间（Unix 时间戳，秒）。begin_time 和 end_time 同时传入时，end_time 必须大于等于 begin_time，且查询时间跨度不能超过 3 个月。  
ref_id | 请求参数 | string | 否 | 业务幂等 ID。传入 ref_id 时服务端按 ref_id 查询，会忽略 begin_time、end_time、type、page、page_size 等其它查询条件。  
type | 请求参数 | string | 否 | 流水类型。  
\- deposit: 资金转入，从现货账户转入到股票账户。  
\- withdraw: 资金转出，从股票账户转出到现货账户。  
\- fee: 交易手续费。  
\- dividend: 分红派息。  
\- sell: 卖出股票入账。  
\- buy: 买入股票出账。  
\- award: 空投奖励。  
\- stock_transfer_in: 股票转入。  
\- stock_transfer_out: 股票转出。  
page | 请求参数 | integer | 否 | 页码，不传默认第 1 页  
page_size | 请求参数 | integer | 否 | 每页数量，不传默认 10，最大 500；超过 500 时服务端按 500 处理。  
  
####  详细描述

**type** : 流水类型。  
\- deposit: 资金转入，从现货账户转入到股票账户。  
\- withdraw: 资金转出，从股票账户转出到现货账户。  
\- fee: 交易手续费。  
\- dividend: 分红派息。  
\- sell: 卖出股票入账。  
\- buy: 买入股票出账。  
\- award: 空投奖励。  
\- stock_transfer_in: 股票转入。  
\- stock_transfer_out: 股票转出。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
type | deposit  
type | withdraw  
type | fee  
type | dividend  
type | sell  
type | buy  
type | award  
type | stock_transfer_in  
type | stock_transfer_out  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradfiSpotTransactionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» total | integer(int64) |   
»» total_page | integer(int64) |   
»» list | array | 资金流水列表  
»»» asset | string | 资产  
»»» symbol | string | 交易对代码  
»»» symbol_display | string | 交易对展示名  
»»» type | string | 流水类型。  
\- deposit: 资金转入。  
\- withdraw: 资金转出。  
\- fee: 交易手续费。  
\- dividend: 分红派息。  
\- sell: 卖出股票入账。  
\- buy: 买入股票出账。  
\- award: 空投奖励。  
\- stock_transfer_in: 股票转入。  
\- stock_transfer_out: 股票转出。  
»»» type_desc | string | 流水类型描述  
»»» change | string | 变动数量。正数表示入账，负数表示出账。  
»»» balance | string | 变动后余额  
»»» ref_id | string | 业务幂等 ID  
»»» time | integer(int64) | 时间戳（秒）  
»»» unit_text | string | 单位展示文案  
»»» detail | object | 业务详情  
»» timestamp | integer(int64) |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | deposit  
type | withdraw  
type | fee  
type | dividend  
type | sell  
type | buy  
type | award  
type | stock_transfer_in  
type | stock_transfer_out  
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/transactions'
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
    url="/stock/transactions"
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
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "asset": "USDT",
            "symbol": "AAPL",
            "symbol_display": "Apple Inc.",
            "type": "deposit",
            "type_desc": "Deposit",
            "change": "100",
            "balance": "1000",
            "ref_id": "transfer-202607070001",
            "time": 1769378400,
            "unit_text": "USDT",
            "detail": {
              "source": "api"
            }
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  资金转入转出🔒 需要认证

POST`/stock/transactions`

POST `/stock/transactions`

_资金转入转出_

限流：5 qps。 资金转入转出用于在现货账户与股票账户之间划转 USDT。

  * deposit: 从现货账户转入到股票账户。
  * withdraw: 从股票账户转出到现货账户。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | TradFiSpotTransactionRequest | 是 |   
» asset | body | string | 是 | 资产，仅支持 USDT  
» change | body | string | 是 | 变动数量，必须大于 0  
» type | body | string | 是 | 交易类型。deposit 表示从现货账户转入到股票账户，withdraw 表示从股票账户转出到现货账户。  
» ref_id | body | string | 是 | 业务幂等 ID  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» asset | USDT  
» type | deposit  
» type | withdraw  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradfiSpotCreateTransaction  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object | 成功时返回空对象  
» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/transactions'
    query_param = ''
    body='{"asset":"USDT","change":"100","type":"deposit","ref_id":"transfer-202607070001"}'
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
    url="/stock/transactions"
    query_param=""
    body_param='{"asset":"USDT","change":"100","type":"deposit","ref_id":"transfer-202607070001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "asset": "USDT",
      "change": "100",
      "type": "deposit",
      "ref_id": "transfer-202607070001"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "data": {},
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询用户资金流水明细🔒 需要认证

GET`/stock/users/balance-records`

GET `/stock/users/balance-records`

_查询用户资金流水明细_

限流：5 qps。 查询当前用户原始资金流水记录。用户范围来自请求头，不支持通过 query 指定 `user_id`。

  * `type`、`business` 支持英文逗号分隔的多值过滤。
  * `begin_time`、`end_time` 按流水创建时间过滤，单位为秒；同时传入时 `end_time` 必须大于 `begin_time`。
  * 结果始终按主键 `id` 排序；`sort_direction` 支持 `asc` 或 `desc`。默认按 `id desc`；传入 `start_id` 且未指定 `sort_direction` 时按 `id asc`，且仅返回 `id > start_id` 的记录，便于增量补数。
  * `detail` 默认不返回；仅当 `include_detail=true` 时返回。
  * `stock_change` 在股票数量类流水中从 `detail.amount` 解析；`balance` 为资金余额快照，不是股票持仓余额。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
type | 请求参数 | string | 否 | 流水类型，多个用英文逗号分隔  
business | 请求参数 | string | 否 | 业务标识，多个用英文逗号分隔  
symbol | 请求参数 | string | 否 | 交易对代码  
begin_time | 请求参数 | integer(int64) | 否 | 开始时间（Unix 时间戳，秒）。begin_time 和 end_time 同时传入时，end_time 必须大于 begin_time。  
end_time | 请求参数 | integer(int64) | 否 | 结束时间（Unix 时间戳，秒）。begin_time 和 end_time 同时传入时，end_time 必须大于 begin_time。  
start_id | 请求参数 | integer(int64) | 否 | 增量查询起始主键 ID；传入后仅返回 id 大于该值的记录。  
sort_direction | 请求参数 | string | 否 | 按主键 id 排序方向。  
\- asc: 升序。  
\- desc: 降序。  
不传时，未提供 start_id 默认 desc；提供 start_id 默认 asc。  
include_detail | 请求参数 | boolean | 否 | 是否返回 detail 原始字段；不传默认 false  
page | 请求参数 | integer | 否 | 页码，不传默认第 1 页  
page_size | 请求参数 | integer | 否 | 每页数量，不传默认 10，最大 100；超过 100 时服务端按 100 处理。  
  
####  详细描述

**sort_direction** : 按主键 id 排序方向。  
\- asc: 升序。  
\- desc: 降序。  
不传时，未提供 start_id 默认 desc；提供 start_id 默认 asc。

####  枚举值列表

枚举值列表参数 | 值  
---|---  
sort_direction | asc  
sort_direction | desc  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | BalanceRecordList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» total | integer(int64) | 总数量  
»» total_page | integer(int64) | 总页数  
»» list | array | 资金流水明细列表  
»»» id | integer(int64) | 资金流水主键 ID  
»»» user_id | integer | 用户 ID  
»»» change | string | 资金变动数量。正数表示入账，负数表示出账。  
»»» balance | string | 变动后资金余额快照  
»»» stock_change | string | 股票数量变动；股票数量类流水从 detail.amount 解析，其他流水可能为空字符串  
»»» type | string | 流水类型原始值。常见值包括：  
\- deposit: 资金转入。  
\- withdraw: 资金转出。  
\- fee: 交易手续费。  
\- dividend: 分红派息。  
\- sell: 卖出股票入账。  
\- buy: 买入股票出账。  
\- award: 空投奖励。  
\- stock_transfer_in: 股票转入。  
\- stock_transfer_out: 股票转出。  
»»» business | string | 业务标识  
»»» business_id | integer(int64) | 业务关联 ID  
»»» symbol | string | 交易对代码  
»»» detail | string | 原始业务详情 JSON 字符串；仅当请求 include_detail=true 时返回  
»»» version | integer | 记录版本号  
»»» time_create | integer(int64) | 业务时间（Unix 时间戳，秒）  
»»» create_time | integer(int64) | 记录创建时间（Unix 时间戳，秒）  
»» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
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
    
    url = '/stock/users/balance-records'
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
    url="/stock/users/balance-records"
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
      "data": {
        "total": 1,
        "total_page": 1,
        "list": [
          {
            "id": 1001,
            "user_id": 100001,
            "change": "100",
            "balance": "1000",
            "stock_change": "10",
            "type": "deposit",
            "business": "transfer",
            "business_id": 2001,
            "symbol": "AAPL",
            "detail": "{\"amount\":\"10\",\"source\":\"api\"}",
            "version": 1,
            "time_create": 1769378400,
            "create_time": 1769378400
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询支持交易市场

GET`/stock/exchanges`

GET `/stock/exchanges`

_查询支持交易市场_

查询股票现货支持的交易市场及是否支持股票转移。限流：5 qps。

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | Exchanges  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» list | array |   
»»» exchange | string | 交易市场。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»»» exchange_desc | string | 市场展示名称  
»»» icon_link | string | 市场图标  
»»» support_transfer | boolean | 是否支持股票转移  
»» timestamp | integer(int64) |   
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/exchanges'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/exchanges \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "list": [
          {
            "exchange": "us",
            "exchange_desc": "United States",
            "icon_link": "https://static.gate.com/us.png",
            "support_transfer": true
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

##  查询日股、韩股手续费率

GET`/stock/fee-rate`

GET `/stock/fee-rate`

_查询日股、韩股手续费率_

查询日股、韩股手续费率。限流：5 qps。

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | FeeRate  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiSpotError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» list | array |   
»»» vip_level | integer | VIP 等级  
»»» maker_fee | string | 日股、韩股 Maker 手续费率  
»»» taker_fee | string | 日股、韩股 Taker 手续费率  
»» timestamp | integer(int64) |   
  
状态码 **400**

_TradFiSpotError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务错误标签  
» message | string | 错误信息  
» data | object|null | 错误附加数据  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/stock/fee-rate'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/stock/fee-rate \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "list": [
          {
            "vip_level": 0,
            "maker_fee": "0.001",
            "taker_fee": "0.001"
          }
        ]
      },
      "timestamp": 1783411200000
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": null,
      "timestamp": 1783411200000
    }
    

#  模型

##  TradFiSpotError

_TradFiSpotError_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
label | string | false | none | 业务错误标签  
message | string | false | none | 错误信息  
data | object|null | false | none | 错误附加数据  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "invalid argument",
      "data": {},
      "timestamp": 1783411200000
    }
    
    

##  TradfiSpotOrderBook

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» symbol | string | false | none | 交易对代码  
» bids | array | false | none | 买盘  
»» p | string | false | none | 价格  
»» user_order | boolean | false | none | 是否为用户自己的订单  
» asks | [TradfiSpotOrderBook/properties/data/properties/bids/items] | false | none | 卖盘  
timestamp | integer(int64) | false | none | none  
      
    
    {
      "data": {
        "symbol": "AAPL",
        "bids": [
          {}
        ],
        "asks": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  FeeRate

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» list | array | false | none | none  
»» vip_level | integer | false | none | VIP 等级  
»» maker_fee | string | false | none | 日股、韩股 Maker 手续费率  
»» taker_fee | string | false | none | 日股、韩股 Taker 手续费率  
» timestamp | integer(int64) | false | none | none  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotUserAssetResp

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» equity | string | false | none | 账户净值  
» balance | string | false | none | 账户余额  
» available | string | false | none | 可用余额  
» loan_amount | string | false | none | 借款金额。非负；由原始可用余额为负时取其绝对值，否则为 0。  
» buy_power | string | false | none | 购买力  
» leverage | string | false | none | 杠杆  
» leave_liquidity | string | false | none | 剩余流动性  
» leave_liquidity_rate | string | false | none | 剩余流动性比率  
» aee | string | false | none | 可用资产（Available Excess Equity）  
» options_margin | string | false | none | 期权保证金  
» position_market_value | string | false | none | 持仓市值  
» position_pnl | string | false | none | 持仓盈亏  
» today_pnl | string | false | none | 今日盈亏  
» option_position_market_value | string | false | none | 期权持仓市值  
» option_position_pnl | string | false | none | 期权持仓盈亏  
» option_today_pnl | string | false | none | 期权今日盈亏  
» user_exists | boolean | false | none | 用户是否已开通业务  
» margin_enabled | boolean | false | none | 是否已开启融资功能  
» long_borrowing_rate | string | false | none | 融资年利率。空字符串表示暂无有效利率。  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
      
    
    {
      "data": {
        "equity": "10000.12",
        "balance": "8000",
        "available": "6500.5",
        "loan_amount": "0",
        "buy_power": "13000",
        "leverage": "2",
        "leave_liquidity": "5000",
        "leave_liquidity_rate": "0.5",
        "aee": "4800",
        "options_margin": "0",
        "position_market_value": "1500.25",
        "position_pnl": "12.5",
        "today_pnl": "3.2",
        "option_position_market_value": "0",
        "option_position_pnl": "0",
        "option_today_pnl": "0",
        "user_exists": true,
        "margin_enabled": true,
        "long_borrowing_rate": "0.03"
      },
      "timestamp": 0
    }
    
    

##  OrderDealList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» total | integer(int64) | false | none | 总数量  
» total_page | integer(int64) | false | none | 总页数  
» list | array | false | none | 成交流水列表  
»» id | integer(int64) | false | none | 成交流水主键 ID  
»» deal_id | integer(int64) | false | none | 成交 ID  
»» order_id | integer(int64) | false | none | 订单 ID  
»» client_order_id | string | false | none | 客户端自定义订单 ID  
»» user_id | integer | false | none | 用户 ID  
»» symbol | string | false | none | 交易对代码  
»» exchange | string | false | none | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»» side | integer | false | none | 买卖方向（1=卖，2=买）  
»» role | string | false | none | 成交角色。  
\- maker: 挂单方。  
\- taker: 吃单方。  
»» price | string | false | none | 成交价格，以标的交易币种计价  
»» quantity | string | false | none | 成交数量  
»» position_qty | string | false | none | 成交后持仓数量  
»» avg_entry_price | string | false | none | 平均开仓价格  
»» value | string | false | none | 成交金额，以标的交易币种计价  
»» fx_rate | string | false | none | 报价币种对美元的汇率  
»» fee | string | false | none | 手续费，以标的交易币种计价  
» timestamp | integer(int64) | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
side | 1  
side | 2  
role | maker  
role | taker  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotTransactionList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» total | integer(int64) | false | none | none  
» total_page | integer(int64) | false | none | none  
» list | array | false | none | 资金流水列表  
»» asset | string | false | none | 资产  
»» symbol | string | false | none | 交易对代码  
»» symbol_display | string | false | none | 交易对展示名  
»» type | string | false | none | 流水类型。  
\- deposit: 资金转入。  
\- withdraw: 资金转出。  
\- fee: 交易手续费。  
\- dividend: 分红派息。  
\- sell: 卖出股票入账。  
\- buy: 买入股票出账。  
\- award: 空投奖励。  
\- stock_transfer_in: 股票转入。  
\- stock_transfer_out: 股票转出。  
»» type_desc | string | false | none | 流水类型描述  
»» change | string | false | none | 变动数量。正数表示入账，负数表示出账。  
»» balance | string | false | none | 变动后余额  
»» ref_id | string | false | none | 业务幂等 ID  
»» time | integer(int64) | false | none | 时间戳（秒）  
»» unit_text | string | false | none | 单位展示文案  
»» detail | object | false | none | 业务详情  
» timestamp | integer(int64) | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | deposit  
type | withdraw  
type | fee  
type | dividend  
type | sell  
type | buy  
type | award  
type | stock_transfer_in  
type | stock_transfer_out  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotSymbols

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» total | integer(int64) | false | none | 总数量  
» total_page | integer | false | none | 总页数  
» list | array | false | none | 交易对列表  
»» symbol | string | false | none | 交易对代码  
»» exchange | string | false | none | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»» exchange_desc | string | false | none | 交易所描述  
»» quote_currency | string | false | none | 报价币种  
»» quote_currency_precision | integer | false | none | 报价币种精度  
»» fx_rate | string | false | none | 报价币种对美元的汇率  
»» symbol_desc | string | false | none | 交易对描述  
»» category | string | false | none | Symbol 分类。  
\- CS: 股票。  
\- ETF: 交易所基金。  
\- ADRC、ADR: 美股里的外国公司股票凭证。  
\- ETV: 交易所交易产品。  
\- PFD: 优先股。  
\- ETS: 交易所交易证券。  
\- ETN: 交易所票据。  
\- FUND: 基金。  
»» asset_type | string | false | none | 资产类型。  
\- STOCK: 股票。  
\- ETF: 交易所基金。  
»» trade_status | string | false | none | 交易状态。  
\- pre_market: 盘前。  
\- open: 盘中。  
\- post_market: 盘后。  
»» trade_mode | integer | false | none | 当前时段交易模式。  
\- 0: 禁止交易。  
\- 1: 仅允许买入。  
\- 2: 仅允许卖出。  
\- 4: 支持买入和卖出。  
\- 5: 交易暂停。  
\- 6: 交易暂停。  
\- 7: 交易暂停。  
\- 8: 交易暂停。  
»» order_fill_timing | integer | false | none | 下单可成交时机（1=立即成交，2=盘前开始后可成交，3=盘中开始后可成交）  
»» icon_link | string | false | none | 图标链接  
»» quote_currency_symbol | string | false | none | 报价币种符号  
»» price_precision | integer | false | none | 价格精度  
»» volume_precision | integer | false | none | 数量精度  
»» is_ipo | boolean | false | none | 是否 IPO 交易对  
»» ipo_price | string | false | none | IPO 价格  
»» sell_price_protection | string | false | none | 卖出价格保护比例  
»» buy_price_protection | string | false | none | 买入价格保护比例  
»» symbol_descs | [TradfiSpotSymbols/definitions/SymbolListItem/properties/symbol_descs/items] | false | none | 多语言交易对描述  
»» margin_mode | integer | false | none | 融资融券模式。  
\- 0: 不支持融资融券。  
\- 1: 可融资。  
\- 2: 可融券。  
\- 3: 可融资和融券。  
»» long_im | string | false | none | 多头初始保证金率  
»» long_mm | string | false | none | 多头维持保证金率  
»» short_im | string | false | none | 空头初始保证金率  
»» short_mm | string | false | none | 空头维持保证金率  
»» long_borrowing_rate | string | false | none | 融资年利率。空字符串表示暂无有效利率。  
»» short_borrowing_rate | string | false | none | 融券年利率。空字符串表示暂无有效利率。  
» timestamp | integer(int64) | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
category | CS  
category | ETF  
category | ADRC  
category | ADR  
category | ETV  
category | PFD  
category | ETS  
category | ETN  
category | FUND  
asset_type | STOCK  
asset_type | ETF  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
order_fill_timing | 1  
order_fill_timing | 2  
order_fill_timing | 3  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  SetMarginFeature

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | 成功时返回空对象  
timestamp | integer(int64) | false | none | none  
      
    
    {
      "data": {},
      "timestamp": 0
    }
    
    

##  Exchanges

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» list | array | false | none | none  
»» exchange | string | false | none | 交易市场。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»» exchange_desc | string | false | none | 市场展示名称  
»» icon_link | string | false | none | 市场图标  
»» support_transfer | boolean | false | none | 是否支持股票转移  
» timestamp | integer(int64) | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  DeleteOrder

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | 成功时返回空对象  
timestamp | integer(int64) | false | none | none  
      
    
    {
      "data": {},
      "timestamp": 0
    }
    
    

##  BalanceRecordList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» total | integer(int64) | false | none | 总数量  
» total_page | integer(int64) | false | none | 总页数  
» list | array | false | none | 资金流水明细列表  
»» id | integer(int64) | false | none | 资金流水主键 ID  
»» user_id | integer | false | none | 用户 ID  
»» change | string | false | none | 资金变动数量。正数表示入账，负数表示出账。  
»» balance | string | false | none | 变动后资金余额快照  
»» stock_change | string | false | none | 股票数量变动；股票数量类流水从 detail.amount 解析，其他流水可能为空字符串  
»» type | string | false | none | 流水类型原始值。常见值包括：  
\- deposit: 资金转入。  
\- withdraw: 资金转出。  
\- fee: 交易手续费。  
\- dividend: 分红派息。  
\- sell: 卖出股票入账。  
\- buy: 买入股票出账。  
\- award: 空投奖励。  
\- stock_transfer_in: 股票转入。  
\- stock_transfer_out: 股票转出。  
»» business | string | false | none | 业务标识  
»» business_id | integer(int64) | false | none | 业务关联 ID  
»» symbol | string | false | none | 交易对代码  
»» detail | string | false | none | 原始业务详情 JSON 字符串；仅当请求 include_detail=true 时返回  
»» version | integer | false | none | 记录版本号  
»» time_create | integer(int64) | false | none | 业务时间（Unix 时间戳，秒）  
»» create_time | integer(int64) | false | none | 记录创建时间（Unix 时间戳，秒）  
» timestamp | integer(int64) | false | none | none  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotOrderRequest

_下单请求参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
volume | string | true | none | 下单数量  
symbol | string | true | none | 交易对代码  
side | integer | true | none | 买卖方向（1=卖，2=买）  
price_type | string | true | none | 价格类型（market=市价，limit=限价）  
trading_session | string | true | none | 交易时段。  
限价单仅支持 all，市价单仅支持 regular。  
time_in_force | string | true | none | 订单有效方式。  
\- day: 当日有效。  
price | string | false | none | 委托价格，限价单使用  
client_order_id | string | false | none | 客户端自定义订单 ID  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
side | 1  
side | 2  
price_type | market  
price_type | limit  
trading_session | regular  
trading_session | all  
time_in_force | day  
      
    
    {
      "volume": "10",
      "symbol": "AAPL",
      "side": 2,
      "price_type": "limit",
      "trading_session": "all",
      "time_in_force": "day",
      "price": "200.12",
      "client_order_id": "client-202607070001"
    }
    
    

##  TradfiSpotCreateTransaction

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | 成功时返回空对象  
timestamp | integer(int64) | false | none | none  
      
    
    {
      "data": {},
      "timestamp": 0
    }
    
    

##  TradfiSpotOrderHistoryList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» total | integer(int64) | false | none | 总数量  
» total_page | integer | false | none | 总页数  
» list | array | false | none | 历史委托单列表  
»» order_id | string | false | none | 订单 ID  
»» symbol | string | false | none | 交易对代码  
»» exchange | string | false | none | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»» quote_currency | string | false | none | 报价币种  
»» fx_rate | string | false | none | 报价币种对美元的汇率  
»» symbol_desc | string | false | none | 交易对描述  
»» price_type | string | false | none | 价格类型（market=市价，limit=限价）  
»» status | integer | false | none | 订单状态。  
\- 0: 未知。  
\- 1: 新订单，订单已验证，等待处理。  
\- 2: 部分成交。  
\- 3: 全部成交。  
\- 4: 已撤销。  
\- 5: 下单被拒绝。  
\- 6: 撤单被拒绝。  
\- 7: 改单成功。  
\- 8: 改单拒绝。  
»» status_desc | string | false | none | 订单状态描述  
»» status_detail | object|null | false | none | 订单状态详情  
»»» title | string | false | none | 状态标题  
»»» message | string | false | none | 状态说明  
»» finish_as | integer | false | none | 订单完成原因。  
\- 0: 未知。  
\- 1: 没有找到报价。  
\- 2: 没有找到匹配。  
\- 3: 触发价格超出。  
\- 4: 订单价值超出限制。  
\- 5: 拒单未知。  
\- 6: 撤单未知。  
\- 7: 用户主动撤销。  
\- 8: 超过订单有效期自动撤单。  
\- 9: 当前交易时段暂不支持交易。  
\- 13: 公司行动撤单。  
»» side | integer | false | none | 买卖方向（1=卖，2=买）  
»» time_in_force | string | false | none | 订单有效方式。  
\- day: 当日有效。  
»» volume | string | false | none | 委托数量  
»» fill_volume | string | false | none | 成交数量  
»» price | string | false | none | 委托价格  
»» avg_fill_price | string|null | false | none | 平均成交价格  
»» commission | string | false | none | 手续费  
»» time_setup | integer(int64) | false | none | 下单时间（Unix 时间戳，秒）  
»» time_done | integer(int64) | false | none | 订单完成时间（Unix 时间戳，秒）  
» timestamp | integer(int64) | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
price_type | market  
price_type | limit  
status | 0  
status | 1  
status | 2  
status | 3  
status | 4  
status | 5  
status | 6  
status | 7  
status | 8  
finish_as | 0  
finish_as | 1  
finish_as | 2  
finish_as | 3  
finish_as | 4  
finish_as | 5  
finish_as | 6  
finish_as | 7  
finish_as | 8  
finish_as | 9  
finish_as | 13  
side | 1  
side | 2  
time_in_force | day  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  SymbolDetail

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» total | integer(int64) | false | none | 总数量  
» total_page | integer | false | none | 总页数  
» list | array | false | none | none  
»» symbol | string | false | none | 交易对代码  
»» exchange | string | false | none | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»» exchange_desc | string | false | none | 交易所描述  
»» quote_currency | string | false | none | 报价币种  
»» quote_currency_precision | integer | false | none | 报价币种精度  
»» fx_rate | string | false | none | 报价币种对美元的汇率  
»» symbol_desc | string | false | none | 交易对描述  
»» category | string | false | none | Symbol 分类。  
\- CS: 股票。  
\- ETF: 交易所基金。  
\- ADRC、ADR: 美股里的外国公司股票凭证。  
\- ETV: 交易所交易产品。  
\- PFD: 优先股。  
\- ETS: 交易所交易证券。  
\- ETN: 交易所票据。  
\- FUND: 基金。  
»» asset_type | string | false | none | 资产类型。  
\- STOCK: 股票。  
\- ETF: 交易所基金。  
»» settlement_currency | string | false | none | 结算币种  
»» max_order_volume | string | false | none | 最大下单数量  
»» step_order_volume | string | false | none | 下单步长  
»» min_order_volume | string | false | none | 最小下单数量  
»» price_precision | integer | false | none | 价格精度  
»» volume_precision | integer | false | none | 数量精度  
»» is_ipo | boolean | false | none | 是否 IPO 交易对  
»» ipo_price | string | false | none | IPO 价格  
»» price_protection | string | false | none | 价格保护范围  
»» sell_price_protection | string | false | none | 卖出价格保护比例  
»» buy_price_protection | string | false | none | 买入价格保护比例  
»» slippage_rate | string | false | none | 滑点  
»» commission_rate | string | false | none | 手续费率  
»» trade_status | string | false | none | 交易状态。  
\- pre_market: 盘前。  
\- open: 盘中。  
\- post_market: 盘后。  
»» trade_mode | integer | false | none | 当前时段交易模式。  
\- 0: 禁止交易。  
\- 1: 仅允许买入。  
\- 2: 仅允许卖出。  
\- 4: 支持买入和卖出。  
\- 5: 交易暂停。  
\- 6: 交易暂停。  
\- 7: 交易暂停。  
\- 8: 交易暂停。  
»» order_fill_timing | integer | false | none | 下单可成交时机（1=立即成交，2=盘前开始后可成交，3=盘中开始后可成交）  
»» symbol_descs | array | false | none | 多语言交易对描述  
»»» lang | string | false | none | 语言  
»»» value | string | false | none | 多语言描述  
»» icon_link | string | false | none | 图标链接  
»» margin_mode | integer | false | none | 融资融券模式。  
\- 0: 不支持融资融券。  
\- 1: 可融资。  
\- 2: 可融券。  
\- 3: 可融资和融券。  
»» long_im | string | false | none | 多头初始保证金率  
»» long_mm | string | false | none | 多头维持保证金率  
»» short_im | string | false | none | 空头初始保证金率  
»» short_mm | string | false | none | 空头维持保证金率  
»» long_borrowing_rate | string | false | none | 融资年利率。空字符串表示暂无有效利率。  
»» short_borrowing_rate | string | false | none | 融券年利率。空字符串表示暂无有效利率。  
» timestamp | integer(int64) | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
category | CS  
category | ETF  
category | ADRC  
category | ADR  
category | ETV  
category | PFD  
category | ETS  
category | ETN  
category | FUND  
asset_type | STOCK  
asset_type | ETF  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
order_fill_timing | 1  
order_fill_timing | 2  
order_fill_timing | 3  
margin_mode | 0  
margin_mode | 1  
margin_mode | 2  
margin_mode | 3  
      
    
    {
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotSetMarginFeatureRequest

_设置融资功能开关请求参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
margin_feature | boolean | true | none | 是否开启融资功能。true 表示开启，false 表示关闭。  
      
    
    {
      "margin_feature": true
    }
    
    

##  TradFiSpotClosePositionRequest

_平仓请求参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | 交易对代码  
close_volume | string | false | none | 平仓数量；部分平仓时必填  
close_type | integer | true | none | 平仓类型（1=部分平仓，2=全平）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
close_type | 1  
close_type | 2  
      
    
    {
      "symbol": "AAPL",
      "close_volume": "2",
      "close_type": 1
    }
    
    

##  TradfiSpotUpdateOrder

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» order_id | integer(int64) | false | none | 订单 ID  
timestamp | integer(int64) | false | none | none  
      
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotTransactionRequest

_资金转入转出请求参数。转入表示从现货账户转入到股票账户，转出表示从股票账户转出到现货账户。_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
asset | string | true | none | 资产，仅支持 USDT  
change | string | true | none | 变动数量，必须大于 0  
type | string | true | none | 交易类型。deposit 表示从现货账户转入到股票账户，withdraw 表示从股票账户转出到现货账户。  
ref_id | string | true | none | 业务幂等 ID  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
asset | USDT  
type | deposit  
type | withdraw  
      
    
    {
      "asset": "USDT",
      "change": "100",
      "type": "deposit",
      "ref_id": "transfer-202607070001"
    }
    
    

##  TradfiSpotOrderList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» list | array | false | none | 当前委托单列表  
»» order_id | string | false | none | 订单 ID  
»» symbol | string | false | none | 交易对代码  
»» exchange | string | false | none | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»» quote_currency | string | false | none | 报价币种  
»» fx_rate | string | false | none | 报价币种对美元的汇率  
»» symbol_desc | string | false | none | 交易对描述  
»» trade_status | string | false | none | 交易状态。  
\- pre_market: 盘前。  
\- open: 盘中。  
\- post_market: 盘后。  
»» trade_mode | integer | false | none | 当前时段交易模式。  
\- 0: 禁止交易。  
\- 1: 仅允许买入。  
\- 2: 仅允许卖出。  
\- 4: 支持买入和卖出。  
\- 5: 交易暂停。  
\- 6: 交易暂停。  
\- 7: 交易暂停。  
\- 8: 交易暂停。  
»» price_type | string | false | none | 价格类型（market=市价，limit=限价）  
»» side | integer | false | none | 买卖方向（1=卖，2=买）  
»» status | integer | false | none | 订单状态。  
\- 0: 未知。  
\- 1: 新订单，订单已验证，等待处理。  
\- 2: 部分成交。  
\- 3: 全部成交。  
\- 4: 已撤销。  
\- 5: 下单被拒绝。  
\- 6: 撤单被拒绝。  
\- 7: 改单成功。  
\- 8: 改单拒绝。  
»» volume | string | false | none | 委托数量  
»» fill_volume | string | false | none | 成交数量  
»» price | string | false | none | 委托价格  
»» time_setup | integer(int64) | false | none | 下单时间（Unix 时间戳，秒）  
»» time_update | integer(int64) | false | none | 订单更新时间（Unix 时间戳，秒）  
»» max_order_volume | string | false | none | 最大下单数量  
»» step_order_volume | string | false | none | 下单步长  
»» min_order_volume | string | false | none | 最小下单数量  
»» price_precision | integer | false | none | 价格精度  
»» price_protection | string | false | none | 价格保护范围  
»» sell_price_protection | string | false | none | 卖出价格保护比例  
»» buy_price_protection | string | false | none | 买入价格保护比例  
»» commission_rate | string | false | none | 手续费率  
»» slippage_rate | string | false | none | 滑点  
» timestamp | integer(int64) | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
trade_mode | 0  
trade_mode | 1  
trade_mode | 2  
trade_mode | 4  
trade_mode | 5  
trade_mode | 6  
trade_mode | 7  
trade_mode | 8  
price_type | market  
price_type | limit  
side | 1  
side | 2  
status | 0  
status | 1  
status | 2  
status | 3  
status | 4  
status | 5  
status | 6  
status | 7  
status | 8  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotCreateOrder

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» id | string | false | none | 订单 ID  
timestamp | integer(int64) | false | none | none  
      
    
    {
      "data": {
        "id": "123456"
      },
      "timestamp": 0
    }
    
    

##  ClosePosition

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» order_id | integer(int64) | false | none | 平仓订单 ID  
timestamp | integer(int64) | false | none | none  
      
    
    {
      "data": {
        "order_id": 123456
      },
      "timestamp": 0
    }
    
    

##  TradfiSpotPositionList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» list | array | false | none | 当前仓位列表  
»» symbol | string | false | none | 交易对代码  
»» exchange | string | false | none | 交易所。  
\- us: 美股。  
\- hk: 港股。  
\- kr: 韩股。  
\- jp: 日股。  
»» quote_currency | string | false | none | 报价币种  
»» quote_currency_precision | integer | false | none | 报价币种精度  
»» fx_rate | string | false | none | 报价币种对美元的汇率  
»» trade_status | string | false | none | 交易状态。  
\- pre_market: 盘前。  
\- open: 盘中。  
\- post_market: 盘后。  
»» symbol_desc | string | false | none | 交易对描述  
»» position_pnl | string | false | none | 持仓盈亏  
»» today_pnl | string | false | none | 今日盈亏  
»» pnl_rate | string | false | none | 收益率  
»» today_sell_amount | string | false | none | 今日卖出额  
»» today_buy_amount | string | false | none | 今日买入额  
»» today_sell_volume | string | false | none | 今日卖出量  
»» today_buy_volume | string | false | none | 今日买入量  
»» yesterday_volume | string | false | none | 昨日收盘持仓量  
»» volume | string | false | none | 持仓量  
»» available | string | false | none | 可用持仓量  
»» transfer_out_pending_qty | string | false | none | 股票转出处理中数量  
»» avg_cost_price | string | false | none | 成本价  
»» diluted_cost_price | string | false | none | 摊薄成本价  
»» last_price | string | false | none | 最新价格  
»» extended_last_price | string|null | false | none | 延长时段最新价格  
»» max_order_volume | string | false | none | 最大下单数量  
»» step_order_volume | string | false | none | 下单步长  
»» min_order_volume | string | false | none | 最小下单数量  
»» price_precision | integer | false | none | 价格精度  
»» price_protection | string | false | none | 价格保护范围  
»» sell_price_protection | string | false | none | 卖出价格保护比例  
»» buy_price_protection | string | false | none | 买入价格保护比例  
»» commission_rate | string | false | none | 手续费率  
»» slippage_rate | string | false | none | 滑点  
» timestamp | integer(int64) | false | none | none  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
exchange | us  
exchange | hk  
exchange | kr  
exchange | jp  
trade_status | pre_market  
trade_status | open  
trade_status | post_market  
      
    
    {
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  TradFiSpotOrderUpdateRequest

_修改委托单请求参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
volume | string | true | none | 修改后的委托数量  
price | string | true | none | 修改后的委托价格  
      
    
    {
      "volume": "8",
      "price": "201.23"
    }