# Scrapy
* scrapy version 0.24, website:http://scrapy.org/
* baidu_top project是抓取百度风云榜单的数据，其中baidu_top/spiders/baidu_top_spider.py调研有linkextract以及xpath selection的使用



# INSTALL
需要先安装lxml，OpenSSL, twisted，zope.interface，w3lib.http，cssselect，cryptography，cffi，service_identity，queuelib
* OpenSSL：https://github.com/pyca/pyopenssl
* cryptography：https://pypi.python.org/pypi/cryptography/, 依赖太多，实际用的是pip install cryptography搞定。"Successfully installed cffi-1.5.2 cryptography-1.2.3 enum34-1.1.2 idna-2.0 ipaddress-1.0.16 pyasn1-0.1.9 pycparser-2.14"
* service_identity: pip install service_identity
* queuelib：pip install queuelib 
* twisted: https://twistedmatrix.com/trac/
* zope.interface: https://pypi.python.org/pypi/zope.interface/
* w3lib.http：https://pypi.python.org/pypi/w3lib
* cssselect：https://pypi.python.org/pypi/cssselect
