---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Margin-Transfer-for-Sub-account
api_type: Account
updated_at: 2026-05-27 19:02:27.994457
---

# Move Position for Sub-account (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Move-Position-for-Sub-account#api-description "Direct link to API Description")

Move position between sub-master, master-sub, or sub-sub accounts when necessary

## HTTP Request[​](/docs/sub_account/asset-management/Move-Position-for-Sub-account#http-request "Direct link to HTTP Request")

POST `/sapi/v1/sub-account/futures/move-position`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Move-Position-for-Sub-account#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Move-Position-for-Sub-account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
fromUserEmail| STRING| YES|   
toUserEmail| STRING| YES|   
productType| STRING| YES| Only support UM  
orderArgs| LIST<JSON>| YES| Max 10 positions supported. When input request parameter,orderArgs.symbol should be STRING, orderArgs.quantity should be BIGDECIMAL, and orderArgs.positionSide should be STRING, positionSide support BOTH,LONG and SHORT. Each entry should be like orderArgs[0].symbol=BTCUSDT,orderArgs[0].quantity=0.001,orderArgs[0].positionSide=BOTH. Example of the request parameter array: orderArgs[0].symbol=BTCUSDT orderArgs[0].quantity=0.001 orderArgs[0].positionSide=BOTH orderArgs[1].symbol=ETHUSDT orderArgs[1].quantity=0.01 orderArgs[1].positionSide=BOTH  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to Enable Trading permission for the API Key which requests this endpoint.
>   * This function only support VIP level 7-9.
>   * Only master account can use the function
>   * Quantity should be positive number only
>   * The function support normal account, PM PRO, PM PRO SPAN and PM Retail.
>   * Only support for from account has positions
>   * For all orders in the same orderArgs request, if any symbol’s total close position quantity is bigger than the symbol’s current position quantity, all batch orders in the same list will fail simultaneously.
>   * Only support cross margin mode
>   * The price for move position is MarkPrice only.
>   * Not support for MSA.
>   * Not support for the symbol under Reduce-Only.
> 


## Response Example[​](/docs/sub_account/asset-management/Move-Position-for-Sub-account#response-example "Direct link to Response Example")
    
    
    {  
    	"movePositionOrders": [{  
    		"fromUserEmail": "testFrom@google.com",  
    		"toUserEmail": "testTo@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"priceType": "MARK_PRICE",  
    		"price": "97139.00000000",  
    		"quantity": "0.001",  
    		"positionSide": "BOTH",  
    		"side": "BUY",  
    		"success": true  
    	}, {  
    		"fromUserEmail": "testFrom1@google.com",  
    		"toUserEmail": "1testTo@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"priceType": "MARK_PRICE",  
    		"price": "97139.00000000",  
    		"quantity": "0.0011",  
    		"positionSide": "BOTH",  
    		"side": "BUY",  
    		"success": true  
    	}]  
    }

---

# 移仓功能 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Move-Position-for-Sub-account#接口描述 "接口描述的直接链接")

支持主账户和母账户，子账户和子账户之间的移仓

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Move-Position-for-Sub-account#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/sub-account/futures/move-position `

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Move-Position-for-Sub-account#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Move-Position-for-Sub-account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromUserEmail| STRING| YES|   
toUserEmail| STRING| YES|   
productType| STRING| YES| 仅支持 UM  
orderArgs| LIST<JSON>| YES| 一次最多支持 10 个仓位转移. orderArgs.symbol的参数类型为STRING, orderArgs.quantity的参数类型为BIGDECIMAL, orderArgs.positionSide的参数类型为STRING, positionSide 支持 BOTH,LONG and SHORT. 请求参数格式如下 orderArgs[0].symbol=BTCUSDT,orderArgs[0].quantity=0.001,orderArgs[0].positionSide=BOTH. 举例: orderArgs[0].symbol=BTCUSDT orderArgs[0].quantity=0.001 orderArgs[0].positionSide=BOTH orderArgs[1].symbol=ETHUSDT orderArgs[1].quantity=0.01 orderArgs[1].positionSide=BOTH  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 您需要打开 API Key 的 Trading 权限以使用此接口。
>   * 该功能仅对VIP7-9开放.
>   * 只有母账户可以调用此接口。
>   * Quantity 必须为正数。
>   * 本功能支持普通合约账户, PM PRO, PM PRO SPAN 和 PM Retail 用户的仓位转移。
>   * 只有 from account 存在仓位才能调用此功能。
>   * 在同一个 orderArgs 的请求, 如果任何symbol的平仓总量大于该symbol的当前持仓量，则整个请求的订单都会失败。
>   * 仅支持全仓的仓位模式。
>   * 移仓价格默认且仅支持标记价格.
>   * MSA无法使用此功能。
>   * 用户账户上存在Reduce-Only设置的symbol无法使用此功能。
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Move-Position-for-Sub-account#响应示例 "响应示例的直接链接")
    
    
    {  
    	"movePositionOrders": [{  
    		"fromUserEmail": "testFrom@google.com",  
    		"toUserEmail": "testTo@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"priceType": "MARK_PRICE",  
    		"price": "97139.00000000",  
    		"quantity": "0.001",  
    		"positionSide": "BOTH",  
    		"side": "BUY",  
    		"success": true  
    	}, {  
    		"fromUserEmail": "testFrom1@google.com",  
    		"toUserEmail": "1testTo@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"priceType": "MARK_PRICE",  
    		"price": "97139.00000000",  
    		"quantity": "0.0011",  
    		"positionSide": "BOTH",  
    		"side": "BUY",  
    		"success": true  
    	}]  
    }