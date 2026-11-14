---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/upgrade-unified-account
api_type: Account
updated_at: 2026-11-13 19:20:57.978979
---

# Upgrade to Unified Account Pro

Upgrade Guidance

Check your current account status by calling this [Get Account Info](/docs/v5/account/account-info)

  * if unifiedMarginStatus=5, then it is [UTA2.0](/docs/v5/acct-mode#uta-20), you can call below upgrade endpoint to [UTA2.0](/docs/v5/acct-mode#uta-20) Pro. Check [Get Account Info](/docs/v5/account/account-info) after a while and if unifiedMarginStatus=6, then the account has successfully upgraded to [UTA2.0](/docs/v5/acct-mode#uta-20) Pro.
  * When the user is a master account, the current user is allowed to upgrade to UTA PRO if they are a VIP or PRO level user.
  * When the user is a sub-account, only parent accounts with VIP or PRO level are allowed to upgrade to UTA PRO.



info

please note belows:

  1. Please avoid upgrading during these period:

|   
---|---  
every hour| 50th minute to 5th minute of next hour  
  
  2. Upgrading from UTA PUBLIC to UTA PRO is prohibited daily between **07:55 and 08:05 UTC+0**  
  

  3. Please ensure: there is no open orders when upgrade from [UTA2.0](/docs/v5/acct-mode#uta-20) to [UTA2.0](/docs/v5/acct-mode#uta-20) Pro  
  

  4. During the account upgrade process, the data of **Rest API/Websocket stream** may be inaccurate due to the fact that the account-related asset data is in the processing state. It is recommended to query and use it after the upgrade is completed.



### HTTP Request

POST`/v5/account/upgrade-to-uta`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
unifiedUpdateStatus| string| Upgrade status. `FAIL`,`PROCESS`,`SUCCESS`  
unifiedUpdateMsg| Object| If `PROCESS`,`SUCCESS`, it returns `null`  
> msg| array| Error message array. Only `FAIL` will have this field  
[](/docs/api-explorer/v5/account/upgrade-unified-account)

* * *

### Request Example

  * HTTP
  * Python
  * GO
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/account/upgrade-to-uta HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672125123533  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {}  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.upgrade_to_unified_trading_account())  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("YOUR_API_KEY", "YOUR_API_SECRET")  
    client.NewUtaBybitServiceNoParams().UpgradeToUTA(context.Background())  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.account.request.AccountDataRequest;  
    import com.bybit.api.client.domain.account.AccountType;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newAccountRestClient();  
    System.out.println(client.upgradeAccountToUTA());  
    
    
    
    using bybit.net.api;  
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models;  
    BybitAccountService accountService = new(apiKey: "xxxxxx", apiSecret: "xxxxx");  
    Console.WriteLine(await accountService.UpgradeAccount());  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .upgradeToUnifiedAccount()  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "unifiedUpdateStatus": "FAIL",  
            "unifiedUpdateMsg": {  
                "msg": [  
                    "Update account failed. You have outstanding liabilities in your Spot account.",  
                    "Update account failed. Please close the usdc perpetual positions in USDC Account.",  
                    "unable to upgrade, please cancel the usdt perpetual open orders in USDT account.",  
                    "unable to upgrade, please close the usdt perpetual positions in USDT account."  
                ]  
        }  
    },  
        "retExtInfo": {},  
        "time": 1672125124195  
    }

---

# 升級到UTA PRO

升級引導

通過調用[查詢賬戶配置](/docs/zh-TW/v5/account/account-info)接口來確認當前的帳戶型態

  * 如果unifiedMarginStatus=5, 則表示帳戶是[統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620), 您可以調用升級接口升級到[統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620) Pro. 調用[查詢賬戶配置](/docs/zh-TW/v5/account/account-info)接口, 如果unifiedMarginStatus=6, 則表示帳戶已經成功升級至[統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620) Pro.
  * 當用戶為母帳戶時，當前用戶是 VIP 或 PRO 等級的用戶時，允許升級到 UTA PRO.
  * 當用戶為子帳戶時，僅允許母帳戶為 VIP 或 PRO 等級的用戶升級到 UTA PRO.



信息

您現在可以持倉完成升級了，但請注意以下事項：

  1. 升級請避開以下時段:

|   
---|---  
每個小時| 當前時間在小時整點的前10分鐘及後5分鐘內  
  
  2. UTA PUBLIC 升級 UTA PRO 每天 UTC+0 **07:55～08:05** 禁止升級  
  

  3. 當從統一帳戶2.0升級到[統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620) Pro時, 確保沒有任何掛單  
  

  4. 帳戶升級過程中，可能會由於帳戶相關資產數據處於處理狀態中導致**查詢/推送** 的數據不準確，建議在完成升級後，再查詢和使用。



### HTTP 請求

POST`/v5/account/upgrade-to-uta`

### 請求參數

無

### 響應參數

Parameter| Type| Comments  
---|---|---  
unifiedUpdateStatus| string| 用戶賬戶的升級狀態. `PROCESS`: 處理中, `FAIL`: 失敗, `SUCCESS`: 成功  
unifiedUpdateMsg| Object| 若是`PROCESS`,`SUCCESS`，則返回`null`  
msg| array| 錯誤原因列表. 只有`FAIL`時，才會有`msg`這個字段  
[](/docs/zh-TW/api-explorer/v5/account/upgrade-unified-account)

* * *

### 請求示例

  * HTTP
  * Python
  * GO
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/account/upgrade-to-uta HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672125123533  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {}  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.upgrade_to_unified_trading_account())  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("YOUR_API_KEY", "YOUR_API_SECRET")  
    client.NewUtaBybitServiceNoParams().UpgradeToUTA(context.Background())  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.account.request.AccountDataRequest;  
    import com.bybit.api.client.domain.account.AccountType;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newAccountRestClient();  
    System.out.println(client.upgradeAccountToUTA());  
    
    
    
    using bybit.net.api;  
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models;  
    BybitAccountService accountService = new(apiKey: "xxxxxx", apiSecret: "xxxxx");  
    Console.WriteLine(await accountService.UpgradeAccount());  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .upgradeToUnifiedAccount()  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "unifiedUpdateStatus": "FAIL",  
            "unifiedUpdateMsg": {  
                "msg": [  
                    "Update account failed. You have outstanding liabilities in your Spot account.",  
                    "Update account failed. Please close the usdc perpetual positions in USDC Account.",  
                    "unable to upgrade, please cancel the usdt perpetual open orders in USDT account.",  
                    "unable to upgrade, please close the usdt perpetual positions in USDT account."  
                ]  
            }  
        },  
        "retExtInfo": {},  
        "time": 1672125124195  
    }