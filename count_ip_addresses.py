"""
Write a function that accepts a starting and ending IPv4 address, and the 
number of IP addresses from start to end, excluding the end IP address.
All input to the function will be valid IPv4 addresses in the form of strings. 
The ending address will be at least one address higher than the starting address.
"""

def ips_between(start, end):
    range_ans = 0
    ip_lst = [int(ip2) - int(ip1) for ip1, ip2 in zip(start.split('.'), end.split('.'))]
    for ind, num in enumerate(ip_lst):
        print (num, ind, len(ip_lst), range_ans)
        range_ans += num * (256 ** (len(ip_lst) - ind - 1))
    return range_ans
