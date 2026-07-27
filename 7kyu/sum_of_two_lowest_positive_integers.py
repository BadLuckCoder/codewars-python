# KATA URL: "https://www.codewars.com/kata/558fc85d8fd1938afb000014/solutions/python"

import heapq

def sum_two_smallest_numbers(numbers):
    sum_lowest = sum(heapq.nsmallest(2, numbers))
    
    return sum_lowest