# Bug Alert

#### Bug Alert is a service for alerting security and IT professionals of high-impact and 0day vulnerabilities.
Hi, I'm Matthew Sullivan, a security practitioner, and the creator of Bug Alert.

When the Log4j vulnerability was first discovered, it was reported, as most are, on Twitter.
13 hours passed between the time it was disclosed on Twitter to the time LunaSec put out their
widely-shared blog post, and 5 hours passed after that before I saw it up at the top of
[Hacker News](https://news.ycombinator.com). By then, precious time for reacting had been completely
lost; it was nearly midnight in my local timezone, and all the people I needed to mobilize were already in bed.

There is no central clearinghouse for notifying security professionals about critical security issues in
widely-used software. The process for issuing security bulletins from organizations like the
[CISA](https://www.cisa.gov/) are both welcomed and well-intentioned, but by the time a CVE
identifier has been issued, or a bulletin posted, it's simply too late.

Bug Alert has exactly one goal: rapid notification for serious flaws in widely-used software. This process
is conducted entirely in the open, via our project on [GitHub](https://github.com/sullivanmatt/bugalert).
Email/phone/SMS notification services are (obviously) not free, but my intent is to keep this effort
funded by community/industry donations, if it is ever needed.

**Contributions are highly encouraged!** We also need a team of volunteers from around the world who can review
and rapidly merge GitHub pull requests detailing new issues, as they come in. Volunteers need to be kind, level-headed
individuals who are willing to engage a diverse set of people in the security community with unwaivering professionalism
and no ego. If that sounds like you, [open a GitHub issue letting us know!](https://github.com/sullivanmatt/bugalert/issues/new?labels=personnel&title=I+would+like+to+volunteer!&body=Tell+us+about+yourself.+We+want+to+ensure+volunteers+have+relevant+security+expertise,+so+please+include+information+and/or+links+related+to+your+skillset+or+past+projects.)

## What Are Notices & Contributing Your Knowledge
Notices are the lifeblood of this service; they are the text that will explain to the community
what they need to be worrying about, and why. The merging of a new notice kicks off the automated processes
for alerting subscribers by phone, SMS, and email - a potentially expensive operation (telephony
services aren't cheap!) that gets only one shot. Notices will generally only be merged into this project
for software in widespread use (think hundreds of thousands of installs), and **only if there is a
large, immediate, demonstrable risk** to the systems that are running the vulnerable software.

If you want to submit a notice, simply fork this repository, follow the template in
`content/notices/202X-MM-DD-slug.md.template` to author a new notice, and make a pull request.

0day vulnerabilities will be the most commonly-reported issue for this project, but Bug Alert's
notices are not *exclusive* to 0days. For example, when Log4j 2.15.0 was released to address a years-old
issue with prior 2.X.X versions, the security community almost immediately found a vector for denial-of-service
(not worthy of a Bug Alert notice). However, a day later, once the DoS issue had already been patched
by 2.16.0, researchers found that the vector for DoS in 2.15.0 could also be used for remote code execution.
Such a finding *would* be worthy of a Bug Alert notice, because 2.15.0 was likely to be in widespread use
at the time the new vector for RCE was found.

Notices are required to have several fields, the most important of which are *Summary*, *Category*,
and *Tags*. Always use the template found at `content/notices/202X-MM-DD-slug.md.template` to craft a
notice, and refer to this README for what acceptable values for summary, category, and tags should be.

### Assigning Severity
Severity levels are 'High', 'Very High', and 'Critical'. Make a best effort based on the criteria
below, but please be aware that project maintainers may raise or lower your proposed severity based
on their own knowledge, experience, and understanding. A new Bug Alert notice may quite literally
wake someone up out of bed; our goal should be to only do that when it is truly necessary and appropriate.

#### High Severity
The high severity level is to be used for vulnerabilities that are extremely damaging, but
only in configurations that are found less often in real-world environments, or have other migitating factors.
These issues need attention, but nobody is working overnight or during the weekend to patch systems.

_Example: A flaw in Adobe Reader for Windows can be utilized to install malware on a single user's
system, simply by opening a malicious PDF file._

#### Very High Severity
The very high severity level is to be used for vulnerabilities that introduce remote code execution,
privilege escalation, information disclosure/leakage, etc, where the impact may be high, but
other mitigating factors are present (necessary insider knowledge required for exploit, chaining
of vulnerabilities is required for successful exploit, etc). These issues need prompt attention
and may require an unexpected evening maintenence window, but you can probably keep your date night
plans.

_Example: A flaw in Microsoft Active Directory allows any authenticated domain user on the local
network to escalate their role to Domain Administrator._

#### Critical Severity
The critical severity level is reserved for vulnerabilities that introduce remote code execution,
privilege escalation, information disclosure/leakage, and similar issues which, if exploited,
will lead to massive reputational and financial damage; the types of vulnerabilities that
make national news. These issues need immediate attention, and you'll be working nights and
weekends until you are certain you've got everything patched up.

_Example: A flaw in Django, a widely-used Python webapp framework, allows an unauthenticated attacker
to run arbitrary commands on the server via the Internet and retrieve the results of those commands._

#### None of Those Seem To Fit?
If the issue you want to report doesn't fit the descriptions above, it may be that the issue
is not of high enough impact to be served by this project. We appreciate that you took the time
to consider reporting the issue to a wider audience, and will encourage you to share your
knowledge on social media such as Twitter or Reddit's security-focused subreddits.

Types of vulnerabilities *generally* outside the scope of Bug Alert's focus are described below.
Use your judgement though, and don't hestitate to submit a notice if you are confident the wider
security and IT communities need to know immediately about an issue.

For example, while DoS vulnerabilities are generally out of scope, an attack that could
crash-loop an nginx server in one packet would still be worthy of a notice.

Issues generally outside the scope of this project include:

* Software not in widespread use
* Denial of service
* Protocol attacks (e.g. TLS cipher downgrade)
* Attacks requiring local network access (e.g. Microsoft SMB RCEs)
* Attacks heavily relying on user interaction (e.g. user must be tricked into downloading an executable)

### Summary
Summary is the text which will be shared in notifications sent out to all subscribers.  It is
the most critical piece of information, and accuracy and clarity is key. For subscribers
who opt to recieve phone calls, the summary will be converted to spoken word through Google's
Text-to-Speech engine.

### Tags
Tags should make it easy for someone to browse the bugalert.org site and find previous issues
related to a specific component. Tags are a comma-separated list that should include the name
of the component, the framework or runtime (if applicable), and the severity rating.

For example, a critical issue impacting the popular Java library 'Jackson Databind' should
include the tags `jackson-databind`, `Java`, and `Critical Severity`. 

### Category
Category is used to segment which notices subscribers would like to receive. There are four
options, and notice authors must only pick one:

#### Software Frameworks, Libraries, and Components
Most commonly used for open-source components.

_Examples: Django, Flask, Rails, Angular, Spring Boot._

#### Operating Systems
For operating systems, in desktop, server, and mobile flavors.

_Examples: Windows SMB, Linux Kernel, iMessage, Apple Darwin._

#### Services & System Applications
For services not written by the operating system vendor, core components,
and language runtimes. This category can also include components primarily
indended for end-users, but that are rarely installed by the average
non-administrative user of a system.

_Examples: openssh, Apache HTTP Server, nodejs, nginx, Java Runtime, vim, curl, Python._

#### End-User Applications
Applications that your average non-technical user uses regularly, often without
updating, unless an automatic updating mechanism is built into the application.

_Examples: Firefox, Chrome, Thunderbird, Outlook, Adobe Acrobat Reader, Spotify,
Audacity, VLC, Steam, Microsoft Office._

## Contributing
Pull requests are welcome and encouraged.

### Run Locally
Clone this repo and `cd` into it:
`git@github.com:BugAlertDotOrg/bugalert.git && cd bugalert`

Clone the bugalert-pelican repo in as well:
`git@github.com:BugAlertDotOrg/bugalert-pelican.git`

In a Python 3.6+ environment, install all project requirements:
`pip install -Ur bugalert-pelican/requirements.txt`

After that, you can run a local instance with:
`rm -rf output && pelican --autoreload --listen -s bugalert-pelican/pelicanconf.py`
