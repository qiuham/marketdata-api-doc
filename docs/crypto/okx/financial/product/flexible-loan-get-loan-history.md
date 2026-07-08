---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan-get-loan-history
anchor_id: financial-product-flexible-loan-get-loan-history
api_type: API
updated_at: 2026-07-08 19:29:36.257169
---

# GET / Loan history

#### Rate Limit: 5 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-history`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/loan-history
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
type | String | No | Action type  
`borrowed`  
`repaid`  
`collateral_locked`  
`collateral_released`  
`forced_repayment_buy`  
`forced_repayment_sell`  
`forced_liquidation`  
`partial_liquidation`  
`sell_collateral`  
`buy_transition_coin`  
`sell_transition_coin`  
`buy_borrowed_coin`  
after | String | No | Pagination of data to return records earlier than the requested `refId`(not include)  
before | String | No | Pagination of data to return records newer than the requested `refId`(not include)  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will return data of all orders  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "-0.001",
                "ccy": "DOT",
                "refId": "17316594851045086",
                "ts": "1731659485000",
                "type": "collateral_locked"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
refId | String | Reference ID  
type | String | Action type  
ccy | String | Currency, e.g. `BTC`  
amt | String | Amount  
ts | String | Timestamp for the action, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 借贷历史

#### 限速：5次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/loan-history`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/loan-history
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 操作类型  
`borrowed`：借入  
`repaid`：还币  
`collateral_locked`：锁定质押物  
`collateral_released`：释放质押物  
`forced_repayment_buy`：自动换币买入  
`forced_repayment_sell`：自动换币卖出  
`forced_liquidation`：强制平仓  
`partial_liquidation`：强制减仓  
`sell_collateral`：卖出质押资产  
`buy_transition_coin`：购买中介币种  
`sell_transition_coin`：卖出中介币种  
`buy_borrowed_coin`：购买借币币种  
after | String | 否 | 请求此 ID 之前（更旧的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
before | String | 否 | 请求此 ID 之后（更新的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
limit | String | 否 | 返回结果的数量，最大为`100`，默认`100`条  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将返回所有订单数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "-0.001",
                "ccy": "DOT",
                "refId": "17316594851045086",
                "ts": "1731659485000",
                "type": "collateral_locked"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
refId | String | 对应记录ID  
type | String | 操作类型  
ccy | String | 币种，如 `BTC`  
amt | String | 数量  
ts | String | 操作发生时间，Unix 时间戳为毫秒数格式，如 `1597026383085`