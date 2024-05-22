import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self, category_factory):
        # arrange
        # act
        x = category_factory(name="test_cat")
        # assert
        assert x.__str__() == "test_cat"

class TestDemandModel:
    def test_str_method(self, demand_factory):
        x = demand_factory(name="test_dmd")
        assert x.__str__() == "test_dmd"
