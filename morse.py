"""
morse.py
author: Sam Larkin
url: https://github.com/samlarkin/morse_code

Module written as a learning exercise
Encodes text to Morse code and vice versa
"""
import string
import json


class Dictionary():
    """
        Creates a Dictionary object from data stored on disk
        Dictionary data on disk is stored in json format
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = json.load(open(self.filepath))

    def valid_char(self, char):
        """
        Determine whether a character is a valid dictionary member
        """
        if char in self.data.keys():
            valid = True
        elif char in list(string.ascii_uppercase):
            char = char.lower()
            valid = True
        else:
            valid = False
        output = [char, valid]
        return output

    def valid_morse(self, morse):
        """
        Determine whether a Morse code character is a valid dictionary member
        """
        if morse in self.data.values():
            for key, value in self.data.items():
                if morse == value:
                    output = [morse, key, True]
        elif morse == '':
            output = [morse, morse, True]
        else:
            output = [morse, None, False]
        return output


class Message():
    """
    Message objects are either text or Morse code messages
    message argument should be a string input
    dictionary argument should be a Dictionary object
    """
    def __init__(self, message, dictionary):
        self.input_string = self.get_valid_input(message)
        self.dictionary = dictionary
        self.output_string = ''

    @classmethod
    def get_valid_input(cls, message):
        """
        Return string from input, regardless of type(message)
        """
        if isinstance(message, str):
            input_string = message
        else:
            input_string = str(message)
        return input_string

    @classmethod
    def at_end(cls, count, list_of_items):
        """
        Check whether a loop has reached the last item in an interable
        """
        if count < len(list_of_items):
            at_end = False
        else:
            at_end = True
        return at_end

    def write(self, filepath):
        """
        Write a message to a file
        """
        with open(filepath, 'w+') as written_file:
            written_file.write(self.input_string)


class Text(Message):
    """
    Stores text in a Message object
    Can be encoded to Morse code
    """
    def encode(self):
        """
        Encodes text to Morse code
        Prints string of Morse code
        Returns Morse object
        """
        input_list = list(self.input_string)
        working_list = []
        count = 0
        for char in input_list:
            count += 1
            [char, valid] = self.dictionary.valid_char(char)
            if valid:
                working_list.append(self.dictionary.data[char])
            else:
                raise ValueError('Invalid character in message '
                                 '(no match found in dictionary)')
            if not self.at_end(count, input_list):
                working_list.append(' ')
        self.output_string = ''.join(working_list)
        print(self.output_string)
        return Morse(self.output_string, self.dictionary)


class Morse(Message):
    """
    Stores Morse code in a Message object
    Can be decoded to plain text
    """
    def decode(self):
        """
        Decodes Morse code to text
        Prints string of text
        Returns Text object
        """
        input_words = self.input_string.split('  ')
        working_list = []
        count = 0
        for word in input_words:
            count += 1
            morse_chars = word.split(' ')
            for char in morse_chars:
                [char, key, valid] = self.dictionary.valid_morse(char)
                if valid:
                    working_list.append(key)
                else:
                    raise ValueError('Not a valid morse code character '
                                     '(no match found in dictionary).')
            if not self.at_end(count, input_words):
                working_list.append(' ')
        self.output_string = ''.join(working_list)
        print(self.output_string)
        return Text(self.output_string, self.dictionary)
