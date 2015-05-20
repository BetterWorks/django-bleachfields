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
        return self._clean_text(text, tuple(self.tags), self.strip)

    @staticmethod
    def _clean_text(text, tags, strip):
        return BleachField._parser.unescape(
            clean(text, tags=tags, strip=strip)
        )
