import unittest
from text import Text

class TestText(unittest.TestCase):

    def setUp(self):
        self.text = Text("Hello, World!")

    def test_getitem_index(self):
        self.assertEqual(self.text[0], 'H')
        self.assertEqual(self.text[7], 'W')
        self.assertEqual(self.text[-1], '!')

    def test_getitem_slice(self):
        self.assertEqual(self.text[0:5], 'Hello')
        self.assertEqual(self.text[7:12], 'World')
        self.assertEqual(self.text[:5], 'Hello')
        self.assertEqual(self.text[7:], 'World!')
        self.assertEqual(self.text[::2], 'Hlo ol!')

    def test_add(self):
        new_text = self.text + " How are you?"
        self.assertEqual(str(new_text), "Hello, World! How are you?")

    def test_iadd(self):
        self.text += " How are you?"
        self.assertEqual(str(self.text), "Hello, World! How are you?")

    def test_contains(self):
        self.assertTrue('Hello' in self.text)
        self.assertTrue('World' in self.text)
        self.assertFalse('Python' in self.text)

    def test_iter(self):
        chars = [char for char in self.text]
        self.assertEqual(chars, list("Hello, World!"))

if __name__ == '__main__':
    unittest.main()