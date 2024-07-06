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

    # GO TO SETTINGS -> POSTFIX COMPLETION and define time postfix action
    fib(50)

    # Click CTRL + OPT + O to fix imports
