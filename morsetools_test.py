import morsetools
import os

wd = os.getcwd()
dictionary_path = os.path.join(wd,'dictionaries','morse_dictionary.json')
dictionary = morsetools.Dictionary(dictionary_path)

test_string = 'the quick brown fox jumps over the lazy dog'
test_text = morsetools.message.Text(test_string, dictionary)
textpath = os.path.join(wd, 'outputs', 'test_text.txt')
test_text.write(textpath)
test_morse = test_text.encode()
outpath = os.path.join(wd, 'outputs', 'test_morse.txt')
test_morse.write(outpath)
test_bounceback = test_morse.decode()
