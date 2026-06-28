---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/logon-fix
api_type: REST
updated_at: 2026-05-27 19:42:23.656897
---

# Logon

The Logon message authenticates a user establishing a connection to the Kraken exchange. The Logon message must be the first message sent by the Firm that needs to initiate a FIX session with exchange.

If the logon is successful, the exchange will answer with a Logon message. The authentication information (username and password) won't be sent back in case of Trading session logon (see below for more details).

If the logon is not successful, Kraken will send a Logout message with a reason will be sent back. It can also happen that the connection get closed without logout message from Kraken.

  * FIX Specification
  * Example Market Data
  * Example Trading

### MESSAGE BODY

**header** `` *required*

MsgType `A`

**98 - EncryptMethod** integer required

Always set to `0` (None) 

**108 - HeartBtInt** integer required

Value in seconds. Recommended value= `60`. 

**109 - ClientID** integer

Used to identify if this connection is associated with any other connection. 

**141 - ResetSeqNumFlag** boolean

**Possible values:**[`true`, ` false`] 

**Default value:**`false`

Indicates both sides should reset sequence numbers. 

**553 - UserName** string conditional

**Condition:** Trading Logon 

The value is the API Key that needs to be created with FIX API purpose. 

**554 - Password** string conditional

**Condition:** Trading Logon 

Password generated with multiple information. See below. 

**8674 - CancelOrdersOnDisconnect** integer

**Possible values:**[`0`, ` 1`] 

**Default value:**`0`

  * `0` : Cancel all open orders from this session
  * `1`: Cancel no orders even if the session is disconnected

**5025 - Nonce** string conditional

**Condition:** Trading Logon 

Required for Trading Logon. Time in ms since epoch as string. (This will be used in password generation and check) 

**5030 - ForceResetClOrdID** boolean

**Possible values:**[`Y`, ` N`] 

**Default value:**`N`

Indicate if you want to reset your Clordid sequence while relogging. Suggestion is to use this feature in emergency only. 

**5051 - Rebased** boolean conditional

**Condition:** Effective for trading xstocks only. 

**Possible values:**[`Y`, `N`] 

**Default value:**`N`

  * `N`: new orders/execution reports will be specified in terms of SPV tokens.
  * `Y`: new orders/execution reports will be specified in terms of underlying equity (i.e. multiplier automatically applied by Kraken).

    
    
    8=FIX.4.4|9=76|35=A|49=MYCOMPID|56=KRAKEN-MD|34=1|52=20230707-13:31:03.000|98=0|108=60|141=Y|10=011|  
    
    
    
    8=FIX.4.4|9=250|35=A|49=MYCOMPID|56=KRAKEN-TRD|34=1|52=20230707-13:21:15.000|98=0|108=60|141=N|553=<API_KEY>|554=<PASSWORD>|5025=1688736075072|10=215|  
    

Password is determined by the following formula :
    
    
    base64(HMAC-512(API secret, SHA256(Message-Input + Nonce)))     
    

Where API Secret and Nonce are linked to the API Key and Message-input is composed of the following fields, all followed by the FIX Separator (SOH = ASCII code 01):

  * 35=A
  * 34=MsgSeqNum
  * 49=SENDERCOMPID
  * 56=TARGETCOMPID
  * 553=API_KEY

caution

API-Secret when used in HMAC-512 needs to be base64 decoded.

The nonce is milliseconds since Epoch (always increasing value). We will check if the value of the nonce is not more than 5 seconds away from the current time of the server.

Here is a Python Example to compute the password:
    
    
      
    def get_password(d_msg):  
        api_key = "YOUR API_KEY"  
        api_secret = "YOUR API_SECRET"  
        nonce = str(time.time() * 1000.).split('.')[0]  
        message_input = "35=" + "A" + __SOH__ + "34=" + d_msg["34"] + __SOH__ + "49=" + d_msg["49"] + __SOH__ + "56=" + "KRAKEN-TRD" + __SOH__ + "553=" + api_key + __SOH__  
        api_sha256 = hashlib.sha256((message_input + nonce).encode("utf-8")).digest()  
        api_hmac = hmac.new(base64.b64decode(api_secret), api_sha256, hashlib.sha512)  
        fix_password = base64.b64encode(api_hmac.digest())  
        return fix_password