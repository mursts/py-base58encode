#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import re

class Base58:
    def __init__(self):
        self._CHARS = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
        self._CHAR_NUM = len(self._CHARS)

    def _is_numeric(self, num):
        matcher = re.compile(r'^[\d]*$')
        return matcher.match(str(num))

    def _is_empty(self, value):
        if value is None or value == '':
            return True
        return False

    def encode(self, value):
        if self._is_empty(value) or self._is_numeric(value) is None:
            raise ValueError('value is Integer or IntegerString Only')
        encoded = ''
        value = int(value)
        while value >= self._CHAR_NUM:
            div, mod = divmod(value, self._CHAR_NUM)
            encoded = self._CHARS[mod] + encoded
            value = div
        return self._CHARS[value] + encoded

    def decode(self, value):
        decoded = 0
        multi = 1
        if self._is_empty(value):
            raise ValueError('value is required')
        for v in reversed(str(value)):
            decoded += multi * self._CHARS.index(v)
            multi *= self._CHAR_NUM
        return decoded

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print 'Usage: python {0} value'.format(args[0])
        sys.exit()
    print 'before:{0}'.format(args[1])
    b58 = Base58()
    encoded = b58.encode(args[1])
    print 'encoded:{0}'.format(encoded)
    print 'decoded:{0}'.format(b58.decode(encoded))
    print b58.decode('asdfghjk')
    print b58.decode('1023456789')
