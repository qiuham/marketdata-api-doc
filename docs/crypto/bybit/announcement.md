---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/announcement
api_type: REST
updated_at: 2026-11-13 19:21:24.066927
---

# Get Announcement

### HTTP Request

GET`/v5/announcements/index`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[locale](/docs/v5/enum#locale)| **true**|  string| Language symbol  
[type](/docs/v5/enum#announcementtype)| false| string| Announcement type  
[tag](/docs/v5/enum#announcementtag)| false| string| Announcement tag  
page| false| integer| Page number. Default: `1`  
limit| false| integer| Limit for data size per page. Default: `20`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
total| integer| Total records  
list| array| Object  
> title| string| Announcement title  
> description| string| Announcement description  
> type| Object|   
>> title| string| The title of announcement type  
>> [key](/docs/v5/enum#announcementtype)| string| The key of announcement type  
> [tags](/docs/v5/enum#announcementtag)| array<string>| The tag of announcement  
> url| string| Announcement url  
> dateTimestamp| number| Timestamp that author fills  
> startDataTimestamp| number| The start timestamp (ms) of the event, only valid when `list.type.key == "latest_activities"`  
> endDataTimestamp| number| The end timestamp (ms) of the event, only valid when `list.type.key == "latest_activities"`  
> publishTime| number| The published timestamp for the announcement  
  
* * *

### Request Example

  * HTTP
  * Python
  * Java


    
    
    GET /v5/announcements/index?locale=en-US&limit=1 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_announcement(  
        locale="en-US",  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.domain.announcement.LanguageSymbol;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var announcementInfoRequest = MarketDataRequest.builder().locale(LanguageSymbol.EN_US).build();  
    client.getAnnouncementInfo(announcementInfoRequest, System.out::println);  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "total": 735,  
            "list": [  
                {  
                    "title": "New Listing: Arbitrum (ARB) — Deposit, Trade and Stake ARB to Share a 400,000 USDT Prize Pool!",  
                    "description": "Bybit is excited to announce the listing of ARB on our trading platform!",  
                    "type": {  
                        "title": "New Listings",  
                        "key": "new_crypto"  
                    },  
                    "tags": [  
                        "Spot",  
                        "Spot Listings"  
                    ],  
                    "url": "https://announcements.bybit.com/en-US/article/new-listing-arbitrum-arb-deposit-trade-and-stake-arb-to-share-a-400-000-usdt-prize-pool--bltf662314c211a8616/",  
                    "dateTimestamp": 1679045608000,  
                    "startDateTimestamp": 1679045608000,  
                    "endDateTimestamp": 1679045608000  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1679415136117  
    }

---

# 查詢公告

### HTTP 請求

GET`/v5/announcements/index`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[locale](/docs/zh-TW/v5/enum#locale)| **true**|  string| 公告語言標識  
[type](/docs/zh-TW/v5/enum#announcementtype)| false| string| 公告類型  
[tag](/docs/zh-TW/v5/enum#announcementtag)| false| string| 公告標籤  
page| false| integer| 分頁頁碼. 默認: `1`  
limit| false| integer| 每頁數據限制. 默認: `20`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
total| integer| 可查詢公告總署  
list| array| Object  
> title| string| 公告標題  
> description| string| 公告描述  
> type| Object|   
>> title| string| 公告類型名稱，多語言  
>> [key](/docs/zh-TW/v5/enum#announcementtype)| string| 公告類型唯一鍵  
> [tags](/docs/zh-TW/v5/enum#announcementtag)| array<string>| 公告標籤  
> url| string| 公告鏈結  
> dateTimestamp| number| 作者填寫的時間戳 (毫秒)  
> startDataTimestamp| number| 事件開始時間戳 (毫秒), 僅當`list.type.key == "latest_activities"`時有效  
> endDataTimestamp| number| 事件結束時間戳 (毫秒), 僅當`list.type.key == "latest_activities"`時有效  
> publishTime| number| 公告發出時間戳 (毫秒)  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Java


    
    
    GET /v5/announcements/index?locale=en-US&limit=1 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_announcement(  
        locale="en-US",  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.domain.announcement.LanguageSymbol;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var announcementInfoRequest = MarketDataRequest.builder().locale(LanguageSymbol.EN_US).build();  
    client.getAnnouncementInfo(announcementInfoRequest, System.out::println);  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "total": 569,  
            "list": [  
                {  
                    "title": "Arbitrum(ARB) 即將上線：儲值 250 ARB 即賺 25 USDT，更可解鎖 150,000 USDT 獎池！",  
                    "description": "好消息！ ARB 即將上線 Bybit 交易平台！",  
                    "type": {  
                        "title": "新幣上線",  
                        "key": "new_crypto"  
                    },  
                    "tags": [  
                        "Spot",  
                        "Spot Listings"  
                    ],  
                    "url": "https://announcements.bybit.com/zh-TW/article/new-listing-arbitrum-arb-deposit-250-arb-to-earn-25-usdt-share-a-150-000-usdt-prize-pool--bltf662314c211a8616/",  
                    "dateTimestamp": 1679045608000,  
                    "startDateTimestamp": 1679564008000,  
                    "endDateTimestamp": 1680255208000  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1679416172335  
    }