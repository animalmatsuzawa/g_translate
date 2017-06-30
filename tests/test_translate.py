# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from g_translate import google_trans
from g_translate import google_translate

class TransrateTestSuite(unittest.TestCase):

    """Basic test cases."""

    def test_transrate_en_jp(self):
        src = "Hello World"
        dest = "こんにちは世界"
        to_lang = "ja"
        out, src_lang = google_translate( src, to_lang=to_lang )
        assert out == dest

    def test_transrate_jp_en(self):
        src = "こんにちは世界"
        dest = "Hello World"
        to_lang = "en"
        out, src_lang = google_translate( src, to_lang=to_lang )
        assert out == dest

    def test_transrate_en_jp_web(self):
        src = "Hello World"
        dest = "こんにちは世界"
        to_lang = "ja"
        out, src_lang = google_translate( src, to_lang=to_lang, mode = False )
        assert out == dest

    def test_transrate_jp_en_web(self):
        src = "こんにちは世界"
        dest = "Hello World"
        to_lang = "en"
        out, src_lang = google_translate( src, to_lang=to_lang, mode = False )
        assert out == dest



if __name__ == '__main__':
    unittest.main()
