import unittest

from bleachfields import BleachCharField


class BleachCharFieldTest(unittest.TestCase):

    def test_pre_save(self):
        test_char_field = BleachCharField()
        test_char_field.attname = 'number'

        simple_html = '<span>123456789</span>'
        simple_html_result = '123456789'

        setattr(test_char_field, 'number', simple_html)

        self.assertEqual(
            test_char_field.pre_save(test_char_field, None),
            simple_html_result
        )
