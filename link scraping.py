import validators
from bs4 import BeautifulSoup
import requests

url_input = input("Enter a wikipedia url")
if validators.url(url_input):
    pass
else:
    print("Not a valid url")

n = int(input(" Enter an integer "))
if n<=20 and n>=1:
    pass
else:
    print(" Not a valid input ")

count = 0
wiki_links = []
def get_wiki_links(soup,n):
    if n:
        for link in soup.find_all('a'):
            if str(link.get('href')).startswith('/wiki/'):
                full_url = 'https://wikipedia.org/'+str(link.get('href'))
                wiki_links.append(full_url)
                reqs = requests.get(full_url)
                soup = BeautifulSoup(reqs.text, 'html.parser')
                print(n)
                get_wiki_links(soup,n-1)
            else:
                pass

   

reqs = requests.get(url_input)
soup = BeautifulSoup(reqs.text, 'html.parser')
wiki_links = get_wiki_links(soup,n)
print(wiki_links)











