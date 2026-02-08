#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    This function computes n! (n factorial) by recursively multiplying
    n by the factorial of (n-1) until reaching the base case of 0.
    
    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.
    
    Returns:
    int: The factorial of n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)