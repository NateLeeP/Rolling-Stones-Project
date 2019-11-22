# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 07:09:07 2019

@author: Nate P
"""

import requests
import re
from bs4 import BeautifulSoup as bs
url = 'https://www.azlyrics.com/r/rollingstones.html'
rs_request = requests.get(url).text
rs_soup = bs(rs_request, 'lxml')
re_album_name = re.compile('".+"')


""" For loop that scrapes each song. 
    https://www.azlyrics.com/lyrics/rollingstones/ineedyoubabymona.html. Example of what htlm looks like. Simply loop over song names, format sting correctly
    
    Use ''.join(c for c in "Route 66" if c.isalnum()).lower() to format string!!
"""
def scrape_song_titles():
    """ Returns a dictionary of 'Album Names': 'Song Titles'. A dictionary of track list. """
    rs_dict = {}
    
    
    for album_tag in rs_soup.find_all('div','album'): 
        if album_tag.text == 'other songs:': ### Error with other songs. Not a real album
            continue
    
        rs_dict[re_album_name.search(album_tag.text).group(0).replace('"','')] = [] ### The key for the dictionary is the cleaned album name
        album_tag_start = album_tag.next_sibling ### Cannot start on class: 'album' tag, need to start on next tag
    
        while True: ### While loop because unsure how many songs are in each album. Loop closes when another class:'album' tag is reached. 
            if (album_tag_start == '\n') or (album_tag_start == ' '): ### Every other line is a new line. Must skip these, or will crash loop
                album_tag_start = album_tag_start.next_sibling
                continue
            elif album_tag_start.has_attr('class') is False: ### If there isn't a class attribute, it is a song title. So we add it to the list.
                rs_dict[re_album_name.search(album_tag.text).group(0).replace('"','')].append(album_tag_start.text)
                album_tag_start = album_tag_start.next_sibling
                continue
            elif album_tag_start.has_attr('class') is True:
                break
    return rs_dict
def clean_song_titles_dictionary(rs_dict):
    """ Song title dictionary has problems. This function cleans up the scraped mess """
    
    """Remove compilation albums from dictionary """
    for key in list(rs_dict.keys()):
        if key not in scrape_album_names():
            del rs_dict[key]
    """ Clean song title list. Have a blank space every other line """
    for album, track_list in rs_dict.items():
        rs_dict[album] = [track for track in track_list if track != '']
    

def scrape_album_names():
    """ Returns list of album names off Rolling Stones AZlyrics website """
    """ Scrape album names """
    albums_scraped = [album.text for album in rs_soup.findAll('div','album') if 'album' in album.text]
    """ Extract actual Album Name """
    album_names = [re_album_name.search(album).group(0).replace('"','') for album in albums_scraped]
    
    return album_names

def scrape_album_years():
    """Returns list of tuples holding album name, year """
    
    """ Regex object that extracts year from scraped text """
    re_year = re.compile('\([0-9]+\)')
    
    """ Scrape albums """
    albums_scraped = [album.text for album in rs_soup.findAll('div','album') if 'album' in album.text]

    """ Extract years from scraped albums """
    years = [re_year.search(album).group(0) for album in albums_scraped]
    album_names = scrape_album_names()
    
    years = list(zip(album_names, years))
    return years

def scrape_song(song_name):
    """ Scrape the Lyrics from a given song. Return list of of lyrics """
    url = 'https://www.azlyrics.com/lyrics/rollingstones/{}.html'.format(''.join(c for c in song_name if c.isalnum()).lower())
    lyric_request = requests.get(url).text
    lyric_soup = bs(lyric_request, 'lxml')
    song_title = re.sub(r' lyrics', '', lyric_soup.h1.text.replace('"', ''))
    lyrics = lyric_soup.find_all('div')[19].text
    lyric = lyrics.strip().split('\n')
    return (song_title, lyric)
    






def lyric_words_count(lyrics):
    word_count_dict = {}
    for line in lyrics:
        for word in line.replace(',','').split(' '):
            if word.lower().strip('.') in word_count_dict.keys():
                word_count_dict[word.lower().strip('.')] += 1
            else:
                word_count_dict[word.lower().strip('.')] = 1
    return sorted(word_count_dict.items(), key = lambda x:x[1], reverse = True)

def lyric_word_count(lyrics, word):
    value = 0
    for line in lyrics:
        for lyric_word in line.replace(',','').split(' '):
            if lyric_word.lower().strip('.') == word.lower():
                value += 1
    return (word, value) if value else 'Word does not appear!'