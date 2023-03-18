from unittest import TestCase
from src.labeler import Labeler, Label

class TestLabeler(TestCase):
    def test_is_valid_label_true(self):
        labelerObject = Labeler("test/resources/example-labels.json")
        result = labelerObject.isValidLabel("housing")
        self.assertTrue(result, "Expected label housing to be in labels.json")

    def test_is_valid_label_false(self):
        labelerObject = Labeler("test/resources/example-labels.json")
        result = labelerObject.isValidLabel("blue")
        self.assertFalse(result, "Expected label blue to not be valid")

    def test_matches_label_true(self):
        labelerObject = Labeler("test/resources/example-labels.json")
        result = labelerObject.matchesLabel("rent")
        self.assertEqual(result, "housing")

    def test_matches_label_false(self):
        labelerObject = Labeler("test/resources/example-labels.json")
        result = labelerObject.matchesLabel("blue")
        self.assertEqual(result, "")

class TestLabel(TestCase):
    def test_matches_true(self):
        label = Label("Housing", ["rent", "internet"])
        result = label.matchLabel("rent")
        self.assertEqual(result, True)

    def test_matches_false(self):
        label = Label("Housing", ["rent", "internet"])
        result = label.matchLabel("blue")
        self.assertEqual(result, False)