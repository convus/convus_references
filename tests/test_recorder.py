from citation_recorder import CitationRecorder  

def test_default_dictionary():
    default_dict = {
        "recorder_schema_version": "1",
        "record_path": "",
        "convus_id": "",
        "url": "",
        "convus_attributes": {},
        "source_attributes": {
            "pay_access": "",
            "title": "",
            "authors": "",
            "description": "",
            "published_at": "",
            "updated_at": "",
            "word_count": "",
            "doi": "",
            "publisher": "",
            "cannonical_url": "",
            "word_count": "",
            "og:image": "",
        }
    }
    target_keys = ["recorder_schema_version", "record_path"]
    assert CitationRecorder.default_dict() == default_dict

# def test_dictionary_to_yaml():
#     target = """
# convus_attributes: {}
# convus_id: ''
# record_path: ''
# recorder_schema_version: '1'
# source_attributes:
#     authors: ''
#     cannonical_url: ''
#     description: ''
#     doi: ''
#     og:image: ''
#     pay_access: ''
#     published_at: ''
#     publisher: ''
#     title: ''
#     updated_at: ''
#     word_count: ''
# url: ''
#     """
#     result = CitationRecorder.dictionary_to_yaml(CitationRecorder.default_dict())
#     print(result)
#     print(target)
#     assert result == target
