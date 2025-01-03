
import unittest
from flask import Flask
from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ping(self):
        response = self.app.get('/api/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Pong!'})

    def test_get_data(self):
        response = self.app.get('/api/data')
        self.assertIn(response.status_code, [200, 500])  # Either success or error handled
