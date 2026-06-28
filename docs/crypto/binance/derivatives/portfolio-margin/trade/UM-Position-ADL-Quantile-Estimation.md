---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation
api_type: Trading
updated_at: 2026-01-15T23:46:00.878354
---

# UM Position ADL Quantile Estimation(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#api-description "Direct link to API Description")

Query UM Position ADL Quantile Estimation

>   * Values update every 30s.
>   * Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
>   * For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
>   * If the positions of the symbol are crossed margined in Hedge Mode: 
>     * "HEDGE" as a sign will be returned instead of "BOTH";
>     * A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.
> 


## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/adlQuantile`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    		"symbol": "ETHUSDT",   
    		"adlQuantile":   
    			{  
    				// if the positions of the symbol are crossed margined in Hedge Mode, "LONG" and "SHORT" will be returned a same quantile value.  
    				"LONG": 3,    
    				"SHORT": 3,   
    				"BOTH": 0    
    			}  
    	},  
     	{  
     		"symbol": "BTCUSDT",   
     		"adlQuantile":   
     			{  
     				"LONG": 0, 	 	// adl quantile for "LONG" position in hedge mode  
     				"SHORT": 0, 	// adl quantile for "SHORT" position in hedge mode  
     				"BOTH": 2		// adl quantile for position in one-way mode  
     			}  
     	}  
    ]

---

# UM持仓ADL队列估算(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#接口描述 "接口描述的直接链接")

查询UM持仓ADL队列估算

  * 每30秒更新数据
  * 队列分数0，1，2，3，4，分数越高说明在ADL队列中的位置越靠前
  * 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数
  * 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE", 其中"HEDGE"的存在仅作为标记;其中如果多空均有持仓的情况下,"LONG"和"SHORT"返回共同计算后相同的队列分数。



## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/adlQuantile`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
    		"symbol": "ETHUSDT",   
    		"adlQuantile":   
    			{  
      
    				// 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH", 其中"BOTH"的存在仅作为标记;如果多空均有持仓的情况下,"LONG"和"SHORT"应返回共同计算后相同的队列分数。  
    				"LONG": 3,    
    				"SHORT": 3,   
    				"BOTH": 0  
    			}    
    	},  
     	{  
     		"symbol": "BTCUSDT",   
     		"adlQuantile":   
     			{  
     				"LONG": 0, 		// 双开模式下多头持仓的ADL队列估算分  
     				"SHORT": 0, 	// 双开模式下空头持仓的ADL队列估算分  
     				"BOTH": 2		// 单开模式下持仓的ADL队列估算分  
     			}  
     	}  
    ]