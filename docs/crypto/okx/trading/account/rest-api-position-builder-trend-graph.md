---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-position-builder-trend-graph
anchor_id: trading-account-rest-api-position-builder-trend-graph
api_type: REST
updated_at: 2026-05-27 19:34:34.268611
---

# Position builder trend graph

#### Rate limit: 1 request per 5 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`POST /api/v5/account/position-builder-graph`

> Request Example
    
    
    {
       "inclRealPosAndEq":false,
       "simPos":[
          {
             "pos":"-10",
             "instId":"BTC-USDT-SWAP",
             "avgPx":"100000"
          },
          {
             "pos":"10",
             "instId":"LTC-USDT-SWAP",
             "avgPx":"8000"
          }
       ],
       "simAsset":[
          {
             "ccy":"USDT",
             "amt":"100"
          }
       ],
       "greeksType":"CASH",
       "type":"mmr",
       "mmrConfig":{
          "acctLv":"3",
          "lever":"1"
       }
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
inclRealPosAndEq | Boolean | No | Whether to import existing positions and assets  
The default is `true`  
simPos | Array of objects | No | List of simulated positions  
> instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
Applicable to `SWAP`/`FUTURES`/`OPTION`  
> pos | String | Yes | Quantity of positions  
> avgPx | String | Yes | Average open price  
> lever | String | No | leverage  
Only applicable to `Multi-currency margin`  
The default is `1`  
If the allowed leverage is exceeded, set according to the maximum leverage.  
simAsset | Array of objects | No | List of simulated assets  
When `inclRealPosAndEq` is `true`, only real assets are considered and virtual assets are ignored  
> ccy | String | Yes | Currency, e.g. `BTC`  
> amt | String | Yes | Currency amount  
type | String | Yes | Trending graph type  
`mmr`  
mmrConfig | Object | Yes | MMR configuration  
> acctLv | String | No | Switch to account mode  
`3`: Multi-currency margin  
`4`: Portfolio margin  
> lever | String | No | Cross margin leverage in Multi-currency margin mode, the default is `1`.  
If the allowed leverage is exceeded, set according to the maximum leverage.  
Only applicable to `Multi-currency margin`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
             {
                "type": "mmr",
                "mmrData": [
                   ......
                   {
                         "mmr": "1415.0254039225917",
                         "mmrRatio": "-47.45603627655477",
                         "shockFactor": "-0.94"
                   },
                   {
                         "mmr": "1417.732491243024",
                         "mmrRatio": "-47.436684685735386",
                         "shockFactor": "-0.93"
                   }
                   ......
                ]
             }
        ],
        "msg": ""
    }
    
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
type | String | Graph type  
`mmr`  
mmrData | Array | Array of mmrData  
Return data in shockFactor ascending order  
> shockFactor | String | Price change ratio, data range -1 to 1.  
> mmr | String | Mmr at specific price  
> mmrRatio | String | Maintenance margin ratio at specific price

---

# 仓位创建器趋势图

#### 限速：1次/5s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`POST /api/v5/account/position-builder-graph`

> 请求示例
    
    
    {
       "inclRealPosAndEq":false,
       "simPos":[
          {
             "pos":"-10",
             "instId":"BTC-USDT-SWAP",
             "avgPx":"100000"
          },
          {
             "pos":"10",
             "instId":"LTC-USDT-SWAP",
             "avgPx":"8000"
          }
       ],
       "simAsset":[
          {
             "ccy":"USDT",
             "amt":"100"
          }
       ],
       "greeksType":"CASH",
       "type":"mmr",
       "mmrConfig":{
          "acctLv":"3",
          "lever":"1"
       }
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
inclRealPosAndEq | Boolean | 否 | 是否代入已有仓位和资产  
默认为`true`  
simPos | Array of objects | 否 | 模拟仓位列表  
> instId | String | 是 | 交易产品ID，如 `BTC-USDT-SWAP`  
适用于 `SWAP`/`FUTURES`/`OPTION`  
> pos | String | 是 | 持仓量  
> avgPx | String | 是 | 平均开仓价格  
> lever | String | 否 | 杠杆  
仅适用于在跨币种保证金模式下指定交易产品的杠杆。如果用户不传，则选择默认杠杆为`1`。  
simAsset | Array of objects | 否 | 模拟资产  
当`inclRealPosAndEq`为`true`，只考虑真实资产，会忽略虚拟资产  
> ccy | String | 是 | 币种，如 `BTC`  
> amt | String | 是 | 币种数量  
可以为负，代表减少币种资产  
type | String | 是 | 趋势图类型  
`mmr`  
mmrConfig | Object | 是 | MMR配置  
> acctLv | String | 否 | 切换至账户模式  
`3`：跨币种保证金模式  
`4`：组合保证金模式  
> lever | String | 否 | 跨币种下整体的全仓合约杠杆数量，默认为`1`。  
如果超过允许的杠杆倍数，按照最大的杠杆设置。  
适用于`跨币种保证金模式`  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
             {
                "type": "mmr",
                "mmrData": [
                   ......
                   {
                         "mmr": "1415.0254039225917",
                         "mmrRatio": "-47.45603627655477",
                         "shockFactor": "-0.94"
                   },
                   {
                         "mmr": "1417.732491243024",
                         "mmrRatio": "-47.436684685735386",
                         "shockFactor": "-0.93"
                   }
                   ......
                ]
             }
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 趋势图类型  
`mmr`  
mmrData | Array | MMR数据  
以shockFactor升序返回  
> shockFactor | String | 价格变动比例，数据范围 -1 到 1.  
> mmr | String | 维持保证金  
> mmrRatio | String | 维持保证金率