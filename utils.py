# common libraries
import pandas as pd
import numpy as np
import scipy as sp
from collections import defaultdict, Counter
from requests import Session

# libs for visualization
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.offline as py
import plotly.graph_objs as go
sns.set_style('whitegrid')

# libraries
import logging.config
from pymongo import MongoClient

import tqdm
from tqdm._tqdm_notebook import tqdm_notebook as tn
tn.pandas()

mc = MongoClient('mongodb://USER:PASS@IP')


def tgn(msg: str, alarmer_keys=None):
    s = Session()
    if alarmer_keys is None:
        alarmer_keys = ['YOUR_TOKEN_FROM_t.me/alarmer_bot']
    parts = msg.split('\n\n')
    for ak in alarmer_keys:
        for part in parts:
            s.get('https://alarmerbot.ru/', params={'key': ak, 'message': part})


def set_logging(level="DEBUG", formatting=None, disable_existing=False, console=True, file=False, path=None):
    handlers = {}
    if console:
        handlers['console'] = {
            "level": level, "class": "logging.StreamHandler",
            "formatter": "debug", "stream": "ext://sys.stdout"
        }
    if file:
        handlers['file'] = {
            "level": level, "class": "logging.handlers.WatchedFileHandler",
            "formatter": "debug", "filename": path or 'debug.log',
            "mode": "w", "encoding": "utf-8"
        }
    if formatting is None:
        formatting = "[%(asctime)s] %(message)s"
    config = {
        "version": 1, "disable_existing_loggers": disable_existing,
        "formatters": {"debug": {"class": "logging.Formatter", "format": formatting}},
        "handlers": handlers,
        "root": {"handlers": list(handlers.keys()), "level": level}
    }
    logging.config.dictConfig(config)
