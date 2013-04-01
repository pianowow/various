#-------------------------------------------------------------------------------
# Name:        pmp sit 2.4
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN

#Write a function censor that takes two strings text and word as input and returns
#the text with the word you chose replaced with asterisks.
#For example:
#censor("this hack is wack hack", "hack")
#should return
#"this **** is wack ****"
#The strings that you will be given will contain no punctuation or upper case letters.
#The number of asterisks you put should correspond to the number of letters in the word.

def censor(text,word):
    textlen = len(text)
    wordlen = len(word)
    for x in range(textlen-wordlen,-1,-1):
        if text[x:x+wordlen] == word:
            text = text[:x] +  "*"*wordlen + text[x+wordlen:]
    return text
