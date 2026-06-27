---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History
api_type: Account
updated_at: 2026-01-15T23:37:46.341256
---

# Get Income History(USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#api-description "Direct link to API Description")

Get income history

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#http-request "Direct link to HTTP Request")

GET `/dapi/v1/income`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
incomeType| STRING| NO| "TRANSFER","WELCOME_BONUS", "FUNDING_FEE", "REALIZED_PNL", "COMMISSION", "INSURANCE_CLEAR", and "DELIVERED_SETTELMENT"  
startTime| LONG| NO| Timestamp in ms to get funding from INCLUSIVE.  
endTime| LONG| NO| Timestamp in ms to get funding until INCLUSIVE.  
page| INT| NO|   
limit| INT| NO| Default 100; max 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If `incomeType ` is not sent, all kinds of flow will be returned
>   * "trandId" is unique in the same "incomeType" for a user
>   * The time between `startTime` and `endTime` can not be longer than 1 year
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#response-example "Direct link to Response Example")
    
    
    [  
    	{  
        	"symbol": "",				// trade symbol, if existing  
        	"incomeType": "TRANSFER",	// income type  
        	"income": "-0.37500000",	// income amount  
        	"asset": "BTC",				// income asset  
        	"info":"WITHDRAW",			// extra information  
        	"time": 1570608000000,  
        	"tranId":"9689322392",		// transaction id  
        	"tradeId":""				// trade id, if existing  
    	},  
    	{  
       		"symbol": "BTCUSD_200925",  
        	"incomeType": "COMMISSION",   
        	"income": "-0.01000000",  
        	"asset": "BTC",  
        	"info":"",  
        	"time": 1570636800000,  
        	"tranId":"9689322392",  
        	"tradeId":"2059192"  
    	}  
    ]

---

# 获取账户损益资金流水(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#接口描述 "接口描述的直接链接")

获取账户损益资金流水

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/income`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
incomeType| STRING| NO| 收益类型 "TRANSFER","WELCOME_BONUS", "FUNDING_FEE", "REALIZED_PNL", "COMMISSION", "INSURANCE_CLEAR", "DELIVERED_SETTELMENT"  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
page| INT| NO| 分页数  
limit| INT| NO| 返回的结果集数量 默认值:100 最大值:1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 如果`incomeType`没有发送,返回所有类型账户损益资金流水。
>   * "trandId" 在相同用户的同一种收益流水类型中是唯一的。
>   * `startTime`与`endTime`间隔不能超过1年回
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
        	"symbol": "", // 交易对,仅针对涉及交易对的资金流  
        	"incomeType": "TRANSFER",	// 资金流类型  
        	"income": "-0.37500000", // 资金流数量,正数代表流入,负数代表流出  
        	"asset": "BTC", // 资产内容  
        	"info":"WITHDRAW", // 备注信息,取决于流水类型  
        	"time": 1570608000000, // 时间  
        	"tranId":"9689322392",		// 划转ID  
        	"tradeId":""					// 引起流水产生的原始交易ID  
    	},  
    	{  
       		"symbol": "BTCUSD_200925",  
        	"incomeType": "COMMISSION",   
        	"income": "-0.01000000",  
        	"asset": "BTC",  
        	"info":"",  
        	"time": 1570636800000,  
        	"tranId":"9689322392",		  
        	"tradeId":"2059192"					  
    	}  
    ]