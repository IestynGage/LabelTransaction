from unittest import TestCase
from src.labeler import Labeler

class TestIsValidLabel(TestCase):
    def test_always_passes(self):
        labelerObject = Labeler("test/resources/labels.json")
        result = labelerObject.isValidLabel("housing")
        self.assertTrue(result, "Expected label housing to be in labels.json")
