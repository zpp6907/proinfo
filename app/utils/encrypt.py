"""
@Time    : 2022/6/25 22:18
@Author  : peyzhang
@Email   : peyzhang@163.com
@File    : encrypt.py
@Software: PyCharm
"""
import hashlib
from django.conf import settings

def md5(data_string):

    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode("utf-8"))
    return obj.hexdigest()


