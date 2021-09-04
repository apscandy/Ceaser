#!/usr/bin/python3
'''
NAME
    Ceaser.py - cipher and print message

SYNOPSIS
    ...$ ./Ceaser.py -m "Hello" -k 12
    ...$ ./Ceaser.py --message "Hello" --key 12
    ...$ ./Ceaser.py -h

DESCRIPTION
    Caesar cipher is to replace each plaintext letter with a
     different one a fixed number of places down the alphabet.
    This program Has a right shift default I.E. A becomes B with a fixed key of 1,
     you shift left with a negative key I.E. -1 B then becomes A

SEE ALSO
    https://en.wikipedia.org/wiki/Caesar_cipher
    https://github.com/apscandy/ICTPRG405-Python/blob/main/AT1/Ceaser.py

BUGS
    Beware of entering `@#` in the Cli as bash, terminal and powershell try to interpret `@#` and will brake the script
'''

import re
import string
import argparse
import os

def main()->str:
    '''
    Takes args from the CLI i.e. `python3 Ceaser.py [-k "key"]... [-m "message"]...`

    Parameters:
        key (int): A number between -26 and 26
        message (str): message to be converted

    Returns:
        message (str): converted string

    Doctest:
        ...$ ./Ceaser.py -m "Hello" -k 12
        Message is: TQXXA

    '''
    parser = argparse.ArgumentParser(description="Andrew's Cipher system")
    parser.add_argument("-k", "--key",required=True ,type=int, help="int: Enter a number between -26 and 26 to Encrypt/Decrypt")
    parser.add_argument("-m", "--message",required=True, type=str, help="str: Enter a message to be Encrypt/Decrypt")
    args = parser.parse_args()
    key:int = args.key
    message:str = args.message

    key_check(key)
    message = convert_to_ceasar(message)
    message = encrypt_caesar(key, message)
    return message


def main_ut(key:int, messsage:str)->str:
    '''
    Testing function for unittest module calls convert_to_ceasar and encrypt_caesar

    Parameter:
        key (int): A number between -26 and 26
        message (str): message to be converted

    Returns:
        message (str): converted string from rot

    Example:
        >>> message = "HELLO"
        >>> key = 13
        >>> encrypt_caesar(key,message)
        'URYYB'
    '''
    messsage = convert_to_ceasar(messsage)
    messsage = encrypt_caesar(key, messsage)
    return messsage


def clear_terminal()->None:
    '''Clears the terminal for a clean output'''
    if os.name == 'nt': os.system("cls")
    elif os.name == 'posix': os.system("clear")


def key_check(key:int)->None:
    '''check if key is in range -26 to 26'''
    if not -26 <= int(key) < 27:
        print("Please enter a key between -26 and 26\n")
        exit()


def convert_to_ceasar(message:str)->str:
    '''
    Converts message:str to upper case and removes non alpha-characters

    Pseudo code:
        Convert text to uppercase
        Replaces fullstops with X
        Removes spaces
        Removes numbers
        Removes special characters

    Parameter:
        message (str): message to be converted

    Returns:
        message (str): converted string

    Example:
        >>> message = "Hello"
        >>> convert_to_ceasar(message)
        'HELLO'
    '''
    message = re.sub("\.", "X", message) # Replaces fullstops(.) with X
    message = re.sub("[^A-Z]", "", message.upper()) #Removes anything that is not a [A-Z] and sets message to uppercase
    return str(message)


def encrypt_caesar(key:int, message:str)->str:
    '''
    Shifts message:str by using key:int to cipher message:str

    Pseudo code:
        Takes key and message parameter
        Shifts letters in message by the key number
        Makes translation table and uses key for shift value
        Translation table looks up new value then message is saved to new value
        Returns ciphered message

    Parameter:
        key (int): A number between -26 and 26
        message (str): The message to be encoded/decoded

    Returns:
        message (str): encoded/decoded message

    Example:
        >>> message = "Hello"
        >>> message = convert_to_ceasar(message)
        >>> key = 13
        >>> encrypt_caesar(key, message)
        'URYYB'
    '''
    translation = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[key:] + string.ascii_uppercase[:key])
    message = message.translate(translation)
    return str(message)


if __name__=="__main__":
    clear_terminal()
    output = main()
    print(f"Message is: {output}\n")
