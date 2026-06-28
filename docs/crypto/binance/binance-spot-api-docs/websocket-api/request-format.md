---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/request-format
api_type: WebSocket
updated_at: 2026-05-27 18:55:12.898684
---

# Request security

* Each method has a security type indicating required API key permissions, shown next to the method name (e.g., [Place new order (TRADE)](/docs/binance-spot-api-docs/websocket-api/request-security#place-new-order-trade)).
  * If unspecified, the security type is `NONE`.
  * Except for `NONE`, all methods with a security type are considered `SIGNED` requests (i.e. including a `signature`), except for [listenKey management](/docs/binance-spot-api-docs/websocket-api/request-security#user-data-stream-requests).
  * Secure methods require a valid API key to be specified and authenticated. 
    * API keys can be created on the [API Management](https://www.binance.com/en/support/faq/360002502072) page of your Binance account.
    * **Both API key and secret key are sensitive.** Never share them with anyone. If you notice unusual activity in your account, immediately revoke all the keys and contact Binance support.
  * API keys can be configured to allow access only to certain types of secure methods. 
    * For example, you can have an API key with `TRADE` permission for trading, while using a separate API key with `USER_DATA` permission to monitor your order status.
    * By default, an API key cannot `TRADE`. You need to enable trading in API Management first.

Security type| Description  
---|---  
`NONE`| Public market data  
`TRADE`| Trading on the exchange, placing and canceling orders  
`USER_DATA`| Private account information, such as order status and your trading history  
`USER_STREAM`| Managing User Data Stream subscriptions  
  
### SIGNED request security[​](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-security "Direct link to SIGNED request security")

  * `SIGNED` requests require an additional parameter: `signature`, authorizing the request.



#### Signature Case Sensitivity[​](/docs/binance-spot-api-docs/websocket-api/request-security#signature-case-sensitivity "Direct link to Signature Case Sensitivity")

  * **HMAC:** Signatures generated using HMAC are **not case-sensitive**. This means the signature string can be verified regardless of letter casing.
  * **RSA:** Signatures generated using RSA are **case-sensitive**.
  * **Ed25519:** Signatures generated using ED25519 are also **case-sensitive**



Please consult [SIGNED request example (HMAC)](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-hmac), [SIGNED request example (RSA)](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-rsa), and [SIGNED request example (Ed25519)](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-ed25519) on how to compute signature, depending on which API key type you are using.

### Timing security[​](/docs/binance-spot-api-docs/websocket-api/request-security#timing-security "Direct link to Timing security")

  * `SIGNED` requests also require a `timestamp` parameter which should be the current timestamp either in milliseconds or microseconds. (See [General API Information](/docs/binance-spot-api-docs/websocket-api/request-security#general-api-information))
  * An additional optional parameter, `recvWindow`, specifies for how long the request stays valid and may only be specified in milliseconds. 
    * `recvWindow` supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
    * If `recvWindow` is not sent, **it defaults to 5000 milliseconds**.
    * Maximum `recvWindow` is 60000 milliseconds.
  * Request processing logic is as follows:


    
    
    serverTime = getCurrentTime()  
    if (timestamp < (serverTime + 1 second) && (serverTime - timestamp) <= recvWindow) {  
      // begin processing request  
      serverTime = getCurrentTime()  
      if (serverTime - timestamp) <= recvWindow {  
        // forward request to Matching Engine  
      } else {  
        // reject request  
      }  
      // finish processing request  
    } else {  
      // reject request  
    }  
    

**Serious trading is about timing.** Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With `recvWindow`, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

**It is recommended to use a small`recvWindow` of 5000 or less!**

### SIGNED request example (HMAC)[​](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-hmac "Direct link to SIGNED request example \(HMAC\)")

Here is a step-by-step guide on how to sign requests using an HMAC secret key.

Example API key and secret key:

Key| Value  
---|---  
`apiKey`| `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A`  
`secretKey`| `NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j`  
  
**WARNING: DO NOT SHARE YOUR API KEY AND SECRET KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

Example of a request with a symbol name containing non-ASCII characters:
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "BUY",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

As you can see, the `signature` parameter is currently missing.

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name** :

For the first set of example parameters (ASCII only):

Parameter| Value  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
For the second set of example parameters (some non-ASCII characters):

Parameter| Value  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`price`| 0.10000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| BUY  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:
    
    
    apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:
    
    
    apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

**Step 2: Compute the signature**

  1. Use the `secretKey` of your API key as the signing key for the HMAC-SHA-256 algorithm.
  2. Sign the UTF-8 bytes of the signature payload constructed in Step 1.
  3. Encode the HMAC-SHA-256 output as a hex string.



Note that `apiKey`, `secretKey`, and the payload are **case-sensitive** , while the resulting signature value is case-insensitive.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):
    
    
    $ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
      | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'  
      
    aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    $ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
      | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'  
      
    b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd  
    

**Step 3: Add`signature` to request `params`**

Complete the request by adding the `signature` parameter with the signature string.

For the first set of example parameters (ASCII only):
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24"  
        }  
    }  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "BUY",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "1.00000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd"  
        }  
    }  
    

### SIGNED request example (RSA)[​](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-rsa "Direct link to SIGNED request example \(RSA\)")

Here is a step-by-step guide on how to sign requests using an RSA private key.

Key| Value  
---|---  
`apiKey`| `CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ`  
  
These examples assume the private key is stored in the file `test-rsa-prv.pem`.

**WARNING: DO NOT SHARE YOUR API KEY AND PRIVATE KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

Example of a request with a symbol name containing non-ASCII characters:
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "BUY",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name** :

For the first set of example parameters (ASCII only):

Parameter| Value  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
For the second set of example parameters (some non-ASCII characters):

Parameter| Value  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
`price`| 0.10000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| BUY  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:
    
    
    apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:
    
    
    apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

**Step 2: Compute the signature**

  1. Sign the UTF-8 bytes of the signature payload constructed in Step 1 using the RSASSA-PKCS1-v1_5 algorithm with SHA-256 hash function.
  2. Encode the output in base64.



Note that `apiKey`, the payload, and the resulting `signature` are **case-sensitive**.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):
    
    
    $ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
      | openssl dgst -sha256 -sign test-rsa-prv.pem \  
      | openssl enc -base64 -A  
      
    OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA==  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    $ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
      | openssl dgst -sha256 -sign test-rsa-prv.pem \  
      | openssl enc -base64 -A  
      
    F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw==  
    

**Step 3: Add`signature` to request `params`**

Complete the request by adding the `signature` parameter with the signature string.

For the first set of example parameters (ASCII only):
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "newOrderRespType": "ACK",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
            "signature": "OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA=="  
        }  
    }  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "1.00000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
            "signature": "F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw=="  
        }  
    }  
    

### SIGNED Request Example (Ed25519)[​](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-ed25519 "Direct link to SIGNED Request Example \(Ed25519\)")

**Note: It is highly recommended to use Ed25519 API keys as they will provide the best performance and security out of all supported key types.**

Here is a step-by-step guide on how to sign requests using an Ed25519 private key.

Key| Value  
---|---  
`apiKey`| `4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO`  
  
These examples assume the private key is stored in the file `test-ed25519-prv.pem`.

**WARNING: DO NOT SHARE YOUR API KEY AND PRIVATE KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

Example of a request with a symbol name containing non-ASCII characters:
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "BUY",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name** :

For the first set of example parameters (ASCII only):

Parameter| Value  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
For the second set of example parameters (some non-ASCII characters):

Parameter| Value  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
`price`| 0.20000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| SELL  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1668481559918  
`type`| LIMIT  
  
Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:
    
    
    apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:
    
    
    apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

**Step 2: Compute the signature**

  1. Sign the UTF-8 bytes of your signature payload constructed in Step 1 using the Ed25519 private key.
  2. Encode the output in base64.



Note that `apiKey`, the payload, and the resulting `signature` are **case-sensitive**.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):
    
    
    echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \  
      | openssl dgst -sign ./test-ed25519-prv.pem \  
      | openssl enc -base64 -A  
      
    EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg==  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \  
      | openssl dgst -sign ./test-ed25519-prv.pem \  
      | openssl enc -base64 -A  
      
    dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA==  
    

**Step 3: Add the signature to request`params`**

For the first set of example parameters (ASCII only):
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "newOrderRespType": "ACK",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
            "signature": "EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg=="  
        }  
    }  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "1.00000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
            "signature": "dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA=="  
        }  
    }  
    

Here is a sample Python script performing all the steps above:
    
    
    #!/usr/bin/env python3  
      
    import base64  
    import time  
    import json  
    from cryptography.hazmat.primitives.serialization import load_pem_private_key  
    from websocket import create_connection  
      
    # Set up authentication  
    API_KEY='put your own API Key here'  
    PRIVATE_KEY_PATH='test-prv-key.pem'  
      
    # Load the private key.  
    # In this example the key is expected to be stored without encryption,  
    # but we recommend using a strong password for improved security.  
    with open(PRIVATE_KEY_PATH, 'rb') as f:  
      private_key = load_pem_private_key(data=f.read(), password=None)  
      
    # Set up the request parameters  
    params = {  
        'apiKey':       API_KEY,  
        'symbol':       '１２３４５６',  
        'side':         'SELL',  
        'type':         'LIMIT',  
        'timeInForce':  'GTC',  
        'quantity':     '1.0000000',  
        'price':        '0.10000000',  
        'recvWindow':   5000  
    }  
      
    # Timestamp the request  
    timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds  
    params['timestamp'] = timestamp  
      
    # Sort parameters alphabetically by name  
    params = dict(sorted(params.items()))  
      
    # Compute the signature payload  
    payload = '&'.join([f"{k}={v}" for k,v in params.items()]) # no percent encoding here!  
      
    # Sign the request  
    signature = base64.b64encode(private_key.sign(payload.encode('UTF-8')))  
    params['signature'] = signature.decode('ASCII')  
      
    # Send the request  
    request = {  
        'id': 'my_new_order',  
        'method': 'order.place',  
        'params': params  
    }  
      
    ws = create_connection("wss://ws-api.binance.com:443/ws-api/v3")  
    ws.send(json.dumps(request))  
    result =  ws.recv()  
    ws.close()  
      
    print(result)

---

# 请求鉴权类型

* 每个方法都有一个鉴权类型，指示所需的 API 密钥权限，显示在方法名称旁边（例如，[下新订单 (TRADE)](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-place)）。
  * 如果未指定，则鉴权类型为 `NONE`。
  * 除了为 `NONE` 外，所有具有鉴权类型的方法均视为 `SIGNED` 请求（即包含 `signature`），[listenKey 管理](/docs/zh-CN/binance-spot-api-docs/websocket-api/account-requests#user-data-stream-requests) 除外。
  * 具有鉴权类型的方法需要提供有效的 API 密钥并验证通过。 
    * API 密钥可在您的 Binance 账户的 [API 管理](https://www.binance.com/en/support/faq/360002502072) 页面创建。
    * **API 密钥和密钥对均为敏感信息，切勿与他人分享。** 如果发现账户有异常活动，请立即撤销所有密钥并联系 Binance 支持。
  * API 密钥可配置为仅允许访问某些鉴权类型。 
    * 例如，您可以拥有具有 `TRADE` 权限的 API 密钥用于交易， 同时使用具有 `USER_DATA` 权限的另一个 API 密钥来监控订单状态。
    * 默认情况下，API 密钥无法进行 `TRADE`，您需要先在 API 管理中启用交易权限。

鉴权类型| 描述  
---|---  
`NONE`| 公开市场数据  
`TRADE`| 在交易所交易，下单和取消订单  
`USER_DATA`| 私人账户信息，例如订单状态和交易历史  
`USER_STREAM`| 管理用户数据流订阅  
  
### 需要签名的请求[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/request-security#需要签名的请求 "需要签名的请求的直接链接")

  * 为了授权请求，`SIGNED` 请求必须带 `signature` 参数。



#### 签名区分大小写[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/request-security#签名区分大小写 "签名区分大小写的直接链接")

  * **HMAC：** 使用 HMAC 生成的签名**不区分大小写** 。这意味着无论字母大小写如何，签名字符串都可以被验证。
  * **RSA：** 使用 RSA 生成的签名**区分大小写** 。
  * **Ed25519：** 使用 Ed25519 生成的签名也**区分大小写** 。



### 时间同步安全[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/request-security#时间同步安全 "时间同步安全的直接链接")

  * `SIGNED` 请求还需要一个 `timestamp` 参数，该参数应为当前时间戳，单位为毫秒或微秒。（参见 [通用 API 信息](/docs/zh-CN/binance-spot-api-docs/websocket-api/autogen_intro#general-api-information)）
  * 另一个可选参数 `recvWindow`，用以指定请求的有效期，只能以毫秒为单位。 
    * `recvWindow` 扩展为三位小数（例如 6000.346），以便可以指定微秒。
    * 如果未发送 `recvWindow`，则 **默认为 5000 毫秒** 。
    * `recvWindow` 的最大值为 60000 毫秒。
  * 请求处理逻辑如下：


    
    
    serverTime = getCurrentTime()  
    if (timestamp < (serverTime + 1 second) && (serverTime - timestamp) <= recvWindow) {  
      // 开始处理请求  
      serverTime = getCurrentTime()  
      if (serverTime - timestamp) <= recvWindow {  
        // 将请求转发到撮合引擎  
      } else {  
        // 拒绝请求  
      }  
      // 结束处理请求  
    } else {  
      // 拒绝请求  
    }  
    

**关于交易时效性** 互联网状况并不完全稳定可靠，因此你的程序本地到币安服务器的时延会有抖动, 这是我们设置 `recvWindow` 的目所在。如果你从事高频交易，对交易时效性有较高的要求，可以灵活设置 `recvWindow` 以达到你的要求。

**建议使用5000毫秒以下的`recvWindow`！**

### SIGNED 请求示例 (HMAC)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/request-security#signed-请求示例-hmac "SIGNED 请求示例 \(HMAC\)的直接链接")

这是有关如何用一个 HMAC secret key 签署请求的分步指南。

示例 API key 和 secret key：

Key| Value  
---|---  
`apiKey`| `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A`  
`secretKey`| `NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j`  
  
**警告：请勿与任何人分享您的 API 密钥和秘钥。**

此处提供的示例密钥仅用于示范说明目的。

交易对名称完全由 ASCII 字符组成的请求示例：

请求示例：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "newOrderRespType": "ACK",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "------ 未填写 ------"  
        }  
    }  
    

交易对名称包含非 ASCII 字符的请求示例：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "BUY",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

**第一步：创建签名内容**

除了 `signature` 之外，获取所有请求 `params`，然后**按参数名称的字母顺序对它们进行排序** ：

对于第一组示例参数（仅限 ASCII 字符）：

参数| 取值  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
对于第二组示例参数（包含一些 Unicode 字符）：

参数| 取值  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`price`| 0.10000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| BUY  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
将参数格式化为 `参数=取值` 对并用 `&` 分隔每个参数对。数值需要采用 UTF-8 编码。

对于第一组示例参数（仅限 ASCII 字符），签名有效负载将如下所示：
    
    
    apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

对于第二组示例参数（包含一些 Unicode 字符），签名有效负载将如下所示：
    
    
    apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

**第二步：计算签名**

  1. 使用 API 密钥中的 `secretKey` 作为 HMAC-SHA-256 算法的签名密钥。
  2. 对步骤 1 中构建的签名 payload 进行签名。
  3. 将 HMAC-SHA-256 的输出编码为十六进制字符串。



请注意，`apiKey`、`secretKey` 和有效负载是**大小写敏感的** 。而生成的签名值是不区分大小写的。

可以使用 OpenSSL 交叉检查您的签名算法实现：

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    $ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
      | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'  
      
    aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    $ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
      | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'  
      
    b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd  
    

**第三步：添加`signature` 到 `params` 中**

通过在对请求中添加 `signature` 参数和签名字串来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24"  
        }  
    }  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "BUY",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "1.00000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd"  
        }  
    }  
    

### SIGNED 请求示例 (RSA)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/request-security#signed-请求示例-rsa "SIGNED 请求示例 \(RSA\)的直接链接")

这是有关如何用一个 RSA private key 签署请求的分步指南。

Key| Value  
---|---  
`apiKey`| `CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ`  
  
这些示例假设私钥存储在文件 `test-prv-key.pem` 中。

**警告：请勿与任何人分享您的 API 密钥和私钥。**

此处提供的示例密钥仅用于示范说明目的。

交易对名称完全由 ASCII 字符组成的请求示例：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

交易对名称包含非 ASCII 字符的请求示例：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "BUY",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

**第一步：创建签名内容**

除了 `signature`，获取请求的所有其它 `params`，然后**按参数名称的字母顺序对它们进行排序** ：

对于第一组示例参数（仅限 ASCII 字符）：

参数| 取值  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
对于第二组示例参数（包含一些 Unicode 字符）：

参数| 取值  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
`price`| 0.10000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| BUY  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
将参数格式化为 `参数=取值` 对并用 `&` 分隔每个参数对。数值需要采用 UTF-8 编码。

对于第一组示例参数（仅限 ASCII 字符），签名有效负载将如下所示：
    
    
    apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

对于第二组示例参数（包含一些 Unicode 字符），签名有效负载将如下所示：
    
    
    apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

**第二步：计算签名**

  1. 使用 RSASSA-PKCS1-v1_5 算法和 SHA-256 哈希函数对步骤 1 中构造的签名有效载荷的 UTF-8 字节进行签名。
  2. 将输出编码为 base64。



请注意，`apiKey`, payload 和生成的`签名值`都是**大小写敏感** 的。

您可以使用 OpenSSL 交叉检查您的签名算法：

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    $ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
      | openssl dgst -sha256 -sign test-rsa-prv.pem \  
      | openssl enc -base64 -A  
      
    OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA==  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    $ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
      | openssl dgst -sha256 -sign test-rsa-prv.pem \  
      | openssl enc -base64 -A  
      
    F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw==  
    

**第三步：在请求的`params` 参数添加签名值**

通过在对请求中添加 `signature` 参数和签名字串来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "newOrderRespType": "ACK",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
            "signature": "OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA=="  
        }  
    }  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "1.00000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
            "signature": "F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw=="  
        }  
    }  
    

### SIGNED 请求示例 (Ed25519)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/request-security#signed-请求示例-ed25519 "SIGNED 请求示例 \(Ed25519\)的直接链接")

**我们强烈建议使用 Ed25519 API keys，因为它在所有受支持的 API key 类型中提供最佳性能和安全性。**

这是有关如何用一个 Ed25519 private key 签署请求的分步指南。

Key| Value  
---|---  
`apiKey`| `4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO`  
  
这些示例假设私钥存储在文件 `test-ed25519-prv.pem` 中。

**警告：请勿与任何人分享您的 API 密钥和私钥。**

此处提供的示例密钥仅用于示范说明目的。

交易对名称完全由 ASCII 字符组成的请求示例：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

交易对名称包含非 ASCII 字符的请求示例：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "BUY",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
            "signature": "------ FILL ME ------"  
        }  
    }  
    

**第一步：创建签名内容**

除了 `signature`，获取请求的所有其它 `params`，然后**按参数名称的字母顺序对它们进行排序** ：

对于第一组示例参数（仅限 ASCII 字符）：

参数| 取值  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
对于第二组示例参数（包含一些 Unicode 字符）：

参数| 取值  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
`price`| 0.20000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| SELL  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1668481559918  
`type`| LIMIT  
  
将参数格式化为 `参数=取值` 对并用 `&` 分隔每个参数对。数值需要采用 UTF-8 编码。

对于第一组示例参数（仅限 ASCII 字符），签名有效负载将如下所示：
    
    
    apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

对于第二组示例参数（包含一些 Unicode 字符），签名有效负载将如下所示：
    
    
    apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT  
    

**第二步：计算签名**

  1. 使用 Ed25519 密钥对步骤 1 中构造的签名有效载荷的 UTF-8 字节进行签名。
  2. 将输出编码为 base64。



请注意，`apiKey`, payload 和生成的`签名值`都是**大小写敏感** 的。

您可以使用 OpenSSL 交叉检查您的签名算法：

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \  
      | openssl dgst -sign ./test-ed25519-prv.pem \  
      | openssl enc -base64 -A  
      
    EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg==  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \  
      | openssl dgst -sign ./test-ed25519-prv.pem \  
      | openssl enc -base64 -A  
      
    dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA==  
    

**第三步：在请求的`params` 参数添加签名值**

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "0.01000000",  
            "price": "52000.00",  
            "newOrderRespType": "ACK",  
            "recvWindow": 100,  
            "timestamp": 1645423376532,  
            "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
            "signature": "EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg=="  
        }  
    }  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    {  
        "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
        "method": "order.place",  
        "params": {  
            "symbol": "１２３４５６",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "quantity": "1.00000000",  
            "price": "0.10000000",  
            "recvWindow": 5000,  
            "timestamp": 1645423376532,  
            "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
            "signature": "dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA=="  
        }  
    }  
    

下面的 Python 示例代码能执行上述所有步骤。
    
    
    #!/usr/bin/env python3  
      
    import base64  
    import time  
    import json  
    from cryptography.hazmat.primitives.serialization import load_pem_private_key  
    from websocket import create_connection  
      
    # 设置身份验证：  
    API_KEY='替换成您的 API Key'  
    PRIVATE_KEY_PATH='test-prv-key.pem'  
      
    # 加载 private key。  
    # 在这个例子中，private key 没有加密  
    # 但我们建议使用强密码以提高安全性。  
    with open(PRIVATE_KEY_PATH, 'rb') as f:  
      private_key = load_pem_private_key(data=f.read(), password=None)  
      
    # 设置请求参数：  
    params = {  
        'apiKey':       API_KEY,  
        'symbol':       '１２３４５６',  
        'side':         'SELL',  
        'type':         'LIMIT',  
        'timeInForce':  'GTC',  
        'quantity':     '1.0000000',  
        'price':        '0.10000000',  
        'recvWindow':   5000  
    }  
      
    # 参数中加时间戳：  
    timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds  
    params['timestamp'] = timestamp  
      
    # 按参数名称的字母顺序进行排序  
    params = dict(sorted(params.items()))  
      
    # 计算签名有效负载  
    payload = '&'.join([f"{k}={v}" for k,v in params.items()]) # no percent encoding here!  
      
    # 对请求进行签名  
    signature = base64.b64encode(private_key.sign(payload.encode('UTF-8')))  
    params['signature'] = signature.decode('ASCII')  
      
    # 发送请求：  
    request = {  
        'id': 'my_new_order',  
        'method': 'order.place',  
        'params': params  
    }  
      
    ws = create_connection("wss://ws-api.binance.com:443/ws-api/v3")  
    ws.send(json.dumps(request))  
    result =  ws.recv()  
    ws.close()  
      
    print(result)