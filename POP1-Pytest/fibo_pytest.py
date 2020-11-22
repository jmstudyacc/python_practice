#!/usr/bin/env python

def fib(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old


# Lucas Sequence

def luc(n):
    old, new = 2, 1
    for _ in range(n):
        old, new = new, old + new
    return old
