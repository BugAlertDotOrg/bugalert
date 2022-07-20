---
Title: Multiple Vulnerabilities in Atlassian Products (CVE-2022-26136, CVE-2022-26137, CVE-2022-26138)
Date: 2022-07-20 10:00
Category: Services & System Applications
Tags: Confluence, Jira, Bitbucket, Bamboo, Fisheye, Crowd, Atlassian, Very High Severity
Slug: atlassian
Summary: Multiple Vulnerabilities have been disclosed in Atlassian Products. A hardcoded credential vulnerability in Questions for Confluence, and Servlet Filter Bypass Vulnerabilities have been found in multiple Atlassian products that may enable Authentication Bypasses, XSS Attacks, and CORS attacks. These vulnerabilites have been assigned a bug alert severity of 'very high'. Atlassian recommends patching affected installations immediately.
---

On Wednesday, July 20th, 2022, [Atlassian released a Security Advisory](https://confluence.atlassian.com/security/july-2022-atlassian-security-advisories-overview-1142446703.html) stating that a hardcoded credential vulnerability exists in the Questions for Confluence application, as well as Servlet Filter bypasses in both first and third party applications tied to multiple Atlassian products. 

The hardcoded credential vulnerability stems from the use of the Questions for Confluence application with the `disabledsystemuser` account. The fix here is to update the Questions for Confluence app to a non-vulnerable version, or to disable/delete this account. **Uninstalling the Questions for Confluence application does not remediate this vulnerability.**

To check for use of the `disabledsystemuser` account, follow instructions found (here.)[https://confluence.atlassian.com/confkb/how-to-get-a-list-of-users-with-their-last-logon-times-985499701.html]

At this time they have not released any specifics as to what the exact vulnerable endpoint is for the servlet bypasses, or any indicators of compromise that could lead defenders to believe they have been exploited. The current fix is to patch to the level indicated in the advisory.

If exploited, these servlet bypass vulnerabilities may enable attackers to perform an Authentication Bypass, Cross-Site Scripting (XSS) Attacks, or Cross-Origin Resource Sharing (CORS) bypass.

If you have feedback (did you agree/disagree that a notice should have been sent?) or questions, please comment on the discussion thread linked below. This notice cost the project approximately $100 USD to send. If you would like to support the project, [you can learn more here](https://bugalert.org/content/pages/financial-support.html).
