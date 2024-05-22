import factory
from ecommerce.product.models import Category, Demand


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # name = "test_category"
    name = factory.Sequence(lambda n: "Category_%d" % n)


class DemandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Demand

    name = "test_demand"
    description = "test_desciption"
    is_digital = True
    category = factory.SubFactory(CategoryFactory)
