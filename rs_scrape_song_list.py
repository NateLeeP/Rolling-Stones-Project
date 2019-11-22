# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 07:10:15 2019

@author: Nate P
"""

import requests
from bs4 import BeautifulSoup as bs
import re
from rs_scrape_albums import album_names
re_album_name = re.compile('".+"') 
""" Need to scrape song list from Wikipedia. Does the song list table serve as only table? Can we use a similar scrape process to 
    NBA project? Practice with 'The Rolling Stones' album
    Overthinking it. Song titles are listed on az lyrics website!!! How do I get them?
   
    Could scrape the whole list of album names + songs, then break off into chunks whenever there is an album name?
    Take a look at .next_sibling and .previous_sibling
    
    Can you use bool to check if return'd value is a div tag? Take a look at 'tag.has_attr'. Do song titles have a class attribute? Maybe not.
    Consider using a 'while' loop to loop through album name until running into a tag with a 'class' attribute. 
    Then how would we get to albums? Using soup.findAll('div','album') call. 
    
    """
    
url =  'https://www.azlyrics.com/r/rollingstones.html'
the_rs_album_request = requests.get(url).text
the_rs_album_soup = bs(the_rs_album_request, 'lxml')


""" Attempting to use a while loop to loop through album tags in rolling stones soup. Doing this will allow us to use .next_sibling to get all the names of songs
    Will use a tag.has_attr('class') to break the loop """
"""    
my_dict = {}
for album_tag in the_rs_album_soup.find_all('div','album'):
    my_dict[album_tag.text] = []
    while album_tag.has_attr('class') is True:
        my_dict[album_tag.text].append(album_tag.next_sibling)

Above code DID NOT WORK. Lets try with just one album """

"""
album_tag = the_rs_album_soup.find('div','album').next_sibling

while album_tag.has_attr('class') is False:
    print(album_tag.text)
    album_tag = album_tag.next_sibling

Above code DID NOT WORK. Lets try a if-else loop embedded in a while loop """
album_tag = the_rs_album_soup.find('div','album').next_sibling
album_song_titles = []
while True:
    if album_tag == '\n':
        album_tag = album_tag.next_sibling
        continue
    elif album_tag.has_attr('class') is False:
        album_song_titles.append(album_tag.text)
        album_tag = album_tag.next_sibling
        continue
    elif album_tag.has_attr('class') is True:
        break
""" ABOVE CODE WORKS!!! Need to clean, turn into function, make repeatable, etc """



"""Can I turn above While loop into a for loop? """

my_dict = {}
for album_tag in the_rs_album_soup.find_all('div','album'):
    if album_tag.text == 'other songs:':
        continue
    my_dict[re_album_name.search(album_tag.text).group(0).replace('"','')] = []
    album_tag_start = album_tag.next_sibling
    while True:
        if (album_tag_start == '\n') or (album_tag_start == ' '):
            album_tag_start = album_tag_start.next_sibling
            continue
        elif album_tag_start.has_attr('class') is False:
            my_dict[re_album_name.search(album_tag.text).group(0).replace('"','')].append(album_tag_start.text)
            album_tag_start = album_tag_start.next_sibling
            continue
        elif album_tag_start.has_attr('class') is True:
            break
my_dict_copy = my_dict        

""" Currently have dictionary of album:song titles. What to do with these? Clean up album names? Use album clean up function?
will clean up work as function? Can you clean key, value at same time?
Should each album have its own dictionary?? One big dictionary, each key is album title. Each value is a dictionary with keys 'Songs' and 'Year'. """

""" Need to delete albums that are not real albums (compilation bullshit). """




