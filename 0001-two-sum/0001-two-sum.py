class Solution(object):
    def twoSum(self, nums, target):
        
        dict = {}

        for index, x in enumerate(nums):
            need = target - x
            if need in dict:
                return[dict[need],index]
            dict[x] = index 
        return []
        