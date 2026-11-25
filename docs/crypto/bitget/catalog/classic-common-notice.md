---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-common-notice
api_type: REST
updated_at: 2026-11-25 19:02:30.870924
---

# Classic Notice API

Public notice endpoints — query platform announcements.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/public/annoucements` — Query Announcements

## Query Announcements

`GET /api/v2/public/annoucements`

Frequency limit: 20 times/1s (IP)

Search for announcements within one month

Description of the announcement sub-type：

The announcement sub-type matches the announcement type.

annType=`latest_news`

    - `announcements` Latest announcement

    - `news` Bitget news

annType=`coin_listings`

    - `spot`

    - `futures`

    - `margin`

    - `copy_trading`

annType=`product_updates`

    - `spot`

    - `futures`

    - `margin`

    - `copy_trading`

annType=`security`

    - `security_information`

annType=`api_trading`

    - `api_announcement`

annType=`symbol_delisting`

    - `trading_pair_delisting`

annType=`maintenance_system_updates`

    - `asset_maintenance`

    - `system_updates`

    - `spot_maintenance`

    - `futures_maintenance`

Operation ID: `classicCommonNoticeGetAllNotices`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| annType | query | string |  | Announcement type<br><br>`latest_news`: Latest events<br><br>`coin_listings`: New coin listings<br><br>`product_updates`: Product update<br><br>`security`: Security<br><br>`api_trading`: Api trading<br><br>`maintenance_system_updates`: maintenance/system upgrades<br><br>`symbol_delisting`: Delisting information |
| startTime | query | string |  | Start time of the query, Unix millisecond timestamp, e.g. 1690196141868<br><br>Search by announcement time |
| endTime | query | string |  | End time of the query, Unix millisecond timestamp, e.g. 1690196141868<br><br>Search by announcement time |
| cursor | query | string |  | Cursor ID <br><br>It is not required for the first call. For subsequent calls, pass the last annId in the previous response. |
| limit | query | string |  | Number of entries per page <br><br> By default, it is 10 entries, and the maximum is 10 entries. |
| language | query | string | 是 | language type<br><br>zh_CN: Chinese<br><br>en_US: English<br><br>Returns English if the language chosen is not supported |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.annId | string |  | Announcement ID |
| data.annTitle | string |  | Announcement title |
| data.annDesc | string |  | Announcement description (This field is deprecated) |
| data.language | string |  | language type |
| data.annUrl | string |  | Announcement URL |
| data.annType | string |  | Announcement type<br><br>`latest_news`: Latest events<br><br>`coin_listings`: New coin listings<br><br>`product_updates`: Product update<br><br>`security`: Security<br><br>`api_trading`: Api trading<br><br>`maintenance_system_updates`: maintenance/system upgrades<br><br>`symbol_delisting`: Delisting information |
| data.annSubType | string |  | Announcement sub-type |
| data.cTime | string |  | Announcement release time<br><br>In the format of Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1688008631614,
  "data": [
    {
      "annId": "1",
      "annTitle": "test0629",
      "annDesc": "Latest announcement",
      "annType": "maintenance_system_updates",
      "annSubType": "asset_maintenance",
      "cTime": "1688008040000",
      "language": "zh_CN",
      "annUrl": "https://www.bitget.com/zh_CN/support/articles/23685"
    }
  ]
}
```


---

公共公告接口 —— 查询平台公告。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/public/annoucements` — 查询公告

## 查询公告

`GET /api/v2/public/annoucements`

限速规则 20次/1s (IP)

查询一个月内的公告

公告子类型说明：

公告子类型与公告类型对应关系如下。

annType=`latest_news`

    - `announcements` 最新公告

    - `news` Bitget资讯

annType=`coin_listings`

    - `spot`

    - `futures`

    - `margin`

    - `copy_trading`

annType=`product_updates`

    - `spot`

    - `futures`

    - `margin`

    - `copy_trading`

annType=`security`

    - `security_information`

annType=`api_trading`

    - `api_announcement`

annType=`symbol_delisting`

    - `trading_pair_delisting`

annType=`maintenance_system_updates`

    - `asset_maintenance`

    - `system_updates`

    - `spot_maintenance`

    - `futures_maintenance`

Operation ID: `classicCommonNoticeGetAllNotices`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| annType | query | string |  | 公告类型<br><br>`latest_news`: 最新动态<br><br>`coin_listings`: 新币上线<br><br>`product_updates`: 产品更新<br><br>`security`: 安全<br><br>`api_trading`: API交易<br><br>`maintenance_system_updates`: 维护/系统升级<br><br>`symbol_delisting`: 下架信息 |
| startTime | query | string |  | 查询起始时间，Unix毫秒时间戳，例如1690196141868<br><br>按公告时间查询 |
| endTime | query | string |  | 查询结束时间，Unix毫秒时间戳，例如1690196141868<br><br>按公告时间查询 |
| cursor | query | string |  | 游标ID<br><br>首次调用不填。后续调用传入上一次响应中最后一条的annId。 |
| limit | query | string |  | 每页条数<br><br>默认10条，最大10条。 |
| language | query | string | 是 | 语言类型<br><br>zh_CN: 中文<br><br>en_US: 英文<br><br>若所选语言不支持，则返回英文 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.annId | string |  | 公告ID |
| data.annTitle | string |  | 公告标题 |
| data.annDesc | string |  | 公告描述（该字段已废弃） |
| data.language | string |  | 语言类型 |
| data.annUrl | string |  | 公告链接 |
| data.annType | string |  | 公告类型<br><br>`latest_news`: 最新动态<br><br>`coin_listings`: 新币上线<br><br>`product_updates`: 产品更新<br><br>`security`: 安全<br><br>`api_trading`: API交易<br><br>`maintenance_system_updates`: 维护/系统升级<br><br>`symbol_delisting`: 下架信息 |
| data.annSubType | string |  | 公告子类型 |
| data.cTime | string |  | 公告发布时间<br><br>Unix毫秒时间戳格式 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1688008631614,
  "data": [
    {
      "annId": "1",
      "annTitle": "test0629",
      "annDesc": "Latest announcement",
      "annType": "maintenance_system_updates",
      "annSubType": "asset_maintenance",
      "cTime": "1688008040000",
      "language": "zh_CN",
      "annUrl": "https://www.bitget.com/zh_CN/support/articles/23685"
    }
  ]
}
```