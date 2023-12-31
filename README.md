# simple-spider-tool-document

easy-spider-tool 可选xpath/jsonpath聚合解析扩展包

## 安装

```shell
pip install easy-spider-tool[document]
```

## 主要功能

- `data_extractor` 表达式数据解析（支持jsonpath,xpath）
- `xpath` xpath语法解析数据（支持首选项，设置默认值）

## 简单使用

```python
from easy_spider_tool_document import data_extractor

data = '<p>这是一个easy_spider_tool的document扩展的示例</p>'
print(data_extractor(data, ['//p//text()'], first=True, default=''))
# 这是一个easy_spider_tool的document扩展的示例

data = {
    "code": 200,
    "data": [
        {
            "id": 1,
            "username": "admin",
            "level": "boss"
        },
        {
            "id": 2,
            "username": "user",
            "level": "staff"
        }
    ]
}

print(data_extractor(data, ['$.data[*].username'], first=False, default=''))
# ['admin', 'user']
```

## 链接

Github：https://github.com/hanxinkong/easy-spider-tool-document

在线文档：https://easy-spider-tool-document.xink.top/

## 注明