import unittest

from bleachfields import BleachField


class BleachFieldTest(unittest.TestCase):

    def test_simple_tag(self):
        test_bleach_field = BleachField()

        simple_html = '<span>Tags are not allowed</span>'
        simple_html_result = 'Tags are not allowed'

        self.assertEqual(
            test_bleach_field.clean_text(simple_html),
            simple_html_result
        )

    def test_nested_tags(self):
        test_bleach_field = BleachField()

        html_nested = ('<!DOCTYPE html><html><body><h1>My First Heading</h1> '
          '<p>My first paragraph.</p></body></html>')
        html_nested_result = 'My First Heading My first paragraph.'
        
        self.assertEqual(
            test_bleach_field.clean_text(html_nested),
            html_nested_result
        )

    def test_multiline_tags(self):
        test_bleach_field = BleachField()

        html_multiline = """ <h1>This is a heading</h1>
                                  <h2>This is a heading</h2>
                                  <h3>This is a heading</h3>
                              """
        html_multiline_result = """ This is a heading
                                  This is a heading
                                  This is a heading
                              """

        self.assertEqual(
            test_bleach_field.clean_text(html_multiline),
            html_multiline_result
        )

    def test_escape_and_bleach(self):
        test_bleach_field = BleachField()

        html_with_escape_one = ('Bleach is <example>&gt; '
            '</example> everything.')
        html_with_escape_one_result = 'Bleach is > everything.'

        html_with_escape_two = 'Good &amp<evil></evil> evil'
        html_with_escape_two_result = 'Good & evil'

        self.assertEqual(
            test_bleach_field.clean_text(html_with_escape_one),
            html_with_escape_one_result
        )

        self.assertEqual(
            test_bleach_field.clean_text(html_with_escape_two),
            html_with_escape_two_result
        )


if __name__ == '__main__':
    unittest.main()
