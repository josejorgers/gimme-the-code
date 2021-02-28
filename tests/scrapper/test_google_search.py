import sys
sys.path.insert(0, 'C:\\Users\\JJ\\Desktop\\gimme-the-code\\')

from gtcode.scrapper.google_search import search, get_code_from_results

def test_google_search():

    query = "create a class in python"

    results = search(query)

    prefix = [True for r in results if r[:4] == 'http']
    
    assert len(results) > 0 and len(prefix) == len(results)

def test_get_code_from_results():

    links = [
        'https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class',
        'https://www.kite.com/python/answers/how-to-find-html-elements-by-class-with-beautifulsoup-in-python'
    ]

    code = get_code_from_results(links)

    assert len(code) > 0