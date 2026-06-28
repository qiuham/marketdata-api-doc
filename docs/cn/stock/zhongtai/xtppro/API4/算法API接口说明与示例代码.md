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
id: zhongtai-xtppro-xtp-pro-algo-api接口说明
title: XTP Pro Algo API接口说明
source_url: 'https://xtp.zts.com.cn/xtp-pro/API4/%E7%AE%97%E6%B3%95API%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E%E4%B8%8E%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81.html'
page_url: 'https://xtp.zts.com.cn/xtp-pro/'
updated_at: 2026-06-08
---

# XTP Pro Algo API接口说明

**XTP Pro Algo API接口说明**

目录

  * **1\. 介绍**
    * 1.1. 接口文件列表
  * **2\. 文档版本和重要更新**
    * 2.1. 版本
  * **3\. 运行环境**
  * **4\. 算法API接口**
    * 4.1. 算法API接口简介
      * 4.1.1. 说明
      * 4.1.2. 代码示例
    * 4.2. AlgoXApi
      * 4.2.1. 接口
      * 4.2.2. 示例代码
      * 4.2.3. CreateAlgoXApi
      * 4.2.4. GetApiVersion
      * 4.2.5. GetApiLastError
      * 4.2.6. RegisterSpi
      * 4.2.7. SetSoftwareVersion
      * 4.2.8. SetHeartBeatInterval
      * 4.2.9. LoginALGO
      * 4.2.10. QueryStrategy
      * 4.2.11. ALGOUserEstablishChannel
      * 4.2.12. InsertAlgoOrder
      * 4.2.13. CancelAlgoOrder
      * 4.2.14. StrategyRecommendation
    * 4.3. AlgoXSpi
      * 4.3.1. 接口
      * 4.3.2. 示例代码
      * 4.3.3. OnQueryStrategy
      * 4.3.4. OnStrategyStateReport
      * 4.3.5. OnALGOUserEstablishChannel
      * 4.3.6. OnInsertAlgoOrder
      * 4.3.7. OnCancelAlgoOrder
      * 4.3.8. OnAlgoDisconnected
      * 4.3.9. OnAlgoConnected
      * 4.3.10. OnStrategySymbolStateReport
      * 4.3.11. OnNewStrategyCreateReport
      * 4.3.12. OnStrategyRecommendation



## **1\. 介绍** ​

本接口说明旨在帮助开发者快速查阅极速交易平台算法API（XTP Pro Algo API）的使用方法、参数说明及注意事项。文中汇集了Algo API使用过程中常见的问题、重要参数说明及接口调用示例。

### 1.1. 接口文件列表 ​

C++头文件：

文件名| 详情  
---|---  
`xtp_algox_api.h`| 算法接口头文件，算法接口类。  
`algox_data_type.h`| 定义算法数据基本类型。  
`algox_api_struct.h`| 定义算法相关数据结构。  
  
算法API的动态链接库：

适用系统| 文件名  
---|---  
windows| `xtpalgoxapi.dll xtpalgoxapi.lib`  
linux| `libxtpalgoxapi.so`  
  
## **2\. 文档版本和重要更新** ​

本次XTP Pro版本的Algo API为首次发布版本。

### 2.1. 版本 ​

V1.0.0

## **3\. 运行环境** ​

Linux操作系统推荐版本为RedHat7、Centos7、Ubuntu16.04及以上。

Windows为windows10及以上的操作系统，支持64位。

## **4\. 算法API接口** ​

### 4.1. 算法API接口简介 ​

#### 4.1.1. 说明 ​

算法API提供了两个接口，分别为AlgoXApi和AlgoXSpi。客户端应用程序可以通过AlgoXApi发出操作请求，通过继承AlgoXSpi并重写回调函数来处理后台服务的响应。

算法API在运行过程中，会将日志写入本地文件中。函数CreateAlgoXApi的第二个参数指明日志文件的路径。若路径不存在会自动创建于系统账户目录。

注意以下事项：

在AlgoXSpi派生类的回调函数中应及时返回，不要阻塞。

API请求的返回参数，一般是0表示正确，其他表示错误，具体见接口详情。详细错误编码请至官网查阅错误列表

#### 4.1.2. 代码示例 ​

◇ 1.源代码

下面是一个简单的代码示例，该示例演示了算法API的初始化、登录算法总线、建立算法通道、算法报单的过程。

以下是MyAlgoXSpi.h文件:

cpp
    
    
    #include "xtp_algox_api.h"
    
    using namespace XTPX::API;
    
    class MyAlgoXSpi : public AlgoXSpi
    {
    public:
    	explicit MyAlgoXSpi();
    	~MyAlgoXSpi();
    
    	///策略报单响应
    	void OnInsertAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name);
    
    	///母单创建通知
    	void OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name);
    
    	///算法通道建立响应
    	void OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info);
    
    	///策略运行时策略状态通知
    	void OnStrategyStateReport(XTPStrategyStateReport* strategy_state, char* user_name);
    
    	///策略运行时策略指定证券执行状态通知
    	void OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, char* user_name);
    
    };

以下是MyAlgoXSpi.cpp文件:

cpp
    
    
    #include "MyAlgoXSpi.h"
    #include <iostream>
    
    MyAlgoXSpi::MyAlgoXSpi()
    :
    {
    }
    
    MyAlgoXSpi::~MyAlgoXSpi()
    {
    }
    
    void MyAlgoXSpi::OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info)
    {
    	cout << "------------------- OnALGOUserEstablishChannel-----------" << endl;
    	/// 建立算法通道的异步通知
    	if (!error_info || error_info->error_id == 0)
    	{
    		/// 建立算法通道成功后，可以下算法母单
    		std::cout << user_name << " establish channel success." << std::endl;
    
    		/// 读取算法单的参数
    		uint64_t client_strategy_id = xxx;
    		uint32_t strategy_type = xxx;
    		std::string strategy_param = "xxx";
    
    		/// 发送算法单
    		std::cout << "Begin to insert algo order." << std::endl;
    		int ret = pUserApi->InsertAlgoOrder(strategy_type, client_strategy_id, (char*)strategy_param.c_str(), user_name);
    		if (ret == 0)
    		{
    			std::cout <<"Insert algo order send success." << std::endl;
    		}
    		else
    		{
    			std::cout << "Failed to insert algo order." << std::endl;
    			XTPARI* error_info = pUserApi->GetApiLastError();
    			std::cout << "error id: " << error_info->error_id << " error msg: " << error_info->error_msg << std::endl;
    		}
    
    	}
    	else
    	{
    		std::cout << user_name << " verification failed." << std::endl;
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
    
    }
    
    void MyAlgoXSpi::OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name)
    {
    	cout << "------------------- OnNewStrategyCreateReport-----------" << endl;
    
    	std::cout << ",strategy:" << strategy_info->m_xtp_strategy_id << ", client id:" << strategy_info->m_client_strategy_id << ", type:" << strategy_info->m_strategy_type;
    	std::cout << ", status:" << strategy_info->m_strategy_state << ",strategy_param:" << strategy_param << endl;
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
    	std::cout << "ticker:" 	<< strategy_symbol_state->m_ticker << ", market:" << strategy_symbol_state->m_market << endl;
    }

以下是MyAlgoXApi.h文件:

cpp
    
    
    #include "xtp_algox_api.h"
    #include "MyAlgoXSpi.h"
    
    class MyAlgoXApi
    {
    public: 
    	explicit MyAlgoXApi();
    	~MyAlgoXApi();
    
    	// 初始化
    	bool initialize();
    	// 登录 
    	int login();
    	// 建立算法通道 
    	int algoUserEstablishChannel();
    
    private: 
    	XTPX::API::AlgoXApi* user_algo_api_;
    	MyAlgoXSpi* m_algo_spi;
    };

以下是MyAlgoXApi.cpp文件:

cpp
    
    
    #include "MyAlgoXApi.h"
    #include <iostream>
    #include <string>
    
    using namespace XTPX::API;
    
    MyAlgoXApi::MyAlgoXApi() 
    {
    	user_algo_api_ = NULL;
    	m_algo_spi = NULL;
    }
    
    MyAlgoXApi::~MyAlgoXApi() 
    { 
    	if (user_algo_api_ != NULL) {
    		user_algo_api_->Logout();
    	}
    }
    
    // 创建并初始化算法API
    bool MyAlgoXApi::initialize()
    { 
    	user_algo_api_ = AlgoXApi::CreateAlgoXApi(1, "./" , XTP_ALGO_LOG_LEVEL_DEBUG);
    	if (user_algo_api_) 
    	{
    		// 注册算法回调接口
    		m_algo_spi = new MyAlgoXSpi();
    		user_algo_api_->RegisterSpi(m_algo_spi);
    		user_algo_api_->SetHeartBeatInterval(15);
    		return true; 
    	}
    	return false;
    } 
    // 登录，用户请自行修改参数
    int MyAlgoXApi::login() 
    { 
    	std::string algo_server_ip = "xxx.xxx.xxx.xxx";
    	int algo_server_port = xxxx;
    	std::string algo_username = "xxxxxxxx";
    	std::string algo_password = "xxxxxx";
    
    	int ret = user_algo_api_->Login(algo_server_ip.c_str(), algo_server_port, algo_username.c_str(), algo_password.c_str(), XTP_ALGO_PROTOCOL_TCP); 
    	if (0 == ret) 
    	{
    		// 登录成功
    	} 
    	else  
    	{ 
    		// 登录失败，并获取错误信息
    		XTPARI* error_info = user_algo_api_->GetApiLastError();
    		std::cout << "login to server error, " << error_info->error_id << " : " << error_info->error_msg << std::endl; 
    	}
    	return ret;
    }   
    // 建立算法通道
    int MyAlgoXApi::algoUserEstablishChannel()
    {
    	///登录oms柜台的用户名和密码
    	std::string account_name_oms = "xxxxxxxx";
    	std::string account_pwd_oms = "xxxxxx";
    	 
    	int ret user_algo_api_->ALGOUserEstablishChannel(account_name_oms.c_str(),account_pw_oms.c_str());
    	return ret;
    }

以下是main.cpp文件:

cpp
    
    
    #include "MyAlgoXApi.h"
    #ifdef _WIN32
    	#include <windows.h>
    #else
    	#include <unistd.h>
    #endif
    
    int main(int argc, char* argv[])
    {
    	MyAlgoXApi *pAlgoXApi = new MyAlgoXApi;
    
    	if (pAlgoXApi)
    	{
    		bool b_ret = pAlgoXApi->initialize();
    		if (! b_ret)
    		{
    			// 初始化失败程序退出
    			return -1;
    		}
    		int ret = pAlgoXApi->login();
    		if (0 == ret)
    		{
    			pAlgoXApi->algoUserEstablishChannel();
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

◇ 2.1. 继承AlgoXSpi类

代码一开始通过#include "xtp_algox_api.h"，将xtpalgoxapi.lib中声明的类和数据类型包括进来，该头文件中有两个重要的基类：AlgoXSpi和AlgoXApi。

AlgoXSpi类提供了算法相关的回调接口，用户需要继承该类并重写这些接口，以获取响应数据。

AlgoXApi类则提供了算法相关的请求接口，例如建立算法通道请求、报送策略订单请求。

我们声明了一个MyAlgoXSpi类，该类继承了AlgoXSpi类，并且重写了OnALGOUserEstablishChannel和OnInsertAlgoOrder等回调接口。当我们收到建立算法通道成功的响应后发起报送策略订单请求成功后，便会触发OnInsertAlgoOrder、OnNewStrategyCreateReport等响应。之后算法总线服务会通过OnStrategyStateReport实时推送策略状态的变化。

我们声明了一个AlgoXApi类型的变量user_algo_api_，创建实例后便可以调用AlgoXApi提供的登录，建立算法通道等接口功能。

◇ 2.2.初始化

initialize()函数里，创建Api实例（AlgoXApi）并为其注册对应的回调接口类的实例（RegisterSpi）。参数"./"指明程序日志文件存放的目录为程序同级目录。

将继承AlgoXSpi类的MyAlgoXSpi注册给AlgoXApi，这样API实例就能把收到的数据通过MyAlgoXSpi的接口推送给用户。

完成以上步骤后，客户端和XTP算法总线登录并建立连接后，就可以调用各种API接口完成算法相关的业务需求。

◇ 2.3.登录

AlgoXSpi成功注册后能够开始登录算法总线服务了，调用AlgoXApi登录接口login，赋值相应字段即可。通过返回值可以判断是否登录成功，0表示成功，其他则表示失败。可以在Login失败后调用GetApiLastError函数，获取失败的原因。Login函数为同步阻塞函数，无需异步等待。

◇ 2.4.建立算法通道行情并报送策略订单

调用建立算法通道的接口ALGOUserEstablishChannel，在OnALGOUserEstablishChannel回调中，如果建立算法通道成功，则用户可以根据需求报送策略订单。若用户需要多个账户建立算法通道，则需要循环调用ALGOUserEstablishChannel接口。

报送策略订单请求发出后，通过OnInserAlgoOrder响应判断是否报送成功。

用户可以在回调函数中做自己的处理逻辑，但是如果处理逻辑比较耗时，应该在另外一个线程处理，而不应该卡在此回调里，否则会导致后续的回调通知消息堵塞在API内部，严重情况下会导致断线。

◇ 2.5.程序运行流程

主函数是业务实现主体。首先初始化MyAlgoXApi类。调用initialize函数开始连接XTP算法总线，依次执行登录、建立算法通道和报送策略订单操作。

### 4.2. AlgoXApi ​

AlgoXApi类提供了算法api的初始化、登录、报送策略订单等功能。

#### 4.2.1. 接口 ​

cpp
    
    
    namespace XTPX {
    	namespace API {
    
    		class ALGOX_API_EXPORT AlgoXApi
    		{
    		public:
    			///创建AlgoXApi
    			///@param client_id （必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义
    			///@param save_file_path （必须输入）存贮订阅信息文件的目录，请设定一个真实存在的有可写权限的路径
    			///@param log_level 日志输出级别
    			///@return 创建出的UserApi
    			///@remark 只能创建一次，系统不支持过夜，请确保每天开盘前重新启动
    			static AlgoXApi *CreateAlgoXApi(uint8_t client_id, const char *save_file_path, XTP_ALGO_LOG_LEVEL log_level = XTP_ALGO_LOG_LEVEL_DEBUG);
    
    			///注册回调接口
    			///@param spi 派生自回调接口类的实例，请在登录之前设定
    			virtual void RegisterSpi(AlgoXSpi *spi) = 0;
    
    			///获取API的系统错误
    			///@return 返回的错误信息，可以在LoginAlgo、InsertAlgoOrder、CancelAlgoOrder返回值为0时调用，获取失败的原因
    			///@remark 可以在调用api接口失败时调用，例如login失败时
    			virtual XTPARI *GetApiLastError() = 0;
    
    			///获取API的发行版本号
    			///@return 返回api发行版本号
    			virtual const char* GetApiVersion() = 0;
    
    			///设置软件开发版本号
    			///@param version 用户开发软件版本号，非api发行版本号，长度不超过15位，以'\0'结尾
    			///@remark 此函数必须在LoginAlgo之前调用，标识的是客户端版本号，而不是API的版本号，由用户自定义
    			virtual void SetSoftwareVersion(const char* version) = 0;
    
    			///设置心跳检测时间间隔，单位为秒
    			///@param interval 心跳检测时间间隔，单位为秒
    			///@remark 此函数必须在LoginAlgo之前调用
    			virtual void SetHeartBeatInterval(uint32_t interval) = 0;
    
    			///用户登录algo服务器请求
    			///@return 表明此资金账号登录是否成功，非“0”表示登录失败，可以调用GetApiLastError()来获取错误代码，“0”表示登录成功
    			///@param ip algo服务器地址，类似“127.0.0.1”
    			///@param port algo服务器端口号
    			///@param user 登录用户名
    			///@param password 登录密码
    			///@param sock_type “1”代表TCP，“2”代表UDP，目前暂时只支持TCP
    			///@remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只需调用一次，所有用户共用即可
    			virtual int LoginALGO(const char* ip, int port, const char* algo_user, const char* password, XTP_ALGO_PROTOCOL_TYPE sock_type) = 0;
    
    			///algo业务中用户报算法单请求
    			///@return 算法报单请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param strategy_type 需要创建的策略类型
    			///@param client_strategy_id 用户自定义id，帮助用户定位
    			///@param strategy_param 策略参数
    			///@param user_name 资金账户
    			///@remark 仅能在用户建立算法通道后使用，算法单的异步通知
    			virtual int InsertAlgoOrder(uint32_t strategy_type, uint64_t client_strategy_id, char* strategy_param, const char* user_name) = 0;
    
    			///algo业务中用户撤销算法单请求
    			///@return 请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param cancel_flag 是否需要算法去处理已下的算法子单标志，true-交给算法自行处理，包括撤单、平仓等，算法处理完成后会通知客户；false-立即停止算法母单的执行，此时算法平台会对已下的子单做撤单操作，其余的平仓等操作需要客户自己处理
    			///@param xtp_strategy_id 需要撤销的算法单在xtp algobus系统中的id
    			///@param user_name 资金账户
    			///@remark 仅能在用户建立算法通道后调用
    			virtual int CancelAlgoOrder(bool cancel_flag, uint64_t xtp_strategy_id, const char* user_name) = 0;
    
    			///algo业务中查询用户策略请求
    			///@return 请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param strategy_type 需要查询的策略类型，可填0
    			///@param client_strategy_id 需要查询的策略用户自定义id，可填0
    			///@param xtp_strategy_id 需要查询的策略在xtp系统中的id，如果指定，就一定按指定查询，如果填0，则按其他筛选条件查询
    			///@param user_name 资金账户
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark xtp_strategy_id条件的优先级最高，只有当xtp_strategy_id为0时，其他条件才生效，此条请求可能对应多条回应消息
    			virtual int QueryStrategy(uint32_t strategy_type, uint64_t client_strategy_id, uint64_t xtp_strategy_id, const char* user_name, int32_t request_id) = 0;
    
    			///用户请求使用algo服务器建立算法通道
    			///@return 表明此资金账号建立算法通道请求消息发送是否成功，非“0”表示发送失败，可以调用GetApiLastError()来获取错误代码，“0”表示发送成功
    			///@param algo_user 登录用户名
    			///@param password 登录密码
    			///@remark 此函数为异步方式，一个用户只能拥有一个算法通道，如果之前已经建立，则无需重复建立
    			virtual int ALGOUserEstablishChannel(const char* user_name, const char* password) = 0;
    
    			///algo业务中请求推荐算法
    			///@return 请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    			///@param basket_flag 是否将满足条件的推荐结果打包成母单篮的标志，true-打包
    			///@param basket_param 需要算法推荐的证券列表，为json字串，具体格式参考说明文档或咨询运营人员
    			///@param user_name 资金账户
    			///@param request_id 用于用户定位查询响应的ID，由用户自定义
    			///@remark 此条请求可能对应多条回应消息，此功能上线时间视服务器后台支持情况而定，具体以运营通知时间为准
    			virtual int StrategyRecommendation(bool basket_flag, char* basket_param, const char* user_name, int32_t request_id) = 0;
    			
    		protected:
    			~AlgoXApi() {};
    		};
    
    	}
    }

#### 4.2.2. 示例代码 ​

以下是MyAlgoXApi.h文件:

cpp
    
    
    #include "xtp_algox_api.h"
    #include "MyAlgoXSpi.h"
    
    using namespace XTPX::API;
    
    class MyAlgoXApi
    {
    public: 
    	explicit MyAlgoXApi();
    	~MyAlgoXApi();
    
    	// 初始化
    	bool initialize();
    
    private: 
    	XTPX::API::AlgoXApi* user_algo_api_;
    	MyAlgoXSpi* m_algo_spi;
    };

以下是MyAlgoXApi.cpp文件:

cpp
    
    
    #include "MyAlgoXApi.h"
    
    MyAlgoXApi::MyAlgoXApi() 
    {
    	user_algo_api_ = NULL;
    	m_algo_spi = NULL;
    }
    
    MyAlgoXApi::~MyAlgoXApi() 
    {
    
    }
    
    bool MyAlgoXApi::initialize()
    {
    	// 创建并初始化算法API
    	user_algo_api_ = XTPX::API::AlgoXApi::CreateAlgoXApi(1, "./", XTP_ALGO_LOG_LEVEL_DEBUG);
    	if (user_algo_api_)
    	{
    		// 注册算法回调接口
    		m_algo_spi = new MyAlgoXSpi();
    		user_algo_api_->RegisterSpi(m_algo_spi);
    		// 登录前参数设置
    		user_algo_api_->SetHeartBeatInterval(15);
    		
    		return true;
    	}
    	return false;
    }

#### 4.2.3. CreateAlgoXApi ​

创建AlgoXApi实例。

◇ 1.函数原型

cpp
    
    
    static AlgoXApi *CreateAlgoXApi(uint8_t client_id, const char *save_file_path, XTP_ALGO_LOG_LEVEL log_level=XTP_ALGO_LOG_LEVEL_DEBUG);

◇ 2.参数

client_id：（必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义

save_file_path：（必须输入）存储行情api日志文件的目录，请设定一个真实存在的有可写权限的路径，如果路径不存在的话，可能会因为写冲突而造成断线

log_level：日志输出级别

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
    XTPX::API::XTP_ALGO_LOG_LEVEL log_level = XTPX::API::XTP_ALGO_LOG_LEVEL_DEBUG;
    
    XTPX::API::AlgoXApi* user_algo_api_ = XTPX::API::AlgoXApi::CreateAlgoXApi(client_id_, stdstr_log_path.c_str(), log_level);
    
    if (user_algo_api_)
    {
    	// 注册算法回调接口
        MyAlgoXSpi *spi = new MyAlgoXSpi();
        user_algo_api_->RegisterSpi(spi);
    }

#### 4.2.4. GetApiVersion ​

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
    if (user_algo_api_)
    {
    	std::cout << "GetApiVersion : " << user_algo_api_->GetApiVersion() << std::endl;
    }

#### 4.2.5. GetApiLastError ​

获取API的系统错误。

可以在调用api接口失败时调用，例如login失败时。

◇ 1.函数原型

cpp
    
    
    virtual XTPARI *GetApiLastError() = 0;

◇ 2.参数

无

◇ 3.返回

cpp
    
    
    namespace XTPX {
    
    	namespace API {
    		///错误信息的字符串长度
    		constexpr int32_t XTP_ALGO_ERR_MSG_LEN = 124;
    		///响应信息
    		typedef struct XTPAlgoRspInfoStruct
    		{
    			///错误代码
    			int32_t	error_id;
    			///错误信息
    			char	error_msg[XTP_ALGO_ERR_MSG_LEN];
    		} XTPARI;
    
    	}
    }

◇ 4.调用示例

cpp
    
    
    // 获取API的系统错误
    if (user_algo_api_)
    {
    	XTPARI* error_info = user_algo_api_->GetApiLastError();
    	std::cout << error_info->error_id << " : " << error_info->error_msg << std::endl;
    }

#### 4.2.6. RegisterSpi ​

注册回调接口。

◇ 1.函数原型

cpp
    
    
    virtual void RegisterSpi(AlgoXSpi *spi) = 0;

◇ 2.参数

spi：派生自回调接口类的实例，请在登录之前设定

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 注册算法回调接口
    if (user_algo_api_)
    {
    	MyAlgoXSpi *spi = new MyAlgoXSpi();
    	user_algo_api_->RegisterSpi(spi);
    }

#### 4.2.7. SetSoftwareVersion ​

设置软件开发版本号。此函数必须在Login之前调用。

◇ 1.函数原型

cpp
    
    
    virtual void SetSoftwareVersion(const char* version) = 0;

◇ 2.参数

version：用户开发软件版本号，非api发行版本号，长度不超过15位，以'\0'结尾

◇ 3.返回

无

◇ 4.调用示例

cpp
    
    
    // 设置软件开发版本号1.1.0，标识的是客户端版本号，而不是API的版本号，由用户自定义
    if (user_algo_api_)
    {
    	user_algo_api_->SetSoftwareVersion("1.1.0");
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
    if (user_algo_api_)
    {
    	user_algo_api_->SetHeartBeatInterval(15);
    }

#### 4.2.9. LoginALGO ​

用户登录algo服务器请求。此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只需调用一次，所有用户共用即可。

登录算法服务器必须使用算法账户登录，交易账户不可登录算法服务器。

◇ 1.函数原型

cpp
    
    
    virtual int LoginALGO(const char* ip, int port, const char* algo_user, const char* password, XTP_ALGO_PROTOCOL_TYPE sock_type) = 0;

◇ 2.参数

ip：algo服务器地址，类似"127.0.0.1"

port：algo服务器端口号

algo_user：算法账户名

password：登录密码

sock_type："1"代表TCP，"2"代表UDP，目前暂时只支持TCP

cpp
    
    
    // XTP_ALGO_PROTOCOL_TYPE是通讯传输协议方式
    typedef enum XTP_ALGO_PROTOCOL_TYPE
    {
    	XTP_ALGO_PROTOCOL_TCP = 1,	///<采用TCP方式传输
    	XTP_ALGO_PROTOCOL_UDP		///<采用UDP方式传输
    }XTP_ALGO_PROTOCOL_TYPE;

◇ 3.返回

表明算法账户登录是否成功，非“0”表示登录失败，可以调用GetApiLastError()来获取错误代码，“0”表示登录成功。

◇ 4.调用示例

cpp
    
    
    // 登录algo服务器请求，参数网址端口账户密码模式等和默认参数本机地址需用户自定义
    if (user_algo_api_)
    {
    	std::string server_ip_algo = "xxx.xxx.xxx.xxx";
    	int server_port_algo = xxxx;
    	std::string account_name_algo = "xxxxxxxx";
    	std::string account_pw_algo = "xxxxxx";
    	std::string local_ip = "xxx.xxx.xxx.xxx";//根据本地网卡对应的ip设定
    	
    	int ret = user_algo_api_->LoginALGO(server_ip_algo.c_str(), server_port_algo, account_name_algo.c_str(), account_pw_algo.c_str(), XTP_ALGO_PROTOCOL_TCP);
        if (login_ret == 0) // 登录algo服务器成功
        {
            std::cout << account_name_algo << " login to AlgoBus success." << std::endl;
        }
        else
        {
    		// 登录algo服务器失败
    		XTPARI* error_info = user_algo_api_->GetApiLastError();
    		std::cout << account_name_algo << " login to AlgoBus error, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
        }
    }

#### 4.2.10. QueryStrategy ​

algo业务中查询用户策略请求。xtp_strategy_id条件的优先级最高，只有当xtp_strategy_id为0时，其他条件才生效，此条请求可能对应多条回应消息.

◇ 1.函数原型

cpp
    
    
    virtual int QueryStrategy(uint32_t strategy_type, uint64_t client_strategy_id, uint64_t xtp_strategy_id, const char* user_name, int32_t request_id) = 0;

◇ 2.参数

strategy_type：需要查询的策略类型，可填0

client_strategy_id：需要查询的策略用户自定义id，可填0

xtp_strategy_id：需要查询的策略在xtp系统中的id，如果指定，就一定按指定查询，如果填0，则按其他筛选条件查询

user_name：资金账户

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

查询请求发送是否成功，"0"表示成功，非"0"表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 查询algo业务中查询用户策略，参数需用户自定义
    if (user_algo_api_)
    {
    	int ret = user_algo_api_->QueryStrategy(0, 0, 0, user_name, request_id);
    }

◇ 5.响应函数

cpp
    
    
    // algo业务中查询策略列表的响应
    virtual void OnQueryStrategy(XTPStrategyInfoStruct* strategy_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name) {};

#### 4.2.11. ALGOUserEstablishChannel ​

用户请求使用algo服务器建立算法通道。此函数为异步方式，一个交易账户只能拥有一个算法通道，如果之前已经建立，则无需重复建立，在使用算法前，请先建立算法通道。

一个算法api进程只能登录一个算法账户至算法总线，但是可以使用多个交易账户建立算法通道。

◇ 1.函数原型

cpp
    
    
    virtual int ALGOUserEstablishChannel(const char* user_name, const char* password) = 0;

◇ 2.参数

user_name：登录用户名

password：登录密码

◇ 3.返回

表明此交易账号建立算法通道请求消息发送是否成功，非“0”表示发送失败，可以调用GetApiLastError()来获取错误代码，“0”表示发送成功

◇ 4.调用示例

cpp
    
    
    // 请求使用algo服务器建立算法通道，参数服务器地址端口用户名密码等需用户自定义
    if (user_algo_api_)
    {
        ///算法用户建立算法通道
    	std::string account_name_oms = "xxxxxxxx";
    	std::string account_pw_oms = "xxxxxx";
    	
    	int ret = user_algo_api_->ALGOUserEstablishChannel(account_name_oms.c_str(), account_pw_oms.c_str());
    	if (ret == 0) // 建立算法通道请求消息，发送成功
    	{
    		std::cout << account_name_oms << " establish channel send success." << std::endl;
    	}
    	else
    	{
    		// 建立算法通道请求消息，发送失败
    		XTPARI* error_info = user_algo_api_->GetApiLastError();
    		std::cout << account_name_algo << " establish channel send error, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
    	}
    }

◇ 5.响应函数

cpp
    
    
    // algo业务中用户建立算法通道的消息响应
    virtual void OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info) {};

#### 4.2.12. InsertAlgoOrder ​

algo业务中用户报算法单请求。

仅能在用户建立算法通道后使用。

◇ 1.函数原型

cpp
    
    
    virtual int InsertAlgoOrder(uint32_t strategy_type, uint64_t client_strategy_id, char* strategy_param, const char* user_name) = 0;

◇ 2.参数

strategy_type：需要创建的策略类型

client_strategy_id：用户自定义id，帮助用户定位

strategy_param：策略参数

user_name：资金账户

◇ 3.返回

算法报单请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码。

◇ 4.调用示例

cpp
    
    
    // 报单，参数需要用户自定义
    if (user_algo_api_)
    {
    	uint32_t strategy_type = xxx;
    	uint64_t client_strategy_id = xxx;
    	std::string strategy_param = "xxxx";
    
    	int ret = user_algo_api_->InsertAlgoOrder(strategy_type, client_strategy_id, (char*)strategy_param.c_str(), user_name);
    	if (ret == 0)  // 发送算法单成功
    	{
    		std::cout <<"Insert algo order send success." << std::endl;
    	}
    	else
    	{
    		// 发送算法单失败，获取下单发送失败的错误信息，并输出打印
    		XTPARI *error_info = user_algo_api_->GetApiLastError();
    		std::cout << "Failed to insert algo order, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
    	}
    }

◇ 5.响应函数

cpp
    
    
    // algo业务中报送策略单的响应
    virtual void OnInsertAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name) {};

#### 4.2.13. CancelAlgoOrder ​

algo业务中用户撤销算法单请求。

仅能在用户建立算法通道后调用。

◇ 1.函数原型

cpp
    
    
    virtual int CancelAlgoOrder(bool cancel_flag, uint64_t xtp_strategy_id, const char* user_name) = 0;

◇ 2.参数

cancel_flag：是否需要撤销的算法单已下的订单，true-撤单，false-不撤单

xtp_strategy_id：需要撤销的算法单在xtp algobus系统中的id

user_name：资金账户

◇ 3.返回

请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码

◇ 4.调用示例

cpp
    
    
    // 撤单，参数用户自定义
    if (user_algo_api_)
    {
    	int ret = user_algo_api_->CancelAlgoOrder(false, xtp_strategy_id, user_name);
    }

◇ 5.响应函数

cpp
    
    
    // algo业务中撤销策略单的响应
    virtual void OnCancelAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name) {};

#### 4.2.14. StrategyRecommendation ​

algo业务中请求推荐算法。

◇ 1.函数原型

cpp
    
    
    virtual int StrategyRecommendation(bool basket_flag, char* basket_param, const char* user_name, int32_t request_id) = 0;

◇ 2.参数

basket_flag：是否将满足条件的推荐结果打包成母单篮的标志，true-打包

basket_param：需要算法推荐的证券列表，为json字串，具体格式参考说明文档或咨询运营人员

user_name：资金账户

request_id：用于用户定位查询响应的ID，由用户自定义

◇ 3.返回

请求发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码

◇ 4.调用示例

cpp
    
    
    // 请求推荐算法
    if (user_algo_api_)
    {
        bool basket_flag = true; //需要打包成母单篮
    	std::string basket_param = "xxxx";//需要算法推荐的证券列表，为json字串
    
    	int ret = user_algo_api_->StrategyRecommendation(basket_flag, (char*)basket_param.c_str(), user_name, request_id);
    
        if (ret == 0)  // 请求发送成功
    	{
    		std::cout <<"Strategy recommendation send success." << std::endl;
    	}
    	else
    	{
    		// 发送请求推荐算法失败，获取发送失败的错误信息，并输出打印
    		XTPARI *error_info = user_algo_api_->GetApiLastError();
    		std::cout << "Failed to strategy recommendation, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
    	}
    
    }

◇ 5.响应函数

cpp
    
    
    ///algo业务中算法推荐的响应
    virtual void OnStrategyRecommendation(bool basket_flag, XTPStrategyRecommendationInfo* recommendation_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name) {};

### 4.3. AlgoXSpi ​

AlgoXSpi类提供了算法相关的回调接口，用户需要继承该类并重写这些接口，以获取响应数据。

#### 4.3.1. 接口 ​

cpp
    
    
    namespace XTPX {
    	namespace API {
    
    		class AlgoXSpi
    		{
    		public:
    			///algo业务中报送策略单的响应
    			///@param strategy_info 用户报送的策略单的具体信息
    			///@param error_info 报送策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param user_name 资金账户
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnInsertAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name) {};
    
    			///algo业务中撤销策略单的响应
    			///@param strategy_info 用户撤销的策略单的具体信息
    			///@param error_info 撤销策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param user_name 资金账户
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnCancelAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name) {};
    
    			///algo业务中查询策略列表的响应
    			///@param strategy_info 策略具体信息
    			///@param strategy_param 此策略中包含的参数，如果error_info.error_id为0时，有意义
    			///@param error_info 查询查询策略列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param user_name 资金账户
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnQueryStrategy(XTPStrategyInfoStruct* strategy_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name) {};
    
    			///algo业务中报送母单创建时的推送消息(包括其他客户端创建的母单)
    			///@param strategy_info 策略具体信息
    			///@param strategy_param 此策略中包含的参数
    			///@param user_name 资金账户
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name) {};
    
    			///algo业务中策略运行时策略状态通知
    			///@param strategy_state 用户策略运行情况的状态通知
    			///@param user_name 资金账户
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnStrategyStateReport(XTPStrategyStateReport* strategy_state, char* user_name) {};
    
    			///algo业务中用户建立算法通道的消息响应
    			///@param user 用户名
    			///@param error_info 建立算法通道发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误，即算法通道成功
    			///@param user_name 资金账户
    			///@remark 算法通道建立成功后，才能对用户创建策略等操作，一个用户只能拥有一个算法通道，如果之前已经建立，则无需重复建立
    			virtual void OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info) {};
    
    			///当客户端与AlgoBus通信连接断开时，该方法被调用。
    			///@param reason 错误原因，请与错误代码表对应
    			///@remark 请不要堵塞此线程，否则会影响algo的登录
    			virtual void OnAlgoDisconnected(int reason) {};
    
    			///当客户端与AlgoBus断线连接时，该方法被调用，仅在断线重连成功后会被调用。
    			virtual void OnAlgoConnected() {};
    
    			///algo业务中策略运行时策略指定证券执行状态通知
    			///@param strategy_symbol_state 用户策略指定证券运行情况的状态通知
    			///@param user_name 资金账户
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, char* user_name) {};
    
    			///algo业务中算法推荐的响应
    			///@param basket_flag 是否将满足条件的推荐结果打包成母单篮的标志，与请求一致，如果此参数为true，那么请以返回的strategy_param为准
    			///@param recommendation_info 推荐算法的具体信息，当basket_flag=true时，此结构体中的market和ticker将没有意义，此时请以strategy_param为准
    			///@param strategy_param 算法参数，可直接用来创建母单，如果error_info.error_id为0时，有意义
    			///@param error_info 请求推荐算法发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    			///@param request_id 此消息响应函数对应的请求ID
    			///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    			///@param user_name 资金账户
    			///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    			virtual void OnStrategyRecommendation(bool basket_flag, XTPStrategyRecommendationInfo* recommendation_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name) {};
    		};
    	}
    }

  


#### 4.3.2. 示例代码 ​

MyAlgoXSpi继承AlgoXSpi

以下是MyAlgoXSpi.h文件:

cpp
    
    
    #include "xtp_algox_api.h"
    
    using namespace XTPX::API;
    
    class MyAlgoXSpi : public AlgoXSpi
    {
    public:
    	explicit MyAlgoXSpi();
    	~MyAlgoXSpi();
    
    	///策略报单响应
    	void OnInsertAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name);
    
    	///母单创建通知
    	void OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name);
    
    	///算法通道建立响应
    	void OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info);
    
    	///策略运行时策略状态通知
    	void OnStrategyStateReport(XTPStrategyStateReport* strategy_state, char* user_name);
    
    	///策略运行时策略指定证券执行状态通知
    	void OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, char* user_name);
    
    };

以下是MyAlgoXSpi.cpp文件:

cpp
    
    
    #include "MyAlgoXSpi.h"
    
    MyAlgoXSpi::MyAlgoXSpi() { }
    MyAlgoXSpi::~MyAlgoXSpi() { }
    
    void MyAlgoXSpi::OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info)
    {
    	cout << "------------------- OnALGOUserEstablishChannel-----------" << endl;
    	/// 建立算法通道的异步通知
    	if (!error_info || error_info->error_id == 0)
    	{
    		/// 建立算法通道成功后，可以下算法母单
    		std::cout << user_name << " establish channel success." << std::endl;
    
    		/// 读取算法单的参数
    		uint64_t client_strategy_id = xxx;
    		uint32_t strategy_type = xxx;
    		std::string strategy_param = "xxx";
    
    		/// 发送算法单
    		std::cout << "Begin to insert algo order." << std::endl;
    		int ret = pUserApi->InsertAlgoOrder(strategy_type, client_strategy_id, (char*)strategy_param.c_str(), user_name);
    		if (ret == 0)
    		{
    			std::cout <<"Insert algo order send success." << std::endl;
    		}
    		else
    		{
    			std::cout << "Failed to insert algo order." << std::endl;
    			XTPARI* error_info = pUserApi->GetApiLastError();
    			std::cout << "error id: " << error_info->error_id << " error msg: " << error_info->error_msg << std::endl;
    		}
    
    	}
    	else
    	{
    		std::cout << user_name << " verification failed." << std::endl;
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
    
    }
    
    void MyAlgoXSpi::OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name)
    {
    	cout << "------------------- OnNewStrategyCreateReport-----------" << endl;
    
    	std::cout << ",strategy:" << strategy_info->m_xtp_strategy_id << ", client id:" << strategy_info->m_client_strategy_id;
    	std::cout << ", type:" << strategy_info->m_strategy_type << ", status:" << strategy_info->m_strategy_state;//<< std::endl;
    	std::cout << ",strategy_param:" << strategy_param << endl;
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
    	std::cout << "ticker:" 	<< strategy_symbol_state->m_ticker << ", market:" << strategy_symbol_state->m_market << endl;
    }

  


#### 4.3.3. OnQueryStrategy ​

algo业务中查询策略列表的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnQueryStrategy(XTPStrategyInfoStruct* strategy_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name) {};

◇ 2.参数

strategy_info：策略具体信息

strategy_param：此策略中包含的参数，如果error_info.error_id为0时，有意义

error_info：查询查询策略列表发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：用于用户定位查询响应的ID，由用户自定义

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

user_name：资金账户

cpp
    
    
    ///策略信息结构体
    typedef struct XTPStrategyInfoStruct
    {
    	uint64_t				m_client_strategy_id;	///< 客户策略id
    	uint64_t				m_xtp_strategy_id;		///< xtp策略id
    	uint16_t				m_strategy_type;		///< 策略类型
    	XTPStrategyStateType	m_strategy_state;		///< 策略状态
    	char					unused[5];				///< 预留字段
    } XTPStrategyInfoStruct;

cpp
    
    
    ///XTPStrategyStateType策略状态类型
    typedef uint8_t XTPStrategyStateType;
    
    ///创建中
    constexpr uint32_t XTP_STRATEGY_STATE_CREATING = 0;
    ///已创建
    constexpr uint32_t XTP_STRATEGY_STATE_CREATED = 1;
    ///开始执行中
    constexpr uint32_t XTP_STRATEGY_STATE_STARTING = 2;
    ///已执行
    constexpr uint32_t XTP_STRATEGY_STATE_STARTED = 3;
    ///停止中
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPING = 4;
    ///已停止
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPED = 5;
    ///销毁中
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYING = 6;
    ///已销毁
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYED = 7;
    ///发生错误
    constexpr uint32_t XTP_STRATEGY_STATE_ERROR = 8;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    ///用户查询策略请求
    virtual int QueryStrategy(uint32_t strategy_type, uint64_t client_strategy_id, uint64_t xtp_strategy_id, const char* user_name, int32_t request_id) = 0;

#### 4.3.4. OnStrategyStateReport ​

algo业务中策略运行时策略状态通知。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnStrategyStateReport(XTPStrategyStateReport* strategy_state, char* user_name) {};

◇ 2.参数

strategy_state：用户策略运行情况的状态通知

user_name：资金账户

cpp
    
    
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
    	XTPARI						m_error_info;				///< 错误信息
    } XTPStrategyStateReport;
    
    ///策略信息结构体
    typedef struct XTPStrategyInfoStruct
    {
    	uint64_t				m_client_strategy_id;	///< 客户策略id
    	uint64_t				m_xtp_strategy_id;		///< xtp策略id
    	uint16_t				m_strategy_type;		///< 策略类型
    	XTPStrategyStateType	m_strategy_state;		///< 策略状态
    	char					unused[5];				///< 预留字段
    } XTPStrategyInfoStruct;

cpp
    
    
    ///XTPStrategyStateType策略状态类型
    typedef uint8_t XTPStrategyStateType;
    
    ///创建中
    constexpr uint32_t XTP_STRATEGY_STATE_CREATING = 0;
    ///已创建
    constexpr uint32_t XTP_STRATEGY_STATE_CREATED = 1;
    ///开始执行中
    constexpr uint32_t XTP_STRATEGY_STATE_STARTING = 2;
    ///已执行
    constexpr uint32_t XTP_STRATEGY_STATE_STARTED = 3;
    ///停止中
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPING = 4;
    ///已停止
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPED = 5;
    ///销毁中
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYING = 6;
    ///已销毁
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYED = 7;
    ///发生错误
    constexpr uint32_t XTP_STRATEGY_STATE_ERROR = 8;

◇ 3.返回

无

  


#### 4.3.5. OnALGOUserEstablishChannel ​

algo业务中用户建立算法通道的消息响应。

算法通道建立成功后，才能对用户创建策略等操作，一个用户只能拥有一个算法通道，如果之前已经建立，则无需重复建立。

◇ 1.函数原型

cpp
    
    
    virtual void OnALGOUserEstablishChannel(char* user_name, XTPARI* error_info) {};

◇ 2.参数

user_name：资金账户

error_info：建立算法通道发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误，即算法通道成功

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    ///algo业务中用户建立算法通道请求
    virtual int ALGOUserEstablishChannel(const char* user_name, const char* password) = 0;

#### 4.3.6. OnInsertAlgoOrder ​

algo业务中报送策略单的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnInsertAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name) {};

◇ 2.参数

strategy_info：用户报送的策略单的具体信息

error_info：报送策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

user_name：资金账户

cpp
    
    
    ///策略信息结构体
    typedef struct XTPStrategyInfoStruct
    {
    	uint64_t				m_client_strategy_id;	///< 客户策略id
    	uint64_t				m_xtp_strategy_id;		///< xtp策略id
    	uint16_t				m_strategy_type;		///< 策略类型
    	XTPStrategyStateType	m_strategy_state;		///< 策略状态
    	char					unused[5];				///< 预留字段
    } XTPStrategyInfoStruct;

cpp
    
    
    ///XTPStrategyStateType策略状态类型
    typedef uint8_t XTPStrategyStateType;
    
    ///创建中
    constexpr uint32_t XTP_STRATEGY_STATE_CREATING = 0;
    ///已创建
    constexpr uint32_t XTP_STRATEGY_STATE_CREATED = 1;
    ///开始执行中
    constexpr uint32_t XTP_STRATEGY_STATE_STARTING = 2;
    ///已执行
    constexpr uint32_t XTP_STRATEGY_STATE_STARTED = 3;
    ///停止中
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPING = 4;
    ///已停止
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPED = 5;
    ///销毁中
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYING = 6;
    ///已销毁
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYED = 7;
    ///发生错误
    constexpr uint32_t XTP_STRATEGY_STATE_ERROR = 8;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    ///algo业务中用户报算法单请求
    virtual int InsertAlgoOrder(uint32_t strategy_type, uint64_t client_strategy_id, char* strategy_param, const char* user_name) = 0;

#### 4.3.7. OnCancelAlgoOrder ​

algo业务中撤销策略单的响应。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnCancelAlgoOrder(XTPStrategyInfoStruct* strategy_info, XTPARI *error_info, char* user_name) {};

◇ 2.参数

strategy_info：用户撤销的策略单的具体信息

error_info：撤销策略单发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

user_name：资金账户

cpp
    
    
    ///策略信息结构体
    typedef struct XTPStrategyInfoStruct
    {
    	uint64_t				m_client_strategy_id;	///< 客户策略id
    	uint64_t				m_xtp_strategy_id;		///< xtp策略id
    	uint16_t				m_strategy_type;		///< 策略类型
    	XTPStrategyStateType	m_strategy_state;		///< 策略状态
    	char					unused[5];				///< 预留字段
    } XTPStrategyInfoStruct;

cpp
    
    
    ///XTPStrategyStateType策略状态类型
    typedef uint8_t XTPStrategyStateType;
    
    ///创建中
    constexpr uint32_t XTP_STRATEGY_STATE_CREATING = 0;
    ///已创建
    constexpr uint32_t XTP_STRATEGY_STATE_CREATED = 1;
    ///开始执行中
    constexpr uint32_t XTP_STRATEGY_STATE_STARTING = 2;
    ///已执行
    constexpr uint32_t XTP_STRATEGY_STATE_STARTED = 3;
    ///停止中
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPING = 4;
    ///已停止
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPED = 5;
    ///销毁中
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYING = 6;
    ///已销毁
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYED = 7;
    ///发生错误
    constexpr uint32_t XTP_STRATEGY_STATE_ERROR = 8;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    ///algo业务中用户撤销算法单请求
    virtual int CancelAlgoOrder(bool cancel_flag, uint64_t xtp_strategy_id, const char* user_name) = 0;

  


#### 4.3.8. OnAlgoDisconnected ​

当客户端与AlgoBus通信连接断开时，该方法被调用。

请不要堵塞此线程，否则会影响algo的登录，与Algo之间的连接，断线后会自动重连，用户无需做其他操作。

◇ 1.函数原型

cpp
    
    
    virtual void OnAlgoDisconnected(int reason) {};

◇ 2.参数

reason：错误原因，请与错误代码表对应

◇ 3.返回

无

#### 4.3.9. OnAlgoConnected ​

当客户端与AlgoBus断线后重新连接时，该方法被调用，仅在断线重连成功后会被调用。

◇ 1.函数原型

cpp
    
    
    virtual void OnAlgoConnected() {};

◇ 2.参数

无

◇ 3.返回

无

#### 4.3.10. OnStrategySymbolStateReport ​

algo业务中策略运行时策略指定证券执行状态通知。

需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。

◇ 1.函数原型

cpp
    
    
    virtual void OnStrategySymbolStateReport(XTPStrategySymbolStateReport* strategy_symbol_state, char* user_name) {};

◇ 2.参数

strategy_symbol_state：用户策略指定证券运行情况的状态通知

user_name：资金账户

cpp
    
    
    ///策略中指定证券的算法执行状态结构体
    typedef struct XTPStrategySymbolStateReportStruct
    {
    	XTPStrategyInfoStruct		m_strategy_info;			///< 策略信息
    	char						m_ticker[XTP_ALGO_TICKER_LEN];	///< 证券代码
    	XTP_ALGO_MARKET_TYPE		m_market;					///< 市场
    	XTP_ALGO_SIDE_TYPE			m_side;						///< 买卖方向，=0时为T0单
    	char						unused[3];					///< 预留字段
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
    	XTPARI						m_error_info;				///< 错误信息
    } XTPStrategySymbolStateReport;

cpp
    
    
    ///策略信息结构体
    typedef struct XTPStrategyInfoStruct
    {
    	uint64_t				m_client_strategy_id;	///< 客户策略id
    	uint64_t				m_xtp_strategy_id;		///< xtp策略id
    	uint16_t				m_strategy_type;		///< 策略类型
    	XTPStrategyStateType	m_strategy_state;		///< 策略状态
    	char					unused[5];				///< 预留字段
    } XTPStrategyInfoStruct;

cpp
    
    
    ///XTPStrategyStateType策略状态类型
    typedef uint8_t XTPStrategyStateType;
    
    ///创建中
    constexpr uint32_t XTP_STRATEGY_STATE_CREATING = 0;
    ///已创建
    constexpr uint32_t XTP_STRATEGY_STATE_CREATED = 1;
    ///开始执行中
    constexpr uint32_t XTP_STRATEGY_STATE_STARTING = 2;
    ///已执行
    constexpr uint32_t XTP_STRATEGY_STATE_STARTED = 3;
    ///停止中
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPING = 4;
    ///已停止
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPED = 5;
    ///销毁中
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYING = 6;
    ///已销毁
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYED = 7;
    ///发生错误
    constexpr uint32_t XTP_STRATEGY_STATE_ERROR = 8;

cpp
    
    
    ///XTP_ALGO_SIDE_TYPE是买卖方向类型
    typedef uint8_t XTP_ALGO_SIDE_TYPE;
    
    ///买（新股申购，ETF买，配股，信用交易中担保品买）
    constexpr uint32_t XTP_ALGO_SIDE_BUY = 1;
    ///卖（逆回购，ETF卖，信用交易中担保品卖）
    constexpr uint32_t XTP_ALGO_SIDE_SELL = 2;
    ///申购
    constexpr uint32_t XTP_ALGO_SIDE_PURCHASE = 7;
    ///赎回
    constexpr uint32_t XTP_ALGO_SIDE_REDEMPTION = 8;
    ///拆分
    constexpr uint32_t XTP_ALGO_SIDE_SPLIT = 9;
    ///合并
    constexpr uint32_t XTP_ALGO_SIDE_MERGE = 10;
    ///改版之后的side的备兑，暂不支持
    constexpr uint32_t XTP_ALGO_SIDE_COVER = 11;
    ///改版之后的side锁定（对应开平标识为开）/解锁（对应开平标识为平）
    constexpr uint32_t XTP_ALGO_SIDE_FREEZE = 12;
    /// 融资买入
    constexpr uint32_t XTP_ALGO_SIDE_MARGIN_TRADE = 21;
    /// 融券卖出
    constexpr uint32_t XTP_ALGO_SIDE_SHORT_SELL = 22;
    /// 卖券还款
    constexpr uint32_t XTP_ALGO_SIDE_REPAY_MARGIN = 23;
    /// 买券还券
    constexpr uint32_t XTP_ALGO_SIDE_REPAY_STOCK = 24;
    /// 现券还券
    constexpr uint32_t XTP_ALGO_SIDE_STOCK_REPAY_STOCK = 26;
    /// 余券划转
    constexpr uint32_t XTP_ALGO_SIDE_SURSTK_TRANS = 27;
    /// 担保品转入
    constexpr uint32_t XTP_ALGO_SIDE_GRTSTK_TRANSIN = 28;
    /// 担保品转出
    constexpr uint32_t XTP_ALGO_SIDE_GRTSTK_TRANSOUT = 29;
    
    ///组合策略的组合
    constexpr uint32_t XTP_ALGO_SIDE_OPT_COMBINE = 31; 
    ///组合策略的拆分
    constexpr uint32_t XTP_ALGO_SIDE_OPT_SPLIT = 32; 
    ///组合策略的管理员强制拆分
    constexpr uint32_t XTP_ALGO_SIDE_OPT_SPLIT_FORCE = 33; 
    ///组合策略的交易所强制拆分
    constexpr uint32_t XTP_ALGO_SIDE_OPT_SPLIT_FORCE_EXCH = 34;
    
    ///未知或者无效买卖方向
    constexpr uint32_t XTP_ALGO_SIDE_UNKNOWN = 50;

◇ 3.返回

无

#### 4.3.11. OnNewStrategyCreateReport ​

algo业务中当用户报送母单创建时，包括其他客户端报送创建母单，此用户所有连接都会有此推送消息，此函数将会被调用。

◇ 1.函数原型

cpp
    
    
    virtual void OnNewStrategyCreateReport(XTPStrategyInfoStruct* strategy_info, char* strategy_param, char* user_name) {};

◇ 2.参数

strategy_info：用户策略的具体信息

strategy_param：此母单策略的参数

user_name：资金账户

cpp
    
    
    ///策略信息结构体
    typedef struct XTPStrategyInfoStruct
    {
    	uint64_t				m_client_strategy_id;	///< 客户策略id
    	uint64_t				m_xtp_strategy_id;		///< xtp策略id
    	uint16_t				m_strategy_type;		///< 策略类型
    	XTPStrategyStateType	m_strategy_state;		///< 策略状态
    	char					unused[5];				///< 预留字段
    } XTPStrategyInfoStruct;

cpp
    
    
    ///@brief XTPStrategyStateType策略状态类型
    typedef uint8_t XTPStrategyStateType;
    
    ///创建中
    constexpr uint32_t XTP_STRATEGY_STATE_CREATING = 0;
    ///已创建
    constexpr uint32_t XTP_STRATEGY_STATE_CREATED = 1;
    ///开始执行中
    constexpr uint32_t XTP_STRATEGY_STATE_STARTING = 2;
    ///已执行
    constexpr uint32_t XTP_STRATEGY_STATE_STARTED = 3;
    ///停止中
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPING = 4;
    ///已停止
    constexpr uint32_t XTP_STRATEGY_STATE_STOPPED = 5;
    ///销毁中
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYING = 6;
    ///已销毁
    constexpr uint32_t XTP_STRATEGY_STATE_DESTROYED = 7;
    ///发生错误
    constexpr uint32_t XTP_STRATEGY_STATE_ERROR = 8;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    ///algo业务中用户报算法单请求
    virtual int InsertAlgoOrder(uint32_t strategy_type, uint64_t client_strategy_id, char* strategy_param, const char* user_name) = 0;

#### 4.3.12. OnStrategyRecommendation ​

当算法推荐有响应时，该方法被调用。

◇ 1.函数原型

cpp
    
    
    virtual void OnStrategyRecommendation(bool basket_flag, XTPStrategyRecommendationInfo* recommendation_info, char* strategy_param, XTPARI *error_info, int32_t request_id, bool is_last, char* user_name) {};

◇ 2.参数

basket_flag：是否将满足条件的推荐结果打包成母单篮的标志，与请求一致，如果此参数为true，那么请以返回的strategy_param为准

recommendation_info：推荐算法的具体信息，当basket_flag=true时，此结构体中的market和ticker将没有意义，此时请以strategy_param为准

strategy_param：算法参数，可直接用来创建母单，如果error_info.error_id为0时，有意义

error_info：请求推荐算法发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误

request_id：此消息响应函数对应的请求ID

is_last：此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应

user_name：资金账户

cpp
    
    
    ///推荐算法结构体
    typedef struct XTPStrategyRecommendationInfoStruct
    {
    	char						m_ticker[XTP_ALGO_TICKER_LEN];	///< 证券代码
    	XTP_ALGO_MARKET_TYPE		m_market;					///< 交易市场
    	uint16_t					m_strategy_type;			///< 策略类型
    	char						unused[66];				///< 保留域
    } XTPStrategyRecommendationInfo;

cpp
    
    
    ///交易市场
    typedef uint32_t XTP_ALGO_MARKET_TYPE;
    
    ///初始化值或者未知
    constexpr uint32_t XTP_ALGO_MKT_INIT = 0;   
    ///深圳A股
    constexpr uint32_t XTP_ALGO_MKT_SZ_A = 1;     
    ///上海A股
    constexpr uint32_t XTP_ALGO_MKT_SH_A = 2;     
    ///北京A股
    constexpr uint32_t XTP_ALGO_MKT_BJ_A = 3;
    ///港股    
    constexpr uint32_t XTP_ALGO_MKT_HK = 4;     
    ///港股通上海
    constexpr uint32_t XTP_ALGO_MKT_SH_HK = 5;     
    ///港股通深圳
    constexpr uint32_t XTP_ALGO_MKT_SZ_HK = 6;     
    ///未知交易市场类型
    constexpr uint32_t XTP_ALGO_MKT_UNKNOWN = 7;

◇ 3.返回

无

◇ 4. 触发函数

cpp
    
    
    ///请求推荐算法
    virtual int StrategyRecommendation(bool basket_flag, char* basket_param, const char* user_name, int32_t request_id) = 0;
