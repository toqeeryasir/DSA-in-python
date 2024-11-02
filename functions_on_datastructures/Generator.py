# Generators are objects those don't use memory unlike lists or othere objects like dicts or sets or tuples.
# They only produce items at the time of use.
values = (x * 2 for x in range(100000000000))
print(values) # It will not print any_thing.

# If we wanna check how memory efficient generator is.
from sys import getsizeof

print(getsizeof(values)) # It  only takes few bytes of memory, 200 bytes <- arbitrary value.

# But if we check list.
values = [x*2 for x in range(1000000)]
print(getsizeof(values)) # It takes too much bytes of memory, 8448728 bytes <- arbitrary value.
