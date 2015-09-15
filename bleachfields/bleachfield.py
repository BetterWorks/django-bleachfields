from HTMLParser import HTMLParser

from bleach import clean


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
        if '<' in text or '&lt' in text:
            text = clean(text, tags=self.tags, strip=self.strip)
        return self._parser.unescape(text)
