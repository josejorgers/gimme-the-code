import requests
from bs4 import BeautifulSoup

from gtcode.extract import get_python_code

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


def get_code_from_results(result_links):
    '''
    Get the code fragments from the results

    Parameters:
        result_links: list of links
    Returns:
        list of code fragments
    '''

    return list(map(get_code_from_result, result_links))

def get_code_from_result(link: str) -> str:

    content = requests.get(link).content
    content = BeautifulSoup(content, 'html.parser').prettify()

    return get_python_code(content)