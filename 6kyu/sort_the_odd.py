# KATA URL: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    odd_list = []
    new_array = source_array[:]
    odd_count = 0
    
    for number in new_array:
        
        if number % 2 != 0:
            
            odd_list.append(number)
    
    odd_list.sort()
    
    for index, num in enumerate(new_array):
        
        
        if num % 2 != 0:
            
            new_array[index] = odd_list[odd_count]
            odd_count += 1
            
    return new_array