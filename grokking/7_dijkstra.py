# Dijkstra's algorithm to find fastest path instead of shortest
# 1. Find the "cheapest node" - The one you can get to in the least amount of time
# 2. Update the costs of the neighbors of this node
# 3. Repeat until you've done this for every one in the graph
# 4. Calculate final path

# With Dijkstra's algorithm, you assign a number (weight) to each segment
# Then the algorithm finds the path with the smallest total weight

# Unweighted graph -> Use BFS. Weighted graph -> Use DA.
# DA only works with directed acyclic graphs (cycles / loops throw it off)
# Negative weights also break DA.
# For shortest path that has negative-weighr edges, Bellman-Ford algorithm can be used.

# DA in practice:

graph = {}
graph["you"] = ["alice", "bob", "claire"] # Neighbors of node

graph["start"] = {} # Weights of the edges
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# print(graph["start"].keys()) -> Print neighbors
# print(graph["start"]["a"]) -> Print neighbor weights
# print(graph["start"]["b"])

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {} # Finish node doesn't have any neighbors

infinity = float("inf") # Costs of each node
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = [] # Array to keep track of the already processed nodes

# Steps order:
# 1. While we have nodes to process
# 2. Grab the nodes closest to the start
# 3. Update costs for its neighbors
# 4. If any of the neighbor's costs were updated, update parents too
# 5. Mark this node processed

def main():
    node = find_lowest_cost_node(costs) # Find the lowest-cost unprocessed node
    while node is not None: # Loops is done after all nodes are processed
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys(): # Go through all neighbors of node.
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost: # If it's cheaper to get to this neighbor by going through this node...
                costs[n] = new_cost # ...update the cost for this node.
                parents[n] = node # This node becomes the new parent for this neighbor
        processed.append(node) # Mark node as processed
        node = find_lowest_cost_node(costs)

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # Go through each node
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # If it's the lowest cost so far and hasn't been processed yet...
            lowest_cost = cost # ...set is as the new lowest-cost node
            lowest_cost_node = node
    return lowest_cost_node

if __name__ == "__main__":
    main()

# RECAP
# BFS is used to calcualte the shortest path for an unweighted graph
# DA is used to calculate the shortest path for a weighted graph
# DA works when all the weights are postiive
# For negative weights, use Bellman-Ford algorithm