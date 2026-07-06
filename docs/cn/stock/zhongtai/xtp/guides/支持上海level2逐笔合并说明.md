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
id: zhongtai-xtp-2074064397487140865
title: 支持上海Level2逐笔合并说明
doc_id: 2074064397487140865
doc_category: 使用建议
source_url: 'https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2074064397487140865'
page_url: 'https://xtp.zts.com.cn/doc/api/xtpDoc'
updated_at: 2026-07-06
---

# 支持上海Level2逐笔合并说明

## XTP支持上海Level2逐笔合并说明


### 一、 逐笔合并后逐笔结构体及字段说明


#### 1.逐笔合并后新增逐笔状态消息


![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2074064397487140865&imagePath=1.png)

上交所逐笔合并行情中，逐笔消息类型有三种：逐笔成交、逐笔委托以及新增的逐笔状态消息，QuoteAPI中的**逐笔状态类型XTPTickByTickStatus结构体**就是用于表示逐笔状态消息。

XTPTickByTickStatus由三个字段组成：
1、**channel_no**表示频道代码，对应上交所逐笔合并数据中的Channel字段；
2、**seq**表示逐笔序号，对应上交所逐笔合并数据中的BizIndex字段；
3、**flag**表示状态信息，当逐笔消息为逐笔状态类型时，对应与TickBSFlag字段，可以表示为START–启动、OCALL–开市集合竞价、TRADE–连续自动撮合、SUSP–停牌、CCALL–收盘集合竞价、CLOSE–闭市、ENDTR–交易结束。

#### 2.逐笔合并后的逐笔序号说明


逐笔合并后，逐笔委托消息、逐笔成交消息以及逐笔状态消息均属于逐笔合并消息，同一个channel下，**逐笔序号是统一的**：**XTPTBT.seq == XTPTickByTickEntrust.seq/XTPTickByTickTrade.seq/XTPTickByTickStatus.seq**，逐笔消息中seq字段均对应于上交所逐笔合并数据中的BizIndex字段，在同一个Channel中连续，从1开始。因此逐笔合并后，逐笔委托，逐笔成交以及逐笔状态消息是有序的，用户无需再排序。

### 二、逐笔合并后使用注意事项


#### 1.确认api版本


若使用上交所逐笔合并行情，请将api更新至**2.2.32.2及以上版本**。

若使用上交所逐笔合并行情时，api为2.2.32.2之前的版本，则仅推送逐笔委托和逐笔成交消息，**无法解析和推送逐笔状态消息**，因此逐笔序号会不连续，无法通过逐笔序号判断接收到的逐笔委托和逐笔成交消息是否发生丢包。

#### 2.去除原有的排序逻辑


上交所逐笔合并行情为有序行情，用户需要修改原程序中对逐笔消息先排序后使用的逻辑，去除排序逻辑。

#### 3.增加逐笔状态处理逻辑


逐笔合并后，上交所推送的逐笔消息中新增了逐笔状态消息，在处理通过QuoteSPI的回调函数OnTickByTick()推送的逐笔数据时，可以先根据XTPTBT.type字段判断消息类型，然后**增加处理逐笔状态消息的代码**，比如新增红框case处理语句处理逐笔状态消息。
![avatar](https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getImageStream?id=2074064397487140865&imagePath=2-3.png)

#### 4.修改判断丢包逻辑


逐笔合并后，逐笔委托、逐笔成交以及逐笔状态消息的逐笔序号是统一的，用户需要修改原程序中判断逐笔消息丢包的逻辑，通过XTPTBT.seq字段判断逐笔消息是否丢包。
