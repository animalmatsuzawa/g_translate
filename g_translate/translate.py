# -*- coding: utf-8 -*-

import sys
import requests
import ctypes
from StringIO import StringIO

def google_translate( sentence, src_lang='auto', to_lang='en', mode = False, proxy=None ):
    """
    Translate by google translation
    @param sentence: source text
    @param mode: (optional) True:Use API for iphone/False:Use API for iphone WebApp
    @param src_lang: (optional) source langage 
        'auto': auto detect
        'en': english
        'jp': japanease
    @param to_lang: (optional) to langage (default 'en')
        'en': english
        'jp': japanease
    @param proxy: (optional) use proxy( {"http":"http://proxy.host:8080", "https":"http://proxy.host:8080"} )
    @return: source: langage, result: text

    """
    out = ''
    fast_lang = None
    if len(sentence) > 5000:
        _input = StringIO(sentence)
        sentence = ''
        flag = False

        fast_lang = src_lang
        
        for line in iter(_input.readline, ""):
            if len(sentence + line) > 5000:
                flag = True
            else:
                sentence = sentence + line
            if flag == True:
                _transe, _lang = google_trans( \
                                     sentence , \
                                     mode=mode, \
                                     to_lang=to_lang, \
                                     src_lang=fast_lang, \
                                     proxy=proxy)
                fast_lang = _lang
                out = out + _transe
                sentence = line
                flag = False

    if fast_lang is None:
        fast_lang = src_lang

    _transe, _lang = google_trans( \
                         sentence , \
                         mode=mode, \
                         to_lang=to_lang, \
                         src_lang=fast_lang, \
                         proxy=proxy)
    out = out + _transe
    return out, fast_lang

def google_trans( sentence, src_lang='auto', to_lang='en', mode = False, proxy=None ):
    def _calc_tk(source):
        """
        calculate tk parameter 
        """
        """Reverse engineered cross-site request protection."""
        # Source: https://github.com/soimort/translate-shell/issues/94#issuecomment-165433715
        # Source: http://www.liuxiatool.com/t.php

        PY2 = int(sys.version[0]) == 2

        tkk = [406398, 561666268 + 1526272306]
        b = tkk[0]

        if PY2:
            d = map(ord, source)
        else:
            d = source.encode('utf-8')

        def RL(a, b):
            for c in range(0, len(b) - 2, 3):
                d = b[c + 2]
                d = ord(d) - 87 if d >= 'a' else int(d)
                xa = ctypes.c_uint32(a).value
                d = xa >> d if b[c + 1] == '+' else xa << d
                a = a + d & 4294967295 if b[c] == '+' else a ^ d
            return ctypes.c_int32(a).value

        a = b

        for di in d:
            a = RL(a + di, "+-a^+6")

        a = RL(a, "+-3^+b+-f")
        a ^= tkk[1]
        a = a if a >= 0 else ((a & 2147483647) + 2147483648)
        a %= pow(10, 6)

        tk = '{0:d}.{1:d}'.format(a, a ^ b)
        return tk

    if isinstance( sentence, unicode):
        sentence = sentence.encode('utf-8')
    if isinstance( src_lang, unicode):
        src_lang = src_lang.encode('utf-8')
    if isinstance( to_lang, unicode):
        to_lang = to_lang.encode('utf-8')
    lang = None
    transtr = None
    url = "https://translate.google.com/translate_a/single"
    if mode:
        # Use API for iphone
        headers = {
            "Host": "translate.google.com",
            "Accept": "*/*",
            "Cookie": "",
            "User-Agent": "GoogleTranslate/5.9.59004 (iPhone; iOS 10.2; ja; iPhone9,1)",
            "Accept-Language": "ja-jp",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        }

        params = {
            "client": "it",
            "dt": ["t", "rmt", "bd", "rms", "qca", "ss", "md", "ld", "ex"],
            "otf": "2",
            "dj": "1",
            #"q": sentence,
            "ie": "UTF-8",
            "oe": "UTF-8",
            #from
            "sl": src_lang,
            #to
            "hl": to_lang,
            "tl": to_lang,
        }
        # GETの場合、パラメータにqを指定
        # POSTの場合、データにqを指定
        data = {"q":sentence}
        response = requests.post(
                url=url,
                headers=headers,
                params=params,
                data=data,
                proxies=proxy,
            )
        if 200 <= response.status_code and response.status_code < 300:
            res_json = response.json()
            #print( res_json )
            transtr = ''
            lang = res_json["src"]
            for trans in res_json["sentences"]:
                if "trans" in trans:
                    transtr += trans["trans"]
    else:
        # Use API for iphone WebApp
        headers = {
            "Host": "translate.google.com",
            "Accept": "*/*",
            "Cookie": "",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept-Language": "ja-jp",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        }

        params = {
            "client": "t",
            "dt": ["at", "bd", "ex", "ld", "md", "qca", "rw", "rm", "ss", "t"],
            "ssel":"0",
            "tsel":"0",
            "kc":"1",
            #"q": sentence,
            "ie": "UTF-8",
            "oe": "UTF-8",
            #from
            "sl": src_lang,
            #to
            "hl": "en",
            "tl": to_lang, 
            "tk": _calc_tk(sentence),
        }
        # GETの場合、パラメータにqを指定
        # POSTの場合、データにqを指定
        data = {"q":sentence}
        response = requests.post(
                url=url,
                headers=headers,
                params=params,
                data=data,
                proxies=proxy,
            )
        if 200 <= response.status_code and response.status_code < 300:
            res_json = response.json()
            transtr = ''
            #print( res_json )
            lang = res_json[2]
            
            for trans in res_json[0]:
                if trans[0] is not None:
                    transtr += trans[0]
    if transtr is not None:
       transtr = transtr.encode('utf-8')

    return transtr, lang

