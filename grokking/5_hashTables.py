book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book)
print(book["avocado"])

# ---

phone_book = {}

phone_book["John"] = "555-1234"
phone_book["Alice"] = "555-5678"
phone_book["Bob"] = "555-9012"

print(phone_book["Alice"])

# --- Voting

voted = {}

def check_voter(name):
    if voted.get(name):
        print("Already voted")
    else:
        voted[name] = True
        print("Eligible to vote")

# --- Website caching

# cache = {}
# 
# def get_page(url):
#     if cache.get(url):
#         return cache[url]
#     else:
#         data = get_data_from_server(url)
#         cache[url] = data
#         return data
        
# RECAP 1
# Hashes are good for
# - modeling relationships from one thing to another thing
# - filtering out duplicates
# - caching/memorizing data instead of working the backend server
        
# - Usually programming languages have built-in hash-tables
# - They are fast at searching, inserting and deletion
# - You can make a hash table by combining a hash function with an array
# - Collisions are bad, you need a hash function that minimizes collisions
# - Load factor is the ratio of the number of elements to the size of the hash table
#   - Time to resize if the load factor is greater than .07
        