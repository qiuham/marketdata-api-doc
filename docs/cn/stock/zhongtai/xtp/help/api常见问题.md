---
api_type: reference
source_type: http_api
version: XTP 3.0
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
provider_name: 中泰证券
product: xtp
product_id: zhongtai-xtp
id: zhongtai-xtp-2056206187128475650
title: API常见问题
doc_id: 2056206187128475650
doc_category: 其他帮助文档
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2056206187128475650'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-05-18
---

# API常见问题

**1.问：VS下为什么编译的时候，发生链接错误？**


> 答：由于我们的库文件目前只支持64位的，所以请看一下默认的编译选项是否是64位的，如果不是，请选择64位进行编译。


**2.问：API接口是否为异步的？**


> 答：API中登录Login、Logout这类接口为同步阻塞式，当函数返回后，可以视为已经登录成功、登出成功，即可进行后续操作。其余所有接口均为异步的。


**3.问：当调用接口失败时，如何知道失败原因？**


> 答：可以调用GetApiLastError()来获取失败原因。如果调用api接口没有出错，GetApiLastError()返回的则是上一次的错误。


**4.问：CreateTraderApi()中的client_id可以相同么？**


> 答：可以。对于同一account，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接。


**5.问：CreateTraderApi()中的save_file_path必须输入么？**


> 答：必须输入，而且必须是一个有可写权限的实际存在的路径。


**6.问：同一个账户account可以多个客户端同时登录么？**


> 答：对于同一账户account的连接，由api的client_id来进行区分。同一个account，可以同时由不同的client_id来进行登录连接，但是对于同一对account和client_id，一次只能有一个连接，client_id建议选择1~99的整数值，100及以上属于xtp预使用区间，注意：交易中client_id的总使用个数建议不超过5个。


**7.问：同一个api支持多个账号account登录么？**


> 答：支持。用户在登录后会得到一个session_id，用户需要记录下account对应的session_id，所有的接口函数都要用到session_id。


**8.问：连接成功后的session会失效么？**


> 答：在同一个交易日内，如果没有出现断线，api也没有销毁，此次的session不会失效。当然，如果用户在登录后，因为阻塞或者其他什么原因导致心跳包无法按时发送到服务器，那么当其他用户用相同的account和client_id再次登录时，前一个session可视为失效。


**9.问：在Spi回调函数中为何不很快返回有可能导致断线？**


> 答：在服务器向客户端发送的数据量很大的情况下，当用户在Spi回调函数中处理过慢，会导致数据接收缓冲区被填满，服务器无法向客户端发送数据，此时会触发断线。所以在实际使用中，请尽快从响应函数中返回。


**10.问：Api断线后会自动重连么？**


> 答：对于普通交易来说，Api不会自动帮用户重连。用户可以在收到断线通知OnDisconnect()后选择不销毁api，不登出logout()，继续登录login()，此时交易服务器会在用户重新登录后，从断点消息处续传。
> 对于算法交易来说，Api会进行自动重连，收到OnAlgoDisconnected()断线通知时，无需用户操作。在重连成功后，无需重新建立算法通道。
> 注意：使用TCP连接行情服务器在断线后不会重新推送行情，除非用户登录成功后重新订阅。


**11.问：同一个进程中支持几个api？**


> 答：对于交易而言，同一个进程中只允许存在一个TraderApi。当用户多账户登录时，请确保程序中只Create了一次api。
> 对于行情而言，2.2.33.5版本开始支持同一个进程可创建多个QuoteApi，可同时连接多个不同的行情地址，但是只有第一次传入CreateQuoteApi()的参数有效，多个QuoteApi共用一个client_id和一份quote.log日志。


**12.问：XTP平台系统支持过夜么？可以每天早上调用Login()，晚上自动Logout()吗？**

> 答：XTP服务器和API都不支持过夜，只支持当日交易时间段。策略程序必须每日重启，也就是需要用户手动销毁QuoteApi、TraderApi，T+1日再重新开启程序，调用CreateQuoteApi()、CreateTraderApi() 重新创建Api，再Login()。


**13.问：login时选择Restart和Quick公共流订阅方式有什么区别？**


> 答：公共流订阅方式必须在login之前设定，在login之后生效。Restart方式会将今日所有的公共流消息都重新发送一遍，包括：OnOrderEvent()，OnTradeEvent()，OnFundTransfer()。Quick方式登录后，客户端只会收到登录后的一系列公有流消息。


**14.问：订单响应OnOrderEvent()在哪几种状态下会推送？**


> 答：对于一个订单而言，OnOrderEvent()只会推送订单的开始状态（未成交），或者终止状态（全部成交、部分撤单、已撤单、已拒绝），部分成交的时候不会推送，部成状态需要用户根据成交回报OnTradeEvent()来确定。


**15.问：调用查询接口，消息返回时，数据是按批推送过来的么？**


> 答：所有查询数据都是按个推送的，每次推送一个，即当查询结果有N个数据时，会回调N次接口，当最后一个数据推送时，会设置参数is_last为true。


**16.问：为什么我没有做过撤单操作，没有调用CancelOrder接口，可是最后订单被撤了？**


> 答：当发生这种情况时，先确认没有其他人使用与你同样的account登录并操作。XTP平台支持同一account以不同的client_id登录，如果多人同时登录，可能会互相撤单。


**17.问：调用InsertOrder()后，返回的order_xtp_id是唯一的么？**


> 答：在同一交易日内，保证唯一。所有数据均当日有效，不保证不同交易日唯一。


**18.问：XTPTradeReport成交回报有唯一标识么？**


> 答：对于单个账户来说，上交所可以使用成交序号 report_index 来唯一区分，深交所可以使用成交编号 exec_id 来唯一区分。对于多账号来说，martket + exec_id + side 组合起来区分，唯一标识一笔成交。


**19.问：如何检查自成交？**


> 答：对于上交所，exec_id可以唯一标识一笔成交。当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交了。对于深交所，exec_id是唯一的，暂时无此判断机制。


**20.问：在断线后，login()之前，调用登出logout()和不调用有何区别？**


> 答：如果不登出就login()，公共流订阅方式不会起作用。用户只会收到断线后的所有消息。如果先logout()再login()，那么公共流订阅方式会起作用，用户收到的数据会根据选择的RESTART/QUICK而定。

**21.问：用户重新login()登录行情服务器后，需要重新订阅么？**


> 答：如果是2.2.33.5以下版本的api，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情。如果是2.2.33.5及以上版本的api，OnDisconnected()回调函数被触发时，其实只是表明TCP连接的断连，不会影响UDP组播接收行情数据，因此可根据实际情况来决定是否需要建立TCP的重连。如果在断连后没有查询行情静态数据的需求，此时可以不用建立TCP重连。


**22.问：下单结构体XTPOrderInsertInfo中的order_client_id有什么作用？**


> 答：order_client_id为用户自定义字段，用户下单时输入什么值，订单响应OnOrderEvent()返回时就会带回什么值，类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。合理的规划好order_client_id，将有助于用户更快定位订单。


**23.问：股票代码ticker字段有什么要求？**


> 答：ticker中要以’\0’结尾，并且不能带任何空格。


**24.问：订单响应结构体XTPOrderInfo中的qty_left数量，为什么在撤单成功时不显示为0？**


> 答：qty_left在订单为未成交、部成、全成、废单状态时，表示此订单还没有成交的数量，在部撤、全撤状态时，表示此订单被撤的数量。


**25.问：为何没有撤单成功响应函数？**


> 答：对于撤单成功，OnOrderEvent()会响应，返回原订单的状态变成部撤或者全撤，所以没有提供单独的撤单成功响应。只有撤单失败时，OnCancelOrderError()会响应并返回撤单失败的原因。


**26.问：GetAccountByXTPID()只能在登录之后调用么？**


> 答：是的，只能在account登录后才能得到正确的结果。


**27.问：GetClientIDByXTPID()有何作用？**


> 答：当多个客户端用同一个account登录时，可以通过此函数得到是哪个client_id的客户端下的单，并据此过滤出自己的订单。


**28.问：一个api里，调用多次login函数登录多个账户，下单的时候就根据session_id来区分单子下到哪个账户里，但是收到成交回报之后，怎么区分是哪个账号的成交回报呢？**


> 答：回调函数中增加了session_id参数可帮助用户进行区分，也可以通过GetAccountByXTPID()来获取此订单对应的账号，但是建议用order_client_id来区分，规划好order_client_id会更方便快捷。


**29.问：为何撤单失败提示错误，找不到原单？**


> 答：请检查撤单时CancelOrder()传入的order_xtp_id是否正确，是否uint64_t位的，请确保传入的order_xtp_id与下单时返回的order_xtp_id是一致的。


**30.问：为何有的时候下单后被拒，成为废单？**


> 答：请先根据拒单原因检查一下订单，可以按如下项进行检查：
> 1. 买入普通股票时，请检查报单数量，单笔申报数量是否为100的整数倍，卖出时，可卖持仓数量不足100股的部分，应该一次性委托卖出。
> 2. 普通股票单笔报单最大数量是否超过了100 万股。债券交易和逆回购单笔报单是否超过了10万 手。
> 3. 买入科创板股票时，请检查报单数量，单笔申报数量是否小于200股。限价买卖科创板股票，是否超过了10万股；市价买卖科创板股票，是否超过了5万股。卖出时，可卖持仓数量不足200股的部分，应当一次性委托卖出。
> 4. 卖出报单的数量，不能超过可卖持仓 sellable_qty。
> 5. 限价单的话，价格是否超过涨跌停价格。
> 6. price_type 价格类型是否正确，是否是交易所允许的价格类型。
> 7. ticker 股票代码是否正确，是否跟交易所类型匹配。
> 8. market 交易所类型是否正确，XTP_MKT_SZ_A = 1 是 深圳A股， XTP_MKT_SH_A = 2 是 上海A股。
> 9. business_type 是否设置正确，注意：信用账号对应的两融业务填XTP_BUSINESS_TYPE_MARGIN。
> 10. position_effect 是否设置正确，该字段仅期权交易中有效，在普通现货和两融交易中都填 0。
> 11. 是否下单数量过多，触发了风控。
> 12. 是否撤单过多，触发了风控。
> 13. 是否在允许报单时间内。
> 如果以上都不是，请看一下是否是模拟撮合环境，如果是模拟撮合环境，会有一定几率发生模拟交易所拒单。此时交易所拒单的error_code是11110000，或者11100000，error_msg通常为217或者10000或者29999。这是模拟拒单，方便您测试拒单情况，不代表您的报单有错误。


**31.问：在订单部分成交时，如何获取该笔订单的剩余未成交数量？**


> 答：订单部分成交时不会推送OnOrderEvent()，只会推送OnTradeEvent()，可通过查询该笔报单QueryOrdersEx()，或者查询未完结报单QueryUnfinishedOrdersEx()来获取 剩余数量 XTPOrderInfoEx.qty_left，成交数量 XTPOrderInfoEx.qty_traded，以及此订单的报单数量 XTPOrderInfoEx.quantity。


**32.问：为何成交回报OnTradeEvent中的成交数量，有的时候不是100的整数倍？**


> 答：成交回报的数量取决于卖单的数量，如果卖单不是100的整数倍，那么成交数量是有可能不是100的整数倍的。交易所只允许将零散股一次性卖出，此时可以下非100的整数倍。


**33.问：全成的订单响应OnOrderEvent会在此订单的所有成交回报OnTradeEvent之后到达么？**


> 答：我们的系统确保订单的开始状态OnOrderEvent在此订单的所有成交回报到达之前到达，同时也确保订单的结束状态OnOrderEvent在此订单的所有成交回报之后到达。


**34.问：每次login之后的session_id会变化么？**


> 答：每次重启程序时，api初始化的session_id是一样，但如果断线重连时，也就是不退出程序没有销毁api，重新login时返回的session_id会不同。请每次登录后及时更新session_id。


**35.问：在查询资金接口中，为何总资产=可用资金+预扣资金？**


> 答：总资产total_asset = 可用资金buying_power + 证券资产security_asset + 预扣资金withholding_amount，由于目前security_asset我们暂时不做统计，默认为0，因此总资产=可用资金+预扣资金。


**36.问：测试环境下，模拟撮合采取的撮合策略是怎样的？**


> 答：测试环境下，目前默认采用的轮询模式进行撮合，按照未成交、全成(单笔成交回报)、部成、废单、全成(多笔成交回报) 轮流来撮合。如果想要设置不同的撮合方式，有如下方式：
>- 如果是在官网申请的测试账号，请至XTP官网的个人中心，设置撮合模式配置。此设置约10分钟后生效。生效后在smartX客户端报单、API方式报单都按照配置的模式来撮合。
>- 如果使用API方式报单，可以直接在InsertOrder()中设置order_client_id数值来撮合。如果官网也设置了，此时API设置的优先级高于官网，即按API设置的方式来撮合。

> **新撮合版本升级后，上海和深圳统一是一套模式：**

> | 设置模式| 撮合模式 |
> | ----------|----------|
> | `auto`| 轮询（未成交、全成(单笔成交回报)、部成、废单、全成(多笔成交回报) 轮流来）|
> | `confirm` | 未成交 |
> | `reportOne` | 全部成交(单笔成交回报) |
> | `part` | 部分成交 |
> | `reject` | 拒单 |
> | `reportMore` | 全部成交(多笔成交回报) |
> | `quote` | 按当前快照盘口行情撮合 |

> **模拟撮合针对API方式下单，新增用户自定义撮合方式，利用InsertOrder时报单所填的order_client_id数值，按如下模式撮合：**

> 1-未成交、2-全成（单笔成交回报）、3-部成、4-废单、5-全成(多笔成交回报)、 6-按当前快照盘口行情撮合

> **对于6-按当前快照盘口行情撮合，目前并不是对所有股票生效，支持规则参考如下：**

> ① 上海深圳都支持：主板，科创板（包含cdr），创业板，etf买卖；

> ② 上海支持债券，深圳不支持债券；

> ③ 上海深圳都不支持：逆回购，etf申赎，配股配债，新股申购等非交易业务；

> ④ 算法账户不支持；


**37.问：实盘下调用InsertOrder()，报单频率是否有限制？**


> 答：有的，后台对报单频率有控制，如果触发oms风控会被断线。具体可参考：XTP金融风控指标文档。


**38.问：公网测试环境的可测试时间段有哪些？**


> 答：除了每日的23:30 - 00:10，8:00 - 9:00，服务器在重启或初始化，以及必要的维护时间，其余时间段，都可以测试。


**39.问：按行情模拟撮合，限价单委托买入普通股票，而且委托价格高于卖一价，为什么没有马上成交呢？**


> 答：是按照当前快照十档盘口的对手方来撮合成交，如果此时对手盘的数量不足，那您的报单就无法成交，只能等到有价有量时再次撮合才会成交，而且撮合结果不会影响行情。


**40.问：按行情模拟撮合，如果我有很多笔买入报单，委托总数量超过了对手盘的数量，是不是只成交一部分？**


> 答：是的，因为要看对手盘的数量，如果不够只会成交一部分，未成交部分等行情来了再次撮合。


**41.问：公网测试环境的订单响应速度不是那么快啊？**


> 答：公网测试环境除了网络延迟比较大之外，模拟撮合的速度也有一定的延迟，以上交所模拟撮合为例，是1秒一个周期进行轮询，如果你下单的时候正好进入下一个周期，那么最晚需要1秒才会收到订单响应。


**42.问：公网测试环境的行情数据更新频率是怎样的？**


> 答：公网测试环境行情来自于交易所的转发数据，推送频率可参考：XTP行情服务接入前指引。收盘后是推送当天的行情回放数据，节假日是推送上一个交易日的回放数据，循环推送以供测试。注意看下此时行情的数据时间data_time。


**43.问：公网测试环境上的行情数据有的时候为什么不动了？**


> 答：公网测试环境，因为带宽有限，请不要使用全市场订阅接口SubscribeAll，以免影响到公网测试环境下的行情数据的获取。当在闭市时间段内，只有静态行情，此时行情是不会变的。如果在开市时间段内，行情数据不动，请联系我们的技术人员。


**44.问：OnDisconnected()什么时候会调用？**


> 答：在服务器与客户端断线的时候会被回调。如果此时用户想要重连，则不要调用Release()，不要调用logout()，只需要在该函数中再次调用Login()，并在登录成功后更新session_id即可。在用户主动调用Logout()时不会触发OnDisconnected()。


**45.问：QuoteApi和TraderApi每次使用其接口前，先要判断下他们是否为空值吗？**


> 答：一般是重复CreateTraderApi()或者Release()销毁了API导致了NULL，如果能确保程序里只CreateTraderApi()一次，并且不调用Release()释放API，就不用每次使用接口前先判断是否为空值。


**46.问：OnError()什么时候调用？**


> 答：只有在服务器发生错误的时候才会触发OnError()。一般情况下，都不会触发。


**47.问：在公网测试环境下，为什么我无法卖出我昨日买入的持仓？**


> 答：因为公网测试环境是不做清算的，每日都会将账户初始化至最初的状态，也就是说今日买入的持仓，在到第二日后不会进入昨日持仓，所有资金和持仓数据均保持初始状态。如果是官网申请的现货测试账号，可以登录官网自行设置保留持仓。注意：保留持仓可能会失败。


**48.问：在查询持仓中股票名称ticker_name为何是乱码？**

> 答：xtp系统中股票名称ticker_name是UTF-8编码，请检查一下编码是否正确。另外，windows默认是gbk编码，直接cout输出到控制台看时中文可能是乱码，需要转换一下编码格式。


**49.问：在断线后，如何系统恢复？**


> 答：收到断线通知后，在不重启的情况下，在OnDisconnected()函数中不要调用Release()，也不调用logout()，直接调用Login()，默认就是resume方式，只会收到断线后的消息；如果是重启程序的情况下，只能通过restart方式，或者quick方式+查询（QueryOrders/QueryTrades）。


**50.问：demo程序为何一直在下单？**


> 答：demo测试程序采用的是乒乓测试下单，当收到OnOrderEvent时，会根据订单的状态来触发撤单或者新一轮下单。除了在xtp_api_demo.cpp文件中有InsertOrder的调用，在trade_spi.cpp文件的OnOrderEvent()响应函数中，也有InsertOrder的调用。如果用demo测试下单时，发觉所有订单都是拒单，请参考第36问。


**51.问：提示 [XTP:1]Login Failed,trade way not allowed,please check it! 这个错误代表什么意思？**


> 答：这个表示在调用void SetSoftwareKey(const char* key)函数时传入的key不对，请填入正确的key。此key在申请账号时会一并给出。每个账户对应的key可能不一样。


**52.问：实盘下连接Level2，Login参数传入了网段对应的local_ip，防火墙也关闭了，为何还是收不到逐笔行情数据？**

> 答：实盘下连接Level2要使用UDP连接。公网测试环境，虽然提供逐笔委托和逐笔成交行情，但是使用TCP连接。


**53.api中回调线程是自动绑核的吗？**


> 答：api没有主动绑核，TCP连接不需要绑核，如果您接收UDP行情需要绑核，请调用我们提供的绑核接口：SetUDPRecvThreadAffinityArray()、SetUDPParseThreadAffinityArray()，注意：要绑定靠后的核，如果绑定第1个核，可能因为资源竞争而导致CPU被系统占用。


**54.问：程序编译可以通过，可是运行时提示确少某些运行库，怎么办？**


> 答：请下载缺少的库，并放置到对应的位置上，下载安装必要的redist补丁包，64位系统需选择vcredist_x64.exe。


**55.问：只能在vs2015下编译运行么？**


> 答：windows系统推荐在win10，vs2015下编译运行，但不局限于此。其他版本的windows和vs可能需要安装部分补丁包和运行库。Linux版推荐ubuntu14，ubuntu16，redhat7.2。


**56.问：demo没有工程文件，请问可以提供工程文件么？**


> 答：demo里包含cmake文件，请用cmake工具，选择好需要的generator，然后生成对应的工程文件。如果generate的时候找不到对应的编译器，请确认已经安装好了Visual Studio编译器，如果安装的编译器版本比较高，可以适当升级一下cmake至匹配的版本，再重新生成工程。


**57.问：demo在release模式下编译时提示找不到对应的库文件。**


> 答：请修改cmakelist文件中optimized后面引用的lib库文件名字，改成debug的库文件。


**58.问：当全市场订阅行情时，为何一会儿就会断线？**


> 答：请按如下顺序检查您的程序：
> 1. 是否在收到行情的Spi回调函数里，能够迅速返回？请在回调函数里只接收数据，所有处理过程在另一个线程里。
> 2. 是否有屏幕输出？如果有，请减少屏幕输出，或者不输出。
> 3. 接收行情线程是否有堵塞。
> 注意：在公网测试环境下，由于带宽有限，如果用户订阅行情数过多，容易导致缓冲区满，从而造成断线，请在公网测试环境下，少订阅几只股票。


**59.问：如何订阅全市场行情？**


> 答：已提供全订阅/退订接口。如果是订阅全市场快照行情，可使用SubscribeAllMarketData()接口订阅，参数exchange_id为XTP_EXCHANGE_UNKNOWN，表示沪深全市场。


**60.问：ETF申购后，对ETF报卖单，数量也是查询持仓中的可卖持仓，为何出现错误代码为11000107的拒单？**


> 答：请检查报单数量是否超过100万股，InsertOrder()传入的quantity，交易所规定普通股票单笔下单数量不能超过100万股。


**61.问：ETF申购后，返回的成交回报中，为何有些成分股的数量为0？**


> 答：成分股成交数量为0时，表明此成分股发生现金替代，从而持仓数量没有变化。


**62.问：查询持仓时，如果账户没有持仓的话，有何返回结果？**


> 答：当没有持仓的时候，OnQueryPosition()函数中的error_info.error_id =11000350，表明没有持仓。同样的，在查询其他记录时，如果没有记录信息，在返回的SPI函数中均有error_info.error_id =11000350。


**63.问：api连接交易服务器时，报错：get_recv_frame function failed，但是api协议的头文件和库文件版本是一致的**


> 答： 如果协议是一致的，请检查Login()时参数sock_type是否误填了UDP方式？交易只能TCP方式连接。


**64.问：可以通过哪些途径知道某只股票是停盘等状态的？**


> 答：在行情marketdata数据中ticker_status字段，表示当前交易状态及标志。
> 1. 对于普通股票/基金，具体值如下：
>- 第 0 位：
>    - ‘S’，启动（开市前）时段(SH/SZ)
>    - ‘C’，集合竞价(SH/SZ)
>    - ‘T’，连续竞价(SH/SZ)
>    - ‘B’，休市（SZ）
>    - ‘E’，闭市(SH/SZ)
>    - ‘P’，产品停牌(SH/SZ)
>    - ‘M’，表示可恢复交易的熔断时段（盘中集合竞价）(SH)
>    - ‘N’，表示不可恢复交易的熔断时段（暂停交易至闭市）(SH)
>    - ‘U’，表示收盘集合竞价时段(SH)
>    - ‘D’，开盘结合竞价结束到连续竞价开始前（SH）
>    - ‘A’，盘后交易（SZ）
>    - ‘V’，波动性中断（SZ，SH期权）
>- 第 1 位：
>   - ‘0’，此产品不可正常交易
>   - ‘1’，此产品可以正常交易
>   - 无意义填空格
>- 第 2 位：
>   - ‘0’，未上市
>   - ‘1’，已上市
>- 第 3 位：
>   - ‘0’，此产品在当前时段，不接受进行新订单申报
>   - ‘1’，此产品在当前时段，可接受进行新订单申报
>   - 无意义填空格


> 深交所只有第0、1位，没有第2、3位


> | 上海市场 | 0-9:15 | 9:15-9:25 | 9:25-9:30 | 9:30-11:30 | 11:30-13:00 | 13:00-14:57 | 14:57-15:00 | 15:00-   |
> | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
> | 非停牌 | S 11 | C111 | T111 | T111 | T111 | T111 | U111 | E111 |
> | 停牌 | P011 | P011 | P011 | P011 | P011 | P011 | P011 | P011 |

> 注意：从2018-12月份开始，上交所停止发送开盘集合竞价消息（UA3107）。开盘/收盘集合竞价消息，直接从UA3202发出。


> | 深圳市场 | 0-9:15 | 9:15-9:25 | 9:25-9:30 | 9:30-11:30 | 11:30-13:00 | 13:00-14:57 | 14:57-15:00 | 15:00-  |
> | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
> | 非停牌 | S1 | C1 | B1 | T1 | B1 | T1 | C1 | E1 |
> | 停牌 | S0 | C0 | B0 | T0 | B0 | T0 | C0 | E0 |


>2. 对于债券，标志含义同股票/基金字段说明，具体如下：
>- 上交所
>    -  从2021.10.25后，上交所启用新的债券交易系统，修改了债券行情的协议。
>    - 上交所L1时，ticker_status有值；
>    - 上交所L2时，ticker_status无意义；参见bond.instrument_status；
>- 深交所
>    - 深交所L1和L2，ticker_status有值；

>3. 对于期权，具体值如下：
>- 上交所标志含义
>  - 第 0 位：
>    - ‘S’，启动（开市前）阶段
>    - ‘C’，集合竞价
>    - ‘T’，连续交易
>    - ‘B’，休市
>    - ‘E’，闭市
>    - ‘V’，波动性中断
>    - ‘P’，临时停牌
>    - ‘U’，收盘集合竞价
>    - ‘M’，可恢复交易的熔断（盘中集合竞价）
>    - ‘N’，不可恢复交易的熔断（暂停交易至闭市）
>  - 第 1 位：
>     - ‘0’，未连续停牌
>     - ‘1’，连续停牌
>     - 预留则填空格
>   - 第 2 位：
>     - ‘0’，不限制开仓
>     - ‘1’，限制备兑开仓
>     - ‘2’，卖出开仓
>     - ‘3’，限制卖出开仓、备兑开仓
>     - ‘4’，限制买入开仓
>     - ‘5’，限制买入开仓、备兑开仓
>     - ‘6’，限制买入开仓、卖出开仓
>     - ‘7’，限制买入开仓、卖出开仓、备兑开仓
>  - 第 3 位：
>     - ‘0’，此产品在当前时段不接受进行新订单申报
>     - ‘1’，此产品在当前时段可接受进行新订单申报
>- 深交所标志含义，同股票/基金字段说明。


**65.问：在行情marketdata数据中，instrument_status 和ticker_status字段的区别？**


> 答：上交所新债券 Level2 行情快照中，XTPMD.ticker_status 不再有意义，请使用 XTPMD.bond.instrument_status 替代判断当前债券所处的交易状态。其他快照行情还是使用ticker_status判断交易状态。


**66.问：xtp结构体中有很多时间，哪些时间是交易所时间，哪些是xtp本地时间？**


> 答：交易中，撤销时间cancel_time、成交时间trade_time是交易所时间。委托时间insert_time、更新时间update_time是xtp本地时间。行情中的data_time都是交易所时间。


**67.问：报单数量XTPOrderInfo.quantity允许非100的整倍数么？**

> 答：（1）如果是买单，普通股票是不允许的。普通股票报单数量必须是100的整数倍，但如果是科创板，报单数量最低200股，1股起加即可。
（2）如果是卖单，要看可卖持仓 XTPQueryStkPositionRsp.sellable_qty，当可卖持仓的剩余数量有零散股时，是允许的，此时要将零散股一次性报出。普通股票，不足100股为零散股，科创板股票，不足200股为零散股。
     例如：A股票有可卖持仓232股报单卖出：  
     如果是普通股票，卖出后剩余数量是非零散股就行。可卖持仓232股，则可以卖出32股，也可以卖出132股，或者一笔报单卖出232股。  
     如果是科创板股票，只有当剩余数量小于200股时，才能一次性委托卖出零散股。当可卖持仓232股时，不能委托卖出32股或132股，但是可以200、32两笔报单卖出，或者201、31两笔报单，或者202、30两笔报单。。。等等。当可卖持仓132股时，只能一笔报单卖出132股。


**68.问：公网测试环境中，订阅行情为何总是断线？**


> 答：由于公网测试环境带宽有限，所有用户共用2MB带宽，当有用户订阅的股票数目比较多时，会造成网路堵塞，不光影响自己，也影响他人，会造成频繁断线。请在公网测试环境中订阅比较少的数量来进行连通性测试。


**69.问：xtp支持哪几种语言接口？**


> 答：目前xtp支持的语言接口包括：
> 1. C++（xtp官网可下 https://xtp.zts.com.cn/service/download）
> 2. Python（https://github.com/ztsec/xtp_api_python）
> 3. Java（https://github.com/ztsec/xtp_api_java）
> 以下为热心用户封装
> 4. C#
> https://github.com/zerochocobo/XTP.NET
> https://github.com/rongyuhuang/XTP.NET
> 5. Go （https://github.com/leochan007/XTP.GO）
> 6. WebSocket （https://github.com/MuggleWei/babel-trader）


**70.问：Python接口中，有接入说明么？**


> 答：请参阅接口调用的两个示例文件：quotetest.py、tradertest.py，官网下载地址：https://github.com/ztsec/xtp_api_python/tree/master/test。
      具体请参阅C++版本.h头文件中的接口注释说明，Python里接口首字母小写（而C++是大写），其他都一样。


**71.问：登录失败，提示"Login Failed,get user identity failed,used client_id number exceeded."是何原因？**


> 答：这是因为您使用的client_id数量过多导致，请将client_id固定下来使用，（建议1~99内），我们对client_id的总共使用个数做了限制，超过最大使用个数就不让登录了。


**72.问：xtp推荐的运行环境是多少？**


> 答：推荐系统windows 10、redhat7、ubuntu16、centos7。


**73.问：quote日志中有“service function is not exists(2040)”这个warning语句是何意？**


> 答：这个warning是因为新版本的api接口新增了部分协议，而用户程序使用的低版本api的库无法解析这些数据。
     比如：api版本为2.2.39.2的QuoteSpi新增了OnETFIOPVData()，当用户程序api是2.2.38.1版本，并且订阅了ETF快照时，就会有该warning日志。如果需要这部分数据，建议升级api版本，否则，可以忽略该warning。


**74.问：为什么设置了正确的日志路径，trade.log却没有生成日志文件？**


> 答：如果日志级别设置得太高，在没有出现该级别的错误时，就不会生成日志文件。调试期间建议设置为 XTP_LOG_LEVEL_DEBUG 或 XTP_LOG_LEVEL_INFO，等调试顺畅了再调高日志级别。


**75.问：为什么账号开通XTP之后，登录SmartX客户端一直提示“The password is incorrect”，而用融易汇相同的密码却能登录？**


> 答：请检查账户的操作权限，是否开通了SmartX客户端的权限，如果没有开通，也会一直提示密码错误。


**76.问：如果某只股票发生配股，需要配股的话，如何操作？**


> 答：先查询持仓，并根据OnQueryPosition返回的position_security_type过滤出配售类型的持仓，包含配股、配债等。其中：
> （1）yesterday_position 表示总可配股数量
> （2）sellable_qty 表示剩余可配股数量
> （3）total_qty 表示已配股数量
> 假如股票A可配股票B 1000股，则持仓中股票B初始数量为：yesterday_position = 1000，sellable_qty=1000，total_qty=0；
报单操作配股200股后，则查询持仓中股票B数量为：yesterday_position = 1000，sellable_qty=800，total_qty=200。


**77.问：新股申购如何操作？**


> 答：今日可申购新股信息，可调用QueryIPOInfoList()查询最大允许申购数量，调用QueryIPOQuotaInfo()查询可申购额度，那么所能申购的最大数量为：min（新股可申购额度，最大允许申购数量）。


**78.问：为什么我调用某些API接口函数时，没有期望的spi接口函数被回调？**


> 答：请检查头文件和库文件版本是否一致，如果不一致，请将所有的头文件和库文件一起更新，然后重新编译再运行，最好将本地其他版本的库文件都清理掉。GetApiVersion()可以获取api版本号，也可以查看头文件和库文件的修改日期是否一致来判断。


**79.问：担保品划转会返回OnTradeEvent()吗？sellable_qty是实时扣减么？**


> 答：担保品划转不会返回OnTradeEvent()。对于担保品转出，当收到OnOrderEvent()订单确认消息，可卖持仓sellable_qty会实时扣减转出数量。对于担保品转入，当收到OnOrderEvent()订单确认消息时，可用持仓不会实时增加。盘中划转委托只是报送到交易所，没有报错即可，是否成功以晚间清算后的结果为准。注意：如果晚间清算时持仓数量不足，整条划转委托会拒单。

**80.问：会发生InsertOrder()接口还没返回，但是先收到OnOrderEvent()返回的订单确认状态的情况么？**


> 答：可能会发生这种情况，而且调用InsertOrder()接口的线程被挂起时，也会晚于订单确认消息返回。用户需注意收到不存在的订单时，先缓存起来不要丢弃。


**81.问：我们遇到在InsertOrder()返回之前就收到了OnOrderEvent()消息，导致没法将内部order_id和order_xtp_id关联起来，请问如何处理？**

> 答：如果InsertOrder()晚于OnOrderEvent返回导致没法关联内部订单，可以使用 GetANewOrderXTPID() + InsertOrderExtra()组合来报单，即先调用GetANewOrderXTPID()提前获取一批实际需要
  的order_xtp_id，再调用InsertOrderExtra()进行报单，注意：如果order_xtp_id设置得不对，会导致报单失败，如果不按顺序使用order_xtp_id，在断线重连的时候可能会丢数据。


**82.问：普通户的股票需要转到信用户，是怎么操作呢？**

> 答：登录信用账户，调用InsertOrder()做担保品转入，business_type 填 XTP_BUSINESS_TYPE_MARGIN，side 填 XTP_SIDE_GRTSTK_TRANSIN。
    从普通户划转到信用户，当天买入的持仓，可以担保品转入。
    从信用户划转到普通户，当日买入的持仓，可以担保品转出，转出时优先扣减昨仓，再扣减今仓，并且维持担保比例超过300%以上的部分才可以转出。


**83.问：担保品划转可以撤销吗？**

> 答：可以撤销，在信用账户调用CancelOrder()发撤单请求。


**84.问：为什么订阅了行情只收到一条行情信息**


> 答：请检查Login()的参数sock_type连接方式是否和服务器一致，目前测试环境的服务器是TCP连接，实盘level2服务器一般是UDP连接。同时请确认防火墙要关闭。


**85.问：QueryAsset()查询资金，上海和深圳的资金是分开的还是合在一起的？**


> 答：如果没有开通一账户两中心，沪深的资金是合在一起的；如果开通了一账户两中心，沪深的资金是分开的。假如在上海节点查询资金，只有上海的资金是准确的，深圳的资金是盘前的初始资金，同理深圳也一样。


**86.问：开通两中心的账号，在当前交易节点如何查询另一个节点的实时资金及授信额度？**


> 答：可调用 QueryOtherServerFund()查询，查询类型 query_type 包括：查询金证主柜台的可转资金（不是可取资金）、双中心账号的对方节点的可用资金、对方节点的融券卖出余额资金、对方节点的授信额度。

**87.问：资金划拨操作是调用哪个API接口？**


> 答：使用FundTransfer()接口请求资金划拨，资金流转方向参见 transfer_type 字段，一账户两中心节点之间的资金划拨，需注意资金划拨的方向，另外，XTP和主柜台之间的资金划拨要使用交易密码。


**88.问：XTPFundTransferNotice中的serial_id，就是调用FundTransfer()函数的返回值吗？**

> 答：是的，serial_id数据类型是uint64_t，注意数据类型要保持一致。


**89.问：资金划拨类型是跨节点转入/转出，那另一个节点也会收到OnFundTransfer()划拨通知吗？？**


> 答：另一个节点也能收到资金划拨消息OnFundTransfer()，但是订单响应、成交回报这些消息，另外的节点都收不到。


**90.问：InsertOrder()下单被拒，错误提示：11000311，User is not allowed to trade in this market!**


> 答：通常为一账号两中心未在对应节点交易对应市场的证券，比如：登录的深圳节点，却报单了沪市的股票，就会拒单。请检查一下连接的交易服务器地址、报单的股票。


**91.问：程序登录失败，显示：**
```
{'error_id': 1, 'error_msg': '[XTP:1]read_ptr function failed.(remain_bytes  答：首先请检查一下账号和密码、服务器IP和Port是否正确，包括行情账户和交易账户，如果都配置正确请再检查一下是否上一次登录的程序未完全退出。如果都没有问题可以临时更改一下client_ id进行登录。

**92.问：登录交易服务器，错误提示：**
```
[XTP:1]user doesn't exist.[OS:106]Transport endpoint is already connected
```
>答：用户名是否输错？比如多了空格之类的符号；用户登录节点是否错误？ 请参见账号对应的服务器IP、Port；实盘客户是否还没有完全开户进xtp？此时需联系运维人员确认账户。


**93.问：linux系统下编译github上的Java版本，需要的库已经放到了系统目录/usr/local/lib/，文件的执行权限也有的，但还报错找不到 libquoteplugin.so、libglog.so。**
```
Exception in thread "main" java.lang.UnsatisfiedLinkError: /usr/local/lib/libquoteplugin.so: libglog.so.0: cannot open shared object file: No such file or directory
    at java.lang.ClassLoader$NativeLibrary.load(Native Method)
    at java.lang.ClassLoader.loadLibrary0(ClassLoader.java:1941)
    at java.lang.ClassLoader.loadLibrary(ClassLoader.java:1824)
    at java.lang.Runtime.load0(Runtime.java:809)
    at java.lang.System.load(System.java:1086)
    at com.zts.xtp.common.jni.JNILoadLibrary.loadLibrary(JNILoadLibrary.java:75)
    at com.zts.xtp.common.jni.JNILoadLibrary.loadLibrary(JNILoadLibrary.java:10)
    at com.etcm.st.EtstServer.(EtstServer.java:40)
```
>答：linux下执行命令：ldd /usr/local/lib/libquoteplugin.so 看下是否缺少库以及依赖的其它库文件。
     如果不缺库文件，那就再设置动态库加载目录，执行命令：export LD_LIBRARY_PATH=/usr/local/lib:$。
     windows下可使用工具dependenciesGUI.exe检查所缺的库文件及其依赖项。


**94.问：下载的github上的Java版本，编译通过，但是运行报错，是什么原因？**
> ![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2056206187128475650&imagePath=94Q-1.png)

> 答：如果使用我们提供的库，那得用官网的glog，libglog.so要放到系统目录，如果是windows系统，要把glog.dll、glog.lib 放到系统目录下C:\Windows\System32\。也可以自己编译 dependsLibSrc目录下的 gflags-master 和 glog-master 源码中的glog。


**95.问：为什么下载的java中的demo编译不了，有很多builder方法没有定义**

> ![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2056206187128475650&imagePath=95Q-1.png)

> 答：java为了减少写代码的工作量，引入了builder模式。需要安装Lombok插件。


**96.问：报单深圳市场的股票，错误提示：error=11100055,Tgw of the pbu id not found，是什么原因？**


> 答：如果是实盘，这个是账户设置问题，分配的服务器没有配置指定的tgw，需要联系营业部检查账户开户设置的情况。如果是测试环境，请确认报单的证券代码和市场是否正确。


**97.问：报单可转债，当price_type填市价单时，报错：新订单的价格类型参数无效，是什么原因呢？**


> 答：可转债不支持市价单，price_type 只能为 XTP_PRICE_LIMIT。


**98.问：下单时返回0，然后使用GetApiLastError又没有错误信息描述，error_id为0，error_msg为空，怎么排查这个问题呢？**


> 答：请检查下单的参数是否有误，如session id ....
      如果最近有升级api版本，请检查一下使用的头文件和库文件的版本是否一致。可直接替换头文件和库文件，重新编译一下再运行。


**99.问：测试环境下，我api方式订阅快照，OnSubMarketData()返回：ErrorId=11210100. ErrorMsg=tickers or sessions used up，这是什么原因呢？**

> 答：您订阅的数量超限了，因为公网环境下带宽有限，而且是TCP连接，订阅太多时会造成网路堵塞，所以我们做了订阅数量限制，单订阅接口单市场上限是100只，沪深2个市场总共200只。


**100.问：InsertOrder()报单沪市股票时报错：Failed to get ticker quotes,ticker does not exist or can not be traded!**


> 答：请检查一下证券代码是否正确，如果无误请检查一下交易市场是否正确。行情api和交易api使用的是不同的市场类型，如果都没问题请确认一下是不是XTP不支持的品种。
> ![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2056206187128475650&imagePath=100A-1.png)


**101.问：在下单的时候，在接收回调函数报单通知时，会不会保证按照正常的订单生命周期对应的时间顺序；举个例子，全成会在部成后面出现，而不会是部成在全成后面出现。**


> 答：一般都是按时间顺序推送，同时api对消息也会保序，保序时间大概在3~5秒内，比如：一笔订单部成后发起撤单，撤单响应和成交回报消息在3秒内先后到达，api就会保序为先收到OnTradeEvent，再收到OnOrderEvent。另外，部成不推送报单通知消息。


**102.问：买一卖一队列的有效委托笔数和总委托笔数有什么区别呢？**


> 答：总委托笔数是市场里的委托笔数，而有效委托笔数是系统揭示的委托笔数，xtp中买一卖一队列最多提供50笔数据，如果max_bid1_count >= 50，则bid1_count = 50，如果max_bid1_count  答：cancel_time是交易所撤单时间。


**104.问：CreateQuoteApi 和CreateTraderApi直接返回NULL是什么原因？**


> 答：请检查是否创建了过多的api对象，2.2.33.5及以上版本的SDK，行情可以创建多个QuoteApi，但是交易只能创建1个TraderApi；如果数量没有超过限制请检查输入参数是否有误，client_id要用正整数；还有一个可能的原因是库文件和头文件的版本不一致。


**105. 问：OnQueryOrderByPage接口返回的记录中包含报单和撤单委托，怎么能方便的把报单和撤单委托区分出来？**


>答：根据order_submit_status字段来区分，枚举值前三个是报单，后面三个是撤单。
```
///@brief XTP_ORDER_SUBMIT_STATUS_TYPE是报单提交状态类型
typedef enum XTP_ORDER_SUBMIT_STATUS_TYPE
{
    XTP_ORDER_SUBMIT_STATUS_INSERT_SUBMITTED = 1, /// 答：测试环境没有orderbook，只有快照数据和逐笔数据。


**107.问：SetSoftwareKey，软件开发Key，能否申购多个测试账号时是同一KEY？**


> 答：这个key是按渠道来的，多个测试账号开通了同一个渠道，那么key就是同一个。


**107.问：现货账号同时订阅 SubscribeAllMarketData，SubscribeAllOptionMarketData，这种情况下，也是一个组播组吧？**


> 答：是一个组播组，快照都在一个组播组，不区分哪个品种的快照。


**109.问：集合竞价期间有orderbook数据吗？**


> 答：集合竞价期间没有orderbook，要到开盘以后9:30才有orderbook。


**110.问：如果一只股票在盘中停牌了, 那已有orderbook会如何更新呢？**


> 答：停盘期间不会推送新的逐笔数据，此时orderbook数据也不会更新。


**111.问：xtp有没有那种正常的仿真交易环境？就是类似simnow那种的**


> 答：XTP的现货和两融测试账户可以设置保留持仓，类似于simnow。


**112.问：登录行情时报错，错误信息：Login failed. [code = 1, error = [XTP:1]connect server failed.[OS:115]Operation now in progress] 可能是什么原因导致的呢？**


>答：connect server failed 是与服务器不连通，如果服务器已开启，能否ping通服务器地址？ 服务器ip和port是否输错？ local_ip是否输错？ 防火墙是否关闭？


**113.问：XXXXXXX login failed, errorMsg=[XTP:1]Login Failed, get user info failed,please check if user info is perfect.[OS:106]Transport endpoint is already connect**


> 答：测试环境下，可能是服务器还没启动好。实盘环境下，可能是账户在半开通状态，请联系营业部确认开通xtp权限的流程是否没有完成。


**114.问：[XTP:1]Login Failed,trade key invalid or not set,set assigned key first!**


> 答：请检查是否在Login()之前调用了SetSoftwareKey()并设置了account_key，如果已设置，请确认account_key是否正确。


**115.问：OnDepthMarketData和OnTickByTick，是深圳和上海各一个线程，还是两个市场共用一个线程？**


> 答：跟市场无关，跟是否在一个组播组有关。OnDepthMarketData在使用UDP的时候可能是两个线程，通常对于一只股票来说，第一个行情快照是TCP线程，后续的都是UDP线程。看下连接的行情地址，如果快照和逐笔是在不同的组播组，那么就是在不同的UDP线程。


**116.问：xtp中进行逆回购时，side = XTP_SIDE_SELL，那正回购填哪个值呢？**


> 答：xtp中不支持正回购，支持的买卖方向参见 XTP_SIDE_TYPE 列出的枚举值。


**117.问：进行ETF申赎时，在休市期间撤单报错返回OnCancelOrderError()，为什么呢？**


> 答：xtp系统不再支持在休市期间对ETF申赎撤单。


**118.问：ETF申购赎回，返回11000010(Failed to get ticker quotes,ticker does not exist or cannot be traded!)** 


> 答：请检查一下ETF代码，xtp统一使用二级市场证券代码申购赎回和交易。


**119.问： ETF申赎的成交记录中，一级市场和二级市场代码都有吗？**


> 答：没有一级市场代码，OnTradeEvent()成交回报中 ETF申赎代码和资金代码 统一为ETF的二级市场买卖代码。成交类型可通过XTPTradeReport.trade_type来区分。


**120.问：沪市ETF申赎，多码合一后，交易所推送的成交回报OnTradeEvent()有什么变化？**


> 答：ETF申赎同一个市场，资金替代只会有一条资金成交回报。成份股中成交数量为0的成交记录，现金替代金额为0的成交记录，成交回报中不再推送。
     对于跨沪港深ETF申赎成交的回报记录，新的多码合一后，现金替代成交记录可能会有本市场资金成交（沪市资金）、跨市场资金成交（深市资金）、港市资金成交，最多有三条成交记录，最少可能0条记录。

**121.问：哪些测试环境可以做ETF申购赎回？**


> 答：仅普通现货测试环境支持ETF申赎。信用账户和期权账户都不支持。


**122.问：测试环境支持期权的锁定和解锁、备兑开仓和备兑平仓吗？**


> 答：不支持，目前期权不支持 锁定解锁、备兑业务。


**123.问：测试环境可以进行资金划拨操作测试吗？**


> 答：不可以，资金划拨需要开启金证kesb环境，目前测试环境没有开启，所以不支持资金划拨测试。


**124.问：如何获取撤单的数量？**


> 答：撤单成功后，原单会收到OnOrderEvent()消息，报单状态为部分撤单或已撤单，此消息中的qty_left就代表撤单数量。


**125.问：SetHeartBeatInterval()设置心跳是通过TCP发送的吗？在OnDisconnected()中重新登录之前需要再次设置心跳间隔么**


> 答：是通过TCP发送的，断线重连不需要再次设置心跳间隔。


**126.问：沪深ETF，债券和股票，都可以报单fak和fok价格类型吗？**


> 答：部分证券类型支持fak和fok，具体请参考price_type对应枚举值的注释。


**127.问：如何理解价格类型里面的注释**

> 答：只有标注了期权的才可用于期权下单，没有标注期权的只能普通股票适用。如果标注了沪深，则沪深两市股票都可用。如果仅标注了沪，则沪市股票可用，深市股票不可用。
```
///@brief XTP_PRICE_TYPE是价格类型
typedef enum XTP_PRICE_TYPE
{
  XTP_PRICE_LIMIT = 1,           /// 答：仅沪市股票，深市期权可用。


**129.问：现货账户申赎沪市交易型货币基金ETF，为何报错 11000306, error_msg =  Service not supported？**


> 答：现货账户可申赎的ETF不包括交易型货币基金，您可以先调用QueryETF()来查询可申赎的ETF清单，再根据返回的ETF代码来报单ETF申赎。


**130.问：信用账户报单ETF申赎时，为何报错 11000308, error_msg =  Business type not match with security type？**


> 答：信用账户不支持ETF申赎，但是可以买卖沪市交易型货币基金。名单公告请参见：https://www.zts.com.cn/hqzx/infoDetail.aspx?doc_id=d6%2fPCP7A4ZB7h4xoDJ%2fnjg%3d%3d。


**131.问：使用UDP接收行情时，设置接收行情线程绑定的cpu，这个是逻辑CPU还是物理CPU呢？**


> 答：这个是逻辑CPU。xtp提供的绑定CPU接口是核绑定，但不是核隔离。


**132.问：模拟环境中的股票状态和实盘是一致的吗？**


> 答：模拟环境的行情中ticker_status跟实盘一致，只是模拟环境中停牌的股票也可以交易测试。


**133.问：指定行情数据使用CPU后，行情数据处理的那个核会很忙，如果不指定，就每个核比较平均，是否可以指定2个CPU呢？**


> 答：只能指定一个CPU。


**134.问：为什么行情期权数据没有找到行权价和到期日？**


> 答：请使用QueryOptionAuctionInfo()查询，exercise_price为行权价，exercise_end_date为结束日期。


**135.问：可以同时在xtp系统和普通柜台交易吗？在xtp系统调用QueryTrades()只能返回当天的成交记录吗**


> 答：不能，开通xtp实盘后，只能使用smartX客户端或程序SDK交易，不能在普通柜台委托交易。XTP中QueryTrades()只能查询当天的成交记录，如果要查询历史成交记录，需登录普通柜台查询。


**136.问：使用SubscribeMarketData()接口能一次性订阅沪深两市的股票吗？**


> 答： 不能，只能一次性订阅同一证券交易所的多个合约，如果要订阅沪深两市的合约，那就要分2个交易所类型调用两次。


**137.问：行情数据里面的时间是哪里的时间呢？**


> 答：行情数据里的data_time时间都是交易所时间。


**138.问：上海和深圳机房的时间是PTP同步还是NTP同步的？**


> 答：windows下是使用NTP对时服务，linux下是使用chrony对时服务，如果需要使用机房内的时钟源，具体请查阅运维给的参数文档。


**139.问：实盘环境，可调用QueryPosition()和QueryAsset()查询持仓和资金的时间段是？**


> 答：在交易日8:45-17:00都可以查询。实盘服务器一般在8:45左右开启，最晚不会超过9:15，在17点关闭。


**140.问：XTP_BUSINESS_TYPE_OPTION 业务类型，可以交易个股期权吗？**


> 答：不支持个股期权，目前只能交易上证50ETF期权、沪深300ETF期权、深证100ETF期权、深交所创业板ETF（代码159915）、深交所中证500ETF（代码159922）、上交所中证500ETF（代码510500）、深证100ETF期权（159901）。


**141.问：XTP的接口函数是线程安全的吗？多线程报单要加锁吗？**


> 答：XTP中与网络通讯有关的接口都是线程安全的，如果多线程调用InsertOrder，不需要加锁。


**142.问：在vs2019里面编译xtp的demo，为什么会错误提示：**
```
LNK2019 无法解析的外部符号 public: static class XTP::API::TraderApi * __cdecl XTP::API::TraderApi::CreateTraderApi(unsigned char,char const *,enum XTP_LOG_LEVEL)" (?CreateTraderApi@TraderApi@API@XTP@@SAPAV123@EPBDW4XTP_LOG_LEVEL@@@Z)，该符号在函数 _main 中被引用
```

> 答：请检查一下是否包含了相应的头文件，是否链接了相应的库文件，如果都没有问题请检查一下编译选项是否为x64。另外，建议参考文档来使用Cmake生成工程。


**143.问：为什么执行java sdk单元测试的时候，执行第n次insert测试时，前面n-1次测试的所有log都会盖上当前时间戳重新打印一次啊？结果就是我每天执行测试的时候，每一次测试log越来越多。**


> 答：请检查SubscribePublicTopic()参数resume_type是否使用的XTP_TERT_RESTART，可改为quick方式登录只收到登录后的一系列公有流消息。

> ![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2056206187128475650&imagePath=143A-1.png)


**144.问：两融仿真测试，所有交易委托订单都被拒绝： error_info=&get;error_id:11000909, error_msg:Order is invalid in current debt expire status! 这是什么原因？**


> 答：存在逾期两融负债合约而禁止当前委托，需要先还清负债。


**145.问：程序运行时提示缺少dll文件是怎么回事？**

> ![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2056206187128475650&imagePath=145Q-1.png)

> 答：这是运行环境缺少必要的库文件，请下载64位运行时库 vcredist_x64.exe，解压后放到程序所在目录。


**146.问：xtp的Spi里面的回调，是多线程执行还是单线程的？**


> 答：TraderSpi中查询的回调都是一个线程，OnOrderEvent() 和 OnTradeEvent() 这些可能会存在两个线程；QuoteSpi中，TCP连接是一个线程，UDP连接会有两个线程。


**147.问：TradeSpi中，查询响应、OnOrderEvent和OnTradeEvent，使用的是同一个线程吗？**


> 答：不一定，查询响应和通知推送，通常是同一个线程，但是，一些超时消息是通过超时线程推送的。例如：您报单后，报单A的订单响应和成交回报没有收到，您退出了登录。过了一段时间，您使用quick方式重新登录服务器，此时如果报单A的全成消息正好回来，那么这条全成消息就会通过超时线程推送给您。


**148.问：TradeSpi中，可能会被两个线程回调的函数有哪些？**


> 答：会有超时线程的4个回调函数：OnOrderEvent()、OnTradeEvent()、OnOptionCombinedOrderEvent()、OnOptionCombinedTradeEvent()。


**149.问：QuoteSpi回调线程有几个？**


> 答：TCP连接是一个线程；UDP连接，如果Level2服务器是单路组播，则一个TCP线程，一个UDP线程，如果L2服务器是多路组播，则一个TCP线程，多个UDP线程（快照UDP线程，逐笔UDP线程，订单簿UDP线程）。


**150.问：盘中在xtp系统调用QueryPosition()返回的持仓，为何跟融易汇里看到的持仓不一致？**


> 答：融易汇里的持仓不是实时更新的，xtp里的持仓需要在T日清算后才同步到融易汇中。


**151.问：对于xtp下单的新股申购，是在XTP柜台缴款，还是在普通柜台缴款？**


> 答：新股申购中签后，确保XTP账户或融易汇中留有足够的新股认购资金即可。


**152.问： XTP的行情日志占用比较大的存储空间。需要定期手动清理吗？还是XTP会自动删除过期的日志？**


> 答：在权限允许的情况下，xtp会自动删除7天前的日志，不过建议您监控好硬盘存储空间。


**153.问：撤单失败是什么原因导致的呢？**
```
  OnCancelOrderError Error.[order_xtp_id:1140851691,order_cancel_xtp_id:1140853695,session_id:572522497,error_code:11000305,error_msg:Failed to find original order!]
```
> 答：这个错误是查找原始报单失败，是否撤单时order_xtp_id填错了？注意 order_xtp_id数据类型是uint64_t。


**154.问：XTP API有接口查询新股中签情况吗？**

> 答：没有，XTP中查不到中签，但是可以通过融易汇在主柜台查询。


**155.问：两融账户的融资可用余额怎么查呢？**


> 答：可参考QueryCreditFundInfo()返回的 XTPCrdFundInfo.line_of_credit 字段，这个实时剩余的授信额度，既可以用来融资，也可以用来融券。


**156.问：两融账户要查询可用保证金，是哪个接口，哪个字段呢？**


> 答：可调用QueryCreditFundInfo()查询，两融保证金可用数 参见返回的 XTPCrdFundInfo.guaranty 字段。


**157.问：XTP快照行情XTPMarketDataStruct.pre_close_price字段，是除权前的收盘价格吗？**

> 答：不是，xtp中的行情价格都是除权除息后的价格，pre_close_price是交易所推送过来的实际昨收价。比如：昨收价是10元，但是一股分红1元，那么今天看到的prev_close_price就是9元。


**158.问：api的log是同步写的吗？**


> 答：quote.log和trade.log是同步写的日志。Level2行情udpseq开头的日志是异步写的日志。


**159.问：为什么实盘下订阅成功，但是OnTickByTick()和OnOrderBook()没有推送数据？**


> 答：请先确认是否已经开通了level2权限，如果开通了请确认是否使用的UDP连接，防火墙是否关闭。对于orderbook数据，请确认连接的行情地址是否有Orderbook数据。


**160.问：逐笔成交如何对应到逐笔委托？**


> 答：深市中XTPTickByTickTrade.bid_no/ask_no 与 XTPTickByTickEntrust.seq对应，沪市中XTPTickByTickTrade.bid_no/ask_no 与 XTPTickByTickEntrust.order_no对应。


**161.问：在逐笔行情中，如何判断这一笔成交是报单成交还是撤单成交呢？**


> 答：深市在逐笔成交里看成交标识trade_flag('4':撤; 'F':成交），沪市则先通过逐笔成交关联到逐笔委托，然后在逐笔委托里看ord_type('A': 增加; 'D': 删除)，'D'说明是一笔撤单，那么该逐笔成交说明是撤单成交。


**162.问：Level2行情推送会有乱序的可能吗？**


> 答：udp组播不保证顺序，可能会乱序，但是api在推送行情时，在一定程度上是对消息保序的。


**163.问：在哪儿查询两融标的列表及保证金比例、可充抵保证金证券及折算率？**


> 答：https://www.zts.com.cn/credit-service/rzrq/article?catId=3705。


**164.问：OnQueryAsset()返回的withholding_amount字段，什么情况不为0？**


> 答：使用自有资金委托买入的订单是未成交的挂单时，withholding_amount不为0。该字段包含：预扣买入未成交的交易资金 + 预扣手续费，可参见XTPQueryAssetRsp结构体中的说明。


**165.问：两融账户报单逆回购，为何报错：11000310, error_msg = User type not match with business type.**


> 答：两融账户不支持该业务，只有普通现货账户可以报单逆回购。


**166.问：两融账户支持可转债申购吗？**

> 答：现货、两融账户都支持可转债申购业务，InsertOrder()报单的 business_type 也是 XTP_BUSINESS_TYPE_IPOS。


**167.问：申购50ETF失败，错误提示：11010203，Cash ratio is overflow in ETF creation，什么原因？**


> 答：申购ETF份额时，允许使用现金替代全部或部分成份股，但不能超过最大现金替代比例。


**168.问：调用SubscribeTickByTick()订阅期权逐笔行情，为什么没有数据推送呢？**


> 答：期权没有逐笔数据，只有5档快照数据，订阅成功也没有数据推送。


**169.问：XTPQuoteFullInfo行情静态数据里，什么类型的证券security_type 是 XTP_SECURITY_OTHERS？**


> 答：是xtp不支持的证券类型，在xtp中不支持买入，但如果有持仓，则可以卖出。


**170.问：xtp有查询所有可交易股票的接口吗？**


> 答：可通过QueryAllTickers()接口来获取所有可交易合约，包括当天停牌的股票、债券，但是不包括指数合约。


**171.问：如果有一只股票已经订阅过了，还没有退订，然后在某个地方又发起了订阅请求，这样会有什么影响吗？**


> 答：允许重复订阅，不影响。


**172.问：不同的进程中TraderSpi能收到其他进程的订单消息和成交回报，那QuoteSpi是否会收到其他进程的订阅和查询消息呢？**


> 答：不会的，不同的进程QuoteSpi消息互不影响，TraderSpi查询消息也互不影响。


**173.问：OnOrderEvent()和OnTradeEvent()之间的时序是怎么样的？**


> 答：基本上保证OnTradeEvent()在OnOrderEvent()的未成和结束状态之间；基本上不存在未成的订单响应在成交回报之后来，全成的订单消息肯定在成交回报后面到来。


**174.问：逐笔数据中，深证市场的逐笔成交中trade_flag为'4'是撤单，但是撤的是买单还是卖单要怎么看呢？**


> 答：XTPTickByTickTrade.bid_no/ask_no，仅其中一个字段有值，另一个字段值为0，如果撤单的买方订单号bid_no不为0，说明撤的就是买单，否则撤的就是卖单。


**175.问：公网测试环境下，请问如何保留每天的交易数据？**


> 答： 如果是官网申请的现货测试账号，可登录官网 https://xtp.zts.com.cn/login 自行设置保留持仓。
    如果不是官网申请的现货和两融账号，请补充以下内容发送邮件到运维的邮箱  wb_chennan@zts.com.cn
>   设置内容：保留账户持仓
>   账号：
>   密码：
>   交易服务器IP：
>   交易服务器port:。


**176.问：公网测试环境下，请问没有新股申购额度如何测试新股申购？**


> 答： 请补充以下内容发送邮件到运维的邮箱  wb_chennan@zts.com.cn
 设置内容：增加新股申购额度
 账号：
 密码：
 交易服务器IP：
 交易服务器port:。


**177.问：请问从行情静态信息里取到的信息，可以用股票类型（风险警示板）以及股票名称中的ST来判断ST股票吗？**


> 答：可以这样判断，判断股票类型是调用QueryAllTickersFullInfo()，如果返回的XTPQuoteFullInfo.security_status 为 XTP_SECURITY_STATUS_ST，则说明该合约属于风险警示板。


**178.问： 请问实盘下单，OnOrderEvent()返回order_status=XTP_ORDER_STATUS_REJECTED是什么原因？**


> 答：可根据错误码查看错误提示，如果是XTP柜台拒单，请至XTP官网查看XTP错误代码速查表，如果是交易所拒单，请到交易所官网下载相应的错误代码文件：
      XTP错误码：https://xtp.zts.com.cn/doc/api/xtpDoc 错误代码速查表。
      上交所：http://www.sse.com.cn/services/tradingservice/tradingtech/technical/other/ ，或者直接搜索：IS111_上海证券交易所报盘软件错误代码表 。
      深交所：http://www.szse.cn/marketServices/technicalservice/interface/ ，或者直接搜索：深圳证券交易所Binary交易数据接口规范。


**179.问：OnQueryAllTickersFullInfo()返回的XTPQuoteFullInfo没有关于期权的字段，比如说对应标的、到期日、行权价、call_or_put之类的信息，如何获取？**


> 答：在交易api里调用接口QueryOptionAuctionInfo()来获取，参见返回的 XTPQueryOptionAuctionInfoRsp 结构体。


**180.问：有API接口来判断申请的账号是普通账号还是信用账号吗？**


> 答：调用QueryAsset()查询账户资金，返回的XTPQueryAssetRsp结构体包含有账户类型 account_type，枚举值如下：
```
///@brief XTP_ACCOUNT_TYPE 账户类型
typedef enum XTP_ACCOUNT_TYPE
{
    XTP_ACCOUNT_NORMAL = 0,	/// 答：读取配置文件config.json失败，请检查配置文件是否存在，路径是否正确，一般应该和程序文件放在同一目录，如果文件没有问题请检查配置参数的语法是否正确。


**182.问：OnOrderBook()推送的订单簿行情，推送频率是间隔多长时间？**

> 答：订单簿和逐笔行情都是实时推送，没有间隔时间限制。具体请参考：XTP行情服务接入前指引。


**183.问：可以多账户登录吗？多账户时共用一个socket还是每个账户一个socket？**


> 答：api支持多个账户连接，多次调用login即可，一个账户一个socket连接，不会共享连接。


**184.问：OnDepthMarketData()推送的期权行情，多久刷新一次呢？**


> 答：连续竞价期间，上海期权，行情数据有变化时 0.5 秒一次，无变化时 30 秒一次；深圳期权，行情数据有变化时 0.5 秒一次，无变化时 60 秒一次。具体请参见：XTP行情服务接入前指引。


**185.问：请问getApiLastError()这个函数是线程安全的吗？会返回空吗？**


> 答：这个函数不是线程安全的，其他函数都是线程安全的。getApiLastError()不会返回NULL。


**186.问：689009可卖持仓185股，报单委托卖出100股，错误提示：11010111，新订单的数量参数无效，是怎么回事？**


> 答：普通CDR遵循普通股票的交易规则，100股以下为零散股。科创板CDR交易规则遵循科创板的报单规则，200股以下为零散股，零散股要一次性委托卖出。


**187.问：科创板股票报单最低值200股，xtp中能通过静态数据获取到吗？**


> 答：可调用QueryAllTickersFullInfo接口获取，参见 XTPQuoteFullInfo结构体中的bid_qty_unit、ask_qty_unit，限价买/卖委托数量单位。


**188.问：XTP支持配债吗？API方式如何报单呢？**


> 答：仅现货账号支持配债，两融账号不支持配债。配债跟配股一样报单，调用InsertOrder接口报单，business_type = 6，side = 1，price_type= 1。


**189.问：账户配债了一只沪市的债券、一只深市的债券，然后查询资金，发现买入成交证券占用资金fund_buy_amount，累计了沪市配债的金额，但没有计算深市配债的金额，这是什么原因呢？**


> 答：沪市的配股配债有成交回报，fund_buy_amount会累计该笔成交金额，但深市的配股配债没有成交回报，没有成交金额，只会预扣资金。


**190..问：信用账号是否支持ETF申赎？**


> 答：信用账号不支持ETF申赎，但是可以买卖ETF，使用担保品买卖。


**191.问：查询ETF清单，OnQueryETF 返回错误 Error: 11000390  msg: Failed to get etf base information!**


> 答：这个错误是获取ETF基本信息失败，一般是不支持申赎的ETF，如果是支持的，应该是市场填错了。


**192.问：ETF申赎，深市的跨市场资金成交记录中，证券代码159900是什么含义？**


> 答：深市的跨市场ETF申购成交类型中，159900是一个虚拟成份股票，实际上是沪市成份股票的现金替代总金额。


**193.问：ETF申赎时的现金替代和跨市场成交，往往返回两笔数据，一笔成交数量为1，一笔成交数量往往是1000000，不知道这两笔数据分别的含义是什么？**


> 答：因为成交金额超限，接口库里字段存不下，所以将成交数量拆分成了两条记录显示。


**194.问：当天申购ETF成功后，赎回ETF时报错：11010121，账户可用持仓不足，但是OnQueryPosition()返回的sellable_qty是够的呢？**


> 答：当日以一篮子股票申购的ETF基金份额，当日不得赎回，但是当日可以卖出。
     当日赎回的ETF基金份额获得的一篮子股票，当日不得用于申购ETF基金份额，但是当日可以卖出。
      报单卖出时参数：business_type=XTP_BUSINESS_TYPE_CASH，side=XTP_SIDE_SELL。


**195.问：ETF申购成功，查询持仓也有了，但是赎回时报错：11010121，账户可用持仓不足？**


> 答：ETF申赎 business_type = XTP_BUSINESS_TYPE_ETF， ETF买卖 business_type = XTP_BUSINESS_TYPE_CASH。两者的关联交易规则如下：
（1）当天买入的股票，当天可以用来申购ETF。
（2）当天买入的ETF份额，当天可以赎回，但是当天不能卖出ETF份额。
（3）当天赎回得到的股票，当天可以卖出。
（4）当天申购的ETF份额，当天可以卖出，但是当天不能赎回ETF份额。


**196.问：如何判断深交所逐笔成交的单子是主动买，还是主动卖呢？**


> 答：主动买，代表卖方委托早于买方委托；主动卖，代表买方委托早于卖方委托。
      逻辑上，一般是和上一笔成交对比，如果比上一笔价格高，说明这笔委托推动了价格上涨，就是主动买。
      沪深两市都可通过 XTPTickByTickTrade.bid_no和ask_no的大小来判断方向，no小的表示先报单。 bid_no > ask_no，则是一笔主动买单；ask_no > bid_no，则是一笔主动卖单。


**197.问：Python版本的demo如何运行？**

> 答：以Linux+python3.9平台运行traderapi为例，需要把bin/Linux/centos7+python3.9/libxtptraderapi.so文件copy到bin/test，并修改test/tradertest.py中ip、port、user、password、local_ip，即可运行交易demo。如果不是安装的python3.9、boost_1_80_0版本，那就得自己重新编译再运行Demo。

**198.问：编译python版本Demo时报错：ImportError: libboost_python39.so.1.80.0: cannot open shared object file: No such file or directory**

> 答：在CMakeLists.txt中设置的python和boost路径是否不正确？如果编译时使用的绝对路径，而之后修改了文件路径，那么就需要重新编译。

**199.问：编译python版本source源码时，使用编译生成的libboost_python39.so.1.80.0，但是错误提示 error: reference to 'mutex' is ambiguous，这是什么原因？**

> 答：是引用的关键字mutex模糊不清，打开 vnxtptrader.h 和 vnxtpquote.h 这2个文件，搜索 mutex，如果缺少boost::，那么修改为 boost::mutex，再重新编译即可。


**200.问：python版本的api是否支持MacOS？**


> 答：目前支持Windows、Linux平台运行，但是不支持MacOS。


**201.问：python版本的api使用Anaconda会跟python不兼容吗？**


> 答：我们编译时使用的python，不能使用Anaconda，如果要直接使用我们封装的库，就只能安装python3.9系列的版本。


**202.问：运行python版本Demo程序报错ImportError: DLL load failed，所有的.dll，.pyd，.lib文件都已经在当前目录了，为什么还找不到指定的模块？**


> 答：python版本api是用VS2010封装的，如果未安装VS的运行环境安装包，运行测试程序时会提示该错误。需根据python的位数安装对应的vs运行库，python是32位就选vcredist_x86.exe，64位选vcredist_x64.exe。


**203.问：在windows下运行Python版本的Demo， 错误提示：ImportError: DLL load failed，找不到指定的模块，这是什么原因？**


> 答：是否未安装VS的运行环境？如果已经安装VS2010的vcredist，那就按照编译说明文档重新编译boost.python库，编译source下封装api的源码，并替换生成的vnxtpquote.dll 和 vnxtptrader.dll库文件再运行。


**204.问：登录行情时，错误提示：connect server failed.[OS:10049]The requested address is not valid in its context.这是什么原因？**


> 答： 能ping通服务器的话，请检查一下Login时local_ip的值，注意金桥机房必须传入实际使用的网卡的IP。如果传入127.0.0.1就默认本机，就连接不上服务器，local_ip不能输入空串，需传入网卡的ip，不是外网ip。


**205.问：[XTP:1]connect server failed.[OS:10049]The requested address is not valid in its context。这个行情连接是什么错误？**


> 答：请检查一下login的参数local_ip是否不对，要填实际使用的网卡的ip。


**206.问：报单回报中需要资金账户这个字段，请问如何处理？**


> 答：登录成功后，可根据session_id和资金账户做一个映射，那么在收到报单回报时，可以通过session_id获取到资金账户。


**207.问：session_id在进程重启后会重复吗？**


> 答：进程重启就相当于重启api，重新Login时初始化的session_id是一样的，如果断线重连时没有销毁api，重新Login时session_id会不同。


**208.问：怎么知道程序中的心跳是否正常？**


> 答：SetHeartBeatInterval设置心跳检测时间间隔默认是15秒，一般在断点调试时，会长时间没有消息通讯，如果心跳间隔值设置短了容易断线，可以适当的设置大点，方便本地调试，比如设置1000秒试试。


**209.问：同一台机器可以开两个进程接收行情吗？开多个进程接收Level2行情有影响吗？**


> 答：可以，两个进程请使用不同的client_id。但是同一台机器开多个进程订阅Level2行情容易丢包，为了确保程序能正常接收行情，一般来说不能超过2个，因为行情数据太多，开多了可能数据推送不过来。


**210.问：国债逆回购XTPOrderInsertInfo.quantity填100的整数倍时，返回错误提示：11010126，证券数量超出范围，什么原因呢**


> 答：上交所和深交所的国债逆回购品种，申报数量应当为1000元⾯额或其整数倍，单笔最⼤申报数量不得超过100亿元⾯额，100元⾯额为1张，1手 = 10张。具体请参见 上海/深圳证券交易所债券交易规则。


**211.问：国债逆回购T+1日后，总资产total_asset字段不包含国债逆回购资金吗？**


> 答：如果买入1天期的国债逆回购，total_asset在T+1日后会包含逆回购资金，因为收益会在T+1日到账进入可用资金。
      如果买入超过1天期的国债逆回购，total_assetT+1日后不会显示逆回购资金，因为xtp系统中只能在买入当日显示国债逆回购的持仓，在T+1日后不会显示，也就没法计算市值。


**212.问：可转债在行情和交易中数量的单位不一致？**


> 答：在行情中，可转债的委托数量和成交数量qty，上交所是"手"为单位，深交所是"张"为单位。但是在交易中，可转债的报单数量quantity是以"张"为单位。1手=10张。


**213.问：恒生ETF 159920，市场是深证，但是查询静态信息返回是未知类型 XTP_TICKER_TYPE_UNKNOWN，该ETF不支持申赎吗？**


> 答：不支持申赎的品种，都是未知类型，请参见官网上的XTP支持业务列表，第一列交易类是可买卖交易的种类，第二列申购赎回中的白名单是支持申赎的ETF代码，不在白名单里的ETF不能申赎，但可以买卖交易。


**214.问：SubscribeMarketData订阅行情，包括指数行情吗？如：中证500指数。**


> 答：交易所的实时行情，xtp系统中都有，包括股票、债券、ETF、指数、期权行情。


**215.问：QueryAllTickers返回的合约静态信息中包括指数吗？**


> 答：不包括指数，该接口查询对应市场的可交易合约（股票/基金/债券/期权）基本信息。


**216.问：在行情数据里，如何区分一个合约代码是股票还是基金还是指数？比如000828，既是股票又是指数，也是开放式基金，数据源里怎么区分？**


> 答：exchange_id + ticker唯一确定一个证券标的，如果要区分是股票/基金/指数，需要自己针对合约代码特征来识别。可以先使用QueryAllTickersFullInfo接口查询静态信息，通过security_type来判断，然后在本地建立好映射表。


**217.问：为什么Level2行情是用TCP订阅的MarketData？**


> 答：所有的订阅都是通过TCP发起的请求，只是使用UDP来接收行情数据。


**218.问：采用UDP方式连接时，如何设置行情接收缓冲区大小？**


> 答： 可以通过SetUDPBufferSize接口设置，建议将UDP的缓存设置大点。2.2.30及以上版本的API，可以设置比以前小一些，默认是64M，设置为256M就够，512M就足够。


**219.问：接收Level2全市场行情数据时CPU占用率一直保持在200%左右，即使盘后没有收到任何行情数据也是这样，请问正常吗？**


> 答：这是正常的，CPU占用率在TCP连接时比较低，UDP连接方式会很高，因为除了一个接收线程接收行情外，还有一个解析线程一直在解析行情，如果关闭异步日志，可以减少一个核的占用。


**220.问：用UDP接收Level2行情时，如何设置线程绑定CPU？**


> 答：分别使用SetUDPRecvThreadAffinityArray()、SetUDPParseThreadAffinityArray()函数设置接收线程、解析线程绑定CPU。一个组播组有一个接收线程和一个解析线程，一个线程绑定一个核，绑定多少个核要看有几个组播组，取决于连接的行情服务器地址和订阅情况。
     如果同时订阅快照和逐笔行情，而且快照和逐笔行情是在2个不同的组播组，那么总共需要绑定4个核，也就是接收行情线程绑定2个cpu，解析行情线程绑定2个cpu。


**221.问：异步日志文件太大，异步日志的作用是什么？建议是开启还是关闭？**


> 答：异步日志仅在UDP接收Level2行情时会有，主要用来排查丢包情况。建议在调试初期开启，调试稳定后可以关闭，设置SetUDPSeqLogOutPutFlag()接口参数flag为false来关闭异步日志。


**222.问：快照行情中last_price和upper_limit_price都是double类型，为什么一只股票的涨停价是2699999， 但是买一价是5.270000？**


> 答：这是因为浮点数导致，股票价格有效位是小数点后两位，请按四舍五入原则处理，保留小数点后两位即可。


**223.问： 集合竞价的时候，快照数据里面的last_price是有数据的么？**


> 答：集合竞价时候，last_price为0，因为没有成交，就不会有成交价。


**224.问：OnDepthMarketData返回的十档申买申卖，9:15-9:25之间没有数据？**


> 答：在集合竞价阶段，十档申买申卖字段仅买一卖一有值，即：bid[0]，ask[0]，bid_qty[0]，sk_qty[0]有值。


**225.问：OnDepthMarketData返回的买一卖一队列，什么时候有值？**


> 答： 交易日9:25分Level2行情开始有买一卖一队列数据，也就是十档行情里的买一卖一。


**226.问：bid1_qty[] 和 ask1_qty[]数组的大小不是固定的？数组最大size为多少**


> 答：数组的大小不是固定的，最大size是50，请先判断数组长度再使用，根据bid1_count 来判断 bid1_qty[] 数组长度，根据ask1_count 来判断 ask1_qty[] 数组长度。


**227.问：股票熔断时，深度行情数据里有标志吗？**


> 答：有标志的，请参见：XTPMarketDataStruct 里的ticker_status，V=波段性中断。


**228.问：9:15- 9:30行情数据中ticker_status[0]是'C'才对啊，为什么会是'B'呢？**


> 答：9:15-9:25为开盘集合竞价时间，ticker_status[0]是'C'，9:25-9:30之间是'B'。


**229.问：停牌的股票，行情数据中ticker_status为什么是T0？**


> 答：P肯定是停牌的，但T也可能不能交易，是否可以交易要看第1位，因为停牌的股票，交易所可能发P，也可能发T。


**230.问：开盘前，想要获取当日股票的涨跌停价格，有接口吗？**


> 答：9:15之前可通过QueryAllTickers获取涨跌停价，参见XTPQuoteStaticInfo中upper_limit_price、lower_limit_price字段。


**231.问：OnTickByTick推送的逐笔数据中channel_no是什么意思？**


> 答：交易所为不同的证券分配了不同的频道代码，一个channel_no里面可能会有多只股票，一只股票的逐笔委托和逐笔成交数据中channel_no 都相同。在同一个channel_no内seq唯一。


**232.问：OnTickByTick返回的逐笔成交数据中交易所时间错乱，如果收到数据直接保存指针，然后对指针所指向的内存数据进行处理会有影响吗？**


> 答：api提供的tickbytick数据，仅在OnTickByTick回调函数中有效，如果您仅仅保存指针，而不是指针所指向的内存数据，就会因为内存在api内部循环使用，导致您后面使用指针的时候，内存数据就不正确了。


**233.问：查询持仓返回的yesterday_position字段是不是不会变？怎么计算当前仓位中当有多少是今天开的仓位？**


> 答：昨日持仓yesterday_position是不变的。如果仅做普通买卖的话，也没有任何未完结的挂单，那么 总持仓 = 可卖持仓 + 今日买入的持仓。日初的时候，总持仓 = 可卖持仓 = 昨日持仓。


**234.问：查询回调函数中参数is_last为true时，这最后一个响应有实际的消息数据吗？**


> 答：有实际的消息数据，可能消息只是error_info有效，判断时请先看error_info的error_id是否为0，如果为0，再判断其他参数。不为0的话，其他的参数可能无效。


**235.问：OnQueryAllTickers返回的ETF合约静态信息中，ticker_type值为什么是6而不是2？**


> 答：交易所官网可以查到每只ETF的交易商名单，如果我们公司不在该名单里，就不支持该ETF，ticker_type 就为6。可参考：http://www.sse.com.cn/assortment/fund/etf/list/。


**236.问：ETF申赎时，T日申购赎回清单中公布的当日现金差额的估计值是哪个字段？**


> 答：XTPQueryETFBaseRsp中的estimate_amount为T日预估现金差额。cash_component，目前这个字段没有使用。


**237.问：如果发生分红、配股之类的，通过什么方式去查询呢？**


> 答：如果是普通现货账号，可以通过查询持仓看到分红送股后的总持仓，参见XTPQueryStkPositionRsp中的total_qty。如果是信用账户，可以通过查询负债看到负债合约中增加的权益数量，通过查询持仓可以看到担保品持仓中送股后的总持仓。


**238.问：融券期间发生的分红、配股，这些权益应该怎么计算？**


> 答：如果有分红送股，在融资融券负债信息XTPCrdDebtInfo中due_right_qty应偿还权益数量会体现。假如融券某只股票1000股，查询负债合约中未偿还融券数量是1000，此时应偿还权益数是0，如果某天这只股票10送3，那么在除权除息日之后，您的负债合约中应偿还权益数量是300，未偿还融  券的数量就变成了1300。


**239.问：qty_upper_limit是指账户对这只股票的最大申购数量吗？错误提示：11010413 The quantity of IPO order exceeds the quota。**


> 答：qty_upper_limit是指这只股票的最大允许申购数量，需查询可申购额度quantity，参见XTPQueryIPOQuotaRsp，请使用min（可申购额度，最大允许申购数量）进行新股申购。


**240.问：报市价单是否可以不用填价格？**


> 答：市价单的委托价price没有意义，但是全面注册制后，沪市主板股票的市价委托需要填一个价格作为保护限价，即买入申报的成交价格和转为限价申报的申报价格 不高于买入保护限价，卖出申报的成交价格和转为限价申报的申报价格 不低于卖出保护限价。深市主板股票的市价单的委托价格可以填0。


**241.问：查询报单和报单是不是共用一个线程？**


> 答：是共用一个socket，如果查询消息没有处理完，会堵塞后续订单响应消息。报单后，如果有查询消息在处理，则会等待查询结果发送完毕，再发送报单的回报消息，那么收到订单确认消息就晚了。


**242.问：报单全部成交时，OnTradeEvent推送快还是OnOrderEvent更快一点？**


> 答：对于全部成交的情况，最后有一个全部成交的状态，这个状态在OnTradeEvent之后推送。也就是OnOrderEvent先推送一个初始状态，有成交时OnTradeEvent推送成交信息，全成时OnOrderEvent再推送一个最终的全成状态。


**243.问：现在报单响应OnOrderEvent()还是不会返回交易所的报单编号order_exch_id？**


> 答：是的，但是可通过查询订单QueryOrdersEx() 或 QueryOrdersByPageEx() 获取，请参见 XTPOrderInfoEx.order_exch_id。另外，成交通知OnTradeEvent()也会返回XTPTradeReport.order_exch_id。


**244.问：查询ETF基本信息和ETF成分股信息是两个单独的回调函数，申赎ETF时如何判断成分股全都收到了，中间有没有丢失？**


> 答：OnOrderEvent返回的order_status为全部成交状态时，就表明ETF成分股都收到了。


**245.问：报单后会返回一个初始的未成交状态吗？然后对该订单进行撤单，OnOrderEvent会返回几种报单状态？**


> 答：报单状态order_status，初始化状态是报单到柜台，未成交状态是收到了交易所确认。如果撤单时订单未成交，撤单成功会返回一个已撤单状态，如果撤单时订单部分成交，则会返回一个部分撤单状态。


**246.问：报单后撤单，会有先收到撤单成功，再收到成交通知的情况吗？**


> 答：xtp撤单的时候，如果是部分成交，一般是先收到部分成交的通知，再收到撤单成功的通知，但如果成交回报消息超时，就有可能先收到撤单成功，再收到部分成交的通知。


**247.问：能否根据order_cancel_xtp_id判断是报单还是撤单？**


> 答：具体报单还是撤单，要根据order_submit_status来区分。如果一个报单是全撤状态，那么订单的order_cancel_xtp_id != 0成立，但是order_cancel_xtp_id != 0 时订单不一定就是报单，我们允许对撤单进行撤单，只是会拒单。


**248.问：在收到撤单回报之后，又收到之前的成交回报，这种情况是否会发生？**


> 答：交易所本身发送的消息是存在这种情况的，但是xtp在某种程度上保证消息顺序，API会一直等到成交回报到齐之后再发送撤单成功消息给用户。


**249.问：查询股票持仓，返回的数据中purchase_redeemable_qty应该是和ETF相关的，为什么普通A股这个字段有数据？**


> 答：如果是ETF的成分股，就代表可用于申购的数量。如果是ETF，就代表可用于赎回的数量。


**250.问：哪个API接口可以查询某只股票所有已经融券的总数量？**


> 答：可以调用QueryCreditTickerDebtInfo()查询指定证券的负债未还信息，返回的stock_total_quantity即为已经融券但是未还的总数量。


**251.问：QueryTrades()可以查询所有历史成交记录吗？怎么返回find none record？**


> 答：xtp不能查询历史记录，服务器每天都重启，仅保持一天的数据，api和客户端都只能查询到当天的订单记录。实盘用户可以登录融易汇或齐富通查询历史记录。


**252.问：信用账户买卖交易报单，错误提示：11000310，User type not match with business type. 这是什么原因？**


> 答：信用户进行普通交易时，要使用担保品买、担保品卖，business_type = 4，Side = 1/2。


**253.问：融资买入的时候，XTPQueryAssetRsp.buying_power可用资金也会减少吗？**


> 答：不会减少，融资买入使用的不是自有资金，而是借来的资金。担保品买使用的是自有资金，可用资金才会减少。可参见 XTPQueryAssetRsp.buying_power 字段。


**254.问：查询持仓total_qty有250股，yesterday_position有200股，报单现券还券50股成功后，报单卖出200股为何也全部成交了？**


> 答：现券还券优先使用当日买入的持仓，然后再使用昨仓。


**255.问：融资融券现金还款，错误提示：11000905，Do not have enough fund to do cash repay! 要先查询可用资金，再查一下负债all_debt，然后用两者最小值来还？**


> 答：先调用QueryAsset查可用资金，如果申请金额大于可用资金余额（amount > buying_power），报单会拒单，如果申请金额大于所有负债未偿还金额，则不会拒单，最终以实际使用金额为准。


**256.问：融资买入产生的挂单，会冻结资金吗？信用额度会减少吗？**


> 答：对于融资买入，未成交或部分成交的挂单，会冻结融资头寸，授信额度也会减少，可参考XTPCrdFundInfo结构体中的line_of_credit字段。


**257.问：对T日前的融券负债还券，当天还券的总数量，调用哪个接口获取呢？**

> 答：没有直接获取的接口，可查询当天还券的委托及成交记录来间接计算。
    如果是买券还券，因为有成交回报，那么可调用QueryTrades()查看返回的成交数量XTPTradeReport.quantity，累加成交数量得到买券还券总数量；
    如果是现券还券，因为没有成交回报，但如果报单状态是已确认，那么可调用QueryOrders()查看返回的委托数量XTPOrderInfo.quantity，累加委托数量得到现券还券总数量。

**258.问：查询指定证券的融券负债，XTPCrdDebtStockInfo中stock_repay_quantity是指可以用来还券的数量吗？今日融券总数量如何计算？**


> 答： stock_repay_quantity指的是融券负债中今日可还券的数量，不包含当天融券卖出的数量。今日融券卖出的数量 = 融券负债未还总数量（stock_total_quantity ） - 融券负债可还券数量（stock_repay_quantity）。


**259.问：使用现券还券偿还融券负债后，当天能恢复"两融授信额度"和"可融券数量"吗？**


> 答："两融授信额度"和"可融券数量"是两个相互独立的概念，在柜台是分别校验的。两融授信额度line_of_credit是实时恢复的，可融券数量left_qty当天不能恢复，需要等到晚间清算后才能恢复。


**260.问：OnQueryCreditTickerAssignInfo返回的是剩余可融数量。请问哪个接口能返回总的融券头寸？**


> 答：目前没有提供这个字段，只能间接计算。日初没有交易的时候，初始的总融券头寸数量 = 剩余可融券数量 + 负债未还总数量，也就是 XTPClientQueryCrdPositionStkInfo.left_qty + XTPCrdDebtStockInfo.stock_total_quantity。


**261.问：OnQueryCreditTickerAssignInfo返回的yesterday_qty 是不是昨夜的总融券头寸？**


> 答：yesterday_qty这个字段没有启用。


**262.问：OnQueryAsset返回的资金中证券资产security_asset为0，OnQueryPosition返回的持仓也没有市值，后续有计划提供吗？**


> 答：由于交易服务器没有连接行情服务器，目前不太好提供这个数值。


**263.问：融券卖出后，融券卖出所得资金余额会马上增加，还是T+1日增加？**


> 答：会马上增加，可调用QueryAsset()接口查询 融券卖出所得资金余额，参见返回的 XTPQueryAssetRsp.repay_stock_aval_banlance 字段。


**264.问：融券卖出报错：11010503，Failed to check credit stock position. 是什么意思？**


> 答：该证券的剩余可融券数量不足，请根据可融券头寸信息中的剩余可融券数量来下单。可调用QueryCreditTickerAssignInfo()查询剩余可融券数量，参见返回的XTPClientQueryCrdPositionStkInfo.left_qty 字段。


**265.问：买券还券时，使用的是账户资金里的可用资金吗？**


> 答：会优先使用融券卖出所得资金余额 repay_stock_aval_banlance，如果这部分资金不够，再自动使用可用资金。


**266.问：融券负债中应偿还权益数量是什么意思？remain_qty不包含due_right_qty吗？**


> 答：融券卖出后分红送股的数量，也就是应偿还权益数量due_right_qty，这部分数量也要偿还。remain_qty不包含due_right_qty，需要还券总数量为due_right_qty + remain_qty。


**267.问：现券还券操作没有报错，但是OnTradeEvent没有响应，怎样才能成交？**


> 答：现券还券属于非交易类型，没有成交回报，订单确认就可以，负债信息中的未偿还融券数量 XTPCrdDebtInfo.remain_qty、该证券的持仓相应地都会更新。


**268.问：现券还券后，OnQueryPosition()返回的total_qty会减少吗？**


> 答：现券还券有OnOrderEvent()响应，也就是订单确认后，如果使用的今仓，则总持仓total_qty会减少，如果使用的昨仓，则可卖持仓sellable_qty会减少。


**269.问：信用账户查询持仓，同一个证券如何区分哪些是融资买入，哪些是担保品买入？**


> 答：OnQueryPosition() 返回的总持仓不区分融资买入和担保品买入。卖出持仓时可以都填担保品卖，如果有对应的融资负债，会自动转换成卖券还款。


**270.问：两融账户，如何使用api报单买卖货币基金？**


> 答：使用InsertOrder()接口报单担保品买、担保品卖，business_type = XTP_BUSINESS_TYPE_MARGIN，担保品买 side = XTP_SIDE_BUY，担保品卖 side = XTP_SIDE_SELL。


**271.问：购买沪市可交易货币基金，应该优先扣减融券卖出所得资金，但是发现优先使用了自有资金，卖出货币基金时优先释放的自有资金，是不是后台扣款顺序的问题？**


> 答：不是扣款顺序的问题，应该是融券卖出所得资金余额为0，自动使用了自有资金。相应地，在卖出货币基金成交后，会优先增加融券卖出所得资金余额repay_stock_aval_banlance，剩余部分增加到账户可用资金buying_power。


**272.问：QueryAllTickers获取不到交易日停牌的股票静态信息？**


> 答：可以获取到停牌的股票静态信息，但是不包括指数合约。建议使用QueryAllTickersFullInfo()来获取所有合约的静态信息，而且包括指数等不可交易的合约。


**273.问：请问 InsertOrder()和InsertOrderExtra()的返回值是不是都是order_xtp_id？哪种接口报单速度更快一点**


> 答：InsertOrder()的返回值是order_xtp_id，但是InsertOrderExtra()要先调用GetANewOrderXTPID()提前获取一批需要的order_xtp_id，返回非0表示报单发送成功，此时等同于传入的order_xtp_id。相比直接调用InsertOrder()报单，GetANewOrderXTPID() + InsertOrderExtra() 速度稍微快一点。


**274.问：在交易日开盘前8:50报单，调用InsertOrder()发送后返回非“0”值，但是开盘前一直收不到OnOrderEvent()响应，这是什么原因呢？**


> 答：在交易日盘前的报单，只是缓存在XTP服务器，要等到9：15开盘时收到报单信号才能发往交易所，之后才会收到OnOrderEvent()报单响应消息。


**275.问：QueryAccountTradeMarket()返回的trade_location，如何判断是沪市还是深市呢？**

> 答：trade_location按位来判断，从低位开始数：
    第0位表示沪市，即如果(trade_location&0x01) == 0x01，代表可交易沪市，
    第1位表示深市，即如果(trade_location&0x02) == 0x02，表示可交易深市，
    如果第0位和第1位均是1，即(trade_location&(0x01|0x02)) == 0x03，就表示可交易沪深2个市场。


**276.问：沪市逐笔成交行情中，trade_flag是不是盘前盘后集合竞价都是N，连续竞价是B或者S？**


> 答：是的，集合竞价阶段trade_flag = 'N'，不存在主动买和主动卖的区分。


**277.问：不同的进程中TraderSpi能收到其他进程的订单消息和成交回报，那么QuoteSpi是否会收到其他进程的订阅和查询消息呢？**


> 答：不会的，不同的进程QuoteSpi消息互不影响，TraderSpi查询消息也互不影响。


**278.问：有接口可以查询到现在还没有成交的挂单吗？**


> 答：可通过QueryUnfinishedOrdersEx()接口查询未完结的报单，另外，查询报单QueryOrdersEx()返回的结果也包含未完结的报单。


**279.问：purchase_redeemable_qty是今日可申购赎回数量，还是今日已申购赎回数量？**


> 答：是可申购或者可赎回的数量。如果是ETF的成分股，就是可用于申购的数量，如果是ETF，就是可用于赎回的数量。


**280.问：除了调用Login()登录，还需要LoginALGO()登录么？**


> 答：如果要使用算法功能，则需要LoginALGO()登录，否则不需要。


**281.问：调用Login()成功后，是先调用ALGOUserEstablishChannel()，再调用LoginAlgo()吗？**


> 答：是先调用LoginALGO()成功后，再调用ALGOUserEstablishChannel()建立算法通道。注意：如果多个普通账号同时调用login()登录，那么每个普通账号都需要调用ALGOUserEstablishChannel()建立算法通道。


**282.问：如果只想QueryStrategy()查询策略，也要调用ALGOUserEstablishChannel()吗？**


> 答：只查询也要调用ALGOUserEstablishChannel()。


**283.问：如果主动logout登出oms，客户端和algobus建立的连接会断开吗？重新登录oms会有新的session_id吗？**


> 答：oms断开的时候，algobus不会断开。重新登录oms后会得到新的session_id，需要使用新的session_id报算法单，但不需重新建立算法通道。


**284.问：调用InsertAlgoOrder()报算法后，算法单的母单号ID对应哪个字段呢？**


> 答：m_xtp_strategy_id 就是算法单的母单号ID，参见OnInsertAlgoOrder()返回的结构体XTPStrategyInfoStruct。


**285.问：m_client_strategy_id 有要求唯一，或者递增之类的限制吗？**


> 答：没有，m_client_strategy_id 不要求唯一，也不是全局唯一的，是用户报算法单时自定义id，帮助用户定位母单。


**286.问：在OnTradeEvent成交回报里，有办法能获取母单的m_client_strategy_id吗？**


> 答：目前OnTradeEvent里没有办法获取，但是可将返回的order_xtp_id作为参数传入GetAlgorithmIDByOrder()获取子单的母单ID，然后调用QueryStrategy()来获取母单的m_client_strategy_id。


**287.问：不知道母单的合约代码，如何获取算法单的母单ticker？**


> 答：OnQueryStrategy()返回值有母单的报单参数，解析strategy_param字符串，就可以获取ticker。


**288.问：如果启动使用restart模式，OnStrategyStateRepot()会从本交易日开始重传吗？**


> 答：不会重传OnStrategyStateRepot()，但是会从本交易日重传推送OnOrderEvent()和OnTradeEvnet()。


**289.问：母单收到了OnInsertAlgoOrder()，但是没有收到OnStrategyStateReport()，这是为什么？**


> 答：因为这个单子的状态没有变化，在策略运行状态有变化时才会通知。


**290.问：已停止状态的母单，可能还会一直推送OnStrategyStateReport()消息吗？**


> 答：可能会，比如：母单执行完停止了，但是时间还没有到用户设定的end_time，这时市场价格还是会不停地刷新。


**291.问：CancelAlgoOrder()成功后，母单是已停止状态还是已销毁状态？**


> 答：CancelAlgoOrder()的参数cancel_flag，如果是true，就是已停止，如果是false，就是已销毁。不管是已停止还是已销毁，都不会再有交易。


**292.问：CancelAlgoOrder()，传入的cancel_flag为false会撤子单吗？**


> 答：为false也会撤子单，但是只会撤一次。cancel_flag为false时，是立即停止算法母单的执行，算法平台会对已下的子单做撤单操作，其余的平仓等操作则需要客户自己处理；cancel_flag为true时，是交给算法自行处理停止请求，包括撤单、平仓、资源清理等，算法处理完成后才能结束停止，在停止过程中，算法可以继续交易。


**293.问：当我收到一个非本客户端发出的母单回报时，都要query一下才能拿到剩余信息，还有其他方式获取吗？**


> 答：OnStrategyStateReport()返回的数量，可计算出剩余信息， 请参考 XTPStrategyStateReportStruct结构体。


**294.问：OnAlgoConnected()函数，第一次登陆不会被调用吗，只有重连的时候才会被调用吗？**


> 答：是的，仅在api与算法服务器断线重连成功后才会被回调。


**295.问：交易日报算法单后，断开重连后会自动推送OnStrategyStateReport()吗？**


> 答：断线重连后，除非策略运行过程中策略状态有更新才会推送。


**296.问：算法策略参数strategy_param中，是否可以存在非策略要求的参数？ 调用QueryStrategy()查询时，返回的strategy_param是原始请求中的值吗?**


> 答：可以存在非策略要求的参数，但是自定义参数名最好不要和已定义的参数名重名，可以加上前缀来区分。如果使用API来委托下母单，QueryStrategy()查询返回的是API原始请求中的strategy_param，但如果使用SmartX客户端来委托下母单，返回的则是SmartX客户端拼接的参数。


**297.问：策略信息中m_strategy_type是个编码，如何对应策略名称？**


> 答：请参考官网中的算法-SDK文档，算法流控及母单参数示例,链接地址：https://xtp.zts.com.cn/doc/api/xtpDoc 。


**298.问：在使用algo算法交易时，算法子单执行后，子单怎么关联到相应的母单？**


> 答：收到子单回报时，可通过判断GetAlgorithmIDByOrder()函数的返回值来做关联，如果返回值非0，则是算法单的母单号。


**299.问：OnStrategyStateReport()这个接口是定时通知的吗？有查询algo执行状态的接口么？**


> 答：不是定时通知的，是母单运行状态有变化时才会推送。也可以调用QueryStrategy()接口查询策略状态，参见m_strategy_state字段。


**300.问：OnStrategyStateReport() 和 OnOrderEvent()，具体有什么区别？**


> 答：OnStrategyStateReport，是策略运行时策略状态通知，如：创建，执行，停止 这一类。OnOrderEvent是在订单未成交、全部成交、全部撤单、部分撤单、已拒绝这些状态时会有响应。


**301.问：为什么已强停的母单，还一直推送OnStrategyStateReport()？**


> 答：因为行情价格还在刷新，行情价格变动会影响算法绩效的更新。


**302.问：算法单运行时间到了设置的end_time之后，如果没有全部成交的话，怎样得到部分成交的状态呢？**


> 答：OnStrategyStateReport()推送的每条消息都会有母单状态，参见m_strategy_state字段。


**303.问：策略运行时策略状态通知，OnStrategyStateReport()每次成交都通知一次，没有完结状态的通知是吧？**


> 答：结束也会通知的，结束和end_time没有必然的关系，要看算法什么时候停止。


**304.问：CancelAlgoOrder()接口是撤销算法单的母单还是子单？**


> 答：是撤销算法母单，如果不想用算法下单时，可调用该接口撤销用户策略。

**305.问：收到OnAlgoDisconnected()，需要重新调用LoginALGO()来登录吗？**


> 答：不需要，与Algo之间的连接，断线后会自动重连，用户无需做其他操作。请不要堵塞此线程，否则会影响algo的登录。


**306.问：算法单，批量停止和批量强停，这两个有什么区别呢？**


> 答：停止的操作需要一个过程，比如撤单或者平仓，算法完整停止后，会把母单状态m_strategy_state置为已停止。
    强停的操作是立即生效，所有的算法操作都会被拦截，平台会做一次撤单操作，如果是T0，会有敞口需要用户手动平仓。尽量不要用强停操作。


**307.问：使用InsertAlgoOrder()报算法单后，OnOrderEvent()返回的是拆单后每个子单的订单状态。那算法母单的状态（例如全部成交、部分成交、撤单、拒单等），是否有对应的接口或者方法获取？**

> 答：运行的策略状态有变化时，OnStrategyStateReport()会推送策略状态通知，可根据策略的已委托数量、已成交数量、已撤单数量字段来间接计算母单的成交状态。


**308.问：如何判断母单是否结束？**


> 答：看策略状态字段 m_strategy_state，已停止 XTP_STRATEGY_STATE_STOPPED、销毁中 XTP_STRATEGY_STATE_DESTROYING、已销毁 XTP_STRATEGY_STATE_DESTROYED，都可视为母单已结束。


**309.问：母单状态XTPStrategyStateType：已执行、已停止、已销毁，这3种状态的区别在哪里？**


> 答：已执行，是策略执行完毕；已停止：一般是算法执行完成后的状态，或者是用户手动停止算法的状态；已销毁：是用户强制停止母单后的状态。已停止和已销毁状态，都不会再有交易发生。


**310.问：报算法单后如果母单被拒单，如何查看拒单信息？**


> 答：如果是发送母单失败时被拒单，可查看OnInsertAlgoOrder()返回的error_info信息，如果是母单运行时被拒单，可查看OnStrategyStateReport()返回的error_info信息。


**311.问：如果母单撤单被拒单，如何查看拒单信息？**

> 答：撤单被拒，OnCancelAlgoOrder()会返回error_info信息。


**312.问：盘中发现Level2接收的逐笔行情有丢包，如何回补缺失的行情数据？**


> 答：官网上2.2.33.5版本的API支持盘中行情回补功能，先调用LoginToRebuildQuoteServer()以TCP方式登录行情回补服务器，然后调用RequestRebuildQuote()请求回补指定行情。


**313.问：LoginToRebuildQuoteServer()是异步函数吗？**


> 答：此函数为同步式阻塞，不需要异步等待登录成功，当函数返回即可进行后续操作。

**314.问：RequestRebuildQuote()接口，并发请求回补行情，会有问题吗？**


> 答：一个QuoteApi实例只能有一个回补连接。如果请求的时候使用了多线程，由于底层通讯还是一个，实际上还是顺序请求。如果是开启了多个实例，那么多个实例就是多个连接。

**315.问：调用RequestRebuildQuote()请求回补行情时，一次性最多请求多少个数据？**


> 答：一次性回补最多1000个数据，超过1000个需要分批次请求，而且一次只能指定一种类型的数据，要么是快照数据，要么是逐笔数据。

**316.问：盘中实时回补行情，调用RequestRebuildQuote()请求频次有限制吗？**


> 答：有限制，目前配置了1秒1000次请求。


**317.问：盘中请求回补行情数据，如果OnRequestRebuildQuote()没有返回全部数据，该如何处理？**


> 答：如果一次性请求数据太多，会导致行情数据无法一次性回补完，那么此时收到的应答消息中rebuild_result.result_code =XTP_REBUILD_RET_PARTLY，用户需要根据回补结果继续发起回补数据请求。


**318.问：盘中OnRebuildTickByTick()推送的回补行情，和OnTickByTick()推送的订阅行情，是同时都会收到吗？**


> 答：请求回补缺失行情的过程中，订阅的行情也是正常推送。OnRebuildTickByTick()和OnTickByTick()函数回调不在同一个线程。


**319.问：在OnRequestRebuildQuote()函数里能调用LogoutFromRebuildQuoteServer()吗？**


> 答：不能在回调线程中调用LogoutFromRebuildQuoteServer()。一般来说，用户无需主动调用该接口，回补服务器会在无消息交互后（3秒左右）定时断线。


**320.问：与回补行情服务器通信连接断开后，API会自动重连吗？**


> 答：收到OnRebuildQuoteServerDisconnected()断线响应时，API不会自动重连。当断线发生时，有回补数据需求时，才需重新请求连接，无回补需求时，无需重连。


**321.问：OnOrderEvent()返回的报单状态会出现初始化 order_status = XTP_ORDER_STATUS_INIT 吗？**


> 答：OnOrderEvent()不会返回init状态，只会在查询报单时返回init状态。当Insertorder()返回值不为0时，就可以认为是init状态。


**322.问：如何区分一个证券代码是股票还是指数呢？**


> 答：可调用QueryAllTickersFullInfo()接口查询 security_type 获取证券详细分类，这类静态数据在开盘之前获取一次，然后在本地做个映射，盘中就不需要多次向服务器发起查询请求。


**323.问：OnQueryAsset()返回值里有一个deposit_withdraw，是做什么用的呢？**


> 答：deposit_withdraw 当天出入金字段，仅限期权账户有效，是指xtp柜台和金证柜台之间的划转资金，当天出入金 = 当日入金 - 当日出金。


**324.问：交易所的2%价格笼子新规，是按照快照行情的最新价的2%，还是逐笔成交行情的最新成交价的2% ？**


> 答：是按照交易所收到报单时的最新价的2%，可以根据快照行情最新价的2%来报单，在逐笔行情没有延迟的情况下，也可根据逐笔最新成交价的2%来报单。


**325.问：调用Login()和LoginAlgo()登录成功后，如果调用logout()登出，algo不会退出吧？**


> 答：不会退出，logout()只是登出oms服务器，并不会登出algo服务器。如果algo断开也会自动重连。


**326.问：[XTP:10210000]Login to algo server failed. User has logged.[OS:106]Transport endpoint is already。这个报错是什么原因？**


> 答：重复登录algo服务器了。一个进程中只能调用一次LoginAlgo()，多个账号同时login()登录成功后，如果其他账号再调用LoginAlgo()就会重复登录；或者一个账号调用Logout()后再调用Login()登录成功，再调用LoginAlgo()也会重复登录。


**327.问：请问GetAlgorithmIDByOrder()接口需要建立算法通道才能请求吗？同一个账户能在两个进程（两个client_id）中能建立两条算法通道吗？**


> 答：如果不涉及其他算法接口，只是调用GetAlgorithmIDByOrder()这个接口，那就不用建立算法通道。同一个账户只能建立一条算法通道。


**328.问：母单号 m_xtp_strategy_id 和 order_xtp_id一样都是全局唯一吗？m_xtp_strategy_id和order_xtp_id之间可能会重复吗？**


> 答：m_xtp_strategy_id 在算法柜台是每个交易日内唯一。如果分别来看，m_xtp_strategy_id 和 order_xtp_id 各自都不会重复，但是如果这2个值一起来看，因为生成机制不同，有可能会重复的。


**329.问：如果算法单参数中设置了 expire_action = true，算法单执行期间遇到涨停，到达结束时间后，算法单还会继续执行吗？**


> 答：设置expire_action参数是控制到了end_time后，如果算法母单还没有执行完，是继续执行还是马上停止。跟是否涨跌停没有关系。


**330.问：我如何知道这个算法单是哪种算法类型，比如是卡方还是皓兴还是非凸？**


> 答：可以调用QueryStrategy()查询策略，传入母单号xtp_strategy_id，回调函数OnQueryStrategy()返回策略类型 XTPStrategyInfoStruct.m_strategy_type。


**331.问：比如我有10000股的授信额度，第一天融券卖出10000股，第二天用现券还券10000股，这时候可不可以继续融券卖出10000股？**


> 答：不可以，剩余可融券数量不能实时恢复，要等到清算后T+1日才能恢复。请参见：XTPClientQueryCrdPositionStkInfo 结构体中 left_qty 字段。
两融授信额度是指是指整个账户能融资和融券的总额度，两融授信额度会实时恢复。请参见：XTPCrdFundInfo 结构体中 line_of_credit 字段。


**332.问：XTPCrdFundInfo中有个两融授信额度 line_of_credit，代表融资融券的额度是共用的吗？如何分别获得融资和融券的可用额度呢？**


> 答：是融资融券共用的总额度，使用之前不区分是融资的额度还是融券的额度，既可以用来融资，也可以用来融券，如果全部用来做融资，那就是融资额度，如果全部用来做融券，那就是融券额度。


**333.问：新增加的授信总额度 XTPCrdFundExtraInfo.contract_debts_load，跟两融授信额度 XTPCrdFundInfo.line_of_credit，有什么区别？**


> 答：XTPCrdFundExtraInfo.contract_debts_load 是柜台设置的总的授信额度，这个值在交易中不会变化，XTPCrdFundInfo.line_of_credit 是剩余可用授信额度，会根据交易情况而实时变化。如果要进行双中心额度划拨，那就参考 XTPCrdFundInfo.line_of_credit。


**334.问：信用双中心账户的授信额度，不同节点也是各自独立的吗？如果需要调整2个节点的额度值，是调用哪个api接口呢？**

> 答：是各自独立的，将授信额度从一个节点划拨到另一个节点，可以调用FundTransfer()接口，内转类型请参见 XTPFundTransferReq.transfer_type 字段。


**335.问：北交所行情有逐笔数据吗？调用哪个接口来订阅北交所行情？**


> 答：目前北交所行情只有5档快照数据，UDP连接调用SubscribeAllMarketData()来订阅，注意：交易所类型 exchange_id 必须填 3（XTP_EXCHANGE_NQ）。


**336.问：QueryAllTickersFullInfo()会返回北交所合约的静态数据吗？**


> 答：不会，这个接口只返回沪深2市合约的详细静态信息，要调用 QueryAllNQTickersFullInfo() 获取北交所合约的详细静态信息。


**337.问：QueryAllNQTickersFullInfo()获取的新三板合约，如何区分是北交所合约呢**

> 答：根据 OnQueryAllNQTickersFullInfo()返回的 XTPNQFI.layer_type 过滤北交所的证券代码，如果 layer_type = 2（XTP_SECURITY_LAYER_NORTH_EX），则为北交所合约。但有一个指数899050是北证50指数，交易所给的layer_type是8。


**338.问：XTPQuoteNQFullInfo.security_type 可以判断合约的详细类型吗？比如是股票还是指数**

> 答：不可以，目前该字段没有定义，取值是255 其他类型。


**339.问：上交所逐笔合并后，还是使用 TBT.seq 判定委托+成交的先后顺序吗？**

> 答：是的，但是委托+成交合在一起编号了（TBT.seq = XTPTickByTickEntrust.seq = XTPTickByTickTrade.seq = BizIndex），均可用于判定逐笔委托+成交的先后顺序。


**340.问：上交所逐笔合并后，XTPMD结构体中的ticker_status 和 bond.instrument_status 是不是趋同了？**

> 答：交易所没说这部分有变动，股票、基金还是继续使用XTPMD.ticker_status字段。

**341.问：OnTickByTickLossRange()返回的begin_seq、end_seq是丢包的逐笔编号seq吗？**

> 答：不是，返回的begin_seq、end_seq包仅为数据包，一个数据包里包含1个或者多个逐笔数据。

**342.问：OnETFIOPVData()什么时候会有回调？**

> 答：订阅ETF快照行情后，当ETF参考单位基金净值数据有变化时，OnETFIOPVData()会有回调。

**343.问：查询可转债申购是哪个接口？申购单位是手还是张？**

> 答：QueryBondIPOInfoList()接口查询今日可转债申购列表，申购最小单位为1手（1000元，10张），申购数量应当为1手或1手的整数倍。
     注意：在OnQueryBondIPOInfoList()回调中，证券类型 参见 ticker_type 字段，债券是 XTP_TICKER_TYPE_BOND。

**344.问：调用insertAlgoOrder()后就退出程序了，再调用QueryStrategy()查看状态停留在已创建，是需要调用start来启动母单吗？**

> 答：停留在已创建是因为这个母单一直没有启动，在调用InsertAlgoOrder()后不能马上退出进程，需要等到OnInsertAlgoOrder()回调响应，如果回调响应没有报错，就说明母单启动了。

**345.问：调用InsertAlgoOrder()后，能确保先有OnInsertAlgoOrder()回调，再有OnStrategySymbolStateReport()回调吗？**

> 答：如果InsertAlgoOrder()发送成功，回调顺序依次是OnNewStrategyCreateReport()、OnStrategySymbolStateReport()、OnInsertAlgoOrder()、OnStrategyStateReport() 。

**346.问：报算法单InsertAlgoOrder()发送成功后，该账号所有登录的其他客户端也会收到回调消息吗？会收到哪些回调消息**

> 答：该账号的所有客户端都会收到这4个回调消息：OnNewStrategyCreateReport()、OnStrategySymbolStateReport()、OnInsertAlgoOrder()、OnStrategyStateReport() 。

**347.问：调用ModifyAlgoOrder()修改已有算法单的报单数量后，如何查看最新的委托数量呢**

> 答：OnStrategySymbolStateReport()会有回调响应，XTPStrategySymbolStateReportStruct.m_strategy_qty 返回修改后的策略总数量 。

**348.问：XTP信用业务支持债转股吗？如何报单债转股**

> 答：现货和信用都支持债转股，还是调用InsertOrder()接口报单，business_type 填 XTP_BUSINESS_TYPE_BOND_SWAP_STOCK，side 填 XTP_SIDE_SELL， price_type 填 XTP_PRICE_LIMIT，价格可以填0，开平方向填0。

**349.问：可转债转股后的股票证券代码、转股价格，是调用哪个接口查询？**

> 答：可调用QueryBondSwapStockInfo()查询可转债转股的基本信息，但是深交所没有转股价格，XTPQueryBondSwapStockRsp.swap_price赋值是0。

**350.问：报单债转股后，没有OnTradeEvent()回调消息，是正常的吗？**

> 答：是正常的，债转股没有成交回报，如果报单没有报错，OnOrderEvent()返回订单状态已确认，就可以了。

**351.问：沪市逐笔行情中，逐笔状态XTPTickByTickStatus.flag字段有哪些状态值？**

> 答：对于股票产品，交易状态如下：
>- 08:45~9:15， 发 START 标志；
>- 09:15~9:25， 开盘集合竞价阶段，发 OCALL 标志；
>- 09:25~14:57，连续竞价阶段，发 TRADE 标志；
>- 14:57~15:00，收盘集合竞价阶段， 发 CCALL 标志；
>- 15:00 后， 首先发 CLOSE标志， 随后发 ENDTR 标志；
具体请参见交易所行情接口说明。

**352.问：如果需要查询所有的母单及详情，包括策略的委托和执行状态信息，是调用哪个接口呢**

> 答：可以调用QueryStrategy()接口获取，回调消息是OnQueryStrategy()，而且还会推送OnStrategyStateReport()、OnStrategySymbolStateReport()通知获取策略的执行状态信息。
