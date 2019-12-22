# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:56:04 2019

@author: Haseeb
"""

import os, re

files = os.listdir('t:/media/movies')

movie = ['mp4', 'mkv', 'mov']

for filename in files:
    if filename.split('.')[-1] in movie:
        
        print(filename)
        

from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

ia = IMDb()

movies = ia.search_movie('avengers')

print(movies[0])
movieID = movies[0].movieID
print(movieID)

# get a movie and print its director(s)
the_matrix = ia.get_movie(movieID)
for director in the_matrix['directors']:
    print(director['name'])

# show all information that are currently available for a movie
print(sorted(the_matrix.keys()))

# show all information sets that can be fetched for a movie
print(ia.get_movie_infoset())

# update a Movie object with more information
ia.update(the_matrix, ['technical'])
# show which keys were added by the information set
print(the_matrix.infoset2keys['technical'])
# print one of the new keys
print(the_matrix.get('tech'))
print(the_matrix['rating'])