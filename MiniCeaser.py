import re
import string

def mc(*message:str, key:int=13)->str:
    '''Ceaser cipher mini'''
    key = key % 26
    message ="".join(message)
    message = re.sub("\.", "X", message)
    message = re.sub("[^A-Z]", "", message.upper())
    translation = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[key:] + string.ascii_uppercase[:key])
    message = message.translate(translation)
    return str(message)

names = ("Andrew", "Ben")

print(mc("hello class", "this is a test", "This can take many arguments", str(names), key=414))