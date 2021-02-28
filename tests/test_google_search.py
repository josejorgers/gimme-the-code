import sys
sys.path.insert(0, 'C:\\Users\\JJ\\Desktop\\gimme-the-code\\')

from gtcode.scrapper.google_search import search

def test_google_search():

    query = "create a class in python"

    results = search(query)

    prefix = [True for r in results if r[:4] == 'http']
    
    assert len(results) > 0 and len(prefix) == len(results)