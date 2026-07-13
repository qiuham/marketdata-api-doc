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
id: zhongtai-xtp-2076482918653411329
title: 上交所新债券Level2行情说明
doc_id: 2076482918653411329
doc_category: 使用建议
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2076482918653411329'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-07-13
---

# 上交所新债券Level2行情说明

针对沪深交易所近期推出的新债券行情，XTP API 做了适当调整，具体变化如下：
## 1. 快照行情变化


### 1.1 快照结构体


![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2076482918653411329&imagePath=1.jpg)
#### （1）新增快照数据类型 XTP_MARKETDATA_TYPE_V2


![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2076482918653411329&imagePath=2.jpg)

此字段在原有的快照数据类型基础上做了更详细的划分，以便于客户使用。

XTPMD.data_type_v2 = XTP_MARKETDATA_V2_INDEX 时，XTPMD 的联合体无效；

XTPMD.data_type_v2 = XTP_MARKETDATA_V2_OPTION 时，XTPMD.opt 有效；

XTPMD.data_type_v2 = XTP_MARKETDATA_V2_ACTUAL 时，XTPMD.stk 有效；

XTPMD.data_type_v2 = XTP_MARKETDATA_V2_BOND 时，XTPMD.bond 有效；

#### （2）新增债券专用结构体 XTPMarketDataBondExData


此结构体仅保留了债券快照的字段。

仅在 XTPMD.data_type_v2 = XTP_MARKETDATA_V2_BOND 时生效。

![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2076482918653411329&imagePath=3.jpg)

### 1.2 XTPMD.ticker_status 含义变化


上交所新债券 Level2 行情系统上线后，对于沪市新债券 Level2 快照行情， XTPMD.ticker_status 不再有意义，请使用 XTPMD.bond.instrument_status 替代判断（参阅 1.3 章节说明）。

上交所新债券 Level2 行情快照中，有个独有字段 instrument_status，标识当前债券所处的交易状态，此字段对应含义如下：

| 字段 | 含义 | 时间段 |
| ------ | ------ | ------ |
| ADD | 产品未上市 |  |
| START | 启动 | 8:45~9:15 |
| OCALL | 开市集合竞价 | 9:15~9:25 |
| TRADE | 连续自动撮合 | 债券现券：9:25~15:00，债券回购：9:25~15:30 |
| SUSP | 停牌 |  |
| CLOSE | 闭市，自动计算闭市价格 | 债券现券：15:00 先到，债券回购：15:30 先到 |
| ENDTR | 交易结束 | 债券现券：15:00 后到，债券回购：15:30 后到 |

交易状态说明如下：
#### （1）对于债券现券产品：


8:45~9:15 发 START 标志；

9:15~9:25 是开盘集合竞价就阶段，发 OCALL 标志；

9:25~15:00 是连续竞价阶段，发 TRADE 标志；

15:00 后，首先发 CLOSE 标志，随后发 ENDTR 标志。

#### （2）对于债券回购产品：


8:45~9:15 发 START 标志；

9:15~9:25 是开盘集合竞价就阶段，发 OCALL 标志；

9:25~15:30 是连续竞价阶段，发 TRADE 标志；

15:30 后，首先发 CLOSE 标志，随后发 ENDTR 标志。

#### （3）Level2 没有全市场收盘标志，只有每只证券的收盘标志。


如果某证券当天停牌，则在当天先后收到 SUSP、CLOSE 及 ENDTR 标志；如果某证券连续停牌，则可以收到该证券快照及 SUSP 标志，且始终保持 SUSP 标志。

## 2.逐笔行情变化


上交所的新债券逐笔行情使用 801 通道，同时增加了状态订单，债券的逐笔成交、逐笔委托、逐笔状态行情三者进行了统一编号。用户可以通过 channel_no=801 过滤出债券逐笔行情，进行单独处理。

### 2.1 逐笔结构体


![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2076482918653411329&imagePath=4.jpg)

![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2076482918653411329&imagePath=5.jpg)

逐笔行情结构体 XTPTBT 中新增了逐笔状态订单 XTPTBT.state

### 2.2 逐笔数据枚举类型


![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2076482918653411329&imagePath=6.jpg)

XTP_TBT_TYPE 新增了逐笔状态订单类型

### 2.3 XTPTBT.state.flag 字段含义


同本文 1.2 章节的 instrument_status 含义

### 2.4 XTPTBT.trade.seq 和 XTPTBT.entrust.seq 字段含义变化


对于上海的新债券行情来说，XTPTBT.trade.seq 和 XTPTBT.entrust.seq 这 2 个字段不再各自排序，而是与 XTPTBT.state.seq 三者一起在同一个 channel_no（801）内统一连续排序。

深圳的逐笔行情不变，仅 channel_no 有变化。

### 2.5 逐笔委托含义变化


之前上海债券的逐笔委托数据是经过一次撮合后的剩余数据，在新债券行情上线后：

（1）逐笔委托数据变为原始订单数据。

（2）集合竞价及停牌期间不发送逐笔委托数据，到集合竞价或停牌结束时统一发送期间的逐笔委托数据。

（3）涉及交易状态改变产生的集中撮合成交数据在产品状态订单之前发布。

## 3.哪些用户需要修改程序


当交易所上线新债券行情后，用户需要针对不同情况做调整，具体如下：

### 3.1 Level1 用户


无影响，可以不做升级。

### 3.2 使用 2.2.32 以前版本的 Level2 用户


按照客户交易偏好，有如下情形：

#### （1）不做债券交易（可转债、国债逆回购）或仅做深交所债券交易


可自行判断影响，选择升级与否。

上交所新债券 Level2 行情系统上线后，旧版的 api 将无法识别新增的上交所新债券行情，需用户自行判断当收到的逐笔数据 XTPTBT.type > XTP_TBT_TRADE时，是否会影响已有的程序逻辑，如果有影响，可以按照 channel_no==801 过滤掉上交所新债券逐笔行情。如果无影响，可不修改。

快照的 XTPMD.ticker_status 字段在沪市债券快照中不再有意义，需用户自行判断是会否会有影响。如果有影响，且在不升级 API 的情况下，可以按照(XTPMD.r4== 3) &&(XTPMD.exchange_id == XTP_EXCHANGE_SH)将沪市新债券快照行情过滤掉。

#### （2）有上交所债券交易


必须升级至 2.2.32 以上版本，并修改程序适配新的行情。

上交所此次行情升级不是兼容性升级，旧版的行情数据在新系统上线后不再提供，如果不升级 API，将会导致收不到正确的上交所新债券 Level2 行情数据。

### 3.3 从旧版升级至 2.2.32 以上版本的 Level2 用户


按照行情不同数据类型，有如下改动：

#### （1）深市债券行情


基本上没有变化，仅 channel_no 做了改变，对于深圳债券的程序处理逻辑可以不用变化，也可以根据 XTPMD.data_type_v2 以及 XTPMD.bond 来修改程序处理逻辑。

#### （2）沪市新债券Level2 行情


变化很大，需要根据新的行情数据来修改程序处理逻辑。
* 逐笔行情：按照 channel_no=801 过滤出上交所的新债券逐笔行情，单独处理。注意：上交所新债券的逐笔委托、逐笔成交、逐笔状态三者有统一连续编号，不再各自编号。
* 快照行情：XTPMD.ticker_status 字段在沪市新债券 Level2 快照中不再有意义，请使用 XTPMD.bond.instrument_status 替代判断（参阅 1.3 章节说明）。
