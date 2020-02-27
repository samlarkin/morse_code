import string
import os
import json

class Dictionary(object):
    def __init__(self,filepath):
        self.filepath = filepath
        self.data = json.load(open(self.filepath))

    def validChar(self, char):
        if char in self.data.keys():
            valid = True
        elif char in list(string.ascii_uppercase):
            char = char.lower()
            valid = True
        else:
            valid = False
        output = [char, valid]
        return output

    def validMorse(self, morse):
        if morse in self.data.values():
            for key, value in self.data.items():
                if morse == value:
                    output = [morse, key, True]
        elif morse == '':
            output = [morse, morse, True]
        else:
            output = [morse, None, False]
        return output

class Message(object):
    def __init__(self, message, dictionary):
        self.input_string = self.getValidInput(message)
        self.dictionary = dictionary

    def getValidInput(self, message):
        if isinstance(message, str):
            input_string = message
        else:
            input_string = str(message)
        return input_string    

    def atEnd(self, count, list_of_items):
        if count < len(list_of_items):
            return False
        else:
            return True

    def write(self, filepath, content):
        with open(filepath, 'w+') as f:
            f.write(content)

class Text(Message):
    def encode(self):
        input_list = list(self.input_string)
        working_list = []
        count = 0
        for char in input_list:
            count += 1
            [char, valid] = self.dictionary.validChar(char)
            if valid:
                working_list.append(self.dictionary.data[char])
            else:
                raise ValueError('Invalid character in message '
                                 '(no match found in dictionary)')                                
            if not self.atEnd(count, input_list):
                working_list.append(' ')
        self.output_string = ''.join(working_list)
        print(self.output_string)
        return Morse(self.output_string, self.dictionary)

class Morse(Message):
    def decode(self):
        input_words = self.input_string.split('  ')
        working_list = []
        count = 0
        for word in input_words:
            count += 1
            morse_chars = word.split(' ')
            for char in morse_chars:
                [char, key, valid] = self.dictionary.validMorse(char)
                if valid:
                    working_list.append(key)
                else:
                    raise ValueError('Not a valid morse code character '
                                     '(no match found in dictionary).')
            if not self.atEnd(count, input_words):
                working_list.append(' ')
        self.output_string = ''.join(working_list)  
        print(self.output_string)
        return Text(self.output_string, self.dictionary)
