# tests/test_app.py
import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.app.get('/about') 
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.app.get('/contact') 
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.get('/login') 
        self.assertEqual(response.status_code, 200)

    def test_devOps(self):
        response = self.app.get('/devops')  
        self.assertEqual(response.status_code, 200)

   
    #def test_failure(self):
        # Este teste sempre falhará
        #self.assertEqual(1, 2)  # Isso irá falhar
        
    def test_success(self):
       self.assertEqual(1, 1)  # Este deve passar

if __name__ == "__main__":
    unittest.main()
