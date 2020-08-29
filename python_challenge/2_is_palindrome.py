def is_palindrome(string):
    if (isinstance(string, str)):
        forwards = string.lower()
        reverse = forwards[::-1]
        return forwards == reverse
    else:
        return "Please enter a valid string"
    

print(is_palindrome("aNnA"))

print(is_palindrome("tESt"))

print(is_palindrome(200))