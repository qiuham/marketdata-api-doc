---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-counterparties
anchor_id: block-trading-rest-api-get-counterparties
api_type: REST
updated_at: 2026-07-15 19:19:30.679698
---

# Get Counterparties

Retrieves the list of counterparties that the user is permitted to trade with. 

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/counterparties`

> Request Example
    
    
    GET /api/v5/rfq/counterparties
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get counterparts
    result = blockTradingAPI.counterparties()
    print(result)
    

#### Request parameters

None

> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "traderName" : "Satoshi Nakamoto",
                "traderCode" : "SATOSHI",
                "type" : "" 
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
traderName | String | The long formative username of trader or entity on the platform.  
traderCode | String | A unique identifier of maker which will be publicly visible on the platform. All RFQ and Quote endpoints will use this as the unique counterparty identifier.  
type | String | The counterparty type. `LP` refers to API connected auto market makers.

---

# 获取报价方信息

查询可以参与交易的报价方信息。

#### 限速: 5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/rfq/counterparties`

> 请求示例
    
    
    GET /api/v5/rfq/counterparties
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取报价方信息
    result = blockTradingAPI.counterparties()
    print(result)
    

#### 请求参数

无

> 响应示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "traderName" : "Satoshi Nakamoto",
                "traderCode" : "SATOSHI",
                "type" : "" 
            }
        ]
    }
    

#### 响应参数

参数名 | 类型 | 描述  
---|---|---  
traderName | String | 报价方名称  
traderCode | String | 报价方唯一标识代码，公开可见；报价和询价的相关接口都使用该代码代表报价方。  
type | String | 报价方类型。`LP`指通过API连接的自动做市商。