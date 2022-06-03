---
Title: Unauthenticated Remote Code Execution in Atlassian Confluence (CVE-2022-26134)
Date: 2022-06-02 17:00
Category: Services & System Applications
Tags: Confluence, Atlassian, Very High Severity
Slug: confluence
Summary: An unauthenticated remote code execution flaw has been found, and is being actively exploited, in Atlassian Confluence, and has been assigned a bug alert severity of 'very high'. Atlassian recommends removing installations from the Internet immediately.
---

On Thursday, June 2nd, 2022, [Atlassian released a Security Advisory](https://confluence.atlassian.com/doc/confluence-security-advisory-2022-06-02-1130377146.html) stating that Confluence Server and Data Center editions are vulnerable to an Unauthenticated Remote Code Execution vulnerability **that is under active exploitation**. At this time they have not released any specifics as to what the exact vulnerable endpoint is, or any indicators of compromise that could lead defenders to believe they have been exploited. There is currently no fix.

Once a patch has been made available, it's likely that additional attackers will inspect the differences in the application binaries between the fixed and vulnerable versions, and develop attack methods rapidly. This post will be updated as information becomes available.

At this time, Atlassian is advising customers to remove Confluence Server and Data Center from being available from the Internet, either by shutting them down, or by firewalling them off.

This vulnerability been assigned CVE-2022-26134. ~~Patches are not yet available from the vendor~~ (see last update for patch links). This notice will be updated when they are published.

## Update as of June 2nd, 10:00PM New York time

Cybersecurity firm Volexity has [published a blog post](https://www.volexity.com/blog/2022/06/02/zero-day-exploitation-of-atlassian-confluence/) detailing how they originally found this vulnerability being used in the wild, prior to reporting it to Atlassian. Their write-up includes IP ranges the attackers utilized, as well as some additional background information.

The United States Cybersecurity & Infrastructure Security Agency (CISA) has added this flaw to its list of [known exploited vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) with a deadline for remediation of Friday, June 3rd, 2022.

~~As of this update, there is still no patch available.~~ Confluence administrators are urged to remove public-facing installations from the Internet as soon as possible.

## Update as of June 3rd, 2:30PM New York time

**[Patches are now available from Atlassian.](https://www.atlassian.com/software/confluence/download-archives)**

If you have feedback (did you agree/disagree that a notice should have been sent?) or questions, please comment on the discussion thread linked below. This notice cost the project approximately $100 USD to send. If you would like to support the project, [you can learn more here](https://bugalert.org/content/pages/financial-support.html).
