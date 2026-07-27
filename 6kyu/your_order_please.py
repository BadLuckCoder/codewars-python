# Kata URL: "https://www.codewars.com/kata/55c45be3b2079eccff00010f/python"

def order(sentence):
    word_list = sentence.split()

    def find_digit(word):
        
        for char in word:
            
            if char.isdigit():
                return int(char)

    result = ' '.join(sorted(word_list, key = find_digit))
    
    return result