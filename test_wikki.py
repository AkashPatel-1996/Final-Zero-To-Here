from wikibot import scrape


def test_check():
    assert 2 == scrape("facebook")
