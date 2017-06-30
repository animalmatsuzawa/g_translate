# coding: utf-8
import argparse
#import random
from .translate import *

"""
socks経由でrequests使う場合は以下必要
pip install -U requests[socks]
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Translate using google translation.')

    parser.add_argument('strings', \
        action='store', \
        nargs=None, \
        const=None, \
        default=None, \
        type=str, \
        choices=None, \
        help='Source strings.(- is stdin input)', \
        metavar=None)

    parser.add_argument('-sl', '--src-lang', \
        action='store', \
        const=None, \
        default=['auto'], \
        type=str, \
        choices=None, \
        help='Source language. (default: auto)', \
        metavar=None)

    parser.add_argument('-tl', '--to-lang', \
        action='store', \
        #nargs='+', \
        const=None, \
        default=['en'], \
        type=str, \
        choices=None, \
        help='Destination language. (default: en)', \
        metavar=None)

    parser.add_argument('-p', '--proxy', \
        action='store', \
        const=None, \
        default=None, \
        type=str, \
        choices=None, \
        help='proxy. (ex -p http://proxy:port)', \
        metavar=None)


    args = parser.parse_args()

    # ランダムでiphone/webを切り分け
    #_mode = bool(random.getrandbits(1))
    _mode = False
    if args.proxy is not None:
         _proxys = {'http':args.proxy, 'https':args.proxy}
    else:
         _proxys = None

    out = ''
    fast_lang = None
    if args.strings == '-':
        sentence = sys.stdin.read()
    else:
        sentence = " ".join(args.strings)

    if fast_lang is None:
        fast_lang = args.src_lang

    _transe, _lang = google_translate( \
                         sentence , \
                         mode=_mode, \
                         to_lang=args.to_lang, \
                         src_lang=args.src_lang, \
                         proxy=_proxys)
    out = out + _transe
    print( out )

