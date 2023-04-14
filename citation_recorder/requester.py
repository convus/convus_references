import requests
from bs4 import BeautifulSoup

class Requester(object):
    def __init__(self, url):
        self.url = url
        self.soup = None

    def get_url(self):
        page = requests.get(self.url)
        return page
    
    # I'm not sure if this is the best way to do this. Memoization?
    def fetch_soup(self):
        if self.soup == None:
            self.soup = BeautifulSoup(self.get_url().text, 'html.parser')
        return self.soup
    
    def meta_attrs(self, soup):
        meta_elements = soup.find_all('meta')
        attrs = {}
        ignored_meta_keys = ['viewport', 'csrf-token', 'csrf-param', 'google-site-verification', 'robots']
        for meta in meta_elements:
            # print(meta.attrs)
            if 'name' in meta.attrs:
                key = meta.attrs['name']
            elif 'property' in meta.attrs:
                key = meta.attrs['property']
            elif 'itemprop' in meta.attrs:
                key = meta.attrs['itemprop']
            else:
                print("No name or property in meta element: ", meta.attrs)
                continue
            if key in ignored_meta_keys:
                continue

            attrs[key] = meta.attrs['content']
        return attrs

    # This will be more sophisticated in the future. Right now, it's just the meta attributes
    def citation_attrs(self):
        source_attributes = self.meta_attrs(self.fetch_soup())
        return source_attributes
    