from converters.builder import CONVERTERS
from converters.converter1 import Converter_1

# 使用注册器管理模块
@CONVERTERS.register_module()
def converter_2(a, b):
    return Converter1(a, b)