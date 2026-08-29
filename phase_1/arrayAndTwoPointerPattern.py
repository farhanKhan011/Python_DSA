# ------------Arrays & Two-Pointer Pattern-----------

'''
How Arrays Work in Memory
An Array (a Python list) stores elements in contiguous (side-by-side) memory blocks.
* Lookup by Index (arr[i]): O(1) constant time because the system calculates exact physical memory address directly.
* Search by Value: O(n) linear time because it checks items sequentially.
* Insertion/Deletion (Middle): O(n) time because elements must shift positions.

'''
'''
The Core Pattern: Two-Pointer Technique Instead of using nested loops (O(n^2) execution),
 the Two-Pointer technique uses two indices moving through the array simultaneously to solve problems in linear O(n) time. 
Problem: Given a sorted array of numbers and a target sum, return the two numbers that add up to target.
'''
# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [2, 7]

# ----------------Code Implementation----------------------

def two_sum_sorted(numbers: list[int], target: int ) -> list[int]:
    left = 0                        # Pointer at start 
    right  = len(numbers) - 1       # Pointer at end 

    while left < right :
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [numbers[left] , numbers[right]]
        elif current_sum < target:
            left += 1 # Need a larger sum -> move left pointer right 
        else:
            right -= 1 # Need a smaller sum -> move right pointer left 
    return []
# Example Run 
nums = [2,7,11,15]
target_val = 9 
print(two_sum_sorted(nums , target_val)) 
# output : [2,7]

# ----------Complexity Analysis-----------
'''
* Time Complexity:O(n)- Each step shifts at least one pointer inward,
  processing the array in a single pass.

* Space Complexity:O(1)-Only two integer variables(left , right ) are stored in memory.

'''
                   