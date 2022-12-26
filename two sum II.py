'''
This is an updated version of two sum where no extra space can be used. Constant space solution requires NOT TO use any extra array or hashmap. So two pointer algorithm
is used here. Starting from the two corner elemets, adding them and comparing them with the target goes on. As the array is sorted already, if the current sum is greater
than the target, then we have to decrease the right pointer. In the same manner, if the target is greater than the current sum, we have to increase the left pointer by one/
That's how we can iterate through the whole list and can get the answer.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            pseudo_sum = numbers[left] + numbers[right]
            if pseudo_sum == target:
                return [left+1, right+1]
            elif pseudo_sum > target:
                right -= 1
            else:
                left += 1
