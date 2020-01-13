def transl(phase):
    word=""
    for letter in phase:
        if letter in "AEOUIaeoui":
            word = word+"d"
        else:
            word=word+letter
    return word

print(transl(input("Enter Phase: ")))
        
