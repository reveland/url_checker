import pandas as pd
import json
import logging.config
from flask import Flask

from provider import Provider
from checker import Checker
from reporter import Reporter

with open('log_config.json', 'r') as log_config_file:
    log_config_dict = json.load(log_config_file)
logging.config.dictConfig(log_config_dict)

provider = Provider()
checker = Checker()
reporter = Reporter()

app = Flask(__name__)


@app.route('/trigger')
def trigger():
    table = provider.get_table()
    df = pd.DataFrame(table)

    df['url_check_result'] = df.apply(
        lambda r: checker.check(r['link']), axis=1)

    reporter.report(df)

    return 'done.'
