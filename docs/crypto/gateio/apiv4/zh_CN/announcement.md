---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/announcement
api_type: REST
updated_at: 2026-11-13 20:57:39.969550
---

# Announcement

公告

##  查询公告文章列表

POST`/ann/list_article`

POST `/ann/list_article`

_查询公告文章列表_

分页查询公告文章，支持按标题、分类、语言和时间等条件筛选。请在 JSON 请求体中传入查询参数。page 和 size 均为可选参数，传入时请使用字符串。该接口无需 API Key。

### 参数

参数名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
body | body | AnnouncementArticleListRequest | 是 |   
» title_query | body | string | 否 | 用于查询公告文章的标题。  
» page | body | string | 否 | 页码，可选，以字符串传递，例如 "1"。  
» size | body | string | 否 | 每页返回的文章数量，可选，以字符串传递，例如 "5"。  
» tags | body | string | 否 | 文章标签  
» timer | body | string | 否 | 查询最近 N 天的公告，N 以字符串传递。例如，今天为 10 号时，传入 "10" 查询 1 号至 10 号的公告。  
» cate_name | body | string | 否 | 公告分类名称。  
» cate_level | body | string | 否 | 分类等级，以字符串传递："1" 或 "2"。  
» sub_website_id | body | string | 否 | 分站 ID，以字符串传递："0" 为主站，"177" 为土耳其站。默认 "0"。  
» pinned | body | integer | 否 | 是否展示置顶文章：1 为展示，0 为不展示。默认 1。  
» update_after | body | integer | 否 | 查询此时间戳之后更新的公告文章。  
» lang | body | string | 否 | 语言代码，例如 "cn"。  
» filter_empty_content | body | integer | 否 | 是否排除当前语言内容为空的文章：0 为不排除，1 为排除。默认 1。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 公告文章列表响应 | AnnouncementArticleListResponse  
  
### 返回格式

状态码 **200**

_AnnouncementArticleListResponse_

名称 | 类型 | 描述  
---|---|---  
» code | integer | 业务状态码  
» data | AnnouncementArticleListData | 公告文章列表及总数  
»» list | array | 公告文章列表  
»»» AnnouncementArticle | AnnouncementArticle | 公告文章  
»»»» id | integer | 公告文章的 ID。  
»»»» title | string | 文章标题  
»»»» brief | string | 文章摘要  
»»»» created | string | 文章创建时间，以字符串返回。  
»»»» updated | string | 文章更新时间，以字符串返回。  
»»»» release_time | string | 文章发布时间，以字符串返回。  
»»»» views | integer | 浏览量  
»»»» author | string | 作者  
»»»» author_id | integer | 文章作者的 ID。  
»»»» tags | string | 文章标签  
»»»» cate | string | 文章所属分类。  
»»»» is_top | integer | 文章的置顶标记。  
»»»» cate_id | integer | 文章所属分类的 ID。  
»»»» source | string | 文章来源  
»»»» content_lang_list | array | 文章支持的语言列表，包含每种语言的代码和名称。  
»»»»» AnnouncementArticleLanguage | AnnouncementArticleLanguage | 公告文章语言  
»»»»»» code | string | 语言代码，例如 "cn"。  
»»»»»» name | string | 语言名称  
»»»»» total | integer | 公告文章总数。  
»»»» message | string | 响应消息  
»»»» version | string | 响应版本  
  
该请求不需要认证 

示例代码
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/ann/list_article'
    query_param = ''
    body='{"pinned":1,"page":"1","size":"5"}'
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    curl -X POST https://api.gateio.ws/api/v4/ann/list_article \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    
    

> 请求体示例
    
    
    {
      "pinned": 1,
      "page": "1",
      "size": "5"
    }
    

> 返回示例

> 200 返回
    
    
    {
      "code": 0,
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "message": "string",
      "version": "string"
    }
    

#  模型

##  AnnouncementArticleListResponse

_AnnouncementArticleListResponse_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | integer | true | none | 业务状态码  
data | AnnouncementArticleListData | true | none | 公告文章列表及总数  
message | string | true | none | 响应消息  
version | string | true | none | 响应版本  
      
    
    {
      "code": 0,
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "message": "string",
      "version": "string"
    }
    
    

##  AnnouncementArticleListRequest

_AnnouncementArticleListRequest_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
title_query | string | false | none | 用于查询公告文章的标题。  
page | string | false | none | 页码，可选，以字符串传递，例如 "1"。  
size | string | false | none | 每页返回的文章数量，可选，以字符串传递，例如 "5"。  
tags | string | false | none | 文章标签  
timer | string | false | none | 查询最近 N 天的公告，N 以字符串传递。例如，今天为 10 号时，传入 "10" 查询 1 号至 10 号的公告。  
cate_name | string | false | none | 公告分类名称。  
cate_level | string | false | none | 分类等级，以字符串传递："1" 或 "2"。  
sub_website_id | string | false | none | 分站 ID，以字符串传递："0" 为主站，"177" 为土耳其站。默认 "0"。  
pinned | integer | false | none | 是否展示置顶文章：1 为展示，0 为不展示。默认 1。  
update_after | integer | false | none | 查询此时间戳之后更新的公告文章。  
lang | string | false | none | 语言代码，例如 "cn"。  
filter_empty_content | integer | false | none | 是否排除当前语言内容为空的文章：0 为不排除，1 为排除。默认 1。  
      
    
    {
      "title_query": "string",
      "page": "1",
      "size": "5",
      "tags": "string",
      "timer": "string",
      "cate_name": "string",
      "cate_level": "string",
      "sub_website_id": "0",
      "pinned": 1,
      "update_after": 0,
      "lang": "cn",
      "filter_empty_content": 1
    }
    
    

##  AnnouncementArticleListData

_AnnouncementArticleListData_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
list | [AnnouncementArticle] | true | none | 公告文章列表  
total | integer | true | none | 公告文章总数。  
      
    
    {
      "list": [
        {
          "id": 0,
          "title": "string",
          "brief": "string",
          "created": "string",
          "updated": "string",
          "release_time": "string",
          "views": 0,
          "author": "string",
          "author_id": 0,
          "tags": "string",
          "cate": "string",
          "is_top": 0,
          "cate_id": 0,
          "source": "string",
          "content_lang_list": []
        }
      ],
      "total": 0
    }
    
    

##  AnnouncementArticle

_AnnouncementArticle_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
id | integer | true | none | 公告文章的 ID。  
title | string | true | none | 文章标题  
brief | string | true | none | 文章摘要  
created | string | true | none | 文章创建时间，以字符串返回。  
updated | string | true | none | 文章更新时间，以字符串返回。  
release_time | string | true | none | 文章发布时间，以字符串返回。  
views | integer | true | none | 浏览量  
author | string | true | none | 作者  
author_id | integer | true | none | 文章作者的 ID。  
tags | string | true | none | 文章标签  
cate | string | true | none | 文章所属分类。  
is_top | integer | true | none | 文章的置顶标记。  
cate_id | integer | true | none | 文章所属分类的 ID。  
source | string | true | none | 文章来源  
content_lang_list | [AnnouncementArticleLanguage] | true | none | 文章支持的语言列表，包含每种语言的代码和名称。  
      
    
    {
      "id": 0,
      "title": "string",
      "brief": "string",
      "created": "string",
      "updated": "string",
      "release_time": "string",
      "views": 0,
      "author": "string",
      "author_id": 0,
      "tags": "string",
      "cate": "string",
      "is_top": 0,
      "cate_id": 0,
      "source": "string",
      "content_lang_list": [
        {
          "code": "string",
          "name": "string"
        }
      ]
    }
    
    

##  AnnouncementArticleLanguage

_AnnouncementArticleLanguage_

###  属性

属性名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
code | string | true | none | 语言代码，例如 "cn"。  
name | string | true | none | 语言名称  
      
    
    {
      "code": "string",
      "name": "string"
    }