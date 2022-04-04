import re
import sys

from bleach import clean, ALLOWED_ATTRIBUTES

ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')


# unescape was moved to the html module in python 3.4
if sys.version_info > (3, 4):
    from html import unescape
else:
    from six.moves import html_parser
    unescape = html_parser.HTMLParser().unescape


class BleachField(object):

    # Parser for unescaping HTML entities

    def __init__(self, tags=(), strip=True, attributes=ALLOWED_ATTRIBUTES, *args, **kwargs):
        super(BleachField, self).__init__(*args, **kwargs)
        self.strip = strip
        self.tags = tags
        self.attributes = attributes

    def clean_text(self, text):
        '''Clean text using bleach.'''
        if text is None:
            return ''
        text = unescape(text)
        text = re.sub(ILLEGAL_CHARACTERS_RE, '', text)
        if '<' in text:
            text = clean(text, tags=self.tags, strip=self.strip, attributes=self.attributes)
        return text
