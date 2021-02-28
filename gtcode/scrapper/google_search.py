import requests
from bs4 import BeautifulSoup



def search(query: str) -> list:
    '''
    Returns a list of strings that are the links of the results
    '''

    words = query.split(' ')
    words = [w.lower() for w in words]

    url = 'https://google.com/search?q='

    for w in words[:-1]:
        url += w + '+'
    url += words[-1]

    page = get_search_result_page(url)

    return get_list_of_links(page)
    

def get_search_result_page(url: str):
    '''
    Returns a BeatifulSoup parsed content of the page referenced by the
    'url'
    '''

    page = requests.get(url)

    return BeautifulSoup(page.content, 'html.parser')


def get_list_of_links(page) -> list:

    '''
    Given a BeautifulSoup parsed page that represents a Google search
    result, returns the list of links in to the results

    Parameters:
        page: BeautifulSoup parsed Google Search results page

    Returns:
        list of strings representing the links of the results
    '''
    results_html = page('div', class_='kCrYT')

    # Not all results have an anchor and 'href' starts with '/url?q='
    return list([r.find('a')['href'][7:] for r in results_html if r.find('a')])
