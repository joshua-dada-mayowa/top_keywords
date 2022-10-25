from requests_html import HTMLSession
from bs4 import BeautifulSoup

s= HTMLSession()
url='https://www.amazon.co.uk/s?k=dslr+camera&i=black-friday&ref=nb_sb_noss'

def getdata(url):
    r =s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def getnextpage(soup):
    pages = soup.find('ul', {'class': 'a-pagination'})
    if not pages.find('li', {'class': 'a-disabled a-last'}):
        url = 'https://www.amazon.co.uk' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return
soup=getdata(url)
print(getnextpage(soup))