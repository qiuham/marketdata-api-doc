---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/fix-api
api_type: REST
updated_at: 2026-11-13 20:24:39.300219
---

# FIX API

This API can only be used with the SPOT Exchange.

## General API Information

  * FIX connections require TLS encryption. Please either use native TCP+TLS connection or set up a local proxy such as [stunnel](https://www.stunnel.org/) to handle TLS encryption.
  * APIs have a timeout of 10 seconds when processing a request. If a response from the Matching Engine takes longer than this, the API responds with "Timeout waiting for response from backend server. Send status unknown; execution status unknown." [(-1007 TIMEOUT)](/en/docs/products/spot/errors#-1007-timeout)
    * This does not always mean that the request failed in the Matching Engine.
    * If the status of the request has not appeared in [User Data Stream](/en/docs/products/spot/user-data-stream), please perform an API query for its status.
  * If your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
  * To ensure uninterrupted connectivity, please make sure that your client sends **SNI (Server Name Indication)** during the TLS handshake and performs certificate validation against the intended hostname.  Clients that do not send SNI may receive an unexpected certificate, which can result in TLS handshake or hostname verification failures.



### NodeJS

If you are using Node.js and connecting via raw TLS sockets (`tls.connect()`), you must explicitly set the servername option. Please refer to the sample below:
    
    
    Code
    
    const tls = require("tls");
    const hostname = "fix-dc.binance.com"; //EXAMPLE
    
    const options = {
      host: hostname,
      port: 9002,
      servername: hostname, // enables SNI
    };

Note that: NodeJS doesn't enable SNI by default for TLS (See <https://nodejs.org/api/tls.html#tlsconnectoptions-callback>).  If you are using standard HTTPS libraries in Node.js (e.g., `https.request()`, `axios`, `fetch`), these typically set SNI automatically when connecting via a hostname/URL.

### Other languages/custom TLS implementations

When using custom TLS agents / TLS APIs, ensure you set the equivalent field (often named `server_hostname`, `hostname`, or `ServerName`) to the endpoint hostname so SNI is sent.

**FIX sessions only support Ed25519 keys.**

Please refer to [this tutorial](https://www.binance.com/en/support/faq/how-to-generate-an-ed25519-key-pair-to-send-api-requests-on-binance-6b9a63f1e3384cf48a2eedb82767a69a) on how to set up an Ed25519 key pair.

### FIX API Order Entry sessions

  * Endpoint is: `tcp+tls://fix-oe.binance.com:9000`
  * Supports placing orders, canceling orders, and querying current limit usage.
  * Supports receiving all of the account's [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) and [List Status`<N>`](/en/docs/products/spot/fix-api#liststatus-n).
  * Only API keys with `FIX_API` are allowed to connect.
  * QuickFIX Schema can be found [here](/en/docs/products/spot/fix/schemas/spot-fix-oe.xml).



### FIX API Drop Copy sessions

  * Endpoint is: `tcp+tls://fix-dc.binance.com:9000`
  * Supports receiving all of the account's [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) and [List Status`<N>`](/en/docs/products/spot/fix-api#liststatus-n).
  * Only API keys with `FIX_API` or `FIX_API_READ_ONLY` are allowed to connect.
  * QuickFIX Schema can be found [here](/en/docs/products/spot/fix/schemas/spot-fix-oe.xml).
  * Data in Drop Copy sessions is delayed by 1 second.



### FIX API Market Data sessions

  * Endpoint is: `tcp+tls://fix-md.binance.com:9000`
  * Supports market data streams and active instruments queries.
  * Does not support placing or canceling orders.
  * Only API keys with `FIX_API` or `FIX_API_READ_ONLY` are allowed to connect.
  * QuickFIX Schema can be found [here](/en/docs/products/spot/fix/schemas/spot-fix-md.xml).



### FIX Connection Lifecycle

  * All FIX API sessions will remain open for as long as possible, on a best-effort basis.
  * There is no minimum connection time guarantee; a server can enter maintenance at any time.
    * When a server enters maintenance, a [News `<B>`](/en/docs/products/spot/fix-api#news-b) message will be sent to clients **every 10 seconds until disconnection** , prompting clients to reconnect. Upon receiving this message, a client is expected to establish a new session and close the old one. If the client does not close the old session before the server disconnects it, the server will proceed to log it out and close the session.
  * After connecting, the client must send a Logon `<A>` request. For more information please refer to [How to sign a Logon request](/en/docs/products/spot/fix-api#how-to-sign-logon-a-request).
  * The client should send a Logout `<5>` message to close the session before disconnecting. Failure to send the logout message will result in the session’s `SenderCompID (49)` being unusable for new session establishment for a duration of 2x the `HeartInt (108)` interval.
  * The system allows negotiation of the `HeartInt (108)` value during the logon process. Accepted values range between 5 and 60 seconds.
    * If the server has not sent any messages within a `HeartInt (108)` interval, a [HeartBeat `<0>`](/en/docs/products/spot/fix-api#heartbeat-0) will be sent.
    * If the server has not received any messages within a `HeartInt (108)` interval, a [TestRequest `<1>`](/en/docs/products/spot/fix-api#testrequest-1) will be sent. If the server does not receive a HeartBeat `<0>` containing the expected `TestReqID (112)` from the client within `HeartInt (108)` seconds, the server will send a Logout `<5>` message and close the connection.
    * If the client has not received any messages within a `HeartInt (108)` interval, the client is responsible for sending a TestRequest `<1>` to ensure the connection is healthy. Upon receiving such a TestRequest `<1>`, the server will respond with a Heartbeat `<0>` containing the expected `TestReqID (112)`. If the client does not receive the server’s response within a `HeartInt (108)` interval, the client should close the session and connection and establish new ones.



### API Key Permissions

To access the FIX API order entry sessions, your API key must be configured with the `FIX_API` permission.

To access the FIX Drop Copy sessions, your API key must be configured with either `FIX_API_READ_ONLY` or `FIX_API` permission.

To access the FIX Market Data sessions, your API key must be configured with either `FIX_API` or `FIX_API_READ_ONLY` permission.

**FIX sessions only support Ed25519 keys.**

Please refer to [this tutorial](https://www.binance.com/en/support/faq/how-to-generate-an-ed25519-key-pair-to-send-api-requests-on-binance-6b9a63f1e3384cf48a2eedb82767a69a) on how to set up an Ed25519 key pair.

### On message processing order

The `MessageHandling (25035)` field required in the initial [Logon`<A>`](/en/docs/products/spot/fix-api#logon-request) message controls whether messages from the client may be reordered before they are processed by the Matching Engine.

Mode| Description  
---|---  
`UNORDERED(1)`| Messages from the client are allowed to be sent to the matching engine in any order.  
`SEQUENTIAL(2)`| Messages from the client are always sent to the matching engine in `MsgSeqNum (34)` order.  
  
In all modes, the client's `MsgSeqNum (34)` must increase monotonically, with each subsequent message having a sequence number that is exactly 1 greater than the previous message.

`UNORDERED(1)` should offer better performance when there are multiple messages in flight from the client to the server.

### Response Mode

By default, all concurrent order entry sessions receive all of the account's successful [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) and [ListStatus`<N>`](/en/docs/products/spot/fix-api#liststatus-n) messages, including those in response to orders placed from other FIX sessions and via non-FIX APIs.

Use the `ResponseMode (25036)` field in the initial [Logon`<A>`](/en/docs/products/spot/fix-api#logon-request) message to change this behavior.

  * `EVERYTHING(1)`: The default mode.
  * `ONLY_ACKS(2)`: Receive only ACK messages whether operation succeeded or failed. Disables ExecutionReport push.



### Timing Security

  * All requests require a `SendingTime(52)` field which should be the current timestamp.
  * An additional optional field, `RecvWindow(25000)`, specifies for how long the request stays valid in milliseconds.
    * `RecvWindow(25000)` supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
    * If `RecvWindow(25000)` is not specified, it defaults to 5000 milliseconds only for the Logon`<A>` request. For other requests if unset, the RecvWindow check is not executed.
    * Maximum `RecvWindow(25000)` is 60000 milliseconds.
  * Request processing logic is as follows:


    
    
    Code
    
    serverTime = getCurrentTime()
    if (SendingTime < (serverTime + 1 second) && (serverTime - SendingTime) <= RecvWindow) {
      // begin processing request
      serverTime = getCurrentTime()
      if (serverTime - SendingTime) <= RecvWindow {
        // forward request to Matching Engine
      } else {
        // reject request
      }
      // finish processing request
    } else {
      // reject request
    }

### How to sign Logon `<A>` request

The [Logon`<A>`](/en/docs/products/spot/fix-api#logon-a) message authenticates your connection to the FIX API. This must be the first message sent by the client.

  * The `Username (553)` field is required to contain the API key.
  * The `RawData (96)` field is required to contain a valid signature made with the API key.



The signature payload is a text string constructed by concatenating the values of the following fields in this exact order, separated by the SOH character:

  1. `MsgType (35)`
  2. `SenderCompId (49)`
  3. `TargetCompId (56)`
  4. `MsgSeqNum (34)`
  5. `SendingTime (52)`



Sign the payload using your private key. Encode the signature with **base64**. The resulting text string is the value of the `RawData (96)` field.

Here is a sample Python code implementing the signature algorithm:
    
    
    Code
    
    import base64
    
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives.serialization import load_pem_private_key
    
    def logon_raw_data(private_key: Ed25519PrivateKey,
                       sender_comp_id: str,
                       target_comp_id: str,
                       msg_seq_num: str,
                       sending_time: str):
        """
        Computes the value of RawData (96) field in Logon<A> message.
        """
        payload = chr(1).join([
            'A',
            sender_comp_id,
            target_comp_id,
            msg_seq_num,
            sending_time,
        ])
        signature = private_key.sign(payload.encode('ASCII'))
        return base64.b64encode(signature).decode('ASCII')
    
    
    with open('private_key.pem', 'rb') as f:
        private_key = load_pem_private_key(data=f.read(),
                                           password=None)
    
    raw_data = logon_raw_data(private_key,
                              sender_comp_id='5JQmUOsm',
                              target_comp_id='SPOT',
                              msg_seq_num='1',
                              sending_time='20240612-08:52:21.613')

The values presented below can be used to validate the correctness of the signature computation implementation:

Field| Value  
---|---  
MsgType (35)| `A`  
SenderCompID (49)| `EXAMPLE`  
TargetCompID (56)| `SPOT`  
MsgSeqNum (34)| `1`  
SendingTime (52)| `20240627-11:17:25.223`  
  
The Ed25519 private key used in the example computation is shown below:

The following secret key is provided solely for illustrative purposes. Do not use this key in any real-world application as it is not secure and may compromise your cryptographic implementation. Always generate your own unique and secure keys for actual use.
    
    
    Code
    
    -----BEGIN PRIVATE KEY-----
    MC4CAQAwBQYDK2VwBCIEIIJEYWtGBrhACmb9Dvy+qa8WEf0lQOl1s4CLIAB9m89u
    -----END PRIVATE KEY-----

Computed signature:
    
    
    Code
    
    4MHXelVVcpkdwuLbl6n73HQUXUf1dse2PCgT1DYqW9w8AVZ1RACFGM+5UdlGPrQHrgtS3CvsRURC1oj73j8gCA==

Resulting Logon `<A>` message:
    
    
    Code
    
    8=FIX.4.4|9=247|35=A|34=1|49=EXAMPLE|52=20240627-11:17:25.223|56=SPOT|95=88|96=4MHXelVVcpkdwuLbl6n73HQUXUf1dse2PCgT1DYqW9w8AVZ1RACFGM+5UdlGPrQHrgtS3CvsRURC1oj73j8gCA==|98=0|108=30|141=Y|553=sBRXrJx2DsOraMXOaUovEhgVRcjOvCtQwnWj8VxkOh1xqboS02SPGfKi2h8spZJb|25035=2|10=227|

## Limits

### Message Limits

  * Each connection has a limit on **how many messages can be sent to the exchange**.
  * The message limit **does not count the messages sent in response to the client**.
  * Breaching the message limit results in immediate [Logout `<5>`](/en/docs/products/spot/fix-api#logout-5) and disconnection.
  * To understand current limits and usage, please send a [LimitQuery`<XLQ>`](/en/docs/products/spot/fix-api#limitquery-xlq) message. A [LimitResponse`<XLR>`](/en/docs/products/spot/fix-api#limitresponse-xlr) message will be sent in response, containing information about Order Rate Limits and Message Limits.
  * FIX Order entry sessions have a limit of 10,000 messages every 10 seconds.
  * FIX Drop Copy sessions have a limit of 60 messages every 60 seconds.
  * FIX Market Data sessions have a limit of 2000 messages every 60 seconds.



### Connection Limits

  * Each Account has a limit on how many TCP connections can be established at the same time.
  * The limit is reduced when the TCP connection is closed. If the reduction of connections is not immediate, please wait up to twice the value of `HeartBtInt (108)` for the change to take effect. For example, if the current value of `HeartBtInt` is 5, please wait up to 10 seconds.
  * Upon breaching the limit a [Reject `<3>`](/en/docs/products/spot/fix-api#reject-3) will be sent containing information about the connection limit breach and the current limit.
  * FIX Order Entry limits:
    * 15 connection attempts within 30 seconds
    * Maximum of 10 concurrent TCP connections per account
  * FIX Drop Copy limits:
    * 15 connection attempts within 30 seconds
    * Maximum of 10 concurrent TCP connections per account
  * FIX Market Data limits
    * 300 connection attempts within 300 seconds
    * Maximum of 100 concurrent TCP connections per account
    * A single connection can listen to a maximum of 1000 streams.



### Unfilled Order Count

  * To understand how many orders you have placed within a certain time interval, please send a [LimitQuery`<XLQ>`](/en/docs/products/spot/fix-api#limitquery-xlq) message. A [LimitResponse`<XLR>`](/en/docs/products/spot/fix-api#limitresponse-xlr) message will be sent in response, containing information about Unfilled Order Count and Message Limits.
  * **Please note that if your orders are consistently filled by trades, you can continuously place orders on the API**. For more information, please see [Spot Unfilled Order Count Rules](/en/docs/products/spot/faqs/order_count_decrement).
  * If you exceed the unfilled order count your message will be rejected, and information will be transferred back to you in a reject message specific to that endpoint.
  * **The number of unfilled orders is tracked for each account.**



## Error Handling

Client messages that contain syntax errors, missing required fields, or refer to unknown symbols will be rejected by the server with a [Reject `<3>`](/en/docs/products/spot/fix-api#reject-3) message.

If a valid message cannot be processed and is rejected, an appropriate reject response will be sent. Please refer to the individual message documentation for possible responses.

Please refer to the `Text (58)` and `ErrorCode (25016)` fields in responses for the reject reason.

The list of error codes can be found on the [Error codes](/en/docs/products/spot/errors) page.

## Types

Only printable ASCII characters and SOH are supported.

Type| Description  
---|---  
`BOOLEAN`| Enum: `Y` or `N`.  
`CHAR`| Single character.  
`INT`| Signed 64-bit integer.  
`LENGTH`| Unsigned 64-bit integer.  
`NUMINGROUP`| Unsigned 64-bit integer.  
`PRICE`| Fixed-point number. Precision depends on the symbol definition.  
`QTY`| Fixed-point number. Precision depends on the symbol definition.  
`SEQNUM`| Unsigned 32-bit integer. Rolls over to 0 after reaching its maximum value of 4,294,967,295.  
`STRING`| Sequence of printable ASCII characters.  
`UTCTIMESTAMP`| String representing datetime in UTC.  
  
Supported `UTCTIMESTAMP` formats:

  * `20011217-09:30:47` \- seconds
  * `20011217-09:30:47.123` \- milliseconds
  * `20011217-09:30:47.123456` \- microseconds (always used in messages from the exchange)



Client order ID fields must conform to the regex `^[a-zA-Z0-9-_]{1,36}$`:

  * `ClOrdID (11)`
  * `OrigClOrdID (41)`
  * `MDReqID (262)`
  * `ClListID (25014)`
  * `OrigClListID (25015)`
  * `CancelClOrdID (25034)`



## Message Components

In example messages, the `|` character is used to represent SOH character:
    
    
    Code
    
    8=FIX.4.4|9=113|35=A|34=1|49=SPOT|52=20240612-08:52:21.636837|56=5JQmUOsm|98=0|108=30|25037=4392a152-3481-4499-921a-6d42c50702e2|10=051|

### Header

Appears at the start of every message.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
8| BeginString| STRING| Y| Always `FIX.4.4`.  Must be the first field the message.  
9| BodyLength| LENGTH| Y| Message length in bytes.  Must be the second field in the message.  
35| MsgType| STRING| Y| Must be the third field in the message.  Possible values: `0` \- [HEARTBEAT](/en/docs/products/spot/fix-api#heartbeat-0) `1` \- [TEST_REQUEST](/en/docs/products/spot/fix-api#testrequest-1) `3` \- [REJECT](/en/docs/products/spot/fix-api#reject-3) `5` \- [LOGOUT](/en/docs/products/spot/fix-api#logout-5) `8` \- [EXECUTION_REPORT](/en/docs/products/spot/fix-api#executionreport-8) `9` \- [ORDER_CANCEL_REJECT](/en/docs/products/spot/fix-api#ordercancelreject-9) `A` \- [LOGON](/en/docs/products/spot/fix-api#logon-a) `D` \- [NEW_ORDER_SINGLE](/en/docs/products/spot/fix-api#newordersingle-d) `E` \- [NEW_ORDER_LIST](/en/docs/products/spot/fix-api#neworderlist-e) `F` \- [ORDER_CANCEL_REQUEST](/en/docs/products/spot/fix-api#ordercancelrequest-f) `N` \- [LIST_STATUS](/en/docs/products/spot/fix-api#liststatus-n) `q` \- [ORDER_MASS_CANCEL_REQUEST](/en/docs/products/spot/fix-api#ordermasscancelrequest-q) `r` \- [ORDER_MASS_CANCEL_REPORT](/en/docs/products/spot/fix-api#ordermasscancelreport-r) `XCN` \- [ORDER_CANCEL_REQUEST_AND_NEW_ORDER_SINGLE](/en/docs/products/spot/fix-api#ordercancelrequestandnewordersingle-xcn) `XLQ` \- [LIMIT_QUERY](/en/docs/products/spot/fix-api#limitquery-xlq) `XLR` \- [LIMIT_RESPONSE](/en/docs/products/spot/fix-api#limitresponse-xlr) `B` \- [NEWS](/en/docs/products/spot/fix-api#news-b) `x`\- [INSTRUMENT_LIST_REQUEST](/en/docs/products/spot/fix-api#instrumentlistrequest-x) `y` \- [INSTRUMENT_LIST](/en/docs/products/spot/fix-api#instrumentlist-y) `V` \- [MARKET_DATA_REQUEST](/en/docs/products/spot/fix-api#marketdatarequest-v) `Y` \- [MARKET_DATA_REQUEST_REJECT](/en/docs/products/spot/fix-api#marketdatarequestreject-y) `W` \- [MARKET_DATA_SNAPSHOT](/en/docs/products/spot/fix-api#marketdatasnapshot-w) `X` \- [MARKET_DATA_INCREMENTAL_REFRESH](/en/docs/products/spot/fix-api#marketdataincrementalrefresh) `XAK` \- [ORDER_AMEND_KEEP_PRIORITY_REQUEST](/en/docs/products/spot/fix-api#orderamendkeeppriorityrequest-xak) `XAR` \- [ORDER_AMEND_REJECT](/en/docs/products/spot/fix-api#orderamendreject-xar)  
49| SenderCompID| STRING| Y| Must be unique across an account's active sessions.  Must obey regex: `^[a-zA-Z0-9-_]{1,8}$`  
56| TargetCompID| STRING| Y| A string identifying this TCP connection.On messages from client required to be set to `SPOT`. Must be unique across TCP connections.  Must conform to the regex: `^[a-zA-Z0-9-_]{1,8}$`  
34| MsgSeqNum| SEQNUM| Y| Integer message sequence number.  Values that will cause a gap will be rejected.  
52| SendingTime| UTCTIMESTAMP| Y| Time of message transmission (always expressed in UTC).  
25000| RecvWindow| FLOAT| N| Number of milliseconds after `SendingTime (52)` the request is valid for.  Defaults to `5000` milliseconds in [Logon`<A>`](/en/docs/products/spot/fix-api#logon-request) and has a max value of `60000` milliseconds.  Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
  
### Trailer

Appears at the end of every message.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
10| CheckSum| STRING| Y| Always three-character numeric string, calculated by summing the ASCII values of each preceding character in the message, including start-of-header (SOH) characters.  The resultant sum is divided by 256, with the remainder forming the CheckSum value.  To maintain a fixed length, the CheckSum field is right-justified and zero-padded as needed.  
  
## Administrative Messages

### Heartbeat `<0>`

Sent by the server if there is no outgoing traffic during the heartbeat interval (`HeartBtInt (108)` in [Logon`<A>`](/en/docs/products/spot/fix-api#logon-a)).

Sent by the client to indicate that the session is healthy.

Sent by the client or the server in response to a [TestRequest`<1>`](/en/docs/products/spot/fix-api#testrequest-1) message.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
112| TestReqID| STRING| N| When Heartbeat`<35>` is sent in response to TestRequest`<1>`, must mirror the value in TestRequest`<1>`.  
  
### TestRequest `<1>`

Sent by the server if there is no incoming traffic during the heartbeat interval (`HeartBtInt (108)` in [Logon`<A>`](/en/docs/products/spot/fix-api#logon-a)).

Sent by the client to request a [Heartbeat`<0>`](/en/docs/products/spot/fix-api#heartbeat-0) response.

If the client does not respond to TestRequest`<1>` with Heartbeat`<0>` with a correct `TestReqID (112)` within timeout, the connection will be dropped.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
112| TestReqID| STRING| Y| Arbitrary string that must be included in the Heartbeat`<0>` response.  
  
### Reject `<3>`

Sent by the server in response to an invalid message that cannot be processed.

Sent by the server if a new connection cannot be accepted. Please refer to [Connection Limits](/en/docs/products/spot/fix-api#connection-limits).

Please refer to the `Text (58)` and `ErrorCode (25016)` fields for the reject reason.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
45| RefSeqNum| INT| N| The `MsgSeqNum (34)` of the rejected message that caused issuance of this Reject`<3>`.  
371| RefTagID| INT| N| When present, identifies the field that directly caused the issuance of this Reject`<3>` message.  
372| RefMsgType| STRING| N| The `MsgType (35)` of the rejected message that caused issuance of this Reject`<3>`.  
373| SessionRejectReason| INT| N| A reason for the reject, can be one of the values below.  Usually accompanied by additional Text description  Possible values: `0`\- INVALID_TAG_NUMBER  `1` \- REQUIRED_TAG_MISSING  `2` \- TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE  `3` \- UNDEFINED_TAG  `5` \- VALUE_IS_INCORRECT  `6` \- INCORRECT_DATA_FORMAT_FOR_VALUE  `8` \- SIGNATURE_PROBLEM  `10` \- SENDINGTIME_ACCURACY_PROBLEM  `12` \- XML_VALIDATION_ERROR  `13` \- TAG_APPEARS_MORE_THAN_ONCE  `14` \- TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER  `15` \- REPEATING_GROUP_FIELDS_OUT_OF_ORDER  `16` \- INCORRECT_NUMINGROUP_COUNT_FOR_REPEATING_GROUP `99` \- OTHER  
25016| ErrorCode| INT| N| API error code (see [Error Codes](/en/docs/products/spot/errors)).  
58| Text| STRING| N| Human-readable error message.  
  
### Logon `<A>`

Sent by the client to authenticate the connection. Logon`<A>` must be the first message sent by the client.

Sent by the server in response to a successful logon.

Logon`<A>` can only be sent once for the entirety of the session.

#### Logon Request

Tag| Name| Type| Required| Description  
---|---|---|---|---  
98| EncryptMethod| INT| Y| Required to be `0`.  
108| HeartBtInt| INT| Y| Required to be within range [5, 60]. Heartbeat interval in seconds.  
95| RawDataLength| LENGTH| Y| Length of the `RawData (96)` field that comes strictly after this field.  
96| RawData| DATA| Y| Signature. [How to sign Logon`<A>` request](/en/docs/products/spot/fix-api#how-to-sign-logon-a-request).  
141| ResetSeqNumFlag| BOOLEAN| Y| Required to be `Y`.  
553| Username| STRING| Y| API key. **Only Ed25519 API keys are supported.**  
25035| MessageHandling| INT| Y| Possible values:  `1` \- UNORDERED  `2` \- SEQUENTIAL  Please refer to [On message order processing](/en/docs/products/spot/fix-api#on-message-processing-order) for more information.  
25036| ResponseMode| INT| N| Please refer to [Response Mode](/en/docs/products/spot/fix-api#response-mode).  
9406| DropCopyFlag| BOOLEAN| N| Must be set to 'Y' when logging into Drop Copy sessions.  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=248|35=A|34=1|49=5JQmUOsm|52=20240612-08:52:21.613|56=SPOT|95=88|96=KhJLbZqADWknfTAcp0ZjyNz36Kxa4ffvpNf9nTIc+K5l35h+vA1vzDRvLAEQckyl6VDOwJ53NOBnmmRYxQvQBQ==|98=0|108=30|141=Y|553=W5rcOD30c0gT4jHK8oX5d5NbzWoa0k4SFVoTHIFNJVZ3NuRpYb6ZyJznj8THyx5d|25035=1|10=000|

#### Logon Response

Tag| Name| Type| Required| Description  
---|---|---|---|---  
98| EncryptMethod| INT| Y| Always `0`.  
108| HeartBtInt| INT| Y| Mirrors value from the Logon request.  
25037| UUID| STRING| Y| UUID of the FIX API serving the requests.  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=113|35=A|34=1|49=SPOT|52=20240612-08:52:21.636837|56=5JQmUOsm|98=0|108=30|25037=4392a152-3481-4499-921a-6d42c50702e2|10=051|

### Logout `<5>`

Sent to initiate the process of closing the connection, and also when responding to Logout.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
58| Text| STRING| N|   
  
**Sample messages:**

Logout Request
    
    
    Code
    
    8=FIX.4.4|9=55|35=5|34=3|49=GhQHzrLR|52=20240611-09:44:25.543|56=SPOT|10=249|

Logout Response
    
    
    Code
    
    8=FIX.4.4|9=84|35=5|34=4|49=SPOT|52=20240611-09:44:25.544001|56=GhQHzrLR|58=Logout acknowledgment.|10=212|

### News `<B>`

When the server enters maintenance, a `News` message will be sent to clients **every 10 seconds** , counting down to disconnection. When the countdown ends, clients are logged out and their sessions are closed.

Upon receiving this message, clients are expected to establish a new session and close the old one.

The countdown message sent will be:
    
    
    Code
    
    You'll be disconnected in %d seconds. Please reconnect.

When there are 10 seconds remaining, the following message will be sent:
    
    
    Code
    
    Your connection is about to be closed. Please reconnect.

If the client does not close the old session within 10 seconds of receiving the above message, the server will log it out and close the session.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
148| Headline| STRING| Y|   
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=0000113|35=B|49=SPOT|56=OE|34=4|52=20240924-21:07:35.773537|148=Your connection is about to be closed. Please reconnect.|10=165|

### Resend Request `<2>`

Resend requests are currently not supported.

## Application Messages

### Order Entry Messages

The messages below can only be used for the FIX Order Entry and FIX Drop Copy Sessions.

#### NewOrderSingle `<D>`

Sent by the client to submit a new order for execution.

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

**Unfilled Order Count:** 1

Please refer to [Supported Order Types](/en/docs/products/spot/fix-api#supported-order-types) for supported field combinations.

Many fields become required based on the order type. Please refer to [Supported Order Types](/en/docs/products/spot/fix-api#supported-order-types).

Tag| Name| Type| Required| Description  
---|---|---|---|---  
11| ClOrdID| STRING| Y| `ClOrdID` to be assigned to the order.  
38| OrderQty| QTY| N| Quantity of the order  
40| OrdType| CHAR| Y| See the [table](/en/docs/products/spot/fix-api#supported-order-types) to understand supported order types and the required fields to use them.Possible values:  `1` \- MARKET  `2` \- LIMIT  `3` \- STOP  `4` \- STOP_LIMIT  `P`\- PEGGED  
18| ExecInst| CHAR| N| Possible values:  `6` \- PARTICIPATE_DONT_INITIATE  
44| Price| PRICE| N| Price of the order  
54| Side| CHAR| Y| Side of the order.Possible values:  `1` \- BUY  `2` \- SELL  
55| Symbol| STRING| Y| Symbol to place the order on.  
59| TimeInForce| CHAR| N| Possible values:  `1` \- GOOD_TILL_CANCEL  `3` \- IMMEDIATE_OR_CANCEL  `4` \- FILL_OR_KILL  
111| MaxFloor| QTY| N| Used for iceberg orders, this specifies the visible quantity of the order on the book.  
152| CashOrderQty| QTY| N| Quantity of the order specified in the quote asset units, for reverse market orders.  
847| TargetStrategy| INT| N| The value cannot be less than `1000000`.  
7940| StrategyID| INT| N|   
25001| SelfTradePreventionMode| CHAR| N| Possible values:  `1` \- NONE  `2` \- EXPIRE_TAKER  `3` \- EXPIRE_MAKER  `4` \- EXPIRE_BOTH  `5` \- DECREMENT  `6` \- TRANSFER  
211| PegOffsetValue| FLOAT| N| Amount added to the peg in the context of the PegOffsetType  
1094| PegPriceType| CHAR| N| Defines the type of peg  Possible values:  `4` \- MARKET_PEG  `5` \- PRIMARY_PEG  
835| PegMoveType| CHAR| N| Describes whether peg is fixed or floats. Required for Pegged Orders and must be set to `1` (FIXED)  
836| PegOffsetType| CHAR| N| Type of price peg offset.  Possible values:  `3` \- PRICE_TIER  
1100| TriggerType| CHAR| N| Possible values: `4` \- PRICE_MOVEMENT  
1101| TriggerAction| CHAR| N| Possible values:  `1` \- ACTIVATE  
1102| TriggerPrice| PRICE| N| Activation price for contingent orders. See [table](/en/docs/products/spot/fix-api#supported-order-types)  
1107| TriggerPriceType| CHAR| N| Possible values:  `2` \- LAST_TRADE  
1109| TriggerPriceDirection| CHAR| N| Used to differentiate between StopLoss and TakeProfit orders. See [table](/en/docs/products/spot/fix-api#supported-order-types).Possible values:  `U` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  `D` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  
25009| TriggerTrailingDeltaBips| INT| N| Provide to create trailing orders.  
25032| SOR| BOOLEAN| N| Whether to activate SOR for this order.  
25057| QuoteNotionalLimit| QTY| N| For orders on the BUY side only. Maximum quote-asset notional the order may consume. Cannot be combined with `CashOrderQty (152)`, `SOR (25032)` or `ExecInst (18)` = `6`. See [quoteNotionalLimit FAQ](/en/docs/products/spot/faqs/quoteNotionalLimit).  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=114|35=D|34=2|49=qNXO12fH|52=20240611-09:01:46.228|56=SPOT|11=1718096506197867067|38=5|40=2|44=10|54=1|55=LTCBNB|59=4|10=016|

**Response:**

  * [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) with `ExecType (150)` value `NEW (0)` if the order was accepted.
  * [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) with `ExecType (150)` value `REJECTED (8)` if the order was rejected.
  * [Reject`<3>`](/en/docs/products/spot/fix-api#reject-3) if the message is rejected.



##### Supported Order Types

Order name| Binance OrderType| Side| required field values| required fields with user values  
---|---|---|---|---  
Market order| `MARKET`| BUY or SELL| 40=1||   
Limit order| `LIMIT`| BUY or SELL| 40=2||   
Limit maker order| `LIMIT_MAKER`| BUY or SELL| 40=2|18=6||   
Buy stop loss order| `STOP_LOSS`| BUY| 40=3|1100=4|1101=1|1107=2|1109=U|| 1102  
Buy trailing stop loss order| `STOP_LOSS`| BUY| 40=3|1100=4|1101=1|1107=2|1109=U|| 1102,25009  
Buy stop loss limit order| `STOP_LOSS_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|1109=U|| 1102  
Buy trailing stop loss limit order| `STOP_LOSS_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|1109=U|| 1102,25009  
Sell stop loss order| `STOP_LOSS`| SELL| 40=3|1100=4|1101=1|1107=2|1109=D|| 1102  
Sell trailing stop loss order| `STOP_LOSS`| SELL| 40=3|1100=4|1101=1|1107=2|1109=D|| 1102,25009  
Sell stop loss limit order| `STOP_LOSS_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|1109=D|| 1102  
Sell trailing stop loss limit order| `STOP_LOSS_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|1109=D|| 1102,25009  
Buy take profit order| `TAKE_PROFIT`| BUY| 40=3|1100=4|1101=1|1107=2|1109=D|| 1102  
Buy trailing take profit order| `TAKE_PROFIT`| BUY| 40=3|1100=4|1101=1|1107=2|1109=D|| 1102,25009  
Buy trailing take profit order| `TAKE_PROFIT`| BUY| 40=3|1100=4|1101=1|1107=2|| 25009  
Buy take profit order| `TAKE_PROFIT_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|1109=D|| 1102  
Buy trailing take profit limit order| `TAKE_PROFIT_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|1109=D|| 1102,25009  
Buy trailing take profit limit order| `TAKE_PROFIT_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|| 25009  
Sell take profit order| `TAKE_PROFIT`| SELL| 40=3|1100=4|1101=1|1107=2|1109=U|| 1102  
Sell trailing take profit order| `TAKE_PROFIT`| SELL| 40=3|1100=4|1101=1|1107=2|1109=U|| 1102,25009  
Sell trailing take profit order| `TAKE_PROFIT`| SELL| 40=3|1100=4|1101=1|1107=2|| 25009  
Sell take profit limit order| `TAKE_PROFIT_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|1109=U|| 1102  
Sell trailing take profit limit order| `TAKE_PROFIT_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|1109=U|| 1102,25009  
Sell trailing take profit limit order| `TAKE_PROFIT_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|| 25009  
  
Required fields based on Binance OrderType:

Binance OrderType| Additional mandatory parameters| Additional Information  
---|---|---  
`LIMIT`| 38, 44, 59|   
`MARKET`| 38 OR 152| `MARKET` orders using the `OrderQty (38)` field specifies the amount of the `base asset` the user wants to buy or sell at the market price.  E.g. `MARKET` order on BTCUSDT will specify how much BTC the user is buying or selling.  `MARKET` orders using `quoteOrderQty` specifies the amount the user wants to spend (when buying) or receive (when selling) the `quote` asset; the correct `quantity` will be determined based on the market liquidity and `quoteOrderQty`.  E.g. Using the symbol BTCUSDT:  `BUY` side, the order will buy as many BTC as `quoteOrderQty` USDT can.  `SELL` side, the order will sell as much BTC needed to receive `CashOrderQty (152)` USDT.  
`STOP_LOSS`| 38, 1102 or 25009| This will execute a `MARKET` order when the conditions are met. (e.g. `TriggerPrice (1102)` is met or `TriggerTrailingDeltaBips (25009)` is activated)  
`STOP_LOSS_LIMIT`| 38, 44, 59, 1102 or 25009|   
`TAKE_PROFIT`| 38, 1102 or 25009| This will execute a `MARKET` order when the conditions are met. (e.g. `TriggerPrice (1102)` is met or `TriggerTrailingDeltaBips (25009)` is activated)  
`TAKE_PROFIT_LIMIT`| 38, 44, 59, 1102 or 25009|   
`LIMIT_MAKER`| 38, 44| This is a `LIMIT` order that will be rejected if the order immediately matches and trades as a taker.  This is also known as a POST-ONLY order.  
  
#### ExecutionReport `<8>`

Sent by the server whenever an order state changes.

  * By default, ExecutionReport`<8>` is sent for all orders of an account, including those submitted in different connections. Please see [Response Mode](/en/docs/products/spot/fix-api#response-mode) for other behavior options.
  * FIX API should give better performance for ExecutionReport<8> push.



Tag| Name| Type| Required| Description  
---|---|---|---|---  
17| ExecID| STRING| N| Omitted on rejected orders.  
11| ClOrdID| STRING| N| `ClOrdID` of the list as assigned on the request.  
41| OrigClOrdID| STRING| N| Original `ClOrdID` of the order.  
37| OrderID| INT| N| Assigned by exchange.  
38| OrderQty| QTY| N| Quantity of the order.  
40| OrdType| CHAR| Y| Possible values:  `1` \- MARKET  `2` \- LIMIT  `3` \- STOP_LOSS  `4` \- STOP_LIMIT  `P` \- PEGGED  
54| Side| CHAR| Y| Possible values:  `1` \- BUY  `2` \- SELL  
55| Symbol| STRING| Y| Symbol of the order.  
18| ExecInst| CHAR| N| Possible values:  `6` \- PARTICIPATE_DONT_INITIATE  
44| Price| PRICE| N| Price of the order.  
59| TimeInForce| CHAR| N| Possible values:  `1` \- GOOD_TILL_CANCEL  `3` \- IMMEDIATE_OR_CANCEL  `4` \- FILL_OR_KILL  
60| TransactTime| UTCTIMESTAMP| N| Timestamp when this event occurred.  
25018| OrderCreationTime| INT| N|   
111| MaxFloor| QTY| N| Appears on iceberg orders.  
66| ListID| STRING| N| Appears on list orders.  
152| CashOrderQty| QTY| N| OrderQty specified in the quote asset units.  
847| TargetStrategy| INT| N| `TargetStrategy (847)` from the order placement request.  
7940| StrategyID| INT| N| `StrategyID (7940)` from the order placement request.  
25001| SelfTradePreventionMode| CHAR| N| Possible values:  `1` \- NONE  `2` \- EXPIRE_TAKER  `3` \- EXPIRE_MAKER `4` \- EXPIRE_BOTH  `5` \- DECREMENT  `6` \- TRANSFER  
150| ExecType| CHAR| Y| **Note:** Field `PreventedMatchID(25024)` will be present if order has expired due to `SelfTradePreventionMode(25013)` Possible values:  `0` \- NEW  `4` \- CANCELED  `5` \- REPLACED  `8` \- REJECTED  `F` \- TRADE `C` \- EXPIRED  
14| CumQty| QTY| Y| Total number of base asset traded on this order.  
151| LeavesQty| QTY| N| Quantity remaining for further execution.  
25017| CumQuoteQty| QTY| N| Total number of quote asset traded on this order.  
1057| AggressorIndicator| BOOLEAN| N| Appears on trade execution reports. Indicates whether the order was a taker in the trade.  
1003| TradeID| STRING| N| Appears on trade execution reports.  
31| LastPx| PRICE| N| The price of the last execution.  
32| LastQty| QTY| Y| The quantity of the last execution.  
39| OrdStatus| CHAR| Y| Possible values:  `0` \- NEW  `1` \- PARTIALLY_FILLED  `2` \- FILLED  `4` \- CANCELED `6` \- PENDING_CANCEL `8` \- REJECTED  `A` \- PENDING_NEW  `C` \- EXPIRED  Note that FIX does not support `EXPIRED_IN_MATCH` status, and get converted to `EXPIRED` in FIX.  
70| AllocID| INT| N| Allocation ID as assigned by the exchange.  
574| MatchType| INT| N| Possible values:`1` \- ONE_PARTY_TRADE_REPORT`4` \- AUTO_MATCH  
25021| WorkingFloor| INT| N| Appears for orders that potentially have allocations.  
25022| TrailingTime| UTCTIMESTAMP| N| Appears only for trailing stop orders.  
636| WorkingIndicator| BOOLEAN| N| Set to `Y` when this order enters order book.  
25023| WorkingTime| UTCTIMESTAMP| N| When this order appeared on the order book.  
25024| PreventedMatchID| INT| N| Appears only for orders that expired due to STP.  
25025| PreventedExecutionPrice| PRICE| N| Appears only for orders that expired due to STP.  
25026| PreventedExecutionQty| QTY| N| Appears only for orders that expired due to STP.  
25027| TradeGroupID| INT| N| Appears only for orders that expired due to STP.  
25028| CounterSymbol| STRING| N| Appears only for orders that expired due to STP.  
25029| CounterOrderID| INT| N| Appears only for orders that expired due to STP.  
25030| PreventedQty| QTY| N| Appears only for orders that expired due to STP.  
25031| LastPreventedQty| QTY| N| Appears only for orders that expired due to STP.  
25032| SOR| BOOLEAN| N| Appears for orders that used SOR.  
25057| QuoteNotionalLimit| QTY| N| Appears only if `QuoteNotionalLimit (25057)` was sent on the order.  
25016| ErrorCode| INT| N| API error code (see [Error Codes](/en/docs/products/spot/errors)).  
58| Text| STRING| N| Human-readable error message.  
25056| ExpiryReason| INT| N| Appears only for expired orders. Possible values:`1` \- REJECTED`2` \- EXCHANGE_CANCELED`3` \- OCO_TRIGGER`4` \- OTO_PHASE_ONE_EXPIRED`5` \- UNFILLED_IOC_QUANTITY_EXPIRED`6` \- UNFILLED_FOK_ORDER_EXPIRED`7` \- INSUFFICIENT_LIQUIDITY`8` \- EXECUTION_RULE_PRICE_RANGE_EXCEEDED`9` \- EXHAUSTED`10` \- INSUFFICIENT_QUOTE_NOTIONAL_LIMIT  
25058| EffectiveSelfTradePreventionMode| CHAR| N| Appears only on prevented-match reports when the STP mode the engine applied differs from the order's `SelfTradePreventionMode (25001)`. Possible values:`3` \- EXPIRE_MAKER`4` \- EXPIRE_BOTH`5` \- DECREMENT  
136| NoMiscFees| NUMINGROUP| N| Number of repeating groups of miscellaneous fees.  
=>137| MiscFeeAmt| QTY| Y| Amount of fees denominated in `MiscFeeCurr(138)` asset  
=>138| MiscFeeCurr| STRING| Y| Currency of miscellaneous fee.  
=>139| MiscFeeType| INT| Y| Possible values: `4` \- EXCHANGE_FEES  
1100| TriggerType| CHAR| N| Possible values: `4` \- PRICE_MOVEMENT  
1101| TriggerAction| CHAR| N| Possible values:  `1` \- ACTIVATE  
1102| TriggerPrice| PRICE| N| Activation price for contingent orders. See [table](/en/docs/products/spot/fix-api#supported-order-types)  
1107| TriggerPriceType| CHAR| N| Possible values:  `2` \- LAST_TRADE  
1109| TriggerPriceDirection| CHAR| N| Used to differentiate between StopLoss and TakeProfit orders. See [table](/en/docs/products/spot/fix-api#supported-order-types).Possible values:  `U` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  `D` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  
25009| TriggerTrailingDeltaBips| INT| N| Appears only for trailing stop orders.  
211| PegOffsetValue| FLOAT| N| Amount added to the peg in the context of the PegOffsetType  
1094| PegPriceType| CHAR| N| Defines the type of peg  Possible values:  `4` \- MARKET_PEG  `5` \- PRIMARY_PEG  
835| PegMoveType| CHAR| N| Describes whether peg is fixed or floats. Required for Pegged Orders and must be set to `1` (FIXED)  
836| PegOffsetType| CHAR| N| Type of price peg offset.  Possible values:  `3` \- PRICE_TIER  
839| PeggedPrice| PRICE| N| Current price the order is pegged at  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=330|35=8|34=2|49=SPOT|52=20240611-09:01:46.228950|56=qNXO12fH|11=1718096506197867067|14=0.00000000|17=144|32=0.00000000|37=76|38=5.00000000|39=0|40=2|44=10.00000000|54=1|55=LTCBNB|59=4|60=20240611-09:01:46.228000|150=0|151=5.00000000|636=Y|1057=Y|25001=1|25017=0.00000000|25018=20240611-09:01:46.228000|25023=20240611-09:01:46.228000|10=095|

#### OrderCancelRequest `<F>`

Sent by the client to cancel an order or an order list.

  * To cancel an order either `OrderID (11)` or `OrigClOrdID (41)` are required.
    * If both `OrderID (37)` and `OrigClOrdID (41)` are provided, the `OrderID` is searched first, then the `OrigClOrdID` from that result is checked against that order. If both conditions are not met the request will be rejected.
  * To cancel an order list either `ListID (66)` or `OrigClListID (25015)` are required.
    * If both `ListID (66)` and `OrigClListID (25015)` are provided, the `ListID` is searched first, then the `OrigClListID` from that result is checked against that order. If both conditions are not met the request will be rejected.



If the canceled order is part of an order list, the entire list will be canceled.

**Note:**

  * The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only `orderId` is sent. Sending `origClientOrderId` or both `orderId` \+ `origClientOrderId` will be slower.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
11| ClOrdID| STRING| Y| `ClOrdID` of this request.  
41| OrigClOrdID| STRING| N| `ClOrdID (11)` of the order to cancel.  
37| OrderID| INT| N| `OrderID (37)` of the order to cancel.  
25015| OrigClListID| STRING| N| `ClListID (25014)` of the order list to cancel.  
66| ListID| STRING| N| `ListID (66)` of the order list to cancel.  
55| Symbol| STRING| Y| Symbol on which to cancel order.  
25002| CancelRestrictions| INT| N| Restrictions on the cancel. Possible values:  `1` \- ONLY_NEW  `2` \- ONLY_PARTIALLY_FILLED  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=93|35=F|34=2|49=ieBwvCKy|52=20240613-01:11:13.784|56=SPOT|11=1718241073695674483|37=2|55=LTCBNB|10=210|

**Response:**

  * [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) with `ExecType (150)` value `CANCELED (4)` for each canceled order.
  * [ListStatus`<N>`](/en/docs/products/spot/fix-api#liststatus-n) if orders in an order list were canceled.
  * [OrderCancelReject`<9>`](/en/docs/products/spot/fix-api#ordercancelreject-9) if cancellation was rejected.
  * [Reject`<3>`](/en/docs/products/spot/fix-api#reject-3) if the message is rejected.



#### OrderCancelReject `<9>`

Sent by the server when [OrderCancelRequest`<F>`](/en/docs/products/spot/fix-api#ordercancelrequest-f) has failed.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
11| ClOrdID| STRING| Y| `ClOrdID (11)` of the cancel request.  
41| OrigClOrdID| STRING| N| `OrigClOrdID (41)` from the cancel request.  
37| OrderID| INT| N| `OrderID (37)` from the cancel request.  
25015| OrigClListID| STRING| N| `OrigClListID (25015)` from the cancel request.  
66| ListID| STRING| N| `ListID (66)` from the cancel request.  
55| Symbol| STRING| Y| `Symbol (55)` from the cancel request.  
25002| CancelRestrictions| INT| N| `CancelRestrictions (25002)` from the cancel request.  
434| CxlRejResponseTo| CHAR| Y| Type of request that this OrderCancelReject`<9>` is in response to.  Possible values:  `1` \- ORDER_CANCEL_REQUEST  
25016| ErrorCode| INT| Y| API error code (see [Error Codes](/en/docs/products/spot/errors)).  
58| Text| STRING| Y| Human-readable error message.  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=137|35=9|34=2|49=SPOT|52=20240613-01:12:41.320869|56=OlZb8ht8|11=1718241161272843932|37=2|55=LTCBNB|58=Unknown order sent.|434=1|25016=-1013|10=087|

#### OrderCancelRequestAndNewOrderSingle `<XCN>`

Sent by the client to cancel an order and submit a new one for execution.

  * To cancel an order either `OrderID (11)` or `OrigClOrdId (41)` are required.
  * If both `OrderID (37)` and `OrigClOrdID (41)` are provided, the `OrderID` is searched first, then the `OrigClOrdID` from that result is checked against that order. If both conditions are not met the request will be rejected.



Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

A new order that was not attempted (i.e. when `newOrderResult: NOT_ATTEMPTED`), will still increase the unfilled order count by 1.

**Unfilled Order Count:** 1

Please refer to [Supported Order Types](/en/docs/products/spot/fix-api#supported-order-types) for supported field combinations when describing the new order.

Cancel is always processed first. Then immediately after that the new order is submitted.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
25033| OrderCancelRequestAndNewOrderSingleMode| INT| Y| What action should be taken if cancel fails.  Possible values:  `1` \- STOP_ON_FAILURE  `2` \- ALLOW_FAILURE  
25038| OrderRateLimitExceededMode| INT| N| What should be done to the cancellation request if you exceed the unfilled order rate limit. Possible values: `1` \- DO_NOTHING  `2` \- CANCEL_ONLY  
37| OrderID| INT| N| `OrderID` of the order to cancel.  
25034| CancelClOrdID| STRING| N| `ClOrdID` of the cancel.  
41| OrigClOrdID| STRING| N| `ClOrdID` of the order to cancel.  
11| ClOrdID| STRING| Y| `ClOrdID` to be assigned to the new order.  
25002| CancelRestrictions| INT| N| Restrictions on the cancel. Possible values:  `1` \- ONLY_NEW  `2` \- ONLY_PARTIALLY_FILLED  
38| OrderQty| QTY| N| Quantity of the new order  
40| OrdType| CHAR| Y| See the [table](/en/docs/products/spot/fix-api#supported-order-types) to understand supported order types and the required fields to use them.Possible values:  `1` \- MARKET  `2` \- LIMIT  `3` \- STOP  `4` \- STOP_LIMIT  `P` \- PEGGED  
18| ExecInst| CHAR| N| Possible values:  `6` \- PARTICIPATE_DONT_INITIATE  
44| Price| PRICE| N| Price of the new order  
54| Side| CHAR| Y| Side of the order.Possible values:  `1` \- BUY  `2` \- SELL  
55| Symbol| STRING| Y| Symbol to cancel and place the order on.  
59| TimeInForce| CHAR| N| Possible values:  `1` \- GOOD_TILL_CANCEL  `3` \- IMMEDIATE_OR_CANCEL  `4` \- FILL_OR_KILL  
111| MaxFloor| QTY| N| Used for iceberg orders, this specifies the visible quantity of the order on the book.  
152| CashOrderQty| QTY| N| Quantity of the order specified in the quote asset units, for reverse market orders.  
847| TargetStrategy| INT| N| The value cannot be less than `1000000`.  
7940| StrategyID| INT| N|   
25001| SelfTradePreventionMode| CHAR| N| Possible values:  `1` \- NONE  `2` \- EXPIRE_TAKER  `3` \- EXPIRE_MAKER  `4` \- EXPIRE_BOTH  `5` \- DECREMENT  `6` \- TRANSFER  
211| PegOffsetValue| FLOAT| N| Amount added to the peg in the context of the PegOffsetType  
1094| PegPriceType| CHAR| N| Defines the type of peg  Possible values:  `4` \- MARKET_PEG  `5` \- PRIMARY_PEG  
835| PegMoveType| CHAR| N| Describes whether peg is fixed or floats. Required for Pegged Orders and must be set to `1` (FIXED)  
836| PegOffsetType| CHAR| N| Type of price peg offset.  Possible values:  `3` \- PRICE_TIER  
1100| TriggerType| CHAR| N| Possible values: `4` \- PRICE_MOVEMENT  
1101| TriggerAction| CHAR| N| Possible values:  `1` \- ACTIVATE  
1102| TriggerPrice| PRICE| N| Activation price for contingent orders. See [table](/en/docs/products/spot/fix-api#supported-order-types)  
1107| TriggerPriceType| CHAR| N| Possible values:  `2` \- LAST_TRADE  
1109| TriggerPriceDirection| CHAR| N| Used to differentiate between StopLoss and TakeProfit orders. See [table](/en/docs/products/spot/fix-api#supported-order-types).Possible values:  `U` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  `D` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  
25009| TriggerTrailingDeltaBips| INT| N| Provide to create trailing orders.  
25057| QuoteNotionalLimit| QTY| N| For replacement orders on the BUY side only. Maximum quote-asset notional the new order may consume. Cannot be combined with `CashOrderQty (152)` or with `ExecInst (18)` = `6`. See [quoteNotionalLimit FAQ](/en/docs/products/spot/faqs/quoteNotionalLimit).  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=160|35=XCN|34=2|49=JS8iiXK6|52=20240613-02:31:53.753|56=SPOT|11=1718245913721036458|37=8|38=5|40=2|44=4|54=1|55=LTCBNB|59=1|111=1|25033=1|25034=1718245913721036819|10=229|

**Response:**

  * [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) with `ExecType (150)` value `CANCELED (4)` for the canceled order.
  * [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) with `ExecType (150)` value `NEW (0)` for the new order.
  * [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) with `ExecType (150)` value `REJECTED (8)` if the new order was rejected.
  * [OrderCancelReject`<9>`](/en/docs/products/spot/fix-api#ordercancelreject-9) if the cancellation was rejected.
  * [Reject`<3>`](/en/docs/products/spot/fix-api#reject-3) if the message is rejected.



#### OrderMassCancelRequest `<q>`

Sent by the client to cancel all open orders on a symbol.

All orders of the account will be canceled, including those placed in different connections.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
11| ClOrdID| STRING| Y| `ClOrdId` of this mass cancel request.  
55| Symbol| STRING| Y| Symbol on which to cancel orders.  
530| MassCancelRequestType| CHAR| Y| Possible values:  `1` \- CANCEL_SYMBOL_ORDERS  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=95|35=q|34=2|49=dpYPesqv|52=20240613-01:24:36.948|56=SPOT|11=1718241876901971671|55=BTCUSDT|530=1|10=243|

**Responses:**

  * [ExecutionReport`<8>`](/en/docs/products/spot/fix-api#executionreport-8) with `ExecType (150)` value `CANCELED (4)` for the every order canceled.
  * [OrderMassCancelReport`<r>`](/en/docs/products/spot/fix-api#ordermasscancelreport-r) with `MassCancelResponse (531)` field indicating whether the message is accepted or rejected.
  * [Reject`<3>`](/en/docs/products/spot/fix-api#reject-3) if the message is rejected.



#### OrderMassCancelReport `<r>`

Sent by the server in response to [OrderMassCancelRequest`<q>`](/en/docs/products/spot/fix-api#ordermasscancelrequest-q).

Tag| Name| Type| Required| Description  
---|---|---|---|---  
55| Symbol| STRING| Y| `Symbol (55)` from the cancel request.  
11| ClOrdID| STRING| Y| `ClOrdID (11)` of the cancel request.  
530| MassCancelRequestType| CHAR| Y| `MassCancelRequestType (530)` from the cancel request.  
531| MassCancelResponse| CHAR| Y| Possible values:  `0` \- CANCEL_REQUEST_REJECTED  `1` \- CANCEL_SYMBOL_ORDERS  
532| MassCancelRejectReason| INT| N| Possible values:  `99` \- OTHER  
533| TotalAffectedOrders| INT| N| How many orders were canceled.  
25016| ErrorCode| INT| N| API error code (see [Error Codes](/en/docs/products/spot/errors)).  
58| Text| STRING| N| Human-readable error message.  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=109|35=r|34=2|49=SPOT|52=20240613-01:24:36.949763|56=dpYPesqv|11=1718241876901971671|55=LTCBNB|530=1|531=1|533=5|10=083|

#### NewOrderList `<E>`

Sent by the client to submit a list of orders for execution.

  * OCOs or OTOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.
  * OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.



**Unfilled Order Count:**

  * OCO: 2
  * OTO: 2
  * OTOCO: 3



Orders in an order list are contingent on one another. Please refer to [Supported Order List Types](/en/docs/products/spot/fix-api#supported-order-list-types) for supported order types and triggering instructions.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
25014| ClListID| STRING| Y| `ClListID` to be assigned to the order list.  
1385| ContingencyType| INT| N| Possible values:  `1` \- ONE_CANCELS_THE_OTHER  `2` \- ONE_TRIGGERS_THE_OTHER  
25046| OPO| BOOLEAN| N| Sets this order list as an [OPO](/en/docs/products/spot/faqs/opo) when set to `true`.  
73| NoOrders| NUMINGROUP| N| The length of the array for Orders. Only 2 or 3 are allowed.  
=>11| ClOrdID| STRING| Y| `ClOrdID` to be assigned to the order  
=>38| OrderQty| QTY| N| Quantity of the order  
=>40| OrdType| CHAR| Y| See the [table](/en/docs/products/spot/fix-api#supported-order-types) to understand supported order types and the required fields to use them.Possible values:  `1` \- MARKET  `2` \- LIMIT  `3` \- STOP  `4` \- STOP_LIMIT  `P` \- PEGGED  
=>18| ExecInst| CHAR| N| Possible values:  `6` \- PARTICIPATE_DONT_INITIATE  
=>44| Price| PRICE| N| Price of the order  
=>54| Side| CHAR| Y| Side of the order. Possible values:  `1` \- BUY  `2` \- SELL  
=>55| Symbol| STRING| Y| Symbol to place the order on.  
=>59| TimeInForce| CHAR| N| Possible values:  `1` \- GOOD_TILL_CANCEL  `3` \- IMMEDIATE_OR_CANCEL  `4` \- FILL_OR_KILL  
=>111| MaxFloor| QTY| N| Used for iceberg orders, this specifies the visible quantity of the order on the book.  
=>152| CashOrderQty| QTY| N| Quantity of the order specified in the quote asset units, for reverse market orders.  
=>847| TargetStrategy| INT| N| The value cannot be less than `1000000`.  
=>7940| StrategyID| INT| N|   
=>25001| SelfTradePreventionMode| CHAR| N| Possible values:  `1` \- NONE `2` \- EXPIRE_TAKER  `3` \- EXPIRE_MAKER  `4` \- EXPIRE_BOTH  `5` \- DECREMENT  `6` \- TRANSFER  
=>211| PegOffsetValue| FLOAT| N| Amount added to the peg in the context of the PegOffsetType  
=>1094| PegPriceType| CHAR| N| Defines the type of peg  Possible values:  `4` \- MARKET_PEG  `5` \- PRIMARY_PEG  
=>835| PegMoveType| CHAR| N| Describes whether peg is fixed or floats. Required for Pegged Orders and must be set to `1` (FIXED)  
=>836| PegOffsetType| CHAR| N| Type of price peg offset.  Possible values:  `3` \- PRICE_TIER  
=>1100| TriggerType| CHAR| N| Possible values:  `4` \- PRICE_MOVEMENT  
=>1101| TriggerAction| CHAR| N| Possible values:  `1` \- ACTIVATE  
=>1102| TriggerPrice| PRICE| N| Activation price for contingent orders. See [table](/en/docs/products/spot/fix-api#supported-order-types)  
=>1107| TriggerPriceType| CHAR| N| Possible values:  `2` \- LAST_TRADE  
=>1109| TriggerPriceDirection| CHAR| N| Used to differentiate between StopLoss and TakeProfit orders. See [table](/en/docs/products/spot/fix-api#supported-order-types).Possible values:  `U` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  `D` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  
=>25009| TriggerTrailingDeltaBips| INT| N| Provide to create trailing orders.  
=>25057| QuoteNotionalLimit| QTY| N| For orders on the BUY side only. Maximum quote-asset notional this order may consume. Not allowed on OPO and OPOCO pending orders. Cannot be combined with `CashOrderQty (152)` or with `ExecInst (18)` = `6`. See [quoteNotionalLimit FAQ](/en/docs/products/spot/faqs/quoteNotionalLimit).  
=>25010| NoListTriggeringInstructions| NUMINGROUP| N| The length of the array for ListTriggeringInstructions.  
==>25011| ListTriggerType| CHAR| N| What needs to happen to the order pointed to by ListTriggerTriggerIndex in order for the action to take place.  Possible values:  `1` \- ACTIVATED  `2` \- PARTIALLY_FILLED  `3` \- FILLED  
==>25012| ListTriggerTriggerIndex| INT| N| Index of the trigger order: 0-indexed.  
==>25013| ListTriggerAction| CHAR| N| Action to take place on this order after the ListTriggerType has been fulfilled.  Possible values:  `1` \- RELEASE  `2` \- CANCEL  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=236|35=E|34=2|49=Eg13pOvN|52=20240607-02:19:07.836|56=SPOT|73=2|11=w1717726747805308656|55=LTCBNB|54=2|38=1|40=2|44=0.25|59=1|11=p1717726747805308656|55=LTCBNB|54=2|38=1|40=1|25010=1|25011=3|25012=0|25013=1|1385=2|25014=1717726747805308656|10=171|

#### Supported Order List Types

Orders must be specified in the sequence indicated in the _Order Names_ column in the table below.

Order list name| Contingency Type (1385)| Order names| Order sides| Allowed Binance order types| List Triggering Instructions  
---|---|---|---|---|---  
OCO| `1`| 1\. below order 2\. above order| 1\. below order=`SELL` 2\. above order=`SELL`| 1\. below order=`STOP_LOSS` or `STOP_LOSS_LIMIT` 2\. above order=`LIMIT_MAKER`| 1\. below order: 25010=1|25011=2|25012=1|25013=2|2\. above order: 25010=1|25011=1|25012=0|25013=2|  
OCO| `1`| 1\. below order 2\. above order| 1\. below order=`BUY` 2\. above order=`BUY`| 1\. below order=`LIMIT_MAKER` 2\. above order=`STOP_LOSS` or `STOP_LOSS_LIMIT`| 1\. below order: 25010=1|25011=1|25012=1|25013=2|2\. above order: 25010=1|25011=2|25012=0|25013=2|  
OCO| `1`| 1\. below order 2\. above order| 1\. below order=`SELL` 2\. above order=`SELL`| 1\. below order=`STOP_LOSS` or `STOP_LOSS_LIMIT` 2\. above order= `TAKE_PROFIT`| 1\. below order: 25010=1|25011=1|25012=1|25013=2|2\. above order: 25010=1|25011=1|25012=0|25013=2|  
OCO| `1`| 1\. below order 2\. above order| 1\. below order=`BUY` 2\. above order=`BUY`| 1\. below order=`TAKE_PROFIT` 2\. above order = `STOP_LOSS` or `STOP_LOSS_LIMIT`| 1\. below order: 25010=1|25011=1|25012=1|25013=2|2\. above order: 25010=1|25011=1|25012=0|25013=2|  
OTO| `2`| 1\. working order 2\. pending order| 1\. working order=`SELL` or `BUY` 2\. pending order=`SELL` or `BUY`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending order=ANY| 1\. working order:NONE 2\. pending order: 25010=1|25011=3|25012=0|25013=1|  
OTOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`SELL` or `BUY` 2\. pending below order=`SELL` 3\. pending above order=`SELL`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending below order=`STOP_LOSS` or `STOP_LOSS_LIMIT` 3\. pending above order=`LIMIT_MAKER`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=2|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
OTOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`SELL` or `BUY` 2\. pending below order=`BUY` 3\. pending above order=`BUY`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending below order=`LIMIT_MAKER` 3\. pending above order=`STOP_LOSS` or `STOP_LOSS_LIMIT`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=2|25012=1|25013=2|  
OTOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`SELL` or `BUY` 2\. pending below order=`SELL` 3\. pending above order=`SELL`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending below order=`STOP_LOSS` or `STOP_LOSS_LIMIT` 3\. pending above order=`TAKE_PROFIT`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
OTOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`SELL` or `BUY` 2\. pending below order=`BUY` 3\. pending above order=`BUY`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending below order=`TAKE_PROFIT` 3\. pending above order=`STOP_LOSS` or `STOP_LOSS_LIMIT`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
OPO| `2`| 1\. working order 2\. pending order| 1\. working order=`BUY` 2\. pending order=`SELL`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending order=ANY| 1\. working order:NONE 2\. pending order: 25010=1|25011=3|25012=0|25013=1|  
OPOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`BUY` 2\. pending below order=`SELL` 3\. pending above order=`SELL`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending below order=`STOP_LOSS` or `STOP_LOSS_LIMIT` 3\. pending above order=`LIMIT_MAKER`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=2|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
OPOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`BUY` 2\. pending below order=`SELL` 3\. pending above order=`SELL`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending below order=`STOP_LOSS` or `STOP_LOSS_LIMIT` 3\. pending above order=`TAKE_PROFIT` or `TAKE_PROFIT_LIMIT`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
  
#### ListStatus `<N>`

Sent by the server whenever an order list state changes.

By default, ListStatus`<N>` is sent for all order lists of an account, including those submitted in different connections. Please see [Response Mode](/en/docs/products/spot/fix-api#response-mode) for other behavior options.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
66| ListID| STRING| N| `ListID` of the list as assigned by the exchange.  
25014| ClListID| STRING| N| `ClListID` of the list as assigned on the request.  
25015| OrigClListID| STRING| N|   
1385| ContingencyType| INT| N| Possible values:  `1` \- ONE_CANCELS_THE_OTHER  `2` \- ONE_TRIGGERS_THE_OTHER  
429| ListStatusType| INT| Y| Possible values:  `2` \- RESPONSE `4` \- EXEC_STARTED  `5` \- ALL_DONE  `100` \- UPDATED  
431| ListOrderStatus| INT| Y| Possible values:  `3` \- EXECUTING  `6` \- ALL_DONE  `7` \- REJECT  
1386| ListRejectReason| INT| N| Possible values:  `99` \- OTHER  
103| OrdRejReason| INT| N| Possible values:  `99` \- OTHER  
60| TransactTime| UTCTIMESTAMP| N| Timestamp when this event occurred.  
25016| ErrorCode| INT| N| API error code (see [Error Codes](/en/docs/products/spot/errors)).  
58| Text| STRING| N| Human-readable error message.  
73| NoOrders| NUMINGROUP| N| The length of the array for Orders.  
=>55| Symbol| STRING| Y| Symbol of the order.  
=>37| OrderID| INT| Y| `OrderID` of the order as assigned by the exchange.  
=>11| ClOrdID| STRING| Y| `ClOrdID` of the order as assigned on the request.  
=>25010| NoListTriggeringInstructions| NUMINGROUP| N| The length of the array for ListTriggeringInstructions.  
==>25011| ListTriggerType| CHAR| N| Possible values:  `1` \- ACTIVATED  `2` \- PARTIALLY_FILLED  `3` \- FILLED  
==>25012| ListTriggerTriggerIndex| INT| N|   
==>25013| ListTriggerAction| CHAR| N| Possible values:  `1` \- RELEASE  `2` \- CANCEL  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=282|35=N|34=2|49=SPOT|52=20240607-02:19:07.837191|56=Eg13pOvN|60=20240607-02:19:07.836000|66=25|73=2|55=BTCUSDT|37=52|11=w1717726747805308656|55=BTCUSDT|37=53|11=p1717726747805308656|25010=1|25011=3|25012=0|25013=1|429=4|431=3|1385=2|25014=1717726747805308656|25015=1717726747805308656|10=223|

#### OrderAmendKeepPriorityRequest `<XAK>`

Sent by the client to reduce the original quantity of their order.

This adds 0 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

**Unfilled Order Count:** 0

Read [Order Amend Keep Priority FAQ](/en/docs/products/spot/faqs/order_amend_keep_priority) to learn more.

**Notes:**

  * The `ClOrdID (11)` is not required to be different from the `ClOrdID` of the order. When the `ClOrdID` of the request is the same as the `ClOrdID` of the order being amended, the `ClOrdID` will remain unchanged.
  * If both `OrderID (37)` and `OrigClOrdID (41)` are provided, the `OrderID` is searched first, then the `OrigClOrdID (41)` from that result is checked against that order. If both conditions are not met the request will be rejected.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
11| ClOrdID| STRING| Y| The ClOrdID of this request.  
41| OrigClOrdID| STRING| N| `ClOrdID (11)` of the order to amend. Either `OrigClOrdID (41)` or `OrderId (37)` have to be specified.  
37| OrderID| INT| N| `OrderID (37)` of the order to amend. Either `OrigClOrdID (41)` or `OrderId (37)` have to be specified.  
55| Symbol| STRING| Y| Symbol on which to amend the order.  
38| OrderQty| QTY| N| New quantity of the order. Required to be smaller than the original OrderQty of the order.  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=103|35=XAK|34=2|49=EXAMPLE|52=20250319-12:35:21.087|56=SPOT|11=O2EIAS01742387721086|37=0|38=0.9|55=BTCUSDT|10=254|

**Response:**

  * [Reject `<3>`](/en/docs/products/spot/fix-api#reject-3) if the incoming request is invalid either due to missing required fields, invalid fields, refers to an invalid symbol, or exceeds the message limit.
  * [OrderAmendReject `<XAR>`](/en/docs/products/spot/fix-api#orderamendreject-xar) if failed due to insufficient order rate limits, pointing to a non-existent order, quantity is invalid, etc.
  * [ExecutionReport `<8>`](/en/docs/products/spot/fix-api#executionreport-8) if the request succeeded for amending a single order.
  * [ExecutionReport `<8>`](/en/docs/products/spot/fix-api#executionreport-8) \+ [ListStatus `<N>`](/en/docs/products/spot/fix-api#liststatus-n) if the request succeeded for amending an order which is part of an Order list.



### OrderAmendReject `<XAR>`

Sent by the server when the OrderAmendKeepPriorityRequest `<XAK>` has failed.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
11| ClOrdID| STRING| Y| `ClOrdId` of the amend request.  
41| OrigClOrdID| STRING| N| `OrigClOrdId` (41) from the amend request.  
37| OrderID| INT| N| `OrderId (37)` from the amend request.  
55| Symbol| STRING| Y| `Symbol (55)` from the amend request.  
38| OrderQty| QTY| Y|   
25016| ErrorCode| INT| Y| API error code (see [Error Codes](/en/docs/products/spot/errors)).  
58| Text| STRING| Y| Human-readable error message.  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=0000176|35=XAR|49=SPOT|56=OE|34=2|52=20250319-14:27:32.751074|11=1WRGW5J1742394452749|37=0|55=BTCUSDT|38=1.000000|25016=-2038|58=The requested action would change no state; rejecting.|10=235|

### Limit Messages

#### LimitQuery `<XLQ>`

Sent by the client to query current limits.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
6136| ReqID| STRING| Y| ID of this request  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=82|35=XLQ|34=2|49=7buKHZxZ|52=20240614-05:35:35.357|56=SPOT|6136=1718343335357229749|10=170|

#### LimitResponse `<XLR>`

Sent by the server in response to [LimitQuery`<XLQ>`](/en/docs/products/spot/fix-api#limitquery-xlq).

Tag| Name| Type| Required| Description  
---|---|---|---|---  
6136| ReqID| STRING| Y| `ReqID` from the request.  
25003| NoLimitIndicators| NUMINGROUP| Y| The length of the array for LimitIndicators.  
=>25004| LimitType| CHAR| Y| Possible values:  `1` \- ORDER_LIMIT  `2` \- MESSAGE_LIMIT  
=>25005| LimitCount| INT| Y| The current use of this limit.  
=>25006| LimitMax| INT| Y| The maximum allowed for this limit.  
=>25007| LimitResetInterval| INT| N| How often the limit resets.  
=>25008| LimitResetIntervalResolution| CHAR| N| Time unit of `LimitResetInterval`. Possible values:  `s` \- SECOND  `m` \- MINUTE  `h` \- HOUR  `d` \- DAY  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=225|35=XLR|34=2|49=SPOT|52=20240614-05:42:42.724057|56=uGnG0ef8|6136=1718343762723730315|25003=3|25004=2|25005=1|25006=1000|25007=10|25008=s|25004=1|25005=0|25006=200|25007=10|25008=s|25004=1|25005=0|25006=200000|25007=1|25008=d|10=241|

### Market Data Messages

The messages below can only be used for the FIX Market Data.

#### InstrumentListRequest `<x>`

Sent by the client to query information about instruments.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
320| InstrumentReqID| STRING| Y| ID of this request  
559| InstrumentListRequestType| INT| Y| Possible values:  `0` \- SINGLE_INSTRUMENT  `4` \- ALL_INSTRUMENTS  
55| Symbol| STRING| N| Required when the `InstrumentListRequestType` is set to `SINGLE_INSTRUMENT(0)`  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=92|35=x|49=BMDWATCH|56=SPOT|34=2|52=20250114-08:46:56.096691|320=BTCUSDT_INFO|559=0|55=BTCUSDT|10=164|

#### InstrumentList `<y>`

Sent by the server in a response to the [InstrumentListRequest`<x>`](/en/docs/products/spot/fix-api#instrumentlistrequest-x).

More detailed symbol information is available through the [exchangeInfo](/en/docs/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info) endpoint.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
320| InstrumentReqID| STRING| Y| `InstrumentReqID` from the request.  
146| NoRelatedSym| NUMINGROUP| Y| Number of symbols  
=>55| Symbol| STRING| Y|   
=>15| Currency| STRING| Y| Quote asset of this symbol  
=>562| MinTradeVol| QTY| N| Corresponds to the [LOT_SIZE](/en/docs/products/spot/filters#lot_size) filter  
=>1140| MaxTradeVol| QTY| N| Corresponds to the [LOT_SIZE](/en/docs/products/spot/filters#lot_size) filter  
=>25039| MinQtyIncrement| QTY| N| Corresponds to the [LOT_SIZE](/en/docs/products/spot/filters#lot_size) filter  
=>25040| MarketMinTradeVol| QTY| N| Corresponds to the [MARKET_LOT_SIZE](/en/docs/products/spot/filters#market_lot_size) filter  
=>25041| MarketMaxTradeVol| QTY| N| Corresponds to the [MARKET_LOT_SIZE](/en/docs/products/spot/filters#market_lot_size) filter  
=>25042| MarketMinQtyIncrement| QTY| N| Corresponds to the [MARKET_LOT_SIZE](/en/docs/products/spot/filters#market_lot_size) filter  
=>969| MinPriceIncrement| PRICE| N| Corresponds to the [PRICE](/en/docs/products/spot/filters#price_filter) filter  
=>2551| StartPriceRange| PRICE| N| Corresponds to the [PRICE](/en/docs/products/spot/filters#price_filter) filter  
=>2552| EndPriceRange| PRICE| N| Corresponds to the [PRICE](/en/docs/products/spot/filters#price_filter) filter  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=218|35=y|49=SPOT|56=BMDWATCH|34=2|52=20250114-08:46:56.100147|320=BTCUSDT_INFO|146=1|55=BTCUSDT|15=USDT|562=0.00001000|1140=9000.00000000|25039=0.00001000|25040=0.00000001|25041=76.79001236|25042=0.00000001|969=0.01000000|10=093|

#### MarketDataRequest `<V>`

Sent by the client to subscribe to or unsubscribe from market data stream.

**Trade Stream**

The Trade Streams push raw trade information; each trade has a unique buyer and seller.

**Fields required to subscribe:**

  * `SubscriptionRequestType` present with value `SUBSCRIBE(1)`
  * `MDEntryType` present with value `TRADE(2)`



**Update Speed:** Real-time

**Individual Symbol Book Ticker Stream**

Pushes any update to the best bid or offers price or quantity in real-time for a specified symbol.

**Fields required to subscribe:**

  * `SubscriptionRequestType` with value `SUBSCRIBE(1)`
  * `MDEntryType` with value `BID(0)`
  * `MDEntryType` with value `OFFER(1)`
  * `MarketDepth` with value `1`



**Update Speed:** Real-time

In the [Individual Symbol Book Ticker Stream](/en/docs/products/spot/fix-api#symbolbooktickerstream), when `MDUpdateAction` is set to `CHANGE(1)` in a [MarketDataIncrementalRefresh`<X>`](/en/docs/products/spot/fix-api#marketdataincrementalrefresh) message sent from the server, it replaces the previous best quote.

**Diff. Depth Stream**

Order book price and quantity depth updates used to locally manage an order book.

**Fields required to subscribe:**

  * `SubscriptionRequestType` with value `SUBSCRIBE(1)`
  * `MDEntryType` with value `BID(0)`
  * `MDEntryType` with value `OFFER(1)`
  * `MarketDepth` with a value between `2` and `5000`, which controls the size of the initial snapshot and has no effect on subsequent [MarketDataIncrementalRefresh`<X>`](/en/docs/products/spot/fix-api#marketdataincrementalrefresh) messages



**Update Speed:** 100ms

Since the [MarketDataSnapshot`<W>`](/en/docs/products/spot/fix-api#marketdatasnapshot-w) have a limit on the number of price levels (5000 on each side maximum), you won't learn the quantities for the levels outside of the initial snapshot unless they change. So be careful when using the information for those levels, since they might not reflect the full view of the order book. However, for most use cases, seeing 5000 levels on each side is enough to understand the market and trade effectively.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
262| MDReqID| STRING| Y| ID of this request  
263| SubscriptionRequestType| CHAR| Y| Subscription Request Type. Possible values:  `1` \- SUBSCRIBE  `2` \- UNSUBSCRIBE  
264| MarketDepth| INT| N| Subscription depth.  Possible values:  `1` \- Book Ticker subscription  `2`-`5000` \- Diff. Depth Stream  
266| AggregatedBook| NUMINGROUP| N| Possible values:  `Y` \- one book entry per side per price  
146| NoRelatedSym| NUMINGROUP| N| Number of symbols  
=>55| Symbol| STRING| Y|   
267| NoMDEntryTypes| NUMINGROUP| N| Number of entry types  
=>269| MDEntryType| CHAR| Y| Possible values:  `0` \- BID  `1` \- OFFER  `2` \- TRADE  
  
**Sample message:**
    
    
    Code
    
    # Subscriptions
    # BOOK TICKER Stream
    8=FIX.4.4|9=132|35=V|49=TRADER1|56=SPOT|34=4|52=20241122-06:17:14.183428|262=BOOK_TICKER_STREAM|263=1|264=1|266=Y|146=1|55=BTCUSDT|267=2|269=0|269=1|10=010|
    
    # DEPTH Stream
    8=FIX.4.4|9=127|35=V|49=TRADER1|56=SPOT|34=7|52=20241122-06:17:14.443822|262=DEPTH_STREAM|263=1|264=10|266=Y|146=1|55=BTCUSDT|267=2|269=0|269=1|10=111|
    
    # TRADE Stream
    8=FIX.4.4|9=120|35=V|49=TRADER1|56=SPOT|34=3|52=20241122-06:34:14.775606|262=TRADE_STREAM|263=1|264=1|266=Y|146=1|55=BTCUSDT|267=1|269=2|10=040|
    
    # Unsubscription from TRADE Stream
    8=FIX.4.4|9=79|35=V|49=TRADER1|56=SPOT|34=7|52=20241122-06:41:56.966969|262=TRADE_STREAM|263=2|264=1|10=113|

### MarketDataRequestReject `<Y>`

Sent by the server in a response to an invalid MarketDataRequest `<V>`.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
262| MDReqID| STRING| Y| ID of the invalid [MarketDataRequest`<V>`](/en/docs/products/spot/fix-api#marketdatarequest-v)  
281| MDReqRejReason| CHAR| N| Possible values:  `1` \- DUPLICATE_MDREQID  `2` \- TOO_MANY_SUBSCRIPTIONS  
25016| ErrorCode| INT| N| API Error code. See [Errors](/en/docs/products/spot/errors)  
58| Text| STRING| N| Human-readable error message.  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=0000218|35=Y|49=SPOT|56=EXAMPLE|34=5|52=20241019-05:39:36.688964|262=BOOK_TICKER_2|281=2|25016=-1191|58=Similar subscription is already active on this connection. Symbol='BNBBUSD', active subscription id: 'BOOK_TICKER_1'.|10=137|

### MarketDataSnapshot `<W>`

Sent by the server in response to a [MarketDataRequest`<V>`](/en/docs/products/spot/fix-api#marketdatarequest-v), activating [Individual Symbol Book Ticker Stream](/en/docs/products/spot/fix-api#symbolbooktickerstream) or [Diff. Depth Stream](/en/docs/products/spot/fix-api#diffdepthstream) subscriptions.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
262| MDReqID| STRING| Y| ID of the [MarketDataRequest`<V>`](/en/docs/products/spot/fix-api#marketdatarequest-v) that activated this subscription  
55| Symbol| STRING| Y|   
25044| LastBookUpdateID| INT| N|   
268| NoMDEntries| NUMINGROUP| Y| Number of entries  
=>269| MDEntryType| CHAR| Y| Possible values:  `0` \- BID  `1` \- OFFER  `2` \- TRADE  
=>270| MDEntryPx| PRICE| Y| Price  
=>271| MDEntrySize| QTY| Y| Quantity  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=0000107|35=W|49=SPOT|56=EXAMPLE|34=34|52=20241019-05:41:52.867164|262=BOOK_TICKER_1_2|55=BNBBUSD|25044=0|268=0|10=151|

### MarketDataIncrementalRefresh `<X>`

Sent by the server when there is a change in a subscribed stream.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
262| MDReqID| STRING| Y| ID of the [MarketDataRequest`<V>`](/en/docs/products/spot/fix-api#marketdatarequest-v) that activated this subscription  
268| NoMDEntries| NUMINGROUP| Y| Number of entries  
=>279| MDUpdateAction| CHAR| Y| Possible values:  `0` \- NEW  `1` \- CHANGE  `2` \- DELETE  
=>270| MDEntryPx| PRICE| Y| Price  
=>271| MDEntrySize| QTY| N| Quantity  
=>269| MDEntryType| CHAR| Y| Possible values:  `0` \- BID  `1` \- OFFER  `2` \- TRADE  
=>55| Symbol| STRING| N| Market Data Entry will default to the same `Symbol` of the previous Market Data Entry in the same Market Data message if `Symbol` is not specified  
=>60| TransactTime| UTCTIMESTAMP| N|   
=>1003| TradeID| INT| N|   
=>2446| AggressorSide| CHAR| N| Possible values:  `1` \- BUY  `2` \- SELL  
=>25043| FirstBookUpdateID| INT| N| Only present in [Diff. Depth Stream](/en/docs/products/spot/fix-api#diffdepthstream).  Market Data Entry will default to the same `FirstBookUpdateID` of the previous Market Data Entry in the same Market Data message if `FirstBookUpdateID` is not specified  
=>25044| LastBookUpdateID| INT| N| Only present in [Diff. Depth Stream](/en/docs/products/spot/fix-api#diffdepthstream) and [Individual Symbol Book Ticker Stream](/en/docs/products/spot/fix-api#symbolbooktickerstream).  Market Data Entry will default to the same `LastBookUpdateID` of the previous Market Data Entry in the same Market Data message if `LastBookUpdateID` is not specified  
  
**Sample message:**
    
    
    Code
    
    8=FIX.4.4|9=0000303|35=X|49=SPOT|56=EXAMPLE|34=16|52=20241019-05:40:11.466313|262=TRADE_3|268=3|279=0|269=2|270=10.00000|271=0.01000|55=BNBBUSD|1003=0|60=20241019-05:40:11.464000|279=0|269=2|270=10.00000|271=0.01000|1003=1|60=20241019-05:40:11.464000|279=0|269=2|270=10.00000|271=0.01000|1003=2|60=20241019-05:40:11.464000|10=042|

## FIX SBE

FIX SBE (Simple Binary Encoding) can be used instead of FIX with the [spot_fix_prod_latest.xml](/en/docs/products/spot/sbe/schemas/spot_fix_prod_latest.xml) schema file.

### SBE

Read the [SBE FAQ](/en/docs/products/spot/faqs/sbe_faq) for important information about using SBE with Binance APIs.

  * Please review and understand the [SBE specification](https://www.fixtrading.org/standards/sbe-online/) before attempting to use FIX SBE
  * When encoding and decoding SBE payloads, it is recommended to use code generated by [`SbeTool`](https://github.com/aeron-io/simple-binary-encoding) to ensure compliance with the FIX SBE specification.



### Endpoints

In addition to FIX encoding available on port 9000, two request/response encoding schemes are supported on additional TCP ports. See below endpoints for each API.

#### Order Entry

  * `tcp+tls://fix-oe.binance.com:9001`: Send FIX requests; receive FIX SBE responses
    * FIX `SbeSchemaId` tag (=25050) must be set to the FIX SBE schema ID (e.g. 1)
    * The FIX `SbeSchemaVersion` tag (=25051) must be set to the FIX SBE schema version (e.g. 0)
  * `tcp+tls://fix-oe.binance.com:9002`: Send FIX SBE requests; receive FIX SBE responses



#### Drop Copy

  * `tcp+tls://fix-dc.binance.com:9001`: Send FIX requests; receive FIX SBE responses
    * FIX `SbeSchemaId` tag (=25050) must be set to the FIX SBE schema ID (e.g. 1)
    * The FIX `SbeSchemaVersion` tag (=25051) must be set to the FIX SBE schema version (e.g. 0)
  * `tcp+tls://fix-dc.binance.com:9002`: Send FIX SBE requests; receive FIX SBE responses



#### Market data

  * `tcp+tls://fix-md.binance.com:9001`: Send FIX requests; receive FIX SBE responses
    * FIX `SbeSchemaId` tag (=25050) must be set to the FIX SBE schema ID (e.g. 1)
    * The FIX `SbeSchemaVersion` tag (=25051) must be set to the FIX SBE schema version (e.g. 0)
  * `tcp+tls://fix-md.binance.com:9002`: Send FIX SBE requests; receive FIX SBE responses



### FIX SBE encoding layout

FIX SBE request/response messages always come with a SOFH (Simple Open Framing Header) and message header. A given FIX SBE message of N bytes has the following wire format:

`<SOFH (6 bytes)> <message header (20 bytes)> <message (N bytes)>`

SOFH: This corresponds to the "sofh" composite type in the schema file. This acts as a framing header so that the FIX SBE servers/clients can know the length of SBE messages and ensure messages have been fully received prior to deserializing them

Notes:

  * The two fields within the SOFH MUST be encoded in little-endian
  * The FIX servers only support `0xEB50` for the encodingType field, i.e. only little-endian is supported for all fields



Message header: This corresponds to the "messageHeader" composite type in the schema file.

### Logon

The logon signature (RawData) is computed as documented in the [signature computation](/en/docs/products/spot/fix-api#how-to-sign-logon-a-request) section.

#### Sample FIX SBE `Logon` request message

Please see below the hexdump of a sample FIX SBE `Logon` message obtained by following the above instructions.

Bytes| Description  
---|---  
0xd1, 0x00, 0x00, 0x00| sofh.messageLength  
0x50, 0xeb| sofh.encodingType  
0x0e, 0x00| messageHeader.blockLength  
0x28, 0x4e| messageHeader.templateId  
0x01, 0x00| messageHeader.schemaId  
0x00, 0x00| messageHeader.version  
0x01, 0x00, 0x00, 0x00| messageHeader.seqNum  
0x58, 0x7a, 0x5f, 0x99, 0xdb, 0x1b, 0x06, 0x00| messageHeader.sendingTime  
0x00| Logon.EncryptMethod  
0x1e, 0x00, 0x00, 0x00| Logon.HeartBtInt  
0x01| Logon.ResetSeqNumFlag  
0x02| Logon.MessageHandling  
0xff| Logon.ResponseMode  
0xff| Logon.ExecutionReportType  
0xff| Logon.DropCopyFlag  
0xff, 0xff, 0xff, 0xff| Logon.RecvWindow  
0x07| Logon.SenderCompId.length  
0x45, 0x58, 0x41, 0x4d, 0x50, 0x4c, 0x45| Logon.SenderCompId.varData  
0x04| Logon.TargetCompId.length  
0x53, 0x50, 0x4f, 0x54| Logon.TargetCompId.varData  
0x58, 0x00| Logon.RawData.length  
0x34, 0x4d, 0x48, 0x58, 0x65, 0x6c, 0x56, 0x56| Logon.RawData.varData  
0x63, 0x70, 0x6b, 0x64, 0x77, 0x75, 0x4c, 0x62| Logon.RawData.varData  
0x6c, 0x36, 0x6e, 0x37, 0x33, 0x48, 0x51, 0x55| Logon.RawData.varData  
0x58, 0x55, 0x66, 0x31, 0x64, 0x73, 0x65, 0x32| Logon.RawData.varData  
0x50, 0x43, 0x67, 0x54, 0x31, 0x44, 0x59, 0x71| Logon.RawData.varData  
0x57, 0x39, 0x77, 0x38, 0x41, 0x56, 0x5a, 0x31| Logon.RawData.varData  
0x52, 0x41, 0x43, 0x46, 0x47, 0x4d, 0x2b, 0x35| Logon.RawData.varData  
0x55, 0x64, 0x6c, 0x47, 0x50, 0x72, 0x51, 0x48| Logon.RawData.varData  
0x72, 0x67, 0x74, 0x53, 0x33, 0x43, 0x76, 0x73| Logon.RawData.varData  
0x52, 0x55, 0x52, 0x43, 0x31, 0x6f, 0x6a, 0x37| Logon.RawData.varData  
0x33, 0x6a, 0x38, 0x67, 0x43, 0x41, 0x3d, 0x3d| Logon.RawData.varData  
0x40, 0x00| Logon.Username.length  
0x73, 0x42, 0x52, 0x58, 0x72, 0x4a, 0x78, 0x32| Logon.Username.varData  
0x44, 0x73, 0x4f, 0x72, 0x61, 0x4d, 0x58, 0x4f| Logon.Username.varData  
0x61, 0x55, 0x6f, 0x76, 0x45, 0x68, 0x67, 0x56| Logon.Username.varData  
0x52, 0x63, 0x6a, 0x4f, 0x76, 0x43, 0x74, 0x51| Logon.Username.varData  
0x77, 0x6e, 0x57, 0x6a, 0x38, 0x56, 0x78, 0x6b| Logon.Username.varData  
0x4f, 0x68, 0x31, 0x78, 0x71, 0x62, 0x6f, 0x53| Logon.Username.varData  
0x30, 0x32, 0x53, 0x50, 0x47, 0x66, 0x4b, 0x69| Logon.Username.varData  
0x32, 0x68, 0x38, 0x73, 0x70, 0x5a, 0x4a, 0x62| Logon.Username.varData  
  
### FIX vs. FIX SBE

General:

  * The `sofh.messageLength` field _must_ include the size of the SOFH (6 bytes)
  * FIX SBE has no `Checksum` field
  * When sending FIX SBE requests on port 9002
    * All fields must be set in the payload
    * Optional fields that are not present must be set to the corresponding `nullValue`
      * The encoders generated by `SbeTool` handle this correctly
      * Please refer to the definition of `nullValue` in the [SBE specification](https://www.fixtrading.org/standards/sbe-online/) if encoding payloads manually



Decimal encoding:

  * In request messages, the values for `PriceExponent` and `QtyExponent` must be no more precise than the precision of the symbol being transacted. Symbol precision can be retrieved from the `InstrumentList` response.



#### Logon

  * The `SenderCompID`, `TargetCompID` and `RecvWindow` fields are provided in the `Logon` FIX SBE message instead of the message header
    * The `RecvWindow` field set in the `Logon` message applies to all trading request messages within the FIX SBE session
    * When set, the `RecvWindow` field is in microseconds
  * When the `ResponseMode` field is set to `OnlyAcks`, the `ExecutionReportType` field can be set to `Mini` to receive `ExecutionReportAck` messages instead of `ExecutionReport`
    * Note: The `ExecutionReportType` field is only supported on port 9001 and port 9002 for the Order Entry and Drop Copy endpoints



#### MarketDataIncrementalRefresh

  * This single message in the FIX schema is split into the following FIX SBE messages: `MarketDataIncrementalTrade`, `MarketDataIncrementalBookTicker` and `MarketDataIncrementalDepth`
  * The `MDReqID` field is omitted from the market data snapshot and refresh messages as these messages can be tied to the subscription request using the `Symbol` field and the message's template ID
    * `MDReqID` is required in the `MarketDataRequest` message so that it may appear in `MarketDataRequestReject`
    * The value of `MDReqID` must be unique across subscriptions



#### MarketDataIncrementalTrade

  * The MDUpdateAction field available in the FIX schema is omitted in FIX SBE since the value is always `NEW`.



#### MarketDataIncrementalBookTicker

  * FIX SBE book ticker subscriptions use **auto-culling** : when the system is under high load, it may drop outdated events instead of queuing all events and delivering them with a delay.
    * For example, if a best bid/ask event is generated at time T2 when there is still an undelivered event queued at time T1 (where T1 < T2), the event for T1 is dropped, and the system will deliver only the event for T2. This is done on a per-symbol basis.
  * The `MDUpdateAction` field available in the FIX schema is omitted in FIX SBE as its value may be derived from `MDEntrySize`.
    * When `MDEntrySize` is unset (`NullVal`), `MDUpdateAction` is `DELETE`.
    * When `MDEntrySize` is set,
      * if the price level exists in your local order book, `MDUpdateAction` is `CHANGE`
      * else `MDUpdateAction` is `NEW`.



#### MarketDataIncrementalDepth

  * FIX SBE depth update speed: 20ms
  * The `MDUpdateAction` field available in the FIX schema is omitted in FIX SBE as its value may be derived from `MDEntrySize`.
    * When `MDEntrySize` is unset (`NullVal`), `MDUpdateAction` is `DELETE`.
    * When `MDEntrySize` is set,
      * if the price level exists in your local order book, `MDUpdateAction` is `CHANGE`
      * else `MDUpdateAction` is `NEW`.



### Limits

Connection limits are shared between FIX and FIX SBE.

### Errors

The following FIX SBE-specific errors may be returned:

Code| Message| Description  
---|---|---  
-1152| Invalid SBE message header.| Error when decoding `messageHeader` in FIX SBE request  
-1153| Invalid SBE schema ID or version specified.| Error when parsing/decoding FIX SBE schema ID/version  
-1177| Invalid encodingType.| Error when decoding `encodingType` field in sofh composite type  
-1221| Invalid/missing field(s) in SBE message.| Invalid/missing field when decoding FIX SBE request  
  
Note: Error codes returned for semantically equivalent FIX and FIX SBE requests may not be identical.

### FAQ

See the [SBE FAQ](/en/docs/products/spot/faqs/sbe_faq) for more information on generating SBE decoders and handling schema updates.

Was this page helpful?

Last modified on November 12, 2026

[WebSocket Streams](/en/docs/products/spot/web-socket-streams)[SBE Market Data Streams](/en/docs/products/spot/sbe-market-data-streams)

---

# FIX API

此 API 只能用于现货 （`SPOT`） 交易所。

## 一般 API 信息

  * FIX 连接需要 TLS 加密。请使用本地 TCP+TLS 连接或设置本地代理如 [stunnel](https://www.stunnel.org/) 来处理 TLS 加密。
  * API 处理请求的超时时间为 10 秒。如果撮合引擎的响应时间超过此时间，API 将返回 “Timeout waiting for response from backend server. Send status unknown; execution status unknown.”。[(-1007 超时)](/zh-CN/docs/products/spot/errors#-1007-timeout)
    * 这并不总是意味着该请求在撮合引擎中失败。
    * 如果请求状态未显示在 [WebSocket 账户接口](/zh-CN/docs/products/spot/user-data-stream) 中，请执行 API 查询以获取其状态。
  * 如果您的请求包含非 ASCII 字符的交易对名称，那么响应中可能包含以 UTF-8 编码的非 ASCII 字符。
  * 为确保连接不中断，请确保您的客户端在 TLS 握手过程中发送 **SNI（服务器名称指示）** ，并对目标主机名进行证书验证。
  * 未发送 SNI 的客户端可能会收到证书错误的消息，导致 TLS 握手或主机名验证失败。



### NodeJS

如果你正在使用 Node.js，并且通过原始 TLS 套接字（`tls.connect()`）进行连接，你必须显式设置 servername 选项。请参考下面的示例：
    
    
    Code
    
    const tls = require("tls");
    const hostname = "fix-dc.binance.com"; //示例
    
    const options = {
      host: hostname,
      port: 9002,
      servername: hostname, // 启用 SNI
    };

注意：NodeJS 默认不启用 TLS 的 SNI（详见 <https://nodejs.org/api/tls.html#tlsconnectoptions-callback>）。如果您使用 Node.js 中的标准 HTTPS 库（例如 `https.request()`、`axios`、`fetch`），通常在通过主机名/URL 连接时会自动设置 SNI。

### 其他语言/自定义 TLS 实现

使用自定义 TLS 代理或 TLS API 时，请确保将相应字段（通常名为 `server_hostname`、`hostname` 或 `ServerName`）设置为目标主机名，以便发送 SNI。

**FIX 会话仅支持 Ed25519 密钥。**

关于如何设置 Ed25519 密钥对，请参考 [本教程](https://www.binance.com/zh-CN/support/faq/%E5%A6%82%E4%BD%95%E7%94%9F%E6%88%90ed25519%E5%AF%86%E9%92%A5%E5%AF%B9%E5%9C%A8%E5%B8%81%E5%AE%89%E5%8F%91%E9%80%81api%E8%AF%B7%E6%B1%82-6b9a63f1e3384cf48a2eedb82767a69a)。

### FIX API 订单接入会话

  * 端点为：`tcp+tls://fix-oe.binance.com:9000`
  * 支持下单，取消订单和查询当前限制使用情况。
  * 支持接收账户的所有 [ExecutionReport`<8>`](/zh-CN/docs/products/spot/fix-api#executionreport) 和 [List Status`<N>`](/zh-CN/docs/products/spot/fix-api#liststatus)。
  * 仅允许带有 `FIX_API` 的 API Key 连接。
  * 关于 QuickFIX 模式文件， 请点击 [这里](/zh-CN/docs/products/spot/fix/schemas/spot-fix-oe.xml)。



### FIX API Drop Copy 会话

  * 端点为：`tcp+tls://fix-dc.binance.com:9000`
  * 支持接收账户的所有 [ExecutionReport`<8>`](/zh-CN/docs/products/spot/fix-api#executionreport) 和 [List Status`<N>`](/zh-CN/docs/products/spot/fix-api#liststatus)。
  * 仅允许连接带有 `FIX_API` 或 `FIX_API_READ_ONLY` 的 API Key。
  * 关于 QuickFIX 模式文件， 请点击 [这里](/zh-CN/docs/products/spot/fix/schemas/spot-fix-oe.xml)。
  * Drop Copy 会话中的数据存在 1 秒的延迟。



### FIX API Market Data 会话

  * 端点为：`tcp+tls：//fix-md.binance.com：9000`
  * 支持市场数据流和活动工具查询。
  * 不支持下订单或取消订单。
  * 仅允许连接带有“FIX_API”或“FIX_API_READ_ONLY”的 API 密钥。



关于 QuickFIX 模式 (Schema) 文件， 请点击 [这里](/zh-CN/docs/products/spot/fix/schemas/spot-fix-oe.xml)。

FIX 连接需要 TLS 加密。请使用本地 TCP+TLS 连接或设置本地代理如 [stunnel](https://www.stunnel.org/) 来处理 TLS 加密。

FIX Market Data 的 QuickFIX Schema 可以在 [这里](/zh-CN/docs/products/spot/fix/schemas/spot-fix-md.xml)

### FIX 连接生命周期

  * 所有 FIX API 会话将尽最大努力，尽可能长时间地保持开放状态。
  * 没有最短连接时间保证，服务器可能随时进入维护状态。
    * 当服务器进入维护状态时，系统将会向客户端**每隔 10 秒发送一条** [News `<B>`](/zh-CN/docs/products/spot/fix-api#news) 消息，**直到断开连接** ，以提示客户端重新连接。收到此消息后，客户端应建立新会话并关闭旧会话。如果客户端在服务器断开连接前没有关闭旧会话，那么服务器会将其注销并关闭会话。
  * 连接后，客户端必须发送 Logon `<A>` 请求。有关详情，请参阅 [如何签署登录请求](/zh-CN/docs/products/spot/fix-api#signaturecomputation)。
  * 客户端应在断开连接之前发送 Logout `<5>` 消息来关闭会话。未能发送注销消息将导致在 2x `HeartInt (108)` 定义的时间间隔内无法将会话的 `SenderCompID (49)` 用于新会话的建立。
  * 系统允许在登录过程中协商 `HeartInt (108)` 值。可接受值的范围为 5 到 60 秒。
    * 如果服务器在 `HeartInt (108)` 间隔内没有发送任何消息，将发送 [HeartBeat `<0>`](/zh-CN/docs/products/spot/fix-api#heartbeat)。
    * 如果服务器在 `HeartInt (108)` 间隔内没有收到任何消息，将发送 [TestRequest `<1>`](/zh-CN/docs/products/spot/fix-api#testrequest)。如果服务器在 `HeartInt (108)` 秒内没有收到来自客户端的包含预期 `TestReqID (112)` 的 HeartBeat `<0>` 消息，服务器将发送 Logout `<5>` 消息并关闭连接。
    * 如果客户端在 `HeartInt (108)` 间隔内未收到任何消息，那么客户端应负责发送 TestRequest `<1>` 消息以确保连接正常。收到这样的 TestRequest `<1>` 后，服务器会发送包含预期 `TestReqID (112)` 的 HeartBeat `<0>` 消息来进行响应。如果客户端在 `HeartInt (108)` 间隔内没有收到服务器的响应，那么客户端应关闭现有的会话和连接，并且建立新的会话和连接。



### API Key 权限

如果您需要使用 FIX API 的订单接入会话，您的 API key 必须配置 `FIX_API` 权限。如果您需要使用 FIX API 的 Drop Copy 会话，您的 API key 必须配置 `FIX_API_READ_ONLY` 或 `FIX_API` 权限。要访问 FIX Market Data 会话，您的 API 密钥必须配置为 `FIX_API` 或 `FIX_API_READ_ONLY` 权限

**FIX 会话仅支持 Ed25519 密钥。**

关于如何设置 Ed25519 密钥对，请参考 [本教程](https://www.binance.com/zh-CN/support/faq/%E5%A6%82%E4%BD%95%E7%94%9F%E6%88%90ed25519%E5%AF%86%E9%92%A5%E5%AF%B9%E5%9C%A8%E5%B8%81%E5%AE%89%E5%8F%91%E9%80%81api%E8%AF%B7%E6%B1%82-6b9a63f1e3384cf48a2eedb82767a69a)。

### 关于消息处理顺序

初始 [Logon`<A>`](/zh-CN/docs/products/spot/fix-api#logon-request) 消息中必需的 `MessageHandling (25035)` 字段控制客户端消息在被撮合引擎处理之前是否可以被重新排序。

模式| 描述  
---|---  
`UNORDERED(1)`| 客户端消息可以按任意顺序发送到撮合引擎。  
`SEQUENTIAL(2)`| 客户端消息始终按 `MsgSeqNum (34)` 顺序发送到撮合引擎。  
  
在所有模式下，客户端的 `MsgSeqNum (34)` 必须单调递增，即每条后续消息的序列号都比前一条消息正好大 1。

在有多个消息需要从客户端传输到服务器的情况时， `UNORDERED(1)` 应该会提供更好的性能。

### 响应模式

默认情况下，所有并发订单录入会话都会接收到账户所有成功的 [ExecutionReport `<8>` ](/zh-CN/docs/products/spot/fix-api#executionreport) 和 [ListStatus `<N>` ](/zh-CN/docs/products/spot/fix-api#liststatus) 消息，包括从其他 FIX 会话和通过非 FIX API 下达的订单。

用户可以在初始消息 [Logon`<A>`](/zh-CN/docs/products/spot/fix-api#logon-request) 中使用 `ResponseMode (25036)` 字段来改变这种行为。

  * `EVERYTHING(1)`： 默认模式。
  * `ONLY_ACKS(2)`： 无论操作成功还是失败，都只接收 ACK 消息。禁用 `ExecutionReport` 推送。



### 时间同步安全

  * 所有请求都需要一个 `SendingTime(52)` 字段，该字段应为当前时间戳。
  * 另有一个可选字段 `RecvWindow(25000)` ，用以指定请求的有效期（以毫秒为单位）。
    * `RecvWindow(25000)` 扩展为三位小数（例如 6000.346），以便可以指定微秒。
    * 如果未指定 `RecvWindow(25000)`，则仅对 Logon`<A>` 请求默认为 5000 毫秒。对于其他请求，如果未设置，则不会执行 RecvWindow 检查。
    * `RecvWindow(25000)` 的最大有效时间为 60000 毫秒。
  * 请求处理逻辑如下：


    
    
    Code
    
    serverTime = getCurrentTime()
    if (SendingTime < (serverTime + 1 second) && (serverTime - SendingTime) <= RecvWindow) {
      // 开始处理请求
      serverTime = getCurrentTime()
      if (serverTime - SendingTime) <= RecvWindow {
        // 将请求转发到撮合引擎
      } else {
        // 拒绝请求
      }
      // 结束处理请求
    } else {
      // 拒绝请求
    }

### 如何签署 Logon `<A>` 请求

[Logon`<A>`](/zh-CN/docs/products/spot/fix-api#logon-main) 消息用于验证您与 FIX API 的连接。这条消息必须是客户端发送的第一条消息。

  * `Username (553)` 字段必须包含 API key。
  * `RawData (96)` 字段必须包含使用 API key 生成的有效签名。



签名 payload 是一个文本字符串。该字符串通过按以下所列顺序去连接下列字段来构成， 并且以 SOH 字符作为分隔符：

  1. `MsgType (35)`
  2. `SenderCompId (49)`
  3. `TargetCompId (56)`
  4. `MsgSeqNum (34)`
  5. `SendingTime (52)`



请使用您的密钥签署 payload。请使用 **base64** 对签名进行编码。生成的文本字符串是 `RawData (96)` 字段的值。

以下是实现签名算法的 Python 代码示例：
    
    
    Code
    
    import base64
    
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives.serialization import load_pem_private_key
    
    def logon_raw_data(private_key: Ed25519PrivateKey,
                       sender_comp_id: str,
                       target_comp_id: str,
                       msg_seq_num: str,
                       sending_time: str):
        """
        Computes the value of RawData (96) field in Logon<A> message.
        """
        payload = chr(1).join([
            'A',
            sender_comp_id,
            target_comp_id,
            msg_seq_num,
            sending_time,
        ])
        signature = private_key.sign(payload.encode('ASCII'))
        return base64.b64encode(signature).decode('ASCII')
    
    
    with open('private_key.pem', 'rb') as f:
        private_key = load_pem_private_key(data=f.read(),
                                           password=None)
    
    raw_data = logon_raw_data(private_key,
                              sender_comp_id='5JQmUOsm',
                              target_comp_id='SPOT',
                              msg_seq_num='1',
                              sending_time='20240612-08:52:21.613')

以下值可用于验证签名计算实现的正确性：

字段| 取值  
---|---  
MsgType (35)| `A`  
SenderCompID (49)| `EXAMPLE`  
TargetCompID (56)| `SPOT`  
MsgSeqNum (34)| `1`  
SendingTime (52)| `20240627-11:17:25.223`  
  
示例计算中使用的 Ed25519 密钥如下所示：

以下密钥仅用于示范说明目的。请务必不要在任何实际应用中使用该密钥，因为它不安全，可能会危及您的加密实现。请在实际使用中生成属于您自己的唯一且安全的密钥。
    
    
    Code
    
    -----BEGIN PRIVATE KEY-----
    MC4CAQAwBQYDK2VwBCIEIIJEYWtGBrhACmb9Dvy+qa8WEf0lQOl1s4CLIAB9m89u
    -----END PRIVATE KEY-----

经过计算生成的签名：
    
    
    Code
    
    4MHXelVVcpkdwuLbl6n73HQUXUf1dse2PCgT1DYqW9w8AVZ1RACFGM+5UdlGPrQHrgtS3CvsRURC1oj73j8gCA==

生成的 Logon `<A>` 消息：
    
    
    Code
    
    8=FIX.4.4|9=247|35=A|34=1|49=EXAMPLE|52=20240627-11:17:25.223|56=SPOT|95=88|96=4MHXelVVcpkdwuLbl6n73HQUXUf1dse2PCgT1DYqW9w8AVZ1RACFGM+5UdlGPrQHrgtS3CvsRURC1oj73j8gCA==|98=0|108=30|141=Y|553=sBRXrJx2DsOraMXOaUovEhgVRcjOvCtQwnWj8VxkOh1xqboS02SPGfKi2h8spZJb|25035=2|10=227|

## 限制

### 消息限制

  * 每个连接都有一个关于 **可以发送到交易所的消息数量** 的限制。
  * 消息限制 **不计算从接口发回到客户端的响应消息数量** 。
  * 违反消息限制会立即导致 [Logout `<5>`](/zh-CN/docs/products/spot/fix-api#logout-5) 并断开连接。
  * 要了解当前的限制和使用情况，请发送 [LimitQuery`<XLQ>`](/zh-CN/docs/products/spot/fix-api#limitquery) 消息。接口将发送 [LimitResponse`<XLR>`](/zh-CN/docs/products/spot/fix-api#limitresponse) 消息作为响应，其中包含了有关订单速率限制和消息限制的信息。
  * FIX API 订单输入会话的限制为每 10 秒 10,000 条消息。
  * FIX Drop Copy 会话的限制为每 60 秒 60 条消息。
  * FIX Market Data 会话的限制为每 60 秒 2000 条消息。



### 未成交订单计数

  * 要了解您在特定时间间隔内下了多少订单，请发送 [LimitQuery`<XLQ>`](/zh-CN/docs/products/spot/fix-api#limitquery) 消息。系统将发送一条 [LimitResponse`<XLR>`](/zh-CN/docs/products/spot/fix-api#limitresponse) 消息作为响应，其中会包含有关未成交订单计数和消息限制的信息。
  * **请注意，如果您的订单一直顺利完成交易，您可以在 API 持续下订单** 。更多信息，请参见[现货未成交订单计数规则](/zh-CN/docs/products/spot/faqs/order_count_decrement)。
  * 如果您超过了未成交的订单计数限制，您的消息将被拒绝，并且信息将用该接口的拒绝消息格式传回给您。
  * **未成交订单数量是按照每个账户来统计的** 。



### 连接限制

  * 每个账户都有一个关于 **可以同时建立的 TCP 连接数量** 的限制。
  * 当 TCP 连接关闭时，限制值会减少。如果限制值没有立即减少，请等待最长不超过2倍于在 `HeartBtInt (108)` 内所定义的时间。比如说，如果 `HeartBtInt` 的值为5， 那么请等待10秒钟。
  * 违反限制时， [Reject `<3>`](/zh-CN/docs/products/spot/fix-api#reject) 消息会被发送给用户。该消息包含了有关违反连接限制和当前限制的信息。
  * FIX 订单接入会话限制：
    * 在 30 秒内 15 次连接尝试的限制
    * 每个账户 最多 10 个并发 TCP 连接的限制
  * FIX Drop Copy 会话限制：
    * 在 30 秒内 15 次连接尝试的限制
    * 每个账户 10 个并发 TCP 连接的限制
  * FIX Market Data 会话限制:
    * 在 300 秒内 300 次连接尝试的限制
    * 每个账户 100 个并发 TCP 连接的限制
    * 单一连接最多能监听 1000 个数据流



## 错误处理

包含句法错误，缺少必填字段，或引用未知交易对的客户端消息将被服务器拒绝，并返回 [Reject `<3>`](/zh-CN/docs/products/spot/fix-api#reject) 消息。

如果有效消息无法被处理并被拒绝，服务器将发送相应的拒绝响应。请参阅各个消息的相关文档以了解可能会发生的响应。

请参阅响应中的 `Text (58)` 和 `ErrorCode (25016)` 字段以了解拒绝原因。

错误代码列表可以在 [错误代码](/zh-CN/docs/products/spot/errors) 页面找到。

## 类型

仅支持可打印的 ASCII 字符和 SOH。

类型| 描述  
---|---  
`BOOLEAN`| Enum：`Y` 或 `N`.  
`CHAR`| 单个字符。  
`INT`| 有符号的 64 位整数。  
`LENGTH`| 无符号的 64 位整数。  
`NUMINGROUP`| 无符号的 64 位整数。  
`PRICE`| 定点数。精度取决于 symbol 定义。  
`QTY`| 定点数。精度取决于 symbol 定义。  
`SEQNUM`| 无符号的 32 位整数。达到最大值 4,294,967,295 后会归 0，然后重新开始计数。  
`STRING`| 可打印的 ASCII 字符串。  
`UTCTIMESTAMP`| 表示 UTC 日期时间的字符串。  
  
支持的 `UTCTIMESTAMP` 格式：

  * `20011217-09:30:47` \- 秒
  * `20011217-09:30:47.123` \- 毫秒
  * `20011217-09:30:47.123456` \- 微秒（用于来自交易所的消息）



客户端订单 ID 字段必须符合正则表达式 `^[a-zA-Z0-9-_]{1,36}$`：

  * `ClOrdID (11)`
  * `OrigClOrdID (41)`
  * `MDReqID (262)`
  * `ClListID (25014)`
  * `OrigClListID (25015)`
  * `CancelClOrdID (25034)`



## 消息组件

在示例消息中， `|` 字符用于表示 SOH 字符：
    
    
    Code
    
    8=FIX.4.4|9=113|35=A|34=1|49=SPOT|52=20240612-08:52:21.636837|56=5JQmUOsm|98=0|108=30|25037=4392a152-3481-4499-921a-6d42c50702e2|10=051|

### Header

出现在每条消息的开头。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
8| BeginString| STRING| Y| 始终为 `FIX.4.4`。  必须是消息的第一个字段。  
9| BodyLength| LENGTH| Y| 消息长度（以字节为单位）。  必须是消息的第二个字段。  
35| MsgType| STRING| Y| 必须是消息的第三个字段。  可能的值： `0` \- [HEARTBEAT](/zh-CN/docs/products/spot/fix-api#heartbeat) `1` \- [TEST_REQUEST](/zh-CN/docs/products/spot/fix-api#testrequest) `3` \- [REJECT](/zh-CN/docs/products/spot/fix-api#reject) `5` \- [LOGOUT](/zh-CN/docs/products/spot/fix-api#logout-5) `8` \- [EXECUTION_REPORT](/zh-CN/docs/products/spot/fix-api#executionreport) `9` \- [ORDER_CANCEL_REJECT](/zh-CN/docs/products/spot/fix-api#ordercancelreject) `A` \- [LOGON](/zh-CN/docs/products/spot/fix-api#logon-main) `D` \- [NEW_ORDER_SINGLE](/zh-CN/docs/products/spot/fix-api#newordersingle) `E` \- [NEW_ORDER_LIST](/zh-CN/docs/products/spot/fix-api#neworderlist) `F` \- [ORDER_CANCEL_REQUEST](/zh-CN/docs/products/spot/fix-api#ordercancelrequest) `N` \- [LIST_STATUS](/zh-CN/docs/products/spot/fix-api#liststatus) `q` \- [ORDER_MASS_CANCEL_REQUEST](/zh-CN/docs/products/spot/fix-api#ordermasscancelrequest) `r` \- [ORDER_MASS_CANCEL_REPORT](/zh-CN/docs/products/spot/fix-api#ordermasscancelreport) `XCN` \- [ORDER_CANCEL_REQUEST_AND_NEW_ORDER_SINGLE](/zh-CN/docs/products/spot/fix-api#ordercancelrequestandnewordersingle) `XLQ` \- [LIMIT_QUERY](/zh-CN/docs/products/spot/fix-api#limitquery) `XLR` \- [LIMIT_RESPONSE](/zh-CN/docs/products/spot/fix-api#limitresponse) `B` \- [NEWS](/zh-CN/docs/products/spot/fix-api#news) `x`\- [INSTRUMENT_LIST_REQUEST](/zh-CN/docs/products/spot/fix-api#instrumentlistrequest) `y` \- [INSTRUMENT_LIST](/zh-CN/docs/products/spot/fix-api#instrumentlist) `V` \- [MARKET_DATA_REQUEST](/zh-CN/docs/products/spot/fix-api#marketdatarequest) `Y` \- [MARKET_DATA_REQUEST_REJECT](/zh-CN/docs/products/spot/fix-api#marketdatarequestreject) `W` \- [MARKET_DATA_SNAPSHOT](/zh-CN/docs/products/spot/fix-api#marketdatasnapshot) `X` \- [MARKET_DATA_INCREMENTAL_REFRESH](/zh-CN/docs/products/spot/fix-api#marketdataincrementalrefresh) `XAK` \- [ORDER_AMEND_KEEP_PRIORITY_REQUEST](/zh-CN/docs/products/spot/fix-api#orderamendkeeppriorityrequest) `XAR` \- [ORDER_AMEND_REJECT](/zh-CN/docs/products/spot/fix-api#orderamendreject)  
49| SenderCompID| STRING| Y| 在账户的活动会话中必须是独特的。 必须使用正则表达式：`^[a-zA-Z0-9-_]{1,8}$`  
56| TargetCompID| STRING| Y| 在客户端的消息中必须设置为`SPOT`。  
34| MsgSeqNum| SEQNUM| Y| 整数消息序列号。  会导致间隙的值将被拒绝。  
52| SendingTime| UTCTIMESTAMP| Y| 消息传输时间（始终以 UTC 表示）。  
25000| RecvWindow| FLOAT| N| 在`SendingTime (52)` 后，用于标识请求有效时间的毫秒数。  在 [Logon`<A>`](/zh-CN/docs/products/spot/fix-api#logon-request) 中默认为 `5000` 毫秒，最大值为 `60000` 毫秒。  支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
  
### Trailer

出现在每条消息的末尾。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
10| CheckSum| STRING| Y| 始终为3个字符的数字字符串。其取值是通过对消息中每个前导字符的 ASCII 值进行求和计算得出的，其中包括 start-of-header（SOH）。  结果总和除以 256，余数形成 CheckSum 值。  为保持固定长度，CheckSum 字段采用右对齐并按需要进行零填充。  
  
## Administrative Messages

### Heartbeat `<0>`

如果在心跳间隔（[Logon`<A>`](/zh-CN/docs/products/spot/fix-api#logon) 中的 `HeartBtInt (108)`）的期间没有传出流量，则由服务器发送。

由客户端发送则用于指示会话正常。

由客户端或服务器发送，用于给予 [TestRequest`<1>`](/zh-CN/docs/products/spot/fix-api#testrequest) 消息有关响应。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
112| TestReqID| STRING| N| 当 Heartbeat`<35>` 作为对 TestRequest`<1>` 的响应发送时，必须镜像 TestRequest`<1>` 中的值。  
  
### TestRequest `<1>`

如果在心跳间隔（[Logon`<A>`](/zh-CN/docs/products/spot/fix-api#logon-main) 中的 `HeartBtInt (108)`）的期间没有传入流量，则由服务器发送。

由客户端发送用于请求 [Heartbeat`<0>`](/zh-CN/docs/products/spot/fix-api#heartbeat) 响应。

如果客户端未能在超时范围内发送带有正确 `TestReqID (112)` 的 Heartbeat`<0>` 来响应 TestRequest`<1>` ，其连接将被断开。

Tag| 名称| 类型| 必填| 描述  
---|---|---|---|---  
112| TestReqID| STRING| Y| 任意字符串，必须包含在 Heartbeat`<0>` 响应中。  
  
### Reject `<3>`

由服务器发送，用以响应无法处理的无效消息。

如果无法接受新连接，则由服务器发送。请参阅 [Connection Limits](/zh-CN/docs/products/spot/fix-api#connection-limits)。

请参阅 `Text (58)` 和 `ErrorCode (25016)` 字段以了解拒绝原因。

Tag| 名称| 类型| 必填| 描述  
---|---|---|---|---  
45| RefSeqNum| INT| N| 导致此 Reject`<3>` 发送的被拒绝消息的 `MsgSeqNum (34)`。  
371| RefTagID| INT| N| 如果存在，标识直接导致此 Reject`<3>` 消息发送的字段。  
372| RefMsgType| STRING| N| 导致此 Reject`<3>` 发送的被拒绝消息的 `MsgType (35)`。  
373| SessionRejectReason| INT| N| 拒绝的原因，可以是以下值之一。  通常伴随附加的文字描述  可能的值： `0`\- INVALID_TAG_NUMBER  `1` \- REQUIRED_TAG_MISSING  `2` \- TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE  `3` \- UNDEFINED_TAG  `5` \- VALUE_IS_INCORRECT  `6` \- INCORRECT_DATA_FORMAT_FOR_VALUE  `8` \- SIGNATURE_PROBLEM  `10` \- SENDINGTIME_ACCURACY_PROBLEM  `12` \- XML_VALIDATION_ERROR  `13` \- TAG_APPEARS_MORE_THAN_ONCE  `14` \- TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER  `15` \- REPEATING_GROUP_FIELDS_OUT_OF_ORDER  `16` \- INCORRECT_NUMINGROUP_COUNT_FOR_REPEATING_GROUP `99` \- OTHER  
25016| ErrorCode| INT| N| API 错误代码（参见 [错误代码](/zh-CN/docs/products/spot/errors)）。  
58| Text| STRING| N| 人类可读的错误信息。  
  
### Logon `<A>`

由客户端发送，用以验证连接。Logon`<A>` 必须是客户端发送的第一条消息。

由服务器发送，用以响应成功的登录。

Logon`<A>` 在整个会话期间只能发送一次。

#### Logon Request

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
98| EncryptMethod| INT| Y| 必须为 `0`。  
108| HeartBtInt| INT| Y| 必须在 [5, 60] 范围内。Heartbeat 间隔（秒）。  
95| RawDataLength| LENGTH| Y| 紧随此字段之后的 `RawData (96)` 字段的长度。  
96| RawData| DATA| Y| 签名。 [如何签署 Logon`<A>` 请求](/zh-CN/docs/products/spot/fix-api#signaturecomputation)。  
141| ResetSeqNumFlag| BOOLEAN| Y| 必须为 `Y`。  
553| Username| STRING| Y| API key。**仅支持 Ed25519 API keys。**  
25035| MessageHandling| INT| Y| 可能的值:  `1` \- UNORDERED  `2` \- SEQUENTIAL  请参阅 [关于消息处理顺序](/zh-CN/docs/products/spot/fix-api#orderedmode) 了解更多信息。  
25036| ResponseMode| INT| N| 请参阅 [响应模式](/zh-CN/docs/products/spot/fix-api#responsemode)。  
9406| DropCopyFlag| BOOLEAN| N| 登录到 Drop Copy 会话时，必须设置为"Y"。  
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=248|35=A|34=1|49=5JQmUOsm|52=20240612-08:52:21.613|56=SPOT|95=88|96=KhJLbZqADWknfTAcp0ZjyNz36Kxa4ffvpNf9nTIc+K5l35h+vA1vzDRvLAEQckyl6VDOwJ53NOBnmmRYxQvQBQ==|98=0|108=30|141=Y|553=W5rcOD30c0gT4jHK8oX5d5NbzWoa0k4SFVoTHIFNJVZ3NuRpYb6ZyJznj8THyx5d|25035=1|10=000|

#### Logon Response

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
98| EncryptMethod| INT| Y| 始终为 `0`。  
108| HeartBtInt| INT| Y| 镜像 Logon 请求中的值。  
25037| UUID| STRING| Y| 提供请求服务的 FIX API 的 UUID。  
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=113|35=A|34=1|49=SPOT|52=20240612-08:52:21.636837|56=5JQmUOsm|98=0|108=30|25037=4392a152-3481-4499-921a-6d42c50702e2|10=051|

### Logout `<5>`

发送此消息以启动关闭连接的过程，并对 Logout 进行响应。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
58| Text| STRING| N|   
  
**示例消息:**

Logout 请求
    
    
    Code
    
    8=FIX.4.4|9=55|35=5|34=3|49=GhQHzrLR|52=20240611-09:44:25.543|56=SPOT|10=249|

Logout 响应
    
    
    Code
    
    8=FIX.4.4|9=84|35=5|34=4|49=SPOT|52=20240611-09:44:25.544001|56=GhQHzrLR|58=Logout acknowledgment.|10=212|

### News `<B>`

当服务器进入维护状态时，系统将会向客户端**每隔 10 秒发送一条** `News` 消息，并倒计时至断开连接。

如果客户端在服务器断开连接前没有关闭旧会话，那么服务器会将其注销并关闭会话。

收到此消息后，客户端应建立新会话并关闭旧会话。

发送的倒计时消息将是：
    
    
    Code
    
    You'll be disconnected in %d seconds. Please reconnect.

剩余 10 秒时，系统将发送以下消息：
    
    
    Code
    
    Your connection is about to be closed. Please reconnect.

如果客户端在收到上述消息后的 10 秒内没有关闭旧会话，那么服务器会将其注销并关闭会话。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
148| Headline| STRING| Y|   
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=0000113|35=B|49=SPOT|56=OE|34=4|52=20240924-21:07:35.773537|148=Your connection is about to be closed. Please reconnect.|10=165|

### Resend Request `<2>`

目前不支持重新发送请求。

## Application Messages

### 下单消息

以下消息只能用于 FIX 订单接入会话和 FIX Drop Copy 会话

#### NewOrderSingle `<D>`

由客户端发送，用以提交新订单并进行执行。

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

**未成交的订单计数:** 1

请参阅 [支持的订单类型](/zh-CN/docs/products/spot/fix-api#ordertype) 了解支持的字段组合。

许多字段会根据订单类型变为必填。请参阅 [支持的订单类型](/zh-CN/docs/products/spot/fix-api#NewOrderSingle-required-fields)。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
11| ClOrdID| STRING| Y| 分配给订单的 `ClOrdID`。  
38| OrderQty| QTY| N| 订单数量  
40| OrdType| CHAR| Y| 请参阅 [表格](/zh-CN/docs/products/spot/fix-api#ordertype) 了解支持的订单类型和所需字段。可能的值:  `1` \- MARKET  `2` \- LIMIT  `3` \- STOP  `4` \- STOP_LIMIT  `P`\- PEGGED  
18| ExecInst| CHAR| N| 可能的值:  `6` \- PARTICIPATE_DONT_INITIATE  
44| Price| PRICE| N| 订单价格  
54| Side| CHAR| Y| 订单方向。可能的值:  `1` \- BUY  `2` \- SELL  
55| Symbol| STRING| Y| 下单的交易对。  
59| TimeInForce| CHAR| N| 可能的值:  `1` \- GOOD_TILL_CANCEL  `3` \- IMMEDIATE_OR_CANCEL  `4` \- FILL_OR_KILL  
111| MaxFloor| QTY| N| 用于冰山订单，指定订单在订单簿上的可见数量。  
152| CashOrderQty| QTY| N| 以报价资产单位指定的订单数量，用于反向市场订单。  
847| TargetStrategy| INT| N| 该值不能小于 `1000000`。  
7940| StrategyID| INT| N|   
25001| SelfTradePreventionMode| CHAR| N| 可能的值:  `1` \- NONE  `2` \- EXPIRE_TAKER  `3` \- EXPIRE_MAKER  `4` \- EXPIRE_BOTH  `5` \- DECREMENT  `6` \- TRANSFER  
211| PegOffsetValue| FLOAT| N| 使用了 `PegOffsetType` 后，添加到挂钩的偏移值  
1094| PegPriceType| CHAR| N| 定义了挂钩价格的类型  可能的值:  `4` \- MARKET_PEG  `5` \- PRIMARY_PEG  
835| PegMoveType| CHAR| N| 描述挂钩是固定的还是浮动的。挂钩订单必用且必须为 `1` (FIXED)  
836| PegOffsetType| CHAR| N| 定义了挂钩价格偏移类型。  可能的值:  `3` \- PRICE_TIER  
1100| TriggerType| CHAR| N| 可能的值: `4` \- PRICE_MOVEMENT  
1101| TriggerAction| CHAR| N| 可能的值:  `1` \- ACTIVATE  
1102| TriggerPrice| PRICE| N| 止盈止损订单的激活价格。请参阅 [表格](/zh-CN/docs/products/spot/fix-api#ordertype)  
1107| TriggerPriceType| CHAR| N| 可能的值:  `2` \- LAST_TRADE  
1109| TriggerPriceDirection| CHAR| N| 用于区分 StopLoss 和 TakeProfit 订单。请参阅 [表格](/zh-CN/docs/products/spot/fix-api#ordertype)。可能的值:  `U` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  `D` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  
25009| TriggerTrailingDeltaBips| INT| N| 提供以创建追踪订单。  
25032| SOR| BOOLEAN| N| 是否为此订单激活 SOR。  
25057| QuoteNotionalLimit| QTY| N| 仅适用于买单。订单可消耗的报价资产名义价值上限。不能与 `CashOrderQty (152)`、`SOR (25032)` 或 `ExecInst (18)` = `6` 同时使用。参见 [quoteNotionalLimit 常见问题](/zh-CN/docs/products/spot/faqs/quoteNotionalLimit)。  
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=114|35=D|34=2|49=qNXO12fH|52=20240611-09:01:46.228|56=SPOT|11=1718096506197867067|38=5|40=2|44=10|54=1|55=LTCBNB|59=4|10=016|

**响应:**

  * 如果订单被接受， [ExecutionReport`<8>`](/zh-CN/docs/products/spot/fix-api#executionreport)的 `ExecType (150)` 值为 `NEW (0)`。
  * 如果订单被拒绝， [ExecutionReport`<8>`](/zh-CN/docs/products/spot/fix-api#executionreport)的 `ExecType (150)` 值为 `REJECTED (8)`。
  * 如果消息被拒绝，则为 [Reject`<3>`](/zh-CN/docs/products/spot/fix-api#reject)。



##### 支持的订单类型

订单名称| Binance OrderType| 方向| 必填字段值| 用户值必填字段  
---|---|---|---|---  
Market order| `MARKET`| BUY 或 SELL| 40=1||   
Limit order| `LIMIT`| BUY 或 SELL| 40=2||   
Limit maker order| `LIMIT_MAKER`| BUY 或 SELL| 40=2|18=6||   
Buy stop loss order| `STOP_LOSS`| BUY| 40=3|1100=4|1101=1|1107=2|1109=U|| 1102  
Buy trailing stop loss order| `STOP_LOSS`| BUY| 40=3|1100=4|1101=1|1107=2|1109=U|| 1102,25009  
Buy stop loss limit order| `STOP_LOSS_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|1109=U|| 1102  
Buy trailing stop loss limit order| `STOP_LOSS_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|1109=U|| 1102,25009  
Sell stop loss order| `STOP_LOSS`| SELL| 40=3|1100=4|1101=1|1107=2|1109=D|| 1102  
Sell trailing stop loss order| `STOP_LOSS`| SELL| 40=3|1100=4|1101=1|1107=2|1109=D|| 1102,25009  
Sell stop loss limit order| `STOP_LOSS_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|1109=D|| 1102  
Sell trailing stop loss limit order| `STOP_LOSS_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|1109=D|| 1102,25009  
Buy take profit order| `TAKE_PROFIT`| BUY| 40=3|1100=4|1101=1|1107=2|1109=D|| 1102  
Buy trailing take profit order| `TAKE_PROFIT`| BUY| 40=3|1100=4|1101=1|1107=2|1109=D|| 1102,25009  
Buy trailing take profit order| `TAKE_PROFIT`| BUY| 40=3|1100=4|1101=1|1107=2|| 25009  
Buy take profit order| `TAKE_PROFIT_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|1109=D|| 1102  
Buy trailing take profit limit order| `TAKE_PROFIT_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|1109=D|| 1102,25009  
Buy trailing take profit limit order| `TAKE_PROFIT_LIMIT`| BUY| 40=4|1100=4|1101=1|1107=2|| 25009  
Sell take profit order| `TAKE_PROFIT`| SELL| 40=3|1100=4|1101=1|1107=2|1109=U|| 1102  
Sell trailing take profit order| `TAKE_PROFIT`| SELL| 40=3|1100=4|1101=1|1107=2|1109=U|| 1102,25009  
Sell trailing take profit order| `TAKE_PROFIT`| SELL| 40=3|1100=4|1101=1|1107=2|| 25009  
Sell take profit limit order| `TAKE_PROFIT_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|1109=U|| 1102  
Sell trailing take profit limit order| `TAKE_PROFIT_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|1109=U|| 1102,25009  
Sell trailing take profit limit order| `TAKE_PROFIT_LIMIT`| SELL| 40=4|1100=4|1101=1|1107=2|| 25009  
  
基于 Binance OrderType 的必填字段:

Binance OrderType| 额外的必填字段| 额外的信息  
---|---|---  
`LIMIT`| 38, 44, 59|   
`MARKET`| 38 或 152| `MARKET` 订单使用 `OrderQty (38)` 字段来指定用户希望以市场价格买入或卖出的 `base asset` 数量。 例如，用户可以使用交易对为 `BTCUSDT` 的 `MARKET` 订单来指定买入或卖出多少 BTC。 用户使用 `MARKET` 订单中的 `quoteOrderQty` 字段来指定花费（买入时）或接收（卖出时）`quote` 资产。正确的 `quantity` 将由市场流动性和 `quoteOrderQty` 来决定。  用交易对 BTCUSDT来举例： `BUY` 方订单将使用由 `quoteOrderQty` 定义的 USDT 数额来购买尽可能多的 BTC。 `SELL` 方订单将出售 BTC 来换取尽可能多的由 `CashOrderQty（152)` 定义的 USDT 数额。  
`STOP_LOSS`| 38, 1102 或 25009| 当满足条件时，将执行 `MARKET` 订单。（例如，满足 `TriggerPrice (1102)` 的条件或激活 `TriggerTrailingDeltaBips (25009)`）  
`STOP_LOSS_LIMIT`| 38, 44, 59, 1102 或 25009|   
`TAKE_PROFIT`| 38, 1102 或 25009| 当满足条件时，这将执行`MARKET`订单。（例如，满足 `TriggerPrice (1102)` 的条件或激活 `TriggerTrailingDeltaBips (25009)`）  
`TAKE_PROFIT_LIMIT`| 38, 44, 59, 1102 或 25009|   
`LIMIT_MAKER`| 38, 44| 这是一个 `LIMIT` 订单。如果订单被立即匹配并作为 taker 进行交易，那么该订单将被拒绝。 这也称为 POST-ONLY 订单。  
  
#### ExecutionReport `<8>`

每当订单状态发生变化时由服务器发送。

  * 默认情况下，ExecutionReport`<8>` 会发送该账户的所有订单，包括在不同连接中提交的订单。 请参阅 [响应模式](/zh-CN/docs/products/spot/fix-api#responsemode) 来了解其他行为选项。
  * FIX API 应该为 ExecutionReport<8> 推送提供更好的性能。



Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
17| ExecID| STRING| N| 被拒绝订单时省略。  
11| ClOrdID| STRING| N| 列表中分配的 `ClOrdID`。  
41| OrigClOrdID| STRING| N| 订单的原始 `ClOrdID`。  
37| OrderID| INT| N| 由交易所分配。  
38| OrderQty| QTY| N| 订单数量。  
40| OrdType| CHAR| Y| 可能的值:  `1` \- MARKET  `2` \- LIMIT  `3` \- STOP_LOSS  `4` \- STOP_LIMIT  `P` \- PEGGED  
54| Side| CHAR| Y| 可能的值:  `1` \- BUY  `2` \- SELL  
55| Symbol| STRING| Y| 订单的交易对。  
18| ExecInst| CHAR| N| 可能的值:  `6` \- PARTICIPATE_DONT_INITIATE  
44| Price| PRICE| N| 订单价格。  
59| TimeInForce| CHAR| N| 可能的值:  `1` \- GOOD_TILL_CANCEL  `3` \- IMMEDIATE_OR_CANCEL  `4` \- FILL_OR_KILL  
60| TransactTime| UTCTIMESTAMP| N| 此事件发生的时间戳。  
25018| OrderCreationTime| INT| N|   
111| MaxFloor| QTY| N| 出现在冰山订单中。  
66| ListID| STRING| N| 出现在列表订单中。  
152| CashOrderQty| QTY| N| 以 quote asset 单位指定的订单数量。  
847| TargetStrategy| INT| N| 订单提交请求中的 `TargetStrategy (847)`。  
7940| StrategyID| INT| N| 订单提交请求中的 `StrategyID (7940)`。  
25001| SelfTradePreventionMode| CHAR| N| 可能的值:  `1` \- NONE  `2` \- EXPIRE_TAKER  `3` \- EXPIRE_MAKER `4` \- EXPIRE_BOTH  `5` \- DECREMENT  `6` \- TRANSFER  
150| ExecType| CHAR| Y| **注意:** 如果订单因 `SelfTradePreventionMode(25013)` 过期，字段 `PreventedMatchID(25024)` 会被显示。  可能的值:  `0` \- NEW  `4` \- CANCELED  `5` \- REPLACED  `8` \- REJECTED  `F` \- TRADE `C` \- EXPIRED  
14| CumQty| QTY| Y| 在此订单上交易的 base asset 总数。  
151| LeavesQty| QTY| N| 剩余的可执行数量。  
25017| CumQuoteQty| QTY| N| 在此订单上交易的 quote asset 总数。  
1057| AggressorIndicator| BOOLEAN| N| 出现在 trade execution reports 中。 指示订单在交易中是否为 taker。  
1003| TradeID| STRING| N| 出现在 trade execution reports 中。  
31| LastPx| PRICE| N| 最后一次执行的价格。  
32| LastQty| QTY| Y| 最后一次执行的数量。  
39| OrdStatus| CHAR| Y| 可能的值:  `0` \- NEW  `1` \- PARTIALLY_FILLED  `2` \- FILLED  `4` \- CANCELED `6` \- PENDING_CANCEL `8` \- REJECTED  `A` \- PENDING_NEW  `C` \- EXPIRED  注意 FIX 不支持 `EXPIRED_IN_MATCH` 状态，并在 FIX 中转换为 `EXPIRED`。  
70| AllocID| INT| N| 由交易所分配的分配 ID。  
574| MatchType| INT| N| 可能的值:`1` \- ONE_PARTY_TRADE_REPORT`4` \- AUTO_MATCH  
25021| WorkingFloor| INT| N| 出现在可能有分配的订单中。  
25022| TrailingTime| UTCTIMESTAMP| N| 仅出现在追踪止损订单中。  
636| WorkingIndicator| BOOLEAN| N| 当此订单进入订单簿时会被设置为 `Y`。  
25023| WorkingTime| UTCTIMESTAMP| N| 此订单出现在订单簿上的时间。  
25024| PreventedMatchID| INT| N| 仅出现在因 STP 过期的订单中。  
25025| PreventedExecutionPrice| PRICE| N| 仅出现在因 STP 过期的订单中。  
25026| PreventedExecutionQty| QTY| N| 仅出现在因 STP 过期的订单中。  
25027| TradeGroupID| INT| N| 仅出现在因 STP 过期的订单中。  
25028| CounterSymbol| STRING| N| 仅出现在因 STP 过期的订单中。  
25029| CounterOrderID| INT| N| 仅出现在因 STP 过期的订单中。  
25030| PreventedQty| QTY| N| 仅出现在因 STP 过期的订单中。  
25031| LastPreventedQty| QTY| N| 仅出现在因 STP 过期的订单中。  
25032| SOR| BOOLEAN| N| 出现在使用 SOR 的订单中。  
25057| QuoteNotionalLimit| QTY| N| 仅当订单发送了 `QuoteNotionalLimit (25057)` 时出现。  
25016| ErrorCode| INT| N| API 错误代码（请参阅 [错误代码](/zh-CN/docs/products/spot/errors)）。  
58| Text| STRING| N| 可读的错误消息。  
25056| ExpiryReason| INT| N| 仅出现在已过期的订单中。可能的值:`1` \- REJECTED`2` \- EXCHANGE_CANCELED`3` \- OCO_TRIGGER`4` \- OTO_PHASE_ONE_EXPIRED`5` \- UNFILLED_IOC_QUANTITY_EXPIRED`6` \- UNFILLED_FOK_ORDER_EXPIRED`7` \- INSUFFICIENT_LIQUIDITY`8` \- EXECUTION_RULE_PRICE_RANGE_EXCEEDED`9` \- EXHAUSTED`10` \- INSUFFICIENT_QUOTE_NOTIONAL_LIMIT  
25058| EffectiveSelfTradePreventionMode| CHAR| N| 仅在预防撮合的执行报告中，且撮合引擎实际生效的 STP 模式与订单的 `SelfTradePreventionMode (25001)` 不同时出现。可能的值:`3` \- EXPIRE_MAKER`4` \- EXPIRE_BOTH`5` \- DECREMENT  
136| NoMiscFees| NUMINGROUP| N| 杂费的重复组数量。  
=>137| MiscFeeAmt| QTY| Y| 以 `MiscFeeCurr(138)` 资产计价的费用金额  
=>138| MiscFeeCurr| STRING| Y| 杂费的货币。  
=>139| MiscFeeType| INT| Y| 可能的值: `4` \- EXCHANGE_FEES  
1100| TriggerType| CHAR| N| 可能的值: `4` \- PRICE_MOVEMENT  
1101| TriggerAction| CHAR| N| 可能的值:  `1` \- ACTIVATE  
1102| TriggerPrice| PRICE| N| 止盈止损订单的激活价格。请参阅 [表格](/zh-CN/docs/products/spot/fix-api#ordertype)  
1107| TriggerPriceType| CHAR| N| 可能的值:  `2` \- LAST_TRADE  
1109| TriggerPriceDirection| CHAR| N| 用于区分止损和止盈订单。请参阅 [表格](/zh-CN/docs/products/spot/fix-api#ordertype)。可能的值:  `U` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  `D` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  
25009| TriggerTrailingDeltaBips| INT| N| 仅出现在追踪止损订单中。  
211| PegOffsetValue| FLOAT| N| 使用了 `PegOffsetType` 后，添加到挂钩的偏移值  
1094| PegPriceType| CHAR| N| 定义了挂钩价格的类型  可能的值:  `4` \- MARKET_PEG  `5` \- PRIMARY_PEG  
835| PegMoveType| CHAR| N| 描述挂钩是固定的还是浮动的。挂钩订单必用且必须为 `1` (FIXED)  
836| PegOffsetType| CHAR| N| 定义了挂钩价格偏移类型。  可能的值:  `3` \- PRICE_TIER  
839| PeggedPrice| PRICE| N| 订单所挂钩的当前价格  
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=330|35=8|34=2|49=SPOT|52=20240611-09:01:46.228950|56=qNXO12fH|11=1718096506197867067|14=0.00000000|17=144|32=0.00000000|37=76|38=5.00000000|39=0|40=2|44=10.00000000|54=1|55=LTCBNB|59=4|60=20240611-09:01:46.228000|150=0|151=5.00000000|636=Y|1057=Y|25001=1|25017=0.00000000|25018=20240611-09:01:46.228000|25023=20240611-09:01:46.228000|10=095|

#### OrderCancelRequest `<F>`

由客户发送的，用以取消订单或订单列表。

  * 要取消订单，需要 `OrderID (11)` 或 `OrigClOrdID (41)`。
    * 当同时提供 `OrderID (37)` 和 `OrigClOrdID (41)` 两个参数时，系统首先将会使用 `OrderID` 来搜索订单。然后， 查找结果中的 `OrigClOrdID` 的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。
  * 要取消订单列表，需要 `ListID (66)` 或 `OrigClListID (25015)`。
    * 当同时提供 `ListID (66)` 和 `OrigClListID (25015)` 两个参数时，系统首先将会使用 `ListID` 来搜索订单列表。然后， 查找结果中的 `OrigClListID` 将会被用来验证订单列表。如果两个条件都不满足，请求将被拒绝。



如果已取消的订单是订单列表的一部分，则整个订单列表将被取消。

**注意：**

  * 当仅发送 `orderId` 时，取消订单的执行(单个 Cancel 或作为 Cancel-Replace 的一部分)总是更快。发送 `origClientOrderId` 或同时发送 `orderId` \+ `origClientOrderId` 会稍慢。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
11| ClOrdID| STRING| Y| 请求的 `ClOrdID`。  
41| OrigClOrdID| STRING| N| 要取消订单的 `ClOrdID (11)`。  
37| Order ID| STRING| N| 要取消订单的 `OrderID (37)`。  
25015| OrigClListID| STRING| N| 要取消订单列表的 `ClListID (25014)`。  
66| ListID| STRING| N| 要取消订单列表的 `ListID (66)`。  
55| Symbol| STRING| Y| 要取消订单的交易对。  
25002| CancelRestrictions| INT| N| 取消的限制。可能的值： `1` \- ONLY_NEW  `2` \- ONLY_PARTIALLY_FILLED  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=93|35=F|34=2|49=ieBwvCKy|52=20240613-01:11:13.784|56=SPOT|11=1718241073695674483|37=2|55=LTCBNB|10=210|

**响应：**

  * 对于每个被取消的订单，[ExecutionReport`<8>`](/zh-CN/docs/products/spot/fix-api#executionreport)的 `ExecType (150)` 值为 `CANCELED (4)`。
  * 如果订单列表中的订单被取消，则为 [ListStatus`<N>`](/zh-CN/docs/products/spot/fix-api#liststatus)。
  * 如果取消被拒绝，则为 [OrderCancelReject`<9>`](/zh-CN/docs/products/spot/fix-api#ordercancelreject)。
  * 如果消息被拒绝，则为 [Reject`<3>`](/zh-CN/docs/products/spot/fix-api#reject)。



#### OrderCancelReject `<9>`

当 [OrderCancelRequest`<F>`](/zh-CN/docs/products/spot/fix-api#ordercancelrequest) 失败时，由服务器发送的消息。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
11| ClOrdID| STRING| Y| 来自取消请求的 `ClOrdID (11)`。  
41| OrigClOrdID| STRING| N| 来自取消请求的 `OrigClOrdID (41)`。  
37| OrderID| INT| N| 来自取消请求的 `OrderID (37)`。  
25015| OrigClListID| STRING| N| 来自取消请求的 `OrigClListID (25015)`。  
66| ListID| STRING| N| 来自取消请求的 `ListID (66)`。  
55| Symbol| STRING| Y| 来自取消请求的 `Symbol (55)`。  
25002| CancelRestrictions| INT| N| 来自取消请求的 `CancelRestrictions (25002)`。  
434| CxlRejResponseTo| CHAR| Y| 此 OrderCancelReject`<9>` 响应的请求类型。 可能的值：  `1` \- ORDER_CANCEL_REQUEST  
25016| ErrorCode| INT| Y| API error code (参考 [错误代码](/zh-CN/docs/products/spot/errors)).  
58| Text| STRING| Y| 可读的错误消息。  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=137|35=9|34=2|49=SPOT|52=20240613-01:12:41.320869|56=OlZb8ht8|11=1718241161272843932|37=2|55=LTCBNB|58=Unknown order sent.|434=1|25016=-1013|10=087|

#### OrderCancelRequestAndNewOrderSingle `<XCN>`

由客户发送，用以取消订单并提交新订单以供执行。

  * 要取消订单，需要 `OrderID (11)` 或 `OrigClOrdId (41)`。
  * 当同时提供 `OrderID (37)` 和 `OrigClOrdID (41)` 两个参数时，系统首先将会使用 `OrderID` 来搜索订单。然后， 查找结果中的 `OrigClOrdID` 的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。



在撤消订单和下单前会判断: 1) 过滤器参数, 以及 2) 目前下单数量。

即使请求中没有尝试发送新订单，比如(`newOrderResult: NOT_ATTEMPTED`)，未成交订单的数量仍然会加1。

**未成交的订单计数:** 1

在描述新订单时，请参阅 [支持的订单类型](/zh-CN/docs/products/spot/fix-api#ordertype) 了解支持的字段组合。

取消始终是优先处理的，紧接着的是提交新订单。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
25033| OrderCancelRequestAndNewOrderSingleMode| INT| Y| 用于定义： 如果取消失败，将会采取的后续操作 。  可能的值 ：  `1` \- STOP_ON_FAILURE  `2` -ALLOW_FAILURE  
25038| OrderRateLimitExceededMode| INT| N| 用于定义： 如果超过未成交订单计数，将会如何处理取消请求。 可能的值 ： `1` \- DO_NOTHING  `2` \- CANCEL_ONLY  
37| OrderID| INT| N| 来自于取消订单的 `OrderID`。  
25034| CancelClOrdID| STRING| N| 待取消的 `ClOrdID`。  
41| OrigClOrdID| STRING| N| 来自待取消订单的 `ClOrdID`。  
11| ClOrdID| STRING| Y| 用于分配给新订单的 `ClOrdID`。  
25002| CancelRestrictions| INT| N| 取消的限制。可能值 ： `1` \- ONLY_NEW  `2` \- ONLY_PARTIALLY_FILLED  
38| OrderQty| QTY| N| 新订单的数量  
40| OrdType| CHAR| Y| 请参阅 [表格](/zh-CN/docs/products/spot/fix-api#ordertype) 以了解支持的订单类型以及相关的必填字段 。  可能的值 ： `1` \- MARKET  `2` \- LIMIT  `3` \- STOP  `4` \- STOP_LIMIT  `P` \- PEGGED  
18| ExecInst| CHAR| N| 可能的值：  `6` \- PARTICIPATE_DONT_INITIATE  
44| Price| PRICE| N| 新订单的价格  
54| Side| CHAR| Y| 订单方向。可能的值：  `1` \- BUY  `2` \- SELL  
55| Symbol| STRING| Y| 取消并下新订单所用的交易对。  
59| TimeInForce| CHAR| N| 可能的值 ：  `1` \- GOOD_TILL_CANCEL  `3` \- IMMEDIATE_OR_CANCEL  `4` \- FILL_OR_KILL  
111| MaxFloor| QTY| N| 用于冰山订单，用于定义订单在 orderbook 上的可见数量。  
152| CashOrderQty| QTY| N| 用于反向市价单，用于定义 quote asset 单位中的订单数量。  
847| TargetStrategy| INT| N| 该值不能小于 `1000000`。  
7940| StrategyID| INT| N|   
25001| SelfTradePreventionMode| CHAR| N| 可能的值:  `1` \- NONE  `2` \- EXPIRE_TAKER  `3` \- EXPIRE_MAKER  `4` \- EXPIRE_BOTH  `5` \- DECREMENT  `6` \- TRANSFER  
211| PegOffsetValue| FLOAT| N| 使用了 `PegOffsetType` 后，添加到挂钩的偏移值  
1094| PegPriceType| CHAR| N| 定义了挂钩价格的类型  可能的值:  `4` \- MARKET_PEG  `5` \- PRIMARY_PEG  
835| PegMoveType| CHAR| N| 描述挂钩是固定的还是浮动的。挂钩订单必用且必须为 `1` (FIXED)  
836| PegOffsetType| CHAR| N| 定义了挂钩价格偏移类型。  可能的值:  `3` \- PRICE_TIER  
1100| TriggerType| CHAR| N| 可能的值: `4` \- PRICE_MOVEMENT  
1101| TriggerAction| CHAR| N| 可能的值:  `1` \- ACTIVATE  
1102| TriggerPrice| PRICE| N| 止盈止损订单的激活价格。参见 [表格](/zh-CN/docs/products/spot/fix-api#ordertype)  
1107| TriggerPriceType| CHAR| N| 可能的值  `2` \- LAST_TRADE  
1109| TriggerPriceDirection| CHAR| N| 用于区分止损订单和止盈订单。参考 [表格](/zh-CN/docs/products/spot/fix-api#ordertype) . 可能的值 ：  `U` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  `D` -TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  
25009| TriggerTrailingDeltaBips| INT| N| 用以创建追踪订单。  
25057| QuoteNotionalLimit| QTY| N| 仅适用于买单方向的替换订单。新订单可消耗的报价资产名义价值上限。不能与 `CashOrderQty (152)` 或 `ExecInst (18)` = `6` 同时使用。参见 [quoteNotionalLimit 常见问题](/zh-CN/docs/products/spot/faqs/quoteNotionalLimit)。  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=160|35=XCN|34=2|49=JS8iiXK6|52=20240613-02:31:53.753|56=SPOT|11=1718245913721036458|37=8|38=5|40=2|44=4|54=1|55=LTCBNB|59=1|111=1|25033=1|25034=1718245913721036819|10=229|

**响应：**

  * 对于每个被取消的订单，[ExecutionReport`<8>`](/zh-CN/docs/products/spot/fix-api#executionreport) 的 `ExecType (150)` 值为 `CANCELED (4)`。
  * 对于新订单，[ExecutionReport`<8>`](/zh-CN/docs/products/spot/fix-api#executionreport) 的 `ExecType (150)` 值为 `NEW (0)`。
  * 如果新订单被拒绝，[ExecutionReport`<8>`](/zh-CN/docs/products/spot/fix-api#executionreport) 的 `ExecType (150)` 值为 `REJECTED (8)`。
  * 如果取消订单的请求被拒绝，则为 [OrderCancelReject`<9>`](/zh-CN/docs/products/spot/fix-api#ordercancelreject)。
  * 如果消息被拒绝，则为 [Reject`<3>`](/zh-CN/docs/products/spot/fix-api#reject)。



#### OrderMassCancelRequest `<q>`

由客户端发送，用以取消交易品种上的所有挂单。

该账户的所有订单都将被取消，包括从不同连接中下的订单。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
11| ClOrdID| STRING| Y| 此批量取消请求的`ClOrdId`。  
55| Symbol| STRING| Y| 取消订单的交易对。  
530| MassCancelRequestType| CHAR| Y| 可能的值:  `1` \- CANCEL_SYMBOL_ORDERS  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=95|35=q|34=2|49=dpYPesqv|52=20240613-01:24:36.948|56=SPOT|11=1718241876901971671|55=BTCUSDT|530=1|10=243|

**响应：**

  * 对于每个被取消的订单，[ExecutionReport`<8>`](/zh-CN/docs/products/spot/fix-api#executionreport) 的 `ExecType (150)` 值为 `CANCELED (4)`。
  * 对于请求是否被接受或者拒绝，请参考 [OrderMassCancelReport`<r>`](/zh-CN/docs/products/spot/fix-api#ordermasscancelreport) 的字段 `MassCancelResponse (531)`。
  * 如果消息被拒绝，则为 [Reject`<3>`](/zh-CN/docs/products/spot/fix-api#reject)。



由服务器发送，用以响应 [OrderMassCancelRequest`<q>`](/zh-CN/docs/products/spot/fix-api#ordermasscancelrequest)。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
55| Symbol| STRING| Y| 取消请求中的 `Symbol (55)` 。  
11| ClOrdID| STRING| Y| 取消请求中的 `ClOrdID （11)`。  
530| MassCancelRequestType| CHAR| Y| 取消请求中的 `MassCancelRequestType (530)`。  
531| MassCancelResponse| CHAR| Y| 可能的值：  `0` \- CANCEL_REQUEST_REJECTED  `1` \- CANCEL_SYMBOL_ORDERS  
532| MassCancelRejectReason| INT| N| 可能的值：  `99` \- OTHER  
533| TotalAffectedOrders| INT| N| 取消了多少订单。  
25016| ErrorCode| INT| N| API 错误代码 (参考 [错误代码](/zh-CN/docs/products/spot/errors)).  
58| Text| STRING| N| 可读的错误消息。  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=109|35=r|34=2|49=SPOT|52=20240613-01:24:36.949763|56=dpYPesqv|11=1718241876901971671|55=LTCBNB|530=1|531=1|533=5|10=083|

#### NewOrderList `<E>`

由客户发送，用以提交需要执行的订单列表。

  * `OTO` 或 `OTO` 订单将**2 个订单** 添加到 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。
  * `OTOCO` 在 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器的基础上添加**3个订单** 。



**未成交的订单计数:**

  * OCO: 2
  * OTO: 2
  * OTOCO: 3



订单列表中的订单是相互依赖的。欲了解支持的订单类型和触发说明，请参考[支持的订单列表类型](/zh-CN/docs/products/spot/fix-api#order-list-types)。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
25014| ClListID| STRING| Y| `ClListID`，用于分配给订单列表。  
1385| ContingencyType| INT| N| 可能的值 ：  `1` -ONE_CANCELS_THE_OTHER  `2` \- ONE_TRIGGERS_THE_OTHER  
25046| OPO| BOOLEAN| N| 设置为 `true` 时，将此订单列表设为 [OPO](/zh-CN/docs/products/spot/faqs/opo)。  
73| NoOrders| NUMINGROUP| N| `Orders` 数组中的元素个数。只允许输入2或者3。  
=>11| ClOrdID| STRING| Y| 用于分配给订单的`ClOrdID`  
=>38| OrderQty| QTY| N| 订单数量  
=>40| OrdType| CHAR| Y| 请参阅 [表格](/zh-CN/docs/products/spot/fix-api#ordertype) 以了解支持的订单类型及相关的必填字段 。可能的值 ：  `1` \- MARKET  `2` \- LIMIT  `3` \- STOP  `4` \- STOP_LIMIT  `P` \- PEGGED  
=>18| ExecInst| CHAR| N| 可能的值： `6` \- PARTICIPATE_DONT_INITIATE  
=>44| Price| PRICE| N| 订单价格  
=>54| Side| CHAR| Y| 订单的方向。 可能的值 ： `1` \- BUY  `2` \- SELL  
=>55| Symbol| STRING| Y| 订单的交易对。  
=>59| TimeInForce| CHAR| N| 可能的值 ：  `1` \- GOOD_TILL_CANCEL  `3` \- IMMEDIATE_OR_CANCEL  `4` \- FILL_OR_KILL  
=>111| MaxFloor| QTY| N| 用于冰山订单，这指定了订单在 order book上的可见数量。  
=>152| CashOrderQty| QTY| N| 对于反向市场订单，在报价资产单位中指定的订单数量。  
=>847| TargetStrategy| INT| N| 该值不能小于 `1000000`。  
=>7940| StrategyID| INT| N|   
=>25001| SelfTradePreventionMode| CHAR| N| 可能的值： `1` \- NONE `2` \- EXPIRE_TAKER  `3` \- EXPIRE_MAKER  `4` \- EXPIRE_BOTH  `5` \- DECREMENT  `6` \- TRANSFER  
=>211| PegOffsetValue| FLOAT| N| 使用了 `PegOffsetType` 后，添加到挂钩的偏移值  
=>1094| PegPriceType| CHAR| N| 定义了挂钩价格的类型  可能的值:  `4` \- MARKET_PEG  `5` \- PRIMARY_PEG  
=>835| PegMoveType| CHAR| N| 描述挂钩是固定的还是浮动的。挂钩订单必用且必须为 `1` (FIXED)  
=>836| PegOffsetType| CHAR| N| 定义了挂钩价格偏移类型。  可能的值:  `3` \- PRICE_TIER  
=>1100| TriggerType| CHAR| N| 可能的值:  `4` \- PRICE_MOVEMENT  
=>1101| TriggerAction| CHAR| N| 可能的值:  `1` \- ACTIVATE  
=>1102| TriggerPrice| PRICE| N| 止盈止损订单的激活价格。参见 [表格](/zh-CN/docs/products/spot/fix-api#ordertype)  
=>1107| TriggerPriceType| CHAR| N| 可能的值:  `2` \- LAST_TRADE  
=>1109| TriggerPriceDirection| CHAR| N| 用于区分止损订单和止盈订单。 参见 [表格](/zh-CN/docs/products/spot/fix-api#ordertype).可能的值:  `U` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  `D` \- TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE  
=>25009| TriggerTrailingDeltaBips| INT| N| 用于追踪订单。  
=>25057| QuoteNotionalLimit| QTY| N| 仅适用于买单。该订单可消耗的报价资产名义价值上限。不允许用于 OPO 和 OPOCO 的待处理订单。不能与 `CashOrderQty (152)` 或 `ExecInst (18)` = `6` 同时使用。参见 [quoteNotionalLimit 常见问题](/zh-CN/docs/products/spot/faqs/quoteNotionalLimit)。  
=>25010| NoListTriggeringInstructions| NUMINGROUP| N| `ListTriggeringInstructions` 数组中的元素个数。  
==>25011| ListTriggerType| CHAR| N| 为了触发 pending order， working order 所需进行的操作。  可能的值:  `1` \- ACTIVATED  `2` \- PARTIALLY_FILLED  `3` \- FILLED  
==>25012| ListTriggerTriggerIndex| INT| N| 条件单的触发 Index：0-indexed。  
==>25013| ListTriggerAction| CHAR| N| 在满足 ListTriggerType 条件后对此订单执行的操作。  可能的值:  `1` \- RELEASE  `2` \- CANCEL  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=236|35=E|34=2|49=Eg13pOvN|52=20240607-02:19:07.836|56=SPOT|73=2|11=w1717726747805308656|55=LTCBNB|54=2|38=1|40=2|44=0.25|59=1|11=p1717726747805308656|55=LTCBNB|54=2|38=1|40=1|25010=1|25011=3|25012=0|25013=1|1385=2|25014=1717726747805308656|10=171|

#### 支持的订单列表类型

订单必须按照下表中 _订单名称_ 中指定的顺序排列。

订单列表名称| 应急类型（1385）| 订单名称| 订单方| 允许的币安订单类型| 列出触发指令  
---|---|---|---|---|---  
OCO| `1`| 1\. below order 2\. above order| 1\. below order=`SELL` 2\. above order=`SELL`| 1\. below order=`STOP_LOSS` 或 `STOP_LOSS_LIMIT` 2\. above order=`LIMIT_MAKER`| 1\. below order: 25010=1|25011=2|25012=1|25013=2|2\. above order: 25010=1|25011=1|25012=0|25013=2|  
OCO| `1`| 1\. below order 2\. above order| 1\. below order=`BUY` 2\. above order=`BUY`| 1\. below order=`LIMIT_MAKER` 2\. above order=`STOP_LOSS` 或 `STOP_LOSS_LIMIT`| 1\. below order: 25010=1|25011=1|25012=1|25013=2|2\. above order: 25010=1|25011=2|25012=0|25013=2|  
OCO| `1`| 1\. below order 2\. above order| 1\. below order=`SELL` 2\. above order=`SELL`| 1\. below order=`STOP_LOSS` 或 `STOP_LOSS_LIMIT` 2\. above order= `TAKE_PROFIT`| 1\. below order: 25010=1|25011=1|25012=1|25013=2|2\. above order: 25010=1|25011=1|25012=0|25013=2|  
OCO| `1`| 1\. below order 2\. above order| 1\. below order=`BUY` 2\. above order=`BUY`| 1\. below order=`TAKE_PROFIT` 2\. above order = `STOP_LOSS` 或 `STOP_LOSS_LIMIT`| 1\. below order: 25010=1|25011=1|25012=1|25013=2|2\. above order: 25010=1|25011=1|25012=0|25013=2|  
OTO| `2`| 1\. working order 2\. pending order| 1\. working order=`SELL` 或 `BUY` 2\. pending order=`SELL` 或 `BUY`| 1\. working order=`LIMIT` 或 `LIMIT_MAKER` 2\. pending order=ANY| 1\. working order:NONE 2\. pending order: 25010=1|25011=3|25012=0|25013=1|  
OTOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`SELL` 或 `BUY` 2\. pending below order=`SELL` 3\. pending above order=`SELL`| 1\. working order=`LIMIT` 或 `LIMIT_MAKER` 2\. pending below order=`STOP_LOSS` 或 `STOP_LOSS_LIMIT` 3\. pending above order=`LIMIT_MAKER`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=2|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
OTOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`SELL` 或 `BUY` 2\. pending below order=`BUY` 3\. pending above order=`BUY`| 1\. working order=`LIMIT` 或 `LIMIT_MAKER` 2\. pending below order=`LIMIT_MAKER` 3\. pending above order=`STOP_LOSS` 或 `STOP_LOSS_LIMIT`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=2|25012=1|25013=2|  
OTOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`SELL` 或 `BUY` 2\. pending below order=`SELL` 3\. pending above order=`SELL`| 1\. working order=`LIMIT` 或 `LIMIT_MAKER` 2\. pending below order=`STOP_LOSS` 或 `STOP_LOSS_LIMIT` 3\. pending above order=`TAKE_PROFIT`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
OTOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`SELL` 或 `BUY` 2\. pending below order=`BUY` 3\. pending above order=`BUY`| 1\. working order=`LIMIT` 或 `LIMIT_MAKER` 2\. pending below order=`TAKE_PROFIT` 3\. pending above order=`STOP_LOSS` 或 `STOP_LOSS_LIMIT`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
OPO| `2`| 1\. working order 2\. pending order| 1\. working order=`BUY` 2\. pending order=`SELL`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending order=ANY| 1\. working order:NONE 2\. pending order: 25010=1|25011=3|25012=0|25013=1|  
OPOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`BUY` 2\. pending below order=`SELL` 3\. pending above order=`SELL`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending below order=`STOP_LOSS` or `STOP_LOSS_LIMIT` 3\. pending above order=`LIMIT_MAKER`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=2|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
OPOCO| `2`| 1\. working order 2\. pending below order 3\. pending above order| 1\. working order=`BUY` 2\. pending below order=`SELL` 3\. pending above order=`SELL`| 1\. working order=`LIMIT` or `LIMIT_MAKER` 2\. pending below order=`STOP_LOSS` or `STOP_LOSS_LIMIT` 3\. pending above order=`TAKE_PROFIT` or `TAKE_PROFIT_LIMIT`| 1\. working order:NONE 2\. pending below order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=2|25013=2|3\. pending above order:25010=2|25011=3|25012=0|25013=2|25011=1|25012=1|25013=2|  
  
#### ListStatus `<N>`

每当订单列表状态发生变化时，由服务器发送的消息。

默认情况下，ListStatus`<N>` 会含有该账户的所有订单列表，包括在不同连接中提交的订单列表。请参阅 [响应模式](/zh-CN/docs/products/spot/fix-api#responsemode) 来了解其他行为选项。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
66| ListID| STRING| N| 由交易所分配的订单列表 `ListID`。  
25014| ClListID| STRING| N| 分配给请求的订单列表 `ClListID` 。  
25015| OrigClListID| STRING| N|   
1385| ContingencyType| INT| N| 可能的值:  `1` \- ONE_CANCELS_THE_OTHER  `2` \- ONE_TRIGGERS_THE_OTHER  
429| ListStatusType| INT| Y| 可能的值:  `2` \- RESPONSE `4` \- EXEC_STARTED  `5` \- ALL_DONE  `100` \- UPDATED  
431| ListOrderStatus| INT| Y| 可能的值:  `3` \- EXECUTING  `6` \- ALL_DONE  `7` \- REJECT  
1386| ListRejectReason| INT| N| 可能的值:  `99` \- OTHER  
103| OrdRejReason| INT| N| 可能的值:  `99` \- OTHER  
60| TransactTime| UTCTIMESTAMP| N| 发生此事件时的时间戳。  
25016| ErrorCode| INT| N| API 错误代码 (参考 [错误代码](/zh-CN/docs/products/spot/errors) )。  
58| Text| STRING| N| 可读的错误消息。  
73| NoOrders| NUMINGROUP| N| `Orders` 数组中的元素个数。  
=>55| Symbol| STRING| Y| 订单的交易对。  
=>37| OrderID| INT| Y| 由交易所分配的订单 `OrderID`。  
=>11| ClOrdID| STRING| Y| 分配给请求的订单 `ClOrdID`。  
=>25010| NoListTriggeringInstructions| NUMINGROUP| N| `ListTriggeringInstructions` 数组中的元素个数。  
==>25011| ListTriggerType| CHAR| N| 可能的值:  `1` \- ACTIVATED  `2` \- PARTIALLY_FILLED  `3` \- FILLED  
==>25012| ListTriggerTriggerIndex| INT| N|   
==>25013| ListTriggerAction| CHAR| N| 可能的值  `1` \- RELEASE  `2` \- CANCEL  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=282|35=N|34=2|49=SPOT|52=20240607-02:19:07.837191|56=Eg13pOvN|60=20240607-02:19:07.836000|66=25|73=2|55=BTCUSDT|37=52|11=w1717726747805308656|55=BTCUSDT|37=53|11=p1717726747805308656|25010=1|25011=3|25012=0|25013=1|429=4|431=3|1385=2|25014=1717726747805308656|25015=1717726747805308656|10=223|

#### OrderAmendKeepPriorityRequest `<XAK>`

由客户发送以减少其订单的原始数量。

这个请求将添加0个订单到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

**未成交的订单计数:** 0

**注意：**

  * `ClOrdID(11)` 不需要与原订单的 `ClOrdID` 不同。当请求的 `ClOrdID` 与待修改订单的 `ClOrdID` 相同时，`ClOrdID` 将保持不变。
  * 当同时提供 `OrderID (37)` 和 `OrigClOrdID (41)` 两个参数时，系统首先将会使用 `OrderID` 来搜索订单。然后， 查找结果中的 `OrigClOrdID (41)` 的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
11| ClOrdID| STRING| Y| 分配给请求的订单 `ClOrdID`。  
41| OrigClOrdID| STRING| N| 待修改订单的 `ClOrdID (11)`。 需提供 `OrigClOrdID (41)` 或 `OrderId (37)`。  
37| OrderID| INT| N| 待修改订单的 `OrderID (37)`。 需提供 `OrigClOrdID (41)` 或 `OrderId (37)`。  
55| Symbol| STRING| Y| 待修改订单的交易对。  
38| OrderQty| QTY| N| 交易的新数量。 必须比订单的原始 OrderQty 小。  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=103|35=XAK|34=2|49=EXAMPLE|52=20250319-12:35:21.087|56=SPOT|11=O2EIAS01742387721086|37=0|38=0.9|55=BTCUSDT|10=254|

**响应：**

  * [Reject `<3>`](/zh-CN/docs/products/spot/fix-api#reject) 请求会由于缺少必填字段，无效字段，引用无效的符号，或超过消息限制而成为无效请求。
  * [OrderAmendReject `<XAR>`](/zh-CN/docs/products/spot/fix-api#orderamendreject) 如果请求失败，则由于订单速率限制不足，指向不存在的订单，数量无效等。
  * [ExecutionReport `<8>`](/zh-CN/docs/products/spot/fix-api#executionreport) 请求成功修改了单个订单。
  * [ExecutionReport `<8>`](/zh-CN/docs/products/spot/fix-api#executionreport) \+ [ListStatus `<N>`](/zh-CN/docs/products/spot/fix-api#liststatus) 请求成功修改了隶属于订单列表中的单个订单。



### OrderAmendReject `<XAR>`

当 OrderAmendKeepPriorityRequest `<XAK>` 请求失败时，由服务器发送。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
11| ClOrdID| STRING| Y| 待修改订单的 `ClOrdId`。  
41| OrigClOrdID| STRING| N| 待修改订单的 `OrigClOrdId (41)`。  
37| OrderID| INT| N| 待修改订单的 `OrderId (37)`。  
55| Symbol| STRING| Y| 待修改订单的 `Symbol (55)`。  
38| OrderQty| QTY| Y|   
25016| ErrorCode| INT| Y| API 错误代码 (参考 [错误代码](/zh-CN/docs/products/spot/errors) )。  
58| Text| STRING| Y| 人类可读的错误消息。  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=0000176|35=XAR|49=SPOT|56=OE|34=2|52=20250319-14:27:32.751074|11=1WRGW5J1742394452749|37=0|55=BTCUSDT|38=1.000000|25016=-2038|58=The requested action would change no state; rejecting.|10=235|

### Limit Messages

#### LimitQuery `<XLQ>`

由客户端发送，用于查询当前限制。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
6136| ReqID| STRING| Y| 此请求的 ID  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=82|35=XLQ|34=2|49=7buKHZxZ|52=20240614-05:35:35.357|56=SPOT|6136=1718343335357229749|10=170|

#### LimitResponse `<XLR>`

由服务器发送，以响应 [LimitQuery`<XLQ>`](/zh-CN/docs/products/spot/fix-api#limitquery) 请求。

Tag| 名称| 类型| 是否必须| 描述  
---|---|---|---|---  
6136| ReqID| STRING| Y| `ReqID`。  
25003| NoLimitIndicators| NUMINGROUP| Y| `LimitIndicator` 数组中的元素个数。  
=>25004| LimitType| CHAR| Y| 可能的值  `1` \- ORDER_LIMIT  `2` \- MESSAGE_LIMIT  
=>25005| LimitCount| INT| Y| 此限制的当前使用情况。  
=>25006| LimitMax| INT| Y| 此限制允许的最大值。  
=>25007| LimitResetInterval| INT| N| 限制重置的频率。  
=>25008| LimitResetIntervalResolution| CHAR| N| `LimitResetInterval` 的时间单位。可能的值：  `s` \- SECOND  `m` \- MINUTE  `h` \- HOUR  `d` \- DAY  
  
**示例消息：**
    
    
    Code
    
    8=FIX.4.4|9=225|35=XLR|34=2|49=SPOT|52=20240614-05:42:42.724057|56=uGnG0ef8|6136=1718343762723730315|25003=3|25004=2|25005=1|25006=1000|25007=10|25008=s|25004=1|25005=0|25006=200|25007=10|25008=s|25004=1|25005=0|25006=200000|25007=1|25008=d|10=241|

### 市场数据流

以下消息只能用于 FIX 市场数据流。

#### InstrumentListRequest `<x>`

由客户端发送，用于查询有关交易对的信息。

Tag| Name| Type| Required| Description  
---|---|---|---|---  
320| InstrumentReqID| STRING| Y| 此请求的 ID  
559| InstrumentListRequestType| INT| Y| 可能的值：  `0` \- SINGLE_INSTRUMENT  `4` \- ALL_INSTRUMENTS  
55| Symbol| STRING| N| 当 `InstrumentListRequestType` 设置为 `SINGLE_INSTRUMENT (0)` 时是必需的  
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=92|35=x|49=BMDWATCH|56=SPOT|34=2|52=20250114-08:46:56.096691|320=BTCUSDT_INFO|559=0|55=BTCUSDT|10=164|

#### InstrumentList `<y>`

由服务器在响应 [InstrumentListRequest`<x>`](/zh-CN/docs/products/spot/fix-api#instrumentlistrequest) 时发送。

有关交易对（例如，过滤器）的其他信息可通过 [exchangeInfo](/zh-CN/docs/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info) 请求来获得。请求来获得。

Tag| Name| Type| Required| Description  
---|---|---|---|---  
320| InstrumentReqID| STRING| Y| `InstrumentReqID` 从请求中得到  
146| NoRelatedSym| NUMINGROUP| Y| 交易数量  
=>55| Symbol| STRING| Y| 交易对  
=>15| Currency| STRING| Y| 此交易品种的报价资产  
146| NoRelatedSym| NUMINGROUP| Y| 交易品种数量  
=>55| Symbol| STRING| Y|   
=>15| Currency| STRING| Y| 此交易品种的 Quote asset  
=>562| MinTradeVol| QTY| N| 对应于 [LOT_SIZE](/zh-CN/docs/products/spot/filters#lot_size) 过滤器  
=>1140| MaxTradeVol| QTY| N| 对应于 [LOT_SIZE](/zh-CN/docs/products/spot/filters#lot_size) 过滤器  
=>25039| MinQtyIncrement| QTY| N| 对应于 [LOT_SIZE](/zh-CN/docs/products/spot/filters#lot_size) 过滤器  
=>25040| MarketMinTradeVol| QTY| N| 对应于 [MARKET_LOT_SIZE](/zh-CN/docs/products/spot/filters#market_lot_size) 过滤器  
=>25041| MarketMaxTradeVol| QTY| N| 对应于 [MARKET_LOT_SIZE](/zh-CN/docs/products/spot/filters#market_lot_size) 过滤器  
=>25042| MarketMinQtyIncrement| QTY| N| 对应于 [MARKET_LOT_SIZE](/zh-CN/docs/products/spot/filters#market_lot_size) 过滤器  
=>969| MinPriceIncrement| PRICE| N| 对应于 [PRICE](/zh-CN/docs/products/spot/filters#price) 过滤器  
=>2551| StartPriceRange| PRICE| N| 对应于 [PRICE](/zh-CN/docs/products/spot/filters#price) 过滤器  
=>2552| EndPriceRange| PRICE| N| 对应于 [PRICE](/zh-CN/docs/products/spot/filters#price) 过滤器  
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=218|35=y|49=SPOT|56=BMDWATCH|34=2|52=20250114-08:46:56.100147|320=BTCUSDT_INFO|146=1|55=BTCUSDT|15=USDT|562=0.00001000|1140=9000.00000000|25039=0.00001000|25040=0.00000001|25041=76.79001236|25042=0.00000001|969=0.01000000|10=093||

#### MarketDataRequest `<V>`

由客户发送，用于订阅或取消订阅市场数据流。

**交易数据流**

交易数据流推送原始交易信息;每笔交易都有唯一的买家和卖家。

**订阅所需的字段：**

  * `SubscriptionRequestType` 的值为 `SUBSCRIBE(1)`
  * `MDEntryType` 的值为 `TRADE(2)`



**更新速度：** 实时

**book ticker数据流**

将指定交易对最佳买价，卖价以及数量的更新进行实时推送。

**订阅所需的字段**

  * `SubscriptionRequestType` 值为 `SUBSCRIBE(1)`
  * `MDEntryType` 值为 `BID (0)`
  * `MDEntryType` 值为 `OFFER(1)`
  * `MarketDepth` 值为 `1`   
**Individual Symbol Book Ticker Stream**



将指定交易品种的任何更新实时推送到最佳买价或卖价或数量。

**订阅所需的字段**

  * 值为 `SUBSCRIBE(1)` 的 `SubscriptionRequestType`
  * 值为 `BID (0)` 的 `MDEntryType`
  * 值为 `OFFER(1)` 的 `MDEntryType`
  * 值为 `1` 的 `MarketDepth`



**更新速度：** 实时

在 [单个交易对订单簿数据流](/zh-CN/docs/products/spot/fix-api#symbolbooktickerstream) 中，在[MarketDataIncrementalRefresh`<X>`](/zh-CN/docs/products/spot/fix-api#marketdataincrementalrefresh) 消息里 `MDUpdateAction` 取代了之前的 Best Quote，

**增量深度数据流**

用于本地订单簿管理的价格和数量深度更新。

**订阅所需的字段**

  * `SubscriptionRequestType` 值为 `SUBSCRIBE(1)`
  * `MDEntryType` 值为 `BID (0)`
  * `MDEntryType` 值为 `OFFER (1)`
  * `MarketDepth` 值介于 `2` 和 `5000` 之间，用于控制初始快照的大小，对后续的 [MarketDataIncrementalRefresh `<X>` ](/zh-CN/docs/products/spot/fix-api#marketdataincrementalrefresh) 消息没有影响



**更新速度：** 100 毫秒

由于 [MarketDataSnapshot`<W>`](/zh-CN/docs/products/spot/fix-api#marketdatasnapshot) 对价格的深度有限制，所在初始快照之外没有数量变化的价格不会在增量深度信息数据流中。因此，即使更新所有推送的数据流信息，依然会导致本地订单簿与真实订单簿有些微差异。对于大多数情况，5000 的深度限制就足以理解市场和进行有效的交易。

Tag| Name| Type| Required| Description  
---|---|---|---|---  
262| MDReqID| STRING| Y| 此请求的 ID  
263| SubscriptionRequestType| CHAR| Y| 订阅请求类型。 可能的值：  `1` \- SUBSCRIBE  `2` \- UNSUBSCRIBE  
264| MarketDepth| INT| N| 订阅深度。可能的值：  `1` \- Book Ticker 订阅  `2`-`5000` \- 增量深度流  
266| AggregatedBook| NUMINGROUP| N| 可能的值：  `Y` \- 每个价格每侧 1 个帐簿条目  
146| NoRelatedSym| NUMINGROUP| N| 交易对数量  
=>55| Symbol| STRING| Y|   
267| NoMDEntryTypes| NUMINGROUP| N| 条目类型数量  
=>269| MDEntryType| CHAR| Y| 可使用的值：  `0` \- BID  `1` \- OFFER  `2` \- TRADE  
  
**示例消息:**
    
    
    Code
    
    # Subscriptions
    # BOOK TICKER Stream
    8=FIX.4.4|9=132|35=V|49=TRADER1|56=SPOT|34=4|52=20241122-06:17:14.183428|262=BOOK_TICKER_STREAM|263=1|264=1|266=Y|146=1|55=BTCUSDT|267=2|269=0|269=1|10=010|
    # DEPTH Stream
    8=FIX.4.4|9=127|35=V|49=TRADER1|56=SPOT|34=7|52=20241122-06:17:14.443822|262=DEPTH_STREAM|263=1|264=10|266=Y|146=1|55=BTCUSDT|267=2|269=0|269=1|10=111|
    # TRADE Stream
    8=FIX.4.4|9=120|35=V|49=TRADER1|56=SPOT|34=3|52=20241122-06:34:14.775606|262=TRADE_STREAM|263=1|264=1|266=Y|146=1|55=BTCUSDT|267=1|269=2|10=040|
    # Unsubscription from TRADE Stream
    8=FIX.4.4|9=79|35=V|49=TRADER1|56=SPOT|34=7|52=20241122-06:41:56.966969|262=TRADE_STREAM|263=2|264=1|10=113|

### MarketDataRequestReject `<Y>`

服务器对不正确的 MarketDataRequest 的响应消息 `<V>`.

Tag| Name| Type| Required| Description  
---|---|---|---|---  
262| MDReqID| STRING| Y| 不正确的ID [MarketDataRequest`<V>`](/zh-CN/docs/products/spot/fix-api#marketdatarequest)  
281| MDReqRejReason| CHAR| N| 可能的错误原因:  `1` \- DUPLICATE_MDREQID  `2` \- TOO_MANY_SUBSCRIPTIONS  
25016| ErrorCode| INT| N| API 错误代码 [参见 错误代码](/zh-CN/docs/products/spot/errors)。  
58| Text| STRING| N| 错误信息。  
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=0000218|35=Y|49=SPOT|56=EXAMPLE|34=5|52=20241019-05:39:36.688964|262=BOOK_TICKER_2|281=2|25016=-1191|58=Similar subscription is already active on this connection. Symbol='BNBBUSD', active subscription id: 'BOOK_TICKER_1'.|10=137|

### MarketDataSnapshot `<W>`

服务器对 [MarketDataRequest`<V>`](/zh-CN/docs/products/spot/fix-api#marketdatarequest)，激活 [单个 Symbol Book Ticker Stream](/zh-CN/docs/products/spot/fix-api#symbolbooktickerstream) 或 [增量深度流](/zh-CN/docs/products/spot/fix-api#diffdepthstream) 订阅的响应消息。

Tag| Name| Type| Required| Description  
---|---|---|---|---  
262| MDReqID| STRING| Y| 激活此订阅的 [MarketDataRequest`<V>`](/zh-CN/docs/products/spot/fix-api#marketdatarequest) 的 ID  
55| Symbol| STRING| Y|   
25044| LastBookUpdateID| INT| N|   
268| NoMDEntries| NUMINGROUP| Y| 条目数  
=>269| MDEntryType| CHAR| Y| 可能的值：  `0` \- BID  `1` \- OFFER  `2` \- TRADE  
=>270| MDEntryPx| PRICE| Y| 价格  
=>271| MDEntrySize| QTY| Y| 数量  
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=0000107|35=W|49=SPOT|56=EXAMPLE|34=34|52=20241019-05:41:52.867164|262=BOOK_TICKER_1_2|55=BNBBUSD|25044=0|268=0|10=151|

### MarketDataIncrementalRefresh `<X>`

当一个订阅的数据流发生变化时，服务器发出的响应消息。

Tag| Name| Type| Required| Description  
---|---|---|---|---  
262| MDReqID| STRING| Y| 激活此订阅的 [MarketDataRequest `<V>`](/zh-CN/docs/products/spot/fix-api#marketdatarequest) 的 ID  
268| NoMDEntries| NUMINGROUP| Y| 条目数  
=>279| MDUpdateAction| CHAR| Y| 可能的值：  `0` \- NEW  `1` \- CHANGE  `2` \- DELETE  
=>270| MDEntryPx| PRICE| Y| 价格  
=>271| MDEntrySize| QTY| N| 数量  
=>269| MDEntryType| CHAR| Y| 可能的值：  `0` \- BID  `1` \- OFFER  `2` \- TRADE  
=>55| Symbol| STRING| N| 如果未指定`交易对`，则默认使用同一市场数据流消息中前一个消息的交易对  
=>60| TransactTime| UTCTIMESTAMP| N|   
=>1003| TradeID| INT| N|   
=>2446| AggressorSide| CHAR| N| 可能的值：  `1` \- BUY  `2` \- SELL  
=>25043| FirstBookUpdateID| INT| N| 只会在 [增量深度数据流](/zh-CN/docs/products/spot/fix-api#diffdepthstream) 中出现.  如果 `LastBookUpdateID` 没有指定，市场数据消息的 `FirstBookUpdateID` 将会默认设置为与之前消息一样的 `FirstBookUpdateID`  
=>25044| LastBookUpdateID| INT| N| 只会在 [增量深度数据流](/zh-CN/docs/products/spot/fix-api#diffdepthstream) 和 [单个交易对订单簿数据流](/zh-CN/docs/products/spot/fix-api#symbolbooktickerstream) 中出现.  如果 `LastBookUpdateID` 没有指定，市场数据消息的 `LastBookUpdateID` 将会默认设置为与之前消息一样的 `LastBookUpdateID`  
  
**示例消息:**
    
    
    Code
    
    8=FIX.4.4|9=0000303|35=X|49=SPOT|56=EXAMPLE|34=16|52=20241019-05:40:11.466313|262=TRADE_3|268=3|279=0|269=2|270=10.00000|271=0.01000|55=BNBBUSD|1003=0|60=20241019-05:40:11.464000|279=0|269=2|270=10.00000|271=0.01000|1003=1|60=20241019-05:40:11.464000|279=0|269=2|270=10.00000|271=0.01000|1003=2|60=20241019-05:40:11.464000|10=042|

## FIX SBE

FIX SBE（简单二进制编码）可以替代 FIX，请使用 [spot_fix_prod_latest.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_fix_prod_latest.xml) 模式文件。

### SBE

请阅读 [简单二进制编码 （SBE） 常见问题](/zh-CN/docs/products/spot/faqs/sbe_faq) 了解有关将 SBE 与币安 API 配合使用的重要信息。

  * 在使用 FIX SBE 之前，请务必阅读并理解 [SBE 规范](https://www.fixtrading.org/standards/sbe-online/)。

  * 在对 SBE payload 进行编码和解码时，建议使用 [`SbeTool`](https://github.com/aeron-io/simple-binary-encoding) 所生成的代码，以确保符合FIX SBE 规范。




### 端点

除了在 9000 端口支持的 FIX 编码外，还支持两种请求/响应编码方案，分别在额外的 TCP 端口上。以下是各个 API 的端点说明。

#### 订单录入

  * `tcp+tls://fix-oe.binance.com:9001`：发送 FIX 请求；接收 FIX SBE 响应
    * FIX `SbeSchemaId` 标签（=25050）必须设置为 FIX SBE 模式 ID（例如 1）
    * FIX `SbeSchemaVersion` 标签（=25051）必须设置为 FIX SBE 模式版本（例如 0）
  * `tcp+tls://fix-oe.binance.com:9002`：发送 FIX SBE 请求；接收 FIX SBE 响应



#### Drop Copy（订单副本）

  * `tcp+tls://fix-dc.binance.com:9001`：发送 FIX 请求；接收 FIX SBE 响应
    * FIX `SbeSchemaId` 标签（=25050）必须设置为 FIX SBE 模式 ID（例如 1）
    * FIX `SbeSchemaVersion` 标签（=25051）必须设置为 FIX SBE 模式版本（例如 0）
  * `tcp+tls://fix-dc.binance.com:9002`：发送 FIX SBE 请求；接收 FIX SBE 响应



#### 市场数据

  * `tcp+tls://fix-md.binance.com:9001`：发送 FIX 请求；接收 FIX SBE 响应
    * FIX `SbeSchemaId` 标签（=25050）必须设置为 FIX SBE 模式 ID（例如 1）
    * FIX `SbeSchemaVersion` 标签（=25051）必须设置为 FIX SBE 模式版本（例如 0）
  * `tcp+tls://fix-md.binance.com:9002`：发送 FIX SBE 请求；接收 FIX SBE 响应



### FIX SBE 编码设计

FIX SBE 请求/响应 消息总会包含一个 SOFH (Simple Open Framing Header) 和消息头. 一个 N 字节的FIX SBE 消息包含下面的格式:

`<SOFH (6 字节> <消息头 (20 字节)> <消息 (N 字节)>`

SOFH：有关模式文件中的组合类型 "sofh"。这个字段作为一个帧头用来让FIX SBE 服务器端/客户端 来确定 SBE 消息的长度和保证在反序列化之前已经接收到完整的消息。

注意：

  * SOFH 中的两个字段必须是小端序编码（little-endian）
  * FIX 服务器仅支持编码类型字段 `0xEB50` , 例如只有小端序（little-endian） 在所有字段被支持



消息头： 这对应于模式文件中的组合类型 "messageHeader".

### Logon

登录签名（RawData）的计算方法如[签名计算](/zh-CN/docs/products/spot/fix-api#signaturecomputation)部分所述。

#### FIX SBE `Logon` 请求消息示例

请参阅下方根据上述说明获取的 FIX SBE `Logon` 十六进制消息示例。

Bytes| Description  
---|---  
0xd1, 0x00, 0x00, 0x00| sofh.messageLength  
0x50, 0xeb| sofh.encodingType  
0x0e, 0x00| messageHeader.blockLength  
0x28, 0x4e| messageHeader.templateId  
0x01, 0x00| messageHeader.schemaId  
0x00, 0x00| messageHeader.version  
0x01, 0x00, 0x00, 0x00| messageHeader.seqNum  
0x58, 0x7a, 0x5f, 0x99, 0xdb, 0x1b, 0x06, 0x00| messageHeader.sendingTime  
0x00| Logon.EncryptMethod  
0x1e, 0x00, 0x00, 0x00| Logon.HeartBtInt  
0x01| Logon.ResetSeqNumFlag  
0x02| Logon.MessageHandling  
0xff| Logon.ResponseMode  
0xff| Logon.ExecutionReportType  
0xff| Logon.DropCopyFlag  
0xff, 0xff, 0xff, 0xff| Logon.RecvWindow  
0x07| Logon.SenderCompId.length  
0x45, 0x58, 0x41, 0x4d, 0x50, 0x4c, 0x45| Logon.SenderCompId.varData  
0x04| Logon.TargetCompId.length  
0x53, 0x50, 0x4f, 0x54| Logon.TargetCompId.varData  
0x58, 0x00| Logon.RawData.length  
0x34, 0x4d, 0x48, 0x58, 0x65, 0x6c, 0x56, 0x56| Logon.RawData.varData  
0x63, 0x70, 0x6b, 0x64, 0x77, 0x75, 0x4c, 0x62| Logon.RawData.varData  
0x6c, 0x36, 0x6e, 0x37, 0x33, 0x48, 0x51, 0x55| Logon.RawData.varData  
0x58, 0x55, 0x66, 0x31, 0x64, 0x73, 0x65, 0x32| Logon.RawData.varData  
0x50, 0x43, 0x67, 0x54, 0x31, 0x44, 0x59, 0x71| Logon.RawData.varData  
0x57, 0x39, 0x77, 0x38, 0x41, 0x56, 0x5a, 0x31| Logon.RawData.varData  
0x52, 0x41, 0x43, 0x46, 0x47, 0x4d, 0x2b, 0x35| Logon.RawData.varData  
0x55, 0x64, 0x6c, 0x47, 0x50, 0x72, 0x51, 0x48| Logon.RawData.varData  
0x72, 0x67, 0x74, 0x53, 0x33, 0x43, 0x76, 0x73| Logon.RawData.varData  
0x52, 0x55, 0x52, 0x43, 0x31, 0x6f, 0x6a, 0x37| Logon.RawData.varData  
0x33, 0x6a, 0x38, 0x67, 0x43, 0x41, 0x3d, 0x3d| Logon.RawData.varData  
0x40, 0x00| Logon.Username.length  
0x73, 0x42, 0x52, 0x58, 0x72, 0x4a, 0x78, 0x32| Logon.Username.varData  
0x44, 0x73, 0x4f, 0x72, 0x61, 0x4d, 0x58, 0x4f| Logon.Username.varData  
0x61, 0x55, 0x6f, 0x76, 0x45, 0x68, 0x67, 0x56| Logon.Username.varData  
0x52, 0x63, 0x6a, 0x4f, 0x76, 0x43, 0x74, 0x51| Logon.Username.varData  
0x77, 0x6e, 0x57, 0x6a, 0x38, 0x56, 0x78, 0x6b| Logon.Username.varData  
0x4f, 0x68, 0x31, 0x78, 0x71, 0x62, 0x6f, 0x53| Logon.Username.varData  
0x30, 0x32, 0x53, 0x50, 0x47, 0x66, 0x4b, 0x69| Logon.Username.varData  
0x32, 0x68, 0x38, 0x73, 0x70, 0x5a, 0x4a, 0x62| Logon.Username.varData  
  
### FIX 与 FIX SBE 模式对比

通用说明：

  * `sofh.messageLength` 字段 _必须_ 包含 SOFH 的大小（6 字节）
  * FIX SBE 没有 `Checksum` 字段
  * 在端口 9002 上发送 FIX SBE 请求时
    * payload 中必须设置所有字段
    * 未设置的可选字段必须设置为相应的 `nullValue`
      * `SbeTool` 生成的编码器可以正确处理这种情况
      * 如果 payload 是手动编码生成的，请参阅 [SBE 规范](https://www.fixtrading.org/standards/sbe-online/) 中有关 `nullValue` 的定义



小数位编码：

  * 在请求消息中，`PriceExponent` 和 `QtyExponent` 的值不得超过其所处理的交易对精度。交易对的精度可以从 `InstrumentList` 响应中获取。



#### Logon

  * `SenderCompID`、`TargetCompID` 和 `RecvWindow` 字段包含在 `Logon` FIX SBE 消息中，而不是消息头
    * `Logon` 消息中设置的 `RecvWindow` 字段适用于 FIX SBE 会话内的所有交易请求消息。
    * 设置后，`RecvWindow` 字段的单位为微秒。
  * 当 `ResponseMode` 字段设置为 `OnlyAcks` 时，`ExecutionReportType` 字段可以设置为 `Mini`，以接收 `ExecutionReportAck` 消息，而非 `ExecutionReport`
    * 注意：只有订单录入和 Drop Copy（订单副本）接口的 9001 端口和 9002 端口会支持 `ExecutionReportType` 字段



#### MarketDataIncrementalRefresh

  * FIX 模式中的单条消息被拆分为以下 FIX SBE 消息：`MarketDataIncrementalTrade`、`MarketDataIncrementalBookTicker` 和 `MarketDataIncrementalDepth`
  * 市场数据快照和刷新消息中省略了 `MDReqID` 字段，因为这些消息可以通过 `Symbol` 字段和消息的模板 ID 与订阅请求关联起来。
    * `MDReqID` 在 `MarketDataRequest` 消息中是必需的，以便它可以在 `MarketDataRequestReject` 中使用。
    * `MDReqID` 的值在所有订阅中必须是唯一的。



#### MarketDataIncrementalTrade

  * FIX 模式中可用的 `MDUpdateAction` 字段在 FIX SBE 中被省略，因为其值始终为 `NEW`。



#### MarketDataIncrementalBookTicker

  * FIX SBE 最优挂单信息订阅使用 **自动剔除（auto-culling）** ：当系统负载较高时，可能会丢弃过时的事件，而不是将所有事件排队并延迟发送。
    * 例如，如果在时间 T2 生成了一个最优买/卖单报价事件，而此时仍有一个未发送的事件排队在时间 T1（且 T1 < T2），则会丢弃时间 T1 的事件，系统只会发送时间 T2 的事件。此操作是基于每个交易对分别进行的。
  * FIX 模式中可用的 `MDUpdateAction` 字段在 FIX SBE 中被省略，因为其值可能源自 `MDEntrySize`。
    * 当 `MDEntrySize` 未设置（`NullVal`）时，`MDUpdateAction` 为 `DELETE`。
    * 当 `MDEntrySize` 已设置时：
      * 如果价格水平已存在于本地订单簿中，则 `MDUpdateAction` 为 `CHANGE`
      * 否则，`MDUpdateAction` 为 `NEW`。



#### MarketDataIncrementalDepth

  * FIX SBE 深度更新速度：20 毫秒
  * FIX 模式中可用的 `MDUpdateAction` 字段在 FIX SBE 中被省略，因为其值可能源自 `MDEntrySize`。
    * 当 `MDEntrySize` 未设置（`NullVal`）时，`MDUpdateAction` 为 `DELETE`。
    * 当 `MDEntrySize` 已设置时：
      * 如果价格水平已存在于本地订单簿中，则 `MDUpdateAction` 为 `CHANGE`
      * 否则，`MDUpdateAction` 为 `NEW`。



### 连接限制

FIX 和 FIX SBE 分享连接限制。

### 错误代码

可能返回以下 FIX SBE 特定错误代码：

代码| 消息| 描述  
---|---|---  
-1152| 无效的 SBE 消息头。| 解码 FIX SBE 请求中的 `messageHeader` 时出错  
-1153| 指定的 SBE 模式 ID 或版本无效。| 解析/解码 FIX SBE 模式 ID/版本时出错  
-1177| 无效的编码类型。| 解码 sofh 复合类型中的 `encodingType` 字段时出错  
-1221| SBE 消息中字段无效或缺失。| 解码 FIX SBE 请求时字段无效或缺失  
  
注意：对于语义等效的 FIX 和 FIX SBE 请求，返回的错误代码可能不完全相同。

### 常见问题

有关生成 SBE 解码器和处理模式更新的更多信息，请参见 [SBE FAQ](/zh-CN/docs/products/spot/faqs/sbe_faq)。

此页面是否有帮助？

Last modified on November 12, 2026

[WebSocket 流信息](/zh-CN/docs/products/spot/web-socket-streams)[SBE 市场数据流](/zh-CN/docs/products/spot/sbe-market-data-streams)