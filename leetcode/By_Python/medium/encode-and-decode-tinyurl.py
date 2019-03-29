#!/usr/bin/env python
# coding=UTF-8
'''
@Author: LogicJake
@Date: 2019-03-29 11:00:29
@LastEditTime: 2019-03-29 11:00:59
'''
import string
import random


class Codec:
    alphabet = string.ascii_letters + '0123456789'
    code2url = {}
    url2code = {}

    def encode(self, longUrl):
        while (longUrl not in self.url2code):
            code = ''.join(random.choice(self.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl.split('/')[-1]]
