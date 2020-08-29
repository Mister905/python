def sort_string(string):
    words = string.split()
    # prepend lowercase version of string to each item in list
    # this is done to sort while preserving original case of strings in list
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)/2:] for w in words]
    print(words)

sort_string("The quick brown fox jumps over the lazy dog")