from bs4 import BeautifulSoup # module to extract html tags and text


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser") # For some websites the lxml module parser works better
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.p)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href")) # Gets the value of the href attribute

heading = soup.find(name="h1", id="name")
print(heading)

section_headings = soup.find(name="h3", class_="heading")
print(section_headings.name)
print(section_headings.getText())

h3_heading = soup.find_all(name="h3", class_="heading")
print(h3_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)