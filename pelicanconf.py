from datetime import datetime

AUTHOR = "Bug Alert Contributors"
SITEURL = "https://bugalert.org"
SUBSCRIPTIONSURL = "https://subscriptions.bugalert.org"
SITENAME = "Bug Alert"
SITETITLE = "Bug Alert"
SITESUBTITLE = "A service for alerting security and IT professionals of high-impact and 0day vulnerabilities."
SITEDESCRIPTION = "A service for alerting security and IT professionals of high-impact and 0day vulnerabilities."
SITELOGO = '/images/bug.svg'
FAVICON = '/images/bug.svg'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

THEME = "./theme"
PATH = "content"
OUTPUT_PATH = "output/"
TIMEZONE = "America/New_York"

DISABLE_URL_HASH = True
DISPLAY_PAGES_ON_MENU = False

# PLUGIN_PATHS = ['pelican-plugins']

# PLUGINS = ['i18n_subsites']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

MARKDOWN = {'extension_configs': { 'pymdownx.tilde': {}
                                 , 'markdown.extensions.fenced_code': {}
                                 , 'markdown.extensions.tables': {}}}

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['manifest']

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
#FEED_ALL_RSS = "feeds/all.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GITHUB_CORNER_URL = "https://github.com/sullivanmatt/bugalert"

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

ARTICLE_URL = 'content/notices/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = 'content/notices/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'

PAGE_URL = 'content/pages/{slug}.html'
PAGE_SAVE_AS = 'content/pages/{slug}.html'

ARCHIVES_SAVE_AS = 'content/notices/index.html'
YEAR_ARCHIVE_SAVE_AS = 'content/notices/{date:%Y}.html'
MONTH_ARCHIVE_SAVE_AS = 'content/notices/{date:%Y}-{date:%m}.html'
DAY_ARCHIVE_SAVE_AS = 'content/notices/{date:%Y}-{date:%m}-{date:%d}.html'

AUTHORS_SAVE_AS = 'authors.html'
AUTHOR_URL = 'authors/{slug}.html'
AUTHOR_SAVE_AS = 'authors/{slug}.html'

CATEGORIES_SAVE_AS = 'categories.html'
CATEGORY_URL = 'categories/{slug}.html'
CATEGORY_SAVE_AS = 'categories/{slug}.html'

TAGS_SAVE_AS = 'tags.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'


SOCIAL = (
    ("github", "https://github.com/sullivanmatt/bugalert"),
    ("twitter", "https://twitter.com/BugAlertDotOrg"),
    ("rss", "/feeds/all.atom.xml"),
)

MENUITEMS = (
    ("About", "/content/pages/about.html", ""),
    ("My Subscriptions", "/content/pages/my-subscriptions.html", ""),
    ("Categories", "/categories.html", "nomobile"),
    ("Tags", "/tags.html", "nomobile"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

STATIC_PATHS = ["images"]#, "extra/ads.txt", "extra/CNAME"]

#EXTRA_PATH_METADATA = {
#    "extra/ads.txt": {"path": "ads.txt"},
#    "extra/CNAME": {"path": "CNAME"},
#}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
