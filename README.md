# g_translate
Translate using google translation

## install
~~~
python ./setup.py install
~~~
## Usage
~~~
python -m g_translate -h
usage: __main__.py [-h] [-sl SRC_LANG] [-tl TO_LANG] [-p PROXY] strings

Translate using google translation.

positional arguments:
  strings               Source strings.(- is stdin input)

optional arguments:
  -h, --help            show this help message and exit
  -sl SRC_LANG, --src-lang SRC_LANG
                        Source language. (default: auto)
  -tl TO_LANG, --to-lang TO_LANG
                        Destination language. (default: en)
  -p PROXY, --proxy PROXY
                        proxy. (ex -p http://proxy:port)
~~~

~~~
echo "Hello world" | python -m g_translate -tl ja -
python -m g_translate -tl ja "Hello world"
python -m g_translate -tl ja -p socks5://locahhost:9050 "Hello world"
~~~

~~~
from g_translate import google_translate

print google_translate( "Hello world", src_lang="en", to_lang="ja" )
~~~
