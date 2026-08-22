class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index

        for index, number in enumerate(nums): #"Go through nums, and give me both the index and the number at that index."
            diff = target - number
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[number] = index
        return