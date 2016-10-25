#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
辅助工具
"""


def read_inputs(message='请输入数据：', *validators, **options):
    """读取输入"""
    while True:
        values = input(message).split(
            options['separate'] if 'separate' in options else ','
        )
        index = 0
        value_num = len(values)
        for validator in validators:
            if index == value_num:
                print('输入参数过少')
                break
            value = values[index]
            if isinstance(validator, Validator):
                _value, types_str = validator.conversion(value)
                if _value is None:
                    print('第%d个参数(%s)不是 %s 类型' % (index + 1, value, types_str))
                    break
                result = validator.validate(_value)
                if result:
                    print('第%d个参数(%s)验证失败，%s' % (index + 1, value, result))
                    break
                values[index] = _value
            else:
                if validator and not validator(value):
                    break
            index += 1
            continue
        if index != len(validators):
            continue
        if index != value_num:
            print('输入参数过多')
            continue
        if 'validate' in options and options['validate'][0](values) != True:
            print(options['validate'][1])
            continue
        if index == 1:
            return values[0]
        return values


class Validator(object):
    """校验器"""

    def conversion(self, value):
        """转换类型"""
        types_str = ''
        _value = value
        for valid_type in self.types:
            try:
                _value = valid_type(value)
            except ValueError:
                _value = None
                types_str += '|' + str(valid_type)[8:-2]
                continue
            break
        return _value, types_str[1:]

    def validate(self, value):
        """校验"""
        for chain in self.chains:
            if chain and not chain[0](value):
                return chain[1]

    def __init__(self, *chains):
        self.chains = chains
        self.types = ()


class NumValidator(Validator):
    """数字校验器"""

    def __init__(self, min_value=None, max_value=None, types=None):
        parent = super(NumValidator, self)
        parent.__init__(
            min_value is not None and (
                lambda value: value >= min_value,
                '数值未达到下限' + str(min_value)
            ),
            max_value is not None and (
                lambda value: value < max_value,
                '数值已达到上限' + str(max_value)
            )
        )
        self.types = types or (int, float)


class IntValidator(NumValidator):
    """整数校验器"""

    def __init__(self, min_value=None, max_value=None):
        super(IntValidator, self).__init__(min_value, max_value, (int,))


class FloatValidator(NumValidator):
    """小数校验器"""

    def __init__(self, min_value=None, max_value=None):
        super(FloatValidator, self).__init__(min_value, max_value, (float,))


class StrValidator(Validator):
    """字符串校验器"""

    def __init__(self, min_len=1, max_len=None):
        parent = super(StrValidator, self)
        parent.__init__(
            min_len is not None and (
                lambda value: len(value) >= min_len,
                '字符串长度低于下限%d' % min_len
            ),
            max_len is not None and (
                lambda value: len(value) <= max_len,
                '字符串长度超出上限%d' % max_len
            )
        )

if __name__ == '__main__':
    print(read_inputs(
        'Test `read_input` function: (None, 1.0, 1, 0.1, "abc")',
        None,  # 无限制
        NumValidator(0, 10.0),
        IntValidator(0, 10),
        FloatValidator(0, 1.0),
        StrValidator(6)
    ))
