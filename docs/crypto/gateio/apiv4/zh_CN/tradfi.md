---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/tradfi
api_type: Trading
updated_at: 2026-05-27 20:18:00.045957
---

# TradFi

TradFi是一个传统金融交易平台，提供基于MT5的外汇和差价合约交易服务。TradFi API提供完整的用户管理、资产查询、订单管理、仓位管理和市场数据查询功能。

  * REST API BaseURL 实盘交易: `https://api.gateio.ws/api/v4/`
  * [帮助中心 ](https://www.gate.com/help/tradfi/functional)
  * [TradFi交易 ](https://www.gate.com/tradfi)
  * 注意使用本业务的接口前，需要确保用户已经开通TradFi业务，开通可以调用 开通TradFi用户接口开通，或者登录app进行开通

##  查询mt5账号信息🔒 需要认证

GET`/tradfi/users/mt5-account`

GET `/tradfi/users/mt5-account`

_查询mt5账号信息_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | Mt5Account  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» code | integer | 业务状态码，非0代表业务异常，请查看message  
» message | string | 返回信息  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» mt5_uid | integer | MT5 用户ID  
»» leverage | integer | 杠杆倍数  
»» stop_out_level | string | 强平保证金比例  
»» status | integer | 账户状态（1=未开通，2=审核中，3=正常）  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/users/mt5-account'
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
    url="/tradfi/users/mt5-account"
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
        "mt5_uid": 0,
        "leverage": 0,
        "stop_out_level": "",
        "status": 1
      },
      "timestamp": 1769426795464
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  查询交易对分类

GET`/tradfi/symbols/categories`

GET `/tradfi/symbols/categories`

_查询交易对分类_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | Categories  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 数据  
»» list | array |   
»»» _None_ | object | 分类信息  
»»»» category_id | integer | 分类ID  
»»»» is_favorite | boolean | 是否是自选分类，一般不需要关注  
»»»» category_name | string | 分类名称  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/tradfi/symbols/categories'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/tradfi/symbols/categories \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "list": [
          {
            "category_id": 1,
            "is_favorite": false,
            "category_name": "金属"
          },
          {
            "category_id": 2,
            "is_favorite": false,
            "category_name": "Stocks"
          },
          {
            "category_id": 4,
            "is_favorite": false,
            "category_name": "指数"
          },
          {
            "category_id": 5,
            "is_favorite": false,
            "category_name": "外汇"
          },
          {
            "category_id": 6,
            "is_favorite": false,
            "category_name": "大宗商品"
          }
        ]
      },
      "timestamp": 1769398039786
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  查询交易对列表

GET`/tradfi/symbols`

GET `/tradfi/symbols`

_查询交易对列表_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | Symbols  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» list | array | 交易品种列表  
»»» _None_ | object | 交易品种信息  
»»»» symbol | string | 交易品种代码  
»»»» symbol_desc | string | 交易品种描述  
»»»» category_id | integer | 分类ID  
»»»» status | string | 交易状态（open=可交易，closed=不可交易）  
»»»» trade_mode | string | 交易模式代码（0=禁用交易, 1=仅允许买入持仓，2=仅允许卖出持仓 ,3=仅允许平仓, 4=完整交易访问）  
»»»» icon_link | string | 品种图标URL  
»»»» close_time | integer(int64) | 收盘时间（Unix时间戳，秒）  
»»»» open_time | integer(int64) | 开盘时间（Unix时间戳，秒）  
»»»» next_open_time | integer(int64) | 下次开盘时间（Unix时间戳，秒，0表示无）  
»»»» settlement_currency | string | 结算币种  
»»»» settlement_currency_symbol | string | 结算币种符号  
»»»» price_precision | integer | 价格精度（小数位数）  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/tradfi/symbols'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/tradfi/symbols \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "list": [
          {
            "symbol": "EURUSD",
            "symbol_desc": "Euro vs United States Dollar",
            "category_id": 6,
            "status": "open",
            "trade_mode": "4",
            "icon_link": "https://gimg.staticimgs.com/image/eurusd_20260123_120701_3982593a8387f849b5eb60a05bbadd3c.png",
            "close_time": 1769464800,
            "open_time": 1769378400,
            "next_open_time": 0,
            "settlement_currency": "USD",
            "settlement_currency_symbol": "$",
            "price_precision": 8
          },
          {
            "symbol": "XAGUSD",
            "symbol_desc": "Silver vs US Dollar / Spot",
            "category_id": 1,
            "status": "open",
            "trade_mode": "4",
            "icon_link": "https://gimg.staticimgs.com/image/xagusd_20260115_162831_6d2429db5ad657da37d139eb33e4a324.png",
            "close_time": 1769464800,
            "open_time": 1769378400,
            "next_open_time": 0,
            "settlement_currency": "USD",
            "settlement_currency_symbol": "$",
            "price_precision": 3
          }
        ]
      },
      "timestamp": 1769426795464
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  查询交易对详情🔒 需要认证

GET`/tradfi/symbols/detail`

GET `/tradfi/symbols/detail`

_查询交易对详情_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 是 | 交易品种代码列表（多个用英文逗号分隔，最多支持查10个）  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | ContractDetail  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» list | array | 合约详情列表  
»»» _None_ | object | 合约详情  
»»»» symbol | string | 交易品种代码  
»»»» symbol_desc | string | 交易品种描述  
»»»» category_name | string | 分类名称  
»»»» contract_volume | string | 合约数量  
»»»» settlement_currency | string | 结算货币  
»»»» max_order_volume | string | 最大订单数量  
»»»» min_order_volume | string | 最小订单数量  
»»»» leverage | string | 杠杆倍数  
»»»» price_precision | integer | 价格精度（小数位数）  
»»»» price_sl_level | string | 止损价格级别  
»»»» swap_cost_type | string | 掉期费类型  
»»»» buy_swap_cost_rate | string | 买入掉期费率  
»»»» sell_swap_cost_rate | string | 卖出掉期费率  
»»»» swap_cost_3day | string | 3天掉期费  
»»»» trade_timezone | string | 交易时区  
»»»» trade_mode | string | 交易模式代码（0=禁用交易, 1=仅允许买入持仓，2=仅允许卖出持仓 ,3=仅允许平仓, 4=完整交易访问）  
»»»» icon_link | string | 品种图标URL  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/symbols/detail'
    query_param = 'symbols=EURUSD,XAGUSD'
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
    url="/tradfi/symbols/detail"
    query_param="symbols=EURUSD,XAGUSD"
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
        "list": [
          {
            "symbol": "PLNJPY",
            "symbol_desc": "掉期费-货币-预0",
            "category_name": "Forex",
            "contract_volume": "100000",
            "settlement_currency": "JPY",
            "max_order_volume": "100",
            "min_order_volume": "10",
            "leverage": "25",
            "price_precision": 4,
            "price_sl_level": "100.00",
            "swap_cost_type": "1",
            "buy_swap_cost_rate": "7.937347",
            "sell_swap_cost_rate": "-172.856426",
            "swap_cost_3day": "3",
            "trade_timezone": "GMT+2",
            "trade_mode": "4",
            "icon_link": ""
          }
        ]
      },
      "timestamp": 1769426795464
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  查询交易对k线

GET`/tradfi/symbols/{symbol}/klines`

GET `/tradfi/symbols/{symbol}/klines`

_查询交易对k线_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | URL | string | 是 | 交易品种代码  
kline_type | 请求参数 | string | 是 | K线类型（时间周期）  
begin_time | 请求参数 | integer(int64) | 否 | 开始时间（Unix 时间戳，秒）  
end_time | 请求参数 | integer(int64) | 否 | 结束时间（Unix 时间戳，秒）  
limit | 请求参数 | integer | 否 | 返回K线数量限制（最大500，超过将报错）  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
kline_type | 1m  
kline_type | 15m  
kline_type | 1h  
kline_type | 4h  
kline_type | 1d  
kline_type | 7d  
kline_type | 30d  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | Klines  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» list | array | K线数据列表  
»»» _None_ | object | 单根K线数据  
»»»» o | string | 开盘价（Open）  
»»»» c | string | 收盘价（Close）  
»»»» h | string | 最高价（High）  
»»»» l | string | 最低价（Low）  
»»»» t | integer(int64) | 时间戳（Unix 秒）  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/tradfi/symbols/EURUSD/klines'
    query_param = 'kline_type=1m'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/tradfi/symbols/EURUSD/klines?kline_type=1m \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 1769398039786,
      "data": {
        "list": [
          {
            "o": "1.17198",
            "c": "1.17213",
            "h": "1.17268",
            "l": "1.1718",
            "t": 1755896400
          },
          {
            "o": "1.17208",
            "c": "1.16092",
            "h": "1.17263",
            "l": "1.16023",
            "t": 1756069200
          }
        ]
      }
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  查询交易对Ticker

GET`/tradfi/symbols/{symbol}/tickers`

GET `/tradfi/symbols/{symbol}/tickers`

_查询交易对Ticker_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | URL | string | 是 | 交易品种代码  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TradFiTicker  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

_TradFiTicker_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» highest_price | string | 最高价  
»» lowest_price | string | 最低价  
»» price_change | string | 价格涨跌幅（百分比，已乘100）  
»» price_change_amount | string | 价格涨跌额  
»» today_open_price | string | 今日开盘价  
»» last_today_close_price | string | 昨日收盘价  
»» last_price | string | 最新成交价  
»» bid_price | string | 买一价（Bid）  
»» ask_price | string | 卖一价（Ask）  
»» favorite | boolean | 是否已收藏  
»» status | string | 交易状态（open=可交易，closed=不可交易）  
»» close_time | integer(int64) | 收盘时间（Unix时间戳，秒）  
»» open_time | integer(int64) | 开盘时间（Unix时间戳，秒）  
»» next_open_time | integer(int64) | 下次开盘时间（0表示无）  
»» trade_mode | string | 交易模式代码  
»» category_name | string | 分类名称  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/tradfi/symbols/EURUSD/tickers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/tradfi/symbols/EURUSD/tickers \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "highest_price": "5093.04",
        "lowest_price": "5003.61",
        "price_change": "1.32",
        "price_change_amount": "66.13",
        "today_open_price": "5008.06",
        "last_today_close_price": "4989.92",
        "last_price": "5074.19",
        "bid_price": "5073.83",
        "ask_price": "5074.06",
        "favorite": false,
        "status": "open",
        "close_time": 1769464800,
        "open_time": 1769378400,
        "next_open_time": 0,
        "trade_mode": "4",
        "category_name": "Metals"
      },
      "timestamp": 1769426795464
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  开通TradFi用户🔒 需要认证

POST`/tradfi/users`

POST `/tradfi/users`

_开通TradFi用户_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 开通成功 | CreateUserResp  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object |   
»» status | integer | 状态(1=未开通，2=审核中，3=已开通 )  
»» leverage | integer | 杠杆  
»» mt5_uid | string | mt5uid  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/users'
    query_param = ''
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/tradfi/users"
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
        "leverage": 1,
        "status": 3,
        "mt5_uid": "1"
      },
      "timestamp": 1769398039786
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  查询资产信息🔒 需要认证

GET`/tradfi/users/assets`

GET `/tradfi/users/assets`

_查询资产信息_

查询资产信息

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | UserAssetResp  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» equity | string | 账户净值  
»» margin_level | string | 保证金水平（百分比）  
»» balance | string | 账户余额  
»» margin | string | 已用保证金  
»» margin_free | string | 可用保证金  
»» unrealized_pnl | string | 未实现盈亏  
»» mt5_uid | string | MT5 用户ID  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/users/assets'
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
    url="/tradfi/users/assets"
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
      "timestamp": 1769426795464,
      "data": {
        "equity": "0.00",
        "margin_level": "0.00",
        "balance": "0.00",
        "margin": "0.00",
        "margin_free": "0.00",
        "unrealized_pnl": "0.00",
        "mt5_uid": "10122"
      }
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  查询资金转入转出流水🔒 需要认证

GET`/tradfi/transactions`

GET `/tradfi/transactions`

_查询资金转入转出流水_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
begin_time | 请求参数 | integer(int64) | 否 | 开始时间（秒级时间戳）  
end_time | 请求参数 | integer(int64) | 否 | 结束时间（秒级时间戳）  
type | 请求参数 | string | 否 | 交易类型（deposit-转入，withdraw-转出，dividend-派息，fill_negative-填平负余额）  
page | 请求参数 | integer | 否 | 页码  
page_size | 请求参数 | integer | 否 | 每页数量，默认10条，最大值50条  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
type | deposit  
type | withdraw  
type | dividend  
type | fill_negative  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | TransactionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» data | object |   
»» total | integer | 总记录数  
»» total_page | integer | 总页数  
»» list | array | 记录列表  
»»» asset | string | 资产类型  
»»» type | string | 交易类型  
»»» type_desc | string | 交易类型描述  
»»» change | string | 变动数量  
»»» balance | string | 当前余额  
»»» time | integer(int64) | 发生时间（秒级时间戳）  
»» timestamp | integer(int64) | 服务器时间戳（毫秒）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | deposit-转入  
type | withdraw-转出  
type | dividend-分红结息  
type | fill_negative-填平负余额  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/transactions'
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
    url="/tradfi/transactions"
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
        "total": 2,
        "total_page": 1,
        "list": [
          {
            "asset": "USDT",
            "type": "dividend",
            "type_desc": "Dividend Adjustment",
            "change": "1",
            "balance": "1",
            "time": 1769329389
          },
          {
            "asset": "USDT",
            "type": "fill_negative",
            "type_desc": "填補損失",
            "change": "0.5",
            "balance": "0.5",
            "time": 1769238545
          }
        ]
      },
      "timestamp": 1769332996590
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  资金转入转出🔒 需要认证

POST`/tradfi/transactions`

POST `/tradfi/transactions`

_资金转入转出_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | TradFiTransactionRequest | 是 |   
» asset | body | string | 是 | 资产类型，例如 USDT,目前只能传入USDT  
» change | body | string | 是 | 变动数量，支持最多两位小数  
» type | body | string | 是 | 交易类型（deposit 转入，withdraw 转出）  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» type | deposit  
» type | withdraw  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | CreateTransaction  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object |   
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/transactions'
    query_param = ''
    body='{"asset":"USDT","change":"10","type":"withdraw"}'
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
    url="/tradfi/transactions"
    query_param=""
    body_param='{"asset":"USDT","change":"10","type":"withdraw"}'
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
      "change": "10",
      "type": "withdraw"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "total": 2,
        "total_page": 1,
        "list": [
          {
            "asset": "USDT",
            "type": "dividend",
            "type_desc": "Dividend Adjustment",
            "change": "1",
            "balance": "1",
            "time": 1769329389
          },
          {
            "asset": "USDT",
            "type": "fill_negative",
            "type_desc": "填補損失",
            "change": "0.5",
            "balance": "0.5",
            "time": 1769238545
          }
        ]
      },
      "timestamp": 1769332996590
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  当前委托单列表🔒 需要认证

GET`/tradfi/orders`

GET `/tradfi/orders`

_当前委托单列表_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | OrderList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» list | array | 订单列表  
»»» _None_ | object | 订单信息  
»»»» order_id | integer | 订单ID  
»»»» symbol | string | 交易对  
»»»» symbol_desc | string | 交易对描述  
»»»» price_type | string | 交易类型（market=市价，trigger=触发价）  
»»»» state | integer | 订单状态码  
»»»» state_desc | string | 订单状态描述  
»»»» finished | integer | 是否完成（0=当前订单列表展示，1=当前列表不展示）  
»»»» side | integer | 买卖方向（1=卖，2=买）  
»»»» volume | string | 委托数量  
»»»» price | string | 触发价格  
»»»» price_tp | string | 止盈价  
»»»» price_sl | string | 止损价  
»»»» time_setup | integer(int64) | 下单时间（Unix时间戳，秒）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
price_type | market  
price_type | trigger  
finished | 0  
finished | 1  
side | 1  
side | 2  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/orders'
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
    url="/tradfi/orders"
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
            "order_id": 2630591,
            "symbol": "USDCHF",
            "symbol_desc": "US Dollar vs Swiss Franc",
            "price_type": "trigger",
            "state": 1,
            "state_desc": "",
            "finished": 0,
            "side": 2,
            "volume": "1.6",
            "price": "5.000000",
            "price_tp": "5.200000",
            "price_sl": "4.800000",
            "time_setup": 1768741530
          },
          {
            "order_id": 2630590,
            "symbol": "USDCHF",
            "symbol_desc": "US Dollar vs Swiss Franc",
            "price_type": "trigger",
            "state": 1,
            "state_desc": "",
            "finished": 0,
            "side": 2,
            "volume": "1.6",
            "price": "5.000000",
            "price_tp": "5.100000",
            "price_sl": "4.900000",
            "time_setup": 1768741526
          }
        ],
        "timestamp": 1769426795464
      }
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  下单🔒 需要认证

POST`/tradfi/orders`

POST `/tradfi/orders`

_下单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | TradFiOrderRequest | 是 |   
» price | body | string | 是 | 下单价格  
» price_type | body | string | 是 | 价格类型（trigger=触发价，market=市价）  
» side | body | integer | 是 | 买卖方向（1=卖，2=买）  
» symbol | body | string | 是 | 交易品种代码  
» volume | body | string | 是 | 下单数量  
» price_tp | body | string | 否 | 止盈价格（Take Profit）,没有可以不传  
» price_sl | body | string | 否 | 止损价格（Stop Loss）,没有可以不传  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» price_type | trigger  
» price_type | market  
» side | 1  
» side | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 下单成功 | CreateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 下单结果  
»» id | string | 队列任务id(非任务id)  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/orders'
    query_param = ''
    body='{"price":"0.9","price_type":"trigger","side":2,"symbol":"EURUSD","volume":"10","price_tp":"1.5","price_sl":"0.8"}'
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
    url="/tradfi/orders"
    query_param=""
    body_param='{"price":"0.9","price_type":"trigger","side":2,"symbol":"EURUSD","volume":"10","price_tp":"1.5","price_sl":"0.8"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "price": "0.9",
      "price_type": "trigger",
      "side": 2,
      "symbol": "EURUSD",
      "volume": "10",
      "price_tp": "1.5",
      "price_sl": "0.8"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "id": "117"
      },
      "timestamp": 1769426795464
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  修改委托单🔒 需要认证

PUT`/tradfi/orders/{order_id}`

PUT `/tradfi/orders/{order_id}`

_修改委托单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | TradFiOrderUpdateRequest | 是 |   
» price | body | string | 是 | 价格  
说明：  
\- 必传  
» price_tp | body | string|null | 否 | 止盈价  
说明：  
\- 不传 或 传 "0"：将清空原有止盈价  
\- 如不希望清空，请传接口返回的原止盈价  
» price_sl | body | string|null | 否 | 止损价  
说明：  
\- 不传 或 传 "0"：将清空原有止损价  
\- 如不希望清空，请传接口返回的原止损价  
order_id | URL | integer | 是 | 订单号  
  
####  详细描述

**» price** : 价格  
说明：  
\- 必传

**» price_tp** : 止盈价  
说明：  
\- 不传 或 传 "0"：将清空原有止盈价  
\- 如不希望清空，请传接口返回的原止盈价

**» price_sl** : 止损价  
说明：  
\- 不传 或 传 "0"：将清空原有止损价  
\- 如不希望清空，请传接口返回的原止损价

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | UpdateOrder  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

_订单修改结果_

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» order_id | integer | 订单ID  
»» symbol | string | 交易对  
»» state | string | 订单状态码  
»» volume | string | 委托数量  
»» price | string | 当前价格  
»» price_tp | string | 当前止盈价  
»» price_sl | string | 当前止损价  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/orders/1223'
    query_param = ''
    body='{"price":"2","price_tp":"1.5","price_sl":"0.8"}'
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
    url="/tradfi/orders/1223"
    query_param=""
    body_param='{"price":"2","price_tp":"1.5","price_sl":"0.8"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "price": "2",
      "price_tp": "1.5",
      "price_sl": "0.8"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "data": {
        "order_id": 2651172,
        "symbol": "AUDUSD",
        "state": "1",
        "volume": "1",
        "price": "2.00000",
        "price_tp": "1.50000",
        "price_sl": "0.80000"
      },
      "timestamp": 1769956396273
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  撤销委托单🔒 需要认证

DELETE`/tradfi/orders/{order_id}`

DELETE `/tradfi/orders/{order_id}`

_撤销委托单_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
order_id | URL | integer | 是 | 订单号  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 删除成功 | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

_成功时返回空对象_

名称 | 类型 | 描述  
---|---|---  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/orders/1223'
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
    url="/tradfi/orders/1223"
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
    
    
    {}
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  历史委托单列表🔒 需要认证

GET`/tradfi/orders/history`

GET `/tradfi/orders/history`

_历史委托单列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
begin_time | 请求参数 | integer(int64) | 否 | 开始时间（Unix 时间戳，秒）最早只能查询一个月前  
end_time | 请求参数 | integer(int64) | 否 | 结束时间（Unix 时间戳，秒）  
symbol | 请求参数 | string | 否 | 交易对  
side | 请求参数 | integer | 否 | 买卖方向（1=卖，2=买）  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
side | 1  
side | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | OrderHistoryList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» list | array | 历史订单列表  
»»» _None_ | object | 订单信息  
»»»» order_id | integer | 订单ID  
»»»» symbol | string | 交易对  
»»»» symbol_desc | string | 交易对描述  
»»»» price_type | string | 交易类型（market=市价，trigger=触发价）  
»»»» order_opt_type | integer | 订单操作类型（1=卖，2=买，3=平多，4=平空，5=强制平多，6=强制平空）  
»»»» state | integer | 订单状态码  
»»»» state_desc | string | 订单状态描述  
»»»» side | integer | 买卖方向（1=卖，2=买）  
»»»» volume | string | 委托数量  
»»»» fill_volume | string | 成交数量  
»»»» close_pnl | string | 平仓盈亏  
»»»» price | string | 成交均价  
»»»» trigger_price | string | 触发价  
»»»» price_tp | string | 止盈价  
»»»» price_sl | string | 止损价  
»»»» time_setup | integer(int64) | 下单时间（Unix时间戳，秒）  
»»»» time_done | integer(int64) | 结束时间（Unix时间戳，秒）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
price_type | market  
price_type | trigger  
order_opt_type | 1  
order_opt_type | 2  
order_opt_type | 3  
order_opt_type | 4  
order_opt_type | 5  
order_opt_type | 6  
side | 1  
side | 2  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/orders/history'
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
    url="/tradfi/orders/history"
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
            "order_id": 2648991,
            "symbol": "USDCAD",
            "symbol_desc": "USD VS CAD;",
            "price_type": "market",
            "order_opt_type": 4,
            "state": 4,
            "state_desc": "Filled",
            "side": 2,
            "volume": "0.05",
            "fill_volume": "0.05",
            "close_pnl": "-1.49755",
            "price": "1.3689",
            "trigger_price": "1.3689",
            "price_tp": "0",
            "price_sl": "0",
            "time_setup": 1769397512,
            "time_done": 1769397512
          }
        ]
      }
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  当前仓位列表🔒 需要认证

GET`/tradfi/positions`

GET `/tradfi/positions`

_当前仓位列表_

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | PositionList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» list | array | 仓位信息  
»»» _None_ | object | 仓位信息  
»»»» position_id | integer | 仓位ID  
»»»» symbol | string | 交易市场代码  
»»»» symbol_desc | string | 市场描述  
»»»» margin | string | 占用保证金  
»»»» unrealized_pnl | string | 未实现盈亏  
»»»» unrealized_pnl_rate | string | 未实现收益率  
»»»» volume | string | 持仓数量  
»»»» price_open | string | 开仓均价  
»»»» position_dir | string | 仓位方向(Long=做多，Short=做空)，  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/positions'
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
    url="/tradfi/positions"
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
            "position_id": 2648925,
            "margin": "2.354440320000000142",
            "symbol": "EURUSD",
            "symbol_desc": "Euro vs United States Dollar",
            "unrealized_pnl": "8.06969999999992903440215741284191608428955078125",
            "unrealized_pnl_rate": "0.0068548775107622",
            "volume": "0.01",
            "price_open": "1.177220",
            "position_dir": "Long",
            "price_tp": "0.000000",
            "price_sl": "0.000000",
            "counterparty_price": "1.1851598599999999539278405791264958679676055908203125",
            "time_create": 1769319320
          }
        ],
        "timestamp": 1769426795464
      }
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  修改仓位🔒 需要认证

PUT`/tradfi/positions/{position_id}`

PUT `/tradfi/positions/{position_id}`

_修改仓位_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
position_id | URL | integer | 是 | 仓位id  
body | body | TradFiPositionUpdateRequest | 是 |   
» price_tp | body | string|null | 否 | 止盈价格  
  
说明：  
\- 不传 或 传 "0"：将清空原有止盈价  
\- 如不希望清空，请传接口返回的原止盈价  
» price_sl | body | string|null | 否 | 止损价格  
  
说明：  
\- 不传 或 传 "0"：将清空原有止损价  
\- 如不希望清空，请传接口返回的原止损价  
  
####  详细描述

**» price_tp** : 止盈价格  
  
说明：  
\- 不传 或 传 "0"：将清空原有止盈价  
\- 如不希望清空，请传接口返回的原止盈价

**» price_sl** : 止损价格  
  
说明：  
\- 不传 或 传 "0"：将清空原有止损价  
\- 如不希望清空，请传接口返回的原止损价

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | UpdatePosition  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object |   
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/positions/1223'
    query_param = ''
    body='{"price_tp":"1","price_sl":"1"}'
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
    url="/tradfi/positions/1223"
    query_param=""
    body_param='{"price_tp":"1","price_sl":"1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "price_tp": "1",
      "price_sl": "1"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 0,
      "data": {}
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  平仓🔒 需要认证

POST`/tradfi/positions/{position_id}/close`

POST `/tradfi/positions/{position_id}/close`

_平仓_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
position_id | URL | integer | 是 | 仓位id  
body | body | TradFiClosePositionRequest | 是 |   
» close_type | body | integer | 是 | 平仓类型  
  
说明：  
\- 1：部分平仓（必须传 close_volume）  
\- 2：全平（无需传 close_volume）  
» close_volume | body | string|null | 否 | 平仓数量  
  
说明：  
\- 当 close_type = 1 时必传  
\- 当 close_type = 2 时忽略该字段  
  
####  详细描述

**» close_type** : 平仓类型  
  
说明：  
\- 1：部分平仓（必须传 close_volume）  
\- 2：全平（无需传 close_volume）

**» close_volume** : 平仓数量  
  
说明：  
\- 当 close_type = 1 时必传  
\- 当 close_type = 2 时忽略该字段

####  枚举值列表

枚举值列表参数 | 值  
---|---  
» close_type | 1  
» close_type | 2  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | DeletePosition  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object |   
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/positions/1223/close'
    query_param = ''
    body='{"close_type":1,"close_volume":"1"}'
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
    url="/tradfi/positions/1223/close"
    query_param=""
    body_param='{"close_type":1,"close_volume":"1"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "close_type": 1,
      "close_volume": "1"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "timestamp": 0,
      "data": {}
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

##  历史仓位列表🔒 需要认证

GET`/tradfi/positions/history`

GET `/tradfi/positions/history`

_历史仓位列表_

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
page | 请求参数 | integer(int64) | 否 | 页码，不传默认第1页  
page_size | 请求参数 | integer(int64) | 否 | 分页大小，不传默认值10，最大值不能超过100  
begin_time | 请求参数 | integer(int64) | 否 | 开始时间（时间戳，秒）开始时间（Unix 时间戳，秒）最早只能查询一个月前  
end_time | 请求参数 | integer(int64) | 否 | 结束时间（时间戳，秒）  
symbol | 请求参数 | string | 否 | 交易对（例如：EURUSD）  
position_dir | 请求参数 | string | 否 | 多空方向（Long=多头，Short=空头）  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
position_dir | Long  
position_dir | Short  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 请求成功 | PositionHistoryList  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求失败 | TradFiError  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» timestamp | integer(int64) | 服务器时间戳（毫秒）  
» data | object | 返回数据  
»» total | integer | 总数  
»» total_page | integer | 总页数  
»» list | array | 历史仓位列表  
»»» _None_ | object | 仓位平仓记录  
»»»» position_id | integer(int64) | 仓位ID  
»»»» symbol | string | 市场 / 交易对  
»»»» realized_pnl | string | 已实现盈亏  
»»»» realized_pnl_rate | string | 已实现收益率  
»»»» volume | string | 持仓量 / 最大持仓量  
»»»» volume_closed | string | 平仓数量  
»»»» price_open | string | 开仓均价  
»»»» position_dir | string | 仓位方向  
\- Long：多头  
\- Short：空头  
»»»» price_tp | string | 止盈价格  
»»»» price_sl | string | 止损价格  
»»»» counterparty_price | string | 对手价格  
»»»» close_price | string | 平仓价格  
»»»» time_create | string | 开仓时间（时间戳，秒）  
»»»» time_close | string | 平仓时间（时间戳，秒）  
»»»» position_status | string | 仓位状态  
\- 1：全部平仓  
\- 2：强制平仓  
»»»» close_detail | object|null | 强平详情（普通平仓时为 null）  
»»»»» margin_level | string | 保证金比例（已乘以100）  
»»»»» margin | string | 保证金  
»»»»» equity | string | 净值  
»»»»» stop_out_level | string | 强平比例（已乘以100）  
»»»» realized_pnl_detail | object | 已实现盈亏明细  
»»»»» closed_pnl | string | 平仓盈亏  
»»»»» swap | string | 掉期费  
»»»»» fee | string | 手续费  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
position_dir | Long  
position_dir | Short  
  
状态码 **400**

_TradFiError_

名称 | 类型 | 描述  
---|---|---  
» label | string | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
» message | string | 返回信息，请求错误时会返回  
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
    
    url = '/tradfi/positions/history'
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
    url="/tradfi/positions/history"
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
            "position_id": 2648854,
            "symbol": "EURUSD",
            "realized_pnl": "-2.4",
            "realized_pnl_rate": "-0.0339783598282142",
            "volume": "0.3",
            "volume_closed": "0.3",
            "price_open": "1.17722016",
            "position_dir": "Long",
            "price_tp": "0",
            "price_sl": "0",
            "counterparty_price": "",
            "close_price": "1.1772198600000001",
            "time_close": "1769223573",
            "time_create": "1769223566",
            "position_status": "1",
            "realized_pnl_detail": {
              "closed_pnl": "0",
              "swap": "0",
              "fee": "-2.4"
            },
            "close_detail": null
          },
          {
            "position_id": 2648850,
            "symbol": "EURUSD",
            "realized_pnl": "-1.6",
            "realized_pnl_rate": "-0.0339783598282142",
            "volume": "0.2",
            "volume_closed": "0.2",
            "price_open": "1.17722016",
            "position_dir": "Long",
            "price_tp": "0",
            "price_sl": "0",
            "counterparty_price": "",
            "close_price": "1.1772198600000001",
            "time_close": "1769223391",
            "time_create": "1769223287",
            "position_status": "1",
            "realized_pnl_detail": {
              "closed_pnl": "0",
              "swap": "0",
              "fee": "-1.6"
            },
            "close_detail": null
          }
        ]
      }
    }
    

> 400 返回
    
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "data": null,
      "timestamp": 1769835481814
    }
    

#  模型

##  TradFiTicker

_TradFiTicker_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
label | string | false | none | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
message | string | false | none | 返回信息，请求错误时会返回  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» highest_price | string | false | none | 最高价  
» lowest_price | string | false | none | 最低价  
» price_change | string | false | none | 价格涨跌幅（百分比，已乘100）  
» price_change_amount | string | false | none | 价格涨跌额  
» today_open_price | string | false | none | 今日开盘价  
» last_today_close_price | string | false | none | 昨日收盘价  
» last_price | string | false | none | 最新成交价  
» bid_price | string | false | none | 买一价（Bid）  
» ask_price | string | false | none | 卖一价（Ask）  
» favorite | boolean | false | none | 是否已收藏  
» status | string | false | none | 交易状态（open=可交易，closed=不可交易）  
» close_time | integer(int64) | false | none | 收盘时间（Unix时间戳，秒）  
» open_time | integer(int64) | false | none | 开盘时间（Unix时间戳，秒）  
» next_open_time | integer(int64) | false | none | 下次开盘时间（0表示无）  
» trade_mode | string | false | none | 交易模式代码  
» category_name | string | false | none | 分类名称  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "timestamp": 0,
      "data": {
        "highest_price": "5093.04",
        "lowest_price": "5003.61",
        "price_change": "1.32",
        "price_change_amount": "66.13",
        "today_open_price": "5008.06",
        "last_today_close_price": "4989.92",
        "last_price": "5074.19",
        "bid_price": "5073.83",
        "ask_price": "5074.06",
        "favorite": false,
        "status": "open",
        "close_time": 1769464800,
        "open_time": 1769378400,
        "next_open_time": 0,
        "trade_mode": "4",
        "category_name": "Metals"
      }
    }
    
    

##  Symbols

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» list | array | false | none | 交易品种列表  
»» _None_ | object | false | none | 交易品种信息  
»»» symbol | string | false | none | 交易品种代码  
»»» symbol_desc | string | false | none | 交易品种描述  
»»» category_id | integer | false | none | 分类ID  
»»» status | string | false | none | 交易状态（open=可交易，closed=不可交易）  
»»» trade_mode | string | false | none | 交易模式代码（0=禁用交易, 1=仅允许买入持仓，2=仅允许卖出持仓 ,3=仅允许平仓, 4=完整交易访问）  
»»» icon_link | string | false | none | 品种图标URL  
»»» close_time | integer(int64) | false | none | 收盘时间（Unix时间戳，秒）  
»»» open_time | integer(int64) | false | none | 开盘时间（Unix时间戳，秒）  
»»» next_open_time | integer(int64) | false | none | 下次开盘时间（Unix时间戳，秒，0表示无）  
»»» settlement_currency | string | false | none | 结算币种  
»»» settlement_currency_symbol | string | false | none | 结算币种符号  
»»» price_precision | integer | false | none | 价格精度（小数位数）  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  PositionList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
label | string | false | none | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
message | string | false | none | 返回信息，请求错误时会返回  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» list | array | false | none | 仓位信息  
»» _None_ | object | false | none | 仓位信息  
»»» position_id | integer | false | none | 仓位ID  
»»» symbol | string | false | none | 交易市场代码  
»»» symbol_desc | string | false | none | 市场描述  
»»» margin | string | false | none | 占用保证金  
»»» unrealized_pnl | string | false | none | 未实现盈亏  
»»» unrealized_pnl_rate | string | false | none | 未实现收益率  
»»» volume | string | false | none | 持仓数量  
»»» price_open | string | false | none | 开仓均价  
»»» position_dir | string | false | none | 仓位方向(Long=做多，Short=做空)，  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  TradFiOrderRequest

_下单请求参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
price | string | true | none | 下单价格  
price_type | string | true | none | 价格类型（trigger=触发价，market=市价）  
side | integer | true | none | 买卖方向（1=卖，2=买）  
symbol | string | true | none | 交易品种代码  
volume | string | true | none | 下单数量  
price_tp | string | false | none | 止盈价格（Take Profit）,没有可以不传  
price_sl | string | false | none | 止损价格（Stop Loss）,没有可以不传  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
price_type | trigger  
price_type | market  
side | 1  
side | 2  
      
    
    {
      "price": "0.9",
      "price_type": "trigger",
      "side": 2,
      "symbol": "EURUSD",
      "volume": "10",
      "price_tp": "1.5",
      "price_sl": "0.8"
    }
    
    

##  TransactionList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
data | object | false | none | none  
» total | integer | false | none | 总记录数  
» total_page | integer | false | none | 总页数  
» list | array | false | none | 记录列表  
»» asset | string | false | none | 资产类型  
»» type | string | false | none | 交易类型  
»» type_desc | string | false | none | 交易类型描述  
»» change | string | false | none | 变动数量  
»» balance | string | false | none | 当前余额  
»» time | integer(int64) | false | none | 发生时间（秒级时间戳）  
» timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | deposit-转入  
type | withdraw-转出  
type | dividend-分红结息  
type | fill_negative-填平负余额  
      
    
    {
      "data": {
        "total": 2,
        "total_page": 1,
        "list": [
          {}
        ]
      },
      "timestamp": 1769332996590
    }
    
    

##  CreateTransaction

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | none  
      
    
    {
      "timestamp": 0,
      "data": {}
    }
    
    

##  UpdatePosition

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | none  
      
    
    {
      "timestamp": 0,
      "data": {}
    }
    
    

##  TradFiError

_TradFiError_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
label | string | false | none | 业务状态码，非空代表请求异常，请查看文档关于TradFi错误枚举  
message | string | false | none | 返回信息，请求错误时会返回  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
      
    
    {
      "label": "INVALID_ARGUMENT",
      "message": "无效参数",
      "timestamp": 0
    }
    
    

##  OrderHistoryList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» list | array | false | none | 历史订单列表  
»» _None_ | object | false | none | 订单信息  
»»» order_id | integer | false | none | 订单ID  
»»» symbol | string | false | none | 交易对  
»»» symbol_desc | string | false | none | 交易对描述  
»»» price_type | string | false | none | 交易类型（market=市价，trigger=触发价）  
»»» order_opt_type | integer | false | none | 订单操作类型（1=卖，2=买，3=平多，4=平空，5=强制平多，6=强制平空）  
»»» state | integer | false | none | 订单状态码  
»»» state_desc | string | false | none | 订单状态描述  
»»» side | integer | false | none | 买卖方向（1=卖，2=买）  
»»» volume | string | false | none | 委托数量  
»»» fill_volume | string | false | none | 成交数量  
»»» close_pnl | string | false | none | 平仓盈亏  
»»» price | string | false | none | 成交均价  
»»» trigger_price | string | false | none | 触发价  
»»» price_tp | string | false | none | 止盈价  
»»» price_sl | string | false | none | 止损价  
»»» time_setup | integer(int64) | false | none | 下单时间（Unix时间戳，秒）  
»»» time_done | integer(int64) | false | none | 结束时间（Unix时间戳，秒）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
price_type | market  
price_type | trigger  
order_opt_type | 1  
order_opt_type | 2  
order_opt_type | 3  
order_opt_type | 4  
order_opt_type | 5  
order_opt_type | 6  
side | 1  
side | 2  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  OrderList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» list | array | false | none | 订单列表  
»» _None_ | object | false | none | 订单信息  
»»» order_id | integer | false | none | 订单ID  
»»» symbol | string | false | none | 交易对  
»»» symbol_desc | string | false | none | 交易对描述  
»»» price_type | string | false | none | 交易类型（market=市价，trigger=触发价）  
»»» state | integer | false | none | 订单状态码  
»»» state_desc | string | false | none | 订单状态描述  
»»» finished | integer | false | none | 是否完成（0=当前订单列表展示，1=当前列表不展示）  
»»» side | integer | false | none | 买卖方向（1=卖，2=买）  
»»» volume | string | false | none | 委托数量  
»»» price | string | false | none | 触发价格  
»»» price_tp | string | false | none | 止盈价  
»»» price_sl | string | false | none | 止损价  
»»» time_setup | integer(int64) | false | none | 下单时间（Unix时间戳，秒）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
price_type | market  
price_type | trigger  
finished | 0  
finished | 1  
side | 1  
side | 2  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  TradFiOrderUpdateRequest

_修改订单价格及止盈止损参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
price | string | true | none | 价格  
说明：  
\- 必传  
price_tp | string|null | false | none | 止盈价  
说明：  
\- 不传 或 传 "0"：将清空原有止盈价  
\- 如不希望清空，请传接口返回的原止盈价  
price_sl | string|null | false | none | 止损价  
说明：  
\- 不传 或 传 "0"：将清空原有止损价  
\- 如不希望清空，请传接口返回的原止损价  
      
    
    {
      "price": "2",
      "price_tp": "1.5",
      "price_sl": "0.8"
    }
    
    

##  ContractDetail

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» list | array | false | none | 合约详情列表  
»» _None_ | object | false | none | 合约详情  
»»» symbol | string | false | none | 交易品种代码  
»»» symbol_desc | string | false | none | 交易品种描述  
»»» category_name | string | false | none | 分类名称  
»»» contract_volume | string | false | none | 合约数量  
»»» settlement_currency | string | false | none | 结算货币  
»»» max_order_volume | string | false | none | 最大订单数量  
»»» min_order_volume | string | false | none | 最小订单数量  
»»» leverage | string | false | none | 杠杆倍数  
»»» price_precision | integer | false | none | 价格精度（小数位数）  
»»» price_sl_level | string | false | none | 止损价格级别  
»»» swap_cost_type | string | false | none | 掉期费类型  
»»» buy_swap_cost_rate | string | false | none | 买入掉期费率  
»»» sell_swap_cost_rate | string | false | none | 卖出掉期费率  
»»» swap_cost_3day | string | false | none | 3天掉期费  
»»» trade_timezone | string | false | none | 交易时区  
»»» trade_mode | string | false | none | 交易模式代码（0=禁用交易, 1=仅允许买入持仓，2=仅允许卖出持仓 ,3=仅允许平仓, 4=完整交易访问）  
»»» icon_link | string | false | none | 品种图标URL  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  CreateOrder

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 下单结果  
» id | string | false | none | 队列任务id(非任务id)  
      
    
    {
      "timestamp": 0,
      "data": {
        "id": "117"
      }
    }
    
    

##  Mt5Account

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | false | none | 业务状态码，非0代表业务异常，请查看message  
message | string | false | none | 返回信息  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» mt5_uid | integer | false | none | MT5 用户ID  
» leverage | integer | false | none | 杠杆倍数  
» stop_out_level | string | false | none | 强平保证金比例  
» status | integer | false | none | 账户状态（1=未开通，2=审核中，3=正常）  
      
    
    {
      "code": 0,
      "message": "ok",
      "timestamp": 0,
      "data": {
        "mt5_uid": 0,
        "leverage": 100,
        "stop_out_level": "50%",
        "status": 1
      }
    }
    
    

##  CreateUserResp

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | none  
» status | integer | false | none | 状态(1=未开通，2=审核中，3=已开通 )  
» leverage | integer | false | none | 杠杆  
» mt5_uid | string | false | none | mt5uid  
      
    
    {
      "timestamp": 0,
      "data": {
        "status": 0,
        "leverage": 0,
        "mt5_uid": "string"
      }
    }
    
    

##  TradFiClosePositionRequest

_平仓请求参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
close_type | integer | true | none | 平仓类型  
  
说明：  
\- 1：部分平仓（必须传 close_volume）  
\- 2：全平（无需传 close_volume）  
close_volume | string|null | false | none | 平仓数量  
  
说明：  
\- 当 close_type = 1 时必传  
\- 当 close_type = 2 时忽略该字段  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
close_type | 1  
close_type | 2  
      
    
    {
      "close_type": 1,
      "close_volume": "1"
    }
    
    

##  DeletePosition

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | none  
      
    
    {
      "timestamp": 0,
      "data": {}
    }
    
    

##  TradFiPositionUpdateRequest

_修改仓位止盈止损参数_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
price_tp | string|null | false | none | 止盈价格  
  
说明：  
\- 不传 或 传 "0"：将清空原有止盈价  
\- 如不希望清空，请传接口返回的原止盈价  
price_sl | string|null | false | none | 止损价格  
  
说明：  
\- 不传 或 传 "0"：将清空原有止损价  
\- 如不希望清空，请传接口返回的原止损价  
      
    
    {
      "price_tp": "1",
      "price_sl": "1"
    }
    
    

##  PositionHistoryList

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» total | integer | false | none | 总数  
» total_page | integer | false | none | 总页数  
» list | array | false | none | 历史仓位列表  
»» _None_ | object | false | none | 仓位平仓记录  
»»» position_id | integer(int64) | true | none | 仓位ID  
»»» symbol | string | true | none | 市场 / 交易对  
»»» realized_pnl | string | true | none | 已实现盈亏  
»»» realized_pnl_rate | string | false | none | 已实现收益率  
»»» volume | string | true | none | 持仓量 / 最大持仓量  
»»» volume_closed | string | true | none | 平仓数量  
»»» price_open | string | true | none | 开仓均价  
»»» position_dir | string | true | none | 仓位方向  
\- Long：多头  
\- Short：空头  
»»» price_tp | string | false | none | 止盈价格  
»»» price_sl | string | false | none | 止损价格  
»»» counterparty_price | string | false | none | 对手价格  
»»» close_price | string | true | none | 平仓价格  
»»» time_create | string | true | none | 开仓时间（时间戳，秒）  
»»» time_close | string | true | none | 平仓时间（时间戳，秒）  
»»» position_status | string | true | none | 仓位状态  
\- 1：全部平仓  
\- 2：强制平仓  
»»» close_detail | object|null | false | none | 强平详情（普通平仓时为 null）  
»»»» margin_level | string | false | none | 保证金比例（已乘以100）  
»»»» margin | string | false | none | 保证金  
»»»» equity | string | false | none | 净值  
»»»» stop_out_level | string | false | none | 强平比例（已乘以100）  
»»» realized_pnl_detail | object | true | none | 已实现盈亏明细  
»»»» closed_pnl | string | false | none | 平仓盈亏  
»»»» swap | string | false | none | 掉期费  
»»»» fee | string | false | none | 手续费  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
position_dir | Long  
position_dir | Short  
      
    
    {
      "timestamp": 0,
      "data": {
        "total": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      }
    }
    
    

##  Categories

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 数据  
» list | array | false | none | none  
»» _None_ | object | false | none | 分类信息  
»»» category_id | integer | false | none | 分类ID  
»»» is_favorite | boolean | false | none | 是否是自选分类，一般不需要关注  
»»» category_name | string | false | none | 分类名称  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  UpdateOrder

_订单修改结果_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» order_id | integer | false | none | 订单ID  
» symbol | string | false | none | 交易对  
» state | string | false | none | 订单状态码  
» volume | string | false | none | 委托数量  
» price | string | false | none | 当前价格  
» price_tp | string | false | none | 当前止盈价  
» price_sl | string | false | none | 当前止损价  
      
    
    {
      "timestamp": 0,
      "data": {
        "order_id": 2630591,
        "symbol": "USDCHF",
        "state": 1,
        "volume": "1.6",
        "price": "5.000000",
        "price_tp": "5.200000",
        "price_sl": "4.800000"
      }
    }
    
    

##  UserAssetResp

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» equity | string | false | none | 账户净值  
» margin_level | string | false | none | 保证金水平（百分比）  
» balance | string | false | none | 账户余额  
» margin | string | false | none | 已用保证金  
» margin_free | string | false | none | 可用保证金  
» unrealized_pnl | string | false | none | 未实现盈亏  
» mt5_uid | string | false | none | MT5 用户ID  
      
    
    {
      "timestamp": 0,
      "data": {
        "equity": "0.00",
        "margin_level": "0.00",
        "balance": "0.00",
        "margin": "0.00",
        "margin_free": "0.00",
        "unrealized_pnl": "0.00",
        "mt5_uid": "10122"
      }
    }
    
    

##  Klines

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
timestamp | integer(int64) | false | none | 服务器时间戳（毫秒）  
data | object | false | none | 返回数据  
» list | array | false | none | K线数据列表  
»» _None_ | object | false | none | 单根K线数据  
»»» o | string | false | none | 开盘价（Open）  
»»» c | string | false | none | 收盘价（Close）  
»»» h | string | false | none | 最高价（High）  
»»» l | string | false | none | 最低价（Low）  
»»» t | integer(int64) | false | none | 时间戳（Unix 秒）  
      
    
    {
      "timestamp": 0,
      "data": {
        "list": [
          {}
        ]
      }
    }
    
    

##  TradFiTransactionRequest

_资金转入转出请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
asset | string | true | none | 资产类型，例如 USDT,目前只能传入USDT  
change | string | true | none | 变动数量，支持最多两位小数  
type | string | true | none | 交易类型（deposit 转入，withdraw 转出）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
type | deposit  
type | withdraw  
      
    
    {
      "asset": "USDT",
      "change": "10",
      "type": "withdraw"
    }