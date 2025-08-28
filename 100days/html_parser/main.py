from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name='a').get("href")
    article_links.append(link)

# Finding the upvotes
# If all articles on the page have upvotes, this will work:
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# However, some submissions may not have any upvotes yet.
# This uses a conditional expression to handle cases where there are no upvotes (span is None)
subtexts = soup.find_all(class_="subtext")
article_upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(
    f"Most upvoted article: {article_texts[largest_index]}\n"
    f"Number of upvotes: {article_upvotes[largest_index]} points\n"
    f"Available at: {article_links[largest_index]}."
)

# with open("website.html") as file:
#     contents = file.read()
# 
# soup = BeautifulSoup(contents, "html.parser") # For some websites the lxml module parser works better
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.p)
# 
# all_anchor_tags = soup.find_all(name="a")
# 
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href")) # Gets the value of the href attribute
# 
# heading = soup.find(name="h1", id="name")
# print(heading)
# 
# section_headings = soup.find(name="h3", class_="heading")
# print(section_headings.name)
# print(section_headings.getText())
# 
# h3_heading = soup.find_all(name="h3", class_="heading")
# print(h3_heading)
# 
# company_url = soup.select_one(selector="p a")
# print(company_url)
# 
# name = soup.select_one(selector="#name")
# print(name)
# 
# headings = soup.select(".heading")
# print(headings)