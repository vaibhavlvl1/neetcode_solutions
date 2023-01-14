"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for ele in arr:
            d[ele] = d.get(ele,0)+1
        print(d)
        max = 0
        for ele in d.values():
            if max<ele:
                max = ele
        print(max)
        j = max
        while len(res)<=k-1:
            value = [i for i in d if d[i]==j]
            for ele in value:
                res.append(ele)
            j = j-1


        return res













# last loop explained

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for ele in nums:
            d[ele] = d.get(ele, 0) + 1

        max = 0
        for value in d.values():
            if max < value:
                max = value

        res = []
        j = max

        while len(res) <= k - 1:
            for i in d.keys():
                if d[i] == j:
                    res.append(i)

            j = j - 1
        return res