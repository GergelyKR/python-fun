import re

url = input("Enter a URL: ").strip()

# re.sub(pattern, replacement, string, count = 0, flags = 0)

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")