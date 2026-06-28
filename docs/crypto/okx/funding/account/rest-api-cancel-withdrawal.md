---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-cancel-withdrawal
anchor_id: funding-account-rest-api-cancel-withdrawal
api_type: REST
updated_at: 2026-06-28 19:38:17.433625
---

# Cancel withdrawal

You can cancel normal withdrawal requests, but you cannot cancel withdrawal requests on Lightning.  
  
#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/asset/cancel-withdrawal`

> Request Example
    
    
    POST /api/v5/asset/cancel-withdrawal
    body {
       "wdId":"1123456"
    }
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel withdrawal
    result = fundingAPI.cancel_withdrawal(
        wdId="123456"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
wdId | String | Yes | Withdrawal ID  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "wdId": "1123456"   
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
wdId | String | Withdrawal ID  
If the code is equal to 0, it cannot be strictly considered that the withdrawal has been revoked. It only means that your request is accepted by the server. The actual result is subject to the status in the withdrawal history.

---

# 撤销提币

可以撤销普通提币，但不支持撤销闪电网络上的提币。  
  
#### 限速：6次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/asset/cancel-withdrawal`

> 请求示例
    
    
    POST /api/v5/asset/cancel-withdrawal
    body {
       "wdId":"1123456"
    }
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 撤销提币
    result = fundingAPI.cancel_withdrawal(
        wdId="123456"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
wdId | String | 是 | 提币申请ID  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "wdId": "1123456"   
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
wdId | String | 提币申请ID  
接口返回code等于0不能严格认为提币已经被撤销，只表示您的请求被系统服务器所接受，实际结果以获取提币记录中的状态为准。