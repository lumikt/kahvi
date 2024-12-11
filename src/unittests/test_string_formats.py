import unittest
from util import reference_to_string

class StringTest(unittest.TestCase):
    def setUp(self):
        self.article_dict = {"id":1, "ref_type":"article", "citation_key":"article_test_case","author":"Jane Doe", "title":"Testing",
                            "journal":"Journal","year":"2024"}

        self.in_proceedings_dict = {"id":"1","ref_type":"inproceedings", "citation_key":"inproceedings_test_case","author":"Jane Doe", 
                                    "booktitle":"Testing","year":"2024", "volume":"2"}
        
        self.book_dict = {"id":"1","ref_type":"book", "citation_key":"book_test_case","author":"Jane Doe", "title":"Testing",
                            "publisher":"Testing Publisher","year":"2024"}

    def test_article_text_string_conversion(self):
        correct_format = """@ARTICLE{article_test_case,\n   author = "Jane Doe",\n   title = "Testing",\n   journal = "Journal",\n   year = "2024"\n}\n"""
        formatted_string =reference_to_string(self.article_dict, False)
        self.assertEqual(formatted_string, correct_format)

    def test_inproceedings_text_string_conversion(self):
        correct_format = """@INPROCEEDINGS{inproceedings_test_case,\n   author = "Jane Doe",\n   booktitle = "Testing",\n   year = "2024",\n   volume = "2"\n}\n"""
        formatted_string =reference_to_string(self.in_proceedings_dict, False)
        self.assertEqual(formatted_string, correct_format)

    def test_book_text_string_conversion(self):
        correct_format = """@BOOK{book_test_case,\n   author = "Jane Doe",\n   title = "Testing",\n   publisher = "Testing Publisher",\n   year = "2024"\n}\n"""
        formatted_string =reference_to_string(self.book_dict, False)
        self.assertEqual(formatted_string, correct_format)

    def test_article_html_string_conversion(self):
        correct_format = """@ARTICLE{article_test_case,<br>&nbsp;&nbsp;&nbsp;author = "Jane Doe",<br>&nbsp;&nbsp;&nbsp;title = "Testing",<br>&nbsp;&nbsp;&nbsp;journal = "Journal",<br>&nbsp;&nbsp;&nbsp;year = "2024"<br>}<br>"""
        formatted_string =reference_to_string(self.article_dict, True)
        self.assertEqual(formatted_string, correct_format)

    def test_inproceedings_html_string_conversion(self):
        correct_format = """@INPROCEEDINGS{inproceedings_test_case,<br>&nbsp;&nbsp;&nbsp;author = "Jane Doe",<br>&nbsp;&nbsp;&nbsp;booktitle = "Testing",<br>&nbsp;&nbsp;&nbsp;year = "2024",<br>&nbsp;&nbsp;&nbsp;volume = "2"<br>}<br>"""
        formatted_string =reference_to_string(self.in_proceedings_dict, True)
        self.assertEqual(formatted_string, correct_format)

    def test_book_html_string_conversion(self):
        correct_format = """@BOOK{book_test_case,<br>&nbsp;&nbsp;&nbsp;author = "Jane Doe",<br>&nbsp;&nbsp;&nbsp;title = "Testing",<br>&nbsp;&nbsp;&nbsp;publisher = "Testing Publisher",<br>&nbsp;&nbsp;&nbsp;year = "2024"<br>}<br>"""
        formatted_string =reference_to_string(self.book_dict, True)
        self.assertEqual(formatted_string, correct_format)