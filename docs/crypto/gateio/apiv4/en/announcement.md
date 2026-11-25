---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/announcement
api_type: REST
updated_at: 2026-11-25 18:56:59.418275
---

# Announcement

Announcements

##  List announcement articles

POST`/ann/list_article`

POST `/ann/list_article`

_List announcement articles_

Query announcement articles with pagination and filters for title, category, language, time, and other criteria. Send query parameters in the JSON request body. Both page and size are optional and must be strings when provided. No API key is required.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AnnouncementArticleListRequest | Required | none  
title_query | body | string | Optional | Article title to use when querying announcements.  
page | body | string | Optional | Page number. Optional. Pass as a string, for example "1".  
size | body | string | Optional | Number of articles to return per page. Optional. Pass as a string, for example "5".  
tags | body | string | Optional | Article tags  
timer | body | string | Optional | Query announcements from the last N days, with N passed as a string. For example, on the 10th, pass "10" to query announcements from the 1st through the 10th.  
cate_name | body | string | Optional | Announcement category name.  
cate_level | body | string | Optional | Category level, passed as a string: "1" or "2".  
sub_website_id | body | string | Optional | Subsite ID, passed as a string: "0" for the main site or "177" for the Turkey site. Defaults to "0".  
pinned | body | integer | Optional | Whether to include pinned articles: 1 to include them or 0 to exclude them. Defaults to 1.  
update_after | body | integer | Optional | Query announcement articles updated after this timestamp.  
lang | body | string | Optional | Language code, for example "cn".  
filter_empty_content | body | integer | Optional | Whether to exclude articles with empty content in the current language: 0 to keep them or 1 to exclude them. Defaults to 1.  
  
####  Request Body Schema

AnnouncementArticleListRequest

Announcement article list query

Request Body SchemaType | Constraints  
---|---  
AnnouncementArticleListRequest |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
title_query | string | Optional |  | Article title to use when querying announcements.  
page | string | Optional |  | Page number. Optional. Pass as a string, for example "1".  
size | string | Optional |  | Number of articles to return per page. Optional. Pass as a string, for example "5".  
tags | string | Optional |  | Article tags  
timer | string | Optional |  | Query announcements from the last N days, with N passed as a string. For example, on the 10th, pass "10" to query announcements from the 1st through the 10th.  
cate_name | string | Optional |  | Announcement category name.  
cate_level | string | Optional |  | Category level, passed as a string: "1" or "2".  
sub_website_id | string | Optional | default: "0" | Subsite ID, passed as a string: "0" for the main site or "177" for the Turkey site. Defaults to "0".  
pinned | integer | Optional | default: 1 | Whether to include pinned articles: 1 to include them or 0 to exclude them. Defaults to 1.  
update_after | integer | Optional |  | Query announcement articles updated after this timestamp.  
lang | string | Optional |  | Language code, for example "cn".  
filter_empty_content | integer | Optional | default: 1 | Whether to exclude articles with empty content in the current language: 0 to keep them or 1 to exclude them. Defaults to 1.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Announcement article list response | AnnouncementArticleListResponse  
  
### Response Schema

Status Code **200**

AnnouncementArticleListResponse

Announcement article list response

Type | Constraints  
---|---  
AnnouncementArticleListResponse | required: ["code","data","message","version"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Business status code  
data | AnnouncementArticleListData | Required | required: ["list","total"] | Announcement articles and total count  
message | string | Required |  | Response message  
version | string | Required |  | Response version  
  
**data**

AnnouncementArticleListData

Announcement articles and total count

Type | Constraints  
---|---  
AnnouncementArticleListData | required: ["list","total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Required |  | Announcement article list  
total | integer | Required |  | Total number of announcement articles.  
  
**data / list**

Announcement article list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

AnnouncementArticle

Announcement article

Type | Constraints  
---|---  
AnnouncementArticle | required: ["id","title","brief","created","updated","release_time","views","author","author_id","tags","cate","is_top","cate_id","source","content_lang_list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Required |  | Announcement article ID.  
title | string | Required |  | Article title  
brief | string | Required |  | Article summary  
created | string | Required |  | Article creation time, returned as a string.  
updated | string | Required |  | Article update time, returned as a string.  
release_time | string | Required |  | Article publication time, returned as a string.  
views | integer | Required |  | View count  
author | string | Required |  | Author  
author_id | integer | Required |  | Article author ID.  
tags | string | Required |  | Article tags  
cate | string | Required |  | Category to which the article belongs.  
is_top | integer | Required |  | Pinned status indicator for the article.  
cate_id | integer | Required |  | ID of the category to which the article belongs.  
source | string | Required |  | Article source  
content_lang_list | array | Required |  | Languages supported by the article, with the code and name of each language.  
  
**data / list / items / content_lang_list**

Languages supported by the article, with the code and name of each language.

Type | Constraints  
---|---  
array |   
  
**data / list / items / content_lang_list / items**

AnnouncementArticleLanguage

Announcement article language

Type | Constraints  
---|---  
AnnouncementArticleLanguage | required: ["code","name"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | string | Required |  | Language code, for example "cn".  
name | string | Required |  | Language name  
  
This operation does not require authentication 

Code samples
    
    
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
    
    

> Body parameter
    
    
    {
      "pinned": 1,
      "page": "1",
      "size": "5"
    }
    

> Example responses

> 200 Response
    
    
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
    

#  Schemas

##  AnnouncementArticleListRequest

AnnouncementArticleListRequest

Announcement article list query

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
title_query | string | Optional |  | Article title to use when querying announcements.  
page | string | Optional |  | Page number. Optional. Pass as a string, for example "1".  
size | string | Optional |  | Number of articles to return per page. Optional. Pass as a string, for example "5".  
tags | string | Optional |  | Article tags  
timer | string | Optional |  | Query announcements from the last N days, with N passed as a string. For example, on the 10th, pass "10" to query announcements from the 1st through the 10th.  
cate_name | string | Optional |  | Announcement category name.  
cate_level | string | Optional |  | Category level, passed as a string: "1" or "2".  
sub_website_id | string | Optional | default: "0" | Subsite ID, passed as a string: "0" for the main site or "177" for the Turkey site. Defaults to "0".  
pinned | integer | Optional | default: 1 | Whether to include pinned articles: 1 to include them or 0 to exclude them. Defaults to 1.  
update_after | integer | Optional |  | Query announcement articles updated after this timestamp.  
lang | string | Optional |  | Language code, for example "cn".  
filter_empty_content | integer | Optional | default: 1 | Whether to exclude articles with empty content in the current language: 0 to keep them or 1 to exclude them. Defaults to 1.  
      
    
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
    
    

##  AnnouncementArticleListResponse

AnnouncementArticleListResponse

Announcement article list response

Type | Constraints  
---|---  
object | required: ["code","data","message","version"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Business status code  
data | AnnouncementArticleListData | Required | required: ["list","total"] | Announcement articles and total count  
message | string | Required |  | Response message  
version | string | Required |  | Response version  
  
**data**

AnnouncementArticleListData

Announcement articles and total count

Type | Constraints  
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

Announcement articles and total count

Type | Constraints  
---|---  
object | required: ["list","total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Required |  | Announcement article list  
total | integer | Required |  | Total number of announcement articles.  
  
**list**

Announcement article list

Type | Constraints  
---|---  
array |   
  
**list / items**

AnnouncementArticle

Announcement article

Type | Constraints  
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
    
    

##  AnnouncementArticle

AnnouncementArticle

Announcement article

Type | Constraints  
---|---  
object | required: ["id","title","brief","created","updated","release_time","views","author","author_id","tags","cate","is_top","cate_id","source","content_lang_list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Required |  | Announcement article ID.  
title | string | Required |  | Article title  
brief | string | Required |  | Article summary  
created | string | Required |  | Article creation time, returned as a string.  
updated | string | Required |  | Article update time, returned as a string.  
release_time | string | Required |  | Article publication time, returned as a string.  
views | integer | Required |  | View count  
author | string | Required |  | Author  
author_id | integer | Required |  | Article author ID.  
tags | string | Required |  | Article tags  
cate | string | Required |  | Category to which the article belongs.  
is_top | integer | Required |  | Pinned status indicator for the article.  
cate_id | integer | Required |  | ID of the category to which the article belongs.  
source | string | Required |  | Article source  
content_lang_list | array | Required |  | Languages supported by the article, with the code and name of each language.  
  
**content_lang_list**

Languages supported by the article, with the code and name of each language.

Type | Constraints  
---|---  
array |   
  
**content_lang_list / items**

AnnouncementArticleLanguage

Announcement article language

Type | Constraints  
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

Announcement article language

Type | Constraints  
---|---  
object | required: ["code","name"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | string | Required |  | Language code, for example "cn".  
name | string | Required |  | Language name  
      
    
    {
      "code": "string",
      "name": "string"
    }