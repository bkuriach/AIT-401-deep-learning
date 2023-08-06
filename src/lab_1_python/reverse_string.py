# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

#Example 2
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class StringReverse():
    def __init__(self):
        pass
    def reverse(self, string):
        string = list(string)
        left = 0
        right = len(string) - 1
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        return string

# StringReverse().reverse("hello")

