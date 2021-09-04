#!/usr/bin/python3
'''
NAME
    Tests.py - automated testing

SYNOPSIS
    ...$ ./Tests.py

DESCRIPTION
    Tests automates 30 tests with a set of strings and checks if the output from the function is correct.

TESTS
    "abc"
    "This is a Test with spaces"
    "This is a Test with numbers 1234"
    "This is a Test with fullstops ..."
    "This is a Test with special chars _!@#$%^&*()"
    "This is a Test with a url https://realpython.com/python-testing/"
    "This is a Test with quotes" ""
    "This is a Test with an email andrewclarke.aron@gmail.com"
    "This is a Test with a lot of spaces                  "
    "This is a Test with a happy face :)"

EXPECTED OUTPUT
    ...$ ./Tests.py
    ..............................
    ----------------------------------------------------------------------
    Ran 30 tests in 0.001s

    OK

UNEXPECTED OUTPUT
    ...$ ./Tests.py
    F.............................
    ======================================================================
    FAIL: test_1 (__main__.Task_1_)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/Users/andy/Documents/GitHub/ICTPRG405-Python/AT1/Tests.py", line 59, in test_1
        self.assertEqual(convert_to_ceasar(unit_test_string_01),"ABC1")
    AssertionError: 'ABC' != 'ABC1'
    - ABC
    + ABC1
    ?    +


    ----------------------------------------------------------------------
    Ran 30 tests in 0.001s

    FAILED (failures=1)

SEE ALSO
    https://github.com/apscandy/ICTPRG405-Python/blob/main/AT1/Tests.py
'''

import unittest
from Ceaser import convert_to_ceasar, encrypt_caesar, main_ut

unit_test_string_01 = "abc"
unit_test_string_02 = "This is a Test with spaces"
unit_test_string_03 = "This is a Test with numbers 1234"
unit_test_string_04 = "This is a Test with fullstops ..."
unit_test_string_05 = "This is a Test with special chars _!@#$%^&*()"
unit_test_string_06 = "This is a Test with a url https://realpython.com/python-testing/"
unit_test_string_07 = "This is a Test with quotes" ""
unit_test_string_08 = "This is a Test with an email andrewclarke.aron@gmail.com"
unit_test_string_09 = "This is a Test with a lot of spaces                  "
unit_test_string_10 = "This is a Test with a happy face :)"

class Task_1_(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_01),"ABC")
    
    def test_2(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_02),"THISISATESTWITHSPACES")

    def test_3(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_03),"THISISATESTWITHNUMBERS")

    def test_4(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_04),"THISISATESTWITHFULLSTOPSXXX")
    
    def test_5(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_05),"THISISATESTWITHSPECIALCHARS")

    def test_6(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_06),"THISISATESTWITHAURLHTTPSREALPYTHONXCOMPYTHONTESTING")

    def test_7(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_07),"THISISATESTWITHQUOTES")

    def test_8(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_08),"THISISATESTWITHANEMAILANDREWCLARKEXARONGMAILXCOM")

    def test_9(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_09),"THISISATESTWITHALOTOFSPACES")
    
    def test_10(self):
        self.assertEqual(convert_to_ceasar(unit_test_string_10),"THISISATESTWITHAHAPPYFACE")

  
class Task_2_(unittest.TestCase):
    
    def test_11(self):
        self.assertEqual(encrypt_caesar(13,unit_test_string_01.upper()),"NOP")
    
    def test_12(self):
        self.assertEqual(encrypt_caesar(13, unit_test_string_02.upper()),"GUVF VF N GRFG JVGU FCNPRF")
    
    def test_13(self):
        self.assertEqual(encrypt_caesar(13, unit_test_string_03.upper()),"GUVF VF N GRFG JVGU AHZOREF 1234")

    def test_14(self):
        self.assertEqual(encrypt_caesar(13, unit_test_string_04.upper()),"GUVF VF N GRFG JVGU SHYYFGBCF ...")

    def test_15(self):
        self.assertEqual(encrypt_caesar(13, unit_test_string_05.upper()),"GUVF VF N GRFG JVGU FCRPVNY PUNEF _!@#$%^&*()")

    def test_16(self):
        self.assertEqual(encrypt_caesar(13, unit_test_string_06.upper()),"GUVF VF N GRFG JVGU N HEY UGGCF://ERNYCLGUBA.PBZ/CLGUBA-GRFGVAT/")

    def test_17(self):
        self.assertEqual(encrypt_caesar(13, unit_test_string_07.upper()),"GUVF VF N GRFG JVGU DHBGRF")

    def test_18(self):
        self.assertEqual(encrypt_caesar(13, unit_test_string_08.upper()),"GUVF VF N GRFG JVGU NA RZNVY NAQERJPYNEXR.NEBA@TZNVY.PBZ")

    def test_19(self):
        self.assertEqual(encrypt_caesar(13, unit_test_string_09.upper()),"GUVF VF N GRFG JVGU N YBG BS FCNPRF                  ")
    
    def test_20(self):
        self.assertEqual(encrypt_caesar(13, unit_test_string_10.upper()),"GUVF VF N GRFG JVGU N UNCCL SNPR :)")


class Task_3_(unittest.TestCase):
     
    def test_21(self):
        self.assertEqual(main_ut(13,unit_test_string_01),"NOP")
    
    def test_22(self):
        self.assertEqual(main_ut(13, unit_test_string_02),"GUVFVFNGRFGJVGUFCNPRF")
    
    def test_23(self):
        self.assertEqual(main_ut(13, unit_test_string_03),"GUVFVFNGRFGJVGUAHZOREF")
    
    def test_24(self):
        self.assertEqual(main_ut(13, unit_test_string_04),"GUVFVFNGRFGJVGUSHYYFGBCFKKK")
    
    def test_25(self):
        self.assertEqual(main_ut(13, unit_test_string_05),"GUVFVFNGRFGJVGUFCRPVNYPUNEF")
    
    def test_26(self):
        self.assertEqual(main_ut(13, unit_test_string_06),"GUVFVFNGRFGJVGUNHEYUGGCFERNYCLGUBAKPBZCLGUBAGRFGVAT")

    def test_27(self):
        self.assertEqual(main_ut(13, unit_test_string_07),"GUVFVFNGRFGJVGUDHBGRF")
    
    def test_28(self):
        self.assertEqual(main_ut(13, unit_test_string_08),"GUVFVFNGRFGJVGUNARZNVYNAQERJPYNEXRKNEBATZNVYKPBZ")
    
    def test_29(self):
        self.assertEqual(main_ut(13, unit_test_string_09),"GUVFVFNGRFGJVGUNYBGBSFCNPRF")
    
    def test_30(self):
        self.assertEqual(main_ut(13, unit_test_string_10),"GUVFVFNGRFGJVGUNUNCCLSNPR")


if __name__ == '__main__':
    print("\n")
    unittest.main()
    