---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation
api_type: Trading
updated_at: 2026-01-15T23:39:50.197849
---

# Position ADL Quantile Estimation(USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#api-description "Direct link to API Description")

Query position ADL quantile estimation

>   * Values update every 30s.
>   * Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
>   * For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
>   * If the positions of the symbol are crossed margined in Hedge Mode: 
>     * "HEDGE" as a sign will be returned instead of "BOTH";
>     * A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.
> 


## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#http-request "Direct link to HTTP Request")

GET `/dapi/v1/adlQuantile`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    		"symbol": "BTCUSD_200925",   
    		"adlQuantile":   
    			{  
    				// if the positions of the symbol are crossed margined in Hedge Mode, "LONG" and "SHORT" will be returned a same quantile value, and "HEDGE" will be returned instead of "BOTH".  
    				"LONG": 3,    
    				"SHORT": 3,   
    				"HEDGE": 0   // only a sign, ignore the value  
    			}  
    		},  
     	{  
     		"symbol": "BTCUSD_201225",   
     		"adlQuantile":   
     			{  
     				// for positions of the symbol are in One-way Mode or isolated margined in Hedge Mode  
     				"LONG": 1, 	    // adl quantile for "LONG" position in hedge mode  
     				"SHORT": 2, 	// adl qauntile for "SHORT" position in hedge mode  
     				"BOTH": 0		// adl qunatile for position in one-way mode  
     			}  
     	}  
     ]

---

# 持仓ADL队列估算(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#接口描述 "接口描述的直接链接")

查询持仓ADL队列估算

>   * 每30秒更新数据
>   * 队列分数0，1，2，3，4，分数越高说明在ADL队列中的位置越靠前
>   * 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数
>   * 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE", 其中"HEDGE"的存在仅作为标记;其中如果多空均有持仓的情况下,"LONG"和"SHORT"返回共同计算后相同的队列分数。
> 


## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/adlQuantile`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
    		"symbol": "BTCUSD_200925",   
    		"adlQuantile":   
    			{  
    				// 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE", 其中"HEDGE"的存在仅作为标记;如果多空均有持仓的情况下,"LONG"和"SHORT"应返回共同计算后相同的队列分数。  
    				"LONG": 3,    
    				"SHORT": 3,   
    				"HEDGE": 0   // HEDGE 仅作为指示出现，请忽略数值  
    			}  
    		},  
     	{  
     		"symbol": "BTCUSD_201225",   
     		"adlQuantile":   
     			{  
     				// 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数  
     				"LONG": 1, 	// 双开模式下多头持仓的ADL队列估算分  
     				"SHORT": 2, 	// 双开模式下空头持仓的ADL队列估算分  
     				"BOTH": 0		// 单开模式下持仓的ADL队列估算分  
     			}  
     	}  
     ]