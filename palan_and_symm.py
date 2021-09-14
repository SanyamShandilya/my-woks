def issym(words):
    if words[:len(words)//2] == words[len(words)//2:]:
        print(words," is a symmetrical word.")
    else:
        print(words," is a not symmetrical word.")

def ispalan(words):
    if words[:] == words[::-1]:
        print(words," is a palandromic word.")
    else:
        print(words," is not a palandromic word.")

word = input("Enter the word you want to check: ").lower()
ispalan(word)
issym(word)