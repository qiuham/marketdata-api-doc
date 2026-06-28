---
api_type: guide
source_type: vitepress
version: XTP Pro
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
provider_name: 中泰证券
product: xtppro
product_id: zhongtai-xtppro
id: zhongtai-xtppro-xtp-pro算法交易xalgo-api使用示例说明
title: XTP Pro算法交易XAlgo-API使用示例说明
source_url: 'https://xtp.zts.com.cn/xtp-pro/API4/%E7%AE%97%E6%B3%95XAlgo-API%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97QuickStart.html'
page_url: 'https://xtp.zts.com.cn/xtp-pro/'
updated_at: 2026-06-08
---

# XTP Pro算法交易XAlgo-API使用示例说明

**XTP Pro算法交易XAlgo-API使用示例说明**

目录

  * **1\. 算法库介绍**
    * 1.1. 头文件
    * 1.2. 库文件
    * 1.3. 接口说明
  * **2\. Quick Start**
    * 2.1. 创建Api实例
    * 2.2. 初始化Api参数
    * 2.3. 创建Spi类
    * 2.4. 创建Spi实例
    * 2.5. 注册Spi
    * 2.6. 登陆算法服务器
    * 2.7. 建立算法通道
    * 2.8. 请求推荐策略
    * 2.9. 报送策略订单
    * 2.10. 母单创建推送消息
    * 2.11. 用户策略指定证券运行情况状态通知
    * 2.12. 报策略单通知响应
    * 2.13. 策略状态通知响应
    * 2.14. 断线重连
  * **3\. 算法交易时需注意的问题**
  * **4\. 简单Demo示例代码**



## **1\. 算法库介绍** ​

该文档旨在帮助开发者快速使用极速交易平台XTP Pro版本的算法API，文中是XAlgo-API接口调用示例。

### 1.1. 头文件 ​

文件名| 详情  
---|---  
`xtp_algox_api.h`| 算法接口头文件，算法接口类。  
`algox_data_type.h`| 定义算法数据基本类型。  
`algox_api_struct.h`| 定义算法相关数据结构。  
  
### 1.2. 库文件 ​

适用系统| 文件名  
---|---  
windows| `xtpalgoxapi.dll xtpalgoxapi.lib`  
linux| `libxtpalgoxapi.so`  
  
### 1.3. 接口说明 ​

  * (1) 算法API提供了两个接口类：算法类AlgoXApi接口和算法回调类AlgoXSpi接口。
  * (2) 报策略订单和查询通知是通过异步方式提供。
  * (3) 客户端应用程序可通过AlgoXApi发出报策略单和查询策略请求，通过继承AlgoXSpi并重写回调函数来响应后台服务，处理算法通知响应。
  * (4) XTP Pro版本的库文件目前只支持64位的，注意创建64位的工程，并且设置64位的编译器来进行编译。



## **2\. Quick Start** ​

### 2.1. 创建Api实例 ​

示例代码如下：

cpp
    
    
    XTPX::API::AlgoXApi* m_pAlgoXApi = NULL;
    int client_id = 1;//一个进程一个client id，可在[0, 255]区间内任选
    std::string save_file_path = "./";//保存xtp api日志的路径，需要有可读写权限
    XTP_ALGO_LOG_LEVEL log_level = XTP_ALGO_LOG_LEVEL_DEBUG;//xtp api日志的输出级别，建议调试时使用debug级别，正常运行时使用info级别
    ///创建AlgoxApi
    m_pAlgoxApi = XTPX::API::AlgoXApi::CreateAlgoXApi(client_id, save_file_path.c_str(), log_level);
    if (NULL == m_pAlgoXApi)
    {
    	//创建API失败
    }

### 2.2. 初始化Api参数 ​

（1）设定心跳超时时间

示例代码如下：

cpp
    
    
    ///设定与算法总线服务器交互的超时时间，单位为秒，默认是15s，调试时可以设定大点
    uint32_t heat_beat_interval = 15;
    m_pAlgoXApi->SetHeartBeatInterval(heat_beat_interval);

（2）设定软件版本号

此软件版本号为用户自定义字段，设定规则是仅可使用如下字符"0-9"、"a-z"、"A-Z"、"."。

示例代码如下：

cpp
    
    
    //设定软件版本号，用户自定义（仅可使用如下字符0-9、a-z、A-Z、.）
    char version[] = "xxxxxxxxxxxxx";
    m_pAlgoXApi->SetSoftwareVersion(version);

### 2.3. 创建Spi类 ​

如果想要获取算法交易的数据，必须得有自己的回调响应类。下面仅以收到算法单响应为例，创建了一个Spi回调响应类MyAlgoXSpi，具体步骤如下：

（1）继承XTPX::API::AlgoXSpi，创建自己的Spi类MyAlgoXSpi

以常用的接口回调函数为例。 algox_spi.h文件，算法交易回调类接口定义：

cpp
    
    
    #include "xtp_algox_api.h"
    
    using namespace XTPX::API;
    
    class MyAlgoXSpi : public AlgoXSpi
    {
    public:
    	MyAlgoXSpi();
    	~MyAlgoXSpi();
    
    	///报送策略订单的响应
    	virtual void OnInsertAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name);
    
    	///撤销策略订单的响应
    	virtual void OnCancelAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name);
    
    	///查询策略列表的响应
    	virtual void OnQueryStrategy(XTPStrategyInfoStruct* strategy_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name);
    
    	///报送母单创建时的推送消息(包括其他客户端创建的母单)
    	virtual void OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name);
    
    	///策略运行时策略状态通知
    	virtual void OnStrategyStateReport(XTPStrategyStateReport* strategy_state, char* user_name);
    
    	///用户建立算法通道的消息响应
    	virtual void OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info);
    
    	///当客户端与AlgoBus通信连接断开时，该方法被调用。
    	virtual void OnAlgoDisconnected(int reason);
    
    	///当客户端与AlgoBus断线连接时，该方法被调用，仅在断线重连成功后会被调用。
    	virtual void OnAlgoConnected();
    
    	///策略运行时策略指定证券执行状态通知
    	virtual void OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, char* user_name);
    	
    	///算法推荐的响应
    	virtual void OnStrategyRecommendation(bool basket_flag, XTPStrategyRecommendationInfo* recommendation_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name);
    
    };

（2）重写回调函数逻辑

根据需要重写对应的回调函数逻辑。

### 2.4. 创建Spi实例 ​

示例代码如下：

cpp
    
    
    //创建Spi实例
    MyAlgoXSpi* m_pAlgoXSpi = new MyAlgoXSpi();

### 2.5. 注册Spi ​

示例代码如下：

cpp
    
    
    //注册Spi
    m_pAlgoXApi->RegisterSpi(m_pAlgoXSpi);

### 2.6. 登陆算法服务器 ​

示例代码如下：

cpp
    
    
    std::string algo_server_ip = "xxxx";
    int algo_server_port = xxx;
    std::string account_pw_algo = "xxx";
    std::string account_name_algo = "xxx";
    
    //使用算法账户登录算法服务器
    int login_ret = m_pAlgoXApi->LoginALGO(server_ip_algo.c_str(), server_port_algo, account_name_algo.c_str(), account_pw_algo.c_str(), XTP_ALGO_PROTOCOL_TCP);
    if (login_ret != 0)
    {
    	//登录失败，获取失败原因
    	XTPARI* error_info = m_pAlgoXApi->GetApiLastError();
    	std::cout << "login to AlgoBus error, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
    
    	return 0;
    }
    
    // 登录成功
    std::cout << "Login to algobus success." << std::endl;
    //TODO: 登录成功后必须先建立算法通道才能进行其他操作

### 2.7. 建立算法通道 ​

登陆成功后需要先建立算法通道，算法通道建立成功后才能报送策略订单，查询策略等操作。

一个算法api进程只能登录一个算法账户至算法总线，但是可以使用多个交易账户建立算法通道。

（1） 调用建立算法通道接口

示例代码如下：

cpp
    
    
    int account_count = xxx;
    std::vector<char*> name_array;
    std::vector<char*> pwd_array;
    for (int i = 0; i < account_count; i++)
    {
    
    	std::string account_name_oms = "user";
    	std::string account_pw_oms = "password";
    
    	name_array.push_back(const_cast<char*>(account_name_oms.c_str()));
    	pwd_array.push_back(const_cast<char*>(account_pw_oms.c_str()));
    	std::cout << account_name_oms << " begin to establish channel." << std::endl;
    	//用户建立算法通道
    	int user_ret = m_pAlgoXApi->ALGOUserEstablishChannel(account_name_oms.c_str(),account_pw_oms.c_str());
    	if (user_ret != 0)
    	{
    		std::cout << account_name_oms << " establish channel send error!!!!!!!!!!!" << std::endl;
    	}
    	else
    	{
    		std::cout << account_name_oms << " establish channel send success." << std::endl;
    	}
    }

（2） 重写建立算法通道响应接口逻辑

以输出查询结果为例，示例代码如下：

cpp
    
    
    void MyAlgoXSpi::OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info)
    {
    	cout << "------------------- OnALGOUserEstablishChannel-----------" << endl;
    	/// 建立算法通道的异步通知
    	if (!error_info || error_info->error_id == 0)
    	{
    		/// 建立算法通道成功后，可以下算法母单
    		std::cout << user_name << " establish channel success." << std::endl;
    
    		/// todo 用户的逻辑，可进行查询策略，报策略单，请求推荐策略等操作
    
    	}
    	else
    	{
    		std::cout << user_name << " verification failed." << std::endl;
    	}
    }

### 2.8. 请求推荐策略 ​

建立算法通道成功后用户可根据需要请求推荐策略。

（1） 调用请求推荐算法接口

示例代码如下：

cpp
    
    
    //请求推荐策略
    	int ret = m_pAlgoXApi->StrategyRecommendation(basket_flag, const_cast<char*>(basket_param.c_str()), user_name.c_str(), 1);
    	if (ret != 0)
    	{
    		XTPARI* error_info = m_pAlgoXApi->GetApiLastError();
    		std::cout << "strategyRecommendation error, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
    	}

（2） 重写推荐策略回报接口逻辑

以输出查询结果为例，示例代码如下：

cpp
    
    
    void MyAlgoXSpi::OnStrategyRecommendation(bool basket_flag, XTPStrategyRecommendationInfo* recommendation_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name)
    {
    	cout << "------------------- OnStrategyRecommendation-----------" << endl;
    	if(error_info && error_info->error_id != 0)
    	{
    		std::cout << "Strategy Recommendation failed: " << error_info->error_id << ", " << error_info->error_msg << std::endl;
    		return;
    	}
    	std::cout << "request_id:" << request_id << ",is_last:" << is_last;
    	std::cout << ", basket_flag:" << basket_flag;
    	std::cout << ",ticker:" << recommendation_info->m_ticker << ", market:" << recommendation_info->m_market << ", type:" << recommendation_info->m_strategy_type;//<< std::endl;
    	std::cout << ",strategy_param:" << strategy_param << endl;	
    }

### 2.9. 报送策略订单 ​

用户建立算法通道成功后可根据需要进行报送策略单。

示例代码如下：

cpp
    
    
    //报送策略订单
    uint32_t strategy_type = 3102;
    uint64_t client_strategy_id = 1;
    std::string strategy_param = "xxxxx";
    std::string user_name = "xxxxx";
    
    int ret = m_pAlgoXApi->InsertAlgoOrder(strategy_type, strategy_client_id, (char*)strategy_param.c_str(), (char*)user_name.c_str());
    if (ret == 0)
    {
    	std::cout <<"Insert algo order send success." << std::endl;
    }
    else
    {
    	std::cout << "Failed to insert algo order." << std::endl;
    	XTPARI* error_info = m_pAlgoXApi->GetApiLastError();
    	std::cout << "error id: " << error_info->error_id << " error msg: " << error_info->error_msg << std::endl;
    }

### 2.10. 母单创建推送消息 ​

当用户成功报送策略订单后，会收到算法总线服务器推送的母单创建推送消息，此时OnNewStrategyCreateReport()函数会被调用。该响应表明算法总线服务器收到了报单且开始创建母单。

用户可以重写响应接口里面的处理逻辑，下面以输出日志为例：

cpp
    
    
    void MyAlgoXSpi::OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name)
    {
    	cout << "------------------- OnNewStrategyCreateReport-----------" << endl;
    	//TODO:处理母单响应，此处仅以做屏幕输出为例，用户可以用自己的处理逻辑改写
    	std::cout << ",strategy:" << strategy_info->m_xtp_strategy_id << ", client id:" << strategy_info->m_client_strategy_id;
    	std::cout << ", type:" << strategy_info->m_strategy_type << ", status:" << strategy_info->m_strategy_state;//<< std::endl;
    	std::cout << ",strategy_param:" << strategy_param << endl;
    }

### 2.11. 用户策略指定证券运行情况状态通知 ​

当用户成功报单后，在母单创建推送消息之后会收到算法总线服务推送的用户策略指定证券运行情况的状态通知，此时OnStrategySymbolStateReport()函数会被调用。

用户可以重写响应接口里面的处理逻辑，下面以输出日志为例：

cpp
    
    
    void MyAlgoXSpi::OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, char* user_name)
    {
    	cout << "------------------- OnStrategySymbolStateReport-----------" << endl;
    	//TODO:处理订单响应，此处仅以做屏幕输出为例，用户可以用自己的处理逻辑改写
    	std::cout << "strategy:" << strategy_symbol_state->m_strategy_info.m_xtp_strategy_id << ", client id:" << strategy_symbol_state->m_strategy_info.m_client_strategy_id;
    	std::cout <<", type:" << strategy_symbol_state->m_strategy_info.m_strategy_type << ", status:" << strategy_symbol_state->m_strategy_info.m_strategy_state << std::endl;
    	std::cout << "ticker:" << strategy_symbol_state->m_ticker << ", market:" << strategy_symbol_state->m_market << endl;
    }

### 2.12. 报策略单通知响应 ​

当用户成功报送策略订单后，会有对应的通知响应推送，此时OnInsertAlgoOrder函数会被调用。

用户可以改写报单通知响应里面的处理逻辑，下面以输出日志为例：

cpp
    
    
    void MyAlgoXSpi::OnInsertAlgoOrder(XTPStrategyInfoStruct * strategy_info, XTPARI * error_info, char* user_name)
    {
    	std::cout << "------------------- OnInsertAlgoOrder-----------" << endl;
    	/// 报送策略订单后的异步通知 
    	/// TODO:处理订单响应，此处仅以做屏幕输出为例，用户可以用自己的处理逻辑改写
    	if (error_info && error_info->error_id != 0)
    	{
    		std::cout << "Insert algo order failed: " << error_info->error_id << ", " << error_info->error_msg << std::endl;
    		return;
    	}
    
    	/// 算法单建立成功
    	std::cout << "Insert algo order success." << endl;
    	std::cout << "strategy:" << strategy_info->m_xtp_strategy_id << ", client id:" << strategy_info->m_client_strategy_id; 
    	std::cout << ", type:" << strategy_info->m_strategy_type << ", status:" << (strategy_info->m_strategy_state - 0) << std::endl;
    
    }

### 2.13. 策略状态通知响应 ​

当用户收到算法报单成功的响应后，根据策略的运行状态算法总线会推送策略状态通知，此时OnStrategyStateReport()函数会被调用。

用户可以改写策略状态通知响应里面的处理逻辑，下面以输出日志为例：

cpp
    
    
    void MyAlgoXSpi::OnStrategyStateReport(XTPStrategyStateReport* strategy_state, char* user_name)
    {
    	cout << "------------------- OnStrategyStateReport-----------" << endl;
    	/// TODO:处理策略状态通知响应，此处仅以做屏幕输出为例，用户可以用自己的处理逻辑改写
    	std::cout << "strategy:" << strategy_state->m_strategy_info.m_xtp_strategy_id << ", client id:" << strategy_state->m_strategy_info.m_client_strategy_id;
    	std::cout", type:" << strategy_state->m_strategy_info.m_strategy_type << ", status:" << strategy_state->m_strategy_info.m_strategy_state << std::endl;
    }

### 2.14. 断线重连 ​

断线通知**OnAlgoDisconnected()** 回调函数只是单纯的通知用户与算法总线服务器断线，API内部有自动重连的机制，自动重连成功后**OnAlgoConnected()** 函数会被调用，该函数仅在断线重连成功后才会被调用。

断线重连后，断线期间的消息不会再重新推送。

示例代码如下：

cpp
    
    
    void MyAlgoXSpi::OnAlgoDisconnected(int reason)
    {
    	cout << "------------------- OnAlgoDisconnected-----------" << endl;
    	/// 与算法服务器断线，此时api会自动与算法服务器重连，无需用户重连
    }
    
    void MyAlgoXSpi::OnAlgoConnected()
    {
    	cout << "------------------- OnAlgoConnected-----------" << endl;
    	/// 与算法服务器重新建立起连接，仅在断连重连成功后通知
    }

## **3\. 算法交易时需注意的问题** ​

  * (1) 一个算法API实例支持一个算法账户登陆，多个不同的交易账户建立算法通道，一个进程中仅允许创建一个算法API实例。
  * (2) 用户登录算法总线后，必须建立算法通道，才能进行后续报策略单，查询策略等操作，否则会报错。
  * (3) 用户进行报策略单，查询策略等操作时入参账户均是交易账户，算法账户仅在登录是使用。
  * (4) 如果用户断线后，算法API会自动重连，无需用户进行重连操作；断线重连后，断线期间的消息不会再重新推送。
  * (5) InsertAlgoOrder()成功后，会依次收到OnNewStrategyCreateReport()、OnStrategySymbolStateReport()、OnInsertAlgoOrder()、OnStrategyStateReport()响应消息。
  * (6) 算法API不支持过夜，请务必每天重启进程。
  * (7) 算法总线服务器目前仅支持TCP连接。



## **4\. 简单Demo示例代码** ​

下面是一个简单的代码示例，演示了算法API通过TCP方式连接算法总线服务器并建立算法通道的过程，包括：创建、初始化、登录算法总线、建立算法通道、报送策略母单以及处理收到算法相关的推送消息。  
main.cpp文件

cpp
    
    
    // testAlgoxApi.cpp : 
    //
    
    #include "xtp_algox_api.h"
    #include <string>
    #include <map>
    #include <iostream>
    #include <vector>
    
    #ifdef _WIN32
    #include <windows.h>
    #else
    #include <unistd.h>
    #endif // _WIN32
    
    #include "algox_spi.h"
    #include <stdio.h>
    
    using namespace XTPX::API;
    
    XTPX::API::AlgoXApi* m_pAlgoXApi = NULL;///全局变量，程序公用一个算法API
    std::string algo_server_ip = "xxxxxx";///算法总线服务器ip地址，请自行修改
    int algo_server_port = xxx; ///算法总线服务器port，请自行修改
    std::string account_name_algo = "xxxxxxxx";//算法总线服务器的登陆账户名，请自行修改
    std::string account_pw_algo = "xxxxxx";//算法总线的登陆密码，请自行修改
    std::string account_name_oms = "xxxxxxxx";//建立算法通道的账户名，请自行修改
    std::string account_pw_oms = "xxxxxx";//建立算法通道的账户密码，请自行修改
    
    int main()
    {
    
    	int client_id = 1;
    	std::string save_file_path = "./";//保存xtp api日志的路径，需要有可读写权限
    	XTP_ALGO_LOG_LEVEL log_level = XTP_ALGO_LOG_LEVEL_DEBUG;//xtp api日志的输出级别，建议调试时使用debug级别，正常运行时使用info以上级别
    	
    	m_pAlgoXApi = XTPX::API::AlgoXApi::CreateAlgoXApi(client_id, save_file_path.c_str(), log_level);
    	if (!m_pAlgoXApi)
    	{
    		std::cout << "Failed to create algox api, please check the input parameters." << std::endl;
    		return 0;
    	}
    
    	int32_t heat_beat_interval = 15;
    	m_pAlgoXApi->SetHeartBeatInterval(heat_beat_interval);
    	MyAlgoXSpi* m_pAlgoXSpi = new MyAlgoXSpi();
    	if (!m_pAlgoXSpi)
    	{
    		std::cout << "Failed to create AlgoX spi, please check the input parameters." << std::endl;
    		return 0;
    	}
    	m_pAlgoXApi->RegisterSpi(m_pAlgoXSpi);
    	m_pAlgoXSpi->setUserAPI(m_pAlgoXApi);
    
    	int login_ret = 0;
    	std::cout << account_name_algo << " begin to login AlgoBus." << std::endl;
    	login_ret = m_pAlgoXApi->LoginALGO(algo_server_ip.c_str(), algo_server_port, account_name_algo.c_str(), account_pw_algo.c_str(), XTP_ALGO_PROTOCOL_TCP);
    	if (login_ret != 0)
    	{
    		std::cout << account_name_algo << " login to AlgoBus error!!!!!!!!!!!" << std::endl;
    
    	}
    	else
    	{
    		std::cout << account_name_oms << " begin to establish channel." << std::endl;
    		int user_ret = m_pAlgoXApi->ALGOUserEstablishChannel(account_name_oms.c_str(),account_pw_oms.c_str());
    		if (user_ret != 0)
    		{
    			std::cout << account_name_oms << " establish channel send error!!!!!!!!!!!" << std::endl;
    		}
    		else
    		{
    			std::cout << account_name_oms << " establish channel send success." << std::endl;
    		}
    	}
    
    	while (true)
    	{
    #ifdef _WIN32
    		Sleep(1000);
    #else
    		sleep(1);
    #endif // _WIN32
    
    	}
    
    	return 0;
    }

MyAlgoXSpi类相关定义和实现文件。

algox_spi.h文件

cpp
    
    
    #pragma once
    #include "xtp_algox_api.h"
    #include <fstream>
    
    using namespace XTPX::API;
    
    class MyAlgoXSpi : public AlgoXSpi
    {
    public:
    	MyAlgoXSpi();
    	~MyAlgoXSpi();
    
    	///报送策略订单通知
    	virtual void OnInsertAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name);
    	///取消策略订单通知
    	virtual void OnCancelAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name);
    	///查询策略通知
    	virtual void OnQueryStrategy(XTPStrategyInfoStruct* strategy_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name);
    	///母单创建通知
    	virtual void OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name);
    	///策略状态变化通知
    	virtual void OnStrategyStateReport(XTPStrategyStateReport* strategy_state, char* user_name);
    	///建立算法通道通知
    	virtual void OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info);
    	///算法总线服务器断线通知
    	virtual void OnAlgoDisconnected(int reason);
    	///算法总线服务器重连成功通知
    	virtual void OnAlgoConnected();
    	///策略运行时策略指定证券执行状态通知
    	virtual void OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, char* user_name);
    	///策略推荐通知
    	virtual void OnStrategyRecommendation(bool basket_flag, XTPStrategyRecommendationInfo* recommendation_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name);
    
    };

algox_spi.cpp文件

cpp
    
    
    #include "algox_spi.h"
    #include <iostream>
    #include <stdio.h>
    #ifndef _WIN32
    #include <unistd.h>
    #else
    #include <windows.h>
    #endif
    
    using namespace std;
    
    extern XTPX::API::AlgoXApi* m_pAlgoXApi;//全局变量，程序共用的api
    
    MyAlgoXSpi::MyAlgoXSpi()
    :request_id_(0)
    {
    
    }
    
    MyAlgoXSpi::~MyAlgoXSpi()
    {
    }
    
    
    
    void MyAlgoXSpi::OnAlgoDisconnected(int reason)
    {
    	cout << "------------------- OnAlgoDisconnected-----------" << endl;
    	/// 与算法服务器断线，此时api会自动与算法服务器重连，无需用户重连
    }
    
    void MyAlgoXSpi::OnAlgoConnected()
    {
    	cout << "------------------- OnAlgoConnected-----------" << endl;
    	/// 与算法服务器重新建立起连接，仅在断连重连成功后通知
    }
    
    void MyAlgoXSpi::OnQueryStrategy(XTPStrategyInfoStruct* strategy_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name)
    {
    	cout << "------------------- OnQueryStrategy-----------" << endl;
    	if (error_info && error_info->error_id != 0)
    	{
    		std::cout << "query strategy failed: " << error_info->error_id << error_info->error_msg << std::endl;
    		return;
    	}
    
    	std::cout << "request_id:" << request_id << ",is_last:" << is_last << ",strategy:" << strategy_info->m_xtp_strategy_id << ", client id:" << strategy_info->m_client_strategy_id;
    	std::cout << ", type:" << strategy_info->m_strategy_type << ", status:" << strategy_info->m_strategy_state << ",strategy_param:" << strategy_param << endl;
    
    }
    
    void MyAlgoXSpi::OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info)
    {
    	cout << "------------------- OnALGOUserEstablishChannel-----------" << endl;
    	/// 建立算法通道的异步通知
    	if (!error_info || error_info->error_id == 0)
    	{
    		/// 建立算法通道成功后，可以下算法母单
    		std::cout << user_name << " establish channel success." << std::endl;
    
    		/// 算法单的参数
    		uint64_t client_strategy_id = xxx;
    		uint32_t strategy_type = xxx;
    		std::string strategy_param = "xxx";
    
    		/// 发送算法单
    		std::cout << "Begin to insert algo order." << std::endl;
    		int ret = m_pAlgoXApi->InsertAlgoOrder(strategy_type, client_strategy_id, (char*)strategy_param.c_str(), user_name);
    		if (ret == 0)
    		{
    			std::cout <<"Insert algo order send success." << std::endl;
    		}
    		else
    		{
    			std::cout << "Failed to insert algo order." << std::endl;
    			XTPARI* error_info = m_pAlgoXApi->GetApiLastError();
    			std::cout << "error id: " << error_info->error_id << " error msg: " << error_info->error_msg << std::endl;
    		}
    
    	}
    	else
    	{
    		std::cout << user_name << " verification failed." << error_info->error_id << "," << error_info->error_msg << std::endl;
    	}
    }
    
    void MyAlgoXSpi::OnInsertAlgoOrder(XTPStrategyInfoStruct * strategy_info, XTPARI * error_info, char* user_name)
    {
    	cout << "------------------- OnInsertAlgoOrder-----------" << endl;
    	/// 发送算法单后的异步通知
    	if (error_info && error_info->error_id != 0)
    	{
    		std::cout << "Insert algo order failed: " << error_info->error_id << ", " << error_info->error_msg << std::endl;
    		return;
    	}
    
    	/// 算法单建立成功
    	std::cout << "Insert algo order success." << endl;
    	std::cout << "strategy:" << strategy_info->m_xtp_strategy_id << ", client id:" << strategy_info->m_client_strategy_id;
    	std::cout << ", type:" << strategy_info->m_strategy_type << ", status:" << (strategy_info->m_strategy_state - 0) << std::endl;
    
    	/// 需要撤销算法单的时候，可以发送撤销算法单消息
    	/*std::cout << "Begin to cancel algo order." << std::endl;
    	int ret = m_pAlgoXApi->CancelAlgoOrder(true, strategy_info->m_xtp_strategy_id, user_name);
    	if (ret == 0)
    	{
    		std::cout << "Cancel algo order send success." << std::endl;
    	}
    	else
    	{
    		std::cout << "Failed to send cancel algo order." << std::endl;
    		XTPARI* error_info = m_pAlgoXApi->GetApiLastError();
    		std::cout << "error id: " << error_info->error_id << " error msg: " << error_info->error_msg << std::endl;
    	}*/
    
    }
    
    void MyAlgoXSpi::OnCancelAlgoOrder(XTPStrategyInfoStruct * strategy_info, XTPARI * error_info, char* user_name)
    {
    	cout << "------------------- OnCancelAlgoOrder-----------" << endl;
    	if (error_info && error_info->error_id != 0)
    	{
    		std::cout << "Cancel algo order failed: " << error_info->error_id << ", " << error_info->error_msg << std::endl;
    		return;
    	}
    	
    	cout << "Cancel algo order success." << endl;
    	cout << "strategy:" << strategy_info->m_xtp_strategy_id << ", client id:" << strategy_info->m_client_strategy_id;
    	cout << ", type:" << strategy_info->m_strategy_type << ", status:" << (strategy_info->m_strategy_state-0) << std::endl;
    
    }
    
    void MyAlgoXSpi::OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name)
    {
    	cout << "------------------- OnNewStrategyCreateReport-----------" << endl;
    
    	std::cout << ",strategy:" << strategy_info->m_xtp_strategy_id << ", client id:" << strategy_info->m_client_strategy_id; 
    	std::cout << ", type:" << strategy_info->m_strategy_type << ", status:" << strategy_info->m_strategy_state << ",strategy_param:" << strategy_param << endl;
    }
    
    void MyAlgoXSpi::OnStrategyStateReport(XTPStrategyStateReport* strategy_state, char* user_name)
    {
    	cout << "------------------- OnStrategyStateReport-----------" << endl;
    
    	std::cout << "strategy:" << strategy_state->m_strategy_info.m_xtp_strategy_id << ", client id:" << strategy_state->m_strategy_info.m_client_strategy_id; 
    	std::cout << ", type:" << strategy_state->m_strategy_info.m_strategy_type << ", status:" << strategy_state->m_strategy_info.m_strategy_state << std::endl;
    }
    
    void MyAlgoXSpi::OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, char* user_name)
    {
    	cout << "------------------- OnStrategySymbolStateReport-----------" << endl;
    
    	std::cout << "strategy:" << strategy_symbol_state->m_strategy_info.m_xtp_strategy_id << ", client id:" << strategy_symbol_state->m_strategy_info.m_client_strategy_id; 
    	std::cout << ", type:" << strategy_symbol_state->m_strategy_info.m_strategy_type << ", status:" << strategy_symbol_state->m_strategy_info.m_strategy_state << std::endl;
    	std::cout << "ticker:" << strategy_symbol_state->m_ticker << ", market:" << strategy_symbol_state->m_market << endl;
    }
    
    void MyAlgoXSpi::OnStrategyRecommendation(bool basket_flag, XTPStrategyRecommendationInfo* recommendation_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name)
    {
    	cout << "------------------- OnStrategyRecommendation-----------" << endl;
    	if(!error_info && error_info->error_id != 0)
    	{
    		std::cout << "Strategy Recommendation failed: " << error_info->error_id << ", " << error_info->error_msg << std::endl;
    		return;
    	}
    	std::cout << "request_id:" << request_id << ",is_last:" << is_last << ", basket_flag:" << basket_flag << ",ticker:" << recommendation_info->m_ticker;
    	std::cout << ", market:" << recommendation_info->m_market << ", type:" << recommendation_info->m_strategy_type << ",strategy_param:" << strategy_param << endl;	
    }
