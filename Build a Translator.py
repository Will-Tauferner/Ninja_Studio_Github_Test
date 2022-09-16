#Basic translator in python

from gettext import translation


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter 
    return translation


print(translate(input("Enter a phrase")))

