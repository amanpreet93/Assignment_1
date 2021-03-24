import unittest
from app import app, db
from flask_testing import TestCase

class MyAppTestCase(unittest.TestCase):
    def setUp(self):
        print("here")
        self.app = app.test_client()
          

    def test_visitot(self):  
      av = self.app.post('/visitor_count',data=dict( user_id=2, item_id=2 ))
      print("here is status code",av.status_code)
      self.assertEqual(av.status_code, 200)
      
    def test_content(self):  
      vb = self.app.post('/whole_content',data=dict( user_id=2 ))
      print("here is status code",vb.status_code)
      self.assertEqual(vb.status_code, 200)
        


if __name__ == '__main__':
    unittest.main()