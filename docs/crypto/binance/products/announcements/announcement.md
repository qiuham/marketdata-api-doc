---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/announcements/announcement
api_type: Guide
updated_at: 2026-11-24 18:35:16.763049
---

# Announcements

- When Binance publishes announcements in English (language code: `en`), subscribed users will
  receive push notifications.

## Topic

- `com_announcement_en`

## Response Content

- Due to the length of the announcement, the example uses `...` to indicate omitted parts.

#### Full Response Example

```json
{
  "type": "DATA",
  "topic": "com_announcement_en",
  "data": "{\"catalogId\":161,\"catalogName\":\"Delisting\",\"publishDate\":1753257631403,\"title\":\"Notice of...\",\"body\":\"This is...\",\"disclaimer\":\"Trade on-the-go...\"}"
}
```

#### Announcement Content Description

- The detailed announcement content is contained in the `data` field. After unescaping the string,
  the structure is as follows:

```javascript
{
    "catalogId": 161,                     --Catalog ID
    "catalogName": "Delisting",           --Catalog Name
    "publishDate": 1753257631403,         --Publish timestamp (milliseconds)
    "title": "Notice of...",              --Announcement title
    "body": "This is...",                 --Announcement body
    "disclaimer": "Trade on-the-go..."    --Disclaimer
}
```

---

# 公告

- 当 Binance 发布英文公告（语言代码：`en`）时，系统会向已订阅的用户推送公告信息。

## 主题

- `com_announcement_en`

## 返回内容

- 例子中由于公告内容较长，用`...`代表省略的内容。

#### 返回示例

```json
{
  "type": "DATA",
  "topic": "com_announcement_en",
  "data": "{\"catalogId\":161,\"catalogName\":\"Delisting\",\"publishDate\":1753257631403,\"title\":\"Notice of...\",\"body\":\"This is...\",\"disclaimer\":\"Trade on-the-go...\"}"
}
```

#### 公告内容说明

- 公告具体内容包含在 `data` 字段中，去除字符串转义后，结构如下：

```javascript
{
    "catalogId": 161,                     --栏目ID
    "catalogName": "Delisting",           --栏目名称
    "publishDate": 1753257631403,         --发布时间戳
    "title": "Notice of...",              --公告标题
    "body": "This is...",                 --公告内容
    "disclaimer": "Trade on-the-go..."    --免责申明
}
```