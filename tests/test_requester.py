import betamax
import requests

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/cassettes'
    config.preserve_exact_body_bytes = True

session = requests.Session()
recorder = betamax.Betamax(session)

from citation_recorder import Requester

def test_meta_attributes(betamax_recorder):
    with recorder.use_cassette("mendo_voice"):
        url = "https://mendovoice.com/2023/02/fort-braggs-new-crisis-team-gets-thumbs-up-from-controversial-homeless-expert"
        requester = Requester(url)
        assert requester.url == url
        meta_attrs = requester.meta_attrs(requester.fetch_soup())
        assert meta_attrs["description"] == 'The first in series from reporter Frank Hartzell.\nShare this:TwitterFacebook'
        target_keys = ['description', 'og:locale', 'og:type', 'og:title', 'og:description', 'og:url', 'og:site_name', 'article:publisher', 'article:published_time', 'article:modified_time', 'og:image', 'og:image:width', 'og:image:height', 'og:image:type', 'author', 'twitter:card', 'twitter:creator', 'twitter:site', 'generator', 'news_keywords', 'original-source', 'syndication-source', 'standout', 'msapplication-TileImage', 'logo', 'datePublished', 'dateModified', 'image']
        assert len(meta_attrs.keys()) == len(target_keys)

def test_citation_attributes(betamax_recorder):
    with recorder.use_cassette("mendo_voice"):
        url = "https://mendovoice.com/2023/02/fort-braggs-new-crisis-team-gets-thumbs-up-from-controversial-homeless-expert"
        requester = Requester(url)
        citation_attrs = requester.citation_attrs()
        target_attribute_keys = ['description', 'og:locale', 'og:type', 'og:title', 'og:description', 'og:url', 'og:site_name', 'article:publisher', 'article:published_time', 'article:modified_time', 'og:image', 'og:image:width', 'og:image:height', 'og:image:type', 'author', 'twitter:card', 'twitter:creator', 'twitter:site', 'generator', 'news_keywords', 'original-source', 'syndication-source', 'standout', 'msapplication-TileImage', 'logo', 'datePublished', 'dateModified', 'image']
        assert list(citation_attrs.keys()) == target_attribute_keys
