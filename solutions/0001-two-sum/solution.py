from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the list that add up to the target.

        Args:
            nums: A list of integers.
            target: The integer target sum.

        Returns:
            A list containing the indices of the two numbers.
            Assumes exactly one solution exists and an element cannot be used twice.
        """
        # A dictionary (hash map) to store numbers and their indices.
        # Key: number, Value: index
        num_map = {} 

        # Iterate through the list of numbers with their indices.
        for i, num in enumerate(nums):
            # Calculate the complement needed for the current number to reach the target.
            complement = target - num

            # Check if the complement already exists in our hash map.
            # If it does, we've found the two numbers.
            if complement in num_map:
                # The index of the complement is stored as its value in the map.
                # The index of the current number is 'i'.
                return [num_map[complement], i]
            
            # If the complement is not found, add the current number and its index 
            # to the map. This way, it can be a complement for subsequent numbers.
            num_map[num] = i
        
        # The problem statement guarantees exactly one solution,
        # so this line should theoretically never be reached.
        # However, for completeness in a real-world scenario, 
        # one might raise an error or return an empty list if no solution is found.
        return []
