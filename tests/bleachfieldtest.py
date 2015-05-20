import unittest

from bleachfields import BleachField


class BleachFieldTest(unittest.TestCase):

    def test_simple_tag(self):
        test_bleach_field = BleachField()

        self.simple_html = '<span>Tags are not allowed</span>'
        self.simple_html_result = 'Tags are not allowed'

        self.assertEqual(
            test_bleach_field.clean_text(self.simple_html),
            self.simple_html_result
        )

    def test_nested_tags(self):
        test_bleach_field = BleachField()

        self.html_nested = \
            """<!DOCTYPE html><html><body><h1>My First Heading</h1>
               <p>My first paragraph.</p></body></html>"""
        self.html_nested_result = \
            'My First Heading\n               My first paragraph.'

        self.assertEqual(
            test_bleach_field.clean_text(self.html_nested),
            self.html_nested_result
        )

    def test_multiline_tags(self):
        test_bleach_field = BleachField()

        self.html_multiline = """ <h1>This is a heading</h1>
                                  <h2>This is a heading</h2>
                                  <h3>This is a heading</h3>
                              """
        self.html_multiline_result = """ This is a heading
                                  This is a heading
                                  This is a heading
                              """

        self.assertEqual(
            test_bleach_field.clean_text(self.html_multiline),
            self.html_multiline_result
        )

    def test_escape_and_bleach(self):
        test_bleach_field = BleachField()

        self.html_with_escape_one = \
            'Bleach is <example>&gt;</example> everything.'
        self.html_with_escape_one_result = 'Bleach is > everything.'

        self.html_with_escape_two = 'Good &amp<evil></evil> evil'
        self.html_with_escape_two_result = 'Good & evil'

        self.assertEqual(
            test_bleach_field.clean_text(self.html_with_escape_one),
            self.html_with_escape_one_result
        )

        self.assertEqual(
            test_bleach_field.clean_text(self.html_with_escape_two),
            self.html_with_escape_two_result
        )


if __name__ == '__main__':
    unittest.main()
