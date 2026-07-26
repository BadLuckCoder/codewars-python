# KATA URL : https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    if n == 0:
        return []
    
    if 0 < n < 3:
        return signature[ : n]
    
    new_list = signature[:]
    
    for number in range(n - len(signature)):
        
        new_list.append(new_list[-1] + new_list[-2] + new_list[-3])
        
    return new_list