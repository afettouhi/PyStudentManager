'''A module for demonstrating exceptions.'''

from math import log
import sys


def convert(s):
    '''Convert to an integer.'''
#    x = -1
    try:
        return int(s)
#        x = int(s)
#        print("Conversion successful! x =", x)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        raise
#        return -1
#        pass
#        print("Conversion failed!")
#    return x
#    except ValueError:
#        print("Conversion failed")
#        x = -1
#    except TypeError:
#        print("Conversion failed")
#        x = -1


def string_log(s):
    v = convert(s)
    return log(v)


# from exceptional import convert
convert("33")
# convert("hedgehog")
# convert([3, 4, 5])


# from exceptional import string_log
string_log("25")