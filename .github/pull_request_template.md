
# Pull Request Template

Please read carefully, we'll keep it brief. Thank you for your contribution.


## Housekeeping (you can remove this section)
Vulnerability reports are treated as emergencies. You can be brief in your pull request description and let your change speak for itself. To assist our volunteers, please adhere to our pull request title format:

Initial report of a vulnerability should be titled as:
> Vulnerability: Component Name

Updates to existing reports should be titled as:
> Update: Component Name

Everything else (typo fixes, changes to site behaviors, etc.) should be titled as:
> Improvement: Component Name

Component names should be as concise and accurate as possible, e.g. `jackson-databind`, `openssl`, etc.

## Contributor Checklist
### For Vulnerability Reports
- [ ] Check ["Allow edit from maintainers" option](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) in pull request so that additional changes can be pushed by the Bug Alert team.
- [ ] Ensure you [used the notice template](https://github.com/sullivanmatt/bugalert/blob/main/content/notices/202X-MM-DD-slug.md.template) for posting a notice. The 'summary' field will be used for notifications (email, phone, and SMS). It is of the utmost importance that the summary be clear and concise, so we ask that you please follow the format suggested in the template unless there is a compelling and justifiable need to deviate from it.

### For Site Improvements

- [ ] Check ["Allow edit from maintainers" option](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) in pull request so that additional changes can be pushed by the Bug Alert team if needed.
- [ ] I have performed a self-review of my own code.
- [ ] I have commented my code, particularly in hard-to-understand areas.
- [ ] My changes generate no new warnings.
- [ ] I have run Pelican locally to ensure my changes have not disrupted the look, feel, or functionality of the site.
- [ ] I have checked my code and corrected any misspellings.
- [ ] I have added a pull request description which details the nature of this change.
