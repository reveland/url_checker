import logging
from urllib2 import Request, urlopen, HTTPError

logger = logging.getLogger(__name__)


class Checker():

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

    def check(self, link):
        logger.info('%s is beeing checked', link)
        r = Request(link, headers=self.headers)
        try:
            urlopen(r).read()
        except HTTPError, e:
            http_error_code = str(e).split(':')[0]
            logger.info('result: ', http_error_code)
            return http_error_code
        except:
            logger.info('result: Error')
            return 'Error'
        logger.info('result: Fine')
        return 'Fine'
