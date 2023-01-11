"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

# dictionary
def is_anagram(s,t):
    if len(s) != len(t):
        return False
    d = {}

    for ele in s:
        if ele not in d:
            d[ele] = 1
        else:
            d[ele] += 1

    for ele in t:
        if ele not in d:
            d[ele] = 1
        else:
            d[ele] -= 1

    for value in d.values():
        if value > 0 or value < 0:
            return False
    return True


# print(is_anagram('ccaa','cataq'))

# using freq array
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*256

        for ele in s:
            freq[ord(ele)]+=1

        for ele in t:
            freq[ord(ele)]-=1

        if freq == [0]*256:
            return True
        else:
            return False



# one liner
from collections import Counter

def is_anagram(s,t):
    return Counter(s)==Counter(t)

# using sort
# sort the strings and equate them


# making a count dicts and comparing

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_s={}
        count_t={}

        for i in range(len(s)):
            count_s[s[i]]= count_s.get(s[i],0)+1
            count_t[t[i]]= count_t.get(t[i],0)+1

        for ele in s:
            if count_s[ele]!=count_t.get(ele,0):
                return False
        return True