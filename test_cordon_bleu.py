"""Unit tests pentru functionalitatea Cordon Bleu."""
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from gastronomie import app


class TestCordonBleu(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_gastronomie_route(self):
        response = self.client.get('/gastronomie')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gastronomie', response.data)

    def test_cordon_bleu_route(self):
        response = self.client.get('/cordon_bleu')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cordon Bleu', response.data)

    def test_descriere_route(self):
        response = self.client.get('/cordon_bleu/descriere')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cordon Bleu', response.data)

    def test_origine_route(self):
        response = self.client.get('/cordon_bleu/origine')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Elve', response.data)


if __name__ == '__main__':
    unittest.main()
