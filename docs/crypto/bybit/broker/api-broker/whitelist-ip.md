---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/broker/api-broker/whitelist-ip
api_type: REST
updated_at: 2026-07-23 18:54:04.490128
---

# Get Broker Whitelist IP

info

This endpoint must be queried from a whitelisted IP address.

### HTTP Request

GET`/v5/broker/whitelist/ip`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Object  
> name| string| Client name  
> endpointDomain| string| Dedicated hostname assigned exclusively to this client  
> ipList| array| Array of whitelisted IP addresses  
  
### Request Example

  * HTTP


    
    
    GET /v5/broker/whitelist/ip HTTP/1.1  
    Host: api.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "name": "CoinXXX",  
                "endpointDomain": "cabxxx0bnh.bybit-aws.com",  
                "ipList": [  
                    "13.112.01.101",  
                    "35.78.100.1"  
                ]  
            },  
            {  
                "name": "CoinXXX",  
                "endpointDomain": "vgjzztjbx91ajfj.bybit.com",  
                "ipList": [  
                    "13.112.01.101",  
                    "35.78.100.1",  
                    "35.78.100.2"  
                ]  
            }  
        ],  
        "time": 1779362854157  
    }

---

# 查詢經紀商 IP 白名單

信息

此接口必須從白名單 IP 位址發起請求。

### HTTP 請求

GET`/v5/broker/whitelist/ip`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| Object  
> name| string| 客戶名稱  
> endpointDomain| string| 分配給該客戶專用的 hostname  
> ipList| array| 白名單 IP 位址列表  
  
### 請求示例

  * HTTP


    
    
    GET /v5/broker/whitelist/ip HTTP/1.1  
    Host: api.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "name": "CoinXXX",  
                "endpointDomain": "cabxxx0bnh.bybit-aws.com",  
                "ipList": [  
                    "13.112.01.101",  
                    "35.78.100.1"  
                ]  
            },  
            {  
                "name": "CoinXXX",  
                "endpointDomain": "vgjzztjbx91ajfj.bybit.com",  
                "ipList": [  
                    "13.112.01.101",  
                    "35.78.100.1",  
                    "35.78.100.2"  
                ]  
            }  
        ],  
        "time": 1779362854157  
    }