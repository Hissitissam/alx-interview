#!/usr/bin/python3
""" The module for task0 0-minoperations"""


def minOperations(n):
    """calculates the fewest number of operations needed to result 
    in exactly n H characters in the file."""
    
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        
        root += 1
    return ops