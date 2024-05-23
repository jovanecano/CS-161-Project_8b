# Author: Jovane Cano
# GitHub username: jovanecano
# Date: 05/22/2024
# Description:
"""This script creates a function called words_in_both that will find then return common words in both inputs"""

def  words_in_both(string_one, string_two):
    """this function allows the user to input two strings, splits, then uses the operator intersection
        to see what words are in common between the two"""
    words_one = set(string_one.lower().split()) #converting the string_one to lower case then splits
    word_two = set(string_two.lower().split())  #converting the string_two to lower case then splits

    common_words = words_one.intersection(word_two) #checking for common words

    return common_words

#testing function with "Mary had a little lamb" and an incorrect version to see whether it works correctly
#print(words_in_both("Mary had a little lamb", "Mary had little lam"))
#output was {'mary', 'had', 'little'} which is correct