---
exchange: gateio
source_url: https://www.gate.com/docs/developers/crossex/zh_CN
api_type: Trading
updated_at: 2026-11-13 20:58:27.530220
---

# Gate CrossEx API v1.0.8

* Python 
  * Shell 

v1.0.8 · Stable


API 全面支持跨所账户核心能力，覆盖资金划转、查询、交易、账户信息更改、订阅及推送等全流程操作。

下方有示例代码，请求和返回示例。 点击上方的语言 tab 来切换各语言的代码示例。

##  访问地址

**REST API BaseURL:**

  * 实盘交易: `https://api.gateio.ws/api/v4`

##  SDK

可用的 SDK:

[PyPython](https://github.com/gate/gateapi-python)[JavaJava](https://github.com/gate/gateapi-java)[PHPPHP](https://github.com/gate/gateapi-php)[GoGo](https://github.com/gate/gateapi-go)[C#C#](https://github.com/gate/gateapi-csharp)[NodeNodeJS](https://github.com/gate/gateapi-nodejs)[JSJavascript](https://github.com/gate/gateapi-js)

  * [Python ](https://github.com/gate/gateapi-python)
  * [Java ](https://github.com/gate/gateapi-java)
  * [PHP ](https://github.com/gate/gateapi-php)
  * [Go ](https://github.com/gate/gateapi-go)
  * [C# ](https://github.com/gate/gateapi-csharp)
  * [NodeJS ](https://github.com/gate/gateapi-nodejs)
  * [Javascript ](https://github.com/gate/gateapi-js)

除了 API 示例，部分 SDK 还提供了额外的演示应用程序。 演示应用程序是一个相对完整的示例，展示了如何使用 SDK。 可以单独构建和运行。详细信息请参考相应的仓库。

  * [Python ](https://github.com/gate/gateapi-python/tree/master/example)
  * [Java ](https://github.com/gate/gateapi-java/tree/master/example)
  * [C# ](https://github.com/gate/gateapi-csharp/tree/master/example)
  * [Go ](https://github.com/gate/gateapi-go/tree/master/_example)

##  关于 CrossEx

CrossEx 是一个跨交易所交易平台，允许用户通过统一账户在多个交易所（Binance、OKX、Gate、Bybit、Kraken、Hyperliquid、Deribit、Lighter、Aster）进行交易。CrossEx API 提供完整的账户管理、资产划转、下单和仓位管理功能，支持跨交易所操作。

  * [帮助中心 ](https://www.gate.com/help/crossex/functional)
  * [跨所交易 ](https://www.gate.com/crossex)

##  技术支持

如果您在使用过程中有任何问题或建议，可以通过以下方式联系我们：

  * 提交工单反馈
  * 在线工单反馈
  * 将您的联系信息和问题发送至 [mm@gate.com](mailto:mm@gate.com)，我们将为您分配 技术专家为您服务。

如果您遇到 API 错误，建议您整理以下内容，以便我们快速为您分析问题：

  1. 问题描述
  2. Gate UID
  3. 请求 URI 和参数
  4. 错误代码
  5. 响应内容

DANGER

即使您提交问题，也不应向客服或他人提交 API key 信息，否则将存在严重的资产风险。如果已经意外泄露，请删除现有 API 并重新创建。

#  更新日志

**v1.0.8**

2026-11-09

  * 明确 `POST /crossex/transfers` 的 `coin` 参数限制。若 `from` 或 `to` 为 `CROSSEX_DERIBIT`，则仅支持 `USDC`。

**v1.0.7**

2026-11-02

  * 新增 `GET /crossex/rule/open_capacity`（`listCrossexRuleOpenCapacity`），响应包含必填字段 `symbol`、`position_side`（`LONG`/`SHORT`）和 `available_to_open_notional`。仅返回剩余可开仓价值低于阈值的交易对及仓位方向；`0` 表示该交易对在对应方向当前不能开仓。

**v1.0.6**

2026-10-12

  * CrossEx 新增美股、港股、韩股和日股的股票及ETF交易能力，交易对格式为 `{市场}_{STOCK或ETF}_{证券代码}_USDT`。
  * 新增 `GET /crossex/security_positions` 证券仓位查询接口，并补充股票及ETF下单限制、价格计价币种和相关字段说明。

**v1.0.5**

2026-09-15

  * CrossEx 新增 `LIGHTER` 交易所支持：合约订单标识使用 `LIGHTER_FUTURE_{Base}_{Counter}`；`POST /crossex/transfers` 支持 `CROSSEX_LIGHTER` 与 `SPOT` 之间的 USDC 划转；`POST /crossex/convert/quote` 支持跨所模式下 `LIGHTER_USDC` 与 `CROSSEX_USDT` 互兑。

**v1.0.4**

2026-08-24

  * `GET /crossex/history_positions` 响应项新增可选字段 `margin_mode`（`CROSS`/`ISOLATED`）
  * `POST /crossex/positions/margin` 响应新增可选字段 `position_side`（`NONE`/`LONG`/`SHORT`）

**v1.0.3**

2026-08-10

  * CrossEx新增Hyperliquid逐仓保证金功能，支持修改、查询保证金模式及增加、减少逐仓保证金
  * CrossEx闪兑支持Hyperliquid USDC币种，同时支持还款负债
  * 完善逐仓保证金和强平价格字段说明，并更新保证金模式及逐仓保证金相关错误码

**v1.0.2**

2026-07-02

  * CrossEx新增支持DERIBIT交易所

2026-06-09

  * CrossEx新增支持HYPERLIQUID交易所

2026-05-19

  * CrossEx新增支持KRAKEN交易所

2026-03-19

  * 支持分所费率，费率查询结构改为数组

**v1.0.1**

2026-03-12

  * CrossEx新增支持BYBIT交易所

**v1.0.0**

2026-01-20

  * CrossEx API 首次发布
  * 提供跨多个交易所的统一账户管理
  * 支持跨交易所资产划转
  * 提供跨交易所下单和管理功能
  * 支持合约和杠杆交易的仓位管理
  * 提供市场数据查询（交易对、风险限额等）
  * 支持账户设置（仓位模式、账户模式、杠杆倍数）

#  概述

API 全面支持跨所账户核心能力，覆盖资金划转、查询、交易、账户信息更改、订阅及推送等全流程操作。

  * [帮助中心 ](https://www.gate.com/help/crossex/functional)
  * [跨所交易 ](https://www.gate.com/crossex)

##  数据中心

Gate 数据中心位于 AWS 日本 ap-northeast-1 区域。

##  API 概览

API 概览API 分类 | 分类链接 | 概述  
---|---|---  
host + `/api/v4/crossex/*` | CrossEx API | 跨交易所交易 API，提供统一账户管理和跨交易所交易功能  
  
##  CrossEx 功能特性

CrossEx 是一个跨交易所交易平台，提供以下功能：

  * 跨多个交易所（Binance、OKX、Gate、Bybit、Kraken、Hyperliquid、Deribit、Lighter、Aster）的统一账户管理
  * 跨交易所资产划转
  * 统一的订单管理和交易
  * 实时仓位和资产监控
  * 支持跨交易所的现货、合约和杠杆交易

##  使用说明

在使用 CrossEx API 之前，请确保：

  1. 您已开通 CrossEx 账户
  2. 您已获得相应的 API 权限
  3. 您了解 CrossEx 的交易规则和限制
  4. 您已正确配置您的交易所账户

##  API 分类

CrossEx API 主要包括以下功能模块：

  * **账户管理** ：查询和管理统一账户资产
  * **资产划转** ：在交易所和现货账户之间划转资产
  * **订单管理** ：跨交易所下单、查询和管理订单
  * **仓位管理** ：查询和管理合约和杠杆交易的仓位
  * **市场数据** ：查询交易对、风险限额和市场信息
  * **账户设置** ：配置仓位模式、账户模式和杠杆倍数

#  认证

##  生成 API key

在调用私有API接口前，需要生成账户的API key来验证身份。 您可以在网页端登录成功后，在【账户管理】-> 【APIv4 Keys】中生成， 或点击 [这里](/myaccount/apiv4keys) 生成 API keys

每个账户最多可以创建 20 个 API key，每个 Key 的权限配置都是相互独立的。 建议给每个 Key 设置能够标明用途的备注名

**`Key`** 访问密钥  
**`Secret Key`** 签名认证加密所使用的密钥

除此之外，还可以配置 IP 白名单，只允许服务端接收来自 IP 白名单里的客户端请求。每个 Key 最多可配置 20 个 IP 地址，IP 地址按照 IPv4 配置， 不支持 IP 地址段。若不设置 IP 白名单，服务端不会验证客户端 IP 来源。

TIP

注：如果发现 Key 的名字是 `spot` 或者 `futures` ，该 Key 很有可能是迁移之后系统的默认命名， 详情参考 “关于 APIv4 Key 升级” 一节。

创建的 Key 还可以更新和删除，不过需要注意的是 Key 的更新和删除，最多需要 5 分钟才能生效。

另外模拟合约与实盘合约属于两套不同的环境，实盘合约的 API Key 不可用于模拟合约。 如果需要使用模拟合约做 API 接口联调测试，需要在个人账户 APIv4Keys 页面的模拟合约入口单独申请。 模拟合约与实盘合约的接口请求方式完全相同，区别只是在 API 的 Base URL 和使用的 API Key

##  APIv4 权限

创建 Key 的时候，可以为该 Key 配置是否开启现货杠杆、合约、钱包或者提现的权限， 开启的权限可以配置读写或者只读。

APIv4 权限产品 | 权限  
---|---  
`现货/杠杆` | `只读`查询订单 `读写`查询订单&下单  
`永续合约` | `只读`查询订单 `读写`查询订单&下单  
`交割合约` | `只读`查询订单 `读写`查询订单&下单  
`钱包` | `只读`查询充提划转记录 `读写` 查询账户记录&资金划转  
`提现` | `只读`查询提现记录 `读写` 查询提现记录&提现  
  
所有请求方法为 `GET` 的都是读操作，其他的则是写请求。每个权限组可以设置为禁用、只读或读写。

值得注意的一点是，尽管提现操作组只有一个 API （即 `POST /withdrawals` ），考虑到一般使用情况， 还是将其从钱包操作里独立成一个权限组，而包括了提现记录的账户转出流水记录查询（即 `GET /wallet/withdrawals` ）还是保留在钱包 API 权限组了。

##  APIv4 验签请求接口发送要求

  1. 在官网个人中心申请 APIv4 Key ，并确保该 Key 拥有对应操作的读写权限。
  2. 在发送请求头部传入 `KEY` ，即 APIv4 密钥对的 Key
  3. 在发送请求头部传入 `Timestamp` ，即请求发送的时间，格式是秒级精度的 Unix 时间戳。 同时该时间不能与当前时间差距超过 60 秒。
  4. 在发送请求头部传入 `SIGN` ，即将请求生成签名字符串并用 APIv4 Secret 加密后生成的签名。 签名字符串生成方法参看下节，加密算法为 `HexEncode(HMAC_SHA512(secret, signature_string))` ， 即通过 HMAC-SHA512 加密算法，将 APIv4 Secret 作为加密密钥，签名字符串作为加密消息， 生成加密结果的 16 进制输出。
  5. 确保发送请求的客户端 IP 地址在所使用的密钥的 IP 地址白名单里。

##  APIv4 签名字符串生成方式

APIv4 中签名字符串按照如下方式拼接生成：

`Request Method + "\n" + Request URL + "\n" + Query String + "\n" + HexEncode(SHA512(Request Payload)) + "\n" + Timestamp`

###  Request Method

请求方法，全大写, 如 `POST`, `GET`

###  Request URL

请求 URL，不包括服务地址和端口，如 `/api/v4/futures/orders`

###  Query String

_没有_ 使用 URL 编码的请求参数，请求参数在参与计算签名时的顺序一定要保证和实际请求里的顺序一致。 如 `status=finished&limit=50` 。

如果没有请求参数，使用空字符串 ("")

###  HexEncode(SHA512(Request Payload))

将请求体字符串使用 SHA512 哈希之后的结果。如果没有请求体，使用空字符串的哈希结果，即 `cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e`

###  Timestamp

设置在请求头部 `Timestamp` 里的值

示例

注：示例中所有的换行都是为了方便显示人为添加的，实际只有示例中的一个 `\n` 保留

假设使用的 Key 为 `key` ，Secret 为 `secret`

  1. 查询所有合约订单

    
    
    	GET /api/v4/futures/orders?contract=BTC_USD&status=finished&limit=50 HTTP/1.1
    

签名字符串:
    
    
    	GET\n
    	/api/v4/futures/orders\n
    	contract=BTC_USD&status=finished&limit=50\n
    	cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e\n
    	1541993715
    

说明

  * `/api/v4/futures/orders`: 请求 URL
  * `contract=BTC_USD&status=finished&limit=50`: 请求参数，与实际请求的顺序完全一致
  * 请求体为空，使用空字符串的哈希输出
  * `1541993715`: Unix 时间戳

签名结果

`55f84ea195d6fe57ce62464daaa7c3c02fa9d1dde954e4c898289c9a2407a3d6fb3faf24deff16790d726b66ac9f74526668b13bd01029199cc4fcc522418b8a`

  2. 创建合约委托

    
    
    	POST /api/v4/futures/orders HTTP/1.1
    
    	{"contract":"BTC_USD","type":"limit","size":100,"price":6800,"time_in_force":"gtc"}
    

签名字符串:
    
    
    	POST\n
    	/api/v4/futures/orders\n
    	\n
    	ad3c169203dc3026558f01b4df307641fa1fa361f086b2306658886d5708767b1854797c68d9e62fef2f991645aa82673622ebf417e091d0bd22bafe5d956cca\n
    	1541993715
    

说明

  * 请求参数为空，使用空字符串
  * 使用 JSON 序列化之后的字符串的哈希输出

签名结果

`eae42da914a590ddf727473aff25fc87d50b64783941061f47a3fdb92742541fc4c2c14017581b4199a1418d54471c269c03a38d788d802e2c306c37636389f0`
    
    
    # coding: utf-8
    
    # Python 示例验签代码
    
    """
    本示例仅作为演示签名计算方式使用，推荐使用各语言的 SDK ，因为已经集成了验签规则
    """
    
    # coding: utf-8
    import time
    import hashlib
    import hmac
    import requests
    import json
    
    def gen_sign(method, url, query_string=None, payload_string=None):
        key = ''        # api_key
        secret = ''     # api_secret
    
        t = time.time()
        m = hashlib.sha512()
        m.update((payload_string or "").encode('utf-8'))
        hashed_payload = m.hexdigest()
        s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
        sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}
    
    if __name__ == "__main__":
        host = "https://api.gateio.ws"
        prefix = "/api/v4"
        common_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
        url = '/futures/orders'
        body = {"contract": "BTC_USD", "size": 100, "price": "30", "tif": "gtc"}
        request_content = json.dumps(body)
        sign_headers = gen_sign('POST', prefix + url, "", request_content)
        sign_headers.update(common_headers)
        print('signature headers: %s' % sign_headers)
        res = requests.post(host + prefix + url, headers=sign_headers, data=request_content)
        print(res.status_code)
        print(res.content)
    

##  异常处理

APIv4 对于所有的异常请求，会设置状态码为非 2xx ，同时返回一个 JSON 格式的返回体来描述具体的错误信息

返回体的格式通常如下所示：
    
    
    {
      "label": "COMMON_PARAM_BIND_ERROR",
      "message": "Invalid parameter, please refer to API documentation"
    }
    

  * `label` 用于标识某种错误的类型，格式 `string` ，它的值是一个固定的列表（见下方）程序处理可以使用 `label` 字段的内容来设定和捕获异常
  * `message` (或 `detail`) 表示详细的错误信息，方便 API 对接时，理解具体是因为什么样的参数设置导致请求出现了异常 该字段内容不建议用于异常的捕获或识别

以 Python [requests ](https://requests.readthedocs.io/zh_CN/latest/) 为例，异常的处理流程可以参考如下所示：

> 以下示例的异常捕获流程只涉及到业务相关的异常，网络连接超时等其他非业务相关的异常还需要自行处理
    
    
    import requests
    
    r = requests.get("https://api.gateio.ws/api/v4/crossex/accounts")
    try:
        r.raise_for_status()
    except requests.HTTPError:
        # 捕获非 2xx 错误，尝试解析 body 里返回的错误消息，并根据不同 label 做不同的异常处理
        if r.json()['label'] == 'xxx':
            print(r.json())
    

##  下单异常 `reason`

为缩短接口响应时间，CrossEx 下单采用异步受理模式。请求被受理后，接口仅返回订单号，行为类似现货下单的 `action_mode=ACK`。

> 返回订单号仅表示 CrossEx 已受理请求，不代表订单已经成功提交到交易所或成交。请通过订单查询接口或订单推送获取最终处理结果。

受理订单后，CrossEx 会依次执行以下操作：

  1. 重新校验账户的交易限制、可用资金（或保证金）及风控状态。
  2. 校验通过后，将订单提交到目标交易所。

订单可能在 CrossEx 校验阶段或交易所校验阶段被拒绝。两种情况的订单状态及 `reason` 格式不同。

###  CrossEx 拒单：`state = FAIL`

当订单不符合 CrossEx 的交易规则、资金要求或风控限制时，订单状态为 `FAIL`。

此时，`reason` 是一个 JSON 字符串，包含可供程序识别的 `label` 和便于排查问题的 `message`。客户端可以将 `reason` 再解析为 JSON，并根据 `label` 执行相应处理。
    
    
    {
      "user_id": "123",
      "order_id": "xxx",
      "state": "FAIL",
      "reason": "{\"label\":\"TRADE_INSUFFICIENT_AVAILABLE_MARGIN_ERROR\",\"message\":\"Insufficient availableMargin\"}"
    }
    

###  交易所拒单：`state = REJECT`

订单通过 CrossEx 校验，但被目标交易所拒绝时，订单状态为 `REJECT`。 此时，`reason` 保留交易所返回的原始错误信息，通常是一段文本，不保证符合 JSON 格式，也没有统一的 `label`。 客户端可将其作为可读错误信息展示或记录，不要依赖固定格式进行程序判断。
    
    
    {
      "user_id": "123",
      "order_id": "xxx",
      "state": "REJECT",
      "reason": "Due to the order could not be executed as maker, the Post Only order will be rejected. The order will not be recorded in the order history"
    }
    

以下整理了部分常见的交易所拒单 `reason` 及处理建议，仅供排查问题时参考。 由于不同交易所的错误信息和交易规则可能存在差异，具体含义及处理方式请以对应交易所的官方文档为准。

###  限价委托错误

下表中的 `${xxx}` 等内容表示交易所返回的动态值，实际 `reason` 中会显示具体数值或名称。

限价委托错误`reason` | `tips`  
---|---  
`Due to the order could not be executed ... The order will not be recorded in the order history` | 订单无法按照指定的成交方式执行。POC/Post Only 订单请调整委托价格，避免立即与对手价成交；FOK 订单请增加可成交深度或改用其他 `time_in_force`。  
`EC_PostOnlyWillTakeLiquidity` | Post Only 订单会立即与对手价成交，因此被拒绝。请将买价调低或卖价调高后重试，也可以改用允许立即成交的委托方式。  
`Post only order would have immediately matched, bbo was ...` | Post Only 订单价格已触及当前最优对手价。请参考返回的最优买卖价（BBO）调整价格，确保订单只进入订单簿而不会立即成交。  
`label: ORDER_POC_IMMEDIATE, message: order price ... while counter price ...` | POC 订单价格会立即与对手价成交。买单价格应低于最优卖价，卖单价格应高于最优买价。  
`label: ORDER_FOK, message: order can not be filled` | 当前市场深度不足，FOK 订单无法立即全部成交。请减小委托数量、调整价格，或改用 IOC/GTC。  
`iocWouldNotExecute` | IOC 订单在当前价格下没有可立即成交的数量。请调整委托价格或等待市场出现可成交深度后重试。  
`Order price is not within the price limit (max buy price: ${price}, min sell price: ${price})` | 委托价格超出交易所允许范围。买单不得高于 `max buy price`，卖单不得低于 `min sell price`，请按返回的价格边界调整。  
`Limit price can't be higher than {price}` | 委托价格高于交易所上限。请将价格调整到返回的最高限价以内。  
`The lowest price limit for sell orders is ${price}` | 卖单价格低于交易所下限。请将卖价提高到返回的最低限价或以上。  
`The highest price limit for buy orders is ${price}` | 买单价格高于交易所上限。请将买价降低到返回的最高限价或以下。  
`The counterparty's best price does not meet the PERCENT_PRICE filter limit.` | 当前对手方最优价超出交易所价格保护范围。请等待行情恢复到允许范围，或改用符合价格限制的限价单。  
`label: PRICE_TOO_DEVIATED, message: order price ... while mark price ... and deviation-rate limit ...` | 委托价相对标记价格的偏离幅度超过限制。请根据返回的标记价格和偏离率上限重新计算委托价格。  
`Price too far from oracle asset=${asset}` | 委托价与预言机价格偏离过大。请获取最新行情后调整价格，并确认价格精度和买卖方向正确。  
`label: RISK_LIMIT_EXCEEDED, message: position value (include pending orders) would reach to ... while risk limit is ...` | 当前仓位与未成交订单合计价值将超过风险限额。请减小订单数量、撤销部分挂单或先降低仓位。  
`Order failed. ... the maximum position amount under current leverage ...` | 当前仓位、待成交订单与本次委托的合计数量超过当前杠杆对应的仓位上限。请减小委托数量、撤销同方向挂单、降低仓位或调整杠杆。  
`Order must have minimum value of $10. asset=${asset}` | 订单金额未达到交易所最低要求。请提高委托数量或价格，使订单金额至少达到 10 美元，并同时满足数量精度要求。  
`label: INVALID_PARAM_VALUE, message: Invalid request parameter tif value: rpi` | 当前交易所或接口不接受 `tif=rpi`。请确认账户和交易对已开通 RPI 权限，否则改用普通限价单支持的 `time_in_force`。  
`label: INVALID_PARAM_VALUE, message: TimeInForce rpi is not support` | 当前交易所、业务类型或交易对不支持 RPI 委托。请改用支持 RPI 的交易通道，或使用 GTC、IOC 等受支持的委托方式。  
`Only post-only orders allowed immediately after network upgrade` | 交易所网络升级完成后的短时间内仅允许 Post Only 订单。请改用 Post Only，或等待交易所恢复其他委托类型后再下单。  
`marketIsPostOnly` | 当前市场处于仅允许 Post Only 的保护状态。请使用 Post Only 委托，或等待市场恢复正常交易后重试。  
  
###  交易所系统维护类错误

CrossEx无法在交易所维护期间为你执行挂单，针对此类异常，建议关注交易所公告，等待交易所恢复服务后再进行下单请求。

交易所系统维护类错误`reason`  
---  
`Order processing error temporarily, please try again later`  
`Systems are busy. Please try again later.`  
`Service is stopping`  
`{"jsonrpc":"2.0","error":{"message":"system_maintenance","code":11051}}`  
`502 bad gateway`  
  
##  异常 `label` 列表

以下错误按常见业务场景分类。`message` 是接口返回的原始错误信息，Tips 说明遇到问题后可以直接采取的处理方式。

###  通用、路由与权限类

通用、路由与权限类`label` | `message` | `tips`  
---|---|---  
`COMMON_PARAM_BIND_ERROR` | Invalid Parameter, please check api doc | 检查请求字段名、字段类型和 JSON 格式；对照接口文档修正参数后再试  
`COMMON_MISSING_PARAM_ERROR` | Missing Parameter, please check api doc | 对照接口文档补齐必填参数；特别检查请求体、路径参数和查询参数是否遗漏  
`TRADE_UNSUPPORTED_OPERATION` | This operation is not currently supported | 当前交易所、业务类型或接口组合不支持该操作；确认三者匹配后再请求  
`NOT_BEST_ACCOUNT_ROUTER` | Your order was not executed. All trading channels are currently busy. Consider reducing the order amount, selecting a different exchange symbol, or trying again later. | 交易通道繁忙；减小订单、切换交易所 symbol，或稍后重试  
`TRADE_ASSET_NOT_EXISTS_ERROR` | Asset is not exists | 账户中没有对应资产；先初始化资产或转入该币种  
  
###  账户与账户模式类

账户与账户模式类`label` | `message` | `tips`  
---|---|---  
`USER_NOT_EXIST` | user does not exist | 请稍后重试  
`QUERY_INVALID_EXCHANGE_TYPE` | The exchange_type is invalid. When the account_mode is ISOLATED_EXCHANGE, it should be GATE, BINANCE, BYBIT, OKX, KRAKEN, HYPERLIQUID, DERIBIT or LIGHTER | 分所模式下请使用 GATE、BINANCE、BYBIT、OKX、KRAKEN、HYPERLIQUID、DERIBIT 或 LIGHTER  
`TRADE_CHANGE_PZ_MODE_SAME_ERROR` | No need to repeatedly change your position mode | 当前已经是目标持仓模式，不需要重复设置  
`TRADE_PZ_MODE_HAVE_ORDER_ERROR` | Change failed. Please cancel any open order and close positions first. | 先撤销全部合约挂单，再修改持仓模式  
`TRADE_PZ_MODE_HAVE_POSITION_ERROR` | Change failed. Please cancel any open order and close positions first. | 先关闭全部合约仓位，再修改持仓模式  
`UPDATE_ACCOUNT_PARAMETERS_ALL_EMPTY_ERROR` | The request parameters cannot all be empty. | 至少传入一个需要修改的账户参数  
`UPDATE_ACCOUNT_PARAMETERS_ERROR` | Cannot set both positionMode and accountMode at the same time. | 修改账户模式和持仓模式,不能同时进行,只传一个  
`UPDATE_ACCOUNT_EXCHANGE_TYPE_PARAMETERS_ERROR` | exchangeType must be provided with positionMode. | 传 exchangeType 时必须同时传 positionMode；如果不修改持仓模式，请不要单独传 exchangeType  
`UPDATE_ACCOUNT_ACCOUNT_MODE_ERROR` | Invalid accountMode , please check api doc | accountMode 只能使用接口文档支持的值，请修正后重试  
`UPDATE_ACCOUNT_EXCHANGE_TYPE_ERROR` | Invalid exchangeType , please check api doc | exchangeType 只能使用接口支持的交易所枚举，请修正后重试  
`UPDATE_ACCOUNT_PZ_ISOLATED_MODE_NOT_EXCHANGE_TYPE_ERROR` | When updating the position mode in isolated mode, the exchange type parameter is required. | 分所模式修改持仓模式时，需要补充 `exchange_type` 参数  
`UPDATE_ACCOUNT_MODE_OPEN_ORDERS_EXIST_ERROR` | The account must not have any open orders to update the account mode. | 先撤销全部挂单，再修改账户模式  
`UPDATE_ACCOUNT_MODE_POSITION_NOT_EMPTY_ERROR` | The account must not have any open positions to update the account mode. | 先关闭全部合约和杠杆仓位，再修改账户模式  
`UPDATE_ACCOUNT_MODE_INITIAL_MARGIN_NOT_ZERO_ERROR` | The account must have zero initial margin to update the account mode. | 先撤单并平仓，确认初始保证金归零后再修改账户模式  
`UPDATE_ACCOUNT_MODE_MAINTENANCE_MARGIN_NOT_ZERO_ERROR` | The account must have zero maintenance margin to update the account mode. | 先关闭全部仓位，确认维持保证金归零后再修改账户模式  
`UPDATE_ACCOUNT_MODE_ACCOUNT_STATUS_NOT_NORMAL_ERROR` | The account status must be NORMAL to update the account mode. | 账户状态恢复为 NORMAL 后才能修改账户模式  
`UPDATE_ACCOUNT_CROSSEX_MODE_EXCHANGE_TYPE_NOT_CROSSEX_ERROR` | In cross-exchange mode, the exchange type must be CROSSEX. | 跨所模式下 exchangeType 必须传 CROSSEX  
`UPDATE_ACCOUNT_ISOLATED_MODE_EXCHANGE_TYPE_NOT_CROSSEX_ERROR` | In isolated mode, the exchange type must not be CROSSEX. | 分所模式下请指定具体交易所，不能传 CROSSEX  
`TRADE_INVALID_PZ_MODE_ERROR` | Invalid positionMode | positionMode 只能使用接口支持的持仓模式  
  
###  闪兑类

闪兑类`label` | `message` | `tips`  
---|---|---  
`CONVERT_TRADE_QUOTE_EXCHANGE_INVALID_ERROR` | Invalid exchangeType , please check api doc | 改用闪兑接口支持的交易所  
`CONVERT_TRADE_QUOTE_FROM_COIN_INVALID_ERROR` | Invalid fromCoin , please check api doc | 检查 fromCoin 拼写，并确认该币种支持闪兑  
`CONVERT_TRADE_QUOTE_TO_COIN_INVALID_ERROR` | Invalid toCoin, please check api doc | 检查 toCoin，并确认兑换方向受支持且两个币种不同  
`CONVERT_TRADE_QUOTE_FROM_AMOUNT_INVALID_ERROR` | Invalid fromAmount , please check api doc | fromAmount 必须是合法数字，最多保留 16 位小数  
`CONVERT_TRADE_QUOTE_FROM_AMOUNT_LIMIT_ERROR` | Invalid fromAmount, fromAmount can't be less than zero | fromAmount 必须大于 0  
`CONVERT_TRADE_QUOTE_FROM_AMOUNT_MAX_ERROR` | Invalid fromAmount, fromAmount value can't be greater than %s USDT | 把兑换金额控制在 %s USDT 以内  
`CONVERT_TRADE_QUOTE_EXCHANGE_REJECT_ERROR` | Convert quote request reject by Exchange, reason : %s | 根据 message 中交易所返回的具体原因调整请求后再试  
`TRADE_CONVERT_QUOTE_ERROR` | Quote does not exist or has expired | 报价不存在、已过期或已使用；请重新获取 quote 后再下单  
  
###  一键平仓类

一键平仓类`label` | `message` | `tips`  
---|---|---  
`CAN_NOT_DELETE_POSITION` | With a position size of 0, it is impossible to completely close out the position. | 仓位已经为 0 时无需再次一键平仓  
`CAN_NOT_DELETE_LARGE_POSITION` | The position size is too large to close at market price. Close the position by placing an order first. | 当前仓位价值过大，只允许仓位价值比名义价值小的仓位才能一键平仓  
`OPEN_ORDERS_CAN_NOT_DELETE_POSITION` | Open orders exist, positions cannot be deleted. | 一键平仓需要先撤销该 symbol 的全部挂单  
  
###  下单参数与币对类

下单参数与币对类`label` | `message` | `tips`  
---|---|---  
`TRADE_CLIENT_ORDER_ID_LENGTH_ERROR` | The order_id must less than 64 | 缩短客户端订单 ID，长度必须小于 64 个字符  
`TRADE_CLIENT_ORDER_ID_MATCH_ERROR` | Text only support letters and numbers | 客户端订单 ID 只使用接口允许的字母和数字  
`TRADE_INVALID_SIDE` | Invalid side | side 只能使用接口支持的买卖方向  
`TRADE_INVALID_ORDER_TYPE` | Invalid order_type | 改用当前业务和交易所支持的订单类型  
`TRADE_INVALID_TIME_IN_FORCE` | Invalid time_in_force | time_in_force 必须与订单类型匹配；例如市价单不要使用 POC  
`TRADE_INVALID_POC` | Market order timeInForce can't be POC | 市价单不能使用 POC，请改用支持的 time_in_force  
`TRADE_INVALID_ORDER_QTY` | Invalid qty | qty 必须是大于 0 的合法数字，并符合币对精度要求  
`TRADE_INVALID_QUOTE_ORDER_QTY` | Invalid quote_qty | quote_qty 必须是大于 0 的合法数字  
`TRADE_INVALID_LIMIT_PRICE` | Invalid limitPrice | 检查价格格式和正负值，并确保价格符合交易所限制  
`TRADE_INVALID_REDUCE_ONLY` | Invalid reduceOnly | reduceOnly 只能传合法布尔值 true 或 false  
`TRADE_SYM_NOT_SUPPORT` | The symbol is not supported | 确认 symbol 已上线，并检查交易所、业务类型和币对拼写  
`TRADE_NOT_SUPPORT_SYMBOLS_ERROR` | These symbols are not supported: [%s] | 查看 message 中列出的 symbol；删除不支持的币对，或改用已上线且符合接口业务类型的 symbol  
`TRADE_MARGIN_INVALID_PZ_SIDE_ERROR` | Invalid position_side, margin order position_side must be LONG or SHORT | 杠杆订单必须指定 LONG 或 SHORT  
`TRADE_INVALID_POSITION_SIDE` | Invalid position_side | position_side 必须与当前持仓模式一致  
`TRADE_INVALID_PZ_SIDE_ERROR` | Invalid position_side, your position_mode is dual, so position_side must be LONG or SHORT | 双向持仓模式下 position_side 必须传 LONG 或 SHORT  
`TRADE_INVALID_EXCHANGE_TYPE` | Invalid exchange_type | 检查 symbol 前缀和 exchange_type 是否一致，并改用当前业务支持的交易所  
`TRADE_INVALID_MARGIN_MODE_ERROR` | Invalid margin_mode | margin_mode 只能使用 CROSS 或 ISOLATED  
`TRADE_INVALID_SYM_BUSINESSTYPE_ERROR` | The symbol should be FUTURE businessType | 该操作需要 FUTURE 类型的 symbol，请不要传 SPOT 或 MARGIN symbol  
`TRADE_INVALID_MARGIN_SYM_BUSINESSTYPE_ERROR` | The symbol should be MARGIN businessType | 该操作需要 MARGIN 类型的 symbol，请不要传 SPOT 或 FUTURE symbol  
  
###  订单限制、查询与改单类

订单限制、查询与改单类`label` | `message` | `tips`  
---|---|---  
`TRADE_ORDER_DUPLICATE_ERROR` | Text duplicate | 使用唯一的客户端订单 ID，避免重复提交同一个 text  
`TRADE_ONE_OF_ORDER_ID_ERROR` | One of the order_id or text must be send | order_id 和 text 至少传一个；同时传入时优先使用 order_id  
`TRADE_ORDER_ID_ERROR` | Invalid orderId | order_id 必须是大于 0 的数字；请检查是否误传了 text 或其他字段  
`TRADE_ORDER_ID_LENGTH` | OrderId length must be 16 digits | 使用接口返回的完整 16 位 order_id，不要截断或自行拼接  
`TRADE_ORDER_NOT_FOUND_ERROR` | The order was not found | 检查订单 ID、用户归属和订单状态；已结束订单可能无法再用 text 查询  
`TRADE_NOT_ALLOW_REPLACE` | Market order not allowed replace | 市价单不能改单，请撤单后重新下单  
`TRADE_ORDER_REPLACE_QTY_PRICE_ERROR` | Replace price or qty invalid | 检查改单后的价格和数量是否为合法值  
`TRADE_ORDER_REPLACE_QTY_PRICE_SAME_ERROR` | The qty and price have not changed | 价格和数量至少修改一项  
`TRADE_ORDER_REPLACE_ALLOW_ERROR` | Order state or type not allow replace | 只有处于可改单状态的限价单支持改单  
`TRADE_ORDER_LOT_SIZE_ERROR` | Order quantity is not multiple of lotSize | 把订单数量调整为 lotSize 的整数倍  
`TRADE_ORDER_QUANTITY_MAX_ERROR` | Order quantity should be less than the max quantity | 降低订单数量，使其不超过该币对的 max quantity  
`TRADE_ORDER_QUANTITY_MIN_ERROR` | Order quantity should be greater than the min quantity | 提高订单数量，使其达到该币对的 min quantity  
`TRADE_ORDER_TICK_SIZE_ERROR` | Order price is not multiple of tickSize | 把订单价格调整为 tickSize 的整数倍  
`TRADE_ORDER_AMOUNT_MIN_ERROR` | Order amount should be greater than the min notional | 提高数量或价格，使订单金额达到 minNotional  
`TRADE_MAX_ORDERS_ERROR` | The open order num exceeds the limit | 先撤销部分挂单，待未完成订单数低于上限后再下单  
`TRADE_ORDER_REPLACE_INSUFFICIENT_AVAILABLE_ERROR` | Replace order failed. Insufficient available | 改单后余额不足；减小新数量或金额，或先补充余额  
  
###  仓位、保证金与减仓类

仓位、保证金与减仓类`label` | `message` | `tips`  
---|---|---  
`MARGIN_ORDER_NOT_SUPPORT` | ISOLATED_EXCHANGE account mode does not currently support MARGIN order. | 分所模式暂不支持杠杆交易；请切换到跨所模式，或改用支持的业务  
`TRADE_APPEND_BALANCE_ERROR` | Insufficient margin. Leverage cannot be adjusted | 可用保证金不足；先补充保证金或减小仓位，再调整杠杆  
`TRADE_BOTH_REDUCE_ERROR` | This order is close order, but your positionQty is 0 | 当前仓位为 0，不要继续提交平仓单；先刷新仓位状态  
`TRADE_CHANGE_MARGIN_MODE_SAME_ERROR` | No need to repeatedly change margin mode | 当前已经是目标保证金模式，不需要重复设置  
`TRADE_EXCEED_MAX_NOTIONAL` | Place order failed. Your open position value exceeds the max notional, you should reduce your open value or lower your leverage | 减小订单或仓位规模；如仍超限，再降低杠杆  
`TRADE_INSUFFICIENT_AVAILABLE_ERROR` | Insufficient available balance | 可用余额不足；转入资产或减小订单数量  
`TRADE_INSUFFICIENT_AVAILABLE_MARGIN_ERROR` | Insufficient availableMargin | 可用保证金不足；补充保证金，或减小仓位和订单规模  
`TRADE_INVALID_ISOLATED_MARGIN_ERROR` | Invalid margin | margin 必须是非零合法数字；正数增加保证金，负数减少保证金  
`TRADE_ISOLATED_MARGIN_TOO_SMALL_ERROR` | The absolute margin amount must be at least 0.01 | 保证金调整金额的绝对值必须大于等于 0.01  
`TRADE_ISOLATED_MARGIN_NOT_SUPPORT` | Only isolated positions support margin adjustment | 只有 Hyperliquid 隔离合约仓位支持调整保证金  
`TRADE_MARGIN_MODE_NOT_SUPPORT` | This symbol does not support changing margin mode | 该币对不支持修改保证金模式  
`TRADE_POSITION_EXCEED_MAX_NOTIONAL_LIMIT` | Position value exceeds the max risk limit value | 减小当前仓位或新订单规模，使仓位价值回到风险限额以内  
`TRADE_POSITION_NOT_FOUND_ERROR` | The position was not found | 检查 symbol 和 position_side；仓位为 0 时无需执行仓位操作  
`TRADE_REDUCE_ISOLATED_MARGIN_ERROR` | The remaining isolated margin does not meet the transfer margin requirement | 减少保证金转出金额，确保剩余隔离保证金仍满足要求  
`TRADE_REDUCE_ONLY_CANNOT_PLACE_IN_THIS_PRICE` | Can not place reduce order | 调整减仓价格或数量；必要时撤销冲突的 reduce-only 订单后重试  
`TRADE_REDUCE_ONLY_ORDER_CANCELLED_ERROR` | Due to an order with a better price, %s reduce only order to %s %s %s at %s was cancelled | 系统因存在更优价格的减仓单而自动撤单；需要时按新价格重新挂单  
`TRADE_REDUCE_ONLY_POSITION_QTY_ERROR` | Can not place ReduceOnly order when position quantity is zero | 当前仓位为 0，不能提交 reduce-only 订单  
`TRADE_REDUCE_ONLY_SIDE_ERROR` | ReduceOnly orders must be in the opposite direction of the position | 减仓方向必须与当前持仓方向相反  
`TRADE_REDUCE_TOO_SMALL_ERROR` | The positionQty occupied by this order is too small to be processed | 提高有效减仓量，或先撤销其他占用仓位的订单  
  
###  杠杆设置类

杠杆设置类`label` | `message` | `tips`  
---|---|---  
`TRADE_SET_LEVERAGE_ERROR` | Invalid leverage | leverage 必须是接口允许的正整数  
`TRADE_SET_LEVERAGE_EXCEED_LIMIT_ERROR` | The leverage you have set exceeds the maximum leverage limit | 把杠杆降低到该 symbol 或当前仓位允许的最大值以内  
`TRADE_LEVERAGE_MARGIN_OPEN_ERROR` | The maximum leverage of the exchange has been adjusted. Please reduce your positionQty or reset your leverage. | 交易所已调整杠杆上限；先减仓或把杠杆重设到最新上限  
`TRADE_LEVERAGE_MARGIN_REVERSE_OPEN_ERROR` | The maximum leverage of the exchange has been adjusted. Only can reduce your current positionQty, reverse open is not allowed. | 当前只能减仓；先重设杠杆，再尝试反向开仓  
  
###  清算、下架与风控类

清算、下架与风控类`label` | `message` | `tips`  
---|---|---  
`RISK_CHECK_MARKET_FORBIDDEN` | Risk management requirements prohibit operations. | 当前操作被风控拦截；等待限制解除，持续发生时请联系我们  
`TRADE_DELIST_OPEN_PROHIBITED_ERROR` | Symbol delisted. Opening positions is prohibited. | 该币对已下架，只能提交减仓或平仓订单  
  
###  RPI 订单类

RPI 订单类`label` | `message` | `tips`  
---|---|---  
`TRADE_RPI_EXCHANGE_NOT_SUPPORT` | The exchange or business type does not support RPI orders | 需要改用支持 RPI 的交易所和业务类型  
`TRADE_RPI_LIMIT_ORDER_REQUIRED` | RPI orders must be limit orders | RPI 订单必须使用限价单  
`TRADE_RPI_REPLACE_NOT_SUPPORT` | Binance RPI order replace is not supported | Binance RPI 不支持改单，请撤单后重新下单  
`TRADE_RPI_SYMBOL_NOT_SUPPORT` | The symbol does not support RPI orders | 改用支持 RPI 的 symbol  
`TRADE_RPI_USER_NOT_SUPPORT` | The user is not allowed to place RPI orders | 当前账户没有 RPI 下单权限；请申请权限，或改用普通限价单  
  
###  交易所专项限制

交易所专项限制`label` | `message` | `tips`  
---|---|---  
`TRADE_OKX_LIMIT_BUY_ORDER_PRICE_ERROR` | Due to OKX's trading rule, the limit price for a buy order cannot be less than 1/3 of the last price or mark price. | 提高 OKX 限价买单价格，不能低于最新价或标记价的三分之一  
`TRADE_HYPERLIQUID_ORDER_LIMIT_ERROR` | Too many order sent for Hyperliquid. Place taker orders to free up 1 request per USDC traded. | 降低 Hyperliquid 下单频率并等待额度恢复；也可按交易所规则提交 taker 单释放额度  
`TRADE_LIGHTER_ORDER_LIMIT_ERROR` | Too many orders sent for Lighter. Place taker orders to free up 1 request per 2 USDC traded. | 降低 Lighter 下单频率并等待额度恢复；每 2 USDC 的 taker 成交量可恢复 1 次请求额度  
`TRADE_HYPERLIQUID_ORDER_REPLACE_EXECUTED_ERROR` | Hyperliquid orders with executed quantity do not support replace | Hyperliquid订单已有成交，不能直接改单；撤销剩余部分后重新下单  
`TRADE_HYPERLIQUID_PRICE_SIGNIFICANT_FIGURES_ERROR` | Order price exceeds Hyperliquid exchange limit: at most 5 significant figures | Hyperliquid订单价格最多 5 位有效数字  
  
#  跨所交易

CrossEx是一个跨交易所交易平台,允许用户通过统一账户在多个交易所(Binance、OKX、Gate、Bybit、Kraken、Hyperliquid、Deribit、Lighter)进行交易，并接入美股、港股、韩股和日股。CrossEx API提供完整的账户管理、资产划转、下单和仓位管理功能,支持跨交易所操作。

  * 股票及ETF仅支持跨所账户模式；股票市场使用US、HK、KR、JP作为exchange_type，使用STOCK、ETF作为business_type
  * REST API BaseURL 实盘交易: `https://api.gateio.ws/api/v4`
  * [帮助中心 ](https://www.gate.com/help/crossex/functional)
  * [跨所交易 ](https://www.gate.com/crossex)

##  查询币对信息

GET`/crossex/rule/symbols`

GET `/crossex/rule/symbols`

_查询币对信息_

查询交易对信息。 股票及ETF的交易对格式为 `{市场}_{业务类型}_{证券代码}_USDT`，例如 `US_STOCK_AAPL_USDT`、`HK_STOCK_00700_USDT`、`US_ETF_SPY_USDT`。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 否 | 币对列表，多个以逗号分隔  
示例值:  
BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT,US_STOCK_AAPL_USDT  
  
  
####  详细描述

**symbols** : 币对列表，多个以逗号分隔  
示例值:  
BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT,US_STOCK_AAPL_USDT  

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Symbol]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array |   
» symbol | string | 交易对唯一标识，格式为 ExchangeType_BusinessType_Base_Counter。  
股票及ETF使用市场作为ExchangeType（US/HK/KR/JP），业务类型为STOCK或ETF，例如US_STOCK_AAPL_USDT、HK_STOCK_00700_USDT、US_ETF_SPY_USDT。  
» exchange_type | string | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER）；股票及ETF返回上市市场（US / HK / KR / JP）  
» business_type | string | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆 / STOCK 股票 / ETF 交易所交易基金）  
» state | string | 状态（live 在线 / suspend 暂停）  
» min_size | string | 最小下单数量  
» min_notional | string | 最小下单价值  
» lot_size | string | 数量步长  
» tick_size | string | 价格步长  
» max_num_orders | string | 最大挂单数量  
» max_market_size | string | 市价单最大下单数量  
» max_limit_size | string | 限价单最大下单数量  
» contract_size | string | 合约乘数（已废弃，统一是量）  
» liquidation_fee | string | 清算费率  
» default_leverage | string | 默认杠杆倍数  
» delist_time | string | 毫秒时间戳，0 表示正常未下架  
» support_rpi | string | 是否支持rpi下单(true支持,false不支持)  
» support_cross | string | 是否支持全仓下单(true支持,false不支持)  
» tag | string | 标签信息。Hyperliquid返回DEX信息；股票及ETF返回证券描述；其他业务返回空字符串  
  
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
        "support_rpi": "false",
        "support_cross": "true",
        "delist_time": "0",
        "tag": ""
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
        "delist_time": "1762163297615",
        "support_rpi": "false",
        "support_cross": "true",
        "tag": ""
      },
      {
        "symbol": "US_STOCK_AAPL_USDT",
        "exchange_type": "US",
        "business_type": "STOCK",
        "state": "live",
        "min_size": "0.01",
        "min_notional": "0",
        "lot_size": "0.01",
        "tick_size": "0.01",
        "max_num_orders": "0",
        "max_market_size": "0",
        "max_limit_size": "0",
        "contract_size": "0",
        "liquidation_fee": "0",
        "delist_time": "0",
        "support_rpi": "false",
        "support_cross": "true",
        "tag": "Apple Inc."
      }
    ]
    

##  查询平台剩余可开仓价值

GET`/crossex/rule/open_capacity`

GET `/crossex/rule/open_capacity`

_查询平台剩余可开仓价值_

查询各合约交易对在 LONG、SHORT 方向当前剩余的最大开仓名义价值。 结果仅包含剩余可开仓价值低于阈值的交易对和仓位方向；未出现在结果中表示其剩余可开仓价值不低于该阈值。 `available_to_open_notional` 为 `0` 时，表示该交易对在对应仓位方向当前不能开仓。平仓方向不受该规则影响

### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 查询成功 | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexOpenCapacity | object |   
»» symbol | string | 合约交易对  
»» position_side | string | 仓位方向（LONG 多仓 / SHORT 空仓）  
»» available_to_open_notional | number(decimal) | 对应仓位方向当前剩余的最大开仓名义价值；0 表示当前不能开仓  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
position_side | LONG  
position_side | SHORT  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/crossex/rule/open_capacity'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/crossex/rule/open_capacity \
      -H 'Accept: application/json'
    
    

> 返回示例

> 200 返回
    
    
    [
      {
        "symbol": "GATE_FUTURE_HIVE_USDT",
        "position_side": "LONG",
        "available_to_open_notional": 390.625
      },
      {
        "symbol": "GATE_FUTURE_HIVE_USDT",
        "position_side": "SHORT",
        "available_to_open_notional": 390.625
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

`est_fee`: 预估手续费, 当你的资金划转涉及链上提现时, 该手续费由交易所收取, 此值为参考值, 实际情况以交易所为准

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
»» min_trans_amount | number | 最小划转数量(已经包含预估手续费)  
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
    

##  资金划转🔒 需要认证

POST`/crossex/transfers`

POST `/crossex/transfers`

_资金划转_

限频：每10秒10次请求

  * 在跨所模式下，划转USDT，`from` & `to`任意一侧必须为`SPOT`， 相应地另一侧应该是`CROSSEX` 如果填写的是`CROSSEX_${exchange_type}`(如`CROSSEX_GATE`)，会默认为你设置为`CROSSEX`
  * 在分所模式下，划转USDT，`from` & `to`任意一侧必须为`CROSSEX_${exchange_type}`，相应地另一侧应该是`SPOT`或者`CROSSEX_${exchange_type}` 如果填写的是`CROSSEX`，会默认为你设置为`CROSSEX_GATE`
  * 划转非USDT币种时，从CrossEx 进行转入或者转出，`from` & `to` 任意一侧都不可以是`CROSSEX`，必须指定为`CROSSEX_${exchange_type}`
  * 划转非USDT币种时，可以进行`CROSSEX_{exchange_type}` 之间的划转，如from = `CROSSEX_BINANCE` , to = `CROSSEX_GATE`
  * 划转任意一侧为 `CROSSEX_KRAKEN`时, 暂时只支持USDT
  * 划转任意一侧为 `CROSSEX_DERIBIT`时, 暂时只支持USDC
  * 划转任意一侧为 `CROSSEX_HYPERLIQUID`时, 另一侧只能为`SPOT`, coin只支持USDC
  * 划转任意一侧为 `CROSSEX_LIGHTER`时, 另一侧只能为`SPOT`, coin只支持USDC

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexTransferRequest | 否 |   
» coin | body | string | 是 | 币种  
» amount | body | string | 是 | 转账数量  
» from | body | string | 是 | 转出账户: CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX_HYPERLIQUID, CROSSEX_DERIBIT, CROSSEX_LIGHTER, CROSSEX, SPOT  
» to | body | string | 是 | 转入账户: CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX_HYPERLIQUID, CROSSEX_DERIBIT, CROSSEX_LIGHTER, CROSSEX, SPOT  
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
  
####  详细描述

**order_id** : 支持查询创建订单时返回的订单ID即tx_id字段，支持用户创建时指定的自定义ID即text字段  

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
»» from_account_type | string | 操作的from账户（CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX_HYPERLIQUID, CROSSEX_DERIBIT, CROSSEX_LIGHTER, CROSSEX, SPOT）  
»» to_account_type | string | 操作的to账户（CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX_HYPERLIQUID, CROSSEX_DERIBIT, CROSSEX_LIGHTER, CROSSEX, SPOT）  
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
    

##  下单🔒 需要认证

POST`/crossex/orders`

POST `/crossex/orders`

_下单_

限频：每10秒100次请求，单个用户的最大挂单数为1,000个。 股票及ETF额外单用户1次/1s，仅支持跨所账户模式和GTC；股票及ETF必须使用qty下单，不支持quote_qty下单。 股票及ETF的委托价格使用上市市场原生计价币种：美股为USD、港股为HKD、韩股为KRW、日股为JPY。

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
如果您想在KRAKEN交易所上为ADA/USD交易对下合约订单，您可以使用这样的唯一标识符：`KRAKEN_FUTURE_ADA_USD`;  
如果您想在HYPERLIQUID交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`HYPERLIQUID_FUTURE_ADA_USDC`;  
如果您想在DERIBIT交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`DERIBIT_FUTURE_ADA_USDC`;  
如果您想在LIGHTER交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`LIGHTER_FUTURE_ADA_USDC`;  
如果您想交易美股AAPL，可以使用这样的唯一标识符：`US_STOCK_AAPL_USDT`;  
如果您想交易港股00700，可以使用这样的唯一标识符：`HK_STOCK_00700_USDT`;  
如果您想交易美股ETF SPY，可以使用这样的唯一标识符：`US_ETF_SPY_USDT`;  
目前支持现货订单、U本位永续合约订单、现货杠杆订单、股票订单和ETF订单。BYBIT/DERIBIT暂不支持现货杠杆订单，KRAKEN、HYPERLIQUID、LIGHTER暂不支持现货与杠杆订单；股票及ETF仅支持跨所账户模式  
» side | body | string | 是 | BUY, SELL  
» type | body | string | 否 | 订单类型（默认`LIMIT`，支持类型列举：`LIMIT`、`MARKET`）  
» time_in_force | body | string | 否 | 默认GTC，支持类型枚举，`GTC`，`IOC`，`FOK`，`POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
股票及ETF仅支持`GTC`  
» qty | body | string | 否 | 订单数量（强制性，除非现货和杠杆市价买入；股票及ETF必须传qty）  
» price | body | string | 否 | 限价订单价格（限价订单必须）。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
» quote_qty | body | string | 否 | 订单报价数量，现货和杠杆市价买单必传；股票及ETF不支持quote_qty下单  
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
如果您想在KRAKEN交易所上为ADA/USD交易对下合约订单，您可以使用这样的唯一标识符：`KRAKEN_FUTURE_ADA_USD`;  
如果您想在HYPERLIQUID交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`HYPERLIQUID_FUTURE_ADA_USDC`;  
如果您想在DERIBIT交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`DERIBIT_FUTURE_ADA_USDC`;  
如果您想在LIGHTER交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`LIGHTER_FUTURE_ADA_USDC`;  
如果您想交易美股AAPL，可以使用这样的唯一标识符：`US_STOCK_AAPL_USDT`;  
如果您想交易港股00700，可以使用这样的唯一标识符：`HK_STOCK_00700_USDT`;  
如果您想交易美股ETF SPY，可以使用这样的唯一标识符：`US_ETF_SPY_USDT`;  
目前支持现货订单、U本位永续合约订单、现货杠杆订单、股票订单和ETF订单。BYBIT/DERIBIT暂不支持现货杠杆订单，KRAKEN、HYPERLIQUID、LIGHTER暂不支持现货与杠杆订单；股票及ETF仅支持跨所账户模式

**» time_in_force** : 默认GTC，支持类型枚举，`GTC`，`IOC`，`FOK`，`POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
股票及ETF仅支持`GTC`

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
» time_in_force | RPI  
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
    

##  批量撤单🔒 需要认证

POST`/crossex/batch_cancel_orders`

POST `/crossex/batch_cancel_orders`

_批量撤单_

批量撤销指定订单，order_id 或 text 必传其一；同时传入时优先使用 order_id。限频：每10秒100次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | array[CrossexBatchCancelOrderRequest] | 是 |   
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 批量撤单请求处理结果 | [CrossexBatchCancelOrderResponse]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
_None_ | array | [批量撤单请求处理结果]  
» CrossexBatchCancelOrderResponse | CrossexBatchCancelOrderResponse | 批量撤单请求处理结果  
»» order_id | string | 订单 ID  
»» text | string | 用户创建订单时指定的自定义 ID  
»» accepted | string | 是否受理成功，字符串 true 或 false  
»» label | string | 受理失败时的错误标识，成功时为空  
»» message | string | 受理失败时的错误信息，成功时为空  
  
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
    
    url = '/crossex/batch_cancel_orders'
    query_param = ''
    body='[{"order_id":"123456"},{"text":"crossex-test-1"}]'
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
    url="/crossex/batch_cancel_orders"
    query_param=""
    body_param='[{"order_id":"123456"},{"text":"crossex-test-1"}]'
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
        "order_id": "123456"
      },
      {
        "text": "crossex-test-1"
      }
    ]
    

> 返回示例

> 200 返回
    
    
    [
      {
        "order_id": "123456",
        "text": "",
        "accepted": "true",
        "label": "",
        "message": ""
      },
      {
        "order_id": "",
        "text": "crossex-test-1",
        "accepted": "false",
        "label": "TRADE_ORDER_NOT_FOUND_ERROR",
        "message": "The order was not found"
      }
    ]
    

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
      "text": "crossex-test-1"
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
CANCELLED: 订单被取消  
» symbol | string | 交易对唯一标识，示例：  
BINANCE_SPOT_BTC_USDT、BINANCE_FUTURE_BTC_USDT  
» side | string | 方向（BUY 买入 / SELL 卖出）  
» type | string | 订单类型（LIMIT 限价 / MARKET 市价）  
» attribute | string | 订单属性（COMMON 普通单 / LIQ 强平接管单 / REDUCE 强平减仓单 / ADL 自动减仓 / SETTLEMENT 下架清算）  
» exchange_type | string | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER）；股票及ETF返回上市市场（US / HK / KR / JP）  
» business_type | string | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆 / CONVERT 闪兑 / STOCK 股票 / ETF 交易所交易基金）  
» qty | string | 基础货币下单数量  
» quote_qty | string | 报价币种下单数量  
» price | string | 订单价格。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
» time_in_force | string | 时效策略（默认 GTC，枚举值：GTC / IOC / FOK / POC / RPI）  
» executed_qty | string | 已成交基础货币数量  
» executed_amount | string | 已成交报价币种金额。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
» executed_avg_price | string | 已成交均价。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
» fee_coin | string | 手续费币种  
» fee | string | 手续费金额  
» reduce_only | string | 是否仅减仓订单（"true" 或 "false"）  
» leverage | string | 订单杠杆倍数  
» reason | string | 失败原因描述  
» last_executed_qty | string | 最新一次成交数量  
» last_executed_price | string | 最新一次成交价格。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
» last_executed_amount | string | 最新一次成交金额。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
» position_side | string | 仓位方向（NONE 单向持仓 / LONG 多仓 / SHORT 空仓）  
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
    

##  闪兑询价🔒 需要认证

POST`/crossex/convert/quote`

POST `/crossex/convert/quote`

_闪兑询价_

限频：每天100次请求 针对HYPERLIQUID, 支持`HYPERLIQUID_USDC` & `CROSSEX_USDT` 互兑, 暂不支持分所模式的HYPERLIQUID闪兑 针对LIGHTER, 支持`LIGHTER_USDC` & `CROSSEX_USDT` 互兑, 暂不支持分所模式的LIGHTER闪兑 针对KRAKEN, 仅支持`KRAKEN_USD`兑换为`CROSSEX_USDT`, 暂不支持分所模式的KRAKEN闪兑

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexConvertQuoteRequest | 否 |   
» exchange_type | body | string | 是 | 交易所类型  
目前仅支持 BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, LIGHTER  
» from_coin | body | string | 是 | 卖出的资产  
» to_coin | body | string | 是 | 买入的资产名称  
OKX, GATE 只允许兑换成BTC, ETH, USDT  
BYBIT, BINANCE 只允许兑换成USDT  
HYPERLIQUID 只允许兑换成USDT, USDC  
KRAKEN 只允许兑换成USDT  
LIGHTER 只允许USDT与USDC互兑  
» from_amount | body | string | 是 | 卖出的资产数量  
  
####  详细描述

**» exchange_type** : 交易所类型  
目前仅支持 BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, LIGHTER

**» to_coin** : 买入的资产名称  
OKX, GATE 只允许兑换成BTC, ETH, USDT  
BYBIT, BINANCE 只允许兑换成USDT  
HYPERLIQUID 只允许兑换成USDT, USDC  
KRAKEN 只允许兑换成USDT  
LIGHTER 只允许USDT与USDC互兑

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
» price | string | 报价价格  
  
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
» exchange_type | body | string | 否 | 交易所（BINANCE/OKX/GATE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT/LIGHTER/CROSSEX，当账户模式为ISOLATED_EXCHANGE时，修改合约仓位模式必须指定交易所）  
  
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
» exchange_type | string | 请求修改的交易所（BINANCE/OKX/GATE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT/LIGHTER/CROSSEX，当账户模式为ISOLATED_EXCHANGE时，修改合约仓位模式必须指定交易所）  
  
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
    body='{"position_mode":"SINGLE"}'
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
    body_param='{"position_mode":"SINGLE"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "position_mode": "SINGLE"
    }
    

> 返回示例

> 202 返回
    
    
    {
      "position_mode": "SINGLE"
    }
    

##  查询账户资产🔒 需要认证

GET`/crossex/accounts`

GET `/crossex/accounts`

_查询账户资产_

限频：每10秒200次请求 100% <= initial_margin_rate < 110%,禁止划出保证金币种 initial_margin_rate < 100%，系统自动撤单，只能平仓不能开仓 maintenance_margin_rate <= 100%，系统强制平仓

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
exchange_type | 请求参数 | string | 否 | 交易所。当跨所模式下不用传，当分所模式下必传(BINANCE/OKX/GATE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT/LIGHTER)  
  
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
»»» equity | string | 币种的保证金净资产权益  
»»» futures_initial_margin | string | 币种的合约初始保证金, 合约结算币种（USDT/USDC/USD）会有此值  
»»» futures_maintenance_margin | string | 币种的合约维持保证金, 合约结算币种（USDT/USDC/USD）会有此值  
»»» borrowing_initial_margin | string | 币种的杠杆交易初始保证金, 杠杆/合约结算币种（USDT/USDC/USD）会有此值  
»»» borrowing_maintenance_margin | string | 币种的杠杆交易维持保证金, 杠杆/合约结算币种（USDT/USDC/USD）会有此值  
»»» available_balance | string | 可用余额  
»»» liability | string | 币种负债, 仅（USDT/USDC/USD）会有值  
  
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
      "symbol": "OKX_FUTURE_ADA_USDT",
      "leverage": "1"
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
    

##  完全平仓🔒 需要认证

POST`/crossex/position`

POST `/crossex/position`

_完全平仓_

限频：每天100次请求。自动平仓规则。支持平仓FUTURE仓位或者MARGIN仓位

使用本接口前，需要满足以下前置条件：

  * 当前账户中不存在该symbol的任何挂单。
  * 在满足前置条件的情况下，当系统检测到仓位在满足以下任一限制时：
  * 小于最小名义金额（minNotional）
  * 小于最小下单数量（minSize）

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
    

##  修改合约仓位保证金模式🔒 需要认证

POST`/crossex/positions/margin_mode`

POST `/crossex/positions/margin_mode`

_修改合约仓位保证金模式_

限频：每10秒100次请求。仅支持Hyperliquid合约交易币对，存在挂单或仓位时不允许修改

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexMarginModeRequest | 否 |   
» symbol | body | string | 是 | Hyperliquid合约交易币对  
» margin_mode | body | string | 是 | 保证金模式（CROSS/ISOLATED）  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» margin_mode | CROSS  
» margin_mode | ISOLATED  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexMarginModeResponse  
  
### 返回格式

状态码 **202**

_CrossexMarginModeResponse_

名称 | 类型 | 描述  
---|---|---  
» symbol | string | 合约交易币对  
» margin_mode | string | 保证金模式（CROSS/ISOLATED）  
  
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
    
    url = '/crossex/positions/margin_mode'
    query_param = ''
    body='{"symbol":"HYPERLIQUID_FUTURE_CXMT_USDC","margin_mode":"ISOLATED"}'
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
    url="/crossex/positions/margin_mode"
    query_param=""
    body_param='{"symbol":"HYPERLIQUID_FUTURE_CXMT_USDC","margin_mode":"ISOLATED"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin_mode": "ISOLATED"
    }
    

> 返回示例

> 202 返回
    
    
    {
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin_mode": "ISOLATED"
    }
    

##  查询合约仓位保证金模式🔒 需要认证

GET`/crossex/positions/margin_mode`

GET `/crossex/positions/margin_mode`

_查询合约仓位保证金模式_

限频：每10秒200次请求

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | 请求参数 | string | 是 | 合约交易币对  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | CrossexMarginModeResponse  
  
### 返回格式

状态码 **200**

_CrossexMarginModeResponse_

名称 | 类型 | 描述  
---|---|---  
» symbol | string | 合约交易币对  
» margin_mode | string | 保证金模式（CROSS/ISOLATED）  
  
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
    
    url = '/crossex/positions/margin_mode'
    query_param = 'symbol=HYPERLIQUID_FUTURE_CXMT_USDC'
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
    url="/crossex/positions/margin_mode"
    query_param="symbol=HYPERLIQUID_FUTURE_CXMT_USDC"
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
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin_mode": "ISOLATED"
    }
    

##  增加或减少逐仓保证金🔒 需要认证

POST`/crossex/positions/margin`

POST `/crossex/positions/margin`

_增加或减少逐仓保证金_

限频：每10秒100次请求。仅支持Hyperliquid逐仓合约仓位，正数为增加保证金，负数为减少保证金

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | CrossexIsolatedMarginRequest | 否 |   
» symbol | body | string | 是 | Hyperliquid合约交易币对  
» margin | body | string | 是 | 保证金调整金额，正数为增加，负数为减少，超过两位小数时向下截断  
» position_side | body | string | 否 | 仓位方向（NONE/LONG/SHORT），单向持仓不传时默认为NONE  
  
####  枚举值列表

枚举值列表参数 | 值  
---|---  
» position_side | NONE  
» position_side | LONG  
» position_side | SHORT  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
202 | [Accepted ](https://tools.ietf.org/html/rfc7231#section-6.3.3) | none | CrossexIsolatedMarginResponse  
  
### 返回格式

状态码 **202**

_CrossexIsolatedMarginResponse_

名称 | 类型 | 描述  
---|---|---  
» symbol | string | 合约交易币对  
» margin | string | 本次增加或减少的逐仓保证金  
» position_side | string | 仓位方向（NONE/LONG/SHORT），单向持仓不传时默认为NONE  
  
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
    
    url = '/crossex/positions/margin'
    query_param = ''
    body='{"symbol":"HYPERLIQUID_FUTURE_CXMT_USDC","margin":"-30","position_side":"NONE"}'
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
    url="/crossex/positions/margin"
    query_param=""
    body_param='{"symbol":"HYPERLIQUID_FUTURE_CXMT_USDC","margin":"-30","position_side":"NONE"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> 请求体示例
    
    
    {
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin": "-30",
      "position_side": "NONE"
    }
    

> 返回示例

> 202 返回
    
    
    {
      "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
      "margin": "-30",
      "position_side": "NONE"
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
» spot_rpi_maker_fee | string | 现货RPI订单Maker费率  
» future_maker_fee | string | 合约Maker费率  
» future_taker_fee | string | 合约Taker费率  
» future_rpi_maker_fee | string | 合约RPI订单Maker费率  
» special_fee_list | array |   
»» CrossexSpecialFee | object |   
»»» symbol | string | 交易对  
»»» taker_fee_rate | string | Taker费率  
»»» maker_fee_rate | string | Maker费率  
»»» rpi_fee_rate | string | RPI订单Maker费率  
  
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
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": "",
        "special_fee_list": []
      },
      {
        "exchange_type": "OKX",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": "",
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
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": "",
        "special_fee_list": []
      },
      {
        "exchange_type": "BYBIT",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": "",
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
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": ""
      },
      {
        "exchange_type": "HYPERLIQUID",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": ""
      },
      {
        "exchange_type": "DERIBIT",
        "spot_maker_fee": "0.0001",
        "spot_taker_fee": "0.00025",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00006",
        "future_taker_fee": "0.00022",
        "future_rpi_maker_fee": ""
      },
      {
        "exchange_type": "LIGHTER",
        "spot_maker_fee": "0.0005",
        "spot_taker_fee": "0.0005",
        "spot_rpi_maker_fee": "",
        "future_maker_fee": "0.00005",
        "future_taker_fee": "0.00005",
        "future_rpi_maker_fee": ""
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
»» isolated_margin | string | 逐仓保证金。全仓时为0，仅逐仓有效  
»» margin_mode | string | 保证金模式（CROSS/ISOLATED）  
»» maintenance_margin | string | 维持保证金  
»» position_qty | string | 仓位数量  
»» position_value | string | 仓位价值  
»» upnl | string | 未结盈亏  
»» upnl_rate | string | 未结盈亏比  
»» entry_price | string | 仓位入场均价  
»» liq_price | string | 强平价格。全仓时为0，仅逐仓有效；逐仓时为0代表不强平  
»» mark_price | string | 标记价格  
»» leverage | string | 仓位杠杆  
»» max_leverage | string | 最大杠杆  
»» risk_limit | string | 风险限额  
»» fee | string | 仓位手续费  
»» funding_fee | string | 累计仓位资金费。正数代表有收益，负数代表有亏损  
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
        "isolated_margin": "0",
        "margin_mode": "CROSS",
        "maintenance_margin": "0.06229625",
        "position_qty": "10",
        "position_value": "5.795",
        "upnl": "0.369",
        "upnl_rate": "0.068005897530409141",
        "entry_price": "0.5426",
        "liq_price": "0",
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
    

##  查询证券仓位🔒 需要认证

GET`/crossex/security_positions`

GET `/crossex/security_positions`

_查询证券仓位_

查询股票及ETF仓位。限频：每10秒200次请求。 价格、持仓价值和未结盈亏使用上市市场原生计价币种：美股为USD、港股为HKD、韩股为KRW、日股为JPY。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbol | 请求参数 | string | 否 | 股票或ETF交易对  
exchange_type | 请求参数 | string | 否 | 股票市场（US/HK/KR/JP）  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexSecurityPosition | object |   
»» user_id | string | 用户ID  
»» symbol | string | 股票或ETF交易对  
»» price | string | 最新价格，单位为上市市场原生计价币种  
»» entry_price | string | 持仓成本价，单位为上市市场原生计价币种  
»» diluted_cost_price | string | 摊薄成本价，单位为上市市场原生计价币种  
»» upnl | string | 未结盈亏，单位为上市市场原生计价币种  
»» position_qty | string | 持仓数量  
»» position_value | string | 持仓价值，单位为上市市场原生计价币种  
  
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
    
    url = '/crossex/security_positions'
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
    url="/crossex/security_positions"
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
        "user_id": "59138103",
        "symbol": "HK_STOCK_00700_USDT",
        "price": "424.8",
        "entry_price": "428",
        "diluted_cost_price": "428",
        "upnl": "-0.032",
        "position_qty": "0.01",
        "position_value": "4.248"
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
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline  
  
### 返回格式

状态码 **200**

_CrossexAdlRank_

名称 | 类型 | 描述  
---|---|---  
» user_id | string | 用户id  
» symbol | string | 交易对  
» crossex_adl_rank | string | Crossex ADL 减仓优先级，取值为 1-5  
优先级从高到低：5、4、3、2、1  
» exchange_adl_rank | string | 交易所原始 ADL 排名。各交易所优先级从高到低如下：  
\- BINANCE：4、3、2、1、0  
\- OKX：5、4、3、2、1、0  
\- GATE：1、2、3、4、5  
\- Kraken：20、40、60、80、100  
\- BYBIT：5、4、3、2、1、0  
  
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
CANCELLED: 订单被取消  
»» symbol | string | 交易对唯一标识，示例：  
BINANCE_SPOT_BTC_USDT、BINANCE_FUTURE_BTC_USDT  
»» side | string | 方向（BUY 买入 / SELL 卖出）  
»» type | string | 订单类型（LIMIT 限价 / MARKET 市价）  
»» attribute | string | 订单属性（COMMON 普通单 / LIQ 强平接管单 / REDUCE 强平减仓单 / ADL 自动减仓 / SETTLEMENT 下架清算）  
»» exchange_type | string | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER）；股票及ETF返回上市市场（US / HK / KR / JP）  
»» business_type | string | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆 / CONVERT 闪兑 / STOCK 股票 / ETF 交易所交易基金）  
»» qty | string | 基础货币下单数量  
»» quote_qty | string | 报价币种下单数量  
»» price | string | 订单价格。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» time_in_force | string | 时效策略（默认 GTC，枚举值：GTC / IOC / FOK / POC / RPI）  
»» executed_qty | string | 已成交基础货币数量  
»» executed_amount | string | 已成交报价币种金额。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» executed_avg_price | string | 已成交均价。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» fee_coin | string | 手续费币种  
»» fee | string | 手续费金额  
»» reduce_only | string | 是否仅减仓订单（"true" 或 "false"）  
»» leverage | string | 订单杠杆倍数  
»» reason | string | 失败原因描述  
»» last_executed_qty | string | 最新一次成交数量  
»» last_executed_price | string | 最新一次成交价格。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» last_executed_amount | string | 最新一次成交金额。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» position_side | string | 仓位方向（NONE 单向持仓 / LONG 多仓 / SHORT 空仓）  
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
CANCELLED: 订单被取消  
»» symbol | string | 交易对唯一标识，示例：  
BINANCE_SPOT_BTC_USDT、BINANCE_FUTURE_BTC_USDT  
»» side | string | 方向（BUY 买入 / SELL 卖出）  
»» type | string | 订单类型（LIMIT 限价 / MARKET 市价）  
»» attribute | string | 订单属性（COMMON 普通单 / LIQ 强平接管单 / REDUCE 强平减仓单 / ADL 自动减仓 / SETTLEMENT 下架清算）  
»» exchange_type | string | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER）；股票及ETF返回上市市场（US / HK / KR / JP）  
»» business_type | string | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆 / CONVERT 闪兑 / STOCK 股票 / ETF 交易所交易基金）  
»» qty | string | 基础货币下单数量  
»» quote_qty | string | 报价币种下单数量  
»» price | string | 订单价格。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» time_in_force | string | 时效策略（默认 GTC，枚举值：GTC / IOC / FOK / POC / RPI）  
»» executed_qty | string | 已成交基础货币数量  
»» executed_amount | string | 已成交报价币种金额。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» executed_avg_price | string | 已成交均价。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» fee_coin | string | 手续费币种  
»» fee | string | 手续费金额  
»» reduce_only | string | 是否仅减仓订单（"true" 或 "false"）  
»» leverage | string | 订单杠杆倍数  
»» reason | string | 失败原因描述  
»» last_executed_qty | string | 最新一次成交数量  
»» last_executed_price | string | 最新一次成交价格。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» last_executed_amount | string | 最新一次成交金额。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
»» position_side | string | 仓位方向（NONE 单向持仓 / LONG 多仓 / SHORT 空仓）  
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
»» margin_mode | string | 保证金模式（CROSS/ISOLATED）  
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
        "update_time": "1750941402661",
        "margin_mode": "CROSS"
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
»» interest | string | 仓位累计利息  
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
from | 请求参数 | integer | 否 | 起始毫秒时间戳  
to | 请求参数 | integer | 否 | 终止毫秒时间戳  
page | 请求参数 | integer | 否 | 列表页数  
limit | 请求参数 | integer | 否 | 列表返回的最大数量，最大1000  
exchange_type | 请求参数 | string | 否 | 交易所  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» CrossexMarginInterestRecord | object |   
»» user_id | string | 用户Id  
»» symbol | string | 币对  
»» interest_id | string | 扣息Id  
»» liability_id | string | 负债源Id,可以是挂单Id 或者仓位Id  
»» liability | string | 负债数量  
»» liability_coin | string | 负债币种  
»» interest | string | 利息  
»» interest_rate | string | 利率  
»» interest_type | string | 扣息类型  
`PERIODIC_POSITION`: 整点仓位收息  
`PERIODIC_OPEN_ORDER`: 整点挂单收息  
`IMMEDIATE_OPEN_ORDER`: 开单收息  
`PERIODIC_ISOLATED`: 整点负债收息  
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
        "exchange_type": "OKX"
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
»» price | string | 成交价格。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
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
        "position_mode": "DUAL",
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
statement_type | 请求参数 | string | 否 | 账单流水类型。过滤同返回数据  
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
»» business_id | string | 业务ID。不同的 `statement_type` 时会有不同的含义。  
TRANSACTION: 对应订单 ID  
TRADING_FEE: 对应订单 ID  
LIQUIDATION_FEE: 对应强平订单 ID  
FUNDING_FEE: 对应仓位 ID 和资金费结算时间  
其他类型的为系统处理 ID，不作任何含义  
»» statement_type | string | 账单流水类型  
`TRANSACTION` 成交  
`TRADING_FEE` 手续费  
`FUNDING_FEE` 合约资金费  
`LIQUIDATION_FEE` 强平费  
`TRANSFER_IN` 资金转入  
`TRANSFER_OUT` 资金转出  
`BANKRUPT_COMPENSATION` 穿仓补贴  
`AUTO_REPAY` 杠杆仓位自动还负债  
`INTEREST_ISOLATED` 利息流水  
`ACCOUNT_MODE_CHANGE` 账户模式切换资金变动流水  
`KRAKEN_CONVERSION` KRAKEN_USD负余额用其他保证金币种兑换  
`SECURITY_DIVIDEND` 股票或ETF分红派息  
`SECURITY_CORPORATE_ACTION` 股票或ETF拆合股  
`OTHER` 其他  
»» exchange_type | string | 交易所  
»» coin | string | 币种  
»» symbol | string | 币对  
»» change | string | 变更金额（正数表示增加，负数表示减少）  
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
        "statement_type": "FUNDING_FEE",
        "exchange_type": "BINANCE",
        "coin": "USDT",
        "symbol": "BINANCE_FUTURE_BTC_USDT",
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
exchange_type | 请求参数 | string | 否 | OKX/GATE/BINANCE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT/LIGHTER  
  
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
    

##  获取交易所ticker🔒 需要认证

GET`/crossex/market/tickers`

GET `/crossex/market/tickers`

_获取交易所ticker_

限频：每1秒1次请求

  * 无法直接传杠杆币对作为参数, 例如`GATE_MARGIN_BTC_USDT`是无效参数

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 否 | 币对列表，多个以逗号分隔  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» symbol | string | 币对  
» last_price | string | 最新价  
» open_24h | string | 24小时开盘价  
» low_24h | string | 24小时最低价  
» high_24h | string | 24小时最高价  
» volume_24h_base | string | 最近24小时成交量，以基础货币为单位  
» volume_24h_quote | string | 最近24小时成交量，以计价货币为单位  
» mark_price | string | 标记价格  
» index_price | string | 指数价格  
» open_interest | string | 总持仓量  
» open_interest_quote | string | 总持仓量(计价币种)  
» timestamp | string | 更新时间戳  
  
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
    
    url = '/crossex/market/tickers'
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
    url="/crossex/market/tickers"
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
        "symbol": "GATE_FUTURE_BTC_USDT",
        "last_price": "64052.4",
        "open_24h": "65144.7",
        "low_24h": "64375",
        "high_24h": "65734.8",
        "volume_24h_base": "31705",
        "volume_24h_quote": "2063128626",
        "mark_price": "65148.9",
        "index_price": "65174.38",
        "open_interest": "65568.2144",
        "open_interest_quote": "4271697043.12416",
        "timestamp": "1785168000000"
      },
      {
        "symbol": "GATE_SPOT_BTC_USDT",
        "last_price": "65179.4",
        "open_24h": "",
        "low_24h": "65744",
        "high_24h": "64410.9",
        "volume_24h_base": "3480.769758",
        "volume_24h_quote": "226794942.82361",
        "mark_price": "",
        "index_price": "",
        "open_interest": "",
        "open_interest_quote": "",
        "timestamp": "1785168000000"
      }
    ]
    

##  获取交易所合约资金费率信息🔒 需要认证

GET`/crossex/market/funding_info`

GET `/crossex/market/funding_info`

_获取交易所合约资金费率信息_

限频：每1秒1次请求

  * 针对`Deribit`, `funding_rate`是按8小时周期计算的当前实时利率

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
symbols | 请求参数 | string | 否 | 币对列表，多个以逗号分隔  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### 返回格式

状态码 **200**

名称 | 类型 | 描述  
---|---|---  
» symbol | string | 币种  
» funding_rate | string | 资金费率  
» funding_interval | string | 资金费间隔时间(单位为秒)  
» funding_time | string | 下次资金费率时间(毫秒时间戳)  
  
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
    
    url = '/crossex/market/funding_info'
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
    url="/crossex/market/funding_info"
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
        "symbol": "BINANCE_FUTURE_BTC_USDT",
        "funding_rate": "0.00006537",
        "funding_time": "1785168000000",
        "funding_interval": "28800"
      },
      {
        "symbol": "OKX_FUTURE_BTC_USDT",
        "funding_rate": "0.0000543885374247",
        "funding_time": "1785168000000",
        "funding_interval": "28800"
      },
      {
        "symbol": "KRAKEN_FUTURE_BTC_USD",
        "funding_rate": "0.000011898754310345",
        "funding_time": "1785139200000",
        "funding_interval": "3600"
      },
      {
        "symbol": "GATE_FUTURE_BTC_USDT",
        "funding_rate": "0.0001",
        "funding_time": "1785168000000",
        "funding_interval": "28800"
      },
      {
        "symbol": "BYBIT_FUTURE_BTC_USDT",
        "funding_rate": "0.00008708",
        "funding_time": "1785168000000",
        "funding_interval": "28800"
      }
    ]
    

#  模型

##  Symbol

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | 交易对唯一标识，格式为 ExchangeType_BusinessType_Base_Counter。  
股票及ETF使用市场作为ExchangeType（US/HK/KR/JP），业务类型为STOCK或ETF，例如US_STOCK_AAPL_USDT、HK_STOCK_00700_USDT、US_ETF_SPY_USDT。  
exchange_type | string | true | none | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER）；股票及ETF返回上市市场（US / HK / KR / JP）  
business_type | string | true | none | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆 / STOCK 股票 / ETF 交易所交易基金）  
state | string | true | none | 状态（live 在线 / suspend 暂停）  
min_size | string | true | none | 最小下单数量  
min_notional | string | true | none | 最小下单价值  
lot_size | string | true | none | 数量步长  
tick_size | string | true | none | 价格步长  
max_num_orders | string | true | none | 最大挂单数量  
max_market_size | string | true | none | 市价单最大下单数量  
max_limit_size | string | true | none | 限价单最大下单数量  
contract_size | string | true | none | 合约乘数（已废弃，统一是量）  
liquidation_fee | string | true | none | 清算费率  
default_leverage | string | false | none | 默认杠杆倍数  
delist_time | string | true | none | 毫秒时间戳，0 表示正常未下架  
support_rpi | string | false | none | 是否支持rpi下单(true支持,false不支持)  
support_cross | string | false | none | 是否支持全仓下单(true支持,false不支持)  
tag | string | true | none | 标签信息。Hyperliquid返回DEX信息；股票及ETF返回证券描述；其他业务返回空字符串  
      
    
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
      "default_leverage": "string",
      "delist_time": "string",
      "support_rpi": "string",
      "support_cross": "string",
      "tag": "string"
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
CANCELLED: 订单被取消  
symbol | string | true | none | 交易对唯一标识，示例：  
BINANCE_SPOT_BTC_USDT、BINANCE_FUTURE_BTC_USDT  
side | string | true | none | 方向（BUY 买入 / SELL 卖出）  
type | string | true | none | 订单类型（LIMIT 限价 / MARKET 市价）  
attribute | string | true | none | 订单属性（COMMON 普通单 / LIQ 强平接管单 / REDUCE 强平减仓单 / ADL 自动减仓 / SETTLEMENT 下架清算）  
exchange_type | string | true | none | 交易所类型（BINANCE / OKX / GATE / BYBIT / KRAKEN / HYPERLIQUID / DERIBIT / LIGHTER）；股票及ETF返回上市市场（US / HK / KR / JP）  
business_type | string | true | none | 业务类型（SPOT 现货 / FUTURE 合约 / MARGIN 杠杆 / CONVERT 闪兑 / STOCK 股票 / ETF 交易所交易基金）  
qty | string | true | none | 基础货币下单数量  
quote_qty | string | true | none | 报价币种下单数量  
price | string | true | none | 订单价格。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
time_in_force | string | true | none | 时效策略（默认 GTC，枚举值：GTC / IOC / FOK / POC / RPI）  
executed_qty | string | true | none | 已成交基础货币数量  
executed_amount | string | true | none | 已成交报价币种金额。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
executed_avg_price | string | true | none | 已成交均价。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
fee_coin | string | true | none | 手续费币种  
fee | string | true | none | 手续费金额  
reduce_only | string | true | none | 是否仅减仓订单（"true" 或 "false"）  
leverage | string | true | none | 订单杠杆倍数  
reason | string | true | none | 失败原因描述  
last_executed_qty | string | true | none | 最新一次成交数量  
last_executed_price | string | true | none | 最新一次成交价格。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
last_executed_amount | string | true | none | 最新一次成交金额。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
position_side | string | true | none | 仓位方向（NONE 单向持仓 / LONG 多仓 / SHORT 空仓）  
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
    
    

##  CrossexBatchCancelOrderRequest

_CrossexBatchCancelOrderRequest_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | false | none | 订单 ID，与 text 必传其一  
text | string | false | none | 用户创建订单时指定的自定义 ID，与 order_id 必传其一  
  
_anyOf_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
  
_or_

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
_None_ | object | false | none | none  
      
    
    {}
    
    

##  CrossexBatchCancelOrderResponse

_CrossexBatchCancelOrderResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
order_id | string | true | none | 订单 ID  
text | string | true | none | 用户创建订单时指定的自定义 ID  
accepted | string | true | none | 是否受理成功，字符串 true 或 false  
label | string | true | none | 受理失败时的错误标识，成功时为空  
message | string | true | none | 受理失败时的错误信息，成功时为空  
      
    
    {
      "order_id": "string",
      "text": "string",
      "accepted": "string",
      "label": "string",
      "message": "string"
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
    
    

##  CrossexMarginModeResponse

_CrossexMarginModeResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | 合约交易币对  
margin_mode | string | true | none | 保证金模式（CROSS/ISOLATED）  
      
    
    {
      "symbol": "string",
      "margin_mode": "string"
    }
    
    

##  CrossexIsolatedMarginResponse

_CrossexIsolatedMarginResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | 合约交易币对  
margin | string | true | none | 本次增加或减少的逐仓保证金  
position_side | string | false | none | 仓位方向（NONE/LONG/SHORT），单向持仓不传时默认为NONE  
      
    
    {
      "symbol": "string",
      "margin": "string",
      "position_side": "string"
    }
    
    

##  CrossexTransferRequest

_资金划转请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
coin | string | true | none | 币种  
amount | string | true | none | 转账数量  
from | string | true | none | 转出账户: CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX_HYPERLIQUID, CROSSEX_DERIBIT, CROSSEX_LIGHTER, CROSSEX, SPOT  
to | string | true | none | 转入账户: CROSSEX_BINANCE, CROSSEX_OKX, CROSSEX_GATE, CROSSEX_BYBIT, CROSSEX_KRAKEN, CROSSEX_HYPERLIQUID, CROSSEX_DERIBIT, CROSSEX_LIGHTER, CROSSEX, SPOT  
text | string | false | none | 用户自定义id  
      
    
    {
      "coin": "string",
      "amount": "string",
      "from": "string",
      "to": "string",
      "text": "string"
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
如果您想在KRAKEN交易所上为ADA/USD交易对下合约订单，您可以使用这样的唯一标识符：`KRAKEN_FUTURE_ADA_USD`;  
如果您想在HYPERLIQUID交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`HYPERLIQUID_FUTURE_ADA_USDC`;  
如果您想在DERIBIT交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`DERIBIT_FUTURE_ADA_USDC`;  
如果您想在LIGHTER交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`LIGHTER_FUTURE_ADA_USDC`;  
如果您想交易美股AAPL，可以使用这样的唯一标识符：`US_STOCK_AAPL_USDT`;  
如果您想交易港股00700，可以使用这样的唯一标识符：`HK_STOCK_00700_USDT`;  
如果您想交易美股ETF SPY，可以使用这样的唯一标识符：`US_ETF_SPY_USDT`;  
目前支持现货订单、U本位永续合约订单、现货杠杆订单、股票订单和ETF订单。BYBIT/DERIBIT暂不支持现货杠杆订单，KRAKEN、HYPERLIQUID、LIGHTER暂不支持现货与杠杆订单；股票及ETF仅支持跨所账户模式  
side | string | true | none | BUY, SELL  
type | string | false | none | 订单类型（默认`LIMIT`，支持类型列举：`LIMIT`、`MARKET`）  
time_in_force | string | false | none | 默认GTC，支持类型枚举，`GTC`，`IOC`，`FOK`，`POC`, `RPI`  
`GTC`: GoodTillCancelled  
`IOC`: ImmediateOrCancelled  
`FOK`: FillOrKill  
`POC`: PendingOrCancelled or PostOnly  
`RPI`: RPI  
股票及ETF仅支持`GTC`  
qty | string | false | none | 订单数量（强制性，除非现货和杠杆市价买入；股票及ETF必须传qty）  
price | string | false | none | 限价订单价格（限价订单必须）。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）  
quote_qty | string | false | none | 订单报价数量，现货和杠杆市价买单必传；股票及ETF不支持quote_qty下单  
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
time_in_force | RPI  
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
    
    

##  CrossexConvertQuoteRequest

_闪兑询价请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
exchange_type | string | true | none | 交易所类型  
目前仅支持 BINANCE, OKX, GATE, BYBIT, HYPERLIQUID, KRAKEN, LIGHTER  
from_coin | string | true | none | 卖出的资产  
to_coin | string | true | none | 买入的资产名称  
OKX, GATE 只允许兑换成BTC, ETH, USDT  
BYBIT, BINANCE 只允许兑换成USDT  
HYPERLIQUID 只允许兑换成USDT, USDC  
KRAKEN 只允许兑换成USDT  
LIGHTER 只允许USDT与USDC互兑  
from_amount | string | true | none | 卖出的资产数量  
      
    
    {
      "exchange_type": "string",
      "from_coin": "string",
      "to_coin": "string",
      "from_amount": "string"
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
    
    

##  CrossexAccountUpdateRequest

_更改账户请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
position_mode | string | false | none | 合约仓位模式（SINGLE/DUAL）  
account_mode | string | false | none | 账户模式（CROSS_EXCHANGE/ISOLATED_EXCHANGE，默认：CROSS_EXCHANGE）  
exchange_type | string | false | none | 交易所（BINANCE/OKX/GATE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT/LIGHTER/CROSSEX，当账户模式为ISOLATED_EXCHANGE时，修改合约仓位模式必须指定交易所）  
      
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
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
    
    

##  CrossexMarginModeRequest

_修改合约仓位保证金模式请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | Hyperliquid合约交易币对  
margin_mode | string | true | none | 保证金模式（CROSS/ISOLATED）  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
margin_mode | CROSS  
margin_mode | ISOLATED  
      
    
    {
      "symbol": "string",
      "margin_mode": "CROSS"
    }
    
    

##  CrossexIsolatedMarginRequest

_增加或减少逐仓保证金请求体_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
symbol | string | true | none | Hyperliquid合约交易币对  
margin | string | true | none | 保证金调整金额，正数为增加，负数为减少，超过两位小数时向下截断  
position_side | string | false | none | 仓位方向（NONE/LONG/SHORT），单向持仓不传时默认为NONE  
  
####  枚举值列表

枚举值列表属性 | 值  
---|---  
position_side | NONE  
position_side | LONG  
position_side | SHORT  
      
    
    {
      "symbol": "string",
      "margin": "string",
      "position_side": "NONE"
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
price | string | true | none | 报价价格  
      
    
    {
      "quote_id": "string",
      "valid_ms": "string",
      "from_coin": "string",
      "to_coin": "string",
      "from_amount": "string",
      "to_amount": "string",
      "price": "string"
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
»» equity | string | false | none | 币种的保证金净资产权益  
»» futures_initial_margin | string | false | none | 币种的合约初始保证金, 合约结算币种（USDT/USDC/USD）会有此值  
»» futures_maintenance_margin | string | false | none | 币种的合约维持保证金, 合约结算币种（USDT/USDC/USD）会有此值  
»» borrowing_initial_margin | string | true | none | 币种的杠杆交易初始保证金, 杠杆/合约结算币种（USDT/USDC/USD）会有此值  
»» borrowing_maintenance_margin | string | true | none | 币种的杠杆交易维持保证金, 杠杆/合约结算币种（USDT/USDC/USD）会有此值  
»» available_balance | string | false | none | 可用余额  
»» liability | string | false | none | 币种负债, 仅（USDT/USDC/USD）会有值  
      
    
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
    
    

##  CrossexAccountUpdateResponse

_CrossexAccountUpdateResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
position_mode | string | false | none | 请求修改的合约仓位模式（SINGLE/DUAL）  
account_mode | string | false | none | 请求修改的账户模式（CROSS_EXCHANGE/ISOLATED_EXCHANGE，默认：CROSS_EXCHANGE）  
exchange_type | string | false | none | 请求修改的交易所（BINANCE/OKX/GATE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT/LIGHTER/CROSSEX，当账户模式为ISOLATED_EXCHANGE时，修改合约仓位模式必须指定交易所）  
      
    
    {
      "position_mode": "string",
      "account_mode": "string",
      "exchange_type": "string"
    }
    
    

Last Updated: 10/12/2026, 12:27:31 PM