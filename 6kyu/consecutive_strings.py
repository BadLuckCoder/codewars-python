"""
===============================================================================
Kata: Consecutive strings
Level: 6 kyu
URL: https://www.codewars.com/kata/56a5d994ac971f1ac500003e
===============================================================================

Problem Description:
--------------------
You are given an array (list) of strings `strarr` and an integer `k`. 
Your task is to return the FIRST longest string consisting of `k` consecutive 
strings taken in the array.

Inputs:
  - strarr: list of strings
  - k: integer (number of consecutive strings to join)

Output:
  - The longest string formed by joining `k` consecutive strings.
  - Return "" if n == 0, k > n, or k <= 0.

Logic & Approach:
-----------------
1. Validate inputs: if array is empty, k <= 0, or k > len(strarr), return "".
2. Iterate through `strarr` using index tracking (`enumerate`).
3. Take a slice of `k` items starting from current index: `strarr[index : index + k]`.
4. Join the sliced array into a single string.
5. If the joined string is strictly longer than `max_result`, update `max_result`.
   (Using `>` ensures that if there are multiple candidates of same max length, 
   we keep the first one encountered).

Complexity:
-----------
- Time Complexity: O(n * k * L) -> where n is array length, k is consecutive elements, 
                                   and L is average string length.
- Space Complexity: O(k * L)   -> for storing the sliced joined string.
===============================================================================
"""

def longest_consec(strarr, k):
    n = len(strarr)
    
    # Edge Cases
    if n == 0 or k > n or k <= 0:
        return ""
        
    max_result = ""
    
    # Iterate and compare consecutive joined strings
    for index, item in enumerate(strarr):
        result = "".join(strarr[index : index + k])
        
        if len(result) > len(max_result):
            max_result = result
            
    return max_result


# Local Test Cases
if __name__ == "__main__":
    assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta"
    assert longest_consec(["ejjjjmmtthh", "zxmzzzz0000", "gketza", "135700"], 1) == "ejjjjmmtthh"
    assert longest_consec([], 3) == ""
    assert longest_consec(["it", "wkppv", "ixoyx", "3521", "123456789"], 5) == "itwkppvixoyx3521123456789"
    assert longest_consec(["it", "wkppv", "ixoyx", "3521", "123456789"], 0) == ""
    print("✅ All test cases passed successfully!")