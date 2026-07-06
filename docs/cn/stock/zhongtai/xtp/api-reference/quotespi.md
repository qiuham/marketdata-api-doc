---
api_type: market_data
source_type: http_api
version: XTP 3.0
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
provider_name: 中泰证券
product: xtp
product_id: zhongtai-xtp
id: zhongtai-xtp-2074064395947831298
title: QuoteSpi
doc_id: 2074064395947831298
doc_category: 详细接口使用说明
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2074064395947831298'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-07-06
---

# QuoteSpi

## QuoteSpi


目录

- [QuoteSpi](#quotespi)
	- [1. 接口](#1-接口)
	- [2. 示例代码](#2-示例代码)
	- [3. OnDisconnected](#3-ondisconnected)
	- [4. OnError](#4-onerror)
	- [5. OnSubMarketData](#5-onsubmarketdata)
	- [6. OnUnSubMarketData](#6-onunsubmarketdata)
	- [7. OnDepthMarketData](#7-ondepthmarketdata)
	- [8. OnSubOrderBook](#8-onsuborderbook)
	- [9. OnUnSubOrderBook](#9-onunsuborderbook)
	- [10. OnOrderBook](#10-onorderbook)
	- [11. OnSubTickByTick](#11-onsubtickbytick)
	- [12. OnUnSubTickByTick](#12-onunsubtickbytick)
	- [13. OnTickByTick](#13-ontickbytick)
	- [14. OnSubscribeAllMarketData](#14-onsubscribeallmarketdata)
	- [15. OnUnSubscribeAllMarketData](#15-onunsubscribeallmarketdata)
	- [16. OnSubscribeAllOrderBook](#16-onsubscribeallorderbook)
	- [17. OnUnSubscribeAllOrderBook](#17-onunsubscribeallorderbook)
	- [18. OnSubscribeAllTickByTick](#18-onsubscribealltickbytick)
	- [19. OnUnSubscribeAllTickByTick](#19-onunsubscribealltickbytick)
	- [20. OnQueryAllTickers](#20-onqueryalltickers)
	- [21. OnQueryTickersPriceInfo](#21-onquerytickerspriceinfo)
	- [22. OnSubscribeAllOptionMarketData](#22-onsubscribealloptionmarketdata)
	- [23. OnUnSubscribeAllOptionMarketData](#23-onunsubscribealloptionmarketdata)
	- [24. OnSubscribeAllOptionOrderBook](#24-onsubscribealloptionorderbook)
	- [25. OnUnSubscribeAllOptionOrderBook](#25-onunsubscribealloptionorderbook)
	- [26. OnSubscribeAllOptionTickByTick](#26-onsubscribealloptiontickbytick)
	- [27. OnUnSubscribeAllOptionTickByTick](#27-onunsubscribealloptiontickbytick)
	- [28. OnQueryAllTickersFullInfo](#28-onqueryalltickersfullinfo)
	- [29. OnRebuildQuoteServerDisconnected](#29-onrebuildquoteserverdisconnected)
	- [30. OnRequestRebuildQuote](#30-onrequestrebuildquote)
	- [31. OnRebuildTickByTick](#31-onrebuildtickbytick)
	- [32. OnRebuildMarketData](#32-onrebuildmarketdata)
	- [33. OnQueryAllNQTickersFullInfo](#33-onqueryallnqtickersfullinfo)
	- [34. OnTickByTickLossRange](#34-ontickbyticklossrange)
	- [35. OnETFIOPVData](#35-onetfiopvdata)


QuoteSpi类提供了行情相关的回调接口，用户需要继承该类并重写这些接口，以获取响应数据。

### 1. 接口


```cpp
namespace XTP {
	namespace API {
		class QuoteSpi
		{
		public:

			///当客户端与行情后台通信连接断开时，该方法被调用。
			///@param reason 错误原因，请与错误代码表对应
			///@remark api不会自动重连，当断线发生时，请用户自行选择后续操作。可以在此函数中调用Login重新登录。注意用户重新登录后，需要重新订阅行情
			virtual void OnDisconnected(int reason) {};


			///错误应答
			///@param error_info 当服务器响应发生错误时的具体的错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 此函数只有在服务器发生错误时才会调用，一般无需用户处理
			virtual void OnError(XTPRI *error_info) {};

            ///逐笔丢包应答
			///@param begin_seq 当逐笔出现丢包时，丢包区间下限（可能与上限一致）
			///@param end_seq 当逐笔出现丢包时，丢包区间上限（可能与下限一致）
			///@remark 此函数只有在逐笔发生丢包时才会有调用，如果丢包的上下限一致，表示仅丢失了一个包，注意此包仅为数据包，包含1个或者多个逐笔数据
			virtual void OnTickByTickLossRange(int begin_seq, int end_seq) {};

			///订阅行情应答，包括股票、指数和期权
			///@param ticker 详细的合约订阅情况
			///@param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) {};

			///退订行情应答，包括股票、指数和期权
			///@param ticker 详细的合约取消订阅情况
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnUnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) {};

			///深度行情通知，包含买一卖一队列
			///@param market_data 行情数据
			///@param bid1_qty 买一队列数据
			///@param bid1_count 买一队列的有效委托笔数，即bid1_qty数组的长度，最大为50
			///@param max_bid1_count 买一队列总委托笔数
			///@param ask1_qty 卖一队列数据
			///@param ask1_count 卖一队列的有效委托笔数，即ask1_qty数组的长度，最大为50
			///@param max_ask1_count 卖一队列总委托笔数
			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count) {};

            /// ETF的IOPV通知
			/// @param iopv ETF的参考单位基金净值数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnETFIOPVData(IOPV *iopv) {};

			///订阅行情订单簿应答，包括股票
			///@param ticker 详细的合约订阅情况
			///@param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) {};

			///退订行情订单簿应答，包括股票
			///@param ticker 详细的合约取消订阅情况
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnUnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) {};

			///行情订单簿通知，包括股票
			///@param order_book 行情订单簿数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnOrderBook(XTPOB *order_book) {};

			///订阅逐笔行情应答，包括股票
			///@param ticker 详细的合约订阅情况
			///@param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) {};

			///退订逐笔行情应答，包括股票
			///@param ticker 详细的合约取消订阅情况
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			///@remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnUnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) {};

			///逐笔行情通知，包括股票
			///@param tbt_data 逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，需要根据type来区分是逐笔委托还是逐笔成交，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
			virtual void OnTickByTick(XTPTBT *tbt_data) {};

			///订阅全市场的股票行情应答
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///退订全市场的股票行情应答
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnUnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///订阅全市场的股票行情订单簿应答
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///退订全市场的股票行情订单簿应答
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnUnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///订阅全市场的股票逐笔行情应答
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///退订全市场的股票逐笔行情应答
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnUnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};


			///查询合约部分静态信息的应答
			///@param ticker_info 合约部分静态信息
			///@param error_info 查询合约部分静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次查询合约部分静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			virtual void OnQueryAllTickers(XTPQSI* ticker_info, XTPRI *error_info, bool is_last) {};

			///查询合约的最新价格信息应答
			///@param ticker_info 合约的最新价格信息
			///@param error_info 查询合约的最新价格信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			virtual void OnQueryTickersPriceInfo(XTPTPI* ticker_info, XTPRI *error_info, bool is_last) {};

			///订阅全市场的期权行情应答
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///退订全市场的期权行情应答
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnUnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///订阅全市场的期权行情订单簿应答
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///退订全市场的期权行情订单簿应答
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnUnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///订阅全市场的期权逐笔行情应答
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///退订全市场的期权逐笔行情应答
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@remark 需要快速返回
			virtual void OnUnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};

			///查询合约完整静态信息的应答
			///@param ticker_info 合约完整静态信息
			///@param error_info 查询合约完整静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次查询合约完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			virtual void OnQueryAllTickersFullInfo(XTPQFI* ticker_info, XTPRI *error_info, bool is_last) {};

			///查询新三板合约完整静态信息的应答
			///@param ticker_info 合约完整静态信息
			///@param error_info 查询合约完整静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
			///@param is_last 是否此次查询合约完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
			virtual void OnQueryAllNQTickersFullInfo(XTPNQFI* ticker_info, XTPRI *error_info, bool is_last) {};

			///当客户端与回补行情服务器通信连接断开时，该方法被调用。
			///@param reason 错误原因，请与错误代码表对应
			///@remark api不会自动重连，当断线发生时，请用户自行选择后续操作。回补服务器会在无消息交互后会定时断线，请注意仅在需要回补数据时才保持连接，无回补需求时，无需登陆。
			virtual void OnRebuildQuoteServerDisconnected(int reason) {};

			///请求回补指定频道的逐笔行情的总体结果应答
			///@param rebuild_result 当回补结束时被调用，如果回补结果失败，则msg参数表示失败原因
			///@remark 需要快速返回，仅在回补数据发送结束后调用，如果请求数据太多，一次性无法回补完，那么rebuild_result.result_code = XTP_REBUILD_RET_PARTLY，此时需要根据回补结果继续发起回补数据请求
			virtual void OnRequestRebuildQuote(XTPQuoteRebuildResultRsp* rebuild_result) {};

			///回补的逐笔行情数据
			///@param tbt_data 回补的逐笔行情数据
			///@remark 需要快速返回，此函数调用与OnTickByTick不在一个线程内，会在OnRequestRebuildQuote()之前回调
			virtual void OnRebuildTickByTick(XTPTBT *tbt_data) {};

			///回补的快照行情数据
			///@param md_data 回补的快照行情数据
			///@remark 需要快速返回，此函数调用与OnDepthMarketData不在一个线程内，会在OnRequestRebuildQuote()之前回调
			virtual void OnRebuildMarketData(XTPMD *md_data) {};
		};
	}
}
```


### 2. 示例代码


MyQuoteSpi继承QuoteSpi

以下是MyQuoteSpi.h文件
```cpp
#include "xtp_quote_api.h"

using namespace XTP::API;

class MyQuoteSpi : public QuoteSpi
{
public:
    explicit MyQuoteSpi();
    ~MyQuoteSpi();

    //接收行情
    void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count);
};
```
以下是MyQuoteSpi.cpp文件
```cpp
#include "MyQuoteSpi.h"

MyQuoteSpi::MyQuoteSpi() { }
MyQuoteSpi::~MyQuoteSpi() { }

//接收行情
void MyQuoteSpi::OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count)
{
	std::cout
#include

using namespace std;
using namespace XTP::API;

class MyQuoteSpi : public QuoteSpi
{
public:
    explicit MyQuoteSpi();
    ~MyQuoteSpi();

	void bindfunc(std::function f)
    {
        _disconnect = f;
    }

private:
    std::function _disconnect;
}
```
以下是MyQuoteSpi.cpp文件
```cpp
#include "MyQuoteSpi.h"

MyQuoteSpi::MyQuoteSpi() { }
MyQuoteSpi::~MyQuoteSpi() { }

void MyQuoteSpi::OnDisconnected(int reason)
{
	std::cout
#else
    #include
#endif

MyQuoteApi::MyQuoteApi()
{
}

// 创建并初始化交易API
bool MyQuoteApi::initialize()
{
	user_quote_api_ = XTP::API::QuoteApi::CreateQuoteApi(1, "./", log_level);
	if (user_quote_api_) {
		// 注册回调接口
		m_quote_spi = new MyQuoteSpi;
		user_quote_api_->RegisterSpi(m_quote_spi);
		// 在spi实例化后绑定重连函数指针
		m_quote_spi->bindfunc(std::bind(&MyQuoteApi::reloginQuote, this));
	}
}

// 重连函数，若最多只允许重连3次，每次重连间隔5秒
void MyQuoteApi::reloginQuote()
{
    if ((!m_loginQuoteInfo.quote_server_ip.empty()) && (m_loginQuoteInfo.quote_server_port != 0)
            && (!m_loginQuoteInfo.quote_username.empty()) && (!m_loginQuoteInfo.quote_password.empty())) {

		//重连次数
		int i_counter = 0;
        while (i_counter Login(m_loginQuoteInfo.quote_server_ip.c_str(),
                                             m_loginQuoteInfo.quote_server_port,
                                             m_loginQuoteInfo.quote_username.c_str(),
                                             m_loginQuoteInfo.quote_password.c_str(),
                                             m_loginQuoteInfo.quote_sock_type,
                                             m_loginQuoteInfo.local_ip.c_str());
            if (0 == ret) {
				std::cout **目前此函数不会被调用**。

 1.函数原型
```cpp
virtual void OnError(XTPRI *error_info) {};
```
 2.参数

error_info：当服务器响应发生错误时的具体的错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

```cpp
///错误信息的字符串长度
#define XTP_ERR_MSG_LEN  124
///响应信息
typedef struct XTPRspInfoStruct
{
	///错误代码
	int32_t	error_id;
	///错误信息
	char	error_msg[XTP_ERR_MSG_LEN];
} XTPRI;
```

 3.返回

无


### 5. OnSubMarketData


订阅行情应答，包括股票、指数和期权。

每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) {};
````
 2.参数

Ticker：详细的合约订阅情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

```cpp
///指定的合约
typedef struct XTPSpecificTickerStruct
{
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
	char	ticker[XTP_TICKER_LEN];
} XTPST;

///XTP_EXCHANGE_TYPE是交易所类型，行情里使用
typedef enum XTP_EXCHANGE_TYPE
{
	XTP_EXCHANGE_SH = 1,	///<上证
	XTP_EXCHANGE_SZ,		///<深证
	XTP_EXCHANGE_NQ,		///<新三板 全国中小企业股份转让系统
    XTP_EXCHANGE_UNKNOWN	///<不存在的交易所类型
}XTP_EXCHANGE_TYPE;

/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
```

 3.返回

无

 4.触发函数
```cpp
// 订阅行情，包括股票、指数和期权
virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
```


### 6. OnUnSubMarketData


退订行情应答，包括股票、指数和期权。

每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnUnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) {};
```
 2.参数

Ticker：详细的合约订阅情况

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///指定的合约
typedef struct XTPSpecificTickerStruct
{
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
	char	ticker[XTP_TICKER_LEN];
} XTPST;
```

 3.返回

无

 4.触发函数
```cpp
// 退订行情，包括股票、指数和期权
virtual int UnSubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
```


### 7. OnDepthMarketData


深度行情通知，包含买一卖一队列。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count) {};
```
 2.参数

market_data：行情数据

bid1_qty：买一队列数据

bid1_count：买一队列的有效委托笔数

max_bid1_count：买一队列总委托笔数

ask1_qty：卖一队列数据

ask1_count：卖一队列的有效委托笔数

max_ask1_count：卖一队列总委托笔数

```cpp
///行情
typedef struct XTPMarketDataStruct
{
    // 代码
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    char	ticker[XTP_TICKER_LEN];

    // 价格
	///最新价
	double	last_price;
	///昨收盘
	double	pre_close_price;
	///今开盘
	double	open_price;
	///最高价
	double	high_price;
	///最低价
	double	low_price;
    ///今收盘
    double	close_price;

    // 期权数据
    ///昨日持仓量(张)(目前未填写)
    int64_t pre_total_long_positon;
    ///持仓量(张)
	int64_t	total_long_positon;
    ///昨日结算价（SH）
    double	pre_settl_price;
    ///今日结算价（SH）
	double	settl_price;

	// 涨跌停
	///涨停价
	double	upper_limit_price;
	///跌停价
	double	lower_limit_price;
	///预留
	double	pre_delta;
	///预留
	double	curr_delta;

    /// 时间类，格式为YYYYMMDDHHMMSSsss
    int64_t data_time;

    // 量额数据
    ///数量，为总成交量（单位股，与交易所一致）
    int64_t	qty;
    ///成交金额，为总成交金额（单位元，与交易所一致）
    double	turnover;
    ///预留(无意义)
    double	avg_price;

    // 买卖盘
    ///十档申买价
    double bid[10];
    ///十档申卖价
    double	ask[10];
    ///十档申买量
    int64_t	bid_qty[10];
    ///十档申卖量
    int64_t	ask_qty[10];

    // 额外数据
    ///成交笔数
    int64_t trades_count;
    ///当前交易状态说明，参阅《XTP API常见问题.doc》文档
    char ticker_status[8];
    ///数据
    union {
        XTPMarketDataStockExData  stk;
        XTPMarketDataOptionExData opt;
    	XTPMarketDataBondExData  bond;
    } ;
    ///决定了union是哪种数据类型 (2.2.32版本以前所用字段，仅为了保持兼容，不建议使用该字段)
    XTP_MARKETDATA_TYPE data_type;
    ///决定了union是哪种数据类型（2.2.32版本新增字段，更详细区分了行情快照数据类型）
    XTP_MARKETDATA_TYPE_V2 data_type_v2;
} XTPMD;

///股票、基金等额外数据
struct XTPMarketDataStockExData {
    ///委托买入总量(SH,SZ)
    int64_t total_bid_qty;
    ///委托卖出总量(SH,SZ)
    int64_t total_ask_qty;
    ///加权平均委买价格(SH,SZ)
    double ma_bid_price;
    ///加权平均委卖价格(SH,SZ)
    double ma_ask_price;
    ///债券加权平均委买价格(SH)
    double ma_bond_bid_price;
    ///债券加权平均委卖价格(SH)
    double ma_bond_ask_price;
    ///债券到期收益率(SH)
    double yield_to_maturity;
    ///基金实时参考净值(SH,SZ)
    double iopv;
    ///ETF申购笔数(SH)
    int32_t etf_buy_count;
    ///ETF赎回笔数(SH)
    int32_t etf_sell_count;
    ///ETF申购数量(SH)
    double etf_buy_qty;
    ///ETF申购金额(SH)
    double etf_buy_money;
    ///ETF赎回数量(SH)
    double etf_sell_qty;
    ///ETF赎回金额(SH)
    double etf_sell_money;
    ///权证执行的总数量(SH)
    double total_warrant_exec_qty;
    ///权证跌停价格（元）(SH)
    double warrant_lower_price;
    ///权证涨停价格（元）(SH)
    double warrant_upper_price;
    ///买入撤单笔数(SH)
    int32_t cancel_buy_count;
    ///卖出撤单笔数(SH)
    int32_t cancel_sell_count;
    ///买入撤单数量(SH)
    double cancel_buy_qty;
    ///卖出撤单数量(SH)
    double cancel_sell_qty;
    ///买入撤单金额(SH)
    double cancel_buy_money;
    ///卖出撤单金额(SH)
    double cancel_sell_money;
    ///买入总笔数(SH)
    int64_t total_buy_count;
    ///卖出总笔数(SH)
    int64_t total_sell_count;
    ///买入委托成交最大等待时间(SH)
    int32_t duration_after_buy;
    ///卖出委托成交最大等待时间(SH)
    int32_t duration_after_sell;
    ///买方委托价位数(SH)
    int32_t num_bid_orders;
    ///卖方委托价位数(SH)
    int32_t num_ask_orders;

    ///基金T-1日净值(SZ)
    double pre_iopv;
    ///预留
    int64_t r1;
    ///预留
    int64_t r2;
};

///期权额外数据
struct XTPMarketDataOptionExData {
    ///波段性中断参考价(SH)
    double  auction_price;
    ///波段性中断集合竞价虚拟匹配量(SH)
    int64_t auction_qty;
    ///最近询价时间(SH)
    int64_t last_enquiry_time;
};

///债券额外数据
struct XTPMarketDataBondExData {
    ///委托买入总量(SH,SZ)
    int64_t total_bid_qty;
    ///委托卖出总量(SH,SZ)
    int64_t total_ask_qty;
    ///加权平均委买价格(SZ)
    double ma_bid_price;
    ///加权平均委卖价格(SZ)
    double ma_ask_price;
    ///债券加权平均委买价格(SH)
    double ma_bond_bid_price;
    ///债券加权平均委卖价格(SH)
    double ma_bond_ask_price;
    ///债券到期收益率(SH)
    double yield_to_maturity;
	///匹配成交最近价(SZ)
	double match_lastpx;
    ///债券加权平均价格(SH)
    double ma_bond_price;
    ///匹配成交成交量(SZ)
    int64_t match_qty;
    ///匹配成交成交金额(SZ)
    double match_turnover;
    ///预留
    double r4;
    ///预留
    double r5;
    ///预留
    double r6;
    ///预留
    double r7;
    ///预留
    double r8;
    ///买入撤单笔数(SH)
    int32_t cancel_buy_count;
    ///卖出撤单笔数(SH)
    int32_t cancel_sell_count;
    ///买入撤单数量(SH)
    double cancel_buy_qty;
    ///卖出撤单数量(SH)
    double cancel_sell_qty;
    ///买入撤单金额(SH)
    double cancel_buy_money;
    ///卖出撤单金额(SH)
    double cancel_sell_money;
    ///买入总笔数(SH)
    int64_t total_buy_count;
    ///卖出总笔数(SH)
    int64_t total_sell_count;
    ///买入委托成交最大等待时间(SH)
    int32_t duration_after_buy;
    ///卖出委托成交最大等待时间(SH)
    int32_t duration_after_sell;
    ///买方委托价位数(SH)
    int32_t num_bid_orders;
    ///卖方委托价位数(SH)
    int32_t num_ask_orders;
    ///时段(SHL2)，L1快照数据没有此字段，具体字段说明参阅《上海新债券Level2行情说明.doc》文档
    char instrument_status[8];
};

///XTP_MARKETDATA_TYPE是行情快照数据类型，2.2.32以前版本所用
enum XTP_MARKETDATA_TYPE {
    XTP_MARKETDATA_ACTUAL = 0, // 现货(股票/基金/债券等)
    XTP_MARKETDATA_OPTION = 1, // 期权
};

///XTP_MARKETDATA_TYPE_V2是行情快照数据类型，2.2.32版本新增字段
enum XTP_MARKETDATA_TYPE_V2 {
    XTP_MARKETDATA_V2_INDEX  = 0, // 指数
    XTP_MARKETDATA_V2_OPTION = 1, // 期权
    XTP_MARKETDATA_V2_ACTUAL = 2, // 现货(股票/基金等)
    XTP_MARKETDATA_V2_BOND   = 3, // 债券
};
```

 3.返回

无

 4.订阅函数
```cpp
// 订阅行情快照，包括股票、指数和期权
virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
// 订阅全市场的股票行情快照
virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
// 订阅全市场的期权行情快照
virtual int SubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 8. OnSubOrderBook


订阅行情订单簿应答。

每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) {};
```
 2.参数

ticker：详细的合约订阅情况

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

```cpp
///指定的合约
typedef struct XTPSpecificTickerStruct
{
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
	char	ticker[XTP_TICKER_LEN];
} XTPST;
```

 3.返回

无

 4.触发函数
```cpp
// 订阅行情订单簿，包括股票
virtual int SubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
```


### 9. OnUnSubOrderBook


退订行情订单簿应答。

每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnUnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) {};
```
 2.参数

ticker：详细的合约取消订阅情况

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

```cpp
///指定的合约
typedef struct XTPSpecificTickerStruct
{
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
	char	ticker[XTP_TICKER_LEN];
} XTPST;
```

 3.返回

无

 4.触发函数
```cpp
// 退订行情订单簿，包括股票
virtual int UnSubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
```


### 10. OnOrderBook


行情订单簿通知，包括股票。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnOrderBook(XTPOB *order_book) {};
```
 2.参数

order_book：行情订单簿数据

```cpp
///订单薄
typedef struct OrderBookStruct {
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    char    ticker[XTP_TICKER_LEN];

    ///最新价
    double last_price;
    ///数量，为总成交量
    int64_t qty;
    ///成交金额，为总成交金额
    double  turnover;
    ///成交笔数
    int64_t trades_count;

    // 买卖盘
    ///十档申买价
    double bid[10];
    ///十档申卖价
    double  ask[10];
    ///十档申买量
    int64_t bid_qty[10];
    ///十档申卖量
    int64_t ask_qty[10];
    /// 时间类
    int64_t data_time;
} XTPOB;
```

 3.返回

无

 4.订阅函数
```cpp
// 订阅行情订单簿，包括股票
virtual int SubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
// 订阅全市场的股票行情订单簿
virtual int SubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
// 订阅全市场的期权行情订单簿（目前期权没有OB数据）
virtual int SubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 11. OnSubTickByTick


订阅逐笔行情应答。

每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) {};
```
 2.参数

ticker：详细的合约订阅情况

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

```cpp
///指定的合约
typedef struct XTPSpecificTickerStruct
{
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
	char	ticker[XTP_TICKER_LEN];
} XTPST;
```

 3.返回

无

 4.触发函数
```cpp
// 订阅逐笔行情，包括股票
virtual int SubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
```


### 12. OnUnSubTickByTick


退订逐笔行情应答，包括股票

每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnUnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) {};
```
 2.参数

ticker：详细的合约取消订阅情况

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

```cpp
///指定的合约
typedef struct XTPSpecificTickerStruct
{
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
	char	ticker[XTP_TICKER_LEN];
} XTPST;
```

 3.返回

无

 4.触发函数
```cpp
// 退订逐笔行情，包括股票
virtual int UnSubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
```


### 13. OnTickByTick


逐笔行情通知，包括股票。

逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，需要根据type来区分是逐笔委托还是逐笔成交，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnTickByTick(XTPTBT *tbt_data) {};
```
 2.参数

tbt_data
逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，需要根据type来区分是逐笔委托还是逐笔成交

```cpp
///逐笔数据信息
typedef struct XTPTickByTickStruct {
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    char ticker[XTP_TICKER_LEN];
    /// SH: 业务序号（委托成交统一编号，同一个channel_no内连续，此seq区别于联合体内的seq，channel_no等同于联合体内的channel_no）
    /// SZ: 无意义
    int64_t seq;
    ///委托时间 or 成交时间
    int64_t data_time;
    ///委托 or 成交
    XTP_TBT_TYPE type;

    union {
        XTPTickByTickEntrust entrust;
        XTPTickByTickTrade     trade;
        XTPTickByTickStatus    state;
    };
} XTPTBT;

///XTP_TBT_TYPE是一个逐笔回报类型
typedef enum XTP_TBT_TYPE {
	XTP_TBT_ENTRUST = 1,	///<逐笔委托
	XTP_TBT_TRADE = 2,		///<逐笔成交
	XTP_TBT_STATE = 3,      ///<逐笔状态订单
}XTP_TBT_TYPE;

///逐笔委托
struct XTPTickByTickEntrust {
    ///频道代码
    int32_t channel_no;
    ///SH: 委托序号(委托单独编号, 同一channel_no内连续)
    ///SZ: 委托序号(委托成交统一编号, 同一channel_no内连续)
    int64_t seq;
    ///委托价格
    double  price;
    ///SH: 剩余委托数量(balance)
    ///SZ: 委托数量
    int64_t qty;
    ///SH: 'B':买; 'S':卖
    ///SZ: '1':买; '2':卖; 'G':借入; 'F':出借
    char  side;
    ///SH: 'A': 增加; 'D': 删除
    ///SZ: 订单类别: '1': 市价; '2': 限价; 'U': 本方最优
    char ord_type;
    ///SH: 原始订单号
    ///SZ: 无意义
    int64_t order_no;
};

///逐笔成交
struct XTPTickByTickTrade {
    ///频道代码
    int32_t channel_no;
    ///SH: 成交序号(成交单独编号, 同一channel_no内连续)
    ///SZ: 成交序号(委托成交统一编号, 同一channel_no内连续)
    int64_t seq;
    ///成交价格
    double price;
    ///成交量
    int64_t qty;
    ///成交金额(仅适用上交所)
    double money;
    ///买方订单号
    int64_t bid_no;
    ///卖方订单号
    int64_t ask_no;
    /// SH: 内外盘标识('B':主动买; 'S':主动卖; 'N':未知)
    /// SZ: 成交标识('4':撤; 'F':成交)
    char trade_flag;
};

///逐笔状态订单
struct XTPTickByTickStatus {
    ///频道代码
    int32_t channel_no;
    ///同一channel_no内连续
    int64_t seq;
    ///状态信息
    char flag[8];
};
```

 3.返回

无

 4.订阅函数
```cpp
// 订阅逐笔行情，包括股票
virtual int SubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
// 订阅全市场的股票逐笔行情
virtual int SubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
// 订阅全市场的期权逐笔行情（目前期权没有逐笔数据）
virtual int SubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 14. OnSubscribeAllMarketData


订阅全市场的股票行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 订阅全市场的股票行情
virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 15. OnUnSubscribeAllMarketData


退订全市场的股票行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnUnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 退订全市场的股票行情
virtual int UnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 16. OnSubscribeAllOrderBook


订阅全市场的股票行情订单簿应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 订阅全市场的股票行情订单簿
virtual int SubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 17. OnUnSubscribeAllOrderBook


退订全市场的股票行情订单簿应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnUnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 退订全市场的股票行情订单簿
virtual int UnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 18. OnSubscribeAllTickByTick


阅全市场的股票逐笔行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 订阅全市场的股票逐笔行情
virtual int SubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 19. OnUnSubscribeAllTickByTick


退订全市场的股票逐笔行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnUnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 退订全市场的股票逐笔行情
virtual int UnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 20. OnQueryAllTickers


查询合约部分静态信息的应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryAllTickers(XTPQSI* ticker_info, XTPRI *error_info, bool is_last) {};
```
 2.参数

ticker_info：合约部分静态信息

error_info：查询合约部分静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询合约部分静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

```cpp
///股票行情静态信息
typedef struct XTPQuoteStaticInfo {
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    char    ticker[XTP_TICKER_LEN];
    /// 合约名称
    char    ticker_name[XTP_TICKER_NAME_LEN];
    /// 合约类型
	XTP_TICKER_TYPE ticker_type;
    ///昨收盘
    double  pre_close_price;
    ///涨停板价
    double  upper_limit_price;
    ///跌停板价
    double  lower_limit_price;
	///最小变动价位
	double  price_tick;
    /// 合约最小交易量(买)
    int32_t  buy_qty_unit;
    /// 合约最小交易量(卖)
	int32_t sell_qty_unit;
} XTPQSI;
```

 3.返回

无

 4.触发函数
```cpp
// 获取当前交易日合约部分静态信息
virtual int QueryAllTickers(XTP_EXCHANGE_TYPE exchange_id) = 0;
```


### 21. OnQueryTickersPriceInfo


查询合约的最新价格信息应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryTickersPriceInfo(XTPTPI* ticker_info, XTPRI *error_info, bool is_last) {};
```
 2.参数

ticker_info：合约的最新价格信息

error_info：查询合约的最新价格信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

```cpp
///供查询的最新信息
typedef struct XTPTickerPriceInfo {
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    char ticker[XTP_TICKER_LEN];
    ///最新价
    double last_price;
} XTPTPI;
```

 3.返回

无

 4.触发函数
```cpp
// 获取合约的最新价格信息
virtual int QueryTickersPriceInfo(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
// 获取所有合约的最新价格信息
virtual int QueryAllTickersPriceInfo() = 0;
```


### 22. OnSubscribeAllOptionMarketData


订阅全市场的期权行情快照应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 订阅全市场的期权行情
virtual int SubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 23. OnUnSubscribeAllOptionMarketData


退订全市场的期权行情快照应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnUnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 退订全市场的期权行情
virtual int UnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 24. OnSubscribeAllOptionOrderBook


订阅全市场的期权行情订单簿应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

目前期权没有OB数据。

 1.函数原型
```cpp
virtual void OnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 订阅全市场的期权行情订单簿
virtual int SubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 25. OnUnSubscribeAllOptionOrderBook


退订全市场的期权行情订单簿应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
目前期权没有OB数据。


 1.函数原型
```cpp
virtual void OnUnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id,
XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 退订全市场的期权行情订单簿
virtual int UnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 26. OnSubscribeAllOptionTickByTick


订阅全市场的期权逐笔行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

目前期权没有逐笔数据。

 1.函数原型
```cpp
virtual void OnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 订阅全市场的期权逐笔行情
virtual int SubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 27. OnUnSubscribeAllOptionTickByTick


退订全市场的期权逐笔行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
目前期权没有逐笔数据。

 1.函数原型
```cpp
virtual void OnUnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id,
XTPRI *error_info) {};
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

 3.返回

无

 4.触发函数
```cpp
// 退订全市场的期权逐笔行情
virtual int UnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```


### 28. OnQueryAllTickersFullInfo


查询合约完整静态信息的应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryAllTickersFullInfo(XTPQFI* ticker_info, XTPRI *error_info, bool is_last) {};
```
 2.参数

ticker_info：合约完整静态信息

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询合约完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

```cpp
///股票行情全量静态信息
typedef struct XTPQuoteFullInfo {
	XTP_EXCHANGE_TYPE  exchange_id;							///<交易所代码
	char               ticker[XTP_TICKER_LEN];				///<证券代码
	char               ticker_name[XTP_TICKER_NAME_LEN];	///<证券名称
	XTP_SECURITY_TYPE      security_type;					///<合约详细类型
	XTP_QUALIFICATION_TYPE ticker_qualification_class;		///<合约适当性类别
	bool is_registration;									///<是否注册制(仅适用创业板股票，创新企业股票及存托凭证)
	bool is_VIE;											///<是否具有协议控制架构(仅适用创业板股票，创新企业股票及存托凭证)
	bool is_noprofit;										///<是否尚未盈利(仅适用创业板股票，创新企业股票及存托凭证)
	bool is_weighted_voting_rights;							///<是否存在投票权差异(仅适用创业板股票，创新企业股票及存托凭证)
	bool is_have_price_limit;								///<是否有涨跌幅限制(注：不提供具体幅度，可通过涨跌停价和昨收价来计算幅度)
	bool is_inventory										///<是否为存量科创板股票（即2025.07.13日前上市的）。1=是；0=否；(注：暂时不启用，待交易所对科创板成长层股票新增特殊标识后启用，启用前该字段无意义)
	double upper_limit_price;								///<涨停价（仅在有涨跌幅限制时有效）
	double lower_limit_price;								///<跌停价（仅在有涨跌幅限制时有效）
	double pre_close_price;									///<昨收价
	double price_tick;										///<价格最小变动价位
	int32_t bid_qty_upper_limit;							///<限价买委托数量上限
	int32_t bid_qty_lower_limit;							///<限价买委托数量下限
	int32_t bid_qty_unit;									///<限价买数量单位
	int32_t ask_qty_upper_limit;							///<限价卖委托数量上限
	int32_t ask_qty_lower_limit;							///<限价卖委托数量下限
	int32_t ask_qty_unit;									///<限价卖数量单位
	int32_t market_bid_qty_upper_limit;						///<市价买委托数量上限
	int32_t market_bid_qty_lower_limit;						///<市价买委托数量下限
	int32_t market_bid_qty_unit;							///<市价买数量单位
	int32_t market_ask_qty_upper_limit;						///<市价卖委托数量上限
	int32_t market_ask_qty_lower_limit;						///<市价卖委托数量上限
	int32_t market_ask_qty_unit;							///<市价卖数量单位
	XTP_SECURITY_STATUS security_status;                    ///<证券状态
	uint32_t unknown1;                                      ///<保留字段
	uint64_t unknown[3];                                    ///<保留字段
}XTPQFI;

///XTP_SECURITY_TYPE是一个证券详细分类枚举类型
typedef enum XTP_SECURITY_TYPE {
	/// 主板股票
	XTP_SECURITY_MAIN_BOARD = 0,
	/// 中小板股票
	XTP_SECURITY_SECOND_BOARD,
	/// 创业板股票
	XTP_SECURITY_STARTUP_BOARD,
	/// 指数
	XTP_SECURITY_INDEX,
	/// 科创板股票(上海)
	XTP_SECURITY_TECH_BOARD = 4,
	/// 国债
	XTP_SECURITY_STATE_BOND = 5,
	/// 企业债
	XTP_SECURITY_ENTERPRICE_BOND = 6,
	/// 公司债
	XTP_SECURITY_COMPANEY_BOND = 7,
	/// 转换债券
	XTP_SECURITY_CONVERTABLE_BOND = 8,
	/// 国债逆回购
	XTP_SECURITY_NATIONAL_BOND_REVERSE_REPO = 12,
	/// 本市场股票 ETF
	XTP_SECURITY_ETF_SINGLE_MARKET_STOCK = 14,
	/// 跨市场股票 ETF
	XTP_SECURITY_ETF_INTER_MARKET_STOCK,
	/// 跨境股票 ETF
	XTP_SECURITY_ETF_CROSS_BORDER_STOCK = 16,
	/// 本市场实物债券 ETF
	XTP_SECURITY_ETF_SINGLE_MARKET_BOND = 17,
    /// 现金债券ETF
    XTP_SECURITY_TYPE_ETF_CASH_BOND = 18,
	/// 黄金 ETF
	XTP_SECURITY_ETF_GOLD = 19,
    // 商品期货ETF
    XTP_SECURITY_ETF_COMMODITY_FUTURES = 22,
	/// 上市开放式基金LOF
	XTP_SECURITY_LOF = 23,
	/// 分级基金子基金
	XTP_SECURITY_STRUCTURED_FUND_CHILD = 24,
	/// 深交所仅申赎基金
	XTP_SECURITY_SZSE_RECREATION_FUND = 26,
	/// 个股期权
	XTP_SECURITY_STOCK_OPTION = 29,
	/// ETF期权
	XTP_SECURITY_ETF_OPTION = 30,
	/// 配股
	XTP_SECURITY_ALLOTMENT = 100,

	/// 上交所申赎型货币基金
	XTP_SECURITY_MONETARY_FUND_SHCR = 110,
	/// 上交所交易型货币基金
	XTP_SECURITY_MONETARY_FUND_SHTR = 111,
	/// 深交所货币基金
	XTP_SECURITY_MONETARY_FUND_SZ = 112,
	/// 跨境LOF
	XTP_SECURITY_LOF_CROSS_BORDER = 113,

	/// 其他
	XTP_SECURITY_OTHERS = 255
}XTP_SECURITY_TYPE;

///XTP_QUALIFICATION_TYPE是一个证券适当性枚举类型
typedef enum  XTP_QUALIFICATION_TYPE
{
	XTP_QUALIFICATION_PUBLIC = 0,			///<公众投资者，合格投资者与机构投资者均可
	XTP_QUALIFICATION_COMMON = 1,			///<仅合格投资者与公众投资者
	XTP_QUALIFICATION_ORGANIZATION = 2,		///<仅限机构投资者
	XTP_QUALIFICATION_UNKNOWN = 3		///<未知，期权等可能为此种类型
}XTP_QUALIFICATION_TYPE;

///XTP_SECURITY_STATUS是一个证券状态枚举类型
typedef enum  XTP_SECURITY_STATUS
{
	XTP_SECURITY_STATUS_ST = 0,         ///< 风险警示板
	XTP_SECURITY_STATUS_N_IPO,          ///< 首日上市
	XTP_SECURITY_STATUS_COMMON,         ///< 普通
	XTP_SECURITY_STATUS_RESUME,         ///< 恢复上市
	XTP_SECURITY_STATUS_DELISTING = 10, ///< 退市整理期
	XTP_SECURITY_STATUS_OTHERS = 255    ///< 其他
}XTP_SECURITY_STATUS;

/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
/// 存放证券名称的字符串长度
#define XTP_TICKER_NAME_LEN 64
```

 3.返回

无

 4.触发函数
```cpp
// 获取所有合约的详细静态信息，包括指数等非可交易的
virtual int QueryAllTickersFullInfo(XTP_EXCHANGE_TYPE exchange_id) = 0;
```


### 29. OnRebuildQuoteServerDisconnected


当客户端与回补行情服务器通信连接断开时，该方法被调用。

Api不会自动重连，当断线发生时，请用户自行选择后续操作。回补服务器会在无消息交互后会定时断线，请注意仅在需要回补数据时才保持连接，无回补需求时，无需登陆。

 1.函数原型
```cpp
virtual void OnDisconnected(int reason) {};
```
 2.参数

Reason：错误原因，目前仅一个原因，可不用参考

 3.返回

无

### 30. OnRequestRebuildQuote


请求回补指定频道的逐笔行情的总体结果应答。

需要快速返回，仅在回补数据发送结束后调用，如果请求数据太多，一次性无法回补完，那么rebuild_result.result_code = XTP_REBUILD_RET_PARTLY，此时需要根据回补结果继续发起回补数据请求。

 1.函数原型
```cpp
virtual void OnRequestRebuildQuote(XTPQuoteRebuildResultRsp* rebuild_result) {};
```
 2.参数

rebuild_result：当回补结束时被调用，如果回补结果失败，则msg参数表示失败原因

```cpp
///实时行情回补响应结构体
typedef struct XTPQuoteRebuildResultRsp
{
    ///请求id 请求包带过来的id
    int32_t                     request_id;
    ///市场类型 上海 深圳
    XTP_EXCHANGE_TYPE           exchange_id;
    ///总共返回的数据条数
    uint32_t                    size;
    ///逐笔数据 通道号
    int16_t                     channel_number;
    ///逐笔 表示序列号begin; 快照 表示时间begin(格式为YYYYMMDDHHMMSSsss)
    int64_t                     begin;
    ///逐笔 表示序列号end; 快照 表示时间end(格式为YYYYMMDDHHMMSSsss)
    int64_t                     end;
    ///结果类型码
    XTP_REBUILD_RET_TYPE        result_code;
    ///结果信息文本
    char                        msg[64];
}XTPQuoteRebuildResultRsp;
```
```cpp
///XTP_REBUILD_RET_TYPE 实时行情回补返回结果类型
typedef enum XTP_REBUILD_RET_TYPE {
    XTP_REBUILD_RET_COMPLETE    = 1,	///<全部数据
    XTP_REBUILD_RET_PARTLY      = 2,	///<部分数据
    XTP_REBUILD_RET_NO_DATA     = 3,	///<没有数据
    XTP_REBUILD_RET_PARAM_ERR   = 4,	///<参数错误
    XTP_REBUILD_RET_FREQUENTLY  = 5,	///<请求频繁
}XTP_REBUILD_RET_TYPE;
```

 3.返回

无

 4.触发函数
```cpp
///请求回补指定行情，包括快照和逐笔
virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;
```


### 31. OnRebuildTickByTick


回补的逐笔行情数据。

需要快速返回，此函数调用与OnTickByTick不在一个线程内，会在OnRequestRebuildQuote()之前回调。

 1.函数原型
```cpp
virtual void OnRebuildTickByTick(XTPTBT *tbt_data) {};
```
 2.参数

tbt_data：回补的逐笔行情数据

```cpp
///逐笔数据信息
typedef struct XTPTickByTickStruct {
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    char ticker[XTP_TICKER_LEN];
    /// SH: 业务序号（委托成交统一编号，同一个channel_no内连续，此seq区别于联合体内的seq，channel_no等同于联合体内的channel_no）
    /// SZ: 无意义
    int64_t seq;
    ///委托时间 or 成交时间
    int64_t data_time;
    ///委托 or 成交
    XTP_TBT_TYPE type;

    union {
        XTPTickByTickEntrust entrust;
        XTPTickByTickTrade     trade;
        XTPTickByTickStatus    state;
    };
} XTPTBT;

///XTP_TBT_TYPE是一个逐笔回报类型
typedef enum XTP_TBT_TYPE {
	XTP_TBT_ENTRUST = 1,	///<逐笔委托
	XTP_TBT_TRADE = 2,		///<逐笔成交
	XTP_TBT_STATE = 3,      ///<逐笔状态订单
}XTP_TBT_TYPE;

///逐笔委托
struct XTPTickByTickEntrust {
    ///频道代码
    int32_t channel_no;
    ///SH: 委托序号(委托单独编号, 同一channel_no内连续)
    ///SZ: 委托序号(委托成交统一编号, 同一channel_no内连续)
    int64_t seq;
    ///委托价格
    double  price;
    ///SH: 剩余委托数量(balance)
    ///SZ: 委托数量
    int64_t qty;
    ///SH: 'B':买; 'S':卖
    ///SZ: '1':买; '2':卖; 'G':借入; 'F':出借
    char  side;
    ///SH: 'A': 增加; 'D': 删除
    ///SZ: 订单类别: '1': 市价; '2': 限价; 'U': 本方最优
    char ord_type;
    ///SH: 原始订单号
    ///SZ: 无意义
    int64_t order_no;
};

///逐笔成交
struct XTPTickByTickTrade {
    ///频道代码
    int32_t channel_no;
    ///SH: 成交序号(成交单独编号, 同一channel_no内连续)
    ///SZ: 成交序号(委托成交统一编号, 同一channel_no内连续)
    int64_t seq;
    ///成交价格
    double price;
    ///成交量
    int64_t qty;
    ///成交金额(仅适用上交所)
    double money;
    ///买方订单号
    int64_t bid_no;
    ///卖方订单号
    int64_t ask_no;
    /// SH: 内外盘标识('B':主动买; 'S':主动卖; 'N':未知)
    /// SZ: 成交标识('4':撤; 'F':成交)
    char trade_flag;
};

///逐笔状态订单
struct XTPTickByTickStatus {
    ///频道代码
    int32_t channel_no;
    ///同一channel_no内连续
    int64_t seq;
    ///状态信息
    char flag[8];
};
```

 3.返回

无

 4.触发函数
```cpp
///请求回补指定行情，包括快照和逐笔
virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;
```


### 32. OnRebuildMarketData


回补的快照行情数据。

需要快速返回，此函数调用与OnDepthMarketData不在一个线程内，会在OnRequestRebuildQuote()之前回调。

 1.函数原型
```cpp
virtual void OnRebuildMarketData(XTPMD *md_data) {};
```
 2.参数

md_data：回补的快照行情数据


```cpp
///行情
typedef struct XTPMarketDataStruct
{
    // 代码
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    char	ticker[XTP_TICKER_LEN];

    // 价格
	///最新价
	double	last_price;
	///昨收盘
	double	pre_close_price;
	///今开盘
	double	open_price;
	///最高价
	double	high_price;
	///最低价
	double	low_price;
    ///今收盘
    double	close_price;

    // 期权数据
    ///昨日持仓量(张)(目前未填写)
    int64_t pre_total_long_positon;
    ///持仓量(张)
	int64_t	total_long_positon;
    ///昨日结算价（SH）
    double	pre_settl_price;
    ///今日结算价（SH）
	double	settl_price;

	// 涨跌停
	///涨停价
	double	upper_limit_price;
	///跌停价
	double	lower_limit_price;
	///预留
	double	pre_delta;
	///预留
	double	curr_delta;

    /// 时间类，格式为YYYYMMDDHHMMSSsss
    int64_t data_time;

    // 量额数据
    ///数量，为总成交量（单位股，与交易所一致）
    int64_t	qty;
    ///成交金额，为总成交金额（单位元，与交易所一致）
    double	turnover;
    ///预留(无意义)
    double	avg_price;

    // 买卖盘
    ///十档申买价
    double bid[10];
    ///十档申卖价
    double	ask[10];
    ///十档申买量
    int64_t	bid_qty[10];
    ///十档申卖量
    int64_t	ask_qty[10];

    // 额外数据
    ///成交笔数
    int64_t trades_count;
    ///当前交易状态说明，参阅《XTP API常见问题.doc》文档
    char ticker_status[8];
    ///数据
    union {
        XTPMarketDataStockExData  stk;
        XTPMarketDataOptionExData opt;
    	XTPMarketDataBondExData  bond;
    } ;
    ///决定了union是哪种数据类型 (2.2.32版本以前所用字段，仅为了保持兼容，不建议使用该字段)
    XTP_MARKETDATA_TYPE data_type;
    ///决定了union是哪种数据类型（2.2.32版本新增字段，更详细区分了行情快照数据类型）
    XTP_MARKETDATA_TYPE_V2 data_type_v2;
} XTPMD;

///股票、基金等额外数据
struct XTPMarketDataStockExData {
    ///委托买入总量(SH,SZ)
    int64_t total_bid_qty;
    ///委托卖出总量(SH,SZ)
    int64_t total_ask_qty;
    ///加权平均委买价格(SH,SZ)
    double ma_bid_price;
    ///加权平均委卖价格(SH,SZ)
    double ma_ask_price;
    ///债券加权平均委买价格(SH)
    double ma_bond_bid_price;
    ///债券加权平均委卖价格(SH)
    double ma_bond_ask_price;
    ///债券到期收益率(SH)
    double yield_to_maturity;
    ///基金实时参考净值(SH,SZ)
    double iopv;
    ///ETF申购笔数(SH)
    int32_t etf_buy_count;
    ///ETF赎回笔数(SH)
    int32_t etf_sell_count;
    ///ETF申购数量(SH)
    double etf_buy_qty;
    ///ETF申购金额(SH)
    double etf_buy_money;
    ///ETF赎回数量(SH)
    double etf_sell_qty;
    ///ETF赎回金额(SH)
    double etf_sell_money;
    ///权证执行的总数量(SH)
    double total_warrant_exec_qty;
    ///权证跌停价格（元）(SH)
    double warrant_lower_price;
    ///权证涨停价格（元）(SH)
    double warrant_upper_price;
    ///买入撤单笔数(SH)
    int32_t cancel_buy_count;
    ///卖出撤单笔数(SH)
    int32_t cancel_sell_count;
    ///买入撤单数量(SH)
    double cancel_buy_qty;
    ///卖出撤单数量(SH)
    double cancel_sell_qty;
    ///买入撤单金额(SH)
    double cancel_buy_money;
    ///卖出撤单金额(SH)
    double cancel_sell_money;
    ///买入总笔数(SH)
    int64_t total_buy_count;
    ///卖出总笔数(SH)
    int64_t total_sell_count;
    ///买入委托成交最大等待时间(SH)
    int32_t duration_after_buy;
    ///卖出委托成交最大等待时间(SH)
    int32_t duration_after_sell;
    ///买方委托价位数(SH)
    int32_t num_bid_orders;
    ///卖方委托价位数(SH)
    int32_t num_ask_orders;

    ///基金T-1日净值(SZ)
    double pre_iopv;
    ///预留
    int64_t r1;
    ///预留
    int64_t r2;
};

///期权额外数据
struct XTPMarketDataOptionExData {
    ///波段性中断参考价(SH)
    double  auction_price;
    ///波段性中断集合竞价虚拟匹配量(SH)
    int64_t auction_qty;
    ///最近询价时间(SH)
    int64_t last_enquiry_time;
};

///债券额外数据
struct XTPMarketDataBondExData {
    ///委托买入总量(SH,SZ)
    int64_t total_bid_qty;
    ///委托卖出总量(SH,SZ)
    int64_t total_ask_qty;
    ///加权平均委买价格(SZ)
    double ma_bid_price;
    ///加权平均委卖价格(SZ)
    double ma_ask_price;
    ///债券加权平均委买价格(SH)
    double ma_bond_bid_price;
    ///债券加权平均委卖价格(SH)
    double ma_bond_ask_price;
    ///债券到期收益率(SH)
    double yield_to_maturity;
	///匹配成交最近价(SZ)
	double match_lastpx;
    ///债券加权平均价格(SH)
    double ma_bond_price;
    ///匹配成交成交量(SZ)
    int64_t match_qty;
    ///匹配成交成交金额(SZ)
    double match_turnover;
    ///预留
    double r4;
    ///预留
    double r5;
    ///预留
    double r6;
    ///预留
    double r7;
    ///预留
    double r8;
    ///买入撤单笔数(SH)
    int32_t cancel_buy_count;
    ///卖出撤单笔数(SH)
    int32_t cancel_sell_count;
    ///买入撤单数量(SH)
    double cancel_buy_qty;
    ///卖出撤单数量(SH)
    double cancel_sell_qty;
    ///买入撤单金额(SH)
    double cancel_buy_money;
    ///卖出撤单金额(SH)
    double cancel_sell_money;
    ///买入总笔数(SH)
    int64_t total_buy_count;
    ///卖出总笔数(SH)
    int64_t total_sell_count;
    ///买入委托成交最大等待时间(SH)
    int32_t duration_after_buy;
    ///卖出委托成交最大等待时间(SH)
    int32_t duration_after_sell;
    ///买方委托价位数(SH)
    int32_t num_bid_orders;
    ///卖方委托价位数(SH)
    int32_t num_ask_orders;
    ///时段(SHL2)，L1快照数据没有此字段，具体字段说明参阅《上海新债券Level2行情说明.doc》文档
    char instrument_status[8];
};

///XTP_MARKETDATA_TYPE是行情快照数据类型，2.2.32以前版本所用
enum XTP_MARKETDATA_TYPE {
    XTP_MARKETDATA_ACTUAL = 0, // 现货(股票/基金/债券等)
    XTP_MARKETDATA_OPTION = 1, // 期权
};

///XTP_MARKETDATA_TYPE_V2是行情快照数据类型，2.2.32版本新增字段
enum XTP_MARKETDATA_TYPE_V2 {
    XTP_MARKETDATA_V2_INDEX  = 0, // 指数
    XTP_MARKETDATA_V2_OPTION = 1, // 期权
    XTP_MARKETDATA_V2_ACTUAL = 2, // 现货(股票/基金等)
    XTP_MARKETDATA_V2_BOND   = 3, // 债券
};
```

 3.返回

无

 4.触发函数
```cpp
///请求回补指定行情，包括快照和逐笔
virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;
```


### 33. OnQueryAllNQTickersFullInfo


查询新三板合约完整静态信息的应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

 1.函数原型
```cpp
virtual void OnQueryAllNQTickersFullInfo(XTPNQFI* ticker_info, XTPRI *error_info, bool is_last) {};
```
 2.参数

ticker_info：新三板合约完整静态信息

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询合约完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

```cpp
///新三板全量静态信息
typedef struct XTPQuoteNQFullInfo {
    XTP_EXCHANGE_TYPE  exchange_id;					    ///<交易所代码
	char ticker[XTP_TICKER_LEN];				        ///<证券代码
	char ticker_name[XTP_TICKER_NAME_LEN];	            ///<证券名称
    XTP_SECURITY_TYPE      security_type;			    ///<合约详细类型
    XTP_QUALIFICATION_TYPE ticker_qualification_class;  ///<合约适当性类别
    char ticker_abbr_en[XTP_TICKER_NAME_LEN];           ///<英文简称
    char base_ticker[XTP_TICKER_LEN];                   ///<基础证券
    char industry_type[6];                              ///<行业种类
    char currency_type[3];                              ///<货币种类
    int32_t trade_unit;                                 ///<交易单位
    int32_t hang_out_date;                              ///<挂牌日期
    int32_t value_date;                                 ///<起息日期
    int32_t maturity_date;                              ///<到期日
    int32_t per_limit_vol;                              ///<每笔限量
    int32_t buy_vol_unit;                               ///<买数量单位
    int32_t sell_vol_unit;                              ///<卖数量单位
    int32_t mini_declared_vol;                          ///<最小申报数量
    int32_t limit_price_attr;                           ///<限价参数性质
    int32_t market_maker_quantity;                      ///<做市商数量
    double price_gear;                                  ///<价格档位
    double first_limit_trans;                           ///<首笔交易限价参数
    double subsequent_limit_trans;                      ///<后续交易限价参数
    double limit_upper_price;                           ///<涨停价格
    double limit_lower_price;                           ///<跌停价格
    double block_trade_upper;                           ///<大宗交易价格上限(预留，默认0)
    double block_trade_lower;                           ///<大宗交易价格下限(预留，默认0)
    double convert_into_ration;                         ///<折合比例
    XTP_TRADE_STATUS        trade_status : 8;           ///<交易状态
    XTP_SECURITY_LEVEL      security_level : 8;         ///<证券级别
    XTP_TRADE_TYPE          trade_type : 8;             ///<交易类型
    XTP_SUSPEND_FLAG        suspend_flag : 8;           ///<停牌标志
    XTP_EX_DIVIDEND_FLAG    ex_dividend_flag : 8;       ///<除权除息标志
    XTP_SECURITY_LAYER_TYPE layer_type : 8;             ///<分层信息
    int32_t reserved1 : 16;                             ///<保留字段
    char trade_places[3];                               ///<交易场所 预留
    char is_rzbd;                                       ///<是否融资标的 Y是 N否
    char is_rqbd;                                       ///<是否融券标的 Y是 N否
    char is_drrz;                                       ///<是否当日可融资 Y是 N否
    char is_drrq;                                       ///<是否当日可融券 Y是 N否
    char reserved;                                      ///<保留字段
    uint64_t unknown[3];                                ///<保留字段
}XTPNQFI;

///XTP_SECURITY_TYPE是一个证券详细分类枚举类型
typedef enum XTP_SECURITY_TYPE {
	/// 主板股票
	XTP_SECURITY_MAIN_BOARD = 0,
	/// 中小板股票
	XTP_SECURITY_SECOND_BOARD,
	/// 创业板股票
	XTP_SECURITY_STARTUP_BOARD,
	/// 指数
	XTP_SECURITY_INDEX,
	/// 科创板股票(上海)
	XTP_SECURITY_TECH_BOARD = 4,
	/// 国债
	XTP_SECURITY_STATE_BOND = 5,
	/// 企业债
	XTP_SECURITY_ENTERPRICE_BOND = 6,
	/// 公司债
	XTP_SECURITY_COMPANEY_BOND = 7,
	/// 转换债券
	XTP_SECURITY_CONVERTABLE_BOND = 8,
	/// 国债逆回购
	XTP_SECURITY_NATIONAL_BOND_REVERSE_REPO = 12,
	/// 本市场股票 ETF
	XTP_SECURITY_ETF_SINGLE_MARKET_STOCK = 14,
	/// 跨市场股票 ETF
	XTP_SECURITY_ETF_INTER_MARKET_STOCK,
	/// 跨境股票 ETF
	XTP_SECURITY_ETF_CROSS_BORDER_STOCK = 16,
	/// 本市场实物债券 ETF
	XTP_SECURITY_ETF_SINGLE_MARKET_BOND = 17,
    /// 现金债券ETF
    XTP_SECURITY_TYPE_ETF_CASH_BOND = 18,
	/// 黄金 ETF
	XTP_SECURITY_ETF_GOLD = 19,
	/// 分级基金子基金
	XTP_SECURITY_STRUCTURED_FUND_CHILD = 24,
	/// 深交所仅申赎基金
	XTP_SECURITY_SZSE_RECREATION_FUND = 26,
	/// 个股期权
	XTP_SECURITY_STOCK_OPTION = 29,
	/// ETF期权
	XTP_SECURITY_ETF_OPTION = 30,
	/// 配股
	XTP_SECURITY_ALLOTMENT = 100,

	/// 上交所申赎型货币基金
	XTP_SECURITY_MONETARY_FUND_SHCR = 110,
	/// 上交所交易型货币基金
	XTP_SECURITY_MONETARY_FUND_SHTR = 111,
	/// 深交所货币基金
	XTP_SECURITY_MONETARY_FUND_SZ = 112,

	/// 其他
	XTP_SECURITY_OTHERS = 255
}XTP_SECURITY_TYPE;

///XTP_QUALIFICATION_TYPE是一个证券适当性枚举类型
typedef enum  XTP_QUALIFICATION_TYPE
{
	XTP_QUALIFICATION_PUBLIC = 0,			///<公众投资者，合格投资者与机构投资者均可
	XTP_QUALIFICATION_COMMON = 1,			///<仅合格投资者与公众投资者
	XTP_QUALIFICATION_ORGANIZATION = 2,		///<仅限机构投资者
	XTP_QUALIFICATION_UNKNOWN = 3		///<未知，期权等可能为此种类型
}XTP_QUALIFICATION_TYPE;

///XTP_SECURITY_STATUS是一个证券状态枚举类型
typedef enum  XTP_SECURITY_STATUS
{
	XTP_SECURITY_STATUS_ST = 0,         ///< 风险警示板
	XTP_SECURITY_STATUS_N_IPO,          ///< 首日上市
	XTP_SECURITY_STATUS_COMMON,         ///< 普通
	XTP_SECURITY_STATUS_RESUME,         ///< 恢复上市
	XTP_SECURITY_STATUS_DELISTING = 10, ///< 退市整理期
	XTP_SECURITY_STATUS_OTHERS = 255    ///< 其他
}XTP_SECURITY_STATUS;

///XTP_TRADE_STATUS是一个交易状态枚举类型
typedef enum XTP_TRADE_STATUS
{
	XTP_TRADE_STATUS_UNKNOW = 0, 		///< 未知状态
	XTP_TRADE_STATUS_N,					///< 正常状态
	XTP_TRADE_STATUS_Y,					///< 首日挂牌
	XTP_TRADE_STATUS_D,					///< 新增股票挂牌交易
	XTP_TRADE_STATUS_I,					///< 询价
	XTP_TRADE_STATUS_F,					///< 申购
}XTP_TRADE_STATUS;

///XTP_SECURITY_LEVEL是一个证券级别枚举类型
typedef enum XTP_SECURITY_LEVEL
{
	XTP_SECURITY_LEVEL_UNKNOW = 0, 		///< 未知类型
	XTP_SECURITY_LEVEL_T,				///< 挂牌公司股票
	XTP_SECURITY_LEVEL_B,				///< 两网公司及退市股票
	XTP_SECURITY_LEVEL_O,				///< 仅提供行权功能的期权
	XTP_SECURITY_LEVEL_P,				///< 持有人数存在200人限制的证券
	XTP_SECURITY_LEVEL_R,				///< 其他类型的业务
	XTP_SECURITY_LEVEL_F,				///< 发行业务
}XTP_SECURITY_LEVEL;

///XTP_TRADE_TYPE是一个交易类型枚举类型
typedef enum XTP_TRADE_TYPE
{
	XTP_TRADE_TYPE_UNKNOW = 0,			///< 未知类型
	XTP_TRADE_TYPE_T,					///< 协议交易方式
	XTP_TRADE_TYPE_M,					///< 做市交易方式
	XTP_TRADE_TYPE_B,					///< 集合竞价+连续交易方式
	XTP_TRADE_TYPE_C,					///< 集合竞价交易方式
	XTP_TRADE_TYPE_P,					///< 发行方式
	XTP_TRADE_TYPE_O,					///< 其他类型
}XTP_TRADE_TYPE;

///XTP_SUSPEND_FLAG是一个停牌标志枚举类型
typedef enum XTP_SUSPEND_FLAG
{
	XTP_SUSPEND_FLAG_UNKNOW = 0,		///< 未知状态
	XTP_SUSPEND_FLAG_F,					///< 正常交易
	XTP_SUSPEND_FLAG_T,					///< 停牌，不接受申报
	XTP_SUSPEND_FLAG_H,					///< 停牌，接受申报
}XTP_SUSPEND_FLAG;

///XTP_EX_DIVIDEND_FLAG是一个除权除息标志枚举类型

typedef enum XTP_EX_DIVIDEND_FLAG
{
	XTP_EX_DIVIDEND_FLAG_UNKNOW = 0,	///< 未知状态
	XTP_EX_DIVIDEND_FLAG_N,				///< 正常状态
	XTP_EX_DIVIDEND_FLAG_E,				///< 除权
	XTP_EX_DIVIDEND_FLAG_D,				///< 除息
	XTP_EX_DIVIDEND_FLAG_A,				///< 除权除息
}XTP_EX_DIVIDEND_FLAG;

/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
/// 存放证券名称的字符串长度
#define XTP_TICKER_NAME_LEN 64
```

 3.返回

无

 4.触发函数
```cpp
// 获取所有新三板合约的详细静态信息，包括指数等非可交易的
virtual int QueryAllNQTickersFullInfo() = 0;
```


### 34. OnTickByTickLossRange


逐笔丢包应答。

此函数只有在逐笔发生丢包时才会有调用，如果丢包的上下限一致，表示仅丢失了一个包，注意此包仅为数据包，包含1个或者多个逐笔数据。

1.函数原型
```cpp
virtual void OnTickByTickLossRange(int begin_seq, int end_seq) {};
```

2.参数
begin_seq: 当逐笔出现丢包时，丢包区间下限（可能与上限一致）

end_seq: 当逐笔出现丢包时，丢包区间上限（可能与下限一致）

3.返回

无


### 35. OnETFIOPVData


ETF的IOPV通知，订阅ETF后调用。

1.函数原型
```cpp
virtual void OnETFIOPVData(IOPV *iopv) {};
```

2.参数

iopv: ETF的参考单位基金净值数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
```cpp
//IOPV数据结构
struct IOPV {
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    char    ticker[XTP_TICKER_LEN];
    /// 时间
    int64_t data_time;
    /// iopv值
    double iopv;
};
```

3.返回

无

4.订阅函数
```cpp
// 订阅行情快照，包括股票、指数和期权
virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
// 订阅全市场的股票行情快照
virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
