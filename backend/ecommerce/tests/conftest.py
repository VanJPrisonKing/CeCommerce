from pytest_factoryboy import register
from rest_framework.test import APIClient
import pytest
from .factories import CategoryFactory, DemandFactory

register(CategoryFactory)
register(DemandFactory)


@pytest.fixture
def api_client():
    return APIClient
