
# PROBLEM 1: LRU Cache Implementation


from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # Set the max size of cache
        self.capacity = capacity
        # OrderedDict keeps track of order (most recent at end)
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # If key doesn't exist, return -1
        if key not in self.cache:
            return -1
        # Move this key to end = mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If key already exists, update and mark as recent
        if key in self.cache:
            self.cache.move_to_end(key)
        # Add/update the key
        self.cache[key] = value
        # If over capacity, remove least recently used (front)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

            # ============================================================
# PROBLEM 2: Event Scheduler
# ============================================================

# For can_attend_all():
# I sort events by start time, then check if any event starts
# before the previous one ends. If yes = overlap = return False.

# For min_rooms_required():
# I separate all start and end times and sort them.
# I use two pointers - one for starts, one for ends.
# When a new meeting starts before another ends = need new room.
# When a meeting ends = that room is free.
# The maximum rooms needed at any moment = my answer.

def can_attend_all(events):
    # Handle empty list
    if not events:
        return True

    # Sort events by their start time
    sorted_events = sorted(events, key=lambda x: x[0])

    # Check each pair of consecutive events
    for i in range(1, len(sorted_events)):
        current_start = sorted_events[i][0]
        previous_end = sorted_events[i - 1][1]

        # If current starts BEFORE previous ends = overlap
        # Note: equal times are NOT overlaps (per requirement)
        if current_start < previous_end:
            return False

    return True


def min_rooms_required(events):
    # Handle empty list
    if not events:
        return 0

    # Separate and sort all start times and end times
    start_times = sorted([e[0] for e in events])
    end_times = sorted([e[1] for e in events])

    rooms_needed = 0      # current rooms in use
    max_rooms = 0         # maximum rooms needed at any point
    i = 0                 # pointer moving through start times
    j = 0                 # pointer moving through end times

    while i < len(start_times):
        if start_times[i] < end_times[j]:
            # New meeting starts before one ends = need new room
            rooms_needed += 1
            i += 1
        else:
            # A meeting ended = free up a room
            rooms_needed -= 1
            j += 1

        # Track the maximum
        max_rooms = max(max_rooms, rooms_needed)

    return max_rooms
# ============================================================
# TEST CASES - To verify everything works
# ============================================================

print("=" * 50)
print("TESTING PROBLEM 1: LRU Cache")
print("=" * 50)

lru = LRUCache(3)
lru.put(1, "A")
lru.put(2, "B")
lru.put(3, "C")
print("Cache after adding 1,2,3:", list(lru.cache.keys()))

lru.put(4, "D")  # Should evict key 1
print("Cache after adding 4 (evicts 1):", list(lru.cache.keys()))

print("Get key 2:", lru.get(2))  # Should return "B"
print("Get key 1:", lru.get(1))  # Should return -1 (evicted)

print()
print("=" * 50)
print("TESTING PROBLEM 2: Event Scheduler")
print("=" * 50)

events1 = [(9, 10), (10, 11), (11, 12)]
print("Events:", events1)
print("Can attend all?", can_attend_all(events1))      # True
print("Rooms required:", min_rooms_required(events1))  # 1

events2 = [(9, 11), (10, 12), (11, 13)]
print()
print("Events:", events2)
print("Can attend all?", can_attend_all(events2))      # False
print("Rooms required:", min_rooms_required(events2))  # 2

events3 = [(9, 10), (9, 11), (9, 12)]
print()
print("Events:", events3)
print("Can attend all?", can_attend_all(events3))      # False
print("Rooms required:", min_rooms_required(events3))  # 3