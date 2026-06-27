---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/spot-grid/validate-input
api_type: REST
updated_at: 2026-05-27 19:15:56.432283
---

# Application Process

## 1\. Information Submission

Submit the following information to Bybit Business via this Email: `broker_program@bybit.com`:

  * **Bybit UID** : Used to log in to the OAuth management backend.
  * **OpenAPI Whitelist IP** : Only applicable to OpenAPI; the OAuth management backend has no IP restrictions.



* * *

## 2\. Merchant Initialization

  1. **Log in to Bybit** using the corresponding UID.
  2. **Access the OAuth Admin Portal** :  
Visit <https://www.bybit.com/app/user/oauth-admin>
     * Configure **Application Name** , **Email** , upload **logo** , etc.  
![](/docs/assets/images/oauth-redirect-url-c4a7907e15a702366f747de41cc92c00.jpg)
  3. **Core Parameter`redirect_uri`**:
     * Multiple callback addresses can be configured.
     * The `redirect_uri` passed when invoking the page must be configured in the management backend.
     * If the passed value does not match the configuration, it defaults to the first address.
  4. **After Successful Application** :
     * You will receive `client_id` and `client_secret`.
     * **Important** : Securely store this information and do not share it with others.



* * *

## API Integration

### 1\. Construct Authorization Page
    
    
    https://www.bybit.com/en/oauth?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope=openapi&state={state}  
    

Parameter| Description  
---|---  
`client_id`| Obtained after merchant initialization.  
`response_type`| Fixed value: `code`.  
`scope`| Pass `openapi`; other values require confirmation with Bybit.  
`state`| Random string.  
`redirect_uri`| The address to redirect to after user authorization; must be configured in the management backend.  
  
* * *

### 2\. Authorization Success Callback

After the user confirms authorization, the page redirects (301) to `redirect_uri` with the parameter `code`.  
**Example** :  
If `redirect_uri = https://www.example.com/callback`, the callback URL will be: 
    
    
    https://www.example.com/callback/?response_type=code&code=sSn87036PCFub1g0FGigexSjT&scope=openapi&state=1234abc  
    

Parameter| Description  
---|---  
`code`| Core parameter; used by the merchant backend to obtain `access_token`.  
  
* * *

### 3\. Obtain Access Token

  * **URL** : `https://api2.bybit.com/oauth/v1/public/access_token`
  * **Method** : `POST`



#### Request Example
    
    
    curl -v -X POST {url} \  
      -H 'Content-Type: application/x-www-form-urlencoded' \  
      -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \  
      -d 'client_id={client_id}' \  
      -d 'client_secret={client_secret}' \  
      -d 'code={code}'    # Note: Code can only be used once.  
    

#### Response Example
    
    
    {  
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjcwODM5NDEsIkNsaWVudElEIjoiQThmMzNFeEVTeEhjIiwiR3JhbnRNZW1iZXJJRCI6MTA2MzEwNzQxLCJBcHByb3ZlZFNjb3BlIjpbIm9wZW5hcGkiXSwiTm9uY2UiOiJPNmZ0QkdTYVdEIn0.Vq46cxPIzKmWz5fFwU4fQuF-IDqFJDOIelNLnH8r2Oo",  
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Njk1ODk1NDEsIkNsaWVudElEIjoiQThmMzNFeEVTeEhjIiwiR3JhbnRNZW1iZXJJRCI6MTA2MzEwNzQxLCJBcHByb3ZlZFNjb3BlIjpbIm9wZW5hcGkiXSwiTm9uY2UiOiIwaVZMWVY3Z1pGIn0.ByGH8d5XtSQnkbxeyiXd56iJUTddBWjqFK8_EcAw48w",  
        "token_type": "bearer",  
        "expires_in": 86400,  
        "refresh_token_expires_in": 2592000  
    }  
    

* * *

### 4\. Obtain OpenAPI

  * **URL** : `https://api2.bybit.com/oauth/v1/resource/restrict/openapi`
  * **Method** : `GET`
  * **Authorization** : Include the `Authorization` header formatted as `"Bearer {access_token}"`.  
**Example** : If `access_token = "12345"`, then `Authorization = "Bearer 12345"`.



#### Request Example
    
    
    curl {url} \  
      -H "Authorization: Bearer {access_token}"  
    

#### Response Example
    
    
    {  
      "ret_code": 0,  
      "ret_msg": "success",  
      "result": {  
        "api_key": "xxxxxxx",  
        "api_secret": "xxxxx"  
      }  
    }  
    

* * *

### Notes

  * The `code` parameter from the authorization callback is single-use and expires quickly.
  * Store `client_secret` and `api_secret` securely and never expose them publicly.

---

# 申請流程

## 1\. 信息提交

通过邮箱（[broker_program@bybit.com](mailto:broker_program@bybit.com)）向 Bybit 商務提交以下信息：

  * **Bybit UID**  
用於登陸 OAuth 管理後台

  * **OpenAPI 白名單 IP**  
僅作用於 OpenAPI（OAuth 管理後台沒有 IP 限制）




* * *

## 2\. 商戶初始化

  1. **登陸 Bybit**  
使用對應的 UID 登陸 Bybit 賬戶

  2. **訪問管理後台**  
打開連結：<https://www.bybit.com/app/user/oauth-admin>

     * 設定 Application Name
     * 設定 Email
     * 上傳 Logo
     * 其他相關操作  
![](/docs/zh-TW/assets/images/oauth-redirect-url-c4a7907e15a702366f747de41cc92c00.jpg)
  3. **核心參數配置**  
**redirect_uri** ：

     * 可設定多個回調地址
     * 喚起頁面傳入的 redirect_uri 必須在管理後台配置
     * 如傳入與配置不匹配，默認跳轉到第一個地址
  4. **獲取憑證**

     * 申請成功後，會收到 client_id 和 client_secret
     * **重要** ：請務必妥善保存此信息，不要對他人展示



* * *

## 接口調試

### 1\. 拼接授權頁面
    
    
    https://www.bybit.com/en/oauth/en/oauth?  
    client_id={client_id}&  
    response_type=code&  
    redirect_uri={redirect_uri}&  
    scope=openapi&  
    state={state}  
    

參數| 說明| 備註  
---|---|---  
`client_id`| 商戶身份標識| 商戶初始化完成後獲得  
`response_type`| 響應類型| 固定值：`code`  
`scope`| 權限範圍| 傳 `openapi`（其他值需與 Bybit 確認）  
`state`| 狀態參數| 隨機字符串，防 CSRF 攻擊  
`redirect_uri`| 回調地址| 必須在管理後台配置  
  
* * *

### 2\. 授權成功回調

用戶確認授權後，頁面將會 301 重定向至 redirect_uri 並攜帶參數 code

**示例** ：
    
    
    # 假設 redirect_uri = https://www.example.com/callback  
    # 回調後的 URL：  
    https://www.example.com/callback/?  
    response_type=code&  
    code=sSn87036PCFub1g0FGigexSjT&  
    scope=openapi&  
    state=1234abc  
    

參數| 說明| 用途  
---|---|---  
`code`| 授權碼| 核心參數，用於獲取 access_token  
  
* * *

### 3\. 獲取 access_token

**接口信息** ：

  * **URL** : <https://api2.bybit.com/oauth/v1/public/access_token>
  * **方法** : POST



**請求示例** ：
    
    
    curl -v -X POST {url} \  
      -H 'Content-Type: application/x-www-form-urlencoded' \  
      -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \  
      -d 'client_id={client_id}' \  
      -d 'client_secret={client_secret}' \  
      -d 'code={code}'    # 注意：code 只能使用 1 次  
    

**響應示例** ：
    
    
    {  
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",  
      "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",  
      "token_type": "bearer",  
      "expires_in": 86400,  
      "refresh_token_expires_in": 2592000  
    }  
    

* * *

### 4\. 獲取 OpenAPI

**接口信息** ：

  * **URL** : <https://api2.bybit.com/oauth/v1/resource/restrict/openapi>
  * **方法** : GET
  * **認證** : 需要在請求頭中攜帶 Authorization 信息  
格式：`Bearer {access_token}`  
示例：`Authorization: Bearer 12345`



#### 請求示例
    
    
    curl {url} \  
      -H "Authorization: Bearer {access_token}"  
    

#### 響應示例
    
    
    {  
      "ret_code": 0,  
      "ret_msg": "success",  
      "result": {  
        "api_key": "xxxxxxx",  
        "api_secret": "xxxxx"  
      }  
    }  
    

* * *

### 注意事項

  1. **安全存儲**  
client_secret 和 api_secret 需安全存儲，切勿泄露

  2. **Code 使用限制**  
授權碼（code）為一次性使用，请在有效時間内使用

  3. **參數配置驗證**  
確保所有參數（特別是 redirect_uri）已在管理後台正確配置