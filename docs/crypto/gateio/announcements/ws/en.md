---
exchange: gateio
source_url: https://www.gate.com/docs/developers/announcements/ws/en
api_type: WebSocket
updated_at: 2026-05-27 20:14:28.983989
---

# Gate Announcement WebSocket v1.0.0

* Python 
  * Golang 

v1.0.0 · Stable


Gate provides a simple announcement push websocket api. When a specified type of announcement is published, it will be pushed to the subscribed client as soon as possible.

##  BaseURL

  * `wss://api.gateio.ws/ws/v4/ann`

#  Changelog

**v0.2.0**

2024-08-05

  * support engine upgrade announcements

**v0.1.0**

2024-05-20

  * support precision announcements

**v0.0.9**

2024-04-15

  * Support rename announcements

**v0.0.8**

2024-04-01

  * Support deposit/withdrawal announcements

**v0.0.6**

2023-07-26

  * Release for the first time, supporting Simplified Chinese and English announcement push

#  Announcement Push API

##  Request Fields

Request FieldsField | Type | Description  
---|---|---  
time | Integer | Request timestamp  
channel | String | Announcement channel name  
event | String | Event type，`subscribe` or `unsubscribe`  
payload | Object | Language of announcement，`cn` or `en` or both  
  
###  Channel Type

  * `announcement.ping`: service liveness check
  * `announcement.summary_listing`: subscribe listing announcement
  * `announcement.summary_delisting`: subscribe delisting announcement
  * `announcement.summary_fee`: subscribe fee announcement
  * `announcement.summary_etf`: subscribe etf announcement
  * `announcement.summary_deposit_withdrawal`: subscribe deposit/withdrawal announcement
  * `announcement.summary_rename`: subscribe rename announcement
  * `announcement.summary_precision`: subscribe precision announcement
  * `announcement.summary_engine_upgrade`: subscribe engine upgrade announcement

##  Response Fields

Response FieldsField | Type | Description  
---|---|---  
time | Integer | Timestamp  
time_ms | Integer | Timestamp (millisecond)  
channel | String | Channel name  
event | String | Event type  
result | Object | Announcement result  
lang | string | Language of announcement  
origin_url | string | Announcement origin url  
title | string | Announcement title  
brief | string | Announcement brief  
published_at | Integer | Announcement published timestamp  
      
    
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
    
    	// build the request body
    	request := Request{
    		Time:    time.Now().Unix(),
    		Channel: "announcement.summary_listing",
    		Event:   "subscribe",
    		Payload: []string{"cn"},
    	}
    
    	// send request
    	if err := conn.WriteJSON(request); err != nil {
    		log.Fatal("Failed to send WebSocket request:", err)
    	}
    
    	// receive response
    	var response Response
    	if err := conn.ReadJSON(&response); err != nil {
    		log.Fatal("Failed to read WebSocket response:", err)
    	}
    
    	log.Printf("%#v\n", response)
    }
    
    

  * Request Example

    
    
    {
      "time": 1659956033,
      "channel": "announcement.summary_listing",
      "event": "subscribe",
      "payload": ["en"]
    }
    

  * Response Example

    
    
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