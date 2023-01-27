from django.views.generic import ListView, DetailView

from products.models import (
    ProductInstance,
)


# Create your views here.
class ProductsListView(ListView):
    model = ProductInstance
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductsDetailView(DetailView):
    model = ProductInstance
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
