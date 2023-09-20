try:
    from easy_spider_tool import *
except ImportError:
    raise ImportError(
        "Using easy_spider_tool, but the 'easy_spider_tool' package is not installed. "
        "Please using `pip install easy_spider_tool>=1.0.08`."
    ) from None

from .data import data_extractor, is_format_element

__author__ = 'hanxinkong'
__author_email__ = 'xinkonghan@gmail.com'

__version__ = "1.0.12"
