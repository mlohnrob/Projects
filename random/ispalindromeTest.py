def isPalindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


print(isPalindrome("DDnKnDD"))
