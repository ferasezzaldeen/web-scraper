import requests
from bs4 import BeautifulSoup


URL='https://en.wikipedia.org/wiki/History_of_Mexico'
# page=   requests.get(URL)
# print(page.content)



def get_citations_needed_count(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('span',text='citation needed')
    return len(result)

def  get_citations_needed_report(url):
    sol = ''
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('p')
    # print(result)
    for x in result:
        # print(x)
        if x.findChildren('span'):
            sol+=x.text
            sol+='\n'

    return sol 




print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))