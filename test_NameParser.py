import unittest
import NameParser


class TestNameParser(unittest.TestCase):
    def test_pascalConversion(self):
        self.assertEqual(
            NameParser.pascalConversion("foo-bar-baz"),
            "FooBarBaz"
        )

    def test_properCapConversion(self):
        self.assertEqual(
            NameParser.properCapConversion("for-foo-bar-and-baz"),
            "For Foo Bar and Baz"
        )

    def test_underCapConversion(self):
        self.assertEqual(
            NameParser.underCapConversion("for-foo-bar-and-baz"),
            "For_Foo_Bar_and_Baz"
        )

    def test_camelConversion(self):
        self.assertEqual(
            NameParser.camelConversion("foo-bar-baz"),
            "fooBarBaz"
        )

    def test_lowerUnder(self):
        self.assertEqual(
            NameParser.lowUnderConversion("foo-bar-baz"),
            "foo_bar_baz"
        )


if __name__ == '__main__':
    unittest.main()
