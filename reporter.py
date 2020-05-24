import os
import smtplib
import logging
from time import gmtime, strftime

logger = logging.getLogger(__name__)


class Reporter():

    def __init__(self):
        self.FROM = os.environ['FROM']
        PASS = os.environ['PASS']
        self.TO = [os.environ['TO']]
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.FROM, PASS)

    def format(self, r):
        return r['url_check_result'] + ': ' + r['link']

    def get_subject(self):
        return 'url error report: ' + strftime("%Y-%m-%d %H:%M:%S", gmtime())

    def select(self, r):
        return r['url_check_result'] != 'Fine' and r['link'] != ''

    def report(self, df):
        filtered = df[df.apply(self.select, axis=1)]
        formatted = filtered.apply(self.format, axis=1)
        report = ' \n'.join(formatted)

        subject = self.get_subject()

        message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (
            self.FROM, ', '.join(self.TO), subject, report)

        logger.info('email sent: %s', message)

        self.server.sendmail(self.FROM, self.TO, message)
