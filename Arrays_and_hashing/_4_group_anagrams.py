"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for w in strs:
            count = [0]*26
            for l in w:
                count[ord(l)-ord("a")] += 1
            res.setdefault(tuple(count),[])
            res[tuple(count)].append(w)
        return res.values()


class Solution:

    def sorti(self, strs):
        newstrs = ""
        strs2 = sorted(strs)
        for i in strs2:
            newstrs = newstrs + i
        return newstrs

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            newi = self.sorti(i)
            res.setdefault(newi, [])
            res[newi].append(i)

        return res.values()