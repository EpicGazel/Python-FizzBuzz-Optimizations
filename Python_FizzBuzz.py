# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:19:32 2022
"""
import time
startTime = time.time()


fizz_value = 3
buzz_value = 5

string_out = ""
i = 1
while i <= 2000000:
    fizz_mod = i % fizz_value
    fizz_diff = fizz_value - fizz_mod
    
    buzz_mod = i % buzz_value
    buzz_diff = buzz_value - buzz_mod
    
    fizz_mod_bool = fizz_mod == 0
    buzz_mod_bool = buzz_mod == 0
    
    if fizz_mod_bool:
        string_out += "Fizz"
    
    if buzz_mod_bool:
        string_out += "Buzz"
        
    if not(fizz_mod_bool or buzz_mod_bool):
        string_out += str(i)
    
    i += 1
    string_out += "\n"
    
print(string_out)
executionTime = (time.time() - startTime)
print("Time to execute in seconds: " + str(executionTime))