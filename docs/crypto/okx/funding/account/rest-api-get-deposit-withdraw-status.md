---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-deposit-withdraw-status
anchor_id: funding-account-rest-api-get-deposit-withdraw-status
api_type: REST
updated_at: 2026-07-03 19:40:53.156050
---

# Get deposit withdraw status

Retrieve deposit's and withdrawal's detailed status and estimated complete time.  
  
#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/deposit-withdraw-status`

> Request Example
    
    
    # For deposit
    GET /api/v5/asset/deposit-withdraw-status?txId=xxxxxx&to=1672734730284&ccy=USDT&chain=USDT-ERC20
    
    # For withdrawal
    GET /api/v5/asset/deposit-withdraw-status?wdId=200045249
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
wdId | String | Conditional | Withdrawal ID, use to retrieve withdrawal status   
Required to input one and only one of `wdId` and `txId`  
txId | String | Conditional | Hash record of the deposit, use to retrieve deposit status   
Required to input one and only one of `wdId` and `txId`  
ccy | String | Conditional | Currency type, e.g. `USDT`   
Required when retrieving deposit status with `txId`  
to | String | Conditional | To address, the destination address in deposit   
Required when retrieving deposit status with `txId`  
chain | String | Conditional | Currency chain information, e.g. USDT-ERC20   
Required when retrieving deposit status with `txId`  
  
> Response Example
    
    
    {
        "code":"0",
        "data":[
            {
                "wdId": "200045249",
                "txId": "16f3638329xxxxxx42d988f97", 
                "state": "Pending withdrawal: Wallet is under maintenance, please wait.",
                "estCompleteTime": "01/09/2023, 8:10:48 PM"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
estCompleteTime | String | Estimated complete time  
The timezone is `UTC+8`. The format is MM/dd/yyyy, h:mm:ss AM/PM   
estCompleteTime is only an approximate estimated time, for reference only.  
state | String | The detailed stage and status of the deposit/withdrawal   
The message in front of the colon is the stage; the message after the colon is the ongoing status.  
txId | String | Hash record on-chain  
For withdrawal, if the `txId` has already been generated, it will return the value, otherwise, it will return "".  
wdId | String | Withdrawal ID  
When retrieving deposit status, wdId returns blank "".  
Stage References  
Deposit  
Stage 1: On-chain transaction detection   
Stage 2: Push deposit data to associated account   
Stage 3: Receiving account credit   
Final stage: Deposit complete  
Withdrawal  
Stage 1: Pending withdrawal   
Stage 2: Withdrawal in progress   
Final stage: Withdrawal complete / cancellation complete

---

# 获取充值/提现的详细状态

获取充值与提现的详细状态信息与预估完成时间。  
  
#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/deposit-withdraw-status`

> 请求示例
    
    
    # 查询充值
    GET /api/v5/asset/deposit-withdraw-status?txId=xxxxxx&to=1672734730284&ccy=USDT&chain=USDT-ERC20
    
    # 查询提现
    GET /api/v5/asset/deposit-withdraw-status?wdId=200045249
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
wdId | String | 可选 | 提币申请ID，用于查询资金提现  
`wdId`与`txId`必传其一也仅可传其一  
txId | String | 可选 | 区块转账哈希记录ID，用于查询资金充值  
`wdId`与`txId`必传其一也仅可传其一  
ccy | String | 可选 | 币种，如`USDT`  
查询充值时必填，需要与`txId`一并提供  
to | String | 可选 | 资金充值到账账户地址   
查询充值时必填，需要与`txId`一并提供  
chain | String | 可选 | 币种链信息，如 USDT-ERC20   
查询充值时必填，需要与`txId`一并提供  
  
> 返回结果
    
    
    {
        "code":"0",
        "data":[
            {
                "wdId": "200045249",
                "txId": "16f3638329xxxxxx42d988f97", 
                "state": "Pending withdrawal: Wallet is under maintenance, please wait.",
                "estCompleteTime": "01/09/2023, 8:10:48 PM"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
estCompleteTime | String | 预估完成时间  
时区为 UTC+8；格式为 MM/dd/yyyy, h:mm:ss AM/PM   
estCompleteTime仅为预估完成时间，仅供参考  
state | String | 充值/提现的现处于的详细阶段提示  
冒号前面代表阶段，后面代表状态  
txId | String | 区块转账哈希记录  
提币如果`txId`已经生成，则返回，否则返回""  
wdId | String | 提币申请ID  
如查询的是充值，该字段返回""  
阶段参考  
充值  
阶段一：监测链上交易  
阶段二：推送充值数据到入账环节  
阶段三：进行入账  
终态：充值已完成  
提现  
阶段一：等待提现  
阶段二：提现中  
终态：提现已完成 / 撤销已完成