# Greedy algorithms can be used where an exact algorithm would take too much time. (Traveling salesperson / "NP-Complete" problems)
# For these cases we use approximations to solve the problem.

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Sets are useful here as they allow no duplicates
stations = {} # List of stations to choose from
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

# Set operations: intersection (&), union (|), difference (-), symmetric difference (^)

while states_needed:
    best_station = None # Station that covers the most uncovered states
    states_covered = set() # Set of all the states this station covers that haven't been covered yet
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)

# How to recognize NP-Complete problems?
# Algorithm runs quickly with a few times, but really slows with more items
# "All combinations of X" usually point to an NP-complete problem
# "Calculate every possible version" that' can't be broken to smaller sub-problems is usually NP-complete
# If the problem involves a sequence (like cities) and it's hard to solve, likely NP-complete
# If the problem involves a set (like set of radio stations) and it's hard to solve, likely NP-complete
# Can you restate the problem as the set-covering problem or traveling-salesperson problem? Definitely NP-complete

# RECAP
# Greedy algorithms optimize locally, hoping to end up with a global optimum
# NP-complete problems have no known fast solution
# If you have an NP-complete problem, better use an approximation algorithm
# Greedy algorithms are easy to write and fast to run, making them good approx. algorithms