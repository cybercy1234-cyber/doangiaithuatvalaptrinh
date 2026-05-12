class Solution(object):
    def isPalindrome(self, s):
        
        text = ""

        for ch in s:

            if ch.isalnum():
                text += ch.lower()

        return text == text[::-1]