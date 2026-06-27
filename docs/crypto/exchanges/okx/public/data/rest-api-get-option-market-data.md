---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-option-market-data
anchor_id: public-data-rest-api-get-option-market-data
api_type: REST
updated_at: 2026-05-27 19:36:10.677127
---

# Get option market data

Retrieve option market data.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP + instFamily

#### HTTP Request

`GET /api/v5/public/opt-summary`

> Request Example
    
    
    GET /api/v5/public/opt-summary?uly=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve option market data
    result = publicDataAPI.get_opt_summary(
        uly="BTC-USD",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | Yes | Instrument family, only applicable to `OPTION`  
  
expTime | String | No | Contract expiry date, the format is "YYMMDD", e.g. "200527"  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "askVol": "3.7207056835937498",
                "bidVol": "0",
                "delta": "0.8310206676289528",
                "deltaBS": "0.9857332101544538",
                "fwdPx": "39016.8143629068452065",
                "gamma": "-1.1965483553276135",
                "gammaBS": "0.000011933182397798109",
                "instId": "BTC-USD-220309-33000-C",
                "instType": "OPTION",
                "lever": "0",
                "markVol": "1.5551965233045728",
                "realVol": "0",
                "volLv": "0",
                "theta": "-0.0014131955002093717",
                "thetaBS": "-66.03526900575946",
                "ts": "1646733631242",
                "uly": "BTC-USD",
                "vega": "0.000018173851073258973",
                "vegaBS": "0.7089307622132419"
            },
            {
                "askVol": "1.7968814062499998",
                "bidVol": "0",
                "delta": "-0.014668822072611904",
                "deltaBS": "-0.01426678984554619",
                "fwdPx": "39016.8143629068452065",
                "gamma": "0.49483062407551576",
                "gammaBS": "0.000011933182397798109",
                "instId": "BTC-USD-220309-33000-P",
                "instType": "OPTION",
                "lever": "0",
                "markVol": "1.5551965233045728",
                "realVol": "0",
                "volLv": "0",
                "theta": "-0.0014131955002093717",
                "thetaBS": "-54.93377294845015",
                "ts": "1646733631242",
                "uly": "BTC-USD",
                "vega": "0.000018173851073258973",
                "vegaBS": "0.7089307622132419"
            }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`OPTION`  
instId | String | Instrument ID, e.g. `BTC-USD-200103-5500-C`  
uly | String | Underlying  
delta | String | Sensitivity of option price to `uly` price  
gamma | String | The delta is sensitivity to `uly` price  
vega | String | Sensitivity of option price to implied volatility  
theta | String | Sensitivity of option price to remaining maturity  
deltaBS | String | Sensitivity of option price to `uly` price in BS mode  
gammaBS | String | The delta is sensitivity to `uly` price in BS mode  
vegaBS | String | Sensitivity of option price to implied volatility in BS mode  
thetaBS | String | Sensitivity of option price to remaining maturity in BS mode  
lever | String | Leverage  
markVol | String | Mark volatility  
bidVol | String | Bid volatility  
askVol | String | Ask volatility  
realVol | String | Realized volatility (not currently used)  
volLv | String | Implied volatility of at-the-money options  
fwdPx | String | Forward price  
ts | String | Data update time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取期权定价

查询期权详细信息  
  
#### 限速：20次/2s

#### 限速规则：IP + instFamily

#### HTTP请求

`GET /api/v5/public/opt-summary`

> 请求示例
    
    
    GET /api/v5/public/opt-summary?uly=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取期权定价
    result = publicDataAPI.get_opt_summary(
        uly="BTC-USD",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 是 | 交易品种，仅适用于期权  
expTime | String | 否 | 合约到期日，格式为"YYMMDD"，如 "200527"  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
          {
                "askVol": "3.7207056835937498",
                "bidVol": "0",
                "delta": "0.8310206676289528",
                "deltaBS": "0.9857332101544538",
                "fwdPx": "39016.8143629068452065",
                "gamma": "-1.1965483553276135",
                "gammaBS": "0.000011933182397798109",
                "instId": "BTC-USD-220309-33000-C",
                "instType": "OPTION",
                "lever": "0",
                "markVol": "1.5551965233045728",
                "realVol": "0",
                "volLv": "0",
                "theta": "-0.0014131955002093717",
                "thetaBS": "-66.03526900575946",
                "ts": "1646733631242",
                "uly": "BTC-USD",
                "vega": "0.000018173851073258973",
                "vegaBS": "0.7089307622132419"
            },
            {
                "askVol": "1.7968814062499998",
                "bidVol": "0",
                "delta": "-0.014668822072611904",
                "deltaBS": "-0.01426678984554619",
                "fwdPx": "39016.8143629068452065",
                "gamma": "0.49483062407551576",
                "gammaBS": "0.000011933182397798109",
                "instId": "BTC-USD-220309-33000-P",
                "instType": "OPTION",
                "lever": "0",
                "markVol": "1.5551965233045728",
                "realVol": "0",
                "volLv": "0",
                "theta": "-0.0014131955002093717",
                "thetaBS": "-54.93377294845015",
                "ts": "1646733631242",
                "uly": "BTC-USD",
                "vega": "0.000018173851073258973",
                "vegaBS": "0.7089307622132419"
            }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`OPTION`：期权  
instId | String | 产品ID，如 `BTC-USD-200103-5500-C`  
uly | String | 标的指数  
delta | String | 期权价格对`uly`价格的敏感度  
gamma | String | delta对`uly`价格的敏感度  
vega | String | 期权价格对隐含波动率的敏感度  
theta | String | 期权价格对剩余期限的敏感度  
deltaBS | String | BS模式下期权价格对`uly`价格的敏感度  
gammaBS | String | BS模式下delta对`uly`价格的敏感度  
vegaBS | String | BS模式下期权价格对隐含波动率的敏感度  
thetaBS | String | BS模式下期权价格对剩余期限的敏感度  
lever | String | 杠杆倍数  
markVol | String | 标记波动率  
bidVol | String | bid波动率  
askVol | String | ask波动率  
realVol | String | 已实现波动率（目前该字段暂未启用）  
volLv | String | 平价期权的隐含波动率  
fwdPx | String | 远期价格  
ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`