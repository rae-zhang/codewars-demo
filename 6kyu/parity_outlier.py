'''DESCRIPTION:
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.'''

def find_outlier(integers):
    even = []
    odd = []
    for i in integers:
        if (i % 2) == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 1:
        for i in even:
            return i
    elif len(odd) == 1:
        for i in odd:
            return i
