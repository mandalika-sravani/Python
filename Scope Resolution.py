# variable scope --- where a variable is visible and accessible
# scope resolution --- (LEGB) -- Local -> Enclosed -> Global -> Built-in

# Local

def fun1():
    x = 3
    print(x)

def fun2():
    y = 9
    print(y)

fun1()
fun2()

# Enclosed

def fun1():
    x = 5
    def fun2():
        print(x)
    fun2()

fun1()

# Global

def fun1():
    print(x)

def fun2():
    print(y)

x = 4
y = 7

fun1()
fun2()

#Built-in
from math import e

def fun1():
    print(e)

e = 3

fun1()