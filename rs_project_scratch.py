# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 09:42:55 2019

@author: Nate P
"""

import re
import rs_functions as rs
""" Can we make an re that match each decade? """

test_years = [1965, 1966,1970, 1976, 1977, 1989, 1987, 1986, 1996]

sixties_pattern = re.compile('196[0-9]')
seventies_pattern = re.compile('197[0-9]')
eighties_pattern = re.compile('198[0-9]')
nineties_pattern = re.compile('199[0-9]')
sixties = []
seventies = []
eighties = []
nineties = []

album_years = rs.scrape_album_years()

for album in album_years:
    if re.search(sixties_pattern, str(album[1])):
        sixties.append(album[0])
    if re.search(seventies_pattern, str(album[1])):
        seventies.append(album[0])
    if re.search(eighties_pattern, str(album[1])):
        eighties.append(album[0])
    if re.search(nineties_pattern, str(album[1])):
        nineties.append(album[0])
        

sixties_albums, seventies_albums, eighties_albums, nineties_albums = rs.albums_by_decade(rs.scrape_album_years())

""" Creating a dictonary where values are a dictionary. Idea is a dictionary of track names and song lyrics. """


 # Dictionary of album:track titles
album_track_titles = rs.clean_song_titles_dictionary(rs.scrape_song_titles())

# Use the corresponding album title from 'album_track_titles'!! This gives track list
nineties_dict = {}
for album in nineties_albums:
    nineties_dict[album] = {'Tracks': {}}
    for track in album_track_titles[album]:
        nineties_dict[album]['Tracks'][track] = rs.scrape_song(track)[1]