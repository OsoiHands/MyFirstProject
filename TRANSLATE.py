#This function letters A,E,I,O,U to YWY
#and B,C,D,F,G,H to AUA

def translator(phrase):
    translation = ""

    for letters in phrase:
        #Check "A, E, I, O, U" and return YWY
        if letters.lower() in "aeiou":
            if letters.isupper():
                translation = translation + "YWY"
            else:
                translation = translation + "ywy"
        #Check "B, C, D, F, G, H" and return AUA
        elif letters.lower() in "bcdfgh":
            if letters.isupper():
                translation = translation + "AUA"
            else:
                translation = translation + "aua"
        #Return the phrase without change
        else:
            translation = translation + letters
    return translation

print(translator(input("Input phrase:  ")))


#This is my first code ever.
#Please give me pointers to what should I learn.
#Thank you for reading!
