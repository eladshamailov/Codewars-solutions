"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot seperating them.
"""

import re

def abbrevName(name):
    return '.'.join(p_name[0] for p_name in name.split()).upper()
