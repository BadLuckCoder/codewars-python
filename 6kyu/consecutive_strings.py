def longest_consec(strarr, k):
    n = len(strarr)
    
    if n == 0 or k > n or k <= 0:
        return ""
    
    max_result = ""
    
    for index, item in enumerate(strarr):
        
        result = "".join(strarr[index : index + k])
        
        if len(result) > len(max_result):
            
            max_result = result
        
    return max_result