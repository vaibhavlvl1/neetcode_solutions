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

def is_anagram(s,t):
    d = dict()
    if len(s) != len(t):
        return False
    for ele in s:
        d[ele] = d.get(ele, 0) + 1

    for ele in t:
        if d[ele]==0:
            d[ele] = 1
        else:
            d[ele] = d[ele]-1


    print(d)
    for value in d.values():
        if value >0:
            return False
    return True


print(is_anagram('ccaa','cataq'))