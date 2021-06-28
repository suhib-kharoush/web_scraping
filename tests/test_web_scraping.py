from web_scraping import __version__
from web_scraping.web_scraping import URL, get_citations_needed_count, get_citations_needed_report 

def test_version():
    assert __version__ == '0.1.0'


def test_get_citation_needed_count():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_count(URL)
    expected = '5'
    assert actual == expected


def test_get_citation_needed_report():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = len(get_citations_needed_report(URL))
    expected = 4
    assert actual == expected

def test_get_citation_needed_report_1():
    URL= 'https://en.wikipedia.org/wiki/History_of_Mexico'
    arr = get_citations_needed_report(URL)
    actual = arr[0]
    expected = "The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence."
    assert actual == expected

