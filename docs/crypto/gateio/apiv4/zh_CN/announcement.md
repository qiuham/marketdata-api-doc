---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN/announcement
api_type: REST
updated_at: 2026-11-22 18:56:22.289388
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
title_query | body | string | 否 | 用于查询公告文章的标题。  
page | body | string | 否 | 页码，可选，以字符串传递，例如 "1"。  
size | body | string | 否 | 每页返回的文章数量，可选，以字符串传递，例如 "5"。  
tags | body | string | 否 | 文章标签  
timer | body | string | 否 | 查询最近 N 天的公告，N 以字符串传递。例如，今天为 10 号时，传入 "10" 查询 1 号至 10 号的公告。  
cate_name | body | string | 否 | 公告分类名称。  
cate_level | body | string | 否 | 分类等级，以字符串传递："1" 或 "2"。  
sub_website_id | body | string | 否 | 分站 ID，以字符串传递："0" 为主站，"177" 为土耳其站。默认 "0"。  
pinned | body | integer | 否 | 是否展示置顶文章：1 为展示，0 为不展示。默认 1。  
update_after | body | integer | 否 | 查询此时间戳之后更新的公告文章。  
lang | body | string | 否 | 语言代码，例如 "cn"。  
filter_empty_content | body | integer | 否 | 是否排除当前语言内容为空的文章：0 为不排除，1 为排除。默认 1。  
  
####  请求体结构

AnnouncementArticleListRequest

公告文章列表查询条件

请求体结构类型 | 约束  
---|---  
AnnouncementArticleListRequest |   
  
**属性**

请求体结构名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
title_query | string | Optional |  | 用于查询公告文章的标题。  
page | string | Optional |  | 页码，可选，以字符串传递，例如 "1"。  
size | string | Optional |  | 每页返回的文章数量，可选，以字符串传递，例如 "5"。  
tags | string | Optional |  | 文章标签  
timer | string | Optional |  | 查询最近 N 天的公告，N 以字符串传递。例如，今天为 10 号时，传入 "10" 查询 1 号至 10 号的公告。  
cate_name | string | Optional |  | 公告分类名称。  
cate_level | string | Optional |  | 分类等级，以字符串传递："1" 或 "2"。  
sub_website_id | string | Optional | default: "0" | 分站 ID，以字符串传递："0" 为主站，"177" 为土耳其站。默认 "0"。  
pinned | integer | Optional | default: 1 | 是否展示置顶文章：1 为展示，0 为不展示。默认 1。  
update_after | integer | Optional |  | 查询此时间戳之后更新的公告文章。  
lang | string | Optional |  | 语言代码，例如 "cn"。  
filter_empty_content | integer | Optional | default: 1 | 是否排除当前语言内容为空的文章：0 为不排除，1 为排除。默认 1。  
  
### 返回

返回状态码 | 含义 | 描述 | 格式  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 公告文章列表响应 | AnnouncementArticleListResponse  
  
### 返回格式

状态码 **200**

AnnouncementArticleListResponse

公告文章列表响应

类型 | 约束  
---|---  
AnnouncementArticleListResponse | required: ["code","data","message","version"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer | Required |  | 业务状态码  
data | AnnouncementArticleListData | Required | required: ["list","total"] | 公告文章列表及总数  
message | string | Required |  | 响应消息  
version | string | Required |  | 响应版本  
  
**data**

AnnouncementArticleListData

公告文章列表及总数

类型 | 约束  
---|---  
AnnouncementArticleListData | required: ["list","total"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
list | array | Required |  | 公告文章列表  
total | integer | Required |  | 公告文章总数。  
  
**data / list**

公告文章列表

类型 | 约束  
---|---  
array |   
  
**data / list / items**

AnnouncementArticle

公告文章

类型 | 约束  
---|---  
AnnouncementArticle | required: ["id","title","brief","created","updated","release_time","views","author","author_id","tags","cate","is_top","cate_id","source","content_lang_list"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer | Required |  | 公告文章的 ID。  
title | string | Required |  | 文章标题  
brief | string | Required |  | 文章摘要  
created | string | Required |  | 文章创建时间，以字符串返回。  
updated | string | Required |  | 文章更新时间，以字符串返回。  
release_time | string | Required |  | 文章发布时间，以字符串返回。  
views | integer | Required |  | 浏览量  
author | string | Required |  | 作者  
author_id | integer | Required |  | 文章作者的 ID。  
tags | string | Required |  | 文章标签  
cate | string | Required |  | 文章所属分类。  
is_top | integer | Required |  | 文章的置顶标记。  
cate_id | integer | Required |  | 文章所属分类的 ID。  
source | string | Required |  | 文章来源  
content_lang_list | array | Required |  | 文章支持的语言列表，包含每种语言的代码和名称。  
  
**data / list / items / content_lang_list**

文章支持的语言列表，包含每种语言的代码和名称。

类型 | 约束  
---|---  
array |   
  
**data / list / items / content_lang_list / items**

AnnouncementArticleLanguage

公告文章语言

类型 | 约束  
---|---  
AnnouncementArticleLanguage | required: ["code","name"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | string | Required |  | 语言代码，例如 "cn"。  
name | string | Required |  | 语言名称  
  
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

AnnouncementArticleListResponse

公告文章列表响应

类型 | 约束  
---|---  
object | required: ["code","data","message","version"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | integer | Required |  | 业务状态码  
data | AnnouncementArticleListData | Required | required: ["list","total"] | 公告文章列表及总数  
message | string | Required |  | 响应消息  
version | string | Required |  | 响应版本  
  
**data**

AnnouncementArticleListData

公告文章列表及总数

类型 | 约束  
---|---  
AnnouncementArticleListData | required: ["list","total"]  
      
    
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
    
    

##  AnnouncementArticleListData

AnnouncementArticleListData

公告文章列表及总数

类型 | 约束  
---|---  
object | required: ["list","total"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
list | array | Required |  | 公告文章列表  
total | integer | Required |  | 公告文章总数。  
  
**list**

公告文章列表

类型 | 约束  
---|---  
array |   
  
**list / items**

AnnouncementArticle

公告文章

类型 | 约束  
---|---  
AnnouncementArticle | required: ["id","title","brief","created","updated","release_time","views","author","author_id","tags","cate","is_top","cate_id","source","content_lang_list"]  
      
    
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
    
    

##  AnnouncementArticleListRequest

AnnouncementArticleListRequest

公告文章列表查询条件

类型 | 约束  
---|---  
object |   
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
title_query | string | Optional |  | 用于查询公告文章的标题。  
page | string | Optional |  | 页码，可选，以字符串传递，例如 "1"。  
size | string | Optional |  | 每页返回的文章数量，可选，以字符串传递，例如 "5"。  
tags | string | Optional |  | 文章标签  
timer | string | Optional |  | 查询最近 N 天的公告，N 以字符串传递。例如，今天为 10 号时，传入 "10" 查询 1 号至 10 号的公告。  
cate_name | string | Optional |  | 公告分类名称。  
cate_level | string | Optional |  | 分类等级，以字符串传递："1" 或 "2"。  
sub_website_id | string | Optional | default: "0" | 分站 ID，以字符串传递："0" 为主站，"177" 为土耳其站。默认 "0"。  
pinned | integer | Optional | default: 1 | 是否展示置顶文章：1 为展示，0 为不展示。默认 1。  
update_after | integer | Optional |  | 查询此时间戳之后更新的公告文章。  
lang | string | Optional |  | 语言代码，例如 "cn"。  
filter_empty_content | integer | Optional | default: 1 | 是否排除当前语言内容为空的文章：0 为不排除，1 为排除。默认 1。  
      
    
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
    
    

##  AnnouncementArticle

AnnouncementArticle

公告文章

类型 | 约束  
---|---  
object | required: ["id","title","brief","created","updated","release_time","views","author","author_id","tags","cate","is_top","cate_id","source","content_lang_list"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
id | integer | Required |  | 公告文章的 ID。  
title | string | Required |  | 文章标题  
brief | string | Required |  | 文章摘要  
created | string | Required |  | 文章创建时间，以字符串返回。  
updated | string | Required |  | 文章更新时间，以字符串返回。  
release_time | string | Required |  | 文章发布时间，以字符串返回。  
views | integer | Required |  | 浏览量  
author | string | Required |  | 作者  
author_id | integer | Required |  | 文章作者的 ID。  
tags | string | Required |  | 文章标签  
cate | string | Required |  | 文章所属分类。  
is_top | integer | Required |  | 文章的置顶标记。  
cate_id | integer | Required |  | 文章所属分类的 ID。  
source | string | Required |  | 文章来源  
content_lang_list | array | Required |  | 文章支持的语言列表，包含每种语言的代码和名称。  
  
**content_lang_list**

文章支持的语言列表，包含每种语言的代码和名称。

类型 | 约束  
---|---  
array |   
  
**content_lang_list / items**

AnnouncementArticleLanguage

公告文章语言

类型 | 约束  
---|---  
AnnouncementArticleLanguage | required: ["code","name"]  
      
    
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

AnnouncementArticleLanguage

公告文章语言

类型 | 约束  
---|---  
object | required: ["code","name"]  
  
**属性**

名称 | 类型 | 必填 | 约束 | 描述  
---|---|---|---|---  
code | string | Required |  | 语言代码，例如 "cn"。  
name | string | Required |  | 语言名称  
      
    
    {
      "code": "string",
      "name": "string"
    }