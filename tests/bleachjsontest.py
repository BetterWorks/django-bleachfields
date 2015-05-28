import unittest

from django.conf import settings
from bleachfields import BleachJSONField


class BleachJSONTest(unittest.TestCase):

    settings.configure()

    def test_simple_JSON(self):
        test_bleach_json = BleachJSONField()

        simple_json = {
            'glossary': {
                'title': 'example glossary',
                'GlossDiv': {
                    'title': 'S',
                    'GlossList': {
                        'GlossEntry': {
                            'ID': 'SGML',
                            'SortAs': 'SGML',
                            'GlossTerm': 'Standard Generalized Markup Lang.',
                            'Acronym': 'SGML',
                            'Abbrev': 'ISO 8879:1986',
                            'GlossDef': {
                                'para': 'A meta-markup language, used to \
                                    create markup languages such as DocBook.',
                                'GlossSeeAlso': ['GML', 'XML']
                            },
                            'GlossSee': 'markup'
                        }
                    }
                }
            }
        }

        simple_json_result = {
            'glossary': {
                'title': 'example glossary',
                'GlossDiv': {
                    'title': 'S',
                    'GlossList': {
                        'GlossEntry': {
                            'ID': 'SGML',
                            'SortAs': 'SGML',
                            'GlossTerm': 'Standard Generalized Markup Lang.',
                            'Acronym': 'SGML',
                            'Abbrev': 'ISO 8879:1986',
                            'GlossDef': {
                                'para': 'A meta-markup language, used to \
                                    create markup languages such as DocBook.',
                                'GlossSeeAlso': ['GML', 'XML']
                            },
                            'GlossSee': 'markup'
                        }
                    }
                }
            }
        }

        self.assertEqual(
            test_bleach_json._bleach_walk(simple_json),
            simple_json_result
        )

    def test_JSON_with_tags(self):
        test_bleach_json = BleachJSONField()

        with_tags = {
            'HTML': '<span>Tags are not allowed</span>',
            'More': {
                'Nested': {
                    'Tags': '<p>My first paragraph.</p>',
                    'Lists': ['GML', 'XML'],
                    'ListsWithTags': [
                        'Good &amp<evil> </evil>evil',
                        'Bleach is<example> &gt; </example>everything',
                        '<h1>This is a heading</h1>'
                    ]
                }
            }
        }

        with_tags_result = {
            'HTML': 'Tags are not allowed',
            'More': {
                'Nested': {
                    'Tags': 'My first paragraph.',
                    'Lists': ['GML', 'XML'],
                    'ListsWithTags': [
                        'Good & evil',
                        'Bleach is > everything',
                        'This is a heading'
                    ]
                }
            }
        }

        self.assertEqual(
            test_bleach_json._bleach_walk(with_tags),
            with_tags_result
        )

    def test_nested_JSON(self):
        test_bleach_json = BleachJSONField()

        nested_json = {
            'Crazy': ['<crazy> </crazy>'],
            'Lists of dictionaries!': [
                {'KPCB': ['<welcome> Fellows </welcome>']},
                {'Program': ['Hello &amp', '&gt; . &lt;']}
            ]
        }

        nested_json_result = {
            'Crazy': [' '],
            'Lists of dictionaries!': [
                {'KPCB': [' Fellows ']},
                {'Program': ['Hello &', '> . <']}
            ]
        }

        self.assertEqual(
            test_bleach_json._bleach_walk(nested_json),
            nested_json_result
        )

if __name__ == '__main__':
    unittest.main()
