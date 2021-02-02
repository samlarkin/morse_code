import warnings


class Message():
    """ Message objects are either text or Morse code messages
    message argument should be a string input
    dictionary_path argument should be a Dictionary object

    """
    def __init__(self, message, dictionary):
        self.input_string = self.get_valid_input(message)
        self.dictionary = dictionary
        self.output_string = ''

    @staticmethod
    def get_valid_input(message):
        """ Return string from input, regardless of type(message) """
        if isinstance(message, str):
            input_string = message
        else:
            warnings.warn(f'message should be str, not {type(message)}')
            input_string = str(message)
        return input_string


class Text(Message):
    """ Stores text in a Message object
    Can be encoded to Morse code

    """
    def encode(self):
        """ Encodes text to Morse code
        Returns Morse object

        """
        input_list = list(self.input_string)
        output_list = []
        while input_list:
            char = input_list.pop(0)
            char = char.lower()
            valid = self.dictionary.valid_char(char)
            if valid:
                output_list.append(self.dictionary.data[char])
            else:
                raise ValueError('Invalid character in message '
                                 '(no match found in dictionary)')
            if len(input_list) > 0:
                output_list.append(' ')

        self.output_string = ''.join(output_list)
        return Morse(self.output_string, self.dictionary)


class Morse(Message):
    """ Stores Morse code in a Message object
    Can be decoded to plain text

    """
    def decode(self):
        """ Decodes Morse code to text
        Returns Text object

        """
        input_words = self.input_string.split('  ')
        working_list = []
        while input_words:
            word = input_words.pop(0)
            morse_chars = word.split(' ')
            while morse_chars:
                char_in_word = []
                morse_char = morse_chars.pop(0)
                valid = self.dictionary.valid_morse(morse_char)
                if valid:
                    for key, value in self.dictionary.data.items():
                        if morse_char == value:
                            char = key
                    char_in_word.append(char)
                else:
                    raise ValueError(
                        f'{morse_char} is not a valid morse '
                        'code character '
                        '(no match found in dictionary).'
                    )
                if len(morse_char) > 0:
                    working_list.append(''.join(char_in_word))

            if len(input_words) > 0:
                working_list.append(' ')

        self.output_string = ''.join(working_list)
        return Text(self.output_string, self.dictionary)
