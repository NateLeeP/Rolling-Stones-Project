# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 06:51:26 2019

@author: Nate P
"""

import requests
from bs4 import BeautifulSoup as bs
import re

url = 'https://www.azlyrics.com/r/rollingstones.html'
rs_request = requests.get(url).text
rs_soup = bs(rs_request, 'lxml')

""" rs albums found in 'div', class = 'album'. Will need to clean albums, and drop those that are 'compilations' """

""" Use regular expression to extract Album name, Year. Album name is in Quotes, Year is in parenthesis """

re_album_name = re.compile('".+"') #Matches everything within quotes (or album names), INCLUDING quote. This will extract album name. 

re_album_year = re.compile('\([0-9]+\)') ### Matches everything within paranthesis, INCLUDING paranthesis. This will extract year. UPDATE: only matches numbers!!!

""" Use pattern objects (re_album_name, re_album_year) to match strings 
    Use for loop and 'if album in text' to filter out compilation albums. 

"""
"""
List comprehension to scrape album names, need to clean further. Scraped, uncleaned data. in format of 'album: "The Rolling Stones" (1964)'
"""
albums_scraped = [album.text for album in rs_soup.findAll('div','album') if 'album' in album.text]

"""
Extract album name, album year 
"""

album_names = [re_album_name.search(album).group(0).replace('"','') for album in albums_scraped]

album_years = [re_album_year.search(album).group(0).replace('(','').replace(')','') for album in albums_scraped]