import unittest
from repositories.reference_repository import create_reference, get_reference

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.dict = False

    def test_mandatory_info_set(self):
        self.dict = {"author": "Mikki Hiiri", "title": "Kerhotalo", "journal": "Disney.fi" , "year": 2012}
        create_reference(self.dict)
        self.assertEqual(get_reference(), ["Mikki Hiiri", "Kerhotalo", "Disney.fi", 2012])