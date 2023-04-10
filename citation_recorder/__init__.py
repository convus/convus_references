import yaml 

class CitationRecorder:
    attributes = [
        "pay_access",
        "title",
        "authors",
        "description",
        "published_at",
        "updated_at",
        "word_count",
        "doi",
        "publisher",
        "cannonical_url"
    ]
    main_attributes = {
        "recorder_schema_version": "1",
        "record_path": "",
        "convus_id": "",
        "url": "",
    }

    def default_dict():
        # merge main_attributes, source_attributes and convus_attributes
        dd = CitationRecorder.main_attributes | {"source_attributes": dict.fromkeys(CitationRecorder.attributes, "")} | {"convus_attributes": {}}
        return dd
    
    def dictionary_to_yaml(dictionary):
        # convert dictionary to yaml
        return yaml.dump(dictionary, sort_keys=True)
    
