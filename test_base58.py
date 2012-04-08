#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base58 import Base58
from nose.tools import *

class TestBase58: 

    b58 = Base58()

    @raises(ValueError)
    def test_encode_blank(self):
        self.b58.encode('')

    @raises(ValueError)
    def test_encode_none(self):
        self.b58.encode(None)

    @raises(ValueError)
    def test_encode_string(self):
        self.b58.encode('asdfghjkl')

    @raises(ValueError)
    def test_encode_integer_and_string(self):
        self.b58.encode('1234asdfg')

    def test_encode_strinteger(self):
        eq_(self.b58.encode('123456789'), 'bUKpk')

    def test_encode_integer(self):
        eq_(self.b58.encode(123456789), 'bUKpk')

    @raises(ValueError)
    def test_decode_blank(self):
        self.b58.decode('')

    @raises(ValueError)
    def test_decode_node(self):
        self.b58.decode(None)

    def test_decode_string(self):
        eq_(self.b58.decode('asdfghjk'), 20869681207839)

    def test_decode_integer(self):
        eq_(self.b58.decode(123456789), 2286136885086)
   
    def test_decode_stringinteger(self):
        eq_(self.b58.decode('123456789'), 2286136885086)
    
