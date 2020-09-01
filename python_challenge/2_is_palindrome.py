def is_palindrome(string):
    if (isinstance(string, str)):
        forwards = string.lower()
        reverse = forwards[::-1]
        return forwards == reverse
    else:
        return "Please enter a valid string"

if __name__ == '__main__':  

    print(is_palindrome("aNnA"))

    print(is_palindrome("tESt"))

    print(is_palindrome(200))