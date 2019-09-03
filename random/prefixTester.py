def prefixTester(words, prefix):
    return [x for x in words if prefix == x[0:len(prefix)]]


print(prefixTester(["hello", "man", "jam", "amazing", "anaconda", "anal", "hellman", "hangman"], "b"))
