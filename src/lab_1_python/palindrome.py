'''
Check whether string is palindrome or not.
'''

class Palindrome:
    def is_palindrome(self, string):
        start, end = 0, len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True

obj = Palindrome()
obj.is_palindrome("madam")
obj.is_palindrome("malayalam")
obj.is_palindrome("python")
obj.is_palindrome("12321")