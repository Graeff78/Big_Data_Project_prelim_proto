from db_config import get_redis_connection
import json

""" 
establish redis connection.
db_setup
""" 
r = get_redis_connection()

""" 
Query Uno
General search for all catalogued movie titles.
""" 
def first_query():   
    print("First:\n\t")
    keys = r.keys("movies:*")
    for key in keys:
        value = r.json().get(key)
        item = json.loads(value)
        print(item["title"])
    print("\n")


""" Query Dos
General search for movies rated higher than a 7 out of 10 points.
""" 
def second_query():
    print("Second:\n\t")
    keys = r.keys("movies:*")
    for key in keys:
        value = r.json().get(key)
        item = json.loads(value)
        if (item["vote_average"] > 7):
            print(item["title"]+":\t"+str(item["vote_average"]))
    print("\n")


""" 
Query Tres
General search for movies with specific genres(Science Fiction).
""" 
def third_query():
    print("Third:\n\t")
    keys = r.keys("movies:*")
    for key in keys:
        value = r.json().get(key)
        item = json.loads(value)
        for genre in item["genre_ids"]:
            if (genre == 878):
                print(item["title"])
    print("\n")

"""
Query Quatro
Aggregate search for a for the average popularity of all stored movies.
"""
import pandas as pd

def fourth_query():
    print("Fourth:\n\t")
    
    keys = r.keys("movies:*")
    data = {}

    for key in keys:
        value = r.json().get(key)
        data[key] = json.loads(value)

    df = pd.DataFrame(data)
    print("Average popularity of all movies:\t", df.loc['popularity'].mean())

