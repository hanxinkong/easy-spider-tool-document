from typing import Union, List
from lxml import etree


def xpath(src_data: etree.HTML, expr: Union[str, List[str]], first: bool = False, default=None):
    """
    xpath解析
    :param src_data: 解析对象
    :param expr: xpath,可选多个
    :param default: 未获取到返回默认值， 默认空字符串
    :param first: `True`只返回第一个， `False`返回全部
    :return: 解析值或者 default
    """
    values = None

    if isinstance(expr, str):
        expr = [expr]

    for i in expr:
        values = src_data.xpath(i)
        # 处理值本身为None的情况
        if isinstance(values, list) and not list(filter(None, values)):
            values = False

        if values:
            break

    if not values:
        return default

    if first is True:
        values = values[0]

    return values
