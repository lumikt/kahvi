from os import path
import unittest
from repositories.reference_repository import create_reference, get_reference
from config import app
from db_helper import load_schema, setup_db

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.dict = False
        project_root = path.dirname(path.abspath(__file__))
        schema_file = path.join(project_root, "../../schema.sql")
        with app.app_context():
            schema = load_schema(schema_file)
            setup_db(schema)

    def test_mandatory_info_set(self):
        with app.app_context():
            print(app.config["SQLALCHEMY_DATABASE_URI"])
            self.dict = {"citation_key": "koe1001", "author": "Mikki Hiiri", "title": "Kerhotalo",
                         "journal": "Disney.fi" , "year": 2012}
            create_reference(self.dict, "article")
            self.assertEqual(get_reference(), ["koe1001, Mikki Hiiri, Kerhotalo, Disney.fi, 2012<br>Tags: "])
