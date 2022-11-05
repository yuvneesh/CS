import time 

def search(collection, value):
    """
    Search many times for value in a collection
    """
    for i in range(50000):
        found = value in collection

size = 10000

list_start_time = time.time()
search(list(range(1,size)), size)
list_end_time = time.time()
list_time = list_end_time - list_start_time

set_start_time = time.time()
search(set(range(1,size)), size)
set_end_timee = time.time()
set_time = set_end_timee - set_start_time

print(f"Time taken by list to search in {size} values: {list_time} seconds")
print(f"Time taken by set to search in {size} values: {set_time} seconds")