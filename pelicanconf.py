from datetime import datetime

AUTHOR = "Bug Alert Contributors"
SITEURL = "https://bugalert.org"
SITENAME = "Bug Alert"
SITETITLE = "Bug Alert"
SITESUBTITLE = "A service for alerting security and IT professionals of high-impact and 0day vulnerabilities."
SITEDESCRIPTION = "Flex - The minimalist Pelican theme."
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

ARTICLE_URL = 'notices/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_SAVE_AS = 'notices/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


ARCHIVES_SAVE_AS = 'notices/index.html'
YEAR_ARCHIVE_SAVE_AS = 'notices/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'notices/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'notices/{date:%Y}/{date:%m}/{date:%d}/index.html'


AUTHORS_SAVE_AS = 'authors/index.html'
AUTHOR_URL = 'authors/{slug}/index.html'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'


CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORY_URL = 'categories/{slug}/index.html'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'


TAGS_SAVE_AS = 'tags/index.html'
TAG_URL = 'tags/{slug}/index.html'
TAG_SAVE_AS = 'tags/{slug}/index.html'


SOCIAL = (
    ("github", "https://github.com/sullivanmatt/bugalert"),
    ("rss", "/feeds/all.atom.xml"),
)

MENUITEMS = (
    ("About", "/pages/about.html"),
    ("Categories", "/categories/index.html"),
    ("Tags", "/tags/index.html"),
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
