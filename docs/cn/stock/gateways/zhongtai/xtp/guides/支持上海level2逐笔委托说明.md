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
id: zhongtai-xtp-2056206187912810498
title: 支持上海Level2逐笔委托说明
doc_id: 2056206187912810498
doc_category: 使用建议
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2056206187912810498'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-05-18
---

# 支持上海Level2逐笔委托说明

- [一、QuoteAPI关于SHL2行情数据说明](#一quoteapi关于shl2行情数据说明)
- [二、盘后测试环境说明](#二盘后测试环境说明)
- [三、实盘环境说明](#三实盘环境说明)


### 一、QuoteAPI关于SHL2行情数据说明


#### 1. SHL2逐笔数据结构体


```cpp
///逐笔委托
struct XTPTickByTickEntrust {
    ///频道代码
    int32_t channel_no;
    ///SH: 委托序号(委托单独编号, 同一channel_no内连续)
    ///SZ: 委托序号(委托成交统一编号, 同一channel_no内连续)
    int64_t seq;
    ///委托价格
    double  price;
    ///SH: 剩余委托数量(balance)
    ///SZ: 委托数量
    int64_t qty;
    ///SH: 'B':买; 'S':卖
    ///SZ: '1':买; '2':卖; 'G':借入; 'F':出借
    char  side;
    ///SH: 'A': 增加; 'D': 删除
    ///SZ: 订单类别: '1': 市价; '2': 限价; 'U': 本方最优
    char ord_type;
    ///SH: 原始订单号
    ///SZ: 无意义
    int64_t order_no;
};

///逐笔成交
struct XTPTickByTickTrade {
    ///频道代码
    int32_t channel_no;
    ///SH: 成交序号(成交单独编号, 同一channel_no内连续)
    ///SZ: 成交序号(委托成交统一编号, 同一channel_no内连续)
    int64_t seq;
    ///成交价格
    double price;
    ///成交量
    int64_t qty;
    ///成交金额(仅适用上交所)
    double money;
    ///买方订单号
    int64_t bid_no;
    ///卖方订单号
    int64_t ask_no;
    /// SH: 内外盘标识('B':主动买; 'S':主动卖; 'N':未知)
    /// SZ: 成交标识('4':撤; 'F':成交)
    char trade_flag;
};

///逐笔状态订单
struct XTPTickByTickStatus {
    ///频道代码
    int32_t channel_no;
    ///同一channel_no内连续
    int64_t seq;
    ///状态信息
    char flag[8];
};

///逐笔数据信息
typedef struct XTPTickByTickStruct {
    ///交易所代码
    XTP_EXCHANGE_TYPE exchange_id;
    ///合约代码（不包含交易所信息），不带空格，以'\0'结尾
    char ticker[XTP_TICKER_LEN];
    /// SH: 业务序号（委托成交统一编号，同一个channel_no内连续，此seq区别于联合体内的seq，channel_no等同于联合体内的channel_no）
    /// SZ: 无意义
    int64_t seq;
    ///委托时间 or 成交时间
    int64_t data_time;
    ///委托 or 成交
    XTP_TBT_TYPE type;

    union {
        XTPTickByTickEntrust entrust;
        XTPTickByTickTrade     trade;
        XTPTickByTickStatus    state;
    };
} XTPTBT;
```

**（1）**：针对上交所Level2逐笔行情，目前有三种消息类型：**XTPTickByTickEntrust逐笔委托消息**、**XTPTickByTickTrade逐笔成交消息**以及**XTPTickByTickStatus逐笔状态消息**，三种消息均是通过QuoteSPI中的回调函数OnTickByTick()进行推送。在接收逐笔行情时，客户可以通过XTPTBT.type字段判定消息类型，然后再对逐笔消息进行处理。

**（2）**：逐笔合并前，仅推送逐笔成交消息和逐笔委托消息，**不推送XTPTickByTickStatus逐笔状态消息**；逐笔合并后，才会推送三种逐笔消息，因此在接收逐笔消息时，请确定行情是否为逐笔合并行情。

**（3）**：逐笔合并前后，逐笔委托、逐笔成交、逐笔状态以及逐笔数据信息结构体中的seq有不同的意义（具体说明参见2），因此使用前需确定行情是否为逐笔合并行情；逐笔委托和逐笔成交的先后顺序，直接会影响原始报单数量的计算（具体说明参见3），因此逐笔合并前请根据XTPTBT.seq字段对逐笔消息进行排序，排序完成后再进行处理；逐笔合并后逐笔委托、逐笔成交以及逐笔状态消息是有序的，用户无需再排序。

#### 2. 上交所逐笔序号seq的说明


**（1）**：**逐笔合并前**，仅有逐笔委托和逐笔成交消息，在同一个channel中**有不同的seq**：

（a）XTPTBT.seq表示逐笔委托和逐笔成交的统一编号，对应上交所逐笔数据中的BizIndex字段，从1开始，按channel连续；

（b）XTPTickByTickEntrust.seq表示逐笔委托序号，对应上交所逐笔委托中的OrderIndex字段，从1开始，按channel连续；

（c）XTPTickByTickTrade.seq表示逐笔成交序号，对应上交所逐笔委托数据中的TradeIndex字段，从1开始，按channel连续；

逐笔合并前逐笔委托消息与逐笔成交消息属于不同的消息，逐笔序号相互独立，**没有固定的到达先后次序关系**，需通过XTPTBT.seq字段判断逐笔委托消息与逐笔成交消息产生的先后顺序。

**（2）**：**逐笔合并后**，逐笔委托、逐笔成交以及逐笔状态消息均属于逐笔合并消息，同一个channel下，有**统一的seq**：**XTPTBT.seq == XTPTickByTickEntrust.seq/XTPTickByTickTrade.seq/XTPTickByTickStatus.seq**，均对应于上交所逐笔合并数据中的BizIndex字段，从1开始，同一个Channel中连续。因此逐笔合并后逐笔委托、逐笔成交以及逐笔状态消息是有序的，用户无需再排序。

#### 3. 上交所逐笔数据中qty的说明


上交所的逐笔委托数据中的qty数量不同于深交所逐笔委托数据中的qty，它代表的是经过一次成交撮合后剩余数量：**上交所收到一笔委托订单后，首先进行一次撮合，然后推送撮合后产生的成交数据，最后推送剩余的委托数据**，后续撮合再产生的剩余委托就不再发送。当某一个订单经过一次撮合全部成交的话，就没有对应的逐笔委托数据，只有逐笔成交数据。

（1）假如订单原始报单数量是1000，第一次撮合后，全成。此种情况下，对于这笔报单，只会有一笔qty=1000的逐笔成交。

（2）假如订单原始报单数量是1000，第一次撮合后，部成200。此种情况下，对于这笔报单，会先有一笔qty=200的逐笔成交，后有一笔qty=800的逐笔委托。

（3）假如订单原始报单数量是1000，第一次撮合后，没有任何成交，后续撮合的时候部成200。此种情况下，对于这笔报单，会先有一笔qty=1000的逐笔委托，后有一笔qty=200的逐笔成交。

（4）假如订单原始报单数量是1000，第一次撮合后，部成了200，然后撤单800。此种情况下，对于这笔报单，会先有一笔qty=200的逐笔成交，后有一笔qty=800，XTPTickByTickEntrust.ord_type=’A’的逐笔委托，最后有一笔qty=800，XTPTickByTickEntrust.ord_type=’D’的撤单逐笔委托。

由上面4种情况可以看出，不同的委托和成交顺序，代表的意思不同。因此**逐笔合并前**处理数据时，请根据XTPTBT.seq字段对逐笔消息进行排序，然后再进行处理；**逐笔合并后**，无需对逐笔消息排序，可直接处理。

### 二、盘后测试环境说明


在上海金桥机房和深圳南方中心机房，分别启动行情测试服务器，供客户测试上交所Level2的行情数据。

行情测试服务器将在盘后对含有SHL2行情数据的历史数据进行回放，并使用组播对外推送行情，具体服务器接入地址和端口号，请以测试环境邮件为准。

行情测试服务器采用多个组播组（2个）方式对外组播，具体组播安排情况，请以测试环境邮件为准。

### 三、实盘环境说明


实盘L2服务器有目前有4个组播组推送上交所行情，分别是TBT逐笔数据、MD行情快照数据、OrderBook数据以及OPTMD期权行情数据。

如果绑核话，需要绑定8个核（MD的接收线程和UDP解析线程各一个，TBT的接收线程和UDP解析线程各一个，OB的接收线程和UDP解析线程各一个以及OPTMD接收线程和UDP解析线程各一个）

目前实盘回调函数线程如下：

![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2056206187912810498&imagePath=4.png)
