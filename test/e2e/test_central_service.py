import requests 
import pytest

URL = 'http://localhost:8081/services'
SERVICE_URL = 'http://localhost:8081/service'

class TestServices():
    @pytest.fixture(autouse=True)
    def setup(self):
        resp = requests.post('{}/init'.format(URL))
        print('Services loaded')
        
    def test_list_services(self):
        resp = requests.get(URL)
        assert(resp.status_code == 200)
        services = resp.json()
        assert('service_names' in services)
        
    def test_add_service(self):
        name = 'testService'
        resp = requests.get(URL)
        assert(resp.status_code == 200)
        out = resp.json()
        services = out['service_names']
        number_of_services = len(services)
        resp = requests.post(URL, json={'name': name, 'url': 'http://localhost:5005/test'})
        assert(resp.status_code == 201)
        resp = requests.get(URL)
        out = resp.json()
        new_services = len(out['service_names'])
        assert(new_services == (number_of_services+1))

    def test_delete_service(self):
        resp = requests.get(URL)
        service_names = resp.json()['service_names']
        number_of_services = len(service_names)
        name = service_names[0]
        resp = requests.delete(URL, json={'name': name})
        assert(resp.status_code == 204)
        
    def test_delete_service_service_not_exist(self):
        resp = requests.get(URL)
        service_names = resp.json()['service_names']
        number_of_services = len(service_names)
        name = '12345'
        resp = requests.delete(URL, json={'name': name})
        assert(resp.status_code == 404)

    def test_service_wordcount(self):
        service_name = 'wordcount'
        resp = requests.post(SERVICE_URL, json={'service': service_name, 'text': 'This is a test'})
        assert(resp.status_code == 200)
        out = resp.json()
        words_count = out['Words_count']
        assert(words_count == 4)
        
    def test_service_sentiment(self):
        service_name = 'sentiment'
        resp = requests.post(SERVICE_URL, json={'service': service_name, 'text': 'I am so happy!'})
        assert(resp.status_code == 200)
        assert(resp.json()['sentiment'] == 'positive')
        
    def test_service_entity_recognition(self):
        service_name = 'entityrecognition'
        resp = requests.post(SERVICE_URL, json={'service': service_name, 'text': 'test'})
        assert(resp.status_code == 200)
        