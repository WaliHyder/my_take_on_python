#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 06:32:35 2022

@author: walihyder
"""
#8.18 (REGULAR EXPRESSION: PASSWORD FORMAT VALIDATOR)

#1. Password Requirements = must contain atleast five words,each seperated by a hyphen,a space,a period, a comma or an underscore.

#importing regular expressions

import re 
password = input('Please enter password: ') #input password 
pattern = r'(([A-Za-z]+[-.,_\s]).{5,})'
#[A-Za-z]+[-.,_\s]{1}[A-Za-z]+[-.,_\s]{1}[A-Za-z]+[-.,_\s]{1}[A-Za-z]+)' #regex
print ("Password is Valid") if re.match(pattern,password)else print ("Invalid Password")  #validation 

#2.Password Requirements = must have a minimum of 8 characters and contain at least one each from uppercase characters, 
# lowercase characters, digits and punctuation characters (such as characters in '!@#$%<^>&*?').


password2 = input('Please enter second password:') #input password 2
pattern2 ="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#$%<^>&*?]).{8,}$"
print ("Password is Valid") if re.findall(pattern2,password2)else print ("Invalid Password")
