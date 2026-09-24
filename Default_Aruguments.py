# default arguments --- A default value for certain parameters. default is used whent that argument is omitted make your 
#                         functions more flexible ---- positional, DEFAULT, keyword, arbitrary

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(2)
    print("DONE!")

count(0, 10)