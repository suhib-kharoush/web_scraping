import requests
from bs4 import BeautifulSoup
import json

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    result_list = list(result)
    length = len(result_list)
    return f'{length}'


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result1 = soup.find('div', class_="mw-parser-output")
    txt=[]
    paragraphs = result1.find_all('p')
    for p in paragraphs:
        p2 = p.find('span',string=lambda text: 'citation needed' in text)
        if p2 :
            txt.append(p.text.strip())
    file_content = json.dumps(txt)
    with open('paragraphs.json', 'w') as f:
        f.write(file_content)

    for a in txt:
        print(a)
    return txt




if __name__=='__main__':
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
