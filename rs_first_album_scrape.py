# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:34:07 2019

@author: Nate P
"""

import requests
from bs4 import BeautifulSoup as bs
from rs_functions import scrape_song
from rs_scrape_albums import album_names, album_years

the_rs_album_songs = ['Route 66', 'I Just Want To Make Love To You','I Need You Baby (Mona)', 'Little By Little', "I'm A King Bee", 'Carol','Tell Me', 
                      'Can I get a Witness', 'You Can Make It If You Try','Walking The Dog']

""" For loop that scrapes each song. 
    https://www.azlyrics.com/lyrics/rollingstones/ineedyoubabymona.html. Example of what htlm looks like. Simply loop over song names, format sting correctly
    
    Use ''.join(c for c in "Route 66" if c.isalnum()).lower() to format string!!
"""



""" Create dictionary where key is song title and value is song lyrics """
song_lyrics = {}
for song in the_rs_album_songs:
    title, lyrics = scrape_song(song)
    song_lyrics[title] = lyrics


""" How do I scrape song lyrics? First, create a list of album names. Imported album names from 'rs_scrape_albums
    Is it possible to scrape album song list from wikipedia? Next Step!!!

"""
""" Step one: Scrape one album, so can find repeatable process. Is an album song list always located in a table? """