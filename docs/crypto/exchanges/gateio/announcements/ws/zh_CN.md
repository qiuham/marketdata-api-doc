---
exchange: gateio
source_url: https://www.gate.com/docs/developers/announcements/ws/zh_CN
api_type: WebSocket
updated_at: 2026-05-27 20:14:32.970295
---

# Gate Announcement WebSocket v1.0.0

* Python 
  * Golang 

v1.0.0 · Stable


Gate 提供一个简单的公告推送接口，当指定类型的公告发布时，会第一时间推送到所订阅的客户端。

##  访问链接

  * `wss://api.gateio.ws/ws/v4/ann`

#  Changelog

**v0.2.0**

2024-08-05

  * 支持引擎升级类型公告推送

**v0.1.0**

2024-05-20

  * 支持精度类型公告推送

**v0.0.9**

2024-04-15

  * 支持更名类型公告推送

**v0.0.8**

2024-04-01

  * 支持充提币公告推送

**v0.0.6**

2023-07-26

  * 初次上线，支持简体中文和英文公告推送

#  公告推送

##  请求字段

请求字段字段名 | 类型 | 描述  
---|---|---  
time | Integer | 请求时间戳  
channel | String | 订阅频道  
event | String | 事件类型，`subscribe` 或 `unsubscribe`  
payload | Object | 公告的语言，`cn` 或 `en`  
  
###  订阅频道

  * `announcement.ping`: 服务存活检查
  * `announcement.summary_listing`: 订阅上新的公告
  * `announcement.summary_delisting`: 订阅下架的公告
  * `announcement.summary_fee`: 订阅费率相关公告
  * `announcement.summary_etf`: 订阅 ETF 相关公告
  * `announcement.summary_deposit_withdrawal`: 订阅充提币相关公告
  * `announcement.summary_rename`: 订阅重命名相关公告
  * `announcement.summary_precision`: 订阅精度相关公告
  * `announcement.summary_engine_upgrade`: 订阅引擎升级相关公告

##  响应字段

响应字段字段名 | 类型 | 描述  
---|---|---  
time | Integer | 时间戳  
time_ms | Integer | 时间戳（毫秒级）  
channel | String | 通道名称  
event | String | 事件类型  
result | Object | 响应结果对象  
lang | String | 语言类型  
origin_url | String | 公告原始链接  
title | String | 标题  
brief | String | 简介  
published_at | Integer | 发布时间戳  
      
    
    import time
    import json
    
    # pip install websocket_client
    from websocket import create_connection
    
    ws = create_connection("wss://api.gateio.ws/ws/v4/ann")
    ws.send(json.dumps({
        "time": int(time.time()),
        "channel": "announcement.summary_listing",
        "event": "subscribe",
        "payload": ["en"]
    }))
    print(ws.recv())
    
    
    
    package main
    
    import (
    	"log"
    	"time"
    
    	"github.com/gorilla/websocket"
    )
    
    type Request struct {
    	Time    int64    `json:"time"`
    	Channel string   `json:"channel"`
    	Event   string   `json:"event"`
    	Payload []string `json:"payload"`
    }
    
    type Response struct {
    	Time    int64  `json:"time"`
    	TimeMs  int64  `json:"time_ms"`
    	Channel string `json:"channel"`
    	Event   string `json:"event"`
    	Result  struct {
    		Status string `json:"status"`
    	} `json:"result"`
    }
    
    func main() {
    	conn, _, err := websocket.DefaultDialer.Dial("wss://api.gateio.ws/ws/v4/ann", nil)
    	if err != nil {
    		log.Fatal("Failed to connect to WebSocket server:", err)
    	}
    	defer conn.Close()
    
    	// 构建请求报文
    	request := Request{
    		Time:    time.Now().Unix(),
    		Channel: "announcement.summary_listing",
    		Event:   "subscribe",
    		Payload: []string{"cn"},
    	}
    
    	// 发送请求报文
    	if err := conn.WriteJSON(request); err != nil {
    		log.Fatal("Failed to send WebSocket request:", err)
    	}
    
    	// 接收响应报文
    	var response Response
    	if err := conn.ReadJSON(&response); err != nil {
    		log.Fatal("Failed to read WebSocket response:", err)
    	}
    
    	log.Printf("%#v\n", response)
    }
    
    

  * 请求示例

    
    
    {
      "time": 1659956033,
      "channel": "announcement.summary_listing",
      "event": "subscribe",
      "payload": ["en"]
    }
    

  * 响应示例

    
    
    {
      "time": 1690365913,
      "time_ms": 1690365913056,
      "channel": "announcement.summary_listing",
      "event": "update",
      "result": {
        "lang": "en",
        "origin_url": "https://www.gate.com/article/228103",
        "title": "Gate will commence Worldcoin(WLD) Trading at 7:30am UTC 24th July 2023 test",
        "brief": "Gate is going to Gate will commence Worldcoin(WLD) Trading at 7:30am UTC 24th July 2023\r\n\r\nToken symbol：WLD\r\nWebsite：https://worldcoin.org/\r\nToken Contract : Erc20: 0x163f8c2467924be0ae7b5347228cabf260318753\r\nOptimism: 0xdc6ff44d5d932cbd77b52e5612ba0529dc6226f1\r\n\r\nDeposit Worldcoin (WLD) at https://www.gate.com/myaccount/deposit/WLD\r\nTrade Worldcoin (WLD) in USDT market via: https://www.gate.com/trade/WLD_USDT\r\n\r\n\r\nGateway to Crypto\r\nTrade over 1,400 cryptocurrencies safely, quickly and easily on Gate.io\r\n\r\nSign up to enter the crypto gateway and get 40% commission from referrals\r\n\r\nDownload iOS/Android App right now.\r\n\r\nReach out to us!\r\nTwitter: https://twitter.com/gate_io\r\nGateVIP Twitter:https://twitter.com/Gateio_Inst\r\nTelegram: https://t.me/gate_zh\r\nAPI Telegram: https://t.me/gateioapi\r\nInstagram: https://www.instagram.com/gateioglobal\r\nMedium: https://gateio.medium.com/\r\nPodcast: https://gateio.buzzsprout.com/?ch=buzzs\r\n\r\nGate.io Team\r\nJuly 24th, 2023",
        "published_at": 1690365913
      }
    }
    

Last Updated: 4/27/2026, 10:15:14 AM