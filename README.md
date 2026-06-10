# LRU-and-event-schedular
Data Structures &amp; Systems Design Assessment  for lru and event under alml project
I used Pythons OrderedDict. This is a kind of order that combines a HashMap and a Doubly Linked List. The HashMap is really useful because it helps me find any key quickly.
The Linked List is also very helpful. It keeps track of the order in which things were used. The recently used item is at the end and the least recently used item is at the front.
When I call get() on the LRU Cache I move that key to the end. This way I know it was just used.When the LRU Cache is full and I call put() I remove the item from the front. This is because it is the recently used item.
Both of these operations are very fast. They take the amount of time every time because I do not have to search for anything or move things around. The LRU cache is very efficient.

Problem 2: Event Scheduler. My Explanation

For can_attend_all I make a list of events in the order they start. Then I check if any event starts before the previous one is over. If that happens it means there is a problem. I say no. If one event ends and another starts at the time that is okay.

For min_rooms_required I make two lists. One for when events start and one, for when they end. I sort these lists separately. Then I go through them with two pointers. Every time a new event starts before an old one ends I need another room. Every time an event ends I can use that room again. The most rooms I need at any one time is my answer.
 
A HashMap by itself gives super-fast lookup but can't keep track of the order things are used. A linked list keeps track of order. It takes a long time to find things. When we use both, the HashMap stores where to find each thing away, and the Linked List keeps track of how things are used so we can get rid of old things fast. This is the way to make both finding and adding things really fast.

Future Proofing. Assigning Room Numbers:

I would keep a list of rooms like Room A and Room B. When a meeting needs a room, I pick one from the list. When the meeting is over, the room is empty again. I would make a list that shows which room each meeting is in, like {(9,11): Room A, (10,12): Room B}.

Concurrency. Thread-Safe LRU Cache:

To make the LRU cache thread-safe, I would use a lock. This lock will be part of the LRUCache class. Before we do anything with the cache, like get something from it or put something in it, we need to get the lock.
We will let go of the lock when we are done.
This way one thing can happen to the cache at a timeThis prevents problems where two things try to change the cache at the time and cause trouble.
For example, if two things try to remove items from the LRU Cache at the same time it can cause problems.With the lock this will not happen because the LRU Cache will only let one thing happen at a time.

