---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/announcement
api_type: REST
updated_at: 2026-11-13 20:56:54.650779
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
» title_query | body | string | Optional | Article title to use when querying announcements.  
» page | body | string | Optional | Page number. Optional. Pass as a string, for example "1".  
» size | body | string | Optional | Number of articles to return per page. Optional. Pass as a string, for example "5".  
» tags | body | string | Optional | Article tags  
» timer | body | string | Optional | Query announcements from the last N days, with N passed as a string. For example, on the 10th, pass "10" to query announcements from the 1st through the 10th.  
» cate_name | body | string | Optional | Announcement category name.  
» cate_level | body | string | Optional | Category level, passed as a string: "1" or "2".  
» sub_website_id | body | string | Optional | Subsite ID, passed as a string: "0" for the main site or "177" for the Turkey site. Defaults to "0".  
» pinned | body | integer | Optional | Whether to include pinned articles: 1 to include them or 0 to exclude them. Defaults to 1.  
» update_after | body | integer | Optional | Query announcement articles updated after this timestamp.  
» lang | body | string | Optional | Language code, for example "cn".  
» filter_empty_content | body | integer | Optional | Whether to exclude articles with empty content in the current language: 0 to keep them or 1 to exclude them. Defaults to 1.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Announcement article list response | AnnouncementArticleListResponse  
  
### Response Schema

Status Code **200**

_AnnouncementArticleListResponse_

Name | Type | Description  
---|---|---  
» code | integer | Business status code  
» data | AnnouncementArticleListData | Announcement articles and total count  
»» list | array | Announcement article list  
»»» AnnouncementArticle | AnnouncementArticle | Announcement article  
»»»» id | integer | Announcement article ID.  
»»»» title | string | Article title  
»»»» brief | string | Article summary  
»»»» created | string | Article creation time, returned as a string.  
»»»» updated | string | Article update time, returned as a string.  
»»»» release_time | string | Article publication time, returned as a string.  
»»»» views | integer | View count  
»»»» author | string | Author  
»»»» author_id | integer | Article author ID.  
»»»» tags | string | Article tags  
»»»» cate | string | Category to which the article belongs.  
»»»» is_top | integer | Pinned status indicator for the article.  
»»»» cate_id | integer | ID of the category to which the article belongs.  
»»»» source | string | Article source  
»»»» content_lang_list | array | Languages supported by the article, with the code and name of each language.  
»»»»» AnnouncementArticleLanguage | AnnouncementArticleLanguage | Announcement article language  
»»»»»» code | string | Language code, for example "cn".  
»»»»»» name | string | Language name  
»»»»» total | integer | Total number of announcement articles.  
»»»» message | string | Response message  
»»»» version | string | Response version  
  
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

##  AnnouncementArticleListResponse

_AnnouncementArticleListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | Business status code  
data | AnnouncementArticleListData | Required | none | Announcement articles and total count  
message | string | Required | none | Response message  
version | string | Required | none | Response version  
      
    
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

_AnnouncementArticleListData_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
list | [AnnouncementArticle] | Required | none | Announcement article list  
total | integer | Required | none | Total number of announcement articles.  
      
    
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

_AnnouncementArticleListRequest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
title_query | string | Optional | none | Article title to use when querying announcements.  
page | string | Optional | none | Page number. Optional. Pass as a string, for example "1".  
size | string | Optional | none | Number of articles to return per page. Optional. Pass as a string, for example "5".  
tags | string | Optional | none | Article tags  
timer | string | Optional | none | Query announcements from the last N days, with N passed as a string. For example, on the 10th, pass "10" to query announcements from the 1st through the 10th.  
cate_name | string | Optional | none | Announcement category name.  
cate_level | string | Optional | none | Category level, passed as a string: "1" or "2".  
sub_website_id | string | Optional | none | Subsite ID, passed as a string: "0" for the main site or "177" for the Turkey site. Defaults to "0".  
pinned | integer | Optional | none | Whether to include pinned articles: 1 to include them or 0 to exclude them. Defaults to 1.  
update_after | integer | Optional | none | Query announcement articles updated after this timestamp.  
lang | string | Optional | none | Language code, for example "cn".  
filter_empty_content | integer | Optional | none | Whether to exclude articles with empty content in the current language: 0 to keep them or 1 to exclude them. Defaults to 1.  
      
    
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

_AnnouncementArticle_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer | Required | none | Announcement article ID.  
title | string | Required | none | Article title  
brief | string | Required | none | Article summary  
created | string | Required | none | Article creation time, returned as a string.  
updated | string | Required | none | Article update time, returned as a string.  
release_time | string | Required | none | Article publication time, returned as a string.  
views | integer | Required | none | View count  
author | string | Required | none | Author  
author_id | integer | Required | none | Article author ID.  
tags | string | Required | none | Article tags  
cate | string | Required | none | Category to which the article belongs.  
is_top | integer | Required | none | Pinned status indicator for the article.  
cate_id | integer | Required | none | ID of the category to which the article belongs.  
source | string | Required | none | Article source  
content_lang_list | [AnnouncementArticleLanguage] | Required | none | Languages supported by the article, with the code and name of each language.  
      
    
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

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | string | Required | none | Language code, for example "cn".  
name | string | Required | none | Language name  
      
    
    {
      "code": "string",
      "name": "string"
    }