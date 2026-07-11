---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-websocket-overview
anchor_id: overview-websocket-overview
api_type: WebSocket
updated_at: 2026-07-11 19:11:55.795592
---

# Overview

WebSocket is a new HTML5 protocol that achieves full-duplex data transmission between the client and server, allowing data to be transferred effectively in both directions. A connection between the client and server can be established with just one handshake. The server will then be able to push data to the client according to preset rules. Its advantages include:

  * The WebSocket request header size for data transmission between client and server is only 2 bytes.
  * Either the client or server can initiate data transmission.
  * There's no need to repeatedly create and delete TCP connections, saving resources on bandwidth and server.

We recommend developers use WebSocket API to retrieve market data and order book depth.

---

# 概述

WebSocket是HTML5一种新的协议（Protocol）。它实现了用户端与服务器全双工通信， 使得数据可以快速地双向传播。通过一次简单的握手就可以建立用户端和服务器连接， 服务器根据业务规则可以主动推送信息给用户端。其优点如下：

  * 用户端和服务器进行数据传输时，请求头信息比较小，大概2个字节。
  * 用户端和服务器皆可以主动地发送数据给对方。
  * 不需要多次创建TCP请求和销毁，节约宽带和服务器的资源。

强烈建议开发者使用WebSocket API获取市场行情和买卖深度等信息。