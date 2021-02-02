import json


class Dictionary():
    """ Creates a Dictionary object from json file

    """
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as f:
            self.data = json.loads(f.read())

    def __repr__(self):
        for key, value in self.data.items():
            print(key + '    ....    ' + value)

    def valid_char(self, char):
        """ Determine whether a character is a valid dictionary member """
        if char.lower() in self.data.keys():
            return True
        return False

    def valid_morse(self, morse_char):
        """ Determine whether a Morse code character is a valid
        dictionary member

        """
        if morse_char in self.data.values():
            return True
        elif morse_char == '':
            return True
        return False
