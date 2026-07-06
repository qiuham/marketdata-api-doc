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
id: zhongtai-xtp-2074064395721338882
title: 行情Quote-API断线后应对措施
doc_id: 2074064395721338882
doc_category: 范例和教程
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2074064395721338882'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-07-06
---

# 行情Quote-API断线后应对措施

- [一.与行情服务器断连现象](#一与行情服务器断连现象)
- [二.与TCP行情服务器断连应对措施](#二与tcp行情服务器断连应对措施)
- [三.与UDP行情服务器断连应对措施](#三与udp行情服务器断连应对措施)
    - [1.后续不再有查询需求](#1后续不再有查询需求)
    - [2.后续有查询需求](#2后续有查询需求)
    - [3.回补行情数据](#3回补行情数据)


在程序运行过程中，不可避免出现与行情服务器断连的情况，下面就断连时出现的回调通知，以及应对措施加以说明（适用于2.2.33.5以上版本api）。
如果使用的是2.2.33.5以下版本的api（不包含2.2.33.5版本），无论行情服务器是TCP还是UDP的，都请参考以下文中的第二章节：与TCP行情服务器断连应对措施 进行断线重连。

## 一.与行情服务器断连现象


当API与行情服务器出现断线时，OnDisconnected()回调函数将会被触发。


## 二.与TCP行情服务器断连应对措施


当用户与行情服务器之间采用的是TCP连接时，为了后续收到行情数据，需要重写 **OnDisconnected()** 回调函数。
回调函数中的总体思路是循环调用 **Login()** ，直至重连成功后，重新订阅快照行情。
示例代码如下：
```cpp
void MyQuoteSpi::OnDisconnected(int reason)
{
	//行情服务器断线后，此函数会被调用
	//TODO:重新login，并在login成功后，再次订阅

	cout Login(quote_server_ip.c_str(), quote_server_port, quote_username.c_str(), quote_password.c_str(), protocol_type);
		if (0 != ret)
		{
			// 登录失败，获取错误信息
			XTPRI* error_info = m_pQuoteApi->GetApiLastError();
			cout error_id error_msg OnDisconnected()回调函数被触发时，其实只是表明TCP连接的断连，不会影响UDP组播接收行情数据。因此需要用户根据实际情况来决定是否需要建立TCP的重连。


### 1.后续不再有查询需求


如果用户在断连后没有查询行情静态数据的需求，此时可以不用重连。


### 2.后续有查询需求


如果用户在断连后有查询行情静态数据的需求，可以参考TCP断线重连方式进行重连，无需在登陆后重新
订阅。
示例代码如下：
```cpp
void MyQuoteSpi::OnDisconnected(int reason)
{
	//行情服务器断线后，此函数会被调用
	//TODO:重新login，并在login成功后，再次订阅

	cout Login(quote_server_ip.c_str(), quote_server_port, quote_username.c_str(), quote_password.c_str(), protocol_type);
		if (0 != ret)
		{
			// 登录失败，获取错误信息
			XTPRI* error_info = m_pQuoteApi->GetApiLastError();
			cout error_id error_msg 《XTP关于L2行情数据回补功能的使用说明》文档。
