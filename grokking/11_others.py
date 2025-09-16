"""
A Binary Search Tree (BST) is a type of binary tree with a special ordering rule:
Each node has up to two children: a left and a right.

For any given node:
All values in the left subtree are smaller than the node’s value.
All values in the right subtree are larger than the node’s value.
This property makes searching, inserting, and deleting efficient (on average O(log n) time if the tree is balanced).
"""

"""
The BST will look like this:

        8
       / \
      3   10
     / \     \
    1   6     14
       / \    /
      4   7  13


Left subtree of 8 contains values smaller than 8 → {3,1,6,4,7}.
Right subtree of 8 contains values greater than 8 → {10,14,13}.
"""

# ---

"""
An inverted index is a data structure that maps words (terms) → to the documents (or locations) where those words occur.
It’s called "inverted" because instead of storing documents → words (the natural way), we flip it to store words → documents.

Suppose we have three tiny documents:

Doc1: "the cat sat on the mat"
Doc2: "the dog sat on the log"
Doc3: "the cat chased the dog"

Step 1: Tokenize
Break each document into words (ignoring punctuation, lowercase, etc.).

Doc1 → ["the", "cat", "sat", "on", "the", "mat"]
Doc2 → ["the", "dog", "sat", "on", "the", "log"]
Doc3 → ["the", "cat", "chased", "the", "dog"]

Step 2: Build the Inverted Index
For each unique word, store a list of documents (and optionally positions) where it occurs:

"the"    → [Doc1, Doc2, Doc3]
"cat"    → [Doc1, Doc3]
"sat"    → [Doc1, Doc2]
"on"     → [Doc1, Doc2]
"mat"    → [Doc1]
"dog"    → [Doc2, Doc3]
"log"    → [Doc2]
"chased" → [Doc3]

"""

# ---

"""
The Fourier Transform is a way of answering:
“What frequencies make up this signal?”
Just like a prism splits white light into its component colors (wavelengths),
the Fourier Transform splits any signal (sound, image, time-series) into its component frequencies.

Any signal can be expressed as a sum of sine and cosine waves.
The Fourier Transform tells you how much of each frequency is present.
It’s like saying:
This signal = 0.7 × sin(440Hz) + 0.3 × sin(880Hz) + ...
"""

# ---

"""
Parallel algorithms to process huge datasets:

MapReduce
MapReduce is a programming model for processing large datasets in parallel. You write two functions:
Map: processes input (usually a chunk of a file) and emits key/value pairs.
Reduce: receives all values for a given key and combines them to produce final output for that key.
Between Map and Reduce there’s a shuffle + sort step that groups all values for the same key together and sends each group to one reducer.

Example:

Documents (raw):
doc1: "Hello world hello"
doc2: "Hello MapReduce"
doc3: "World of MapReduce hello"

Normalize to lowercase first. The goal: count how many times each word appears across all docs.

1) Map phase (run in parallel on each input split)
Each map task reads one document and emits (word, 1) for every word.
Map outputs (after normalizing to lowercase):

From doc1 → hello:1, world:1, hello:1 (i.e. ("hello",1),("world",1),("hello",1))
From doc2 → hello:1, mapreduce:1
From doc3 → world:1, of:1, mapreduce:1, hello:1

2) Shuffle & Sort (group by key)

The system collects all map outputs, groups values by key and typically sorts keys. Example grouped form:

hello → [1, 1, 1, 1] (two from doc1, one from doc2, one from doc3)
world → [1, 1] (one from doc1, one from doc3)
mapreduce → [1, 1]
of → [1]

Partitioning decides which reducer gets which key (commonly hash(key) % num_reducers), ensuring all values for a key go to the same reducer.

3) Reduce phase (run in parallel, one reducer per set of keys it receives)

Each reducer receives (key, list_of_values) and combines them, e.g. by summation.

hello → sum([1,1,1,1]) = 4
world → 2
mapreduce → 2
of → 1

Final output: { hello:4, world:2, mapreduce:2, of:1 }

Important implementation details & why MapReduce scales - - -
Input splitting: the input is split (e.g., HDFS blocks) so many mappers can run in parallel on different machines.
Data locality: mappers ideally run where the input block lives to avoid network transfer.
Shuffle: network-intensive stage — map outputs are transferred across the cluster to the reducers.
Partitioner: decides which reducer receives a given key (commonly hash(key) % R).
Combiner (optional): local reduce run on mapper outputs to reduce the volume of data sent over the network (useful for associative+commutative operations like sum).
Fault tolerance: if a map or reduce task fails, the master re-launches it on another node (map outputs are on disk so reducers can fetch again).
Sorting: reducers usually receive keys sorted — useful if reduce logic expects ordered keys.

When to use MapReduce — and when not - - -

Use MapReduce when:
You have large batch jobs over huge datasets (TB+).
Problem fits "map (emit key/value) — reduce (combine values)" pattern (e.g., counts, sums, joins, distributed grep).

Avoid MapReduce for:
Low-latency or iterative algorithms (many machine learning algorithms) — frameworks like Spark (in-memory) are often faster.
Complex workflows that require many chained jobs unless orchestration is provided.
"""

# ---

"""
Bloom filters

A Bloom filter is a probabilistic data structure used to test if an element is possibly in a set or definitely not in the set.
It can have false positives (says “yes” when the element isn’t really in the set).
It has no false negatives (if it says “no”, the element is guaranteed not to be in the set).

So:
“No” means absolutely not in the set.
“Yes” means maybe (probably in the set, but could be false positive).

How does it work?

A Bloom filter is just:
A bit array of size m (all initially 0).
A set of k hash functions that map an input to k positions in the bit array.

Adding an element:

Hash the element with all k hash functions.
Set the corresponding k bits in the array to 1.

Checking membership:

Hash the element with all k functions.
If any of those bits is 0, the element is definitely not in the set.
If all are 1, then the element is probably in the set.

Example:
Say we have a Bloom filter of length 10 bits (all zeros at start), with 3 hash functions.

Step 1: Insert "orange"

Hash functions return positions: 2, 5, 7
Set those bits to 1.

Bit array now:
Index: 0 1 2 3 4 5 6 7 8 9
Bits:  0 0 1 0 0 1 0 1 0 0

Step 2: Insert "grapefruit"

Hashes return: 1, 5, 9
Set those bits to 1.

Now:
Index: 0 1 2 3 4 5 6 7 8 9
Bits:  0 1 1 0 0 1 0 1 0 1

Step 3: Query "orange"

"orange" → hashes 2, 5, 7
All bits at 2, 5, 7 are 1 → so "orange" is probably present.

Step 4: Query "apple"

"apple" → suppose hashes 0, 3, 7
Bit at index 0 is still 0 → so "apple" is definitely not present.
"""

# ---

"""
HyperLogLog (HLL) is a probabilistic algorithm for estimating the cardinality (number of unique elements) in a dataset.

Instead of storing all elements (which can be huge), it uses a fixed-size data structure.
Provides an approximate count with small, controllable error (often 2-3%).
Very memory-efficient: can count billions of unique elements using just a few kilobytes.

🧠 Intuition
1. Hash each element into a binary string.
2. Count the number of leading zeros in the hash.
    Random hashes have more leading zeros for rarer elements.
    This gives an estimate of how many unique elements exist.

3. Split the hash space into buckets (registers).
    Keep track of the maximum number of leading zeros in each bucket.
4. Combine the statistics across all buckets to get the final cardinality estimate.
"""