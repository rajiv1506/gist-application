import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_gists_for_user(self):
        response = self.app.post('/gists', data={'github_username': 'octocat'})
        self.assertEqual(response.status_code, 302)  

    def test_get_gists_route(self):
        response = self.app.get('/gists/testuser')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
