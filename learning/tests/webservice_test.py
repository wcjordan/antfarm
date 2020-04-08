import requests

BASE_URL = 'http://localhost:8000/'
DEFAULT_HEADERS = {'content-type': 'application/json'}

def test_start_training_run():
    headers = {
        'X-HTTP-Method-Override': 'POST',
    }
    headers.update(DEFAULT_HEADERS)
    req = requests.post(
        '{}start_training_run'.format(BASE_URL),
        headers=headers)

    assert req.status_code == 200, 'Expected status 200, received {}.'.format(req.status_code)
    assert req.json() == {'test':'testy'}