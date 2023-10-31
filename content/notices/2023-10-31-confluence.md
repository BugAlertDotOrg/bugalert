---
Title: Privilege escalation in Atlassian Confluence (CVE-2023-22515)
Date: 2023-10-31 14:45
Category: Services & System Applications
Tags: Confluence, Atlassian, High Severity, CVE-2023-22518
Slug: confluence
Summary: An authorization vulnerability exploitable by unauthenticated users has been discovered in Atlassian Confluence, and has been assigned a bug alert severity of 'very high'. Exploitation of the vulnerability can cause substanial data loss. Atlassian recommends removing installations from the Internet immediately if they cannot be patched.
---

| :exclamation:  SMS and phone notifications are not working in the United States due to new compliance requirements. Bug Alert is working with our telephony provider to resolve this as soon as possible.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

On Tuesday, October 31st, 2023, [Atlassian released a Security Advisory](https://confluence.atlassian.com/security/cve-2023-22518-improper-authorization-vulnerability-in-confluence-data-center-and-confluence-server-1311473907.html) stating that Confluence Server and Data Center editions are vulnerable to an authorization vulnerability which allows an unauthenticated attacker to cause significant data loss. Patches are available.

Now that a patch has been made available, it's likely that additional attackers will inspect the differences in the application binaries between the fixed and vulnerable versions, and develop attack methods rapidly. At this time, Atlassian is advising customers to remove Confluence Server and Data Center from being available from the Internet if they cannot be patched immediately, either by shutting them down, or by firewalling them off.

This vulnerability been assigned CVE-2023-22518.

If you have feedback (did you agree/disagree that a notice should have been sent?) or questions, please comment on the discussion thread linked below. This notice cost the project approximately $100 USD to send. If you would like to support the project, [you can learn more here](https://bugalert.org/content/pages/financial-support.html).
