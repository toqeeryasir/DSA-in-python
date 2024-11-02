# Our normal ;ost is not worthy to use for creating queue, because when we remove an item from our queue, we have to shift all of out items to the left side to fill the gap of the last index.
# So we can use d_queue object that also deals with lists with more methodes.
# To do so we need to import d_queue object.
from collections import deque

first_queue = deque([]) # Here i passed an empty list to convert it to dequeue object.

# By using append methode we can add an item in our queue.
first_queue.append("toqeer")
first_queue.append("faizan")
first_queue.append("abdullah")
print(first_queue)

# To remove an item from our queue we use popleft methode.
first_queue.popleft()
first_queue.popleft()
print(first_queue)
first_queue.popleft()

# To check is our queue is empty or not we can use if statemnt with not operator.
if not first_queue:
    print("Queue is empty!")
print(first_queue)