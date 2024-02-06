**README.md**

# Top Keywords Project

This is a Python project hosted on GitHub that aims to extract and analyze the top keywords from a given web page. The project includes two main scripts: `multiple_page.py` and `common_word.py`.

## Repository

Visit the GitHub repository: [Top Keywords Project](https://github.com/joshua-dada-mayowa/top_keywords/)

## Prerequisites

Make sure you have the following installed:

- Python
- requests_html library
- BeautifulSoup library

You can install the required libraries using the following:

```bash
pip install requests_html
pip install beautifulsoup4
```

## How to Use

### `multiple_page.py`

This script scrapes multiple pages of an Amazon search for DSLR cameras and prints the URL of the next page, demonstrating basic web scraping functionality.

```python
from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
url = 'https://www.amazon.co.uk/s?k=dslr+camera&i=black-friday&ref=nb_sb_noss'

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def getnextpage(soup):
    pages = soup.find('ul', {'class': 'a-pagination'})
    if not pages.find('li', {'class': 'a-disabled a-last'}):
        url = 'https://www.amazon.co.uk' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return

soup = getdata(url)
print(getnextpage(soup))
```

### `common_word.py`

This script extracts top keywords from a given URL, in this case, [http://en.wikipedia.org/wiki/In-memory_database](http://en.wikipedia.org/wiki/In-memory_database), and prints the top 50 keywords excluding common words defined in `common_words.txt`.

```python
import urllib.request
from bs4 import BeautifulSoup

def getKeywords(articletext):
    common = open("common_words.txt").read().split('\n')
    word_dict = {}
    word_list = articletext.lower().split()
    for word in word_list:
        if word not in common and word.isalnum():
            if word not in word_dict:
                word_dict[word] = 1
            if word in word_dict:
                word_dict[word] += 1
    top_words = sorted(word_dict.items(), reverse=True)[0:50]
    top50 = []
    for w in top_words:
        top50.append(w)
    return top50

url = "http://en.wikipedia.org/wiki/In-memory_database"
htmltext = urllib.request.urlopen(url).read()
soup = BeautifulSoup(htmltext, "lxml")

article = ""
for text in soup.findAll(text=True):
    article += text

print(getKeywords(article))
```

Feel free to explore, modify, and integrate these scripts into your projects. Don't forget to customize the URLs and adapt the code to your specific use case.
