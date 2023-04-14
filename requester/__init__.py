import requests
from bs4 import BeautifulSoup

class Requester(object):
    def __init__(self, url, record_path=None, convus_id=None, convus_attributes=None):
        self.url = url
        self.record_path = record_path
        self.convus_id = convus_id
        self.convus_attributes = convus_attributes
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

    def citation_attrs(self):
        source_attributes = self.meta_attrs(self.fetch_soup())
        attrs = {'reference_schema_version': '0.1',
                 'record_path': self.record_path,
                 'url': self.url,
                 'convus_id': self.convus_id,
                 'convus_attributes': self.convus_attributes,
                 'source_attributes': source_attributes}
        return attrs