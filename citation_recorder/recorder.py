import yaml 

from .requester import Requester

class Recorder(object):
    def __init__(self, url, record_path=None, convus_id=None, convus_attributes=None):
        self.url = url
        self.record_path = record_path
        self.convus_id = convus_id
        self.convus_attributes = convus_attributes

    def source_attributes(self):
        return Requester(self.url).citation_attrs()

    def record_attributes(self):
        return {
            'reference_schema_version': '0.1',
            'url': self.url,
            'record_path': self.record_path,
            'convus_id': self.convus_id,
            'convus_attributes': self.convus_attributes,
            'source_attributes': self.source_attributes(),
        }

    def record_attributes_yaml(self):
        # convert dictionary to yaml
        return yaml.dump(self.record_attributes(), sort_keys=False)
    
    def write_yaml(self):
        filename = "citations/" + self.record_path + ".yaml"
        with open(filename, 'w') as f:
            f.write(self.record_attributes_yaml())

# attributes = [
#     "pay_access",
#     "title",
#     "authors",
#     "description",
#     "published_at",
#     "updated_at",
#     "word_count",
#     "doi",
#     "publisher", # og:site_name
#     "word_count",
# ]
