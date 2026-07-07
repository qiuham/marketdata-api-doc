---
api_type: market_data
source_type: vitepress
version: XTP Pro
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
provider_name: 中泰证券
product: xtppro
product_id: zhongtai-xtppro
id: zhongtai-xtppro-xtp-pro行情xquote-api断线后应对措施
title: XTP-Pro行情XQuote-API断线后应对措施
source_url: 'https://xtp.zts.com.cn/xtp-pro/API4/%E8%A1%8C%E6%83%85XQuote-API%E6%96%AD%E7%BA%BF%E5%90%8E%E5%BA%94%E5%AF%B9%E6%8E%AA%E6%96%BD.html'
page_url: 'https://xtp.zts.com.cn/xtp-pro/'
updated_at: 2026-05-21
---

# XTP-Pro行情XQuote-API断线后应对措施

**XTP-Pro行情XQuote-API断线后应对措施**

目录

  * **1\. 与行情服务器断连现象**
  * **2\. 与TCP行情服务器断连应对措施**
  * **3\. 与UDP行情服务器断连应对措施**
    * 3.1. 后续不再有查询需求和行情回补需求
    * 3.2. 后续有查询需求或行情回补需求
    * 3.3. 回补行情数据

  


在程序运行过程中，不可避免出现与行情服务器断连的情况，下面就断连时出现的回调通知，以及应对措施加以说明（适用于XTPX版本的api）。

## **1\. 与行情服务器断连现象** ​

当API与行情服务器出现断线时，OnDisconnected()回调函数将会被触发。

## **2\. 与TCP行情服务器断连应对措施** ​

当用户与行情服务器之间采用的是TCP连接时，为了后续收到行情数据，需要重写**OnDisconnected()** 回调函数。 回调函数中的总体思路是循环调用**Login()** ，直至重连成功后，重新订阅快照行情。 示例代码如下：

cpp
    
    
    void MyQuoteSpi::OnDisconnected(int reason)
    {
    	//行情服务器断线后，此函数会被调用
    	//TODO:重新login，并在login成功后，再次订阅
    
    	cout << "Disconnect from quote server. " << endl;
    
    	//重新登陆行情服务器
    	int ret = -1;
    	while (0 != ret)
    	{
    		ret = m_pQuoteApi->Login(quote_server_ip.c_str(), quote_server_port, quote_username.c_str(), quote_password.c_str(), protocol_type);
    		if (0 != ret)
    		{
    			// 登录失败，获取错误信息
    			XTPRI* error_info = m_pQuoteApi->GetApiLastError();
    			cout << "login to server error, " << error_info->error_id << " : " << error_info->error_msg << endl;
    
    			//等待10s以后再次连接，可修改此等待时间，建议不要小于3s
    #ifdef _WIN32
    			Sleep(10000);
    #else
    			sleep(10);
    #endif // _WIN32	
    		}
    	}
    
    	//重连成功
    	cout << "login to server success. " << endl;
    	//再次订阅行情快照
    	subscribeMarketData();
    
    }

## **3\. 与UDP行情服务器断连应对措施** ​

对于UDP行情服务器来说，行情是通过UDP组播来接收的，OnDisconnected()回调函数被触发时，其实只是表明TCP连接的断连，不会影响UDP组播接收行情数据。因此需要用户根据实际情况来决定是否需要建立TCP的重连。

### 3.1. 后续不再有查询需求和行情回补需求 ​

如果用户在断连后没有查询行情静态数据的需求以及行情回补需求，此时可以不用重连。

### 3.2. 后续有查询需求或行情回补需求 ​

如果用户在断连后有查询行情静态数据的需求或者行情回补需求，可以参考TCP断线重连方式进行重连，无需在登陆后重新订阅。 示例代码如下：

cpp
    
    
    void MyQuoteSpi::OnDisconnected(int reason)
    {
    	//行情服务器断线后，此函数会被调用
    	//TODO:重新login，并在login成功后，再次订阅
    
    	cout << "Disconnect from quote server. " << endl;
    
    	//重新登陆行情服务器
    	int ret = -1;
    	while (0 != ret)
    	{
    		ret = m_pQuoteApi->Login(quote_server_ip.c_str(), quote_server_port, quote_username.c_str(), quote_password.c_str(), protocol_type);
    		if (0 != ret)
    		{
    			// 登录失败，获取错误信息
    			XTPRI* error_info = m_pQuoteApi->GetApiLastError();
    			cout << "login to server error, " << error_info->error_id << " : " << error_info->error_msg << endl;
    
    			//等待10s以后再次连接，可修改此等待时间，建议不要小于3s
    #ifdef _WIN32
    			Sleep(10000);
    #else
    			sleep(10);
    #endif // _WIN32	
    		}
    	}
    
    	//重连成功
    	cout << "login to server success. " << endl;
    
    }

### 3.3. 回补行情数据 ​

通常发生断线的时候，可能是网路状态不好导致，此时可能会有行情丢包发生。 如果发现有行情丢包情形发生，可以通过调用请求回补行情接口，将丢失的数据回补回去。  
注意：XTP-Pro行情回补与XTP行情回补不同，当与行情服务器发生断连时，要先重连行情服务器，再使用行情回补功能。 具体回补行情的用法可以参阅《关于L2行情数据回补功能的使用说明》文档。
