---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Balance-and-Position-Update
api_type: REST
updated_at: 2026-01-15T23:47:41.806232
---

# Event: Balance and Position Update

## Event Description[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Balance-and-Position-Update#event-description "Direct link to Event Description")

Event type is `ACCOUNT_UPDATE`.

  * When balance or position get updated, this event will be pushed.

    * `ACCOUNT_UPDATE` will be pushed only when update happens on user's account, including changes on balances, positions, or margin type.
    * Unfilled orders or cancelled orders will not make the event `ACCOUNT_UPDATE` pushed, since there's no change on positions.
    * "position" in `ACCOUNT_UPDATE`: Only symbols of changed positions will be pushed.
  * When "FUNDING FEE" changes to the user's balance, the event will be pushed with the brief message:

    * When "FUNDING FEE" occurs in a **crossed position** , `ACCOUNT_UPDATE` will be pushed with only the balance `B`(including the "FUNDING FEE" asset only), without any position `P` message.
    * When "FUNDING FEE" occurs in an **isolated position** , `ACCOUNT_UPDATE` will be pushed with only the balance `B`(including the "FUNDING FEE" asset only) and the relative position message `P`( including the isolated position on which the "FUNDING FEE" occurs only, without any other position message).
  * The field "m" represents the reason type for the event and may shows the following possible types:

    * DEPOSIT
    * WITHDRAW
    * ORDER
    * FUNDING_FEE
    * WITHDRAW_REJECT
    * ADJUSTMENT
    * INSURANCE_CLEAR
    * ADMIN_DEPOSIT
    * ADMIN_WITHDRAW
    * MARGIN_TRANSFER
    * MARGIN_TYPE_CHANGE
    * ASSET_TRANSFER
    * OPTIONS_PREMIUM_FEE
    * OPTIONS_SETTLE_PROFIT
    * AUTO_EXCHANGE
    * COIN_SWAP_DEPOSIT
    * COIN_SWAP_WITHDRAW
  * The field "bc" represents the balance change except for PnL and commission.




## Event Name[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Balance-and-Position-Update#event-name "Direct link to Event Name")

`ACCOUNT_UPDATE`

## Response Example[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Balance-and-Position-Update#response-example "Direct link to Response Example")
    
    
    {  
      "e": "ACCOUNT_UPDATE",				// Event Type  
      "E": 1564745798939,            		// Event Time  
      "T": 1564745798938 ,           		// Transaction  
      "a":                          		// Update Data  
        {  
          "m":"ORDER",						// Event reason type  
          "B":[                     		// Balances  
            {  
              "a":"USDT",           		// Asset  
              "wb":"122624.12345678",    	// Wallet Balance  
              "cw":"100.12345678",			// Cross Wallet Balance  
              "bc":"50.12345678"			// Balance Change except PnL and Commission  
            },  
            {  
              "a":"BUSD",             
              "wb":"1.00000000",  
              "cw":"0.00000000",           
              "bc":"-49.12345678"  
            }  
          ],  
          "P":[  
            {  
              "s":"BTCUSDT",          	// Symbol  
              "pa":"0",               	// Position Amount  
              "ep":"0.00000",            // Entry Price  
              "bep":"0",                // breakeven price   
    		  "cr":"200",             	// (Pre-fee) Accumulated Realized  
              "up":"0",						// Unrealized PnL  
              "mt":"isolated",				// Margin Type  
              "iw":"0.00000000",			// Isolated Wallet (if isolated position)  
              "ps":"BOTH"					// Position Side  
            }，  
            {  
            	"s":"BTCUSDT",  
            	"pa":"20",  
            	"ep":"6563.66500",  
            	"bep":"0",                // breakeven price  
            	"cr":"0",  
            	"up":"2850.21200",  
            	"mt":"isolated",  
            	"iw":"13200.70726908",  
            	"ps":"LONG"  
          	 },  
            {  
            	"s":"BTCUSDT",  
            	"pa":"-10",  
            	"ep":"6563.86000",  
            	"bep":"6563.6",          // breakeven price  
            	"cr":"-45.04000000",  
            	"up":"-1423.15600",  
            	"mt":"isolated",  
            	"iw":"6570.42511771",  
            	"ps":"SHORT"  
            }  
          ]  
        }  
    }

---

# Balance 和 Position 更新推送

## 事件描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Balance-and-Position-Update#事件描述 "事件描述的直接链接")

账户更新事件的 event type 固定为 `ACCOUNT_UPDATE`

  * 当账户信息有变动时，会推送此事件：

    * 仅当账户信息有变动时(包括资金、仓位、保证金模式等发生变化)，才会推送此事件；
    * 订单状态变化没有引起账户和持仓变化的，不会推送此事件；
    * position 信息：仅当 symbol 仓位有变动时推送。
  * "FUNDING FEE" 引起的资金余额变化，仅推送简略事件：

    * 当用户某**全仓** 持仓发生"FUNDING FEE"时，事件`ACCOUNT_UPDATE`将只会推送相关的用户资产余额信息`B`(仅推送 FUNDING FEE 发生相关的资产余额信息)，而不会推送任何持仓信息`P`。
    * 当用户某**逐仓** 仓持仓发生"FUNDING FEE"时，事件`ACCOUNT_UPDATE`将只会推送相关的用户资产余额信息`B`(仅推送"FUNDING FEE"所使用的资产余额信息)，和相关的持仓信息`P`(仅推送这笔"FUNDING FEE"发生所在的持仓信息)，其余持仓信息不会被推送。
  * 字段"m"代表了事件推出的原因，包含了以下可能类型:

    * DEPOSIT
    * WITHDRAW
    * ORDER
    * FUNDING_FEE
    * WITHDRAW_REJECT
    * ADJUSTMENT
    * INSURANCE_CLEAR
    * ADMIN_DEPOSIT
    * ADMIN_WITHDRAW
    * MARGIN_TRANSFER
    * MARGIN_TYPE_CHANGE
    * ASSET_TRANSFER
    * OPTIONS_PREMIUM_FEE
    * OPTIONS_SETTLE_PROFIT
    * AUTO_EXCHANGE
    * COIN_SWAP_DEPOSIT
    * COIN_SWAP_WITHDRAW
  * 字段"bc"代表了钱包余额的改变量，即 balance change，但注意其不包含仓位盈亏及交易手续费。




## 事件类型[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Balance-and-Position-Update#事件类型 "事件类型的直接链接")

`ACCOUNT_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Balance-and-Position-Update#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "ACCOUNT_UPDATE",				// 事件类型  
      "E": 1564745798939,            		// 事件时间  
      "T": 1564745798938 ,           		// 撮合时间  
      "a":                          		// 账户更新事件  
        {  
          "m":"ORDER",						// 事件推出原因  
          "B":[                     		// 余额信息  
            {  
              "a":"USDT",           		// 资产名称  
              "wb":"122624.12345678",    	// 钱包余额  
              "cw":"100.12345678",			// 除去逐仓仓位保证金的钱包余额  
              "bc":"50.12345678"			// 除去盈亏与交易手续费以外的钱包余额改变量  
            },  
            {  
              "a":"BUSD",  
              "wb":"1.00000000",  
              "cw":"0.00000000",  
              "bc":"-49.12345678"  
            }  
          ],  
          "P":[  
           {  
              "s":"BTCUSDT",          	// 交易对  
              "pa":"0",               	// 仓位  
              "ep":"0.00000",            // 入仓价格  
              "bep":"0",                // 盈亏平衡价  
              "cr":"200",             	// (费前)累计实现损益  
              "up":"0",						// 持仓未实现盈亏  
              "mt":"isolated",				// 保证金模式  
              "iw":"0.00000000",			// 若为逐仓，仓位保证金  
              "ps":"BOTH"					// 持仓方向  
           }，  
           {  
            	"s":"BTCUSDT",  
            	"pa":"20",  
            	"ep":"6563.66500",  
            	"bep":"6563.6",  
            	"cr":"0",  
            	"up":"2850.21200",  
            	"mt":"isolated",  
            	"iw":"13200.70726908",  
            	"ps":"LONG"  
          	 },  
           {  
            	"s":"BTCUSDT",  
            	"pa":"-10",  
            	"ep":"6563.86000",  
            	"bep":"6563.6",  
            	"cr":"-45.04000000",  
            	"up":"-1423.15600",  
            	"mt":"isolated",  
            	"iw":"6570.42511771",  
            	"ps":"SHORT"  
           }  
          ]  
        }  
    }