import pytest
import json

pytestmark = pytest.mark.django_db


class TestCateegoryEndpoints:
    endpoint = "/api/category/"

    def test_category_get(self, category_factory, api_client):
        # arrange
        category_factory.create_batch(4)
        # act
        response = api_client().get(self.endpoint)
        # assert
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4


class TestDemandEndpoints:
    endpoint = "/api/demand/"

    def test_demand_get(self, demand_factory, api_client):
        # arrange
        demand_factory.create_batch(5)
        # act
        response = api_client().get(self.endpoint)
        # assert
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 5
