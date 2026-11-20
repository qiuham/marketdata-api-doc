---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/institution/connection-limit
api_type: REST
updated_at: 2026-11-20 18:52:12.936926
---

# Get Institution Connection Limit

> API rate limit: 1 req per minute

info

This endpoint must be requested with a master account API key.

### HTTP Request

GET`/v5/ins/connection-limit`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Object  
> host| string| Host  
> endpointDomain| string| Dedicated endpoint domain  
> spot| object| Spot connection limits  
>> json| object| JSON WebSocket connection limits  
>>> max| integer| Maximum number of connections  
>>> current| integer| Current number of connections  
>> sbe| object| SBE connection limits  
>>> max| integer| Maximum number of connections  
>>> current| integer| Current number of connections  
> derivative| object| Derivatives connection limits  
>> json| object| JSON WebSocket connection limits  
>>> max| integer| Maximum number of connections  
>>> current| integer| Current number of connections  
>> sbe| object| SBE connection limits  
>>> max| integer| Maximum number of connections  
>>> current| integer| Current number of connections  
  
### Request Example

  * HTTP


    
    
    GET /v5/ins/connection-limit HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1794457439807  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "host": "SELF_USE",  
                "endpointDomain": "8ipum71s9p2t5m25.bybit-ws-tkyo.com",  
                "spot": {  
                    "json": {  
                        "max": 1500,  
                        "current": 0  
                    },  
                    "sbe": {  
                        "max": 1500,  
                        "current": 0  
                    }  
                },  
                "derivative": {  
                    "json": {  
                        "max": 3000,  
                        "current": 0  
                    },  
                    "sbe": {  
                        "max": 3000,  
                        "current": 0  
                    }  
                }  
            },  
            {  
                "host": "SELF_USE",  
                "endpointDomain": "primary-nggxtax0ux4uwvfu.bybit-ws-tkyo.com",  
                "spot": {  
                    "json": {  
                        "max": 1500,  
                        "current": 5  
                    },  
                    "sbe": {  
                        "max": 1500,  
                        "current": 7  
                    }  
                },  
                "derivative": {  
                    "json": {  
                        "max": 3000,  
                        "current": 14  
                    },  
                    "sbe": {  
                        "max": 3000,  
                        "current": 15  
                    }  
                }  
            },  
            {  
                "host": "SELF_USE",  
                "endpointDomain": "vgx0s429h1x03zkn.bybit-tkyo.com",  
                "spot": {  
                    "json": {  
                        "max": 1500,  
                        "current": 0  
                    },  
                    "sbe": {  
                        "max": 1500,  
                        "current": 0  
                    }  
                },  
                "derivative": {  
                    "json": {  
                        "max": 3000,  
                        "current": 0  
                    },  
                    "sbe": {  
                        "max": 3000,  
                        "current": 0  
                    }  
                }  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1794457439807  
    }

---

# 查詢機構連線限制

> API 限頻：每分鐘 1 次請求

信息

此接口必須使用主帳戶 API key 請求。

### HTTP 請求

GET`/v5/ins/connection-limit`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| Object  
> host| string| 端點  
> endpointDomain| string| 專用端點域名  
> spot| object| 現貨連線限制  
>> json| object| JSON WebSocket 連線限制  
>>> max| integer| 最大連線數  
>>> current| integer| 目前連線數  
>> sbe| object| SBE 連線限制  
>>> max| integer| 最大連線數  
>>> current| integer| 目前連線數  
> derivative| object| 衍生品連線限制  
>> json| object| JSON WebSocket 連線限制  
>>> max| integer| 最大連線數  
>>> current| integer| 目前連線數  
>> sbe| object| SBE 連線限制  
>>> max| integer| 最大連線數  
>>> current| integer| 目前連線數  
  
### 請求範例

  * HTTP


    
    
    GET /v5/ins/connection-limit HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1794457439807  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### 響應範例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "host": "SELF_USE",  
                "endpointDomain": "8ipum71s9p2t5m25.bybit-ws-tkyo.com",  
                "spot": {  
                    "json": {  
                        "max": 1500,  
                        "current": 0  
                    },  
                    "sbe": {  
                        "max": 1500,  
                        "current": 0  
                    }  
                },  
                "derivative": {  
                    "json": {  
                        "max": 3000,  
                        "current": 0  
                    },  
                    "sbe": {  
                        "max": 3000,  
                        "current": 0  
                    }  
                }  
            },  
            {  
                "host": "SELF_USE",  
                "endpointDomain": "primary-nggxtax0ux4uwvfu.bybit-ws-tkyo.com",  
                "spot": {  
                    "json": {  
                        "max": 1500,  
                        "current": 5  
                    },  
                    "sbe": {  
                        "max": 1500,  
                        "current": 7  
                    }  
                },  
                "derivative": {  
                    "json": {  
                        "max": 3000,  
                        "current": 14  
                    },  
                    "sbe": {  
                        "max": 3000,  
                        "current": 15  
                    }  
                }  
            },  
            {  
                "host": "SELF_USE",  
                "endpointDomain": "vgx0s429h1x03zkn.bybit-tkyo.com",  
                "spot": {  
                    "json": {  
                        "max": 1500,  
                        "current": 0  
                    },  
                    "sbe": {  
                        "max": 1500,  
                        "current": 0  
                    }  
                },  
                "derivative": {  
                    "json": {  
                        "max": 3000,  
                        "current": 0  
                    },  
                    "sbe": {  
                        "max": 3000,  
                        "current": 0  
                    }  
                }  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1794457439807  
    }