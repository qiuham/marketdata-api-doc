---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/capital/deposite-history
api_type: REST
updated_at: 2026-06-28 18:54:22.394085
---

# Fetch deposit address list with network(USER_DATA)

## API Description[​](/docs/wallet/capital/fetch-deposit-address-list-with-network#api-description "Direct link to API Description")

Fetch deposit address list with network.

## HTTP Request[​](/docs/wallet/capital/fetch-deposit-address-list-with-network#http-request "Direct link to HTTP Request")

GET `/sapi/v1/capital/deposit/address/list`

## Request Weight(IP)[​](/docs/wallet/capital/fetch-deposit-address-list-with-network#request-weightip "Direct link to Request Weight\(IP\)")

**10**

## Request Parameters[​](/docs/wallet/capital/fetch-deposit-address-list-with-network#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
coin| STRING| YES| `coin` refers to the parent network address format that the address is using  
network| STRING| NO|   
timestamp| LONG| YES|   
  
>   * If network is not send, return with default network of the coin.
>   * You can get network and isDefault in networkList in the response of `Get /sapi/v1/capital/config/getall`.
> 


## Response Example[​](/docs/wallet/capital/fetch-deposit-address-list-with-network#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "coin": "ETH",                                               // coin here means network address space, ETH for all EVM-like network  
            "address": "0xD316E95Fd9E8E237Cb11f8200Babbc5D8D177BA4",  
            "tag": "",  
            "isDefault": 0  
        },  
        {  
            "coin": "ETH",  
            "address": "0xD316E95Fd9E8E237Cb11f8200Babbc5D8D177BA4",  
            "tag": "",  
            "isDefault": 0  
        },  
        {  
            "coin": "ETH",  
            "address": "0x00003ada75e7da97ba0db2fcde72131f712455e2",  
            "tag": "",  
            "isDefault": 1                                               // 'isDefault' is 1 means the address is default, same as shown in the app.  
        }  
    ]

---

# 查询充值地址列表(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/capital/fetch-deposit-address-list-with-network#接口描述 "接口描述的直接链接")

根据网络币种或币种获取充值地址列表

## HTTP请求[​](/docs/zh-CN/wallet/capital/fetch-deposit-address-list-with-network#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/capital/deposit/address/list`

## 请求权重(IP)[​](/docs/zh-CN/wallet/capital/fetch-deposit-address-list-with-network#请求权重ip "请求权重\(IP\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/wallet/capital/fetch-deposit-address-list-with-network#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
coin| STRING| YES| `coin`是网络的地址空间名称  
network| STRING| NO| 网络  
timestamp| LONG| YES| 时间戳  
  
>   * 如果没传网络，会返回网络对应的默认网络。
>   * 可以通过后面的接口，来获取网络和 isDefault 字段，在返回的响应里`Get /sapi/v1/capital/config/getall`.
> 


## 响应示例[​](/docs/zh-CN/wallet/capital/fetch-deposit-address-list-with-network#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "coin": "ETH", //这里 coin 实际上指 network 的地址空间, 类 ETH 网络都使用 ETH 的地址  
            "address": "0xD316E95Fd9E8E237Cb11f8200Babbc5D8D177BA4",  
            "tag": "",  
            "isDefault": 0  
        },  
        {  
            "coin": "ETH",  
            "address": "0xD316E95Fd9E8E237Cb11f8200Babbc5D8D177BA4",  
            "tag": "",  
            "isDefault": 0  
        },  
        {  
            "coin": "ETH",  
            "address": "0x00003ada75e7da97ba0db2fcde72131f712455e2",  
            "tag": "",  
            "isDefault": 1  
        }  
    ]