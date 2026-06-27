---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/fix-auth
api_type: Guide
updated_at: 2026-05-27 19:57:10.966748
---

# FIX Authentication

Both public market data and private trading endpoints requires a first layer of authentication with the usage of `SenderCompID` (Tag 49) at the [logon](/api/docs/fix-api/logon-fix) and on all subsequent messages.

This `senderCompId` will be provided by Kraken support during onboarding. Spot and Derivative will require 2 different pair of sessions. The Derivatives `SenderCompID` that you will be given will have a `DRV` suffix.

For the private logon, another layer of authentication is required and detailed on this [page](/api/docs/fix-api/logon-fix). We recommend using 2 different API Key for Spot and Derivatives but the mechanism to Authenticate will the same on the 2 different sessions. The API Key need to be generated from your pro kraken account in the [settings]<https://pro.kraken.com/app/settings/api>. You will need to create an SPOT API Key with `FIX` type for both Spot and Futures.
    
    
      
    def get_password(d_msg):  
        api_key = "YOUR API_KEY"  
        api_secret = "YOUR API_SECRET"  
        nonce = str(time.time() * 1000.).split('.')[0]  
        message_input = "35=" + "A" + __SOH__ + "34=" + d_msg["34"] + __SOH__ + "49=" + d_msg["49"] + __SOH__ + "56=" + "KRAKEN-TRD" + __SOH__ + "553=" + api_key + __SOH__  
        api_sha256 = hashlib.sha256((message_input + nonce).encode("utf-8")).digest()  
        api_hmac = hmac.new(base64.b64decode(api_secret), api_sha256, hashlib.sha512)  
        fix_password = base64.b64encode(api_hmac.digest())  
        return fix_password