#!/bin/python

import unittest

from recorder.recorder import Recorder

print("WTFFFFF")

class TestRecorder(unittest.TestCase):
    def test_default_dict(self):
        """
        Test this it returns the expected structure
        """
        print("fffffff-------")
        target_keys = ["recorder_schema_version", "record_path"]
        result = Recorder.default_dict()
        print(result)
        print(result.keys())
        self.assertEqual(result.keys(), target_keys)

if __name__ == '__main__':
    unittest.main()