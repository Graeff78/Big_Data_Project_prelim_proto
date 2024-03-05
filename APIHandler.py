import requests
import json
from Loader import load
""" 
This class pulls the GET meta data from the source db API.

establish http connection.
Use JSON format to fit into queried request object.
""" 
def fetch_response():

    """ 
    increase range for more movie data. 10 movies per page.
    """ 
    for page in range(1, 2):

        url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page="+str(page)+"&sort_by=popularity.desc"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMTM3YzIyOGYzYmFhMWEzYTkzYmRjYzNmYjUzNGNlMyIsInN1YiI6IjY1MmQ2OGUyMGNiMzM1MTZmNzQ4ODRkNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FNdcYi26XXZ1_3XaXY6vApqkNACsw37YdTFawjqRHmM"
        }
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)

        """ 
        call loader instance to inject movie into redis
        """ 
        for item in data["results"]:
            load(item)  
        