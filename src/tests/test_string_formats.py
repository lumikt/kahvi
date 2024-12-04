import unittest

from repositories.reference_repository import reference_to_html_string, reference_to_text_string

class StringTest(unittest.TestCase):
    def setUp(self):
        self.article_dict = {"id":1, "ref_type":"article", "citation_key":"article_test_case","author":"Jane Doe", "title":"Testing",
                            "journal":"Journal","year":"2024"}

        self.in_proceedings_dict = {"id":"1","ref_type":"inproceedings", "citation_key":"inproceedings_test_case","author":"Jane Doe", 
                                    "booktitle":"Testing","year":"2024", "volume":"2"}
        
        self.book_dict = {"id":"1","ref_type":"book", "citation_key":"book_test_case","author":"Jane Doe", "title":"Testing",
                            "publisher":"Testing Publisher","year":"2024"}

    def test_article_text_string_conversion(self):
        correct_format = """@ARTICLE{article_test_case,\n   author = "Jane Doe",\n   title = "Testing",\n   journal = "Journal",\n   year = "2024"\n }\n\n"""
        formatted_string =reference_to_text_string(self.article_dict)
        self.assertEqual(formatted_string, correct_format)

    def test_inproceedings_string_conversion(self):
        correct_format = """@INPROCEEDINGS{inproceedings_test_case,\n   author = "Jane Doe",\n   booktitle = "Testing",\n   year = "2024",\n   volume = "2"\n }\n\n"""
        formatted_string =reference_to_text_string(self.in_proceedings_dict)
        self.assertEqual(formatted_string, correct_format)

    def test_book_string_conversion(self):
        correct_format = """@BOOK{book_test_case,\n   author = "Jane Doe",\n   title = "Testing",\n   publisher = "Testing Publisher",\n   year = "2024"\n }\n\n"""
        formatted_string =reference_to_text_string(self.book_dict)
        self.assertEqual(formatted_string, correct_format)
