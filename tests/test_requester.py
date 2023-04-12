from requester import CitationSpider

# Following along this:
# https://stackoverflow.com/questions/6456304/scrapy-unit-testing

def test_recorder():
    url = "https://www.example.com"
    requester = Requester(url)
    assert requester.url == url
