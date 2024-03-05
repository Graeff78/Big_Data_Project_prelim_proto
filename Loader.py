from db_config import get_redis_connection
import json
from Movie import movie
""" 
This class will connect to redis and load JSON data onto the redis API

establish redis connection.
db_setup 
""" 
r = get_redis_connection()

""" 
call request objects. 
transform and load item data into redis.
""" 
def load(item):
    mov = movie(item)
    r.json().set('movies:'+str(mov.id)+'', '.', json.dumps(item))
