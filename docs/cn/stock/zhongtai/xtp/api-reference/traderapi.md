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
id: zhongtai-xtp-2074064396069466114
title: TraderApi
doc_id: 2074064396069466114
doc_category: 详细接口使用说明
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2074064396069466114'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-07-06
---

# TraderApi

## TraderApi


目录

- [TraderApi](#traderapi)
	- [1. 接口](#1-接口)
	- [2. 示例代码](#2-示例代码)
	- [3. CreateTraderApi](#3-createtraderapi)
	- [4. Release](#4-release)
	- [5. GetTradingDay](#5-gettradingday)
	- [6. RegisterSpi](#6-registerspi)
	- [7. GetApiLastError](#7-getapilasterror)
	- [8. GetApiVersion](#8-getapiversion)
	- [9. GetClientIDByXTPID](#9-getclientidbyxtpid)
	- [10. GetAccountByXTPID](#10-getaccountbyxtpid)
	- [11. SubscribePublicTopic](#11-subscribepublictopic)
	- [12. SetSoftwareVersion](#12-setsoftwareversion)
	- [13. SetSoftwareKey](#13-setsoftwarekey)
	- [14. SetHeartBeatInterval](#14-setheartbeatinterval)
	- [15. SetMaxOrderBufferQuantity](#15-setmaxorderbufferquantity)
	- [16. Login](#16-login)
	- [17. Logout](#17-logout)
	- [18. IsServerRestart](#18-isserverrestart)
	- [19. ModifyUserTerminalInfo](#19-modifyuserterminalinfo)
	- [20. QueryAccountTradeMarket](#20-queryaccounttrademarket)
	- [21. GetANewOrderXTPID](#21-getaneworderxtpid)
	- [22. InsertOrder](#22-insertorder)
	- [23. InsertOrderExtra](#23-insertorderextra)
	- [24. CancelOrder](#24-cancelorder)
	- [25. QueryOrderByXTPID](#25-queryorderbyxtpid)
	- [26. QueryOrders](#26-queryorders)
	- [27. QueryUnfinishedOrders](#27-queryunfinishedorders)
	- [28. QueryOrdersByPage](#28-queryordersbypage)
	- [29. QueryOrderByXTPIDEx](#29-queryorderbyxtpidex)
	- [30. QueryOrdersEx](#30-queryordersex)
	- [31. QueryUnfinishedOrdersEx](#31-queryunfinishedordersex)
	- [32. QueryOrdersByPageEx](#32-queryordersbypageex)
	- [33. QueryTradesByXTPID](#33-querytradesbyxtpid)
	- [34. QueryTrades](#34-querytrades)
	- [35. QueryTradesByPage](#35-querytradesbypage)
	- [36. QueryPosition](#36-queryposition)
	- [37. QueryAsset](#37-queryasset)
	- [38. QueryStructuredFund](#38-querystructuredfund)
	- [39. FundTransfer](#39-fundtransfer)
	- [40. QueryFundTransfer](#40-queryfundtransfer)
	- [41. QueryOtherServerFund](#41-queryotherserverfund)
	- [42. QueryETF](#42-queryetf)
	- [43. QueryETFTickerBasket](#43-queryetftickerbasket)
	- [44. QueryIPOInfoList](#44-queryipoinfolist)
	- [45. QueryIPOQuotaInfo](#45-queryipoquotainfo)
	- [46. QueryBondIPOInfoList](#46-querybondipoinfolist)
	- [47. QueryOptionAuctionInfo](#47-queryoptionauctioninfo)
	- [48. CreditCashRepay](#48-creditcashrepay)
	- [49. CreditCashRepayDebtInterestFee](#49-creditcashrepaydebtinterestfee)
	- [50. CreditSellStockRepayDebtInterestFee](#50-creditsellstockrepaydebtinterestfee)
	- [51. QueryCreditCashRepayInfo](#51-querycreditcashrepayinfo)
	- [52. QueryCreditFundInfo](#52-querycreditfundinfo)
	- [53. QueryCreditDebtInfo](#53-querycreditdebtinfo)
	- [54. QueryCreditTickerDebtInfo](#54-querycredittickerdebtinfo)
	- [55. QueryCreditAssetDebtInfo](#55-querycreditassetdebtinfo)
	- [56. QueryCreditTickerAssignInfo](#56-querycredittickerassigninfo)
	- [57. QueryCreditExcessStock](#57-querycreditexcessstock)
	- [58. QueryMulCreditExcessStock](#58-querymulcreditexcessstock)
	- [59. CreditExtendDebtDate](#59-creditextenddebtdate)
	- [60. QueryCreditExtendDebtDateOrders](#60-querycreditextenddebtdateorders)
	- [61. QueryCreditFundExtraInfo](#61-querycreditfundextrainfo)
	- [62. QueryCreditPositionExtraInfo](#62-querycreditpositionextrainfo)
	- [63. InsertOptionCombinedOrder](#63-insertoptioncombinedorder)
	- [64. InsertOptionCombinedOrderExtra](#64-insertoptioncombinedorderextra)
	- [65. CancelOptionCombinedOrder](#65-canceloptioncombinedorder)
	- [66. QueryOptionCombinedUnfinishedOrders](#66-queryoptioncombinedunfinishedorders)
	- [67. QueryOptionCombinedOrderByXTPID](#67-queryoptioncombinedorderbyxtpid)
	- [68. QueryOptionCombinedOrders](#68-queryoptioncombinedorders)
	- [69. QueryOptionCombinedOrdersByPage](#69-queryoptioncombinedordersbypage)
	- [70. QueryOptionCombinedUnfinishedOrdersEx](#70-queryoptioncombinedunfinishedordersex)
	- [71. QueryOptionCombinedOrderByXTPIDEx](#71-queryoptioncombinedorderbyxtpidex)
	- [72. QueryOptionCombinedOrdersEx](#72-queryoptioncombinedordersex)
	- [73. QueryOptionCombinedOrdersByPageEx](#73-queryoptioncombinedordersbypageex)
	- [74. QueryOptionCombinedTradesByXTPID](#74-queryoptioncombinedtradesbyxtpid)
	- [75. QueryOptionCombinedTrades](#75-queryoptioncombinedtrades)
	- [76. QueryOptionCombinedTradesByPage](#76-queryoptioncombinedtradesbypage)
	- [77. QueryOptionCombinedPosition](#77-queryoptioncombinedposition)
	- [78. QueryOptionCombinedStrategyInfo](#78-queryoptioncombinedstrategyinfo)
	- [79. QueryOptionCombinedExecPosition](#79-queryoptioncombinedexecposition)
	- [80. LoginALGO](#80-loginalgo)
	- [81. QueryStrategy](#81-querystrategy)
	- [82. ALGOUserEstablishChannel](#82-algouserestablishchannel)
	- [83. InsertAlgoOrder](#83-insertalgoorder)
	- [84. CancelAlgoOrder](#84-cancelalgoorder)
	- [85. GetAlgorithmIDByOrder](#85-getalgorithmidbyorder)
	- [86. StrategyRecommendation](#86-strategyrecommendation)
	- [87. QueryBondSwapStockInfo](#87-querybondswapstockinfo)
	- [88. ModifyAlgoOrder](#88-modifyalgoorder)
	- [89. PauseAlgoOrder](#89-pausealgoorder)
	- [90. ResumeAlgoOrder](#90-resumealgoorder)


TraderApi类提供了交易api的初始化、登录、报单等功能。

### 1. 接口


```cpp
namespace XTP {
	namespace API {
		class TRADER_API_EXPORT TraderApi
		{
		public:
			///创建TraderApi
			///@param client_id （必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义，普通用户必须使用1-99之间的数值，否则可能无法登录
			///@param save_file_path （必须输入）存贮订阅信息文件的目录，请设定一个真实存在的有可写权限的路径
			///@param log_level 日志输出级别
			///@return 创建出的UserApi
			///@remark 只能创建一次，如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，但是对于同一账户，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接。系统不支持过夜，请确保每天开盘前重新启动
			static TraderApi *CreateTraderApi(uint8_t client_id, const char *save_file_path, XTP_LOG_LEVEL log_level = XTP_LOG_LEVEL_DEBUG);

			///删除接口对象本身
			///@remark 不再使用本接口对象时,调用该函数删除接口对象
			virtual void Release() = 0;

			///获取当前交易日
			///@return 获取到的交易日
			///@remark 只有登录成功后,才能得到正确的交易日
			virtual const char *GetTradingDay() = 0;

			///注册回调接口
			///@param spi 派生自回调接口类的实例，请在登录之前设定
			virtual void RegisterSpi(TraderSpi *spi) = 0;

			///获取API的系统错误
			///@return 返回的错误信息，可以在Login、InsertOrder、CancelOrder返回值为0时调用，获取失败的原因
			///@remark 可以在调用api接口失败时调用，例如login失败时
			virtual XTPRI *GetApiLastError() = 0;

			///获取API的发行版本号
			///@return 返回api发行版本号
			virtual const char* GetApiVersion() = 0;

			///通过报单在xtp系统中的ID获取下单的客户端id
			///@return 返回客户端id，可以用此方法过滤自己下的订单
			///@param order_xtp_id 报单在xtp系统中的ID
			///@remark 由于系统允许同一用户在不同客户端上登录操作，每个客户端通过不同的client_id进行区分
			virtual uint8_t GetClientIDByXTPID(uint64_t order_xtp_id) = 0;

			///通过报单在xtp系统中的ID获取相关资金账户名
			///@return 返回资金账户名
			///@param order_xtp_id 报单在xtp系统中的ID
			///@remark 只有资金账户登录成功后,才能得到正确的信息
			virtual const char* GetAccountByXTPID(uint64_t order_xtp_id) = 0;

			///订阅公共流。
			///@param resume_type 公共流（订单响应、成交回报）重传方式
			///        XTP_TERT_RESTART:从本交易日开始重传
			///        XTP_TERT_RESUME:(保留字段，此方式暂未支持)从上次收到的续传
			///        XTP_TERT_QUICK:只传送登录后公共流的内容
			///@remark 该方法要在Login方法前调用。若不调用则不会收到公共流的数据。注意在用户断线后，如果不登出就login()，公共流订阅方式不会起作用。用户只会收到断线后的所有消息。如果先logout()再login()，那么公共流订阅方式会起作用，用户收到的数据会根据用户的选择方式而定。
			virtual void SubscribePublicTopic(XTP_TE_RESUME_TYPE resume_type) = 0;

			///设置软件开发版本号
			///@param version 用户开发软件版本号，非api发行版本号，长度不超过15位，以'\0'结尾
			///@remark 此函数必须在Login之前调用，标识的是客户端版本号，而不是API的版本号，由用户自定义
			virtual void SetSoftwareVersion(const char* version) = 0;

			///设置软件开发Key
			///@param key 用户开发软件Key，用户申请开户时给予，以'\0'结尾
			///@remark 此函数必须在Login之前调用
			virtual void SetSoftwareKey(const char* key) = 0;

			///设置心跳检测时间间隔，单位为秒
			///@param interval 心跳检测时间间隔，单位为秒
			///@remark 此函数必须在Login之前调用
			virtual void SetHeartBeatInterval(uint32_t interval) = 0;

			///设置单个用户当日报单总量的最大值
			///@return true表示设置成功，false表示设置失败;若设置失败则采用默认值；
			///@param max_order_qty 当日报单总量的最大值，范围：0~(1024*1024*32-1000)
			///@remark 此函数为设置该Api内部单个账户的缓存订单总量，该缓存非动态增减，必须在Login之前调用；若不调用则默认最大值为1024*200；实际报单总量若大于预设值，报单则报错
			virtual bool SetMaxOrderBufferQuantity(uint32_t max_order_qty) = 0;

			///用户登录请求
			///@return session_id表明此资金账号登录是否成功，“0”表示登录失败，可以调用GetApiLastError()来获取错误代码，非“0”表示登录成功，此时需要记录下这个返回值session_id，与登录的资金账户对应
			///@param ip 服务器地址，类似“127.0.0.1”
			///@param port 服务器端口号
			///@param user 登录用户名
			///@param password 登录密码
			///@param sock_type “1”代表TCP，“2”代表UDP，目前暂时只支持TCP
			///@param local_ip 本地网卡地址，类似“127.0.0.1”
			///@remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api可支持多个账户连接，但是同一个账户同一个client_id只能有一个session连接，后面的登录在前一个session存续期间，无法连接
			virtual uint64_t Login(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;


			///登出请求
			///@return 登出是否成功，“0”表示登出成功，“-1”表示登出失败
			///@param session_id 资金账户对应的session_id,登录时得到
			virtual int Logout(uint64_t session_id) = 0;

			///服务器是否重启过
			///@return “true”表示重启过，“false”表示没有重启过
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 此函数必须在Login之后调用
			virtual bool IsServerRestart(uint64_t session_id) = 0;

			///修改已登录用户的硬件信息，仅限授权系统使用
			///@return 发送消息是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param info 需要修改成的用户硬件信息
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 此函数必须在Login之后调用，且仅限授权系统使用，一般客户无需使用
			virtual int ModifyUserTerminalInfo(XTPUserTerminalInfoReq* info,uint64_t session_id) = 0;

			///查询用户在本节点上的可交易市场类型
			///@return 发送消息是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 此函数必须在Login之后调用，对应的响应函数是OnQueryAccountTradeMarket()
			virtual int QueryAccountTradeMarket(uint64_t session_id, int request_id) = 0;

			///为用户获取一个新的订单XTPID，用于报单
			///@return 生成的订单XTPID，非“0”表示获取成功，“0”表示获取失败，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 此函数必须在Login之后调用，通过这个函数获取的order_xtp_id仅用于对应的用户报单，如果设置错误，将会导致下单失败
			virtual uint64_t GetANewOrderXTPID(uint64_t session_id) = 0;

			///报单录入请求
			///@return 报单在XTP系统中的ID,如果为‘0’表示报单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示报单发送成功，用户需要记录下返回的order_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
			///@param order 报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。order.order_xtp_id字段无需用户填写，order.ticker必须不带空格，以'\0'结尾
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 交易所接收订单后，会在报单响应函数OnOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回
			virtual uint64_t InsertOrder(XTPOrderInsertInfo *order, uint64_t session_id) = 0;

			///已经提前设置order_xtp_id的报单录入请求，与GetANewOrderXTPID()配合使用
			///@return 报单在XTP系统中的ID,如果为‘0’表示报单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示报单发送成功，此时等同与传入的order_xtp_id
			///@param order 报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单，也可以什么都不填。order.order_xtp_id字段必须是通过GetANewOrderXTPID()获得的值，order.ticker必须不带空格，以'\0'结尾
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 使用设置好的order_xtp_id（通过GetANewOrderXTPID()获得）进行报单，注意此处如果order_xtp_id设置不对，将导致报单失败。交易所接收订单后，会在报单响应函数OnOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回
			virtual uint64_t InsertOrderExtra(XTPOrderInsertInfo *order, uint64_t session_id) = 0;

			///报单操作请求
			///@return 撤单在XTP系统中的ID,如果为‘0’表示撤单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示撤单发送成功，用户需要记录下返回的order_cancel_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
			///@param order_xtp_id 需要撤销的委托单在XTP系统中的ID
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 如果撤单成功，会在报单响应函数OnOrderEvent()里返回原单部撤或者全撤的消息，如果不成功，会在OnCancelOrderError()响应函数中返回错误原因
			virtual uint64_t CancelOrder(const uint64_t order_xtp_id, uint64_t session_id) = 0;

			///根据报单ID请求查询报单-旧版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param order_xtp_id 需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryOrderByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;

			///请求查询报单-旧版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual int QueryOrders(const XTPQueryOrderReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询未完结报单-旧版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryUnfinishedOrders(uint64_t session_id, int request_id) = 0;

			///分页请求查询报单-旧版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
			virtual int QueryOrdersByPage(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

			///根据报单ID请求查询报单-新版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param order_xtp_id 需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryOrderByXTPIDEx(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;

			///请求查询报单-新版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual int QueryOrdersEx(const XTPQueryOrderReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询未完结报单-新版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryUnfinishedOrdersEx(uint64_t session_id, int request_id) = 0;

			///分页请求查询报单-新版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
			virtual int QueryOrdersByPageEx(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

			///根据委托编号请求查询相关成交
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param order_xtp_id 需要查询的委托编号，即InsertOrder()成功时返回的order_xtp_id
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 此函数查询出的结果可能对应多个查询结果响应
			virtual int QueryTradesByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;

			///请求查询已成交
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的成交回报筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有成交回报，否则查询时间段内所有跟股票代码相关的成交回报，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual int QueryTrades(XTPQueryTraderReq *query_param, uint64_t session_id, int request_id) = 0;

			///分页请求查询成交回报
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要分页查询成交回报的条件，如果第一次查询，那么reference填0
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
			virtual int QueryTradesByPage(const XTPQueryTraderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询投资者持仓
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param ticker 需要查询持仓的合约代码，可以为NULL，表示查询全市场，如果不为NULL，请不带空格，并以'\0'结尾，注意需与market匹配，不匹配的话，可能由于证券代码沪深2个市场有重复，而导致查询不到所需的持仓
			///@param market 需要查询持仓的合约所在市场，默认为0，仅在合约代码不为NULL的时候，才会使用。market不指定或者为非0的其他非有效值情况下，可能由于证券代码沪深2个市场有重复，而导致查询不到所需的持仓。如果想正确查询指定持仓，请指定market
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法如果用户提供了合约代码，则会查询此合约的持仓信息（注意请指定market，如果market为0，可能会查询到2个市场的持仓，如果market为其他非有效值，则查询结果会返回找不到持仓），如果合约代码为空，则默认查询所有持仓信息。
			virtual int QueryPosition(const char *ticker, uint64_t session_id, int request_id, XTP_MARKET_TYPE market = XTP_MKT_INIT) = 0;

			///请求查询资产
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryAsset(uint64_t session_id, int request_id) = 0;

			///请求查询分级基金
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的分级基金筛选条件，其中母基金代码可以为空，则默认所有存在的母基金，如果不为空，请不带空格，并以'\0'结尾，其中交易市场不能为空
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 此函数查询出的结果可能对应多个查询结果响应
			virtual int QueryStructuredFund(XTPQueryStructuredFundInfoReq *query_param, uint64_t session_id, int request_id) = 0;

			///资金划拨请求
			///@return 资金划拨订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示消息发送成功，用户需要记录下返回的serial_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
			///@param fund_transfer 资金划拨的请求信息
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 此函数支持一号两中心节点之间的资金划拨，注意资金划拨的方向。
			virtual uint64_t FundTransfer(XTPFundTransferReq *fund_transfer, uint64_t session_id) = 0;

			///请求查询资金划拨
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的资金划拨订单筛选条件，其中serial_id可以为0，则默认所有资金划拨订单，如果不为0，则请求特定的资金划拨订单
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryFundTransfer(XTPQueryFundTransferLogReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询其他节点可用资金
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 查询时需要提供的信息
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryOtherServerFund(XTPFundQueryReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询ETF清单文件
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的ETF清单文件的筛选条件，其中合约代码可以为空，则默认所有存在的ETF合约代码，market字段也可以为初始值，则默认所有市场的ETF合约
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryETF(XTPQueryETFBaseReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询ETF股票篮
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询股票篮的的ETF合约，其中合约代码不可以为空，market字段也必须指定
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryETFTickerBasket(XTPQueryETFComponentReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询今日新股申购信息列表
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryIPOInfoList(uint64_t session_id, int request_id) = 0;

			///请求查询用户新股申购额度信息
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryIPOQuotaInfo(uint64_t session_id, int request_id) = 0;

			///请求查询可转债转股的基本信息
			///@return 查询是否发送成功，“0”表示发送成功，非“0”表示发送出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的可转债转股信息的筛选条件，可以为NULL（为NULL表示查询所有的可转债转股信息），此参数中合约代码可以为空字符串，如果为空字符串，则查询所有可转债转股信息，如果不为空字符串，请不带空格，并以'\0'结尾，且必须与market匹配
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryBondSwapStockInfo(XTPQueryBondSwapStockReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询期权合约
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的期权合约的筛选条件，可以为NULL（为NULL表示查询所有的期权合约）
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryOptionAuctionInfo(XTPQueryOptionAuctionInfoReq *query_param, uint64_t session_id, int request_id) = 0;

			///融资融券业务中现金直接还款请求
			///@return 现金直接还款订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示消息发送成功，用户需要记录下返回的xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
			///@param amount 现金还款的金额
			///@param session_id 资金账户对应的session_id,登录时得到
			virtual uint64_t CreditCashRepay(double amount, uint64_t session_id) = 0;

			///融资融券业务中现金还指定负债合约息费请求
			///@return 现金还息订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示消息发送成功，用户需要记录下返回的xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
			///@param debt_id 指定的负债合约编号
			///@param amount 现金还息的金额
			///@param session_id 资金账户对应的session_id,登录时得到
			virtual uint64_t CreditCashRepayDebtInterestFee(const char* debt_id, double amount, uint64_t session_id) = 0;

			///融资融券业务中卖券还指定负债合约息费请求
			///@return 卖券还息订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示消息发送成功，用户需要记录下返回的xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
			///@param order 卖券的报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。order.order_xtp_id字段无需用户填写，order.ticker必须不带空格，以'\0'结尾
			///@param debt_id 指定的负债合约编号
			///@param session_id 资金账户对应的session_id,登录时得到
			virtual uint64_t CreditSellStockRepayDebtInterestFee(XTPOrderInsertInfo* order, const char* debt_id, uint64_t session_id) = 0;

			///请求查询融资融券业务中的现金直接还款报单
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryCreditCashRepayInfo(uint64_t session_id, int request_id) = 0;

			///请求查询信用账户特有信息，除资金账户以外的信息
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryCreditFundInfo(uint64_t session_id, int request_id) = 0;

			///请求查询信用账户负债合约信息
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryCreditDebtInfo(uint64_t session_id, int request_id) = 0;

			///请求查询指定证券负债未还信息
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的指定证券，筛选条件中ticker可以全填0，如果不为0，请不带空格，并以'\0'结尾
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryCreditTickerDebtInfo(XTPClientQueryCrdDebtStockReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询信用账户待还资金信息
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryCreditAssetDebtInfo(uint64_t session_id, int request_id) = 0;

			///请求查询信用账户可融券头寸信息
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的证券，筛选条件中ticker可以全填0，如果不为0，请不带空格，并以'\0'结尾
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryCreditTickerAssignInfo(XTPClientQueryCrdPositionStockReq *query_param, uint64_t session_id, int request_id) = 0;

			///融资融券业务中请求查询指定证券的余券
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的余券信息，不可以为空，需要明确指定
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法中用户必须提供了证券代码和所在市场
			virtual int QueryCreditExcessStock(XTPClientQueryCrdSurplusStkReqInfo *query_param, uint64_t session_id, int request_id) = 0;

			///融资融券业务中请求查询余券
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的余券信息。若填入市场和股票代码，返回单支股票信息；若市场代码为空，股票代码非空，是无效查询，会在SPI中返回错误；若市场和股票代码均为空，返回全市场信息；若市场代码非空，股票代码为空，返回单市场信息。
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryMulCreditExcessStock(XTPClientQueryCrdSurplusStkReqInfo *query_param, uint64_t session_id, int request_id) = 0;

			///融资融券业务中请求负债合约展期
			///@return 负债合约展期订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示消息发送成功，用户需要记录下返回的xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
			///@param debt_extend 负债合约展期的请求信息
			///@param session_id 资金账户对应的session_id,登录时得到
			virtual uint64_t CreditExtendDebtDate(XTPCreditDebtExtendReq *debt_extend, uint64_t session_id) = 0;

			///融资融券业务中请求查询负债合约展期
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param xtp_id 需要查询的负债合约展期订单筛选条件，xtp_id可以为0，则默认所有负债合约展期订单，如果不为0，则请求特定的负债合约展期订单
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryCreditExtendDebtDateOrders(uint64_t xtp_id, uint64_t session_id, int request_id) = 0;

			///请求查询融资融券业务中账戶的附加信息
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryCreditFundExtraInfo(uint64_t session_id, int request_id) = 0;

			///请求查询融资融券业务中账戶指定证券的附加信息
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要指定的证券，筛选条件中ticker可以全填0，如果不为0，请不带空格，并以'\0'结尾
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryCreditPositionExtraInfo(XTPClientQueryCrdPositionStockReq *query_param, uint64_t session_id, int request_id) = 0;

			///期权组合策略报单录入请求
			///@return 报单在XTP系统中的ID,如果为‘0’表示报单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示报单发送成功，用户需要记录下返回的order_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
			///@param order 报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOptionCombinedOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。order.order_xtp_id字段无需用户填写，order.ticker必须不带空格，以'\0'结尾
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 交易所接收订单后，会在报单响应函数OnOptionCombinedOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回
			virtual uint64_t InsertOptionCombinedOrder(XTPOptCombOrderInsertInfo *order, uint64_t session_id) = 0;

			///已经提前设置order_xtp_id的期权组合策略报单录入请求，与GetANewOrderXTPID()配合使用
			///@return 报单在XTP系统中的ID,如果为‘0’表示报单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示报单发送成功，此时等同与传入的order_xtp_id
			///@param order 报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单，也可以什么都不填。order.order_xtp_id字段必须是通过GetANewOrderXTPID()获得的值，order.ticker必须不带空格，以'\0'结尾
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 使用设置好的order_xtp_id（通过GetANewOrderXTPID()获得）进行报单，注意此处如果order_xtp_id设置不对，将导致报单失败。交易所接收订单后，会在报单响应函数OnOptionCombinedOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回
			virtual uint64_t InsertOptionCombinedOrderExtra(XTPOptCombOrderInsertInfo *order, uint64_t session_id) = 0;

			///期权组合策略报单撤单请求
			///@return 撤单在XTP系统中的ID,如果为‘0’表示撤单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示撤单发送成功，用户需要记录下返回的order_cancel_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
			///@param order_xtp_id 需要撤销的期权组合策略委托单在XTP系统中的ID
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 如果撤单成功，会在报单响应函数OnOptionCombinedOrderEvent()里返回原单部撤或者全撤的消息，如果不成功，会在OnCancelOrderError()响应函数中返回错误原因
			virtual uint64_t CancelOptionCombinedOrder(const uint64_t order_xtp_id, uint64_t session_id) = 0;

			///请求查询期权组合策略未完结报单-旧版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryOptionCombinedUnfinishedOrders(uint64_t session_id, int request_id) = 0;

			///根据报单ID请求查询期权组合策略报单-旧版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param order_xtp_id 需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryOptionCombinedOrderByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;

			///请求查询期权组合策略报单-旧版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual int QueryOptionCombinedOrders(const XTPQueryOptCombOrderReq *query_param, uint64_t session_id, int request_id) = 0;

			///分页请求查询期权组合策略报单-旧版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
			virtual int QueryOptionCombinedOrdersByPage(const XTPQueryOptCombOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询期权组合策略未完结报单-新版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryOptionCombinedUnfinishedOrdersEx(uint64_t session_id, int request_id) = 0;

			///根据报单ID请求查询期权组合策略报单-新版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param order_xtp_id 需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			virtual int QueryOptionCombinedOrderByXTPIDEx(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;

			///请求查询期权组合策略报单-新版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual int QueryOptionCombinedOrdersEx(const XTPQueryOptCombOrderReq *query_param, uint64_t session_id, int request_id) = 0;

			///分页请求查询期权组合策略报单-新版本接口
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
			virtual int QueryOptionCombinedOrdersByPageEx(const XTPQueryOptCombOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

			///根据期权组合策略委托编号请求查询相关成交
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param order_xtp_id 需要查询的委托编号，即InsertOrder()成功时返回的order_xtp_id
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 此函数查询出的结果可能对应多个查询结果响应
			virtual int QueryOptionCombinedTradesByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;

			///请求查询期权组合策略的成交回报
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的成交回报筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有成交回报，否则查询时间段内所有跟股票代码相关的成交回报，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
			virtual int QueryOptionCombinedTrades(const XTPQueryOptCombTraderReq *query_param, uint64_t session_id, int request_id) = 0;

			///分页请求查询期权组合策略成交回报
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要分页查询成交回报的条件，如果第一次查询，那么reference填0
			///@param session_id 资金账户对应的session_id，登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
			virtual int QueryOptionCombinedTradesByPage(const XTPQueryOptCombTraderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

			///请求查询投资者期权组合策略持仓
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询持仓的筛选条件，其中组合策略代码可以初始化为空，表示查询所有，如果不为空，请不带空格，并以'\0'结尾，注意需与market匹配，不匹配的话，可能导致查询不到所需的持仓
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法如果用户提供了合约代码，则会查询此合约的持仓信息（注意请指定market，如果market为0，可能会查询到2个市场的持仓，如果market为其他非有效值，则查询结果会返回找不到持仓），如果合约代码为空，则默认查询所有持仓信息。
			virtual int QueryOptionCombinedPosition(const XTPQueryOptCombPositionReq* query_param, uint64_t session_id, int request_id) = 0;

			///请求查询期权组合策略信息
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法仅支持精确查询，不支持模糊查询
			virtual int QueryOptionCombinedStrategyInfo(uint64_t session_id, int request_id) = 0;

			///请求查询期权行权合并头寸
			///@return 查询请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param query_param 需要查询的行权合并的筛选条件，其中market为0会默认查询全市场，成分合约代码可以初始化为空，如果不为空，请不带空格，并以'\0'结尾，注意所有填写的条件都会进行匹配
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 该方法可能对应多条响应消息
			virtual int QueryOptionCombinedExecPosition(const XTPQueryOptCombExecPosReq* query_param, uint64_t session_id, int request_id) = 0;

			///用户登录algo服务器请求
			///@return 表明此资金账号登录是否成功，非“0”表示登录失败，可以调用GetApiLastError()来获取错误代码，“0”表示登录成功
			///@param ip algo服务器地址，类似“127.0.0.1”
			///@param port algo服务器端口号
			///@param user 登录用户名
			///@param password 登录密码
			///@param sock_type “1”代表TCP，“2”代表UDP，目前暂时只支持TCP
			///@param local_ip 本地网卡地址，类似“127.0.0.1”
			///@remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只需调用一次，所有用户共用即可
			virtual int LoginALGO(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;

			///algo业务中查询用户策略请求
			///@return 请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param strategy_type 需要查询的策略类型，可填0
			///@param client_strategy_id 需要查询的策略用户自定义id，可填0
			///@param xtp_strategy_id 需要查询的策略在xtp系统中的id，如果指定，就一定按指定查询，如果填0，则按其他筛选条件查询
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark xtp_strategy_id条件的优先级最高，只有当xtp_strategy_id为0时，其他条件才生效，此条请求可能对应多条回应消息
			virtual int QueryStrategy(uint32_t strategy_type, uint64_t client_strategy_id, uint64_t xtp_strategy_id, uint64_t session_id, int32_t request_id) = 0;

			///用户请求使用algo服务器建立算法通道
			///@return 表明此资金账号建立算法通道请求消息发送是否成功，非“0”表示发送失败，可以调用GetApiLastError()来获取错误代码，“0”表示发送成功
			///@param oms_ip oms服务器地址，类似“127.0.0.1”，非algo服务器地址
			///@param oms_port oms服务器端口号，非algo服务器端口号
			///@param user 登录用户名
			///@param password 登录密码
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 此函数为异步方式，一个用户只能拥有一个算法通道，如果之前已经建立，则无需重复建立，在使用算法前，请先建立算法通道
			virtual int ALGOUserEstablishChannel(const char* oms_ip, int oms_port, const char* user, const char* password, uint64_t session_id) = 0;

			///algo业务中用户报算法单请求
			///@return 算法报单请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param strategy_type 需要创建的策略类型
			///@param client_strategy_id 用户自定义id，帮助用户定位
			///@param strategy_param 策略参数
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 仅能在用户建立算法通道后使用
			virtual int InsertAlgoOrder(uint32_t strategy_type, uint64_t client_strategy_id, char* strategy_param, uint64_t session_id) = 0;

			///algo业务中用户撤销算法单请求
			///@return 请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param cancel_flag 是否需要撤销的算法单已下的订单，true-撤单，false-不撤单
			///@param xtp_strategy_id 需要撤销的算法单在xtp algobus系统中的id
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 仅能在用户建立算法通道后调用
			virtual int CancelAlgoOrder(bool cancel_flag, uint64_t xtp_strategy_id, uint64_t session_id) = 0;

			///获取算法单的母单ID
			///@return 返回算法单的母单ID，如果返回为0表示不是算法单
			///@param order_xtp_id 算法单对应的xtp id
			///@param order_client_id 算法单对应的自定义ID，不可随意填写
			///@remark 返回为0表示，不是算法单，如果传入的参数不对的话，可能会得不到正确结果，此函数调用不依赖于是否登录
			virtual uint64_t GetAlgorithmIDByOrder(uint64_t order_xtp_id, uint32_t order_client_id) = 0;

			///algo业务中请求推荐算法
			///@return 请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param basket_flag 是否将满足条件的推荐结果打包成母单篮的标志，true-打包
			///@param basket_param 需要算法推荐的证券列表，为json字串，具体格式参考说明文档或咨询运营人员
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 此条请求可能对应多条回应消息
			virtual int StrategyRecommendation(bool basket_flag, char* basket_param, uint64_t session_id, int32_t request_id) = 0;

			///algo业务中修改已有的算法单
			///@return 算法单修改请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param xtp_strategy_id xtp算法单策略ID
			///@param strategy_param 修改后的策略参数
			///@param session_id 资金账户对应的session_id,登录时得到
			///@remark 仅能在用户建立算法通道后使用，此功能上线时间视服务器后台支持情况而定，具体以运营通知时间为准
			virtual int ModifyAlgoOrder(uint64_t xtp_strategy_id, char* strategy_param, uint64_t session_id) = 0;

			///algo业务中暂停指定策略中指定证券的算法单请求
			///@return 请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param xtp_strategy_id xtp算法单策略ID
			///@param ticker_info 指定证券信息，可以为null，为null表示暂停指定策略中所有证券的算法单
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 仅能在用户建立算法通道后使用，此功能上线时间视服务器后台支持情况而定，具体以运营通知时间为准
			virtual int PauseAlgoOrder(uint64_t xtp_strategy_id, XTPStrategyTickerInfo* ticker_info, uint64_t session_id, int32_t request_id) = 0;

			///algo业务中重启指定策略中指定证券的算法单请求
			///@return 请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
			///@param xtp_strategy_id xtp算法单策略ID
			///@param ticker_info 指定证券信息，可以为null，为null表示重启指定策略中所有证券的算法单
			///@param session_id 资金账户对应的session_id,登录时得到
			///@param request_id 用于用户定位查询响应的ID，由用户自定义
			///@remark 仅能在用户建立算法通道后使用，此功能上线时间视服务器后台支持情况而定，具体以运营通知时间为准
			virtual int ResumeAlgoOrder(uint64_t xtp_strategy_id, XTPStrategyTickerInfo* ticker_info, uint64_t session_id, int32_t request_id) = 0;

		protected:
			~TraderApi() {};
		};
	}
}
```


### 2. 示例代码


以下是MyTraderApi.h文件
```cpp
#include "xtp_trader_api.h"
#include "MyTraderSpi.h"

using namespace XTP::API;

class MyTraderApi
{
public:
	explicit MyTraderApi();
	~MyTraderApi();

	// 初始化
	bool initialize();

private:
	TraderApi *user_trade_api;
	MyTraderSpi *m_trader_spi;
};
```
以下是MyTraderApi.cpp文件
```cpp
#include "MyTraderApi.h"

MyTraderApi::MyTraderApi()
{
	user_trade_api_ = nullptr;
    m_trader_spi = nullptr;
}

MyTraderApi::~MyTraderApi()
{

}

bool MyTraderApi::initialize()
{
	// 创建并初始化交易API
	user_trade_api_ = XTP::API::TraderApi::CreateTraderApi(1, "./", XTP_LOG_LEVEL_DEBUG);
	if (user_trader_api_)
	{
		// 注册回调接口
		m_trader_spi = new MyTraderSpi();
		user_trade_api_->RegisterSpi(m_trader_spi);
		// 登录前参数设置，用户请自行修改
		user_trade_api_->SetHeartBeatInterval(15);
		user_trade_api_->SetSoftwareKey("xxxxxxxxxx");
		user_trade_api_->SetSoftwareVersion("xx.xx.xx.xx");
		// 设置公有流（订单响应、成交回报）重传方式
		user_trade_api_->SubscribePublicTopic(XTP_TERT_QUICK);

		return true;
	}
	return false;
}
```


### 3. CreateTraderApi


创建TraderApi的实例。只能创建一次，如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，但是对于同一账户，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接。系统不支持过夜，请确保每天开盘前重新启动。

 1.函数原型
```cpp
static TraderApi *CreateTraderApi(uint8_t client_id, const char *save_file_path, XTP_LOG_LEVEL log_level = XTP_LOG_LEVEL_DEBUG);
```
 2.参数

client_id：（必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义，普通用户必须使用1-99之间的数值

save_file_path：（必须输入）存储交易api日志文件的目录，请设定一个真实存在的有可写权限的路径

log_level：日志输出级别

 3.返回

无

 4.调用示例
```cpp
//初始化api，创建单例
uint8_t client_id_ = 1;
string stdstr_log_path("./");
// 开发调试时用XTP_LOG_LEVEL_DEBUG，稳定运行时用XTP_LOG_LEVEL_INFO
XTP_LOG_LEVEL log_level = XTP_LOG_LEVEL_DEBUG;

XTP::API::TraderApi* user_trade_api_ = XTP::API::TraderApi::CreateTraderApi(client_id_, stdstr_log_path.c_str(), log_level);

if (user_trade_api_)
{
	// 注册回调接口
	MyTraderSpi *spi = new MyTraderSpi();
	user_trade_api_->RegisterSpi(spi);
}
```


### 4. Release


删除接口对象本身。当程序退出前，不再使用本接口对象时，调用该函数删除接口对象。

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
// 登出并删除接口对象
if (user_trade_api_)
{
	user_trade_api_->Logout(session_id_);
	user_trade_api_->Release();
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
// 获取交易日
if (user_trade_api_)
{
	std::cout GetTradingDay() RegisterSpi(spi);
}
```


### 7. GetApiLastError


获取API的系统错误。返回的错误信息，可以在Login、InsertOrder、CancelOrder返回值为0时调用，获取失败的原因。可以在调用api接口失败时调用，例如login失败时

 1.函数原型
```cpp
virtual XTPRI *GetApiLastError() = 0;
```
 2.参数

无

 3.返回

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

 4.调用示例
```cpp
// 获取API的系统错误
if (user_trade_api_)
{
	XTPRI* error_info = user_trade_api_->GetApiLastError();
	std::cout error_id error_msg GetApiVersion() GetClientIDByXTPID(order_xtp_id);
}
```


### 10. GetAccountByXTPID


通过报单在xtp系统中的ID获取相关资金账户名。只有资金账户登录成功后,才能得到正确的信息。

 1.函数原型
```cpp
virtual const char* GetAccountByXTPID(uint64_t order_xtp_id) = 0;
```
 2.参数

order_xtp_id：报单在xtp系统中的ID

 3.返回

返回资金账户名。

 4.调用示例
```cpp
// 通过报单在xtp系统中的ID获取相关资金账户名
if (user_trade_api_)
{
	const char *clientAccount = user_trade_api_->GetAccountByXTPID(order_xtp_id);
}
```


### 11. SubscribePublicTopic


订阅公共流。该方法要在Login方法前调用。若不调用则默认是用quick方式。注意在用户断线后，如果不登出就login()，公共流订阅方式将会默认使用resume方式。用户收到的数据会根据用户的选择方式而定。

 1.函数原型
```cpp
virtual void SubscribePublicTopic(XTP_TE_RESUME_TYPE resume_type) = 0;
```
 2.参数

```cpp
///XTP_TE_RESUME_TYPE是公有流（订单响应、成交回报）重传方式
typedef enum XTP_TE_RESUME_TYPE
{
	XTP_TERT_RESTART = 0,	///SubscribePublicTopic(XTP_TERT_QUICK);
}
```


### 12. SetSoftwareVersion


设置软件开发版本号。此函数必须在Login之前调用。

 1.函数原型
```cpp
virtual void SetSoftwareVersion(const char* version) = 0;
```
 2.参数

version 用户开发软件版本号，非api发行版本号，长度不超过15位，以'\0'结尾

 3.返回

无

 4.调用示例
```cpp
// 设置软件开发版本号1.1.0，标识的是客户端版本号，而不是API的版本号，由用户自定义
if (user_trade_api_)
{
	user_trade_api_->SetSoftwareVersion("1.1.0");
}
```


### 13. SetSoftwareKey


设置软件开发Key。此函数必须在Login之前调用。

 1.函数原型
```cpp
virtual void SetSoftwareKey(const char* key) = 0;
```
 2.参数

Key:用户开发软件Key，用户申请开户时给予，以'\0'结尾

 3.返回

无

 4.调用示例
```cpp
// 设置软件开发Key
if (user_trade_api_)
{
	user_trade_api_->SetSoftwareKey("xxxxxx");
}
```


### 14. SetHeartBeatInterval


设置心跳检测时间间隔，单位为秒，默认是15s。此函数必须在Login之前调用。

 1.函数原型
```cpp
virtual void SetHeartBeatInterval(uint32_t interval) = 0;
```
 2.参数

Interval：心跳检测时间间隔，单位为秒

 3.返回

无

 4.调用示例
```cpp
// 设定交易服务器超时时间为15秒，用户可自定义
if (user_trade_api_)
{
	user_trade_api_->SetHeartBeatInterval(15);
}
```


### 15. SetMaxOrderBufferQuantity


设置Api内部单个账户的缓存订单总量，默认是1024*200，该缓存非动态增减。 此函数必须在Login之前调用。

 1.函数原型
```cpp
virtual bool SetMaxOrderBufferQuantity(uint32_t max_order_qty) = 0;
```
 2.参数

max_order_qty：当日报单总量的最大值，范围：0~(1024×1024×32-1000)，用户根据实际需要设置单个用户当日报单总量的最大值，若报单总量超过设置的最大值，会导致报单失败；若用户无法确认实际需要设置的值，可设置为较大的值，防止报单失败。

 3.返回

设置是否成功

true表示设置成功，false表示设置失败

 4.调用示例
```cpp
// 设定报单总量的最大值为100000，用户可自定义
if (user_trade_api_)
{
	user_trade_api_->SetMaxOrderBufferQuantity(100000);
}
```

5.注意事项

若已调用该接口成功设置单个用户当日报单总量的最大值，则对后续所有登录的账户都生效；若不同的账户需要设置不同的最大值，则需每次login前调用该接口设定指定的值**。

若调用该接口设置单个用户当日报单总量的最大值成功后，若当日报单总量超过设定值，则TraderApi报xtp_id越界的错误，对应的错误码为10210305，报单时返回的xtp_id为0，此时用户可调用GetApiLastError获取报单失败的错误信息。

调用该接口设置的报单量实际上是账户本次登录期间允许报单的数量，报单总量超过设定值后，必须logout登出后再重新login登录后才可以正常报单，每次logout后再login都会刷新本次登录期间的报单数量。

若用户在OnDisconnected回调中直接调用login接口重新登录，而不是先logout登出后再login登录，则不会刷新本次登录期间允许的报单数量，该账号允许的最大报单数量还是第一次登录前设定的值。


### 16. Login


用户登录请求。此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api可支持多个账户连接，但是同一个账户同一个client_id只能有一个session连接，后面的登录在前一个session存续期间，无法连接。

 1.函数原型
```cpp
virtual uint64_t Login(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;
```
 2.参数

Ip：服务器地址，类似"127.0.0.1"

Port：服务器端口号

User：登录用户名

Password：登录密码

sock_type："1"代表TCP，"2"代表UDP，目前暂时只支持TCP

local_ip：本地网卡地址，类似"127.0.0.1"

```cpp
// XTP_PROTOCOL_TYPE是通讯传输协议方式
typedef enum XTP_PROTOCOL_TYPE
{
	XTP_PROTOCOL_TCP = 1,	///Login(trade_server_ip.c_str(), trade_server_port, account_name.c_str(), account_pw.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str());
}
```


### 17. Logout


登出请求。

 1.函数原型
```cpp
virtual int Logout(uint64_t session_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

 3.返回

登出是否成功，"0"表示登出成功，"-1"表示登出失败

 4.调用示例
```cpp
// 登出请求
if (user_trade_api_)
{
	int ret = user_trade_api_->Logout(session_id);
}
```


### 18. IsServerRestart


服务器是否重启过。此函数必须在Login之后调用。

 1.函数原型
```cpp
virtual bool IsServerRestart(uint64_t session_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

 3.返回

"true"表示重启过，"false"表示没有重启过。

 4.调用示例
```cpp
// 查询服务器是否重启过
if (user_trade_api_)
{
	bool bisr = user_trade_api_->IsServerRestart(session_id);
}
```


### 19. ModifyUserTerminalInfo


修改已登录用户的硬件信息，仅限授权系统使用。

 1.函数原型
```cpp
virtual int ModifyUserTerminalInfo(XTPUserTerminalInfoReq* info,uint64_t session_id) = 0;
```
 2.参数

info：需要修改成的用户硬件信息

session_id：资金账户对应的session_id,登录时得到
```cpp
///申报用户的ip和mac等信息，仅限授权用户使用
struct XTPUserTerminalInfoReq {
	char  local_ip[XTP_INET_ADDRESS_STR_LEN];			///ModifyUserTerminalInfo(&info, session_id);
}
```


### 20. QueryAccountTradeMarket


查询用户在本节点上的可交易市场类型。

 1.函数原型
```cpp
virtual int QueryAccountTradeMarket(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

发送消息是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码

 4.调用示例
```cpp
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryAccountTradeMarket(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryAccountTradeMarket(int trade_location, XTPRI *error_info, int request_id, uint64_t session_id) {};
```


### 21. GetANewOrderXTPID


为用户获取一个新的订单XTPID，用于报单。

此函数必须在Login之后调用，通过这个函数获取的order_xtp_id仅用于对应的用户报单，如果设置错误，将会导致下单失败。

 1.函数原型
```cpp
virtual uint64_t GetANewOrderXTPID(uint64_t session_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

 3.返回

生成的订单XTPID，非“0”表示获取成功，“0”表示获取失败，此时用户可以调用GetApiLastError()来获取错误代码

 4.调用示例
```cpp
if (user_trade_api_)
{
	uint64_t xtp_id = user_trade_api_->GetANewOrderXTPID(session_id);
}
```


### 22. InsertOrder


报单录入请求。

交易所接收订单后，会在报单响应函数OnOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回。

 1.函数原型
```cpp
virtual uint64_t InsertOrder(XTPOrderInsertInfo *order, uint64_t session_id) = 0;
```
 2.参数

order：报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。order.order_xtp_id字段无需用户填写，order.ticker必须不带空格，以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

```cpp
///新订单请求
struct XTPOrderInsertInfo
{
    ///XTP系统订单ID，无需用户填写，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，由客户自定义
    uint32_t	            order_client_id;
    ///合约代码 客户端请求不带空格，以'\0'结尾
    char                    ticker[XTP_TICKER_LEN];
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///价格
    double                  price;
    ///止损价（保留字段）
    double                  stop_price;
    ///数量(股票单位为股，逆回购单位为张)
    int64_t                 quantity;
    ///报单价格
    XTP_PRICE_TYPE          price_type;
    union{
		///32位字段，用来兼容老版本api，用户无需关心
        uint32_t            u32;
        struct {
            ///买卖方向
            XTP_SIDE_TYPE               side;
            ///开平标志
            XTP_POSITION_EFFECT_TYPE    position_effect;
			///预留字段1
            uint8_t                     reserved1;
			///预留字段2
			uint8_t                     reserved2;
        };
    };
	///业务类型
	XTP_BUSINESS_TYPE       business_type;
 };
```
```cpp
///XTP_MARKET_TYPE市场类型，交易里使用
typedef enum XTP_MARKET_TYPE
{
    XTP_MKT_INIT = 0,///InsertOrder(&order, session_id_);
}
```

 5.响应函数
```cpp
// 报单响应
virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};
// 报单成交响应
virtual void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id) {};
```


### 23. InsertOrderExtra


已经提前设置order_xtp_id的报单录入请求，与GetANewOrderXTPID()配合使用。

使用设置好的order_xtp_id（通过GetANewOrderXTPID()获得）进行报单，注意此处如果order_xtp_id设置不对，将导致报单失败。

交易所接收订单后，会在报单响应函数OnOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回。

 1.函数原型
```cpp
virtual uint64_t InsertOrderExtra(XTPOrderInsertInfo *order, uint64_t session_id) = 0;
```
 2.参数

order：报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单，也可以什么都不填。order.order_xtp_id字段必须是通过GetANewOrderXTPID()获得的值，order.ticker必须不带空格，以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

```cpp
///新订单请求
struct XTPOrderInsertInfo
{
    ///XTP系统订单ID，无需用户填写，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，由客户自定义
    uint32_t	            order_client_id;
    ///合约代码 客户端请求不带空格，以'\0'结尾
    char                    ticker[XTP_TICKER_LEN];
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///价格
    double                  price;
    ///止损价（保留字段）
    double                  stop_price;
    ///数量(股票单位为股，逆回购单位为张)
    int64_t                 quantity;
    ///报单价格
    XTP_PRICE_TYPE          price_type;
    union{
		///32位字段，用来兼容老版本api，用户无需关心
        uint32_t            u32;
        struct {
            ///买卖方向
            XTP_SIDE_TYPE               side;
            ///开平标志
            XTP_POSITION_EFFECT_TYPE    position_effect;
			///预留字段1
            uint8_t                     reserved1;
			///预留字段2
			uint8_t                     reserved2;
        };
    };
	///业务类型
	XTP_BUSINESS_TYPE       business_type;
 };
```
```cpp
///XTP_MARKET_TYPE市场类型，交易里使用
typedef enum XTP_MARKET_TYPE
{
    XTP_MKT_INIT = 0,///GetANewOrderXTPID(session_id);

	XTPOrderInsertInfo order;
	memset(&order, 0, sizeof(XTPOrderInsertInfo));

	order.order_xtp_id = new_xtp_id;
	order.market = XTP_MKT_SH_A;
	std::string stdstr_ticker = "600000";
	strncpy(order.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
	order.business_type = XTP_BUSINESS_TYPE_CASH;
	order.side = XTP_SIDE_BUY;
	order.position_effect = XTP_POSITION_EFFECT_INIT;
	order.price_type = XTP_PRICE_LIMIT;
	order.price = 9.01;
	order.quantity = 1000;

	uint64_t order_xtp_id = user_trade_api_->InsertOrderExtra(&order, session_id_);
	if (order_xtp_id == new_xtp_id)
	{
		// 报单发送成功
	}
}
```

 5.响应函数
```cpp
// 报单响应
virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};
// 报单成交响应
virtual void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id) {};
```


### 24. CancelOrder


撤单请求。

如果撤单成功，会在报单响应函数OnOrderEvent()里返回原单部撤或者全撤的消息，如果不成功，会在OnCancelOrderError()响应函数中返回错误原因。

 1.函数原型
```cpp
virtual uint64_t CancelOrder(const uint64_t order_xtp_id, uint64_t session_id) = 0;
```
 2.参数

order_xtp_id：需要撤销的委托单在XTP系统中的ID

session_id：资金账户对应的session_id,登录时得到

 3.返回

撤单在XTP系统中的ID,如果为‘0’表示撤单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非"0"表示撤单发送成功，用户需要记录下返回的order_cancel_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性。

 4.调用示例
```cpp
// 撤单
if (user_trade_api_)
{
	uint64_t ret = user_trade_api_->CancelOrder(order_xtp_id, session_id);
}
```

 5.响应函数
```cpp
// 撤单响应
virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};
// 撤单出错响应
virtual void OnCancelOrderError(XTPOrderCancelInfo *cancel_info, XTPRI *error_info, uint64_t session_id) {};
```


### 25. QueryOrderByXTPID


根据报单ID请求查询报单-旧版本接口。

 1.函数原型
```cpp
virtual int QueryOrderByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
```
 2.参数

order_xtp_id：需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码

 4.调用示例
```cpp
// 根据报单ID请求查询报单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryOrderByXTPID(order_xtp_id, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 26. QueryOrders


请求查询报单-旧版本接口。

该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

 1.函数原型
```cpp
virtual int QueryOrders(const XTPQueryOrderReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///报单查询请求-条件查询
struct XTPQueryOrderReq
{
    ///证券代码，可以为空，如果为空，则默认查询时间段内的所有成交回报
    char      ticker[XTP_TICKER_LEN];
    ///格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点
    int64_t   begin_time;
    ///格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    int64_t   end_time;
};
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询当前交易日0点至当前时间点的所有报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	int ret = user_trade_api_->QueryOrders(&query_param, session_id, request_id);
}
```
```cpp
// 查询600000这支股票在当前交易日0点至当前时间点的全部报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	std::string stdstr_ticker = "600000";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);

	int ret = user_trade_api_->QueryOrders(&query_param, session_id, request_id);
}
```
```cpp
// 查询600000这支股票在22年8月1日0时至15时的全部报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	std::string stdstr_ticker = "600000";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
	query_param.begin_time = 20220801000000000;
	query_param.end_time = 20220801150000000;

	int ret = user_trade_api_->QueryOrders(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 27. QueryUnfinishedOrders


请求查询未完结报单-旧版本接口。

 1.函数原型
```cpp
virtual int QueryUnfinishedOrders(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 请求查询未完结报单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryUnfinishedOrders(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 28. QueryOrdersByPage


分页请求查询报单-旧版本接口。

该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。

 1.函数原型
```cpp
virtual int QueryOrdersByPage(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询订单请求-分页查询
struct XTPQueryOrderByPageReq
{
	///需要查询的订单条数
    int64_t         req_count;
	///上一次收到的查询订单结果中带回来的索引，如果是从头查询，请置0
    int64_t         reference;
	///保留字段
    int64_t         reserved;
};
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 从索引初始开始分页查询1000条报单
if (user_trade_api_)
{
	XTPQueryOrderByPageReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderByPageReq));

	query_param.req_count = 1000;
	query_param.reference = 0;

	int ret = user_trade_api_->QueryOrdersByPage(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOrderByPage(XTPQueryOrderRsp *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};
```


### 29. QueryOrderByXTPIDEx


根据报单ID请求查询报单-新版本接口。

 1.函数原型
```cpp
virtual int QueryOrderByXTPIDEx(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
```
 2.参数

order_xtp_id：需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码

 4.调用示例
```cpp
// 根据报单ID请求查询报单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryOrderByXTPIDEx(order_xtp_id, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOrderEx(XTPOrderInfoEx *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 30. QueryOrdersEx


请求查询报单-新版本接口。

该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

 1.函数原型
```cpp
virtual int QueryOrdersEx(const XTPQueryOrderReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///报单查询请求-条件查询
struct XTPQueryOrderReq
{
    ///证券代码，可以为空，如果为空，则默认查询时间段内的所有成交回报
    char      ticker[XTP_TICKER_LEN];
    ///格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点
    int64_t   begin_time;
    ///格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    int64_t   end_time;
};
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询当前交易日0点至当前时间点的所有报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	int ret = user_trade_api_->QueryOrdersEx(&query_param, session_id, request_id);
}
```
```cpp
// 查询600000这支股票在当前交易日0点至当前时间点的全部报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	std::string stdstr_ticker = "600000";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);

	int ret = user_trade_api_->QueryOrdersEx(&query_param, session_id, request_id);
}
```
```cpp
// 查询600000这支股票在21年8月1日0时至15时的全部报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	std::string stdstr_ticker = "600000";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
	query_param.begin_time = 20210801000000000;
	query_param.end_time = 20210801150000000;

	int ret = user_trade_api_->QueryOrdersEx(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOrderEx(XTPOrderInfoEx *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 31. QueryUnfinishedOrdersEx


请求查询未完结报单-新版本接口。

 1.函数原型
```cpp
virtual int QueryUnfinishedOrdersEx(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 请求查询未完结报单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryUnfinishedOrdersEx(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOrderEx(XTPOrderInfoEx *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 32. QueryOrdersByPageEx


分页请求查询报单-新版本接口。

该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。

 1.函数原型
```cpp
virtual int QueryOrdersByPageEx(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询订单请求-分页查询
struct XTPQueryOrderByPageReq
{
	///需要查询的订单条数
    int64_t         req_count;
	///上一次收到的查询订单结果中带回来的索引，如果是从头查询，请置0
    int64_t         reference;
	///保留字段
    int64_t         reserved;
};
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 从索引初始开始分页查询1000条报单
if (user_trade_api_)
{
	XTPQueryOrderByPageReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderByPageReq));

	query_param.req_count = 1000;
	query_param.reference = 0;

	int ret = user_trade_api_->QueryOrdersByPageEx(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOrderByPageEx(XTPOrderInfoEx *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};
```


### 33. QueryTradesByXTPID


根据委托编号请求查询相关成交。

此函数查询出的结果可能对应多个查询结果响应。

 1.函数原型
```cpp
virtual int QueryTradesByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
```
 2.参数

order_xtp_id：需要查询的委托编号，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 根据委托编号请求查询相关成交
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryTradesByXTPID(order_xtp_id, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryTrade(XTPQueryTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 34. QueryTrades


请求查询已成交。

该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有成交回报，否则查询时间段内所有跟股票代码相关的成交回报，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

 1.函数原型
```cpp
virtual int QueryTrades(XTPQueryTraderReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的成交回报筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询成交回报请求-查询条件
struct XTPQueryTraderReq
{
    ///证券代码，可以为空，如果为空，则默认查询时间段内的所有成交回报
    char      ticker[XTP_TICKER_LEN];
    ///开始时间，格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点
    int64_t   begin_time;
    ///结束时间，格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    int64_t   end_time;
};
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询当前交易日0点至当前时间点的所有成交单
if (user_trade_api_)
{
	XTPQueryTraderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryTraderReq));

	int ret = user_trade_api_->QueryTrades(&query_param, session_id, request_id);
}
```
```cpp
// 查询600000这支股票在当前交易日0点至当前时间点的全部成交单
if (user_trade_api_)
{
	XTPQueryTraderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryTraderReq));

	std::string stdstr_ticker = "600000";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);

	int ret = user_trade_api_->QueryTrades(&query_param, session_id, request_id);
}
```
```cpp
// 查询600000这支股票在21年8月1日0时至15时的全部成交单
if (user_trade_api_)
{
	XTPQueryTraderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryTraderReq));

	std::string stdstr_ticker = "600000";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
	query_param.begin_time = 20210801000000000;
	query_param.end_time = 20210801150000000;

	int ret = user_trade_api_->QueryTrades(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryTrade(XTPQueryTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 35. QueryTradesByPage


分页请求查询成交回报。

该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。

 1.函数原型
```cpp
virtual int QueryTradesByPage(const XTPQueryTraderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要分页查询成交回报的条件，如果第一次查询，那么reference填0

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询成交回报请求-分页查询
struct XTPQueryTraderByPageReq
{
	///需要查询的成交回报条数
	int64_t         req_count;
	///上一次收到的查询成交回报结果中带回来的索引，如果是从头查询，请置0
	int64_t         reference;
	///保留字段
	int64_t         reserved;
};
```

 3.返回

无

 4.调用示例
```cpp
// 从索引初始开始分页查询1000条成交单
if (user_trade_api_)
{
	XTPQueryTraderByPageReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryTraderByPageReq));

	query_param.req_count = 1000;
	query_param.reference = 0;

	int ret = user_trade_api_->QueryTradesByPage(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryTradeByPage(XTPQueryTradeRsp *trade_info, int64_t req_count, int64_t trade_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};
```


### 36. QueryPosition


请求查询投资者持仓。

该方法如果用户提供了合约代码，则会查询此合约的持仓信息，如果合约代码为空，则默认查询所有持仓信息。

 1.函数原型
```cpp
virtual int QueryPosition(const char *ticker, uint64_t session_id, int request_id, XTP_MARKET_TYPE market = XTP_MKT_INIT) = 0;
```
 2.参数

Ticker：需要查询的持仓合约代码，可以为空，如果不为空，请不带空格，并以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

market：需要查询持仓的合约所在市场，默认为0，仅在合约代码不为NULL的时候，才会使用。market不指定或者为非0的其他非有效值情况下，可能由于证券代码沪深2个市场有重复，而导致查询不到所需的持仓。如果想正确查询指定持仓，请指定market

```cpp
///XTP_MARKET_TYPE市场类型，交易里使用
typedef enum XTP_MARKET_TYPE
{
    XTP_MKT_INIT = 0,///QueryPosition("600000", session_id, request_id， XTP_MKT_SH_A);
}
```
```cpp
// 查询全市场持仓
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryPosition(NULL, session_id, request_id, XTP_MKT_INIT);
}
```

 5.响应函数
```cpp
virtual void OnQueryPosition(XTPQueryStkPositionRsp *position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 37. QueryAsset


请求查询资产。

 1.函数原型
```cpp
virtual int QueryAsset(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码

 4.调用示例
```cpp
// 查询资金
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryAsset(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryAsset(XTPQueryAssetRsp *asset, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 38. QueryStructuredFund


请求查询分级基金。此函数查询出的结果可能对应多个查询结果响应。

 1.函数原型
```cpp
virtual int QueryStructuredFund(XTPQueryStructuredFundInfoReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的分级基金筛选条件，其中母基金代码可以为空，则默认所有存在的母基金，如果不为空，请不带空格，并以'\0'结尾，其中交易市场不能为空

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询分级基金信息结构体
struct XTPQueryStructuredFundInfoReq
{
	XTP_EXCHANGE_TYPE   exchange_id;  ///QueryStructuredFund(&query_param, session_id, request_id);
}
```
```cpp
// 母基金代码可为空，查询深证交易所所有母基金的分级基金
if (user_trade_api_)
{
	XTPQueryStructuredFundInfoReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryStructuredFundInfoReq));

	query_param.exchange_id = XTP_EXCHANGE_SZ;

	int ret = user_trade_api_->QueryStructuredFund(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryStructuredFund(XTPStructuredFundInfo *fund_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 39. FundTransfer


资金划拨请求。此函数支持一号两中心节点之间的资金划拨，注意资金划拨的方向。

 1.函数原型
```cpp
virtual uint64_t FundTransfer(XTPFundTransferReq *fund_transfer, uint64_t session_id) = 0;
```
 2.参数

fund_transfer：资金划拨的请求信息

session_id：资金账户对应的session_id,登录时得到

```cpp
///用户资金请求
struct XTPFundTransferReq
{
    ///资金内转编号，无需用户填写，类似于xtp_id
    uint64_t	serial_id;
	///资金账户代码
	char        fund_account[XTP_ACCOUNT_NAME_LEN];
	///资金账户密码
	char	    password[XTP_ACCOUNT_PASSWORD_LEN];
	///金额
	double	    amount;
	///内转类型
	XTP_FUND_TRANSFER_TYPE	transfer_type;

};
```
```cpp
///XTP_FUND_TRANSFER_TYPE是资金流转方向类型
typedef enum XTP_FUND_TRANSFER_TYPE
{
    XTP_FUND_TRANSFER_OUT = 0,		///FundTransfer(&fund_transfer, session_id);
	if (serial_id == 0)
	{
		// 发送失败，获取失败原因
		XTPRI* error_info = m_pTraderApi->GetApiLastError();
		std::cout error_id error_msg QueryFundTransfer(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryFundTransfer(XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 41. QueryOtherServerFund


请求查询其他节点可用资金。

 1.函数原型
```cpp
virtual int QueryOtherServerFund(XTPFundQueryReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：查询时需要提供的信息

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///用户资金查询请求结构体
struct XTPFundQueryReq
{
	///资金账户代码
	char        fund_account[XTP_ACCOUNT_NAME_LEN];
	///资金账户密码
	char	    password[XTP_ACCOUNT_PASSWORD_LEN];
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
	XTP_FUND_QUERY_JZ = 0,		///QueryOtherServerFund(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOtherServerFund(XTPFundQueryRsp *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) {};
```


### 42. QueryETF


请求查询ETF清单文件。

 1.函数原型
```cpp
virtual int QueryETF(XTPQueryETFBaseReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的ETF清单文件的筛选条件，其中合约代码可以为空，则默认所有存在的ETF合约代码，market字段也可以为初始值，则默认所有市场的ETF合约

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询股票ETF合约基本情况--请求结构体,
struct XTPQueryETFBaseReq
{
    ///交易市场
    XTP_MARKET_TYPE    market;
    ///ETF买卖代码
    char               ticker[XTP_TICKER_LEN];
};
```
```cpp
///XTP_MARKET_TYPE市场类型，交易里使用
typedef enum XTP_MARKET_TYPE
{
    XTP_MKT_INIT = 0,///QueryETF(&query_param, session_id, request_id);
}
```
```cpp
// 可以ticker为0,查询全市场
if (user_trade_api_)
{
	XTPQueryETFBaseReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryETFBaseReq));

	int ret = user_trade_api_->QueryETF(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryETF(XTPQueryETFBaseRsp *etf_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 43. QueryETFTickerBasket


请求查询ETF股票篮。

 1.函数原型
```cpp
virtual int QueryETFTickerBasket(XTPQueryETFComponentReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询股票篮的的ETF合约，其中合约代码不可以为空，market字段也必须指定

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询股票ETF合约成分股信息--请求结构体,请求参数为:交易市场+ETF买卖代码
typedef struct XTPQueryETFComponentReq
{
    ///交易市场
    XTP_MARKET_TYPE     market;
    ///ETF买卖代码
    char                ticker[XTP_TICKER_LEN];
}XTPQueryETFComponentReq;
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询沪市某支ETF的成分股信息
if (user_trade_api_)
{
	XTPQueryETFComponentReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryETFComponentReq));

	query_param.market = XTP_MKT_SH_A;
	std::string stdstr_ticker = "xxxxxx";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);

	int ret = user_trade_api_->QueryETFTickerBasket(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryETFBasket(XTPQueryETFComponentRsp *etf_component_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 44. QueryIPOInfoList


请求查询今日新股申购信息列表。

 1.函数原型
```cpp
virtual int QueryIPOInfoList(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询今日新股申购信息列表
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryIPOInfoList(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 45. QueryIPOQuotaInfo


请求查询用户新股申购额度信息。

 1.函数原型
```cpp
virtual int QueryIPOQuotaInfo(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询用户新股申购额度信息
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryIPOQuotaInfo(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryIPOQuotaInfo(XTPQueryIPOQuotaRsp *quota_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 46. QueryBondIPOInfoList


请求查询今日可转债申购信息列表。

1.函数原型
```cpp
virtual int QueryBondIPOInfoList(uint64_t session_id, int request_id) = 0;
```

2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

4.调用示例
```cpp
// 查询用户今日可转债申购信息列表
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryBondIPOInfoList(session_id, request_id);
}
```

5.响应函数
```cpp
virtual void  OnQueryBondIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id)
```


### 47. QueryOptionAuctionInfo


请求查询期权合约。

 1.函数原型
```cpp
virtual int QueryOptionAuctionInfo(XTPQueryOptionAuctionInfoReq *query_param,
uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的期权合约的筛选条件，可以为NULL（为NULL表示查询所有的期权合约）

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询期权竞价交易业务参考信息--请求结构体,请求参数为:交易市场+8位期权代码
struct XTPQueryOptionAuctionInfoReq {
    ///交易市场
    XTP_MARKET_TYPE     market;
    ///8位期权合约代码
    char                ticker[XTP_TICKER_LEN];
};
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询深市90000900这份期权合约详情
if (user_trade_api_)
{
	XTPQueryOptionAuctionInfoReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptionAuctionInfoReq));

	query_param.market = XTP_MKT_SZ_A;
	std::string stdstr_ticker = "90000900";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);

	int ret = user_trade_api_->QueryOptionAuctionInfo(&query_param, session_id, request_id);
}
```
```cpp
// 查询深市所有期权合约详情
if (user_trade_api_)
{
	XTPQueryOptionAuctionInfoReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptionAuctionInfoReq));

	query_param.market = XTP_MKT_SZ_A;

	int ret = user_trade_api_->QueryOptionAuctionInfo(&query_param, session_id, request_id);
}
```
```cpp
// 查询所有期权合约详情
if (user_trade_api_)
{
	XTPQueryOptionAuctionInfoReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptionAuctionInfoReq));

	int ret = user_trade_api_->QueryOptionAuctionInfo(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionAuctionInfo(XTPQueryOptionAuctionInfoRsp *option_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 48. CreditCashRepay


融资融券业务中现金直接还款请求。

 1.函数原型
```cpp
virtual uint64_t CreditCashRepay(double amount, uint64_t session_id) = 0;
```
 2.参数

Amount：现金还款的金额

session_id：资金账户对应的session_id,登录时得到

 3.返回

现金直接还款订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非"0"表示消息发送成功，用户需要记录下返回的xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性。

 4.调用示例
```cpp
// 某信用账户发出10000元现金还款的请求，具体参数需用户自定义
if (user_trade_api_)
{
	uint64_t ret = user_trade_api_->CreditCashRepay(10000, session_id);
}
```

 5.响应函数
```cpp
virtual void OnCreditCashRepay(XTPCrdCashRepayRsp *cash_repay_info, XTPRI *error_info, uint64_t session_id) {};
```


### 49. CreditCashRepayDebtInterestFee


融资融券业务中现金还指定负债合约息费请求。

 1.函数原型
```cpp
virtual uint64_t CreditCashRepayDebtInterestFee(const char* debt_id, double amount, uint64_t session_id) = 0;
```
 2.参数

debt_id：指定的负债合约编号

Amount：现金还息的金额

session_id：资金账户对应的session_id,登录时得到

 3.返回

现金还息订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非"0"表示消息发送成功，用户需要记录下返回的xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性。

 4.调用示例
```cpp
// 某信用账户偿还编号为202111111111110000001这份负债合约息费10000元，具体参数需用户自定义
if (user_trade_api_)
{
	uint64_t ret = user_trade_api_->CreditCashRepayDebtInterestFee("202111111111110000001", 10000, session_id);
}
```

 5.响应函数
```cpp
virtual void OnCreditCashRepayDebtInterestFee(XTPCrdCashRepayDebtInterestFeeRsp *cash_repay_info, XTPRI *error_info, uint64_t session_id) {};
```


### 50. CreditSellStockRepayDebtInterestFee


融资融券业务中卖券还指定负债合约息费请求。

 1.函数原型
```cpp
virtual uint64_t CreditSellStockRepayDebtInterestFee(XTPOrderInsertInfo* order, const char* debt_id, uint64_t session_id) = 0;
```
 2.参数

Order：卖券的报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。order.order_xtp_id字段无需用户填写，order.ticker必须不带空格，以'\0'结尾

debt_id：指定的负债合约编号

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///新订单请求
struct XTPOrderInsertInfo
{
    ///XTP系统订单ID，无需用户填写，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，由客户自定义
    uint32_t	            order_client_id;
    ///合约代码 客户端请求不带空格，以'\0'结尾
    char                    ticker[XTP_TICKER_LEN];
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///价格
    double                  price;
    ///止损价（保留字段）
    double                  stop_price;
    ///数量(股票单位为股，逆回购单位为张)
    int64_t                 quantity;
    ///报单价格
    XTP_PRICE_TYPE          price_type;
    union{
		///32位字段，用来兼容老版本api，用户无需关心
        uint32_t            u32;
        struct {
            ///买卖方向
            XTP_SIDE_TYPE               side;
            ///开平标志
            XTP_POSITION_EFFECT_TYPE    position_effect;
			///预留字段1
            uint8_t                     reserved1;
			///预留字段2
			uint8_t                     reserved2;
        };
    };
	///业务类型
	XTP_BUSINESS_TYPE       business_type;
 };
```

 3.返回

卖券还息订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非"0"表示消息发送成功，用户需要记录下返回的xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性。

 4.调用示例
```cpp
// 某信用账户报单以123.4元卖出深市某股票100份，偿还编号为202111111111110000001的负债合约的息费
if (user_trade_api_)
{
	XTPOrderInsertInfo order;
	memset(&order, 0, sizeof(XTPOrderInsertInfo));

	order.market = XTP_MKT_SZ_A;
	std::string stdstr_ticker = "xxxxxx";
	strncpy(order.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
	order.business_type = XTP_BUSINESS_TYPE_MARGIN;
	order.side = XTP_SIDE_REPAY_MARGIN;
	order.position_effect = XTP_POSITION_EFFECT_INIT;
	order.price_type = XTP_PRICE_LIMIT;
	order.price = 123.40;
	order.quantity = 100;
	std::string str_debt_id = "202111111111110000001";
	uint64_t order_xtp_id = user_trade_api_->CreditSellStockRepayDebtInterestFee(&order, str_debt_id.c_str(), session_id);
}
```

 5.响应函数
```cpp
// 报单完成响应
virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};
// 报单成交响应
virtual void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id) {};
```


### 51. QueryCreditCashRepayInfo


请求查询融资融券业务中的现金直接还款报单。

 1.函数原型
```cpp
virtual int QueryCreditCashRepayInfo(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询融资融券业务中的现金直接还款报单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryCreditCashRepayInfo(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditCashRepayInfo(XTPCrdCashRepayInfo *cash_repay_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 52. QueryCreditFundInfo


请求查询信用账户特有信息，除资金账户以外的信息。

 1.函数原型
```cpp
virtual int QueryCreditFundInfo(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询信用账户特有信息，除资金账户以外的信息
if (user_trade_api_)
{
	int res = user_trade_api_->QueryCreditFundInfo(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditFundInfo(XTPCrdFundInfo *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) {};
```


### 53. QueryCreditDebtInfo


请求查询信用账户负债合约信息。

 1.函数原型
```cpp
virtual int QueryCreditDebtInfo(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询信用账户负债合约信息
if (user_trade_api_)
{
	int res = user_trade_api_->QueryCreditDebtInfo(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditDebtInfo(XTPCrdDebtInfo *debt_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 54. QueryCreditTickerDebtInfo


请求查询指定证券负债未还信息。

 1.函数原型
```cpp
virtual int QueryCreditTickerDebtInfo(XTPClientQueryCrdDebtStockReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的指定证券，筛选条件中ticker可以全填0，如果不为0，请不带空格，并以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///融资融券指定证券上的负债未还数量请求结构体
typedef struct XTPClientQueryCrdDebtStockReq
{
    XTP_MARKET_TYPE market;                 ///QueryCreditTickerDebtInfo(&query_param, session_id, request_id);
}
```
```cpp
// 查询510500的负债未还信息
if (user_trade_api_)
{
	XTPClientQueryCrdDebtStockReq query_param;
	memset(&query_param, 0, sizeof(XTPClientQueryCrdDebtStockReq));

	query_param.market = XTP_MKT_SH_A;
	std::string stdstr_ticker = "510500";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);

	int res = user_trade_api_->QueryCreditTickerDebtInfo(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditTickerDebtInfo(XTPCrdDebtStockInfo *debt_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 55. QueryCreditAssetDebtInfo


请求查询信用账户待还资金信息

 1.函数原型
```cpp
virtual int QueryCreditAssetDebtInfo(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询信用账户待还资金信息
if (user_trade_api_)
{
	int res = user_trade_api_->QueryCreditAssetDebtInfo(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditAssetDebtInfo(double remain_amount, XTPRI *error_info, int request_id, uint64_t session_id) {};
```


### 56. QueryCreditTickerAssignInfo


请求查询信用账户可融券头寸信息。

 1.函数原型
```cpp
virtual int QueryCreditTickerAssignInfo(XTPClientQueryCrdPositionStockReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的指定证券，筛选条件中ticker可以全填0，如果不为0，请不带空格，并以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///融券头寸证券查询请求结构体
typedef struct XTPClientQueryCrdPositionStockReq
{
    XTP_MARKET_TYPE market;                 ///QueryCreditTickerAssignInfo(&query_param, session_id, request_id);
}
```
```cpp
// 查询代码为510500的证券的可融券头寸信息
if (user_trade_api_)
{
	XTPClientQueryCrdPositionStockReq query_param;
	memset(&query_param, 0, sizeof(XTPClientQueryCrdPositionStockReq));

	query_param.market = XTP_MKT_SH_A;
	std::string stdstr_ticker = "510500";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);

	int res = user_trade_api_->QueryCreditTickerAssignInfo(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditTickerAssignInfo(XTPClientQueryCrdPositionStkInfo *assign_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 57. QueryCreditExcessStock


融资融券业务中请求查询指定证券的余券。该方法中用户必须提供了证券代码和所在市场。

 1.函数原型
```cpp
virtual int QueryCreditExcessStock(XTPClientQueryCrdSurplusStkReqInfo *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的余券信息，不可以为空，需要明确指定

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
/// 信用业务余券查询请求结构体
typedef struct XTPClientQueryCrdSurplusStkReqInfo
{
    XTP_MARKET_TYPE market;                 ///QueryCreditExcessStock(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditExcessStock(XTPClientQueryCrdSurplusStkRspInfo* stock_info, XTPRI *error_info, int request_id, uint64_t session_id) {};
```


### 58. QueryMulCreditExcessStock


融资融券业务中请求查询余券。

 1.函数原型
```cpp
virtual int QueryMulCreditExcessStock(XTPClientQueryCrdSurplusStkReqInfo *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的余券信息。若填入市场和股票代码，返回单支股票信息；若市场代码为空，股票代码非空，是无效查询，会在SPI中返回错误；若市场和股票代码均为空，返回全市场信息；若市场代码非空，股票代码为空，返回单市场信息

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
/// 信用业务余券查询请求结构体
typedef struct XTPClientQueryCrdSurplusStkReqInfo
{
    XTP_MARKET_TYPE market;                 ///QueryMulCreditExcessStock(&query_param, session_id, request_id)
}
```
```cpp
// 查询沪市余券信息
if (user_trade_api_)
{
	XTPClientQueryCrdSurplusStkReqInfo query_param;
	memset(&query_param, 0, sizeof(XTPClientQueryCrdSurplusStkReqInfo));

	query_param.market = XTP_MKT_SH_A;

	int res = user_trade_api_->QueryMulCreditExcessStock(&query_param, session_id, request_id)
}
```
```cpp
// 查询全市场余券信息
if (user_trade_api_)
{
	XTPClientQueryCrdSurplusStkReqInfo query_param;
	memset(&query_param, 0, sizeof(XTPClientQueryCrdSurplusStkReqInfo));

	int res = user_trade_api_->QueryMulCreditExcessStock(&query_param, session_id, request_id)
}
```

 5.响应函数
```cpp
virtual void OnQueryMulCreditExcessStock(XTPClientQueryCrdSurplusStkRspInfo* stock_info, XTPRI *error_info, int request_id, uint64_t session_id, bool is_last) {};
```


### 59. CreditExtendDebtDate


融资融券业务中请求负债合约展期。

 1.函数原型
```cpp
virtual uint64_t CreditExtendDebtDate(XTPCreditDebtExtendReq *debt_extend, uint64_t session_id) = 0;
```
 2.参数

debt_extend：负债合约展期的请求信息

session_id：资金账户对应的session_id,登录时得到

```cpp
///用户展期请求
struct XTPCreditDebtExtendReq
{
	uint64_t	xtpid;								///CreditExtendDebtDate(&debt_extend, session_id);
}
```

 5.响应函数
```cpp
virtual void OnCreditExtendDebtDate(XTPCreditDebtExtendNotice *debt_extend_info, XTPRI *error_info, uint64_t session_id) {};
```


### 60. QueryCreditExtendDebtDateOrders


融资融券业务中请求查询负债合约展期。

 1.函数原型
```cpp
virtual int QueryCreditExtendDebtDateOrders(uint64_t xtp_id, uint64_t
session_id, int request_id) = 0;
```
 2.参数

xtp_id：需要查询的负债合约展期订单筛选条件，xtp_id可以为0，则默认所有负债合约展期订单，如果不为0，则请求特定的负债合约展期订单

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询编号为1234567890123456789的负债合约展期订单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryCreditExtendDebtDateOrders(1234567890123456789, session_id, request_id);
}
```
```cpp
// 查询所有负债合约展期订单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryCreditExtendDebtDateOrders(0, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditExtendDebtDateOrders(XTPCreditDebtExtendNotice *debt_extend_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 61. QueryCreditFundExtraInfo


请求查询融资融券业务中账戶的附加信息。

 1.函数原型
```cpp
virtual int QueryCreditFundExtraInfo(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询融资融券业务中账戶的附加信息
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryCreditFundExtraInfo(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditFundExtraInfo(XTPCrdFundExtraInfo *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) {};
```


### 62. QueryCreditPositionExtraInfo


请求查询融资融券业务中账戶指定证券的附加信息。

 1.函数原型
```cpp
virtual int QueryCreditPositionExtraInfo(XTPClientQueryCrdPositionStockReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要指定的证券，筛选条件中ticker可以全填0，如果不为0，请不带空格，并以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///融券头寸证券查询请求结构体
typedef struct XTPClientQueryCrdPositionStockReq
{
    XTP_MARKET_TYPE market;                 ///QueryCreditPositionExtraInfo(&query_param, session_id, request_id);
}
```
```cpp
// 查询证券510500的附加信息
if (user_trade_api_)
{
	XTPClientQueryCrdPositionStockReq query_param;
	memset(&query_param, 0, sizeof(XTPClientQueryCrdPositionStockReq));

	query_param.market = XTP_MKT_SH_A;
	std::string stdstr_ticker = "510500";
	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);

	int res = user_trade_api_->QueryCreditPositionExtraInfo(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryCreditPositionExtraInfo(XTPCrdPositionExtraInfo *fund_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 63. InsertOptionCombinedOrder


期权组合策略报单录入请求。

交易所接收订单后，会在报单响应函数OnOptionCombinedOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回。

 1.函数原型
```cpp
virtual uint64_t InsertOptionCombinedOrder(XTPOptCombOrderInsertInfo *order, uint64_t session_id) = 0;
```
 2.参数

order：报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOptionCombinedOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。order.order_xtp_id字段无需用户填写，order.ticker必须不带空格，以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

```cpp
///期权组合策略新订单请求
struct XTPOptCombOrderInsertInfo
{
    ///XTP系统订单ID，无需用户填写，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，由客户自定义
    uint32_t	            order_client_id;
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///数量(单位为份)
    int64_t                 quantity;

    ///组合方向
    XTP_SIDE_TYPE           side;

    ///业务类型
    XTP_BUSINESS_TYPE       business_type;

    ///期权组合策略信息
    XTPOptCombPlugin        opt_comb_info;
};
```
```cpp
///XTP_MARKET_TYPE市场类型，交易里使用
typedef enum XTP_MARKET_TYPE
{
    XTP_MKT_INIT = 0,///InsertOptionCombinedOrder(&order,session_id);
}
```

 5.响应函数
```cpp
// 报单完成响应
virtual void OnOptionCombinedOrderEvent(XTPOptCombOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};
// 报单成交响应
virtual void OnOptionCombinedTradeEvent(XTPOptCombTradeReport *trade_info, uint64_t session_id) {};
```


### 64. InsertOptionCombinedOrderExtra


已经提前设置order_xtp_id的期权组合策略报单录入请求，与GetANewOrderXTPID()配合使用。

使用设置好的order_xtp_id（通过GetANewOrderXTPID()获得）进行报单，注意此处如果order_xtp_id设置不对，将导致报单失败。交易所接收订单后，会在报单响应函数OnOptionCombinedOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回。

 1.函数原型
```cpp
virtual uint64_t InsertOptionCombinedOrderExtra(XTPOptCombOrderInsertInfo *order, uint64_t session_id) = 0;
```
 2.参数

order：报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOptionCombinedOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单，也可以什么都不填。order.order_xtp_id字段必须是通过GetANewOrderXTPID()获得的值，order.ticker必须不带空格，以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

```cpp
///期权组合策略新订单请求
struct XTPOptCombOrderInsertInfo
{
    ///XTP系统订单ID，无需用户填写，在XTP系统中唯一
    uint64_t                order_xtp_id;
    ///报单引用，由客户自定义
    uint32_t	            order_client_id;
    ///交易市场
    XTP_MARKET_TYPE         market;
    ///数量(单位为份)
    int64_t                 quantity;

    ///组合方向
    XTP_SIDE_TYPE           side;

    ///业务类型
    XTP_BUSINESS_TYPE       business_type;

    ///期权组合策略信息
    XTPOptCombPlugin        opt_comb_info;
};
```
```cpp
///XTP_MARKET_TYPE市场类型，交易里使用
typedef enum XTP_MARKET_TYPE
{
    XTP_MKT_INIT = 0,///GetANewOrderXTPID(session_id);

	// 期权组合策略报单附加信息结构体初始化
	XTPOptCombPlugin plugin_param;
	memset(&plugin_param, 0, sizeof(XTPOptCombPlugin));

	std::string std_str_strategy_id = "CNSJC";
	strncpy(plugin_param.strategy_id, std_str_strategy_id.c_str(), XTP_STRATEGY_ID_LEN);
	// 需要拆分的组合编码
	std::string std_str_comb_num = "xxxxxxxxxx";
	strncpy(plugin_param.comb_num, std_str_comb_num.c_str(), XTP_SECONDARY_ORDER_ID_LEN);

	// 期权组合策略报单结构体初始化
	XTPOptCombOrderInsertInfo order;
	memset(&order, 0, sizeof(XTPOptCombOrderInsertInfo));

	order.order_xtp_id = new_xtp_id;
	order.market = XTP_MKT_SZ_A;
	order.quantity = 100;
	order.business_type = XTP_BUSINESS_TYPE_OPTION_COMBINE;
	order.side = XTP_SIDE_OPT_SPLIT;
	order.opt_comb_info = plugin_param;

	uint64_t ret = user_trade_api_->InsertOptionCombinedOrderExtra(&order,session_id);
	if (ret == new_xtp_id)
	{
		// 组合策略报单发送成功
	}
}
```

 5.响应函数
```cpp
// 报单完成响应
virtual void OnOptionCombinedOrderEvent(XTPOptCombOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};
// 报单成交响应
virtual void OnOptionCombinedTradeEvent(XTPOptCombTradeReport *trade_info, uint64_t session_id) {};
```


### 65. CancelOptionCombinedOrder


期权组合策略报单撤单请求。

如果撤单成功，会在报单响应函数OnOptionCombinedOrderEvent()里返回原单部撤或者全撤的消息，如果不成功，会在OnCancelOrderError()响应函数中返回错误原因。

 1.函数原型
```cpp
virtual uint64_t CancelOptionCombinedOrder(const uint64_t order_xtp_id, uint64_t session_id) = 0;
```
 2.参数

order_xtp_id：需要撤销的期权组合策略委托单在XTP系统中的ID

session_id：资金账户对应的session_id,登录时得到

 3.返回

撤单在XTP系统中的ID,如果为‘0’表示撤单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非"0"表示撤单发送成功，用户需要记录下返回的order_cancel_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性。

 4.调用示例
```cpp
// 期权组合策略报单撤单请求
if (user_trade_api_)
{
	uint64_t ret = user_trade_api_->CancelOptionCombinedOrder(order_xtp_id, session_id);
}
```

 5.响应函数
```cpp
// 撤单完成响应
virtual void OnOptionCombinedOrderEvent(XTPOptCombOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) {};
// 撤单失败响应
virtual void OnCancelOptionCombinedOrderError(XTPOptCombOrderCancelInfo *cancel_info, XTPRI *error_info, uint64_t session_id) {};
```


### 66. QueryOptionCombinedUnfinishedOrders


请求查询期权组合策略未完结报单-旧版本接口。

 1.函数原型
```cpp
virtual int QueryOptionCombinedUnfinishedOrders(uint64_t session_id, int request_id) = 0;
```
 2.参数

order_xtp_id：需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码

 4.调用示例
```cpp
// 查询期权组合策略未完结报单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryOptionCombinedUnfinishedOrders(session_id,request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedOrders(XTPQueryOptCombOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 67. QueryOptionCombinedOrderByXTPID


根据报单ID请求查询期权组合策略报单-旧版本接口。

 1.函数原型
```cpp
virtual int QueryOptionCombinedOrderByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
```
 2.参数

order_xtp_id：需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 根据报单ID请求查询期权组合策略报单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryOptionCombinedOrderByXTPID(order_xtp_id, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedOrders(XTPQueryOptCombOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 68. QueryOptionCombinedOrders


请求查询期权组合策略报单-旧版本接口。

该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

 1.函数原型
```cpp
virtual int QueryOptionCombinedOrders(const XTPQueryOptCombOrderReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///期权组合策略报单查询请求-条件查询
struct XTPQueryOptCombOrderReq
{
    ///组合编码（流水号），可以为空，如果为空，则默认查询时间段内的所有成交回报
    char      comb_num[XTP_SECONDARY_ORDER_ID_LEN];
    ///格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点
    int64_t   begin_time;
    ///格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    int64_t   end_time;
};
```
```cpp
/// 期权组合策略组合编码字符串长度
#define XTP_SECONDARY_ORDER_ID_LEN 18
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询当前交易日0点至当前时间点的所有期权组合策略报单
if (user_trade_api_)
{
	XTPQueryOptCombOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombOrderReq));

	int ret = user_trade_api_->QueryOptionCombinedOrders(&query_param, session_id, request_id);
}
```
```cpp
// 查询某期权组合策略在当前交易日0点至当前时间点的全部报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	std::string comNumStr("xxxxxxxxxxxxxxxx");
	strncpy(query_param.comb_num, comNumStr.c_str(), XTP_SECONDARY_ORDER_ID_LEN);

	int ret = user_trade_api_->QueryOptionCombinedOrders(&query_param, session_id, request_id);
}
```
```cpp
// 查询某期权组合策略在21年8月1日0时至15时的全部报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	std::string comNumStr("xxxxxxxxxxxxxxxx");
	strncpy(query_param.comb_num, comNumStr.c_str(), XTP_SECONDARY_ORDER_ID_LEN);
	query_param.begin_time = 20210801000000000;
	query_param.end_time = 20210801150000000;

	int ret = user_trade_api_->QueryOptionCombinedOrders(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedOrders(XTPQueryOptCombOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 69. QueryOptionCombinedOrdersByPage


分页请求查询期权组合策略报单-旧版本接口。

该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。

 1.函数原型
```cpp
virtual int QueryOptionCombinedOrdersByPage(const XTPQueryOptCombOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询期权组合策略订单请求-分页查询
struct XTPQueryOptCombOrderByPageReq
{
    ///需要查询的订单条数
    int64_t         req_count;
    ///上一次收到的查询订单结果中带回来的索引，如果是从头查询，请置0
    int64_t         reference;
    ///保留字段
    int64_t         reserved;
};
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 从索引初始开始分页查询50条期权组合策略报单
if (user_trade_api_)
{
	XTPQueryOptCombOrderByPageReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombOrderByPageReq));

	query_param.req_count = 50;
	query_param.reference = 0;

	int ret = user_trade_api_->QueryOptionCombinedOrdersByPage(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedOrdersByPage(XTPQueryOptCombOrderRsp *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};
```


### 70. QueryOptionCombinedUnfinishedOrdersEx


请求查询期权组合策略未完结报单-新版本接口。

 1.函数原型
```cpp
virtual int QueryOptionCombinedUnfinishedOrdersEx(uint64_t session_id, int request_id) = 0;
```
 2.参数

order_xtp_id：需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码

 4.调用示例
```cpp
// 查询期权组合策略未完结报单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryOptionCombinedUnfinishedOrders(session_id,request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedOrdersEx(XTPQueryOptCombOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 71. QueryOptionCombinedOrderByXTPIDEx


根据报单ID请求查询期权组合策略报单-新版本接口。

 1.函数原型
```cpp
virtual int QueryOptionCombinedOrderByXTPIDEx(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
```
 2.参数

order_xtp_id：需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 根据报单ID请求查询期权组合策略报单
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryOptionCombinedOrderByXTPIDEx(order_xtp_id, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedOrdersEx(XTPQueryOptCombOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 72. QueryOptionCombinedOrdersEx


请求查询期权组合策略报单-新版本接口。

该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

 1.函数原型
```cpp
virtual int QueryOptionCombinedOrdersEx(const XTPQueryOptCombOrderReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///期权组合策略报单查询请求-条件查询
struct XTPQueryOptCombOrderReq
{
    ///组合编码（流水号），可以为空，如果为空，则默认查询时间段内的所有成交回报
    char      comb_num[XTP_SECONDARY_ORDER_ID_LEN];
    ///格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点
    int64_t   begin_time;
    ///格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    int64_t   end_time;
};
```
```cpp
/// 期权组合策略组合编码字符串长度
#define XTP_SECONDARY_ORDER_ID_LEN 18
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询当前交易日0点至当前时间点的所有期权组合策略报单
if (user_trade_api_)
{
	XTPQueryOptCombOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombOrderReq));

	int ret = user_trade_api_->QueryOptionCombinedOrdersEx(&query_param, session_id, request_id);
}
```
```cpp
// 查询某期权组合策略在当前交易日0点至当前时间点的全部报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	std::string comNumStr("xxxxxxxxxxxxxxxx");
	strncpy(query_param.comb_num, comNumStr.c_str(), XTP_SECONDARY_ORDER_ID_LEN);

	int ret = user_trade_api_->QueryOptionCombinedOrdersEx(&query_param, session_id, request_id);
}
```
```cpp
// 查询某期权组合策略在21年8月1日0时至15时的全部报单
if (user_trade_api_)
{
	XTPQueryOrderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOrderReq));

	std::string comNumStr("xxxxxxxxxxxxxxxx");
	strncpy(query_param.comb_num, comNumStr.c_str(), XTP_SECONDARY_ORDER_ID_LEN);
	query_param.begin_time = 20210801000000000;
	query_param.end_time = 20210801150000000;

	int ret = user_trade_api_->QueryOptionCombinedOrdersEx(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedOrdersEx(XTPOptCombOrderInfoEx *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 73. QueryOptionCombinedOrdersByPageEx


分页请求查询期权组合策略报单-新版本接口。

该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。

 1.函数原型
```cpp
virtual int QueryOptionCombinedOrdersByPageEx(const XTPQueryOptCombOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询期权组合策略订单请求-分页查询
struct XTPQueryOptCombOrderByPageReq
{
    ///需要查询的订单条数
    int64_t         req_count;
    ///上一次收到的查询订单结果中带回来的索引，如果是从头查询，请置0
    int64_t         reference;
    ///保留字段
    int64_t         reserved;
};
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 从索引初始开始分页查询50条期权组合策略报单
if (user_trade_api_)
{
	XTPQueryOptCombOrderByPageReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombOrderByPageReq));

	query_param.req_count = 50;
	query_param.reference = 0;

	int ret = user_trade_api_->QueryOptionCombinedOrdersByPageEx(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedOrdersByPageEx(XTPOptCombOrderInfoEx *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};
```


### 74. QueryOptionCombinedTradesByXTPID


根据期权组合策略委托编号请求查询相关成交。此函数查询出的结果可能对应多个查询结果响应。

 1.函数原型
```cpp
virtual int QueryOptionCombinedTradesByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
```
 2.参数

order_xtp_id：需要查询的委托编号，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 根据期权组合策略委托编号请求查询相关成交
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryOptionCombinedTradesByXTPID(order_xtp_id, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedTrades(XTPQueryOptCombTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 75. QueryOptionCombinedTrades


请求查询期权组合策略的成交回报。

该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有成交回报，否则查询时间段内所有跟股票代码相关的成交回报，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

 1.函数原型
```cpp
virtual int QueryOptionCombinedTrades(const XTPQueryOptCombTraderReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的成交回报筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询期权组合策略成交回报请求-查询条件
struct XTPQueryOptCombTraderReq
{
    ///组合编码（流水号），可以为空，如果为空，则默认查询时间段内的所有成交回报
    char      comb_num[XTP_SECONDARY_ORDER_ID_LEN];
    ///开始时间，格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点
    int64_t   begin_time;
    ///结束时间，格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    int64_t   end_time;
};
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询当前交易日0点至当前时间点的所有成交单
if (user_trade_api_)
{
	XTPQueryOptCombTraderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombTraderReq));

	int ret = user_trade_api_->QueryOptionCombinedTrades(&query_param, session_id, request_id);
}
```
```cpp
// 查询某期权组合策略在当前交易日0点至当前时间点的全部成交单
if (user_trade_api_)
{
	XTPQueryOptCombTraderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombTraderReq));

	std::string comNumStr("xxxxxxxxxxxxxxxx");
	strncpy(query_param.comb_num, comNumStr.c_str(), XTP_SECONDARY_ORDER_ID_LEN);

	int ret = user_trade_api_->QueryOptionCombinedTrades(&query_param, session_id, request_id);
}
```
```cpp
// 查询某期权组合策略在21年8月1日0时至15时的全部成交单
if (user_trade_api_)
{
	XTPQueryOptCombTraderReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombTraderReq));

	std::string comNumStr("xxxxxxxxxxxxxxxx");
	strncpy(query_param.comb_num, comNumStr.c_str(), XTP_SECONDARY_ORDER_ID_LEN);
	query_param.begin_time = 20210801000000000;
	query_param.end_time = 20210801150000000;

	int ret = user_trade_api_->QueryOptionCombinedTrades(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedTrades(XTPQueryOptCombTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 76. QueryOptionCombinedTradesByPage


分页请求查询期权组合策略成交回报。

该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。

 1.函数原型
```cpp
virtual int QueryOptionCombinedTradesByPage(const XTPQueryOptCombTraderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要分页查询订单的条件，如果第一次查询，那么reference填0

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询期权组合策略成交回报请求-分页查询
struct XTPQueryOptCombTraderByPageReq
{
    ///需要查询的成交回报条数
    int64_t         req_count;
    ///上一次收到的查询成交回报结果中带回来的索引，如果是从头查询，请置0
    int64_t         reference;
    ///保留字段
    int64_t         reserved;
};
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 从索引初始开始分页查询50条期权组合策略成交单
if (user_trade_api_)
{
	XTPQueryOptCombTraderByPageReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombTraderByPageReq));

	query_param.req_count = 50;
	query_param.reference = 0;

	int ret = user_trade_api_->QueryOptionCombinedTradesByPage(&query_param,session_id,request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedTradesByPage(XTPQueryOptCombTradeRsp *trade_info, int64_t req_count, int64_t trade_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) {};
```


### 77. QueryOptionCombinedPosition


请求查询投资者期权组合策略持仓。

该方法如果用户提供了合约代码，则会查询此合约的持仓信息（注意请指定market，如果market为0，可能会查询到2个市场的持仓，如果market为其他非有效值，则查询结果会返回找不到持仓），如果合约代码为空，则默认查询所有持仓信息。

 1.函数原型
```cpp
virtual int QueryOptionCombinedPosition(const XTPQueryOptCombPositionReq* query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询持仓的筛选条件，其中组合策略代码可以初始化为空，表示查询所有，如果不为空，请不带空格，并以'\0'结尾，注意需与market匹配，不匹配的话，可能导致查询不到所需的持仓

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询期权组合策略持仓情况请求结构体
struct XTPQueryOptCombPositionReq
{
    ///组合编码
    char comb_num[XTP_SECONDARY_ORDER_ID_LEN];
    ///交易市场
    XTP_MARKET_TYPE     market;
};
```
```cpp
///XTP_MARKET_TYPE市场类型，交易里使用
typedef enum XTP_MARKET_TYPE
{
    XTP_MKT_INIT = 0,///QueryOptionCombinedPosition(&query_param, session_id, request_id);
}
```
```cpp
// 查询全市场所有的期权组合策略持仓信息
if (user_trade_api_)
{
	XTPQueryOptCombPositionReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombPositionReq));

	int ret = user_trade_api_->QueryOptionCombinedPosition(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedPosition(XTPQueryOptCombPositionRsp *position_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 78. QueryOptionCombinedStrategyInfo


请求查询期权组合策略信息。该方法仅支持精确查询，不支持模糊查询。

 1.函数原型
```cpp
virtual int QueryOptionCombinedStrategyInfo(uint64_t session_id, int request_id) = 0;
```
 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询期权组合策略信息
if (user_trade_api_)
{
	int ret = user_trade_api_->QueryOptionCombinedStrategyInfo(session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedStrategyInfo(XTPQueryCombineStrategyInfoRsp *strategy_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 79. QueryOptionCombinedExecPosition


请求查询期权行权合并头寸。该方法可能对应多条响应消息。

 1.函数原型
```cpp
virtual int QueryOptionCombinedExecPosition(const XTPQueryOptCombExecPosReq* query_param, uint64_t session_id, int request_id) = 0;
```
 2.参数

query_param：需要查询的行权合并的筛选条件，其中market为0会默认查询全市场，成分合约代码可以初始化为空，如果不为空，请不带空格，并以'\0'结尾，注意所有填写的条件都会进行匹配

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

```cpp
///查询期权行权合并头寸请求结构体
struct XTPQueryOptCombExecPosReq
{
    ///市场
    XTP_MARKET_TYPE market;
    ///成分合约1代码
    char cntrt_code_1[XTP_TICKER_LEN];
    ///成分合约2代码
    char cntrt_code_2[XTP_TICKER_LEN];
};
```
```cpp
/// 存放证券代码的字符串长度
#define XTP_TICKER_LEN 16
```

 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 查询某期权行权合并头寸
if (user_trade_api_)
{
	XTPQueryOptCombExecPosReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombExecPosReq));

	query_param.market = XTP_MKT_INIT;
	std::string ticker1 = "xxxxxxxx";
	std::string ticker2 = "xxxxxxxx";
	strncpy(query_param.cntrt_code_1, ticker1.c_str(), XTP_TICKER_LEN);
	strncpy(query_param.cntrt_code_1, ticker2.c_str(), XTP_TICKER_LEN);

	int ret = user_trade_api_->QueryOptionCombinedExecPosition(&query_param, session_id, request_id);
}
```
```cpp
// 查询全市场期权行权合并头寸
if (user_trade_api_)
{
	XTPQueryOptCombExecPosReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryOptCombExecPosReq));

	int ret = user_trade_api_->QueryOptionCombinedExecPosition(&query_param, session_id, request_id);
}
```

 5.响应函数
```cpp
virtual void OnQueryOptionCombinedExecPosition(XTPQueryOptCombExecPosRsp *position_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 80. LoginALGO


用户登录algo服务器请求。此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只需调用一次，所有用户共用即可。

 1.函数原型
```cpp
virtual int LoginALGO(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;
```
 2.参数

ip：algo服务器地址，类似"127.0.0.1"

port：algo服务器端口号

user：登录用户名

password：登录密码

sock_type："1"代表TCP，"2"代表UDP，目前暂时只支持TCP

local_ip：本地网卡地址，类似"127.0.0.1"

```cpp
// XTP_PROTOCOL_TYPE是通讯传输协议方式
typedef enum XTP_PROTOCOL_TYPE
{
	XTP_PROTOCOL_TCP = 1,	///LoginALGO(server_ip_algo.c_str(), server_port_algo, account_name_algo.c_str(), account_pw_algo.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str());
    if (login_ret == 0) // 登录algo服务器成功
    {
        std::cout GetApiLastError();
		std::cout error_id error_msg QueryStrategy(0, 0, 0, session_id, request_id);
}
```

 5.响应函数
```cpp
// algo业务中查询策略列表的响应
virtual void OnQueryStrategy(XTPStrategyInfoStruct* strategy_info, char* strategy_param, XTPRI *error_info, int32_t request_id, bool is_last, uint64_t session_id) {};
```


### 82. ALGOUserEstablishChannel


用户请求使用algo服务器建立算法通道。此函数为异步方式，一个用户只能拥有一个算法通道，如果之前已经建立，则无需重复建立，在使用算法前，请先建立算法通道。

 1.函数原型
```cpp
virtual int ALGOUserEstablishChannel(const char* oms_ip, int oms_port, const char* user, const char* password, uint64_t session_id) = 0;
```
 2.参数

oms_ip：oms服务器地址，类似"127.0.0.1"，非algo服务器地址

oms_port：oms服务器端口号

user：登录用户名

password：登录密码

session_id：资金账户对应的session_id,登录时得到

 3.返回

表明此资金账号建立算法通道请求消息发送是否成功，非“0”表示发送失败，可以调用GetApiLastError()来获取错误代码，“0”表示发送成功

 4.调用示例
```cpp
// 请求使用algo服务器建立算法通道，参数服务器地址端口用户名密码等需用户自定义
if (user_trade_api_)
{
    ///在用户成功登录交易服务器后，算法用户建立算法通道
    if (session_id_ != 0)
    {
        std::string oms_server_ip = "xxx.xxx.xxx.xxx";
        int oms_server_port = xxxx;
        std::string account_name_oms = "xxxxxxxx";
        std::string account_pw_oms = "xxxxxx";

        int ret = user_trade_api_->ALGOUserEstablishChannel(oms_server_ip.c_str(), oms_server_port, account_name_oms.c_str(), account_pw_oms.c_str(), session_id_);
        if (ret == 0) // 建立算法通道请求消息，发送成功
		{
			std::cout GetApiLastError();
			std::cout error_id error_msg InsertAlgoOrder(strategy_type, client_strategy_id, (char*)strategy_param.c_str(), session_id);
	if (ret == 0)  // 发送算法单成功
	{
		std::cout GetApiLastError();
		std::cout error_id error_msg CancelAlgoOrder(false, xtp_strategy_id, session_id);
}
```

 5.响应函数
```cpp
// algo业务中撤销策略单的响应
virtual void OnCancelAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPRI *error_info, uint64_t session_id) {};
```


### 85. GetAlgorithmIDByOrder


获取算法单的母单ID。

 1.函数原型
```cpp
virtual uint64_t GetAlgorithmIDByOrder(uint64_t order_xtp_id, uint32_t order_client_id) = 0;
```
 2.参数

order_xtp_id：算法单对应的xtp id

order_client_id：算法单对应的自定义ID，不可随意填写

 3.返回

返回算法单的母单ID，如果返回为0表示不是算法单

 4.调用示例
```cpp
// 根据报单ID请求查询报单
if (user_trade_api_)
{
    uint32_t order_client_id = xxx;

	uint64_t ret = user_trade_api_->GetAlgorithmIDByOrder(order_xtp_id, order_client_id);
    // ret不为0即为算法母单ID
}
```


### 86. StrategyRecommendation


algo业务中请求推荐算法。

 1.函数原型
```cpp
virtual int StrategyRecommendation(bool basket_flag, char* basket_param, uint64_t session_id, int32_t request_id) = 0;
```
 2.参数

basket_flag：是否将满足条件的推荐结果打包成母单篮的标志，true-打包

basket_param：需要算法推荐的证券列表，为json字串，具体格式参考说明文档或咨询运营人员

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

 3.返回

请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码

 4.调用示例
```cpp
// 请求推荐算法
if (user_trade_api_)
{
    bool basket_flag = true; //需要打包成母单篮
	std::string basket_param = "xxxx";//需要算法推荐的证券列表，为json字串

	int ret = user_trade_api_->StrategyRecommendation(basket_flag, (char*)basket_param.c_str(), session_id, request_id);

    if (ret == 0)  // 请求发送成功
	{
		std::cout GetApiLastError();
		std::cout error_id error_msg QueryBondSwapStockInfo(&query_param, session_id, request_id);
}
```
```cpp
// 查询所有的可转债转股信息
if (user_trade_api_)
{
	XTPQueryBondSwapStockReq query_param;
	memset(&query_param, 0, sizeof(XTPQueryBondSwapStockReq));

	int ret = user_trade_api_->QueryBondSwapStockInfo(&query_param, session_id, request_id);
}
```

 5.响应函数

```cpp
virtual void OnQueryBondSwapStockInfo(XTPQueryBondSwapStockRsp *swap_stock_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};
```


### 88. ModifyAlgoOrder


algo业务中修改已有的算法单。

 1.函数原型
```cpp
virtual int ModifyAlgoOrder(uint64_t xtp_strategy_id, char* strategy_param, uint64_t session_id) = 0;
```

 2.参数

xtp_strategy_id：xtp算法单策略ID
strategy_param：修改后的策略参数
session_id：资金账户对应的session_id,登录时得到

 3.返回

算法单修改请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

 4.调用示例
```cpp
// 修改已有的算法单，参数需要用户自定义
if (user_trade_api_)
{
	uint64_t xtp_strategy_id = xxx;
	std::string strategy_param = "xxxx";

	int ret = user_trade_api_->ModifyAlgoOrder(xtp_strategy_id, (char*)strategy_param.c_str(), session_id);
	if (ret == 0)  // 发送算法单修改请求成功
	{
		std::cout GetApiLastError();
		std::cout error_id error_msg PauseAlgoOrder(xtp_strategy_id, &ticker_info, session_id, request_id);
	if (ret == 0)  // 发送暂停算法母单请求成功
	{
		std::cout GetApiLastError();
		std::cout error_id error_msg ResumeAlgoOrder(xtp_strategy_id, &ticker_info, session_id, request_id);
	if (ret == 0)  // 发送重启算法母单请求成功
	{
		std::cout GetApiLastError();
		std::cout error_id error_msg << std::endl;
	}
}
```

◇ 5.响应函数

```cpp
virtual void OnResumeAlgoOrder(uint64_t xtp_strategy_id, XTPStrategyTickerInfo* ticker_info, XTPRI *error_info, int32_t request_id, uint64_t session_id) {};
```
