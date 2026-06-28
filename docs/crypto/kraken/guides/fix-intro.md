---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/fix-intro
api_type: Guide
updated_at: 2026-05-27 19:57:25.279680
---

# FIX Introduction

## Overview

The Financial Information Exchange (FIX) API protocol offered by Kraken Exchange is a standardized and widely adopted messaging protocol designed to facilitate electronic communication between institutional clients and the exchange. Kraken's FIX API is tailored to meet the unique needs of institutional clients, offering a direct and efficient channel for trading cryptocurrencies. It offers access to both the Spot and the Derivatives exchange.

Kraken FIX API allows clients to trade, access liquidity and receive streaming market data. You can find the Rules of Engagement of the Kraken FIX API [here](/api/docs/fix-api/nos-fix).

To get access to our FIX API, please reach out to your Account Manager.

## Key Features

### Messages

Access to real-time prices and order management including the following messages:

  * **Reference data** : InstrumentListRequest and InstrumentList
  * **Order book and trades** : MarketDataRequest, MarketDataFull and incremental snapshot
  * **Trading engine status** : TradingSessionStatusRequest and TradingSessionStatus
  * **Order entry** : NewOrderSingle, OrderCancelRequest and OrderMassCancelRequest
  * **Order status** : OrderStatusRequest and ExecutionReport
  * **Kill switch** : Session-based cancel on disconnect (COD)

### Performance

  * Hosted in proximity to our data center for superior latency
  * Native trading engine integration for fast execution

### Guaranteed Delivery and Recovery

  * Recovery of missed messages and reliable connection maintenance through the FIX resend request mechanism
  * Guaranteed ordering of messages from the client to the trading engine

### User Acceptance Testing (UAT)

  * Test and certify FIX 4.4 in a sandboxed UAT environment before going live
  * Includes the entire Kraken trading stack
  * Validate functionality and compatibility to minimize any integration issues

### Security

  * Advanced encryption and secure authentication
  * Regular infrastructure updates safeguard against potential threats

### Dedicated Support

  * 24/7 support from experienced professionals
  * Comprehensive resources including documentation and support portal

### Session Protocol

The Kraken implementation of the FIX Protocol is based on FIX 4.4.

Please refer to the FIX v4.4 protocol document ( <https://fixtrading.org/standards> ) for details about the FIX Protocol. This protocol layer offers session management capabilities such as establishing a FIX session, authentication, application/administrative messaging over TCP/IP, sequencing of messages, heartbeats and gap fills.

### Hours of Operation  

Both market data and trading sessions will be operated on a 24/7 schedule with a logical session roll over everyday at _**10PM UTC**_. This maintenance will last for 30s everyday and both Trading and Market Data sequence numbers will be reset to `0`.

### Connectivity Details

Before logging into their FIX session, clients must have their incoming IP addresses whitelisted and establish a secure channel to the provided FIX API. Kraken will provide a pair of designated compIDs, URL and ports to establish a FIX session. Trading and market data endpoints will be served over different ports. Connection with the FIX API need to be done using TCP SSL with TLS 1.3.

### Trading Rate limits

Kraken APIs use trading rate limits to protect the APIs against malicious usage, and to protect our markets against order book manipulation.

The full documentation about trading Rate limits is available [here](/api/docs/guides/spot-ratelimits).

### FIX Dictionary

The latest FIX4.4 xml dictionary used to validated the different messages and fields used for the Kraken FIX API can be downloaded [here](/api/assets/files/FIX44-134e693e41c869bb407c5bef71be41da.xml).

  * Overview
  * Key Features
* Messages
* Performance
* Guaranteed Delivery and Recovery
* User Acceptance Testing (UAT)
* Security
* Dedicated Support
* Session Protocol
* Hours of Operation
* Connectivity Details
* Trading Rate limits
* FIX Dictionary