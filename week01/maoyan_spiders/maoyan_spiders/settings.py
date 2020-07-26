# Scrapy settings for maoyan_spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyan_spiders'

SPIDER_MODULES = ['maoyan_spiders.spiders']
NEWSPIDER_MODULE = 'maoyan_spiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'maoyan_spiders (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3

DOWNLOAD_DELAY = 1

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIES_ENABLED = True


# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Cookie' : '__mta=150247945.1595499635438.1595726937207.1595729340863.17; uuid_n_v=v1; uuid=23F353E0CCCE11EA84945F632DCF0A4DCEFE032F925645FC99EE76F3A3EFE98B; _csrf=634c86e324fd45655a9b8573209f7ba8a566fccf8026be2489dacb427f007148; mojo-uuid=cfcf00377f0f9a348eea4c5ad7401352; _lxsdk_cuid=1737b3062d0c8-01d5a4db5e5bba-1b396257-13c680-1737b3062d0c8; _lxsdk=23F353E0CCCE11EA84945F632DCF0A4DCEFE032F925645FC99EE76F3A3EFE98B; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595499635,1595499962; mojo-session-id={"id":"33036e78ff22ecd0e98543118dca94e8","time":1595735429165}; mojo-trace-id=6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595736400; __mta=150247945.1595499635438.1595729340863.1595736399650.18; _lxsdk_s=173893e4d26-243-844-b%7C%7C12'
  }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyan_spiders.middlewares.MaoyanSpidersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyan_spiders.middlewares.MaoyanSpidersDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'maoyan_spiders.pipelines.MaoyanSpidersPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
