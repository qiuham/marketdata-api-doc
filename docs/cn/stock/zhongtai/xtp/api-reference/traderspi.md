---
api_type: trade
source_type: http_api
version: XTP 3.0
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
provider_name: 中泰证券
product: xtp
product_id: zhongtai-xtp
id: zhongtai-xtp-2074064396203683842
title: TraderSpi
doc_id: 2074064396203683842
doc_category: 详细接口使用说明
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2074064396203683842'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-07-06
---

# TraderSpi

## TraderSpi


- [TraderSpi](#traderspi)
  - [1. 接口](#1-接口)
  - [2. 代码示例](#2-代码示例)
  - [3. OnDisconnected](#3-ondisconnected)
  - [4. OnError](#4-onerror)
  - [5. OnQueryAccountTradeMarket](#5-onqueryaccounttrademarket)
  - [6. OnOrderEvent](#6-onorderevent)
  - [7. OnUnknownOrder](#7-onunknownorder)
  - [8. OnTradeEvent](#8-ontradeevent)
  - [9. OnCancelOrderError](#9-oncancelordererror)
  - [10. OnQueryOrder](#10-onqueryorder)
  - [11. OnQueryOrderEx](#11-onqueryorderex)
  - [12. OnQueryOrderByPage](#12-onqueryorderbypage)
  - [13. OnQueryOrderByPageEx](#13-onqueryorderbypageex)
  - [14. OnQueryTrade](#14-onquerytrade)
  - [15. OnQueryTradeByPage](#15-onquerytradebypage)
  - [16. OnQueryPosition](#16-onqueryposition)
  - [17. OnQueryAsset](#17-onqueryasset)
  - [18. OnQueryStructuredFund](#18-onquerystructuredfund)
  - [19. OnQueryFundTransfer](#19-onqueryfundtransfer)
  - [20. OnFundTransfer](#20-onfundtransfer)
  - [21. OnQueryOtherServerFund](#21-onqueryotherserverfund)
  - [22. OnQueryETF](#22-onqueryetf)
  - [23. OnQueryETFBasket](#23-onqueryetfbasket)
  - [24. OnQueryIPOInfoList](#24-onqueryipoinfolist)
  - [25. OnQueryIPOQuotaInfo](#25-onqueryipoquotainfo)
  - [26. OnQueryBondIPOInfoList](#26-onquerybondipoinfolist)
  - [27. OnQueryBondSwapStockInfo](#27-onquerybondswapstockinfo)
  - [28. OnQueryOptionAuctionInfo](#28-onqueryoptionauctioninfo)
  - [29. OnCreditCashRepay](#29-oncreditcashrepay)
  - [30. OnCreditCashRepayDebtInterestFee](#30-oncreditcashrepaydebtinterestfee)
  - [31. OnQueryCreditCashRepayInfo](#31-onquerycreditcashrepayinfo)
  - [32. OnQueryCreditFundInfo](#32-onquerycreditfundinfo)
  - [33. OnQueryCreditDebtInfo](#33-onquerycreditdebtinfo)
  - [34. OnQueryCreditTickerDebtInfo](#34-onquerycredittickerdebtinfo)
  - [35. OnQueryCreditAssetDebtInfo](#35-onquerycreditassetdebtinfo)
  - [36. OnQueryCreditTickerAssignInfo](#36-onquerycredittickerassigninfo)
  - [37. OnQueryCreditExcessStock](#37-onquerycreditexcessstock)
  - [38. OnQueryMulCreditExcessStock](#38-onquerymulcreditexcessstock)
  - [39. OnCreditExtendDebtDate](#39-oncreditextenddebtdate)
  - [40. OnQueryCreditExtendDebtDateOrders](#40-onquerycreditextenddebtdateorders)
  - [41. OnQueryCreditFundExtraInfo](#41-onquerycreditfundextrainfo)
  - [42. OnQueryCreditPositionExtraInfo](#42-onquerycreditpositionextrainfo)
  - [43. OnOptionCombinedOrderEvent](#43-onoptioncombinedorderevent)
  - [44. OnOptionCombinedTradeEvent](#44-onoptioncombinedtradeevent)
  - [45. OnCancelOptionCombinedOrderError](#45-oncanceloptioncombinedordererror)
  - [46. OnQueryOptionCombinedOrders](#46-onqueryoptioncombinedorders)
  - [47. OnQueryOptionCombinedOrdersEx](#47-onqueryoptioncombinedordersex)
  - [48. OnQueryOptionCombinedOrdersByPage](#48-onqueryoptioncombinedordersbypage)
  - [49. OnQueryOptionCombinedOrdersByPageEx](#49-onqueryoptioncombinedordersbypageex)
  - [50. OnQueryOptionCombinedTrades](#50-onqueryoptioncombinedtrades)
  - [51. OnQueryOptionCombinedTradesByPage](#51-onqueryoptioncombinedtradesbypage)
  - [52. OnQueryOptionCombinedPosition](#52-onqueryoptioncombinedposition)
  - [53. OnQueryOptionCombinedStrategyInfo](#53-onqueryoptioncombinedstrategyinfo)
  - [54. OnQueryOptionCombinedExecPosition](#54-onqueryoptioncombinedexecposition)
  - [55. OnQueryStrategy](#55-onquerystrategy)
  - [56. OnStrategyStateReport](#56-onstrategystatereport)
  - [57. OnALGOUserEstablishChannel](#57-onalgouserestablishchannel)
  - [58. OnInsertAlgoOrder](#58-oninsertalgoorder)
  - [59. OnCancelAlgoOrder](#59-oncancelalgoorder)
  - [60. OnAlgoDisconnected](#60-onalgodisconnected)
  - [61. OnAlgoConnected](#61-onalgoconnected)
  - [62. OnStrategySymbolStateReport](#62-onstrategysymbolstatereport)
  - [63. OnNewStrategyCreateReport](#63-onnewstrategycreatereport)
  - [64. OnStrategyRecommendation](#64-onstrategyrecommendation)
  - [65. OnModifyAlgoOrder](#65-onmodifyalgoorder)
  - [66. OnPauseAlgoOrder](#66-onpausealgoorder)
  - [67. OnResumeAlgoOrder](#67-onresumealgoorder)


TraderSpi类提供了交易相关的回调接口，用户需要继承该类并重写这些接口，以获取响应数据。

### 1. 接口


```cpp
namespace XTP {
	namespace API {

		class TraderSpi
		{
		public:

			///当客户端的某个连接与交易后台通信连接断开时，该方法被调用。
			///@param reason 错误原因，请与错误代码表对应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 用户主动调用logout导致的断线，不会触发此函数。api不会自动重连，当断线发生时，请用户自行选择后续操作，可以在此函数中调用Login重新登录，并更新session_id，此时用户收到的数据跟断线之前是连续的
			virtual void OnDisconnected(uint64_t session_id, int reason) {};

			///错误应答
			///@param error_info 当服务器响应发生错误时的具体的错误代码和错误信息,当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 此函数只有在服务器发生错误时才会调用，一般无需用户处理
			virtual void OnError(XTPRI *error_info) {};

			///请求查询用户在本节点上可交易市场的响应
			///@param trade_location 查询到的交易市场信息，按位来看，从低位开始数，第0位表示沪市，即如果(trade_location&0x01) == 0x01，代表可交易沪市，第1位表示深市，即如果(trade_location&0x02) == 0x02，表示可交易深市，如果第0位和第1位均是1，即(trade_location&(0x01|0x02)) == 0x03，就表示可交易沪深2个市场
			///@param error_info 查询可交易市场发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 此查询只会有一个结果
			virtual void OnQueryAccountTradeMarket(int trade_location, XTPRI *error_info, int request_id, uint64_t session_id) {};

			///报单通知
			///@param order_info 订单响应具体信息，用户可以通过order_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单，order_info.qty_left字段在订单为未成交、部成、全成、废单状态时，表示此订单还没有成交的数量，在部撤、全撤状态时，表示此订单被撤的数量。order_info.order_cancel_xtp_id为其所对应的撤单ID，不为0时表示此单被撤成功
			///@param error_info 订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 每次订单状态更新时，都会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，在订单未成交、全部成交、全部撤单、部分撤单、已拒绝这些状态时会有响应，对于部分成交的情况，请由订单的成交回报来自行确认。所有登录了此用户的客户端都将收到此用户的订单响应
			virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};

			///报单未知状态通知
			///@param order_xtp_id 未知状态订单的order_xtp_id
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 此响应仅表明交易服务器丢失订单，并没有报送到交易所。如果收到此响应，可以在本地订单缓存中查找到对应的订单进行标注
			virtual void OnUnknownOrder(uint64_t order_xtp_id, uint64_t session_id) {};

			///成交通知
			///@param trade_info 成交回报的具体信息，用户可以通过trade_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。对于上交所，exec_id可以唯一标识一笔成交。当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交了。对于深交所，exec_id是唯一的，暂时无此判断机制。report_index+market字段可以组成唯一标识表示成交回报。
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 订单有成交发生的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的成交回报。相关订单为部成状态，需要用户通过成交回报的成交数量来确定，OnOrderEvent()不会推送部成状态。
			virtual void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id) {};

			///撤单出错响应
			///@param cancel_info 撤单具体信息，包括撤单的order_cancel_xtp_id和待撤单的order_xtp_id
			///@param error_info 撤单被拒绝或者发生错误时错误代码和错误信息，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 此响应只会在撤单发生错误时被回调
			virtual void OnCancelOrderError(XTPOrderCancelInfo *cancel_info, XTPRI *error_info, uint64_t session_id) {};

			///请求查询报单响应-旧版本接口
			///@param order_info 查询到的一个报单
			///@param error_info 查询报单时发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询报单响应-新版本接口
			///@param order_info 查询到的一个报单信息
			///@param error_info 查询报单时发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryOrderEx(XTPOrderInfoEx *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///分页请求查询报单响应-旧版本接口
			///@param order_info 查询到的一个报单
			///@param req_count 分页请求的最大数量
			///@param order_sequence 分页请求的当前回报数量
			///@param query_reference 当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果order_sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
			virtual void OnQueryOrderByPage(XTPQueryOrderRsp *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};

			///分页请求查询报单响应-新版本接口
			///@param order_info 查询到的一个报单
			///@param req_count 分页请求的最大数量
			///@param order_sequence 分页请求的当前回报数量
			///@param query_reference 当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果order_sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
			virtual void OnQueryOrderByPageEx(XTPOrderInfoEx *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询成交响应
			///@param trade_info 查询到的一个成交回报
			///@param error_info 查询成交回报发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual void OnQueryTrade(XTPQueryTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///分页请求查询成交响应
			///@param trade_info 查询到的一个成交信息
			///@param req_count 分页请求的最大数量
			///@param trade_sequence 分页请求的当前回报数量
			///@param query_reference 当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 当trade_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果trade_sequence等于req_count，那么表示还有回报，可以进行下一次分页查询，如果不等，表示所有回报已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
			virtual void OnQueryTradeByPage(XTPQueryTradeRsp *trade_info, int64_t req_count, int64_t trade_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询投资者持仓响应
			///@param position 查询到的一只股票的持仓情况
			///@param error_info 查询账户持仓发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 由于用户可能持有多个股票，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryPosition(XTPQueryStkPositionRsp *position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询资金账户响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param asset 查询到的资金账户情况
			///@param error_info 查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryAsset(XTPQueryAssetRsp *asset, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询分级基金信息响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param fund_info 查询到的分级基金情况
			///@param error_info 查询分级基金发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryStructuredFund(XTPStructuredFundInfo *fund_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询资金划拨订单响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param fund_transfer_info 查询到的资金账户情况
			///@param error_info 查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryFundTransfer(XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///资金划拨通知
			///@param fund_transfer_info 资金划拨通知的具体信息，用户可以通过fund_transfer_info.serial_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。
			///@param error_info 资金划拨订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误。当资金划拨方向为一号两中心节点之间划拨，且error_info.error_id=11000384时，error_info.error_msg中含有对方结点中可用于划拨的资金（以整数为准），用户需解析后进行stringToInt的转化，可据此填写合适的资金，再次发起划拨请求
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 当资金划拨订单有状态变化的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的资金划拨通知。
			virtual void OnFundTransfer(XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info, uint64_t session_id) {};

			///请求查询其他节点可用资金的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param fund_info 查询到的其他节点可用资金情况
			///@param error_info 查询其他节点可用资金发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryOtherServerFund(XTPFundQueryRsp *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) {};

			///请求查询ETF清单文件的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param etf_info 查询到的ETF清单文件情况
			///@param error_info 查询ETF清单文件发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryETF(XTPQueryETFBaseRsp *etf_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询ETF股票篮的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param etf_component_info 查询到的ETF合约的相关成分股信息
			///@param error_info 查询ETF股票篮发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryETFBasket(XTPQueryETFComponentRsp *etf_component_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询今日新股申购信息列表的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param ipo_info 查询到的今日新股申购的一只股票信息
			///@param error_info 查询今日新股申购信息列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询用户新股申购额度信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param quota_info 查询到的用户某个市场的今日新股申购额度信息
			///@param error_info 查查询用户新股申购额度信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryIPOQuotaInfo(XTPQueryIPOQuotaRsp *quota_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询今日可转债申购信息列表的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param ipo_info 查询到的今日可转债申购的一只可转债信息
			///@param error_info 查询今日可转债申购信息列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryBondIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询用户可转债转股信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param swap_stock_info 查询到某条可转债转股信息
			///@param error_info 查查询可转债转股信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryBondSwapStockInfo(XTPQueryBondSwapStockRsp *swap_stock_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询期权合约的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param option_info 查询到的期权合约情况
			///@param error_info 查询期权合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryOptionAuctionInfo(XTPQueryOptionAuctionInfoRsp *option_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///融资融券业务中现金直接还款的响应
			///@param cash_repay_info 现金直接还款通知的具体信息，用户可以通过cash_repay_info.xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。
			///@param error_info 现金还款发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnCreditCashRepay(XTPCrdCashRepayRsp *cash_repay_info, XTPRI *error_info, uint64_t session_id) {};

			///融资融券业务中现金还息的响应
			///@param cash_repay_info 现金还息通知的具体信息，用户可以通过cash_repay_info.xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。
			///@param error_info 现金还息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnCreditCashRepayDebtInterestFee(XTPCrdCashRepayDebtInterestFeeRsp *cash_repay_info, XTPRI *error_info, uint64_t session_id) {};

			///请求查询融资融券业务中的现金直接还款报单的响应
			///@param cash_repay_info 查询到的某一笔现金直接还款通知的具体信息
			///@param error_info 查询现金直接报单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditCashRepayInfo(XTPCrdCashRepayInfo *cash_repay_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询信用账户额外信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param fund_info 查询到的信用账户额外信息情况
			///@param error_info 查询信用账户额外信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditFundInfo(XTPCrdFundInfo *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) {};

			///请求查询信用账户负债信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param debt_info 查询到的信用账户合约负债情况
			///@param error_info 查询信用账户负债信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditDebtInfo(XTPCrdDebtInfo *debt_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询信用账户指定证券负债未还信息响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param debt_info 查询到的信用账户指定证券负债未还信息情况
			///@param error_info 查询信用账户指定证券负债未还信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditTickerDebtInfo(XTPCrdDebtStockInfo *debt_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询信用账户待还资金的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param remain_amount 查询到的信用账户待还资金
			///@param error_info 查询信用账户待还资金发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditAssetDebtInfo(double remain_amount, XTPRI *error_info, int request_id, uint64_t session_id) {};

			///请求查询信用账户可融券头寸信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param assign_info 查询到的信用账户可融券头寸信息
			///@param error_info 查询信用账户可融券头寸信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditTickerAssignInfo(XTPClientQueryCrdPositionStkInfo *assign_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///融资融券业务中请求查询指定余券信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param stock_info 查询到的余券信息
			///@param error_info 查询信用账户余券信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditExcessStock(XTPClientQueryCrdSurplusStkRspInfo* stock_info, XTPRI *error_info, int request_id, uint64_t session_id) {};

			///融资融券业务中请求查询余券信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param stock_info 查询到的余券信息
			///@param error_info 查询信用账户余券信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryMulCreditExcessStock(XTPClientQueryCrdSurplusStkRspInfo* stock_info, XTPRI *error_info, int request_id, uint64_t session_id, bool is_last) {};

			///融资融券业务中负债合约展期的通知
			///@param debt_extend_info 负债合约展期通知的具体信息，用户可以通过debt_extend_info.xtpid来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。
			///@param error_info 负债合约展期订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误。
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 当负债合约展期订单有状态变化的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的负债合约展期通知。
			virtual void OnCreditExtendDebtDate(XTPCreditDebtExtendNotice *debt_extend_info, XTPRI *error_info, uint64_t session_id) {};

			///查询融资融券业务中负债合约展期订单响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param debt_extend_info 查询到的负债合约展期情况
			///@param error_info 查询负债合约展期发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误。当error_info.error_id=11000350时，表明没有记录，当为其他非0值时，表明合约发生拒单时的错误原因
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditExtendDebtDateOrders(XTPCreditDebtExtendNotice *debt_extend_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///查询融资融券业务中信用账户附加信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param fund_info 信用账户附加信息
			///@param error_info 查询信用账户附加信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditFundExtraInfo(XTPCrdFundExtraInfo *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) {};

			///查询融资融券业务中信用账户指定证券的附加信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			///@param fund_info 信用账户指定证券的附加信息
			///@param error_info 查询信用账户附加信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryCreditPositionExtraInfo(XTPCrdPositionExtraInfo *fund_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///期权组合策略报单通知
			///@param order_info 订单响应具体信息，用户可以通过order_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单，order_info.qty_left字段在订单为未成交、部成、全成、废单状态时，表示此订单还没有成交的数量，在部撤、全撤状态时，表示此订单被撤的数量。order_info.order_cancel_xtp_id为其所对应的撤单ID，不为0时表示此单被撤成功
			///@param error_info 订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 每次订单状态更新时，都会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，在订单未成交、全部成交、全部撤单、部分撤单、已拒绝这些状态时会有响应，对于部分成交的情况，请由订单的成交回报来自行确认。所有登录了此用户的客户端都将收到此用户的订单响应
			virtual void OnOptionCombinedOrderEvent(XTPOptCombOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};

			///期权组合策略成交通知
			///@param trade_info 成交回报的具体信息，用户可以通过trade_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。对于上交所，exec_id可以唯一标识一笔成交。当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交了。对于深交所，exec_id是唯一的，暂时无此判断机制。report_index+market字段可以组成唯一标识表示成交回报。
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 订单有成交发生的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的成交回报。相关订单为部成状态，需要用户通过成交回报的成交数量来确定，OnOrderEvent()不会推送部成状态。
			virtual void OnOptionCombinedTradeEvent(XTPOptCombTradeReport *trade_info, uint64_t session_id) {};

			///期权组合策略撤单出错响应
			///@param cancel_info 撤单具体信息，包括撤单的order_cancel_xtp_id和待撤单的order_xtp_id
			///@param error_info 撤单被拒绝或者发生错误时错误代码和错误信息，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 此响应只会在撤单发生错误时被回调
			virtual void OnCancelOptionCombinedOrderError(XTPOptCombOrderCancelInfo *cancel_info, XTPRI *error_info, uint64_t session_id) {};

			///请求查询期权组合策略报单响应-旧版本接口
			///@param order_info 查询到的一个报单
			///@param error_info 查询报单时发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual void OnQueryOptionCombinedOrders(XTPQueryOptCombOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询期权组合策略报单响应-新版本接口
			///@param order_info 查询到的一个报单
			///@param error_info 查询报单时发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual void OnQueryOptionCombinedOrdersEx(XTPOptCombOrderInfoEx *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///分页请求查询期权组合策略报单响应-旧版本接口
			///@param order_info 查询到的一个报单
			///@param req_count 分页请求的最大数量
			///@param order_sequence 分页请求的当前回报数量
			///@param query_reference 当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果order_sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
			virtual void OnQueryOptionCombinedOrdersByPage(XTPQueryOptCombOrderRsp *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};

			///分页请求查询期权组合策略报单响应-新版本接口
			///@param order_info 查询到的一个报单
			///@param req_count 分页请求的最大数量
			///@param order_sequence 分页请求的当前回报数量
			///@param query_reference 当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果order_sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
			virtual void OnQueryOptionCombinedOrdersByPageEx(XTPOptCombOrderInfoEx *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询期权组合策略成交响应
			///@param trade_info 查询到的一个成交回报
			///@param error_info 查询成交回报发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual void OnQueryOptionCombinedTrades(XTPQueryOptCombTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///分页请求查询期权组合策略成交响应
			///@param trade_info 查询到的一个成交信息
			///@param req_count 分页请求的最大数量
			///@param trade_sequence 分页请求的当前回报数量
			///@param query_reference 当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 当trade_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果trade_sequence等于req_count，那么表示还有回报，可以进行下一次分页查询，如果不等，表示所有回报已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
			virtual void OnQueryOptionCombinedTradesByPage(XTPQueryOptCombTradeRsp *trade_info, int64_t req_count, int64_t trade_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询期权组合策略持仓响应
			///@param position_info 查询到的一个持仓信息
			///@param error_info 查询持仓发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
			virtual void OnQueryOptionCombinedPosition(XTPQueryOptCombPositionRsp *position_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///请求查询期权组合策略信息响应
			///@param strategy_info 查询到的一个组合策略信息
			///@param error_info 查询成交回报发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
			virtual void OnQueryOptionCombinedStrategyInfo(XTPQueryCombineStrategyInfoRsp *strategy_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///查询期权行权合并头寸的响应
			///@param position_info 查询到的一个行权合并头寸信息
			///@param error_info 查询持仓发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
			virtual void OnQueryOptionCombinedExecPosition(XTPQueryOptCombExecPosRsp *position_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

			///algo业务中查询策略列表的响应
			///@param strategy_info 策略具体信息
			///@param strategy_param 此策略中包含的参数，如果error_info.error_id为0时，有意义
			///@param error_info 查询查询策略列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnQueryStrategy(XTPStrategyInfoStruct* strategy_info, char* strategy_param, XTPRI *error_info, int32_t request_id, bool is_last, uint64_t session_id) {};

			///algo业务中策略运行时策略状态通知
			///@param strategy_state 用户策略运行情况的状态通知
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnStrategyStateReport(XTPStrategyStateReportStruct* strategy_state, uint64_t session_id) {};

			///algo业务中用户建立算法通道的消息响应
			///@param user 用户名
			///@param error_info 建立算法通道发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误，即算法通道成功
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 算法通道建立成功后，才能对用户创建策略等操作，一个用户只能拥有一个算法通道，如果之前已经建立，则无需重复建立
			virtual void OnALGOUserEstablishChannel(char* user, XTPRI* error_info, uint64_t session_id) {};

			///algo业务中报送策略单的响应
			///@param strategy_info 用户报送的策略单的具体信息
			///@param error_info 报送策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnInsertAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPRI *error_info, uint64_t session_id) {};

			///algo业务中撤销策略单的响应
			///@param strategy_info 用户撤销的策略单的具体信息
			///@param error_info 撤销策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnCancelAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPRI *error_info, uint64_t session_id) {};

			///当客户端与AlgoBus通信连接断开时，该方法被调用。
			///@param reason 错误原因，请与错误代码表对应
			///@remark 请不要堵塞此线程，否则会影响algo的登录，与Algo之间的连接，断线后会自动重连，用户无需做其他操作
			virtual void OnAlgoDisconnected(int reason) {};

			///当客户端与AlgoBus断线后重新连接时，该方法被调用，仅在断线重连成功后会被调用。
			virtual void OnAlgoConnected() {};

			///algo业务中策略运行时策略指定证券执行状态通知
			///@param strategy_symbol_state 用户策略指定证券运行情况的状态通知
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, uint64_t session_id) {};

			///algo业务中报送母单创建时的推送消息(包括其他客户端创建的母单)
			///@param strategy_info 策略具体信息
			///@param strategy_param 此策略中包含的参数
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, uint64_t session_id) {};

			///algo业务中算法推荐的响应
			///@param basket_flag 是否将满足条件的推荐结果打包成母单篮的标志，与请求一致，如果此参数为true，那么请以返回的strategy_param为准
			///@param recommendation_info 推荐算法的具体信息，当basket_flag=true时，此结构体中的market和ticker将没有意义，此时请以strategy_param为准
			///@param strategy_param 算法参数，可直接用来创建母单，如果error_info.error_id为0时，有意义
			///@param error_info 请求推荐算法发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnStrategyRecommendation(bool basket_flag, XTPStrategyRecommendationInfo* recommendation_info, char* strategy_param, XTPRI *error_info, int32_t request_id, bool is_last, uint64_t session_id) {};

			///algo业务中修改已有策略单的响应
			///@param strategy_info 用户修改后策略单的具体信息
			///@param error_info 修改策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnModifyAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPRI *error_info, uint64_t session_id) {};

            ///algo业务中暂停指定策略指定证券算法单的响应
			///@param xtp_strategy_id xtp算法单策略ID
			///@param ticker_info 指定证券信息，可以为null，为null表示暂停指定策略中所有证券的算法单
			///@param error_info 修改策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnPauseAlgoOrder(uint64_t xtp_strategy_id, XTPStrategyTickerInfo* ticker_info, XTPRI *error_info, int32_t request_id, uint64_t session_id) {};

			///algo业务中重启指定策略指定证券算法单的响应
			///@param xtp_strategy_id xtp算法单策略ID
			///@param ticker_info 指定证券信息，可以为null，为null表示重启指定策略中所有证券的算法单
			///@param error_info 修改策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param request_id 此消息响应函数对应的请求ID
			///@param session_id 资金账户对应的session_id，登录时得到
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnResumeAlgoOrder(uint64_t xtp_strategy_id, XTPStrategyTickerInfo* ticker_info, XTPRI *error_info, int32_t request_id, uint64_t session_id) {};
		};
	}
}
```


### 2. 代码示例


MyTraderSpi继承TraderSpi
以下是MyTraderSpi.h文件
```cpp
#include "xtp_trader_api.h"

using namespace XTP::API;

class MyTraderSpi : public TraderSpi
{
public:
	explicit MyTraderSpi();
	~MyTraderSpi();

	// 查询报单响应
	void OnQueryOrder(XTPOrderInfo *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id);
	// 报单通知
	void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id);
	// 成交通知
	void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id);
};
```
以下是MyTraderSpi.cpp文件
```cpp
#include "MyTraderSpi.h"

MyTraderSpi::MyTraderSpi() { }
MyTraderSpi::~MyTraderSpi() { }

// 查询报单响应
void MyTraderSpi::OnQueryOrder(XTPOrderInfo *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id)
{
	std::cout
#include

using namespace std;
using namespace XTP::API;

class MyTraderSpi : public TraderSpi
{
public:
	explicit MyTraderSpi();
	~MyTraderSpi();

	void bindTraderFunc(std::function f)
    {
        _disconnect = f;
    }

private:
    std::function _disconnect;
}
```
以下是MyTraderSpi.cpp文件
```cpp
#include "MyTraderSpi.h"

MyTraderSpi::MyTraderSpi() { }
MyTraderSpi::~MyTraderSpi() { }

void MyTraderSpi::OnDisconnected(uint64_t session_id, int reason)
{
	std::cout
#else
    #include
#endif

MyTraderApi::MyTraderApi()
{
}

// 创建并初始化交易API
bool MyTraderApi::initialize()
{
	user_trade_api_ = XTP::API::TraderApi::CreateTraderApi(1, "./", XTP_LOG_LEVEL_DEBUG);
	if (user_trader_api_)
	{
		// 注册回调接口
		m_trader_spi = new MyTraderSpi();
		user_trade_api_->RegisterSpi(m_trader_spi);
		// 在spi实例化后绑定重连函数指针
		m_trader_spi->bindTraderFunc(std::bind(&MyTraderApi::reloginTrader, this));
	}
}

// 重连函数，若最多只允许重连3次，每次重连间隔5秒
void MyTraderApi::reloginTrader()
{
    if ((!m_loginTraderInfo.trade_server_ip.empty()) && (m_loginTraderInfo.trade_server_port != 0)
            && (!m_loginTraderInfo.account_name.empty()) && (!m_loginTraderInfo.account_pw.empty())) {

		//重连次数
		int i_counter = 0;
        while (i_counter Login(m_loginTraderInfo.trade_server_ip.c_str(),
                                             m_loginTraderInfo.trade_server_port,
                                             m_loginTraderInfo.account_name.c_str(),
                                             m_loginTraderInfo.account_pw.c_str(),
                                             m_loginTraderInfo.trade_sock_type,
                                             m_loginTraderInfo.local_ip.c_str());
            if (ret != 0) {
				std::cout
#include

using namespace std;
using namespace XTP::API;

class MyTraderSpi : public TraderSpi
{
public:
	explicit MyTraderSpi();
	~MyTraderSpi();

	void OnQueryPosition(XTPQueryStkPositionRsp * investor_position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id);

private:
    std::list query_stk_position_buffer_;
    std::list query_allotment_buffer_;
}
```
以下是MyTraderSpi.cpp文件
```cpp
#include "MyTraderSpi.h"

MyTraderSpi::MyTraderSpi() { }
MyTraderSpi::~MyTraderSpi() { }

void MyTraderSpi::OnQueryPosition(XTPQueryStkPositionRsp * investor_position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id)
{
    if (error_info && (error_info->error_id != 0)) {
		//查询出错
		if (error_info->error_id == 11000350)
		{
			//账户里没有持仓
			std::cout position_security_type)
            query_allotment_buffer_.push_back(*investor_position);
    }

    if (is_last) {
		/// 两份缓存数据发送至UI线程

		// 缓存发送后清空容器
        query_stk_position_buffer_.clear();
        query_allotment_buffer_.clear();
    }
}
```

 5.触发函数
```cpp
// 请求查询投资者持仓
virtual int QueryPosition(const char *ticker, uint64_t session_id, int request_id, XTP_MARKET_TYPE market = XTP_MKT_INIT) = 0;
```


### 17. OnQueryAsset


请求查询资金账户响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryAsset(XTPQueryAssetRsp *asset, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

Asset：查询到的资金账户情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///账户资金查询响应结构体
struct XTPQueryAssetRsp
{
    ///总资产（现货账户/期权账户参考公式：总资产 = 可用资金 + 证券资产（目前为0）+ 预扣的资金），（信用账户参考公式：总资产 = 可用资金 + 融券卖出所得资金余额 + 证券资产+ 预扣的资金）
    double total_asset;
    ///可用资金
    double buying_power;
    ///证券资产（保留字段，目前为0）
    double security_asset;
    ///累计买入成交证券占用资金（仅限现货账户/期权账户，信用账户暂不可用）
    double fund_buy_amount;
    ///累计买入成交交易费用（仅限现货账户/期权账户，信用账户暂不可用）
    double fund_buy_fee;
    ///累计卖出成交证券所得资金（仅限现货账户/期权账户，信用账户暂不可用）
    double fund_sell_amount;
    ///累计卖出成交交易费用（仅限现货账户/期权账户，信用账户暂不可用）
    double fund_sell_fee;
    ///XTP系统预扣的资金（包括买卖股票时预扣的交易资金+预扣手续费）
    double withholding_amount;
    ///账户类型
    XTP_ACCOUNT_TYPE account_type;

    ///冻结的保证金（仅限期权账户）
    double frozen_margin;
    ///行权冻结资金（仅限期权账户）
    double frozen_exec_cash;
    ///行权费用（仅限期权账户）
    double frozen_exec_fee;
    ///垫付资金（仅限期权账户）
    double pay_later;
    ///预垫付资金（仅限期权账户）
    double preadva_pay;
    ///昨日余额（仅限期权账户）
    double orig_banlance;
    ///当前余额（仅限期权账户）
    double banlance;
    ///当天出入金（仅限期权账户）
    double deposit_withdraw;
    ///当日交易资金轧差（仅限期权账户）
    double trade_netting;
    ///资金资产（仅限期权账户）
    double captial_asset;

    ///强锁资金（仅限期权账户）
    double force_freeze_amount;
    ///可取资金（仅限期权账户）
    double preferred_amount;

    // 信用业务新增字段开始（数量1）
    ///融券卖出所得资金余额（仅限信用账户，只能用于买券还券）
    double repay_stock_aval_banlance;

    // 信用业务新增字段结束（数量1）

    ///累计订单流量费
    double fund_order_data_charges;
    ///累计撤单流量费
    double fund_cancel_data_charges;
    //流量费统计新增字段结束（数量2）

    ///交易所实时风险度（仅限期权账户,后续服务器版本支持，目前为0）
    double exchange_cur_risk_degree;
    ///公司实时风险度（仅限期权账户,后续服务器版本支持，目前为0）
    double company_cur_risk_degree;
    //风险度新增字段结束（数量2）

    ///(保留字段)
    uint64_t unknown[43 - 12 - 1 - 2 - 2];
};
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询资产
virtual int QueryAsset(uint64_t session_id, int request_id) = 0;
```


### 18. OnQueryStructuredFund


请求查询分级基金信息响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryStructuredFund(XTPStructuredFundInfo *fund_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

fund_info：查询到的分级基金情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///查询分级基金信息响应结构体
struct XTPStructuredFundInfo
{
    XTP_EXCHANGE_TYPE   exchange_id;  ///<交易所代码
	char                sf_ticker[XTP_TICKER_LEN];   ///<分级基金母基金代码
	char                sf_ticker_name[XTP_TICKER_NAME_LEN]; ///<分级基金母基金名称
    char                ticker[XTP_TICKER_LEN];   ///<分级基金子基金代码
    char                ticker_name[XTP_TICKER_NAME_LEN]; ///<分级基金子基金名称
	XTP_SPLIT_MERGE_STATUS	split_merge_status;   ///<基金允许拆分合并状态
    uint32_t            ratio; ///<拆分合并比例
    uint32_t            min_split_qty;///<最小拆分数量
    uint32_t            min_merge_qty; ///<最小合并数量
    double              net_price;///<基金净值
}
```
```cpp
///XTP_EXCHANGE_TYPE是交易所类型，行情里使用
typedef enum XTP_EXCHANGE_TYPE
{
	XTP_EXCHANGE_SH = 1,	///<上证
	XTP_EXCHANGE_SZ,		///<深证
	XTP_EXCHANGE_NQ,		///<新三板 全国中小企业股份转让系统
    XTP_EXCHANGE_UNKNOWN	///<不存在的交易所类型
}XTP_EXCHANGE_TYPE;
```
```cpp
///XTP_SPLIT_MERGE_STATUS是一个基金当天拆分合并状态类型
typedef enum XTP_SPLIT_MERGE_STATUS {
	XTP_SPLIT_MERGE_STATUS_ALLOW = 0,	///<允许拆分和合并
	XTP_SPLIT_MERGE_STATUS_ONLY_SPLIT,	///<只允许拆分，不允许合并
	XTP_SPLIT_MERGE_STATUS_ONLY_MERGE,	///<只允许合并，不允许拆分
	XTP_SPLIT_MERGE_STATUS_FORBIDDEN	///<不允许拆分合并
}XTP_SPLIT_MERGE_STATUS;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
/// 存放证券名称的字符串长度
#define XTP_TICKER_NAME_LEN 64
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询分级基金
virtual int QueryStructuredFund(XTPQueryStructuredFundInfoReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 19. OnQueryFundTransfer


请求查询资金划拨订单响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryFundTransfer(XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

fund_transfer_info：查询到的资金账户情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///资金内转流水通知
struct XTPFundTransferNotice
{
    ///资金内转编号
    uint64_t	            serial_id;
    ///内转类型
    XTP_FUND_TRANSFER_TYPE	transfer_type;
    ///金额
    double	                amount;
    ///操作结果
    XTP_FUND_OPER_STATUS    oper_status;
    ///操作时间
    uint64_t	            transfer_time;
};
```
```cpp
///XTP_FUND_TRANSFER_TYPE是资金流转方向类型
typedef enum XTP_FUND_TRANSFER_TYPE
{
    XTP_FUND_TRANSFER_OUT = 0,		///<转出 从XTP转出到柜台
    XTP_FUND_TRANSFER_IN,	        ///<转入 从柜台转入XTP
    XTP_FUND_INTER_TRANSFER_OUT,    ///<跨节点转出 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨，只能跨账户用户使用
    XTP_FUND_INTER_TRANSFER_IN,     ///<跨节点转入 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨，只能跨账户用户使用
    XTP_FUND_INTER_TRANSFER_REPAY_OUT, ///<跨节点转出 融券卖出资金 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    XTP_FUND_INTER_TRANSFER_REPAY_IN, ///<跨节点转入 融券卖出资金 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    XTP_FUND_INTER_TRANSFER_CONTRACT_OUT, ///<跨节点转出 授信额度 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    XTP_FUND_INTER_TRANSFER_CONTRACT_IN, ///<跨节点转入 授信额度 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    XTP_FUND_TRANSFER_UNKNOWN		///<未知类型
}XTP_FUND_TRANSFER_TYPE;
```
```cpp
///XTP_FUND_OPER_STATUS柜台资金操作结果
typedef enum XTP_FUND_OPER_STATUS {
    XTP_FUND_OPER_PROCESSING = 0,	///<XTP已收到，正在处理中
    XTP_FUND_OPER_SUCCESS,			///<成功
    XTP_FUND_OPER_FAILED,			///<失败
    XTP_FUND_OPER_SUBMITTED,		///<已提交到集中柜台处理
    XTP_FUND_OPER_UNKNOWN			///<未知
}XTP_FUND_OPER_STATUS;
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询资金划拨
virtual int QueryFundTransfer(XTPQueryFundTransferLogReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 20. OnFundTransfer


资金划拨通知。

当资金划拨订单有状态变化的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的资金划拨通知。

 1.函数原型
```cpp
virtual void OnFundTransfer(XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info, uint64_t session_id) {};
```
 2.参数

fund_transfer_info：资金划拨通知的具体信息，用户可以通过fund_transfer_info.serial_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单

error_info：资金划拨订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误。当资金划拨方向为一号两中心节点之间划拨，且error_info.error_id=11000384时，error_info.error_msg为结点中可用于划拨的资金（以整数为准），用户需进行stringToInt的转化，可据此填写合适的资金，再次发起划拨请求

request_id：用于用户定位查询响应的ID，由用户自定义

session_id：资金账户对应的session_id，登录时得到

```cpp
///资金内转流水通知
struct XTPFundTransferNotice
{
    ///资金内转编号
    uint64_t	            serial_id;
    ///内转类型
    XTP_FUND_TRANSFER_TYPE	transfer_type;
    ///金额
    double	                amount;
    ///操作结果
    XTP_FUND_OPER_STATUS    oper_status;
    ///操作时间
    uint64_t	            transfer_time;
};
```

 3.返回

无

 4.触发函数
```cpp
// 资金划拨请求
virtual uint64_t FundTransfer(XTPFundTransferReq *fund_transfer, uint64_t session_id) = 0;
```


### 21. OnQueryOtherServerFund


请求查询其他节点可用资金的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryOtherServerFund(XTPFundQueryRsp *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) {};
```
 2.参数

fund_info：查询到的其他节点可用资金情况

error_info：查询到的其他节点可用资金情况发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

session_id：资金账户对应的session_id，登录时得到

```cpp
///用户资金查询响应结构体
struct XTPFundQueryRsp
{
	///金额
	double        amount;
	///查询类型
	XTP_FUND_QUERY_TYPE	query_type;
	///预留字段，用户无需填写
	uint64_t	unknown[4];

};
```
```cpp
///XTP_FUND_QUERY_TYPE是柜台资金查询类型
typedef enum XTP_FUND_QUERY_TYPE
{
	XTP_FUND_QUERY_JZ = 0,		///<查询金证主柜台可转资金
	XTP_FUND_QUERY_INTERNAL,	///<查询一账号两中心设置时，对方节点的资金
	XTP_FUND_QUERY_INTERNAL_REPAY,	///<查询一账号两中心设置时，对方节点的融券卖余额资金
	XTP_FUND_QUERY_INTERNAL_CONTRACT, ///<查询一账号两中心设置时，对方节点的授信额度
	XTP_FUND_QUERY_UNKNOWN		///<未知类型
}XTP_FUND_QUERY_TYPE;
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询其他节点可用资金
virtual int QueryOtherServerFund(XTPFundQueryReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 22. OnQueryETF


请求查询ETF清单文件的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryETF(XTPQueryETFBaseRsp *etf_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

etf_info：查询到的ETF清单文件情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///查询股票ETF合约基本情况--响应结构体
typedef struct XTPQueryETFBaseRsp
{
    XTP_MARKET_TYPE     market;                             ///<交易市场
    char                etf[XTP_TICKER_LEN];                ///<etf代码,买卖,申赎统一使用该代码
    char                subscribe_redemption_ticker[XTP_TICKER_LEN];    ///<etf申购赎回代码
    int32_t             unit;                               ///<最小申购赎回单位对应的ETF份数,例如上证"50ETF"就是900000
    int32_t             subscribe_status;                   ///<是否允许申购,1-允许,0-禁止
    int32_t             redemption_status;                  ///<是否允许赎回,1-允许,0-禁止
    double              max_cash_ratio;                     ///<最大现金替代比例,小于1的数值   TODO 是否采用double
    double              estimate_amount;                    ///<T日预估金额差额
    double              cash_component;                     ///<T-X日现金差额
    double              net_value;                          ///<基金单位净值
    double              total_amount;                       ///<最小申赎单位净值总金额=net_value*unit
}XTPQueryETFBaseRsp;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询ETF清单文件
virtual int QueryETF(XTPQueryETFBaseReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 23. OnQueryETFBasket


请求查询ETF股票篮的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryETFBasket(XTPQueryETFComponentRsp *etf_component_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

etf_component_info：查询到的ETF合约的相关成分股信息

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///查询股票ETF成分股信息--响应结构体
struct XTPQueryETFComponentRsp
{
    ///交易市场
    XTP_MARKET_TYPE     market;
    ///ETF代码
    char                ticker[XTP_TICKER_LEN];
    ///成份股代码
    char                component_ticker[XTP_TICKER_LEN];
    ///成份股名称
    char                component_name[XTP_TICKER_NAME_LEN];
    ///成份股数量
    int64_t             quantity;
    ///成份股交易市场
    XTP_MARKET_TYPE     component_market;
    ///成份股替代标识
    ETF_REPLACE_TYPE    replace_type;
    ///溢价比例
    double              premium_ratio;
    ///成分股替代标识为必须现金替代时候的总金额
    double              amount;
    ///申购溢价比例
    double              creation_premium_ratio;
    ///赎回溢价比例
    double              redemption_discount_ratio;
    ///申购时，成分股替代标识为必须现金替代时候的总金额
    double              creation_amount;
    ///赎回时，成分股替代标识为必须现金替代时候的总金额
    double              redemption_amount;

};

///ETF_REPLACE_TYPE现金替代标识定义
typedef enum ETF_REPLACE_TYPE
{
    ERT_CASH_FORBIDDEN = 0,             ///<禁止现金替代
    ERT_CASH_OPTIONAL,                  ///<可以现金替代
    ERT_CASH_MUST,                      ///<必须现金替代
    ERT_CASH_RECOMPUTE_INTER_SZ,        ///<深市退补现金替代
    ERT_CASH_MUST_INTER_SZ,             ///<深市必须现金替代
    ERT_CASH_RECOMPUTE_INTER_OTHER,     ///<非沪深市场成分证券退补现金替代（不适用于跨沪深港ETF产品）
    ERT_CASH_MUST_INTER_OTHER,          ///<表示非沪深市场成份证券必须现金替代（不适用于跨沪深港ETF产品）
    ERT_CASH_RECOMPUTE_INTER_HK,	    ///港市退补现金替代（仅适用于跨沪深港ETF产品）
    ERT_CASH_MUST_INTER_HK,		        ///港市必须现金替代（仅适用于跨沪深港ETF产品）
    EPT_INVALID                         ///<无效值
}ETF_REPLACE_TYPE;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
/// 存放证券名称的字符串长度
#define XTP_TICKER_NAME_LEN 64
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询ETF股票篮
virtual int QueryETFTickerBasket(XTPQueryETFComponentReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 24. OnQueryIPOInfoList


请求查询今日新股申购信息列表的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

ipo_info 查询到的今日新股申购的一只股票信息

error_info：查询今日新股申购信息列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///查询当日可申购新股信息
struct XTPQueryIPOTickerRsp {
    ///交易市场
    XTP_MARKET_TYPE     market;
    ///申购代码
    char                ticker[XTP_TICKER_LEN];
    ///申购股票名称
    char                ticker_name[XTP_TICKER_NAME_LEN];
    /// 证券类别
    XTP_TICKER_TYPE     ticker_type;
    ///申购价格
    double              price;
    ///申购单元
    int32_t             unit;
    ///最大允许申购数量
    int32_t             qty_upper_limit;
};
```
```cpp
///XTP_TICKER_TYPE证券类型
typedef enum XTP_TICKER_TYPE
{
	XTP_TICKER_TYPE_STOCK = 0,            ///<普通股票
	XTP_TICKER_TYPE_INDEX,                ///<指数
	XTP_TICKER_TYPE_FUND,                 ///<基金
	XTP_TICKER_TYPE_BOND,                 ///<债券
	XTP_TICKER_TYPE_OPTION,               ///<期权
    XTP_TICKER_TYPE_TECH_STOCK,           ///<科创板股票（上海）
	XTP_TICKER_TYPE_UNKNOWN               ///<未知类型
}XTP_TICKER_TYPE;
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询今日新股申购信息列表
virtual int QueryIPOInfoList(uint64_t session_id, int request_id) = 0;
```


### 25. OnQueryIPOQuotaInfo


请求查询用户新股申购额度信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryIPOQuotaInfo(XTPQueryIPOQuotaRsp *quota_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

quota_info：查询到的用户某个市场的今日新股申购额度信息

error_info：查询用户新股申购额度信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///查询用户申购额度-包含创业板额度
struct XTPQueryIPOQuotaRsp {
    ///交易市场
    XTP_MARKET_TYPE     market;
    ///可申购额度
    int32_t             quantity;
    /// 上海科创板额度
    int32_t             tech_quantity;
    /// 保留
    int32_t             unused;
};
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询用户新股申购额度信息
virtual int QueryIPOQuotaInfo(uint64_t session_id, int request_id) = 0;
```


### 26. OnQueryBondIPOInfoList


请求查询今日可转债申购信息列表的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

1.函数原型
```cpp
virtual void OnQueryBondIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```

2.参数

ipo_info：查询到的今日可转债申购的可转债信息

error_info：查询用户今日可转债申购信息列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到
```cpp
///查询当日可申购新股信息
struct XTPQueryIPOTickerRsp {
    ///交易市场
    XTP_MARKET_TYPE     market;
    ///申购代码
    char                ticker[XTP_TICKER_LEN];
    ///申购股票名称
    char                ticker_name[XTP_TICKER_NAME_LEN];
    /// 证券类别
    XTP_TICKER_TYPE     ticker_type;
    ///申购价格
    double              price;
    ///申购单元
    int32_t             unit;
    ///最大允许申购数量
    int32_t             qty_upper_limit;
};
```
```cpp
///XTP_TICKER_TYPE证券类型
typedef enum XTP_TICKER_TYPE
{
	XTP_TICKER_TYPE_STOCK = 0,            ///<普通股票
	XTP_TICKER_TYPE_INDEX,                ///<指数
	XTP_TICKER_TYPE_FUND,                 ///<基金
	XTP_TICKER_TYPE_BOND,                 ///<债券
	XTP_TICKER_TYPE_OPTION,               ///<期权
    XTP_TICKER_TYPE_TECH_STOCK,           ///<科创板股票（上海）
	XTP_TICKER_TYPE_UNKNOWN               ///<未知类型
}XTP_TICKER_TYPE;
```

3.返回

无

4.触发函数
```cpp
// 请求查询用户今日可转债申购信息
virtual int QueryBondIPOInfoList(uint64_t session_id, int request_id) = 0;
```


### 27. OnQueryBondSwapStockInfo


请求查询用户可转债转股信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryBondSwapStockInfo(XTPQueryBondSwapStockRsp *swap_stock_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

swap_stock_info: 查询到某条可转债转股信息

error_info：查询可转债信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///用户债转股信息结构体
typedef struct XTPQueryBondSwapStockRsp
{
    XTP_MARKET_TYPE    market;                  // 交易市场
    char   ticker[XTP_TICKER_LEN];              // 债券证券代码
    char underlying_ticker[XTP_TICKER_LEN];     // 转股后的股票证券代码
    int32_t unit;                               // 转换数量单位（张）
    int64_t qty_min;                            // 最小下单量（张）
    int64_t qty_max;                            // 最大下单量（张）
    double swap_price;                          // 转股价格
    int32_t swap_flag;                          // 是否处于转股期；0: 不可转股；1：可转股；
}XTPQueryBondSwapStockRsp;
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询用户债转股信息
virtual int QueryBondSwapStockInfo(XTPQueryBondSwapStockReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 28. OnQueryOptionAuctionInfo


请求查询期权合约的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryOptionAuctionInfo(XTPQueryOptionAuctionInfoRsp *option_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

option_info：查询到的期权合约情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///查询期权竞价交易业务参考信息
struct XTPQueryOptionAuctionInfoRsp {
    char                ticker[XTP_TICKER_LEN];             ///<合约编码，报单ticker采用本字段
    XTP_MARKET_TYPE     security_id_source;                 ///<证券代码源
    char                symbol[XTP_TICKER_NAME_LEN];        ///<合约简称
    char                contract_id[XTP_TICKER_NAME_LEN];   ///<合约交易代码
    char                underlying_security_id[XTP_TICKER_LEN]; ///<基础证券代码
	XTP_MARKET_TYPE     underlying_security_id_source;      ///<基础证券代码源

    uint32_t            list_date;                          ///<上市日期，格式为YYYYMMDD
    uint32_t            last_trade_date;                    ///<最后交易日，格式为YYYYMMDD
    XTP_TICKER_TYPE     ticker_type;                        ///<证券类别
    int32_t             day_trading;                        ///<是否支持当日回转交易，1-允许，0-不允许

    XTP_OPT_CALL_OR_PUT_TYPE    call_or_put;                ///<认购或认沽
    uint32_t            delivery_day;                       ///<行权交割日，格式为YYYYMMDD
    uint32_t            delivery_month;                     ///<交割月份，格式为YYYYMM

    XTP_OPT_EXERCISE_TYPE_TYPE  exercise_type;              ///<行权方式
    uint32_t            exercise_begin_date;                ///<行权起始日期，格式为YYYYMMDD
    uint32_t            exercise_end_date;                  ///<行权结束日期，格式为YYYYMMDD
    double              exercise_price;                     ///<行权价格

    int64_t             qty_unit;                           ///<数量单位，对于某一证券申报的委托，其委托数量字段必须为该证券数量单位的整数倍
    int64_t             contract_unit;                      ///<合约单位
    int64_t             contract_position;                  ///<合约持仓量

    double              prev_close_price;                   ///<合约前收盘价
    double              prev_clearing_price;                ///<合约前结算价

    int64_t             lmt_buy_max_qty;                    ///<限价买最大量
    int64_t             lmt_buy_min_qty;                    ///<限价买最小量
    int64_t             lmt_sell_max_qty;                   ///<限价卖最大量
    int64_t             lmt_sell_min_qty;                   ///<限价卖最小量
    int64_t             mkt_buy_max_qty;                    ///<市价买最大量
    int64_t             mkt_buy_min_qty;                    ///<市价买最小量
    int64_t             mkt_sell_max_qty;                   ///<市价卖最大量
    int64_t             mkt_sell_min_qty;                   ///<市价卖最小量

    double              price_tick;                         ///<最小报价单位
    double              upper_limit_price;                  ///<涨停价
    double              lower_limit_price;                  ///<跌停价
    double              sell_margin;                        ///<今卖开每张保证金
    double              margin_ratio_param1;                ///<交易所保证金比例计算参数一
    double              margin_ratio_param2;                ///<交易所保证金比例计算参数二

    uint64_t            unknown[20];                        ///<（保留字段）
};
```
```cpp
///XTP_TICKER_TYPE证券类型
typedef enum XTP_TICKER_TYPE
{
	XTP_TICKER_TYPE_STOCK = 0,            ///<普通股票
	XTP_TICKER_TYPE_INDEX,                ///<指数
	XTP_TICKER_TYPE_FUND,                 ///<基金
	XTP_TICKER_TYPE_BOND,                 ///<债券
	XTP_TICKER_TYPE_OPTION,               ///<期权
    XTP_TICKER_TYPE_TECH_STOCK,           ///<科创板股票（上海）
	XTP_TICKER_TYPE_UNKNOWN               ///<未知类型

}XTP_TICKER_TYPE;
```
```cpp
///XTP_OPT_CALL_OR_PUT_TYPE是一个认沽或认购类型
typedef enum XTP_OPT_CALL_OR_PUT_TYPE {
	XTP_OPT_CALL = 1,	    ///<认购
	XTP_OPT_PUT = 2,		///<认沽
}XTP_OPT_CALL_OR_PUT_TYPE;
```
```cpp
///XTP_OPT_EXERCISE_TYPE_TYPE是一个行权方式类型
typedef enum XTP_OPT_EXERCISE_TYPE_TYPE {
	XTP_OPT_EXERCISE_TYPE_EUR = 1,	    ///<欧式
	XTP_OPT_EXERCISE_TYPE_AME = 2,		///<美式
}XTP_OPT_EXERCISE_TYPE_TYPE;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
/// 存放证券名称的字符串长度
#define XTP_TICKER_NAME_LEN 64
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询期权合约
virtual int QueryOptionAuctionInfo(XTPQueryOptionAuctionInfoReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 29. OnCreditCashRepay


融资融券业务中现金直接还款的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnCreditCashRepay(XTPCrdCashRepayRsp *cash_repay_info, XTPRI *error_info, uint64_t session_id) {};
```
 2.参数

cash_repay_info：现金直接还款通知的具体信息，用户可以通过cash_repay_info.xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

session_id：资金账户对应的session_id，登录时得到

```cpp
///融资融券直接还款响应信息
struct XTPCrdCashRepayRsp
{
    int64_t xtp_id;             ///< 直接还款操作的XTPID
    double  request_amount;     ///< 直接还款的申请金额
    double  cash_repay_amount;  ///< 实际还款使用金额
};
```

 3.返回

无

 4.触发函数
```cpp
// 融资融券业务中现金直接还款请求
virtual uint64_t CreditCashRepay(double amount, uint64_t session_id) = 0;
```


### 30. OnCreditCashRepayDebtInterestFee


融资融券业务中现金还息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnCreditCashRepayDebtInterestFee(XTPCrdCashRepayDebtInterestFeeRsp *cash_repay_info, XTPRI *error_info, uint64_t session_id) {};
```
 2.参数

cash_repay_info：现金还息通知的具体信息，用户可以通过cash_repay_info.xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单

error_info：现金还息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

session_id：资金账户对应的session_id，登录时得到

```cpp
///融资融券现金还息费响应信息
struct XTPCrdCashRepayDebtInterestFeeRsp
{
	int64_t xtp_id;             ///< 直接还款操作的XTPID
	double  request_amount;     ///< 直接还款的申请金额
	double  cash_repay_amount;  ///< 实际还款使用金额
	char	debt_compact_id[XTP_CREDIT_DEBT_ID_LEN]; ///< 指定的负债合约编号
	char	unknow[32];			///< 保留字段
};
```
```cpp
/// 信用业务合约负债编号长度
#define XTP_CREDIT_DEBT_ID_LEN 33
```

 3.返回

无

 4.触发函数
```cpp
// 融资融券业务中现金还指定负债合约息费请求
virtual uint64_t CreditCashRepayDebtInterestFee(const char* debt_id, double amount, uint64_t session_id) = 0;
```


### 31. OnQueryCreditCashRepayInfo


请求查询融资融券业务中的现金直接还款报单的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditCashRepayInfo(XTPCrdCashRepayInfo *cash_repay_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

cash_repay_info 查询到的某一笔现金直接还款通知的具体信息

error_info：查询现金直接报单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///单条融资融券直接还款记录信息
struct XTPCrdCashRepayInfo
{
    int64_t                     xtp_id;             ///< 直接还款操作的XTPID
    XTP_CRD_CR_STATUS           status;             ///< 直接还款处理状态
    double                      request_amount;     ///< 直接还款的申请金额
    double                      cash_repay_amount;  ///< 实际还款使用金额
    XTP_POSITION_EFFECT_TYPE    position_effect;    ///< 强平标志
	XTPRI						error_info;			///< 直接还款发生错误时的错误信息
};
```
```cpp
///XTP_CRD_CASH_REPAY_STATUS是一个融资融券直接还款状态类型
typedef enum XTP_CRD_CR_STATUS {
    XTP_CRD_CR_INIT = 0,        ///< 初始、未处理状态
    XTP_CRD_CR_SUCCESS,         ///< 已成功处理状态
    XTP_CRD_CR_FAILED,          ///< 处理失败状态
} XTP_CRD_CR_STATUS;
```
```cpp
///XTP_POSITION_EFFECT_TYPE是开平标识类型
typedef uint8_t XTP_POSITION_EFFECT_TYPE;

/// 初始值或未知值开平标识，除期权外，均使用此值
#define XTP_POSITION_EFFECT_INIT                0
/// 开
#define XTP_POSITION_EFFECT_OPEN                1
/// 平
#define XTP_POSITION_EFFECT_CLOSE               2
/// 强平
#define XTP_POSITION_EFFECT_FORCECLOSE          3
/// 平今
#define XTP_POSITION_EFFECT_CLOSETODAY          4
/// 平昨
#define XTP_POSITION_EFFECT_CLOSEYESTERDAY      5
/// 强减
#define XTP_POSITION_EFFECT_FORCEOFF            6
/// 本地强平
#define XTP_POSITION_EFFECT_LOCALFORCECLOSE     7
/// 信用业务追保强平
#define XTP_POSITION_EFFECT_CREDIT_FORCE_COVER  8
/// 信用业务清偿强平
#define XTP_POSITION_EFFECT_CREDIT_FORCE_CLEAR  9
/// 信用业务合约到期强平
#define XTP_POSITION_EFFECT_CREDIT_FORCE_DEBT   10
/// 信用业务无条件强平
#define XTP_POSITION_EFFECT_CREDIT_FORCE_UNCOND 11
/// 未知的开平标识类型
#define XTP_POSITION_EFFECT_UNKNOWN             12
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询融资融券业务中的现金直接还款报单
virtual int QueryCreditCashRepayInfo(uint64_t session_id, int request_id) = 0;
```


### 32. OnQueryCreditFundInfo


请求查询信用账户额外信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditFundInfo(XTPCrdFundInfo *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) {};
```
 2.参数

fund_info：查询到的信用账户额外信息情况

error_info：查询信用账户额外信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

session_id：资金账户对应的session_id，登录时得到

```cpp
///融资融券特有帐户数据
typedef struct XTPCrdFundInfo
{
    double maintenance_ratio;       ///< 维持担保品比例
    double all_asset;               ///< 总资产(包含证券资产)
    double all_debt;                ///< 总负债
    double line_of_credit;          ///< 两融授信额度
    double guaranty;                ///< 两融保证金可用数
    double reserved;                ///< 保留字段
}XTPCrdFundInfo;
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询信用账户特有信息，除资金账户以外的信息
virtual int QueryCreditFundInfo(uint64_t session_id, int request_id) = 0;
```


### 33. OnQueryCreditDebtInfo


请求查询信用账户负债信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditDebtInfo(XTPCrdDebtInfo *debt_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

debt_info：查询到的信用账户合约负债情况

error_info：查询信用账户负债信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///单条融资融券负债记录信息
typedef struct XTPCrdDebtInfo
{
    int32_t             debt_type;              ///< 负债合约类型：0为融资，1为融券，2未知
    char                debt_id[33];            ///< 负债合约编号
    int64_t             position_id;            ///< 负债对应两融头寸编号
    uint64_t            order_xtp_id;           ///< 生成负债的订单编号，非当日负债无此项
    int32_t             debt_status;            ///< 负债合约状态：0为未偿还或部分偿还，1为已偿还，2为过期未平仓，3未知
    XTP_MARKET_TYPE     market;                 ///< 市场
    char                ticker[XTP_TICKER_LEN]; ///< 证券代码
    uint64_t            order_date;             ///< 委托日期
    uint64_t            end_date;               ///< 负债截止日期
    uint64_t            orig_end_date;          ///< 负债原始截止日期
    bool                is_extended;            ///< 当日是否接收到展期请求：false为没收到，true为收到
    double              remain_amt;             ///< 未偿还金额
    int64_t             remain_qty;             ///< 未偿还融券数量
    double              remain_principal;       ///< 未偿还本金金额
	int64_t				due_right_qty;			///< 应偿还权益数量
	int64_t				unknown[2];				///< 保留字段
}XTPCrdDebtInfo;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询信用账户负债合约信息
virtual int QueryCreditDebtInfo(uint64_t session_id, int request_id) = 0;
```


### 34. OnQueryCreditTickerDebtInfo


请求查询信用账户指定证券负债未还信息响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditTickerDebtInfo(XTPCrdDebtStockInfo *debt_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

debt_info：查询到的信用账户指定证券负债未还信息情况

error_info：查询信用账户指定证券负债未还信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///融资融券指定证券的融券负债相关信息
typedef struct XTPCrdDebtStockInfo
{
    XTP_MARKET_TYPE market;                     ///< 市场
    char            ticker[XTP_TICKER_LEN];     ///< 证券代码
    int64_t         stock_repay_quantity;       ///< 融券负债可还券数量
    int64_t         stock_total_quantity;       ///< 融券负债未还总数量
}XTPCrdDebtStockInfo;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询指定证券负债未还信息
virtual int QueryCreditTickerDebtInfo(XTPClientQueryCrdDebtStockReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 35. OnQueryCreditAssetDebtInfo


请求查询信用账户待还资金的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditAssetDebtInfo(double remain_amount, XTPRI *error_info, int request_id, uint64_t session_id) {};
```
 2.参数

remain_amount：查询到的信用账户待还资金

error_info：查询信用账户待还资金发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

session_id：资金账户对应的session_id，登录时得到

 3.返回

无

 4.触发函数
```cpp
// 请求查询信用账户待还资金信息
virtual int QueryCreditAssetDebtInfo(uint64_t session_id, int request_id) = 0;
```


### 36. OnQueryCreditTickerAssignInfo


请求查询信用账户可融券头寸信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditTickerAssignInfo(XTPClientQueryCrdPositionStkInfo *assign_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

assign_info：查询到的信用账户可融券头寸信息

error_info：查询信用账户可融券头寸信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///融券头寸证券信息
typedef struct XTPClientQueryCrdPositionStkInfo
{
    XTP_MARKET_TYPE market;                 ///< 证券市场
    char            ticker[XTP_TICKER_LEN]; ///< 证券代码
    int64_t         limit_qty;              ///< 融券限量(保留字段)
    int64_t         yesterday_qty;          ///< 昨日日融券数量(保留字段)
    int64_t         left_qty;               ///< 剩余可融券数量
    int64_t         frozen_qty;             ///< 冻结融券数量(保留字段)
}XTPClientQueryCrdPositionStkInfo;
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询信用账户可融券头寸信息
virtual int QueryCreditTickerAssignInfo(XTPClientQueryCrdPositionStockReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 37. OnQueryCreditExcessStock


融资融券业务中请求查询指定余券信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditExcessStock(XTPClientQueryCrdSurplusStkRspInfo* stock_info, XTPRI *error_info, int request_id, uint64_t session_id) {};
```
 2.参数

stock_info：查询到的余券信息

error_info：查询信用账户余券信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

session_id：资金账户对应的session_id，登录时得到

```cpp
///信用业务余券信息
typedef struct XTPClientQueryCrdSurplusStkRspInfo
{
    XTP_MARKET_TYPE market;                 ///< 证券市场
    char            ticker[XTP_TICKER_LEN]; ///< 证券代码
    int64_t         transferable_quantity;  ///< 可划转数量
    int64_t         transferred_quantity;   ///< 已划转数量
}XTPClientQueryCrdSurplusStkRspInfo;
```

 3.返回

无

 4.触发函数
```cpp
// 融资融券业务中请求查询指定证券的余券
virtual int QueryCreditExcessStock(XTPClientQueryCrdSurplusStkReqInfo *query_param, uint64_t session_id, int request_id) = 0;
```


### 38. OnQueryMulCreditExcessStock


融资融券业务中请求查询余券信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryMulCreditExcessStock(XTPClientQueryCrdSurplusStkRspInfo* stock_info, XTPRI *error_info, int request_id, uint64_t session_id, bool is_last) {};
```
 2.参数

stock_info：查询到的余券信息

error_info：查询信用账户余券信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///信用业务余券信息
typedef struct XTPClientQueryCrdSurplusStkRspInfo
{
    XTP_MARKET_TYPE market;                 ///< 证券市场
    char            ticker[XTP_TICKER_LEN]; ///< 证券代码
    int64_t         transferable_quantity;  ///< 可划转数量
    int64_t         transferred_quantity;   ///< 已划转数量
}XTPClientQueryCrdSurplusStkRspInfo;
```

 3.返回

无

 4.触发函数
```cpp
// 融资融券业务中请求查询余券
virtual int QueryMulCreditExcessStock(XTPClientQueryCrdSurplusStkReqInfo *query_param, uint64_t session_id, int request_id) = 0;
```


### 39. OnCreditExtendDebtDate


融资融券业务中负债合约展期的通知。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnCreditExtendDebtDate(XTPCreditDebtExtendNotice *debt_extend_info, XTPRI *error_info, uint64_t session_id) {};
```
 2.参数

debt_extend_info：负债合约展期通知的具体信息，用户可以通过debt_extend_info.xtpid来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单

error_info：负债合约展期订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

session_id：资金账户对应的session_id，登录时得到

```cpp
///用户展期请求的通知
struct XTPCreditDebtExtendNotice
{
	uint64_t	xtpid;								///<XTP系统订单ID，无需用户填写，在XTP系统中唯一
	char		debt_id[XTP_CREDIT_DEBT_ID_LEN];	///<负债合约编号
	XTP_DEBT_EXTEND_OPER_STATUS		oper_status;	///<展期请求操作状态
	uint64_t	oper_time;							///<操作时间
};
```
```cpp
///XTP_DEBT_EXTEND_OPER_STATUS柜台负债展期操作状态
typedef enum XTP_DEBT_EXTEND_OPER_STATUS {
	XTP_DEBT_EXTEND_OPER_PROCESSING = 0,	///<XTP已收到，正在处理中
    XTP_DEBT_EXTEND_OPER_SUBMITTED,			///<已提交到集中柜台处理
	XTP_DEBT_EXTEND_OPER_SUCCESS,			///<成功
	XTP_DEBT_EXTEND_OPER_FAILED,			///<失败
	XTP_DEBT_EXTEND_OPER_UNKNOWN			///<未知
}XTP_DEBT_EXTEND_OPER_STATUS;
```
```cpp
/// 信用业务合约负债编号长度
#define XTP_CREDIT_DEBT_ID_LEN      33
```

 3.返回

无

 4.触发函数
```cpp
// 融资融券业务中请求负债合约展期
virtual uint64_t CreditExtendDebtDate(XTPCreditDebtExtendReq *debt_extend, uint64_t session_id) = 0;
```


### 40. OnQueryCreditExtendDebtDateOrders


请求查询负债合约展期订单响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditExtendDebtDateOrders(XTPCreditDebtExtendNotice *debt_extend_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

debt_extend_info：查询到的负债合约展期情况

error_info：查询负债合约展期发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///用户展期请求的通知
struct XTPCreditDebtExtendNotice
{
	uint64_t	xtpid;								///<XTP系统订单ID，无需用户填写，在XTP系统中唯一
	char		debt_id[XTP_CREDIT_DEBT_ID_LEN];	///<负债合约编号
	XTP_DEBT_EXTEND_OPER_STATUS		oper_status;	///<展期请求操作状态
	uint64_t	oper_time;							///<操作时间
};
```
```cpp
///XTP_DEBT_EXTEND_OPER_STATUS柜台负债展期操作状态
typedef enum XTP_DEBT_EXTEND_OPER_STATUS {
	XTP_DEBT_EXTEND_OPER_PROCESSING = 0,	///<XTP已收到，正在处理中
	XTP_DEBT_EXTEND_OPER_SUBMITTED,			///<已提交到集中柜台处理
	XTP_DEBT_EXTEND_OPER_SUCCESS,			///<成功
	XTP_DEBT_EXTEND_OPER_FAILED,			///<失败
	XTP_DEBT_EXTEND_OPER_UNKNOWN			///<未知
}XTP_DEBT_EXTEND_OPER_STATUS;
```
```cpp
/// 信用业务合约负债编号长度
#define XTP_CREDIT_DEBT_ID_LEN      33
```

 3.返回

无

 4.触发函数
```cpp
// 融资融券业务中请求查询负债合约展期
virtual int QueryCreditExtendDebtDateOrders(uint64_t xtp_id, uint64_t session_id, int request_id) = 0;
```


### 41. OnQueryCreditFundExtraInfo


查询融资融券业务中信用账户附加信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditFundExtraInfo(XTPCrdFundExtraInfo *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) {};
```
 2.参数

fund_info：信用账户附加信息

error_info：查询信用账户附加信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

session_id：资金账户对应的session_id，登录时得到

```cpp
/// 融资融券帐户附加信息
typedef struct XTPCrdFundExtraInfo
{
    double    mf_rs_avl_used;  ///<当前资金账户购买货币基金使用的融券卖出所得资金占用
	///证券市值
	double security_capital;
	///融资负债
	double financing_debts;
	///融券负债
	double short_sell_debts;
	///授信总额度
	double contract_debts_load;
    char      reserve[64-32];     ///<预留空间
}XTPCrdFundExtraInfo;
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询融资融券业务中账戶的附加信息
virtual int QueryCreditFundExtraInfo(uint64_t session_id, int request_id) = 0;
```


### 42. OnQueryCreditPositionExtraInfo


查询融资融券业务中信用账户指定证券的附加信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryCreditPositionExtraInfo(XTPCrdPositionExtraInfo *fund_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

fund_info：信用账户指定证券的附加信息

error_info：查询信用账户附加信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///融资融券帐户持仓附加信息
typedef struct XTPCrdPositionExtraInfo
{
    XTP_MARKET_TYPE market;                 ///<证券市场
    char            ticker[XTP_TICKER_LEN]; ///<证券代码
    double          mf_rs_avl_used;         ///<购买货币基金使用的融券卖出所得资金占用
    char            reserve[64];            ///<预留空间
}XTPCrdPositionExtraInfo;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询融资融券业务中账戶指定证券的附加信息
virtual int QueryCreditPositionExtraInfo(XTPClientQueryCrdPositionStockReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 43. OnOptionCombinedOrderEvent


期权组合策略报单通知。

每次订单状态更新时，都会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，在订单未成交、全部成交、全部撤单、部分撤单、已拒绝这些状态时会有响应，对于部分成交的情况，请由订单的成交回报来自行确认。所有登录了此用户的客户端都将收到此用户的订单响应。

 1.函数原型
```cpp
virtual void OnOptionCombinedOrderEvent(XTPOptCombOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};
```
 2.参数

order_info：订单响应具体信息，用户可以通过order_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单，order_info.qty_left字段在订单为未成交、部成、全成、废单状态时，表示此订单还没有成交的数量，在部撤、全撤状态时，表示此订单被撤的数量。order_info.order_cancel_xtp_id为其所对应的撤单ID，不为0时表示此单被撤成功

error_info：订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///期权组合策略报单响应结构体
struct XTPOptCombOrderInfo
{
    ///XTP系统订单ID，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，用户自定义
    uint32_t	            order_client_id;
    ///报单操作引用，用户自定义（暂未使用）
    uint32_t                order_cancel_client_id;
    ///撤单在XTP系统中的id，在XTP系统中唯一
    uint64_t                order_cancel_xtp_id;
    ///证券代码
    ///char                    ticker[XTP_TICKER_LEN];
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///数量，此订单的报单数量
    int64_t                 quantity;

    ///组合方向
    XTP_SIDE_TYPE               side;

    ///业务类型
    XTP_BUSINESS_TYPE       business_type;
    ///今成交数量，为此订单累计成交数量
    int64_t                 qty_traded;
    ///剩余数量，当撤单成功时，表示撤单数量
    int64_t                 qty_left;
    ///委托时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 insert_time;
    ///最后修改时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 update_time;
    ///撤销时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 cancel_time;
    ///成交金额，组合拆分涉及的保证金(保留字段)
    double                  trade_amount;
    ///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    ///报单状态，订单响应中没有部分成交状态的推送，在查询订单结果中，会有部分成交状态
    XTP_ORDER_STATUS_TYPE   order_status;
    ///报单提交状态，用户可用此字段来区分撤单和报单
    XTP_ORDER_SUBMIT_STATUS_TYPE   order_submit_status;
    ///报单类型
    TXTPOrderTypeType       order_type;

    ///期权组合策略信息
    XTPOptCombPlugin        opt_comb_info;
};
```
```cpp
///XTP_ORDER_STATUS_TYPE是报单状态类型
typedef enum XTP_ORDER_STATUS_TYPE
{
    XTP_ORDER_STATUS_INIT = 0,///<初始化
    XTP_ORDER_STATUS_ALLTRADED = 1,           ///<全部成交
    XTP_ORDER_STATUS_PARTTRADEDQUEUEING,  ///<部分成交
    XTP_ORDER_STATUS_PARTTRADEDNOTQUEUEING, ///<部分撤单
    XTP_ORDER_STATUS_NOTRADEQUEUEING,   ///<未成交
    XTP_ORDER_STATUS_CANCELED,  ///<已撤单
    XTP_ORDER_STATUS_REJECTED,  ///<已拒绝
    XTP_ORDER_STATUS_UNKNOWN  ///<未知订单状态
}XTP_ORDER_STATUS_TYPE;
```
```cpp
///XTP_ORDER_SUBMIT_STATUS_TYPE是报单提交状态类型
typedef enum XTP_ORDER_SUBMIT_STATUS_TYPE
{
    XTP_ORDER_SUBMIT_STATUS_INSERT_SUBMITTED = 1, ///<订单已经提交
    XTP_ORDER_SUBMIT_STATUS_INSERT_ACCEPTED,///<订单已经被接受
    XTP_ORDER_SUBMIT_STATUS_INSERT_REJECTED,///<订单已经被拒绝
    XTP_ORDER_SUBMIT_STATUS_CANCEL_SUBMITTED,///<撤单已经提交
    XTP_ORDER_SUBMIT_STATUS_CANCEL_REJECTED,///<撤单已经被拒绝
    XTP_ORDER_SUBMIT_STATUS_CANCEL_ACCEPTED ///<撤单已经被接受
}XTP_ORDER_SUBMIT_STATUS_TYPE;
```
```cpp
///TXTPOrderTypeType是报单类型类型
typedef char TXTPOrderTypeType;

///正常
#define XTP_ORDT_Normal '0'
///报价衍生
#define XTP_ORDT_DeriveFromQuote '1'
///组合衍生
#define XTP_ORDT_DeriveFromCombination '2'
///组合报单
#define XTP_ORDT_Combination '3'
///条件单
#define XTP_ORDT_ConditionalOrder '4'
///互换单
#define XTP_ORDT_Swap '5'
```
```cpp
///期权组合策略报单附加信息结构体
typedef struct XTPOptCombPlugin {
    char                                strategy_id[XTP_STRATEGY_ID_LEN];               ///< 组合策略代码，比如CNSJC认购牛市价差策略等。合并行权时，此字段可为空
    char                                comb_num[XTP_SECONDARY_ORDER_ID_LEN];           ///< 组合编码，组合申报时，该字段为空；拆分申报时，填写拟拆分组合的组合编码。
    int32_t                             num_legs;                                       ///< 成分合约数
    XTPOptCombLegInfo                   leg_detail[XTP_STRATEGE_LEG_NUM];               ///< 成分合约数组，最多四条腿。
}XTPOptCombPlugin;
```
```cpp
/// 组合策略腿合约信息结构体
typedef struct XTPOptCombLegInfo {
    char                            leg_security_id[XTP_TICKER_LEN]; ///< 成分合约代码
    XTP_OPT_CALL_OR_PUT_TYPE        leg_cntr_type;                   ///< 合约类型，认沽或认购。
    XTP_POSITION_DIRECTION_TYPE     leg_side;                        ///< 持仓方向，权利方或义务方。
    XTP_OPT_COVERED_OR_UNCOVERED    leg_covered;                     ///< 备兑标签
    int32_t                         leg_qty;                         ///< 成分合约数量（张）
}XTPOptCombLegInfo;
```
```cpp
/// XTP_OPT_CALL_OR_PUT_TYPE是一个认沽或认购类型
typedef enum XTP_OPT_CALL_OR_PUT_TYPE {
	XTP_OPT_CALL = 1,	    ///<认购
	XTP_OPT_PUT = 2,		///<认沽
}XTP_OPT_CALL_OR_PUT_TYPE;
```
```cpp
/// XTP_POSITION_DIRECTION_TYPE是一个持仓方向类型
typedef enum XTP_POSITION_DIRECTION_TYPE {
	XTP_POSITION_DIRECTION_NET = 0,	    ///<净
	XTP_POSITION_DIRECTION_LONG,		///<多（期权则为权利方）
    XTP_POSITION_DIRECTION_SHORT,       ///<空（期权则为义务方）
    XTP_POSITION_DIRECTION_COVERED,     ///<备兑（期权则为备兑义务方）
}XTP_POSITION_DIRECTION_TYPE;
```
```cpp
/// XTP_OPT_COVERED_OR_UNCOVERED是否备兑的标签
typedef enum XTP_OPT_COVERED_OR_UNCOVERED {
    XTP_POSITION_UNCOVERED = 0,     ///<非备兑
    XTP_POSITION_COVERED,           ///<备兑
}XTP_OPT_COVERED_OR_UNCOVERED;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
/// 本地报单编号的字符串长度
#define XTP_LOCAL_ORDER_LEN         11
/// 期权组合策略最多腿数
#define XTP_STRATEGE_LEG_NUM        4
/// 期权组合策略代码字符串长度
#define XTP_STRATEGY_ID_LEN         10
/// 期权组合策略组合编码字符串长度
#define XTP_SECONDARY_ORDER_ID_LEN  18
```

 3.返回

无

 4.触发函数
```cpp
// 期权组合策略报单录入请求
virtual uint64_t InsertOptionCombinedOrder(XTPOptCombOrderInsertInfo *order, uint64_t session_id) = 0;
// 期权组合策略报单撤单请求
virtual uint64_t CancelOptionCombinedOrder(const uint64_t order_xtp_id, uint64_t session_id) = 0;
```


### 44. OnOptionCombinedTradeEvent


期权组合策略成交通知。

订单有成交发生的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的成交回报。相关订单为部成状态，需要用户通过成交回报的成交数量来确定，OnOrderEvent()不会推送部成状态。

 1.函数原型
```cpp
virtual void OnOptionCombinedTradeEvent(XTPOptCombTradeReport *trade_info, uint64_t session_id) {};
```
 2.参数

trade_info：成交回报的具体信息，用户可以通过trade_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。对于上交所，exec_id可以唯一标识一笔成交。当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交了。对于深交所，exec_id是唯一的，暂时无此判断机制。report_index+market字段可以组成唯一标识表示成交回报

session_id：资金账户对应的session_id，登录时得到

```cpp
///期权组合策略报单成交结构体
struct XTPOptCombTradeReport
{
    ///XTP系统订单ID，此成交回报相关的订单ID，在XTP系统中唯一
    uint64_t                 order_xtp_id;
    ///报单引用
    uint32_t                 order_client_id;
    ///交易市场
    XTP_MARKET_TYPE          market;
    ///订单号，引入XTPID后，该字段实际和order_xtp_id重复。接口中暂时保留。
    uint64_t                 local_order_id;
    ///成交编号，深交所唯一，上交所每笔交易唯一，当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交
    char                     exec_id[XTP_EXEC_ID_LEN];
    ///数量，此次成交的数量，不是累计数量
    int64_t                  quantity;
    ///成交时间，格式为YYYYMMDDHHMMSSsss
    int64_t                  trade_time;
    ///成交金额，组合拆分涉及的保证金
    double                   trade_amount;
    ///成交序号 --回报记录号，每个交易所唯一,report_index+market字段可以组成唯一标识表示成交回报
    uint64_t                 report_index;
    ///报单编号 --交易所单号(保留字段)
    char                     order_exch_id[XTP_ORDER_EXCH_LEN];
    ///成交类型  --成交回报中的执行类型
    TXTPTradeTypeType        trade_type;
    ///组合方向
    XTP_SIDE_TYPE            side;
    ///业务类型
    XTP_BUSINESS_TYPE        business_type;
    ///交易所交易员代码
    char                     branch_pbu[XTP_BRANCH_PBU_LEN];

    ///期权组合策略信息
    XTPOptCombPlugin         opt_comb_info;
};
```
```cpp
/// 成交执行编号的字符串长度
#define XTP_EXEC_ID_LEN 18
/// 交易所单号的字符串长度
#define XTP_ORDER_EXCH_LEN 17
/// 交易所交易员代码字符串长度
#define XTP_BRANCH_PBU_LEN 7
```

 3.返回

无

 4.触发函数
```cpp
// 期权组合策略报单录入请求
virtual uint64_t InsertOptionCombinedOrder(XTPOptCombOrderInsertInfo *order, uint64_t session_id) = 0;
```


### 45. OnCancelOptionCombinedOrderError


期权组合策略撤单出错响应。

此响应只会在撤单发生错误时被回调。

 1.函数原型
```cpp
virtual void OnCancelOptionCombinedOrderError(XTPOptCombOrderCancelInfo *cancel_info, XTPRI *error_info, uint64_t session_id) {};
```
 2.参数

cancel_info：撤单具体信息，包括撤单的order_cancel_xtp_id和待撤单的order_xtp_id

error_info：撤单被拒绝或者发生错误时错误代码和错误信息，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
// 期权组合策略撤单错误响应结构体
typedef struct XTPOrderCancelInfo XTPOptCombOrderCancelInfo;

///撤单失败响应消息
struct XTPOrderCancelInfo
{
    ///撤单XTPID
    uint64_t                 order_cancel_xtp_id;
    ///原始订单XTPID
    uint64_t                 order_xtp_id;
};
```

 3.返回

无

 4.触发函数
```cpp
// 期权组合策略报单撤单请求
virtual uint64_t CancelOptionCombinedOrder(const uint64_t order_xtp_id, uint64_t session_id) = 0;
```


### 46. OnQueryOptionCombinedOrders


请求查询期权组合策略报单响应-旧版本接口。

由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

 1.函数原型
```cpp
virtual void OnQueryOptionCombinedOrders(XTPQueryOptCombOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

order_info：查询到的一个报单

error_info：查询报单时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
//期权组合策略报单查询响应结构体
typedef struct XTPOptCombOrderInfo XTPQueryOptCombOrderRsp;

///期权组合策略报单响应结构体
struct XTPOptCombOrderInfo
{
    ///XTP系统订单ID，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，用户自定义
    uint32_t	            order_client_id;
    ///报单操作引用，用户自定义（暂未使用）
    uint32_t                order_cancel_client_id;
    ///撤单在XTP系统中的id，在XTP系统中唯一
    uint64_t                order_cancel_xtp_id;
    ///证券代码
    ///char                    ticker[XTP_TICKER_LEN];
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///数量，此订单的报单数量
    int64_t                 quantity;

    ///组合方向
    XTP_SIDE_TYPE               side;

    ///业务类型
    XTP_BUSINESS_TYPE       business_type;
    ///今成交数量，为此订单累计成交数量
    int64_t                 qty_traded;
    ///剩余数量，当撤单成功时，表示撤单数量
    int64_t                 qty_left;
    ///委托时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 insert_time;
    ///最后修改时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 update_time;
    ///撤销时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 cancel_time;
    ///成交金额，组合拆分涉及的保证金(保留字段)
    double                  trade_amount;
    ///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    ///报单状态，订单响应中没有部分成交状态的推送，在查询订单结果中，会有部分成交状态
    XTP_ORDER_STATUS_TYPE   order_status;
    ///报单提交状态，用户可用此字段来区分撤单和报单
    XTP_ORDER_SUBMIT_STATUS_TYPE   order_submit_status;
    ///报单类型
    TXTPOrderTypeType       order_type;

    ///期权组合策略信息
    XTPOptCombPlugin        opt_comb_info;
};
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询期权组合策略未完结报单-旧版本接口
virtual int QueryOptionCombinedUnfinishedOrders(uint64_t session_id, int request_id) = 0;
// 根据报单ID请求查询期权组合策略报单-旧版本接口
virtual int QueryOptionCombinedOrderByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
// 请求查询期权组合策略报单-旧版本接口
virtual int QueryOptionCombinedOrders(const XTPQueryOptCombOrderReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 47. OnQueryOptionCombinedOrdersEx


请求查询期权组合策略报单响应-新版本接口。

由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

 1.函数原型
```cpp
virtual void OnQueryOptionCombinedOrdersEx(XTPOptCombOrderInfoEx *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

order_info：查询到的一个报单

error_info：查询报单时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///期权组合策略报单响应结构体，新版本
struct XTPOptCombOrderInfoEx
{
    ///XTP系统订单ID，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，用户自定义
    uint32_t	            order_client_id;
    ///报单操作引用，用户自定义（暂未使用）
    uint32_t                order_cancel_client_id;
    ///撤单在XTP系统中的id，在XTP系统中唯一
    uint64_t                order_cancel_xtp_id;
    ///证券代码
    ///char                    ticker[XTP_TICKER_LEN];
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///数量，此订单的报单数量
    int64_t                 quantity;

    ///组合方向
    XTP_SIDE_TYPE               side;

    ///业务类型
    XTP_BUSINESS_TYPE       business_type;
    ///今成交数量，为此订单累计成交数量
    int64_t                 qty_traded;
    ///剩余数量，当撤单成功时，表示撤单数量
    int64_t                 qty_left;
    ///委托时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 insert_time;
    ///最后修改时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 update_time;
    ///撤销时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 cancel_time;
    ///成交金额，组合拆分涉及的保证金
    double                  trade_amount;
    ///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    ///报单状态，订单响应中没有部分成交状态的推送，在查询订单结果中，会有部分成交状态
    XTP_ORDER_STATUS_TYPE   order_status;
    ///报单提交状态，OMS内部使用，用户无需关心
    XTP_ORDER_SUBMIT_STATUS_TYPE   order_submit_status;
    ///报单类型
    TXTPOrderTypeType       order_type;

    ///期权组合策略信息
    XTPOptCombPlugin        opt_comb_info;
    ///报单编号 --交易所单号，上交所为空，深交所有此字段
    char                    order_exch_id[XTP_ORDER_EXCH_LEN];
    ///订单的错误信息
    XTPRI                   order_err_t;
    ///保留字段
    uint64_t                unknown[2];
};
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询期权组合策略未完结报单-新版本接口
virtual int QueryOptionCombinedUnfinishedOrdersEx(uint64_t session_id, int request_id) = 0;
// 根据报单ID请求查询期权组合策略报单-新版本接口
virtual int QueryOptionCombinedOrderByXTPIDEx(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
// 请求查询期权组合策略报单-新版本接口
virtual int QueryOptionCombinedOrdersEx(const XTPQueryOptCombOrderReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 48. OnQueryOptionCombinedOrdersByPage


分页请求查询期权组合策略报单响应-旧版本接口。

当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果order_sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryOptionCombinedOrdersByPage(XTPQueryOptCombOrderRsp *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

order_info：查询到的一个报单

req_count：分页请求的最大数量

order_sequence：分页请求的当前回报数量

query_reference：当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
// 期权组合策略报单查询响应结构体
typedef struct XTPOptCombOrderInfo XTPQueryOptCombOrderRsp;

///期权组合策略报单响应结构体
struct XTPOptCombOrderInfo
{
    ///XTP系统订单ID，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，用户自定义
    uint32_t	            order_client_id;
    ///报单操作引用，用户自定义（暂未使用）
    uint32_t                order_cancel_client_id;
    ///撤单在XTP系统中的id，在XTP系统中唯一
    uint64_t                order_cancel_xtp_id;
    ///证券代码
    ///char                    ticker[XTP_TICKER_LEN];
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///数量，此订单的报单数量
    int64_t                 quantity;

    ///组合方向
    XTP_SIDE_TYPE               side;

    ///业务类型
    XTP_BUSINESS_TYPE       business_type;
    ///今成交数量，为此订单累计成交数量
    int64_t                 qty_traded;
    ///剩余数量，当撤单成功时，表示撤单数量
    int64_t                 qty_left;
    ///委托时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 insert_time;
    ///最后修改时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 update_time;
    ///撤销时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 cancel_time;
    ///成交金额，组合拆分涉及的保证金(保留字段)
    double                  trade_amount;
    ///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    ///报单状态，订单响应中没有部分成交状态的推送，在查询订单结果中，会有部分成交状态
    XTP_ORDER_STATUS_TYPE   order_status;
    ///报单提交状态，用户可用此字段来区分撤单和报单
    XTP_ORDER_SUBMIT_STATUS_TYPE   order_submit_status;
    ///报单类型
    TXTPOrderTypeType       order_type;

    ///期权组合策略信息
    XTPOptCombPlugin        opt_comb_info;
};
```

 3.返回

无

 4.触发函数
```cpp
// 分页请求查询期权组合策略报单-旧版本接口
virtual int QueryOptionCombinedOrdersByPage(const XTPQueryOptCombOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 49. OnQueryOptionCombinedOrdersByPageEx


分页请求查询期权组合策略报单响应-新版本接口。

当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果order_sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryOptionCombinedOrdersByPageEx(XTPOptCombOrderInfoEx *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

order_info：查询到的一个报单

req_count：分页请求的最大数量

order_sequence：分页请求的当前回报数量

query_reference：当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///期权组合策略报单响应结构体，新版本
struct XTPOptCombOrderInfoEx
{
    ///XTP系统订单ID，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，用户自定义
    uint32_t	            order_client_id;
    ///报单操作引用，用户自定义（暂未使用）
    uint32_t                order_cancel_client_id;
    ///撤单在XTP系统中的id，在XTP系统中唯一
    uint64_t                order_cancel_xtp_id;
    ///证券代码
    ///char                    ticker[XTP_TICKER_LEN];
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///数量，此订单的报单数量
    int64_t                 quantity;

    ///组合方向
    XTP_SIDE_TYPE               side;

    ///业务类型
    XTP_BUSINESS_TYPE       business_type;
    ///今成交数量，为此订单累计成交数量
    int64_t                 qty_traded;
    ///剩余数量，当撤单成功时，表示撤单数量
    int64_t                 qty_left;
    ///委托时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 insert_time;
    ///最后修改时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 update_time;
    ///撤销时间，格式为YYYYMMDDHHMMSSsss
    int64_t                 cancel_time;
    ///成交金额，组合拆分涉及的保证金
    double                  trade_amount;
    ///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    ///报单状态，订单响应中没有部分成交状态的推送，在查询订单结果中，会有部分成交状态
    XTP_ORDER_STATUS_TYPE   order_status;
    ///报单提交状态，OMS内部使用，用户无需关心
    XTP_ORDER_SUBMIT_STATUS_TYPE   order_submit_status;
    ///报单类型
    TXTPOrderTypeType       order_type;

    ///期权组合策略信息
    XTPOptCombPlugin        opt_comb_info;
    ///报单编号 --交易所单号，上交所为空，深交所有此字段
    char                    order_exch_id[XTP_ORDER_EXCH_LEN];
    ///订单的错误信息
    XTPRI                   order_err_t;
    ///保留字段
    uint64_t                unknown[2];
};
```

 3.返回

无

 4.触发函数
```cpp
// 分页请求查询期权组合策略报单-新版本接口
virtual int QueryOptionCombinedOrdersByPageEx(const XTPQueryOptCombOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 50. OnQueryOptionCombinedTrades


请求查询期权组合策略成交响应。

由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

 1.函数原型
```cpp
virtual void OnQueryOptionCombinedTrades(XTPQueryOptCombTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

trade_info：查询到的一个成交回报

error_info：查询成交回报发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
// 成交回报查询响应结构体
typedef struct XTPOptCombTradeReport XTPQueryOptCombTradeRsp;

///期权组合策略报单成交结构体
struct XTPOptCombTradeReport
{
    ///XTP系统订单ID，此成交回报相关的订单ID，在XTP系统中唯一
    uint64_t                 order_xtp_id;
    ///报单引用
    uint32_t                 order_client_id;
    ///交易市场
    XTP_MARKET_TYPE          market;
    ///订单号，引入XTPID后，该字段实际和order_xtp_id重复。接口中暂时保留。
    uint64_t                 local_order_id;
    ///成交编号，深交所唯一，上交所每笔交易唯一，当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交
    char                     exec_id[XTP_EXEC_ID_LEN];
    ///数量，此次成交的数量，不是累计数量
    int64_t                  quantity;
    ///成交时间，格式为YYYYMMDDHHMMSSsss
    int64_t                  trade_time;
    ///成交金额，组合拆分涉及的保证金
    double                   trade_amount;
    ///成交序号 --回报记录号，每个交易所唯一,report_index+market字段可以组成唯一标识表示成交回报
    uint64_t                 report_index;
    ///报单编号 --交易所单号(保留字段)
    char                     order_exch_id[XTP_ORDER_EXCH_LEN];
    ///成交类型  --成交回报中的执行类型
    TXTPTradeTypeType        trade_type;
    ///组合方向
    XTP_SIDE_TYPE            side;
    ///业务类型
    XTP_BUSINESS_TYPE        business_type;
    ///交易所交易员代码
    char                     branch_pbu[XTP_BRANCH_PBU_LEN];

    ///期权组合策略信息
    XTPOptCombPlugin         opt_comb_info;
};
```

 3.返回

无

 4.触发函数
```cpp
// 根据期权组合策略委托编号请求查询相关成交
virtual int QueryOptionCombinedTradesByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
// 请求查询期权组合策略的成交回报
virtual int QueryOptionCombinedTrades(const XTPQueryOptCombTraderReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 51. OnQueryOptionCombinedTradesByPage


分页请求查询期权组合策略成交响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryOptionCombinedTradesByPage(XTPQueryOptCombTradeRsp *trade_info, int64_t req_count, int64_t trade_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

trade_info：查询到的一个成交信息

req_count：分页请求的最大数量

order_sequence：分页请求的当前回报数量

query_reference：当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
// 成交回报查询响应结构体
typedef struct XTPOptCombTradeReport XTPQueryOptCombTradeRsp;

///期权组合策略报单成交结构体
struct XTPOptCombTradeReport
{
    ///XTP系统订单ID，此成交回报相关的订单ID，在XTP系统中唯一
    uint64_t                 order_xtp_id;
    ///报单引用
    uint32_t                 order_client_id;
    ///交易市场
    XTP_MARKET_TYPE          market;
    ///订单号，引入XTPID后，该字段实际和order_xtp_id重复。接口中暂时保留。
    uint64_t                 local_order_id;
    ///成交编号，深交所唯一，上交所每笔交易唯一，当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交
    char                     exec_id[XTP_EXEC_ID_LEN];
    ///数量，此次成交的数量，不是累计数量
    int64_t                  quantity;
    ///成交时间，格式为YYYYMMDDHHMMSSsss
    int64_t                  trade_time;
    ///成交金额，组合拆分涉及的保证金
    double                   trade_amount;
    ///成交序号 --回报记录号，每个交易所唯一,report_index+market字段可以组成唯一标识表示成交回报
    uint64_t                 report_index;
    ///报单编号 --交易所单号(保留字段)
    char                     order_exch_id[XTP_ORDER_EXCH_LEN];
    ///成交类型  --成交回报中的执行类型
    TXTPTradeTypeType        trade_type;
    ///组合方向
    XTP_SIDE_TYPE            side;
    ///业务类型
    XTP_BUSINESS_TYPE        business_type;
    ///交易所交易员代码
    char                     branch_pbu[XTP_BRANCH_PBU_LEN];

    ///期权组合策略信息
    XTPOptCombPlugin         opt_comb_info;
};
```

 3.返回

无

 4.触发函数
```cpp
// 分页请求查询期权组合策略成交回报
virtual int QueryOptionCombinedTradesByPage(const XTPQueryOptCombTraderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
```


### 52. OnQueryOptionCombinedPosition


请求查询期权组合策略持仓响应。

一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryOptionCombinedPosition(XTPQueryOptCombPositionRsp *position_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

position_info：查询到的一个持仓信息

error_info：查询持仓发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
/// 查询期权组合策略持仓信息的响应
struct XTPQueryOptCombPositionRsp {
    char                    strategy_id[XTP_STRATEGY_ID_LEN];           ///< 组合策略代码
    char                    strategy_name[XTP_STRATEGY_NAME_LEN];       ///< 组合策略名称

    XTP_MARKET_TYPE         market;                                     ///< 交易市场
    int64_t                 total_qty;                                  ///< 总持仓
    int64_t                 available_qty;                              ///< 可拆分持仓
    int64_t                 yesterday_position;                         ///< 昨日持仓

    XTPOptCombPlugin        opt_comb_info;                              ///< 期权组合策略信息

	double					secu_comb_margin;							///< 组合占用保证金（公司）（目前暂未启用）

    uint64_t                reserved[50-1];                             ///< 保留字段
};

///期权组合策略报单附加信息结构体
typedef struct XTPOptCombPlugin {
    char                                strategy_id[XTP_STRATEGY_ID_LEN];               ///< 组合策略代码，比如CNSJC认购牛市价差策略等。合并行权时，此字段可为空
    char                                comb_num[XTP_SECONDARY_ORDER_ID_LEN];           ///< 组合编码，组合申报时，该字段为空；拆分申报时，填写拟拆分组合的组合编码。
    int32_t                             num_legs;                                       ///< 成分合约数
    XTPOptCombLegInfo                   leg_detail[XTP_STRATEGE_LEG_NUM];               ///< 成分合约数组，最多四条腿。
}XTPOptCombPlugin;

/// 组合策略腿合约信息结构体
typedef struct XTPOptCombLegInfo {
    char                            leg_security_id[XTP_TICKER_LEN]; ///< 成分合约代码
    XTP_OPT_CALL_OR_PUT_TYPE        leg_cntr_type;                   ///< 合约类型，认沽或认购。
    XTP_POSITION_DIRECTION_TYPE     leg_side;                        ///< 持仓方向，权利方或义务方。
    XTP_OPT_COVERED_OR_UNCOVERED    leg_covered;                     ///< 备兑标签
    int32_t                         leg_qty;                         ///< 成分合约数量（张）
}XTPOptCombLegInfo;

/// XTP_OPT_CALL_OR_PUT_TYPE是一个认沽或认购类型
typedef enum XTP_OPT_CALL_OR_PUT_TYPE {
	XTP_OPT_CALL = 1,	    ///<认购
	XTP_OPT_PUT = 2,		///<认沽
}XTP_OPT_CALL_OR_PUT_TYPE;

/// XTP_POSITION_DIRECTION_TYPE是一个持仓方向类型
typedef enum XTP_POSITION_DIRECTION_TYPE {
	XTP_POSITION_DIRECTION_NET = 0,	    ///<净
	XTP_POSITION_DIRECTION_LONG,		///<多（期权则为权利方）
    XTP_POSITION_DIRECTION_SHORT,       ///<空（期权则为义务方）
    XTP_POSITION_DIRECTION_COVERED,     ///<备兑（期权则为备兑义务方）
}XTP_POSITION_DIRECTION_TYPE;

/// XTP_OPT_COVERED_OR_UNCOVERED是否备兑的标签
typedef enum XTP_OPT_COVERED_OR_UNCOVERED {
    XTP_POSITION_UNCOVERED = 0,     ///<非备兑
    XTP_POSITION_COVERED,           ///<备兑
}XTP_OPT_COVERED_OR_UNCOVERED;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
/// 本地报单编号的字符串长度
#define XTP_LOCAL_ORDER_LEN         11
/// 期权组合策略最多腿数
#define XTP_STRATEGE_LEG_NUM        4
/// 期权组合策略代码字符串长度
#define XTP_STRATEGY_ID_LEN         10
/// 期权组合策略名称字符串长度
#define XTP_STRATEGY_NAME_LEN		32
/// 期权组合策略组合编码字符串长度
#define XTP_SECONDARY_ORDER_ID_LEN  18
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询投资者期权组合策略持仓
virtual int QueryOptionCombinedPosition(const XTPQueryOptCombPositionReq* query_param, uint64_t session_id, int request_id) = 0;
```


### 53. OnQueryOptionCombinedStrategyInfo


请求查询期权组合策略信息响应。

一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryOptionCombinedStrategyInfo(XTPQueryCombineStrategyInfoRsp *strategy_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

strategy_info：查询到的一个组合策略信息

error_info：查询成交回报发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
/// 查询期权组合策略信息的响应
struct XTPQueryCombineStrategyInfoRsp {
    char                    strategy_id[XTP_STRATEGY_ID_LEN];        ///< 组合策略代码，CNSJC、PXSJC、PNSJC、CXSJC、KS、KKS
    char                    strategy_name[XTP_STRATEGY_NAME_LEN];    ///< 组合策略名称，认购牛市价差策略、认沽熊市价差策略、认沽牛市价差策略、认购熊市价差策略、跨式空头、宽跨式空头
	XTP_MARKET_TYPE         market;                                  ///< 交易市场

    int32_t                 leg_num;                                 ///< 成分合约个数，1-4个，即下面数组的实际大小
    XTPCombLegStrategy      leg_strategy[XTP_STRATEGE_LEG_NUM];      ///< 成分合约信息，最多四条腿

    XTP_EXPIRE_DATE_TYPE    expire_date_type;                        ///< 到期日要求。枚举值为：同到期日，不同到期日，无到期日要求
    XTP_UNDERLYING_TYPE     underlying_type;                         ///< 标的要求。枚举值为：相同标的，不同标的，无标的要求
    XTP_AUTO_SPLIT_TYPE     auto_sep_type;                           ///< 自动解除类型。枚举值为：-1：不适用；0：到期日自动解除；1：E-1日自动解除，依次类推

    uint64_t                reserved[10];                            ///< 预留的字段
};
```
```cpp
/// 期权组合策略的成分合约信息
struct XTPCombLegStrategy {
    XTP_OPT_CALL_OR_PUT_TYPE    call_or_put;        ///< 合约类型，认沽或认购
    XTP_POSITION_DIRECTION_TYPE position_side;      ///< 权利仓或者义务仓或备兑义务仓
    TXTPExerciseSeqType         exercise_price_seq; ///< 行权价顺序
    int32_t                     expire_date_seq;    ///< 到期日顺序
    int64_t                     leg_qty;            ///< 单份组合策略中包含的此合约张数
};
```
```cpp
///XTP_EXPIRE_DATE_TYPE是一个期权组合策略合约到期日要求类型
typedef enum XTP_EXPIRE_DATE_TYPE {
	XTP_EXP_DATE_SAME = 0,   ///< 相同到期日
	XTP_EXP_DATE_DIFF,      ///< 不同到期日
	XTP_EXP_DATE_NON         ///< 无到期日要求
}XTP_EXPIRE_DATE_TYPE;
```
```cpp
///XTP_UNDERLYING_TYPE是一个期权组合策略标的要求类型
typedef enum XTP_UNDERLYING_TYPE {
	XTP_UNDERLYING_SAME = 0,	///<相同标的
	XTP_UNDERLYING_DIFF,		///<不同标的
	XTP_UNDERLYING_NON			///<无标的要求
}XTP_UNDERLYING_TYPE;
```
```cpp
///XTP_AUTO_SPLIT_TYPE是一个期权组合策略自动解除枚举类型
typedef enum XTP_AUTO_SPLIT_TYPE {
	XTP_AUTO_SPLIT_EXPDAY = 0,	///<到期日自动解除
	XTP_AUTO_SPLIT_PREDAY,		///<E-1日自动解除
	XTP_AUTO_SPLIT_PRE2DAY,		///<E-2日自动解除
	XTP_AUTO_SPLIT_NON			///<无效值
}XTP_AUTO_SPLIT_TYPE;
```
```cpp
/// 期权组合策略最多腿数
#define XTP_STRATEGE_LEG_NUM        4
/// 期权组合策略代码字符串长度
#define XTP_STRATEGY_ID_LEN         10
/// 期权组合策略名称字符串长度
#define XTP_STRATEGY_NAME_LEN       32
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询期权组合策略信息
virtual int QueryOptionCombinedStrategyInfo(uint64_t session_id, int request_id) = 0;
```


### 54. OnQueryOptionCombinedExecPosition


查询期权行权合并头寸的响应。

一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryOptionCombinedExecPosition(XTPQueryOptCombExecPosRsp *position_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

position_info：查询到的一个行权合并头寸信息

error_info：查询持仓发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
/// 查询期权行权合并头寸的响应
struct XTPQueryOptCombExecPosRsp {

    XTP_MARKET_TYPE                 market;                             ///< 市场
    char                            cntrt_code_1[XTP_TICKER_LEN];       ///< 成分合约1代码
    char                            cntrt_name_1[XTP_TICKER_NAME_LEN];  ///< 成分合约1名称
    XTP_POSITION_DIRECTION_TYPE     position_side_1;                    ///< 成分合约1持仓方向
    XTP_OPT_CALL_OR_PUT_TYPE        call_or_put_1;                      ///< 成分合约1类型
    int64_t                         avl_qty_1;                          ///< 成分合约1可用持仓数量
    int64_t                         orig_own_qty_1;                     ///< 成分合约1昨日持仓数量
    int64_t                         own_qty_1;                          ///< 成分合约1当前持仓数量

    char                            cntrt_code_2[XTP_TICKER_LEN];       ///< 成分合约2代码
    char                            cntrt_name_2[XTP_TICKER_NAME_LEN];  ///< 成分合约2名称
    XTP_POSITION_DIRECTION_TYPE     position_side_2;                    ///< 成分合约2持仓方向
    XTP_OPT_CALL_OR_PUT_TYPE        call_or_put_2;                      ///< 成分合约2类型
    int64_t                         avl_qty_2;                          ///< 成分合约2可用持仓数量
    int64_t                         orig_own_qty_2;                     ///< 成分合约2昨日持仓数量
    int64_t                         own_qty_2;                          ///< 成分合约2当前持仓数量

    int64_t                         net_qty;                            ///< 权利仓净头寸

    int64_t                         order_qty;                          ///< 行权合并委托数量，不含已拒单已撤单。
    int64_t                         confirm_qty;                        ///< 行权合并已确认数量
    int64_t                         avl_qty;                            ///< 可行权合并数量

    uint64_t                        reserved[49];                       ///< 保留字段
};
```
```cpp
///XTP_POSITION_DIRECTION_TYPE是一个持仓方向类型
typedef enum XTP_POSITION_DIRECTION_TYPE {
	XTP_POSITION_DIRECTION_NET = 0,	    ///<净
	XTP_POSITION_DIRECTION_LONG,		///<多（期权则为权利方）
    XTP_POSITION_DIRECTION_SHORT,       ///<空（期权则为义务方）
    XTP_POSITION_DIRECTION_COVERED,     ///<备兑（期权则为备兑义务方）
}XTP_POSITION_DIRECTION_TYPE;
```
```cpp
///XTP_OPT_CALL_OR_PUT_TYPE是一个认沽或认购类型
typedef enum XTP_OPT_CALL_OR_PUT_TYPE {
	XTP_OPT_CALL = 1,	    ///<认购
	XTP_OPT_PUT = 2,		///<认沽
}XTP_OPT_CALL_OR_PUT_TYPE;
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
/// 存放证券名称的字符串长度
#define XTP_TICKER_NAME_LEN 64
```

 3.返回

无

 4.触发函数
```cpp
// 请求查询期权行权合并头寸
virtual int QueryOptionCombinedExecPosition(const XTPQueryOptCombExecPosReq* query_param, uint64_t session_id, int request_id) = 0;
```


### 55. OnQueryStrategy


algo业务中查询策略列表的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryStrategy(XTPStrategyInfoStruct* strategy_info, char* strategy_param, XTPRI *error_info, int32_t request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

strategy_info：策略具体信息

strategy_param：此策略中包含的参数，如果error_info.error_id为0时，有意义

error_info：查询查询策略列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///策略信息结构体
typedef struct XTPStrategyInfoStruct
{
	uint16_t				m_strategy_type;		///< 策略类型
	XTPStrategyStateType	m_strategy_state;		///< 策略状态
	uint64_t				m_client_strategy_id;	///< 客户策略id
	uint64_t				m_xtp_strategy_id;		///< xtp策略id
} XTPStrategyInfoStruct;
```
```cpp
///XTPStrategyStateType策略状态类型
typedef uint8_t XTPStrategyStateType;

///创建中
#define XTP_STRATEGY_STATE_CREATING		0
///已创建
#define XTP_STRATEGY_STATE_CREATED		1
///开始执行中
#define XTP_STRATEGY_STATE_STARTING		2
///已执行
#define XTP_STRATEGY_STATE_STARTED		3
///停止中
#define XTP_STRATEGY_STATE_STOPPING		4
///已停止
#define XTP_STRATEGY_STATE_STOPPED		5
///销毁中
#define XTP_STRATEGY_STATE_DESTROYING	6
///已销毁
#define XTP_STRATEGY_STATE_DESTROYED	7
///发生错误
#define XTP_STRATEGY_STATE_ERROR		8
```

 3.返回

无

 4.触发函数
```cpp
///algo业务中查询用户策略请求
virtual int QueryStrategy(uint32_t strategy_type, uint64_t client_strategy_id, uint64_t xtp_strategy_id, uint64_t session_id, int32_t request_id) = 0;
```


### 56. OnStrategyStateReport


algo业务中策略运行时策略状态通知。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnStrategyStateReport(XTPStrategyStateReportStruct* strategy_state, uint64_t session_id) {};
```
 2.参数

strategy_state：用户策略运行情况的状态通知

session_id：资金账户对应的session_id，登录时得到

```cpp
///策略状态结构体
typedef struct XTPStrategyStateReportStruct
{
	XTPStrategyInfoStruct		m_strategy_info;			///< 策略信息
	int64_t						m_strategy_qty;				///< 策略总量
	int64_t						m_strategy_ordered_qty;		///< 策略已委托数量
	int64_t						m_strategy_cancelled_qty;	///< 策略已撤单数量
	int64_t						m_strategy_execution_qty;	///< 策略已成交数量
	int64_t						m_strategy_unclosed_qty;	///< 策略未平仓数量(T0卖出数量-买入数量)
	double						m_strategy_asset;			///< 策略总金额
	double						m_strategy_ordered_asset;	///< 策略已委托金额
	double						m_strategy_execution_asset;	///< 策略已成交金额
	double						m_strategy_execution_price;	///< 策略执行价格
	double						m_strategy_market_price;	///< 策略市场价
	double						m_strategy_price_diff;		///< 策略执行价差
	double						m_strategy_asset_diff;		///< 策略执行绩效(T0资金预净收入)
	XTPRI						m_error_info;				///< 错误信息
} XTPStrategyStateReport;

///策略信息结构体
typedef struct XTPStrategyInfoStruct
{
	uint16_t				m_strategy_type;		///< 策略类型
	XTPStrategyStateType	m_strategy_state;		///< 策略状态
	uint64_t				m_client_strategy_id;	///< 客户策略id
	uint64_t				m_xtp_strategy_id;		///< xtp策略id
} XTPStrategyInfoStruct;
```
```cpp
///XTPStrategyStateType策略状态类型
typedef uint8_t XTPStrategyStateType;

///创建中
#define XTP_STRATEGY_STATE_CREATING		0
///已创建
#define XTP_STRATEGY_STATE_CREATED		1
///开始执行中
#define XTP_STRATEGY_STATE_STARTING		2
///已执行
#define XTP_STRATEGY_STATE_STARTED		3
///停止中
#define XTP_STRATEGY_STATE_STOPPING		4
///已停止
#define XTP_STRATEGY_STATE_STOPPED		5
///销毁中
#define XTP_STRATEGY_STATE_DESTROYING	6
///已销毁
#define XTP_STRATEGY_STATE_DESTROYED	7
///发生错误
#define XTP_STRATEGY_STATE_ERROR		8
```

 3.返回

无


### 57. OnALGOUserEstablishChannel


algo业务中用户建立算法通道的消息响应。

算法通道建立成功后，才能对用户创建策略等操作，一个用户只能拥有一个算法通道，如果之前已经建立，则无需重复建立。

 1.函数原型
```cpp
virtual void OnALGOUserEstablishChannel(char* user, XTPRI* error_info, uint64_t session_id) {};
```
 2.参数

user：用户名

error_info：建立算法通道发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误，即算法通道成功

session_id：资金账户对应的session_id，登录时得到

 3.返回

无

4.触发函数
```cpp
///用户请求使用algo服务器建立算法通道
virtual int ALGOUserEstablishChannel(const char* oms_ip, int oms_port, const char* user, const char* password, uint64_t session_id) = 0;
```


### 58. OnInsertAlgoOrder


algo业务中报送策略单的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnInsertAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPRI *error_info, uint64_t session_id) {};
```
 2.参数

strategy_info：用户报送的策略单的具体信息

error_info：报送策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

session_id：资金账户对应的session_id，登录时得到

```cpp
///策略信息结构体
typedef struct XTPStrategyInfoStruct
{
	uint16_t				m_strategy_type;		///< 策略类型
	XTPStrategyStateType	m_strategy_state;		///< 策略状态
	uint64_t				m_client_strategy_id;	///< 客户策略id
	uint64_t				m_xtp_strategy_id;		///< xtp策略id
} XTPStrategyInfoStruct;
```
```cpp
///XTPStrategyStateType策略状态类型
typedef uint8_t XTPStrategyStateType;

///创建中
#define XTP_STRATEGY_STATE_CREATING		0
///已创建
#define XTP_STRATEGY_STATE_CREATED		1
///开始执行中
#define XTP_STRATEGY_STATE_STARTING		2
///已执行
#define XTP_STRATEGY_STATE_STARTED		3
///停止中
#define XTP_STRATEGY_STATE_STOPPING		4
///已停止
#define XTP_STRATEGY_STATE_STOPPED		5
///销毁中
#define XTP_STRATEGY_STATE_DESTROYING	6
///已销毁
#define XTP_STRATEGY_STATE_DESTROYED	7
///发生错误
#define XTP_STRATEGY_STATE_ERROR		8
```

 3.返回

无

 4.触发函数
```cpp
///algo业务中用户报算法单请求
virtual int InsertAlgoOrder(uint32_t strategy_type, uint64_t client_strategy_id, char* strategy_param, uint64_t session_id) = 0;
```


### 59. OnCancelAlgoOrder


algo业务中撤销策略单的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnCancelAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPRI *error_info, uint64_t session_id) {};
```
 2.参数

strategy_info：用户撤销的策略单的具体信息

error_info：撤销策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

session_id：资金账户对应的session_id，登录时得到

```cpp
///策略信息结构体
typedef struct XTPStrategyInfoStruct
{
	uint16_t				m_strategy_type;		///< 策略类型
	XTPStrategyStateType	m_strategy_state;		///< 策略状态
	uint64_t				m_client_strategy_id;	///< 客户策略id
	uint64_t				m_xtp_strategy_id;		///< xtp策略id
} XTPStrategyInfoStruct;
```
```cpp
///XTPStrategyStateType策略状态类型
typedef uint8_t XTPStrategyStateType;

///创建中
#define XTP_STRATEGY_STATE_CREATING		0
///已创建
#define XTP_STRATEGY_STATE_CREATED		1
///开始执行中
#define XTP_STRATEGY_STATE_STARTING		2
///已执行
#define XTP_STRATEGY_STATE_STARTED		3
///停止中
#define XTP_STRATEGY_STATE_STOPPING		4
///已停止
#define XTP_STRATEGY_STATE_STOPPED		5
///销毁中
#define XTP_STRATEGY_STATE_DESTROYING	6
///已销毁
#define XTP_STRATEGY_STATE_DESTROYED	7
///发生错误
#define XTP_STRATEGY_STATE_ERROR		8
```

 3.返回

无

 4.触发函数
```cpp
///algo业务中用户撤销算法单请求
virtual int CancelAlgoOrder(bool cancel_flag, uint64_t xtp_strategy_id, uint64_t session_id) = 0;
```


### 60. OnAlgoDisconnected


当客户端与AlgoBus通信连接断开时，该方法被调用。

请不要堵塞此线程，否则会影响algo的登录，与Algo之间的连接，断线后会自动重连，用户无需做其他操作。

 1.函数原型
```cpp
virtual void OnAlgoDisconnected(int reason) {};
```
 2.参数

reason：错误原因，请与错误代码表对应

 3.返回

无


### 61. OnAlgoConnected


当客户端与AlgoBus断线后重新连接时，该方法被调用，仅在断线重连成功后会被调用。

 1.函数原型
```cpp
virtual void OnAlgoConnected() {};
```
 2.参数

无

 3.返回

无


### 62. OnStrategySymbolStateReport


algo业务中策略运行时策略指定证券执行状态通知。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, uint64_t session_id) {};
```
 2.参数

strategy_symbol_state：用户策略指定证券运行情况的状态通知

session_id：资金账户对应的session_id，登录时得到

```cpp
///策略中指定证券的算法执行状态结构体
typedef struct XTPStrategySymbolStateReportStruct
{
	XTPStrategyInfoStruct		m_strategy_info;			///< 策略信息
	char						m_ticker[XTP_TICKER_LEN];	///< 证券代码
	XTP_MARKET_TYPE				m_market;					///< 市场
	XTP_SIDE_TYPE				m_side;						///< 买卖方向，=0时为T0单
	int64_t						m_strategy_qty;				///< 策略总量
	int64_t						m_strategy_ordered_qty;		///< 策略已委托数量
	int64_t						m_strategy_cancelled_qty;	///< 策略已撤单数量
	int64_t						m_strategy_execution_qty;	///< 策略已成交数量
	int64_t						m_strategy_buy_qty;			///< 策略已买入数量(T0)
	int64_t						m_strategy_sell_qty;		///< 策略已卖出数量(T0)
	int64_t						m_strategy_unclosed_qty;	///< 策略未平仓数量(T0卖出数量-买入数量)
	double						m_strategy_asset;			///< 策略总金额
	double						m_strategy_ordered_asset;	///< 策略已委托金额
	double						m_strategy_execution_asset;	///< 策略已成交金额
	double						m_strategy_buy_asset;		///< 策略买入金额(T0)
	double						m_strategy_sell_asset;		///< 策略卖出金额(TO)
	double						m_strategy_unclosed_asset;	///< 策略未平仓金额(T0)
	double						m_strategy_asset_diff;		///< 策略毛收益增强金额(T0)
	double						m_strategy_execution_price;	///< 策略执行价格
	double						m_strategy_market_price;	///< 策略市场价
	double						m_strategy_price_diff;		///< 策略执行价差(T0时为毛增强收益率)
	XTPRI						m_error_info;				///< 错误信息
} XTPStrategySymbolStateReport;
```
```cpp
///策略信息结构体
typedef struct XTPStrategyInfoStruct
{
	uint16_t				m_strategy_type;		///< 策略类型
	XTPStrategyStateType	m_strategy_state;		///< 策略状态
	uint64_t				m_client_strategy_id;	///< 客户策略id
	uint64_t				m_xtp_strategy_id;		///< xtp策略id
} XTPStrategyInfoStruct;
```
```cpp
///XTPStrategyStateType策略状态类型
typedef uint8_t XTPStrategyStateType;

///创建中
#define XTP_STRATEGY_STATE_CREATING		0
///已创建
#define XTP_STRATEGY_STATE_CREATED		1
///开始执行中
#define XTP_STRATEGY_STATE_STARTING		2
///已执行
#define XTP_STRATEGY_STATE_STARTED		3
///停止中
#define XTP_STRATEGY_STATE_STOPPING		4
///已停止
#define XTP_STRATEGY_STATE_STOPPED		5
///销毁中
#define XTP_STRATEGY_STATE_DESTROYING	6
///已销毁
#define XTP_STRATEGY_STATE_DESTROYED	7
///发生错误
#define XTP_STRATEGY_STATE_ERROR		8
```
```cpp
///XTP_SIDE_TYPE是买卖方向类型
typedef uint8_t XTP_SIDE_TYPE;

///买（新股申购，ETF买，配股，信用交易中担保品买）
#define XTP_SIDE_BUY            1
///卖（逆回购，ETF卖，信用交易中担保品卖）
#define XTP_SIDE_SELL           2
///申购
#define XTP_SIDE_PURCHASE       7
///赎回
#define XTP_SIDE_REDEMPTION     8
///拆分
#define XTP_SIDE_SPLIT          9
///合并
#define XTP_SIDE_MERGE          10
///改版之后的side的备兑，暂不支持
#define XTP_SIDE_COVER          11
///改版之后的side锁定（对应开平标识为开）/解锁（对应开平标识为平）
#define XTP_SIDE_FREEZE         12
/// 融资买入
#define XTP_SIDE_MARGIN_TRADE	21
/// 融券卖出
#define XTP_SIDE_SHORT_SELL		22
/// 卖券还款
#define XTP_SIDE_REPAY_MARGIN	23
/// 买券还券
#define XTP_SIDE_REPAY_STOCK	24
/// 现金还款（不放在普通订单协议，另加请求和查询协议）
//#define XTP_SIDE_CASH_REPAY_MARGIN	25
/// 现券还券
#define XTP_SIDE_STOCK_REPAY_STOCK	26
/// 余券划转
#define XTP_SIDE_SURSTK_TRANS       27
/// 担保品转入
#define XTP_SIDE_GRTSTK_TRANSIN     28
/// 担保品转出
#define XTP_SIDE_GRTSTK_TRANSOUT    29

///组合策略的组合
#define XTP_SIDE_OPT_COMBINE        31
///组合策略的拆分
#define XTP_SIDE_OPT_SPLIT          32
///组合策略的管理员强制拆分
#define XTP_SIDE_OPT_SPLIT_FORCE    33
///组合策略的交易所强制拆分
#define XTP_SIDE_OPT_SPLIT_FORCE_EXCH    34

///未知或者无效买卖方向
#define XTP_SIDE_UNKNOWN        50
```
 3.返回

无


### 63. OnNewStrategyCreateReport


algo业务中当用户报送母单创建时，包括其他客户端报送创建母单，此用户所有连接都会有此推送消息，此函数将会被调用。

 1.函数原型
```cpp
virtual void OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, uint64_t session_id) {};
```
 2.参数

strategy_info：用户策略的具体信息

strategy_param：此母单策略的参数

session_id：资金账户对应的session_id，登录时得到

```cpp
///策略信息结构体
typedef struct XTPStrategyInfoStruct
{
	uint16_t				m_strategy_type;		///< 策略类型
	XTPStrategyStateType	m_strategy_state;		///< 策略状态
	uint64_t				m_client_strategy_id;	///< 客户策略id
	uint64_t				m_xtp_strategy_id;		///< xtp策略id
} XTPStrategyInfoStruct;
```
```cpp
///XTPStrategyStateType策略状态类型
typedef uint8_t XTPStrategyStateType;

///创建中
#define XTP_STRATEGY_STATE_CREATING		0
///已创建
#define XTP_STRATEGY_STATE_CREATED		1
///开始执行中
#define XTP_STRATEGY_STATE_STARTING		2
///已执行
#define XTP_STRATEGY_STATE_STARTED		3
///停止中
#define XTP_STRATEGY_STATE_STOPPING		4
///已停止
#define XTP_STRATEGY_STATE_STOPPED		5
///销毁中
#define XTP_STRATEGY_STATE_DESTROYING	6
///已销毁
#define XTP_STRATEGY_STATE_DESTROYED	7
///发生错误
#define XTP_STRATEGY_STATE_ERROR		8
```

 3.返回

无

 4.触发函数
```cpp
///algo业务中用户报算法单请求
virtual int InsertAlgoOrder(uint32_t strategy_type, uint64_t client_strategy_id, char* strategy_param, uint64_t session_id) = 0;
```


### 64. OnStrategyRecommendation


当算法推荐有响应时，该方法被调用。

 1.函数原型
```cpp
virtual void OnStrategyRecommendation(bool basket_flag, XTPStrategyRecommendationInfo* recommendation_info, char* strategy_param, XTPRI *error_info, int32_t request_id, bool is_last, uint64_t session_id) {};
```
 2.参数

basket_flag：是否将满足条件的推荐结果打包成母单篮的标志，与请求一致，如果此参数为true，那么请以返回的strategy_param为准

recommendation_info：推荐算法的具体信息，当basket_flag=true时，此结构体中的market和ticker将没有意义，此时请以strategy_param为准

strategy_param：算法参数，可直接用来创建母单，如果error_info.error_id为0时，有意义

error_info：请求推荐算法发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：此消息响应函数对应的请求ID

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///推荐算法结构体
typedef struct XTPStrategyRecommendationInfoStruct
{
	uint16_t					m_strategy_type;			///< 策略类型
	XTP_MARKET_TYPE				m_market;					///< 交易市场
	char						m_ticker[XTP_TICKER_LEN];	///< 证券代码
	char						m_reserved[64];				///< 保留域
} XTPStrategyRecommendationInfo;

```
```cpp
///XTP_MARKET_TYPE市场类型，交易里使用
typedef enum XTP_MARKET_TYPE
{
    XTP_MKT_INIT = 0,///<初始化值或者未知
    XTP_MKT_SZ_A = 1,///<深圳A股
    XTP_MKT_SH_A,    ///<上海A股
    XTP_MKT_BJ_A,    ///<北京A股
    XTP_MKT_HK,      ///<港股
    XTP_MKT_UNKNOWN   ///<未知交易市场类型
}XTP_MARKET_TYPE;

```

 3.返回

无

 4.触发函数
```cpp
///请求推荐算法
virtual int StrategyRecommendation(bool basket_flag, char* basket_param, uint64_t session_id, int32_t request_id) = 0;
```


### 65. OnModifyAlgoOrder


algo业务中修改已有策略单的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnModifyAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPRI *error_info, uint64_t session_id) {};
```

 2.参数
strategy_info：用户修改后策略单的具体信息
error_info：修改策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
session_id：资金账户对应的session_id，登录时得到
```cpp
///策略信息结构体
typedef struct XTPStrategyInfoStruct
{
	uint16_t				m_strategy_type;		///< 策略类型
	XTPStrategyStateType	m_strategy_state;		///< 策略状态
	uint64_t				m_client_strategy_id;	///< 客户策略id
	uint64_t				m_xtp_strategy_id;		///< xtp策略id
} XTPStrategyInfoStruct;
```
```cpp
///XTPStrategyStateType策略状态类型
typedef uint8_t XTPStrategyStateType;

///创建中
#define XTP_STRATEGY_STATE_CREATING		0
///已创建
#define XTP_STRATEGY_STATE_CREATED		1
///开始执行中
#define XTP_STRATEGY_STATE_STARTING		2
///已执行
#define XTP_STRATEGY_STATE_STARTED		3
///停止中
#define XTP_STRATEGY_STATE_STOPPING		4
///已停止
#define XTP_STRATEGY_STATE_STOPPED		5
///销毁中
#define XTP_STRATEGY_STATE_DESTROYING	6
///已销毁
#define XTP_STRATEGY_STATE_DESTROYED	7
///发生错误
#define XTP_STRATEGY_STATE_ERROR		8
```

 3.返回

无

 4.触发函数
```cpp
///algo业务中修改已有的算法单
virtual int ModifyAlgoOrder(uint64_t xtp_strategy_id, char* strategy_param, uint64_t session_id) = 0;
```


### 66. OnPauseAlgoOrder


algo业务中暂停指定策略指定证券算法单的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型
```cpp
virtual void OnPauseAlgoOrder(uint64_t xtp_strategy_id, XTPStrategyTickerInfo* ticker_info, XTPRI *error_info, int32_t request_id, uint64_t session_id) {};
```
◇ 2.参数

xtp_strategy_id：xtp算法单策略ID

ticker_info：指定证券信息，可以为null，为null表示暂停指定策略中所有证券的算法单

error_info：修改策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：此消息响应函数对应的请求ID

session_id：资金账户对应的session_id，登录时得到


```cpp
///策略中的证券信息结构体
typedef struct XTPStrategyTickerInfoStruct
{
	char						m_ticker[XTP_TICKER_LEN];	///< 证券代码
	XTP_MARKET_TYPE				m_market;					///< 交易市场
} XTPStrategyTickerInfo

```

◇ 3.返回

无

◇ 4. 触发函数
```cpp
///algo业务中暂停指定策略中指定证券的算法单请求
virtual int PauseAlgoOrder(uint64_t xtp_strategy_id, char* ticker, XTP_MARKET_TYPE market, uint64_t session_id, int32_t request_id) = 0;;
```


### 67. OnResumeAlgoOrder


algo业务中重启指定策略指定证券算法单的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型
```cpp
virtual void OnResumeAlgoOrder(uint64_t xtp_strategy_id, XTPStrategyTickerInfo* ticker_info, XTPRI *error_info, int32_t request_id, uint64_t session_id) {};
```
◇ 2.参数

xtp_strategy_id：xtp算法单策略ID

ticker_info：指定证券信息，可以为null，为null表示重启指定策略中所有证券的算法单

error_info：修改策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：此消息响应函数对应的请求ID

session_id：资金账户对应的session_id，登录时得到

```cpp
///策略信息结构体
///策略中的证券信息结构体
typedef struct XTPStrategyTickerInfoStruct
{
	char						m_ticker[XTP_TICKER_LEN];	///< 证券代码
	XTP_MARKET_TYPE				m_market;					///< 交易市场
} XTPStrategyTickerInfo
```

◇ 3.返回

无

◇ 4. 触发函数
```cpp
///algo业务中重启指定策略中指定证券的算法单请求
virtual int ResumeAlgoOrder(uint64_t xtp_strategy_id, XTPStrategyTickerInfo* ticker_info, uint64_t session_id, int32_t request_id) = 0;
```
