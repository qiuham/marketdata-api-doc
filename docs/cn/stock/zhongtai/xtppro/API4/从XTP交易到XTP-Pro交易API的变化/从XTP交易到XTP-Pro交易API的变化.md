---
api_type: migration
source_type: vitepress
version: XTP Pro
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
provider_name: 中泰证券
product: xtppro
product_id: zhongtai-xtppro
id: zhongtai-xtppro-从xtp交易到xtp-pro交易api的变化
title: 从XTP交易到XTP-Pro交易API的变化
source_url: 'https://xtp.zts.com.cn/xtp-pro/API4/%E4%BB%8EXTP%E4%BA%A4%E6%98%93%E5%88%B0XTP-Pro%E4%BA%A4%E6%98%93API%E7%9A%84%E5%8F%98%E5%8C%96/%E4%BB%8EXTP%E4%BA%A4%E6%98%93%E5%88%B0XTP-Pro%E4%BA%A4%E6%98%93API%E7%9A%84%E5%8F%98%E5%8C%96.html'
page_url: 'https://xtp.zts.com.cn/xtp-pro/'
updated_at: 2026-05-20
---

# 从XTP交易到XTP-Pro交易API的变化

**从XTP交易到XTP-Pro交易API的变化**

目录

  * **1\. 新增接口**
    * 1.1. 新增获取分页查询的最大查询数量的接口
    * 1.2. 新增持仓查询接口
    * 1.3. 新增查询用户的股卡信息
    * 1.4. 新增资金划拨查询接口
      * 1.4.1. 查询指定资金划拨订单
      * 1.4.2. 分页查询资金划拨订单
    * 1.5. 登录时客户认证成功的通知
    * 1.6. 登录后重传或续传公共流消息接收结束的通知
    * 1.7. 新增报单状态通知
      * 1.7.1. 报单未知状态的通知
      * 1.7.2. 报单初始状态的通知
    * 1.8. 新增资金划拨订单未知状态的通知
    * 1.9. 服务状态改变时的通知
  * **2\. 已去除接口**
    * 2.1. 去除接口IsServerRestart()
    * 2.2. 去除接口ModifyUserTerminalInfo()
    * 2.3. 去除不必要的报单查询接口以及对应的响应接口
    * 2.4. 去除分级基金查询
    * 2.5. 去除回调函数OnQueryAccountTradeMarket()
  * **3\. 接口功能变更**
    * 3.1. 获取本节点可交易市场类型
    * 3.2. 分页查询
    * 3.3. 查询持仓接口QueryPosition()
  * **4\. 结构体变化**
    * 4.1. 结构体XTPOrderInfo变化
    * 4.2. 结构体XTPTradeReport变化
    * 4.3. 回调函数OnCancelOrderError()中的结构体XTPOrderCancelErrorInfo变化
    * 4.4. 结构体XTPQueryStkPositionRsp变化
    * 4.5. 结构体XTPQueryAssetRsp变化
    * 4.6. 结构体XTPFundTransferNotice变化
    * 4.7. 结构体XTPFundQueryRsp变化
    * 4.8. 结构体XTPOrderInsertInfo变化
    * 4.9. 结构体XTPFundTransferReq变化
    * 4.10. 结构体XTPFundQueryReq变化
  * **5\. 如何从XTP交易迁移到XTP-Pro交易**
    * 5.1. 文件修改
    * 5.2. 代码修改

  


本文档介绍的XTP-Pro版本的交易API用户手册是在XTP版本的基础上进行比较说明。

## **1\. 新增接口** ​

### 1.1. 新增获取分页查询的最大查询数量的接口 ​

XTP-Pro版本的交易API对于所有分页查询接口都设定了分页查询的最大查询数量的限制，如果用户分页查询超出了这个最大允许查询数量，调用接口就会报错，需要用户重新设定更小的分页查询数量，少量查询。接口如下：

cpp
    
    
    ///获取用户分页查询允许的最大查询数量
    ///@return 分页查询允许的最大查询数量req_count，非“0”表示获取成功，“0”表示获取失败，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@remark 此函数必须在Login之后调用，通过这个函数获取的req_count可用于用户进行分页查询请求的填写，如果填写错误，将会导致分页查询接口调用失败
    virtual int64_t GetMaxReqNumOfPagedQuery(uint64_t session_id) = 0;

### 1.2. 新增持仓查询接口 ​

XTP-Pro版本的交易API增加了按股卡信息条件查询对应持仓，请求接口如下：

cpp
    
    
    ///按条件请求查询投资者持仓
    ///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param query_param 需要查询持仓的条件，可以为NULL，表示查询沪深全市场主股卡持仓，如果不为NULL，会优先看股卡信息，如果提供了股卡，需要与market匹配；如果没有提供股卡信息，则默认查询market对应的主股卡持仓（如果此时market为0，ticker不为空，则默认查询主股卡中指定ticker持仓；如果market不为0，ticker不为空，则默认查询主股卡中market里指定ticker的持仓）
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 该方法如果用户没有提供股卡信息，则默认查主股卡的持仓，如果提供了股卡，需要与market匹配，否则查不到正确的持仓。此函数支持查指定合约代码的持仓。当查指定合约代码持仓时，不受查询服务是否可用影响。
    virtual int QueryAllPosition(const XTPQueryStkPositionReq* query_param, uint64_t session_id, int request_id) = 0;

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

  * 当query_param为NULL，仅查询沪深主股卡持仓，该查询受查询服务器是否可用影响。
  * 当query_param->ticker为空，且query_param->account_id也为空，query_param->market指定市场类型，表示查询主股卡对应market市场的持仓，该查询受查询服务器是否可用影响。
  * 当query_param->ticker为空，且query_param->account_id不为空，query_param->market指定市场类型，表示查询account_id股卡上对应market市场的持仓，该查询受查询服务器是否可用影响。
  * 当query_param->ticker不为空，且query_param->account_id为空，query_param->market必须指定ticker对应市场类型，表示查询主股卡上对应ticker的持仓，该查询不受查询服务器是否可用影响。
  * 当query_param->ticker不为空，且query_param->account_id不为空，query_param->market必须指定ticker对应市场类型，表示查询account_id股卡上对应ticker的持仓，该查询不受查询服务器是否可用影响。



注意：用户查询持仓时，查询条件不同，受查询服务影响也不同。只有查询特定合约持仓时，不受查询服务是否可用的影响。

查询持仓的回调响应函数还是OnQueryPosition()。

### 1.3. 新增查询用户的股卡信息 ​

XTP-Pro版本的交易API支持多股卡交易，用户可以查询到账号绑定的所有股卡信息，查询请求接口如下：

cpp
    
    
    ///请求查询用户的证券账户信息（股卡信息）
    ///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    virtual int QuerySecurityAccount(uint64_t session_id, int request_id) = 0;

该查询请求接口的回调响应函数是OnQuerySecurityAccount(), 函数详情如下：

cpp
    
    
    ///请求查询用户证券账户信息响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    ///@param account_info 查询到的用户证券账户信息
    ///@param error_info 查询用户证券账户信息发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    ///@param request_id 此消息响应函数对应的请求ID
    ///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    virtual void OnQuerySecurityAccount(XTPQueryAccountIdRsp *account_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) { (void)account_info; (void)error_info; (void)request_id; (void)is_last; (void)session_id; };
    
    //////////////////////////////////////////////////////////////////////////
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

### 1.4. 新增资金划拨查询接口 ​

XTP-Pro版本的交易API将XTP版本的资金划拨查询接口QueryFundTransfer()改成了下面两种查询方法。

#### 1.4.1. 查询指定资金划拨订单 ​

用户可以指定资金划拨的id来查询，请求接口如下：

cpp
    
    
    ///请求查询指定资金划拨订单
    ///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param serial_id 需要查询的资金划拨订单ID,不可以为0
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 此函数不再支持全部查询，如果需要查询所有资金划拨订单，请使用分页查询接口QueryFundTransferByPage()查询。此函数受资金划拨服务器是否可用影响。
    virtual int QueryFundTransferByID(uint64_t serial_id, uint64_t session_id, int request_id) = 0;

该查询接口的回调响应函数还是OnQueryFundTransfer(),跟XTP版本的一样。

#### 1.4.2. 分页查询资金划拨订单 ​

XTP-Pro版本取消了XTP版本的一次性请求全部查询功能，不过用户可以按分页查询资金划拨，只是可能需要用户根据查询结果来多次发出请求。分页查询请求接口如下：

cpp
    
    
    ///分页请求查询资金划拨订单
    ///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。此函数受资金划拨服务器是否可用影响。
    virtual int QueryFundTransferByPage(const XTPQueryFundTransferByPageReq *query_param, uint64_t session_id, int request_id) = 0;
    
    /////////////////////////////////////////////////////////////////////////
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

注意：当用户请求查询的数据条目超出了服务器设定的分页查询的最大数量，查询接口就会返回错误。建议用户少量查询，分多次请求。

该接口的回调响应函数是OnQueryFundTransferByPage(),函数详情如下：

cpp
    
    
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
    ///@remark 当sequence为0，表明当次查询没有查到任何记录，当is_last为true时，如果sequence等于req_count，那么表示还有报单，可以进行下一次分页查询，如果不等，表示所有报单已经查询完毕。一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。
    virtual void OnQueryFundTransferByPage(XTPFundTransferLog *fund_transfer_info, XTPRI *fund_transfer_err_info, XTPRI *error_info, int64_t req_count, int64_t sequence, int64_t query_reference, int request_id, bool is_last, uint64_t session_id) { (void)fund_transfer_info; (void)fund_transfer_err_info; (void)error_info; (void)req_count; (void)sequence; (void)query_reference; (void)request_id; (void)is_last; (void)session_id; };
    
    /////////////////////////////////////////////////////////////////////////
    ///资金内转流水记录结构体
    /////////////////////////////////////////////////////////////////////////
    typedef struct XTPFundTransferNotice XTPFundTransferLog;
    
    /////////////////////////////////////////////////////////////////////////
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

### 1.5. 登录时客户认证成功的通知 ​

Login时，新增客户账号认证成功的回调通知，此时客户可以提前将session_id和登录的账户名保存对应关系。回调函数详情如下：

cpp
    
    
    ///当客户认证成功时，该方法被调用。		
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param user_name 登录用户名，login时传入的
    ///@remark 用户收到此回调，仅表明已经认证成功，此时还不能向服务器发送报单和查询等操作，需要等login返回才能进行后续下单操作，此处可提前记录并更新用户名与session_id的对应关系
    virtual void OnConnect(uint64_t session_id, const char* user_name) { (void)session_id; (void)user_name; };

### 1.6. 登录后重传或续传公共流消息接收结束的通知 ​

当客户以restart重传方式登录，或者断线重连后，有续传的报单消息，直至消息推送结束后，会收到回调函数OnResumeEnd()的通知，表示重传的消息推送已结束，后面推送消息是实时推送消息。回调函数详情如下：

cpp
    
    
    ///断线重连后，所有需要重传的推送消息（成交回报、订单响应）接收结束通知
    ///@param session_id 账户对应的session_id，登录时得到
    ///@remark 此函数在用户使用quick第一次登录时，不会有触发。只有在API与服务器以restart方式登录时，或者api与服务器非主动断线，且用户重新login后，进行resume消息重传时，当推送消息重传结束时才会调用，收到此通知就表明断线时的推送消息已经接受完毕，后面收到的推送消息将是实时推送消息
    virtual void OnResumeEnd(uint64_t session_id) { (void)session_id; };

### 1.7. 新增报单状态通知 ​

#### 1.7.1. 报单未知状态的通知 ​

当服务端未收到该订单，且未报送到交易所，会推送未知状态的报单回调消息，回调函数详情如下：

cpp
    
    
    ///报单未知状态通知
    ///@param order_xtp_id 未知状态订单的xtp id
    ///@param session_id 账户对应的session_id，登录时得到
    ///@remark 此响应仅表明XTP服务器丢失订单，并没有报送到交易所。
    virtual void OnUnknownOrder(uint64_t order_xtp_id, uint64_t session_id) { (void)order_xtp_id; (void)session_id; };

#### 1.7.2. 报单初始状态的通知 ​

XTP-Pro版本增加了报单初始状态的通知，当用户报单成功且没有被XTP柜台拒单，就会收到该初始状态的回调通知，但该状态并不表示报单到交易所，交易所确认报单以OnOrderEvent()回调消息为准。报单初始状态的回调函数详情如下：

cpp
    
    
    ///报单初始状态通知
    ///@param order_info 订单响应具体信息，用户可以通过order_info.order_xtp_id来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单
    ///@param session_id 账户对应的session_id，登录时得到
    ///@remark 此响应仅表明XTP服务器收到了报单且没被OMS拒单（OMS内部拒单将没有这条ack消息，仅有OrderEvent的拒单消息），不代表已经报送到交易所
    virtual void OnOrderAck(XTPOrderInfo *order_info, uint64_t session_id) { (void)order_info; (void)session_id; };

### 1.8. 新增资金划拨订单未知状态的通知 ​

当用户资金划拨时，资金划拨服务端未收到该订单，且未发送到后台，就会收到该回调通知，回调函数详情如下：

cpp
    
    
    ///资金划拨订单未知状态通知
    ///@param serial_id 未知状态资金划拨订单的serial id
    ///@param session_id 账户对应的session_id，登录时得到
    ///@remark 此响应仅表明XTP资金划拨服务器丢失订单，并没有报送到后台。
    virtual void OnUnknownFundTransfer(uint64_t serial_id, uint64_t session_id) { (void)serial_id; (void)session_id; };

### 1.9. 服务状态改变时的通知 ​

XTP-Pro版本新增的OnServerStatusNotification()回调函数，核心作用是实时推送资金划拨服务、查询服务的可用状态变化，帮助用户及时感知服务的可用性，避免因服务不可用导致操作失败。当用户Login后，默认服务都是可用的，当收到服务不可用的通知时，之前没有完成的查询，不再推送后续消息，需等待查询服务恢复后重新查询。回调函数详情如下：

cpp
    
    
    ///当登录成功后，中途出现某个服务（资金划拨或者查询）服务状态改变时，该方法将被调用。
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param server_type 服务类型，1-资金划拨服务，2-查询服务
    ///@param status 服务是否可用标识，false-服务不可用，true-服务恢复可用
    ///@remark 用户登录成功时，默认服务可用。当用户收到服务不可用的通知时，之前没有完成的查询，将不再推送后续的查询消息，需要用户等待查询服务恢复后重新发起查询。
    virtual void OnServerStatusNotification(uint64_t session_id, uint32_t server_type, bool status) { (void)session_id; (void)server_type; (void)status; };

## **2\. 已去除接口** ​

### 2.1. 去除接口IsServerRestart() ​

对于程序化接入的用户来说，XTP-Pro版本去除了不需要用到的接口IsServerRestart()。在XTP版本该函数原型如下：

cpp
    
    
    ///服务器是否重启过
    ///@return “true”表示重启过，“false”表示没有重启过
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@remark 此函数必须在Login之后调用
    virtual bool IsServerRestart(uint64_t session_id) = 0;

### 2.2. 去除接口ModifyUserTerminalInfo() ​

对于程序化接入的用户来说，XTP-Pro版本去除了不需要用到的接口ModifyUserTerminalInfo()。在XTP版本该函数原型如下：

cpp
    
    
    ///修改已登录用户的硬件信息，仅限授权系统使用
    ///@return 发送消息是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param info 需要修改成的用户硬件信息
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@remark 此函数必须在Login之后调用，且仅限授权系统使用，一般客户无需使用
    virtual int ModifyUserTerminalInfo(const XTPUserTerminalInfoReq* info, uint64_t session_id) = 0;

### 2.3. 去除不必要的报单查询接口以及对应的响应接口 ​

由于XTP-Pro版本统一了XTP版本的结构体XTPOrderInfoEx和结构体XTPOrderInfoEx里面的数据字段了，所以XTP-Pro版本中去除了XTP版本使用的以下接口：

  * QueryOrderByXTPIDEx()



cpp
    
    
    ///根据报单ID请求查询报单-新版本接口
    ///@return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param order_xtp_id 需要查询的报单在xtp系统中的ID，即InsertOrder()成功时返回的order_xtp_id
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    virtual int QueryOrderByXTPIDEx(const uint64_t order_xtp_id, uint64_t session_id, int request_id) = 0;

  * QueryOrdersEx()



cpp
    
    
    ///请求查询报单-新版本接口
    ///@return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param query_param 需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应。此函数不建议轮询使用，当报单量过多时，容易造成用户线路拥堵，导致api断线
    virtual int QueryOrdersEx(const XTPQueryOrderReq *query_param, uint64_t session_id, int request_id) = 0;

  * QueryUnfinishedOrdersEx()



cpp
    
    
    ///请求查询未完结报单-新版本接口
    ///@return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    virtual int QueryUnfinishedOrdersEx(uint64_t session_id, int request_id) = 0;

  * QueryOrdersByPageEx()



cpp
    
    
    ///分页请求查询报单-新版本接口
    ///@return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
    virtual int QueryOrdersByPageEx(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

  * OnQueryOrderEx()



cpp
    
    
    ///请求查询报单响应-新版本接口
    ///@param order_info 查询到的一个报单信息
    ///@param error_info 查询报单时发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    ///@param request_id 此消息响应函数对应的请求ID
    ///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    virtual void OnQueryOrderEx(XTPOrderInfoEx *order_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

  * OnQueryOrderByPageEx()



cpp
    
    
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

### 2.4. 去除分级基金查询 ​

由于分级基金业务已下线，不再支持，XTP-Pro版本去除了XTP版本中查询分级基金的相关接口:

  * 请求接口原型如下：



cpp
    
    
    ///请求查询分级基金
    ///@return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param query_param 需要查询的分级基金筛选条件，其中母基金代码可以为空，则默认所有存在的母基金，如果不为空，请不带空格，并以'\0'结尾，其中交易市场不能为空
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 此函数查询出的结果可能对应多个查询结果响应
    virtual int QueryStructuredFund(XTPQueryStructuredFundInfoReq *query_param, uint64_t session_id, int request_id) = 0;

  * 回调函数原型如下：



cpp
    
    
    ///请求查询分级基金信息响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    ///@param fund_info 查询到的分级基金情况
    ///@param error_info 查询分级基金发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    ///@param request_id 此消息响应函数对应的请求ID
    ///@param is_last 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    virtual void OnQueryStructuredFund(XTPStructuredFundInfo *fund_info, XTPRI *error_info, int request_id, bool is_last, uint64_t session_id) {};

### 2.5. 去除回调函数OnQueryAccountTradeMarket() ​

在XTP-Pro版本中，用户查询本节点可交易市场类型是API本地直接返回，无需通过查询服务端，所以去除XTP版本的响应回调函数OnQueryAccountTradeMarket()，函数原型如下：

cpp
    
    
    ///请求查询用户在本节点上可交易市场的响应
    ///@param trade_location 查询到的交易市场信息，按位来看，从低位开始数，第0位表示沪市，即如果(trade_location&0x01) == 0x01，代表可交易沪市，第1位表示深市，即如果(trade_location&0x02) == 0x02，表示可交易深市，如果第0位和第1位均是1，即(trade_location&(0x01|0x02)) == 0x03，就表示可交易沪深2个市场
    ///@param error_info 查询可交易市场发生错误时，返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    ///@param request_id 此消息响应函数对应的请求ID
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@remark 此查询只会有一个结果
    virtual void OnQueryAccountTradeMarket(int trade_location, XTPRI *error_info, int request_id, uint64_t session_id) {};

## **3\. 接口功能变更** ​

### 3.1. 获取本节点可交易市场类型 ​

在XTP-Pro版本中，用户查询本节点可交易市场类型是API本地直接返回，无需通过查询服务端异步回调过来，所以原XTP版本中的查询接口QueryAccountTradeMarket()名称改成现在的GetAccountTradeMarket(),并直接返回结果。原XTP版本的查询接口原型如下：

cpp
    
    
    ///查询用户在本节点上的可交易市场类型
    ///@return 发送消息是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 此函数必须在Login之后调用，对应的响应函数是OnQueryAccountTradeMarket()
    virtual int QueryAccountTradeMarket(uint64_t session_id, int request_id) = 0;

对应现在XTP-Pro版本的查询接口详情如下：

cpp
    
    
    ///查询用户在本节点上的可交易市场类型
    ///@return 按位来看，从低位开始数，第0位表示沪市，即如果(trade_location&0x01) == 0x01，代表可交易沪市，第1位表示深市，即如果(trade_location&0x02) == 0x02，表示可交易深市，如果第0位和第1位均是1，即(trade_location&(0x01|0x02)) == 0x03，就表示可交易沪深2个市场
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@remark 此函数必须在Login之后调用，为同步函数
    virtual uint32_t GetAccountTradeMarket(uint64_t session_id) = 0;

### 3.2. 分页查询 ​

由于XTP-Pro版本增加了最大分页查询数量限制，当用户请求的分页查询数量超出了系统设定的最大值，分页查询接口就会调用失败，根据错误信息中提示的可允许分页查询数量范围，或者调用接口GetMaxReqNumOfPagedQuery()获取分页查询最大数量，用户重新调整请求的分页查询数量。涉及的请求查询函数如下：

  * QueryOrdersByPage()



cpp
    
    
    ///分页请求查询报单
    ///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
    virtual int QueryOrdersByPage(const XTPQueryOrderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

  * QueryTradesByPage()



cpp
    
    
    ///分页请求查询成交回报
    ///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param query_param 需要分页查询成交回报的条件，如果第一次查询，那么reference填0
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用
    virtual int QueryTradesByPage(const XTPQueryTraderByPageReq *query_param, uint64_t session_id, int request_id) = 0;

  * QueryFundTransferByPage()



cpp
    
    
    ///分页请求查询资金划拨订单
    ///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param query_param 需要分页查询订单的条件，如果第一次查询，那么query_param.reference填0
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 该方法支持分页查询，注意用户需要记录下最后一笔查询结果的reference以便用户下次查询使用。此函数受资金划拨服务器是否可用影响。
    virtual int QueryFundTransferByPage(const XTPQueryFundTransferByPageReq *query_param, uint64_t session_id, int request_id) = 0;

分页查询委托的示例代码：

cpp
    
    
    if (user_api)
    {
    	XTPQueryOrderByPageReq query_param;
    	memset(&query_param, 0, sizeof(XTPQueryOrderByPageReq));
    	
    	int64_t maxReq = user_api->GetMaxReqNumOfPagedQuery(session_id);//获取最大分页查询数量
    	query_param.req_count = maxReq;
    	query_param.reference = 0;
    
    	int ret = user_api->QueryOrdersByPage(&query_param, session_id, request_id);
    	if(ret != 0)//查询请求失败
    	{
    		XTPRI* error_info = user_api->GetApiLastError();
    	    std::cout <<" query orders by page is error, " << error_info->error_id << " : " << error_info->error_msg << std::endl;
    	}
    }

注意：当用户请求查询的数量超出系统设定的分页查询最大值时，会出现类似以下错误信息：
    
    
    error id:10210301,error msg: Query orders by page failed:invalid parameters, req_count must in [1,200].

用户根据错误信息，重新调整req_count参数值。

### 3.3. 查询持仓接口QueryPosition() ​

XTP-Pro版本支持绑定多股卡交易，所以当用户需要查询沪深全市场持仓时，回调函数默认只返回沪深主股卡上的持仓，这点与XTP版本的有所区别，XTP-Pro版本的查询持仓请求接口详情如下：

cpp
    
    
    ///按条件请求查询投资者指定持仓
    ///@return 查询发送是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError()来获取错误代码
    ///@param ticker 需要查询持仓的合约代码，可以为NULL，表示查询沪深全市场主股卡持仓，如果不为NULL，请不带空格，并以'\0'结尾，注意需与market匹配，不匹配的话，查询不到所需的持仓
    ///@param market 需要查询持仓的合约所在市场，仅在合约代码不为NULL的时候，才会使用。使用时，market必须指定。需要查单市场持仓，请使用QueryAllPosition()
    ///@param session_id 资金账户对应的session_id,登录时得到
    ///@param request_id 用于用户定位查询响应的ID，由用户自定义
    ///@remark 该方法如果用户提供了合约代码，则会查询此合约的持仓信息（注意请指定market），如果合约代码为空，则默认查询沪深市场的主股卡持仓信息,类似于使用QueryAllPosition()。
    virtual int QueryPosition(const char *ticker, uint64_t session_id, int request_id, XTP_MARKET_TYPE market) = 0;

注意：XTP-Pro版本的该接口中参数market没有设定默认值XTP_MKT_INIT，用户在调用的时候，需指定市场类型值。另外，当查询指定合约持仓的时候，不受查询服务器是否可用的影响，而查询沪深全市场持仓需要看查询服务器是否可用。

## **4\. 结构体变化** ​

### 4.1. 结构体XTPOrderInfo变化 ​

跟XTP版本相比，XTP-Pro版本的报单回调函数OnOrderEvent()的结构体XTPOrderInfo新增了一些字段，结构体如下：

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

XTP-Pro版本新增了以下字段：

  * exec_type  
XTP-Pro版本增加了交易所执行报单的状态，‘0’-新订单，‘4’-已撤销，‘8’-已拒绝，‘F’-已成交；如果是非交易所的回报，此字段为0。
  * order_exch_id  
交易所订单编号，同XTP版本中查询报单的回调函数OnQueryOrderEx()中结构体XTPOrderInfoEx.order_exch_id一样。
  * order_withhold_amount  
XTP-Pro版本增加了每笔订单会预扣的费用，包含预扣手续费，并不表示实际预扣费用，仅供用户参考。
  * order_withhold_fee  
XTP-Pro版本增加了每笔订单会预扣的手续费，并不表示实际预扣费用，仅供用户参考。
  * exec_id  
XTP-Pro版本报单回调函数里增加了执行编号，交易所字段。
  * strategy_type  
XTP-Pro版本增加了算法策略类型，仅为算法单时有效。
  * set_id  
XTP-Pro版本增加了平台分区号，交易所字段。
  * report_index  
XTP-Pro版本报单回调函数里增加了执行报告编号，交易所字段。
  * transact_time  
XTP-Pro版本增加了报单回报时间，交易所字段。
  * strategy_id  
XTP-Pro版本增加了算法母单编号ID，仅为算法单时有效。
  * error_code  
XTP-Pro版本增加了XTP柜台拒单原因代码。
  * extra_error_code  
XTP-Pro版本增加了外部系统拒单的原因代码,一般是表示交易所拒单的原因代码。
  * account_id  
XTP-Pro版本增加了多股卡交易，该字段是对应报单的股卡号。
  * branch_pbu  
XTP-Pro版本报单回调函数里增加了交易所PBU代码。



### 4.2. 结构体XTPTradeReport变化 ​

跟XTP版本相比，XTP-Pro版本的订单成交回调函数OnTradeEvent()的结构体XTPTradeReport新增了一些字段，结构体如下：

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

XTP-Pro版本新增了以下字段：

  * strategy_type  
XTP-Pro版本增加了算法策略类型，仅为算法单时有效。
  * set_id  
XTP-Pro版本增加了平台分区号。
  * strategy_id  
XTP-Pro版本增加了算法母单编号ID，仅为算法单时有效。
  * account_id  
XTP-Pro版本增加了多股卡交易，该字段是对应报单的股卡号。



### 4.3. 回调函数OnCancelOrderError()中的结构体XTPOrderCancelErrorInfo变化 ​

跟XTP版本相比，XTP-Pro版本的回调函数OnCancelOrderError()的结构体XTPOrderCancelErrorInfo新增了一些字段，结构体如下：

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

XTP-Pro版本新增了以下字段：

  * ticker  
XTP-Pro版本新增证券代码字段。
  * market  
XTP-Pro版本新增交易市场字段。
  * order_client_id  
XTP-Pro版本新增用户自定义字段。
  * transact_time  
XTP-Pro版本新增报单回报时间字段，交易所字段
  * report_index  
XTP-Pro版本新增执行编号字段。
  * set_id  
XTP-Pro版本新增平台分区号字段，交易所字段。
  * error_code  
XTP-Pro版本新增拒单原因代码字段。
  * extra_error_code  
XTP-Pro版本新增外部系统拒单原因代码字段，一般是指交易所拒单原因代码。
  * orig_order_local_id  
XTP-Pro版本新增原始订单编号。
  * order_local_id  
XTP-Pro版本新增本地报单编号。



### 4.4. 结构体XTPQueryStkPositionRsp变化 ​

跟XTP版本相比，XTP-Pro版本的查询持仓回调函数OnQueryPosition()的结构体XTPQueryStkPositionRsp新增了一些字段，结构体如下：

cpp
    
    
    //////////////////////////////////////////////////////////////////////////
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

XTP-Pro版本新增了字段account_id，即股卡，XTP-Pro版本支持多股卡交易，该字段表示查询结果为该股卡上的持仓。

### 4.5. 结构体XTPQueryAssetRsp变化 ​

跟XTP版本相比，XTP-Pro版本的查询资金回调函数OnQueryAsset()的结构体XTPQueryAssetRsp新增了一些字段，结构体如下：

cpp
    
    
    //////////////////////////////////////////////////////////////////////////
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

XTP-Pro版本新增了字段currency_type，即货币种类。

### 4.6. 结构体XTPFundTransferNotice变化 ​
    
    
    跟XTP版本相比，XTP-Pro版本的资金划拨回调函数OnFundTransfer()的结构体XTPFundTransferNotice新增了一些字段，结构体如下：
    

cpp
    
    
    /////////////////////////////////////////////////////////////////////////
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

XTP-Pro版本新增了以下字段：

  * site  
XTP-Pro版本新增了转入或转出的目标服务器对应的节点字段，用户无论登录的是哪个节点，都可以清楚的查询到资金划转的目标节点。



cpp
    
    
    /////////////////////////////////////////////////////////////////////////
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

  * currency_type  
XTP-Pro版本新增了货币种类字段。



cpp
    
    
    /////////////////////////////////////////////////////////////////////////
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

### 4.7. 结构体XTPFundQueryRsp变化 ​

跟XTP版本相比，XTP-Pro版本的回调函数OnQueryOtherServerFund()的结构体XTPFundQueryRsp新增了一些字段，结构体如下：

cpp
    
    
    /////////////////////////////////////////////////////////////////////////
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

XTP-Pro版本新增了以下字段：

  * query_site  
XTP-Pro版本在回调函数OnQueryOtherServerFund()里增加了资金查询的对应交易市场字段，用于表示用户所查询到的资金是哪个市场节点的。



cpp
    
    
    /////////////////////////////////////////////////////////////////////////
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

  * currency_type  
XTP-Pro版本增加了货币种类字段。



cpp
    
    
    /////////////////////////////////////////////////////////////////////////
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

### 4.8. 结构体XTPOrderInsertInfo变化 ​

跟XTP版本相比，XTP-Pro版本的报单接口InsertOrder()的结构体XTPOrderInsertInfo新增了一些字段，结构体如下：

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

XTP-Pro版本新增了以下字段：

  * strategy_type  
XTP-Pro版本增加了算法策略类型字段，普通户不用填。
  * strategy_id  
XTP-Pro版本增加了算法母单编号字段，普通户不用填。
  * account_id  
XTP-Pro版本支持多股卡交易，用户在报单的时候，可以指定股卡报送，如果不填，默认以主股卡报送。
  * branch_pbu  
XTP-Pro版本新增交易所PBU代码字段，普通户不用填。



### 4.9. 结构体XTPFundTransferReq变化 ​
    
    
    跟XTP版本相比，XTP-Pro版本的资金划拨接口FundTransfer()的结构体XTPFundTransferReq增删了一些字段，结构体如下：
    

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

XTP-Pro版本新增了以下字段：

  * site  
XTP-Pro版本新增划转时的目标服务器对应节点类型字段，这个是跨节点划转所必填字段。



cpp
    
    
    /////////////////////////////////////////////////////////////////////////
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

  * currency_type  
XTP-Pro版本新增货币种类字段。



cpp
    
    
    /////////////////////////////////////////////////////////////////////////
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

XTP-Pro版本删除了以下字段：

  * password  
XTP-Pro版本划转资金时，无需再填写密码。



### 4.10. 结构体XTPFundQueryReq变化 ​

跟XTP版本相比，XTP-Pro版本的查询其它节点资金接口QueryOtherServerFund()的结构体XTPFundQueryReq有增删了一些字段，结构体如下：

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

XTP-Pro版本新增了以下字段：

  * query_site  
XTP-Pro版本新增了查询服务器对应节点类型的字段，双中心用户必填。



cpp
    
    
    /////////////////////////////////////////////////////////////////////////
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

  * currency_type  
XTP-Pro版本新增了货币种类字段。



cpp
    
    
    /////////////////////////////////////////////////////////////////////////
    ///@brief XTP_CURRENCY_TYPE是一个货币种类类型
    /////////////////////////////////////////////////////////////////////////
    typedef uint32_t XTP_CURRENCY_TYPE;
    
    ///人民币
    constexpr uint32_t XTP_CURRENCY_CNY = 0;
    ///美元
    constexpr uint32_t XTP_CURRENCY_USD = 1;
    ///港币
    constexpr uint32_t XTP_CURRENCY_HKD = 2;

XTP-Pro版本删除了以下字段：

  * password  
XTP-Pro版本查询其它节点资金时，无需填写密码。



## **5\. 如何从XTP交易迁移到XTP-Pro交易** ​

### 5.1. 文件修改 ​

  * 从官网上下载XTP-Pro版本的SDK，将XTP版本的所有库文件和头文件全部替换成XTP-Pro版本的库文件和头文件，步骤如下：  
(1) 把XTP API交易使用的以下头文件和库文件删除：

![oldLibrary](/xtp-pro/assets/1.B4z2Dxop.jpg)

(2) 把XTP-Pro API交易使用的以下头文件和库文件添加进来：

![newLibrary](/xtp-pro/assets/2.C3IRE8Ni.jpg)




### 5.2. 代码修改 ​

  * XTP-Pro版本的接口类和数据类型是定义在域名XTPX：：API之下，客户在使用相关类和参数类型时，请注意使用域名XTPX::API。

  * XTP-Pro版本的用户调用接口CreateTraderApi()创建api对象时，传入的参数client_id取值范围有变化，普通用户取值区间是[1-24]，如使用值超出范围，请注意修改，函数原型如下：




cpp
    
    
    ///创建TraderApi
    ///@param client_id （必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义，总体取值区间[1,127]，普通用户取值区间[1,24]
    ///@param save_file_path （必须输入）存贮订阅信息文件的目录，请设定一个真实存在的有可写权限的路径
    ///@param log_level 日志输出级别
    ///@return 创建出的UserApi
    ///@remark 只能创建一次，如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，但是对于同一账户，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接。系统不支持过夜，请确保每天开盘前重新启动
    static TraderApi *CreateTraderApi(uint8_t client_id, const char *save_file_path, XTP_LOG_LEVEL log_level = XTP_LOG_LEVEL_DEBUG);

  * 用户在使用接口InsertOrder()或者InsertOrderExtra()进行报单时，可能需要根据新的结构体里的新增字段来修改代码。另外，用户报单时，结构体XTPOrderInsertInfo变量必须使用memset将内存区域初始化为0，如果没有此操作，股卡字段将默认保留随机值（未初始化状态），系统会直接判定为无效订单并拒单！代码示例如下：



cpp
    
    
    // 报入一笔限价单，以9.01的价格买入沪市"600000"的普通交易，数量1000。
    if (user_trade_api_)
    {
    	XTPOrderInsertInfo order;
    	memset(&order, 0, sizeof(XTPOrderInsertInfo));//不可缺少此操作，部分字段需要初始化为空
    
    	order.market = XTP_MKT_SH_A;
    	std::string stdstr_ticker = "600000";
    	strncpy(order.ticker, stdstr_ticker.c_str(), XTP_TICKER_LEN);
    	order.business_type = XTP_BUSINESS_TYPE_CASH;
    	order.side = XTP_SIDE_BUY;
    	order.position_effect = XTP_POSITION_EFFECT_INIT;
    	order.price_type = XTP_PRICE_LIMIT;
    	order.price = 9.01;
    	order.quantity = 1000;
    
    	uint64_t order_xtp_id = user_trade_api_->InsertOrder(&order, session_id_);//默认以主股卡报送订单
    }

  * XTP-Pro版本在查询其它节点资金(QueryOtherServerFund())时,双中心账户查询必须要填写目标节点类型。

  * XTP-Pro版本在资金划拨(FundTransfer())时，跨节点划拨必须要填写目标节点类型。

  * 资金划拨(FundTransfer())或者查询其它节点资金(QueryOtherServerFund())时，结构体已删除字段password，无需填写password，代码中需删除password字段。

  * XTP-Pro版本的回调函数OnCancelOrderError()里的参数类型跟XTP版本不同，用户需要修改回调函数的参数类型XTPOrderCancelErrorInfo，函数原型如下：




cpp
    
    
    ///撤单出错响应
    ///@param cancel_info 撤单具体信息，包括撤单的order_cancel_xtp_id和待撤单的order_xtp_id
    ///@param error_info 撤单被拒绝或者发生错误时错误代码和错误信息，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，当error_info为空，或者error_info.error_id为0时，表明没有错误
    ///@param session_id 资金账户对应的session_id，登录时得到
    ///@remark 此响应只会在撤单发生错误时被回调
    virtual void OnCancelOrderError(XTPOrderCancelErrorInfo *cancel_info, XTPRI *error_info, uint64_t session_id) { (void)cancel_info; (void)error_info; (void)session_id; };

  * XTP-Pro版本中所有分页查询接口都有设定最大分页请求条数，如果超出系统设定的条数，分页查询接口会返回错误，请注意修改请求条数。

  * XTP-Pro版本去除了资金划拨查询接口QueryFundTransfer(),用户查询资金划拨订单可以改用QueryFundTransferByID()或QueryFundTransferByPage()进行查询。

  * 如代码中使用了XTP-Pro版本中已去除的接口IsServerRestart()，ModifyUserTerminalInfo()，QueryOrderByXTPIDEx(),QueryOrdersEx(),QueryUnfinishedOrdersEx(),QueryOrdersByPageEx(),OnQueryOrderEx(),OnQueryOrderByPageEx(),OnQueryAccountTradeMarket()等，请在代码中删除，可调整使用其它相关接口。

  * XTP-Pro版本中查询持仓接口QueryPosition()的第四个参数market去除了默认值，用户调用时，必须设定market值。函数如下：




cpp
    
    
    virtual int QueryPosition(const char *ticker, uint64_t session_id, int request_id, XTP_MARKET_TYPE market) = 0;

使用接口QueryPosition()查询沪深主股卡上所有持仓的代码示例：

cpp
    
    
    //查询沪深主卡上所有持仓
    if(user_api)
    {
    	int ret = user_api->QueryPosition(NULL, session_id, 0, XTP_MKT_INIT)；
    }

  * 使用XTP-Pro版本的用户需在spi回调接口类中增加回调响应函数OnServerStatusNotification()，用于实时接收资金划拨和查询服务端是否可用的通知，当出现不可用时，用户需等待服务恢复再做请求操作。

  * 使用XTP-Pro版本的用户需在spi回调接口类中增加回调响应函数OnConnect(),通过回调过来的参数，提前记录或更新session_id和登录账户之间的对应关系。

  * 使用XTP-Pro版本的用户需在spi回调接口类中增加回调响应函数OnResumeEnd()，当用户登录时，有需要重传的消息，当重传的消息结束时，用户会收到该回调响应，后面收到推送消息将是实时推送消息。

  * 使用XTP-Pro版本的用户需在spi回调接口类中增加回调响应函数OnUnknownOrder()，当服务端未收到该订单，且未报送到交易所，就会收到该回调响应。

  * 使用XTP-Pro版本的用户需在spi回调接口类中增加回调响应函数OnUnknownFundTransfer()，当资金划拨服务端未收到该订单，且未报送到后台，就会收到该回调响应。

  * 使用XTP Pro版本的用户需在spi回调接口类中增加回调响应函数OnOrderAck()，当用户报单后，XTP服务端收到该订单，且未被XTP柜台拒单，就会收到该回调响应，表示报单的初始状态，并不代表已经报送交易所。

  * 凡是通过查询服务返回结果的查询接口，有调用频率限制，用户在调用这些查询接口时，在1秒内不要过于频繁的调用，否则回调函数会返回错误。
