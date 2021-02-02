import unittest
from message import Text, Morse
from dictionary import Dictionary


class TestMorseTools(unittest.TestCase):
    """ Test case

    """
    def setUp(self):
        """ setUp run before each test """
        self.test_string = 'the quick brown fox jumps over the lazy dog'
        self.dictionary = Dictionary('morse_dictionary.json')

    def test_encode_decode(self):
        """ Test encode/decode loop """
        test_text = Text(self.test_string, self.dictionary)
        test_text.encode()
        test_morse = Morse(test_text.output_string, self.dictionary)
        test_morse.decode()
        result = test_morse.output_string
        self.assertEqual(self.test_string, result)


if __name__ == '__main__':
    unittest.main()
