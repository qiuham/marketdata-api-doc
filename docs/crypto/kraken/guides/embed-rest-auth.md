---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/embed-rest-auth
api_type: Guide
updated_at: 2026-05-27 19:57:03.794934
---

# Embed REST Authentication

## Authentication Parameters

For the Embed REST API, the following parameters are used for authentication:

  * `API-Key` HTTP header parameter: your public API key.
  * `API-Sign` HTTP header parameter: HMAC-SHA512 signature of the request.
  * `API-Nonce` HTTP header parameter: always increasing, unsigned 64-bit integer.

Optionally, the following header can be included:

  * `Kraken-Version` HTTP header parameter (optional): API version string (e.g., `2025-04-15`). If not specified, the latest version is used.

## Setting the API-Key Parameter

The value for the `API-Key` HTTP header parameter is your **public** API key.

Contact your Payward account representative to obtain API credentials.

caution

From your API key-pair, clearly identify which key is public and which key is private.

  * The **public** key is sent in the `API-Key` header parameter.
  * The **private** key is **never** sent, it is only used to encode the signature for `API-Sign` header parameter.

## Setting the API-Sign Parameter

The value for the `API-Sign` HTTP header parameter is a signature generated from encoding your **private** API key, nonce, encoded payload, and URI path.
    
    
    HMAC-SHA512 of (URI path + SHA256(nonce + JSON body)) and base64 decoded secret API key  
    

### Algorithm Steps

  1. **Build the message** : Concatenate the nonce with the request body (JSON stringified)
* For GET requests: use only the nonce
* For POST/PUT requests: `nonce + JSON.stringify(body)`
  2. **Hash the message** : Compute SHA256 of the encoded message
  3. **Concatenate with path** : Combine the URL path bytes with the SHA256 hash
  4. **Sign** : Generate HMAC-SHA512 using your base64-decoded secret
  5. **Encode** : Base64 encode the signature

### Examples

The following code snippets demonstrate how to generate the signature in Python, Go, and JavaScript.

  * Python
  * Go
  * JavaScript

    
    
    import json  
    import time  
    import hashlib  
    import hmac  
    import base64  
      
    def get_payward_signature(urlpath, data, secret, nonce):  
        """  
        Generate Payward Embed API signature.  
          
        Args:  
            urlpath: API endpoint (e.g., '/b2b/assets')  
            data: Request body dict (None for GET requests)  
            secret: Base64-encoded API secret  
            nonce: Always-increasing integer  
          
        Returns:  
            Base64-encoded signature string  
        """  
        if data is None:  
            encoded = str(nonce).encode('utf-8')  
        else:  
            encoded = (str(nonce) + json.dumps(data)).encode('utf-8')  
          
        message = urlpath.encode() + hashlib.sha256(encoded).digest()  
        mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)  
        return base64.b64encode(mac.digest()).decode()  
      
      
    # Example usage  
    api_secret = "your-api-secret-here"  
    nonce = time.time_ns()  # Nanoseconds (recommended for high-throughput request bursts)  
    endpoint = "/b2b/assets"  
      
    signature = get_payward_signature(endpoint, None, api_secret, nonce)  
    print(f"API-Sign: {signature}")  
    
    
    
    package main  
      
    import (  
        "crypto/hmac"  
        "crypto/sha256"  
        "crypto/sha512"  
        "encoding/base64"  
        "encoding/json"  
        "fmt"  
        "strconv"  
        "time"  
    )  
      
    // GetPaywardSignature generates the Payward Embed API signature.  
    func GetPaywardSignature(urlpath string, data interface{}, secret string, nonce int64) (string, error) {  
        var encoded string  
        if data == nil {  
            encoded = strconv.FormatInt(nonce, 10)  
        } else {  
            jsonData, err := json.Marshal(data)  
            if err != nil {  
                return "", err  
            }  
            encoded = strconv.FormatInt(nonce, 10) + string(jsonData)  
        }  
      
        sha := sha256.New()  
        sha.Write([]byte(encoded))  
        shaSum := sha.Sum(nil)  
      
        message := append([]byte(urlpath), shaSum...)  
      
        secretBytes, err := base64.StdEncoding.DecodeString(secret)  
        if err != nil {  
            return "", err  
        }  
        mac := hmac.New(sha512.New, secretBytes)  
        mac.Write(message)  
        macSum := mac.Sum(nil)  
      
        return base64.StdEncoding.EncodeToString(macSum), nil  
    }  
      
    func main() {  
        apiSecret := "your-api-secret-here"  
        nonce := time.Now().UnixNano()  // Nanoseconds (recommended for high-throughput request bursts)  
        endpoint := "/b2b/assets"  
      
        signature, err := GetPaywardSignature(endpoint, nil, apiSecret, nonce)  
        if err != nil {  
            fmt.Println("Error:", err)  
            return  
        }  
        fmt.Printf("API-Sign: %s\n", signature)  
    }  
    
    
    
    import crypto from 'crypto';  
      
    /**  
* Generate Payward Embed API signature.  
* @param {string} urlpath - API endpoint (e.g., '/b2b/assets')  
* @param {Object|null} data - Request body (null for GET requests)  
* @param {string} secret - Base64-encoded API secret  
* @param {bigint|number|string} nonce - Always-increasing integer  
* @returns {string} Base64-encoded signature  
 */  
    function getPaywardSignature(urlpath, data, secret, nonce) {  
      const encoded = data === null   
        ? String(nonce)   
        : String(nonce) + JSON.stringify(data);  
      
      const sha256Hash = crypto.createHash('sha256').update(encoded).digest();  
      const message = Buffer.concat([Buffer.from(urlpath), sha256Hash]);  
        
      const secretBuffer = Buffer.from(secret, 'base64');  
      const hmac = crypto.createHmac('sha512', secretBuffer);  
      hmac.update(message);  
        
      return hmac.digest('base64');  
    }  
      
    // Example usage  
    const apiSecret = 'your-api-secret-here';  
    const nonce = process.hrtime.bigint().toString();  // Monotonic nanoseconds (recommended for JS)  
    const endpoint = '/b2b/assets';  
      
    const signature = getPaywardSignature(endpoint, null, apiSecret, nonce);  
    console.log(`API-Sign: ${signature}`);  
    

## Setting the API-Nonce Parameter

The value for the `API-Nonce` HTTP header parameter is an always increasing, unsigned 64-bit integer for each request made with a particular API key.

While a simple counter would provide a valid nonce, a common method is to use a UNIX timestamp in milliseconds. For fast sequential or parallel request bursts, we recommend a higher-resolution nonce strategy (for example nanosecond-resolution values) to reduce collisions and ordering issues. Once you choose a format for an API key, keep that format consistent and ensure each new nonce is greater than the previous one. For JavaScript clients, we recommend `process.hrtime.bigint()` because it is monotonic and avoids wall-clock drift.

tip

Problems can arise from requests arriving out of order due to API keys being shared across processes, or from system clock drift/recalibration. If multiple workers share one API key, coordinate nonces through a shared per-key generator (for example an atomic counter in Redis or another centralized store). When configuring Domain Management API keys, use the **Custom number only used once window** setting. Increase this value if you receive `Invalid nonce` (or `EAPI:Invalid nonce`) errors due to networking delays or out-of-order delivery, since this setting adjusts nonce tolerance.

### Examples

  * Python
  * Go
  * JavaScript

    
    
    import time  
      
    # Nanosecond nonce (recommended for high-throughput request bursts)  
    nonce = time.time_ns()  
    
    
    
    import "time"  
      
    // Nanosecond nonce (recommended for high-throughput request bursts)  
    nonce := time.Now().UnixNano()  
    
    
    
    // Monotonic nonce (recommended for JavaScript)  
    const nonce = process.hrtime.bigint().toString();  
    

## Complete Request Example

Here's a complete example making an authenticated GET request to list assets:

  * Python
  * JavaScript

    
    
    import os  
    import json  
    import time  
    import hashlib  
    import hmac  
    import base64  
    import requests  
      
    API_KEY = os.environ.get("PAYWARD_API_KEY")  
    API_SECRET = os.environ.get("PAYWARD_API_SECRET")  
    BASE_URL = "https://nexus.kraken.com"  
      
      
    def get_payward_signature(urlpath, data, secret, nonce):  
        if data is None:  
            encoded = str(nonce).encode("utf-8")  
        else:  
            encoded = (str(nonce) + json.dumps(data)).encode("utf-8")  
      
        message = urlpath.encode() + hashlib.sha256(encoded).digest()  
        mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)  
        return base64.b64encode(mac.digest()).decode()  
      
      
    def list_assets():  
        endpoint = "/b2b/assets"  
        nonce = time.time_ns()  # Nanoseconds (recommended for high-throughput request bursts)  
        signature = get_payward_signature(endpoint, None, API_SECRET, nonce)  
      
        headers = {  
            "API-Key": API_KEY,  
            "API-Sign": signature,  
            "API-Nonce": str(nonce),  
        }  
      
        response = requests.get(BASE_URL + endpoint, headers=headers)  
        return response.json()  
      
      
    assets = list_assets()  
    print(assets)  
    
    
    
    import crypto from 'crypto';  
      
    const API_KEY = process.env.PAYWARD_API_KEY;  
    const API_SECRET = process.env.PAYWARD_API_SECRET;  
    const BASE_URL = 'https://nexus.kraken.com';  
      
    function getPaywardSignature(urlpath, data, secret, nonce) {  
      const encoded = data === null   
        ? String(nonce)   
        : String(nonce) + JSON.stringify(data);  
      
      const sha256Hash = crypto.createHash('sha256').update(encoded).digest();  
      const message = Buffer.concat([Buffer.from(urlpath), sha256Hash]);  
        
      const secretBuffer = Buffer.from(secret, 'base64');  
      const hmac = crypto.createHmac('sha512', secretBuffer);  
      hmac.update(message);  
        
      return hmac.digest('base64');  
    }  
      
    async function listAssets() {  
      const endpoint = '/b2b/assets';  
      const nonce = process.hrtime.bigint().toString();  // Monotonic nanoseconds (recommended for JS)  
      const signature = getPaywardSignature(endpoint, null, API_SECRET, nonce);  
      
      const response = await fetch(BASE_URL + endpoint, {  
        method: 'GET',  
        headers: {  
          'API-Key': API_KEY,  
          'API-Sign': signature,  
          'API-Nonce': String(nonce),  
        },  
      });  
      
      return response.json();  
    }  
      
    const assets = await listAssets();  
    console.log(assets);  
    

## Query Parameters in Signature

When your request includes query parameters, they must be included in the URL path used for signature generation:
    
    
    // Include query params in the signature path  
    const params = { 'page[size]': 10, quote: 'USD' };  
    const queryString = new URLSearchParams(params).toString();  
    const signaturePath = `/b2b/assets?${queryString}`;  
      
    const signature = getPaywardSignature(signaturePath, null, API_SECRET, nonce);  
    

## Troubleshooting

Error| Cause| Solution  
---|---|---  
`Invalid signature`| Signature doesn't match| Verify secret encoding, nonce, and body format  
`Invalid nonce`| Nonce is not increasing| Ensure nonce > previous nonce  
`Missing API-Key`| Header not set| Check header name is exactly `API-Key`  
* Authentication Parameters
  * Setting the API-Key Parameter
  * Setting the API-Sign Parameter
* Algorithm Steps
* Examples
  * Setting the API-Nonce Parameter
* Examples
  * Complete Request Example
  * Query Parameters in Signature
  * Troubleshooting