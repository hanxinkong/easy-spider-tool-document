from easy_spider_tool_document import data_extractor

if __name__ == '__main__':
    data = '<div><p>这是一个easy_spider_tool的document扩展的示例</p></div>'
    data = data_extractor(data, ['//div'], first=True, default='')
    print(data_extractor(data, ['.//p//text()', '$.data[*].username'], first=False, default=''))

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

    print(data_extractor(data, ['.//p//text()', '$.data[*].username'], first=False, default=''))
