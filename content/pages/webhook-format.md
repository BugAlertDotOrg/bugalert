---
title: Webhook Format
---

Webhook calls will POST a JSON body with the following format and content:
```
{
  "title": "RCE in Log4j",
  "category": "Software Frameworks, Libraries, and Components",
  "tags": "Java, Log4j, Critical Severity",
  "url": "https://bugalert.org/content/notices/2021-12-09-log4j.html",
  "slug": "log4j",
  "summary": "A remote code execution vulnerability has been found in the popular Java logging library Log4j. This issue is easily exploited in common configurations, and has been assigned a bug alert severity of 'critical'."
}
```
