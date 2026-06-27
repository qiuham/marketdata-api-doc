---
api_type: reference
source_type: vitepress
version: XTP Pro
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
provider_name: 中泰证券
product: xtppro
product_id: zhongtai-xtppro
id: zhongtai-xtppro-xtp-pro-api接口说明
title: XTP-Pro API接口说明
source_url: 'https://xtp.zts.com.cn/xtp-pro/API4/API%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E%E4%B8%8E%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81.html'
page_url: 'https://xtp.zts.com.cn/xtp-pro/'
updated_at: 2026-06-23
---

# XTP-Pro API接口说明

**XTP-Pro API接口说明**

目录

  * **1\. 介绍**
    * 1.1. 接口文件列表
  * **2\. 文档版本和重要更新**
    * 2.1. 版本
    * 2.2. 更新历史
  * **3\. 运行环境**
  * **4\. 行情接口**
    * 4.1. 行情接口简介
      * 4.1.1. 说明
      * 4.1.2. 代码示例
    * 4.2. QuoteApi
      * 4.2.1. 接口
      * 4.2.2. 示例代码
      * 4.2.3. CreateQuoteApi
      * 4.2.4. Release
      * 4.2.5. GetApiVersion
      * 4.2.6. GetApiLastError
      * 4.2.7. RegisterSpi
      * 4.2.8. SetHeartBeatInterval
      * 4.2.9. SetConfigFile
      * 4.2.10. SetUDPThreadAffinityArray
      * 4.2.11. SubscribeMarketData
      * 4.2.12. UnSubscribeMarketData
      * 4.2.13. SubscribeOrderBook
      * 4.2.14. UnSubscribeOrderBook
      * 4.2.15. SubscribeTickByTick
      * 4.2.16. UnSubscribeTickByTick
      * 4.2.17. SubscribeAllMarketData
      * 4.2.18. UnSubscribeAllMarketData
      * 4.2.19. SubscribeAllOrderBook
      * 4.2.20. UnSubscribeAllOrderBook
      * 4.2.21. SubscribeAllTickByTick
      * 4.2.22. UnSubscribeAllTickByTick
      * 4.2.23. Login
      * 4.2.24. Logout
      * 4.2.25. QueryAllTickers
      * 4.2.26. QueryTickersPriceInfo
      * 4.2.27. QueryAllTickersPriceInfo
      * 4.2.28. SubscribeAllOptionMarketData
      * 4.2.29. UnSubscribeAllOptionMarketData
      * 4.2.30. QueryAllTickersFullInfo
      * 4.2.31. QueryAllNQTickersFullInfo
      * 4.2.32. QueryTickersLatestMarketData
      * 4.2.33. SubscribeAllIndexPress
      * 4.2.34. UnSubscribeAllIndexPress
      * 4.2.35. SubscribeAllHKCMarketData
      * 4.2.36. UnSubscribeAllHKCMarketData
      * 4.2.37. RequestRebuildQuote
      * 4.2.38. QueryAllHKCInfo
      * 4.2.39. QueryAllIndexPressInfo
    * 4.3. QuoteSpi
      * 4.3.1. 接口
      * 4.3.2. 示例代码
      * 4.3.3. OnDisconnected
      * 4.3.4. OnError
      * 4.3.5. OnSubMarketData
      * 4.3.6. OnUnSubMarketData
      * 4.3.7. OnDepthMarketData
      * 4.3.8. OnSubOrderBook
      * 4.3.9. OnUnSubOrderBook
      * 4.3.10. OnOrderBook
      * 4.3.11. OnSubTickByTick
      * 4.3.12. OnUnSubTickByTick
      * 4.3.13. OnTickByTick
      * 4.3.14. OnSubscribeAllMarketData
      * 4.3.15. OnUnSubscribeAllMarketData
      * 4.3.16. OnSubscribeAllOrderBook
      * 4.3.17. OnUnSubscribeAllOrderBook
      * 4.3.18. OnSubscribeAllTickByTick
      * 4.3.19. OnUnSubscribeAllTickByTick
      * 4.3.20. OnQueryAllTickers
      * 4.3.21. OnQueryTickersPriceInfo
      * 4.3.22. OnSubscribeAllOptionMarketData
      * 4.3.23. OnUnSubscribeAllOptionMarketData
      * 4.3.24. OnQueryAllTickersFullInfo
      * 4.3.25. OnRequestRebuildQuote
      * 4.3.26. OnRebuildTickByTick
      * 4.3.27. OnRebuildMarketData
      * 4.3.28. OnQueryAllNQTickersFullInfo
      * 4.3.29. OnETFIOPVData
      * 4.3.30. OnXTPQuoteNQFullInfo
      * 4.3.31. OnQueryTickersLatestMarketData
      * 4.3.32. OnSubscribeAllIndexPress
      * 4.3.33. OnUnSubscribeAllIndexPress
      * 4.3.34. OnIndexPress
      * 4.3.35. OnSubscribeAllHKCMarketData
      * 4.3.36. OnUnSubscribeAllHKCMarketData
      * 4.3.37. OnHKRLData
      * 4.3.38. OnHKCMarketData
      * 4.3.39. OnQueryAllHKCInfo
      * 4.3.40. OnQueryAllIndexPressInfo
  * **5\. 交易接口**
    * 5.1. 交易接口简介
      * 5.1.1. 说明
      * 5.1.2. 代码示例
    * 5.2. TraderApi
      * 5.2.1. 接口
      * 5.2.2. 示例代码
      * 5.2.3. CreateTraderApi
      * 5.2.4. Release
      * 5.2.5. GetTradingDay
      * 5.2.6. RegisterSpi
      * 5.2.7. GetApiLastError
      * 5.2.8. GetApiVersion
      * 5.2.9. GetClientIDByXTPID
      * 5.2.10. GetAccountByXTPID
      * 5.2.11. SubscribePublicTopic
      * 5.2.12. SetSoftwareVersion
      * 5.2.13. SetSoftwareKey
      * 5.2.14. SetHeartBeatInterval
      * 5.2.15. Login
      * 5.2.16. Logout
      * 5.2.17. GetAccountTradeMarket
      * 5.2.18. GetANewOrderXTPID
      * 5.2.19. GetMaxReqNumOfPagedQuery
      * 5.2.20. InsertOrder
      * 5.2.21. InsertOrderExtra
      * 5.2.22. CancelOrder
      * 5.2.23. QueryOrderByXTPID
      * 5.2.24. QueryOrders
      * 5.2.25. QueryUnfinishedOrders
      * 5.2.26. QueryOrdersByPage
      * 5.2.27. QueryTradesByXTPID
      * 5.2.28. QueryTrades
      * 5.2.29. QueryTradesByPage
      * 5.2.30. QueryPosition
      * 5.2.31. QueryAllPosition
      * 5.2.32. QuerySecurityAccount
      * 5.2.33. QueryAsset
      * 5.2.34. FundTransfer
      * 5.2.35. QueryFundTransferByID
      * 5.2.36. QueryFundTransferByPage
      * 5.2.37. QueryOtherServerFund
      * 5.2.38. QueryETF
      * 5.2.39. QueryETFTickerBasket
      * 5.2.40. QueryIPOInfoList
      * 5.2.41. QueryIPOQuotaInfo
      * 5.2.42. QueryBondIPOInfoList
      * 5.2.43. QueryBondSwapStockInfo
    * 5.3. TraderSpi
      * 5.3.1. 接口
      * 5.3.2. 代码示例
      * 5.3.3. OnDisconnected
      * 5.3.4. OnServerStatusNotification
      * 5.3.5. OnError
      * 5.3.6. OnConnect
      * 5.3.7. OnResumeEnd
      * 5.3.8. OnUnknownOrder
      * 5.3.9. OnOrderAck
      * 5.3.10. OnOrderEvent
      * 5.3.11. OnTradeEvent
      * 5.3.12. OnCancelOrderError
      * 5.3.13. OnQueryOrder
      * 5.3.14. OnQueryOrderByPage
      * 5.3.15. OnQueryTrade
      * 5.3.16. OnQueryTradeByPage
      * 5.3.17. OnQueryPosition
      * 5.3.18. OnQuerySecurityAccount
      * 5.3.19. OnQueryAsset
      * 5.3.20. OnQueryFundTransfer
      * 5.3.21. OnQueryFundTransferByPage
      * 5.3.22. OnFundTransfer
      * 5.3.23. OnUnknownFundTransfer
      * 5.3.24. OnQueryOtherServerFund
      * 5.3.25. OnQueryETF
      * 5.3.26. OnQueryETFBasket
      * 5.3.27. OnQueryIPOInfoList
      * 5.3.28. OnQueryIPOQuotaInfo
      * 5.3.29. OnQueryBondIPOInfoList
      * 5.3.30. OnQueryBondSwapStockInfo



  
  


## **1\. 介绍** ​

本接口说明旨在帮助开发者快速查阅极速交易平台API（XTP-Pro API）的使用方法、参数说明及注意事项。文中汇集了API使用过程中常见的问题、重要参数说明及接口调用示例。

  


### 1.1. 接口文件列表 ​

C++头文件：

文件名| 详情  
---|---  
`xtpx_trader_api.h`| 定义客户端交易接口  
`xtpx_api_struct_common.h`| 定义业务公共数据结构  
`xoms_x_api_struct.h`| 定义交易类相关数据结构  
`xtpx_api_data_type.h`| 定义兼容数据基本类型  
`xgw_x_api_fund_struct.h`| 定义资金划拨相关结构体类型  
`xgw_x_api_query_struct.h`| 定义交易类查询相关数据结构  
`xtrade_x_api_data_type.h`| 定义交易使用的数据基本类型  
`xtpx_quote_api.h`| 定义行情订阅客户端接口  
`xquote_x_api_struct.h`| 定义行情使用的数据基本类型  
`xquote_x_api_rebuild_tbt_struct.h`| 定义行情回补相关数据结构  
`xquote_x_api_data_type.h`| 定义行情使用的数据基本类型  
  


交易部分的动态链接库：

  
适用系统| 文件名  
---|---  
windows| `xtpxtraderapi.dll xtpxtraderapi.lib`  
linux| `libxtpxtraderapi.so`  
  


行情部分的动态链接库：

  
适用系统| 文件名  
---|---  
windows| `xtpxquoteapi.dll xtpxquoteapi.lib`  
linux| `libxtpxquoteapi.so`  
  
  
  


## **2\. 文档版本和重要更新** ​

本文档介绍的是XTP-Pro版本的API接口说明与示例代码，XTP-Pro与XTP版本的区别，请参阅文档《从XTP行情到XTP-Pro行情API的变化》和《从XTP交易到XTP-Pro交易API的变化》。

  


### 2.1. 版本 ​

V1.2.1

### 2.2. 更新历史 ​

version 1.2.1

(1) 港股通HKC和指数通IndexPress与快照MD配置合并，不再单独配置

(2) 配置文件中新增busy_wait配置项，所有接收线程均可单独配置，此选项默认开启

(3) 逐笔委托XTPTickByTickEntrust结构体中增加已成交的委托数量字段traded_qty

(4) 修改异步日志输出格式

(5) 修复bug   


version 1.2.0

(1) 行情API增加查询港股通的静态信息

(2) 行情API增加查询指数通的静态信息   


version 1.1.0

(1) 交易API增加流控控制和风控的红绿灯机制

(2) 交易API的交易连接和查询连接做绑定分离，使得查询连接断连不再导致交易连接断连

(3) 行情API查询里支持REITs基金分类

(4) 行情API支持OB行情解析

(5) 修改bug   


version 1.0.15

(1) 修改bug

(2) 修改部分日志级别

(3) 新增行情解析线程和接收线程绑核接口SetUDPThreadAffinityArray   


version 1.0.14

(1) 修改bug

  
  


## **3\. 运行环境** ​

Linux操作系统推荐版本为RedHat7、Centos7、Ubuntu16.04及以上。

Windows为windows10及以上的操作系统，支持64位。

  
  


## **4\. 行情接口** ​

### 4.1. 行情接口简介 ​

#### 4.1.1. 说明 ​

行情API提供了两个接口，分别为QuoteApi和QuoteSpi。客户端应用程序可以通过QuoteApi发出操作请求，通过继承QuoteSpi并重写回调函数来处理后台服务的响应。

  


#### 4.1.2. 代码示例 ​

◇ 1.源代码

下面是一个简单的代码示例，该示例演示了API的初始化、连接前置、登录行情系统和订阅行情的过程。

以下是MyQuoteSpi.h文件

cpp
    
    
    #include "xtpx_quote_api.h"
    
    class MyQuoteSpi : public XTPX::API::QuoteSpi
    {
    public:
        explicit MyQuoteSpi();
        ~MyQuoteSpi();
    
        //接收行情
        void OnDepthMarketData(XTPX::API::XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count);
    };

以下是MyQuoteSpi.cpp文件

cpp
    
    
    #include "MyQuoteSpi.h"
    #include <iostream>
    
    using namespace XTPX::API;
    
    MyQuoteSpi::MyQuoteSpi() { }
    MyQuoteSpi::~MyQuoteSpi() { }
    
    //接收行情
    void MyQuoteSpi::OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count)
    {
    	std::cout << "OnDepthMarketData." << std::endl;
    }

以下是MyQuoteApi.h文件

cpp
    
    
    #include "xtpx_quote_api.h"
    #include "MyQuoteSpi.h"
    
    class MyQuoteApi
    {
    public: 
    	explicit MyQuoteApi();
    	~MyQuoteApi();
    
    	// 初始化
        bool initialize();
        // 登录 
        int login();
        // 订阅行情 
        void subscribeMarketData();
    	// 释放
    	void release();
    
    private: 
        XTPX::API::QuoteApi* user_quote_api_;
    	MyQuoteSpi* m_quote_spi;
    };

以下是MyQuoteApi.cpp文件

cpp
    
    
    #include "MyQuoteApi.h"
    #include <iostream>
    #include <string>
    
    using namespace XTPX::API;
    
    MyQuoteApi::MyQuoteApi() 
    {
    	user_quote_api_ = NULL;
    	m_quote_spi = NULL;
    }
    
    MyQuoteApi::~MyQuoteApi() 
    { 
    	if (user_quote_api_ != NULL) {
            user_quote_api_->Logout();
        }
    }
    
    // 创建并初始化行情API
    bool MyQuoteApi::initialize()
    { 
    	user_quote_api_ = QuoteApi::CreateQuoteApi(1, "./", XTP_LOG_LEVEL_DEBUG, true);//第四个参数控制异步日志输出的
    	if (user_quote_api_) 
    	{
    		// 注册行情回调接口
    		m_quote_spi = new MyQuoteSpi();
    		user_quote_api_->RegisterSpi(m_quote_spi);
    		user_quote_api_->SetHeartBeatInterval(15);
            user_quote_api_->SetConfigFile("D:/quote_config.ini");//设置行情接收的配置文件
    		return true; 
    	}
    	return false;
    } 
    // 登录，用户请自行修改参数
    int MyQuoteApi::login() 
    { 
    	std::string quote_server_ip = "xxx.xxx.xxx.xxx";
    	int quote_server_port = xxxx;
    	std::string quote_username = "xxxxxxxx";
    	std::string quote_password = "xxxxxx";
    	std::string local_ip = "xxx.xxx.xxx.xxx";
    
    	int ret = user_quote_api_->Login(quote_server_ip.c_str(), quote_server_port, quote_username.c_str(), quote_password.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str()); 
    	if (0 == ret) 
    	{
    		// 登录成功
    	} 
    	else  
    	{ 
    		// 登录失败，并获取错误信息
    		XTPRI* error_info = user_quote_api_->GetApiLastError();
    		std::cout << "login to server error, " << error_info->error_id << " : " << error_info->error_msg << std::endl; 
    	}
    	return ret;
    }   
    // 订阅行情 
    void MyQuoteApi::subscribeMarketData()
    {
    	// 申请内存
    	int ticker_count = 2;//需要订阅行情的证券代码数量，可根据实际订阅需求改动
    	char **ppInstrumentID = new char*[ticker_count];
    	for (int i = 0; i < ticker_count; i++) 
    	{
    		ppInstrumentID[i] = new char[XTP_QUOTE_TICKER_LEN]; 
    	}
    	strcpy_s(ppInstrumentID[0], XTP_QUOTE_TICKER_LEN, "600000");
    	strcpy_s(ppInstrumentID[1], XTP_QUOTE_TICKER_LEN, "600001");
    	//订阅沪市的600000、600001两只股票快照行情 
    	user_quote_api_->SubscribeMarketData(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);
    	
    	// 释放内存
    	for (int i = 0; i < ticker_count; i++) {
    		delete[] ppInstrumentID[i];
    		ppInstrumentID[i] = NULL;
    	}
    	delete[] ppInstrumentID;
    	ppInstrumentID = NULL;
    }
    // 释放
    void MyQuoteApi::release()
    {
    	if (user_quote_api_ != NULL) {
            user_quote_api_->Logout();
        }
    }

以下是main.cpp文件

cpp
    
    
    #include "MyQuoteApi.h"
    #ifdef _WIN32
    	#include <windows.h>
    #else
    	#include <unistd.h>
    #endif
    
    int main(int argc, char* argv[])
    {
        MyQuoteApi *pQuoteApi = new MyQuoteApi;
    
    	if (pQuoteApi)
    	{
    		bool b_ret = pQuoteApi->initialize();
    		if (! b_ret)
    		{
    			// 初始化失败程序退出
    			return -1;
    		}
    		int ret = pQuoteApi->login();
    		if (0 == ret)
    		{
    			pQuoteApi->subscribeMarketData();
    		}
    		//主线程循环，防止进程退出
    		while (true)
    		{
    #ifdef _WIN32
    			Sleep(1000);
    #else
    			sleep(1);
    #endif // WIN32
    		}
    	}
    
    	return 0;
    }

◇ 2.代码说明

◇ 2.1. 继承QuoteSpi类

代码一开始通过#include "xtpx_quote_api.h"，将xtpxquoteapi.lib中声明的类和数据类型包括进来，该头文件中有两个重要的基类：QuoteSpi和QuoteApi。

QuoteSpi类提供了行情相关的回调接口，用户需要继承该类并重写这些接口，以获取响应数据。

QuoteApi类则提供了行情相关的请求接口，例如订阅快照行情请求、订阅逐笔行情请求、订阅订单簿行情请求。

我们声明了一个MyQuoteSpi类，该类继承了QuoteSpi类，并且重写了OnSubMarketData和OnDepthMarketData等回调接口。当我们发起订阅行情SubscribeMarketData请求成功后，便会触发OnSubMarketData响应。之后行情系统会通过OnDepthMarketData实时推送行情。

我们声明了一个QuoteApi类型的变量user_quote_api_，创建实例后便可以调用QuoteApi提供的登录，订阅行情等接口功能。

◇ 2.2.初始化

initialize()函数里，创建Api实例（QuoteApi）并为其注册对应的回调接口类的实例（RegisterSpi）。参数"./"指明程序日志文件存放的目录为程序同级目录。

继承Spi类的MyQuoteSpi注册给QuoteApi，这样API就能将收到的各种数据通过Spi类的接口回调给用户。

完成以上步骤后，客户端和XTP行情建立连接后，就可以调用各种API接口完成业务需求。

◇ 2.3.登录

QuoteSpi成功注册后能够开始登录行情系统了，调用QuoteApi登录接口login，赋值相应字段即可。通过返回值可以判断是否登录成功，0表示成功，其他则表示失败。可以在Login失败后调用GetApiLastError函数，获取失败的原因。Login函数为同步阻塞函数，无需异步等待。

◇ 2.4.订阅行情

调用订阅行情的接口SubscribeMarketData，我们这里订阅了合约"600000"。若需要批量订阅多个合约，则需要循环把合约输入到ppInstrumentID中去，同时别忘了更改合约数量（第二个参数）。

注意这里返回0不表示登录成功，而是仅仅表示api指令发出去了。该规则同样适用于其他请求接口，建议在实际应用中做好超时重发机制，以便在网络丢包的情况下能够及时重发指令。

订阅请求发出后，通过OnSubMarketData响应判断是否订阅成功。

通过OnDepthMarketData回调推送实时行情信息。可以在此实现自身业务逻辑。

但是如果业务逻辑比较耗时，应该在另外一个线程处理，而不应该卡在此回调里，否则会导致后续的行情堵塞在API内部，严重情况下会导致断线。

◇ 2.5.程序运行流程

主函数是业务实现主体。首先初始化MyQuoteApi类。调用initialize函数开始连接XTP行情，依次执行登录和订阅行情操作。

### 4.2. QuoteApi ​

QuoteApi类提供了行情api的初始化、登录、订阅等功能。

#### 4.2.1. 接口 ​

cpp
    
    
    namespace XTPX {
    	namespace API {
    		class MD_API_EXPORT QuoteApi
    		{
    		public:
    			///创建QuoteApi
    			///@param client_id （必须输入）用于区分同一用户的不同客户端，由用户自定义
    			///@param save_file_path （必须输入）存贮订阅信息文件的目录，请设定一个有可写权限的真实存在的路径，如果路径不存在的话，可能会因为写冲突而造成断线
    			///@param log_level 日志输出级别
    			///@param udpseq_output udpseq异步日志是否输出标识，默认为true，如果不想输出异步日志，请设置此参数为false
    			///@return 创建出的UserApi
    			///@remark 如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，但是对于同一账户，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接
    			static QuoteApi *CreateQuoteApi(uint8_t client_id, const char *save_file_path, XTP_LOG_LEVEL log_level=XTP_LOG_LEVEL_DEBUG, bool udpseq_output = true);
    
    			///删除接口对象本身
    			///@remark 不再使用本接口对象时,调用该函数删除接口对象
    			virtual void Release() = 0;
    
    
    			///获取API的发行版本号
    			///@return 返回api发行版本号
    			virtual const char* GetApiVersion() = 0;
    
    			///获取API的系统错误
    			///@return 返回的错误信息，可以在Login、Logout、订阅、取消订阅失败时调用，获取失败的原因
    			///@remark 可以在调用api接口失败时调用，例如login失败时
    			virtual XTPRI *GetApiLastError() = 0;
    
    			///注册回调接口
    			///@param spi 派生自回调接口类的实例，请在登录之前设定
    			virtual void RegisterSpi(QuoteSpi *spi) = 0;
    
    			///设置心跳检测时间间隔，单位为秒
    			///@param interval 心跳检测时间间隔，单位为秒
    			///@remark 此函数必须在Login之前调用
    			virtual void SetHeartBeatInterval(uint32_t interval) = 0;
    
    
    			///设置行情接收的配置文件
    			///@return 设置配置文件是否成功，true-成功，false-失败，需要检查配置文件是否正确
    			///@param filename 包含绝对路径的配置文件名
    			///@remark 此函数必须在Login之前调用，如果不调用，将无法获取行情
    			virtual bool SetConfigFile(const char* filename) = 0;
    
    			///订阅行情，包括股票、指数、期权、债券等。
    			///@return 订阅接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格 
    			///@param count 要订阅/退订行情的合约个数
    			///@param exchange_id 交易所代码
    			///@remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情
    			virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///退订行情，包括股票、指数、期权、债券等。
    			///@return 取消订阅接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格  
    			///@param count 要订阅/退订行情的合约个数
    			///@param exchange_id 交易所代码
    			///@remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅行情接口配套使用
    			virtual int UnSubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///订阅行情订单簿，包括股票、债券等。（新三板暂不支持）
    			///@return 订阅行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格 
    			///@param count 要订阅/退订行情订单簿的合约个数
    			///@param exchange_id 交易所代码
    			///@remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情(仅支持深交所)
    			virtual int SubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///退订行情订单簿，包括股票、债券等。（新三板暂不支持）
    			///@return 取消订阅行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格  
    			///@param count 要订阅/退订行情订单簿的合约个数
    			///@param exchange_id 交易所代码
    			///@remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅行情订单簿接口配套使用
    			virtual int UnSubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///订阅逐笔行情，包括股票、债券等。（新三板暂不支持）
    			///@return 订阅逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格  
    			///@param count 要订阅/退订行情订单簿的合约个数
    			///@param exchange_id 交易所代码
    			///@remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情
    			virtual int SubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///退订逐笔行情，包括股票、债券等。（新三板暂不支持）
    			///@return 取消订阅逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格  
    			///@param count 要订阅/退订行情订单簿的合约个数
    			///@param exchange_id 交易所代码
    			///@remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅逐笔行情接口配套使用
    			virtual int UnSubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///订阅全市场的股票、债券、指数等行情
    			///@return 订阅全市场行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@remark 需要与全市场退订行情接口配套使用
    			virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
    
    			///退订全市场的股票、债券、指数等行情
    			///@return 退订全市场行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@remark 需要与订阅全市场行情接口配套使用
    			virtual int UnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
    
    			///订阅全市场的股票、债券等行情订单簿（新三板暂不支持）
    			///@return 订阅全市场行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@remark 需要与全市场退订行情订单簿接口配套使用
    			virtual int SubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
    
    			///退订全市场的股票、债券等行情订单簿（新三板暂不支持）
    			///@return 退订全市场行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@remark 需要与订阅全市场行情订单簿接口配套使用
    			virtual int UnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
    
    			///订阅全市场的股票、债券等逐笔行情（新三板暂不支持）
    			///@return 订阅全市场逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@remark 需要与全市场退订逐笔行情接口配套使用
    			virtual int SubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
    
    			///退订全市场的股票、债券等逐笔行情（新三板暂不支持）
    			///@return 退订全市场逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@remark 需要与订阅全市场逐笔行情接口配套使用
    			virtual int UnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
    
    			///用户登录请求
    			///@return 登录是否成功，“0”表示登录成功，“-1”表示连接服务器出错，此时用户可以调用GetApiLastError()来获取错误代码，“-2”表示已存在连接，不允许重复登录，如果需要重连，请先logout，“-3”表示输入有错误
    			///@param ip 服务器ip地址，类似“127.0.0.1”
    			///@param port 服务器端口号
    			///@param user 登陆用户名
    			///@param password 登陆密码
    			///@param sock_type “1”代表TCP，“2”代表UDP
    			///@param local_ip 本地网卡地址，类似“127.0.0.1”
    			///@remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只能有一个连接
    			virtual int Login(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;
    
    
    			///登出请求
    			///@return 登出是否成功，“0”表示登出成功，非“0”表示登出出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@remark 此函数为同步阻塞式，不需要异步等待登出，当函数返回即可进行后续操作，不允许在回调线程调用。
    			virtual int Logout() = 0;
    
    			///获取沪深2市当前交易日合约部分静态信息
    			///@return 发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功
    			///@param exchange_id 交易所代码，必须提供 1-上海 2-深圳
    			virtual int QueryAllTickers(XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///获取合约的最新价格信息
    			///@return 发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功
    			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格  
    			///@param count 要查询的合约个数
    			///@param exchange_id 交易所代码
    			virtual int QueryTickersPriceInfo(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///获取所有合约的最新价格信息
    			///@return 发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功
    			///@param exchange_id 表示当前全查询的市场，必须指定，仅支持单市场查询
    			virtual int QueryAllTickersPriceInfo(XTP_EXCHANGE_TYPE exchange_id) = 0;
    			
    			///订阅全市场的期权行情
    			///@return 订阅全市期权场行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@remark 需要与全市场退订期权行情接口配套使用
    			virtual int SubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
    
    			///退订全市场的期权行情
    			///@return 退订全市场期权行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@remark 需要与订阅全市场期权行情接口配套使用
    			virtual int UnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
    
    			///获取沪深2市所有合约的详细静态信息，包括指数等非可交易的，不包括新三板
    			///@return 发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功
    			///@param exchange_id 交易所代码，必须提供 1-上海 2-深圳
    			virtual int QueryAllTickersFullInfo(XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///获取新三板所有合约的详细静态信息，包括指数等非可交易的
    			///@return 发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功
    			virtual int QueryAllNQTickersFullInfo() = 0;
    
    			///获取合约的最新快照信息
    			///@return 发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功
    			///@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格  
    			///@param count 要查询的合约个数
    			///@param exchange_id 交易所代码
    			virtual int QueryTickersLatestMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    
    			///订阅指数通行情（TCP模式下不支持）
    			///@return 发送订阅请求是否成功，“0”表示发送订阅请求成功，非“0”表示发送订阅请求不成功
    			///@remark 对应响应函数是OnSubscribeAllIndexPress()
    			virtual int SubscribeAllIndexPress() = 0;
    
    			///取消订阅指数通行情（TCP模式下不支持）
    			///@return 发送订阅请求是否成功，“0”表示发送订阅请求成功，非“0”表示发送订阅请求不成功
    			///@remark 对应响应函数是OnSubscribeAllIndexPress()
    			virtual int UnSubscribeAllIndexPress() = 0;
    
    			///订阅港股通的行情（TCP模式下不支持）
    			///@return 发送订阅请求是否成功，“0”表示发送订阅请求成功，非“0”表示发送订阅请求不成功
    			///@remark 对应响应函数是OnSubscribeAllHKCMarketData()
    			virtual int SubscribeAllHKCMarketData() = 0;
    
    			///取消订阅港股通的行情（TCP模式下不支持）
    			///@return 发送订阅请求是否成功，“0”表示发送订阅请求成功，非“0”表示发送订阅请求不成功
    			///@remark 对应响应函数是OnSubscribeAllHKCMarketData()
    			virtual int UnSubscribeAllHKCMarketData() = 0;
    
    			///请求回补指定行情，包括快照和逐笔
    			///@return 请求回补指定行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
    			///@param rebuild_param 指定回补的参数信息，注意一次性回补最多1000个数据，超过1000需要分批次请求，一次只能指定一种类型的数据
    			///@remark 仅在逐笔行情丢包时或者确实快照行情时使用，回补的行情数据将从OnRebuildTickByTick或者OnRebuildMarketData()接口回调提供，与订阅的行情数据不在同一个线程内
    			virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;
    
    			///获取港股通的静态信息
    			///@return 发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功
    			virtual int QueryAllHKCInfo() = 0;
    
    			///获取指数通的静态信息
    			///@return 发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功
    			virtual int QueryAllIndexPressInfo() = 0;
    
    
    		protected:
    			~QuoteApi() {};
    		};
    	}
    }

  


#### 4.2.2. 示例代码 ​

以下是MyQuoteApi.h文件

cpp
    
    
    #include "xtpx_quote_api.h"
    #include "MyQuoteSpi.h"
    
    using namespace XTPX::API;
    
    class MyQuoteApi
    {
    public: 
    	explicit MyQuoteApi();
    	~MyQuoteApi();
    
    	// 初始化
        bool initialize();
    
    private: 
        XTPX::API::QuoteApi* user_quote_api_;
    	MyQuoteSpi* m_quote_spi;
    };

以下是MyQuoteApi.cpp文件

cpp
    
    
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
    	user_quote_api_ = XTPX::API::QuoteApi::CreateQuoteApi(1, "./", XTP_LOG_LEVEL_DEBUG,true);
    	if (user_quote_api_)
    	{
    		// 注册行情回调接口
    		m_quote_spi = new MyQuoteSpi();
    		user_quote_api_->RegisterSpi(m_quote_spi);
    		// 登录前参数设置
    		user_quote_api_->SetHeartBeatInterval(15);
    		user_quote_api_->SetConfigFile("D:/quote_config.ini");//设置行情接收的配置文件
    		
    		return true;
    	}
    	return false;
    }

  


#### 4.2.3. CreateQuoteApi ​

创建QuoteApi实例。

如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，但是对于同一账户，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接。

◇ 1.函数原型

cpp
    
    
    static QuoteApi *CreateQuoteApi(uint8_t client_id, const char *save_file_path, XTP_LOG_LEVEL log_level=XTP_LOG_LEVEL_DEBUG, bool udpseq_output = true);

◇ 2.参数

client_id：（必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义，普通用户必须使用1-24之间的数值

save_file_path：（必须输入）存储行情api日志文件的目录，请设定一个真实存在的有可写权限的路径，如果路径不存在的话，可能会因为写冲突而造成断线

log_level：日志输出级别

udpseq_output:异步日志是否输出标识

◇ 3.返回

创建出的UserApi

◇ 4.调用示例

cpp
    
    
    #include <iostream>
    #include <cstdint>
    
    typedef unsigned char uint8_t;
    using namespace std;
    
    // 初始化api，创建单例
    uint8_t client_id_ = 1;
    string stdstr_log_path("./");
    
    // 开发调试时用XTP_LOG_LEVEL_DEBUG，稳定运行时用XTP_LOG_LEVEL_INFO
    XTPX::API::XTP_LOG_LEVEL log_level = XTPX::API::XTP_LOG_LEVEL_DEBUG;
    bool udpseq_output = false;
    
    XTPX::API::QuoteApi* user_quote_api_ = XTPX::API::QuoteApi::CreateQuoteApi(client_id_, stdstr_log_path.c_str(), log_level,udpseq_output);
    
    if (user_quote_api_)
    {
    	// 注册行情回调接口
        MyQuoteSpi *spi = new MyQuoteSpi();
        user_quote_api_->RegisterSpi(spi);
    }

  


#### 4.2.4. Release ​

删除接口对象本身。程序退出前，不再使用本接口对象时,可调用该函数删除接口对象。

◇ 1.函数原型

cpp
    
    
    virtual void Release() = 0;

◇ 2.参数

无

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 注销当前会话并删除接口对象
    if (user_quote_api_ != NULL)
    {
    	user_quote_api_->Logout();
    	user_quote_api_->Release();
    }

  


#### 4.2.5. GetApiVersion ​

获取API的发行版本号。

◇ 1.函数原型

cpp
    
    
    virtual const char* GetApiVersion() = 0;

◇ 2.参数

无

◇ 3.返回

返回api发行版本号。

◇ 4.调用示例

cpp
    
    
    // 获取API的发行版本号
    if (user_quote_api_)
    {
    	std::cout << "GetApiVersion : " << user_quote_api_->GetApiVersion() << std::endl;
    }

  


#### 4.2.6. GetApiLastError ​

获取API的系统错误。

可以在调用api接口失败时调用，例如login失败时。

◇ 1.函数原型

cpp
    
    
    virtual XTPRI *GetApiLastError() = 0;

◇ 2.参数

无

◇ 3.返回

cpp
    
    
    namespace XTPX {
    
    	namespace API {
    		///错误信息的字符串长度
    		constexpr int32_t XTP_ERR_MSG_LEN = 124;
    		///响应信息
    		typedef struct XTPRspInfoStruct
    		{
    			///错误代码
    			int32_t	error_id;
    			///错误信息
    			char	error_msg[XTP_ERR_MSG_LEN];
    		} XTPRI;
    
    	}
    }

◇ 4.调用示例

cpp
    
    
    // 获取API的系统错误
    if (user_quote_api_)
    {
    	XTPRI* error_info = user_quote_api_->GetApiLastError();
    	std::cout << error_info->error_id << " : " << error_info->error_msg << std::endl;
    }

  


#### 4.2.7. RegisterSpi ​

注册回调接口。

◇ 1.函数原型

cpp
    
    
    virtual void RegisterSpi(QuoteSpi *spi) = 0;

◇ 2.参数

spi：派生自回调接口类的实例，请在登录之前设定

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 注册行情回调接口
    if (user_quote_api_)
    {
    	MyQuoteSpi *spi = new MyQuoteSpi();
    	user_quote_api_->RegisterSpi(spi);
    }

  


#### 4.2.8. SetHeartBeatInterval ​

设置心跳检测时间间隔，单位为秒。此函数必须在Login之前调用。

◇ 1.函数原型

cpp
    
    
    virtual void SetHeartBeatInterval(uint32_t interval) = 0;

◇ 2.参数

interval：心跳检测时间间隔，单位为秒

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 设定交易服务器超时时间为15秒，用户可自定义
    if (user_quote_api_)
    {
    	user_quote_api_->SetHeartBeatInterval(15);
    }

  


#### 4.2.9. SetConfigFile ​

在登录udp连接方式的行情服务器之前，必须要先设置接收行情的配置文件，此接口只针对udp连接方式的行情环境有效。

◇ 1.函数原型

cpp
    
    
    virtual bool SetConfigFile(const char* filename) = 0;

◇ 2.参数

filename:包含绝对路径的配置文件名

◇ 3.返回

设置配置文件是否成功，true-成功，false-失败，需要检查配置文件是否正确

◇ 4.调用示例

cpp
    
    
    // 设置采用UDP方式连接时的单个队列接收缓冲区大小为256MB
    if (user_quote_api_)
    {
    	std::string fileName("D:/quote_config.ini");
    	user_quote_api_->SetConfigFile(fileName.c_str());
    }

quote_config.ini文件参数设置如下：
    
    
    [md]              #快照行情的参数设置(港股通和指数通行情与快照用同一个md设置)
    decode_flag = 1   #1表示解码的快照数据，目前api提供的只有解码的行情数据
    parse_cpu_id = 2  #解析线程绑核的cpu核id(逻辑核)，0表示不绑核
    [md.normal]
    enable = ON          #ON 表示启用软件行情的快照， OFF表示不启用
    local_ip = 127.0.0.1  #接收快照所在组播组的网段的网卡地址
    recv_cpu_id = 3       #接收线程绑核的cpu核id(逻辑核)，0表示不绑核
    enable_efvi = OFF     #基于solarflare网卡的一种api标识
    L1_buf_capacity = 256 #一级缓存的大小，最小为256k个缓存单元
    L2_buf_capacity = 8   #二级缓存的大小，最小为8k个缓存单元
    busy_wait = ON        #ON 表示开启接收线程忙等状态， OFF表示关闭接收线程忙等状态
    [md.fpga]
    enable = OFF      #ON表示启用硬件行情的快照，OFF表示不启用
    local_ip = 127.0.0.1   #接收快照所在组播组的网段的网卡地址
    recv_cpu_id = 3      #接收线程绑核的cpu核id(逻辑核)，0表示不绑核
    enable_efvi = OFF    #基于solarflare网卡的一种api标识
    L1_buf_capacity = 256 #一级缓存的大小，最小为256k个缓存单元
    L2_buf_capacity = 8   #二级缓存的大小，最小为8k个缓存单元
    busy_wait = ON        #ON 表示开启接收线程忙等状态， OFF表示关闭接收线程忙等状态
    
    [tbt]            #逐笔行情的参数设置
    decode_flag = 1  #1表示解码的逐笔数据，目前api提供的只有解码的行情数据
    parse_cpu_id = 4 #解析线程绑核的cpu核id(逻辑核)，0表示不绑核
    [tbt.normal]
    enable = ON    #ON表示启用软件行情的逐笔，OFF表示不启用
    local_ip = 127.0.0.1  #接收逐笔数据所在组播组的网段的网卡地址
    recv_cpu_id = 5     #接收线程绑核的cpu核id(逻辑核),0表示不绑核
    enable_efvi = OFF   #基于solarflare网卡的一种api标识
    L1_buf_capacity = 256 #一级缓存的大小，最小为256k个缓存单元
    L2_buf_capacity = 8   #二级缓存的大小，最小为8k个缓存单元
    busy_wait = ON     #ON 表示开启接收线程忙等状态， OFF表示关闭接收线程忙等状态
    [tbt.fpga]
    enable = OFF         #ON表示启用硬件行情的逐笔，OFF表示不启用
    local_ip = 127.0.0.1 #接收逐笔数据所在组播组的网段的网卡地址
    recv_cpu_id = 5      #接收线程绑核的cpu核id(逻辑核)，0表示不绑核
    enable_efvi = OFF    #基于solarflare网卡的一种api标识
    L1_buf_capacity = 256 #一级缓存的大小，最小为256k个缓存单元
    L2_buf_capacity = 8   #二级缓存的大小，最小为8k个缓存单元
    busy_wait = ON        #ON 表示开启接收线程忙等状态， OFF表示关闭接收线程忙等状态
    
    [ob]              #订单簿行情的参数设置
    decode_flag = 1   #1表示解码的订单簿数据，目前api提供的只有解码的行情数据。
    parse_cpu_id = 6  #解析线程绑核的cpu核id(逻辑核)，0表示不绑核
    [ob.normal]
    enable = ON      #ON表示启用软件行情的订单簿，OFF表示不启用
    local_ip = 127.0.0.1  #接收订单簿所在组播组的网段的网卡地址
    recv_cpu_id = 7       #接收线程绑核的cpu核id(逻辑核)，0表示不绑核
    enable_efvi = OFF     #基于solarflare网卡的一种api标识
    L1_buf_capacity = 256 #一级缓存的大小，最小为256k个缓存单元
    L2_buf_capacity = 8   #二级缓存的大小，最小为8k个缓存单元
    busy_wait = ON        #ON 表示开启接收线程忙等状态， OFF表示关闭接收线程忙等状态
    
    [subscribe_quote_type]
    sh_ob = OFF            #上海订单簿行情是否打开标志，OFF:关闭，ON：打开
    sz_ob = OFF            #深圳订单簿行情是否打开标志，OFF:关闭，ON：打开
    sh_level1_md_index = ON  #L1沪市指数(指数、IOPV)快照行情是否打开标识
    sh_level1_md_stock = ON  #L1 沪市股票(股票、基金、债券)快照行情是否打开标识
    sh_level1_md_option = ON #L1 沪市期权快照行情是否打开标识
    sh_level2_md_index = ON  #L2 沪市指数快照行情是否打开标识
    sh_level2_md_stock = ON  #L2 沪市股票(股票、基金)快照行情是否打开标识
    sh_level2_md_bond = ON   #L2 沪市债券(可转债、国债逆回购等债券)快照行情是否打开标识
    sh_level2_tbt_stock = ON #L2 沪市股票(股票、基金)逐笔行情是否打开标识
    sh_level2_tbt_bond = ON  #L2 沪市债券(可转债、国债逆回购等债券)逐笔行情是否打开标识
    sz_level1_md_index = ON  #L1 深市指数(指数、IOPV)快照行情是否打开标识
    sz_level1_md_stock = ON  #L1 深市股票(股票、基金、可转债)快照行情是否打开标识
    sz_level1_md_option = ON #L1 深市期权快照行情是否打开标识
    sz_level1_md_bond = ON   #L1 深市债券(国债逆回购等其它债券)行情是否打开标识
    sz_level2_md_index = ON  #L2 深市指数(指数、IOPV)快照行情是否打开标识
    sz_level2_md_stock = ON  #L2 深市股票(股票、基金，可转债)快照行情是否打开标识
    sz_level2_md_bond = ON   #L2 深市债券(国债逆回购等其它债券)快照行情是否打开标识
    sz_level2_tbt_stock = ON #L2 深市股票(股票、基金、可转债)逐笔行情是否打开标识
    sz_level2_tbt_bond = ON  #L2 深市债券(国债逆回购等其它债券)逐笔行情是否打开标识
    nq_rawtxt = OFF        #新三板股票行情是否打开标识
    nq_md_bond = OFF       #新三板债券快照行情是否打开标识
    nq_tbt_bond = OFF      #新三板债券逐笔行情是否打开标识
    
    #以下为指数通indexpress订阅配置
    sh_level1_rawtxt = ON
    #以下为港股通hkc相关订阅配置
    sz_level1_md_hkc = ON
    sz_level1_md_hkcsta = ON

备注：API是1.2.1及其以上的版本将港股通hkc和指数通idxpress与快照md配置合并，不再单独配置。   


#### 4.2.10. SetUDPThreadAffinityArray ​

用UDP接收行情时，设置接收和解析行情线程绑定的cpu集合。

此函数可不调用。若不调用，系统将自动采用配置文件中的默认CPU配置；若需调用则必须严格遵循调用时序——仅允许在执行Login操作前且完成SetConfigFile设置后调用，否则配置将无法生效。在绑核分配环节，api会按数组从前往后的核序号依次分配给配置文件中md、ob、tbt、idxpress、hkc这些CPU设置项（enable为OFF的不会分配）。

◇ 1.函数原型

cpp
    
    
    virtual bool SetUDPThreadAffinityArray(int32_t cpu_no_array[], int32_t count) = 0;

◇ 2.参数

cpu_no_array：设置绑定的cpu集合数组

count：cpu集合数组长度

◇ 3.返回

配置是否成功，true-成功，false-失败

◇ 4.调用示例

cpp
    
    
    //如配置文件只设置了快照和逐笔行情的软硬件接收
    if (user_quote_api_)
    {
    	int32_t cpu_no_array[] = {1,2,3,4,5,6}；
    	user_quote_api_->SetUDPThreadAffinityArray(cpu_no_array, 6);
    }

#### 4.2.11. SubscribeMarketData ​

订阅行情，包括股票、指数和期权。

可以一次性订阅同一证券交易所的多个合约。

◇ 1.函数原型

cpp
    
    
    virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数

ticker：合约ID数组，注意合约代码必须以'\0'结尾，不包含空格

count：要订阅/退订行情的合约个数

exchange_id：交易所代码

◇ 3.返回

订阅接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

◇ 4.调用示例

cpp
    
    
    // 订阅沪市的600000和600001两支股票的行情
    if (user_quote_api_)
    {
    	// 申请内存
    	int ticker_count = 2;//需要订阅行情的证券代码数量，可根据实际订阅需求改动
    	char **ppInstrumentID = new char*[ticker_count];
    	for (int i = 0; i < ticker_count; i++) 
    	{
    		ppInstrumentID[i] = new char[XTP_QUOTE_TICKER_LEN]; 
    	}
    	strcpy_s(ppInstrumentID[0], XTP_QUOTE_TICKER_LEN, "600000");
    	strcpy_s(ppInstrumentID[1], XTP_QUOTE_TICKER_LEN, "600001");
    	//订阅沪市的600000、600001两只股票快照行情 
    	user_quote_api_->SubscribeMarketData(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);
    	
    	// 释放内存
    	for (int i = 0; i < ticker_count; i++) {
    		delete[] ppInstrumentID[i];
    		ppInstrumentID[i] = NULL;
    	}
    	delete[] ppInstrumentID;
    	ppInstrumentID = NULL;
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

◇ 6.通知函数

cpp
    
    
    virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count) { (void)market_data; (void)bid1_qty; (void)bid1_count; (void)max_bid1_count; (void)ask1_qty; (void)ask1_count; (void)max_ask1_count; };

  


#### 4.2.12. UnSubscribeMarketData ​

退订行情，包括股票、指数和期权。

可以一次性取消订阅同一证券交易所的多个合约。

◇ 1.函数原型

cpp
    
    
    virtual int UnSubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数

ticker：合约ID数组，注意合约代码必须以'\0'结尾，不包含空格

count：要订阅/退订行情的合约个数

exchange_id：交易所代码

◇ 3.返回

取消订阅接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

◇ 4.调用示例

cpp
    
    
    // 取消订阅沪市的600000和600001两支股票的行情
    if (user_quote_api_)
    {
    	// 申请内存
    	int ticker_count = 2;//需要取消订阅行情的证券代码数量，可根据实际取消订阅需求改动
    	char **ppInstrumentID = new char*[ticker_count];
    	for (int i = 0; i < ticker_count; i++) 
    	{
    		ppInstrumentID[i] = new char[XTP_QUOTE_TICKER_LEN]; 
    	}
    	strcpy_s(ppInstrumentID[0], XTP_QUOTE_TICKER_LEN, "600000");
    	strcpy_s(ppInstrumentID[1], XTP_QUOTE_TICKER_LEN, "600001");	
    	//取消订阅沪市的600000、600001两只股票快照行情 
    	user_quote_api_->UnSubscribeMarketData(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);
    	
    	// 释放内存
    	for (int i = 0; i < ticker_count; i++) {
    		delete[] ppInstrumentID[i];
    		ppInstrumentID[i] = NULL;
    	}
    	delete[] ppInstrumentID;
    	ppInstrumentID = NULL;
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnUnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

  


#### 4.2.13. SubscribeOrderBook ​

订阅行情订单簿,可以一次性订阅同一证券交易所的多个合约。

◇ 1.函数原型

cpp
    
    
    virtual int SubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数

ticker：合约ID数组，注意合约代码必须以'\0'结尾，不包含空格

count：要订阅/退订行情的合约个数

exchange_id：交易所代码，不支持新三板

◇ 3.返回

订阅行情订单簿是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

◇ 4.调用示例

cpp
    
    
    // 订阅沪市的600000和600001两支股票的行情订单簿
    if (user_quote_api_)
    {
    	// 申请内存
    	int ticker_count = 2;//需要订阅行情的证券代码数量，可根据实际订阅需求改动
    	char **ppInstrumentID = new char*[ticker_count];
    	for (int i = 0; i < ticker_count; i++) 
    	{
    		ppInstrumentID[i] = new char[XTP_QUOTE_TICKER_LEN]; 
    	}
    	strcpy_s(ppInstrumentID[0], XTP_QUOTE_TICKER_LEN, "600000");
    	strcpy_s(ppInstrumentID[1], XTP_QUOTE_TICKER_LEN, "600001");
    	//订阅沪市的600000、600001两只股票订单簿行情
    	user_quote_api_->SubscribeOrderBook(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);
    	
    	// 释放内存
    	for (int i = 0; i < ticker_count; i++) {
    		delete[] ppInstrumentID[i];
    		ppInstrumentID[i] = NULL;
    	}
    	delete[] ppInstrumentID;
    	ppInstrumentID = NULL;
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

◇ 6.通知函数

cpp
    
    
    virtual void OnOrderBook(XTPOB *order_book) { (void)order_book; };

  


#### 4.2.14. UnSubscribeOrderBook ​

取消订阅行情订单簿,可以一次性取消订阅同一证券交易所的多个合约。

◇ 1.函数原型

cpp
    
    
    virtual int UnSubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数

ticker：合约ID数组，注意合约代码必须以'\0'结尾，不包含空格

count：要订阅/退订行情的合约个数

exchange_id：交易所代码，不支持新三板

◇ 3.返回

取消订阅行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

◇ 4.调用示例

cpp
    
    
    // 取消订阅沪市的600000和600001两支股票的行情订单簿
    if (user_quote_api_)
    {
    	// 申请内存
    	int ticker_count = 2;//需要取消订阅行情的证券代码数量，可根据实际取消订阅需求改动
    	char **ppInstrumentID = new char*[ticker_count];
    	for (int i = 0; i < ticker_count; i++) 
    	{
    		ppInstrumentID[i] = new char[XTP_QUOTE_TICKER_LEN]; 
    	}
    	strcpy_s(ppInstrumentID[0], XTP_QUOTE_TICKER_LEN, "600000");
    	strcpy_s(ppInstrumentID[1], XTP_QUOTE_TICKER_LEN, "600001");
    	//取消订阅沪市的600000、600001两只股票订单簿行情
    	user_quote_api_->UnSubscribeOrderBook(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);
    	
    	// 释放内存
    	for (int i = 0; i < ticker_count; i++) {
    		delete[] ppInstrumentID[i];
    		ppInstrumentID[i] = NULL;
    	}
    	delete[] ppInstrumentID;
    	ppInstrumentID = NULL;
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnUnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

  


#### 4.2.15. SubscribeTickByTick ​

订阅逐笔行情,可以一次性订阅同一证券交易所的多个合约。

◇ 1.函数原型

cpp
    
    
    virtual int SubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数

ticker：合约ID数组，注意合约代码必须以'\0'结尾，不包含空格

count：要订阅/退订逐笔行情的合约个数

exchange_id：交易所代码

◇ 3.返回

订阅逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

◇ 4.调用示例

cpp
    
    
    // 订阅沪市的600000和600001两支股票的逐笔行情
    if (user_quote_api_)
    {
    	// 申请内存
    	int ticker_count = 2;//需要订阅行情的证券代码数量，可根据实际订阅需求改动
    	char **ppInstrumentID = new char*[ticker_count];
    	for (int i = 0; i < ticker_count; i++) 
    	{
    		ppInstrumentID[i] = new char[XTP_QUOTE_TICKER_LEN]; 
    	}
    	strcpy_s(ppInstrumentID[0], XTP_QUOTE_TICKER_LEN, "600000");
    	strcpy_s(ppInstrumentID[1], XTP_QUOTE_TICKER_LEN, "600001");
    	//订阅沪市的600000、600001两只股票逐笔行情
    	user_quote_api_->SubscribeTickByTick(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);
    	
    	// 释放内存
    	for (int i = 0; i < ticker_count; i++) {
    		delete[] ppInstrumentID[i];
    		ppInstrumentID[i] = NULL;
    	}
    	delete[] ppInstrumentID;
    	ppInstrumentID = NULL;
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

◇ 6.通知函数

cpp
    
    
    virtual void OnTickByTick(XTPTBT *tbt_data) { (void)tbt_data; };

  


#### 4.2.16. UnSubscribeTickByTick ​

取消订阅逐笔行情,可以一次性取消订阅同一证券交易所的多个合约。

◇ 1.函数原型

cpp
    
    
    virtual int UnSubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数

ticker：合约ID数组，注意合约代码必须以'\0'结尾，不包含空格

count：要订阅/退订逐笔行情的合约个数

exchange_id：交易所代码

◇ 3.返回

取消订阅逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

◇ 4.调用示例

cpp
    
    
    // 取消订阅沪市的600000和600001两支股票的逐笔行情
    if (user_quote_api_)
    {
    	// 申请内存
    	int ticker_count = 2;//需要取消订阅行情的证券代码数量，可根据实际订阅需求改动
    	char **ppInstrumentID = new char*[ticker_count];
    	for (int i = 0; i < ticker_count; i++) 
    	{ 
    		ppInstrumentID[i] = new char[XTP_QUOTE_TICKER_LEN]; 
    	}
    	strcpy_s(ppInstrumentID[0], XTP_QUOTE_TICKER_LEN, "600000");
    	strcpy_s(ppInstrumentID[1], XTP_QUOTE_TICKER_LEN, "600001");
    	//发起取消订阅请求
    	int ret = user_quote_api_->UnSubscribeTickByTick(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);
    
    	//释放内存
    	for (int i = 0; i < ticker_count; i++) {
    		delete[] ppInstrumentID[i];
    		ppInstrumentID[i] = NULL;
    	}
    	delete[] ppInstrumentID;
    	ppInstrumentID = NULL;
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnUnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

  


#### 4.2.17. SubscribeAllMarketData ​

订阅全市场的股票行情。

需要与全市场退订行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

◇ 3.返回

订阅全市场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

◇ 4.调用示例

cpp
    
    
    // 订阅全市场股票行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->SubscribeAllMarketData();
    }

cpp
    
    
    // 订阅沪市股票行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->SubscribeAllMarketData(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 6.通知函数

cpp
    
    
    virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count) { (void)market_data; (void)bid1_qty; (void)bid1_count; (void)max_bid1_count; (void)ask1_qty; (void)ask1_count; (void)max_ask1_count; };

  


#### 4.2.18. UnSubscribeAllMarketData ​

退订全市场的股票行情。

需要与全市场订阅行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int UnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

◇ 3.返回

退订全市场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

◇ 4.调用示例

cpp
    
    
    // 退订全市场股票行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->UnSubscribeAllMarketData();
    }

cpp
    
    
    // 退订沪市股票行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->UnSubscribeAllMarketData(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnUnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

  


#### 4.2.19. SubscribeAllOrderBook ​

订阅全市场的股票行情订单簿。

需要与全市场退订订单簿行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int SubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持）

◇ 3.返回

订阅全市场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

◇ 4.调用示例

cpp
    
    
    // 订阅全市场股票行情订单簿
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->SubscribeAllOrderBook();
    }

cpp
    
    
    // 订阅沪市股票行情订单簿
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->SubscribeAllOrderBook(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 6.通知函数

cpp
    
    
    virtual void OnOrderBook(XTPOB *order_book) { (void)order_book; };

  


#### 4.2.20. UnSubscribeAllOrderBook ​

退订全市场的股票行情订单簿。

需要与全市场订阅订单簿行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int UnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持）

◇ 3.返回

退订全市场行情订单簿接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

◇ 4.调用示例

cpp
    
    
    // 退订全市场股票行情订单簿
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->UnSubscribeAllOrderBook();
    }

cpp
    
    
    // 退订沪市股票行情订单簿
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->UnSubscribeAllOrderBook(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnUnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

  


#### 4.2.21. SubscribeAllTickByTick ​

订阅全市场的股票逐笔行情。

需要与全市场退订逐笔行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int SubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

◇ 3.返回

订阅全市场行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

◇ 4.调用示例

cpp
    
    
    // 订阅全市场股票逐笔行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->SubscribeAllTickByTick();
    }

cpp
    
    
    // 订阅沪市股票逐笔行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->SubscribeAllTickByTick(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 6.通知函数

cpp
    
    
    virtual void OnTickByTick(XTPTBT *tbt_data) { (void)tbt_data; };

  


#### 4.2.22. UnSubscribeAllTickByTick ​

退订全市场的股票逐笔行情。

需要与全市场订阅逐笔行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int UnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

◇ 3.返回

退订全市场逐笔行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

◇ 4.调用示例

cpp
    
    
    // 退订全市场股票逐笔行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->UnSubscribeAllTickByTick();
    }

cpp
    
    
    // 退订沪市股票逐笔行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->UnSubscribeAllTickByTick(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnUnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

  


#### 4.2.23. Login ​

用户登录请求。

此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只能有一个连接。

◇ 1.函数原型

cpp
    
    
    virtual int Login(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;

◇ 2.参数

Ip：服务器ip地址，类似"127.0.0.1"

port：服务器端口号

user：登录用户名

password：登录密码

sock_type："1"代表TCP，"2"代表UDP

local_ip：本地网卡地址，类似"127.0.0.1"

cpp
    
    
    // XTP_PROTOCOL_TYPE是通讯传输协议方式
    typedef enum XTP_PROTOCOL_TYPE
    {
    	XTP_PROTOCOL_TCP = 1,	///<采用TCP方式传输
    	XTP_PROTOCOL_UDP		///<采用UDP方式传输(仅行情接口支持)
    }XTP_PROTOCOL_TYPE;

◇ 3.返回

登陆是否成功，"0"表示登陆成功，非"0"表示登陆不成功。

◇ 4.调用示例

cpp
    
    
    if (user_quote_api_)
    {
        // 登录前参数设置
    	user_quote_api_->SetHeartBeatInterval(15);
    	std::string quote_server_ip = "xxx.xxx.xxx.xxx";
    	int quote_server_port = xxxx;
    	std::string quote_username = "xxxxxxxx";
    	std::string quote_password = "xxxxxx";
    	std::string local_ip = "xxx.xxx.xxx.xxx";//根据本地网卡对应的ip设定
    	std::string fileName = "D:/quote_config.ini";
    	XTPX::API::XTP_PROTOCOL_TYPE quote_protocol = XTPX::API::XTP_PROTOCOL_TCP;//测试环境请使用tcp连接方式，实盘使用udp连接方式
    	user_quote_api_->SetConfigFile(fileName.c_str());//quote_config.ini配置可以参考前面接口SetConfigFile()的使用示例
    
    	// 登录
    	int ret = user_quote_api_->Login(quote_server_ip.c_str(), quote_server_port, quote_username.c_str(), quote_password.c_str(), XTPX::API::XTP_PROTOCOL_TCP, local_ip.c_str());
    }

  


#### 4.2.24. Logout ​

登出请求。此函数为同步阻塞式，不需要异步等待登出，当函数返回即可进行后续操作。

◇ 1.函数原型

cpp
    
    
    virtual int Logout() = 0;

◇ 2.参数

无

◇ 3.返回

登出是否成功，"0"表示登出成功，非"0"表示登出出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 登出请求
    if (user_quote_api_) {
    	int ret = user_quote_api_->Logout();
    }

  


#### 4.2.25. QueryAllTickers ​

获取沪深当前交易日合约部分静态信息。

◇ 1.函数原型

cpp
    
    
    virtual int QueryAllTickers(XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数

exchange_id：交易所代码，必须提供 1-上海 2-深圳，不支持新三板

◇ 3.返回

发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功。

◇ 4.调用示例

cpp
    
    
    // 获取当前交易日沪市所有合约静态信息
    if (user_quote_api_) {
    	int ret = user_quote_api_->QueryAllTickers(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryAllTickers(XTPQSI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };

  


#### 4.2.26. QueryTickersPriceInfo ​

获取合约的最新价格信息。

◇ 1.函数原型

cpp
    
    
    virtual int QueryTickersPriceInfo(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数

ticker：合约ID数组，注意合约代码必须以'\0'结尾，不包含空格

count：要订阅/退订逐笔行情的合约个数

exchange_id：交易所代码

◇ 3.返回

发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功。

◇ 4.调用示例

cpp
    
    
    // 获取沪市的600000和600001两支股票的最新价格信息
    if (user_quote_api_)
    {
    	// 申请内存
    	int ticker_count = 2;//需要查询的证券代码数量，可根据实际需求改动
    	char **ppInstrumentID = new char*[ticker_count];
    	for (int i = 0; i < ticker_count; i++) 
    	{ 
    		ppInstrumentID[i] = new char[XTP_QUOTE_TICKER_LEN]; 
    	}
    	strcpy_s(ppInstrumentID[0], XTP_QUOTE_TICKER_LEN, "600000");
    	strcpy_s(ppInstrumentID[1], XTP_QUOTE_TICKER_LEN, "600001");
    	// 发送查询请求
    	int ret = user_quote_api_->QueryTickersPriceInfo(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);
    
    	//释放内存
    	for (int i = 0; i < ticker_count; i++) {
    		delete[] ppInstrumentID[i];
    		ppInstrumentID[i] = NULL;
    	}
    	delete[] ppInstrumentID;
    	ppInstrumentID = NULL;
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryTickersPriceInfo(XTPTPI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };

  


#### 4.2.27. QueryAllTickersPriceInfo ​

获取所有合约的最新价格信息。

◇ 1.函数原型

cpp
    
    
    virtual int QueryAllTickersPriceInfo(XTP_EXCHANGE_TYPE exchange_id) = 0；

◇ 2.参数

无

◇ 3.返回

发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功。

◇ 4.调用示例

cpp
    
    
    // 获取沪市所有合约的最新价格信息
    if (user_quote_api_) {
    	int ret = user_quote_api_->QueryAllTickersPriceInfo(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryTickersPriceInfo(XTPTPI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };

  


#### 4.2.28. SubscribeAllOptionMarketData ​

订阅全市场的期权行情快照。

需要与全市场退订期权快照行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int SubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持新三板）

◇ 3.返回

订阅全市场期权行情接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错。

◇ 4.调用示例

cpp
    
    
    // 订阅全市场期权行情快照
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->SubscribeAllOptionMarketData();
    }

cpp
    
    
    // 订阅沪市期权行情快照
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->SubscribeAllOptionMarketData(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 6.通知函数

cpp
    
    
    virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count) { (void)market_data; (void)bid1_qty; (void)bid1_count; (void)max_bid1_count; (void)ask1_qty; (void)ask1_count; (void)max_ask1_count; };

  


#### 4.2.29. UnSubscribeAllOptionMarketData ​

退订期权行情快照。

需要与订阅全市场期权行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int UnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

◇ 2.参数

exchange_id：表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板（目前不支持新三板）

◇ 3.返回

取消订阅接口调用是否成功，"0"表示接口调用成功，非"0"表示接口调用出错

◇ 4.调用示例

cpp
    
    
    // 退订全市场期权行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->UnSubscribeAllOptionMarketData();
    }

cpp
    
    
    // 退订沪市期权行情
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->UnSubscribeAllOptionMarketData(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnUnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

  


#### 4.2.30. QueryAllTickersFullInfo ​

获取沪深所有合约的详细静态信息，包括指数等非可交易的。沪深两市需分市场分别查询。

◇ 1.函数原型

cpp
    
    
    virtual int QueryAllTickersFullInfo(XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数

exchange_id：交易所代码，必须提供，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场（目前不支持新三板）

◇ 3.返回

发送查询请求是否成功，"0"表示发送查询请求成功，非"0"表示发送查询请求不成功。

◇ 4.调用示例

cpp
    
    
    // 获取沪市所有合约的详细静态信息
    if (user_quote_api_)
    {
    	int ret = user_quote_api_->QueryAllTickersFullInfo(XTP_EXCHANGE_SH);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryAllTickersFullInfo(XTPQFI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };

  


#### 4.2.31. QueryAllNQTickersFullInfo ​

取新三板所有合约的详细静态信息，包括指数等非可交易的。

◇ 1.函数原型

cpp
    
    
    virtual int QueryAllNQTickersFullInfo() = 0;

◇ 2.参数

无

◇ 3.返回

发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功。

◇ 4.调用示例

cpp
    
    
    if(user_quote_api_)
    {
    	int ret = user_quote_api_->QueryAllNQTickersFullInfo();
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryAllNQTickersFullInfo(XTPNQFI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };

  


#### 4.2.32. QueryTickersLatestMarketData ​

获取合约的最新快照信息

◇ 1.函数原型

cpp
    
    
    virtual int QueryTickersLatestMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

◇ 2.参数 ticker[]:合约ID数组，注意合约代码必须以'\0'结尾，不包含空格  
count:要查询的合约个数  
exchange_id：交易所代码

◇ 3.返回

发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功。

◇ 4.调用示例

cpp
    
    
    // 获取沪市的600000和600001两支股票的最新快照信息
    if (user_quote_api_)
    {
    	// 申请内存
    	int ticker_count = 2;//需要查询的证券代码数量，可根据实际需求改动
    	char **ppInstrumentID = new char*[ticker_count];
    	for (int i = 0; i < ticker_count; i++) 
    	{ 
    		ppInstrumentID[i] = new char[XTP_QUOTE_TICKER_LEN]; 
    	}
    	strcpy_s(ppInstrumentID[0], XTP_QUOTE_TICKER_LEN, "600000");
    	strcpy_s(ppInstrumentID[1], XTP_QUOTE_TICKER_LEN, "600001");
    	// 发送查询请求
    	int ret = user_quote_api_->QueryTickersLatestMarketData(ppInstrumentID, ticker_count, XTP_EXCHANGE_SH);
    
    	//释放内存
    	for (int i = 0; i < ticker_count; i++) {
    		delete[] ppInstrumentID[i];
    		ppInstrumentID[i] = NULL;
    	}
    	delete[] ppInstrumentID;
    	ppInstrumentID = NULL;
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryTickersLatestMarketData(XTPMD* market_data, XTPRI *error_info, bool is_last) { (void)market_data; (void)error_info; (void)is_last; };

  


#### 4.2.33. SubscribeAllIndexPress ​

订阅指数通行情。

与退订指数通行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int SubscribeAllIndexPress() = 0;

◇ 2.参数  
无

◇ 3.返回

发送订阅请求是否成功，“0”表示发送订阅请求成功，非“0”表示发送订阅请求不成功。

◇ 4.调用示例

cpp
    
    
    if (user_quote_api_)
    {
    	user_quote_api_->SubscribeAllIndexPress();
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnSubscribeAllIndexPress(XTPRI *error_info) { (void)error_info; };

◇ 6.通知函数

cpp
    
    
    virtual void OnIndexPress(XTPIndexPress *idx) { (void)idx; };

  


#### 4.2.34. UnSubscribeAllIndexPress ​

取消订阅指数通行情。

与订阅指数通行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int UnSubscribeAllIndexPress() = 0;

◇ 2.参数  
无

◇ 3.返回

发送取消订阅请求是否成功，“0”表示发送请求成功，非“0”表示发送请求不成功。

◇ 4.调用示例

cpp
    
    
    if (user_quote_api_)
    {
    	user_quote_api_->UnSubscribeAllIndexPress();
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnUnSubscribeAllIndexPress(XTPRI *error_info) { (void)error_info; };

  


#### 4.2.35. SubscribeAllHKCMarketData ​

订阅港股通的行情。

与退订港股通行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int SubscribeAllHKCMarketData() = 0;

◇ 2.参数  
无

◇ 3.返回

发送订阅请求是否成功，“0”表示发送订阅请求成功，非“0”表示发送订阅请求不成功。

◇ 4.调用示例

cpp
    
    
    if (user_quote_api_)
    {
    	user_quote_api_->SubscribeAllHKCMarketData();
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnSubscribeAllHKCMarketData(XTPRI *error_info) { (void)error_info; };

◇ 6.通知函数

cpp
    
    
    virtual void OnHKRLData(XTPHKCRL *hkc_data) { (void)hkc_data; };

  


#### 4.2.36. UnSubscribeAllHKCMarketData ​

取消订阅港股通的行情。

与订阅港股通行情接口配套使用。

◇ 1.函数原型

cpp
    
    
    virtual int UnSubscribeAllHKCMarketData() = 0;

◇ 2.参数  
无

◇ 3.返回

发送取消订阅请求是否成功，“0”表示发送请求成功，非“0”表示发送请求不成功。

◇ 4.调用示例

cpp
    
    
    if (user_quote_api_)
    {
    	user_quote_api_->UnSubscribeAllHKCMarketData();
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnUnSubscribeAllHKCMarketData(XTPRI *error_info) { (void)error_info; };

  


#### 4.2.37. RequestRebuildQuote ​

请求回补指定行情，包括快照和逐笔。

仅在逐笔行情丢包时或者缺失快照行情时使用，回补的行情数据将从OnRebuildTickByTick或者OnRebuildMarketData()接口回调提供，与订阅的行情数据不在同一个线程内。

◇ 1.函数原型

cpp
    
    
    virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;

◇ 2.参数

rebuild_param：指定回补的参数信息，注意一次性回补最多1000个数据，超过1000需要分批次请求，一次只能指定一种类型的数据

cpp
    
    
    ///实时行情回补请求结构体
    typedef struct XTPQuoteRebuildReq
    {
    	///请求id 请求端自行管理定义
    	int32_t                     request_id;
    	///请求数据类型 1-快照 2-逐笔 3-指定股票逐笔
    	XTP_QUOTE_REBUILD_DATA_TYPE data_type;
    	///请求市场 1-上海  2-深圳
    	XTP_EXCHANGE_TYPE           exchange_id;
    	///data_type=逐笔或者指定股票逐笔时，表示逐笔通道号
    	int16_t                     channel_number;
    	///预留
    	char                        unuse[2];
    	///合约代码 以'\0'结尾  沪深A股6位  期权8位，当data_type=为快照或者指定股票逐笔时使用
    	char                        ticker[16];
    	///data_type=逐笔或者指定股票逐笔时 表示序列号begin； =快照 表示时间begin(格式为YYYYMMDDHHMMSSsss)
    	int64_t                     begin;
    	///data_type=逐笔或者指定股票逐笔时 表示序列号end； =快照 表示时间end(格式为YYYYMMDDHHMMSSsss)   逐笔区间：[begin, end]前后闭区间  快照区间：[begin, end)  前闭后开区间      
    	int64_t                     end;
    }XTPQuoteRebuildReq;

cpp
    
    
    ///@brief XTP_QUOTE_DATA_TYPE是行情数据类型 逐笔，快照等
    /////////////////////////////////////////////////////////////////////////
    typedef  uint32_t  XTP_QUOTE_REBUILD_DATA_TYPE;
    ///<未知类型
    constexpr uint32_t XTP_QUOTE_REBUILD_UNKNOW = 0;
    ///<快照类型
    constexpr uint32_t XTP_QUOTE_REBUILD_MD = 1;
    ///<逐笔类型
    constexpr uint32_t XTP_QUOTE_REBUILD_TBT = 2;
    ///<指定股票逐笔类型
    constexpr uint32_t XTP_QUOTE_REBUILD_TICKER_TBT = 3;

◇ 3.返回

请求回补指定行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错。

◇ 4.调用示例

cpp
    
    
    // 请求回补上证600000股票的快照
    if (user_quote_api_) 
    {
    	XTPQuoteRebuildReq rebuild_param;
    	rebuild_param.request_id = 100;
    	rebuild_param.data_type = XTP_QUOTE_REBUILD_MD;
    	rebuild_param.exchange_id = XTP_EXCHANGE_SH;
    	std::string stdstr_ticker = "600000";
    	strncpy(rebuild_param.ticker, stdstr_ticker.c_str(), XTP_QUOTE_TICKER_LEN);
    	rebuild_param.channel_number = 0;//仅逐笔订阅时生效，对于快照可不赋值
    	rebuild_param.begin = YYYYMMDDHHMMSSsss;//快照开始时间，闭区间，用户根据实际情况修改
    	rebuild_param.end = YYYYMMDDHHMMSSsss;//快照结束时间，开区间，用户根据实际情况修改
    
    	int ret = user_quote_api_->RequestRebuildQuote(&rebuild_param);
    }

◇ 5.响应函数

cpp
    
    
    ///请求回补指定行情的总体结果应答
    virtual void OnRequestRebuildQuote(XTPQuoteRebuildResultRsp* rebuild_result) { (void)rebuild_result; };
    ///回补的逐笔行情数据
    virtual void OnRebuildTickByTick(XTPTBT *tbt_data) { (void)tbt_data; };
    ///回补的快照行情数据
    virtual void OnRebuildMarketData(XTPMD *md_data) { (void)md_data; };

  


#### 4.2.38. QueryAllHKCInfo ​

获取港股通的静态信息。

◇ 1.函数原型

cpp
    
    
    virtual int QueryAllHKCInfo() = 0;

◇ 2.参数

无

◇ 3.返回

发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功。

◇ 4.调用示例

cpp
    
    
    if(user_quote_api_)
    {
    	user_quote_api_->QueryAllHKCInfo();
    }

◇ 5.响应函数

cpp
    
    
    ///查询港股通完整静态信息的应答
    virtual void OnQueryAllHKCInfo(XTPHKCSI* hkcsi, XTPRI *error_info, bool is_last) { (void)hkcsi; (void)error_info; (void)is_last; };

  


#### 4.2.39. QueryAllIndexPressInfo ​

获取指数通的静态信息。

◇ 1.函数原型

cpp
    
    
    virtual int QueryAllIndexPressInfo() = 0;

◇ 2.参数

无

◇ 3.返回

发送查询请求是否成功，“0”表示发送查询请求成功，非“0”表示发送查询请求不成功.

◇ 4.调用示例

cpp
    
    
    if(user_quote_api_)
    {
    	user_quote_api_->QueryAllIndexPressInfo();
    }

◇ 5.响应函数

cpp
    
    
    ///查询指数通完整静态信息的应答
    virtual void OnQueryAllIndexPressInfo(XTPIPSI* ipsi, XTPRI *error_info, bool is_last) { (void)ipsi; (void)error_info; (void)is_last; };

  


### 4.3. QuoteSpi ​

QuoteSpi类提供了行情相关的回调接口，用户需要继承该类并重写这些接口，以获取响应数据。

#### 4.3.1. 接口 ​

cpp
    
    
    namespace XTPX {
    	namespace API {
    		class QuoteSpi
    		{
    		public:
    
    			///当客户端与行情后台通信连接断开时，该方法被调用。
    			///@param reason 错误原因，请与错误代码表对应
    			///@remark api不会自动重连，当断线发生时，请用户自行选择后续操作。可以在此函数中调用Login重新登录。注意用户重新登录后，需要重新订阅行情
    			virtual void OnDisconnected(int reason) { (void)reason; };
    
    
    			///错误应答
    			///@param error_info 当服务器响应发生错误时的具体的错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 此函数只有在服务器发生错误时才会调用，一般无需用户处理
    			virtual void OnError(XTPRI *error_info) { (void)error_info; };
    
    			///订阅行情应答，包括股票、指数和期权
    			///@param ticker 详细的合约订阅情况
    			///@param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };
    
    			///退订行情应答，包括股票、指数和期权
    			///@param ticker 详细的合约取消订阅情况
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnUnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };
    
    			///深度行情通知，包含买一卖一队列
    			///@param market_data 行情数据
    			///@param bid1_qty 买一队列数据
    			///@param bid1_count 买一队列的有效委托笔数，即bid1_qty数组的长度，最大为50
    			///@param max_bid1_count 买一队列总委托笔数
    			///@param ask1_qty 卖一队列数据
    			///@param ask1_count 卖一队列的有效委托笔数，即ask1_qty数组的长度，最大为50
    			///@param max_ask1_count 卖一队列总委托笔数
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count) { (void)market_data; (void)bid1_qty; (void)bid1_count; (void)max_bid1_count; (void)ask1_qty; (void)ask1_count; (void)max_ask1_count; };
    
    			/// ETF的IOPV通知
    			/// @param iopv ETF的参考单位基金净值数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnETFIOPVData(IOPV *iopv) { (void)iopv; };
    
    			///订阅行情订单簿应答，包括股票、债券
    			///@param ticker 详细的合约订阅情况
    			///@param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };
    
    			///退订行情订单簿应答，包括股票、债券
    			///@param ticker 详细的合约取消订阅情况
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnUnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };
    
    			///行情订单簿通知，包括股票、债券
    			///@param order_book 行情订单簿数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnOrderBook(XTPOB *order_book) { (void)order_book; };
    
    			///订阅逐笔行情应答，包括股票、债券
    			///@param ticker 详细的合约订阅情况
    			///@param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };
    
    			///退订逐笔行情应答，包括股票、债券
    			///@param ticker 详细的合约取消订阅情况
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnUnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };
    
    			///逐笔行情通知，包括股票、债券
    			///@param tbt_data 逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，需要根据type来区分是逐笔委托还是逐笔成交，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnTickByTick(XTPTBT *tbt_data) { (void)tbt_data; };
    
    			///订阅全市场的股票行情应答
    			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };
    
    			///退订全市场的股票行情应答
    			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnUnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };
    
    			///订阅全市场的股票行情订单簿应答
    			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };
    
    			///退订全市场的股票行情订单簿应答
    			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnUnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };
    
    			///订阅全市场的股票逐笔行情应答
    			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };
    
    			///退订全市场的股票逐笔行情应答
    			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnUnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };
    
    
    			///查询合约部分静态信息的应答
    			///@param ticker_info 合约部分静态信息
    			///@param error_info 查询合约部分静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次查询合约部分静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			virtual void OnQueryAllTickers(XTPQSI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };
    
    			///查询合约的最新价格信息应答
    			///@param ticker_info 合约的最新价格信息
    			///@param error_info 查询合约的最新价格信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			virtual void OnQueryTickersPriceInfo(XTPTPI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };
    
    			///订阅全市场的期权行情应答
    			///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };
    
    			///退订全市场的期权行情应答
    			///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板
    			///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnUnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };
    
    			///查询沪深2市合约完整静态信息的应答
    			///@param ticker_info 合约完整静态信息
    			///@param error_info 查询合约完整静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次查询合约完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			virtual void OnQueryAllTickersFullInfo(XTPQFI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };
    
    			///查询新三板合约完整静态信息的应答
    			///@param ticker_info 合约完整静态信息
    			///@param error_info 查询合约完整静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次查询合约完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			virtual void OnQueryAllNQTickersFullInfo(XTPNQFI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };
    
    			///新三板合约完整静态信息盘中推送通知
    			///@param ticker_info 合约完整静态信息
    			virtual void OnXTPQuoteNQFullInfo(XTPNQFI* ticker_info) { (void)ticker_info; };
    
    			///查询合约的最新快照信息应答
    			///@param market_data 合约的最新快照信息
    			///@param error_info 查询合约的最新快照信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			virtual void OnQueryTickersLatestMarketData(XTPMD* market_data, XTPRI *error_info, bool is_last) { (void)market_data; (void)error_info; (void)is_last; };
    
    			///订阅指数通行情应答
    			///@param error_info 订阅指数通时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnSubscribeAllIndexPress(XTPRI *error_info) { (void)error_info; };
    
    			///取消订阅指数通行情应答
    			///@param error_info 取消订阅指数通时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnUnSubscribeAllIndexPress(XTPRI *error_info) { (void)error_info; };
    
    			///指数通行情通知
    			///@param idx 指数通的行情数据
    			///@remark 订阅指数通行情的时候触发推送通知
    			virtual void OnIndexPress(XTPIndexPress *idx) { (void)idx; };
    
    			///订阅港股通行情应答
    			///@param error_info 订阅港股通通时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnSubscribeAllHKCMarketData(XTPRI *error_info) { (void)error_info; };
    
    			///取消订阅港股通行情应答
    			///@param error_info 取消订阅港股通时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 需要快速返回
    			virtual void OnUnSubscribeAllHKCMarketData(XTPRI *error_info) { (void)error_info; };
    
    			///港股通实时额度通知
    			///@param hkc_data 港股通实时额度数据
    			///@remark 订阅港股通行情的时候会触发推送通知
    			virtual void OnHKRLData(XTPHKCRL *hkc_data) { (void)hkc_data; };
    
    			///港股通行情通知
    			///@param hkc_md 港股通的行情数据
    			///@remark 订阅港股通行情的时候会触发推送通知
    			virtual void OnHKCMarketData(XTPHKCMD *hkc_md) { (void)hkc_md; };
    
    			///请求回补指定行情的总体结果应答
    			///@param rebuild_result 当回补结束时被调用，如果回补结果失败，则msg参数表示失败原因
    			///@remark 需要快速返回，仅在回补数据发送结束后调用，如果请求数据太多，一次性无法回补完，那么rebuild_result.result_code = XTP_REBUILD_RET_PARTLY，此时需要根据回补结果继续发起回补数据请求
    			virtual void OnRequestRebuildQuote(XTPQuoteRebuildResultRsp* rebuild_result) { (void)rebuild_result; };
    
    			///回补的逐笔行情数据
    			///@param tbt_data 回补的逐笔行情数据
    			///@remark 需要快速返回，此函数调用与OnTickByTick不在一个线程内，会在OnRequestRebuildQuote()之前回调
    			virtual void OnRebuildTickByTick(XTPTBT *tbt_data) { (void)tbt_data; };
    
    			///回补的快照行情数据
    			///@param md_data 回补的快照行情数据
    			///@remark 需要快速返回，此函数调用与OnDepthMarketData不在一个线程内，会在OnRequestRebuildQuote()之前回调
    			virtual void OnRebuildMarketData(XTPMD *md_data) { (void)md_data; };
    
    			///查询港股通完整静态信息的应答
    			///@param hkcsi 港股通静态信息
    			///@param error_info 查询港股通完整静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次查询港股通完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			virtual void OnQueryAllHKCInfo(XTPHKCSI* hkcsi, XTPRI *error_info, bool is_last) { (void)hkcsi; (void)error_info; (void)is_last; };
    
    			///查询指数通完整静态信息的应答
    			///@param ipsi 指数通完整静态信息
    			///@param error_info 查询指数通完整静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param is_last 是否此次查询指数通完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			virtual void OnQueryAllIndexPressInfo(XTPIPSI* ipsi, XTPRI *error_info, bool is_last) { (void)ipsi; (void)error_info; (void)is_last; };
    
    		};
    	}
    }

  


#### 4.3.2. 示例代码 ​

MyQuoteSpi继承QuoteSpi

以下是MyQuoteSpi.h文件

cpp
    
    
    #include "xtpx_quote_api.h"
    
    using namespace XTPX::API;
    
    class MyQuoteSpi : public QuoteSpi
    {
    public:
        explicit MyQuoteSpi();
        ~MyQuoteSpi();
    
        //接收行情
        void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count);
    };

以下是MyQuoteSpi.cpp文件

cpp
    
    
    #include "MyQuoteSpi.h"
    
    MyQuoteSpi::MyQuoteSpi() { }
    MyQuoteSpi::~MyQuoteSpi() { }
    
    //接收行情
    void MyQuoteSpi::OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count)
    {
    	std::cout << "OnDepthMarketData." << std::endl;
    }

  


#### 4.3.3. OnDisconnected ​

当客户端与行情后台通信连接断开时，该方法被调用。

API不会自动重连，当断线发生时，请用户自行选择后续操作。可以在此函数中调用Login重新登录。对于接入实盘(UDP连接方式)的用户重新登录后，无需重新订阅行情。

◇ 1.函数原型

cpp
    
    
    virtual void OnDisconnected(int reason) {};

◇ 2.参数

Reason：错误原因，目前仅一个原因，可不用参考

◇ 3.返回

◇ 4.示例代码 以下是MyQuoteSpi.h文件

cpp
    
    
    #include "xtpx_quote_api.h"
    #include <iostream>
    #include <functional>
    
    using namespace std;
    using namespace XTPX::API;
    
    class MyQuoteSpi : public QuoteSpi
    {
    public:
        explicit MyQuoteSpi();
        ~MyQuoteSpi();
        void OnDisconnected(int reason);
    	void bindfunc(std::function<void(void)> f)
        {
            _disconnect = f;
        }
    
    private:
        std::function<void(void)> _disconnect;
    }

以下是MyQuoteSpi.cpp文件

cpp
    
    
    #include "MyQuoteSpi.h"
    
    MyQuoteSpi::MyQuoteSpi() { }
    MyQuoteSpi::~MyQuoteSpi() { }
    
    void MyQuoteSpi::OnDisconnected(int reason)
    {
    	std::cout << "quote is disconnected." << std::endl;
    	// 重连通知
    	_disconnect();
    }

以下是MyQuoteApi.h文件

cpp
    
    
    #include "xtpx_quote_api.h"
    #include "MyQuoteSpi.h"
    
    using namespace XTPX::API;
    
    // 行情登录信息缓存
    struct LoginQuoteInfo
    {
        LoginQuoteInfo()
        {
            quote_server_port = 0;
        }
    
        std::string quote_server_ip;
        int quote_server_port;
    	std::string quote_username;
    	std::string quote_password;
        XTP_PROTOCOL_TYPE quote_sock_type;
    	std::string local_ip;
    };
    
    class MyQuoteApi
    {
    public: 
    	explicit MyQuoteApi();
    	~MyQuoteApi();
    
    	// 重连函数
    	void reloginQuote();
    
    private: 
    
    	LoginQuoteInfo m_loginQuoteInfo;
    };

以下是MyQuoteApi.cpp文件

cpp
    
    
    #include "MyQuoteApi.h"
    #ifdef _WIN32
        #include <windows.h>
    #else
        #include <unistd.h>
    #endif
    
    MyQuoteApi::MyQuoteApi() 
    {
    }
    
    // 创建并初始化交易API
    bool MyQuoteApi::initialize()
    {
    	user_quote_api_ = XTPX::API::QuoteApi::CreateQuoteApi(1, "./", log_level, true);
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
            while (i_counter < 3) {
                i_counter++;
    			
                int ret = user_quote_api_->Login(m_loginQuoteInfo.quote_server_ip.c_str(),
                                                 m_loginQuoteInfo.quote_server_port,
                                                 m_loginQuoteInfo.quote_username.c_str(),
                                                 m_loginQuoteInfo.quote_password.c_str(),
                                                 m_loginQuoteInfo.quote_sock_type,
                                                 m_loginQuoteInfo.local_ip.c_str());
                if (0 == ret) {
    				std::cout << "relogin success." << std::endl;
                    return;
                } else {
    				std::cout << "relogin failed." << std::endl;
    #ifdef _WIN32
                    Sleep(5000);
    #else
                    sleep(5);
    #endif
                }
            }
    		std::cout << "relogin failed over 3 times." << std::endl;
        } else {
    		std::cout << "relogin info missing." << std::endl;
        }    
    }

无   


#### 4.3.4. OnError ​

错误应答。

此函数只有在服务器发生错误时才会调用，一般无需用户处理。

**目前此函数不会被调用**。

◇ 1.函数原型

cpp
    
    
    virtual void OnError(XTPRI *error_info) { (void)error_info; };

◇ 2.参数

error_info：当服务器响应发生错误时的具体的错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

cpp
    
    
    ///错误信息的字符串长度
    constexpr int32_t XTP_ERR_MSG_LEN = 124;
    ///响应信息
    typedef struct XTPRspInfoStruct
    {
    	///错误代码
    	int32_t	error_id;
    	///错误信息
    	char	error_msg[XTP_ERR_MSG_LEN];
    } XTPRI;

◇ 3.返回

无   


#### 4.3.5. OnSubMarketData ​

订阅行情应答，包括股票、指数和期权。

每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

◇ 2.参数

Ticker：详细的合约订阅情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

cpp
    
    
    ///指定的合约
    typedef struct XTPSpecificTickerStruct
    {
    	///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    
    } XTPST;

cpp
    
    
    ///@brief XTP_EXCHANGE_TYPE是交易所类型
    ////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_EXCHANGE_TYPE;
    ///<上证
    constexpr uint32_t XTP_EXCHANGE_SH = 1;
    ///<深证
    constexpr uint32_t XTP_EXCHANGE_SZ = 2;
    ///<新三板，全国中小企业股份转让系统
    constexpr uint32_t XTP_EXCHANGE_NQ = 3;
    ///<港交所
    constexpr uint32_t XTP_EXCHANGE_HK = 4;
    ///<不存在的交易所类型
    constexpr uint32_t XTP_EXCHANGE_UNKNOWN = 5;
    
    /// 存放证券代码的字符串长度
    constexpr int32_t XTP_QUOTE_TICKER_LEN = 16;

  


◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 订阅行情，包括股票、指数和期权
    virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.6. OnUnSubMarketData ​

退订行情应答，包括股票、指数和期权。

每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) {};

◇ 2.参数

Ticker：详细的合约订阅情况

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///指定的合约
    typedef struct XTPSpecificTickerStruct
    {
    	///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    
    } XTPST;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 退订行情，包括股票、指数和期权
    virtual int UnSubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.7. OnDepthMarketData ​

深度行情通知，包含买一卖一队列。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count, int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count) {};

◇ 2.参数

market_data：行情数据

bid1_qty：买一队列数据

bid1_count：买一队列的有效委托笔数

max_bid1_count：买一队列总委托笔数

ask1_qty：卖一队列数据

ask1_count：卖一队列的有效委托笔数

max_ask1_count：卖一队列总委托笔数

XTP推送的深交所行情数据现已支持ETFXTPMarketDataStockExData结构体中的ETF申购笔数etf_buy_count、ETF赎回笔数etf_sell_count、ETF申购数量etf_buy_qty以及ETF赎回数量etf_sell_qty字段，用于表示深交所新增的ETF申赎的实时申赎量数据。

cpp
    
    
    ///行情
    typedef struct XTPMarketDataStruct
    {
    	// 代码
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    	/// 决定了union是哪种数据类型
    	XTP_MARKETDATA_TYPE_V2 data_type_v2;
    
    	// 价格
    	///最新价
    	double  last_price;
    	///昨收盘
    	double  pre_close_price;
    	///今开盘
    	double  open_price;
    	///最高价
    	double  high_price;
    	///最低价
    	double  low_price;
    	///今收盘
    	double  close_price;
    
    	// 期权数据
    	///昨日持仓量(张)(目前未填写)
    	int64_t pre_total_long_positon;
    	///持仓量(张)
    	int64_t total_long_positon;
    	///昨日结算价
    	double  pre_settl_price;
    	///今日结算价
    	double  settl_price;
    
    	// 涨跌停 
    	///SH:上交所涨跌停价赋值为0 
    	///涨停价
    	double  upper_limit_price;
    	///跌停价
    	double  lower_limit_price;
    	///预留
    	double  pre_delta;
    	///预留
    	double  curr_delta;
    
    	/// 时间类，格式为YYYYMMDDHHMMSSsss
    	int64_t data_time;
    
    	// 量额数据
    	///数量，为总成交量（单位股，与交易所一致）
    	int64_t qty;
    	///成交金额，为总成交金额（单位元，与交易所一致）
    	double  turnover;
    	///预留(无意义)
    	double  avg_price;
    
    	// 买卖盘
    	///十档申买价
    	double  bid[10];
    	///十档申卖价
    	double  ask[10];
    	///十档申买量
    	int64_t bid_qty[10];
    	///十档申卖量
    	int64_t ask_qty[10];
    
    	// 额外数据
    	///成交笔数
    	int64_t trades_count;
    	///当前交易状态说明，参见官网常见问题说明
    	char    ticker_status[8];
    	///数据
    	union {
    		XTPMarketDataStockExData  stk;
    		XTPMarketDataOptionExData opt;
    		XTPMarketDataBondExData  bond;
    	};
    	int64_t r1; // 预留字段,Rebuild查询md时为首次更新时间
    
    } XTPMD;
    
    ///股票、基金 等额外数据
    struct XTPMarketDataStockExData {
    	///委托买入总量(SH,SZ)
    	int64_t total_bid_qty;
    	///委托卖出总量(SH,SZ)
    	int64_t total_ask_qty;
    	///加权平均委买价格(SH,SZ)
    	double  ma_bid_price;
    	///加权平均委卖价格(SH,SZ)
    	double  ma_ask_price;
    	///债券加权平均委买价格(SH)
    	double  ma_bond_bid_price;
    	///债券加权平均委卖价格(SH)
    	double  ma_bond_ask_price;
    	///债券到期收益率(SH)
    	double  yield_to_maturity;
    	///基金实时参考净值(SH,SZ)
    	double  iopv;
    	///ETF申购笔数(SZ)
    	int32_t etf_buy_count;
    	///ETF赎回笔数(SZ)
    	int32_t etf_sell_count;
    	///ETF申购数量(SZ)
    	double  etf_buy_qty;
    	///ETF申购金额(SZ)
    	double  etf_buy_money;
    	///ETF赎回数量(SZ)
    	double  etf_sell_qty;
    	///ETF赎回金额(SZ)
    	double  etf_sell_money;
    	///权证执行的总数量(SH)
    	double  total_warrant_exec_qty;
    	///权证跌停价格（元）(SH)
    	double  warrant_lower_price;
    	///权证涨停价格（元）(SH)
    	double  warrant_upper_price;
    	///买入撤单笔数(SH)
    	int32_t cancel_buy_count;
    	///卖出撤单笔数(SH)
    	int32_t cancel_sell_count;
    	///买入撤单数量(SH)
    	double  cancel_buy_qty;
    	///卖出撤单数量(SH)
    	double  cancel_sell_qty;
    	///买入撤单金额(SH)
    	double  cancel_buy_money;
    	///卖出撤单金额(SH)
    	double  cancel_sell_money;
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
    	double  pre_iopv;
    	///预留
    	int64_t r1;
    	///预留
    	int64_t r2;
    };
    
    // 期权额外数据
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
    	double  ma_bid_price;
    	///加权平均委卖价格(SZ)
    	double  ma_ask_price;
    	///债券加权平均委买价格(SH)
    	double  ma_bond_bid_price;
    	///债券加权平均委卖价格(SH)
    	double  ma_bond_ask_price;
    	///债券到期收益率(SH)
    	double  yield_to_maturity;
    	///匹配成交最近价(SZ)
    	double  match_lastpx;
    	///债券加权平均价格(SH)
    	double  ma_bond_price;
    	///匹配成交成交量(SZ)
    	int64_t match_qty;
    	///匹配成交成交金额(SZ)
    	double  match_turnover;
    	///预留
    	double  r4;
    	///预留
    	double  r5;
    	///预留
    	double  r6;
    	///预留
    	double  r7;
    	///预留
    	double  r8;
    	///买入撤单笔数(SH)
    	int32_t cancel_buy_count;
    	///卖出撤单笔数(SH)
    	int32_t cancel_sell_count;
    	///买入撤单数量(SH)
    	double  cancel_buy_qty;
    	///卖出撤单数量(SH)
    	double  cancel_sell_qty;
    	///买入撤单金额(SH)
    	double  cancel_buy_money;
    	///卖出撤单金额(SH)
    	double  cancel_sell_money;
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
    	///时段(SHL2)
    	char    instrument_status[8];
    };
    
    ///@brief XTP_MARKETDATA_TYPE_V2是快照数据中的Union类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t  XTP_MARKETDATA_TYPE_V2;
    // 指数
    constexpr uint32_t XTP_MARKETDATA_V2_INDEX = 0;
    // 期权
    constexpr uint32_t XTP_MARKETDATA_V2_OPTION = 1;
    // 现货(股票/基金等)
    constexpr uint32_t XTP_MARKETDATA_V2_ACTUAL = 2;
    // 债券
    constexpr uint32_t XTP_MARKETDATA_V2_BOND = 3;

◇ 3.返回

无

◇ 4.订阅函数

cpp
    
    
    // 订阅行情快照，包括股票、指数和期权
    virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    // 订阅全市场的股票行情快照
    virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;
    // 订阅全市场的期权行情快照
    virtual int SubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.8. OnSubOrderBook ​

订阅行情订单簿应答。

每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

◇ 2.参数

ticker：详细的合约订阅情况

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///指定的合约
    typedef struct XTPSpecificTickerStruct
    {
    	///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    
    } XTPST;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 订阅行情订单簿，包括股票
    virtual int SubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.9. OnUnSubOrderBook ​

退订行情订单簿应答。

每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

◇ 2.参数

ticker：详细的合约取消订阅情况

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

cpp
    
    
    ///指定的合约
    typedef struct XTPSpecificTickerStruct
    {
    	///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    
    } XTPST;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 退订行情订单簿，包括股票
    virtual int UnSubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.10. OnOrderBook ​

行情订单簿通知，包括股票。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnOrderBook(XTPOB *order_book) { (void)order_book; };

◇ 2.参数

order_book：行情订单簿数据

cpp
    
    
    ///订单薄
    typedef struct OrderBookStruct {
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    	///预留
    	int32_t unused;
    
    	///最新价
    	double  last_price;
    	///数量，为总成交量
    	int64_t qty;
    	///成交金额，为总成交金额
    	double  turnover;
    	///成交笔数
    	int64_t trades_count;
    
    	// 买卖盘
    	///十档申买价
    	double  bid[10];
    	///十档申卖价
    	double  ask[10];
    	///十档申买量
    	int64_t bid_qty[10];
    	///十档申卖量
    	int64_t ask_qty[10];
    	/// 时间类
    	int64_t data_time;
    } XTPOB;

◇ 3.返回

无

◇ 4.订阅函数

cpp
    
    
    // 订阅行情订单簿，包括股票
    virtual int SubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    // 订阅全市场的股票行情订单簿
    virtual int SubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.11. OnSubTickByTick ​

订阅逐笔行情应答。

每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

◇ 2.参数

ticker：详细的合约订阅情况

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

cpp
    
    
    ///指定的合约
    typedef struct XTPSpecificTickerStruct
    {
    	///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    
    } XTPST;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 订阅逐笔行情，包括股票
    virtual int SubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.12. OnUnSubTickByTick ​

退订逐笔行情应答，包括股票

每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) { (void)ticker; (void)error_info; (void)is_last; };

◇ 2.参数

ticker：详细的合约取消订阅情况

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

cpp
    
    
    ///指定的合约
    typedef struct XTPSpecificTickerStruct
    {
    	///合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    
    } XTPST;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 退订逐笔行情，包括股票
    virtual int UnSubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.13. OnTickByTick ​

逐笔行情通知，包括股票。

逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，需要根据type来区分是逐笔委托还是逐笔成交，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnTickByTick(XTPTBT *tbt_data) { (void)tbt_data; };

◇ 2.参数

tbt_data 逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，需要根据type来区分是逐笔委托还是逐笔成交

cpp
    
    
    ///逐笔数据信息
    typedef struct XTPTickByTickStruct {
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    	///委托 or 成交
    	XTP_TBT_TYPE type;
    
    	/// SH: 业务序号（委托成交统一编号，同一个channel_no内连续）
    	/// SZ: 无意义
    	int64_t seq;
    	///委托时间 or 成交时间
    	int64_t data_time;
    
    	union {
    		XTPTickByTickEntrust   entrust;
    		XTPTickByTickTrade     trade;
    		XTPTickByTickStatus    state;
    	};
    } XTPTBT;
    
    ///@brief XTP_TBT_TYPE是一个逐笔回报类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TBT_TYPE;
    ///<逐笔委托
    constexpr uint32_t XTP_TBT_ENTRUST = 1;
    ///<逐笔成交
    constexpr uint32_t  XTP_TBT_TRADE = 2;
    ///<逐笔状态订单
    constexpr uint32_t  XTP_TBT_STATE = 3;
    
    ///逐笔委托
    struct XTPTickByTickEntrust {
    	///频道代码
    	int32_t channel_no;
    	///SH: 'B':买; 'S':卖
    	///SZ: '1':买; '2':卖; 'G':借入; 'F':出借
    	char    side;
    	///SH: 'A': 增加; 'D': 删除
    	///SZ: 订单类别: '1': 市价; '2': 限价; 'U': 本方最优
    	char    ord_type;
    	///预留
    	char    unused[2];
    	///SH: 委托序号(委托成交统一编号, 同一channel_no内连续)
    	///SZ: 委托序号(委托成交统一编号, 同一channel_no内连续)
    	int64_t seq;
    	///委托价格
    	double  price;
    	///SH: 剩余委托数量(balance)
    	///SZ: 委托数量
    	int64_t qty;
    	///SH: 原始订单号
    	///SZ: 无意义
    	int64_t order_no;
    
    	/// SH: 已成交的委托数量
    	/// SZ: 无意义
    	int64_t traded_qty;
    	};
    
    
    ///逐笔成交
    struct XTPTickByTickTrade {
    	///频道代码
    	int32_t channel_no;
    	/// SH: 内外盘标识('B':主动买; 'S':主动卖; 'N':未知)
    	/// SZ: 成交标识('4':撤; 'F':成交)
    	char    trade_flag;
    	///预留
    	char    unused[3];
    	///SH: 成交序号(委托单独编号, 同一channel_no内连续)
    	///SZ: 成交序号(委托成交统一编号, 同一channel_no内连续)
    	int64_t seq;
    	///成交价格
    	double  price;
    	///成交量
    	int64_t qty;
    	///成交金额(仅适用上交所)
    	double  money;
    	///买方订单号
    	int64_t bid_no;
    	///卖方订单号
    	int64_t ask_no;
    };
    
    ///逐笔状态订单
    struct XTPTickByTickStatus {
    	///频道代码
    	int32_t channel_no;
    	///预留1
    	int32_t unused1;
    	///同一channel_no内连续
    	int64_t seq;
    	///状态信息
    	char    flag[8];
    };

◇ 3.返回

无

◇ 4.订阅函数

cpp
    
    
    // 订阅逐笔行情，包括股票
    virtual int SubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    // 订阅全市场的股票逐笔行情
    virtual int SubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.14. OnSubscribeAllMarketData ​

订阅全市场的股票行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 订阅全市场的股票行情
    virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.15. OnUnSubscribeAllMarketData ​

退订全市场的股票行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 2.参数

exchange_id：表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 退订全市场的股票行情
    virtual int UnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.16. OnSubscribeAllOrderBook ​

订阅全市场的股票行情订单簿应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 订阅全市场的股票行情订单簿
    virtual int SubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.17. OnUnSubscribeAllOrderBook ​

退订全市场的股票行情订单簿应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 退订全市场的股票行情订单簿
    virtual int UnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.18. OnSubscribeAllTickByTick ​

阅全市场的股票逐笔行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 订阅全市场的股票逐笔行情
    virtual int SubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.19. OnUnSubscribeAllTickByTick ​

退订全市场的股票逐笔行情应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 退订全市场的股票逐笔行情
    virtual int UnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.20. OnQueryAllTickers ​

查询合约部分静态信息的应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryAllTickers(XTPQSI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };

◇ 2.参数

ticker_info：合约部分静态信息

error_info：查询合约部分静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询合约部分静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

cpp
    
    
    ///股票行情静态信息
    typedef struct XTPQuoteStaticInfo {
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    	/// 合约类型
    	XTP_QUOTE_TICKER_TYPE ticker_type;
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	/// 合约名称
    	char    ticker_name[XTP_QUOTE_TICKER_NAME_LEN];
    	///昨收盘
    	double  pre_close_price;
    	///涨停板价
    	double  upper_limit_price;
    	///跌停板价
    	double  lower_limit_price;
    	///最小变动价位
    	double  price_tick;
    	/// 合约最小交易量(买)
    	int32_t buy_qty_unit;
    	/// 合约最小交易量(卖)
    	int32_t sell_qty_unit;
    } XTPQSI;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 获取当前交易日合约部分静态信息
    virtual int QueryAllTickers(XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.21. OnQueryTickersPriceInfo ​

查询合约的最新价格信息应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryTickersPriceInfo(XTPTPI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };

◇ 2.参数

ticker_info：合约的最新价格信息

error_info：查询合约的最新价格信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

cpp
    
    
    ///供查询的最新信息
    typedef struct XTPTickerPriceInfo {
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    	///预留
    	int32_t unused;
    	///最新价
    	double  last_price;
    } XTPTPI;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 获取合约的最新价格信息
    virtual int QueryTickersPriceInfo(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    // 获取所有合约的最新价格信息
    virtual int QueryAllTickersPriceInfo(XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.22. OnSubscribeAllOptionMarketData ​

订阅全市场的期权行情快照应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：订阅合约发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 订阅全市场的期权行情
    virtual int SubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.23. OnUnSubscribeAllOptionMarketData ​

退订全市场的期权行情快照应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) { (void)exchange_id; (void)error_info; };

◇ 2.参数

exchange_id：表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场（不包括新三板），XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场，XTP_EXCHANGE_NQ表示新三板

error_info：取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 退订全市场的期权行情
    virtual int UnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.24. OnQueryAllTickersFullInfo ​

查询合约完整静态信息的应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryAllTickersFullInfo(XTPQFI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };

◇ 2.参数

ticker_info：合约完整静态信息

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询合约完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

cpp
    
    
    ///股票行情全量静态信息
    typedef struct XTPQuoteFullInfo {
    	XTP_EXCHANGE_TYPE  exchange_id;                    ///<交易所代码
    	XTP_SECURITY_TYPE  security_type;                  ///<合约详细类型
    	char    ticker[XTP_QUOTE_TICKER_LEN];              ///<证券代码
    	char    ticker_name[XTP_QUOTE_TICKER_NAME_LEN];    ///<证券名称
    	XTP_QUALIFICATION_TYPE ticker_qualification_class; ///<合约适当性类别
    	bool    is_registration;                           ///<是否注册制(仅适用创业板股票，创新企业股票及存托凭证)
    	bool    is_VIE;                                    ///<是否具有协议控制架构(仅适用创业板股票，创新企业股票及存托凭证)
    	bool    is_noprofit;                               ///<是否尚未盈利(仅适用创业板股票，创新企业股票及存托凭证)
    	bool    is_weighted_voting_rights;                 ///<是否存在投票权差异(仅适用创业板股票，创新企业股票及存托凭证)
    	bool    is_have_price_limit;                       ///<是否有涨跌幅限制(注：不提供具体幅度，可通过涨跌停价和昨收价来计算幅度)
    	char    unused[7];                                 ///预留
    	double  upper_limit_price;                         ///<涨停价（仅在有涨跌幅限制时有效）
    	double  lower_limit_price;                         ///<跌停价（仅在有涨跌幅限制时有效）
    	double  pre_close_price;                           ///<昨收价
    	double  price_tick;                                ///<价格最小变动价位
    	int32_t bid_qty_upper_limit;                       ///<限价买委托数量上限
    	int32_t bid_qty_lower_limit;                       ///<限价买委托数量下限
    	int32_t bid_qty_unit;                              ///<限价买数量单位
    	int32_t ask_qty_upper_limit;                       ///<限价卖委托数量上限
    	int32_t ask_qty_lower_limit;                       ///<限价卖委托数量下限
    	int32_t ask_qty_unit;                              ///<限价卖数量单位
    	int32_t market_bid_qty_upper_limit;                ///<市价买委托数量上限
    	int32_t market_bid_qty_lower_limit;                ///<市价买委托数量下限
    	int32_t market_bid_qty_unit;                       ///<市价买数量单位
    	int32_t market_ask_qty_upper_limit;                ///<市价卖委托数量上限
    	int32_t market_ask_qty_lower_limit;                ///<市价卖委托数量上限
    	int32_t market_ask_qty_unit;                       ///<市价卖数量单位
    	XTP_SECURITY_STATUS security_status;               ///<证券状态
    	uint32_t unknown1;                                 ///<保留字段
    	uint64_t unknown[3];                               ///<保留字段
    
    }XTPQFI;
    
    /////////////////////////////////////////////////////////////////////////
    ///@brief XTP_SECURITY_TYPE是一个证券详细分类枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t  XTP_SECURITY_TYPE;
    /// 主板股票
    constexpr uint32_t XTP_SECURITY_MAIN_BOARD = 0;
    /// 中小板股票
    constexpr uint32_t XTP_SECURITY_SECOND_BOARD = 1;
    /// 创业板股票
    constexpr uint32_t XTP_SECURITY_STARTUP_BOARD = 2;
    /// 指数
    constexpr uint32_t XTP_SECURITY_INDEX = 3;
    /// 科创板股票(上海)
    constexpr uint32_t XTP_SECURITY_TECH_BOARD = 4;
    /// 国债
    constexpr uint32_t XTP_SECURITY_STATE_BOND = 5;
    /// 企业债
    constexpr uint32_t XTP_SECURITY_ENTERPRICE_BOND = 6;
    /// 公司债
    constexpr uint32_t XTP_SECURITY_COMPANEY_BOND = 7;
    /// 转换债券
    constexpr uint32_t XTP_SECURITY_CONVERTABLE_BOND = 8;
    /// 国债逆回购
    constexpr uint32_t XTP_SECURITY_NATIONAL_BOND_REVERSE_REPO = 12;
    /// 本市场股票 ETF
    constexpr uint32_t XTP_SECURITY_ETF_SINGLE_MARKET_STOCK = 14;
    /// 跨市场股票 ETF
    constexpr uint32_t XTP_SECURITY_ETF_INTER_MARKET_STOCK = 15;
    /// 跨境股票 ETF
    constexpr uint32_t XTP_SECURITY_ETF_CROSS_BORDER_STOCK = 16;
    /// 本市场实物债券 ETF
    constexpr uint32_t XTP_SECURITY_ETF_SINGLE_MARKET_BOND = 17;
    /// 现金债券ETF
    constexpr uint32_t XTP_SECURITY_TYPE_ETF_CASH_BOND = 18;
    /// 黄金 ETF
    constexpr uint32_t XTP_SECURITY_ETF_GOLD = 19;
    /// 商品期货ETF
    constexpr uint32_t XTP_SECURITY_ETF_COMMODITY_FUTURES = 22;
    /// 上市开放式基金LOF
    constexpr uint32_t XTP_SECURITY_LOF = 23;
    /// 分级基金子基金
    constexpr uint32_t XTP_SECURITY_STRUCTURED_FUND_CHILD = 24;
    /// 深交所仅申赎基金
    constexpr uint32_t XTP_SECURITY_SZSE_RECREATION_FUND = 26;
    /// 个股期权
    constexpr uint32_t XTP_SECURITY_STOCK_OPTION = 29;
    /// ETF期权
    constexpr uint32_t XTP_SECURITY_ETF_OPTION = 30;
    /// REITs基金
    constexpr uint32_t XTP_SECURITY_REITS = 38;
    /// 配股
    constexpr uint32_t XTP_SECURITY_ALLOTMENT = 100;
    /// 上交所申赎型货币基金
    constexpr uint32_t XTP_SECURITY_MONETARY_FUND_SHCR = 110;
    /// 上交所交易型货币基金
    constexpr uint32_t XTP_SECURITY_MONETARY_FUND_SHTR = 111;
    /// 深交所货币基金
    constexpr uint32_t XTP_SECURITY_MONETARY_FUND_SZ = 112;
    /// 跨境LOF
    constexpr uint32_t XTP_SECURITY_LOF_CROSS_BORDER = 113;
    /// 其他
    constexpr uint32_t XTP_SECURITY_OTHERS = 255;
    
    ///@brief XTP_QUALIFICATION_TYPE是一个证券适当性枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t   XTP_QUALIFICATION_TYPE;
    ///<公众投资者，合格投资者与机构投资者均可
    constexpr uint32_t XTP_QUALIFICATION_PUBLIC = 0;
    ///<仅合格投资者与公众投资者      
    constexpr uint32_t XTP_QUALIFICATION_COMMON = 1;
    ///<仅限机构投资者
    constexpr uint32_t XTP_QUALIFICATION_ORGANIZATION = 2;
    ///<未知，期权等可能为此种类型
    constexpr uint32_t XTP_QUALIFICATION_UNKNOWN = 3;
    
    ///@brief XTP_SECURITY_STATUS是一个证券状态枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t   XTP_SECURITY_STATUS;
    ///< 风险警示板
    constexpr uint32_t XTP_SECURITY_STATUS_ST = 0;
    ///< 首日上市
    constexpr uint32_t XTP_SECURITY_STATUS_N_IPO = 1;
    ///< 普通
    constexpr uint32_t XTP_SECURITY_STATUS_COMMON = 2;
    ///< 恢复上市
    constexpr uint32_t XTP_SECURITY_STATUS_RESUME = 3;
    ///< 退市整理期
    constexpr uint32_t XTP_SECURITY_STATUS_DELISTING = 10;
    ///< 其他
    constexpr uint32_t XTP_SECURITY_STATUS_OTHERS = 255;
    
    /// 存放证券代码的字符串长度
    constexpr int32_t XTP_QUOTE_TICKER_LEN = 16;
    
    /// 存放证券名称的字符串长度
    constexpr int32_t XTP_QUOTE_TICKER_NAME_LEN = 64;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 获取所有合约的详细静态信息，包括指数等非可交易的
    virtual int QueryAllTickersFullInfo(XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.25. OnRequestRebuildQuote ​

请求回补指定行情的总体结果应答。

需要快速返回，仅在回补数据发送结束后调用，如果请求数据太多，一次性无法回补完，那么rebuild_result.result_code = XTP_REBUILD_RET_PARTLY，此时需要根据回补结果继续发起回补数据请求。

◇ 1.函数原型

cpp
    
    
    virtual void OnRequestRebuildQuote(XTPQuoteRebuildResultRsp* rebuild_result) { (void)rebuild_result; };

◇ 2.参数

rebuild_result：当回补结束时被调用，如果回补结果失败，则msg参数表示失败原因

cpp
    
    
    ///实时行情回补响应结构体
    typedef struct XTPQuoteRebuildResultRsp
    {
    	///请求id 请求包带过来的id
    	int32_t                     request_id;
    	///市场类型 上海 深圳
    	XTP_EXCHANGE_TYPE           exchange_id;
    	///总共返回的数据条数
    	uint32_t                    size;
    	///结果类型码
    	XTP_REBUILD_RET_TYPE        result_code;
    	///逐笔数据 通道号                
    	int16_t                     channel_number;
    	///预留
    	char                        unused[6];
    	///逐笔 表示序列号begin; 快照 表示时间begin(格式为YYYYMMDDHHMMSSsss)            
    	int64_t                     begin;
    	///逐笔 表示序列号end; 快照 表示时间end(格式为YYYYMMDDHHMMSSsss)
    	int64_t                     end;
    
    	///结果信息文本
    	char                        msg[64];
    }XTPQuoteRebuildResultRsp;

cpp
    
    
    ///@brief XTP_REBUILD_RET_TYPE 实时行情回补返回结果类型
    /////////////////////////////////////////////////////////////////////////
    typedef  uint32_t   XTP_REBUILD_RET_TYPE;
    ///<全部数据
    constexpr uint32_t XTP_REBUILD_RET_COMPLETE = 1;
    ///<部分数据
    constexpr uint32_t XTP_REBUILD_RET_PARTLY = 2;
    ///<没有数据
    constexpr uint32_t XTP_REBUILD_RET_NO_DATA = 3;
    ///<参数错误
    constexpr uint32_t XTP_REBUILD_RET_PARAM_ERR = 4;
    ///<请求频繁
    constexpr uint32_t XTP_REBUILD_RET_FREQUENTLY = 5;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    ///请求回补指定行情，包括快照和逐笔
    virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;

  


#### 4.3.26. OnRebuildTickByTick ​

回补的逐笔行情数据。

需要快速返回，此函数调用与OnTickByTick不在一个线程内，会在OnRequestRebuildQuote()之前回调。

◇ 1.函数原型

cpp
    
    
    virtual void OnRebuildTickByTick(XTPTBT *tbt_data) { (void)tbt_data; };

◇ 2.参数

tbt_data：回补的逐笔行情数据

cpp
    
    
    ///逐笔数据信息
    typedef struct XTPTickByTickStruct {
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    	///委托 or 成交
    	XTP_TBT_TYPE type;
    
    	/// SH: 业务序号（委托成交统一编号，同一个channel_no内连续）
    	/// SZ: 无意义
    	int64_t seq;
    	///委托时间 or 成交时间
    	int64_t data_time;
    
    	union {
    		XTPTickByTickEntrust   entrust;
    		XTPTickByTickTrade     trade;
    		XTPTickByTickStatus    state;
    	};
    } XTPTBT;
    
    ///@brief XTP_TBT_TYPE是一个逐笔回报类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TBT_TYPE;
    ///<逐笔委托
    constexpr uint32_t XTP_TBT_ENTRUST = 1;
    ///<逐笔成交
    constexpr uint32_t  XTP_TBT_TRADE = 2;
    ///<逐笔状态订单
    constexpr uint32_t  XTP_TBT_STATE = 3;
    
    ///逐笔委托
    struct XTPTickByTickEntrust {
    	///频道代码
    	int32_t channel_no;
    	///SH: 'B':买; 'S':卖
    	///SZ: '1':买; '2':卖; 'G':借入; 'F':出借
    	char    side;
    	///SH: 'A': 增加; 'D': 删除
    	///SZ: 订单类别: '1': 市价; '2': 限价; 'U': 本方最优
    	char    ord_type;
    	///预留
    	char    unused[2];
    	///SH: 委托序号(委托成交统一编号, 同一channel_no内连续)
    	///SZ: 委托序号(委托成交统一编号, 同一channel_no内连续)
    	int64_t seq;
    	///委托价格
    	double  price;
    	///SH: 剩余委托数量(balance)
    	///SZ: 委托数量
    	int64_t qty;
    	///SH: 原始订单号
    	///SZ: 无意义
    	int64_t order_no;
    
    	/// SH: 已成交的委托数量
    	/// SZ: 无意义
    	int64_t traded_qty;
    	};
    
    
    ///逐笔成交
    struct XTPTickByTickTrade {
    	///频道代码
    	int32_t channel_no;
    	/// SH: 内外盘标识('B':主动买; 'S':主动卖; 'N':未知)
    	/// SZ: 成交标识('4':撤; 'F':成交)
    	char    trade_flag;
    	///预留
    	char    unused[3];
    	///SH: 成交序号(委托单独编号, 同一channel_no内连续)
    	///SZ: 成交序号(委托成交统一编号, 同一channel_no内连续)
    	int64_t seq;
    	///成交价格
    	double  price;
    	///成交量
    	int64_t qty;
    	///成交金额(仅适用上交所)
    	double  money;
    	///买方订单号
    	int64_t bid_no;
    	///卖方订单号
    	int64_t ask_no;
    };
    
    ///逐笔状态订单
    struct XTPTickByTickStatus {
    	///频道代码
    	int32_t channel_no;
    	///预留1
    	int32_t unused1;
    	///同一channel_no内连续
    	int64_t seq;
    	///状态信息
    	char    flag[8];
    };

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    ///请求回补指定行情，包括快照和逐笔
    virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;

  


#### 4.3.27. OnRebuildMarketData ​

回补的快照行情数据。

需要快速返回，此函数调用与OnDepthMarketData不在一个线程内，会在OnRequestRebuildQuote()之前回调。

◇ 1.函数原型

cpp
    
    
    virtual void OnRebuildMarketData(XTPMD *md_data) { (void)md_data; };

◇ 2.参数

md_data：回补的快照行情数据

cpp
    
    
    ///行情
    typedef struct XTPMarketDataStruct
    {
    	// 代码
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    	/// 决定了union是哪种数据类型
    	XTP_MARKETDATA_TYPE_V2 data_type_v2;
    
    	// 价格
    	///最新价
    	double  last_price;
    	///昨收盘
    	double  pre_close_price;
    	///今开盘
    	double  open_price;
    	///最高价
    	double  high_price;
    	///最低价
    	double  low_price;
    	///今收盘
    	double  close_price;
    
    	// 期权数据
    	///昨日持仓量(张)(目前未填写)
    	int64_t pre_total_long_positon;
    	///持仓量(张)
    	int64_t total_long_positon;
    	///昨日结算价
    	double  pre_settl_price;
    	///今日结算价
    	double  settl_price;
    
    	// 涨跌停 
    	///SH:上交所涨跌停价赋值为0 
    	///涨停价
    	double  upper_limit_price;
    	///跌停价
    	double  lower_limit_price;
    	///预留
    	double  pre_delta;
    	///预留
    	double  curr_delta;
    
    	/// 时间类，格式为YYYYMMDDHHMMSSsss
    	int64_t data_time;
    
    	// 量额数据
    	///数量，为总成交量（单位股，与交易所一致）
    	int64_t qty;
    	///成交金额，为总成交金额（单位元，与交易所一致）
    	double  turnover;
    	///预留(无意义)
    	double  avg_price;
    
    	// 买卖盘
    	///十档申买价
    	double  bid[10];
    	///十档申卖价
    	double  ask[10];
    	///十档申买量
    	int64_t bid_qty[10];
    	///十档申卖量
    	int64_t ask_qty[10];
    
    	// 额外数据
    	///成交笔数
    	int64_t trades_count;
    	///当前交易状态说明，参见官网常见问题说明
    	char    ticker_status[8];
    	///数据
    	union {
    		XTPMarketDataStockExData  stk;
    		XTPMarketDataOptionExData opt;
    		XTPMarketDataBondExData  bond;
    	};
    	int64_t r1; // 预留字段,Rebuild查询md时为首次更新时间
    
    } XTPMD;
    
    ///股票、基金 等额外数据
    struct XTPMarketDataStockExData {
    	///委托买入总量(SH,SZ)
    	int64_t total_bid_qty;
    	///委托卖出总量(SH,SZ)
    	int64_t total_ask_qty;
    	///加权平均委买价格(SH,SZ)
    	double  ma_bid_price;
    	///加权平均委卖价格(SH,SZ)
    	double  ma_ask_price;
    	///债券加权平均委买价格(SH)
    	double  ma_bond_bid_price;
    	///债券加权平均委卖价格(SH)
    	double  ma_bond_ask_price;
    	///债券到期收益率(SH)
    	double  yield_to_maturity;
    	///基金实时参考净值(SH,SZ)
    	double  iopv;
    	///ETF申购笔数(SZ)
    	int32_t etf_buy_count;
    	///ETF赎回笔数(SZ)
    	int32_t etf_sell_count;
    	///ETF申购数量(SZ)
    	double  etf_buy_qty;
    	///ETF申购金额(SZ)
    	double  etf_buy_money;
    	///ETF赎回数量(SZ)
    	double  etf_sell_qty;
    	///ETF赎回金额(SZ)
    	double  etf_sell_money;
    	///权证执行的总数量(SH)
    	double  total_warrant_exec_qty;
    	///权证跌停价格（元）(SH)
    	double  warrant_lower_price;
    	///权证涨停价格（元）(SH)
    	double  warrant_upper_price;
    	///买入撤单笔数(SH)
    	int32_t cancel_buy_count;
    	///卖出撤单笔数(SH)
    	int32_t cancel_sell_count;
    	///买入撤单数量(SH)
    	double  cancel_buy_qty;
    	///卖出撤单数量(SH)
    	double  cancel_sell_qty;
    	///买入撤单金额(SH)
    	double  cancel_buy_money;
    	///卖出撤单金额(SH)
    	double  cancel_sell_money;
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
    	double  pre_iopv;
    	///预留
    	int64_t r1;
    	///预留
    	int64_t r2;
    };
    
    // 期权额外数据
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
    	double  ma_bid_price;
    	///加权平均委卖价格(SZ)
    	double  ma_ask_price;
    	///债券加权平均委买价格(SH)
    	double  ma_bond_bid_price;
    	///债券加权平均委卖价格(SH)
    	double  ma_bond_ask_price;
    	///债券到期收益率(SH)
    	double  yield_to_maturity;
    	///匹配成交最近价(SZ)
    	double  match_lastpx;
    	///债券加权平均价格(SH)
    	double  ma_bond_price;
    	///匹配成交成交量(SZ)
    	int64_t match_qty;
    	///匹配成交成交金额(SZ)
    	double  match_turnover;
    	///预留
    	double  r4;
    	///预留
    	double  r5;
    	///预留
    	double  r6;
    	///预留
    	double  r7;
    	///预留
    	double  r8;
    	///买入撤单笔数(SH)
    	int32_t cancel_buy_count;
    	///卖出撤单笔数(SH)
    	int32_t cancel_sell_count;
    	///买入撤单数量(SH)
    	double  cancel_buy_qty;
    	///卖出撤单数量(SH)
    	double  cancel_sell_qty;
    	///买入撤单金额(SH)
    	double  cancel_buy_money;
    	///卖出撤单金额(SH)
    	double  cancel_sell_money;
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
    	///时段(SHL2)
    	char    instrument_status[8];
    };
    
    ///@brief XTP_MARKETDATA_TYPE_V2是快照数据中的Union类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t  XTP_MARKETDATA_TYPE_V2;
    // 指数
    constexpr uint32_t XTP_MARKETDATA_V2_INDEX = 0;
    // 期权
    constexpr uint32_t XTP_MARKETDATA_V2_OPTION = 1;
    // 现货(股票/基金等)
    constexpr uint32_t XTP_MARKETDATA_V2_ACTUAL = 2;
    // 债券
    constexpr uint32_t XTP_MARKETDATA_V2_BOND = 3;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    ///请求回补指定行情，包括快照和逐笔
    virtual int RequestRebuildQuote(XTPQuoteRebuildReq* rebuild_param) = 0;

  


#### 4.3.28. OnQueryAllNQTickersFullInfo ​

查询新三板合约完整静态信息的应答。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryAllNQTickersFullInfo(XTPNQFI* ticker_info, XTPRI *error_info, bool is_last) { (void)ticker_info; (void)error_info; (void)is_last; };

◇ 2.参数

ticker_info：新三板合约完整静态信息

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

is_last：是否此次查询合约完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

cpp
    
    
    ///新三板全量静态信息
    typedef struct XTPQuoteNQFullInfo {
    	XTP_EXCHANGE_TYPE  exchange_id;                     ///<交易所代码
    	int32_t unused;                                     ///<预留
    	char    ticker[XTP_QUOTE_TICKER_LEN];               ///<证券代码
    	char    base_ticker[XTP_QUOTE_TICKER_LEN];          ///<基础证券
    	char    ticker_name[XTP_QUOTE_TICKER_NAME_LEN];     ///<证券名称
    	char    ticker_abbr_en[XTP_QUOTE_TICKER_NAME_LEN];  ///<英文简称
    	XTP_QUALIFICATION_TYPE ticker_qualification_class;  ///<合约适当性类别
    	XTP_SECURITY_TYPE      security_type;               ///<合约详细类型，目前均为255
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
    	double  price_gear;                                 ///<价格档位
    	double  first_limit_trans;                          ///<首笔交易限价参数
    	double  subsequent_limit_trans;                     ///<后续交易限价参数
    	double  limit_upper_price;                          ///<涨停价格
    	double  limit_lower_price;                          ///<跌停价格
    	double  block_trade_upper;                          ///<大宗交易价格上限(预留，默认0)
    	double  block_trade_lower;                          ///<大宗交易价格下限(预留，默认0)
    	double  convert_into_ration;                        ///<折合比例
    	XTP_TRADE_STATUS        trade_status : 8;           ///<交易状态
    	XTP_SECURITY_LEVEL      security_level : 8;         ///<证券级别
    	XTP_TRADE_TYPE          trade_type : 8;             ///<交易类型
    	XTP_SUSPEND_FLAG        suspend_flag : 8;           ///<停牌标志
    	XTP_EX_DIVIDEND_FLAG    ex_dividend_flag : 8;       ///<除权除息标志
    	XTP_SECURITY_LAYER_TYPE layer_type : 8;             ///<分层信息
    	char    reserved1[2];                               ///<保留字段
    	char    industry_type[6];                           ///<行业种类
    	char    currency_type[3];                           ///<货币种类
    	char    trade_places[3];                            ///<交易场所 预留
    	char    is_rzbd;                                    ///<是否融资标的 Y是 N否
    	char    is_rqbd;                                    ///<是否融券标的 Y是 N否
    	char    is_drrz;                                    ///<是否当日可融资 Y是 N否
    	char    is_drrq;                                    ///<是否当日可融券 Y是 N否
    	uint64_t unknown[3];                                ///<保留字段  
    }XTPNQFI;
    
    /////////////////////////////////////////////////////////////////////////
    ///@brief XTP_SECURITY_TYPE是一个证券详细分类枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t  XTP_SECURITY_TYPE;
    /// 主板股票
    constexpr uint32_t XTP_SECURITY_MAIN_BOARD = 0;
    /// 中小板股票
    constexpr uint32_t XTP_SECURITY_SECOND_BOARD = 1;
    /// 创业板股票
    constexpr uint32_t XTP_SECURITY_STARTUP_BOARD = 2;
    /// 指数
    constexpr uint32_t XTP_SECURITY_INDEX = 3;
    /// 科创板股票(上海)
    constexpr uint32_t XTP_SECURITY_TECH_BOARD = 4;
    /// 国债
    constexpr uint32_t XTP_SECURITY_STATE_BOND = 5;
    /// 企业债
    constexpr uint32_t XTP_SECURITY_ENTERPRICE_BOND = 6;
    /// 公司债
    constexpr uint32_t XTP_SECURITY_COMPANEY_BOND = 7;
    /// 转换债券
    constexpr uint32_t XTP_SECURITY_CONVERTABLE_BOND = 8;
    /// 国债逆回购
    constexpr uint32_t XTP_SECURITY_NATIONAL_BOND_REVERSE_REPO = 12;
    /// 本市场股票 ETF
    constexpr uint32_t XTP_SECURITY_ETF_SINGLE_MARKET_STOCK = 14;
    /// 跨市场股票 ETF
    constexpr uint32_t XTP_SECURITY_ETF_INTER_MARKET_STOCK = 15;
    /// 跨境股票 ETF
    constexpr uint32_t XTP_SECURITY_ETF_CROSS_BORDER_STOCK = 16;
    /// 本市场实物债券 ETF
    constexpr uint32_t XTP_SECURITY_ETF_SINGLE_MARKET_BOND = 17;
    /// 现金债券ETF
    constexpr uint32_t XTP_SECURITY_TYPE_ETF_CASH_BOND = 18;
    /// 黄金 ETF
    constexpr uint32_t XTP_SECURITY_ETF_GOLD = 19;
    /// 商品期货ETF
    constexpr uint32_t XTP_SECURITY_ETF_COMMODITY_FUTURES = 22;
    /// 上市开放式基金LOF
    constexpr uint32_t XTP_SECURITY_LOF = 23;
    /// 分级基金子基金
    constexpr uint32_t XTP_SECURITY_STRUCTURED_FUND_CHILD = 24;
    /// 深交所仅申赎基金
    constexpr uint32_t XTP_SECURITY_SZSE_RECREATION_FUND = 26;
    /// 个股期权
    constexpr uint32_t XTP_SECURITY_STOCK_OPTION = 29;
    /// ETF期权
    constexpr uint32_t XTP_SECURITY_ETF_OPTION = 30;
    /// REITs基金
    constexpr uint32_t XTP_SECURITY_REITS = 38;
    /// 配股
    constexpr uint32_t XTP_SECURITY_ALLOTMENT = 100;
    /// 上交所申赎型货币基金
    constexpr uint32_t XTP_SECURITY_MONETARY_FUND_SHCR = 110;
    /// 上交所交易型货币基金
    constexpr uint32_t XTP_SECURITY_MONETARY_FUND_SHTR = 111;
    /// 深交所货币基金
    constexpr uint32_t XTP_SECURITY_MONETARY_FUND_SZ = 112;
    /// 跨境LOF
    constexpr uint32_t XTP_SECURITY_LOF_CROSS_BORDER = 113;
    /// 其他
    constexpr uint32_t XTP_SECURITY_OTHERS = 255;
    
    ///@brief XTP_QUALIFICATION_TYPE是一个证券适当性枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t   XTP_QUALIFICATION_TYPE;
    ///<公众投资者，合格投资者与机构投资者均可
    constexpr uint32_t XTP_QUALIFICATION_PUBLIC = 0;
    ///<仅合格投资者与公众投资者      
    constexpr uint32_t XTP_QUALIFICATION_COMMON = 1;
    ///<仅限机构投资者
    constexpr uint32_t XTP_QUALIFICATION_ORGANIZATION = 2;
    ///<未知，期权等可能为此种类型
    constexpr uint32_t XTP_QUALIFICATION_UNKNOWN = 3;
    
    
    ///@brief XTP_TRADE_STATUS是一个交易状态枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t    XTP_TRADE_STATUS;
    ///< 未知状态
    constexpr uint8_t XTP_TRADE_STATUS_UNKNOW = 0;
    ///< 正常状态
    constexpr uint8_t XTP_TRADE_STATUS_N = 1;
    ///< 首日挂牌
    constexpr uint8_t XTP_TRADE_STATUS_Y = 2;
    ///< 新增股票挂牌交易
    constexpr uint8_t XTP_TRADE_STATUS_D = 3;
    ///< 询价
    constexpr uint8_t XTP_TRADE_STATUS_I = 4;
    ///< 申购
    constexpr uint8_t XTP_TRADE_STATUS_F = 5;
    
    ///@brief XTP_SECURITY_LEVEL是一个证券级别枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t  XTP_SECURITY_LEVEL;
    ///< 未知类型
    constexpr uint8_t XTP_SECURITY_LEVEL_UNKNOW = 0;
    ///< 挂牌公司股票
    constexpr uint8_t XTP_SECURITY_LEVEL_T = 1;
    ///< 两网公司及退市股票
    constexpr uint8_t XTP_SECURITY_LEVEL_B = 2;
    ///< 仅提供行权功能的期权
    constexpr uint8_t XTP_SECURITY_LEVEL_O = 3;
    ///< 持有人数存在200人限制的证券
    constexpr uint8_t XTP_SECURITY_LEVEL_P = 4;
    ///< 其他类型的业务
    constexpr uint8_t XTP_SECURITY_LEVEL_R = 5;
    ///< 发行业务
    constexpr uint8_t XTP_SECURITY_LEVEL_F = 6;
    
    ///@brief XTP_TRADE_TYPE是一个交易类型枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef  uint8_t   XTP_TRADE_TYPE;
    ///< 未知类型
    constexpr uint8_t XTP_TRADE_TYPE_UNKNOW = 0;
    ///< 协议交易方式
    constexpr uint8_t XTP_TRADE_TYPE_T = 1;
    ///< 做市交易方式
    constexpr uint8_t XTP_TRADE_TYPE_M = 2;
    ///< 集合竞价+连续交易方式
    constexpr uint8_t XTP_TRADE_TYPE_B = 3;
    ///< 集合竞价交易方式
    constexpr uint8_t XTP_TRADE_TYPE_C = 4;
    ///< 发行方式
    constexpr uint8_t XTP_TRADE_TYPE_P = 5;
    ///< 其他类型
    constexpr uint8_t XTP_TRADE_TYPE_O = 6;
    
    ///@brief XTP_SUSPEND_FLAG是一个停牌标志枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef  uint8_t  XTP_SUSPEND_FLAG;
    ///< 未知状态
    constexpr uint8_t XTP_SUSPEND_FLAG_UNKNOW = 0;
    ///< 正常交易
    constexpr uint8_t XTP_SUSPEND_FLAG_F = 1;
    ///< 停牌，不接受申报
    constexpr uint8_t XTP_SUSPEND_FLAG_T = 2;
    ///< 停牌，接受申报
    constexpr uint8_t XTP_SUSPEND_FLAG_H = 3;
    
    ///@brief XTP_EX_DIVIDEND_FLAG是一个除权除息标志枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef  uint8_t    XTP_EX_DIVIDEND_FLAG;
    ///< 未知状态
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_UNKNOW = 0;
    ///< 正常状态
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_N = 1;
    ///< 除权
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_E = 2;
    ///< 除息
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_D = 3;
    ///< 除权除息
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_A = 4;
    
    /// 存放证券代码的字符串长度
    constexpr int32_t XTP_QUOTE_TICKER_LEN = 16;
    
    /// 存放证券名称的字符串长度
    constexpr int32_t XTP_QUOTE_TICKER_NAME_LEN = 64;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 获取所有新三板合约的详细静态信息，包括指数等非可交易的
    virtual int QueryAllNQTickersFullInfo() = 0;

  


#### 4.3.29. OnETFIOPVData ​

ETF的IOPV通知，订阅ETF后调用。

◇ 1.函数原型

cpp
    
    
    virtual void OnETFIOPVData(IOPV *iopv) {};

◇ 2.参数

iopv: ETF的参考单位基金净值数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

cpp
    
    
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

◇ 3.返回

无

◇ 4.订阅函数

cpp
    
    
    // 订阅行情快照，包括股票、指数和期权
    virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    // 订阅全市场的股票行情快照
    virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.30. OnXTPQuoteNQFullInfo ​

新三板合约完整静态信息盘中推送通知,仅当订阅了新三板快照行情后会自动推送相关合约的静态信息。

◇ 1.函数原型

cpp
    
    
    virtual void OnXTPQuoteNQFullInfo(XTPNQFI* ticker_info) { (void)ticker_info; };

◇ 2.参数

ticker_info:合约完整静态信息

cpp
    
    
    ///新三板全量静态信息
    typedef struct XTPQuoteNQFullInfo {
    	XTP_EXCHANGE_TYPE  exchange_id;                     ///<交易所代码
    	int32_t unused;                                     ///<预留
    	char    ticker[XTP_QUOTE_TICKER_LEN];               ///<证券代码
    	char    base_ticker[XTP_QUOTE_TICKER_LEN];          ///<基础证券
    	char    ticker_name[XTP_QUOTE_TICKER_NAME_LEN];     ///<证券名称
    	char    ticker_abbr_en[XTP_QUOTE_TICKER_NAME_LEN];  ///<英文简称
    	XTP_QUALIFICATION_TYPE ticker_qualification_class;  ///<合约适当性类别
    	XTP_SECURITY_TYPE      security_type;               ///<合约详细类型，目前均为255
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
    	double  price_gear;                                 ///<价格档位
    	double  first_limit_trans;                          ///<首笔交易限价参数
    	double  subsequent_limit_trans;                     ///<后续交易限价参数
    	double  limit_upper_price;                          ///<涨停价格
    	double  limit_lower_price;                          ///<跌停价格
    	double  block_trade_upper;                          ///<大宗交易价格上限(预留，默认0)
    	double  block_trade_lower;                          ///<大宗交易价格下限(预留，默认0)
    	double  convert_into_ration;                        ///<折合比例
    	XTP_TRADE_STATUS        trade_status : 8;           ///<交易状态
    	XTP_SECURITY_LEVEL      security_level : 8;         ///<证券级别
    	XTP_TRADE_TYPE          trade_type : 8;             ///<交易类型
    	XTP_SUSPEND_FLAG        suspend_flag : 8;           ///<停牌标志
    	XTP_EX_DIVIDEND_FLAG    ex_dividend_flag : 8;       ///<除权除息标志
    	XTP_SECURITY_LAYER_TYPE layer_type : 8;             ///<分层信息
    	char    reserved1[2];                               ///<保留字段
    	char    industry_type[6];                           ///<行业种类
    	char    currency_type[3];                           ///<货币种类
    	char    trade_places[3];                            ///<交易场所 预留
    	char    is_rzbd;                                    ///<是否融资标的 Y是 N否
    	char    is_rqbd;                                    ///<是否融券标的 Y是 N否
    	char    is_drrz;                                    ///<是否当日可融资 Y是 N否
    	char    is_drrq;                                    ///<是否当日可融券 Y是 N否
    	uint64_t unknown[3];                                ///<保留字段  
    }XTPNQFI;
    
    /////////////////////////////////////////////////////////////////////////
    ///@brief XTP_SECURITY_TYPE是一个证券详细分类枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t  XTP_SECURITY_TYPE;
    /// 主板股票
    constexpr uint32_t XTP_SECURITY_MAIN_BOARD = 0;
    /// 中小板股票
    constexpr uint32_t XTP_SECURITY_SECOND_BOARD = 1;
    /// 创业板股票
    constexpr uint32_t XTP_SECURITY_STARTUP_BOARD = 2;
    /// 指数
    constexpr uint32_t XTP_SECURITY_INDEX = 3;
    /// 科创板股票(上海)
    constexpr uint32_t XTP_SECURITY_TECH_BOARD = 4;
    /// 国债
    constexpr uint32_t XTP_SECURITY_STATE_BOND = 5;
    /// 企业债
    constexpr uint32_t XTP_SECURITY_ENTERPRICE_BOND = 6;
    /// 公司债
    constexpr uint32_t XTP_SECURITY_COMPANEY_BOND = 7;
    /// 转换债券
    constexpr uint32_t XTP_SECURITY_CONVERTABLE_BOND = 8;
    /// 国债逆回购
    constexpr uint32_t XTP_SECURITY_NATIONAL_BOND_REVERSE_REPO = 12;
    /// 本市场股票 ETF
    constexpr uint32_t XTP_SECURITY_ETF_SINGLE_MARKET_STOCK = 14;
    /// 跨市场股票 ETF
    constexpr uint32_t XTP_SECURITY_ETF_INTER_MARKET_STOCK = 15;
    /// 跨境股票 ETF
    constexpr uint32_t XTP_SECURITY_ETF_CROSS_BORDER_STOCK = 16;
    /// 本市场实物债券 ETF
    constexpr uint32_t XTP_SECURITY_ETF_SINGLE_MARKET_BOND = 17;
    /// 现金债券ETF
    constexpr uint32_t XTP_SECURITY_TYPE_ETF_CASH_BOND = 18;
    /// 黄金 ETF
    constexpr uint32_t XTP_SECURITY_ETF_GOLD = 19;
    /// 商品期货ETF
    constexpr uint32_t XTP_SECURITY_ETF_COMMODITY_FUTURES = 22;
    /// 上市开放式基金LOF
    constexpr uint32_t XTP_SECURITY_LOF = 23;
    /// 分级基金子基金
    constexpr uint32_t XTP_SECURITY_STRUCTURED_FUND_CHILD = 24;
    /// 深交所仅申赎基金
    constexpr uint32_t XTP_SECURITY_SZSE_RECREATION_FUND = 26;
    /// 个股期权
    constexpr uint32_t XTP_SECURITY_STOCK_OPTION = 29;
    /// ETF期权
    constexpr uint32_t XTP_SECURITY_ETF_OPTION = 30;
    /// REITs基金
    constexpr uint32_t XTP_SECURITY_REITS = 38;
    /// 配股
    constexpr uint32_t XTP_SECURITY_ALLOTMENT = 100;
    /// 上交所申赎型货币基金
    constexpr uint32_t XTP_SECURITY_MONETARY_FUND_SHCR = 110;
    /// 上交所交易型货币基金
    constexpr uint32_t XTP_SECURITY_MONETARY_FUND_SHTR = 111;
    /// 深交所货币基金
    constexpr uint32_t XTP_SECURITY_MONETARY_FUND_SZ = 112;
    /// 跨境LOF
    constexpr uint32_t XTP_SECURITY_LOF_CROSS_BORDER = 113;
    /// 其他
    constexpr uint32_t XTP_SECURITY_OTHERS = 255;
    
    ///@brief XTP_QUALIFICATION_TYPE是一个证券适当性枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t   XTP_QUALIFICATION_TYPE;
    ///<公众投资者，合格投资者与机构投资者均可
    constexpr uint32_t XTP_QUALIFICATION_PUBLIC = 0;
    ///<仅合格投资者与公众投资者      
    constexpr uint32_t XTP_QUALIFICATION_COMMON = 1;
    ///<仅限机构投资者
    constexpr uint32_t XTP_QUALIFICATION_ORGANIZATION = 2;
    ///<未知，期权等可能为此种类型
    constexpr uint32_t XTP_QUALIFICATION_UNKNOWN = 3;
    
    
    ///@brief XTP_TRADE_STATUS是一个交易状态枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t    XTP_TRADE_STATUS;
    ///< 未知状态
    constexpr uint8_t XTP_TRADE_STATUS_UNKNOW = 0;
    ///< 正常状态
    constexpr uint8_t XTP_TRADE_STATUS_N = 1;
    ///< 首日挂牌
    constexpr uint8_t XTP_TRADE_STATUS_Y = 2;
    ///< 新增股票挂牌交易
    constexpr uint8_t XTP_TRADE_STATUS_D = 3;
    ///< 询价
    constexpr uint8_t XTP_TRADE_STATUS_I = 4;
    ///< 申购
    constexpr uint8_t XTP_TRADE_STATUS_F = 5;
    
    ///@brief XTP_SECURITY_LEVEL是一个证券级别枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t  XTP_SECURITY_LEVEL;
    ///< 未知类型
    constexpr uint8_t XTP_SECURITY_LEVEL_UNKNOW = 0;
    ///< 挂牌公司股票
    constexpr uint8_t XTP_SECURITY_LEVEL_T = 1;
    ///< 两网公司及退市股票
    constexpr uint8_t XTP_SECURITY_LEVEL_B = 2;
    ///< 仅提供行权功能的期权
    constexpr uint8_t XTP_SECURITY_LEVEL_O = 3;
    ///< 持有人数存在200人限制的证券
    constexpr uint8_t XTP_SECURITY_LEVEL_P = 4;
    ///< 其他类型的业务
    constexpr uint8_t XTP_SECURITY_LEVEL_R = 5;
    ///< 发行业务
    constexpr uint8_t XTP_SECURITY_LEVEL_F = 6;
    
    ///@brief XTP_TRADE_TYPE是一个交易类型枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef  uint8_t   XTP_TRADE_TYPE;
    ///< 未知类型
    constexpr uint8_t XTP_TRADE_TYPE_UNKNOW = 0;
    ///< 协议交易方式
    constexpr uint8_t XTP_TRADE_TYPE_T = 1;
    ///< 做市交易方式
    constexpr uint8_t XTP_TRADE_TYPE_M = 2;
    ///< 集合竞价+连续交易方式
    constexpr uint8_t XTP_TRADE_TYPE_B = 3;
    ///< 集合竞价交易方式
    constexpr uint8_t XTP_TRADE_TYPE_C = 4;
    ///< 发行方式
    constexpr uint8_t XTP_TRADE_TYPE_P = 5;
    ///< 其他类型
    constexpr uint8_t XTP_TRADE_TYPE_O = 6;
    
    ///@brief XTP_SUSPEND_FLAG是一个停牌标志枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef  uint8_t  XTP_SUSPEND_FLAG;
    ///< 未知状态
    constexpr uint8_t XTP_SUSPEND_FLAG_UNKNOW = 0;
    ///< 正常交易
    constexpr uint8_t XTP_SUSPEND_FLAG_F = 1;
    ///< 停牌，不接受申报
    constexpr uint8_t XTP_SUSPEND_FLAG_T = 2;
    ///< 停牌，接受申报
    constexpr uint8_t XTP_SUSPEND_FLAG_H = 3;
    
    ///@brief XTP_EX_DIVIDEND_FLAG是一个除权除息标志枚举类型
    /////////////////////////////////////////////////////////////////////////
    typedef  uint8_t    XTP_EX_DIVIDEND_FLAG;
    ///< 未知状态
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_UNKNOW = 0;
    ///< 正常状态
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_N = 1;
    ///< 除权
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_E = 2;
    ///< 除息
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_D = 3;
    ///< 除权除息
    constexpr uint8_t XTP_EX_DIVIDEND_FLAG_A = 4;
    
    /// 存放证券代码的字符串长度
    constexpr int32_t XTP_QUOTE_TICKER_LEN = 16;
    
    /// 存放证券名称的字符串长度
    constexpr int32_t XTP_QUOTE_TICKER_NAME_LEN = 64;

◇ 3.返回

无

◇ 4.订阅函数

cpp
    
    
    virtual int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;
    virtual int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id = XTP_EXCHANGE_UNKNOWN) = 0;

  


#### 4.3.31. OnQueryTickersLatestMarketData ​

查询合约的最新快照信息应答。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryTickersLatestMarketData(XTPMD* market_data, XTPRI *error_info, bool is_last) { (void)market_data; (void)error_info; (void)is_last; };

◇ 2.参数

market_data:合约的最新快照信息  
error_info:查询合约的最新快照信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误  
is_last:是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

cpp
    
    
    ///行情
    typedef struct XTPMarketDataStruct
    {
    	// 代码
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    	/// 决定了union是哪种数据类型
    	XTP_MARKETDATA_TYPE_V2 data_type_v2;
    
    	// 价格
    	///最新价
    	double  last_price;
    	///昨收盘
    	double  pre_close_price;
    	///今开盘
    	double  open_price;
    	///最高价
    	double  high_price;
    	///最低价
    	double  low_price;
    	///今收盘
    	double  close_price;
    
    	// 期权数据
    	///昨日持仓量(张)(目前未填写)
    	int64_t pre_total_long_positon;
    	///持仓量(张)
    	int64_t total_long_positon;
    	///昨日结算价
    	double  pre_settl_price;
    	///今日结算价
    	double  settl_price;
    
    	// 涨跌停 
    	///SH:上交所涨跌停价赋值为0 
    	///涨停价
    	double  upper_limit_price;
    	///跌停价
    	double  lower_limit_price;
    	///预留
    	double  pre_delta;
    	///预留
    	double  curr_delta;
    
    	/// 时间类，格式为YYYYMMDDHHMMSSsss
    	int64_t data_time;
    
    	// 量额数据
    	///数量，为总成交量（单位股，与交易所一致）
    	int64_t qty;
    	///成交金额，为总成交金额（单位元，与交易所一致）
    	double  turnover;
    	///预留(无意义)
    	double  avg_price;
    
    	// 买卖盘
    	///十档申买价
    	double  bid[10];
    	///十档申卖价
    	double  ask[10];
    	///十档申买量
    	int64_t bid_qty[10];
    	///十档申卖量
    	int64_t ask_qty[10];
    
    	// 额外数据
    	///成交笔数
    	int64_t trades_count;
    	///当前交易状态说明，参见官网常见问题说明
    	char    ticker_status[8];
    	///数据
    	union {
    		XTPMarketDataStockExData  stk;
    		XTPMarketDataOptionExData opt;
    		XTPMarketDataBondExData  bond;
    	};
    	int64_t r1; // 预留字段,Rebuild查询md时为首次更新时间
    
    } XTPMD;
    
    ///股票、基金 等额外数据
    struct XTPMarketDataStockExData {
    	///委托买入总量(SH,SZ)
    	int64_t total_bid_qty;
    	///委托卖出总量(SH,SZ)
    	int64_t total_ask_qty;
    	///加权平均委买价格(SH,SZ)
    	double  ma_bid_price;
    	///加权平均委卖价格(SH,SZ)
    	double  ma_ask_price;
    	///债券加权平均委买价格(SH)
    	double  ma_bond_bid_price;
    	///债券加权平均委卖价格(SH)
    	double  ma_bond_ask_price;
    	///债券到期收益率(SH)
    	double  yield_to_maturity;
    	///基金实时参考净值(SH,SZ)
    	double  iopv;
    	///ETF申购笔数(SZ)
    	int32_t etf_buy_count;
    	///ETF赎回笔数(SZ)
    	int32_t etf_sell_count;
    	///ETF申购数量(SZ)
    	double  etf_buy_qty;
    	///ETF申购金额(SZ)
    	double  etf_buy_money;
    	///ETF赎回数量(SZ)
    	double  etf_sell_qty;
    	///ETF赎回金额(SZ)
    	double  etf_sell_money;
    	///权证执行的总数量(SH)
    	double  total_warrant_exec_qty;
    	///权证跌停价格（元）(SH)
    	double  warrant_lower_price;
    	///权证涨停价格（元）(SH)
    	double  warrant_upper_price;
    	///买入撤单笔数(SH)
    	int32_t cancel_buy_count;
    	///卖出撤单笔数(SH)
    	int32_t cancel_sell_count;
    	///买入撤单数量(SH)
    	double  cancel_buy_qty;
    	///卖出撤单数量(SH)
    	double  cancel_sell_qty;
    	///买入撤单金额(SH)
    	double  cancel_buy_money;
    	///卖出撤单金额(SH)
    	double  cancel_sell_money;
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
    	double  pre_iopv;
    	///预留
    	int64_t r1;
    	///预留
    	int64_t r2;
    };
    
    // 期权额外数据
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
    	double  ma_bid_price;
    	///加权平均委卖价格(SZ)
    	double  ma_ask_price;
    	///债券加权平均委买价格(SH)
    	double  ma_bond_bid_price;
    	///债券加权平均委卖价格(SH)
    	double  ma_bond_ask_price;
    	///债券到期收益率(SH)
    	double  yield_to_maturity;
    	///匹配成交最近价(SZ)
    	double  match_lastpx;
    	///债券加权平均价格(SH)
    	double  ma_bond_price;
    	///匹配成交成交量(SZ)
    	int64_t match_qty;
    	///匹配成交成交金额(SZ)
    	double  match_turnover;
    	///预留
    	double  r4;
    	///预留
    	double  r5;
    	///预留
    	double  r6;
    	///预留
    	double  r7;
    	///预留
    	double  r8;
    	///买入撤单笔数(SH)
    	int32_t cancel_buy_count;
    	///卖出撤单笔数(SH)
    	int32_t cancel_sell_count;
    	///买入撤单数量(SH)
    	double  cancel_buy_qty;
    	///卖出撤单数量(SH)
    	double  cancel_sell_qty;
    	///买入撤单金额(SH)
    	double  cancel_buy_money;
    	///卖出撤单金额(SH)
    	double  cancel_sell_money;
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
    	///时段(SHL2)
    	char    instrument_status[8];
    };
    
    ///@brief XTP_MARKETDATA_TYPE_V2是快照数据中的Union类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t  XTP_MARKETDATA_TYPE_V2;
    // 指数
    constexpr uint32_t XTP_MARKETDATA_V2_INDEX = 0;
    // 期权
    constexpr uint32_t XTP_MARKETDATA_V2_OPTION = 1;
    // 现货(股票/基金等)
    constexpr uint32_t XTP_MARKETDATA_V2_ACTUAL = 2;
    // 债券
    constexpr uint32_t XTP_MARKETDATA_V2_BOND = 3;

◇ 3.返回

无

◇ 4.订阅接口

cpp
    
    
    virtual int QueryTickersLatestMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) = 0;

  


#### 4.3.32. OnSubscribeAllIndexPress ​

订阅指数通行情应答.

◇ 1.函数原型

cpp
    
    
    virtual void OnSubscribeAllIndexPress(XTPRI *error_info) { (void)error_info; };

◇ 2.参数  
error_info:订阅指数通时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误.

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    virtual int SubscribeAllIndexPress() = 0;

  


#### 4.3.33. OnUnSubscribeAllIndexPress ​

取消订阅指数通行情应答。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnSubscribeAllIndexPress(XTPRI *error_info) { (void)error_info; };

◇ 2.参数  
error_info:订阅指数通时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误.

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    virtual int UnSubscribeAllIndexPress() = 0;

  


#### 4.3.34. OnIndexPress ​

指数通行情通知。

◇ 1.函数原型

cpp
    
    
    virtual void OnIndexPress(XTPIndexPress *idx) { (void)idx; };

◇ 2.参数  
idx:指数通的行情数据。行情数据类型如下：

cpp
    
    
    ///上海指数通快照行情
    typedef struct XTPIndexPress {
    
    	// 代码
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码(无意义)
    	XTP_EXCHANGE_TYPE exchange_id;
    	///数据来源, 7=指数通.
    	char    data_source;
    	char    unused[3];
    
    	/// 时间类，格式为YYYYMMDDHHMMSSsss
    	int64_t data_time;
    
    	// 价格
    	///最新价
    	double  last_price;
    	///昨收盘
    	double  pre_close_price;
    	///今开盘
    	double  open_price;
    	///最高价
    	double  high_price;
    	///最低价
    	double  low_price;
    	///今收盘
    	double  close_price;
    
    
    	// 量额数据
    	///总成交量
    	int64_t qty;
    	///总成交金额
    	double  turnover;
    	///成交笔数
    	int64_t trades_count;
    }XTPIP;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    virtual int SubscribeAllIndexPress() = 0;

  


#### 4.3.35. OnSubscribeAllHKCMarketData ​

订阅港股通行情应答。

◇ 1.函数原型

cpp
    
    
    virtual void OnSubscribeAllHKCMarketData(XTPRI *error_info) { (void)error_info; };

◇ 2.参数  
error_info:订阅港股通时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误.

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    virtual int SubscribeAllHKCMarketData() = 0;

  


#### 4.3.36. OnUnSubscribeAllHKCMarketData ​

取消订阅港股通行情应答。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnSubscribeAllHKCMarketData(XTPRI *error_info) { (void)error_info; };

◇ 2.参数  
error_info:取消订阅港股通时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误.

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    virtual int UnSubscribeAllHKCMarketData() = 0;

  


#### 4.3.37. OnHKRLData ​

港股通实时额度通知。

◇ 1.函数原型

cpp
    
    
    virtual void OnHKRLData(XTPHKCRL *hkc_data) { (void)hkc_data; };

◇ 2.参数  
hkc_data：港股通实时额度数据。 相关数据字段如下：

cpp
    
    
    ///港股通实时额度
    typedef struct XTPHKCRealtimeLimit {
    	/// 时间类，格式为YYYYMMDDHHMMSSsss
    	int64_t data_time;
    
    	/// 市场代码
    	char    market_id[8];
    	/// 市场板块代码,预留
    	char    market_segment_id[8];
    
    	/// 每日初始额度
    	int64_t threshold_amount;
    	/// 日中剩余额度
    	int64_t pos_amt;
    	/// 额度状态: 
    	/// 1=额度不可用; pos_amt = 0.0000
    	/// 2=额度可用(额度可用且低于当日初始额度的30%时); pos_amt = 当前实际剩余额度
    	/// 3=额度充足(额度可用且大于或等于当日初始额度的30%时); pos_amt = 0.0000
    	char    amount_status;
    	char    unused[7];
    } XTPHKCRL;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    virtual int SubscribeAllHKCMarketData() = 0;

  


#### 4.3.38. OnHKCMarketData ​

港股通行情通知。

◇ 1.函数原型

cpp
    
    
    virtual void OnHKCMarketData(XTPHKCMD *hkc_md) { (void)hkc_md; };

◇ 2.参数  
hkc_md:港股通的行情数据,相关的数据字段如下：

cpp
    
    
    ///深交所港股通快照行情
    typedef struct XTPHKCMarketdata {
    	// 代码
    	///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    	char    ticker[XTP_QUOTE_TICKER_LEN];
    	///交易所代码
    	XTP_EXCHANGE_TYPE exchange_id;
    	///预留
    	int32_t unused;
    
    	/// 时间类，格式为YYYYMMDDHHMMSSsss
    	int64_t data_time;
    	///当前交易状态说明
    	char    ticker_status[8];
    
    	///成交笔数
    	int64_t trades_count;
    	///数量，为总成交量（单位股，与交易所一致）
    	int64_t qty;
    	///成交金额，为总成交金额（单位元，与交易所一致）
    	double  turnover;
    
    	///涨停价
    	double  upper_limit_price;
    	///跌停价
    	double  lower_limit_price;
    
    	// 价格
    	///最新价
    	double  last_price;
    	///昨收盘
    	double  pre_close_price;
    	///参考价
    	double  ref_price;
    	///最高价
    	double  high_price;
    	///最低价
    	double  low_price;
    	///按盘价/盘后为今收价
    	double  nominal_price;
    
    	///买盘上限价 如果处于开盘集合竞价时段，则表示开盘竞价时段的买盘价格上限
    	double  bid_upper_price;
    	///买盘下限价 如果处于开盘集合竞价时段，则表示开盘竞价时段的买盘价格下限
    	double  bid_lower_price;
    	///卖盘上限价 如果处于开盘集合竞价时段，则表示开盘竞价时段的卖盘价格上限
    	double  ask_upper_price;
    	///卖盘下限价 如果处于开盘集合竞价时段，则表示开盘竞价时段的卖盘价格下限
    	double  ask_lower_price;
    
    	///冷静期开始时间 大于0表示当前处于触发VCM的冷静期
    	int64_t complex_event_start_time;
    	///冷静期结束时间 大于0表示当前处于触发VCM的冷静期
    	int64_t complex_event_end_time;
    
    	// 买卖盘
    	///十档申买价
    	double  bid[10];
    	///十档申卖价
    	double  ask[10];
    	///十档申买量
    	int64_t bid_qty[10];
    	///十档申卖量
    	int64_t ask_qty[10];
    } XTPHKCMD;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    virtual int SubscribeAllHKCMarketData() = 0;

  


#### 4.3.39. OnQueryAllHKCInfo ​

查询港股通完整静态信息的应答。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryAllHKCInfo(XTPHKCSI* hkcsi, XTPRI *error_info, bool is_last) { (void)hkcsi; (void)error_info; (void)is_last; };

◇ 2.参数

hkcsi:港股通静态信息，相关字段如下：

cpp
    
    
    // 港股通静态信息
    typedef struct XTPHKCStaticInfo {
    	char    ticker[XTP_QUOTE_TICKER_LEN];               ///<证券代码
    	char    ticker_name[XTP_QUOTE_TICKER_NAME_LEN];     ///<证券名称
    	XTP_EXCHANGE_TYPE exchange_id;                      ///<交易所代码(XTP_EXCHANGE_HK)
    	char    unknown[4];                                 ///<预留
    } XTPHKCSI;

error_info:查询港股通完整静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误.

is_last:是否此次查询港股通完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应.

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    ///获取港股通的静态信息
    virtual int QueryAllHKCInfo() = 0;

  


#### 4.3.40. OnQueryAllIndexPressInfo ​

查询指数通完整静态信息的应答.

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryAllIndexPressInfo(XTPIPSI* ipsi, XTPRI *error_info, bool is_last) { (void)ipsi; (void)error_info; (void)is_last; };

◇ 2.参数

ipsi:指数通完整静态信息,相关字段如下：

cpp
    
    
    // 指数通静态信息
    typedef struct XTPIndexPressStaticInfo {
    	char    ticker[XTP_QUOTE_TICKER_LEN];               ///<证券代码
    	char    ticker_name[XTP_QUOTE_TICKER_NAME_LEN];     ///<证券名称
    	XTP_QUOTE_MKT_CODE_TYPE market_code;                ///<市场代码
    	char    unknown[7];                                 ///<预留
    } XTPIPSI;

error_info:查询指数通完整静态信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误.

is_last:是否此次查询指数通完整静态信息的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应.

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    ///获取指数通的静态信息
    virtual int QueryAllIndexPressInfo() = 0;

  


## **5\. 交易接口** ​

### 5.1. 交易接口简介 ​

#### 5.1.1. 说明 ​

交易API提供了两个接口，分别为TraderApi和TraderSpi。客户端应用程序可以通过TraderApi发出操作请求，通过继承TraderSpi并重写回调函数来处理后台服务的响应。

交易API在运行过程中，会将日志写入本地文件中。函数CreateTraderApi的第二个参数指明日志文件的路径。若路径不存在会自动创建于系统账户目录。

注意以下事项：

在TraderSpi派生类的回调函数中应及时返回，不要阻塞。

API请求的返回参数，一般是0表示正确，其他表示错误，具体见接口详情。详细错误编码请至官网查阅错误列表。

#### 5.1.2. 代码示例 ​

下面通过一个简单的代码示例，来快速了解下交易API的使用方法。该示例演示了API的初始化、订阅公共流、登录交易系统和报单等过程。

◇ 1.源代码 以下是MyTraderSpi.h文件

cpp
    
    
    #include "xtpx_trader_api.h"
    
    using namespace XTPX::API;
    
    class MyTraderSpi : public TraderSpi
    {
    public:
    	explicit MyTraderSpi();
    	~MyTraderSpi();
        
    	void OnOrderAck(XTPOrderInfo *order_info, uint64_t session_id);
    	// 查询报单响应
    	void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id);
    	// 报单通知
    	void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id);
    	// 成交通知
    	void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id);
    };

以下是MyTraderSpi.cpp文件

cpp
    
    
    #include "MyTraderSpi.h"
    #include <iostream>
    
    MyTraderSpi::MyTraderSpi() { }
    MyTraderSpi::~MyTraderSpi() { }
    
    //报单初始状态通知
    void MyTraderSpi::OnOrderAck(XTPOrderInfo *order_info, uint64_t session_id)
    {
    	std::cout << "OnOrderAck." << std::endl;
    }
    // 查询报单响应
    void MyTraderSpi::OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id)
    {
    	std::cout << "OnQueryOrder." << std::endl;
    }
    
    // 报单通知
    void MyTraderSpi::OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id)
    {
    	std::cout << "OnOrderEvent." << std::endl;
    }
    
    // 成交通知
    void MyTraderSpi::OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id)
    {
    	std::cout << "OnTradeEvent." << std::endl;
    }

以下是MyTraderApi.h文件

cpp
    
    
    #include "xtpx_trader_api.h"
    #include "MyTraderSpi.h"
    
    using namespace XTPX::API;
    
    class MyTraderApi
    {
    public:
    	explicit MyTraderApi();
    	~MyTraderApi();
    
    	// 初始化
    	bool initialize();
    	// 释放
    	void release();
    	// 登录
    	uint64_t login();
    	// 报单
    	void insertOrder();
    	// 查询报单
    	void queryOrders();
    
    private:
    	TraderApi *user_trade_api_;
    	MyTraderSpi *m_trader_spi;
    
    	uint64_t session_id_;
    };

以下是MyTraderApi.cpp文件

cpp
    
    
    #include "MyTraderApi.h"
    #include <iostream>
    #include <string>
    
    MyTraderApi::MyTraderApi()
    {
        user_trade_api_ = nullptr;
        m_trader_spi = nullptr;
    
        session_id_ = 0;
    }
    
    MyTraderApi::~MyTraderApi()
    {
    	if (user_trade_api_ != NULL) {
            user_trade_api_->Logout(session_id_)
        }
    }
    
    bool MyTraderApi::initialize()
    {
    	// 创建并初始化交易API
    	user_trade_api_ = XTPX::API::TraderApi::CreateTraderApi(1, "./", XTP_LOG_LEVEL_DEBUG);
    	if (user_trader_api_)
    	{
    		// 注册回调接口
    		m_trader_spi = new MyTraderSpi();
    		user_trade_api_->RegisterSpi(m_trader_spi);
    		// 登录前参数设置
    		user_trade_api_->SetHeartBeatInterval(15);
    		user_trade_api_->SetSoftwareKey("xxxxxxxxxx");
    		user_trade_api_->SetSoftwareVersion("xx.xx.xx.xx");
    		// 设置公有流（订单响应、成交回报）重传方式
    		user_trade_api_->SubscribePublicTopic(XTP_TERT_QUICK);
    
    		return true;
    	}
    	return false;
    }
    
    // 释放
    void MyTraderApi::release()
    {
    	if (user_trade_api_ != NULL) {
            user_trade_api_->Logout(session_id_);
        }
    }
    
    // 登录
    uint64_t MyTraderApi::login()
    {
    	std::string trade_server_ip = "xxx.xxx.xxx.xxx";
    	int trade_server_port = xxxx;
    	std::string account_name = "xxxxxxxx";
    	std::string account_pw = "xxxxxx";
    	std::string local_ip = "xxx.xxx.xxx.xxx";//根据本地网卡对应的ip设定
    
    	uint64_t ret = user_trade_api_->Login(trade_server_ip.c_str(), trade_server_port, account_name.c_str(), account_pw.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str());
    	if (0 != ret) // 登录成功
    	{
    		session_id_ = ret;
    	}
    	else // 登录失败
    	{
    		XTPRI* error_info = user_trader_api_->GetApiLastError();
    		std::cout << "login to server error, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
    	}
    	return ret;
    }
    
    //报单
    void MyTraderApi::insertOrder()
    {
    	uint64_t order_xtp_id_ = 0;
    	XTPOrderInsertInfo order;
    	memset(&order, 0, sizeof(XTPOrderInsertInfo));
    
    	order.market = XTP_MKT_SH_A;
    	std::string stdstr_ticker = "600000";
    	strncpy(order.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
    	order.business_type = XTP_BUSINESS_TYPE_CASH;
    	order.side = XTP_SIDE_BUY;
    	order.position_effect = XTP_POSITION_EFFECT_INIT;
    	order.price_type = XTP_PRICE_LIMIT;
    	order.price = 9.01;
    	order.quantity = 1000;
    	std::string stdstr_accountid = "AXXXXXXXXX";
    	strncpy(order.account_id, stdstr_accountid.c_str(), XTP_ACCOUNT_ID_LEN);//order.account_id可以不填，默认以主股卡报送
    
    	uint64_t ret = user_trade_api_->InsertOrder(&order,session_id_);
    	if (ret != 0)
    	{
    		// 报单成功会返回的order_xtp_id，它保证一个交易日内唯一
    		order_xtp_id_ = ret;
    	}
    	else
    	{
    		// 报单失败，获取失败原因
    		XTPRI* error_info = user_trade_api_->GetApiLastError();
    		std::cout << "Insert order error, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
    	}
    }
    
    // 查询报单
    void MyTraderApi::queryOrders()
    {
    	XTPQueryOrderReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryOrderReq));
    
    	std::string stdstr_ticker = "600000";
    	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
    	query_param.begin_time = 20210801000000000;
    	query_param.end_time = 20210801150000000;
    
    	int ret = user_trade_api_->QueryOrders(&query_param, session_id_, request_id);
    }

以下是main.cpp文件

cpp
    
    
    #include <iostream>
    #include "MyTraderApi.h"
    #ifdef _WIN32
    	#include <windows.h>
    #else
    	#include <unistd.h>
    #endif
    
    using namespace std;
    
    int main(int argc, char *argv[])
    {
    	MyTraderApi *pTraderApi = new MyTraderApi;
    
    	if (pTraderApi)
    	{
    		bool b_ret = pTraderApi->initialize();
    		if (! b_ret)
    		{
    			// 初始化失败程序退出
    			return -1;
    		}
    		uint64_t ret = pTraderApi->login();
    		if (ret != 0)
    		{
    			pTraderApi->insertOrder();
    		}
    		
    		//主线程循环，防止进程退出
    		while (true)
    		{
    #ifdef _WIN32
    			Sleep(1000);
    #else
    			sleep(1);
    #endif
    		}
    	}
    	
    	return 0;
    }

◇ 2.代码说明

◇ 2.1.继承TraderSpi类

代码一开始通过#include "xtpx_trader_api.h"，将xtpxtraderapi.lib中声明的类和数据类型包括进来，该头文件中有两个重要的基类：TraderSpi和TraderApi。

TraderSpi类提供了交易相关的回调接口，用户需要继承该类并重写这些接口，以获取响应数据。

TraderApi类则是提供了交易相关功能的请求接口，例如查询请求、报单请求、撤单请求等。

我们声明了一个MyTraderSpi类，该类正是继承了TraderSpi类，并且重写了OnOrderEvent、OnTradeEvent、OnQueryOrder等接口。通过这些回调返回的数据，我们可以得知当前业务处理的结果或者获取我们想要的业务数据，进一步实现自己的业务逻辑。

我们声明了一个包含TraderApi类型的变量user_trade_api_，后续我们会实例化它，以便我们使用tradeapi提供的登录、报单和查询等功能。

◇ 2.2.初始化

方法（initialize）里，实现了线程的初始化，步骤为：

Step 1 通过（CreateTraderApi）方法创建一个traderapi的实例。

Step 2 创建一个traderspi的实例，向traderapi的实例注册（RegisterSpi）。

Step 3 设置登录操作前的必要参数，包括设置软件开发版本号，软件开发Key，心跳检测时间间隔，公共流订阅模式等。

将自己定义的继承了Spi类的MyTraderSpi实例注册给TraderApi，这样API就能将收到的各种数据通过Spi类的接口回调给用户。

公共流订阅仅能选择QUICK和RESTART两种方式，用户收到的数据会根据用户的选择方式而定，区别在于是否接收登录前的订单响应和成交回报。必须在Login方法前调用，不调用则默认使用QUICK模式，即只接收登录后的推送消息。

调用（initialize）方法开始初始化api，也就是说前面的工作只是准备工作，到了这里api才真正开始工作。此时api会按照之前设置的公共流订阅方式接收来自服务端的数据。

方法（initialize）和方法（release）不是线程安全的，多线程使用需要加锁。

完成以上步骤后，客户端就已经和API建立了连接。

如果成功建立连接，我们就可以调用各种API接口完成业务需求。

◇ 2.3.释放api线程

方法（release）释放了api线程，释放后api资源会被回收，并且与API断开连接。

◇ 2.4.登录

ip、port、user、password都是必要字段。登录（Login）指令是同步函数。通过返回值可以判断是否连接成功，非0表示成功，其他则表示失败，具体可以参考接口Login。可以在Login失败后调用GetApiLastError函数，获取失败的原因。

注意：除了登录接口返回会话ID表示登录成功外，其他请求接口返回0不表示请求成功，而是仅仅表示api指令发出去了。建议在实际应用中做好超时重发机制，以便在网络丢包的情况下能够及时重发指令。

对于api用户来说，如果同一用户有多个同时在线的会话，需要不同client_id，否则不予登录。登录接口返回的session_id对于单个进程来说是不同的，但是多个进程之间是可能相同的。

注意：如果重启api后调用login登录，那么登录成功返回的session_id可能会跟之前的一样；如果收到断线通知OnDisconnected，在不没有销毁api的情况下，直接重连，那么重新login登录成功返回的session_id会不同。

◇ 2.5.报单

报入一笔限价单，以9.01的价格买入沪市"600000"的普通交易，数量1000。

注意，报单成功会返回报单在XTP系统中的ID，用户需要记录下返回的order_xtp_id，它保证一个交易日内唯一。

若报单填错了字段，或者客户资金不足报单指令发出后会被XTP拒绝。拒单会触发回调函数（OnOrderEvent），返回报单拒绝的消息和原因。

若oms服务器接收订单，会在回调函数OnOrderAck()里收到初始状态的通知，但不代表已经报送到交易所。若交易所收到订单，报单回调会在报单响应函数OnOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（包括订单未成交、全部成交、全部撤单、部分撤单、已拒绝，除了部成状态）都会通过报单响应函数OnOrderEvent()返回。所有登录了此用户的客户端都将收到此用户的订单响应。

若订单有成交发生，会通过OnTradeEvent返回成交单详情。若相关订单为部成状态，需要用户通过成交回报的成交数量来确定，OnOrderEvent()不会推送部成状态。所有登录了此用户的客户端都将收到此用户的成交回报。

◇ 2.6.查询合约

请求查询合约信息。对于大部分查询接口，如果请求信息填空，则会返回所有的记录；但是也有例外，部分请求必须指定合约，可以参考对应的接口说明。

◇ 2.7.程序运行流程

首先初始化user_trader_api_类。调用initialize函数开始连接服务端，执行登录，报单等操作。

### 5.2. TraderApi ​

TraderApi类提供了交易api的初始化、登录、报单等功能。

#### 5.2.1. 接口 ​

cpp
    
    
    namespace XTPX {
    	namespace API {
    
    		class XTPX_TRADER_API_EXPORT TraderApi
    		{
    		public:
    			///创建TraderApi
    			///@param client_id （必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义，总体取值区间[1,127]，普通用户取值区间[1,24]
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
    			///@remark 此函数为同步阻塞式，不需要异步等待登出，当函数返回即可进行后续操作，不允许在回调线程调用。
    			virtual int Logout(uint64_t session_id) = 0;
    
    // 			///服务器是否重启过
    // 			///@return “true”表示重启过，“false”表示没有重启过
    // 			///@param session_id 资金账户对应的session_id,登录时得到
    // 			///@remark 此函数必须在Login之后调用
    // 			virtual bool IsServerRestart(uint64_t session_id) = 0;
    // 
    // 			///修改已登录用户的硬件信息，仅限授权系统使用
    // 			///@return 发送消息是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    // 			///@param info 需要修改成的用户硬件信息
    // 			///@param session_id 资金账户对应的session_id,登录时得到
    // 			///@remark 此函数必须在Login之后调用，且仅限授权系统使用，一般客户无需使用
    // 			virtual int ModifyUserTerminalInfo(const XTPUserTerminalInfoReq* info, uint64_t session_id) = 0;
    
    			///查询用户在本节点上的可交易市场类型
    			///@return 按位来看，从低位开始数，第0位表示沪市，即如果(trade_location&0x01) == 0x01，代表可交易沪市，第1位表示深市，即如果(trade_location&0x02) == 0x02，表示可交易深市，如果第0位和第1位均是1，即(trade_location&(0x01|0x02)) == 0x03，就表示可交易沪深2个市场
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@remark 此函数必须在Login之后调用，为同步函数
    			virtual uint32_t GetAccountTradeMarket(uint64_t session_id) = 0;
    
    			///为用户获取一个新的订单XTPID，用于报单
    			///@return 生成的订单XTPID，非“0”表示获取成功，“0”表示获取失败，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@remark 此函数必须在Login之后调用，通过这个函数获取的order_xtp_id仅用于对应的用户报单，如果设置错误，将会导致下单失败
    			virtual uint64_t GetANewOrderXTPID(uint64_t session_id) = 0;
    
    			///获取用户分页查询允许的最大查询数量
    			///@return 分页查询允许的最大查询数量req_count，非“0”表示获取成功，“0”表示获取失败，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@remark 此函数必须在Login之后调用，通过这个函数获取的req_count可用于用户进行分页查询请求的填写，如果填写错误，将会导致分页查询接口调用失败
    			virtual int64_t GetMaxReqNumOfPagedQuery(uint64_t session_id) = 0;
    
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
    
    			///根据报单ID请求查询报单
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param order_xtp_id 需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 该方法不受查询服务是否可用影响
    			virtual int QueryOrderByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
    
    			///请求查询报单
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
    			virtual int QueryOrders(const XTPQueryOrderReq *query_param, uint64_t session_id, int request_id) = 0;
    
    			///请求查询未完结报单
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			virtual int QueryUnfinishedOrders(uint64_t session_id, int request_id) = 0;
    
    			///分页请求查询报单
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
    			virtual int QueryOrdersByPage(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
    
    // 			///根据报单ID请求查询报单
    // 			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    // 			///@param order_xtp_id 需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id
    // 			///@param session_id 资金账户对应的session_id，登录时得到
    // 			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    // 			virtual int QueryOrderByXTPIDEx(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
    
    // 			///请求查询报单
    // 			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    // 			///@param query_param 需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    // 			///@param session_id 资金账户对应的session_id，登录时得到
    // 			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    // 			///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
    // 			virtual int QueryOrdersEx(const XTPQueryOrderReq *query_param, uint64_t session_id, int request_id) = 0;
    
    // 			///请求查询未完结报单
    // 			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    // 			///@param session_id 资金账户对应的session_id，登录时得到
    // 			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    // 			virtual int QueryUnfinishedOrdersEx(uint64_t session_id, int request_id) = 0;
    
    // 			///分页请求查询报单-新版本接口
    // 			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    // 			///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
    // 			///@param session_id 资金账户对应的session_id，登录时得到
    // 			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    // 			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
    // 			virtual int QueryOrdersByPageEx(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
    
    			///根据委托编号请求查询相关成交
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param order_xtp_id 需要查询的委托编号，即InsertOrder()成功时返回的order_xtp_id
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 此函数查询出的结果可能对应多个查询结果响应
    			virtual int QueryTradesByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
    
    			///请求查询已成交
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 需要查询的成交回报筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有成交回报，否则查询时间段内所有跟股票代码相关的成交回报，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
    			virtual int QueryTrades(XTPQueryTraderReq *query_param, uint64_t session_id, int request_id) = 0;
    
    			///分页请求查询成交回报
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 需要分页查询成交回报的条件，如果第一次查询，那么reference填0
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
    			virtual int QueryTradesByPage(const XTPQueryTraderByPageReq *query_param, uint64_t session_id, int request_id) = 0;
    
    			///按条件请求查询投资者指定持仓
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param ticker 需要查询持仓的合约代码，可以为NULL，表示查询沪深全市场主股卡持仓，如果不为NULL，请不带空格，并以'\0'结尾，注意需与market匹配，不匹配的话，查询不到所需的持仓
    			///@param market 需要查询持仓的合约所在市场，仅在合约代码不为NULL的时候，才会使用。使用时，market必须指定。需要查单市场持仓，请使用QueryAllPosition()
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 该方法如果用户提供了合约代码，则会查询此合约的主股卡持仓信息（注意请指定market，不指定查不到所需的持仓,此时不受查询服务是否可用影响），如果合约代码为空，则默认查询沪深市场的主股卡持仓信息,类似于使用QueryAllPosition()。
    			virtual int QueryPosition(const char *ticker, uint64_t session_id, int request_id, XTP_MARKET_TYPE market) = 0;
    
    			///按条件请求查询投资者持仓
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 需要查询持仓的条件，可以为NULL，表示查询沪深全市场主股卡持仓，如果不为NULL，会优先看股卡信息，如果提供了股卡，必须与market匹配；如果没有提供股卡信息，则默认查询market对应的主股卡持仓（注意market不可为0。当market不为0，ticker为空时，默认查询主股卡中market对应的持仓；当market不为0，ticker不为空时，默认查询主股卡中market里指定ticker的持仓）
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 该方法如果用户没有提供股卡信息，则默认查主股卡的持仓，如果提供了股卡，必须与market匹配，否则查不到正确的持仓。此函数支持查指定合约代码的持仓。当查指定合约代码持仓时，不受查询服务是否可用影响。
    			virtual int QueryAllPosition(const XTPQueryStkPositionReq* query_param, uint64_t session_id, int request_id) = 0;
    
    			///请求查询用户的证券账户信息（股卡信息）
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			virtual int QuerySecurityAccount(uint64_t session_id, int request_id) = 0;
    
    			///请求查询资产
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 该方法不受查询服务是否可用影响
    			virtual int QueryAsset(uint64_t session_id, int request_id) = 0;
    
    // 			///请求查询分级基金
    // 			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    // 			///@param query_param 需要查询的分级基金筛选条件，其中母基金代码可以为空，则默认所有存在的母基金，如果不为空，请不带空格，并以'\0'结尾，其中交易市场不能为空
    // 			///@param session_id 资金账户对应的session_id,登录时得到
    // 			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    // 			///@remark 此函数查询出的结果可能对应多个查询结果响应
    // 			virtual int QueryStructuredFund(XTPQueryStructuredFundInfoReq *query_param, uint64_t session_id, int request_id) = 0;
    
    			///资金划拨请求
    			///@return 资金划拨订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示消息发送成功，用户需要记录下返回的serial_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
    			///@param fund_transfer 资金划拨的请求信息
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@remark 此函数支持一号两中心节点之间的资金划拨，注意资金划拨的方向。此函数受资金划拨服务器是否可用影响。
    			virtual uint64_t FundTransfer(XTPFundTransferReq *fund_transfer, uint64_t session_id) = 0;
    
    			///请求查询指定资金划拨订单
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param serial_id 需要查询的资金划拨订单ID,不可以为0
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 此函数不再支持全部查询，如果需要查询所有资金划拨订单，请使用分页查询接口QueryFundTransferByPage()查询。此函数受资金划拨服务器是否可用影响。
    			virtual int QueryFundTransferByID(uint64_t serial_id, uint64_t session_id, int request_id) = 0;
    
    			///分页请求查询资金划拨订单
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。此函数受资金划拨服务器是否可用影响。
    			virtual int QueryFundTransferByPage(const XTPQueryFundTransferByPageReq *query_param, uint64_t session_id, int request_id) = 0;
    
    			///请求查询其他节点可用资金
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 查询时需要提供的信息
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 此函数受资金划拨服务器是否可用影响。
    			virtual int QueryOtherServerFund(XTPFundQueryReq *query_param, uint64_t session_id, int request_id) = 0;
    
    			///请求查询ETF清单文件
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 需要查询的ETF清单文件的筛选条件，其中合约代码可以为空，则默认所有存在的ETF合约代码，market字段也可以为初始值，则默认所有市场的ETF合约
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			virtual int QueryETF(XTPQueryETFBaseReq *query_param, uint64_t session_id, int request_id) = 0;
    
    			///请求查询ETF股票篮
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 需要查询股票篮的的ETF合约，其中合约代码不可以为空，market字段也必须指定
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			virtual int QueryETFTickerBasket(XTPQueryETFComponentReq *query_param, uint64_t session_id, int request_id) = 0;
    
    			///请求查询今日新股申购信息列表
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			virtual int QueryIPOInfoList(uint64_t session_id, int request_id) = 0;
    
    			///请求查询用户新股申购额度信息
    			///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			virtual int QueryIPOQuotaInfo(uint64_t session_id, int request_id) = 0;
    
    			///请求查询今日可转债申购信息列表
    	        ///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    	        ///@param session_id 资金账户对应的session_id,登录时得到
    	        ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    	        virtual int QueryBondIPOInfoList(uint64_t session_id, int request_id) = 0;
    
    			///请求查询可转债转股的基本信息
    			///@return 查询是否发送成功，“0”表示发送成功，非“0”表示发送出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param query_param 需要查询的可转债转股信息的筛选条件，可以为NULL（为NULL表示查询所有的可转债转股信息），此参数中合约代码可以为空字符串，如果为空字符串，则查询所有可转债转股信息，如果不为空字符串，请不带空格，并以'\0'结尾，且必须与market匹配
    			///@param session_id 资金账户对应的session_id,登录时得到
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			virtual int QueryBondSwapStockInfo(XTPQueryBondSwapStockReq *query_param, uint64_t session_id, int request_id) = 0;
    
    
    		protected:
    			~TraderApi() {};
    		};
    
    			}
    }

  


#### 5.2.2. 示例代码 ​

以下是MyTraderApi.h文件

cpp
    
    
    #include "xtpx_trader_api.h"
    #include "MyTraderSpi.h"
    
    using namespace XTPX::API;
    
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

以下是MyTraderApi.cpp文件

cpp
    
    
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
    	user_trade_api_ = XTPX::API::TraderApi::CreateTraderApi(1, "./", XTP_LOG_LEVEL_DEBUG);
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

  


#### 5.2.3. CreateTraderApi ​

创建TraderApi的实例。只能创建一次，如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，但是对于同一账户，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接。系统不支持过夜，请确保每天开盘前重新启动。

◇ 1.函数原型

cpp
    
    
    static TraderApi *CreateTraderApi(uint8_t client_id, const char *save_file_path, XTP_LOG_LEVEL log_level = XTP_LOG_LEVEL_DEBUG);

◇ 2.参数

client_id：（必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义，总体取值区间[1,127]，普通用户取值区间[1,24]

save_file_path：（必须输入）存贮订阅信息文件的目录，请设定一个真实存在的有可写权限的路径

log_level：日志输出级别

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    //初始化api，创建单例
    uint8_t client_id_ = 1;
    string stdstr_log_path("./");
    // 开发调试时用XTP_LOG_LEVEL_DEBUG，稳定运行时用XTP_LOG_LEVEL_INFO
    XTP_LOG_LEVEL log_level = XTP_LOG_LEVEL_DEBUG;
    
    XTPX::API::TraderApi* user_trade_api_ = XTPX::API::TraderApi::CreateTraderApi(client_id_, stdstr_log_path.c_str(), log_level);
    
    if (user_trade_api_)
    {
    	// 注册回调接口
    	MyTraderSpi *spi = new MyTraderSpi();
    	user_trade_api_->RegisterSpi(spi);
    }

  


#### 5.2.4. Release ​

删除接口对象本身。当程序退出前，不再使用本接口对象时，调用该函数删除接口对象。

◇ 1.函数原型

cpp
    
    
    virtual void Release() = 0;

◇ 2.参数

无

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 登出并删除接口对象
    if (user_trade_api_)
    {
    	user_trade_api_->Logout(session_id_);
    	user_trade_api_->Release();
    }

  


#### 5.2.5. GetTradingDay ​

获取当前交易日。只有登录成功后,才能得到正确的交易日。

◇ 1.函数原型

cpp
    
    
    virtual const char *GetTradingDay() = 0;

◇ 2.参数

无

◇ 3.返回

返回一个指向日期信息字符串的常量指针。

◇ 4.调用示例

cpp
    
    
    // 获取交易日
    if (user_trade_api_)
    {
    	std::cout << "GetTradingDay：" << user_trade_api_->GetTradingDay() << std::endl;
    }

  


#### 5.2.6. RegisterSpi ​

注册回调接口。派生自回调接口类的实例，请在登录之前设定。

◇ 1.函数原型

cpp
    
    
    virtual void RegisterSpi(TraderSpi *spi) = 0;

◇ 2.参数

TraderSpi：接口类实例

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 注册回调接口
    if (user_trade_api_)
    {
    	MyTraderSpi *spi = new MyTraderSpi();
    	user_trade_api_->RegisterSpi(spi);
    }

  


#### 5.2.7. GetApiLastError ​

获取API的系统错误。返回的错误信息，可以在Login、InsertOrder、CancelOrder返回值为0时调用，获取失败的原因。可以在调用api接口失败时调用，例如login失败时

◇ 1.函数原型

cpp
    
    
    virtual XTPRI *GetApiLastError() = 0;

◇ 2.参数

无

◇ 3.返回

cpp
    
    
    namespace XTPX {
    
    	namespace API {
    		///错误信息的字符串长度
    		constexpr int32_t XTP_ERR_MSG_LEN = 124;
    		///响应信息
    		typedef struct XTPRspInfoStruct
    		{
    			///错误代码
    			int32_t	error_id;
    			///错误信息
    			char	error_msg[XTP_ERR_MSG_LEN];
    		} XTPRI;
    
    	}
    }

◇ 4.调用示例

cpp
    
    
    // 获取API的系统错误
    if (user_trade_api_)
    {
    	XTPRI* error_info = user_trade_api_->GetApiLastError();
    	std::cout << error_info->error_id << " : " << error_info->error_msg << std::endl;
    }

  


#### 5.2.8. GetApiVersion ​

获取API的发行版本号。

◇ 1.函数原型

cpp
    
    
    virtual const char* GetApiVersion() = 0;

◇ 2.参数

无

◇ 3.返回

返回api发行版本号。

◇ 4.调用示例

cpp
    
    
    // 获取API的发行版本号
    if (user_trade_api_)
    {
    	std::cout << "GetApiVersion ：" << user_trade_api_->GetApiVersion() << std::endl;
    }

  


#### 5.2.9. GetClientIDByXTPID ​

通过报单在xtp系统中的ID获取下单的客户端id。

由于系统允许同一用户在不同客户端上登录操作，每个客户端通过不同的client_id进行区分。

◇ 1.函数原型

cpp
    
    
    virtual uint8_t GetClientIDByXTPID(uint64_t order_xtp_id) = 0;

◇ 2.参数

order_xtp_id：报单在xtp系统中的ID

◇ 3.返回

返回客户端id，可以用此方法过滤自己下的订单

◇ 4.调用示例

cpp
    
    
    // 通过报单在xtp系统中的ID获取下单的客户端id
    if (user_trade_api_)
    {
    	uint8_t clientId = user_trade_api_->GetClientIDByXTPID(order_xtp_id);
    }

  


#### 5.2.10. GetAccountByXTPID ​

通过报单在xtp系统中的ID获取相关资金账户名。只有资金账户登录成功后,才能得到正确的信息。

◇ 1.函数原型

cpp
    
    
    virtual const char* GetAccountByXTPID(uint64_t order_xtp_id) = 0;

◇ 2.参数

order_xtp_id：报单在xtp系统中的ID

◇ 3.返回

返回资金账户名。

◇ 4.调用示例

cpp
    
    
    // 通过报单在xtp系统中的ID获取相关资金账户名
    if (user_trade_api_)
    {
    	const char *clientAccount = user_trade_api_->GetAccountByXTPID(order_xtp_id);
    }

  


#### 5.2.11. SubscribePublicTopic ​

订阅公共流。该方法要在Login方法前调用。若不调用则默认是用quick方式。注意在用户断线后，如果不登出就login()，公共流订阅方式将会默认使用resume方式。用户收到的数据会根据用户的选择方式而定。

◇ 1.函数原型

cpp
    
    
    virtual void SubscribePublicTopic(XTP_TE_RESUME_TYPE resume_type) = 0;

◇ 2.参数

cpp
    
    
    ///@brief XTP_TE_RESUME_TYPE是公有流（订单响应、成交回报）重传方式
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TE_RESUME_TYPE;
    
    ///从本交易日开始重传
    constexpr uint32_t XTP_TERT_RESTART = 0;    
    ///从从上次收到的续传（暂未支持）
    constexpr uint32_t XTP_TERT_RESUME = 1;  
    ///只传送登录后公有流（订单响应、成交回报）的内容
    constexpr uint32_t XTP_TERT_QUICK = 2;

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 订阅公有流，只传送登录后的订单响应和成交回报
    if (user_trade_api_)
    {
    	user_trade_api_->SubscribePublicTopic(XTP_TERT_QUICK);
    }

  


#### 5.2.12. SetSoftwareVersion ​

设置软件开发版本号。此函数必须在Login之前调用。

◇ 1.函数原型

cpp
    
    
    virtual void SetSoftwareVersion(const char* version) = 0;

◇ 2.参数

version 用户开发软件版本号，非api发行版本号，长度不超过15位，以'\0'结尾

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 设置软件开发版本号1.1.0，标识的是客户端版本号，而不是API的版本号，由用户自定义
    if (user_trade_api_)
    {
    	user_trade_api_->SetSoftwareVersion("1.1.0");
    }

  


#### 5.2.13. SetSoftwareKey ​

设置软件开发Key。此函数必须在Login之前调用。

◇ 1.函数原型

cpp
    
    
    virtual void SetSoftwareKey(const char* key) = 0;

◇ 2.参数

Key:用户开发软件Key，用户申请开户时给予，以'\0'结尾

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 设置软件开发Key
    if (user_trade_api_)
    {
    	user_trade_api_->SetSoftwareKey("xxxxxx");
    }

  


#### 5.2.14. SetHeartBeatInterval ​

设置心跳检测时间间隔，单位为秒，默认是15s。此函数必须在Login之前调用。

◇ 1.函数原型

cpp
    
    
    virtual void SetHeartBeatInterval(uint32_t interval) = 0;

◇ 2.参数

Interval：心跳检测时间间隔，单位为秒

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 设定交易服务器超时时间为15秒，用户可自定义
    if (user_trade_api_)
    {
    	user_trade_api_->SetHeartBeatInterval(15);
    }

  


#### 5.2.15. Login ​

用户登录请求。此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api可支持多个账户连接，但是同一个账户同一个client_id只能有一个session连接，后面的登录在前一个session存续期间，无法连接。

◇ 1.函数原型

cpp
    
    
    virtual uint64_t Login(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;

◇ 2.参数

Ip：服务器地址，类似"127.0.0.1"

Port：服务器端口号

User：登录用户名

Password：登录密码

sock_type："1"代表TCP，"2"代表UDP，目前暂时只支持TCP

local_ip：本地网卡地址，类似"127.0.0.1"

cpp
    
    
    ///@brief XTP_PROTOCOL_TYPE是通讯传输协议方式
    /////////////////////////////////////////////////////////////////////////
    typedef enum XTP_PROTOCOL_TYPE
    {
    	XTP_PROTOCOL_TCP = 1,	///<采用TCP方式传输
    	XTP_PROTOCOL_UDP		///<采用UDP方式传输(仅行情接口支持)
    }XTP_PROTOCOL_TYPE;

◇ 3.返回

session_id表明此资金账号登录是否成功。

"0"表示登录失败，可以调用GetApiLastError()来获取错误代码。

非"0"表示登录成功，此时需要记录下这个返回值session_id，与登录的资金账户对应。

◇ 4.调用示例

cpp
    
    
    // 登录请求，参数网址端口账户密码模式等和默认参数本机地址需用户自定义
    if (user_trade_api_)
    {
    	std::string trade_server_ip = "xxx.xxx.xxx.xxx";
    	int trade_server_port = xxxx;
    	std::string account_name = "xxxxxxxx";
    	std::string account_pw = "xxxxxx";
    	std::string local_ip = "xxx.xxx.xxx.xxx";//根据本地网卡对应的ip设定
    	
    	uint64_t ret = user_trade_api_->Login(trade_server_ip.c_str(), trade_server_port, account_name.c_str(), account_pw.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str());
    }

  


#### 5.2.16. Logout ​

登出请求。

◇ 1.函数原型

cpp
    
    
    virtual int Logout(uint64_t session_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id,登录时得到

◇ 3.返回

登出是否成功，"0"表示登出成功，"-1"表示登出失败

◇ 4.调用示例

cpp
    
    
    // 登出请求
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->Logout(session_id);
    }

  


#### 5.2.17. GetAccountTradeMarket ​

查询用户在本节点上的可交易市场类型。

◇ 1.函数原型

cpp
    
    
    virtual uint32_t GetAccountTradeMarket(uint64_t session_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id,登录时得到

◇ 3.返回

按位来看，从低位开始数，第0位表示沪市，即如果(trade_location&0x01) == 0x01，代表可交易沪市，第1位表示深市，即如果(trade_location&0x02) == 0x02，表示可交易深市，如果第0位和第1位均是1，即(trade_location&(0x01|0x02)) == 0x03，就表示可交易沪深2个市场

◇ 4.调用示例

cpp
    
    
    if (user_trade_api_)
    {
    	uint32_t trade_location = user_trade_api_->GetAccountTradeMarket(session_id);
    }

  


#### 5.2.18. GetANewOrderXTPID ​

为用户获取一个新的订单XTPID，用于报单。

此函数必须在Login之后调用，通过这个函数获取的order_xtp_id仅用于对应的用户报单，如果设置错误，将会导致下单失败。

◇ 1.函数原型

cpp
    
    
    virtual uint64_t GetANewOrderXTPID(uint64_t session_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id,登录时得到

◇ 3.返回

生成的订单XTPID，非“0”表示获取成功，“0”表示获取失败，此时用户可以调用GetApiLastError()来获取错误代码

◇ 4.调用示例

cpp
    
    
    if (user_trade_api_)
    {
    	uint64_t xtp_id = user_trade_api_->GetANewOrderXTPID(session_id);
    }

  


#### 5.2.19. GetMaxReqNumOfPagedQuery ​

获取用户分页查询允许的最大查询数量，方便用户在调用分页查询接口时，合理填写分页查询数量，否则超出最大查询限制，调用查询接口会失败。该函数必须是Login之后调用。

◇ 1.函数原型

cpp
    
    
    virtual int64_t GetMaxReqNumOfPagedQuery(uint64_t session_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id,登录时得到

◇ 3.返回

分页查询允许的最大查询数量req_count，非“0”表示获取成功，“0”表示获取失败，此时用户可以调用GetApiLastError()来获取错误代码

◇ 4.调用示例

cpp
    
    
    if(user_trade_api_)
    {
    	int64_t maxReqNum = user_trade_api_->GetMaxReqNumOfPagedQuery(session_id);
    }

  


#### 5.2.20. InsertOrder ​

报单录入请求。

交易所接收订单后，会在报单响应函数OnOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回。

◇ 1.函数原型

cpp
    
    
    virtual uint64_t InsertOrder(XTPOrderInsertInfo *order, uint64_t session_id) = 0;

◇ 2.参数

order：报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。order.order_xtp_id字段无需用户填写，order.ticker必须不带空格，以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

cpp
    
    
    ///新订单请求
    struct XTPOrderInsertInfo
    {
    	///XTP系统订单ID，无需用户填写，在XTP系统中唯一
    	uint64_t                order_xtp_id;
    	///合约代码 客户端请求不带空格，以'\0'结尾
    	char                    ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE         market;
    	///报单引用，由客户自定义
    	uint32_t                order_client_id;
    	///价格
    	double                  price;
    	///数量(股票单位为股，逆回购单位为张)
    	int64_t                 quantity;
    	///价格类型
    	XTP_PRICE_TYPE          price_type;
    	///买卖方向
    	XTP_SIDE_TYPE           side;
    	///开平标志（期权用户使用）
    	XTP_POSITION_EFFECT_TYPE    position_effect;
    	///算法策略类型（普通用户不填）
    	uint16_t                strategy_type;
    	///算法母单编号ID（普通用户不填）
    	uint64_t                strategy_id;
    	///业务类型
    	XTP_BUSINESS_TYPE       business_type;
    	/// 证券账户（股卡），非必填字段。不填，默认以主股卡报送；填了，即用指定股卡报送。
    	char                    account_id[XTP_ACCOUNT_ID_LEN];
    	///交易所PBU代码，非必填字段。不填，以默认席位报送；填了，即用指定席位报送。（通常为券结业务客户使用）
    	char                    branch_pbu[XTP_BRANCH_PBU_LEN];
    	/// 预留
    	char                    unused[4];
    };

cpp
    
    
    ///@brief XTP_MARKET_TYPE市场类型，交易里使用
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_MKT_UNKNOWN = 7;

cpp
    
    
    ///@brief XTP_PRICE_TYPE是价格类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_PRICE_TYPE;
    
    ///限价单-沪 / 深 / 沪期权 / 深期权 （除普通股票业务外，其余未特指的业务均使用此种类型）
    constexpr uint32_t XTP_PRICE_LIMIT = 1;        
    ///即时成交剩余转撤销，市价单-深 / 沪期权 / 深期权
    constexpr uint32_t XTP_PRICE_BEST_OR_CANCEL = 2;        
    ///最优五档即时成交剩余转限价，市价单-沪
    constexpr uint32_t XTP_PRICE_BEST5_OR_LIMIT = 3;        
    ///最优5档即时成交剩余转撤销，市价单-沪深 / 深期权
    constexpr uint32_t XTP_PRICE_BEST5_OR_CANCEL = 4;        
    ///全部成交或撤销,市价单-深 / 沪期权 / 深期权
    constexpr uint32_t XTP_PRICE_ALL_OR_CANCEL = 5;        
    ///本方最优，市价单-沪深 / 深期权
    constexpr uint32_t XTP_PRICE_FORWARD_BEST = 6; 
    ///对手方最优，市价单-沪深 / 深期权    
    constexpr uint32_t XTP_PRICE_REVERSE_BEST_LIMIT = 7;        
    ///期权限价申报FOK
    constexpr uint32_t XTP_PRICE_LIMIT_OR_CANCEL = 8;        
    ///未知或者无效价格类型
    constexpr uint32_t XTP_PRICE_TYPE_UNKNOWN = 9;

cpp
    
    
    ///@brief XTP_SIDE_TYPE是买卖方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_SIDE_TYPE;
    
    ///买（新股申购，ETF买，配股，信用交易中担保品买）
    constexpr uint32_t XTP_SIDE_BUY = 1;
    ///卖（逆回购，ETF卖，信用交易中担保品卖）
    constexpr uint32_t XTP_SIDE_SELL = 2;
    ///申购
    constexpr uint32_t XTP_SIDE_PURCHASE = 7;
    ///赎回
    constexpr uint32_t XTP_SIDE_REDEMPTION = 8;
    ///拆分
    constexpr uint32_t XTP_SIDE_SPLIT = 9;
    ///合并
    constexpr uint32_t XTP_SIDE_MERGE = 10;
    ///改版之后的side的备兑，暂不支持
    constexpr uint32_t XTP_SIDE_COVER = 11;
    ///改版之后的side锁定（对应开平标识为开）/解锁（对应开平标识为平）
    constexpr uint32_t XTP_SIDE_FREEZE = 12;
    /// 融资买入
    constexpr uint32_t XTP_SIDE_MARGIN_TRADE = 21;
    /// 融券卖出
    constexpr uint32_t XTP_SIDE_SHORT_SELL = 22;
    /// 卖券还款
    constexpr uint32_t XTP_SIDE_REPAY_MARGIN = 23;
    /// 买券还券
    constexpr uint32_t XTP_SIDE_REPAY_STOCK = 24;
    /// 现金还款（不放在普通订单协议，另加请求和查询协议）
    //		constexpr uint32_t XTP_SIDE_CASH_REPAY_MARGIN = 25;
    /// 现券还券
    constexpr uint32_t XTP_SIDE_STOCK_REPAY_STOCK = 26;
    /// 余券划转
    constexpr uint32_t XTP_SIDE_SURSTK_TRANS = 27;
    /// 担保品转入
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSIN = 28;
    /// 担保品转出
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSOUT = 29;
    
    ///组合策略的组合
    constexpr uint32_t XTP_SIDE_OPT_COMBINE = 31; 
    ///组合策略的拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT = 32; 
    ///组合策略的管理员强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE = 33; 
    ///组合策略的交易所强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE_EXCH = 34;
    
    ///未知或者无效买卖方向
    constexpr uint32_t XTP_SIDE_UNKNOWN = 50;

cpp
    
    
    ///@brief XTP_POSITION_EFFECT_TYPE是开平标识类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_POSITION_EFFECT_TYPE;
    
    /// 初始值或未知值开平标识，除期权外，均使用此值
    constexpr uint32_t XTP_POSITION_EFFECT_INIT = 0;
    /// 开
    constexpr uint32_t XTP_POSITION_EFFECT_OPEN = 1;
    /// 平
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSE = 2;
    /// 强平
    constexpr uint32_t XTP_POSITION_EFFECT_FORCECLOSE = 3;
    /// 平今
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSETODAY = 4;
    /// 平昨
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSEYESTERDAY = 5;
    /// 强减
    constexpr uint32_t XTP_POSITION_EFFECT_FORCEOFF = 6;
    /// 本地强平
    constexpr uint32_t XTP_POSITION_EFFECT_LOCALFORCECLOSE = 7;
    /// 信用业务追保强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_COVER = 8;
    /// 信用业务清偿强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_CLEAR = 9;
    /// 信用业务合约到期强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_DEBT = 10;
    /// 信用业务无条件强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_UNCOND = 11;
    /// 未知的开平标识类型
    constexpr uint32_t XTP_POSITION_EFFECT_UNKNOWN = 12;

cpp
    
    
    ///@brief XTP_BUSINESS_TYPE证券业务类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_BUSINESS_TYPE;
    
    ///普通股票业务（股票买卖，ETF买卖，沪市交易型货币基金等）
    constexpr uint32_t XTP_BUSINESS_TYPE_CASH = 0;            
    ///新股申购业务（对应的price type需选择限价类型）
    constexpr uint32_t XTP_BUSINESS_TYPE_IPOS = 1;
    ///回购业务（国债逆回购业务对应的price type填为限价，side填为卖）
    constexpr uint32_t XTP_BUSINESS_TYPE_REPO = 2;
    ///ETF申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_ETF = 3;
    ///融资融券业务
    constexpr uint32_t XTP_BUSINESS_TYPE_MARGIN = 4;              
    ///转托管（未支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_DESIGNATION = 5;
    ///配股业务（对应的price type需选择限价类型,side填为买）
    constexpr uint32_t XTP_BUSINESS_TYPE_ALLOTMENT = 6;
    ///分级基金申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION = 7;      
    ///分级基金拆分合并业务（业务已下线，不再支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE = 8;
    ///货币基金申赎业务（暂未支持，沪市交易型货币基金的买卖请使用普通股票业务）
    constexpr uint32_t XTP_BUSINESS_TYPE_MONEY_FUND = 9;
    ///期权业务       
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION = 10;
    ///行权
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE = 11;             
    ///锁定解锁，暂不支持
    constexpr uint32_t XTP_BUSINESS_TYPE_FREEZE = 12;             
    ///期权组合策略 组合和拆分业务
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION_COMBINE = 13;
    ///期权行权合并业务
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE_COMBINE = 14;    
    /// 债转股业务
    constexpr uint32_t XTP_BUSINESS_TYPE_BOND_SWAP_STOCK = 15;  
    ///未知类型   
    constexpr uint32_t XTP_BUSINESS_TYPE_UNKNOWN = 16;

cpp
    
    
    /// 存放证券代码的字符串长度
    constexpr uint32_t XTP_TICKER_LEN = 16;
    /// 用户股东账户的字符串长度
    constexpr uint32_t XTP_ACCOUNT_ID_LEN = 17;
    /// 交易所交易员代码字符串长度
    constexpr uint32_t XTP_BRANCH_PBU_LEN = 7;

◇ 3.返回

报单在XTP系统中的ID,如果为‘0’表示报单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非"0"表示报单发送成功，用户需要记录下返回的order_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性。

◇ 4.调用示例

cpp
    
    
    // 报入一笔限价单，以9.01的价格买入沪市"600000"的普通交易，数量1000。
    if (user_trade_api_)
    {
    	XTPOrderInsertInfo order;
    	memset(&order, 0, sizeof(XTPOrderInsertInfo));
    
    	order.market = XTP_MKT_SH_A;
    	std::string stdstr_ticker = "600000";
    	strncpy(order.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
    	order.business_type = XTP_BUSINESS_TYPE_CASH;
    	order.side = XTP_SIDE_BUY;
    	order.position_effect = XTP_POSITION_EFFECT_INIT;
    	order.price_type = XTP_PRICE_LIMIT;
    	order.price = 9.01;
    	order.quantity = 1000;
    	std::string stdstr_accountid = "AXXXXXXXXX";
    	strncpy(order.account_id, stdstr_accountid.c_str(), XTP_ACCOUNT_ID_LEN);//order.account_id可以不填，默认以主股卡报送
    
    	uint64_t order_xtp_id = user_trade_api_->InsertOrder(&order, session_id_);
    }

◇ 5.响应函数

cpp
    
    
    ///报单初始状态通知
    virtual void OnOrderAck(XTPOrderInfo *order_info, uint64_t session_id) { (void)order_info; (void)session_id; };
    // 报单响应
    virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) { (void)order_info; (void)error_info; (void)session_id; };
    // 报单成交响应
    virtual void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id) { (void)trade_info; (void)session_id; };

  


#### 5.2.21. InsertOrderExtra ​

已经提前设置order_xtp_id的报单录入请求，与GetANewOrderXTPID()配合使用。

使用设置好的order_xtp_id（通过GetANewOrderXTPID()获得）进行报单，注意此处如果order_xtp_id设置不对，将导致报单失败。

交易所接收订单后，会在报单响应函数OnOrderEvent()中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回。

◇ 1.函数原型

cpp
    
    
    virtual uint64_t InsertOrderExtra(XTPOrderInsertInfo *order, uint64_t session_id) = 0

◇ 2.参数

order：报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单，也可以什么都不填。order.order_xtp_id字段必须是通过GetANewOrderXTPID()获得的值，order.ticker必须不带空格，以'\0'结尾

session_id：资金账户对应的session_id,登录时得到

cpp
    
    
    ///新订单请求
    struct XTPOrderInsertInfo
    {
    	///XTP系统订单ID，无需用户填写，在XTP系统中唯一
    	uint64_t                order_xtp_id;
    	///合约代码 客户端请求不带空格，以'\0'结尾
    	char                    ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE         market;
    	///报单引用，由客户自定义
    	uint32_t                order_client_id;
    	///价格
    	double                  price;
    	///数量(股票单位为股，逆回购单位为张)
    	int64_t                 quantity;
    	///价格类型
    	XTP_PRICE_TYPE          price_type;
    	///买卖方向
    	XTP_SIDE_TYPE           side;
    	///开平标志（期权用户使用）
    	XTP_POSITION_EFFECT_TYPE    position_effect;
    	///算法策略类型（普通用户不填）
    	uint16_t                strategy_type;
    	///算法母单编号ID（普通用户不填）
    	uint64_t                strategy_id;
    	///业务类型
    	XTP_BUSINESS_TYPE       business_type;
    	/// 证券账户（股卡），非必填字段。不填，默认以主股卡报送；填了，即用指定股卡报送。
    	char                    account_id[XTP_ACCOUNT_ID_LEN];
    	///交易所PBU代码，非必填字段。不填，以默认席位报送；填了，即用指定席位报送。（通常为券结业务客户使用）
    	char                    branch_pbu[XTP_BRANCH_PBU_LEN];
    	/// 预留
    	char                    unused[4];
    };

cpp
    
    
    ///@brief XTP_MARKET_TYPE市场类型，交易里使用
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_MKT_UNKNOWN = 7;

cpp
    
    
    ///@brief XTP_PRICE_TYPE是价格类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_PRICE_TYPE;
    
    ///限价单-沪 / 深 / 沪期权 / 深期权 （除普通股票业务外，其余未特指的业务均使用此种类型）
    constexpr uint32_t XTP_PRICE_LIMIT = 1;        
    ///即时成交剩余转撤销，市价单-深 / 沪期权 / 深期权
    constexpr uint32_t XTP_PRICE_BEST_OR_CANCEL = 2;        
    ///最优五档即时成交剩余转限价，市价单-沪
    constexpr uint32_t XTP_PRICE_BEST5_OR_LIMIT = 3;        
    ///最优5档即时成交剩余转撤销，市价单-沪深 / 深期权
    constexpr uint32_t XTP_PRICE_BEST5_OR_CANCEL = 4;        
    ///全部成交或撤销,市价单-深 / 沪期权 / 深期权
    constexpr uint32_t XTP_PRICE_ALL_OR_CANCEL = 5;        
    ///本方最优，市价单-沪深 / 深期权
    constexpr uint32_t XTP_PRICE_FORWARD_BEST = 6; 
    ///对手方最优，市价单-沪深 / 深期权    
    constexpr uint32_t XTP_PRICE_REVERSE_BEST_LIMIT = 7;        
    ///期权限价申报FOK
    constexpr uint32_t XTP_PRICE_LIMIT_OR_CANCEL = 8;        
    ///未知或者无效价格类型
    constexpr uint32_t XTP_PRICE_TYPE_UNKNOWN = 9;

cpp
    
    
    ///@brief XTP_SIDE_TYPE是买卖方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_SIDE_TYPE;
    
    ///买（新股申购，ETF买，配股，信用交易中担保品买）
    constexpr uint32_t XTP_SIDE_BUY = 1;
    ///卖（逆回购，ETF卖，信用交易中担保品卖）
    constexpr uint32_t XTP_SIDE_SELL = 2;
    ///申购
    constexpr uint32_t XTP_SIDE_PURCHASE = 7;
    ///赎回
    constexpr uint32_t XTP_SIDE_REDEMPTION = 8;
    ///拆分
    constexpr uint32_t XTP_SIDE_SPLIT = 9;
    ///合并
    constexpr uint32_t XTP_SIDE_MERGE = 10;
    ///改版之后的side的备兑，暂不支持
    constexpr uint32_t XTP_SIDE_COVER = 11;
    ///改版之后的side锁定（对应开平标识为开）/解锁（对应开平标识为平）
    constexpr uint32_t XTP_SIDE_FREEZE = 12;
    /// 融资买入
    constexpr uint32_t XTP_SIDE_MARGIN_TRADE = 21;
    /// 融券卖出
    constexpr uint32_t XTP_SIDE_SHORT_SELL = 22;
    /// 卖券还款
    constexpr uint32_t XTP_SIDE_REPAY_MARGIN = 23;
    /// 买券还券
    constexpr uint32_t XTP_SIDE_REPAY_STOCK = 24;
    /// 现金还款（不放在普通订单协议，另加请求和查询协议）
    //		constexpr uint32_t XTP_SIDE_CASH_REPAY_MARGIN = 25;
    /// 现券还券
    constexpr uint32_t XTP_SIDE_STOCK_REPAY_STOCK = 26;
    /// 余券划转
    constexpr uint32_t XTP_SIDE_SURSTK_TRANS = 27;
    /// 担保品转入
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSIN = 28;
    /// 担保品转出
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSOUT = 29;
    
    ///组合策略的组合
    constexpr uint32_t XTP_SIDE_OPT_COMBINE = 31; 
    ///组合策略的拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT = 32; 
    ///组合策略的管理员强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE = 33; 
    ///组合策略的交易所强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE_EXCH = 34;
    
    ///未知或者无效买卖方向
    constexpr uint32_t XTP_SIDE_UNKNOWN = 50;

cpp
    
    
    ///@brief XTP_POSITION_EFFECT_TYPE是开平标识类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_POSITION_EFFECT_TYPE;
    
    /// 初始值或未知值开平标识，除期权外，均使用此值
    constexpr uint32_t XTP_POSITION_EFFECT_INIT = 0;
    /// 开
    constexpr uint32_t XTP_POSITION_EFFECT_OPEN = 1;
    /// 平
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSE = 2;
    /// 强平
    constexpr uint32_t XTP_POSITION_EFFECT_FORCECLOSE = 3;
    /// 平今
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSETODAY = 4;
    /// 平昨
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSEYESTERDAY = 5;
    /// 强减
    constexpr uint32_t XTP_POSITION_EFFECT_FORCEOFF = 6;
    /// 本地强平
    constexpr uint32_t XTP_POSITION_EFFECT_LOCALFORCECLOSE = 7;
    /// 信用业务追保强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_COVER = 8;
    /// 信用业务清偿强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_CLEAR = 9;
    /// 信用业务合约到期强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_DEBT = 10;
    /// 信用业务无条件强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_UNCOND = 11;
    /// 未知的开平标识类型
    constexpr uint32_t XTP_POSITION_EFFECT_UNKNOWN = 12;

cpp
    
    
    ///@brief XTP_BUSINESS_TYPE证券业务类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_BUSINESS_TYPE;
    
    ///普通股票业务（股票买卖，ETF买卖，沪市交易型货币基金等）
    constexpr uint32_t XTP_BUSINESS_TYPE_CASH = 0;            
    ///新股申购业务（对应的price type需选择限价类型）
    constexpr uint32_t XTP_BUSINESS_TYPE_IPOS = 1;
    ///回购业务（国债逆回购业务对应的price type填为限价，side填为卖）
    constexpr uint32_t XTP_BUSINESS_TYPE_REPO = 2;
    ///ETF申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_ETF = 3;
    ///融资融券业务
    constexpr uint32_t XTP_BUSINESS_TYPE_MARGIN = 4;              
    ///转托管（未支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_DESIGNATION = 5;
    ///配股业务（对应的price type需选择限价类型,side填为买）
    constexpr uint32_t XTP_BUSINESS_TYPE_ALLOTMENT = 6;
    ///分级基金申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION = 7;      
    ///分级基金拆分合并业务（业务已下线，不再支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE = 8;
    ///货币基金申赎业务（暂未支持，沪市交易型货币基金的买卖请使用普通股票业务）
    constexpr uint32_t XTP_BUSINESS_TYPE_MONEY_FUND = 9;
    ///期权业务       
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION = 10;
    ///行权
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE = 11;             
    ///锁定解锁，暂不支持
    constexpr uint32_t XTP_BUSINESS_TYPE_FREEZE = 12;             
    ///期权组合策略 组合和拆分业务
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION_COMBINE = 13;
    ///期权行权合并业务
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE_COMBINE = 14;    
    /// 债转股业务
    constexpr uint32_t XTP_BUSINESS_TYPE_BOND_SWAP_STOCK = 15;  
    ///未知类型   
    constexpr uint32_t XTP_BUSINESS_TYPE_UNKNOWN = 16;

cpp
    
    
    /// 存放证券代码的字符串长度
    constexpr uint32_t XTP_TICKER_LEN = 16;
    /// 用户股东账户的字符串长度
    constexpr uint32_t XTP_ACCOUNT_ID_LEN = 17;
    /// 交易所交易员代码字符串长度
    constexpr uint32_t XTP_BRANCH_PBU_LEN = 7;

◇ 3.返回

报单在XTP系统中的ID,如果为‘0’表示报单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非“0”表示报单发送成功，此时等同与传入的order_xtp_id。

◇ 4.调用示例

cpp
    
    
    // 报入一笔限价单，以9.01的价格买入沪市"600000"的普通交易，数量1000。
    if (user_trade_api_)
    {
    	uint64_t new_xtp_id = user_trade_api_->GetANewOrderXTPID(session_id);
    
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
    	std::string stdstr_accountid = "AXXXXXXXXX";
    	strncpy(order.account_id, stdstr_accountid.c_str(), XTP_ACCOUNT_ID_LEN);//order.account_id可以不填，默认以主股卡报送
    
    	uint64_t order_xtp_id = user_trade_api_->InsertOrderExtra(&order, session_id_);
    	if (order_xtp_id == new_xtp_id)
    	{
    		// 报单发送成功
    	}
    }

◇ 5.响应函数

cpp
    
    
    ///报单初始状态通知
    virtual void OnOrderAck(XTPOrderInfo *order_info, uint64_t session_id) { (void)order_info; (void)session_id; };
    // 报单响应
    virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) { (void)order_info; (void)error_info; (void)session_id; };
    // 报单成交响应
    virtual void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id) { (void)trade_info; (void)session_id; };

  


#### 5.2.22. CancelOrder ​

撤单请求。

如果撤单成功，会在报单响应函数OnOrderEvent()里返回原单部撤或者全撤的消息，如果不成功，会在OnCancelOrderError()响应函数中返回错误原因。

◇ 1.函数原型

cpp
    
    
    virtual uint64_t CancelOrder(const uint64_t order_xtp_id, uint64_t session_id) = 0;

◇ 2.参数

order_xtp_id：需要撤销的委托单在XTP系统中的ID

session_id：资金账户对应的session_id,登录时得到

◇ 3.返回

撤单在XTP系统中的ID,如果为‘0’表示撤单发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非"0"表示撤单发送成功，用户需要记录下返回的order_cancel_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性。

◇ 4.调用示例

cpp
    
    
    // 撤单
    if (user_trade_api_)
    {
    	uint64_t ret = user_trade_api_->CancelOrder(order_xtp_id, session_id);
    }

◇ 5.响应函数

cpp
    
    
    // 撤单响应
    virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) { (void)order_info; (void)error_info; (void)session_id; };
    // 撤单出错响应
    virtual void OnCancelOrderError(XTPOrderCancelErrorInfo *cancel_info, XTPRI *error_info, uint64_t session_id) { (void)cancel_info; (void)error_info; (void)session_id; };

  


#### 5.2.23. QueryOrderByXTPID ​

根据报单ID请求查询报单。

◇ 1.函数原型

cpp
    
    
    virtual int QueryOrderByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;

◇ 2.参数

order_xtp_id：需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码

◇ 4.调用示例

cpp
    
    
    // 根据报单ID请求查询报单
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QueryOrderByXTPID(order_xtp_id, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.24. QueryOrders ​

请求查询报单。

该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

◇ 1.函数原型

cpp
    
    
    virtual int QueryOrders(const XTPQueryOrderReq *query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param：需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

cpp
    
    
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

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询当前交易日0点至当前时间点的所有报单
    if (user_trade_api_)
    {
    	XTPQueryOrderReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryOrderReq));
    
    	int ret = user_trade_api_->QueryOrders(&query_param, session_id, request_id);
    }

cpp
    
    
    // 查询600000这支股票在当前交易日0点至当前时间点的全部报单
    if (user_trade_api_)
    {
    	XTPQueryOrderReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryOrderReq));
    
    	std::string stdstr_ticker = "600000";
    	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
    
    	int ret = user_trade_api_->QueryOrders(&query_param, session_id, request_id);
    }

cpp
    
    
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

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.25. QueryUnfinishedOrders ​

请求查询未完结报单。

◇ 1.函数原型

cpp
    
    
    virtual int QueryUnfinishedOrders(uint64_t session_id, int request_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 请求查询未完结报单
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QueryUnfinishedOrders(session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.26. QueryOrdersByPage ​

分页请求查询报单。

该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。另外，如果用户填的分页查询数量req_count超出了系统允许的最大分页查询数量的限制，会导致查询失败，  
最大分页查询数量可调用接口GetMaxReqNumOfPagedQuery()获取。

◇ 1.函数原型

cpp
    
    
    virtual int QueryOrdersByPage(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param：需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

cpp
    
    
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

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    if (user_trade_api_)
    {
    	XTPQueryOrderByPageReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryOrderByPageReq));
    	int64_t maxReq = user_trade_api_->GetMaxReqNumOfPagedQuery(session_id);//获取最大分页查询数量
    	query_param.req_count = maxReq;//可以设置比允许的最大分页查询数量更小
    	query_param.reference = 0;//第一次查询
    
    	int ret = user_trade_api_->QueryOrdersByPage(&query_param, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryOrderByPage(XTPQueryOrderRsp *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)req_count; (void)order_sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.27. QueryTradesByXTPID ​

根据委托编号请求查询相关成交。

此函数查询出的结果可能对应多个查询结果响应。

◇ 1.函数原型

cpp
    
    
    virtual int QueryTradesByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;

◇ 2.参数

order_xtp_id：需要查询的委托编号，即InsertOrder()成功时返回的order_xtp_id

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 根据委托编号请求查询相关成交
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QueryTradesByXTPID(order_xtp_id, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryTrade(XTPQueryTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)trade_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.28. QueryTrades ​

请求查询已成交。

该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有成交回报，否则查询时间段内所有跟股票代码相关的成交回报，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

◇ 1.函数原型

cpp
    
    
    virtual int QueryTrades(XTPQueryTraderReq *query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param：需要查询的成交回报筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

cpp
    
    
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

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询当前交易日0点至当前时间点的所有成交单
    if (user_trade_api_)
    {
    	XTPQueryTraderReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryTraderReq));
    
    	int ret = user_trade_api_->QueryTrades(&query_param, session_id, request_id);
    }

cpp
    
    
    // 查询600000这支股票在当前交易日0点至当前时间点的全部成交单
    if (user_trade_api_)
    {
    	XTPQueryTraderReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryTraderReq));
    
    	std::string stdstr_ticker = "600000";
    	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
    
    	int ret = user_trade_api_->QueryTrades(&query_param, session_id, request_id);
    }

cpp
    
    
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

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryTrade(XTPQueryTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)trade_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.29. QueryTradesByPage ​

分页请求查询成交回报。

该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。另外，如果用户填的分页查询数量req_count超出了系统允许的最大分页查询数量的限制，会导致查询失败，  
最大分页查询数量可调用接口GetMaxReqNumOfPagedQuery()获取。

◇ 1.函数原型

cpp
    
    
    virtual int QueryTradesByPage(const XTPQueryTraderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param：需要分页查询成交回报的条件，如果第一次查询，那么reference填0

session_id：资金账户对应的session_id，登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

cpp
    
    
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

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    if (user_trade_api_)
    {
    	XTPQueryTraderByPageReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryTraderByPageReq));
    	int64_t maxReq = user_trade_api_->GetMaxReqNumOfPagedQuery(session_id);//获取最大分页查询数量
    	query_param.req_count = maxReq;//可以设置比允许的最大分页查询数量更小
    	query_param.reference = 0;
    
    	int ret = user_trade_api_->QueryTradesByPage(&query_param, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryTradeByPage(XTPQueryTradeRsp *trade_info, int64_t req_count, int64_t trade_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)trade_info; (void)req_count; (void)trade_sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.30. QueryPosition ​

按条件请求查询投资者指定持仓。

该方法如果用户提供了合约代码，则会查询此合约的主股卡持仓信息（注意请指定market，不指定查不到所需的持仓,此时不受查询服务是否可用影响），如果合约代码为空，则默认查询沪深市场的主股卡持仓信息,类似于使用QueryAllPosition()。

◇ 1.函数原型

cpp
    
    
    virtual int QueryPosition(const char *ticker, uint64_t session_id, int request_id, XTP_MARKET_TYPE market) = 0;

◇ 2.参数

Ticker：需要查询持仓的合约代码，可以为NULL，表示查询沪深全市场主股卡持仓，如果不为NULL，请不带空格，并以'\0'结尾，注意需与market匹配，不匹配的话，查询不到所需的持仓

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

market：需要查询持仓的合约所在市场，仅在合约代码不为NULL的时候，才会使用。使用时，market必须指定。需要查单市场持仓，请使用QueryAllPosition()

cpp
    
    
    //////////////////////////////////////////////////////////////////////////
    ///@brief XTP_MARKET_TYPE市场类型，交易里使用
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_MKT_UNKNOWN = 7;

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询沪市主股卡上600000这支股票的持仓
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QueryPosition("600000", session_id, request_id， XTP_MKT_SH_A);
    }

cpp
    
    
    // 查询沪深全市场主股卡持仓
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QueryPosition(NULL, session_id, request_id, XTP_MKT_INIT);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryPosition(XTPQueryStkPositionRsp *position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)position; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.31. QueryAllPosition ​

按条件请求查询投资者持仓。

该方法如果用户没有提供股卡信息，则默认查主股卡的持仓，如果提供了股卡，必须与market匹配，否则查不到正确的持仓。此函数支持查询指定合约代码的持仓。当查询指定合约代码持仓时，不受查询服务是否可用的影响。

◇ 1.函数原型

cpp
    
    
    virtual int QueryAllPosition(const XTPQueryStkPositionReq* query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param: 需要查询持仓的条件，可以为NULL，表示查询沪深全市场主股卡持仓，如果不为NULL，会优先看股卡信息，如果提供了股卡，必须与market匹配；如果没有提供股卡信息，则默认查询market对应的主股卡持仓（注意market不可为0。当market不为0，ticker为空时，默认查询主股卡中market对应的持仓；当market不为0，ticker不为空时，默认查询主股卡中market里指定ticker的持仓）

session_id: 资金账户对应的session_id,登录时得到

request_id: 用于用户定位查询响应的ID，由用户自定义

cpp
    
    
    ///查询股票持仓情况请求结构体
    //////////////////////////////////////////////////////////////////////////
    struct XTPQueryStkPositionReq
    {
    	///证券代码
    	char                ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE     market;
    	///证券账户（股卡）
    	char                account_id[XTP_ACCOUNT_ID_LEN];
    	/// 预留
    	char                unused[3];
    };
    
    ///@brief XTP_MARKET_TYPE市场类型，交易里使用
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_MKT_UNKNOWN = 7;

◇ 3.返回

查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码

◇ 4.调用示例

cpp
    
    
    //查询沪深全市场主股卡持仓
    if(user_trade_api_)
    {
    	int ret = user_trade_api_->QueryAllPosition(NULL, session_id, request_id);
    }

cpp
    
    
    //查询沪市主股卡的所有持仓
    if(user_trade_api_)
    {
    	XTPQueryStkPositionReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryStkPositionReq));
    	query_param.market = XTP_MKT_SH_A;
    	int ret = user_trade_api_->QueryAllPosition(&query_param, session_id, request_id);
    }

cpp
    
    
    //查询沪市某个股卡上的所有持仓
    if(user_trade_api_)
    {
    	XTPQueryStkPositionReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryStkPositionReq));
    	query_param.market = XTP_MKT_SH_A;
    	std::string stdstr_accountid = "AXXXXXXXXX";//股卡号要与市场类型相对应
    	strncpy(query_param.account_id, stdstr_accountid.c_str(), XTP_ACCOUNT_ID_LEN);
    	int ret = user_trade_api_->QueryAllPosition(&query_param, session_id, request_id);
    }

cpp
    
    
    //查询沪市某股卡上600000的持仓
    if(user_trade_api_)
    {
    	XTPQueryStkPositionReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryStkPositionReq));
    	query_param.market = XTP_MKT_SH_A;
    	std::string ticker_str = "600000";
    	strncpy(query_param.ticker, ticker_str.c_str(), XTP_TICKER_LEN);
    	std::string stdstr_accountid = "AXXXXXXXXX";//股卡号要与市场类型相对应,为空的话，默认是沪市主股卡
    	strncpy(query_param.account_id, stdstr_accountid.c_str(), XTP_ACCOUNT_ID_LEN);
    	int ret = user_trade_api_->QueryAllPosition(&query_param, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryPosition(XTPQueryStkPositionRsp *position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)position; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.32. QuerySecurityAccount ​

请求查询用户的证券账户信息（股卡信息）。

◇ 1.函数原型

cpp
    
    
    virtual int QuerySecurityAccount(uint64_t session_id, int request_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码

◇ 4.调用示例

cpp
    
    
    // 查询资金
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QuerySecurityAccount(session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQuerySecurityAccount(XTPQueryAccountIdRsp *account_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)account_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.33. QueryAsset ​

请求查询资产，该方法不受查询服务是否可用影响。

◇ 1.函数原型

cpp
    
    
    virtual int QueryAsset(uint64_t session_id, int request_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码

◇ 4.调用示例

cpp
    
    
    // 查询资金
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QueryAsset(session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryAsset(XTPQueryAssetRsp *asset, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)asset; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.34. FundTransfer ​

资金划拨请求。此函数支持一号两中心节点之间的资金划拨，注意资金划拨的方向。此函数受资金划拨服务器是否可用影响。

◇ 1.函数原型

cpp
    
    
    virtual uint64_t FundTransfer(XTPFundTransferReq *fund_transfer, uint64_t session_id) = 0;

◇ 2.参数

fund_transfer：资金划拨的请求信息

session_id：资金账户对应的session_id,登录时得到

cpp
    
    
    ///用户资金划转请求结构体
    /////////////////////////////////////////////////////////////////////////
    struct XTPFundTransferReq
    {
    	///资金内转编号，无需用户填写，类似于xtp_id
    	uint64_t    serial_id;
    	///资金账户代码
    	char        fund_account[XTP_ACCOUNT_NAME_LEN];
    	///金额
    	double      amount;
    	///内转类型
    	XTP_FUND_TRANSFER_TYPE    transfer_type;
    	///转入或转出的目标服务器对应的节点类型（双中心用户跨节点划拨时必填）
    	XTP_TRANSFER_SITE_TYPE    site;
    	///货币种类
    	XTP_CURRENCY_TYPE        currency_type; 
    	///预留字段
    	char                     unused[4];
    };

cpp
    
    
    ///@brief XTP_FUND_TRANSFER_TYPE是资金流转方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_FUND_TRANSFER_TYPE;
    
    ///转出 从XTP转出到柜台
    constexpr uint32_t XTP_FUND_TRANSFER_OUT = 0;        
    ///转入 从柜台转入XTP
    constexpr uint32_t XTP_FUND_TRANSFER_IN = 1;
    ///跨节点转出 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨，只能“一账号两中心”跨节点用户使用
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_OUT = 2;
    ///跨节点转入 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨，只能“一账号两中心”跨节点用户使用
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_IN = 3;
    ///跨节点转出 融券卖出资金 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_REPAY_OUT = 4;
    ///跨节点转入 融券卖出资金 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_REPAY_IN = 5;
    ///跨节点转出 授信额度 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_CONTRACT_OUT = 6;
    ///跨节点转入 授信额度 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_CONTRACT_IN = 7; 
    ///未知类型
    constexpr uint32_t XTP_FUND_TRANSFER_UNKNOWN = 8;
    
    
    
    ///@brief XTP_TRANSFER_SITE_TYPE是一个划转节点类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TRANSFER_SITE_TYPE;
    
    ///主柜台
    constexpr uint32_t XTP_TRANSFER_SITE_COUNTER = 0;
    ///上海节点
    constexpr uint32_t XTP_TRANSFER_SITE_SH = 2;
    ///深圳节点
    constexpr uint32_t XTP_TRANSFER_SITE_SZ = 4;
    ///北京节点
    constexpr uint32_t XTP_TRANSFER_SITE_NQ = 8;
    ///香港节点
    constexpr uint32_t XTP_TRANSFER_SITE_HK = 16;
    ///未知节点
    constexpr uint32_t XTP_TRANSFER_SITE_UNKNOWN = 256;
    
    
    
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

◇ 3.返回

资金划拨订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError()来获取错误代码，非"0"表示消息发送成功，用户需要记录下返回的serial_id，它保证一个交易日内唯一，不同的交易日不保证唯一性。

◇ 4.调用示例

cpp
    
    
    // 发送某账户从柜台转入XTP的10000.01资金划拨请求，具体参数需用户自定义
    if (user_trade_api_)
    {
    	XTPFundTransferReq fund_transfer;
    	memset(&fund_transfer, 0, sizeof(XTPFundTransferReq));
    
    	std::string stdstr_fund_account = "xxxxxxxx";
    	strncpy(fund_transfer.fund_account, stdstr_fund_account.c_str(), XTP_ACCOUNT_NAME_LEN);
    	fund_transfer.amount = 10000.01;
    	fund_transfer.transfer_type = XTP_FUND_INTER_TRANSFER_OUT;
    	fund_transfer.site = XTP_TRANSFER_SITE_SZ;//双中心跨节点划转必须填写目标节点类型
    
    	uint64_t serial_id = user_trade_api_->FundTransfer(&fund_transfer, session_id);
    	if (serial_id == 0)
    	{
    		// 发送失败，获取失败原因
    		XTPRI* error_info = m_pTraderApi->GetApiLastError();
    		std::cout << "Fund transfer send error, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
    	}
    	else
    	{
    		// 发送成功返回的serial_id，保证一个交易日内唯一
    		//TODO:其他逻辑
    	}
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnFundTransfer(XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info, uint64_t session_id) { (void)fund_transfer_info; (void)error_info; (void)session_id; };

  


#### 5.2.35. QueryFundTransferByID ​

请求查询指定资金划拨订单。此函数不支持全部查询，如果需要查询所有资金划拨订单，请使用分页查询接口QueryFundTransferByPage()查询。此函数受资金划拨服务器是否可用影响。

◇ 1.函数原型

cpp
    
    
    virtual int QueryFundTransferByID(uint64_t serial_id, uint64_t session_id, int request_id) = 0;

◇ 2.参数

serial_id：需要查询的资金划拨订单ID,不可以为0

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询编号为1234567890123456的资金内转记录
    if (user_trade_api_)
    {
    	// 资金内转编号需替换成用户自己的id
    	uint64_t serial_id = 1234567890123456;
    
    	int ret = user_trade_api_->QueryFundTransferByID(serial_id, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryFundTransfer(XTPFundTransferLog *fund_transfer_info, XTPRI *fund_transfer_err_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)fund_transfer_info; (void)fund_transfer_err_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.36. QueryFundTransferByPage ​

分页请求查询资金划拨订单。该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。此函数受资金划拨服务器是否可用的影响。另外，如果用户填的分页查询数量req_count超出了系统允许的最大分页查询数量的限制，会导致查询失败，最大分页查询数量可调用接口GetMaxReqNumOfPagedQuery()获取。

◇ 1.函数原型

cpp
    
    
    virtual int QueryFundTransferByPage(const XTPQueryFundTransferByPageReq *query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param: 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0

session_id: 资金账户对应的session_id,登录时得到

request_id: 用于用户定位查询响应的ID，由用户自定义

cpp
    
    
    ///分页查询资金内转流水
    /////////////////////////////////////////////////////////////////////////
    struct XTPQueryFundTransferByPageReq
    {
    	///需要查询的资金流水条数
    	int64_t         req_count;
    	///上一次收到的查询结果中带回来的索引，如果是从头查询，请置0
    	int64_t         reference;
    	///保留字段
    	int64_t         reserved;
    };

◇ 3.返回

查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码.

◇ 4.调用示例

cpp
    
    
    //分页查询资金划拨订单
    if(user_trade_api_)
    {
    	XTPQueryFundTransferByPageReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryFundTransferByPageReq));
    	int64_t maxReq = user_trade_api_->GetMaxReqNumOfPagedQuery(session_id);//获取查询允许的最大分页查询数量
    	query_param.req_count = maxReq;//可以设置比最大分页查询数量小一点
    	query_param.reference = 0;//第一次查询
    	int ret = user_trade_api_->QueryFundTransferByPage(&query_param, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryFundTransferByPage(XTPFundTransferLog *fund_transfer_info, XTPRI *fund_transfer_err_info, XTPRI *error_info, int64_t req_count, int64_t sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)fund_transfer_info; (void)fund_transfer_err_info; (void)error_info; (void)req_count; (void)sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.37. QueryOtherServerFund ​

请求查询其他节点可用资金。

◇ 1.函数原型

cpp
    
    
    virtual int QueryOtherServerFund(XTPFundQueryReq *query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param：查询时需要提供的信息

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

cpp
    
    
    ///用户资金查询请求结构体
    /////////////////////////////////////////////////////////////////////////
    struct XTPFundQueryReq
    {
    	///资金账户代码
    	char        fund_account[XTP_ACCOUNT_NAME_LEN];
    	///查询类型
    	XTP_FUND_QUERY_TYPE    query_type;
    	///需要查询的服务器对应的节点类型（双中心用户查询时必填）
    	XTP_TRANSFER_SITE_TYPE query_site;
    	///货币种类
    	XTP_CURRENCY_TYPE      currency_type;
    	///预留字段
    	char                   unused[4];
    
    };

cpp
    
    
    ///@brief XTP_FUND_QUERY_TYPE是柜台资金查询类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_FUND_QUERY_TYPE;
    
    ///查询金证主柜台可转资金
    constexpr uint32_t XTP_FUND_QUERY_JZ = 0;        
    ///查询一账号两中心设置时，对方节点的资金
    constexpr uint32_t XTP_FUND_QUERY_INTERNAL = 1;
    ///查询一账号两中心设置时，对方节点的融券卖余额资金
    constexpr uint32_t XTP_FUND_QUERY_INTERNAL_REPAY = 2;  
    ///查询一账号两中心设置时，对方节点的授信额度
    constexpr uint32_t XTP_FUND_QUERY_INTERNAL_CONTRACT = 3; 
    ///未知类型
    constexpr uint32_t XTP_FUND_QUERY_UNKNOWN = 4;

cpp
    
    
    ///@brief XTP_TRANSFER_SITE_TYPE是一个划转节点类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TRANSFER_SITE_TYPE;
    
    ///主柜台
    constexpr uint32_t XTP_TRANSFER_SITE_COUNTER = 0;
    ///上海节点
    constexpr uint32_t XTP_TRANSFER_SITE_SH = 2;
    ///深圳节点
    constexpr uint32_t XTP_TRANSFER_SITE_SZ = 4;
    ///北京节点
    constexpr uint32_t XTP_TRANSFER_SITE_NQ = 8;
    ///香港节点
    constexpr uint32_t XTP_TRANSFER_SITE_HK = 16;
    ///未知节点
    constexpr uint32_t XTP_TRANSFER_SITE_UNKNOWN = 256;

cpp
    
    
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

cpp
    
    
    /// 用户资金账户的字符串长度
    constexpr uint32_t XTP_ACCOUNT_NAME_LEN = 16;

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询某账户在金证主柜台的可转资金，具体参数需用户自定义
    if (user_trade_api_)
    {
    	XTPFundQueryReq query_param;
    	memset(&query_param, 0, sizeof(XTPFundQueryReq));
    
    	query_param.query_type = XTP_FUND_QUERY_JZ;
    	query_param.query_site = XTP_TRANSFER_SITE_COUNTER;//双中心账户查询必填
    	std::string stdstr_fund_account = "xxxxxxx";
    	strncpy(query_param.fund_account, stdstr_fund_account.c_str(), XTP_ACCOUNT_NAME_LEN);
    	int ret = user_trade_api_->QueryOtherServerFund(&query_param, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryOtherServerFund(XTPFundQueryRsp *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) { (void)fund_info; (void)error_info; (void)request_id; (void)session_id; };

  


#### 5.2.38. QueryETF ​

请求查询ETF清单文件。

◇ 1.函数原型

cpp
    
    
    virtual int QueryETF(XTPQueryETFBaseReq *query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param：需要查询的ETF清单文件的筛选条件，其中合约代码可以为空，则默认所有存在的ETF合约代码，market字段也可以为初始值，则默认所有市场的ETF合约

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

cpp
    
    
    ///查询股票ETF合约基本情况--请求结构体,
    ///请求参数为多条件参数:1,不填则返回所有市场的ETF合约信息。
    ///                  2,只填写market,返回该交易市场下结果
    ///                   3,填写market及ticker参数,只返回该etf信息。
    //////////////////////////////////////////////////////////////////////////
    struct XTPQueryETFBaseReq
    {
    	///交易市场
    	XTP_MARKET_TYPE    market;
    	///ETF买卖代码
    	char               ticker[XTP_TICKER_LEN];
    	/// 预留
    	char               unused[4];    
    };

cpp
    
    
    ///@brief XTP_MARKET_TYPE市场类型，交易里使用
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_MKT_UNKNOWN = 7;

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 可以指定ticker，查询单个ETF
    if (user_trade_api_)
    {
    	XTPQueryETFBaseReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryETFBaseReq));
    
    	query_param.market = XTP_MKT_SH_A;
    	std::string stdstr_ticker = "xxxxxx";
    	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
    
    	int ret = user_trade_api_->QueryETF(&query_param, session_id, request_id);
    }

cpp
    
    
    // 可以ticker为0,查询全市场
    if (user_trade_api_)
    {
    	XTPQueryETFBaseReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryETFBaseReq));
    
    	int ret = user_trade_api_->QueryETF(&query_param, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryETF(XTPQueryETFBaseRsp *etf_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)etf_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.39. QueryETFTickerBasket ​

请求查询ETF股票篮。

◇ 1.函数原型

cpp
    
    
    virtual int QueryETFTickerBasket(XTPQueryETFComponentReq *query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param：需要查询股票篮的的ETF合约，其中合约代码不可以为空，market字段也必须指定

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

cpp
    
    
    //////////////////////////////////////////////////////////////////////////
    ///查询股票ETF合约成分股信息--请求结构体,请求参数为:交易市场+ETF买卖代码
    //////////////////////////////////////////////////////////////////////////
    typedef struct XTPQueryETFComponentReq
    {
    	///ETF买卖代码
    	char               ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE    market;
    	/// 预留
    	char               unused[4]; 
    }XTPQueryETFComponentReq;

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
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

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryETFBasket(XTPQueryETFComponentRsp *etf_component_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)etf_component_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.40. QueryIPOInfoList ​

请求查询今日新股申购信息列表。

◇ 1.函数原型

cpp
    
    
    virtual int QueryIPOInfoList(uint64_t session_id, int request_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询今日新股申购信息列表
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QueryIPOInfoList(session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)ipo_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.41. QueryIPOQuotaInfo ​

请求查询用户新股申购额度信息。

◇ 1.函数原型

cpp
    
    
    virtual int QueryIPOQuotaInfo(uint64_t session_id, int request_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询用户新股申购额度信息
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QueryIPOQuotaInfo(session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryIPOQuotaInfo(XTPQueryIPOQuotaRsp *quota_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)quota_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.42. QueryBondIPOInfoList ​

请求查询今日可转债申购信息列表。

◇ 1.函数原型

cpp
    
    
    virtual int QueryBondIPOInfoList(uint64_t session_id, int request_id) = 0;

◇ 2.参数

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询用户今日可转债申购信息列表
    if (user_trade_api_)
    {
    	int ret = user_trade_api_->QueryBondIPOInfoList(session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryBondIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)ipo_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


#### 5.2.43. QueryBondSwapStockInfo ​

请求查询用户可转债转股信息。

◇ 1.函数原型

cpp
    
    
    virtual int QueryBondSwapStockInfo(XTPQueryBondSwapStockReq *query_param, uint64_t session_id, int request_id) = 0;

◇ 2.参数

query_param：需要查询的可转债转股信息的筛选条件，可以为NULL（为NULL表示查询所有的可转债转股信息），此参数中合约代码可以为空字符串，如果为空字符串，则查询所有可转债转股信息，如果不为空字符串，请不带空格，并以'\0'结尾，且必须与market匹配

session_id：资金账户对应的session_id,登录时得到

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询用户可转债转股信息
    // 可以指定ticker，查询单个可转债转股
    if (user_trade_api_)
    {
    	XTPQueryBondSwapStockReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryBondSwapStockReq));
    
    	query_param.market = XTP_MKT_SH_A;
    	std::string stdstr_ticker = "xxxxxx";
    	strncpy(query_param.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
    
    	int ret = user_trade_api_->QueryBondSwapStockInfo(&query_param, session_id, request_id);
    }

cpp
    
    
    // 查询所有的可转债转股信息
    if (user_trade_api_)
    {
    	XTPQueryBondSwapStockReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryBondSwapStockReq));
    
    	int ret = user_trade_api_->QueryBondSwapStockInfo(&query_param, session_id, request_id);
    }

◇ 5.响应函数

cpp
    
    
    virtual void OnQueryBondSwapStockInfo(XTPQueryBondSwapStockRsp *swap_stock_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)swap_stock_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

  


  
  


### 5.3. TraderSpi ​

TraderSpi类提供了交易相关的回调接口，用户需要继承该类并重写这些接口，以获取响应数据。

#### 5.3.1. 接口 ​

cpp
    
    
    namespace XTPX {
    	namespace API {
    
    		class TraderSpi
    		{
    		public:
    
    			///当客户端的某个连接与交易后台通信连接断开时，该方法被调用。
    			///@param reason 错误原因，请与错误代码表对应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 用户主动调用logout导致的断线，不会触发此函数。api不会自动重连，当断线发生时，请用户自行选择后续操作，可以在此函数中调用Login重新登录，并更新session_id，此时用户收到的数据跟断线之前是连续的
    			virtual void OnDisconnected(uint64_t session_id, int reason) { (void)session_id; (void)reason; };
    
    			///当登录成功后，中途出现某个服务（资金划拨或者查询）服务状态改变时，该方法将被调用。
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@param server_type 服务类型，1-资金划拨服务，2-查询服务
    			///@param status 服务是否可用标识，false-服务不可用，true-服务恢复可用
    			///@remark 用户登录成功时，默认服务可用。当用户收到服务不可用的通知时，之前没有完成的查询，将不再推送后续的查询消息，需要用户等待查询服务恢复后重新发起查询。
    			virtual void OnServerStatusNotification(uint64_t session_id, uint32_t server_type, bool status) { (void)session_id; (void)server_type; (void)status; };
    
    			///错误应答
    			///@param error_info 当服务器响应发生错误时的具体的错误代码和错误信息,当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@remark 此函数只有在服务器发生错误时才会调用，一般无需用户处理
    			virtual void OnError(XTPRI *error_info) { (void)error_info; };
    
    
    			///当客户认证成功时，该方法被调用。		
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@param user_name 登录用户名，login时传入的
    			///@remark 用户收到此回调，仅表明已经认证成功，此时还不能向服务器发送报单和查询等操作，需要等login返回才能进行后续下单操作，此处可提前记录并更新用户名与session_id的对应关系
    			virtual void OnConnect(uint64_t session_id, const char* user_name) { (void)session_id; (void)user_name; };
    
    			///断线重连后，所有需要重传的推送消息（成交回报、订单响应）接收结束通知
    			///@param session_id 账户对应的session_id，登录时得到
    			///@remark 此函数在用户使用quick第一次登录时，不会有触发。只有在API与服务器以restart方式登录时，或者api与服务器非主动断线，且用户重新login后，进行resume消息重传时，当推送消息重传结束时才会调用，收到此通知就表明断线时的推送消息已经接受完毕，后面收到的推送消息将是实时推送消息
    			virtual void OnResumeEnd(uint64_t session_id) { (void)session_id; };
    
    			///报单未知状态通知
    			///@param order_xtp_id 未知状态订单的xtp id
    			///@param session_id 账户对应的session_id，登录时得到
    			///@remark 此响应仅表明XTP服务器丢失订单，并没有报送到交易所。
    			virtual void OnUnknownOrder(uint64_t order_xtp_id, uint64_t session_id) { (void)order_xtp_id; (void)session_id; };
    
    			///报单初始状态通知
    			///@param order_info 订单响应具体信息，用户可以通过order_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单
    			///@param session_id 账户对应的session_id，登录时得到
    			///@remark 此响应仅表明XTP服务器收到了报单且没被OMS拒单（OMS内部拒单将没有这条ack消息，仅有OrderEvent的拒单消息），不代表已经报送到交易所
    			virtual void OnOrderAck(XTPOrderInfo *order_info, uint64_t session_id) { (void)order_info; (void)session_id; };
    
    // 			///请求查询用户在本节点上可交易市场的响应
    // 			///@param trade_location 查询到的交易市场信息，按位来看，从低位开始数，第0位表示沪市，即如果(trade_location&0x01) == 0x01，代表可交易沪市，第1位表示深市，即如果(trade_location&0x02) == 0x02，表示可交易深市，如果第0位和第1位均是1，即(trade_location&(0x01|0x02)) == 0x03，就表示可交易沪深2个市场
    // 			///@param error_info 查询可交易市场发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    // 			///@param request_id 此消息响应函数对应的请求ID
    // 			///@param session_id 资金账户对应的session_id，登录时得到
    // 			///@remark 此查询只会有一个结果
    // 			virtual void OnQueryAccountTradeMarket(int trade_location, XTPRI *error_info, int request_id, uint64_t session_id) {};
    
    			///报单通知
    			///@param order_info 订单响应具体信息，用户可以通过order_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单，order_info.qty_left字段在订单为未成交、部成、全成、废单状态时，表示此订单还没有成交的数量，在部撤、全撤状态时，表示此订单被撤的数量。order_info.order_cancel_xtp_id为其所对应的撤单ID，不为0时表示此单被撤成功
    			///@param error_info 订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 每次订单状态更新时，都会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，在订单未成交、全部成交、全部撤单、部分撤单、已拒绝这些状态时会有响应，对于部分成交的情况，请由订单的成交回报来自行确认。所有登录了此用户的客户端都将收到此用户的订单响应
    			virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) { (void)order_info; (void)error_info; (void)session_id; };
    
    			///成交通知
    			///@param trade_info 成交回报的具体信息，用户可以通过trade_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。对于上交所，exec_id可以唯一标识一笔成交。当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交了。对于深交所，exec_id是唯一的，暂时无此判断机制。report_index+market字段可以组成唯一标识表示成交回报。
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 订单有成交发生的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的成交回报。相关订单为部成状态，需要用户通过成交回报的成交数量来确定，OnOrderEvent()不会推送部成状态。
    			virtual void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id) { (void)trade_info; (void)session_id; };
    
    			///撤单出错响应
    			///@param cancel_info 撤单具体信息，包括撤单的order_cancel_xtp_id和待撤单的order_xtp_id
    			///@param error_info 撤单被拒绝或者发生错误时错误代码和错误信息，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 此响应只会在撤单发生错误时被回调
    			virtual void OnCancelOrderError(XTPOrderCancelErrorInfo *cancel_info, XTPRI *error_info, uint64_t session_id) { (void)cancel_info; (void)error_info; (void)session_id; };
    
    			///请求查询报单响应
    			///@param order_info 查询到的一个报单
    			///@param error_info 查询报单时发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
    			virtual void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    // 			///请求查询报单响应-新版本接口
    // 			///@param order_info 查询到的一个报单信息
    // 			///@param error_info 查询报单时发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    // 			///@param request_id 此消息响应函数对应的请求ID
    // 			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    // 			///@param session_id 资金账户对应的session_id，登录时得到
    // 			///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    // 			virtual void OnQueryOrderEx(XTPOrderInfoEx *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///分页请求查询报单响应
    			///@param order_info 查询到的一个报单
    			///@param req_count 分页请求的最大数量
    			///@param order_sequence 分页请求的当前回报数量
    			///@param query_reference 当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果order_sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
    			virtual void OnQueryOrderByPage(XTPQueryOrderRsp *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)req_count; (void)order_sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };
    
    // 			///分页请求查询报单响应
    // 			///@param order_info 查询到的一个报单
    // 			///@param req_count 分页请求的最大数量
    // 			///@param order_sequence 分页请求的当前回报数量
    // 			///@param query_reference 当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
    // 			///@param request_id 此消息响应函数对应的请求ID
    // 			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    // 			///@param session_id 资金账户对应的session_id，登录时得到
    // 			///@remark 当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果order_sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
    // 			virtual void OnQueryOrderByPageEx(XTPOrderInfoEx *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)req_count; (void)order_sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询成交响应
    			///@param trade_info 查询到的一个成交回报
    			///@param error_info 查询成交回报发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
    			virtual void OnQueryTrade(XTPQueryTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)trade_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///分页请求查询成交响应
    			///@param trade_info 查询到的一个成交信息
    			///@param req_count 分页请求的最大数量
    			///@param trade_sequence 分页请求的当前回报数量
    			///@param query_reference 当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 当trade_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果trade_sequence等于req_count，那么表示还有回报，可以进行下一次分页查询，如果不等，表示所有回报已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
    			virtual void OnQueryTradeByPage(XTPQueryTradeRsp *trade_info, int64_t req_count, int64_t trade_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)trade_info; (void)req_count; (void)trade_sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询投资者持仓响应
    			///@param position 查询到的一只股票的持仓情况
    			///@param error_info 查询账户持仓发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 由于用户可能持有多个股票，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryPosition(XTPQueryStkPositionRsp *position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)position; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询用户证券账户信息响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param account_info 查询到的用户证券账户信息
    			///@param error_info 查询用户证券账户信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQuerySecurityAccount(XTPQueryAccountIdRsp *account_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)account_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询资金账户响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param asset 查询到的资金账户情况
    			///@param error_info 查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryAsset(XTPQueryAssetRsp *asset, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)asset; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询资金划拨订单响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param fund_transfer_info 查询到的资金账户情况
    			///@param fund_transfer_err_info 返回的资金划拨订单fund_transfer_info划拨失败时的错误信息，当fund_transfer_err_info为空，或者fund_transfer_err_info.error_id为0时，表明划转成功，没有错误
    			///@param error_info 查询资金划拨订单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明查询没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryFundTransfer(XTPFundTransferLog *fund_transfer_info, XTPRI *fund_transfer_err_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)fund_transfer_info; (void)fund_transfer_err_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///分页请求查询资金划拨订单响应
    			///@param fund_transfer_info 查询到的一个资金划拨订单
    			///@param fund_transfer_err_info 返回的资金划拨订单order_info划拨失败时的错误信息，当fund_transfer_err_info为空，或者fund_transfer_err_info.error_id为0时，表明划转成功，没有错误
    			///@param error_info 分页查询资金资金划拨订单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明查询没有错误
    			///@param req_count 分页请求的最大数量
    			///@param sequence 分页请求的当前回报数量
    			///@param query_reference 当前资金划拨订单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
    			virtual void OnQueryFundTransferByPage(XTPFundTransferLog *fund_transfer_info, XTPRI *fund_transfer_err_info, XTPRI *error_info, int64_t req_count, int64_t sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)fund_transfer_info; (void)fund_transfer_err_info; (void)error_info; (void)req_count; (void)sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };
    
    			///资金划拨通知
    			///@param fund_transfer_info 资金划拨通知的具体信息，用户可以通过fund_transfer_info.serial_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。
    			///@param error_info 资金划拨订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误。当资金划拨方向为一号两中心节点之间划拨，且error_info.error_id=11000384时，error_info.error_msg中含有对方结点中可用于划拨的资金（以整数为准），用户需解析后进行stringToInt的转化，可据此填写合适的资金，再次发起划拨请求
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 当资金划拨订单有状态变化的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的资金划拨通知。
    			virtual void OnFundTransfer(XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info, uint64_t session_id) { (void)fund_transfer_info; (void)error_info; (void)session_id; };
    
    			///资金划拨订单未知状态通知
    			///@param serial_id 未知状态资金划拨订单的serial id
    			///@param session_id 账户对应的session_id，登录时得到
    			///@remark 此响应仅表明XTP资金划拨服务器丢失订单，并没有报送到后台。
    			virtual void OnUnknownFundTransfer(uint64_t serial_id, uint64_t session_id) { (void)serial_id; (void)session_id; };
    
    			///请求查询其他节点可用资金的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param fund_info 查询到的其他节点可用资金情况
    			///@param error_info 查询其他节点可用资金发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryOtherServerFund(XTPFundQueryRsp *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) { (void)fund_info; (void)error_info; (void)request_id; (void)session_id; };
    
    			///请求查询ETF清单文件的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param etf_info 查询到的ETF清单文件情况
    			///@param error_info 查询ETF清单文件发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryETF(XTPQueryETFBaseRsp *etf_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)etf_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询ETF股票篮的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param etf_component_info 查询到的ETF合约的相关成分股信息
    			///@param error_info 查询ETF股票篮发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryETFBasket(XTPQueryETFComponentRsp *etf_component_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)etf_component_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询今日新股申购信息列表的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param ipo_info 查询到的今日新股申购的一只股票信息
    			///@param error_info 查询今日新股申购信息列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)ipo_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询用户新股申购额度信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param quota_info 查询到的用户某个市场的今日新股申购额度信息
    			///@param error_info 查查询用户新股申购额度信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryIPOQuotaInfo(XTPQueryIPOQuotaRsp *quota_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)quota_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询今日可转债申购信息列表的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param ipo_info 查询到的今日可转债申购的一只可转债信息
    			///@param error_info 查询今日可转债申购信息列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryBondIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)ipo_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    			///请求查询用户可转债转股信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			///@param swap_stock_info 查询到某条可转债转股信息
    			///@param error_info 查查询可转债转股信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param session_id 资金账户对应的session_id，登录时得到
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryBondSwapStockInfo(XTPQueryBondSwapStockRsp *swap_stock_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)swap_stock_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    		};
    	}
    }

  


#### 5.3.2. 代码示例 ​

MyTraderSpi继承TraderSpi 以下是MyTraderSpi.h文件

cpp
    
    
    #include "xtpx_trader_api.h"
    
    using namespace XTPX::API;
    
    class MyTraderSpi : public TraderSpi
    {
    public:
    	explicit MyTraderSpi();
    	~MyTraderSpi();
    
    	// 查询报单响应
    	void OnQueryOrder(XTPOrderInfo *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id);
    	// 报单初始状态通知
    	void OnOrderAck(XTPOrderInfo *order_info, uint64_t session_id);
    	// 报单通知
    	void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id);
    	// 成交通知
    	void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id);
    };

以下是MyTraderSpi.cpp文件

cpp
    
    
    #include "MyTraderSpi.h"
    
    MyTraderSpi::MyTraderSpi() { }
    MyTraderSpi::~MyTraderSpi() { }
    
    // 查询报单响应
    void MyTraderSpi::OnQueryOrder(XTPOrderInfo *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id)
    {
    	std::cout << "OnQueryOrder." << std::endl;
    }
    
    // 报单初始状态通知
    void MyTraderSpi::OnOrderAck(XTPOrderInfo *order_info, uint64_t session_id)
    {
    	std::cout << "OnOrderAck." << std::endl;
    }
    
    // 报单通知
    void MyTraderSpi::OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id)
    {
    	std::cout << "OnOrderEvent." << std::endl;
    }
    
    // 成交通知
    void MyTraderSpi::OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id)
    {
    	std::cout << "OnTradeEvent." << std::endl;
    }

  


#### 5.3.3. OnDisconnected ​

当客户端的某个连接与交易后台通信连接断开时，该方法被调用。

用户主动调用logout导致的断线，不会触发此函数。api不会自动重连，当断线发生时，请用户自行选择后续操作，可以在此函数中调用Login重新登录，并更新session_id，此时用户收到的数据跟断线之前是连续的。

◇ 1.函数原型

cpp
    
    
    virtual void OnDisconnected(uint64_t session_id, int reason) { (void)session_id; (void)reason; };

◇ 2.参数

Reason：错误原因，请与错误代码表对应

session_id：资金账户对应的session_id，登录时得到

◇ 3.返回

无

◇ 4.示例代码

以下是MyTraderSpi.h文件

cpp
    
    
    #include "xtpx_trader_api.h"
    #include <iostream>
    #include <functional>
    
    using namespace std;
    using namespace XTPX::API;
    
    class MyTraderSpi : public TraderSpi
    {
    public:
    	explicit MyTraderSpi();
    	~MyTraderSpi();
    	
    	void bindTraderFunc(std::function<void(void)> f)
        {
            _disconnect = f;
        }
    
    private:
        std::function<void(void)> _disconnect;
    }

以下是MyTraderSpi.cpp文件

cpp
    
    
    #include "MyTraderSpi.h"
    
    MyTraderSpi::MyTraderSpi() { }
    MyTraderSpi::~MyTraderSpi() { }
    
    void MyTraderSpi::OnDisconnected(uint64_t session_id, int reason)
    {
    	std::cout << "trader is disconnected." << std::endl;
    	// 重连通知
    	_disconnect();
    }

以下是MyTraderApi.h文件

cpp
    
    
    #include "xtpx_trader_api.h"
    #include "MyTraderSpi.h"
    
    // 登录信息缓存
    struct LoginTraderInfo
    {
        LoginTraderInfo()
        {
            trade_server_port = 0;
    		trade_sock_type = XTP_PROTOCOL_TCP;
        }
    
        std::string trade_server_ip;
        int trade_server_port;
        std::string account_name;
        std::string account_pw;
        XTP_PROTOCOL_TYPE trade_sock_type;
    	std::string local_ip;
    };
    
    using namespace XTPX::API;
    
    class MyTraderApi
    {
    public:
    	explicit MyTraderApi();
    	~MyTraderApi();
    
    	// 重连函数
    	void reloginTrader();
    
    private: 
    	LoginTraderInfo m_loginTraderInfo;
    };

以下是MyTraderApi.cpp文件

cpp
    
    
    #include "MyTraderApi.h"
    #ifdef _WIN32
        #include <windows.h>
    #else
        #include <unistd.h>
    #endif
    
    MyTraderApi::MyTraderApi()
    {
    }
    
    // 创建并初始化交易API
    bool MyTraderApi::initialize()
    {
    	user_trade_api_ = XTPX::API::TraderApi::CreateTraderApi(1, "./", XTP_LOG_LEVEL_DEBUG);
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
            while (i_counter < 3) {
                i_counter++;
    			
    			uint64_t ret = user_trade_api_->Login(m_loginTraderInfo.trade_server_ip.c_str(),
                                                 m_loginTraderInfo.trade_server_port,
                                                 m_loginTraderInfo.account_name.c_str(),
                                                 m_loginTraderInfo.account_pw.c_str(),
                                                 m_loginTraderInfo.trade_sock_type,
                                                 m_loginTraderInfo.local_ip.c_str());
                if (ret != 0) {
    				std::cout << "relogin success." << std::endl;
                    session_id_ = ret;//登陆成功后更新session_id
    				return;
                } else {
    				std::cout << "relogin failed." << std::endl;
    #ifdef _WIN32
                    Sleep(5000);
    #else
                    sleep(5);
    #endif
                }
            }
    		std::cout << "relogin failed over 3 times." << std::endl;
        } else {
    		std::cout << "relogin info missing." << std::endl;
        }
    
    }

  


#### 5.3.4. OnServerStatusNotification ​

当登录成功后，中途出现某个服务（资金划拨或者查询）的状态改变时，该方法将被调用。

用户登录成功时，默认服务可用。当用户收到服务不可用的通知时，之前没有完成的查询，将不再推送后续的查询消息，需要用户等待查询服务恢复后重新发起查询。

◇ 1.函数原型

cpp
    
    
    virtual void OnServerStatusNotification(uint64_t session_id, uint32_t server_type, bool status) { (void)session_id; (void)server_type; (void)status; };

◇ 2.参数

session_id: 资金账户对应的session_id，登录时得到

server_type: 服务类型，1-资金划拨服务，2-查询服务

status: 服务是否可用标识，false-服务不可用，true-服务恢复可用

◇ 3.返回

无   


#### 5.3.5. OnError ​

错误应答。

此函数只有在服务器发生错误时才会调用，一般无需用户处理。

◇ 1.函数原型

cpp
    
    
    virtual void OnError(XTPRI *error_info) {};

◇ 2.参数

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

cpp
    
    
    namespace XTPX {
    
    	namespace API {
    		///错误信息的字符串长度
    		constexpr int32_t XTP_ERR_MSG_LEN = 124;
    		///响应信息
    		typedef struct XTPRspInfoStruct
    		{
    			///错误代码
    			int32_t	error_id;
    			///错误信息
    			char	error_msg[XTP_ERR_MSG_LEN];
    		} XTPRI;
    	}
    }

◇ 3.返回

无   


#### 5.3.6. OnConnect ​

当客户认证成功时，该方法被调用。

用户收到此回调，仅表明已经认证成功，此时还不能向服务器发送报单和查询等操作，需要等login返回才能进行后续下单操作，此处可提前记录并更新用户名与session_id的对应关系。

◇ 1.函数原型

cpp
    
    
    virtual void OnConnect(uint64_t session_id, const char* user_name) { (void)session_id; (void)user_name; };

◇ 2.参数

session_id: 资金账户对应的session_id，登录时得到

user_name: 登录用户名，login时传入的

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    //用户登录请求
    virtual uint64_t Login(const char* ip, int port, const char* user, const char* password, XTP_PROTOCOL_TYPE sock_type, const char* local_ip = NULL) = 0;

  


#### 5.3.7. OnResumeEnd ​

断线重连后，所有需要重传的推送消息（成交回报、订单响应）接收结束通知。

此函数在用户使用quick第一次登录时，不会有触发。只有在API与服务器以restart方式登录时，或者api与服务器非主动断线，且用户重新login后，进行resume消息重传时，当推送消息重传结束时才会调用，收到此通知就表明断线时的推送消息已经接受完毕，后面收到的推送消息将是实时推送消息。

◇ 1.函数原型

cpp
    
    
    virtual void OnResumeEnd(uint64_t session_id) { (void)session_id; };

◇ 2.参数

session_id: 资金账户对应的session_id，登录时得到

◇ 3.返回

无   


#### 5.3.8. OnUnknownOrder ​

报单未知状态通知。

此响应仅表明XTP服务端未收到过该订单，且没有报送到交易所。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnknownOrder(uint64_t order_xtp_id, uint64_t session_id) { (void)order_xtp_id; (void)session_id; };

◇ 2.参数

order_xtp_id: 未知状态订单的xtp id

session_id: 账户对应的session_id，登录时得到

◇ 3.返回

无   


#### 5.3.9. OnOrderAck ​

报单初始状态通知。

此响应仅表明XTP服务器收到了报单且没被OMS拒单（OMS内部拒单将没有这条ack消息，仅有OrderEvent的拒单消息），不代表已经报送到交易所。

◇ 1.函数原型

cpp
    
    
    virtual void OnOrderAck(XTPOrderInfo *order_info, uint64_t session_id) { (void)order_info; (void)session_id; };

◇ 2.参数

order_info: 订单响应具体信息，用户可以通过order_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单

session_id: 账户对应的session_id，登录时得到

cpp
    
    
    ///报单响应结构体
    struct XTPOrderInfo
    {
    	///订单号
    	uint64_t                order_xtp_id;
    	///证券代码
    	char                    ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE         market;
    	///用户自定义字段
    	uint32_t                order_client_id;
    	///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    	char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    	///订单执行状态，与交易所回报ExecType字段一致，‘0’-新订单，‘4’-已撤销，‘8’-已拒绝，‘F’-已成交；如果是非交易所的回报，此字段为0
    	char                    exec_type;
    	///订单状态
    	XTP_ORDER_STATUS_TYPE   order_status;
    	///交易所订单编号
    	char                    order_exch_id[XTP_ORDER_EXCH_LEN];
    	///报单类型
    	TXTPOrderTypeType       order_type;
    	///买卖方向
    	XTP_SIDE_TYPE           side;
    	///开平标志
    	XTP_POSITION_EFFECT_TYPE    position_effect;
    	///报单提交状态，可以用来区分是否是撤单
    	XTP_ORDER_SUBMIT_STATUS_TYPE   order_submit_status;
    	///订单数量
    	int64_t                 quantity;
    	///订单价格
    	double                  price;
    	///价格类型
    	XTP_PRICE_TYPE          price_type;
    	///业务类型
    	XTP_BUSINESS_TYPE       business_type;
    	///撤单在XTP系统中的id，在XTP系统中唯一（仅撤单成功时有效，此字段为0则表示没有撤单）
    	uint64_t                order_cancel_xtp_id;
    	///成交金额，为此订单的成交总金额
    	double                  trade_amount;
    	///今成交数量，为此订单累计成交数量
    	int64_t                 qty_traded;
    	///剩余数量
    	int64_t                 qty_left;
    	///预扣金额，为此订单的预扣金额（包含预扣手续费，此金额不会改变，仅供参考）
    	double                  order_withhold_amount;
    	///预扣手续费，为此订单的预扣手续费（此金额不会改变，仅供参考）
    	double                  order_withhold_fee;
    	///执行编号
    	char                    exec_id[XTP_EXEC_ID_LEN];
    	///算法策略类型，仅为算法单时有效
    	uint16_t                strategy_type;
    	///平台分区号
    	int32_t                 set_id;
    	///执行报告编号
    	uint64_t                report_index;
    	///回报时间
    	uint64_t                transact_time;
    	///委托时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                insert_time;
    	///最后修改时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                update_time;
    	///撤销时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                cancel_time;
    	///算法母单编号ID，仅为算法单时有效
    	uint64_t                strategy_id;
    	///XTP拒单原因代码
    	uint32_t                error_code;
    	///外部系统拒单原因代码
    	uint32_t                extra_error_code;
    	/// 证券账户（股卡）
    	char                    account_id[XTP_ACCOUNT_ID_LEN];
    	///交易所PBU代码 
    	char                    branch_pbu[XTP_BRANCH_PBU_LEN];
    	/// 预留
    	char                    unused[8];
    };

cpp
    
    
    ///@brief XTP_MARKET_TYPE市场类型，交易里使用
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_MKT_UNKNOWN = 7;

cpp
    
    
    ///@brief XTP_ORDER_STATUS_TYPE是报单状态类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_ORDER_STATUS_TYPE;
    
    ///初始化
    constexpr uint32_t XTP_ORDER_STATUS_INIT = 0;
    ///全部成交
    constexpr uint32_t XTP_ORDER_STATUS_ALLTRADED = 1;           
    ///部分成交
    constexpr uint32_t XTP_ORDER_STATUS_PARTTRADEDQUEUEING = 2;
    ///部分撤单
    constexpr uint32_t XTP_ORDER_STATUS_PARTTRADEDNOTQUEUEING = 3; 
    ///未成交
    constexpr uint32_t XTP_ORDER_STATUS_NOTRADEQUEUEING = 4;   
    ///已撤单
    constexpr uint32_t XTP_ORDER_STATUS_CANCELED = 5;  
    ///已拒绝
    constexpr uint32_t XTP_ORDER_STATUS_REJECTED = 6; 
    ///未知订单状态
    constexpr uint32_t XTP_ORDER_STATUS_UNKNOWN = 7;

cpp
    
    
    ///TXTPOrderTypeType是报单类型类型
    /////////////////////////////////////////////////////////////////////////
    typedef char TXTPOrderTypeType;
    
    ///正常
    constexpr char XTP_ORDT_Normal = '0';
    ///报价衍生
    constexpr char XTP_ORDT_DeriveFromQuote = '1';
    ///组合衍生
    constexpr char XTP_ORDT_DeriveFromCombination = '2';
    ///组合报单
    constexpr char XTP_ORDT_Combination = '3';
    ///条件单
    constexpr char XTP_ORDT_ConditionalOrder = '4';
    ///互换单
    constexpr char XTP_ORDT_Swap = '5';

cpp
    
    
    /////////////////////////////////////////////////////////////////////////
    ///@brief XTP_SIDE_TYPE是买卖方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_SIDE_TYPE;
    
    ///买（新股申购，ETF买，配股，信用交易中担保品买）
    constexpr uint32_t XTP_SIDE_BUY = 1;
    ///卖（逆回购，ETF卖，信用交易中担保品卖）
    constexpr uint32_t XTP_SIDE_SELL = 2;
    ///申购
    constexpr uint32_t XTP_SIDE_PURCHASE = 7;
    ///赎回
    constexpr uint32_t XTP_SIDE_REDEMPTION = 8;
    ///拆分
    constexpr uint32_t XTP_SIDE_SPLIT = 9;
    ///合并
    constexpr uint32_t XTP_SIDE_MERGE = 10;
    ///改版之后的side的备兑，暂不支持
    constexpr uint32_t XTP_SIDE_COVER = 11;
    ///改版之后的side锁定（对应开平标识为开）/解锁（对应开平标识为平）
    constexpr uint32_t XTP_SIDE_FREEZE = 12;
    /// 融资买入
    constexpr uint32_t XTP_SIDE_MARGIN_TRADE = 21;
    /// 融券卖出
    constexpr uint32_t XTP_SIDE_SHORT_SELL = 22;
    /// 卖券还款
    constexpr uint32_t XTP_SIDE_REPAY_MARGIN = 23;
    /// 买券还券
    constexpr uint32_t XTP_SIDE_REPAY_STOCK = 24;
    /// 现金还款（不放在普通订单协议，另加请求和查询协议）
    //		constexpr uint32_t XTP_SIDE_CASH_REPAY_MARGIN = 25;
    /// 现券还券
    constexpr uint32_t XTP_SIDE_STOCK_REPAY_STOCK = 26;
    /// 余券划转
    constexpr uint32_t XTP_SIDE_SURSTK_TRANS = 27;
    /// 担保品转入
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSIN = 28;
    /// 担保品转出
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSOUT = 29;
    
    ///组合策略的组合
    constexpr uint32_t XTP_SIDE_OPT_COMBINE = 31; 
    ///组合策略的拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT = 32; 
    ///组合策略的管理员强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE = 33; 
    ///组合策略的交易所强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE_EXCH = 34;
    
    ///未知或者无效买卖方向
    constexpr uint32_t XTP_SIDE_UNKNOWN = 50;

cpp
    
    
    ///@brief XTP_POSITION_EFFECT_TYPE是开平标识类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_POSITION_EFFECT_TYPE;
    
    /// 初始值或未知值开平标识，除期权外，均使用此值
    constexpr uint32_t XTP_POSITION_EFFECT_INIT = 0;
    /// 开
    constexpr uint32_t XTP_POSITION_EFFECT_OPEN = 1;
    /// 平
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSE = 2;
    /// 强平
    constexpr uint32_t XTP_POSITION_EFFECT_FORCECLOSE = 3;
    /// 平今
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSETODAY = 4;
    /// 平昨
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSEYESTERDAY = 5;
    /// 强减
    constexpr uint32_t XTP_POSITION_EFFECT_FORCEOFF = 6;
    /// 本地强平
    constexpr uint32_t XTP_POSITION_EFFECT_LOCALFORCECLOSE = 7;
    /// 信用业务追保强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_COVER = 8;
    /// 信用业务清偿强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_CLEAR = 9;
    /// 信用业务合约到期强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_DEBT = 10;
    /// 信用业务无条件强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_UNCOND = 11;
    /// 未知的开平标识类型
    constexpr uint32_t XTP_POSITION_EFFECT_UNKNOWN = 12;

cpp
    
    
    ///@brief XTP_ORDER_SUBMIT_STATUS_TYPE是报单提交状态类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_ORDER_SUBMIT_STATUS_TYPE;
    
    ///订单已经提交
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_INSERT_SUBMITTED = 1;
    ///订单已经被接受
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_INSERT_ACCEPTED = 2;
    ///订单已经被拒绝
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_INSERT_REJECTED = 3;
    ///撤单已经提交
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_CANCEL_SUBMITTED = 4;
    ///撤单已经被拒绝
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_CANCEL_REJECTED = 5;
    ///撤单已经被接受
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_CANCEL_ACCEPTED = 6;

cpp
    
    
    ///@brief XTP_PRICE_TYPE是价格类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_PRICE_TYPE;
    
    ///限价单-沪 / 深 / 沪期权 / 深期权 （除普通股票业务外，其余未特指的业务均使用此种类型）
    constexpr uint32_t XTP_PRICE_LIMIT = 1;        
    ///即时成交剩余转撤销，市价单-深 / 沪期权 / 深期权
    constexpr uint32_t XTP_PRICE_BEST_OR_CANCEL = 2;        
    ///最优五档即时成交剩余转限价，市价单-沪
    constexpr uint32_t XTP_PRICE_BEST5_OR_LIMIT = 3;        
    ///最优5档即时成交剩余转撤销，市价单-沪深 / 深期权
    constexpr uint32_t XTP_PRICE_BEST5_OR_CANCEL = 4;        
    ///全部成交或撤销,市价单-深 / 沪期权 / 深期权
    constexpr uint32_t XTP_PRICE_ALL_OR_CANCEL = 5;        
    ///本方最优，市价单-沪深 / 深期权
    constexpr uint32_t XTP_PRICE_FORWARD_BEST = 6; 
    ///对手方最优，市价单-沪深 / 深期权    
    constexpr uint32_t XTP_PRICE_REVERSE_BEST_LIMIT = 7;        
    ///期权限价申报FOK
    constexpr uint32_t XTP_PRICE_LIMIT_OR_CANCEL = 8;        
    ///未知或者无效价格类型
    constexpr uint32_t XTP_PRICE_TYPE_UNKNOWN = 9;

cpp
    
    
    ///@brief XTP_BUSINESS_TYPE证券业务类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_BUSINESS_TYPE;
    
    ///普通股票业务（股票买卖，ETF买卖，沪市交易型货币基金等）
    constexpr uint32_t XTP_BUSINESS_TYPE_CASH = 0;            
    ///新股申购业务（对应的price type需选择限价类型）
    constexpr uint32_t XTP_BUSINESS_TYPE_IPOS = 1;
    ///回购业务（国债逆回购业务对应的price type填为限价，side填为卖）
    constexpr uint32_t XTP_BUSINESS_TYPE_REPO = 2;
    ///ETF申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_ETF = 3;
    ///融资融券业务
    constexpr uint32_t XTP_BUSINESS_TYPE_MARGIN = 4;              
    ///转托管（未支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_DESIGNATION = 5;
    ///配股业务（对应的price type需选择限价类型,side填为买）
    constexpr uint32_t XTP_BUSINESS_TYPE_ALLOTMENT = 6;
    ///分级基金申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION = 7;      
    ///分级基金拆分合并业务（业务已下线，不再支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE = 8;
    ///货币基金申赎业务（暂未支持，沪市交易型货币基金的买卖请使用普通股票业务）
    constexpr uint32_t XTP_BUSINESS_TYPE_MONEY_FUND = 9;
    ///期权业务       
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION = 10;
    ///行权
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE = 11;             
    ///锁定解锁，暂不支持
    constexpr uint32_t XTP_BUSINESS_TYPE_FREEZE = 12;             
    ///期权组合策略 组合和拆分业务
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION_COMBINE = 13;
    ///期权行权合并业务
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE_COMBINE = 14;    
    /// 债转股业务
    constexpr uint32_t XTP_BUSINESS_TYPE_BOND_SWAP_STOCK = 15;  
    ///未知类型   
    constexpr uint32_t XTP_BUSINESS_TYPE_UNKNOWN = 16;

cpp
    
    
    /// 本地报单编号的字符串长度
    constexpr uint32_t XTP_LOCAL_ORDER_LEN = 11;
    /// 交易所单号的字符串长度
    constexpr uint32_t XTP_ORDER_EXCH_LEN = 17;
    /// 用户股东账户的字符串长度
    constexpr uint32_t XTP_ACCOUNT_ID_LEN = 17;
    /// 交易所交易员代码字符串长度
    constexpr uint32_t XTP_BRANCH_PBU_LEN = 7;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 报单录入
    virtual uint64_t InsertOrder(XTPOrderInsertInfo *order, uint64_t session_id) = 0;
    //已经提前设置order_xtp_id的报单录入请求
    virtual uint64_t InsertOrderExtra(XTPOrderInsertInfo *order, uint64_t session_id) = 0;

#### 5.3.10. OnOrderEvent ​

报单通知。

每次订单状态更新时，都会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，在订单未成交、全部成交、全部撤单、部分撤单、已拒绝这些状态时会有响应，对于部分成交的情况，请由订单的成交回报来自行确认。所有登录了此用户的客户端都将收到此用户的订单响应。

◇ 1.函数原型

cpp
    
    
    virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id) { (void)order_info; (void)error_info; (void)session_id; };

◇ 2.参数

order_info：订单响应具体信息，用户可以通过order_info.order_xtp_id来管理订单，通过(GetClientIDByXTPID() == client_id)来过滤自己的订单，order_info.qty_left字段在订单为未成交、部成、全成、废单状态时，表示此订单还没有成交的数量，在部撤、全撤状态时，表示此订单被撤的数量。order_info.order_cancel_xtp_id为其所对应的撤单ID，不为0时表示此单被撤成功

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///报单响应结构体
    struct XTPOrderInfo
    {
    	///订单号
    	uint64_t                order_xtp_id;
    	///证券代码
    	char                    ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE         market;
    	///用户自定义字段
    	uint32_t                order_client_id;
    	///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    	char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    	///订单执行状态，与交易所回报ExecType字段一致，‘0’-新订单，‘4’-已撤销，‘8’-已拒绝，‘F’-已成交；如果是非交易所的回报，此字段为0
    	char                    exec_type;
    	///订单状态
    	XTP_ORDER_STATUS_TYPE   order_status;
    	///交易所订单编号
    	char                    order_exch_id[XTP_ORDER_EXCH_LEN];
    	///报单类型
    	TXTPOrderTypeType       order_type;
    	///买卖方向
    	XTP_SIDE_TYPE           side;
    	///开平标志
    	XTP_POSITION_EFFECT_TYPE    position_effect;
    	///报单提交状态，可以用来区分是否是撤单
    	XTP_ORDER_SUBMIT_STATUS_TYPE   order_submit_status;
    	///订单数量
    	int64_t                 quantity;
    	///订单价格
    	double                  price;
    	///价格类型
    	XTP_PRICE_TYPE          price_type;
    	///业务类型
    	XTP_BUSINESS_TYPE       business_type;
    	///撤单在XTP系统中的id，在XTP系统中唯一（仅撤单成功时有效，此字段为0则表示没有撤单）
    	uint64_t                order_cancel_xtp_id;
    	///成交金额，为此订单的成交总金额
    	double                  trade_amount;
    	///今成交数量，为此订单累计成交数量
    	int64_t                 qty_traded;
    	///剩余数量
    	int64_t                 qty_left;
    	///预扣金额，为此订单的预扣金额（包含预扣手续费，此金额不会改变，仅供参考）
    	double                  order_withhold_amount;
    	///预扣手续费，为此订单的预扣手续费（此金额不会改变，仅供参考）
    	double                  order_withhold_fee;
    	///执行编号
    	char                    exec_id[XTP_EXEC_ID_LEN];
    	///算法策略类型，仅为算法单时有效
    	uint16_t                strategy_type;
    	///平台分区号
    	int32_t                 set_id;
    	///执行报告编号
    	uint64_t                report_index;
    	///回报时间
    	uint64_t                transact_time;
    	///委托时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                insert_time;
    	///最后修改时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                update_time;
    	///撤销时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                cancel_time;
    	///算法母单编号ID，仅为算法单时有效
    	uint64_t                strategy_id;
    	///XTP拒单原因代码
    	uint32_t                error_code;
    	///外部系统拒单原因代码
    	uint32_t                extra_error_code;
    	/// 证券账户（股卡）
    	char                    account_id[XTP_ACCOUNT_ID_LEN];
    	///交易所PBU代码 
    	char                    branch_pbu[XTP_BRANCH_PBU_LEN];
    	/// 预留
    	char                    unused[8];
    };

cpp
    
    
    ///@brief XTP_MARKET_TYPE市场类型，交易里使用
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_MKT_UNKNOWN = 7;

cpp
    
    
    ///@brief XTP_ORDER_STATUS_TYPE是报单状态类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_ORDER_STATUS_TYPE;
    
    ///初始化
    constexpr uint32_t XTP_ORDER_STATUS_INIT = 0;
    ///全部成交
    constexpr uint32_t XTP_ORDER_STATUS_ALLTRADED = 1;           
    ///部分成交
    constexpr uint32_t XTP_ORDER_STATUS_PARTTRADEDQUEUEING = 2;
    ///部分撤单
    constexpr uint32_t XTP_ORDER_STATUS_PARTTRADEDNOTQUEUEING = 3; 
    ///未成交
    constexpr uint32_t XTP_ORDER_STATUS_NOTRADEQUEUEING = 4;   
    ///已撤单
    constexpr uint32_t XTP_ORDER_STATUS_CANCELED = 5;  
    ///已拒绝
    constexpr uint32_t XTP_ORDER_STATUS_REJECTED = 6; 
    ///未知订单状态
    constexpr uint32_t XTP_ORDER_STATUS_UNKNOWN = 7;

cpp
    
    
    ///TXTPOrderTypeType是报单类型类型
    /////////////////////////////////////////////////////////////////////////
    typedef char TXTPOrderTypeType;
    
    ///正常
    constexpr char XTP_ORDT_Normal = '0';
    ///报价衍生
    constexpr char XTP_ORDT_DeriveFromQuote = '1';
    ///组合衍生
    constexpr char XTP_ORDT_DeriveFromCombination = '2';
    ///组合报单
    constexpr char XTP_ORDT_Combination = '3';
    ///条件单
    constexpr char XTP_ORDT_ConditionalOrder = '4';
    ///互换单
    constexpr char XTP_ORDT_Swap = '5';

cpp
    
    
    /////////////////////////////////////////////////////////////////////////
    ///@brief XTP_SIDE_TYPE是买卖方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_SIDE_TYPE;
    
    ///买（新股申购，ETF买，配股，信用交易中担保品买）
    constexpr uint32_t XTP_SIDE_BUY = 1;
    ///卖（逆回购，ETF卖，信用交易中担保品卖）
    constexpr uint32_t XTP_SIDE_SELL = 2;
    ///申购
    constexpr uint32_t XTP_SIDE_PURCHASE = 7;
    ///赎回
    constexpr uint32_t XTP_SIDE_REDEMPTION = 8;
    ///拆分
    constexpr uint32_t XTP_SIDE_SPLIT = 9;
    ///合并
    constexpr uint32_t XTP_SIDE_MERGE = 10;
    ///改版之后的side的备兑，暂不支持
    constexpr uint32_t XTP_SIDE_COVER = 11;
    ///改版之后的side锁定（对应开平标识为开）/解锁（对应开平标识为平）
    constexpr uint32_t XTP_SIDE_FREEZE = 12;
    /// 融资买入
    constexpr uint32_t XTP_SIDE_MARGIN_TRADE = 21;
    /// 融券卖出
    constexpr uint32_t XTP_SIDE_SHORT_SELL = 22;
    /// 卖券还款
    constexpr uint32_t XTP_SIDE_REPAY_MARGIN = 23;
    /// 买券还券
    constexpr uint32_t XTP_SIDE_REPAY_STOCK = 24;
    /// 现金还款（不放在普通订单协议，另加请求和查询协议）
    //		constexpr uint32_t XTP_SIDE_CASH_REPAY_MARGIN = 25;
    /// 现券还券
    constexpr uint32_t XTP_SIDE_STOCK_REPAY_STOCK = 26;
    /// 余券划转
    constexpr uint32_t XTP_SIDE_SURSTK_TRANS = 27;
    /// 担保品转入
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSIN = 28;
    /// 担保品转出
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSOUT = 29;
    
    ///组合策略的组合
    constexpr uint32_t XTP_SIDE_OPT_COMBINE = 31; 
    ///组合策略的拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT = 32; 
    ///组合策略的管理员强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE = 33; 
    ///组合策略的交易所强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE_EXCH = 34;
    
    ///未知或者无效买卖方向
    constexpr uint32_t XTP_SIDE_UNKNOWN = 50;

cpp
    
    
    ///@brief XTP_POSITION_EFFECT_TYPE是开平标识类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_POSITION_EFFECT_TYPE;
    
    /// 初始值或未知值开平标识，除期权外，均使用此值
    constexpr uint32_t XTP_POSITION_EFFECT_INIT = 0;
    /// 开
    constexpr uint32_t XTP_POSITION_EFFECT_OPEN = 1;
    /// 平
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSE = 2;
    /// 强平
    constexpr uint32_t XTP_POSITION_EFFECT_FORCECLOSE = 3;
    /// 平今
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSETODAY = 4;
    /// 平昨
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSEYESTERDAY = 5;
    /// 强减
    constexpr uint32_t XTP_POSITION_EFFECT_FORCEOFF = 6;
    /// 本地强平
    constexpr uint32_t XTP_POSITION_EFFECT_LOCALFORCECLOSE = 7;
    /// 信用业务追保强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_COVER = 8;
    /// 信用业务清偿强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_CLEAR = 9;
    /// 信用业务合约到期强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_DEBT = 10;
    /// 信用业务无条件强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_UNCOND = 11;
    /// 未知的开平标识类型
    constexpr uint32_t XTP_POSITION_EFFECT_UNKNOWN = 12;

cpp
    
    
    ///@brief XTP_ORDER_SUBMIT_STATUS_TYPE是报单提交状态类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_ORDER_SUBMIT_STATUS_TYPE;
    
    ///订单已经提交
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_INSERT_SUBMITTED = 1;
    ///订单已经被接受
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_INSERT_ACCEPTED = 2;
    ///订单已经被拒绝
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_INSERT_REJECTED = 3;
    ///撤单已经提交
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_CANCEL_SUBMITTED = 4;
    ///撤单已经被拒绝
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_CANCEL_REJECTED = 5;
    ///撤单已经被接受
    constexpr uint32_t XTP_ORDER_SUBMIT_STATUS_CANCEL_ACCEPTED = 6;

cpp
    
    
    ///@brief XTP_PRICE_TYPE是价格类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_PRICE_TYPE;
    
    ///限价单-沪 / 深 / 沪期权 / 深期权 （除普通股票业务外，其余未特指的业务均使用此种类型）
    constexpr uint32_t XTP_PRICE_LIMIT = 1;        
    ///即时成交剩余转撤销，市价单-深 / 沪期权 / 深期权
    constexpr uint32_t XTP_PRICE_BEST_OR_CANCEL = 2;        
    ///最优五档即时成交剩余转限价，市价单-沪
    constexpr uint32_t XTP_PRICE_BEST5_OR_LIMIT = 3;        
    ///最优5档即时成交剩余转撤销，市价单-沪深 / 深期权
    constexpr uint32_t XTP_PRICE_BEST5_OR_CANCEL = 4;        
    ///全部成交或撤销,市价单-深 / 沪期权 / 深期权
    constexpr uint32_t XTP_PRICE_ALL_OR_CANCEL = 5;        
    ///本方最优，市价单-沪深 / 深期权
    constexpr uint32_t XTP_PRICE_FORWARD_BEST = 6; 
    ///对手方最优，市价单-沪深 / 深期权    
    constexpr uint32_t XTP_PRICE_REVERSE_BEST_LIMIT = 7;        
    ///期权限价申报FOK
    constexpr uint32_t XTP_PRICE_LIMIT_OR_CANCEL = 8;        
    ///未知或者无效价格类型
    constexpr uint32_t XTP_PRICE_TYPE_UNKNOWN = 9;

cpp
    
    
    ///@brief XTP_BUSINESS_TYPE证券业务类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_BUSINESS_TYPE;
    
    ///普通股票业务（股票买卖，ETF买卖，沪市交易型货币基金等）
    constexpr uint32_t XTP_BUSINESS_TYPE_CASH = 0;            
    ///新股申购业务（对应的price type需选择限价类型）
    constexpr uint32_t XTP_BUSINESS_TYPE_IPOS = 1;
    ///回购业务（国债逆回购业务对应的price type填为限价，side填为卖）
    constexpr uint32_t XTP_BUSINESS_TYPE_REPO = 2;
    ///ETF申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_ETF = 3;
    ///融资融券业务
    constexpr uint32_t XTP_BUSINESS_TYPE_MARGIN = 4;              
    ///转托管（未支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_DESIGNATION = 5;
    ///配股业务（对应的price type需选择限价类型,side填为买）
    constexpr uint32_t XTP_BUSINESS_TYPE_ALLOTMENT = 6;
    ///分级基金申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION = 7;      
    ///分级基金拆分合并业务（业务已下线，不再支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE = 8;
    ///货币基金申赎业务（暂未支持，沪市交易型货币基金的买卖请使用普通股票业务）
    constexpr uint32_t XTP_BUSINESS_TYPE_MONEY_FUND = 9;
    ///期权业务       
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION = 10;
    ///行权
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE = 11;             
    ///锁定解锁，暂不支持
    constexpr uint32_t XTP_BUSINESS_TYPE_FREEZE = 12;             
    ///期权组合策略 组合和拆分业务
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION_COMBINE = 13;
    ///期权行权合并业务
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE_COMBINE = 14;    
    /// 债转股业务
    constexpr uint32_t XTP_BUSINESS_TYPE_BOND_SWAP_STOCK = 15;  
    ///未知类型   
    constexpr uint32_t XTP_BUSINESS_TYPE_UNKNOWN = 16;

cpp
    
    
    /// 本地报单编号的字符串长度
    constexpr uint32_t XTP_LOCAL_ORDER_LEN = 11;
    /// 交易所单号的字符串长度
    constexpr uint32_t XTP_ORDER_EXCH_LEN = 17;
    /// 用户股东账户的字符串长度
    constexpr uint32_t XTP_ACCOUNT_ID_LEN = 17;
    /// 交易所交易员代码字符串长度
    constexpr uint32_t XTP_BRANCH_PBU_LEN = 7;

◇ 3.返回

无

◇ 4.触发函数

cpp
    
    
    // 报单录入
    virtual uint64_t InsertOrder(XTPOrderInsertInfo *order, uint64_t session_id) = 0;
    //已经提前设置order_xtp_id的报单录入请求
    virtual uint64_t InsertOrderExtra(XTPOrderInsertInfo *order, uint64_t session_id) = 0;
    // 撤单请求
    virtual uint64_t CancelOrder(const uint64_t order_xtp_id, uint64_t session_id) = 0;

  


#### 5.3.11. OnTradeEvent ​

成交通知。

订单有成交发生的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的成交回报。相关订单为部成状态，需要用户通过成交回报的成交数量来确定，OnOrderEvent()不会推送部成状态。

◇ 1.函数原型

cpp
    
    
    virtual void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id) { (void)trade_info; (void)session_id; };

◇ 2.参数

trade_info：成交回报的具体信息，用户可以通过trade_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。对于上交所，exec_id可以唯一标识一笔成交。当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交了。对于深交所，exec_id是唯一的，暂时无此判断机制。report_index+market字段可以组成唯一标识表示成交回报。

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///报单成交结构体
    struct XTPTradeReport
    {
    	///XTP系统订单ID，此成交回报相关的订单ID，在XTP系统中唯一
    	uint64_t                 order_xtp_id;
    	///合约代码
    	char                     ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE          market;
    	///报单引用
    	uint32_t                 order_client_id; 
    	///成交时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                 trade_time;
    	///交易所交易员代码 
    	char                     branch_pbu[XTP_BRANCH_PBU_LEN];
    	///成交类型  --成交回报中的执行类型
    	TXTPTradeTypeType        trade_type;
    	///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    	char                     order_local_id[XTP_LOCAL_ORDER_LEN];
    	///买卖方向
    	XTP_SIDE_TYPE            side;
    	///业务类型
    	XTP_BUSINESS_TYPE        business_type;
    	///价格，此次成交的价格
    	double                   price;
    	///数量，此次成交的数量，不是累计数量
    	int64_t                  quantity;
    	///成交金额，此次成交的总金额 = price*quantity
    	double                   trade_amount;
    	///报单编号 --交易所单号
    	char                     order_exch_id[XTP_ORDER_EXCH_LEN];
    	///开平标志
    	XTP_POSITION_EFFECT_TYPE    position_effect;
    	///算法策略类型
    	uint16_t                 strategy_type;
    	///平台分区号
    	int32_t                  set_id;
    	///成交序号 --回报记录号，对于单个账户来说，深交所每个平台（不同交易品种）唯一，上交所唯一，对于多账户来说，不唯一
    	uint64_t                 report_index;
    	///算法母单编号ID，仅为算法单时有效
    	uint64_t                 strategy_id;
    	///成交编号，深交所唯一，上交所每笔交易唯一，当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交
    	char                     exec_id[XTP_EXEC_ID_LEN];
    	/// 证券账户（股卡） 
    	char                     account_id[XTP_ACCOUNT_ID_LEN];
    	///预留字段
    	char                     unused[5];
    };

cpp
    
    
    ///@brief XTP_MARKET_TYPE市场类型，交易里使用
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_MKT_UNKNOWN = 7;

cpp
    
    
    ///TXTPTradeTypeType是成交类型类型
    /////////////////////////////////////////////////////////////////////////
    typedef char TXTPTradeTypeType;
    
    ///普通成交
    constexpr char XTP_TRDT_COMMON = '0';
    ///现金替代
    constexpr char XTP_TRDT_CASH = '1';
    ///一级市场成交
    constexpr char XTP_TRDT_PRIMARY = '2';
    ///跨市场资金成交
    constexpr char XTP_TRDT_CROSS_MKT_CASH = '3';
    ///港市资金成交
    constexpr char XTP_TRDT_HK_MKT_CASH = '4';
    ///非沪深资金成交
    constexpr char XTP_TRDT_NON_SHSZ_MKT_CASH = '5';

cpp
    
    
    ///@brief XTP_SIDE_TYPE是买卖方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_SIDE_TYPE;
    
    ///买（新股申购，ETF买，配股，信用交易中担保品买）
    constexpr uint32_t XTP_SIDE_BUY = 1;
    ///卖（逆回购，ETF卖，信用交易中担保品卖）
    constexpr uint32_t XTP_SIDE_SELL = 2;
    ///申购
    constexpr uint32_t XTP_SIDE_PURCHASE = 7;
    ///赎回
    constexpr uint32_t XTP_SIDE_REDEMPTION = 8;
    ///拆分
    constexpr uint32_t XTP_SIDE_SPLIT = 9;
    ///合并
    constexpr uint32_t XTP_SIDE_MERGE = 10;
    ///改版之后的side的备兑，暂不支持
    constexpr uint32_t XTP_SIDE_COVER = 11;
    ///改版之后的side锁定（对应开平标识为开）/解锁（对应开平标识为平）
    constexpr uint32_t XTP_SIDE_FREEZE = 12;
    /// 融资买入
    constexpr uint32_t XTP_SIDE_MARGIN_TRADE = 21;
    /// 融券卖出
    constexpr uint32_t XTP_SIDE_SHORT_SELL = 22;
    /// 卖券还款
    constexpr uint32_t XTP_SIDE_REPAY_MARGIN = 23;
    /// 买券还券
    constexpr uint32_t XTP_SIDE_REPAY_STOCK = 24;
    /// 现金还款（不放在普通订单协议，另加请求和查询协议）
    //		constexpr uint32_t XTP_SIDE_CASH_REPAY_MARGIN = 25;
    /// 现券还券
    constexpr uint32_t XTP_SIDE_STOCK_REPAY_STOCK = 26;
    /// 余券划转
    constexpr uint32_t XTP_SIDE_SURSTK_TRANS = 27;
    /// 担保品转入
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSIN = 28;
    /// 担保品转出
    constexpr uint32_t XTP_SIDE_GRTSTK_TRANSOUT = 29;
    
    ///组合策略的组合
    constexpr uint32_t XTP_SIDE_OPT_COMBINE = 31; 
    ///组合策略的拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT = 32; 
    ///组合策略的管理员强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE = 33; 
    ///组合策略的交易所强制拆分
    constexpr uint32_t XTP_SIDE_OPT_SPLIT_FORCE_EXCH = 34;
    
    ///未知或者无效买卖方向
    constexpr uint32_t XTP_SIDE_UNKNOWN = 50;

cpp
    
    
    ///@brief XTP_BUSINESS_TYPE证券业务类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_BUSINESS_TYPE;
    
    ///普通股票业务（股票买卖，ETF买卖，沪市交易型货币基金等）
    constexpr uint32_t XTP_BUSINESS_TYPE_CASH = 0;            
    ///新股申购业务（对应的price type需选择限价类型）
    constexpr uint32_t XTP_BUSINESS_TYPE_IPOS = 1;
    ///回购业务（国债逆回购业务对应的price type填为限价，side填为卖）
    constexpr uint32_t XTP_BUSINESS_TYPE_REPO = 2;
    ///ETF申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_ETF = 3;
    ///融资融券业务
    constexpr uint32_t XTP_BUSINESS_TYPE_MARGIN = 4;              
    ///转托管（未支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_DESIGNATION = 5;
    ///配股业务（对应的price type需选择限价类型,side填为买）
    constexpr uint32_t XTP_BUSINESS_TYPE_ALLOTMENT = 6;
    ///分级基金申赎业务
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION = 7;      
    ///分级基金拆分合并业务（业务已下线，不再支持）
    constexpr uint32_t XTP_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE = 8;
    ///货币基金申赎业务（暂未支持，沪市交易型货币基金的买卖请使用普通股票业务）
    constexpr uint32_t XTP_BUSINESS_TYPE_MONEY_FUND = 9;
    ///期权业务       
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION = 10;
    ///行权
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE = 11;             
    ///锁定解锁，暂不支持
    constexpr uint32_t XTP_BUSINESS_TYPE_FREEZE = 12;             
    ///期权组合策略 组合和拆分业务
    constexpr uint32_t XTP_BUSINESS_TYPE_OPTION_COMBINE = 13;
    ///期权行权合并业务
    constexpr uint32_t XTP_BUSINESS_TYPE_EXECUTE_COMBINE = 14;    
    /// 债转股业务
    constexpr uint32_t XTP_BUSINESS_TYPE_BOND_SWAP_STOCK = 15;  
    ///未知类型   
    constexpr uint32_t XTP_BUSINESS_TYPE_UNKNOWN = 16;

cpp
    
    
    ///@brief XTP_POSITION_EFFECT_TYPE是开平标识类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint8_t XTP_POSITION_EFFECT_TYPE;
    
    /// 初始值或未知值开平标识，除期权外，均使用此值
    constexpr uint32_t XTP_POSITION_EFFECT_INIT = 0;
    /// 开
    constexpr uint32_t XTP_POSITION_EFFECT_OPEN = 1;
    /// 平
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSE = 2;
    /// 强平
    constexpr uint32_t XTP_POSITION_EFFECT_FORCECLOSE = 3;
    /// 平今
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSETODAY = 4;
    /// 平昨
    constexpr uint32_t XTP_POSITION_EFFECT_CLOSEYESTERDAY = 5;
    /// 强减
    constexpr uint32_t XTP_POSITION_EFFECT_FORCEOFF = 6;
    /// 本地强平
    constexpr uint32_t XTP_POSITION_EFFECT_LOCALFORCECLOSE = 7;
    /// 信用业务追保强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_COVER = 8;
    /// 信用业务清偿强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_CLEAR = 9;
    /// 信用业务合约到期强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_DEBT = 10;
    /// 信用业务无条件强平
    constexpr uint32_t XTP_POSITION_EFFECT_CREDIT_FORCE_UNCOND = 11;
    /// 未知的开平标识类型
    constexpr uint32_t XTP_POSITION_EFFECT_UNKNOWN = 12;

cpp
    
    
    /// 存放证券代码的字符串长度
    constexpr uint32_t XTP_TICKER_LEN = 16;
    /// 交易所交易员代码字符串长度
    constexpr uint32_t XTP_BRANCH_PBU_LEN = 7;
    /// 交易所单号的字符串长度
    constexpr uint32_t XTP_ORDER_EXCH_LEN = 17;
    /// 成交执行编号的字符串长度
    constexpr uint32_t XTP_EXEC_ID_LEN = 18;
    /// 用户股东账户的字符串长度
    constexpr uint32_t XTP_ACCOUNT_ID_LEN = 17;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 报单录入
    virtual uint64_t InsertOrder(XTPOrderInsertInfo *order, uint64_t session_id) = 0;
    //已经提前设置order_xtp_id的报单录入请求
    virtual uint64_t InsertOrderExtra(XTPOrderInsertInfo *order, uint64_t session_id) = 0;

  


#### 5.3.12. OnCancelOrderError ​

撤单出错响应。此响应只会在撤单发生错误时被回调。

◇ 1.函数原型

cpp
    
    
    virtual void OnCancelOrderError(XTPOrderCancelErrorInfo *cancel_info, XTPRI *error_info, uint64_t session_id) { (void)cancel_info; (void)error_info; (void)session_id; };

◇ 2.参数

cancel_info: 撤单具体信息，包括撤单的order_cancel_xtp_id和待撤单的order_xtp_id

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///撤单失败回报响应结构体
    struct XTPOrderCancelErrorInfo
    { 
    	///撤单订单号
    	uint64_t                order_xtp_id;
    	///证券代码
    	char                    ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE         market;
    	///用户自定义字段
    	uint32_t                order_client_id;
    	///原单号
    	uint64_t                orig_order_xtp_id;
    	///回报时间
    	uint64_t                transact_time;
    	///执行报告编号
    	uint64_t                report_index; 
    	///平台分区号
    	int32_t                 set_id;
    	///拒单原因代码
    	uint32_t                error_code;
    	///外部系统拒单原因代码
    	uint32_t                extra_error_code; 
    	///原始会员内部订单编号
    	char                    orig_order_local_id[XTP_LOCAL_ORDER_LEN];
    	///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    	char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    	/// 预留
    	char                    unused[6];
    
    };

cpp
    
    
    ///@brief XTP_MARKET_TYPE市场类型，交易里使用
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_MKT_UNKNOWN = 7;

cpp
    
    
    /// 存放证券代码的字符串长度
    constexpr uint32_t XTP_TICKER_LEN = 16;
    /// 本地报单编号的字符串长度
    constexpr uint32_t XTP_LOCAL_ORDER_LEN = 11;
    /// 本地报单编号的字符串长度
    constexpr uint32_t XTP_LOCAL_ORDER_LEN = 11;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 撤单请求
    virtual uint64_t CancelOrder(const uint64_t order_xtp_id, uint64_t session_id) = 0;

  


#### 5.3.13. OnQueryOrder ​

请求查询报单响应。

由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryOrder(XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

order_info：查询到的一个报单信息

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///报单查询响应结构体
    typedef struct XTPOrderInfo XTPQueryOrderRsp;
    
    ///报单响应结构体
    struct XTPOrderInfo
    {
    	///订单号
    	uint64_t                order_xtp_id;
    	///证券代码
    	char                    ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE         market;
    	///用户自定义字段
    	uint32_t                order_client_id;
    	///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    	char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    	///订单执行状态，与交易所回报ExecType字段一致，‘0’-新订单，‘4’-已撤销，‘8’-已拒绝，‘F’-已成交；如果是非交易所的回报，此字段为0
    	char                    exec_type;
    	///订单状态
    	XTP_ORDER_STATUS_TYPE   order_status;
    	///交易所订单编号
    	char                    order_exch_id[XTP_ORDER_EXCH_LEN];
    	///报单类型
    	TXTPOrderTypeType       order_type;
    	///买卖方向
    	XTP_SIDE_TYPE           side;
    	///开平标志
    	XTP_POSITION_EFFECT_TYPE    position_effect;
    	///报单提交状态，可以用来区分是否是撤单
    	XTP_ORDER_SUBMIT_STATUS_TYPE   order_submit_status;
    	///订单数量
    	int64_t                 quantity;
    	///订单价格
    	double                  price;
    	///价格类型
    	XTP_PRICE_TYPE          price_type;
    	///业务类型
    	XTP_BUSINESS_TYPE       business_type;
    	///撤单在XTP系统中的id，在XTP系统中唯一（仅撤单成功时有效，此字段为0则表示没有撤单）
    	uint64_t                order_cancel_xtp_id;
    	///成交金额，为此订单的成交总金额
    	double                  trade_amount;
    	///今成交数量，为此订单累计成交数量
    	int64_t                 qty_traded;
    	///剩余数量
    	int64_t                 qty_left;
    	///预扣金额，为此订单的预扣金额（包含预扣手续费，此金额不会改变，仅供参考）
    	double                  order_withhold_amount;
    	///预扣手续费，为此订单的预扣手续费（此金额不会改变，仅供参考）
    	double                  order_withhold_fee;
    	///执行编号
    	char                    exec_id[XTP_EXEC_ID_LEN];
    	///算法策略类型，仅为算法单时有效
    	uint16_t                strategy_type;
    	///平台分区号
    	int32_t                 set_id;
    	///执行报告编号
    	uint64_t                report_index;
    	///回报时间
    	uint64_t                transact_time;
    	///委托时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                insert_time;
    	///最后修改时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                update_time;
    	///撤销时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                cancel_time;
    	///算法母单编号ID，仅为算法单时有效
    	uint64_t                strategy_id;
    	///XTP拒单原因代码
    	uint32_t                error_code;
    	///外部系统拒单原因代码
    	uint32_t                extra_error_code;
    	/// 证券账户（股卡）
    	char                    account_id[XTP_ACCOUNT_ID_LEN];
    	///交易所PBU代码 
    	char                    branch_pbu[XTP_BRANCH_PBU_LEN];
    	/// 预留
    	char                    unused[8];
    };

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 根据报单ID请求查询报单
    virtual int QueryOrderByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
    // 请求查询报单
    virtual int QueryOrders(const XTPQueryOrderReq *query_param, uint64_t session_id, int request_id) = 0;
    // 请求查询未完结报单
    virtual int QueryUnfinishedOrders(uint64_t session_id, int request_id) = 0;

  


#### 5.3.14. OnQueryOrderByPage ​

分页请求查询报单响应。

当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果order_sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryOrderByPage(XTPQueryOrderRsp *order_info, int64_t req_count, int64_t order_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)order_info; (void)req_count; (void)order_sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

order_info：查询到的一个报单

req_count：分页请求的最大数量

order_sequence：分页请求的当前回报数量

query_reference：当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///报单查询响应结构体
    typedef struct XTPOrderInfo XTPQueryOrderRsp;
    
    ///报单响应结构体
    struct XTPOrderInfo
    {
    	///订单号
    	uint64_t                order_xtp_id;
    	///证券代码
    	char                    ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE         market;
    	///用户自定义字段
    	uint32_t                order_client_id;
    	///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    	char                    order_local_id[XTP_LOCAL_ORDER_LEN];
    	///订单执行状态，与交易所回报ExecType字段一致，‘0’-新订单，‘4’-已撤销，‘8’-已拒绝，‘F’-已成交；如果是非交易所的回报，此字段为0
    	char                    exec_type;
    	///订单状态
    	XTP_ORDER_STATUS_TYPE   order_status;
    	///交易所订单编号
    	char                    order_exch_id[XTP_ORDER_EXCH_LEN];
    	///报单类型
    	TXTPOrderTypeType       order_type;
    	///买卖方向
    	XTP_SIDE_TYPE           side;
    	///开平标志
    	XTP_POSITION_EFFECT_TYPE    position_effect;
    	///报单提交状态，可以用来区分是否是撤单
    	XTP_ORDER_SUBMIT_STATUS_TYPE   order_submit_status;
    	///订单数量
    	int64_t                 quantity;
    	///订单价格
    	double                  price;
    	///价格类型
    	XTP_PRICE_TYPE          price_type;
    	///业务类型
    	XTP_BUSINESS_TYPE       business_type;
    	///撤单在XTP系统中的id，在XTP系统中唯一（仅撤单成功时有效，此字段为0则表示没有撤单）
    	uint64_t                order_cancel_xtp_id;
    	///成交金额，为此订单的成交总金额
    	double                  trade_amount;
    	///今成交数量，为此订单累计成交数量
    	int64_t                 qty_traded;
    	///剩余数量
    	int64_t                 qty_left;
    	///预扣金额，为此订单的预扣金额（包含预扣手续费，此金额不会改变，仅供参考）
    	double                  order_withhold_amount;
    	///预扣手续费，为此订单的预扣手续费（此金额不会改变，仅供参考）
    	double                  order_withhold_fee;
    	///执行编号
    	char                    exec_id[XTP_EXEC_ID_LEN];
    	///算法策略类型，仅为算法单时有效
    	uint16_t                strategy_type;
    	///平台分区号
    	int32_t                 set_id;
    	///执行报告编号
    	uint64_t                report_index;
    	///回报时间
    	uint64_t                transact_time;
    	///委托时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                insert_time;
    	///最后修改时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                update_time;
    	///撤销时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                cancel_time;
    	///算法母单编号ID，仅为算法单时有效
    	uint64_t                strategy_id;
    	///XTP拒单原因代码
    	uint32_t                error_code;
    	///外部系统拒单原因代码
    	uint32_t                extra_error_code;
    	/// 证券账户（股卡）
    	char                    account_id[XTP_ACCOUNT_ID_LEN];
    	///交易所PBU代码 
    	char                    branch_pbu[XTP_BRANCH_PBU_LEN];
    	/// 预留
    	char                    unused[8];
    };

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 分页请求查询报单
    virtual int QueryOrdersByPage(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

  


#### 5.3.15. OnQueryTrade ​

请求查询成交响应。

由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。此对应的请求函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryTrade(XTPQueryTradeRsp *trade_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)trade_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

trade_info：查询到的一个成交回报

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///成交回报查询响应结构体
    typedef struct XTPTradeReport  XTPQueryTradeRsp;
    
    ///报单成交结构体
    struct XTPTradeReport
    {
    	///XTP系统订单ID，此成交回报相关的订单ID，在XTP系统中唯一
    	uint64_t                 order_xtp_id;
    	///合约代码
    	char                     ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE          market;
    	///报单引用
    	uint32_t                 order_client_id; 
    	///成交时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                 trade_time;
    	///交易所交易员代码 
    	char                     branch_pbu[XTP_BRANCH_PBU_LEN];
    	///成交类型  --成交回报中的执行类型
    	TXTPTradeTypeType        trade_type;
    	///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    	char                     order_local_id[XTP_LOCAL_ORDER_LEN];
    	///买卖方向
    	XTP_SIDE_TYPE            side;
    	///业务类型
    	XTP_BUSINESS_TYPE        business_type;
    	///价格，此次成交的价格
    	double                   price;
    	///数量，此次成交的数量，不是累计数量
    	int64_t                  quantity;
    	///成交金额，此次成交的总金额 = price*quantity
    	double                   trade_amount;
    	///报单编号 --交易所单号
    	char                     order_exch_id[XTP_ORDER_EXCH_LEN];
    	///开平标志
    	XTP_POSITION_EFFECT_TYPE    position_effect;
    	///算法策略类型
    	uint16_t                 strategy_type;
    	///平台分区号
    	int32_t                  set_id;
    	///成交序号 --回报记录号，对于单个账户来说，深交所每个平台（不同交易品种）唯一，上交所唯一，对于多账户来说，不唯一
    	uint64_t                 report_index;
    	///算法母单编号ID，仅为算法单时有效
    	uint64_t                 strategy_id;
    	///成交编号，深交所唯一，上交所每笔交易唯一，当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交
    	char                     exec_id[XTP_EXEC_ID_LEN];
    	/// 证券账户（股卡） 
    	char                     account_id[XTP_ACCOUNT_ID_LEN];
    	///预留字段
    	char                     unused[5];
    };

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 根据委托编号请求查询相关成交
    virtual int QueryTradesByXTPID(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;
    // 请求查询已成交
    virtual int QueryTrades(XTPQueryTraderReq *query_param, uint64_t session_id, int request_id) = 0;

  


#### 5.3.16. OnQueryTradeByPage ​

分页请求查询成交响应。

当trade_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果trade_sequence等于req_count，那么表示还有回报，可以进行下一次分页查询，如果不等，表示所有回报已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryTradeByPage(XTPQueryTradeRsp *trade_info, int64_t req_count, int64_t trade_sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)trade_info; (void)req_count; (void)trade_sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

trade_info：查询到的一个成交信息

req_count：分页请求的最大数量

order_sequence：分页请求的当前回报数量

query_reference：当前报单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///成交回报查询响应结构体
    typedef struct XTPTradeReport  XTPQueryTradeRsp;
    
    ///报单成交结构体
    struct XTPTradeReport
    {
    	///XTP系统订单ID，此成交回报相关的订单ID，在XTP系统中唯一
    	uint64_t                 order_xtp_id;
    	///合约代码
    	char                     ticker[XTP_TICKER_LEN];
    	///交易市场
    	XTP_MARKET_TYPE          market;
    	///报单引用
    	uint32_t                 order_client_id; 
    	///成交时间，格式为YYYYMMDDHHMMSSsss
    	uint64_t                 trade_time;
    	///交易所交易员代码 
    	char                     branch_pbu[XTP_BRANCH_PBU_LEN];
    	///成交类型  --成交回报中的执行类型
    	TXTPTradeTypeType        trade_type;
    	///本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
    	char                     order_local_id[XTP_LOCAL_ORDER_LEN];
    	///买卖方向
    	XTP_SIDE_TYPE            side;
    	///业务类型
    	XTP_BUSINESS_TYPE        business_type;
    	///价格，此次成交的价格
    	double                   price;
    	///数量，此次成交的数量，不是累计数量
    	int64_t                  quantity;
    	///成交金额，此次成交的总金额 = price*quantity
    	double                   trade_amount;
    	///报单编号 --交易所单号
    	char                     order_exch_id[XTP_ORDER_EXCH_LEN];
    	///开平标志
    	XTP_POSITION_EFFECT_TYPE    position_effect;
    	///算法策略类型
    	uint16_t                 strategy_type;
    	///平台分区号
    	int32_t                  set_id;
    	///成交序号 --回报记录号，对于单个账户来说，深交所每个平台（不同交易品种）唯一，上交所唯一，对于多账户来说，不唯一
    	uint64_t                 report_index;
    	///算法母单编号ID，仅为算法单时有效
    	uint64_t                 strategy_id;
    	///成交编号，深交所唯一，上交所每笔交易唯一，当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交
    	char                     exec_id[XTP_EXEC_ID_LEN];
    	/// 证券账户（股卡） 
    	char                     account_id[XTP_ACCOUNT_ID_LEN];
    	///预留字段
    	char                     unused[5];
    };

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 分页请求查询成交回报
    virtual int QueryTradesByPage(const XTPQueryTraderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

  


#### 5.3.17. OnQueryPosition ​

请求查询投资者持仓响应。

由于用户可能持有多个股票，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryPosition(XTPQueryStkPositionRsp *position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)position; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

Position：查询到的一只股票的持仓情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///查询股票持仓情况
    //////////////////////////////////////////////////////////////////////////
    struct XTPQueryStkPositionRsp
    {
    	///证券代码
    	char                ticker[XTP_TICKER_LEN];
    	///证券名称
    	char                ticker_name[XTP_TICKER_NAME_LEN];
    	///证券账户（股卡）
    	char                account_id[XTP_ACCOUNT_ID_LEN];
    	///(保留字段)
    	char                unused[3];
    	///交易市场
    	XTP_MARKET_TYPE     market;
    	///总持仓
    	int64_t             total_qty;
    	///可卖持仓
    	int64_t             sellable_qty;
    	///持仓成本
    	double              avg_price;
    	///浮动盈亏（保留字段）
    	double              unrealized_pnl;
    	///昨日持仓
    	int64_t             yesterday_position;
    	///今日申购赎回数量（申购和赎回数量不可能同时存在，因此可以共用一个字段）
    	int64_t             purchase_redeemable_qty;
    
    	//以下为期权用户关心字段
    	/// 持仓方向
    	XTP_POSITION_DIRECTION_TYPE      position_direction;
    	///持仓类型(此字段所有账户都可能用到，可以用来区分股份是否为配售)
    	XTP_POSITION_SECURITY_TYPE       position_security_type;
    	/// 可行权合约
    	int64_t             executable_option;
    	/// 可锁定标的
    	int64_t             lockable_position;
    	/// 可行权标的
    	int64_t             executable_underlying;
    	/// 已锁定标的
    	int64_t             locked_position;
    	/// 可用已锁定标的
    	int64_t             usable_locked_position;
    
    	//以下为现货用户关心字段
    	///盈亏成本价
    	double             profit_price;
    	///买入成本
    	double             buy_cost;
    	///盈亏成本
    	double             profit_cost;
    	
    	///持仓市值（此字段目前只有期权账户有值，其他类型账户为0）
    	double             market_value;
    	///义务仓占用保证金（此字段目前只有期权账户有值，其他类型账户为0）
    	double             margin;
    	
    	///昨日买入成本
    	double             last_buy_cost;
    	///昨日盈亏成本
    	double             last_profit_cost;
    
    };

cpp
    
    
    ///@brief XTP_POSITION_DIRECTION_TYPE是一个持仓方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_POSITION_DIRECTION_TYPE;
    
    ///净
    constexpr uint32_t XTP_POSITION_DIRECTION_NET = 0;       
    ///多（期权则为权利方） 
    constexpr uint32_t XTP_POSITION_DIRECTION_LONG = 1;
    ///空（期权则为义务方）
    constexpr uint32_t XTP_POSITION_DIRECTION_SHORT = 2;  
    ///备兑（期权则为备兑义务方）
    constexpr uint32_t XTP_POSITION_DIRECTION_COVERED = 3;

cpp
    
    
    ///@brief XTP_POSITION_SECURITY_TYPE是一个持仓证券类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t  XTP_POSITION_SECURITY_TYPE;
    
    ///普通持仓
    constexpr uint32_t XTP_POSITION_SECURITY_NORMAL = 0;            
    ///配售类型的持仓，包含配股、配债等
    constexpr uint32_t XTP_POSITION_SECURITY_PLACEMENT = 1;        
    ///未知类型
    constexpr uint32_t XTP_POSITION_SECURITY_UNKNOWN = 2;

cpp
    
    
    /// 存放证券代码的字符串长度
    constexpr uint32_t XTP_TICKER_LEN = 16;
    /// 存放证券名称的字符串长度
    constexpr uint32_t XTP_TICKER_NAME_LEN = 64;
    /// 用户股东账户的字符串长度
    constexpr uint32_t XTP_ACCOUNT_ID_LEN = 17;

◇ 3.返回

无

◇ 4. 示例代码 以下是MyTraderSpi.h文件

cpp
    
    
    #include "xtpx_trader_api.h"
    #include <iostream>
    #include <list>
    
    using namespace std;
    using namespace XTPX::API;
    
    class MyTraderSpi : public TraderSpi
    {
    public:
    	explicit MyTraderSpi();
    	~MyTraderSpi();
    	
    	void OnQueryPosition(XTPQueryStkPositionRsp * investor_position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id);
    
    private:
        std::list<XTPQueryStkPositionRsp> query_stk_position_buffer_;
        std::list<XTPQueryStkPositionRsp> query_allotment_buffer_;
    }

以下是MyTraderSpi.cpp文件

cpp
    
    
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
    			std::cout << "Position is empty." << std::endl;
    		}
    		else
    		{
    			//真正的出错
    		}
    		return;
        }
    
    	//TODO：用户可以根据自己的需要编写程序逻辑，以下仅以缓存查询结果为例
        if (investor_position) {
    		// 持仓缓存
            query_stk_position_buffer_.push_back(*investor_position);
    		// 配股或配债缓存
            if (XTP_POSITION_SECURITY_PLACEMENT == investor_position->position_security_type)
                query_allotment_buffer_.push_back(*investor_position);
        }
    
        if (is_last) {
    		/// 两份缓存数据发送至UI线程
    		
    		// 缓存发送后清空容器
            query_stk_position_buffer_.clear();
            query_allotment_buffer_.clear();
        }
    }

◇ 5. 触发函数

cpp
    
    
    // 请求查询投资者持仓
    virtual int QueryPosition(const char *ticker, uint64_t session_id, int request_id, XTP_MARKET_TYPE market) = 0;

  


#### 5.3.18. OnQuerySecurityAccount ​

请求查询用户证券账户信息响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQuerySecurityAccount(XTPQueryAccountIdRsp *account_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)account_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

account_info: 查询到的用户证券账户信息

error_info: 查询用户证券账户信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id: 用于用户定位查询响应的ID，由用户自定义

is_last: 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id: 资金账户对应的session_id，登录时得到

cpp
    
    
    ///查询股卡情况--响应结构体
    //////////////////////////////////////////////////////////////////////////
    struct XTPQueryAccountIdRsp
    {
    	///交易市场
    	XTP_MARKET_TYPE     market;
    	///证券账户（股卡）
    	char                account_id[XTP_ACCOUNT_ID_LEN];
    	/// 主股东账户标识
    	bool                is_main_account;
    	/// 预留
    	char                unused[2];
    };

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    //请求查询用户的证券账户信息（股卡信息）
    virtual int QuerySecurityAccount(uint64_t session_id, int request_id) = 0;

#### 5.3.19. OnQueryAsset ​

请求查询资金账户响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryAsset(XTPQueryAssetRsp *asset, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)asset; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

Asset：查询到的资金账户情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///账户资金查询响应结构体
    //////////////////////////////////////////////////////////////////////////
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
    
    	///账户类型
    	XTP_ACCOUNT_TYPE account_type;
    	///货币种类
    	XTP_CURRENCY_TYPE  currency_type;                                    
    };

cpp
    
    
    ///@brief XTP_ACCOUNT_TYPE账户类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_ACCOUNT_TYPE;
    
    ///普通账户
    constexpr uint32_t XTP_ACCOUNT_NORMAL = 0;    
    ///信用账户
    constexpr uint32_t XTP_ACCOUNT_CREDIT = 1;    
    ///衍生品账户
    constexpr uint32_t XTP_ACCOUNT_DERIVE = 2;    
    ///未知账户类型
    constexpr uint32_t XTP_ACCOUNT_UNKNOWN = 3;

cpp
    
    
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 请求查询资产
    virtual int QueryAsset(uint64_t session_id, int request_id) = 0;

  


#### 5.3.20. OnQueryFundTransfer ​

请求查询资金划拨订单响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryFundTransfer(XTPFundTransferLog *fund_transfer_info, XTPRI *fund_transfer_err_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)fund_transfer_info; (void)fund_transfer_err_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

fund_transfer_info：查询到的资金账户情况

fund_transfer_err_info: 返回的资金划拨订单fund_transfer_info划拨失败时的错误信息，当fund_transfer_err_info为空，或者fund_transfer_err_info.error_id为0时，表明划转成功，没有错误

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///资金内转流水记录结构体
    /////////////////////////////////////////////////////////////////////////
    typedef struct XTPFundTransferNotice XTPFundTransferLog;
    ///资金内转流水通知
    /////////////////////////////////////////////////////////////////////////
    struct XTPFundTransferNotice
    {
    	///资金内转编号
    	uint64_t                serial_id;
    	///金额
    	double	                amount;
    	///内转类型
    	XTP_FUND_TRANSFER_TYPE  transfer_type;
    	///操作结果 
    	XTP_FUND_OPER_STATUS    oper_status;
    	///操作时间
    	uint64_t	            transfer_time;
    	///转入或转出的目标服务器对应的节点类型
    	XTP_TRANSFER_SITE_TYPE  site;
    	///货币种类
    	XTP_CURRENCY_TYPE       currency_type;
    
    };

cpp
    
    
    ///@brief XTP_FUND_TRANSFER_TYPE是资金流转方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_FUND_TRANSFER_TYPE;
    
    ///转出 从XTP转出到柜台
    constexpr uint32_t XTP_FUND_TRANSFER_OUT = 0;        
    ///转入 从柜台转入XTP
    constexpr uint32_t XTP_FUND_TRANSFER_IN = 1;
    ///跨节点转出 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨，只能“一账号两中心”跨节点用户使用
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_OUT = 2;
    ///跨节点转入 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨，只能“一账号两中心”跨节点用户使用
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_IN = 3;
    ///跨节点转出 融券卖出资金 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_REPAY_OUT = 4;
    ///跨节点转入 融券卖出资金 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_REPAY_IN = 5;
    ///跨节点转出 授信额度 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_CONTRACT_OUT = 6;
    ///跨节点转入 授信额度 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_CONTRACT_IN = 7; 
    ///未知类型
    constexpr uint32_t XTP_FUND_TRANSFER_UNKNOWN = 8;

cpp
    
    
    ///@brief XTP_FUND_OPER_STATUS柜台资金操作结果
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_FUND_OPER_STATUS;
    
    ///XTP已收到，正在处理中
    constexpr uint32_t XTP_FUND_OPER_PROCESSING = 0;    
    ///成功
    constexpr uint32_t XTP_FUND_OPER_SUCCESS = 1;     
    ///失败
    constexpr uint32_t XTP_FUND_OPER_FAILED = 2;    
    ///划拨服务处理中
    constexpr uint32_t XTP_FUND_OPER_SUBMITTED = 3;   
    ///未知
    constexpr uint32_t XTP_FUND_OPER_UNKNOWN = 4;

cpp
    
    
    ///@brief XTP_TRANSFER_SITE_TYPE是一个划转节点类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TRANSFER_SITE_TYPE;
    
    ///主柜台
    constexpr uint32_t XTP_TRANSFER_SITE_COUNTER = 0;
    ///上海节点
    constexpr uint32_t XTP_TRANSFER_SITE_SH = 2;
    ///深圳节点
    constexpr uint32_t XTP_TRANSFER_SITE_SZ = 4;
    ///北京节点
    constexpr uint32_t XTP_TRANSFER_SITE_NQ = 8;
    ///香港节点
    constexpr uint32_t XTP_TRANSFER_SITE_HK = 16;
    ///未知节点
    constexpr uint32_t XTP_TRANSFER_SITE_UNKNOWN = 256;

cpp
    
    
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 请求查询指定资金划拨订单
    virtual int QueryFundTransferByID(uint64_t serial_id, uint64_t session_id, int request_id) = 0;

  


#### 5.3.21. OnQueryFundTransferByPage ​

分页请求查询资金划拨订单响应。

当order_sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryFundTransferByPage(XTPFundTransferLog *fund_transfer_info, XTPRI *fund_transfer_err_info, XTPRI *error_info, int64_t req_count, int64_t sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)fund_transfer_info; (void)fund_transfer_err_info; (void)error_info; (void)req_count; (void)sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

fund_transfer_info: 查询到的一个资金划拨订单

fund_transfer_err_info: 返回的资金划拨订单order_info划拨失败时的错误信息，当fund_transfer_err_info为空，或者fund_transfer_err_info.error_id为0时，表明划转成功，没有错误

error_info: 分页查询资金资金划拨订单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明查询没有错误

req_count: 分页请求的最大数量

sequence: 分页请求的当前回报数量

query_reference: 当前资金划拨订单信息所对应的查询索引，需要记录下来，在进行下一次分页查询的时候需要用到

request_id: 此消息响应函数对应的请求ID

is_last: 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id: 资金账户对应的session_id，登录时得到

cpp
    
    
    ///资金内转流水记录结构体
    /////////////////////////////////////////////////////////////////////////
    typedef struct XTPFundTransferNotice XTPFundTransferLog;
    ///资金内转流水通知
    /////////////////////////////////////////////////////////////////////////
    struct XTPFundTransferNotice
    {
    	///资金内转编号
    	uint64_t                serial_id;
    	///金额
    	double	                amount;
    	///内转类型
    	XTP_FUND_TRANSFER_TYPE  transfer_type;
    	///操作结果 
    	XTP_FUND_OPER_STATUS    oper_status;
    	///操作时间
    	uint64_t	            transfer_time;
    	///转入或转出的目标服务器对应的节点类型
    	XTP_TRANSFER_SITE_TYPE  site;
    	///货币种类
    	XTP_CURRENCY_TYPE       currency_type;
    
    };

cpp
    
    
    ///@brief XTP_FUND_TRANSFER_TYPE是资金流转方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_FUND_TRANSFER_TYPE;
    
    ///转出 从XTP转出到柜台
    constexpr uint32_t XTP_FUND_TRANSFER_OUT = 0;        
    ///转入 从柜台转入XTP
    constexpr uint32_t XTP_FUND_TRANSFER_IN = 1;
    ///跨节点转出 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨，只能“一账号两中心”跨节点用户使用
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_OUT = 2;
    ///跨节点转入 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨，只能“一账号两中心”跨节点用户使用
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_IN = 3;
    ///跨节点转出 融券卖出资金 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_REPAY_OUT = 4;
    ///跨节点转入 融券卖出资金 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_REPAY_IN = 5;
    ///跨节点转出 授信额度 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_CONTRACT_OUT = 6;
    ///跨节点转入 授信额度 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_CONTRACT_IN = 7; 
    ///未知类型
    constexpr uint32_t XTP_FUND_TRANSFER_UNKNOWN = 8;

cpp
    
    
    ///@brief XTP_FUND_OPER_STATUS柜台资金操作结果
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_FUND_OPER_STATUS;
    
    ///XTP已收到，正在处理中
    constexpr uint32_t XTP_FUND_OPER_PROCESSING = 0;    
    ///成功
    constexpr uint32_t XTP_FUND_OPER_SUCCESS = 1;     
    ///失败
    constexpr uint32_t XTP_FUND_OPER_FAILED = 2;    
    ///划拨服务处理中
    constexpr uint32_t XTP_FUND_OPER_SUBMITTED = 3;   
    ///未知
    constexpr uint32_t XTP_FUND_OPER_UNKNOWN = 4;

cpp
    
    
    ///@brief XTP_TRANSFER_SITE_TYPE是一个划转节点类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TRANSFER_SITE_TYPE;
    
    ///主柜台
    constexpr uint32_t XTP_TRANSFER_SITE_COUNTER = 0;
    ///上海节点
    constexpr uint32_t XTP_TRANSFER_SITE_SH = 2;
    ///深圳节点
    constexpr uint32_t XTP_TRANSFER_SITE_SZ = 4;
    ///北京节点
    constexpr uint32_t XTP_TRANSFER_SITE_NQ = 8;
    ///香港节点
    constexpr uint32_t XTP_TRANSFER_SITE_HK = 16;
    ///未知节点
    constexpr uint32_t XTP_TRANSFER_SITE_UNKNOWN = 256;

cpp
    
    
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    //分页请求查询资金划拨订单
    virtual int QueryFundTransferByPage(const XTPQueryFundTransferByPageReq *query_param, uint64_t session_id, int request_id) = 0;

  


#### 5.3.22. OnFundTransfer ​

资金划拨通知。

当资金划拨订单有状态变化的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的资金划拨通知。

◇ 1.函数原型

cpp
    
    
    virtual void OnFundTransfer(XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info, uint64_t session_id) { (void)fund_transfer_info; (void)error_info; (void)session_id; };

◇ 2.参数

fund_transfer_info：资金划拨通知的具体信息，用户可以通过fund_transfer_info.serial_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。

error_info：资金划拨订单被拒绝或者发生错误时错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误。当资金划拨方向为一号两中心节点之间划拨，且error_info.error_id=11000384时，error_info.error_msg中含有对方结点中可用于划拨的资金（以整数为准），用户需解析后进行stringToInt的转化，可据此填写合适的资金，再次发起划拨请求

request_id：用于用户定位查询响应的ID，由用户自定义

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///资金内转流水通知
    /////////////////////////////////////////////////////////////////////////
    struct XTPFundTransferNotice
    {
    	///资金内转编号
    	uint64_t                serial_id;
    	///金额
    	double	                amount;
    	///内转类型
    	XTP_FUND_TRANSFER_TYPE  transfer_type;
    	///操作结果 
    	XTP_FUND_OPER_STATUS    oper_status;
    	///操作时间
    	uint64_t	            transfer_time;
    	///转入或转出的目标服务器对应的节点类型
    	XTP_TRANSFER_SITE_TYPE  site;
    	///货币种类
    	XTP_CURRENCY_TYPE       currency_type;
    
    };

cpp
    
    
    ///@brief XTP_FUND_TRANSFER_TYPE是资金流转方向类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_FUND_TRANSFER_TYPE;
    
    ///转出 从XTP转出到柜台
    constexpr uint32_t XTP_FUND_TRANSFER_OUT = 0;        
    ///转入 从柜台转入XTP
    constexpr uint32_t XTP_FUND_TRANSFER_IN = 1;
    ///跨节点转出 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨，只能“一账号两中心”跨节点用户使用
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_OUT = 2;
    ///跨节点转入 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨，只能“一账号两中心”跨节点用户使用
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_IN = 3;
    ///跨节点转出 融券卖出资金 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_REPAY_OUT = 4;
    ///跨节点转入 融券卖出资金 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_REPAY_IN = 5;
    ///跨节点转出 授信额度 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_CONTRACT_OUT = 6;
    ///跨节点转入 授信额度 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨
    constexpr uint32_t XTP_FUND_INTER_TRANSFER_CONTRACT_IN = 7; 
    ///未知类型
    constexpr uint32_t XTP_FUND_TRANSFER_UNKNOWN = 8;

cpp
    
    
    ///@brief XTP_FUND_OPER_STATUS柜台资金操作结果
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_FUND_OPER_STATUS;
    
    ///XTP已收到，正在处理中
    constexpr uint32_t XTP_FUND_OPER_PROCESSING = 0;    
    ///成功
    constexpr uint32_t XTP_FUND_OPER_SUCCESS = 1;     
    ///失败
    constexpr uint32_t XTP_FUND_OPER_FAILED = 2;    
    ///划拨服务处理中
    constexpr uint32_t XTP_FUND_OPER_SUBMITTED = 3;   
    ///未知
    constexpr uint32_t XTP_FUND_OPER_UNKNOWN = 4;

cpp
    
    
    ///@brief XTP_TRANSFER_SITE_TYPE是一个划转节点类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TRANSFER_SITE_TYPE;
    
    ///主柜台
    constexpr uint32_t XTP_TRANSFER_SITE_COUNTER = 0;
    ///上海节点
    constexpr uint32_t XTP_TRANSFER_SITE_SH = 2;
    ///深圳节点
    constexpr uint32_t XTP_TRANSFER_SITE_SZ = 4;
    ///北京节点
    constexpr uint32_t XTP_TRANSFER_SITE_NQ = 8;
    ///香港节点
    constexpr uint32_t XTP_TRANSFER_SITE_HK = 16;
    ///未知节点
    constexpr uint32_t XTP_TRANSFER_SITE_UNKNOWN = 256;

cpp
    
    
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 资金划拨请求
    virtual uint64_t FundTransfer(XTPFundTransferReq *fund_transfer, uint64_t session_id) = 0;

  


#### 5.3.23. OnUnknownFundTransfer ​

资金划拨订单未知状态通知。

此响应仅表明XTP资金划拨服务端未收到过该订单，且没有报送到后台。

◇ 1.函数原型

cpp
    
    
    virtual void OnUnknownFundTransfer(uint64_t serial_id, uint64_t session_id) { (void)serial_id; (void)session_id; };

◇ 2.参数

serial_id: 未知状态资金划拨订单的serial id

session_id: 资金账户对应的session_id，登录时得到

◇ 3.返回

无

  


#### 5.3.24. OnQueryOtherServerFund ​

请求查询其他节点可用资金的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryOtherServerFund(XTPFundQueryRsp *fund_info, XTPRI *error_info, int request_id, uint64_t session_id) { (void)fund_info; (void)error_info; (void)request_id; (void)session_id; };

◇ 2.参数

fund_info：查询到的其他节点可用资金情况

error_info：查询到的其他节点可用资金情况发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///用户资金查询响应结构体
    /////////////////////////////////////////////////////////////////////////
    struct XTPFundQueryRsp
    {
    	///金额
    	double        amount;
    	///查询类型
    	XTP_FUND_QUERY_TYPE    query_type;
    	///对应的交易市场
    	XTP_TRANSFER_SITE_TYPE query_site;
    	///货币种类
    	XTP_CURRENCY_TYPE      currency_type;
    	///预留字段
    	char                   unused[4];
    
    };

cpp
    
    
    ///@brief XTP_FUND_QUERY_TYPE是柜台资金查询类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_FUND_QUERY_TYPE;
    
    ///查询金证主柜台可转资金
    constexpr uint32_t XTP_FUND_QUERY_JZ = 0;        
    ///查询一账号两中心设置时，对方节点的资金
    constexpr uint32_t XTP_FUND_QUERY_INTERNAL = 1;
    ///查询一账号两中心设置时，对方节点的融券卖余额资金
    constexpr uint32_t XTP_FUND_QUERY_INTERNAL_REPAY = 2;  
    ///查询一账号两中心设置时，对方节点的授信额度
    constexpr uint32_t XTP_FUND_QUERY_INTERNAL_CONTRACT = 3; 
    ///未知类型
    constexpr uint32_t XTP_FUND_QUERY_UNKNOWN = 4;

cpp
    
    
    ///@brief XTP_TRANSFER_SITE_TYPE是一个划转节点类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TRANSFER_SITE_TYPE;
    
    ///主柜台
    constexpr uint32_t XTP_TRANSFER_SITE_COUNTER = 0;
    ///上海节点
    constexpr uint32_t XTP_TRANSFER_SITE_SH = 2;
    ///深圳节点
    constexpr uint32_t XTP_TRANSFER_SITE_SZ = 4;
    ///北京节点
    constexpr uint32_t XTP_TRANSFER_SITE_NQ = 8;
    ///香港节点
    constexpr uint32_t XTP_TRANSFER_SITE_HK = 16;
    ///未知节点
    constexpr uint32_t XTP_TRANSFER_SITE_UNKNOWN = 256;

cpp
    
    
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 请求查询其他节点可用资金
    virtual int QueryOtherServerFund(XTPFundQueryReq *query_param, uint64_t session_id, int request_id) = 0;

  


#### 5.3.25. OnQueryETF ​

请求查询ETF清单文件的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryETF(XTPQueryETFBaseRsp *etf_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)etf_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

etf_info：查询到的ETF清单文件情况

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///查询股票ETF合约基本情况--响应结构体
    //////////////////////////////////////////////////////////////////////////
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

cpp
    
    
    /// 存放证券代码的字符串长度
    constexpr uint32_t XTP_TICKER_LEN = 16;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 请求查询ETF清单文件
    virtual int QueryETF(XTPQueryETFBaseReq *query_param, uint64_t session_id, int request_id) = 0;

  


#### 5.3.26. OnQueryETFBasket ​

请求查询ETF股票篮的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryETFBasket(XTPQueryETFComponentRsp *etf_component_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)etf_component_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

etf_component_info：查询到的ETF合约的相关成分股信息

error_info：查询资金账户发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///查询股票ETF成分股信息--响应结构体
    //////////////////////////////////////////////////////////////////////////
    struct XTPQueryETFComponentRsp
    {
    	///ETF代码
    	char                ticker[XTP_TICKER_LEN];
    	///成份股代码
    	char                component_ticker[XTP_TICKER_LEN];
    	///成份股名称
    	char                component_name[XTP_TICKER_NAME_LEN];
    	///成份股数量
    	int64_t             quantity;
    	///交易市场
    	XTP_MARKET_TYPE     market;
    	///成份股交易市场
    	XTP_MARKET_TYPE     component_market;
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
    	///成份股替代标识
    	ETF_REPLACE_TYPE    replace_type;
    	/// 预留
    	char                unused[4];
    };
    
    ///@brief ETF_REPLACE_TYPE现金替代标识定义
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t ETF_REPLACE_TYPE;
    
    ///禁止现金替代
    constexpr uint32_t ERT_CASH_FORBIDDEN = 0;            
    ///可以现金替代
    constexpr uint32_t ERT_CASH_OPTIONAL = 1;
    ///必须现金替代
    constexpr uint32_t ERT_CASH_MUST = 2;
    ///深市退补现金替代
    constexpr uint32_t ERT_CASH_RECOMPUTE_INTER_SZ = 3;
    ///深市必须现金替代
    constexpr uint32_t ERT_CASH_MUST_INTER_SZ = 4;         
    ///非沪深市场成分证券退补现金替代（不适用于跨沪深港ETF产品）
    constexpr uint32_t ERT_CASH_RECOMPUTE_INTER_OTHER = 5; 
    ///表示非沪深市场成份证券必须现金替代（不适用于跨沪深港ETF产品）
    constexpr uint32_t ERT_CASH_MUST_INTER_OTHER = 6;
    ///港市退补现金替代（仅适用于跨沪深港ETF产品）
    constexpr uint32_t ERT_CASH_RECOMPUTE_INTER_HK = 7;
    ///港市必须现金替代（仅适用于跨沪深港ETF产品）
    constexpr uint32_t ERT_CASH_MUST_INTER_HK = 8;  
    ///无效值
    constexpr uint32_t   EPT_INVALID = 9;

cpp
    
    
    /// 存放证券代码的字符串长度
    constexpr uint32_t XTP_TICKER_LEN = 16;
    /// 存放证券名称的字符串长度
    constexpr uint32_t XTP_TICKER_NAME_LEN = 64;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 请求查询ETF股票篮
    virtual int QueryETFTickerBasket(XTPQueryETFComponentReq *query_param, uint64_t session_id, int request_id) = 0;

  


#### 5.3.27. OnQueryIPOInfoList ​

请求查询今日新股申购信息列表的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)ipo_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

ipo_info 查询到的今日新股申购的一只股票信息

error_info：查询今日新股申购信息列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///查询当日可申购新股信息
    //////////////////////////////////////////////////////////////////////////
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
    	///<是否尚未盈利(仅适用创业板股票，创新企业股票及存托凭证)
    	bool                is_noprofit;
    	///预留
    	char                unused[31];
    };

cpp
    
    
    ///@brief XTP_TICKER_TYPE证券类型
    //////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_TICKER_TYPE;
    
    ///普通股票
    constexpr uint32_t XTP_TICKER_TYPE_STOCK = 0;            
    ///指数
    constexpr uint32_t XTP_TICKER_TYPE_INDEX = 1;          
    ///基金
    constexpr uint32_t XTP_TICKER_TYPE_FUND = 2;         
    ///债券
    constexpr uint32_t XTP_TICKER_TYPE_BOND = 3;          
    ///期权
    constexpr uint32_t XTP_TICKER_TYPE_OPTION = 4;          
    ///科创板股票（上海）
    constexpr uint32_t XTP_TICKER_TYPE_TECH_STOCK = 5;         
    ///未知类型
    constexpr uint32_t XTP_TICKER_TYPE_UNKNOWN = 6;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 请求查询今日新股申购信息列表
    virtual int QueryIPOInfoList(uint64_t session_id, int request_id) = 0;

  


#### 5.3.28. OnQueryIPOQuotaInfo ​

请求查询用户新股申购额度信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryIPOQuotaInfo(XTPQueryIPOQuotaRsp *quota_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)quota_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

quota_info：查询到的用户某个市场的今日新股申购额度信息

error_info：查询用户新股申购额度信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///查询用户申购额度-包含创业板额度
    //////////////////////////////////////////////////////////////////////////
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

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 请求查询用户新股申购额度信息
    virtual int QueryIPOQuotaInfo(uint64_t session_id, int request_id) = 0;

  


#### 5.3.29. OnQueryBondIPOInfoList ​

请求查询今日可转债申购信息列表的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryBondIPOInfoList(XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)ipo_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

ipo_info：查询到的今日可转债申购的可转债信息

error_info：查询用户今日可转债申购信息列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///查询当日可申购新股信息
    //////////////////////////////////////////////////////////////////////////
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
    	///<是否尚未盈利(仅适用创业板股票，创新企业股票及存托凭证)
    	bool                is_noprofit;
    	///预留
    	char                unused[31];
    };

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 请求查询用户今日可转债申购信息
    virtual int QueryBondIPOInfoList(uint64_t session_id, int request_id) = 0;

  


#### 5.3.30. OnQueryBondSwapStockInfo ​

请求查询用户可转债转股信息的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryBondSwapStockInfo(XTPQueryBondSwapStockRsp *swap_stock_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)swap_stock_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };

◇ 2.参数

swap_stock_info: 查询到某条可转债转股信息

error_info：查询可转债信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

session_id：资金账户对应的session_id，登录时得到

cpp
    
    
    ///查询债转股信息-------响应结构体
    //////////////////////////////////////////////////////////////////////////
    typedef struct XTPQueryBondSwapStockRsp
    {
    	char              ticker[XTP_TICKER_LEN];// 债券证券代码
    	char              underlying_ticker[XTP_TICKER_LEN];// 转股后的股票证券代码
    	XTP_MARKET_TYPE   market;// 交易市场
    	int32_t           unit;// 转换数量单位（张）
    	int64_t           qty_min;// 最小下单量（张）
    	int64_t           qty_max;// 最大下单量（张）
    	double            swap_price;// 转股价格
    	int32_t           swap_flag;// 是否处于转股期；0: 不可转股；1：可转股；
    	char              unused[4];// 预留
    }XTPQueryBondSwapStockRsp;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    // 请求查询用户债转股信息
    virtual int QueryBondSwapStockInfo(XTPQueryBondSwapStockReq *query_param, uint64_t session_id, int request_id) = 0;
