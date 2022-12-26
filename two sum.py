# First I am taking an empty hashmap and then I am iterating through the whole given list.
# Then the hashmap is updated with index of the items of the list as values and the items itself as keys.
# I am keeping the difference between a given item from the list and the target in a variable. And then checking if it alreay exists in the hashmap keys or not.
# if the difference matches with an existing key in the hashmap, then return the present iteration key and the key for the corresponding difference from the hashmap.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for key, value in enumerate(nums):
            difference = target - value
            if difference in hm:
                return [key, hm[difference]]
            else:
                hm[value] = key
