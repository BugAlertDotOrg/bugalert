---
title: Privacy Policy
---

### Overview
Bug Alert will never sell or make available your data. This project is not intended to make me (Matthew Sullivan - the founder and maintainer), money. In fact, I'm quite sure it will do the opposite with great efficiency.
#### Terminology
Amazon Web Services is referred to a number of times in this document, using the abbreviation 'AWS'.

### Tracking
We do not track your use of the site via the browser, aside from access logs held by Cloudflare and AWS (Lambda / CloudWatch Logs) as part of hosting this service. These services log typical web server access information, including source IP address, user agent, etc.

When you receive a Bug Alert notice via email, we may track link click-through rates via our provider SendGrid. This is only utilized for understanding what level of value email notifications are providing to subscribers, and do not contain information that identifies your email address specifically when tracking click-through rates.

### What data is stored, and where?
#### By us
Bug Alert stores only two pieces of personal information: your email address (required), and, optionally, your phone number. These are stored at rest in an AWS-based, KMS-encrypted DynamoDB instance in the United States (us-east-1). The AWS account is controlled by one person (Matthew Sullivan), and utilizes MFA with a strong, fully-random password and least-privilege IAM policies where possible.

#### By our sub-processors
Telephony services are currently provided by Call-Em-All LLC. Call-Em-All will be provided your phone number if you opt to receive notices by phone or SMS. They are not provided your email address under any circumstances. Call-Em-All LLC. is a US-based company that stores data in the United States (AWS, us-east-1), and their privacy policy, including right-to-be-forgotten information, is found at [https://www.text-em-all.com/privacy-policy](https://www.text-em-all.com/privacy-policy).

Email services are provided by Twilio (SendGrid). In the future, it is likely that Twilio will *also* be utilized as a provider of telephony services for phone numbers serviced outside of the US and Canada, and perhaps eventually for all global telephony services. Their privacy policy, including right-to-be-forgotten information, is found at [https://www.twilio.com/legal/privacy](https://www.twilio.com/legal/privacy). At this time, since Twilio is not being utilized for telephony services yet, they are only provided your email address. Twilio stores data in the United States (multiple datacenters and locations).

Some additional email services are provided by AWS Simple Email Service (SES) in the United States (AWS, us-east-1).

### Need more information?
Open a GitHub issue if this privacy policy has not addressed your questions or concerns. We aim to operate in a highly transparent way.
