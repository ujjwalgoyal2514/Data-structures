class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
        s=0
        for i in range(len(nums)):
            count[nums[i]]=i
        for i in range(len(nums)):
            c=target-nums[i]
            if c in count and count[c]!=i:
                return [i,count[c]]
        return []
