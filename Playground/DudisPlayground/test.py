#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate


def main():
    to_translate = 'היי'
    print(translate(to_translate))
    print(translate(to_translate,'fr'))
    print(translate(to_translate, 'ru'))

if __name__ == '__main__':
    main()
