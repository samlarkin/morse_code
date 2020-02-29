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
