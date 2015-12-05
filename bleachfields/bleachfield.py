import re
import six

from bleach import clean

if six.PY3:
    from html.parser import HTMLParser
else:
    from HTMLParser import HTMLParser


ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')


class BleachField(object):

    # Parser for unescaping HTML entities
    _parser = HTMLParser()

    def __init__(self, tags=(), strip=True, *args, **kwargs):
        super(BleachField, self).__init__(*args, **kwargs)
        self.strip = strip
        self.tags = tags

    def clean_text(self, text):
        '''Clean text using bleach.'''
        if text is None:
            return ''
        text = re.sub(ILLEGAL_CHARACTERS_RE, '', text)
        if '<' in text or '&lt' in text:
            text = clean(text, tags=self.tags, strip=self.strip)
        return self._parser.unescape(text)
