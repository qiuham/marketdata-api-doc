---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints
api_type: Account
updated_at: 2026-06-28 18:49:38.654090
---

# Error Codes

* Any endpoint can return an ERROR



Sample Payload below:
    
    
    {  
        "code": -1121,  
        "msg": "Invalid symbol."  
    }  
    

  * Specific error codes and messages are defined in [Errors Codes](/docs/binance-spot-api-docs/errors).

---

# 接口错误代码

* 每个接口都有可能抛出异常，异常响应格式如下：


    
    
    {  
        "code": -1121,  
        "msg": "Invalid symbol."  
    }  
    

  * 具体的错误码及其解释在[错误代码汇总](/docs/zh-CN/binance-spot-api-docs/errors)