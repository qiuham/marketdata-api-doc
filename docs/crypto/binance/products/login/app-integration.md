---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/login/app-integration
api_type: Guide
updated_at: 2026-11-18 02:00:34.696142
---

# Integrate Binance Login with your App

## Binance Oauth 2.0

Binance Oauth 2.0 provides two authorization ways, through Binance app or web page, which is
convenient to authorize the Binance account safely and quickly. it will adopt different ways
according to the situations and users' choices.

To begin, your app should identify the needed permissions (scope) firstly. Setup and register your
app with Binance Accounts, and get your client_id . For now, Binance Login(Oauth2.0), is only
provided to close ecosystem partners now. Please reach to our business team for more details.

### Process Introduction

The Binance app will be called to authorize when the user clicks to login with the Binance account
in the app. If the user does not install the Binance app supported the authorization,there would be
a prompt for the user to authorize through the browser or download the Binance app. The result would
be returned to the app after the authorization is finished.

![img](/img/binance-oauth-flow.png)

## Integrate for Android

### How to use?

#### Create a url

- First you need a url start with 'https://accounts.binance.com/oauth/authorize' to construct an
  intent.

- Add the query parameters listed on the `parameter and description` table(At the article's end).

- Eexample:  
   `https://accounts.binance.com/oauth/authorize?response_type=code&scope=user:openId,create:apikey&client_id=xxxxxxxxx&redirect_uri=https%3A%2F%2Faccounts.pexpay.com%2Fen%2Foauth-handle&state=76ea8434ceca47ada566308030ef5f5c&bundleID=com.xxx.www`

#### Create an Intent and start oauth activity

- Using the URL you created, to create an new Intent, then start the Activity:
  ```
  val uri = Uri.Builder()
      .scheme("https")
      .authority("accounts.binance.com")
      .appendPath("oauth")
      .appendPath("authorize")
      .appendQueryParameter("response_type", "code")
      .appendQueryParameter("scope", scope)
      .appendQueryParameter("redirect_uri", redirectUri)
      .appendQueryParameter("state", state)
      .appendQueryParameter("client_id", clientID)
      .build()
  val intent = Intent(Intent.ACTION_VIEW, uri)
  startActivity(intent)
  ```
  Or
  ```
  val uri = Uri.parse(
      "https://accounts.binance.com/oauth/authorize?response_type=code&scope=user:openId,create:apikey&client_id=xxxxxxxxx&redirect_uri=https%3A%2F%2Faccounts.pexpay.com%2Fen%2Foauth-handle&state=76ea8434ceca47ada566308030ef5f5c&bundleID=com.xxx.www"
  )
  val intent = Intent(Intent.ACTION_VIEW, uri)
  startActivity(intent)
  ```

#### Once user finish the oauth successfully, we will call the url you provided through `redirect_uri`

- For example, if you pass "app://yourapp.com" as `redirect_uri`

- Once user finish oauth.
  - If success:  
    We will call `app://yourapp.com?code=xxxxx&state=xxxxx` as intent uri with action:
    `Intent.ACTION_VIEW` and category: `Intent.CATEGORY_BROWSABLE`.  
    After getting the code, it will be sent to your server. Your server will then send it to the
    oauth server to get the user data and complete the authorization process.
  - If failed: We will call `app://yourapp.com?error=xxxxx&error_description=xxxxx` as intent uri
    with action: `Intent.ACTION_VIEW` and category: `Intent.CATEGORY_BROWSABLE`.  
    You can find the error and error_description on the `error and error_description` table(At the
    article's end).

- So if you want to get the result of this OAuth action, you should announce that your app can
  consume the intent, you can achieve this by adding those codes into your AndroidMainfest.xml:

  ```
  <activity
      android:exported="true"
      android:name=".YourActivity">

      <intent-filter>
          <action android:name="android.intent.action.VIEW" />

          <category android:name="android.intent.category.DEFAULT" />
          <category android:name="android.intent.category.BROWSABLE" />

          <data
              android:host="yourapp.com"
              android:scheme="app" />
      </intent-filter>

  </activity>
  ```

  Then finally get the uri on `onCreate` or `onNewIntent`:

  ```
  class YourActivity : AppCompatActivity() {

      override fun onCreate(savedInstanceState: Bundle?) {
          super.onCreate(savedInstanceState)

          val uri = intent.data
          //handle the uri here
      }

      override fun onNewIntent(intent: Intent?) {
          super.onNewIntent(intent)

          val uri = intent.data
          //handle the uri here
      }

      ......
  }
  ```

## <font color="red">Please note that, this function is based on <a herf="https://developer.android.com/training/app-links#android-app-links">Android App Links</a>. So sometimes when the user's application's AppUrls haven't finished verified, this function may not work correctly. Which means you will always be led to the website to do the OAuth.</font>

## Integrate for iOS

### How to use?

#### Create a url

- First you need a url 'https://accounts.binance.com/oauth/authorize'

- Add the query parameters listed on the parameter and description table(At the article's end).

- Eexample Scheme:  
   `https://accounts.binance.com/oauth/authorize?response_type=code&scope=user:openId,create:apikey&client_id=xxxxxxxxx&redirect_uri=oauthdemo%3A%2F%2Flogin&state=76ea8434ceca47ada566308030ef5f5c&bundleID=com.xxx.www `
- Eexample Universal link:  
   `https://accounts.binance.com/oauth/authorize?response_type=code&scope=user:openId,create:apikey&client_id=xxxxxxxxx&redirect_uri=https%3A%2F%2Faccounts.pexpay.com%2Fen%2Foauth-handle&state=76ea8434ceca47ada566308030ef5f5c&bundleID=com.xxx.www" `
- If you use scheme, you must add path, otherwise it will definitely
  fail.`redirect_uri=oauthdemo%3A%2F%2Flogin`

#### Start oauth

- Using the url you created to open binance app

  ```
  let urlString = "https://accounts.binance.com/oauth/authorize?response_type=code&scope=user:openId,create:apikey&client_id=m1smLsRw0q&redirect_uri=oauthdemo%3A%2F%2Flogin&state=76ea8434ceca47ada566308030ef5f5c"
  guard let url = URL(string: urlString) else {
     return
  }
  UIApplication.shared.open(url)
  ```

#### Get oauth result

- Once user finish the oauth successfully, we will call the url you provided through `redirect_uri`
  and get your result

  ```
  func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
      print("*****\(String(describing: URLContexts.first))*****")
  }

  *****Optional(<UIOpenURLContext: 0x283e58d60; URL: oauthdemo://login?state=76ea8434ceca47ada566308030ef5f5c&code=XP2Vp57c3lyQeqp25tTglA4QqgKxAbEk; options: <UISceneOpenURLOptions: 0x282b284c0; sourceApp: com.xxxxx.xxxx; annotation: (null); openInPlace: NO; _eventAttribution: (null)>>)*****

  oauthdemo://login?state=76ea8434ceca47ada566308030ef5f5c&code=XP2Vp57c3lyQeqp25tTglA4QqgKxAbEk is the result returned
  ```

After getting the code, it will be sent to your server. Your server will then send it to the oauth
server to get the user data and complete the authorization process.

#### Error Type

- Eexample

  ```
  *****Optional(<UIOpenURLContext: 0x283e5d2c0; URL: oauthdemo://login?error=cancelled&error_description=cancelled%20by%20user; options: <UISceneOpenURLOptions: 0x282b34e40; sourceApp: com.czzhao.binance.dev; annotation: (null); openInPlace: NO; _eventAttribution: (null)>>)*****
  ```

  You can find the error and error_description on the `error and error_description` table(At the
  article's end).

## Add On Tables

- ### error and error_description:

  | error                | description                                     |
  | -------------------- | ----------------------------------------------- |
  | cancelled            | User has cancelled the authorization manually.  |
  | readClientInfoFailed | Binance App read your app's information failed. |
  | invaildClientInfo    | You app's information is invalid.               |

- ### parameter and description:
  | parameter           | description                                                                          |
  | ------------------- | ------------------------------------------------------------------------------------ |
  | redirectUri         | The URL in your application where users will be redirected after web authorization.  |
  | scope               | List of scopes enum your application requests access to, with comma (`,`) seperated. |
  | state               | The CSRF token to protect against CSRF (cross-site request forgery) attacks.         |
  | response_type       | Always use `code`                                                                    |
  | client_id           | Binance client ID                                                                    |
  | bundleID (Optional) | Bundle ID of your app                                                                |

---

# 集成币安SDK

## Binance Open SDK

Binance Open
SDK(以下简称 SDK)提供了通过币安应用和 Web 页面两种授权的方式，方便用户安全、快捷的使用币安账户进行授权，SDK 会根据不同情况和用户的选择采用不同的方式。  
集成 SDK 需要您首先确定应用程序所需的权限范围，我们目前只提供给紧密的生态系合作伙伴。请联系
<oauth-apply@binance.com> 确认合作关系后，技术团队才会协助注册您的应用程序，然后获取 client_id。

### 流程介绍

用户在应用中点击使用币安账户登陆后，会调起币安应用进行授权操作，如果用户未安装支持授权的币安应用，会提示用户可以选择通过浏览器进行授权，或者下载币安应用后再进行授权。用户授权完成，会把授权结果返回给应用。

![img](/img/binance-oauth-flow-zh.png)

### Android 集成 SDK

#### 1. 引入 SDK

- 确保您的项目中已包含`jcenter`仓库(`project > build.gradle`)。

```groovy
repositories {
    jcenter()
}
```

- 在项目的`build.gradle`文件中添加如下依赖：(`project > module > build.gradle`)。

```groovy
dependencies {
    implementation 'com.binance.android:binance-opensdk:0.3.1'
}
```

- 在 AndroidManifest.xml 文件中配置 clientID

```xml
<application>
      <meta-data
          android:name="BINANCE_CLIENT_ID"
          android:resource="clientID"/>
</application>
```

### 2. 调用授权接口

我们提供了两种授权模式

1. 有后端服务的 App 请使用授权码模式。
2. 没有后端服务的 App 请使用 PKCE 模式。

#### 2.1. 授权码模式

```kotlin
// context必须是Activity对象
val binanceAPI = BinanceAPIFactory.createAPI(context)
val oauthParams = OAuthParams(redirectUri, scope, state)
binanceAPI.authorize(oauthParams, object : BinanceListener {
    override fun onSuccess(code: String, state: String) {
        Log.d(LOG_TAG, "code $code")
    }

    override fun onCancel() {
        Log.d(LOG_TAG, "onCancel")
    }

    override fun onError(errCode: Int) {
        Log.d(LOG_TAG, "errCode $errCode")
    }
})
```

接口参数说明

| 参数        | 说明                                                                                |
| ----------- | ----------------------------------------------------------------------------------- |
| redirectUri | 在向 Binance 注册时使用的 redirectUri，用于通过 web 授权登陆时返回接入方 app 使用。 |
| scope       | 本次进行授权所申请的权限，多个权限用","分割。                                       |
| state       | 为了防止 CSRF 攻击，请携带此参数，授权完成后，Binance 会将该字段原样返回给接入方。  |

#### 2.2. PKCE 模式

PKCE 模式提供了一套客户端验证机制，防止第三方恶意拦截授权流程，获取访问令牌，非法盗取数据。详细内容参见：https://tools.ietf.org/html/rfc7636

```kotlin
// createAPI的第一个参数必须是Activity对象
val binanceAPI = BinanceAPIFactory.createAPI(context)
val oauthParams = OAuthParams(redirectUri, scope, state)
val codeVerifier = UUID.randomUUID().toString()
val codeChallenge = generateCodeChallenge(codeVerifier)
val challengeParams = ChallengeParams(codeChallenge, "S256")
binanceAPI.authorize(oauthParams, challengeParams, object : BinanceListener {
    override fun onSuccess(code: String, state: String) {
        Log.d(LOG_TAG, "code $code")
    }

    override fun onCancel() {
        Log.d(LOG_TAG, "onCancel")
    }

    override fun onError(errCode: Int) {
        Log.d(LOG_TAG, "errCode $errCode")
    }
})
```

generateCodeChallenge:
SDK 提供了对 codeVerifier 加密的工具方法，方便开发者快速获取 codeChallenge。Java 代码可通过`BinanceKit.generateCodeChallenge(codeVerifier)`调用。

> 获取`accessToken`以及用户信息的接口参见:
> [使用授权码获取 accessToken](/products/login/web-integration#step-4-exchange-authorization-code-for-refresh-and-access-tokens-1)、[调用币安 API](/products/login/web-integration#step-5-calling-binance-apis)

接口参数说明

| 参数           | 说明                                                                                |
| -------------- | ----------------------------------------------------------------------------------- |
| redirectUri    | 在向 Binance 注册时使用的 redirectUri，用于通过 web 授权登陆时返回接入方 app 使用。 |
| scope          | 本次进行授权所申请的权限，多个权限用","分割。                                       |
| state          | 为了防止 CSRF 攻击，请携带此参数，授权完成后，Binance 会将该字段原样返回给接入方。  |
| codeVerifier   | 随机字符串，用于获取 accessToken 时校验。                                           |
| code_challenge | 对 codeVerifier 使用 SHA-256 加密后的 Base64 哈希值。                               |

### 3. 接收返回数据

如果用户通过币安 App 进行登陆授权，则会在`BinanceListener`中收到授权结果。如果用户是通过 Web 登录授权，会通过`DeepLink`的方式打开指定页面，并把授权结果返回。为了能正常接收到授权结果，需要在调用授权接口的Activity类的`onActivityResult`方法中添加如下代码

```
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    super.onActivityResult(requestCode, resultCode, data)
    binanceAPI?.handleResp(requestCode, resultCode, data)
}
```

- `BinanceListener`
  - 授权成功会回调`onSuccess`方法，`code`为授权结果，`state`为调用`authorize`接口时传递的参数`state`。
  - 用户取消授权会回调`onCancel`接口，表示授权过程被取消。
  - 授权失败会回调`onError`接口，`errCode`为错误码。

    | errCode | 原因                                   |
    | ------- | -------------------------------------- |
    | 10000   | Binance App 未安装                     |
    | 10001   | Binance App 版本不支持                 |
    | 10002   | clientId 为空                          |
    | 10003   | 参数错误                               |
    | 10004   | App 检验失败(app 信息与注册信息不一致) |

- `DeepLink`  
  如果用户是通过 Web 登录授权，授权完成后，会通过`DeepLink`的方式打开指定页面(注册时`redirectUri`对应的页面)，此时需要在该页面的`onCreate`方法和`onNewIntent`方法中处理授权结果，授权成功的`DeepLink`格式为`{redirectUri}?code=xxxxx&state=xxxxx`。示例代码：

```
class LoginActivity : AppCompatActivity() {

   override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val code = intent?.data?.getQueryParameter("code")
        val state = intent?.data?.getQueryParameter("state")
        Log.d(LOG_TAG, "code $code")
    }

   override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        val code = intent?.data?.getQueryParameter("code")
        val state = intent?.data?.getQueryParameter("state")
        Log.d(LOG_TAG, "code $code")
    }

    ......
}
```

### iOS 集成 SDK

#### 版本

- Binance iOS App: 2.17.0+
- iOS 系统: iOS10+

#### 集成

##### Cocoapods

##### 手动

1. 下载`BinanceOpenSDK.framework`动态库文件
2. 将`BinanceOpenSDK.framework`添加到你的工程文件内
3. 选择`Build Phases`选项，将`BinanceOpenSDK.framework`添加到`Embed Frameworks`

#### 使用

##### Bundle ID & App ID

首先，你需要`Binance`为您提供的基于你工程的`BundleID`所对应的`AppID`。

##### Info.plist

配置`Info.plist`必要的参数:

1. 在`LSApplicationQueriesSchemes`内添加两个参数:
   `account.binance.oauth.suppor`和`com.binance.app.binance`
2. 新增一个`String`类型参数，key 为`BinanceAppID`，value 为你自己的`AppID`

##### 接口列表

###### 验证(authorize)

我们提供了两种授权模式

1. 有后端服务的 App 请使用授权码模式。
2. 没有后端服务的 App 请使用 PKCE 模式。

两种授权模式都使用通过`authorize(with:, baseAt:, onSuccess:, onFailure:)`这个接口来发起一次`oauth`的验证请求。

```swift
public func authorize(with parameters: OAuthParameters, baseAt container: UIView, onSuccess:((String, String) -> Void)?, onFailure: ((OAuthError) -> Void)?)
```

###### OAuthParameters

`OAuthParameters`是用于封装`OAuth`请求必需的参数的结构体。

`codeChallenge`是对 codeVerifier 使用 SHA-256 加密后的 Base64 哈希值，SDK 提供了工具方法帮你计算`BinanceOpenUtils.generateCodeChallendge(codeVerifier)`。

如果你使用授权码模式，则无需传入`codeChallenge`，如果采用`PKCE`模式，则可传入`.s256(code: BinanceOpenUtils.generateCodeChallendge(codeVerifier)!)`

```swift

public struct OAuthParameters {
    public var scope: String
    public var state: String
    public var redirectURI: String
    public var codeChallenge: CodeChallenge?
}
```

| 参数          | 说明                                                                                |
| ------------- | ----------------------------------------------------------------------------------- |
| redirectUri   | 在向 Binance 注册时使用的 redirectUri，用于通过 web 授权登陆时返回接入方 app 使用。 |
| scope         | 本次进行授权所申请的权限。                                                          |
| state         | 为了防止 CSRF 攻击，请携带此参数，授权完成后，Binance 会将该字段原样返回给接入方。  |
| codeChallenge | 对 codeVerifier 使用 SHA-256 加密后的 Base64 哈希值                                 |

#### Handle Open URL

需要在`AppDelegate`中处理`openURL`:

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    return BinanceOpenSDK.shared.handle(openURL: url)
}
```

##### 状态自检

`BinanceOpenSDK`提供了`selfTest()`函数用于自我状态的检测。此函数用于检测 SDK 所必须的参数和环境，当检测失败时，会将具体的问题返回给你。如果返回值为`nil`，那么则表明检测后 SDK 当前状态是没有问题的。

具体的返回的警告是以下的枚举:

```swift
public enum Warning {
    case invalidAppID
    case invalidBundleID
    case noBinanceApp
    case oauth(OAuthWarning)
}
```

##### 多语言

`BinanceOpenSDK`目前支持两种语言模式:

1. 自动模式(默认): 自动模式 SDK 将会跟随系统语言来展示文案
2. 手动模式: 你可以为 SDK 指定一种语言

```swift

// 自动模式
BinanceOpenSDK.shared.languageMode = .automatic

// 手动模式
BinanceOpenSDK.shared.languageMode = .manual(language: .russia)

```

目前支持的语言有以下几种:

| Language           | Desc     |
| ------------------ | -------- |
| english            | 英文     |
| chinese            | 简体中文 |
| traditionalChinese | 繁体中文 |
| korean             | 韩文     |
| turkish            | 土耳其语 |
| vietnamese         | 越南语   |
| spanish            | 西班牙语 |
| russia             | 俄语     |
| portuguese         | 葡语     |
| japanese           | 日语     |
| polish             | 波兰语   |
| ukrainian          | 乌克兰语 |
| french             | 法语     |

##### 错误类型

整体看来`BinanceOpenSDK`的错误类型分为两种，一种是 SDK 内部的错误，一种是调用 Binance
App 之后，回调的错误。主要是以下的枚举:

```swift

public enum OAuthError: Error {
    case invalidBundleID
    case invalidAppID
    case invalidParameters
    case openAppFailed
    case openSafariFailed
    case fromBinanceApp(type: String, desc: String)
}
```

`fromBinanceApp`为 Binance App 返回的错误，常见的 3 种类型如下:

- cancelled: 用户手动取消验证
- readClientInfoFailed: 获取第三方 App 信息失败
- invaildClientInfo: 第三方 App 校验失败(信息与注册是不匹配)