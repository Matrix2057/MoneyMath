# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 2021

@author: Matrix2057
"""

import streamlit as st

st.title('Money Math')
penny = ['a','e','i','o','u']
dime = ['k','l','m','n','p','q','r']
nickel = ['b','c','d','f','g','h','j']
quarter = ['s','t','v','w','x','y','z']

# Python3 program to Split string into characters 
def split(word): 
    return list(word) 
       
def calculateword(word):
        wordlist = (split(word))         
        worth = 0
        for letter in wordlist:
            if letter in penny:
                worth +=1
            if letter in dime:
                worth +=10
            if letter in nickel:
                worth +=5
            if letter in quarter:
                worth += 25
        return worth

# =============================================================================
# Main
# =============================================================================

st.write("Type any word to be converted to money")
word = st.text_input(label = "Enter word:", key = 'wordkey').lower()

worth = calculateword(word)
st.write("Your word is worth: "+str(worth))

st.write(f"""
         ---
         ## Current configurations...\n
         penny = {''.join(penny)}\n
         dime = {''.join(dime)}\n
         nickel = {''.join(nickel)}\n
         quarter = {''.join(quarter)}\n
        """)


if st.button('Quit'):
    st.write("Thanks for playing!")
    st.stop()