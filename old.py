# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:19:32 2022
"""
import time
startTime = time.time()


fizz_value = 3
buzz_value = 5


i = 1
while i <= 50625:
    string_out = ""
    
    fizz_mod = i % fizz_value
    fizz_diff = fizz_value - fizz_mod
    
    buzz_mod = i % buzz_value
    buzz_diff = buzz_value - buzz_mod
    
    
    if fizz_mod == 0:
        string_out += "Fizz"
    
    if buzz_mod == 0:
        string_out += "Buzz"
        
    if string_out == "":
        min_diff = min([fizz_diff, buzz_diff])
        for n in range(i, min_diff+i):
            print(n)
        i += min_diff
        continue
    
    
    i += 1
    print(string_out)

executionTime = (time.time() - startTime)
print("Time to execute in seconds: " + str(executionTime))