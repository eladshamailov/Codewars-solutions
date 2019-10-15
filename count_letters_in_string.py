'''
In this kata, you've to count lowercase letters in a given string and return the letter count in a hash with 
'letter' as key and count as 'value'. 
The key must be 'symbol' instead of string in Ruby and 'char' instead of string in Crystal.
'''

def letter_count(s):
    letter_dict = {}
    for c in s:
        if c not in letter_dict:
            letter_dict[c] = 1
        else:
            letter_dict[c] = letter_dict[c] + 1
    return letter_dict
