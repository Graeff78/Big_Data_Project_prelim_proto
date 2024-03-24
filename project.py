from QueryPackage import *
from APIHandler import *
import timeit

start_time = timeit.default_timer()
fetch_response()
first_query()
second_query()
third_query()
fourth_query()
end_time = timeit.default_timer()
print(f"\n\n\ntime\t: {end_time - start_time}")