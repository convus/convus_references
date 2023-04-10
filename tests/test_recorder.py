from citation_recorder import CitationRecorder  

def test_something():
    assert 1 == 1

def test_anotherthing():
    target_keys = ["recorder_schema_version", "record_path"]  
    # print(CitationRecorder.default_dict())
    assert list(CitationRecorder.default_dict().keys()) == target_keys
