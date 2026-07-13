---
api_type: guide
source_type: http_api
version: XTP 3.0
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
provider_name: 中泰证券
product: xtp
product_id: zhongtai-xtp
id: zhongtai-xtp-2076482915994222594
title: 交易Trader-API使用指南QuickStart
doc_id: 2076482915994222594
doc_category: XTP API 快速入门
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2076482915994222594'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-07-13
---

# 交易Trader-API使用指南QuickStart

目录


- [一. 交易库介绍](#一-交易库介绍)
	- [1.头文件](#头文件)
	- [2.库文件](#库文件)
	- [3.使用说明](#接口说明)
- [二. Quick Start](#二-quick-start)
	- [1.创建Api实例](#创建api实例)
	- [2.初始化Api参数](#初始化api参数)
	- [3.创建Spi类](#创建spi类)
	- [4.创建Spi实例](#创建spi实例)
	- [5.注册Spi](#注册spi)
	- [6.登陆交易服务器](#登陆交易服务器)
	- [7.查询账户资金](#查询用户资金)
	- [8.查询账户持仓](#查询用户持仓)
	- [9.报单](#报单)
	- [10.处理订单响应](#处理订单响应)
	- [11.处理成交回报](#处理成交回报)
	- [12.断线重连](#断线重连)
- [三. 交易时需注意的问题](#三-交易时需注意的问题)
- [四. 简单Demo示例代码](#四-简单demo示例代码)


# 一.  交易库介绍


该文档旨在帮助开发者快速使用极速交易平台XTP的交易API，文中是Trader-API接口调用示例。


## 头文件


|  文件名               | 详情                                |
|  ----                | ----                                |
| `xtp_trader_api.h`    |交易接口头文件，交易接口类。	  |
| `xtp_api_struct.h`   |业务数据结构。                      |
| `xtp_api_data_type.h`|交易和行情的数据基本类型。          |
|`xtp_api_struct_common.h`|定义业务公共数据结构。      |
|`xoms_api_fund_struct.h`|定义资金划拨数据结构。      |
|`xoms_api_struct.h`|定义交易所需数据结构。      |
|`xquote_api_struct.h`|定义行情所需数据结构。      |
|`xquote_api_rebuild_tbt_struct.h`|定义行情回补所需数据结构。|
|`algo_data_type.h`|定义算法所需数据基本类型。|
|`algo_api_struct.h`|定义算法所需数据结构。|


## 库文件


| 适用系统 | 文件名 |
| ---- | ---- |
| windows | `xtptraderapi.dll  xtptraderapi.lib`  |
| linux | `libxtptraderapi.so`  |
| macos | `libxtptraderapi.dylib`|


## 接口说明


- (1) 交易API提供了两个接口类：交易类TraderApi接口和交易回调类TraderSpi接口。
- (2) 报单和查询通知是通过异步方式提供。
- (3) 客户端应用程序可通过TraderApi发出报单和查询请求，通过继承TraderSpi并重写回调函数来响应后台服务，处理回报数据。
- (4) XTP的库文件目前只支持64位的，注意创建64位的工程，并且设置64位的编译器来进行编译。


# 二.  Quick Start


## 创建Api实例


示例代码如下：
```cpp
	XTP::API::TraderApi* m_pTraderApi = NULL;
	int client_id = 1;//一个进程一个client id，可在[1, 99]区间内任选，并固定下来
	std::string save_file_path = "./";//保存xtp api日志的路径，需要有可读写权限
	XTP_LOG_LEVEL log_level = XTP_LOG_LEVEL_DEBUG;//xtp api日志的输出级别，建议调试时使用debug级别，正常运行时使用info级别
	///创建TraderApi
	m_pTraderApi = XTP::API::TraderApi::CreateTraderApi(client_id, save_file_path.c_str(), log_level);
	if (NULL == m_pTraderApi)
	{
		//创建API失败
	}

```

## 初始化Api参数


### （1）设定心跳超时时间


示例代码如下：
```cpp
	///设定与交易服务器交互的超时时间，单位为秒，默认是15s，调试时可以设定大点
	uint32_t heat_beat_interval = 15;
	m_pTraderApi->SetHeartBeatInterval(heat_beat_interval);
```

### （2）设定交易公共流首次登录时的传输方式


如果不设置，默认将采用 **Quick** 方式登录。
如果需要获取登录前的报单订单响应和成交回报信息，可以采用 **Restart** 方式登录。
如果不需要登录前的报单订单响应和成交回报信息，可以采用 **Quick** 方式登录。

示例代码如下：
```cpp
	//设定公共流传输方式
	XTP_TE_RESUME_TYPE resume_type = XTP_TERT_QUICK;//第一次登陆所使用的公共流消息传送方式，用户可视自身需要在quick和restart中任选
	m_pTraderApi->SubscribePublicTopic(resume_type);
```

### （3）设定软件开发代码


此软件开发代码，为客户申请XTP开户时，由运营人员提供。如果用户没有收到这个软件开发代码，或者使用已有的软件开发代码无法登录时，请联系运营人员。

示例代码如下：
```cpp
	//设定软件开发代码，由运营人员提供
	char software_key[] = "xxxxxxxxxxxxx";
	m_pTraderApi->SetSoftwareKey(software_key);
```

### （4）设定软件版本号


此软件版本号为用户自定义字段，设定规则是仅可使用如下字符0-9，a-z，A-Z 以及. 。

示例代码如下：
```cpp
	//设定软件版本号，用户自定义（仅可使用如下字符0-9，a-z，A-Z，.）
	char version[] = "xxxxxxxxxxxxx";
	m_pTraderApi->SetSoftwareVersion(version);
```

## 创建Spi类


如果想要获取交易数据，必须得有自己的回调响应类。下面仅以收到订单响应为例，创建了一个Spi回调响应类MyTraderSpi，具体步骤如下：

### （1）继承XTP::API::TraderSpi，创建自己的Spi类MyTraderSpi


以常用的接口回调函数为例。
trader_spi.h文件,交易回调类接口定义：
```cpp
#include "xtp_trader_api.h"

using namespace XTP::API;

class MyTraderSpi : public TraderSpi
{
public:
	MyTraderSpi();
	~MyTraderSpi();

	///交易服务器断线通知
	void OnDisconnected(uint64_t session_id, int reason);

	///报单响应通知
	void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id);

	///成交回报通知
	void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id);

	///撤单失败通知
	void OnCancelOrderError(XTPOrderCancelInfo *cancel_info, XTPRI *error_info, uint64_t session_id);

	///查询持仓回调响应
	void OnQueryPosition(XTPQueryStkPositionRsp *investor_position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id);

	///查询资金回调响应
	void OnQueryAsset(XTPQueryAssetRsp *trading_account, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id);


	//TODO:根据需要可继续重写其他回调函数

};
```

### （2）重写回调函数逻辑


根据需要重写对应的回调函数逻辑。

## 创建Spi实例


示例代码如下：
```cpp
	//创建Spi实例
	MyTraderSpi* m_pTraderSpi = new MyTraderSpi();
```

## 注册Spi


示例代码如下：
```cpp
	//注册Spi
	m_pTraderApi->RegisterSpi(m_pTraderSpi);
```

## 登陆交易服务器


示例代码如下：
```cpp
	std::string trader_server_ip = "xxx.xxx.xxx.xxx";//交易服务器ip地址
	int trader_server_port = xxx;//交易服务器端口port
	std::string trader_username = "xxxxxxxx";//交易服务器的登陆账户名
	std::string trader_password = "xxxxxx";//交易服务器的登陆密码
	std::string local_ip = "192.168.2.111";//用户的本地ip，需要用户自行修改为网卡对应的ip
	uint64_t session_id_ = 0;//用户登陆后对应的session_id

	//登录交易服务器
	session_id_ = m_pTraderApi->Login(trader_server_ip.c_str(), trader_server_port, trader_username.c_str(), trader_password.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str());
	if (0 == session_id_)
	{
		//登录失败，获取失败原因
		XTPRI* error_info = m_pTraderApi->GetApiLastError();
		std::cout error_id error_msg QueryAsset(session_id_, 1);//request_id用户可自定义，此处以1为例
```

### （2） 重写查询资金回报接口逻辑


以输出查询结果为例，示例代码如下：
```cpp
void MyTraderSpi::OnQueryAsset(XTPQueryAssetRsp * trading_account, XTPRI * error_info, int request_id, bool is_last, uint64_t session_id)
{
 	cout total_asset security_asset;
	cout buying_power fund_buy_amount;
	cout fund_buy_fee fund_sell_amount fund_sell_fee QueryPosition(NULL, session_id_, 2);//request_id用户可自定义，此处以2为例
```

### （2） 重写查询持仓回报接口逻辑


以输出查询结果为例，示例代码如下：
```cpp
void MyTraderSpi::OnQueryPosition(XTPQueryStkPositionRsp * investor_position, XTPRI * error_info, int request_id, bool is_last, uint64_t session_id)
{
	if (error_info && error_info->error_id !=0)
	{
		//查询出错
		if (error_info->error_id == 11000350)
		{
			//账户里没有持仓
			cout ticker ticker_name;
	cout total_qty sellable_qty avg_price;
	cout unrealized_pnl position_security_type)
	{
		//此时查询到的持仓为配股或者配债持仓，需要单独处理
	}

	if (is_last)
	{
		//TODO：为最后一条持仓回报，可以进行后续的处理逻辑
	}

}
```

## 报单


在资金和持仓都查询成功后，可以根据需要进行报单。
示例代码如下：
```cpp
	//报单
	//初始化报单结构体，以9.01的限价买入沪市"600000"1000股为例。
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

	uint64_t ret = m_pTraderApi->InsertOrder(&order, session_id_);
	if (ret == 0)
	{
		// 报单失败，获取失败原因
		XTPRI* error_info = m_pTraderApi->GetApiLastError();
		std::cout error_id error_msg order_xtp_id order_client_id order_status order_cancel_xtp_id order_cancel_client_id;
	cout order_submit_status ticker market price;
	cout quantity price_type side position_effect;
	cout qty_traded qty_left;
	cout insert_time update_time cancel_time trade_amount;
	cout order_local_id order_type order_status)
	{
	case XTP_ORDER_STATUS_NOTRADEQUEUEING:
	{
		//订单确认状态，表示订单被交易所接受
		break;
	}
	case XTP_ORDER_STATUS_ALLTRADED:
	{
		//订单全部成交状态，表示订单到达已完结状态
		break;
	}
	case XTP_ORDER_STATUS_PARTTRADEDNOTQUEUEING:
	{
		//订单部分撤单状态，表示订单到达已完结状态
		break;
	}
	case XTP_ORDER_STATUS_CANCELED:
	{
		//订单全部撤单状态，表示订单到达已完结状态
		break;
	}
	case XTP_ORDER_STATUS_REJECTED:
	{
		//订单拒单状态，表示订单因有错误而被拒绝，此时可以关注拒单原因
		if (error_info && (error_info->error_id > 0))
		{
			//TODO:说明有错误导致拒单，此处仅以屏幕输出错误信息为例，用户可以用自己的处理逻辑改写
			cout error_id error_msg order_xtp_id order_client_id;
	cout ticker market price;
	cout quantity side position_effect trade_time trade_amount;
	cout exec_id report_index order_exch_id;
	cout trade_type branch_pbu  **OnDisconnected()** 回调函数，总体思路是调用 **Login()** 重连成功后，重新更新session_id。示例代码如下：
```cpp
void MyTraderSpi::OnDisconnected(uint64_t session_id, int reason)
{
	//交易服务器断线后，此函数会被调用
	//TODO:重新login，并在login成功后，更新session_id

	cout Login(trader_server_ip.c_str(), trader_server_port, trader_username.c_str(), trader_password.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str());
		if (temp_session_id_ == 0)
		{
			// 登录失败，获取错误信息
			XTPRI* error_info = m_pTraderApi->GetApiLastError();
			std::cout error_id error_msg 多个不同的账户登陆，一个进程中仅允许创建一个交易API实例。
- (2) 订单响应OnOrderEvent里不会推送订单的部成状态，需要用户自己结合成交回报来判断订单的部成状态。
- (3) 在登陆的时候，仅支持Quick和Restart两种公共流消息传输模式，如果用户断线后，在不调用Logout()的情况下重连，将默认采用Resume模式连接。
- (4) InsertOrder()成功即可视报单为初始状态。
- (5) 订单号order_xtp_id的生成是在API本地生成，不涉及网络通讯。order_xtp_id将保证当天唯一。
- (6) 交易API不支持过夜，请务必每天重启进程。
- (7) 交易服务器目前仅支持TCP连接。
- (8) 用户自行选择client_id时，仅支持[1,99]之间的数值，[100,255]区间的数值为XTP自有系统所用，用户自己无法选用。
- (9) 交易服务器上有风控控制，请注意报单的频率和拒单数量。触发风控后，可能会被限制下单或强制断线。
- (10) 查询结果中，如果返回的错误信息中error_id=11000350，此时不代表查询出错，仅仅代表没有找到满足查询条件的结果。

# 四.  简单Demo示例代码


下面是一个简单的代码示例，演示了交易API通过TCP方式连接交易服务器并执行查询和报单的过程，包括：创建、初始化、登录交易、在登陆成功后查询资金、查询资金结果收到后查询持仓、收到查询持仓结果后进行报单、处理回报消息、断线重连。
main.cpp文件
```cpp
#include "xtp_trader_api.h"
#include
#include
#ifdef _WIN32
#include
#else
#include
#endif // _WIN32

#include "trade_spi.h"

XTP::API::TraderApi* m_pTraderApi = NULL;//全局变量，程序共用一个api
std::string trader_server_ip = "xxx.xxx.xxx.xxx";//交易服务器ip地址，请自行修改
int trader_server_port = xxx;//交易服务器端口port，请自行修改
std::string trader_username = "xxxxxxxx";//交易服务器的登陆账户名，请自行修改
std::string trader_password = "xxxxxx";//交易服务器的登陆密码，请自行修改
std::string local_ip = "192.168.2.111";//用户的本地ip，需要用户自行修改为网卡对应的ip
uint64_t session_id_ = 0;//用户登陆后对应的session_id

int main()
{
	int client_id = 1;//一个进程一个client id，可在[1, 99]区间内任选，并固定下来
	std::string save_file_path = "./";//保存xtp api日志的路径，需要有可读写权限
	XTP_LOG_LEVEL log_level = XTP_LOG_LEVEL_DEBUG;//xtp api日志的输出级别，建议调试时使用debug级别，正常运行时使用info以上级别


	//初始化交易api
	m_pTraderApi = XTP::API::TraderApi::CreateTraderApi(client_id, save_file_path.c_str(), XTP_LOG_LEVEL_DEBUG);
	if (NULL == m_pTraderApi)
	{
		//创建API失败
		std::cout SetHeartBeatInterval(heat_beat_interval);

	//设定公共流传输方式
	XTP_TE_RESUME_TYPE resume_type = XTP_TERT_QUICK;//第一次登陆所使用的公共流消息传送方式，用户可视自身需要在quick和restart中任选
	m_pTraderApi->SubscribePublicTopic(resume_type);

	//设定用户的开发代码，在XTP申请开户时，由xtp运营人员提供
	char software_key[] = "xxxxxxxxxxxxx";
	m_pTraderApi->SetSoftwareKey(software_key);

	//设定软件版本号，用户自定义（仅可使用如下字符0-9，a-z，A-Z，.）
	char version[] = "xxxxxxxxxxxxx";
	m_pTraderApi->SetSoftwareVersion(version);


	//创建Spi类实例
	MyTraderSpi* m_pTraderSpi = new MyTraderSpi();
	if (NULL == m_pTraderSpi)
	{
		std::cout RegisterSpi(m_pTraderSpi);

	//登录交易服务器
	session_id_ = m_pTraderApi->Login(trader_server_ip.c_str(), trader_server_port, trader_username.c_str(), trader_password.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str());
	if (0 == session_id_)
	{
		//登录失败，获取失败原因
		XTPRI* error_info = m_pTraderApi->GetApiLastError();
		std::cout error_id error_msg QueryAsset(session_id_, 1);//request_id用户可自定义，此处以1为例
	if (ret != 0)
	{
		//查询资金请求发送失败，打印失败原因
		XTPRI* error_info = m_pTraderApi->GetApiLastError();
		std::cout error_id error_msg

using namespace XTP::API;

class MyTraderSpi : public TraderSpi
{
public:
	MyTraderSpi();
	~MyTraderSpi();

	///交易服务器断线通知
	virtual void OnDisconnected(uint64_t session_id, int reason);

	///报单响应通知
	virtual void OnOrderEvent(XTPOrderInfo *order_info, XTPRI *error_info, uint64_t session_id);

	///成交回报通知
	virtual void OnTradeEvent(XTPTradeReport *trade_info, uint64_t session_id);

	///撤单失败通知
	virtual void OnCancelOrderError(XTPOrderCancelInfo *cancel_info, XTPRI *error_info, uint64_t session_id);

	///查询持仓回调响应
	virtual void OnQueryPosition(XTPQueryStkPositionRsp *investor_position, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id);

	///查询资金回调响应
	virtual void OnQueryAsset(XTPQueryAssetRsp *trading_account, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id);

	//TODO:根据需要可继续重写其他回调函数

};
```

trader_spi.cpp文件
```cpp
#include "trade_spi.h"
#include
#include
#ifndef _WIN32
#include
#else
#include
#endif


using namespace std;

extern XTP::API::TraderApi* m_pTraderApi;//全局变量，程序共用的api
extern std::string trader_server_ip;//交易服务器ip地址
extern int trader_server_port;//交易服务器端口port
extern std::string trader_username;//交易服务器的登陆账户名
extern std::string trader_password;//交易服务器的登陆密码
extern std::string local_ip;//用户的本地ip，需要用户自行修改为网卡对应的ip
extern uint64_t session_id_;//用户登陆后对应的session_id

MyTraderSpi::MyTraderSpi()
{
}

MyTraderSpi::~MyTraderSpi()
{
}

void MyTraderSpi::OnDisconnected(uint64_t session_id, int reason)
{
	//交易服务器断线后，此函数会被调用
	//TODO:重新login，并在login成功后，更新session_id

	cout Login(trader_server_ip.c_str(), trader_server_port, trader_username.c_str(), trader_password.c_str(), XTP_PROTOCOL_TCP, local_ip.c_str());
		if (temp_session_id_ == 0)
		{
			// 登录失败，获取错误信息
			XTPRI* error_info = m_pTraderApi->GetApiLastError();
			std::cout error_id error_msg order_xtp_id order_client_id order_status order_cancel_xtp_id order_cancel_client_id;
	cout order_submit_status ticker market price;
	cout quantity price_type side position_effect;
	cout qty_traded qty_left;
	cout insert_time update_time cancel_time trade_amount;
	cout order_local_id order_type order_status)
	{
	case XTP_ORDER_STATUS_NOTRADEQUEUEING:
	{
		//订单确认状态，表示订单被交易所接受
		break;
	}
	case XTP_ORDER_STATUS_ALLTRADED:
	{
		//订单全部成交状态，表示订单到达已完结状态
		break;
	}
	case XTP_ORDER_STATUS_PARTTRADEDNOTQUEUEING:
	{
		//订单部分撤单状态，表示订单到达已完结状态
		break;
	}
	case XTP_ORDER_STATUS_CANCELED:
	{
		//订单全部撤单状态，表示订单到达已完结状态
		break;
	}
	case XTP_ORDER_STATUS_REJECTED:
	{
		//订单拒单状态，表示订单因有错误而被拒绝，此时可以关注拒单原因
		if (error_info && (error_info->error_id > 0))
		{
			//TODO:说明有错误导致拒单，此处仅以屏幕输出错误信息为例，用户可以用自己的处理逻辑改写
			cout error_id error_msg order_xtp_id order_client_id;
	cout ticker market price;
	cout quantity side position_effect trade_time trade_amount;
	cout exec_id report_index order_exch_id;
	cout trade_type branch_pbu order_cancel_xtp_id order_xtp_id error_id error_msg error_id !=0)
	{
		//查询出错
		if (error_info->error_id == 11000350)
		{
			//账户里没有持仓
			cout ticker ticker_name;
	cout total_qty sellable_qty avg_price;
	cout unrealized_pnl InsertOrder(&order, session_id_);
		if (ret == 0)
		{
			// 报单失败，获取失败原因
			XTPRI* error_info = m_pTraderApi->GetApiLastError();
			cout error_id error_msg total_asset security_asset;
	cout buying_power fund_buy_amount;
	cout fund_buy_fee fund_sell_amount fund_sell_fee QueryPosition(NULL, session_id_, 2);//request_id用户可自定义，此处以2为例
	if (ret != 0)
	{
		//查询持仓请求发送失败，打印失败原因
		XTPRI* error_info = m_pTraderApi->GetApiLastError();
		cout error_id error_msg << endl;
	}

}


```
