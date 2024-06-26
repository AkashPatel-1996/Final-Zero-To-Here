from wikibot import scrape, scrape_withoutCli


def test_check():
    result = "Narendra Damodardas Modi (Gujarati: [ˈnəɾendɾə dɑmodəɾˈdɑs ˈmodiː] ; born 17 September 1950) is an Indian politician who has served as the 14th Prime Minister of India since 26 May 2014."
    assert result == scrape_withoutCli("narendra modi")