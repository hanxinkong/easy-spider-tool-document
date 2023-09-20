import json
from typing import Dict, Any, List, Union
from easy_spider_tool import is_format_json, jsonpath
from lxml import etree

from easy_spider_tool_document.xpath import xpath

__all__ = ['data_extractor', 'is_format_element']


def is_format_element(element_string: Union[str, etree._Element]) -> bool:
    # noinspection PyBroadException
    if isinstance(element_string, etree._Element):
        return True
    try:
        etree.HTML(element_string)
        return True
    except Exception as _:
        pass
    return False


def to_dict(src: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
    if isinstance(src, dict):
        return src

    return json.loads(src)


def to_element(element: Union[str, etree._Element]) -> etree._Element:
    if isinstance(element, etree._Element):
        return element

    if isinstance(element, str):
        return etree.HTML(element)

    return etree.HTML('')


def element_type(string: str) -> str:
    """获取类型"""
    if any([
        isinstance(string, dict),
        is_format_json(string),
    ]):
        return 'json'
    elif is_format_element(string):
        return 'element'
    return None


def data_extractor(src_data, expr: Union[str, List[str]], first: bool = False, default=None):
    """json，xpath选择器"""
    # assert src_data, ''
    # if len(src_data) < 1:
    #     return default

    ele_type = element_type(src_data)

    if ele_type is None:
        return default

    values = None

    if isinstance(expr, str):
        expr = [expr]

    json_expr = list(filter(lambda x: x.startswith('$'), expr))
    xpath_expr = list(filter(lambda x: x.startswith('.') or x.startswith('/'), expr))

    if ele_type == 'json':
        if json_expr:
            data = to_dict(src_data)
            values = jsonpath(data, json_expr, first=first, default=default)

    if ele_type == 'element':
        if any(xpath_expr):
            data = to_element(src_data)
            values = xpath(data, xpath_expr, first=first, default=default)

    if len(values) < 1:
        values = default

    return values
