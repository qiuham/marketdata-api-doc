---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-lead-trader-ranks
anchor_id: order-book-trading-copy-trading-get-lead-trader-ranks
api_type: API
updated_at: 2026-07-05 19:34:13.020075
---

# GET / Lead trader ranks

Public endpoint. Retrieve lead trader ranks.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/public-lead-traders`

> Request example
    
    
    GET /api/v5/copytrading/public-lead-traders?instType=SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
sortType | String | No | Sort type  
`overview`: overview, the default value  
`pnl`: profit and loss  
`aum`: assets under management  
`win_ratio`: win ratio  
`pnl_ratio`: pnl ratio  
`current_copy_trader_pnl`: current copy trader pnl  
state | String | No | Lead trader state  
`0`: All lead traders, the default, including vacancy and non-vacancy   
`1`: lead traders who have vacancy  
minLeadDays | String | No | Minimum lead days  
`1`: 7 days  
`2`: 30 days  
`3`: 90 days  
`4`: 180 days  
minAssets | String | No | Minimum assets in USDT  
maxAssets | String | No | Maximum assets in USDT  
minAum | String | No | Minimum assets in USDT under management.  
maxAum | String | No | Maximum assets in USDT under management.  
dataVer | String | No | Data version. It is 14 numbers. e.g. 20231010182400. Generally, it is used for pagination   
A new version will be generated every 10 minutes. Only last 5 versions are stored  
The default is latest version. If it is not exist, error will not be throwed and the latest version will be used.  
page | String | No | Page for pagination  
limit | String | No | Number of results per request. The maximum is 20; the default is 10  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "dataVer": "20231129213200",
                "ranks": [
                    {
                        "accCopyTraderNum": "3536",
                        "aum": "1509265.3238761567721365",
                        "ccy": "USDT",
                        "copyState": "0",
                        "copyTraderNum": "999",
                        "leadDays": "156",
                        "maxCopyTraderNum": "1000",
                        "nickName": "Crypto to the moon",
                        "pnl": "48805.1105999999972258",
                        "pnlRatio": "1.6898",
                        "pnlRatios": [
                            {
                                "beginTs": "1701187200000",
                                "pnlRatio": "1.6744"
                            },
                            {
                                "beginTs": "1700755200000",
                                "pnlRatio": "1.649"
                            }
                        ],
                        "portLink": "https://static.okx.com/cdn/okex/users/headimages/20230624/f49a683aaf5949ea88b01bbc771fb9fc",
                        "traderInsts": [
                            "ICP-USDT-SWAP",
                            "MINA-USDT-SWAP"
    
                        ],
                        "uniqueCode": "540D011FDACCB47A",
                        "winRatio": "0.6957"
                    }
                ],
                "totalPage": "1"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
dataVer | String | Data version  
totalPage | String | Total number of pages  
ranks | Array of objects | The rank information of lead traders  
> aum | String | assets under management  
> copyState | String | Current copy state   
`0`: non-copy, `1`: copy  
> maxCopyTraderNum | String | Maximum number of copy traders  
> copyTraderNum | String | Current number of copy traders  
> accCopyTraderNum | String | Accumulated number of copy traders  
> portLink | String | Portrait link  
> nickName | String | Nick name  
> ccy | String | Margin currency  
> uniqueCode | String | Lead trader unique code  
> winRatio | String | Win ratio, 0.1 represents 10%  
> leadDays | String | Lead days  
> traderInsts | Array of strings | Contract list which lead trader is leading  
> pnl | String | Pnl (in USDT) of last 90 days.  
> pnlRatio | String | Pnl ratio of last 90 days. 0.1 represents 10%  
> pnlRatios | Array of objects | Pnl ratios  
>> beginTs | String | Begin time of pnl ratio on that day  
>> pnlRatio | String | Pnl ratio on that day

---

# GET / 获取交易员排名

公共接口，获取交易员排名信息。  
  
#### 限速：5次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/public-lead-traders`

> 请求示例
    
    
    GET /api/v5/copytrading/public-lead-traders?instType=SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
sortType | String | 否 | 排名类型  
`overview`: 综合排序，默认值  
`pnl`: 按照交易员收益额排序  
`aum`: 按照带单规模排序  
`win_ratio`: 胜率  
`pnl_ratio`: 收益率  
`current_copy_trader_pnl`: 当前跟单人的收益额  
state | String | 否 | 交易员的状态  
`0`: 所有交易员，默认值，包括有空缺和没有空缺   
`1`: 有空缺的交易员  
minLeadDays | String | 否 | 最短带单时长  
`1`: 7 天  
`2`: 30 天  
`3`: 90 天  
`4`: 180天  
minAssets | String | 否 | 交易员资产范围的最小值，单位为 USDT  
maxAssets | String | 否 | 交易员资产范围的最大值，单位为 USDT  
minAum | String | 否 | 带单规模的最小值，单位为 USDT  
maxAum | String | 否 | 带单规模的最大值，单位为 USDT  
dataVer | String | 否 | 排名数据的版本，14 位数字，如：20231010182400，主要在分页时使用   
每10分钟生成一版，仅保留最新的5个版本  
默认使用最近的版本；不存在时不会报错，会使用最近的版本。  
page | String | 否 | 查询页数  
limit | String | 否 | 分页返回的结果集数量，最大为 20，不填默认返回 10 条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "dataVer": "20231129213200",
                "ranks": [
                    {
                        "accCopyTraderNum": "3536",
                        "aum": "1509265.3238761567721365",
                        "ccy": "USDT",
                        "copyState": "0",
                        "copyTraderNum": "999",
                        "leadDays": "156",
                        "maxCopyTraderNum": "1000",
                        "nickName": "Crypto to the moon",
                        "pnl": "48805.1105999999972258",
                        "pnlRatio": "1.6898",
                        "pnlRatios": [
                            {
                                "beginTs": "1701187200000",
                                "pnlRatio": "1.6744"
                            },
                            {
                                "beginTs": "1700755200000",
                                "pnlRatio": "1.649"
                            }
                        ],
                        "portLink": "https://static.okx.com/cdn/okex/users/headimages/20230624/f49a683aaf5949ea88b01bbc771fb9fc",
                        "traderInsts": [
                            "ICP-USDT-SWAP",
                            "MINA-USDT-SWAP"
    
                        ],
                        "uniqueCode": "540D011FDACCB47A",
                        "winRatio": "0.6957"
                    }
                ],
                "totalPage": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
dataVer | String | 排名数据的版本  
totalPage | String | 总的页数  
ranks | Array of objects | 交易员排名信息  
> aum | String | 带单规模，单位为USDT  
> copyState | String | 当前跟单状态   
`0`: 没在跟单  
`1`：在跟单  
> maxCopyTraderNum | String | 最大跟单人数  
> copyTraderNum | String | 跟单人数  
> accCopyTraderNum | String | 累计跟单人数  
> portLink | String | 头像  
> nickName | String | 昵称  
> ccy | String | 保证金币种  
> uniqueCode | String | 交易员唯一标识码  
> winRatio | String | 胜率，0.1 代表 10%  
> leadDays | String | 带单天数  
> traderInsts | Array of strings | 交易员带单的合约列表  
> pnl | String | 近90日交易员收益，单位为 USDT  
> pnlRatio | String | 近90日交易员收益率，0.1 代表 10%  
> pnlRatios | Array of objects | 收益率数据  
>> beginTs | String | 当天收益率的开始时间  
>> pnlRatio | String | 当天收益率