#!/usr/bin/python
# -*- coding: utf-8 -*-

# Pywikibot will automatically set the user-agent to include your username.
# To customise the user-agent see
# https://www.mediawiki.org/wiki/Manual:Pywikibot/User-agent

import pywikibot
from pywikibot.pagegenerators import WikidataSPARQLPageGenerator
from pywikibot.bot import SingleSiteBot


class WikidataQueryBot(SingleSiteBot):
    """
    Basic bot to show wikidata queries.

    See https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Pywikibot
    for more information.
    """

    def __init__(self, generator, **kwargs):
        """
        Initializer.

        @param generator: the page generator that determines on which pages
            to print
        @type generator: generator
        """
        super(WikidataQueryBot, self).__init__(**kwargs)
        self.generator = generator

    def treat(self, page):
        print(page)


if __name__ == '__main__':
    query = """SELECT DISTINCT ?itemLabel WHERE {
  ?Q wdt:P31/wdt:P279? ?item .
  ?Q rdfs:label "Elon Musk"@en
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
}
order by ?item
"""
    site = pywikibot.Site('wikidata')
    gen = WikidataSPARQLPageGenerator(query, site=site.data_repository(),
                                      endpoint='https://query.wikidata.org/sparql')
    bot = WikidataQueryBot(gen, site=site)
    bot.run()