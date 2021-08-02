import unittest
import json
from flask import request
from app import app


class TestAPI(unittest.TestCase):
    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={'sentence': 'A human walks on a Moon'})
            assert response._status_code == 200

    def test_ner_endpoint_given_json_body_with_known_entities_return_entity_result_in_response(self):
        with app.test_client() as client:
            response = client.post('/ner', json={'sentence': 'New York is an amazing city where Barrack Obama lives'})
            data = json.loads(response.get_data())
            assert len(data['entities']) > 0


if __name__ == '__main__':
    unittest.main()
