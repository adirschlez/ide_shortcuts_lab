import time
import os
import json
import logging

logger = logging.getLogger(__name__)


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def run():
    itterations = 200
    # We whould like to add a shortcut for printing this struct of code:
    #
    # start = time.time()
    # fib(itterations)
    # end = time.time()
    # print(f"Function fib(itterations) Execution time: {end - start}")

    fib(itterations)

    # We will define a new POSTFIX COMPLETION for this action
    # GO TO SETTINGS -> POSTFIX COMPLETION and define time postfix action
    # insert the next struct:
    #
    # start = time.time()
    # $EXPR$
    # end = time.time()
    # print(f"Function $EXPR$ Execution time: {end - start}")




