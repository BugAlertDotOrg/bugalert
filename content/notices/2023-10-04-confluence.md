---
Title: Privilege escalation in Atlassian Confluence (CVE-2023-22515)
Date: 2023-10-04 12:45
Category: Services & System Applications
Tags: Confluence, Atlassian, High Severity, CVE-2023-22515
Slug: confluence
Summary: A privilege escalation flaw has been found, and is being actively exploited, in Atlassian Confluence, and has been assigned a bug alert severity of 'very high'. Atlassian recommends removing installations from the Internet immediately if they cannot be patched.
---

On Wednesday, October 4th, 2023, [Atlassian released a Security Advisory](https://confluence.atlassian.com/security/cve-2023-22515-privilege-escalation-vulnerability-in-confluence-data-center-and-server-1295682276.html) stating that Confluence Server and Data Center editions are vulnerable to a privilege escalation vulnerability **that is under active exploitation**. Patches are available.

Now that a patch has been made available, it's likely that additional attackers will inspect the differences in the application binaries between the fixed and vulnerable versions, and develop attack methods rapidly. At this time, Atlassian is advising customers to remove Confluence Server and Data Center from being available from the Internet if they cannot be patched immediately, either by shutting them down, or by firewalling them off.

This vulnerability been assigned CVE-2023-22515.

If your Confluence installation is hosted behind Cloudflare and your origin is protected from the Internet, [Cloudflare is mitigating the exploit for you already](https://blog.cloudflare.com/all-cloudflare-customers-protected-atlassian-cve-2023-22515/).

If you have feedback (did you agree/disagree that a notice should have been sent?) or questions, please comment on the discussion thread linked below. This notice cost the project approximately $100 USD to send. If you would like to support the project, [you can learn more here](https://bugalert.org/content/pages/financial-support.html).
