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
id: zhongtai-xtp-2056206185257816066
title: QuoteApi
doc_id: 2056206185257816066
doc_category: 详细接口使用说明
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2056206185257816066'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-05-18
---

# QuoteApi

## QuoteApi


目录


- [1. 接口](#1-接口)
- [2. 示例代码](#2-示例代码)
- [3. CreateQuoteApi](#3-createquoteapi)
- [4. Release](#4-release)
- [5. GetTradingDay](#5-gettradingday)
- [6. GetApiVersion](#6-getapiversion)
- [7. GetApiLastError](#7-getapilasterror)
- [8. SetUDPBufferSize](#8-setudpbuffersize)
- [9. RegisterSpi](#9-registerspi)
- [10. SetHeartBeatInterval](#10-setheartbeatinterval)
- [11. SetUDPRecvThreadAffinity](#11-setudprecvthreadaffinity)
- [12. SetUDPRecvThreadAffinityArray](#12-setudprecvthreadaffinityarray)
- [13. SetUDPParseThreadAffinity](#13-setudpparsethreadaffinity)
- [14. SetUDPParseThreadAffinityArray](#14-setudpparsethreadaffinityarray)
- [15. SetUDPSeqLogOutPutFlag](#15-setudpseqlogoutputflag)
- [16. SubscribeMarketData](#16-subscribemarketdata)
- [17. UnSubscribeMarketData](#17-unsubscribemarketdata)
- [18. SubscribeOrderBook](#18-subscribeorderbook)
- [19. UnSubscribeOrderBook](#19-unsubscribeorderbook)
- [20. SubscribeTickByTick](#20-subscribetickbytick)
- [21. UnSubscribeTickByTick](#21-unsubscribetickbytick)
- [22. SubscribeAllMarketData](#22-subscribeallmarketdata)
- [23. UnSubscribeAllMarketData](#23-unsubscribeallmarketdata)
- [24. SubscribeAllOrderBook](#24-subscribeallorderbook)
- [25. UnSubscribeAllOrderBook](#25-unsubscribeallorderbook)
- [26. SubscribeAllTickByTick](#26-subscribealltickbytick)
- [27. UnSubscribeAllTickByTick](#27-unsubscribealltickbytick)
- [28. Login](#28-login)
- [29. Logout](#29-logout)
- [30. QueryAllTickers](#30-queryalltickers)
- [31. QueryTickersPriceInfo](#31-querytickerspriceinfo)
- [32. QueryAllTickersPriceInfo](#32-queryalltickerspriceinfo)
- [33. SubscribeAllOptionMarketData](#33-subscribealloptionmarketdata)
- [34. UnSubscribeAllOptionMarketData](#34-unsubscribealloptionmarketdata)
- [35. SubscribeAllOptionOrderBook](#35-subscribealloptionorderbook)
- [36. UnSubscribeAllOptionOrderBook](#36-unsubscribealloptionorderbook)
- [37. SubscribeAllOptionTickByTick](#37-subscribealloptiontickbytick)
- [38. UnSubscribeAllOptionTickByTick](#38-unsubscribealloptiontickbytick)
- [39. QueryAllTickersFullInfo](#39-queryalltickersfullinfo)
- [40. LoginToRebuildQuoteServer](#40-logintorebuildquoteserver)
- [41. LogoutFromRebuildQuoteServer](#41-logoutfromrebuildquoteserver)
- [42. RequestRebuildQuote](#42-requestrebuildquote)
- [43. QueryAllNQTickersFullInfo](#43-queryallnqtickersfullinfo)


QuoteApi类提供了行情api的初始化、登录、订阅等功能。

### 1. 接口


```cpp
namespace XTP {
	namespace API {
		class MD_API_EXPORT QuoteApi
		{
		public:
			///创建QuoteApi
			///@param client_id （必须输入）用于区分同一用户的不同客户端，由用户自定义
			///@param save_file_path （必须输入）存贮订阅信息文件的目录，请设定一个有可写权限的真实存在的路径，如果路径不存在的话，可能会因为写冲突而造成断线
			///@param log_level 日志输出级别
			///@return 创建出的UserApi
			///@remark 如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，但是对于同一账户，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接
			static QuoteApi *CreateQuoteApi(uint8_t client_id, const char *save_file_path, XTP_LOG_LEVEL log_level=XTP_LOG_LEVEL_DEBUG);

			///删除接口对象本身
			///@remark 不再使用本接口对象时,调用该函数删除接口对象
			virtual void Release() = 0;


			///获取当前交易日
			///@return 获取到的交易日
			///@remark 只有登录成功后,才能得到正确的交易日
			virtual const char *GetTradingDay() = 0;

			///获取API的发行版本号
			///@return 返回api发行版本号
			virtual const char* GetApiVersion() = 0;

			///获取API的系统错误
			///@return 返回的错误信息，可以在Login、Logout、订阅、取消订阅失败时调用，获取失败的原因
			///@remark 可以在调用api接口失败时调用，例如login失败时
			virtual XTPRI *GetApiLastError() = 0;

			///设置采用UDP方式连接时的单个队列接收缓冲区大小，目前可能最大使用4个缓冲区队列
			///@remark 需要在Login之前调用，默认大小和最小设置均为64MB。此缓存大小单位为MB，请输入2的次方数，例如128MB请输入128。
			virtual void SetUDPBufferSize(uint32_t buff_size) = 0;


			///注册回调接口
			///@param spi 派生自回调接口类的实例，请在登录之前设定
			virtual void RegisterSpi(QuoteSpi *spi) = 0;

			///设置心跳检测时间间隔，单位为秒
			///@param interval 心跳检测时间间隔，单位为秒
			///@remark 此函数必须在Login之前调用
			virtual void SetHeartBeatInterval(uint32_t interval) = 0;

			///使用UDP接收行情时，设置接收行情线程绑定的cpu，此版本不建议使用，只为跟之前的版本兼容，请替换使用SetUDPRecvThreadAffinityArray函数
			///@param cpu_no 设置绑定的cpu，例如绑定cpu 0，可以设置0，绑定cpu 2，可以设置2，建议绑定后面的cpu
			///@remark 此版本不建议使用,请替换使用SetUDPRecvThreadAffinityArray函数，如果调用则必须在Login之前调用，否则不会生效，与SetUDPRecvThreadAffinityArray一起使用时，仅第一个被调用的生效
			virtual void SetUDPRecvThreadAffinity(int32_t cpu_no) = 0;

			///使用UDP接收行情时，设置接收行情线程绑定的cpu集合
			///@param cpu_no_array 设置绑定的cpu集合数组
			///@param count cpu集合数组长度
			///@remark 此函数可不调用，如果调用则必须在Login之前调用，否则不会生效。绑核时，将从数组前面的核开始使用
			virtual void SetUDPRecvThreadAffinityArray(int32_t cpu_no_array[], int32_t count) = 0;

			///使用UDP接收行情时，设置解析行情线程绑定的cpu，此版本不建议使用，只为跟之前的版本兼容，请替换使用SetUDPParseThreadAffinityArray函数
			///@param cpu_no 设置绑定的cpu，例如绑定cpu 0，可以设置0，绑定cpu 2，可以设置2，建议绑定后面的cpu
			///@remark 此版本不建议使用，请替换使用SetUDPParseThreadAffinityArray函数，如果调用则必须在Login之前调用，否则不会生效，与SetUDPParseThreadAffinityArray一起使用时，仅第一个被调用的生效
			virtual void SetUDPParseThreadAffinity(int32_t cpu_no) = 0;

			///使用UDP接收行情时，设置解析行情线程绑定的cpu集合
			///@param cpu_no_array 设置绑定的cpu集合数组
			///@param count cpu集合数组长度
			///@remark 此函数可不调用，如果调用则必须在Login之前调用，否则不会生效。绑核时，将从数组前面的核开始使用
			virtual void SetUDPParseThreadAffinityArray(int32_t cpu_no_array[], int32_t count) = 0;

			///设定UDP收行情时是否输出异步日志
			///@param flag 是否输出标识，默认为true，如果不想输出"udpseq"开头的异步日志，请设置此参数为false
			///@remark 此函数可不调用，如果调用则必须在Login之前调用，否则不会生效
			virtual void SetUDPSeqLogOutPutFlag(bool flag = true) = 0;

			///订阅行情，包括股票、指数和期权。
			///@return 订阅接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
			///@param count 要订阅/退订行情的合约个数
			///@param exchange_id 交易所代码
			///@remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情
			virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

			///退订行情，包括股票、指数和期权。
			///@return 取消订阅接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
			///@param count 要订阅/退订行情的合约个数
			///@param exchange_id 交易所代码
			///@remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅行情接口配套使用
			virtual int UnSubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

			///订阅行情订单簿。
			///@return 订阅行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
			///@param count 要订阅/退订行情订单簿的合约个数
			///@param exchange_id 交易所代码
			///@remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情(仅支持深交所)
			virtual int SubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

			///退订行情订单簿。
			///@return 取消订阅行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
			///@param count 要订阅/退订行情订单簿的合约个数
			///@param exchange_id 交易所代码
			///@remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅行情订单簿接口配套使用
			virtual int UnSubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

			///订阅逐笔行情。
			///@return 订阅逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
			///@param count 要订阅/退订行情订单簿的合约个数
			///@param exchange_id 交易所代码
			///@remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情
			virtual int SubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

			///退订逐笔行情。
			///@return 取消订阅逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
			///@param count 要订阅/退订行情订单簿的合约个数
			///@param exchange_id 交易所代码
			///@remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅逐笔行情接口配套使用
			virtual int UnSubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

			///订阅全市场的股票行情
			///@return 订阅全市场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@remark 需要与全市场退订行情接口配套使用
			virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///退订全市场的股票行情
			///@return 退订全市场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@remark 需要与订阅全市场行情接口配套使用
			virtual int UnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///订阅全市场的股票行情订单簿
			///@return 订阅全市场行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@remark 需要与全市场退订行情订单簿接口配套使用
			virtual int SubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///退订全市场的股票行情订单簿
			///@return 退订全市场行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@remark 需要与订阅全市场行情订单簿接口配套使用
			virtual int UnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///订阅全市场的股票逐笔行情
			///@return 订阅全市场逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@remark 需要与全市场退订逐笔行情接口配套使用
			virtual int SubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///退订全市场的股票逐笔行情
			///@return 退订全市场逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
			///@remark 需要与订阅全市场逐笔行情接口配套使用
			virtual int UnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///用户登录请求
			///@return 登录是否成功，"0"表示登录成功，"-1"表示连接服务器出错，此时用户可以调用GetApiLastError()来获取错误代码，"-2"表示已存在连接，不允许重复登录，如果需要重连，请先logout，"-3"表示输入有错误
			///@param ip 服务器ip地址，类似"127.0.0.1"
			///@param port 服务器端口号
			///@param user 登录用户名
			///@param password 登录密码
			///@param sock_type "1"代表TCP，"2"代表UDP
			///@param local_ip 本地网卡地址，类似"127.0.0.1"
			///@remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只能有一个连接
			virtual int Login(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;


			///登出请求
			///@return 登出是否成功，"0"表示登出成功，非"0"表示登出出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@remark 此函数为同步阻塞式，不需要异步等待登出，当函数返回即可进行后续操作
			virtual int Logout() = 0;

			///获取当前交易日合约部分静态信息
			///@return 发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功
			///@param exchange_id 交易所代码，必须提供 1-上海 2-深圳
			virtual int QueryAllTickers(XTP_EXCHANGE_TYPE exchange_id) = 0;

			///获取合约的最新价格信息
			///@return 发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功
			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
			///@param count 要查询的合约个数
			///@param exchange_id 交易所代码
			virtual int QueryTickersPriceInfo(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

			///获取所有合约的最新价格信息
			///@return 发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功
			virtual int QueryAllTickersPriceInfo() = 0;

			///订阅全市场的期权行情
			///@return 订阅全市期权场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前新三板没有期权）
			///@remark 需要与全市场退订期权行情接口配套使用
			virtual int SubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///退订全市场的期权行情
			///@return 退订全市场期权行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前新三板没有期权）
			///@remark 需要与订阅全市场期权行情接口配套使用
			virtual int UnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///订阅全市场的期权行情订单簿（目前期权没有订单簿数据）
			///@return 订阅全市场期权行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前新三板没有期权）
			///@remark 需要与全市场退订期权行情订单簿接口配套使用
			virtual int SubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///退订全市场的期权行情订单簿（目前期权没有订单簿数据）
			///@return 退订全市场期权行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前新三板没有期权）
			///@remark 需要与订阅全市场期权行情订单簿接口配套使用
			virtual int UnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///订阅全市场的期权逐笔行情（目前期权没有逐笔行情数据）
			///@return 订阅全市场期权逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前新三板没有期权）
			///@remark 需要与全市场退订期权逐笔行情接口配套使用
			virtual int SubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///退订全市场的期权逐笔行情（目前期权没有逐笔行情数据）
			///@return 退订全市场期权逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错
			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前新三板没有期权）
			///@remark 需要与订阅全市场期权逐笔行情接口配套使用
			virtual int UnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

			///获取沪深两市所有合约的详细静态信息，包括指数等非可交易的
			///@return 发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功
			///@param exchange_id 交易所代码，必须提供 1-上海 2-深圳，不支持新三板
			virtual int QueryAllTickersFullInfo(XTP_EXCHANGE_TYPE exchange_id) = 0;

			///获取新三板所有合约的详细静态信息，包括指数等非可交易的
			///@return 发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功
			virtual int QueryAllNQTickersFullInfo() = 0;

			///用户登录回补服务器请求
			///@return 登录是否成功，“0”表示登录成功，“-1”表示连接服务器出错，此时用户可以调用GetApiLastError()来获取错误代码，“-2”表示已存在连接，不允许重复登录，如果需要重连，请先logout，“-3”表示输入有错误
			///@param ip 服务器ip地址，类似“127.0.0.1”
			///@param port 服务器端口号
			///@param user 登陆用户名
			///@param password 登陆密码
			///@param sock_type “1”代表TCP，“2”代表UDP
			///@param local_ip 本地网卡地址，类似“127.0.0.1”
			///@remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只能有一个连接。回补服务器会在无消息交互后定时断线，请注意仅在需要回补数据时才保持连接，回补完成后请及时logout
			virtual int LoginToRebuildQuoteServer(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;

			///登出回补服务器请求
			///@return 登出是否成功，“0”表示登出成功，非“0”表示登出出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@remark 此函数为同步阻塞式，不需要异步等待登出，当函数返回即可进行后续操作
			virtual int LogoutFromRebuildQuoteServer() = 0;

			///请求回补指定行情，包括快照和逐笔
			///@return 请求回补指定频道的逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
			///@param rebuild_param 指定回补的参数信息，注意一次性回补最多1000个数据，超过1000需要分批次请求，一次只能指定一种类型的数据
			///@remark 仅在逐笔行情丢包时或者确实快照行情时使用，回补的行情数据将从OnRebuildTickByTick或者OnRebuildMarketData()接口回调提供，与订阅的行情数据不在同一个线程内
			virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;

		protected:
			~QuoteApi() {};
		};
	}
}
```


### 2. 示例代码


以下是MyQuoteApi.h文件
```cpp
#include "xtp_quote_api.h"
#include "MyQuoteSpi.h"

using namespace XTP::API;

class MyQuoteApi
{
public:
	explicit MyQuoteApi();
	~MyQuoteApi();

	// 初始化
    bool initialize();

private:
    XTP::API::QuoteApi* user_quote_api_;
	MyQuoteSpi* m_quote_spi;
};
```
以下是MyQuoteApi.cpp文件
```cpp
#include "MyQuoteApi.h"

MyQuoteApi::MyQuoteApi()
{
	user_quote_api_ = NULL;
	m_quote_spi = NULL;
}

MyQuoteApi::~MyQuoteApi()
{

}

bool MyQuoteApi::initialize()
{
	// 创建并初始化行情API
	user_quote_api_ = XTP::API::QuoteApi::CreateQuoteApi(1, "./", XTP_LOG_LEVEL_DEBUG);
	if (user_quote_api_)
	{
		// 注册行情回调接口
		m_quote_spi = new MyQuoteSpi();
		user_quote_api_->RegisterSpi(m_quote_spi);
		// 登录前参数设置
		user_quote_api_->SetHeartBeatInterval(15);

		return true;
	}
	return false;
}
```


### 3. CreateQuoteApi


创建QuoteApi实例。

如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，但是对于同一账户，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接。

2.2.33.5以上版本支持一个进程中创建多个QuoteApi实例，但是每个实例的创建参数必须一致。

 1.函数原型
```cpp
static QuoteApi *CreateQuoteApi(uint8_t client_id, const char *save_file_path, XTP_LOG_LEVEL log_level=XTP_LOG_LEVEL_DEBUG);
```
 2.参数

client_id：（必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义，普通用户必须使用1-99之间的数值

save_file_path：（必须输入）存储行情api日志文件的目录，请设定一个真实存在的有可写权限的路径，如果路径不存在的话，可能会因为写冲突而造成断线

log_level：日志输出级别

 3.返回

创建出的UserApi

 4.调用示例
```cpp
#include
#include

typedef unsigned char uint8_t;
using namespace std;

// 初始化api，创建单例
uint8_t client_id_ = 1;
string stdstr_log_path("./");
// 开发调试时用XTP_LOG_LEVEL_DEBUG，稳定运行时用XTP_LOG_LEVEL_INFO
XTP_LOG_LEVEL log_level = XTP_LOG_LEVEL_DEBUG;

XTP::API::QuoteApi* user_quote_api_ = XTP::API::QuoteApi::CreateQuoteApi(client_id_, stdstr_log_path.c_str(), log_level);

if (user_quote_api_)
{
	// 注册行情回调接口
    MyQuoteSpi *spi = new MyQuoteSpi();
    user_quote_api_->RegisterSpi(spi);
}
```


### 4. Release


删除接口对象本身。程序退出前，不再使用本接口对象时,可调用该函数删除接口对象。

 1.函数原型
```cpp
virtual void Release() = 0;
```
 2.参数

无

 3.返回

无

 4.调用示例
```cpp
// 注销当前会话并删除接口对象
if (user_quote_api_ != NULL)
{
	user_quote_api_->Logout();
	user_quote_api_->Release();
}
```


### 5. GetTradingDay


获取当前交易日。只有登录成功后,才能得到正确的交易日。

 1.函数原型
```cpp
virtual const char *GetTradingDay() = 0;
```
 2.参数

无

 3.返回

返回一个指向日期信息字符串的常量指针。

 4.调用示例
```cpp
// 获取当前交易日
if (user_quote_api_)
{
    std::cout GetTradingDay() GetApiVersion() GetApiLastError();
	std::cout error_id error_msg SetUDPBufferSize(256);
}
```


### 9. RegisterSpi


注册回调接口。

 1.函数原型
```cpp
virtual void RegisterSpi(QuoteSpi *spi) = 0;
```
 2.参数

spi：派生自回调接口类的实例，请在登录之前设定

 3.返回

无

 4.调用示例
```cpp
// 注册行情回调接口
if (user_quote_api_)
{
	MyQuoteSpi *spi = new MyQuoteSpi();
	user_quote_api_->RegisterSpi(spi);
}
```


### 10. SetHeartBeatInterval


设置心跳检测时间间隔，单位为秒。此函数必须在Login之前调用。

 1.函数原型
```cpp
virtual void SetHeartBeatInterval(uint32_t interval) = 0;
```
 2.参数

interval：心跳检测时间间隔，单位为秒

 3.返回

无

 4.调用示例
```cpp
// 设定交易服务器超时时间为15秒，用户可自定义
if (user_quote_api_)
{
	user_quote_api_->SetHeartBeatInterval(15);
}
```


### 11. SetUDPRecvThreadAffinity


使用UDP接收行情时，设置接收行情线程绑定的cpu。

2.2.30.7以上版本api请**不要使用**此函数，只为跟之前的版本兼容，请务必替换使用SetUDPRecvThreadAffinityArray函数。
如果调用则必须在Login之前调用，否则不会生效，与SetUDPRecvThreadAffinityArray一起使用时，仅第一个被调用的生效。

 1.函数原型
```cpp
virtual void SetUDPRecvThreadAffinity(int32_t cpu_no) = 0;
```
 2.参数

cpu_no：设置绑定的cpu，例如绑定cpu 1，可以设置1，绑定cpu 2，可以设置2，建议绑定后面的cpu，不要绑定cpu 0。

 3.返回

无

 4.调用示例
```cpp
// 设置接收行情线程绑定核2
if (user_quote_api_)
{
	user_quote_api_->SetUDPRecvThreadAffinity(2);
}
```


### 12. SetUDPRecvThreadAffinityArray


使用UDP接收行情时，设置接收行情线程绑定的cpu集合。

此函数可不调用，如果调用则必须在Login之前调用，否则不会生效。绑核时，将从数组前面的核开始使用。

 1.函数原型
```cpp
virtual void SetUDPRecvThreadAffinityArray(int32_t cpu_no_array[], int32_t count) = 0;
```
 2.参数

cpu_no_array：设置绑定的cpu集合数组

count：cpu集合数组长度

 3.返回

无

 4.调用示例
```cpp
// 设置接收行情线程绑定核1核2
if (user_quote_api_)
{
	int32_t array[] = {1, 2}；
	user_quote_api_->SetUDPRecvThreadAffinityArray(array, 2);
}
```


### 13. SetUDPParseThreadAffinity


使用UDP接收行情时，设置解析行情线程绑定的cpu。

2.2.30.7以上版本api请**不要使用**此函数，只为跟之前的版本兼容，请务必使用SetUDPParseThreadAffinityArray函数。

如果调用则必须在Login之前调用，否则不会生效，与SetUDPParseThreadAffinityArray一起使用时，仅第一个被调用的生效。

 1.函数原型
```cpp
virtual void SetUDPParseThreadAffinity(int32_t cpu_no) = 0;
```
 2.参数

cpu_no：设置绑定的cpu，例如绑定cpu 1，可以设置1，绑定cpu 2，可以设置2，建议绑定后面的cpu，不要绑定cpu 0。

 3.返回

无

 4.调用示例
```cpp
// 设置解析行情线程绑定核3
if (user_quote_api_)
{
	user_quote_api_->SetUDPParseThreadAffinity(3);
}
```


### 14. SetUDPParseThreadAffinityArray


使用UDP接收行情时，设置解析行情线程绑定的cpu集合。

此函数可不调用，如果调用则必须在Login之前调用，否则不会生效。绑核时，将从数组前面的核开始使用。

 1.函数原型
```cpp
virtual void SetUDPParseThreadAffinityArray(int32_t cpu_no_array[], int32_t count) = 0;
```
 2.参数

cpu_no_array：设置绑定的cpu集合数组

count：cpu集合数组长度

 3.返回

无

 4.调用示例
```cpp
// 设置解析行情线程绑定核3核4
if (user_quote_api_)
{
	int32_t array[] = {3, 4}；
	user_quote_api_->SetUDPParseThreadAffinityArray(array, 2);
}
```


### 15. SetUDPSeqLogOutPutFlag


设定UDP收行情时是否输出异步日志。

此函数可不调用，如果调用则必须在Login之前调用，否则不会生效。
建议在调试和实盘初期时开启，稳定运行后可以关闭。

 1.函数原型
```cpp
virtual void SetUDPSeqLogOutPutFlag(bool flag = true) = 0;
```
 2.参数

flag：是否输出标识，默认为true，如果不想输出"udpseq"开头的异步日志，请设置此参数为false

 3.返回

无

 4.调用示例
```cpp
// 设定UDP接收行情不输出异步日志
if (user_quote_api_)
{
	user_quote_api_->SetUDPSeqLogOutPutFlag(false);
}
```


### 16. SubscribeMarketData


订阅行情，包括股票、指数和期权。

可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情。

 1.函数原型
```cpp
virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
```
 2.参数

ticker：合约ID数组，注意合约代码必须以'\0'结尾，不包含空格

count：要订阅/退订行情的合约个数

exchange_id：交易所代码

 3.返回

订阅接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

 4.调用示例
```cpp
// 订阅沪市的600000和600001两支股票的行情
if (user_quote_api_)
{
	// 申请内存
	int ticker_count = 2;//需要订阅行情的证券代码数量，可根据实际订阅需求改动
	char **ppInstrumentID = new char*[ticker_count];
	for (int i = 0; i SubscribeMarketData(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);

	// 释放内存
	for (int i = 0; i UnSubscribeMarketData(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);

	// 释放内存
	for (int i = 0; i SubscribeOrderBook(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);

	// 释放内存
	for (int i = 0; i UnSubscribeOrderBook(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);

	// 释放内存
	for (int i = 0; i SubscribeTickByTick(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);

	// 释放内存
	for (int i = 0; i UnSubscribeTickByTick(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);

	//释放内存
	for (int i = 0; i SubscribeAllMarketData();
}
```
```cpp
// 订阅沪市股票行情
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllMarketData(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```

 6.通知函数
```cpp
virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count);
```


### 23. UnSubscribeAllMarketData


退订全市场的股票行情。

需要与全市场订阅行情接口配套使用。

 1.函数原型
```cpp
virtual int UnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

 3.返回

退订全市场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

 4.调用示例
```cpp
// 退订全市场股票行情
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllMarketData();
}
```
```cpp
// 退订沪市股票行情
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllMarketData(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnUnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```


### 24. SubscribeAllOrderBook


订阅全市场的股票行情订单簿。

需要与全市场退订行情订单簿接口配套使用。

 1.函数原型
```cpp
virtual int SubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持）

 3.返回

订阅全市场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

 4.调用示例
```cpp
// 订阅全市场股票行情订单簿
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllOrderBook();
}
```
```cpp
// 订阅沪市股票行情订单簿
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllOrderBook(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```

 6.通知函数
```cpp
virtual void OnOrderBook(XTPOB *order_book) {};
```


### 25. UnSubscribeAllOrderBook


退订全市场的股票行情订单簿。

需要与全市场订阅行情订单簿接口配套使用。

 1.函数原型
```cpp
virtual int UnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持）

 3.返回

退订全市场行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

 4.调用示例
```cpp
// 退订全市场股票行情订单簿
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllOrderBook();
}
```
```cpp
// 退订沪市股票行情订单簿
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllOrderBook(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnUnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```


### 26. SubscribeAllTickByTick


订阅全市场的股票逐笔行情。

需要与全市场退订逐笔行情接口配套使用。

 1.函数原型
```cpp
virtual int SubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持）

 3.返回

订阅全市场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

 4.调用示例
```cpp
// 订阅全市场股票逐笔行情
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllTickByTick();
}
```
```cpp
// 订阅沪市股票逐笔行情
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllTickByTick(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```

 6.通知函数
```cpp
virtual void OnTickByTick(XTPTBT *tbt_data);
```


### 27. UnSubscribeAllTickByTick


退订全市场的股票逐笔行情。

需要与全市场订阅逐笔行情接口配套使用。

 1.函数原型
```cpp
virtual int UnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持）

 3.返回

退订全市场逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

 4.调用示例
```cpp
// 退订全市场股票逐笔行情
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllTickByTick();
}
```
```cpp
// 退订沪市股票逐笔行情
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllTickByTick(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnUnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```


### 28. Login


用户登录请求。

此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只能有一个连接。

 1.函数原型
```cpp
virtual int Login(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;
```
 2.参数

Ip：服务器ip地址，类似"127.0.0.1"

port：服务器端口号

user：登录用户名

password：登录密码

sock_type："1"代表TCP，"2"代表UDP

local_ip：本地网卡地址，类似"127.0.0.1"

```cpp
// XTP_PROTOCOL_TYPE是通讯传输协议方式
typedef enum XTP_PROTOCOL_TYPE
{
	XTP_PROTOCOL_TCP = 1,	///SetHeartBeatInterval(15);

	std::string quote_server_ip = "xxx.xxx.xxx.xxx";
	int quote_server_port = xxxx;
	std::string quote_username = "xxxxxxxx";
	std::string quote_password = "xxxxxx";
	std::string local_ip = "xxx.xxx.xxx.xxx";//根据本地网卡对应的ip设定

	// 登录
	int ret = user_quote_api_->Login(quote_server_ip.c_str(), quote_server_port, quote_username.c_str(), quote_password.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str());
}
```
```cpp
// 行情采用UDP方式连接
if (user_quote_api_)
{
	// 登录前参数设置
	user_quote_api_->SetHeartBeatInterval(15);
	user_quote_api_->SetUDPBufferSize(256);
	// UDP设置中绑核函数和异步日志设置函数可不调用
	int32_t arr_recv[] = {1, 2}；
	user_quote_api_->SetUDPRecvThreadAffinityArray(arr_recv, 2);
	int32_t arr_parse[] = {3, 4}；
	user_quote_api_->SetUDPParseThreadAffinityArray(arr_parse, 2);
	user_quote_api_->SetUDPSeqLogOutPutFlag(false);

	// 登录
	std::string quote_server_ip = "xxx.xxx.xxx.xxx";
	int quote_server_port = xxxx;
	std::string quote_username = "xxxxxxxx";
	std::string quote_password = "xxxxxx";
	std::string local_ip = "xxx.xxx.xxx.xxx";//根据本地网卡对应的ip设定

	int ret = user_quote_api_->Login(quote_server_ip.c_str(), quote_server_port, quote_username.c_str(), quote_password.c_str(), XTP_PROTOCOL_UDP, local_ip.c_str());
}
```


### 29. Logout


登出请求。此函数为同步阻塞式，不需要异步等待登出，当函数返回即可进行后续操作。

 1.函数原型
```cpp
virtual int Logout() = 0;
```
 2.参数

无

 3.返回

登出是否成功，"0"表示登出成功，非"0"表示登出出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 登出请求
if (user_quote_api_) {
	int ret = user_quote_api_->Logout();
}
```


### 30. QueryAllTickers


获取沪深当前交易日合约部分静态信息。

 1.函数原型
```cpp
virtual int QueryAllTickers(XTP_EXCHANGE_TYPE exchange_id) = 0;
```
 2.参数

exchange_id：交易所代码，必须提供 1-上海 2-深圳，不支持新三板

 3.返回

发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功。

 4.调用示例
```cpp
// 获取当前交易日沪市所有合约静态信息
if (user_quote_api_) {
	int ret = user_quote_api_->QueryAllTickers(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnQueryAllTickers(XTPQSI* ticker_info, XTPRI *error_info, bool is_last) {};
```


### 31. QueryTickersPriceInfo


获取合约的最新价格信息。

 1.函数原型
```cpp
virtual int QueryTickersPriceInfo(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
```
 2.参数

ticker：合约ID数组，注意合约代码必须以'\0'结尾，不包含空格

count：要订阅/退订逐笔行情的合约个数

exchange_id：交易所代码

 3.返回

发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功。

 4.调用示例
```cpp
// 获取沪市的600000和600001两支股票的最新价格信息
if (user_quote_api_)
{
	// 申请内存
	int ticker_count = 2;//需要查询的证券代码数量，可根据实际需求改动
	char **ppInstrumentID = new char*[ticker_count];
	for (int i = 0; i QueryTickersPriceInfo(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);

	//释放内存
	for (int i = 0; i QueryAllTickersPriceInfo();
}
```

 5.响应函数
```cpp
virtual void OnQueryTickersPriceInfo(XTPTPI* ticker_info, XTPRI *error_info, bool is_last) {};
```


### 33. SubscribeAllOptionMarketData


订阅全市场的期权行情快照。

需要与全市场退订期权行情快照接口配套使用。

 1.函数原型
```cpp
virtual int SubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持新三板）

 3.返回

订阅全市场期权行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

 4.调用示例
```cpp
// 订阅全市场期权行情快照
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllOptionMarketData();
}
```
```cpp
// 订阅沪市期权行情快照
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllOptionMarketData(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```

 6.通知函数
```cpp
virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count);
```


### 34. UnSubscribeAllOptionMarketData


退订期权行情快照。

需要与订阅全市场期权行情接口配套使用。

 1.函数原型
```cpp
virtual int UnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持新三板）

 3.返回

取消订阅接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

 4.调用示例
```cpp
// 退订全市场期权行情
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllOptionMarketData();
}
```
```cpp
// 退订沪市期权行情
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllOptionMarketData(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnUnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```


### 35. SubscribeAllOptionOrderBook


全市场订阅期权行情订单簿。

需要与全市场退订期权行情订单簿接口配套使用。
目前期权没有OB数据。

 1.函数原型
```cpp
virtual int SubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持新三板）

 3.返回

订阅行情订单簿是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

 4.调用示例
```cpp
// 订阅全市场期权行情订单簿
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllOptionOrderBook();
}
```
```cpp
// 订阅沪市期权行情订单簿
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllOptionOrderBook(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```

 6.通知函数
```cpp
virtual void OnOrderBook(XTPOB *order_book) {};
```


### 36. UnSubscribeAllOptionOrderBook


退订全市场的期权行情订单簿。

需要与全市场订阅期权行情订单簿接口配套使用。
目前期权没有OB数据。

 1.函数原型
```cpp
virtual int UnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持新三板）

 3.返回

退订全市场行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

 4.调用示例
```cpp
// 退订全市场期权行情订单簿
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllOptionOrderBook();
}
```
```cpp
// 退订沪市期权行情订单簿
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllOptionOrderBook(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnUnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```


### 37. SubscribeAllOptionTickByTick


订阅全市场的期权逐笔行情。

需要与全市场退订期权逐笔行情接口配套使用。

目前期权没有逐笔TBT数据。

 1.函数原型
```cpp
virtual int SubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持新三板）

 3.返回

订阅全市场期权逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

 4.调用示例
```cpp
// 订阅全市场期权逐笔行情
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllOptionTickByTick();
}
```
```cpp
// 订阅沪市期权逐笔行情
if (user_quote_api_)
{
	int ret = user_quote_api_->SubscribeAllOptionTickByTick(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```

 6.通知函数
```cpp
virtual void OnTickByTick(XTPTBT *tbt_data);
```


### 38. UnSubscribeAllOptionTickByTick


退订全市场的期权逐笔行情。

需要与全市场期权订阅逐笔行情接口配套使用。
目前期权没有逐笔TBT数据。

 1.函数原型
```cpp
virtual int UnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
```
 2.参数

exchange_id：表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持新三板）

 3.返回

退订全市场期权逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

 4.调用示例
```cpp
// 退订全市场期权逐笔行情
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllOptionTickByTick();
}
```
```cpp
// 退订沪市期权逐笔行情
if (user_quote_api_)
{
	int ret = user_quote_api_->UnSubscribeAllOptionTickByTick(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnUnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {};
```


### 39. QueryAllTickersFullInfo


获取沪深所有合约的详细静态信息，包括指数等非可交易的。沪深两市需分市场分别查询。

 1.函数原型
```cpp
virtual int QueryAllTickersFullInfo(XTP_EXCHANGE_TYPE exchange_id) = 0;
```
 2.参数

exchange_id：交易所代码，必须提供，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场（目前不支持新三板）

 3.返回

发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功。

 4.调用示例

```cpp
// 获取沪市所有合约的详细静态信息
if (user_quote_api_)
{
	int ret = user_quote_api_->QueryAllTickersFullInfo(XTP_EXCHANGE_SH);
}
```

 5.响应函数
```cpp
virtual void OnQueryAllTickersFullInfo(XTPQFI* ticker_info, XTPRI *error_info, bool is_last) {};
```


### 40. LoginToRebuildQuoteServer


用户登录回补服务器请求。

此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只能有一个连接。

回补服务器会在无消息交互后定时断线，请注意仅在需要回补数据时才保持连接，回补完成后请及时logout.

 1.函数原型
```cpp
virtual int LoginToRebuildQuoteServer(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;
```
 2.参数

Ip：服务器ip地址，类似"127.0.0.1"

port：服务器端口号

user：登录用户名

password：登录密码

sock_type："1"代表TCP，"2"代表UDP，此处仅支持TCP

local_ip：本地网卡地址，类似"127.0.0.1"，可以为NULL

```cpp
// XTP_PROTOCOL_TYPE是通讯传输协议方式
typedef enum XTP_PROTOCOL_TYPE
{
	XTP_PROTOCOL_TCP = 1,	///LoginToRebuildQuoteServer(quote_rebuild_server_ip.c_str(), quote_rebuild_server_port, quote_rebuild_username.c_str(),
	quote_rebuild_password.c_str(), XTP_PROTOCOL_TCP);
 	if (0 != ret)
	{
		// 登录失败，获取错误信息
		XTPRI* error_info = m_pQuoteApi->GetApiLastError();
		std::cout error_id error_msg LogoutFromRebuildQuoteServer();
}
```


### 42. RequestRebuildQuote


请求回补指定行情，包括快照和逐笔。

仅在逐笔行情丢包时或者确实快照行情时使用，回补的行情数据将从OnRebuildTickByTick或者OnRebuildMarketData()接口回调提供，与订阅的行情数据不在同一个线程内。

注意此函数不能在回调线程中调用。

 1.函数原型
```cpp
virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;
```
 2.参数

rebuild_param：指定回补的参数信息，注意一次性回补最多1000个数据，超过1000需要分批次请求，一次只能指定一种类型的数据

```cpp
///实时行情回补请求结构体
typedef struct XTPQuoteRebuildReq
{
    ///请求id 请求端自行管理定义
    int32_t                     request_id;
    ///请求数据类型 1-快照 2-逐笔
    XTP_QUOTE_REBUILD_DATA_TYPE data_type;
    ///请求市场 1-上海  2-深圳
    XTP_EXCHANGE_TYPE           exchange_id;
    ///合约代码 以'\0'结尾  沪深A股6位  期权8位
    char                        ticker[16];
    ///data_type=逐笔 表示逐笔通道号
    int16_t                     channel_number;
    ///data_type=逐笔 表示序列号begin； =快照 表示时间begin(格式为YYYYMMDDHHMMSSsss)
    int64_t                     begin;
    ///data_type=逐笔 表示序列号end； =快照 表示时间end(格式为YYYYMMDDHHMMSSsss)   逐笔区间：[begin, end]前后闭区间  快照区间：[begin, end)  前闭后开区间
    int64_t                     end;
}XTPQuoteRebuildReq;
```
```cpp
///XTP_QUOTE_DATA_TYPE是行情数据类型 逐笔，快照等
typedef enum XTP_QUOTE_REBUILD_DATA_TYPE {
	XTP_QUOTE_REBUILD_UNKNOW = 0,	///RequestRebuildQuote(&req);
}
```

（2） 请求回补逐笔数据
下面以请求回补沪市频道号为2011，逐笔序列号在[20,78]区间内的逐笔数据为例：
```cpp
//请求回补沪市频道号为2011，逐笔序列号在[20,78]区间内的逐笔数据
if (user_quote_api_)
{
    //回补请求参数赋值
	XTPQuoteRebuildReq req;
	memset(&req, 0, sizeof(XTPQuoteRebuildReq));
	req.request_id = 1;//用户自定义，用来标识此次查询请求
	req.data_type = XTP_QUOTE_REBUILD_TBT;//回补数据类型
	req.exchange_id = XTP_EXCHANGE_SH;//交易所类型，用户根据实际情况修改
	req.channel_number = 2011;//仅逐笔订阅时生效，对于快照可不赋值，用户根据实际情况修改
	req.begin = 20;//逐笔开始的序列号，闭区间，用户根据实际情况修改
	req.end = 78;//逐笔结束的序列号，闭区间，用户根据实际情况修改
    // 发送请求
	int ret = user_quote_api_->RequestRebuildQuote(&req);
}
```

 5.响应函数
```cpp
///请求回补指定频道的逐笔行情的总体结果应答
virtual void OnRequestRebuildQuote(XTPQuoteRebuildResultRsp* rebuild_result) {};
```

6.通知函数
```cpp
///回补的逐笔行情数据
virtual void OnRebuildTickByTick(XTPTBT *tbt_data) {};
///回补的快照行情数据
virtual void OnRebuildMarketData(XTPMD *md_data) {};
```


### 43. QueryAllNQTickersFullInfo


获取新三板所有合约的详细静态信息，包括指数等非可交易的。
此函数仅可在成功登陆新三板行情服务器后使用，如果在沪深行情服务器上使用，将得不到响应。

 1.函数原型
```cpp
virtual int QueryAllNQTickersFullInfo() = 0;
```
 2.参数

无

 3.返回

发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功。

 4.调用示例

```cpp
// 获取新三板所有合约的详细静态信息
if (user_quote_api_)
{
	int ret = user_quote_api_->QueryAllNQTickersFullInfo();
}
```

 5.响应函数
```cpp
virtual void OnQueryAllNQTickersFullInfo(XTPNQFI* ticker_info, XTPRI *error_info, bool is_last) {};
```
