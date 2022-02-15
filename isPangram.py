# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string

class Solution:
    def isPangram(self,s):
        try:
            for i in string.ascii_lowercase:
                if i not in s.lower():
                    return f"{s} is not a pangram"
                return f"{s} is a pangram"
        except Exception as e:
            print(e)

s = "'The quick brown fox jumps over the lazy dog'"
P = Solution()
Q = P.isPangram(s)
print(Q)
