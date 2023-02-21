# make sure you fork this and git repo it
# go to the shell command screen and type
# pip install -r requirements.txt
#to install the necessary components
import requests
from bs4 import BeautifulSoup

# get the html
url = "https://www.amazon.com/Best-Sellers-Books/zgbs/books"
headers = {
  'user-agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
#get all books
books = soup.find_all(id="gridItemRoot")
#get info from first book
print(books[0])
book = books[0]
rank = book.find('span', class_='zg-bdg-text').text[1:]
print(rank)
title = '_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'