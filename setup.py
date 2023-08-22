from os import path as os_path

from setuptools import setup, find_packages

from easy_spider_tool_document import __version__

this_directory = os_path.abspath(os_path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


if __name__ == '__main__':
    setup(
        name='easy-spider-tool-document',  # 包名
        python_requires='>=3.6.8',  # python环境
        version=__version__,  # 包的版本
        description="easy-spider-tool 可选xpath/jsonpath聚合解析扩展包",  # 包简介，显示在PyPI上
        long_description=read_file('README.md'),  # 读取的Readme文档内容
        long_description_content_type="text/markdown",  # 指定包文档格式为markdown
        author="hanxinkong",  # 作者相关信息
        author_email='xinkonghan@gmail.com',
        url='https://easy-spider-tool-document.xink.top/',
        # 指定包信息，还可以用find_packages()函数
        packages=find_packages(),
        install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
        license="MIT",
        keywords=['easy', 'spider', 'tool', 'document'],
    )

# python setup.py sdist bdist_wheel upload -r local
