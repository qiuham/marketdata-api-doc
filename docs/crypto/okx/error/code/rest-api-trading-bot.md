---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#error-code-rest-api-trading-bot
anchor_id: error-code-rest-api-trading-bot
api_type: REST
updated_at: 2026-07-10 19:33:00.519631
---

# Trading bot

Error Code from 55100 to 55999  
  
Error Code | HTTP Status Code | Error Message  
---|---|---  
55100 | 200 | Take profit % should be within the range of {parameter1}-{parameter2}  
55101 | 200 | Stop loss % should be within the range of {parameter1}-{parameter2}  
55102 | 200 | Take profit % should be greater than the current bot’s PnL%  
55103 | 200 | Stop loss % should be less than the current bot’s PnL%  
55104 | 200 | Only futures grid supports take profit or stop loss based on profit percentage  
55105 | 200 | Increasing positions is not allowed under current status  
55106 | 200 | Increased amount should be within the range of {parameter1} - {parameter2}  
55111 | 200 | This signal name is in use, please try a new name  
55112 | 200 | This signal does not exist  
55113 | 200 | Create signal strategies with leverage greater than the maximum leverage of the instruments  
55116 | 200 | You can only place one chase order for each trading pair.

---

# 策略交易

错误码从 55100 到 55999  
  
错误码 | HTTP 状态码 | 错误提示  
---|---|---  
55100 | 200 | 止盈百分比应在 {parameter1} ~ {parameter2} 的范围内  
55101 | 200 | 止损百分比应在 {parameter1} ~ {parameter2} 的范围内  
55102 | 200 | 止盈百分比需大于当前策略收益率  
55103 | 200 | 止损百分比需小于当前策略收益率  
55104 | 200 | 仅合约网格支持按收益率百分比止盈止损  
55105 | 200 | 当前状态不支持加仓操作  
55106 | 200 | 加仓金额应在 {parameter1} ~ {parameter2} 的范围内  
55111 | 200 | 此信号名称正在使用中，请尝试新名称  
55112 | 200 | 此信号不存在  
55113 | 200 | 创建信号策略的杠杆倍数大于交易产品列的最大杠杆倍数  
55116 | 200 | 每个交易对只能进行一笔追逐限价委托