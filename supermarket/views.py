from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

# Import Mddels
from .models import (
    Catagory,
    Product,
)


class IndexView(TemplateView):
    """
    View for Index Page
    """
    template_name = 'supermarket/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['catagory_list'] = Catagory.objects.all()
        return context


class CatagoryList(ListView):
    """
    View for listing all Product Catagory
    """
    model = Catagory

    def get_context_data(self, *args, **kwargs):
        context = super(CatagoryList, self).get_context_data(*args, **kwargs)
        context['product_list'] = Product.objects.all()
        return context


class CatagoryDetail(DetailView):
    """
    View for a particular Product Catagory Detail
    """
    model = Catagory


class ProductList(ListView):
    """
    View for listing all Products
    """
    model = Product


class ProductDetail(DetailView):
    """
    View for a particular Product Detail
    """
    model = Product
