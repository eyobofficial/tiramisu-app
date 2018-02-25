from django.shortcuts import render
from django.generic.views import DetailView, ListView, TemplateView

# Import Mddels
from .models import (
    Catagory,
    Product,
)


class IndexView(TemplateView):
    """
    View for Index Page
    """
    pass


class CatagoryList(ListView):
    """
    View for listing all Product Catagory
    """
    model = Catagory


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
