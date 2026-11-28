---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-c-get-glp-c-eligible-instruments
anchor_id: global-liquidity-program-glp-c-get-glp-c-eligible-instruments
api_type: API
updated_at: 2026-11-28 18:57:22.945878
---

# Get GLP-C eligible instruments

Retrieve GLP-C instruments eligible for the current account, with registration counts and qualification requirements.  
  
#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/instruments`

> Request Example
    
    
    GET /api/v5/users/glp-c/instruments?instType=SPOT&page=1&pageSize=10&filterType=1
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`: Spot  
`PERP`: Perpetual  
page | Integer | Yes | Page number, starting from `1`  
pageSize | Integer | Yes | Number of results per page. The maximum is `100`  
filterType | Integer | Yes | `1`: All eligible instruments  
`2`: Registered  
`3`: Open for registration  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "page": 1,
            "pageSize": 10,
            "total": 1,
            "startIndex": 0,
            "hasNextPage": false,
            "rows": [
                {
                    "instType": "SPOT",
                    "instId": "BTC-USDT",
                    "instGroup": "G1",
                    "registeredClientCount": 0,
                    "dailyAvgPlatTv7d": "0",
                    "b3PriceLevel": "5",
                    "b3PriceQuoteSize": "25",
                    "requiredMarketShare": "0.05",
                    "requiredUptime": "0.7"
                }
            ]
        }
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
page | Integer | Current page number  
pageSize | Integer | Number of results per page  
total | Integer | Total number of results before pagination  
startIndex | Integer | Zero-based offset of the current page: (page − 1) × pageSize  
hasNextPage | Boolean | Whether there is a next page  
rows | Array of objects | Instrument list. `[]` if there are no results  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> instGroup | String | Instrument group  
`G1`  
`G2`  
`G3`  
> registeredClientCount | Integer | Number of clients registered for the instrument  
> dailyAvgPlatTv7d | String | 7-day daily average platform trading volume  
> b3PriceLevel | String | Average spread between the third-best ask and bid over the past 7 days, calculated as (ask₃ − bid₃) ÷ their midpoint × 10,000, in bp. Lower values indicate a tighter order book.  
> b3PriceQuoteSize | String | Average combined bid and ask quote size across order book levels 1–3 over the past 7 days, in USD. For example, `25` means 25 USD.  
> requiredMarketShare | String | Required minute market share. e.g. `0.05` means 5%.  
> requiredUptime | String | Required hourly uptime. e.g. `0.7` means 70%  
Only instruments tradable by the current account are returned.

---

# 获取 GLP-C 可参与产品

获取当前账户可参与 GLP-C 的产品，包括注册数量及达标要求。  
  
#### 限速：5次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp-c/instruments`

> 请求示例
    
    
    GET /api/v5/users/glp-c/instruments?instType=SPOT&page=1&pageSize=10&filterType=1
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：现货  
`PERP`：永续合约  
page | Integer | 是 | 页码，从 `1` 开始  
pageSize | Integer | 是 | 每页返回的结果数量，最大为 `100`  
filterType | Integer | 是 | `1`：全部可参与产品  
`2`：已注册  
`3`：可注册  
instId | String | 否 | 产品 ID，如 `BTC-USDT`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "page": 1,
            "pageSize": 10,
            "total": 1,
            "startIndex": 0,
            "hasNextPage": false,
            "rows": [
                {
                    "instType": "SPOT",
                    "instId": "BTC-USDT",
                    "instGroup": "G1",
                    "registeredClientCount": 0,
                    "dailyAvgPlatTv7d": "0",
                    "b3PriceLevel": "5",
                    "b3PriceQuoteSize": "25",
                    "requiredMarketShare": "0.05",
                    "requiredUptime": "0.7"
                }
            ]
        }
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
page | Integer | 当前页码  
pageSize | Integer | 每页返回的结果数量  
total | Integer | 分页前的结果总数  
startIndex | Integer | 当前页的起始偏移量（从 0 开始）：(page − 1) × pageSize  
hasNextPage | Boolean | 是否有下一页  
rows | Array of objects | 产品列表。无结果时返回 `[]`  
> instType | String | 产品类型  
> instId | String | 产品 ID  
> instGroup | String | 产品分组  
`G1`  
`G2`  
`G3`  
> registeredClientCount | Integer | 已注册该产品的客户数量  
> dailyAvgPlatTv7d | String | 平台近 7 日日均交易量  
> b3PriceLevel | String | 过去 7 天第三档卖价与买价之间价差的平均值，计算公式为（ask₃ − bid₃）÷ 两者中间价 × 10,000，单位为 bp。数值越低表示订单簿价差越小。  
> b3PriceQuoteSize | String | 过去 7 天订单簿买卖两侧第 1–3 档合计报价量的平均值，单位为 USD。例如，`25` 表示 25 USD。  
> requiredMarketShare | String | 要求的分钟市场份额，如 `0.05` 表示 5%。  
> requiredUptime | String | 要求的小时在线率。如 `0.7` 表示 70%  
仅返回当前账户可交易的产品。