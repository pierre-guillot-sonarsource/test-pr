import logging
from logging import Logger, Handler, Filter
from logging.config import fileConfig, dictConfig

#test


class MyClass:
    pass

myvar = MyClass()
myvar()  # Noncompliant

none_var = None
none_var()  # Noncomplian

class CustomException:
    """An Invalid exception class."""

try:
    "a string" * 42
except CustomException:  # Noncompliant
    print("exception")
except (None, list()):  # Noncompliant * 2
    print("exception")

try:
    "a string" * 42
except [TypeError, ValueError]:  # Noncompliant. Lists are not accepted.
    print("exception")
except {TypeError, ValueError}:  # Noncompliant. Sets are not accepted.
    print("exception")
