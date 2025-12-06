# 1. Running Sum Of 1d Array
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        curr = 0
        for n in nums:
            curr += n
            answer.append(curr)
        return answer

# 2. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ## APPROACH : GREEDY ##
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
# 3. Kids With the Greatest Number of Candies   
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies any kid currently has
        maxCandies = max(candies)

        # List to store results
        greatestCandies = []
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies any kid currently has
        maxCandies = max(candies)

        # List to store results
        greatestCandies = []

     