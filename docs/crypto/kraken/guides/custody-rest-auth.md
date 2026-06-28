---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/custody-rest-auth
api_type: Guide
updated_at: 2026-05-27 19:56:26.793409
---

# Custody REST Authentication

The Custody REST API uses API keys to authenticate and authorize API requests. A secure authentication process is enforced to ensure high security both when creating API keys and when making API calls. To authenticate API requests, you must first create an API user and obtain API key credentials.

## API Users and Access Control

API users function similarly to human users in that they are assigned roles, permissions, and vault access at the time of creation. When an API user interacts with the system, these settings are enforced to control which data they can access and which actions they can perform.

However, unlike regular users, API users cannot log in to the Custody application. Their interaction with the system is limited strictly to API calls, making them an essential component for programmatic access while maintaining strict security boundaries.

## Creating a new API Key

A system administrator must initiate the creation of a new API user before generating an API key:

  1. Log in to your Custody environment
  2. Navigate to Settings → Users → API Users
  3. Submit a request for a new API user and complete the two-factor authentication (2FA) process
  4. The request will appear under Tasks → Pending until it is approved by the Admin Quorum
  5. Once approved, open the request details to view the API key information
  6. The admin user who submitted the request can access the API key and secret from the API key details page

caution

Only the admin user who created the API user request can view the API key and secret. Store these credentials securely. For security reasons, the API key and secret will not be viewable again after they are generated. API key credentials are a prime target for malicious actors. Ensure you follow security best practices to protect them.

## Authentication Parameters

For the REST API, the following parameters are used for authentication to endpoints which contain private data:

  * `API-Key` HTTP header parameter: the public key from your API key-pair.
  * `API-Sign` HTTP header parameter: encrypted signature of message.
  * `nonce` payload parameter: always increasing, unsigned 64-bit integer.

## Setting the API-Key Parameter

The value for the `API-Key` HTTP header parameter is your **public** API key.

An API key-pair is required to access the authenticated endpoints.

caution

From your API key-pair, clearly identify which key is public and which key is private.

  * The **public** key is sent in the `API-Key` header parameter.
  * The **private** key is **never** sent, it is only used to encode the signature for `API-Sign` header parameter.

## Setting the API-Sign Parameter

The value for the `API-Sign` HTTP header parameter is a signature generated from encoding your **private** API key, nonce, encoded payload, and URI path.
    
    
      HMAC-SHA512 of (URI path + SHA256(nonce + POST data)) and base64 decoded secret API key  
    

Note: The URI path used for API-Sign should be the part starting with "/0/private" of the API URL.

### Examples

The following is a specific example of a signature generated with a particular private key, nonce, and payload corresponding to a new limit order (buy 1.25 XBTUSD at $37,500). If your code is generating a different signature (`API-Sign`) for this example, then there is likely an issue with your application of the above methodology. Code snippets for generating the signature in Python, Golang and Node.js follow below.

Field| Value  
---|---  
Private Key| kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg==  
Nonce| 1616492376594  
Encoded Payload| nonce=1616492376594  
URI Path| /0/private/GetCustodyTask?id=TGWOJ4JQPOTZT2  
**API-Sign**| **2rM09q8HG7LvjivBitQUybwZ/DSeO8+i0U/at/wclH2Jma6gMaE/0Nw9dyLR+ykMd5eWCngSL4K58i6uJzXDCw==**  
* Python
  * Go
  * Node JS

    
    
    import urllib.parse  
    import hashlib  
    import hmac  
    import base64  
      
    def get_kraken_signature(urlpath, data, secret):  
      
        if isinstance(data, str):  
            encoded = (str(json.loads(data)["nonce"]) + data).encode()  
        else:  
            encoded = (str(data["nonce"]) + urllib.parse.urlencode(data)).encode()  
        message = urlpath.encode() + hashlib.sha256(encoded).digest()  
      
        mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)  
        sigdigest = base64.b64encode(mac.digest())  
        return sigdigest.decode()  
      
    api_sec = "kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg=="  
      
    payload = {  
      "nonce": 1616492376594,  
    }  
      
    signature = get_kraken_signature("/0/private/GetCustodyTask?id=TGWOJ4JQPOTZT2", payload, api_sec)  
    print("API-Sign: {}".format(signature))  
      
    
    
    
    package main  
      
    import (  
        "crypto/hmac"  
        "crypto/sha256"  
        "crypto/sha512"  
        "encoding/base64"  
        "net/url"  
        "fmt"  
        "encoding/json"  
        "strings"  
      
        )  
      
        func getKrakenSignature(urlPath string, data interface{}, secret string) (string, error) {  
            var encodedData string  
      
            switch v := data.(type) {  
            case string:  
                var jsonData map[string]interface{}  
                if err := json.Unmarshal([]byte(v), &jsonData); err != nil {  
                    return "", err  
                }  
                encodedData = jsonData["nonce"].(string) + v  
            case map[string]interface{}:  
                dataMap := url.Values{}  
                for key, value := range v {  
                    dataMap.Set(key, fmt.Sprintf("%v", value))  
                }  
                encodedData = v["nonce"].(string) + dataMap.Encode()  
            default:  
                return "", fmt.Errorf("invalid data type")  
            }  
            sha := sha256.New()  
            sha.Write([]byte(encodedData))  
            shasum := sha.Sum(nil)  
      
            message := append([]byte(urlPath), shaSum...)  
            mac := hmac.New(sha512.New, base64.StdEncoding.DecodeString(secret))  
            mac.Write(message)  
            macsum := mac.Sum(nil)  
            sigDigest := base64.StdEncoding.EncodeToString(macSum)  
            return sigDigest, nil  
        }  
      
        func main() {  
      
            apiSecret := "kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg=="  
      
            payload := map[string]interface{}{  
                "nonce":     1616492376594,  
            }  
      
            signature, err := getKrakenSignature("/0/private/GetCustodyTask?id=TGWOJ4JQPOTZT2", payload, apiSec)  
            if err != nil {  
                fmt.Println("Error generating signature:", err)  
                return  
            }  
            fmt.Printf("API-Sign: %s\n", signature)  
        }  
    
    
    
    const crypto = require('crypto');  
    const querystring = require('querystring');  
      
    // Function to get Kraken signature  
    function getKrakenSignature(urlPath, data, secret) {  
      let encoded;  
      if (typeof data === 'string') {  
        const jsonData = JSON.parse(data);  
        encoded = jsonData.nonce + data;  
      } else if (typeof data === 'object') {  
        const dataStr = querystring.stringify(data);  
        encoded = data.nonce + dataStr;  
      } else {  
        throw new Error('Invalid data type');  
      }  
      
      const sha256Hash = crypto.createHash('sha256').update(encoded).digest();  
      const message = urlPath + sha256Hash.toString('binary');  
      const secretBuffer = Buffer.from(secret, 'base64');  
      const hmac = crypto.createHmac('sha512', secretBuffer);  
      hmac.update(message, 'binary');  
      const signature = hmac.digest('base64');  
      return signature;  
    }  
      
    const apiSec = 'kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg==';  
      
    const payload = JSON.stringify({  
      nonce: 1616492376594,  
    });  
      
    const signature = getKrakenSignature('/0/private/GetCustodyTask?id=TGWOJ4JQPOTZT2', payload, apiSec);  
    console.log(`API-Sign: ${signature}`);  
    

## Setting the nonce Parameter

The value for the `nonce` payload body parameter is an always increasing, unsigned 64-bit integer for each request that is made with a particular API key.

While a simple counter would provide a valid nonce, a more usual method of generating a valid nonce is to use e.g. a UNIX timestamp in milliseconds. There is no way to reset the nonce for an API key to a lower value, so be sure to use a nonce generation method that won't produce numbers less than the previous nonce.

Too many requests with invalid nonces (EAPI:Invalid nonce) can result in temporary bans.

Problems can arise from requests arriving out of order due to API keys being shared across processes, or from system clock drift/recalibration. An optional "nonce window" can be configured to specify a tolerance between nonce values.

### Examples

The following are some examples of how to generate valid millisecond resolution nonce values in different programming languages:

  * Python
  * JavaScript
  * PHP

    
    
    import time  
      
    api_nonce = time.time_ns()  
    
    
    
    const api_nonce = Date.now()  
    
    
    
    $api_nonce = explode(' ', microtime());  
    $api_nonce = $api_nonce[1].substr($api_nonce[0], 2, 3);  
* API Users and Access Control
  * Creating a new API Key
  * Authentication Parameters
  * Setting the API-Key Parameter
  * Setting the API-Sign Parameter
* Examples
  * Setting the nonce Parameter
* Examples