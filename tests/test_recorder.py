from citation_recorder import Requester, Recorder

def test_default_dictionary(monkeypatch):
    def mock_citation_attrs(self):
        return {'example_meta_key': 'foo bar'}
    
    monkeypatch.setattr(Requester, 'citation_attrs', mock_citation_attrs)

    target_result = {
        "reference_schema_version": "0.1",
        "record_path": "a",
        "convus_id": "b",
        "url": "http://example.com",
        "convus_attributes": {},
        "source_attributes": {'example_meta_key': 'foo bar'}
    }
    result = Recorder("http://example.com", "a", "b", {}).record_attributes()
    # print(result)
    assert result == target_result


def test_dictionary_to_yaml(monkeypatch):
    def mock_citation_attrs(self):
        return {'example_meta_key': 'foo bar'}
    
    monkeypatch.setattr(Requester, 'citation_attrs', mock_citation_attrs)

    target_result = ["convus_attributes: {}",
        "convus_id: b",
        "record_path: a",
        "reference_schema_version: '0.1'",
        "source_attributes:",
        "  example_meta_key: foo bar",
        "url: https://www.convus.org\n",
    ]


    result = Recorder("https://www.convus.org", "a", "b", {}).record_attributes_yaml()
    # print(result)
    assert result == "\n".join(target_result)

