import pyodbc
from datetime import date
import random
import os
import mysql.connector

start_year = 0


class Movie:
    def __init__(self, iID, sTitle, iYearReleased, iTime, iRating, sNote):
        self.ID = iID
        self.Title = sTitle
        self.Time = iTime
        self.Rating = iRating
        self.Note = sNote
        self.YearReleased = iYearReleased

    def MovieString(self):
        return '{0}\t{1}\t{2}\t{3}\t{4}'.format(self.ID,self.Title,self.YearReleased,self.Time,self.Rating)

try:
    start_year = date.today().year -2

    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='entertainment')

    cursor = cnx.cursor()

    search_SQL = """
                SELECT      *   
                FROM        movies
                 """

    movie_set = []

    cursor.execute(search_SQL)
    row = cursor.fetchone()

    while row is not None:
        if row[4] is None and row[2] <= start_year:
            movie_set.append(Movie(row[0],row[1],row[2],row[3],row[4],row[5]))
        row = cursor.fetchone()

    record_count = len(movie_set)
    
    command = ''
    while command != 'q':
        selected_ID = random.randint(0,(record_count-1))
        print(movie_set[selected_ID].MovieString())   
        command = input()
        
except Exception as err:
    print(err)
    input()








