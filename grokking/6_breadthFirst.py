# Breadth-first search is a graph based search.
# It can answer two questions:
#   - Is there a path from A to B?
#   - What is the shortest path from A to B?
# Breadth-first search is a type of tree traversal.
# It goes through each node at the same level before going deeper into the tree.


# Algorithm implementation steps (find a mango seller in your network)
# 1. Keep a queue containing the people to check
# 2. Pop a person off the queue
# 3. Check if the person is a mango seller
# 4a. If they are, you're done!
# 4b. If not, add their friends to the queue
# 5. Loop back to step 2
# 6. If the queue is empty, there are no mango sellers in your network

# Use double-ended queue function for the queue (deque)

def main():
    graph = {
        "you": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": [],
    }

    from collections import deque

    def search(name):
        search_queue = deque() # creates a new queue
        search_queue += graph["you"] # Adds all neighbors to the search queue
        searched = [] # To prevent infinite loops, add already searched people
        while search_queue: # While the queue isn't empty ...
            person = search_queue.popleft() # ... grabs the first person off the queue
            if person not in searched: # Only search this person if you haven't searched them yet
                if person_is_seller(person): # checks if the person is a mango seller
                    print(f"{person} is a mango seller!") # Yes, they are a mango seller.
                    return True
                else:
                    search_queue += graph[person] # No, they aren't a mango seller. Add their neighbors to the queue
                    searched.append(person) # Add the person to the searched list
        return False # If you reached here, noone in your network is a mango seller

    search("you")

def person_is_seller(name):
    return name[-1] == "m"

if __name__ == "__main__":
    main()

# ---

# RECAP
# - On a task list, if task A depends on task B, task A shows up later in the list (topological sort)
# - Trees are special type of graphs where no edges ever point back

# - Breadth-first search tells you if there's a path from A to B
# - If there's a path, breadth-first search tells you the shortest path
# - If you have "find shortest X" task, try model the problem as a graph and use BFS
# - A directed graph has arrows, and the relationship follows the direction of the arrow
#   (rama -> adit means "rama owes adit money")
# - Undirected graphs don't have arrows, and the relationship goes both ways
#   (ross - rachel means "ross dated rachel and rachel dated ross")
# - Queues are FIFO (First In First Out)
# - Stacks are LIFO (Last In First Out)
# - Need to check people in order they were added, so queue has to be used
# - Once you check someone, make sure you don't check them again (otherwise can trigger infinite loop)