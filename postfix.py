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
    # click ADD (`+` button), choose Python & define the following:
    # 1) in the Key parameter, insert "check_time"
    # 2) check the "Apply to the topmost expression" checkbox
    # 3) in the Template parameter, insert the following:
    #       start = time.time()
    #       $EXPR$
    #       end = time.time()
    #       print(f"Function $EXPR$ Execution time: {end - start}")

    # finally:
    #   go to the end of 24th line, add a dot (`.`) and choose "check_time" in the autocomplete list
