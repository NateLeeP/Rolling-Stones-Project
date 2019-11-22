# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 07:29:13 2019

@author: Nate P
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.azlyrics.com/lyrics/rollingstones/connection.html' ## Lyrics to 'Connection'

connection_request = requests.get(url).text ##Request html for connection

connection_soup = bs(connection_request, 'lxml')

song_title = connection_soup.h1.text ## Returns title of song, assuming song title is ALWAYS at h1. 

connection_lyrics = connection_soup.find_all('div')[19].text ### Work with lyrics first. Can I get each line as an element in a list?

connection_lyric = connection_lyrics.strip().split('\n') ###List with each element a lyric line

"""Create counter function """

### Below prints each word in a lyric line (my_string is the lyric line)        
def lyric_words_count(lyrics):
    word_count_dict = {}
    for line in lyrics:
        for word in line.replace(',','').split(' '):
            if word.lower().strip('.') in word_count_dict.keys():
                word_count_dict[word.lower().strip('.')] += 1
            else:
                word_count_dict[word.lower().strip('.')] = 1
    return sorted(word_count_dict.items(), key = lambda x:x[1], reverse = True)



""" Returns count of specific word """
def lyric_word_count(lyrics, word):
    value = 0
    for line in lyrics:
        for lyric_word in line.replace(',','').split(' '):
            if lyric_word.lower().strip('.') == word.lower():
                value += 1
    return (word, value) if value else 'Word does not appear!'