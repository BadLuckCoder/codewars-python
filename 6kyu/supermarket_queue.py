"""
===============================================================================
Kata: The Supermarket Queue
Level: 6 kyu
URL: https://www.codewars.com/kata/57eb8f6071852669ae000109/train/python
===============================================================================

Problem Description:
--------------------
There is a queue for the self-checkout tills at the supermarket.
Your task is to write a function to calculate the total time required 
for all the customers to check out!

Inputs:
  - customers: A list of positive integers representing the queue. 
               Each integer is the time a customer requires to check out.
  - n: A positive integer representing the number of checkout tills.

Output:
  - Return an integer: the total time required for all customers to checkout.

Logic & Approach:
-----------------
1. Initialize a list `machines` of size `n` with 0s to represent the available tills.
2. Iterate through each customer in the queue.
3. Find the till that will finish the earliest (i.e., minimum value in `machines`).
4. Add the current customer's time to that till.
5. The total time required is the maximum value in `machines` after processing all customers.

Complexity:
-----------
- Time Complexity: O(C * n)  -> where C is the number of customers and n is the number of tills.
- Space Complexity: O(n)     -> to store the time for n tills.
===============================================================================
"""

def queue_time(customers, n):
    machines = [0] * n
    for customer in customers:
        min_machine_index = machines.index(min(machines))
        machines[min_machine_index] += customer
    return max(machines)


# Local Test Cases
if __name__ == "__main__":
    assert queue_time([], 1) == 0
    assert queue_time([5, 3, 4], 1) == 12
    assert queue_time([10, 2, 3, 3], 2) == 10
    assert queue_time([2, 3, 10], 2) == 12
    print("✅ All test cases passed successfully!")