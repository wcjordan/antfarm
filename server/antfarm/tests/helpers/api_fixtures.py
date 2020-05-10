"""
Helpers for interacting w/ APIs via requests
Useful for integration tests
"""
import pytest
import requests

BASE_URL = 'http://localhost:8000/api/training/'
DEFAULT_HEADERS = {'content-type': 'application/json'}


class ModelApiHelper:
    """
    Helper for submitting requests to a model API
    """

    def __init__(self, model_uri):
        self._model_uri = model_uri

    def fetch(self):
        """
        Helper to fetch model instances
        """
        req = requests.get('{}{}/'.format(BASE_URL, self._model_uri),
                           headers=DEFAULT_HEADERS)

        assert req.status_code == 200, 'Expected status 200, received {} - {}.'.format(
            req.status_code, req.content)
        return req.json()

    def update(self, model_id, data):
        """
        Helper to update a model instance
        """
        req = requests.patch(
            '{}{}/{}/'.format(BASE_URL, self._model_uri, model_id),
            headers=DEFAULT_HEADERS,
            json=data,
        )

        assert req.status_code == 200, 'Expected status 200, received {} - {}.'.format(
            req.status_code, req.content)
        return req.json()

    def create(self, data):
        """
        Helper to create a model instance
        """
        req = requests.post(
            '{}{}/'.format(BASE_URL, self._model_uri),
            headers=DEFAULT_HEADERS,
            json=data,
        )

        assert req.status_code == 201, 'Expected status 201, received {} - {}.'.format(
            req.status_code, req.content)
        return req.json()

    def delete(self, model_id):
        """
        Helper to delete a model instance
        """
        req = requests.delete(
            '{}{}/{}/'.format(BASE_URL, self._model_uri, model_id),
            headers=DEFAULT_HEADERS,
        )

        assert req.status_code == 204, 'Expected status 204, received {} - {}.'.format(
            req.status_code, req.content)


class ModelApiFixture:
    """
    Wraps ModelApiHelper to manage data created during test
    This tracks which instances have been created
    and provides a helper to delete them at the end of the test
    """

    def __init__(self, model_uri, request):
        self._api_helper = ModelApiHelper(model_uri)
        self._added_ids = []
        request.addfinalizer(self._remove_all_data)

    def fetch(self):
        """
        Helper to fetch model instances
        """
        return self._api_helper.fetch()

    def update(self, model_id, data):
        """
        Helper to update a model instance
        """
        return self._api_helper.update(model_id, data)

    def create(self, data):
        """
        Helper to create a model instance
        """
        result = self._api_helper.create(data)
        self._added_ids.append(result['id'])
        return result

    def delete(self, model_id):
        """
        Helper to delete a model instance
        """
        result = self._api_helper.delete(model_id)
        self._added_ids.remove(model_id)

    def _remove_all_data(self):
        for item_id in self._added_ids:
            try:
                self._api_helper.delete(item_id)
            except AssertionError as error:
                print(error)


@pytest.fixture()
def training_runs_fixture(request):
    return ModelApiFixture('training_runs', request)


@pytest.fixture()
def episodes_fixture(request):
    return ModelApiFixture('episodes', request)


@pytest.fixture()
def steps_fixture(request):
    return ModelApiFixture('steps', request)
