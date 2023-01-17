"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.


"""


def isPalindrome(self, s: str) -> bool:
    new_s = ""
    for ele in s:
        if ele.isalnum():
            new_s += ele.lower()
    i = 0
    j = len(new_s) - 1

    while i <= j:
        if new_s[i] != new_s[j]:
            return False
        i = i + 1
        j = j - 1
    return True


print(isPalindrome("race car"))




# Another solution better than above

def alphanum(self, c):
    return (ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord('0') <= ord(c) <= ord('9'))


def isPalindrome(self, s: str) -> bool:
    i = 0
    j = len(s) - 1

    while i < j:
        while i < j and not self.alphanum(s[i]):
            i = i + 1
        while j > i and not self.alphanum(s[j]):
            j = j - 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True