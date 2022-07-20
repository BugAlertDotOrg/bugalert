---
Title: Servlet Filter Bypass Vulnerabilities in Multiple Atlassian Products (CVE-2022-26136, CVE-2022-26137)
Date: 2022-07-20 10:00
Category: Services & System Applications
Tags: Confluence, Jira, Bitbucket, Bamboo, Fisheye, Crowd, Atlassian, Very High Severity
Slug: atlassian
Summary: Servlet Filter Bypass Vulnerabilities have been found in multiple Atlassian products that may enable Authentication Bypasses, XSS Vulnerabilities, and CORS vulnerabilities. These vulnerabilites have been assigned a bug alert severity of 'very high'. Atlassian recommends patching affected installations immediately.
---

On Wednesday, July 20th, 2022, [Atlassian released a Security Advisory](https://confluence.atlassian.com/doc/confluence-security-advisory-2022-06-02-1130377146.html) stating that Servlet Filter bypasses exist in both first and third party applications tied to multiple Atlassian products. At this time they have not released any specifics as to what the exact vulnerable endpoint is, or any indicators of compromise that could lead defenders to believe they have been exploited. The current fix is to patch to the level indicated in the advisory.

If exploited, these vulnerabilities may enable attackers to perform an Authentication Bypass, Cross-Site Scripting (XSS) Attacks, or Cross-Origin Resource Sharing (CORS) bypass.

If you have feedback (did you agree/disagree that a notice should have been sent?) or questions, please comment on the discussion thread linked below. This notice cost the project approximately $100 USD to send. If you would like to support the project, [you can learn more here](https://bugalert.org/content/pages/financial-support.html).
